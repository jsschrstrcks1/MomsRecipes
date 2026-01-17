#!/usr/bin/env python3
"""
Add Honest Food (Hank Shaw) recipes - Batch 4
Organ meats, doves, pigeons, and carp recipes
"""

import json
from pathlib import Path

RECIPES_FILE = Path(__file__).parent.parent / "data" / "recipes.json"

HONEST_FOOD_RECIPES = [
    # ===== ORGAN MEAT RECIPES =====
    {
        "id": "grilled-deer-heart-hf",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Grilled Deer Heart",
        "category": "main dishes",
        "attribution": "Honest Food / Hank Shaw",
        "source_note": "From honest-food.net - Marinated and grilled venison heart",
        "description": "Grilled heart with marinated peppers and onions. When prepared properly, heart has a texture somewhere between ribeye and flank steak.",
        "servings_yield": "4 servings",
        "prep_time": "20 minutes plus 2 hours marinating",
        "cook_time": "10 minutes",
        "ingredients": [
            {"item": "deer or elk heart", "quantity": "1", "unit": "", "prep_note": "cleaned and butterflied"},
            {"item": "olive oil", "quantity": "1/4", "unit": "cup"},
            {"item": "red wine vinegar", "quantity": "2", "unit": "tbsp"},
            {"item": "Worcestershire sauce", "quantity": "1", "unit": "tbsp"},
            {"item": "garlic", "quantity": "3", "unit": "cloves", "prep_note": "minced"},
            {"item": "dried oregano", "quantity": "1", "unit": "tsp"},
            {"item": "salt", "quantity": "1", "unit": "tsp"},
            {"item": "black pepper", "quantity": "1/2", "unit": "tsp"},
            {"item": "bell peppers", "quantity": "2", "unit": "", "prep_note": "for grilling"},
            {"item": "onion", "quantity": "1", "unit": "large", "prep_note": "sliced thick for grilling"}
        ],
        "instructions": [
            {"step": 1, "text": "Clean the heart: cut off the top at the fat line, trim off fat, and remove the 'heart strings' (connective tissue connecting muscle to valves)."},
            {"step": 2, "text": "Butterfly the heart by cutting it open lengthwise so it lies flat."},
            {"step": 3, "text": "Whisk together olive oil, vinegar, Worcestershire, garlic, oregano, salt, and pepper."},
            {"step": 4, "text": "Marinate the heart for 2-4 hours in the refrigerator."},
            {"step": 5, "text": "Get grill very hot. Remove heart from marinade and pat dry."},
            {"step": 6, "text": "Grill heart for 3-4 minutes per side for medium-rare."},
            {"step": 7, "text": "Grill peppers and onions alongside until charred."},
            {"step": 8, "text": "Let heart rest 5 minutes, then slice thin against the grain."},
            {"step": 9, "text": "Serve slices topped with grilled peppers and onions."}
        ],
        "temperature": "High heat grill",
        "pan_size": "",
        "notes": ["Works with deer, elk, moose, antelope, wild boar, or beef heart", "Slice thin against the grain like flank steak", "Heart should be pink in the middle - don't overcook"],
        "tags": ["venison", "heart", "organ meat", "grilled", "wild game"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "deviled-duck-hearts-hf",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Deviled Duck Hearts",
        "category": "appetizers",
        "attribution": "Honest Food / Hank Shaw",
        "source_note": "From honest-food.net - Adapted from Fergus Henderson's The Whole Beast",
        "description": "British-style deviled hearts dusted with mustard and cayenne, served with watercress. 'Deviled' means anything with mustard and cayenne.",
        "servings_yield": "4 appetizer servings",
        "prep_time": "15 minutes",
        "cook_time": "8 minutes",
        "ingredients": [
            {"item": "duck hearts", "quantity": "1", "unit": "lb", "prep_note": "trimmed"},
            {"item": "flour", "quantity": "2", "unit": "tbsp"},
            {"item": "dry mustard", "quantity": "1", "unit": "tsp"},
            {"item": "cayenne pepper", "quantity": "1/2", "unit": "tsp"},
            {"item": "salt", "quantity": "1/2", "unit": "tsp"},
            {"item": "duck fat or butter", "quantity": "2", "unit": "tbsp"},
            {"item": "onion", "quantity": "2", "unit": "tbsp", "prep_note": "finely grated"},
            {"item": "Worcestershire sauce", "quantity": "1", "unit": "tbsp"},
            {"item": "chicken broth", "quantity": "1/4", "unit": "cup"},
            {"item": "fresh parsley", "quantity": "2", "unit": "tbsp", "prep_note": "chopped"},
            {"item": "watercress", "quantity": "2", "unit": "cups", "prep_note": "for serving"},
            {"item": "crusty bread", "quantity": "", "unit": "", "prep_note": "for serving"}
        ],
        "instructions": [
            {"step": 1, "text": "Trim hearts: remove the top above the white fat ring (arterial tissue). Leave small hearts whole, halve larger ones."},
            {"step": 2, "text": "Mix flour, dry mustard, cayenne, and salt together."},
            {"step": 3, "text": "Dust hearts with the seasoned flour mixture."},
            {"step": 4, "text": "Heat duck fat in a pan over medium-high heat."},
            {"step": 5, "text": "Add hearts and sauté 3-4 minutes, shaking pan to let them roll around."},
            {"step": 6, "text": "Add grated onion, Worcestershire sauce, and broth."},
            {"step": 7, "text": "Scrape up browned bits and let sauce reduce to a glaze, about 3 minutes."},
            {"step": 8, "text": "Stir in parsley and serve immediately with watercress and crusty bread."}
        ],
        "temperature": "",
        "pan_size": "large skillet",
        "notes": ["Works with any small hearts: chicken, pheasant, grouse, quail, turkey, rabbit", "Teal hearts stay whole, goose hearts should be sliced", "Adapted from Fergus Henderson's nose-to-tail cooking"],
        "tags": ["duck", "heart", "organ meat", "british", "appetizer", "wild game"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "venison-liver-onions-hf",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Venison Liver and Onions",
        "category": "main dishes",
        "attribution": "Honest Food / Hank Shaw",
        "source_note": "From honest-food.net - Classic preparation with double-soak method",
        "description": "Deer liver and onions done right, with a double-soak method to tame any off-flavors. Best with livers from young animals.",
        "servings_yield": "4 servings",
        "prep_time": "30 minutes plus soaking time",
        "cook_time": "20 minutes",
        "ingredients": [
            {"item": "deer liver", "quantity": "1", "unit": "lb", "prep_note": "sliced 1/2 inch thick"},
            {"item": "salt", "quantity": "1", "unit": "tbsp", "prep_note": "for brine"},
            {"item": "water", "quantity": "4", "unit": "cups", "prep_note": "for brine"},
            {"item": "milk or buttermilk", "quantity": "2", "unit": "cups", "prep_note": "for soaking"},
            {"item": "onions", "quantity": "2", "unit": "large", "prep_note": "sliced thin"},
            {"item": "butter", "quantity": "4", "unit": "tbsp", "prep_note": "divided"},
            {"item": "flour", "quantity": "1/2", "unit": "cup", "prep_note": "for dredging"},
            {"item": "salt and pepper", "quantity": "", "unit": "", "prep_note": "to taste"},
            {"item": "fresh thyme", "quantity": "1", "unit": "tsp", "prep_note": "chopped"}
        ],
        "instructions": [
            {"step": 1, "text": "First soak: Dissolve salt in water. Soak liver slices for 30 minutes."},
            {"step": 2, "text": "Second soak: Drain and soak liver in milk for 1 hour or overnight."},
            {"step": 3, "text": "Melt 2 tbsp butter in a large skillet over medium heat."},
            {"step": 4, "text": "Add onions and cook slowly until caramelized, 15-20 minutes. Remove and keep warm."},
            {"step": 5, "text": "Remove liver from milk, pat dry, and season with salt and pepper."},
            {"step": 6, "text": "Dredge liver slices in flour, shaking off excess."},
            {"step": 7, "text": "Add remaining butter to pan over medium-high heat."},
            {"step": 8, "text": "Sear liver quickly, about 2 minutes per side for medium. Don't overcook."},
            {"step": 9, "text": "Serve liver topped with caramelized onions and fresh thyme."}
        ],
        "temperature": "",
        "pan_size": "large skillet",
        "notes": ["Double soak (brine then dairy) removes off-flavors", "Works with elk, pronghorn, caribou, or any large mammal liver", "Best with livers from young animals"],
        "tags": ["venison", "liver", "organ meat", "classic", "wild game"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "braised-venison-tongue-hf",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Braised Venison Tongue",
        "category": "main dishes",
        "attribution": "Honest Food / Hank Shaw",
        "source_note": "From honest-food.net - Slow braised deer or elk tongue",
        "description": "Tongue braised low and slow until tender, then peeled and sliced. Makes excellent tacos de lengua.",
        "servings_yield": "4-6 servings",
        "prep_time": "15 minutes",
        "cook_time": "3 hours",
        "ingredients": [
            {"item": "venison tongues", "quantity": "2-3", "unit": "", "prep_note": "deer or elk"},
            {"item": "beef or game stock", "quantity": "4", "unit": "cups"},
            {"item": "onion", "quantity": "1", "unit": "", "prep_note": "quartered"},
            {"item": "carrot", "quantity": "1", "unit": "", "prep_note": "chunked"},
            {"item": "celery", "quantity": "2", "unit": "stalks"},
            {"item": "garlic", "quantity": "4", "unit": "cloves", "prep_note": "whole"},
            {"item": "fresh thyme", "quantity": "4", "unit": "sprigs"},
            {"item": "bay leaves", "quantity": "2", "unit": ""},
            {"item": "salt", "quantity": "1", "unit": "tsp"},
            {"item": "black peppercorns", "quantity": "1", "unit": "tsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Place tongues in a pot with stock, vegetables, and aromatics."},
            {"step": 2, "text": "Add enough water to cover if needed."},
            {"step": 3, "text": "Bring to a simmer, cover, and place in 350°F oven."},
            {"step": 4, "text": "Braise until a knife inserts easily, about 2-3 hours depending on size."},
            {"step": 5, "text": "Let tongues cool in the braising liquid until cool enough to handle."},
            {"step": 6, "text": "Peel the outer membrane off the tongues - it should slip off easily."},
            {"step": 7, "text": "Slice and serve warm, or dice for tacos."},
            {"step": 8, "text": "Strain and reserve braising liquid for reheating or as a sauce base."}
        ],
        "temperature": "350°F (175°C)",
        "pan_size": "Dutch oven",
        "notes": ["Peel the membrane when tongue is warm - it comes off easily", "Great for tacos de lengua with cilantro and onion", "Can be served cold sliced, or reheated in braising liquid"],
        "tags": ["venison", "tongue", "organ meat", "braised", "wild game"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    # ===== DOVE & PIGEON RECIPES =====
    {
        "id": "peppered-dove-breasts-hf",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Peppered Dove Breasts (Doves au Poivre)",
        "category": "main dishes",
        "attribution": "Honest Food / Hank Shaw",
        "source_note": "From honest-food.net - French classic adapted for dove",
        "description": "Dove breasts seared in butter with an easy pan sauce of shallots, brandy, cream, and peppercorns. Simple, fast, and delicious.",
        "servings_yield": "4 servings",
        "prep_time": "10 minutes",
        "cook_time": "10 minutes",
        "ingredients": [
            {"item": "dove breasts", "quantity": "16", "unit": "", "prep_note": "boneless"},
            {"item": "butter", "quantity": "4", "unit": "tbsp", "prep_note": "divided"},
            {"item": "shallot", "quantity": "1", "unit": "large", "prep_note": "minced"},
            {"item": "brandy", "quantity": "2", "unit": "tbsp"},
            {"item": "chicken or game stock", "quantity": "1/2", "unit": "cup"},
            {"item": "heavy cream", "quantity": "1/4", "unit": "cup"},
            {"item": "black pepper", "quantity": "1", "unit": "tbsp", "prep_note": "freshly coarse-ground"},
            {"item": "green peppercorns", "quantity": "1", "unit": "tbsp", "prep_note": "brined, optional"},
            {"item": "salt", "quantity": "", "unit": "", "prep_note": "to taste"}
        ],
        "instructions": [
            {"step": 1, "text": "Salt dove breasts well and keep refrigerated until ready to cook."},
            {"step": 2, "text": "Heat 3 tbsp butter in a skillet over medium-high heat."},
            {"step": 3, "text": "Sear dove breasts 2 minutes on one side only. Remove to rest."},
            {"step": 4, "text": "Add shallot to pan and sauté 1 minute."},
            {"step": 5, "text": "Turn off heat and add brandy. Turn heat back to medium."},
            {"step": 6, "text": "Add stock and both peppers. Simmer 2 minutes."},
            {"step": 7, "text": "Add cream and simmer until slightly thickened."},
            {"step": 8, "text": "Swirl in remaining 1 tbsp butter."},
            {"step": 9, "text": "Spoon sauce over dove breasts and serve."}
        ],
        "temperature": "",
        "pan_size": "large skillet",
        "notes": ["Pepper is the dominant flavor - use freshly ground", "Green peppercorns found near capers in most stores", "Dove breast should be pink inside"],
        "tags": ["dove", "french", "game bird", "pan sauce", "wild game"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "turkish-roast-pigeon-hf",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Turkish Roast Pigeon with Bulgur",
        "category": "main dishes",
        "attribution": "Honest Food / Hank Shaw",
        "source_note": "From honest-food.net - Middle Eastern stuffed pigeon",
        "description": "Turkish-style roast pigeon stuffed with spiced bulgur wheat and walnuts. The Middle East cooks the best pigeon.",
        "servings_yield": "2-4 servings",
        "prep_time": "45 minutes plus brining",
        "cook_time": "45 minutes",
        "ingredients": [
            {"item": "pigeons or squab", "quantity": "2", "unit": "", "prep_note": "plucked whole"},
            {"item": "salt", "quantity": "1/4", "unit": "cup", "prep_note": "for brine"},
            {"item": "water", "quantity": "4", "unit": "cups", "prep_note": "for brine"},
            {"item": "bulgur wheat", "quantity": "1", "unit": "cup"},
            {"item": "chicken stock", "quantity": "1.5", "unit": "cups"},
            {"item": "walnuts", "quantity": "1/2", "unit": "cup", "prep_note": "chopped"},
            {"item": "onion", "quantity": "1", "unit": "small", "prep_note": "diced"},
            {"item": "olive oil", "quantity": "2", "unit": "tbsp"},
            {"item": "cinnamon", "quantity": "1/2", "unit": "tsp"},
            {"item": "cardamom", "quantity": "1/4", "unit": "tsp"},
            {"item": "allspice", "quantity": "1/4", "unit": "tsp"},
            {"item": "fresh mint", "quantity": "2", "unit": "tbsp", "prep_note": "chopped"},
            {"item": "lemon juice", "quantity": "1", "unit": "tbsp"},
            {"item": "celery stalks", "quantity": "2", "unit": "", "prep_note": "for roasting rack"}
        ],
        "instructions": [
            {"step": 1, "text": "Brine pigeons: dissolve salt in water, submerge birds, refrigerate 6-12 hours."},
            {"step": 2, "text": "Make stuffing: Bring stock to simmer with cinnamon, cardamom, allspice, and 1 tsp salt. Add bulgur, cover, simmer 15 minutes."},
            {"step": 3, "text": "Meanwhile, heat oil and fry onions and walnuts until colored."},
            {"step": 4, "text": "Combine cooked bulgur with onion-walnut mixture. Cool slightly, then add mint and lemon juice."},
            {"step": 5, "text": "Remove pigeons from brine, pat dry, and stuff loosely with bulgur mixture."},
            {"step": 6, "text": "Preheat oven to 350°F."},
            {"step": 7, "text": "Place celery stalks in pan, lay pigeons breast-side down on celery. Roast 25 minutes."},
            {"step": 8, "text": "Turn birds over and roast 10 more minutes."},
            {"step": 9, "text": "Increase heat to 500°F and roast 10 minutes to brown and crisp."},
            {"step": 10, "text": "Serve on remaining bulgur with lemon juice and fleur de sel."}
        ],
        "temperature": "350°F rising to 500°F",
        "pan_size": "cast-iron pan or roasting pan",
        "notes": ["Brining keeps lean wild pigeons from drying out", "Can substitute ptarmigan, sharp-tailed grouse, or Cornish hens", "Goes well with raki or medium-bodied red wine"],
        "tags": ["pigeon", "turkish", "middle eastern", "bulgur", "stuffed", "wild game"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "pigeon-tortellini-hf",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Pigeon Tortellini",
        "category": "main dishes",
        "attribution": "Honest Food / Hank Shaw",
        "source_note": "From honest-food.net - Stuffed pasta with ground pigeon",
        "description": "Morsels of pasta stuffed with ground pigeon, sweet wine, herbs, and roasted garlic, served with a juniper butter sauce.",
        "servings_yield": "4 servings",
        "prep_time": "1 hour",
        "cook_time": "30 minutes",
        "ingredients": [
            {"item": "pigeon meat", "quantity": "1", "unit": "lb", "prep_note": "ground or finely chopped"},
            {"item": "roasted garlic", "quantity": "4", "unit": "cloves", "prep_note": "mashed"},
            {"item": "Marsala or sweet wine", "quantity": "2", "unit": "tbsp"},
            {"item": "fresh rosemary", "quantity": "1", "unit": "tsp", "prep_note": "minced"},
            {"item": "fresh sage", "quantity": "1", "unit": "tsp", "prep_note": "minced"},
            {"item": "Parmesan cheese", "quantity": "1/4", "unit": "cup", "prep_note": "grated"},
            {"item": "salt", "quantity": "1", "unit": "tsp"},
            {"item": "black pepper", "quantity": "1/2", "unit": "tsp"},
            {"item": "egg", "quantity": "1", "unit": "", "prep_note": "for filling"},
            {"item": "fresh pasta sheets", "quantity": "1", "unit": "lb"},
            {"item": "butter", "quantity": "4", "unit": "tbsp", "prep_note": "for sauce"},
            {"item": "juniper berries", "quantity": "6", "unit": "", "prep_note": "crushed"},
            {"item": "chicken stock", "quantity": "1/2", "unit": "cup"}
        ],
        "instructions": [
            {"step": 1, "text": "Make filling: Mix ground pigeon with roasted garlic, wine, herbs, Parmesan, salt, pepper, and egg."},
            {"step": 2, "text": "Cut pasta into 3-inch squares."},
            {"step": 3, "text": "Place small spoonful of filling in center of each square."},
            {"step": 4, "text": "Fold corner to corner to make triangle, pressing edges to seal."},
            {"step": 5, "text": "Wrap around finger and pinch corners together to form tortellini shape."},
            {"step": 6, "text": "Bring large pot of salted water to boil."},
            {"step": 7, "text": "Meanwhile, make sauce: Melt butter with juniper berries, add stock, simmer 5 minutes."},
            {"step": 8, "text": "Cook tortellini until they float, about 3-4 minutes."},
            {"step": 9, "text": "Toss with juniper butter sauce and extra Parmesan."}
        ],
        "temperature": "",
        "pan_size": "large pot and saucepan",
        "notes": ["Can substitute dove, pheasant, or duck for pigeon", "Juniper adds a piney, gin-like note to the butter", "Can make tortellini ahead and freeze"],
        "tags": ["pigeon", "pasta", "italian", "stuffed", "wild game"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    # ===== FISH RECIPES =====
    {
        "id": "sichuan-crispy-carp-hf",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Sichuan Crispy Fried Carp",
        "category": "main dishes",
        "attribution": "Honest Food / Hank Shaw",
        "source_note": "From honest-food.net - When life gives you carp, think East",
        "description": "Chinese-style whole fried carp - crispy and delicious. Carp is prized in Asia, and this is an excellent way to prepare it.",
        "servings_yield": "2-4 servings",
        "prep_time": "30 minutes",
        "cook_time": "15 minutes",
        "ingredients": [
            {"item": "whole carp", "quantity": "1", "unit": "", "prep_note": "2-3 lb, cleaned and scaled"},
            {"item": "cornstarch", "quantity": "1", "unit": "cup"},
            {"item": "vegetable oil", "quantity": "", "unit": "", "prep_note": "for deep frying"},
            {"item": "green onions", "quantity": "3", "unit": "", "prep_note": "chopped"},
            {"item": "fresh ginger", "quantity": "1", "unit": "inch", "prep_note": "minced"},
            {"item": "garlic", "quantity": "3", "unit": "cloves", "prep_note": "minced"},
            {"item": "Chinese cooking wine", "quantity": "2", "unit": "tbsp"},
            {"item": "soy sauce", "quantity": "3", "unit": "tbsp"},
            {"item": "rice vinegar", "quantity": "2", "unit": "tbsp"},
            {"item": "sugar", "quantity": "2", "unit": "tbsp"},
            {"item": "dried red chiles", "quantity": "4-6", "unit": ""},
            {"item": "Sichuan peppercorns", "quantity": "1", "unit": "tsp"},
            {"item": "chicken stock", "quantity": "1/2", "unit": "cup"}
        ],
        "instructions": [
            {"step": 1, "text": "Score the fish in a crosshatch pattern on both sides, cutting to the bone."},
            {"step": 2, "text": "Pat fish very dry and dust heavily with cornstarch, getting into all the cuts."},
            {"step": 3, "text": "Heat oil in wok or deep pot to 375°F."},
            {"step": 4, "text": "Carefully lower fish into oil and fry until golden and crispy, about 8-10 minutes. Keep oil temperature up."},
            {"step": 5, "text": "Remove fish to a platter."},
            {"step": 6, "text": "Pour off all but 2 tbsp oil. Add ginger, garlic, chiles, and Sichuan peppercorns. Stir-fry 30 seconds."},
            {"step": 7, "text": "Add wine, soy sauce, vinegar, sugar, and stock. Simmer 2 minutes."},
            {"step": 8, "text": "Pour sauce over fish and top with green onions."}
        ],
        "temperature": "375°F oil temperature",
        "pan_size": "wok or large pot",
        "notes": ["Works with any whole fish that fits in a wok", "Scoring helps the fish cook evenly and get crispy", "Carp is prized in Asian cuisines"],
        "tags": ["carp", "fish", "chinese", "fried", "sichuan"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "catfish-etouffee-hf",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Catfish Étouffée (Smothered Catfish)",
        "category": "main dishes",
        "attribution": "Honest Food / Hank Shaw",
        "source_note": "From honest-food.net - Cajun smothered catfish",
        "description": "Cajun smothered catfish in a rich tomato and pepper sauce. A wonderful way to celebrate this fish.",
        "servings_yield": "4 servings",
        "prep_time": "20 minutes",
        "cook_time": "30 minutes",
        "ingredients": [
            {"item": "catfish fillets", "quantity": "1.5", "unit": "lb", "prep_note": "cut into chunks"},
            {"item": "butter", "quantity": "4", "unit": "tbsp"},
            {"item": "onion", "quantity": "1", "unit": "large", "prep_note": "diced"},
            {"item": "celery", "quantity": "2", "unit": "stalks", "prep_note": "diced"},
            {"item": "green bell pepper", "quantity": "1", "unit": "", "prep_note": "diced"},
            {"item": "garlic", "quantity": "4", "unit": "cloves", "prep_note": "minced"},
            {"item": "flour", "quantity": "2", "unit": "tbsp"},
            {"item": "tomato paste", "quantity": "2", "unit": "tbsp"},
            {"item": "diced tomatoes", "quantity": "1", "unit": "cup"},
            {"item": "fish or chicken stock", "quantity": "2", "unit": "cups"},
            {"item": "Cajun seasoning", "quantity": "1", "unit": "tbsp"},
            {"item": "cayenne pepper", "quantity": "1/4", "unit": "tsp"},
            {"item": "green onions", "quantity": "4", "unit": "", "prep_note": "sliced"},
            {"item": "fresh parsley", "quantity": "2", "unit": "tbsp", "prep_note": "chopped"},
            {"item": "steamed rice", "quantity": "", "unit": "", "prep_note": "for serving"}
        ],
        "instructions": [
            {"step": 1, "text": "Melt butter in a large skillet over medium heat."},
            {"step": 2, "text": "Add onion, celery, and bell pepper. Sauté until soft, about 8 minutes."},
            {"step": 3, "text": "Add garlic and sauté 1 minute."},
            {"step": 4, "text": "Stir in flour and cook 2 minutes, stirring constantly."},
            {"step": 5, "text": "Add tomato paste and tomatoes. Cook 3 minutes."},
            {"step": 6, "text": "Pour in stock and add Cajun seasoning and cayenne. Simmer 10 minutes."},
            {"step": 7, "text": "Add catfish chunks and simmer gently until fish is cooked, about 8-10 minutes."},
            {"step": 8, "text": "Stir in green onions and parsley."},
            {"step": 9, "text": "Serve over steamed rice."}
        ],
        "temperature": "",
        "pan_size": "large skillet or Dutch oven",
        "notes": ["Can add small shrimp or crawfish 5 minutes before end", "Don't stir too vigorously or fish will break up", "Use any fresh catfish - wild or farmed"],
        "tags": ["catfish", "cajun", "etouffee", "southern", "fish"],
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
    print(f"  Added: {added} new Honest Food recipes (batch 4)")
    print(f"  Skipped: {skipped} duplicates")
    print(f"  Total recipes now: {len(recipes)}")


if __name__ == "__main__":
    main()
