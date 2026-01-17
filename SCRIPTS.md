# MomMom's Kitchen - Scripts Reference

Complete documentation for all scripts in the `scripts/` directory.

---

## Quick Reference

| Script | Purpose | When to Run |
|--------|---------|-------------|
| `validate-recipes.py` | Validate recipe data | Before every commit |
| `process_images.py` | Resize oversized images | After adding new images |
| `image_safeguards.py` | Image validation & tracking | After image processing |
| `optimize_images.py` | Compress JPEGs | Monthly or when repo grows |
| `pdf_safeguards.py` | PDF validation & extraction | After adding new PDFs |
| `create_shards.py` | Generate category shards | After bulk recipe additions |

---

## Core Scripts

### validate-recipes.py

**Purpose:** Validates all recipes against the schema and sanity checks.

**Usage:**
```bash
python scripts/validate-recipes.py
python scripts/validate-recipes.py --strict    # Fail on warnings too
```

**What It Checks:**
- Required fields present (id, title, ingredients, instructions, category)
- Valid category values
- Reasonable ingredient quantities (e.g., no "4 cups salt")
- Temperature sanity (200-550°F range)
- Image references exist in data/ directory
- No duplicate recipe IDs
- Confidence levels are valid (high/medium/low)

**Output:**
```
RECIPE VALIDATION REPORT
==============================================================
Total recipes validated: 2713

5 ERROR(S):
  ERROR [bad-recipe-id]: Missing required field: category
  ERROR [another-id]: Invalid category: "mains" (should be "main dishes")

8 WARNING(S):
  WARNING [salt-heavy]: Suspicious quantity: 4 cups salt
  WARNING [cold-oven]: Low temperature: 150°F

==============================================================
Validation FAILED with 5 errors
```

**Exit Codes:**
- `0` - All validations passed
- `1` - Errors found

---

### process_images.py

**Purpose:** Resizes images larger than 2000px to fit Claude API limits.

**Usage:**
```bash
python scripts/process_images.py                # Process all images
python scripts/process_images.py --dry-run      # Preview only, no changes
python scripts/process_images.py --fix-broken   # Attempt to recover corrupted
```

**Input:** `data/*.jpeg` (original iPhone photos, 4032x3024px)

**Output:**
- `data/processed/*.jpeg` (resized to ≤2000px)
- `data/processing_log_YYYYMMDD_HHMMSS.json` (processing log)

**Key Features:**
- Maintains aspect ratio when resizing
- Preserves EXIF orientation data
- Skips already-processed images
- Creates detailed processing log

**When to Run:**
- After adding new recipe images to `data/`
- Before attempting OCR on new images

---

### image_safeguards.py

**Purpose:** Validates images and maintains the image manifest.

**Usage:**
```bash
python scripts/image_safeguards.py validate     # Validate all images
python scripts/image_safeguards.py status       # Show processing status
python scripts/image_safeguards.py next         # Get next unprocessed image
python scripts/image_safeguards.py mark "Moms Recipes - 1.jpeg" processed
python scripts/image_safeguards.py mark "Moms Recipes - 2.jpeg" skipped "Not a recipe"
```

**Manifest File:** `data/image_manifest.json`

**Status Values:**
| Status | Meaning | Action |
|--------|---------|--------|
| `valid` | Within size limits | Ready for processing |
| `oversized` | Exceeds 2000px | Run process_images.py |
| `resized` | Has processed version | Use processed version |
| `broken` | Corrupted file | Attempt recovery or skip |
| `processed` | OCR complete | Recipes extracted |
| `skipped` | Not a recipe | No action needed |

**When to Run:**
- After `process_images.py` completes
- Before starting OCR session
- To check overall image status

---

### optimize_images.py

**Purpose:** Compresses JPEG files to reduce repository size.

**Usage:**
```bash
python scripts/optimize_images.py --dry-run     # Preview savings
python scripts/optimize_images.py               # Optimize all images
python scripts/optimize_images.py --quality 80  # Custom quality (default 85)
python scripts/optimize_images.py --backup      # Keep .original files
```

**Manifest File:** `data/optimization_manifest.json`

**Key Features:**
- Uses quality setting Q85 by default
- Skips images that won't benefit (≥10% savings required)
- Tracks optimized images to prevent re-processing
- Can reduce repository size by 30%+

**When to Run:**
- Monthly maintenance
- When repository size becomes unwieldy
- After large batches of new images

---

### pdf_safeguards.py

