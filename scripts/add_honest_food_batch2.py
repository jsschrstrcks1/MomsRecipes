#!/usr/bin/env python3
"""
Add Honest Food (Hank Shaw) recipes - Wild Game Batch 2
Birds: snipe, woodcock, pheasant, goose, duck
"""

import json
from pathlib import Path

RECIPES_FILE = Path(__file__).parent.parent / "data" / "recipes.json"

HONEST_FOOD_RECIPES = [
    # ===== SNIPE RECIPES =====
    {
        "id": "roast-snipe-hf",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Roast Snipe",
        "category": "main dishes",
        "attribution": "Hank Shaw / Hunter Angler Gardener Cook",
        "source_note": "From honest-food.net - Roast Snipe",
        "description": "Simple roast snipe over a bed of sea beans - a rare treat with flavor all out of proportion to its size.",
        "servings_yield": "2 servings as appetizer, or 1 as main",
        "prep_time": "15 minutes",
        "cook_time": "15 minutes",
        "ingredients": [
            {"item": "snipe", "quantity": "4", "unit": "", "prep_note": "plucked, gutted"},
            {"item": "butter", "quantity": "4", "unit": "tbsp", "prep_note": "softened"},
            {"item": "salt", "quantity": "", "unit": "", "prep_note": "to taste"},
            {"item": "black pepper", "quantity": "", "unit": "", "prep_note": "to taste"},
            {"item": "fresh thyme", "quantity": "1", "unit": "tsp"},
            {"item": "sea beans or samphire", "quantity": "1", "unit": "cup", "prep_note": "optional, for serving"}
        ],
        "instructions": [
            {"step": 1, "text": "Preheat oven to 450°F."},
            {"step": 2, "text": "Pat snipe dry and season inside and out with salt and pepper."},
            {"step": 3, "text": "Rub softened butter over the birds and sprinkle with thyme."},
            {"step": 4, "text": "Roast in hot oven for 12-15 minutes for medium-rare."},
            {"step": 5, "text": "Rest 5 minutes before serving."},
            {"step": 6, "text": "Serve over blanched sea beans or samphire if available."}
        ],
        "temperature": "450°F (230°C)",
        "pan_size": "roasting pan",
        "notes": ["One snipe makes a great appetizer, four make a hearty meal", "Snipe has intense flavor despite small size", "Cook medium-rare to medium"],
        "tags": ["snipe", "roasted", "wild game", "shorebird", "unusual protein"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "fried-snipe-hf",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Jesse's Hot Fried Snipe",
        "category": "main dishes",
        "attribution": "Hank Shaw / Hunter Angler Gardener Cook",
        "source_note": "From honest-food.net - Fried Snipe",
        "description": "Southern-style fried snipe doused with a hot sauce, honey, butter and garlic glaze.",
        "servings_yield": "4 servings",
        "prep_time": "20 minutes",
        "cook_time": "15 minutes",
        "ingredients": [
            {"item": "snipe", "quantity": "8", "unit": "", "prep_note": "split in half"},
            {"item": "buttermilk", "quantity": "2", "unit": "cups"},
            {"item": "flour", "quantity": "1", "unit": "cup"},
            {"item": "salt", "quantity": "1", "unit": "tsp"},
            {"item": "black pepper", "quantity": "1/2", "unit": "tsp"},
            {"item": "cayenne", "quantity": "1/4", "unit": "tsp"},
            {"item": "vegetable oil", "quantity": "", "unit": "", "prep_note": "for frying"},
            {"item": "butter", "quantity": "4", "unit": "tbsp"},
            {"item": "hot sauce", "quantity": "1/4", "unit": "cup"},
            {"item": "honey", "quantity": "2", "unit": "tbsp"},
            {"item": "garlic", "quantity": "2", "unit": "cloves", "prep_note": "minced"}
        ],
        "instructions": [
            {"step": 1, "text": "Soak split snipe in buttermilk for at least 30 minutes."},
            {"step": 2, "text": "Mix flour with salt, pepper, and cayenne."},
            {"step": 3, "text": "Heat oil to 350°F in a deep pan or fryer."},
            {"step": 4, "text": "Dredge snipe in seasoned flour, shaking off excess."},
            {"step": 5, "text": "Fry until golden and cooked through, about 4-5 minutes."},
            {"step": 6, "text": "Meanwhile, melt butter with hot sauce, honey, and garlic."},
            {"step": 7, "text": "Drain fried snipe and immediately toss with the hot butter sauce."},
            {"step": 8, "text": "Serve immediately."}
        ],
        "temperature": "350°F oil",
        "pan_size": "deep fryer or heavy pot",
        "notes": ["Also works with doves and quail", "From Jesse Griffiths' book Afield"],
        "tags": ["snipe", "fried", "southern", "wild game", "hot sauce"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "salmis-of-snipe-hf",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Salmis of Snipe",
        "category": "main dishes",
        "attribution": "Hank Shaw / Hunter Angler Gardener Cook",
        "source_note": "From honest-food.net - Salmis of Snipe",
        "description": "A classic French snipe recipe where birds are roasted, sauce made from bones, served with mushrooms.",
        "servings_yield": "4 servings",
        "prep_time": "30 minutes",
        "cook_time": "1 hour",
        "ingredients": [
            {"item": "snipe", "quantity": "8", "unit": "", "prep_note": "plucked and gutted"},
            {"item": "butter", "quantity": "4", "unit": "tbsp"},
            {"item": "shallots", "quantity": "3", "unit": "", "prep_note": "minced"},
            {"item": "cremini or wild mushrooms", "quantity": "8", "unit": "oz", "prep_note": "sliced"},
            {"item": "red wine", "quantity": "1", "unit": "cup"},
            {"item": "game or chicken stock", "quantity": "1", "unit": "cup"},
            {"item": "fresh thyme", "quantity": "1", "unit": "tsp"},
            {"item": "bay leaf", "quantity": "1", "unit": ""},
            {"item": "Cognac or brandy", "quantity": "2", "unit": "tbsp"},
            {"item": "salt and pepper", "quantity": "", "unit": "", "prep_note": "to taste"},
            {"item": "toast points", "quantity": "", "unit": "", "prep_note": "for serving"}
        ],
        "instructions": [
            {"step": 1, "text": "Roast snipe at 450°F for 10-12 minutes until medium-rare. Let rest."},
            {"step": 2, "text": "Remove breasts and legs from carcasses. Set meat aside, keeping warm."},
            {"step": 3, "text": "Chop carcasses and sauté in butter over high heat for 5 minutes."},
            {"step": 4, "text": "Add shallots and mushrooms, cook until mushrooms release liquid."},
            {"step": 5, "text": "Add wine, stock, thyme, and bay leaf. Simmer 30 minutes."},
            {"step": 6, "text": "Strain sauce, pressing on solids. Return to pan and reduce by half."},
            {"step": 7, "text": "Add Cognac and reserved mushrooms. Season with salt and pepper."},
            {"step": 8, "text": "Arrange snipe pieces on toast points and spoon sauce over."}
        ],
        "temperature": "450°F for roasting",
        "pan_size": "",
        "notes": ["Classic French technique called 'salmis'", "The sauce from the bones is the star", "Works with woodcock, dove, or squab"],
        "tags": ["snipe", "french", "salmis", "mushrooms", "wild game"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },

    # ===== WOODCOCK RECIPES =====
    {
        "id": "roast-woodcock-cumberland-hf",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Roast Woodcock with Cumberland Sauce",
        "category": "main dishes",
        "attribution": "Hank Shaw / Hunter Angler Gardener Cook",
        "source_note": "From honest-food.net - Roast Woodcock",
        "description": "Classic roast woodcock with Cumberland sauce - the king of game birds.",
        "servings_yield": "2 servings",
        "prep_time": "20 minutes",
        "cook_time": "20 minutes",
        "ingredients": [
            {"item": "woodcock", "quantity": "2", "unit": "", "prep_note": "plucked, entrails removed (keep livers)"},
            {"item": "butter", "quantity": "4", "unit": "tbsp", "prep_note": "softened"},
            {"item": "salt and pepper", "quantity": "", "unit": "", "prep_note": "to taste"},
            {"item": "toast", "quantity": "2", "unit": "slices", "prep_note": "for serving"},
            {"item": "red currant jelly", "quantity": "1/2", "unit": "cup", "prep_note": "for Cumberland sauce"},
            {"item": "port wine", "quantity": "1/4", "unit": "cup"},
            {"item": "orange zest", "quantity": "1", "unit": "tbsp"},
            {"item": "orange juice", "quantity": "2", "unit": "tbsp"},
            {"item": "lemon juice", "quantity": "1", "unit": "tbsp"},
            {"item": "Dijon mustard", "quantity": "1", "unit": "tsp"},
            {"item": "ginger", "quantity": "1/4", "unit": "tsp", "prep_note": "ground"}
        ],
        "instructions": [
            {"step": 1, "text": "Preheat oven to 450°F."},
            {"step": 2, "text": "Season woodcock inside and out with salt and pepper. Rub with butter."},
            {"step": 3, "text": "Roast for 15-18 minutes for medium-rare (internal 130°F)."},
            {"step": 4, "text": "Meanwhile, make Cumberland sauce: Heat currant jelly with port, citrus zest and juice, mustard, and ginger until combined."},
            {"step": 5, "text": "If you saved the livers, mash them on toast as a base."},
            {"step": 6, "text": "Rest woodcock 5 minutes, then serve on toast with Cumberland sauce."}
        ],
        "temperature": "450°F (230°C)",
        "pan_size": "roasting pan",
        "notes": ["Many consider woodcock the king of game birds", "Traditionally served on toast spread with the bird's liver", "Cook medium-rare - the meat should be pink"],
        "tags": ["woodcock", "roasted", "british", "cumberland sauce", "wild game", "unusual protein"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "pan-seared-woodcock-hf",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Pan-Seared Woodcock with Mushrooms",
        "category": "main dishes",
        "attribution": "Hank Shaw / Hunter Angler Gardener Cook",
        "source_note": "From honest-food.net - Pan-Seared Woodcock",
        "description": "Simple pan-seared woodcock served with roasted mushrooms and Brussels sprouts.",
        "servings_yield": "2 servings",
        "prep_time": "15 minutes",
        "cook_time": "25 minutes",
        "ingredients": [
            {"item": "woodcock", "quantity": "2", "unit": "", "prep_note": "breasts and legs separated"},
            {"item": "butter", "quantity": "4", "unit": "tbsp", "prep_note": "divided"},
            {"item": "cremini mushrooms", "quantity": "8", "unit": "oz", "prep_note": "quartered"},
            {"item": "Brussels sprouts", "quantity": "8", "unit": "oz", "prep_note": "halved"},
            {"item": "shallot", "quantity": "1", "unit": "", "prep_note": "minced"},
            {"item": "white wine or vermouth", "quantity": "1/4", "unit": "cup"},
            {"item": "fresh thyme", "quantity": "1", "unit": "tsp"},
            {"item": "salt and pepper", "quantity": "", "unit": "", "prep_note": "to taste"}
        ],
        "instructions": [
            {"step": 1, "text": "Roast mushrooms and Brussels sprouts at 400°F with 2 tbsp butter until browned, about 20 minutes."},
            {"step": 2, "text": "Season woodcock pieces with salt and pepper."},
            {"step": 3, "text": "Heat remaining butter in a skillet over medium-high heat."},
            {"step": 4, "text": "Sear woodcock breasts skin-side down for 2 minutes. Flip and cook 1-2 more minutes for medium-rare."},
            {"step": 5, "text": "Remove breasts. Add legs and cook 4-5 minutes total."},
            {"step": 6, "text": "Remove legs. Add shallot, cook 30 seconds. Add wine and thyme, scraping pan."},
            {"step": 7, "text": "Serve woodcock over roasted vegetables with pan sauce."}
        ],
        "temperature": "400°F for vegetables",
        "pan_size": "cast iron skillet",
        "notes": ["Breasts cook faster than legs - cook separately", "Woodcock has a strong, gamey flavor in a good way"],
        "tags": ["woodcock", "pan-seared", "mushrooms", "wild game"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },

    # ===== PHEASANT RECIPES =====
    {
        "id": "pheasant-mushrooms-cream-hf",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Pheasant with Mushrooms and Cream",
        "category": "main dishes",
        "attribution": "Hank Shaw / Hunter Angler Gardener Cook",
        "source_note": "From honest-food.net - Pheasant with Mushrooms and Cream",
        "description": "Simple, homey pheasant breasts with fresh mushrooms, cream and brandy.",
        "servings_yield": "4 servings",
        "prep_time": "15 minutes",
        "cook_time": "25 minutes",
        "ingredients": [
            {"item": "pheasant breasts", "quantity": "4", "unit": "", "prep_note": "boneless"},
            {"item": "butter", "quantity": "4", "unit": "tbsp"},
            {"item": "shallots", "quantity": "2", "unit": "", "prep_note": "minced"},
            {"item": "fresh mushrooms", "quantity": "8", "unit": "oz", "prep_note": "sliced"},
            {"item": "brandy", "quantity": "1/4", "unit": "cup"},
            {"item": "heavy cream", "quantity": "1", "unit": "cup"},
            {"item": "fresh tarragon", "quantity": "1", "unit": "tbsp", "prep_note": "chopped"},
            {"item": "salt and pepper", "quantity": "", "unit": "", "prep_note": "to taste"}
        ],
        "instructions": [
            {"step": 1, "text": "Season pheasant breasts with salt and pepper."},
            {"step": 2, "text": "Heat butter in a large skillet over medium-high heat."},
            {"step": 3, "text": "Sear pheasant breasts for 3-4 minutes per side until golden. Remove and keep warm."},
            {"step": 4, "text": "Add shallots and mushrooms to pan. Cook until mushrooms are browned, about 5 minutes."},
            {"step": 5, "text": "Add brandy and carefully ignite to burn off alcohol (or just let it reduce)."},
            {"step": 6, "text": "Add cream and tarragon. Simmer until sauce thickens slightly, about 5 minutes."},
            {"step": 7, "text": "Return pheasant to pan, spooning sauce over. Cook 2-3 more minutes."},
            {"step": 8, "text": "Slice pheasant and serve with mushroom cream sauce."}
        ],
        "temperature": "",
        "pan_size": "large skillet",
        "notes": ["Also works with grouse, chicken, or turkey breast", "Don't overcook - pheasant dries out easily"],
        "tags": ["pheasant", "mushrooms", "cream", "french", "wild game"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "fried-pheasant-pickle-brine-hf",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Pickle-Brined Fried Pheasant",
        "category": "main dishes",
        "attribution": "Hank Shaw / Hunter Angler Gardener Cook",
        "source_note": "From honest-food.net - Fried Pheasant",
        "description": "Pheasant brined in pickle juice then fried - tangy, tender, and crispy.",
        "servings_yield": "4 servings",
        "prep_time": "15 minutes plus brining",
        "cook_time": "20 minutes",
        "ingredients": [
            {"item": "pheasant", "quantity": "1", "unit": "", "prep_note": "cut into pieces"},
            {"item": "pickle juice", "quantity": "2", "unit": "cups", "prep_note": "from dill pickles"},
            {"item": "buttermilk", "quantity": "1", "unit": "cup"},
            {"item": "flour", "quantity": "1.5", "unit": "cups"},
            {"item": "cornstarch", "quantity": "1/2", "unit": "cup"},
            {"item": "salt", "quantity": "1", "unit": "tsp"},
            {"item": "black pepper", "quantity": "1", "unit": "tsp"},
            {"item": "paprika", "quantity": "1", "unit": "tsp"},
            {"item": "garlic powder", "quantity": "1/2", "unit": "tsp"},
            {"item": "vegetable oil", "quantity": "", "unit": "", "prep_note": "for frying"}
        ],
        "instructions": [
            {"step": 1, "text": "Brine pheasant pieces in pickle juice for 4-24 hours in refrigerator."},
            {"step": 2, "text": "Remove from brine and soak in buttermilk for 30 minutes."},
            {"step": 3, "text": "Mix flour, cornstarch, salt, pepper, paprika, and garlic powder."},
            {"step": 4, "text": "Heat oil to 325°F - lower than typical fried chicken to account for leaner meat."},
            {"step": 5, "text": "Dredge pheasant pieces in flour mixture."},
            {"step": 6, "text": "Fry in batches for 12-15 minutes, turning occasionally, until golden and cooked through."},
            {"step": 7, "text": "Drain on wire rack and season with salt while hot."}
        ],
        "temperature": "325°F oil",
        "pan_size": "Dutch oven or deep fryer",
        "notes": ["Lower frying temperature prevents drying out lean game birds", "Also works great with grouse and partridge", "The pickle brine adds flavor and tenderizes"],
        "tags": ["pheasant", "fried", "pickle brine", "southern", "wild game"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },

    # ===== DUCK/GOOSE RECIPES =====
    {
        "id": "duck-confit-hf",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Duck or Goose Confit",
        "category": "main dishes",
        "attribution": "Hank Shaw / Hunter Angler Gardener Cook",
        "source_note": "From honest-food.net - Duck Confit",
        "description": "Classic French duck confit - legs slowly cooked in duck fat until meltingly tender.",
        "servings_yield": "4 servings",
        "prep_time": "20 minutes plus curing",
        "cook_time": "3-4 hours",
        "ingredients": [
            {"item": "duck or goose legs", "quantity": "4", "unit": ""},
            {"item": "kosher salt", "quantity": "1/4", "unit": "cup"},
            {"item": "black pepper", "quantity": "1", "unit": "tbsp"},
            {"item": "fresh thyme", "quantity": "1", "unit": "tbsp"},
            {"item": "bay leaves", "quantity": "2", "unit": "", "prep_note": "crumbled"},
            {"item": "garlic", "quantity": "4", "unit": "cloves", "prep_note": "minced"},
            {"item": "duck fat", "quantity": "4", "unit": "cups", "prep_note": "or enough to cover"}
        ],
        "instructions": [
            {"step": 1, "text": "Mix salt, pepper, thyme, bay leaves, and garlic. Rub generously over duck legs."},
            {"step": 2, "text": "Place legs in a container, cover, and refrigerate 24-48 hours."},
            {"step": 3, "text": "Rinse legs and pat dry thoroughly."},
            {"step": 4, "text": "Preheat oven to 250°F."},
            {"step": 5, "text": "Place legs in a single layer in an oven-safe pot. Cover completely with duck fat."},
            {"step": 6, "text": "Cook uncovered for 3-4 hours until meat is very tender and pulls easily from bone."},
            {"step": 7, "text": "Let cool in fat. Store submerged in fat in refrigerator for up to 3 months."},
            {"step": 8, "text": "To serve, remove legs from fat and crisp skin in a hot skillet."}
        ],
        "temperature": "250°F (120°C)",
        "pan_size": "Dutch oven or deep baking dish",
        "notes": ["Skin-on specklebelly and Canada goose legs are the gold standard", "Do NOT make confit from breasts - they become livery", "Stored in fat, confit keeps for months"],
        "tags": ["duck", "goose", "confit", "french", "preserved", "wild game"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "goose-breast-orange-greek-hf",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Goose Breast with Orange (Greek Style)",
        "category": "main dishes",
        "attribution": "Hank Shaw / Hunter Angler Gardener Cook",
        "source_note": "From honest-food.net - Goose Breast with Orange",
        "description": "Duck l'orange with a Greek twist using ouzo - works beautifully with goose.",
        "servings_yield": "4 servings",
        "prep_time": "15 minutes",
        "cook_time": "20 minutes",
        "ingredients": [
            {"item": "goose breasts", "quantity": "2", "unit": "", "prep_note": "skin scored"},
            {"item": "salt and pepper", "quantity": "", "unit": "", "prep_note": "to taste"},
            {"item": "orange juice", "quantity": "1", "unit": "cup", "prep_note": "fresh"},
            {"item": "orange zest", "quantity": "1", "unit": "tbsp"},
            {"item": "ouzo", "quantity": "1/4", "unit": "cup"},
            {"item": "honey", "quantity": "2", "unit": "tbsp"},
            {"item": "chicken or game stock", "quantity": "1/2", "unit": "cup"},
            {"item": "butter", "quantity": "2", "unit": "tbsp", "prep_note": "cold"}
        ],
        "instructions": [
            {"step": 1, "text": "Score goose breast skin in a crosshatch pattern. Season with salt and pepper."},
            {"step": 2, "text": "Place breasts skin-side down in a cold pan. Turn heat to medium."},
            {"step": 3, "text": "Render fat slowly for 10-12 minutes until skin is very crispy."},
            {"step": 4, "text": "Flip and cook 3-4 more minutes for medium-rare (130°F internal)."},
            {"step": 5, "text": "Remove breasts and rest. Pour off most fat."},
            {"step": 6, "text": "Add orange juice, zest, ouzo, honey, and stock to pan. Reduce by half."},
            {"step": 7, "text": "Remove from heat and whisk in cold butter to make glossy sauce."},
            {"step": 8, "text": "Slice goose breast against the grain and serve with sauce."}
        ],
        "temperature": "",
        "pan_size": "cast iron skillet",
        "notes": ["Start skin-side down in a COLD pan for crispiest skin", "Goose and duck should be served medium-rare like steak", "Ouzo adds anise flavor - substitute Pernod or skip if unavailable"],
        "tags": ["goose", "duck", "orange sauce", "greek", "wild game"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "german-rabbit-stew-hf",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "German Rabbit Stew with Lemon",
        "category": "main dishes",
        "attribution": "Hank Shaw / Hunter Angler Gardener Cook",
        "source_note": "From honest-food.net - German Rabbit Stew",
        "description": "A light, brothy German rabbit stew with lemon, bay leaves, capers and sour cream.",
        "servings_yield": "4-6 servings",
        "prep_time": "20 minutes",
        "cook_time": "1.5 hours",
        "ingredients": [
            {"item": "rabbit", "quantity": "1", "unit": "", "prep_note": "cut into pieces"},
            {"item": "butter", "quantity": "4", "unit": "tbsp"},
            {"item": "onion", "quantity": "1", "unit": "large", "prep_note": "sliced"},
            {"item": "chicken or rabbit stock", "quantity": "4", "unit": "cups"},
            {"item": "white wine", "quantity": "1", "unit": "cup"},
            {"item": "bay leaves", "quantity": "3", "unit": ""},
            {"item": "lemon zest", "quantity": "1", "unit": "tbsp"},
            {"item": "lemon juice", "quantity": "3", "unit": "tbsp"},
            {"item": "capers", "quantity": "3", "unit": "tbsp"},
            {"item": "sour cream", "quantity": "1/2", "unit": "cup"},
            {"item": "fresh parsley", "quantity": "2", "unit": "tbsp", "prep_note": "chopped"},
            {"item": "salt and pepper", "quantity": "", "unit": "", "prep_note": "to taste"}
        ],
        "instructions": [
            {"step": 1, "text": "Season rabbit pieces with salt and pepper."},
            {"step": 2, "text": "Brown rabbit in butter over medium-high heat. Remove and set aside."},
            {"step": 3, "text": "Sauté onion until softened, about 5 minutes."},
            {"step": 4, "text": "Add stock, wine, bay leaves, and lemon zest. Return rabbit to pot."},
            {"step": 5, "text": "Simmer covered for 1-1.5 hours until rabbit is tender."},
            {"step": 6, "text": "Remove rabbit. Add lemon juice and capers to broth."},
            {"step": 7, "text": "Temper sour cream with a little hot broth, then stir into pot."},
            {"step": 8, "text": "Return rabbit, garnish with parsley. Serve with roasted potatoes."}
        ],
        "temperature": "",
        "pan_size": "Dutch oven",
        "notes": ["Different from hasenpfeffer - this is light and brothy", "Rabbits are mild white meat, hares are strongly flavored red meat", "Knockout dish with roasted potatoes"],
        "tags": ["rabbit", "german", "stew", "lemon", "wild game"],
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
    print(f"  Added: {added} new Honest Food recipes (batch 2)")
    print(f"  Skipped: {skipped} duplicates")
    print(f"  Total recipes now: {len(recipes)}")


if __name__ == "__main__":
    main()
