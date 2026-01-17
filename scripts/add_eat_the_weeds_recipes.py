#!/usr/bin/env python3
"""
Add Eat the Weeds recipes to recipes.json.

These are wild foraging recipes from Green Deane's website eattheweeds.com.
This is a first batch - the site has 300+ plant pages with potentially
hundreds more recipes.
"""

import json
from pathlib import Path

RECIPES_FILE = Path(__file__).parent.parent / "data" / "recipes.json"

ETW_RECIPES = [
    # ===== DANDELION RECIPES =====
    {
        "id": "dandelion-wine-etw",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Dandelion Wine",
        "category": "beverages",
        "attribution": "Eat the Weeds - Green Deane",
        "source_note": "Wild foraging recipe from eattheweeds.com",
        "description": "Traditional homemade wine from dandelion flowers.",
        "servings_yield": "1 gallon",
        "ingredients": [
            {"item": "dandelion flowers", "quantity": "3", "unit": "quarts"},
            {"item": "golden raisins", "quantity": "1", "unit": "lb"},
            {"item": "water", "quantity": "1", "unit": "gallon"},
            {"item": "granulated sugar", "quantity": "3", "unit": "lbs"},
            {"item": "lemons", "quantity": "2", "unit": ""},
            {"item": "orange", "quantity": "1", "unit": ""},
            {"item": "yeast and nutrient", "quantity": "", "unit": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Pick fresh flowers and trim stalks, removing all green parts."},
            {"step": 2, "text": "Place flowers in large bowl. Set aside one pint of water."},
            {"step": 3, "text": "Boil remaining gallon and pour over flowers. Cover tightly with plastic wrap for two days, stirring twice daily."},
            {"step": 4, "text": "Transfer to large pot and bring to low boil."},
            {"step": 5, "text": "Add sugar and citrus peelings (thinly sliced, avoiding white pith). Boil for one hour."},
            {"step": 6, "text": "Pour into fermenter and cool. Add yeast, nutrient, cover, and place in warm location for three days."},
            {"step": 7, "text": "Strain into secondary fermenter with raisins and fit fermentation lock."},
            {"step": 8, "text": "Rack after wine clears. After two months, rack and bottle."},
            {"step": 9, "text": "Age six months to one year."}
        ],
        "tags": ["wine", "dandelion", "fermented", "foraging", "eat the weeds"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "dandelion-burgers-etw",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Dandelion Burgers",
        "category": "main-dishes",
        "attribution": "Eat the Weeds - Green Deane",
        "source_note": "Wild foraging recipe from eattheweeds.com",
        "description": "Vegetarian burgers made with dandelion petals.",
        "servings_yield": "4-5 burgers",
        "ingredients": [
            {"item": "dandelion petals", "quantity": "1", "unit": "cup", "prep_note": "packed, no greens"},
            {"item": "flour", "quantity": "1", "unit": "cup"},
            {"item": "egg", "quantity": "1", "unit": ""},
            {"item": "milk", "quantity": "1/4", "unit": "cup"},
            {"item": "chopped onions", "quantity": "1/2", "unit": "cup"},
            {"item": "salt", "quantity": "1/4", "unit": "tsp"},
            {"item": "garlic powder", "quantity": "1/2", "unit": "tsp"},
            {"item": "basil", "quantity": "1/4", "unit": "tsp"},
            {"item": "oregano", "quantity": "1/4", "unit": "tsp"},
            {"item": "pepper", "quantity": "1/8", "unit": "tsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Mix all ingredients until combined into goopy batter."},
            {"step": 2, "text": "Form into patties."},
            {"step": 3, "text": "Pan-fry in oil or butter, turning until both sides are crisp."}
        ],
        "tags": ["vegetarian", "burgers", "dandelion", "foraging", "eat the weeds"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "dandelion-blossom-bread-etw",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Dandelion Blossom Bread",
        "category": "breads",
        "attribution": "Eat the Weeds - Green Deane",
        "source_note": "Wild foraging recipe from eattheweeds.com",
        "description": "Quick bread made with dandelion blossoms.",
        "servings_yield": "1 loaf or 12 muffins",
        "ingredients": [
            {"item": "flour", "quantity": "2", "unit": "cups"},
            {"item": "baking powder", "quantity": "2", "unit": "tsp"},
            {"item": "salt", "quantity": "1/2", "unit": "tsp"},
            {"item": "dandelion blossoms", "quantity": "1", "unit": "cup", "prep_note": "all green removed"},
            {"item": "oil", "quantity": "1/4", "unit": "cup"},
            {"item": "honey", "quantity": "4", "unit": "tbsp"},
            {"item": "egg", "quantity": "1", "unit": ""},
            {"item": "milk", "quantity": "1 1/2", "unit": "cups"}
        ],
        "instructions": [
            {"step": 1, "text": "Combine dry ingredients including separated dandelion petals."},
            {"step": 2, "text": "In separate bowl, mix milk, honey, oil, and beaten egg."},
            {"step": 3, "text": "Add liquid to dry ingredients."},
            {"step": 4, "text": "Pour into buttered bread or muffin tin."},
            {"step": 5, "text": "Bake at 400°F for 20-25 minutes for muffins or longer for bread loaf."}
        ],
        "temperature": "400°F (205°C)",
        "cook_time": "20-25 minutes",
        "tags": ["bread", "muffins", "dandelion", "foraging", "eat the weeds"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "cream-of-dandelion-soup-etw",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Cream of Dandelion Soup",
        "category": "soups",
        "attribution": "Eat the Weeds - Green Deane",
        "source_note": "Wild foraging recipe from eattheweeds.com",
        "description": "Creamy soup made with dandelion leaves, petals, and buds.",
        "servings_yield": "6 servings",
        "ingredients": [
            {"item": "dandelion leaves", "quantity": "4", "unit": "cups", "prep_note": "chopped"},
            {"item": "dandelion flower petals", "quantity": "2", "unit": "cups"},
            {"item": "dandelion buds", "quantity": "2", "unit": "cups"},
            {"item": "butter or olive oil", "quantity": "1", "unit": "tbsp"},
            {"item": "wild leeks or onions", "quantity": "1", "unit": "cup", "prep_note": "chopped"},
            {"item": "garlic", "quantity": "6", "unit": "cloves", "prep_note": "minced"},
            {"item": "water", "quantity": "4", "unit": "cups"},
            {"item": "half-and-half or heavy cream", "quantity": "2", "unit": "cups"},
            {"item": "salt", "quantity": "2", "unit": "tsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Gently boil dandelion leaves in 6 cups water. Pour off bitter water."},
            {"step": 2, "text": "Boil gently a second time and drain."},
            {"step": 3, "text": "In heavy-bottom soup pot, sauté leeks and garlic in butter until tender."},
            {"step": 4, "text": "Add 4 cups water, dandelion leaves, flower petals, buds, and salt."},
            {"step": 5, "text": "Simmer 45 minutes."},
            {"step": 6, "text": "Add cream and simmer several minutes more. Garnish with flower petals."}
        ],
        "tags": ["soup", "cream", "dandelion", "foraging", "eat the weeds"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "dandelion-blossom-syrup-etw",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Dandelion Blossom Syrup",
        "category": "preserves",
        "attribution": "Eat the Weeds - Green Deane",
        "source_note": "Wild foraging recipe from eattheweeds.com",
        "description": "Honey-like syrup made from dandelion blossoms.",
        "servings_yield": "2-3 pints",
        "ingredients": [
            {"item": "dandelion flowers", "quantity": "1", "unit": "quart"},
            {"item": "water", "quantity": "4", "unit": "cups"},
            {"item": "sugar", "quantity": "4", "unit": "cups"},
            {"item": "lemon or orange", "quantity": "1/2", "unit": "", "prep_note": "chopped with peel, optional"}
        ],
        "instructions": [
            {"step": 1, "text": "Place blossoms and water in pot."},
            {"step": 2, "text": "Bring just to boil, turn off heat, cover, and let sit overnight."},
            {"step": 3, "text": "The next day, strain and press liquid from spent flowers."},
            {"step": 4, "text": "Add sugar and citrus, then heat slowly, stirring occasionally."},
            {"step": 5, "text": "Continue for several hours until reduced to thick, honey-like consistency."},
            {"step": 6, "text": "Can in half-pint or pint jars."}
        ],
        "tags": ["syrup", "preserves", "dandelion", "foraging", "eat the weeds"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "dandelion-baklava-etw",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Dandelion Baklava",
        "category": "desserts",
        "attribution": "Eat the Weeds - Green Deane",
        "source_note": "Wild foraging recipe from eattheweeds.com",
        "description": "Traditional baklava made with dandelion blossom syrup.",
        "servings_yield": "30 pieces",
        "ingredients": [
            {"item": "fillo leaves", "quantity": "1/2", "unit": "box"},
            {"item": "butter", "quantity": "1", "unit": "stick"},
            {"item": "hickory nuts, walnuts, or pecans", "quantity": "2", "unit": "cups", "prep_note": "finely chopped"},
            {"item": "sugar", "quantity": "1", "unit": "tsp"},
            {"item": "cinnamon", "quantity": "1/2", "unit": "tsp"},
            {"item": "nutmeg", "quantity": "1/2", "unit": "tsp"},
            {"item": "dandelion blossom syrup", "quantity": "3/4", "unit": "cup"}
        ],
        "instructions": [
            {"step": 1, "text": "Combine nuts with sugar and spices."},
            {"step": 2, "text": "Melt butter."},
            {"step": 3, "text": "Layer 8 fillo sheets in buttered 9x13 pan, brushing every other sheet with butter."},
            {"step": 4, "text": "Sprinkle half the nut mixture."},
            {"step": 5, "text": "Layer 8 more sheets and remaining nut mixture."},
            {"step": 6, "text": "Top with remaining fillo sheets, brushing top generously with butter."},
            {"step": 7, "text": "Cut into 30 squares before baking."},
            {"step": 8, "text": "Bake at 375°F for 30 minutes until lightly browned."},
            {"step": 9, "text": "Pour room temperature syrup over hot baklava."}
        ],
        "temperature": "375°F (190°C)",
        "cook_time": "30 minutes",
        "tags": ["dessert", "baklava", "dandelion", "foraging", "eat the weeds"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "dandelion-burdock-beer-etw",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Dandelion and Burdock Beer",
        "category": "beverages",
        "attribution": "Eat the Weeds - Green Deane",
        "source_note": "Wild foraging recipe from eattheweeds.com",
        "description": "Traditional British herbal beer made with dandelion and burdock.",
        "servings_yield": "1 gallon",
        "ingredients": [
            {"item": "young nettles", "quantity": "1", "unit": "lb"},
            {"item": "dandelion leaves", "quantity": "4", "unit": "oz"},
            {"item": "fresh burdock root", "quantity": "4", "unit": "oz", "prep_note": "sliced, or 2 oz dried"},
            {"item": "ginger root", "quantity": "1/2", "unit": "oz", "prep_note": "bruised"},
            {"item": "lemons", "quantity": "2", "unit": ""},
            {"item": "water", "quantity": "1", "unit": "gallon"},
            {"item": "soft brown sugar", "quantity": "1 lb + 4", "unit": "tsp"},
            {"item": "cream of tartar", "quantity": "1", "unit": "oz"},
            {"item": "brewing yeast", "quantity": "", "unit": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Put nettles, dandelion leaves, burdock, ginger, and thinly pared lemon rinds in large pan with water."},
            {"step": 2, "text": "Bring to boil and simmer 30 minutes."},
            {"step": 3, "text": "Pour lemon juice, sugar, and cream of tartar into large container and strain liquid through, pressing down on solids."},
            {"step": 4, "text": "Stir to dissolve sugar. Cool to room temperature."},
            {"step": 5, "text": "Sprinkle in yeast. Cover and leave to ferment in warm place for 3 days."},
            {"step": 6, "text": "Pour off beer and bottle, adding 1 tsp sugar per pint."},
            {"step": 7, "text": "Leave undisturbed about 1 week until clear."}
        ],
        "tags": ["beer", "fermented", "dandelion", "burdock", "foraging", "eat the weeds"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    # ===== CATTAIL RECIPES =====
    {
        "id": "scalloped-cattails-etw",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Scalloped Cattails",
        "category": "vegetables",
        "attribution": "Eat the Weeds - Green Deane",
        "source_note": "Wild foraging recipe from eattheweeds.com",
        "description": "Baked cattail tops in a creamy casserole.",
        "servings_yield": "4 servings",
        "ingredients": [
            {"item": "cattail tops", "quantity": "2", "unit": "cups", "prep_note": "chopped"},
            {"item": "eggs", "quantity": "2", "unit": "", "prep_note": "beaten"},
            {"item": "butter", "quantity": "1/2", "unit": "cup", "prep_note": "melted"},
            {"item": "sugar", "quantity": "1/2", "unit": "tsp"},
            {"item": "nutmeg", "quantity": "1/2", "unit": "tsp"},
            {"item": "black pepper", "quantity": "", "unit": "", "prep_note": "to taste"},
            {"item": "milk", "quantity": "1", "unit": "cup", "prep_note": "scalded"},
            {"item": "Swiss cheese", "quantity": "", "unit": "", "prep_note": "grated, optional"}
        ],
        "instructions": [
            {"step": 1, "text": "Combine cattail tops with eggs, butter, sugar, nutmeg, and pepper in a bowl."},
            {"step": 2, "text": "Gradually blend in the scalded milk."},
            {"step": 3, "text": "Pour mixture into a greased casserole dish."},
            {"step": 4, "text": "Top with cheese and butter."},
            {"step": 5, "text": "Bake at 275°F for 30 minutes."}
        ],
        "temperature": "275°F (135°C)",
        "cook_time": "30 minutes",
        "tags": ["casserole", "cattails", "vegetables", "foraging", "eat the weeds"],
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
        "description": "Biscuits made with cattail pollen flour.",
        "servings_yield": "12 biscuits",
        "ingredients": [
            {"item": "cattail pollen", "quantity": "1/4", "unit": "cup"},
            {"item": "flour", "quantity": "1 3/4", "unit": "cups"},
            {"item": "baking powder", "quantity": "3", "unit": "tsp"},
            {"item": "salt", "quantity": "1", "unit": "tsp"},
            {"item": "shortening", "quantity": "4", "unit": "tbsp"},
            {"item": "milk", "quantity": "3/4", "unit": "cup"}
        ],
        "instructions": [
            {"step": 1, "text": "Mix pollen, flour, baking powder, and salt."},
            {"step": 2, "text": "Cut in shortening."},
            {"step": 3, "text": "Add milk and mix."},
            {"step": 4, "text": "Form biscuits."},
            {"step": 5, "text": "Bake at 425°F for 20 minutes."}
        ],
        "temperature": "425°F (220°C)",
        "cook_time": "20 minutes",
        "tags": ["biscuits", "bread", "cattails", "pollen", "foraging", "eat the weeds"],
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
        "description": "Pancakes made with cattail pollen for a golden color.",
        "servings_yield": "12-15 small pancakes",
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
            {"step": 1, "text": "Combine dry ingredients."},
            {"step": 2, "text": "Mix with egg, milk, and bacon drippings."},
            {"step": 3, "text": "Pour dollar-sized amounts onto a hot griddle."},
            {"step": 4, "text": "Cook until bubbles form, then flip."}
        ],
        "tags": ["pancakes", "breakfast", "cattails", "pollen", "foraging", "eat the weeds"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    # ===== KUDZU RECIPES =====
    {
        "id": "kudzu-blossom-jelly-etw",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Kudzu Blossom Jelly",
        "category": "preserves",
        "attribution": "Eat the Weeds - Green Deane",
        "source_note": "Wild foraging recipe from eattheweeds.com",
        "description": "Purple jelly made from kudzu blossoms.",
        "servings_yield": "6 half pints",
        "ingredients": [
            {"item": "kudzu blossoms", "quantity": "4", "unit": "cups"},
            {"item": "boiling water", "quantity": "4", "unit": "cups"},
            {"item": "lemon juice", "quantity": "1", "unit": "tbsp"},
            {"item": "powdered pectin", "quantity": "1 3/4", "unit": "oz"},
            {"item": "sugar", "quantity": "5", "unit": "cups"}
        ],
        "instructions": [
            {"step": 1, "text": "Wash blossoms and place in a large bowl."},
            {"step": 2, "text": "Pour boiling water over blossoms; refrigerate 8 hours or overnight."},
            {"step": 3, "text": "Strain blossoms and liquid through colander into Dutch oven."},
            {"step": 4, "text": "Add lemon juice and pectin; bring to rolling boil over high heat, stirring constantly."},
            {"step": 5, "text": "Stir in sugar; return to rolling boil and boil 1 minute while stirring."},
            {"step": 6, "text": "Remove from heat; skim foam with spoon."},
            {"step": 7, "text": "Pour into sterilized jars, filling to 1/4 inch from top."},
            {"step": 8, "text": "Process in boiling water bath for 5 minutes."}
        ],
        "tags": ["jelly", "preserves", "kudzu", "foraging", "eat the weeds"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "rolled-kudzu-leaves-etw",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Rolled Kudzu Leaves",
        "category": "main-dishes",
        "attribution": "Eat the Weeds - Green Deane",
        "source_note": "Wild foraging recipe from eattheweeds.com",
        "description": "Stuffed kudzu leaves similar to dolmas.",
        "servings_yield": "30 rolls",
        "ingredients": [
            {"item": "young kudzu leaves", "quantity": "30", "unit": "medium"},
            {"item": "diced tomatoes", "quantity": "14", "unit": "oz", "prep_note": "canned"},
            {"item": "salt", "quantity": "2", "unit": "tsp"},
            {"item": "garlic", "quantity": "3", "unit": "cloves", "prep_note": "halved"},
            {"item": "lemon juice", "quantity": "3", "unit": "lemons"},
            {"item": "rice", "quantity": "1", "unit": "cup", "prep_note": "rinsed"},
            {"item": "ground lamb or beef", "quantity": "1", "unit": "lb"},
            {"item": "allspice", "quantity": "1/2", "unit": "tsp"},
            {"item": "salt and pepper", "quantity": "", "unit": "", "prep_note": "to taste"}
        ],
        "instructions": [
            {"step": 1, "text": "Gather leaves from unsprayed areas and wash them."},
            {"step": 2, "text": "Boil leaves in salted water for 2-3 minutes, separating as needed."},
            {"step": 3, "text": "Remove to plate to cool. Remove heavy center stems."},
            {"step": 4, "text": "Combine rice, meat, 1 cup diced tomatoes, allspice, salt and pepper for stuffing."},
            {"step": 5, "text": "Fill each leaf with 1 teaspoon stuffing and roll cigar-shaped."},
            {"step": 6, "text": "Arrange rolls alternately in opposite directions in large pan."},
            {"step": 7, "text": "Pour in remaining diced tomatoes, salt, and garlic."},
            {"step": 8, "text": "Press down with inverted dish; add water to reach dish."},
            {"step": 9, "text": "Cover and cook on medium for 30 minutes."},
            {"step": 10, "text": "Add lemon juice and cook 10 minutes more."}
        ],
        "cook_time": "40 minutes",
        "tags": ["stuffed", "kudzu", "dolmas", "foraging", "eat the weeds"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "kudzu-quiche-etw",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Kudzu Quiche",
        "category": "main-dishes",
        "attribution": "Eat the Weeds - Green Deane",
        "source_note": "Wild foraging recipe from eattheweeds.com",
        "description": "Savory quiche made with young kudzu leaves.",
        "servings_yield": "6 servings",
        "ingredients": [
            {"item": "heavy cream", "quantity": "1", "unit": "cup"},
            {"item": "eggs", "quantity": "3", "unit": "", "prep_note": "beaten"},
            {"item": "young kudzu leaves and stems", "quantity": "1", "unit": "cup", "prep_note": "chopped"},
            {"item": "salt", "quantity": "1/2", "unit": "tsp"},
            {"item": "ground pepper", "quantity": "", "unit": "", "prep_note": "to taste"},
            {"item": "mozzarella cheese", "quantity": "1", "unit": "cup", "prep_note": "grated"},
            {"item": "unbaked pie shell", "quantity": "1", "unit": "9-inch"}
        ],
        "instructions": [
            {"step": 1, "text": "Preheat oven to 350°F."},
            {"step": 2, "text": "Mix cream, eggs, kudzu, salt, pepper, and cheese."},
            {"step": 3, "text": "Place mixture in pie shell."},
            {"step": 4, "text": "Bake 35 to 45 minutes until center is set."}
        ],
        "temperature": "350°F (175°C)",
        "cook_time": "35-45 minutes",
        "tags": ["quiche", "kudzu", "foraging", "eat the weeds"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    # ===== BEAUTYBERRY RECIPES =====
    {
        "id": "beautyberry-jelly-etw",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Beautyberry Jelly",
        "category": "preserves",
        "attribution": "Eat the Weeds - Green Deane",
        "source_note": "Wild foraging recipe from eattheweeds.com",
        "description": "Purple jelly made from American beautyberries.",
        "servings_yield": "4-5 half pints",
        "ingredients": [
            {"item": "ripe beautyberries", "quantity": "1 1/2", "unit": "quarts", "prep_note": "washed and cleaned"},
            {"item": "water", "quantity": "2", "unit": "quarts"},
            {"item": "beautyberry infusion", "quantity": "3", "unit": "cups"},
            {"item": "Sure-Jell pectin", "quantity": "1", "unit": "envelope"},
            {"item": "sugar", "quantity": "4 1/2", "unit": "cups"}
        ],
        "instructions": [
            {"step": 1, "text": "Wash and clean beautyberries, removing all green stems and leaves."},
            {"step": 2, "text": "Cover berries with 2 quarts water."},
            {"step": 3, "text": "Boil for 20 minutes."},
            {"step": 4, "text": "Strain to create infusion."},
            {"step": 5, "text": "Use 3 cups of the infusion and bring to boil."},
            {"step": 6, "text": "Add Sure-Jell and sugar."},
            {"step": 7, "text": "Return to second boil and boil for 2 minutes."},
            {"step": 8, "text": "Remove from heat and let stand until foam forms."},
            {"step": 9, "text": "Skim off foam."},
            {"step": 10, "text": "Pour into sterilized jars and cap."}
        ],
        "tags": ["jelly", "preserves", "beautyberry", "foraging", "eat the weeds"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    # ===== LOQUAT RECIPES =====
    {
        "id": "loquat-grappa-etw",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Loquat Grappa",
        "category": "beverages",
        "attribution": "Eat the Weeds - Green Deane",
        "source_note": "Wild foraging recipe from eattheweeds.com",
        "description": "Italian-style liqueur made from loquat seeds.",
        "servings_yield": "2 bottles",
        "ingredients": [
            {"item": "loquat seeds", "quantity": "1-2", "unit": "quarts", "prep_note": "clean, whole"},
            {"item": "vodka", "quantity": "1", "unit": "quart"},
            {"item": "sugar", "quantity": "", "unit": "", "prep_note": "equal parts with water"},
            {"item": "water", "quantity": "", "unit": "", "prep_note": "equal parts with sugar"}
        ],
        "instructions": [
            {"step": 1, "text": "Soak seeds in vodka for 1-6 months in a sealed jar."},
            {"step": 2, "text": "Drain flavored vodka and divide between two bottles."},
            {"step": 3, "text": "Heat equal parts sugar and water until dissolved."},
            {"step": 4, "text": "Top off each bottle with sugar syrup."},
            {"step": 5, "text": "Adjust sweetness as desired."}
        ],
        "notes": ["Seeds contain cyanogenetic glycosides; consume sparingly, no more than 4 ounces at a time."],
        "tags": ["liqueur", "grappa", "loquat", "foraging", "eat the weeds"],
        "confidence": {"overall": "high", "flags": ["Contains warning about cyanogenic compounds"]},
        "image_refs": []
    },
    {
        "id": "loquat-wine-etw",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Loquat Wine",
        "category": "beverages",
        "attribution": "Eat the Weeds - Green Deane",
        "source_note": "Wild foraging recipe from eattheweeds.com",
        "description": "Fruit wine made from fresh loquats.",
        "servings_yield": "1 gallon",
        "ingredients": [
            {"item": "fresh loquats", "quantity": "4", "unit": "lbs", "prep_note": "seeds removed"},
            {"item": "granulated sugar", "quantity": "2", "unit": "lbs"},
            {"item": "acid blend", "quantity": "1", "unit": "tsp"},
            {"item": "water", "quantity": "1", "unit": "gallon"},
            {"item": "Campden tablet", "quantity": "1", "unit": "", "prep_note": "crushed"},
            {"item": "pectic enzyme", "quantity": "1/2", "unit": "tsp"},
            {"item": "grape tannin", "quantity": "1/2", "unit": "tsp"},
            {"item": "wine yeast and nutrient", "quantity": "", "unit": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Chop fruit finely, pour over half sugar, Campden tablet, tannin, and water."},
            {"step": 2, "text": "After 12 hours, add pectic enzyme."},
            {"step": 3, "text": "After another 12 hours, add yeast."},
            {"step": 4, "text": "Stir daily, adding remaining sugar after 3 days."},
            {"step": 5, "text": "Ferment on pulp 4 more days."},
            {"step": 6, "text": "Strain through jelly bag, pour into secondary with airlock."},
            {"step": 7, "text": "Rack every 30 days until clear (3-4 additional rackings)."},
            {"step": 8, "text": "Bottle and age."}
        ],
        "tags": ["wine", "fermented", "loquat", "foraging", "eat the weeds"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "loquat-jelly-etw",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Loquat Jelly",
        "category": "preserves",
        "attribution": "Eat the Weeds - Green Deane",
        "source_note": "Wild foraging recipe from eattheweeds.com",
        "description": "Clear jelly made from loquat fruit.",
        "servings_yield": "5-6 half pints",
        "ingredients": [
            {"item": "ripe loquats", "quantity": "5", "unit": "lbs"},
            {"item": "water", "quantity": "1", "unit": "cup"},
            {"item": "lemon juice", "quantity": "1/2", "unit": "cup"},
            {"item": "pectin", "quantity": "1", "unit": "package"},
            {"item": "sugar", "quantity": "5 1/2", "unit": "cups"}
        ],
        "instructions": [
            {"step": 1, "text": "Wash loquats, remove seeds and blossom ends."},
            {"step": 2, "text": "Barely cover with cold water. Simmer covered 15 minutes until soft."},
            {"step": 3, "text": "Strain through jelly bag."},
            {"step": 4, "text": "Measure 3 1/2 cups juice and lemon juice."},
            {"step": 5, "text": "Add pectin, stir well. Bring to boil, stirring constantly."},
            {"step": 6, "text": "Add sugar, return to rolling boil for exactly 2 minutes."},
            {"step": 7, "text": "Remove from heat, skim."},
            {"step": 8, "text": "Pour into sterilized glasses, seal with paraffin."}
        ],
        "tags": ["jelly", "preserves", "loquat", "foraging", "eat the weeds"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "loquat-pie-etw",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Loquat Pie",
        "category": "desserts",
        "attribution": "Eat the Weeds - Green Deane",
        "source_note": "Wild foraging recipe from eattheweeds.com",
        "description": "Traditional fruit pie made with loquats.",
        "servings_yield": "8 servings",
        "ingredients": [
            {"item": "loquats", "quantity": "8", "unit": "cups"},
            {"item": "water", "quantity": "1/2", "unit": "cup"},
            {"item": "sugar", "quantity": "1", "unit": "cup"},
            {"item": "flour", "quantity": "3", "unit": "tbsp"},
            {"item": "salt", "quantity": "1/4", "unit": "tsp"},
            {"item": "ginger", "quantity": "1/8", "unit": "tsp"},
            {"item": "allspice", "quantity": "1/8", "unit": "tsp"},
            {"item": "pastry for double crust pie", "quantity": "", "unit": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Stem, wash, and cut loquats, leaving a few seeds for flavor."},
            {"step": 2, "text": "Cook in water covered 10 minutes until nearly tender."},
            {"step": 3, "text": "Combine sugar, flour, salt, ginger, and allspice."},
            {"step": 4, "text": "Stir into loquats. Cook stirring until thickened, cool."},
            {"step": 5, "text": "Pour into bottom crust, cover with top crust, prick or slash."},
            {"step": 6, "text": "Bake at 450°F for 10 minutes, reduce to 350°F for 45 minutes."},
            {"step": 7, "text": "Serve with vanilla ice cream and rum sauce."}
        ],
        "temperature": "450°F then 350°F",
        "cook_time": "55 minutes",
        "tags": ["pie", "dessert", "loquat", "foraging", "eat the weeds"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "spiced-loquats-etw",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Spiced Loquats",
        "category": "preserves",
        "attribution": "Eat the Weeds - Green Deane",
        "source_note": "Wild foraging recipe from eattheweeds.com",
        "description": "Pickled loquats with warm spices.",
        "servings_yield": "3-4 pints",
        "ingredients": [
            {"item": "firm loquats", "quantity": "3", "unit": "lbs"},
            {"item": "sugar", "quantity": "3", "unit": "cups"},
            {"item": "water", "quantity": "1 1/2", "unit": "cups"},
            {"item": "cider vinegar", "quantity": "1 1/2", "unit": "cups"},
            {"item": "whole cloves", "quantity": "1", "unit": "tbsp"},
            {"item": "whole allspice", "quantity": "1", "unit": "tbsp"},
            {"item": "cinnamon stick", "quantity": "2", "unit": "inches"}
        ],
        "instructions": [
            {"step": 1, "text": "Wash loquats, remove stem and blossom ends."},
            {"step": 2, "text": "Combine sugar, water, and vinegar."},
            {"step": 3, "text": "Tie spices in cheesecloth, add to mixture. Boil 10 minutes."},
            {"step": 4, "text": "Add fruit, cook gently until tender."},
            {"step": 5, "text": "Remove fruit, pour syrup into sterilized jars, fill with hot syrup."},
            {"step": 6, "text": "Seal immediately."}
        ],
        "tags": ["pickled", "preserves", "loquat", "spiced", "foraging", "eat the weeds"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    # ===== MULBERRY RECIPES =====
    {
        "id": "mulberry-pie-etw",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Mulberry Pie",
        "category": "desserts",
        "attribution": "Eat the Weeds - Green Deane",
        "source_note": "Wild foraging recipe from eattheweeds.com",
        "description": "Fruit pie made with fresh mulberries.",
        "servings_yield": "8 servings",
        "ingredients": [
            {"item": "baked 9-inch pie crust", "quantity": "1", "unit": ""},
            {"item": "stemmed mulberries", "quantity": "4", "unit": "cups"},
            {"item": "cornstarch", "quantity": "1/4", "unit": "cup"},
            {"item": "sugar", "quantity": "3/4", "unit": "cup"},
            {"item": "water", "quantity": "1/2", "unit": "cup"},
            {"item": "lemon or lime juice", "quantity": "2", "unit": "tbsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Combine sugar with mulberries in a saucepan."},
            {"step": 2, "text": "Mix cornstarch with water separately."},
            {"step": 3, "text": "Add cornstarch mixture and juice to berries."},
            {"step": 4, "text": "Cook over medium heat until mixture thickens and juice becomes clear."},
            {"step": 5, "text": "Pour into baked pie shell."},
            {"step": 6, "text": "Cool and serve."}
        ],
        "tags": ["pie", "dessert", "mulberry", "foraging", "eat the weeds"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "mulberry-vinegar-etw",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Mulberry Vinegar",
        "category": "preserves",
        "attribution": "Eat the Weeds - Green Deane",
        "source_note": "Wild foraging recipe from eattheweeds.com",
        "description": "Fruit vinegar made from mulberries.",
        "servings_yield": "Several pints",
        "ingredients": [
            {"item": "clean mulberries", "quantity": "3", "unit": "quarts"},
            {"item": "white vinegar", "quantity": "3", "unit": "cups", "prep_note": "boiling hot"},
            {"item": "sugar", "quantity": "1", "unit": "cup", "prep_note": "per cup of juice"}
        ],
        "instructions": [
            {"step": 1, "text": "Place mulberries in large bowl."},
            {"step": 2, "text": "Mash berries and pour hot vinegar over them."},
            {"step": 3, "text": "Cover with towel; stir with wooden spoon daily for 3 days."},
            {"step": 4, "text": "Strain juice through jelly bag."},
            {"step": 5, "text": "Add 1 cup sugar per cup juice."},
            {"step": 6, "text": "Boil together for 5 minutes."},
            {"step": 7, "text": "Pour into sterilized jars and seal."},
            {"step": 8, "text": "To serve: Mix 2 tablespoons vinegar in 8-ounce glass with water and ice."}
        ],
        "tags": ["vinegar", "preserves", "mulberry", "foraging", "eat the weeds"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "mulberry-sauce-etw",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Mulberry Sauce",
        "category": "preserves",
        "attribution": "Eat the Weeds - Green Deane",
        "source_note": "Wild foraging recipe from eattheweeds.com",
        "description": "Spiced fruit sauce from mulberries.",
        "servings_yield": "2-3 pints",
        "ingredients": [
            {"item": "mulberries", "quantity": "4", "unit": "cups"},
            {"item": "brown sugar", "quantity": "1 1/2", "unit": "cups"},
            {"item": "cloves", "quantity": "1", "unit": "tsp"},
            {"item": "allspice", "quantity": "1", "unit": "tsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Add sugar and spices to mashed berries."},
            {"step": 2, "text": "Bring to boil."},
            {"step": 3, "text": "Simmer until thick, stirring frequently."},
            {"step": 4, "text": "Bottle and seal."}
        ],
        "tags": ["sauce", "preserves", "mulberry", "foraging", "eat the weeds"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    # ===== CHICKWEED RECIPES =====
    {
        "id": "chickweed-bread-etw",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Chickweed Bread",
        "category": "breads",
        "attribution": "Eat the Weeds - Green Deane",
        "source_note": "Wild foraging recipe from eattheweeds.com",
        "description": "Yeast bread made with sautéed chickweed.",
        "servings_yield": "1 loaf",
        "ingredients": [
            {"item": "chickweed leaves and stems", "quantity": "2", "unit": "cups", "prep_note": "chopped"},
            {"item": "onion", "quantity": "1/4", "unit": "cup", "prep_note": "minced"},
            {"item": "oil", "quantity": "2", "unit": "tbsp"},
            {"item": "honey", "quantity": "2", "unit": "tbsp"},
            {"item": "salt", "quantity": "1", "unit": "tsp"},
            {"item": "wheat flour", "quantity": "3", "unit": "cups"},
            {"item": "warm water", "quantity": "3/4", "unit": "cup"},
            {"item": "yeast", "quantity": "1", "unit": "packet"}
        ],
        "instructions": [
            {"step": 1, "text": "Sauté onion and chickweed until tender (avoid browning)."},
            {"step": 2, "text": "Dissolve honey and yeast in warm water, then add salt."},
            {"step": 3, "text": "Mix yeast mixture with cooled sautéed chickweed and onions."},
            {"step": 4, "text": "Gradually incorporate flour until dough no longer adheres to fingers."},
            {"step": 5, "text": "Form into a ball and allow to rise to double volume."},
            {"step": 6, "text": "Shape into loaves and let rise again."},
            {"step": 7, "text": "Bake at 375°F for 40-45 minutes."}
        ],
        "temperature": "375°F (190°C)",
        "cook_time": "40-45 minutes",
        "tags": ["bread", "yeast", "chickweed", "foraging", "eat the weeds"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "chickweed-bacon-pie-etw",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Chickweed and Bacon Pie",
        "category": "main-dishes",
        "attribution": "Eat the Weeds - Green Deane",
        "source_note": "Wild foraging recipe from eattheweeds.com",
        "description": "Savory pie with chickweed, bacon, and sour cream.",
        "servings_yield": "6-8 servings",
        "ingredients": [
            {"item": "10-inch pie crust", "quantity": "1", "unit": ""},
            {"item": "chickweed", "quantity": "3", "unit": "cups", "prep_note": "chopped"},
            {"item": "slab bacon", "quantity": "1", "unit": "cup", "prep_note": "diced"},
            {"item": "onion", "quantity": "1/2", "unit": "cup", "prep_note": "finely chopped"},
            {"item": "large eggs", "quantity": "3", "unit": ""},
            {"item": "sour cream", "quantity": "1 1/2", "unit": "cups"},
            {"item": "all-purpose flour", "quantity": "1", "unit": "tbsp"},
            {"item": "nutmeg", "quantity": "1/2", "unit": "tsp", "prep_note": "grated"}
        ],
        "instructions": [
            {"step": 1, "text": "Preheat oven to 325°F."},
            {"step": 2, "text": "Line 10-inch pie dish with crust, creating raised border to prevent overflow."},
            {"step": 3, "text": "Remove chickweed leaves and twigs, keeping only greenest parts; rinse and dry."},
            {"step": 4, "text": "Chop chickweed into confetti texture and measure."},
            {"step": 5, "text": "Fry bacon until browning begins, add onion, cook 3 minutes until wilted."},
            {"step": 6, "text": "Transfer bacon and onions to bowl with chickweed using slotted spoon."},
            {"step": 7, "text": "Beat eggs until lemon-colored, mix with sour cream, flour, and nutmeg."},
            {"step": 8, "text": "Combine egg mixture with chickweed, bacon, and onions."},
            {"step": 9, "text": "Spread filling evenly in pie shell, press down firmly with spoon."},
            {"step": 10, "text": "Bake 45-50 minutes until center sets and top turns golden."}
        ],
        "temperature": "325°F (165°C)",
        "cook_time": "45-50 minutes",
        "tags": ["pie", "savory", "chickweed", "bacon", "foraging", "eat the weeds"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    # ===== ELDERBERRY RECIPES =====
    {
        "id": "elderberry-schnapps-etw",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Elderberry Schnapps",
        "category": "beverages",
        "attribution": "Eat the Weeds - Green Deane",
        "source_note": "Wild foraging recipe from eattheweeds.com",
        "description": "Elderberry-infused vodka liqueur.",
        "servings_yield": "1 quart",
        "ingredients": [
            {"item": "elderberries", "quantity": "", "unit": "", "prep_note": "measured by weight"},
            {"item": "unflavored vodka", "quantity": "", "unit": "", "prep_note": "half the weight of berries, or more to cover"}
        ],
        "instructions": [
            {"step": 1, "text": "Rinse and clean elderberries, removing all stems."},
            {"step": 2, "text": "Weigh the prepared berries."},
            {"step": 3, "text": "Place berries in a clean glass jar with tight-fitting lid."},
            {"step": 4, "text": "Add vodka equal to half the berry weight (or more to fully cover)."},
            {"step": 5, "text": "Seal jar and store in a dark place at room temperature."},
            {"step": 6, "text": "Shake occasionally."},
            {"step": 7, "text": "After 1-4 weeks, strain and discard berries."},
            {"step": 8, "text": "Transfer liquid to a new clean jar with tight lid."},
            {"step": 9, "text": "Age for at least two months before consuming."}
        ],
        "tags": ["liqueur", "schnapps", "elderberry", "foraging", "eat the weeds"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "elderberry-wine-etw",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Elderberry Wine",
        "category": "beverages",
        "attribution": "Eat the Weeds - Green Deane",
        "source_note": "Wild foraging recipe from eattheweeds.com",
        "description": "Traditional homemade elderberry wine.",
        "servings_yield": "1 gallon",
        "ingredients": [
            {"item": "ripe elderberries", "quantity": "3", "unit": "lbs"},
            {"item": "fine sugar", "quantity": "2", "unit": "lbs"},
            {"item": "water", "quantity": "3 1/2", "unit": "quarts"},
            {"item": "acid blend", "quantity": "2", "unit": "tsp"},
            {"item": "yeast nutrient", "quantity": "1", "unit": "tsp"},
            {"item": "pectin enzyme", "quantity": "1/2", "unit": "tsp"},
            {"item": "Campden tablet", "quantity": "1", "unit": "", "prep_note": "crushed"},
            {"item": "Montrachet wine yeast", "quantity": "", "unit": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Wash elderberries and remove stems, discarding unsuitable ones."},
            {"step": 2, "text": "Boil water and dissolve sugar into it."},
            {"step": 3, "text": "Place berries in a nylon straining bag and tie it."},
            {"step": 4, "text": "Put bag in primary fermentation container."},
            {"step": 5, "text": "Mash berries while wearing sterilized gloves."},
            {"step": 6, "text": "Pour hot sugar water over berries and cover."},
            {"step": 7, "text": "When cooled to lukewarm, add acid blend, crushed Campden tablet, and yeast nutrient."},
            {"step": 8, "text": "Cover and wait 12 hours."},
            {"step": 9, "text": "Stir in pectin enzyme, cover and wait another 12 hours."},
            {"step": 10, "text": "Add yeast and stir daily for 14 days."},
            {"step": 11, "text": "Gently squeeze bag while wearing sterile gloves after each stirring."},
            {"step": 12, "text": "Drip drain berries without squeezing; add juice to primary container."},
            {"step": 13, "text": "Rack wine into secondary container with airlock."},
            {"step": 14, "text": "Store in dark place and ferment for two months."},
            {"step": 15, "text": "Rack again, top up, and refit airlock."},
            {"step": 16, "text": "Repeat racking process two more times."},
            {"step": 17, "text": "Stabilize wine and wait 10 days."},
            {"step": 18, "text": "Rack final time, sweeten to taste, and bottle."},
            {"step": 19, "text": "Store in dark place for one year before consuming."}
        ],
        "tags": ["wine", "fermented", "elderberry", "foraging", "eat the weeds"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    # ===== HENBIT RECIPE =====
    {
        "id": "spicy-henbit-etw",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Spicy Henbit",
        "category": "vegetables",
        "attribution": "Eat the Weeds - Green Deane",
        "source_note": "Wild foraging recipe from eattheweeds.com",
        "description": "Curried henbit greens in sour cream sauce.",
        "servings_yield": "4 servings",
        "ingredients": [
            {"item": "henbit shoots", "quantity": "4", "unit": "cups"},
            {"item": "butter", "quantity": "3", "unit": "tbsp"},
            {"item": "curry powder", "quantity": "1", "unit": "tsp"},
            {"item": "whole cloves", "quantity": "2", "unit": ""},
            {"item": "ground cinnamon", "quantity": "1/4", "unit": "tsp"},
            {"item": "flour", "quantity": "2", "unit": "tbsp"},
            {"item": "boiling water", "quantity": "1/2", "unit": "cup", "prep_note": "from cooking henbit"},
            {"item": "sour cream", "quantity": "3/4", "unit": "cup"}
        ],
        "instructions": [
            {"step": 1, "text": "Chop four cups of shoots and cover with water, then boil for 10 minutes."},
            {"step": 2, "text": "In a separate pan, melt butter and add curry powder, whole cloves, and cinnamon; stir and cook for one minute."},
            {"step": 3, "text": "Stir in flour and cook for another minute."},
            {"step": 4, "text": "Add half a cup of the boiling water from the henbit, stirring until smooth."},
            {"step": 5, "text": "Drain the boiled henbit and add it to the pan along with sour cream."},
            {"step": 6, "text": "Cook on low heat for 15 minutes."}
        ],
        "cook_time": "25 minutes",
        "tags": ["greens", "henbit", "curry", "foraging", "eat the weeds"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    # ===== MAYPOP RECIPE =====
    {
        "id": "maypop-jelly-etw",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Maypop Jelly",
        "category": "preserves",
        "attribution": "Eat the Weeds - Green Deane",
        "source_note": "Wild foraging recipe from eattheweeds.com",
        "description": "Jelly made from wild passion fruit (maypops).",
        "servings_yield": "2 1/2 pints",
        "ingredients": [
            {"item": "ripe maypops", "quantity": "2", "unit": "cups", "prep_note": "sliced"},
            {"item": "water", "quantity": "1", "unit": "cup"},
            {"item": "sugar", "quantity": "2 1/2", "unit": "cups"},
            {"item": "pectin", "quantity": "1 3/4", "unit": "oz"}
        ],
        "instructions": [
            {"step": 1, "text": "Combine maypops and water, then boil gently for five minutes."},
            {"step": 2, "text": "Strain the mixture, discarding the pulp."},
            {"step": 3, "text": "Combine the liquid with sugar and bring to a full rolling boil."},
            {"step": 4, "text": "Add pectin and return to rolling boil."},
            {"step": 5, "text": "Remove from heat and pour into hot, sterilized jars."},
            {"step": 6, "text": "Seal the jars."}
        ],
        "tags": ["jelly", "preserves", "maypop", "passion fruit", "foraging", "eat the weeds"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    # ===== DAYLILY RECIPE =====
    {
        "id": "daylily-jelly-etw",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Day Lily Jelly",
        "category": "preserves",
        "attribution": "Eat the Weeds - Green Deane",
        "source_note": "Wild foraging recipe from eattheweeds.com",
        "description": "Floral jelly made from daylily petals.",
        "servings_yield": "5-6 half pints",
        "ingredients": [
            {"item": "day lily petals", "quantity": "", "unit": "", "prep_note": "harvested early morning"},
            {"item": "water", "quantity": "", "unit": "", "prep_note": "to cover petals"},
            {"item": "day lily juice", "quantity": "5", "unit": "cups", "prep_note": "from steeped petals"},
            {"item": "sugar", "quantity": "4", "unit": "cups"},
            {"item": "lemon juice", "quantity": "1/4", "unit": "cup"},
            {"item": "pectin", "quantity": "1", "unit": "package"}
        ],
        "instructions": [
            {"step": 1, "text": "Bring petals and water to a boil, then remove from heat."},
            {"step": 2, "text": "Cover and let steep for 10-15 minutes."},
            {"step": 3, "text": "Pour mixture through jelly bag or doubled cheesecloth into strainer."},
            {"step": 4, "text": "Allow liquid to drip into bowl overnight—do not squeeze."},
            {"step": 5, "text": "Measure 5 cups of juice into pot."},
            {"step": 6, "text": "Add sugar, lemon juice, and pectin."},
            {"step": 7, "text": "Follow standard jelly-making procedures to set."}
        ],
        "tags": ["jelly", "preserves", "daylily", "floral", "foraging", "eat the weeds"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    # ===== PINDO PALM RECIPES =====
    {
        "id": "pindo-palm-wine-etw",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Pindo Palm Wine",
        "category": "beverages",
        "attribution": "Eat the Weeds - Green Deane",
        "source_note": "Wild foraging recipe from eattheweeds.com",
        "description": "Fruit wine made from pindo palm (jelly palm) fruit.",
        "servings_yield": "5 liters",
        "ingredients": [
            {"item": "ripe pindo fruit", "quantity": "1.2", "unit": "kg"},
            {"item": "Campden tablet", "quantity": "1", "unit": ""},
            {"item": "sugar", "quantity": "1.2", "unit": "kg"},
            {"item": "boiling water", "quantity": "1", "unit": "liter"},
            {"item": "tannic acid", "quantity": "1/2", "unit": "tsp", "prep_note": "optional"},
            {"item": "yeast nutrient", "quantity": "1/2", "unit": "tsp"},
            {"item": "winemaking yeast", "quantity": "", "unit": ""},
            {"item": "pectinase enzyme", "quantity": "", "unit": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Cover fruit with water and use clean hands to rub out seeds."},
            {"step": 2, "text": "Mash the fibrous fruit pulp."},
            {"step": 3, "text": "Add crushed Campden tablet; let sit covered for 24 hours."},
            {"step": 4, "text": "Prepare wine starter."},
            {"step": 5, "text": "Add pectinase dissolved in water; let sit several hours."},
            {"step": 6, "text": "Add sugar syrup, tannic acid, and yeast nutrient; make up to 5 liters total."},
            {"step": 7, "text": "Add yeast and stir three times daily for 6 days."},
            {"step": 8, "text": "Sieve into demijohn."},
            {"step": 9, "text": "Rack and add sugar as needed for final gravity around 1.020."}
        ],
        "tags": ["wine", "fermented", "pindo palm", "jelly palm", "foraging", "eat the weeds"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "pindo-palm-jelly-etw",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Pindo Palm Jelly",
        "category": "preserves",
        "attribution": "Eat the Weeds - Green Deane",
        "source_note": "Wild foraging recipe from eattheweeds.com",
        "description": "Jelly made from pindo palm (jelly palm) fruit.",
        "servings_yield": "4-5 half pints",
        "ingredients": [
            {"item": "ripe pindo fruit", "quantity": "6", "unit": "cups"},
            {"item": "water", "quantity": "3", "unit": "cups"},
            {"item": "sugar", "quantity": "2-3", "unit": "cups", "prep_note": "depending on taste"},
            {"item": "pectin", "quantity": "", "unit": "", "prep_note": "per Sure Jell box instructions"}
        ],
        "instructions": [
            {"step": 1, "text": "Cut and scrape fruit from seeds (aim for 3 cups cleaned fruit from 6 cups starting amount)."},
            {"step": 2, "text": "Cover fruit with 3 cups water."},
            {"step": 3, "text": "Bring to boil and cook until approximately 3.5 cups infused juice remains."},
            {"step": 4, "text": "Filter juice (optional for clarity)."},
            {"step": 5, "text": "Follow Sure Jell box recipe for three cups fruit juice."},
            {"step": 6, "text": "Adjust sugar to taste and can jars."}
        ],
        "tags": ["jelly", "preserves", "pindo palm", "jelly palm", "foraging", "eat the weeds"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    # ===== GARLIC MUSTARD RECIPE =====
    {
        "id": "garlic-mustard-vichyssoise-etw",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Garlic Mustard Vichyssoise",
        "category": "soups",
        "attribution": "Eat the Weeds - Green Deane",
        "source_note": "Wild foraging recipe from eattheweeds.com",
        "description": "Chilled potato soup with garlic mustard and goat cheese.",
        "servings_yield": "4 servings",
        "ingredients": [
            {"item": "butter", "quantity": "75", "unit": "g"},
            {"item": "onion", "quantity": "1", "unit": "", "prep_note": "chopped"},
            {"item": "three cornered garlic stems", "quantity": "75", "unit": "g"},
            {"item": "water", "quantity": "800", "unit": "ml"},
            {"item": "large potato", "quantity": "1", "unit": "", "prep_note": "peeled, diced and rinsed"},
            {"item": "salt and pepper", "quantity": "", "unit": "", "prep_note": "to taste"},
            {"item": "garlic mustard", "quantity": "75", "unit": "g"},
            {"item": "goat cheese", "quantity": "75", "unit": "g"},
            {"item": "milk for foam", "quantity": "75", "unit": "ml"},
            {"item": "cumin", "quantity": "1", "unit": "pinch"},
            {"item": "white pepper", "quantity": "1", "unit": "pinch"}
        ],
        "instructions": [
            {"step": 1, "text": "In a heavy bottomed pan add water and potatoes with salt and boil until potatoes soften. Set aside."},
            {"step": 2, "text": "Melt butter in a medium saucepan. Add onion and cook until softened. Pour over boiled potatoes and water."},
            {"step": 3, "text": "Blend in food processor until smooth. Add water as needed for consistency. Pass through a sieve."},
            {"step": 4, "text": "Chill in refrigerator. Check seasoning."},
            {"step": 5, "text": "Blanch garlic mustard for 10 seconds in salted boiling water and refresh in ice water."},
            {"step": 6, "text": "Add garlic mustard and blend until smooth."},
            {"step": 7, "text": "Add three cornered garlic and blend until smooth. Check seasoning."},
            {"step": 8, "text": "Serve with crumbled goat's cheese, frothed milk, pinch of cumin, and white pepper."}
        ],
        "prep_time": "30 minutes",
        "cook_time": "10 minutes",
        "tags": ["soup", "vichyssoise", "garlic mustard", "chilled", "foraging", "eat the weeds"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    # ===== BURDOCK RECIPES =====
    {
        "id": "greek-cardune-burdock-etw",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Greek Cardune (Burdock Flower Stalks)",
        "category": "vegetables",
        "attribution": "Eat the Weeds - Green Deane",
        "source_note": "Wild foraging recipe from eattheweeds.com",
        "description": "Mediterranean-style braised burdock flower stalks with rice.",
        "servings_yield": "6-8 servings",
        "ingredients": [
            {"item": "immature burdock flower stalks", "quantity": "4", "unit": "cups", "prep_note": "sliced"},
            {"item": "vinegar", "quantity": "", "unit": "", "prep_note": "dash"},
            {"item": "olive oil", "quantity": "", "unit": "", "prep_note": "dash"},
            {"item": "water or vegetable stock", "quantity": "2", "unit": "cups"},
            {"item": "red onions", "quantity": "2", "unit": "", "prep_note": "sliced"},
            {"item": "olive oil", "quantity": "1/4", "unit": "cup"},
            {"item": "small tomatoes", "quantity": "4", "unit": "", "prep_note": "sliced"},
            {"item": "carrots", "quantity": "2", "unit": "cups", "prep_note": "sliced"},
            {"item": "basmati brown rice", "quantity": "2/3", "unit": "cup"},
            {"item": "fresh dill", "quantity": "3", "unit": "tbsp", "prep_note": "chopped"},
            {"item": "lemon juice", "quantity": "1", "unit": "lemon"},
            {"item": "salt", "quantity": "2", "unit": "tsp", "prep_note": "to taste"},
            {"item": "ground white pepper", "quantity": "1/4", "unit": "tsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Parboil flower stalks 1 minute in salted water to remove bitterness."},
            {"step": 2, "text": "Combine all ingredients in covered saucepan."},
            {"step": 3, "text": "Simmer over low heat 70 minutes until rice is tender."}
        ],
        "cook_time": "70 minutes",
        "tags": ["vegetables", "burdock", "greek", "rice", "foraging", "eat the weeds"],
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

    added = 0
    skipped = 0

    print("\nAdding Eat the Weeds recipes...")
    for recipe in ETW_RECIPES:
        if recipe['id'] in existing_ids:
            print(f"  Skipping (exists): {recipe['id']}")
            skipped += 1
        else:
            recipes.append(recipe)
            existing_ids.add(recipe['id'])
            print(f"  Added: {recipe['title']}")
            added += 1

    # Update total count
    data['meta']['total_recipes'] = len(recipes)

    print(f"\nWriting {len(recipes)} recipes back to {RECIPES_FILE}")
    with open(RECIPES_FILE, 'w') as f:
        json.dump(data, f, indent=2)

    print(f"\nDone!")
    print(f"  Added {added} Eat the Weeds recipes")
    print(f"  Skipped {skipped} existing")
    print(f"  Total recipes now: {len(recipes)}")
    print("\nNote: This is a first batch. Eat the Weeds has 300+ plant pages")
    print("with potentially hundreds more recipes to add.")


if __name__ == "__main__":
    main()
