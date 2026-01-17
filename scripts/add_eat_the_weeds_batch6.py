#!/usr/bin/env python3
"""
Add Eat the Weeds recipes - Batch 6
Recipes from: garlic mustard, banana, bulrush, hornworms, mole crickets
"""

import json
from pathlib import Path

RECIPES_FILE = Path(__file__).parent.parent / "data" / "recipes.json"

ETW_BATCH6_RECIPES = [
    # ===== GARLIC MUSTARD =====
    {
        "id": "garlic-mustard-vichyssoisse-etw",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Garlic Mustard Vichyssoisse",
        "category": "soups",
        "attribution": "Eat the Weeds",
        "source_note": "From eattheweeds.com - Garlic Mustard article",
        "description": "A cold soup featuring foraged garlic mustard (jack-by-the-hedge) and three-cornered garlic.",
        "servings_yield": "4 servings",
        "prep_time": "30 minutes",
        "cook_time": "10 minutes",
        "ingredients": [
            {"item": "butter", "quantity": "75", "unit": "g"},
            {"item": "onion", "quantity": "1", "unit": "", "prep_note": "chopped"},
            {"item": "three-cornered garlic stems", "quantity": "75", "unit": "g"},
            {"item": "water", "quantity": "800", "unit": "ml"},
            {"item": "potato", "quantity": "1", "unit": "large", "prep_note": "peeled, diced, rinsed"},
            {"item": "salt", "quantity": "", "unit": "", "prep_note": "to taste"},
            {"item": "black pepper", "quantity": "", "unit": "", "prep_note": "freshly ground, to taste"},
            {"item": "garlic mustard (jack-by-the-hedge)", "quantity": "75", "unit": "g"},
            {"item": "goat's cheese", "quantity": "75", "unit": "g"},
            {"item": "milk", "quantity": "75", "unit": "ml", "prep_note": "for foam"},
            {"item": "cumin", "quantity": "1", "unit": "pinch"},
            {"item": "white pepper", "quantity": "1", "unit": "pinch"}
        ],
        "instructions": [
            {"step": 1, "text": "In a heavy bottomed pan, add water and potatoes with a good pinch of salt. Boil until potatoes are soft. Remove from heat and set aside."},
            {"step": 2, "text": "Melt butter in a medium saucepan. Add the onion and cook until softened. Pour over the boiled potatoes and water."},
            {"step": 3, "text": "Blitz in food processor until smooth. Add water if needed to reach desired consistency. Pass through a sieve."},
            {"step": 4, "text": "Chill in the refrigerator. Check seasoning."},
            {"step": 5, "text": "Blanch jack-by-the-hedge for 10 seconds in salted boiling water and refresh in ice water."},
            {"step": 6, "text": "Add jack-by-the-hedge and blitz again until smooth."},
            {"step": 7, "text": "Add the three-cornered garlic, blitz until smooth, and check seasoning again."},
            {"step": 8, "text": "Serve with crumbled goat's cheese, frothed milk, a pinch of cumin, crispy fried nettle dusted with white pepper, and a three-cornered garlic flower."}
        ],
        "temperature": "",
        "pan_size": "",
        "notes": ["Serve cold", "Garlic mustard is also known as jack-by-the-hedge or sauce-alone"],
        "tags": ["soup", "cold soup", "foraged", "garlic mustard", "wild greens", "vichyssoisse"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },

    # ===== BANANA RECIPES =====
    {
        "id": "sauteed-banana-tree-stem-etw",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Sautéed Banana Tree Stem",
        "category": "vegetables",
        "attribution": "Eat the Weeds",
        "source_note": "From eattheweeds.com - Bananas article",
        "description": "A South Indian style preparation using the edible core of banana tree stems.",
        "servings_yield": "4 servings",
        "prep_time": "20 minutes",
        "cook_time": "1 hour",
        "ingredients": [
            {"item": "banana tree stem center core", "quantity": "1", "unit": "lb"},
            {"item": "grated coconut", "quantity": "1/4", "unit": "coconut"},
            {"item": "garlic cloves", "quantity": "6", "unit": ""},
            {"item": "chili powder", "quantity": "1/4", "unit": "tsp"},
            {"item": "curry leaves", "quantity": "1.5", "unit": "tsp"},
            {"item": "salt", "quantity": "", "unit": "", "prep_note": "to taste"},
            {"item": "mustard seeds", "quantity": "1/2", "unit": "tsp"},
            {"item": "coconut oil", "quantity": "1", "unit": "tbsp"},
            {"item": "turmeric", "quantity": "1/4", "unit": "tsp", "prep_note": "optional, for color"}
        ],
        "instructions": [
            {"step": 1, "text": "Remove outer fiber layer from banana stem and chop finely."},
            {"step": 2, "text": "Wash and drain."},
            {"step": 3, "text": "Heat half the oil; add mustard seeds until crackling."},
            {"step": 4, "text": "Add chopped banana stem, curry leaves, salt, and chili powder. Optionally add turmeric for color."},
            {"step": 5, "text": "Cover and simmer until soft, approximately one hour."},
            {"step": 6, "text": "Blend grated coconut and garlic together."},
            {"step": 7, "text": "Add coconut-garlic mixture when stem is nearly cooked; keep covered until fully cooked."},
            {"step": 8, "text": "Drizzle remaining coconut oil over finished dish and mix."},
            {"step": 9, "text": "Let sit covered briefly before serving."}
        ],
        "temperature": "",
        "pan_size": "",
        "notes": ["Use only the tender inner core of the banana stem"],
        "tags": ["vegetable", "banana", "indian", "coconut", "vegan"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "banana-flower-stir-fry-etw",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Banana Flower Stir Fry",
        "category": "vegetables",
        "attribution": "Eat the Weeds",
        "source_note": "From eattheweeds.com - Bananas article",
        "description": "An Indian-style stir fry using banana flower with lentils and coconut.",
        "servings_yield": "4 servings",
        "prep_time": "30 minutes",
        "cook_time": "15 minutes",
        "ingredients": [
            {"item": "banana flower", "quantity": "1", "unit": ""},
            {"item": "lentils", "quantity": "1/2", "unit": "cup"},
            {"item": "onion", "quantity": "1", "unit": "small"},
            {"item": "green chillies", "quantity": "5", "unit": "", "prep_note": "adjust to taste"},
            {"item": "garlic", "quantity": "1", "unit": "clove"},
            {"item": "cumin powder", "quantity": "1/4", "unit": "tsp"},
            {"item": "turmeric powder", "quantity": "1", "unit": "pinch"},
            {"item": "grated coconut", "quantity": "1/2", "unit": "cup"},
            {"item": "oil", "quantity": "1", "unit": "tbsp"},
            {"item": "mustard seeds", "quantity": "", "unit": "", "prep_note": "for tempering"},
            {"item": "dry red chillies", "quantity": "", "unit": "", "prep_note": "for tempering"},
            {"item": "curry leaves", "quantity": "", "unit": "", "prep_note": "as desired"},
            {"item": "salt", "quantity": "", "unit": "", "prep_note": "to taste"}
        ],
        "instructions": [
            {"step": 1, "text": "Cook lentils and set aside."},
            {"step": 2, "text": "Remove outer petals of banana flower until reaching cream-colored edible interior; chop finely."},
            {"step": 3, "text": "Apply coconut oil to palm and rub chopped flower to remove lumps; repeat until smooth."},
            {"step": 4, "text": "Dice garlic."},
            {"step": 5, "text": "Heat oil and splutter mustard seeds; add dry red chillies, onion, green chillies, and curry leaves; sauté until onions turn light brown."},
            {"step": 6, "text": "Add prepared flower, garlic, cumin, salt, and turmeric; cook covered 5 minutes on medium heat without adding water."},
            {"step": 7, "text": "Add cooked lentils and mix well."},
            {"step": 8, "text": "Cook another 5 minutes until completely dry."}
        ],
        "temperature": "",
        "pan_size": "",
        "notes": ["Chopped banana flower can be soaked in milk beforehand to reduce bitterness"],
        "tags": ["vegetable", "banana flower", "indian", "lentils", "stir fry", "vegan"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },

    # ===== BULRUSH RECIPES =====
    {
        "id": "roasted-bulrush-roots-etw",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Roasted Bulrush Roots",
        "category": "vegetables",
        "attribution": "Eat the Weeds",
        "source_note": "From eattheweeds.com - Bulrush Bonanza",
        "description": "Primitive pit-roasted bulrush roots wrapped in leaves.",
        "servings_yield": "varies",
        "prep_time": "15 minutes",
        "cook_time": "2-3 hours",
        "ingredients": [
            {"item": "bulrush roots", "quantity": "", "unit": "", "prep_note": "cleaned"},
            {"item": "large leaves", "quantity": "", "unit": "", "prep_note": "for wrapping"}
        ],
        "instructions": [
            {"step": 1, "text": "Clean roots thoroughly, remove hair roots by scraping."},
            {"step": 2, "text": "Wrap roots in large leaves."},
            {"step": 3, "text": "Dig an 18-inch hole, 6 inches deep."},
            {"step": 4, "text": "Build fire and create coal bed."},
            {"step": 5, "text": "Place wrapped roots inside and cover with coals."},
            {"step": 6, "text": "Roast for 2 to 3 hours."}
        ],
        "temperature": "",
        "pan_size": "",
        "notes": ["Traditional primitive cooking method"],
        "tags": ["bulrush", "foraged", "primitive cooking", "roots", "survival"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "bulrush-stew-etw",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Bulrush Stew",
        "category": "soups",
        "attribution": "Eat the Weeds",
        "source_note": "From eattheweeds.com - Bulrush Bonanza",
        "description": "A simple stew with bulrush roots and wild game.",
        "servings_yield": "varies",
        "prep_time": "15 minutes",
        "cook_time": "1 hour",
        "ingredients": [
            {"item": "bulrush roots", "quantity": "", "unit": "", "prep_note": "peeled, cut into 1-inch pieces"},
            {"item": "wild onions or mint", "quantity": "", "unit": ""},
            {"item": "porcupine or small game", "quantity": "", "unit": ""},
            {"item": "water", "quantity": "", "unit": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Peel root skin and cut into inch-long pieces."},
            {"step": 2, "text": "Boil with water, onions or mint, and meat for one hour."}
        ],
        "temperature": "",
        "pan_size": "",
        "notes": ["Traditional survival recipe"],
        "tags": ["bulrush", "stew", "foraged", "wild game", "survival"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "bulrush-flour-etw",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Bulrush Flour",
        "category": "preserves",
        "attribution": "Eat the Weeds",
        "source_note": "From eattheweeds.com - Bulrush Bonanza",
        "description": "How to make flour from dried bulrush roots.",
        "servings_yield": "varies",
        "prep_time": "varies",
        "cook_time": "",
        "ingredients": [
            {"item": "bulrush roots", "quantity": "", "unit": "", "prep_note": "cleaned"}
        ],
        "instructions": [
            {"step": 1, "text": "Clean roots thoroughly."},
            {"step": 2, "text": "Dry roots completely in sun."},
            {"step": 3, "text": "Remove fibers."},
            {"step": 4, "text": "Pound pulp into flour. The texture depends upon how much elbow grease you use."}
        ],
        "temperature": "",
        "pan_size": "",
        "notes": ["Can be used in place of regular flour in recipes"],
        "tags": ["bulrush", "flour", "foraged", "survival", "preservation"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "bulrush-pancakes-etw",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Bulrush Pancakes",
        "category": "breads",
        "attribution": "Eat the Weeds",
        "source_note": "From eattheweeds.com - Bulrush Bonanza",
        "description": "Primitive pancakes made from bulrush root gruel.",
        "servings_yield": "varies",
        "prep_time": "30 minutes",
        "cook_time": "varies",
        "ingredients": [
            {"item": "bulrush roots", "quantity": "", "unit": "", "prep_note": "peeled and cut"},
            {"item": "water", "quantity": "", "unit": ""},
            {"item": "porcupine fat or oil", "quantity": "", "unit": ""},
            {"item": "porcupine or bacon", "quantity": "", "unit": "", "prep_note": "chopped"},
            {"item": "berries", "quantity": "", "unit": "", "prep_note": "optional"}
        ],
        "instructions": [
            {"step": 1, "text": "Peel and cut roots."},
            {"step": 2, "text": "Boil into gruel and let cool."},
            {"step": 3, "text": "Mix with fat and meat."},
            {"step": 4, "text": "Form into patties."},
            {"step": 5, "text": "Fry on heated stones."}
        ],
        "temperature": "",
        "pan_size": "",
        "notes": ["Add berries for sweetness if desired"],
        "tags": ["bulrush", "pancakes", "foraged", "primitive cooking", "survival"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "bulrush-bread-etw",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Bulrush Bread",
        "category": "breads",
        "attribution": "Eat the Weeds",
        "source_note": "From eattheweeds.com - Bulrush Bonanza",
        "description": "Primitive bread made from bulrush root flour.",
        "servings_yield": "varies",
        "prep_time": "1 hour",
        "cook_time": "varies",
        "ingredients": [
            {"item": "bulrush roots", "quantity": "", "unit": "", "prep_note": "skinned and cut"},
            {"item": "fat", "quantity": "", "unit": ""},
            {"item": "flat rock", "quantity": "1", "unit": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Skin and cut roots."},
            {"step": 2, "text": "Boil into gruel."},
            {"step": 3, "text": "Remove fibers."},
            {"step": 4, "text": "Evaporate water to create sweet flour."},
            {"step": 5, "text": "Mix with fat."},
            {"step": 6, "text": "Roll onto flat rock and bake in reflector oven, or twist around stick and roast."}
        ],
        "temperature": "",
        "pan_size": "",
        "notes": ["The flour becomes naturally sweet as water evaporates"],
        "tags": ["bulrush", "bread", "foraged", "primitive cooking", "survival"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "bulrush-broth-etw",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Bulrush Broth",
        "category": "soups",
        "attribution": "Eat the Weeds",
        "source_note": "From eattheweeds.com - Bulrush Bonanza",
        "description": "A hearty oxtail broth with bulrush shoots and wild rice.",
        "servings_yield": "6 servings",
        "prep_time": "20 minutes",
        "cook_time": "1.5 hours",
        "ingredients": [
            {"item": "oxtail", "quantity": "1.5", "unit": "lb"},
            {"item": "salt", "quantity": "1.5", "unit": "tsp"},
            {"item": "flour", "quantity": "1/2", "unit": "cup"},
            {"item": "bulrush flour", "quantity": "2", "unit": "tbsp"},
            {"item": "mustard seed", "quantity": "2", "unit": "tbsp"},
            {"item": "bacon fat", "quantity": "2", "unit": "tbsp"},
            {"item": "water", "quantity": "6", "unit": "cups"},
            {"item": "bulrush shoots", "quantity": "1/2", "unit": "cup"},
            {"item": "wild onions", "quantity": "3", "unit": ""},
            {"item": "wild rice", "quantity": "1/4", "unit": "cup"},
            {"item": "bulrush roots", "quantity": "3", "unit": "", "prep_note": "sliced"},
            {"item": "Worcestershire sauce", "quantity": "1", "unit": "tbsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Roll meat in flour and salt mixture."},
            {"step": 2, "text": "Sauté meat in bacon fat until browned."},
            {"step": 3, "text": "Add water, shoots, and onions."},
            {"step": 4, "text": "Cover and simmer 1½ hours or until wild rice is tender."}
        ],
        "temperature": "",
        "pan_size": "",
        "notes": ["Use bulrush flour to thicken"],
        "tags": ["bulrush", "broth", "soup", "oxtail", "wild rice", "foraged"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "bulrush-casserole-etw",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Bulrush Casserole",
        "category": "casseroles",
        "attribution": "Eat the Weeds",
        "source_note": "From eattheweeds.com - Bulrush Bonanza",
        "description": "A modern casserole with bulrush sprouts, ground beef, and tomato soup.",
        "servings_yield": "6 servings",
        "prep_time": "15 minutes",
        "cook_time": "1 hour 10 minutes",
        "ingredients": [
            {"item": "small bulrush sprouts", "quantity": "1", "unit": "lb"},
            {"item": "ground beef", "quantity": "1", "unit": "lb"},
            {"item": "onion", "quantity": "1", "unit": "large"},
            {"item": "tomato soup", "quantity": "1", "unit": "can"},
            {"item": "tomato juice", "quantity": "1", "unit": "cup"},
            {"item": "potato chips", "quantity": "", "unit": "", "prep_note": "for topping"},
            {"item": "salt", "quantity": "", "unit": "", "prep_note": "to taste"},
            {"item": "pepper", "quantity": "", "unit": "", "prep_note": "to taste"}
        ],
        "instructions": [
            {"step": 1, "text": "Mix meat with chopped onion and season with salt and pepper."},
            {"step": 2, "text": "Layer sprouts and meat in greased casserole."},
            {"step": 3, "text": "Pour soup over mixture."},
            {"step": 4, "text": "Bake at 425°F for about an hour until tender, adding tomato juice as needed."},
            {"step": 5, "text": "Top with potato chips and bake 10 minutes more."}
        ],
        "temperature": "425°F (220°C)",
        "pan_size": "casserole dish",
        "notes": ["Add tomato juice during baking if casserole seems dry"],
        "tags": ["bulrush", "casserole", "ground beef", "foraged"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "creamed-bulrush-etw",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Creamed Bulrush",
        "category": "vegetables",
        "attribution": "Eat the Weeds",
        "source_note": "From eattheweeds.com - Bulrush Bonanza",
        "description": "Tender bulrush shoots in a creamy sauce, garnished with hard-boiled eggs.",
        "servings_yield": "6 servings",
        "prep_time": "15 minutes",
        "cook_time": "20 minutes",
        "ingredients": [
            {"item": "tender bulrush shoots", "quantity": "12", "unit": "lb"},
            {"item": "salt", "quantity": "1/2", "unit": "tsp"},
            {"item": "water", "quantity": "1", "unit": "cup"},
            {"item": "butter", "quantity": "3", "unit": "tbsp"},
            {"item": "bulrush flour", "quantity": "3", "unit": "tbsp"},
            {"item": "liquid (milk and bulrush juice)", "quantity": "3", "unit": "cups"},
            {"item": "sugar", "quantity": "1", "unit": "tbsp"},
            {"item": "pepper", "quantity": "1/4", "unit": "tsp"},
            {"item": "hard-boiled eggs", "quantity": "", "unit": "", "prep_note": "sliced, for garnish"}
        ],
        "instructions": [
            {"step": 1, "text": "Steam shoots with salt and water until tender. Drain and save juice."},
            {"step": 2, "text": "Chop shoots finely."},
            {"step": 3, "text": "Melt butter in saucepan."},
            {"step": 4, "text": "Stir in bulrush flour."},
            {"step": 5, "text": "Gradually add bulrush juice and milk (3 cups total)."},
            {"step": 6, "text": "Stir constantly until smooth."},
            {"step": 7, "text": "Season to taste with sugar and pepper."},
            {"step": 8, "text": "Garnish with sliced hard-boiled eggs."}
        ],
        "temperature": "",
        "pan_size": "",
        "notes": ["Reserve cooking liquid from shoots to use in sauce"],
        "tags": ["bulrush", "creamed vegetable", "foraged", "side dish"],
        "confidence": {"overall": "medium", "flags": ["12 lb shoots seems like a lot - may be a typo"]},
        "image_refs": []
    },
    {
        "id": "hunters-stew-bulrush-etw",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Hunters' Stew with Bulrush",
        "category": "main dishes",
        "attribution": "Eat the Weeds",
        "source_note": "From eattheweeds.com - Bulrush Bonanza",
        "description": "A hearty hunters' stew with beef, bacon, bulrush roots and shoots, and wild rice.",
        "servings_yield": "6 servings",
        "prep_time": "30 minutes",
        "cook_time": "2 hours",
        "ingredients": [
            {"item": "wild onion", "quantity": "2", "unit": "cups", "prep_note": "chopped"},
            {"item": "bulrush roots", "quantity": "2", "unit": "medium"},
            {"item": "bacon", "quantity": "10", "unit": "slices", "prep_note": "diced"},
            {"item": "beef chunks", "quantity": "3", "unit": "lb"},
            {"item": "chives", "quantity": "1", "unit": "tbsp", "prep_note": "chopped"},
            {"item": "water", "quantity": "2", "unit": "cups"},
            {"item": "dry red wine", "quantity": "1/2", "unit": "cup"},
            {"item": "black pepper", "quantity": "1/2", "unit": "tsp"},
            {"item": "wild rice", "quantity": "1", "unit": "cup"},
            {"item": "bulrush shoots", "quantity": "8", "unit": ""},
            {"item": "beef stock", "quantity": "1.5", "unit": "cups"}
        ],
        "instructions": [
            {"step": 1, "text": "Boil bulrush roots for 30 minutes, then slice."},
            {"step": 2, "text": "Cook bacon until crisp and remove from pan."},
            {"step": 3, "text": "Sauté onions in bacon fat until softened."},
            {"step": 4, "text": "Add beef, chives, and sliced roots. Cook 15 minutes."},
            {"step": 5, "text": "Return bacon to pan. Add water and wine."},
            {"step": 6, "text": "Simmer covered for about an hour."},
            {"step": 7, "text": "Cook wild rice separately for 30 minutes."},
            {"step": 8, "text": "Stir rice, bulrush shoots, and beef stock into stew."},
            {"step": 9, "text": "Simmer 30 minutes more. Taste and adjust seasoning, add more stock if needed."}
        ],
        "temperature": "",
        "pan_size": "large skillet or Dutch oven",
        "notes": ["Garnish with leeks and parsley"],
        "tags": ["bulrush", "stew", "hunters stew", "beef", "bacon", "wild rice", "foraged"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },

    # ===== INSECT RECIPES =====
    {
        "id": "fried-hornworms-tomatoes-basil-etw",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Fried Hornworms with Tomatoes and Basil",
        "category": "main dishes",
        "attribution": "Eat the Weeds / David George Gordon",
        "source_note": "From eattheweeds.com - Tomato Tobacco Hornworms, credited to Eat-a-Bug Cookbook",
        "description": "Pan-fried tomato hornworms served atop fried green tomatoes with fresh basil.",
        "servings_yield": "4 servings",
        "prep_time": "20 minutes",
        "cook_time": "15 minutes",
        "ingredients": [
            {"item": "olive oil", "quantity": "3", "unit": "tbsp"},
            {"item": "tomato hornworms", "quantity": "16", "unit": "", "prep_note": "purged"},
            {"item": "basil leaves", "quantity": "16", "unit": ""},
            {"item": "green tomatoes", "quantity": "4", "unit": "medium", "prep_note": "sliced 1/4 inch thick"},
            {"item": "white cornmeal", "quantity": "", "unit": "", "prep_note": "for coating"},
            {"item": "salt", "quantity": "", "unit": "", "prep_note": "to taste"},
            {"item": "pepper", "quantity": "", "unit": "", "prep_note": "to taste"}
        ],
        "instructions": [
            {"step": 1, "text": "Lightly fry the hornworms in a pan for a few minutes, being careful not to rupture the exoskeleton with high heat. Set aside to drain."},
            {"step": 2, "text": "Sprinkle tomato slices with salt and pepper, then coat with cornmeal."},
            {"step": 3, "text": "Fry tomato slices on both sides until lightly brown."},
            {"step": 4, "text": "Top each tomato slice with one to two hornworms."},
            {"step": 5, "text": "Crown each hornworm with a basil leaf."}
        ],
        "temperature": "",
        "pan_size": "",
        "notes": ["Hornworms should be purged (fed clean food) before cooking", "Use low to medium heat to prevent rupturing"],
        "tags": ["insects", "entomophagy", "hornworms", "fried green tomatoes", "unusual protein"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "classic-kamaro-mole-cricket-etw",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Classic Kamaro (Mole Cricket)",
        "category": "main dishes",
        "attribution": "Eat the Weeds",
        "source_note": "From eattheweeds.com - Mole Crickets article",
        "description": "Traditional Filipino preparation of mole crickets, known as kamaro.",
        "servings_yield": "varies",
        "prep_time": "30 minutes",
        "cook_time": "20 minutes",
        "ingredients": [
            {"item": "mole crickets", "quantity": "", "unit": "", "prep_note": "cleaned"},
            {"item": "vinegar", "quantity": "", "unit": "", "prep_note": "for boiling"},
            {"item": "garlic", "quantity": "", "unit": "", "prep_note": "for boiling"},
            {"item": "oil", "quantity": "", "unit": "", "prep_note": "for sautéing"},
            {"item": "onion", "quantity": "", "unit": "", "prep_note": "chopped"},
            {"item": "tomatoes", "quantity": "", "unit": "", "prep_note": "chopped"},
            {"item": "cold beer", "quantity": "", "unit": "", "prep_note": "for serving"}
        ],
        "instructions": [
            {"step": 1, "text": "Boil the mole crickets in vinegar and garlic."},
            {"step": 2, "text": "Drain the crickets."},
            {"step": 3, "text": "Remove legs, wings, and claws."},
            {"step": 4, "text": "Sauté the bodies in oil with chopped onion and tomatoes until they reach a chocolate brown color."},
            {"step": 5, "text": "Serve with cold beer on the side."}
        ],
        "temperature": "",
        "pan_size": "",
        "notes": ["Result should be crispy on the outside, moist in the middle", "A traditional Filipino delicacy from Pampanga province"],
        "tags": ["insects", "entomophagy", "mole cricket", "kamaro", "filipino", "unusual protein"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "philippine-style-kamaro-etw",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Philippine-Style Kamaro (Adobo Style)",
        "category": "main dishes",
        "attribution": "Eat the Weeds",
        "source_note": "From eattheweeds.com - Mole Crickets article",
        "description": "Mole crickets prepared adobo-style with soy sauce, vinegar, and optional coconut milk.",
        "servings_yield": "varies",
        "prep_time": "30 minutes",
        "cook_time": "20 minutes",
        "ingredients": [
            {"item": "mole crickets", "quantity": "", "unit": "", "prep_note": "scratchy parts removed"},
            {"item": "garlic", "quantity": "", "unit": "", "prep_note": "minced"},
            {"item": "onions", "quantity": "", "unit": "", "prep_note": "sliced"},
            {"item": "soy sauce", "quantity": "", "unit": ""},
            {"item": "vinegar", "quantity": "", "unit": ""},
            {"item": "hot pepper", "quantity": "", "unit": ""},
            {"item": "coconut milk", "quantity": "", "unit": "", "prep_note": "optional, to thicken"}
        ],
        "instructions": [
            {"step": 1, "text": "Numb the crickets and remove legs, wings, and claws."},
            {"step": 2, "text": "Sauté crickets in garlic and onions."},
            {"step": 3, "text": "Add soy sauce, vinegar, and hot pepper."},
            {"step": 4, "text": "Optional: Add coconut milk to thicken the sauce."},
            {"step": 5, "text": "Simmer until cooked through and sauce is reduced."}
        ],
        "temperature": "",
        "pan_size": "",
        "notes": ["Adobo-style preparation", "Coconut milk adds richness"],
        "tags": ["insects", "entomophagy", "mole cricket", "kamaro", "filipino", "adobo", "unusual protein"],
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

    for recipe in ETW_BATCH6_RECIPES:
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
    print(f"  Added: {added} new Eat the Weeds recipes (batch 6)")
    print(f"  Skipped: {skipped} duplicates")
    print(f"  Total recipes now: {len(recipes)}")


if __name__ == "__main__":
    main()
