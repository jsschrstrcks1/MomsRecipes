#!/usr/bin/env python3
"""
Add Eat the Weeds recipes - Batch 4.

This batch includes: Japanese knotweed, groundnut, nasturtium,
acorn, and maypop recipes from Green Deane's eattheweeds.com.
"""

import json
from pathlib import Path

RECIPES_FILE = Path(__file__).parent.parent / "data" / "recipes.json"

ETW_BATCH4_RECIPES = [
    # ===== JAPANESE KNOTWEED RECIPES =====
    {
        "id": "japanese-knotweed-puree-etw",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Japanese Knotweed Purée",
        "category": "desserts",
        "attribution": "Eat the Weeds - Green Deane",
        "source_note": "Wild foraging recipe from eattheweeds.com",
        "description": "Sweet purée from Japanese knotweed, similar to rhubarb.",
        "ingredients": [
            {"item": "knotweed stalks", "quantity": "5", "unit": "cups", "prep_note": "thick stems, sliced 1-inch"},
            {"item": "sugar", "quantity": "3/4", "unit": "cup"},
            {"item": "water", "quantity": "1/2", "unit": "cup", "prep_note": "approximately"},
            {"item": "lemon juice", "quantity": "", "unit": "", "prep_note": "to taste"},
            {"item": "additional sugar", "quantity": "", "unit": "", "prep_note": "optional, to taste"}
        ],
        "instructions": [
            {"step": 1, "text": "Gather stalks and remove all leaves and tips."},
            {"step": 2, "text": "Slice stems into 1-inch pieces and place in a pot."},
            {"step": 3, "text": "Add sugar and let stand 20 minutes to extract juices."},
            {"step": 4, "text": "Add water to prevent scorching."},
            {"step": 5, "text": "Cook until pieces soften, adding more water if needed."},
            {"step": 6, "text": "Mix thoroughly once cooked."},
            {"step": 7, "text": "Season with lemon juice and additional sugar to taste."},
            {"step": 8, "text": "Serve chilled as dessert, over vanilla ice cream, or in a pie shell."}
        ],
        "notes": ["Can be refrigerated or frozen for later use", "Similar to rhubarb sauce"],
        "tags": ["knotweed", "dessert", "sauce", "foraging", "eat the weeds"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "japanese-knotweed-bread-etw",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Japanese Knotweed Bread",
        "category": "breads",
        "attribution": "Eat the Weeds - Green Deane",
        "source_note": "Wild foraging recipe from eattheweeds.com",
        "description": "Quick bread made with sweetened knotweed purée and hazelnuts.",
        "servings_yield": "1 loaf or 12 muffins",
        "ingredients": [
            {"item": "unbleached flour", "quantity": "2", "unit": "cups"},
            {"item": "sugar", "quantity": "1/2", "unit": "cup"},
            {"item": "baking powder", "quantity": "1.5", "unit": "tsp"},
            {"item": "salt", "quantity": "1", "unit": "tsp"},
            {"item": "egg", "quantity": "1", "unit": ""},
            {"item": "salad oil", "quantity": "2", "unit": "tbsp"},
            {"item": "orange juice", "quantity": "3/4", "unit": "cup"},
            {"item": "chopped hazelnuts", "quantity": "3/4", "unit": "cup"},
            {"item": "sweetened Japanese knotweed purée", "quantity": "1", "unit": "cup"}
        ],
        "instructions": [
            {"step": 1, "text": "Preheat oven to 350°F."},
            {"step": 2, "text": "Sift dry ingredients together."},
            {"step": 3, "text": "Beat egg white with oil and orange juice, then combine with hazelnuts and purée."},
            {"step": 4, "text": "Add to dry ingredients, mixing gently until just moistened."},
            {"step": 5, "text": "Transfer to buttered 9½-by-5-by-3-inch loaf pan."},
            {"step": 6, "text": "Bake approximately 1 hour until a tester inserted in the center comes out dry."},
            {"step": 7, "text": "Cool on a rack."}
        ],
        "temperature": "350°F (175°C)",
        "notes": ["For muffins, use muffin tins and bake about 25 minutes"],
        "tags": ["knotweed", "bread", "quick bread", "foraging", "eat the weeds"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    # ===== GROUNDNUT RECIPE =====
    {
        "id": "groundnut-olive-stew-etw",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Groundnut and Olive Stew",
        "category": "main-dishes",
        "attribution": "Eat the Weeds - Green Deane",
        "source_note": "Wild foraging recipe from eattheweeds.com",
        "description": "Hearty stew with American groundnuts, olives, and tomatoes.",
        "ingredients": [
            {"item": "boiled groundnuts", "quantity": "8-16", "unit": "oz"},
            {"item": "olives", "quantity": "16", "unit": "oz", "prep_note": "California or Kalamata; reduce salt if using Kalamata"},
            {"item": "chopped tomatoes", "quantity": "16", "unit": "oz", "prep_note": "canned"},
            {"item": "large onion", "quantity": "1", "unit": "", "prep_note": "chopped"},
            {"item": "garlic cloves", "quantity": "", "unit": "", "prep_note": "several whole, to taste"},
            {"item": "broth or water", "quantity": "", "unit": "", "prep_note": "to cover"},
            {"item": "olive oil", "quantity": "1", "unit": "tbsp", "prep_note": "approximately"},
            {"item": "pepper", "quantity": "", "unit": "", "prep_note": "to taste"},
            {"item": "salt", "quantity": "", "unit": "", "prep_note": "to taste"},
            {"item": "lamb shank or stew meat", "quantity": "12", "unit": "oz", "prep_note": "optional"}
        ],
        "instructions": [
            {"step": 1, "text": "Cook large-cut groundnuts in abundant water until done (approximately 40 minutes). Drain thoroughly."},
            {"step": 2, "text": "Combine all ingredients in a pot."},
            {"step": 3, "text": "For a meatless version, simmer on medium heat until flavors meld, typically about an hour."},
            {"step": 4, "text": "If including meat, use low heat until the meat becomes tender, requiring two to three hours."},
            {"step": 5, "text": "Serve with hearty bread and red wine."}
        ],
        "notes": ["Avoid aluminum cookware - latex smears and sticks badly", "Groundnuts must be cooked; raw versions can taste bitter"],
        "tags": ["groundnut", "stew", "native american", "foraging", "eat the weeds"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    # ===== NASTURTIUM RECIPES =====
    {
        "id": "nasturtium-bouquet-salad-etw",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Nasturtium Bouquet Salad",
        "category": "salads",
        "attribution": "Eat the Weeds - Green Deane",
        "source_note": "Wild foraging recipe from eattheweeds.com",
        "description": "Elegant salad with radicchio, spinach, and nasturtium blossoms.",
        "servings_yield": "8 servings",
        "ingredients": [
            {"item": "white wine or champagne vinegar", "quantity": "1/4", "unit": "cup"},
            {"item": "Dijon mustard", "quantity": "1", "unit": "tbsp"},
            {"item": "vegetable oil", "quantity": "1", "unit": "cup"},
            {"item": "salt and pepper", "quantity": "", "unit": "", "prep_note": "to taste"},
            {"item": "light olive oil", "quantity": "1/4", "unit": "cup"},
            {"item": "freshly squeezed lime juice", "quantity": "1", "unit": "tbsp"},
            {"item": "lime zest", "quantity": "", "unit": "", "prep_note": "finely grated"},
            {"item": "radicchio", "quantity": "3", "unit": "heads", "prep_note": "washed and dried"},
            {"item": "chives", "quantity": "1", "unit": "small bunch"},
            {"item": "tender spinach", "quantity": "1", "unit": "lb", "prep_note": "trimmed, washed, and dried"},
            {"item": "nasturtium blossoms", "quantity": "", "unit": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Whisk vinegar and mustard together in a bowl."},
            {"step": 2, "text": "Gradually add oils while whisking. Add lime juice and zest."},
            {"step": 3, "text": "Season with salt and pepper."},
            {"step": 4, "text": "Just before serving, toss greens, chives, and flowers with sufficient dressing to coat."}
        ],
        "tags": ["nasturtium", "salad", "flower", "foraging", "eat the weeds"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "nasturtium-bundles-etw",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Nasturtium Bundles",
        "category": "appetizers",
        "attribution": "Eat the Weeds - Green Deane",
        "source_note": "Wild foraging recipe from eattheweeds.com",
        "description": "Cream cheese and pineapple wrapped in nasturtium leaves.",
        "ingredients": [
            {"item": "medium-sized nasturtium leaves", "quantity": "", "unit": "", "prep_note": "rinsed and dried"},
            {"item": "cream cheese", "quantity": "8", "unit": "oz", "prep_note": "softened"},
            {"item": "crushed pineapple", "quantity": "1", "unit": "small can", "prep_note": "drained"},
            {"item": "fresh herbs", "quantity": "3", "unit": "tbsp", "prep_note": "thyme, lemon verbena, lemon-scented geranium, basil, chives, or rose petals"}
        ],
        "instructions": [
            {"step": 1, "text": "Mix cream cheese, pineapple, and chosen herbs."},
            {"step": 2, "text": "Spread generously on each leaf."},
            {"step": 3, "text": "Roll up and arrange on a serving platter."},
            {"step": 4, "text": "Garnish with nasturtium flowers."}
        ],
        "tags": ["nasturtium", "appetizer", "flower", "cream cheese", "foraging", "eat the weeds"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "steamed-beets-nasturtium-etw",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Steamed Beets with Nasturtium",
        "category": "sides",
        "attribution": "Eat the Weeds - Green Deane",
        "source_note": "Wild foraging recipe from eattheweeds.com",
        "description": "Tender beets with peppery nasturtium leaves and balsamic dressing.",
        "servings_yield": "3-4 servings",
        "ingredients": [
            {"item": "whole beets", "quantity": "4", "unit": "", "prep_note": "steamed"},
            {"item": "nasturtium leaves", "quantity": "6", "unit": "", "prep_note": "shredded"},
            {"item": "nasturtium flowers", "quantity": "4", "unit": ""},
            {"item": "olive oil", "quantity": "1/3", "unit": "cup"},
            {"item": "balsamic vinegar", "quantity": "2", "unit": "tbsp"},
            {"item": "salt", "quantity": "1/2", "unit": "tsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Steam peeled beets until fork-tender (about 30 minutes)."},
            {"step": 2, "text": "Cool and cut into bite-sized wedges."},
            {"step": 3, "text": "Whisk olive oil, balsamic vinegar, and salt together."},
            {"step": 4, "text": "Sprinkle shredded nasturtium leaves over beets."},
            {"step": 5, "text": "Drizzle with dressing and decorate with flowers."}
        ],
        "tags": ["nasturtium", "beets", "salad", "flower", "foraging", "eat the weeds"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    # ===== ACORN RECIPES =====
    {
        "id": "acorn-bread-etw",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Acorn Bread",
        "category": "breads",
        "attribution": "Eat the Weeds - Green Deane",
        "source_note": "Wild foraging recipe from eattheweeds.com",
        "description": "Nutritious bread made with acorn flour and maple syrup.",
        "ingredients": [
            {"item": "acorn flour", "quantity": "2", "unit": "cups"},
            {"item": "cattail or white flour", "quantity": "2", "unit": "cups"},
            {"item": "baking powder", "quantity": "3", "unit": "tsp"},
            {"item": "maple syrup or sugar", "quantity": "1/3", "unit": "cup"},
            {"item": "egg", "quantity": "1", "unit": ""},
            {"item": "milk", "quantity": "1/2", "unit": "cup"},
            {"item": "olive oil", "quantity": "3", "unit": "tbsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Mix all ingredients together."},
            {"step": 2, "text": "Pour into a greased pan."},
            {"step": 3, "text": "Bake at 400°F for 30 minutes or until done."}
        ],
        "temperature": "400°F (200°C)",
        "notes": ["Acorn flour contains no gluten; mix 50/50 with wheat flour for better binding"],
        "tags": ["acorn", "bread", "native american", "foraging", "eat the weeds"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "acorn-muffins-etw",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Acorn Muffins",
        "category": "breads",
        "attribution": "Eat the Weeds - Green Deane (from BSteele, California)",
        "source_note": "Wild foraging recipe from eattheweeds.com",
        "description": "Hearty muffins with acorn pulp, cornmeal, and walnuts.",
        "servings_yield": "12 muffins",
        "ingredients": [
            {"item": "stone-ground cornmeal", "quantity": "1", "unit": "cup"},
            {"item": "drained leached acorn pulp", "quantity": "1", "unit": "cup"},
            {"item": "wheat flour", "quantity": "3/4", "unit": "cup"},
            {"item": "amaranth flour", "quantity": "1/4", "unit": "cup"},
            {"item": "melted butter", "quantity": "3", "unit": "tbsp"},
            {"item": "baking powder", "quantity": "3", "unit": "tsp"},
            {"item": "milk", "quantity": "3/4", "unit": "cup"},
            {"item": "eggs", "quantity": "2", "unit": ""},
            {"item": "diced walnuts", "quantity": "1/2", "unit": "cup"}
        ],
        "instructions": [
            {"step": 1, "text": "Mix all ingredients together."},
            {"step": 2, "text": "Pour into well-greased muffin pans."},
            {"step": 3, "text": "Bake at 400°F for 15 minutes."}
        ],
        "temperature": "400°F (200°C)",
        "notes": ["Store acorn flour carefully to prevent rancidity due to high oil content"],
        "tags": ["acorn", "muffins", "native american", "foraging", "eat the weeds"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    # ===== MAYPOP RECIPE =====
    {
        "id": "maypop-jelly-etw",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Maypop Jelly",
        "category": "preserves",
        "attribution": "Eat the Weeds - Green Deane",
        "source_note": "Wild foraging recipe from eattheweeds.com",
        "description": "Tropical-flavored jelly from native passion fruit (maypops).",
        "servings_yield": "2.5 pints",
        "ingredients": [
            {"item": "ripe maypops", "quantity": "2", "unit": "cups", "prep_note": "sliced"},
            {"item": "water", "quantity": "1", "unit": "cup"},
            {"item": "sugar", "quantity": "2.5", "unit": "cups"},
            {"item": "pectin", "quantity": "1.75", "unit": "oz"}
        ],
        "instructions": [
            {"step": 1, "text": "Combine maypops and water, boil gently for five minutes."},
            {"step": 2, "text": "Strain, discarding the pulp."},
            {"step": 3, "text": "Mix liquid with sugar and bring to full rolling boil."},
            {"step": 4, "text": "Add pectin and return to rolling boil."},
            {"step": 5, "text": "Remove from heat, pour into hot sterilized jars, and seal."}
        ],
        "notes": ["Green maypops are better cooked than raw", "Yellow ripe ones work well raw"],
        "tags": ["maypop", "passion fruit", "jelly", "preserves", "foraging", "eat the weeds"],
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

    for recipe in ETW_BATCH4_RECIPES:
        if recipe['id'] in existing_ids:
            print(f"  Skipping duplicate: {recipe['id']}")
            skipped += 1
        else:
            recipes.append(recipe)
            existing_ids.add(recipe['id'])
            added += 1
            print(f"  Added: {recipe['title']}")

    data['meta']['total_recipes'] = len(recipes)

    print(f"\nWriting {len(recipes)} recipes to {RECIPES_FILE}")
    with open(RECIPES_FILE, 'w') as f:
        json.dump(data, f, indent=2)

    print(f"\nSummary:")
    print(f"  Added: {added} new Eat the Weeds recipes (batch 4)")
    print(f"  Skipped: {skipped} duplicates")
    print(f"  Total recipes now: {len(recipes)}")


if __name__ == "__main__":
    main()
