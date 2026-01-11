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
                qty = 1  # Default assumption
                assumptions.append(f"Assumed 1 unit for {item}")

        # Get nutrition data
        nut_data = NUTRITION_DB[match]

        # Calculate multiplier based on unit
        multiplier = qty
        unit_lower = unit.lower() if unit else ''

        # Handle special cases
        if match in ['butter', 'margarine'] and unit_lower in ['stick', 'sticks']:
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
