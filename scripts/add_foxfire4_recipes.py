#!/usr/bin/env python3
"""
Add recipes from Foxfire Book 4 to recipes.json

Foxfire 4 contains:
- Cheese-making (Mrs. Reese's Pressed Cheese, Mrs. Earp's Quick Cheese, Cottage Cheese)
- Sassafras Jelly
- Apple Cider
- Bleached Apple Pie
- Fried Apple Pies
"""

import json
from pathlib import Path

RECIPES_FILE = Path(__file__).parent.parent / "data" / "recipes.json"

FOXFIRE4_RECIPES = [
    {
        "id": "foxfire4-pressed-cheese",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Mrs. Reese's Pressed Cheese",
        "category": "dairy",
        "attribution": "Mrs. Monroe Reese, via Foxfire 4",
        "source_note": "Traditional Appalachian cheese-making from Foxfire Book 4",
        "description": "A traditional pressed cheese that forms a dry crust and keeps for a month or more. Uses rennet tablets to curdle the milk.",
        "servings_yield": "1 block of cheese",
        "prep_time": "30 minutes",
        "cook_time": "1 hour",
        "total_time": "13-14 hours (including overnight pressing)",
        "ingredients": [
            {"item": "whole milk (raw, from cow)", "quantity": "2 1/2", "unit": "gallons", "prep_note": "refrigerated"},
            {"item": "Hansen's Cheese Rennet Tablet", "quantity": "1/4", "unit": "tablet", "prep_note": "dissolved in 1 teacup water"},
            {"item": "Hansen's Cheese Color Tablet", "quantity": "1/8", "unit": "tablet", "prep_note": "dissolved in 1 teacup water"},
            {"item": "salt", "quantity": "1", "unit": "heaping tsp", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Pour all the milk into a large pan and heat on a wood stove (for slower, steadier heat) until a little past lukewarm."},
            {"step": 2, "text": "Remove from heat and add the dissolved rennet tablet and color tablet."},
            {"step": 3, "text": "Let sit for 15-30 minutes until the milk stiffens and becomes jelly-like."},
            {"step": 4, "text": "Cut the curd with a knife or spatula into tiny squares, also running the spatula under the surface as if cutting it into layers."},
            {"step": 5, "text": "Let sit briefly, then gently work the mixture until broken into pieces the size of grains of corn."},
            {"step": 6, "text": "Return pan to stove and heat slowly, stirring constantly, until almost as hot as the touch can stand but not boiling."},
            {"step": 7, "text": "Remove from heat and let sit 15-30 minutes to cool."},
            {"step": 8, "text": "Strain contents through cheesecloth in a colander. Let drip naturally, do not squeeze."},
            {"step": 9, "text": "Return curds to pan, add the salt, and massage it in well."},
            {"step": 10, "text": "Put curds into a homemade press lined with cheesecloth. Add weight in stages and leave overnight (12 hours)."},
            {"step": 11, "text": "Remove from press and dry in open air for one week, turning twice daily. The cheese forms a dry crust on the outside."}
        ],
        "temperature": "",
        "pan_size": "Large pan, cheese press",
        "notes": [
            "Before rennet tablets were available, a piece of dried cow stomach lining (about thumbnail size) was used to curdle the milk.",
            "A wood stove is preferred for its slower, steadier heat.",
            "The cheese keeps for a month or more without refrigeration."
        ],
        "tags": ["cheese", "dairy", "appalachian", "foxfire", "traditional", "preservation"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "foxfire4-quick-fried-cheese",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Mrs. Thelma Earp's Quick Fried Cheese",
        "category": "dairy",
        "attribution": "Mrs. Thelma Earp, via Foxfire 4",
        "source_note": "Traditional Appalachian cheese-making from Foxfire Book 4",
        "description": "A quick cheese that can be eaten right away, made by frying curds in butter. Forms a cake as it cools.",
        "servings_yield": "1 cake of cheese",
        "prep_time": "2 days (for clabbering)",
        "cook_time": "30 minutes",
        "total_time": "2 days plus 30 minutes",
        "ingredients": [
            {"item": "whole milk (raw)", "quantity": "2", "unit": "gallons", "prep_note": ""},
            {"item": "buttermilk", "quantity": "4-6", "unit": "tbsp", "prep_note": "for clabbering"},
            {"item": "salt", "quantity": "1 1/2", "unit": "tsp", "prep_note": ""},
            {"item": "egg", "quantity": "1", "unit": "", "prep_note": "raw, barnyard eggs preferred for color"},
            {"item": "butter", "quantity": "1", "unit": "large hen egg size lump", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Allow cream to rise on whole milk, skim it off and make butter."},
            {"step": 2, "text": "Add 2-3 tablespoons buttermilk per gallon of skimmed milk and let sit out for two days to sour."},
            {"step": 3, "text": "Refrigerate the clabbered milk until ready to use."},
            {"step": 4, "text": "Pour clabbered milk into a pan and heat until a little hotter than lukewarm (pretty hot but not boiling, won't burn hands)."},
            {"step": 5, "text": "Pour into a strainer made with cotton cloth pinned over a bucket. Squeeze the whey through, leaving curds."},
            {"step": 6, "text": "Put curds in a bowl, add salt and raw egg. Mix with hands."},
            {"step": 7, "text": "Melt butter in a large iron frying pan. Prefer wood stove for even, slow heat."},
            {"step": 8, "text": "Add curds and keep turning in the pan over medium heat until all curds melt and run together into a cake."},
            {"step": 9, "text": "Put out into a dish to cool. It automatically forms a cake as it cools."}
        ],
        "temperature": "Medium heat",
        "pan_size": "Large iron frying pan",
        "notes": [
            "Can be eaten right away or kept several days.",
            "Do not refrigerate - it should dry out somewhat.",
            "After a short while it gets hard enough to cut into slices.",
            "Keeps about a week.",
            "Feed the whey to the hogs."
        ],
        "tags": ["cheese", "dairy", "appalachian", "foxfire", "traditional", "quick"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "foxfire4-cottage-cheese",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Appalachian Cottage Cheese",
        "category": "dairy",
        "attribution": "Mrs. Harriet Echols and Mrs. Nora Garland, via Foxfire 4",
        "source_note": "Traditional Appalachian cottage cheese from Foxfire Book 4",
        "description": "Simple cottage cheese made by clabbering raw milk, then heating and draining the curds.",
        "servings_yield": "About 1 lb cottage cheese",
        "prep_time": "1-2 days (for clabbering)",
        "cook_time": "2-3 hours (including draining)",
        "total_time": "1-2 days plus 3 hours",
        "ingredients": [
            {"item": "raw whole milk (unpasteurized)", "quantity": "1", "unit": "gallon", "prep_note": ""},
            {"item": "salt", "quantity": "to taste", "unit": "", "prep_note": ""},
            {"item": "sour cream", "quantity": "optional", "unit": "", "prep_note": "reserved from clabbered milk"}
        ],
        "instructions": [
            {"step": 1, "text": "Pour raw milk into an enamel or metal pan."},
            {"step": 2, "text": "Let sit on back of wood stove (winter) or kitchen table (warm weather) to sour slowly. Takes 1-2 days depending on temperature."},
            {"step": 3, "text": "After milk clabbers, lift off the cream and refrigerate (can be used as sour cream or mixed back in later)."},
            {"step": 4, "text": "Heat the skimmed clabbered milk over low fire until it curdles."},
            {"step": 5, "text": "Remove from heat and pour into a colander or cheesecloth to drain. Takes a couple of hours. Can hang in a clean flour sack overnight."},
            {"step": 6, "text": "Work the cheese by squeezing with hands or spoon to remove remaining water. Don't work too vigorously or get curds too fine."},
            {"step": 7, "text": "Sprinkle in salt to taste. For creamier cheese, mix in some of the reserved sour cream."},
            {"step": 8, "text": "Package in small containers and refrigerate. Keeps several weeks."}
        ],
        "temperature": "Low heat",
        "pan_size": "Enamel or metal pan, colander",
        "notes": [
            "Do not heat the milk before it clabbers.",
            "Mrs. Garland put the curdled milk in a clean flour sack and let it drain outside overnight."
        ],
        "tags": ["cheese", "cottage cheese", "dairy", "appalachian", "foxfire", "traditional"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "foxfire4-sassafras-jelly",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Pearl's Sassafras Jelly",
        "category": "preserves",
        "attribution": "Pearl, via Foxfire 4",
        "source_note": "Traditional Appalachian sassafras jelly recipe from Foxfire Book 4",
        "description": "A unique jelly made from sassafras tea, capturing the distinctive flavor of this Appalachian root.",
        "servings_yield": "Several jars",
        "prep_time": "30 minutes",
        "cook_time": "30 minutes",
        "total_time": "1 hour",
        "ingredients": [
            {"item": "sassafras tea", "quantity": "8", "unit": "cups", "prep_note": "made by boiling 4 roots in 1 gallon water for 15-20 minutes"},
            {"item": "Sure-Jell", "quantity": "1", "unit": "package", "prep_note": ""},
            {"item": "sugar", "quantity": "8", "unit": "cups", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Make sassafras tea: Boil 4 average-sized sassafras roots in 1 gallon of water for 15-20 minutes. The longer boiled, the stronger the tea. Strain."},
            {"step": 2, "text": "Mix one package of Sure-Jell with 8 cups of sassafras tea in a large saucepan."},
            {"step": 3, "text": "Bring quickly to a hard boil, stirring occasionally."},
            {"step": 4, "text": "Add 8 cups sugar and bring to a full rolling boil."},
            {"step": 5, "text": "Boil hard one minute, stirring constantly."},
            {"step": 6, "text": "Skim off foam with a metal spoon."},
            {"step": 7, "text": "Pour at once into jelly jars and seal with paraffin."}
        ],
        "temperature": "",
        "pan_size": "Large saucepan",
        "notes": [
            "Pearl also makes sassafras tea, serving it hot or iced, sweetened with sugar or honey.",
            "Sassafras tea can be made stronger or weaker by adjusting boiling time."
        ],
        "tags": ["jelly", "preserves", "sassafras", "appalachian", "foxfire", "wild foods"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "foxfire4-bleached-apple-pie",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Mrs. Parker's Bleached Apple Pie",
        "category": "desserts",
        "attribution": "Mrs. Parker, via Foxfire 4",
        "source_note": "Traditional Appalachian bleached apple pie from Foxfire Book 4",
        "description": "A pie made with sulfur-bleached apples that taste like fresh apples even months after preserving.",
        "servings_yield": "1 pie",
        "prep_time": "15 minutes",
        "cook_time": "30-35 minutes",
        "total_time": "45-50 minutes",
        "ingredients": [
            {"item": "bleached apple pieces", "quantity": "several", "unit": "cups", "prep_note": "sulfur-preserved"},
            {"item": "pie crust", "quantity": "1", "unit": "", "prep_note": "uncooked"},
            {"item": "butter", "quantity": "to taste", "unit": "", "prep_note": ""},
            {"item": "sugar", "quantity": "to taste", "unit": "", "prep_note": ""},
            {"item": "cinnamon", "quantity": "to taste", "unit": "", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Preheat oven to 350°F (175°C)."},
            {"step": 2, "text": "Place several cups of bleached apple pieces in an uncooked pie crust."},
            {"step": 3, "text": "Add butter, sugar, and cinnamon to taste."},
            {"step": 4, "text": "Cover with pastry strips or a second crust if preferred."},
            {"step": 5, "text": "Bake for 30-35 minutes or until crust is golden brown."}
        ],
        "temperature": "350°F (175°C)",
        "pan_size": "Pie pan",
        "notes": [
            "Bleached apples are preserved using sulfur smoke in a special box.",
            "Use as little water as possible when cooking bleached apples - water brings back the sulfur taste.",
            "The sulfur taste is not noticeable when apples are eaten dry."
        ],
        "tags": ["pie", "desserts", "apple", "appalachian", "foxfire", "traditional"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "foxfire4-fried-apple-pies",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Blanche Harkins' Fried Apple Pies",
        "category": "desserts",
        "attribution": "Blanche Harkins, via Foxfire 4",
        "source_note": "Traditional Appalachian fried apple pies from Foxfire Book 4",
        "description": "Traditional half-moon shaped pies filled with spiced dried apples, fried until golden. Yellow apples make tastier pies.",
        "servings_yield": "4 small pies",
        "prep_time": "30 minutes",
        "cook_time": "20 minutes",
        "total_time": "50 minutes (plus time for drying apples)",
        "ingredients": [
            {"item": "dried apples", "quantity": "1", "unit": "quart", "prep_note": "red or yellow, yellow preferred"},
            {"item": "sugar", "quantity": "to taste", "unit": "", "prep_note": ""},
            {"item": "cinnamon or allspice", "quantity": "to taste", "unit": "", "prep_note": ""},
            {"item": "self-rising flour", "quantity": "4", "unit": "cups", "prep_note": ""},
            {"item": "Crisco (shortening)", "quantity": "1/2", "unit": "cup", "prep_note": "for crust"},
            {"item": "water", "quantity": "1", "unit": "cup", "prep_note": "for crust"},
            {"item": "Crisco (shortening)", "quantity": "enough to almost cover pies", "unit": "", "prep_note": "for frying"},
            {"item": "butter", "quantity": "for brushing", "unit": "", "prep_note": "optional, for baking"}
        ],
        "instructions": [
            {"step": 1, "text": "To dry apples: Peel and core apples, cut into thin slices. Soak in salt water, drain, lay on flat board or pan on white cloth. Dry outside in sunshine for several days until shrunk to half size. Store in sacks in dry place."},
            {"step": 2, "text": "To prepare filling: Add small amount of water to dried apples and cook until tender. Mash with a fork. Add sugar and cinnamon or allspice to taste."},
            {"step": 3, "text": "Make pie crust: Mix 4 cups self-rising flour with 1/2 cup Crisco and 1 cup water. Work like regular pie crust."},
            {"step": 4, "text": "Divide dough into fist-sized balls (one per pie)."},
            {"step": 5, "text": "Roll each ball into a very thin circle."},
            {"step": 6, "text": "Place cooked apples on one half of the circle."},
            {"step": 7, "text": "Fold crust over apples and press edges together with fingers or fork."},
            {"step": 8, "text": "Make tiny holes or slits in top with fork or knife to let air out."},
            {"step": 9, "text": "Put enough Crisco in large iron frying pan to almost cover the pies. Fry until golden."},
            {"step": 10, "text": "Alternatively, brush with melted butter and bake for crisp crust."}
        ],
        "temperature": "Medium-high heat for frying",
        "pan_size": "Large iron frying pan",
        "notes": [
            "Yellow apples make tastier pies than red.",
            "The holes in the crust prevent edges from turning up during cooking.",
            "Can be baked instead of fried - brush with melted butter before baking."
        ],
        "tags": ["pie", "fried pie", "desserts", "apple", "appalachian", "foxfire", "traditional", "dried fruit"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "foxfire4-apple-cider",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Mrs. Brown's Apple Cider",
        "category": "beverages",
        "attribution": "Mrs. Harry Brown of Betty's Creek Community, via Foxfire 4",
        "source_note": "Traditional Appalachian apple cider from Foxfire Book 4",
        "description": "Old-fashioned apple cider made with a traditional cider press, using a mix of sour and sweet apples.",
        "servings_yield": "Varies by quantity of apples",
        "prep_time": "30 minutes",
        "cook_time": "None (fresh) or time for canning",
        "total_time": "30 minutes to several hours",
        "ingredients": [
            {"item": "apples (sour)", "quantity": "half", "unit": "of total", "prep_note": "washed"},
            {"item": "apples (sweet)", "quantity": "half", "unit": "of total", "prep_note": "washed"}
        ],
        "instructions": [
            {"step": 1, "text": "Wash apples thoroughly."},
            {"step": 2, "text": "Use a proportion of half sour and half sweet apples. Adjust ratio for sweeter or more tart cider."},
            {"step": 3, "text": "Place whole apples into the wooden hopper of the cider mill."},
            {"step": 4, "text": "Turn the mill crank to crush apples. Pulp drops into a slatted, bottomless tub."},
            {"step": 5, "text": "When tub is full, move it under the screw press."},
            {"step": 6, "text": "Fit wooden disc into top of tub and turn the screw to press disc down onto apple pulp, squeezing out all juice."},
            {"step": 7, "text": "Strain cider through cheesecloth into pans or pitchers."},
            {"step": 8, "text": "Serve fresh, or preserve by canning or freezing."}
        ],
        "temperature": "",
        "pan_size": "Cider press, pans, cheesecloth",
        "notes": [
            "Any type of apples can be used.",
            "For sweeter cider, add more sweet apples; for more tart, add more sour apples.",
            "Cider can be preserved by canning or freezing.",
            "Mrs. Brown prefers freezing to canning."
        ],
        "tags": ["cider", "beverages", "apple", "appalachian", "foxfire", "traditional", "preservation"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    }
]


def main():
    # Load existing recipes
    with open(RECIPES_FILE, 'r') as f:
        data = json.load(f)

    recipes = data['recipes']

    # Track existing IDs
    existing_ids = {r['id'] for r in recipes}

    # Add new recipes
    added = 0
    for recipe in FOXFIRE4_RECIPES:
        if recipe['id'] not in existing_ids:
            recipes.append(recipe)
            existing_ids.add(recipe['id'])
            added += 1
            print(f"Added: {recipe['title']}")
        else:
            print(f"Skipped (exists): {recipe['title']}")

    # Update meta
    data['meta']['total_recipes'] = len(recipes)

    # Save updated recipes
    with open(RECIPES_FILE, 'w') as f:
        json.dump(data, f, indent=2)

    print(f"\nAdded {added} Foxfire 4 recipes. Total: {len(recipes)}")


if __name__ == "__main__":
    main()
