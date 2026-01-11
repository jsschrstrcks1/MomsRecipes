#!/usr/bin/env python3
"""Apply meat and soup nutrition data from Better Homes and Gardens cookbook."""

import json
import re

# Meat nutrition data from page 208
MEAT_NUTRITION = {
    "meatballs with oven browned gravy": {"servings": 4, "calories": 361, "protein_g": 25, "carbs_g": 9, "fat_g": 25, "sodium_mg": 462, "cholesterol_mg": 123},
    "spaghetti with meat sauce": {"servings": 4, "calories": 473, "protein_g": 25, "carbs_g": 51, "fat_g": 18, "sodium_mg": 551, "cholesterol_mg": 57},
    "stuffed burgers": {"servings": 4, "calories": 364, "protein_g": 27, "carbs_g": 4, "fat_g": 27, "sodium_mg": 294, "cholesterol_mg": 20},
    "stuffed cabbage rolls": {"servings": 4, "calories": 244, "protein_g": 18, "carbs_g": 21, "fat_g": 10, "sodium_mg": 706, "cholesterol_mg": 65},
    "stuffed peppers": {"servings": 4, "calories": 226, "protein_g": 18, "carbs_g": 21, "fat_g": 8, "sodium_mg": 726, "cholesterol_mg": 50},
    "stuffed zucchini": {"servings": 4, "calories": 191, "protein_g": 18, "carbs_g": 9, "fat_g": 10, "sodium_mg": 269, "cholesterol_mg": 50},
    "swiss steak": {"servings": 4, "calories": 267, "protein_g": 31, "carbs_g": 4, "fat_g": 14, "sodium_mg": 786, "cholesterol_mg": 90},
    "taco pizza": {"servings": 4, "calories": 397, "protein_g": 30, "carbs_g": 31, "fat_g": 18, "sodium_mg": 239, "cholesterol_mg": 52},
    "texas-style beef brisket": {"servings": 12, "calories": 324, "protein_g": 26, "carbs_g": 8, "fat_g": 21, "sodium_mg": 211, "cholesterol_mg": 79},
    "veal cordon bleu": {"servings": 8, "calories": 211, "protein_g": 34, "carbs_g": 22, "fat_g": 10, "sodium_mg": 215, "cholesterol_mg": 79},
    "veal marsala": {"servings": 4, "calories": 329, "protein_g": 34, "carbs_g": 6, "fat_g": 17, "sodium_mg": 344, "cholesterol_mg": 79},
    "vegetable stuffed rouladen": {"servings": 4, "calories": 376, "protein_g": 30, "carbs_g": 7, "fat_g": 25, "sodium_mg": 292, "cholesterol_mg": 79},
    "zesty pork roast": {"servings": 17, "calories": 282, "protein_g": 25, "carbs_g": 3, "fat_g": 18, "sodium_mg": 114, "cholesterol_mg": 79},
    "veal roll-ups": {"servings": 3, "calories": 383, "protein_g": 26, "carbs_g": 2, "fat_g": 30, "sodium_mg": 330, "cholesterol_mg": 79},
    "saucy lamb shanks": {"servings": 4, "calories": 597, "protein_g": 39, "carbs_g": 31, "fat_g": 35, "sodium_mg": 766, "cholesterol_mg": 138},
    "saucy pork chops": {"servings": 4, "calories": 269, "protein_g": 22, "carbs_g": 8, "fat_g": 17, "sodium_mg": 218, "cholesterol_mg": 56},
    "pot roast": {"servings": 8, "calories": 303, "protein_g": 31, "carbs_g": 9, "fat_g": 15, "sodium_mg": 56, "cholesterol_mg": 90},
    "pork chops with apple glaze": {"servings": 4, "calories": 324, "protein_g": 22, "carbs_g": 8, "fat_g": 23, "sodium_mg": 143, "cholesterol_mg": 79},
    "pork roast with apple stuffing": {"servings": 8, "calories": 324, "protein_g": 22, "carbs_g": 15, "fat_g": 19, "sodium_mg": 161, "cholesterol_mg": 79},
    "oven swiss steak": {"servings": 6, "calories": 334, "protein_g": 29, "carbs_g": 8, "fat_g": 21, "sodium_mg": 323, "cholesterol_mg": 90},
    "orange-glazed ribs": {"servings": 4, "calories": 519, "protein_g": 25, "carbs_g": 16, "fat_g": 40, "sodium_mg": 234, "cholesterol_mg": 100},
    "onion-smothered steak": {"servings": 4, "calories": 267, "protein_g": 26, "carbs_g": 7, "fat_g": 14, "sodium_mg": 232, "cholesterol_mg": 72},
    "new england boiled dinner": {"servings": 8, "calories": 473, "protein_g": 26, "carbs_g": 30, "fat_g": 27, "sodium_mg": 232, "cholesterol_mg": 79},
    "meat loaf": {"servings": 8, "calories": 254, "protein_g": 17, "carbs_g": 13, "fat_g": 15, "sodium_mg": 339, "cholesterol_mg": 95},
    "marinated blade steak": {"servings": 4, "calories": 218, "protein_g": 22, "carbs_g": 2, "fat_g": 13, "sodium_mg": 256, "cholesterol_mg": 79},
    "lemon-herb lamb roast": {"servings": 10, "calories": 157, "protein_g": 23, "carbs_g": 1, "fat_g": 6, "sodium_mg": 61, "cholesterol_mg": 79},
    "lamb chops supreme": {"servings": 4, "calories": 326, "protein_g": 30, "carbs_g": 1, "fat_g": 22, "sodium_mg": 131, "cholesterol_mg": 110},
    "lamb chops with mint": {"servings": 4, "calories": 252, "protein_g": 22, "carbs_g": 7, "fat_g": 15, "sodium_mg": 68, "cholesterol_mg": 79},
    "honey-lime lamb chops": {"servings": 4, "calories": 198, "protein_g": 22, "carbs_g": 8, "fat_g": 8, "sodium_mg": 72, "cholesterol_mg": 79},
    "hamburgers": {"servings": 4, "calories": 243, "protein_g": 22, "carbs_g": 0, "fat_g": 16, "sodium_mg": 68, "cholesterol_mg": 79},
    "grilled ham slice": {"servings": 6, "calories": 234, "protein_g": 23, "carbs_g": 12, "fat_g": 10, "sodium_mg": 1509, "cholesterol_mg": 50},
    "glazed ham": {"servings": 20, "calories": 234, "protein_g": 23, "carbs_g": 12, "fat_g": 10, "sodium_mg": 1509, "cholesterol_mg": 50},
    "glazed ham balls": {"servings": 6, "calories": 375, "protein_g": 19, "carbs_g": 28, "fat_g": 21, "sodium_mg": 1095, "cholesterol_mg": 137},
    "ginger-glazed pork roast": {"servings": 8, "calories": 324, "protein_g": 22, "carbs_g": 8, "fat_g": 23, "sodium_mg": 261, "cholesterol_mg": 79},
    "beer braised rabbit": {"servings": 6, "calories": 391, "protein_g": 32, "carbs_g": 12, "fat_g": 22, "sodium_mg": 549, "cholesterol_mg": 149},
    "beef bourguignon": {"servings": 6, "calories": 368, "protein_g": 28, "carbs_g": 12, "fat_g": 22, "sodium_mg": 462, "cholesterol_mg": 79},
    "beef and brew": {"servings": 8, "calories": 310, "protein_g": 28, "carbs_g": 19, "fat_g": 12, "sodium_mg": 653, "cholesterol_mg": 79},
}

