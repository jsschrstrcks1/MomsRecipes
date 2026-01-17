# MomMom's Kitchen - AI Assistant Context

## Project Mission & Values

This is a labor of love being performed by a Reformed Baptist family. Our ethos is **Soli Deo Gloria** (Glory to God Alone).

This repository is a **standalone collection** containing MomMom Baker's recipes - family recipes passed down through generations.

**Accuracy is more important than speed.** There are hundreds of real people that will be impacted by these recipes. They matter deeply to this family.

---

## Standalone Collection Architecture

This repo is part of a multi-repo Family Recipe Archive:

```
MomsRecipes/           (THIS REPO - MomMom Baker)
GrandmasRecipes/       (Grandma Baker - separate repo)
GrannysRecipes/        (Granny Hudson - separate repo)
ReferenceRecipes/      (Reference cookbooks - separate repo)
FamilyRecipeHub/       (aggregator with cross-collection features)
```

### This Repository Contains ONLY:
- MomMom Baker's recipe images (`data/*.jpeg`)
- MomMom Baker's recipe data (`data/recipes.json`)
- A standalone website for browsing this collection
- Collection-specific processing scripts

### Collection Info
```json
{
  "id": "mommom",
  "display_name": "MomMom Baker",
  "description": "Family recipes passed down through generations"
}
```

---

## OCR Correction Guidelines

### Common OCR Errors to Watch For
- `l` ↔ `1` (lowercase L vs number one)
- `O` ↔ `0` (letter O vs zero)
- `rn` ↔ `m` (r-n combination vs letter m)
- `cl` ↔ `d` (c-l combination vs letter d)
- `tsp` vs `tbsp` (critical for measurements!)

### Measurement Standardization
| Original | Standardized |
|----------|-------------|
| teaspoon, t, t. | tsp |
| tablespoon, T, Tbsp, Tbs | tbsp |
| cup, c, C | cup |
| ounce, oz | oz |
| pound, lb, # | lb |

### Temperature Format
Prefer dual format: `350°F (175°C)`

---

## Image Processing

### CRITICAL: MomMom's images are iPhone photos (4032x3024px)

**API LIMIT**: Claude's API rejects images >2000px in any dimension.

**ALWAYS use processed images:**
```
CORRECT:   data/processed/*.jpeg  (resized to ≤2000px)
WRONG:     data/*.jpeg            (original 4032x3024px - TOO LARGE!)
```

**Before processing images, run:**
```bash
python scripts/process_images.py
python scripts/image_safeguards.py validate
```

### Image Status Commands
```bash
# Check manifest status
python scripts/image_safeguards.py status

# Get next unprocessed image
python scripts/image_safeguards.py next

# Mark image as processed/skipped
python scripts/image_safeguards.py mark "Moms Recipes - 1.jpeg" processed
python scripts/image_safeguards.py mark "Moms Recipes - 2.jpeg" skipped "Not a recipe"
```

---

## PDF Processing

### CRITICAL: Large PDFs can crash AI sessions

**SIZE LIMITS** for Claude's PDF reading:
| Metric | Soft Limit | Hard Limit | Action |
|--------|------------|------------|--------|
| File size | 10 MB | 50 MB | Extract text |
| Page count | 100 pages | 500 pages | Use page ranges or extract |
| Page dimensions | - | 2000px | May affect embedded images |

**ALWAYS validate PDFs first:**
```bash
python scripts/pdf_safeguards.py validate
```

### PDF Status Commands
```bash
# Check all PDFs in data/
python scripts/pdf_safeguards.py validate

# View current status
python scripts/pdf_safeguards.py status

# Get detailed info on a specific PDF
python scripts/pdf_safeguards.py info "Foxfire-Book-2.pdf"

# Extract text from oversized PDF
python scripts/pdf_safeguards.py extract "Foxfire-Book-2.pdf"

# Mark PDF as processed
python scripts/pdf_safeguards.py mark "foxfire-three.pdf" processed
```

### Workflow for Large PDFs (like Foxfire volumes)
1. **Validate**: `python scripts/pdf_safeguards.py validate`
2. **If oversized**: Extract text with `python scripts/pdf_safeguards.py extract <file>`
3. **Process**: Work with the `.txt` file instead of the raw PDF
4. **Example**: `FoxfireVol1.txt.html` was used instead of reading the PDF directly

### Current PDF Status
- `Foxfire-Book-2.pdf` (18MB) - LARGE, text extraction recommended
- `foxfire-three.pdf` (17MB) - LARGE, text extraction recommended
- `FoxfireVol1.txt.html` - Already extracted, recipes processed

