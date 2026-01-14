#!/usr/bin/env python3
"""
Nutrition Estimation Script for MomMom's Recipes

Estimates approximate nutritional values based on common ingredient data.
All estimates are rough approximations - marked as 'partial' with assumptions.
"""

import json
import re
from pathlib import Path

# Approximate nutrition per standard unit (calories, fat_g, protein_g, carbs_g)
# Sources: USDA FoodData Central approximations
NUTRITION_DB = {
    # Dairy
    'butter': {'per': '1 tbsp', 'cal': 102, 'fat': 11.5, 'protein': 0.1, 'carbs': 0},
    'margarine': {'per': '1 tbsp', 'cal': 100, 'fat': 11, 'protein': 0, 'carbs': 0},
    'milk': {'per': '1 cup', 'cal': 150, 'fat': 8, 'protein': 8, 'carbs': 12},
    'cream': {'per': '1 cup', 'cal': 820, 'fat': 88, 'protein': 5, 'carbs': 7},
    'heavy cream': {'per': '1 cup', 'cal': 820, 'fat': 88, 'protein': 5, 'carbs': 7},
    'sour cream': {'per': '1 cup', 'cal': 445, 'fat': 45, 'protein': 5, 'carbs': 8},
    'cream cheese': {'per': '1 oz', 'cal': 99, 'fat': 10, 'protein': 2, 'carbs': 1},
    'cheddar cheese': {'per': '1 oz', 'cal': 113, 'fat': 9, 'protein': 7, 'carbs': 0.4},
    'cheese': {'per': '1 oz', 'cal': 110, 'fat': 9, 'protein': 7, 'carbs': 1},
    'parmesan': {'per': '1 tbsp', 'cal': 22, 'fat': 1.4, 'protein': 2, 'carbs': 0.2},
    'egg': {'per': '1 large', 'cal': 72, 'fat': 5, 'protein': 6, 'carbs': 0.4},
    'eggs': {'per': '1 large', 'cal': 72, 'fat': 5, 'protein': 6, 'carbs': 0.4},
    'evaporated milk': {'per': '1 cup', 'cal': 338, 'fat': 19, 'protein': 17, 'carbs': 25},
    'condensed milk': {'per': '1 cup', 'cal': 982, 'fat': 27, 'protein': 24, 'carbs': 166},
    'yogurt': {'per': '1 cup', 'cal': 150, 'fat': 8, 'protein': 9, 'carbs': 11},

    # Fats & Oils
    'oil': {'per': '1 tbsp', 'cal': 120, 'fat': 14, 'protein': 0, 'carbs': 0},
    'vegetable oil': {'per': '1 tbsp', 'cal': 120, 'fat': 14, 'protein': 0, 'carbs': 0},
    'olive oil': {'per': '1 tbsp', 'cal': 119, 'fat': 13.5, 'protein': 0, 'carbs': 0},
    'shortening': {'per': '1 tbsp', 'cal': 113, 'fat': 13, 'protein': 0, 'carbs': 0},
    'lard': {'per': '1 tbsp', 'cal': 115, 'fat': 13, 'protein': 0, 'carbs': 0},
    'bacon grease': {'per': '1 tbsp', 'cal': 116, 'fat': 13, 'protein': 0, 'carbs': 0},

    # Sweeteners
    'sugar': {'per': '1 cup', 'cal': 774, 'fat': 0, 'protein': 0, 'carbs': 200},
    'brown sugar': {'per': '1 cup', 'cal': 836, 'fat': 0, 'protein': 0, 'carbs': 216},
    'powdered sugar': {'per': '1 cup', 'cal': 467, 'fat': 0, 'protein': 0, 'carbs': 119},
    'confectioners sugar': {'per': '1 cup', 'cal': 467, 'fat': 0, 'protein': 0, 'carbs': 119},
    'honey': {'per': '1 tbsp', 'cal': 64, 'fat': 0, 'protein': 0.1, 'carbs': 17},
    'molasses': {'per': '1 tbsp', 'cal': 58, 'fat': 0, 'protein': 0, 'carbs': 15},
    'corn syrup': {'per': '1 tbsp', 'cal': 57, 'fat': 0, 'protein': 0, 'carbs': 16},
    'maple syrup': {'per': '1 tbsp', 'cal': 52, 'fat': 0, 'protein': 0, 'carbs': 13},

    # Flours & Grains
    'flour': {'per': '1 cup', 'cal': 455, 'fat': 1.2, 'protein': 13, 'carbs': 95},
    'all-purpose flour': {'per': '1 cup', 'cal': 455, 'fat': 1.2, 'protein': 13, 'carbs': 95},
    'bread flour': {'per': '1 cup', 'cal': 495, 'fat': 2.3, 'protein': 16, 'carbs': 99},
    'whole wheat flour': {'per': '1 cup', 'cal': 407, 'fat': 2.2, 'protein': 16, 'carbs': 87},
    'cake flour': {'per': '1 cup', 'cal': 400, 'fat': 1, 'protein': 9, 'carbs': 85},
    'cornmeal': {'per': '1 cup', 'cal': 442, 'fat': 4.4, 'protein': 10, 'carbs': 94},
    'oats': {'per': '1 cup', 'cal': 307, 'fat': 5, 'protein': 11, 'carbs': 55},
    'oatmeal': {'per': '1 cup', 'cal': 307, 'fat': 5, 'protein': 11, 'carbs': 55},
    'rice': {'per': '1 cup', 'cal': 206, 'fat': 0.4, 'protein': 4, 'carbs': 45},
    'bread crumbs': {'per': '1 cup', 'cal': 427, 'fat': 6, 'protein': 14, 'carbs': 78},
    'cornstarch': {'per': '1 tbsp', 'cal': 31, 'fat': 0, 'protein': 0, 'carbs': 7},
    'biscuit mix': {'per': '1 cup', 'cal': 480, 'fat': 17, 'protein': 8, 'carbs': 72},

    # Proteins
    'chicken': {'per': '1 lb', 'cal': 750, 'fat': 42, 'protein': 86, 'carbs': 0},
    'chicken breast': {'per': '1 lb', 'cal': 500, 'fat': 11, 'protein': 93, 'carbs': 0},
    'ground beef': {'per': '1 lb', 'cal': 1152, 'fat': 88, 'protein': 80, 'carbs': 0},
    'beef': {'per': '1 lb', 'cal': 1000, 'fat': 70, 'protein': 80, 'carbs': 0},
    'pork': {'per': '1 lb', 'cal': 1000, 'fat': 72, 'protein': 80, 'carbs': 0},
    'ham': {'per': '1 lb', 'cal': 650, 'fat': 25, 'protein': 100, 'carbs': 4},
    'bacon': {'per': '1 slice', 'cal': 43, 'fat': 3.3, 'protein': 3, 'carbs': 0.1},
    'sausage': {'per': '1 lb', 'cal': 1200, 'fat': 100, 'protein': 60, 'carbs': 4},
    'tuna': {'per': '1 can', 'cal': 200, 'fat': 5, 'protein': 40, 'carbs': 0},
    'salmon': {'per': '1 lb', 'cal': 830, 'fat': 47, 'protein': 90, 'carbs': 0},
    'shrimp': {'per': '1 lb', 'cal': 480, 'fat': 8, 'protein': 92, 'carbs': 4},
    'crab': {'per': '1 lb', 'cal': 400, 'fat': 4, 'protein': 80, 'carbs': 0},

    # Vegetables
    'onion': {'per': '1 cup', 'cal': 64, 'fat': 0.2, 'protein': 2, 'carbs': 15},
    'onions': {'per': '1 cup', 'cal': 64, 'fat': 0.2, 'protein': 2, 'carbs': 15},
    'celery': {'per': '1 cup', 'cal': 16, 'fat': 0.2, 'protein': 0.7, 'carbs': 3},
    'carrot': {'per': '1 cup', 'cal': 52, 'fat': 0.3, 'protein': 1.2, 'carbs': 12},
    'carrots': {'per': '1 cup', 'cal': 52, 'fat': 0.3, 'protein': 1.2, 'carbs': 12},
    'potato': {'per': '1 medium', 'cal': 161, 'fat': 0.2, 'protein': 4, 'carbs': 37},
    'potatoes': {'per': '1 lb', 'cal': 350, 'fat': 0.4, 'protein': 9, 'carbs': 80},
    'tomato': {'per': '1 medium', 'cal': 22, 'fat': 0.2, 'protein': 1, 'carbs': 5},
    'tomatoes': {'per': '1 cup', 'cal': 32, 'fat': 0.4, 'protein': 1.6, 'carbs': 7},
    'green beans': {'per': '1 cup', 'cal': 31, 'fat': 0.1, 'protein': 2, 'carbs': 7},
    'corn': {'per': '1 cup', 'cal': 132, 'fat': 2, 'protein': 5, 'carbs': 29},
    'peas': {'per': '1 cup', 'cal': 117, 'fat': 0.6, 'protein': 8, 'carbs': 21},
    'spinach': {'per': '1 cup', 'cal': 7, 'fat': 0.1, 'protein': 0.9, 'carbs': 1},
    'lettuce': {'per': '1 cup', 'cal': 5, 'fat': 0.1, 'protein': 0.5, 'carbs': 1},
    'cabbage': {'per': '1 cup', 'cal': 22, 'fat': 0.1, 'protein': 1, 'carbs': 5},
    'mushrooms': {'per': '1 cup', 'cal': 15, 'fat': 0.2, 'protein': 2, 'carbs': 2},
    'bell pepper': {'per': '1 medium', 'cal': 24, 'fat': 0.2, 'protein': 1, 'carbs': 6},
    'garlic': {'per': '1 clove', 'cal': 4, 'fat': 0, 'protein': 0.2, 'carbs': 1},
    'broccoli': {'per': '1 cup', 'cal': 31, 'fat': 0.3, 'protein': 2.5, 'carbs': 6},
    'zucchini': {'per': '1 cup', 'cal': 19, 'fat': 0.2, 'protein': 1.4, 'carbs': 4},

    # Fruits
    'apple': {'per': '1 medium', 'cal': 95, 'fat': 0.3, 'protein': 0.5, 'carbs': 25},
    'banana': {'per': '1 medium', 'cal': 105, 'fat': 0.4, 'protein': 1.3, 'carbs': 27},
    'lemon juice': {'per': '1 tbsp', 'cal': 3, 'fat': 0, 'protein': 0.1, 'carbs': 1},
    'orange juice': {'per': '1 cup', 'cal': 112, 'fat': 0.5, 'protein': 2, 'carbs': 26},
    'raisins': {'per': '1 cup', 'cal': 434, 'fat': 0.7, 'protein': 5, 'carbs': 115},
    'dates': {'per': '1 cup', 'cal': 415, 'fat': 0.4, 'protein': 4, 'carbs': 110},
    'coconut': {'per': '1 cup', 'cal': 283, 'fat': 27, 'protein': 3, 'carbs': 12},
    'pineapple': {'per': '1 cup', 'cal': 82, 'fat': 0.2, 'protein': 0.9, 'carbs': 22},
    'strawberries': {'per': '1 cup', 'cal': 49, 'fat': 0.5, 'protein': 1, 'carbs': 12},
    'blueberries': {'per': '1 cup', 'cal': 84, 'fat': 0.5, 'protein': 1, 'carbs': 21},
    'cherries': {'per': '1 cup', 'cal': 87, 'fat': 0.3, 'protein': 1.5, 'carbs': 22},
    'peaches': {'per': '1 cup', 'cal': 60, 'fat': 0.4, 'protein': 1.4, 'carbs': 15},

    # Nuts
    'pecans': {'per': '1 cup', 'cal': 753, 'fat': 78, 'protein': 10, 'carbs': 15},
    'walnuts': {'per': '1 cup', 'cal': 765, 'fat': 76, 'protein': 18, 'carbs': 16},
    'almonds': {'per': '1 cup', 'cal': 828, 'fat': 72, 'protein': 30, 'carbs': 28},
    'peanuts': {'per': '1 cup', 'cal': 828, 'fat': 72, 'protein': 38, 'carbs': 24},
    'peanut butter': {'per': '1 tbsp', 'cal': 94, 'fat': 8, 'protein': 4, 'carbs': 3},

    # Canned goods
    'cream of mushroom soup': {'per': '1 can', 'cal': 260, 'fat': 18, 'protein': 4, 'carbs': 20},
    'cream of chicken soup': {'per': '1 can', 'cal': 280, 'fat': 18, 'protein': 6, 'carbs': 22},
    'cream of celery soup': {'per': '1 can', 'cal': 220, 'fat': 14, 'protein': 4, 'carbs': 18},
    'tomato soup': {'per': '1 can', 'cal': 180, 'fat': 4, 'protein': 4, 'carbs': 32},
    'tomato sauce': {'per': '1 cup', 'cal': 59, 'fat': 0.5, 'protein': 3, 'carbs': 13},
    'tomato paste': {'per': '1 tbsp', 'cal': 13, 'fat': 0.1, 'protein': 0.7, 'carbs': 3},

    # Baking
    'baking powder': {'per': '1 tsp', 'cal': 2, 'fat': 0, 'protein': 0, 'carbs': 1},
    'baking soda': {'per': '1 tsp', 'cal': 0, 'fat': 0, 'protein': 0, 'carbs': 0},
    'yeast': {'per': '1 packet', 'cal': 21, 'fat': 0.3, 'protein': 3, 'carbs': 3},
    'vanilla': {'per': '1 tsp', 'cal': 12, 'fat': 0, 'protein': 0, 'carbs': 0.5},
    'cocoa': {'per': '1 tbsp', 'cal': 12, 'fat': 0.7, 'protein': 1, 'carbs': 3},
    'chocolate chips': {'per': '1 cup', 'cal': 805, 'fat': 50, 'protein': 7, 'carbs': 92},
    'chocolate': {'per': '1 oz', 'cal': 155, 'fat': 9, 'protein': 2, 'carbs': 17},
    'gelatin': {'per': '1 packet', 'cal': 23, 'fat': 0, 'protein': 6, 'carbs': 0},
    'jello': {'per': '1 package', 'cal': 80, 'fat': 0, 'protein': 2, 'carbs': 19},

    # Condiments
    'mayonnaise': {'per': '1 tbsp', 'cal': 94, 'fat': 10, 'protein': 0.1, 'carbs': 0.1},
    'mustard': {'per': '1 tsp', 'cal': 3, 'fat': 0.2, 'protein': 0.2, 'carbs': 0.3},
    'ketchup': {'per': '1 tbsp', 'cal': 19, 'fat': 0, 'protein': 0.2, 'carbs': 5},
    'soy sauce': {'per': '1 tbsp', 'cal': 9, 'fat': 0, 'protein': 1, 'carbs': 1},
    'worcestershire sauce': {'per': '1 tbsp', 'cal': 13, 'fat': 0, 'protein': 0, 'carbs': 3},
    'vinegar': {'per': '1 tbsp', 'cal': 3, 'fat': 0, 'protein': 0, 'carbs': 0},
    'salad dressing': {'per': '1 tbsp', 'cal': 73, 'fat': 8, 'protein': 0.1, 'carbs': 1},
    'hot sauce': {'per': '1 tsp', 'cal': 1, 'fat': 0, 'protein': 0, 'carbs': 0},
    'tabasco': {'per': '1 tsp', 'cal': 1, 'fat': 0, 'protein': 0, 'carbs': 0},
    'pickle': {'per': '1 medium', 'cal': 7, 'fat': 0, 'protein': 0, 'carbs': 2},
    'pickles': {'per': '1 cup', 'cal': 17, 'fat': 0.3, 'protein': 0.5, 'carbs': 3},
    'relish': {'per': '1 tbsp', 'cal': 20, 'fat': 0, 'protein': 0, 'carbs': 5},
    'salsa': {'per': '1 cup', 'cal': 70, 'fat': 0, 'protein': 3, 'carbs': 14},
    'picante sauce': {'per': '1 cup', 'cal': 70, 'fat': 0, 'protein': 3, 'carbs': 14},

    # Beverages & Liquids
    'water': {'per': '1 cup', 'cal': 0, 'fat': 0, 'protein': 0, 'carbs': 0},
    'coffee': {'per': '1 cup', 'cal': 2, 'fat': 0, 'protein': 0, 'carbs': 0},
    'tea': {'per': '1 cup', 'cal': 2, 'fat': 0, 'protein': 0, 'carbs': 1},
    'wine': {'per': '1 cup', 'cal': 200, 'fat': 0, 'protein': 0, 'carbs': 4},
    'beer': {'per': '1 cup', 'cal': 103, 'fat': 0, 'protein': 1, 'carbs': 6},
    'rum': {'per': '1 oz', 'cal': 64, 'fat': 0, 'protein': 0, 'carbs': 0},
    'vodka': {'per': '1 oz', 'cal': 64, 'fat': 0, 'protein': 0, 'carbs': 0},
    'whiskey': {'per': '1 oz', 'cal': 70, 'fat': 0, 'protein': 0, 'carbs': 0},
    'bourbon': {'per': '1 oz', 'cal': 70, 'fat': 0, 'protein': 0, 'carbs': 0},
    'brandy': {'per': '1 oz', 'cal': 65, 'fat': 0, 'protein': 0, 'carbs': 0},
    'sherry': {'per': '1 oz', 'cal': 40, 'fat': 0, 'protein': 0, 'carbs': 2},
    'cola': {'per': '1 cup', 'cal': 97, 'fat': 0, 'protein': 0, 'carbs': 26},
    'soda': {'per': '1 cup', 'cal': 97, 'fat': 0, 'protein': 0, 'carbs': 26},
    'ginger ale': {'per': '1 cup', 'cal': 83, 'fat': 0, 'protein': 0, 'carbs': 21},
    'club soda': {'per': '1 cup', 'cal': 0, 'fat': 0, 'protein': 0, 'carbs': 0},
    'cranberry juice': {'per': '1 cup', 'cal': 116, 'fat': 0, 'protein': 0, 'carbs': 31},
    'apple juice': {'per': '1 cup', 'cal': 114, 'fat': 0, 'protein': 0, 'carbs': 28},
    'grape juice': {'per': '1 cup', 'cal': 152, 'fat': 0, 'protein': 1, 'carbs': 37},
    'lime juice': {'per': '1 tbsp', 'cal': 4, 'fat': 0, 'protein': 0, 'carbs': 1},
    'limeade': {'per': '1 cup', 'cal': 100, 'fat': 0, 'protein': 0, 'carbs': 26},
    'lemonade': {'per': '1 cup', 'cal': 99, 'fat': 0, 'protein': 0, 'carbs': 26},

    # More Vegetables
    'asparagus': {'per': '1 cup', 'cal': 27, 'fat': 0.2, 'protein': 3, 'carbs': 5},
    'artichoke': {'per': '1 medium', 'cal': 60, 'fat': 0.2, 'protein': 4, 'carbs': 13},
    'beets': {'per': '1 cup', 'cal': 58, 'fat': 0.2, 'protein': 2, 'carbs': 13},
    'brussels sprouts': {'per': '1 cup', 'cal': 56, 'fat': 0.8, 'protein': 4, 'carbs': 11},
    'cauliflower': {'per': '1 cup', 'cal': 25, 'fat': 0.3, 'protein': 2, 'carbs': 5},
    'cucumber': {'per': '1 cup', 'cal': 16, 'fat': 0.1, 'protein': 0.7, 'carbs': 4},
    'eggplant': {'per': '1 cup', 'cal': 35, 'fat': 0.2, 'protein': 1, 'carbs': 9},
    'kale': {'per': '1 cup', 'cal': 33, 'fat': 0.5, 'protein': 2, 'carbs': 6},
    'leek': {'per': '1 cup', 'cal': 54, 'fat': 0.3, 'protein': 1, 'carbs': 13},
    'okra': {'per': '1 cup', 'cal': 33, 'fat': 0.2, 'protein': 2, 'carbs': 7},
    'parsnips': {'per': '1 cup', 'cal': 100, 'fat': 0.4, 'protein': 2, 'carbs': 24},
    'pumpkin': {'per': '1 cup', 'cal': 49, 'fat': 0.2, 'protein': 2, 'carbs': 12},
    'radish': {'per': '1 cup', 'cal': 19, 'fat': 0.1, 'protein': 0.8, 'carbs': 4},
    'squash': {'per': '1 cup', 'cal': 41, 'fat': 0.4, 'protein': 1, 'carbs': 10},
    'sweet potato': {'per': '1 medium', 'cal': 103, 'fat': 0.1, 'protein': 2, 'carbs': 24},
    'turnip': {'per': '1 cup', 'cal': 36, 'fat': 0.1, 'protein': 1, 'carbs': 8},
    'watercress': {'per': '1 cup', 'cal': 4, 'fat': 0, 'protein': 0.8, 'carbs': 0.4},
    'green pepper': {'per': '1 medium', 'cal': 24, 'fat': 0.2, 'protein': 1, 'carbs': 6},
    'red pepper': {'per': '1 medium', 'cal': 37, 'fat': 0.4, 'protein': 1, 'carbs': 7},
    'jalapeno': {'per': '1 pepper', 'cal': 4, 'fat': 0, 'protein': 0.1, 'carbs': 1},
    'green onion': {'per': '1 cup', 'cal': 32, 'fat': 0.2, 'protein': 2, 'carbs': 7},
    'scallion': {'per': '1 cup', 'cal': 32, 'fat': 0.2, 'protein': 2, 'carbs': 7},
    'shallot': {'per': '1 tbsp', 'cal': 7, 'fat': 0, 'protein': 0.3, 'carbs': 2},

    # More Fruits
    'apricot': {'per': '1 cup', 'cal': 74, 'fat': 0.6, 'protein': 2, 'carbs': 17},
    'avocado': {'per': '1 medium', 'cal': 322, 'fat': 29, 'protein': 4, 'carbs': 17},
    'blackberries': {'per': '1 cup', 'cal': 62, 'fat': 0.7, 'protein': 2, 'carbs': 14},
    'cantaloupe': {'per': '1 cup', 'cal': 54, 'fat': 0.3, 'protein': 1, 'carbs': 13},
    'cranberries': {'per': '1 cup', 'cal': 46, 'fat': 0.1, 'protein': 0.4, 'carbs': 12},
    'figs': {'per': '1 cup', 'cal': 371, 'fat': 1.4, 'protein': 5, 'carbs': 95},
    'grapefruit': {'per': '1 medium', 'cal': 82, 'fat': 0.3, 'protein': 2, 'carbs': 21},
    'grapes': {'per': '1 cup', 'cal': 104, 'fat': 0.2, 'protein': 1, 'carbs': 27},
    'honeydew': {'per': '1 cup', 'cal': 61, 'fat': 0.2, 'protein': 0.9, 'carbs': 15},
    'kiwi': {'per': '1 medium', 'cal': 42, 'fat': 0.4, 'protein': 0.8, 'carbs': 10},
    'lemon': {'per': '1 medium', 'cal': 17, 'fat': 0.2, 'protein': 0.6, 'carbs': 5},
    'lime': {'per': '1 medium', 'cal': 20, 'fat': 0.1, 'protein': 0.5, 'carbs': 7},
    'mango': {'per': '1 cup', 'cal': 99, 'fat': 0.6, 'protein': 1, 'carbs': 25},
    'melon': {'per': '1 cup', 'cal': 54, 'fat': 0.3, 'protein': 1, 'carbs': 13},
    'nectarine': {'per': '1 medium', 'cal': 62, 'fat': 0.5, 'protein': 2, 'carbs': 15},
    'orange': {'per': '1 medium', 'cal': 62, 'fat': 0.2, 'protein': 1, 'carbs': 15},
    'papaya': {'per': '1 cup', 'cal': 55, 'fat': 0.2, 'protein': 0.9, 'carbs': 14},
    'pear': {'per': '1 medium', 'cal': 101, 'fat': 0.2, 'protein': 0.6, 'carbs': 27},
    'plum': {'per': '1 medium', 'cal': 30, 'fat': 0.2, 'protein': 0.5, 'carbs': 8},
    'prunes': {'per': '1 cup', 'cal': 418, 'fat': 0.7, 'protein': 4, 'carbs': 111},
    'raspberries': {'per': '1 cup', 'cal': 64, 'fat': 0.8, 'protein': 1.5, 'carbs': 15},
    'watermelon': {'per': '1 cup', 'cal': 46, 'fat': 0.2, 'protein': 0.9, 'carbs': 12},

    # More Proteins
    'turkey': {'per': '1 lb', 'cal': 560, 'fat': 12, 'protein': 104, 'carbs': 0},
    'lamb': {'per': '1 lb', 'cal': 1100, 'fat': 80, 'protein': 84, 'carbs': 0},
    'veal': {'per': '1 lb', 'cal': 560, 'fat': 20, 'protein': 92, 'carbs': 0},
    'duck': {'per': '1 lb', 'cal': 600, 'fat': 32, 'protein': 76, 'carbs': 0},
    'liver': {'per': '1 lb', 'cal': 550, 'fat': 14, 'protein': 100, 'carbs': 16},
    'hot dog': {'per': '1 link', 'cal': 150, 'fat': 13, 'protein': 5, 'carbs': 2},
    'pepperoni': {'per': '1 oz', 'cal': 138, 'fat': 12, 'protein': 6, 'carbs': 1},
    'corned beef': {'per': '1 lb', 'cal': 700, 'fat': 40, 'protein': 80, 'carbs': 0},
    'ground turkey': {'per': '1 lb', 'cal': 680, 'fat': 36, 'protein': 84, 'carbs': 0},
    'ground pork': {'per': '1 lb', 'cal': 1200, 'fat': 100, 'protein': 68, 'carbs': 0},

    # More Seafood
    'cod': {'per': '1 lb', 'cal': 370, 'fat': 3, 'protein': 80, 'carbs': 0},
    'tilapia': {'per': '1 lb', 'cal': 430, 'fat': 9, 'protein': 92, 'carbs': 0},
    'halibut': {'per': '1 lb', 'cal': 500, 'fat': 10, 'protein': 96, 'carbs': 0},
    'catfish': {'per': '1 lb', 'cal': 460, 'fat': 12, 'protein': 80, 'carbs': 0},
    'trout': {'per': '1 lb', 'cal': 580, 'fat': 24, 'protein': 84, 'carbs': 0},
    'lobster': {'per': '1 lb', 'cal': 440, 'fat': 4, 'protein': 92, 'carbs': 0},
    'scallops': {'per': '1 lb', 'cal': 400, 'fat': 4, 'protein': 76, 'carbs': 12},
    'oysters': {'per': '1 cup', 'cal': 170, 'fat': 6, 'protein': 18, 'carbs': 10},
    'clams': {'per': '1 cup', 'cal': 168, 'fat': 2, 'protein': 29, 'carbs': 6},
    'mussels': {'per': '1 cup', 'cal': 172, 'fat': 5, 'protein': 24, 'carbs': 8},
    'anchovies': {'per': '1 oz', 'cal': 37, 'fat': 1.4, 'protein': 6, 'carbs': 0},
    'sardines': {'per': '1 can', 'cal': 190, 'fat': 11, 'protein': 23, 'carbs': 0},
    'fish': {'per': '1 lb', 'cal': 450, 'fat': 10, 'protein': 80, 'carbs': 0},

    # Legumes & Beans
    'black beans': {'per': '1 cup', 'cal': 227, 'fat': 0.9, 'protein': 15, 'carbs': 41},
    'kidney beans': {'per': '1 cup', 'cal': 225, 'fat': 0.9, 'protein': 15, 'carbs': 40},
    'pinto beans': {'per': '1 cup', 'cal': 245, 'fat': 1.1, 'protein': 15, 'carbs': 45},
    'navy beans': {'per': '1 cup', 'cal': 255, 'fat': 1.1, 'protein': 15, 'carbs': 47},
    'lima beans': {'per': '1 cup', 'cal': 216, 'fat': 0.7, 'protein': 15, 'carbs': 39},
    'chickpeas': {'per': '1 cup', 'cal': 269, 'fat': 4.3, 'protein': 15, 'carbs': 45},
    'garbanzo beans': {'per': '1 cup', 'cal': 269, 'fat': 4.3, 'protein': 15, 'carbs': 45},
    'lentils': {'per': '1 cup', 'cal': 230, 'fat': 0.8, 'protein': 18, 'carbs': 40},
    'split peas': {'per': '1 cup', 'cal': 231, 'fat': 0.8, 'protein': 16, 'carbs': 41},
    'refried beans': {'per': '1 cup', 'cal': 237, 'fat': 3, 'protein': 14, 'carbs': 39},
    'baked beans': {'per': '1 cup', 'cal': 392, 'fat': 13, 'protein': 14, 'carbs': 54},
    'tofu': {'per': '1 cup', 'cal': 188, 'fat': 12, 'protein': 20, 'carbs': 5},

    # More Dairy
    'buttermilk': {'per': '1 cup', 'cal': 99, 'fat': 2.2, 'protein': 8, 'carbs': 12},
    'cottage cheese': {'per': '1 cup', 'cal': 220, 'fat': 10, 'protein': 28, 'carbs': 6},
    'ricotta': {'per': '1 cup', 'cal': 428, 'fat': 32, 'protein': 28, 'carbs': 8},
    'mozzarella': {'per': '1 oz', 'cal': 85, 'fat': 6, 'protein': 6, 'carbs': 1},
    'swiss cheese': {'per': '1 oz', 'cal': 108, 'fat': 8, 'protein': 8, 'carbs': 2},
    'american cheese': {'per': '1 slice', 'cal': 104, 'fat': 9, 'protein': 5, 'carbs': 1},
    'blue cheese': {'per': '1 oz', 'cal': 100, 'fat': 8, 'protein': 6, 'carbs': 1},
    'feta cheese': {'per': '1 oz', 'cal': 75, 'fat': 6, 'protein': 4, 'carbs': 1},
    'goat cheese': {'per': '1 oz', 'cal': 76, 'fat': 6, 'protein': 5, 'carbs': 0},
    'ice cream': {'per': '1 cup', 'cal': 274, 'fat': 15, 'protein': 5, 'carbs': 31},
    'whipped cream': {'per': '1 cup', 'cal': 400, 'fat': 42, 'protein': 2, 'carbs': 3},
    'cool whip': {'per': '1 cup', 'cal': 200, 'fat': 13, 'protein': 0, 'carbs': 17},
    'half and half': {'per': '1 cup', 'cal': 315, 'fat': 28, 'protein': 7, 'carbs': 10},
    'whipping cream': {'per': '1 cup', 'cal': 820, 'fat': 88, 'protein': 5, 'carbs': 7},

    # More Grains & Starches
    'pasta': {'per': '1 cup', 'cal': 220, 'fat': 1.3, 'protein': 8, 'carbs': 43},
    'noodles': {'per': '1 cup', 'cal': 220, 'fat': 3, 'protein': 8, 'carbs': 40},
    'egg noodles': {'per': '1 cup', 'cal': 220, 'fat': 3, 'protein': 8, 'carbs': 40},
    'spaghetti': {'per': '1 cup', 'cal': 220, 'fat': 1.3, 'protein': 8, 'carbs': 43},
    'macaroni': {'per': '1 cup', 'cal': 220, 'fat': 1.3, 'protein': 8, 'carbs': 43},
    'crackers': {'per': '1 oz', 'cal': 130, 'fat': 4, 'protein': 3, 'carbs': 22},
    'graham crackers': {'per': '1 sheet', 'cal': 59, 'fat': 1.4, 'protein': 1, 'carbs': 11},
    'tortilla': {'per': '1 medium', 'cal': 90, 'fat': 2.5, 'protein': 2, 'carbs': 15},
    'bread': {'per': '1 slice', 'cal': 79, 'fat': 1, 'protein': 3, 'carbs': 15},
    'bun': {'per': '1 bun', 'cal': 120, 'fat': 2, 'protein': 4, 'carbs': 22},
    'roll': {'per': '1 roll', 'cal': 87, 'fat': 2, 'protein': 3, 'carbs': 15},
    'croutons': {'per': '1 cup', 'cal': 122, 'fat': 2, 'protein': 4, 'carbs': 22},
    'stuffing mix': {'per': '1 cup', 'cal': 350, 'fat': 15, 'protein': 6, 'carbs': 45},
    'cereal': {'per': '1 cup', 'cal': 120, 'fat': 1, 'protein': 3, 'carbs': 26},
    'corn flakes': {'per': '1 cup', 'cal': 100, 'fat': 0, 'protein': 2, 'carbs': 24},
    'wheat germ': {'per': '1 tbsp', 'cal': 26, 'fat': 0.7, 'protein': 2, 'carbs': 4},
    'bran': {'per': '1 cup', 'cal': 125, 'fat': 3, 'protein': 9, 'carbs': 37},
    'wild rice': {'per': '1 cup', 'cal': 166, 'fat': 0.6, 'protein': 7, 'carbs': 35},
    'barley': {'per': '1 cup', 'cal': 193, 'fat': 0.7, 'protein': 4, 'carbs': 44},
    'couscous': {'per': '1 cup', 'cal': 176, 'fat': 0.3, 'protein': 6, 'carbs': 36},
    'quinoa': {'per': '1 cup', 'cal': 222, 'fat': 4, 'protein': 8, 'carbs': 39},
    'grits': {'per': '1 cup', 'cal': 143, 'fat': 0.5, 'protein': 3, 'carbs': 31},
    'polenta': {'per': '1 cup', 'cal': 145, 'fat': 0.6, 'protein': 3, 'carbs': 31},

    # More Canned Goods
    'canned tomatoes': {'per': '1 can', 'cal': 80, 'fat': 0, 'protein': 4, 'carbs': 16},
    'diced tomatoes': {'per': '1 can', 'cal': 80, 'fat': 0, 'protein': 4, 'carbs': 16},
    'crushed tomatoes': {'per': '1 can', 'cal': 80, 'fat': 0, 'protein': 4, 'carbs': 16},
    'stewed tomatoes': {'per': '1 can', 'cal': 80, 'fat': 0, 'protein': 4, 'carbs': 16},
    'rotel': {'per': '1 can', 'cal': 50, 'fat': 0, 'protein': 2, 'carbs': 10},
    'enchilada sauce': {'per': '1 cup', 'cal': 80, 'fat': 3, 'protein': 2, 'carbs': 12},
    'green chilies': {'per': '1 can', 'cal': 30, 'fat': 0, 'protein': 1, 'carbs': 6},
    'bamboo shoots': {'per': '1 cup', 'cal': 25, 'fat': 0, 'protein': 2, 'carbs': 4},
    'water chestnuts': {'per': '1 cup', 'cal': 60, 'fat': 0, 'protein': 1, 'carbs': 15},
    'olives': {'per': '1 cup', 'cal': 145, 'fat': 15, 'protein': 1, 'carbs': 4},
    'sauerkraut': {'per': '1 cup', 'cal': 27, 'fat': 0, 'protein': 1, 'carbs': 6},
    'pumpkin puree': {'per': '1 cup', 'cal': 83, 'fat': 0.7, 'protein': 3, 'carbs': 20},
    'pie filling': {'per': '1 cup', 'cal': 300, 'fat': 0, 'protein': 1, 'carbs': 75},
    'fruit cocktail': {'per': '1 cup', 'cal': 181, 'fat': 0, 'protein': 1, 'carbs': 47},
    'mandarin oranges': {'per': '1 cup', 'cal': 154, 'fat': 0, 'protein': 2, 'carbs': 40},
    'pineapple chunks': {'per': '1 cup', 'cal': 150, 'fat': 0, 'protein': 1, 'carbs': 39},
    'coconut milk': {'per': '1 cup', 'cal': 445, 'fat': 48, 'protein': 5, 'carbs': 6},

    # Spices & Seasonings (mostly negligible calories but included for matching)
    'salt': {'per': '1 tsp', 'cal': 0, 'fat': 0, 'protein': 0, 'carbs': 0},
    'pepper': {'per': '1 tsp', 'cal': 6, 'fat': 0.1, 'protein': 0.2, 'carbs': 2},
    'cinnamon': {'per': '1 tsp', 'cal': 6, 'fat': 0, 'protein': 0.1, 'carbs': 2},
    'nutmeg': {'per': '1 tsp', 'cal': 12, 'fat': 0.8, 'protein': 0.1, 'carbs': 1},
    'ginger': {'per': '1 tsp', 'cal': 6, 'fat': 0.1, 'protein': 0.2, 'carbs': 1},
    'paprika': {'per': '1 tsp', 'cal': 6, 'fat': 0.3, 'protein': 0.3, 'carbs': 1},
    'cumin': {'per': '1 tsp', 'cal': 8, 'fat': 0.5, 'protein': 0.4, 'carbs': 1},
    'oregano': {'per': '1 tsp', 'cal': 5, 'fat': 0.2, 'protein': 0.2, 'carbs': 1},
    'basil': {'per': '1 tsp', 'cal': 1, 'fat': 0, 'protein': 0.1, 'carbs': 0.1},
    'thyme': {'per': '1 tsp', 'cal': 4, 'fat': 0.1, 'protein': 0.1, 'carbs': 1},
    'rosemary': {'per': '1 tsp', 'cal': 4, 'fat': 0.2, 'protein': 0.1, 'carbs': 1},
    'sage': {'per': '1 tsp', 'cal': 2, 'fat': 0.1, 'protein': 0.1, 'carbs': 0.4},
    'bay leaf': {'per': '1 leaf', 'cal': 2, 'fat': 0, 'protein': 0, 'carbs': 0},
    'tarragon': {'per': '1 tsp', 'cal': 5, 'fat': 0.1, 'protein': 0.4, 'carbs': 1},
    'parsley': {'per': '1 tbsp', 'cal': 1, 'fat': 0, 'protein': 0.1, 'carbs': 0.2},
    'cilantro': {'per': '1 tbsp', 'cal': 0, 'fat': 0, 'protein': 0, 'carbs': 0},
    'dill': {'per': '1 tsp', 'cal': 3, 'fat': 0.1, 'protein': 0.2, 'carbs': 0.6},
    'chives': {'per': '1 tbsp', 'cal': 1, 'fat': 0, 'protein': 0.1, 'carbs': 0.1},
    'mint': {'per': '1 tbsp', 'cal': 1, 'fat': 0, 'protein': 0.1, 'carbs': 0.1},
    'chili powder': {'per': '1 tsp', 'cal': 8, 'fat': 0.4, 'protein': 0.3, 'carbs': 1},
    'curry powder': {'per': '1 tsp', 'cal': 7, 'fat': 0.3, 'protein': 0.3, 'carbs': 1},
    'allspice': {'per': '1 tsp', 'cal': 5, 'fat': 0.2, 'protein': 0.1, 'carbs': 1},
    'cloves': {'per': '1 tsp', 'cal': 7, 'fat': 0.4, 'protein': 0.1, 'carbs': 1},
    'cardamom': {'per': '1 tsp', 'cal': 6, 'fat': 0.1, 'protein': 0.2, 'carbs': 1},
    'cayenne': {'per': '1 tsp', 'cal': 6, 'fat': 0.3, 'protein': 0.2, 'carbs': 1},
    'turmeric': {'per': '1 tsp', 'cal': 8, 'fat': 0.2, 'protein': 0.3, 'carbs': 1},
    'bouillon': {'per': '1 cube', 'cal': 10, 'fat': 0.5, 'protein': 1, 'carbs': 1},
    'chicken bouillon': {'per': '1 cube', 'cal': 10, 'fat': 0.5, 'protein': 1, 'carbs': 1},
    'beef bouillon': {'per': '1 cube', 'cal': 10, 'fat': 0.5, 'protein': 1, 'carbs': 1},
    'broth': {'per': '1 cup', 'cal': 15, 'fat': 0.5, 'protein': 2, 'carbs': 1},
    'chicken broth': {'per': '1 cup', 'cal': 15, 'fat': 0.5, 'protein': 2, 'carbs': 1},
    'beef broth': {'per': '1 cup', 'cal': 17, 'fat': 0.5, 'protein': 3, 'carbs': 0},
    'vegetable broth': {'per': '1 cup', 'cal': 12, 'fat': 0, 'protein': 1, 'carbs': 2},

    # More Nuts & Seeds
    'cashews': {'per': '1 cup', 'cal': 786, 'fat': 63, 'protein': 21, 'carbs': 45},
    'macadamia': {'per': '1 cup', 'cal': 962, 'fat': 102, 'protein': 11, 'carbs': 19},
    'pine nuts': {'per': '1 cup', 'cal': 909, 'fat': 92, 'protein': 18, 'carbs': 18},
    'hazelnuts': {'per': '1 cup', 'cal': 848, 'fat': 82, 'protein': 20, 'carbs': 23},
    'pistachios': {'per': '1 cup', 'cal': 691, 'fat': 56, 'protein': 26, 'carbs': 34},
    'sunflower seeds': {'per': '1 cup', 'cal': 818, 'fat': 72, 'protein': 29, 'carbs': 28},
    'sesame seeds': {'per': '1 tbsp', 'cal': 52, 'fat': 5, 'protein': 2, 'carbs': 2},
    'poppy seeds': {'per': '1 tbsp', 'cal': 46, 'fat': 4, 'protein': 2, 'carbs': 2},
    'flax seeds': {'per': '1 tbsp', 'cal': 37, 'fat': 3, 'protein': 1, 'carbs': 2},
    'chia seeds': {'per': '1 tbsp', 'cal': 58, 'fat': 4, 'protein': 2, 'carbs': 5},
    'almond butter': {'per': '1 tbsp', 'cal': 98, 'fat': 9, 'protein': 3, 'carbs': 3},
    'tahini': {'per': '1 tbsp', 'cal': 89, 'fat': 8, 'protein': 3, 'carbs': 3},
}

