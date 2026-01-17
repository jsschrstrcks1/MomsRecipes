#!/usr/bin/env python3
"""
Add Eat the Weeds recipes - Batch 3.

This batch includes: lotus, bulrush/cattail recipes, burdock beer,
begonia, alligator, armadillo, bitter melon, and chaya recipes
from Green Deane's eattheweeds.com.
"""

import json
from pathlib import Path

RECIPES_FILE = Path(__file__).parent.parent / "data" / "recipes.json"

ETW_BATCH3_RECIPES = [
    # ===== LOTUS RECIPES =====
    {
        "id": "stir-fried-lotus-root-etw",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Stir-Fried Lotus Root",
        "category": "sides",
        "attribution": "Eat the Weeds - Green Deane",
        "source_note": "Wild foraging recipe from eattheweeds.com",
        "description": "Asian-style stir-fried lotus root with sesame and sake.",
        "ingredients": [
            {"item": "lotus root", "quantity": "2", "unit": "lbs", "prep_note": "trimmed and peeled"},
            {"item": "sesame oil", "quantity": "2", "unit": "tbsp"},
            {"item": "sugar", "quantity": "1.5", "unit": "tbsp"},
            {"item": "sake or pale dry sherry", "quantity": "1", "unit": "cup"},
            {"item": "dark soy sauce", "quantity": "2", "unit": "tbsp"},
            {"item": "toasted sesame seeds", "quantity": "1", "unit": "tsp"},
            {"item": "hot pepper (chipotle in adobo)", "quantity": "1", "unit": "small"},
            {"item": "scallions", "quantity": "2", "unit": "", "prep_note": "optional"}
        ],
        "instructions": [
            {"step": 1, "text": "Slice lotus root crosswise into quarter-inch pieces."},
            {"step": 2, "text": "Soak in water and change until water runs clear, then dry thoroughly."},
            {"step": 3, "text": "Heat sesame oil and add lotus roots, tossing briefly."},
            {"step": 4, "text": "Add remaining ingredients and stir continuously for approximately 10 minutes until the mixture reduces."},
            {"step": 5, "text": "Serve warm. Reheats well."}
        ],
        "notes": ["Lotus root discolors quickly - place cut pieces in water with lemon juice immediately"],
        "tags": ["lotus", "asian", "stir-fry", "sides", "foraging", "eat the weeds"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    # ===== BULRUSH RECIPES =====
    {
        "id": "bulrush-broth-etw",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Bulrush Broth",
        "category": "soups",
        "attribution": "Eat the Weeds - Green Deane",
        "source_note": "Wild foraging recipe from eattheweeds.com",
        "description": "Hearty broth with bulrush shoots, roots, and oxtail.",
        "ingredients": [
            {"item": "oxtail", "quantity": "1.5", "unit": "lbs", "prep_note": "cut up"},
            {"item": "salt", "quantity": "1.5", "unit": "tsp"},
            {"item": "flour", "quantity": "1/2", "unit": "cup"},
            {"item": "bulrush flour", "quantity": "2", "unit": "tbsp"},
            {"item": "mustard seed", "quantity": "2", "unit": "tbsp"},
            {"item": "bacon fat", "quantity": "2", "unit": "tbsp"},
            {"item": "water", "quantity": "6", "unit": "cups"},
            {"item": "bulrush shoots", "quantity": "1/2", "unit": "cup"},
            {"item": "wild onions", "quantity": "3", "unit": ""},
            {"item": "wild rice", "quantity": "1/4", "unit": "cup"},
            {"item": "bulrush roots", "quantity": "3", "unit": "", "prep_note": "thinly sliced"},
            {"item": "Worcestershire sauce", "quantity": "1", "unit": "tbsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Roll meat in flour-salt mixture."},
            {"step": 2, "text": "Sauté in hot fat until browned."},
            {"step": 3, "text": "Add water, shoots, onions, cover, and simmer 1.5 hours until rice is tender."}
        ],
        "tags": ["bulrush", "cattail", "soup", "broth", "foraging", "eat the weeds"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "bulrush-casserole-etw",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Bulrush Casserole",
        "category": "main-dishes",
        "attribution": "Eat the Weeds - Green Deane",
        "source_note": "Wild foraging recipe from eattheweeds.com",
        "description": "Comfort food casserole with bulrush sprouts and ground beef.",
        "servings_yield": "6 servings",
        "ingredients": [
            {"item": "small bulrush sprouts", "quantity": "1", "unit": "lb"},
            {"item": "ground beef", "quantity": "1", "unit": "lb"},
            {"item": "large onion", "quantity": "1", "unit": ""},
            {"item": "tomato soup", "quantity": "1", "unit": "can"},
            {"item": "tomato juice", "quantity": "1", "unit": "cup"},
            {"item": "potato chips", "quantity": "", "unit": ""},
            {"item": "salt and pepper", "quantity": "", "unit": "", "prep_note": "to taste"}
        ],
        "instructions": [
            {"step": 1, "text": "Mix meat with finely chopped onion, season."},
            {"step": 2, "text": "Layer sprouts and meat in greased casserole."},
            {"step": 3, "text": "Pour tomato soup over mixture."},
            {"step": 4, "text": "Bake at 425°F for one hour until tender, adding tomato juice as needed."},
            {"step": 5, "text": "Top with potato chips, bake 10 minutes more."}
        ],
        "temperature": "425°F (220°C)",
        "tags": ["bulrush", "cattail", "casserole", "comfort food", "foraging", "eat the weeds"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "creamed-bulrush-etw",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Creamed Bulrush",
        "category": "sides",
        "attribution": "Eat the Weeds - Green Deane",
        "source_note": "Wild foraging recipe from eattheweeds.com",
        "description": "Tender bulrush shoots in a creamy white sauce.",
        "ingredients": [
            {"item": "tender bulrush shoots", "quantity": "1-2", "unit": "lbs"},
            {"item": "salt", "quantity": "1/2", "unit": "tsp"},
            {"item": "water", "quantity": "1", "unit": "cup"},
            {"item": "butter", "quantity": "3", "unit": "tbsp"},
            {"item": "bulrush flour", "quantity": "3", "unit": "tbsp"},
            {"item": "liquid (milk plus bulrush juice)", "quantity": "3", "unit": "cups"},
            {"item": "sugar", "quantity": "1", "unit": "tbsp"},
            {"item": "pepper", "quantity": "1/4", "unit": "tsp"},
            {"item": "hard-boiled eggs", "quantity": "", "unit": "", "prep_note": "sliced, for garnish"}
        ],
        "instructions": [
            {"step": 1, "text": "Rinse shoots, steam with salt and water until limp. Drain, saving juice."},
            {"step": 2, "text": "Chop shoots finely."},
            {"step": 3, "text": "Melt butter in double boiler, stir in flour."},
            {"step": 4, "text": "Gradually add juice and milk to reach 3 cups liquid, stirring constantly until smooth."},
            {"step": 5, "text": "Season to taste. Garnish with egg slices."}
        ],
        "tags": ["bulrush", "cattail", "creamed", "sides", "foraging", "eat the weeds"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "hunters-stew-bulrush-etw",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Hunter's Stew with Bulrush",
        "category": "main-dishes",
        "attribution": "Eat the Weeds - Green Deane",
        "source_note": "Wild foraging recipe from eattheweeds.com",
        "description": "Hearty stew with beef, wild rice, bacon, and bulrush.",
        "servings_yield": "6 servings",
        "ingredients": [
            {"item": "chopped wild onion", "quantity": "2", "unit": "cups"},
            {"item": "medium bulrush roots", "quantity": "2", "unit": ""},
            {"item": "bacon slices", "quantity": "10", "unit": "", "prep_note": "diced"},
            {"item": "boneless beef chunks", "quantity": "3", "unit": "lbs", "prep_note": "2-inch cubes"},
            {"item": "chopped chives", "quantity": "1", "unit": "tbsp"},
            {"item": "water", "quantity": "2", "unit": "cups"},
            {"item": "dry red wine", "quantity": "1", "unit": "cup", "prep_note": "divided"},
            {"item": "black pepper", "quantity": "1/2", "unit": "tsp"},
            {"item": "wild rice", "quantity": "1", "unit": "cup"},
            {"item": "bulrush shoots", "quantity": "8", "unit": ""},
            {"item": "beef stock", "quantity": "1.5", "unit": "cups"}
        ],
        "instructions": [
            {"step": 1, "text": "Boil bulrush roots in salted water for 30 minutes, drain, scrape and slice into 1/4-inch pieces."},
            {"step": 2, "text": "Cook bacon until crisp, remove to paper towels."},
            {"step": 3, "text": "Cook onions in fat until transparent."},
            {"step": 4, "text": "Add beef, chives, roots, and bacon. Cook 15 minutes."},
            {"step": 5, "text": "Stir in water and wine, season, simmer covered one hour."},
            {"step": 6, "text": "Cook rice separately (30 minutes)."},
            {"step": 7, "text": "Add rice, shoots, and beef stock to skillet, bring to boil, simmer covered 30 minutes."},
            {"step": 8, "text": "Add remaining stock if needed. Garnish with leeks and parsley."}
        ],
        "tags": ["bulrush", "cattail", "stew", "beef", "wild rice", "foraging", "eat the weeds"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    # ===== BURDOCK RECIPES =====
    {
        "id": "dandelion-burdock-beer-etw",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Dandelion and Burdock Beer",
        "category": "beverages",
        "attribution": "Eat the Weeds - Green Deane",
        "source_note": "Wild foraging recipe from eattheweeds.com",
        "description": "Traditional British fermented beverage from foraged roots and leaves.",
        "servings_yield": "About 1 gallon",
        "ingredients": [
            {"item": "young nettles", "quantity": "1", "unit": "lb"},
            {"item": "dandelion leaves", "quantity": "4", "unit": "oz"},
            {"item": "fresh burdock root", "quantity": "4", "unit": "oz", "prep_note": "sliced, or 2 oz dried"},
            {"item": "ginger root", "quantity": "1/2", "unit": "oz", "prep_note": "bruised"},
            {"item": "lemons", "quantity": "2", "unit": ""},
            {"item": "water", "quantity": "1", "unit": "gallon"},
            {"item": "soft brown sugar", "quantity": "1", "unit": "lb", "prep_note": "plus 4 tsp for bottling"},
            {"item": "cream of tartar", "quantity": "1", "unit": "oz"},
            {"item": "brewing yeast", "quantity": "", "unit": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Combine nettles, dandelion leaves, burdock, ginger, and lemon rinds in a large pan with water."},
            {"step": 2, "text": "Bring to boil and simmer 30 minutes."},
            {"step": 3, "text": "Strain liquid into container with lemon juice, 1 lb sugar, and cream of tartar."},
            {"step": 4, "text": "Cool to room temperature."},
            {"step": 5, "text": "Sprinkle in yeast."},
            {"step": 6, "text": "Cover and ferment in warm place for 3 days."},
            {"step": 7, "text": "Bottle, adding 1/2 tsp sugar per pint."},
            {"step": 8, "text": "Age until clear (approximately 1 week)."}
        ],
        "tags": ["beer", "dandelion", "burdock", "fermented", "foraging", "eat the weeds"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "dandelion-burdock-syrup-etw",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Dandelion and Burdock Syrup",
        "category": "preserves",
        "attribution": "Eat the Weeds - Green Deane",
        "source_note": "Wild foraging recipe from eattheweeds.com",
        "description": "Sweet syrup concentrate for making soft drinks.",
        "ingredients": [
            {"item": "water", "quantity": "1.5", "unit": "liters"},
            {"item": "fine ground dandelion root", "quantity": "2", "unit": "tsp"},
            {"item": "fine ground burdock root", "quantity": "1.5", "unit": "tsp"},
            {"item": "root ginger slices", "quantity": "5", "unit": ""},
            {"item": "star anise", "quantity": "1.5", "unit": ""},
            {"item": "citric acid", "quantity": "1", "unit": "tsp"},
            {"item": "orange zest", "quantity": "", "unit": ""},
            {"item": "sugar", "quantity": "750", "unit": "g"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat water and add all ingredients except sugar."},
            {"step": 2, "text": "Simmer 15-20 minutes, then strain."},
            {"step": 3, "text": "Dissolve sugar while hot."},
            {"step": 4, "text": "To serve: Dilute with soda (1:4 ratio)."},
            {"step": 5, "text": "Garnish with borage flowers in summer."}
        ],
        "tags": ["syrup", "dandelion", "burdock", "soft drink", "foraging", "eat the weeds"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "greek-cardune-burdock-etw",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Greek Cardune (Burdock Flower Stalks)",
        "category": "main-dishes",
        "attribution": "Eat the Weeds - Green Deane",
        "source_note": "Wild foraging recipe from eattheweeds.com",
        "description": "Mediterranean-style dish with immature burdock flower stalks and rice.",
        "servings_yield": "6-8 servings",
        "ingredients": [
            {"item": "immature burdock flower stalks", "quantity": "4", "unit": "cups", "prep_note": "sliced"},
            {"item": "water or vegetable stock", "quantity": "2", "unit": "cups"},
            {"item": "red onions", "quantity": "2", "unit": "", "prep_note": "sliced"},
            {"item": "olive oil", "quantity": "1/4", "unit": "cup"},
            {"item": "small tomatoes", "quantity": "4", "unit": "", "prep_note": "sliced"},
            {"item": "carrots", "quantity": "2", "unit": "cups", "prep_note": "sliced"},
            {"item": "basmati brown rice", "quantity": "2/3", "unit": "cup"},
            {"item": "fresh dill", "quantity": "3", "unit": "tbsp", "prep_note": "chopped"},
            {"item": "lemon juice", "quantity": "1", "unit": "lemon"},
            {"item": "salt", "quantity": "2", "unit": "tsp"},
            {"item": "white pepper", "quantity": "1/4", "unit": "tsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Parboil stalks 1 minute in salted water with vinegar and olive oil to reduce bitterness."},
            {"step": 2, "text": "Combine all ingredients and simmer covered 70 minutes until rice is tender."}
        ],
        "tags": ["burdock", "cardune", "greek", "mediterranean", "foraging", "eat the weeds"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    # ===== BEGONIA RECIPES =====
    {
        "id": "begonia-tartlet-etw",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Begonia Tartlet",
        "category": "desserts",
        "attribution": "Eat the Weeds - Green Deane",
        "source_note": "Wild foraging recipe from eattheweeds.com",
        "description": "Unique tart with sour begonia leaves and cream.",
        "servings_yield": "1 tartlet",
        "ingredients": [
            {"item": "edible begonia leaves", "quantity": "2", "unit": "cups"},
            {"item": "sour cream", "quantity": "3", "unit": "oz"},
            {"item": "sugar", "quantity": "1/4-1/2", "unit": "tsp", "prep_note": "to taste"},
            {"item": "pastry or graham cracker tartlet shell", "quantity": "1", "unit": "", "prep_note": "pre-baked"}
        ],
        "instructions": [
            {"step": 1, "text": "Chop the leaves and cook in a pot with approximately 1/2 cup water over medium-low heat until reduced to a thick paste."},
            {"step": 2, "text": "Stir the sour cream and sugar into the paste."},
            {"step": 3, "text": "Transfer mixture to tartlet and bake at 300°F for 30-60 minutes until the filling bubbles gently."},
            {"step": 4, "text": "Cool before serving."}
        ],
        "temperature": "300°F (150°C)",
        "notes": ["This preparation also works with sorrel"],
        "tags": ["begonia", "tartlet", "dessert", "flower", "foraging", "eat the weeds"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "begonia-spread-etw",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Begonia Spread",
        "category": "appetizers",
        "attribution": "Eat the Weeds - Green Deane",
        "source_note": "Wild foraging recipe from eattheweeds.com",
        "description": "Cream cheese spread with strawberry jam and begonia petals.",
        "ingredients": [
            {"item": "soft cream cheese", "quantity": "8", "unit": "oz"},
            {"item": "strawberry jam or similar jelly", "quantity": "1/4-1/3", "unit": "cup"},
            {"item": "fruit juice or liquid", "quantity": "", "unit": "", "prep_note": "as needed for consistency"},
            {"item": "begonia flower petals", "quantity": "1/3", "unit": "cup", "prep_note": "coarsely chopped"}
        ],
        "instructions": [
            {"step": 1, "text": "Combine cream cheese and jelly in a food processor or mixer."},
            {"step": 2, "text": "Add chopped begonia petals and blend until well combined."},
            {"step": 3, "text": "Adjust flower quantity based on personal preference."}
        ],
        "tags": ["begonia", "spread", "cream cheese", "flower", "foraging", "eat the weeds"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    # ===== ALLIGATOR RECIPES =====
    {
        "id": "alligator-nuggets-etw",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Alligator Nuggets",
        "category": "main-dishes",
        "attribution": "Eat the Weeds - Green Deane (Bobby Flay method)",
        "source_note": "Wild foraging recipe from eattheweeds.com",
        "description": "Crispy fried alligator bites with dipping sauces.",
        "ingredients": [
            {"item": "alligator meat", "quantity": "1/2", "unit": "lb", "prep_note": "cut into 1/2-inch cubes"},
            {"item": "fish batter", "quantity": "", "unit": "", "prep_note": "for coating"},
            {"item": "cooking oil", "quantity": "", "unit": "", "prep_note": "for frying"},
            {"item": "salt and pepper", "quantity": "", "unit": "", "prep_note": "to taste"},
            {"item": "dipping sauces", "quantity": "", "unit": "", "prep_note": "remoulade, mustard, or cocktail sauce"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat oil to 360°F in a deep pot."},
            {"step": 2, "text": "Coat meat with fish batter."},
            {"step": 3, "text": "Fry 2-3 minutes until it floats."},
            {"step": 4, "text": "Season with salt and pepper."},
            {"step": 5, "text": "Serve with dipping sauces."}
        ],
        "temperature": "360°F (180°C) oil",
        "notes": ["Soak alligator meat in milk three hours before prepping to reduce swamp notes"],
        "tags": ["alligator", "fried", "cajun", "florida", "foraging", "eat the weeds"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "alligator-sauce-piquant-etw",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Alligator Sauce Piquant",
        "category": "main-dishes",
        "attribution": "Eat the Weeds - Green Deane (Rouses Louisiana's Best)",
        "source_note": "Wild foraging recipe from eattheweeds.com",
        "description": "Classic Louisiana alligator stew in spicy tomato sauce.",
        "ingredients": [
            {"item": "flour", "quantity": "1/2", "unit": "cup"},
            {"item": "cooking oil", "quantity": "1", "unit": "cup"},
            {"item": "large onion", "quantity": "1", "unit": "", "prep_note": "chopped"},
            {"item": "garlic clove", "quantity": "1", "unit": "", "prep_note": "chopped"},
            {"item": "bell pepper", "quantity": "1/2", "unit": "", "prep_note": "chopped"},
            {"item": "large can tomatoes", "quantity": "1", "unit": ""},
            {"item": "tomato sauce", "quantity": "1", "unit": "can"},
            {"item": "water", "quantity": "3", "unit": "cups"},
            {"item": "salt and pepper", "quantity": "", "unit": "", "prep_note": "to taste"},
            {"item": "alligator meat", "quantity": "1", "unit": "lb", "prep_note": "cut into 1-inch cubes"},
            {"item": "chopped onion tops", "quantity": "1/2", "unit": "cup"}
        ],
        "instructions": [
            {"step": 1, "text": "Create roux by cooking flour in oil until medium brown."},
            {"step": 2, "text": "Add onion until wilted."},
            {"step": 3, "text": "Mix in garlic, pepper, tomatoes, sauce, and water; simmer 30 minutes."},
            {"step": 4, "text": "Add alligator, salt, pepper, and onion tops."},
            {"step": 5, "text": "Cook 30-45 minutes until tender."}
        ],
        "notes": ["Remove all yellow fat from alligator before cooking"],
        "tags": ["alligator", "cajun", "louisiana", "stew", "foraging", "eat the weeds"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    # ===== ARMADILLO RECIPES =====
    {
        "id": "baked-armadillo-etw",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Baked Armadillo",
        "category": "main-dishes",
        "attribution": "Eat the Weeds - Green Deane",
        "source_note": "Wild foraging recipe from eattheweeds.com",
        "description": "Whole armadillo baked with fruit stuffing.",
        "ingredients": [
            {"item": "armadillo", "quantity": "1", "unit": "", "prep_note": "removed from shell"},
            {"item": "salt and pepper", "quantity": "", "unit": "", "prep_note": "to taste"},
            {"item": "apple chunks", "quantity": "1.5", "unit": "cups"},
            {"item": "pineapple chunks", "quantity": "1.5", "unit": "cups"},
            {"item": "butter", "quantity": "1/2", "unit": "cup"},
            {"item": "foil", "quantity": "", "unit": "", "prep_note": "for wrapping"}
        ],
        "instructions": [
            {"step": 1, "text": "Wash meat thoroughly."},
            {"step": 2, "text": "Salt and pepper the armadillo."},
            {"step": 3, "text": "Stuff cavity with fruit chunks."},
            {"step": 4, "text": "Coat with butter, wrap in foil, place in roasting pan."},
            {"step": 5, "text": "Bake at 325°F until internal temperature reaches 180°F (approximately 30-45 minutes per pound)."}
        ],
        "temperature": "325°F (165°C)",
        "notes": ["Wear gloves when cleaning due to potential leprosy bacteria risk"],
        "tags": ["armadillo", "baked", "game", "foraging", "eat the weeds"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "armadillo-fricassee-etw",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Armadillo Fricassee",
        "category": "main-dishes",
        "attribution": "Eat the Weeds - Green Deane",
        "source_note": "Wild foraging recipe from eattheweeds.com",
        "description": "Slow-simmered armadillo with vegetables.",
        "ingredients": [
            {"item": "armadillo", "quantity": "1", "unit": "", "prep_note": "cut into pieces"},
            {"item": "medium potatoes", "quantity": "2", "unit": ""},
            {"item": "onions", "quantity": "2", "unit": "", "prep_note": "sliced"},
            {"item": "carrots", "quantity": "2", "unit": "", "prep_note": "coin-chopped"},
            {"item": "celery stalk", "quantity": "1", "unit": "", "prep_note": "chopped"},
            {"item": "bay leaf", "quantity": "1", "unit": ""},
            {"item": "thyme", "quantity": "1/4", "unit": "tsp"},
            {"item": "butter", "quantity": "1/2", "unit": "cup"},
            {"item": "flour", "quantity": "1/2", "unit": "cup"},
            {"item": "salt", "quantity": "1/2", "unit": "tsp"},
            {"item": "pepper", "quantity": "1/4", "unit": "tsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Dust meat in flour, salt, and pepper."},
            {"step": 2, "text": "Brown both sides in butter."},
            {"step": 3, "text": "Add water to cover vegetables."},
            {"step": 4, "text": "Add potatoes, onions, carrots, celery, bay leaf, and thyme."},
            {"step": 5, "text": "Cover and simmer approximately 2 hours until tender."},
            {"step": 6, "text": "Thicken sauce with seasoned flour and water mixture."}
        ],
        "tags": ["armadillo", "fricassee", "stew", "game", "foraging", "eat the weeds"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "armadillo-chili-etw",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Armadillo Chili",
        "category": "main-dishes",
        "attribution": "Eat the Weeds - Green Deane",
        "source_note": "Wild foraging recipe from eattheweeds.com",
        "description": "Hearty chili made with armadillo meat.",
        "ingredients": [
            {"item": "armadillo", "quantity": "3.5-4", "unit": "lbs", "prep_note": "cubed 1/4-inch"},
            {"item": "diced onion", "quantity": "2", "unit": "cups"},
            {"item": "garlic cloves", "quantity": "3", "unit": "", "prep_note": "minced"},
            {"item": "black pepper", "quantity": "1/2", "unit": "tsp"},
            {"item": "vegetable oil", "quantity": "1/4", "unit": "cup"},
            {"item": "crushed tomatoes", "quantity": "28", "unit": "oz"},
            {"item": "water or beer", "quantity": "1.75", "unit": "cups"},
            {"item": "dried red chili pod", "quantity": "1", "unit": ""},
            {"item": "oregano", "quantity": "1/2", "unit": "tsp"},
            {"item": "green bell peppers", "quantity": "2", "unit": "medium", "prep_note": "diced"},
            {"item": "salt", "quantity": "2", "unit": "tsp"},
            {"item": "sugar", "quantity": "1", "unit": "tbsp"},
            {"item": "canned tomatoes", "quantity": "28", "unit": "oz"},
            {"item": "tomato paste", "quantity": "12", "unit": "oz"},
            {"item": "ground cumin", "quantity": "1", "unit": "tsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Remove stem and seeds from chili pod. Toast pod over medium-low heat until crisp. Cool, then crumble into powder."},
            {"step": 2, "text": "Heat oil, brown meat in batches, remove."},
            {"step": 3, "text": "Sauté onions, peppers, garlic, and powdered chili until tender."},
            {"step": 4, "text": "Add remaining ingredients and browned meat."},
            {"step": 5, "text": "Bring to boil, reduce heat, cover, and simmer 1 hour, stirring frequently until tender."},
            {"step": 6, "text": "Serve with hot sauce, salsa, and cheese garnish."}
        ],
        "tags": ["armadillo", "chili", "game", "foraging", "eat the weeds"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "armadillo-meatloaf-etw",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Armadillo Meatloaf",
        "category": "main-dishes",
        "attribution": "Eat the Weeds - Green Deane",
        "source_note": "Wild foraging recipe from eattheweeds.com",
        "description": "Classic meatloaf made with ground armadillo.",
        "ingredients": [
            {"item": "ground armadillo meat", "quantity": "1.5", "unit": "lbs"},
            {"item": "beaten eggs", "quantity": "2", "unit": ""},
            {"item": "dry bread crumbs", "quantity": "1/8", "unit": "cup"},
            {"item": "evaporated milk", "quantity": "1", "unit": "cup"},
            {"item": "onion", "quantity": "1/4", "unit": "", "prep_note": "minced"},
            {"item": "thyme", "quantity": "1/4", "unit": "tsp"},
            {"item": "salt", "quantity": "1", "unit": "tsp"},
            {"item": "pepper", "quantity": "1/4", "unit": "tsp"},
            {"item": "Worcestershire sauce", "quantity": "1", "unit": "tsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Soak meat overnight in salted water. Remove from bones and grind."},
            {"step": 2, "text": "Mix thoroughly with all ingredients."},
            {"step": 3, "text": "Place in loaf dish in hot water bath."},
            {"step": 4, "text": "Bake at 350°F for 1.25 to 2 hours."}
        ],
        "temperature": "350°F (175°C)",
        "tags": ["armadillo", "meatloaf", "game", "foraging", "eat the weeds"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    # ===== BITTER MELON RECIPES =====
    {
        "id": "karela-bhaji-etw",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Karela Bhaji (Pan-fried Bitter Melon)",
        "category": "sides",
        "attribution": "Eat the Weeds - Green Deane",
        "source_note": "Wild foraging recipe from eattheweeds.com",
        "description": "Indian-style pan-fried bitter melon with aromatic spices.",
        "ingredients": [
            {"item": "Indian or Chinese bitter melon", "quantity": "1", "unit": "lb"},
            {"item": "salt", "quantity": "1.5", "unit": "tsp", "prep_note": "divided"},
            {"item": "ghee", "quantity": "1", "unit": "tbsp"},
            {"item": "avocado oil", "quantity": "2", "unit": "tbsp"},
            {"item": "cumin seeds", "quantity": "1/2", "unit": "tsp"},
            {"item": "fennel seeds", "quantity": "1/4", "unit": "tsp"},
            {"item": "ginger", "quantity": "1", "unit": "inch", "prep_note": "grated"},
            {"item": "garlic cloves", "quantity": "2", "unit": "", "prep_note": "minced"},
            {"item": "onion", "quantity": "1", "unit": "", "prep_note": "finely chopped"},
            {"item": "garam masala", "quantity": "1/2", "unit": "tsp"},
            {"item": "ground coriander", "quantity": "1/2", "unit": "tsp"},
            {"item": "ground turmeric", "quantity": "1/4", "unit": "tsp"},
            {"item": "Kashmiri red chili powder", "quantity": "1/4", "unit": "tsp"},
            {"item": "black pepper", "quantity": "1/4", "unit": "tsp"},
            {"item": "amchur (green mango) powder", "quantity": "1", "unit": "tsp"},
            {"item": "coconut palm sugar", "quantity": "2", "unit": "tsp"},
            {"item": "chicken stock", "quantity": "1/2", "unit": "cup"},
            {"item": "fresh cilantro", "quantity": "", "unit": "", "prep_note": "for garnish"}
        ],
        "instructions": [
            {"step": 1, "text": "Halve melon lengthwise; scrape out seeds and pith. Slice into 1/4-inch pieces."},
            {"step": 2, "text": "Sprinkle with 1 tsp salt in a colander; drain 30 minutes. Squeeze and blot dry."},
            {"step": 3, "text": "Warm ghee and oil until shimmering; toast cumin and fennel seeds ~30 seconds."},
            {"step": 4, "text": "Add garlic and ginger; sauté 30 seconds."},
            {"step": 5, "text": "Reduce heat to medium; add onion, coriander, turmeric, chili, pepper, and remaining salt. Sauté 6 minutes until softened."},
            {"step": 6, "text": "Stir in melon and stock; sauté until tender and liquid mostly evaporates (~10 minutes), stirring often."},
            {"step": 7, "text": "Add amchur and sugar; increase heat to high."},
            {"step": 8, "text": "Pan-fry until liquid evaporates and melon crisps (~3 minutes), stirring frequently."},
            {"step": 9, "text": "Season to taste; serve with cilantro."}
        ],
        "tags": ["bitter melon", "karela", "indian", "vegetable", "foraging", "eat the weeds"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "bitter-melon-salad-etw",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Bitter Melon Salad (Philippine Style)",
        "category": "salads",
        "attribution": "Eat the Weeds - Green Deane",
        "source_note": "Wild foraging recipe from eattheweeds.com",
        "description": "Fresh Philippine-style bitter melon salad with tomatoes.",
        "ingredients": [
            {"item": "bitter melon gourds", "quantity": "", "unit": ""},
            {"item": "salt", "quantity": "", "unit": ""},
            {"item": "tomatoes", "quantity": "", "unit": "", "prep_note": "cut into wedges"},
            {"item": "onion", "quantity": "", "unit": "", "prep_note": "thinly sliced"},
            {"item": "vinaigrette", "quantity": "", "unit": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Halve gourds lengthwise and scoop out seeds with a spoon."},
            {"step": 2, "text": "Cut into half-moon pieces and toss with salt; let sit to remove bitterness."},
            {"step": 3, "text": "Slice tomatoes into wedges and onion thinly."},
            {"step": 4, "text": "Rinse salt from melon and combine with tomatoes and onions."},
            {"step": 5, "text": "Dress with vinaigrette and chill before serving."}
        ],
        "tags": ["bitter melon", "salad", "philippine", "vegetable", "foraging", "eat the weeds"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    # ===== CHAYA RECIPE =====
    {
        "id": "chaya-soup-etw",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Chaya Soup",
        "category": "soups",
        "attribution": "Eat the Weeds - Green Deane",
        "source_note": "Wild foraging recipe from eattheweeds.com",
        "description": "Creamy soup made with chaya (tree spinach) leaves.",
        "ingredients": [
            {"item": "tender chaya leaves", "quantity": "20", "unit": "", "prep_note": "washed"},
            {"item": "organic whole milk", "quantity": "2", "unit": "cups"},
            {"item": "fresh basil leaves", "quantity": "4", "unit": ""},
            {"item": "crushed garlic clove", "quantity": "1", "unit": ""},
            {"item": "small onion", "quantity": "1", "unit": "", "prep_note": "diced"},
            {"item": "vegetable bouillon", "quantity": "1", "unit": "cup"},
            {"item": "salt and pepper", "quantity": "", "unit": "", "prep_note": "to taste"},
            {"item": "unsweetened cream", "quantity": "2", "unit": "tbsp", "prep_note": "for garnish"}
        ],
        "instructions": [
            {"step": 1, "text": "Place chopped chaya leaves, onions, and garlic in a pot with vegetable bouillon."},
            {"step": 2, "text": "Cook 10 minutes on medium heat until leaves are blanched."},
            {"step": 3, "text": "Add milk and allow to cool slightly."},
            {"step": 4, "text": "Blend remaining ingredients until smooth, return to pot."},
            {"step": 5, "text": "Heat 5-10 minutes until hot (do not boil)."},
            {"step": 6, "text": "Serve with cream drizzled on top and optional crushed dried red chili."}
        ],
        "notes": ["Cook chaya for at least 10-20 minutes to eliminate hydrogen cyanide", "Avoid aluminum cookware - use glass or pottery"],
        "tags": ["chaya", "soup", "tree spinach", "tropical", "foraging", "eat the weeds"],
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

    for recipe in ETW_BATCH3_RECIPES:
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
    print(f"  Added: {added} new Eat the Weeds recipes (batch 3)")
    print(f"  Skipped: {skipped} duplicates")
    print(f"  Total recipes now: {len(recipes)}")


if __name__ == "__main__":
    main()