**Purpose:** Validates PDFs and extracts text from oversized files.

**Usage:**
```bash
python scripts/pdf_safeguards.py validate              # Validate all PDFs
python scripts/pdf_safeguards.py status                # Show current status
python scripts/pdf_safeguards.py info "Foxfire-Book-2.pdf"  # Detailed info
python scripts/pdf_safeguards.py extract "Foxfire-Book-2.pdf"  # Extract text
python scripts/pdf_safeguards.py mark "foxfire.pdf" processed  # Mark complete
```

**Manifest File:** `data/pdf_manifest.json`

**Size Limits:**
| Metric | Soft Limit | Hard Limit |
|--------|------------|------------|
| File size | 10 MB | 50 MB |
| Page count | 100 pages | 500 pages |

**Status Values:**
| Status | Meaning | Action |
|--------|---------|--------|
| `valid` | Within all limits | Can be read directly |
| `large` | Exceeds soft limit | Extraction recommended |
| `oversized` | Exceeds hard limit | Must extract text |
| `extracted` | Text extracted | Use .txt file |
| `processed` | Recipes extracted | Complete |

**When to Run:**
- After adding new PDF files
- Before attempting to read large PDFs

---

### create_shards.py

**Purpose:** Splits recipes.json into category-specific shards for website performance.

**Usage:**
```bash
python scripts/create_shards.py
```

**Input:** `data/recipes.json`

**Output:**
- `data/recipes-index.json` - Minimal metadata for browsing
- `data/recipes-{category}.json` - Full recipes per category (32 files)

**Generated Shard Files:**
```
recipes-index.json
recipes-appetizers.json
recipes-beverages.json
recipes-breads.json
recipes-breakfast.json
recipes-desserts.json
recipes-main dishes.json
recipes-salads.json
recipes-sides.json
recipes-soups.json
... (32 total)
```

**When to Run:**
- After adding 10+ recipes
- After changing recipe categories
- After modifying recipe IDs
- After any bulk data operation

**Verification:**
```bash
# Ensure counts match
python3 -c "
import json
m = len(json.load(open('data/recipes.json'))['recipes'])
i = len(json.load(open('data/recipes-index.json'))['recipes'])
print(f'Master: {m}, Index: {i}, Match: {m == i}')
"
```

---

## Data Ingestion Scripts

These scripts add recipes from external sources to the collection.

### Pattern

All batch scripts follow this pattern:

```python
#!/usr/bin/env python3
"""Add {Source} recipes - Batch {N}"""

import json
from pathlib import Path

RECIPES_FILE = Path(__file__).parent.parent / "data" / "recipes.json"

RECIPES = [
    {
        "id": "unique-id",
        "collection": "mommom",
        "title": "Recipe Title",
        # ... full recipe
    },
]

def main():
    with open(RECIPES_FILE, 'r') as f:
        data = json.load(f)

    existing_ids = {r['id'] for r in data['recipes']}
    added = 0

    for recipe in RECIPES:
        if recipe['id'] not in existing_ids:
            data['recipes'].append(recipe)
            print(f"  Added: {recipe['title']}")
            added += 1

    data['meta']['total_recipes'] = len(data['recipes'])

    with open(RECIPES_FILE, 'w') as f:
        json.dump(data, f, indent=2)

    print(f"Added {added} recipes. Total: {len(data['recipes'])}")

if __name__ == "__main__":
    main()
```

### Eat the Weeds Batches

| Script | Recipes | Content |
|--------|---------|---------|
| `add_eat_the_weeds_recipes.py` | ~20 | Initial batch |
| `add_eat_the_weeds_batch2.py` | ~15 | Batch 2 |
| `add_eat_the_weeds_batch3.py` | ~15 | Batch 3 |
| ... | ... | ... |
| `add_eat_the_weeds_batch12.py` | ~20 | Final batch |

**Total:** ~157 recipes from Eat the Weeds

**Content Types:** Wild edibles, foraged plants, unusual ingredients

### Honest Food Batches

| Script | Recipes | Content |
|--------|---------|---------|
| `add_honest_food_batch1.py` | 10 | Squirrel, turtle, wild boar |
| `add_honest_food_batch2.py` | 10 | Snipe, woodcock, pheasant, duck, goose, rabbit |
| `add_honest_food_batch3.py` | 9 | Bear, frog, grouse, venison |
| `add_honest_food_batch4.py` | 8 | Organ meats, doves, pigeon, carp, catfish |
| `add_honest_food_batch5.py` | 8 | Wild turkey, andouille, boudin, venison sausage |