# Standard can/jar sizes (in cups or units as appropriate)
# These are typical US sizes used when can/jar size isn't specified
STANDARD_CAN_SIZES = {
    # Soups - typically 10.5-10.75 oz condensed
    'cream of mushroom soup': 1.25,  # cups when prepared
    'cream of chicken soup': 1.25,
    'cream of celery soup': 1.25,
    'tomato soup': 1.25,
    'soup': 1.5,  # generic soup can

    # Vegetables/fruits - typically 14.5-15 oz
    'tomatoes': 1.75,
    'diced tomatoes': 1.75,
    'crushed tomatoes': 1.75,
    'tomato sauce': 1.0,  # 8 oz can
    'beans': 1.75,
    'corn': 1.75,
    'peas': 1.75,
    'green beans': 1.75,
    'pumpkin': 1.875,  # 15 oz
    'fruit cocktail': 1.875,
    'pineapple': 1.5,
    'mandarin oranges': 1.375,  # 11 oz
    'olives': 0.75,  # 6 oz
    'green chilies': 0.5,  # 4 oz
    'rotel': 1.25,  # 10 oz

    # Seafood
    'tuna': 1.0,  # 5-6 oz drained
    'salmon': 1.75,  # 14.75 oz
    'crab': 0.75,  # 6 oz
    'shrimp': 0.5,  # 4 oz small can
    'clams': 0.8,  # 6.5 oz

    # Dairy
    'evaporated milk': 1.5,  # 12 oz
    'condensed milk': 1.25,  # 14 oz

    # Other
    'broth': 1.75,  # 14 oz
    'chicken broth': 1.75,
    'beef broth': 1.75,
    'coconut milk': 1.75,  # 13.5 oz
}

