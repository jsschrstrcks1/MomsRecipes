#!/usr/bin/env python3
"""
Add Eat the Weeds recipes - Batch 7
Recipes from: chestnut, henbit, amaranth, hawthorn
"""

import json
from pathlib import Path

RECIPES_FILE = Path(__file__).parent.parent / "data" / "recipes.json"

ETW_BATCH7_RECIPES = [
    # ===== CHESTNUT =====
    {
        "id": "hungarian-chestnut-soup-etw",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Hungarian Cream of Chestnut Soup (Gesztenye Leves)",
        "category": "soups",
        "attribution": "Eat the Weeds",
        "source_note": "From eattheweeds.com - Chestnuts article",
        "description": "A rich Hungarian soup with chestnuts, root vegetables, apples, and cream.",
        "servings_yield": "6-8 servings",
        "prep_time": "45 minutes",
        "cook_time": "1 hour",
        "ingredients": [
            {"item": "cooked and peeled chestnuts", "quantity": "12-14", "unit": "oz", "prep_note": "finely chopped"},
            {"item": "butter", "quantity": "4", "unit": "tbsp"},
            {"item": "parsnips", "quantity": "2", "unit": "", "prep_note": "peeled, thinly sliced"},
            {"item": "carrots", "quantity": "2", "unit": "", "prep_note": "peeled, thinly sliced diagonally"},
            {"item": "apples", "quantity": "2", "unit": "", "prep_note": "peeled, cored, quartered, thinly sliced"},
            {"item": "leeks", "quantity": "2", "unit": "", "prep_note": "white part only, thinly sliced"},
            {"item": "Hungarian paprika", "quantity": "2", "unit": "tsp", "prep_note": "sweet or hot"},
            {"item": "leftover ham", "quantity": "1/2", "unit": "lb", "prep_note": "julienne-sliced"},
            {"item": "chicken stock", "quantity": "5", "unit": "cups"},
            {"item": "whipping cream", "quantity": "1.5", "unit": "cups"},
            {"item": "egg yolks", "quantity": "2", "unit": ""}
        ],
        "instructions": [
            {"step": 1, "text": "If using fresh chestnuts: Score an X on the bottom of one pound fresh chestnuts. Boil in water, then simmer 30 minutes. Cool slightly, peel, and chop finely. Alternatively, use pre-cooked chestnuts."},
            {"step": 2, "text": "Melt butter in a large saucepan and sauté parsnips, carrots, apples, and leeks for about 10 minutes until nearly tender."},
            {"step": 3, "text": "Mix in ham, chestnuts, and paprika. Cook one minute."},
            {"step": 4, "text": "Stir in stock and bring to boil. Reduce heat and simmer uncovered for 20 minutes."},
            {"step": 5, "text": "Whisk cream and egg yolks together. Temper with a few ladles of hot broth while whisking constantly."},
            {"step": 6, "text": "Pour tempered cream mixture into soup while whisking for one minute until thickened. Season to taste."},
            {"step": 7, "text": "Serve with sour cream if desired."}
        ],
        "temperature": "",
        "pan_size": "large saucepan",
        "notes": ["Temper the cream mixture slowly to prevent curdling"],
        "tags": ["soup", "chestnut", "hungarian", "cream soup", "fall", "winter"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },

    # ===== HENBIT =====
    {
        "id": "spicy-henbit-etw",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Spicy Henbit",
        "category": "vegetables",
        "attribution": "Eat the Weeds",
        "source_note": "From eattheweeds.com - Henbit article",
        "description": "Foraged henbit shoots in a curry-spiced cream sauce.",
        "servings_yield": "4 servings",
        "prep_time": "10 minutes",
        "cook_time": "30 minutes",
        "ingredients": [
            {"item": "henbit shoots", "quantity": "4", "unit": "cups"},
            {"item": "water", "quantity": "", "unit": "", "prep_note": "to cover"},
            {"item": "butter", "quantity": "3", "unit": "tbsp"},
            {"item": "curry powder", "quantity": "1", "unit": "tsp"},
            {"item": "whole cloves", "quantity": "2", "unit": ""},
            {"item": "ground cinnamon", "quantity": "1/4", "unit": "tsp"},
            {"item": "flour", "quantity": "2", "unit": "tbsp"},
            {"item": "boiling water from henbit", "quantity": "1/2", "unit": "cup"},
            {"item": "sour cream", "quantity": "3/4", "unit": "cup"}
        ],
        "instructions": [
            {"step": 1, "text": "Chop four cups of henbit shoots and cover with water, then boil for 10 minutes."},
            {"step": 2, "text": "In a separate pan, melt butter and add curry powder, cloves, and cinnamon."},
            {"step": 3, "text": "Stir and cook for one minute."},
            {"step": 4, "text": "Add flour and cook another minute."},
            {"step": 5, "text": "Add half a cup of boiling water from the henbit, stirring until smooth."},
            {"step": 6, "text": "Drain the boiled henbit and add to the mixture along with sour cream."},
            {"step": 7, "text": "Cook on low heat for 15 minutes."}
        ],
        "temperature": "",
        "pan_size": "",
        "notes": ["Henbit is a common spring weed in the mint family", "Reserve cooking water before draining"],
        "tags": ["henbit", "foraged", "wild greens", "curry", "side dish"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },

    # ===== AMARANTH =====
    {
        "id": "amaranth-tabouli-etw",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Amaranth Tabouli",
        "category": "salads",
        "attribution": "Eat the Weeds / Salt Spring Seeds",
        "source_note": "From eattheweeds.com - Amaranth article",
        "description": "A Middle Eastern-style tabouli made with amaranth seeds instead of bulgur.",
        "servings_yield": "4-6 servings",
        "prep_time": "20 minutes",
        "cook_time": "15 minutes",
        "total_time": "1 hour 35 minutes (including chilling)",
        "ingredients": [
            {"item": "amaranth seeds", "quantity": "1", "unit": "cup", "prep_note": "pre-soaked"},
            {"item": "parsley", "quantity": "1", "unit": "cup", "prep_note": "chopped"},
            {"item": "scallions", "quantity": "1/2", "unit": "cup", "prep_note": "chopped"},
            {"item": "fresh mint", "quantity": "2", "unit": "tbsp"},
            {"item": "lemon juice", "quantity": "1/2", "unit": "cup"},
            {"item": "olive oil", "quantity": "1/4", "unit": "cup"},
            {"item": "garlic cloves", "quantity": "2", "unit": "", "prep_note": "pressed"},
            {"item": "olives", "quantity": "1/4", "unit": "cup", "prep_note": "sliced"},
            {"item": "lettuce leaves", "quantity": "", "unit": "", "prep_note": "whole, for serving"}
        ],
        "instructions": [
            {"step": 1, "text": "Simmer amaranth seeds in an equal volume of water for 12-15 minutes."},
            {"step": 2, "text": "Allow mixture to cool completely."},
            {"step": 3, "text": "In a mixing bowl, combine all ingredients except lettuce and olives."},
            {"step": 4, "text": "Toss ingredients together lightly."},
            {"step": 5, "text": "Chill for one hour or longer to allow flavors to blend."},
            {"step": 6, "text": "Wash and dry lettuce leaves and use them to line a salad bowl."},
            {"step": 7, "text": "Transfer the amaranth mixture onto the lettuce."},
            {"step": 8, "text": "Garnish with olives before serving."}
        ],
        "temperature": "",
        "pan_size": "",
        "notes": ["Amaranth is a nutritious ancient grain", "Can substitute quinoa if amaranth unavailable"],
        "tags": ["amaranth", "tabouli", "salad", "middle eastern", "ancient grains", "vegan"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },

    # ===== HAWTHORN RECIPES =====
    {
        "id": "hawthorn-schnapps-etw",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Hawthorn Schnapps",
        "category": "beverages",
        "attribution": "Eat the Weeds",
        "source_note": "From eattheweeds.com - The Crataegus Clan",
        "description": "A homemade schnapps infused with hawthorn berries.",
        "servings_yield": "1 bottle",
        "prep_time": "15 minutes",
        "cook_time": "",
        "total_time": "6-8 weeks (steeping time)",
        "ingredients": [
            {"item": "hawthorn berries", "quantity": "", "unit": "", "prep_note": "stalkless, enough to fill jar 2/3 full"},
            {"item": "vodka", "quantity": "", "unit": "", "prep_note": "clear, unflavored, to cover berries"}
        ],
        "instructions": [
            {"step": 1, "text": "Rinse berries and allow to dry completely."},
            {"step": 2, "text": "Fill a clean glass jar 2/3 full with berries."},
            {"step": 3, "text": "Cover berries entirely with vodka."},
            {"step": 4, "text": "Seal jar tightly."},
            {"step": 5, "text": "Steep for 5-6 weeks in a dark place at 64-68°F, shaking occasionally."},
            {"step": 6, "text": "Strain and filter into clean bottles."},
            {"step": 7, "text": "Age for a couple months in darkness before serving."}
        ],
        "temperature": "64-68°F for steeping",
        "pan_size": "glass jar",
        "notes": ["Use Crataegus monogyna or C. laevigata berries", "Patience is key - aging improves flavor"],
        "tags": ["hawthorn", "schnapps", "liqueur", "infusion", "foraged", "beverage"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "haw-sauce-etw",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Haw Sauce",
        "category": "preserves",
        "attribution": "Eat the Weeds",
        "source_note": "From eattheweeds.com - The Crataegus Clan",
        "description": "A tangy condiment sauce made from hawthorn berries.",
        "servings_yield": "about 2 cups",
        "prep_time": "15 minutes",
        "cook_time": "40 minutes",
        "ingredients": [
            {"item": "hawthorn berries", "quantity": "1.5", "unit": "lb", "prep_note": "stalkless"},
            {"item": "vinegar", "quantity": "3/4", "unit": "pint", "prep_note": "any type"},
            {"item": "sugar", "quantity": "4", "unit": "oz"},
            {"item": "salt", "quantity": "1", "unit": "oz", "prep_note": "optional, to taste"},
            {"item": "black pepper", "quantity": "1", "unit": "tsp", "prep_note": "freshly ground"}
        ],
        "instructions": [
            {"step": 1, "text": "Wash berries and place in pan with vinegar."},
            {"step": 2, "text": "Cook gently for 30 minutes."},
            {"step": 3, "text": "Press pulp through sieve."},
            {"step": 4, "text": "Return to pan with sugar and seasonings."},
            {"step": 5, "text": "Boil for 10 minutes."},
            {"step": 6, "text": "Bottle and seal."}
        ],
        "temperature": "",
        "pan_size": "",
        "notes": ["Similar to ketchup in use", "Good with meats"],
        "tags": ["hawthorn", "sauce", "condiment", "foraged", "preserves"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "hawthorn-berry-soup-etw",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Hawthorn Berry Soup",
        "category": "soups",
        "attribution": "Eat the Weeds",
        "source_note": "From eattheweeds.com - The Crataegus Clan",
        "description": "A sweet dessert soup made from hawthorn berries with cinnamon.",
        "servings_yield": "4 servings",
        "prep_time": "10 minutes",
        "cook_time": "30 minutes",
        "ingredients": [
            {"item": "hawthorn berries", "quantity": "1", "unit": "lb", "prep_note": "stalkless"},
            {"item": "water", "quantity": "1/2", "unit": "cup"},
            {"item": "sugar", "quantity": "1/2", "unit": "lb", "prep_note": "adjust to taste"},
            {"item": "cinnamon sticks", "quantity": "2", "unit": ""},
            {"item": "chili flakes or powder", "quantity": "1", "unit": "pinch", "prep_note": "optional"}
        ],
        "instructions": [
            {"step": 1, "text": "Add berries and water to pot."},
            {"step": 2, "text": "Bring to gentle simmer and cover tightly."},
            {"step": 3, "text": "Cook for 30 minutes."},
            {"step": 4, "text": "Cool and pass through sieve, discarding seeds."},
            {"step": 5, "text": "Transfer to pan with sugar, cinnamon, and chili if using."},
            {"step": 6, "text": "Cook until sauce thickens and serve."}
        ],
        "temperature": "",
        "pan_size": "",
        "notes": ["Can be served warm or chilled", "A sweet dessert soup"],
        "tags": ["hawthorn", "soup", "dessert", "sweet", "foraged"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "euell-gibbons-hawthorn-jelly-etw",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Euell Gibbons' Hawthorn Jelly",
        "category": "preserves",
        "attribution": "Eat the Weeds / Euell Gibbons",
        "source_note": "From eattheweeds.com - The Crataegus Clan",
        "description": "A classic hawthorn jelly recipe from foraging legend Euell Gibbons.",
        "servings_yield": "6-8 half-pint jars",
        "prep_time": "30 minutes",
        "cook_time": "30 minutes",
        "ingredients": [
            {"item": "hawthorn fruit", "quantity": "3", "unit": "lb"},
            {"item": "water", "quantity": "4", "unit": "cups"},
            {"item": "sugar", "quantity": "7", "unit": "cups"},
            {"item": "powdered pectin", "quantity": "1", "unit": "package", "prep_note": "if needed for overripe fruit"},
            {"item": "lemon juice", "quantity": "", "unit": "", "prep_note": "juice of 2 lemons, optional"}
        ],
        "instructions": [
            {"step": 1, "text": "Crush three pounds of fruit."},
            {"step": 2, "text": "Add water, bring to boil, cover and simmer 10 minutes."},
            {"step": 3, "text": "Strain juice through jelly bag, discard pulp and seeds."},
            {"step": 4, "text": "If fruit is overripe, add pectin; add lemon juice if desired."},
            {"step": 5, "text": "Place 4 cups juice in large saucepan and bring to boil."},
            {"step": 6, "text": "Add 7 cups sugar and return to boil."},
            {"step": 7, "text": "Test for gel consistency and jar using standard canning methods."}
        ],
        "temperature": "",
        "pan_size": "large saucepan",
        "notes": ["Euell Gibbons was a famous American forager and author", "Pectin may not be needed if fruit is not overripe"],
        "tags": ["hawthorn", "jelly", "preserves", "canning", "foraged", "euell gibbons"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "hawthorn-berry-catsup-etw",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Hawthorn Berry Catsup",
        "category": "preserves",
        "attribution": "Eat the Weeds",
        "source_note": "From eattheweeds.com - The Crataegus Clan",
        "description": "A unique ketchup-style condiment made from hawthorn berries.",
        "servings_yield": "about 2 cups",
        "prep_time": "20 minutes",
        "cook_time": "40 minutes",
        "ingredients": [
            {"item": "hawthorn berries", "quantity": "2", "unit": "cups"},
            {"item": "apple cider vinegar", "quantity": "1/4", "unit": "cup"},
            {"item": "water", "quantity": "1/4", "unit": "cup"},
            {"item": "sugar or honey", "quantity": "", "unit": "", "prep_note": "to taste"},
            {"item": "black cherry juice", "quantity": "1/3", "unit": "cup", "prep_note": "optional but recommended"},
            {"item": "sea salt", "quantity": "1/2", "unit": "tsp"},
            {"item": "black pepper or cayenne", "quantity": "", "unit": "", "prep_note": "freshly ground, to taste"}
        ],
        "instructions": [
            {"step": 1, "text": "Remove berries from stalks and rinse."},
            {"step": 2, "text": "Place in saucepan with vinegar and water."},
            {"step": 3, "text": "Bring to boil and simmer 25 minutes until skins split."},
            {"step": 4, "text": "Cool and press through sieve to remove pits."},
            {"step": 5, "text": "Return to pan with sweeteners and heat slowly, stirring frequently."},
            {"step": 6, "text": "Add spices and bring to low boil."},
            {"step": 7, "text": "Simmer 5-10 minutes until syrupy."},
            {"step": 8, "text": "Add black cherry juice gradually for desired consistency."},
            {"step": 9, "text": "Pour into sterilized bottles and refrigerate. Use within 3 months."}
        ],
        "temperature": "",
        "pan_size": "",
        "notes": ["Black cherry juice adds depth and color", "Store in refrigerator"],
        "tags": ["hawthorn", "catsup", "ketchup", "condiment", "foraged", "preserves"],
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

    for recipe in ETW_BATCH7_RECIPES:
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
    print(f"  Added: {added} new Eat the Weeds recipes (batch 7)")
    print(f"  Skipped: {skipped} duplicates")
    print(f"  Total recipes now: {len(recipes)}")


if __name__ == "__main__":
    main()
