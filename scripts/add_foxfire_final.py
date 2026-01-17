#!/usr/bin/env python3
"""
Add final batch of missed Foxfire recipes to recipes.json.

Recipes discovered through deeper search of Foxfire Books 2 and 3:
- Ramp soup (with variations)
- Ramp salad
- Mustard-ramp soup
- Mustard flowers
- Garlic vinegar
- Blackberry nectar
- Blackberry shrub
- Raspberry pickles
- Raspberry vinegar
- Sumac and elderberry jelly
- Elderberry wine
- Elderberry jam
- Elderberry-apple-orange jam
- Steamed elderberry pudding
"""

import json
from pathlib import Path

RECIPES_FILE = Path(__file__).parent.parent / "data" / "recipes.json"

FINAL_RECIPES = [
    # From Foxfire Book 2 - Wild Plant Foods
    {
        "id": "appalachian-ramp-soup",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Appalachian Ramp Soup",
        "category": "soups",
        "attribution": "Foxfire Book 2",
        "source_note": "Traditional Appalachian wild plant recipes",
        "description": "Traditional soup made with wild ramps, with three variations using beef or venison.",
        "servings_yield": "4-6 servings",
        "ingredients": [
            {"item": "beef or venison", "quantity": "1", "unit": "lb", "prep_note": "cut in small pieces"},
            {"item": "ramps", "quantity": "36", "unit": "", "prep_note": "cleaned"},
            {"item": "carrots", "quantity": "2", "unit": "", "prep_note": "cut in small pieces"},
            {"item": "potatoes", "quantity": "2", "unit": "", "prep_note": "cut in small pieces"},
            {"item": "salt", "quantity": "", "unit": "", "prep_note": "to taste"},
            {"item": "water", "quantity": "", "unit": "", "prep_note": "to cover"}
        ],
        "instructions": [
            {"step": 1, "text": "Cut one pound of beef in small pieces, add salt and water, and boil."},
            {"step": 2, "text": "Skim the foam from the top."},
            {"step": 3, "text": "Add ramps, carrots, and potatoes cut in small pieces."},
            {"step": 4, "text": "Take out meat and eat separately."},
            {"step": 5, "text": "Put vegetables through sieve and serve hot."}
        ],
        "notes": [
            "Variation 1: Cook beef or venison and add celery leaves, bay leaves, three cloves, and thirty-six ramps. Take meat out and serve separately. Lift out ramps and serve broth with rice.",
            "Variation 2: Add fried ramps to beef stock. Season with black pepper and serve."
        ],
        "tags": ["soup", "ramps", "wild plants", "appalachian", "foxfire"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "appalachian-ramp-salad",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Appalachian Ramp Salad",
        "category": "salads",
        "attribution": "Foxfire Book 2",
        "source_note": "Traditional Appalachian wild plant recipes",
        "description": "Fresh wild ramp salad with multiple serving variations.",
        "servings_yield": "2-4 servings",
        "ingredients": [
            {"item": "young ramp leaves", "quantity": "2", "unit": "cups", "prep_note": "chopped into tiny bits"},
            {"item": "vinegar", "quantity": "", "unit": "", "prep_note": "optional"},
            {"item": "mayonnaise", "quantity": "", "unit": "", "prep_note": "optional"}
        ],
        "instructions": [
            {"step": 1, "text": "Chop up young ramp leaves into tiny bits."},
            {"step": 2, "text": "Eat raw, or cook and add vinegar when ready to eat."},
            {"step": 3, "text": "Alternatively, add a little to any salad."},
            {"step": 4, "text": "Or chop fine, parboil, drain and cool, and mix with mayonnaise and serve with trout."}
        ],
        "notes": [
            "You can also add one-half cup chopped fine to mashed potatoes just before serving."
        ],
        "tags": ["salad", "ramps", "wild plants", "appalachian", "foxfire"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "appalachian-mustard-ramp-soup",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Mustard-Ramp Soup",
        "category": "soups",
        "attribution": "Foxfire Book 2",
        "source_note": "Traditional Appalachian wild plant recipes",
        "description": "Creamy soup made with wild mustard greens and ramps.",
        "servings_yield": "4 servings",
        "ingredients": [
            {"item": "mustard leaves", "quantity": "2", "unit": "cups", "prep_note": "cleaned and washed"},
            {"item": "milk", "quantity": "1", "unit": "quart"},
            {"item": "bacon fat", "quantity": "2", "unit": "tbsp"},
            {"item": "ramps", "quantity": "1", "unit": "cup", "prep_note": "chopped"},
            {"item": "salt", "quantity": "", "unit": "", "prep_note": "to taste"},
            {"item": "black pepper", "quantity": "", "unit": "", "prep_note": "to taste"},
            {"item": "flour", "quantity": "2", "unit": "tbsp"},
            {"item": "dry mustard", "quantity": "1", "unit": "tsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Clean and wash mustard leaves."},
            {"step": 2, "text": "Heat one quart milk almost to boiling."},
            {"step": 3, "text": "Meanwhile melt bacon fat in skillet, add chopped ramps, cook until brown."},
            {"step": 4, "text": "Add salt, pepper, flour, and mustard. Cook five minutes."},
            {"step": 5, "text": "Add milk and simmer."}
        ],
        "tags": ["soup", "ramps", "mustard greens", "wild plants", "appalachian", "foxfire"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "appalachian-mustard-flowers",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Cooked Mustard Flowers",
        "category": "vegetables",
        "attribution": "Foxfire Book 2",
        "source_note": "Traditional Appalachian wild plant recipes",
        "description": "Simple preparation of wild mustard flowers.",
        "servings_yield": "2 servings",
        "ingredients": [
            {"item": "mustard flowers", "quantity": "2", "unit": "cups", "prep_note": "newly opened blooms"},
            {"item": "butter or bacon fat", "quantity": "2", "unit": "tbsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Gather newly opened mustard blooms."},
            {"step": 2, "text": "Cook in boiling water until tender."},
            {"step": 3, "text": "Remove from heat, add butter or bacon fat."},
            {"step": 4, "text": "Serve immediately."}
        ],
        "tags": ["vegetables", "wild plants", "mustard", "appalachian", "foxfire"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "appalachian-garlic-vinegar",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Wild Garlic Vinegar",
        "category": "preserves",
        "attribution": "Foxfire Book 2",
        "source_note": "Traditional Appalachian wild plant recipes",
        "description": "Infused vinegar made with wild garlic bulbs.",
        "servings_yield": "1 pint",
        "ingredients": [
            {"item": "wild garlic bulbs", "quantity": "6-8", "unit": "", "prep_note": "peeled"},
            {"item": "vinegar", "quantity": "1", "unit": "pint"}
        ],
        "instructions": [
            {"step": 1, "text": "Peel garlic bulbs."},
            {"step": 2, "text": "Place in one pint vinegar."},
            {"step": 3, "text": "Cover tightly and let stand for ten to fourteen days."},
            {"step": 4, "text": "Strain and bottle."}
        ],
        "tags": ["preserves", "vinegar", "wild garlic", "wild plants", "appalachian", "foxfire"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    # From Foxfire Three - Summer and Fall Wild Plant Foods
    {
        "id": "appalachian-blackberry-nectar",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Blackberry Nectar",
        "category": "beverages",
        "attribution": "Foxfire Three",
        "source_note": "Traditional Appalachian wild plant recipes",
        "description": "Sweet blackberry drink concentrate made with vinegar.",
        "servings_yield": "About 2 pints",
        "ingredients": [
            {"item": "ripe blackberries", "quantity": "1", "unit": "quart", "prep_note": "sound and ripe"},
            {"item": "good vinegar", "quantity": "3", "unit": "cups"},
            {"item": "sugar", "quantity": "1", "unit": "lb", "prep_note": "per pint of juice"}
        ],
        "instructions": [
            {"step": 1, "text": "Select sound, ripe blackberries."},
            {"step": 2, "text": "Add the berries to 3 cups good vinegar in a crock or large jar."},
            {"step": 3, "text": "Cover the crock with cheesecloth and let stand three or four days, stirring daily."},
            {"step": 4, "text": "When ready, strain without crushing the berries."},
            {"step": 5, "text": "Measure, and add one pound sugar for each pint juice."},
            {"step": 6, "text": "Boil gently for five minutes."},
            {"step": 7, "text": "Put in bottles or jars and seal."}
        ],
        "notes": [
            "When serving, dilute with water and crushed ice.",
            "Use less sugar if a tart drink is preferred."
        ],
        "tags": ["beverage", "blackberry", "wild plants", "appalachian", "foxfire"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "appalachian-blackberry-shrub",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Blackberry Shrub",
        "category": "beverages",
        "attribution": "Foxfire Three",
        "source_note": "Traditional Appalachian wild plant recipes",
        "description": "Traditional shrub drink made from blackberries and apple vinegar.",
        "servings_yield": "About 1 quart",
        "ingredients": [
            {"item": "blackberries", "quantity": "1", "unit": "quart", "prep_note": "washed and selected, no sour or imperfect ones"},
            {"item": "apple vinegar", "quantity": "", "unit": "", "prep_note": "two years old, to cover"},
            {"item": "sugar", "quantity": "", "unit": "", "prep_note": "to taste"}
        ],
        "instructions": [
            {"step": 1, "text": "Gather the blackberries, wash and select so that there will be no sour or imperfect ones."},
            {"step": 2, "text": "Cover with apple vinegar (two years old) and cook until soft."},
            {"step": 3, "text": "Strain, and sweeten the juice to taste."},
            {"step": 4, "text": "Boil down until it is about the consistency of thick syrup."},
            {"step": 5, "text": "Bottle and put in a cool, dark place."}
        ],
        "notes": [
            "When serving, use three or four tablespoonfuls to a glass cold water."
        ],
        "tags": ["beverage", "shrub", "blackberry", "wild plants", "appalachian", "foxfire"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "appalachian-raspberry-pickles",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Raspberry Pickles",
        "category": "preserves",
        "attribution": "Foxfire Three",
        "source_note": "Traditional Appalachian wild plant recipes",
        "description": "Spiced pickled raspberries preserved in sweetened vinegar.",
        "servings_yield": "About 1/2 gallon",
        "ingredients": [
            {"item": "fresh raspberries", "quantity": "1/2", "unit": "gallon", "prep_note": "almost ripe"},
            {"item": "cloves", "quantity": "1/2", "unit": "tsp"},
            {"item": "allspice", "quantity": "1/2", "unit": "tsp"},
            {"item": "cinnamon stick", "quantity": "1", "unit": ""},
            {"item": "good apple vinegar", "quantity": "1 1/2", "unit": "pints"},
            {"item": "sugar", "quantity": "1/2", "unit": "cup"}
        ],
        "instructions": [
            {"step": 1, "text": "Wash 1/2 gallon fresh, almost ripe berries."},
            {"step": 2, "text": "Place them in self-sealing jars with a half teaspoon each of cloves and allspice, and one stick of cinnamon."},
            {"step": 3, "text": "Boil 1 1/2 pints of good apple vinegar with a half cup of sugar."},
            {"step": 4, "text": "Pour over the berries."},
            {"step": 5, "text": "Seal while hot."}
        ],
        "tags": ["preserves", "pickles", "raspberry", "wild plants", "appalachian", "foxfire"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "appalachian-raspberry-vinegar",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Raspberry Vinegar",
        "category": "preserves",
        "attribution": "Foxfire Three",
        "source_note": "Traditional Appalachian wild plant recipes",
        "description": "Sweetened raspberry-infused vinegar, a traditional Appalachian condiment.",
        "servings_yield": "About 2 gallons",
        "ingredients": [
            {"item": "ripe raspberries", "quantity": "4", "unit": "gallons", "prep_note": "divided into 2 batches"},
            {"item": "cider vinegar", "quantity": "1", "unit": "gallon"},
            {"item": "sugar", "quantity": "", "unit": "", "prep_note": "equal measure to juice"}
        ],
        "instructions": [
            {"step": 1, "text": "Put two gallons ripe raspberries in a stone jar."},
            {"step": 2, "text": "Pour a gallon cider vinegar over them and let stand twenty-four hours."},
            {"step": 3, "text": "Drain, then pour the liquor over a gallon fresh berries and let stand overnight."},
            {"step": 4, "text": "Strain and add one measure of sugar for every measure of juice."},
            {"step": 5, "text": "Boil and skim."},
            {"step": 6, "text": "Bottle when cold."}
        ],
        "tags": ["preserves", "vinegar", "raspberry", "wild plants", "appalachian", "foxfire"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "appalachian-sumac-elderberry-jelly",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Sumac and Elderberry Jelly",
        "category": "preserves",
        "attribution": "Foxfire Three",
        "source_note": "Traditional Appalachian wild plant recipes",
        "description": "Unique jelly combining wild sumac berries and elderberries.",
        "servings_yield": "About 3 cups",
        "ingredients": [
            {"item": "sumac berries", "quantity": "1", "unit": "pint"},
            {"item": "elderberries", "quantity": "1", "unit": "quart"},
            {"item": "water", "quantity": "6", "unit": "pints", "prep_note": "divided"},
            {"item": "sugar", "quantity": "1", "unit": "cup", "prep_note": "per cup juice"}
        ],
        "instructions": [
            {"step": 1, "text": "Boil one pint sumac berries in three pints water until there is one quart juice."},
            {"step": 2, "text": "Separately, boil one quart elderberries in three pints water until fruit is soft."},
            {"step": 3, "text": "Mash the elderberries."},
            {"step": 4, "text": "Strain juice from both through a thick white cloth."},
            {"step": 5, "text": "Mix the juices together."},
            {"step": 6, "text": "Add one cup sugar for each cup juice and cook into jelly."}
        ],
        "tags": ["preserves", "jelly", "sumac", "elderberry", "wild plants", "appalachian", "foxfire"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "appalachian-elderberry-wine",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Elderberry Wine",
        "category": "beverages",
        "attribution": "Foxfire Three",
        "source_note": "Traditional Appalachian wild plant recipes",
        "description": "Traditional homemade wine from wild elderberries.",
        "servings_yield": "About 1 gallon",
        "ingredients": [
            {"item": "elderberries", "quantity": "5", "unit": "quarts"},
            {"item": "water", "quantity": "6", "unit": "quarts"},
            {"item": "sugar", "quantity": "", "unit": "", "prep_note": "equal to juice amount"}
        ],
        "instructions": [
            {"step": 1, "text": "Use five quarts of berries to six quarts of water."},
            {"step": 2, "text": "Mash the berries and let stand in a crock two weeks, stirring every day."},
            {"step": 3, "text": "Strain."},
            {"step": 4, "text": "Add as much sugar as you have juice."},
            {"step": 5, "text": "Let stand two weeks and then bottle."}
        ],
        "tags": ["beverage", "wine", "elderberry", "wild plants", "appalachian", "foxfire"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "appalachian-elderberry-jam",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Elderberry Jam",
        "category": "preserves",
        "attribution": "Foxfire Three",
        "source_note": "Traditional Appalachian wild plant recipes",
        "description": "Simple jam made from wild elderberries with vinegar.",
        "servings_yield": "About 6 cups",
        "ingredients": [
            {"item": "elderberries", "quantity": "8", "unit": "cups"},
            {"item": "sugar", "quantity": "6", "unit": "cups"},
            {"item": "vinegar", "quantity": "1/4", "unit": "cup"}
        ],
        "instructions": [
            {"step": 1, "text": "Crush and measure the berries."},
            {"step": 2, "text": "Add sugar and vinegar."},
            {"step": 3, "text": "Boil until thick."},
            {"step": 4, "text": "Pour boiling into scalded jars and seal."}
        ],
        "tags": ["preserves", "jam", "elderberry", "wild plants", "appalachian", "foxfire"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "appalachian-elderberry-apple-orange-jam",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Elderberry-Apple-Orange Jam",
        "category": "preserves",
        "attribution": "Foxfire Three",
        "source_note": "Traditional Appalachian wild plant recipes",
        "description": "Rich jam combining elderberries with apples and citrus.",
        "servings_yield": "About 8 cups",
        "ingredients": [
            {"item": "elderberries", "quantity": "1", "unit": "quart"},
            {"item": "sugar", "quantity": "5", "unit": "cups"},
            {"item": "lemon", "quantity": "1", "unit": ""},
            {"item": "large cooking apples", "quantity": "12", "unit": ""},
            {"item": "medium oranges", "quantity": "3", "unit": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Cook apples until mushy."},
            {"step": 2, "text": "Add the berries, oranges, and lemon chopped fine."},
            {"step": 3, "text": "Grate the rinds of one orange and the lemon."},
            {"step": 4, "text": "Mix together with sugar."},
            {"step": 5, "text": "Boil thirty minutes."},
            {"step": 6, "text": "Pour into sterilized jars and seal."}
        ],
        "tags": ["preserves", "jam", "elderberry", "apple", "orange", "wild plants", "appalachian", "foxfire"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "appalachian-steamed-elderberry-pudding",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Steamed Elderberry Pudding",
        "category": "desserts",
        "attribution": "Foxfire Three",
        "source_note": "Traditional Appalachian wild plant recipes",
        "description": "Traditional steamed pudding made with wild elderberries.",
        "servings_yield": "6-8 servings",
        "ingredients": [
            {"item": "elderberries", "quantity": "4", "unit": "cups"},
            {"item": "sugar", "quantity": "2", "unit": "cups"},
            {"item": "lemon juice", "quantity": "1", "unit": "tsp"},
            {"item": "butter", "quantity": "1", "unit": "tbsp"},
            {"item": "flour", "quantity": "2", "unit": "cups"},
            {"item": "baking powder", "quantity": "4", "unit": "tsp"},
            {"item": "salt", "quantity": "1", "unit": "tsp"},
            {"item": "milk", "quantity": "3/4", "unit": "cup"}
        ],
        "instructions": [
            {"step": 1, "text": "Sift dry ingredients (flour, baking powder, salt) together."},
            {"step": 2, "text": "Work in the butter."},
            {"step": 3, "text": "Add milk and mix well."},
            {"step": 4, "text": "Combine sugar, berries, and lemon juice."},
            {"step": 5, "text": "Mix these with the batter."},
            {"step": 6, "text": "Pour into a buttered baking dish."},
            {"step": 7, "text": "Cover tightly and steam forty-five minutes."},
            {"step": 8, "text": "Serve with cream."}
        ],
        "tags": ["dessert", "pudding", "elderberry", "steamed", "wild plants", "appalachian", "foxfire"],
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

    added = 0
    skipped = 0

    for recipe in FINAL_RECIPES:
        if recipe['id'] in existing_ids:
            print(f"  Skipping (exists): {recipe['id']}")
            skipped += 1
        else:
            recipes.append(recipe)
            existing_ids.add(recipe['id'])
            print(f"  Added: {recipe['title']}")
            added += 1

    # Update total count
    data['meta']['total_recipes'] = len(recipes)

    print(f"\nWriting {len(recipes)} recipes back to {RECIPES_FILE}")
    with open(RECIPES_FILE, 'w') as f:
        json.dump(data, f, indent=2)

    print(f"\nDone! Added {added} recipes, skipped {skipped} existing.")
    print(f"Total recipes now: {len(recipes)}")


if __name__ == "__main__":
    main()
