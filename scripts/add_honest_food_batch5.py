#!/usr/bin/env python3
"""
Add Honest Food (Hank Shaw) recipes - Batch 5
Wild turkey and Cajun sausage recipes
"""

import json
from pathlib import Path

RECIPES_FILE = Path(__file__).parent.parent / "data" / "recipes.json"

HONEST_FOOD_RECIPES = [
    # ===== WILD TURKEY RECIPES =====
    {
        "id": "turkey-carnitas-hf",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Wild Turkey Carnitas",
        "category": "main dishes",
        "attribution": "Honest Food / Hank Shaw",
        "source_note": "From honest-food.net - Braised and crisped turkey for tacos",
        "description": "The perfect solution for tough wild turkey legs. Braised until tender, then shredded and crisped in lard for tacos.",
        "servings_yield": "8 servings",
        "prep_time": "20 minutes",
        "cook_time": "2-4 hours",
        "ingredients": [
            {"item": "wild turkey legs and thighs", "quantity": "3-4", "unit": "lb"},
            {"item": "turkey or chicken stock", "quantity": "4", "unit": "cups"},
            {"item": "water", "quantity": "", "unit": "", "prep_note": "to cover"},
            {"item": "onion", "quantity": "1", "unit": "large", "prep_note": "quartered"},
            {"item": "garlic", "quantity": "6", "unit": "cloves", "prep_note": "smashed"},
            {"item": "bay leaves", "quantity": "2", "unit": ""},
            {"item": "dried oregano", "quantity": "1", "unit": "tbsp"},
            {"item": "cumin", "quantity": "1", "unit": "tsp"},
            {"item": "salt", "quantity": "1", "unit": "tbsp"},
            {"item": "lard or vegetable oil", "quantity": "3", "unit": "tbsp", "prep_note": "for crisping"},
            {"item": "corn tortillas", "quantity": "", "unit": "", "prep_note": "for serving"},
            {"item": "lime wedges", "quantity": "", "unit": "", "prep_note": "for serving"},
            {"item": "white onion", "quantity": "", "unit": "", "prep_note": "diced, for serving"},
            {"item": "cilantro", "quantity": "", "unit": "", "prep_note": "chopped, for serving"},
            {"item": "salsa verde", "quantity": "", "unit": "", "prep_note": "for serving"}
        ],
        "instructions": [
            {"step": 1, "text": "Place turkey pieces in a large Dutch oven with stock, onion, garlic, bay leaves, oregano, cumin, and salt."},
            {"step": 2, "text": "Add enough water to cover the meat."},
            {"step": 3, "text": "Bring to a simmer, then cook gently until meat is very tender - 90 minutes for domestic, up to 4 hours for old wild tom."},
            {"step": 4, "text": "Remove turkey and let cool. Reserve cooking liquid."},
            {"step": 5, "text": "Shred meat off the bones, discarding tendons and cartilage."},
            {"step": 6, "text": "When ready to serve, heat lard in a large skillet over high heat."},
            {"step": 7, "text": "Add shredded meat and let sit without stirring until one side is crispy and browned."},
            {"step": 8, "text": "Stir and repeat if desired for more crispy bits."},
            {"step": 9, "text": "Serve in warm tortillas with lime, onion, cilantro, and salsa."}
        ],
        "temperature": "",
        "pan_size": "Dutch oven",
        "notes": ["The shredded meat keeps for a week in the fridge before crisping", "Also works with pheasant, old chicken, or guinea hen", "Crisp only the portion you're serving"],
        "tags": ["wild turkey", "mexican", "tacos", "braised", "wild game"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "bbq-turkey-legs-hf",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "BBQ Turkey Legs with Maple-Bourbon Sauce",
        "category": "main dishes",
        "attribution": "Honest Food / Hank Shaw",
        "source_note": "From honest-food.net - Barbecued wild turkey thighs",
        "description": "Slow-smoked turkey legs with a homemade maple-bourbon barbecue sauce. Thighs work better than drumsticks since they have fewer tough tendons.",
        "servings_yield": "4 servings",
        "prep_time": "30 minutes",
        "cook_time": "3 hours",
        "ingredients": [
            {"item": "turkey thighs", "quantity": "4", "unit": "", "prep_note": "wild or domestic"},
            {"item": "dry rub", "quantity": "", "unit": "", "prep_note": "your favorite"},
            {"item": "ketchup", "quantity": "1", "unit": "cup"},
            {"item": "maple syrup", "quantity": "1/4", "unit": "cup"},
            {"item": "bourbon", "quantity": "2", "unit": "tbsp"},
            {"item": "apple cider vinegar", "quantity": "2", "unit": "tbsp"},
            {"item": "Worcestershire sauce", "quantity": "1", "unit": "tbsp"},
            {"item": "smoked paprika", "quantity": "1", "unit": "tsp"},
            {"item": "garlic powder", "quantity": "1/2", "unit": "tsp"},
            {"item": "cayenne pepper", "quantity": "1/4", "unit": "tsp"},
            {"item": "salt", "quantity": "", "unit": "", "prep_note": "to taste"}
        ],
        "instructions": [
            {"step": 1, "text": "Coat turkey thighs with dry rub and refrigerate for at least 2 hours or overnight."},
            {"step": 2, "text": "Make the sauce: Combine ketchup, maple syrup, bourbon, vinegar, Worcestershire, paprika, garlic powder, and cayenne in a saucepan. Simmer 10 minutes."},
            {"step": 3, "text": "Set up smoker or grill for indirect heat at 275°F."},
            {"step": 4, "text": "Smoke thighs until internal temperature reaches 165°F, about 2-3 hours."},
            {"step": 5, "text": "During the last 30 minutes, brush with barbecue sauce every 10 minutes."},
            {"step": 6, "text": "Let rest 10 minutes before serving with extra sauce."}
        ],
        "temperature": "275°F (135°C)",
        "pan_size": "smoker or grill",
        "notes": ["Thighs are preferred over drumsticks - fewer tendons", "Can also be done in oven at 275°F with liquid smoke", "Works with store-bought or wild turkey"],
        "tags": ["wild turkey", "bbq", "smoked", "bourbon", "wild game"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "turkey-leg-stew-hf",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Southwestern Turkey Leg Stew",
        "category": "soups",
        "attribution": "Honest Food / Hank Shaw",
        "source_note": "From honest-food.net - New Mexican stew with chicos",
        "description": "A classic New Mexican stew with dried corn (chicos), chiles, and braised turkey legs. The perfect use for tough wild turkey drumsticks.",
        "servings_yield": "6 servings",
        "prep_time": "30 minutes plus soaking",
        "cook_time": "3 hours",
        "ingredients": [
            {"item": "turkey legs", "quantity": "2", "unit": "", "prep_note": "wild or domestic"},
            {"item": "dried chicos or posole corn", "quantity": "1", "unit": "cup", "prep_note": "soaked overnight"},
            {"item": "dried New Mexico chiles", "quantity": "4", "unit": "", "prep_note": "stemmed and seeded"},
            {"item": "chicken or turkey stock", "quantity": "6", "unit": "cups"},
            {"item": "onion", "quantity": "1", "unit": "large", "prep_note": "diced"},
            {"item": "garlic", "quantity": "4", "unit": "cloves", "prep_note": "minced"},
            {"item": "cumin", "quantity": "1", "unit": "tsp"},
            {"item": "oregano", "quantity": "1", "unit": "tsp"},
            {"item": "salt", "quantity": "", "unit": "", "prep_note": "to taste"},
            {"item": "lime wedges", "quantity": "", "unit": "", "prep_note": "for serving"},
            {"item": "cilantro", "quantity": "", "unit": "", "prep_note": "for serving"},
            {"item": "radishes", "quantity": "", "unit": "", "prep_note": "sliced, for serving"}
        ],
        "instructions": [
            {"step": 1, "text": "Soak chicos or posole in water overnight. Drain."},
            {"step": 2, "text": "Toast dried chiles in a dry pan until fragrant. Cover with hot water and soak 20 minutes. Blend smooth."},
            {"step": 3, "text": "In a large pot, brown turkey legs on all sides. Remove and set aside."},
            {"step": 4, "text": "Sauté onion until soft, add garlic, cumin, and oregano."},
            {"step": 5, "text": "Add chile puree, stock, corn, and turkey legs."},
            {"step": 6, "text": "Simmer until turkey is fall-off-the-bone tender and corn is soft, 2-3 hours."},
            {"step": 7, "text": "Remove turkey, shred meat, discard bones and tendons."},
            {"step": 8, "text": "Return meat to pot. Season with salt."},
            {"step": 9, "text": "Serve with lime, cilantro, and radishes."}
        ],
        "temperature": "",
        "pan_size": "large soup pot",
        "notes": ["Chicos are dried roasted corn used in New Mexican cooking", "Can substitute hominy if chicos unavailable", "The long cooking time tenderizes even old wild turkey"],
        "tags": ["wild turkey", "stew", "southwestern", "new mexico", "wild game"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "turkey-gumbo-hf",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Wild Turkey Gumbo",
        "category": "soups",
        "attribution": "Honest Food / Hank Shaw",
        "source_note": "From honest-food.net - Classic Louisiana gumbo with turkey",
        "description": "One of the great uses for turkey drumsticks - a rich gumbo with andouille sausage and seafood. Uses turkey legs, thighs, and wings.",
        "servings_yield": "8-10 servings",
        "prep_time": "45 minutes",
        "cook_time": "3 hours",
        "ingredients": [
            {"item": "turkey legs and thighs", "quantity": "3", "unit": "lb"},
            {"item": "andouille sausage", "quantity": "1", "unit": "lb", "prep_note": "sliced"},
            {"item": "shrimp", "quantity": "1", "unit": "lb", "prep_note": "peeled (or crawfish)"},
            {"item": "vegetable oil", "quantity": "3/4", "unit": "cup"},
            {"item": "flour", "quantity": "3/4", "unit": "cup"},
            {"item": "onion", "quantity": "2", "unit": "cups", "prep_note": "diced"},
            {"item": "celery", "quantity": "1", "unit": "cup", "prep_note": "diced"},
            {"item": "green bell pepper", "quantity": "1", "unit": "cup", "prep_note": "diced"},
            {"item": "garlic", "quantity": "6", "unit": "cloves", "prep_note": "minced"},
            {"item": "turkey or chicken stock", "quantity": "8", "unit": "cups"},
            {"item": "bay leaves", "quantity": "2", "unit": ""},
            {"item": "thyme", "quantity": "1", "unit": "tbsp", "prep_note": "fresh"},
            {"item": "cayenne pepper", "quantity": "1/2", "unit": "tsp"},
            {"item": "okra", "quantity": "2", "unit": "cups", "prep_note": "sliced, optional"},
            {"item": "filé powder", "quantity": "1", "unit": "tbsp", "prep_note": "optional"},
            {"item": "green onions", "quantity": "1", "unit": "cup", "prep_note": "sliced"},
            {"item": "cooked rice", "quantity": "", "unit": "", "prep_note": "for serving"}
        ],
        "instructions": [
            {"step": 1, "text": "Simmer turkey in stock until tender, 2-3 hours. Remove turkey, reserve stock. Shred meat when cool."},
            {"step": 2, "text": "Make roux: Heat oil in a large pot over medium heat. Whisk in flour."},
            {"step": 3, "text": "Cook roux, stirring constantly, until dark chocolate brown, 30-45 minutes."},
            {"step": 4, "text": "Add onion, celery, and bell pepper (the 'trinity'). Cook 10 minutes."},
            {"step": 5, "text": "Add garlic and cook 1 minute."},
            {"step": 6, "text": "Add reserved stock, bay leaves, thyme, and cayenne. Simmer 30 minutes."},
            {"step": 7, "text": "Add andouille sausage and cook 15 minutes."},
            {"step": 8, "text": "Add okra if using and cook 10 minutes."},
            {"step": 9, "text": "Add shredded turkey and shrimp. Cook until shrimp are pink, about 5 minutes."},
            {"step": 10, "text": "Remove from heat, stir in filé powder if using. Top with green onions."},
            {"step": 11, "text": "Serve over rice."}
        ],
        "temperature": "",
        "pan_size": "large Dutch oven",
        "notes": ["Never boil gumbo after adding filé or it becomes stringy", "Turkey breast doesn't work well - use dark meat", "Can use any smoked sausage if andouille unavailable"],
        "tags": ["wild turkey", "gumbo", "cajun", "louisiana", "wild game"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    # ===== CAJUN SAUSAGE RECIPES =====
    {
        "id": "andouille-sausage-hf",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Homemade Andouille Sausage",
        "category": "main dishes",
        "attribution": "Honest Food / Hank Shaw",
        "source_note": "From honest-food.net - Cajun smoked sausage",
        "description": "A heavily seasoned Cajun sausage, almost always smoked. Can be made with any meat - pork, venison, bear, or beef.",
        "servings_yield": "5 lb sausage",
        "prep_time": "1 hour",
        "cook_time": "3-4 hours smoking",
        "ingredients": [
            {"item": "pork shoulder or venison", "quantity": "4", "unit": "lb", "prep_note": "cut into chunks"},
            {"item": "pork fat or bacon", "quantity": "1", "unit": "lb", "prep_note": "cut into chunks"},
            {"item": "kosher salt", "quantity": "3", "unit": "tbsp"},
            {"item": "garlic", "quantity": "8", "unit": "cloves", "prep_note": "minced"},
            {"item": "cayenne pepper", "quantity": "2", "unit": "tsp"},
            {"item": "black pepper", "quantity": "1", "unit": "tbsp"},
            {"item": "paprika", "quantity": "2", "unit": "tbsp"},
            {"item": "dried thyme", "quantity": "2", "unit": "tsp"},
            {"item": "powdered milk", "quantity": "1/4", "unit": "cup"},
            {"item": "ice water", "quantity": "1/2", "unit": "cup"},
            {"item": "hog casings", "quantity": "", "unit": "", "prep_note": "soaked in water"}
        ],
        "instructions": [
            {"step": 1, "text": "Chill meat and fat in freezer until very cold but not frozen, about 30 minutes."},
            {"step": 2, "text": "Grind meat and fat through coarse die (6-7mm)."},
            {"step": 3, "text": "Mix ground meat with all seasonings and powdered milk."},
            {"step": 4, "text": "Add ice water and mix thoroughly until the mixture is tacky and binds together."},
            {"step": 5, "text": "Stuff into hog casings, twisting into 6-inch links."},
            {"step": 6, "text": "Let sausages dry uncovered in refrigerator overnight."},
            {"step": 7, "text": "Set up smoker with pecan or other hardwood at 175-200°F."},
            {"step": 8, "text": "Smoke until internal temperature reaches 150°F, about 3-4 hours."},
            {"step": 9, "text": "Fully cook before eating by grilling, pan-frying, or adding to gumbo."}
        ],
        "temperature": "175-200°F smoking",
        "pan_size": "smoker",
        "notes": ["Can use venison, bear, beef, or any meat", "Pecan is traditional wood for smoking andouille", "Smoked sausages can be frozen after smoking and before final cooking"],
        "tags": ["sausage", "andouille", "cajun", "smoked", "wild game"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "boudin-sausage-hf",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Louisiana Boudin",
        "category": "main dishes",
        "attribution": "Honest Food / Hank Shaw",
        "source_note": "From honest-food.net - Cajun rice and meat sausage",
        "description": "A cooked sausage with meat, liver, rice, and Cajun seasonings. A Louisiana favorite that's loosely stuffed into casings.",
        "servings_yield": "about 4 lb boudin",
        "prep_time": "1 hour",
        "cook_time": "2 hours",
        "ingredients": [
            {"item": "pork shoulder or wild game", "quantity": "1.5", "unit": "lb", "prep_note": "cubed"},
            {"item": "pork or duck liver", "quantity": "0.5", "unit": "lb"},
            {"item": "pork fat or bacon", "quantity": "0.5", "unit": "lb", "prep_note": "cubed"},
            {"item": "onion", "quantity": "1", "unit": "large", "prep_note": "chopped"},
            {"item": "celery", "quantity": "2", "unit": "stalks", "prep_note": "chopped"},
            {"item": "green bell pepper", "quantity": "1", "unit": "", "prep_note": "chopped"},
            {"item": "garlic", "quantity": "6", "unit": "cloves", "prep_note": "chopped"},
            {"item": "bay leaf", "quantity": "1", "unit": ""},
            {"item": "kosher salt", "quantity": "4", "unit": "tbsp"},
            {"item": "Cajun seasoning", "quantity": "3-5", "unit": "tbsp"},
            {"item": "cooked white rice", "quantity": "2", "unit": "cups", "prep_note": "long-grain"},
            {"item": "fresh parsley", "quantity": "1", "unit": "cup", "prep_note": "chopped"},
            {"item": "green onions", "quantity": "1", "unit": "cup", "prep_note": "chopped"},
            {"item": "hog casings", "quantity": "", "unit": "", "prep_note": "soaked in water"}
        ],
        "instructions": [
            {"step": 1, "text": "Place meat, liver, fat, onion, celery, pepper, garlic, and bay leaf in a pot. Cover with water."},
            {"step": 2, "text": "Simmer until meat is very tender, about 1.5 hours. Reserve cooking liquid."},
            {"step": 3, "text": "Remove bay leaf. Grind everything through coarse die."},
            {"step": 4, "text": "Add ground mixture to a large bowl with salt and Cajun seasoning."},
            {"step": 5, "text": "Add cooked rice, parsley, and green onions."},
            {"step": 6, "text": "Add up to 4 cups reserved cooking liquid and mix 3-5 minutes until cohesive but still loose."},
            {"step": 7, "text": "Stuff loosely into hog casings, twist into 8-inch links."},
            {"step": 8, "text": "Poach in salted water at 165-170°F for 10 minutes."},
            {"step": 9, "text": "Serve immediately, or grill until casing is crispy."}
        ],
        "temperature": "165-170°F poaching",
        "pan_size": "large pot",
        "notes": ["Everything is cooked before stuffing - a 'cooked sausage'", "Can also be formed into balls and fried (boudin balls)", "Best grilled so casing gets crispy", "Works with duck, turkey, venison, or pork"],
        "tags": ["sausage", "boudin", "cajun", "louisiana", "rice", "wild game"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "venison-sausage-hf",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Country-Style Venison Sausage",
        "category": "main dishes",
        "attribution": "Honest Food / Hank Shaw",
        "source_note": "From honest-food.net - Rich sausage with bay and garlic",
        "description": "A rich country-style venison sausage where ground bay leaves and garlic are the dominant flavors. Especially good for grilling.",
        "servings_yield": "5 lb sausage",
        "prep_time": "45 minutes",
        "cook_time": "varies",
        "ingredients": [
            {"item": "venison", "quantity": "3.5", "unit": "lb", "prep_note": "cubed, very cold"},
            {"item": "pork fat or bacon", "quantity": "1.5", "unit": "lb", "prep_note": "cubed, very cold"},
            {"item": "kosher salt", "quantity": "3", "unit": "tbsp"},
            {"item": "bay leaves", "quantity": "6", "unit": "", "prep_note": "ground to powder"},
            {"item": "garlic", "quantity": "8", "unit": "cloves", "prep_note": "minced"},
            {"item": "black pepper", "quantity": "1", "unit": "tbsp"},
            {"item": "dried sage", "quantity": "1", "unit": "tsp"},
            {"item": "dried thyme", "quantity": "1", "unit": "tsp"},
            {"item": "red pepper flakes", "quantity": "1/2", "unit": "tsp"},
            {"item": "ice water", "quantity": "1/2", "unit": "cup"},
            {"item": "hog casings", "quantity": "", "unit": "", "prep_note": "soaked in water"}
        ],
        "instructions": [
            {"step": 1, "text": "Grind bay leaves to powder in a spice grinder."},
            {"step": 2, "text": "Mix all seasonings together."},
            {"step": 3, "text": "Grind very cold venison and fat through coarse die."},
            {"step": 4, "text": "Add seasonings and ice water to ground meat."},
            {"step": 5, "text": "Mix by hand or with paddle attachment until mixture is tacky, about 2 minutes."},
            {"step": 6, "text": "Fry a small patty to test seasoning. Adjust salt if needed."},
            {"step": 7, "text": "Stuff into hog casings, twisting into 5-6 inch links."},
            {"step": 8, "text": "Refrigerate overnight uncovered to dry casings."},
            {"step": 9, "text": "Grill, pan-fry, or use in other recipes."}
        ],
        "temperature": "",
        "pan_size": "",
        "notes": ["Keep meat and fat very cold for best texture", "Bay leaves must be ground to powder - whole bay leaf bits are unpleasant", "Especially good on the grill"],
        "tags": ["sausage", "venison", "country style", "wild game"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "polish-duck-sausage-hf",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Polish Duck Sausages",
        "category": "main dishes",
        "attribution": "Honest Food / Hank Shaw",
        "source_note": "From honest-food.net - Fine-grained emulsified sausage",
        "description": "A fine-grained, almost emulsified sausage like a real Polish kielbasa, but with duck as the dominant meat. Snow goose would be perfect here too.",
        "servings_yield": "5 lb sausage",
        "prep_time": "1 hour",
        "cook_time": "1 hour poaching",
        "ingredients": [
            {"item": "duck meat", "quantity": "3", "unit": "lb", "prep_note": "from legs and thighs"},
            {"item": "pork fat or bacon", "quantity": "1.5", "unit": "lb"},
            {"item": "pork shoulder", "quantity": "0.5", "unit": "lb", "prep_note": "optional, for binding"},
            {"item": "kosher salt", "quantity": "3", "unit": "tbsp"},
            {"item": "garlic", "quantity": "6", "unit": "cloves", "prep_note": "minced"},
            {"item": "black pepper", "quantity": "1", "unit": "tbsp"},
            {"item": "marjoram", "quantity": "1", "unit": "tbsp"},
            {"item": "mustard seeds", "quantity": "1", "unit": "tsp", "prep_note": "ground"},
            {"item": "caraway seeds", "quantity": "1/2", "unit": "tsp", "prep_note": "optional"},
            {"item": "powdered milk", "quantity": "1/4", "unit": "cup"},
            {"item": "ice water", "quantity": "1/2", "unit": "cup"},
            {"item": "hog casings", "quantity": "", "unit": "", "prep_note": "soaked in water"}
        ],
        "instructions": [
            {"step": 1, "text": "Chill all meat and fat in freezer until very firm but not frozen."},
            {"step": 2, "text": "Grind meat and fat through fine die (4mm)."},
            {"step": 3, "text": "Put ground meat in mixer with paddle. Add all seasonings and powdered milk."},
            {"step": 4, "text": "Mix on low while adding ice water. Continue until mixture becomes sticky and emulsified, about 5 minutes."},
            {"step": 5, "text": "Stuff into hog casings, twisting into 6-inch links."},
            {"step": 6, "text": "Poach in 170°F water until internal temperature reaches 150°F, about 45 minutes."},
            {"step": 7, "text": "Chill in ice water to stop cooking."},
            {"step": 8, "text": "Grill or pan-fry before serving."}
        ],
        "temperature": "170°F poaching",
        "pan_size": "large pot",
        "notes": ["Fine grind and emulsification create the smooth kielbasa texture", "Snow goose works perfectly", "Marjoram is essential for Polish flavor"],
        "tags": ["sausage", "duck", "polish", "kielbasa", "wild game"],
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
    print(f"  Added: {added} new Honest Food recipes (batch 5)")
    print(f"  Skipped: {skipped} duplicates")
    print(f"  Total recipes now: {len(recipes)}")


if __name__ == "__main__":
    main()