# Soup nutrition data from page 370
SOUP_NUTRITION = {
    "alphabet meatball soup": {"servings": 4, "calories": 380, "protein_g": 23, "carbs_g": 12, "fat_g": 27, "sodium_mg": 1103, "cholesterol_mg": 972},
    "barley-beef soup": {"servings": 4, "calories": 318, "protein_g": 25, "carbs_g": 31, "fat_g": 11, "sodium_mg": 12, "cholesterol_mg": 1096},
    "bean and sausage soup": {"servings": 4, "calories": 404, "protein_g": 20, "carbs_g": 38, "fat_g": 14, "sodium_mg": 381, "cholesterol_mg": 689},
    "beef bourguignonne": {"servings": 6, "calories": 368, "protein_g": 28, "carbs_g": 12, "fat_g": 22, "sodium_mg": 462, "cholesterol_mg": 79},
    "beef broth": {"servings": 8, "calories": 0, "protein_g": 0, "carbs_g": 0, "fat_g": 0, "sodium_mg": 965, "cholesterol_mg": 0},
    "beef stew": {"servings": 4, "calories": 378, "protein_g": 28, "carbs_g": 12, "fat_g": 22, "sodium_mg": 463, "cholesterol_mg": 289},
    "beer cheese soup": {"servings": 5, "calories": 440, "protein_g": 18, "carbs_g": 18, "fat_g": 32, "sodium_mg": 1334, "cholesterol_mg": 714},
    "black bean soup": {"servings": 4, "calories": 182, "protein_g": 9, "carbs_g": 5, "fat_g": 11, "sodium_mg": 71, "cholesterol_mg": 43},
    "cheese dumplings for stew": {"servings": 4, "calories": 182, "protein_g": 5, "carbs_g": 5, "fat_g": 11, "sodium_mg": 374, "cholesterol_mg": 43},
    "cheese soup": {"servings": 5, "calories": 159, "protein_g": 9, "carbs_g": 7, "fat_g": 10, "sodium_mg": 374, "cholesterol_mg": 578},
    "chicken and sausage gumbo": {"servings": 4, "calories": 506, "protein_g": 29, "carbs_g": 28, "fat_g": 31, "sodium_mg": 874, "cholesterol_mg": 578},
    "chicken broth": {"servings": 5, "calories": 0, "protein_g": 0, "carbs_g": 0, "fat_g": 0, "sodium_mg": 426, "cholesterol_mg": 0},
    "chicken noodle soup": {"servings": 4, "calories": 232, "protein_g": 25, "carbs_g": 21, "fat_g": 6, "sodium_mg": 67, "cholesterol_mg": 754},
    "chicken stew with dumplings": {"servings": 4, "calories": 357, "protein_g": 24, "carbs_g": 41, "fat_g": 11, "sodium_mg": 0, "cholesterol_mg": 1183},
    "chicken vegetable soup": {"servings": 4, "calories": 216, "protein_g": 24, "carbs_g": 34, "fat_g": 55, "sodium_mg": 14, "sodium_mg": 529},
    "chili": {"servings": 4, "calories": 466, "protein_g": 34, "carbs_g": 35, "fat_g": 14, "sodium_mg": 727, "cholesterol_mg": 1171},
    "cioppino": {"servings": 5, "calories": 143, "protein_g": 12, "carbs_g": 12, "fat_g": 2, "sodium_mg": 50, "cholesterol_mg": 539},
    "corn chowder": {"servings": 4, "calories": 186, "protein_g": 7, "carbs_g": 28, "fat_g": 6, "sodium_mg": 8, "cholesterol_mg": 286},
    "cream of acorn squash soup": {"servings": 3, "calories": 139, "protein_g": 4, "carbs_g": 0, "fat_g": 9, "sodium_mg": 992, "cholesterol_mg": 665},
    "cream of asparagus soup": {"servings": 3, "calories": 118, "protein_g": 4, "carbs_g": 7, "fat_g": 6, "sodium_mg": 299, "cholesterol_mg": 9},
    "cream of broccoli soup": {"servings": 3, "calories": 114, "protein_g": 6, "carbs_g": 7, "fat_g": 6, "sodium_mg": 9, "cholesterol_mg": 299},
    "cream of brussels sprout soup": {"servings": 3, "calories": 124, "protein_g": 6, "carbs_g": 17, "fat_g": 6, "sodium_mg": 409, "cholesterol_mg": 458},
    "cream of carrot soup": {"servings": 3, "calories": 131, "protein_g": 4, "carbs_g": 17, "fat_g": 6, "sodium_mg": 6, "cholesterol_mg": 456},
    "cream of cauliflower soup": {"servings": 3, "calories": 111, "protein_g": 5, "carbs_g": 11, "fat_g": 6, "sodium_mg": 6, "cholesterol_mg": 414},
    "cream of celery soup": {"servings": 3, "calories": 99, "protein_g": 4, "carbs_g": 9, "fat_g": 6, "sodium_mg": 694, "cholesterol_mg": 492},
    "cream of chicken soup": {"servings": 3, "calories": 286, "protein_g": 23, "carbs_g": 9, "fat_g": 28, "sodium_mg": 115, "cholesterol_mg": 608},
    "cream of green bean soup": {"servings": 3, "calories": 113, "protein_g": 5, "carbs_g": 11, "fat_g": 6, "sodium_mg": 6, "cholesterol_mg": 390},
    "cream of mushroom soup": {"servings": 3, "calories": 111, "protein_g": 5, "carbs_g": 11, "fat_g": 6, "sodium_mg": 6, "cholesterol_mg": 590},
    "cream of onion soup": {"servings": 3, "calories": 124, "protein_g": 4, "carbs_g": 11, "fat_g": 6, "sodium_mg": 417, "cholesterol_mg": 343},
    "cream of pea soup": {"servings": 3, "calories": 174, "protein_g": 8, "carbs_g": 23, "fat_g": 6, "sodium_mg": 6, "cholesterol_mg": 391},
    "cream of potato soup": {"servings": 3, "calories": 174, "protein_g": 5, "carbs_g": 27, "fat_g": 6, "sodium_mg": 6, "cholesterol_mg": 392},
    "cream of spinach soup": {"servings": 3, "calories": 109, "protein_g": 6, "carbs_g": 10, "fat_g": 6, "sodium_mg": 6, "cholesterol_mg": 464},
    "cream of zucchini soup": {"servings": 3, "calories": 103, "protein_g": 4, "carbs_g": 11, "fat_g": 5, "sodium_mg": 6, "cholesterol_mg": 391},
    "dumplings for stew": {"servings": 4, "calories": 144, "protein_g": 3, "carbs_g": 17, "fat_g": 7, "sodium_mg": 1, "cholesterol_mg": 150},
    "fish chowder": {"servings": 4, "calories": 468, "protein_g": 39, "carbs_g": 37, "fat_g": 18, "sodium_mg": 136, "cholesterol_mg": 936},
    "french onion soup": {"servings": 4, "calories": 270, "protein_g": 11, "carbs_g": 13, "fat_g": 24, "sodium_mg": 624, "cholesterol_mg": 184},
    "gazpacho": {"servings": 4, "calories": 57, "protein_g": 2, "carbs_g": 9, "fat_g": 3, "sodium_mg": 0, "cholesterol_mg": 291},
    "gingered cream of chicken soup": {"servings": 3, "calories": 386, "protein_g": 23, "carbs_g": 23, "fat_g": 18, "sodium_mg": 115, "cholesterol_mg": 608},
    "ham and bean soup": {"servings": 4, "calories": 226, "protein_g": 18, "carbs_g": 33, "fat_g": 3, "sodium_mg": 19, "cholesterol_mg": 742},
    "herbed lamb stew": {"servings": 4, "calories": 451, "protein_g": 29, "carbs_g": 19, "fat_g": 30, "sodium_mg": 19, "cholesterol_mg": 407},
    "herbed tomato soup": {"servings": 4, "calories": 93, "protein_g": 2, "carbs_g": 10, "fat_g": 6, "sodium_mg": 6, "cholesterol_mg": 578},
    "lentil stew": {"servings": 4, "calories": 466, "protein_g": 26, "carbs_g": 42, "fat_g": 22, "sodium_mg": 39, "cholesterol_mg": 1261},
    "manhattan clam chowder": {"servings": 4, "calories": 213, "protein_g": 13, "carbs_g": 32, "fat_g": 4, "sodium_mg": 34, "cholesterol_mg": 970},
    "minestrone": {"servings": 5, "calories": 80, "protein_g": 4, "carbs_g": 12, "fat_g": 2, "sodium_mg": 3, "cholesterol_mg": 230},
    "mulligatawny": {"servings": 3, "calories": 302, "protein_g": 24, "carbs_g": 8, "fat_g": 52, "sodium_mg": 60, "cholesterol_mg": 864},
    "new england clam chowder": {"servings": 4, "calories": 323, "protein_g": 24, "carbs_g": 43, "fat_g": 8, "sodium_mg": 52, "cholesterol_mg": 60},
    "oyster stew": {"servings": 4, "calories": 393, "protein_g": 18, "carbs_g": 34, "fat_g": 20, "sodium_mg": 90, "cholesterol_mg": 864},
    "quick minestrone": {"servings": 4, "calories": 266, "protein_g": 14, "carbs_g": 13, "fat_g": 17, "sodium_mg": 18, "cholesterol_mg": 496},
    "quick vegetable-beef soup": {"servings": 5, "calories": 311, "protein_g": 23, "carbs_g": 17, "fat_g": 18, "sodium_mg": 323, "cholesterol_mg": 655},
    "seafood gumbo": {"servings": 4, "calories": 589, "protein_g": 32, "carbs_g": 42, "fat_g": 32, "sodium_mg": 144, "cholesterol_mg": 1271},
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
    for suffix in [' recipe', ' recipes']:
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

    # Combine nutrition databases
    all_nutrition = {}
    all_nutrition.update({normalize_name(k): v for k, v in MEAT_NUTRITION.items()})
    all_nutrition.update({normalize_name(k): v for k, v in SOUP_NUTRITION.items()})

    updated = 0
    matched_names = []

    for recipe in recipes:
        if not isinstance(recipe, dict):
            continue

        title = recipe.get('title', '')
        category = recipe.get('category', '')

        # Only process meat and soups categories, or if not already complete
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
            matched_names.append(title)

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
