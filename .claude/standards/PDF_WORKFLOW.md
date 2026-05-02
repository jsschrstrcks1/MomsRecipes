# PDF Workflow — MomMom's Kitchen

Large PDFs can crash AI sessions. Always validate before reading.

## Size Limits

| Metric | Soft | Hard | Action |
|---|---|---|---|
| File size | 10 MB | 50 MB | Extract text |
| Page count | 100 | 500 | Use page ranges or extract |
| Page dimensions | — | 2000 px | May affect embedded images |

## Always Validate First

```bash
python scripts/pdf_safeguards.py validate
```

## Status & Extraction Commands

```bash
# Validate all PDFs in data/
python scripts/pdf_safeguards.py validate

# Current status
python scripts/pdf_safeguards.py status

# Detail on a specific PDF
python scripts/pdf_safeguards.py info "Foxfire-Book-2.pdf"

# Extract text from oversized PDF
python scripts/pdf_safeguards.py extract "Foxfire-Book-2.pdf"

# Mark as processed
python scripts/pdf_safeguards.py mark "foxfire-three.pdf" processed
```

## Workflow for Large PDFs

1. **Validate** — `python scripts/pdf_safeguards.py validate`
2. **If oversized** — extract text via `python scripts/pdf_safeguards.py extract <file>`
3. **Process** — work with the `.txt` (or `.txt.html`) output, not the raw PDF
4. **Example** — `FoxfireVol1.txt.html` was used in place of the raw PDF

## Current PDF Status

- `Foxfire-Book-2.pdf` (18 MB) — large, text extraction recommended
- `foxfire-three.pdf` (17 MB) — large, text extraction recommended
- `FoxfireVol1.txt.html` — already extracted, recipes processed
