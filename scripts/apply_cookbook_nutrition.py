#!/usr/bin/env python3
"""Apply nutrition data from Better Homes and Gardens cookbook nutrition analysis tables."""

import json
import re

# Nutrition data extracted from cookbook photos
# Format: recipe_name: {servings, calories, protein, carbs, fat, cholesterol, sodium}

CANDY_NUTRITION = {
    "caramel apples": {"servings": 14, "calories": 439, "carbs_g": 68, "fat_g": 20, "protein_g": 23, "sodium_mg": 132, "cholesterol_mg": 292},
    "caramel corn": {"servings": 9, "calories": 169, "protein_g": 1, "carbs_g": 27, "fat_g": 7, "sodium_mg": 4, "cholesterol_mg": 42},
    "caramels": {"servings": 30, "calories": 85, "protein_g": 0, "carbs_g": 8, "fat_g": 6, "sodium_mg": 3, "cholesterol_mg": 14},
    "caramel snappers": {"servings": 30, "calories": 60, "protein_g": 1, "carbs_g": 4, "fat_g": 4, "sodium_mg": 0, "cholesterol_mg": 19},
    "chocolate-covered cherries": {"servings": 60, "calories": 40, "protein_g": 4, "carbs_g": 1, "fat_g": 4, "sodium_mg": 4, "cholesterol_mg": 39},
    "chocolate-dipped fruit": {"servings": 50, "calories": 29, "protein_g": 0, "carbs_g": 4, "fat_g": 4, "sodium_mg": 1, "cholesterol_mg": 77},
    "chocolate pralines": {"servings": 36, "calories": 139, "protein_g": 1, "carbs_g": 9, "fat_g": 8, "sodium_mg": 12, "cholesterol_mg": 5},
    "cream cheese mints": {"servings": 40, "calories": 67, "protein_g": 0, "carbs_g": 7, "fat_g": 17, "sodium_mg": 0, "cholesterol_mg": 5},
    "divinity": {"servings": 24, "calories": 69, "protein_g": 0, "carbs_g": 18, "fat_g": 0, "sodium_mg": 0, "cholesterol_mg": 1},
    "fondant": {"servings": 12, "calories": 150, "protein_g": 3, "carbs_g": 14, "fat_g": 10, "sodium_mg": 0, "cholesterol_mg": 25},
    "glazed nuts": {"servings": 30, "calories": 59, "protein_g": 0, "carbs_g": 14, "fat_g": 0, "sodium_mg": 5, "cholesterol_mg": 34},
    "mint patties": {"servings": 30, "calories": 59, "protein_g": 0, "carbs_g": 14, "fat_g": 0, "sodium_mg": 5, "cholesterol_mg": 34},
    "mocha caramels": {"servings": 64, "calories": 80, "protein_g": 1, "carbs_g": 0, "fat_g": 10, "sodium_mg": 3, "cholesterol_mg": 37},
    "nut brittle": {"servings": 72, "calories": 72, "protein_g": 1, "carbs_g": 7, "fat_g": 10, "sodium_mg": 3, "cholesterol_mg": 37},
    "nutty caramel corn": {"servings": 10, "calories": 278, "protein_g": 6, "carbs_g": 28, "fat_g": 17, "sodium_mg": 0, "cholesterol_mg": 111},
    "old-time fudge": {"servings": 32, "calories": 67, "protein_g": 0, "carbs_g": 13, "fat_g": 1, "sodium_mg": 3, "cholesterol_mg": 8},
    "opera fudge": {"servings": 32, "calories": 60, "protein_g": 0, "carbs_g": 13, "fat_g": 1, "sodium_mg": 3, "cholesterol_mg": 8},
    "peanut butter balls": {"servings": 30, "calories": 90, "protein_g": 2, "carbs_g": 9, "fat_g": 6, "sodium_mg": 7, "cholesterol_mg": 91},
    "peanut clusters": {"servings": 36, "calories": 105, "protein_g": 3, "carbs_g": 8, "fat_g": 8, "sodium_mg": 7, "cholesterol_mg": 91},
    "penuche": {"servings": 36, "calories": 57, "protein_g": 0, "carbs_g": 17, "fat_g": 2, "sodium_mg": 5, "cholesterol_mg": 39},
    "pralines": {"servings": 36, "calories": 132, "protein_g": 1, "carbs_g": 19, "fat_g": 7, "sodium_mg": 4, "cholesterol_mg": 17},
    "remarkable fudge": {"servings": 96, "calories": 86, "protein_g": 1, "carbs_g": 13, "fat_g": 4, "sodium_mg": 1, "cholesterol_mg": 27},
    "rocky road": {"servings": 36, "calories": 97, "protein_g": 2, "carbs_g": 10, "fat_g": 6, "sodium_mg": 3, "cholesterol_mg": 13},
    "saltwater taffy": {"servings": 48, "calories": 56, "protein_g": 0, "carbs_g": 13, "fat_g": 0, "sodium_mg": 0, "cholesterol_mg": 10},
    "shortcut caramels": {"servings": 64, "calories": 86, "protein_g": 1, "carbs_g": 14, "fat_g": 3, "sodium_mg": 2, "cholesterol_mg": 47},
    "toffee butter crunch": {"servings": 47, "calories": 83, "protein_g": 1, "carbs_g": 7, "fat_g": 6, "sodium_mg": 11, "cholesterol_mg": 42},
    "truffles": {"servings": 32, "calories": 108, "protein_g": 1, "carbs_g": 10, "fat_g": 7, "sodium_mg": 12, "cholesterol_mg": 27},
    "walnut caramels": {"servings": 64, "calories": 94, "protein_g": 1, "carbs_g": 5, "fat_g": 5, "sodium_mg": 5, "cholesterol_mg": 42},
    "chocolate fudge": {"servings": 32, "calories": 95, "protein_g": 1, "carbs_g": 14, "fat_g": 4, "sodium_mg": 18, "cholesterol_mg": 9},
    "marzipan": {"servings": 48, "calories": 60, "protein_g": 1, "carbs_g": 8, "fat_g": 3, "sodium_mg": 3, "cholesterol_mg": 3},
}

