#!/usr/bin/env python3
"""
Add additional recipes found in deeper search of Foxfire Books 2 and 4.

Includes:
- Switchell (honey-vinegar drink)
- Violet recipes (jelly, sugared, syrup)
- Milkweed recipes
- Chicory recipes
- Wild lettuce recipes
- Dandelion recipes (wine, coffee, salad, omelet)
- Cochan greens
- Tar cough syrup
- Sawmill gravy
"""

import json
from pathlib import Path

RECIPES_FILE = Path(__file__).parent.parent / "data" / "recipes.json"

ADDITIONAL_RECIPES = [
    {
        "id": "foxfire2-switchell-drink",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Switchell (Honey-Vinegar Drink)",
        "category": "beverages",
        "attribution": "Traditional Appalachian, via Foxfire 2",
        "source_note": "Traditional drink for hot summer haymaking days from Foxfire Book 2",
        "description": "A nourishing drink made from honey and cider vinegar, traditionally consumed during haymaking days in summer.",
        "servings_yield": "1 jar concentrate",
        "prep_time": "5 minutes",
        "cook_time": "None",
        "total_time": "5 minutes",
        "ingredients": [
            {"item": "honey", "quantity": "1/2", "unit": "cup", "prep_note": ""},
            {"item": "cider vinegar", "quantity": "1/2", "unit": "cup", "prep_note": ""},
            {"item": "water", "quantity": "1", "unit": "dipper", "prep_note": "per serving"}
        ],
        "instructions": [
            {"step": 1, "text": "Mix half cup honey and half cup cider vinegar together."},
            {"step": 2, "text": "Keep in a jar."},
            {"step": 3, "text": "To serve, add four teaspoons of the mixture to a dipper of water for a nourishing drink."}
        ],
        "temperature": "",
        "pan_size": "",
        "notes": ["A traditional drink for hot summer haymaking days."],
        "tags": ["beverage", "drink", "honey", "vinegar", "appalachian", "foxfire", "traditional", "summer"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "foxfire2-violet-jelly",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Violet Jelly",
        "category": "preserves",
        "attribution": "Traditional Appalachian, via Foxfire 2",
        "source_note": "Traditional wild food recipe from Foxfire Book 2",
        "description": "A delicate jelly made from wild violet flowers.",
        "servings_yield": "Several jars",
        "prep_time": "30 minutes",
        "cook_time": "30 minutes",
        "total_time": "1 hour",
        "ingredients": [
            {"item": "violet flowers", "quantity": "several cups", "unit": "", "prep_note": "fresh"},
            {"item": "boiling water", "quantity": "to cover", "unit": "", "prep_note": ""},
            {"item": "sugar", "quantity": "to taste", "unit": "", "prep_note": ""},
            {"item": "pectin", "quantity": "as needed", "unit": "", "prep_note": ""},
            {"item": "lemon", "quantity": "1/2", "unit": "", "prep_note": "juice only"}
        ],
        "instructions": [
            {"step": 1, "text": "Cook violet flowers with boiling water."},
            {"step": 2, "text": "Strain the liquid."},
            {"step": 3, "text": "Add sugar, pectin, and juice of half a lemon."},
            {"step": 4, "text": "Simmer until it jells."},
            {"step": 5, "text": "Pour into jars and seal."}
        ],
        "temperature": "",
        "pan_size": "Large saucepan",
        "notes": ["Violet flowers give this jelly a beautiful color and delicate flavor."],
        "tags": ["jelly", "preserves", "violet", "wild foods", "appalachian", "foxfire", "flowers"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "foxfire2-sugared-violets",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Sugared Violets",
        "category": "desserts",
        "attribution": "Traditional Appalachian, via Foxfire 2",
        "source_note": "Traditional confection from Foxfire Book 2",
        "description": "Crystallized violet blossoms for decoration or eating.",
        "servings_yield": "About 1 cup",
        "prep_time": "20 minutes",
        "cook_time": "10 minutes",
        "total_time": "30 minutes plus drying time",
        "ingredients": [
            {"item": "sugar", "quantity": "2", "unit": "cups", "prep_note": ""},
            {"item": "water", "quantity": "1/2", "unit": "cup", "prep_note": ""},
            {"item": "cream of tartar", "quantity": "dash", "unit": "", "prep_note": ""},
            {"item": "fresh violet blossoms", "quantity": "as desired", "unit": "", "prep_note": "stems removed"}
        ],
        "instructions": [
            {"step": 1, "text": "Cook two cups sugar, half cup water, and a dash of cream of tartar."},
            {"step": 2, "text": "Stir until sugar grains (crystallizes)."},
            {"step": 3, "text": "Dip fresh violet blossoms (free from stems) into the sugar mixture."},
            {"step": 4, "text": "Place on platter to dry."}
        ],
        "temperature": "",
        "pan_size": "Saucepan",
        "notes": ["Beautiful for decorating cakes or eating as confections."],
        "tags": ["confection", "desserts", "violet", "candy", "appalachian", "foxfire", "flowers"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "foxfire2-violet-syrup",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Violet Syrup",
        "category": "preserves",
        "attribution": "Traditional Appalachian, via Foxfire 2",
        "source_note": "Traditional cold remedy from Foxfire Book 2",
        "description": "A medicinal syrup made from violet blossoms, good for colds or coughs.",
        "servings_yield": "Several jars",
        "prep_time": "2 days",
        "cook_time": "15 minutes",
        "total_time": "2 days plus 15 minutes",
        "ingredients": [
            {"item": "violet blossoms", "quantity": "as needed", "unit": "", "prep_note": ""},
            {"item": "water", "quantity": "to cover", "unit": "", "prep_note": ""},
            {"item": "honey", "quantity": "to taste", "unit": "", "prep_note": ""},
            {"item": "lemon", "quantity": "1", "unit": "", "prep_note": "juice only"}
        ],
        "instructions": [
            {"step": 1, "text": "Cover violet blossoms with water."},
            {"step": 2, "text": "Let stand two days."},
            {"step": 3, "text": "Strain the liquid."},
            {"step": 4, "text": "Cook with honey and juice of lemon."},
            {"step": 5, "text": "Stir well and bring to a boil."},
            {"step": 6, "text": "Put in jars and seal."}
        ],
        "temperature": "",
        "pan_size": "Saucepan",
        "notes": ["Good for colds or coughs."],
        "tags": ["syrup", "preserves", "violet", "remedy", "cold", "cough", "appalachian", "foxfire"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "foxfire2-fried-milkweed",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Fried Milkweed",
        "category": "side dishes",
        "attribution": "Traditional Appalachian, via Foxfire 2",
        "source_note": "Traditional wild food recipe from Foxfire Book 2",
        "description": "Young milkweed shoots fried with eggs and cheese.",
        "servings_yield": "2-4 servings",
        "prep_time": "10 minutes",
        "cook_time": "20 minutes",
        "total_time": "30 minutes",
        "ingredients": [
            {"item": "young milkweed shoots", "quantity": "1", "unit": "lb", "prep_note": "very young, before leaves unfold"},
            {"item": "water", "quantity": "to cover", "unit": "", "prep_note": "salted"},
            {"item": "fat for frying", "quantity": "small amount", "unit": "", "prep_note": ""},
            {"item": "eggs", "quantity": "2-3", "unit": "", "prep_note": ""},
            {"item": "salt and pepper", "quantity": "to taste", "unit": "", "prep_note": ""},
            {"item": "cheese", "quantity": "optional", "unit": "", "prep_note": "grated"}
        ],
        "instructions": [
            {"step": 1, "text": "Cut young milkweed shoots in small pieces."},
            {"step": 2, "text": "Boil fifteen minutes in salted water."},
            {"step": 3, "text": "Drain well."},
            {"step": 4, "text": "Fry in small amount of fat."},
            {"step": 5, "text": "Add eggs, salt and pepper, and cheese if desired."}
        ],
        "temperature": "Medium heat",
        "pan_size": "Frying pan",
        "notes": ["Only use very young shoots before leaves unfold. Do not gather milkweed after July."],
        "tags": ["side dish", "milkweed", "wild foods", "eggs", "appalachian", "foxfire"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "foxfire2-milkweed-soup",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Milkweed Soup",
        "category": "soups",
        "attribution": "Traditional Appalachian, via Foxfire 2",
        "source_note": "Traditional wild food recipe from Foxfire Book 2",
        "description": "Hearty soup made from milkweed shoots or young pods.",
        "servings_yield": "4-6 servings",
        "prep_time": "15 minutes",
        "cook_time": "45 minutes",
        "total_time": "1 hour",
        "ingredients": [
            {"item": "young milkweed shoots or pods", "quantity": "1", "unit": "lb", "prep_note": "cut in small pieces"},
            {"item": "hambone or bacon drippings", "quantity": "1", "unit": "", "prep_note": ""},
            {"item": "rice", "quantity": "1/2", "unit": "cup", "prep_note": ""},
            {"item": "wild onions or ramps", "quantity": "handful", "unit": "", "prep_note": "chopped"},
            {"item": "water", "quantity": "to cover", "unit": "", "prep_note": ""},
            {"item": "salt and pepper", "quantity": "to taste", "unit": "", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "For shoots: Gather young shoots while young and tender (not after July). Wash, cook, and drain."},
            {"step": 2, "text": "Add more water, rice, bacon drippings, salt, pepper, and wild onions."},
            {"step": 3, "text": "Cook over a slow fire until done."},
            {"step": 4, "text": "For pods: Boil a hambone in water."},
            {"step": 5, "text": "Add young milkweed pods cut in small pieces, wild onions or ramps, and a handful of rice."},
            {"step": 6, "text": "Cook slowly. Add salt and pepper before serving."}
        ],
        "temperature": "Low heat",
        "pan_size": "Large pot",
        "notes": ["Two methods: one using shoots, one using young pods. Only gather milkweed before July."],
        "tags": ["soup", "milkweed", "wild foods", "appalachian", "foxfire"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "foxfire2-milkweed-greens",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Milkweed Greens",
        "category": "side dishes",
        "attribution": "Traditional Appalachian, via Foxfire 2",
        "source_note": "Traditional wild food recipe from Foxfire Book 2",
        "description": "Simple preparation of young milkweed stalks as a green vegetable.",
        "servings_yield": "4 servings",
        "prep_time": "5 minutes",
        "cook_time": "10 minutes",
        "total_time": "15 minutes",
        "ingredients": [
            {"item": "very young milkweed stalks", "quantity": "1", "unit": "lb", "prep_note": ""},
            {"item": "water", "quantity": "to cover", "unit": "", "prep_note": ""},
            {"item": "salt", "quantity": "to taste", "unit": "", "prep_note": ""},
            {"item": "butter", "quantity": "2", "unit": "tbsp", "prep_note": ""},
            {"item": "wild onions", "quantity": "to taste", "unit": "", "prep_note": "chopped"}
        ],
        "instructions": [
            {"step": 1, "text": "Cook one pound very young milkweed stalks in water with salt and butter, covered, for ten minutes."},
            {"step": 2, "text": "Drain."},
            {"step": 3, "text": "Add more butter and chopped wild onions."}
        ],
        "temperature": "Medium heat",
        "pan_size": "Saucepan",
        "notes": ["In Tennessee and Kentucky, milkweed is considered a tonic, 'good for what ails you.'"],
        "tags": ["greens", "side dish", "milkweed", "wild foods", "appalachian", "foxfire"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "foxfire2-chicory-with-sauce",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Chicory with Sauce",
        "category": "side dishes",
        "attribution": "Traditional Appalachian, via Foxfire 2",
        "source_note": "Traditional wild food recipe from Foxfire Book 2",
        "description": "Chicory greens served with a tangy mustard sauce.",
        "servings_yield": "4 servings",
        "prep_time": "15 minutes",
        "cook_time": "20 minutes",
        "total_time": "35 minutes",
        "ingredients": [
            {"item": "chicory greens", "quantity": "1", "unit": "lb", "prep_note": "cooked and drained"},
            {"item": "sugar", "quantity": "1/4", "unit": "cup", "prep_note": ""},
            {"item": "salt", "quantity": "1/2", "unit": "tsp", "prep_note": ""},
            {"item": "egg yolks", "quantity": "2", "unit": "", "prep_note": ""},
            {"item": "scalded milk", "quantity": "1", "unit": "cup", "prep_note": ""},
            {"item": "vinegar", "quantity": "2", "unit": "tbsp", "prep_note": ""},
            {"item": "mustard", "quantity": "1", "unit": "tbsp", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Cook chicory greens and drain well."},
            {"step": 2, "text": "Make sauce: combine sugar, salt, egg yolks, scalded milk, vinegar, and mustard."},
            {"step": 3, "text": "Blend until thick in a double boiler."},
            {"step": 4, "text": "Serve sauce over the drained chicory."}
        ],
        "temperature": "Medium heat (double boiler)",
        "pan_size": "Double boiler",
        "notes": ["The tangy sauce complements the slightly bitter chicory greens."],
        "tags": ["greens", "side dish", "chicory", "wild foods", "sauce", "appalachian", "foxfire"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "foxfire2-panned-chicory",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Panned Chicory",
        "category": "side dishes",
        "attribution": "Traditional Appalachian, via Foxfire 2",
        "source_note": "Traditional wild food recipe from Foxfire Book 2",
        "description": "Quick pan-steamed chicory greens in cream sauce.",
        "servings_yield": "2-4 servings",
        "prep_time": "5 minutes",
        "cook_time": "20 minutes",
        "total_time": "25 minutes",
        "ingredients": [
            {"item": "fat", "quantity": "2", "unit": "tbsp", "prep_note": ""},
            {"item": "chicory greens", "quantity": "1", "unit": "lb", "prep_note": "chopped"},
            {"item": "flour", "quantity": "1", "unit": "tbsp", "prep_note": ""},
            {"item": "cream", "quantity": "small amount", "unit": "", "prep_note": ""},
            {"item": "salt and pepper", "quantity": "to taste", "unit": "", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Melt two tablespoons fat in pan."},
            {"step": 2, "text": "Add chopped chicory greens."},
            {"step": 3, "text": "Cover and steam for fifteen minutes."},
            {"step": 4, "text": "Add one tablespoon flour, a small amount of cream, salt and pepper."},
            {"step": 5, "text": "Let simmer five minutes more."}
        ],
        "temperature": "Medium heat",
        "pan_size": "Large covered pan",
        "notes": ["A quick and creamy way to prepare wild chicory."],
        "tags": ["greens", "side dish", "chicory", "wild foods", "appalachian", "foxfire"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "foxfire2-chicory-coffee",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Chicory Coffee",
        "category": "beverages",
        "attribution": "Traditional Appalachian, via Foxfire 2",
        "source_note": "Traditional coffee substitute from Foxfire Book 2",
        "description": "Roasted chicory root used as a coffee substitute or additive.",
        "servings_yield": "Varies",
        "prep_time": "15 minutes",
        "cook_time": "30 minutes",
        "total_time": "45 minutes",
        "ingredients": [
            {"item": "chicory roots", "quantity": "as needed", "unit": "", "prep_note": "fresh"}
        ],
        "instructions": [
            {"step": 1, "text": "Wash and peel chicory roots."},
            {"step": 2, "text": "Grind the roots."},
            {"step": 3, "text": "Roast in oven until dark brown."},
            {"step": 4, "text": "Add to regular coffee, or use instead of coffee."}
        ],
        "temperature": "350°F (175°C)",
        "pan_size": "Baking sheet",
        "notes": ["Popular during times when coffee was scarce or expensive."],
        "tags": ["beverage", "coffee", "chicory", "wild foods", "substitute", "appalachian", "foxfire"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "foxfire2-dandelion-bud-omelet",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Dandelion Bud Omelet",
        "category": "breakfast",
        "attribution": "Traditional Appalachian, via Foxfire 2",
        "source_note": "Traditional wild food recipe from Foxfire Book 2",
        "description": "Fluffy omelet made with dandelion buds fried in butter.",
        "servings_yield": "2 servings",
        "prep_time": "10 minutes",
        "cook_time": "10 minutes",
        "total_time": "20 minutes",
        "ingredients": [
            {"item": "dandelion buds", "quantity": "1", "unit": "cup", "prep_note": "gathered before flower color shows"},
            {"item": "butter", "quantity": "1", "unit": "dab", "prep_note": ""},
            {"item": "eggs", "quantity": "4", "unit": "", "prep_note": ""},
            {"item": "salt and pepper", "quantity": "to taste", "unit": "", "prep_note": ""},
            {"item": "dandelion leaves", "quantity": "handful", "unit": "", "prep_note": "raw, finely cut"}
        ],
        "instructions": [
            {"step": 1, "text": "Gather one cup dandelion buds before flower color shows."},
            {"step": 2, "text": "Fry buds in a dab of butter until they pop."},
            {"step": 3, "text": "Add four eggs, salt and pepper."},
            {"step": 4, "text": "Cook as an omelet."},
            {"step": 5, "text": "Top with raw dandelion leaves, finely cut, before serving."}
        ],
        "temperature": "Medium heat",
        "pan_size": "Omelet pan",
        "notes": ["Gather buds before they show any yellow color for best flavor."],
        "tags": ["omelet", "breakfast", "eggs", "dandelion", "wild foods", "appalachian", "foxfire"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "foxfire2-dandelion-wine",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Dandelion Wine",
        "category": "beverages",
        "attribution": "Traditional Appalachian, via Foxfire 2",
        "source_note": "Traditional wine recipe from Foxfire Book 2",
        "description": "Classic homemade wine made from dandelion flowers.",
        "servings_yield": "About 1 gallon",
        "prep_time": "30 minutes",
        "cook_time": "None",
        "total_time": "About 2 weeks",
        "ingredients": [
            {"item": "dandelion flowers", "quantity": "1", "unit": "gallon", "prep_note": ""},
            {"item": "boiling water", "quantity": "1", "unit": "gallon", "prep_note": ""},
            {"item": "lemons", "quantity": "4", "unit": "", "prep_note": "juice only"},
            {"item": "oranges", "quantity": "4", "unit": "", "prep_note": "juice only"},
            {"item": "sugar", "quantity": "4", "unit": "lbs", "prep_note": ""},
            {"item": "yeast cake", "quantity": "1", "unit": "", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Pour one gallon boiling water over one gallon dandelion flowers."},
            {"step": 2, "text": "Let stand until blossoms rise (24-48 hours)."},
            {"step": 3, "text": "Strain into a stone jar."},
            {"step": 4, "text": "Add juices of four lemons and four oranges, four pounds of sugar, and one yeast cake."},
            {"step": 5, "text": "Stir four or five times a day until it stops fermenting."},
            {"step": 6, "text": "Keep well covered."},
            {"step": 7, "text": "In two weeks, strain, bottle and cork tightly."}
        ],
        "temperature": "",
        "pan_size": "Stone jar",
        "notes": ["A traditional spring wine. Use only the flower petals, not the green parts."],
        "tags": ["wine", "beverage", "dandelion", "wild foods", "fermented", "appalachian", "foxfire"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "foxfire2-dandelion-coffee",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Dandelion Coffee",
        "category": "beverages",
        "attribution": "Traditional Appalachian, via Foxfire 2",
        "source_note": "Traditional coffee substitute from Foxfire Book 2",
        "description": "Roasted dandelion root used as a coffee substitute.",
        "servings_yield": "Varies",
        "prep_time": "15 minutes",
        "cook_time": "30 minutes",
        "total_time": "45 minutes",
        "ingredients": [
            {"item": "dandelion roots", "quantity": "as needed", "unit": "", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Gather dandelion roots."},
            {"step": 2, "text": "Peel the roots."},
            {"step": 3, "text": "Roast until dark brown."},
            {"step": 4, "text": "Grind."},
            {"step": 5, "text": "Use as substitute for real coffee."}
        ],
        "temperature": "350°F (175°C)",
        "pan_size": "Baking sheet",
        "notes": ["A caffeine-free coffee alternative with a slightly bitter, nutty flavor."],
        "tags": ["beverage", "coffee", "dandelion", "wild foods", "substitute", "appalachian", "foxfire"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "foxfire2-green-drink-tonic",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Green Drink Tonic",
        "category": "beverages",
        "attribution": "Traditional Appalachian, via Foxfire 2",
        "source_note": "Traditional tonic from Foxfire Book 2",
        "description": "A healthful tonic drink made from chickweed and dandelion.",
        "servings_yield": "1 serving",
        "prep_time": "15 minutes",
        "cook_time": "20 minutes",
        "total_time": "35 minutes",
        "ingredients": [
            {"item": "chickweed", "quantity": "1", "unit": "cup", "prep_note": ""},
            {"item": "dandelion greens", "quantity": "1", "unit": "cup", "prep_note": ""},
            {"item": "cider vinegar", "quantity": "to taste", "unit": "", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Cook chickweed and dandelion separately."},
            {"step": 2, "text": "Put each through a sieve."},
            {"step": 3, "text": "Add cider vinegar to the combined purees."},
            {"step": 4, "text": "Drink as a tonic."}
        ],
        "temperature": "",
        "pan_size": "Saucepan",
        "notes": ["A spring tonic to cleanse the system after winter."],
        "tags": ["beverage", "tonic", "dandelion", "chickweed", "wild foods", "health", "appalachian", "foxfire"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "foxfire2-wild-lettuce-salad",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Wild Lettuce Salad",
        "category": "salads",
        "attribution": "Traditional Appalachian, via Foxfire 2",
        "source_note": "Traditional wild food recipe from Foxfire Book 2",
        "description": "Fresh salad made with wild lettuce and hot bacon dressing.",
        "servings_yield": "2-4 servings",
        "prep_time": "10 minutes",
        "cook_time": "10 minutes",
        "total_time": "20 minutes",
        "ingredients": [
            {"item": "wild lettuce leaves", "quantity": "4", "unit": "cups", "prep_note": "young, washed and chopped"},
            {"item": "green onions", "quantity": "2-3", "unit": "", "prep_note": "chopped"},
            {"item": "bacon", "quantity": "3", "unit": "strips", "prep_note": ""},
            {"item": "brown sugar", "quantity": "1", "unit": "tbsp", "prep_note": ""},
            {"item": "vinegar", "quantity": "2", "unit": "tbsp", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Cut up wild lettuce greens and wash."},
            {"step": 2, "text": "Cut green onions in it."},
            {"step": 3, "text": "Fry bacon until crisp and crumbly."},
            {"step": 4, "text": "Add brown sugar and vinegar to the hot bacon grease."},
            {"step": 5, "text": "Pour hot dressing over the chopped wild lettuce leaves."},
            {"step": 6, "text": "For extra flavor, add chickweed or mustard."}
        ],
        "temperature": "",
        "pan_size": "Frying pan for bacon",
        "notes": [
            "Gather wild lettuce in early spring when plants are young.",
            "Older plants get tough and wormy.",
            "Wild lettuce has a milky juice when stems are broken."
        ],
        "tags": ["salad", "wild lettuce", "wild foods", "bacon", "appalachian", "foxfire"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "foxfire2-cochan-greens",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Cochan (Tall Coneflower) Greens",
        "category": "side dishes",
        "attribution": "Traditional Appalachian, via Foxfire 2",
        "source_note": "Traditional wild food recipe from Foxfire Book 2",
        "description": "Greens from the tall coneflower plant, parboiled and fried.",
        "servings_yield": "2-4 servings",
        "prep_time": "10 minutes",
        "cook_time": "20 minutes",
        "total_time": "30 minutes",
        "ingredients": [
            {"item": "young cochan (tall coneflower) leaves", "quantity": "1", "unit": "lb", "prep_note": "tender"},
            {"item": "grease", "quantity": "2", "unit": "tbsp", "prep_note": ""},
            {"item": "salt", "quantity": "to taste", "unit": "", "prep_note": ""},
            {"item": "margarine", "quantity": "1", "unit": "tbsp", "prep_note": ""},
            {"item": "boiled eggs", "quantity": "2", "unit": "", "prep_note": "chopped"}
        ],
        "instructions": [
            {"step": 1, "text": "Pick cochan leaves when tender."},
            {"step": 2, "text": "Parboil until tender."},
            {"step": 3, "text": "Wash until water is clear."},
            {"step": 4, "text": "Squeeze water out."},
            {"step": 5, "text": "Put in pan with grease and fry."},
            {"step": 6, "text": "Alternatively, after cooking, chop fine and add salt and margarine."},
            {"step": 7, "text": "Top with chopped boiled eggs."}
        ],
        "temperature": "Medium heat",
        "pan_size": "Frying pan",
        "notes": [
            "Cochan grows along branch banks.",
            "Looks like golden globe flowers.",
            "Be careful not to confuse with wild parsnip, which has more whitish leaves.",
            "Has a distinctive odor when cooking."
        ],
        "tags": ["greens", "side dish", "coneflower", "wild foods", "appalachian", "foxfire"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "foxfire4-tar-cough-syrup",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Tar Cough Syrup",
        "category": "remedies",
        "attribution": "Traditional Appalachian, via Foxfire 4",
        "source_note": "Traditional home remedy from Foxfire Book 4",
        "description": "A traditional cough syrup made from pine tar, molasses, and sulfur.",
        "servings_yield": "About 1 cup",
        "prep_time": "5 minutes",
        "cook_time": "None",
        "total_time": "5 minutes",
        "ingredients": [
            {"item": "pine tar (resin)", "quantity": "1", "unit": "part", "prep_note": "melted from fat pine"},
            {"item": "molasses", "quantity": "5", "unit": "parts", "prep_note": ""},
            {"item": "sulfur", "quantity": "2", "unit": "parts", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Mix one part tar with five parts molasses and two parts sulfur."},
            {"step": 2, "text": "Stir until well combined."},
            {"step": 3, "text": "Take one teaspoonful at a time for coughs."}
        ],
        "temperature": "",
        "pan_size": "",
        "notes": [
            "Tar was also used on blisters, sores, and sometimes poison ivy.",
            "Pine tar was traditionally melted from fat pine on a special rock."
        ],
        "tags": ["remedy", "cough", "syrup", "traditional medicine", "appalachian", "foxfire"],
        "confidence": {"overall": "medium", "flags": ["historical remedy - not for modern medical use"]},
        "image_refs": []
    },
    {
        "id": "foxfire4-sawmill-gravy",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Sawmill Gravy",
        "category": "sauces",
        "attribution": "Traditional Appalachian logging camp, via Foxfire 4",
        "source_note": "Traditional breakfast gravy from Foxfire Book 4 logging camp section",
        "description": "Classic Appalachian white gravy made for logging camp breakfasts, served over biscuits.",
        "servings_yield": "6-8 servings",
        "prep_time": "5 minutes",
        "cook_time": "10 minutes",
        "total_time": "15 minutes",
        "ingredients": [
            {"item": "flour (or corn meal)", "quantity": "3", "unit": "tbsp", "prep_note": "flour preferred"},
            {"item": "pan drippings or grease", "quantity": "3", "unit": "tbsp", "prep_note": "from bacon or meat"},
            {"item": "milk (or water)", "quantity": "2", "unit": "cups", "prep_note": "milk preferred"},
            {"item": "salt and pepper", "quantity": "to taste", "unit": "", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Put flour in a great big skillet."},
            {"step": 2, "text": "Let it brown a little bit in the pan drippings."},
            {"step": 3, "text": "Dump in milk or water if you don't have milk."},
            {"step": 4, "text": "Stir constantly until thickened."},
            {"step": 5, "text": "Season with salt and pepper."},
            {"step": 6, "text": "Serve over hot biscuits."}
        ],
        "temperature": "Medium heat",
        "pan_size": "Large skillet",
        "notes": [
            "Can be made with corn meal instead of flour.",
            "Served every morning in logging camps with eggs, bacon, and biscuits."
        ],
        "tags": ["gravy", "sauce", "breakfast", "biscuits", "appalachian", "foxfire", "logging camp"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    }
]


def main():
    # Load existing recipes
    with open(RECIPES_FILE, 'r') as f:
        data = json.load(f)

    recipes = data['recipes']

    # Track existing IDs
    existing_ids = {r['id'] for r in recipes}

    # Add new recipes
    added = 0
    for recipe in ADDITIONAL_RECIPES:
        if recipe['id'] not in existing_ids:
            recipes.append(recipe)
            existing_ids.add(recipe['id'])
            added += 1
            print(f"Added: {recipe['title']}")
        else:
            print(f"Skipped (exists): {recipe['title']}")

    # Update meta
    data['meta']['total_recipes'] = len(recipes)

    # Save updated recipes
    with open(RECIPES_FILE, 'w') as f:
        json.dump(data, f, indent=2)

    print(f"\nAdded {added} additional Foxfire recipes. Total: {len(recipes)}")


if __name__ == "__main__":
    main()
