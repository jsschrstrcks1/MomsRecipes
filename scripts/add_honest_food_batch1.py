#!/usr/bin/env python3
"""
Add Honest Food (Hank Shaw) recipes - Wild Game Batch 1
Unusual game recipes: squirrel, turtle, wild boar, dove
"""

import json
from pathlib import Path

RECIPES_FILE = Path(__file__).parent.parent / "data" / "recipes.json"

HONEST_FOOD_RECIPES = [
    # ===== SQUIRREL RECIPES =====
    {
        "id": "squirrel-stew-paprika-hf",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Squirrel Stew with Paprika and Greens",
        "category": "main dishes",
        "attribution": "Hank Shaw / Hunter Angler Gardener Cook",
        "source_note": "From honest-food.net - Squirrel Stew with Paprika",
        "description": "A hearty Cajun-style squirrel stew with smoked sausage, paprika, greens and tomatoes.",
        "servings_yield": "8 servings",
        "prep_time": "30 minutes",
        "cook_time": "2 hours",
        "total_time": "2 hours 20 minutes",
        "ingredients": [
            {"item": "squirrels", "quantity": "3", "unit": "", "prep_note": "cut into serving pieces"},
            {"item": "salt", "quantity": "", "unit": "", "prep_note": "to taste"},
            {"item": "black pepper", "quantity": "", "unit": "", "prep_note": "to taste"},
            {"item": "flour", "quantity": "", "unit": "", "prep_note": "for dusting"},
            {"item": "olive oil", "quantity": "1/3", "unit": "cup"},
            {"item": "onion", "quantity": "2", "unit": "cups", "prep_note": "sliced"},
            {"item": "garlic", "quantity": "3", "unit": "cloves", "prep_note": "minced"},
            {"item": "tomato paste", "quantity": "1", "unit": "heaping tbsp"},
            {"item": "white wine", "quantity": "1", "unit": "cup"},
            {"item": "cider vinegar", "quantity": "1/4", "unit": "cup"},
            {"item": "dried savory or oregano", "quantity": "1", "unit": "heaping tsp"},
            {"item": "red pepper flakes", "quantity": "1/2", "unit": "tsp"},
            {"item": "paprika", "quantity": "1", "unit": "heaping tbsp"},
            {"item": "whole peeled tomatoes", "quantity": "2-3", "unit": "cups", "prep_note": "torn into large pieces"},
            {"item": "smoked sausage (kielbasa or linguica)", "quantity": "1", "unit": "lb", "prep_note": "sliced bite-sized"},
            {"item": "greens (kale, chard, collards, or wild)", "quantity": "1", "unit": "lb"},
            {"item": "water", "quantity": "1", "unit": "quart", "prep_note": "approximately"}
        ],
        "instructions": [
            {"step": 1, "text": "Season squirrel pieces with salt and dust with flour."},
            {"step": 2, "text": "Heat olive oil in a heavy Dutch oven over medium-high heat. Brown squirrels in batches without crowding. Set browned pieces aside."},
            {"step": 3, "text": "Remove all squirrel from pot and add onions. Sauté 6-8 minutes until edges brown."},
            {"step": 4, "text": "Add minced garlic and cook 1 minute. Stir in tomato paste and cook 2-3 minutes, stirring frequently."},
            {"step": 5, "text": "Pour in white wine, vinegar, and approximately 1 quart water. Add savory, red pepper flakes, and paprika."},
            {"step": 6, "text": "Add torn tomatoes and return squirrel to pot. Bring to simmer and cook approximately 90 minutes until meat falls from bones easily."},
            {"step": 7, "text": "Remove squirrel pieces and pull meat from bones. Return meat to pot."},
            {"step": 8, "text": "Add sliced sausage and greens; cook about 10 minutes until greens are tender (collards need 15-20 minutes)."},
            {"step": 9, "text": "Season to taste and serve with crusty bread."}
        ],
        "temperature": "",
        "pan_size": "Dutch oven",
        "notes": ["Chicken, turkey, or rabbit can substitute for squirrel", "Better the next day like most stews"],
        "tags": ["squirrel", "stew", "cajun", "wild game", "paprika", "unusual protein"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "turtle-sauce-piquante-hf",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Cajun Turtle Sauce Piquante",
        "category": "main dishes",
        "attribution": "Hank Shaw / Hunter Angler Gardener Cook",
        "source_note": "From honest-food.net - Turtle Sauce Piquante",
        "description": "A Cajun tomato-based stew with snapping turtle, one of the few Cajun dishes that commonly has tomato in it.",
        "servings_yield": "6-8 servings",
        "prep_time": "30 minutes",
        "cook_time": "2 hours",
        "ingredients": [
            {"item": "snapping turtle meat", "quantity": "2", "unit": "lb", "prep_note": "cut into small dice"},
            {"item": "butter", "quantity": "4", "unit": "tbsp"},
            {"item": "flour", "quantity": "4", "unit": "tbsp"},
            {"item": "onion", "quantity": "2", "unit": "cups", "prep_note": "diced (part of the holy trinity)"},
            {"item": "celery", "quantity": "1", "unit": "cup", "prep_note": "diced"},
            {"item": "green bell pepper", "quantity": "1", "unit": "cup", "prep_note": "diced"},
            {"item": "garlic", "quantity": "4", "unit": "cloves", "prep_note": "minced"},
            {"item": "white wine", "quantity": "1", "unit": "cup"},
            {"item": "crushed tomatoes", "quantity": "1", "unit": "can (28 oz)"},
            {"item": "hot water or stock", "quantity": "2", "unit": "cups"},
            {"item": "bay leaves", "quantity": "2", "unit": ""},
            {"item": "Cajun seasoning", "quantity": "1", "unit": "tbsp"},
            {"item": "hot sauce (Tabasco)", "quantity": "", "unit": "", "prep_note": "to taste"},
            {"item": "salt and black pepper", "quantity": "", "unit": "", "prep_note": "to taste"},
            {"item": "green onions", "quantity": "1/2", "unit": "cup", "prep_note": "sliced, for garnish"}
        ],
        "instructions": [
            {"step": 1, "text": "Make a blonde roux: Melt butter in a Dutch oven over medium heat. Add flour and cook, stirring constantly, until it turns the color of peanut butter (10-15 minutes). Do not let it get darker."},
            {"step": 2, "text": "Add the holy trinity (onion, celery, bell pepper) and cook until softened, about 10 minutes."},
            {"step": 3, "text": "Add garlic and cook 1 minute."},
            {"step": 4, "text": "Add white wine and scrape up any browned bits."},
            {"step": 5, "text": "Add crushed tomatoes, hot water, bay leaves, and Cajun seasoning. Stir well."},
            {"step": 6, "text": "Add diced turtle meat. Bring to a simmer."},
            {"step": 7, "text": "Cook gently for 1.5-2 hours until turtle is tender. The small dice makes tough turtle meat innocuous."},
            {"step": 8, "text": "Season with salt, pepper, and hot sauce to taste."},
            {"step": 9, "text": "Serve over white rice, garnished with green onions. Put hot sauce on the table."}
        ],
        "temperature": "",
        "pan_size": "Dutch oven",
        "notes": [
            "Turtle uses a blonde (peanut butter colored) roux and white wine, unlike dark meat which uses chocolate-colored roux and red wine",
            "Alligator, frog legs, squirrel, or chicken thighs work as alternatives",
            "Better the day after it's made"
        ],
        "tags": ["turtle", "snapping turtle", "cajun", "sauce piquante", "wild game", "unusual protein"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "creole-turtle-soup-hf",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Creole Turtle Soup",
        "category": "soups",
        "attribution": "Hank Shaw / Hunter Angler Gardener Cook",
        "source_note": "From honest-food.net - Creole Turtle Soup",
        "description": "Classic New Orleans-style turtle soup with sherry and hard-boiled eggs.",
        "servings_yield": "8-10 servings",
        "prep_time": "45 minutes",
        "cook_time": "2.5 hours",
        "ingredients": [
            {"item": "turtle meat", "quantity": "2", "unit": "lb", "prep_note": "diced small"},
            {"item": "butter", "quantity": "1/2", "unit": "cup"},
            {"item": "flour", "quantity": "1/2", "unit": "cup"},
            {"item": "onion", "quantity": "2", "unit": "cups", "prep_note": "diced"},
            {"item": "celery", "quantity": "1", "unit": "cup", "prep_note": "diced"},
            {"item": "green bell pepper", "quantity": "1", "unit": "", "prep_note": "diced"},
            {"item": "garlic", "quantity": "6", "unit": "cloves", "prep_note": "minced"},
            {"item": "tomato paste", "quantity": "3", "unit": "tbsp"},
            {"item": "crushed tomatoes", "quantity": "1", "unit": "cup"},
            {"item": "beef or turtle stock", "quantity": "8", "unit": "cups"},
            {"item": "dry sherry", "quantity": "1/2", "unit": "cup", "prep_note": "plus more for serving"},
            {"item": "Worcestershire sauce", "quantity": "2", "unit": "tbsp"},
            {"item": "bay leaves", "quantity": "3", "unit": ""},
            {"item": "fresh thyme", "quantity": "1", "unit": "tbsp"},
            {"item": "cayenne pepper", "quantity": "1/2", "unit": "tsp"},
            {"item": "hard-boiled eggs", "quantity": "4", "unit": "", "prep_note": "chopped, for garnish"},
            {"item": "lemon", "quantity": "1", "unit": "", "prep_note": "sliced thin, for garnish"},
            {"item": "parsley", "quantity": "1/4", "unit": "cup", "prep_note": "chopped, for garnish"}
        ],
        "instructions": [
            {"step": 1, "text": "Make a dark roux: Melt butter in a large pot over medium heat. Add flour and cook, stirring constantly, until it turns the color of milk chocolate (20-30 minutes)."},
            {"step": 2, "text": "Add onion, celery, and bell pepper. Cook until softened, about 10 minutes."},
            {"step": 3, "text": "Add garlic and tomato paste. Cook 2 minutes."},
            {"step": 4, "text": "Add crushed tomatoes, stock, sherry, Worcestershire, bay leaves, thyme, and cayenne."},
            {"step": 5, "text": "Add turtle meat and bring to a simmer."},
            {"step": 6, "text": "Simmer gently for 2 hours until turtle is very tender."},
            {"step": 7, "text": "Remove bay leaves. Season with salt and pepper to taste."},
            {"step": 8, "text": "Serve in bowls, garnished with chopped hard-boiled eggs, thin lemon slices, and parsley. Pass extra sherry at the table."}
        ],
        "temperature": "",
        "pan_size": "large pot",
        "notes": ["A Commander's Palace classic", "Pass sherry at the table for diners to add more", "Snapping turtle is traditional"],
        "tags": ["turtle", "soup", "creole", "new orleans", "sherry", "unusual protein"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "braised-squirrel-aurora-hf",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Braised Squirrel Aurora (Spanish Style)",
        "category": "main dishes",
        "attribution": "Hank Shaw / Hunter Angler Gardener Cook",
        "source_note": "From honest-food.net - Braised Squirrel Aurora",
        "description": "Spanish-style braised squirrel with almonds and green olives.",
        "servings_yield": "4 servings",
        "prep_time": "20 minutes",
        "cook_time": "1.5 hours",
        "ingredients": [
            {"item": "squirrels", "quantity": "2-3", "unit": "", "prep_note": "cut into serving pieces"},
            {"item": "salt and pepper", "quantity": "", "unit": "", "prep_note": "to taste"},
            {"item": "olive oil", "quantity": "3", "unit": "tbsp"},
            {"item": "onion", "quantity": "1", "unit": "large", "prep_note": "sliced"},
            {"item": "garlic", "quantity": "4", "unit": "cloves", "prep_note": "minced"},
            {"item": "white wine", "quantity": "1", "unit": "cup"},
            {"item": "chicken or squirrel stock", "quantity": "1", "unit": "cup"},
            {"item": "blanched almonds", "quantity": "1/2", "unit": "cup"},
            {"item": "green olives", "quantity": "1/2", "unit": "cup", "prep_note": "pitted"},
            {"item": "saffron", "quantity": "1", "unit": "pinch", "prep_note": "optional"},
            {"item": "bay leaf", "quantity": "1", "unit": ""},
            {"item": "fingerling potatoes", "quantity": "1", "unit": "lb", "prep_note": "optional, to bulk up"}
        ],
        "instructions": [
            {"step": 1, "text": "Season squirrel pieces with salt and pepper."},
            {"step": 2, "text": "Heat olive oil in a Dutch oven or braiser over medium-high heat. Brown squirrel pieces on all sides. Remove and set aside."},
            {"step": 3, "text": "Add onion and cook until softened, about 5 minutes. Add garlic and cook 1 minute."},
            {"step": 4, "text": "Add white wine and scrape up browned bits. Add stock, saffron if using, and bay leaf."},
            {"step": 5, "text": "Return squirrel to pot. Add almonds and olives."},
            {"step": 6, "text": "Cover and braise at a gentle simmer for 1-1.5 hours until squirrel is tender."},
            {"step": 7, "text": "If using potatoes, add them in the last 30 minutes of cooking."},
            {"step": 8, "text": "Remove bay leaf, adjust seasoning, and serve."}
        ],
        "temperature": "",
        "pan_size": "Dutch oven or braiser",
        "notes": ["Rabbit or chicken can substitute for squirrel", "The almonds and olives are the defining flavors"],
        "tags": ["squirrel", "spanish", "braised", "almonds", "olives", "wild game", "unusual protein"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "grilled-doves-la-mancha-hf",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Grilled Doves La Mancha",
        "category": "main dishes",
        "attribution": "Hank Shaw / Hunter Angler Gardener Cook",
        "source_note": "From honest-food.net - Grilled Doves La Mancha",
        "description": "Spanish-style grilled doves with herbs and smoked paprika - the ultimate dove recipe.",
        "servings_yield": "4 servings",
        "prep_time": "20 minutes",
        "cook_time": "10 minutes",
        "total_time": "30 minutes plus marinating",
        "ingredients": [
            {"item": "doves or pigeons", "quantity": "8-12", "unit": "", "prep_note": "whole, spatchcocked"},
            {"item": "olive oil", "quantity": "1/4", "unit": "cup"},
            {"item": "smoked paprika (pimentón)", "quantity": "2", "unit": "tbsp"},
            {"item": "garlic", "quantity": "4", "unit": "cloves", "prep_note": "minced"},
            {"item": "fresh thyme", "quantity": "1", "unit": "tbsp", "prep_note": "minced"},
            {"item": "fresh rosemary", "quantity": "1", "unit": "tbsp", "prep_note": "minced"},
            {"item": "salt", "quantity": "1", "unit": "tbsp"},
            {"item": "black pepper", "quantity": "1", "unit": "tsp"},
            {"item": "sherry vinegar", "quantity": "2", "unit": "tbsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Spatchcock the doves by cutting out the backbone and pressing flat."},
            {"step": 2, "text": "Mix olive oil, paprika, garlic, thyme, rosemary, salt, pepper, and sherry vinegar to make a paste."},
            {"step": 3, "text": "Coat doves thoroughly with the paste. Marinate at least 1 hour or overnight."},
            {"step": 4, "text": "Heat grill to high. Clean and oil the grates."},
            {"step": 5, "text": "Grill doves skin-side down first for 3-4 minutes until skin is crispy."},
            {"step": 6, "text": "Flip and grill another 2-3 minutes. Breast meat should be pink (medium)."},
            {"step": 7, "text": "Rest 5 minutes before serving."}
        ],
        "temperature": "high heat grill",
        "pan_size": "",
        "notes": ["Grilling is the best way to get crispy skin without overcooking the breast", "Also works with pigeons, squab, teal, woodcock, rails, quail, or Cornish game hens", "Serve medium (pink inside) - not well done"],
        "tags": ["dove", "pigeon", "grilled", "spanish", "smoked paprika", "wild game"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "dove-poppers-hf",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Hank's Dove Poppers",
        "category": "appetizers",
        "attribution": "Hank Shaw / Hunter Angler Gardener Cook",
        "source_note": "From honest-food.net - Dove Poppers",
        "description": "The most popular dove recipe in America - dove breasts with roasted garlic, poblano chiles, wrapped in bacon.",
        "servings_yield": "6-8 servings as appetizer",
        "prep_time": "30 minutes",
        "cook_time": "20 minutes",
        "ingredients": [
            {"item": "dove breasts", "quantity": "16-20", "unit": "", "prep_note": "boneless"},
            {"item": "cream cheese", "quantity": "4", "unit": "oz", "prep_note": "softened"},
            {"item": "roasted garlic", "quantity": "1", "unit": "head", "prep_note": "cloves mashed"},
            {"item": "roasted poblano or Hatch chile", "quantity": "1", "unit": "", "prep_note": "seeded and diced"},
            {"item": "jalapeño", "quantity": "1", "unit": "", "prep_note": "seeded and minced"},
            {"item": "bacon", "quantity": "8-10", "unit": "slices", "prep_note": "cut in half"},
            {"item": "salt and pepper", "quantity": "", "unit": "", "prep_note": "to taste"}
        ],
        "instructions": [
            {"step": 1, "text": "Mix cream cheese with mashed roasted garlic, diced poblano, and minced jalapeño. Season with salt and pepper."},
            {"step": 2, "text": "Butterfly each dove breast if thick, or leave whole if small."},
            {"step": 3, "text": "Place a spoonful of filling on each dove breast."},
            {"step": 4, "text": "Roll up and wrap with half a slice of bacon. Secure with a toothpick."},
            {"step": 5, "text": "Grill over medium-high heat, turning occasionally, until bacon is crispy and dove is cooked through but still pink inside, about 10-15 minutes."},
            {"step": 6, "text": "Alternatively, bake at 400°F for 15-20 minutes."}
        ],
        "temperature": "400°F (200°C) if baking",
        "pan_size": "",
        "notes": ["Different from traditional poppers with roasted garlic and poblano instead of just jalapeño and cheese", "Can use duck, goose, quail, or pheasant breast"],
        "tags": ["dove", "poppers", "appetizer", "bacon", "wild game", "grilled"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "wild-boar-sausage-hf",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Wild Boar Sausage",
        "category": "charcuterie",
        "attribution": "Hank Shaw / Hunter Angler Gardener Cook",
        "source_note": "From honest-food.net - Wild Boar Sausage",
        "description": "A coarse, country-style wild boar sausage that highlights the flavor of the boar.",
        "servings_yield": "about 5 pounds",
        "prep_time": "1 hour",
        "cook_time": "",
        "ingredients": [
            {"item": "wild boar shoulder or leg", "quantity": "4", "unit": "lb", "prep_note": "cubed"},
            {"item": "pork fat (back fat or belly)", "quantity": "1", "unit": "lb", "prep_note": "cubed"},
            {"item": "salt", "quantity": "2", "unit": "tbsp"},
            {"item": "black pepper", "quantity": "1", "unit": "tbsp", "prep_note": "freshly ground"},
            {"item": "fresh sage", "quantity": "2", "unit": "tbsp", "prep_note": "minced"},
            {"item": "fresh thyme", "quantity": "1", "unit": "tbsp", "prep_note": "minced"},
            {"item": "garlic", "quantity": "4", "unit": "cloves", "prep_note": "minced"},
            {"item": "ice water", "quantity": "1/4", "unit": "cup"},
            {"item": "hog casings", "quantity": "", "unit": "", "prep_note": "soaked"}
        ],
        "instructions": [
            {"step": 1, "text": "Cube meat and fat. Freeze for 30 minutes to make grinding easier."},
            {"step": 2, "text": "Grind meat and fat together through a coarse plate (3/8 inch)."},
            {"step": 3, "text": "Mix ground meat with salt, pepper, sage, thyme, and garlic."},
            {"step": 4, "text": "Add ice water and mix until the mixture becomes sticky and cohesive."},
            {"step": 5, "text": "Fry a small test patty to check seasoning. Adjust if needed."},
            {"step": 6, "text": "Stuff into soaked hog casings, twisting into 6-inch links."},
            {"step": 7, "text": "Let rest uncovered in refrigerator overnight to dry slightly before cooking."}
        ],
        "temperature": "",
        "pan_size": "",
        "notes": ["Use 20-25% fat for best results", "Wild boar fat can be softer - mixing with domestic pork fat helps", "Can be used as bulk sausage without casings"],
        "tags": ["wild boar", "sausage", "charcuterie", "wild game", "pork"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "grilled-deer-heart-hf",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Grilled Deer Heart with Peppers and Onions",
        "category": "main dishes",
        "attribution": "Hank Shaw / Hunter Angler Gardener Cook",
        "source_note": "From honest-food.net - Grilled Deer Heart",
        "description": "Grilled venison heart served with marinated peppers and onions - a celebration of the hunt.",
        "servings_yield": "4 servings",
        "prep_time": "30 minutes",
        "cook_time": "15 minutes",
        "ingredients": [
            {"item": "deer heart", "quantity": "1", "unit": "", "prep_note": "cleaned and trimmed"},
            {"item": "olive oil", "quantity": "3", "unit": "tbsp"},
            {"item": "red wine vinegar", "quantity": "2", "unit": "tbsp"},
            {"item": "garlic", "quantity": "2", "unit": "cloves", "prep_note": "minced"},
            {"item": "fresh rosemary", "quantity": "1", "unit": "tbsp", "prep_note": "minced"},
            {"item": "salt", "quantity": "1", "unit": "tsp"},
            {"item": "black pepper", "quantity": "1/2", "unit": "tsp"},
            {"item": "bell peppers (mixed colors)", "quantity": "2", "unit": "", "prep_note": "sliced"},
            {"item": "onion", "quantity": "1", "unit": "large", "prep_note": "sliced"}
        ],
        "instructions": [
            {"step": 1, "text": "Clean heart by trimming off fat, arteries, and silverskin. Slice into 1/2-inch steaks."},
            {"step": 2, "text": "Mix olive oil, vinegar, garlic, rosemary, salt, and pepper."},
            {"step": 3, "text": "Marinate heart slices for 30 minutes to 2 hours."},
            {"step": 4, "text": "Grill peppers and onions over medium heat until charred and softened. Set aside."},
            {"step": 5, "text": "Grill heart slices over high heat, 2-3 minutes per side for medium-rare."},
            {"step": 6, "text": "Let rest 5 minutes. Slice against the grain and serve with peppers and onions."}
        ],
        "temperature": "high heat grill",
        "pan_size": "",
        "notes": ["Works with elk, moose, antelope, or beef heart", "Elk or moose heart feeds up to 6 people", "Serve medium-rare to medium - overcooking makes it tough"],
        "tags": ["venison", "deer heart", "offal", "grilled", "wild game"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "brunswick-stew-hf",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Brunswick Stew",
        "category": "main dishes",
        "attribution": "Hank Shaw / Hunter Angler Gardener Cook",
        "source_note": "From honest-food.net - Brunswick Stew",
        "description": "Iconic Southern stew traditionally made with squirrel, though many meats work.",
        "servings_yield": "10-12 servings",
        "prep_time": "45 minutes",
        "cook_time": "3 hours",
        "ingredients": [
            {"item": "squirrel or rabbit", "quantity": "2-3", "unit": "", "prep_note": "cut up (or 2 lb chicken)"},
            {"item": "smoked ham hock", "quantity": "1", "unit": ""},
            {"item": "bacon", "quantity": "4", "unit": "slices", "prep_note": "diced"},
            {"item": "onion", "quantity": "2", "unit": "large", "prep_note": "diced"},
            {"item": "potatoes", "quantity": "1", "unit": "lb", "prep_note": "peeled and cubed"},
            {"item": "lima beans or butter beans", "quantity": "2", "unit": "cups"},
            {"item": "corn kernels", "quantity": "2", "unit": "cups"},
            {"item": "tomatoes", "quantity": "2", "unit": "cups", "prep_note": "crushed"},
            {"item": "chicken or game stock", "quantity": "6", "unit": "cups"},
            {"item": "Worcestershire sauce", "quantity": "2", "unit": "tbsp"},
            {"item": "hot sauce", "quantity": "1", "unit": "tsp"},
            {"item": "apple cider vinegar", "quantity": "2", "unit": "tbsp"},
            {"item": "brown sugar", "quantity": "1", "unit": "tbsp"},
            {"item": "salt and pepper", "quantity": "", "unit": "", "prep_note": "to taste"}
        ],
        "instructions": [
            {"step": 1, "text": "Render bacon in a large pot. Remove and set aside."},
            {"step": 2, "text": "Brown meat pieces in bacon fat. Remove and set aside."},
            {"step": 3, "text": "Sauté onion until softened."},
            {"step": 4, "text": "Add stock, ham hock, and browned meat. Simmer 2 hours until meat is very tender."},
            {"step": 5, "text": "Remove meat and ham hock. Shred all meat and discard bones."},
            {"step": 6, "text": "Add potatoes, cook 15 minutes. Add beans and corn, cook 15 more minutes."},
            {"step": 7, "text": "Add tomatoes, Worcestershire, hot sauce, vinegar, and brown sugar."},
            {"step": 8, "text": "Return shredded meat to pot. Simmer 30 minutes, mashing some potatoes to thicken."},
            {"step": 9, "text": "Season with salt and pepper. Serve with cornbread."}
        ],
        "temperature": "",
        "pan_size": "large pot or Dutch oven",
        "notes": ["Squirrel is traditional but chicken is common now", "Virginia claims this stew originated there, Georgia disputes this", "Stew should be thick enough to eat with a fork"],
        "tags": ["brunswick stew", "squirrel", "southern", "stew", "wild game"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "wild-hog-bbq-pulled-pork-hf",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Wild Hog BBQ (Pulled Pork)",
        "category": "main dishes",
        "attribution": "Hank Shaw / Hunter Angler Gardener Cook",
        "source_note": "From honest-food.net - Wild Hog BBQ",
        "description": "Slow-smoked wild hog shoulder for pulled pork - takes longer than domestic pork.",
        "servings_yield": "12-16 servings",
        "prep_time": "30 minutes",
        "cook_time": "10-14 hours",
        "ingredients": [
            {"item": "wild hog shoulder", "quantity": "8-10", "unit": "lb", "prep_note": "bone-in"},
            {"item": "yellow mustard", "quantity": "1/2", "unit": "cup", "prep_note": "as binder"},
            {"item": "brown sugar", "quantity": "1/2", "unit": "cup"},
            {"item": "paprika", "quantity": "1/4", "unit": "cup"},
            {"item": "chili powder", "quantity": "2", "unit": "tbsp"},
            {"item": "garlic powder", "quantity": "2", "unit": "tbsp"},
            {"item": "onion powder", "quantity": "1", "unit": "tbsp"},
            {"item": "black pepper", "quantity": "1", "unit": "tbsp"},
            {"item": "cayenne", "quantity": "1", "unit": "tsp"},
            {"item": "salt", "quantity": "2", "unit": "tbsp"},
            {"item": "apple cider vinegar", "quantity": "1", "unit": "cup", "prep_note": "for spritzing"},
            {"item": "BBQ sauce", "quantity": "", "unit": "", "prep_note": "for serving"}
        ],
        "instructions": [
            {"step": 1, "text": "Mix dry rub ingredients (brown sugar through salt)."},
            {"step": 2, "text": "Coat shoulder with mustard, then apply rub liberally. Let sit overnight in refrigerator."},
            {"step": 3, "text": "Set up smoker for 225-250°F. Use oak, hickory, or fruit wood."},
            {"step": 4, "text": "Smoke shoulder fat-side up. Spritz with vinegar every hour after first 3 hours."},
            {"step": 5, "text": "When internal temp reaches 165°F (usually 6-8 hours), wrap tightly in foil or butcher paper."},
            {"step": 6, "text": "Continue cooking until internal temp reaches 200-205°F and probe slides in easily."},
            {"step": 7, "text": "Rest wrapped for at least 1 hour."},
            {"step": 8, "text": "Pull meat, discarding fat and bone. Mix with BBQ sauce or serve sauce on the side."}
        ],
        "temperature": "225-250°F smoker",
        "pan_size": "",
        "notes": ["Wild hog takes longer than domestic due to less fat", "Internal temp of 200-205°F is key for proper texture", "Can finish in 300°F oven if needed"],
        "tags": ["wild boar", "bbq", "pulled pork", "smoked", "wild game"],
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

    for recipe in HONEST_FOOD_RECIPES:
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
    print(f"  Added: {added} new Honest Food recipes")
    print(f"  Skipped: {skipped} duplicates")
    print(f"  Total recipes now: {len(recipes)}")


if __name__ == "__main__":
    main()
