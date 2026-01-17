#!/usr/bin/env python3
"""
Add Eat the Weeds recipes - Batch 8
Recipes from: root beer, garum
"""

import json
from pathlib import Path

RECIPES_FILE = Path(__file__).parent.parent / "data" / "recipes.json"

ETW_BATCH8_RECIPES = [
    # ===== ROOT BEER =====
    {
        "id": "homemade-root-beer-etw",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Homemade Root Beer",
        "category": "beverages",
        "attribution": "Eat the Weeds / herb lover",
        "source_note": "From eattheweeds.com - Root Beer Rat Killer article comments",
        "description": "A traditional homemade root beer using foraged botanicals and natural ingredients.",
        "servings_yield": "about 6 quarts",
        "prep_time": "30 minutes",
        "cook_time": "1 hour",
        "ingredients": [
            {"item": "water", "quantity": "6", "unit": "quarts"},
            {"item": "honey", "quantity": "3", "unit": "lb"},
            {"item": "licorice root", "quantity": "1", "unit": "oz"},
            {"item": "star anise", "quantity": "3", "unit": ""},
            {"item": "cinnamon stick", "quantity": "1", "unit": ""},
            {"item": "salt", "quantity": "1/2", "unit": "tsp"},
            {"item": "sassafras root", "quantity": "1", "unit": "oz"},
            {"item": "smilex root (sarsaparilla)", "quantity": "1", "unit": "oz"},
            {"item": "black cherry bark", "quantity": "1", "unit": "oz"},
            {"item": "molasses", "quantity": "1/2", "unit": "cup"},
            {"item": "sugar", "quantity": "6", "unit": "cups"},
            {"item": "vanilla bean", "quantity": "1", "unit": ""},
            {"item": "raisins", "quantity": "1/4", "unit": "cup"},
            {"item": "nutmeg", "quantity": "1/8", "unit": "tsp"},
            {"item": "cherries", "quantity": "3", "unit": ""},
            {"item": "juniper berries", "quantity": "50", "unit": ""},
            {"item": "wintergreen", "quantity": "1", "unit": "oz"}
        ],
        "instructions": [
            {"step": 1, "text": "Combine all ingredients in a large pot."},
            {"step": 2, "text": "Boil together for 1 hour."},
            {"step": 3, "text": "Strain the mixture through cheesecloth or fine mesh strainer."},
            {"step": 4, "text": "Carbonate the strained liquid using your preferred method (natural fermentation with yeast or force carbonation)."}
        ],
        "temperature": "",
        "pan_size": "large stockpot",
        "notes": [
            "Traditional root beer uses sassafras which contains safrole - use sparingly or substitute sassafras flavoring",
            "For natural carbonation, add champagne yeast and bottle in pressure-safe containers",
            "Smilex is another name for sarsaparilla"
        ],
        "tags": ["root beer", "beverage", "soda", "foraged", "traditional", "homemade"],
        "confidence": {"overall": "high", "flags": ["sassafras safety note"]},
        "image_refs": []
    },

    # ===== GARUM (modern interpretations) =====
    {
        "id": "josep-mercader-garum-etw",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Josep Mercader's Garum",
        "category": "preserves",
        "attribution": "Eat the Weeds / Josep Mercader",
        "source_note": "From eattheweeds.com - Fish Sauce article",
        "description": "A modern interpretation of ancient Roman garum using olives, anchovies, and fresh herbs.",
        "servings_yield": "about 2 cups",
        "prep_time": "20 minutes",
        "cook_time": "",
        "ingredients": [
            {"item": "black olives", "quantity": "560", "unit": "g", "prep_note": "stones removed"},
            {"item": "anchovy fillets", "quantity": "16", "unit": "", "prep_note": "soaked in water 1 hour, patted dry"},
            {"item": "hard-boiled egg yolk", "quantity": "1", "unit": ""},
            {"item": "capers", "quantity": "90", "unit": "g"},
            {"item": "garlic", "quantity": "1", "unit": "clove", "prep_note": "finely chopped"},
            {"item": "grainy mustard", "quantity": "1", "unit": "tsp"},
            {"item": "fresh parsley", "quantity": "1", "unit": "tbsp", "prep_note": "finely chopped"},
            {"item": "fresh marjoram", "quantity": "1", "unit": "tbsp", "prep_note": "finely chopped"},
            {"item": "fresh rosemary", "quantity": "1", "unit": "tbsp", "prep_note": "finely chopped"},
            {"item": "fresh thyme", "quantity": "1", "unit": "tbsp", "prep_note": "finely chopped"},
            {"item": "white pepper", "quantity": "1", "unit": "tsp"},
            {"item": "olive oil", "quantity": "60", "unit": "ml"}
        ],
        "instructions": [
            {"step": 1, "text": "Combine all ingredients in a blender or food processor."},
            {"step": 2, "text": "Process until light and fluffy."},
            {"step": 3, "text": "Pass mixture through a food mill or push through a sieve with a wooden spoon."},
            {"step": 4, "text": "Return to blender or processor and briefly process until smooth."},
            {"step": 5, "text": "Refrigerate until ready to use."}
        ],
        "temperature": "",
        "pan_size": "",
        "notes": ["Use fresh herbs only - do not substitute dried", "Store refrigerated"],
        "tags": ["garum", "roman", "anchovy", "condiment", "sauce", "mediterranean"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "quick-garum-etw",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Quick Garum",
        "category": "preserves",
        "attribution": "Eat the Weeds",
        "source_note": "From eattheweeds.com - Fish Sauce article",
        "description": "A quick approximation of ancient Roman garum using grape juice and anchovy paste.",
        "servings_yield": "about 1/2 cup",
        "prep_time": "5 minutes",
        "cook_time": "30-45 minutes",
        "ingredients": [
            {"item": "grape juice", "quantity": "1", "unit": "quart"},
            {"item": "anchovy paste", "quantity": "2", "unit": "tbsp"},
            {"item": "oregano", "quantity": "1", "unit": "pinch"}
        ],
        "instructions": [
            {"step": 1, "text": "Cook grape juice over medium heat, reducing to one-tenth its original volume (about 3/4 cup)."},
            {"step": 2, "text": "Dilute anchovy paste in the concentrated juice."},
            {"step": 3, "text": "Mix in a pinch of oregano."}
        ],
        "temperature": "",
        "pan_size": "",
        "notes": ["A quick substitute for traditional fermented garum", "Use as a savory condiment"],
        "tags": ["garum", "roman", "anchovy", "condiment", "quick", "sauce"],
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

    for recipe in ETW_BATCH8_RECIPES:
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
    print(f"  Added: {added} new Eat the Weeds recipes (batch 8)")
    print(f"  Skipped: {skipped} duplicates")
    print(f"  Total recipes now: {len(recipes)}")


if __name__ == "__main__":
    main()
