#!/usr/bin/env python3
"""
Add Eat the Weeds recipes - Batch 10
Recipes from: cranberry/lingonberry article
"""

import json
from pathlib import Path

RECIPES_FILE = Path(__file__).parent.parent / "data" / "recipes.json"

ETW_BATCH10_RECIPES = [
    # ===== CRANBERRY RECIPES =====
    {
        "id": "cranberry-sauce-etw",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Cranberry Sauce",
        "category": "preserves",
        "attribution": "Eat the Weeds",
        "source_note": "From eattheweeds.com - Cranberry/Lingonberry article",
        "description": "A simple two-ingredient cranberry sauce.",
        "servings_yield": "about 3 cups",
        "prep_time": "5 minutes",
        "cook_time": "10 minutes",
        "ingredients": [
            {"item": "cranberries", "quantity": "4", "unit": "cups"},
            {"item": "sugar", "quantity": "2", "unit": "cups"}
        ],
        "instructions": [
            {"step": 1, "text": "Wash berries."},
            {"step": 2, "text": "Add sugar to berries, stirring thoroughly."},
            {"step": 3, "text": "Cook slowly without additional water (just what remains from washing)."},
            {"step": 4, "text": "Boil for 10 minutes."}
        ],
        "temperature": "",
        "pan_size": "",
        "notes": ["No additional water needed - the washing water is sufficient"],
        "tags": ["cranberry", "sauce", "thanksgiving", "holiday", "preserves"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "spiced-cranberries-etw",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Spiced Cranberries",
        "category": "preserves",
        "attribution": "Eat the Weeds",
        "source_note": "From eattheweeds.com - Cranberry/Lingonberry article",
        "description": "Tangy spiced cranberries preserved in vinegar with warm spices.",
        "servings_yield": "several pints",
        "prep_time": "10 minutes",
        "cook_time": "2 hours",
        "ingredients": [
            {"item": "cranberries", "quantity": "5", "unit": "lb"},
            {"item": "white vinegar", "quantity": "3.5", "unit": "cups"},
            {"item": "cinnamon or allspice", "quantity": "2", "unit": "tbsp"},
            {"item": "cloves", "quantity": "1", "unit": "tbsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Combine all ingredients in a large pot."},
            {"step": 2, "text": "Boil for 2 hours."},
            {"step": 3, "text": "Place in hot sterilized jars and seal."}
        ],
        "temperature": "",
        "pan_size": "large pot",
        "notes": ["For canning - use proper canning procedures"],
        "tags": ["cranberry", "spiced", "preserves", "canning", "holiday"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "cranberry-orange-relish-etw",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Cranberry Orange Relish",
        "category": "preserves",
        "attribution": "Eat the Weeds",
        "source_note": "From eattheweeds.com - Cranberry/Lingonberry article",
        "description": "A fresh, no-cook cranberry orange relish.",
        "servings_yield": "2 pints",
        "prep_time": "15 minutes",
        "cook_time": "",
        "ingredients": [
            {"item": "cranberries", "quantity": "4", "unit": "cups", "prep_note": "about 1 lb"},
            {"item": "oranges", "quantity": "2", "unit": "", "prep_note": "quartered, seeds removed"},
            {"item": "sugar", "quantity": "2", "unit": "cups"}
        ],
        "instructions": [
            {"step": 1, "text": "Put berries and oranges (including rind) through food grinder using coarse blade."},
            {"step": 2, "text": "Stir in sugar."},
            {"step": 3, "text": "Chill before serving."}
        ],
        "temperature": "",
        "pan_size": "",
        "notes": ["Keeps several weeks refrigerated", "Include the orange rind for best flavor"],
        "tags": ["cranberry", "orange", "relish", "no-cook", "thanksgiving", "holiday"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "cranberry-punch-etw",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Cranberry Punch",
        "category": "beverages",
        "attribution": "Eat the Weeds",
        "source_note": "From eattheweeds.com - Cranberry/Lingonberry article",
        "description": "A festive cranberry punch with citrus and ginger ale.",
        "servings_yield": "about 3 quarts",
        "prep_time": "20 minutes",
        "cook_time": "15 minutes",
        "ingredients": [
            {"item": "cranberries", "quantity": "1", "unit": "quart"},
            {"item": "water", "quantity": "6", "unit": "cups", "prep_note": "divided"},
            {"item": "sugar", "quantity": "2", "unit": "cups"},
            {"item": "orange juice", "quantity": "1", "unit": "cup"},
            {"item": "lemon juice", "quantity": "3", "unit": "tbsp"},
            {"item": "ginger ale", "quantity": "1", "unit": "quart"}
        ],
        "instructions": [
            {"step": 1, "text": "Cook berries in 4 cups water until soft."},
            {"step": 2, "text": "Crush and drain through cheesecloth."},
            {"step": 3, "text": "Boil sugar and remaining 2 cups water for 5 minutes."},
            {"step": 4, "text": "Add sugar syrup to berry juice and chill."},
            {"step": 5, "text": "Add orange juice and lemon juice."},
            {"step": 6, "text": "Just before serving, add ginger ale."}
        ],
        "temperature": "",
        "pan_size": "",
        "notes": ["Add ginger ale just before serving to keep it fizzy"],
        "tags": ["cranberry", "punch", "beverage", "holiday", "party"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "cranberry-salsa-etw",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Cranberry Salsa",
        "category": "preserves",
        "attribution": "Eat the Weeds",
        "source_note": "From eattheweeds.com - Cranberry/Lingonberry article",
        "description": "A unique cranberry salsa with cilantro, jalapeño, and lime.",
        "servings_yield": "about 3 cups",
        "prep_time": "15 minutes",
        "cook_time": "",
        "ingredients": [
            {"item": "cranberries", "quantity": "12", "unit": "oz", "prep_note": "fresh or frozen"},
            {"item": "cilantro", "quantity": "1", "unit": "bunch", "prep_note": "chopped"},
            {"item": "green onions", "quantity": "1", "unit": "bunch", "prep_note": "cut into 3-inch lengths"},
            {"item": "jalapeño pepper", "quantity": "1", "unit": "", "prep_note": "seeded and minced"},
            {"item": "limes", "quantity": "2", "unit": "", "prep_note": "juiced"},
            {"item": "white sugar", "quantity": "3/4", "unit": "cup"},
            {"item": "salt", "quantity": "1", "unit": "pinch"}
        ],
        "instructions": [
            {"step": 1, "text": "Combine all ingredients in food processor fitted with medium blade."},
            {"step": 2, "text": "Chop to medium consistency."},
            {"step": 3, "text": "Refrigerate if not using immediately."},
            {"step": 4, "text": "Serve at room temperature."}
        ],
        "temperature": "",
        "pan_size": "",
        "notes": ["Great with tortilla chips or as a topping for turkey"],
        "tags": ["cranberry", "salsa", "cilantro", "lime", "holiday", "appetizer"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "cranberry-muffins-etw",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Cranberry Muffins",
        "category": "breads",
        "attribution": "Eat the Weeds",
        "source_note": "From eattheweeds.com - Cranberry/Lingonberry article",
        "description": "Hearty whole wheat and oat muffins studded with cranberries.",
        "servings_yield": "12 muffins",
        "prep_time": "15 minutes",
        "cook_time": "18-20 minutes",
        "ingredients": [
            {"item": "whole wheat flour", "quantity": "1", "unit": "cup"},
            {"item": "rolled oats", "quantity": "1", "unit": "cup"},
            {"item": "2% milk", "quantity": "1", "unit": "cup", "prep_note": "soured"},
            {"item": "canola oil", "quantity": "1/4", "unit": "cup"},
            {"item": "brown sugar", "quantity": "1/2", "unit": "cup"},
            {"item": "egg", "quantity": "1", "unit": "large"},
            {"item": "cranberries", "quantity": "1.5", "unit": "cups"},
            {"item": "baking powder", "quantity": "1", "unit": "tsp"},
            {"item": "baking soda", "quantity": "1/2", "unit": "tsp"},
            {"item": "salt", "quantity": "1/2", "unit": "tsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Combine milk and oats and let stand."},
            {"step": 2, "text": "Mix egg, oil, and brown sugar together."},
            {"step": 3, "text": "Mix dry ingredients (flour, baking powder, baking soda, salt)."},
            {"step": 4, "text": "Add berries to dry ingredients and toss until coated."},
            {"step": 5, "text": "Mix all ingredients together just until blended."},
            {"step": 6, "text": "Fill greased muffin cups."},
            {"step": 7, "text": "Bake at 350°F for 18-20 minutes."}
        ],
        "temperature": "350°F (175°C)",
        "pan_size": "12-cup muffin tin",
        "notes": ["Sour the milk by adding 1 tbsp lemon juice or vinegar", "Don't overmix the batter"],
        "tags": ["cranberry", "muffins", "whole wheat", "oats", "breakfast", "baking"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    }
]


def main():
    print(f"Loading recipes from {RECIPES_FILE}")
    with open(RECIPES_FILE, 'r') as f:
        data = json.load(f)

    recipes = data['recipes']
    existing_ids = {r['id'] for r in recipes}
    print(f"Found {len(recipes)} existing recipes")

    added = 0
    skipped = 0

    for recipe in ETW_BATCH10_RECIPES:
        if recipe['id'] in existing_ids:
            print(f"  Skipping duplicate: {recipe['id']}")
            skipped += 1
        else:
            recipes.append(recipe)
            existing_ids.add(recipe['id'])
            print(f"  Added: {recipe['title']}")
            added += 1

    data['meta']['total_recipes'] = len(recipes)

    print(f"\nWriting {len(recipes)} recipes to {RECIPES_FILE}")
    with open(RECIPES_FILE, 'w') as f:
        json.dump(data, f, indent=2)

    print(f"\nSummary:")
    print(f"  Added: {added} new Eat the Weeds recipes (batch 10)")
    print(f"  Skipped: {skipped} duplicates")
    print(f"  Total recipes now: {len(recipes)}")


if __name__ == "__main__":
    main()