COOKIES_NUTRITION = {
    "almond strips": {"servings": 48, "calories": 58, "protein_g": 1, "carbs_g": 8, "fat_g": 3, "sodium_mg": 6, "cholesterol_mg": 37},
    "applesauce bars": {"servings": 48, "calories": 97, "protein_g": 1, "carbs_g": 17, "fat_g": 5, "sodium_mg": 23, "cholesterol_mg": 55},
    "banana-spice cookies": {"servings": 60, "calories": 58, "protein_g": 1, "carbs_g": 9, "fat_g": 2, "sodium_mg": 9, "cholesterol_mg": 30},
    "brandy snaps": {"servings": 54, "calories": 28, "protein_g": 0, "carbs_g": 4, "fat_g": 1, "sodium_mg": 0, "cholesterol_mg": 1},
    "buttermilk brownies": {"servings": 36, "calories": 158, "protein_g": 2, "carbs_g": 23, "fat_g": 7, "sodium_mg": 5, "cholesterol_mg": 138},
    "butter-pecan shortbread": {"servings": 16, "calories": 102, "protein_g": 1, "carbs_g": 10, "fat_g": 6, "sodium_mg": 16, "cholesterol_mg": 60},
    "cake brownies": {"servings": 36, "calories": 112, "protein_g": 2, "carbs_g": 12, "fat_g": 7, "sodium_mg": 16, "cholesterol_mg": 56},
    "candy-window sugar-cookie cutouts": {"servings": 36, "calories": 85, "protein_g": 1, "carbs_g": 12, "fat_g": 4, "sodium_mg": 8, "cholesterol_mg": 9},
    "cashew-nutmeg drops": {"servings": 48, "calories": 77, "protein_g": 1, "carbs_g": 10, "fat_g": 4, "sodium_mg": 7, "cholesterol_mg": 41},
    "chocolate-candy cookies": {"servings": 60, "calories": 103, "protein_g": 1, "carbs_g": 14, "fat_g": 5, "sodium_mg": 9, "cholesterol_mg": 31},
    "chocolate chip cookies": {"servings": 60, "calories": 99, "protein_g": 1, "carbs_g": 12, "fat_g": 5, "sodium_mg": 5, "cholesterol_mg": 31},
    "chocolate-coconut pinwheels": {"servings": 72, "calories": 48, "protein_g": 1, "carbs_g": 6, "fat_g": 2, "sodium_mg": 5, "cholesterol_mg": 15},
    "chocolate-cream cheese cutouts": {"servings": 60, "calories": 83, "protein_g": 1, "carbs_g": 7, "fat_g": 6, "sodium_mg": 0, "cholesterol_mg": 26},
    "chocolate crinkles": {"servings": 48, "calories": 76, "protein_g": 1, "carbs_g": 10, "fat_g": 4, "sodium_mg": 17, "cholesterol_mg": 17},
    "chocolate-kiss peanut butter cookies": {"servings": 36, "calories": 116, "protein_g": 2, "carbs_g": 14, "fat_g": 6, "sodium_mg": 9, "cholesterol_mg": 73},
    "chocolate-peanut drop cookies": {"servings": 30, "calories": 83, "protein_g": 2, "carbs_g": 9, "fat_g": 5, "sodium_mg": 5, "cholesterol_mg": 43},
    "chocolate revel bars": {"servings": 60, "calories": 145, "protein_g": 2, "carbs_g": 20, "fat_g": 7, "sodium_mg": 12, "cholesterol_mg": 72},
    "chocolate spritz": {"servings": 84, "calories": 68, "protein_g": 1, "carbs_g": 6, "fat_g": 5, "sodium_mg": 0, "cholesterol_mg": 7},
    "choose-a-chip oatmeal cookies": {"servings": 54, "calories": 96, "protein_g": 1, "carbs_g": 12, "fat_g": 5, "sodium_mg": 6, "cholesterol_mg": 47},
    "cinnamon snaps": {"servings": 54, "calories": 30, "protein_g": 0, "carbs_g": 5, "fat_g": 1, "sodium_mg": 0, "cholesterol_mg": 14},
    "citrus cream cheese cutouts": {"servings": 60, "calories": 48, "protein_g": 1, "carbs_g": 2, "fat_g": 6, "sodium_mg": 7, "cholesterol_mg": 26},
    "coconut macaroons": {"servings": 30, "calories": 34, "protein_g": 0, "carbs_g": 6, "fat_g": 1, "sodium_mg": 0, "cholesterol_mg": 4},
    "coconut-pecan drop cookies": {"servings": 36, "calories": 87, "protein_g": 1, "carbs_g": 8, "fat_g": 6, "sodium_mg": 7, "cholesterol_mg": 22},
    "cranberry-pecan bars": {"servings": 24, "calories": 77, "protein_g": 1, "carbs_g": 10, "fat_g": 4, "sodium_mg": 11, "cholesterol_mg": 45},
    "cream cheese cutouts": {"servings": 60, "calories": 48, "protein_g": 1, "carbs_g": 7, "fat_g": 2, "sodium_mg": 6, "cholesterol_mg": 26},
    "crispy cereal squares": {"servings": 25, "calories": 112, "protein_g": 3, "carbs_g": 14, "fat_g": 5, "sodium_mg": 0, "cholesterol_mg": 109},
    "date-filled rounds": {"servings": 36, "calories": 135, "protein_g": 2, "carbs_g": 18, "fat_g": 6, "sodium_mg": 0, "cholesterol_mg": 83},
    "date pinwheel cookies": {"servings": 72, "calories": 62, "protein_g": 1, "carbs_g": 9, "fat_g": 3, "sodium_mg": 4, "cholesterol_mg": 32},
    "drop cookies": {"servings": 72, "calories": 62, "protein_g": 1, "carbs_g": 9, "fat_g": 3, "sodium_mg": 4, "cholesterol_mg": 32},
    "filled sugar-cookie cutouts": {"servings": 24, "calories": 212, "protein_g": 2, "carbs_g": 33, "fat_g": 9, "sodium_mg": 19, "cholesterol_mg": 88},
    "florentines": {"servings": 24, "calories": 124, "protein_g": 2, "carbs_g": 12, "fat_g": 8, "sodium_mg": 0, "cholesterol_mg": 44},
    "fruit-filled oatmeal bars with apple-cinnamon filling": {"servings": 25, "calories": 96, "protein_g": 1, "carbs_g": 14, "fat_g": 4, "sodium_mg": 0, "cholesterol_mg": 56},
    "fruit-filled oatmeal bars with apricot-coconut filling": {"servings": 25, "calories": 113, "protein_g": 1, "carbs_g": 18, "fat_g": 4, "sodium_mg": 0, "cholesterol_mg": 57},
    "fruit-filled oatmeal bars with raisin filling": {"servings": 25, "calories": 107, "protein_g": 1, "carbs_g": 17, "fat_g": 4, "sodium_mg": 0, "cholesterol_mg": 57},
    "fruit-topped oatmeal cookies": {"servings": 48, "calories": 100, "protein_g": 1, "carbs_g": 16, "fat_g": 4, "sodium_mg": 6, "cholesterol_mg": 49},
    "fudge brownies": {"servings": 24, "calories": 115, "protein_g": 2, "carbs_g": 13, "fat_g": 7, "sodium_mg": 23, "cholesterol_mg": 51},
    "fudge ecstasies": {"servings": 24, "calories": 115, "protein_g": 2, "carbs_g": 13, "fat_g": 7, "sodium_mg": 23, "cholesterol_mg": 51},
    "giant chocolate chip cookies": {"servings": 20, "calories": 105, "protein_g": 3, "carbs_g": 17, "fat_g": 7, "sodium_mg": 15, "cholesterol_mg": 14},
    "gingerbread cutouts": {"servings": 36, "calories": 80, "protein_g": 1, "carbs_g": 12, "fat_g": 3, "sodium_mg": 8, "cholesterol_mg": 27},
    "gingerbread people cutouts": {"servings": 12, "calories": 240, "protein_g": 3, "carbs_g": 37, "fat_g": 9, "sodium_mg": 23, "cholesterol_mg": 82},
    "gingersnaps": {"servings": 48, "calories": 76, "protein_g": 1, "carbs_g": 11, "fat_g": 3, "sodium_mg": 6, "cholesterol_mg": 26},
    "granola bars": {"servings": 24, "calories": 139, "protein_g": 2, "carbs_g": 16, "fat_g": 8, "sodium_mg": 5, "cholesterol_mg": 28},
    "gumdrop drop cookies": {"servings": 30, "calories": 97, "protein_g": 1, "carbs_g": 14, "fat_g": 3, "sodium_mg": 9, "cholesterol_mg": 28},
    "hermits": {"servings": 36, "calories": 84, "protein_g": 1, "carbs_g": 12, "fat_g": 4, "sodium_mg": 8, "cholesterol_mg": 42},
    "jam thumbprints": {"servings": 42, "calories": 80, "protein_g": 1, "carbs_g": 8, "fat_g": 5, "sodium_mg": 15, "cholesterol_mg": 57},
    "lemon and poppy seed shortbread": {"servings": 30, "calories": 58, "protein_g": 1, "carbs_g": 5, "fat_g": 4, "sodium_mg": 5, "cholesterol_mg": 47},
    "lemon bars": {"servings": 20, "calories": 100, "protein_g": 1, "carbs_g": 16, "fat_g": 4, "sodium_mg": 2, "cholesterol_mg": 47},
    "lemon macaroons": {"servings": 30, "calories": 54, "protein_g": 1, "carbs_g": 6, "fat_g": 3, "sodium_mg": 0, "cholesterol_mg": 31},
    "lemon tea cookies": {"servings": 30, "calories": 54, "protein_g": 1, "carbs_g": 6, "fat_g": 3, "sodium_mg": 0, "cholesterol_mg": 31},
    "macadamia nut and white chocolate chunk cookies": {"servings": 60, "calories": 60, "protein_g": 1, "carbs_g": 6, "fat_g": 3, "sodium_mg": 0, "cholesterol_mg": 36},
    "nutty macaroons": {"servings": 30, "calories": 47, "protein_g": 1, "carbs_g": 4, "fat_g": 4, "sodium_mg": 7, "cholesterol_mg": 3},
    "nutty spritz": {"servings": 84, "calories": 58, "protein_g": 1, "carbs_g": 6, "fat_g": 3, "sodium_mg": 5, "cholesterol_mg": 43},
    "oatmeal cookies": {"servings": 60, "calories": 68, "protein_g": 1, "carbs_g": 10, "fat_g": 3, "sodium_mg": 3, "cholesterol_mg": 35},
    "oatmeal shortbread": {"servings": 60, "calories": 44, "protein_g": 1, "carbs_g": 4, "fat_g": 3, "sodium_mg": 3, "cholesterol_mg": 59},
    "oat-spiced slices": {"servings": 60, "calories": 44, "protein_g": 1, "carbs_g": 4, "fat_g": 3, "sodium_mg": 3, "cholesterol_mg": 59},
    "orange-chocolate slices": {"servings": 60, "calories": 44, "protein_g": 1, "carbs_g": 4, "fat_g": 3, "sodium_mg": 3, "cholesterol_mg": 59},
    "orange-date bars": {"servings": 30, "calories": 56, "protein_g": 1, "carbs_g": 8, "fat_g": 3, "sodium_mg": 2, "cholesterol_mg": 5},
    "peanut butter bars": {"servings": 30, "calories": 56, "protein_g": 2, "carbs_g": 6, "fat_g": 3, "sodium_mg": 3, "cholesterol_mg": 69},
    "peanut butter cookies": {"servings": 30, "calories": 56, "protein_g": 2, "carbs_g": 6, "fat_g": 3, "sodium_mg": 3, "cholesterol_mg": 69},
    "pecan snaps": {"servings": 30, "calories": 66, "protein_g": 1, "carbs_g": 6, "fat_g": 4, "sodium_mg": 0, "cholesterol_mg": 42},
    "pineapple-coconut drop cookies": {"servings": 30, "calories": 81, "protein_g": 1, "carbs_g": 10, "fat_g": 6, "sodium_mg": 9, "cholesterol_mg": 26},
    "pumpkin bars": {"servings": 48, "calories": 115, "protein_g": 1, "carbs_g": 14, "fat_g": 6, "sodium_mg": 5, "cholesterol_mg": 51},
    "raisin-oatmeal cookies": {"servings": 54, "calories": 81, "protein_g": 1, "carbs_g": 13, "fat_g": 3, "sodium_mg": 0, "cholesterol_mg": 40},
    "ranger cookies": {"servings": 54, "calories": 65, "protein_g": 1, "carbs_g": 7, "fat_g": 4, "sodium_mg": 0, "cholesterol_mg": 23},
    "sandies": {"servings": 36, "calories": 105, "protein_g": 1, "carbs_g": 7, "fat_g": 9, "sodium_mg": 0, "cholesterol_mg": 60},
    "santa's whiskers": {"servings": 16, "calories": 95, "protein_g": 1, "carbs_g": 11, "fat_g": 0, "sodium_mg": 6, "cholesterol_mg": 15},
    "shortbread": {"servings": 36, "calories": 68, "protein_g": 1, "carbs_g": 10, "fat_g": 6, "sodium_mg": 16, "cholesterol_mg": 59},
    "snickerdoodles": {"servings": 30, "calories": 81, "protein_g": 1, "carbs_g": 12, "fat_g": 3, "sodium_mg": 9, "cholesterol_mg": 26},
    "spiced raisin drop cookies": {"servings": 16, "calories": 96, "protein_g": 1, "carbs_g": 10, "fat_g": 6, "sodium_mg": 6, "cholesterol_mg": 0},
    "spiced shortbread": {"servings": 60, "calories": 65, "protein_g": 1, "carbs_g": 7, "fat_g": 4, "sodium_mg": 5, "cholesterol_mg": 29},
    "spiced slices": {"servings": 24, "calories": 84, "protein_g": 1, "carbs_g": 12, "fat_g": 4, "sodium_mg": 11, "cholesterol_mg": 45},
    "spicy prune bars": {"servings": 84, "calories": 58, "protein_g": 1, "carbs_g": 6, "fat_g": 3, "sodium_mg": 5, "cholesterol_mg": 43},
    "spritz": {"servings": 36, "calories": 75, "protein_g": 1, "carbs_g": 9, "fat_g": 4, "sodium_mg": 2, "cholesterol_mg": 15},
    "sugar-cookie cutouts": {"servings": 24, "calories": 100, "protein_g": 1, "carbs_g": 9, "fat_g": 7, "sodium_mg": 2, "cholesterol_mg": 72},
    "tiny tarts with lemon-coconut filling": {"servings": 24, "calories": 115, "protein_g": 1, "carbs_g": 11, "fat_g": 7, "sodium_mg": 15, "cholesterol_mg": 66},
    "tiny tarts with pecan filling": {"servings": 24, "calories": 80, "protein_g": 1, "carbs_g": 7, "fat_g": 5, "sodium_mg": 16, "cholesterol_mg": 59},
    "tiny tarts with pumpkin filling": {"servings": 24, "calories": 102, "protein_g": 1, "carbs_g": 14, "fat_g": 5, "sodium_mg": 4, "cholesterol_mg": 58},
    "tiny tarts with spiced fruit filling": {"servings": 24, "calories": 115, "protein_g": 1, "carbs_g": 16, "fat_g": 5, "sodium_mg": 4, "cholesterol_mg": 74},
    "toffee bars": {"servings": 36, "calories": 115, "protein_g": 1, "carbs_g": 16, "fat_g": 5, "sodium_mg": 4, "cholesterol_mg": 74},
    "whole wheat chocolate revel bars": {"servings": 60, "calories": 144, "protein_g": 2, "carbs_g": 20, "fat_g": 7, "sodium_mg": 12, "cholesterol_mg": 72},
    "whole wheat spiced slices": {"servings": 60, "calories": 65, "protein_g": 1, "carbs_g": 7, "fat_g": 4, "sodium_mg": 5, "cholesterol_mg": 29},
    "whole wheat spritz": {"servings": 84, "calories": 58, "protein_g": 1, "carbs_g": 6, "fat_g": 3, "sodium_mg": 5, "cholesterol_mg": 43},
}

