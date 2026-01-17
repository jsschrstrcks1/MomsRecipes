#!/usr/bin/env python3
"""
Script to add Foxfire Vol 1 recipes - Batch 2 (Hog recipes and more preserves)
"""
import json
from pathlib import Path

DATA_DIR = Path(__file__).parent.parent / "data"
RECIPES_FILE = DATA_DIR / "recipes.json"

FOXFIRE_RECIPES_BATCH2 = [
    # === HOG RECIPES ===
    {
        "id": "foxfire-souse-headcheese",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Souse (Headcheese)",
        "category": "main dishes",
        "attribution": "Foxfire Vol 1",
        "source_note": "Traditional Appalachian hog recipe from The Foxfire Book",
        "description": "Also called 'souse meat,' 'headcheese,' or 'pressed hog's head.' A traditional way to use the whole hog.",
        "servings_yield": "",
        "prep_time": "Overnight soaking",
        "cook_time": "Until meat falls off bone",
        "total_time": "",
        "ingredients": [
            {"item": "hog's head", "quantity": "1", "unit": "", "prep_note": "trimmed, scraped, eyes removed"},
            {"item": "salt", "quantity": "", "unit": "for soaking and cooking", "prep_note": ""},
            {"item": "sage", "quantity": "1", "unit": "tbsp", "prep_note": "per head"},
            {"item": "ground red pepper", "quantity": "1/2", "unit": "tsp", "prep_note": ""},
            {"item": "black pepper", "quantity": "", "unit": "to taste", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Trim, scrape, or singe off any hairs or bristles. Cut out the eyes."},
            {"step": 2, "text": "Remove ears, brains, snout, tongue, or jowls if using separately; otherwise leave on for grinding."},
            {"step": 3, "text": "Halve or quarter the head with an axe. Soak overnight in fresh water to remove blood."},
            {"step": 4, "text": "Rinse until water runs clear."},
            {"step": 5, "text": "Put in a pot of clean, salty water and cook slowly until meat falls off the bones."},
            {"step": 6, "text": "Remove all meat from bones and run through a food chopper."},
            {"step": 7, "text": "Season with sage, red pepper, black pepper, and salt to taste."},
            {"step": 8, "text": "Mix thoroughly and put into jars, a mold, or a plate covered with clean white cloth."},
            {"step": 9, "text": "Store in smokehouse where winter weather will keep it fresh."}
        ],
        "temperature": "",
        "pan_size": "Large pot",
        "notes": [
            "Can be eaten cold or reheated",
            "Ears are gristly and leave white flukes in the meat - some find this unattractive",
            "Alternative seasoning: one onion, one pod strong red pepper chopped fine, one tsp salt",
            "Beulah Perry uses: red and black pepper, onion, a little corn meal, sage and garlic",
            "Evie Carpenter adds: a little vinegar, sage, black pepper and onion"
        ],
        "tags": ["souse", "headcheese", "hog", "appalachian", "foxfire", "meat", "preserving"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": ["FoxfireVol1.txt.html"]
    },
    {
        "id": "foxfire-scrapple",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Scrapple",
        "category": "main dishes",
        "attribution": "Foxfire Vol 1 - Mrs. Mann Norton",
        "source_note": "Traditional Appalachian recipe from The Foxfire Book, as told by Mrs. Mann Norton",
        "description": "Cornmeal mush with hog's head meat. Mann Norton added, 'Just hold your tongue so y'didn't swaller it when y'went t'eatin'!'",
        "servings_yield": "",
        "prep_time": "",
        "cook_time": "",
        "total_time": "",
        "ingredients": [
            {"item": "hog's head", "quantity": "1", "unit": "", "prep_note": "eyes, ears removed, cleaned"},
            {"item": "sage", "quantity": "", "unit": "to taste", "prep_note": ""},
            {"item": "pepper", "quantity": "", "unit": "to taste", "prep_note": ""},
            {"item": "corn meal", "quantity": "", "unit": "enough to make thick", "prep_note": "plain"}
        ],
        "instructions": [
            {"step": 1, "text": "Take the head, take the eyeballs out and the ears, and cut down in there. Get all the hairs off."},
            {"step": 2, "text": "Put it in a big pot and cook it til the meat just turns loose of the main big bone."},
            {"step": 3, "text": "Lift them bones out, and lay your meat over and feel with your hands to check for bones."},
            {"step": 4, "text": "Strain your liquid through a strainer so the little bones come out."},
            {"step": 5, "text": "Put the liquid back in a pot, and put that mashed meat back in that liquid."},
            {"step": 6, "text": "Put your sage and pepper in there."},
            {"step": 7, "text": "Stir it til it got to boiling."},
            {"step": 8, "text": "Stir in plain corn meal til it's just plumb thick."},
            {"step": 9, "text": "Pour it up in a mold, and cut it off and fry it and brown it."}
        ],
        "temperature": "",
        "pan_size": "Large pot, mold",
        "notes": ["Mrs. Norton: 'Tastes just like fish.'"],
        "tags": ["scrapple", "hog", "cornmeal", "appalachian", "foxfire", "breakfast", "meat"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": ["FoxfireVol1.txt.html"]
    },
    {
        "id": "foxfire-liver-mush",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Liver Pudding (Liver Mush)",
        "category": "main dishes",
        "attribution": "Foxfire Vol 1",
        "source_note": "Traditional Appalachian hog recipe from The Foxfire Book",
        "description": "Traditional liver mush made with hog liver and cornmeal.",
        "servings_yield": "",
        "prep_time": "",
        "cook_time": "",
        "total_time": "",
        "ingredients": [
            {"item": "hog liver", "quantity": "1", "unit": "", "prep_note": "cut up, washed, skin removed"},
            {"item": "salt", "quantity": "", "unit": "to taste", "prep_note": ""},
            {"item": "black pepper", "quantity": "1/2", "unit": "tsp", "prep_note": ""},
            {"item": "sage", "quantity": "2", "unit": "tbsp", "prep_note": ""},
            {"item": "red pepper", "quantity": "", "unit": "to taste", "prep_note": "optional"},
            {"item": "broth from cooking", "quantity": "1", "unit": "cup", "prep_note": ""},
            {"item": "corn meal", "quantity": "", "unit": "enough to thicken", "prep_note": "sifted"}
        ],
        "instructions": [
            {"step": 1, "text": "Cut up the liver, wash it well, and remove skin."},
            {"step": 2, "text": "Boil until tender in salted water."},
            {"step": 3, "text": "Remove and run through a colander until fine, or mash well."},
            {"step": 4, "text": "Mix the meat with one cup of the broth it was cooked in."},
            {"step": 5, "text": "Bring to a boil slowly, stirring in sifted corn meal until thick."},
            {"step": 6, "text": "Stir in salt (to taste), half teaspoon black pepper, two tablespoons sage, and a little red pepper if desired."},
            {"step": 7, "text": "Pour into a mold and let sit until cold."},
            {"step": 8, "text": "Slice and eat. Some eat it as a sandwich, or warm the slices in bacon fat."}
        ],
        "temperature": "",
        "pan_size": "Pot, mold",
        "notes": ["Can be eaten cold, as sandwich, or warmed in bacon fat"],
        "tags": ["liver-mush", "liver-pudding", "hog", "appalachian", "foxfire", "breakfast"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": ["FoxfireVol1.txt.html"]
    },
    {
        "id": "foxfire-sausage",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Mountain Sausage",
        "category": "main dishes",
        "attribution": "Foxfire Vol 1",
        "source_note": "Traditional Appalachian hog recipe from The Foxfire Book",
        "description": "Traditional country sausage with sage and peppers, preserved in hot grease.",
        "servings_yield": "",
        "prep_time": "",
        "cook_time": "",
        "total_time": "",
        "ingredients": [
            {"item": "lean pork", "quantity": "10", "unit": "lb", "prep_note": "trimmings from hams, shoulders, etc."},
            {"item": "salt", "quantity": "1/4", "unit": "cup", "prep_note": ""},
            {"item": "brown sugar", "quantity": "1/2", "unit": "cup", "prep_note": ""},
            {"item": "sage", "quantity": "2", "unit": "tbsp", "prep_note": ""},
            {"item": "black pepper", "quantity": "2", "unit": "tsp", "prep_note": ""},
            {"item": "red pepper", "quantity": "2", "unit": "tsp", "prep_note": "many parch their own"}
        ],
        "instructions": [
            {"step": 1, "text": "Use any combination of lean meat not used otherwise - trimmings from hams, shoulders, middlin' meat, tenderloin, head meat, and jowls if desired."},
            {"step": 2, "text": "Run the mixture through a sausage grinder."},
            {"step": 3, "text": "Fry it good and brown (but not completely cooked since it has to be reheated when served)."},
            {"step": 4, "text": "Pack into jars (half to three-quarters full) while still very hot."},
            {"step": 5, "text": "Pour hot grease over the top."},
            {"step": 6, "text": "Close the jars and turn them upside down to cool."},
            {"step": 7, "text": "When the grease cools, it seals the lids shut."}
        ],
        "temperature": "",
        "pan_size": "",
        "notes": [
            "Store with jars remaining upside down",
            "Many parch their own red pepper in front of the fireplace, crush it, then add to sausage",
            "Alternative storage: Roll into balls, pack in churn jar, pour hot grease over, tie cloth over lid, set in spring house water trough",
            "Can also pack in cleaned small intestine, tie off, hang in smokehouse",
            "Or pack in washed corn shuck, tie closed, hang in smokehouse",
            "Or pack in small clean white cloth sacks and hang in smokehouse"
        ],
        "tags": ["sausage", "hog", "appalachian", "foxfire", "meat", "preserving"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": ["FoxfireVol1.txt.html"]
    },
    {
        "id": "foxfire-chitlins",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Chitterlings (Chitlins)",
        "category": "main dishes",
        "attribution": "Foxfire Vol 1",
        "source_note": "Traditional Appalachian hog recipe from The Foxfire Book",
        "description": "Fried hog intestines - a traditional mountain delicacy.",
        "servings_yield": "",
        "prep_time": "3-4 days soaking",
        "cook_time": "",
        "total_time": "",
        "ingredients": [
            {"item": "hog intestines", "quantity": "", "unit": "sections", "prep_note": ""},
            {"item": "salt", "quantity": "", "unit": "", "prep_note": ""},
            {"item": "pepper", "quantity": "1/2", "unit": "pod", "prep_note": ""},
            {"item": "flour", "quantity": "", "unit": "", "prep_note": "for batter"},
            {"item": "water", "quantity": "", "unit": "", "prep_note": "for batter"},
            {"item": "baking powder", "quantity": "", "unit": "", "prep_note": "for batter"},
            {"item": "egg", "quantity": "1", "unit": "", "prep_note": "optional, for batter"},
            {"item": "corn meal", "quantity": "", "unit": "for coating", "prep_note": "alternative to batter"},
            {"item": "grease", "quantity": "", "unit": "for frying", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Put sections of intestine in a jar of salt water and let sit for three or four days."},
            {"step": 2, "text": "Take out, rinse, wash, and rinse again."},
            {"step": 3, "text": "In winter, can lightly salt, put in jars, and keep a few days before cooking."},
            {"step": 4, "text": "When cooking, cut up in small pieces and remove any unwanted layers of lining."},
            {"step": 5, "text": "Boil in salt water with a half pod of pepper until tender."},
            {"step": 6, "text": "Either dip into a batter made of flour, water, and baking powder (with an egg if desired) and fry; or roll in corn meal and fry in grease."}
        ],
        "temperature": "",
        "pan_size": "",
        "notes": [],
        "tags": ["chitlins", "chitterlings", "hog", "appalachian", "foxfire", "fried"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": ["FoxfireVol1.txt.html"]
    },
    # === MORE PRESERVES ===
    {
        "id": "foxfire-watermelon-pickles",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Watermelon Pickles",
        "category": "preserves",
        "attribution": "Foxfire Vol 1",
        "source_note": "Traditional Appalachian recipe from The Foxfire Book",
        "description": "Sweet pickled watermelon rind.",
        "servings_yield": "About 12 half pints",
        "prep_time": "",
        "cook_time": "",
        "total_time": "",
        "ingredients": [
            {"item": "watermelon rind", "quantity": "4", "unit": "lb", "prep_note": "pink pulp and outer peel removed"},
            {"item": "cold water", "quantity": "2", "unit": "quarts", "prep_note": ""},
            {"item": "slaked lime", "quantity": "1", "unit": "tbsp", "prep_note": ""},
            {"item": "whole allspice", "quantity": "2", "unit": "tbsp", "prep_note": ""},
            {"item": "whole cloves", "quantity": "2", "unit": "tbsp", "prep_note": ""},
            {"item": "cider vinegar", "quantity": "1", "unit": "quart", "prep_note": ""},
            {"item": "sugar", "quantity": "4", "unit": "lb", "prep_note": ""},
            {"item": "stick cinnamon", "quantity": "10", "unit": "pieces", "prep_note": "2-inch pieces"}
        ],
        "instructions": [
            {"step": 1, "text": "Remove all pink pulp from watermelon rind. Peel outside peeling from the rind. Weigh."},
            {"step": 2, "text": "Cut in 1 inch circles or cubes."},
            {"step": 3, "text": "Combine cold water and lime. Pour over rind. Let stand one hour. Drain."},
            {"step": 4, "text": "Cover with fresh cold water. Simmer 1 1/2 hours or until tender. Drain."},
            {"step": 5, "text": "Tie spices in a cheesecloth."},
            {"step": 6, "text": "Combine vinegar, 1 quart water, and sugar. Heat until sugar dissolves."},
            {"step": 7, "text": "Add spice bag and rind; simmer gently two hours."},
            {"step": 8, "text": "Pack rind in clean hot sterile jars. Fill jars with boiling hot syrup. Seal."}
        ],
        "temperature": "",
        "pan_size": "",
        "notes": [],
        "tags": ["watermelon", "pickles", "preserves", "appalachian", "foxfire", "canning"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": ["FoxfireVol1.txt.html"]
    },
    {
        "id": "foxfire-tomato-catsup",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Tomato Catsup",
        "category": "preserves",
        "attribution": "Foxfire Vol 1",
        "source_note": "Traditional Appalachian recipe from The Foxfire Book",
        "description": "Homemade tomato ketchup.",
        "servings_yield": "",
        "prep_time": "",
        "cook_time": "3 hours",
        "total_time": "",
        "ingredients": [
            {"item": "tomatoes", "quantity": "", "unit": "enough to make a gallon when cooked", "prep_note": "good, firm, ripe"},
            {"item": "sugar", "quantity": "1/2", "unit": "cup", "prep_note": ""},
            {"item": "ground mustard", "quantity": "2", "unit": "tbsp", "prep_note": ""},
            {"item": "cider vinegar", "quantity": "1", "unit": "pint", "prep_note": ""},
            {"item": "salt", "quantity": "3", "unit": "tbsp", "prep_note": ""},
            {"item": "black pepper", "quantity": "1", "unit": "tbsp", "prep_note": ""},
            {"item": "ground cloves", "quantity": "1/2", "unit": "tbsp", "prep_note": ""},
            {"item": "ground allspice", "quantity": "1", "unit": "tbsp", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Select good, firm ripe tomatoes."},
            {"step": 2, "text": "Scald and strain through a coarse sieve to remove seed and skin."},
            {"step": 3, "text": "When cold, add to each gallon of tomatoes the spices, sugar, vinegar, and salt."},
            {"step": 4, "text": "Let simmer slowly for three hours."},
            {"step": 5, "text": "Seal in bottles or jars."}
        ],
        "temperature": "",
        "pan_size": "",
        "notes": [],
        "tags": ["catsup", "ketchup", "tomato", "preserves", "appalachian", "foxfire"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": ["FoxfireVol1.txt.html"]
    },
    {
        "id": "foxfire-pear-preserves",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Pear Preserves",
        "category": "preserves",
        "attribution": "Foxfire Vol 1",
        "source_note": "Traditional Appalachian recipe from The Foxfire Book",
        "description": "Simple pear preserves with sugar.",
        "servings_yield": "",
        "prep_time": "Overnight",
        "cook_time": "",
        "total_time": "",
        "ingredients": [
            {"item": "pears", "quantity": "", "unit": "", "prep_note": "washed, peeled, cut into quarters"},
            {"item": "sugar", "quantity": "", "unit": "layers", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Wash pears, peel, and cut into quarters. Rinse."},
            {"step": 2, "text": "Place a layer of sugar and a layer of pears until all the fruit has been used."},
            {"step": 3, "text": "Let this stand overnight."},
            {"step": 4, "text": "Put over moderate heat and cook until well done and a syrup has been made from the mixture."},
            {"step": 5, "text": "Put into sterile jars and seal."}
        ],
        "temperature": "",
        "pan_size": "",
        "notes": [],
        "tags": ["pear", "preserves", "appalachian", "foxfire", "canning"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": ["FoxfireVol1.txt.html"]
    },
    {
        "id": "foxfire-mint-jelly",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Mint Jelly from Apple Juice",
        "category": "preserves",
        "attribution": "Foxfire Vol 1",
        "source_note": "Traditional Appalachian recipe from The Foxfire Book",
        "description": "Apple-based mint jelly.",
        "servings_yield": "",
        "prep_time": "1 hour steeping",
        "cook_time": "",
        "total_time": "",
        "ingredients": [
            {"item": "mint leaves", "quantity": "1", "unit": "cup", "prep_note": "chopped fine and packed tight"},
            {"item": "boiling water", "quantity": "", "unit": "to cover", "prep_note": ""},
            {"item": "apple juice", "quantity": "1", "unit": "cup", "prep_note": ""},
            {"item": "sugar", "quantity": "3/4", "unit": "cup", "prep_note": ""},
            {"item": "green food coloring", "quantity": "", "unit": "", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Pour boiling water over the clean mint leaves."},
            {"step": 2, "text": "Cover and allow to steep for one hour."},
            {"step": 3, "text": "Press juice from the leaves."},
            {"step": 4, "text": "Add 2 tablespoons of this extract to 1 cup apple juice and 3/4 cup sugar."},
            {"step": 5, "text": "Boil until jelly test is reached."},
            {"step": 6, "text": "Add green food coloring."},
            {"step": 7, "text": "Pour into hot glasses and seal."}
        ],
        "temperature": "",
        "pan_size": "",
        "notes": [],
        "tags": ["mint", "jelly", "apple", "preserves", "appalachian", "foxfire"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": ["FoxfireVol1.txt.html"]
    },
    {
        "id": "foxfire-muscadine-wine",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Muscadine Wine",
        "category": "beverages",
        "attribution": "Foxfire Vol 1",
        "source_note": "Traditional Appalachian recipe from The Foxfire Book",
        "description": "Traditional muscadine grape wine.",
        "servings_yield": "About 4 gallons",
        "prep_time": "",
        "cook_time": "",
        "total_time": "About 2-3 weeks fermentation",
        "ingredients": [
            {"item": "muscadine grapes", "quantity": "1/2", "unit": "bushel", "prep_note": ""},
            {"item": "sugar", "quantity": "12 1/2", "unit": "lb", "prep_note": "divided"}
        ],
        "instructions": [
            {"step": 1, "text": "Mash the grapes with your hands."},
            {"step": 2, "text": "Put them in a large churn and add 2 1/2 pounds sugar."},
            {"step": 3, "text": "Let it work (ferment) for about a week, until it quits."},
            {"step": 4, "text": "Strain the mixture to get out the grape skins and impurities."},
            {"step": 5, "text": "Put back in the churn, add 10 pounds more of sugar."},
            {"step": 6, "text": "Let it work about eight to ten days until it quits."}
        ],
        "temperature": "",
        "pan_size": "Large churn",
        "notes": [],
        "tags": ["wine", "muscadine", "grapes", "appalachian", "foxfire", "beverage", "fermented"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": ["FoxfireVol1.txt.html"]
    },
    {
        "id": "foxfire-apple-beer",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Apple Beer",
        "category": "beverages",
        "attribution": "Foxfire Vol 1",
        "source_note": "Traditional Appalachian recipe from The Foxfire Book",
        "description": "A simple fermented beverage made from apple peelings.",
        "servings_yield": "",
        "prep_time": "",
        "cook_time": "",
        "total_time": "1-2 days",
        "ingredients": [
            {"item": "apple peelings", "quantity": "", "unit": "", "prep_note": "dried in sun or by stove"},
            {"item": "boiling water", "quantity": "", "unit": "enough to cover", "prep_note": ""},
            {"item": "sugar", "quantity": "", "unit": "optional", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Peel your apples and dry the peelings in the sun or by the stove."},
            {"step": 2, "text": "Put them in a crock and add enough boiling water to cover them."},
            {"step": 3, "text": "Cover the crock and let it sit for one or two days, until all the flavor comes out of the peelings."},
            {"step": 4, "text": "You may add some sugar if you want."}
        ],
        "temperature": "",
        "pan_size": "Crock",
        "notes": ["A frugal way to use apple peelings that would otherwise be discarded"],
        "tags": ["apple", "beer", "beverage", "appalachian", "foxfire", "fermented"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": ["FoxfireVol1.txt.html"]
    }
]

def main():
    with open(RECIPES_FILE, 'r') as f:
        data = json.load(f)

    existing_ids = {r['id'] for r in data['recipes']}
    added = 0
    for recipe in FOXFIRE_RECIPES_BATCH2:
        if recipe['id'] not in existing_ids:
            data['recipes'].append(recipe)
            added += 1
            print(f"Added: {recipe['title']}")
        else:
            print(f"Skipped (exists): {recipe['title']}")

    data['meta']['total_recipes'] = len(data['recipes'])
    data['meta']['last_updated'] = "2026-01-17"

    with open(RECIPES_FILE, 'w') as f:
        json.dump(data, f, indent=2)

    print(f"\nAdded {added} new recipes. Total: {len(data['recipes'])}")

if __name__ == "__main__":
    main()
