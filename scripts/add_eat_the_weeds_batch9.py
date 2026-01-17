#!/usr/bin/env python3
"""
Add Eat the Weeds recipes - Batch 9
Recipes from: codium, sea blite, lemongrass
"""

import json
from pathlib import Path

RECIPES_FILE = Path(__file__).parent.parent / "data" / "recipes.json"

ETW_BATCH9_RECIPES = [
    # ===== CODIUM (SEAWEED) =====
    {
        "id": "codium-salad-etw",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Codium Salad",
        "category": "salads",
        "attribution": "Eat the Weeds",
        "source_note": "From eattheweeds.com - Codiums article",
        "description": "A refreshing raw seaweed salad with Asian-inspired dressing.",
        "servings_yield": "4 servings",
        "prep_time": "15 minutes",
        "cook_time": "",
        "ingredients": [
            {"item": "codium seaweed", "quantity": "4", "unit": "cups", "prep_note": "well cleaned"},
            {"item": "sweet onion", "quantity": "1", "unit": "small"},
            {"item": "tomato", "quantity": "1", "unit": "medium"},
            {"item": "soy sauce", "quantity": "1/4", "unit": "cup"},
            {"item": "wine vinegar", "quantity": "2", "unit": "tsp"},
            {"item": "sugar", "quantity": "2", "unit": "tsp"},
            {"item": "sherry", "quantity": "1/4", "unit": "cup"},
            {"item": "black pepper", "quantity": "1", "unit": "tsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Mix all dressing ingredients (soy sauce, wine vinegar, sugar, sherry, and black pepper) together."},
            {"step": 2, "text": "Pour the dressing over chopped onions."},
            {"step": 3, "text": "Just before serving, chop the tomatoes and codium into bite-sized pieces."},
            {"step": 4, "text": "Toss the chopped tomatoes and seaweed with the dressed onions."},
            {"step": 5, "text": "Garnish with tomato slices."},
            {"step": 6, "text": "Chill before serving."}
        ],
        "temperature": "",
        "pan_size": "",
        "notes": ["Never cook codium - it becomes soft and disintegrates from heat", "Always eat raw after thorough washing"],
        "tags": ["seaweed", "codium", "salad", "raw", "asian", "foraged"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },

    # ===== SEA BLITE RECIPES =====
    {
        "id": "sea-blite-sour-cream-salad-etw",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Sea Blite and Sour Cream Salad",
        "category": "salads",
        "attribution": "Eat the Weeds",
        "source_note": "From eattheweeds.com - Sea Blite article",
        "description": "A creamy salad featuring foraged sea blite with hard-boiled eggs.",
        "servings_yield": "4-6 servings",
        "prep_time": "20 minutes",
        "cook_time": "10 minutes",
        "total_time": "2 hours 30 minutes (including refrigeration)",
        "ingredients": [
            {"item": "sea blite leaves, stems, or flowers", "quantity": "4", "unit": "cups", "prep_note": "cooked, drained, chopped"},
            {"item": "sugar", "quantity": "1", "unit": "tbsp"},
            {"item": "sour cream", "quantity": "1", "unit": "cup"},
            {"item": "onion", "quantity": "3", "unit": "tbsp", "prep_note": "grated"},
            {"item": "vinegar or lemon juice", "quantity": "2", "unit": "tbsp"},
            {"item": "hard-cooked eggs", "quantity": "2", "unit": "", "prep_note": "diced"},
            {"item": "salt", "quantity": "", "unit": "", "prep_note": "optional, to taste"}
        ],
        "instructions": [
            {"step": 1, "text": "Cook sea blite in boiling water until tender, then drain and chop."},
            {"step": 2, "text": "Combine all ingredients in a bowl and mix well."},
            {"step": 3, "text": "Refrigerate for two hours before serving."}
        ],
        "temperature": "",
        "pan_size": "",
        "notes": ["Sea blite is naturally salty, so taste before adding salt", "Also known as Suaeda"],
        "tags": ["sea blite", "salad", "sour cream", "foraged", "coastal"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "garnished-sea-blite-etw",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Garnished Sea Blite",
        "category": "vegetables",
        "attribution": "Eat the Weeds",
        "source_note": "From eattheweeds.com - Sea Blite article",
        "description": "Steamed sea blite topped with crispy bacon and Parmesan.",
        "servings_yield": "4 servings",
        "prep_time": "10 minutes",
        "cook_time": "15 minutes",
        "ingredients": [
            {"item": "sea blite", "quantity": "4", "unit": "cups", "prep_note": "chopped"},
            {"item": "bacon", "quantity": "6", "unit": "slices", "prep_note": "chopped and fried crisp"},
            {"item": "Parmesan cheese", "quantity": "2", "unit": "tbsp", "prep_note": "grated"},
            {"item": "vinegar", "quantity": "2", "unit": "tbsp", "prep_note": "wine or light vinegar preferred"},
            {"item": "bacon fat", "quantity": "", "unit": "", "prep_note": "optional"}
        ],
        "instructions": [
            {"step": 1, "text": "Boil or steam the sea blite until tender."},
            {"step": 2, "text": "Drain thoroughly."},
            {"step": 3, "text": "Combine with crispy bacon, cheese, vinegar, and bacon fat if desired."},
            {"step": 4, "text": "Serve hot."}
        ],
        "temperature": "",
        "pan_size": "",
        "notes": ["A warm side dish featuring the naturally salty sea blite"],
        "tags": ["sea blite", "bacon", "parmesan", "side dish", "foraged", "coastal"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "sea-blite-chicken-soup-etw",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Sea Blite Chicken Soup",
        "category": "soups",
        "attribution": "Eat the Weeds",
        "source_note": "From eattheweeds.com - Sea Blite article",
        "description": "A hearty chicken soup featuring foraged sea blite and Parmesan.",
        "servings_yield": "6-8 servings",
        "prep_time": "20 minutes",
        "cook_time": "1 hour 15 minutes",
        "ingredients": [
            {"item": "chicken breasts", "quantity": "2", "unit": ""},
            {"item": "water", "quantity": "2", "unit": "quarts"},
            {"item": "sea blite leaves", "quantity": "1", "unit": "cup", "prep_note": "washed, chopped"},
            {"item": "carrots", "quantity": "3", "unit": "", "prep_note": "diced"},
            {"item": "scallions", "quantity": "2", "unit": "", "prep_note": "chopped"},
            {"item": "celery stalks", "quantity": "2", "unit": "", "prep_note": "chopped"},
            {"item": "rosemary", "quantity": "1/4", "unit": "tsp"},
            {"item": "thyme", "quantity": "1/4", "unit": "tsp"},
            {"item": "parsley flakes", "quantity": "1/4", "unit": "tsp"},
            {"item": "garlic", "quantity": "1", "unit": "clove", "prep_note": "minced"},
            {"item": "Parmesan cheese", "quantity": "1/2", "unit": "cup"}
        ],
        "instructions": [
            {"step": 1, "text": "Boil chicken in water for 30 minutes."},
            {"step": 2, "text": "Remove chicken and cut into bite-sized pieces."},
            {"step": 3, "text": "Add all remaining ingredients except cheese to broth."},
            {"step": 4, "text": "Simmer 45 minutes."},
            {"step": 5, "text": "Return chicken to pot."},
            {"step": 6, "text": "Stir in Parmesan cheese before serving."}
        ],
        "temperature": "",
        "pan_size": "large pot",
        "notes": ["Sea blite adds natural saltiness - taste before adding salt"],
        "tags": ["sea blite", "chicken soup", "soup", "foraged", "coastal"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },

    # ===== LEMONGRASS =====
    {
        "id": "lemongrass-tea-etw",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Lemongrass Tea (Knotted Blade Method)",
        "category": "beverages",
        "attribution": "Eat the Weeds",
        "source_note": "From eattheweeds.com - Lemongrass article",
        "description": "A simple method for making fresh lemongrass tea using a knotted blade.",
        "servings_yield": "1 cup",
        "prep_time": "2 minutes",
        "cook_time": "2 minutes",
        "ingredients": [
            {"item": "lemongrass blade", "quantity": "1", "unit": "full blade"},
            {"item": "hot water", "quantity": "1", "unit": "cup"}
        ],
        "instructions": [
            {"step": 1, "text": "Take a complete lemongrass blade (be cautious, as the edges can cut you)."},
            {"step": 2, "text": "Starting from the bottom, begin tying the blade into knots."},
            {"step": 3, "text": "Continue knotting until you have created a large knot with sufficient length remaining for a handle to dip with."},
            {"step": 4, "text": "Place the knotted blade in hot water."},
            {"step": 5, "text": "Allow to steep for one to two minutes."},
            {"step": 6, "text": "Use the handle to stir if desired."}
        ],
        "temperature": "",
        "pan_size": "",
        "notes": ["The knotting releases more flavor than simply steeping a flat blade", "Handle lemongrass carefully - blade edges are sharp"],
        "tags": ["lemongrass", "tea", "beverage", "herbal tea", "simple"],
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

    for recipe in ETW_BATCH9_RECIPES:
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
    print(f"  Added: {added} new Eat the Weeds recipes (batch 9)")
    print(f"  Skipped: {skipped} duplicates")
    print(f"  Total recipes now: {len(recipes)}")


if __name__ == "__main__":
    main()
