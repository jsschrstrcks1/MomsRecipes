#!/usr/bin/env python3
"""
Add nutrition data to ALL recipes lacking it.
Expands on add_muffin_nutrition.py with comprehensive ingredient database.
"""

import json
import re
import glob
from fractions import Fraction
from pathlib import Path

# =============================================================================
# COMPREHENSIVE NUTRITION DATABASE (USDA values)
# Format: {ingredient: {unit: {cal, fat, carbs, protein, sodium, fiber, sugar}}}
# =============================================================================

NUTRITION_DB = {
    # =========================================================================
    # WATER & LIQUIDS (0 or minimal calories)
    # =========================================================================
    "water": {"cup": {"cal": 0, "fat": 0, "carbs": 0, "protein": 0, "sodium": 0, "fiber": 0, "sugar": 0},
              "tbsp": {"cal": 0, "fat": 0, "carbs": 0, "protein": 0, "sodium": 0, "fiber": 0, "sugar": 0}},
    "ice": {"cup": {"cal": 0, "fat": 0, "carbs": 0, "protein": 0, "sodium": 0, "fiber": 0, "sugar": 0}},

    # =========================================================================
    # FLOURS & STARCHES
    # =========================================================================
    "all-purpose flour": {"cup": {"cal": 455, "fat": 1.2, "carbs": 95, "protein": 13, "sodium": 2, "fiber": 3.4, "sugar": 0.3},
                         "tbsp": {"cal": 28, "fat": 0.1, "carbs": 6, "protein": 0.8, "sodium": 0, "fiber": 0.2, "sugar": 0},
                         "oz": {"cal": 103, "fat": 0.3, "carbs": 22, "protein": 3, "sodium": 0, "fiber": 0.8, "sugar": 0.1},
                         "g": {"cal": 3.6, "fat": 0.01, "carbs": 0.76, "protein": 0.1, "sodium": 0, "fiber": 0.03, "sugar": 0}},
    "flour": {"cup": {"cal": 455, "fat": 1.2, "carbs": 95, "protein": 13, "sodium": 2, "fiber": 3.4, "sugar": 0.3},
             "tbsp": {"cal": 28, "fat": 0.1, "carbs": 6, "protein": 0.8, "sodium": 0, "fiber": 0.2, "sugar": 0},
             "oz": {"cal": 103, "fat": 0.3, "carbs": 22, "protein": 3, "sodium": 0, "fiber": 0.8, "sugar": 0.1},
             "g": {"cal": 3.6, "fat": 0.01, "carbs": 0.76, "protein": 0.1, "sodium": 0, "fiber": 0.03, "sugar": 0}},
    "whole wheat flour": {"cup": {"cal": 408, "fat": 2.2, "carbs": 87, "protein": 16, "sodium": 6, "fiber": 15, "sugar": 0.4},
                         "oz": {"cal": 97, "fat": 0.5, "carbs": 21, "protein": 4, "sodium": 1, "fiber": 3.6, "sugar": 0.1},
                         "g": {"cal": 3.4, "fat": 0.02, "carbs": 0.73, "protein": 0.13, "sodium": 0.05, "fiber": 0.13, "sugar": 0}},
    "bread flour": {"cup": {"cal": 495, "fat": 1.5, "carbs": 99, "protein": 16, "sodium": 2, "fiber": 3.4, "sugar": 0.3},
                   "oz": {"cal": 110, "fat": 0.3, "carbs": 22, "protein": 3.6, "sodium": 0, "fiber": 0.8, "sugar": 0.1},
                   "g": {"cal": 3.9, "fat": 0.01, "carbs": 0.78, "protein": 0.13, "sodium": 0, "fiber": 0.03, "sugar": 0}},
    "cake flour": {"cup": {"cal": 400, "fat": 1, "carbs": 88, "protein": 9, "sodium": 2, "fiber": 2, "sugar": 0.3}},
    "self-rising flour": {"cup": {"cal": 443, "fat": 1.2, "carbs": 93, "protein": 12, "sodium": 1520, "fiber": 3, "sugar": 0.3}},
    "almond flour": {"cup": {"cal": 640, "fat": 56, "carbs": 24, "protein": 24, "sodium": 0, "fiber": 12, "sugar": 4}},
    "coconut flour": {"cup": {"cal": 480, "fat": 16, "carbs": 64, "protein": 16, "sodium": 64, "fiber": 40, "sugar": 8}},
    "cornstarch": {"cup": {"cal": 488, "fat": 0.1, "carbs": 117, "protein": 0.3, "sodium": 12, "fiber": 1, "sugar": 0},
                  "tbsp": {"cal": 30, "fat": 0, "carbs": 7, "protein": 0, "sodium": 1, "fiber": 0, "sugar": 0}},
    "tapioca": {"cup": {"cal": 544, "fat": 0, "carbs": 135, "protein": 0, "sodium": 2, "fiber": 1, "sugar": 5},
               "tbsp": {"cal": 34, "fat": 0, "carbs": 8, "protein": 0, "sodium": 0, "fiber": 0, "sugar": 0}},
    "cornmeal": {"cup": {"cal": 442, "fat": 4, "carbs": 94, "protein": 10, "sodium": 43, "fiber": 9, "sugar": 1}},
    "masa harina": {"cup": {"cal": 416, "fat": 4, "carbs": 87, "protein": 11, "sodium": 6, "fiber": 7, "sugar": 1}},
    "chickpea flour": {"cup": {"cal": 356, "fat": 6, "carbs": 53, "protein": 21, "sodium": 59, "fiber": 10, "sugar": 10},
                      "oz": {"cal": 100, "fat": 1.7, "carbs": 15, "protein": 6, "sodium": 17, "fiber": 3, "sugar": 3}},
    "garbanzo bean flour": {"cup": {"cal": 356, "fat": 6, "carbs": 53, "protein": 21, "sodium": 59, "fiber": 10, "sugar": 10}},
    "semolina": {"cup": {"cal": 601, "fat": 1.8, "carbs": 122, "protein": 21, "sodium": 2, "fiber": 6.5, "sugar": 0},
                "oz": {"cal": 106, "fat": 0.3, "carbs": 22, "protein": 4, "sodium": 0, "fiber": 1, "sugar": 0}},
    "semolina flour": {"cup": {"cal": 601, "fat": 1.8, "carbs": 122, "protein": 21, "sodium": 2, "fiber": 6.5, "sugar": 0}},
    "rye flour": {"cup": {"cal": 361, "fat": 2, "carbs": 75, "protein": 11, "sodium": 2, "fiber": 15, "sugar": 1}},
    "whole wheat flour": {"cup": {"cal": 408, "fat": 2.2, "carbs": 87, "protein": 16, "sodium": 6, "fiber": 15, "sugar": 0.4},
                         "oz": {"cal": 96, "fat": 0.5, "carbs": 20, "protein": 4, "sodium": 1, "fiber": 3.5, "sugar": 0.1}},

    # =========================================================================
    # SUGARS & SWEETENERS
    # =========================================================================
    "sugar": {"cup": {"cal": 774, "fat": 0, "carbs": 200, "protein": 0, "sodium": 2, "fiber": 0, "sugar": 200},
             "tbsp": {"cal": 48, "fat": 0, "carbs": 12.5, "protein": 0, "sodium": 0, "fiber": 0, "sugar": 12.5},
             "tsp": {"cal": 16, "fat": 0, "carbs": 4, "protein": 0, "sodium": 0, "fiber": 0, "sugar": 4}},
    "brown sugar": {"cup": {"cal": 836, "fat": 0, "carbs": 216, "protein": 0, "sodium": 57, "fiber": 0, "sugar": 213},
                   "tbsp": {"cal": 52, "fat": 0, "carbs": 13.5, "protein": 0, "sodium": 4, "fiber": 0, "sugar": 13}},
    "powdered sugar": {"cup": {"cal": 467, "fat": 0, "carbs": 120, "protein": 0, "sodium": 1, "fiber": 0, "sugar": 117},
                       "tbsp": {"cal": 29, "fat": 0, "carbs": 7.5, "protein": 0, "sodium": 0, "fiber": 0, "sugar": 7.3},
                       "": {"cal": 29, "fat": 0, "carbs": 7.5, "protein": 0, "sodium": 0, "fiber": 0, "sugar": 7.3}},
    "honey": {"cup": {"cal": 1031, "fat": 0, "carbs": 279, "protein": 1, "sodium": 14, "fiber": 0, "sugar": 278},
             "tbsp": {"cal": 64, "fat": 0, "carbs": 17, "protein": 0, "sodium": 1, "fiber": 0, "sugar": 17}},
    "maple syrup": {"cup": {"cal": 840, "fat": 0.2, "carbs": 216, "protein": 0, "sodium": 27, "fiber": 0, "sugar": 192},
                   "tbsp": {"cal": 52, "fat": 0, "carbs": 13, "protein": 0, "sodium": 2, "fiber": 0, "sugar": 12}},
    "molasses": {"cup": {"cal": 977, "fat": 0, "carbs": 252, "protein": 0, "sodium": 121, "fiber": 0, "sugar": 183},
                "tbsp": {"cal": 58, "fat": 0, "carbs": 15, "protein": 0, "sodium": 7, "fiber": 0, "sugar": 11}},
    "corn syrup": {"cup": {"cal": 925, "fat": 0, "carbs": 251, "protein": 0, "sodium": 395, "fiber": 0, "sugar": 155},
                  "tbsp": {"cal": 57, "fat": 0, "carbs": 15.5, "protein": 0, "sodium": 24, "fiber": 0, "sugar": 9.5}},
    "agave": {"tbsp": {"cal": 60, "fat": 0, "carbs": 16, "protein": 0, "sodium": 0, "fiber": 0, "sugar": 15}},
    "stevia": {"tsp": {"cal": 0, "fat": 0, "carbs": 1, "protein": 0, "sodium": 0, "fiber": 0, "sugar": 0}},
    "splenda": {"tsp": {"cal": 0, "fat": 0, "carbs": 1, "protein": 0, "sodium": 0, "fiber": 0, "sugar": 0}},
    "caramels": {"": {"cal": 39, "fat": 0.8, "carbs": 8, "protein": 0.5, "sodium": 25, "fiber": 0, "sugar": 6},
                "cup": {"cal": 624, "fat": 13, "carbs": 128, "protein": 8, "sodium": 400, "fiber": 0, "sugar": 96}},
    "caramel": {"": {"cal": 39, "fat": 0.8, "carbs": 8, "protein": 0.5, "sodium": 25, "fiber": 0, "sugar": 6}},

    # =========================================================================
    # DAIRY
    # =========================================================================
    "milk": {"cup": {"cal": 149, "fat": 8, "carbs": 12, "protein": 8, "sodium": 105, "fiber": 0, "sugar": 12},
            "tbsp": {"cal": 9, "fat": 0.5, "carbs": 0.75, "protein": 0.5, "sodium": 7, "fiber": 0, "sugar": 0.75},
            "pint": {"cal": 298, "fat": 16, "carbs": 24, "protein": 16, "sodium": 210, "fiber": 0, "sugar": 24},
            "quart": {"cal": 596, "fat": 32, "carbs": 48, "protein": 32, "sodium": 420, "fiber": 0, "sugar": 48},
            "ml": {"cal": 0.63, "fat": 0.03, "carbs": 0.05, "protein": 0.03, "sodium": 0.44, "fiber": 0, "sugar": 0.05}},
    "skim milk": {"cup": {"cal": 83, "fat": 0.2, "carbs": 12, "protein": 8, "sodium": 103, "fiber": 0, "sugar": 12}},
    "evaporated milk": {"cup": {"cal": 338, "fat": 19, "carbs": 25, "protein": 17, "sodium": 267, "fiber": 0, "sugar": 25}},
    "sweetened condensed milk": {"cup": {"cal": 982, "fat": 27, "carbs": 166, "protein": 24, "sodium": 389, "fiber": 0, "sugar": 166}},
    "buttermilk": {"cup": {"cal": 99, "fat": 2.2, "carbs": 12, "protein": 8, "sodium": 257, "fiber": 0, "sugar": 12}},
    "heavy cream": {"cup": {"cal": 821, "fat": 88, "carbs": 7, "protein": 5, "sodium": 89, "fiber": 0, "sugar": 7},
                   "tbsp": {"cal": 51, "fat": 5.5, "carbs": 0.4, "protein": 0.3, "sodium": 6, "fiber": 0, "sugar": 0.4}},
    "half and half": {"cup": {"cal": 315, "fat": 28, "carbs": 10, "protein": 7, "sodium": 98, "fiber": 0, "sugar": 10},
                     "tbsp": {"cal": 20, "fat": 1.7, "carbs": 0.6, "protein": 0.4, "sodium": 6, "fiber": 0, "sugar": 0.6}},
    "sour cream": {"cup": {"cal": 444, "fat": 45, "carbs": 8, "protein": 5, "sodium": 108, "fiber": 0, "sugar": 5},
                  "tbsp": {"cal": 28, "fat": 2.8, "carbs": 0.5, "protein": 0.3, "sodium": 7, "fiber": 0, "sugar": 0.3}},
    "cream cheese": {"cup": {"cal": 793, "fat": 79, "carbs": 8, "protein": 14, "sodium": 691, "fiber": 0, "sugar": 6},
                    "oz": {"cal": 99, "fat": 10, "carbs": 1, "protein": 2, "sodium": 86, "fiber": 0, "sugar": 0.8},
                    "tbsp": {"cal": 50, "fat": 5, "carbs": 0.5, "protein": 1, "sodium": 43, "fiber": 0, "sugar": 0.4}},
    "yogurt": {"cup": {"cal": 149, "fat": 8, "carbs": 11, "protein": 9, "sodium": 113, "fiber": 0, "sugar": 11}},
    "greek yogurt": {"cup": {"cal": 190, "fat": 10, "carbs": 8, "protein": 18, "sodium": 65, "fiber": 0, "sugar": 7}},
    "cottage cheese": {"cup": {"cal": 220, "fat": 10, "carbs": 8, "protein": 25, "sodium": 819, "fiber": 0, "sugar": 5}},
    "ricotta cheese": {"cup": {"cal": 428, "fat": 32, "carbs": 7, "protein": 28, "sodium": 307, "fiber": 0, "sugar": 0.5}},
    "cheddar cheese": {"cup": {"cal": 455, "fat": 37, "carbs": 1, "protein": 28, "sodium": 702, "fiber": 0, "sugar": 0.5},
                      "oz": {"cal": 113, "fat": 9, "carbs": 0.3, "protein": 7, "sodium": 175, "fiber": 0, "sugar": 0.1},
                      "g": {"cal": 4.0, "fat": 0.33, "carbs": 0.01, "protein": 0.25, "sodium": 6.2, "fiber": 0, "sugar": 0}},
    "parmesan cheese": {"cup": {"cal": 431, "fat": 29, "carbs": 4, "protein": 38, "sodium": 1529, "fiber": 0, "sugar": 1},
                       "tbsp": {"cal": 22, "fat": 1.4, "carbs": 0.2, "protein": 2, "sodium": 76, "fiber": 0, "sugar": 0},
                       "g": {"cal": 3.9, "fat": 0.26, "carbs": 0.03, "protein": 0.34, "sodium": 13.9, "fiber": 0, "sugar": 0}},
    "mozzarella cheese": {"cup": {"cal": 336, "fat": 25, "carbs": 2, "protein": 25, "sodium": 627, "fiber": 0, "sugar": 1},
                         "oz": {"cal": 84, "fat": 6, "carbs": 0.6, "protein": 6, "sodium": 157, "fiber": 0, "sugar": 0.2}},
    "swiss cheese": {"cup": {"cal": 420, "fat": 31, "carbs": 6, "protein": 30, "sodium": 228, "fiber": 0, "sugar": 2},
                    "oz": {"cal": 106, "fat": 8, "carbs": 1.5, "protein": 8, "sodium": 54, "fiber": 0, "sugar": 0.4}},
    "american cheese": {"slice": {"cal": 94, "fat": 7, "carbs": 2, "protein": 5, "sodium": 274, "fiber": 0, "sugar": 1}},
    "provolone cheese": {"slice": {"cal": 98, "fat": 7, "carbs": 0.6, "protein": 7, "sodium": 248, "fiber": 0, "sugar": 0.2},
                        "oz": {"cal": 98, "fat": 7, "carbs": 0.6, "protein": 7, "sodium": 248, "fiber": 0, "sugar": 0.2}},
    "velveeta": {"oz": {"cal": 80, "fat": 6, "carbs": 3, "protein": 4, "sodium": 410, "fiber": 0, "sugar": 2}},
    "whipped cream": {"cup": {"cal": 240, "fat": 22, "carbs": 7, "protein": 3, "sodium": 60, "fiber": 0, "sugar": 7},
                     "tbsp": {"cal": 15, "fat": 1.4, "carbs": 0.4, "protein": 0.2, "sodium": 4, "fiber": 0, "sugar": 0.4}},

    # =========================================================================
    # FATS & OILS
    # =========================================================================
    "butter": {"cup": {"cal": 1628, "fat": 184, "carbs": 0, "protein": 2, "sodium": 1246, "fiber": 0, "sugar": 0},
              "tbsp": {"cal": 102, "fat": 11.5, "carbs": 0, "protein": 0.1, "sodium": 78, "fiber": 0, "sugar": 0},
              "tsp": {"cal": 34, "fat": 4, "carbs": 0, "protein": 0, "sodium": 26, "fiber": 0, "sugar": 0},
              "": {"cal": 102, "fat": 11.5, "carbs": 0, "protein": 0.1, "sodium": 78, "fiber": 0, "sugar": 0}},
    "margarine": {"tbsp": {"cal": 100, "fat": 11, "carbs": 0, "protein": 0, "sodium": 90, "fiber": 0, "sugar": 0},
                  "stick": {"cal": 810, "fat": 91, "carbs": 1, "protein": 1, "sodium": 800, "fiber": 0, "sugar": 0},
                  "": {"cal": 100, "fat": 11, "carbs": 0, "protein": 0, "sodium": 90, "fiber": 0, "sugar": 0}},
    "oleo": {"tbsp": {"cal": 100, "fat": 11, "carbs": 0, "protein": 0, "sodium": 90, "fiber": 0, "sugar": 0},
             "stick": {"cal": 810, "fat": 91, "carbs": 1, "protein": 1, "sodium": 800, "fiber": 0, "sugar": 0},
             "": {"cal": 100, "fat": 11, "carbs": 0, "protein": 0, "sodium": 90, "fiber": 0, "sugar": 0}},
    "vegetable oil": {"cup": {"cal": 1927, "fat": 218, "carbs": 0, "protein": 0, "sodium": 0, "fiber": 0, "sugar": 0},
                     "tbsp": {"cal": 120, "fat": 14, "carbs": 0, "protein": 0, "sodium": 0, "fiber": 0, "sugar": 0},
                     "": {"cal": 120, "fat": 14, "carbs": 0, "protein": 0, "sodium": 0, "fiber": 0, "sugar": 0}},
    "olive oil": {"cup": {"cal": 1909, "fat": 216, "carbs": 0, "protein": 0, "sodium": 0, "fiber": 0, "sugar": 0},
                 "tbsp": {"cal": 119, "fat": 14, "carbs": 0, "protein": 0, "sodium": 0, "fiber": 0, "sugar": 0}},
    "coconut oil": {"tbsp": {"cal": 117, "fat": 14, "carbs": 0, "protein": 0, "sodium": 0, "fiber": 0, "sugar": 0}},
    "shortening": {"cup": {"cal": 1812, "fat": 205, "carbs": 0, "protein": 0, "sodium": 0, "fiber": 0, "sugar": 0},
                  "tbsp": {"cal": 113, "fat": 13, "carbs": 0, "protein": 0, "sodium": 0, "fiber": 0, "sugar": 0}},
    "lard": {"cup": {"cal": 1849, "fat": 205, "carbs": 0, "protein": 0, "sodium": 0, "fiber": 0, "sugar": 0},
            "tbsp": {"cal": 115, "fat": 13, "carbs": 0, "protein": 0, "sodium": 0, "fiber": 0, "sugar": 0}},
    "mayonnaise": {"cup": {"cal": 1440, "fat": 160, "carbs": 0, "protein": 2, "sodium": 1250, "fiber": 0, "sugar": 0},
                  "tbsp": {"cal": 90, "fat": 10, "carbs": 0, "protein": 0.1, "sodium": 78, "fiber": 0, "sugar": 0}},
    "bacon grease": {"tbsp": {"cal": 116, "fat": 13, "carbs": 0, "protein": 0, "sodium": 19, "fiber": 0, "sugar": 0}},

    # =========================================================================
    # EGGS
    # =========================================================================
    "egg": {"": {"cal": 72, "fat": 5, "carbs": 0.4, "protein": 6, "sodium": 71, "fiber": 0, "sugar": 0.4}},
    "large egg": {"": {"cal": 72, "fat": 5, "carbs": 0.4, "protein": 6, "sodium": 71, "fiber": 0, "sugar": 0.4}},
    "eggs": {"": {"cal": 72, "fat": 5, "carbs": 0.4, "protein": 6, "sodium": 71, "fiber": 0, "sugar": 0.4}},
    "egg white": {"": {"cal": 17, "fat": 0, "carbs": 0.2, "protein": 4, "sodium": 55, "fiber": 0, "sugar": 0.2}},
    "egg yolk": {"": {"cal": 55, "fat": 5, "carbs": 0.6, "protein": 3, "sodium": 8, "fiber": 0, "sugar": 0.1}},

    # =========================================================================
    # MEATS - POULTRY
    # =========================================================================
    "chicken breast": {"lb": {"cal": 748, "fat": 16, "carbs": 0, "protein": 140, "sodium": 340, "fiber": 0, "sugar": 0},
                      "": {"cal": 187, "fat": 4, "carbs": 0, "protein": 35, "sodium": 85, "fiber": 0, "sugar": 0}},
    "chicken thigh": {"lb": {"cal": 980, "fat": 54, "carbs": 0, "protein": 115, "sodium": 422, "fiber": 0, "sugar": 0},
                     "": {"cal": 206, "fat": 11, "carbs": 0, "protein": 24, "sodium": 88, "fiber": 0, "sugar": 0}},
    "chicken": {"lb": {"cal": 880, "fat": 40, "carbs": 0, "protein": 120, "sodium": 380, "fiber": 0, "sugar": 0},
               "cup": {"cal": 231, "fat": 10, "carbs": 0, "protein": 32, "sodium": 100, "fiber": 0, "sugar": 0}},
    "ground chicken": {"lb": {"cal": 748, "fat": 36, "carbs": 0, "protein": 100, "sodium": 340, "fiber": 0, "sugar": 0}},
    "turkey": {"lb": {"cal": 720, "fat": 32, "carbs": 0, "protein": 104, "sodium": 300, "fiber": 0, "sugar": 0},
              "cup": {"cal": 190, "fat": 8, "carbs": 0, "protein": 27, "sodium": 79, "fiber": 0, "sugar": 0}},
    "ground turkey": {"lb": {"cal": 752, "fat": 36, "carbs": 0, "protein": 100, "sodium": 340, "fiber": 0, "sugar": 0}},

    # =========================================================================
    # MEATS - BEEF
    # =========================================================================
    "ground beef": {"lb": {"cal": 1152, "fat": 88, "carbs": 0, "protein": 80, "sodium": 304, "fiber": 0, "sugar": 0}},
    "lean ground beef": {"lb": {"cal": 816, "fat": 48, "carbs": 0, "protein": 92, "sodium": 320, "fiber": 0, "sugar": 0}},
    "beef": {"lb": {"cal": 1000, "fat": 68, "carbs": 0, "protein": 92, "sodium": 280, "fiber": 0, "sugar": 0},
            "cup": {"cal": 263, "fat": 18, "carbs": 0, "protein": 24, "sodium": 74, "fiber": 0, "sugar": 0}},
    "steak": {"lb": {"cal": 880, "fat": 52, "carbs": 0, "protein": 100, "sodium": 260, "fiber": 0, "sugar": 0},
             "oz": {"cal": 55, "fat": 3.3, "carbs": 0, "protein": 6, "sodium": 16, "fiber": 0, "sugar": 0}},
    "roast beef": {"lb": {"cal": 800, "fat": 40, "carbs": 0, "protein": 108, "sodium": 272, "fiber": 0, "sugar": 0}},
    "beef stew meat": {"lb": {"cal": 720, "fat": 32, "carbs": 0, "protein": 108, "sodium": 280, "fiber": 0, "sugar": 0}},
    "corned beef": {"lb": {"cal": 880, "fat": 56, "carbs": 2, "protein": 88, "sodium": 3840, "fiber": 0, "sugar": 0}},

    # =========================================================================
    # MEATS - PORK
    # =========================================================================
    "pork": {"lb": {"cal": 1016, "fat": 60, "carbs": 0, "protein": 112, "sodium": 260, "fiber": 0, "sugar": 0}},
    "pork chop": {"": {"cal": 231, "fat": 13, "carbs": 0, "protein": 26, "sodium": 62, "fiber": 0, "sugar": 0}},
    "pork loin": {"lb": {"cal": 680, "fat": 24, "carbs": 0, "protein": 116, "sodium": 280, "fiber": 0, "sugar": 0}},
    "pork tenderloin": {"lb": {"cal": 544, "fat": 12, "carbs": 0, "protein": 104, "sodium": 240, "fiber": 0, "sugar": 0}},
    "bacon": {"slice": {"cal": 43, "fat": 3, "carbs": 0, "protein": 3, "sodium": 137, "fiber": 0, "sugar": 0},
             "strip": {"cal": 43, "fat": 3, "carbs": 0, "protein": 3, "sodium": 137, "fiber": 0, "sugar": 0},
             "strips": {"cal": 43, "fat": 3, "carbs": 0, "protein": 3, "sodium": 137, "fiber": 0, "sugar": 0},
             "lb": {"cal": 2420, "fat": 232, "carbs": 0, "protein": 60, "sodium": 3040, "fiber": 0, "sugar": 0}},
    "ham": {"cup": {"cal": 207, "fat": 11, "carbs": 2, "protein": 24, "sodium": 1684, "fiber": 0, "sugar": 0},
           "lb": {"cal": 620, "fat": 32, "carbs": 4, "protein": 80, "sodium": 5050, "fiber": 0, "sugar": 0}},
    "sausage": {"link": {"cal": 82, "fat": 7, "carbs": 0.5, "protein": 4, "sodium": 192, "fiber": 0, "sugar": 0},
               "lb": {"cal": 1148, "fat": 100, "carbs": 4, "protein": 56, "sodium": 2840, "fiber": 0, "sugar": 0}},
    "italian sausage": {"link": {"cal": 125, "fat": 10, "carbs": 1, "protein": 8, "sodium": 380, "fiber": 0, "sugar": 0}},
    "ground pork": {"lb": {"cal": 1200, "fat": 92, "carbs": 0, "protein": 80, "sodium": 280, "fiber": 0, "sugar": 0}},

    # =========================================================================
    # SEAFOOD
    # =========================================================================
    "shrimp": {"lb": {"cal": 480, "fat": 8, "carbs": 4, "protein": 92, "sodium": 800, "fiber": 0, "sugar": 0},
              "cup": {"cal": 120, "fat": 2, "carbs": 1, "protein": 23, "sodium": 200, "fiber": 0, "sugar": 0},
              "": {"cal": 7, "fat": 0.1, "carbs": 0, "protein": 1.5, "sodium": 13, "fiber": 0, "sugar": 0}},
    "chipotle pepper": {"": {"cal": 4, "fat": 0, "carbs": 1, "protein": 0.2, "sodium": 100, "fiber": 0.3, "sugar": 0.5},
                       "tbsp": {"cal": 17, "fat": 0.5, "carbs": 3, "protein": 0.5, "sodium": 400, "fiber": 1, "sugar": 2}},
    "salmon": {"lb": {"cal": 936, "fat": 56, "carbs": 0, "protein": 104, "sodium": 260, "fiber": 0, "sugar": 0},
              "oz": {"cal": 59, "fat": 3.5, "carbs": 0, "protein": 6.5, "sodium": 16, "fiber": 0, "sugar": 0}},
    "trout": {"lb": {"cal": 680, "fat": 28, "carbs": 0, "protein": 104, "sodium": 260, "fiber": 0, "sugar": 0},
              "oz": {"cal": 43, "fat": 1.8, "carbs": 0, "protein": 6.5, "sodium": 16, "fiber": 0, "sugar": 0},
              "fillet": {"cal": 215, "fat": 9, "carbs": 0, "protein": 33, "sodium": 81, "fiber": 0, "sugar": 0},
              "fillets": {"cal": 215, "fat": 9, "carbs": 0, "protein": 33, "sodium": 81, "fiber": 0, "sugar": 0}},
    "tuna": {"can": {"cal": 179, "fat": 1, "carbs": 0, "protein": 40, "sodium": 558, "fiber": 0, "sugar": 0},
            "cup": {"cal": 179, "fat": 1, "carbs": 0, "protein": 40, "sodium": 558, "fiber": 0, "sugar": 0}},
    "cod": {"lb": {"cal": 372, "fat": 4, "carbs": 0, "protein": 80, "sodium": 280, "fiber": 0, "sugar": 0}},
    "tilapia": {"lb": {"cal": 436, "fat": 8, "carbs": 0, "protein": 92, "sodium": 232, "fiber": 0, "sugar": 0}},
    "crab": {"cup": {"cal": 97, "fat": 2, "carbs": 0, "protein": 19, "sodium": 911, "fiber": 0, "sugar": 0}},
    "crabmeat": {"oz": {"cal": 25, "fat": 0.4, "carbs": 0, "protein": 5, "sodium": 95, "fiber": 0, "sugar": 0}},
    "clams": {"cup": {"cal": 168, "fat": 2, "carbs": 6, "protein": 29, "sodium": 127, "fiber": 0, "sugar": 0},
             "can": {"cal": 120, "fat": 1.5, "carbs": 4, "protein": 20, "sodium": 350, "fiber": 0, "sugar": 0},
             "oz": {"cal": 21, "fat": 0.3, "carbs": 0.8, "protein": 4, "sodium": 16, "fiber": 0, "sugar": 0}},
    "lobster": {"cup": {"cal": 142, "fat": 1, "carbs": 2, "protein": 30, "sodium": 705, "fiber": 0, "sugar": 0}},
    "anchovies": {"can": {"cal": 94, "fat": 4, "carbs": 0, "protein": 13, "sodium": 1651, "fiber": 0, "sugar": 0}},
    "swordfish": {"oz": {"cal": 41, "fat": 1.4, "carbs": 0, "protein": 6.7, "sodium": 30, "fiber": 0, "sugar": 0}},
    "red snapper": {"oz": {"cal": 28, "fat": 0.4, "carbs": 0, "protein": 5.8, "sodium": 18, "fiber": 0, "sugar": 0}},
    "cornish hen": {"": {"cal": 500, "fat": 28, "carbs": 0, "protein": 60, "sodium": 200, "fiber": 0, "sugar": 0}},
    "corned beef": {"oz": {"cal": 71, "fat": 5.4, "carbs": 0.4, "protein": 5, "sodium": 285, "fiber": 0, "sugar": 0}},
    "sirloin": {"lb": {"cal": 880, "fat": 48, "carbs": 0, "protein": 104, "sodium": 280, "fiber": 0, "sugar": 0}},
    "round steak": {"lb": {"cal": 720, "fat": 24, "carbs": 0, "protein": 120, "sodium": 240, "fiber": 0, "sugar": 0}},
    "pot roast": {"lb": {"cal": 880, "fat": 52, "carbs": 0, "protein": 100, "sodium": 280, "fiber": 0, "sugar": 0}},
    "stew meat": {"lb": {"cal": 880, "fat": 52, "carbs": 0, "protein": 100, "sodium": 280, "fiber": 0, "sugar": 0}},
    "salami": {"oz": {"cal": 119, "fat": 10, "carbs": 0.5, "protein": 6, "sodium": 529, "fiber": 0, "sugar": 0}},

    # =========================================================================
    # CANNED GOODS & PREPARED FOODS
    # =========================================================================
    "cream of chicken soup": {"can": {"cal": 225, "fat": 14, "carbs": 18, "protein": 6, "sodium": 1800, "fiber": 0, "sugar": 2}},
    "cream of mushroom soup": {"can": {"cal": 200, "fat": 13, "carbs": 15, "protein": 4, "sodium": 1700, "fiber": 1, "sugar": 2}},
    "cream of celery soup": {"can": {"cal": 180, "fat": 11, "carbs": 17, "protein": 3, "sodium": 1650, "fiber": 1, "sugar": 2}},
    "tomato soup": {"can": {"cal": 161, "fat": 4, "carbs": 28, "protein": 4, "sodium": 1410, "fiber": 3, "sugar": 19}},
    "chicken broth": {"cup": {"cal": 15, "fat": 0.5, "carbs": 1, "protein": 2, "sodium": 860, "fiber": 0, "sugar": 0},
                     "can": {"cal": 30, "fat": 1, "carbs": 2, "protein": 4, "sodium": 1720, "fiber": 0, "sugar": 0}},
    "beef broth": {"cup": {"cal": 17, "fat": 0.5, "carbs": 1, "protein": 3, "sodium": 890, "fiber": 0, "sugar": 0},
                  "can": {"cal": 34, "fat": 1, "carbs": 2, "protein": 6, "sodium": 1780, "fiber": 0, "sugar": 0}},
    "vegetable broth": {"cup": {"cal": 12, "fat": 0, "carbs": 3, "protein": 0, "sodium": 700, "fiber": 0, "sugar": 1}},
    "bouillon cube": {"": {"cal": 5, "fat": 0, "carbs": 1, "protein": 0.5, "sodium": 900, "fiber": 0, "sugar": 0}},
    "chicken bouillon cube": {"": {"cal": 5, "fat": 0, "carbs": 1, "protein": 0.5, "sodium": 900, "fiber": 0, "sugar": 0}},
    "beef bouillon cube": {"": {"cal": 5, "fat": 0, "carbs": 1, "protein": 0.5, "sodium": 900, "fiber": 0, "sugar": 0}},
    "bouillon": {"cube": {"cal": 5, "fat": 0, "carbs": 1, "protein": 0.5, "sodium": 900, "fiber": 0, "sugar": 0}},
    "tomato paste": {"can": {"cal": 139, "fat": 1, "carbs": 32, "protein": 7, "sodium": 170, "fiber": 7, "sugar": 21},
                    "tbsp": {"cal": 13, "fat": 0.1, "carbs": 3, "protein": 0.7, "sodium": 16, "fiber": 0.7, "sugar": 2}},
    "tomato sauce": {"cup": {"cal": 59, "fat": 0.4, "carbs": 13, "protein": 3, "sodium": 1116, "fiber": 4, "sugar": 8},
                    "can": {"cal": 89, "fat": 0.6, "carbs": 20, "protein": 4, "sodium": 1674, "fiber": 6, "sugar": 12}},
    "marinara sauce": {"cup": {"cal": 128, "fat": 4, "carbs": 20, "protein": 3, "sodium": 940, "fiber": 4, "sugar": 11},
                      "can": {"cal": 192, "fat": 6, "carbs": 30, "protein": 4.5, "sodium": 1410, "fiber": 6, "sugar": 16}},
    "spaghetti sauce": {"cup": {"cal": 128, "fat": 4, "carbs": 20, "protein": 3, "sodium": 940, "fiber": 4, "sugar": 11},
                       "can": {"cal": 192, "fat": 6, "carbs": 30, "protein": 4.5, "sodium": 1410, "fiber": 6, "sugar": 16}},
    "stewed tomatoes": {"can": {"cal": 66, "fat": 0.4, "carbs": 16, "protein": 3, "sodium": 564, "fiber": 4, "sugar": 9}},
    "diced tomatoes": {"can": {"cal": 66, "fat": 0.4, "carbs": 16, "protein": 3, "sodium": 564, "fiber": 4, "sugar": 9}},
    "crushed tomatoes": {"can": {"cal": 70, "fat": 0.5, "carbs": 16, "protein": 3, "sodium": 600, "fiber": 4, "sugar": 10}},
    "canned tomatoes": {"can": {"cal": 66, "fat": 0.4, "carbs": 16, "protein": 3, "sodium": 564, "fiber": 4, "sugar": 9}},
    "salsa": {"cup": {"cal": 70, "fat": 0.3, "carbs": 15, "protein": 3, "sodium": 1990, "fiber": 4, "sugar": 8},
             "can": {"cal": 140, "fat": 0.6, "carbs": 30, "protein": 6, "sodium": 3980, "fiber": 8, "sugar": 16},
             "oz": {"cal": 9, "fat": 0, "carbs": 2, "protein": 0.4, "sodium": 249, "fiber": 0.5, "sugar": 1}},
    "enchilada sauce": {"cup": {"cal": 60, "fat": 1, "carbs": 11, "protein": 2, "sodium": 1160, "fiber": 2, "sugar": 4}},
    "black beans": {"can": {"cal": 339, "fat": 1, "carbs": 61, "protein": 22, "sodium": 660, "fiber": 15, "sugar": 1},
                   "cup": {"cal": 227, "fat": 0.9, "carbs": 41, "protein": 15, "sodium": 440, "fiber": 10, "sugar": 0.5}},
    "kidney beans": {"can": {"cal": 330, "fat": 1, "carbs": 58, "protein": 23, "sodium": 880, "fiber": 16, "sugar": 3}},
    "pinto beans": {"can": {"cal": 320, "fat": 1, "carbs": 56, "protein": 20, "sodium": 620, "fiber": 15, "sugar": 1}},
    "refried beans": {"cup": {"cal": 237, "fat": 3, "carbs": 39, "protein": 14, "sodium": 1069, "fiber": 11, "sugar": 1}},
    "baked beans": {"cup": {"cal": 266, "fat": 1, "carbs": 52, "protein": 12, "sodium": 928, "fiber": 10, "sugar": 22}},
    "green beans": {"can": {"cal": 44, "fat": 0.3, "carbs": 10, "protein": 2, "sodium": 620, "fiber": 4, "sugar": 2},
                   "cup": {"cal": 31, "fat": 0.2, "carbs": 7, "protein": 2, "sodium": 6, "fiber": 3, "sugar": 3}},
    "corn": {"can": {"cal": 210, "fat": 2, "carbs": 50, "protein": 6, "sodium": 600, "fiber": 4, "sugar": 12},
            "cup": {"cal": 132, "fat": 2, "carbs": 29, "protein": 5, "sodium": 1, "fiber": 4, "sugar": 5},
            "ear": {"cal": 77, "fat": 1, "carbs": 17, "protein": 3, "sodium": 1, "fiber": 2, "sugar": 3}},
    "cream-style corn": {"can": {"cal": 184, "fat": 1, "carbs": 46, "protein": 4, "sodium": 730, "fiber": 3, "sugar": 11}},
    "peas": {"cup": {"cal": 117, "fat": 0.6, "carbs": 21, "protein": 8, "sodium": 7, "fiber": 7, "sugar": 8},
            "can": {"cal": 175, "fat": 0.9, "carbs": 31, "protein": 12, "sodium": 800, "fiber": 10, "sugar": 12}},
    "mushrooms": {"can": {"cal": 39, "fat": 0.5, "carbs": 8, "protein": 3, "sodium": 660, "fiber": 4, "sugar": 2},
                 "cup": {"cal": 15, "fat": 0.2, "carbs": 2, "protein": 2, "sodium": 4, "fiber": 0.7, "sugar": 1},
                 "oz": {"cal": 6, "fat": 0.1, "carbs": 0.9, "protein": 0.9, "sodium": 1, "fiber": 0.3, "sugar": 0.6}},
    "olives": {"cup": {"cal": 155, "fat": 14, "carbs": 8, "protein": 1, "sodium": 1556, "fiber": 3, "sugar": 0}},
    "coconut milk": {"cup": {"cal": 445, "fat": 48, "carbs": 6, "protein": 5, "sodium": 29, "fiber": 0, "sugar": 6}},
    "pumpkin puree": {"cup": {"cal": 83, "fat": 0.7, "carbs": 20, "protein": 3, "sodium": 12, "fiber": 7, "sugar": 8}},
    "green chiles": {"can": {"cal": 30, "fat": 0, "carbs": 6, "protein": 1, "sodium": 400, "fiber": 2, "sugar": 3},
                    "cup": {"cal": 30, "fat": 0, "carbs": 6, "protein": 1, "sodium": 400, "fiber": 2, "sugar": 3}},
    "diced green chiles": {"can": {"cal": 30, "fat": 0, "carbs": 6, "protein": 1, "sodium": 400, "fiber": 2, "sugar": 3}},
    "chopped green chiles": {"can": {"cal": 30, "fat": 0, "carbs": 6, "protein": 1, "sodium": 400, "fiber": 2, "sugar": 3}},

    # =========================================================================
    # VEGETABLES
    # =========================================================================
    "onion": {"cup": {"cal": 64, "fat": 0.2, "carbs": 15, "protein": 2, "sodium": 6, "fiber": 3, "sugar": 7},
             "medium": {"cal": 44, "fat": 0.1, "carbs": 10, "protein": 1, "sodium": 4, "fiber": 2, "sugar": 5},
             "small": {"cal": 28, "fat": 0.1, "carbs": 7, "protein": 0.8, "sodium": 3, "fiber": 1, "sugar": 3},
             "large": {"cal": 60, "fat": 0.2, "carbs": 14, "protein": 1.5, "sodium": 5, "fiber": 2.5, "sugar": 6},
             "": {"cal": 44, "fat": 0.1, "carbs": 10, "protein": 1, "sodium": 4, "fiber": 2, "sugar": 5}},
    "green onion": {"cup": {"cal": 32, "fat": 0.2, "carbs": 7, "protein": 2, "sodium": 16, "fiber": 3, "sugar": 2},
                   "": {"cal": 5, "fat": 0, "carbs": 1, "protein": 0.3, "sodium": 2, "fiber": 0.4, "sugar": 0.4}},
    "garlic": {"clove": {"cal": 4, "fat": 0, "carbs": 1, "protein": 0.2, "sodium": 1, "fiber": 0.1, "sugar": 0},
              "cloves": {"cal": 4, "fat": 0, "carbs": 1, "protein": 0.2, "sodium": 1, "fiber": 0.1, "sugar": 0},
              "tbsp": {"cal": 13, "fat": 0, "carbs": 3, "protein": 0.6, "sodium": 2, "fiber": 0.2, "sugar": 0},
              "tsp": {"cal": 4, "fat": 0, "carbs": 1, "protein": 0.2, "sodium": 1, "fiber": 0.1, "sugar": 0},
              "": {"cal": 4, "fat": 0, "carbs": 1, "protein": 0.2, "sodium": 1, "fiber": 0.1, "sugar": 0}},
    "celery": {"cup": {"cal": 16, "fat": 0.2, "carbs": 3, "protein": 0.7, "sodium": 80, "fiber": 2, "sugar": 1},
              "stalk": {"cal": 6, "fat": 0.1, "carbs": 1, "protein": 0.3, "sodium": 32, "fiber": 0.6, "sugar": 0.5}},
    "carrot": {"cup": {"cal": 52, "fat": 0.3, "carbs": 12, "protein": 1, "sodium": 88, "fiber": 4, "sugar": 6},
              "medium": {"cal": 25, "fat": 0.1, "carbs": 6, "protein": 0.6, "sodium": 42, "fiber": 2, "sugar": 3},
              "": {"cal": 25, "fat": 0.1, "carbs": 6, "protein": 0.6, "sodium": 42, "fiber": 2, "sugar": 3}},
    "bell pepper": {"cup": {"cal": 30, "fat": 0.3, "carbs": 6, "protein": 1, "sodium": 4, "fiber": 2, "sugar": 4},
                   "medium": {"cal": 24, "fat": 0.2, "carbs": 5, "protein": 0.8, "sodium": 3, "fiber": 1.5, "sugar": 3},
                   "": {"cal": 24, "fat": 0.2, "carbs": 5, "protein": 0.8, "sodium": 3, "fiber": 1.5, "sugar": 3}},
    "green pepper": {"cup": {"cal": 30, "fat": 0.3, "carbs": 6, "protein": 1, "sodium": 4, "fiber": 2, "sugar": 4},
                    "": {"cal": 24, "fat": 0.2, "carbs": 5, "protein": 0.8, "sodium": 3, "fiber": 1.5, "sugar": 3}},
    "red pepper": {"cup": {"cal": 39, "fat": 0.4, "carbs": 9, "protein": 1, "sodium": 5, "fiber": 3, "sugar": 6}},
    "jalapeno": {"": {"cal": 4, "fat": 0, "carbs": 1, "protein": 0.1, "sodium": 0, "fiber": 0.4, "sugar": 0.5}},
    "green chiles": {"cup": {"cal": 30, "fat": 0.2, "carbs": 7, "protein": 1, "sodium": 552, "fiber": 1.5, "sugar": 4},
                    "can": {"cal": 15, "fat": 0.1, "carbs": 3, "protein": 0.5, "sodium": 276, "fiber": 0.8, "sugar": 2},
                    "oz": {"cal": 4, "fat": 0, "carbs": 0.9, "protein": 0.1, "sodium": 69, "fiber": 0.2, "sugar": 0.5}},
    "poblano pepper": {"": {"cal": 48, "fat": 0.4, "carbs": 9, "protein": 2, "sodium": 7, "fiber": 4, "sugar": 5}},
    "anaheim pepper": {"": {"cal": 10, "fat": 0.1, "carbs": 2, "protein": 0.4, "sodium": 2, "fiber": 0.8, "sugar": 1}},
    "tomato": {"cup": {"cal": 32, "fat": 0.4, "carbs": 7, "protein": 2, "sodium": 9, "fiber": 2, "sugar": 5},
              "medium": {"cal": 22, "fat": 0.2, "carbs": 5, "protein": 1, "sodium": 6, "fiber": 1.5, "sugar": 3},
              "": {"cal": 22, "fat": 0.2, "carbs": 5, "protein": 1, "sodium": 6, "fiber": 1.5, "sugar": 3}},
    "potato": {"medium": {"cal": 163, "fat": 0.2, "carbs": 37, "protein": 4, "sodium": 13, "fiber": 4, "sugar": 2},
              "cup": {"cal": 116, "fat": 0.1, "carbs": 26, "protein": 3, "sodium": 9, "fiber": 3, "sugar": 1},
              "lb": {"cal": 354, "fat": 0.4, "carbs": 80, "protein": 9, "sodium": 28, "fiber": 9, "sugar": 4},
              "": {"cal": 163, "fat": 0.2, "carbs": 37, "protein": 4, "sodium": 13, "fiber": 4, "sugar": 2}},
    "sweet potato": {"cup": {"cal": 114, "fat": 0.1, "carbs": 27, "protein": 2, "sodium": 73, "fiber": 4, "sugar": 6},
                    "medium": {"cal": 103, "fat": 0.1, "carbs": 24, "protein": 2, "sodium": 41, "fiber": 4, "sugar": 7},
                    "": {"cal": 103, "fat": 0.1, "carbs": 24, "protein": 2, "sodium": 41, "fiber": 4, "sugar": 7}},
    "broccoli": {"cup": {"cal": 31, "fat": 0.3, "carbs": 6, "protein": 3, "sodium": 30, "fiber": 2, "sugar": 2}},
    "cauliflower": {"cup": {"cal": 27, "fat": 0.3, "carbs": 5, "protein": 2, "sodium": 32, "fiber": 2, "sugar": 2}},
    "spinach": {"cup": {"cal": 7, "fat": 0.1, "carbs": 1, "protein": 1, "sodium": 24, "fiber": 0.7, "sugar": 0.1}},
    "lettuce": {"cup": {"cal": 5, "fat": 0.1, "carbs": 1, "protein": 0.5, "sodium": 5, "fiber": 0.5, "sugar": 0.5}},
    "cabbage": {"cup": {"cal": 22, "fat": 0.1, "carbs": 5, "protein": 1, "sodium": 16, "fiber": 2, "sugar": 3},
               "head": {"cal": 218, "fat": 1, "carbs": 52, "protein": 11, "sodium": 164, "fiber": 22, "sugar": 28},
               "medium": {"cal": 218, "fat": 1, "carbs": 52, "protein": 11, "sodium": 164, "fiber": 22, "sugar": 28}},
    "zucchini": {"cup": {"cal": 19, "fat": 0.2, "carbs": 4, "protein": 1, "sodium": 12, "fiber": 1, "sugar": 3},
                "medium": {"cal": 33, "fat": 0.4, "carbs": 6, "protein": 2, "sodium": 20, "fiber": 2, "sugar": 5}},
    "squash": {"cup": {"cal": 21, "fat": 0.2, "carbs": 5, "protein": 1, "sodium": 2, "fiber": 1, "sugar": 3}},
    "eggplant": {"cup": {"cal": 20, "fat": 0.2, "carbs": 5, "protein": 0.8, "sodium": 2, "fiber": 3, "sugar": 3}},
    "cucumber": {"cup": {"cal": 16, "fat": 0.1, "carbs": 4, "protein": 0.7, "sodium": 2, "fiber": 0.5, "sugar": 2}},
    "asparagus": {"cup": {"cal": 27, "fat": 0.2, "carbs": 5, "protein": 3, "sodium": 3, "fiber": 3, "sugar": 2}},
    "brussels sprouts": {"cup": {"cal": 56, "fat": 0.4, "carbs": 12, "protein": 4, "sodium": 28, "fiber": 4, "sugar": 3}},
    "kale": {"cup": {"cal": 33, "fat": 0.5, "carbs": 6, "protein": 2, "sodium": 25, "fiber": 1, "sugar": 1}},
    "avocado": {"": {"cal": 234, "fat": 21, "carbs": 12, "protein": 3, "sodium": 10, "fiber": 10, "sugar": 1},
               "cup": {"cal": 234, "fat": 21, "carbs": 12, "protein": 3, "sodium": 10, "fiber": 10, "sugar": 1}},
    "artichoke": {"": {"cal": 60, "fat": 0.2, "carbs": 13, "protein": 4, "sodium": 120, "fiber": 7, "sugar": 1}},
    "leek": {"cup": {"cal": 54, "fat": 0.3, "carbs": 13, "protein": 1, "sodium": 18, "fiber": 2, "sugar": 3},
             "": {"cal": 54, "fat": 0.3, "carbs": 13, "protein": 1, "sodium": 18, "fiber": 2, "sugar": 3}},
    "leeks": {"cup": {"cal": 54, "fat": 0.3, "carbs": 13, "protein": 1, "sodium": 18, "fiber": 2, "sugar": 3},
              "": {"cal": 54, "fat": 0.3, "carbs": 13, "protein": 1, "sodium": 18, "fiber": 2, "sugar": 3}},
    "parsley": {"cup": {"cal": 22, "fat": 0.5, "carbs": 4, "protein": 2, "sodium": 34, "fiber": 2, "sugar": 0.5},
                "tbsp": {"cal": 1, "fat": 0, "carbs": 0.2, "protein": 0.1, "sodium": 2, "fiber": 0.1, "sugar": 0}},
    "cilantro": {"cup": {"cal": 1, "fat": 0, "carbs": 0.1, "protein": 0.1, "sodium": 3, "fiber": 0.2, "sugar": 0},
                 "tbsp": {"cal": 0, "fat": 0, "carbs": 0, "protein": 0, "sodium": 0, "fiber": 0, "sugar": 0}},
    "basil": {"cup": {"cal": 1, "fat": 0, "carbs": 0.1, "protein": 0.2, "sodium": 0, "fiber": 0.1, "sugar": 0},
              "tbsp": {"cal": 0, "fat": 0, "carbs": 0, "protein": 0, "sodium": 0, "fiber": 0, "sugar": 0}},
    "chives": {"tbsp": {"cal": 1, "fat": 0, "carbs": 0.1, "protein": 0.1, "sodium": 0, "fiber": 0.1, "sugar": 0}},
    "dill": {"tbsp": {"cal": 0, "fat": 0, "carbs": 0.1, "protein": 0, "sodium": 1, "fiber": 0, "sugar": 0}},
    "mint": {"tbsp": {"cal": 1, "fat": 0, "carbs": 0.1, "protein": 0, "sodium": 0, "fiber": 0.1, "sugar": 0}},
    "rosemary": {"tbsp": {"cal": 2, "fat": 0.1, "carbs": 0.4, "protein": 0, "sodium": 1, "fiber": 0.2, "sugar": 0}},
    "thyme": {"tbsp": {"cal": 1, "fat": 0, "carbs": 0.2, "protein": 0, "sodium": 0, "fiber": 0.1, "sugar": 0}},
    "sage": {"tbsp": {"cal": 2, "fat": 0.1, "carbs": 0.4, "protein": 0.1, "sodium": 0, "fiber": 0.3, "sugar": 0}},

    # =========================================================================
    # FRUITS
    # =========================================================================
    "apple": {"cup": {"cal": 65, "fat": 0.2, "carbs": 17, "protein": 0.3, "sodium": 1, "fiber": 3, "sugar": 13},
             "medium": {"cal": 95, "fat": 0.3, "carbs": 25, "protein": 0.5, "sodium": 2, "fiber": 4, "sugar": 19},
             "": {"cal": 95, "fat": 0.3, "carbs": 25, "protein": 0.5, "sodium": 2, "fiber": 4, "sugar": 19}},
    "banana": {"": {"cal": 105, "fat": 0.4, "carbs": 27, "protein": 1, "sodium": 1, "fiber": 3, "sugar": 14},
              "cup": {"cal": 134, "fat": 0.5, "carbs": 34, "protein": 1.6, "sodium": 2, "fiber": 4, "sugar": 18}},
    "orange": {"": {"cal": 62, "fat": 0.2, "carbs": 15, "protein": 1, "sodium": 0, "fiber": 3, "sugar": 12},
              "cup": {"cal": 85, "fat": 0.2, "carbs": 21, "protein": 2, "sodium": 0, "fiber": 4, "sugar": 17}},
    "lemon": {"": {"cal": 17, "fat": 0.2, "carbs": 5, "protein": 0.6, "sodium": 1, "fiber": 2, "sugar": 1.5}},
    "lime": {"": {"cal": 20, "fat": 0.1, "carbs": 7, "protein": 0.5, "sodium": 1, "fiber": 2, "sugar": 1}},
    "lemon juice": {"cup": {"cal": 54, "fat": 0.6, "carbs": 17, "protein": 1, "sodium": 4, "fiber": 1, "sugar": 6},
                   "tbsp": {"cal": 4, "fat": 0, "carbs": 1, "protein": 0, "sodium": 0, "fiber": 0, "sugar": 0.4}},
    "lime juice": {"cup": {"cal": 60, "fat": 0.2, "carbs": 20, "protein": 1, "sodium": 4, "fiber": 1, "sugar": 4},
                  "tbsp": {"cal": 4, "fat": 0, "carbs": 1, "protein": 0, "sodium": 0, "fiber": 0, "sugar": 0.3}},
    "orange juice": {"cup": {"cal": 112, "fat": 0.5, "carbs": 26, "protein": 2, "sodium": 2, "fiber": 0.5, "sugar": 21}},
    "blueberries": {"cup": {"cal": 84, "fat": 0.5, "carbs": 21, "protein": 1, "sodium": 1, "fiber": 4, "sugar": 15}},
    "strawberries": {"cup": {"cal": 49, "fat": 0.5, "carbs": 12, "protein": 1, "sodium": 2, "fiber": 3, "sugar": 7}},
    "raspberries": {"cup": {"cal": 64, "fat": 0.8, "carbs": 15, "protein": 1.5, "sodium": 1, "fiber": 8, "sugar": 5}},
    "blackberries": {"cup": {"cal": 62, "fat": 0.7, "carbs": 14, "protein": 2, "sodium": 1, "fiber": 8, "sugar": 7}},
    "berries": {"cup": {"cal": 65, "fat": 0.6, "carbs": 16, "protein": 1, "sodium": 1, "fiber": 6, "sugar": 9}},
    "mixed berries": {"cup": {"cal": 65, "fat": 0.6, "carbs": 16, "protein": 1, "sodium": 1, "fiber": 6, "sugar": 9}},
    "cranberries": {"cup": {"cal": 46, "fat": 0.1, "carbs": 12, "protein": 0.4, "sodium": 2, "fiber": 5, "sugar": 4}},
    "grapes": {"cup": {"cal": 104, "fat": 0.2, "carbs": 27, "protein": 1, "sodium": 3, "fiber": 1, "sugar": 23}},
    "peach": {"cup": {"cal": 60, "fat": 0.4, "carbs": 14, "protein": 1, "sodium": 0, "fiber": 2, "sugar": 12},
             "": {"cal": 59, "fat": 0.4, "carbs": 14, "protein": 1, "sodium": 0, "fiber": 2, "sugar": 13}},
    "pear": {"": {"cal": 102, "fat": 0.2, "carbs": 27, "protein": 0.6, "sodium": 2, "fiber": 6, "sugar": 17}},
    "plum": {"": {"cal": 30, "fat": 0.2, "carbs": 8, "protein": 0.5, "sodium": 0, "fiber": 1, "sugar": 7}},
    "mango": {"cup": {"cal": 99, "fat": 0.6, "carbs": 25, "protein": 1, "sodium": 2, "fiber": 3, "sugar": 23}},
    "pineapple": {"cup": {"cal": 82, "fat": 0.2, "carbs": 22, "protein": 1, "sodium": 2, "fiber": 2, "sugar": 16}},
    "watermelon": {"cup": {"cal": 46, "fat": 0.2, "carbs": 12, "protein": 1, "sodium": 2, "fiber": 0.6, "sugar": 9}},
    "cantaloupe": {"cup": {"cal": 54, "fat": 0.3, "carbs": 13, "protein": 1, "sodium": 26, "fiber": 1, "sugar": 12}},
    "cherries": {"cup": {"cal": 97, "fat": 0.3, "carbs": 25, "protein": 2, "sodium": 0, "fiber": 3, "sugar": 20}},
    "raisins": {"cup": {"cal": 434, "fat": 0.5, "carbs": 115, "protein": 5, "sodium": 18, "fiber": 5, "sugar": 86}},
    "dates": {"cup": {"cal": 415, "fat": 0.4, "carbs": 110, "protein": 4, "sodium": 3, "fiber": 12, "sugar": 93}},
    "dried cranberries": {"cup": {"cal": 308, "fat": 1, "carbs": 82, "protein": 0.2, "sodium": 3, "fiber": 6, "sugar": 65}},
    "dried apricots": {"cup": {"cal": 313, "fat": 0.7, "carbs": 81, "protein": 4, "sodium": 13, "fiber": 9, "sugar": 69},
                      "lb": {"cal": 1063, "fat": 2.3, "carbs": 275, "protein": 14, "sodium": 45, "fiber": 31, "sugar": 235}},
    "applesauce": {"cup": {"cal": 167, "fat": 0.4, "carbs": 43, "protein": 0.4, "sodium": 5, "fiber": 3, "sugar": 36}},

    # =========================================================================
    # NUTS & SEEDS
    # =========================================================================
    "almonds": {"cup": {"cal": 828, "fat": 72, "carbs": 28, "protein": 30, "sodium": 1, "fiber": 17, "sugar": 6},
               "oz": {"cal": 164, "fat": 14, "carbs": 6, "protein": 6, "sodium": 0, "fiber": 3.5, "sugar": 1}},
    "walnuts": {"cup": {"cal": 765, "fat": 76, "carbs": 16, "protein": 18, "sodium": 2, "fiber": 8, "sugar": 3}},
    "pecans": {"cup": {"cal": 753, "fat": 78, "carbs": 15, "protein": 10, "sodium": 0, "fiber": 10, "sugar": 4}},
    "peanuts": {"cup": {"cal": 828, "fat": 72, "carbs": 24, "protein": 38, "sodium": 26, "fiber": 12, "sugar": 6}},
    "peanut butter": {"cup": {"cal": 1517, "fat": 130, "carbs": 50, "protein": 64, "sodium": 1010, "fiber": 12, "sugar": 24},
                     "tbsp": {"cal": 95, "fat": 8, "carbs": 3, "protein": 4, "sodium": 63, "fiber": 0.8, "sugar": 1.5}},
    "cashews": {"cup": {"cal": 786, "fat": 64, "carbs": 44, "protein": 25, "sodium": 22, "fiber": 4, "sugar": 8}},
    "sunflower seeds": {"cup": {"cal": 818, "fat": 71, "carbs": 28, "protein": 29, "sodium": 4, "fiber": 12, "sugar": 4}},
    "pumpkin seeds": {"cup": {"cal": 677, "fat": 55, "carbs": 25, "protein": 34, "sodium": 25, "fiber": 12, "sugar": 2}},
    "sesame seeds": {"cup": {"cal": 825, "fat": 72, "carbs": 34, "protein": 25, "sodium": 16, "fiber": 17, "sugar": 0},
                    "tbsp": {"cal": 52, "fat": 4.5, "carbs": 2, "protein": 1.6, "sodium": 1, "fiber": 1, "sugar": 0}},
    "flax seeds": {"tbsp": {"cal": 37, "fat": 3, "carbs": 2, "protein": 1.3, "sodium": 2, "fiber": 2, "sugar": 0}},
    "flaxseed": {"tbsp": {"cal": 37, "fat": 3, "carbs": 2, "protein": 1.3, "sodium": 2, "fiber": 2, "sugar": 0},
                "cup": {"cal": 592, "fat": 48, "carbs": 32, "protein": 21, "sodium": 32, "fiber": 32, "sugar": 0}},
    "ground flaxseed": {"tbsp": {"cal": 37, "fat": 3, "carbs": 2, "protein": 1.3, "sodium": 2, "fiber": 2, "sugar": 0}},
    "chia seeds": {"tbsp": {"cal": 58, "fat": 4, "carbs": 5, "protein": 2, "sodium": 2, "fiber": 4, "sugar": 0}},
    "coconut": {"cup": {"cal": 283, "fat": 27, "carbs": 12, "protein": 3, "sodium": 16, "fiber": 7, "sugar": 5}},

    # =========================================================================
    # GRAINS & PASTA
    # =========================================================================
    "rice": {"cup": {"cal": 206, "fat": 0.4, "carbs": 45, "protein": 4, "sodium": 2, "fiber": 0.6, "sugar": 0}},
    "brown rice": {"cup": {"cal": 216, "fat": 1.8, "carbs": 45, "protein": 5, "sodium": 10, "fiber": 4, "sugar": 0}},
    "pasta": {"cup": {"cal": 220, "fat": 1.3, "carbs": 43, "protein": 8, "sodium": 1, "fiber": 3, "sugar": 0.8},
             "lb": {"cal": 756, "fat": 4.5, "carbs": 148, "protein": 27, "sodium": 3, "fiber": 10, "sugar": 3}},
    "egg noodles": {"cup": {"cal": 221, "fat": 3.3, "carbs": 40, "protein": 7, "sodium": 8, "fiber": 2, "sugar": 0.5}},
    "oats": {"cup": {"cal": 307, "fat": 5, "carbs": 55, "protein": 11, "sodium": 5, "fiber": 8, "sugar": 1}},
    "instant oatmeal": {"packet": {"cal": 100, "fat": 2, "carbs": 19, "protein": 4, "sodium": 75, "fiber": 3, "sugar": 1},
                        "packets": {"cal": 100, "fat": 2, "carbs": 19, "protein": 4, "sodium": 75, "fiber": 3, "sugar": 1},
                        "oz": {"cal": 100, "fat": 2, "carbs": 19, "protein": 4, "sodium": 75, "fiber": 3, "sugar": 1},
                        "1-oz": {"cal": 100, "fat": 2, "carbs": 19, "protein": 4, "sodium": 75, "fiber": 3, "sugar": 1},
                        "cup": {"cal": 150, "fat": 3, "carbs": 28, "protein": 6, "sodium": 113, "fiber": 4, "sugar": 1}},
    "quinoa": {"cup": {"cal": 222, "fat": 3.6, "carbs": 39, "protein": 8, "sodium": 13, "fiber": 5, "sugar": 2}},
    "couscous": {"cup": {"cal": 176, "fat": 0.3, "carbs": 36, "protein": 6, "sodium": 8, "fiber": 2, "sugar": 0}},
    "breadcrumbs": {"cup": {"cal": 427, "fat": 6, "carbs": 78, "protein": 14, "sodium": 791, "fiber": 5, "sugar": 6}},
    "croutons": {"cup": {"cal": 122, "fat": 2, "carbs": 22, "protein": 4, "sodium": 209, "fiber": 2, "sugar": 2}},

    # =========================================================================
    # BREADS & TORTILLAS
    # =========================================================================
    "bread": {"slice": {"cal": 79, "fat": 1, "carbs": 15, "protein": 3, "sodium": 147, "fiber": 0.6, "sugar": 1.5}},
    "white bread": {"slice": {"cal": 79, "fat": 1, "carbs": 15, "protein": 3, "sodium": 147, "fiber": 0.6, "sugar": 1.5}},
    "whole wheat bread": {"slice": {"cal": 81, "fat": 1, "carbs": 14, "protein": 4, "sodium": 146, "fiber": 2, "sugar": 1.4}},
    "tortilla": {"": {"cal": 94, "fat": 2, "carbs": 16, "protein": 2, "sodium": 191, "fiber": 1, "sugar": 0.4},
                "large": {"cal": 140, "fat": 3.5, "carbs": 24, "protein": 4, "sodium": 290, "fiber": 1.5, "sugar": 0.6}},
    "flour tortilla": {"": {"cal": 94, "fat": 2, "carbs": 16, "protein": 2, "sodium": 191, "fiber": 1, "sugar": 0.4},
                      "large": {"cal": 140, "fat": 3.5, "carbs": 24, "protein": 4, "sodium": 290, "fiber": 1.5, "sugar": 0.6}},
    "corn tortilla": {"": {"cal": 52, "fat": 0.7, "carbs": 11, "protein": 1, "sodium": 11, "fiber": 1.5, "sugar": 0.2}},
    "pita bread": {"": {"cal": 165, "fat": 0.7, "carbs": 34, "protein": 5, "sodium": 322, "fiber": 1, "sugar": 0.5}},
    "hamburger bun": {"": {"cal": 120, "fat": 2, "carbs": 21, "protein": 4, "sodium": 206, "fiber": 0.9, "sugar": 3}},
    "hot dog bun": {"": {"cal": 100, "fat": 1.5, "carbs": 18, "protein": 3, "sodium": 180, "fiber": 0.7, "sugar": 2}},
    "hoagie roll": {"": {"cal": 190, "fat": 3, "carbs": 35, "protein": 7, "sodium": 340, "fiber": 1.5, "sugar": 3}},
    "sub roll": {"": {"cal": 190, "fat": 3, "carbs": 35, "protein": 7, "sodium": 340, "fiber": 1.5, "sugar": 3}},
    "italian roll": {"": {"cal": 175, "fat": 2, "carbs": 33, "protein": 6, "sodium": 310, "fiber": 1.5, "sugar": 2}},
    "pie crust": {"": {"cal": 648, "fat": 40, "carbs": 63, "protein": 7, "sodium": 520, "fiber": 2, "sugar": 2}},
    "pizza dough": {"lb": {"cal": 680, "fat": 8, "carbs": 130, "protein": 22, "sodium": 1200, "fiber": 5, "sugar": 4}},
    "biscuit": {"": {"cal": 127, "fat": 6, "carbs": 17, "protein": 2, "sodium": 368, "fiber": 0.5, "sugar": 2}},
    "biscuits": {"": {"cal": 127, "fat": 6, "carbs": 17, "protein": 2, "sodium": 368, "fiber": 0.5, "sugar": 2},
                "can": {"cal": 800, "fat": 38, "carbs": 102, "protein": 12, "sodium": 2200, "fiber": 3, "sugar": 12}},
    "refrigerated biscuits": {"can": {"cal": 800, "fat": 38, "carbs": 102, "protein": 12, "sodium": 2200, "fiber": 3, "sugar": 12}},
    "crescent rolls": {"can": {"cal": 880, "fat": 48, "carbs": 96, "protein": 12, "sodium": 1920, "fiber": 0, "sugar": 12}},
    "croissant": {"": {"cal": 231, "fat": 12, "carbs": 26, "protein": 5, "sodium": 319, "fiber": 1.5, "sugar": 5}},
    "french bread": {"slice": {"cal": 92, "fat": 1, "carbs": 18, "protein": 4, "sodium": 202, "fiber": 0.8, "sugar": 1},
                    "loaf": {"cal": 1100, "fat": 12, "carbs": 216, "protein": 48, "sodium": 2424, "fiber": 10, "sugar": 12}},
    "rye bread": {"slice": {"cal": 83, "fat": 1, "carbs": 15, "protein": 3, "sodium": 211, "fiber": 1.9, "sugar": 1}},
    "sourdough": {"slice": {"cal": 93, "fat": 0.6, "carbs": 18, "protein": 4, "sodium": 206, "fiber": 0.6, "sugar": 0.5}},
    "ciabatta": {"": {"cal": 150, "fat": 2, "carbs": 28, "protein": 6, "sodium": 310, "fiber": 1, "sugar": 1},
                "loaf": {"cal": 600, "fat": 8, "carbs": 112, "protein": 24, "sodium": 1240, "fiber": 4, "sugar": 4}},

    # =========================================================================
    # CHOCOLATE & BAKING
    # =========================================================================
    "chocolate chips": {"cup": {"cal": 805, "fat": 50, "carbs": 100, "protein": 7, "sodium": 23, "fiber": 10, "sugar": 81}},
    "cocoa powder": {"cup": {"cal": 196, "fat": 12, "carbs": 47, "protein": 17, "sodium": 18, "fiber": 29, "sugar": 1},
                    "tbsp": {"cal": 12, "fat": 0.7, "carbs": 3, "protein": 1, "sodium": 1, "fiber": 2, "sugar": 0}},
    "malted milk": {"cup": {"cal": 480, "fat": 10, "carbs": 84, "protein": 16, "sodium": 580, "fiber": 0, "sugar": 64},
                   "tbsp": {"cal": 30, "fat": 0.6, "carbs": 5, "protein": 1, "sodium": 36, "fiber": 0, "sugar": 4}},
    "baking chocolate": {"oz": {"cal": 145, "fat": 15, "carbs": 8, "protein": 3, "sodium": 4, "fiber": 4, "sugar": 0}},
    "white chocolate": {"cup": {"cal": 916, "fat": 55, "carbs": 101, "protein": 10, "sodium": 153, "fiber": 0, "sugar": 101}},
    "nutella": {"tbsp": {"cal": 100, "fat": 6, "carbs": 11, "protein": 1, "sodium": 15, "fiber": 0.5, "sugar": 10}},
    "gelatin": {"tbsp": {"cal": 23, "fat": 0, "carbs": 0, "protein": 6, "sodium": 14, "fiber": 0, "sugar": 0},
               "packet": {"cal": 23, "fat": 0, "carbs": 0, "protein": 6, "sodium": 14, "fiber": 0, "sugar": 0},
               "envelope": {"cal": 23, "fat": 0, "carbs": 0, "protein": 6, "sodium": 14, "fiber": 0, "sugar": 0}},
    "vanilla extract": {"tsp": {"cal": 12, "fat": 0, "carbs": 0.5, "protein": 0, "sodium": 0, "fiber": 0, "sugar": 0.5}},
    "almond extract": {"tsp": {"cal": 12, "fat": 0, "carbs": 0.3, "protein": 0, "sodium": 0, "fiber": 0, "sugar": 0}},

    # =========================================================================
    # LEAVENING & BAKING STAPLES
    # =========================================================================
    "baking powder": {"tsp": {"cal": 2, "fat": 0, "carbs": 0.7, "protein": 0, "sodium": 133, "fiber": 0, "sugar": 0},
                     "tbsp": {"cal": 5, "fat": 0, "carbs": 2, "protein": 0, "sodium": 400, "fiber": 0, "sugar": 0}},
    "baking soda": {"tsp": {"cal": 0, "fat": 0, "carbs": 0, "protein": 0, "sodium": 1260, "fiber": 0, "sugar": 0}},
    "yeast": {"packet": {"cal": 21, "fat": 0.3, "carbs": 3, "protein": 3, "sodium": 4, "fiber": 2, "sugar": 0},
             "sachet": {"cal": 21, "fat": 0.3, "carbs": 3, "protein": 3, "sodium": 4, "fiber": 2, "sugar": 0},
             "tbsp": {"cal": 23, "fat": 0.4, "carbs": 3, "protein": 3, "sodium": 4, "fiber": 2, "sugar": 0},
             "tsp": {"cal": 8, "fat": 0.1, "carbs": 1, "protein": 1, "sodium": 1, "fiber": 0.6, "sugar": 0}},
    "cream of tartar": {"tsp": {"cal": 8, "fat": 0, "carbs": 2, "protein": 0, "sodium": 2, "fiber": 0, "sugar": 0}},

    # =========================================================================
    # SPICES & SEASONINGS
    # =========================================================================
    "salt": {"tsp": {"cal": 0, "fat": 0, "carbs": 0, "protein": 0, "sodium": 2325, "fiber": 0, "sugar": 0},
            "tbsp": {"cal": 0, "fat": 0, "carbs": 0, "protein": 0, "sodium": 6975, "fiber": 0, "sugar": 0},
            "pinch": {"cal": 0, "fat": 0, "carbs": 0, "protein": 0, "sodium": 150, "fiber": 0, "sugar": 0},
            "to taste": {"cal": 0, "fat": 0, "carbs": 0, "protein": 0, "sodium": 300, "fiber": 0, "sugar": 0},
            "": {"cal": 0, "fat": 0, "carbs": 0, "protein": 0, "sodium": 300, "fiber": 0, "sugar": 0}},
    "pepper": {"tsp": {"cal": 6, "fat": 0.1, "carbs": 1.5, "protein": 0.2, "sodium": 0, "fiber": 0.6, "sugar": 0},
              "to taste": {"cal": 1, "fat": 0, "carbs": 0.3, "protein": 0, "sodium": 0, "fiber": 0.1, "sugar": 0},
              "": {"cal": 1, "fat": 0, "carbs": 0.3, "protein": 0, "sodium": 0, "fiber": 0.1, "sugar": 0}},
    "black pepper": {"tsp": {"cal": 6, "fat": 0.1, "carbs": 1.5, "protein": 0.2, "sodium": 0, "fiber": 0.6, "sugar": 0}},
    "garlic powder": {"tsp": {"cal": 10, "fat": 0, "carbs": 2, "protein": 0.5, "sodium": 2, "fiber": 0.3, "sugar": 0}},
    "onion powder": {"tsp": {"cal": 8, "fat": 0, "carbs": 2, "protein": 0.2, "sodium": 2, "fiber": 0.2, "sugar": 0.4}},
    "cumin": {"tsp": {"cal": 8, "fat": 0.5, "carbs": 1, "protein": 0.4, "sodium": 4, "fiber": 0.2, "sugar": 0},
             "tbsp": {"cal": 22, "fat": 1.3, "carbs": 3, "protein": 1, "sodium": 10, "fiber": 0.6, "sugar": 0.1}},
    "paprika": {"tsp": {"cal": 6, "fat": 0.3, "carbs": 1.2, "protein": 0.3, "sodium": 2, "fiber": 0.8, "sugar": 0.5},
               "": {"cal": 6, "fat": 0.3, "carbs": 1.2, "protein": 0.3, "sodium": 2, "fiber": 0.8, "sugar": 0.5}},
    "chili powder": {"tsp": {"cal": 8, "fat": 0.4, "carbs": 1.4, "protein": 0.3, "sodium": 26, "fiber": 0.9, "sugar": 0.3},
                    "tbsp": {"cal": 24, "fat": 1.3, "carbs": 4, "protein": 1, "sodium": 77, "fiber": 2.7, "sugar": 0.9}},
    "cayenne pepper": {"tsp": {"cal": 6, "fat": 0.3, "carbs": 1, "protein": 0.2, "sodium": 1, "fiber": 0.5, "sugar": 0.2}},
    "oregano": {"tsp": {"cal": 5, "fat": 0.2, "carbs": 1, "protein": 0.2, "sodium": 0, "fiber": 0.4, "sugar": 0}},
    "basil": {"tsp": {"cal": 1, "fat": 0, "carbs": 0.1, "protein": 0.1, "sodium": 0, "fiber": 0.1, "sugar": 0}},
    "thyme": {"tsp": {"cal": 3, "fat": 0.1, "carbs": 0.6, "protein": 0.1, "sodium": 1, "fiber": 0.4, "sugar": 0}},
    "rosemary": {"tsp": {"cal": 2, "fat": 0.1, "carbs": 0.4, "protein": 0, "sodium": 1, "fiber": 0.2, "sugar": 0}},
    "sage": {"tsp": {"cal": 2, "fat": 0.1, "carbs": 0.4, "protein": 0.1, "sodium": 0, "fiber": 0.3, "sugar": 0}},
    "marjoram": {"tsp": {"cal": 2, "fat": 0.1, "carbs": 0.4, "protein": 0.1, "sodium": 0, "fiber": 0.2, "sugar": 0}},
    "tarragon": {"tsp": {"cal": 2, "fat": 0, "carbs": 0.4, "protein": 0.1, "sodium": 0, "fiber": 0.1, "sugar": 0}},
    "bay leaf": {"": {"cal": 2, "fat": 0.1, "carbs": 0.5, "protein": 0, "sodium": 0, "fiber": 0.2, "sugar": 0}},
    "bay leaves": {"": {"cal": 2, "fat": 0.1, "carbs": 0.5, "protein": 0, "sodium": 0, "fiber": 0.2, "sugar": 0}},
    "parsley": {"tsp": {"cal": 1, "fat": 0, "carbs": 0.1, "protein": 0.1, "sodium": 2, "fiber": 0.1, "sugar": 0},
               "cup": {"cal": 22, "fat": 0.5, "carbs": 4, "protein": 2, "sodium": 34, "fiber": 2, "sugar": 0.5}},
    "cilantro": {"cup": {"cal": 1, "fat": 0, "carbs": 0.1, "protein": 0.1, "sodium": 3, "fiber": 0.2, "sugar": 0}},
    "dill": {"tsp": {"cal": 1, "fat": 0, "carbs": 0.1, "protein": 0, "sodium": 1, "fiber": 0, "sugar": 0},
            "tbsp": {"cal": 3, "fat": 0.1, "carbs": 0.6, "protein": 0.2, "sodium": 5, "fiber": 0.2, "sugar": 0}},
    "cinnamon": {"tsp": {"cal": 6, "fat": 0, "carbs": 2, "protein": 0, "sodium": 0, "fiber": 1, "sugar": 0}},
    "nutmeg": {"tsp": {"cal": 12, "fat": 0.8, "carbs": 1, "protein": 0.1, "sodium": 0, "fiber": 0.5, "sugar": 0}},
    "ginger": {"tsp": {"cal": 6, "fat": 0, "carbs": 1.3, "protein": 0.2, "sodium": 1, "fiber": 0.2, "sugar": 0},
              "tbsp": {"cal": 18, "fat": 0, "carbs": 4, "protein": 0.5, "sodium": 3, "fiber": 0.6, "sugar": 0.5}},
    "allspice": {"tsp": {"cal": 5, "fat": 0.2, "carbs": 1.4, "protein": 0.1, "sodium": 1, "fiber": 0.4, "sugar": 0}},
    "star anise": {"": {"cal": 7, "fat": 0.3, "carbs": 1, "protein": 0.2, "sodium": 0, "fiber": 0.3, "sugar": 0},
                  "tsp": {"cal": 7, "fat": 0.3, "carbs": 1, "protein": 0.2, "sodium": 0, "fiber": 0.3, "sugar": 0}},
    "sichuan peppercorns": {"tsp": {"cal": 6, "fat": 0.2, "carbs": 1, "protein": 0.2, "sodium": 0, "fiber": 0.3, "sugar": 0}},
    "long pepper": {"tsp": {"cal": 6, "fat": 0.2, "carbs": 1, "protein": 0.2, "sodium": 0, "fiber": 0.3, "sugar": 0}},
    "cloves": {"tsp": {"cal": 7, "fat": 0.4, "carbs": 1.3, "protein": 0.1, "sodium": 5, "fiber": 0.7, "sugar": 0}},
    "mustard": {"tsp": {"cal": 3, "fat": 0.2, "carbs": 0.3, "protein": 0.2, "sodium": 57, "fiber": 0.1, "sugar": 0.1},
               "tbsp": {"cal": 10, "fat": 0.7, "carbs": 0.8, "protein": 0.7, "sodium": 171, "fiber": 0.4, "sugar": 0.3}},
    "dry mustard": {"tsp": {"cal": 9, "fat": 0.5, "carbs": 0.5, "protein": 0.5, "sodium": 0, "fiber": 0.2, "sugar": 0}},
    "curry powder": {"tsp": {"cal": 7, "fat": 0.3, "carbs": 1.2, "protein": 0.3, "sodium": 1, "fiber": 0.7, "sugar": 0.1},
                    "tbsp": {"cal": 20, "fat": 0.9, "carbs": 3.7, "protein": 0.8, "sodium": 3, "fiber": 2, "sugar": 0.2}},
    "bay leaf": {"": {"cal": 2, "fat": 0.1, "carbs": 0.5, "protein": 0, "sodium": 0, "fiber": 0.2, "sugar": 0}},
    "bay leaves": {"": {"cal": 2, "fat": 0.1, "carbs": 0.5, "protein": 0, "sodium": 0, "fiber": 0.2, "sugar": 0}},
    "italian seasoning": {"tsp": {"cal": 3, "fat": 0.1, "carbs": 0.6, "protein": 0.1, "sodium": 1, "fiber": 0.3, "sugar": 0}},
    "taco seasoning": {"packet": {"cal": 30, "fat": 0.5, "carbs": 6, "protein": 1, "sodium": 1400, "fiber": 1, "sugar": 1},
                      "tbsp": {"cal": 15, "fat": 0.3, "carbs": 3, "protein": 0.5, "sodium": 700, "fiber": 0.5, "sugar": 0.5}},
    "ranch seasoning": {"packet": {"cal": 45, "fat": 0, "carbs": 10, "protein": 1, "sodium": 1200, "fiber": 0, "sugar": 2}},
    "worcestershire sauce": {"tbsp": {"cal": 13, "fat": 0, "carbs": 3, "protein": 0, "sodium": 167, "fiber": 0, "sugar": 2}},
    "browning sauce": {"tsp": {"cal": 5, "fat": 0, "carbs": 1, "protein": 0, "sodium": 100, "fiber": 0, "sugar": 0},
                      "tbsp": {"cal": 15, "fat": 0, "carbs": 3, "protein": 0, "sodium": 300, "fiber": 0, "sugar": 0}},
    "soy sauce": {"tbsp": {"cal": 9, "fat": 0, "carbs": 1, "protein": 1, "sodium": 879, "fiber": 0, "sugar": 0},
                 "cup": {"cal": 135, "fat": 0, "carbs": 15, "protein": 15, "sodium": 14000, "fiber": 0, "sugar": 1}},
    "hot sauce": {"tsp": {"cal": 1, "fat": 0, "carbs": 0, "protein": 0, "sodium": 124, "fiber": 0, "sugar": 0}},
    "bbq sauce": {"tbsp": {"cal": 29, "fat": 0.1, "carbs": 7, "protein": 0.1, "sodium": 175, "fiber": 0.2, "sugar": 5}},
    "ketchup": {"tbsp": {"cal": 19, "fat": 0, "carbs": 5, "protein": 0.2, "sodium": 154, "fiber": 0, "sugar": 4}},

    # =========================================================================
    # VINEGARS & ACIDS
    # =========================================================================
    "vinegar": {"tbsp": {"cal": 3, "fat": 0, "carbs": 0, "protein": 0, "sodium": 0, "fiber": 0, "sugar": 0},
               "cup": {"cal": 43, "fat": 0, "carbs": 0.9, "protein": 0, "sodium": 2, "fiber": 0, "sugar": 0.4},
               "quart": {"cal": 172, "fat": 0, "carbs": 3.6, "protein": 0, "sodium": 8, "fiber": 0, "sugar": 1.6},
               "pint": {"cal": 86, "fat": 0, "carbs": 1.8, "protein": 0, "sodium": 4, "fiber": 0, "sugar": 0.8}},
    "apple cider vinegar": {"tbsp": {"cal": 3, "fat": 0, "carbs": 0.1, "protein": 0, "sodium": 1, "fiber": 0, "sugar": 0}},
    "balsamic vinegar": {"tbsp": {"cal": 14, "fat": 0, "carbs": 3, "protein": 0, "sodium": 4, "fiber": 0, "sugar": 2}},
    "red wine vinegar": {"tbsp": {"cal": 3, "fat": 0, "carbs": 0, "protein": 0, "sodium": 1, "fiber": 0, "sugar": 0},
                         "cup": {"cal": 45, "fat": 0, "carbs": 0, "protein": 0, "sodium": 12, "fiber": 0, "sugar": 0}},
    "white wine vinegar": {"tbsp": {"cal": 3, "fat": 0, "carbs": 0, "protein": 0, "sodium": 1, "fiber": 0, "sugar": 0}},
    "rice vinegar": {"tbsp": {"cal": 3, "fat": 0, "carbs": 0, "protein": 0, "sodium": 0, "fiber": 0, "sugar": 0},
                    "cup": {"cal": 45, "fat": 0, "carbs": 0, "protein": 0, "sodium": 0, "fiber": 0, "sugar": 0}},

    # =========================================================================
    # WINES & ALCOHOL (for cooking)
    # =========================================================================
    "white wine": {"cup": {"cal": 194, "fat": 0, "carbs": 5, "protein": 0.3, "sodium": 10, "fiber": 0, "sugar": 1.4}},
    "red wine": {"cup": {"cal": 199, "fat": 0, "carbs": 5, "protein": 0.3, "sodium": 10, "fiber": 0, "sugar": 0.9}},
    "cooking wine": {"cup": {"cal": 190, "fat": 0, "carbs": 8, "protein": 0, "sodium": 1000, "fiber": 0, "sugar": 4}},
    "beer": {"cup": {"cal": 103, "fat": 0, "carbs": 6, "protein": 1, "sodium": 14, "fiber": 0, "sugar": 0}},
    "rum": {"tbsp": {"cal": 32, "fat": 0, "carbs": 0, "protein": 0, "sodium": 0, "fiber": 0, "sugar": 0}},
    "bourbon": {"tbsp": {"cal": 32, "fat": 0, "carbs": 0, "protein": 0, "sodium": 0, "fiber": 0, "sugar": 0}},
    "vodka": {"tbsp": {"cal": 32, "fat": 0, "carbs": 0, "protein": 0, "sodium": 0, "fiber": 0, "sugar": 0}},
    "champagne": {"cup": {"cal": 168, "fat": 0, "carbs": 3, "protein": 0.5, "sodium": 10, "fiber": 0, "sugar": 1.5},
                 "oz": {"cal": 21, "fat": 0, "carbs": 0.4, "protein": 0, "sodium": 1, "fiber": 0, "sugar": 0.2}},
    "sparkling wine": {"cup": {"cal": 168, "fat": 0, "carbs": 3, "protein": 0.5, "sodium": 10, "fiber": 0, "sugar": 1.5}},
    "prosecco": {"cup": {"cal": 160, "fat": 0, "carbs": 2, "protein": 0.4, "sodium": 10, "fiber": 0, "sugar": 1}},
    "dry vermouth": {"oz": {"cal": 35, "fat": 0, "carbs": 3.5, "protein": 0, "sodium": 2, "fiber": 0, "sugar": 1.5}},
    "sweet vermouth": {"oz": {"cal": 45, "fat": 0, "carbs": 5, "protein": 0, "sodium": 2, "fiber": 0, "sugar": 4}},
    "vermouth": {"oz": {"cal": 40, "fat": 0, "carbs": 4, "protein": 0, "sodium": 2, "fiber": 0, "sugar": 2}},
    "sherry": {"cup": {"cal": 258, "fat": 0, "carbs": 8, "protein": 0.5, "sodium": 20, "fiber": 0, "sugar": 2}},
    "port": {"cup": {"cal": 352, "fat": 0, "carbs": 20, "protein": 0.5, "sodium": 20, "fiber": 0, "sugar": 18}},
    "brandy": {"oz": {"cal": 65, "fat": 0, "carbs": 0, "protein": 0, "sodium": 0, "fiber": 0, "sugar": 0}},
    "cognac": {"oz": {"cal": 65, "fat": 0, "carbs": 0, "protein": 0, "sodium": 0, "fiber": 0, "sugar": 0}},
    "whiskey": {"oz": {"cal": 70, "fat": 0, "carbs": 0, "protein": 0, "sodium": 0, "fiber": 0, "sugar": 0}},
    "scotch": {"oz": {"cal": 70, "fat": 0, "carbs": 0, "protein": 0, "sodium": 0, "fiber": 0, "sugar": 0}},
    "tequila": {"oz": {"cal": 64, "fat": 0, "carbs": 0, "protein": 0, "sodium": 0, "fiber": 0, "sugar": 0}},
    "triple sec": {"oz": {"cal": 103, "fat": 0, "carbs": 11, "protein": 0, "sodium": 2, "fiber": 0, "sugar": 11}},
    "kahlua": {"oz": {"cal": 91, "fat": 0.1, "carbs": 14, "protein": 0, "sodium": 3, "fiber": 0, "sugar": 14}},
    "amaretto": {"oz": {"cal": 110, "fat": 0, "carbs": 17, "protein": 0, "sodium": 3, "fiber": 0, "sugar": 17}},
    "grand marnier": {"oz": {"cal": 76, "fat": 0, "carbs": 7, "protein": 0, "sodium": 1, "fiber": 0, "sugar": 7}},
    "simple syrup": {"oz": {"cal": 52, "fat": 0, "carbs": 13, "protein": 0, "sodium": 0, "fiber": 0, "sugar": 13}},

    # =========================================================================
    # MISCELLANEOUS
    # =========================================================================
    "coffee": {"cup": {"cal": 2, "fat": 0, "carbs": 0, "protein": 0.3, "sodium": 5, "fiber": 0, "sugar": 0}},
    "tea": {"cup": {"cal": 2, "fat": 0, "carbs": 1, "protein": 0, "sodium": 7, "fiber": 0, "sugar": 0}},
    "cocoa": {"cup": {"cal": 196, "fat": 12, "carbs": 47, "protein": 17, "sodium": 18, "fiber": 29, "sugar": 1}},
    "jam": {"tbsp": {"cal": 56, "fat": 0, "carbs": 14, "protein": 0, "sodium": 6, "fiber": 0.2, "sugar": 10}},
    "jelly": {"tbsp": {"cal": 56, "fat": 0, "carbs": 14, "protein": 0, "sodium": 6, "fiber": 0, "sugar": 10}},
    "marshmallows": {"cup": {"cal": 159, "fat": 0, "carbs": 41, "protein": 1, "sodium": 22, "fiber": 0, "sugar": 29}},
    "graham cracker": {"sheet": {"cal": 59, "fat": 1.4, "carbs": 11, "protein": 1, "sodium": 67, "fiber": 0.4, "sugar": 4}},
    "crackers": {"cup": {"cal": 484, "fat": 15, "carbs": 78, "protein": 10, "sodium": 1080, "fiber": 3, "sugar": 6}},
    "tortilla chips": {"cup": {"cal": 267, "fat": 14, "carbs": 33, "protein": 3, "sodium": 179, "fiber": 2, "sugar": 0}},
    "potato chips": {"cup": {"cal": 274, "fat": 19, "carbs": 25, "protein": 3, "sodium": 303, "fiber": 2, "sugar": 1}},
    "french fried onions": {"cup": {"cal": 320, "fat": 24, "carbs": 24, "protein": 4, "sodium": 520, "fiber": 2, "sugar": 4}},

    # Cooking sprays & zests
    "cooking spray": {"": {"cal": 0, "fat": 0, "carbs": 0, "protein": 0, "sodium": 0, "fiber": 0, "sugar": 0}},
    "nonstick spray": {"": {"cal": 0, "fat": 0, "carbs": 0, "protein": 0, "sodium": 0, "fiber": 0, "sugar": 0}},
    "lemon zest": {"tsp": {"cal": 1, "fat": 0, "carbs": 0.3, "protein": 0, "sodium": 0, "fiber": 0.1, "sugar": 0.1},
                   "tbsp": {"cal": 3, "fat": 0, "carbs": 1, "protein": 0.1, "sodium": 0, "fiber": 0.4, "sugar": 0.2}},
    "orange zest": {"tsp": {"cal": 2, "fat": 0, "carbs": 0.5, "protein": 0, "sodium": 0, "fiber": 0.2, "sugar": 0.2},
                    "tbsp": {"cal": 6, "fat": 0, "carbs": 1.5, "protein": 0.1, "sodium": 0, "fiber": 0.6, "sugar": 0.4}},
    "lime zest": {"tsp": {"cal": 1, "fat": 0, "carbs": 0.3, "protein": 0, "sodium": 0, "fiber": 0.1, "sugar": 0.1},
                  "tbsp": {"cal": 3, "fat": 0, "carbs": 0.9, "protein": 0, "sodium": 0, "fiber": 0.3, "sugar": 0.2}},
    "onion juice": {"tbsp": {"cal": 4, "fat": 0, "carbs": 1, "protein": 0.1, "sodium": 1, "fiber": 0, "sugar": 0.4},
                    "tsp": {"cal": 1, "fat": 0, "carbs": 0.3, "protein": 0, "sodium": 0, "fiber": 0, "sugar": 0.1}},
    "grated onion": {"tbsp": {"cal": 4, "fat": 0, "carbs": 1, "protein": 0.1, "sodium": 1, "fiber": 0.1, "sugar": 0.4}},

    # Cream and creamed soups
    "cream": {"cup": {"cal": 821, "fat": 88, "carbs": 7, "protein": 5, "sodium": 89, "fiber": 0, "sugar": 7}},
    "whipped topping": {"cup": {"cal": 239, "fat": 19, "carbs": 17, "protein": 1, "sodium": 5, "fiber": 0, "sugar": 14}},
    "cool whip": {"cup": {"cal": 239, "fat": 19, "carbs": 17, "protein": 1, "sodium": 5, "fiber": 0, "sugar": 14}},
    "cream of chicken soup": {"can": {"cal": 226, "fat": 14, "carbs": 18, "protein": 6, "sodium": 1764, "fiber": 1, "sugar": 2}},
    "cream of mushroom soup": {"can": {"cal": 260, "fat": 18, "carbs": 18, "protein": 4, "sodium": 1740, "fiber": 2, "sugar": 4}},
    "cream of celery soup": {"can": {"cal": 180, "fat": 10, "carbs": 18, "protein": 2, "sodium": 1760, "fiber": 2, "sugar": 4}},
    "tomato soup": {"can": {"cal": 160, "fat": 2, "carbs": 34, "protein": 4, "sodium": 1400, "fiber": 2, "sugar": 20}},

    # Pinch/dash for minimal seasonings
    "pinch": {"": {"cal": 0, "fat": 0, "carbs": 0, "protein": 0, "sodium": 75, "fiber": 0, "sugar": 0}},
    "dash": {"": {"cal": 0, "fat": 0, "carbs": 0, "protein": 0, "sodium": 75, "fiber": 0, "sugar": 0}},

    # Baked goods & prepared items (from GrannysRecipes)
    "croissant": {"": {"cal": 230, "fat": 12, "carbs": 26, "protein": 5, "sodium": 310, "fiber": 1, "sugar": 6}},
    "crescent rolls": {"": {"cal": 100, "fat": 5, "carbs": 11, "protein": 2, "sodium": 220, "fiber": 0, "sugar": 2}},
    "puff pastry": {"sheet": {"cal": 900, "fat": 60, "carbs": 72, "protein": 12, "sodium": 360, "fiber": 2, "sugar": 2}},
    "english muffin": {"": {"cal": 134, "fat": 1, "carbs": 26, "protein": 4, "sodium": 264, "fiber": 2, "sugar": 2}},
    "angel food cake": {"slice": {"cal": 72, "fat": 0.2, "carbs": 16, "protein": 2, "sodium": 210, "fiber": 0, "sugar": 12}},
    "crepe": {"": {"cal": 90, "fat": 4, "carbs": 11, "protein": 3, "sodium": 100, "fiber": 0, "sugar": 2}},
    "crepes": {"": {"cal": 90, "fat": 4, "carbs": 11, "protein": 3, "sodium": 100, "fiber": 0, "sugar": 2}},
    "pound cake": {"slice": {"cal": 220, "fat": 10, "carbs": 28, "protein": 3, "sodium": 180, "fiber": 0.5, "sugar": 18}},

    # Convenience foods
    "cake mix": {"package": {"cal": 1600, "fat": 32, "carbs": 312, "protein": 16, "sodium": 2800, "fiber": 4, "sugar": 168}},
    "pudding mix": {"package": {"cal": 140, "fat": 0, "carbs": 35, "protein": 0, "sodium": 340, "fiber": 0, "sugar": 28}},
    "jello": {"package": {"cal": 80, "fat": 0, "carbs": 19, "protein": 2, "sodium": 120, "fiber": 0, "sugar": 19}},
    "pie filling": {"can": {"cal": 840, "fat": 0, "carbs": 210, "protein": 0, "sodium": 100, "fiber": 4, "sugar": 180}},
    "tater tots": {"cup": {"cal": 200, "fat": 10, "carbs": 24, "protein": 2, "sodium": 400, "fiber": 2, "sugar": 0}},
    "bouillon cube": {"": {"cal": 5, "fat": 0.1, "carbs": 0.6, "protein": 0.5, "sodium": 900, "fiber": 0, "sugar": 0}},

    # Additional vegetables/fruits
    "beets": {"cup": {"cal": 58, "fat": 0.2, "carbs": 13, "protein": 2, "sodium": 106, "fiber": 4, "sugar": 9}},
    "cherry": {"cup": {"cal": 87, "fat": 0.3, "carbs": 22, "protein": 1.5, "sodium": 0, "fiber": 3, "sugar": 18}},
    "cherries": {"cup": {"cal": 87, "fat": 0.3, "carbs": 22, "protein": 1.5, "sodium": 0, "fiber": 3, "sugar": 18}},
    "mandarin oranges": {"cup": {"cal": 72, "fat": 0.2, "carbs": 18, "protein": 1, "sodium": 10, "fiber": 2, "sugar": 14}},
    "prunes": {"cup": {"cal": 418, "fat": 0.7, "carbs": 111, "protein": 4, "sodium": 4, "fiber": 12, "sugar": 66}},
    "barley": {"cup": {"cal": 651, "fat": 2.3, "carbs": 135, "protein": 23, "sodium": 22, "fiber": 32, "sugar": 1}},

    # Condiments & misc
    "horseradish": {"tbsp": {"cal": 7, "fat": 0.1, "carbs": 2, "protein": 0.2, "sodium": 47, "fiber": 0.5, "sugar": 1}},
    "chili sauce": {"tbsp": {"cal": 20, "fat": 0.1, "carbs": 5, "protein": 0.3, "sodium": 200, "fiber": 0.2, "sugar": 3},
                   "cup": {"cal": 320, "fat": 1.6, "carbs": 80, "protein": 4.8, "sodium": 3200, "fiber": 3.2, "sugar": 48}},
    "pickles": {"cup": {"cal": 17, "fat": 0.2, "carbs": 3.7, "protein": 0.4, "sodium": 1208, "fiber": 1, "sugar": 2}},
    "pickle": {"": {"cal": 12, "fat": 0.1, "carbs": 2.7, "protein": 0.3, "sodium": 870, "fiber": 0.8, "sugar": 1}},

    # =========================================================================
    # ADDITIONAL FROM MomsRecipes DATABASE
    # =========================================================================

    # Meat variants & poultry
    "chicken thighs": {"lb": {"cal": 900, "fat": 56, "carbs": 0, "protein": 80, "sodium": 340, "fiber": 0, "sugar": 0}},
    "extra-lean ground beef": {"lb": {"cal": 800, "fat": 48, "carbs": 0, "protein": 88, "sodium": 300, "fiber": 0, "sugar": 0}},
    "pork chops": {"oz": {"cal": 52, "fat": 2.5, "carbs": 0, "protein": 7, "sodium": 18, "fiber": 0, "sugar": 0},
                   "": {"cal": 231, "fat": 13, "carbs": 0, "protein": 26, "sodium": 62, "fiber": 0, "sugar": 0}},
    "spareribs": {"lb": {"cal": 1200, "fat": 96, "carbs": 0, "protein": 80, "sodium": 400, "fiber": 0, "sugar": 0}},
    "lamb": {"lb": {"cal": 1100, "fat": 80, "carbs": 0, "protein": 88, "sodium": 280, "fiber": 0, "sugar": 0}},
    "ground lamb": {"lb": {"cal": 1100, "fat": 80, "carbs": 0, "protein": 88, "sodium": 280, "fiber": 0, "sugar": 0}},
    "lamb chops": {"lb": {"cal": 880, "fat": 60, "carbs": 0, "protein": 84, "sodium": 260, "fiber": 0, "sugar": 0}},
    "guanciale": {"oz": {"cal": 155, "fat": 14, "carbs": 0, "protein": 6, "sodium": 480, "fiber": 0, "sugar": 0}},
    "pancetta": {"oz": {"cal": 145, "fat": 13, "carbs": 0, "protein": 7, "sodium": 500, "fiber": 0, "sugar": 0}},
    "andouille sausage": {"oz": {"cal": 90, "fat": 8, "carbs": 1, "protein": 4, "sodium": 300, "fiber": 0, "sugar": 0}},
    "tofu": {"oz": {"cal": 22, "fat": 1.3, "carbs": 0.5, "protein": 2, "sodium": 2, "fiber": 0, "sugar": 0},
             "cup": {"cal": 176, "fat": 10, "carbs": 4, "protein": 16, "sodium": 16, "fiber": 0, "sugar": 0}},
    "fish": {"oz": {"cal": 35, "fat": 0.8, "carbs": 0, "protein": 7, "sodium": 45, "fiber": 0, "sugar": 0},
             "lb": {"cal": 560, "fat": 13, "carbs": 0, "protein": 112, "sodium": 720, "fiber": 0, "sugar": 0}},

    # Dairy aliases & variants
    "unsalted butter": {"cup": {"cal": 1628, "fat": 184, "carbs": 0, "protein": 2, "sodium": 12, "fiber": 0, "sugar": 0},
                        "tbsp": {"cal": 102, "fat": 11.5, "carbs": 0, "protein": 0.1, "sodium": 1, "fiber": 0, "sugar": 0}},
    "butter or margarine": {"cup": {"cal": 1628, "fat": 184, "carbs": 0, "protein": 2, "sodium": 1284, "fiber": 0, "sugar": 0},
                            "tbsp": {"cal": 102, "fat": 11.5, "carbs": 0, "protein": 0.1, "sodium": 80, "fiber": 0, "sugar": 0}},
    "oleo (margarine)": {"tbsp": {"cal": 100, "fat": 11, "carbs": 0, "protein": 0, "sodium": 90, "fiber": 0, "sugar": 0}},
    "whipping cream": {"cup": {"cal": 821, "fat": 88, "carbs": 7, "protein": 5, "sodium": 89, "fiber": 0, "sugar": 7}},
    "half-and-half": {"cup": {"cal": 315, "fat": 28, "carbs": 10, "protein": 7, "sodium": 98, "fiber": 0, "sugar": 10},
                      "tbsp": {"cal": 20, "fat": 1.7, "carbs": 0.6, "protein": 0.4, "sodium": 6, "fiber": 0, "sugar": 0.6}},
    "shredded cheddar cheese": {"cup": {"cal": 455, "fat": 37, "carbs": 1.5, "protein": 28, "sodium": 700, "fiber": 0, "sugar": 0}},
    "grated parmesan cheese": {"tbsp": {"cal": 22, "fat": 1.4, "carbs": 0.2, "protein": 2, "sodium": 76, "fiber": 0, "sugar": 0},
                               "cup": {"cal": 352, "fat": 22, "carbs": 3, "protein": 32, "sodium": 1216, "fiber": 0, "sugar": 0}},
    "cheese": {"cup": {"cal": 400, "fat": 32, "carbs": 2, "protein": 24, "sodium": 650, "fiber": 0, "sugar": 0},
               "oz": {"cal": 100, "fat": 8, "carbs": 0.5, "protein": 6, "sodium": 162, "fiber": 0, "sugar": 0}},
    "large eggs": {"": {"cal": 72, "fat": 5, "carbs": 0.4, "protein": 6, "sodium": 71, "fiber": 0, "sugar": 0.4}},
    "egg whites": {"": {"cal": 17, "fat": 0, "carbs": 0.2, "protein": 3.6, "sodium": 55, "fiber": 0, "sugar": 0}},
    "egg yolks": {"": {"cal": 55, "fat": 4.5, "carbs": 0.6, "protein": 2.7, "sodium": 8, "fiber": 0, "sugar": 0}},

    # Grains & starches
    "quick oats": {"cup": {"cal": 307, "fat": 5, "carbs": 55, "protein": 11, "sodium": 5, "fiber": 8, "sugar": 1}},
    "oatmeal": {"cup": {"cal": 307, "fat": 5, "carbs": 55, "protein": 11, "sodium": 5, "fiber": 8, "sugar": 1}},
    "noodles": {"cup": {"cal": 220, "fat": 2, "carbs": 40, "protein": 8, "sodium": 10, "fiber": 2, "sugar": 0}},
    "linguine": {"oz": {"cal": 100, "fat": 0.5, "carbs": 20, "protein": 3.5, "sodium": 1, "fiber": 1, "sugar": 0}},
    "elbow macaroni": {"cup": {"cal": 200, "fat": 1, "carbs": 41, "protein": 7, "sodium": 2, "fiber": 2, "sugar": 1}},
    "rotini": {"cup": {"cal": 200, "fat": 1, "carbs": 41, "protein": 7, "sodium": 2, "fiber": 2, "sugar": 1}},
    "fresh chinese noodles": {"oz": {"cal": 100, "fat": 1, "carbs": 20, "protein": 3, "sodium": 150, "fiber": 1, "sugar": 0}},
    "bread crumbs": {"cup": {"cal": 427, "fat": 6, "carbs": 78, "protein": 14, "sodium": 930, "fiber": 3, "sugar": 6}},
    "bread slices": {"": {"cal": 79, "fat": 1, "carbs": 15, "protein": 3, "sodium": 147, "fiber": 1, "sugar": 1}},
    "kashi pilaf": {"cup": {"cal": 170, "fat": 1, "carbs": 34, "protein": 6, "sodium": 0, "fiber": 6, "sugar": 0}},
    "biscuit mix": {"cup": {"cal": 480, "fat": 16, "carbs": 72, "protein": 8, "sodium": 1360, "fiber": 2, "sugar": 8}},
    "bisquick": {"cup": {"cal": 480, "fat": 16, "carbs": 72, "protein": 8, "sodium": 1360, "fiber": 2, "sugar": 8}},
    "graham crackers": {"cup": {"cal": 440, "fat": 10, "carbs": 80, "protein": 6, "sodium": 520, "fiber": 2, "sugar": 24}},
    "graham cracker crust": {"": {"cal": 800, "fat": 36, "carbs": 112, "protein": 8, "sodium": 600, "fiber": 2, "sugar": 40}},

    # Sugar aliases
    "granulated sugar": {"cup": {"cal": 774, "fat": 0, "carbs": 200, "protein": 0, "sodium": 2, "fiber": 0, "sugar": 200},
                         "tbsp": {"cal": 48, "fat": 0, "carbs": 12.5, "protein": 0, "sodium": 0, "fiber": 0, "sugar": 12.5}},
    "white sugar": {"cup": {"cal": 774, "fat": 0, "carbs": 200, "protein": 0, "sodium": 2, "fiber": 0, "sugar": 200}},
    "light brown sugar": {"cup": {"cal": 829, "fat": 0, "carbs": 214, "protein": 0, "sodium": 57, "fiber": 0, "sugar": 212}},
    "packed brown sugar": {"cup": {"cal": 829, "fat": 0, "carbs": 214, "protein": 0, "sodium": 57, "fiber": 0, "sugar": 212}},
    "confectioners' sugar": {"cup": {"cal": 467, "fat": 0, "carbs": 119, "protein": 0, "sodium": 1, "fiber": 0, "sugar": 117}},

    # Oils
    "oil": {"tbsp": {"cal": 120, "fat": 14, "carbs": 0, "protein": 0, "sodium": 0, "fiber": 0, "sugar": 0},
            "cup": {"cal": 1920, "fat": 224, "carbs": 0, "protein": 0, "sodium": 0, "fiber": 0, "sugar": 0}},
    "sesame oil": {"tbsp": {"cal": 120, "fat": 14, "carbs": 0, "protein": 0, "sodium": 0, "fiber": 0, "sugar": 0}},

    # Vegetables
    "onions": {"cup": {"cal": 64, "fat": 0.2, "carbs": 15, "protein": 1.8, "sodium": 6, "fiber": 3, "sugar": 7}},
    "green onions": {"cup": {"cal": 32, "fat": 0.2, "carbs": 7, "protein": 1.8, "sodium": 16, "fiber": 2.6, "sugar": 2.3},
                     "bunch": {"cal": 32, "fat": 0.2, "carbs": 7, "protein": 1.8, "sodium": 16, "fiber": 2.6, "sugar": 2.3}},
    "carrots": {"cup": {"cal": 52, "fat": 0.3, "carbs": 12, "protein": 1.2, "sodium": 88, "fiber": 3.6, "sugar": 6}},
    "tomatoes": {"can": {"cal": 80, "fat": 0.4, "carbs": 16, "protein": 4, "sodium": 600, "fiber": 4, "sugar": 10},
                 "cup": {"cal": 32, "fat": 0.4, "carbs": 7, "protein": 1.6, "sodium": 9, "fiber": 2, "sugar": 5}},
    "potatoes": {"lb": {"cal": 350, "fat": 0.4, "carbs": 80, "protein": 9, "sodium": 28, "fiber": 9, "sugar": 4}},
    "rhubarb": {"cup": {"cal": 26, "fat": 0.2, "carbs": 6, "protein": 1.1, "sodium": 5, "fiber": 2, "sugar": 1.3}},
    "pumpkin": {"cup": {"cal": 83, "fat": 0.3, "carbs": 20, "protein": 3, "sodium": 12, "fiber": 3, "sugar": 8}},
    "okra": {"cup": {"cal": 33, "fat": 0.2, "carbs": 7, "protein": 2, "sodium": 7, "fiber": 3, "sugar": 1}},
    "sauerkraut": {"cup": {"cal": 27, "fat": 0.2, "carbs": 6, "protein": 1.3, "sodium": 939, "fiber": 4, "sugar": 3}},
    "green chilies": {"can": {"cal": 30, "fat": 0, "carbs": 6, "protein": 1, "sodium": 550, "fiber": 2, "sugar": 3}},
    "chopped green chilies": {"can": {"cal": 30, "fat": 0, "carbs": 6, "protein": 1, "sodium": 550, "fiber": 2, "sugar": 3}},
    "frozen mixed vegetables": {"cup": {"cal": 82, "fat": 0.5, "carbs": 16, "protein": 4, "sodium": 64, "fiber": 5, "sugar": 4}},
    "mixed vegetables": {"cup": {"cal": 82, "fat": 0.5, "carbs": 16, "protein": 4, "sodium": 64, "fiber": 5, "sugar": 4}},
    "beans": {"cup": {"cal": 225, "fat": 1, "carbs": 40, "protein": 15, "sodium": 400, "fiber": 12, "sugar": 1}},

    # Fruits
    "calamondin": {"": {"cal": 12, "fat": 0.1, "carbs": 3, "protein": 0.2, "sodium": 1, "fiber": 0.5, "sugar": 1.5}},
    "calamondins": {"cup": {"cal": 60, "fat": 0.5, "carbs": 15, "protein": 1, "sodium": 5, "fiber": 2.5, "sugar": 7.5}},
    "crushed pineapple": {"can": {"cal": 280, "fat": 0.4, "carbs": 68, "protein": 2, "sodium": 4, "fiber": 4, "sugar": 60}},
    "apricots": {"cup": {"cal": 79, "fat": 0.6, "carbs": 18, "protein": 2.3, "sodium": 2, "fiber": 3, "sugar": 15}},
    "dried apricots": {"cup": {"cal": 313, "fat": 0.7, "carbs": 81, "protein": 4.4, "sodium": 13, "fiber": 9.5, "sugar": 69}},
    "lemons": {"": {"cal": 17, "fat": 0.2, "carbs": 5, "protein": 0.6, "sodium": 1, "fiber": 1.6, "sugar": 1.5}},
    "lemon": {"": {"cal": 17, "fat": 0.2, "carbs": 5, "protein": 0.6, "sodium": 1, "fiber": 1.6, "sugar": 1.5}},
    "cranberry juice": {"cup": {"cal": 116, "fat": 0.3, "carbs": 31, "protein": 0, "sodium": 5, "fiber": 0.3, "sugar": 31}},

    # Nuts
    "chopped pecans": {"cup": {"cal": 753, "fat": 78, "carbs": 15, "protein": 10, "sodium": 0, "fiber": 10, "sugar": 4}},
    "pecan halves": {"cup": {"cal": 753, "fat": 78, "carbs": 15, "protein": 10, "sodium": 0, "fiber": 10, "sugar": 4}},
    "chopped nuts": {"cup": {"cal": 800, "fat": 72, "carbs": 24, "protein": 20, "sodium": 5, "fiber": 8, "sugar": 4}},
    "nuts": {"cup": {"cal": 800, "fat": 72, "carbs": 24, "protein": 20, "sodium": 5, "fiber": 8, "sugar": 4}},
    "wheat germ": {"tbsp": {"cal": 26, "fat": 0.7, "carbs": 3.7, "protein": 2, "sodium": 0, "fiber": 1, "sugar": 0},
                   "cup": {"cal": 414, "fat": 11, "carbs": 60, "protein": 27, "sodium": 4, "fiber": 15, "sugar": 0}},

    # Baking & chocolate
    "chocolate": {"oz": {"cal": 155, "fat": 9, "carbs": 17, "protein": 1.4, "sodium": 7, "fiber": 2, "sugar": 14}},
    "unsweetened cocoa": {"tbsp": {"cal": 12, "fat": 0.7, "carbs": 3, "protein": 1, "sodium": 1, "fiber": 2, "sugar": 0}},
    "vanilla": {"tsp": {"cal": 12, "fat": 0, "carbs": 0.5, "protein": 0, "sodium": 0, "fiber": 0, "sugar": 0.5}},
    "lemon extract": {"tsp": {"cal": 10, "fat": 0, "carbs": 0.3, "protein": 0, "sodium": 0, "fiber": 0, "sugar": 0.3}},
    "active dry yeast": {"packet": {"cal": 21, "fat": 0.3, "carbs": 3, "protein": 3, "sodium": 4, "fiber": 1, "sugar": 0}},
    "yellow cake mix": {"package": {"cal": 1600, "fat": 32, "carbs": 312, "protein": 16, "sodium": 2800, "fiber": 4, "sugar": 168}},
    "brownie mix": {"package": {"cal": 1600, "fat": 32, "carbs": 280, "protein": 16, "sodium": 800, "fiber": 4, "sugar": 160}},
    "liquid pectin": {"pouch": {"cal": 10, "fat": 0, "carbs": 3, "protein": 0, "sodium": 5, "fiber": 1, "sugar": 0}},

    # Pie shells
    "pie shell": {"": {"cal": 650, "fat": 40, "carbs": 64, "protein": 8, "sodium": 400, "fiber": 2, "sugar": 2}},
    "baked pie shell": {"": {"cal": 650, "fat": 40, "carbs": 64, "protein": 8, "sodium": 400, "fiber": 2, "sugar": 2}},
    "unbaked pie shell": {"": {"cal": 650, "fat": 40, "carbs": 64, "protein": 8, "sodium": 400, "fiber": 2, "sugar": 2}},

    # Herbs & spices - dried variants
    "ground cinnamon": {"tsp": {"cal": 6, "fat": 0, "carbs": 2, "protein": 0.1, "sodium": 0, "fiber": 1, "sugar": 0}},
    "ground nutmeg": {"tsp": {"cal": 12, "fat": 0.8, "carbs": 1.1, "protein": 0.1, "sodium": 0, "fiber": 0.5, "sugar": 0}},
    "ground ginger": {"tsp": {"cal": 6, "fat": 0.1, "carbs": 1.3, "protein": 0.2, "sodium": 1, "fiber": 0.2, "sugar": 0.1}},
    "ground cumin": {"tsp": {"cal": 8, "fat": 0.5, "carbs": 0.9, "protein": 0.4, "sodium": 4, "fiber": 0.2, "sugar": 0}},
    "fresh ginger": {"tbsp": {"cal": 5, "fat": 0, "carbs": 1, "protein": 0.1, "sodium": 1, "fiber": 0.1, "sugar": 0.1},
                    "slice": {"cal": 2, "fat": 0, "carbs": 0.5, "protein": 0, "sodium": 0, "fiber": 0, "sugar": 0},
                    "inch": {"cal": 8, "fat": 0, "carbs": 2, "protein": 0.2, "sodium": 1, "fiber": 0.2, "sugar": 0.2},
                    "": {"cal": 8, "fat": 0, "carbs": 2, "protein": 0.2, "sodium": 1, "fiber": 0.2, "sugar": 0.2}},
    "fresh parsley": {"tbsp": {"cal": 1, "fat": 0, "carbs": 0.2, "protein": 0.1, "sodium": 2, "fiber": 0.1, "sugar": 0}},
    "fresh dill": {"tbsp": {"cal": 1, "fat": 0, "carbs": 0.1, "protein": 0.1, "sodium": 2, "fiber": 0, "sugar": 0}},
    "dried dill": {"tsp": {"cal": 3, "fat": 0.1, "carbs": 0.5, "protein": 0.2, "sodium": 2, "fiber": 0.1, "sugar": 0}},
    "dried oregano": {"tsp": {"cal": 3, "fat": 0.1, "carbs": 0.7, "protein": 0.1, "sodium": 0, "fiber": 0.4, "sugar": 0}},
    "dried thyme": {"tsp": {"cal": 3, "fat": 0.1, "carbs": 0.6, "protein": 0.1, "sodium": 1, "fiber": 0.3, "sugar": 0}},
    "dried parsley": {"tbsp": {"cal": 4, "fat": 0.1, "carbs": 0.6, "protein": 0.3, "sodium": 6, "fiber": 0.2, "sugar": 0.1}},
    "dried parsley flakes": {"tbsp": {"cal": 4, "fat": 0.1, "carbs": 0.6, "protein": 0.3, "sodium": 6, "fiber": 0.2, "sugar": 0.1}},
    "parsley flakes": {"tbsp": {"cal": 4, "fat": 0.1, "carbs": 0.6, "protein": 0.3, "sodium": 6, "fiber": 0.2, "sugar": 0.1}},
    "turmeric": {"tsp": {"cal": 8, "fat": 0.2, "carbs": 1.4, "protein": 0.3, "sodium": 1, "fiber": 0.5, "sugar": 0.1}},
    "poultry seasoning": {"tsp": {"cal": 5, "fat": 0.2, "carbs": 1, "protein": 0.1, "sodium": 0, "fiber": 0.2, "sugar": 0}},
    "white pepper": {"tsp": {"cal": 7, "fat": 0.1, "carbs": 1.6, "protein": 0.3, "sodium": 0, "fiber": 0.6, "sugar": 0}},
    "salt and pepper": {"tsp": {"cal": 3, "fat": 0, "carbs": 0.7, "protein": 0.1, "sodium": 1163, "fiber": 0.3, "sugar": 0}},
    "seasoned salt": {"tsp": {"cal": 0, "fat": 0, "carbs": 0, "protein": 0, "sodium": 1360, "fiber": 0, "sugar": 0}},
    "garlic salt": {"tsp": {"cal": 3, "fat": 0, "carbs": 0.7, "protein": 0.1, "sodium": 1480, "fiber": 0, "sugar": 0}},

    # Condiments & sauces
    "oyster sauce": {"tbsp": {"cal": 9, "fat": 0, "carbs": 2, "protein": 0.2, "sodium": 437, "fiber": 0, "sugar": 1}},
    "white vinegar": {"tbsp": {"cal": 3, "fat": 0, "carbs": 0, "protein": 0, "sodium": 0, "fiber": 0, "sugar": 0}},
    "tabasco sauce": {"tsp": {"cal": 1, "fat": 0, "carbs": 0, "protein": 0, "sodium": 124, "fiber": 0, "sugar": 0}},
    "marinara sauce": {"cup": {"cal": 80, "fat": 2, "carbs": 12, "protein": 2, "sodium": 560, "fiber": 2, "sugar": 8}},

    # Alcohol
    "wine": {"cup": {"cal": 200, "fat": 0, "carbs": 5, "protein": 0.2, "sodium": 12, "fiber": 0, "sugar": 2}},
    "chinese cooking wine": {"tbsp": {"cal": 15, "fat": 0, "carbs": 2, "protein": 0, "sodium": 180, "fiber": 0, "sugar": 1}},
    "sherry": {"oz": {"cal": 45, "fat": 0, "carbs": 2, "protein": 0.1, "sodium": 3, "fiber": 0, "sugar": 1},
               "tbsp": {"cal": 22, "fat": 0, "carbs": 1, "protein": 0, "sodium": 2, "fiber": 0, "sugar": 0.5}},
    "brandy": {"oz": {"cal": 64, "fat": 0, "carbs": 0, "protein": 0, "sodium": 0, "fiber": 0, "sugar": 0},
               "tbsp": {"cal": 32, "fat": 0, "carbs": 0, "protein": 0, "sodium": 0, "fiber": 0, "sugar": 0}},

    # Water variants
    "warm water": {"cup": {"cal": 0, "fat": 0, "carbs": 0, "protein": 0, "sodium": 0, "fiber": 0, "sugar": 0}},
    "hot water": {"cup": {"cal": 0, "fat": 0, "carbs": 0, "protein": 0, "sodium": 0, "fiber": 0, "sugar": 0}},
    "cold water": {"cup": {"cal": 0, "fat": 0, "carbs": 0, "protein": 0, "sodium": 0, "fiber": 0, "sugar": 0}},
    "boiling water": {"cup": {"cal": 0, "fat": 0, "carbs": 0, "protein": 0, "sodium": 0, "fiber": 0, "sugar": 0}},

    # Miscellaneous
    "miniature marshmallows": {"cup": {"cal": 159, "fat": 0.1, "carbs": 41, "protein": 1.4, "sodium": 22, "fiber": 0, "sugar": 29}},
    "pretzels": {"cup": {"cal": 229, "fat": 2, "carbs": 48, "protein": 5, "sodium": 814, "fiber": 2, "sugar": 1}},
    "chex cereal": {"cup": {"cal": 110, "fat": 0.5, "carbs": 25, "protein": 2, "sodium": 220, "fiber": 1, "sugar": 2}},
    "lemon rind": {"tbsp": {"cal": 3, "fat": 0, "carbs": 1, "protein": 0.1, "sodium": 0, "fiber": 0.4, "sugar": 0.4}},
    "grated lemon rind": {"tbsp": {"cal": 3, "fat": 0, "carbs": 1, "protein": 0.1, "sodium": 0, "fiber": 0.4, "sugar": 0.4}},
    "grated lemon peel": {"tbsp": {"cal": 3, "fat": 0, "carbs": 1, "protein": 0.1, "sodium": 0, "fiber": 0.4, "sugar": 0.4}},
    "orange peel": {"tbsp": {"cal": 6, "fat": 0, "carbs": 2, "protein": 0.1, "sodium": 0, "fiber": 0.6, "sugar": 1}},
    "grated orange peel": {"tbsp": {"cal": 6, "fat": 0, "carbs": 2, "protein": 0.1, "sodium": 0, "fiber": 0.6, "sugar": 1}},
    "food coloring": {"drop": {"cal": 0, "fat": 0, "carbs": 0, "protein": 0, "sodium": 0, "fiber": 0, "sugar": 0}},
    "green food coloring": {"drop": {"cal": 0, "fat": 0, "carbs": 0, "protein": 0, "sodium": 0, "fiber": 0, "sugar": 0}},
    "red food coloring": {"drop": {"cal": 0, "fat": 0, "carbs": 0, "protein": 0, "sodium": 0, "fiber": 0, "sugar": 0}},
    "vegetable cooking spray": {"": {"cal": 0, "fat": 0, "carbs": 0, "protein": 0, "sodium": 0, "fiber": 0, "sugar": 0}},
    "nonstick cooking spray": {"": {"cal": 0, "fat": 0, "carbs": 0, "protein": 0, "sodium": 0, "fiber": 0, "sugar": 0}},

    # =========================================================================
    # ADDITIONAL FROM MomsRecipes DATABASE - ROUND 2
    # =========================================================================

    # Beverages
    "cola": {"cup": {"cal": 97, "fat": 0, "carbs": 26, "protein": 0, "sodium": 7, "fiber": 0, "sugar": 26}},
    "soda": {"cup": {"cal": 97, "fat": 0, "carbs": 26, "protein": 0, "sodium": 7, "fiber": 0, "sugar": 26}},
    "ginger ale": {"cup": {"cal": 83, "fat": 0, "carbs": 21, "protein": 0, "sodium": 26, "fiber": 0, "sugar": 21}},
    "apple juice": {"cup": {"cal": 114, "fat": 0.3, "carbs": 28, "protein": 0.2, "sodium": 10, "fiber": 0.2, "sugar": 24}},
    "grape juice": {"cup": {"cal": 152, "fat": 0.2, "carbs": 37, "protein": 1, "sodium": 13, "fiber": 0.3, "sugar": 36}},
    "limeade": {"cup": {"cal": 104, "fat": 0, "carbs": 27, "protein": 0.1, "sodium": 5, "fiber": 0, "sugar": 26}},
    "lemonade": {"cup": {"cal": 99, "fat": 0.1, "carbs": 26, "protein": 0.2, "sodium": 7, "fiber": 0.2, "sugar": 25}},
    "cranberry juice": {"cup": {"cal": 116, "fat": 0.3, "carbs": 31, "protein": 0, "sodium": 5, "fiber": 0.3, "sugar": 31}},
    "tomato juice": {"cup": {"cal": 41, "fat": 0.1, "carbs": 10, "protein": 1.8, "sodium": 654, "fiber": 1, "sugar": 8}},
    "v8 juice": {"cup": {"cal": 46, "fat": 0.1, "carbs": 10, "protein": 1.5, "sodium": 480, "fiber": 1.5, "sugar": 7}},
    "prune juice": {"cup": {"cal": 182, "fat": 0.1, "carbs": 45, "protein": 1.6, "sodium": 10, "fiber": 2.6, "sugar": 42}},

    # Proteins - meats & poultry
    "veal": {"lb": {"cal": 800, "fat": 32, "carbs": 0, "protein": 120, "sodium": 340, "fiber": 0, "sugar": 0}},
    "duck": {"lb": {"cal": 1300, "fat": 100, "carbs": 0, "protein": 88, "sodium": 280, "fiber": 0, "sugar": 0}},
    "liver": {"lb": {"cal": 600, "fat": 16, "carbs": 16, "protein": 92, "sodium": 300, "fiber": 0, "sugar": 0}},
    "sweetbreads": {"lb": {"cal": 680, "fat": 32, "carbs": 0, "protein": 92, "sodium": 400, "fiber": 0, "sugar": 0},
                   "": {"cal": 170, "fat": 8, "carbs": 0, "protein": 23, "sodium": 100, "fiber": 0, "sugar": 0}},
    "chicken liver": {"lb": {"cal": 600, "fat": 16, "carbs": 3, "protein": 84, "sodium": 320, "fiber": 0, "sugar": 0}},
    "hot dog": {"each": {"cal": 151, "fat": 13, "carbs": 2, "protein": 5, "sodium": 567, "fiber": 0, "sugar": 1}},
    "hot dogs": {"each": {"cal": 151, "fat": 13, "carbs": 2, "protein": 5, "sodium": 567, "fiber": 0, "sugar": 1}},
    "frankfurter": {"each": {"cal": 151, "fat": 13, "carbs": 2, "protein": 5, "sodium": 567, "fiber": 0, "sugar": 1}},
    "pepperoni": {"oz": {"cal": 138, "fat": 12, "carbs": 0.9, "protein": 6, "sodium": 463, "fiber": 0, "sugar": 0}},
    "salami": {"oz": {"cal": 119, "fat": 10, "carbs": 0.5, "protein": 6, "sodium": 529, "fiber": 0, "sugar": 0}},
    "prosciutto": {"oz": {"cal": 55, "fat": 3, "carbs": 0.3, "protein": 7, "sodium": 520, "fiber": 0, "sugar": 0}},
    "corned beef": {"lb": {"cal": 800, "fat": 48, "carbs": 2, "protein": 88, "sodium": 3200, "fiber": 0, "sugar": 0}},

    # Proteins - seafood
    "halibut": {"lb": {"cal": 500, "fat": 10, "carbs": 0, "protein": 96, "sodium": 260, "fiber": 0, "sugar": 0}},
    "catfish": {"lb": {"cal": 544, "fat": 24, "carbs": 0, "protein": 80, "sodium": 200, "fiber": 0, "sugar": 0}},
    "scallops": {"lb": {"cal": 400, "fat": 4, "carbs": 8, "protein": 76, "sodium": 700, "fiber": 0, "sugar": 0}},
    "sea scallops": {"lb": {"cal": 400, "fat": 4, "carbs": 8, "protein": 76, "sodium": 700, "fiber": 0, "sugar": 0}},
    "oysters": {"cup": {"cal": 169, "fat": 6, "carbs": 10, "protein": 17, "sodium": 521, "fiber": 0, "sugar": 0}},
    "mussels": {"lb": {"cal": 350, "fat": 8, "carbs": 16, "protein": 48, "sodium": 1200, "fiber": 0, "sugar": 0}},
    "sardines": {"can": {"cal": 191, "fat": 11, "carbs": 0, "protein": 23, "sodium": 465, "fiber": 0, "sugar": 0}},
    "anchovies": {"can": {"cal": 95, "fat": 4, "carbs": 0, "protein": 13, "sodium": 1650, "fiber": 0, "sugar": 0}},
    "anchovy fillets": {"each": {"cal": 8, "fat": 0.4, "carbs": 0, "protein": 1, "sodium": 147, "fiber": 0, "sugar": 0}},
    "cod": {"lb": {"cal": 372, "fat": 3, "carbs": 0, "protein": 80, "sodium": 220, "fiber": 0, "sugar": 0}},
    "sole": {"lb": {"cal": 360, "fat": 4, "carbs": 0, "protein": 76, "sodium": 360, "fiber": 0, "sugar": 0}},
    "flounder": {"lb": {"cal": 360, "fat": 4, "carbs": 0, "protein": 76, "sodium": 360, "fiber": 0, "sugar": 0}},
    "perch": {"lb": {"cal": 420, "fat": 4, "carbs": 0, "protein": 88, "sodium": 300, "fiber": 0, "sugar": 0}},
    "trout": {"lb": {"cal": 600, "fat": 24, "carbs": 0, "protein": 92, "sodium": 220, "fiber": 0, "sugar": 0}},
    "swordfish": {"lb": {"cal": 548, "fat": 16, "carbs": 0, "protein": 92, "sodium": 420, "fiber": 0, "sugar": 0}},
    "mahi mahi": {"lb": {"cal": 384, "fat": 4, "carbs": 0, "protein": 84, "sodium": 400, "fiber": 0, "sugar": 0}},

    # Legumes
    "navy beans": {"cup": {"cal": 255, "fat": 1, "carbs": 47, "protein": 15, "sodium": 0, "fiber": 19, "sugar": 0}},
    "lima beans": {"cup": {"cal": 216, "fat": 0.7, "carbs": 39, "protein": 15, "sodium": 29, "fiber": 13, "sugar": 6}},
    "chickpeas": {"cup": {"cal": 269, "fat": 4, "carbs": 45, "protein": 15, "sodium": 11, "fiber": 12.5, "sugar": 8}},
    "garbanzo beans": {"cup": {"cal": 269, "fat": 4, "carbs": 45, "protein": 15, "sodium": 11, "fiber": 12.5, "sugar": 8}},
    "lentils": {"cup": {"cal": 230, "fat": 0.8, "carbs": 40, "protein": 18, "sodium": 4, "fiber": 16, "sugar": 4}},
    "split peas": {"cup": {"cal": 231, "fat": 0.8, "carbs": 41, "protein": 16, "sodium": 4, "fiber": 16, "sugar": 6}},
    "hummus": {"cup": {"cal": 435, "fat": 21, "carbs": 50, "protein": 20, "sodium": 960, "fiber": 15, "sugar": 0}},

    # Dairy
    "ricotta cheese": {"cup": {"cal": 428, "fat": 32, "carbs": 7.5, "protein": 28, "sodium": 307, "fiber": 0, "sugar": 0.6}},
    "ricotta": {"cup": {"cal": 428, "fat": 32, "carbs": 7.5, "protein": 28, "sodium": 307, "fiber": 0, "sugar": 0.6}},
    "blue cheese": {"oz": {"cal": 100, "fat": 8, "carbs": 0.7, "protein": 6, "sodium": 325, "fiber": 0, "sugar": 0.1}},
    "feta cheese": {"oz": {"cal": 75, "fat": 6, "carbs": 1, "protein": 4, "sodium": 316, "fiber": 0, "sugar": 1}},
    "feta": {"oz": {"cal": 75, "fat": 6, "carbs": 1, "protein": 4, "sodium": 316, "fiber": 0, "sugar": 1}},
    "goat cheese": {"oz": {"cal": 76, "fat": 6, "carbs": 0, "protein": 5, "sodium": 104, "fiber": 0, "sugar": 0}},
    "gorgonzola": {"oz": {"cal": 100, "fat": 9, "carbs": 1, "protein": 6, "sodium": 375, "fiber": 0, "sugar": 0}},
    "gorgonzola cheese": {"oz": {"cal": 100, "fat": 9, "carbs": 1, "protein": 6, "sodium": 375, "fiber": 0, "sugar": 0}},
    "string cheese": {"each": {"cal": 80, "fat": 6, "carbs": 1, "protein": 7, "sodium": 200, "fiber": 0, "sugar": 0}},
    "mozzarella string cheese": {"each": {"cal": 80, "fat": 6, "carbs": 1, "protein": 7, "sodium": 200, "fiber": 0, "sugar": 0}},
    "crème fraîche": {"cup": {"cal": 450, "fat": 45, "carbs": 3, "protein": 3, "sodium": 40, "fiber": 0, "sugar": 3},
                     "tbsp": {"cal": 28, "fat": 2.8, "carbs": 0.2, "protein": 0.2, "sodium": 2, "fiber": 0, "sugar": 0.2}},
    "creme fraiche": {"cup": {"cal": 450, "fat": 45, "carbs": 3, "protein": 3, "sodium": 40, "fiber": 0, "sugar": 3},
                     "tbsp": {"cal": 28, "fat": 2.8, "carbs": 0.2, "protein": 0.2, "sodium": 2, "fiber": 0, "sugar": 0.2}},
    "ice cream": {"cup": {"cal": 273, "fat": 15, "carbs": 31, "protein": 5, "sodium": 100, "fiber": 0.7, "sugar": 28}},
    "vanilla ice cream": {"cup": {"cal": 273, "fat": 15, "carbs": 31, "protein": 5, "sodium": 100, "fiber": 0.7, "sugar": 28}},
    "sweetened condensed milk": {"can": {"cal": 982, "fat": 27, "carbs": 166, "protein": 24, "sodium": 389, "fiber": 0, "sugar": 166}},
    "mascarpone": {"cup": {"cal": 920, "fat": 96, "carbs": 4, "protein": 8, "sodium": 80, "fiber": 0, "sugar": 4}},
    "queso fresco": {"oz": {"cal": 80, "fat": 6, "carbs": 1, "protein": 5, "sodium": 180, "fiber": 0, "sugar": 0}},

    # Produce - vegetables
    "artichoke": {"each": {"cal": 60, "fat": 0.2, "carbs": 13, "protein": 4, "sodium": 120, "fiber": 6.5, "sugar": 1}},
    "artichoke hearts": {"cup": {"cal": 90, "fat": 0.3, "carbs": 20, "protein": 6, "sodium": 180, "fiber": 9, "sugar": 2}},
    "parsnips": {"cup": {"cal": 100, "fat": 0.4, "carbs": 24, "protein": 1.6, "sodium": 13, "fiber": 6.5, "sugar": 6}},
    "parsnip": {"cup": {"cal": 100, "fat": 0.4, "carbs": 24, "protein": 1.6, "sodium": 13, "fiber": 6.5, "sugar": 6},
                "": {"cal": 75, "fat": 0.3, "carbs": 18, "protein": 1.2, "sodium": 10, "fiber": 5, "sugar": 4.5}},
    "radish": {"cup": {"cal": 19, "fat": 0.1, "carbs": 4, "protein": 0.8, "sodium": 45, "fiber": 1.9, "sugar": 2}},
    "radishes": {"cup": {"cal": 19, "fat": 0.1, "carbs": 4, "protein": 0.8, "sodium": 45, "fiber": 1.9, "sugar": 2}},
    "turnip": {"cup": {"cal": 36, "fat": 0.1, "carbs": 8, "protein": 1, "sodium": 87, "fiber": 2.3, "sugar": 5}},
    "turnips": {"cup": {"cal": 36, "fat": 0.1, "carbs": 8, "protein": 1, "sodium": 87, "fiber": 2.3, "sugar": 5}},
    "watercress": {"cup": {"cal": 4, "fat": 0, "carbs": 0.4, "protein": 0.8, "sodium": 14, "fiber": 0.2, "sugar": 0.1}},
    "shallot": {"tbsp": {"cal": 7, "fat": 0, "carbs": 2, "protein": 0.3, "sodium": 1, "fiber": 0, "sugar": 0.8},
               "": {"cal": 28, "fat": 0, "carbs": 7, "protein": 1, "sodium": 5, "fiber": 0, "sugar": 3}},
    "shallots": {"tbsp": {"cal": 7, "fat": 0, "carbs": 2, "protein": 0.3, "sodium": 1, "fiber": 0, "sugar": 0.8},
                "": {"cal": 28, "fat": 0, "carbs": 7, "protein": 1, "sodium": 5, "fiber": 0, "sugar": 3}},
    "leek": {"cup": {"cal": 54, "fat": 0.3, "carbs": 13, "protein": 1.3, "sodium": 18, "fiber": 1.6, "sugar": 3.5}},
    "leeks": {"cup": {"cal": 54, "fat": 0.3, "carbs": 13, "protein": 1.3, "sodium": 18, "fiber": 1.6, "sugar": 3.5}},
    "fennel": {"cup": {"cal": 27, "fat": 0.2, "carbs": 6, "protein": 1, "sodium": 45, "fiber": 3, "sugar": 3}},
    "fennel bulb": {"cup": {"cal": 27, "fat": 0.2, "carbs": 6, "protein": 1, "sodium": 45, "fiber": 3, "sugar": 3}},
    "rutabaga": {"cup": {"cal": 52, "fat": 0.3, "carbs": 12, "protein": 1.5, "sodium": 28, "fiber": 3, "sugar": 7}},
    "kohlrabi": {"cup": {"cal": 36, "fat": 0.1, "carbs": 8, "protein": 2, "sodium": 27, "fiber": 5, "sugar": 4}},
    "jicama": {"cup": {"cal": 46, "fat": 0.1, "carbs": 11, "protein": 0.9, "sodium": 5, "fiber": 6, "sugar": 2}},
    "bok choy": {"cup": {"cal": 9, "fat": 0.1, "carbs": 1.5, "protein": 1, "sodium": 46, "fiber": 0.7, "sugar": 0.8}},
    "swiss chard": {"cup": {"cal": 7, "fat": 0.1, "carbs": 1.4, "protein": 0.6, "sodium": 77, "fiber": 0.6, "sugar": 0.4}},
    "collard greens": {"cup": {"cal": 11, "fat": 0.2, "carbs": 2, "protein": 1, "sodium": 6, "fiber": 1.4, "sugar": 0.2}},
    "mustard greens": {"cup": {"cal": 15, "fat": 0.2, "carbs": 3, "protein": 1.5, "sodium": 14, "fiber": 2, "sugar": 0.8}},

    # Produce - fruits
    "blackberries": {"cup": {"cal": 62, "fat": 0.7, "carbs": 14, "protein": 2, "sodium": 1, "fiber": 7.6, "sugar": 7}},
    "cantaloupe": {"cup": {"cal": 53, "fat": 0.3, "carbs": 13, "protein": 1.3, "sodium": 25, "fiber": 1.4, "sugar": 12}},
    "figs": {"each": {"cal": 37, "fat": 0.2, "carbs": 10, "protein": 0.4, "sodium": 1, "fiber": 1.5, "sugar": 8}},
    "dried figs": {"cup": {"cal": 371, "fat": 1.4, "carbs": 95, "protein": 5, "sodium": 14, "fiber": 14.6, "sugar": 71}},
    "honeydew": {"cup": {"cal": 61, "fat": 0.2, "carbs": 15, "protein": 0.9, "sodium": 30, "fiber": 1.4, "sugar": 14}},
    "honeydew melon": {"cup": {"cal": 61, "fat": 0.2, "carbs": 15, "protein": 0.9, "sodium": 30, "fiber": 1.4, "sugar": 14}},
    "kiwi": {"each": {"cal": 42, "fat": 0.4, "carbs": 10, "protein": 0.8, "sodium": 2, "fiber": 2.1, "sugar": 6}},
    "kiwi fruit": {"each": {"cal": 42, "fat": 0.4, "carbs": 10, "protein": 0.8, "sodium": 2, "fiber": 2.1, "sugar": 6}},
    "mango": {"each": {"cal": 202, "fat": 1.3, "carbs": 50, "protein": 2.8, "sodium": 3, "fiber": 5.4, "sugar": 45}},
    "papaya": {"cup": {"cal": 55, "fat": 0.2, "carbs": 14, "protein": 0.8, "sodium": 4, "fiber": 2.5, "sugar": 8}},
    "passion fruit": {"each": {"cal": 17, "fat": 0.1, "carbs": 4, "protein": 0.4, "sodium": 5, "fiber": 1.9, "sugar": 2}},
    "pomegranate": {"each": {"cal": 234, "fat": 3.3, "carbs": 53, "protein": 4.7, "sodium": 8, "fiber": 11, "sugar": 39}},
    "pomegranate seeds": {"cup": {"cal": 144, "fat": 2, "carbs": 33, "protein": 3, "sodium": 5, "fiber": 7, "sugar": 24}},
    "persimmon": {"each": {"cal": 118, "fat": 0.3, "carbs": 31, "protein": 1, "sodium": 2, "fiber": 6, "sugar": 21}},
    "guava": {"each": {"cal": 37, "fat": 0.5, "carbs": 8, "protein": 1.4, "sodium": 1, "fiber": 3, "sugar": 5}},
    "star fruit": {"each": {"cal": 28, "fat": 0.3, "carbs": 6, "protein": 1, "sodium": 2, "fiber": 2.5, "sugar": 4}},
    "tangerine": {"each": {"cal": 47, "fat": 0.3, "carbs": 12, "protein": 0.7, "sodium": 2, "fiber": 1.6, "sugar": 9}},
    "clementine": {"each": {"cal": 35, "fat": 0.1, "carbs": 9, "protein": 0.6, "sodium": 1, "fiber": 1.3, "sugar": 7}},
    "nectarine": {"each": {"cal": 63, "fat": 0.5, "carbs": 15, "protein": 1.5, "sodium": 0, "fiber": 2.4, "sugar": 11}},
    "plantain": {"each": {"cal": 218, "fat": 0.5, "carbs": 57, "protein": 2, "sodium": 6, "fiber": 4, "sugar": 27}},

    # Grains
    "stuffing mix": {"cup": {"cal": 356, "fat": 17, "carbs": 44, "protein": 6, "sodium": 1086, "fiber": 3, "sugar": 4}},
    "corn flakes": {"cup": {"cal": 101, "fat": 0.2, "carbs": 24, "protein": 2, "sodium": 203, "fiber": 0.7, "sugar": 3}},
    "bran": {"cup": {"cal": 125, "fat": 2.5, "carbs": 37, "protein": 9, "sodium": 1, "fiber": 25, "sugar": 0}},
    "wheat bran": {"cup": {"cal": 125, "fat": 2.5, "carbs": 37, "protein": 9, "sodium": 1, "fiber": 25, "sugar": 0}},
    "oat bran": {"cup": {"cal": 231, "fat": 6.5, "carbs": 62, "protein": 16, "sodium": 4, "fiber": 14.5, "sugar": 1}},
    "wild rice": {"cup": {"cal": 166, "fat": 0.6, "carbs": 35, "protein": 6.5, "sodium": 5, "fiber": 3, "sugar": 1}},
    "grits": {"cup": {"cal": 143, "fat": 0.5, "carbs": 31, "protein": 3, "sodium": 5, "fiber": 1, "sugar": 0}},
    "polenta": {"cup": {"cal": 143, "fat": 0.5, "carbs": 31, "protein": 3, "sodium": 5, "fiber": 1, "sugar": 0}},
    "couscous": {"cup": {"cal": 176, "fat": 0.3, "carbs": 36, "protein": 6, "sodium": 8, "fiber": 2.2, "sugar": 0}},
    "quinoa": {"cup": {"cal": 222, "fat": 4, "carbs": 39, "protein": 8, "sodium": 13, "fiber": 5, "sugar": 0}},
    "bulgur": {"cup": {"cal": 151, "fat": 0.4, "carbs": 34, "protein": 6, "sodium": 9, "fiber": 8, "sugar": 0}},
    "farro": {"cup": {"cal": 200, "fat": 1.5, "carbs": 40, "protein": 8, "sodium": 0, "fiber": 5, "sugar": 0}},
    "barley": {"cup": {"cal": 193, "fat": 0.7, "carbs": 44, "protein": 4, "sodium": 5, "fiber": 6, "sugar": 0.4}},
    "pearl barley": {"cup": {"cal": 193, "fat": 0.7, "carbs": 44, "protein": 4, "sodium": 5, "fiber": 6, "sugar": 0.4}},
    "millet": {"cup": {"cal": 207, "fat": 1.7, "carbs": 41, "protein": 6, "sodium": 3, "fiber": 2.3, "sugar": 0}},
    "buckwheat": {"cup": {"cal": 155, "fat": 1, "carbs": 34, "protein": 6, "sodium": 7, "fiber": 4.5, "sugar": 0}},
    "orzo": {"cup": {"cal": 200, "fat": 0.9, "carbs": 42, "protein": 7, "sodium": 0, "fiber": 2, "sugar": 0}},

    # Nuts & seeds
    "macadamia nuts": {"cup": {"cal": 962, "fat": 102, "carbs": 18, "protein": 10, "sodium": 6, "fiber": 11, "sugar": 6}},
    "macadamias": {"cup": {"cal": 962, "fat": 102, "carbs": 18, "protein": 10, "sodium": 6, "fiber": 11, "sugar": 6}},
    "pine nuts": {"cup": {"cal": 909, "fat": 92, "carbs": 18, "protein": 18, "sodium": 3, "fiber": 5, "sugar": 5}},
    "pignoli": {"cup": {"cal": 909, "fat": 92, "carbs": 18, "protein": 18, "sodium": 3, "fiber": 5, "sugar": 5}},
    "hazelnuts": {"cup": {"cal": 848, "fat": 82, "carbs": 23, "protein": 20, "sodium": 0, "fiber": 13, "sugar": 6}},
    "filberts": {"cup": {"cal": 848, "fat": 82, "carbs": 23, "protein": 20, "sodium": 0, "fiber": 13, "sugar": 6}},
    "pistachios": {"cup": {"cal": 685, "fat": 55, "carbs": 34, "protein": 25, "sodium": 1, "fiber": 13, "sugar": 9}},
    "poppy seeds": {"tbsp": {"cal": 46, "fat": 4, "carbs": 2, "protein": 1.6, "sodium": 2, "fiber": 0.5, "sugar": 0.3}},
    "tahini": {"tbsp": {"cal": 89, "fat": 8, "carbs": 3, "protein": 2.6, "sodium": 17, "fiber": 0.7, "sugar": 0}},
    "sesame paste": {"tbsp": {"cal": 89, "fat": 8, "carbs": 3, "protein": 2.6, "sodium": 17, "fiber": 0.7, "sugar": 0}},
    "pumpkin seeds": {"cup": {"cal": 285, "fat": 12, "carbs": 34, "protein": 12, "sodium": 12, "fiber": 12, "sugar": 0}},
    "pepitas": {"cup": {"cal": 285, "fat": 12, "carbs": 34, "protein": 12, "sodium": 12, "fiber": 12, "sugar": 0}},
    "chia seeds": {"tbsp": {"cal": 58, "fat": 4, "carbs": 5, "protein": 2, "sodium": 2, "fiber": 4, "sugar": 0}},
    "hemp seeds": {"tbsp": {"cal": 57, "fat": 4, "carbs": 1, "protein": 3, "sodium": 0, "fiber": 0.3, "sugar": 0}},

    # Canned goods
    "rotel": {"can": {"cal": 50, "fat": 0, "carbs": 10, "protein": 2, "sodium": 890, "fiber": 2, "sugar": 6}},
    "bamboo shoots": {"cup": {"cal": 25, "fat": 0.5, "carbs": 4, "protein": 2.5, "sodium": 9, "fiber": 2, "sugar": 3}},
    "water chestnuts": {"cup": {"cal": 60, "fat": 0.1, "carbs": 15, "protein": 1, "sodium": 9, "fiber": 2, "sugar": 3}},
    "fruit cocktail": {"cup": {"cal": 110, "fat": 0, "carbs": 28, "protein": 0.5, "sodium": 10, "fiber": 2.5, "sugar": 26}},
    "mandarin oranges": {"cup": {"cal": 72, "fat": 0.1, "carbs": 19, "protein": 1, "sodium": 12, "fiber": 1.8, "sugar": 16}},
    "crushed pineapple": {"cup": {"cal": 109, "fat": 0.2, "carbs": 28, "protein": 0.8, "sodium": 2, "fiber": 2, "sugar": 25}},
    "pineapple chunks": {"cup": {"cal": 109, "fat": 0.2, "carbs": 28, "protein": 0.8, "sodium": 2, "fiber": 2, "sugar": 25}},
    "pineapple tidbits": {"cup": {"cal": 109, "fat": 0.2, "carbs": 28, "protein": 0.8, "sodium": 2, "fiber": 2, "sugar": 25}},
    "sliced pineapple": {"cup": {"cal": 109, "fat": 0.2, "carbs": 28, "protein": 0.8, "sodium": 2, "fiber": 2, "sugar": 25}},
    "hearts of palm": {"cup": {"cal": 41, "fat": 0.9, "carbs": 7, "protein": 4, "sodium": 622, "fiber": 3.5, "sugar": 0}},
    "palm hearts": {"cup": {"cal": 41, "fat": 0.9, "carbs": 7, "protein": 4, "sodium": 622, "fiber": 3.5, "sugar": 0}},

    # Sauces & condiments
    "pesto": {"tbsp": {"cal": 80, "fat": 8, "carbs": 1, "protein": 2, "sodium": 125, "fiber": 0, "sugar": 0}},
    "basil pesto": {"tbsp": {"cal": 80, "fat": 8, "carbs": 1, "protein": 2, "sodium": 125, "fiber": 0, "sugar": 0}},
    "sun-dried tomato pesto": {"tbsp": {"cal": 70, "fat": 6, "carbs": 3, "protein": 1, "sodium": 160, "fiber": 0.5, "sugar": 2}},
    "aioli": {"tbsp": {"cal": 100, "fat": 11, "carbs": 0.5, "protein": 0.3, "sodium": 110, "fiber": 0, "sugar": 0}},
    "chipotle mayo": {"tbsp": {"cal": 100, "fat": 11, "carbs": 0.5, "protein": 0.1, "sodium": 140, "fiber": 0, "sugar": 0}},
    "sriracha mayo": {"tbsp": {"cal": 100, "fat": 11, "carbs": 1, "protein": 0.1, "sodium": 160, "fiber": 0, "sugar": 0.5}},
    "tartar sauce": {"tbsp": {"cal": 74, "fat": 8, "carbs": 1, "protein": 0.2, "sodium": 107, "fiber": 0, "sugar": 1}},
    "cocktail sauce": {"tbsp": {"cal": 20, "fat": 0, "carbs": 5, "protein": 0.3, "sodium": 270, "fiber": 0, "sugar": 4}},
    "hoisin sauce": {"tbsp": {"cal": 35, "fat": 0.5, "carbs": 7, "protein": 0.5, "sodium": 258, "fiber": 0.4, "sugar": 5}},
    "fish sauce": {"tbsp": {"cal": 6, "fat": 0, "carbs": 0.7, "protein": 0.9, "sodium": 1413, "fiber": 0, "sugar": 0}},
    "oyster sauce": {"tbsp": {"cal": 9, "fat": 0, "carbs": 2, "protein": 0.2, "sodium": 492, "fiber": 0, "sugar": 1}},
    "miso paste": {"tbsp": {"cal": 34, "fat": 1, "carbs": 4.5, "protein": 2, "sodium": 634, "fiber": 0.9, "sugar": 1}},
    "white miso": {"tbsp": {"cal": 34, "fat": 1, "carbs": 4.5, "protein": 2, "sodium": 634, "fiber": 0.9, "sugar": 1}},
    "red miso": {"tbsp": {"cal": 35, "fat": 1, "carbs": 5, "protein": 2, "sodium": 750, "fiber": 1, "sugar": 1}},
    "sambal oelek": {"tbsp": {"cal": 15, "fat": 0, "carbs": 3, "protein": 0.5, "sodium": 600, "fiber": 1, "sugar": 1}},
    "gochujang": {"tbsp": {"cal": 40, "fat": 1, "carbs": 8, "protein": 1, "sodium": 410, "fiber": 1, "sugar": 4}},
    "harissa": {"tbsp": {"cal": 15, "fat": 0.5, "carbs": 2.5, "protein": 0.5, "sodium": 95, "fiber": 0.5, "sugar": 1}},
    "chili garlic sauce": {"tbsp": {"cal": 20, "fat": 0.5, "carbs": 4, "protein": 0.5, "sodium": 450, "fiber": 0.5, "sugar": 2}},
    "duck sauce": {"tbsp": {"cal": 60, "fat": 0, "carbs": 15, "protein": 0, "sodium": 75, "fiber": 0, "sugar": 13}},
    "plum sauce": {"tbsp": {"cal": 35, "fat": 0, "carbs": 8, "protein": 0.2, "sodium": 180, "fiber": 0.2, "sugar": 6}},
    "sweet chili sauce": {"tbsp": {"cal": 40, "fat": 0, "carbs": 10, "protein": 0.1, "sodium": 220, "fiber": 0, "sugar": 9}},
    "ponzu": {"tbsp": {"cal": 10, "fat": 0, "carbs": 2, "protein": 0.5, "sodium": 600, "fiber": 0, "sugar": 1}},

    # Prepared foods
    "pizza dough": {"lb": {"cal": 1100, "fat": 6, "carbs": 220, "protein": 32, "sodium": 1600, "fiber": 8, "sugar": 4}},
    "pie crust": {"each": {"cal": 620, "fat": 39, "carbs": 60, "protein": 7, "sodium": 420, "fiber": 2, "sugar": 2}},
    "puff pastry": {"sheet": {"cal": 850, "fat": 56, "carbs": 72, "protein": 11, "sodium": 420, "fiber": 2, "sugar": 1}},
    "phyllo dough": {"sheet": {"cal": 57, "fat": 1, "carbs": 10, "protein": 1.4, "sodium": 92, "fiber": 0.4, "sugar": 0}},
    "wonton wrappers": {"each": {"cal": 23, "fat": 0.4, "carbs": 4.6, "protein": 0.8, "sodium": 46, "fiber": 0.2, "sugar": 0}},
    "egg roll wrappers": {"each": {"cal": 93, "fat": 1.6, "carbs": 18, "protein": 3, "sodium": 183, "fiber": 0.6, "sugar": 0}},
    "tortilla chips": {"cup": {"cal": 200, "fat": 10, "carbs": 24, "protein": 2.5, "sodium": 170, "fiber": 2, "sugar": 0.5}},
    "croutons": {"cup": {"cal": 122, "fat": 2, "carbs": 22, "protein": 4, "sodium": 210, "fiber": 1.5, "sugar": 1}},

    # =========================================================================
    # GAP ANALYSIS - ROUND 3 (most common missing ingredients)
    # =========================================================================

    # Syrups & sweeteners
    "light corn syrup": {"cup": {"cal": 925, "fat": 0, "carbs": 251, "protein": 0, "sodium": 395, "fiber": 0, "sugar": 251}},
    "dark corn syrup": {"cup": {"cal": 925, "fat": 0, "carbs": 251, "protein": 0, "sodium": 210, "fiber": 0, "sugar": 251}},
    "superfine sugar": {"cup": {"cal": 774, "fat": 0, "carbs": 200, "protein": 0, "sodium": 2, "fiber": 0, "sugar": 200}},
    "caster sugar": {"cup": {"cal": 774, "fat": 0, "carbs": 200, "protein": 0, "sodium": 2, "fiber": 0, "sugar": 200}},
    "raw sugar": {"cup": {"cal": 774, "fat": 0, "carbs": 200, "protein": 0, "sodium": 2, "fiber": 0, "sugar": 200}},
    "turbinado sugar": {"cup": {"cal": 774, "fat": 0, "carbs": 200, "protein": 0, "sodium": 2, "fiber": 0, "sugar": 200}},
    "demerara sugar": {"cup": {"cal": 774, "fat": 0, "carbs": 200, "protein": 0, "sodium": 2, "fiber": 0, "sugar": 200}},
    "muscovado sugar": {"cup": {"cal": 760, "fat": 0, "carbs": 196, "protein": 0, "sodium": 6, "fiber": 0, "sugar": 196}},

    # Dried fruits
    "currants": {"cup": {"cal": 408, "fat": 0.4, "carbs": 107, "protein": 6, "sodium": 12, "fiber": 10, "sugar": 93}},
    "dried currants": {"cup": {"cal": 408, "fat": 0.4, "carbs": 107, "protein": 6, "sodium": 12, "fiber": 10, "sugar": 93}},
    "citron": {"cup": {"cal": 320, "fat": 0.3, "carbs": 82, "protein": 0.5, "sodium": 290, "fiber": 5, "sugar": 73}},
    "candied citron": {"cup": {"cal": 320, "fat": 0.3, "carbs": 82, "protein": 0.5, "sodium": 290, "fiber": 5, "sugar": 73}},
    "maraschino cherries": {"each": {"cal": 8, "fat": 0, "carbs": 2, "protein": 0, "sodium": 0, "fiber": 0, "sugar": 2}},
    "candied cherries": {"cup": {"cal": 160, "fat": 0, "carbs": 40, "protein": 0, "sodium": 30, "fiber": 0, "sugar": 36}},

    # Condiments & sauces
    "catsup": {"tbsp": {"cal": 17, "fat": 0, "carbs": 4.5, "protein": 0.2, "sodium": 154, "fiber": 0, "sugar": 3.5}},
    "ketchup": {"tbsp": {"cal": 17, "fat": 0, "carbs": 4.5, "protein": 0.2, "sodium": 154, "fiber": 0, "sugar": 3.5}},
    "dijon mustard": {"tbsp": {"cal": 15, "fat": 1, "carbs": 1, "protein": 1, "sodium": 360, "fiber": 0.5, "sugar": 0}},
    "prepared mustard": {"tbsp": {"cal": 10, "fat": 0.6, "carbs": 0.8, "protein": 0.6, "sodium": 168, "fiber": 0.4, "sugar": 0.3}},
    "yellow mustard": {"tbsp": {"cal": 10, "fat": 0.6, "carbs": 0.8, "protein": 0.6, "sodium": 168, "fiber": 0.4, "sugar": 0.3}},
    "stone ground mustard": {"tbsp": {"cal": 15, "fat": 1, "carbs": 1, "protein": 1, "sodium": 200, "fiber": 0.5, "sugar": 0}},
    "salad dressing": {"tbsp": {"cal": 60, "fat": 5, "carbs": 3, "protein": 0, "sodium": 160, "fiber": 0, "sugar": 2}},
    "thousand island dressing": {"tbsp": {"cal": 59, "fat": 5.6, "carbs": 2.4, "protein": 0.1, "sodium": 138, "fiber": 0, "sugar": 2}},
    "ranch dressing": {"tbsp": {"cal": 73, "fat": 7.7, "carbs": 0.5, "protein": 0.1, "sodium": 122, "fiber": 0, "sugar": 0.4}},
    "blue cheese dressing": {"tbsp": {"cal": 77, "fat": 8, "carbs": 0.6, "protein": 0.4, "sodium": 167, "fiber": 0, "sugar": 0.5}},
    "italian dressing": {"tbsp": {"cal": 35, "fat": 3, "carbs": 1.5, "protein": 0, "sodium": 146, "fiber": 0, "sugar": 1}},
    "sweet pickle": {"each": {"cal": 32, "fat": 0, "carbs": 9, "protein": 0.1, "sodium": 160, "fiber": 0.3, "sugar": 7}},
    "sweet pickle relish": {"tbsp": {"cal": 20, "fat": 0.1, "carbs": 5, "protein": 0.1, "sodium": 122, "fiber": 0.2, "sugar": 4}},
    "dill pickle relish": {"tbsp": {"cal": 4, "fat": 0.1, "carbs": 1, "protein": 0, "sodium": 210, "fiber": 0.2, "sugar": 0.5}},

    # Vegetables
    "pimiento": {"oz": {"cal": 6, "fat": 0.1, "carbs": 1.3, "protein": 0.2, "sodium": 4, "fiber": 0.4, "sugar": 0.8},
                "tbsp": {"cal": 3, "fat": 0, "carbs": 0.6, "protein": 0.1, "sodium": 2, "fiber": 0.2, "sugar": 0.4},
                "": {"cal": 6, "fat": 0.1, "carbs": 1.3, "protein": 0.2, "sodium": 4, "fiber": 0.4, "sugar": 0.8}},
    "pimentos": {"oz": {"cal": 6, "fat": 0.1, "carbs": 1.3, "protein": 0.2, "sodium": 4, "fiber": 0.4, "sugar": 0.8},
                "": {"cal": 6, "fat": 0.1, "carbs": 1.3, "protein": 0.2, "sodium": 4, "fiber": 0.4, "sugar": 0.8}},
    "water chestnuts": {"can": {"cal": 66, "fat": 0.1, "carbs": 15, "protein": 1, "sodium": 11, "fiber": 2, "sugar": 3},
                       "cup": {"cal": 60, "fat": 0.1, "carbs": 13, "protein": 1, "sodium": 10, "fiber": 2, "sugar": 3}},
    "jicama": {"cup": {"cal": 46, "fat": 0.1, "carbs": 11, "protein": 0.9, "sodium": 5, "fiber": 6, "sugar": 2}},
    "mango": {"cup": {"cal": 99, "fat": 0.6, "carbs": 25, "protein": 1.4, "sodium": 2, "fiber": 2.6, "sugar": 23},
             "": {"cal": 135, "fat": 0.8, "carbs": 35, "protein": 1.9, "sodium": 3, "fiber": 3.7, "sugar": 31}},
    "green peppers": {"cup": {"cal": 30, "fat": 0.3, "carbs": 7, "protein": 1.3, "sodium": 4, "fiber": 2.5, "sugar": 4}},
    "red peppers": {"cup": {"cal": 39, "fat": 0.4, "carbs": 9, "protein": 1.5, "sodium": 6, "fiber": 3, "sugar": 6}},
    "apples": {"each": {"cal": 95, "fat": 0.3, "carbs": 25, "protein": 0.5, "sodium": 2, "fiber": 4.4, "sugar": 19}},
    "apple": {"each": {"cal": 95, "fat": 0.3, "carbs": 25, "protein": 0.5, "sodium": 2, "fiber": 4.4, "sugar": 19}},
    "bananas": {"each": {"cal": 105, "fat": 0.4, "carbs": 27, "protein": 1.3, "sodium": 1, "fiber": 3.1, "sugar": 14}},
    "banana": {"each": {"cal": 105, "fat": 0.4, "carbs": 27, "protein": 1.3, "sodium": 1, "fiber": 3.1, "sugar": 14}},
    "peaches": {"each": {"cal": 59, "fat": 0.4, "carbs": 14, "protein": 1.4, "sodium": 0, "fiber": 2.3, "sugar": 13}},
    "peach": {"each": {"cal": 59, "fat": 0.4, "carbs": 14, "protein": 1.4, "sodium": 0, "fiber": 2.3, "sugar": 13}},

    # Dairy & cream
    "light cream": {"cup": {"cal": 468, "fat": 46, "carbs": 9, "protein": 6, "sodium": 95, "fiber": 0, "sugar": 9}},
    "coffee cream": {"cup": {"cal": 468, "fat": 46, "carbs": 9, "protein": 6, "sodium": 95, "fiber": 0, "sugar": 9}},
    "table cream": {"cup": {"cal": 468, "fat": 46, "carbs": 9, "protein": 6, "sodium": 95, "fiber": 0, "sugar": 9}},
    "sour milk": {"cup": {"cal": 98, "fat": 2.4, "carbs": 12, "protein": 8, "sodium": 257, "fiber": 0, "sugar": 12}},
    "buttermilk powder": {"tbsp": {"cal": 25, "fat": 0.4, "carbs": 3, "protein": 2, "sodium": 34, "fiber": 0, "sugar": 3}},
    "rich milk": {"cup": {"cal": 150, "fat": 8, "carbs": 12, "protein": 8, "sodium": 105, "fiber": 0, "sugar": 12}},
    "plain yogurt": {"cup": {"cal": 149, "fat": 8, "carbs": 11, "protein": 9, "sodium": 113, "fiber": 0, "sugar": 11}},
    "greek yogurt": {"cup": {"cal": 190, "fat": 10, "carbs": 8, "protein": 18, "sodium": 65, "fiber": 0, "sugar": 7}},

    # Cheese variations
    "sharp cheddar cheese": {"cup": {"cal": 455, "fat": 37, "carbs": 1.4, "protein": 28, "sodium": 701, "fiber": 0, "sugar": 0.5}},
    "mild cheddar cheese": {"cup": {"cal": 455, "fat": 37, "carbs": 1.4, "protein": 28, "sodium": 621, "fiber": 0, "sugar": 0.5}},
    "monterey jack cheese": {"cup": {"cal": 421, "fat": 34, "carbs": 0.7, "protein": 28, "sodium": 603, "fiber": 0, "sugar": 0.5}},
    "pepper jack cheese": {"cup": {"cal": 421, "fat": 34, "carbs": 0.7, "protein": 28, "sodium": 650, "fiber": 0, "sugar": 0.5}},
    "colby cheese": {"cup": {"cal": 445, "fat": 36, "carbs": 2.9, "protein": 27, "sodium": 684, "fiber": 0, "sugar": 0.5}},
    "american cheese": {"slice": {"cal": 104, "fat": 9, "carbs": 0.5, "protein": 5, "sodium": 406, "fiber": 0, "sugar": 0.3}},
    "velveeta": {"oz": {"cal": 80, "fat": 6, "carbs": 3, "protein": 4, "sodium": 410, "fiber": 0, "sugar": 2}},

    # Spices & seasonings
    "cayenne": {"tsp": {"cal": 6, "fat": 0.3, "carbs": 1, "protein": 0.2, "sodium": 1, "fiber": 0.5, "sugar": 0.2}},
    "cayenne pepper": {"tsp": {"cal": 6, "fat": 0.3, "carbs": 1, "protein": 0.2, "sodium": 1, "fiber": 0.5, "sugar": 0.2}},
    "mace": {"tsp": {"cal": 8, "fat": 0.6, "carbs": 0.9, "protein": 0.1, "sodium": 1, "fiber": 0.3, "sugar": 0}},
    "ground mace": {"tsp": {"cal": 8, "fat": 0.6, "carbs": 0.9, "protein": 0.1, "sodium": 1, "fiber": 0.3, "sugar": 0}},
    "whole cloves": {"tsp": {"cal": 7, "fat": 0.4, "carbs": 1.3, "protein": 0.1, "sodium": 5, "fiber": 0.7, "sugar": 0.5}},
    "celery seed": {"tsp": {"cal": 8, "fat": 0.5, "carbs": 0.8, "protein": 0.4, "sodium": 3, "fiber": 0.2, "sugar": 0}},
    "celery salt": {"tsp": {"cal": 6, "fat": 0.3, "carbs": 0.6, "protein": 0.3, "sodium": 1280, "fiber": 0.2, "sugar": 0}},
    "cinnamon stick": {"each": {"cal": 6, "fat": 0, "carbs": 2, "protein": 0.1, "sodium": 0, "fiber": 1.4, "sugar": 0}},
    "cinnamon sticks": {"each": {"cal": 6, "fat": 0, "carbs": 2, "protein": 0.1, "sodium": 0, "fiber": 1.4, "sugar": 0}},
    "red pepper flakes": {"tsp": {"cal": 6, "fat": 0.3, "carbs": 1, "protein": 0.2, "sodium": 0, "fiber": 0.5, "sugar": 0.2}},
    "crushed red pepper": {"tsp": {"cal": 6, "fat": 0.3, "carbs": 1, "protein": 0.2, "sodium": 0, "fiber": 0.5, "sugar": 0.2}},
    "ground coriander": {"tsp": {"cal": 5, "fat": 0.3, "carbs": 1, "protein": 0.2, "sodium": 1, "fiber": 0.8, "sugar": 0}},
    "freshly grated nutmeg": {"tsp": {"cal": 12, "fat": 0.8, "carbs": 1, "protein": 0.1, "sodium": 0, "fiber": 0.5, "sugar": 0.1}},
    "cream tartar": {"tsp": {"cal": 8, "fat": 0, "carbs": 1.8, "protein": 0, "sodium": 2, "fiber": 0, "sugar": 0}},
    "cream of tartar": {"tsp": {"cal": 8, "fat": 0, "carbs": 1.8, "protein": 0, "sodium": 2, "fiber": 0, "sugar": 0}},

    # Flavorings
    "rose water": {"tbsp": {"cal": 0, "fat": 0, "carbs": 0, "protein": 0, "sodium": 0, "fiber": 0, "sugar": 0}},
    "rose-water": {"tbsp": {"cal": 0, "fat": 0, "carbs": 0, "protein": 0, "sodium": 0, "fiber": 0, "sugar": 0}},
    "orange extract": {"tsp": {"cal": 12, "fat": 0, "carbs": 0.3, "protein": 0, "sodium": 0, "fiber": 0, "sugar": 0}},
    "lemon extract": {"tsp": {"cal": 12, "fat": 0, "carbs": 0.3, "protein": 0, "sodium": 0, "fiber": 0, "sugar": 0}},
    "almond extract": {"tsp": {"cal": 12, "fat": 0, "carbs": 0.3, "protein": 0, "sodium": 0, "fiber": 0, "sugar": 0}},
    "peppermint extract": {"tsp": {"cal": 12, "fat": 0, "carbs": 0.3, "protein": 0, "sodium": 0, "fiber": 0, "sugar": 0}},
    "rum extract": {"tsp": {"cal": 12, "fat": 0, "carbs": 0.3, "protein": 0, "sodium": 0, "fiber": 0, "sugar": 0}},
    "maple extract": {"tsp": {"cal": 12, "fat": 0, "carbs": 0.3, "protein": 0, "sodium": 0, "fiber": 0, "sugar": 0}},
    "coconut extract": {"tsp": {"cal": 12, "fat": 0, "carbs": 0.3, "protein": 0, "sodium": 0, "fiber": 0, "sugar": 0}},

    # Flours & starches
    "pastry flour": {"cup": {"cal": 400, "fat": 1, "carbs": 84, "protein": 9, "sodium": 2, "fiber": 2, "sugar": 0}},
    "whole wheat pastry flour": {"cup": {"cal": 400, "fat": 2, "carbs": 80, "protein": 12, "sodium": 2, "fiber": 12, "sugar": 0}},
    "cake flour": {"cup": {"cal": 400, "fat": 1, "carbs": 85, "protein": 8, "sodium": 2, "fiber": 2, "sugar": 0}},
    "bread flour": {"cup": {"cal": 495, "fat": 1.5, "carbs": 99, "protein": 16, "sodium": 2, "fiber": 3.4, "sugar": 0.3},
                   "oz": {"cal": 110, "fat": 0.3, "carbs": 22, "protein": 3.6, "sodium": 0, "fiber": 0.8, "sugar": 0.1},
                   "g": {"cal": 3.9, "fat": 0.01, "carbs": 0.78, "protein": 0.13, "sodium": 0, "fiber": 0.03, "sugar": 0}},
    "self-rising flour": {"cup": {"cal": 443, "fat": 1.2, "carbs": 93, "protein": 12, "sodium": 1588, "fiber": 3, "sugar": 0}},
    "yellow cornmeal": {"cup": {"cal": 442, "fat": 4, "carbs": 94, "protein": 10, "sodium": 4, "fiber": 9, "sugar": 1}},
    "white cornmeal": {"cup": {"cal": 442, "fat": 4, "carbs": 94, "protein": 10, "sodium": 4, "fiber": 9, "sugar": 1}},
    "corn meal": {"cup": {"cal": 442, "fat": 4, "carbs": 94, "protein": 10, "sodium": 4, "fiber": 9, "sugar": 1}},
    "indian meal": {"cup": {"cal": 442, "fat": 4, "carbs": 94, "protein": 10, "sodium": 4, "fiber": 9, "sugar": 1}},
    "corn starch": {"tbsp": {"cal": 30, "fat": 0, "carbs": 7, "protein": 0, "sodium": 0, "fiber": 0, "sugar": 0}},
    "tapioca starch": {"tbsp": {"cal": 30, "fat": 0, "carbs": 7, "protein": 0, "sodium": 0, "fiber": 0, "sugar": 0}},
    "arrowroot": {"tbsp": {"cal": 29, "fat": 0, "carbs": 7, "protein": 0.1, "sodium": 0, "fiber": 0.4, "sugar": 0}},
    "dry bread crumbs": {"cup": {"cal": 427, "fat": 6, "carbs": 78, "protein": 14, "sodium": 791, "fiber": 5, "sugar": 6}},
    "panko": {"cup": {"cal": 220, "fat": 2, "carbs": 44, "protein": 6, "sodium": 300, "fiber": 2, "sugar": 2}},
    "panko bread crumbs": {"cup": {"cal": 220, "fat": 2, "carbs": 44, "protein": 6, "sodium": 300, "fiber": 2, "sugar": 2}},

    # Fats & oils
    "salad oil": {"tbsp": {"cal": 120, "fat": 14, "carbs": 0, "protein": 0, "sodium": 0, "fiber": 0, "sugar": 0}},
    "drippings": {"tbsp": {"cal": 115, "fat": 13, "carbs": 0, "protein": 0, "sodium": 0, "fiber": 0, "sugar": 0}},
    "bacon drippings": {"tbsp": {"cal": 115, "fat": 13, "carbs": 0, "protein": 0, "sodium": 0, "fiber": 0, "sugar": 0}},
    "bacon grease": {"tbsp": {"cal": 115, "fat": 13, "carbs": 0, "protein": 0, "sodium": 0, "fiber": 0, "sugar": 0}},
    "fat": {"tbsp": {"cal": 115, "fat": 13, "carbs": 0, "protein": 0, "sodium": 0, "fiber": 0, "sugar": 0}},
    "salt pork": {"oz": {"cal": 212, "fat": 23, "carbs": 0, "protein": 1.4, "sodium": 404, "fiber": 0, "sugar": 0}},
    "fatback": {"oz": {"cal": 212, "fat": 23, "carbs": 0, "protein": 1.4, "sodium": 404, "fiber": 0, "sugar": 0}},
    "suet": {"oz": {"cal": 242, "fat": 27, "carbs": 0, "protein": 0.4, "sodium": 2, "fiber": 0, "sugar": 0}},

    # Meats
    "chicken wings": {"lb": {"cal": 960, "fat": 68, "carbs": 0, "protein": 80, "sodium": 360, "fiber": 0, "sugar": 0}},
    "chicken wing": {"each": {"cal": 43, "fat": 3, "carbs": 0, "protein": 4, "sodium": 16, "fiber": 0, "sugar": 0}},
    "ground italian sausage": {"lb": {"cal": 1360, "fat": 112, "carbs": 4, "protein": 68, "sodium": 1500, "fiber": 0, "sugar": 0}},
    "italian sausage links": {"each": {"cal": 286, "fat": 23, "carbs": 1, "protein": 16, "sodium": 756, "fiber": 0, "sugar": 0}},
    "breakfast sausage": {"lb": {"cal": 1360, "fat": 112, "carbs": 0, "protein": 64, "sodium": 1400, "fiber": 0, "sugar": 0}},
    "polish sausage": {"lb": {"cal": 1280, "fat": 104, "carbs": 8, "protein": 68, "sodium": 2800, "fiber": 0, "sugar": 0}},
    "kielbasa": {"lb": {"cal": 1280, "fat": 104, "carbs": 8, "protein": 68, "sodium": 2800, "fiber": 0, "sugar": 0}},
    "andouille sausage": {"lb": {"cal": 1200, "fat": 96, "carbs": 8, "protein": 68, "sodium": 3200, "fiber": 0, "sugar": 0}},
    "chorizo": {"lb": {"cal": 1550, "fat": 132, "carbs": 8, "protein": 72, "sodium": 2700, "fiber": 0, "sugar": 0}},

    # Rice & grains
    "instant rice": {"cup": {"cal": 190, "fat": 0.4, "carbs": 42, "protein": 4, "sodium": 5, "fiber": 1, "sugar": 0}},
    "minute rice": {"cup": {"cal": 190, "fat": 0.4, "carbs": 42, "protein": 4, "sodium": 5, "fiber": 1, "sugar": 0}},
    "converted rice": {"cup": {"cal": 200, "fat": 0.5, "carbs": 44, "protein": 4, "sodium": 5, "fiber": 1, "sugar": 0}},
    "arborio rice": {"cup": {"cal": 200, "fat": 0.4, "carbs": 45, "protein": 4, "sodium": 0, "fiber": 1, "sugar": 0}},
    "jasmine rice": {"cup": {"cal": 205, "fat": 0.4, "carbs": 45, "protein": 4, "sodium": 2, "fiber": 0.6, "sugar": 0}},
    "basmati rice": {"cup": {"cal": 205, "fat": 0.4, "carbs": 45, "protein": 4, "sodium": 2, "fiber": 0.6, "sugar": 0}},
    "sushi rice": {"cup": {"cal": 200, "fat": 0.4, "carbs": 44, "protein": 4, "sodium": 0, "fiber": 0.6, "sugar": 0}},

    # Canned goods
    "tomato sauce": {"cup": {"cal": 59, "fat": 0.5, "carbs": 13, "protein": 2.6, "sodium": 1116, "fiber": 3, "sugar": 9}},
    "mushrooms": {"can": {"cal": 39, "fat": 0.5, "carbs": 8, "protein": 3, "sodium": 660, "fiber": 4, "sugar": 2},
                 "cup": {"cal": 15, "fat": 0.2, "carbs": 2.3, "protein": 2.2, "sodium": 4, "fiber": 0.7, "sugar": 1},
                 "oz": {"cal": 6, "fat": 0.1, "carbs": 0.9, "protein": 0.9, "sodium": 1, "fiber": 0.3, "sugar": 0.6}},
    "canned mushrooms": {"cup": {"cal": 33, "fat": 0.3, "carbs": 6, "protein": 2.5, "sodium": 561, "fiber": 2, "sugar": 2}},

    # Wine & alcohol
    "dry white wine": {"cup": {"cal": 194, "fat": 0, "carbs": 5, "protein": 0, "sodium": 10, "fiber": 0, "sugar": 1}},
    "dry sherry": {"cup": {"cal": 255, "fat": 0, "carbs": 10, "protein": 0, "sodium": 20, "fiber": 0, "sugar": 2}},
    "cooking sherry": {"cup": {"cal": 225, "fat": 0, "carbs": 8, "protein": 0, "sodium": 1100, "fiber": 0, "sugar": 4}},
    "marsala wine": {"cup": {"cal": 320, "fat": 0, "carbs": 28, "protein": 0, "sodium": 20, "fiber": 0, "sugar": 18}},
    "port wine": {"cup": {"cal": 370, "fat": 0, "carbs": 36, "protein": 0, "sodium": 20, "fiber": 0, "sugar": 30}},
    "madeira wine": {"cup": {"cal": 330, "fat": 0, "carbs": 32, "protein": 0, "sodium": 20, "fiber": 0, "sugar": 20}},
    "sake": {"cup": {"cal": 195, "fat": 0, "carbs": 7.5, "protein": 0.7, "sodium": 3, "fiber": 0, "sugar": 0}},

    # Chocolate & cocoa
    "semisweet chocolate": {"oz": {"cal": 136, "fat": 9, "carbs": 15, "protein": 1.2, "sodium": 2, "fiber": 1.8, "sugar": 13}},
    "bittersweet chocolate": {"oz": {"cal": 136, "fat": 9, "carbs": 13, "protein": 1.4, "sodium": 4, "fiber": 2, "sugar": 10}},
    "unsweetened chocolate": {"oz": {"cal": 145, "fat": 15, "carbs": 8, "protein": 3, "sodium": 4, "fiber": 5, "sugar": 0}},
    "baking chocolate": {"oz": {"cal": 145, "fat": 15, "carbs": 8, "protein": 3, "sodium": 4, "fiber": 5, "sugar": 0}},
    "white chocolate": {"oz": {"cal": 153, "fat": 9, "carbs": 17, "protein": 1.5, "sodium": 25, "fiber": 0, "sugar": 17}},
    "german chocolate": {"oz": {"cal": 140, "fat": 8, "carbs": 16, "protein": 1, "sodium": 5, "fiber": 1.5, "sugar": 14}},
    "dutch-process cocoa powder": {"tbsp": {"cal": 12, "fat": 0.7, "carbs": 3, "protein": 1, "sodium": 0, "fiber": 2, "sugar": 0}},
    "natural cocoa powder": {"tbsp": {"cal": 12, "fat": 0.7, "carbs": 3, "protein": 1, "sodium": 0, "fiber": 2, "sugar": 0}},

    # Miscellaneous
    "pistachio nuts": {"cup": {"cal": 685, "fat": 55, "carbs": 34, "protein": 25, "sodium": 1, "fiber": 13, "sugar": 9}},
    "slivered almonds": {"cup": {"cal": 624, "fat": 54, "carbs": 22, "protein": 23, "sodium": 1, "fiber": 12, "sugar": 5}},
    "sliced almonds": {"cup": {"cal": 530, "fat": 46, "carbs": 18, "protein": 20, "sodium": 1, "fiber": 10, "sugar": 4}},
    "almond meal": {"cup": {"cal": 640, "fat": 56, "carbs": 24, "protein": 24, "sodium": 0, "fiber": 14, "sugar": 5}},
    "lukewarm water": {"cup": {"cal": 0, "fat": 0, "carbs": 0, "protein": 0, "sodium": 0, "fiber": 0, "sugar": 0}},
    "warm water": {"cup": {"cal": 0, "fat": 0, "carbs": 0, "protein": 0, "sodium": 0, "fiber": 0, "sugar": 0}},
    "cider vinegar": {"tbsp": {"cal": 3, "fat": 0, "carbs": 0.1, "protein": 0, "sodium": 1, "fiber": 0, "sugar": 0.1}},
    "apple cider vinegar": {"tbsp": {"cal": 3, "fat": 0, "carbs": 0.1, "protein": 0, "sodium": 1, "fiber": 0, "sugar": 0.1}},
    "kitchen bouquet": {"tsp": {"cal": 15, "fat": 0, "carbs": 4, "protein": 0, "sodium": 10, "fiber": 0, "sugar": 3}},
    "truvia": {"packet": {"cal": 0, "fat": 0, "carbs": 3, "protein": 0, "sodium": 0, "fiber": 0, "sugar": 0}},
    "truvia natural sweetener": {"packet": {"cal": 0, "fat": 0, "carbs": 3, "protein": 0, "sodium": 0, "fiber": 0, "sugar": 0}},
    "truvia natural sweetener spoonable": {"tsp": {"cal": 0, "fat": 0, "carbs": 1, "protein": 0, "sodium": 0, "fiber": 0, "sugar": 0}},
    "splenda": {"packet": {"cal": 0, "fat": 0, "carbs": 1, "protein": 0, "sodium": 0, "fiber": 0, "sugar": 0}},
    "stevia": {"packet": {"cal": 0, "fat": 0, "carbs": 1, "protein": 0, "sodium": 0, "fiber": 0, "sugar": 0}},

    # =========================================================================
    # GAP ANALYSIS - ROUND 4 (remaining missing ingredients)
    # =========================================================================

    # Vegetables
    "sweet potatoes": {"lb": {"cal": 390, "fat": 0.4, "carbs": 90, "protein": 7, "sodium": 250, "fiber": 14, "sugar": 18}},
    "sweet potato": {"each": {"cal": 112, "fat": 0.1, "carbs": 26, "protein": 2, "sodium": 72, "fiber": 4, "sugar": 5}},
    "acorn squash": {"cup": {"cal": 56, "fat": 0.1, "carbs": 15, "protein": 1, "sodium": 4, "fiber": 2, "sugar": 0}},
    "butternut squash": {"cup": {"cal": 63, "fat": 0.1, "carbs": 16, "protein": 1.4, "sodium": 6, "fiber": 2.8, "sugar": 3}},
    "spaghetti squash": {"cup": {"cal": 31, "fat": 0.6, "carbs": 7, "protein": 0.6, "sodium": 17, "fiber": 1.5, "sugar": 2.5}},
    "button mushrooms": {"cup": {"cal": 15, "fat": 0.2, "carbs": 2.3, "protein": 2.2, "sodium": 4, "fiber": 0.7, "sugar": 1}},
    "black olives": {"cup": {"cal": 142, "fat": 13, "carbs": 8, "protein": 1, "sodium": 735, "fiber": 3, "sugar": 0}},
    "green olives": {"cup": {"cal": 145, "fat": 15, "carbs": 4, "protein": 1, "sodium": 1556, "fiber": 3, "sugar": 0}},
    "kalamata olives": {"cup": {"cal": 196, "fat": 17, "carbs": 10, "protein": 2, "sodium": 1840, "fiber": 3, "sugar": 0}},
    "plum tomato": {"each": {"cal": 11, "fat": 0.1, "carbs": 2.4, "protein": 0.5, "sodium": 3, "fiber": 0.7, "sugar": 1.6}},
    "stalk celery": {"each": {"cal": 6, "fat": 0.1, "carbs": 1, "protein": 0.3, "sodium": 32, "fiber": 0.6, "sugar": 0.6}},
    "celery stalks": {"each": {"cal": 6, "fat": 0.1, "carbs": 1, "protein": 0.3, "sodium": 32, "fiber": 0.6, "sugar": 0.6}},

    # Nuts & seeds
    "blanched almonds": {"cup": {"cal": 624, "fat": 54, "carbs": 22, "protein": 23, "sodium": 1, "fiber": 12, "sugar": 5}},
    "nut meats": {"cup": {"cal": 785, "fat": 79, "carbs": 16, "protein": 18, "sodium": 1, "fiber": 8, "sugar": 3}},
    "walnut meats": {"cup": {"cal": 785, "fat": 79, "carbs": 16, "protein": 18, "sodium": 1, "fiber": 8, "sugar": 3}},
    "fennel seeds": {"tsp": {"cal": 7, "fat": 0.3, "carbs": 1, "protein": 0.3, "sodium": 2, "fiber": 0.8, "sugar": 0}},
    "mustard seeds": {"tsp": {"cal": 15, "fat": 1, "carbs": 1, "protein": 0.8, "sodium": 0, "fiber": 0.4, "sugar": 0}},

    # Proteins
    "cooked chicken": {"cup": {"cal": 231, "fat": 5, "carbs": 0, "protein": 43, "sodium": 104, "fiber": 0, "sugar": 0}},
    "frying chicken": {"lb": {"cal": 960, "fat": 68, "carbs": 0, "protein": 80, "sodium": 360, "fiber": 0, "sugar": 0}},
    "smoked salmon": {"oz": {"cal": 33, "fat": 1.2, "carbs": 0, "protein": 5, "sodium": 222, "fiber": 0, "sugar": 0}},

    # Juices
    "pineapple juice": {"cup": {"cal": 132, "fat": 0.3, "carbs": 32, "protein": 0.9, "sodium": 5, "fiber": 0.5, "sugar": 25}},

    # Sauces
    "white sauce": {"cup": {"cal": 368, "fat": 27, "carbs": 23, "protein": 10, "sodium": 797, "fiber": 0.5, "sugar": 12}},
    "cream sauce": {"cup": {"cal": 368, "fat": 27, "carbs": 23, "protein": 10, "sodium": 797, "fiber": 0.5, "sugar": 12}},
    "cheese sauce": {"cup": {"cal": 470, "fat": 36, "carbs": 14, "protein": 24, "sodium": 1360, "fiber": 0.5, "sugar": 6}},
    "mushroom soup": {"cup": {"cal": 129, "fat": 9, "carbs": 9, "protein": 2.3, "sodium": 871, "fiber": 0.5, "sugar": 1.6}},

    # Breads & doughs
    "whole ciabatta": {"each": {"cal": 600, "fat": 4, "carbs": 120, "protein": 20, "sodium": 1200, "fiber": 4, "sugar": 4}},
    "pancake mix": {"cup": {"cal": 420, "fat": 4, "carbs": 84, "protein": 12, "sodium": 1400, "fiber": 3, "sugar": 12}},
    "macaroons": {"each": {"cal": 97, "fat": 4, "carbs": 14, "protein": 1, "sodium": 30, "fiber": 0.5, "sugar": 13}},

    # Flours
    "whole-wheat flour": {"cup": {"cal": 407, "fat": 2, "carbs": 87, "protein": 16, "sodium": 6, "fiber": 15, "sugar": 0}},
    "unsifted whole-wheat flour": {"cup": {"cal": 407, "fat": 2, "carbs": 87, "protein": 16, "sodium": 6, "fiber": 15, "sugar": 0}},

    # Dairy
    "sweet cream": {"cup": {"cal": 821, "fat": 88, "carbs": 7, "protein": 5, "sodium": 89, "fiber": 0, "sugar": 7}},
    "sweet milk": {"cup": {"cal": 149, "fat": 8, "carbs": 12, "protein": 8, "sodium": 105, "fiber": 0, "sugar": 12}},
    "sharp cheese": {"cup": {"cal": 455, "fat": 37, "carbs": 1.4, "protein": 28, "sodium": 701, "fiber": 0, "sugar": 0.5}},

    # Wine
    "dry red wine": {"cup": {"cal": 199, "fat": 0, "carbs": 6, "protein": 0, "sodium": 8, "fiber": 0, "sugar": 1}},
    "red wine": {"cup": {"cal": 199, "fat": 0, "carbs": 6, "protein": 0, "sodium": 8, "fiber": 0, "sugar": 1}},

    # Miscellaneous
    "basil leaves": {"cup": {"cal": 1, "fat": 0, "carbs": 0.1, "protein": 0.2, "sodium": 0, "fiber": 0.1, "sugar": 0}},
    "tortillas": {"each": {"cal": 150, "fat": 4, "carbs": 26, "protein": 4, "sodium": 340, "fiber": 2, "sugar": 1}},
    "unsweetened applesauce": {"cup": {"cal": 102, "fat": 0.2, "carbs": 28, "protein": 0.4, "sodium": 5, "fiber": 2.7, "sugar": 23}},
    "applesauce": {"cup": {"cal": 167, "fat": 0.4, "carbs": 43, "protein": 0.4, "sodium": 5, "fiber": 2.7, "sugar": 37}},
    "creamy peanut butter": {"tbsp": {"cal": 94, "fat": 8, "carbs": 3, "protein": 4, "sodium": 73, "fiber": 1, "sugar": 1.5}},
    "chunky peanut butter": {"tbsp": {"cal": 94, "fat": 8, "carbs": 3.5, "protein": 4, "sodium": 78, "fiber": 1, "sugar": 1}},
    "mustard powder": {"tsp": {"cal": 9, "fat": 0.6, "carbs": 0.6, "protein": 0.5, "sodium": 0, "fiber": 0.2, "sugar": 0}},
    "dry mustard": {"tsp": {"cal": 9, "fat": 0.6, "carbs": 0.6, "protein": 0.5, "sodium": 0, "fiber": 0.2, "sugar": 0}},
    "golden raisins": {"cup": {"cal": 434, "fat": 0.7, "carbs": 115, "protein": 5, "sodium": 17, "fiber": 5, "sugar": 86}},
    "apricot preserves": {"tbsp": {"cal": 50, "fat": 0, "carbs": 13, "protein": 0, "sodium": 8, "fiber": 0.2, "sugar": 11}},
    "apricot jam": {"tbsp": {"cal": 50, "fat": 0, "carbs": 13, "protein": 0, "sodium": 8, "fiber": 0.2, "sugar": 11}},
    "malted milk powder": {"tbsp": {"cal": 40, "fat": 0.5, "carbs": 7, "protein": 1.5, "sodium": 40, "fiber": 0, "sugar": 5}},
    "grated nutmeg": {"tsp": {"cal": 12, "fat": 0.8, "carbs": 1, "protein": 0.1, "sodium": 0, "fiber": 0.5, "sugar": 0.1}},
    "tomato catsup": {"tbsp": {"cal": 17, "fat": 0, "carbs": 4.5, "protein": 0.2, "sodium": 154, "fiber": 0, "sugar": 3.5}},
    "gelatine": {"envelope": {"cal": 23, "fat": 0, "carbs": 0, "protein": 6, "sodium": 14, "fiber": 0, "sugar": 0}},

    # =========================================================================
    # GAP ANALYSIS - ROUND 5 (remaining missing ingredients)
    # =========================================================================

    # Vegetables
    "avocados": {"each": {"cal": 322, "fat": 29, "carbs": 17, "protein": 4, "sodium": 14, "fiber": 13, "sugar": 1}},
    "avocado": {"each": {"cal": 322, "fat": 29, "carbs": 17, "protein": 4, "sodium": 14, "fiber": 13, "sugar": 1},
               "": {"cal": 322, "fat": 29, "carbs": 17, "protein": 4, "sodium": 14, "fiber": 13, "sugar": 1},
               "cup": {"cal": 234, "fat": 21, "carbs": 12, "protein": 3, "sodium": 10, "fiber": 10, "sugar": 1}},
    "broccoli florets": {"cup": {"cal": 31, "fat": 0.3, "carbs": 6, "protein": 2.5, "sodium": 30, "fiber": 2.4, "sugar": 1.5}},
    "broccoli": {"cup": {"cal": 31, "fat": 0.3, "carbs": 6, "protein": 2.5, "sodium": 30, "fiber": 2.4, "sugar": 1.5}},
    "cucumbers": {"each": {"cal": 45, "fat": 0.3, "carbs": 11, "protein": 2, "sodium": 6, "fiber": 1.5, "sugar": 5}},
    "cucumber": {"each": {"cal": 45, "fat": 0.3, "carbs": 11, "protein": 2, "sodium": 6, "fiber": 1.5, "sugar": 5}},
    "baby spinach": {"cup": {"cal": 7, "fat": 0.1, "carbs": 1.1, "protein": 0.9, "sodium": 24, "fiber": 0.7, "sugar": 0.1}},
    "spring onions": {"each": {"cal": 5, "fat": 0, "carbs": 1, "protein": 0.3, "sodium": 2, "fiber": 0.4, "sugar": 0.4}},
    "rocket": {"cup": {"cal": 5, "fat": 0.1, "carbs": 0.7, "protein": 0.5, "sodium": 5, "fiber": 0.3, "sugar": 0.4}},
    "arugula": {"cup": {"cal": 5, "fat": 0.1, "carbs": 0.7, "protein": 0.5, "sodium": 5, "fiber": 0.3, "sugar": 0.4}},
    "mashed potatoes": {"cup": {"cal": 237, "fat": 9, "carbs": 35, "protein": 4, "sodium": 699, "fiber": 3, "sugar": 3}},
    "new potatoes": {"lb": {"cal": 350, "fat": 0.4, "carbs": 80, "protein": 9, "sodium": 25, "fiber": 8, "sugar": 4}},
    "small potatoes": {"each": {"cal": 130, "fat": 0.1, "carbs": 30, "protein": 3.5, "sodium": 8, "fiber": 3, "sugar": 1}},

    # Beans & legumes
    "cannellini beans": {"cup": {"cal": 225, "fat": 0.9, "carbs": 40, "protein": 15, "sodium": 4, "fiber": 11, "sugar": 0.6}},
    "white beans": {"cup": {"cal": 225, "fat": 0.9, "carbs": 40, "protein": 15, "sodium": 4, "fiber": 11, "sugar": 0.6}},
    "great northern beans": {"cup": {"cal": 209, "fat": 0.8, "carbs": 37, "protein": 15, "sodium": 4, "fiber": 12, "sugar": 0.6}},
    "pork & beans": {"cup": {"cal": 268, "fat": 4, "carbs": 51, "protein": 13, "sodium": 1047, "fiber": 14, "sugar": 16}},
    "soybeans": {"cup": {"cal": 298, "fat": 15, "carbs": 17, "protein": 29, "sodium": 1, "fiber": 10, "sugar": 6}},
    "edamame": {"cup": {"cal": 188, "fat": 8, "carbs": 14, "protein": 18, "sodium": 9, "fiber": 8, "sugar": 3}},

    # Meats
    "flank steak": {"lb": {"cal": 720, "fat": 32, "carbs": 0, "protein": 104, "sodium": 280, "fiber": 0, "sugar": 0}},
    "round beef": {"lb": {"cal": 680, "fat": 28, "carbs": 0, "protein": 100, "sodium": 260, "fiber": 0, "sugar": 0}},
    "streaky bacon": {"slice": {"cal": 43, "fat": 3.3, "carbs": 0.1, "protein": 3, "sodium": 137, "fiber": 0, "sugar": 0}},
    "bacon strips": {"slice": {"cal": 43, "fat": 3.3, "carbs": 0.1, "protein": 3, "sodium": 137, "fiber": 0, "sugar": 0}},
    "slices bacon": {"slice": {"cal": 43, "fat": 3.3, "carbs": 0.1, "protein": 3, "sodium": 137, "fiber": 0, "sugar": 0}},
    "strips bacon": {"slice": {"cal": 43, "fat": 3.3, "carbs": 0.1, "protein": 3, "sodium": 137, "fiber": 0, "sugar": 0}},
    "chopped cooked ham": {"cup": {"cal": 203, "fat": 8, "carbs": 2, "protein": 30, "sodium": 1684, "fiber": 0, "sugar": 0}},
    "chicken breast halves": {"each": {"cal": 284, "fat": 6, "carbs": 0, "protein": 53, "sodium": 104, "fiber": 0, "sugar": 0}},

    # Grains & pasta
    "white rice": {"cup": {"cal": 205, "fat": 0.4, "carbs": 45, "protein": 4, "sodium": 2, "fiber": 0.6, "sugar": 0}},
    "macaroni": {"cup": {"cal": 221, "fat": 1.3, "carbs": 43, "protein": 8, "sodium": 1, "fiber": 2.5, "sugar": 1}},
    "elbow macaroni": {"cup": {"cal": 221, "fat": 1.3, "carbs": 43, "protein": 8, "sodium": 1, "fiber": 2.5, "sugar": 1}},
    "soft bread crumbs": {"cup": {"cal": 120, "fat": 2, "carbs": 22, "protein": 4, "sodium": 200, "fiber": 1, "sugar": 2}},
    "wheat bread": {"slice": {"cal": 81, "fat": 1, "carbs": 15, "protein": 4, "sodium": 146, "fiber": 2, "sugar": 1}},
    "slices wheat bread": {"slice": {"cal": 81, "fat": 1, "carbs": 15, "protein": 4, "sodium": 146, "fiber": 2, "sugar": 1}},
    "ciabatta": {"each": {"cal": 200, "fat": 1.3, "carbs": 40, "protein": 7, "sodium": 400, "fiber": 1.5, "sugar": 1}},
    "muesli": {"cup": {"cal": 289, "fat": 4, "carbs": 66, "protein": 8, "sodium": 14, "fiber": 6, "sugar": 26}},
    "cornflakes": {"cup": {"cal": 101, "fat": 0.2, "carbs": 24, "protein": 2, "sodium": 203, "fiber": 0.7, "sugar": 3}},

    # Cheese
    "longhorn cheese": {"cup": {"cal": 455, "fat": 37, "carbs": 1.4, "protein": 28, "sodium": 701, "fiber": 0, "sugar": 0.5}},
    "muenster cheese": {"oz": {"cal": 104, "fat": 8.5, "carbs": 0.3, "protein": 7, "sodium": 178, "fiber": 0, "sugar": 0.3}},
    "sieved cottage cheese": {"cup": {"cal": 163, "fat": 2.3, "carbs": 6, "protein": 28, "sodium": 918, "fiber": 0, "sugar": 5}},

    # Condiments & sauces
    "chunky salsa": {"cup": {"cal": 70, "fat": 0.4, "carbs": 14, "protein": 3, "sodium": 1200, "fiber": 4, "sugar": 8},
                    "can": {"cal": 140, "fat": 0.8, "carbs": 28, "protein": 6, "sodium": 2400, "fiber": 8, "sugar": 16},
                    "oz": {"cal": 9, "fat": 0.1, "carbs": 2, "protein": 0.4, "sodium": 150, "fiber": 0.5, "sugar": 1}},
    "salsa": {"cup": {"cal": 70, "fat": 0.4, "carbs": 14, "protein": 3, "sodium": 1200, "fiber": 4, "sugar": 8},
             "can": {"cal": 140, "fat": 0.8, "carbs": 28, "protein": 6, "sodium": 2400, "fiber": 8, "sugar": 16},
             "oz": {"cal": 9, "fat": 0.1, "carbs": 2, "protein": 0.4, "sodium": 150, "fiber": 0.5, "sugar": 1}},
    "seasoning salt": {"tsp": {"cal": 0, "fat": 0, "carbs": 0, "protein": 0, "sodium": 1600, "fiber": 0, "sugar": 0}},
    "low-sodium soy sauce": {"tbsp": {"cal": 10, "fat": 0, "carbs": 1, "protein": 1, "sodium": 533, "fiber": 0, "sugar": 0}},
    "bottled minced garlic": {"tsp": {"cal": 5, "fat": 0, "carbs": 1, "protein": 0.2, "sodium": 0, "fiber": 0, "sugar": 0}},

    # Spices
    "whole allspice": {"tsp": {"cal": 5, "fat": 0.2, "carbs": 1.4, "protein": 0.1, "sodium": 1, "fiber": 0.4, "sugar": 0}},
    "pumpkin pie spice": {"tsp": {"cal": 6, "fat": 0.2, "carbs": 1.2, "protein": 0.1, "sodium": 1, "fiber": 0.4, "sugar": 0}},
    "greek seasoning": {"tsp": {"cal": 5, "fat": 0.2, "carbs": 1, "protein": 0.2, "sodium": 5, "fiber": 0.3, "sugar": 0}},
    "sage leaves": {"each": {"cal": 1, "fat": 0, "carbs": 0.1, "protein": 0, "sodium": 0, "fiber": 0, "sugar": 0}},

    # Alcohol
    "gin": {"oz": {"cal": 73, "fat": 0, "carbs": 0, "protein": 0, "sodium": 0, "fiber": 0, "sugar": 0}},
    "vodka": {"oz": {"cal": 64, "fat": 0, "carbs": 0, "protein": 0, "sodium": 0, "fiber": 0, "sugar": 0}},
    "tequila": {"oz": {"cal": 64, "fat": 0, "carbs": 0, "protein": 0, "sodium": 0, "fiber": 0, "sugar": 0}},
    "whiskey": {"oz": {"cal": 70, "fat": 0, "carbs": 0, "protein": 0, "sodium": 0, "fiber": 0, "sugar": 0}},
    "bourbon": {"oz": {"cal": 70, "fat": 0, "carbs": 0, "protein": 0, "sodium": 0, "fiber": 0, "sugar": 0}},
    "scotch": {"oz": {"cal": 70, "fat": 0, "carbs": 0, "protein": 0, "sodium": 0, "fiber": 0, "sugar": 0}},
    "cognac": {"oz": {"cal": 69, "fat": 0, "carbs": 1, "protein": 0, "sodium": 0, "fiber": 0, "sugar": 0}},
    "brandy": {"oz": {"cal": 69, "fat": 0, "carbs": 1, "protein": 0, "sodium": 0, "fiber": 0, "sugar": 0}},
    "triple sec": {"oz": {"cal": 103, "fat": 0, "carbs": 11, "protein": 0, "sodium": 2, "fiber": 0, "sugar": 11}},
    "kahlua": {"oz": {"cal": 91, "fat": 0, "carbs": 14, "protein": 0, "sodium": 3, "fiber": 0, "sugar": 14}},
    "amaretto": {"oz": {"cal": 110, "fat": 0, "carbs": 17, "protein": 0, "sodium": 3, "fiber": 0, "sugar": 17}},
    "grand marnier": {"oz": {"cal": 76, "fat": 0, "carbs": 7, "protein": 0, "sodium": 0, "fiber": 0, "sugar": 7}},

    # Gelatin flavors
    "lemon-flavored gelatin": {"package": {"cal": 80, "fat": 0, "carbs": 19, "protein": 2, "sodium": 120, "fiber": 0, "sugar": 19}},
    "strawberry gelatin": {"package": {"cal": 80, "fat": 0, "carbs": 19, "protein": 2, "sodium": 120, "fiber": 0, "sugar": 19}},
    "lime gelatin": {"package": {"cal": 80, "fat": 0, "carbs": 19, "protein": 2, "sodium": 120, "fiber": 0, "sugar": 19}},
    "orange gelatin": {"package": {"cal": 80, "fat": 0, "carbs": 19, "protein": 2, "sodium": 120, "fiber": 0, "sugar": 19}},
    "cherry gelatin": {"package": {"cal": 80, "fat": 0, "carbs": 19, "protein": 2, "sodium": 120, "fiber": 0, "sugar": 19}},

    # Fruits
    "grapefruits": {"each": {"cal": 103, "fat": 0.3, "carbs": 26, "protein": 2, "sodium": 0, "fiber": 4, "sugar": 17}},
    "grapefruit": {"each": {"cal": 103, "fat": 0.3, "carbs": 26, "protein": 2, "sodium": 0, "fiber": 4, "sugar": 17}},
    "large apple": {"each": {"cal": 116, "fat": 0.4, "carbs": 31, "protein": 0.6, "sodium": 2, "fiber": 5.4, "sugar": 23}},
    "large bananas": {"each": {"cal": 121, "fat": 0.4, "carbs": 31, "protein": 1.5, "sodium": 1, "fiber": 3.5, "sugar": 17}},
    "large mangos": {"each": {"cal": 202, "fat": 1.3, "carbs": 50, "protein": 2.8, "sodium": 3, "fiber": 5.4, "sugar": 45}},
    "mixed berries": {"cup": {"cal": 70, "fat": 0.5, "carbs": 17, "protein": 1, "sodium": 1, "fiber": 4, "sugar": 10}},

    # Yogurt flavors
    "plain nonfat yoghurt": {"cup": {"cal": 137, "fat": 0.4, "carbs": 19, "protein": 14, "sodium": 189, "fiber": 0, "sugar": 19}},
    "banana-flavored yogurt": {"cup": {"cal": 193, "fat": 2.8, "carbs": 36, "protein": 11, "sodium": 148, "fiber": 0, "sugar": 33}},
    "mango flavored yogurt": {"cup": {"cal": 193, "fat": 2.8, "carbs": 36, "protein": 11, "sodium": 148, "fiber": 0, "sugar": 33}},

    # Chiles & peppers
    "whole green chiles": {"can": {"cal": 30, "fat": 0, "carbs": 6, "protein": 1, "sodium": 680, "fiber": 2, "sugar": 3}},
    "green chiles": {"can": {"cal": 30, "fat": 0, "carbs": 6, "protein": 1, "sodium": 680, "fiber": 2, "sugar": 3}},
    "diced green chiles": {"can": {"cal": 30, "fat": 0, "carbs": 6, "protein": 1, "sodium": 680, "fiber": 2, "sugar": 3}},

    # Seeds
    "linseeds": {"tbsp": {"cal": 55, "fat": 4.3, "carbs": 3, "protein": 2, "sodium": 3, "fiber": 2.8, "sugar": 0.2}},
    "flaxseeds": {"tbsp": {"cal": 55, "fat": 4.3, "carbs": 3, "protein": 2, "sodium": 3, "fiber": 2.8, "sugar": 0.2}},
    "flax seeds": {"tbsp": {"cal": 55, "fat": 4.3, "carbs": 3, "protein": 2, "sodium": 3, "fiber": 2.8, "sugar": 0.2}},

    # Historical/vintage ingredients (for old cookbooks)
    "pearl ash": {"tsp": {"cal": 0, "fat": 0, "carbs": 0, "protein": 0, "sodium": 0, "fiber": 0, "sugar": 0}},
    "saleratus": {"tsp": {"cal": 0, "fat": 0, "carbs": 0, "protein": 0, "sodium": 629, "fiber": 0, "sugar": 0}},
    "emptins": {"cup": {"cal": 30, "fat": 1, "carbs": 4, "protein": 2, "sodium": 10, "fiber": 1, "sugar": 0}},

    # Misc
    "thick cream": {"cup": {"cal": 821, "fat": 88, "carbs": 7, "protein": 5, "sodium": 89, "fiber": 0, "sugar": 7}},
    "truffles": {"oz": {"cal": 84, "fat": 9, "carbs": 2, "protein": 1, "sodium": 15, "fiber": 0, "sugar": 0}},
    "minced parsley": {"tbsp": {"cal": 1, "fat": 0, "carbs": 0.2, "protein": 0.1, "sodium": 2, "fiber": 0.1, "sugar": 0}},

    # =========================================================================
    # GAP ANALYSIS - ROUND 6 (final pass)
    # =========================================================================

    # Meats & sausages
    "pork sausage": {"lb": {"cal": 1360, "fat": 112, "carbs": 0, "protein": 64, "sodium": 1400, "fiber": 0, "sugar": 0}},
    "pork sausage links": {"each": {"cal": 80, "fat": 7, "carbs": 0, "protein": 4, "sodium": 200, "fiber": 0, "sugar": 0}},
    "stewing beef": {"lb": {"cal": 800, "fat": 48, "carbs": 0, "protein": 88, "sodium": 280, "fiber": 0, "sugar": 0}},

    # Chocolate & chips
    "milk chocolate": {"oz": {"cal": 153, "fat": 8, "carbs": 17, "protein": 2, "sodium": 23, "fiber": 0.8, "sugar": 15}},
    "milk chocolate chips": {"cup": {"cal": 840, "fat": 48, "carbs": 92, "protein": 10, "sodium": 128, "fiber": 4, "sugar": 84}},
    "peanut butter chips": {"cup": {"cal": 800, "fat": 48, "carbs": 80, "protein": 16, "sodium": 320, "fiber": 2, "sugar": 72}},
    "butterscotch chips": {"cup": {"cal": 800, "fat": 40, "carbs": 100, "protein": 2, "sodium": 300, "fiber": 0, "sugar": 92}},
    "squares unsweetened chocolate": {"each": {"cal": 145, "fat": 15, "carbs": 8, "protein": 3, "sodium": 4, "fiber": 5, "sugar": 0}},

    # Nuts
    "black walnuts": {"cup": {"cal": 760, "fat": 71, "carbs": 12, "protein": 30, "sodium": 2, "fiber": 6, "sugar": 1}},
    "chopped walnuts": {"cup": {"cal": 785, "fat": 79, "carbs": 16, "protein": 18, "sodium": 1, "fiber": 8, "sugar": 3}},
    "broken pecans": {"cup": {"cal": 753, "fat": 78, "carbs": 15, "protein": 10, "sodium": 0, "fiber": 10, "sugar": 4}},
    "cut-up nuts": {"cup": {"cal": 785, "fat": 79, "carbs": 16, "protein": 18, "sodium": 1, "fiber": 8, "sugar": 3}},

    # Dried fruits
    "cut-up raisins": {"cup": {"cal": 434, "fat": 0.5, "carbs": 115, "protein": 5, "sodium": 18, "fiber": 6, "sugar": 86}},
    "cut-up dates": {"cup": {"cal": 415, "fat": 0.6, "carbs": 110, "protein": 4, "sodium": 3, "fiber": 12, "sugar": 93}},
    "eeded raisins": {"cup": {"cal": 434, "fat": 0.5, "carbs": 115, "protein": 5, "sodium": 18, "fiber": 6, "sugar": 86}},

    # Coconut variants
    "sweetened shredded coconut": {"cup": {"cal": 466, "fat": 33, "carbs": 44, "protein": 3, "sodium": 244, "fiber": 4, "sugar": 40}},
    "cocoanut": {"cup": {"cal": 283, "fat": 27, "carbs": 12, "protein": 3, "sodium": 16, "fiber": 7, "sugar": 5}},

    # Spreads & condiments
    "apple butter": {"tbsp": {"cal": 29, "fat": 0.1, "carbs": 7, "protein": 0.1, "sodium": 1, "fiber": 0.3, "sugar": 6}},
    "spicy salsa": {"cup": {"cal": 70, "fat": 0.4, "carbs": 14, "protein": 3, "sodium": 1400, "fiber": 4, "sugar": 8}},

    # Seeds & spices
    "mustard seed": {"tsp": {"cal": 15, "fat": 1, "carbs": 1, "protein": 0.8, "sodium": 0, "fiber": 0.4, "sugar": 0}},
    "caraway seeds": {"tsp": {"cal": 7, "fat": 0.3, "carbs": 1, "protein": 0.4, "sodium": 0, "fiber": 0.8, "sugar": 0}},
    "caraway seed": {"tsp": {"cal": 7, "fat": 0.3, "carbs": 1, "protein": 0.4, "sodium": 0, "fiber": 0.8, "sugar": 0}},
    "coriander seed": {"tsp": {"cal": 5, "fat": 0.3, "carbs": 1, "protein": 0.2, "sodium": 1, "fiber": 0.8, "sugar": 0}},
    "spice": {"tsp": {"cal": 6, "fat": 0.2, "carbs": 1, "protein": 0.1, "sodium": 1, "fiber": 0.5, "sugar": 0}},
    "mild chili powder": {"tsp": {"cal": 8, "fat": 0.4, "carbs": 1.4, "protein": 0.3, "sodium": 26, "fiber": 0.9, "sugar": 0.2}},

    # Dairy
    "eggnog": {"cup": {"cal": 343, "fat": 19, "carbs": 34, "protein": 10, "sodium": 137, "fiber": 0, "sugar": 34}},
    "coconut custard": {"cup": {"cal": 280, "fat": 14, "carbs": 32, "protein": 8, "sodium": 180, "fiber": 1, "sugar": 28}},
    "milk or cream": {"cup": {"cal": 150, "fat": 8, "carbs": 12, "protein": 8, "sodium": 105, "fiber": 0, "sugar": 12}},
    "lukewarm milk": {"cup": {"cal": 149, "fat": 8, "carbs": 12, "protein": 8, "sodium": 105, "fiber": 0, "sugar": 12}},

    # Flour variants
    "buckwheat flour": {"cup": {"cal": 402, "fat": 4, "carbs": 85, "protein": 15, "sodium": 13, "fiber": 12, "sugar": 3}},

    # Apples
    "tart apples": {"each": {"cal": 80, "fat": 0.3, "carbs": 21, "protein": 0.4, "sodium": 1, "fiber": 4, "sugar": 15}},
    "tart cooking apples": {"each": {"cal": 80, "fat": 0.3, "carbs": 21, "protein": 0.4, "sodium": 1, "fiber": 4, "sugar": 15}},

    # Yeast variants
    "yeast cake": {"each": {"cal": 10, "fat": 0.1, "carbs": 1.5, "protein": 1.3, "sodium": 4, "fiber": 0.8, "sugar": 0}},
    "cake yeast": {"each": {"cal": 10, "fat": 0.1, "carbs": 1.5, "protein": 1.3, "sodium": 4, "fiber": 0.8, "sugar": 0}},
    "granulated yeast": {"tsp": {"cal": 8, "fat": 0.1, "carbs": 1, "protein": 1, "sodium": 2, "fiber": 0.5, "sugar": 0}},

    # Canned goods
    "can tomato soup": {"can": {"cal": 161, "fat": 2.4, "carbs": 33, "protein": 4, "sodium": 1710, "fiber": 1.6, "sugar": 20}},
    "strained tomato": {"cup": {"cal": 41, "fat": 0.3, "carbs": 9, "protein": 2, "sodium": 800, "fiber": 2, "sugar": 7}},

    # Cereals
    "kellogg's rice krispies cereal": {"cup": {"cal": 96, "fat": 0.3, "carbs": 23, "protein": 2, "sodium": 190, "fiber": 0.3, "sugar": 3}},
    "rice krispies": {"cup": {"cal": 96, "fat": 0.3, "carbs": 23, "protein": 2, "sodium": 190, "fiber": 0.3, "sugar": 3}},

    # Vegetables
    "shelled peas": {"cup": {"cal": 117, "fat": 0.6, "carbs": 21, "protein": 8, "sodium": 7, "fiber": 7, "sugar": 8}},
    "one carrot": {"each": {"cal": 25, "fat": 0.1, "carbs": 6, "protein": 0.6, "sodium": 42, "fiber": 1.7, "sugar": 3}},

    # Misc prepared
    "stove top stuffing": {"cup": {"cal": 177, "fat": 9, "carbs": 21, "protein": 4, "sodium": 522, "fiber": 1, "sugar": 3}},
    "fine sugar": {"cup": {"cal": 774, "fat": 0, "carbs": 200, "protein": 0, "sodium": 2, "fiber": 0, "sugar": 200}},

    # =========================================================================
    # GAP ANALYSIS - ROUND 7 (final cleanup)
    # =========================================================================

    # Herbs & leaves
    "mint leaves": {"tbsp": {"cal": 1, "fat": 0, "carbs": 0.1, "protein": 0.1, "sodium": 1, "fiber": 0, "sugar": 0}},
    "oregano leaves": {"tsp": {"cal": 3, "fat": 0.1, "carbs": 0.7, "protein": 0.1, "sodium": 0, "fiber": 0.4, "sugar": 0}},
    "thyme sprigs": {"each": {"cal": 1, "fat": 0, "carbs": 0.1, "protein": 0, "sodium": 0, "fiber": 0, "sugar": 0}},
    "fresh oregano": {"tbsp": {"cal": 3, "fat": 0.1, "carbs": 0.5, "protein": 0.1, "sodium": 0, "fiber": 0.3, "sugar": 0}},

    # Spices & seasonings
    "ground red pepper": {"tsp": {"cal": 6, "fat": 0.3, "carbs": 1, "protein": 0.2, "sodium": 1, "fiber": 0.5, "sugar": 0.2}},
    "garam masala": {"tsp": {"cal": 7, "fat": 0.3, "carbs": 1.3, "protein": 0.2, "sodium": 2, "fiber": 0.5, "sugar": 0.1}},
    "turmeric powder": {"tsp": {"cal": 8, "fat": 0.2, "carbs": 1.4, "protein": 0.3, "sodium": 1, "fiber": 0.5, "sugar": 0.1}},
    "turmeric": {"tsp": {"cal": 8, "fat": 0.2, "carbs": 1.4, "protein": 0.3, "sodium": 1, "fiber": 0.5, "sugar": 0.1}},
    "powdered thyme": {"tsp": {"cal": 4, "fat": 0.1, "carbs": 0.9, "protein": 0.1, "sodium": 1, "fiber": 0.5, "sugar": 0}},
    "black peppercorns": {"tsp": {"cal": 6, "fat": 0.1, "carbs": 1.4, "protein": 0.2, "sodium": 0, "fiber": 0.6, "sugar": 0}},
    "peppercorns": {"tsp": {"cal": 6, "fat": 0.1, "carbs": 1.4, "protein": 0.2, "sodium": 0, "fiber": 0.6, "sugar": 0}},
    "alum": {"tsp": {"cal": 0, "fat": 0, "carbs": 0, "protein": 0, "sodium": 2, "fiber": 0, "sugar": 0}},

    # Nuts & seeds
    "pecan meats": {"cup": {"cal": 753, "fat": 78, "carbs": 15, "protein": 10, "sodium": 0, "fiber": 10, "sugar": 4}},
    "cashew nuts": {"cup": {"cal": 786, "fat": 63, "carbs": 45, "protein": 21, "sodium": 16, "fiber": 4, "sugar": 6}},
    "cashews": {"cup": {"cal": 786, "fat": 63, "carbs": 45, "protein": 21, "sodium": 16, "fiber": 4, "sugar": 6}},

    # Peppers
    "serrano chile": {"each": {"cal": 2, "fat": 0, "carbs": 0.4, "protein": 0.1, "sodium": 1, "fiber": 0.2, "sugar": 0.2}},
    "poblano pepper": {"each": {"cal": 48, "fat": 0.5, "carbs": 9, "protein": 2, "sodium": 6, "fiber": 4, "sugar": 5}},
    "poblano": {"each": {"cal": 48, "fat": 0.5, "carbs": 9, "protein": 2, "sodium": 6, "fiber": 4, "sugar": 5}},

    # Vegetables
    "yellow squash": {"cup": {"cal": 18, "fat": 0.2, "carbs": 4, "protein": 1, "sodium": 2, "fiber": 1, "sugar": 2}},
    "sliced cucumber": {"cup": {"cal": 14, "fat": 0.1, "carbs": 3, "protein": 0.6, "sodium": 2, "fiber": 0.5, "sugar": 1.5}},
    "corn kernels": {"cup": {"cal": 132, "fat": 1.8, "carbs": 29, "protein": 5, "sodium": 23, "fiber": 4, "sugar": 5}},
    "one leek": {"each": {"cal": 54, "fat": 0.3, "carbs": 13, "protein": 1.3, "sodium": 18, "fiber": 1.6, "sugar": 3.5}},
    "celery stalk": {"each": {"cal": 6, "fat": 0.1, "carbs": 1, "protein": 0.3, "sodium": 32, "fiber": 0.6, "sugar": 0.6}},
    "stalks celery": {"each": {"cal": 6, "fat": 0.1, "carbs": 1, "protein": 0.3, "sodium": 32, "fiber": 0.6, "sugar": 0.6}},
    "capers": {"tbsp": {"cal": 2, "fat": 0, "carbs": 0.4, "protein": 0.2, "sodium": 255, "fiber": 0.3, "sugar": 0}},
    "guacamole": {"cup": {"cal": 368, "fat": 32, "carbs": 20, "protein": 4, "sodium": 700, "fiber": 14, "sugar": 2}},

    # Beans
    "red kidney beans": {"cup": {"cal": 225, "fat": 0.9, "carbs": 40, "protein": 15, "sodium": 2, "fiber": 11, "sugar": 0.6}},
    "chili beans": {"cup": {"cal": 286, "fat": 2.6, "carbs": 52, "protein": 17, "sodium": 920, "fiber": 18, "sugar": 6}},

    # Cheese
    "asiago cheese": {"oz": {"cal": 111, "fat": 9, "carbs": 1, "protein": 7, "sodium": 340, "fiber": 0, "sugar": 0.5}},
    "parmigiano-reggiano cheese": {"oz": {"cal": 111, "fat": 7, "carbs": 1, "protein": 10, "sodium": 330, "fiber": 0, "sugar": 0}},
    "mozzarella": {"cup": {"cal": 318, "fat": 22, "carbs": 3, "protein": 26, "sodium": 627, "fiber": 0, "sugar": 1}},
    "cheese slices": {"slice": {"cal": 104, "fat": 9, "carbs": 0.5, "protein": 5, "sodium": 406, "fiber": 0, "sugar": 0.3}},

    # Dairy
    "crème fraîche": {"cup": {"cal": 440, "fat": 46, "carbs": 3, "protein": 4, "sodium": 40, "fiber": 0, "sugar": 3}},
    "creme fraiche": {"cup": {"cal": 440, "fat": 46, "carbs": 3, "protein": 4, "sodium": 40, "fiber": 0, "sugar": 3}},
    "full cream milk": {"cup": {"cal": 149, "fat": 8, "carbs": 12, "protein": 8, "sodium": 105, "fiber": 0, "sugar": 12}},
    "ice cubes": {"cup": {"cal": 0, "fat": 0, "carbs": 0, "protein": 0, "sodium": 0, "fiber": 0, "sugar": 0}},

    # Meats
    "ground turkey breast": {"lb": {"cal": 544, "fat": 8, "carbs": 0, "protein": 112, "sodium": 320, "fiber": 0, "sugar": 0}},
    "lean beef": {"lb": {"cal": 680, "fat": 28, "carbs": 0, "protein": 100, "sodium": 260, "fiber": 0, "sugar": 0}},
    "ham fat": {"oz": {"cal": 170, "fat": 18, "carbs": 0, "protein": 1.5, "sodium": 320, "fiber": 0, "sugar": 0}},

    # Juices & beverages
    "grapefruit juice": {"cup": {"cal": 96, "fat": 0.3, "carbs": 23, "protein": 1.2, "sodium": 2, "fiber": 0.2, "sugar": 20}},
    "strong hot coffee": {"cup": {"cal": 2, "fat": 0, "carbs": 0, "protein": 0.3, "sodium": 5, "fiber": 0, "sugar": 0}},
    "apricot nectar": {"cup": {"cal": 140, "fat": 0.2, "carbs": 36, "protein": 0.9, "sodium": 8, "fiber": 1.5, "sugar": 33}},
    "apple juice or cider": {"cup": {"cal": 114, "fat": 0.3, "carbs": 28, "protein": 0.2, "sodium": 10, "fiber": 0.2, "sugar": 24}},

    # Breads
    "baguette": {"each": {"cal": 680, "fat": 2, "carbs": 140, "protein": 24, "sodium": 1400, "fiber": 6, "sugar": 2}},

    # Oils
    "peanut oil": {"tbsp": {"cal": 119, "fat": 14, "carbs": 0, "protein": 0, "sodium": 0, "fiber": 0, "sugar": 0}},

    # Condiments & canned
    "jellied cranberry sauce": {"cup": {"cal": 418, "fat": 0.4, "carbs": 108, "protein": 0.5, "sodium": 80, "fiber": 3, "sugar": 87}},
    "cranberry sauce": {"cup": {"cal": 418, "fat": 0.4, "carbs": 108, "protein": 0.5, "sodium": 80, "fiber": 3, "sugar": 87},
                       "can": {"cal": 418, "fat": 0.4, "carbs": 108, "protein": 0.5, "sodium": 80, "fiber": 3, "sugar": 87}},
    "tzatziki": {"cup": {"cal": 150, "fat": 10, "carbs": 10, "protein": 6, "sodium": 400, "fiber": 0.5, "sugar": 6}},
    "tzatziki sauce": {"cup": {"cal": 150, "fat": 10, "carbs": 10, "protein": 6, "sodium": 400, "fiber": 0.5, "sugar": 6}},
    "onion soup": {"can": {"cal": 140, "fat": 4, "carbs": 18, "protein": 5, "sodium": 2440, "fiber": 2, "sugar": 5}},
    "condensed french onion soup": {"can": {"cal": 140, "fat": 4, "carbs": 18, "protein": 5, "sodium": 2440, "fiber": 2, "sugar": 5}},
    "mushrooms canned": {"cup": {"cal": 33, "fat": 0.3, "carbs": 6, "protein": 2.5, "sodium": 561, "fiber": 2, "sugar": 2}},

    # Sweeteners
    "swerve sweetener": {"cup": {"cal": 0, "fat": 0, "carbs": 96, "protein": 0, "sodium": 0, "fiber": 0, "sugar": 0}},

    # Misc
    "large banana": {"each": {"cal": 121, "fat": 0.4, "carbs": 31, "protein": 1.5, "sodium": 1, "fiber": 3.5, "sugar": 17}},
    "frozen strawberries": {"cup": {"cal": 77, "fat": 0.2, "carbs": 20, "protein": 1, "sodium": 3, "fiber": 3.3, "sugar": 13}},

    # =========================================================================
    # BATCH 13: Additional missing ingredients
    # =========================================================================

    # Dips & spreads
    "hummus": {"cup": {"cal": 435, "fat": 21, "carbs": 50, "protein": 20, "sodium": 960, "fiber": 15, "sugar": 0},
              "oz": {"cal": 54, "fat": 2.6, "carbs": 6, "protein": 2.5, "sodium": 120, "fiber": 2, "sugar": 0},
              "tbsp": {"cal": 27, "fat": 1.3, "carbs": 3, "protein": 1.3, "sodium": 60, "fiber": 1, "sugar": 0}},
    "pita chips": {"cup": {"cal": 260, "fat": 10, "carbs": 36, "protein": 6, "sodium": 380, "fiber": 2, "sugar": 1},
                  "bag": {"cal": 780, "fat": 30, "carbs": 108, "protein": 18, "sodium": 1140, "fiber": 6, "sugar": 3},
                  "oz": {"cal": 130, "fat": 5, "carbs": 18, "protein": 3, "sodium": 190, "fiber": 1, "sugar": 0.5}},
    "tzatziki": {"cup": {"cal": 150, "fat": 10, "carbs": 10, "protein": 6, "sodium": 400, "fiber": 0.5, "sugar": 6}},

    # Meats
    "ground veal": {"lb": {"cal": 840, "fat": 40, "carbs": 0, "protein": 112, "sodium": 320, "fiber": 0, "sugar": 0},
                   "oz": {"cal": 53, "fat": 2.5, "carbs": 0, "protein": 7, "sodium": 20, "fiber": 0, "sugar": 0}},
    "veal": {"lb": {"cal": 840, "fat": 40, "carbs": 0, "protein": 112, "sodium": 320, "fiber": 0, "sugar": 0},
             "oz": {"cal": 53, "fat": 2.5, "carbs": 0, "protein": 7, "sodium": 20, "fiber": 0, "sugar": 0}},
    "skirt steak": {"lb": {"cal": 800, "fat": 48, "carbs": 0, "protein": 92, "sodium": 280, "fiber": 0, "sugar": 0},
                   "oz": {"cal": 50, "fat": 3, "carbs": 0, "protein": 5.8, "sodium": 18, "fiber": 0, "sugar": 0}},
    "beef heart": {"lb": {"cal": 560, "fat": 16, "carbs": 0, "protein": 96, "sodium": 400, "fiber": 0, "sugar": 0},
                  "oz": {"cal": 35, "fat": 1, "carbs": 0, "protein": 6, "sodium": 25, "fiber": 0, "sugar": 0}},
    "tripe": {"lb": {"cal": 400, "fat": 16, "carbs": 0, "protein": 60, "sodium": 180, "fiber": 0, "sugar": 0}},
    "honeycomb tripe": {"lb": {"cal": 400, "fat": 16, "carbs": 0, "protein": 60, "sodium": 180, "fiber": 0, "sugar": 0}},
    "veal knuckle": {"each": {"cal": 350, "fat": 12, "carbs": 0, "protein": 56, "sodium": 200, "fiber": 0, "sugar": 0}},

    # Cheese varieties
    "roquefort cheese": {"oz": {"cal": 105, "fat": 9, "carbs": 0.6, "protein": 6, "sodium": 513, "fiber": 0, "sugar": 0},
                        "cup": {"cal": 420, "fat": 36, "carbs": 2.4, "protein": 24, "sodium": 2052, "fiber": 0, "sugar": 0}},
    "cotija cheese": {"oz": {"cal": 106, "fat": 8, "carbs": 2, "protein": 7, "sodium": 350, "fiber": 0, "sugar": 0},
                     "cup": {"cal": 424, "fat": 32, "carbs": 8, "protein": 28, "sodium": 1400, "fiber": 0, "sugar": 0}},
    "queso cheese": {"cup": {"cal": 480, "fat": 36, "carbs": 8, "protein": 28, "sodium": 1200, "fiber": 0, "sugar": 2},
                    "oz": {"cal": 60, "fat": 4.5, "carbs": 1, "protein": 3.5, "sodium": 150, "fiber": 0, "sugar": 0.3}},
    "queso fresco": {"oz": {"cal": 80, "fat": 6, "carbs": 1, "protein": 5, "sodium": 180, "fiber": 0, "sugar": 0}},
    "daiya cheese": {"cup": {"cal": 240, "fat": 16, "carbs": 16, "protein": 0, "sodium": 640, "fiber": 0, "sugar": 0},
                    "oz": {"cal": 60, "fat": 4, "carbs": 4, "protein": 0, "sodium": 160, "fiber": 0, "sugar": 0}},
    "muenster cheese": {"slice": {"cal": 104, "fat": 8.5, "carbs": 0.3, "protein": 6.6, "sodium": 178, "fiber": 0, "sugar": 0.1},
                       "oz": {"cal": 104, "fat": 8.5, "carbs": 0.3, "protein": 6.6, "sodium": 178, "fiber": 0, "sugar": 0.1}},
    "gouda cheese": {"slice": {"cal": 101, "fat": 8, "carbs": 0.6, "protein": 7, "sodium": 232, "fiber": 0, "sugar": 0.6},
                    "oz": {"cal": 101, "fat": 8, "carbs": 0.6, "protein": 7, "sodium": 232, "fiber": 0, "sugar": 0.6}},

    # Spices & seasonings
    "saffron": {"tsp": {"cal": 2, "fat": 0, "carbs": 0.5, "protein": 0.1, "sodium": 1, "fiber": 0, "sugar": 0},
               "threads": {"cal": 2, "fat": 0, "carbs": 0.5, "protein": 0.1, "sodium": 1, "fiber": 0, "sugar": 0}},
    "saffron threads": {"tsp": {"cal": 2, "fat": 0, "carbs": 0.5, "protein": 0.1, "sodium": 1, "fiber": 0, "sugar": 0}},
    "garam masala": {"tsp": {"cal": 6, "fat": 0.3, "carbs": 1, "protein": 0.2, "sodium": 1, "fiber": 0.4, "sugar": 0},
                    "tbsp": {"cal": 18, "fat": 0.9, "carbs": 3, "protein": 0.6, "sodium": 3, "fiber": 1.2, "sugar": 0}},
    "cardamom": {"tsp": {"cal": 6, "fat": 0.1, "carbs": 1.4, "protein": 0.2, "sodium": 0, "fiber": 0.6, "sugar": 0}},
    "green cardamom": {"pod": {"cal": 6, "fat": 0.1, "carbs": 1.4, "protein": 0.2, "sodium": 0, "fiber": 0.6, "sugar": 0}},
    "black cardamom": {"pod": {"cal": 6, "fat": 0.2, "carbs": 1.2, "protein": 0.2, "sodium": 0, "fiber": 0.6, "sugar": 0}},
    "peppercorns": {"tsp": {"cal": 6, "fat": 0.1, "carbs": 1.5, "protein": 0.2, "sodium": 0, "fiber": 0.6, "sugar": 0}},
    "lavender": {"tsp": {"cal": 2, "fat": 0, "carbs": 0.5, "protein": 0.1, "sodium": 0, "fiber": 0.2, "sugar": 0}},
    "dried lavender": {"tsp": {"cal": 2, "fat": 0, "carbs": 0.5, "protein": 0.1, "sodium": 0, "fiber": 0.2, "sugar": 0}},

    # Sauces
    "green chile sauce": {"cup": {"cal": 60, "fat": 1, "carbs": 11, "protein": 2, "sodium": 1200, "fiber": 2, "sugar": 4},
                         "can": {"cal": 90, "fat": 1.5, "carbs": 16, "protein": 3, "sodium": 1800, "fiber": 3, "sugar": 6},
                         "oz": {"cal": 8, "fat": 0.1, "carbs": 1.4, "protein": 0.3, "sodium": 150, "fiber": 0.3, "sugar": 0.5}},
    "picante sauce": {"cup": {"cal": 70, "fat": 0.3, "carbs": 16, "protein": 3, "sodium": 2400, "fiber": 4, "sugar": 8},
                     "jar": {"cal": 140, "fat": 0.6, "carbs": 32, "protein": 6, "sodium": 4800, "fiber": 8, "sugar": 16}},
    "russian dressing": {"tbsp": {"cal": 57, "fat": 5, "carbs": 3, "protein": 0.2, "sodium": 133, "fiber": 0, "sugar": 2},
                        "bottle": {"cal": 912, "fat": 80, "carbs": 48, "protein": 3, "sodium": 2128, "fiber": 0, "sugar": 32}},
    "creamy french dressing": {"tbsp": {"cal": 70, "fat": 6, "carbs": 4, "protein": 0, "sodium": 140, "fiber": 0, "sugar": 3},
                              "bottle": {"cal": 1120, "fat": 96, "carbs": 64, "protein": 0, "sodium": 2240, "fiber": 0, "sugar": 48}},
    "stove top stuffing": {"pkg": {"cal": 440, "fat": 8, "carbs": 84, "protein": 12, "sodium": 1800, "fiber": 4, "sugar": 6}},

    # Preserves & sweets
    "jam": {"tbsp": {"cal": 56, "fat": 0, "carbs": 14, "protein": 0, "sodium": 6, "fiber": 0.2, "sugar": 10}},
    "preserves": {"tbsp": {"cal": 56, "fat": 0, "carbs": 14, "protein": 0, "sodium": 6, "fiber": 0.2, "sugar": 10},
                 "jar": {"cal": 1008, "fat": 0, "carbs": 252, "protein": 0, "sodium": 108, "fiber": 3.6, "sugar": 180}},
    "apricot preserves": {"tbsp": {"cal": 50, "fat": 0, "carbs": 13, "protein": 0, "sodium": 8, "fiber": 0.2, "sugar": 11},
                         "jar": {"cal": 800, "fat": 0, "carbs": 208, "protein": 0, "sodium": 128, "fiber": 3.2, "sugar": 176}},
    "preserved ginger": {"tbsp": {"cal": 20, "fat": 0, "carbs": 5, "protein": 0, "sodium": 1, "fiber": 0, "sugar": 4}},
    "crystallized ginger": {"oz": {"cal": 96, "fat": 0.1, "carbs": 24, "protein": 0.2, "sodium": 4, "fiber": 0.4, "sugar": 19}},
    "lady fingers": {"each": {"cal": 40, "fat": 1, "carbs": 7, "protein": 1, "sodium": 16, "fiber": 0, "sugar": 4},
                    "doz": {"cal": 480, "fat": 12, "carbs": 84, "protein": 12, "sodium": 192, "fiber": 0, "sugar": 48}},

    # Condiments
    "pickle relish": {"tbsp": {"cal": 14, "fat": 0.1, "carbs": 3.5, "protein": 0.1, "sodium": 164, "fiber": 0.2, "sugar": 2.5}},
    "pickle juice": {"cup": {"cal": 0, "fat": 0, "carbs": 0, "protein": 0, "sodium": 1800, "fiber": 0, "sugar": 0},
                    "tbsp": {"cal": 0, "fat": 0, "carbs": 0, "protein": 0, "sodium": 113, "fiber": 0, "sugar": 0}},
    "horseradish": {"tbsp": {"cal": 7, "fat": 0.1, "carbs": 2, "protein": 0.2, "sodium": 47, "fiber": 0.5, "sugar": 1}},
    "prepared horseradish": {"tbsp": {"cal": 7, "fat": 0.1, "carbs": 2, "protein": 0.2, "sodium": 47, "fiber": 0.5, "sugar": 1}},

    # Fruits
    "gooseberries": {"cup": {"cal": 66, "fat": 0.9, "carbs": 15, "protein": 1.3, "sodium": 2, "fiber": 6.5, "sugar": 0},
                    "lb": {"cal": 134, "fat": 1.8, "carbs": 30, "protein": 2.6, "sodium": 4, "fiber": 13, "sugar": 0}},
    "ripe gooseberries": {"lb": {"cal": 134, "fat": 1.8, "carbs": 30, "protein": 2.6, "sodium": 4, "fiber": 13, "sugar": 0}},
    "roma tomatoes": {"each": {"cal": 11, "fat": 0.1, "carbs": 2.4, "protein": 0.5, "sodium": 3, "fiber": 0.7, "sugar": 1.6},
                     "cup": {"cal": 32, "fat": 0.4, "carbs": 7, "protein": 1.6, "sodium": 9, "fiber": 2, "sugar": 5}},

    # Meat alternatives
    "tvp": {"cup": {"cal": 222, "fat": 0.5, "carbs": 21, "protein": 35, "sodium": 4, "fiber": 12, "sugar": 9}},
    "textured vegetable protein": {"cup": {"cal": 222, "fat": 0.5, "carbs": 21, "protein": 35, "sodium": 4, "fiber": 12, "sugar": 9}},

    # Canned goods
    "clam juice": {"cup": {"cal": 6, "fat": 0, "carbs": 0, "protein": 1, "sodium": 640, "fiber": 0, "sugar": 0},
                  "bottle": {"cal": 12, "fat": 0, "carbs": 0, "protein": 2, "sodium": 1280, "fiber": 0, "sugar": 0}},
    "crabmeat": {"cup": {"cal": 134, "fat": 2, "carbs": 0, "protein": 28, "sodium": 600, "fiber": 0, "sugar": 0},
                "can": {"cal": 100, "fat": 1.5, "carbs": 0, "protein": 21, "sodium": 450, "fiber": 0, "sugar": 0},
                "oz": {"cal": 25, "fat": 0.4, "carbs": 0, "protein": 5, "sodium": 95, "fiber": 0, "sugar": 0}},
    "peach syrup": {"cup": {"cal": 240, "fat": 0, "carbs": 60, "protein": 0, "sodium": 10, "fiber": 0, "sugar": 55}},

    # Baked goods
    "saltine crackers": {"each": {"cal": 13, "fat": 0.3, "carbs": 2.2, "protein": 0.3, "sodium": 38, "fiber": 0.1, "sugar": 0},
                        "cup": {"cal": 195, "fat": 4.5, "carbs": 33, "protein": 4.5, "sodium": 570, "fiber": 1.5, "sugar": 0}},
    "ritz crackers": {"tube": {"cal": 1600, "fat": 80, "carbs": 200, "protein": 16, "sodium": 3200, "fiber": 8, "sugar": 24},
                     "each": {"cal": 16, "fat": 0.8, "carbs": 2, "protein": 0.2, "sodium": 32, "fiber": 0.1, "sugar": 0.2}},

    # Flavored gelatin
    "lemon-flavored gelatin": {"pkg": {"cal": 80, "fat": 0, "carbs": 19, "protein": 2, "sodium": 120, "fiber": 0, "sugar": 19}},
    "orange-flavored gelatin": {"pkg": {"cal": 80, "fat": 0, "carbs": 19, "protein": 2, "sodium": 120, "fiber": 0, "sugar": 19}},
    "strawberry gelatin": {"pkg": {"cal": 80, "fat": 0, "carbs": 19, "protein": 2, "sodium": 120, "fiber": 0, "sugar": 19}},
    "lime gelatin": {"pkg": {"cal": 80, "fat": 0, "carbs": 19, "protein": 2, "sodium": 120, "fiber": 0, "sugar": 19}},
    "unflavored gelatin": {"envelope": {"cal": 23, "fat": 0, "carbs": 0, "protein": 6, "sodium": 14, "fiber": 0, "sugar": 0},
                          "pkg": {"cal": 23, "fat": 0, "carbs": 0, "protein": 6, "sodium": 14, "fiber": 0, "sugar": 0}},

    # Beverages
    "gingerale": {"cup": {"cal": 83, "fat": 0, "carbs": 21, "protein": 0, "sodium": 26, "fiber": 0, "sugar": 21}},
    "apple cider": {"cup": {"cal": 117, "fat": 0.3, "carbs": 29, "protein": 0.2, "sodium": 5, "fiber": 0.2, "sugar": 24},
                   "gallon": {"cal": 1872, "fat": 4.8, "carbs": 464, "protein": 3.2, "sodium": 80, "fiber": 3.2, "sugar": 384}},

    # Misc
    "spanish rice": {"cup": {"cal": 130, "fat": 1, "carbs": 28, "protein": 3, "sodium": 510, "fiber": 1, "sugar": 2}},
    "savory pie crust": {"each": {"cal": 620, "fat": 39, "carbs": 60, "protein": 7, "sodium": 560, "fiber": 2, "sugar": 2}},
    "deep dish pie crust": {"each": {"cal": 720, "fat": 45, "carbs": 70, "protein": 8, "sodium": 650, "fiber": 2, "sugar": 3}},
    "enchilada sauce": {"cup": {"cal": 60, "fat": 1, "carbs": 11, "protein": 2, "sodium": 1160, "fiber": 2, "sugar": 4},
                       "can": {"cal": 90, "fat": 1.5, "carbs": 16, "protein": 3, "sodium": 1740, "fiber": 3, "sugar": 6}},
    "red enchilada sauce": {"cup": {"cal": 60, "fat": 1, "carbs": 11, "protein": 2, "sodium": 1160, "fiber": 2, "sugar": 4}},

    # BATCH 14: Additional missing ingredients and units
    # New entries for missing items
    "red onion": {"cup": {"cal": 64, "fat": 0.2, "carbs": 15, "protein": 2, "sodium": 6, "fiber": 2, "sugar": 7},
                 "medium": {"cal": 44, "fat": 0.1, "carbs": 10, "protein": 1.3, "sodium": 4, "fiber": 1.5, "sugar": 5},
                 "tbsp": {"cal": 4, "fat": 0, "carbs": 1, "protein": 0.1, "sodium": 0, "fiber": 0.1, "sugar": 0.4}},
    "light mayonnaise": {"tbsp": {"cal": 35, "fat": 3.5, "carbs": 1, "protein": 0, "sodium": 100, "fiber": 0, "sugar": 1},
                        "cup": {"cal": 560, "fat": 56, "carbs": 16, "protein": 0, "sodium": 1600, "fiber": 0, "sugar": 16}},
    "hemp seeds": {"tbsp": {"cal": 55, "fat": 4.5, "carbs": 1, "protein": 3, "sodium": 0, "fiber": 0.5, "sugar": 0},
                  "cup": {"cal": 880, "fat": 72, "carbs": 16, "protein": 48, "sodium": 0, "fiber": 8, "sugar": 0}},
    "pumpkin seeds": {"cup": {"cal": 721, "fat": 63, "carbs": 25, "protein": 34, "sodium": 25, "fiber": 12, "sugar": 2},
                     "oz": {"cal": 126, "fat": 11, "carbs": 4.4, "protein": 6, "sodium": 4, "fiber": 2, "sugar": 0.4},
                     "tbsp": {"cal": 45, "fat": 4, "carbs": 1.5, "protein": 2, "sodium": 2, "fiber": 0.7, "sugar": 0.1}},
    "sunflower seeds": {"cup": {"cal": 818, "fat": 72, "carbs": 28, "protein": 29, "sodium": 5, "fiber": 12, "sugar": 3},
                       "oz": {"cal": 165, "fat": 14, "carbs": 5.6, "protein": 5.8, "sodium": 1, "fiber": 2.4, "sugar": 0.6},
                       "tbsp": {"cal": 51, "fat": 4.5, "carbs": 1.8, "protein": 1.8, "sodium": 0, "fiber": 0.7, "sugar": 0.2}},
    "poppy seeds": {"tbsp": {"cal": 46, "fat": 4, "carbs": 2, "protein": 1.5, "sodium": 2, "fiber": 1, "sugar": 0.3},
                   "tsp": {"cal": 15, "fat": 1.3, "carbs": 0.7, "protein": 0.5, "sodium": 0.5, "fiber": 0.3, "sugar": 0.1}},
    "caraway seeds": {"tsp": {"cal": 7, "fat": 0.3, "carbs": 1, "protein": 0.4, "sodium": 0.4, "fiber": 0.8, "sugar": 0},
                     "tbsp": {"cal": 21, "fat": 0.9, "carbs": 3, "protein": 1.2, "sodium": 1, "fiber": 2.4, "sugar": 0}},
    "dark sesame oil": {"tbsp": {"cal": 120, "fat": 14, "carbs": 0, "protein": 0, "sodium": 0, "fiber": 0, "sugar": 0},
                       "tsp": {"cal": 40, "fat": 4.5, "carbs": 0, "protein": 0, "sodium": 0, "fiber": 0, "sugar": 0}},
    "ground chipotle pepper": {"tsp": {"cal": 8, "fat": 0.4, "carbs": 1.5, "protein": 0.3, "sodium": 26, "fiber": 0.9, "sugar": 0.5}},
    "chipotle chile pepper": {"tsp": {"cal": 8, "fat": 0.4, "carbs": 1.5, "protein": 0.3, "sodium": 26, "fiber": 0.9, "sugar": 0.5}},
    "asian chili sauce": {"tsp": {"cal": 6, "fat": 0, "carbs": 1.2, "protein": 0.2, "sodium": 100, "fiber": 0.2, "sugar": 0.8},
                         "tbsp": {"cal": 18, "fat": 0, "carbs": 3.6, "protein": 0.6, "sodium": 300, "fiber": 0.6, "sugar": 2.4}},
    "turkey italian sausage": {"link": {"cal": 140, "fat": 8, "carbs": 2, "protein": 14, "sodium": 480, "fiber": 0, "sugar": 1},
                              "oz": {"cal": 44, "fat": 2.5, "carbs": 0.6, "protein": 4.4, "sodium": 150, "fiber": 0, "sugar": 0.3},
                              "lb": {"cal": 704, "fat": 40, "carbs": 10, "protein": 70, "sodium": 2400, "fiber": 0, "sugar": 5}},
    "clam juice": {"cup": {"cal": 5, "fat": 0, "carbs": 0, "protein": 1, "sodium": 516, "fiber": 0, "sugar": 0},
                  "oz": {"cal": 0.6, "fat": 0, "carbs": 0, "protein": 0.1, "sodium": 64, "fiber": 0, "sugar": 0},
                  "bottle": {"cal": 5, "fat": 0, "carbs": 0, "protein": 1, "sodium": 516, "fiber": 0, "sugar": 0}},
    "beef roast": {"lb": {"cal": 816, "fat": 48, "carbs": 0, "protein": 88, "sodium": 280, "fiber": 0, "sugar": 0},
                  "oz": {"cal": 51, "fat": 3, "carbs": 0, "protein": 5.5, "sodium": 18, "fiber": 0, "sugar": 0}},
    "chuck roast": {"lb": {"cal": 1080, "fat": 72, "carbs": 0, "protein": 96, "sodium": 320, "fiber": 0, "sugar": 0},
                   "oz": {"cal": 67, "fat": 4.5, "carbs": 0, "protein": 6, "sodium": 20, "fiber": 0, "sugar": 0}},
    "canned tomatoes": {"can": {"cal": 72, "fat": 0.4, "carbs": 16, "protein": 3.2, "sodium": 640, "fiber": 4, "sugar": 10},
                       "cup": {"cal": 41, "fat": 0.2, "carbs": 9, "protein": 1.8, "sodium": 360, "fiber": 2.2, "sugar": 5.5}},
    # Additional units for existing items
    "cucumber": {"cup": {"cal": 16, "fat": 0.1, "carbs": 4, "protein": 0.7, "sodium": 2, "fiber": 0.5, "sugar": 2},
                "medium": {"cal": 24, "fat": 0.2, "carbs": 6, "protein": 1, "sodium": 3, "fiber": 0.7, "sugar": 3},
                "each": {"cal": 45, "fat": 0.3, "carbs": 11, "protein": 2, "sodium": 6, "fiber": 1.5, "sugar": 5}},
    "lettuce": {"cup": {"cal": 5, "fat": 0.1, "carbs": 1, "protein": 0.5, "sodium": 5, "fiber": 0.5, "sugar": 0.4},
               "leaf": {"cal": 1, "fat": 0, "carbs": 0.2, "protein": 0.1, "sodium": 1, "fiber": 0.1, "sugar": 0.1},
               "head": {"cal": 54, "fat": 0.5, "carbs": 10, "protein": 5, "sodium": 50, "fiber": 5, "sugar": 4}},

    # BATCH 15: More missing ingredients and expanded units
    # Spices & seasonings
    "italian herbs": {"tsp": {"cal": 3, "fat": 0.1, "carbs": 0.6, "protein": 0.1, "sodium": 1, "fiber": 0.3, "sugar": 0},
                     "tbsp": {"cal": 9, "fat": 0.3, "carbs": 1.8, "protein": 0.3, "sodium": 3, "fiber": 0.9, "sugar": 0}},
    "ground pepper": {"tsp": {"cal": 6, "fat": 0.1, "carbs": 1.4, "protein": 0.2, "sodium": 1, "fiber": 0.6, "sugar": 0},
                     "tbsp": {"cal": 18, "fat": 0.3, "carbs": 4.2, "protein": 0.6, "sodium": 3, "fiber": 1.8, "sugar": 0}},
    "lemon-pepper seasoning": {"tsp": {"cal": 7, "fat": 0.1, "carbs": 1.5, "protein": 0.2, "sodium": 340, "fiber": 0.3, "sugar": 0.2}},
    "ground mustard": {"tsp": {"cal": 9, "fat": 0.5, "carbs": 0.6, "protein": 0.5, "sodium": 0, "fiber": 0.2, "sugar": 0}},
    "rubbed sage": {"tsp": {"cal": 2, "fat": 0.1, "carbs": 0.4, "protein": 0.1, "sodium": 0, "fiber": 0.3, "sugar": 0}},
    "cajun seasoning": {"tsp": {"cal": 8, "fat": 0.3, "carbs": 1.5, "protein": 0.3, "sodium": 200, "fiber": 0.5, "sugar": 0.2},
                       "tbsp": {"cal": 24, "fat": 0.9, "carbs": 4.5, "protein": 0.9, "sodium": 600, "fiber": 1.5, "sugar": 0.6}},
    "ground cardamom": {"tsp": {"cal": 6, "fat": 0.1, "carbs": 1.4, "protein": 0.2, "sodium": 0, "fiber": 0.6, "sugar": 0}},
    "ground turmeric": {"tsp": {"cal": 8, "fat": 0.2, "carbs": 1.4, "protein": 0.3, "sodium": 1, "fiber": 0.5, "sugar": 0.1}},
    "chipotle": {"tsp": {"cal": 8, "fat": 0.4, "carbs": 1.5, "protein": 0.3, "sodium": 26, "fiber": 0.9, "sugar": 0.5},
                "each": {"cal": 15, "fat": 0.8, "carbs": 3, "protein": 0.6, "sodium": 52, "fiber": 1.8, "sugar": 1}},
    "pepper sauce": {"tsp": {"cal": 1, "fat": 0, "carbs": 0.1, "protein": 0, "sodium": 124, "fiber": 0, "sugar": 0},
                    "tbsp": {"cal": 3, "fat": 0, "carbs": 0.3, "protein": 0, "sodium": 372, "fiber": 0, "sugar": 0}},
    # Cheese
    "part-skim mozzarella cheese": {"cup": {"cal": 336, "fat": 20, "carbs": 4, "protein": 32, "sodium": 704, "fiber": 0, "sugar": 2},
                                    "oz": {"cal": 72, "fat": 4.5, "carbs": 0.8, "protein": 7, "sodium": 150, "fiber": 0, "sugar": 0.4}},
    "jack cheese": {"cup": {"cal": 422, "fat": 34, "carbs": 2, "protein": 28, "sodium": 660, "fiber": 0, "sugar": 0.5},
                   "oz": {"cal": 106, "fat": 8.5, "carbs": 0.5, "protein": 7, "sodium": 165, "fiber": 0, "sugar": 0.1}},
    "blue cheese crumbles": {"cup": {"cal": 476, "fat": 39, "carbs": 3, "protein": 29, "sodium": 1395, "fiber": 0, "sugar": 0.5},
                            "oz": {"cal": 100, "fat": 8, "carbs": 0.7, "protein": 6, "sodium": 325, "fiber": 0, "sugar": 0.1},
                            "tbsp": {"cal": 30, "fat": 2.5, "carbs": 0.2, "protein": 1.8, "sodium": 87, "fiber": 0, "sugar": 0}},
    # Vegetables
    "fresh mushrooms": {"cup": {"cal": 15, "fat": 0.2, "carbs": 2.3, "protein": 2.2, "sodium": 4, "fiber": 0.7, "sugar": 1.4},
                       "oz": {"cal": 6, "fat": 0.1, "carbs": 0.9, "protein": 0.9, "sodium": 1.5, "fiber": 0.3, "sugar": 0.5}},
    "fresh gingerroot": {"tbsp": {"cal": 5, "fat": 0, "carbs": 1, "protein": 0.1, "sodium": 1, "fiber": 0.1, "sugar": 0.1},
                        "tsp": {"cal": 2, "fat": 0, "carbs": 0.4, "protein": 0, "sodium": 0, "fiber": 0, "sugar": 0},
                        "inch": {"cal": 8, "fat": 0.1, "carbs": 1.8, "protein": 0.2, "sodium": 1, "fiber": 0.2, "sugar": 0.2}},
    "medium green pepper": {"": {"cal": 24, "fat": 0.2, "carbs": 5.5, "protein": 1, "sodium": 4, "fiber": 2, "sugar": 3}},
    "medium zucchini": {"": {"cal": 33, "fat": 0.4, "carbs": 6, "protein": 2.4, "sodium": 16, "fiber": 2, "sugar": 5}},
    "medium ripe avocado": {"": {"cal": 240, "fat": 22, "carbs": 13, "protein": 3, "sodium": 11, "fiber": 10, "sugar": 1}},
    "medium carrot": {"": {"cal": 25, "fat": 0.1, "carbs": 6, "protein": 0.6, "sodium": 42, "fiber": 1.7, "sugar": 3}},
    "medium cucumber": {"": {"cal": 24, "fat": 0.2, "carbs": 6, "protein": 1, "sodium": 3, "fiber": 0.7, "sugar": 3}},
    "coleslaw mix": {"cup": {"cal": 17, "fat": 0.1, "carbs": 4, "protein": 1, "sodium": 13, "fiber": 1.4, "sugar": 2},
                    "bag": {"cal": 85, "fat": 0.5, "carbs": 20, "protein": 5, "sodium": 65, "fiber": 7, "sugar": 10}},
    # Meat
    "pork loin chops": {"lb": {"cal": 680, "fat": 28, "carbs": 0, "protein": 100, "sodium": 260, "fiber": 0, "sugar": 0},
                       "oz": {"cal": 43, "fat": 1.8, "carbs": 0, "protein": 6.3, "sodium": 16, "fiber": 0, "sugar": 0},
                       "each": {"cal": 170, "fat": 7, "carbs": 0, "protein": 25, "sodium": 65, "fiber": 0, "sugar": 0}},
    "lean ground turkey": {"lb": {"cal": 720, "fat": 36, "carbs": 0, "protein": 92, "sodium": 400, "fiber": 0, "sugar": 0},
                          "oz": {"cal": 45, "fat": 2.3, "carbs": 0, "protein": 5.8, "sodium": 25, "fiber": 0, "sugar": 0}},
    "beef steak": {"lb": {"cal": 880, "fat": 56, "carbs": 0, "protein": 88, "sodium": 280, "fiber": 0, "sugar": 0},
                  "oz": {"cal": 55, "fat": 3.5, "carbs": 0, "protein": 5.5, "sodium": 18, "fiber": 0, "sugar": 0}},
    "white fish": {"lb": {"cal": 400, "fat": 4, "carbs": 0, "protein": 84, "sodium": 300, "fiber": 0, "sugar": 0},
                  "oz": {"cal": 25, "fat": 0.3, "carbs": 0, "protein": 5.3, "sodium": 19, "fiber": 0, "sugar": 0},
                  "fillet": {"cal": 100, "fat": 1, "carbs": 0, "protein": 21, "sodium": 75, "fiber": 0, "sugar": 0}},
    # Broths
    "reduced-sodium chicken broth": {"cup": {"cal": 15, "fat": 0.5, "carbs": 1, "protein": 2, "sodium": 450, "fiber": 0, "sugar": 0},
                                    "can": {"cal": 22, "fat": 0.8, "carbs": 1.5, "protein": 3, "sodium": 675, "fiber": 0, "sugar": 0}},
    "reduced-sodium beef broth": {"cup": {"cal": 17, "fat": 0.5, "carbs": 1, "protein": 3, "sodium": 440, "fiber": 0, "sugar": 0},
                                 "can": {"cal": 25, "fat": 0.8, "carbs": 1.5, "protein": 4.5, "sodium": 660, "fiber": 0, "sugar": 0}},
    "beef bouillon granules": {"tsp": {"cal": 5, "fat": 0.2, "carbs": 0.5, "protein": 0.5, "sodium": 900, "fiber": 0, "sugar": 0},
                              "tbsp": {"cal": 15, "fat": 0.6, "carbs": 1.5, "protein": 1.5, "sodium": 2700, "fiber": 0, "sugar": 0}},
    # Sauces
    "barbecue sauce": {"tbsp": {"cal": 29, "fat": 0.1, "carbs": 7, "protein": 0.2, "sodium": 175, "fiber": 0.2, "sugar": 5},
                      "cup": {"cal": 464, "fat": 1.6, "carbs": 112, "protein": 3.2, "sodium": 2800, "fiber": 3.2, "sugar": 80}},
    "bechamel sauce": {"cup": {"cal": 308, "fat": 22, "carbs": 18, "protein": 9, "sodium": 680, "fiber": 0.5, "sugar": 8},
                      "tbsp": {"cal": 19, "fat": 1.4, "carbs": 1.1, "protein": 0.6, "sodium": 42, "fiber": 0, "sugar": 0.5}},
    # Miscellaneous
    "chips": {"cup": {"cal": 274, "fat": 18, "carbs": 25, "protein": 3, "sodium": 268, "fiber": 2, "sugar": 0.5},
             "oz": {"cal": 152, "fat": 10, "carbs": 14, "protein": 1.7, "sodium": 149, "fiber": 1.1, "sugar": 0.3}},
    "pita": {"each": {"cal": 165, "fat": 0.7, "carbs": 34, "protein": 5.5, "sodium": 322, "fiber": 1.3, "sugar": 0.7},
            "half": {"cal": 82, "fat": 0.4, "carbs": 17, "protein": 2.8, "sodium": 161, "fiber": 0.7, "sugar": 0.4}},
}

# =============================================================================
# STANDARD CAN & JAR SIZES
# =============================================================================

STANDARD_CAN_SIZES = {
    # Size name: ounces
    "small": 8,
    "regular": 14.5,
    "standard": 14.5,
    "large": 28,
    "family": 28,
    "#10": 106,  # Restaurant size
    "#300": 14,
    "#303": 16,
    "#2": 20,
    "#2.5": 28,
    "#3": 46,
}

STANDARD_JAR_SIZES = {
    # Size name: ounces
    "small": 8,
    "regular": 16,
    "standard": 16,
    "large": 24,
    "family": 32,
}

# =============================================================================
# INGREDIENT NORMALIZATION
# =============================================================================

def parse_quantity(qty_str):
    """Parse quantity string to float, handling fractions and ranges."""
    if not qty_str or qty_str.strip() == "":
        return 1.0

    qty_str = str(qty_str).strip().lower()

    # Handle ranges like "1-2" or "6-8" - take midpoint
    if '-' in qty_str and not qty_str.startswith('-'):
        parts = qty_str.split('-')
        if len(parts) == 2:
            try:
                low = parse_quantity(parts[0])
                high = parse_quantity(parts[1])
                return (low + high) / 2
            except:
                pass

    # Handle "to" ranges like "6 to 8"
    if ' to ' in qty_str:
        parts = qty_str.split(' to ')
        if len(parts) == 2:
            try:
                low = parse_quantity(parts[0])
                high = parse_quantity(parts[1])
                return (low + high) / 2
            except:
                pass

    # Handle mixed numbers like "1 1/2"
    parts = qty_str.split()
    total = 0
    for part in parts:
        try:
            if '/' in part:
                total += float(Fraction(part))
            else:
                # Remove any trailing punctuation
                part = part.rstrip('.,;:')
                total += float(part)
        except (ValueError, ZeroDivisionError):
            continue

    return total if total > 0 else 1.0


def normalize_unit(unit):
    """Normalize unit names to standard forms."""
    unit = str(unit).lower().strip().rstrip('.')

    unit_map = {
        # Volume
        "cups": "cup", "c": "cup", "c.": "cup",
        "tablespoons": "tbsp", "tablespoon": "tbsp", "tbsps": "tbsp", "t": "tbsp", "tbs": "tbsp", "tbl": "tbsp",
        "tblsp": "tbsp", "tblsps": "tbsp", "tblsp.": "tbsp", "tblsps.": "tbsp",
        "teaspoons": "tsp", "teaspoon": "tsp", "tsps": "tsp", "t.": "tsp",
        "ounces": "oz", "ounce": "oz", "ozs": "oz",
        "pounds": "lb", "pound": "lb", "lbs": "lb",
        "pints": "pint", "pt": "pint",
        "quarts": "quart", "qt": "quart",
        "gallons": "gallon", "gal": "gallon",
        # Historical measurements (Batch 14)
        "gill": "gill", "gills": "gill",  # 4 fl oz = 0.5 cup
        "drachm": "drachm", "drachms": "drachm", "dram": "drachm", "drams": "drachm",  # 1/8 oz
        "dessertspoon": "dessertspoon", "dessertspoons": "dessertspoon", "dssp": "dessertspoon",  # 2 tsp
        "saltspoon": "saltspoon", "saltspoons": "saltspoon", "saltspoonful": "saltspoon", "saltspoonfuls": "saltspoon",  # 1/4 tsp
        "wineglass": "wineglass", "wineglasses": "wineglass", "wine glass": "wineglass", "wine glasses": "wineglass",  # ~4 fl oz = 0.5 cup
        "teacup": "teacup", "teacups": "teacup", "tea cup": "teacup", "tea cups": "teacup",  # ~6 fl oz = 0.75 cup
        "coffeecup": "coffeecup", "coffeecups": "coffeecup", "coffee cup": "coffeecup", "coffee cups": "coffeecup",  # ~1 cup
        "jigger": "jigger", "jiggers": "jigger",  # 1.5 oz = 3 tbsp
        "peck": "peck", "pecks": "peck", "pk": "peck",  # 8 quarts (dry)
        "bushel": "bushel", "bushels": "bushel", "bu": "bushel",  # 4 pecks = 32 quarts
        "firkin": "firkin", "firkins": "firkin",  # 9 gallons
        "hogshead": "hogshead", "hogsheads": "hogshead",  # 63 gallons
        # Count
        "slices": "slice",
        "links": "link",
        "cloves": "clove",
        "cans": "can",
        "packages": "packet", "pkg": "packet", "pkgs": "packet", "packets": "packet", "pkg.": "packet",
        "sachet (7g)": "sachet", "sachets": "sachet",
        "envelopes": "envelope",
        "stalks": "stalk",
        "sprigs": "sprig",
        "ears": "ear",
        "bunches": "bunch",
        "heads": "head",
        "loaves": "loaf",
        "pieces": "piece", "pc": "piece", "pcs": "piece",
        # Size-based
        "small": "small", "sm": "small",
        "medium": "medium", "med": "medium",
        "large": "large", "lg": "large",
    }

    # Handle embedded sizes like "can (17 oz)" or "cup (4 oz)" → strip the size
    import re
    embedded_size = re.match(r'^(\w+)\s*\([\d\s.]+\s*oz\)$', unit)
    if embedded_size:
        unit = embedded_size.group(1)

    # Handle "15 1/2 oz cans" or "14.5-oz cans" → "can"
    oz_cans = re.match(r'^[\d\s./½¼¾-]+\s*oz\.?\s*cans?$', unit)
    if oz_cans:
        unit = "can"

    # Handle "oz jar" or "16 oz jar" → "jar" (treat as can equivalent)
    oz_jar = re.match(r'^(?:[\d\s./]+\s*)?oz\.?\s*jar$', unit)
    if oz_jar:
        unit = "can"  # jars are roughly equivalent to cans

    # Descriptive units that should be treated as empty (each)
    descriptive_units = ["ripe", "fresh"]
    if unit in descriptive_units:
        unit = ""

    return unit_map.get(unit, unit)


def normalize_ingredient(item):
    """Normalize ingredient name for database lookup."""
    if not item:
        return ""

    item = str(item).lower().strip()

    # Fix unicode fractions
    unicode_fractions = {
        '½': '1/2', '¼': '1/4', '¾': '3/4', '⅓': '1/3', '⅔': '2/3',
        '⅛': '1/8', '⅜': '3/8', '⅝': '5/8', '⅞': '7/8'
    }
    for uf, replacement in unicode_fractions.items():
        item = item.replace(uf, replacement)

    # Normalize curly quotes and special characters
    item = item.replace('\u2019', "'")   # Right single curly quote '
    item = item.replace('\u2018', "'")   # Left single curly quote '
    item = item.replace('\u201c', '"')   # Left double curly quote "
    item = item.replace('\u201d', '"')   # Right double curly quote "
    item = item.replace('ﬂ', 'fl')  # fi/fl ligature
    item = item.replace('ﬁ', 'fi')  # fi ligature

    # Remove leading numbers/quantities EARLY so unit patterns can match (Batch 14 fix)
    import re
    item = re.sub(r'^\d+[\s/\d.-]*\s*', '', item)

    # Fix common OCR quirks in ingredient text
    ocr_fixes = [
        (r'^ful[s]?\s+of\s*', ''),           # item starts with "ful of" (OCR artifact)
        (r'^ful[s]?\s+', ''),                # item starts with "ful " (OCR artifact)
        (r'\btsp\s*ful\s*of\b', ''),         # "tsp ful of" -> ""
        (r'\btbsp\s*ful[s]?\s*of\b', ''),    # "tbsp fuls of" -> ""
        (r'\btsp\s*ful\b', ''),              # "tsp ful" -> ""
        (r'\btbsp\s*ful[s]?\b', ''),         # "tbsp fuls" -> ""
        (r'\btblsp\.?\b', ''),               # "tblsp" -> ""
        (r'\blevel\s+tablespoonful[s]?\s+of\b', ''),  # "level tablespoonfuls of"
        (r'\blevel\s+teaspoonful[s]?\s+of\b', ''),    # "level teaspoonfuls of"
        (r'\bsaltspoonful\s+of\b', ''),      # "saltspoonful of" -> ""
        (r'\bfew\s+grains\b', ''),           # "few grains" -> ""
        (r'\bdash\s+of\b', ''),              # "dash of" -> ""
        (r'\bdash\s+', ''),                  # "dash " embedded in item
        (r'\bpinch\s+', ''),                 # "pinch " embedded in item
        (r'\btsp\.?\s+', ''),                # "tsp " or "tsp. " embedded in item
        (r'\btbsp\.?\s+', ''),               # "tbsp " embedded in item
        (r'^t\s+', ''),                      # "t " at start (abbreviation for tsp)
        (r'^c\s+', ''),                      # "c " at start (abbreviation for cup)
        (r'^T\s+', ''),                      # "T " at start (abbreviation for tbsp)
        # Full-word units embedded in item (Batch 14)
        (r'^teaspoons?\s+', ''),             # "teaspoon " or "teaspoons " at start
        (r'^tablespoons?\s+', ''),           # "tablespoon " or "tablespoons " at start
        (r'^ounces?\s+', ''),                # "ounce " or "ounces " at start
        (r'^pounds?\s+', ''),                # "pound " or "pounds " at start
        (r'\b1/2\s+cups?\s+', ''),           # "1/2 cup(s) " embedded
        (r'\b1/4\s+cups?\s+', ''),           # "1/4 cup(s) " embedded
        (r'\b3/4\s+cups?\s+', ''),           # "3/4 cup(s) " embedded
        (r'\b1/2\s+tsp\.?\s+', ''),          # "1/2 tsp " embedded
        (r'\b1/4\s+tsp\.?\s+', ''),          # "1/4 tsp " embedded
        (r'\b1/2\s+tbsp\.?\s+', ''),         # "1/2 tbsp " embedded
        (r'\bcup[s]?\s+', ''),               # "cup " embedded in item
        (r'\bpint[s]?\s+', ''),              # "pint " embedded in item
        (r'\bquart[s]?\s+', ''),             # "quart " embedded in item
        (r'\bpound[s]?\s+', ''),             # "pound " embedded in item
        (r'\s+of\s+', ' '),                  # " of " -> " "
        (r'\s*\.\s*$', ''),                  # trailing period
        (r'\s*\.\s+', ' '),                  # period in middle
        (r'-\s+', ' '),                      # hyphen with trailing space (OCR line-break)
        (r'\s+-', ' '),                      # space before hyphen
        (r',\s*$', ''),                      # trailing comma
        (r'\s{2,}', ' '),                    # multiple spaces
    ]
    for pattern, replacement in ocr_fixes:
        item = re.sub(pattern, replacement, item)

    # Remove prep notes after comma
    if "," in item:
        item = item.split(",")[0].strip()

    # Remove parenthetical notes (including leading ones like "(4 oz)")
    item = re.sub(r'^\([^)]*\)\s*', '', item)  # Leading parenthetical
    item = re.sub(r'\s*\([^)]*\)', '', item)   # Embedded parenthetical

    # Second pass: Remove any new leading numbers exposed after parenthetical removal
    item = re.sub(r'^\d+[\s/\d.-]*\s*', '', item)

    # Common prefixes to remove
    prefixes = [
        "fresh ", "frozen ", "dried ", "canned ", "cooked ", "raw ",
        "chopped ", "diced ", "minced ", "sliced ", "cubed ",
        "grated ", "shredded ", "mashed ", "crushed ", "crumbled ",
        "melted ", "softened ", "room temperature ", "cold ", "warm ", "hot ",
        "ripe ", "peeled ", "pitted ", "seeded ", "cored ",
        "toasted ", "roasted ", "sauteed ",
        "sifted ", "packed ", "firmly packed ", "lightly packed ",
        "finely ", "coarsely ", "roughly ", "thinly ",
        "boneless ", "skinless ",
        "low-fat ", "lowfat ", "low fat ", "nonfat ", "non-fat ", "fat-free ",
        "unsalted ", "salted ",
        "pure ", "organic ", "natural ",
        "about ", "approximately ", "approx ",
    ]

    for prefix in prefixes:
        if item.startswith(prefix):
            item = item[len(prefix):]

    # Brand name normalization (use straight quotes since curly quotes are normalized earlier)
    brand_map = {
        "grandma's molasses": "molasses",
        "grandmas molasses": "molasses",
        "carnation milk": "evaporated milk",
        "gold medal flour": "flour",
        "pillsbury flour": "flour",
        "crisco": "shortening",
        "pam": "cooking spray",
        "kraft": "",
        "heinz": "",
        "hellmann's": "mayonnaise",
        "best foods": "mayonnaise",
        "philadelphia": "cream cheese",
        "jell-o": "gelatin",
        "knox": "gelatin",
        "bisquick": "biscuit mix",
        "jiffy": "corn muffin mix",
        "shedd's spread country crock calcium plus vitamin d": "margarine",
        "shedd's spread country crock": "margarine",
        "shedd's spread": "margarine",
        "country crock": "margarine",
        "i can't believe it's not butter": "margarine",
        "campbell's": "",
        "swanson": "",
        "progresso": "",
        "lipton": "",
        "mccormick": "",
    }

    for brand, replacement in brand_map.items():
        if brand in item:
            if replacement:
                item = replacement
            else:
                item = item.replace(brand, "").strip()

    # Common ingredient synonyms
    synonyms = {
        # Flour
        "all purpose flour": "flour",
        "all-purpose flour": "flour",
        "ap flour": "flour",
        "plain flour": "flour",
        "unbleached flour": "flour",
        "enriched flour": "flour",
        "strong white bread flour": "bread flour",

        # Sugar
        "granulated sugar": "sugar",
        "white sugar": "sugar",
        "cane sugar": "sugar",
        "light brown sugar": "brown sugar",
        "dark brown sugar": "brown sugar",
        "confectioners sugar": "powdered sugar",
        "confectioner's sugar": "powdered sugar",
        "icing sugar": "powdered sugar",
        "10x sugar": "powdered sugar",

        # Eggs
        "large eggs": "egg",
        "eggs": "egg",
        "whole egg": "egg",
        "beaten egg": "egg",
        "egg whites": "egg white",
        "egg yolks": "egg yolk",

        # Dairy
        "whole milk": "milk",
        "2% milk": "milk",
        "1% milk": "skim milk",
        "fat free milk": "skim milk",
        "heavy whipping cream": "heavy cream",
        "whipping cream": "heavy cream",

        # Butter
        "unsalted butter": "butter",
        "salted butter": "butter",
        "stick butter": "butter",
        "butter or margarine": "butter",

        # Oil
        "canola oil": "vegetable oil",
        "corn oil": "vegetable oil",
        "safflower oil": "vegetable oil",
        "cooking oil": "vegetable oil",
        "extra virgin olive oil": "olive oil",
        "extra-virgin olive oil": "olive oil",
        "evoo": "olive oil",

        # Chicken
        "chicken breasts": "chicken breast",
        "boneless skinless chicken breasts": "chicken breast",
        "boneless skinless chicken breast": "chicken breast",
        "whole chicken breasts": "chicken breast",
        "chicken thighs": "chicken thigh",
        "boneless skinless chicken thighs": "chicken thigh",

        # Ground meats
        "lean ground beef": "ground beef",
        "ground chuck": "ground beef",
        "hamburger": "ground beef",
        "hamburger meat": "ground beef",

        # Onion/garlic
        "yellow onion": "onion",
        "white onion": "onion",
        "red onion": "onion",
        "sweet onion": "onion",
        "vidalia onion": "onion",
        "garlic cloves": "garlic",
        "cloves garlic": "garlic",
        "garlic clove": "garlic",
        "green onions": "green onion",
        "scallions": "green onion",

        # Peppers
        "green bell pepper": "green pepper",
        "red bell pepper": "red pepper",
        "bell pepper": "bell pepper",
        "jalapeno pepper": "jalapeno",
        "jalapeño": "jalapeno",
        "serrano pepper": "jalapeno",

        # Tomatoes
        "roma tomatoes": "tomato",
        "plum tomatoes": "tomato",
        "cherry tomatoes": "tomato",
        "grape tomatoes": "tomato",
        "tomatoes": "tomato",

        # Potatoes
        "russet potato": "potato",
        "russet potatoes": "potato",
        "yukon gold potato": "potato",
        "red potato": "potato",
        "baking potato": "potato",
        "idaho potato": "potato",

        # Spices
        "ground cumin": "cumin",
        "ground cinnamon": "cinnamon",
        "ground ginger": "ginger",
        "ground nutmeg": "nutmeg",
        "ground cloves": "cloves",
        "ground allspice": "allspice",
        "ground black pepper": "black pepper",
        "freshly ground black pepper": "black pepper",
        "freshly ground pepper": "pepper",
        "kosher salt": "salt",
        "sea salt": "salt",
        "table salt": "salt",
        "salt and pepper": "salt",
        "salt & pepper": "salt",

        # Vanilla
        "pure vanilla extract": "vanilla extract",
        "vanilla": "vanilla extract",
        "pure vanilla": "vanilla extract",

        # Oatmeal
        "instant oatmeal packets": "instant oatmeal",
        "instant oatmeal packets plain": "instant oatmeal",
        "oatmeal packets": "instant oatmeal",
        "quaker instant oatmeal": "instant oatmeal",
        "quaker oats instant oatmeal": "instant oatmeal",
        "quick oats": "oats",
        "rolled oats": "oats",
        "old fashioned oats": "oats",

        # Baking
        "baking cocoa": "cocoa powder",
        "unsweetened cocoa": "cocoa powder",
        "unsweetened cocoa powder": "cocoa powder",
        "dutch process cocoa": "cocoa powder",
        "semisweet chocolate chips": "chocolate chips",
        "semi-sweet chocolate chips": "chocolate chips",
        "dark chocolate chips": "chocolate chips",
        "milk chocolate chips": "chocolate chips",
        "active dry yeast": "yeast",
        "instant yeast": "yeast",
        "rapid rise yeast": "yeast",
        "unflavored gelatin": "gelatin",

        # Broth
        "low sodium chicken broth": "chicken broth",
        "reduced sodium chicken broth": "chicken broth",
        "low sodium beef broth": "beef broth",
        "stock": "chicken broth",
        "chicken stock": "chicken broth",
        "beef stock": "beef broth",

        # Canned goods
        "condensed cream of chicken soup": "cream of chicken soup",
        "condensed cream of mushroom soup": "cream of mushroom soup",
        "condensed cream of celery soup": "cream of celery soup",
        "condensed tomato soup": "tomato soup",
        "petite diced tomatoes": "diced tomatoes",
        "fire roasted diced tomatoes": "diced tomatoes",
        "stewed tomatoes": "canned tomatoes",
        "whole tomatoes": "canned tomatoes",

        # Herbs
        "fresh parsley": "parsley",
        "flat-leaf parsley": "parsley",
        "italian parsley": "parsley",
        "fresh cilantro": "cilantro",
        "fresh basil": "basil",
        "fresh dill": "dill",
        "fresh thyme": "thyme",
        "fresh rosemary": "rosemary",
        "fresh mint": "mint",
        "fresh sage": "sage",

        # Fish
        "trout fillets": "trout",
        "trout fillet": "trout",
        "salmon fillets": "salmon",
        "salmon fillet": "salmon",
        "skinless trout": "trout",
        "skinless salmon": "salmon",

        # Leavening
        "soda": "baking soda",
        "bicarbonate of soda": "baking soda",
        "bicarb": "baking soda",
        "dry active yeast": "yeast",
        "dry yeast": "yeast",
        "fast-action dried yeast": "yeast",
        "fast action dried yeast": "yeast",
        "quick rise yeast": "yeast",

        # Milk variants
        "lukewarm milk": "milk",
        "warm milk": "milk",
        "cold milk": "milk",
        "whole milk": "milk",
        "2% milk": "milk",

        # Mustard variants
        "english mustard powder": "mustard powder",
        "dry mustard powder": "mustard powder",
        "coleman's mustard": "mustard powder",

        # Cheese variants
        "extra mature cheddar cheese": "cheddar cheese",
        "extra sharp cheddar cheese": "cheddar cheese",
        "sharp cheddar cheese": "cheddar cheese",
        "mild cheddar cheese": "cheddar cheese",
        "mature cheddar cheese": "cheddar cheese",

        # Citrus zest
        "lemon rind": "lemon zest",
        "grated lemon rind": "lemon zest",
        "lemon peel": "lemon zest",
        "orange rind": "orange zest",
        "grated orange rind": "orange zest",
        "orange peel": "orange zest",
        "lime rind": "lime zest",
        "grated lime rind": "lime zest",

        # Salt & pepper
        "salt and pepper": "salt",
        "salt & pepper": "salt",
        "kosher salt and pepper": "salt",
        "kosher salt and freshly ground pepper": "salt",
        "salt and freshly ground pepper": "salt",
        "salt and freshly ground black pepper": "salt",
        "salt to taste": "salt",
        "pepper to taste": "pepper",
        "paprika": "paprika",

        # Misc
        "fresh lemon juice": "lemon juice",
        "fresh lime juice": "lime juice",
        "worcestershire": "worcestershire sauce",
        "sour cream": "sour cream",
        "plain greek yogurt": "greek yogurt",
        "non-fat greek yogurt": "greek yogurt",
        "thick-cut bacon": "bacon",
        "thick cut bacon": "bacon",
        "turkey bacon": "bacon",
        "center-cut bacon": "bacon",

        # Cooking spray
        "cooking spray": "cooking spray",
        "nonstick cooking spray": "cooking spray",
        "non-stick cooking spray": "cooking spray",
        "vegetable cooking spray": "cooking spray",
        "butter flavored cooking spray": "cooking spray",

        # Pie crust
        "savory deep dish pie crust": "pie crust",
        "deep dish pie crust": "pie crust",
        "9-inch pie crust": "pie crust",
        "unbaked pie crust": "pie crust",
        "prepared pie crust": "pie crust",
        "refrigerated pie crust": "pie crust",

        # Creamed soups
        "cream chicken soup": "cream of chicken soup",
        "cream mushroom soup": "cream of mushroom soup",
        "cream celery soup": "cream of celery soup",

        # Tortillas
        "large flour tortillas": "flour tortilla",
        "flour tortillas": "flour tortilla",
        "corn tortillas": "corn tortilla",
        "10-inch flour tortillas": "flour tortilla",
        "8-inch flour tortillas": "flour tortilla",

        # Lemons/citrus
        "lemons": "lemon",
        "limes": "lime",
        "oranges": "orange",

        # Gelatin
        "envelope unflavored gelatin": "gelatin",
        "packet unflavored gelatin": "gelatin",
        "unflavored gelatine": "gelatin",

        # Additional gap analysis mappings
        "soft shortening": "shortening",
        "soft butter": "butter",
        "creamed butter": "butter",
        "sweet butter": "butter",
        "butter substitute": "butter",
        "chilled butter": "butter",
        "clove garlic": "garlic",
        "small onion": "onion",
        "medium onion": "onion",
        "large onion": "onion",
        "chopped onion": "onion",
        "one onion": "onion",
        "two onions": "onion",
        "cut onion": "onion",
        "cutonion": "onion",
        "one egg": "egg",
        "eggwhites": "egg white",

        # OCR artifact fixes - space-corrupted words
        "mayonnais e": "mayonnaise",
        "eg g yolks": "egg yolk",
        "eg g": "egg",
        "unsalt ed butter": "butter",
        "lemo n peel": "lemon zest",
        "lemo n": "lemon",
        "m iniature marshmallows": "miniature marshmallows",
        "bouillon c ube": "bouillon cube",
        "unsweet ened pineapple juice": "pineapple juice",
        "s. hard pears": "pear",
        "s. sugar": "sugar",
        "all-purpose ﬂour": "flour",
        "ﬂour": "flour",  # Wrong fl character
        "confectioners' sugar": "powdered sugar",
        "cutparsley": "parsley",
        "teaspoon salt": "salt",
        "teaspoons salt": "salt",
        "t salt": "salt",
        "of salt": "salt",
        "two teaspoons ofsalt": "salt",
        "two teaspoons ofbaking powder": "baking powder",
        "three offlour": "flour",
        "four tablespoons ofshortening": "shortening",

        # Unit embedded in item cleanup
        "c sugar": "sugar",
        "c flour": "flour",
        "c butter": "butter",
        "c water": "water",
        "c milk": "milk",
        "qts water": "water",

        # Additional cheese
        "sharp cheddar": "sharp cheddar cheese",
        "mild cheddar": "mild cheddar cheese",
        "monterey jack": "monterey jack cheese",
        "pepper jack": "pepper jack cheese",
        "extra sharp cheddar": "sharp cheddar cheese",

        # Additional common mappings
        "boneless": "chicken breast",
        "skinless": "chicken breast",
        "low-sodium chicken broth": "chicken broth",
        "reduced sodium chicken broth": "chicken broth",
        "fat-free": "skim milk",

        # Corn syrup
        "corn syrup": "light corn syrup",
        "karo syrup": "light corn syrup",
        "karo": "light corn syrup",

        # More synonyms from gap analysis
        "large ripe banana": "banana",
        "ripe banana": "banana",
        "ripe mango": "mango",
        "t water": "water",
        "t milk": "milk",
        "t sugar": "sugar",
        "t cornstarch": "cornstarch",
        "c celery": "celery",
        "c powdered sugar": "powdered sugar",
        "c powdere d sugar": "powdered sugar",
        "lb butter": "butter",
        "teaspoon nutmeg": "nutmeg",
        "teaspoon cinnamon": "cinnamon",
        "teaspoons cinnamon": "cinnamon",
        "can tomato sauce": "tomato sauce",
        "can mushrooms": "mushrooms",
        "jar apricot preserves": "apricot preserves",
        "mel ted butter": "butter",
        "parsl ey": "parsley",
        "chili flakes": "red pepper flakes",
        "% milk": "milk",
        "spices": "allspice",
        "flavoring": "vanilla extract",

        # Round 5 gap analysis synonyms
        "c walnuts": "walnuts",
        "c salad oil": "salad oil",
        "c lemo n juice": "lemon juice",
        "tbs flour": "flour",
        "mozzarella chees e": "mozzarella cheese",
        "d onion": "onion",
        "cutgreen peppers": "green pepper",
        "pulverized sugar": "powdered sugar",
        "teaspoon pepper": "pepper",
        "of pepper": "pepper",
        "t cold water": "water",
        "glass white wine": "dry white wine",
        "olive or vegetable oil": "olive oil",
        "margarine or butter": "butter",
        "cereals or muesli": "muesli",
        "two tablespoons ofbutter": "butter",
        "two tablespoonfuls ofsugar": "sugar",
        "four branches ofparsley": "parsley",
        "three tablespoons offinely minced parsley": "parsley",
        "two teaspoonfuls ofsalt": "salt",
        "one teaspoonful ofsalt": "salt",
        "two level tablespoons ofbaking powder": "baking powder",
        "three cupsofflour": "flour",
        "ofmilk": "milk",

        # Historical cookbook OCR artifacts
        "double-acting or 11/2 teaspoons cream tartar baking powder": "baking powder",
        "double-acting or 11/4 teaspoons cream tartar baking powder": "baking powder",
        "double-acting or 3 teaspoons cream tartar baking powder": "baking powder",
        "pastry for 2-crust": "pie crust",
        "cooked": "chicken",
        "meal": "cornmeal",

        # Round 6 synonyms
        "confectioners' sugar": "powdered sugar",
        "ugar": "sugar",
        "ugar;": "sugar",
        "cheddar": "cheddar cheese",
        "tablespoons butter": "butter",
        "vinegar or lemon juice": "vinegar",
        "c brown sugar": "brown sugar",
        "two ofsugar": "sugar",
        "and a half sugar": "sugar",
        "butter with two sugar": "butter",
        "three teaspoonfuls baking powder": "baking powder",
        "three tablespoons ofbaking powder": "baking powder",
        "four cupsofsifted flour": "flour",
        "two tablespoons ofshortening": "shortening",
        "to 4 flour": "flour",
        "juice 1 lemon": "lemon juice",
        "black molasses": "molasses",
        "no 2 can crushed pineapple": "crushed pineapple",
        "one 9-inch pie shell": "pie crust",
        "pastry for 9\" shell": "pie crust",
        "s stewing beef": "stewing beef",
        "miniature marshmallows or 20 regular marshmallows": "miniature marshmallows",
        "orange zest strips": "orange zest",
        "stove top stuffi ng": "stove top stuffing",

        # Round 8 synonyms - OCR artifacts
        "tblsp. flour": "flour",
        "tblsp. sugar": "sugar",
        "tblsp. vinegar": "vinegar",
        "tblsp flour": "flour",
        "tblsp sugar": "sugar",
        "t vanilla": "vanilla extract",
        "t. vanilla": "vanilla extract",
        "tsp. vanilla": "vanilla extract",
        "level tablespoonfuls of flour": "flour",
        "level tablespoons of flour": "flour",
        "level tablespoonfuls flour": "flour",
        "tablespoonfuls of flour": "flour",
        "tablespoons of flour": "flour",
        "tablespoons flour": "flour",
        "½ cups sugar": "sugar",
        "½ cups flour": "flour",
        "½ cup sugar": "sugar",
        "½ cup shortening": "shortening",
        "½ cup milk": "milk",
        "½ tsp. baking powder": "baking powder",
        "½ tsp. cloves": "cloves",
        "½ tsp baking powder": "baking powder",
        "¾ cup sugar": "sugar",

        # Rose water variants
        "rose-water": "rose water",
        "rosewater": "rose water",

        # Catsup/ketchup
        "catsup": "ketchup",

        # Corn variants
        "kernel corn": "corn",
        "corn kernels": "corn",
        "whole kernel corn": "corn",

        # Pimiento/pimento
        "pimento": "pimiento",
        "chopped pimiento": "pimiento",
        "chopped pimento": "pimiento",

        # Green items
        "green peppers": "green pepper",
        "green chiles, chopped": "green chiles",
        "(4 oz) green chiles, chopped": "green chiles",
        "green chiles chopped": "green chiles",
        "chopped green chiles": "green chiles",

        # Whole spices
        "whole cloves": "cloves",
        "whole allspice": "allspice",

        # Common plurals and variants
        "potatoes": "potato",
        "onions": "onion",
        "carrots": "carrot",
        "apples": "apple",
        "avocados": "avocado",
        "raisins": "raisins",
        "bread crumbs": "breadcrumbs",

        # Gelatin
        "envelope unflavored gelatin": "gelatin",
        "envelopes unflavored gelatin": "gelatin",
        "packet gelatin": "gelatin",

        # Wine
        "wine": "dry white wine",
        "white wine": "dry white wine",
        "red wine": "dry red wine",

        # Soy sauce
        "soy sauce": "soy sauce",

        # Mace
        "mace": "nutmeg",  # Similar flavor profile

        # Sliced variants
        "slices bacon": "bacon",
        "bacon slices": "bacon",

        # Water variants
        "boiling water": "water",
        "cold water": "water",
        "qts. water": "water",

        # Spice synonyms
        "white peppercorns": "peppercorns",
        "black peppercorns": "peppercorns",
        "coriander seeds": "coriander seed",
        "ground fennel seeds": "fennel seeds",
        "fennel seeds, crushed": "fennel seeds",
        "ground cayenne pepper": "cayenne",
        "ground cayenne": "cayenne",
        "pinch cayenne": "cayenne",
        "red pepper flakes": "crushed red pepper",
        "seasoning salt": "salt",

        # Panko/breadcrumbs
        "panko crumbs": "panko",
        "panko breadcrumbs": "panko",

        # Cheese synonyms
        "crumbled feta cheese": "feta cheese",
        "crumbled gorgonzola cheese": "gorgonzola",
        "crumbled feta": "feta cheese",
        "crumbled gorgonzola": "gorgonzola",
        "romano cheese": "parmesan cheese",
        "parmigiano-reggiano cheese": "parmesan cheese",
        "parmigiano-reggiano": "parmesan cheese",

        # Pasta synonyms
        "penne pasta": "pasta",
        "bucatini": "pasta",
        "uncooked penne pasta": "pasta",
        "uncooked bucatini": "pasta",

        # Brand name cleanup
        "campbell's condensed french onion soup": "onion soup",
        "pepperidge farm classic sandwich buns": "hamburger bun",
        "ocean spray jellied cranberry sauce": "cranberry sauce",
        "heinz chili sauce": "chili sauce",
        "bird's eye": "",

        # Ingredient with prep embedded (from insufficient recipes analysis)
        "large potato": "potato",
        "large potato, diced": "potato",
        "medium potato": "potato",
        "small potato": "potato",
        "top sirloin steak": "sirloin",
        "top sirloin": "sirloin",
        "ribeye steaks": "steak",
        "ribeye steak": "steak",
        "beef ribeye steaks": "steak",
        "hoagie rolls": "hoagie roll",
        "italian rolls": "italian roll",
        "sub rolls": "sub roll",
        "crusty italian rolls": "italian roll",

        # Cottage cheese variants
        "½ cups cottage cheese": "cottage cheese",
        "cups cottage cheese": "cottage cheese",

        # Cooked rice/noodles
        "cooked rice": "rice",
        "cooked noodles": "noodles",
        "fine noodles": "noodles",
        "½ cups cooked rice": "rice",
        "½ cups cooked rice or fine noodles": "rice",

        # Tomato variants
        "¼ cups tomato juice": "tomato juice",
        "cups tomato juice": "tomato juice",

        # Green chile variants
        "green chiles, chopped": "green chiles",
        "chopped green chiles": "green chiles",
        "diced green chiles": "green chiles",

        # Cherry variants
        "sour cherries": "cherries",
        "pitted sour cherries": "cherries",
        "pitted cherries": "cherries",
        "concord grapes": "grapes",

        # Pepper variants
        "poblano peppers": "poblano pepper",
        "anaheim peppers": "anaheim pepper",

        # OCR space-corruption patterns
        "c raspb erries": "raspberries",
        "raspb erries": "raspberries",
        "c sugar": "sugar",
        "c water": "water",
        "t cornstarch": "cornstarch",
        "t vanilla": "vanilla",
        "t baking powder": "baking powder",
        "t bakin g powder": "baking powder",
        "t lemon extrac t": "lemon extract",
        "lemon extrac t": "lemon extract",
        "c flour": "flour",
        "c peca ns": "pecans",
        "peca ns": "pecans",
        "t lem on peel": "lemon zest",
        "lem on peel": "lemon zest",
        "c brown sugar": "brown sugar",
        "m iniature marshmallows": "marshmallows",
        "mini ature marsh mallows": "marshmallows",
        "miniature marshmallows": "marshmallows",
        "chop ped walnuts": "walnuts",
        "all-purpos e flour": "flour",
        "all purpos e flour": "flour",
        "shorte ning": "shortening",
        "semi- sweet real chocolate": "chocolate chips",
        "semi-sweet real chocolate": "chocolate chips",

        # Ingredient with unit embedded (from Corn Relish analysis)
        "ears corn": "corn",
        "ears ofcorn": "corn",
        "ears of corn": "corn",
        "head cabbage": "cabbage",
        "medium head cabbage": "cabbage",
        "dry mustard": "mustard powder",
        "red peppers": "red pepper",
        "green peppers": "green pepper",

        # Gelatin variants
        "lime gelatin": "gelatin",
        "lemon gelatin": "gelatin",
        "orange gelatin": "gelatin",
        "strawberry gelatin": "gelatin",
        "unflavored gelatin": "gelatin",
        "plain gelatin": "gelatin",

        # More OCR patterns
        "ofvinegar": "vinegar",
        "pint ofvinegar": "vinegar",

        # Embedded size units (strip the descriptor)
        "oz mushrooms": "mushrooms",
        "mushrooms, sliced": "mushrooms",
        "sliced mushrooms": "mushrooms",

        # Shrimp variants (from batch 2 analysis)
        "large shrimp": "shrimp",
        "medium shrimp": "shrimp",
        "small shrimp": "shrimp",
        "jumbo shrimp": "shrimp",

        # Chipotle variants
        "chipotle pepper in adobo": "chipotle pepper",
        "chipotle peppers in adobo": "chipotle pepper",
        "chipotle in adobo": "chipotle pepper",
        "chipotles in adobo": "chipotle pepper",

        # Salsa variants
        "chunky salsa": "salsa",
        "mild salsa": "salsa",
        "hot salsa": "salsa",
        "medium salsa": "salsa",

        # Pimiento variants
        "diced pimiento": "pimiento",
        "chopped pimiento": "pimiento",
        "jarred pimiento": "pimiento",

        # Walnut variants
        "black walnuts": "walnuts",
        "chopped black walnuts": "walnuts",
        "english walnuts": "walnuts",

        # Corn syrup variants
        "dark corn syrup": "corn syrup",
        "light corn syrup": "corn syrup",

        # Cold/cooked variants
        "cold chicken": "chicken",
        "cooked chicken": "chicken",
        "cooked cubed chicken": "chicken",

        # Wild rice variants
        "uncle ben's wild rice": "wild rice",
        "wild rice mix": "wild rice",

        # Water chestnuts variants
        "sliced water chestnuts": "water chestnuts",
        "canned water chestnuts": "water chestnuts",

        # Peeled/sliced variants
        "peeled jicama": "jicama",
        "julienne-cut peeled jicama": "jicama",
        "sliced peeled ripe mango": "mango",
        "peeled ripe mango": "mango",

        # Celery soup
        "cream of celery soup": "cream of chicken soup",
        "celery soup": "cream of chicken soup",

        # French green beans
        "french green beans": "green beans",
        "french cut green beans": "green beans",

        # Rhubarb
        "stewed rhubarb": "rhubarb",

        # Brand names
        "carnation milk": "evaporated milk",

        # Batch 3 analysis - OCR space-corrupted patterns
        "garl ic powder": "garlic powder",
        "garl ic": "garlic",
        "papri ka": "paprika",
        "alls pice": "allspice",
        "cocktai l": "cocktail",
        "conv erted": "converted",

        # Batch 3 analysis - historical ingredient names
        "calf's liver": "liver",
        "calfs liver": "liver",
        "beef liver": "liver",
        "fryer": "chicken",
        "fryer in pieces": "chicken",
        "frying chicken": "chicken",

        # Hard-cooked eggs
        "hard-cooked egg": "egg",
        "hard-cooked large egg": "egg",
        "hard boiled egg": "egg",
        "hard-boiled egg": "egg",

        # Crispy rice cereal
        "crispy rice cereal": "rice krispies",
        "cups crispy rice cereal": "rice krispies",
        "cups cups crispy rice cereal": "rice krispies",

        # Barley variants
        "pearled barley": "barley",
        "pearl barley": "barley",

        # Biscuit dough
        "biscuit dough": "biscuit",

        # Cakes yeast (historical format)
        "cakes yeast": "yeast",
        "cake yeast": "yeast",

        # Sauce variants
        "spaghetti sauce with mushrooms": "spaghetti sauce",
        "spaghetti sauce": "marinara sauce",
        "stewed tomato bits": "stewed tomatoes",

        # Cheese variants
        "ricotta salata cheese": "ricotta cheese",
        "ricotta salata": "ricotta cheese",
        "freshly crumbled ricotta salata cheese": "ricotta cheese",

        # Plum tomato
        "plum tomato": "tomato",
        "sliced plum tomato": "tomato",

        # Dutch-process cocoa
        "dutch-process cocoa powder": "cocoa powder",

        # Malted milk
        "malted milk powder": "malted milk",

        # Half-and-half variants
        "half-and-half": "half and half",

        # Olives
        "niçoise olives": "olives",
        "nicoise olives": "olives",
        "pitted niçoise olives": "olives",
        "pitted nicoise olives": "olives",
        "chopped pitted niçoise olives": "olives",
        "chopped pitted nicoise olives": "olives",

        # Basil variants
        "sliced fresh basil": "basil",
        "thinly sliced fresh basil": "basil",
        "torn basil leaves": "basil",
        "fresh basil leaves": "basil",

        # Mint variants
        "mint leaves": "mint",
        "torn mint leaves": "mint",
        "mint sprigs": "mint",

        # Sardinian bread (specialty, use crackers equiv)
        "pane carasau": "crackers",
        "sardinian music bread": "crackers",
        "sheets pane carasau": "crackers",

        # Browning sauce (negligible calories)
        "bottled browning sauce": "browning sauce",
        "kitchen bouquet": "browning sauce",

        # Whole wheat baguette
        "whole-wheat french bread baguette": "french bread",
        "whole wheat french bread baguette": "french bread",

        # Rice vinegar
        "rice wine vinegar": "rice vinegar",

        # Ginger slices
        "slice ginger": "fresh ginger",
        "inch slice ginger": "fresh ginger",
        "slices ginger": "fresh ginger",

        # Batch 4 analysis - OCR space-corrupted patterns
        "chick en": "chicken",
        "chick en breast": "chicken breast",
        "slice d": "sliced",
        "slice d mushrooms": "mushrooms",
        "pounded chick en breast": "chicken breast",

        # Batch 4 - historical/archaic ingredient names
        "yellow corn meal": "cornmeal",
        "sour milk": "buttermilk",
        "sweet milk or buttermilk": "buttermilk",
        "sour milk or buttermilk": "buttermilk",
        "naples biscuit": "ladyfinger",
        "naples biscuits": "ladyfinger",
        "fine loaf crumbs": "breadcrumbs",
        "seville oranges": "orange",
        "seville orange": "orange",
        "orange water": "orange extract",
        "rose water": "rose water",
        "races of ginger": "ginger",
        "saltpork": "salt pork",
        "salt pork": "salt pork",
        "beef tips": "beef stew meat",

        # Batch 4 - spice variants
        "sichuan peppercorns": "sichuan peppercorns",
        "szechuan peppercorns": "sichuan peppercorns",
        "regular peppercorns": "peppercorns",
        "white pepper corns": "peppercorns",

        # Batch 4 - cheese variants
        "slices swiss cheese": "swiss cheese",
        "swiss cheese slices": "swiss cheese",

        # Batch 4 - cherry variants
        "bing cherries": "cherries",
        "no. 2½ can bing cherries": "cherries",
        "cherry-flavored gelatin": "gelatin",

        # Batch 4 - stuffed olives
        "stuffed olives": "olives",
        "bottle stuffed olives": "olives",

        # Batch 4 - mixed herbs
        "mixed fresh herbs": "fresh herbs",
        "fresh herbs": "parsley",

        # Batch 4 - brand names
        "carnation": "evaporated milk",
        "carnation milk": "evaporated milk",
        "wesson oil": "vegetable oil",
        "grandma's molasses": "molasses",

        # Batch 4 - package/envelope normalization
        "unflavored gelatin": "gelatin",
        "envelopes unflavored gelatin": "gelatin",
        "1-oz instant oatmeal packet": "instant oatmeal",
        "instant oatmeal packet plain": "instant oatmeal",
        "instant oatmeal packets plain": "instant oatmeal",

        # Batch 4 - frozen vegetables
        "frozen pepper stir-fry": "mixed vegetables",
        "pepper stir-fry": "mixed vegetables",

        # Batch 4 - baby food (negligible calories for marinades)
        "baby juice": "apple juice",
        "baby food peaches": "peaches",
        "jars baby juice": "apple juice",
        "jars baby food peaches": "peaches",

        # Batch 4 manual repairs - additional patterns found
        "chopped red skinned apples": "apple",
        "red skinned apples": "apple",
        "green onion tops": "green onion",
        "finely chopped green onion tops": "green onion",
        "broken pecans": "pecans",
        "broken pecan meats": "pecans",
        "pecan meats": "pecans",
        "mixed stuffing": "stuffing mix",
        "savory deep dish pie crust": "pie crust",
        "deep dish pie crust": "pie crust",
        "half and half cream": "half and half",
        "cumin seeds": "cumin",
        "fine sugar": "sugar",
        "moist shredded coconut": "coconut",
        "moist": "coconut",
        "shredded coconut": "coconut",
        "one clove": "garlic",

        # Batch 5 manual repairs
        "stewing hen": "chicken",
        "rivels": "egg noodles",
        "zwieback": "crackers",
        "broccoli rabe": "broccoli",
        "chili flakes": "red pepper flakes",
        "anchovies": "fish",
        "tuna steaks": "tuna",
        "yellowfin tuna steaks": "tuna",
        "yellowfin tuna": "tuna",
        "napa cabbage": "cabbage",
        "chinese cabbage": "cabbage",
        "fish broth": "chicken broth",
        "crisp rice cereal": "rice krispies",
        "rice krispies": "puffed rice",
        "rose water": "vanilla extract",
        "rose-water": "vanilla extract",
        "granulated gelatin": "unflavored gelatin",
        "fruit juice": "orange juice",
        "fruit pulp": "applesauce",
        "salsa verde": "salsa",
        "fire-roasted salsa verde": "salsa",
        "fire-roasted salsa": "salsa",
        "pizza dough": "bread dough",
        "matchstick-cut carrots": "carrots",
        "presliced red onion": "red onion",
        "chili seasoning mix": "chili powder",
        "bouillon cubes": "bouillon",
        "beef bouillon cubes": "bouillon",
        "chicken bouillon cubes": "bouillon",
        "ground turkey breast": "ground turkey",

        # Batch 6 manual repairs
        "venison": "beef",
        "condensed mushroom soup": "cream of mushroom soup",
        "french onion soup": "onion soup",
        "salad dressing": "mayonnaise",
        "chopped sweet pickle": "sweet pickle relish",
        "dark molasses": "molasses",
        "mel ted margari ne": "margarine",
        "melted margarine": "margarine",
        "double crust": "pie crust",
        "lard": "shortening",
        "alum": "cream of tartar",
        "corned beef brisket": "corned beef",
        "dijon mustard": "mustard",
        "orange marmalade": "orange jam",
        "mashed potatoes": "potatoes",
        "bread dough": "yeast dough",
        "sherry": "white wine",
        "chinese rice wine": "white wine",
        "dry sherry": "white wine",
        "orange zest strips": "orange zest",
        "pearled barley": "barley",
        "anaheim chile peppers": "green chiles",
        "anaheim chiles": "green chiles",
        "melba toast crumbs": "bread crumbs",
        "apple butter": "applesauce",
        "peach syrup": "simple syrup",
        "white sauce": "bechamel sauce",
        "petite diced tomatoes": "diced tomatoes",
        "mild chili beans": "chili beans",
        "mild chili seasoning mix": "chili powder",
        "canned peaches": "peaches",

        # Batch 7 manual repairs
        "strawberry syrup": "simple syrup",
        "maraschino cherries": "cherries",
        "reserved chicken cooking liquid": "chicken broth",
        "chicken cooking liquid": "chicken broth",
        "slivered almonds": "almonds",
        "franks": "hot dogs",
        "cooked franks": "hot dogs",
        "corn tortillas": "tortillas",
        "grated pineapple": "pineapple",
        "roquefort cheese": "blue cheese",
        "roquefort": "blue cheese",
        "firm tofu": "tofu",
        "gai lan": "broccoli",
        "chinese broccoli": "broccoli",
        "uncle ben's": "",
        "converted brand rice": "rice",
        "caramel ice cream topping": "caramel sauce",
        "baker's semi-sweet chocolate": "semi-sweet chocolate",
        "cool whip whipped topping": "whipped cream",
        "cool whip": "whipped cream",
        "nilla wafer pie crust": "pie crust",
        "philadelphia cream cheese": "cream cheese",
        "sweet milk": "milk",
        "custard": "vanilla pudding",
        "thin custard": "vanilla pudding",
        "muenster": "cheese",
        "gouda cheese": "cheese",
        "muenster cheese": "cheese",
        "wild mushrooms": "mushrooms",
        "fregula": "couscous",
        "abbamele": "honey",
        "pastry flour": "flour",
        "cold fat": "shortening",
        "lavender": "vanilla extract",
        "dried lavender": "vanilla extract",
        "culinary lavender": "vanilla extract",
        "dandelion greens": "spinach",
        "young dandelion greens": "spinach",
        "oysters": "clams",
        "green tomatoes": "tomatoes",
        "celery seed": "celery salt",
        "mustard seed": "dry mustard",

        # Batch 8 manual repairs
        "anasazi beans": "pinto beans",
        "black forest ham": "ham",
        "smoked mozzarella": "mozzarella",
        "chicken cutlets": "chicken breast",
        "pearl ash": "baking soda",
        "double refined sugar": "sugar",
        "sweetest cream": "heavy cream",
        "cakes yeast": "yeast",
        "pot pie dough": "pie crust",
        "almond paste": "marzipan",
        "marzipan": "almonds",
        "apricot nectar": "apricot juice",
        "sriracha": "hot sauce",
        "sweet marjoram": "marjoram",
        "mace": "nutmeg",
        "mutton": "lamb",
        "jicama": "water chestnuts",
        "instant spanish rice": "rice",
        "picante sauce": "salsa",
        "colliflowers": "cauliflower",
        "fresh chives": "chives",
        "whole wheat pastry flour": "whole wheat flour",
        "wheat bran": "bran",
        "fat": "butter",
        "breakfast sausage": "sausage",
        "frozen pizza dough": "pizza dough",
        "biscuit mix": "bisquick",
        "bisquick": "flour",
        "pancake mix": "flour",
        "instant rice": "rice",

        # Batch 9: Synonyms from GrandmasRecipes script
        # Poultry variants
        "boneless chicken": "chicken breast",
        "boneless skinless chicken": "chicken breast",
        "chicken breast halves": "chicken breast",
        "boneless skinless chicken breast halves": "chicken breast",
        "chicken breast half": "chicken breast",
        "bone-in chicken": "chicken thighs",
        "chicken pieces": "chicken thighs",
        "cornish hen": "chicken",
        "cornish game hen": "chicken",
        "game hen": "chicken",
        "rock cornish hen": "chicken",
        "capon": "chicken",
        "rotisserie chicken": "chicken",
        "cooked chicken": "chicken breast",
        "leftover chicken": "chicken breast",
        "shredded chicken": "chicken breast",
        "diced chicken": "chicken breast",
        "cubed chicken": "chicken breast",

        # Sausage variants
        "andouille sausage": "sausage",
        "andouille": "sausage",
        "kielbasa": "sausage",
        "polish sausage": "sausage",
        "italian sausage links": "italian sausage",
        "hot italian sausage": "italian sausage",
        "mild italian sausage": "italian sausage",
        "sweet italian sausage": "italian sausage",
        "breakfast sausage links": "sausage",
        "sausage patties": "sausage",
        "pork sausage": "sausage",
        "turkey sausage": "sausage",
        "chicken sausage": "sausage",
        "smoked sausage": "sausage",
        "chorizo sausage": "chorizo",

        # Other meats
        "chuck roast": "beef roast",
        "pot roast": "beef roast",
        "eye of round": "beef roast",
        "rump roast": "beef roast",
        "sirloin roast": "beef roast",
        "top round": "beef roast",
        "bottom round": "beef roast",
        "brisket": "beef roast",
        "beef brisket": "beef roast",
        "corned beef brisket": "corned beef",
        "short ribs": "beef ribs",
        "beef short ribs": "beef ribs",
        "beef stew meat": "beef",
        "stew meat": "beef",
        "cubed beef": "beef",
        "london broil": "flank steak",
        "skirt steak": "flank steak",
        "hanger steak": "flank steak",
        "flat iron steak": "beef steak",
        "ribeye": "beef steak",
        "rib eye": "beef steak",
        "new york strip": "beef steak",
        "strip steak": "beef steak",
        "filet mignon": "beef tenderloin",
        "beef filet": "beef tenderloin",
        "tenderloin steak": "beef tenderloin",
        "tri-tip": "beef roast",
        "tri tip": "beef roast",

        # Pork variants
        "pork tenderloin": "pork loin",
        "pork roast": "pork loin",
        "pork shoulder": "pork",
        "pork butt": "pork",
        "boston butt": "pork",
        "pulled pork": "pork",
        "pork cutlets": "pork chops",
        "boneless pork chops": "pork chops",
        "bone-in pork chops": "pork chops",
        "thick-cut pork chops": "pork chops",
        "center-cut pork chops": "pork chops",
        "pork ribs": "pork",
        "baby back ribs": "pork",
        "spare ribs": "pork",
        "st louis ribs": "pork",
        "country-style ribs": "pork",

        # Seafood variants
        "cod fillets": "cod",
        "cod fillet": "cod",
        "haddock": "cod",
        "pollock": "cod",
        "halibut": "cod",
        "halibut fillet": "cod",
        "tilapia": "white fish",
        "tilapia fillets": "white fish",
        "swai": "white fish",
        "catfish fillets": "catfish",
        "salmon fillets": "salmon",
        "salmon fillet": "salmon",
        "sockeye salmon": "salmon",
        "atlantic salmon": "salmon",
        "wild salmon": "salmon",
        "smoked salmon": "salmon",
        "lox": "salmon",
        "trout": "salmon",
        "rainbow trout": "salmon",
        "steelhead": "salmon",
        "tuna steaks": "tuna",
        "ahi tuna": "tuna",
        "yellowfin tuna": "tuna",
        "swordfish": "tuna",
        "mahi mahi": "white fish",
        "mahi-mahi": "white fish",
        "sea bass": "white fish",
        "grouper": "white fish",
        "snapper": "white fish",
        "red snapper": "white fish",
        "flounder": "white fish",
        "sole": "white fish",

        # Shellfish
        "jumbo shrimp": "shrimp",
        "large shrimp": "shrimp",
        "medium shrimp": "shrimp",
        "small shrimp": "shrimp",
        "tiger shrimp": "shrimp",
        "gulf shrimp": "shrimp",
        "bay shrimp": "shrimp",
        "rock shrimp": "shrimp",
        "prawns": "shrimp",
        "langostino": "shrimp",
        "crawfish": "shrimp",
        "crayfish": "shrimp",
        "lobster tail": "lobster",
        "lobster tails": "lobster",
        "sea scallops": "scallops",
        "bay scallops": "scallops",
        "littleneck clams": "clams",
        "cherrystone clams": "clams",
        "manila clams": "clams",
        "razor clams": "clams",
        "mussels": "clams",
        "oysters": "clams",

        # Grain variants
        "polenta": "cornmeal",
        "instant polenta": "cornmeal",
        "coarse cornmeal": "cornmeal",
        "fine cornmeal": "cornmeal",
        "corn grits": "grits",
        "hominy grits": "grits",
        "instant grits": "grits",
        "stone-ground grits": "grits",
        "quinoa": "rice",
        "red quinoa": "rice",
        "white quinoa": "rice",
        "tri-color quinoa": "rice",
        "bulgur": "barley",
        "bulgur wheat": "barley",
        "cracked wheat": "barley",
        "farro": "barley",
        "freekeh": "barley",
        "wheat berries": "barley",
        "spelt": "barley",
        "kamut": "barley",
        "millet": "rice",
        "amaranth": "rice",
        "teff": "rice",
        "sorghum": "rice",
        "buckwheat": "oats",
        "buckwheat groats": "oats",
        "kasha": "oats",
        "steel-cut oats": "oats",
        "rolled oats": "oats",
        "old-fashioned oats": "oats",
        "quick oats": "oats",
        "instant oatmeal": "oats",
        "oat bran": "oats",

        # Bean variants
        "navy beans": "beans",
        "great northern beans": "beans",
        "cannellini beans": "beans",
        "white beans": "beans",
        "small white beans": "beans",
        "butter beans": "lima beans",
        "baby lima beans": "lima beans",
        "large lima beans": "lima beans",
        "flageolet beans": "beans",
        "cranberry beans": "pinto beans",
        "roman beans": "pinto beans",
        "borlotti beans": "pinto beans",
        "red beans": "kidney beans",
        "small red beans": "kidney beans",
        "dark red kidney beans": "kidney beans",
        "light red kidney beans": "kidney beans",
        "pink beans": "pinto beans",
        "black turtle beans": "black beans",
        "frijoles negros": "black beans",
        "black-eyed peas": "black eyed peas",
        "cowpeas": "black eyed peas",
        "field peas": "black eyed peas",
        "crowder peas": "black eyed peas",
        "split peas": "lentils",
        "green split peas": "lentils",
        "yellow split peas": "lentils",
        "red lentils": "lentils",
        "green lentils": "lentils",
        "brown lentils": "lentils",
        "french lentils": "lentils",
        "du puy lentils": "lentils",
        "beluga lentils": "lentils",

        # Pasta variants
        "rotini": "pasta",
        "fusilli": "pasta",
        "penne": "pasta",
        "penne rigate": "pasta",
        "rigatoni": "pasta",
        "ziti": "pasta",
        "mostaccioli": "pasta",
        "farfalle": "pasta",
        "bow tie pasta": "pasta",
        "bowtie pasta": "pasta",
        "bow ties": "pasta",
        "orecchiette": "pasta",
        "cavatappi": "pasta",
        "gemelli": "pasta",
        "campanelle": "pasta",
        "radiatore": "pasta",
        "wagon wheels": "pasta",
        "rotelle": "pasta",
        "shells": "pasta",
        "medium shells": "pasta",
        "large shells": "pasta",
        "jumbo shells": "pasta",
        "conchiglie": "pasta",
        "elbows": "macaroni",
        "elbow pasta": "macaroni",
        "elbow macaroni": "macaroni",
        "ditalini": "macaroni",
        "tubetti": "macaroni",
        "orzo": "pasta",
        "acini di pepe": "pasta",
        "pastina": "pasta",
        "stelline": "pasta",
        "alphabets": "pasta",
        "couscous": "pasta",
        "israeli couscous": "pasta",
        "pearl couscous": "pasta",
        "spaghetti": "pasta",
        "thin spaghetti": "pasta",
        "spaghettini": "pasta",
        "angel hair": "pasta",
        "capellini": "pasta",
        "linguine": "pasta",
        "fettuccine": "pasta",
        "tagliatelle": "pasta",
        "pappardelle": "pasta",
        "bucatini": "pasta",
        "perciatelli": "pasta",
        "vermicelli": "pasta",
        "lasagna noodles": "pasta",
        "lasagne": "pasta",
        "manicotti": "pasta",
        "cannelloni": "pasta",
        "egg noodles": "pasta",
        "wide egg noodles": "pasta",
        "extra wide egg noodles": "pasta",
        "kluski noodles": "pasta",
        "no-boil lasagna": "pasta",
        "oven-ready lasagna": "pasta",
        "rice noodles": "pasta",
        "pad thai noodles": "pasta",
        "lo mein noodles": "pasta",
        "ramen noodles": "pasta",
        "udon noodles": "pasta",
        "soba noodles": "pasta",
        "rice vermicelli": "pasta",
        "cellophane noodles": "pasta",
        "glass noodles": "pasta",
        "bean thread noodles": "pasta",

        # Vegetable variants
        "scallions": "green onions",
        "green onion": "green onions",
        "spring onions": "green onions",
        "collard greens": "spinach",
        "collards": "spinach",
        "mustard greens": "spinach",
        "turnip greens": "spinach",
        "beet greens": "spinach",
        "swiss chard": "spinach",
        "chard": "spinach",
        "rainbow chard": "spinach",
        "escarole": "spinach",
        "endive": "spinach",
        "belgian endive": "lettuce",
        "radicchio": "lettuce",
        "frisee": "lettuce",
        "arugula": "spinach",
        "rocket": "spinach",
        "watercress": "spinach",
        "baby spinach": "spinach",
        "baby kale": "kale",
        "lacinato kale": "kale",
        "tuscan kale": "kale",
        "curly kale": "kale",
        "dinosaur kale": "kale",
        "artichoke hearts": "asparagus",
        "artichokes": "asparagus",
        "hearts of palm": "asparagus",
        "palm hearts": "asparagus",
        "okra": "green beans",
        "jicama": "water chestnuts",
        "daikon": "radishes",
        "daikon radish": "radishes",
        "turnips": "potatoes",
        "rutabaga": "potatoes",
        "parsnips": "carrots",
        "celeriac": "celery",
        "celery root": "celery",
        "fennel bulb": "celery",
        "fennel": "celery",
        "kohlrabi": "cabbage",
        "bok choy": "cabbage",
        "baby bok choy": "cabbage",
        "napa cabbage": "cabbage",
        "chinese cabbage": "cabbage",
        "savoy cabbage": "cabbage",
        "red cabbage": "cabbage",
        "green cabbage": "cabbage",
        "brussels sprouts": "broccoli",
        "broccolini": "broccoli",
        "broccoli rabe": "broccoli",
        "rapini": "broccoli",
        "broccoli florets": "broccoli",
        "cauliflower florets": "cauliflower",
        "romanesco": "cauliflower",

        # Squash variants
        "butternut squash": "squash",
        "acorn squash": "squash",
        "spaghetti squash": "squash",
        "delicata squash": "squash",
        "kabocha squash": "squash",
        "hubbard squash": "squash",
        "winter squash": "squash",
        "summer squash": "zucchini",
        "yellow squash": "zucchini",
        "crookneck squash": "zucchini",
        "pattypan squash": "zucchini",
        "chayote": "zucchini",

        # Pepper variants
        "bell pepper": "green pepper",
        "bell peppers": "green pepper",
        "red bell pepper": "red pepper",
        "yellow bell pepper": "green pepper",
        "orange bell pepper": "green pepper",
        "sweet pepper": "green pepper",
        "sweet peppers": "green pepper",
        "cubanelle pepper": "green pepper",
        "banana pepper": "green pepper",
        "pepperoncini": "green pepper",
        "pimento": "red pepper",
        "pimientos": "red pepper",
        "roasted red peppers": "red pepper",
        "jarred roasted peppers": "red pepper",
        "jalapeno pepper": "jalapeno",
        "jalapeno peppers": "jalapeno",
        "serrano pepper": "jalapeno",
        "serrano peppers": "jalapeno",
        "fresno pepper": "jalapeno",
        "poblano pepper": "green chilies",
        "poblano peppers": "green chilies",
        "anaheim pepper": "green chilies",
        "anaheim peppers": "green chilies",
        "hatch chiles": "green chilies",
        "pasilla pepper": "green chilies",
        "ancho chile": "green chilies",
        "guajillo chile": "green chilies",
        "chipotle pepper": "chipotle",
        "habanero": "jalapeno",
        "habanero pepper": "jalapeno",
        "scotch bonnet": "jalapeno",
        "thai chili": "jalapeno",
        "thai chilies": "jalapeno",
        "bird's eye chili": "jalapeno",

        # Mushroom variants
        "cremini mushrooms": "mushrooms",
        "cremini": "mushrooms",
        "baby bella mushrooms": "mushrooms",
        "baby bellas": "mushrooms",
        "button mushrooms": "mushrooms",
        "white mushrooms": "mushrooms",
        "portobello mushrooms": "mushrooms",
        "portobello": "mushrooms",
        "portabella": "mushrooms",
        "portobella": "mushrooms",
        "shiitake mushrooms": "mushrooms",
        "shiitake": "mushrooms",
        "oyster mushrooms": "mushrooms",
        "chanterelle mushrooms": "mushrooms",
        "chanterelles": "mushrooms",
        "porcini mushrooms": "mushrooms",
        "porcini": "mushrooms",
        "morel mushrooms": "mushrooms",
        "morels": "mushrooms",
        "enoki mushrooms": "mushrooms",
        "king trumpet mushrooms": "mushrooms",
        "maitake mushrooms": "mushrooms",
        "hen of the woods": "mushrooms",
        "dried mushrooms": "mushrooms",
        "dried porcini": "mushrooms",
        "dried shiitake": "mushrooms",
        "mushroom caps": "mushrooms",
        "sliced mushrooms": "mushrooms",

        # Tomato variants
        "roma tomatoes": "tomatoes",
        "plum tomatoes": "tomatoes",
        "grape tomatoes": "tomatoes",
        "cherry tomatoes": "tomatoes",
        "beefsteak tomatoes": "tomatoes",
        "heirloom tomatoes": "tomatoes",
        "vine-ripened tomatoes": "tomatoes",
        "campari tomatoes": "tomatoes",
        "san marzano tomatoes": "canned tomatoes",
        "fire-roasted tomatoes": "canned tomatoes",
        "fire roasted tomatoes": "canned tomatoes",
        "petite diced tomatoes": "canned tomatoes",
        "stewed tomatoes": "canned tomatoes",
        "crushed tomatoes": "canned tomatoes",
        "tomato puree": "tomato sauce",
        "tomato passata": "tomato sauce",
        "marinara sauce": "tomato sauce",
        "pizza sauce": "tomato sauce",
        "sun-dried tomato paste": "tomato paste",
        "double-concentrated tomato paste": "tomato paste",

        # Onion variants
        "yellow onion": "onion",
        "white onion": "onion",
        "red onion": "onion",
        "sweet onion": "onion",
        "vidalia onion": "onion",
        "walla walla onion": "onion",
        "maui onion": "onion",
        "spanish onion": "onion",
        "bermuda onion": "onion",
        "pearl onions": "onion",
        "cipollini onions": "onion",
        "boiling onions": "onion",
        "shallots": "onion",
        "shallot": "onion",
        "leeks": "onion",
        "leek": "onion",
        "ramps": "onion",
        "chives": "green onions",

        # Cheese variants
        "sharp cheddar": "cheddar cheese",
        "mild cheddar": "cheddar cheese",
        "medium cheddar": "cheddar cheese",
        "extra sharp cheddar": "cheddar cheese",
        "white cheddar": "cheddar cheese",
        "aged cheddar": "cheddar cheese",
        "colby cheese": "cheddar cheese",
        "colby jack": "cheddar cheese",
        "monterey jack cheese": "jack cheese",
        "pepper jack cheese": "jack cheese",
        "pepper jack": "jack cheese",
        "queso fresco": "feta cheese",
        "cotija cheese": "parmesan cheese",
        "cotija": "parmesan cheese",
        "pecorino romano": "parmesan cheese",
        "pecorino": "parmesan cheese",
        "asiago cheese": "parmesan cheese",
        "asiago": "parmesan cheese",
        "grana padano": "parmesan cheese",
        "parmigiano-reggiano": "parmesan cheese",
        "parmigiano reggiano": "parmesan cheese",
        "gruyere cheese": "swiss cheese",
        "gruyere": "swiss cheese",
        "emmental": "swiss cheese",
        "emmentaler": "swiss cheese",
        "jarlsberg": "swiss cheese",
        "fontina cheese": "swiss cheese",
        "fontina": "swiss cheese",
        "provolone cheese": "provolone",
        "smoked provolone": "provolone",
        "havarti cheese": "swiss cheese",
        "havarti": "swiss cheese",
        "gouda cheese": "swiss cheese",
        "gouda": "swiss cheese",
        "smoked gouda": "swiss cheese",
        "edam": "swiss cheese",
        "manchego": "swiss cheese",
        "muenster cheese": "swiss cheese",
        "muenster": "swiss cheese",
        "brie cheese": "brie",
        "camembert": "brie",
        "boursin": "cream cheese",
        "neufchatel": "cream cheese",
        "mascarpone cheese": "cream cheese",
        "mascarpone": "cream cheese",
        "ricotta cheese": "ricotta",
        "part-skim ricotta": "ricotta",
        "whole milk ricotta": "ricotta",
        "fresh mozzarella": "mozzarella",
        "buffalo mozzarella": "mozzarella",
        "mozzarella pearls": "mozzarella",
        "bocconcini": "mozzarella",
        "burrata": "mozzarella",
        "string cheese": "mozzarella",
        "crumbled feta": "feta cheese",
        "crumbled blue cheese": "blue cheese",
        "crumbled gorgonzola": "blue cheese",
        "gorgonzola": "blue cheese",
        "roquefort": "blue cheese",
        "stilton": "blue cheese",
        "danish blue": "blue cheese",
        "maytag blue": "blue cheese",

        # Batch 10: Specialty and prepared ingredients
        # Indian ingredients
        "indian puffed rice": "rice",
        "puffed rice": "rice",
        "sev": "noodles",
        "fine indian noodles": "noodles",
        "tamarind-date chutney": "jam",
        "tamarind chutney": "jam",
        "date chutney": "jam",
        "mint chutney": "jam",
        "cilantro chutney": "jam",
        "mango chutney": "jam",
        "serrano chile": "jalapeno",
        "serrano chiles": "jalapeno",
        "semolina": "flour",
        "pasta flour": "flour",
        "semolina flour": "flour",
        "durum flour": "flour",
        "00 flour": "flour",

        # Prepared/packaged items
        "container prepared hummus": "hummus",
        "prepared hummus": "hummus",
        "store-bought hummus": "hummus",
        "iceberg lettuce": "lettuce",
        "romaine lettuce": "lettuce",
        "boston lettuce": "lettuce",
        "bibb lettuce": "lettuce",
        "butter lettuce": "lettuce",
        "red leaf lettuce": "lettuce",
        "green leaf lettuce": "lettuce",
        "mixed greens": "lettuce",
        "spring mix": "lettuce",
        "salad mix": "lettuce",
        "container crumbled feta cheese": "feta cheese",
        "container feta": "feta cheese",
        "packages sliced smoked salmon": "salmon",
        "sliced smoked salmon": "salmon",
        "smoked salmon slices": "salmon",
        "packages pie dough mix": "pie crust",
        "pie dough mix": "pie crust",
        "refrigerated pie crust": "pie crust",
        "frozen pie crust": "pie crust",
        "pie dough": "pie crust",
        "puff pastry sheets": "pie crust",
        "puff pastry": "pie crust",
        "phyllo dough": "pie crust",
        "filo dough": "pie crust",
        "can white chicken meat": "chicken breast",
        "canned chicken": "chicken breast",
        "canned chicken breast": "chicken breast",
        "shredded rotisserie chicken": "chicken breast",
        "can sliced ripe olives": "olives",
        "sliced ripe olives": "olives",
        "sliced black olives": "olives",
        "pitted olives": "olives",
        "kalamata olives": "olives",
        "green olives": "olives",
        "stuffed olives": "olives",
        "shredded mexican cheese blend": "cheddar cheese",
        "mexican cheese blend": "cheddar cheese",
        "mexican blend cheese": "cheddar cheese",
        "taco cheese": "cheddar cheese",
        "fiesta blend cheese": "cheddar cheese",

        # Bread varieties
        "baguette": "french bread",
        "french baguette": "french bread",
        "italian bread": "french bread",
        "ciabatta": "french bread",
        "focaccia": "french bread",
        "pumpernickel bread": "rye bread",
        "pumpernickel": "rye bread",
        "dark rye": "rye bread",
        "marble rye": "rye bread",
        "sourdough bread": "bread",
        "sourdough": "bread",
        "brioche": "bread",
        "challah": "bread",
        "english muffins": "bread",
        "english muffin": "bread",
        "bagels": "bread",
        "bagel": "bread",
        "croissants": "bread",
        "croissant": "bread",
        "pita bread": "bread",
        "naan": "bread",
        "naan bread": "bread",
        "flatbread": "bread",
        "tortilla chips": "chips",
        "corn chips": "chips",
        "pita chips": "chips",

        # Nuts and dried fruit
        "candied pecans": "pecans",
        "glazed pecans": "pecans",
        "praline pecans": "pecans",
        "candied walnuts": "walnuts",
        "glazed walnuts": "walnuts",
        "candied almonds": "almonds",
        "sliced almonds": "almonds",
        "slivered almonds": "almonds",
        "blanched almonds": "almonds",
        "marcona almonds": "almonds",
        "roasted almonds": "almonds",
        "dry-roasted peanuts": "peanuts",
        "roasted peanuts": "peanuts",
        "honey roasted peanuts": "peanuts",
        "cocktail peanuts": "peanuts",
        "chopped peanuts": "peanuts",
        "pine nuts": "almonds",
        "pignoli": "almonds",
        "pistachios": "almonds",
        "pistachio": "almonds",
        "macadamia nuts": "almonds",
        "macadamias": "almonds",
        "hazelnuts": "almonds",
        "filberts": "almonds",
        "chestnuts": "almonds",
        "cashews": "almonds",
        "cashew pieces": "almonds",
        "mixed nuts": "almonds",

        # Canned fruits
        "cans sliced pears": "pears",
        "canned pears": "pears",
        "sliced pears": "pears",
        "canned peaches": "peaches",
        "sliced peaches": "peaches",
        "canned fruit cocktail": "mixed fruit",
        "fruit cocktail": "mixed fruit",
        "canned mandarin oranges": "oranges",
        "mandarin oranges": "oranges",
        "canned pineapple": "pineapple",
        "crushed pineapple": "pineapple",
        "pineapple chunks": "pineapple",
        "pineapple tidbits": "pineapple",
        "pineapple rings": "pineapple",
        "maraschino cherries": "cherries",

        # Deli meats
        "pepperoni slices": "pepperoni",
        "sliced pepperoni": "pepperoni",
        "turkey pepperoni": "pepperoni",
        "salami": "pepperoni",
        "hard salami": "pepperoni",
        "genoa salami": "pepperoni",
        "sopressata": "pepperoni",
        "capicola": "ham",
        "capocollo": "ham",
        "prosciutto": "ham",
        "pancetta": "bacon",
        "guanciale": "bacon",
        "canadian bacon": "ham",
        "black forest ham": "ham",
        "honey ham": "ham",
        "deli ham": "ham",
        "deli turkey": "turkey",
        "sliced turkey": "turkey",
        "turkey breast": "turkey",
        "roast beef": "beef",
        "deli roast beef": "beef",
        "corned beef": "beef",
        "pastrami": "beef",

        # Hot dogs and sausages
        "cooked franks": "hot dogs",
        "franks": "hot dogs",
        "frankfurters": "hot dogs",
        "wieners": "hot dogs",
        "beef franks": "hot dogs",
        "turkey dogs": "hot dogs",
        "cocktail franks": "hot dogs",
        "cocktail weiners": "hot dogs",
        "little smokies": "sausage",
        "lit'l smokies": "sausage",

        # Condiments and sauces
        "soy sauce": "soy sauce",
        "tamari": "soy sauce",
        "coconut aminos": "soy sauce",
        "teriyaki sauce": "soy sauce",
        "hoisin sauce": "soy sauce",
        "oyster sauce": "soy sauce",
        "fish sauce": "soy sauce",
        "worcestershire sauce": "soy sauce",
        "hot sauce": "salsa",
        "sriracha": "salsa",
        "tabasco": "salsa",
        "buffalo sauce": "salsa",
        "wing sauce": "salsa",
        "enchilada sauce": "salsa",
        "taco sauce": "salsa",
        "picante sauce": "salsa",
        "verde salsa": "salsa",
        "salsa verde": "salsa",
        "pico de gallo": "salsa",
        "for serving marinara sauce": "tomato sauce",
        "for dipping": "soy sauce",

        # Dairy and cream
        "plain yogurt": "yogurt",
        "vanilla yogurt": "yogurt",
        "greek yogurt": "yogurt",
        "nonfat yogurt": "yogurt",
        "non fat yogurt": "yogurt",
        "low-fat yogurt": "yogurt",
        "whole milk yogurt": "yogurt",
        "26% greek yogurt": "yogurt",
        "sour cream": "cream cheese",
        "creme fraiche": "cream cheese",
        "clotted cream": "cream cheese",
        "sweetened condensed milk": "milk",
        "condensed milk": "milk",
        "evaporated milk": "milk",
        "coconut milk": "milk",
        "coconut cream": "cream",
        "heavy whipping cream": "cream",
        "whipping cream": "cream",
        "half and half": "cream",
        "half-and-half": "cream",
        "light cream": "cream",
        "whipped cream": "cream",
        "cool whip": "cream",
        "whipped topping": "cream",

        # Baking items
        "caramel squares": "caramels",
        "caramel candies": "caramels",
        "kraft caramels": "caramels",
        "dulce de leche": "caramels",
        "caster sugar": "sugar",
        "castor sugar": "sugar",
        "superfine sugar": "sugar",
        "confectioners sugar": "powdered sugar",
        "icing sugar": "powdered sugar",
        "turbinado sugar": "brown sugar",
        "demerara sugar": "brown sugar",
        "muscovado sugar": "brown sugar",
        "raw sugar": "sugar",
        "cane sugar": "sugar",
        "coconut sugar": "brown sugar",
        "instant coffee": "coffee",
        "espresso powder": "coffee",
        "instant espresso": "coffee",
        "coffee granules": "coffee",
        "grated chocolate": "chocolate",
        "chocolate shavings": "chocolate",
        "chocolate curls": "chocolate",
        "mini chocolate chips": "chocolate chips",
        "white chocolate chips": "chocolate chips",
        "dark chocolate chips": "chocolate chips",
        "bittersweet chocolate": "chocolate",
        "semisweet chocolate": "chocolate",
        "unsweetened chocolate": "chocolate",
        "milk chocolate": "chocolate",
        "german chocolate": "chocolate",
        "cocoa nibs": "cocoa",
        "cacao powder": "cocoa",
        "dutch process cocoa": "cocoa",
        "natural cocoa": "cocoa",

        # Yeast and leavening
        "dry yeast": "yeast",
        "active dry yeast": "yeast",
        "instant yeast": "yeast",
        "rapid rise yeast": "yeast",
        "bread machine yeast": "yeast",
        "granulated yeast": "yeast",
        "package dry yeast": "yeast",
        "pkg yeast": "yeast",
        "packet yeast": "yeast",

        # Fruit items
        "large banana": "banana",
        "ripe banana": "banana",
        "mashed banana": "banana",
        "mashed ripe banana": "banana",
        "banana essence": "vanilla extract",
        "granny smith apples": "apples",
        "granny smith apple": "apples",
        "green apples": "apples",
        "gala apples": "apples",
        "fuji apples": "apples",
        "honeycrisp apples": "apples",
        "pink lady apples": "apples",
        "mcintosh apples": "apples",
        "red delicious apples": "apples",
        "golden delicious apples": "apples",
        "baked apples": "apples",
        "apple slices": "apples",

        # Alcohol
        "cognac": "brandy",
        "armagnac": "brandy",
        "calvados": "brandy",
        "grand marnier": "brandy",
        "cointreau": "brandy",
        "triple sec": "brandy",
        "orange liqueur": "brandy",
        "kahlua": "brandy",
        "coffee liqueur": "brandy",
        "amaretto": "brandy",
        "frangelico": "brandy",
        "bailey's": "cream",
        "irish cream": "cream",
        "champagne": "wine",
        "demi-sec champagne": "wine",
        "sparkling wine": "wine",
        "prosecco": "wine",
        "cava": "wine",
        "dry vermouth": "wine",
        "sweet vermouth": "wine",
        "sherry": "wine",
        "marsala": "wine",
        "port": "wine",
        "madeira": "wine",
        "sake": "wine",
        "mirin": "wine",
        "rice wine": "wine",
        "seltzer": "water",
        "club soda": "water",
        "sparkling water": "water",
        "tonic water": "water",
        "sparkling apple juice": "apple juice",

        # Juice and nectar
        "apricot nectar": "orange juice",
        "peach nectar": "orange juice",
        "mango nectar": "orange juice",
        "guava nectar": "orange juice",
        "cranberry juice": "orange juice",
        "grape juice": "orange juice",
        "pomegranate juice": "orange juice",
        "grapefruit juice": "orange juice",
        "pineapple juice": "orange juice",
        "tomato juice": "tomato sauce",
        "v8 juice": "tomato sauce",
        "clamato": "tomato sauce",
        "frozen orange juice": "orange juice",
        "can frozen orange juice": "orange juice",
        "bottle cranberry juice": "orange juice",

        # Canned items
        "cans biscuits": "biscuits",
        "can biscuits": "biscuits",
        "refrigerated biscuits": "biscuits",
        "pillsbury biscuits": "biscuits",
        "grands biscuits": "biscuits",
        "crescent rolls": "biscuits",
        "crescent roll dough": "biscuits",
        "can green chile strips": "green chilies",
        "green chile strips": "green chilies",
        "can green chile sauce": "green chilies",
        "can tomato sauce": "tomato sauce",
        "cans tomato sauce": "tomato sauce",
        "can mushroom soup": "cream of mushroom soup",
        "cans mushroom soup": "cream of mushroom soup",
        "condensed mushroom soup": "cream of mushroom soup",
        "cream of mushroom": "cream of mushroom soup",
        "condensed beef": "beef broth",
        "cans mushrooms": "mushrooms",
        "can mushrooms": "mushrooms",
        "canned mushrooms": "mushrooms",

        # Flax and seeds
        "ground flaxseed": "flaxseed",
        "ground flax seed": "flaxseed",
        "flax meal": "flaxseed",
        "flaxseed meal": "flaxseed",
        "chia seeds": "flaxseed",
        "hemp seeds": "flaxseed",
        "hemp hearts": "hemp seeds",
        "sunflower kernels": "sunflower seeds",
        "pepitas": "pumpkin seeds",
        # Note: sesame seeds, poppy seeds, caraway seeds are in database - no mapping needed

        # Herbs (fresh)
        "bunch dill": "dill",
        "fresh dill": "dill",
        "dill weed": "dill",
        "dill fronds": "dill",
        "grapefruit zest": "lemon zest",
        "orange zest": "lemon zest",
        "lime zest": "lemon zest",
        "citrus zest": "lemon zest",
        "loosely packed cilantro leaves": "cilantro",
        "cilantro leaves": "cilantro",
        "fresh cilantro": "cilantro",
        "coriander leaves": "cilantro",
        "mint leaves": "mint",
        "fresh mint": "mint",
        "spearmint": "mint",
        "peppermint": "mint",

        # Miscellaneous prepared items
        "salt-free all-purpose seasoning": "salt",
        "all-purpose seasoning": "salt",
        "seasoning blend": "salt",
        "mrs dash": "salt",
        "creamy peanut butter": "peanut butter",
        "smooth peanut butter": "peanut butter",
        "crunchy peanut butter": "peanut butter",
        "chunky peanut butter": "peanut butter",
        "natural peanut butter": "peanut butter",
        "almond butter": "peanut butter",
        "cashew butter": "peanut butter",
        "sunflower butter": "peanut butter",
        "pecan meats": "pecans",
        "walnut pieces": "walnuts",
        "walnut halves": "walnuts",
        "pecan pieces": "pecans",
        "pecan halves": "pecans",

        # Batch 11: More ingredient synonyms
        # Cereals and bran
        "bran cereal": "bran",
        "all-bran": "bran",
        "raisin bran": "bran",
        "bran flakes": "bran",
        "wheat bran": "bran",
        "oat bran": "oats",
        "bran flour": "bran",
        "grape nuts": "bran",
        "corn flakes": "cornmeal",
        "rice krispies": "rice",
        "cheerios": "oats",
        "granola": "oats",

        # Applesauce and fruit purees
        "applesauce": "apples",
        "unsweetened applesauce": "apples",
        "apple sauce": "apples",
        "apple butter": "apples",
        "pumpkin puree": "pumpkin",
        "canned pumpkin": "pumpkin",
        "pumpkin pie filling": "pumpkin",
        "mashed sweet potato": "sweet potatoes",
        "mashed potatoes": "potatoes",

        # Berries
        "frozen berries": "berries",
        "mixed berries": "berries",
        "fresh berries": "berries",
        "berry mix": "berries",
        "frozen strawberries": "strawberries",
        "frozen blueberries": "blueberries",
        "frozen raspberries": "raspberries",
        "frozen blackberries": "blackberries",
        "fresh strawberries": "strawberries",
        "fresh blueberries": "blueberries",
        "fresh raspberries": "raspberries",

        # Syrups
        "strawberry syrup": "sugar",
        "raspberry syrup": "sugar",
        "blueberry syrup": "sugar",
        "fruit syrup": "sugar",
        "simple syrup": "sugar",
        "malt syrup": "honey",
        "barley malt syrup": "honey",
        "rice syrup": "honey",
        "brown rice syrup": "honey",
        "golden syrup": "honey",
        "agave syrup": "honey",
        "agave nectar": "honey",
        "date syrup": "honey",
        "pomegranate molasses": "molasses",

        # Beef cuts
        "round steak": "beef steak",
        "cube steak": "beef steak",
        "minute steak": "beef steak",
        "swiss steak": "beef steak",
        "chicken fried steak": "beef steak",
        "salisbury steak": "ground beef",

        # Tortillas
        "corn tortillas": "tortillas",
        "flour tortillas": "tortillas",
        "whole wheat tortillas": "tortillas",
        "soft taco shells": "tortillas",
        "hard taco shells": "tortillas",
        "taco shells": "tortillas",
        "tostada shells": "tortillas",
        "burrito shells": "tortillas",
        "burrito tortillas": "tortillas",
        "fajita tortillas": "tortillas",

        # Coconut products
        "coconut flakes": "coconut",
        "shredded coconut": "coconut",
        "sweetened coconut": "coconut",
        "unsweetened coconut": "coconut",
        "toasted coconut": "coconut",
        "coconut chips": "coconut",
        "desiccated coconut": "coconut",

        # More bread items
        "ciabatta rolls": "french bread",
        "ciabatta roll": "french bread",
        "whole ciabatta": "french bread",
        "kaiser rolls": "bread",
        "hoagie rolls": "bread",
        "sub rolls": "bread",
        "hamburger buns": "bread",
        "hot dog buns": "bread",
        "slider buns": "bread",
        "dinner rolls": "bread",
        "parker house rolls": "bread",
        "crescent rolls": "biscuits",
        "hawaiian rolls": "bread",
        "kings hawaiian": "bread",
        "texas toast": "bread",
        "garlic bread": "bread",

        # Ham varieties
        "spiced ham": "ham",
        "baked ham": "ham",
        "glazed ham": "ham",
        "spiral ham": "ham",
        "bone-in ham": "ham",
        "boneless ham": "ham",
        "ham steak": "ham",
        "country ham": "ham",
        "city ham": "ham",
        "smoked ham": "ham",
        "virginia ham": "ham",

        # Bacon
        "bacon strips": "bacon",
        "bacon slices": "bacon",
        "thick-cut bacon": "bacon",
        "thin-cut bacon": "bacon",
        "center-cut bacon": "bacon",
        "applewood bacon": "bacon",
        "hickory bacon": "bacon",
        "maple bacon": "bacon",
        "turkey bacon": "bacon",
        "beef bacon": "bacon",

        # Greens (arugula/rocket)
        "fresh rocket": "spinach",
        "rocket leaves": "spinach",
        "baby rocket": "spinach",
        "wild arugula": "spinach",
        "baby arugula": "spinach",

        # Citrus
        "grapefruits": "grapefruit",
        "pink grapefruit": "grapefruit",
        "ruby red grapefruit": "grapefruit",
        "white grapefruit": "grapefruit",
        "grapefruit segments": "grapefruit",
        "grapefruit sections": "grapefruit",
        "blood orange": "oranges",
        "navel orange": "oranges",
        "cara cara orange": "oranges",
        "clementines": "oranges",
        "tangerines": "oranges",
        "satsumas": "oranges",
        "meyer lemon": "lemon",
        "meyer lemons": "lemon",
        "key limes": "lime",
        "persian limes": "lime",

        # Vegetables
        "eggplant": "squash",
        "egg plant": "squash",
        "aubergine": "squash",
        "japanese eggplant": "squash",
        "chinese eggplant": "squash",
        "baby eggplant": "squash",
        "pimiento": "red pepper",
        "pimientos": "red pepper",
        "whole pimiento": "red pepper",
        "diced pimientos": "red pepper",

        # Vinegars
        "cider vinegar": "vinegar",
        "apple cider vinegar": "vinegar",
        "white vinegar": "vinegar",
        "distilled vinegar": "vinegar",
        "red wine vinegar": "vinegar",
        "white wine vinegar": "vinegar",
        "sherry vinegar": "vinegar",
        "champagne vinegar": "vinegar",
        "balsamic vinegar": "vinegar",
        "rice vinegar": "vinegar",
        "seasoned rice vinegar": "vinegar",
        "malt vinegar": "vinegar",

        # Spices (whole vs ground)
        "whole cloves": "cloves",
        "ground cloves": "cloves",
        "whole allspice": "allspice",
        "ground allspice": "allspice",
        "whole nutmeg": "nutmeg",
        "freshly grated nutmeg": "nutmeg",
        "celery seed": "celery",
        "celery seeds": "celery",
        "mustard seed": "mustard",
        "mustard seeds": "mustard",
        "cumin seed": "cumin",
        "cumin seeds": "cumin",
        "coriander seed": "coriander",
        "coriander seeds": "coriander",
        "fennel seed": "fennel",
        "fennel seeds": "fennel",
        "dill seed": "dill",
        "dill seeds": "dill",
        "anise seed": "fennel",
        "anise seeds": "fennel",
        "star anise": "fennel",

        # Chili and pepper powders
        "mild chili powder": "chili powder",
        "hot chili powder": "chili powder",
        "ancho chili powder": "chili powder",
        "chipotle chili powder": "chili powder",
        "cayenne pepper": "chili powder",
        "ground cayenne": "chili powder",
        "red pepper flakes": "chili powder",
        "crushed red pepper": "chili powder",
        "aleppo pepper": "chili powder",
        "gochugaru": "chili powder",
        "korean chili flakes": "chili powder",

        # Breakfast meats
        "breakfast sausage": "sausage",
        "pork sausage": "sausage",
        "turkey sausage": "sausage",
        "chicken sausage": "sausage",
        "veggie sausage": "sausage",
        "sausage links": "sausage",
        "sausage patties": "sausage",
        "chorizo sausage": "chorizo",
        "mexican chorizo": "chorizo",
        "spanish chorizo": "chorizo",

        # Pizza dough
        "frozen pizza dough": "pizza dough",
        "refrigerated pizza dough": "pizza dough",
        "store-bought pizza dough": "pizza dough",
        "pizza crust": "pizza dough",
        "prebaked pizza crust": "pizza dough",
        "boboli": "pizza dough",
        "naan pizza crust": "pizza dough",
        "flatbread pizza crust": "pizza dough",

        # Measurement/equipment words to filter
        "pkg": "",
        "package": "",
        "packages": "",
        "can": "",
        "cans": "",
        "jar": "",
        "jars": "",
        "bag": "",
        "bags": "",
        "box": "",
        "boxes": "",
        "bunch": "",
        "bunches": "",
        "handful": "",
        "handfuls": "",
        "slice": "",
        "slices": "",
        "strip": "",
        "strips": "",
        "piece": "",
        "pieces": "",
        "whole": "",
        "inch": "",
        "inches": "",

        # Juice concentrate
        "apple juice concentrate": "apple juice",
        "frozen apple juice concentrate": "apple juice",
        "orange juice concentrate": "orange juice",
        "frozen orange juice concentrate": "orange juice",
        "grape juice concentrate": "grape juice",
        "lemon juice concentrate": "lemon juice",
        "lime juice concentrate": "lime juice",
        "pineapple juice concentrate": "pineapple juice",

        # More misc items
        "boiling water": "water",
        "cold water": "water",
        "warm water": "water",
        "hot water": "water",
        "ice water": "water",
        "room temperature water": "water",
        "honey": "honey",
        "warmed honey": "honey",
        "raw honey": "honey",
        "local honey": "honey",
        "clover honey": "honey",
        "wildflower honey": "honey",
        "manuka honey": "honey",
        "for serving": "",
        "for topping": "",
        "for garnish": "",
        "for dipping": "",
        "optional": "",

        # Batch 13: More ingredient synonyms
        # Vegetables & Produce
        "roma tomato": "roma tomatoes",
        "plum tomato": "roma tomatoes",
        "medium roma tomatoes": "roma tomatoes",
        "medium tomatoes": "tomatoes",
        "medium tomato": "tomatoes",
        "diced tomatoes": "canned tomatoes",
        "sliced cucumber": "cucumber",
        "diced cucumber": "cucumber",
        "chopped cucumber": "cucumber",
        "english cucumber": "cucumber",
        "seedless cucumber": "cucumber",
        "peeled jicama": "jicama",
        "julienne-cut peeled jicama": "jicama",
        "julienne jicama": "jicama",
        "yellow squash": "zucchini",

        # Seafood
        "yellowfin tuna steaks": "tuna",
        "yellowfin tuna": "tuna",
        "ahi tuna steaks": "tuna",
        "tuna steak": "tuna",
        "cod fillet": "cod",
        "scrubbed mussels": "mussels",
        "debearded mussels": "mussels",

        # Meats
        "ground veal or turkey": "ground veal",
        "top sirloin beef": "beef steak",
        "top sirloin": "beef steak",
        "boneless pork steak": "pork chops",
        "pork steak": "pork chops",
        "beef round steak": "beef steak",
        "boneless beef chuck roast": "beef roast",
        "guanciale": "pancetta",
        "finely chopped pancetta": "pancetta",

        # Cheese
        "smoked mozzarella": "mozzarella",
        "fresh mozzarella": "mozzarella",
        "shredded mozzarella": "mozzarella",
        "grated mozzarella": "mozzarella",
        "grated fresh parmigiano-reggiano cheese": "parmesan cheese",
        "fresh parmigiano-reggiano": "parmesan cheese",
        "parmigiano-reggiano": "parmesan cheese",
        "grated parmesan": "parmesan cheese",
        "freshly grated parmesan": "parmesan cheese",
        "shredded cheddar cheese": "cheddar cheese",
        "shredded monterey jack cheese": "monterey jack cheese",
        "shredded mexican-blend cheese": "cheddar cheese",
        "mexican blend cheese": "cheddar cheese",
        "sharp cheddar": "cheddar cheese",
        "longhorn cheese": "cheddar cheese",
        "long horn cheese": "cheddar cheese",
        "feta cheese": "feta",
        "crumbled feta": "feta",
        "crumbled cotija cheese": "cotija cheese",
        "soft goat cheese": "goat cheese",

        # Sauces & condiments
        "shoyu": "soy sauce",
        "tamari": "soy sauce",
        "red russian dressing": "russian dressing",
        "kraft creamy french dressing": "creamy french dressing",
        "old world style pasta sauce": "tomato sauce",
        "ragu pasta sauce": "tomato sauce",
        "jar taco sauce": "taco sauce",
        "bottle tomato catsup": "ketchup",
        "tomato catsup": "ketchup",
        "bottle russian dressing": "russian dressing",

        # Bread & dough
        "savory deep dish pie crust": "deep dish pie crust",
        "frozen puff pastry": "puff pastry",
        "thawed puff pastry": "puff pastry",
        "pita bread": "pita",
        "sandwich bread": "bread",
        "white sandwich bread": "bread",
        "whole wheat bread": "bread",

        # Alcohol & beverages
        "apricot brandy": "brandy",
        "cooking wine": "white wine",
        "unsweetened pineapple juice": "pineapple juice",

        # Spices & seasonings
        "tarragon leaves": "tarragon",
        "fresh tarragon": "tarragon",
        "dried tarragon": "tarragon",
        "dried oregano leaves": "oregano",
        "dried thyme leaves": "thyme",
        "crushed oregano": "oregano",
        "coriander powder": "coriander",
        "garam masala powder": "garam masala",
        "taco seasoning": "chili powder",
        "chili seasoning mix": "chili powder",
        "taco seasoning mix": "chili powder",
        "mild chili seasoning": "chili powder",
        "onion soup mix": "onion soup",
        "dry onion soup": "onion soup",
        "lipton onion soup": "onion soup",

        # Canned goods
        "can black olives": "black olives",
        "ripe black olives": "black olives",
        "sliced black olives": "black olives",
        "pitted black olives": "black olives",
        "can kidney beans": "kidney beans",
        "can black beans": "black beans",
        "can pinto beans": "pinto beans",
        "can chili beans": "chili beans",
        "can cannellini beans": "cannellini beans",
        "can great northern beans": "great northern beans",
        "can refried beans": "refried beans",
        "can tomato sauce": "tomato sauce",
        "can stewed tomatoes": "canned tomatoes",
        "can diced tomatoes": "canned tomatoes",
        "can tomato juice": "tomato juice",
        "can tomato puree": "tomato puree",
        "can green chiles": "green chilies",
        "can diced green chiles": "green chilies",
        "can cream of mushroom soup": "mushroom soup",
        "can cream of chicken soup": "cream of chicken soup",
        "can chicken broth": "chicken broth",
        "can beef broth": "beef broth",
        "can mixed vegetables": "mixed vegetables",
        "can corn": "corn",
        "canned pineapple chunk": "pineapple chunks",

        # Preserves & sweets
        "jar apricot preserves": "apricot preserves",
        "apricot jam": "apricot preserves",
        "strawberry preserves": "jam",
        "fruit preserves": "jam",
        "grape jelly": "jam",

        # Misc
        "hot dogs": "hot dog",
        "frankfurters": "hot dog",
        "franks": "hot dog",
        "lesueur peas": "peas",
        "petit pois": "peas",
        "instant yeast": "yeast",
        "active dry yeast": "yeast",
        "dry yeast": "yeast",
        "rapid rise yeast": "yeast",
        "yeast cake": "yeast",
        "cake yeast": "yeast",
        "biscuit baking mix": "bisquick",
        "baking mix": "bisquick",
        "watercress": "arugula",
        "tough stems removed": "",
        "cooked rice": "rice",
        "leftover rice": "rice",
        "steamed rice": "rice",
        "chopped walnuts": "walnuts",
        "chopped pecans": "pecans",
        "chopped almonds": "almonds",

        # Batch 14: Additional synonyms for common variations
        # Onion variants
        "purple onion": "red onion",
        "spanish onion": "onion",
        "yellow onion": "onion",
        "sweet onion": "onion",
        "vidalia onion": "onion",
        "walla walla onion": "onion",
        # Lettuce types -> lettuce (base mapping)
        "bibb lettuce": "lettuce",
        "boston lettuce": "lettuce",
        "butterhead lettuce": "lettuce",
        "romaine lettuce": "lettuce",
        "iceberg lettuce": "lettuce",
        "leaf lettuce": "lettuce",
        "mixed greens": "lettuce",
        "salad greens": "lettuce",
        "spring mix": "lettuce",
        # Celery variants
        "chopped celery": "celery",
        "celery stalk": "celery",
        "celery stalks": "celery",
        "celery ribs": "celery",
        "celery rib": "celery",
        # Carrot variants
        "chopped carrot": "carrots",
        "shredded carrot": "carrots",
        "carrot sticks": "carrots",
        # Pepper variants
        "sweet red pepper": "red pepper",
        "red bell pepper": "red pepper",
        "green bell pepper": "green pepper",
        "yellow bell pepper": "yellow pepper",
        "orange bell pepper": "orange pepper",
        "bell pepper": "green pepper",
        # Herbs with sprigs/leaves
        "thyme sprigs": "thyme",
        "thyme sprig": "thyme",
        "parsley sprigs": "parsley",
        "parsley sprig": "parsley",
        "dill sprigs": "dill",
        "rosemary sprigs": "rosemary",
        "oregano leaves": "oregano",
        "thyme leaves": "thyme",
        "basil leaves": "basil",
        "sage leaves": "sage",
        "mint leaves": "mint",
        # Mayonnaise variants
        "reduced-fat mayonnaise": "light mayonnaise",
        "low-fat mayonnaise": "light mayonnaise",
        "fat free mayonnaise": "light mayonnaise",
        "mayo": "mayonnaise",
        # Sesame oil
        "toasted sesame oil": "dark sesame oil",
        "asian sesame oil": "dark sesame oil",
        # Large/medium/small fruit
        "large lemon": "lemon",
        "medium lemon": "lemon",
        "small lemon": "lemon",
        "large lime": "lime",
        "medium lime": "lime",
        "large orange": "oranges",
        "medium orange": "oranges",
        "navel orange": "oranges",
        "valencia orange": "oranges",
        # Cheese variants
        "parmigiano-reggiano cheese": "parmesan cheese",
        "parmigiano-reggiano": "parmesan cheese",
        "pecorino romano": "parmesan cheese",
        "grated parmesan": "parmesan cheese",
        "shaved parmesan": "parmesan cheese",
        "blue cheese": "blue cheese crumbles",
        "gorgonzola": "blue cheese crumbles",
        # Pepper/spices
        "coarsely ground pepper": "black pepper",
        "freshly ground pepper": "black pepper",
        "ground black pepper": "black pepper",
        "cracked pepper": "black pepper",
        "crushed red pepper": "red pepper flakes",
        "red pepper flakes": "red pepper flakes",
        "italian seasoning": "italian herbs",
        # Meat variants
        "boneless skinless chicken": "chicken breast",
        "chicken cutlets": "chicken breast",
        "chicken tenders": "chicken breast",
        "skinless chicken thighs": "chicken thighs",
        "bone-in chicken": "chicken",
        # Pasta
        "penne pasta": "pasta",
        "spaghetti": "pasta",
        "linguine": "pasta",
        "fettuccine": "pasta",
        "rigatoni": "pasta",
        "farfalle": "pasta",
        "rotini": "pasta",
        "angel hair": "pasta",
        "egg noodles": "pasta",

        # Batch 15: More synonyms for remaining variations
        # Ginger variants
        "gingerroot": "fresh gingerroot",
        "fresh ginger": "fresh gingerroot",
        "ginger root": "fresh gingerroot",
        "minced ginger": "fresh gingerroot",
        "grated ginger": "fresh gingerroot",
        # Mushroom variants
        "sliced mushrooms": "fresh mushrooms",
        "white mushrooms": "fresh mushrooms",
        "cremini mushrooms": "fresh mushrooms",
        "button mushrooms": "fresh mushrooms",
        "baby bella mushrooms": "fresh mushrooms",
        # Cheese variants
        "mozzarella cheese": "part-skim mozzarella cheese",
        "shredded mozzarella": "part-skim mozzarella cheese",
        "fresh mozzarella": "part-skim mozzarella cheese",
        "monterey jack cheese": "jack cheese",
        "pepper jack cheese": "jack cheese",
        "colby jack cheese": "jack cheese",
        "crumbled blue cheese": "blue cheese crumbles",
        # Pepper variants
        "green pepper": "medium green pepper",
        "large green pepper": "medium green pepper",
        "small green pepper": "medium green pepper",
        "diced green pepper": "medium green pepper",
        # Avocado
        "ripe avocado": "medium ripe avocado",
        "large avocado": "medium ripe avocado",
        "haas avocado": "medium ripe avocado",
        "hass avocado": "medium ripe avocado",
        # Zucchini
        "small zucchini": "medium zucchini",
        "large zucchini": "medium zucchini",
        "diced zucchini": "zucchini",
        "sliced zucchini": "zucchini",
        # Broth variants
        "low-sodium chicken broth": "reduced-sodium chicken broth",
        "low sodium chicken broth": "reduced-sodium chicken broth",
        "less sodium chicken broth": "reduced-sodium chicken broth",
        "low-sodium beef broth": "reduced-sodium beef broth",
        "low sodium beef broth": "reduced-sodium beef broth",
        # Sauce variants
        "hot sauce": "pepper sauce",
        "hot pepper sauce": "pepper sauce",
        "tabasco": "pepper sauce",
        "franks hot sauce": "pepper sauce",
        "louisiana hot sauce": "pepper sauce",
        "sriracha": "pepper sauce",
        "bbq sauce": "barbecue sauce",
        "white sauce": "bechamel sauce",
        # Section headers (to ignore)
        "sauce:": "",
        "filling:": "",
        "topping:": "",
        "dressing:": "",
        "salad:": "",
        "for the sauce:": "",
        "for the filling:": "",
        "for the topping:": "",
        # Meat variants
        "pork chops": "pork loin chops",
        "boneless pork chops": "pork loin chops",
        "thick-cut pork chops": "pork loin chops",
        "ground turkey": "lean ground turkey",
        "extra lean ground turkey": "lean ground turkey",
        "flank steak": "beef steak",
        "sirloin steak": "beef steak",
        "strip steak": "beef steak",
        "ribeye steak": "beef steak",
        "tilapia": "white fish",
        "halibut": "white fish",
        "mahi mahi": "white fish",
        "snapper": "white fish",
        "sea bass": "white fish",
        # Seasoning variants
        "lemon pepper": "lemon-pepper seasoning",
        "creole seasoning": "cajun seasoning",
        "blackening seasoning": "cajun seasoning",
        "dry mustard": "ground mustard",
        "mustard powder": "ground mustard",
        "sage": "rubbed sage",
        "dried sage": "rubbed sage",
        "ground sage": "rubbed sage",
        # Garnishes (minimal calories)
        "lemon wedges": "lemon",
        "lime wedges": "lime",
        "lime wedge": "lime",
        "orange wedges": "oranges",
    }

    # Check for exact match first
    if item in synonyms:
        item = synonyms[item]
    else:
        # Try partial matches
        for old, new in synonyms.items():
            if old in item:
                item = new
                break

    return item.strip()


# =============================================================================
# EQUIPMENT FILTER - Items that are not food
# =============================================================================

EQUIPMENT_WORDS = {
    # Kitchen equipment
    "mixing-bowl", "mixing bowl", "bowl", "mixing-spoon", "spoon", "fork",
    "dover beater", "beater", "double-boiler", "double boiler", "saucepan",
    "flour sifter", "sifter", "vegetable-knife", "knife", "grater",
    "egg mixing-bowl", "butter mixing-bowl", "ugar mixing-spoon",
    "milk dover beater", "milk double-boiler",
    # Meta instructions
    "for the cake:", "for the frosting:", "for the filling:",
    "mrs.wilson's cookbook", "-inch", "-sized",
    # Non-food items
    "each", "s", "d 227", "egg .03",
}

def is_equipment(item):
    """Check if an item is equipment/non-food rather than an ingredient."""
    item_lower = item.lower().strip()

    # Direct matches
    if item_lower in EQUIPMENT_WORDS:
        return True

    # Partial matches for equipment patterns
    equipment_patterns = [
        "mixing-bowl", "mixing bowl", "double-boiler", "double boiler",
        "dover beater", "vegetable-knife", "flour sifter",
        "for the ", "cookbook", "-inch", "-sized potatoes vegetable",
        "for topping", "for serving", "for dipping", "for garnish",
        "for dusting", "(optional)", "optional",
    ]
    for pattern in equipment_patterns:
        if pattern in item_lower:
            return True

    # Very short items that are likely OCR garbage
    if len(item_lower) <= 2 and not item_lower.isdigit():
        return True

    return False


# =============================================================================
# SERVING INFERENCE - Smart defaults based on category
# =============================================================================

def infer_servings(recipe):
    """Infer serving size based on recipe characteristics."""
    # Check if we have explicit servings
    servings_yield = recipe.get("servings_yield", "")
    if servings_yield:
        parsed = parse_servings(servings_yield)
        if parsed:
            return parsed

    category = recipe.get("category", "").lower()
    title = recipe.get("title", "").lower()
    ingredients = recipe.get("ingredients", [])

    # Count key ingredients to estimate yield
    flour_cups = 0
    meat_lbs = 0
    egg_count = 0

    for ing in ingredients:
        item = ing.get("item", "").lower()
        unit = ing.get("unit", "").lower()
        try:
            qty = float(ing.get("quantity", 0) or 0)
        except:
            qty = 1

        if "flour" in item and "cup" in unit:
            flour_cups += qty
        elif any(m in item for m in ["beef", "chicken", "pork", "turkey", "lamb"]) and "lb" in unit:
            meat_lbs += qty
        elif "egg" in item and unit in ("", "each", "large"):
            egg_count += qty

    # Category-based defaults
    if category == "beverages":
        return 4
    elif category == "appetizers":
        return 8  # Appetizers usually serve more
    elif category == "desserts":
        if "cookie" in title or "bar" in title:
            return 24  # Cookies/bars make many
        elif "cake" in title:
            return 12
        elif "pie" in title:
            return 8
        elif flour_cups >= 3:
            return 16  # Large batch
        else:
            return 8
    elif category == "breads":
        if "muffin" in title:
            return 12
        elif "roll" in title or "biscuit" in title:
            return 12
        elif "loaf" in title or "bread" in title:
            return 12  # One loaf = ~12 slices
        else:
            return 8
    elif category == "breakfast":
        if "pancake" in title or "waffle" in title:
            return 4
        else:
            return 4
    elif category == "mains":
        if meat_lbs >= 2:
            return 8
        elif meat_lbs >= 1:
            return 6
        else:
            return 4
    elif category == "soups":
        return 6
    elif category == "salads":
        return 6
    elif category == "sides":
        return 6

    # Fallback based on ingredient volume
    if flour_cups >= 4:
        return 16
    elif flour_cups >= 2:
        return 8
    elif meat_lbs >= 2:
        return 8

    return 4  # Default


# =============================================================================
# NUTRITION CALCULATION
# =============================================================================

def get_nutrition_for_ingredient(ingredient):
    """Calculate nutrition for a single ingredient entry."""
    raw_item = ingredient.get("item", "")
    raw_unit = ingredient.get("unit", "")

    # Extract OCR-embedded unit prefixes from item (e.g., "c sugar" -> unit="cup", item="sugar")
    ocr_unit_prefixes = {
        "c ": "cup",
        "t ": "tsp",
        "T ": "tbsp",
        "slices ": "slice",
        "slice ": "slice",
        "ears ": "ear",
        "ear ": "ear",
        "qt. ": "quart",
        "qt ": "quart",
        "pt. ": "pint",
        "pt ": "pint",
        "oz ": "oz",
        "lb ": "lb",
        "cups ": "cup",
        "cup ": "cup",
        "tbsp ": "tbsp",
        "tsp ": "tsp",
        "tblsp. ": "tbsp",
        "tblsps. ": "tbsp",
    }
    extracted_unit = None
    for prefix, unit_name in ocr_unit_prefixes.items():
        if raw_item.lower().startswith(prefix.lower()) and not raw_unit:
            extracted_unit = unit_name
            raw_item = raw_item[len(prefix):]
            break

    item = normalize_ingredient(raw_item)
    unit = str(raw_unit).lower() if raw_unit else (extracted_unit or "")

    # Skip equipment and non-food items
    if is_equipment(item):
        return {"cal": 0, "fat": 0, "carbs": 0, "protein": 0, "sodium": 0, "fiber": 0, "sugar": 0, "_skipped": True}

    # Skip items where unit indicates non-countable usage (greasing, brushing, etc.)
    non_countable_units = ["for greasing", "for brushing", "for drizzling", "as needed"]
    if any(ncu in unit for ncu in non_countable_units):
        return {"cal": 0, "fat": 0, "carbs": 0, "protein": 0, "sodium": 0, "fiber": 0, "sugar": 0, "_skipped": True}

    quantity = parse_quantity(ingredient.get("quantity", "1"))
    # Only normalize unit if we didn't extract one from OCR prefix
    if not extracted_unit:
        unit = normalize_unit(ingredient.get("unit", ""))

    # Handle compound units like "5-oz" or "6-inch" -> extract multiplier
    compound_match = re.match(r'^(\d+(?:\.\d+)?)-?(\w+)$', unit)
    if compound_match:
        unit_multiplier = float(compound_match.group(1))
        unit = compound_match.group(2)
        quantity = quantity * unit_multiplier

    # Handle "to taste" / "to sweeten" - minimal impact (check unit, item, and prep_note)
    to_taste_fields = [
        str(ingredient.get("unit", "")).lower(),
        str(ingredient.get("item", "")).lower(),
        str(ingredient.get("prep_note", "")).lower()
    ]
    if any("to taste" in f or "to sweeten" in f for f in to_taste_fields):
        if "salt" in item or "pepper" in item:
            return {"cal": 0, "fat": 0, "carbs": 0, "protein": 0, "sodium": 150, "fiber": 0, "sugar": 0}
        return {"cal": 0, "fat": 0, "carbs": 0, "protein": 0, "sodium": 0, "fiber": 0, "sugar": 0}

    # Handle water
    if "water" in item and item not in NUTRITION_DB:
        return {"cal": 0, "fat": 0, "carbs": 0, "protein": 0, "sodium": 0, "fiber": 0, "sugar": 0}

    # Try exact match
    if item in NUTRITION_DB:
        db_entry = NUTRITION_DB[item]
        if unit in db_entry:
            base = db_entry[unit]
            return {k: v * quantity for k, v in base.items()}
        elif "" in db_entry:  # Unit-less items
            base = db_entry[""]
            return {k: v * quantity for k, v in base.items()}
        # Try unit conversions
        elif unit == "tbsp" and "cup" in db_entry:
            base = db_entry["cup"]
            return {k: v * quantity / 16 for k, v in base.items()}
        elif unit == "tsp" and "cup" in db_entry:
            base = db_entry["cup"]
            return {k: v * quantity / 48 for k, v in base.items()}
        elif unit == "tsp" and "tbsp" in db_entry:
            base = db_entry["tbsp"]
            return {k: v * quantity / 3 for k, v in base.items()}
        elif unit == "tbsp" and "tsp" in db_entry:
            base = db_entry["tsp"]
            return {k: v * quantity * 3 for k, v in base.items()}
        # Pint/quart to cup conversions
        elif unit == "pint" and "cup" in db_entry:
            base = db_entry["cup"]
            return {k: v * quantity * 2 for k, v in base.items()}  # 1 pint = 2 cups
        elif unit == "quart" and "cup" in db_entry:
            base = db_entry["cup"]
            return {k: v * quantity * 4 for k, v in base.items()}  # 1 quart = 4 cups
        elif unit == "gallon" and "cup" in db_entry:
            base = db_entry["cup"]
            return {k: v * quantity * 16 for k, v in base.items()}  # 1 gallon = 16 cups
        # ML to cup conversion
        elif unit == "ml" and "cup" in db_entry:
            base = db_entry["cup"]
            return {k: v * quantity / 237 for k, v in base.items()}  # ~237 ml per cup
        # Historical measurement conversions (Batch 14)
        elif unit == "gill" and "cup" in db_entry:
            base = db_entry["cup"]
            return {k: v * quantity * 0.5 for k, v in base.items()}  # 1 gill = 0.5 cup (4 fl oz)
        elif unit == "drachm" and "oz" in db_entry:
            base = db_entry["oz"]
            return {k: v * quantity / 8 for k, v in base.items()}  # 1 drachm = 1/8 oz
        elif unit == "drachm" and "tbsp" in db_entry:
            base = db_entry["tbsp"]
            return {k: v * quantity / 4 for k, v in base.items()}  # 1 fluid drachm ≈ 0.25 tbsp
        elif unit == "dessertspoon" and "tsp" in db_entry:
            base = db_entry["tsp"]
            return {k: v * quantity * 2 for k, v in base.items()}  # 1 dessertspoon = 2 tsp
        elif unit == "dessertspoon" and "tbsp" in db_entry:
            base = db_entry["tbsp"]
            return {k: v * quantity * 0.67 for k, v in base.items()}  # 1 dessertspoon = 2/3 tbsp
        elif unit == "dessertspoon" and "cup" in db_entry:
            base = db_entry["cup"]
            return {k: v * quantity / 24 for k, v in base.items()}  # 24 dessertspoons = 1 cup
        elif unit == "saltspoon" and "tsp" in db_entry:
            base = db_entry["tsp"]
            return {k: v * quantity / 4 for k, v in base.items()}  # 1 saltspoon = 1/4 tsp
        elif unit == "saltspoon" and "cup" in db_entry:
            base = db_entry["cup"]
            return {k: v * quantity / 192 for k, v in base.items()}  # 192 saltspoons = 1 cup
        elif unit == "wineglass" and "cup" in db_entry:
            base = db_entry["cup"]
            return {k: v * quantity * 0.5 for k, v in base.items()}  # 1 wineglass ≈ 0.5 cup (4 fl oz)
        elif unit == "teacup" and "cup" in db_entry:
            base = db_entry["cup"]
            return {k: v * quantity * 0.75 for k, v in base.items()}  # 1 teacup ≈ 0.75 cup (6 fl oz)
        elif unit == "coffeecup" and "cup" in db_entry:
            base = db_entry["cup"]
            return {k: v * quantity for k, v in base.items()}  # 1 coffeecup ≈ 1 cup
        elif unit == "jigger" and "tbsp" in db_entry:
            base = db_entry["tbsp"]
            return {k: v * quantity * 3 for k, v in base.items()}  # 1 jigger = 3 tbsp (1.5 oz)
        elif unit == "jigger" and "cup" in db_entry:
            base = db_entry["cup"]
            return {k: v * quantity / 5.33 for k, v in base.items()}  # 1 jigger ≈ 3/16 cup
        elif unit == "peck" and "quart" in db_entry:
            base = db_entry["quart"]
            return {k: v * quantity * 8 for k, v in base.items()}  # 1 peck = 8 quarts
        elif unit == "peck" and "cup" in db_entry:
            base = db_entry["cup"]
            return {k: v * quantity * 32 for k, v in base.items()}  # 1 peck = 32 cups
        elif unit == "bushel" and "quart" in db_entry:
            base = db_entry["quart"]
            return {k: v * quantity * 32 for k, v in base.items()}  # 1 bushel = 32 quarts
        elif unit == "bushel" and "cup" in db_entry:
            base = db_entry["cup"]
            return {k: v * quantity * 128 for k, v in base.items()}  # 1 bushel = 128 cups
        # Batch 15: Weight to volume conversions for common baking items
        elif unit == "lb" and "cup" in db_entry:
            # Common conversions: flour ~4 cups/lb, sugar ~2.25 cups/lb, butter ~2 cups/lb
            if "flour" in item:
                base = db_entry["cup"]
                return {k: v * quantity * 4 for k, v in base.items()}  # 1 lb flour ≈ 4 cups
            elif "sugar" in item:
                base = db_entry["cup"]
                return {k: v * quantity * 2.25 for k, v in base.items()}  # 1 lb sugar ≈ 2.25 cups
            else:
                base = db_entry["cup"]
                return {k: v * quantity * 2 for k, v in base.items()}  # Generic: 1 lb ≈ 2 cups
        elif unit == "oz" and "cup" in db_entry:
            base = db_entry["cup"]
            return {k: v * quantity / 8 for k, v in base.items()}  # 8 oz = 1 cup (volume)
        elif unit == "oz" and "tbsp" in db_entry:
            base = db_entry["tbsp"]
            return {k: v * quantity * 2 for k, v in base.items()}  # 1 oz = 2 tbsp
        elif unit == "tsp" and "cup" in db_entry:
            base = db_entry["cup"]
            return {k: v * quantity / 48 for k, v in base.items()}  # 48 tsp = 1 cup
        # Empty unit fallback - use first available unit as reasonable default
        elif unit == "" and db_entry:
            # Prefer common units in order
            for preferred in ["tbsp", "tsp", "cup", "oz", "each", ""]:
                if preferred in db_entry:
                    base = db_entry[preferred]
                    return {k: v * quantity for k, v in base.items()}

    # Try without unit for counted items
    if item in NUTRITION_DB and "" in NUTRITION_DB[item]:
        base = NUTRITION_DB[item][""]
        return {k: v * quantity for k, v in base.items()}

    return None


def parse_servings(servings_str, default=4):
    """Parse servings from yield string. Default to 4 if not specified."""
    if not servings_str:
        return default

    servings_str = str(servings_str).lower()

    # Handle range like "6-8 servings" - take midpoint
    range_match = re.search(r'(\d+)\s*[-–to]+\s*(\d+)', servings_str)
    if range_match:
        low = int(range_match.group(1))
        high = int(range_match.group(2))
        return (low + high) // 2

    # Handle simple number
    match = re.search(r'(\d+)', servings_str)
    if match:
        return int(match.group(1))

    # Handle word-based
    word_map = {
        "one": 1, "two": 2, "three": 3, "four": 4, "five": 5,
        "six": 6, "seven": 7, "eight": 8, "nine": 9, "ten": 10,
        "twelve": 12, "dozen": 12, "several": 4
    }
    for word, num in word_map.items():
        if word in servings_str:
            return num

    return default


def calculate_recipe_nutrition(recipe, default_servings=4):
    """Calculate complete nutrition for a recipe."""
    ingredients = recipe.get("ingredients", [])

    # Use smart serving inference
    servings = infer_servings(recipe)
    serving_inferred = not recipe.get("servings_yield")

    total = {"cal": 0, "fat": 0, "carbs": 0, "protein": 0, "sodium": 0, "fiber": 0, "sugar": 0}
    missing = []
    skipped_equipment = 0
    actual_ingredients = 0

    for ing in ingredients:
        nutr = get_nutrition_for_ingredient(ing)
        if nutr:
            # Check if it was skipped equipment
            if nutr.get("_skipped"):
                skipped_equipment += 1
            else:
                actual_ingredients += 1
                for key in total:
                    total[key] += nutr.get(key, 0)
        else:
            # Check if it's equipment before adding to missing
            item = normalize_ingredient(ing.get("item", ""))
            if not is_equipment(item):
                actual_ingredients += 1
                ing_str = f"{ing.get('quantity', '')} {ing.get('unit', '')} {ing.get('item', '')}".strip()
                if ing_str:
                    missing.append(ing_str)

    # Calculate per-serving values
    per_serving = {
        "calories": round(total["cal"] / servings),
        "fat_g": round(total["fat"] / servings, 1),
        "carbs_g": round(total["carbs"] / servings, 1),
        "protein_g": round(total["protein"] / servings, 1),
        "sodium_mg": round(total["sodium"] / servings),
        "fiber_g": round(total["fiber"] / servings, 1),
        "sugar_g": round(total["sugar"] / servings, 1)
    }

    # Determine status (based on actual food ingredients, not equipment)
    total_food_ingredients = actual_ingredients
    missing_count = len(missing)

    if missing_count == 0:
        status = "complete"
    elif missing_count <= 2 or (total_food_ingredients > 0 and missing_count / total_food_ingredients <= 0.2):
        status = "partial"
    else:
        status = "insufficient_data"

    assumptions = [f"Calculated for {servings} servings"]
    if serving_inferred:
        category = recipe.get("category", "unknown")
        assumptions.append(f"Serving size inferred from {category} category")

    return {
        "status": status,
        "per_serving": per_serving,
        "missing_inputs": missing[:10] if len(missing) > 10 else missing,  # Limit to 10
        "assumptions": assumptions
    }


# =============================================================================
# MAIN PROCESSING
# =============================================================================

def process_all_recipes():
    """Process all recipe shards and add nutrition data."""
    shard_files = sorted(glob.glob('data/recipes-*.json'))

    total_processed = 0
    total_complete = 0
    total_partial = 0
    total_insufficient = 0

    for shard_file in shard_files:
        if 'index' in shard_file:
            continue

        print(f"\nProcessing {shard_file}...")

        with open(shard_file, 'r') as f:
            data = json.load(f)

        recipes = data.get('recipes', [])
        updated = 0

        for recipe in recipes:
            # Skip flagged non-recipe content
            if recipe.get('flagged_for_review'):
                continue

            # Skip if already has complete nutrition
            existing = recipe.get('nutrition', {})
            if existing.get('status') == 'complete':
                total_complete += 1
                continue

            # Calculate nutrition
            nutrition = calculate_recipe_nutrition(recipe, default_servings=4)
            recipe['nutrition'] = nutrition
            updated += 1
            total_processed += 1

            if nutrition['status'] == 'complete':
                total_complete += 1
            elif nutrition['status'] == 'partial':
                total_partial += 1
            else:
                total_insufficient += 1

        # Save updated shard
        with open(shard_file, 'w') as f:
            json.dump(data, f, indent=2)

        print(f"  Updated {updated} recipes")

    print(f"\n{'='*60}")
    print(f"NUTRITION PROCESSING COMPLETE")
    print(f"{'='*60}")
    print(f"Total processed: {total_processed}")
    print(f"Complete: {total_complete}")
    print(f"Partial: {total_partial}")
    print(f"Insufficient data: {total_insufficient}")

    return total_processed, total_complete, total_partial, total_insufficient


if __name__ == "__main__":
    process_all_recipes()