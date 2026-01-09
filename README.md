# MomMom's Kitchen

A treasured collection of family recipes passed down through generations.

> *Soli Deo Gloria*

---

## About This Project

This archive preserves MomMom Baker's recipes - family favorites collected from handwritten cards, magazine clippings, and treasured family sources.

This is a **standalone collection repository**, part of the larger Family Recipe Archive system.

---

## Project Structure

```
MomsRecipes/
├── CLAUDE.md                  # AI assistant context & guidelines
├── README.md                  # This file
├── index.html                 # Home page with search & filters
├── recipe.html                # Recipe detail page
├── styles.css                 # Stylesheet
├── script.js                  # Client-side JavaScript
├── data/
│   ├── *.jpeg                 # Original recipe images (iPhone photos)
│   ├── processed/             # Resized images for AI processing
│   ├── recipes.json           # All recipes in structured format
│   ├── collections.json       # Collection metadata
│   └── processed_images.json  # Scan processing log
├── scripts/
│   ├── validate-recipes.py    # Recipe validation
│   ├── process_images.py      # Image resizing
│   ├── image_safeguards.py    # Image validation
│   └── optimize_images.py     # JPEG optimization
└── ebook/
    ├── book.html              # Print-optimized e-book HTML
    └── print.css              # Print stylesheet
```

---

## Quick Start

### View the Website Locally

1. **Using Python (recommended):**
   ```bash
   cd MomsRecipes
   python -m http.server 8000
   ```
   Then open http://localhost:8000 in your browser.

2. **Using Node.js:**
   ```bash
   npx serve .
   ```

### Host on GitHub Pages

1. Push this repository to GitHub
2. Go to **Settings > Pages**
3. Set source to your main branch
4. Your site will be live at `https://yourusername.github.io/MomsRecipes/`

---

## Image Processing

MomMom's recipe images are iPhone photos (4032x3024px), which exceed Claude's 2000px limit.

**Before AI processing, resize images:**
```bash
python scripts/process_images.py
```

This creates AI-friendly versions in `data/processed/`.

**Check image status:**
```bash
python scripts/image_safeguards.py status
```

---

## Adding New Recipes

### 1. Add Your Recipe Image

- Save image to `data/` folder
- Name format: `Moms Recipes - N.jpeg`

### 2. Process the Image

```bash
python scripts/process_images.py
```

### 3. Extract the Recipe

Follow the workflow in `CLAUDE.md`:
1. Analyze the scan for orientation and content
2. Extract all recipe data following the JSON schema
3. Add to `data/recipes.json`
4. Update `data/processed_images.json`

### 4. Validate

```bash
python scripts/validate-recipes.py
```

---

## Recipe JSON Schema

```json
{
  "id": "recipe-slug",
  "collection": "mommom",
  "collection_display": "MomMom Baker",
  "title": "Recipe Title",
  "category": "desserts|mains|sides|etc",
  "ingredients": [
    {"item": "flour", "quantity": "2", "unit": "cups", "prep_note": "sifted"}
  ],
  "instructions": [
    {"step": 1, "text": "Preheat oven to 350°F."}
  ],
  "temperature": "350°F (175°C)",
  "tags": ["dessert", "holiday"],
  "confidence": {"overall": "high|medium|low"},
  "image_refs": ["Moms Recipes - 1.jpeg"]
}
```

---

## Family Recipe Archive

This repository is part of a multi-repo system:

| Repository | Collection |
|------------|------------|
| **MomsRecipes** | MomMom Baker (this repo) |
| GrandmasRecipes | Grandma Baker |
| GrannysRecipes | Granny Hudson |
| ReferenceRecipes | Reference cookbooks |
| FamilyRecipeHub | Aggregator & cross-collection search |

---

## Validation

```bash
# Check JSON syntax
python -m json.tool data/recipes.json > /dev/null && echo "JSON valid"

# Full validation
python scripts/validate-recipes.py
```

---

## Contributing

This is a family project. If you're family and have:
- Additional recipes from MomMom
- Corrections to existing recipes
- Memories or context about specific recipes

Please reach out!

---

## License

This recipe collection is a family treasure. Please use respectfully.

---

*"She looketh well to the ways of her household, and eateth not the bread of idleness."*
— Proverbs 31:27
