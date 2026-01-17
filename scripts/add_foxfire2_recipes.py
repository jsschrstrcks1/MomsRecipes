#!/usr/bin/env python3
"""
Script to add Foxfire 2 recipes to recipes.json
Spring Wild Plant Foods chapter - traditional Appalachian foraging recipes
"""
import json
from pathlib import Path

DATA_DIR = Path(__file__).parent.parent / "data"
RECIPES_FILE = DATA_DIR / "recipes.json"

# Foxfire 2 recipes - Spring Wild Plant Foods
FOXFIRE2_RECIPES = [
    # === SASSAFRAS RECIPES ===
    {
        "id": "foxfire2-sassafras-tea",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Sassafras Tea",
        "category": "beverages",
        "attribution": "Foxfire 2 - Florence Brooks",
        "source_note": "Traditional Appalachian spring tonic from The Foxfire Book 2",
        "description": "A spring tonic tea made from sassafras roots. As they say, 'Drink sassafras during March, and you won't need a doctor all year.'",
        "servings_yield": "1 quart",
        "prep_time": "",
        "cook_time": "10-12 minutes",
        "total_time": "",
        "ingredients": [
            {"item": "sassafras roots and tender limbs", "quantity": "", "unit": "", "prep_note": "gathered in March"},
            {"item": "shredded bark", "quantity": "1", "unit": "cup", "prep_note": "alternative"},
            {"item": "water", "quantity": "1", "unit": "quart", "prep_note": "boiling"},
            {"item": "sugar", "quantity": "", "unit": "to taste", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Find a small bush, pull up roots and all, or dig down by the base of a tree and cut off a few sections of root."},
            {"step": 2, "text": "Wash the roots and scrub until the bark is pink and clean. Peel off the pinkish bark for tea."},
            {"step": 3, "text": "Put one cup shredded bark in quart of boiling water."},
            {"step": 4, "text": "Boil ten to twelve minutes."},
            {"step": 5, "text": "Sweeten with sugar to taste. Can be served hot or with ice."}
        ],
        "temperature": "",
        "pan_size": "",
        "notes": [
            "Sassafras is best gathered in spring when the bark 'slips' or peels off easily",
            "Red sassafras is considered best but hard to find nowadays",
            "Big roots should be pounded to a pulp before boiling"
        ],
        "tags": ["beverage", "tea", "spring-tonic", "appalachian", "foxfire", "foraging"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": ["Foxfire-Book-2.txt"]
    },
    {
        "id": "foxfire2-sassafras-jelly",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Sassafras Jelly",
        "category": "preserves",
        "attribution": "Foxfire 2",
        "source_note": "Traditional Appalachian recipe from The Foxfire Book 2",
        "description": "A unique jelly made from strong sassafras tea.",
        "servings_yield": "",
        "prep_time": "",
        "cook_time": "",
        "total_time": "",
        "ingredients": [
            {"item": "strong sassafras tea", "quantity": "2", "unit": "cups", "prep_note": ""},
            {"item": "powdered pectin", "quantity": "1", "unit": "package", "prep_note": ""},
            {"item": "strained honey", "quantity": "3", "unit": "cups", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Boil two cups strong sassafras tea and one package powdered pectin."},
            {"step": 2, "text": "Add three cups strained honey."},
            {"step": 3, "text": "Strain and put in jars."}
        ],
        "temperature": "",
        "pan_size": "",
        "notes": [],
        "tags": ["jelly", "preserves", "sassafras", "appalachian", "foxfire", "foraging"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": ["Foxfire-Book-2.txt"]
    },
    # === DOCK RECIPES ===
    {
        "id": "foxfire2-dock-greens",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Dock Greens",
        "category": "sides",
        "attribution": "Foxfire 2",
        "source_note": "Traditional Appalachian wild greens from The Foxfire Book 2",
        "description": "Young dock leaves cooked as greens, rich in vitamins A and C. Dock greens eaten in spring will thin and purify the blood.",
        "servings_yield": "",
        "prep_time": "",
        "cook_time": "",
        "total_time": "",
        "ingredients": [
            {"item": "young dock leaves", "quantity": "", "unit": "", "prep_note": "very young and tender"},
            {"item": "grease", "quantity": "", "unit": "for frying", "prep_note": "hot"},
            {"item": "salt", "quantity": "", "unit": "to taste", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Wash dock leaves thoroughly."},
            {"step": 2, "text": "Parboil until leaves turn a lighter green."},
            {"step": 3, "text": "Pour off water, wash two or three times."},
            {"step": 4, "text": "Either fry in hot grease and salt for three to five minutes, or bring to a boil in fresh water, season and serve."}
        ],
        "temperature": "",
        "pan_size": "Frying pan",
        "notes": [
            "Often cooked in combination with horseradish, mustard, or turnip greens",
            "Cooked with meat, dock leaves are said to make the meat cook more rapidly"
        ],
        "tags": ["greens", "wild-plants", "appalachian", "foxfire", "foraging", "spring"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": ["Foxfire-Book-2.txt"]
    },
    {
        "id": "foxfire2-hot-greens-on-toast",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Hot Greens on Toast",
        "category": "sides",
        "attribution": "Foxfire 2",
        "source_note": "Traditional Appalachian recipe from The Foxfire Book 2",
        "description": "Creamy dock greens served on toast with bacon.",
        "servings_yield": "",
        "prep_time": "",
        "cook_time": "",
        "total_time": "",
        "ingredients": [
            {"item": "cooked dock", "quantity": "1", "unit": "pint", "prep_note": ""},
            {"item": "onion", "quantity": "1", "unit": "tbsp", "prep_note": "chopped"},
            {"item": "horseradish", "quantity": "2", "unit": "tbsp", "prep_note": ""},
            {"item": "sour cream", "quantity": "1", "unit": "cup", "prep_note": "or a little vinegar"},
            {"item": "salt", "quantity": "", "unit": "to taste", "prep_note": ""},
            {"item": "pepper", "quantity": "", "unit": "to taste", "prep_note": ""},
            {"item": "toast", "quantity": "", "unit": "for serving", "prep_note": ""},
            {"item": "bacon", "quantity": "", "unit": "for topping", "prep_note": "fried"}
        ],
        "instructions": [
            {"step": 1, "text": "To one pint of cooked dock, add one tablespoon chopped onion, two tablespoons horseradish, and one cup sour cream or a little vinegar."},
            {"step": 2, "text": "Season with salt and pepper."},
            {"step": 3, "text": "Serve on toast and top with fried bacon."}
        ],
        "temperature": "",
        "pan_size": "",
        "notes": [],
        "tags": ["greens", "breakfast", "appalachian", "foxfire", "foraging"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": ["Foxfire-Book-2.txt"]
    },
    {
        "id": "foxfire2-dock-soup",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Dock Soup",
        "category": "soups",
        "attribution": "Foxfire 2",
        "source_note": "Traditional Appalachian soup from The Foxfire Book 2",
        "description": "A creamy soup made from young dock leaves.",
        "servings_yield": "",
        "prep_time": "",
        "cook_time": "30 minutes",
        "total_time": "",
        "ingredients": [
            {"item": "young dock leaves", "quantity": "", "unit": "", "prep_note": ""},
            {"item": "milk", "quantity": "", "unit": "", "prep_note": ""},
            {"item": "onion", "quantity": "", "unit": "", "prep_note": ""},
            {"item": "butter", "quantity": "", "unit": "", "prep_note": ""},
            {"item": "flour", "quantity": "2", "unit": "tbsp", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Cook young leaves, drain off water and strain."},
            {"step": 2, "text": "Add milk, onion, butter, and two tablespoons flour."},
            {"step": 3, "text": "Cook slowly one-half hour."}
        ],
        "temperature": "",
        "pan_size": "",
        "notes": [],
        "tags": ["soup", "greens", "wild-plants", "appalachian", "foxfire", "foraging"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": ["Foxfire-Book-2.txt"]
    },
    # === SORREL RECIPES ===
    {
        "id": "foxfire2-sorrel-soup",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Sorrel Soup",
        "category": "soups",
        "attribution": "Foxfire 2",
        "source_note": "Traditional Appalachian recipe from The Foxfire Book 2",
        "description": "A rich, creamy soup from sheep sorrel leaves, high in vitamin C.",
        "servings_yield": "",
        "prep_time": "",
        "cook_time": "",
        "total_time": "",
        "ingredients": [
            {"item": "sorrel leaves", "quantity": "1", "unit": "lb", "prep_note": "bruised"},
            {"item": "butter or margarine", "quantity": "1/4", "unit": "cup", "prep_note": ""},
            {"item": "egg yolks", "quantity": "2", "unit": "", "prep_note": ""},
            {"item": "salt", "quantity": "", "unit": "dash", "prep_note": ""},
            {"item": "pepper", "quantity": "", "unit": "dash", "prep_note": ""},
            {"item": "onion", "quantity": "1/2", "unit": "cup", "prep_note": "chopped"},
            {"item": "cream", "quantity": "1", "unit": "cup", "prep_note": ""},
            {"item": "chicken broth", "quantity": "3", "unit": "cups", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Chop sorrel and onion together (or ramps, if available)."},
            {"step": 2, "text": "Simmer in butter until wilted."},
            {"step": 3, "text": "Add eggs and cream."},
            {"step": 4, "text": "Bring to a quick boil and serve."}
        ],
        "temperature": "",
        "pan_size": "",
        "notes": ["Ramps can be substituted for onion if available"],
        "tags": ["soup", "sorrel", "wild-plants", "appalachian", "foxfire", "foraging"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": ["Foxfire-Book-2.txt"]
    },
    {
        "id": "foxfire2-sorrel-omelet",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Sorrel Omelet",
        "category": "breakfast",
        "attribution": "Foxfire 2",
        "source_note": "Traditional Appalachian recipe from The Foxfire Book 2",
        "description": "A fresh omelet made with wild sorrel leaves.",
        "servings_yield": "",
        "prep_time": "",
        "cook_time": "",
        "total_time": "",
        "ingredients": [
            {"item": "young sorrel leaves", "quantity": "", "unit": "", "prep_note": "washed and dried"},
            {"item": "eggs", "quantity": "", "unit": "", "prep_note": ""},
            {"item": "onion", "quantity": "", "unit": "some", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Wash and dry young sorrel leaves. Chop fine."},
            {"step": 2, "text": "Add to eggs, with some onion."},
            {"step": 3, "text": "Cook omelet."},
            {"step": 4, "text": "When omelet is cooked, sprinkle more fresh sorrel leaves on top."}
        ],
        "temperature": "",
        "pan_size": "",
        "notes": [],
        "tags": ["omelet", "breakfast", "eggs", "wild-plants", "appalachian", "foxfire"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": ["Foxfire-Book-2.txt"]
    },
    # === RHUBARB RECIPES ===
    {
        "id": "foxfire2-rhubarb-pie",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Rhubarb Pie",
        "category": "desserts",
        "attribution": "Foxfire 2",
        "source_note": "Traditional Appalachian recipe from The Foxfire Book 2",
        "description": "A layered rhubarb pie with biscuits, served cold with milk or cream.",
        "servings_yield": "",
        "prep_time": "",
        "cook_time": "",
        "total_time": "",
        "ingredients": [
            {"item": "rhubarb stalks", "quantity": "", "unit": "", "prep_note": "cut just above ground"},
            {"item": "water", "quantity": "", "unit": "a little", "prep_note": ""},
            {"item": "honey or syrup", "quantity": "", "unit": "to sweeten", "prep_note": ""},
            {"item": "biscuits", "quantity": "", "unit": "", "prep_note": "split"}
        ],
        "instructions": [
            {"step": 1, "text": "Cut rhubarb stalks just above ground. Slice into half-inch pieces."},
            {"step": 2, "text": "Cook with a little water over low heat in uncovered pan, stirring often, until rhubarb is the consistency of applesauce."},
            {"step": 3, "text": "Sweeten with honey or syrup."},
            {"step": 4, "text": "Layer in large flat-bottomed pan with half inch of rhubarb sauce, layer of split biscuits, layer of rhubarb, etc., finishing with layer of biscuits."},
            {"step": 5, "text": "Chill and eat with milk or cream."}
        ],
        "temperature": "Low heat",
        "pan_size": "Large flat-bottomed pan",
        "notes": ["Rhubarb leaves are poisonous - use only the stalks"],
        "tags": ["pie", "rhubarb", "dessert", "appalachian", "foxfire"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": ["Foxfire-Book-2.txt"]
    },
    {
        "id": "foxfire2-rhubarb-jelly",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Rhubarb Jelly",
        "category": "preserves",
        "attribution": "Foxfire 2",
        "source_note": "Traditional Appalachian recipe from The Foxfire Book 2",
        "description": "A tangy jelly made from fresh rhubarb.",
        "servings_yield": "",
        "prep_time": "",
        "cook_time": "",
        "total_time": "",
        "ingredients": [
            {"item": "rhubarb", "quantity": "3", "unit": "lb", "prep_note": "washed and sliced"},
            {"item": "water", "quantity": "1", "unit": "cup", "prep_note": ""},
            {"item": "sugar", "quantity": "3", "unit": "lb", "prep_note": "about 7 cups"},
            {"item": "liquid pectin", "quantity": "1", "unit": "bottle", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Wash and slice three pounds rhubarb."},
            {"step": 2, "text": "Add one cup water and bring to a boil."},
            {"step": 3, "text": "Reduce heat and simmer ten minutes."},
            {"step": 4, "text": "Strain through cheesecloth."},
            {"step": 5, "text": "Add three pounds of sugar (about seven cups) and bring to a rolling boil."},
            {"step": 6, "text": "Add one bottle liquid pectin."},
            {"step": 7, "text": "Cook, stirring, one more minute."},
            {"step": 8, "text": "Pour in glasses. Jelly should harden in three to four hours."}
        ],
        "temperature": "",
        "pan_size": "",
        "notes": [],
        "tags": ["jelly", "preserves", "rhubarb", "appalachian", "foxfire", "canning"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": ["Foxfire-Book-2.txt"]
    },
    {
        "id": "foxfire2-turks-delight",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Turk's Delight (Fried Rhubarb Flowers)",
        "category": "desserts",
        "attribution": "Foxfire 2",
        "source_note": "Traditional Appalachian recipe from The Foxfire Book 2",
        "description": "Battered and fried rhubarb flowers, dipped in sugar.",
        "servings_yield": "",
        "prep_time": "",
        "cook_time": "",
        "total_time": "",
        "ingredients": [
            {"item": "rhubarb flowers", "quantity": "", "unit": "", "prep_note": "gathered"},
            {"item": "salt water", "quantity": "", "unit": "for soaking", "prep_note": ""},
            {"item": "batter", "quantity": "", "unit": "", "prep_note": ""},
            {"item": "fat", "quantity": "", "unit": "for frying", "prep_note": "hot"},
            {"item": "sugar", "quantity": "", "unit": "for dipping", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Gather rhubarb flowers."},
            {"step": 2, "text": "Soak one-half hour in salt water."},
            {"step": 3, "text": "Drain and dry."},
            {"step": 4, "text": "Dip in batter and fry in hot fat."},
            {"step": 5, "text": "Drain."},
            {"step": 6, "text": "Dip in sugar and eat hot."}
        ],
        "temperature": "",
        "pan_size": "",
        "notes": [],
        "tags": ["fried", "flowers", "rhubarb", "dessert", "appalachian", "foxfire"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": ["Foxfire-Book-2.txt"]
    },
    # === POKE RECIPES ===
    {
        "id": "foxfire2-poke-greens",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Poke Greens",
        "category": "sides",
        "attribution": "Foxfire 2 - Dr. Neville",
        "source_note": "Traditional Appalachian recipe from The Foxfire Book 2",
        "description": "The most popular wild food in the mountain area. Dr. Neville said to eat at least one mess of poke each spring - 'worth all the medicine you could buy.'",
        "servings_yield": "",
        "prep_time": "",
        "cook_time": "",
        "total_time": "",
        "ingredients": [
            {"item": "young poke shoots", "quantity": "", "unit": "", "prep_note": "6-8 inches high"},
            {"item": "water", "quantity": "", "unit": "for parboiling", "prep_note": ""},
            {"item": "salt", "quantity": "", "unit": "to taste", "prep_note": ""},
            {"item": "hard-boiled eggs", "quantity": "", "unit": "for topping", "prep_note": "sliced"}
        ],
        "instructions": [
            {"step": 1, "text": "Collect tender young shoots of poke six to eight inches high in the spring. Do not cut below surface of ground as root is poisonous."},
            {"step": 2, "text": "Wash and cook leaves and stems together, parboiling two times (pouring off water each time after boiling a few minutes)."},
            {"step": 3, "text": "Boil in third water until tender, salting to taste."},
            {"step": 4, "text": "Drain and top with slices of hard-boiled egg."}
        ],
        "temperature": "",
        "pan_size": "",
        "notes": [
            "NEVER eat poke raw - it must be cooked",
            "Roots and berries are poisonous",
            "Avoid when stems become red and plant is over a foot high",
            "Rich in iron and vitamin C"
        ],
        "tags": ["greens", "poke", "wild-plants", "spring-tonic", "appalachian", "foxfire", "foraging"],
        "confidence": {"overall": "high", "flags": ["Must parboil twice - safety critical"]},
        "image_refs": ["Foxfire-Book-2.txt"]
    },
    {
        "id": "foxfire2-poke-sallet",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Poke Sallet",
        "category": "sides",
        "attribution": "Foxfire 2",
        "source_note": "Traditional Appalachian recipe from The Foxfire Book 2",
        "description": "Classic poke sallet fried with eggs.",
        "servings_yield": "",
        "prep_time": "",
        "cook_time": "",
        "total_time": "",
        "ingredients": [
            {"item": "poke greens", "quantity": "", "unit": "", "prep_note": "young shoots"},
            {"item": "hot grease", "quantity": "", "unit": "for frying", "prep_note": ""},
            {"item": "salt", "quantity": "1/2", "unit": "tsp", "prep_note": ""},
            {"item": "eggs", "quantity": "2", "unit": "", "prep_note": "beaten"},
            {"item": "vinegar or pickle juice", "quantity": "", "unit": "for serving", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Put greens in a boiler of cold water; wash two or three times."},
            {"step": 2, "text": "Drain off all the water."},
            {"step": 3, "text": "Fry in pan of hot grease. Add half teaspoon of salt."},
            {"step": 4, "text": "Let cool. Beat two eggs and stir in after greens have cooled."},
            {"step": 5, "text": "Serve with vinegar or pickle juice."}
        ],
        "temperature": "",
        "pan_size": "Frying pan",
        "notes": ["Always parboil poke twice before frying"],
        "tags": ["greens", "poke", "eggs", "appalachian", "foxfire", "foraging"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": ["Foxfire-Book-2.txt"]
    },
    {
        "id": "foxfire2-poke-pickles",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Poke Pickles",
        "category": "preserves",
        "attribution": "Foxfire 2",
        "source_note": "Traditional Appalachian pickles from The Foxfire Book 2",
        "description": "Pickled young poke stalks, preserved in spiced vinegar.",
        "servings_yield": "",
        "prep_time": "",
        "cook_time": "",
        "total_time": "",
        "ingredients": [
            {"item": "very young poke stalks", "quantity": "", "unit": "", "prep_note": "scraped, leaves removed"},
            {"item": "vinegar", "quantity": "1", "unit": "cup", "prep_note": ""},
            {"item": "sugar", "quantity": "1/2", "unit": "cup", "prep_note": ""},
            {"item": "salt", "quantity": "1", "unit": "tbsp", "prep_note": ""},
            {"item": "cinnamon stick", "quantity": "1", "unit": "", "prep_note": ""},
            {"item": "whole cloves", "quantity": "", "unit": "several", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Collect very young stalks, scrape, remove leaves, and pack in jars."},
            {"step": 2, "text": "Combine one cup vinegar, half cup sugar, one tablespoon salt, one stick cinnamon, several whole cloves."},
            {"step": 3, "text": "Boil, pour over poke, and seal."}
        ],
        "temperature": "",
        "pan_size": "",
        "notes": [],
        "tags": ["pickles", "poke", "preserves", "appalachian", "foxfire", "canning"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": ["Foxfire-Book-2.txt"]
    },
    # === LAMB'S QUARTERS RECIPES ===
    {
        "id": "foxfire2-lambs-quarter-greens",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Lamb's Quarter Greens",
        "category": "sides",
        "attribution": "Foxfire 2",
        "source_note": "Traditional Appalachian recipe from The Foxfire Book 2",
        "description": "Wild spinach-like greens. As someone said, 'If they think it's spinach, they think it's good.' Rich in iron and potassium.",
        "servings_yield": "1 gallon",
        "prep_time": "",
        "cook_time": "",
        "total_time": "",
        "ingredients": [
            {"item": "lamb's quarters and dock", "quantity": "1", "unit": "gallon", "prep_note": "mixed"},
            {"item": "water", "quantity": "1", "unit": "cup", "prep_note": ""},
            {"item": "grease", "quantity": "4", "unit": "tbsp", "prep_note": ""},
            {"item": "fatback", "quantity": "", "unit": "optional", "prep_note": "streak of fat and streak of lean"}
        ],
        "instructions": [
            {"step": 1, "text": "Gather one gallon greens (lamb's quarters and dock)."},
            {"step": 2, "text": "Wash and boil for ten minutes."},
            {"step": 3, "text": "Drain and add one cup water and four tablespoons grease."},
            {"step": 4, "text": "Cook covered until tender."},
            {"step": 5, "text": "If preferred, cook with a streak of fat and streak of lean."}
        ],
        "temperature": "",
        "pan_size": "",
        "notes": ["Can use white sauce with lemon, butter, bacon bits and vinegar instead"],
        "tags": ["greens", "wild-plants", "appalachian", "foxfire", "foraging", "spring"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": ["Foxfire-Book-2.txt"]
    },
    # === PURSLANE (PUSSLEY) RECIPES ===
    {
        "id": "foxfire2-pussley-casserole",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Pussley Casserole",
        "category": "main dishes",
        "attribution": "Foxfire 2",
        "source_note": "Traditional Appalachian casserole from The Foxfire Book 2",
        "description": "A baked casserole made from purslane (pussley), rich in vitamin C.",
        "servings_yield": "",
        "prep_time": "",
        "cook_time": "",
        "total_time": "",
        "ingredients": [
            {"item": "purslane (pussley)", "quantity": "", "unit": "", "prep_note": "cooked, drained, and chopped fine"},
            {"item": "eggs", "quantity": "", "unit": "", "prep_note": ""},
            {"item": "cracker crumbs or cornbread", "quantity": "", "unit": "", "prep_note": "crumbled"},
            {"item": "cheese", "quantity": "", "unit": "for topping", "prep_note": "grated"}
        ],
        "instructions": [
            {"step": 1, "text": "Cook purslane, drain, and chop fine."},
            {"step": 2, "text": "Add eggs and cracker crumbs, or crumbled cornbread."},
            {"step": 3, "text": "Bake."},
            {"step": 4, "text": "Top with grated cheese just before serving."}
        ],
        "temperature": "Low heat",
        "pan_size": "Baking dish",
        "notes": ["Can add bread crumbs, onion, poke greens, and beaten egg instead"],
        "tags": ["casserole", "wild-plants", "purslane", "appalachian", "foxfire", "foraging"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": ["Foxfire-Book-2.txt"]
    },
    {
        "id": "foxfire2-pickled-pussley",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Pickled Pussley",
        "category": "preserves",
        "attribution": "Foxfire 2",
        "source_note": "Traditional Appalachian pickles from The Foxfire Book 2",
        "description": "Pickled purslane tips in mustard vinegar.",
        "servings_yield": "",
        "prep_time": "",
        "cook_time": "",
        "total_time": "",
        "ingredients": [
            {"item": "pussley tips", "quantity": "", "unit": "", "prep_note": ""},
            {"item": "wild onions", "quantity": "", "unit": "", "prep_note": ""},
            {"item": "vinegar", "quantity": "", "unit": "", "prep_note": ""},
            {"item": "ground mustard seed", "quantity": "1/4", "unit": "cup", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Cook wild onions with vinegar and one-quarter cup ground mustard seed."},
            {"step": 2, "text": "Simmer, strain."},
            {"step": 3, "text": "Pour over pussley tips."}
        ],
        "temperature": "",
        "pan_size": "",
        "notes": [],
        "tags": ["pickles", "preserves", "purslane", "wild-plants", "appalachian", "foxfire"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": ["Foxfire-Book-2.txt"]
    },
    # === CRESS RECIPES ===
    {
        "id": "foxfire2-cress-salad",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Cress Salad",
        "category": "salads",
        "attribution": "Foxfire 2",
        "source_note": "Traditional Appalachian salad from The Foxfire Book 2",
        "description": "A fresh salad using wild water cress.",
        "servings_yield": "",
        "prep_time": "",
        "cook_time": "",
        "total_time": "",
        "ingredients": [
            {"item": "cresses", "quantity": "2", "unit": "cups", "prep_note": "finely cut"},
            {"item": "salt", "quantity": "1/4", "unit": "tsp", "prep_note": ""},
            {"item": "salad oil", "quantity": "1", "unit": "tbsp", "prep_note": ""},
            {"item": "vinegar", "quantity": "1", "unit": "tbsp", "prep_note": ""},
            {"item": "French dressing", "quantity": "1", "unit": "tbsp", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Toss together lightly: two cups finely cut cresses, one-fourth teaspoon salt, one tablespoon salad oil, one tablespoon vinegar, one tablespoon French dressing."}
        ],
        "temperature": "",
        "pan_size": "",
        "notes": ["Can also chop and add hard-boiled egg"],
        "tags": ["salad", "cress", "wild-plants", "appalachian", "foxfire", "foraging", "raw"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": ["Foxfire-Book-2.txt"]
    },
    # === NETTLE RECIPES ===
    {
        "id": "foxfire2-nettle-soup",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Nettle Soup",
        "category": "soups",
        "attribution": "Foxfire 2",
        "source_note": "Traditional Appalachian soup from The Foxfire Book 2",
        "description": "A nutritious soup made from stinging nettles. Must gather with stout gloves!",
        "servings_yield": "",
        "prep_time": "",
        "cook_time": "Long time",
        "total_time": "",
        "ingredients": [
            {"item": "nettles", "quantity": "", "unit": "", "prep_note": "gathered in early spring with gloves"},
            {"item": "water", "quantity": "", "unit": "", "prep_note": ""},
            {"item": "butter", "quantity": "", "unit": "", "prep_note": ""},
            {"item": "flour", "quantity": "", "unit": "", "prep_note": ""},
            {"item": "egg yolks", "quantity": "", "unit": "", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Gather plants in early spring with stout gloves."},
            {"step": 2, "text": "Cook a long time to destroy sting."},
            {"step": 3, "text": "Add water, thicken with butter, flour, and egg yolks."}
        ],
        "temperature": "",
        "pan_size": "",
        "notes": [
            "Must gather with stout gloves",
            "Repeated cookings destroy the sting"
        ],
        "tags": ["soup", "nettles", "wild-plants", "appalachian", "foxfire", "foraging", "spring"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": ["Foxfire-Book-2.txt"]
    },
    {
        "id": "foxfire2-baked-nettles",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Baked Nettles",
        "category": "main dishes",
        "attribution": "Foxfire 2",
        "source_note": "Traditional Appalachian recipe from The Foxfire Book 2",
        "description": "Nettles baked with ground beef and rice.",
        "servings_yield": "",
        "prep_time": "",
        "cook_time": "",
        "total_time": "",
        "ingredients": [
            {"item": "nettles", "quantity": "", "unit": "", "prep_note": "cooked a long time"},
            {"item": "ground beef", "quantity": "", "unit": "", "prep_note": ""},
            {"item": "rice", "quantity": "", "unit": "", "prep_note": ""},
            {"item": "seasoning", "quantity": "", "unit": "", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Cook nettles a long time."},
            {"step": 2, "text": "Strain off liquid."},
            {"step": 3, "text": "Chop fine."},
            {"step": 4, "text": "Add ground beef, rice, and seasoning."},
            {"step": 5, "text": "Bake at low heat until firm."}
        ],
        "temperature": "Low heat",
        "pan_size": "Baking dish",
        "notes": [],
        "tags": ["casserole", "nettles", "beef", "wild-plants", "appalachian", "foxfire"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": ["Foxfire-Book-2.txt"]
    },
    # === HORSERADISH ===
    {
        "id": "foxfire2-horseradish-sauce",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Horseradish Sauce",
        "category": "sauces",
        "attribution": "Foxfire 2",
        "source_note": "Traditional Appalachian sauce from The Foxfire Book 2",
        "description": "A classic horseradish sauce for beef.",
        "servings_yield": "",
        "prep_time": "",
        "cook_time": "",
        "total_time": "",
        "ingredients": [
            {"item": "butter", "quantity": "3", "unit": "tbsp", "prep_note": ""},
            {"item": "flour", "quantity": "1", "unit": "tbsp", "prep_note": ""},
            {"item": "boiling beef stock", "quantity": "1 1/2", "unit": "cups", "prep_note": ""},
            {"item": "horseradish", "quantity": "", "unit": "to taste", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Combine three tablespoons butter, one tablespoon flour, one and one-half cups boiling beef stock and horseradish to taste."},
            {"step": 2, "text": "Cook until thickened and serve."}
        ],
        "temperature": "",
        "pan_size": "",
        "notes": ["Eating horseradish is said to be good for rheumatism, scurvy, and hoarseness"],
        "tags": ["sauce", "horseradish", "condiment", "appalachian", "foxfire"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": ["Foxfire-Book-2.txt"]
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
    for recipe in FOXFIRE2_RECIPES:
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

    print(f"\nAdded {added} new recipes from Foxfire 2. Total: {len(data['recipes'])}")


if __name__ == "__main__":
    main()