EGGS_CHEESE_LEGUMES_NUTRITION = {
    "asparagus egg casserole": {"servings": 2, "calories": 330, "protein_g": 17, "carbs_g": 18, "fat_g": 25, "sodium_mg": 295, "cholesterol_mg": 590},
    "bacon-asparagus puffy omelet": {"servings": 3, "calories": 269, "protein_g": 16, "carbs_g": 2, "fat_g": 22, "sodium_mg": 564, "cholesterol_mg": 303},
    "baked eggs": {"servings": 3, "calories": 382, "protein_g": 20, "carbs_g": 27, "fat_g": 23, "sodium_mg": 1010, "cholesterol_mg": 787},
    "bean and cheese burritos": {"servings": 3, "calories": 382, "protein_g": 29, "carbs_g": 65, "fat_g": 10, "sodium_mg": 1196, "cholesterol_mg": 762},
    "bean and cheese chimichangas": {"servings": 4, "calories": 378, "protein_g": 21, "carbs_g": 19, "fat_g": 23, "sodium_mg": 126, "cholesterol_mg": 532},
    "beer rarebit": {"servings": 4, "calories": 535, "protein_g": 31, "carbs_g": 15, "fat_g": 27, "sodium_mg": 267, "cholesterol_mg": 730},
    "blue cheese and bacon puff": {"servings": 5, "calories": 325, "protein_g": 15, "carbs_g": 10, "fat_g": 25, "sodium_mg": 354, "cholesterol_mg": 203},
    "breakfast pizza": {"servings": 6, "calories": 325, "protein_g": 15, "carbs_g": 10, "fat_g": 25, "sodium_mg": 354, "cholesterol_mg": 203},
    "broccoli puff": {"servings": 4, "calories": 454, "protein_g": 27, "carbs_g": 19, "fat_g": 30, "sodium_mg": 14, "cholesterol_mg": 582},
    "bulgur tacos": {"servings": 6, "calories": 297, "protein_g": 17, "carbs_g": 31, "fat_g": 14, "sodium_mg": 570, "cholesterol_mg": 729},
    "california-style egg salad sandwiches": {"servings": 4, "calories": 369, "protein_g": 21, "carbs_g": 2, "fat_g": 22, "sodium_mg": 228, "cholesterol_mg": 430},
    "cheese fondue": {"servings": 5, "calories": 359, "protein_g": 21, "carbs_g": 2, "fat_g": 22, "sodium_mg": 75, "cholesterol_mg": 228},
    "cheese french omelet": {"servings": 1, "calories": 396, "protein_g": 21, "carbs_g": 5, "fat_g": 33, "sodium_mg": 579, "cholesterol_mg": 447},
    "cheese-herb puffy omelet": {"servings": 2, "calories": 391, "protein_g": 17, "carbs_g": 1, "fat_g": 35, "sodium_mg": 570, "cholesterol_mg": 646},
    "cheese-onion scrambled eggs": {"servings": 3, "calories": 291, "protein_g": 17, "carbs_g": 4, "fat_g": 23, "sodium_mg": 572, "cholesterol_mg": 213},
    "cheese souffle": {"servings": 4, "calories": 465, "protein_g": 23, "carbs_g": 10, "fat_g": 37, "sodium_mg": 539, "cholesterol_mg": 586},
    "cheese strata": {"servings": 6, "calories": 260, "protein_g": 15, "carbs_g": 19, "fat_g": 14, "sodium_mg": 213, "cholesterol_mg": 673},
    "cheese-stuffed manicotti": {"servings": 5, "calories": 577, "protein_g": 35, "carbs_g": 39, "fat_g": 29, "sodium_mg": 142, "cholesterol_mg": 1026},
    "cheesy brunch roll-ups": {"servings": 6, "calories": 394, "protein_g": 19, "carbs_g": 26, "fat_g": 24, "sodium_mg": 183, "cholesterol_mg": 367},
    "choose-a-flavor quiche": {"servings": 4, "calories": 406, "protein_g": 20, "carbs_g": 25, "fat_g": 26, "sodium_mg": 181, "cholesterol_mg": 331},
    "cream-cheese scrambled eggs": {"servings": 4, "calories": 406, "protein_g": 20, "carbs_g": 25, "fat_g": 26, "sodium_mg": 181, "cholesterol_mg": 331},
    "creamy cheese fondue": {"servings": 3, "calories": 429, "protein_g": 19, "carbs_g": 4, "fat_g": 34, "sodium_mg": 103, "cholesterol_mg": 1169},
    "creamy lasagna": {"servings": 4, "calories": 610, "protein_g": 36, "carbs_g": 46, "fat_g": 30, "sodium_mg": 142, "cholesterol_mg": 1026},
    "creamy poached eggs": {"servings": 4, "calories": 323, "protein_g": 17, "carbs_g": 17, "fat_g": 21, "sodium_mg": 320, "cholesterol_mg": 451},
    "denver omelet": {"servings": 2, "calories": 416, "protein_g": 23, "carbs_g": 11, "fat_g": 31, "sodium_mg": 572, "cholesterol_mg": 859},
    "denver scrambled eggs": {"servings": 3, "calories": 307, "protein_g": 17, "carbs_g": 2, "fat_g": 24, "sodium_mg": 560, "cholesterol_mg": 544},
    "deviled eggs": {"servings": 12, "calories": 73, "protein_g": 3, "carbs_g": 1, "fat_g": 6, "sodium_mg": 140, "cholesterol_mg": 66},
    "egg-pita sandwiches": {"servings": 2, "calories": 364, "protein_g": 18, "carbs_g": 26, "fat_g": 21, "sodium_mg": 436, "cholesterol_mg": 336},
    "egg-salad sandwiches": {"servings": 2, "calories": 416, "protein_g": 17, "carbs_g": 31, "fat_g": 24, "sodium_mg": 558, "cholesterol_mg": 654},
    "eggs benedict": {"servings": 4, "calories": 358, "protein_g": 21, "carbs_g": 17, "fat_g": 23, "sodium_mg": 401, "cholesterol_mg": 873},
    "eggs in a puff": {"servings": 4, "calories": 941, "protein_g": 18, "carbs_g": 28, "fat_g": 32, "sodium_mg": 560, "cholesterol_mg": 630},
    "farmer's breakfast": {"servings": 4, "calories": 372, "protein_g": 19, "carbs_g": 16, "fat_g": 26, "sodium_mg": 431, "cholesterol_mg": 713},
    "fettuccine with asparagus and swiss cheese sauce": {"servings": 4, "calories": 455, "protein_g": 22, "carbs_g": 35, "fat_g": 17, "sodium_mg": 39, "cholesterol_mg": 825},
    "fettuccine with broccoli and cheese sauce": {"servings": 4, "calories": 438, "protein_g": 21, "carbs_g": 55, "fat_g": 15, "sodium_mg": 39, "cholesterol_mg": 834},
    "fettuccine with cheese sauce": {"servings": 4, "calories": 420, "protein_g": 19, "carbs_g": 51, "fat_g": 15, "sodium_mg": 39, "cholesterol_mg": 819},
    "french omelet": {"servings": 1, "calories": 261, "protein_g": 12, "carbs_g": 1, "fat_g": 23, "sodium_mg": 550, "cholesterol_mg": 540},
    "fried eggs": {"servings": 2, "calories": 192, "protein_g": 12, "carbs_g": 1, "fat_g": 15, "sodium_mg": 555, "cholesterol_mg": 183},
    "fried rice supper": {"servings": 4, "calories": 454, "protein_g": 24, "carbs_g": 64, "fat_g": 12, "sodium_mg": 69, "cholesterol_mg": 594},
    "frittata": {"servings": 3, "calories": 229, "protein_g": 15, "carbs_g": 5, "fat_g": 6, "sodium_mg": 553, "cholesterol_mg": 266},
    "fruited french omelet": {"servings": 1, "calories": 391, "protein_g": 14, "carbs_g": 19, "fat_g": 29, "sodium_mg": 563, "cholesterol_mg": 561},
    "garbanzo sandwich spread": {"servings": 5, "calories": 170, "protein_g": 5, "carbs_g": 15, "fat_g": 10, "sodium_mg": 0, "cholesterol_mg": 115},
    "greek frittata": {"servings": 3, "calories": 259, "protein_g": 17, "carbs_g": 5, "fat_g": 19, "sodium_mg": 567, "cholesterol_mg": 432},
    "greek-style egg-salad sandwiches": {"servings": 2, "calories": 461, "protein_g": 20, "carbs_g": 32, "fat_g": 28, "sodium_mg": 570, "cholesterol_mg": 785},
    "ham-and-cheese puffy omelet": {"servings": 2, "calories": 422, "protein_g": 24, "carbs_g": 10, "fat_g": 31, "sodium_mg": 385, "cholesterol_mg": 746},
    "hard-cooked eggs": {"servings": 3, "calories": 159, "protein_g": 10, "carbs_g": 1, "fat_g": 11, "sodium_mg": 150, "cholesterol_mg": 139},
    "herbed scrambled eggs": {"servings": 3, "calories": 206, "protein_g": 13, "carbs_g": 1, "fat_g": 16, "sodium_mg": 552, "cholesterol_mg": 375},
    "huevos rancheros": {"servings": 3, "calories": 427, "protein_g": 23, "carbs_g": 25, "fat_g": 27, "sodium_mg": 6, "cholesterol_mg": 552},
    "indian-style deviled eggs": {"servings": 12, "calories": 90, "protein_g": 4, "carbs_g": 1, "fat_g": 8, "sodium_mg": 0, "cholesterol_mg": 547},
    "individual quiche casseroles": {"servings": 4, "calories": 276, "protein_g": 20, "carbs_g": 9, "fat_g": 18, "sodium_mg": 252, "cholesterol_mg": 342},
    "italian-style deviled eggs": {"servings": 12, "calories": 64, "protein_g": 4, "carbs_g": 1, "fat_g": 5, "sodium_mg": 98, "cholesterol_mg": 96},
    "macaroni and cheese": {"servings": 4, "calories": 295, "protein_g": 14, "carbs_g": 25, "fat_g": 16, "sodium_mg": 1016, "cholesterol_mg": 301},
    "meatless tacos": {"servings": 4, "calories": 378, "protein_g": 16, "carbs_g": 36, "fat_g": 19, "sodium_mg": 7, "cholesterol_mg": 604},
    "meaty red beans and rice": {"servings": 4, "calories": 386, "protein_g": 17, "carbs_g": 40, "fat_g": 17, "sodium_mg": 9, "cholesterol_mg": 495},
    "mediterranean sandwich": {"servings": 2, "calories": 392, "protein_g": 21, "carbs_g": 28, "fat_g": 23, "sodium_mg": 9, "cholesterol_mg": 17},
    "mexican-style deviled eggs": {"servings": 12, "calories": 86, "protein_g": 4, "carbs_g": 2, "fat_g": 8, "sodium_mg": 7, "cholesterol_mg": 24},
    "mushroom french omelet": {"servings": 1, "calories": 304, "protein_g": 14, "carbs_g": 3, "fat_g": 26, "sodium_mg": 9, "cholesterol_mg": 547},
    "mushroom scrambled eggs": {"servings": 3, "calories": 216, "protein_g": 14, "carbs_g": 2, "fat_g": 17, "sodium_mg": 3, "cholesterol_mg": 383},
    "onion cheese fondue": {"servings": 5, "calories": 391, "protein_g": 21, "carbs_g": 5, "fat_g": 25, "sodium_mg": 80, "cholesterol_mg": 13},
    "oven frittata": {"servings": 6, "calories": 347, "protein_g": 27, "carbs_g": 6, "fat_g": 24, "sodium_mg": 15, "cholesterol_mg": 578},
    "poached eggs": {"servings": 4, "calories": 148, "protein_g": 12, "carbs_g": 1, "fat_g": 10, "sodium_mg": 138, "cholesterol_mg": 423},
    "puffy omelet": {"servings": 2, "calories": 237, "protein_g": 14, "carbs_g": 2, "fat_g": 19, "sodium_mg": 570, "cholesterol_mg": 646},
    "quiche lorraine": {"servings": 4, "calories": 548, "protein_g": 25, "carbs_g": 24, "fat_g": 39, "sodium_mg": 5, "cholesterol_mg": 18},
    "red beans and corn bread": {"servings": 4, "calories": 548, "protein_g": 25, "carbs_g": 79, "fat_g": 14, "sodium_mg": 10, "cholesterol_mg": 107},
    "scrambled egg casserole": {"servings": 6, "calories": 376, "protein_g": 19, "carbs_g": 21, "fat_g": 23, "sodium_mg": 471, "cholesterol_mg": 416},
    "scrambled eggs": {"servings": 3, "calories": 181, "protein_g": 12, "carbs_g": 2, "fat_g": 15, "sodium_mg": 575, "cholesterol_mg": 417},
    "shortcut macaroni and cheese": {"servings": 4, "calories": 276, "protein_g": 10, "carbs_g": 36, "fat_g": 10, "sodium_mg": 1016, "cholesterol_mg": 301},
    "soft-cooked eggs": {"servings": 4, "calories": 276, "protein_g": 10, "carbs_g": 36, "fat_g": 10, "sodium_mg": 1016, "cholesterol_mg": 301},
    "spinach-egg casserole": {"servings": 6, "calories": 202, "protein_g": 14, "carbs_g": 5, "fat_g": 14, "sodium_mg": 9, "cholesterol_mg": 19},
    "spinach manicotti": {"servings": 4, "calories": 593, "protein_g": 27, "carbs_g": 44, "fat_g": 30, "sodium_mg": 5, "cholesterol_mg": 1032},
    "spinach puff": {"servings": 4, "calories": 431, "protein_g": 26, "carbs_g": 14, "fat_g": 30, "sodium_mg": 659, "cholesterol_mg": 29},
    "vegetable cheese strata": {"servings": 6, "calories": 257, "protein_g": 15, "carbs_g": 21, "fat_g": 14, "sodium_mg": 213, "cholesterol_mg": 675},
    "vegetable french omelet": {"servings": 1, "calories": 353, "protein_g": 3, "carbs_g": 35, "fat_g": 5, "sodium_mg": 584, "cholesterol_mg": 714},
    "vegetable macaroni and cheese": {"servings": 4, "calories": 480, "protein_g": 29, "carbs_g": 40, "fat_g": 5, "sodium_mg": 1048, "cholesterol_mg": 454},
    "vegetable souffle": {"servings": 4, "calories": 323, "protein_g": 16, "carbs_g": 13, "fat_g": 24, "sodium_mg": 280, "cholesterol_mg": 497},
    "welsh rarebit breakfast": {"servings": 4, "calories": 304, "protein_g": 23, "carbs_g": 20, "fat_g": 18, "sodium_mg": 130, "cholesterol_mg": 637},
}