# Standard jar sizes (in cups)
STANDARD_JAR_SIZES = {
    'salsa': 2.0,  # 16 oz
    'picante sauce': 2.0,
    'spaghetti sauce': 3.0,  # 24 oz
    'pasta sauce': 3.0,
    'marinara': 3.0,
    'alfredo sauce': 2.0,
    'peanut butter': 2.0,  # 16 oz
    'jelly': 1.5,  # 12 oz
    'jam': 1.5,
    'mayonnaise': 2.0,
    'pickles': 2.0,
    'relish': 1.0,  # 8 oz
    'mustard': 1.0,
    'applesauce': 3.0,  # 24 oz
    'maraschino cherries': 0.625,  # 10 oz with liquid
}

# Default quantities when not specified (by ingredient type)
DEFAULT_QUANTITIES = {
    # Proteins (typically 1 lb for main dishes)
    'chicken': 1.0,
    'beef': 1.0,
    'pork': 1.0,
    'ground beef': 1.0,
    'ground turkey': 1.0,
    'ham': 0.5,
    'bacon': 6,  # slices
    'sausage': 1.0,
    'fish': 1.0,
    'shrimp': 1.0,
    'crab': 0.5,

    # Dairy
    'egg': 2,
    'eggs': 2,
    'milk': 1.0,  # cup
    'butter': 2,  # tbsp
    'cheese': 1.0,  # cup shredded
    'cream cheese': 8,  # oz (1 package)
    'sour cream': 1.0,  # cup

    # Vegetables (typically 1 cup or 1 medium)
    'onion': 1.0,
    'garlic': 2,  # cloves
    'celery': 0.5,  # cup
    'carrot': 1.0,
    'potato': 2,  # medium
    'tomato': 1,
    'bell pepper': 1,
    'mushrooms': 1.0,  # cup

    # Pantry staples
    'flour': 2.0,  # cups for baking
    'sugar': 1.0,  # cup
    'oil': 2,  # tbsp
    'salt': 1,  # tsp
    'pepper': 0.25,  # tsp
}

