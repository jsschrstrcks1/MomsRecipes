#!/usr/bin/env python3
"""
Script to add Foxfire Vol 1 recipes to recipes.json
"""
import json
from pathlib import Path

DATA_DIR = Path(__file__).parent.parent / "data"
RECIPES_FILE = DATA_DIR / "recipes.json"

# Foxfire Vol 1 recipes extracted with love and care
FOXFIRE_RECIPES = [
    # === MOUNTAIN RECIPES: MAIN DISHES ===
    {
        "id": "foxfire-brunswick-stew",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Brunswick Stew",
        "category": "main dishes",
        "attribution": "Foxfire Vol 1",
        "source_note": "Traditional Appalachian mountain recipe from The Foxfire Book",
        "description": "A hearty mountain stew with multiple meats and vegetables, designed to feed many and preserve well.",
        "servings_yield": "Large batch, suitable for canning",
        "prep_time": "",
        "cook_time": "Long simmer",
        "total_time": "",
        "ingredients": [
            {"item": "cooked ground beef", "quantity": "2", "unit": "lb", "prep_note": ""},
            {"item": "cooked lean ground pork", "quantity": "1", "unit": "lb", "prep_note": ""},
            {"item": "cooked chicken", "quantity": "1", "unit": "small", "prep_note": "chopped"},
            {"item": "potatoes", "quantity": "3-4", "unit": "", "prep_note": "diced"},
            {"item": "kernel corn", "quantity": "1", "unit": "pint", "prep_note": ""},
            {"item": "lima beans", "quantity": "1", "unit": "cup", "prep_note": ""},
            {"item": "carrots", "quantity": "2-3", "unit": "", "prep_note": "diced"},
            {"item": "onions", "quantity": "2-3", "unit": "", "prep_note": "chopped"},
            {"item": "tomatoes or tomato juice", "quantity": "1", "unit": "pint", "prep_note": ""},
            {"item": "catsup", "quantity": "", "unit": "to taste", "prep_note": ""},
            {"item": "chile powder", "quantity": "", "unit": "to taste", "prep_note": ""},
            {"item": "salt", "quantity": "", "unit": "to taste", "prep_note": ""},
            {"item": "black pepper", "quantity": "", "unit": "to taste", "prep_note": ""},
            {"item": "red pepper", "quantity": "", "unit": "to taste", "prep_note": ""},
            {"item": "Worcestershire sauce", "quantity": "", "unit": "to taste", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "The vegetables may be either raw or canned."},
            {"step": 2, "text": "Mix everything together and simmer a long time."},
            {"step": 3, "text": "If you want to can it, put in jars and place them in a boiling water bath for 1/2 hour."}
        ],
        "temperature": "",
        "pan_size": "Large pot",
        "notes": [
            "Vegetables may be raw or canned",
            "Great for canning and preserving"
        ],
        "tags": ["stew", "appalachian", "foxfire", "canning", "main-dish"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": ["FoxfireVol1.txt.html"]
    },
    # === VEGETABLES ===
    {
        "id": "foxfire-leather-breeches-beans",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Leather Breeches Beans",
        "category": "sides",
        "attribution": "Foxfire Vol 1 - Andy Webb",
        "source_note": "Traditional Appalachian preserved beans from The Foxfire Book",
        "description": "Dried green beans cooked with meat - a mountain winter staple. As Andy Webb said, 'Now they's somethin' good ta'eat.'",
        "servings_yield": "",
        "prep_time": "",
        "cook_time": "All morning",
        "total_time": "",
        "ingredients": [
            {"item": "dried green beans (leather breeches)", "quantity": "1", "unit": "string", "prep_note": ""},
            {"item": "ham, pork, or similar meat", "quantity": "1", "unit": "good hunk", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Sometime during the winter take a string of dried green beans down, remove the thread."},
            {"step": 2, "text": "Drop them in a pot of scalding water."},
            {"step": 3, "text": "Add a good hunk of meat (ham, pork, or the like, depending on your taste)."},
            {"step": 4, "text": "Cook all morning."}
        ],
        "temperature": "",
        "pan_size": "Large pot",
        "notes": [
            "Andy Webb: 'I'd rather have them as t'have canned beans.'",
            "To dry beans: String tender green beans, push needle through center, hang in warm air (not direct sunlight) until dry, store in bag."
        ],
        "tags": ["beans", "appalachian", "foxfire", "preserved", "winter-food"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": ["FoxfireVol1.txt.html"]
    },
    {
        "id": "foxfire-cabbage",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Mountain Cabbage",
        "category": "sides",
        "attribution": "Foxfire Vol 1",
        "source_note": "Traditional Appalachian recipe from The Foxfire Book",
        "description": "Simple simmered cabbage with lard.",
        "servings_yield": "",
        "prep_time": "10 minutes",
        "cook_time": "25-30 minutes",
        "total_time": "",
        "ingredients": [
            {"item": "cabbage", "quantity": "1", "unit": "head", "prep_note": "chopped"},
            {"item": "lard", "quantity": "4", "unit": "tbsp", "prep_note": ""},
            {"item": "salt", "quantity": "", "unit": "to taste", "prep_note": ""},
            {"item": "pepper", "quantity": "", "unit": "to taste", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Put about an inch of water in a large frying pan and bring to a boil."},
            {"step": 2, "text": "Put all the cabbage and lard in, season, and cover."},
            {"step": 3, "text": "Simmer for about twenty-five to thirty minutes."}
        ],
        "temperature": "",
        "pan_size": "Large frying pan",
        "notes": [],
        "tags": ["cabbage", "appalachian", "foxfire", "vegetable", "simple"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": ["FoxfireVol1.txt.html"]
    },
    {
        "id": "foxfire-fried-potatoes",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Mountain Fried Potatoes",
        "category": "sides",
        "attribution": "Foxfire Vol 1",
        "source_note": "Traditional Appalachian recipe from The Foxfire Book",
        "description": "Thin-sliced potatoes fried until light brown.",
        "servings_yield": "",
        "prep_time": "",
        "cook_time": "",
        "total_time": "",
        "ingredients": [
            {"item": "potatoes", "quantity": "3-4", "unit": "", "prep_note": "sliced very thin, like potato chips"},
            {"item": "grease", "quantity": "", "unit": "for frying", "prep_note": "hot"},
            {"item": "salt", "quantity": "", "unit": "to taste", "prep_note": ""},
            {"item": "pepper", "quantity": "", "unit": "to taste", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Slice three or four potatoes very thin, like potato chips."},
            {"step": 2, "text": "Put in frying pan with hot grease and season with salt and pepper."},
            {"step": 3, "text": "Cover and cook until light brown, turning occasionally."}
        ],
        "temperature": "",
        "pan_size": "Frying pan",
        "notes": [],
        "tags": ["potatoes", "appalachian", "foxfire", "fried", "simple"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": ["FoxfireVol1.txt.html"]
    },
    {
        "id": "foxfire-fried-okra",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Fried Okra",
        "category": "sides",
        "attribution": "Foxfire Vol 1",
        "source_note": "Traditional Appalachian recipe from The Foxfire Book",
        "description": "Cornmeal-crusted fried okra.",
        "servings_yield": "",
        "prep_time": "",
        "cook_time": "",
        "total_time": "",
        "ingredients": [
            {"item": "okra", "quantity": "", "unit": "", "prep_note": "sliced 1/2 inch thick"},
            {"item": "cornmeal", "quantity": "", "unit": "for coating", "prep_note": ""},
            {"item": "salt", "quantity": "", "unit": "to taste", "prep_note": ""},
            {"item": "grease", "quantity": "", "unit": "for frying", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Slice the okra about 1/2 inch thick."},
            {"step": 2, "text": "Roll in meal and salt."},
            {"step": 3, "text": "Fry in grease until light brown and crispy."}
        ],
        "temperature": "",
        "pan_size": "Frying pan",
        "notes": [],
        "tags": ["okra", "appalachian", "foxfire", "fried", "vegetable"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": ["FoxfireVol1.txt.html"]
    },
    {
        "id": "foxfire-october-beans",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "October Beans",
        "category": "sides",
        "attribution": "Foxfire Vol 1",
        "source_note": "Traditional Appalachian recipe from The Foxfire Book",
        "description": "Mountain substitute for soup beans, which don't grow in the mountains.",
        "servings_yield": "",
        "prep_time": "",
        "cook_time": "",
        "total_time": "",
        "ingredients": [
            {"item": "October beans", "quantity": "", "unit": "", "prep_note": "dried and shelled"},
            {"item": "water", "quantity": "1", "unit": "quart", "prep_note": "per cup of beans"},
            {"item": "salt", "quantity": "", "unit": "to taste", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Parboil beans for five minutes, using about a quart of water per cup of beans and some salt."},
            {"step": 2, "text": "Cover and simmer until tender."}
        ],
        "temperature": "",
        "pan_size": "",
        "notes": [
            "Can be eaten fresh when young and tender",
            "Usually dried, shelled, and stored for later use"
        ],
        "tags": ["beans", "appalachian", "foxfire", "dried", "winter-food"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": ["FoxfireVol1.txt.html"]
    },
    {
        "id": "foxfire-fried-squash-blossoms",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Fried Pumpkin/Squash Blossoms",
        "category": "sides",
        "attribution": "Foxfire Vol 1",
        "source_note": "Traditional Appalachian recipe from The Foxfire Book",
        "description": "Battered and fried squash or pumpkin blossoms.",
        "servings_yield": "",
        "prep_time": "",
        "cook_time": "",
        "total_time": "",
        "ingredients": [
            {"item": "pumpkin or squash blossoms", "quantity": "", "unit": "", "prep_note": ""},
            {"item": "egg", "quantity": "1", "unit": "", "prep_note": ""},
            {"item": "flour", "quantity": "1/2", "unit": "cup", "prep_note": "about"},
            {"item": "milk", "quantity": "", "unit": "enough to make thin batter", "prep_note": ""},
            {"item": "grease", "quantity": "", "unit": "for deep frying", "prep_note": "hot"}
        ],
        "instructions": [
            {"step": 1, "text": "Make a thin batter using an egg, about half a cup of flour, and milk."},
            {"step": 2, "text": "Dip the blossoms in it."},
            {"step": 3, "text": "Fry in deep hot grease."},
            {"step": 4, "text": "Serve as you would any vegetable."}
        ],
        "temperature": "",
        "pan_size": "Deep fryer or deep pan",
        "notes": [],
        "tags": ["squash", "pumpkin", "blossoms", "appalachian", "foxfire", "fried"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": ["FoxfireVol1.txt.html"]
    },
    {
        "id": "foxfire-hominy",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Hominy",
        "category": "sides",
        "attribution": "Foxfire Vol 1 - Mrs. Algie Norton",
        "source_note": "Traditional Appalachian recipe from The Foxfire Book",
        "description": "Lye-processed corn made in a big washpot, as told by Mrs. Algie Norton.",
        "servings_yield": "",
        "prep_time": "",
        "cook_time": "16-18 hours total",
        "total_time": "",
        "ingredients": [
            {"item": "white corn", "quantity": "12-15", "unit": "ears", "prep_note": "big grain, shelled by hand"},
            {"item": "lye (dripped from ashes)", "quantity": "1", "unit": "gallon", "prep_note": ""},
            {"item": "water", "quantity": "10-15", "unit": "gallons", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Shell 12-15 big ears of corn by hand so you can get all the sorry grains out."},
            {"step": 2, "text": "Put lye in a big washpot (about 1/3 lye to 2/3 water)."},
            {"step": 3, "text": "Add corn and cook by the fireplace for about 8-9 hours."},
            {"step": 4, "text": "When grains begin to crack open, swell, and get tender, remove from fire."},
            {"step": 5, "text": "Wash in plenty of water (maybe a dozen waters), rubbing to get all the husk, hearts, and lye off."},
            {"step": 6, "text": "Put back in pot with fresh water and cook all night until good and tender."}
        ],
        "temperature": "",
        "pan_size": "10-15 gallon washpot",
        "notes": [
            "White corn makes the best - yellow corn wouldn't be as good",
            "Use big grain corn",
            "Keep in a cool place - will keep for a week in winter",
            "Can be canned but traditionally kept fresh in cold weather",
            "Mrs. Norton: 'Then y'had some good eatin'.'"
        ],
        "tags": ["corn", "hominy", "appalachian", "foxfire", "lye", "traditional"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": ["FoxfireVol1.txt.html"]
    },
    # === BREADS ===
    {
        "id": "foxfire-corn-pones",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Corn Pones",
        "category": "breads",
        "attribution": "Foxfire Vol 1",
        "source_note": "Traditional Appalachian recipe from The Foxfire Book",
        "description": "Simple cornmeal pones baked in a hot oven.",
        "servings_yield": "",
        "prep_time": "10 minutes",
        "cook_time": "30 minutes",
        "total_time": "",
        "ingredients": [
            {"item": "corn meal", "quantity": "1", "unit": "pint", "prep_note": ""},
            {"item": "salt", "quantity": "1/2", "unit": "tsp", "prep_note": ""},
            {"item": "baking powder", "quantity": "1", "unit": "tsp", "prep_note": ""},
            {"item": "lard", "quantity": "1", "unit": "tbsp", "prep_note": ""},
            {"item": "milk", "quantity": "", "unit": "enough for stiff batter", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Mix together meal, powder, and salt, cut in lard."},
            {"step": 2, "text": "Add enough milk to make a stiff batter."},
            {"step": 3, "text": "Form into pones with hands (or add some milk and drop from the end of a spoon)."},
            {"step": 4, "text": "Place in a greased pan and bake in a hot oven for about half an hour."}
        ],
        "temperature": "400-425°F (205-220°C)",
        "pan_size": "Greased baking pan",
        "notes": [],
        "tags": ["cornbread", "appalachian", "foxfire", "bread"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": ["FoxfireVol1.txt.html"]
    },
    {
        "id": "foxfire-corn-cakes",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Corn Cakes",
        "category": "breads",
        "attribution": "Foxfire Vol 1",
        "source_note": "Traditional Appalachian recipe from The Foxfire Book",
        "description": "Griddle cakes made with cornmeal - good with butter and syrup.",
        "servings_yield": "",
        "prep_time": "",
        "cook_time": "",
        "total_time": "",
        "ingredients": [
            {"item": "corn meal", "quantity": "2", "unit": "cups", "prep_note": ""},
            {"item": "flour", "quantity": "1", "unit": "kitchen spoon", "prep_note": ""},
            {"item": "eggs", "quantity": "2", "unit": "", "prep_note": ""},
            {"item": "salt", "quantity": "1", "unit": "tsp", "prep_note": ""},
            {"item": "baking powder", "quantity": "2", "unit": "tsp", "prep_note": ""},
            {"item": "melted butter or lard", "quantity": "1", "unit": "tbsp", "prep_note": ""},
            {"item": "milk", "quantity": "", "unit": "enough for thin batter", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Beat eggs."},
            {"step": 2, "text": "Add meal, flour, salt, baking powder, and butter."},
            {"step": 3, "text": "Add enough milk to make a thin batter."},
            {"step": 4, "text": "Pour out onto a hot griddle."},
            {"step": 5, "text": "Flip to other side when brown."}
        ],
        "temperature": "",
        "pan_size": "Hot griddle",
        "notes": ["Good with butter and syrup"],
        "tags": ["cornmeal", "appalachian", "foxfire", "griddle-cakes", "breakfast"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": ["FoxfireVol1.txt.html"]
    },
    {
        "id": "foxfire-hush-puppies",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Hush Puppies",
        "category": "breads",
        "attribution": "Foxfire Vol 1",
        "source_note": "Traditional Appalachian recipe from The Foxfire Book",
        "description": "Deep fried cornmeal balls with onion.",
        "servings_yield": "",
        "prep_time": "",
        "cook_time": "",
        "total_time": "",
        "ingredients": [
            {"item": "flour", "quantity": "1", "unit": "cup", "prep_note": ""},
            {"item": "corn meal", "quantity": "1", "unit": "cup", "prep_note": ""},
            {"item": "salt", "quantity": "1", "unit": "pinch", "prep_note": ""},
            {"item": "soda", "quantity": "1", "unit": "pinch", "prep_note": ""},
            {"item": "egg", "quantity": "1", "unit": "", "prep_note": ""},
            {"item": "buttermilk", "quantity": "", "unit": "enough for right consistency", "prep_note": ""},
            {"item": "onion", "quantity": "1", "unit": "medium", "prep_note": "chopped"},
            {"item": "fat", "quantity": "", "unit": "for deep frying", "prep_note": "hot"}
        ],
        "instructions": [
            {"step": 1, "text": "Mix flour, corn meal, and a pinch of salt and soda."},
            {"step": 2, "text": "Add egg and buttermilk until it is the right consistency to hold its shape when rolled into a ball."},
            {"step": 3, "text": "Mix in chopped onion."},
            {"step": 4, "text": "Roll into balls about 1-2 inches across."},
            {"step": 5, "text": "Drop into a couple inches of hot fat."},
            {"step": 6, "text": "Let them deep fry until they're brown and crispy."},
            {"step": 7, "text": "Drain a bit on some paper and serve hot."}
        ],
        "temperature": "",
        "pan_size": "Deep fryer or deep pan",
        "notes": [],
        "tags": ["hush-puppies", "cornmeal", "appalachian", "foxfire", "fried"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": ["FoxfireVol1.txt.html"]
    },
    {
        "id": "foxfire-light-bread",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Light Bread",
        "category": "breads",
        "attribution": "Foxfire Vol 1",
        "source_note": "Traditional Appalachian yeast bread from The Foxfire Book",
        "description": "Traditional mountain yeast bread made with potatoes.",
        "servings_yield": "",
        "prep_time": "",
        "cook_time": "",
        "total_time": "",
        "ingredients": [
            {"item": "yeast", "quantity": "1", "unit": "cake", "prep_note": ""},
            {"item": "sugar", "quantity": "3", "unit": "tsp", "prep_note": ""},
            {"item": "warm water", "quantity": "1", "unit": "pint", "prep_note": ""},
            {"item": "potatoes", "quantity": "2", "unit": "medium", "prep_note": "cooked and mashed very fine"},
            {"item": "salt", "quantity": "2", "unit": "tsp", "prep_note": ""},
            {"item": "flour", "quantity": "", "unit": "enough for firm dough", "prep_note": "sifted"}
        ],
        "instructions": [
            {"step": 1, "text": "Dissolve the yeast in 1 cup of the water."},
            {"step": 2, "text": "Cook the potatoes, mash very fine, and add yeast along with 1 tsp salt, 1 tsp sugar, and the rest of the water."},
            {"step": 3, "text": "Put in a jar and leave in a warm place to rise."},
            {"step": 4, "text": "Sift flour, and mix it in with the yeast mixture along with 1 more tsp salt and 2 more tsp sugar."},
            {"step": 5, "text": "Keep adding flour until it makes a firm dough."},
            {"step": 6, "text": "Let rise to double, knead, and make into loaves."},
            {"step": 7, "text": "Let rise for one hour, and then bake at about 350°F until it tests done."}
        ],
        "temperature": "350°F (175°C)",
        "pan_size": "Loaf pans",
        "notes": [],
        "tags": ["yeast-bread", "appalachian", "foxfire", "bread"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": ["FoxfireVol1.txt.html"]
    },
    {
        "id": "foxfire-cracklin-bread",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Cracklin' Bread",
        "category": "breads",
        "attribution": "Foxfire Vol 1",
        "source_note": "Traditional Appalachian recipe from The Foxfire Book",
        "description": "Cornbread made with cracklin's (crispy bits left from rendering lard).",
        "servings_yield": "",
        "prep_time": "",
        "cook_time": "",
        "total_time": "",
        "ingredients": [
            {"item": "corn meal", "quantity": "2", "unit": "cups", "prep_note": ""},
            {"item": "salt", "quantity": "2", "unit": "tsp", "prep_note": ""},
            {"item": "buttermilk", "quantity": "1", "unit": "cup", "prep_note": ""},
            {"item": "soda", "quantity": "1", "unit": "tsp", "prep_note": ""},
            {"item": "baking powder", "quantity": "1/4", "unit": "tsp", "prep_note": ""},
            {"item": "cracklin's", "quantity": "1/2", "unit": "cup", "prep_note": ""},
            {"item": "lukewarm water", "quantity": "", "unit": "if needed", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Mix corn meal, salt, buttermilk, soda, and baking powder."},
            {"step": 2, "text": "Mix in 1/2 cup of cracklin's."},
            {"step": 3, "text": "If it is too dry use some lukewarm water to make the right consistency for corn bread."},
            {"step": 4, "text": "Put in oven and cook until brown."}
        ],
        "temperature": "400°F (205°C)",
        "pan_size": "",
        "notes": ["Cracklin's are the crispy bits left after rendering lard from hog fat"],
        "tags": ["cornbread", "cracklins", "appalachian", "foxfire", "bread"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": ["FoxfireVol1.txt.html"]
    },
    {
        "id": "foxfire-old-fashioned-gingerbread",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Old-Fashioned Gingerbread",
        "category": "desserts",
        "attribution": "Foxfire Vol 1",
        "source_note": "Traditional Appalachian recipe from The Foxfire Book - at least 100 years old",
        "description": "A century-old gingerbread recipe from the Appalachian mountains.",
        "servings_yield": "",
        "prep_time": "",
        "cook_time": "About 1 hour",
        "total_time": "",
        "ingredients": [
            {"item": "sugar", "quantity": "1/2", "unit": "cup", "prep_note": ""},
            {"item": "butter", "quantity": "1/2", "unit": "cup", "prep_note": ""},
            {"item": "molasses", "quantity": "1", "unit": "cup", "prep_note": ""},
            {"item": "flour", "quantity": "2", "unit": "cups", "prep_note": ""},
            {"item": "soda", "quantity": "1/2", "unit": "tsp", "prep_note": ""},
            {"item": "ginger", "quantity": "1 1/2", "unit": "tsp", "prep_note": ""},
            {"item": "cinnamon", "quantity": "1/2", "unit": "tsp", "prep_note": ""},
            {"item": "sour milk", "quantity": "1/2", "unit": "cup", "prep_note": ""},
            {"item": "nuts or raisins", "quantity": "", "unit": "if desired", "prep_note": "optional"}
        ],
        "instructions": [
            {"step": 1, "text": "Mix all ingredients together."},
            {"step": 2, "text": "Pour into a large loaf pan."},
            {"step": 3, "text": "Bake for about an hour."}
        ],
        "temperature": "325°F (165°C)",
        "pan_size": "Large loaf pan",
        "notes": ["This recipe is at least a hundred years old."],
        "tags": ["gingerbread", "appalachian", "foxfire", "dessert", "molasses", "heritage"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": ["FoxfireVol1.txt.html"]
    },
    {
        "id": "foxfire-pumpkin-cake",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Pumpkin Cake",
        "category": "desserts",
        "attribution": "Foxfire Vol 1",
        "source_note": "Traditional Appalachian recipe from The Foxfire Book",
        "description": "A moist pumpkin cake with nuts and raisins.",
        "servings_yield": "",
        "prep_time": "",
        "cook_time": "About 1 hour",
        "total_time": "",
        "ingredients": [
            {"item": "corn oil", "quantity": "1 1/2", "unit": "cups", "prep_note": ""},
            {"item": "sugar", "quantity": "2", "unit": "cups", "prep_note": ""},
            {"item": "flour", "quantity": "3", "unit": "cups", "prep_note": ""},
            {"item": "baking powder", "quantity": "2", "unit": "tsp", "prep_note": ""},
            {"item": "soda", "quantity": "2", "unit": "tsp", "prep_note": "scant"},
            {"item": "salt", "quantity": "1", "unit": "tsp", "prep_note": ""},
            {"item": "pumpkin spice", "quantity": "2", "unit": "tsp", "prep_note": ""},
            {"item": "vanilla", "quantity": "2", "unit": "tsp", "prep_note": ""},
            {"item": "eggs", "quantity": "4", "unit": "", "prep_note": "beaten well"},
            {"item": "pumpkin", "quantity": "2", "unit": "cups", "prep_note": ""},
            {"item": "raisins or fruit cake mix", "quantity": "1", "unit": "cup", "prep_note": ""},
            {"item": "chopped nuts", "quantity": "1", "unit": "cup", "prep_note": ""},
            {"item": "flour", "quantity": "1/2", "unit": "cup", "prep_note": "extra, for coating fruit/nuts"}
        ],
        "instructions": [
            {"step": 1, "text": "Mix corn oil, sugar, flour, spice, powder, soda, salt, and pumpkin."},
            {"step": 2, "text": "Add eggs beaten well."},
            {"step": 3, "text": "Add vanilla, nuts, and raisins that have been mixed with 1/2 cup of extra flour."},
            {"step": 4, "text": "Bake in a loaf pan for about an hour at 400-450°F."}
        ],
        "temperature": "400-450°F (205-230°C)",
        "pan_size": "Loaf pan",
        "notes": [],
        "tags": ["pumpkin", "cake", "appalachian", "foxfire", "dessert"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": ["FoxfireVol1.txt.html"]
    },
    {
        "id": "foxfire-sweet-potato-pie",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Sweet Potato Pie",
        "category": "desserts",
        "attribution": "Foxfire Vol 1",
        "source_note": "Traditional Appalachian recipe from The Foxfire Book",
        "description": "A rustic sweet potato pie with molasses and biscuit dough crust.",
        "servings_yield": "",
        "prep_time": "",
        "cook_time": "",
        "total_time": "",
        "ingredients": [
            {"item": "sweet potatoes", "quantity": "2", "unit": "cups", "prep_note": "diced and cooked"},
            {"item": "molasses", "quantity": "2/3", "unit": "cup", "prep_note": ""},
            {"item": "ginger", "quantity": "1/2", "unit": "tsp", "prep_note": ""},
            {"item": "butter", "quantity": "1/2", "unit": "stick", "prep_note": ""},
            {"item": "sweet milk", "quantity": "1/2", "unit": "cup", "prep_note": ""},
            {"item": "salt", "quantity": "1", "unit": "pinch", "prep_note": ""},
            {"item": "biscuit dough", "quantity": "", "unit": "enough for crust and topping", "prep_note": ""},
            {"item": "other spices", "quantity": "", "unit": "if desired", "prep_note": "optional"}
        ],
        "instructions": [
            {"step": 1, "text": "Mix together all the ingredients except the dough and bring to a boil."},
            {"step": 2, "text": "Cut rolled dough into cubes and drop into boiling mixture."},
            {"step": 3, "text": "Put thin slices of dough on top."},
            {"step": 4, "text": "Put pan in oven and bake until crust is brown."}
        ],
        "temperature": "375°F (190°C)",
        "pan_size": "Pie pan",
        "notes": [],
        "tags": ["sweet-potato", "pie", "appalachian", "foxfire", "dessert", "molasses"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": ["FoxfireVol1.txt.html"]
    },
    {
        "id": "foxfire-blackberry-cobbler",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Blackberry Cobbler",
        "category": "desserts",
        "attribution": "Foxfire Vol 1",
        "source_note": "Traditional Appalachian recipe from The Foxfire Book",
        "description": "Simple blackberry cobbler with biscuit crust.",
        "servings_yield": "1 pie",
        "prep_time": "",
        "cook_time": "",
        "total_time": "",
        "ingredients": [
            {"item": "blackberries", "quantity": "", "unit": "enough for one pie", "prep_note": ""},
            {"item": "sugar", "quantity": "", "unit": "to taste", "prep_note": ""},
            {"item": "butter", "quantity": "", "unit": "small amount", "prep_note": ""},
            {"item": "biscuit dough", "quantity": "", "unit": "enough for several biscuits", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Cook the blackberries until they come to a boil."},
            {"step": 2, "text": "Add as much or little sugar as you want, and then add some butter."},
            {"step": 3, "text": "Cook until thick."},
            {"step": 4, "text": "Roll out the dough, cut as for biscuits, and drop into the blackberries."},
            {"step": 5, "text": "Then roll some dough thin, cut into strips, and place on top of the blackberries."},
            {"step": 6, "text": "Set the pan in the oven until the crust on top is brown."}
        ],
        "temperature": "400°F (205°C)",
        "pan_size": "Pie pan or baking dish",
        "notes": [],
        "tags": ["blackberry", "cobbler", "appalachian", "foxfire", "dessert"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": ["FoxfireVol1.txt.html"]
    },
    {
        "id": "foxfire-molasses-candy",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Molasses Candy",
        "category": "desserts",
        "attribution": "Foxfire Vol 1",
        "source_note": "Traditional Appalachian recipe from The Foxfire Book",
        "description": "Old-fashioned pulled molasses candy.",
        "servings_yield": "",
        "prep_time": "",
        "cook_time": "",
        "total_time": "",
        "ingredients": [
            {"item": "molasses", "quantity": "1", "unit": "cup", "prep_note": ""},
            {"item": "water", "quantity": "1", "unit": "cup", "prep_note": ""},
            {"item": "salt", "quantity": "", "unit": "a few grains", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Combine molasses, water, and a few grains of salt."},
            {"step": 2, "text": "Boil ingredients (do not stir) to hard ball stage."},
            {"step": 3, "text": "Remove from the fire, and let stand until cool enough to hold in well greased hands."},
            {"step": 4, "text": "After pulling for some time it will change from brown to a yellowish color."},
            {"step": 5, "text": "Cut into pieces."}
        ],
        "temperature": "",
        "pan_size": "",
        "notes": ["Do not stir while boiling", "Grease hands well before pulling"],
        "tags": ["candy", "molasses", "appalachian", "foxfire", "dessert", "pulled-candy"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": ["FoxfireVol1.txt.html"]
    },
    {
        "id": "foxfire-apple-butter",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Apple Butter",
        "category": "preserves",
        "attribution": "Foxfire Vol 1",
        "source_note": "Traditional Appalachian recipe from The Foxfire Book",
        "description": "Traditional slow-cooked apple butter.",
        "servings_yield": "",
        "prep_time": "",
        "cook_time": "",
        "total_time": "",
        "ingredients": [
            {"item": "apples", "quantity": "", "unit": "", "prep_note": "peeled and sliced"},
            {"item": "sugar", "quantity": "1", "unit": "cup", "prep_note": "per cup of cooked apples"},
            {"item": "cinnamon", "quantity": "", "unit": "to taste", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Peel and slice apples, and immediately place them in a pan of cold, salty water so they won't turn brown."},
            {"step": 2, "text": "Rinse the salt out and cook the apples until soft and mushy."},
            {"step": 3, "text": "Add one cup of sugar to every cup of cooked apples."},
            {"step": 4, "text": "Add cinnamon to taste."},
            {"step": 5, "text": "Cook until thick."},
            {"step": 6, "text": "Put in jars and seal."}
        ],
        "temperature": "",
        "pan_size": "Large pot",
        "notes": ["Soak sliced apples in cold salty water to prevent browning"],
        "tags": ["apple-butter", "preserves", "appalachian", "foxfire", "canning"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": ["FoxfireVol1.txt.html"]
    },
    {
        "id": "foxfire-sauerkraut",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Sour Kraut",
        "category": "preserves",
        "attribution": "Foxfire Vol 1 - Daisy Justice",
        "source_note": "Traditional Appalachian recipe from The Foxfire Book",
        "description": "Traditional fermented sauerkraut. Daisy Justice says, 'When the moon is new is the best time to make kraut.'",
        "servings_yield": "",
        "prep_time": "",
        "cook_time": "",
        "total_time": "10 days fermentation",
        "ingredients": [
            {"item": "cabbage", "quantity": "", "unit": "firm heads", "prep_note": "chopped"},
            {"item": "salt", "quantity": "1/2", "unit": "cup", "prep_note": "per gallon of cabbage, not iodized"},
            {"item": "hot pepper", "quantity": "1", "unit": "pod", "prep_note": "optional, for flavor"}
        ],
        "instructions": [
            {"step": 1, "text": "Select firm cabbage heads and chop."},
            {"step": 2, "text": "Have a clean churn jar (usually five gallon), and pack the jar with alternating layers of chopped cabbage and a sprinkling of salt (usually a half cup of salt per gallon of cabbage)."},
            {"step": 3, "text": "You need not add water as the cabbage will produce its own."},
            {"step": 4, "text": "Cover the cabbage with a clean white cloth, large cabbage leaves, or a saucer."},
            {"step": 5, "text": "Place a flat flint rock or other weight on top to hold the cabbage under the brine."},
            {"step": 6, "text": "Let stand ten days, or as long as necessary to get it as sour as you want."},
            {"step": 7, "text": "Take the kraut out and pack it in canning jars."},
            {"step": 8, "text": "Put the jars in a pot of water and bring to a boil to seal the jars and cook the cabbage."}
        ],
        "temperature": "",
        "pan_size": "5 gallon churn jar",
        "notes": [
            "Daisy Justice: 'Be sure that the signs are not in the bowels. When the moon is new is the best time to make kraut.'",
            "Do not use iodized salt for pickling",
            "If signs are in the bowels, kraut will be slimy or soft and not fit to eat",
            "Some add a pod of hot pepper at the beginning for additional flavor",
            "Old-timers left cabbage in churn jars but it turns dark; jars keep it fresh"
        ],
        "tags": ["sauerkraut", "fermented", "preserves", "appalachian", "foxfire", "canning"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": ["FoxfireVol1.txt.html"]
    },
    {
        "id": "foxfire-chow-chow",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Chow Chow",
        "category": "preserves",
        "attribution": "Foxfire Vol 1",
        "source_note": "Traditional Appalachian recipe from The Foxfire Book",
        "description": "Traditional Appalachian mixed vegetable relish.",
        "servings_yield": "Large batch",
        "prep_time": "",
        "cook_time": "3 hours",
        "total_time": "",
        "ingredients": [
            {"item": "green tomatoes", "quantity": "1", "unit": "peck", "prep_note": "chopped"},
            {"item": "string beans", "quantity": "1", "unit": "peck", "prep_note": ""},
            {"item": "small white onions", "quantity": "1/4", "unit": "peck", "prep_note": "chopped"},
            {"item": "green peppers", "quantity": "1/4", "unit": "peck", "prep_note": "chopped"},
            {"item": "cabbage", "quantity": "2", "unit": "large heads", "prep_note": "chopped"},
            {"item": "red peppers", "quantity": "1/4", "unit": "peck", "prep_note": "chopped"},
            {"item": "white or black cloves", "quantity": "2", "unit": "oz", "prep_note": ""},
            {"item": "celery seeds", "quantity": "2", "unit": "oz", "prep_note": ""},
            {"item": "allspice", "quantity": "2", "unit": "oz", "prep_note": ""},
            {"item": "brown sugar", "quantity": "1", "unit": "lb", "prep_note": ""},
            {"item": "yellow mustard seed", "quantity": "1", "unit": "box", "prep_note": ""},
            {"item": "white mustard seed", "quantity": "4", "unit": "tbsp", "prep_note": ""},
            {"item": "tumeric", "quantity": "1", "unit": "oz", "prep_note": ""},
            {"item": "vinegar", "quantity": "", "unit": "to cover", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Chop the tomatoes, let them stand overnight in their own juice."},
            {"step": 2, "text": "Squeeze out the brine."},
            {"step": 3, "text": "Chop the cabbage, peppers, onions, and beans."},
            {"step": 4, "text": "Mix together and add the tomatoes and the spices and sugar."},
            {"step": 5, "text": "Put in a porcelain kettle, cover with vinegar, and boil three hours."},
            {"step": 6, "text": "When cool, seal in jars."}
        ],
        "temperature": "",
        "pan_size": "Porcelain kettle",
        "notes": [],
        "tags": ["chow-chow", "relish", "preserves", "appalachian", "foxfire", "canning"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": ["FoxfireVol1.txt.html"]
    }
]

def main():
    # Load existing recipes
    with open(RECIPES_FILE, 'r') as f:
        data = json.load(f)

    # Get existing recipe IDs to avoid duplicates
    existing_ids = {r['id'] for r in data['recipes']}

    # Add new recipes
    added = 0
    for recipe in FOXFIRE_RECIPES:
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

    print(f"\nAdded {added} new recipes. Total: {len(data['recipes'])}")

if __name__ == "__main__":
    main()
