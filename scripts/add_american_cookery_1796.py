#!/usr/bin/env python3
"""
Add recipes from "American Cookery" by Amelia Simmons (1796)
The First American Cookbook - historical recipes with 18th century language
"""

import json
from pathlib import Path
from datetime import datetime

DATA_DIR = Path(__file__).parent.parent / "data"
RECIPES_FILE = DATA_DIR / "recipes.json"

# Image references for this cookbook
IMAGE_DIR = "The First American Cookbook"
IMAGES = [f"IMG_{i}.PNG" for i in range(5925, 5997)]

def load_recipes():
    with open(RECIPES_FILE, 'r') as f:
        return json.load(f)

def save_recipes(data):
    data['meta']['last_updated'] = datetime.now().strftime('%Y-%m-%d')
    data['meta']['total_recipes'] = len(data['recipes'])
    with open(RECIPES_FILE, 'w') as f:
        json.dump(data, f, indent=2)
    print(f"Saved {len(data['recipes'])} recipes")

def create_recipe(id, title, category, description, ingredients, instructions,
                  source_note, tags, image_refs, notes=None):
    """Create a recipe entry for American Cookery 1796"""
    recipe = {
        "id": id,
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": title,
        "category": category,
        "attribution": "Amelia Simmons",
        "source_note": source_note,
        "description": description,
        "servings_yield": "",
        "prep_time": "",
        "cook_time": "",
        "total_time": "",
        "ingredients": ingredients,
        "instructions": instructions,
        "temperature": "",
        "pan_size": "",
        "notes": notes or ["From American Cookery (1796), the first American cookbook. Language updated from 18th century spelling."],
        "tags": tags,
        "confidence": {
            "overall": "high",
            "flags": ["historical-recipe", "18th-century"]
        },
        "image_refs": image_refs
    }
    return recipe