---

## Recipe Schema

```json
{
  "id": "stable-slug-like-chicken-casserole",
  "collection": "mommom",
  "collection_display": "MomMom Baker",
  "title": "",
  "category": "desserts",
  "attribution": "",
  "source_note": "e.g., handwritten card, magazine clipping",
  "description": "1-2 sentences, only if supported by text",
  "servings_yield": "",
  "prep_time": "",
  "cook_time": "",
  "total_time": "",
  "ingredients": [
    {"item": "", "quantity": "", "unit": "", "prep_note": ""}
  ],
  "instructions": [
    {"step": 1, "text": ""}
  ],
  "temperature": "",
  "pan_size": "",
  "notes": [""],
  "tags": ["dessert", "holiday", "casserole"],
  "confidence": {
    "overall": "high|medium|low",
    "flags": []
  },
  "image_refs": ["Moms Recipes - 1.jpeg"],

  "conversions": {
    "has_conversions": true,
    "conversion_assumptions": [],
    "ingredients_metric": [],
    "temperature_c": ""
  },

  "nutrition": {
    "status": "complete|partial|insufficient_data",
    "per_serving": {},
    "missing_inputs": [],
    "assumptions": []
  }
}
```

---

## Project Structure

```
MomsRecipes/
├── CLAUDE.md                 # This file
├── README.md                 # Setup instructions
├── index.html                # Home page
├── recipe.html               # Recipe detail page
├── styles.css                # Stylesheet
├── script.js                 # Client-side rendering
├── data/
│   ├── *.jpeg               # Original recipe images (OVERSIZED!)
│   ├── processed/           # AI-friendly versions (≤2000px) - USE THESE!
│   │   └── *.jpeg
│   ├── recipes.json         # All recipes for this collection
│   ├── collections.json     # Collection metadata
│   ├── processed_images.json # OCR tracking log
│   └── image_manifest.json  # Image validation status
├── scripts/
│   ├── validate-recipes.py  # Recipe validation
│   ├── process_images.py    # Image resizing for AI
│   ├── image_safeguards.py  # Image size/broken detection
│   ├── pdf_safeguards.py    # PDF size validation & text extraction
│   └── optimize_images.py   # JPEG optimization
└── ebook/
    ├── book.html            # Print-optimized HTML
    └── print.css            # Print stylesheet
```

---

## Quality Checklist

- [ ] Cross-check ingredient quantities against instructions
- [ ] Flag implausible amounts (e.g., "4 cups salt" is probably an OCR error)
- [ ] Preserve original voice where possible
- [ ] Verify temperatures are reasonable (most baking: 300-425°F)
- [ ] Check that liquid-to-dry ratios make sense

---

## Non-Negotiable Rules

1. **Do NOT invent** ingredients, steps, temperatures, times, or yields
2. If anything is **unreadable or ambiguous**, mark it as `[UNCLEAR]`
3. **Preserve original intent**, but normalize spelling and formatting
4. **Keep family names/attributions** if present
5. **Never discard a scan reference** - keep all image_refs
6. **All recipes must have** `"collection": "mommom"`

---

## Validation

Run before committing:
```bash
python scripts/validate-recipes.py
```

This checks:
- Required fields present
- Valid category values
- Reasonable ingredient quantities
- Temperature sanity
- Image references exist

---

## Claude Code Session Management

### Resuming Previous Sessions

When returning to work on this project, you can resume previous Claude Code sessions:

**From the command line:**
```bash
# Resume most recent session
claude --continue

# Resume a specific named session
claude --resume recipe-ocr-batch

# Browse all sessions interactively
claude --resume
```

**Inside an active session:**
```
/resume          # Open session picker to switch sessions
/rename task-name  # Name the current session for easy resuming later
```

### Session Picker Shortcuts

| Key | Action |
|-----|--------|
| `↑` `↓` | Navigate sessions |
| `Enter` | Select session |
| `P` | Preview session content |
| `R` | Rename session |
| `/` | Search sessions |
| `Esc` | Exit picker |

### Best Practices for This Project

1. **Name sessions by task**: `/rename ocr-batch-42` or `/rename foxfire-extraction`
2. **Use descriptive names**: Include the image range or PDF being processed
3. **Continue quickly**: Use `claude --continue` when returning to finish a task
4. **Preview before resuming**: Press `P` in the picker to verify you're resuming the right session

### Deleting Old Sessions

To clean up sessions you no longer need:
```
/delete          # Delete current or selected session
```

From the session picker, navigate to a session and delete it to keep your session list manageable.