SALADS_NUTRITION = {
    "ginger vinaigrette": {"servings": 12, "calories": 0, "protein_g": 0, "carbs_g": 0, "fat_g": 0, "sodium_mg": 0, "cholesterol_mg": 0},
    "greek style salads": {"servings": 3, "calories": 419, "protein_g": 21, "carbs_g": 10, "fat_g": 34, "sodium_mg": 310, "cholesterol_mg": 545},
    "green goddess dressing": {"servings": 16, "calories": 47, "protein_g": 0, "carbs_g": 5, "fat_g": 3, "sodium_mg": 0, "cholesterol_mg": 4},
    "greens with basil vinaigrette": {"servings": 4, "calories": 68, "protein_g": 2, "carbs_g": 4, "fat_g": 5, "sodium_mg": 1, "cholesterol_mg": 11},
    "ham and rice salad": {"servings": 4, "calories": 601, "protein_g": 17, "carbs_g": 40, "fat_g": 79, "sodium_mg": 981, "cholesterol_mg": 352},
    "ham salad": {"servings": 4, "calories": 280, "protein_g": 15, "carbs_g": 2, "fat_g": 23, "sodium_mg": 176, "cholesterol_mg": 867},
    "herb blender mayonnaise": {"servings": 16, "calories": 92, "protein_g": 0, "carbs_g": 0, "fat_g": 10, "sodium_mg": 0, "cholesterol_mg": 45},
    "herb vinegar": {"servings": 32, "calories": 0, "protein_g": 0, "carbs_g": 0, "fat_g": 0, "sodium_mg": 0, "cholesterol_mg": 0},
    "honey-lime dressing": {"servings": 21, "calories": 86, "protein_g": 0, "carbs_g": 0, "fat_g": 9, "sodium_mg": 0, "cholesterol_mg": 0},
    "horseradish dressing": {"servings": 20, "calories": 50, "protein_g": 0, "carbs_g": 2, "fat_g": 5, "sodium_mg": 0, "cholesterol_mg": 5},
    "italian-style pasta toss": {"servings": 6, "calories": 60, "protein_g": 2, "carbs_g": 3, "fat_g": 4, "sodium_mg": 65, "cholesterol_mg": 497},
    "italian vinaigrette": {"servings": 12, "calories": 84, "protein_g": 0, "carbs_g": 1, "fat_g": 9, "sodium_mg": 0, "cholesterol_mg": 38},
    "louis dressing": {"servings": 4, "calories": 195, "protein_g": 0, "carbs_g": 7, "fat_g": 19, "sodium_mg": 0, "cholesterol_mg": 24},
    "marinated cucumbers": {"servings": 4, "calories": 78, "protein_g": 0, "carbs_g": 8, "fat_g": 5, "sodium_mg": 1, "cholesterol_mg": 7},
    "marinated mushroom salad": {"servings": 4, "calories": 117, "protein_g": 0, "carbs_g": 8, "fat_g": 10, "sodium_mg": 0, "cholesterol_mg": 83},
    "marinated potato salad": {"servings": 4, "calories": 204, "protein_g": 4, "carbs_g": 21, "fat_g": 10, "sodium_mg": 6, "cholesterol_mg": 14},
    "marinated steak salads": {"servings": 4, "calories": 397, "protein_g": 27, "carbs_g": 22, "fat_g": 23, "sodium_mg": 134, "cholesterol_mg": 121},
    "marinated vegetable salad": {"servings": 6, "calories": 127, "protein_g": 2, "carbs_g": 9, "fat_g": 10, "sodium_mg": 4, "cholesterol_mg": 23},
    "mayonnaise": {"servings": 32, "calories": 102, "protein_g": 0, "carbs_g": 0, "fat_g": 11, "sodium_mg": 0, "cholesterol_mg": 17},
    "nut-flavored oil": {"servings": 40, "calories": 118, "protein_g": 0, "carbs_g": 0, "fat_g": 14, "sodium_mg": 0, "cholesterol_mg": 0},
    "nutty citrus coleslaw": {"servings": 5, "calories": 242, "protein_g": 5, "carbs_g": 13, "fat_g": 21, "sodium_mg": 5, "cholesterol_mg": 7},
    "oil-free dressing": {"servings": 8, "calories": 8, "protein_g": 0, "carbs_g": 2, "fat_g": 0, "sodium_mg": 0, "cholesterol_mg": 0},
    "onion vinaigrette": {"servings": 12, "calories": 86, "protein_g": 0, "carbs_g": 1, "fat_g": 9, "sodium_mg": 0, "cholesterol_mg": 0},
    "peach-berry frozen salad": {"servings": 9, "calories": 268, "protein_g": 2, "carbs_g": 27, "fat_g": 17, "sodium_mg": 100, "cholesterol_mg": 21},
    "pea-cheese salad": {"servings": 3, "calories": 229, "protein_g": 8, "carbs_g": 7, "fat_g": 19, "sodium_mg": 8, "cholesterol_mg": 143},
    "pineapple-lemon squares": {"servings": 9, "calories": 251, "protein_g": 5, "carbs_g": 14, "fat_g": 21, "sodium_mg": 12, "cholesterol_mg": 71},
    "red wine vinaigrette": {"servings": 12, "calories": 87, "protein_g": 0, "carbs_g": 2, "fat_g": 9, "sodium_mg": 0, "cholesterol_mg": 0},
    "reuben salads": {"servings": 4, "calories": 515, "protein_g": 40, "carbs_g": 8, "fat_g": 70, "sodium_mg": 149, "cholesterol_mg": 480},
    "russian dressing": {"servings": 11, "calories": 56, "protein_g": 0, "carbs_g": 3, "fat_g": 5, "sodium_mg": 0, "cholesterol_mg": 118},
    "rye croutons": {"servings": 4, "calories": 47, "protein_g": 2, "carbs_g": 7, "fat_g": 1, "sodium_mg": 0, "cholesterol_mg": 2},
    "salad nicoise": {"servings": 4, "calories": 456, "protein_g": 20, "carbs_g": 33, "fat_g": 236, "sodium_mg": 151, "cholesterol_mg": 718},
    "salmon pasta salad": {"servings": 6, "calories": 528, "protein_g": 22, "carbs_g": 19, "fat_g": 41, "sodium_mg": 44, "cholesterol_mg": 435},
    "salmon salad": {"servings": 4, "calories": 295, "protein_g": 19, "carbs_g": 4, "fat_g": 7, "sodium_mg": 14, "cholesterol_mg": 63},
    "salmon salad nicoise": {"servings": 4, "calories": 491, "protein_g": 19, "carbs_g": 9, "fat_g": 39, "sodium_mg": 226, "cholesterol_mg": 415},
    "sherried cranberry relish ring": {"servings": 12, "calories": 179, "protein_g": 4, "carbs_g": 0, "fat_g": 0, "sodium_mg": 60, "cholesterol_mg": 72},
    "spinach and garbanzo bean salad": {"servings": 6, "calories": 274, "protein_g": 21, "carbs_g": 10, "fat_g": 18, "sodium_mg": 98, "cholesterol_mg": 149},
    "spinach-orange toss": {"servings": 4, "calories": 167, "protein_g": 4, "carbs_g": 16, "fat_g": 11, "sodium_mg": 0, "cholesterol_mg": 5},
    "sunflower nut dressing": {"servings": 16, "calories": 18, "protein_g": 1, "carbs_g": 1, "fat_g": 1, "sodium_mg": 11, "cholesterol_mg": 46},
    "tabbouleh": {"servings": 6, "calories": 168, "protein_g": 3, "carbs_g": 19, "fat_g": 8, "sodium_mg": 0, "cholesterol_mg": 84},
    "taco salads": {"servings": 6, "calories": 431, "protein_g": 25, "carbs_g": 22, "fat_g": 26, "sodium_mg": 91, "cholesterol_mg": 900},
    "thousand island dressing": {"servings": 24, "calories": 74, "protein_g": 0, "carbs_g": 1, "fat_g": 8, "sodium_mg": 7, "cholesterol_mg": 111},
    "three bean salad": {"servings": 6, "calories": 204, "protein_g": 6, "carbs_g": 25, "fat_g": 10, "sodium_mg": 0, "cholesterol_mg": 63},
    "tomato vegetable aspic": {"servings": 8, "calories": 311, "protein_g": 3, "carbs_g": 6, "fat_g": 0, "sodium_mg": 0, "cholesterol_mg": 426},
    "tortilla cups": {"servings": 6, "calories": 177, "protein_g": 2, "carbs_g": 21, "fat_g": 10, "sodium_mg": 0, "cholesterol_mg": 0},
    "tuna-melon plates": {"servings": 4, "calories": 417, "protein_g": 25, "carbs_g": 15, "fat_g": 29, "sodium_mg": 70, "cholesterol_mg": 311},
    "tuna salad": {"servings": 4, "calories": 260, "protein_g": 17, "carbs_g": 1, "fat_g": 18, "sodium_mg": 177, "cholesterol_mg": 223},
    "24-hour fruit salad": {"servings": 8, "calories": 199, "protein_g": 2, "carbs_g": 29, "fat_g": 9, "sodium_mg": 123, "cholesterol_mg": 30},
    "24-hour vegetable salad": {"servings": 6, "calories": 357, "protein_g": 11, "carbs_g": 8, "fat_g": 32, "sodium_mg": 127, "cholesterol_mg": 459},
    "vegetable pasta salad": {"servings": 8, "calories": 179, "protein_g": 4, "carbs_g": 25, "fat_g": 7, "sodium_mg": 0, "cholesterol_mg": 121},
    "vinaigrette": {"servings": 12, "calories": 85, "protein_g": 0, "carbs_g": 1, "fat_g": 9, "sodium_mg": 0, "cholesterol_mg": 0},
    "vinaigrette coleslaw": {"servings": 4, "calories": 140, "protein_g": 1, "carbs_g": 12, "fat_g": 10, "sodium_mg": 0, "cholesterol_mg": 13},
    "waldorf salad": {"servings": 4, "calories": 283, "protein_g": 2, "carbs_g": 19, "fat_g": 23, "sodium_mg": 35, "cholesterol_mg": 95},
    "wilted spinach salad": {"servings": 4, "calories": 147, "protein_g": 9, "carbs_g": 6, "fat_g": 10, "sodium_mg": 83, "cholesterol_mg": 480},
}

