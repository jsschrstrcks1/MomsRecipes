#!/usr/bin/env python3
"""
Add missing BHG (Better Homes and Gardens) recipes that were found
in unreferenced images during the image-by-image audit.

These recipes were on images that existed but were never incorporated
into recipes.json.
"""

import json
from pathlib import Path

RECIPES_FILE = Path(__file__).parent.parent / "data" / "recipes.json"

MISSING_RECIPES = [
    # From IMG_5395 Large.jpeg (page 235)
    {
        "id": "ham-with-pineapple-sauce-bhg",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Ham with Pineapple Sauce",
        "category": "main-dishes",
        "attribution": "Better Homes and Gardens",
        "source_note": "BHG Cookbook - Meat section",
        "description": "Baked ham glazed with a sweet pineapple sauce.",
        "servings_yield": "4-6 servings",
        "ingredients": [
            {"item": "fully cooked ham", "quantity": "4-6", "unit": "lb"},
            {"item": "pineapple juice", "quantity": "1/2", "unit": "cup"},
            {"item": "orange marmalade", "quantity": "1/4", "unit": "cup"},
            {"item": "prepared mustard", "quantity": "2", "unit": "tsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Place ham in a shallow baking pan."},
            {"step": 2, "text": "Bake in 325°F oven for 1 1/4 to 2 1/4 hours."},
            {"step": 3, "text": "Meanwhile combine pineapple juice, marmalade, and mustard."},
            {"step": 4, "text": "Brush ham with glaze during last 30 minutes of baking."}
        ],
        "temperature": "325°F (165°C)",
        "tags": ["ham", "pineapple", "glaze", "main dish", "bhg"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": ["IMG_5395 Large.jpeg"]
    },
    {
        "id": "ham-caribbean-bhg",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Ham Caribbean",
        "category": "main-dishes",
        "attribution": "Better Homes and Gardens",
        "source_note": "BHG Cookbook - Meat section",
        "description": "Ham baked with tropical fruit flavors including pineapple, orange juice, and rum.",
        "servings_yield": "6-8 servings",
        "ingredients": [
            {"item": "fully cooked center-cut ham slice", "quantity": "1 1/2", "unit": "lb", "prep_note": "cut 1 inch thick"},
            {"item": "canned pineapple chunks", "quantity": "8", "unit": "oz", "prep_note": "juice pack"},
            {"item": "packed brown sugar", "quantity": "1/4", "unit": "cup"},
            {"item": "ground cloves or nutmeg", "quantity": "1/8", "unit": "tsp"},
            {"item": "orange juice", "quantity": "1/3", "unit": "cup"},
            {"item": "light rum", "quantity": "2", "unit": "tbsp"},
            {"item": "light raisins", "quantity": "1/4", "unit": "cup"}
        ],
        "instructions": [
            {"step": 1, "text": "Trim fat from ham. Place ham on rack in shallow baking pan."},
            {"step": 2, "text": "Slash edges of ham at 1-inch intervals."},
            {"step": 3, "text": "Bake in 350°F oven for 30 minutes."},
            {"step": 4, "text": "Meanwhile, drain pineapple; combine juice with brown sugar, cornstarch, and cloves."},
            {"step": 5, "text": "Add orange juice, and if using, rum. Cook and stir till thickened."},
            {"step": 6, "text": "Add pineapple chunks. Simmer in pineapple mixture and cloves."},
            {"step": 7, "text": "Spoon over ham during last 10 minutes of baking."}
        ],
        "temperature": "350°F (175°C)",
        "tags": ["ham", "caribbean", "pineapple", "main dish", "bhg"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": ["IMG_5395 Large.jpeg"]
    },
    # From IMG_5408 Large.jpeg (page 248)
    {
        "id": "meat-corn-bread-squares-bhg",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Meat and Corn Bread Squares",
        "category": "main-dishes",
        "attribution": "Better Homes and Gardens",
        "source_note": "BHG Cookbook - Meat section",
        "description": "Ground beef topped with cornbread, baked until golden.",
        "servings_yield": "6 servings",
        "ingredients": [
            {"item": "ground beef", "quantity": "1", "unit": "lb"},
            {"item": "chopped onion", "quantity": "1/2", "unit": "cup"},
            {"item": "chili powder", "quantity": "1", "unit": "tsp"},
            {"item": "garlic salt", "quantity": "1/4", "unit": "tsp"},
            {"item": "stewed tomatoes", "quantity": "16", "unit": "oz"},
            {"item": "kidney beans", "quantity": "15", "unit": "oz", "prep_note": "drained"},
            {"item": "shredded cheddar cheese", "quantity": "1/2", "unit": "cup"},
            {"item": "cornmeal", "quantity": "3/4", "unit": "cup"},
            {"item": "all-purpose flour", "quantity": "3/4", "unit": "cup"},
            {"item": "baking powder", "quantity": "1", "unit": "tbsp"},
            {"item": "milk", "quantity": "2/3", "unit": "cup"},
            {"item": "beaten egg", "quantity": "1", "unit": ""},
            {"item": "cooking oil", "quantity": "2", "unit": "tbsp"}
        ],
        "instructions": [
            {"step": 1, "text": "In skillet cook beef and onion till brown. Drain fat."},
            {"step": 2, "text": "Stir in chili powder and garlic salt."},
            {"step": 3, "text": "Add undrained tomatoes and beans. Bring to boiling."},
            {"step": 4, "text": "Transfer to 9x9x2-inch baking dish. Top with cheese."},
            {"step": 5, "text": "Combine cornmeal, flour, and baking powder."},
            {"step": 6, "text": "Mix milk, egg, and oil; add to dry ingredients. Stir just till moistened."},
            {"step": 7, "text": "Spread over meat mixture."},
            {"step": 8, "text": "Bake at 425°F for 20 to 25 minutes or till golden."}
        ],
        "temperature": "425°F (220°C)",
        "cook_time": "20-25 minutes",
        "tags": ["ground beef", "cornbread", "casserole", "main dish", "bhg"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": ["IMG_5408 Large.jpeg"]
    },
    {
        "id": "meat-pasta-bake-bhg",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Meat and Pasta Bake",
        "category": "main-dishes",
        "attribution": "Better Homes and Gardens",
        "source_note": "BHG Cookbook - Meat section (EASY)",
        "description": "Easy casserole with ground beef, pasta, and cheese.",
        "servings_yield": "6 servings",
        "ingredients": [
            {"item": "elbow macaroni", "quantity": "4", "unit": "oz"},
            {"item": "ground beef or pork", "quantity": "1", "unit": "lb"},
            {"item": "chopped onion", "quantity": "1/2", "unit": "cup"},
            {"item": "condensed cream of mushroom or celery soup", "quantity": "10 3/4", "unit": "oz"},
            {"item": "shredded American cheese", "quantity": "1", "unit": "cup"},
            {"item": "milk", "quantity": "1/4", "unit": "cup"},
            {"item": "Worcestershire sauce", "quantity": "1", "unit": "tsp"},
            {"item": "dried thyme, marjoram, or savory", "quantity": "1/2", "unit": "tsp"},
            {"item": "dry white wine", "quantity": "2", "unit": "tbsp"},
            {"item": "granules instant beef bouillon", "quantity": "1/2", "unit": "tsp"},
            {"item": "light cream or milk", "quantity": "2/3", "unit": "cup"}
        ],
        "instructions": [
            {"step": 1, "text": "Cook macaroni according to package directions; drain."},
            {"step": 2, "text": "In large skillet cook meat and onion till meat is brown. Drain."},
            {"step": 3, "text": "Stir in soup, half the cheese, milk, Worcestershire sauce, and herb."},
            {"step": 4, "text": "Stir in cooked macaroni."},
            {"step": 5, "text": "Transfer to 1 1/2-quart casserole."},
            {"step": 6, "text": "Bake, covered, at 350°F for 30 minutes."},
            {"step": 7, "text": "Uncover; top with remaining cheese. Bake 5 minutes more."}
        ],
        "temperature": "350°F (175°C)",
        "cook_time": "35 minutes",
        "tags": ["ground beef", "pasta", "casserole", "easy", "main dish", "bhg"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": ["IMG_5408 Large.jpeg"]
    },
    {
        "id": "hamburger-pie-bhg",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Hamburger Pie",
        "category": "main-dishes",
        "attribution": "Better Homes and Gardens",
        "source_note": "BHG Cookbook - Meat section",
        "description": "Classic comfort food with seasoned ground beef and mashed potato topping.",
        "servings_yield": "4 servings",
        "ingredients": [
            {"item": "ground beef", "quantity": "1", "unit": "lb"},
            {"item": "chopped onion", "quantity": "1/2", "unit": "cup"},
            {"item": "salt", "quantity": "1/2", "unit": "tsp"},
            {"item": "pepper", "quantity": "1/8", "unit": "tsp"},
            {"item": "cut green beans", "quantity": "16", "unit": "oz", "prep_note": "drained"},
            {"item": "condensed tomato soup", "quantity": "10 3/4", "unit": "oz"},
            {"item": "mashed potatoes", "quantity": "3", "unit": "cups"},
            {"item": "beaten egg", "quantity": "1", "unit": ""},
            {"item": "shredded American cheese", "quantity": "1/2", "unit": "cup"}
        ],
        "instructions": [
            {"step": 1, "text": "In skillet cook beef and onion till meat is brown. Drain."},
            {"step": 2, "text": "Add salt and pepper."},
            {"step": 3, "text": "Stir in beans and soup. Pour into 1 1/2-quart casserole."},
            {"step": 4, "text": "Combine mashed potatoes and egg."},
            {"step": 5, "text": "Spoon potato mixture in mounds over meat."},
            {"step": 6, "text": "Bake at 350°F for 25 to 30 minutes."},
            {"step": 7, "text": "Sprinkle with cheese. Bake 2 to 3 minutes more till cheese melts."}
        ],
        "temperature": "350°F (175°C)",
        "cook_time": "30-35 minutes",
        "tags": ["ground beef", "potato", "casserole", "main dish", "bhg"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": ["IMG_5408 Large.jpeg"]
    },
    # From IMG_5409 Large.jpeg (page 249)
    {
        "id": "chili-mac-skillet-bhg",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Chili-Mac Skillet",
        "category": "main-dishes",
        "attribution": "Better Homes and Gardens",
        "source_note": "BHG Cookbook - Meat section",
        "description": "One-skillet meal combining chili and macaroni.",
        "servings_yield": "5 servings",
        "ingredients": [
            {"item": "ground beef", "quantity": "1", "unit": "lb"},
            {"item": "chopped onion", "quantity": "3/4", "unit": "cup"},
            {"item": "tomato sauce", "quantity": "8", "unit": "oz"},
            {"item": "red kidney beans", "quantity": "15 1/2", "unit": "oz", "prep_note": "drained"},
            {"item": "elbow macaroni", "quantity": "1", "unit": "cup"},
            {"item": "chili powder", "quantity": "2-3", "unit": "tsp"},
            {"item": "garlic salt", "quantity": "1/2", "unit": "tsp"},
            {"item": "shredded Monterey Jack cheese", "quantity": "1/2", "unit": "cup"}
        ],
        "instructions": [
            {"step": 1, "text": "In large skillet cook meat and onion till meat is brown. Drain."},
            {"step": 2, "text": "Stir in undrained tomatoes, tomato sauce, undrained beans, uncooked pasta, chili powder, garlic salt, and 1/4 cup water."},
            {"step": 3, "text": "Bring to boiling; reduce heat. Cover; simmer 20 minutes, stirring often."},
            {"step": 4, "text": "Top with cheese. Cover; heat 2 minutes or till cheese melts."}
        ],
        "cook_time": "25 minutes",
        "tags": ["ground beef", "pasta", "chili", "one-pot", "main dish", "bhg"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": ["IMG_5409 Large.jpeg"]
    },
    {
        "id": "stuffed-green-peppers-bhg",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Stuffed Green Peppers",
        "category": "main-dishes",
        "attribution": "Better Homes and Gardens",
        "source_note": "BHG Cookbook - Meat section",
        "description": "Bell peppers stuffed with seasoned ground beef and rice mixture.",
        "servings_yield": "6 servings",
        "ingredients": [
            {"item": "large green peppers", "quantity": "6", "unit": ""},
            {"item": "ground beef or lamb", "quantity": "1", "unit": "lb"},
            {"item": "chopped onion", "quantity": "1/2", "unit": "cup"},
            {"item": "tomatoes", "quantity": "16", "unit": "oz", "prep_note": "cut up"},
            {"item": "cooked rice", "quantity": "1/2", "unit": "cup"},
            {"item": "Worcestershire sauce", "quantity": "1", "unit": "tsp"},
            {"item": "salt", "quantity": "1/2", "unit": "tsp"},
            {"item": "shredded American cheese", "quantity": "1/2", "unit": "cup"}
        ],
        "instructions": [
            {"step": 1, "text": "Cut tops from peppers; remove seeds and membranes."},
            {"step": 2, "text": "Precook peppers in boiling salted water for 5 minutes; drain."},
            {"step": 3, "text": "For filling, in skillet cook meat and onion till meat is brown. Drain."},
            {"step": 4, "text": "Add half the tomatoes, rice, Worcestershire, and salt."},
            {"step": 5, "text": "Stuff peppers with meat mixture. Place in baking dish."},
            {"step": 6, "text": "Pour remaining tomatoes around peppers."},
            {"step": 7, "text": "Bake, uncovered, at 375°F for 35 to 40 minutes."},
            {"step": 8, "text": "Top with cheese; bake 5 minutes more."}
        ],
        "temperature": "375°F (190°C)",
        "cook_time": "40-45 minutes",
        "tags": ["ground beef", "peppers", "stuffed", "main dish", "bhg"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": ["IMG_5409 Large.jpeg"]
    },
    # From IMG_5411 Large.jpeg (page 251)
    {
        "id": "deep-dish-meat-pie-bhg",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Deep-Dish Meat Pie",
        "category": "main-dishes",
        "attribution": "Better Homes and Gardens",
        "source_note": "BHG Cookbook - Meat section (EASY)",
        "description": "Hearty meat and vegetable pie with pastry crust.",
        "servings_yield": "6 servings",
        "ingredients": [
            {"item": "beef stew meat", "quantity": "1", "unit": "lb", "prep_note": "cubed"},
            {"item": "potatoes", "quantity": "2", "unit": "cups", "prep_note": "peeled and cubed"},
            {"item": "frozen peas", "quantity": "1", "unit": "cup"},
            {"item": "beef broth", "quantity": "1 1/2", "unit": "cups"},
            {"item": "dried thyme, savory, or basil", "quantity": "1/2", "unit": "tsp"},
            {"item": "salt", "quantity": "1/4", "unit": "tsp"},
            {"item": "pepper", "quantity": "1/8", "unit": "tsp"},
            {"item": "all-purpose flour", "quantity": "1/3", "unit": "cup"},
            {"item": "cold water", "quantity": "1/3", "unit": "cup"},
            {"item": "pastry for single-crust pie", "quantity": "", "unit": ""}
        ],
        "instructions": [
            {"step": 1, "text": "In large saucepan combine meat, potatoes, and 1 cup broth."},
            {"step": 2, "text": "Add thyme, salt, and pepper. Bring to boiling; reduce heat."},
            {"step": 3, "text": "Cover; simmer 45 minutes or till meat is tender."},
            {"step": 4, "text": "Add peas; cook 5 minutes."},
            {"step": 5, "text": "Combine flour and cold water; stir into meat mixture."},
            {"step": 6, "text": "Cook and stir till thickened. Pour into 2-quart casserole."},
            {"step": 7, "text": "Roll pastry to fit top of casserole. Place over filling; seal and flute."},
            {"step": 8, "text": "Cut slits for steam. Bake at 425°F for 20 to 25 minutes."}
        ],
        "temperature": "425°F (220°C)",
        "cook_time": "70-75 minutes total",
        "tags": ["beef", "pot pie", "pastry", "easy", "main dish", "bhg"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": ["IMG_5411 Large.jpeg"]
    },
    {
        "id": "ham-potato-scallop-bhg",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Ham-Potato Scallop",
        "category": "main-dishes",
        "attribution": "Better Homes and Gardens",
        "source_note": "BHG Cookbook - Meat section",
        "description": "Creamy scalloped potatoes layered with ham.",
        "servings_yield": "4 servings",
        "ingredients": [
            {"item": "cubed fully cooked ham", "quantity": "1 1/2", "unit": "cups"},
            {"item": "chopped onion", "quantity": "1/4", "unit": "cup"},
            {"item": "medium potatoes", "quantity": "4", "unit": "", "prep_note": "peeled and thinly sliced"},
            {"item": "cream of mushroom or celery soup", "quantity": "10 3/4", "unit": "oz"},
            {"item": "milk", "quantity": "1/4", "unit": "cup"},
            {"item": "dry bread crumbs", "quantity": "1/2", "unit": "cup"},
            {"item": "snipped parsley", "quantity": "1", "unit": "tbsp"},
            {"item": "margarine or butter", "quantity": "1", "unit": "tbsp", "prep_note": "melted"}
        ],
        "instructions": [
            {"step": 1, "text": "In 1 1/2-quart casserole layer half of the ham, half of the onion, and half of the potatoes. Repeat layers."},
            {"step": 2, "text": "Mix soup and milk; pour over layers."},
            {"step": 3, "text": "Cover; bake at 350°F for 1 hour."},
            {"step": 4, "text": "Combine crumbs, parsley, and margarine."},
            {"step": 5, "text": "Sprinkle atop casserole. Bake, uncovered, 15 minutes more."}
        ],
        "temperature": "350°F (175°C)",
        "cook_time": "1 hour 15 minutes",
        "tags": ["ham", "potato", "casserole", "scalloped", "main dish", "bhg"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": ["IMG_5411 Large.jpeg"]
    },
    {
        "id": "meaty-noodle-casserole-bhg",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Meaty Noodle Casserole",
        "category": "main-dishes",
        "attribution": "Better Homes and Gardens",
        "source_note": "BHG Cookbook - Meat section (EASY)",
        "description": "Easy casserole with ground beef, noodles, and sour cream sauce.",
        "servings_yield": "4-5 servings",
        "ingredients": [
            {"item": "medium noodles", "quantity": "3", "unit": "cups"},
            {"item": "ground beef or pork", "quantity": "1", "unit": "lb"},
            {"item": "cream of mushroom soup", "quantity": "10 3/4", "unit": "oz"},
            {"item": "milk", "quantity": "1/2", "unit": "cup"},
            {"item": "dairy sour cream", "quantity": "1/2", "unit": "cup"},
            {"item": "chopped pimiento", "quantity": "2", "unit": "tbsp"},
            {"item": "snipped parsley", "quantity": "2", "unit": "tbsp"},
            {"item": "shredded cheddar", "quantity": "1/2", "unit": "cup"}
        ],
        "instructions": [
            {"step": 1, "text": "Cook noodles according to package directions; drain."},
            {"step": 2, "text": "In skillet cook meat till brown; drain."},
            {"step": 3, "text": "Stir in soup, milk, sour cream, pimiento, and parsley."},
            {"step": 4, "text": "Fold in noodles. Transfer to 2-quart casserole."},
            {"step": 5, "text": "Bake, covered, at 375°F for 35 to 40 minutes."},
            {"step": 6, "text": "Sprinkle with cheese; bake 5 minutes more."}
        ],
        "temperature": "375°F (190°C)",
        "cook_time": "40-45 minutes",
        "tags": ["ground beef", "noodles", "casserole", "easy", "main dish", "bhg"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": ["IMG_5411 Large.jpeg"]
    },
    # From IMG_5412 Large.jpeg (page 252)
    {
        "id": "corned-beef-hash-bhg",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Corned Beef Hash",
        "category": "main-dishes",
        "attribution": "Better Homes and Gardens",
        "source_note": "BHG Cookbook - Meat section",
        "description": "Classic hash made with corned beef, potatoes, and onion.",
        "servings_yield": "4 servings",
        "ingredients": [
            {"item": "finely chopped cooked corned beef", "quantity": "2", "unit": "cups"},
            {"item": "finely chopped cooked potato", "quantity": "1 1/2", "unit": "cups"},
            {"item": "finely chopped onion", "quantity": "1/4", "unit": "cup"},
            {"item": "salt", "quantity": "1/4", "unit": "tsp"},
            {"item": "pepper", "quantity": "1/8", "unit": "tsp"},
            {"item": "milk", "quantity": "1/4", "unit": "cup"},
            {"item": "margarine or butter", "quantity": "2", "unit": "tbsp"},
            {"item": "Worcestershire sauce", "quantity": "2", "unit": "tsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Stir together corned beef, potato, onion, salt, pepper, and milk."},
            {"step": 2, "text": "In large skillet melt margarine over medium heat."},
            {"step": 3, "text": "Spread hash evenly in skillet."},
            {"step": 4, "text": "Cook over medium heat for 8 to 10 minutes, turning occasionally."},
            {"step": 5, "text": "Stir in Worcestershire sauce. Serve hot."}
        ],
        "cook_time": "10 minutes",
        "tags": ["corned beef", "hash", "potato", "breakfast", "main dish", "bhg"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": ["IMG_5412 Large.jpeg"]
    },
    {
        "id": "meaty-stuffed-potatoes-bhg",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Meaty Stuffed Potatoes",
        "category": "main-dishes",
        "attribution": "Better Homes and Gardens",
        "source_note": "BHG Cookbook - Meat section",
        "description": "Baked potatoes stuffed with ham and cheese.",
        "servings_yield": "6 servings",
        "ingredients": [
            {"item": "medium baking potatoes", "quantity": "6", "unit": ""},
            {"item": "diced cooked ham, beef, or pork", "quantity": "6-8", "unit": "oz"},
            {"item": "dairy sour cream", "quantity": "1/2", "unit": "cup"},
            {"item": "milk", "quantity": "1/4", "unit": "cup"},
            {"item": "sliced green onion", "quantity": "3", "unit": "tbsp"},
            {"item": "salt", "quantity": "1/4", "unit": "tsp"},
            {"item": "pepper", "quantity": "1/8", "unit": "tsp"},
            {"item": "shredded American, Swiss, or Monterey Jack cheese", "quantity": "1/2", "unit": "cup"}
        ],
        "instructions": [
            {"step": 1, "text": "Scrub potatoes; prick with a fork. Bake in 425°F oven for 50 to 60 minutes or till tender."},
            {"step": 2, "text": "Cut a lengthwise slice off tops of potatoes; scoop out insides."},
            {"step": 3, "text": "Mash potato; mix in meat, sour cream, milk, onion, salt, and pepper."},
            {"step": 4, "text": "Pile mixture back into potato shells."},
            {"step": 5, "text": "Place in baking dish. Bake at 425°F for 20 to 25 minutes."},
            {"step": 6, "text": "Top with cheese; bake 2 to 3 minutes more till cheese melts."}
        ],
        "temperature": "425°F (220°C)",
        "cook_time": "1 hour 25 minutes total",
        "tags": ["potato", "ham", "stuffed", "cheese", "main dish", "bhg"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": ["IMG_5412 Large.jpeg"]
    },
    {
        "id": "creamed-dried-beef-bhg",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Creamed Dried Beef",
        "category": "main-dishes",
        "attribution": "Better Homes and Gardens",
        "source_note": "BHG Cookbook - Meat section (FAST)",
        "description": "Classic SOS (creamed chipped beef) served over toast.",
        "servings_yield": "4 servings",
        "ingredients": [
            {"item": "dried beef", "quantity": "3-4", "unit": "oz", "prep_note": "sliced"},
            {"item": "margarine or butter", "quantity": "2", "unit": "tbsp"},
            {"item": "all-purpose flour", "quantity": "2", "unit": "tbsp"},
            {"item": "milk", "quantity": "1 1/2", "unit": "cups"},
            {"item": "pepper", "quantity": "1/8", "unit": "tsp"},
            {"item": "snipped green pepper", "quantity": "2", "unit": "tbsp", "prep_note": "optional"},
            {"item": "toast points", "quantity": "4", "unit": "slices"}
        ],
        "instructions": [
            {"step": 1, "text": "If using dried beef, rinse and drain well. In a large skillet cook dried beef and, if desired, green pepper in margarine about 3 minutes or till edges curl."},
            {"step": 2, "text": "Stir in flour and pepper. Add milk all at once."},
            {"step": 3, "text": "Cook and stir till thickened and bubbly."},
            {"step": 4, "text": "Cook and stir 1 minute more."},
            {"step": 5, "text": "Serve over toast points."}
        ],
        "cook_time": "10 minutes",
        "tags": ["dried beef", "creamed", "toast", "fast", "breakfast", "main dish", "bhg"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": ["IMG_5412 Large.jpeg"]
    },
    # From IMG_5413 Large.jpeg (page 253)
    {
        "id": "reuben-sandwiches-bhg",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Reuben Sandwiches",
        "category": "sandwiches",
        "attribution": "Better Homes and Gardens",
        "source_note": "BHG Cookbook - Meat section (FAST)",
        "description": "Classic grilled Reuben with corned beef, sauerkraut, and Swiss cheese.",
        "servings_yield": "4 servings",
        "ingredients": [
            {"item": "slices dark rye or pumpernickel bread", "quantity": "8", "unit": ""},
            {"item": "Thousand Island salad dressing", "quantity": "1/3", "unit": "cup"},
            {"item": "thinly sliced cooked corned beef", "quantity": "1/2", "unit": "lb"},
            {"item": "Swiss cheese slices", "quantity": "4", "unit": ""},
            {"item": "sauerkraut", "quantity": "1", "unit": "cup", "prep_note": "well drained"},
            {"item": "softened butter", "quantity": "2", "unit": "tbsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Spread one side of bread slices with dressing."},
            {"step": 2, "text": "Top 4 slices with corned beef, cheese, and sauerkraut."},
            {"step": 3, "text": "Cover with remaining bread, dressing side down."},
            {"step": 4, "text": "Butter top and bottom of sandwiches."},
            {"step": 5, "text": "Grill in skillet over medium heat till bread is golden and cheese melts, turning once."}
        ],
        "cook_time": "10 minutes",
        "tags": ["corned beef", "sandwich", "reuben", "grilled", "fast", "bhg"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": ["IMG_5413 Large.jpeg"]
    },
    {
        "id": "barbecue-style-sandwiches-bhg",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Barbecue-Style Sandwiches",
        "category": "sandwiches",
        "attribution": "Better Homes and Gardens",
        "source_note": "BHG Cookbook - Meat section (EASY)",
        "description": "Sloppy Joe-style sandwiches with tangy barbecue sauce.",
        "servings_yield": "4 servings",
        "ingredients": [
            {"item": "tomato sauce", "quantity": "8", "unit": "oz"},
            {"item": "finely chopped onion", "quantity": "1/2", "unit": "cup"},
            {"item": "finely chopped green pepper", "quantity": "1/4", "unit": "cup"},
            {"item": "brown sugar", "quantity": "2", "unit": "tbsp"},
            {"item": "vinegar", "quantity": "1 1/2", "unit": "tbsp"},
            {"item": "Worcestershire sauce", "quantity": "1 1/2", "unit": "tbsp"},
            {"item": "dry mustard", "quantity": "1/4", "unit": "tsp"},
            {"item": "celery seed", "quantity": "1/4", "unit": "tsp"},
            {"item": "garlic, minced", "quantity": "1", "unit": "clove"},
            {"item": "chili powder", "quantity": "1/4", "unit": "tsp"},
            {"item": "thinly sliced cooked beef, pork, or lamb", "quantity": "1/2", "unit": "lb"},
            {"item": "French-style rolls", "quantity": "4", "unit": "", "prep_note": "split and toasted"}
        ],
        "instructions": [
            {"step": 1, "text": "In medium saucepan combine tomato sauce, onion, green pepper, brown sugar, vinegar, Worcestershire, mustard, celery seed, garlic, and chili powder."},
            {"step": 2, "text": "Bring to boiling; reduce heat. Cover; simmer 15 minutes."},
            {"step": 3, "text": "Stir some of the meat mixture onto bottom half of each roll."},
            {"step": 4, "text": "Spoon some of the meat mixture onto bottom half of each roll. Top with other half of roll."}
        ],
        "cook_time": "15 minutes",
        "tags": ["beef", "sandwich", "barbecue", "easy", "bhg"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": ["IMG_5413 Large.jpeg"]
    },
    {
        "id": "meat-stuffed-pita-pockets-bhg",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Meat-Stuffed Pita Pockets",
        "category": "sandwiches",
        "attribution": "Better Homes and Gardens",
        "source_note": "BHG Cookbook - Meat section (FAST)",
        "description": "Pita bread stuffed with seasoned ground beef and fresh vegetables.",
        "servings_yield": "4 servings",
        "ingredients": [
            {"item": "skinny worcester cream or salad dressing", "quantity": "1/4", "unit": "cup"},
            {"item": "prepared horseradish", "quantity": "1", "unit": "tbsp"},
            {"item": "cooked ground beef, pork, or lamb", "quantity": "1", "unit": "cup"},
            {"item": "shredded carrot", "quantity": "1/2", "unit": "cup"},
            {"item": "celery", "quantity": "1/4", "unit": "cup", "prep_note": "chopped"},
            {"item": "pita bread rounds", "quantity": "2", "unit": "large"},
            {"item": "lettuce leaves", "quantity": "4", "unit": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Stir together sour cream and horseradish."},
            {"step": 2, "text": "Combine meat, carrot, and celery with half the sour cream mixture."},
            {"step": 3, "text": "Cut pita rounds in half; open pockets."},
            {"step": 4, "text": "Line each half with lettuce."},
            {"step": 5, "text": "Spoon in meat mixture. Drizzle with remaining sour cream mixture."}
        ],
        "tags": ["ground beef", "pita", "sandwich", "fast", "bhg"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": ["IMG_5413 Large.jpeg"]
    },
    # From IMG_5473 Large.jpeg (page 310)
    {
        "id": "chicken-with-papaya-bhg",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Chicken with Papaya",
        "category": "main-dishes",
        "attribution": "Better Homes and Gardens",
        "source_note": "BHG Cookbook - Poultry section",
        "description": "Stir-fried chicken with tropical papaya and ginger.",
        "servings_yield": "4 servings",
        "ingredients": [
            {"item": "finely shredded orange peel", "quantity": "1/2", "unit": "tsp"},
            {"item": "orange juice", "quantity": "1/3", "unit": "cup"},
            {"item": "soy sauce", "quantity": "1", "unit": "tbsp"},
            {"item": "honey", "quantity": "2", "unit": "tsp"},
            {"item": "grated gingerroot", "quantity": "1 1/2", "unit": "tsp"},
            {"item": "skinless boneless chicken breasts", "quantity": "2", "unit": "", "prep_note": "1/2 lb total, cut into 1-inch pieces"},
            {"item": "cornstarch", "quantity": "2", "unit": "tsp"},
            {"item": "cooking oil", "quantity": "2", "unit": "tbsp"},
            {"item": "thinly bias-sliced celery", "quantity": "1", "unit": "cup"},
            {"item": "papaya", "quantity": "1", "unit": "small", "prep_note": "halved, seeded, peeled, and cut into bite-size pieces"},
            {"item": "macadamia nuts or toasted blanched whole almonds", "quantity": "1/2", "unit": "cup"},
            {"item": "hot cooked rice", "quantity": "2", "unit": "cups"}
        ],
        "instructions": [
            {"step": 1, "text": "For marinade, in a bowl stir together orange peel, orange juice, soy sauce, honey, and gingerroot."},
            {"step": 2, "text": "Rinse chicken; pat dry. Cut into 1-inch pieces. Add chicken to marinade, stirring to coat. Cover and marinate at room temperature for 30 minutes or in the refrigerator for 2 hours, stirring occasionally."},
            {"step": 3, "text": "Drain chicken, reserving marinade. Combine cornstarch and reserved marinade. Set aside."},
            {"step": 4, "text": "Preheat a wok or large skillet over high heat; add cooking oil."},
            {"step": 5, "text": "Stir-fry celery in hot oil for 3 to 4 minutes or till crisp-tender. Remove from wok."},
            {"step": 6, "text": "Add chicken to wok; stir-fry for 2 to 3 minutes or till no longer pink. Push from center of wok."},
            {"step": 7, "text": "Stir marinade mixture; add to center of wok. Cook and stir till thickened and bubbly."},
            {"step": 8, "text": "Return celery to wok; add papaya. Stir to coat well. Cook, covered, about 1 minute or till heated through."},
            {"step": 9, "text": "Stir in nuts. Serve with hot cooked rice."}
        ],
        "tags": ["chicken", "papaya", "stir-fry", "tropical", "main dish", "bhg"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": ["IMG_5473 Large.jpeg"]
    },
    {
        "id": "beer-batter-fried-chicken-bhg",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Beer Batter-Fried Chicken",
        "category": "main-dishes",
        "attribution": "Better Homes and Gardens",
        "source_note": "BHG Cookbook - Poultry section",
        "description": "Crispy deep-fried chicken coated in light beer batter.",
        "servings_yield": "6 servings",
        "ingredients": [
            {"item": "broiler-fryer chicken", "quantity": "2 1/2-3", "unit": "lb", "prep_note": "cut up"},
            {"item": "packaged biscuit mix", "quantity": "1", "unit": "cup"},
            {"item": "onion salt", "quantity": "1/2", "unit": "tsp"},
            {"item": "garlic powder", "quantity": "1/4", "unit": "tsp"},
            {"item": "ground red pepper", "quantity": "1/8-1/4", "unit": "tsp"},
            {"item": "beaten egg", "quantity": "1", "unit": ""},
            {"item": "beer", "quantity": "1/2", "unit": "cup"},
            {"item": "shortening or cooking oil", "quantity": "", "unit": "", "prep_note": "for deep-fat frying"}
        ],
        "instructions": [
            {"step": 1, "text": "Skin chicken, if desired. Rinse chicken. In a large saucepan cover chicken with lightly salted water. Bring to boiling; reduce heat. Cover and simmer for 20 minutes. Drain. Pat dry with paper towels."},
            {"step": 2, "text": "For batter, in a bowl combine biscuit mix, onion salt, garlic powder, and ground red pepper. In another bowl stir together egg and beer; add to biscuit mixture. Beat till smooth."},
            {"step": 3, "text": "Meanwhile, in a heavy 3-quart saucepan or deep-fat fryer heat 1 1/4 inches shortening or oil to 365°."},
            {"step": 4, "text": "Dip chicken pieces, one at a time, into batter, gently shaking off excess batter. Carefully lower into the hot oil. Fry, two or three pieces at a time, for 2 to 3 minutes or till golden, turning once."},
            {"step": 5, "text": "Drain well. Keep warm."}
        ],
        "temperature": "365°F (185°C) for frying",
        "tags": ["chicken", "fried", "beer batter", "deep fried", "main dish", "bhg"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": ["IMG_5473 Large.jpeg"]
    },
    # From IMG_5474 Large.jpeg (page 311)
    {
        "id": "cornmeal-batter-fried-chicken-bhg",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Cornmeal Batter-Fried Chicken",
        "category": "main-dishes",
        "attribution": "Better Homes and Gardens",
        "source_note": "BHG Cookbook - Poultry section",
        "description": "Deep-fried chicken with crispy cornmeal coating.",
        "servings_yield": "6 servings",
        "ingredients": [
            {"item": "broiler-fryer chicken", "quantity": "2 1/2-3", "unit": "lb", "prep_note": "cut up"},
            {"item": "all-purpose flour", "quantity": "2/3", "unit": "cup"},
            {"item": "cornmeal", "quantity": "1/3", "unit": "cup"},
            {"item": "baking powder", "quantity": "1/2", "unit": "tsp"},
            {"item": "garlic salt", "quantity": "1/2", "unit": "tsp"},
            {"item": "poultry seasoning", "quantity": "1/4", "unit": "tsp"},
            {"item": "ground red pepper", "quantity": "1/8", "unit": "tsp"},
            {"item": "beaten egg", "quantity": "1", "unit": ""},
            {"item": "milk", "quantity": "1/3", "unit": "cup"},
            {"item": "cooking oil", "quantity": "2", "unit": "tbsp"},
            {"item": "shortening or cooking oil", "quantity": "", "unit": "", "prep_note": "for deep-fat frying"}
        ],
        "instructions": [
            {"step": 1, "text": "Skin chicken, if desired. Rinse chicken. In a large saucepan cover chicken with lightly salted water. Bring to boiling; reduce heat. Cover and simmer for 20 minutes. Drain. Pat dry with paper towels."},
            {"step": 2, "text": "For batter, in a mixing bowl combine flour, cornmeal, baking powder, garlic salt, poultry seasoning, and red pepper. Stir together egg, milk, and the 2 tablespoons oil. Add to flour mixture; beat till smooth."},
            {"step": 3, "text": "Meanwhile, in a heavy 3-quart saucepan or deep-fat fryer heat 1 1/4 inches shortening or oil to 365°."},
            {"step": 4, "text": "Dip chicken pieces, one at a time, into batter, gently shaking off excess batter. Carefully lower into the hot oil. Fry, two or three pieces at a time, for 2 to 3 minutes or till golden, turning once. Carefully remove; drain well. Keep warm while frying remaining chicken."}
        ],
        "temperature": "365°F (185°C) for frying",
        "notes": ["Variations: Herbed Batter-Fried Chicken - omit poultry seasoning, add 1 tsp dried thyme, savory, marjoram, Italian seasoning, or sage. Taco Batter-Fried Chicken - omit poultry seasoning, add 1 1/4 oz envelope taco seasoning mix, increase milk to 2/3 cup. Parmesan Batter-Fried Chicken - omit garlic salt and poultry seasoning, add 1/4 cup grated Parmesan cheese, 2 tbsp snipped parsley, 1/4 tsp garlic powder, increase milk to 2/3 cup."],
        "tags": ["chicken", "fried", "cornmeal", "deep fried", "main dish", "bhg"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": ["IMG_5474 Large.jpeg"]
    },
    {
        "id": "turkey-rice-skillet-bhg",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Turkey-Rice Skillet",
        "category": "main-dishes",
        "attribution": "Better Homes and Gardens",
        "source_note": "BHG Cookbook - Poultry section (EASY)",
        "description": "Quick one-skillet meal with ground turkey, rice, and cheese.",
        "servings_yield": "4 servings",
        "ingredients": [
            {"item": "ground raw turkey", "quantity": "1", "unit": "lb"},
            {"item": "stewed tomatoes", "quantity": "14 1/2", "unit": "oz"},
            {"item": "water", "quantity": "1", "unit": "cup"},
            {"item": "long grain rice", "quantity": "1/2", "unit": "cup"},
            {"item": "chili powder", "quantity": "2", "unit": "tsp"},
            {"item": "pepper", "quantity": "1/2", "unit": "tsp"},
            {"item": "shredded Monterey Jack cheese", "quantity": "1/2", "unit": "cup"}
        ],
        "instructions": [
            {"step": 1, "text": "In large skillet cook 1 pound ground raw turkey till brown. Drain well."},
            {"step": 2, "text": "Stir in one 14 1/2-ounce can stewed tomatoes, undrained, 1 cup water, 1/2 cup long grain rice, 2 teaspoons chili powder, and 1/2 teaspoon pepper."},
            {"step": 3, "text": "Bring to boiling; reduce heat. Cover and simmer about 20 minutes or till rice is tender."},
            {"step": 4, "text": "Stir together 3/4 cup milk and 1 tablespoon all-purpose flour; add to skillet. Cook and stir till thickened and bubbly. Cook and stir 1 minute more."},
            {"step": 5, "text": "Add 1/2 cup shredded Monterey Jack cheese; stir till melted."}
        ],
        "cook_time": "25 minutes",
        "tags": ["turkey", "rice", "skillet", "one-pot", "easy", "main dish", "bhg"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": ["IMG_5474 Large.jpeg"]
    },
    # From IMG_5477 Large.jpeg (page 314)
    {
        "id": "mediterranean-chicken-bhg",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Mediterranean Chicken",
        "category": "main-dishes",
        "attribution": "Better Homes and Gardens",
        "source_note": "BHG Cookbook - Poultry section",
        "description": "Chicken and rice dish with chorizo, olives, and peas reminiscent of paella.",
        "servings_yield": "6 servings",
        "ingredients": [
            {"item": "meaty chicken pieces", "quantity": "1 1/2", "unit": "lb", "prep_note": "breasts, thighs, and drumsticks"},
            {"item": "cooking oil", "quantity": "2", "unit": "tbsp"},
            {"item": "bulk chorizo or bulk Italian sausage", "quantity": "6", "unit": "oz"},
            {"item": "medium onions", "quantity": "2", "unit": "", "prep_note": "cut into wedges"},
            {"item": "garlic", "quantity": "3", "unit": "cloves", "prep_note": "minced"},
            {"item": "water", "quantity": "2 1/2", "unit": "cups"},
            {"item": "long grain rice", "quantity": "3/4", "unit": "cup"},
            {"item": "instant chicken bouillon granules", "quantity": "1", "unit": "tbsp"},
            {"item": "dried oregano, crushed", "quantity": "1/2", "unit": "tsp"},
            {"item": "pepper", "quantity": "1/4", "unit": "tsp"},
            {"item": "frozen peas", "quantity": "10", "unit": "oz", "prep_note": "thawed"},
            {"item": "green or sweet red pepper", "quantity": "1", "unit": "medium", "prep_note": "cut into 1-inch squares"},
            {"item": "cherry tomatoes", "quantity": "8", "unit": "", "prep_note": "halved"},
            {"item": "sliced ripe olives", "quantity": "1/2", "unit": "cup"}
        ],
        "instructions": [
            {"step": 1, "text": "Rinse chicken; pat dry. In a 4 1/2-quart Dutch oven cook chicken in hot oil, uncovered, over medium heat about 15 minutes, turning to brown evenly. Remove chicken and set aside. Discard drippings."},
            {"step": 2, "text": "In the same pan cook sausage, onions, and garlic over medium heat for 8 to 10 minutes or till sausage is no longer pink. Drain; return to pan."},
            {"step": 3, "text": "Add water, rice, bouillon granules, oregano, and pepper. Bring to boiling, scraping up the browned bits. Place chicken pieces atop the sausage mixture. Reduce heat. Cover and simmer about 15 minutes or till chicken is nearly tender, turning chicken once."},
            {"step": 4, "text": "Add peas and green or red pepper to chicken mixture. Cook, covered, about 5 minutes more or till chicken is tender and no longer pink. Gently stir in tomatoes and olives."}
        ],
        "cook_time": "45 minutes",
        "tags": ["chicken", "chorizo", "rice", "mediterranean", "one-pot", "main dish", "bhg"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": ["IMG_5477 Large.jpeg"]
    },
    {
        "id": "chicken-country-captain-bhg",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Chicken Country Captain",
        "category": "main-dishes",
        "attribution": "Better Homes and Gardens",
        "source_note": "BHG Cookbook - Poultry section",
        "description": "Classic Southern curry-spiced chicken with tomatoes and raisins.",
        "servings_yield": "6 servings",
        "ingredients": [
            {"item": "broiler-fryer chicken", "quantity": "2 1/2-3", "unit": "lb", "prep_note": "cut up"},
            {"item": "chopped onion", "quantity": "1/2", "unit": "cup"},
            {"item": "chopped green pepper", "quantity": "1/2", "unit": "cup"},
            {"item": "garlic", "quantity": "1", "unit": "clove", "prep_note": "minced"},
            {"item": "margarine or butter", "quantity": "1", "unit": "tbsp"},
            {"item": "tomatoes", "quantity": "14 1/2", "unit": "oz", "prep_note": "cut up"},
            {"item": "snipped parsley", "quantity": "1/4", "unit": "cup"},
            {"item": "currants or raisins", "quantity": "2", "unit": "tbsp"},
            {"item": "curry powder", "quantity": "1", "unit": "tbsp"},
            {"item": "salt", "quantity": "1/2", "unit": "tsp"},
            {"item": "ground mace or nutmeg", "quantity": "1/4", "unit": "tsp"},
            {"item": "sugar", "quantity": "1/4", "unit": "tsp"},
            {"item": "pepper", "quantity": "1/8", "unit": "tsp"},
            {"item": "cornstarch", "quantity": "1", "unit": "tbsp"},
            {"item": "hot cooked rice", "quantity": "2", "unit": "cups"},
            {"item": "toasted sliced almonds", "quantity": "2", "unit": "tbsp", "prep_note": "optional"}
        ],
        "instructions": [
            {"step": 1, "text": "Skin chicken, if desired. Rinse and pat dry. In a large skillet cook onion, green pepper, and garlic in margarine or butter till tender but not brown. Remove from heat."},
            {"step": 2, "text": "Stir in undrained tomatoes, parsley, currants or raisins, curry powder, salt, mace, sugar, and pepper. Bring to boiling."},
            {"step": 3, "text": "Add chicken pieces to the skillet, turning to coat. Bring to boiling; reduce heat. Cover and simmer for 35 to 45 minutes or till tender and no longer pink, turning chicken once. Remove chicken from the skillet; keep warm."},
            {"step": 4, "text": "For sauce, skim fat from tomato mixture. Stir together cornstarch and 1 tablespoon cold water; add to tomato mixture. Cook and stir till thickened and bubbly. Cook and stir 1 minute more."},
            {"step": 5, "text": "Season to taste with salt and pepper. Serve gravy over chicken and dumplings. If desired, sprinkle with almonds."}
        ],
        "cook_time": "50 minutes",
        "tags": ["chicken", "curry", "southern", "country captain", "main dish", "bhg"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": ["IMG_5477 Large.jpeg"]
    },
    # From IMG_5478 Large.jpeg (page 315)
    {
        "id": "stewed-chicken-bhg",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Stewed Chicken",
        "category": "main-dishes",
        "attribution": "Better Homes and Gardens",
        "source_note": "BHG Cookbook - Poultry section",
        "description": "Basic stewed chicken that produces both cooked chicken and broth for other recipes.",
        "servings_yield": "About 5 1/2 cups broth and 2 1/2 cups chopped meat",
        "ingredients": [
            {"item": "broiler-fryer chicken", "quantity": "2 1/2-3", "unit": "lb", "prep_note": "cut up"},
            {"item": "celery with leaves", "quantity": "3", "unit": "stalks", "prep_note": "cut up"},
            {"item": "carrots", "quantity": "2", "unit": "", "prep_note": "cut up"},
            {"item": "large onion", "quantity": "1", "unit": "", "prep_note": "quartered"},
            {"item": "parsley sprigs", "quantity": "2", "unit": ""},
            {"item": "salt", "quantity": "1", "unit": "tsp"},
            {"item": "dried thyme, sage, or basil, crushed", "quantity": "1/2", "unit": "tsp"},
            {"item": "pepper", "quantity": "1/4", "unit": "tsp"},
            {"item": "bay leaves", "quantity": "2", "unit": ""},
            {"item": "water", "quantity": "6", "unit": "cups"}
        ],
        "instructions": [
            {"step": 1, "text": "Skin chicken, if desired. Rinse. In a 4 1/2-quart Dutch oven combine chicken; celery; carrots; onion; parsley; salt; thyme, sage, or basil; pepper; and bay leaves. Add water. Bring to boiling; reduce heat. Cover and simmer for 40 minutes."},
            {"step": 2, "text": "Remove chicken. Strain broth through a large sieve lined with 2 layers of cheesecloth. Discard solids. If using broth while hot, skim off fat. (Or, if storing broth for later use, chill broth in a bowl for 6 hours. Lift off fat. Pour broth into airtight containers, discarding residue in the bottom of the bowl. Seal containers. Chill up to 2 days or freeze up to 3 months.)"},
            {"step": 3, "text": "When chicken is cool enough to handle, remove meat from bones; discard skin and bones. Chop meat and use immediately. (Or, if storing meat for later use, place in airtight containers; seal. Chill up to 3 days or freeze up to 3 months.)"}
        ],
        "cook_time": "40 minutes",
        "tags": ["chicken", "stewed", "broth", "basic", "main dish", "bhg"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": ["IMG_5478 Large.jpeg"]
    },
    {
        "id": "chicken-and-dumplings-bhg",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Chicken and Dumplings",
        "category": "main-dishes",
        "attribution": "Better Homes and Gardens",
        "source_note": "BHG Cookbook - Poultry section",
        "description": "Classic comfort food with tender chicken and fluffy dumplings in gravy.",
        "servings_yield": "6 servings",
        "ingredients": [
            {"item": "broiler-fryer chicken", "quantity": "2 1/2-3", "unit": "lb", "prep_note": "cut up"},
            {"item": "chopped onion", "quantity": "1/2", "unit": "cup"},
            {"item": "poultry seasoning or dried sage or thyme, crushed", "quantity": "1/2", "unit": "tsp"},
            {"item": "salt", "quantity": "1/4", "unit": "tsp"},
            {"item": "pepper", "quantity": "1/4", "unit": "tsp"},
            {"item": "sliced carrot", "quantity": "2", "unit": "cups"},
            {"item": "sliced celery", "quantity": "1", "unit": "cup"},
            {"item": "Dumplings for Stew", "quantity": "", "unit": "", "prep_note": "see recipe, page 378"},
            {"item": "all-purpose flour", "quantity": "1/4", "unit": "cup"}
        ],
        "instructions": [
            {"step": 1, "text": "Skin chicken, if desired. Rinse. In a 4 1/2-quart Dutch oven combine chicken, onion, poultry seasoning, salt, and pepper. Add 3 cups water. Bring to boiling; reduce heat. Cover and simmer for 25 minutes. Add carrot and celery. Simmer, covered, for 10 minutes more."},
            {"step": 2, "text": "Prepare Dumplings for Stew, omitting the herb. Drop from a tablespoon into six mounds directly onto chicken (do not drop batter into liquid). Cover; simmer about 12 minutes or till a toothpick inserted into dumplings comes out clean."},
            {"step": 3, "text": "Using a slotted spoon, transfer chicken, dumplings, and vegetables to a platter; cover."},
            {"step": 4, "text": "For gravy, skim fat from broth; discard fat. Measure 2 cups broth into the Dutch oven. Slowly stir 1/2 cup cold water into flour. Stir into broth. Cook and stir till bubbly. Cook and stir 1 minute more. Season to taste with salt and pepper. Serve gravy over chicken and dumplings."}
        ],
        "cook_time": "50 minutes",
        "notes": ["Chicken and Noodles variation: Prepare as above, except pour 4 cups of the hot broth into the Dutch oven. (Freeze remaining broth for another use.) Bring to boiling. Add 6 ounces (2 1/2 cups) dried Homemade Pasta or 6 ounces (3 cups) packaged noodles, or one 8-ounce package frozen noodles. Stir in 1 cup thinly sliced carrots; 1/2 cup sliced celery; 1/2 cup chopped onion; 1/2 teaspoon dried thyme, sage, or basil, crushed; and 1/4 teaspoon pepper. Return to boiling; reduce heat. Cover and simmer for 10 to 15 minutes or till noodles and vegetables are tender."],
        "tags": ["chicken", "dumplings", "comfort food", "classic", "main dish", "bhg"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": ["IMG_5478 Large.jpeg"]
    },
    # From IMG_5479 Large.jpeg (page 316)
    {
        "id": "chicken-potpies-bhg",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Chicken Potpies",
        "category": "main-dishes",
        "attribution": "Better Homes and Gardens",
        "source_note": "BHG Cookbook - Poultry section",
        "description": "Individual chicken pies with flaky pastry topping.",
        "servings_yield": "6 servings",
        "ingredients": [
            {"item": "Pastry for Double-Crust Pie", "quantity": "", "unit": "", "prep_note": "see recipe"},
            {"item": "frozen peas and carrots", "quantity": "10", "unit": "oz"},
            {"item": "chopped onion", "quantity": "1/3", "unit": "cup"},
            {"item": "chopped fresh mushrooms", "quantity": "1/2", "unit": "cup"},
            {"item": "margarine or butter", "quantity": "1/4", "unit": "cup"},
            {"item": "all-purpose flour", "quantity": "1/3", "unit": "cup"},
            {"item": "salt", "quantity": "1/4", "unit": "tsp"},
            {"item": "dried sage, marjoram, or thyme, crushed", "quantity": "1/4", "unit": "tsp"},
            {"item": "pepper", "quantity": "1/8", "unit": "tsp"},
            {"item": "chicken broth", "quantity": "2", "unit": "cups"},
            {"item": "milk", "quantity": "2/3", "unit": "cup"},
            {"item": "cubed cooked chicken or turkey", "quantity": "3", "unit": "cups"},
            {"item": "snipped parsley", "quantity": "1/4", "unit": "cup"},
            {"item": "chopped pimiento", "quantity": "1/4", "unit": "cup"}
        ],
        "instructions": [
            {"step": 1, "text": "Prepare pastry; set aside. Cook peas and carrots according to package directions; drain. In a saucepan cook onion and mushrooms in margarine or butter till tender. Stir in flour, salt, sage, marjoram, or thyme; and pepper."},
            {"step": 2, "text": "Add chicken broth and milk all at once. Cook and stir till thickened and bubbly. Stir in drained peas and carrots, chicken or turkey, parsley, and pimiento; heat till bubbly."},
            {"step": 3, "text": "Pour chicken mixture into six 10-ounce round casseroles."},
            {"step": 4, "text": "Roll pastry into a 15x10-inch rectangle. Cut into six 5-inch circles and place atop the 10-ounce casseroles. (Or, roll pastry into a 13x9-inch rectangle. Place over the 12x7 1/2x2-inch baking dish.) Flute edges of pastry and cut slits in the top for steam to escape."},
            {"step": 5, "text": "Bake in a 450°F oven for 12 to 15 minutes or till pastry is golden brown."}
        ],
        "temperature": "450°F (230°C)",
        "cook_time": "12-15 minutes",
        "notes": ["Herb-Crumb-Topped Chicken Potpies: Prepare as above, except omit pastry. Stir together 1 cup herb-seasoned stuffing croutons and 2 tablespoons melted margarine or butter. Sprinkle atop chicken mixture in casseroles or dish. Bake in a 400°F oven about 15 minutes or till biscuits are golden.", "Biscuit-Topped Chicken Potpies: Prepare as above, except omit pastry. Cut 6 refrigerated biscuits into quarters and arrange atop bubbly chicken mixture in casseroles or dish. Bake in a 400°F oven about 15 minutes or till biscuits are golden."],
        "tags": ["chicken", "pot pie", "pastry", "comfort food", "main dish", "bhg"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": ["IMG_5479 Large.jpeg"]
    },
    {
        "id": "chicken-a-la-king-bhg",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Chicken à la King",
        "category": "main-dishes",
        "attribution": "Better Homes and Gardens",
        "source_note": "BHG Cookbook - Poultry section",
        "description": "Classic creamy chicken dish served over toast points or patty shells.",
        "servings_yield": "4 servings",
        "ingredients": [
            {"item": "margarine or butter", "quantity": "1/4", "unit": "cup"},
            {"item": "sliced fresh mushrooms", "quantity": "1", "unit": "cup"},
            {"item": "all-purpose flour", "quantity": "1/4", "unit": "cup"},
            {"item": "milk", "quantity": "1 1/2", "unit": "cups"},
            {"item": "chicken broth", "quantity": "1", "unit": "cup"},
            {"item": "cubed cooked chicken or turkey", "quantity": "2", "unit": "cups"},
            {"item": "chopped pimiento", "quantity": "1/4", "unit": "cup"},
            {"item": "dry sherry", "quantity": "2", "unit": "tbsp", "prep_note": "optional"},
            {"item": "salt", "quantity": "1/4", "unit": "tsp"},
            {"item": "pepper", "quantity": "1/8", "unit": "tsp"},
            {"item": "toast points or baked patty shells", "quantity": "8", "unit": ""}
        ],
        "instructions": [
            {"step": 1, "text": "In a saucepan melt margarine. If using fresh mushrooms, add mushrooms and cook, tender."},
            {"step": 2, "text": "Stir in flour, 1/2 teaspoon salt, and 1/4 teaspoon pepper. Add milk and chicken broth all at once."},
            {"step": 3, "text": "Cook and stir till thickened and bubbly. Cook and stir for 1 minute more."},
            {"step": 4, "text": "Add canned mushrooms, if using. Stir in chicken or turkey, pimiento, and, if desired, dry sherry. Heat through."},
            {"step": 5, "text": "Spoon atop toast points."}
        ],
        "cook_time": "15 minutes",
        "notes": ["Cheesy Chicken à la King: Prepare as above, except add 1 cup shredded American or process Swiss cheese to the thickened mixture before adding the chicken or turkey. Stir till cheese melts.", "Curried Chicken à la King: Prepare as above, except add 1 teaspoon curry powder to melted margarine or butter; cook for 1 minute. Omit dry sherry. If desired, add 1 tablespoon chutney with chicken or turkey.", "Herbed Chicken à la King: Prepare as above, except cook 2 tablespoons finely chopped green pepper or sliced green onion; 1 clove garlic, minced; and 1/2 teaspoon dried basil, crushed, in melted margarine or butter till tender."],
        "tags": ["chicken", "creamy", "classic", "main dish", "bhg"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": ["IMG_5479 Large.jpeg"]
    }
]

# Tips and techniques to add as reference items
TIPS_AND_TECHNIQUES = [
    {
        "id": "tip-to-skin-or-not-bhg",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "To Skin or Not to Skin (Chicken)",
        "category": "tips",
        "attribution": "Better Homes and Gardens",
        "source_note": "BHG Cookbook - Poultry section tip",
        "description": "Guide for when to leave chicken skin on or remove it during cooking.",
        "content": "Our recipes deal with chicken skin in three ways. In some recipes, we call for the skin to be left on, either because it is too difficult to remove or because it is necessary to keep the chicken from overcooking. In other recipes, we give you a choice. Remove the skin if you wish to save calories and cut down on fat. Finally, in still other recipes, we tell you to remove the skin. In these dishes, the skin develops an unpleasant texture if it is left on. Keep these guidelines in mind when you're trying to decide whether to skin chicken for your own recipes. One last tip: If you're micro-cooking skinned chicken, be sure to cover the baking dish with vented clear plastic wrap to keep the chicken moist.",
        "tags": ["tip", "chicken", "poultry", "technique", "bhg"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": ["IMG_5473 Large.jpeg"]
    },
    {
        "id": "tip-carving-roasted-bird-bhg",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Carving a Roasted Bird",
        "category": "tips",
        "attribution": "Better Homes and Gardens",
        "source_note": "BHG Cookbook - Poultry section tip",
        "description": "Step-by-step instructions for carving whole roasted poultry.",
        "content": "To carve poultry with confidence, use a sharp knife and these directions. When the bird is done, remove it from the oven and cover it with foil. Let it stand for 15 to 20 minutes before beginning to carve. Standing lets the bird's flesh firm up, meaning the carved slices will hold together better. Place the bird on a cutting board. Remove the stuffing. Grasp the tip of one drumstick and pull it away from the body. Cut through the skin and meat between the thigh and the body. Repeat on the other side. With the tip of the knife, separate the thighbone from the backbone by cutting through the joint. Repeat on other side. To separate the thighs and drumsticks, cut through the joints where the drumstick bones and thighbones meet. To carve the meat from the drumsticks, hold each drumstick vertically by the tip with the large end resting on the cutting board. Slice the meat parallel to the bone and under some tendons, turning the leg to get even slices. Slice thigh meat the same way. To carve the breast meat, make a deep horizontal cut into the breast above each wing. This cut marks one end of each breast meat slice. Beginning at the outer edge of one side of each breast, cut slices from the top of the breast down to the horizontal cut. Cut the final smaller slices following the curve of the breastbone. Remove wings by cutting through the joints where the wing bones and backbone meet.",
        "tags": ["tip", "carving", "roasting", "poultry", "technique", "bhg"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": ["IMG_5485 Large.jpeg"]
    },
    {
        "id": "tip-brown-bag-pointers-bhg",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Brown-Bag Pointers",
        "category": "tips",
        "attribution": "Better Homes and Gardens",
        "source_note": "BHG Cookbook - Meat section tip",
        "description": "Tips for packing lunches safely.",
        "content": "Here are three-bag tips to keep your lunch fresh: Most bag lunches are easy to keep at room temperature. Pack cold foods in an insulated lunch box with ice packs. Seal cold foods in clean airtight containers. For sandwiches, pack meats separate from bread. Fill hot thermoses only with foods at temperatures of 165°F or higher. Pack foods that can stay at room temperature safely in paper bags. Keep your lunch in a cool, dry place.",
        "tags": ["tip", "lunch", "food safety", "bhg"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": ["IMG_5413 Large.jpeg"]
    },
    {
        "id": "tip-food-safety-storage-bhg",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Food Safety and Storage",
        "category": "tips",
        "attribution": "Better Homes and Gardens",
        "source_note": "BHG Cookbook - Special Helps section",
        "description": "Comprehensive guide to keeping food safe and storing it properly.",
        "content": "Keeping food safe to eat is as simple as keeping hot foods hot, cold foods cold, and all foods clean. Keeping Foods Hot: To prevent the buildup of illness-causing bacteria, cook foods thoroughly, especially meat, poultry, and dishes containing eggs. Since bacteria grow at room temperature, discard any cooked or chilled food that has been left out longer than two hours. Cover leftovers while reheating to retain moisture. Be sure, too, to heat the food completely. Keeping Foods Cold: Keep your refrigerator at about 40°F and your freezer at 0°F or less. Check them both periodically with an appliance thermometer. Thaw meat and poultry in the refrigerator overnight. For faster thawing, place frozen packages in a watertight plastic bag under cold water. Change the water often. Do not thaw meat on the kitchen counter. Store leftovers in the refrigerator as soon as possible. Do not let food cool on the counter. When shopping, pick up perishables last. Be sure frozen foods are solid and refrigerated foods are cold. If you live more than 30 minutes from the store, you may want to stow frozen, refrigerated, and perishable foods in an ice chest for the trip home. Keeping Foods Clean: Since bacteria live all around us, always wash and dry your hands with clean cloths before you begin to cook. When working with raw meat and poultry, wash hands, counters, and utensils in hot soapy water between each recipe step. Bacteria on raw meat and poultry can contaminate other foods. Never put cooked meat or poultry on the same plate that held the raw food.",
        "tags": ["tip", "food safety", "storage", "bhg"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": ["IMG_5580 Large.jpeg"]
    },
    {
        "id": "tip-measuring-techniques-bhg",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Measuring Techniques",
        "category": "tips",
        "attribution": "Better Homes and Gardens",
        "source_note": "BHG Cookbook - Special Helps section",
        "description": "Guide to properly measuring ingredients for consistent results.",
        "content": "Correctly measuring ingredients is important for consistent results. 1. Measuring Liquids: Use a glass or clear plastic measuring cup. Place the cup on a level surface and bend down so your eye is level with the marking you wish to read. Fill the cup to the marking. Don't lift the cup off the counter to your eye; your hand is not as steady as the countertop. When using measuring spoons to measure a liquid, pour the liquid just to the top of the spoon without letting it spill over. Don't measure over the mixing bowl because the liquid could overflow from the spoon into the bowl. 2. Measuring Flour: Stir the flour in the canister to lighten it. (Sifting flours, except cake flour, no longer is necessary.) Then gently spoon the flour into a dry measuring cup and level off the top with the straight edge of a knife or a metal spatula. 3. Measuring Sugar: Press brown sugar firmly into a dry measuring cup so that it holds the shape of the cup when turned out. To measure granulated sugar, spoon the sugar into a dry measuring cup, then level it off with the straight edge of a knife or a metal spatula. 4. Measuring Solid Shortening: Using a rubber spatula, press the shortening firmly into a dry measuring cup. Level it off with the straight edge of a knife or a metal spatula. 5. Measuring Margarine or Butter: For stick margarine or butter, use an entire 1/4-pound stick for 1/2 cup, half of a stick for 1/4 cup, or an eighth of a stick for 1 tablespoon. With a sharp knife, cut off the amount needed, following the guidelines on the wrapper. For unwrapped margarine or butter, soften it, then measure as directed for solid shortening. 6. Measuring Dried Herbs: Lightly fill a measuring spoon just to the top with the dried herb (leveling with a spatula is not necessary). Then empty the spoon into your hand. Crush the herb with the fingers of your other hand. This breaks the leaves and releases their flavor. (Some of the harder dried herbs, such as rosemary and thyme, are best crushed with a mortar and pestle.)",
        "tags": ["tip", "measuring", "technique", "baking", "bhg"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": ["IMG_5590 Large.jpeg"]
    },
    {
        "id": "tip-garnishing-techniques-bhg",
        "collection": "mommom",
        "collection_display": "MomMom Baker",
        "title": "Garnishing Techniques",
        "category": "tips",
        "attribution": "Better Homes and Gardens",
        "source_note": "BHG Cookbook - Special Helps section",
        "description": "Easy garnishing ideas to make everyday meals special.",
        "content": "Make even the most everyday meal seem special with these easy-to-do garnishes. 1. Radish Accordions: Make 8 to 10 narrow crosswise cuts 1/4 inch apart in long narrow radishes, cutting only partially through each radish. (To keep from cutting through the radishes, place them between two parallel wooden sticks when cutting.) Place the radishes in ice water so the slices fan out. Use with meats or salads. 2. Citrus Twists: Thinly slice lemons, limes, and oranges. Cut into center of each slice; twist ends in opposite directions. Use with fish and citrus or cream pies. 3. Fluted Mushrooms: With a paring knife held at an angle, and beginning at the top of each mushroom cap, make cuts in the form of an inverted V. Turn mushroom slightly; cut another inverted V; repeat around cap. For a similar effect, make a series of slight indentations in mushroom cap with a punch-type can opener. Use with salads and meats. 4. Tomato Roses: Cut a base from the stem end of each tomato (do not sever). Cut a continuous narrow strip in spiral fashion, tapering end to remove. Curl strip onto its base in a rose shape. Use with salads and dips. 5. Scored Cucumbers: Make a V-shape cut lengthwise down each cucumber (or run the tines of a fork lengthwise down each cucumber, pressing to break the skin). Repeat at regular intervals around cucumber. Slice or bias-slice. Use with salads and dips. 6. Onion Brushes: Slice roots from ends of green onions; remove most of green portion. Make slashes at both ends of the onion pieces to make fringes. Place in ice water to curl the ends. Use with steaks or roasts. 7. Carrot Curls/Zigzags: Using a vegetable peeler, cut thin lengthwise strips from carrots. For curls, roll up; secure with toothpicks. For zigzags, thread on toothpicks accordion-style. Put curls and zigzags in ice water; remove toothpicks before using. Use with salads, sauces, and thickened soups. 8. Chocolate Curls/Grated Chocolate: For curls, use a bar of chocolate at room temperature. Carefully draw a vegetable peeler across the chocolate, making thin strips that curl. To grate, rub a cool, firm square of chocolate across a hand grater. Use to garnish cakes, tortes, custards, or ice-cream drinks.",
        "tags": ["tip", "garnish", "presentation", "technique", "bhg"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": ["IMG_5600 Large.jpeg"]
    }
]


def main():
    print(f"Loading recipes from {RECIPES_FILE}")
    with open(RECIPES_FILE, 'r') as f:
        data = json.load(f)

    recipes = data['recipes']
    existing_ids = {r['id'] for r in recipes}

    added_recipes = 0
    added_tips = 0
    skipped = 0

    # Add missing recipes
    print("\nAdding missing recipes...")
    for recipe in MISSING_RECIPES:
        if recipe['id'] in existing_ids:
            print(f"  Skipping (exists): {recipe['id']}")
            skipped += 1
        else:
            recipes.append(recipe)
            existing_ids.add(recipe['id'])
            print(f"  Added: {recipe['title']}")
            added_recipes += 1

    # Add tips and techniques
    print("\nAdding tips and techniques...")
    for tip in TIPS_AND_TECHNIQUES:
        if tip['id'] in existing_ids:
            print(f"  Skipping (exists): {tip['id']}")
            skipped += 1
        else:
            recipes.append(tip)
            existing_ids.add(tip['id'])
            print(f"  Added: {tip['title']}")
            added_tips += 1

    # Update total count
    data['meta']['total_recipes'] = len(recipes)

    print(f"\nWriting {len(recipes)} recipes back to {RECIPES_FILE}")
    with open(RECIPES_FILE, 'w') as f:
        json.dump(data, f, indent=2)

    print(f"\nDone!")
    print(f"  Added {added_recipes} recipes")
    print(f"  Added {added_tips} tips/techniques")
    print(f"  Skipped {skipped} existing")
    print(f"  Total recipes now: {len(recipes)}")


if __name__ == "__main__":
    main()