def main():
    data = load_recipes()
    existing_ids = {r['id'] for r in data['recipes']}
    new_recipes = []

    # ============================================
    # SELECTION GUIDES / TIPS (Reference entries)
    # ============================================

    # 1. Selecting Meat Guide
    if "american-cookery-1796-selecting-meat-guide" not in existing_ids:
        new_recipes.append(create_recipe(
            id="american-cookery-1796-selecting-meat-guide",
            title="Directions for Selecting Meat (1796)",
            category="reference",
            description="Historical guide to selecting quality beef, mutton, lamb, veal, and pork from America's first cookbook.",
            ingredients=[],
            instructions=[
                {"step": 1, "text": "BEEF: The large stall-fed ox beef is the best. It has a coarse open grain and oily smoothness. Dent it with your finger and it will immediately rise again; if old, it will be rough and spongy, and the dent remain. Cow beef is less boned and generally more tender and juicy than the ox in America."},
                {"step": 2, "text": "MUTTON: Grass-fed is good at two or three years old."},
                {"step": 3, "text": "LAMB: If under six months is rich, and no danger of imposition; it may be known by its size."},
                {"step": 4, "text": "VEAL: Is soon lost—great care therefore is necessary in purchasing. Veal brought to market in panniers, or in carriages, is to be preferred to that brought in bags and flouncing on a sweaty horse."},
                {"step": 5, "text": "PORK: Is known by its size and whether properly fattened by its appearance."},
                {"step": 6, "text": "Of almost every species of Animals, Birds and Fishes, the female is the tenderest, the richest flavored, and among poultry the soonest fattened."}
            ],
            source_note="American Cookery by Amelia Simmons (1796), pages 32-33",
            tags=["reference", "guide", "historical", "meat-selection", "1796"],
            image_refs=[f"{IMAGE_DIR}/IMG_5925.PNG", f"{IMAGE_DIR}/IMG_5926.PNG"]
        ))

    # 2. Making Bacon
    if "american-cookery-1796-making-bacon" not in existing_ids:
        new_recipes.append(create_recipe(
            id="american-cookery-1796-making-bacon",
            title="To Make the Best Bacon (1796)",
            category="reference",
            description="Historical method for curing bacon from America's first cookbook.",
            ingredients=[
                {"item": "ham", "quantity": "1", "unit": "each", "prep_note": ""},
                {"item": "saltpetre", "quantity": "1", "unit": "oz", "prep_note": "per ham"},
                {"item": "bay salt", "quantity": "1", "unit": "pint", "prep_note": ""},
                {"item": "molasses", "quantity": "1", "unit": "pint", "prep_note": ""}
            ],
            instructions=[
                {"step": 1, "text": "To each ham put one ounce saltpetre, one pint bay salt, one pint molasses."},
                {"step": 2, "text": "Shake together 6 or 8 weeks, or when a large quantity is together, baste them with the liquor every day."},
                {"step": 3, "text": "When taken out to dry, smoke three weeks with cobs or malt fumes."},
                {"step": 4, "text": "To every ham may be added a cheek, if you stow away a barrel and not alter the composition, some add a shoulder."},
                {"step": 5, "text": "For transportation or exportation, double the period of smoking."}
            ],
            source_note="American Cookery by Amelia Simmons (1796), page 32",
            tags=["preservation", "bacon", "curing", "smoking", "historical", "1796"],
            image_refs=[f"{IMAGE_DIR}/IMG_5926.PNG"]
        ))

    # 3. Fish Selection Guide
    if "american-cookery-1796-selecting-fish-guide" not in existing_ids:
        new_recipes.append(create_recipe(
            id="american-cookery-1796-selecting-fish-guide",
            title="Directions for Selecting Fish (1796)",
            category="reference",
            description="Historical guide to selecting quality fish from America's first cookbook.",
            ingredients=[],
            instructions=[
                {"step": 1, "text": "SALMON: The noblest and richest fish taken in fresh water—the largest are the best. They are unlike almost every other fish, are ameliorated by being 3 or 4 days out of water, if kept from heat and the moon (which has much more injurious effect than the sun)."},
                {"step": 2, "text": "In all great fish-markets, great fish-mongers strictly examine the gills—if the bright redness is exchanged for a low brown, they are stale."},
                {"step": 3, "text": "SHAD: Contrary to the generally received opinion, are not so much richer flavored when first taken out of the water. A Shad 36 or 48 hours out of water may not cook so hard and solid, yet give a higher relished flavor to the taste."},
                {"step": 4, "text": "Every species generally of salt water Fish are best fresh from the water, though Hannah Hill, Black Fish, Lobster, Oyster, Flounder, Bass, Cod, Haddock, and Eel, with many others, may be transported by land many miles, find a good market, and retain a good relish."},
                {"step": 5, "text": "Fresh gills, full bright eyes, moist fins and tails are denotements of their being fresh caught; if they are soft, it's certain they are stale."},
                {"step": 6, "text": "SALMON TROUT: They are best when caught under a fall or cataract—the waters are much colder at the foot of a fall than at the head; Trout choose those waters."},
                {"step": 7, "text": "PERCH AND ROACH: Noble pan fish, the deeper the water from whence taken, the finer are their flavors; if taken from shallow water with muddy bottoms, they are impregnated therewith and are unsavory."},
                {"step": 8, "text": "EELS: Though taken from muddy bottoms, are best to jump in the pan."}
            ],
            source_note="American Cookery by Amelia Simmons (1796), pages 33-34",
            tags=["reference", "guide", "historical", "fish-selection", "1796"],
            image_refs=[f"{IMAGE_DIR}/IMG_5927.PNG", f"{IMAGE_DIR}/IMG_5928.PNG"]
        ))

    # 4. Poultry Selection Guide
    if "american-cookery-1796-selecting-poultry-guide" not in existing_ids:
        new_recipes.append(create_recipe(
            id="american-cookery-1796-selecting-poultry-guide",
            title="Directions for Selecting Poultry (1796)",
            category="reference",
            description="Historical guide to selecting quality poultry and game birds from America's first cookbook.",
            ingredients=[],
            instructions=[
                {"step": 1, "text": "The female in almost every instance is preferable to the male, and peculiarly so in the PEACOCK, which though beautifully plumaged, is tough, hard, stringy, and even indelicious—while the Pea Hen is exactly otherwise, and the queen of all birds."},
                {"step": 2, "text": "TURKEY: Hen turkey is higher and richer flavored, easier fattened and plumper—they are no odds in market."},
                {"step": 3, "text": "CHICKENS: Of either kind are good, and the yellow legged the best, and their taste the sweetest."},
                {"step": 4, "text": "CAPONS: If young are good, are known by short spurs and smooth legs."},
                {"step": 5, "text": "All birds are known, whether fresh killed or stale, by a tight vent in the former, and a loose open vent if old or stale; their smell denotes their goodness; speckled rough legs denote age, while smooth legs and combs prove them young."},
                {"step": 6, "text": "A GOOSE: If young, the bill will be yellow, and will have but few hairs, the bones will crack easily; but if old, the contrary—the bill will be red, and the pads still redder; the joints stiff and difficultly disjointed; if young, otherwise choose one not very fleshy on the breast, but fat in the rump."},
                {"step": 7, "text": "DUCKS: Are similar to geese. WILD DUCKS have redder pads, and smaller than the tame ones, otherwise are like the goose or tame duck, or to be chosen by the same rules."},
                {"step": 8, "text": "WOOD COCKS: Ought to be thick, fat and flesh firm, the nose dry, and throat clear."},
                {"step": 9, "text": "SNIPES: If young and fat, have full veins under the wing, and are small in the veins, otherwise like the Woodcock."},
                {"step": 10, "text": "PARTRIDGES: If young, will have black bills, yellowish legs; if old, the legs look bluish; if old or stale, it may be perceived by smelling at their mouths."},
                {"step": 11, "text": "PIGEONS: Young have light red legs, and the flesh of a colour, and prick easily—old have red legs, blackish in parts, more hairs, plumper and loose vents—so also of grey or green Plover, Black Birds, Thrash, Lark, and wild Fowl in general."}
            ],
            source_note="American Cookery by Amelia Simmons (1796), pages 35-36",
            tags=["reference", "guide", "historical", "poultry-selection", "game-birds", "1796"],
            image_refs=[f"{IMAGE_DIR}/IMG_5929.PNG", f"{IMAGE_DIR}/IMG_5930.PNG"]
        ))

    # 5. Vegetables Selection Guide
    if "american-cookery-1796-selecting-vegetables-guide" not in existing_ids:
        new_recipes.append(create_recipe(
            id="american-cookery-1796-selecting-vegetables-guide",
            title="Directions for Selecting Vegetables (1796)",
            category="reference",
            description="Historical guide to selecting quality vegetables from America's first cookbook.",
            ingredients=[],
            instructions=[
                {"step": 1, "text": "POTATOES: Take rank for universal use, profit and easy acquirement. The smooth skin, known by the name of How's Potatoe, is the most mealy and richest flavored; the yellow rusticoat next best; the red and red rusticoat are tolerable. Those cultivated from imported seed on sandy or dry loomy lands are best for table use. All potatoes should be dug before the rainy seasons in the fall, well dried in the sun, kept from frost and dampness during the winter."},
                {"step": 2, "text": "ONIONS: The Madeira white is best in market, esteemed softer flavored and not so fiery, but the high red, round hard onions are the best; if you consult cheapness, the largest are best."},
                {"step": 3, "text": "BEETS: Grow on any ground, but best on loom or light gravel grounds; the red is the richest and best approved; the white has a fickish sweetness which is disliked by many."},
                {"step": 4, "text": "PARSNIPS: Are a valuable root, cultivated best in rich old grounds, and doubly deep plowed, late sown. They are richer flavored when plowed out of the ground in April, having stood out during the winter."},
                {"step": 5, "text": "CARROTS: Are managed as it respects plowing and rich ground, similarly to Parsnips. The yellow are better than the orange or red; middling sized, a foot long and two inches thick at the top end, are better than over grown ones."},
                {"step": 6, "text": "ASPARAGUS: The mode of cultivation belongs to gardening; the largest is best, the growth of a day sufficient, six inches long, and cut just above the ground."},
                {"step": 7, "text": "LETTUCE: Is of various kinds; the purple spotted leaf is generally the tenderest, and free from bitter—Your taste must guide your market."},
                {"step": 8, "text": "CABBAGE: They are so multifarious that requires a page. Note, all Cabbages have a higher relish that grow on new unmatured grounds."}
            ],
            source_note="American Cookery by Amelia Simmons (1796), pages 37-42",
            tags=["reference", "guide", "historical", "vegetable-selection", "1796"],
            image_refs=[f"{IMAGE_DIR}/IMG_5933.PNG", f"{IMAGE_DIR}/IMG_5934.PNG", f"{IMAGE_DIR}/IMG_5935.PNG", f"{IMAGE_DIR}/IMG_5938.PNG"]
        ))

    # 6. Herbs in Cookery Guide
    if "american-cookery-1796-herbs-guide" not in existing_ids:
        new_recipes.append(create_recipe(
            id="american-cookery-1796-herbs-guide",
            title="Herbs Useful in Cookery (1796)",
            category="reference",
            description="Historical guide to culinary herbs and their uses from America's first cookbook.",
            ingredients=[],
            instructions=[
                {"step": 1, "text": "THYME: Is good in soups and stuffings."},
                {"step": 2, "text": "SWEET MARJORAM: Is used in Turkeys."},
                {"step": 3, "text": "SUMMER SAVORY: Ditto, and in Sausages and salted Beef, and legs of Pork."},
                {"step": 4, "text": "SAGE: Is used in Cheese and Pork, but not generally approved."},
                {"step": 5, "text": "PARSLEY: Good in soups, and to garnish roast Beef, excellent with bread and butter in the spring."},
                {"step": 6, "text": "PENNY ROYAL: Is a high aromatic, although a spontaneous herb in old ploughed fields, yet might be more generally cultivated in gardens, and used in cookery and medicines."},
                {"step": 7, "text": "SWEET THYME: Is most useful and best approved in cookery."}
            ],
            source_note="American Cookery by Amelia Simmons (1796), page 43",
            tags=["reference", "guide", "historical", "herbs", "1796"],
            image_refs=[f"{IMAGE_DIR}/IMG_5941.PNG"]
        ))

    # ============================================
    # MAIN COURSE RECIPES
    # ============================================

    # 7. To Roast Beef
    if "american-cookery-1796-roast-beef" not in existing_ids:
        new_recipes.append(create_recipe(
            id="american-cookery-1796-roast-beef",
            title="To Roast Beef (1796)",
            category="main-dishes",
            description="Historical method for roasting beef from America's first cookbook.",
            ingredients=[
                {"item": "beef", "quantity": "", "unit": "lb", "prep_note": "any cut suitable for roasting"},
                {"item": "salt", "quantity": "", "unit": "", "prep_note": "for basting"},
                {"item": "water", "quantity": "", "unit": "", "prep_note": "for basting"}
            ],
            instructions=[
                {"step": 1, "text": "The general rules are, to have a brisk hot fire, to hang down rather than to spit, to baste with salt and water."},
                {"step": 2, "text": "Allow one quarter of an hour to every pound of beef, though tender beef will require less, while old tough beef will require more roasting."},
                {"step": 3, "text": "Pricking with a fork will determine whether done or not; rare done is the healthiest and the taste of this age."}
            ],
            source_note="American Cookery by Amelia Simmons (1796), page 44",
            tags=["main-dish", "beef", "roast", "historical", "1796"],
            image_refs=[f"{IMAGE_DIR}/IMG_5943.PNG"]
        ))

    # 8. To Roast Mutton
    if "american-cookery-1796-roast-mutton" not in existing_ids:
        new_recipes.append(create_recipe(
            id="american-cookery-1796-roast-mutton",
            title="To Roast Mutton (1796)",
            category="main-dishes",
            description="Historical method for roasting mutton from America's first cookbook.",
            ingredients=[
                {"item": "mutton", "quantity": "", "unit": "", "prep_note": "breast, leg, chine, or saddle"},
                {"item": "horseradish", "quantity": "", "unit": "", "prep_note": "scraped, for garnish"},
                {"item": "potatoes", "quantity": "", "unit": "", "prep_note": "for serving"},
                {"item": "beans", "quantity": "", "unit": "", "prep_note": "for serving"},
                {"item": "colliflowers", "quantity": "", "unit": "", "prep_note": "for serving"}
            ],
            instructions=[
                {"step": 1, "text": "If a breast let it be cauled; if a leg, shuffed or not; let it be done more gently than beef, and done more."},
                {"step": 2, "text": "The chine, saddle or leg require more fire and longer time than the breast."},
                {"step": 3, "text": "Garnish with scraped horseradish, and serve with potatoes, beans, colliflowers, water-cresses, or boiled onion, caper sauce, mashed turnip, or lettuce."}
            ],
            source_note="American Cookery by Amelia Simmons (1796), page 45",
            tags=["main-dish", "mutton", "lamb", "roast", "historical", "1796"],
            image_refs=[f"{IMAGE_DIR}/IMG_5944.PNG"]
        ))

    # 9. To Stuff a Turkey
    if "american-cookery-1796-stuffed-turkey" not in existing_ids:
        new_recipes.append(create_recipe(
            id="american-cookery-1796-stuffed-turkey",
            title="To Stuff and Roast a Turkey (1796)",
            category="main-dishes",
            description="Historical recipe for stuffed roast turkey from America's first cookbook.",
            ingredients=[
                {"item": "turkey", "quantity": "1", "unit": "", "prep_note": ""},
                {"item": "wheat bread", "quantity": "1", "unit": "lb", "prep_note": "soft"},
                {"item": "beef suet", "quantity": "3", "unit": "oz", "prep_note": "or butter"},
                {"item": "eggs", "quantity": "3", "unit": "", "prep_note": ""},
                {"item": "sweet thyme", "quantity": "", "unit": "", "prep_note": "a little"},
                {"item": "sweet marjoram", "quantity": "", "unit": "", "prep_note": ""},
                {"item": "pepper", "quantity": "", "unit": "", "prep_note": "to taste"},
                {"item": "salt", "quantity": "", "unit": "", "prep_note": "to taste"},
                {"item": "wine", "quantity": "1", "unit": "gill", "prep_note": "optional"}
            ],
            instructions=[
                {"step": 1, "text": "Grate a wheat loaf, one quarter of a pound butter, one quarter of a pound salt pork, finely chopped, 2 eggs, a little sweet marjoram, summer savory, parsley and sage, pepper and salt (if the pork be not sufficient), fill the bird and sew up."},
                {"step": 2, "text": "Hang down to a steady solid fire, basting frequently with salt and water, and roast until a steam emits from the breast."},
                {"step": 3, "text": "Put one third of a pound of butter into the gravy, dust flour over the bird and baste with the gravy."},
                {"step": 4, "text": "Serve up with boiled onions and cranberry sauce, mangoes, pickles or celery."},
                {"step": 5, "text": "The same will answer for all Wild Fowl. Water Fowls require onions."}
            ],
            source_note="American Cookery by Amelia Simmons (1796), pages 45-46",
            tags=["main-dish", "turkey", "poultry", "stuffing", "roast", "historical", "1796", "holiday"],
            image_refs=[f"{IMAGE_DIR}/IMG_5944.PNG", f"{IMAGE_DIR}/IMG_5946.PNG"]
        ))

    # 10. Johny Cake or Hoe Cake
    if "american-cookery-1796-johny-cake" not in existing_ids:
        new_recipes.append(create_recipe(
            id="american-cookery-1796-johny-cake",
            title="Johny Cake, or Hoe Cake (1796)",
            category="breads",
            description="America's original Johnny Cake recipe from the first American cookbook.",
            ingredients=[
                {"item": "milk", "quantity": "1", "unit": "pint", "prep_note": "scalded"},
                {"item": "Indian meal", "quantity": "3", "unit": "pints", "prep_note": "cornmeal"},
                {"item": "flour", "quantity": "0.5", "unit": "pint", "prep_note": ""}
            ],
            instructions=[
                {"step": 1, "text": "Scald 1 pint of milk and put to 3 pints of Indian meal, and half pint of flour—bake before the fire."},
                {"step": 2, "text": "Or scald with milk two thirds of the Indian meal, or wet two thirds with boiling water, add salt, molasses and shortening, work up with cold water pretty stiff, and bake as above."}
            ],
            source_note="American Cookery by Amelia Simmons (1796), page 61",
            tags=["bread", "cornmeal", "johnny-cake", "historical", "1796", "american-classic"],
            image_refs=[f"{IMAGE_DIR}/IMG_5969.PNG"],
            notes=["This is one of the earliest published recipes for Johnny Cake, a quintessentially American bread.", "From American Cookery (1796), the first American cookbook."]
        ))

    # 11. Indian Slapjack
    if "american-cookery-1796-indian-slapjack" not in existing_ids:
        new_recipes.append(create_recipe(
            id="american-cookery-1796-indian-slapjack",
            title="Indian Slapjack (1796)",
            category="breads",
            description="Early American pancake recipe from the first American cookbook.",
            ingredients=[
                {"item": "milk", "quantity": "1", "unit": "quart", "prep_note": ""},
                {"item": "Indian meal", "quantity": "1", "unit": "pint", "prep_note": "cornmeal"},
                {"item": "eggs", "quantity": "4", "unit": "", "prep_note": ""},
                {"item": "flour", "quantity": "4", "unit": "spoons", "prep_note": ""},
                {"item": "salt", "quantity": "", "unit": "", "prep_note": "a little"}
            ],
            instructions=[
                {"step": 1, "text": "One quart of milk, 1 pint of Indian meal, 4 eggs, 4 spoons of flour, little salt, beat together."},
                {"step": 2, "text": "Baked on griddles, or fry in a dry pan, or baked in a pan which has been rubbed with suet, lard or butter."}
            ],
            source_note="American Cookery by Amelia Simmons (1796), page 61",
            tags=["bread", "pancake", "cornmeal", "breakfast", "historical", "1796"],
            image_refs=[f"{IMAGE_DIR}/IMG_5969.PNG"]
        ))

    # 12. Pumpkin Pudding No. 1
    if "american-cookery-1796-pumpkin-pudding" not in existing_ids:
        new_recipes.append(create_recipe(
            id="american-cookery-1796-pumpkin-pudding",
            title="Pompkin Pudding No. 1 (1796)",
            category="desserts",
            description="One of the earliest published pumpkin pie recipes from America's first cookbook.",
            ingredients=[
                {"item": "pumpkin", "quantity": "1", "unit": "quart", "prep_note": "stewed and strained"},
                {"item": "cream", "quantity": "3", "unit": "pints", "prep_note": ""},
                {"item": "eggs", "quantity": "9", "unit": "", "prep_note": "beaten"},
                {"item": "sugar", "quantity": "", "unit": "", "prep_note": "to taste"},
                {"item": "mace", "quantity": "", "unit": "", "prep_note": "to taste"},
                {"item": "nutmeg", "quantity": "", "unit": "", "prep_note": "to taste"},
                {"item": "ginger", "quantity": "", "unit": "", "prep_note": "to taste"}
            ],
            instructions=[
                {"step": 1, "text": "One quart stewed and strained pumpkin, 3 pints cream, 9 beaten eggs, sugar, mace, nutmeg and ginger."},
                {"step": 2, "text": "Laid into paste No. 7 or 3, and with a dough spur, cross and chequer it."},
                {"step": 3, "text": "Bake in dishes three quarters of an hour."}
            ],
            source_note="American Cookery by Amelia Simmons (1796), page 55",
            tags=["dessert", "pudding", "pie", "pumpkin", "historical", "1796", "american-classic", "holiday"],
            image_refs=[f"{IMAGE_DIR}/IMG_5960.PNG"],
            notes=["This is one of the earliest published pumpkin pie recipes in America.", "The word 'pompkin' was common spelling in 1796.", "From American Cookery (1796), the first American cookbook."]
        ))

    # 13. Pumpkin Pudding No. 2
    if "american-cookery-1796-pumpkin-pudding-2" not in existing_ids:
        new_recipes.append(create_recipe(
            id="american-cookery-1796-pumpkin-pudding-2",
            title="Pompkin Pudding No. 2 (1796)",
            category="desserts",
            description="A simpler pumpkin pie variation from America's first cookbook.",
            ingredients=[
                {"item": "milk", "quantity": "1", "unit": "quart", "prep_note": ""},
                {"item": "pumpkin", "quantity": "1", "unit": "pint", "prep_note": ""},
                {"item": "eggs", "quantity": "4", "unit": "", "prep_note": ""},
                {"item": "molasses", "quantity": "", "unit": "", "prep_note": "to taste"},
                {"item": "allspice", "quantity": "", "unit": "", "prep_note": "to taste"},
                {"item": "ginger", "quantity": "", "unit": "", "prep_note": "to taste"}
            ],
            instructions=[
                {"step": 1, "text": "One quart of milk, 1 pint pumpkin, 4 eggs, molasses, allspice and ginger in a crust."},
                {"step": 2, "text": "Bake 1 hour."}
            ],
            source_note="American Cookery by Amelia Simmons (1796), page 55",
            tags=["dessert", "pudding", "pie", "pumpkin", "historical", "1796"],
            image_refs=[f"{IMAGE_DIR}/IMG_5960.PNG"]
        ))

    # 14. Apple Pie
    if "american-cookery-1796-apple-pie" not in existing_ids:
        new_recipes.append(create_recipe(
            id="american-cookery-1796-apple-pie",
            title="Apple Pie (1796)",
            category="desserts",
            description="Traditional apple pie recipe from America's first cookbook.",
            ingredients=[
                {"item": "apples", "quantity": "3", "unit": "pints", "prep_note": "stewed and strained"},
                {"item": "lemon peel", "quantity": "1", "unit": "", "prep_note": "fresh, grated"},
                {"item": "cinnamon", "quantity": "", "unit": "", "prep_note": "to taste"},
                {"item": "mace", "quantity": "", "unit": "", "prep_note": "to taste"},
                {"item": "rose-water", "quantity": "", "unit": "", "prep_note": "to taste"},
                {"item": "sugar", "quantity": "", "unit": "", "prep_note": "to taste"}
            ],
            instructions=[
                {"step": 1, "text": "Stew and strain the apples."},
                {"step": 2, "text": "To every three pints, grate the peel of a fresh lemon, add cinnamon, mace, rose-water and sugar to your taste."},
                {"step": 3, "text": "Bake in paste No. 3."},
                {"step": 4, "text": "Every species of fruit such as peas, plums, raspberries, black berries may be only sweetened, without spices—and bake in paste No. 3."}
            ],
            source_note="American Cookery by Amelia Simmons (1796), page 52",
            tags=["dessert", "pie", "apple", "fruit", "historical", "1796"],
            image_refs=[f"{IMAGE_DIR}/IMG_5955.PNG"]
        ))

    # 15. Indian Pudding No. 1
    if "american-cookery-1796-indian-pudding" not in existing_ids:
        new_recipes.append(create_recipe(
            id="american-cookery-1796-indian-pudding",
            title="A Nice Indian Pudding No. 1 (1796)",
            category="desserts",
            description="Traditional Indian pudding (cornmeal pudding) from America's first cookbook.",
            ingredients=[
                {"item": "milk", "quantity": "3", "unit": "pints", "prep_note": "scalded"},
                {"item": "Indian meal", "quantity": "7", "unit": "spoons", "prep_note": "fine cornmeal"},
                {"item": "eggs", "quantity": "7", "unit": "", "prep_note": ""},
                {"item": "raisins", "quantity": "0.5", "unit": "lb", "prep_note": ""},
                {"item": "butter", "quantity": "4", "unit": "oz", "prep_note": ""},
                {"item": "spice", "quantity": "", "unit": "", "prep_note": "to taste"},
                {"item": "sugar", "quantity": "", "unit": "", "prep_note": "to taste"}
            ],
            instructions=[
                {"step": 1, "text": "3 pints scalded milk, 7 spoons fine Indian meal, stir well together while hot, let stand till cooled."},
                {"step": 2, "text": "Add 7 eggs, half pound raisins, 4 ounces butter, spice and sugar."},
                {"step": 3, "text": "Bake one and half hour."}
            ],
            source_note="American Cookery by Amelia Simmons (1796), page 53",
            tags=["dessert", "pudding", "cornmeal", "historical", "1796", "american-classic"],
            image_refs=[f"{IMAGE_DIR}/IMG_5957.PNG"]
        ))

    # 16. Rice Pudding No. 1
    if "american-cookery-1796-rice-pudding" not in existing_ids:
        new_recipes.append(create_recipe(
            id="american-cookery-1796-rice-pudding",
            title="A Rice Pudding No. 1 (1796)",
            category="desserts",
            description="Traditional rice pudding from America's first cookbook.",
            ingredients=[
                {"item": "rice", "quantity": "0.25", "unit": "lb", "prep_note": ""},
                {"item": "cinnamon", "quantity": "1", "unit": "stick", "prep_note": ""},
                {"item": "milk", "quantity": "1", "unit": "quart", "prep_note": ""},
                {"item": "nutmeg", "quantity": "0.5", "unit": "", "prep_note": ""},
                {"item": "rose-water", "quantity": "4", "unit": "spoons", "prep_note": ""},
                {"item": "eggs", "quantity": "8", "unit": "", "prep_note": ""},
                {"item": "butter", "quantity": "", "unit": "", "prep_note": "for puff paste dish"}
            ],
            instructions=[
                {"step": 1, "text": "One quarter of a pound rice, a stick of cinnamon, to a quart of milk (stirred often to keep from burning)."},
                {"step": 2, "text": "Boil quick, cool and add half a nutmeg, 4 spoons rose-water, 8 eggs."},
                {"step": 3, "text": "Butter or puff paste a dish and pour the above composition into it."},
                {"step": 4, "text": "Bake one and half hour."}
            ],
            source_note="American Cookery by Amelia Simmons (1796), page 52",
            tags=["dessert", "pudding", "rice", "historical", "1796"],
            image_refs=[f"{IMAGE_DIR}/IMG_5956.PNG"]
        ))

    # 17. Cookies
    if "american-cookery-1796-cookies" not in existing_ids:
        new_recipes.append(create_recipe(
            id="american-cookery-1796-cookies",
            title="Cookies (1796)",
            category="desserts",
            description="One of the earliest published cookie recipes in America, from the first American cookbook.",
            ingredients=[
                {"item": "sugar", "quantity": "1", "unit": "lb", "prep_note": "boiled slowly in half pint water"},
                {"item": "pearl ash", "quantity": "2", "unit": "tsp", "prep_note": "dissolved in milk"},
                {"item": "flour", "quantity": "2.5", "unit": "lb", "prep_note": ""},
                {"item": "butter", "quantity": "4", "unit": "oz", "prep_note": ""},
                {"item": "coriander seed", "quantity": "2", "unit": "spoons", "prep_note": "finely powdered"}
            ],
            instructions=[
                {"step": 1, "text": "One pound sugar boiled slowly in half pint water, scum well and cool."},
                {"step": 2, "text": "Add two tea spoons pearl ash dissolved in milk, then two and half pounds flour, rub in 4 ounces butter, and two large spoons of finely powdered coriander seed, wet with above."},
                {"step": 3, "text": "Make roles half an inch thick and cut to the shape you please."},
                {"step": 4, "text": "Bake fifteen or twenty minutes in a slack oven—good three weeks."}
            ],
            source_note="American Cookery by Amelia Simmons (1796), page 63",
            tags=["dessert", "cookies", "baking", "historical", "1796", "american-classic"],
            image_refs=[f"{IMAGE_DIR}/IMG_5971.PNG"],
            notes=["This is one of the earliest published cookie recipes in America.", "Pearl ash (potassium carbonate) was an early leavening agent.", "From American Cookery (1796), the first American cookbook."]
        ))

    # 18. Christmas Cookey
    if "american-cookery-1796-christmas-cookies" not in existing_ids:
        new_recipes.append(create_recipe(
            id="american-cookery-1796-christmas-cookies",
            title="Christmas Cookey (1796)",
            category="desserts",
            description="Historic Christmas cookie recipe from America's first cookbook.",
            ingredients=[
                {"item": "flour", "quantity": "3", "unit": "lb", "prep_note": ""},
                {"item": "coriander seed", "quantity": "1", "unit": "tsp", "prep_note": "fine powdered"},
                {"item": "butter", "quantity": "1", "unit": "lb", "prep_note": ""},
                {"item": "sugar", "quantity": "1.5", "unit": "lb", "prep_note": ""},
                {"item": "pearl ash", "quantity": "3", "unit": "tsp", "prep_note": "dissolved in milk"}
            ],
            instructions=[
                {"step": 1, "text": "To three pound flour, sprinkle a tea cup of fine powdered coriander seed, rub in one pound butter."},
                {"step": 2, "text": "Add one and half pound sugar, dissolve three tea spoons of pearl ash in a tea cup of milk."},
                {"step": 3, "text": "Kneed all together well, roll three quarters of an inch thick, and cut or stamp into shape and size you please."},
                {"step": 4, "text": "Bake slowly fifteen or twenty minutes; though hard and dry at first, if put into an earthern pot, and dry cellar, or damp room, they will be finer, softer and better when six months old."}
            ],
            source_note="American Cookery by Amelia Simmons (1796), page 63",
            tags=["dessert", "cookies", "christmas", "holiday", "historical", "1796"],
            image_refs=[f"{IMAGE_DIR}/IMG_5971.PNG"]
        ))

    # 19. Gingerbread
    if "american-cookery-1796-gingerbread" not in existing_ids:
        new_recipes.append(create_recipe(
            id="american-cookery-1796-gingerbread",
            title="Molasses Gingerbread (1796)",
            category="desserts",
            description="Traditional molasses gingerbread from America's first cookbook.",
            ingredients=[
                {"item": "cinnamon", "quantity": "1", "unit": "tbsp", "prep_note": ""},
                {"item": "allspice", "quantity": "", "unit": "", "prep_note": "or some coriander"},
                {"item": "pearl ash", "quantity": "4", "unit": "tsp", "prep_note": "dissolved in half pint water"},
                {"item": "flour", "quantity": "4", "unit": "lb", "prep_note": ""},
                {"item": "molasses", "quantity": "1", "unit": "quart", "prep_note": ""},
                {"item": "butter", "quantity": "4", "unit": "oz", "prep_note": "in summer rub in the butter, if in winter warm the butter and molasses"}
            ],
            instructions=[
                {"step": 1, "text": "One table spoon of cinnamon, some coriander or allspice, put to four tea spoons pearl ash dissolved in half pint water."},
                {"step": 2, "text": "Add four pound flour, one quart molasses, four ounces butter (if in summer rub in the butter, if in winter warm the butter and molasses and pour to the spiced flour)."},
                {"step": 3, "text": "Knead well 'till stiff, the more the better, the lighter and whiter it will be."},
                {"step": 4, "text": "Bake brisk fifteen minutes; don't scorch."},
                {"step": 5, "text": "Before it is put in, wash it with whites and sugar beat together."}
            ],
            source_note="American Cookery by Amelia Simmons (1796), page 64",
            tags=["dessert", "gingerbread", "molasses", "spiced", "historical", "1796"],
            image_refs=[f"{IMAGE_DIR}/IMG_5972.PNG"]
        ))

    # 20. Pound Cake
    if "american-cookery-1796-pound-cake" not in existing_ids:
        new_recipes.append(create_recipe(
            id="american-cookery-1796-pound-cake",
            title="Pound Cake (1796)",
            category="desserts",
            description="Traditional pound cake from America's first cookbook.",
            ingredients=[
                {"item": "sugar", "quantity": "1", "unit": "lb", "prep_note": ""},
                {"item": "butter", "quantity": "1", "unit": "lb", "prep_note": ""},
                {"item": "flour", "quantity": "1", "unit": "lb", "prep_note": ""},
                {"item": "eggs", "quantity": "10", "unit": "", "prep_note": "or one pound"},
                {"item": "rose water", "quantity": "1", "unit": "gill", "prep_note": ""},
                {"item": "spices", "quantity": "", "unit": "", "prep_note": "to your taste"}
            ],
            instructions=[
                {"step": 1, "text": "One pound sugar, one pound butter, one pound flour, one pound or ten eggs."},
                {"step": 2, "text": "Add rose water one gill, spices to your taste."},
                {"step": 3, "text": "Watch it well, it will bake in a slow oven in 15 minutes."}
            ],
            source_note="American Cookery by Amelia Simmons (1796), page 64",
            tags=["dessert", "cake", "pound-cake", "historical", "1796"],
            image_refs=[f"{IMAGE_DIR}/IMG_5973.PNG", f"{IMAGE_DIR}/IMG_5974.PNG"]
        ))

    # 21. Spruce Beer
    if "american-cookery-1796-spruce-beer" not in existing_ids:
        new_recipes.append(create_recipe(
            id="american-cookery-1796-spruce-beer",
            title="For Brewing Spruce Beer (1796)",
            category="beverages",
            description="Historic spruce beer recipe from America's first cookbook.",
            ingredients=[
                {"item": "hops", "quantity": "4", "unit": "oz", "prep_note": ""},
                {"item": "water", "quantity": "1", "unit": "gallon", "prep_note": "for boiling hops"},
                {"item": "warm water", "quantity": "16", "unit": "gallons", "prep_note": ""},
                {"item": "molasses", "quantity": "2", "unit": "gallons", "prep_note": ""},
                {"item": "essence of spruce", "quantity": "8", "unit": "oz", "prep_note": "dissolved in one quart water"},
                {"item": "emptins (yeast)", "quantity": "0.5", "unit": "pint", "prep_note": ""}
            ],
            instructions=[
                {"step": 1, "text": "Take four ounces of hops, let them boil half an hour in one gallon of water, strain the hop water."},
                {"step": 2, "text": "Then add sixteen gallons of warm water, two gallons of molasses, eight ounces of essence of spruce dissolved in one quart of water."},
                {"step": 3, "text": "Put it in a clean cask, then shake it well together, add half a pint of emptins (yeast)."},
                {"step": 4, "text": "Then let it stand and work one week. If very warm weather less time will do."},
                {"step": 5, "text": "When it is drawn off to bottle, add one spoonful of molasses to every bottle."}
            ],
            source_note="American Cookery by Amelia Simmons (1796), page 75",
            tags=["beverage", "beer", "spruce", "brewing", "historical", "1796"],
            image_refs=[f"{IMAGE_DIR}/IMG_5990.PNG"]
        ))

    # 22. Emptins (Yeast)
    if "american-cookery-1796-emptins" not in existing_ids:
        new_recipes.append(create_recipe(
            id="american-cookery-1796-emptins",
            title="Emptins (Homemade Yeast) (1796)",
            category="reference",
            description="Historic recipe for making emptins (homemade yeast) from America's first cookbook.",
            ingredients=[
                {"item": "hops", "quantity": "1", "unit": "handful", "prep_note": ""},
                {"item": "water", "quantity": "3", "unit": "quarts", "prep_note": ""}
            ],
            instructions=[
                {"step": 1, "text": "Take a handful of hops and about three quarts of water, let it boil about fifteen minutes."},
                {"step": 2, "text": "Then make a thickening as you do for starch, strain the liquor."},
                {"step": 3, "text": "When cold put a little emptins (yeast) to work them."},
                {"step": 4, "text": "They will keep well corked in a bottle five or six weeks."}
            ],
            source_note="American Cookery by Amelia Simmons (1796), page 76",
            tags=["reference", "yeast", "baking", "historical", "1796"],
            image_refs=[f"{IMAGE_DIR}/IMG_5991.PNG"],
            notes=["Emptins was the 18th century term for homemade yeast.", "From American Cookery (1796), the first American cookbook."]
        ))

    # 23. 1796 Cooking Glossary
    if "american-cookery-1796-glossary" not in existing_ids:
        new_recipes.append(create_recipe(
            id="american-cookery-1796-glossary",
            title="Glossary of 18th Century Cooking Terms (1796)",
            category="reference",
            description="Glossary of historical cooking terms from America's first cookbook.",
            ingredients=[],
            instructions=[
                {"step": 1, "text": "AMBER GUM: Probably ambergris, the wax-like secretion of the sperm whale, now used in perfumery, formerly in cookery."},
                {"step": 2, "text": "BELL-METAL: The metallic substance of which bells are made."},
                {"step": 3, "text": "BLADDER AND LEATHER: Pieces of each substance to be tied over the mouths of jars and bottles to secure the contents against air."},
                {"step": 4, "text": "BULLACE: A small wild or semi-domesticated plum."},
                {"step": 5, "text": "CALAVANCE (CALIVANSE): The name for certain varieties of pulse; here, an early variety of bean."},
                {"step": 6, "text": "CALIPASH: That part of the turtle adjoining the upper shell."},
                {"step": 7, "text": "CALIPEE: That part of the turtle adjoining the lower shell."},
                {"step": 8, "text": "CAUL: An enveloping membrane."},
                {"step": 9, "text": "CHINE: A 'joint' made up of part of the backbone and adjoining flesh."},
                {"step": 10, "text": "COB: Corn cob."},
                {"step": 11, "text": "DO.: Abbreviation for ditto."},
                {"step": 12, "text": "EMPTINS: Semiliquid prepared yeast."},
                {"step": 13, "text": "FAIR: (of water) clean; pure."},
                {"step": 14, "text": "FROST GRAPE: A native American species, also called 'chicken grape'."},
                {"step": 15, "text": "FROWY, FROUGHY: Stale; sour; musty."},
                {"step": 16, "text": "FRUMENTY: Hulled wheat cooked in milk and seasoned with spice, sugar, etc."},
                {"step": 17, "text": "GALLIPOT: A small earthen pot."},
                {"step": 18, "text": "HASLET, HARSLET (HEARTSLET): Edible entrails; liver, heart, etc."},
                {"step": 19, "text": "JAGGING IRON or DOUGHSPUR: An instrument used for ornamenting pastry, in the form of a toothed wheel set in a handle."},
                {"step": 20, "text": "JUMP IN THE PAN: A characteristic action of eels while in the process of cooking."},
                {"step": 21, "text": "LADE: To transfer as with a ladle or scoop."},
                {"step": 22, "text": "MANGO: A pickled green melon stuffed with various condiments."},
                {"step": 23, "text": "NEAT'S FOOT: The foot of an ox."},
                {"step": 24, "text": "ORANGE FLOWER WATER: A liquid distilled from orange blossoms."},
                {"step": 25, "text": "PANNIKIN: A small metal vessel."},
                {"step": 26, "text": "PEARLASH: A salt obtained from the ashes of plants (potassium carbonate, an early leavening agent)."},
                {"step": 27, "text": "PIPPIN: A variety of apple."},
                {"step": 28, "text": "Q.S. (QUANTUM SUFFICIT): As much as suffices."},
                {"step": 29, "text": "RACE: A root (as in 'a race of ginger')."},
                {"step": 30, "text": "RUN OUT or DEPRECIATE: To decline in quality with each planting."},
                {"step": 31, "text": "SCUM: To skim."},
                {"step": 32, "text": "SYLLABUB, SILLABUB: A mixture of milk or cream with wine, cider, or other acid, usually whipped to a froth."},
                {"step": 33, "text": "WALLOP: A bubbling motion made by rapidly boiling water, hence the duration of one such motion used as a measure of time in cooking."}
            ],
            source_note="American Cookery by Amelia Simmons (1796), pages 79-80",
            tags=["reference", "glossary", "historical", "terminology", "1796"],
            image_refs=[f"{IMAGE_DIR}/IMG_5994.PNG", f"{IMAGE_DIR}/IMG_5995.PNG", f"{IMAGE_DIR}/IMG_5996.PNG"]
        ))

    # 24. To Preserve Quinces
    if "american-cookery-1796-preserved-quinces" not in existing_ids:
        new_recipes.append(create_recipe(
            id="american-cookery-1796-preserved-quinces",
            title="For Preserving Quinces (1796)",
            category="preserves",
            description="Historic quince preserving recipe from America's first cookbook.",
            ingredients=[
                {"item": "quinces", "quantity": "1", "unit": "peck", "prep_note": "pared, cored"},
                {"item": "frost grapes", "quantity": "2", "unit": "lb", "prep_note": "parings and cores"},
                {"item": "water", "quantity": "3", "unit": "quarts", "prep_note": ""},
                {"item": "sugar", "quantity": "1.25", "unit": "lb", "prep_note": "per pound of quince"}
            ],
            instructions=[
                {"step": 1, "text": "Take a peck of Quinces, pare them, take out the core with a sharp knife."},
                {"step": 2, "text": "If you wish to have them whole, boil parings and cores with two pound frost grapes in 3 quarts water, boil the liquor an hour and an half, or till it is thick."},
                {"step": 3, "text": "Strain it through a coarse hair sieve, add one and a quarter pound sugar to every pound of quince."},
                {"step": 4, "text": "Put the sugar into the syrup, scald and skim it till it is clear."},
                {"step": 5, "text": "Put the quinces into the syrup, hang them over a gentle fire for five hours, then put them in a stone pot for use, set them in a dry cool place."}
            ],
            source_note="American Cookery by Amelia Simmons (1796), pages 66-67",
            tags=["preserves", "quince", "fruit", "historical", "1796"],
            image_refs=[f"{IMAGE_DIR}/IMG_5977.PNG"]
        ))

    # 25. To Pickle Cucumbers
    if "american-cookery-1796-pickled-cucumbers" not in existing_ids:
        new_recipes.append(create_recipe(
            id="american-cookery-1796-pickled-cucumbers",
            title="To Pickle Cucumbers (1796)",
            category="preserves",
            description="Historic cucumber pickle recipe from America's first cookbook.",
            ingredients=[
                {"item": "cucumbers", "quantity": "", "unit": "", "prep_note": "small, fresh gathered, free from spots"},
                {"item": "salt", "quantity": "", "unit": "", "prep_note": "for brine, strong enough to bear an egg"},
                {"item": "water", "quantity": "", "unit": "", "prep_note": ""},
                {"item": "white wine vinegar", "quantity": "", "unit": "", "prep_note": "the best"},
                {"item": "cloves", "quantity": "", "unit": "", "prep_note": "sliced"},
                {"item": "mace", "quantity": "", "unit": "", "prep_note": ""},
                {"item": "nutmeg", "quantity": "", "unit": "", "prep_note": ""},
                {"item": "white pepper corns", "quantity": "", "unit": "", "prep_note": ""},
                {"item": "long pepper", "quantity": "", "unit": "", "prep_note": ""},
                {"item": "ginger", "quantity": "", "unit": "", "prep_note": "races of"}
            ],
            instructions=[
                {"step": 1, "text": "Let your cucumbers be small, fresh gathered, and free from spots."},
                {"step": 2, "text": "Then make a pickle of salt and water, strong enough to bear an egg."},
                {"step": 3, "text": "Boil the pickle and skim it well, and then pour it upon your cucumbers, and stive them down for twenty four hours."},
                {"step": 4, "text": "Then strain them out into a cullender, and dry them well with a cloth."},
                {"step": 5, "text": "Take the best white wine vinegar, with cloves, sliced mace, nutmeg, white pepper corns, long pepper, and races of ginger (as much as you please), boil them up together."},
                {"step": 6, "text": "Then clap the cucumbers in, with a few vine leaves, and a little salt, and as soon as they begin to turn their colour, put them into jars, stive them down close, and when cold, tie on a bladder and leather."}
            ],
            source_note="American Cookery by Amelia Simmons (1796), pages 73-74",
            tags=["preserves", "pickles", "cucumber", "historical", "1796"],
            image_refs=[f"{IMAGE_DIR}/IMG_5985.PNG", f"{IMAGE_DIR}/IMG_5986.PNG"]
        ))

    # 26. Currant Jelly
    if "american-cookery-1796-currant-jelly" not in existing_ids:
        new_recipes.append(create_recipe(
            id="american-cookery-1796-currant-jelly",
            title="Currant Jelly (1796)",
            category="preserves",
            description="Historic currant jelly recipe from America's first cookbook.",
            ingredients=[
                {"item": "currants", "quantity": "", "unit": "", "prep_note": "stripped from stalks"},
                {"item": "sugar", "quantity": "1", "unit": "lb", "prep_note": "per pint of juice"}
            ],
            instructions=[
                {"step": 1, "text": "Having stripped the currants from the stalks, put them in a stone jar, stop it close."},
                {"step": 2, "text": "Set it in a kettle of boiling water, half way the jar, let it boil half an hour."},
                {"step": 3, "text": "Take it out and strain the juice through a coarse hair sieve."},
                {"step": 4, "text": "To a pint of juice put a pound of sugar, set it over a fine quick fire in a preserving pan, or a bell-metal skillet."},
                {"step": 5, "text": "Keep stirring it all the time till the sugar be melted, then skim the scum off as fast as it rises."},
                {"step": 6, "text": "When the jelly is very clear and fine, pour it into earthen or china cups, when cold, cut white papers just the bigness of the top of the pot, and lay on the jelly."},
                {"step": 7, "text": "Dip those papers in brandy, then cover the top of the pot and prick it full of holes, set it in a dry place; you may put some into glasses for present use."}
            ],
            source_note="American Cookery by Amelia Simmons (1796), page 71",
            tags=["preserves", "jelly", "currant", "fruit", "historical", "1796"],
            image_refs=[f"{IMAGE_DIR}/IMG_5983.PNG"]
        ))

    # Add all new recipes
    if new_recipes:
        data['recipes'].extend(new_recipes)
        print(f"Added {len(new_recipes)} recipes from American Cookery (1796)")
        save_recipes(data)
    else:
        print("No new recipes to add - all already exist")

    return len(new_recipes)

if __name__ == "__main__":
    count = main()
    print(f"\nTotal new recipes added: {count}")
