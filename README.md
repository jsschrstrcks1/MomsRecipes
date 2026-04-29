# MomMom's Kitchen

A treasured collection of family recipes passed down through generations
of MomMom Baker — handwritten cards, magazine clippings, and treasured
family sources, preserved as a static website and a printable e-book.

> *Soli Deo Gloria.*

---

## Table of Contents

- [About this project](#about-this-project)
- [Family Recipe Archive (multi-repo)](#family-recipe-archive-multi-repo)
- [Project structure](#project-structure)
- [Quick start](#quick-start)
- [Image processing](#image-processing)
- [Adding new recipes](#adding-new-recipes)
- [Recipe JSON schema](#recipe-json-schema)
- [Validation](#validation)
- [Maintenance](#maintenance)
- [Multi-LLM integration](#multi-llm-integration)
- [Contributing](#contributing)
- [License](#license)

---

## About this project

This archive preserves **MomMom Baker's recipes** — collected from
handwritten cards, magazine clippings, and treasured family sources.
The site is fully static (HTML + CSS + vanilla JS) and runs anywhere
that serves files: GitHub Pages, Netlify, Vercel, a Raspberry Pi, an
SD card.

This is a **standalone collection repository**, part of the larger
Family Recipe Archive system documented below.

---

## Family Recipe Archive (multi-repo)

The Baker / Hudson recipe collection is split across several repos so
each cook keeps her own kitchen:

| Repo | Collection |
|---|---|
| **MomsRecipes** | **MomMom Baker** *(this repo)* |
| [Grandmasrecipes](https://github.com/jsschrstrcks1/Grandmasrecipes) | Grandma Baker (Michigan → Florida) |
| [Grannysrecipes](https://github.com/jsschrstrcks1/Grannysrecipes) | Granny Hudson (Florida → Boston → back) |
| [Allrecipes](https://github.com/jsschrstrcks1/Allrecipes) | Reference cookbooks & magazines |

Each repo follows the same data shape (`recipes.json` or
`recipes_master.json`) and the same UI shell, so a future Family Recipe
Hub can aggregate them by reading their JSON directly.

---

## Project structure

```
MomsRecipes/
├── CLAUDE.md                  # AI assistant context & guidelines
├── DATA_SCHEMA.md             # Full JSON schema reference
├── MAINTENANCE.md             # Operational runbook
├── SCRIPTS.md                 # Script catalogue with usage
├── TROUBLESHOOTING.md         # Common problems and fixes
├── OVERLOOKED_TIPS_AUDIT.md   # Audit of "tips that should have been captured"
├── README.md                  # This file
├── index.html                 # Home page with search & filters
├── recipe.html                # Recipe detail page
├── styles.css                 # Stylesheet
├── script.js                  # Client-side JavaScript
├── robots.txt                 # Search-engine directives
├── data/
│   ├── *.jpeg                 # Original recipe images (iPhone photos)
│   ├── processed/             # Resized images for AI processing
│   ├── recipes.json           # All recipes in structured form
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

For the full data shape see [`DATA_SCHEMA.md`](DATA_SCHEMA.md). For the
operational checklist (rebuild, regenerate ebook, ship a release) see
[`MAINTENANCE.md`](MAINTENANCE.md).

---

## Quick start

### View the site locally

```bash
# Python (recommended)
cd MomsRecipes
python -m http.server 8000

# or Node.js
npx serve .

# or PHP
php -S localhost:8000
```

Open <http://localhost:8000>.

### Host on GitHub Pages

1. Push this repository to GitHub.
2. **Settings → Pages → Source** → your default branch, root folder.
3. The site goes live at `https://<username>.github.io/MomsRecipes/`.

### Host on Netlify or Vercel

Static site, no build step. Point the publish directory at the repo root
and deploy.

---

## Image processing

MomMom's recipe images are iPhone photos (often 4032 × 3024 px), which
exceed Claude's 2000 px API limit. Before any AI processing, resize:

```bash
python scripts/process_images.py
```

This creates AI-friendly versions in `data/processed/`. Originals stay
under `data/`.

Check status anytime:

```bash
python scripts/image_safeguards.py status
```

The safeguard script refuses to commit oversized images and warns when a
processed copy is missing for a referenced original. See
[`SCRIPTS.md`](SCRIPTS.md) for every flag.

---

## Adding new recipes

1. **Photograph or scan** the source. Save to `data/` as
   `Moms Recipes - N.jpeg` (any number that doesn't collide).
2. **Resize for AI:**

   ```bash
   python scripts/process_images.py
   ```

3. **Extract** following the workflow in [`CLAUDE.md`](CLAUDE.md):
   - Analyze the scan for orientation and content.
   - Extract all recipe data following the JSON schema.
   - Add to `data/recipes.json`.
   - Update `data/processed_images.json`.
4. **Validate:**

   ```bash
   python scripts/validate-recipes.py
   ```

5. **Commit** with a message like `recipe: add MomMom's apple butter`.

If a card is illegible or instructions are missing, capture what's there
and flag the rest with `confidence.overall = "low"` and a `flags` entry
explaining what's uncertain. Honest gaps are better than invented steps.

---

## Recipe JSON schema

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

Optional fields supported by the renderer: `attribution`, `source_note`,
`description`, `servings_yield`, `prep_time`, `cook_time`, `total_time`,
`pan_size`, `notes`, `tips` (the "overlooked tips" set tracked in
`OVERLOOKED_TIPS_AUDIT.md`).

Full schema: [`DATA_SCHEMA.md`](DATA_SCHEMA.md).

---

## Validation

```bash
# JSON syntax check
python -m json.tool data/recipes.json > /dev/null && echo "JSON valid"

# Full validation
python scripts/validate-recipes.py

# Strict mode (warnings become errors)
python scripts/validate-recipes.py --strict
```

The validator checks required fields, quantity/unit shape, image
references, slug uniqueness, and category vocabulary.

---

## Maintenance

[`MAINTENANCE.md`](MAINTENANCE.md) is the operational runbook:

- Updating the e-book after adding recipes
- Rebuilding `processed_images.json`
- Regenerating the print PDF
- Backing up to a USB drive for the family
- Diagnosing search/filter regressions

[`TROUBLESHOOTING.md`](TROUBLESHOOTING.md) collects fixes for things that
have actually broken (image rotation, missing slugs, broken JSON, encoding
glitches in old text).

---

## Multi-LLM integration

This repo defaults to **`recipe` mode** in the multi-LLM orchestrator
hosted in [ken](https://github.com/jsschrstrcks1/ken).

| Skill | Usage |
|---|---|
| `/consult` | `/consult gpt structure "review this extracted recipe"` |
| `/orchestrate recipe "<task>"` | Full pipeline: extract → validate → integrate |
| Cognitive memory | Scope `/MomsRecipes` |

#### Setup (per session)

```bash
pip3 install -q -r /home/user/ken/orchestrator/requirements.txt
```

The `recipe-transcription` and `recipe-validation` skills are designed
to run inside this pipeline; they handle messy handwriting and partial
text — but they never invent steps. Anything inferred is flagged.

---

## Contributing

This is a family project. If you're family and have:

- Additional recipes from MomMom
- Corrections to existing recipes
- Memories or context about specific recipes

Please reach out, or open a PR on the
`claude/<topic>-<id>` branch pattern.

---

## License

This recipe collection is a family treasure. Please use respectfully.
The site source is published under [`LICENSE`](LICENSE) (GNU AGPL v3);
recipe text and images are family-private and not licensed for
commercial reuse.

---

*"She looketh well to the ways of her household, and eateth not the
bread of idleness." — Proverbs 31:27*