**Total:** ~45 recipes from Honest Food (Hank Shaw)

**Content Types:** Wild game, unusual meats, Cajun/Southern

### Foxfire Batches

| Script | Recipes | Content |
|--------|---------|---------|
| `add_foxfire_recipes.py` | ~20 | Initial Appalachian recipes |
| `add_foxfire_supplemental.py` | ~15 | Additional recipes |

**Total:** ~35 recipes from Foxfire books

**Content Types:** Appalachian traditional, preservation, heritage

### Other Ingestion Scripts

| Script | Purpose |
|--------|---------|
| `add_missing_bhg_recipes.py` | Better Homes & Gardens recipes |
| `add_nutrition.py` | Add nutrition data to existing recipes |
| `estimate_nutrition.py` | Estimate nutrition from ingredients |
| `apply_cookbook_nutrition.py` | Apply cookbook nutritional data |
| `apply_meat_soup_nutrition.py` | Apply meat/soup specific nutrition |

---

## Utility Scripts

### estimate_nutrition.py

**Purpose:** Estimates nutritional values from ingredient lists.

**Usage:**
```bash
python scripts/estimate_nutrition.py
```

**What It Does:**
- Parses ingredient quantities
- Looks up nutrition data from database
- Calculates per-serving values
- Adds `nutrition` object to recipes

---

### apply_cookbook_nutrition.py

**Purpose:** Applies nutrition data extracted from cookbooks.

**Usage:**
```bash
python scripts/apply_cookbook_nutrition.py
```

---

## Running Scripts in Sequence

### After Adding New Images

```bash
# 1. Process images
python scripts/process_images.py

# 2. Validate
python scripts/image_safeguards.py validate

# 3. Check status
python scripts/image_safeguards.py status
```

### After Bulk Recipe Addition

```bash
# 1. Run ingestion script
python scripts/add_honest_food_batch5.py

# 2. Validate
python scripts/validate-recipes.py

# 3. Regenerate shards
python scripts/create_shards.py

# 4. Commit
git add data/recipes.json data/recipes-*.json scripts/add_*.py
git commit -m "Add X recipes from Source"
```

### Full Maintenance Cycle

```bash
# 1. Validate everything
python scripts/validate-recipes.py
python scripts/image_safeguards.py validate
python scripts/pdf_safeguards.py validate

# 2. Check shard freshness
python scripts/create_shards.py

# 3. Optimize images (monthly)
python scripts/optimize_images.py --dry-run
python scripts/optimize_images.py

# 4. Clean old logs
find data -name "processing_log_*.json" -mtime +30 -delete
```

---

## Script Dependencies

| Script | Requires |
|--------|----------|
| `validate-recipes.py` | Standard library only |
| `process_images.py` | Pillow |
| `image_safeguards.py` | Pillow |
| `optimize_images.py` | Pillow |
| `pdf_safeguards.py` | PyMuPDF or pypdf |
| `create_shards.py` | Standard library only |
| `add_*.py` | Standard library only |
| `*_nutrition.py` | Standard library only |

**Install dependencies:**
```bash
pip install -r requirements.txt
```

---

## Error Handling

### Common Errors

| Error | Script | Solution |
|-------|--------|----------|
| `ModuleNotFoundError: PIL` | process_images.py | `pip install Pillow` |
| `ModuleNotFoundError: fitz` | pdf_safeguards.py | `pip install PyMuPDF` |
| `JSONDecodeError` | Any | Check for JSON syntax errors |
| `FileNotFoundError` | Any | Verify file paths |
| `KeyError: 'recipes'` | Any | Verify recipes.json structure |

### Validation Errors

See [TROUBLESHOOTING.md](TROUBLESHOOTING.md) for solutions to specific validation errors.

---

## Adding New Scripts

When adding a new script:

1. **Follow naming convention:**
   - Ingestion: `add_{source}_batch{N}.py`
   - Validation: `validate_{what}.py`
   - Processing: `process_{what}.py`

2. **Include docstring:**
   ```python
   #!/usr/bin/env python3
   """
   Script purpose and description.

   Usage:
       python scripts/script_name.py [options]
   """
   ```

3. **Use consistent paths:**
   ```python
   from pathlib import Path
   RECIPES_FILE = Path(__file__).parent.parent / "data" / "recipes.json"
   ```

4. **Add to this documentation**

5. **Update MAINTENANCE.md if it's a routine task**
