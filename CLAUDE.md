# MomMom's Kitchen — AI Assistant Context

**Version:** 2.0 (lean hub)
**Last updated:** 2026-05-01

> **Soli Deo Gloria.** A labor of love by a Reformed Baptist family. Real
> people will eat from these recipes — accuracy matters more than speed.

This repo is a **standalone collection** holding **MomMom Baker's recipes**. It
is part of the multi-repo Family Recipe Archive (Grandma, Granny, Reference).

---

## Quick Start (read first)

1. **Image API limit is 2000 px.** Always read from `data/processed/`, not `data/`.
2. **PDF API limit is 100 pages / 50 MB.** Use `scripts/pdf_safeguards.py` for big books.
3. **Never invent** ingredients, steps, temperatures, times, or yields.
4. **Mark unclear text `[UNCLEAR]`.** Don't guess.
5. **Run `python scripts/validate-recipes.py`** before every commit.
6. **Every recipe must have `"collection": "mommom"`.**

When sources conflict: accuracy → preservation → fidelity → readability.

---

## Essential Reading

### Standards (extracted)

| File | What it covers |
|---|---|
| [`.claude/standards/OCR_STANDARDS.md`](.claude/standards/OCR_STANDARDS.md) | OCR error patterns, measurement standardization, temperature format |
| [`.claude/standards/IMAGE_WORKFLOW.md`](.claude/standards/IMAGE_WORKFLOW.md) | Image processing, 2000 px limit, manifest commands |
| [`.claude/standards/PDF_WORKFLOW.md`](.claude/standards/PDF_WORKFLOW.md) | PDF size limits, text extraction, Foxfire workflow |
| [`.claude/standards/RECIPE_SCHEMA.md`](.claude/standards/RECIPE_SCHEMA.md) | Full recipe JSON schema with conversion + nutrition fields |
| [`.claude/standards/SESSION_MANAGEMENT.md`](.claude/standards/SESSION_MANAGEMENT.md) | Resuming sessions, naming, picker shortcuts |

### Operations

| File | What it covers |
|---|---|
| [`MAINTENANCE.md`](MAINTENANCE.md) | Routine maintenance schedules and checklists |
| [`SCRIPTS.md`](SCRIPTS.md) | Every script with usage examples |
| [`DATA_SCHEMA.md`](DATA_SCHEMA.md) | Recipe JSON schema (canonical) |
| [`TROUBLESHOOTING.md`](TROUBLESHOOTING.md) | Common errors and fixes |
| [`requirements.txt`](requirements.txt) | Python dependencies |

---

## Repository at a Glance

```
MomsRecipes/
├── CLAUDE.md                 # This hub
├── MAINTENANCE.md            # Routine maintenance procedures
├── DATA_SCHEMA.md            # Canonical recipe schema
├── SCRIPTS.md                # Script catalogue
├── TROUBLESHOOTING.md        # Known issues + fixes
├── README.md                 # Public-facing overview
├── requirements.txt          # Python deps
├── index.html / recipe.html  # Static site
├── styles.css / script.js    # Site bundle
├── data/
│   ├── *.jpeg                # Originals (4032×3024 — DO NOT read directly)
│   ├── processed/            # AI-safe ≤2000 px copies — USE THESE
│   ├── recipes.json          # ~2,700+ recipes
│   ├── recipes-index.json    # Generated browse index
│   ├── recipes-{cat}.json    # Generated category shards
│   ├── collections.json      # Collection metadata
│   ├── foraging_tips.json    # Foraging tips & safety rules
│   ├── image_manifest.json   # Image validation status
│   └── pdf_manifest.json     # PDF validation status
├── scripts/
│   ├── validate-recipes.py
│   ├── process_images.py     # Resize for AI
│   ├── image_safeguards.py   # Manifest + size detection
│   ├── pdf_safeguards.py     # PDF size + text extraction
│   ├── optimize_images.py    # JPEG optimization
│   ├── create_shards.py      # Regenerate category shards
│   └── add_*.py              # Recipe ingestion scripts (37+)
├── .claude/standards/        # Extracted reference files (see above)
└── ebook/
    ├── book.html             # Print-optimized
    └── print.css
```

---

## Non-Negotiable Rules

1. Do NOT invent ingredients, steps, temperatures, times, or yields.
2. Mark unreadable / ambiguous text as `[UNCLEAR]` — never guess.
3. Preserve original intent; normalize only spelling and formatting.
4. Keep family names and attributions.
5. Never discard a `image_refs` reference, even on merged duplicates.
6. Every recipe must have `"collection": "mommom"`.
7. Never read images >2000 px directly — use `data/processed/`.
8. Never load a PDF >100 pages or >50 MB without first running `pdf_safeguards.py`.

---

## Recipe Sources

| Source | Batches | Recipes | Notes |
|---|---|---|---|
| MomMom's Cards | — | ~800 | Original family recipes |
| Eat the Weeds | 1–12 | ~157 | Wild edibles, foraging |
| Honest Food | 1–5 | ~45 | Wild game, unusual meats |
| Foxfire Books | Multiple | ~35 | Appalachian heritage |
| BHG Cookbooks | 1 | Various | Better Homes & Gardens |

---

## Maintenance Cheat Sheet

```bash
# Quick health check
python scripts/validate-recipes.py
python scripts/image_safeguards.py status
ls data/processing_log_*.json 2>/dev/null | wc -l

# After bulk recipe additions (10+)
python scripts/validate-recipes.py
python scripts/create_shards.py
```

Full procedures live in [`MAINTENANCE.md`](MAINTENANCE.md).

---

## Version History

| Version | Date | Changes |
|---|---|---|
| 2.0 | 2026-05-01 | Lean hub restructure. Extracted OCR / image / PDF / schema / session subfiles into `.claude/standards/`. CLAUDE.md cut from ~391 lines to ~120. |
| 1.x | 2026-01..03 | Original monolithic context file. |

---

*"She looketh well to the ways of her household, and eateth not the bread of idleness."* — Proverbs 31:27
