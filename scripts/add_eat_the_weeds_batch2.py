#!/usr/bin/env python3
"""
Add Eat the Weeds recipes - Batch 2.

This batch includes: hard cider, fermented beverages, hickory nut recipes,
palm recipes, cactus recipes, ginkgo, banana, juneberry, amaranth, hawthorn,
and other wild foraging recipes from Green Deane's eattheweeds.com.
"""

import json
from pathlib import Path

RECIPES_FILE = Path(__file__).parent.parent / "data" / "recipes.json"

ETW_BATCH2_RECIPES = [
    # ===== FERMENTED BEVERAGES =====
    {
        "id": "hard-cider-quick-easy-etw",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Quick & Easy Hard Cider",
        "category": "beverages",
        "attribution": "Eat the Weeds - Green Deane",
        "source_note": "Wild foraging recipe from eattheweeds.com",
        "description": "Simple hard cider made in 5-7 days with natural fermentation.",
        "servings_yield": "1 gallon, ~2% ABV",
        "ingredients": [
            {"item": "apple cider", "quantity": "1", "unit": "gallon", "prep_note": "no preservatives; pasteurized OK"},
            {"item": "starter culture or yeast", "quantity": "1/2", "unit": "cup", "prep_note": "or 1 tsp beer/champagne yeast"},
            {"item": "sugar", "quantity": "", "unit": "", "prep_note": "optional, for sweetness"}
        ],
        "instructions": [
            {"step": 1, "text": "Pour off 1/2 cup juice from cider gallon."},
            {"step": 2, "text": "Add 1/2 cup starter culture to the jug."},
            {"step": 3, "text": "Install fermentation lock (balloon, condom, or commercial airlock with pinhole)."},
            {"step": 4, "text": "Keep in warm location (65-75°F ideal)."},
            {"step": 5, "text": "Ferment 5 days for sweeter result; 7-14 days for drier."},
            {"step": 6, "text": "Bottle in plastic seltzer bottles or capped containers."},
            {"step": 7, "text": "Keep warm 1-2 days to carbonate (bottles become firm)."},
            {"step": 8, "text": "Refrigerate to stop fermentation and slow carbonation buildup."}
        ],
        "notes": ["Avoid juice containing nitrates, sulfides, or potassium sorbate, which kills yeast"],
        "tags": ["cider", "fermented", "beverages", "foraging", "eat the weeds"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "wild-yeast-starter-culture-etw",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Wild Yeast Starter Culture",
        "category": "techniques",
        "attribution": "Eat the Weeds - Green Deane",
        "source_note": "Wild foraging technique from eattheweeds.com",
        "description": "Reusable wild yeast starter for making cider and other fermented drinks.",
        "servings_yield": "Reusable for 2+ years",
        "ingredients": [
            {"item": "pasteurized cider", "quantity": "1", "unit": "gallon", "prep_note": "no preservatives"},
            {"item": "organic apple", "quantity": "1", "unit": "", "prep_note": "unwashed, for wild yeast"}
        ],
        "instructions": [
            {"step": 1, "text": "Peel organic apple; place peeling in cider."},
            {"step": 2, "text": "Cover loosely; keep in warm, dark place."},
            {"step": 3, "text": "After 2-3 weeks, visible bubbles indicate active yeast."},
            {"step": 4, "text": "Use 1/2 cup of this culture per batch of cider."},
            {"step": 5, "text": "To maintain: After bottling each batch, save dregs (sediment + yeast + juice). Add 2 tbsp sugar and store in warm place (refresh every few days) or refrigerate long-term."}
        ],
        "notes": ["Reusable for 2+ years before genetic drift requires starting fresh"],
        "tags": ["starter", "yeast", "fermentation", "foraging", "eat the weeds"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "concord-grape-quick-ferment-etw",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Concord Grape Quick Ferment",
        "category": "beverages",
        "attribution": "Eat the Weeds - Green Deane",
        "source_note": "Wild foraging recipe from eattheweeds.com",
        "description": "Quick fermented grape beverage resembling semi-bubbly red Lambrusco.",
        "servings_yield": "1 gallon",
        "ingredients": [
            {"item": "Concord grape juice", "quantity": "1", "unit": "gallon"},
            {"item": "starter or yeast", "quantity": "1/2", "unit": "cup", "prep_note": "or 1 tsp yeast"},
            {"item": "sugar", "quantity": "", "unit": "", "prep_note": "optional"}
        ],
        "instructions": [
            {"step": 1, "text": "Follow cider method but ferment only 3 days maximum."},
            {"step": 2, "text": "Shorter fermentation preserves sweetness; longer fermentation produces harsh flavor."},
            {"step": 3, "text": "Cap and carbonate for 1 day, then chill and serve."}
        ],
        "notes": ["Results resemble semi-bubbly red Lambrusco when chilled"],
        "tags": ["grape", "wine", "fermented", "beverages", "foraging", "eat the weeds"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "elderberry-wine-gallon-etw",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Elderberry Wine (1 Gallon)",
        "category": "beverages",
        "attribution": "Eat the Weeds - Green Deane",
        "source_note": "Wild foraging recipe from eattheweeds.com",
        "description": "Traditional homemade elderberry wine with detailed fermentation instructions.",
        "servings_yield": "1 gallon",
        "ingredients": [
            {"item": "ripe elderberries", "quantity": "3", "unit": "lbs"},
            {"item": "fine sugar", "quantity": "2", "unit": "lbs"},
            {"item": "water", "quantity": "3.5", "unit": "quarts"},
            {"item": "acid blend", "quantity": "2", "unit": "tsp"},
            {"item": "yeast nutrient", "quantity": "1", "unit": "tsp"},
            {"item": "pectin enzyme", "quantity": "1/2", "unit": "tsp"},
            {"item": "Campden tablet", "quantity": "1", "unit": "", "prep_note": "crushed"},
            {"item": "Montrachet wine yeast", "quantity": "", "unit": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Wash berries and remove stems, discarding unsuitable ones."},
            {"step": 2, "text": "Boil water and dissolve sugar into it."},
            {"step": 3, "text": "Place berries in a nylon straining bag and mash while wearing sterilized gloves."},
            {"step": 4, "text": "Pour hot sugar water over berries and cover. Cool to lukewarm."},
            {"step": 5, "text": "Add acid blend, crushed Campden tablet, and yeast nutrient. Cover and wait 12 hours."},
            {"step": 6, "text": "Stir in pectin enzyme, cover again, and wait another 12 hours before adding yeast."},
            {"step": 7, "text": "Stir daily for 14 days, gently squeezing the bag with sterile gloves."},
            {"step": 8, "text": "Drain without squeezing and transfer juice to a secondary container with airlock."},
            {"step": 9, "text": "Ferment in darkness for two months."},
            {"step": 10, "text": "Rack again, top up, and refit airlock. Repeat racking two more times."},
            {"step": 11, "text": "Stabilize after 10 days, rack once more, sweeten to taste, and bottle."},
            {"step": 12, "text": "Store in darkness for one year."}
        ],
        "notes": ["Freezing berry clusters makes them separate from branches more easily"],
        "tags": ["wine", "elderberry", "fermented", "foraging", "eat the weeds"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "elderberry-schnapps-etw",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Elderberry Schnapps",
        "category": "beverages",
        "attribution": "Eat the Weeds - Green Deane",
        "source_note": "Wild foraging recipe from eattheweeds.com",
        "description": "Elderberry-infused vodka schnapps aged to perfection.",
        "servings_yield": "About 1 pint",
        "ingredients": [
            {"item": "ripe elderberries", "quantity": "", "unit": "", "prep_note": "cleaned of all stems"},
            {"item": "unflavored vodka", "quantity": "", "unit": "", "prep_note": "half the weight of berries, or more to cover"}
        ],
        "instructions": [
            {"step": 1, "text": "Weigh cleaned elderberries and place in a clean jar with tight lid."},
            {"step": 2, "text": "Cover with vodka equal to half their weight (or enough to cover)."},
            {"step": 3, "text": "Seal tightly and steep in a dark place at room temperature for one to four weeks, shaking occasionally."},
            {"step": 4, "text": "Strain and discard berries."},
            {"step": 5, "text": "Transfer liquid to clean jar and age at least two months before serving."}
        ],
        "tags": ["schnapps", "elderberry", "liqueur", "foraging", "eat the weeds"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "walnut-liquor-etw",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Walnut Liquor (Nocino)",
        "category": "beverages",
        "attribution": "Eat the Weeds - Green Deane",
        "source_note": "Wild foraging recipe from eattheweeds.com",
        "description": "Traditional walnut liqueur made from green walnuts.",
        "servings_yield": "About 1 quart",
        "ingredients": [
            {"item": "green walnuts", "quantity": "25", "unit": "", "prep_note": "dehusked, about apricot-sized"},
            {"item": "cloves", "quantity": "3", "unit": ""},
            {"item": "cinnamon stick", "quantity": "1", "unit": ""},
            {"item": "lemon peel", "quantity": "1", "unit": "", "prep_note": "yellow part only, no white pith"},
            {"item": "vodka", "quantity": "1", "unit": "quart", "prep_note": "100 proof"},
            {"item": "sugar", "quantity": "3", "unit": "cups"}
        ],
        "instructions": [
            {"step": 1, "text": "Soak the walnuts overnight to draw out any worms and impurities."},
            {"step": 2, "text": "Quarter them and place in a large jar with all other ingredients."},
            {"step": 3, "text": "Place in a sunny spot, sealed, for at least 40 days (2 months is better)."},
            {"step": 4, "text": "Shake every few days."},
            {"step": 5, "text": "Strain and bottle the liquid; let sit for another month or two minimum."},
            {"step": 6, "text": "Best after aging 2-3 years."}
        ],
        "notes": ["Optional: Combine filter solids with 2 cups alcohol, 1 cup sugar, and a bottle of cheap sparkling wine for a secondary liqueur"],
        "tags": ["liqueur", "walnut", "nocino", "foraging", "eat the weeds"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    # ===== HICKORY NUT RECIPES =====
    {
        "id": "hickory-nut-coffee-etw",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Hickory Nut Coffee",
        "category": "beverages",
        "attribution": "Eat the Weeds - Green Deane",
        "source_note": "Wild foraging recipe from eattheweeds.com",
        "description": "Coffee-like beverage made from roasted hickory nuts.",
        "servings_yield": "1-2 cups",
        "ingredients": [
            {"item": "hulled hickory nuts", "quantity": "6", "unit": "", "prep_note": "larva-free"},
            {"item": "water", "quantity": "1-2", "unit": "cups"}
        ],
        "instructions": [
            {"step": 1, "text": "Roast nuts for 15 minutes at 350°F."},
            {"step": 2, "text": "Cool completely. Do not cook longer or at higher temperature without first scoring them so heat can escape."},
            {"step": 3, "text": "Split shells, add to water, bring to boil."},
            {"step": 4, "text": "Strain when water turns golden and serve."}
        ],
        "temperature": "350°F (175°C)",
        "tags": ["coffee", "hickory", "beverage", "foraging", "eat the weeds"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "hickory-nut-cake-etw",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Hickory Nut Cake",
        "category": "desserts",
        "attribution": "Eat the Weeds - Green Deane",
        "source_note": "Wild foraging recipe from eattheweeds.com",
        "description": "Classic three-layer cake with hickory nuts.",
        "servings_yield": "12-16 servings",
        "ingredients": [
            {"item": "butter", "quantity": "1/2", "unit": "cup"},
            {"item": "sugar", "quantity": "1.5", "unit": "cups"},
            {"item": "cake flour", "quantity": "2.5", "unit": "cups"},
            {"item": "baking powder", "quantity": "1", "unit": "tbsp"},
            {"item": "salt", "quantity": "1/4", "unit": "tsp"},
            {"item": "milk", "quantity": "1", "unit": "cup"},
            {"item": "vanilla", "quantity": "1", "unit": "tsp"},
            {"item": "chopped hickory nuts", "quantity": "1", "unit": "cup"},
            {"item": "egg whites", "quantity": "5", "unit": "", "prep_note": "stiffly beaten"}
        ],
        "instructions": [
            {"step": 1, "text": "Preheat oven to 350°F."},
            {"step": 2, "text": "Cream butter and sugar together."},
            {"step": 3, "text": "Alternate adding flour mixture and milk."},
            {"step": 4, "text": "Add vanilla."},
            {"step": 5, "text": "Fold in nuts and stiffly beaten egg whites."},
            {"step": 6, "text": "Divide among three greased pans."},
            {"step": 7, "text": "Bake 20 minutes until done."}
        ],
        "temperature": "350°F (175°C)",
        "tags": ["cake", "hickory", "dessert", "foraging", "eat the weeds"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "hickory-nut-filling-etw",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Hickory Nut Filling",
        "category": "desserts",
        "attribution": "Eat the Weeds - Green Deane",
        "source_note": "Wild foraging recipe from eattheweeds.com",
        "description": "Creamy filling for cakes made with hickory nuts.",
        "ingredients": [
            {"item": "sugar", "quantity": "3", "unit": "cups"},
            {"item": "light cream", "quantity": "1", "unit": "cup"},
            {"item": "corn syrup", "quantity": "1", "unit": "tsp"},
            {"item": "butter", "quantity": "1", "unit": "tbsp"},
            {"item": "chopped hickory nuts", "quantity": "1", "unit": "cup"}
        ],
        "instructions": [
            {"step": 1, "text": "Cook sugar, cream, and syrup to 238°F (soft ball stage)."},
            {"step": 2, "text": "Remove from heat and cool."},
            {"step": 3, "text": "Beat until creamy."},
            {"step": 4, "text": "Stir in butter and nuts."}
        ],
        "tags": ["filling", "frosting", "hickory", "dessert", "foraging", "eat the weeds"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "hickory-nut-pie-etw",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Hickory Nut Pie",
        "category": "desserts",
        "attribution": "Eat the Weeds - Green Deane",
        "source_note": "Wild foraging recipe from eattheweeds.com",
        "description": "Southern-style pie similar to pecan pie but with hickory nuts.",
        "servings_yield": "8 servings",
        "ingredients": [
            {"item": "pastry for 9-inch deep-dish pie", "quantity": "1", "unit": ""},
            {"item": "eggs", "quantity": "3", "unit": ""},
            {"item": "light corn syrup", "quantity": "1", "unit": "cup"},
            {"item": "melted butter", "quantity": "1/4", "unit": "cup"},
            {"item": "brown sugar", "quantity": "1/2", "unit": "cup"},
            {"item": "maple syrup or flavoring", "quantity": "1", "unit": "tbsp", "prep_note": "or 1/2 tsp maple flavoring"},
            {"item": "coarsely chopped hickory nuts", "quantity": "1", "unit": "cup", "prep_note": "heaping"}
        ],
        "instructions": [
            {"step": 1, "text": "Preheat to 350°F."},
            {"step": 2, "text": "Beat eggs, add syrup and butter."},
            {"step": 3, "text": "Stir in sugar, maple syrup, and nuts."},
            {"step": 4, "text": "Pour into pastry shell."},
            {"step": 5, "text": "Bake 45-55 minutes until set."},
            {"step": 6, "text": "Serve with whipped cream."}
        ],
        "temperature": "350°F (175°C)",
        "tags": ["pie", "hickory", "dessert", "foraging", "eat the weeds"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "hickory-nut-refrigerator-cookies-etw",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Hickory Nut Refrigerator Cookies",
        "category": "desserts",
        "attribution": "Eat the Weeds - Green Deane",
        "source_note": "Wild foraging recipe from eattheweeds.com",
        "description": "Slice-and-bake cookies with hickory nuts.",
        "servings_yield": "4 dozen",
        "ingredients": [
            {"item": "butter", "quantity": "1", "unit": "cup", "prep_note": "room temperature"},
            {"item": "egg", "quantity": "1", "unit": ""},
            {"item": "sugar", "quantity": "1", "unit": "cup"},
            {"item": "vanilla", "quantity": "1", "unit": "tsp"},
            {"item": "flour", "quantity": "2", "unit": "cups"},
            {"item": "baking soda", "quantity": "1/2", "unit": "tsp"},
            {"item": "salt", "quantity": "1/4", "unit": "tsp"},
            {"item": "chopped hickory nuts", "quantity": "1", "unit": "cup"}
        ],
        "instructions": [
            {"step": 1, "text": "Cream butter, add egg and beat until fluffy."},
            {"step": 2, "text": "Beat in sugar and vanilla."},
            {"step": 3, "text": "Stir in flour, baking soda, salt, and nuts."},
            {"step": 4, "text": "Shape into two logs, wrap and refrigerate 1-2 hours."},
            {"step": 5, "text": "Slice thin, bake at 350°F for 10-15 minutes until golden."}
        ],
        "temperature": "350°F (175°C)",
        "tags": ["cookies", "hickory", "dessert", "foraging", "eat the weeds"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "maple-hickory-apple-crisp-etw",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Maple Hickory Apple Crisp",
        "category": "desserts",
        "attribution": "Eat the Weeds - Green Deane",
        "source_note": "Wild foraging recipe from eattheweeds.com",
        "description": "Apple crisp topped with hickory nuts and maple syrup.",
        "servings_yield": "15 servings",
        "ingredients": [
            {"item": "sliced apples", "quantity": "8", "unit": "cups"},
            {"item": "lemon juice", "quantity": "1", "unit": "tbsp"},
            {"item": "ground cinnamon", "quantity": "3", "unit": "tsp", "prep_note": "divided"},
            {"item": "flour", "quantity": "3", "unit": "tbsp"},
            {"item": "water or apple juice", "quantity": "1/2", "unit": "cup"},
            {"item": "rolled oats", "quantity": "1", "unit": "cup"},
            {"item": "whole-wheat flour", "quantity": "1", "unit": "cup"},
            {"item": "brown sugar", "quantity": "1", "unit": "cup"},
            {"item": "hickory nuts", "quantity": "1", "unit": "cup"},
            {"item": "butter", "quantity": "1", "unit": "cup", "prep_note": "room temperature"},
            {"item": "pure maple syrup", "quantity": "1/4-1/2", "unit": "cup"}
        ],
        "instructions": [
            {"step": 1, "text": "Preheat to 375°F."},
            {"step": 2, "text": "Toss apples with lemon juice, 1 tsp cinnamon, and 3 tbsp flour."},
            {"step": 3, "text": "Layer in greased pan with liquid."},
            {"step": 4, "text": "Mix oats, flour, sugar, remaining cinnamon, nuts, and butter until crumbly."},
            {"step": 5, "text": "Spread over apples, drizzle with maple syrup."},
            {"step": 6, "text": "Bake 45 minutes."}
        ],
        "temperature": "375°F (190°C)",
        "tags": ["apple", "crisp", "hickory", "maple", "dessert", "foraging", "eat the weeds"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "hickory-wild-rice-stuffing-etw",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Hickory Wild Rice Stuffing",
        "category": "sides",
        "attribution": "Eat the Weeds - Green Deane",
        "source_note": "Wild foraging recipe from eattheweeds.com",
        "description": "Savory stuffing with wild rice, sausage, and hickory nuts.",
        "servings_yield": "12 servings",
        "ingredients": [
            {"item": "dry wild rice", "quantity": "1.25", "unit": "cups"},
            {"item": "ground sausage", "quantity": "8", "unit": "oz", "prep_note": "optional"},
            {"item": "butter", "quantity": "1", "unit": "tbsp"},
            {"item": "celery", "quantity": "2", "unit": "ribs", "prep_note": "diced"},
            {"item": "onion", "quantity": "1", "unit": "medium", "prep_note": "minced"},
            {"item": "salt", "quantity": "1", "unit": "tsp"},
            {"item": "black pepper", "quantity": "1/2", "unit": "tsp"},
            {"item": "chopped hickory nuts", "quantity": "2", "unit": "cups"}
        ],
        "instructions": [
            {"step": 1, "text": "Cook rice per package directions until tender."},
            {"step": 2, "text": "Cook sausage if using, add to rice."},
            {"step": 3, "text": "Sauté celery and onion in drippings or butter."},
            {"step": 4, "text": "Combine with rice, add salt, pepper, and nuts."},
            {"step": 5, "text": "Use for poultry stuffing or bake in casserole at 325°F for 20 minutes."}
        ],
        "temperature": "325°F (165°C)",
        "tags": ["stuffing", "wild rice", "hickory", "holiday", "foraging", "eat the weeds"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    # ===== CHESTNUT RECIPE =====
    {
        "id": "hungarian-chestnut-soup-etw",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Hungarian Cream of Chestnut Soup (Gesztenye Leves)",
        "category": "soups",
        "attribution": "Eat the Weeds - Green Deane",
        "source_note": "Wild foraging recipe from eattheweeds.com",
        "description": "Rich Hungarian soup with chestnuts, ham, and cream.",
        "servings_yield": "6-8 servings",
        "ingredients": [
            {"item": "cooked chestnuts", "quantity": "12-14", "unit": "oz", "prep_note": "peeled, finely chopped"},
            {"item": "butter", "quantity": "4", "unit": "tbsp"},
            {"item": "parsnips", "quantity": "2", "unit": "", "prep_note": "peeled and thinly sliced"},
            {"item": "carrots", "quantity": "2", "unit": "", "prep_note": "peeled and thinly sliced diagonally"},
            {"item": "apples", "quantity": "2", "unit": "", "prep_note": "peeled, cored, quartered and thinly sliced"},
            {"item": "leeks", "quantity": "2", "unit": "", "prep_note": "white part only, thinly sliced"},
            {"item": "Hungarian paprika", "quantity": "2", "unit": "tsp", "prep_note": "sweet or hot"},
            {"item": "ham", "quantity": "1/2", "unit": "lb", "prep_note": "julienne-sliced, leftover"},
            {"item": "chicken stock", "quantity": "5", "unit": "cups"},
            {"item": "whipping cream", "quantity": "1.5", "unit": "cups"},
            {"item": "egg yolks", "quantity": "2", "unit": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Prepare chestnuts: Score fresh chestnuts with an X on the bottom. Boil in water 30 minutes, cool slightly, and peel. Chop finely once completely cooled."},
            {"step": 2, "text": "Melt butter in a large saucepan. Add parsnips, carrots, apples, and leeks. Cook 10 minutes, stirring occasionally, until nearly tender."},
            {"step": 3, "text": "Mix in ham, chestnuts, and paprika. Cook one minute."},
            {"step": 4, "text": "Add stock and bring to boil. Reduce heat and simmer uncovered 20 minutes."},
            {"step": 5, "text": "Whisk cream and egg yolks together. Temper by slowly adding hot soup broth while whisking."},
            {"step": 6, "text": "Pour mixture back into soup, whisking constantly for one minute until thickened."},
            {"step": 7, "text": "Season to taste. Serve with sour cream if desired."}
        ],
        "tags": ["soup", "chestnut", "Hungarian", "cream", "foraging", "eat the weeds"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    # ===== PALM RECIPES =====
    {
        "id": "swamp-cabbage-slaw-etw",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Swamp Cabbage Slaw (Heart of Palm)",
        "category": "salads",
        "attribution": "Eat the Weeds - Green Deane (from Marian Van Atta's Wild Edibles)",
        "source_note": "Wild foraging recipe from eattheweeds.com",
        "description": "Simple slaw made from fresh heart of palm.",
        "ingredients": [
            {"item": "heart of palm", "quantity": "", "unit": "", "prep_note": "cut fine or shredded"},
            {"item": "mayonnaise", "quantity": "", "unit": "", "prep_note": "to taste"},
            {"item": "pickle relish", "quantity": "1-2", "unit": "tsp"},
            {"item": "salt and pepper", "quantity": "", "unit": "", "prep_note": "to taste"}
        ],
        "instructions": [
            {"step": 1, "text": "Optionally soak shredded palm hearts in ice water for an hour."},
            {"step": 2, "text": "Mix with mayonnaise and pickle relish."},
            {"step": 3, "text": "Season to taste with salt and pepper."}
        ],
        "tags": ["salad", "slaw", "heart of palm", "florida", "foraging", "eat the weeds"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "roasted-palm-seed-beverage-etw",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Roasted Palm Seed Beverage",
        "category": "beverages",
        "attribution": "Eat the Weeds - Green Deane",
        "source_note": "Wild foraging recipe from eattheweeds.com",
        "description": "Coffee-like drink made from roasted palm kernels.",
        "ingredients": [
            {"item": "palm kernels", "quantity": "", "unit": "", "prep_note": "pulpless"}
        ],
        "instructions": [
            {"step": 1, "text": "Roast pulpless kernels at 350°F for 20-30 minutes."},
            {"step": 2, "text": "Grind using an industrial coffee grinder and grain grinder."},
            {"step": 3, "text": "Brew like coffee for a passable coffee-like drink, especially aromatic."}
        ],
        "temperature": "350°F (175°C)",
        "tags": ["coffee", "palm", "beverage", "florida", "foraging", "eat the weeds"],
        "confidence": {"overall": "medium", "flags": ["Requires industrial grinder"]},
        "image_refs": []
    },
    # ===== CACTUS RECIPES =====
    {
        "id": "grilled-cactus-pads-etw",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Grilled Cactus Pads (Nopales)",
        "category": "sides",
        "attribution": "Eat the Weeds - Green Deane",
        "source_note": "Wild foraging recipe from eattheweeds.com",
        "description": "Simple grilled prickly pear cactus pads.",
        "ingredients": [
            {"item": "cactus pads", "quantity": "", "unit": "", "prep_note": "spines removed"},
            {"item": "oil", "quantity": "", "unit": "", "prep_note": "for brushing"}
        ],
        "instructions": [
            {"step": 1, "text": "Scrub pads thoroughly and remove all spines."},
            {"step": 2, "text": "Cut around spiny nodules completely."},
            {"step": 3, "text": "Brush with oil while grilling."},
            {"step": 4, "text": "Grill over charcoal 10-12 minutes per side (thicker pads need longer)."},
            {"step": 5, "text": "Serve hot."}
        ],
        "notes": ["Select the best pads when shiny and not too thick", "Remove glochids by spraying with water, burning off, or using duct tape"],
        "tags": ["cactus", "nopales", "grilled", "sides", "foraging", "eat the weeds"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "cactus-jelly-etw",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Prickly Pear Cactus Jelly",
        "category": "preserves",
        "attribution": "Eat the Weeds - Green Deane",
        "source_note": "Wild foraging recipe from eattheweeds.com",
        "description": "Beautiful pink-red jelly from prickly pear cactus fruit.",
        "servings_yield": "About 4 half-pints",
        "ingredients": [
            {"item": "cactus fruit", "quantity": "1-2", "unit": "quarts", "prep_note": "about 1.5 pounds"},
            {"item": "sugar", "quantity": "3", "unit": "cups"},
            {"item": "lemon juice", "quantity": "1/2", "unit": "cup"},
            {"item": "liquid fruit pectin", "quantity": "6", "unit": "oz"},
            {"item": "boiling water", "quantity": "", "unit": ""},
            {"item": "cheesecloth", "quantity": "", "unit": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Place fruit in large saucepan, cover with boiling water, let stand 2-3 minutes, drain."},
            {"step": 2, "text": "Peel fruit, cut into pieces, cover with water and boil 5 minutes."},
            {"step": 3, "text": "Pour through cheesecloth, drain thoroughly, discard seeds."},
            {"step": 4, "text": "Combine juice, sugar, and lemon juice in large saucepan."},
            {"step": 5, "text": "Bring to rolling boil, reduce heat to medium-high."},
            {"step": 6, "text": "Add pectin, cook 8-12 minutes until thickened."},
            {"step": 7, "text": "Skim foam, pour into sterilized jars."},
            {"step": 8, "text": "Process in boiling water bath 5 minutes."}
        ],
        "notes": ["Ripe fruit flesh tastes similar to raspberries", "Eating ripe fruit can turn urine reddish (normal)"],
        "tags": ["jelly", "cactus", "prickly pear", "preserves", "foraging", "eat the weeds"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "cactus-monterey-etw",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Cactus Monterey",
        "category": "sides",
        "attribution": "Eat the Weeds - Green Deane",
        "source_note": "Wild foraging recipe from eattheweeds.com",
        "description": "Savory cactus dish with tomatoes, peppers, and cheese.",
        "ingredients": [
            {"item": "cactus pieces", "quantity": "1", "unit": "lb"},
            {"item": "small tomato", "quantity": "1", "unit": ""},
            {"item": "small white onion", "quantity": "1/4", "unit": ""},
            {"item": "jalapeño pepper", "quantity": "1", "unit": ""},
            {"item": "cilantro", "quantity": "1/4", "unit": "bunch"},
            {"item": "shredded Monterey Jack cheese", "quantity": "1/4", "unit": "cup"},
            {"item": "salt", "quantity": "1", "unit": "tsp", "prep_note": "optional"},
            {"item": "avocado or olive oil", "quantity": "4", "unit": "tbsp", "prep_note": "low-heat"}
        ],
        "instructions": [
            {"step": 1, "text": "Steam cactus until softened, drain."},
            {"step": 2, "text": "Lightly fry remaining ingredients (except cheese)."},
            {"step": 3, "text": "Combine fried ingredients with cactus."},
            {"step": 4, "text": "Simmer 15 minutes."},
            {"step": 5, "text": "Top with cheese before serving."}
        ],
        "tags": ["cactus", "nopales", "mexican", "sides", "foraging", "eat the weeds"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "cactus-flower-wine-etw",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Cactus Flower Wine",
        "category": "beverages",
        "attribution": "Eat the Weeds - Green Deane",
        "source_note": "Wild foraging recipe from eattheweeds.com",
        "description": "Delicate wine made from prickly pear cactus flowers.",
        "servings_yield": "About 1 gallon",
        "ingredients": [
            {"item": "packed cactus flowers", "quantity": "2.5", "unit": "quarts"},
            {"item": "granulated sugar", "quantity": "2", "unit": "lbs"},
            {"item": "frozen white grape juice concentrate", "quantity": "11", "unit": "oz"},
            {"item": "acid blend", "quantity": "1.75", "unit": "tsp"},
            {"item": "grape tannin", "quantity": "1/8", "unit": "tsp"},
            {"item": "water", "quantity": "6.25", "unit": "pints"},
            {"item": "Campden tablet", "quantity": "1", "unit": "", "prep_note": "crushed"},
            {"item": "yeast nutrient", "quantity": "1", "unit": "tsp"},
            {"item": "Champagne wine yeast", "quantity": "1", "unit": "packet"}
        ],
        "instructions": [
            {"step": 1, "text": "Wash flowers, place in nylon straining bag with dozen marbles for weight."},
            {"step": 2, "text": "Heat 1 quart water, dissolve sugar."},
            {"step": 3, "text": "Cool with frozen grape concentrate and remaining water, add to primary fermenter."},
            {"step": 4, "text": "Add remaining ingredients except yeast, stir well."},
            {"step": 5, "text": "Cover and wait 10-12 hours before adding activated yeast."},
            {"step": 6, "text": "Stir daily until specific gravity drops to 1.020."},
            {"step": 7, "text": "Drip-drain bag, transfer to secondary with airlock."},
            {"step": 8, "text": "Rack after 45 days, then again after another 45 days."},
            {"step": 9, "text": "Final rack 60 days after clearing, age 90-120 days."},
            {"step": 10, "text": "Stabilize, sweeten to taste, bottle."},
            {"step": 11, "text": "Taste after 6 months in bottle."}
        ],
        "tags": ["wine", "cactus", "flower", "fermented", "foraging", "eat the weeds"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    # ===== GINKGO RECIPES =====
    {
        "id": "roasted-ginkgo-nuts-etw",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Roasted Ginkgo Nuts",
        "category": "snacks",
        "attribution": "Eat the Weeds - Green Deane",
        "source_note": "Wild foraging recipe from eattheweeds.com",
        "description": "Traditional roasted ginkgo nuts for snacking or adding to dishes.",
        "ingredients": [
            {"item": "cleaned ginkgo seeds", "quantity": "", "unit": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Roast cleaned seeds at 350°F for one hour."},
            {"step": 2, "text": "Crush seeds between towels while tapping gently with a hammer."},
            {"step": 3, "text": "Shell and serve."}
        ],
        "temperature": "350°F (175°C)",
        "notes": ["Ginkgo nuts can be used in soups, stuffings, desserts, meat dishes, poultry dishes and vegetarian dishes"],
        "tags": ["ginkgo", "nuts", "roasted", "snacks", "foraging", "eat the weeds"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "boiled-ginkgo-nuts-etw",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Boiled Ginkgo Nuts",
        "category": "snacks",
        "attribution": "Eat the Weeds - Green Deane",
        "source_note": "Wild foraging recipe from eattheweeds.com",
        "description": "Simple boiled ginkgo nuts as a snack.",
        "ingredients": [
            {"item": "raw ginkgo seeds", "quantity": "", "unit": ""},
            {"item": "salted water", "quantity": "", "unit": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Crack seeds raw using a nutcracker."},
            {"step": 2, "text": "Boil seeds in salty water until tender."},
            {"step": 3, "text": "Rub with a ladle to remove the brown membrane."},
            {"step": 4, "text": "Salt and serve."}
        ],
        "tags": ["ginkgo", "nuts", "boiled", "snacks", "foraging", "eat the weeds"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    # ===== BANANA RECIPES =====
    {
        "id": "banana-tree-stem-sauteed-etw",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Sautéed Banana Tree Stem",
        "category": "sides",
        "attribution": "Eat the Weeds - Green Deane",
        "source_note": "Wild foraging recipe from eattheweeds.com",
        "description": "Indian-style sautéed banana stem with coconut and spices.",
        "ingredients": [
            {"item": "banana tree stem core", "quantity": "1", "unit": "lb"},
            {"item": "grated coconut", "quantity": "1/4", "unit": "coconut"},
            {"item": "garlic cloves", "quantity": "6", "unit": ""},
            {"item": "chili powder", "quantity": "1/4", "unit": "tsp"},
            {"item": "curry leaves", "quantity": "1.5", "unit": "tsp"},
            {"item": "salt", "quantity": "", "unit": "", "prep_note": "to taste"},
            {"item": "mustard seeds", "quantity": "1/2", "unit": "tsp"},
            {"item": "coconut oil", "quantity": "1", "unit": "tbsp"},
            {"item": "turmeric", "quantity": "1/4", "unit": "tsp", "prep_note": "optional"}
        ],
        "instructions": [
            {"step": 1, "text": "Peel outer fibers from stem and chop finely."},
            {"step": 2, "text": "Heat half the oil, add mustard seeds until crackling."},
            {"step": 3, "text": "Add stem pieces, curry, salt, and chili powder."},
            {"step": 4, "text": "Cover and simmer until soft (approximately one hour)."},
            {"step": 5, "text": "Grind coconut and garlic together."},
            {"step": 6, "text": "When stem is almost cooked, add coconut-garlic mixture and continue cooking covered."},
            {"step": 7, "text": "Finish with remaining coconut oil and let rest before serving."}
        ],
        "tags": ["banana", "stem", "indian", "sides", "foraging", "eat the weeds"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "banana-flower-stir-fry-etw",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Banana Flower Stir Fry",
        "category": "sides",
        "attribution": "Eat the Weeds - Green Deane",
        "source_note": "Wild foraging recipe from eattheweeds.com",
        "description": "Indian-style banana flower stir fry with lentils.",
        "ingredients": [
            {"item": "banana flower", "quantity": "1", "unit": ""},
            {"item": "lentils", "quantity": "1/2", "unit": "cup"},
            {"item": "onion", "quantity": "1", "unit": "small"},
            {"item": "green chillies", "quantity": "5", "unit": ""},
            {"item": "garlic", "quantity": "1", "unit": "clove"},
            {"item": "cumin powder", "quantity": "1/4", "unit": "tsp"},
            {"item": "turmeric powder", "quantity": "", "unit": "pinch"},
            {"item": "grated coconut", "quantity": "1/2", "unit": "cup"},
            {"item": "oil", "quantity": "1", "unit": "tbsp"},
            {"item": "curry leaves", "quantity": "", "unit": ""},
            {"item": "mustard seeds", "quantity": "", "unit": ""},
            {"item": "salt", "quantity": "", "unit": "", "prep_note": "to taste"}
        ],
        "instructions": [
            {"step": 1, "text": "Cook lentils separately."},
            {"step": 2, "text": "Remove outer petals from flower; chop inner cream portion finely."},
            {"step": 3, "text": "Apply coconut oil to palms and rub chopped flower to remove lumps."},
            {"step": 4, "text": "Heat oil and splutter mustard seeds. Add chillies, onion, curry leaves; sauté until onions brown."},
            {"step": 5, "text": "Add flower, garlic, spices, and salt. Cook covered 5 minutes without water."},
            {"step": 6, "text": "Stir in lentils and cook 5 more minutes until dry."}
        ],
        "notes": ["Optional: soak chopped flower in milk to reduce bitterness"],
        "tags": ["banana", "flower", "indian", "sides", "foraging", "eat the weeds"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    # ===== JUNEBERRY RECIPES =====
    {
        "id": "juneberry-pie-etw",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Juneberry Pie",
        "category": "desserts",
        "attribution": "Eat the Weeds - Green Deane",
        "source_note": "Wild foraging recipe from eattheweeds.com",
        "description": "Classic pie made with foraged juneberries (serviceberries).",
        "ingredients": [
            {"item": "pastry for 2-crust pie", "quantity": "1", "unit": ""},
            {"item": "juneberries", "quantity": "3-4", "unit": "cups", "prep_note": "washed"},
            {"item": "flour", "quantity": "2", "unit": "tbsp"},
            {"item": "lemon juice", "quantity": "2", "unit": "tbsp"},
            {"item": "sugar", "quantity": "1/2", "unit": "cup"},
            {"item": "nutmeg", "quantity": "1/4", "unit": "tsp"},
            {"item": "sugar for sprinkling", "quantity": "", "unit": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Combine all filling ingredients together."},
            {"step": 2, "text": "Pour into pastry-lined pie plate."},
            {"step": 3, "text": "Top with pastry strips and sprinkle with sugar."},
            {"step": 4, "text": "Bake at 450°F for 15 minutes then at 350°F for 25 minutes more."}
        ],
        "temperature": "450°F then 350°F",
        "tags": ["pie", "juneberry", "serviceberry", "dessert", "foraging", "eat the weeds"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "juneberry-jam-etw",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Juneberry Jam",
        "category": "preserves",
        "attribution": "Eat the Weeds - Green Deane",
        "source_note": "Wild foraging recipe from eattheweeds.com",
        "description": "Simple jam made with juneberries and rhubarb.",
        "ingredients": [
            {"item": "juneberries", "quantity": "4", "unit": "cups", "prep_note": "cleaned"},
            {"item": "cut-up rhubarb", "quantity": "4", "unit": "cups"},
            {"item": "white sugar", "quantity": "4", "unit": "cups"},
            {"item": "cinnamon", "quantity": "1", "unit": "tsp", "prep_note": "optional"},
            {"item": "lemon juice", "quantity": "1", "unit": "tbsp", "prep_note": "optional"}
        ],
        "instructions": [
            {"step": 1, "text": "Grind berries and combine with sugar and rhubarb."},
            {"step": 2, "text": "Bring to simmer."},
            {"step": 3, "text": "Stir and cook until thick. Burns easily - watch carefully."},
            {"step": 4, "text": "Pour into jars and seal."}
        ],
        "tags": ["jam", "juneberry", "serviceberry", "rhubarb", "preserves", "foraging", "eat the weeds"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "juneberry-muffins-etw",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Juneberry Muffins",
        "category": "breads",
        "attribution": "Eat the Weeds - Green Deane",
        "source_note": "Wild foraging recipe from eattheweeds.com",
        "description": "Muffins studded with fresh juneberries.",
        "servings_yield": "12 muffins",
        "ingredients": [
            {"item": "flour", "quantity": "2", "unit": "cups"},
            {"item": "sugar", "quantity": "1/4", "unit": "cup"},
            {"item": "baking powder", "quantity": "3", "unit": "tsp"},
            {"item": "salt", "quantity": "1/4", "unit": "tsp"},
            {"item": "shortening", "quantity": "1/4", "unit": "cup"},
            {"item": "egg", "quantity": "1", "unit": ""},
            {"item": "milk", "quantity": "1", "unit": "cup"},
            {"item": "juneberries", "quantity": "1.5", "unit": "cups"}
        ],
        "instructions": [
            {"step": 1, "text": "Combine dry ingredients with egg, shortening, salt, and milk. Blend well."},
            {"step": 2, "text": "Stir in berries."},
            {"step": 3, "text": "Fill muffin cups two-thirds full."},
            {"step": 4, "text": "Bake 20 minutes at 350°F."}
        ],
        "temperature": "350°F (175°C)",
        "tags": ["muffins", "juneberry", "serviceberry", "breakfast", "foraging", "eat the weeds"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    # ===== AMARANTH RECIPE =====
    {
        "id": "amaranth-tabouli-etw",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Amaranth Tabouli",
        "category": "salads",
        "attribution": "Eat the Weeds - Green Deane",
        "source_note": "Wild foraging recipe from eattheweeds.com",
        "description": "Middle Eastern-style grain salad made with amaranth instead of bulgur.",
        "ingredients": [
            {"item": "pre-soaked amaranth seeds", "quantity": "1", "unit": "cup"},
            {"item": "parsley", "quantity": "1", "unit": "cup", "prep_note": "chopped"},
            {"item": "scallions", "quantity": "1/2", "unit": "cup", "prep_note": "chopped"},
            {"item": "fresh mint", "quantity": "2", "unit": "tbsp"},
            {"item": "lemon juice", "quantity": "1/2", "unit": "cup"},
            {"item": "olive oil", "quantity": "1/4", "unit": "cup"},
            {"item": "garlic cloves", "quantity": "2", "unit": "", "prep_note": "pressed"},
            {"item": "olives", "quantity": "1/4", "unit": "cup", "prep_note": "sliced"},
            {"item": "lettuce leaves", "quantity": "", "unit": "", "prep_note": "whole, for serving"}
        ],
        "instructions": [
            {"step": 1, "text": "Simmer amaranth in equal volume of water for 12-15 minutes and cool completely."},
            {"step": 2, "text": "Combine all ingredients except lettuce and olives in a bowl, tossing gently."},
            {"step": 3, "text": "Refrigerate at least one hour to blend flavors."},
            {"step": 4, "text": "Line a serving bowl with washed, dried lettuce leaves."},
            {"step": 5, "text": "Add the amaranth mixture and garnish with olives."}
        ],
        "notes": ["Soak amaranth overnight in water to reduce saponin content before cooking"],
        "tags": ["salad", "tabouli", "amaranth", "grain", "foraging", "eat the weeds"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    # ===== HAWTHORN RECIPES =====
    {
        "id": "hawthorn-jelly-no-cook-etw",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Hawthorn Jelly (No-Cook Method)",
        "category": "preserves",
        "attribution": "Eat the Weeds - Green Deane",
        "source_note": "Wild foraging recipe from eattheweeds.com",
        "description": "Simple no-cook jelly from single-seed hawthorn berries.",
        "ingredients": [
            {"item": "one-seed hawthorn berries", "quantity": "", "unit": "", "prep_note": "Crataegus monogyna"}
        ],
        "instructions": [
            {"step": 1, "text": "Crush berries thoroughly by hand in a bowl."},
            {"step": 2, "text": "Resulting liquid should be pudding-like consistency (add water if dry year)."},
            {"step": 3, "text": "Work quickly: squeeze seeds from berries."},
            {"step": 4, "text": "Filter thick slurry into bowl."},
            {"step": 5, "text": "In about five minutes, mixture will jell."},
            {"step": 6, "text": "Flip onto plate; eat as-is, slice, or sun-dry."}
        ],
        "notes": ["Keeps for many years when dried", "Do not eat the seeds - they contain cyanide bonded with sugar (amygdalin)"],
        "tags": ["jelly", "hawthorn", "haw", "no-cook", "preserves", "foraging", "eat the weeds"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "hawthorn-jelly-gibbons-etw",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Hawthorn Jelly (Euell Gibbons' Recipe)",
        "category": "preserves",
        "attribution": "Eat the Weeds - Green Deane (from Euell Gibbons)",
        "source_note": "Wild foraging recipe from eattheweeds.com",
        "description": "Traditional cooked hawthorn jelly from the famous forager.",
        "ingredients": [
            {"item": "hawthorn fruit", "quantity": "3", "unit": "lbs"},
            {"item": "water", "quantity": "4", "unit": "cups"},
            {"item": "powdered pectin", "quantity": "", "unit": "", "prep_note": "if berries very ripe"},
            {"item": "lemon juice", "quantity": "2", "unit": "lemons", "prep_note": "optional"},
            {"item": "sugar", "quantity": "7", "unit": "cups"}
        ],
        "instructions": [
            {"step": 1, "text": "Crush fruit, add water."},
            {"step": 2, "text": "Bring to boil, cover, simmer 10 minutes."},
            {"step": 3, "text": "Strain through jelly bag, discard pulp/seeds/skins."},
            {"step": 4, "text": "Add pectin and lemon juice if needed."},
            {"step": 5, "text": "Boil 4 cups juice, add sugar."},
            {"step": 6, "text": "Return to boil until perfect jelly test achieved."}
        ],
        "notes": ["Do not eat the seeds - they contain cyanide bonded with sugar (amygdalin)"],
        "tags": ["jelly", "hawthorn", "haw", "preserves", "foraging", "eat the weeds"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "hawthorn-schnapps-etw",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Hawthorn Schnapps",
        "category": "beverages",
        "attribution": "Eat the Weeds - Green Deane",
        "source_note": "Wild foraging recipe from eattheweeds.com",
        "description": "Hawthorn berry-infused vodka schnapps.",
        "ingredients": [
            {"item": "stalkless hawthorn berries", "quantity": "", "unit": "", "prep_note": "fill jar 2/3 full"},
            {"item": "clear unflavored vodka", "quantity": "", "unit": "", "prep_note": "to cover"}
        ],
        "instructions": [
            {"step": 1, "text": "Rinse and dry berries."},
            {"step": 2, "text": "Fill jar 2/3 full with berries."},
            {"step": 3, "text": "Cover completely with vodka."},
            {"step": 4, "text": "Seal tightly."},
            {"step": 5, "text": "Steep 5-6 weeks in dark place at 64-68°F, shaking occasionally."},
            {"step": 6, "text": "Strain and filter."},
            {"step": 7, "text": "Age 2 months in dark before serving."}
        ],
        "tags": ["schnapps", "hawthorn", "haw", "liqueur", "foraging", "eat the weeds"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "haw-sauce-etw",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Haw Sauce",
        "category": "sauces",
        "attribution": "Eat the Weeds - Green Deane",
        "source_note": "Wild foraging recipe from eattheweeds.com",
        "description": "Tangy condiment sauce made from hawthorn berries.",
        "ingredients": [
            {"item": "stalkless hawthorn berries", "quantity": "1.5", "unit": "lbs"},
            {"item": "vinegar", "quantity": "3/4", "unit": "pint"},
            {"item": "sugar", "quantity": "4", "unit": "oz"},
            {"item": "salt", "quantity": "1", "unit": "oz", "prep_note": "optional"},
            {"item": "freshly ground black pepper", "quantity": "1", "unit": "tsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Wash berries."},
            {"step": 2, "text": "Cook with vinegar for 30 minutes."},
            {"step": 3, "text": "Press pulp through sieve."},
            {"step": 4, "text": "Return to pan with sugar and seasonings."},
            {"step": 5, "text": "Boil 10 minutes."},
            {"step": 6, "text": "Bottle and seal."}
        ],
        "tags": ["sauce", "hawthorn", "haw", "condiment", "foraging", "eat the weeds"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "hawthorn-berry-soup-etw",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Hawthorn Berry Soup",
        "category": "soups",
        "attribution": "Eat the Weeds - Green Deane",
        "source_note": "Wild foraging recipe from eattheweeds.com",
        "description": "Sweet spiced soup from hawthorn berries.",
        "ingredients": [
            {"item": "stalkless hawthorn berries", "quantity": "1", "unit": "lb"},
            {"item": "water", "quantity": "1/2", "unit": "cup"},
            {"item": "sugar", "quantity": "1/2", "unit": "lb", "prep_note": "adjust to taste"},
            {"item": "cinnamon sticks", "quantity": "2", "unit": ""},
            {"item": "chili flakes or powder", "quantity": "", "unit": "pinch", "prep_note": "optional"}
        ],
        "instructions": [
            {"step": 1, "text": "Add berries to pot with water."},
            {"step": 2, "text": "Simmer gently 30 minutes, covered."},
            {"step": 3, "text": "Cool and pass through sieve (discard seeds)."},
            {"step": 4, "text": "Transfer to pan, add sugar, cinnamon, chili."},
            {"step": 5, "text": "Cook until sauce thickens."},
            {"step": 6, "text": "Serve."}
        ],
        "notes": ["Do not eat the seeds"],
        "tags": ["soup", "hawthorn", "haw", "sweet", "foraging", "eat the weeds"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "hawthorn-berry-catsup-etw",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Hawthorn Berry Catsup",
        "category": "sauces",
        "attribution": "Eat the Weeds - Green Deane",
        "source_note": "Wild foraging recipe from eattheweeds.com",
        "description": "Tangy ketchup-style condiment from hawthorn berries.",
        "ingredients": [
            {"item": "hawthorn berries", "quantity": "2", "unit": "cups"},
            {"item": "apple cider vinegar", "quantity": "1/4", "unit": "cup"},
            {"item": "water", "quantity": "1/4", "unit": "cup"},
            {"item": "sugar or honey", "quantity": "", "unit": "", "prep_note": "to taste"},
            {"item": "black cherry juice", "quantity": "1/3", "unit": "cup", "prep_note": "optional but recommended"},
            {"item": "sea salt", "quantity": "1/2", "unit": "tsp"},
            {"item": "black pepper or cayenne", "quantity": "", "unit": "", "prep_note": "to taste"}
        ],
        "instructions": [
            {"step": 1, "text": "Remove berries from stalks, rinse."},
            {"step": 2, "text": "Place in saucepan with vinegar and water."},
            {"step": 3, "text": "Simmer 25 minutes until skins split."},
            {"step": 4, "text": "Cool, push through sieve to remove pits."},
            {"step": 5, "text": "Return to pan, add sweeteners."},
            {"step": 6, "text": "Slowly heat, stir frequently, add spices."},
            {"step": 7, "text": "Low boil 5-10 minutes until syrupy."},
            {"step": 8, "text": "Add cherry juice gradually for consistency."},
            {"step": 9, "text": "Pour into sterilized bottles."},
            {"step": 10, "text": "Refrigerate, use within 3 months."}
        ],
        "tags": ["catsup", "ketchup", "hawthorn", "haw", "condiment", "foraging", "eat the weeds"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    # ===== LION'S MANE MUSHROOM =====
    {
        "id": "lions-mane-sauteed-butter-etw",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Sautéed Lion's Mane Mushroom",
        "category": "sides",
        "attribution": "Eat the Weeds - Green Deane",
        "source_note": "Wild foraging recipe from eattheweeds.com",
        "description": "Simple sautéed lion's mane mushroom with crab-like flavor.",
        "ingredients": [
            {"item": "lion's mane mushroom", "quantity": "", "unit": ""},
            {"item": "real butter", "quantity": "", "unit": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Clean mushroom and slice or tear into pieces."},
            {"step": 2, "text": "Sauté in real butter until golden and tender."},
            {"step": 3, "text": "Serve immediately."}
        ],
        "notes": ["Has a texture and flavor reminiscent of crab or lobster"],
        "tags": ["mushroom", "lions mane", "sauteed", "foraging", "eat the weeds"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    # ===== MAPLE RECIPE =====
    {
        "id": "maple-beer-etw",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Maple Beer",
        "category": "beverages",
        "attribution": "Eat the Weeds - Green Deane (from F.A. Michaux, 1853)",
        "source_note": "Wild foraging recipe from eattheweeds.com",
        "description": "Historical fermented maple beverage from 1853.",
        "servings_yield": "About 4 gallons",
        "ingredients": [
            {"item": "boiling water", "quantity": "4", "unit": "gallons"},
            {"item": "maple molasses (syrup)", "quantity": "1", "unit": "quart"},
            {"item": "yeast or leaven", "quantity": "", "unit": "", "prep_note": "for fermentation"},
            {"item": "essence of spruce", "quantity": "1", "unit": "spoonful"}
        ],
        "instructions": [
            {"step": 1, "text": "Pour the maple molasses into boiling water."},
            {"step": 2, "text": "Add yeast to trigger fermentation."},
            {"step": 3, "text": "Stir in the spruce essence."},
            {"step": 4, "text": "Allow to ferment until a pleasant and salutary drink is obtained."}
        ],
        "tags": ["beer", "maple", "fermented", "historical", "foraging", "eat the weeds"],
        "confidence": {"overall": "medium", "flags": ["Historical recipe - may need adjustment"]},
        "image_refs": []
    },
    # ===== REDBUD RECIPE =====
    {
        "id": "redbud-blossom-muffins-etw",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Redbud Blossom Muffins",
        "category": "breads",
        "attribution": "Eat the Weeds - Green Deane",
        "source_note": "Wild foraging recipe from eattheweeds.com",
        "description": "Delicate muffins made with foraged redbud blossoms.",
        "servings_yield": "12 muffins",
        "ingredients": [
            {"item": "redbud blossoms", "quantity": "2", "unit": "cups"},
            {"item": "fresh sage or rosemary", "quantity": "2", "unit": "tbsp", "prep_note": "minced"},
            {"item": "sugar", "quantity": "1/2", "unit": "cup"},
            {"item": "lemon zest", "quantity": "1", "unit": "", "prep_note": "minced"},
            {"item": "flour", "quantity": "1.5", "unit": "cups"},
            {"item": "baking powder", "quantity": "2", "unit": "tsp"},
            {"item": "baking soda", "quantity": "1/2", "unit": "tsp"},
            {"item": "salt", "quantity": "1/4", "unit": "tsp"},
            {"item": "egg", "quantity": "1", "unit": "large"},
            {"item": "milk", "quantity": "3/4", "unit": "cup"},
            {"item": "yogurt", "quantity": "1/2", "unit": "cup"},
            {"item": "melted butter or oil", "quantity": "2", "unit": "tbsp"},
            {"item": "lemon juice", "quantity": "1", "unit": "tbsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Preheat oven to 375°F."},
            {"step": 2, "text": "In bowl #1, combine redbuds, herb, sugar, and zest. Let sit 30 minutes."},
            {"step": 3, "text": "In bowl #2, sift flour, baking powder, baking soda, and salt."},
            {"step": 4, "text": "In bowl #3, combine egg, yogurt, milk, oil, and lemon juice."},
            {"step": 5, "text": "Pour bowl #1 contents into bowl #2 and toss."},
            {"step": 6, "text": "Add wet ingredients from bowl #3, stirring until just moistened (avoid overmixing)."},
            {"step": 7, "text": "Fill muffin tins 3/4 full."},
            {"step": 8, "text": "Combine 1 tbsp sugar and 1/2 tsp cinnamon; sprinkle on each muffin."},
            {"step": 9, "text": "Bake 25 minutes until tops spring back when lightly touched."},
            {"step": 10, "text": "Cool on wire rack."}
        ],
        "temperature": "375°F (190°C)",
        "notes": ["The light colored upper part of the blossom is sweet, the darker lower part is bitter"],
        "tags": ["muffins", "redbud", "flower", "foraging", "eat the weeds"],
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

    for recipe in ETW_BATCH2_RECIPES:
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
    print(f"  Added: {added} new Eat the Weeds recipes (batch 2)")
    print(f"  Skipped: {skipped} duplicates")
    print(f"  Total recipes now: {len(recipes)}")


if __name__ == "__main__":
    main()