def normalize_name(name):
    """Normalize recipe name for matching."""
    name = name.lower()
    name = re.sub(r'[^a-z0-9\s]', '', name)
    name = ' '.join(name.split())
    return name

def match_recipe(recipe_title, nutrition_db):
    """Try to match recipe title to nutrition database entry."""
    normalized = normalize_name(recipe_title)

    # Direct match
    if normalized in nutrition_db:
        return nutrition_db[normalized]

    # Try without common suffixes
    for suffix in [' recipe', ' recipes', ' casserole', ' dish']:
        test_name = normalized.replace(suffix, '')
        if test_name in nutrition_db:
            return nutrition_db[test_name]

    # Try partial matches
    for db_name, data in nutrition_db.items():
        if db_name in normalized or normalized in db_name:
            return data

    return None

def main():
    with open('data/recipes.json') as f:
        data = json.load(f)

    recipes = data.get('recipes', [])

    # Combine all nutrition databases
    all_nutrition = {}
    all_nutrition.update({normalize_name(k): v for k, v in CANDY_NUTRITION.items()})
    all_nutrition.update({normalize_name(k): v for k, v in COOKIES_NUTRITION.items()})
    all_nutrition.update({normalize_name(k): v for k, v in EGGS_CHEESE_LEGUMES_NUTRITION.items()})
    all_nutrition.update({normalize_name(k): v for k, v in SALADS_NUTRITION.items()})

    updated = 0
    matched_names = set()

    for recipe in recipes:
        if not isinstance(recipe, dict):
            continue

        title = recipe.get('title', '')
        category = recipe.get('category', '')

        # Only update if not already complete
        nutrition = recipe.get('nutrition', {})
        if nutrition.get('status') == 'complete':
            continue

        # Try to match
        match = match_recipe(title, all_nutrition)
        if match:
            recipe['nutrition'] = {
                'status': 'complete',
                'per_serving': {
                    'calories': match.get('calories', 0),
                    'fat_g': match.get('fat_g', 0),
                    'protein_g': match.get('protein_g', 0),
                    'carbs_g': match.get('carbs_g', 0),
                    'cholesterol_mg': match.get('cholesterol_mg', 0),
                    'sodium_mg': match.get('sodium_mg', 0)
                },
                'source': 'Better Homes and Gardens cookbook nutrition analysis',
                'assumptions': []
            }
            updated += 1
            matched_names.add(title)

    # Save
    with open('data/recipes.json', 'w') as f:
        json.dump(data, f, indent=2)

    print(f"Total nutrition entries in database: {len(all_nutrition)}")
    print(f"Updated {updated} recipes with complete nutrition")
    print(f"\nMatched recipes:")
    for name in sorted(matched_names):
        print(f"  - {name}")

if __name__ == '__main__':
    main()
