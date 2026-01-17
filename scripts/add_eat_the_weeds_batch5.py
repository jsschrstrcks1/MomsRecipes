#!/usr/bin/env python3
"""
Add Eat the Weeds recipes - Batch 5.

This batch includes: cattail, akebi, eryngo, sea lettuce, Surinam cherry,
ivy gourd, eel, gar, and guinea pig (cuy) recipes from eattheweeds.com.
"""

import json
from pathlib import Path

RECIPES_FILE = Path(__file__).parent.parent / "data" / "recipes.json"

ETW_BATCH5_RECIPES = [
    # ===== CATTAIL RECIPES =====
    {
        "id": "scalloped-cattails-etw",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Scalloped Cattails",
        "category": "sides",
        "attribution": "Eat the Weeds - Green Deane",
        "source_note": "Wild foraging recipe from eattheweeds.com",
        "description": "Creamy baked cattail casserole with Swiss cheese.",
        "ingredients": [
            {"item": "chopped cattail tops", "quantity": "2", "unit": "cups", "prep_note": "green, not brown"},
            {"item": "beaten eggs", "quantity": "2", "unit": ""},
            {"item": "melted butter", "quantity": "1/2", "unit": "cup"},
            {"item": "sugar", "quantity": "1/2", "unit": "tsp"},
            {"item": "nutmeg", "quantity": "1/2", "unit": "tsp"},
            {"item": "black pepper", "quantity": "", "unit": "", "prep_note": "to taste"},
            {"item": "scalded milk", "quantity": "1", "unit": "cup"},
            {"item": "grated Swiss cheese", "quantity": "", "unit": "", "prep_note": "optional"},
            {"item": "butter", "quantity": "", "unit": "", "prep_note": "for topping"}
        ],
        "instructions": [
            {"step": 1, "text": "Combine cattail tops with eggs, melted butter, sugar, nutmeg, and pepper."},
            {"step": 2, "text": "Slowly blend in scalded milk."},
            {"step": 3, "text": "Pour into greased casserole, top with cheese and butter."},
            {"step": 4, "text": "Bake at 275°F for 30 minutes."}
        ],
        "temperature": "275°F (135°C)",
        "tags": ["cattail", "casserole", "sides", "foraging", "eat the weeds"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "cattail-pollen-biscuits-etw",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Cattail Pollen Biscuits",
        "category": "breads",
        "attribution": "Eat the Weeds - Green Deane",
        "source_note": "Wild foraging recipe from eattheweeds.com",
        "description": "Golden biscuits made with foraged cattail pollen.",
        "ingredients": [
            {"item": "cattail pollen", "quantity": "1/4", "unit": "cup"},
            {"item": "flour", "quantity": "1.75", "unit": "cups"},
            {"item": "baking powder", "quantity": "3", "unit": "tsp"},
            {"item": "salt", "quantity": "1", "unit": "tsp"},
            {"item": "shortening", "quantity": "4", "unit": "tbsp"},
            {"item": "milk", "quantity": "3/4", "unit": "cup"}
        ],
        "instructions": [
            {"step": 1, "text": "Mix all dry ingredients."},
            {"step": 2, "text": "Cut in shortening and add milk."},
            {"step": 3, "text": "Cut into biscuits."},
            {"step": 4, "text": "Bake at 425°F for 20 minutes."}
        ],
        "temperature": "425°F (220°C)",
        "tags": ["cattail", "pollen", "biscuits", "foraging", "eat the weeds"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "cattail-pollen-pancakes-etw",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Cattail Pollen Pancakes",
        "category": "breakfast",
        "attribution": "Eat the Weeds - Green Deane",
        "source_note": "Wild foraging recipe from eattheweeds.com",
        "description": "Fluffy pancakes made with foraged cattail pollen.",
        "ingredients": [
            {"item": "cattail pollen", "quantity": "1/2", "unit": "cup"},
            {"item": "flour", "quantity": "1/2", "unit": "cup"},
            {"item": "baking powder", "quantity": "2", "unit": "tbsp"},
            {"item": "salt", "quantity": "1", "unit": "tsp"},
            {"item": "egg", "quantity": "1", "unit": ""},
            {"item": "milk", "quantity": "1", "unit": "cup"},
            {"item": "bacon drippings", "quantity": "3", "unit": "tbsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Combine all ingredients."},
            {"step": 2, "text": "Pour dollar-sized, four-inch pancakes onto hot griddle."},
            {"step": 3, "text": "Cook until bubbles form, flip and cook other side."}
        ],
        "tags": ["cattail", "pollen", "pancakes", "breakfast", "foraging", "eat the weeds"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "cattail-casserole-etw",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Cattail Casserole",
        "category": "main-dishes",
        "attribution": "Eat the Weeds - Green Deane",
        "source_note": "Wild foraging recipe from eattheweeds.com",
        "description": "Savory cattail casserole with cheese.",
        "ingredients": [
            {"item": "scraped cattail spikes", "quantity": "2", "unit": "cups"},
            {"item": "bread crumbs", "quantity": "1", "unit": "cup"},
            {"item": "beaten egg", "quantity": "1", "unit": ""},
            {"item": "milk", "quantity": "1/2", "unit": "cup"},
            {"item": "salt and pepper", "quantity": "", "unit": "", "prep_note": "to taste"},
            {"item": "diced onion", "quantity": "1", "unit": ""},
            {"item": "shredded cheddar cheese", "quantity": "1/2", "unit": "cup"}
        ],
        "instructions": [
            {"step": 1, "text": "Mix all ingredients in casserole dish."},
            {"step": 2, "text": "Bake at 350°F for 25 minutes."}
        ],
        "temperature": "350°F (175°C)",
        "tags": ["cattail", "casserole", "foraging", "eat the weeds"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    # ===== AKEBI RECIPE =====
    {
        "id": "akebi-miso-itame-etw",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Akebi Pod Miso Itame",
        "category": "sides",
        "attribution": "Eat the Weeds - Green Deane",
        "source_note": "Wild foraging recipe from eattheweeds.com",
        "description": "Japanese stir-fried chocolate vine pods with miso.",
        "ingredients": [
            {"item": "akebi pod", "quantity": "1", "unit": "", "prep_note": "inner fruit removed"},
            {"item": "sesame oil", "quantity": "2", "unit": "tbsp"},
            {"item": "miso paste", "quantity": "1-2", "unit": "tsp", "prep_note": "sweet Kansai-style preferred"},
            {"item": "sugar", "quantity": "1", "unit": "tsp"},
            {"item": "shoyu (soy sauce)", "quantity": "1", "unit": "tsp"},
            {"item": "ryorishu (cooking sake)", "quantity": "2", "unit": "tbsp"},
            {"item": "shiso leaf", "quantity": "", "unit": "", "prep_note": "fresh, optional garnish"}
        ],
        "instructions": [
            {"step": 1, "text": "Optionally soak pod halves in warm water for 30-60 minutes to reduce bitterness; pat dry."},
            {"step": 2, "text": "Combine all liquid ingredients in a bowl, dissolving the miso paste and sugar together."},
            {"step": 3, "text": "Heat oil in a fry pan. Add sliced akebi pod and sauté covered until softened, approximately 2 minutes."},
            {"step": 4, "text": "Pour in the liquid mixture, reduce heat, and simmer until most liquid evaporates (1-2 minutes). Monitor closely to prevent burning."},
            {"step": 5, "text": "Serve on a plate; garnish with chopped shiso leaf if desired."}
        ],
        "tags": ["akebi", "chocolate vine", "japanese", "miso", "foraging", "eat the weeds"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    # ===== ERYNGO RECIPES =====
    {
        "id": "candied-eryngo-roots-etw",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Candied Eryngo Roots (Elizabethan)",
        "category": "desserts",
        "attribution": "Eat the Weeds - Green Deane",
        "source_note": "Historical wild foraging recipe from eattheweeds.com",
        "description": "Traditional Elizabethan candied sea holly roots, once famous as an aphrodisiac.",
        "ingredients": [
            {"item": "fresh eryngo roots", "quantity": "", "unit": ""},
            {"item": "spring water", "quantity": "", "unit": "", "prep_note": "for boiling"},
            {"item": "sugar", "quantity": "", "unit": "", "prep_note": "equal weight to roots"},
            {"item": "rose water", "quantity": "", "unit": ""},
            {"item": "fair water", "quantity": "", "unit": "", "prep_note": "equal amount to rose water"}
        ],
        "instructions": [
            {"step": 1, "text": "Boil fresh roots in spring water until they reach the consistency of cooked parsnips."},
            {"step": 2, "text": "Cut lengthwise and remove the pith with a knife."},
            {"step": 3, "text": "Peel and soak in fresh water, then wring dry with cloth."},
            {"step": 4, "text": "Bundle 3-4 roots together, tying at each end."},
            {"step": 5, "text": "Create a syrup from sugar, rose water, and fair water."},
            {"step": 6, "text": "Boil bundled roots in syrup until liquid nearly evaporates."},
            {"step": 7, "text": "Shake in basin to distribute syrup coating."},
            {"step": 8, "text": "Dry by fire and store in boxes."}
        ],
        "notes": ["Famous in Colchester, England in Elizabethan times", "Considered an aphrodisiac"],
        "tags": ["eryngo", "sea holly", "candied", "elizabethan", "historical", "foraging", "eat the weeds"],
        "confidence": {"overall": "medium", "flags": ["Historical recipe"]},
        "image_refs": []
    },
    # ===== SEA LETTUCE RECIPES =====
    {
        "id": "sea-lettuce-soup-etw",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Sea Lettuce Soup",
        "category": "soups",
        "attribution": "Eat the Weeds - Green Deane",
        "source_note": "Wild foraging recipe from eattheweeds.com",
        "description": "Light Asian-style soup with sea lettuce (ulva) seaweed.",
        "ingredients": [
            {"item": "chicken stock", "quantity": "4", "unit": "cups"},
            {"item": "ulva (sea lettuce) sheets", "quantity": "2", "unit": ""},
            {"item": "eggs", "quantity": "2", "unit": ""},
            {"item": "salt and pepper", "quantity": "", "unit": "", "prep_note": "to taste"},
            {"item": "sesame oil", "quantity": "1/2", "unit": "tsp"},
            {"item": "green scallions", "quantity": "1-2", "unit": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Bring stock to a boil."},
            {"step": 2, "text": "Add sea lettuce and stir until soft."},
            {"step": 3, "text": "Stir in beaten eggs and boil briefly, then remove from heat."},
            {"step": 4, "text": "Season with salt and pepper."},
            {"step": 5, "text": "Add sesame oil, garnish with scallions, and serve."}
        ],
        "notes": ["Wash sea lettuce well and optionally soak 2 hours before using"],
        "tags": ["seaweed", "ulva", "sea lettuce", "soup", "asian", "foraging", "eat the weeds"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "toasted-sea-lettuce-etw",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Toasted Sea Lettuce",
        "category": "snacks",
        "attribution": "Eat the Weeds - Green Deane",
        "source_note": "Wild foraging recipe from eattheweeds.com",
        "description": "Crispy toasted sea lettuce with sesame, similar to Korean nori.",
        "ingredients": [
            {"item": "ulva (sea lettuce) sheets", "quantity": "6", "unit": ""},
            {"item": "salt", "quantity": "1/2", "unit": "tsp"},
            {"item": "sesame oil", "quantity": "1.5", "unit": "tbsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Mix salt and sesame oil, rubbing thinly onto the sea lettuce."},
            {"step": 2, "text": "Stack 6 sheets and roll; marinate 5 minutes."},
            {"step": 3, "text": "Unroll and cook each sheet separately in a hot pan over low heat until crisp."},
            {"step": 4, "text": "Cut into pieces and serve with hot rice."}
        ],
        "notes": ["Refrigerate 2-3 days or freeze for six months", "Can also toast over charcoal"],
        "tags": ["seaweed", "ulva", "sea lettuce", "toasted", "snacks", "foraging", "eat the weeds"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    # ===== SURINAM CHERRY RECIPE =====
    {
        "id": "surinam-cherry-chiffon-pie-etw",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Surinam Cherry Chiffon Pie",
        "category": "desserts",
        "attribution": "Eat the Weeds - Green Deane",
        "source_note": "Wild foraging recipe from eattheweeds.com",
        "description": "Light and airy chiffon pie with tropical Surinam cherries.",
        "servings_yield": "8-10 servings",
        "ingredients": [
            {"item": "9-10 inch pie crust", "quantity": "1", "unit": "", "prep_note": "baked and cooled"},
            {"item": "unflavored gelatin powder", "quantity": "1", "unit": "tbsp"},
            {"item": "cold water", "quantity": "1/4", "unit": "cup"},
            {"item": "large eggs", "quantity": "4", "unit": "", "prep_note": "separated"},
            {"item": "granulated sugar", "quantity": "1", "unit": "cup"},
            {"item": "Surinam cherry pulp", "quantity": "3/4", "unit": "cup", "prep_note": "about 1.5 cups fruit"},
            {"item": "whipping cream", "quantity": "1", "unit": "cup", "prep_note": "sweetened with powdered sugar"}
        ],
        "instructions": [
            {"step": 1, "text": "Soften gelatin in cold water."},
            {"step": 2, "text": "Beat egg yolks with half the sugar, add fruit pulp."},
            {"step": 3, "text": "Cook over medium heat until thick, stirring constantly."},
            {"step": 4, "text": "Add softened gelatin and stir until dissolved. Cool."},
            {"step": 5, "text": "Whip egg whites until frothy, gradually add remaining sugar, beating until peaks form."},
            {"step": 6, "text": "Fold whites into cherry mixture."},
            {"step": 7, "text": "Fill pie shell and chill until firm."},
            {"step": 8, "text": "Top with whipped cream before serving."}
        ],
        "notes": ["Only use ripe berries - one unripe berry can taint the rest", "Select deep blood-red fruits"],
        "tags": ["surinam cherry", "pitanga", "pie", "chiffon", "tropical", "foraging", "eat the weeds"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    # ===== IVY GOURD RECIPE =====
    {
        "id": "spiced-tindora-curry-etw",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Spiced Tindora Curry (Ivy Gourd)",
        "category": "sides",
        "attribution": "Eat the Weeds - Green Deane",
        "source_note": "Wild foraging recipe from eattheweeds.com",
        "description": "Indian-style spiced ivy gourd (tindora) curry.",
        "servings_yield": "4 servings",
        "prep_time": "15 minutes",
        "cook_time": "20-25 minutes",
        "ingredients": [
            {"item": "tindora (ivy gourd)", "quantity": "1.5", "unit": "lbs", "prep_note": "sliced"},
            {"item": "oil", "quantity": "1", "unit": "tbsp"},
            {"item": "mustard seeds", "quantity": "1/2", "unit": "tsp"},
            {"item": "cumin seeds", "quantity": "1/2", "unit": "tsp"},
            {"item": "asafoetida (hing)", "quantity": "", "unit": "pinch"},
            {"item": "turmeric powder", "quantity": "1/4", "unit": "tsp"},
            {"item": "green chilies", "quantity": "", "unit": "", "prep_note": "to taste, finely chopped"},
            {"item": "coriander powder", "quantity": "1", "unit": "tsp"},
            {"item": "cumin powder", "quantity": "1/2", "unit": "tsp"},
            {"item": "red chili powder", "quantity": "", "unit": "", "prep_note": "to taste"},
            {"item": "salt", "quantity": "", "unit": "", "prep_note": "to taste"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat oil in medium non-stick pan over medium heat."},
            {"step": 2, "text": "Add mustard seeds; allow to pop."},
            {"step": 3, "text": "Add cumin seeds; let sizzle."},
            {"step": 4, "text": "Add asafoetida, turmeric, green chilies, and tindora; mix well."},
            {"step": 5, "text": "Season with salt, red chili powder, coriander, and cumin powder."},
            {"step": 6, "text": "Cover and cook until tindora becomes tender, stirring every few minutes."},
            {"step": 7, "text": "Uncover and cook additional minutes to lightly brown."}
        ],
        "notes": ["Use the slicer blade of your food processor to quickly slice the tindora", "Cleaned, cut tindora freezes well"],
        "tags": ["ivy gourd", "tindora", "indian", "curry", "vegetable", "foraging", "eat the weeds"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    # ===== EEL RECIPES =====
    {
        "id": "eel-stifle-etw",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Eel Stifle",
        "category": "main-dishes",
        "attribution": "Eat the Weeds - Green Deane",
        "source_note": "Wild foraging recipe from eattheweeds.com",
        "description": "Traditional layered eel and potato casserole.",
        "servings_yield": "6 servings",
        "ingredients": [
            {"item": "peeled potatoes", "quantity": "2", "unit": "lbs", "prep_note": "sliced thin"},
            {"item": "onions", "quantity": "6", "unit": "", "prep_note": "sliced"},
            {"item": "eel", "quantity": "2", "unit": "lbs", "prep_note": "cut into 3-inch pieces"},
            {"item": "milk", "quantity": "2", "unit": "cups"},
            {"item": "salt pork", "quantity": "1/4", "unit": "lb", "prep_note": "diced"},
            {"item": "flour", "quantity": "", "unit": ""},
            {"item": "salt and pepper", "quantity": "", "unit": "", "prep_note": "to taste"}
        ],
        "instructions": [
            {"step": 1, "text": "Layer potatoes/onions, eel, and salt pork in buttered casserole."},
            {"step": 2, "text": "Top with remaining potatoes/onions and salt pork."},
            {"step": 3, "text": "Add milk."},
            {"step": 4, "text": "Bake at 350°F for one hour until tender."}
        ],
        "temperature": "350°F (175°C)",
        "notes": ["Eels must be thoroughly cleaned - remove all traces of slime"],
        "tags": ["eel", "casserole", "fish", "foraging", "eat the weeds"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "grilled-eel-etw",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Grilled Eel with Sage",
        "category": "main-dishes",
        "attribution": "Eat the Weeds - Green Deane",
        "source_note": "Wild foraging recipe from eattheweeds.com",
        "description": "Simple grilled eel with olive oil, paprika, and fresh sage.",
        "ingredients": [
            {"item": "eel", "quantity": "2", "unit": "lbs"},
            {"item": "olive oil", "quantity": "1/3", "unit": "cup"},
            {"item": "paprika", "quantity": "", "unit": "", "prep_note": "to taste"},
            {"item": "fresh sage leaves", "quantity": "10", "unit": "", "prep_note": "chopped"},
            {"item": "salt and pepper", "quantity": "", "unit": "", "prep_note": "to taste"}
        ],
        "instructions": [
            {"step": 1, "text": "Mix seasonings with oil; let sit 10 minutes."},
            {"step": 2, "text": "Cut eel into 3-inch pieces; wipe dry."},
            {"step": 3, "text": "Coat in oil mixture."},
            {"step": 4, "text": "Broil 4 inches from heat or grill 10 minutes per side, basting with oil mixture."},
            {"step": 5, "text": "Cook until light golden brown."}
        ],
        "tags": ["eel", "grilled", "fish", "foraging", "eat the weeds"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "jellied-eel-etw",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Jellied Eel",
        "category": "main-dishes",
        "attribution": "Eat the Weeds - Green Deane",
        "source_note": "Wild foraging recipe from eattheweeds.com",
        "description": "Traditional British jellied eel served cold.",
        "ingredients": [
            {"item": "cleaned eels", "quantity": "2", "unit": "", "prep_note": "gutted and skinned"},
            {"item": "water", "quantity": "3/4", "unit": "pint"},
            {"item": "white wine vinegar", "quantity": "5", "unit": "tbsp"},
            {"item": "black peppercorns", "quantity": "10", "unit": ""},
            {"item": "bay leaf", "quantity": "1", "unit": ""},
            {"item": "salt", "quantity": "", "unit": "", "prep_note": "to taste"},
            {"item": "butter", "quantity": "", "unit": "", "prep_note": "for greasing"}
        ],
        "instructions": [
            {"step": 1, "text": "Chop eels into 2-inch pieces."},
            {"step": 2, "text": "Grease casserole with butter."},
            {"step": 3, "text": "Combine all ingredients; season with salt."},
            {"step": 4, "text": "Cover and bake at 325°F for one hour."},
            {"step": 5, "text": "Cool, refrigerate overnight until liquid jellies."}
        ],
        "temperature": "325°F (165°C)",
        "tags": ["eel", "jellied", "british", "cold", "foraging", "eat the weeds"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "english-eel-pie-etw",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "English Eel Pie",
        "category": "main-dishes",
        "attribution": "Eat the Weeds - Green Deane",
        "source_note": "Wild foraging recipe from eattheweeds.com",
        "description": "Traditional English savory pie with eel, mushrooms, and sherry.",
        "ingredients": [
            {"item": "large eels", "quantity": "2", "unit": "", "prep_note": "skinned, cleaned, cut"},
            {"item": "butter", "quantity": "1", "unit": "tbsp"},
            {"item": "chopped mushrooms", "quantity": "1/2", "unit": "cup"},
            {"item": "chopped parsley", "quantity": "1", "unit": "tbsp"},
            {"item": "minced onion", "quantity": "1", "unit": ""},
            {"item": "bay leaf", "quantity": "1", "unit": ""},
            {"item": "salt and pepper", "quantity": "", "unit": "", "prep_note": "to taste"},
            {"item": "lemon rind", "quantity": "", "unit": ""},
            {"item": "Sherry", "quantity": "1", "unit": "wine glass"},
            {"item": "beef stock", "quantity": "1", "unit": "cup"},
            {"item": "pastry", "quantity": "", "unit": ""},
            {"item": "hard-boiled eggs", "quantity": "2", "unit": "", "prep_note": "sliced"},
            {"item": "egg yolk", "quantity": "1", "unit": "", "prep_note": "for glaze"}
        ],
        "instructions": [
            {"step": 1, "text": "Cook eels with butter, mushrooms, parsley, onion, bay leaf, seasonings, lemon rind, Sherry, and stock until tender."},
            {"step": 2, "text": "Strain sauce; thicken with butter and flour."},
            {"step": 3, "text": "Line baking dish with pastry."},
            {"step": 4, "text": "Add eels and sauce; top with egg slices."},
            {"step": 5, "text": "Cover with pastry; brush with egg yolk."},
            {"step": 6, "text": "Bake one hour at moderate temperature."},
            {"step": 7, "text": "Serve hot or cold."}
        ],
        "tags": ["eel", "pie", "english", "british", "foraging", "eat the weeds"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "achilles-eel-etw",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Achilles' Eel (Greek-Style)",
        "category": "main-dishes",
        "attribution": "Eat the Weeds - Green Deane",
        "source_note": "Wild foraging recipe from eattheweeds.com",
        "description": "Greek-style braised eel with tomatoes, feta, and herbs.",
        "ingredients": [
            {"item": "olive oil", "quantity": "2", "unit": "tbsp"},
            {"item": "eel", "quantity": "2", "unit": "lbs", "prep_note": "cut into 3-inch pieces"},
            {"item": "chopped onions", "quantity": "1/2", "unit": "lb"},
            {"item": "sun-dried tomatoes", "quantity": "3", "unit": "", "prep_note": "soaked in 2 tbsp boiling water, or 1 tbsp tomato paste"},
            {"item": "chopped tomatoes", "quantity": "3/4", "unit": "lb"},
            {"item": "honey", "quantity": "1/2", "unit": "tsp"},
            {"item": "fresh thyme", "quantity": "1", "unit": "tbsp"},
            {"item": "bay leaf", "quantity": "1", "unit": ""},
            {"item": "lemon zest", "quantity": "", "unit": ""},
            {"item": "lemon juice", "quantity": "1", "unit": "tbsp"},
            {"item": "minced garlic", "quantity": "2", "unit": "cloves"},
            {"item": "chopped flat-leaf parsley", "quantity": "1", "unit": "cup"},
            {"item": "chopped fresh mint", "quantity": "1", "unit": "tbsp"},
            {"item": "crumbled feta cheese", "quantity": "1/2", "unit": "lb"},
            {"item": "salt and pepper", "quantity": "", "unit": "", "prep_note": "to taste"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat oil in heavy skillet; brown eel pieces on all sides. Remove and set aside."},
            {"step": 2, "text": "Add onions; fry until translucent."},
            {"step": 3, "text": "Add sun-dried tomatoes (or paste), chopped tomatoes, honey, thyme, bay leaf, lemon zest, and garlic; simmer 10-12 minutes until sauce thickens."},
            {"step": 4, "text": "Return eel; stir in parsley, mint, salt, and pepper."},
            {"step": 5, "text": "Transfer to baking dish. Top with feta and sprinkle lemon juice."},
            {"step": 6, "text": "Bake at 350°F for 30 minutes."}
        ],
        "temperature": "350°F (175°C)",
        "tags": ["eel", "greek", "mediterranean", "feta", "foraging", "eat the weeds"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    # ===== GAR RECIPE =====
    {
        "id": "gar-lobster-etw",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Gar Lobster",
        "category": "main-dishes",
        "attribution": "Eat the Weeds - Green Deane",
        "source_note": "Wild foraging recipe from eattheweeds.com",
        "description": "Boiled gar fish that tastes remarkably like lobster.",
        "ingredients": [
            {"item": "gar fish", "quantity": "", "unit": "", "prep_note": "cut into chunks or nuggets"},
            {"item": "crab boil spices", "quantity": "", "unit": "", "prep_note": "prepared according to package"},
            {"item": "butter", "quantity": "", "unit": "", "prep_note": "melted, for dipping"},
            {"item": "mustard", "quantity": "", "unit": "", "prep_note": "optional, for frying"}
        ],
        "instructions": [
            {"step": 1, "text": "Prepare water with crab boil spices per package directions."},
            {"step": 2, "text": "Add gar chunks to water (can wrap in cheesecloth)."},
            {"step": 3, "text": "Boil for 5 minutes or longer depending on quantity."},
            {"step": 4, "text": "Turn off heat and let sit for same duration as boiling."},
            {"step": 5, "text": "Drain meat thoroughly."},
            {"step": 6, "text": "Dip each piece in melted butter and serve."}
        ],
        "notes": ["Alternative: Dip nuggets in mustard and fry until golden", "Never consume gar eggs or meat surrounding eggs"],
        "tags": ["gar", "fish", "seafood", "cajun", "foraging", "eat the weeds"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    # ===== GUINEA PIG (CUY) RECIPES =====
    {
        "id": "cuy-chactado-etw",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Cuy Chactado (Fried Guinea Pig)",
        "category": "main-dishes",
        "attribution": "Eat the Weeds - Green Deane",
        "source_note": "Traditional Peruvian recipe from eattheweeds.com",
        "description": "Traditional Ayacucho-style fried guinea pig.",
        "ingredients": [
            {"item": "guinea pig", "quantity": "1", "unit": "", "prep_note": "de-haired, gutted, and cleaned"},
            {"item": "flour", "quantity": "1/2", "unit": "cup"},
            {"item": "ground cumin", "quantity": "1/4-1/2", "unit": "tsp"},
            {"item": "salt and black pepper", "quantity": "", "unit": "", "prep_note": "to taste"},
            {"item": "oil", "quantity": "1/2", "unit": "cup"}
        ],
        "instructions": [
            {"step": 1, "text": "Pat the skin dry and rub with cumin, salt, and pepper."},
            {"step": 2, "text": "Heat oil."},
            {"step": 3, "text": "Dust the carcass with flour and place on its back in hot oil."},
            {"step": 4, "text": "Turn to cook both sides until golden. Alternatively, cut into quarters before frying."},
            {"step": 5, "text": "Serve with boiled potatoes or manioc root, plus a salad of tomatoes and slivered onions in lime juice and salt."}
        ],
        "notes": ["Guinea pig has 21% protein and 8% fat - more protein and less cholesterol than beef, pork, or chicken"],
        "tags": ["guinea pig", "cuy", "peruvian", "fried", "foraging", "eat the weeds"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "cuy-picante-huanuqueno-etw",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Cuy Picante Huanuqueño Style",
        "category": "main-dishes",
        "attribution": "Eat the Weeds - Green Deane",
        "source_note": "Traditional Peruvian recipe from eattheweeds.com",
        "description": "Spicy Peruvian guinea pig with aji peppers and peanuts.",
        "servings_yield": "4 servings",
        "ingredients": [
            {"item": "large guinea pigs", "quantity": "2", "unit": ""},
            {"item": "crushed garlic", "quantity": "1", "unit": "tbsp"},
            {"item": "salt", "quantity": "1.5", "unit": "tsp"},
            {"item": "pepper", "quantity": "1.5", "unit": "tsp"},
            {"item": "cumin powder", "quantity": "1.5", "unit": "tsp"},
            {"item": "aji panca", "quantity": "2", "unit": "tbsp", "prep_note": "liquefied"},
            {"item": "aji mirasol", "quantity": "2", "unit": "tbsp", "prep_note": "liquefied"},
            {"item": "cooking oil or margarine", "quantity": "1", "unit": "cup"},
            {"item": "scallions", "quantity": "10", "unit": ""},
            {"item": "guinea pig hearts and livers", "quantity": "", "unit": ""},
            {"item": "crushed peanuts", "quantity": "1", "unit": "tbsp"},
            {"item": "yellow potatoes", "quantity": "8", "unit": "", "prep_note": "boiled and skinned"}
        ],
        "instructions": [
            {"step": 1, "text": "Quarter the guinea pigs and fry until golden brown."},
            {"step": 2, "text": "In a heavy skillet, combine garlic, aji panca, and aji mirasol over high heat, stirring constantly."},
            {"step": 3, "text": "Chop scallion bulbs and add with cumin."},
            {"step": 4, "text": "Blend hearts, livers, and peanuts separately, then add to the pan."},
            {"step": 5, "text": "Include guinea pig pieces and cook 10-15 minutes."},
            {"step": 6, "text": "Let stand 15 minutes before serving over sliced potatoes."}
        ],
        "tags": ["guinea pig", "cuy", "peruvian", "spicy", "foraging", "eat the weeds"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "cuyes-en-salsa-de-mani-etw",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Cuyes en Salsa de Maní (Guinea Pig with Peanut Sauce)",
        "category": "main-dishes",
        "attribution": "Eat the Weeds - Green Deane",
        "source_note": "Traditional Peruvian recipe from eattheweeds.com",
        "description": "Deep-fried guinea pig served with creamy peanut sauce.",
        "ingredients": [
            {"item": "whole guinea pig", "quantity": "1", "unit": ""},
            {"item": "salt and pepper", "quantity": "", "unit": "", "prep_note": "to taste"},
            {"item": "vegetable oil", "quantity": "", "unit": "", "prep_note": "for deep frying"},
            {"item": "creamy peanut sauce", "quantity": "", "unit": ""},
            {"item": "white rice", "quantity": "", "unit": "", "prep_note": "for serving"},
            {"item": "fried yuccas", "quantity": "", "unit": "", "prep_note": "for serving"},
            {"item": "boiled sweet potatoes", "quantity": "", "unit": "", "prep_note": "for serving"}
        ],
        "instructions": [
            {"step": 1, "text": "Season whole guinea pig with salt and pepper."},
            {"step": 2, "text": "Deep fry in vegetable oil until golden and cooked through."},
            {"step": 3, "text": "Serve with creamy peanut sauce, white rice, fried yuccas, and boiled sweet potatoes."}
        ],
        "tags": ["guinea pig", "cuy", "peruvian", "peanut sauce", "foraging", "eat the weeds"],
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

    for recipe in ETW_BATCH5_RECIPES:
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
    print(f"  Added: {added} new Eat the Weeds recipes (batch 5)")
    print(f"  Skipped: {skipped} duplicates")
    print(f"  Total recipes now: {len(recipes)}")


if __name__ == "__main__":
    main()
