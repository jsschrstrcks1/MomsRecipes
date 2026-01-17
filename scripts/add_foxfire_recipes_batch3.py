#!/usr/bin/env python3
"""
Script to add Foxfire Vol 1 recipes - Batch 3 (Wild Game and remaining recipes)
"""
import json
from pathlib import Path

DATA_DIR = Path(__file__).parent.parent / "data"
RECIPES_FILE = DATA_DIR / "recipes.json"

FOXFIRE_RECIPES_BATCH3 = [
    # === WILD GAME ===
    {
        "id": "foxfire-fried-squirrel",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Fried Squirrel",
        "category": "main dishes",
        "attribution": "Foxfire Vol 1",
        "source_note": "Traditional Appalachian wild game recipe from The Foxfire Book",
        "description": "Pan-fried squirrel - a mountain hunting tradition.",
        "servings_yield": "",
        "prep_time": "",
        "cook_time": "",
        "total_time": "",
        "ingredients": [
            {"item": "squirrel", "quantity": "1", "unit": "", "prep_note": "skinned, gutted, soaked to remove blood"},
            {"item": "flour", "quantity": "", "unit": "for coating", "prep_note": ""},
            {"item": "salt", "quantity": "", "unit": "to taste", "prep_note": ""},
            {"item": "pepper", "quantity": "", "unit": "to taste", "prep_note": ""},
            {"item": "grease or lard", "quantity": "", "unit": "for frying", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Soak the squirrel long enough to get all the blood out."},
            {"step": 2, "text": "Cut into pieces."},
            {"step": 3, "text": "Roll the pieces in flour, salt, and pepper."},
            {"step": 4, "text": "Fry until tender and brown."}
        ],
        "temperature": "",
        "pan_size": "Frying pan",
        "notes": [
            "If the squirrel is old, you may want to parboil it in water containing sage to take out the wild taste",
            "Can also make squirrel dumplings: parboil 5 min, cook in fresh water until tender, add pepper, butter, milk to broth, drop in dumpling dough and cook 10 min covered"
        ],
        "tags": ["squirrel", "wild-game", "fried", "appalachian", "foxfire", "hunting"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": ["FoxfireVol1.txt.html"]
    },
    {
        "id": "foxfire-rabbit",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Fried or Baked Rabbit",
        "category": "main dishes",
        "attribution": "Foxfire Vol 1",
        "source_note": "Traditional Appalachian wild game recipe from The Foxfire Book",
        "description": "Mountain-style rabbit prepared by frying or baking.",
        "servings_yield": "",
        "prep_time": "",
        "cook_time": "30 minutes baking",
        "total_time": "",
        "ingredients": [
            {"item": "rabbit", "quantity": "1", "unit": "", "prep_note": "skinned and cut into sections"},
            {"item": "salt", "quantity": "2", "unit": "tbsp", "prep_note": "for parboiling"},
            {"item": "flour or meal", "quantity": "", "unit": "for coating", "prep_note": ""},
            {"item": "pepper", "quantity": "1/2", "unit": "tsp", "prep_note": ""},
            {"item": "grease", "quantity": "", "unit": "for frying", "prep_note": ""},
            {"item": "eggs", "quantity": "2", "unit": "", "prep_note": "for batter, if baking"},
            {"item": "flour", "quantity": "4", "unit": "tbsp", "prep_note": "for batter"},
            {"item": "milk", "quantity": "1/4", "unit": "cup", "prep_note": "for batter"}
        ],
        "instructions": [
            {"step": 1, "text": "Cut the rabbit into sections. Remove the legs, and separate the ribs and back section by cutting up the rabbit's sides vertically."},
            {"step": 2, "text": "Parboil the pieces in covered pot in salted (two tablespoons) water to make tender if not young."},
            {"step": 3, "text": "For frying: put the parboiled pieces in a greased pan and fry until brown on all sides, seasoning with half teaspoon pepper. Some roll pieces in meal or flour before frying."},
            {"step": 4, "text": "For baking: dip parboiled pieces in a breaded solution of two eggs, four tablespoons flour, quarter cup milk, and half teaspoon pepper. Bake until brown (about thirty minutes)."}
        ],
        "temperature": "350°F (175°C)",
        "pan_size": "",
        "notes": ["Can also be simmered in salted water until tender and served as is"],
        "tags": ["rabbit", "wild-game", "fried", "baked", "appalachian", "foxfire", "hunting"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": ["FoxfireVol1.txt.html"]
    },
    {
        "id": "foxfire-possum-and-sweet-potatoes",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Possum and Sweet Potatoes",
        "category": "main dishes",
        "attribution": "Foxfire Vol 1 - Beulah Perry",
        "source_note": "Traditional Appalachian wild game recipe from The Foxfire Book",
        "description": "Classic mountain possum baked with sweet potatoes. Beulah Perry loved the possum head as a child.",
        "servings_yield": "",
        "prep_time": "Overnight soaking",
        "cook_time": "About 2 hours",
        "total_time": "",
        "ingredients": [
            {"item": "possum", "quantity": "1", "unit": "", "prep_note": "scalded, scraped, gutted, musk glands removed"},
            {"item": "lime or ashes", "quantity": "1/2", "unit": "cup", "prep_note": "for scalding water"},
            {"item": "salt", "quantity": "", "unit": "to taste", "prep_note": ""},
            {"item": "red or black pepper", "quantity": "", "unit": "to taste", "prep_note": ""},
            {"item": "sweet potatoes", "quantity": "", "unit": "", "prep_note": ""},
            {"item": "grease", "quantity": "", "unit": "for pan", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Scald the possum in boiling water containing a half cup of lime or ashes."},
            {"step": 2, "text": "Scrape until hairless, gut (should have been bled immediately after caught)."},
            {"step": 3, "text": "Remove the musk glands under the forearms, and either the head or at least the eyes."},
            {"step": 4, "text": "Soak overnight before cooking."},
            {"step": 5, "text": "Parboil in water containing salt and red or black pepper to taste until tender."},
            {"step": 6, "text": "Put in a greased pan surrounded or filled with sweet potatoes."},
            {"step": 7, "text": "Bake until golden brown (about two hours if using a wood stove)."}
        ],
        "temperature": "350°F (175°C)",
        "pan_size": "Baking pan",
        "notes": [
            "Beulah Perry: 'Lot a times, when I was a kid, the possum head was my favorite... You eat the tongue, brains, everything in the head except the eyes.'",
            "Alternative: line pan with sassafras sticks instead of grease",
            "Can also skin possum, parboil until tender, cut up, roll in pepper and flour, and fry"
        ],
        "tags": ["possum", "wild-game", "sweet-potato", "appalachian", "foxfire", "baked", "hunting"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": ["FoxfireVol1.txt.html"]
    },
    {
        "id": "foxfire-coon",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Baked Raccoon",
        "category": "main dishes",
        "attribution": "Foxfire Vol 1",
        "source_note": "Traditional Appalachian wild game recipe from The Foxfire Book",
        "description": "Raccoon baked until golden brown - a mountain hunting tradition.",
        "servings_yield": "",
        "prep_time": "Overnight soaking",
        "cook_time": "",
        "total_time": "",
        "ingredients": [
            {"item": "raccoon", "quantity": "1", "unit": "", "prep_note": "skinned, musk glands removed, gutted, soaked"},
            {"item": "salt", "quantity": "1", "unit": "spoon per lb", "prep_note": ""},
            {"item": "red pepper", "quantity": "1-2", "unit": "pods", "prep_note": "or 1 tbsp black pepper"},
            {"item": "grease", "quantity": "", "unit": "for pan", "prep_note": ""},
            {"item": "flour", "quantity": "", "unit": "for coating", "prep_note": "optional"},
            {"item": "sweet potatoes", "quantity": "", "unit": "", "prep_note": "optional, quartered"}
        ],
        "instructions": [
            {"step": 1, "text": "Skin the coon, remove the two pear-shaped musk glands from under the forearms."},
            {"step": 2, "text": "Gut, remove head, tail, and feet. Soak overnight in cold water to get the blood out."},
            {"step": 3, "text": "Put in a pot of salted water (one spoon of salt per pound), one or two pods of red pepper or one tablespoon of black pepper."},
            {"step": 4, "text": "Boil with no lid until the meat is tender."},
            {"step": 5, "text": "Remove, put in a greased baking pan, and bake until golden brown."}
        ],
        "temperature": "400°F (205°C)",
        "pan_size": "Baking pan",
        "notes": [
            "To remove wild taste: add spicewood twigs, an onion or two, a teaspoon of vinegar, or some potatoes to parboiling water",
            "Alternative: parboil, rub with salt and pepper, dot with butter, add quartered sweet potatoes around meat, bake at 400°F until tender",
            "Can also parboil, cut into pieces, roll in corn meal, and fry in lard",
            "Can be salted and smoked like ham for later use"
        ],
        "tags": ["raccoon", "coon", "wild-game", "baked", "appalachian", "foxfire", "hunting"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": ["FoxfireVol1.txt.html"]
    },
    {
        "id": "foxfire-groundhog",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Baked Groundhog",
        "category": "main dishes",
        "attribution": "Foxfire Vol 1",
        "source_note": "Traditional Appalachian wild game recipe from The Foxfire Book",
        "description": "Groundhog baked until brown.",
        "servings_yield": "",
        "prep_time": "Overnight soaking",
        "cook_time": "",
        "total_time": "",
        "ingredients": [
            {"item": "groundhog", "quantity": "1", "unit": "", "prep_note": "skinned, glands removed, gutted"},
            {"item": "salt", "quantity": "", "unit": "for soaking", "prep_note": ""},
            {"item": "spicewood twigs", "quantity": "", "unit": "", "prep_note": "to remove wild taste"},
            {"item": "pepper", "quantity": "", "unit": "to taste", "prep_note": ""},
            {"item": "grease", "quantity": "", "unit": "for pan", "prep_note": ""},
            {"item": "carrots", "quantity": "2", "unit": "", "prep_note": "optional"},
            {"item": "garlic", "quantity": "", "unit": "to taste", "prep_note": "optional"},
            {"item": "fat meat", "quantity": "1", "unit": "piece", "prep_note": "about the size of a baby's fist, optional"}
        ],
        "instructions": [
            {"step": 1, "text": "Skin the groundhog, remove the glands from under the legs, gut, and soak overnight in salty water."},
            {"step": 2, "text": "Parboil with spicewood twigs (to take the wild taste out) until tender."},
            {"step": 3, "text": "Pepper and put in a greased pan to bake until brown."}
        ],
        "temperature": "350°F (175°C)",
        "pan_size": "Baking pan",
        "notes": [
            "The hide was often placed in a bucket of ashes over which water was poured. After the ashes took the hair off, the hide was dried, kneaded, and cut up in strips for shoe strings.",
            "Alternative: parboil until tender in water with two carrots, garlic, and a piece of fat meat about the size of a baby's fist, add pepper and 1 tbsp salt. Then brown in open baking pan.",
            "Can be dried, salted, and smoked for later use"
        ],
        "tags": ["groundhog", "wild-game", "baked", "appalachian", "foxfire", "hunting"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": ["FoxfireVol1.txt.html"]
    },
    {
        "id": "foxfire-venison-stew",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Venison Stew",
        "category": "main dishes",
        "attribution": "Foxfire Vol 1",
        "source_note": "Traditional Appalachian wild game recipe from The Foxfire Book",
        "description": "Hearty venison stew with vegetables.",
        "servings_yield": "",
        "prep_time": "",
        "cook_time": "3 hours",
        "total_time": "",
        "ingredients": [
            {"item": "venison", "quantity": "2", "unit": "lb", "prep_note": "cut into 1-inch cubes"},
            {"item": "fat", "quantity": "", "unit": "small amount", "prep_note": "for browning"},
            {"item": "water", "quantity": "2", "unit": "cups", "prep_note": ""},
            {"item": "potatoes", "quantity": "4", "unit": "", "prep_note": ""},
            {"item": "carrots", "quantity": "6", "unit": "large", "prep_note": ""},
            {"item": "onions", "quantity": "4", "unit": "medium", "prep_note": ""},
            {"item": "tomatoes", "quantity": "1", "unit": "quart", "prep_note": ""},
            {"item": "salt", "quantity": "1", "unit": "tbsp", "prep_note": ""},
            {"item": "pepper", "quantity": "1", "unit": "tsp", "prep_note": ""},
            {"item": "flour", "quantity": "3", "unit": "tbsp", "prep_note": "for thickening"},
            {"item": "water", "quantity": "1/2", "unit": "cup", "prep_note": "for thickening"}
        ],
        "instructions": [
            {"step": 1, "text": "Cut two pounds of meat into one-inch cubes and brown on all sides in a small amount of fat."},
            {"step": 2, "text": "In a stewing pot, add the meat, two cups water, four potatoes, six large carrots, four medium onions, one quart of tomatoes, one tablespoon salt, and one teaspoon pepper."},
            {"step": 3, "text": "Bring to a boil and simmer for three hours."},
            {"step": 4, "text": "After three hours, thicken with three tablespoons flour and one half cup water."},
            {"step": 5, "text": "Eat then, or store in a cool place and heat as needed."}
        ],
        "temperature": "",
        "pan_size": "Stewing pot",
        "notes": ["Alternative thickening: flour, three tablespoons bacon drippings, and a pint of tomato juice"],
        "tags": ["venison", "deer", "stew", "wild-game", "appalachian", "foxfire", "hunting"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": ["FoxfireVol1.txt.html"]
    },
    {
        "id": "foxfire-venison-loaf",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Venison Loaf",
        "category": "main dishes",
        "attribution": "Foxfire Vol 1",
        "source_note": "Traditional Appalachian wild game recipe from The Foxfire Book",
        "description": "Meatloaf made with venison and pork.",
        "servings_yield": "",
        "prep_time": "",
        "cook_time": "About 1 hour",
        "total_time": "",
        "ingredients": [
            {"item": "ground deer meat", "quantity": "2 1/2", "unit": "lb", "prep_note": ""},
            {"item": "ground hog meat", "quantity": "1", "unit": "lb", "prep_note": ""},
            {"item": "eggs", "quantity": "2", "unit": "", "prep_note": ""},
            {"item": "salt", "quantity": "2", "unit": "tsp", "prep_note": ""},
            {"item": "pepper", "quantity": "1", "unit": "tsp", "prep_note": ""},
            {"item": "onion", "quantity": "1", "unit": "large", "prep_note": "chopped"},
            {"item": "breadcrumbs", "quantity": "1 1/2", "unit": "cups", "prep_note": "dampened with a little water"}
        ],
        "instructions": [
            {"step": 1, "text": "Mix together ground deer meat, ground hog meat, eggs, salt, pepper, chopped onion, and dampened breadcrumbs."},
            {"step": 2, "text": "Shape into a loaf."},
            {"step": 3, "text": "Bake for about an hour at 400°F."}
        ],
        "temperature": "400°F (205°C)",
        "pan_size": "Loaf pan or baking dish",
        "notes": [],
        "tags": ["venison", "deer", "meatloaf", "wild-game", "appalachian", "foxfire", "hunting"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": ["FoxfireVol1.txt.html"]
    },
    {
        "id": "foxfire-fried-turtle",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Fried Turtle",
        "category": "main dishes",
        "attribution": "Foxfire Vol 1",
        "source_note": "Traditional Appalachian recipe from The Foxfire Book",
        "description": "Battered and fried turtle meat.",
        "servings_yield": "",
        "prep_time": "Overnight soaking",
        "cook_time": "",
        "total_time": "",
        "ingredients": [
            {"item": "turtle", "quantity": "1", "unit": "", "prep_note": "cleaned, meat cut into pieces"},
            {"item": "salt", "quantity": "", "unit": "for soaking", "prep_note": ""},
            {"item": "soda", "quantity": "", "unit": "optional for soaking", "prep_note": ""},
            {"item": "flour", "quantity": "1", "unit": "cup", "prep_note": "plain, sifted"},
            {"item": "salt", "quantity": "1/2", "unit": "tsp", "prep_note": ""},
            {"item": "baking powder", "quantity": "1", "unit": "tsp", "prep_note": ""},
            {"item": "eggs", "quantity": "2", "unit": "", "prep_note": "beaten"},
            {"item": "milk", "quantity": "1/2", "unit": "cup", "prep_note": ""},
            {"item": "pepper", "quantity": "1", "unit": "tsp", "prep_note": "for coating"},
            {"item": "fat", "quantity": "", "unit": "for deep frying", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Clean turtle: chop head off, drop shell and all into boiling water, cut meat loose from shell, gut, cut into pieces."},
            {"step": 2, "text": "Soak meat overnight in salty water (some add a little soda) to remove the wild, strong taste."},
            {"step": 3, "text": "Parboil if desired (with salt and hot pepper)."},
            {"step": 4, "text": "Cool and dip meat into a batter made of one cup plain sifted flour, one half teaspoon salt, one teaspoon baking powder, two beaten eggs, and one half cup milk."},
            {"step": 5, "text": "Fry in deep fat until golden brown."}
        ],
        "temperature": "",
        "pan_size": "Deep fryer",
        "notes": [
            "Alternative: parboil, roll in flour, and fry with 3 tbsp flour, 1 tbsp salt, 1 tsp pepper in covered skillet",
            "Can also stew in sweet milk and butter, pepper and salt just like oyster stew"
        ],
        "tags": ["turtle", "fried", "appalachian", "foxfire", "wild-game"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": ["FoxfireVol1.txt.html"]
    },
    {
        "id": "foxfire-fried-frog-legs",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Fried Frog Legs",
        "category": "main dishes",
        "attribution": "Foxfire Vol 1 - Mrs. Lake Stiles",
        "source_note": "Traditional Appalachian recipe from The Foxfire Book, as told by Mrs. Lake Stiles",
        "description": "Fried frog legs, as told by Mrs. Lake Stiles.",
        "servings_yield": "",
        "prep_time": "",
        "cook_time": "",
        "total_time": "",
        "ingredients": [
            {"item": "frog legs", "quantity": "", "unit": "", "prep_note": "cleaned"},
            {"item": "grease", "quantity": "", "unit": "for frying", "prep_note": "not too hot"},
            {"item": "flour", "quantity": "", "unit": "for coating", "prep_note": ""},
            {"item": "salt", "quantity": "", "unit": "to taste", "prep_note": ""},
            {"item": "pepper", "quantity": "", "unit": "to taste", "prep_note": ""},
            {"item": "buttermilk", "quantity": "", "unit": "for batter", "prep_note": "optional"},
            {"item": "egg", "quantity": "1", "unit": "", "prep_note": "optional"},
            {"item": "bread crumbs or cracker crumbs", "quantity": "", "unit": "for coating", "prep_note": "optional"}
        ],
        "instructions": [
            {"step": 1, "text": "Get them dressed - cut the legs off and clean them and throw the rest away."},
            {"step": 2, "text": "Get your grease not too awfully hot - if you get it too hot, when you put the legs in they'll jump out."},
            {"step": 3, "text": "Roll them in flour and salt and pepper like chicken, and fry them."},
            {"step": 4, "text": "Or you can take buttermilk and an egg and whip it together, then roll the legs in it and either bread crumbs or cracker crumbs, and fry."}
        ],
        "temperature": "",
        "pan_size": "Frying pan",
        "notes": ["Mrs. Lake Stiles: 'Get your grease not too awfully hot - if you get it too hot, when you put the legs in they'll jump out.'"],
        "tags": ["frog-legs", "fried", "appalachian", "foxfire", "wild-game"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": ["FoxfireVol1.txt.html"]
    },
    # === MORE BREADS AND MISC ===
    {
        "id": "foxfire-ash-cakes",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Ash Cakes",
        "category": "breads",
        "attribution": "Foxfire Vol 1",
        "source_note": "Traditional Appalachian recipe from The Foxfire Book",
        "description": "Corn bread baked in hot ashes - the original mountain bread.",
        "servings_yield": "",
        "prep_time": "",
        "cook_time": "About 30 minutes",
        "total_time": "",
        "ingredients": [
            {"item": "corn bread dough", "quantity": "", "unit": "", "prep_note": "thick enough to hold shape"}
        ],
        "instructions": [
            {"step": 1, "text": "Mix up dough for corn bread, and make sure it's thick enough to hold its shape."},
            {"step": 2, "text": "Clean out a corner of the fireplace."},
            {"step": 3, "text": "Put the 'cake' in it and cover it with a clean cloth."},
            {"step": 4, "text": "Put hot ashes over the cloth, then put hot coals on top of that."},
            {"step": 5, "text": "It takes about half an hour."}
        ],
        "temperature": "",
        "pan_size": "Fireplace corner",
        "notes": ["The original way to bake bread in the mountains"],
        "tags": ["ash-cakes", "cornbread", "appalachian", "foxfire", "fireplace", "bread"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": ["FoxfireVol1.txt.html"]
    },
    {
        "id": "foxfire-bran-bread",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Bran Bread",
        "category": "breads",
        "attribution": "Foxfire Vol 1",
        "source_note": "Traditional Appalachian recipe from The Foxfire Book",
        "description": "Hearty bread made with bran flour, raisins, and molasses.",
        "servings_yield": "",
        "prep_time": "",
        "cook_time": "",
        "total_time": "",
        "ingredients": [
            {"item": "bran flour", "quantity": "1", "unit": "quart", "prep_note": ""},
            {"item": "white flour", "quantity": "1", "unit": "quart", "prep_note": ""},
            {"item": "buttermilk", "quantity": "1", "unit": "quart", "prep_note": ""},
            {"item": "seeded raisins", "quantity": "1", "unit": "cup", "prep_note": ""},
            {"item": "molasses", "quantity": "1", "unit": "cup", "prep_note": ""},
            {"item": "baking soda", "quantity": "1", "unit": "tsp", "prep_note": ""},
            {"item": "salt", "quantity": "1", "unit": "tsp", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Mix together bran flour, white flour, and buttermilk."},
            {"step": 2, "text": "Add seeded raisins and molasses."},
            {"step": 3, "text": "Last mix in baking soda and salt."},
            {"step": 4, "text": "Put into loaf pans and bake until done."}
        ],
        "temperature": "350°F (175°C)",
        "pan_size": "Loaf pans",
        "notes": [],
        "tags": ["bran", "bread", "raisins", "molasses", "appalachian", "foxfire"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": ["FoxfireVol1.txt.html"]
    },
    {
        "id": "foxfire-rye-bread",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Rye Bread (Biscuit Style)",
        "category": "breads",
        "attribution": "Foxfire Vol 1",
        "source_note": "Traditional Appalachian recipe from The Foxfire Book",
        "description": "Quick rye bread cut like biscuits.",
        "servings_yield": "",
        "prep_time": "",
        "cook_time": "10-12 minutes",
        "total_time": "",
        "ingredients": [
            {"item": "wheat flour", "quantity": "1", "unit": "cup", "prep_note": ""},
            {"item": "rye flour", "quantity": "1", "unit": "cup", "prep_note": ""},
            {"item": "corn meal", "quantity": "1/4", "unit": "cup", "prep_note": ""},
            {"item": "salt", "quantity": "1", "unit": "tsp", "prep_note": ""},
            {"item": "baking powder", "quantity": "1", "unit": "tsp", "prep_note": ""},
            {"item": "buttermilk", "quantity": "", "unit": "enough for firm dough", "prep_note": ""},
            {"item": "soda", "quantity": "1/2", "unit": "tsp", "prep_note": "per cup of buttermilk"},
            {"item": "shortening", "quantity": "3", "unit": "tbsp", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Sift together wheat flour, rye flour, corn meal, salt, and baking powder."},
            {"step": 2, "text": "Add enough buttermilk to make a firm dough, adding 1/2 tsp of soda per cup of buttermilk."},
            {"step": 3, "text": "Cut in shortening, mix thoroughly."},
            {"step": 4, "text": "Roll out to about 1/2 inch thick."},
            {"step": 5, "text": "Cut as you would biscuits, place on greased sheet."},
            {"step": 6, "text": "Bake at 450°F for ten to twelve minutes."}
        ],
        "temperature": "450°F (230°C)",
        "pan_size": "Greased baking sheet",
        "notes": [],
        "tags": ["rye", "bread", "biscuit", "appalachian", "foxfire"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": ["FoxfireVol1.txt.html"]
    },
    {
        "id": "foxfire-molasses-cookies",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Molasses Cookies",
        "category": "desserts",
        "attribution": "Foxfire Vol 1",
        "source_note": "Traditional Appalachian recipe from The Foxfire Book",
        "description": "Simple molasses cookies.",
        "servings_yield": "",
        "prep_time": "",
        "cook_time": "",
        "total_time": "",
        "ingredients": [
            {"item": "brown sugar", "quantity": "1", "unit": "cup", "prep_note": ""},
            {"item": "egg", "quantity": "1", "unit": "", "prep_note": ""},
            {"item": "molasses", "quantity": "1", "unit": "cup", "prep_note": ""},
            {"item": "melted lard or butter", "quantity": "3/4", "unit": "cup", "prep_note": ""},
            {"item": "boiling water", "quantity": "1/4", "unit": "cup", "prep_note": ""},
            {"item": "salt", "quantity": "", "unit": "to taste", "prep_note": ""},
            {"item": "flour", "quantity": "", "unit": "enough to knead", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Mix brown sugar, egg, molasses, melted lard or butter, boiling water, and salt."},
            {"step": 2, "text": "Add enough flour to knead."},
            {"step": 3, "text": "Roll, cut out, and bake in hot oven."}
        ],
        "temperature": "375°F (190°C)",
        "pan_size": "Baking sheet",
        "notes": [],
        "tags": ["cookies", "molasses", "appalachian", "foxfire", "dessert"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": ["FoxfireVol1.txt.html"]
    },
    {
        "id": "foxfire-homemade-butter",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Homemade Butter",
        "category": "dairy",
        "attribution": "Foxfire Vol 1",
        "source_note": "Traditional butter churning from The Foxfire Book",
        "description": "Traditional churned butter with tips for proper temperature and handling.",
        "servings_yield": "About 1/2-1 lb per batch",
        "prep_time": "",
        "cook_time": "30-40 minutes churning",
        "total_time": "",
        "ingredients": [
            {"item": "rich milk (mostly cream)", "quantity": "", "unit": "half to fill churn", "prep_note": "clabbered"},
            {"item": "salt", "quantity": "1/4 to 1/2", "unit": "tsp", "prep_note": "per pint of butter"}
        ],
        "instructions": [
            {"step": 1, "text": "Fill churn half or slightly over half full with rich milk which should be mostly cream."},
            {"step": 2, "text": "Set the churn aside so the cream can 'turn' or clabber. In summer, pour up one night and churn the next. In winter, warm on alternate sides by fireplace for 3 days."},
            {"step": 3, "text": "Test readiness: tilt the churn to its side - liquid should hold together in one form, separating cleanly from sides."},
            {"step": 4, "text": "Insert dasher into churn, cover with lid (hole in center for dasher stick)."},
            {"step": 5, "text": "Agitate up and down for 30-40 minutes until butter gathers."},
            {"step": 6, "text": "Remove lid and stir gently with the dasher in a sideways motion to bring butter together."},
            {"step": 7, "text": "Lift lumps of butter out, drain, place in bowl."},
            {"step": 8, "text": "Either chill overnight in refrigerator then mold with salt; or rinse with cold water immediately for fresher flavor."},
            {"step": 9, "text": "Press butter into mold. Store in cool place."}
        ],
        "temperature": "",
        "pan_size": "4-5 gallon churn",
        "notes": [
            "If clabbered cream is too warm: result is soft white puffy butter - add cold water to improve texture",
            "If too cold: yields specks that won't stick together - stir in hot water to help gather",
            "If left too long, cream will curdle and separate and won't make good butter",
            "If churned too early while still 'blinky milk,' won't make good butter either",
            "Liquid left after butter removed is buttermilk",
            "Traditional chant: 'Come butter come, Come butter come, Peter standing at the gate, Waiting for a butter cake, Come butter come.'"
        ],
        "tags": ["butter", "dairy", "churning", "appalachian", "foxfire", "traditional"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": ["FoxfireVol1.txt.html"]
    }
]

def main():
    with open(RECIPES_FILE, 'r') as f:
        data = json.load(f)

    existing_ids = {r['id'] for r in data['recipes']}
    added = 0
    for recipe in FOXFIRE_RECIPES_BATCH3:
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
