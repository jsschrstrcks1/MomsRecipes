#!/usr/bin/env python3
"""
Add Eat the Weeds recipes - Batch 12
Simple/informal recipes and preparation methods
"""

import json
from pathlib import Path

RECIPES_FILE = Path(__file__).parent.parent / "data" / "recipes.json"

ETW_BATCH12_RECIPES = [
    # ===== ACORN GRUBS =====
    {
        "id": "fried-acorn-grubs-etw",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Fried Acorn Grubs",
        "category": "main dishes",
        "attribution": "Eat the Weeds",
        "source_note": "From eattheweeds.com - Acorn Grubs article",
        "description": "Simple fried grubs - soft and buttery when cooked properly.",
        "servings_yield": "varies",
        "prep_time": "10 minutes",
        "cook_time": "5 minutes",
        "ingredients": [
            {"item": "acorn grubs", "quantity": "", "unit": "", "prep_note": "cleaned"},
            {"item": "butter or oil", "quantity": "", "unit": "", "prep_note": "for frying"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat butter or oil over LOW heat. This is critical."},
            {"step": 2, "text": "Add grubs and fry gently for a few minutes."},
            {"step": 3, "text": "Do NOT use high heat - grubs will explode within a second in very hot fat."},
            {"step": 4, "text": "Cook until soft and buttery."}
        ],
        "temperature": "low heat only",
        "pan_size": "",
        "notes": ["Raw grubs taste mild and chewy like fat", "Cooked grubs are soft and buttery", "Peak harvest is September after August rains"],
        "tags": ["grubs", "insects", "foraged", "survival", "unusual protein"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },

    # ===== NEW JERSEY TEA =====
    {
        "id": "new-jersey-tea-etw",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "New Jersey Tea",
        "category": "beverages",
        "attribution": "Eat the Weeds",
        "source_note": "From eattheweeds.com - Ceanothus americanus article",
        "description": "Revolutionary War-era tea substitute made from Red Root plant.",
        "servings_yield": "1 cup",
        "prep_time": "5 minutes",
        "cook_time": "5 minutes",
        "ingredients": [
            {"item": "New Jersey Tea leaves", "quantity": "1", "unit": "tbsp", "prep_note": "fresh, or 1 tsp dried"},
            {"item": "hot water", "quantity": "1", "unit": "cup"}
        ],
        "instructions": [
            {"step": 1, "text": "Hand-crush leaves slightly."},
            {"step": 2, "text": "If using fresh leaves, shade dry them first."},
            {"step": 3, "text": "Steep in hot water like black tea."},
            {"step": 4, "text": "Use 1 tablespoon fresh leaves OR 1 teaspoon dried leaves per cup."}
        ],
        "temperature": "",
        "pan_size": "",
        "notes": ["Colonial fermentation method: Make a decoction of leaves and twigs, dip fresh leaves in it, then dry", "Best harvest time is early summer when plant blossoms", "Seeds are NOT edible"],
        "tags": ["tea", "beverage", "foraged", "historical", "colonial"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },

    # ===== TONBURI =====
    {
        "id": "tonburi-kochia-caviar-etw",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Tonburi (Land Caviar from Kochia Seeds)",
        "category": "vegetables",
        "attribution": "Eat the Weeds",
        "source_note": "From eattheweeds.com - Kochia article",
        "description": "Japanese preparation of kochia seeds that resemble caviar.",
        "servings_yield": "varies",
        "prep_time": "2 days",
        "cook_time": "30 minutes",
        "ingredients": [
            {"item": "kochia seeds", "quantity": "", "unit": "", "prep_note": "dried"}
        ],
        "instructions": [
            {"step": 1, "text": "Dry the seeds thoroughly."},
            {"step": 2, "text": "Boil the dried seeds."},
            {"step": 3, "text": "Soak in cold water for one full day."},
            {"step": 4, "text": "Rub seeds by hand to remove outer skin."},
            {"step": 5, "text": "Seeds will become glossy black-green and resemble caviar."}
        ],
        "temperature": "",
        "pan_size": "",
        "notes": ["Used as garnish in Japanese cuisine", "Plant is very salty tasting", "Like spinach, kochia can accumulate nitrates"],
        "tags": ["kochia", "tonburi", "japanese", "caviar substitute", "foraged"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },

    # ===== PUFFBALL PREPARATIONS =====
    {
        "id": "puffball-crepes-etw",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Puffball Crepes",
        "category": "main dishes",
        "attribution": "Eat the Weeds",
        "source_note": "From eattheweeds.com - Puffballs article",
        "description": "Thin-sliced puffball mushrooms used like crepes.",
        "servings_yield": "varies",
        "prep_time": "10 minutes",
        "cook_time": "10 minutes",
        "ingredients": [
            {"item": "puffball mushroom", "quantity": "1", "unit": "", "prep_note": "verified safe - pure white inside"},
            {"item": "butter", "quantity": "", "unit": "", "prep_note": "for frying"}
        ],
        "instructions": [
            {"step": 1, "text": "CRITICAL: Cut puffball from top to bottom and examine inside."},
            {"step": 2, "text": "Interior must be marshmallow soft, pure white (never dark), with thin outer skin and no outline of mushroom inside."},
            {"step": 3, "text": "Slice puffball very thin."},
            {"step": 4, "text": "Brown slices with butter in a pan."},
            {"step": 5, "text": "Use like crepes - fill and roll."}
        ],
        "temperature": "",
        "pan_size": "",
        "notes": ["Puffballs absorb flavor well but have little taste on their own", "DANGER: Young Amanita (deadly) can look like small puffballs - always cut open to verify", "Young Scleroderma (fatal) has hard white flesh inside"],
        "tags": ["puffball", "mushroom", "foraged", "crepes"],
        "confidence": {"overall": "high", "flags": ["identification critical"]},
        "image_refs": []
    },
    {
        "id": "breaded-puffball-etw",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Breaded Deep-Fried Puffball",
        "category": "main dishes",
        "attribution": "Eat the Weeds",
        "source_note": "From eattheweeds.com - Puffballs article",
        "description": "Puffball slices breaded and deep fried like potatoes.",
        "servings_yield": "varies",
        "prep_time": "10 minutes",
        "cook_time": "10 minutes",
        "ingredients": [
            {"item": "puffball mushroom", "quantity": "1", "unit": "", "prep_note": "verified safe"},
            {"item": "flour", "quantity": "", "unit": "", "prep_note": "for breading"},
            {"item": "oil", "quantity": "", "unit": "", "prep_note": "for deep frying"}
        ],
        "instructions": [
            {"step": 1, "text": "Verify puffball safety: cut open, check for pure white, soft interior with no mushroom outline."},
            {"step": 2, "text": "Slice like potatoes."},
            {"step": 3, "text": "Bread slices in flour."},
            {"step": 4, "text": "Deep fry until golden."}
        ],
        "temperature": "",
        "pan_size": "",
        "notes": ["Can also cube for miso soup or cut into strips for stir fry"],
        "tags": ["puffball", "mushroom", "foraged", "fried"],
        "confidence": {"overall": "high", "flags": ["identification critical"]},
        "image_refs": []
    },

    # ===== WATER HYACINTH =====
    {
        "id": "water-hyacinth-stir-fry-etw",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Water Hyacinth Stir Fry",
        "category": "vegetables",
        "attribution": "Eat the Weeds",
        "source_note": "From eattheweeds.com - Water Hyacinth article",
        "description": "Deep fried water hyacinth bulbs and steamed leaves.",
        "servings_yield": "varies",
        "prep_time": "15 minutes",
        "cook_time": "15 minutes",
        "ingredients": [
            {"item": "water hyacinth bulbous bottoms", "quantity": "", "unit": "", "prep_note": "young"},
            {"item": "water hyacinth leaves", "quantity": "", "unit": "", "prep_note": "young"},
            {"item": "butter", "quantity": "", "unit": ""},
            {"item": "bacon or pork fat", "quantity": "", "unit": "", "prep_note": "optional"}
        ],
        "instructions": [
            {"step": 1, "text": "Harvest only from clean water sources - never downstream from mines."},
            {"step": 2, "text": "Deep fry young bulbous bottoms in butter until crispy like pork rinds."},
            {"step": 3, "text": "Steam young leaves like mustard greens with bacon or pork fat."},
            {"step": 4, "text": "Alternatively, boil or fry leaves."}
        ],
        "temperature": "",
        "pan_size": "",
        "notes": ["May cause itching in some people even when cooked", "Contains 18.7% protein", "ILLEGAL to collect/possess in Florida", "Flowers can be boiled or candied"],
        "tags": ["water hyacinth", "foraged", "aquatic", "stir fry"],
        "confidence": {"overall": "high", "flags": ["legal restrictions in some areas"]},
        "image_refs": []
    },

    # ===== COQUINA BEACH CHOWDER =====
    {
        "id": "coquina-beach-chowder-etw",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Coquina Beach Chowder",
        "category": "soups",
        "attribution": "Eat the Weeds",
        "source_note": "From eattheweeds.com - Cast Netting article",
        "description": "A foraged beach chowder using coquina clams and sea purslane.",
        "servings_yield": "varies",
        "prep_time": "30 minutes",
        "cook_time": "30 minutes",
        "ingredients": [
            {"item": "coquina clams", "quantity": "", "unit": "", "prep_note": "sifted from sand with colander"},
            {"item": "mole crabs", "quantity": "", "unit": "", "prep_note": "optional"},
            {"item": "sea purslane", "quantity": "", "unit": ""},
            {"item": "butter", "quantity": "", "unit": "", "prep_note": "optional"},
            {"item": "cream", "quantity": "", "unit": "", "prep_note": "optional"}
        ],
        "instructions": [
            {"step": 1, "text": "Boil coquina clams and mole crabs together for broth."},
            {"step": 2, "text": "Cook sea purslane separately in plain water to reduce its natural salt."},
            {"step": 3, "text": "Combine broth with purslane and some coquina meat."},
            {"step": 4, "text": "Warm together and serve."},
            {"step": 5, "text": "Add butter and cream if available for richer chowder."}
        ],
        "temperature": "",
        "pan_size": "",
        "notes": ["Coquina broth also makes excellent base for creamed potato soup", "Can stuff fish with sea purslane or sea rocket"],
        "tags": ["chowder", "beach", "foraged", "coquina", "coastal"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },

    # ===== PALMETTO GRUBS =====
    {
        "id": "fried-palmetto-grubs-etw",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Fried Palmetto Weevil Grubs (Grugru)",
        "category": "main dishes",
        "attribution": "Eat the Weeds",
        "source_note": "From eattheweeds.com - Palmetto Weevil Grub article",
        "description": "Fried palm grubs - a tropical delicacy.",
        "servings_yield": "varies",
        "prep_time": "10 minutes",
        "cook_time": "5 minutes",
        "ingredients": [
            {"item": "palmetto weevil grubs", "quantity": "", "unit": "", "prep_note": "from dying palm trees"},
            {"item": "oil or butter", "quantity": "", "unit": "", "prep_note": "for frying"}
        ],
        "instructions": [
            {"step": 1, "text": "Slice or crack grub partway open around the middle."},
            {"step": 2, "text": "This prevents explosion during cooking."},
            {"step": 3, "text": "Fry in oil or butter until cooked through."},
            {"step": 4, "text": "Alternatively, roast next to an open fire."}
        ],
        "temperature": "",
        "pan_size": "",
        "notes": ["Can also be eaten raw", "Pupa stage is reportedly tastiest but rarest", "Contains 3-7% protein and 10-30% fat", "Find in dying palms with dead/bent growing tips"],
        "tags": ["grubs", "insects", "foraged", "survival", "unusual protein", "tropical"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },

    # ===== SUNFLOWER PREPARATIONS =====
    {
        "id": "sunflower-hull-coffee-etw",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Sunflower Hull Coffee",
        "category": "beverages",
        "attribution": "Eat the Weeds",
        "source_note": "From eattheweeds.com - Sunflowers article",
        "description": "A coffee substitute made from roasted sunflower seed hulls.",
        "servings_yield": "varies",
        "prep_time": "10 minutes",
        "cook_time": "20 minutes",
        "ingredients": [
            {"item": "sunflower seed hulls", "quantity": "", "unit": ""},
            {"item": "water", "quantity": "", "unit": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Collect sunflower seed hulls."},
            {"step": 2, "text": "Roast hulls until dark and fragrant."},
            {"step": 3, "text": "Brew roasted hulls in hot water like coffee."}
        ],
        "temperature": "",
        "pan_size": "",
        "notes": ["Seeds can be roasted for snacks or ground raw to thicken soups", "Young stems can be roasted", "Inner stalk pulp was chewed as gum by Pima Indians"],
        "tags": ["sunflower", "coffee substitute", "beverage", "foraged"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },

    # ===== AGAVE PREPARATIONS =====
    {
        "id": "agave-flowers-scrambled-eggs-etw",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Agave Flowers with Scrambled Eggs (Oaxacan Style)",
        "category": "main dishes",
        "attribution": "Eat the Weeds",
        "source_note": "From eattheweeds.com - Century Plant article",
        "description": "Traditional Oaxacan preparation of agave flowers.",
        "servings_yield": "varies",
        "prep_time": "10 minutes",
        "cook_time": "15 minutes",
        "ingredients": [
            {"item": "agave flowers", "quantity": "", "unit": "", "prep_note": "several pounds available per plant"},
            {"item": "eggs", "quantity": "", "unit": "", "prep_note": "scrambled"},
            {"item": "butter or oil", "quantity": "", "unit": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Harvest flowers during summer bloom."},
            {"step": 2, "text": "Boil flowers until tender."},
            {"step": 3, "text": "Mix boiled flowers with scrambled eggs."},
            {"step": 4, "text": "Cook together until eggs are set."}
        ],
        "temperature": "",
        "pan_size": "",
        "notes": ["Flowers can also be roasted", "WARNING: Raw agave juice causes dermatitis - wear eye protection when cutting", "Avoid Agave lechuguilla (toxic species in TX/NM)"],
        "tags": ["agave", "eggs", "mexican", "foraged", "breakfast"],
        "confidence": {"overall": "high", "flags": ["handle with caution"]},
        "image_refs": []
    },
    {
        "id": "pit-roasted-agave-heart-etw",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Pit-Roasted Agave Heart",
        "category": "vegetables",
        "attribution": "Eat the Weeds",
        "source_note": "From eattheweeds.com - Century Plant article",
        "description": "Traditional pit-baked agave stalk with molasses-like flavor.",
        "servings_yield": "varies",
        "prep_time": "1 hour",
        "cook_time": "24 hours",
        "ingredients": [
            {"item": "agave heart/stalk", "quantity": "1", "unit": "", "prep_note": "harvested before blooming"}
        ],
        "instructions": [
            {"step": 1, "text": "Harvest stalk before the plant blooms in summer."},
            {"step": 2, "text": "Dig a pit and line with rocks."},
            {"step": 3, "text": "Build fire and reduce to ashes/coals."},
            {"step": 4, "text": "Place agave heart inside pit."},
            {"step": 5, "text": "Cover to retain heat."},
            {"step": 6, "text": "Retrieve next day after 24 hours."}
        ],
        "temperature": "",
        "pan_size": "pit lined with rocks",
        "notes": ["Tastes like molasses when roasted", "Old and tough plants are best (opposite of typical foraging)", "Seeds can be ground into flour for bread or soup thickener"],
        "tags": ["agave", "pit roasting", "primitive", "foraged", "survival"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },

    # ===== WILD POTATO VINE =====
    {
        "id": "wild-potato-vine-root-etw",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Wild Potato Vine Root (Ipomoea pandurata)",
        "category": "vegetables",
        "attribution": "Eat the Weeds",
        "source_note": "From eattheweeds.com - Ipomoea article",
        "description": "Wild tuber that must be boiled twice to remove acridity.",
        "servings_yield": "varies",
        "prep_time": "20 minutes",
        "cook_time": "1 hour",
        "ingredients": [
            {"item": "wild potato vine roots", "quantity": "", "unit": "", "prep_note": "younger/smaller preferred"}
        ],
        "instructions": [
            {"step": 1, "text": "Cube the roots."},
            {"step": 2, "text": "Boil in water until tender."},
            {"step": 3, "text": "DRAIN and discard water."},
            {"step": 4, "text": "Boil again in fresh water."},
            {"step": 5, "text": "Optionally roast the cubes after double-boiling."}
        ],
        "temperature": "",
        "pan_size": "",
        "notes": ["NEVER eat raw", "Must boil in at least two changes of water", "Younger/smaller roots are less acrid than older ones", "Roots grow straight down from vine entry point"],
        "tags": ["wild potato", "ipomoea", "foraged", "tuber", "survival"],
        "confidence": {"overall": "high", "flags": ["requires double boiling"]},
        "image_refs": []
    },

    # ===== WATER SPINACH =====
    {
        "id": "water-spinach-stir-fry-etw",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Water Spinach Stir Fry",
        "category": "vegetables",
        "attribution": "Eat the Weeds",
        "source_note": "From eattheweeds.com - Ipomoea article",
        "description": "Simple Asian-style stir fried water spinach.",
        "servings_yield": "varies",
        "prep_time": "10 minutes",
        "cook_time": "5 minutes",
        "ingredients": [
            {"item": "water spinach shoots and leaves", "quantity": "", "unit": "", "prep_note": "Ipomoea aquatica"},
            {"item": "garlic", "quantity": "", "unit": "", "prep_note": "minced"},
            {"item": "oil", "quantity": "", "unit": ""},
            {"item": "salt", "quantity": "", "unit": "", "prep_note": "to taste"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat oil in wok or pan."},
            {"step": 2, "text": "Add garlic and stir fry briefly."},
            {"step": 3, "text": "Add water spinach shoots and leaves."},
            {"step": 4, "text": "Stir fry until wilted."},
            {"step": 5, "text": "Season with salt."}
        ],
        "temperature": "high heat",
        "pan_size": "wok",
        "notes": ["Can be eaten raw from clean water", "48% carbs, 24% protein", "Rich in vitamins A, C, E"],
        "tags": ["water spinach", "stir fry", "asian", "foraged", "aquatic"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },

    # ===== JERUSALEM ARTICHOKE =====
    {
        "id": "jerusalem-artichoke-pickles-etw",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Jerusalem Artichoke Pickles",
        "category": "preserves",
        "attribution": "Eat the Weeds",
        "source_note": "From eattheweeds.com - Jerusalem Artichoke article",
        "description": "Pickled sunchokes using bread and butter pickle method.",
        "servings_yield": "varies",
        "prep_time": "30 minutes",
        "cook_time": "varies",
        "ingredients": [
            {"item": "Jerusalem artichokes", "quantity": "", "unit": "", "prep_note": "cleaned, sliced"},
            {"item": "bread and butter pickle brine", "quantity": "", "unit": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Clean tubers thoroughly - they are lumpy and tedious."},
            {"step": 2, "text": "Slice tubers."},
            {"step": 3, "text": "Pickle using bread and butter style method (works better than dill)."}
        ],
        "temperature": "",
        "pan_size": "",
        "notes": ["Pick tubers two weeks after flowers fade", "Flavor improves after frost", "Don't store except in ground - dig as needed", "Build digestive tolerance by eating small portions for 3-4 days first"],
        "tags": ["jerusalem artichoke", "sunchoke", "pickles", "foraged", "preserves"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },

    # ===== WILD RICE =====
    {
        "id": "popped-wild-rice-maple-etw",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Popped Wild Rice with Maple Sugar",
        "category": "snacks",
        "attribution": "Eat the Weeds",
        "source_note": "From eattheweeds.com - Wild Rice article",
        "description": "Traditional Ojibwa preparation of popped wild rice.",
        "servings_yield": "varies",
        "prep_time": "5 minutes",
        "cook_time": "10 minutes",
        "ingredients": [
            {"item": "wild rice grains", "quantity": "", "unit": "", "prep_note": "parched/dried"},
            {"item": "maple sugar or syrup solids", "quantity": "", "unit": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Heat a dry pan."},
            {"step": 2, "text": "Add parched wild rice grains."},
            {"step": 3, "text": "Pop like popcorn, stirring constantly."},
            {"step": 4, "text": "Mix with maple sugar or leftover maple syrup solids."}
        ],
        "temperature": "",
        "pan_size": "",
        "notes": ["Harvest mid-August to mid-September when plants still green", "Sun dry at least 2 days before parching", "Hull immediately after parching or grains reabsorb moisture", "Keep away from sand"],
        "tags": ["wild rice", "popped", "maple", "native american", "foraged", "snack"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },

    # ===== POPLAR BARK =====
    {
        "id": "poplar-bark-bread-etw",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Poplar Bark Bread",
        "category": "breads",
        "attribution": "Eat the Weeds",
        "source_note": "From eattheweeds.com - Poplars and Aspens article",
        "description": "Survival bread made with dried poplar inner bark.",
        "servings_yield": "varies",
        "prep_time": "varies",
        "cook_time": "varies",
        "ingredients": [
            {"item": "poplar inner bark (cambium)", "quantity": "", "unit": "", "prep_note": "cut into strips"},
            {"item": "flour", "quantity": "", "unit": ""},
            {"item": "water", "quantity": "", "unit": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Cut inner bark (cambium) into strips."},
            {"step": 2, "text": "Dry strips completely."},
            {"step": 3, "text": "Grind dried bark into powder."},
            {"step": 4, "text": "Mix bark powder with regular flour."},
            {"step": 5, "text": "Add water to form dough and bake as bread, or cook as mush."}
        ],
        "temperature": "",
        "pan_size": "",
        "notes": ["Inner bark is edible raw or cooked", "High in Vitamin C", "Best species: Eastern Cottonwood, Fremont Cottonwood, Aspens", "Twigs have bitter aspirin-like taste"],
        "tags": ["poplar", "bark", "survival", "bread", "foraged"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },

    # ===== ELDERFLOWER PREPARATIONS =====
    {
        "id": "elder-blow-champagne-etw",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Elder Blow Champagne",
        "category": "beverages",
        "attribution": "Eat the Weeds / Dick Deuerling",
        "source_note": "From eattheweeds.com - Edible Flowers Part Three",
        "description": "Light sparkling wine flavored with elderberry blossoms.",
        "servings_yield": "varies",
        "prep_time": "varies",
        "cook_time": "fermentation time varies",
        "ingredients": [
            {"item": "elderberry blossoms", "quantity": "", "unit": ""},
            {"item": "white wine or champagne base", "quantity": "", "unit": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Harvest elderberry blossoms when fully open."},
            {"step": 2, "text": "Use blossoms to flavor light summer wine."},
            {"step": 3, "text": "Allow to ferment to sparkling stage."}
        ],
        "temperature": "",
        "pan_size": "",
        "notes": ["Elderberry blossoms can also be added to pancake batter", "Use only true elderberry - not water elder or other lookalikes"],
        "tags": ["elderberry", "champagne", "wine", "foraged", "beverage"],
        "confidence": {"overall": "medium", "flags": ["recipe details sparse"]},
        "image_refs": []
    },

    # ===== LINDEN TEA =====
    {
        "id": "linden-basswood-tea-etw",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Linden-Basswood Tea",
        "category": "beverages",
        "attribution": "Eat the Weeds",
        "source_note": "From eattheweeds.com - Edible Flowers Part Three",
        "description": "Honey-flavored tea from linden/basswood blossoms.",
        "servings_yield": "1 cup",
        "prep_time": "5 minutes",
        "cook_time": "5 minutes",
        "ingredients": [
            {"item": "linden/basswood blossoms", "quantity": "", "unit": "", "prep_note": "dried"},
            {"item": "hot water", "quantity": "1", "unit": "cup"}
        ],
        "instructions": [
            {"step": 1, "text": "Harvest and dry linden/basswood blossoms."},
            {"step": 2, "text": "Steep dried blossoms in hot water."},
            {"step": 3, "text": "Strain and serve."}
        ],
        "temperature": "",
        "pan_size": "",
        "notes": ["Has natural honey flavor", "Mix blossoms with basswood seeds for chocolate-like taste"],
        "tags": ["linden", "basswood", "tea", "foraged", "beverage"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },

    # ===== WOKAS =====
    {
        "id": "wokas-pond-lily-seeds-etw",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Wokas (Yellow Pond Lily Seeds)",
        "category": "grains",
        "attribution": "Eat the Weeds",
        "source_note": "From eattheweeds.com - Yellow Pond Lily article",
        "description": "Traditional Native American preparation of pond lily seeds.",
        "servings_yield": "varies",
        "prep_time": "3 weeks",
        "cook_time": "varies",
        "ingredients": [
            {"item": "yellow pond lily seed pods", "quantity": "", "unit": "", "prep_note": "ripe"}
        ],
        "instructions": [
            {"step": 1, "text": "Collect ripe seed pods."},
            {"step": 2, "text": "Place in water for EXACTLY three weeks - this removes bitterness through enzyme action."},
            {"step": 3, "text": "Remove seeds from rotted pods."},
            {"step": 4, "text": "Air dry seeds completely."},
            {"step": 5, "text": "Pop like popcorn (they crack rather than puff), or grind into flour."}
        ],
        "temperature": "",
        "pan_size": "",
        "notes": ["Seeds can be stored as staple or used to thicken soups", "Roots are NOT recommended - extremely bitter even after extensive processing", "Young leaves can go in soups but may be bitter"],
        "tags": ["pond lily", "wokas", "native american", "foraged", "survival"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },

    # ===== HIGH BUSH CRANBERRY =====
    {
        "id": "highbush-cranberry-fritters-etw",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "High Bush Cranberry Flower Fritters",
        "category": "desserts",
        "attribution": "Eat the Weeds",
        "source_note": "From eattheweeds.com - High Bush Cranberry article",
        "description": "Flowers dipped in pancake batter and fried.",
        "servings_yield": "varies",
        "prep_time": "10 minutes",
        "cook_time": "10 minutes",
        "ingredients": [
            {"item": "high bush cranberry flowers", "quantity": "", "unit": ""},
            {"item": "pancake batter", "quantity": "", "unit": ""},
            {"item": "oil", "quantity": "", "unit": "", "prep_note": "for frying"}
        ],
        "instructions": [
            {"step": 1, "text": "Harvest high bush cranberry flowers."},
            {"step": 2, "text": "Dip flowers in pancake batter."},
            {"step": 3, "text": "Fry until golden and batter is cooked through."}
        ],
        "temperature": "",
        "pan_size": "",
        "notes": ["Berries taste better after one or two frosts", "Berries make excellent jelly without added pectin", "Use orange zest to enhance berry flavor"],
        "tags": ["highbush cranberry", "fritters", "flowers", "foraged", "dessert"],
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

    for recipe in ETW_BATCH12_RECIPES:
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
    print(f"  Added: {added} new Eat the Weeds recipes (batch 12)")
    print(f"  Skipped: {skipped} duplicates")
    print(f"  Total recipes now: {len(recipes)}")


if __name__ == "__main__":
    main()