# Unit conversions to standard
UNIT_CONVERSIONS = {
    # Volume
    'cup': 1.0,
    'cups': 1.0,
    'c': 1.0,
    'tbsp': 0.0625,  # 1/16 cup
    'tablespoon': 0.0625,
    'tablespoons': 0.0625,
    'tbs': 0.0625,
    'tsp': 0.0208,  # 1/48 cup
    'teaspoon': 0.0208,
    'teaspoons': 0.0208,
    't': 0.0208,
    'oz': 0.125,  # 1/8 cup
    'ounce': 0.125,
    'ounces': 0.125,
    'lb': 1.0,  # handled separately
    'lbs': 1.0,
    'pound': 1.0,
    'pounds': 1.0,
    'can': 1.0,  # handled as unit
    'cans': 1.0,
    'package': 1.0,
    'packages': 1.0,
    'pkg': 1.0,
    'stick': 8.0,  # 8 tbsp = 1 stick butter
    'sticks': 8.0,
    'large': 1.0,  # for eggs
    'medium': 1.0,
    'small': 0.75,
    'clove': 1.0,
    'cloves': 1.0,
    'slice': 1.0,
    'slices': 1.0,
    'piece': 1.0,
    'pieces': 1.0,
    'packet': 1.0,
    'envelope': 1.0,
}

