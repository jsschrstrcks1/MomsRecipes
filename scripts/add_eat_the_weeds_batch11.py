#!/usr/bin/env python3
"""
Add Eat the Weeds recipes - Batch 11
Unusual/historical recipes
"""

import json
from pathlib import Path

RECIPES_FILE = Path(__file__).parent.parent / "data" / "recipes.json"

ETW_BATCH11_RECIPES = [
    # ===== UNUSUAL HISTORICAL RECIPES =====
    {
        "id": "lemongrass-dog-etw",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Lemon Grass Dog (Vietnamese Style)",
        "category": "main dishes",
        "attribution": "Eat the Weeds",
        "source_note": "From eattheweeds.com - Dog and Cat article (historical/cultural recipe)",
        "description": "A traditional Vietnamese preparation using lemongrass marinade. Dog meat is consumed in parts of Asia.",
        "servings_yield": "6-8 servings",
        "prep_time": "30 minutes plus overnight marinating",
        "cook_time": "varies",
        "ingredients": [
            {"item": "dog meat", "quantity": "2", "unit": "lb"},
            {"item": "lemongrass stalks", "quantity": "4", "unit": "", "prep_note": "3-foot stalks, minced (or 8 oz frozen minced)"},
            {"item": "Vietnamese fish sauce (nuoc mam)", "quantity": "3", "unit": "tbsp"},
            {"item": "lime juice", "quantity": "2", "unit": "tsp"},
            {"item": "lime zest", "quantity": "1/2", "unit": "tsp"},
            {"item": "jasmine rice", "quantity": "", "unit": "", "prep_note": "optional, for serving"},
            {"item": "rice vermicelli", "quantity": "", "unit": "", "prep_note": "optional, for serving"},
            {"item": "baguette", "quantity": "", "unit": "", "prep_note": "optional, for serving"}
        ],
        "instructions": [
            {"step": 1, "text": "Mince four 3-foot stalks of fresh lemongrass (or use 8 oz frozen minced lemongrass)."},
            {"step": 2, "text": "Mix minced lemongrass with fish sauce, lime juice, and lime zest."},
            {"step": 3, "text": "Chop meat into 1-inch pieces."},
            {"step": 4, "text": "Add lemongrass marinade to meat and stir well."},
            {"step": 5, "text": "Refrigerate mixture overnight."},
            {"step": 6, "text": "Sauté, steam, or grill the meat. Alternatively, skewer chunks and roast in rotisserie oven."},
            {"step": 7, "text": "Serve with jasmine rice, rice vermicelli, or baguette."}
        ],
        "temperature": "",
        "pan_size": "",
        "notes": ["Historical/cultural recipe from Vietnam", "Dog meat consumption is traditional in parts of Asia"],
        "tags": ["unusual", "historical", "vietnamese", "lemongrass", "cultural"],
        "confidence": {"overall": "high", "flags": ["cultural context required"]},
        "image_refs": []
    },
    {
        "id": "cat-braise-etw",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Cat Braisé (French Style)",
        "category": "main dishes",
        "attribution": "Eat the Weeds",
        "source_note": "From eattheweeds.com - Dog and Cat article (historical recipe)",
        "description": "A historical French-style braised preparation with artichokes and white wine. Cat was historically consumed during times of scarcity.",
        "servings_yield": "4-6 servings",
        "prep_time": "45 minutes",
        "cook_time": "1 hour",
        "ingredients": [
            {"item": "cat", "quantity": "1", "unit": "", "prep_note": "cut into serving pieces, dusted with flour, salt, and pepper"},
            {"item": "extra virgin olive oil", "quantity": "1/4", "unit": "cup"},
            {"item": "artichokes", "quantity": "6", "unit": ""},
            {"item": "slab bacon", "quantity": "2", "unit": "slices", "prep_note": "1/4 inch thick, diced"},
            {"item": "sweet onion", "quantity": "1", "unit": "small", "prep_note": "diced"},
            {"item": "garlic", "quantity": "4", "unit": "cloves", "prep_note": "minced"},
            {"item": "carrot", "quantity": "1", "unit": "", "prep_note": "diced"},
            {"item": "lemon", "quantity": "1", "unit": ""},
            {"item": "tomatoes", "quantity": "3", "unit": "small", "prep_note": "peeled, seeded, diced"},
            {"item": "dry white wine", "quantity": "1/2", "unit": "cup"},
            {"item": "homemade chicken broth", "quantity": "2-4", "unit": "cups"},
            {"item": "parsley stems", "quantity": "4", "unit": "", "prep_note": "flat, for bouquet garni"},
            {"item": "thyme branches", "quantity": "6", "unit": "", "prep_note": "leafy, for bouquet garni"},
            {"item": "bay leaf", "quantity": "1", "unit": "", "prep_note": "for bouquet garni"},
            {"item": "salt and pepper", "quantity": "", "unit": "", "prep_note": "to taste"},
            {"item": "flat-leaf parsley", "quantity": "1/4", "unit": "cup", "prep_note": "chopped, optional garnish"}
        ],
        "instructions": [
            {"step": 1, "text": "Prepare artichokes by snapping off outer leaves; trim stems and remove chokes; cut bottoms into quarters and soak in lemon-water."},
            {"step": 2, "text": "Heat 2 tbsp olive oil in large casserole; brown seasoned meat pieces on all sides; remove to plate."},
            {"step": 3, "text": "Discard remaining oil; add 1 tbsp fresh oil and bacon; sauté until cooked."},
            {"step": 4, "text": "Add remaining oil, onion, and carrot; sauté 5 minutes."},
            {"step": 5, "text": "Add artichoke quarters and garlic; stir 1 minute; add tomatoes and white wine."},
            {"step": 6, "text": "Reduce heat until syrupy, stirring constantly, approximately 5 minutes."},
            {"step": 7, "text": "Lay bouquet garni over vegetables; arrange meat pieces on top with accumulated juices."},
            {"step": 8, "text": "Pour broth halfway up meat pieces; cover and simmer 1 hour or bake at 350°F for 1 hour."},
            {"step": 9, "text": "Meat should be tender; turn pieces once during cooking."},
            {"step": 10, "text": "Remove meat pieces and vegetables to warm platter; strain pan juices, reduce by one-third, and pour over."},
            {"step": 11, "text": "Serve immediately; garnish with parsley if desired."}
        ],
        "temperature": "350°F (175°C)",
        "pan_size": "large casserole or Dutch oven",
        "notes": ["Historical recipe - cat was consumed during wartime and famine in Europe", "French braising technique"],
        "tags": ["unusual", "historical", "french", "braised", "cultural"],
        "confidence": {"overall": "high", "flags": ["historical context required"]},
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

    for recipe in ETW_BATCH11_RECIPES:
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
    print(f"  Added: {added} new Eat the Weeds recipes (batch 11)")
    print(f"  Skipped: {skipped} duplicates")
    print(f"  Total recipes now: {len(recipes)}")


if __name__ == "__main__":
    main()
