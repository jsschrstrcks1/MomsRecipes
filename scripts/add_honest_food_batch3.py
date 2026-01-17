#!/usr/bin/env python3
"""
Add Honest Food (Hank Shaw) recipes - Batch 3
Bear, frog, and upland game bird recipes
"""

import json
from pathlib import Path

RECIPES_FILE = Path(__file__).parent.parent / "data" / "recipes.json"

HONEST_FOOD_RECIPES = [
    # ===== BEAR RECIPES =====
    {
        "id": "siberian-bear-pelmeni-hf",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Siberian Bear Pelmeni",
        "category": "main dishes",
        "attribution": "Honest Food / Hank Shaw",
        "source_note": "From honest-food.net - Russian dumplings traditionally made with bear meat",
        "description": "Traditional Siberian dumplings with bear meat and lots of onion. The original pelmeni were made by bear hunters and frozen in the snow for the trail.",
        "servings_yield": "about 50 dumplings",
        "prep_time": "1 hour",
        "cook_time": "8 minutes",
        "ingredients": [
            {"item": "bear meat", "quantity": "1", "unit": "lb", "prep_note": "ground (or pork/beef)"},
            {"item": "onion", "quantity": "1", "unit": "large", "prep_note": "finely minced"},
            {"item": "garlic", "quantity": "2", "unit": "cloves", "prep_note": "minced"},
            {"item": "salt pork or fatback", "quantity": "2", "unit": "oz", "prep_note": "minced"},
            {"item": "salt", "quantity": "1", "unit": "tsp"},
            {"item": "black pepper", "quantity": "1/2", "unit": "tsp"},
            {"item": "flour", "quantity": "3", "unit": "cups"},
            {"item": "egg yolks", "quantity": "2", "unit": ""},
            {"item": "buttermilk or whey", "quantity": "1", "unit": "cup"},
            {"item": "water", "quantity": "1/2", "unit": "cup"},
            {"item": "sour cream", "quantity": "", "unit": "", "prep_note": "for serving"},
            {"item": "fresh dill", "quantity": "", "unit": "", "prep_note": "chopped, for serving"}
        ],
        "instructions": [
            {"step": 1, "text": "Make the dough: Mix flour with egg yolks, buttermilk, and water. Knead until smooth. Let rest 30 minutes."},
            {"step": 2, "text": "Make the filling: Combine ground bear meat with onion, garlic, salt pork, salt, and pepper. Mix well."},
            {"step": 3, "text": "Roll dough thin and cut into 3-inch rounds."},
            {"step": 4, "text": "Place a small spoonful of filling in center of each round."},
            {"step": 5, "text": "Fold in half and pinch edges to seal, then bring corners together to form the classic pelmeni shape."},
            {"step": 6, "text": "Bring a large pot of salted water to a boil."},
            {"step": 7, "text": "Boil pelmeni for 6-8 minutes to ensure bear meat is fully cooked."},
            {"step": 8, "text": "Serve with sour cream mixed with dill and black pepper."}
        ],
        "temperature": "",
        "pan_size": "large pot",
        "notes": ["Use a lot of onion - it's a defining feature of these dumplings", "Can substitute pork or beef for bear", "Traditionally made with sourdough using whey"],
        "tags": ["bear", "russian", "dumplings", "wild game", "unusual"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "chinese-red-braised-bear-hf",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Chinese Red Braised Pork or Bear",
        "category": "main dishes",
        "attribution": "Honest Food / Hank Shaw",
        "source_note": "From honest-food.net - Classic Chinese dish adapted for wild game",
        "description": "Sweet-savory braised fatty meat with star anise and dark soy sauce. Works beautifully with fat wild pigs or bear belly.",
        "servings_yield": "4-6 servings",
        "prep_time": "20 minutes",
        "cook_time": "2-3 hours",
        "ingredients": [
            {"item": "bear belly or pork belly", "quantity": "2", "unit": "lb"},
            {"item": "rock sugar or brown sugar", "quantity": "3", "unit": "tbsp"},
            {"item": "water", "quantity": "3", "unit": "tbsp", "prep_note": "for sugar"},
            {"item": "dark soy sauce", "quantity": "3", "unit": "tbsp"},
            {"item": "light soy sauce", "quantity": "2", "unit": "tbsp"},
            {"item": "Shaoxing wine or dry sherry", "quantity": "1/4", "unit": "cup"},
            {"item": "star anise", "quantity": "3", "unit": "whole"},
            {"item": "garlic", "quantity": "4", "unit": "cloves", "prep_note": "smashed"},
            {"item": "ginger", "quantity": "2", "unit": "inches", "prep_note": "sliced"},
            {"item": "scallions", "quantity": "4", "unit": "", "prep_note": "cut into 2-inch pieces"},
            {"item": "water or stock", "quantity": "2", "unit": "cups"}
        ],
        "instructions": [
            {"step": 1, "text": "Bring a large pot of water to boil. Boil the whole slab of belly for 5 minutes. Remove and let cool."},
            {"step": 2, "text": "Cut the meat into 2-inch cubes."},
            {"step": 3, "text": "Mix sugar with 3 tablespoons water until dissolved."},
            {"step": 4, "text": "In a wok or Dutch oven, heat the sugar syrup over medium heat until it turns amber, about 5 minutes."},
            {"step": 5, "text": "Add the par-cooked meat and turn to coat with the caramelized sugar."},
            {"step": 6, "text": "Add garlic, ginger, and scallions. Stir for 1 minute."},
            {"step": 7, "text": "Add both soy sauces, wine, star anise, and enough water to barely cover the meat."},
            {"step": 8, "text": "Bring to a boil, then reduce to a gentle simmer."},
            {"step": 9, "text": "Simmer for 90 minutes for pork, up to 3 hours for wild hog or bear, until meat is very tender."},
            {"step": 10, "text": "Serve over steamed jasmine rice."}
        ],
        "temperature": "",
        "pan_size": "wok or Dutch oven",
        "notes": ["Dark soy sauce has a slight molasses sweetness different from regular soy", "Wild game may take longer than domestic pork", "Any fatty cut works - shoulder is also good"],
        "tags": ["bear", "wild boar", "chinese", "braised", "wild game"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "bear-fat-biscuits-hf",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Bear Fat Buttermilk Biscuits",
        "category": "breads",
        "attribution": "Honest Food / Hank Shaw",
        "source_note": "From honest-food.net - Classic biscuits made with rendered bear fat",
        "description": "Classic buttermilk biscuits using bear fat instead of butter or lard. Bear fat makes exceptionally flaky pastry with no gamey flavor.",
        "servings_yield": "8-10 biscuits",
        "prep_time": "15 minutes",
        "cook_time": "12-15 minutes",
        "ingredients": [
            {"item": "all-purpose flour", "quantity": "2", "unit": "cups"},
            {"item": "rendered bear fat", "quantity": "1/3", "unit": "cup", "prep_note": "cold"},
            {"item": "buttermilk", "quantity": "3/4", "unit": "cup"},
            {"item": "sugar", "quantity": "1", "unit": "tbsp"},
            {"item": "baking powder", "quantity": "1", "unit": "tbsp"},
            {"item": "salt", "quantity": "1/2", "unit": "tsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Preheat oven to 450°F."},
            {"step": 2, "text": "Whisk together flour, sugar, baking powder, and salt in a bowl."},
            {"step": 3, "text": "Add the cold bear fat and cut it into the flour with a fork or pastry cutter."},
            {"step": 4, "text": "Work quickly so the fat doesn't melt. You're done when the mixture looks like little crumbly peas."},
            {"step": 5, "text": "Pour in the buttermilk and stir just until dough comes together. It should be sticky but pull away from the sides."},
            {"step": 6, "text": "Don't overwork the dough or biscuits will be tough."},
            {"step": 7, "text": "Turn out onto floured surface, pat to 3/4-inch thickness."},
            {"step": 8, "text": "Cut with a biscuit cutter and place on baking sheet."},
            {"step": 9, "text": "Bake for 12-15 minutes until golden brown."}
        ],
        "temperature": "450°F (230°C)",
        "pan_size": "baking sheet",
        "notes": ["Can substitute up to 1/2 cup acorn flour for variety", "Use fresh rendered bear fat, not hydrogenated lard", "Duck fat or lard work as substitutes"],
        "tags": ["bear", "biscuits", "breakfast", "wild game", "baking"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    # ===== FROG RECIPES =====
    {
        "id": "french-fried-frog-legs-hf",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "French Fried Frog Legs",
        "category": "main dishes",
        "attribution": "Honest Food / Hank Shaw",
        "source_note": "From honest-food.net - French-style fried frog legs with butter sauce",
        "description": "Classic French preparation of frog legs, lightly fried in clarified butter and served with garlic parsley butter sauce.",
        "servings_yield": "4 servings",
        "prep_time": "15 minutes plus 1 hour marinating",
        "cook_time": "10 minutes",
        "ingredients": [
            {"item": "frog legs", "quantity": "2", "unit": "lb", "prep_note": "about 12-16 pairs"},
            {"item": "milk", "quantity": "1", "unit": "cup", "prep_note": "for soaking"},
            {"item": "clarified butter or ghee", "quantity": "4", "unit": "tbsp", "prep_note": "for frying"},
            {"item": "unsalted butter", "quantity": "3", "unit": "tbsp", "prep_note": "for sauce"},
            {"item": "garlic", "quantity": "3", "unit": "cloves", "prep_note": "minced"},
            {"item": "fresh parsley", "quantity": "1/4", "unit": "cup", "prep_note": "chopped"},
            {"item": "lemon juice", "quantity": "2", "unit": "tbsp"},
            {"item": "flour", "quantity": "1/2", "unit": "cup", "prep_note": "for dredging"},
            {"item": "salt and pepper", "quantity": "", "unit": "", "prep_note": "to taste"}
        ],
        "instructions": [
            {"step": 1, "text": "Soak frog legs in milk in the refrigerator for 1 hour. (Skip for store-bought legs.)"},
            {"step": 2, "text": "Remove legs from milk, pat dry, and season with salt and pepper."},
            {"step": 3, "text": "Dredge legs lightly in flour, shaking off excess."},
            {"step": 4, "text": "Heat clarified butter in a large skillet over medium-high heat until you see a wisp of smoke (about 340°F)."},
            {"step": 5, "text": "Add frog legs and cook 3-4 minutes per side until golden brown and cooked through."},
            {"step": 6, "text": "Remove legs to a warm platter."},
            {"step": 7, "text": "Add regular butter to the pan, then garlic. Sauté 30 seconds."},
            {"step": 8, "text": "Add parsley and lemon juice, swirl to combine."},
            {"step": 9, "text": "Pour sauce over frog legs and serve immediately."}
        ],
        "temperature": "340°F oil temperature",
        "pan_size": "large skillet",
        "notes": ["Frog legs taste like a combination of chicken breast, shrimp, and crab", "Use clarified butter to fry - higher smoke point", "Good fresh ingredients are key - no wilty parsley"],
        "tags": ["frog", "french", "fried", "wild game", "unusual"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "chinese-stir-fried-frog-legs-hf",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Chinese Stir-Fried Frog Legs",
        "category": "main dishes",
        "attribution": "Honest Food / Hank Shaw",
        "source_note": "From honest-food.net - An amalgam of General Tso's, kung pao, and black bean styles",
        "description": "Battered and fried frog legs tossed in a sweet-spicy sauce with vegetables. A fusion of Chinese-American classics.",
        "servings_yield": "4 servings",
        "prep_time": "30 minutes",
        "cook_time": "15 minutes",
        "ingredients": [
            {"item": "frog legs", "quantity": "2", "unit": "lb", "prep_note": "separated"},
            {"item": "egg yolks", "quantity": "2", "unit": ""},
            {"item": "soy sauce", "quantity": "2", "unit": "tbsp", "prep_note": "for marinade"},
            {"item": "cornstarch", "quantity": "1/2", "unit": "cup"},
            {"item": "vegetable oil", "quantity": "2", "unit": "cups", "prep_note": "for frying"},
            {"item": "garlic", "quantity": "3", "unit": "cloves", "prep_note": "minced"},
            {"item": "ginger", "quantity": "1", "unit": "inch", "prep_note": "minced"},
            {"item": "shallot", "quantity": "1", "unit": "", "prep_note": "sliced"},
            {"item": "bamboo shoots", "quantity": "1/2", "unit": "cup", "prep_note": "sliced"},
            {"item": "wood ear mushrooms", "quantity": "1/4", "unit": "cup", "prep_note": "sliced, optional"},
            {"item": "red bell pepper", "quantity": "1/2", "unit": "", "prep_note": "diced"},
            {"item": "chile bean sauce", "quantity": "1", "unit": "tbsp"},
            {"item": "soy sauce", "quantity": "2", "unit": "tbsp", "prep_note": "for sauce"},
            {"item": "rice vinegar", "quantity": "1", "unit": "tbsp"},
            {"item": "sugar", "quantity": "1", "unit": "tbsp"},
            {"item": "chicken stock", "quantity": "1/4", "unit": "cup"},
            {"item": "sesame oil", "quantity": "1", "unit": "tsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Whisk egg yolks with 2 tbsp soy sauce. Marinate frog legs while prepping other ingredients."},
            {"step": 2, "text": "Mix sauce ingredients: chile bean sauce, 2 tbsp soy sauce, vinegar, sugar, stock, and 1 tbsp cornstarch."},
            {"step": 3, "text": "Remove frog legs from marinade and dust with remaining cornstarch."},
            {"step": 4, "text": "Heat oil to 350°F. Fry frog legs in batches until golden, 3-5 minutes. Drain."},
            {"step": 5, "text": "Pour off all but 2 tbsp oil from wok."},
            {"step": 6, "text": "Get wok very hot. Add garlic, ginger, and shallot. Stir-fry 30 seconds."},
            {"step": 7, "text": "Add bamboo shoots, mushrooms, bell pepper, and fried frog legs. Stir-fry 2 minutes."},
            {"step": 8, "text": "Add sauce, toss to coat. Cook until sauce thickens, 1-2 minutes."},
            {"step": 9, "text": "Drizzle with sesame oil and serve over steamed rice."}
        ],
        "temperature": "350°F oil temperature",
        "pan_size": "wok",
        "notes": ["Best eaten with chopsticks - meat slides right off the bones", "Wood ear mushrooms add meaty texture but can be omitted", "Find frog legs in Asian market freezer sections"],
        "tags": ["frog", "chinese", "stir-fry", "wild game", "unusual"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    # ===== UPLAND GAME BIRDS =====
    {
        "id": "roast-chukar-partridge-hf",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Roast Chukar or Partridge",
        "category": "main dishes",
        "attribution": "Honest Food / Hank Shaw",
        "source_note": "From honest-food.net - Brined and roasted small game birds",
        "description": "Simple brined and roasted chukar partridge. The overnight brine keeps these lean birds juicy and gives you wiggle room during roasting.",
        "servings_yield": "2 servings",
        "prep_time": "15 minutes plus overnight brine",
        "cook_time": "25 minutes",
        "ingredients": [
            {"item": "chukars or Hungarian partridges", "quantity": "2", "unit": "", "prep_note": "plucked whole"},
            {"item": "kosher salt", "quantity": "1/4", "unit": "cup", "prep_note": "for brine"},
            {"item": "hot water", "quantity": "4", "unit": "cups"},
            {"item": "bay leaf", "quantity": "1", "unit": ""},
            {"item": "dried thyme", "quantity": "1", "unit": "tsp"},
            {"item": "rosemary", "quantity": "1", "unit": "sprig"},
            {"item": "sage leaves", "quantity": "5", "unit": "", "prep_note": "chopped"},
            {"item": "cloves", "quantity": "2", "unit": "whole"},
            {"item": "lemon", "quantity": "1", "unit": "", "prep_note": "quartered"},
            {"item": "celery stalks", "quantity": "2", "unit": "", "prep_note": "for roasting rack"}
        ],
        "instructions": [
            {"step": 1, "text": "Make brine: Pour hot water over salt, stir to dissolve. Add bay leaf, thyme, rosemary, sage, and cloves. Cool to room temperature."},
            {"step": 2, "text": "Submerge birds in brine, cover, and refrigerate up to 8 hours."},
            {"step": 3, "text": "Remove birds from brine, pat dry. Let sit uncovered in fridge several hours to dry the skin, or at room temperature 20 minutes."},
            {"step": 4, "text": "Preheat oven to 450°F."},
            {"step": 5, "text": "Stuff each bird cavity with a lemon quarter. Lightly salt exterior."},
            {"step": 6, "text": "Lay celery stalks in a cast-iron pan to keep birds off the bottom."},
            {"step": 7, "text": "Place birds on celery and roast 20-25 minutes."},
            {"step": 8, "text": "Check temperature - breast meat should be 150-155°F, no higher. Pink is good."},
            {"step": 9, "text": "Rest 5 minutes before serving."}
        ],
        "temperature": "450°F (230°C)",
        "pan_size": "cast-iron pan or roasting pan",
        "notes": ["Never let breast meat exceed 155°F or it will be dry", "Works for quail, small grouse, and Cornish game hens too", "Only for plucked birds - don't use this recipe if skinned"],
        "tags": ["chukar", "partridge", "game bird", "roasted", "wild game"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "grouse-wild-rice-soup-hf",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Grouse Soup with Wild Rice",
        "category": "soups",
        "attribution": "Honest Food / Hank Shaw",
        "source_note": "From honest-food.net - Forest flavors in a bowl",
        "description": "The essence of the forest in a bowl - grouse meat with wild rice, porcini mushrooms, and chestnuts or acorns.",
        "servings_yield": "6-8 servings",
        "prep_time": "30 minutes",
        "cook_time": "1.5 hours",
        "ingredients": [
            {"item": "grouse carcasses", "quantity": "2-3", "unit": "", "prep_note": "with meat reserved"},
            {"item": "game or chicken broth", "quantity": "3", "unit": "quarts"},
            {"item": "wild rice", "quantity": "1", "unit": "cup"},
            {"item": "grouse meat", "quantity": "2", "unit": "cups", "prep_note": "chopped"},
            {"item": "dried porcini mushrooms", "quantity": "1", "unit": "oz"},
            {"item": "chestnuts or acorns", "quantity": "1", "unit": "cup", "prep_note": "cooked and chopped"},
            {"item": "chard or spinach", "quantity": "2", "unit": "cups", "prep_note": "chopped"},
            {"item": "onion", "quantity": "1", "unit": "", "prep_note": "diced"},
            {"item": "carrots", "quantity": "2", "unit": "", "prep_note": "diced"},
            {"item": "celery", "quantity": "2", "unit": "stalks", "prep_note": "diced"},
            {"item": "salt", "quantity": "", "unit": "", "prep_note": "to taste"}
        ],
        "instructions": [
            {"step": 1, "text": "Place grouse carcasses, dried mushrooms, onion, carrots, and celery in a large pot with broth."},
            {"step": 2, "text": "Simmer for 1 hour to extract flavor."},
            {"step": 3, "text": "Strain broth through a fine strainer lined with paper towel. You need 2-3 quarts."},
            {"step": 4, "text": "Chop the rehydrated mushrooms and reserve."},
            {"step": 5, "text": "Bring strained broth to a simmer. Add salt and wild rice."},
            {"step": 6, "text": "Cook at a slow boil. True wild rice cooks in about 25 minutes; cultivated takes longer."},
            {"step": 7, "text": "When rice is nearly done, add grouse meat, chestnuts, mushrooms, and greens."},
            {"step": 8, "text": "Simmer 5 minutes more and serve."}
        ],
        "temperature": "",
        "pan_size": "large soup pot",
        "notes": ["For non-hunters: use turkey or chicken thighs, cultivated wild rice, and chestnuts", "Real foraged wild rice cooks faster than cultivated", "Save grouse carcasses in freezer until you have enough"],
        "tags": ["grouse", "soup", "wild rice", "mushrooms", "wild game"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "venison-steak-diane-hf",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Venison Steak Diane",
        "category": "main dishes",
        "attribution": "Honest Food / Hank Shaw",
        "source_note": "From honest-food.net - Classic sauce for venison medallions",
        "description": "Seared venison medallions with a rich brandy, mustard, and Worcestershire sauce. Named for Diana, goddess of the hunt.",
        "servings_yield": "4 servings",
        "prep_time": "15 minutes",
        "cook_time": "15 minutes",
        "ingredients": [
            {"item": "venison medallions", "quantity": "1.5", "unit": "lb", "prep_note": "deer, elk, or moose backstrap"},
            {"item": "butter", "quantity": "4", "unit": "tbsp", "prep_note": "divided"},
            {"item": "shallots", "quantity": "2", "unit": "", "prep_note": "minced"},
            {"item": "mushrooms", "quantity": "8", "unit": "oz", "prep_note": "sliced"},
            {"item": "garlic", "quantity": "2", "unit": "cloves", "prep_note": "minced"},
            {"item": "brandy", "quantity": "1/4", "unit": "cup"},
            {"item": "Dijon mustard", "quantity": "2", "unit": "tbsp"},
            {"item": "Worcestershire sauce", "quantity": "1", "unit": "tbsp"},
            {"item": "tomato paste", "quantity": "1", "unit": "tbsp"},
            {"item": "beef or game stock", "quantity": "1/2", "unit": "cup"},
            {"item": "heavy cream", "quantity": "1/4", "unit": "cup", "prep_note": "optional"},
            {"item": "parsley", "quantity": "2", "unit": "tbsp", "prep_note": "chopped"},
            {"item": "salt and pepper", "quantity": "", "unit": "", "prep_note": "to taste"}
        ],
        "instructions": [
            {"step": 1, "text": "Pat venison dry and season generously with salt and pepper. Let sit 10 minutes."},
            {"step": 2, "text": "Melt 2 tbsp butter in a heavy pan over medium-high heat."},
            {"step": 3, "text": "Sear venison, turning every minute, until nicely browned and medium-rare. Remove to rest."},
            {"step": 4, "text": "Add remaining butter to pan with shallots and mushrooms. Sauté until starting to brown."},
            {"step": 5, "text": "Add garlic and sauté 30 seconds."},
            {"step": 6, "text": "Turn off heat and add brandy. Turn heat back to medium - this prevents flare-ups."},
            {"step": 7, "text": "Cook until brandy is almost evaporated."},
            {"step": 8, "text": "Add mustard, tomato paste, Worcestershire, and stock. Simmer 2 minutes."},
            {"step": 9, "text": "Add cream if using. Taste and adjust seasoning."},
            {"step": 10, "text": "Slice venison and serve with sauce. Garnish with parsley."}
        ],
        "temperature": "",
        "pan_size": "heavy-bottomed skillet",
        "notes": ["Steak Diane originated with Escoffier and was named for the goddess of the hunt", "Works with any venison - deer, elk, moose, caribou, antelope", "Don't overcook venison - medium-rare is best"],
        "tags": ["venison", "deer", "elk", "moose", "steak", "wild game"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "sharp-tailed-grouse-rosehip-hf",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Roast Sharp-tailed Grouse with Rose Hip Glaze",
        "category": "main dishes",
        "attribution": "Honest Food / Hank Shaw",
        "source_note": "From honest-food.net - Prairies bird with prairies garnish",
        "description": "Sharp-tailed grouse roasted with a rose hip jelly glaze. The dark meat should be served pink, like doves.",
        "servings_yield": "2 servings",
        "prep_time": "10 minutes",
        "cook_time": "15-20 minutes",
        "ingredients": [
            {"item": "sharp-tailed grouse", "quantity": "2", "unit": "", "prep_note": "plucked whole"},
            {"item": "rose hip jelly", "quantity": "3", "unit": "tbsp"},
            {"item": "butter", "quantity": "2", "unit": "tbsp", "prep_note": "softened"},
            {"item": "red wine vinegar", "quantity": "1", "unit": "tbsp"},
            {"item": "salt", "quantity": "", "unit": "", "prep_note": "to taste"},
            {"item": "black pepper", "quantity": "", "unit": "", "prep_note": "to taste"}
        ],
        "instructions": [
            {"step": 1, "text": "Preheat oven to 450°F."},
            {"step": 2, "text": "Season grouse inside and out with salt and pepper."},
            {"step": 3, "text": "Mix rose hip jelly with butter and vinegar to make glaze."},
            {"step": 4, "text": "Brush grouse liberally with glaze."},
            {"step": 5, "text": "Roast for 15-20 minutes, basting with glaze halfway through."},
            {"step": 6, "text": "Breast meat should be pink - about 135-140°F internal temperature."},
            {"step": 7, "text": "Rest 5 minutes before serving."}
        ],
        "temperature": "450°F (230°C)",
        "pan_size": "roasting pan",
        "notes": ["Sharp-tailed grouse are red meat and should be served pink like doves", "Substitute currant jelly or crabapple jelly if no rose hip", "From a cooking standpoint, these are essentially giant doves"],
        "tags": ["grouse", "game bird", "roasted", "wild game"],
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
    print(f"  Added: {added} new Honest Food recipes (batch 3)")
    print(f"  Skipped: {skipped} duplicates")
    print(f"  Total recipes now: {len(recipes)}")


if __name__ == "__main__":
    main()
