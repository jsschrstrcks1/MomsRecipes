# Image Workflow — MomMom's Kitchen

## Critical: API limit is 2000 px

MomMom's images are iPhone photos at **4032 × 3024 px**. Claude's API rejects
images with any dimension > 2000 px.

```
CORRECT:   data/processed/*.jpeg     # ≤ 2000 px, AI-safe
WRONG:     data/*.jpeg                # 4032 × 3024 — TOO LARGE
```

## Before reading any image

```bash
python scripts/process_images.py
python scripts/image_safeguards.py validate
```

## Manifest Commands

```bash
# Manifest status
python scripts/image_safeguards.py status

# Get next unprocessed image
python scripts/image_safeguards.py next

# Mark images
python scripts/image_safeguards.py mark "Moms Recipes - 1.jpeg" processed
python scripts/image_safeguards.py mark "Moms Recipes - 2.jpeg" skipped "Not a recipe"
```

## Image Status Values

| Status | Meaning |
|---|---|
| `valid` | Ready to process |
| `oversized` | Valid but >2000 px (use processed version) |
| `resized` | Processed version available |
| `broken` | Cannot read (skip) |
| `processed` | Recipe extraction complete |
| `skipped` | Not a recipe |
