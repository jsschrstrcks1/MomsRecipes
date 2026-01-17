#!/usr/bin/env python3
"""
Supplemental Foxfire recipes from Books 2 & 3
Additional recipes found in deeper search including:
- Wild strawberry recipes (Foxfire 2)
- Mixed greens recipes (Foxfire 2)
- Appendix recipes (Foxfire 2)
- Persimmon recipes (Foxfire 3)
- Pawpaw recipes (Foxfire 3)
- Wild plum recipes (Foxfire 3)
- Nut recipes (Foxfire 3)
- Grape recipes (Foxfire 3)
- Elderflower/elderberry additional (Foxfire 3)
- Fig recipes (Foxfire 3)
- Apple/crabapple recipes (Foxfire 3)
- Mint recipes (Foxfire 3)
"""
import json
from pathlib import Path

DATA_DIR = Path(__file__).parent.parent / "data"
RECIPES_FILE = DATA_DIR / "recipes.json"

SUPPLEMENTAL_RECIPES = [
    # ==========================================
    # FOXFIRE 2 - WILD STRAWBERRY RECIPES
    # ==========================================
    {
        "id": "foxfire2-wild-strawberry-jam",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Wild Strawberry Jam",
        "category": "preserves",
        "attribution": "Foxfire 2",
        "source_note": "Traditional Appalachian recipe from Foxfire 2",
        "description": "Jam from tiny wild strawberries. As they say, 'If it is four o'clock by the time you get your clothes on, it will be light enough to pick strawberries.'",
        "servings_yield": "",
        "prep_time": "",
        "cook_time": "",
        "total_time": "",
        "ingredients": [
            {"item": "wild strawberries", "quantity": "1", "unit": "quart", "prep_note": ""},
            {"item": "sugar", "quantity": "3", "unit": "cups", "prep_note": "added 1 cup at a time"}
        ],
        "instructions": [
            {"step": 1, "text": "Put a quart of berries in a pot, add a cup of sugar, and bring to a boil, stirring gently."},
            {"step": 2, "text": "Boil three minutes, add another cup of sugar and boil three more minutes."},
            {"step": 3, "text": "Add a final cup of sugar, skim off foam and put in jars and seal."}
        ],
        "temperature": "",
        "pan_size": "",
        "notes": ["Wild strawberries are rich in iron and vitamin C"],
        "tags": ["jam", "strawberry", "wild", "preserves", "appalachian", "foxfire", "foraging"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": ["Foxfire-Book-2.txt"]
    },
    {
        "id": "foxfire2-wild-strawberry-preserves",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Wild Strawberry Preserves",
        "category": "preserves",
        "attribution": "Foxfire 2",
        "source_note": "Traditional Appalachian recipe from Foxfire 2",
        "description": "Old-fashioned strawberry preserves that rest overnight.",
        "servings_yield": "",
        "prep_time": "",
        "cook_time": "",
        "total_time": "Overnight",
        "ingredients": [
            {"item": "wild strawberries", "quantity": "1", "unit": "quart", "prep_note": ""},
            {"item": "sugar", "quantity": "1", "unit": "cup", "prep_note": ""},
            {"item": "water", "quantity": "3", "unit": "tbsp", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "To a quart of strawberries, add one cup of sugar and three tablespoons water."},
            {"step": 2, "text": "Boil slowly fifteen minutes. Let stand overnight."},
            {"step": 3, "text": "Next morning, bring to boiling point and pour in jars while hot."}
        ],
        "temperature": "",
        "pan_size": "",
        "notes": [],
        "tags": ["preserves", "strawberry", "wild", "appalachian", "foxfire", "foraging"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": ["Foxfire-Book-2.txt"]
    },
    {
        "id": "foxfire2-strawberry-leather",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Strawberry Leather",
        "category": "preserves",
        "attribution": "Foxfire 2",
        "source_note": "Traditional Appalachian fruit leather from Foxfire 2",
        "description": "Sun-dried strawberry leather, rolled up like a jelly cake.",
        "servings_yield": "",
        "prep_time": "",
        "cook_time": "",
        "total_time": "",
        "ingredients": [
            {"item": "ripe strawberries", "quantity": "", "unit": "", "prep_note": "mashed to pulp"},
            {"item": "sugar", "quantity": "", "unit": "for dusting", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Mash ripe berries to pulp."},
            {"step": 2, "text": "Spread on platters."},
            {"step": 3, "text": "When dry, dust with sugar and roll up like a jelly cake into pieces."},
            {"step": 4, "text": "Pack into clean jars."}
        ],
        "temperature": "",
        "pan_size": "Platters",
        "notes": ["A traditional method of preserving fruit before glass jars were available"],
        "tags": ["fruit-leather", "strawberry", "dried", "preserves", "appalachian", "foxfire"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": ["Foxfire-Book-2.txt"]
    },
    {
        "id": "foxfire2-strawberry-pie",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Wild Strawberry Pie",
        "category": "desserts",
        "attribution": "Foxfire 2",
        "source_note": "Traditional Appalachian recipe from Foxfire 2",
        "description": "Fresh strawberry pie with syrup topping.",
        "servings_yield": "1 pie",
        "prep_time": "",
        "cook_time": "15 minutes",
        "total_time": "",
        "ingredients": [
            {"item": "flour", "quantity": "3", "unit": "cups", "prep_note": ""},
            {"item": "lard", "quantity": "1", "unit": "cup", "prep_note": ""},
            {"item": "salt", "quantity": "1", "unit": "tsp", "prep_note": ""},
            {"item": "egg", "quantity": "1", "unit": "", "prep_note": ""},
            {"item": "cold water", "quantity": "5", "unit": "tbsp", "prep_note": ""},
            {"item": "vinegar", "quantity": "1", "unit": "tbsp", "prep_note": ""},
            {"item": "crushed strawberries", "quantity": "1", "unit": "cup", "prep_note": "for filling"},
            {"item": "sugar", "quantity": "1/2", "unit": "cup", "prep_note": ""},
            {"item": "cornstarch", "quantity": "2", "unit": "tbsp", "prep_note": ""},
            {"item": "water", "quantity": "1", "unit": "cup", "prep_note": ""},
            {"item": "fresh strawberries", "quantity": "", "unit": "for filling", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Sift flour, mix with lard, salt, cold water, and vinegar. Mix well and roll out dough."},
            {"step": 2, "text": "Put in greased pie pan. Bake fifteen minutes."},
            {"step": 3, "text": "Make filling of one cup crushed strawberries, one-half cup sugar, two tablespoons cornstarch, and one cup water. Cook into a syrup."},
            {"step": 4, "text": "Fill pie crust with fresh strawberries, pour syrup over top and serve."}
        ],
        "temperature": "400°F (205°C)",
        "pan_size": "Pie pan",
        "notes": [],
        "tags": ["pie", "strawberry", "wild", "dessert", "appalachian", "foxfire"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": ["Foxfire-Book-2.txt"]
    },
    {
        "id": "foxfire2-strawberry-mallow",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Strawberry Mallow",
        "category": "desserts",
        "attribution": "Foxfire 2",
        "source_note": "Traditional Appalachian dessert from Foxfire 2",
        "description": "A chilled strawberry and marshmallow dessert.",
        "servings_yield": "",
        "prep_time": "",
        "cook_time": "",
        "total_time": "",
        "ingredients": [
            {"item": "wild strawberries", "quantity": "2", "unit": "cups", "prep_note": ""},
            {"item": "sugar", "quantity": "1/2", "unit": "cup", "prep_note": ""},
            {"item": "salt", "quantity": "", "unit": "few grains", "prep_note": ""},
            {"item": "marshmallows", "quantity": "1/2", "unit": "lb", "prep_note": "cut up"},
            {"item": "cream", "quantity": "1", "unit": "cup", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Mix together strawberries, sugar, salt, marshmallows, and cream."},
            {"step": 2, "text": "Chill."},
            {"step": 3, "text": "Top with whole berries."}
        ],
        "temperature": "",
        "pan_size": "",
        "notes": [],
        "tags": ["dessert", "strawberry", "marshmallow", "no-bake", "appalachian", "foxfire"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": ["Foxfire-Book-2.txt"]
    },
    # ==========================================
    # FOXFIRE 2 - MIXED GREENS RECIPES
    # ==========================================
    {
        "id": "foxfire2-mixed-wild-greens",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Mixed Wild Greens",
        "category": "sides",
        "attribution": "Foxfire 2",
        "source_note": "Traditional Appalachian recipe from Foxfire 2",
        "description": "A 'mess' of mixed wild greens with salt pork and vinegar.",
        "servings_yield": "",
        "prep_time": "",
        "cook_time": "",
        "total_time": "",
        "ingredients": [
            {"item": "poke", "quantity": "", "unit": "", "prep_note": "young shoots"},
            {"item": "dandelion", "quantity": "", "unit": "", "prep_note": ""},
            {"item": "lamb's quarters", "quantity": "", "unit": "", "prep_note": ""},
            {"item": "violet leaves", "quantity": "", "unit": "", "prep_note": ""},
            {"item": "sour dock", "quantity": "", "unit": "", "prep_note": ""},
            {"item": "salt pork", "quantity": "", "unit": "", "prep_note": "fried bits"},
            {"item": "vinegar", "quantity": "", "unit": "a little", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Get together a mess of poke, dandelion, lamb's quarters, violet leaves, and sour dock."},
            {"step": 2, "text": "Mix together and cook."},
            {"step": 3, "text": "Drain and season with bits of fried salt pork, and a little vinegar."}
        ],
        "temperature": "",
        "pan_size": "",
        "notes": ["Any mild-flavored green can be combined with sharper mustards and cresses"],
        "tags": ["greens", "mixed", "wild-plants", "spring", "appalachian", "foxfire", "foraging"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": ["Foxfire-Book-2.txt"]
    },
    {
        "id": "foxfire2-mixed-green-salad",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Mixed Wild Green Salad",
        "category": "salads",
        "attribution": "Foxfire 2",
        "source_note": "Traditional Appalachian salad from Foxfire 2",
        "description": "A raw salad of wild spring greens with garlic dressing.",
        "servings_yield": "",
        "prep_time": "",
        "cook_time": "",
        "total_time": "",
        "ingredients": [
            {"item": "dandelion", "quantity": "", "unit": "equal parts", "prep_note": ""},
            {"item": "shepherd's purse", "quantity": "", "unit": "equal parts", "prep_note": ""},
            {"item": "peppergrass", "quantity": "", "unit": "equal parts", "prep_note": ""},
            {"item": "curly dock", "quantity": "", "unit": "equal parts", "prep_note": ""},
            {"item": "poke shoots", "quantity": "", "unit": "equal parts", "prep_note": "must be cooked first"},
            {"item": "sorrel", "quantity": "", "unit": "equal parts", "prep_note": ""},
            {"item": "wild onion", "quantity": "", "unit": "to taste", "prep_note": ""},
            {"item": "oil", "quantity": "", "unit": "for dressing", "prep_note": ""},
            {"item": "vinegar", "quantity": "", "unit": "for dressing", "prep_note": ""},
            {"item": "garlic", "quantity": "", "unit": "for dressing", "prep_note": ""},
            {"item": "mustard", "quantity": "", "unit": "for dressing", "prep_note": ""},
            {"item": "salt and pepper", "quantity": "", "unit": "to taste", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Take equal parts of dandelion, shepherd's purse, peppergrass, curly dock, poke shoots (must be cooked first), and sorrel. Chop fine."},
            {"step": 2, "text": "Add wild onion to taste."},
            {"step": 3, "text": "Make a dressing of oil and vinegar, and flavor with garlic, mustard, salt, and pepper."},
            {"step": 4, "text": "Serve on a bed of wild dock or lettuce leaves."}
        ],
        "temperature": "",
        "pan_size": "",
        "notes": ["Poke shoots MUST be cooked before adding to raw salad"],
        "tags": ["salad", "greens", "wild-plants", "raw", "appalachian", "foxfire", "foraging"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": ["Foxfire-Book-2.txt"]
    },
    {
        "id": "foxfire2-canned-wild-greens",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Canned Wild Greens",
        "category": "preserves",
        "attribution": "Foxfire 2",
        "source_note": "Traditional Appalachian canning method from Foxfire 2",
        "description": "How to can wild greens for winter use.",
        "servings_yield": "",
        "prep_time": "",
        "cook_time": "30 minutes in pressure cooker",
        "total_time": "",
        "ingredients": [
            {"item": "mustard greens", "quantity": "", "unit": "", "prep_note": "wild"},
            {"item": "wild turnip greens", "quantity": "", "unit": "", "prep_note": ""},
            {"item": "buff sallet", "quantity": "", "unit": "optional", "prep_note": ""},
            {"item": "creases", "quantity": "", "unit": "optional", "prep_note": ""},
            {"item": "water", "quantity": "", "unit": "", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Mix mustard and wild turnip greens, or buff sallet and mustard mixed, or with creases."},
            {"step": 2, "text": "Fix and precook until tender."},
            {"step": 3, "text": "Put in jars, add water, seal."},
            {"step": 4, "text": "Cook thirty minutes in pressure cooker."}
        ],
        "temperature": "",
        "pan_size": "Canning jars",
        "notes": ["Most wild sallets can be canned this way"],
        "tags": ["canning", "greens", "wild-plants", "preserves", "appalachian", "foxfire"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": ["Foxfire-Book-2.txt"]
    },
    {
        "id": "foxfire2-wilted-greens-bacon",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Wilted Greens with Hot Bacon Dressing",
        "category": "salads",
        "attribution": "Foxfire 2",
        "source_note": "Traditional Appalachian recipe from Foxfire 2",
        "description": "Wild greens wilted with hot bacon and vinegar dressing.",
        "servings_yield": "",
        "prep_time": "",
        "cook_time": "",
        "total_time": "",
        "ingredients": [
            {"item": "bacon", "quantity": "3", "unit": "slices", "prep_note": "cut fine"},
            {"item": "vinegar", "quantity": "3", "unit": "tbsp", "prep_note": ""},
            {"item": "salt", "quantity": "", "unit": "dash", "prep_note": ""},
            {"item": "cress", "quantity": "1", "unit": "cup", "prep_note": "chopped"},
            {"item": "dandelions", "quantity": "1", "unit": "cup", "prep_note": ""},
            {"item": "wild lettuce", "quantity": "1", "unit": "cup", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Fry bacon until crisp."},
            {"step": 2, "text": "Add vinegar and salt to the hot bacon grease."},
            {"step": 3, "text": "Pour over the greens and toss."}
        ],
        "temperature": "",
        "pan_size": "",
        "notes": [],
        "tags": ["salad", "wilted", "bacon", "greens", "appalachian", "foxfire"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": ["Foxfire-Book-2.txt"]
    },
    # ==========================================
    # FOXFIRE 3 - PERSIMMON RECIPES
    # ==========================================
    {
        "id": "foxfire3-persimmon-bread",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Persimmon Bread",
        "category": "breads",
        "attribution": "Foxfire 3",
        "source_note": "Traditional Appalachian recipe from Foxfire 3",
        "description": "Cornmeal bread with ripe persimmons.",
        "servings_yield": "",
        "prep_time": "",
        "cook_time": "",
        "total_time": "",
        "ingredients": [
            {"item": "cornmeal", "quantity": "1", "unit": "cup", "prep_note": ""},
            {"item": "flour", "quantity": "1", "unit": "cup", "prep_note": ""},
            {"item": "persimmons", "quantity": "1", "unit": "cup", "prep_note": "crushed, seeds removed"},
            {"item": "baking soda", "quantity": "1", "unit": "spoonful", "prep_note": ""},
            {"item": "salt", "quantity": "", "unit": "dash", "prep_note": ""},
            {"item": "buttermilk", "quantity": "1/2", "unit": "cup", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Mix everything together."},
            {"step": 2, "text": "Add water if mixture is not thin enough."},
            {"step": 3, "text": "Bake like cornbread."}
        ],
        "temperature": "400°F (205°C)",
        "pan_size": "",
        "notes": ["To be good, a raw persimmon must be soft and squishy to the touch"],
        "tags": ["bread", "persimmon", "cornmeal", "appalachian", "foxfire", "foraging"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": ["foxfire-three.txt"]
    },
    {
        "id": "foxfire3-persimmon-beer",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Persimmon Beer",
        "category": "beverages",
        "attribution": "Foxfire 3",
        "source_note": "Traditional Appalachian fermented drink from Foxfire 3",
        "description": "A potent fermented drink made from persimmons and honey locust pods.",
        "servings_yield": "",
        "prep_time": "",
        "cook_time": "",
        "total_time": "At least 1 week",
        "ingredients": [
            {"item": "persimmons", "quantity": "", "unit": "", "prep_note": "washed"},
            {"item": "honey locust seed pods", "quantity": "", "unit": "good number", "prep_note": "washed"},
            {"item": "boiling water", "quantity": "", "unit": "to cover", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Gather persimmons and a good number of honey locust seed pods. Wash them both well."},
            {"step": 2, "text": "Place them in a large crock in layers until the crock is full."},
            {"step": 3, "text": "Pour enough boiling water in to cover them."},
            {"step": 4, "text": "Cover the churn and let it sit at least a week."},
            {"step": 5, "text": "Pour off or dip out the beer as desired."},
            {"step": 6, "text": "When drained, the churn may be filled with boiling water again to make a second batch."}
        ],
        "temperature": "",
        "pan_size": "Large crock or churn",
        "notes": ["The beer is supposed to be very potent"],
        "tags": ["beer", "persimmon", "fermented", "beverage", "appalachian", "foxfire"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": ["foxfire-three.txt"]
    },
    {
        "id": "foxfire3-persimmon-pudding",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Persimmon Pudding",
        "category": "desserts",
        "attribution": "Foxfire 3",
        "source_note": "Traditional Appalachian recipe from Foxfire 3",
        "description": "A rich baked persimmon pudding.",
        "servings_yield": "",
        "prep_time": "",
        "cook_time": "1 hour",
        "total_time": "",
        "ingredients": [
            {"item": "persimmon pulp", "quantity": "1 1/2", "unit": "cups", "prep_note": "strained through colander"},
            {"item": "sugar", "quantity": "1 1/2", "unit": "cups", "prep_note": ""},
            {"item": "salt", "quantity": "1/2", "unit": "tsp", "prep_note": ""},
            {"item": "buttermilk", "quantity": "1 1/2", "unit": "cups", "prep_note": ""},
            {"item": "flour", "quantity": "1 1/4", "unit": "cups", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Strain persimmons through a colander."},
            {"step": 2, "text": "Stir all ingredients together."},
            {"step": 3, "text": "Put in greased pan."},
            {"step": 4, "text": "Bake one hour at low heat."}
        ],
        "temperature": "325°F (165°C)",
        "pan_size": "Greased baking pan",
        "notes": ["Persimmons are very high in food energy"],
        "tags": ["pudding", "persimmon", "dessert", "baked", "appalachian", "foxfire"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": ["foxfire-three.txt"]
    },
    {
        "id": "foxfire3-persimmon-pie",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Persimmon Pie",
        "category": "desserts",
        "attribution": "Foxfire 3",
        "source_note": "Traditional Appalachian recipe from Foxfire 3",
        "description": "A spiced persimmon custard pie with meringue topping.",
        "servings_yield": "1 nine-inch pie",
        "prep_time": "",
        "cook_time": "",
        "total_time": "",
        "ingredients": [
            {"item": "persimmon pulp", "quantity": "1", "unit": "cup", "prep_note": "peeled and crushed smooth"},
            {"item": "sugar", "quantity": "2", "unit": "cups", "prep_note": ""},
            {"item": "milk", "quantity": "1", "unit": "cup", "prep_note": ""},
            {"item": "flour or cornstarch", "quantity": "1", "unit": "tbsp", "prep_note": ""},
            {"item": "eggs", "quantity": "3", "unit": "", "prep_note": "separated"},
            {"item": "nutmeg", "quantity": "1", "unit": "tsp", "prep_note": ""},
            {"item": "salt", "quantity": "1/2", "unit": "tsp", "prep_note": ""},
            {"item": "pie shell", "quantity": "1", "unit": "nine-inch", "prep_note": "unbaked"}
        ],
        "instructions": [
            {"step": 1, "text": "Peel and crush persimmons until smooth."},
            {"step": 2, "text": "Add sugar and beat. Add three egg yolks and one egg white."},
            {"step": 3, "text": "Add milk, nutmeg, and salt. Beat until smooth."},
            {"step": 4, "text": "Pour into nine-inch pie shell and bake until done."},
            {"step": 5, "text": "Make meringue by beating whites of remaining eggs until stiff. Add four tablespoons sugar."},
            {"step": 6, "text": "Put on top of pie and brown in moderate oven."}
        ],
        "temperature": "350°F (175°C)",
        "pan_size": "9-inch pie pan",
        "notes": [],
        "tags": ["pie", "persimmon", "meringue", "dessert", "appalachian", "foxfire"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": ["foxfire-three.txt"]
    },
    {
        "id": "foxfire3-persimmon-nut-bread",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Persimmon-Nut Bread",
        "category": "breads",
        "attribution": "Foxfire 3",
        "source_note": "Traditional Appalachian recipe from Foxfire 3",
        "description": "A sweet quick bread with persimmons and hickory nuts or black walnuts.",
        "servings_yield": "1 loaf",
        "prep_time": "",
        "cook_time": "1 hour",
        "total_time": "",
        "ingredients": [
            {"item": "shortening", "quantity": "1/3", "unit": "cup", "prep_note": ""},
            {"item": "sugar", "quantity": "1/2", "unit": "cup", "prep_note": ""},
            {"item": "eggs", "quantity": "2", "unit": "", "prep_note": ""},
            {"item": "flour", "quantity": "1 3/4", "unit": "cups", "prep_note": ""},
            {"item": "baking powder", "quantity": "2", "unit": "tsp", "prep_note": ""},
            {"item": "salt", "quantity": "1/2", "unit": "tsp", "prep_note": ""},
            {"item": "baking soda", "quantity": "1/4", "unit": "tsp", "prep_note": ""},
            {"item": "mashed persimmons", "quantity": "1", "unit": "cup", "prep_note": ""},
            {"item": "hickory-nut or black-walnut meats", "quantity": "1/2", "unit": "cup", "prep_note": "chopped"}
        ],
        "instructions": [
            {"step": 1, "text": "Cream shortening, add sugar and eggs; beat well."},
            {"step": 2, "text": "Sift dry ingredients, add to creamed mixture alternately with persimmons and nuts."},
            {"step": 3, "text": "Pour in greased loaf pan and bake at 350° for one hour."}
        ],
        "temperature": "350°F (175°C)",
        "pan_size": "Loaf pan",
        "notes": [],
        "tags": ["bread", "persimmon", "nuts", "quick-bread", "appalachian", "foxfire"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": ["foxfire-three.txt"]
    },
    {
        "id": "foxfire3-candied-persimmons",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Candied Persimmons",
        "category": "preserves",
        "attribution": "Foxfire 3",
        "source_note": "Traditional Appalachian recipe from Foxfire 3",
        "description": "Persimmons preserved with sugar until candied.",
        "servings_yield": "",
        "prep_time": "",
        "cook_time": "",
        "total_time": "",
        "ingredients": [
            {"item": "persimmons", "quantity": "", "unit": "", "prep_note": ""},
            {"item": "sugar", "quantity": "", "unit": "for layering", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Pack persimmons in jars, alternating with layers of sugar."},
            {"step": 2, "text": "Put on lids and store in a cool place until they become candied."}
        ],
        "temperature": "",
        "pan_size": "Jars",
        "notes": [],
        "tags": ["candied", "persimmon", "preserved", "appalachian", "foxfire"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": ["foxfire-three.txt"]
    },
    {
        "id": "foxfire3-persimmon-butter",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Persimmon Butter",
        "category": "preserves",
        "attribution": "Foxfire 3",
        "source_note": "Traditional Appalachian fruit butter from Foxfire 3",
        "description": "A spiced persimmon spread like apple butter.",
        "servings_yield": "",
        "prep_time": "",
        "cook_time": "",
        "total_time": "",
        "ingredients": [
            {"item": "persimmons", "quantity": "", "unit": "", "prep_note": "cooked and strained"},
            {"item": "baking soda", "quantity": "1/2", "unit": "tsp", "prep_note": "per cup pulp"},
            {"item": "sugar", "quantity": "", "unit": "to taste", "prep_note": ""},
            {"item": "spices or orange rind", "quantity": "", "unit": "for flavoring", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Cook and strain persimmons."},
            {"step": 2, "text": "Add 1/2 teaspoon soda to each cup pulp."},
            {"step": 3, "text": "Sweeten and flavor with spices or orange rind."},
            {"step": 4, "text": "Cook thoroughly and bottle."}
        ],
        "temperature": "",
        "pan_size": "",
        "notes": [],
        "tags": ["butter", "persimmon", "spread", "preserves", "appalachian", "foxfire"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": ["foxfire-three.txt"]
    },
    # ==========================================
    # FOXFIRE 3 - PAWPAW RECIPES
    # ==========================================
    {
        "id": "foxfire3-pawpaw-pie",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Pawpaw Pie",
        "category": "desserts",
        "attribution": "Foxfire 3",
        "source_note": "Traditional Appalachian recipe from Foxfire 3",
        "description": "A custard pie made from pawpaws, which taste 'somewheres between a banana and a persimmon.'",
        "servings_yield": "1 pie",
        "prep_time": "",
        "cook_time": "",
        "total_time": "",
        "ingredients": [
            {"item": "sugar", "quantity": "1", "unit": "cup", "prep_note": ""},
            {"item": "milk", "quantity": "1", "unit": "cup", "prep_note": ""},
            {"item": "egg", "quantity": "1", "unit": "", "prep_note": ""},
            {"item": "salt", "quantity": "1/4", "unit": "tsp", "prep_note": ""},
            {"item": "pawpaws", "quantity": "1 1/2", "unit": "cups", "prep_note": "peeled and seeded"},
            {"item": "pie shell", "quantity": "1", "unit": "", "prep_note": "unbaked"}
        ],
        "instructions": [
            {"step": 1, "text": "Place sugar, milk, egg, salt, and pawpaws in a stew pan and stir together."},
            {"step": 2, "text": "Cook until thickened."},
            {"step": 3, "text": "Pour in an unbaked pie shell and bake until done."}
        ],
        "temperature": "350°F (175°C)",
        "pan_size": "Pie pan",
        "notes": ["Pawpaws ripen in late autumn and taste like a cross between banana and persimmon"],
        "tags": ["pie", "pawpaw", "custard", "dessert", "appalachian", "foxfire", "foraging"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": ["foxfire-three.txt"]
    },
    {
        "id": "foxfire3-pawpaw-bread",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Pawpaw Bread",
        "category": "breads",
        "attribution": "Foxfire 3",
        "source_note": "Traditional Appalachian recipe from Foxfire 3",
        "description": "Nut bread with pawpaw pulp that gives it a lovely rose-red color.",
        "servings_yield": "",
        "prep_time": "",
        "cook_time": "",
        "total_time": "",
        "ingredients": [
            {"item": "pawpaw pulp", "quantity": "", "unit": "", "prep_note": ""},
            {"item": "nut bread ingredients", "quantity": "", "unit": "", "prep_note": "your favorite recipe"}
        ],
        "instructions": [
            {"step": 1, "text": "Add pawpaw pulp to your favorite nut bread recipe."},
            {"step": 2, "text": "Bake as directed. It gives bread a lovely rose-red color."}
        ],
        "temperature": "",
        "pan_size": "",
        "notes": [],
        "tags": ["bread", "pawpaw", "quick-bread", "appalachian", "foxfire"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": ["foxfire-three.txt"]
    },
    # ==========================================
    # FOXFIRE 3 - WILD PLUM RECIPES
    # ==========================================
    {
        "id": "foxfire3-wild-plum-catsup",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Wild Plum Catsup",
        "category": "sauces",
        "attribution": "Foxfire 3",
        "source_note": "Traditional Appalachian condiment from Foxfire 3",
        "description": "A spiced plum catsup for meats.",
        "servings_yield": "",
        "prep_time": "",
        "cook_time": "",
        "total_time": "",
        "ingredients": [
            {"item": "wild plums", "quantity": "5", "unit": "quarts", "prep_note": ""},
            {"item": "sugar", "quantity": "4", "unit": "lb", "prep_note": ""},
            {"item": "vinegar", "quantity": "1", "unit": "pint", "prep_note": ""},
            {"item": "water", "quantity": "1", "unit": "pint", "prep_note": ""},
            {"item": "cinnamon", "quantity": "1 1/2", "unit": "tsp", "prep_note": ""},
            {"item": "allspice", "quantity": "1", "unit": "tbsp", "prep_note": ""},
            {"item": "cloves", "quantity": "1", "unit": "tbsp", "prep_note": ""},
            {"item": "baking soda", "quantity": "1", "unit": "tsp", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Boil plums with one teaspoon soda. Bring to a rolling boil."},
            {"step": 2, "text": "Strain through a colander."},
            {"step": 3, "text": "Simmer with sugar, vinegar, and spices until thick as catsup."}
        ],
        "temperature": "",
        "pan_size": "",
        "notes": ["Chickasaw plums have the best-tasting fruit"],
        "tags": ["catsup", "plum", "condiment", "spiced", "appalachian", "foxfire"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": ["foxfire-three.txt"]
    },
    {
        "id": "foxfire3-plum-cobbler",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Wild Plum Cobbler",
        "category": "desserts",
        "attribution": "Foxfire 3",
        "source_note": "Traditional Appalachian recipe from Foxfire 3",
        "description": "A layered plum cobbler with strips of biscuit dough.",
        "servings_yield": "",
        "prep_time": "",
        "cook_time": "",
        "total_time": "",
        "ingredients": [
            {"item": "wild plums", "quantity": "1", "unit": "quart", "prep_note": "cooked and pitted"},
            {"item": "biscuit dough", "quantity": "", "unit": "", "prep_note": "rolled thin, cut in strips"},
            {"item": "sugar", "quantity": "", "unit": "for topping", "prep_note": ""},
            {"item": "butter", "quantity": "", "unit": "for dotting", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Cook and pit one quart plums."},
            {"step": 2, "text": "Roll biscuit dough thin and cut in strips."},
            {"step": 3, "text": "Grease a pan well and add a layer of plums and strips of dough, topping with sugar and dabs of butter."},
            {"step": 4, "text": "Repeat until pan is almost full."},
            {"step": 5, "text": "Bake in medium oven."}
        ],
        "temperature": "375°F (190°C)",
        "pan_size": "Greased baking pan",
        "notes": [],
        "tags": ["cobbler", "plum", "wild", "dessert", "appalachian", "foxfire"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": ["foxfire-three.txt"]
    },
    {
        "id": "foxfire3-plum-pudding",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Wild Plum Pudding",
        "category": "desserts",
        "attribution": "Foxfire 3",
        "source_note": "Traditional Appalachian recipe from Foxfire 3",
        "description": "A baked plum pudding with cake-like topping.",
        "servings_yield": "",
        "prep_time": "",
        "cook_time": "1 hour",
        "total_time": "",
        "ingredients": [
            {"item": "wild plums", "quantity": "", "unit": "", "prep_note": "pitted, cooked, sweetened, 2 inches deep"},
            {"item": "sugar", "quantity": "1", "unit": "cup", "prep_note": ""},
            {"item": "butter", "quantity": "4", "unit": "tbsp", "prep_note": ""},
            {"item": "egg", "quantity": "1", "unit": "", "prep_note": ""},
            {"item": "milk", "quantity": "1", "unit": "scant cup", "prep_note": ""},
            {"item": "all-purpose flour", "quantity": "2", "unit": "cups", "prep_note": ""},
            {"item": "baking powder", "quantity": "2", "unit": "tsp", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Put pitted, cooked, sweetened plums two inches deep in bottom of a baking dish."},
            {"step": 2, "text": "Beat one cup sugar, four tablespoons butter, and one egg to a cream."},
            {"step": 3, "text": "Add one scant cup of milk, two cups all-purpose flour, and two teaspoons baking powder."},
            {"step": 4, "text": "Mix well, and pour over plums."},
            {"step": 5, "text": "Bake one hour at 350°."}
        ],
        "temperature": "350°F (175°C)",
        "pan_size": "Baking dish",
        "notes": [],
        "tags": ["pudding", "plum", "wild", "dessert", "appalachian", "foxfire"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": ["foxfire-three.txt"]
    },
    {
        "id": "foxfire3-wild-plum-conserve",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Wild Plum Conserve",
        "category": "preserves",
        "attribution": "Foxfire 3",
        "source_note": "Traditional Appalachian recipe from Foxfire 3",
        "description": "A rich conserve with plums, oranges, and raisins.",
        "servings_yield": "",
        "prep_time": "",
        "cook_time": "",
        "total_time": "",
        "ingredients": [
            {"item": "wild plums", "quantity": "7", "unit": "lb", "prep_note": ""},
            {"item": "sugar", "quantity": "5", "unit": "lb", "prep_note": ""},
            {"item": "seeded raisins", "quantity": "2", "unit": "lb", "prep_note": "ground"},
            {"item": "oranges", "quantity": "3", "unit": "", "prep_note": "sliced thin with rind"}
        ],
        "instructions": [
            {"step": 1, "text": "Wash and pick over plums. Cover with boiling water, and add 1/2 teaspoon soda."},
            {"step": 2, "text": "Bring to rolling boil. Pour off the soda water, rinse plums, and strain through a colander."},
            {"step": 3, "text": "Slice oranges in thin slices, rind and all, removing seeds, and grind the raisins."},
            {"step": 4, "text": "Combine fruit and sugar, adding enough water to keep them from sticking."},
            {"step": 5, "text": "Simmer until thick and clear."}
        ],
        "temperature": "",
        "pan_size": "",
        "notes": [],
        "tags": ["conserve", "plum", "preserves", "oranges", "appalachian", "foxfire"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": ["foxfire-three.txt"]
    },
    {
        "id": "foxfire3-plum-jelly",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Wild Plum Jelly",
        "category": "preserves",
        "attribution": "Foxfire 3",
        "source_note": "Traditional Appalachian recipe from Foxfire 3",
        "description": "Classic wild plum jelly.",
        "servings_yield": "",
        "prep_time": "",
        "cook_time": "20-30 minutes",
        "total_time": "",
        "ingredients": [
            {"item": "half-ripe plums", "quantity": "1/2", "unit": "gallon", "prep_note": ""},
            {"item": "water", "quantity": "", "unit": "to cover", "prep_note": ""},
            {"item": "sugar", "quantity": "1", "unit": "lb", "prep_note": "per pint juice"}
        ],
        "instructions": [
            {"step": 1, "text": "Cover 1/2 gallon half-ripe plums with water in a porcelain kettle."},
            {"step": 2, "text": "Boil ten minutes."},
            {"step": 3, "text": "Pour off the juice and strain through flannel."},
            {"step": 4, "text": "Add one pound sugar to each pint juice."},
            {"step": 5, "text": "Boil until it will harden when cold (about twenty to thirty minutes)."}
        ],
        "temperature": "",
        "pan_size": "Porcelain kettle",
        "notes": ["Use half-ripe plums for best jelling"],
        "tags": ["jelly", "plum", "wild", "preserves", "appalachian", "foxfire"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": ["foxfire-three.txt"]
    },
    # ==========================================
    # FOXFIRE 3 - NUT RECIPES
    # ==========================================
    {
        "id": "foxfire3-sugared-nut-meats",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Sugared Nut Meats",
        "category": "desserts",
        "attribution": "Foxfire 3",
        "source_note": "Traditional Appalachian recipe from Foxfire 3",
        "description": "Spiced candied nuts with rum flavoring.",
        "servings_yield": "",
        "prep_time": "",
        "cook_time": "10 minutes",
        "total_time": "",
        "ingredients": [
            {"item": "vegetable oil", "quantity": "1/4", "unit": "cup", "prep_note": ""},
            {"item": "powdered sugar", "quantity": "2", "unit": "cups", "prep_note": ""},
            {"item": "rum flavor", "quantity": "2", "unit": "tsp", "prep_note": ""},
            {"item": "cinnamon", "quantity": "", "unit": "dash", "prep_note": ""},
            {"item": "nutmeg", "quantity": "", "unit": "dash", "prep_note": ""},
            {"item": "ginger", "quantity": "", "unit": "dash", "prep_note": ""},
            {"item": "shelled nuts", "quantity": "1 1/2", "unit": "cups", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Cream oil, sugar, flavoring and spices."},
            {"step": 2, "text": "Spread nuts on cookie sheet, heat in moderate oven ten minutes."},
            {"step": 3, "text": "Turn hot nuts into the cream mixture and stir."},
            {"step": 4, "text": "Separate and spread on a cookie sheet to cool."}
        ],
        "temperature": "350°F (175°C)",
        "pan_size": "Cookie sheet",
        "notes": ["Can use walnuts, hickory nuts, or hazelnuts"],
        "tags": ["candy", "nuts", "spiced", "dessert", "appalachian", "foxfire"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": ["foxfire-three.txt"]
    },
    {
        "id": "foxfire3-nut-brittle-squares",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Nut Brittle Squares",
        "category": "desserts",
        "attribution": "Foxfire 3",
        "source_note": "Traditional Appalachian candy from Foxfire 3",
        "description": "Caramelized sugar poured over nuts for a simple brittle.",
        "servings_yield": "",
        "prep_time": "",
        "cook_time": "",
        "total_time": "",
        "ingredients": [
            {"item": "butter", "quantity": "", "unit": "for pan", "prep_note": ""},
            {"item": "nuts", "quantity": "1", "unit": "cup", "prep_note": "finely chopped"},
            {"item": "sugar", "quantity": "1", "unit": "cup", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Butter the outside bottom of an eight-inch-square pan."},
            {"step": 2, "text": "Spread evenly with one cup finely chopped nuts."},
            {"step": 3, "text": "Set pan, nut side up, on a tray."},
            {"step": 4, "text": "Put one cup sugar in skillet and heat, stirring until golden brown and syrupy."},
            {"step": 5, "text": "Pour over nuts at once."},
            {"step": 6, "text": "When slightly cooled, remove in one piece to a board and cut into two-inch squares."}
        ],
        "temperature": "",
        "pan_size": "8-inch square pan",
        "notes": ["Works with walnuts, hickory nuts, or hazelnuts"],
        "tags": ["brittle", "candy", "nuts", "dessert", "appalachian", "foxfire"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": ["foxfire-three.txt"]
    },
    {
        "id": "foxfire3-chestnut-croquettes",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Chestnut Croquettes",
        "category": "desserts",
        "attribution": "Foxfire 3",
        "source_note": "Traditional Appalachian recipe from Foxfire 3",
        "description": "Sweet fried chestnut balls.",
        "servings_yield": "",
        "prep_time": "",
        "cook_time": "",
        "total_time": "",
        "ingredients": [
            {"item": "chestnuts", "quantity": "1", "unit": "cup", "prep_note": "mashed, boiled"},
            {"item": "vanilla", "quantity": "1/4", "unit": "tsp", "prep_note": ""},
            {"item": "egg yolks", "quantity": "2", "unit": "", "prep_note": "beaten"},
            {"item": "cream", "quantity": "2", "unit": "tbsp", "prep_note": ""},
            {"item": "sugar", "quantity": "1", "unit": "tsp", "prep_note": ""},
            {"item": "crumbs", "quantity": "", "unit": "for rolling", "prep_note": ""},
            {"item": "fat", "quantity": "", "unit": "for deep frying", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Mix one cup mashed, boiled chestnuts with 1/4 teaspoon vanilla, two beaten egg yolks, two tablespoons cream, one teaspoon sugar."},
            {"step": 2, "text": "Shape in balls, roll in crumbs."},
            {"step": 3, "text": "Fry in deep fat."}
        ],
        "temperature": "",
        "pan_size": "",
        "notes": ["American chestnuts are now rare due to blight but still occasionally found"],
        "tags": ["croquettes", "chestnut", "fried", "dessert", "appalachian", "foxfire"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": ["foxfire-three.txt"]
    },
    {
        "id": "foxfire3-acorn-coffee",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Acorn Coffee",
        "category": "beverages",
        "attribution": "Foxfire 3",
        "source_note": "Traditional Appalachian recipe from Foxfire 3",
        "description": "A coffee substitute made from roasted acorns. 'Real good, just as good as bought coffee.'",
        "servings_yield": "",
        "prep_time": "",
        "cook_time": "",
        "total_time": "",
        "ingredients": [
            {"item": "white oak acorns", "quantity": "", "unit": "", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Parch acorns until thoroughly dry but not burned."},
            {"step": 2, "text": "Grind into powder."},
            {"step": 3, "text": "Brew like coffee. It makes a red coffee."}
        ],
        "temperature": "",
        "pan_size": "",
        "notes": ["White oak acorns are sweetest; also use chestnut oak or yellow chestnut oak"],
        "tags": ["coffee", "acorn", "beverage", "substitute", "appalachian", "foxfire", "foraging"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": ["foxfire-three.txt"]
    },
    {
        "id": "foxfire3-acorn-indian-pudding",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Acorn Indian Pudding",
        "category": "desserts",
        "attribution": "Foxfire 3",
        "source_note": "Traditional Appalachian recipe from Foxfire 3",
        "description": "A cornmeal-style pudding made with acorn meal and sorghum.",
        "servings_yield": "",
        "prep_time": "",
        "cook_time": "15 minutes",
        "total_time": "",
        "ingredients": [
            {"item": "acorn meal", "quantity": "1", "unit": "cup", "prep_note": ""},
            {"item": "water", "quantity": "4", "unit": "cups", "prep_note": "3 cups boiling, 1 cup for mixing"},
            {"item": "sorghum syrup", "quantity": "", "unit": "to taste", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Put three cups water on to boil."},
            {"step": 2, "text": "Mix acorn meal with remaining cup of water, stir until smooth."},
            {"step": 3, "text": "Add to boiling water, stir until thickened."},
            {"step": 4, "text": "Add sorghum syrup to taste."},
            {"step": 5, "text": "Cover and cook fifteen minutes at low heat."}
        ],
        "temperature": "Low heat",
        "pan_size": "",
        "notes": ["Acorn meal was once a staple of pioneer diet when times were rough"],
        "tags": ["pudding", "acorn", "sorghum", "appalachian", "foxfire", "foraging"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": ["foxfire-three.txt"]
    },
    # ==========================================
    # FOXFIRE 3 - ELDERFLOWER RECIPES
    # ==========================================
    {
        "id": "foxfire3-elderflower-fritters",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Elderflower Fritters",
        "category": "desserts",
        "attribution": "Foxfire 3",
        "source_note": "Traditional Appalachian recipe from Foxfire 3",
        "description": "Battered and fried elderflower clusters.",
        "servings_yield": "",
        "prep_time": "",
        "cook_time": "",
        "total_time": "",
        "ingredients": [
            {"item": "elderflower clusters", "quantity": "", "unit": "", "prep_note": ""},
            {"item": "fritter batter", "quantity": "", "unit": "", "prep_note": ""},
            {"item": "fat", "quantity": "", "unit": "for frying", "prep_note": ""},
            {"item": "powdered sugar", "quantity": "", "unit": "for dusting", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Dip elderflower clusters in fritter batter."},
            {"step": 2, "text": "Fry in fat."},
            {"step": 3, "text": "Dust with powdered sugar and serve."}
        ],
        "temperature": "",
        "pan_size": "",
        "notes": [],
        "tags": ["fritters", "elderflower", "fried", "dessert", "appalachian", "foxfire"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": ["foxfire-three.txt"]
    },
    {
        "id": "foxfire3-elderberry-apple-orange-jam",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Elderberry-Apple-Orange Jam",
        "category": "preserves",
        "attribution": "Foxfire 3",
        "source_note": "Traditional Appalachian recipe from Foxfire 3",
        "description": "A complex jam combining elderberries with apples and citrus.",
        "servings_yield": "",
        "prep_time": "",
        "cook_time": "",
        "total_time": "",
        "ingredients": [
            {"item": "elderberries", "quantity": "1", "unit": "quart", "prep_note": ""},
            {"item": "sugar", "quantity": "5", "unit": "cups", "prep_note": ""},
            {"item": "lemon", "quantity": "1", "unit": "", "prep_note": ""},
            {"item": "large cooking apples", "quantity": "12", "unit": "", "prep_note": ""},
            {"item": "medium oranges", "quantity": "3", "unit": "", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Cook apples until mushy."},
            {"step": 2, "text": "Add the berries, oranges, and lemon chopped fine."},
            {"step": 3, "text": "Add sugar and cook until thick."}
        ],
        "temperature": "",
        "pan_size": "",
        "notes": [],
        "tags": ["jam", "elderberry", "apple", "orange", "preserves", "appalachian", "foxfire"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": ["foxfire-three.txt"]
    },
    # ==========================================
    # FOXFIRE 3 - GRAPE RECIPES
    # ==========================================
    {
        "id": "foxfire3-stuffed-grape-leaves",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Stuffed Grape Leaves",
        "category": "main dishes",
        "attribution": "Foxfire 3",
        "source_note": "Traditional Appalachian recipe from Foxfire 3",
        "description": "Grape leaves stuffed with meat and rice.",
        "servings_yield": "",
        "prep_time": "",
        "cook_time": "",
        "total_time": "",
        "ingredients": [
            {"item": "grape leaves", "quantity": "", "unit": "", "prep_note": "young and tender"},
            {"item": "ground meat", "quantity": "", "unit": "", "prep_note": ""},
            {"item": "rice", "quantity": "", "unit": "", "prep_note": "cooked"},
            {"item": "onion", "quantity": "", "unit": "", "prep_note": "chopped"},
            {"item": "seasonings", "quantity": "", "unit": "", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Mix ground meat with cooked rice, onion, and seasonings."},
            {"step": 2, "text": "Place filling on grape leaves and roll up."},
            {"step": 3, "text": "Steam or bake until done."}
        ],
        "temperature": "",
        "pan_size": "",
        "notes": [],
        "tags": ["stuffed", "grape-leaves", "meat", "rice", "appalachian", "foxfire"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": ["foxfire-three.txt"]
    },
    {
        "id": "foxfire3-spiced-grapes",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Spiced Grapes",
        "category": "preserves",
        "attribution": "Foxfire 3",
        "source_note": "Traditional Appalachian recipe from Foxfire 3",
        "description": "Pickled spiced grapes.",
        "servings_yield": "",
        "prep_time": "",
        "cook_time": "",
        "total_time": "",
        "ingredients": [
            {"item": "grapes", "quantity": "5", "unit": "lb", "prep_note": "stemmed"},
            {"item": "sugar", "quantity": "4", "unit": "lb", "prep_note": ""},
            {"item": "cinnamon", "quantity": "1", "unit": "stick", "prep_note": ""},
            {"item": "apple vinegar", "quantity": "1 1/2", "unit": "pints", "prep_note": "good quality"},
            {"item": "allspice", "quantity": "1/2", "unit": "tsp", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Stem and wash five pounds grapes."},
            {"step": 2, "text": "Boil one and one-half pints of good apple vinegar with sugar and one stick cinnamon and half teaspoon allspice."},
            {"step": 3, "text": "Add grapes and boil until thick."},
            {"step": 4, "text": "Bottle and seal while hot."}
        ],
        "temperature": "",
        "pan_size": "",
        "notes": [],
        "tags": ["spiced", "grapes", "pickled", "preserves", "appalachian", "foxfire"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": ["foxfire-three.txt"]
    },
    # ==========================================
    # FOXFIRE 3 - MAYAPPLE RECIPES
    # ==========================================
    {
        "id": "foxfire3-mayapple-marmalade",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Mayapple Marmalade",
        "category": "preserves",
        "attribution": "Foxfire 3",
        "source_note": "Traditional Appalachian recipe from Foxfire 3",
        "description": "A marmalade from ripe mayapple fruits with their strawberry-like flavor.",
        "servings_yield": "",
        "prep_time": "",
        "cook_time": "",
        "total_time": "",
        "ingredients": [
            {"item": "ripe mayapple fruits", "quantity": "", "unit": "", "prep_note": "must be fully ripe"},
            {"item": "sugar", "quantity": "", "unit": "to taste", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Gather ripe fruits and simmer until soft."},
            {"step": 2, "text": "Strain through a colander."},
            {"step": 3, "text": "Boil the pulp with sugar to taste."}
        ],
        "temperature": "",
        "pan_size": "",
        "notes": [
            "CAUTION: Only the ripe fruit is edible - all other parts of the plant are poisonous",
            "Green mayapples can cause stomach ache"
        ],
        "tags": ["marmalade", "mayapple", "preserves", "appalachian", "foxfire", "foraging"],
        "confidence": {"overall": "high", "flags": ["Only ripe fruit is safe - rest of plant is poisonous"]},
        "image_refs": ["foxfire-three.txt"]
    },
    # ==========================================
    # FOXFIRE 3 - GROUNDCHERRY RECIPES
    # ==========================================
    {
        "id": "foxfire3-groundcherry-preserves",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Groundcherry Preserves",
        "category": "preserves",
        "attribution": "Foxfire 3",
        "source_note": "Traditional Appalachian recipe from Foxfire 3",
        "description": "Preserves made from groundcherries (husk tomatoes).",
        "servings_yield": "",
        "prep_time": "",
        "cook_time": "",
        "total_time": "",
        "ingredients": [
            {"item": "groundcherries", "quantity": "1", "unit": "quart", "prep_note": "husked"},
            {"item": "sugar", "quantity": "3", "unit": "cups", "prep_note": ""},
            {"item": "water", "quantity": "1/4", "unit": "cup", "prep_note": ""},
            {"item": "lemon juice", "quantity": "2", "unit": "tbsp", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Remove husks from groundcherries and wash."},
            {"step": 2, "text": "Combine with sugar, water, and lemon juice."},
            {"step": 3, "text": "Cook slowly until thick."},
            {"step": 4, "text": "Pour into jars and seal."}
        ],
        "temperature": "",
        "pan_size": "",
        "notes": ["Also called cape gooseberry or husk tomato"],
        "tags": ["preserves", "groundcherry", "appalachian", "foxfire", "foraging"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": ["foxfire-three.txt"]
    },
    # ==========================================
    # FOXFIRE 3 - WALNUT RECIPES
    # ==========================================
    {
        "id": "foxfire3-black-walnut-pudding",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Black Walnut Pudding",
        "category": "desserts",
        "attribution": "Foxfire 3",
        "source_note": "Traditional Appalachian recipe from Foxfire 3",
        "description": "A rich pudding with black walnuts.",
        "servings_yield": "",
        "prep_time": "",
        "cook_time": "",
        "total_time": "",
        "ingredients": [
            {"item": "black walnut meats", "quantity": "1", "unit": "cup", "prep_note": "chopped"},
            {"item": "eggs", "quantity": "3", "unit": "", "prep_note": "separated"},
            {"item": "sugar", "quantity": "1", "unit": "cup", "prep_note": ""},
            {"item": "milk", "quantity": "2", "unit": "cups", "prep_note": ""},
            {"item": "vanilla", "quantity": "1", "unit": "tsp", "prep_note": ""},
            {"item": "flour", "quantity": "2", "unit": "tbsp", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Beat egg yolks with sugar until light."},
            {"step": 2, "text": "Add milk and flour, cook until thickened."},
            {"step": 3, "text": "Add vanilla and walnuts."},
            {"step": 4, "text": "Fold in stiffly beaten egg whites."},
            {"step": 5, "text": "Pour into baking dish and bake until set."}
        ],
        "temperature": "325°F (165°C)",
        "pan_size": "Baking dish",
        "notes": [],
        "tags": ["pudding", "walnut", "black-walnut", "dessert", "appalachian", "foxfire"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": ["foxfire-three.txt"]
    },
    {
        "id": "foxfire3-pickled-walnuts",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Pickled Walnuts",
        "category": "preserves",
        "attribution": "Foxfire 3",
        "source_note": "Traditional Appalachian pickle from Foxfire 3",
        "description": "Green walnuts pickled in spiced vinegar.",
        "servings_yield": "",
        "prep_time": "",
        "cook_time": "",
        "total_time": "Several weeks",
        "ingredients": [
            {"item": "green walnuts", "quantity": "100", "unit": "", "prep_note": "young, before shell hardens"},
            {"item": "salt", "quantity": "", "unit": "for brining", "prep_note": ""},
            {"item": "vinegar", "quantity": "1", "unit": "gallon", "prep_note": ""},
            {"item": "black pepper", "quantity": "1", "unit": "oz", "prep_note": ""},
            {"item": "ginger", "quantity": "1/2", "unit": "oz", "prep_note": ""},
            {"item": "mace", "quantity": "1/2", "unit": "oz", "prep_note": ""},
            {"item": "nutmeg", "quantity": "1/2", "unit": "oz", "prep_note": ""},
            {"item": "cloves", "quantity": "1/2", "unit": "oz", "prep_note": ""},
            {"item": "mustard seed", "quantity": "1/2", "unit": "oz", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Gather green walnuts before the shell hardens (test with a needle)."},
            {"step": 2, "text": "Soak in brine for nine days, changing brine every three days."},
            {"step": 3, "text": "Drain and spread on trays in sun until they turn black."},
            {"step": 4, "text": "Pack in jars."},
            {"step": 5, "text": "Boil vinegar with spices and pour over walnuts."},
            {"step": 6, "text": "Seal and store."}
        ],
        "temperature": "",
        "pan_size": "",
        "notes": ["Must use young green walnuts before shell hardens"],
        "tags": ["pickled", "walnuts", "green", "spiced", "preserves", "appalachian", "foxfire"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": ["foxfire-three.txt"]
    },
    # ==========================================
    # FOXFIRE 2 - APPENDIX RECIPES
    # ==========================================
    {
        "id": "foxfire2-leather-breeches-beans",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Aunt Arie's Leather Breeches Beans",
        "category": "sides",
        "attribution": "Foxfire 2 - Aunt Arie",
        "source_note": "Traditional Appalachian preserved beans from Foxfire 2",
        "description": "Dried green beans strung and hung from the rafters, then rehydrated and cooked with pork.",
        "servings_yield": "",
        "prep_time": "",
        "cook_time": "3-4 hours total",
        "total_time": "",
        "ingredients": [
            {"item": "leather breeches beans", "quantity": "", "unit": "as many strings as needed", "prep_note": "dried green beans on thread"},
            {"item": "baking soda", "quantity": "1", "unit": "tsp", "prep_note": "for parboiling"},
            {"item": "fat pork", "quantity": "", "unit": "several large chunks", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Take good, full green beans and string them on spool thread, breaking off the ends. Hang from rafters in warm, dark attic (not in sun or open air)."},
            {"step": 2, "text": "To cook: take down as many strings as needed and soak overnight."},
            {"step": 3, "text": "In the morning, parboil for an hour with a little soda added (not over a teaspoon or they'll turn yellow)."},
            {"step": 4, "text": "Take them out, wash and rinse them."},
            {"step": 5, "text": "Put in a pot with clear water and several large chunks of fat pork."},
            {"step": 6, "text": "Cook for two or three hours more until soft and done."}
        ],
        "temperature": "",
        "pan_size": "",
        "notes": ["If beans are 'nothin' but slabs, they ain't fit t'eat' - use good, full beans"],
        "tags": ["beans", "dried", "preserved", "pork", "appalachian", "foxfire", "aunt-arie"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": ["Foxfire-Book-2.txt"]
    },
    {
        "id": "foxfire2-ada-kelly-cornbread",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Ada Kelly's Fermented Cornbread",
        "category": "breads",
        "attribution": "Foxfire 2 - Ada Kelly",
        "source_note": "Traditional Appalachian fermented cornbread from Foxfire 2",
        "description": "An old-fashioned cornbread made with fermented cornmeal mush.",
        "servings_yield": "",
        "prep_time": "Overnight fermentation",
        "cook_time": "",
        "total_time": "",
        "ingredients": [
            {"item": "corn meal mush", "quantity": "1", "unit": "quart", "prep_note": "cooked thoroughly"},
            {"item": "salt", "quantity": "", "unit": "to taste", "prep_note": ""},
            {"item": "cold water", "quantity": "", "unit": "enough to cool", "prep_note": ""},
            {"item": "sugar", "quantity": "3/4", "unit": "cup", "prep_note": ""},
            {"item": "lard", "quantity": "3/4", "unit": "cup", "prep_note": ""},
            {"item": "corn meal", "quantity": "", "unit": "additional for batter", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Cook one quart of corn meal mush until thoroughly done. Salt to taste."},
            {"step": 2, "text": "Remove from heat and add cold water until you can bear your finger in it."},
            {"step": 3, "text": "Add 3/4 cup sugar, 3/4 cup lard, and meal enough to make stiff as cornbread."},
            {"step": 4, "text": "Set aside until it ferments (overnight)."},
            {"step": 5, "text": "Add meal to make medium batter."},
            {"step": 6, "text": "Bake in well-greased pan in slow oven. Remove from pan when cold."}
        ],
        "temperature": "300°F (150°C)",
        "pan_size": "Well-greased baking pan",
        "notes": [],
        "tags": ["cornbread", "fermented", "bread", "appalachian", "foxfire"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": ["Foxfire-Book-2.txt"]
    },
    {
        "id": "foxfire2-icicle-pickles",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Icicle Pickles",
        "category": "preserves",
        "attribution": "Foxfire 2 - Margaret Norton",
        "source_note": "Traditional Appalachian pickles from Foxfire 2",
        "description": "Sweet, crisp cucumber pickles that take about two weeks to make.",
        "servings_yield": "2 gallons",
        "prep_time": "",
        "cook_time": "",
        "total_time": "About 2 weeks",
        "ingredients": [
            {"item": "cucumbers", "quantity": "2", "unit": "gallons", "prep_note": "split lengthwise"},
            {"item": "coarse salt", "quantity": "1", "unit": "pint", "prep_note": ""},
            {"item": "boiling water", "quantity": "1", "unit": "gallon", "prep_note": ""},
            {"item": "alum", "quantity": "1", "unit": "walnut-sized lump", "prep_note": ""},
            {"item": "vinegar", "quantity": "2", "unit": "quarts", "prep_note": ""},
            {"item": "white sugar", "quantity": "4", "unit": "quarts", "prep_note": ""},
            {"item": "saccharine", "quantity": "1", "unit": "tablet", "prep_note": ""},
            {"item": "pickling spice", "quantity": "1", "unit": "tbsp", "prep_note": ""},
            {"item": "celery seed", "quantity": "2", "unit": "tbsp", "prep_note": ""},
            {"item": "cinnamon buds", "quantity": "2", "unit": "tbsp", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Split cucumbers lengthwise, no matter how small. Add salt to boiling water and pour over cucumbers. Let stand one week."},
            {"step": 2, "text": "Drain, cover with boiling water again and let stand twenty-four hours."},
            {"step": 3, "text": "Drain, dissolve alum in boiling water and pour over pickles. Let stand twenty-four hours."},
            {"step": 4, "text": "Drain. Boil vinegar, sugar, and all spices together and pour over pickles."},
            {"step": 5, "text": "Do this for four mornings - pouring off liquid, reboiling it, and pouring back over pickles boiling hot."},
            {"step": 6, "text": "Seal in cans."}
        ],
        "temperature": "",
        "pan_size": "",
        "notes": ["Will also keep in an open jar but most people seal them for winter"],
        "tags": ["pickles", "cucumber", "sweet", "preserves", "appalachian", "foxfire", "canning"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": ["Foxfire-Book-2.txt"]
    },
    {
        "id": "foxfire2-lime-pickles",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Lime Pickles",
        "category": "preserves",
        "attribution": "Foxfire 2 - Margaret Norton",
        "source_note": "Traditional Appalachian pickles from Foxfire 2",
        "description": "Crisp pickles made with builder's lime for extra crunch.",
        "servings_yield": "7 quarts",
        "prep_time": "",
        "cook_time": "1 hour",
        "total_time": "About 2 days",
        "ingredients": [
            {"item": "green tomatoes or cucumbers", "quantity": "7", "unit": "lb", "prep_note": "cut up"},
            {"item": "builder's lime", "quantity": "3", "unit": "cups", "prep_note": ""},
            {"item": "cold water", "quantity": "2", "unit": "gallons", "prep_note": ""},
            {"item": "vinegar", "quantity": "3", "unit": "pints", "prep_note": ""},
            {"item": "white sugar", "quantity": "5", "unit": "lb", "prep_note": ""},
            {"item": "pickling spice", "quantity": "2", "unit": "tbsp", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Let tomatoes or cucumbers soak with lime and water for twenty-four hours."},
            {"step": 2, "text": "Then let pickles soak in clear water for four hours, changing water every hour."},
            {"step": 3, "text": "Make syrup of vinegar, sugar, and pickling spice and bring to a boil."},
            {"step": 4, "text": "Add cucumbers and let stand overnight."},
            {"step": 5, "text": "Boil for one hour, pack in glass jars, and seal."}
        ],
        "temperature": "",
        "pan_size": "",
        "notes": [],
        "tags": ["pickles", "lime", "crisp", "preserves", "appalachian", "foxfire", "canning"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": ["Foxfire-Book-2.txt"]
    },
    {
        "id": "foxfire2-spiced-grapes",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Spiced Grapes Relish",
        "category": "preserves",
        "attribution": "Foxfire 2 - Margaret Norton",
        "source_note": "Traditional Appalachian relish from Foxfire 2",
        "description": "A spiced grape relish used with meat and bread.",
        "servings_yield": "",
        "prep_time": "",
        "cook_time": "",
        "total_time": "",
        "ingredients": [
            {"item": "grapes", "quantity": "7", "unit": "lb", "prep_note": "Concord or wine grapes"},
            {"item": "fruit vinegar", "quantity": "1", "unit": "cup", "prep_note": ""},
            {"item": "cinnamon", "quantity": "2", "unit": "tsp", "prep_note": ""},
            {"item": "sugar", "quantity": "5", "unit": "lb", "prep_note": ""},
            {"item": "cloves", "quantity": "1", "unit": "tsp", "prep_note": ""},
            {"item": "allspice", "quantity": "1", "unit": "tsp", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Wash, stem, and pulp grapes."},
            {"step": 2, "text": "Put pulp with seeds over fire and cook until seeds come free."},
            {"step": 3, "text": "Add skins and pulp together, and also add sugar, vinegar, and spices."},
            {"step": 4, "text": "Cook until thick and can."}
        ],
        "temperature": "",
        "pan_size": "",
        "notes": [],
        "tags": ["relish", "grapes", "spiced", "preserves", "appalachian", "foxfire"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": ["Foxfire-Book-2.txt"]
    },
    {
        "id": "foxfire2-pickled-green-tomatoes",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Pickled Green Tomatoes",
        "category": "preserves",
        "attribution": "Foxfire 2 - Margaret Norton",
        "source_note": "Traditional Appalachian pickles from Foxfire 2",
        "description": "Hot and sweet pickled green tomatoes.",
        "servings_yield": "",
        "prep_time": "",
        "cook_time": "15 minutes processing",
        "total_time": "",
        "ingredients": [
            {"item": "green tomatoes", "quantity": "", "unit": "", "prep_note": "washed and quartered"},
            {"item": "hot pepper pods", "quantity": "2-3", "unit": "small whole", "prep_note": "per pint jar"},
            {"item": "bell pepper", "quantity": "1", "unit": "pod", "prep_note": "quartered, per jar"},
            {"item": "vinegar", "quantity": "2", "unit": "parts", "prep_note": ""},
            {"item": "water", "quantity": "1", "unit": "part", "prep_note": ""},
            {"item": "sugar", "quantity": "1", "unit": "part", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Wash and quarter green tomatoes. Pack raw into pint jars."},
            {"step": 2, "text": "Add to each jar two-three small whole pods of hot pepper and one quartered pod of bell pepper."},
            {"step": 3, "text": "Make brine of two parts vinegar, one part water, one part sugar; heat until sugar melts."},
            {"step": 4, "text": "Pour into packed jars leaving half-inch at top."},
            {"step": 5, "text": "Put on lids and rings and process fifteen minutes in water bath."}
        ],
        "temperature": "",
        "pan_size": "Pint jars",
        "notes": [],
        "tags": ["pickles", "tomatoes", "green", "hot", "preserves", "appalachian", "foxfire", "canning"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": ["Foxfire-Book-2.txt"]
    },
    {
        "id": "foxfire2-pickled-peaches-apples",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Pickled Peaches or Apples",
        "category": "preserves",
        "attribution": "Foxfire 2 - Margaret Norton",
        "source_note": "Traditional Appalachian pickled fruit from Foxfire 2",
        "description": "Spiced pickled peaches or apples.",
        "servings_yield": "",
        "prep_time": "",
        "cook_time": "",
        "total_time": "",
        "ingredients": [
            {"item": "peaches or apples", "quantity": "", "unit": "", "prep_note": "peeled and quartered"},
            {"item": "vinegar", "quantity": "2", "unit": "parts", "prep_note": ""},
            {"item": "sugar", "quantity": "2", "unit": "parts", "prep_note": ""},
            {"item": "water", "quantity": "1", "unit": "part", "prep_note": ""},
            {"item": "ground cinnamon", "quantity": "", "unit": "to taste", "prep_note": ""},
            {"item": "nutmeg", "quantity": "", "unit": "to taste", "prep_note": ""},
            {"item": "allspice", "quantity": "", "unit": "to taste", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Peel apples or peaches, quarter, and put in a pot."},
            {"step": 2, "text": "Make enough brine of two parts vinegar, two parts sugar, and one part water to cover fruit."},
            {"step": 3, "text": "Add ground cinnamon, nutmeg, and allspice to taste, and cook until tender."},
            {"step": 4, "text": "When done, lift fruit out and pack into jars."},
            {"step": 5, "text": "Keep brine simmering and pour into jars over fruit leaving one-half inch at top."},
            {"step": 6, "text": "Seal immediately."}
        ],
        "temperature": "",
        "pan_size": "",
        "notes": [],
        "tags": ["pickled", "peaches", "apples", "spiced", "preserves", "appalachian", "foxfire"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": ["Foxfire-Book-2.txt"]
    },
    {
        "id": "foxfire2-aunt-arie-egg-custard",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Aunt Arie's Egg Custard",
        "category": "desserts",
        "attribution": "Foxfire 2 - Aunt Arie",
        "source_note": "Traditional Appalachian custard pie from Foxfire 2",
        "description": "A simple egg custard pie baked on a wood stove.",
        "servings_yield": "4 servings",
        "prep_time": "",
        "cook_time": "",
        "total_time": "",
        "ingredients": [
            {"item": "biscuit dough", "quantity": "", "unit": "for crust", "prep_note": "rolled thin"},
            {"item": "egg", "quantity": "1", "unit": "", "prep_note": "beaten well"},
            {"item": "sweet milk", "quantity": "1", "unit": "cup", "prep_note": ""},
            {"item": "flour", "quantity": "1", "unit": "handful", "prep_note": ""},
            {"item": "nutmeg", "quantity": "1", "unit": "tsp", "prep_note": ""},
            {"item": "sugar", "quantity": "1/2", "unit": "teacup", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Line a small pie pan with plain biscuit dough rolled thin."},
            {"step": 2, "text": "In a separate bowl, mix up one egg (beaten well), one cup of sweet milk, a handful of flour, a teaspoon of nutmeg, half a teacup of sugar."},
            {"step": 3, "text": "Mix it all up well, pour into the crust."},
            {"step": 4, "text": "Using just a little wood so the fire won't be too hot, bake slowly until it 'sets.'"},
            {"step": 5, "text": "It will 'blubber up' - or bubble, and then the bubbles will settle. At this point it is ready to eat."}
        ],
        "temperature": "Low/slow heat",
        "pan_size": "Small pie pan",
        "notes": ["Originally cooked on a wood stove"],
        "tags": ["custard", "pie", "egg", "dessert", "appalachian", "foxfire", "aunt-arie"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": ["Foxfire-Book-2.txt"]
    },
    {
        "id": "foxfire2-sweet-potato-pudding",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Sweet Potato Pudding",
        "category": "desserts",
        "attribution": "Foxfire 2",
        "source_note": "Traditional Appalachian recipe from Foxfire 2",
        "description": "A baked sweet potato pudding with raisins and coconut.",
        "servings_yield": "",
        "prep_time": "",
        "cook_time": "30 minutes",
        "total_time": "",
        "ingredients": [
            {"item": "sweet potato", "quantity": "2", "unit": "cups", "prep_note": "cooked and mashed"},
            {"item": "brown sugar", "quantity": "1/2", "unit": "cup", "prep_note": ""},
            {"item": "sweet milk", "quantity": "1", "unit": "cup", "prep_note": ""},
            {"item": "eggs", "quantity": "2", "unit": "", "prep_note": ""},
            {"item": "vanilla", "quantity": "1", "unit": "tsp", "prep_note": ""},
            {"item": "raisins", "quantity": "1/2", "unit": "cup", "prep_note": ""},
            {"item": "grated coconut", "quantity": "1/2", "unit": "cup", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Mix together all ingredients."},
            {"step": 2, "text": "Bake in a casserole dish in a moderate oven for about half-hour, or until firm."},
            {"step": 3, "text": "Serve hot or cold."}
        ],
        "temperature": "350°F (175°C)",
        "pan_size": "Casserole dish",
        "notes": [],
        "tags": ["pudding", "sweet-potato", "dessert", "appalachian", "foxfire"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": ["Foxfire-Book-2.txt"]
    },
    {
        "id": "foxfire2-irish-potato-dumplings",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Irish Potato Dumplings",
        "category": "main dishes",
        "attribution": "Foxfire 2",
        "source_note": "Traditional Appalachian recipe from Foxfire 2",
        "description": "Biscuit dumplings cooked in creamy potato broth.",
        "servings_yield": "",
        "prep_time": "",
        "cook_time": "",
        "total_time": "",
        "ingredients": [
            {"item": "potatoes", "quantity": "1", "unit": "quart", "prep_note": "peeled and quartered"},
            {"item": "water", "quantity": "1 1/2 to 2", "unit": "quarts", "prep_note": ""},
            {"item": "salt and pepper", "quantity": "", "unit": "to taste", "prep_note": ""},
            {"item": "butter", "quantity": "1", "unit": "tbsp", "prep_note": ""},
            {"item": "sweet milk", "quantity": "1", "unit": "cup", "prep_note": ""},
            {"item": "biscuit dough", "quantity": "", "unit": "", "prep_note": "rolled 1/4-inch thick, cut in 2-inch squares"}
        ],
        "instructions": [
            {"step": 1, "text": "Put quartered potatoes in pot, cover with water, add salt, pepper, butter, and milk."},
            {"step": 2, "text": "Boil until potatoes are tender."},
            {"step": 3, "text": "Roll biscuit dough out one-quarter-inch thick, cut in two-inch squares."},
            {"step": 4, "text": "Drop into the rapidly boiling water the potatoes are in."},
            {"step": 5, "text": "Cook dumplings about one minute, take the pot off the heat, and serve."}
        ],
        "temperature": "",
        "pan_size": "",
        "notes": [],
        "tags": ["dumplings", "potato", "comfort-food", "appalachian", "foxfire"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": ["Foxfire-Book-2.txt"]
    },
    {
        "id": "foxfire2-pepper-sauce",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Pepper Sauce (Hot Pepper Relish)",
        "category": "preserves",
        "attribution": "Foxfire 2",
        "source_note": "Traditional Appalachian hot pepper sauce from Foxfire 2",
        "description": "A hot pepper and onion relish.",
        "servings_yield": "",
        "prep_time": "",
        "cook_time": "15 minutes",
        "total_time": "",
        "ingredients": [
            {"item": "large onions", "quantity": "14", "unit": "", "prep_note": ""},
            {"item": "green bell peppers", "quantity": "12", "unit": "", "prep_note": ""},
            {"item": "ripe bell peppers", "quantity": "12", "unit": "", "prep_note": ""},
            {"item": "vinegar", "quantity": "2-3", "unit": "pints", "prep_note": ""},
            {"item": "sugar", "quantity": "2", "unit": "cups", "prep_note": ""},
            {"item": "salt", "quantity": "2", "unit": "tbsp", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Chop onions and peppers up fine."},
            {"step": 2, "text": "Pour boiling water over them and let stand for five minutes, then drain."},
            {"step": 3, "text": "Put back in kettle and pour on more boiling water, let boil two minutes, drain."},
            {"step": 4, "text": "Put back in kettle again."},
            {"step": 5, "text": "Add vinegar, sugar, and salt and boil for fifteen minutes."},
            {"step": 6, "text": "Can while hot."}
        ],
        "temperature": "",
        "pan_size": "",
        "notes": [],
        "tags": ["pepper-sauce", "relish", "hot", "preserves", "appalachian", "foxfire", "canning"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": ["Foxfire-Book-2.txt"]
    },
    # ==========================================
    # FOXFIRE 3 - MINT RECIPES
    # ==========================================
    {
        "id": "foxfire3-mint-with-peas",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Mint with New Peas",
        "category": "sides",
        "attribution": "Foxfire 3",
        "source_note": "Traditional Appalachian recipe from Foxfire 3",
        "description": "Fresh mint cooked with young peas.",
        "servings_yield": "",
        "prep_time": "",
        "cook_time": "",
        "total_time": "",
        "ingredients": [
            {"item": "young peas", "quantity": "", "unit": "", "prep_note": "very young"},
            {"item": "mint leaves", "quantity": "", "unit": "", "prep_note": "young, torn in pieces"}
        ],
        "instructions": [
            {"step": 1, "text": "Tear young mint leaves in pieces."},
            {"step": 2, "text": "Cook with very young peas."}
        ],
        "temperature": "",
        "pan_size": "",
        "notes": ["Use spearmint or peppermint"],
        "tags": ["peas", "mint", "vegetable", "side", "appalachian", "foxfire"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": ["foxfire-three.txt"]
    },
    {
        "id": "foxfire3-mint-syrup",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Mint Syrup",
        "category": "sauces",
        "attribution": "Foxfire 3",
        "source_note": "Traditional Appalachian recipe from Foxfire 3",
        "description": "A sweet mint syrup for fresh fruit or puddings.",
        "servings_yield": "",
        "prep_time": "",
        "cook_time": "",
        "total_time": "1 hour steeping",
        "ingredients": [
            {"item": "sugar", "quantity": "2", "unit": "cups", "prep_note": ""},
            {"item": "water", "quantity": "1", "unit": "cup", "prep_note": ""},
            {"item": "fresh or dried mint leaves", "quantity": "1", "unit": "tbsp", "prep_note": "chopped fine"}
        ],
        "instructions": [
            {"step": 1, "text": "Stir together sugar, water, and mint leaves."},
            {"step": 2, "text": "Simmer until sugar is completely dissolved."},
            {"step": 3, "text": "Cover and let stand one hour."},
            {"step": 4, "text": "Strain and use over fresh fruit or puddings."}
        ],
        "temperature": "",
        "pan_size": "",
        "notes": [],
        "tags": ["syrup", "mint", "sauce", "dessert", "appalachian", "foxfire"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": ["foxfire-three.txt"]
    },
    {
        "id": "foxfire3-mint-jelly",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Mint Jelly",
        "category": "preserves",
        "attribution": "Foxfire 3",
        "source_note": "Traditional Appalachian recipe from Foxfire 3",
        "description": "Fresh mint jelly, traditionally served with lamb.",
        "servings_yield": "",
        "prep_time": "",
        "cook_time": "",
        "total_time": "",
        "ingredients": [
            {"item": "mint leaves", "quantity": "", "unit": "", "prep_note": "fresh"},
            {"item": "boiling water", "quantity": "", "unit": "to cover", "prep_note": ""},
            {"item": "sugar", "quantity": "", "unit": "", "prep_note": ""},
            {"item": "pectin", "quantity": "", "unit": "", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Do not boil leaves, but pour boiling water over them and let steep."},
            {"step": 2, "text": "Strain."},
            {"step": 3, "text": "Add sugar and pectin."},
            {"step": 4, "text": "Cook until it jells."}
        ],
        "temperature": "",
        "pan_size": "",
        "notes": [],
        "tags": ["jelly", "mint", "preserves", "lamb", "appalachian", "foxfire"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": ["foxfire-three.txt"]
    },
    {
        "id": "foxfire3-mint-vinegar",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Mint Vinegar",
        "category": "preserves",
        "attribution": "Foxfire 3",
        "source_note": "Traditional Appalachian flavored vinegar from Foxfire 3",
        "description": "Mint-infused vinegar that ripens over several weeks.",
        "servings_yield": "",
        "prep_time": "",
        "cook_time": "",
        "total_time": "Several weeks to ripen",
        "ingredients": [
            {"item": "tender mint leaves", "quantity": "2", "unit": "cups", "prep_note": ""},
            {"item": "sugar", "quantity": "1", "unit": "cup", "prep_note": ""},
            {"item": "cider vinegar", "quantity": "1", "unit": "quart", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Let mint stand covered by sugar for five minutes."},
            {"step": 2, "text": "Bring vinegar to a boil."},
            {"step": 3, "text": "Add mint and sugar to vinegar and boil three minutes."},
            {"step": 4, "text": "Strain through cheesecloth and bottle."},
            {"step": 5, "text": "Let stand several weeks to ripen."}
        ],
        "temperature": "",
        "pan_size": "",
        "notes": [],
        "tags": ["vinegar", "mint", "flavored", "preserves", "appalachian", "foxfire"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": ["foxfire-three.txt"]
    },
    {
        "id": "foxfire3-mint-sauce",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Mint Sauce",
        "category": "sauces",
        "attribution": "Foxfire 3",
        "source_note": "Traditional Appalachian sauce from Foxfire 3",
        "description": "Classic mint sauce for lamb.",
        "servings_yield": "",
        "prep_time": "",
        "cook_time": "",
        "total_time": "1 hour",
        "ingredients": [
            {"item": "mint", "quantity": "1", "unit": "bunch", "prep_note": ""},
            {"item": "sugar", "quantity": "3/4", "unit": "tbsp", "prep_note": ""},
            {"item": "vinegar", "quantity": "3/4", "unit": "cup", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Chop mint very fine."},
            {"step": 2, "text": "Dissolve sugar in vinegar."},
            {"step": 3, "text": "Add mint and let stand one hour."},
            {"step": 4, "text": "Strain and serve."}
        ],
        "temperature": "",
        "pan_size": "",
        "notes": [],
        "tags": ["sauce", "mint", "lamb", "condiment", "appalachian", "foxfire"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": ["foxfire-three.txt"]
    },
    {
        "id": "foxfire3-mint-frosting",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Mint Frosting",
        "category": "desserts",
        "attribution": "Foxfire 3",
        "source_note": "Traditional Appalachian frosting from Foxfire 3",
        "description": "A fresh mint frosting for cakes.",
        "servings_yield": "",
        "prep_time": "",
        "cook_time": "",
        "total_time": "",
        "ingredients": [
            {"item": "young mint leaves", "quantity": "", "unit": "", "prep_note": "chopped fine"},
            {"item": "powdered sugar", "quantity": "", "unit": "", "prep_note": ""},
            {"item": "soft butter", "quantity": "", "unit": "", "prep_note": ""},
            {"item": "cream", "quantity": "", "unit": "drops", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Chop young mint leaves fine."},
            {"step": 2, "text": "Mix with powdered sugar, soft butter, and drops of cream."}
        ],
        "temperature": "",
        "pan_size": "",
        "notes": [],
        "tags": ["frosting", "mint", "cake", "dessert", "appalachian", "foxfire"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": ["foxfire-three.txt"]
    },
    # ==========================================
    # FOXFIRE 3 - FIG RECIPES
    # ==========================================
    {
        "id": "foxfire3-fig-preserves",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Fig Preserves",
        "category": "preserves",
        "attribution": "Foxfire 3",
        "source_note": "Traditional Appalachian recipe from Foxfire 3",
        "description": "Simple fig preserves.",
        "servings_yield": "",
        "prep_time": "",
        "cook_time": "",
        "total_time": "Overnight",
        "ingredients": [
            {"item": "figs", "quantity": "", "unit": "", "prep_note": ""},
            {"item": "sugar", "quantity": "", "unit": "to cover figs", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Put figs in a pan, and add sugar until it covers the figs."},
            {"step": 2, "text": "Let stand overnight."},
            {"step": 3, "text": "In the morning, cook until thick and clear."},
            {"step": 4, "text": "Put in jars and seal."}
        ],
        "temperature": "",
        "pan_size": "",
        "notes": ["Figs should be picked in early morning"],
        "tags": ["preserves", "figs", "appalachian", "foxfire"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": ["foxfire-three.txt"]
    },
    {
        "id": "foxfire3-fig-pudding",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Fig Pudding",
        "category": "desserts",
        "attribution": "Foxfire 3",
        "source_note": "Traditional Appalachian recipe from Foxfire 3",
        "description": "A rice pudding with figs and nuts.",
        "servings_yield": "",
        "prep_time": "",
        "cook_time": "",
        "total_time": "",
        "ingredients": [
            {"item": "cooked rice", "quantity": "2", "unit": "cups", "prep_note": ""},
            {"item": "milk", "quantity": "2", "unit": "cups", "prep_note": ""},
            {"item": "egg", "quantity": "1", "unit": "whole", "prep_note": "beaten"},
            {"item": "butter or margarine", "quantity": "1/4", "unit": "stick", "prep_note": "melted"},
            {"item": "figs", "quantity": "1", "unit": "cup", "prep_note": "chopped"},
            {"item": "nuts", "quantity": "1/2", "unit": "cup", "prep_note": "chopped"},
            {"item": "cinnamon", "quantity": "1/2", "unit": "tsp", "prep_note": ""},
            {"item": "nutmeg", "quantity": "1/4", "unit": "tsp", "prep_note": ""},
            {"item": "vanilla", "quantity": "1", "unit": "tsp", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Mix rice, milk, beaten egg, figs, nuts, and spices."},
            {"step": 2, "text": "Add vanilla and melted butter."},
            {"step": 3, "text": "Pour into greased baking dish and bake."}
        ],
        "temperature": "350°F (175°C)",
        "pan_size": "Greased baking dish",
        "notes": [],
        "tags": ["pudding", "fig", "rice", "dessert", "appalachian", "foxfire"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": ["foxfire-three.txt"]
    },
    {
        "id": "foxfire3-honey-figs",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Honey Figs",
        "category": "desserts",
        "attribution": "Foxfire 3",
        "source_note": "Traditional Appalachian recipe from Foxfire 3",
        "description": "Fresh figs drizzled with honey.",
        "servings_yield": "",
        "prep_time": "",
        "cook_time": "",
        "total_time": "",
        "ingredients": [
            {"item": "figs", "quantity": "", "unit": "", "prep_note": "peeled and halved"},
            {"item": "honey", "quantity": "", "unit": "", "prep_note": "thin"}
        ],
        "instructions": [
            {"step": 1, "text": "Peel figs and cut in half."},
            {"step": 2, "text": "Arrange in serving dish."},
            {"step": 3, "text": "Pour a thin honey over them."}
        ],
        "temperature": "",
        "pan_size": "",
        "notes": [],
        "tags": ["figs", "honey", "dessert", "simple", "appalachian", "foxfire"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": ["foxfire-three.txt"]
    },
    # ==========================================
    # FOXFIRE 3 - CRABAPPLE RECIPES
    # ==========================================
    {
        "id": "foxfire3-crabapple-jelly",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Crabapple Jelly",
        "category": "preserves",
        "attribution": "Foxfire 3",
        "source_note": "Traditional Appalachian recipe from Foxfire 3",
        "description": "Classic crabapple jelly, can add mint leaves if desired.",
        "servings_yield": "",
        "prep_time": "",
        "cook_time": "20 minutes",
        "total_time": "",
        "ingredients": [
            {"item": "crabapples", "quantity": "", "unit": "", "prep_note": ""},
            {"item": "water", "quantity": "", "unit": "to cover", "prep_note": ""},
            {"item": "sugar", "quantity": "1", "unit": "cup", "prep_note": "per cup juice"},
            {"item": "mint leaves", "quantity": "", "unit": "optional", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Simmer crabapples twenty minutes. Mash in pan."},
            {"step": 2, "text": "Strain. Add one cup sugar to one cup juice."},
            {"step": 3, "text": "Add mint leaves if desired."},
            {"step": 4, "text": "Put in jars, and set in a dark place to thicken."}
        ],
        "temperature": "",
        "pan_size": "",
        "notes": ["Crabapples were often added to blackberries or blueberries to help jelly set"],
        "tags": ["jelly", "crabapple", "preserves", "appalachian", "foxfire", "foraging"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": ["foxfire-three.txt"]
    },
    {
        "id": "foxfire3-crabapple-butter",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Crabapple Butter",
        "category": "preserves",
        "attribution": "Foxfire 3",
        "source_note": "Traditional Appalachian fruit butter from Foxfire 3",
        "description": "A spiced crabapple butter.",
        "servings_yield": "",
        "prep_time": "",
        "cook_time": "",
        "total_time": "",
        "ingredients": [
            {"item": "crabapples", "quantity": "4", "unit": "quarts", "prep_note": ""},
            {"item": "sugar", "quantity": "3", "unit": "cups", "prep_note": ""},
            {"item": "sweet cider", "quantity": "4", "unit": "cups", "prep_note": ""},
            {"item": "cinnamon", "quantity": "2", "unit": "tsp", "prep_note": ""},
            {"item": "cloves", "quantity": "1", "unit": "tsp", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Cook crabapples with peelings and run through a food mill."},
            {"step": 2, "text": "Boil slowly until thick."},
            {"step": 3, "text": "Add sugar and spices and cook until thick."},
            {"step": 4, "text": "Pour into jars and seal."}
        ],
        "temperature": "",
        "pan_size": "",
        "notes": [],
        "tags": ["butter", "crabapple", "spiced", "preserves", "appalachian", "foxfire"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": ["foxfire-three.txt"]
    },
    {
        "id": "foxfire3-sweet-pickled-crabapples",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Sweet Pickled Crabapples",
        "category": "preserves",
        "attribution": "Foxfire 3",
        "source_note": "Traditional Appalachian pickle from Foxfire 3",
        "description": "Spiced pickled crabapples.",
        "servings_yield": "2 quarts",
        "prep_time": "",
        "cook_time": "",
        "total_time": "",
        "ingredients": [
            {"item": "crabapples", "quantity": "2", "unit": "quarts", "prep_note": ""},
            {"item": "sugar", "quantity": "2 1/2", "unit": "cups", "prep_note": ""},
            {"item": "whole cloves", "quantity": "2", "unit": "tsp", "prep_note": ""},
            {"item": "cinnamon sticks", "quantity": "2", "unit": "", "prep_note": ""},
            {"item": "vinegar", "quantity": "2", "unit": "cups", "prep_note": ""},
            {"item": "water", "quantity": "1 1/2", "unit": "cups", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Wash crabapples. Cut out blossom ends, but leave stems intact."},
            {"step": 2, "text": "Combine sugar, spices, vinegar, and water in large saucepan and heat until sugar dissolves."},
            {"step": 3, "text": "Add crabapples and simmer gently until tender."},
            {"step": 4, "text": "Pack in jars, pour syrup over, and seal."}
        ],
        "temperature": "",
        "pan_size": "",
        "notes": [],
        "tags": ["pickled", "crabapple", "sweet", "spiced", "preserves", "appalachian", "foxfire"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": ["foxfire-three.txt"]
    },
    # ==========================================
    # FOXFIRE 3 - YARROW & TEA RECIPES
    # ==========================================
    {
        "id": "foxfire3-yarrow-tea",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Yarrow Tea",
        "category": "beverages",
        "attribution": "Foxfire 3",
        "source_note": "Traditional Appalachian tea from Foxfire 3",
        "description": "A bracing, warming tea from yarrow leaves.",
        "servings_yield": "",
        "prep_time": "",
        "cook_time": "",
        "total_time": "",
        "ingredients": [
            {"item": "yarrow leaves", "quantity": "", "unit": "", "prep_note": "dry or green"}
        ],
        "instructions": [
            {"step": 1, "text": "Place dry or green yarrow leaves in a cup."},
            {"step": 2, "text": "Pour hot water over them."},
            {"step": 3, "text": "Steep only until color shows."},
            {"step": 4, "text": "Drink without sweetening."}
        ],
        "temperature": "",
        "pan_size": "",
        "notes": ["Good and warming in cold weather"],
        "tags": ["tea", "yarrow", "beverage", "medicinal", "appalachian", "foxfire", "foraging"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": ["foxfire-three.txt"]
    },
    {
        "id": "foxfire3-fried-yarrow",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Fried Yarrow",
        "category": "sides",
        "attribution": "Foxfire 3",
        "source_note": "Traditional Appalachian recipe from Foxfire 3",
        "description": "Yarrow leaves fried in butter and served with orange juice.",
        "servings_yield": "",
        "prep_time": "",
        "cook_time": "",
        "total_time": "",
        "ingredients": [
            {"item": "yarrow leaves", "quantity": "", "unit": "", "prep_note": ""},
            {"item": "butter", "quantity": "", "unit": "", "prep_note": ""},
            {"item": "sugar", "quantity": "", "unit": "for sprinkling", "prep_note": ""},
            {"item": "orange juice", "quantity": "", "unit": "", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Fry yarrow in butter until brown."},
            {"step": 2, "text": "Serve hot, sprinkled with sugar and the juice of an orange."}
        ],
        "temperature": "",
        "pan_size": "",
        "notes": [],
        "tags": ["yarrow", "fried", "side", "wild-plants", "appalachian", "foxfire"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": ["foxfire-three.txt"]
    },
    {
        "id": "foxfire3-chamomile-tea",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Chamomile Tea",
        "category": "beverages",
        "attribution": "Foxfire 3",
        "source_note": "Traditional Appalachian tea from Foxfire 3",
        "description": "A pleasant-tasting tea from chamomile flower heads.",
        "servings_yield": "",
        "prep_time": "",
        "cook_time": "",
        "total_time": "",
        "ingredients": [
            {"item": "chamomile flower heads", "quantity": "", "unit": "", "prep_note": "gathered at noon when sun is shining"}
        ],
        "instructions": [
            {"step": 1, "text": "Gather flower heads at noon when the sun is shining (dried blooms will retain better flavor)."},
            {"step": 2, "text": "Pour hot water over flower heads."},
            {"step": 3, "text": "Steep and strain."}
        ],
        "temperature": "",
        "pan_size": "",
        "notes": [],
        "tags": ["tea", "chamomile", "beverage", "medicinal", "appalachian", "foxfire", "foraging"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": ["foxfire-three.txt"]
    },
    {
        "id": "foxfire3-pennyroyal-tea",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Pennyroyal Tea",
        "category": "beverages",
        "attribution": "Foxfire 3",
        "source_note": "Traditional Appalachian tea from Foxfire 3",
        "description": "The best-tasting of the wild mint teas, helpful for coughs and colds.",
        "servings_yield": "",
        "prep_time": "",
        "cook_time": "",
        "total_time": "",
        "ingredients": [
            {"item": "pennyroyal leaves", "quantity": "", "unit": "", "prep_note": "fresh or dried"},
            {"item": "hot water", "quantity": "", "unit": "", "prep_note": ""},
            {"item": "syrup or honey", "quantity": "", "unit": "for sweetening", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Use fresh or dried leaves. Do not boil."},
            {"step": 2, "text": "Merely pour hot water over the leaves and let stand for a few minutes."},
            {"step": 3, "text": "Flavor with syrup or honey."}
        ],
        "temperature": "",
        "pan_size": "",
        "notes": ["Also called penny-rile or squaw-mint"],
        "tags": ["tea", "pennyroyal", "mint", "beverage", "medicinal", "appalachian", "foxfire"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": ["foxfire-three.txt"]
    },
    {
        "id": "foxfire3-blue-mountain-tea",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Blue-Mountain Tea",
        "category": "beverages",
        "attribution": "Foxfire 3",
        "source_note": "Traditional Appalachian tea from Foxfire 3",
        "description": "A delicious licorice-flavored tea from a special goldenrod that grows in the Blue Ridge Mountains.",
        "servings_yield": "",
        "prep_time": "",
        "cook_time": "",
        "total_time": "",
        "ingredients": [
            {"item": "blue-mountain tea leaves", "quantity": "", "unit": "", "prep_note": "green or dry (Solidago odora)"},
            {"item": "hot water", "quantity": "", "unit": "", "prep_note": ""},
            {"item": "sugar, honey, or lemon", "quantity": "", "unit": "optional", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Steep green or dry leaves in hot water until the tea is a pale golden color."},
            {"step": 2, "text": "Add sugar, honey, or lemon if desired."},
            {"step": 3, "text": "Can be served hot or cold."}
        ],
        "temperature": "",
        "pan_size": "",
        "notes": ["Has a distinctive licorice taste and odor - impossible to mistake for any other plant"],
        "tags": ["tea", "goldenrod", "beverage", "licorice", "appalachian", "foxfire", "foraging"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": ["foxfire-three.txt"]
    },
    # ==========================================
    # FOXFIRE 3 - HAW RECIPES
    # ==========================================
    {
        "id": "foxfire3-possum-haw-jelly",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Possum Haw Jelly",
        "category": "preserves",
        "attribution": "Foxfire 3",
        "source_note": "Traditional Appalachian recipe from Foxfire 3",
        "description": "Jelly from possum haw berries, often combined with crabapples.",
        "servings_yield": "",
        "prep_time": "",
        "cook_time": "",
        "total_time": "",
        "ingredients": [
            {"item": "possum haw berries", "quantity": "", "unit": "", "prep_note": ""},
            {"item": "sugar", "quantity": "", "unit": "to taste", "prep_note": ""},
            {"item": "crabapples", "quantity": "", "unit": "optional", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Boil berries until soft."},
            {"step": 2, "text": "Strain through cloth."},
            {"step": 3, "text": "Add sugar to taste."},
            {"step": 4, "text": "Boil again until thickened."},
            {"step": 5, "text": "Combine with crabapples if desired."}
        ],
        "temperature": "",
        "pan_size": "",
        "notes": ["Haw berries are extremely seedy"],
        "tags": ["jelly", "haw", "preserves", "appalachian", "foxfire", "foraging"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": ["foxfire-three.txt"]
    },
    {
        "id": "foxfire3-black-haw-sauce",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Black Haw Sauce",
        "category": "sauces",
        "attribution": "Foxfire 3",
        "source_note": "Traditional Appalachian sauce from Foxfire 3",
        "description": "A honey-sweetened sauce from black haw berries.",
        "servings_yield": "",
        "prep_time": "",
        "cook_time": "",
        "total_time": "",
        "ingredients": [
            {"item": "black haw berries", "quantity": "1", "unit": "quart", "prep_note": ""},
            {"item": "honey", "quantity": "3/4", "unit": "cup", "prep_note": ""},
            {"item": "lemon juice", "quantity": "2", "unit": "tbsp", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Wash berries well."},
            {"step": 2, "text": "Cook with honey and lemon juice until soft."},
            {"step": 3, "text": "Strain and serve."}
        ],
        "temperature": "",
        "pan_size": "",
        "notes": [],
        "tags": ["sauce", "haw", "honey", "appalachian", "foxfire", "foraging"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": ["foxfire-three.txt"]
    },
    {
        "id": "foxfire3-red-haw-relish",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Red Haw (Hawthorn) Relish",
        "category": "preserves",
        "attribution": "Foxfire 3",
        "source_note": "Traditional Appalachian recipe from Foxfire 3",
        "description": "A spiced relish from hawthorn fruits.",
        "servings_yield": "",
        "prep_time": "",
        "cook_time": "",
        "total_time": "",
        "ingredients": [
            {"item": "red haw (hawthorn) fruit", "quantity": "3", "unit": "lb", "prep_note": "crushed, not too ripe"},
            {"item": "water", "quantity": "4", "unit": "cups", "prep_note": ""},
            {"item": "sugar", "quantity": "1", "unit": "lb", "prep_note": ""},
            {"item": "vinegar", "quantity": "1/2", "unit": "pint", "prep_note": ""},
            {"item": "cloves", "quantity": "1", "unit": "tsp", "prep_note": ""},
            {"item": "cinnamon", "quantity": "1", "unit": "tsp", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Crush three pounds fruit (not too ripe)."},
            {"step": 2, "text": "Add four cups water and cook until soft."},
            {"step": 3, "text": "Strain through cloth."},
            {"step": 4, "text": "Add sugar, vinegar, and spices."},
            {"step": 5, "text": "Boil until thick. Bottle and seal."}
        ],
        "temperature": "",
        "pan_size": "",
        "notes": [],
        "tags": ["relish", "hawthorn", "haw", "spiced", "preserves", "appalachian", "foxfire"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": ["foxfire-three.txt"]
    },
    {
        "id": "foxfire3-haw-marmalade",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Haw Marmalade",
        "category": "preserves",
        "attribution": "Foxfire 3",
        "source_note": "Traditional Appalachian recipe from Foxfire 3",
        "description": "A marmalade from hawthorn fruits.",
        "servings_yield": "",
        "prep_time": "",
        "cook_time": "",
        "total_time": "",
        "ingredients": [
            {"item": "haw fruits", "quantity": "", "unit": "", "prep_note": ""},
            {"item": "water", "quantity": "", "unit": "very little", "prep_note": ""},
            {"item": "sugar", "quantity": "", "unit": "to taste", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Cook haws in very little water."},
            {"step": 2, "text": "Press through a colander to remove seeds."},
            {"step": 3, "text": "Add sugar to taste."},
            {"step": 4, "text": "Cook until thick and bottle."}
        ],
        "temperature": "",
        "pan_size": "",
        "notes": [],
        "tags": ["marmalade", "haw", "hawthorn", "preserves", "appalachian", "foxfire"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": ["foxfire-three.txt"]
    },
]


def main():
    # Load existing recipes
    with open(RECIPES_FILE, 'r') as f:
        data = json.load(f)

    # Get existing recipe IDs to avoid duplicates
    existing_ids = {r['id'] for r in data['recipes']}

    # Add new recipes
    added = 0
    for recipe in SUPPLEMENTAL_RECIPES:
        if recipe['id'] not in existing_ids:
            data['recipes'].append(recipe)
            added += 1
            print(f"Added: {recipe['title']}")
        else:
            print(f"Skipped (exists): {recipe['title']}")

    # Update metadata
    data['meta']['total_recipes'] = len(data['recipes'])
    data['meta']['last_updated'] = "2026-01-17"

    # Save
    with open(RECIPES_FILE, 'w') as f:
        json.dump(data, f, indent=2)

    print(f"\nAdded {added} supplemental Foxfire recipes. Total: {len(data['recipes'])}")


if __name__ == "__main__":
    main()