def parse_fraction(s):
    """Parse a fraction string to float."""
    s = s.strip()
    if not s:
        return None

    # Handle mixed fractions like "1 1/2"
    parts = s.split()
    total = 0
    for part in parts:
        if '/' in part:
            try:
                num, denom = part.split('/')
                total += float(num) / float(denom)
            except:
                return None
        else:
            try:
                total += float(part)
            except:
                return None
    return total if total > 0 else None

def find_ingredient_match(item):
    """Find the best match for an ingredient in our database."""
    item_lower = item.lower()

    # Direct match
    if item_lower in NUTRITION_DB:
        return item_lower

    # Check if any DB key is in the item
    for key in sorted(NUTRITION_DB.keys(), key=len, reverse=True):
        if key in item_lower:
            return key

    return None

def estimate_servings(recipe):
    """Try to estimate servings from yield field."""
    servings = recipe.get('servings_yield', '')
    if not servings:
        return None

    # Look for numbers
    match = re.search(r'(\d+)', str(servings))
    if match:
        num = int(match.group(1))
        # Reasonable serving range
        if 1 <= num <= 100:
            return num
    return None

def calculate_recipe_nutrition(recipe):
    """Calculate nutrition for a single recipe."""
    ingredients = recipe.get('ingredients', [])
    if not ingredients:
        return None, ['No ingredients listed']

    total_cal = 0
    total_fat = 0
    total_protein = 0
    total_carbs = 0
    matched = 0
    missing = []
    assumptions = []

    for ing in ingredients:
        item = ing.get('item', '')
        quantity = ing.get('quantity', '')
        unit = ing.get('unit', '')

        # Skip unclear items
        if '[UNCLEAR]' in item or '[UNCLEAR]' in str(quantity):
            missing.append(f"Unclear: {item}")
            continue

        # Find ingredient in database
        match = find_ingredient_match(item)
        if not match:
            missing.append(f"Not in database: {item}")
            continue

        # Parse quantity
        qty = parse_fraction(str(quantity))
        if qty is None:
            # Try to extract number from quantity string
            match_num = re.search(r'[\d./]+', str(quantity))
            if match_num:
                qty = parse_fraction(match_num.group())
            else:
                # Try to infer from DEFAULT_QUANTITIES
                item_lower = item.lower()
                default_found = False
                for default_item, default_qty in DEFAULT_QUANTITIES.items():
                    if default_item in item_lower or item_lower in default_item:
                        qty = default_qty
                        assumptions.append(f"Inferred {qty} for {item} (standard quantity)")
                        default_found = True
                        break
                if not default_found:
                    qty = 1  # Fallback assumption
                    assumptions.append(f"Assumed 1 unit for {item}")

        # Get nutrition data
        nut_data = NUTRITION_DB[match]

        # Calculate multiplier based on unit
        multiplier = qty
        unit_lower = unit.lower() if unit else ''

        # Handle can/jar sizes when no specific size given
        if unit_lower in ['can', 'cans']:
            # Look up standard can size for this ingredient
            item_lower = item.lower()
            can_size = None
            for can_item, size in STANDARD_CAN_SIZES.items():
                if can_item in item_lower or item_lower in can_item:
                    can_size = size
                    break
            if can_size:
                multiplier = qty * can_size
                assumptions.append(f"Used standard can size ({can_size} cups) for {item}")
            else:
                multiplier = qty * 1.5  # Default 12oz can
                assumptions.append(f"Assumed 1.5 cup can for {item}")
        elif unit_lower in ['jar', 'jars']:
            # Look up standard jar size
            item_lower = item.lower()
            jar_size = None
            for jar_item, size in STANDARD_JAR_SIZES.items():
                if jar_item in item_lower or item_lower in jar_item:
                    jar_size = size
                    break
            if jar_size:
                multiplier = qty * jar_size
                assumptions.append(f"Used standard jar size ({jar_size} cups) for {item}")
            else:
                multiplier = qty * 2.0  # Default 16oz jar
                assumptions.append(f"Assumed 2 cup jar for {item}")
        # Handle special cases
        elif match in ['butter', 'margarine'] and unit_lower in ['stick', 'sticks']:
            multiplier = qty * 8  # 8 tbsp per stick
        elif match in ['egg', 'eggs']:
            multiplier = qty  # per egg
        elif unit_lower in UNIT_CONVERSIONS:
            # Very rough conversion
            multiplier = qty * UNIT_CONVERSIONS.get(unit_lower, 1)

        total_cal += nut_data['cal'] * multiplier
        total_fat += nut_data['fat'] * multiplier
        total_protein += nut_data['protein'] * multiplier
        total_carbs += nut_data['carbs'] * multiplier
        matched += 1

    if matched == 0:
        return None, missing

    # Get servings
    servings = estimate_servings(recipe)
    if servings is None:
        # Estimate based on total calories
        if total_cal > 4000:
            servings = 12
        elif total_cal > 2000:
            servings = 8
        elif total_cal > 1000:
            servings = 6
        else:
            servings = 4
        assumptions.append(f"Estimated {servings} servings based on total calories")

    per_serving = {
        'calories': round(total_cal / servings),
        'fat_g': round(total_fat / servings, 1),
        'protein_g': round(total_protein / servings, 1),
        'carbs_g': round(total_carbs / servings, 1)
    }

    coverage = matched / len(ingredients) * 100
    assumptions.append(f"Based on {matched}/{len(ingredients)} ingredients ({coverage:.0f}% coverage)")

    return per_serving, assumptions, missing

