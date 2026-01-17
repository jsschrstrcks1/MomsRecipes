#!/usr/bin/env python3
"""
Script to add Foxfire 3 recipes to recipes.json
Summer and Fall Wild Plant Foods chapter - berry and fruit recipes
"""
import json
from pathlib import Path

DATA_DIR = Path(__file__).parent.parent / "data"
RECIPES_FILE = DATA_DIR / "recipes.json"

# Foxfire 3 recipes - Summer and Fall Wild Plant Foods (Berries)
FOXFIRE3_RECIPES = [
    # === MULBERRY RECIPES ===
    {
        "id": "foxfire3-mulberry-candy",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Mulberry Candy",
        "category": "desserts",
        "attribution": "Foxfire 3",
        "source_note": "Traditional Appalachian recipe from Foxfire 3",
        "description": "Simple candy balls made from mulberries and walnuts.",
        "servings_yield": "",
        "prep_time": "",
        "cook_time": "",
        "total_time": "",
        "ingredients": [
            {"item": "mulberries", "quantity": "", "unit": "", "prep_note": "crushed"},
            {"item": "walnuts", "quantity": "", "unit": "", "prep_note": "ground"},
            {"item": "sugar", "quantity": "", "unit": "for rolling", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Crush mulberries and mix with ground walnuts."},
            {"step": 2, "text": "Make small balls and roll in sugar."}
        ],
        "temperature": "",
        "pan_size": "",
        "notes": ["Red mulberries ripen in June and are best for cooking"],
        "tags": ["candy", "mulberry", "walnuts", "no-bake", "appalachian", "foxfire", "foraging"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": ["foxfire-three.txt"]
    },
    {
        "id": "foxfire3-mulberry-pie",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Mulberry Pie",
        "category": "desserts",
        "attribution": "Foxfire 3",
        "source_note": "Traditional Appalachian recipe from Foxfire 3",
        "description": "A creamy pie made with fresh mulberries.",
        "servings_yield": "1 pie",
        "prep_time": "",
        "cook_time": "",
        "total_time": "",
        "ingredients": [
            {"item": "mulberries", "quantity": "", "unit": "", "prep_note": "cooked and drained"},
            {"item": "eggs", "quantity": "2", "unit": "", "prep_note": "beaten"},
            {"item": "cream", "quantity": "1", "unit": "cup", "prep_note": ""},
            {"item": "sugar", "quantity": "1/2", "unit": "cup", "prep_note": ""},
            {"item": "pie shell", "quantity": "1", "unit": "", "prep_note": "unbaked"}
        ],
        "instructions": [
            {"step": 1, "text": "Cook mulberries and drain."},
            {"step": 2, "text": "Mix with two beaten eggs, one cup cream, and 1/2 cup sugar."},
            {"step": 3, "text": "Fill a pie shell and bake."}
        ],
        "temperature": "350°F (175°C)",
        "pan_size": "Pie pan",
        "notes": [],
        "tags": ["pie", "mulberry", "dessert", "appalachian", "foxfire", "foraging"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": ["foxfire-three.txt"]
    },
    # === SERVICEBERRY RECIPES ===
    {
        "id": "foxfire3-serviceberry-pie",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Serviceberry Pie",
        "category": "desserts",
        "attribution": "Foxfire 3 - Jake Waldroop",
        "source_note": "Traditional Appalachian recipe from Foxfire 3",
        "description": "A pie made from serviceberries (sarviceberries). Jake Waldroop said, 'The berries are just wonderful for pies.'",
        "servings_yield": "1 pie",
        "prep_time": "",
        "cook_time": "",
        "total_time": "",
        "ingredients": [
            {"item": "ripe serviceberries", "quantity": "1", "unit": "pint", "prep_note": ""},
            {"item": "sugar", "quantity": "2/3", "unit": "cup", "prep_note": ""},
            {"item": "pie shell", "quantity": "1", "unit": "", "prep_note": "unbaked"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat one pint ripe berries and 2/3 cup sugar."},
            {"step": 2, "text": "Pour into a pie shell."},
            {"step": 3, "text": "Bake in a hot oven."}
        ],
        "temperature": "400°F (205°C)",
        "pan_size": "Pie pan",
        "notes": [
            "Serviceberries can be substituted for blueberries in pie recipes",
            "Also called sarviceberry, juneberry, or sarvis"
        ],
        "tags": ["pie", "serviceberry", "sarvis", "dessert", "appalachian", "foxfire", "foraging"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": ["foxfire-three.txt"]
    },
    {
        "id": "foxfire3-serviceberry-flan",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Serviceberry Flan",
        "category": "desserts",
        "attribution": "Foxfire 3",
        "source_note": "Traditional Appalachian recipe from Foxfire 3",
        "description": "A custard flan with serviceberries.",
        "servings_yield": "",
        "prep_time": "",
        "cook_time": "",
        "total_time": "",
        "ingredients": [
            {"item": "serviceberries", "quantity": "3", "unit": "cups", "prep_note": ""},
            {"item": "sugar", "quantity": "1/2", "unit": "cup", "prep_note": ""},
            {"item": "flour", "quantity": "3/4", "unit": "cup", "prep_note": ""},
            {"item": "milk", "quantity": "1 1/4", "unit": "cups", "prep_note": ""},
            {"item": "salt", "quantity": "", "unit": "pinch", "prep_note": ""},
            {"item": "vanilla", "quantity": "1", "unit": "tbsp", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Beat milk, sugar, flour, salt, and vanilla until smooth."},
            {"step": 2, "text": "Pour half of the mixture into a buttered baking dish and bake one minute."},
            {"step": 3, "text": "Add the berries, then cover with the other half of the mix."},
            {"step": 4, "text": "Bake until set."}
        ],
        "temperature": "375°F (190°C)",
        "pan_size": "Buttered baking dish",
        "notes": [],
        "tags": ["flan", "serviceberry", "custard", "dessert", "appalachian", "foxfire"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": ["foxfire-three.txt"]
    },
    # === DEWBERRY RECIPES ===
    {
        "id": "foxfire3-dewberry-frosting",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Dewberry Frosting",
        "category": "desserts",
        "attribution": "Foxfire 3",
        "source_note": "Traditional Appalachian recipe from Foxfire 3",
        "description": "A bright frosting made from dewberry juice.",
        "servings_yield": "",
        "prep_time": "",
        "cook_time": "",
        "total_time": "",
        "ingredients": [
            {"item": "dewberry juice", "quantity": "1", "unit": "cup", "prep_note": "from cooked and strained berries"},
            {"item": "confectioners sugar", "quantity": "1", "unit": "cup", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Cook berries and strain."},
            {"step": 2, "text": "Use one cup juice to one cup confectioners sugar."},
            {"step": 3, "text": "Spread on cake."}
        ],
        "temperature": "",
        "pan_size": "",
        "notes": [],
        "tags": ["frosting", "dewberry", "cake", "dessert", "appalachian", "foxfire"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": ["foxfire-three.txt"]
    },
    {
        "id": "foxfire3-dewberry-pie",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Dewberry Pie",
        "category": "desserts",
        "attribution": "Foxfire 3",
        "source_note": "Traditional Appalachian recipe from Foxfire 3",
        "description": "A simple dewberry pie with a buttery top.",
        "servings_yield": "1 pie",
        "prep_time": "",
        "cook_time": "",
        "total_time": "",
        "ingredients": [
            {"item": "dewberries", "quantity": "", "unit": "to fill shell", "prep_note": ""},
            {"item": "sugar", "quantity": "1", "unit": "cup", "prep_note": ""},
            {"item": "flour", "quantity": "1/4", "unit": "cup", "prep_note": ""},
            {"item": "salt", "quantity": "", "unit": "dash", "prep_note": ""},
            {"item": "butter", "quantity": "", "unit": "for dotting", "prep_note": ""},
            {"item": "pastry shell", "quantity": "1", "unit": "", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Mix one cup sugar, 1/4 cup flour, and dash of salt."},
            {"step": 2, "text": "Fill a pastry shell with dewberries."},
            {"step": 3, "text": "Sprinkle the mixture of sugar, flour, and salt over the top."},
            {"step": 4, "text": "Dot with butter and bake."}
        ],
        "temperature": "375°F (190°C)",
        "pan_size": "Pie pan",
        "notes": [],
        "tags": ["pie", "dewberry", "dessert", "appalachian", "foxfire", "foraging"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": ["foxfire-three.txt"]
    },
    # === BLACKBERRY RECIPES ===
    {
        "id": "foxfire3-blackberry-cobbler",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Blackberry Cobbler (Foxfire 3)",
        "category": "desserts",
        "attribution": "Foxfire 3",
        "source_note": "Traditional Appalachian recipe from Foxfire 3",
        "description": "Classic mountain blackberry cobbler with biscuit topping.",
        "servings_yield": "",
        "prep_time": "",
        "cook_time": "",
        "total_time": "",
        "ingredients": [
            {"item": "blackberries", "quantity": "1", "unit": "pint", "prep_note": ""},
            {"item": "sugar", "quantity": "", "unit": "to taste", "prep_note": ""},
            {"item": "butter", "quantity": "", "unit": "small amount", "prep_note": ""},
            {"item": "biscuit dough", "quantity": "", "unit": "for several biscuits", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Cook the blackberries until they come to a boil."},
            {"step": 2, "text": "Add the sugar, then some butter, and cook until thick."},
            {"step": 3, "text": "Roll out the dough, cut as for biscuits, and drop into the blackberries."},
            {"step": 4, "text": "Roll some dough very thin, cut it into strips and place on top of the blackberries."},
            {"step": 5, "text": "Bake until the crust on top is brown."}
        ],
        "temperature": "400°F (205°C)",
        "pan_size": "Baking dish",
        "notes": ["Blackberries were sometimes dried on strips of chestnut bark and stored in sacks"],
        "tags": ["cobbler", "blackberry", "dessert", "appalachian", "foxfire", "foraging"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": ["foxfire-three.txt"]
    },
    {
        "id": "foxfire3-blackberry-syrup",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Blackberry Syrup",
        "category": "preserves",
        "attribution": "Foxfire 3",
        "source_note": "Traditional Appalachian recipe from Foxfire 3",
        "description": "A spiced blackberry syrup for pancakes.",
        "servings_yield": "",
        "prep_time": "",
        "cook_time": "15 minutes",
        "total_time": "",
        "ingredients": [
            {"item": "blackberry juice", "quantity": "1", "unit": "quart", "prep_note": ""},
            {"item": "sugar", "quantity": "1", "unit": "pint", "prep_note": ""},
            {"item": "allspice", "quantity": "1", "unit": "tsp", "prep_note": ""},
            {"item": "cinnamon", "quantity": "1", "unit": "tsp", "prep_note": ""},
            {"item": "cloves", "quantity": "1", "unit": "tsp", "prep_note": ""},
            {"item": "nutmeg", "quantity": "1", "unit": "tsp", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Mix all ingredients together."},
            {"step": 2, "text": "Boil for fifteen minutes."},
            {"step": 3, "text": "Use over pancakes."}
        ],
        "temperature": "",
        "pan_size": "",
        "notes": [],
        "tags": ["syrup", "blackberry", "pancakes", "preserves", "appalachian", "foxfire"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": ["foxfire-three.txt"]
    },
    {
        "id": "foxfire3-blackberry-flummery",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Blackberry Flummery",
        "category": "desserts",
        "attribution": "Foxfire 3",
        "source_note": "Traditional Appalachian recipe from Foxfire 3",
        "description": "A chilled blackberry pudding thickened with cornstarch.",
        "servings_yield": "",
        "prep_time": "",
        "cook_time": "",
        "total_time": "",
        "ingredients": [
            {"item": "blackberries", "quantity": "1", "unit": "quart", "prep_note": ""},
            {"item": "sugar", "quantity": "1 1/4", "unit": "cups", "prep_note": ""},
            {"item": "cinnamon", "quantity": "", "unit": "dash", "prep_note": ""},
            {"item": "hot water", "quantity": "1/2", "unit": "cup", "prep_note": ""},
            {"item": "salt", "quantity": "", "unit": "dash", "prep_note": ""},
            {"item": "cornstarch", "quantity": "2", "unit": "tbsp", "prep_note": ""},
            {"item": "cold water", "quantity": "3", "unit": "tbsp", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Mix berries with water, sugar, salt, and cinnamon, and cook to the boiling point."},
            {"step": 2, "text": "Reduce heat and cook slowly until liquid begins to look slightly syrupy."},
            {"step": 3, "text": "Make a paste of cornstarch and three tablespoons water."},
            {"step": 4, "text": "Stir into berry mixture, cook until slightly thick."},
            {"step": 5, "text": "Serve cold."}
        ],
        "temperature": "",
        "pan_size": "",
        "notes": [],
        "tags": ["flummery", "pudding", "blackberry", "dessert", "appalachian", "foxfire"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": ["foxfire-three.txt"]
    },
    {
        "id": "foxfire3-blackberry-roll",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Blackberry Roll",
        "category": "desserts",
        "attribution": "Foxfire 3",
        "source_note": "Traditional Appalachian recipe from Foxfire 3",
        "description": "A rolled pastry filled with blackberries and honey.",
        "servings_yield": "",
        "prep_time": "",
        "cook_time": "30 minutes",
        "total_time": "",
        "ingredients": [
            {"item": "biscuit dough", "quantity": "", "unit": "", "prep_note": ""},
            {"item": "blackberries", "quantity": "4", "unit": "cups", "prep_note": "divided"},
            {"item": "cinnamon", "quantity": "1/2", "unit": "tsp", "prep_note": ""},
            {"item": "butter or margarine", "quantity": "2", "unit": "tbsp", "prep_note": "melted"},
            {"item": "honey", "quantity": "1/2", "unit": "cup", "prep_note": ""},
            {"item": "sugar", "quantity": "1/2", "unit": "cup", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Roll dough to 1/3-inch thickness, and brush with melted butter."},
            {"step": 2, "text": "Combine 1/2 the berries with cinnamon and honey and spread them over dough."},
            {"step": 3, "text": "Roll as a jelly roll. Place in a large, well-greased pan."},
            {"step": 4, "text": "Surround with remaining blackberries and sugar."},
            {"step": 5, "text": "Bake at 425° for thirty minutes."},
            {"step": 6, "text": "Slice and serve from the pan."}
        ],
        "temperature": "425°F (220°C)",
        "pan_size": "Large greased pan",
        "notes": [],
        "tags": ["roll", "blackberry", "honey", "dessert", "appalachian", "foxfire"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": ["foxfire-three.txt"]
    },
    {
        "id": "foxfire3-blackberry-jelly",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Blackberry Jelly",
        "category": "preserves",
        "attribution": "Foxfire 3",
        "source_note": "Traditional Appalachian recipe from Foxfire 3",
        "description": "Simple blackberry jelly made without commercial pectin.",
        "servings_yield": "",
        "prep_time": "",
        "cook_time": "",
        "total_time": "",
        "ingredients": [
            {"item": "blackberries", "quantity": "1", "unit": "quart", "prep_note": "crushed"},
            {"item": "sugar", "quantity": "1 1/2", "unit": "cups", "prep_note": "per cup of juice"}
        ],
        "instructions": [
            {"step": 1, "text": "Crush one quart berries in a pan without sugar or water."},
            {"step": 2, "text": "Cook slowly eight minutes."},
            {"step": 3, "text": "Strain; measure; bring to boiling point."},
            {"step": 4, "text": "Add 1 1/2 cups sugar to each cup juice gradually, so the boiling does not stop."},
            {"step": 5, "text": "Bring to a brisk boil, skim, and bottle."}
        ],
        "temperature": "",
        "pan_size": "",
        "notes": ["No commercial pectin needed - natural pectin in berries"],
        "tags": ["jelly", "blackberry", "preserves", "canning", "appalachian", "foxfire"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": ["foxfire-three.txt"]
    },
    {
        "id": "foxfire3-blackberry-wine-jake-waldroop",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Jake Waldroop's Blackberry Wine",
        "category": "beverages",
        "attribution": "Foxfire 3 - Jake Waldroop",
        "source_note": "Traditional Appalachian recipe from Foxfire 3",
        "description": "Jake Waldroop's recipe for homemade blackberry wine, stored in an earthenware jug with a corn cob stopper.",
        "servings_yield": "",
        "prep_time": "",
        "cook_time": "",
        "total_time": "Several weeks fermentation",
        "ingredients": [
            {"item": "wild blackberries", "quantity": "6-8", "unit": "gallons", "prep_note": "washed"},
            {"item": "sugar", "quantity": "5", "unit": "lb", "prep_note": "plus more for second addition"}
        ],
        "instructions": [
            {"step": 1, "text": "Gather six to eight gallons of wild blackberries, wash them well, and put them in a big container."},
            {"step": 2, "text": "Mix in five pounds of sugar."},
            {"step": 3, "text": "Cover the top of the churn or container with a cloth, tied down so air can get in but insects can't."},
            {"step": 4, "text": "Let the mixture work for eight to ten days."},
            {"step": 5, "text": "Strain the mixture through a clean cloth, squeezing the pulp so that all the juice is removed."},
            {"step": 6, "text": "Measure the juice you have. For every gallon of juice, add one and a half pounds of sugar."},
            {"step": 7, "text": "Let it work off. When it stops (when the foaming and bubbling have stopped on top), strain it again."},
            {"step": 8, "text": "Measure the juice, and again add one and a half pounds of sugar to each gallon of juice."},
            {"step": 9, "text": "When it finishes working this time, it is done and can be bottled."}
        ],
        "temperature": "",
        "pan_size": "Large churn or container",
        "notes": [
            "Jake keeps his in an earthenware jug with a corn cob stopper",
            "Makes grape wine the same way"
        ],
        "tags": ["wine", "blackberry", "fermented", "beverage", "appalachian", "foxfire"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": ["foxfire-three.txt"]
    },
    {
        "id": "foxfire3-blackberry-cordial",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Blackberry Cordial",
        "category": "beverages",
        "attribution": "Foxfire 3",
        "source_note": "Traditional Appalachian recipe from Foxfire 3",
        "description": "A spiced blackberry cordial with whiskey.",
        "servings_yield": "",
        "prep_time": "",
        "cook_time": "15 minutes",
        "total_time": "",
        "ingredients": [
            {"item": "blackberries", "quantity": "", "unit": "", "prep_note": ""},
            {"item": "white sugar", "quantity": "1", "unit": "lb", "prep_note": "per pint of juice"},
            {"item": "mace", "quantity": "1/2", "unit": "oz", "prep_note": "whole, not ground"},
            {"item": "cloves", "quantity": "2", "unit": "tsp", "prep_note": "whole, not ground"},
            {"item": "whiskey", "quantity": "3/4", "unit": "cup", "prep_note": "per quart of juice"}
        ],
        "instructions": [
            {"step": 1, "text": "Boil the berries until they will break into pieces."},
            {"step": 2, "text": "Strain through a bag."},
            {"step": 3, "text": "To each pint of juice, add one pound of white sugar, a half ounce of mace, and two teaspoonfuls of cloves. Do not use ground spices."},
            {"step": 4, "text": "Boil for fifteen minutes."},
            {"step": 5, "text": "When cold, strain, and to each quart of juice add 3/4 cup of whiskey."},
            {"step": 6, "text": "Bottle and seal."}
        ],
        "temperature": "",
        "pan_size": "",
        "notes": ["Use whole spices, not ground"],
        "tags": ["cordial", "blackberry", "whiskey", "beverage", "appalachian", "foxfire"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": ["foxfire-three.txt"]
    },
    # === BLUEBERRY RECIPES ===
    {
        "id": "foxfire3-blueberry-cobbler",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Blueberry Cobbler",
        "category": "desserts",
        "attribution": "Foxfire 3",
        "source_note": "Traditional Appalachian recipe from Foxfire 3",
        "description": "Mountain blueberry cobbler with sweet biscuit topping.",
        "servings_yield": "",
        "prep_time": "",
        "cook_time": "",
        "total_time": "",
        "ingredients": [
            {"item": "blueberries", "quantity": "", "unit": "", "prep_note": ""},
            {"item": "sugar", "quantity": "1", "unit": "cup", "prep_note": ""},
            {"item": "flour", "quantity": "2", "unit": "cups", "prep_note": ""},
            {"item": "sugar", "quantity": "2", "unit": "tbsp", "prep_note": "for dough"},
            {"item": "shortening", "quantity": "2", "unit": "tbsp", "prep_note": ""},
            {"item": "salt", "quantity": "", "unit": "pinch", "prep_note": ""},
            {"item": "baking powder", "quantity": "2", "unit": "tsp", "prep_note": ""},
            {"item": "milk", "quantity": "", "unit": "enough to mix", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Cook berries for fifteen minutes over medium heat with one cup sugar."},
            {"step": 2, "text": "For dough, use two cups flour and two tablespoons each of sugar and shortening with a pinch of salt and two teaspoons baking powder. Add enough milk to mix."},
            {"step": 3, "text": "Drop dough by spoonfuls onto hot berries and bake until golden."}
        ],
        "temperature": "375°F (190°C)",
        "pan_size": "Baking dish",
        "notes": [],
        "tags": ["cobbler", "blueberry", "dessert", "appalachian", "foxfire", "foraging"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": ["foxfire-three.txt"]
    },
    {
        "id": "foxfire3-blueberry-crisp",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Blueberry Crisp",
        "category": "desserts",
        "attribution": "Foxfire 3",
        "source_note": "Traditional Appalachian recipe from Foxfire 3",
        "description": "A simple blueberry crisp with oat topping.",
        "servings_yield": "",
        "prep_time": "",
        "cook_time": "",
        "total_time": "",
        "ingredients": [
            {"item": "blueberries", "quantity": "4", "unit": "cups", "prep_note": ""},
            {"item": "sugar", "quantity": "1/3", "unit": "cup", "prep_note": ""},
            {"item": "butter", "quantity": "4", "unit": "tbsp", "prep_note": ""},
            {"item": "brown sugar", "quantity": "1/2", "unit": "cup", "prep_note": ""},
            {"item": "flour", "quantity": "1/3", "unit": "cup", "prep_note": ""},
            {"item": "quick oats", "quantity": "3/4", "unit": "cup", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Put berries in a greased baking dish and sprinkle with 1/3 cup sugar."},
            {"step": 2, "text": "For topping, cream butter and brown sugar."},
            {"step": 3, "text": "Blend in flour and oats with a fork."},
            {"step": 4, "text": "Spread over berries and bake."}
        ],
        "temperature": "375°F (190°C)",
        "pan_size": "Greased baking dish",
        "notes": [],
        "tags": ["crisp", "blueberry", "oats", "dessert", "appalachian", "foxfire"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": ["foxfire-three.txt"]
    },
    {
        "id": "foxfire3-blueberry-dessert",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Blueberry Dessert Rolls",
        "category": "desserts",
        "attribution": "Foxfire 3",
        "source_note": "Traditional Appalachian recipe from Foxfire 3",
        "description": "Rolled biscuit dough filled with blueberries, baked upside down.",
        "servings_yield": "",
        "prep_time": "",
        "cook_time": "",
        "total_time": "",
        "ingredients": [
            {"item": "blueberries", "quantity": "1", "unit": "quart", "prep_note": "cooked and drained"},
            {"item": "biscuit mix", "quantity": "2", "unit": "cups", "prep_note": ""},
            {"item": "milk", "quantity": "2/3", "unit": "cup", "prep_note": ""},
            {"item": "butter", "quantity": "2", "unit": "tbsp", "prep_note": "melted"},
            {"item": "sugar", "quantity": "2", "unit": "tbsp", "prep_note": ""},
            {"item": "cinnamon", "quantity": "1/4", "unit": "tsp", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Cook berries and drain thoroughly."},
            {"step": 2, "text": "Make dough from biscuit mix and milk."},
            {"step": 3, "text": "Roll out dough, brush with butter, and sprinkle with sugar and cinnamon."},
            {"step": 4, "text": "Cover with blueberries."},
            {"step": 5, "text": "Roll up like a jelly roll. Place seam side down in a greased baking dish."},
            {"step": 6, "text": "Bake in a hot oven (425°) about thirty minutes."}
        ],
        "temperature": "425°F (220°C)",
        "pan_size": "Greased baking dish",
        "notes": [],
        "tags": ["rolls", "blueberry", "dessert", "appalachian", "foxfire"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": ["foxfire-three.txt"]
    },
    # === SUMAC RECIPES ===
    {
        "id": "foxfire3-sumac-lemonade",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Sumac Lemonade",
        "category": "beverages",
        "attribution": "Foxfire 3",
        "source_note": "Traditional Appalachian recipe from Foxfire 3",
        "description": "A refreshing pink lemonade-like drink made from sumac berries. Said to relieve fatigue and reduce fever.",
        "servings_yield": "",
        "prep_time": "",
        "cook_time": "",
        "total_time": "",
        "ingredients": [
            {"item": "sumac berries", "quantity": "", "unit": "", "prep_note": "red, woolly type"},
            {"item": "boiling water", "quantity": "", "unit": "to cover", "prep_note": ""},
            {"item": "sugar or honey", "quantity": "", "unit": "to taste", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Crush sumac berries."},
            {"step": 2, "text": "Cover with boiling water."},
            {"step": 3, "text": "Steep until well colored."},
            {"step": 4, "text": "Strain through a cloth."},
            {"step": 5, "text": "Sweeten with sugar or honey and serve cold."}
        ],
        "temperature": "",
        "pan_size": "",
        "notes": [
            "Prepare and serve at once - will not keep",
            "Use red sumac (staghorn or smooth), NOT poison sumac which has white berries"
        ],
        "tags": ["lemonade", "sumac", "beverage", "foraging", "appalachian", "foxfire"],
        "confidence": {"overall": "high", "flags": ["Use only red sumac, never white-berried poison sumac"]},
        "image_refs": ["foxfire-three.txt"]
    },
    {
        "id": "foxfire3-sumac-elderberry-jelly",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Sumac and Elderberry Jelly",
        "category": "preserves",
        "attribution": "Foxfire 3",
        "source_note": "Traditional Appalachian recipe from Foxfire 3",
        "description": "A unique jelly combining tart sumac with sweet elderberries.",
        "servings_yield": "",
        "prep_time": "",
        "cook_time": "",
        "total_time": "",
        "ingredients": [
            {"item": "sumac berries", "quantity": "1", "unit": "pint", "prep_note": ""},
            {"item": "water", "quantity": "3", "unit": "pints", "prep_note": ""},
            {"item": "elderberries", "quantity": "1", "unit": "pint", "prep_note": ""},
            {"item": "sugar", "quantity": "1", "unit": "cup", "prep_note": "per cup juice"}
        ],
        "instructions": [
            {"step": 1, "text": "Boil one pint sumac berries in three pints water."},
            {"step": 2, "text": "Add one pint elderberries."},
            {"step": 3, "text": "Strain through cloth."},
            {"step": 4, "text": "Add one cup sugar for each cup juice and cook into jelly."}
        ],
        "temperature": "",
        "pan_size": "",
        "notes": [],
        "tags": ["jelly", "sumac", "elderberry", "preserves", "appalachian", "foxfire"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": ["foxfire-three.txt"]
    },
    # === GOOSEBERRY RECIPES ===
    {
        "id": "foxfire3-gooseberry-pie",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Gooseberry Pie",
        "category": "desserts",
        "attribution": "Foxfire 3",
        "source_note": "Traditional Appalachian recipe from Foxfire 3",
        "description": "A classic gooseberry pie with lattice top.",
        "servings_yield": "1 pie",
        "prep_time": "",
        "cook_time": "",
        "total_time": "",
        "ingredients": [
            {"item": "gooseberries", "quantity": "2", "unit": "cups", "prep_note": ""},
            {"item": "sugar", "quantity": "3/4", "unit": "cup", "prep_note": ""},
            {"item": "pie crust", "quantity": "", "unit": "bottom and lattice top", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Mix two cups berries with 3/4 cup sugar and cook until soft and clear."},
            {"step": 2, "text": "Pour into a pie shell."},
            {"step": 3, "text": "Lay strips of pie dough crosswise on the berries."},
            {"step": 4, "text": "Bake at about 450° until the crust is golden."}
        ],
        "temperature": "450°F (230°C)",
        "pan_size": "Pie pan",
        "notes": ["Wild gooseberries are prickly but very sweet inside"],
        "tags": ["pie", "gooseberry", "dessert", "appalachian", "foxfire", "foraging"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": ["foxfire-three.txt"]
    },
    # === ELDERBERRY RECIPES ===
    {
        "id": "foxfire3-elderberry-jelly",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Elderberry Jelly",
        "category": "preserves",
        "attribution": "Foxfire 3",
        "source_note": "Traditional Appalachian recipe from Foxfire 3",
        "description": "Classic elderberry jelly.",
        "servings_yield": "",
        "prep_time": "",
        "cook_time": "",
        "total_time": "",
        "ingredients": [
            {"item": "elderberries", "quantity": "", "unit": "", "prep_note": "ripe"},
            {"item": "water", "quantity": "", "unit": "small amount", "prep_note": ""},
            {"item": "sugar", "quantity": "1", "unit": "lb", "prep_note": "per pint juice"}
        ],
        "instructions": [
            {"step": 1, "text": "Cook elderberries with a small amount of water until thoroughly cooked."},
            {"step": 2, "text": "Strain, and to one pint juice, add one pound sugar."},
            {"step": 3, "text": "Cook until it jellies."}
        ],
        "temperature": "",
        "pan_size": "",
        "notes": [],
        "tags": ["jelly", "elderberry", "preserves", "appalachian", "foxfire", "foraging"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": ["foxfire-three.txt"]
    },
    {
        "id": "foxfire3-spiced-elderberries",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Spiced Elderberries",
        "category": "preserves",
        "attribution": "Foxfire 3",
        "source_note": "Traditional Appalachian recipe from Foxfire 3",
        "description": "Spiced preserved elderberries.",
        "servings_yield": "",
        "prep_time": "",
        "cook_time": "",
        "total_time": "",
        "ingredients": [
            {"item": "elderberries", "quantity": "", "unit": "", "prep_note": "washed"},
            {"item": "vinegar", "quantity": "", "unit": "to cover", "prep_note": ""},
            {"item": "cloves", "quantity": "1/2", "unit": "tsp", "prep_note": "per jar"},
            {"item": "allspice", "quantity": "1/2", "unit": "tsp", "prep_note": "per jar"},
            {"item": "sugar", "quantity": "1", "unit": "cup", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Wash elderberries and pack in self-sealing jars with a half teaspoon each of cloves and allspice."},
            {"step": 2, "text": "Cover with vinegar."},
            {"step": 3, "text": "Boil one cup of sugar and pour over the berries."},
            {"step": 4, "text": "Seal while hot."}
        ],
        "temperature": "",
        "pan_size": "Self-sealing jars",
        "notes": [],
        "tags": ["spiced", "elderberry", "preserves", "canning", "appalachian", "foxfire"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": ["foxfire-three.txt"]
    },
]


def main():
    # Load existing recipes
    with open(RECIPES_FILE, 'r') as f:
        data = json.load(f)

    # Get existing recipe IDs to avoid duplicates
    existing_ids = {r['id'] for r in data['recipes']}

    # Add new recipes
    added = 0
    for recipe in FOXFIRE3_RECIPES:
        if recipe['id'] not in existing_ids:
            data['recipes'].append(recipe)
            added += 1
            print(f"Added: {recipe['title']}")
        else:
            print(f"Skipped (exists): {recipe['title']}")

    # Update metadata
    data['meta']['total_recipes'] = len(data['recipes'])
    data['meta']['last_updated'] = "2026-01-17"

    # Save
    with open(RECIPES_FILE, 'w') as f:
        json.dump(data, f, indent=2)

    print(f"\nAdded {added} new recipes from Foxfire 3. Total: {len(data['recipes'])}")


if __name__ == "__main__":
    main()