def process_recipes(dry_run=False):
    """Process all recipes needing nutrition data."""
    recipes_path = Path('data/recipes.json')

    with open(recipes_path) as f:
        data = json.load(f)

    recipes = data.get('recipes', [])
    non_food_categories = ['tips', 'basics', 'reference']

    updated = 0
    insufficient = 0

    for recipe in recipes:
        # Skip non-food categories
        if recipe.get('category') in non_food_categories:
            continue

        # Skip if already has complete nutrition
        nut = recipe.get('nutrition', {})
        if nut.get('status') in ['complete']:
            continue

        # Skip if already marked insufficient
        if nut.get('status') == 'insufficient_data':
            continue

        # Calculate nutrition
        result = calculate_recipe_nutrition(recipe)

        if result is None or result[0] is None:
            # Insufficient data
            missing = result[1] if result else ['Unable to parse ingredients']
            recipe['nutrition'] = {
                'status': 'insufficient_data',
                'per_serving': {},
                'missing_inputs': missing[:5],  # Limit to 5
                'assumptions': []
            }
            insufficient += 1
        else:
            per_serving, assumptions, missing = result

            # Determine status based on coverage
            if missing and len(missing) > len(recipe.get('ingredients', [])) / 2:
                status = 'partial'
            else:
                status = 'partial'  # Always partial for estimates

            recipe['nutrition'] = {
                'status': status,
                'per_serving': per_serving,
                'missing_inputs': missing[:3] if missing else [],
                'assumptions': assumptions[:5]
            }
            updated += 1

    if not dry_run:
        with open(recipes_path, 'w') as f:
            json.dump(data, f, indent=2)

    return updated, insufficient

if __name__ == '__main__':
    import sys

    dry_run = '--dry-run' in sys.argv

    if dry_run:
        print("DRY RUN - no changes will be saved")

    updated, insufficient = process_recipes(dry_run=dry_run)

    print(f"Updated with estimates: {updated}")
    print(f"Marked insufficient: {insufficient}")

    if not dry_run:
        print("\nNutrition estimates saved to data/recipes.json")
