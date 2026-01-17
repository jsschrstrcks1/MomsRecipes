# MomMom's Kitchen - Maintenance Guide

This document outlines routine maintenance tasks for the MomsRecipes repository. Follow these checklists to keep the collection healthy and performant.

---

## Quick Reference: Script Commands

```bash
# Validation (run before every commit)
python scripts/validate-recipes.py

# Image processing (after adding new images)
python scripts/process_images.py
python scripts/image_safeguards.py validate

# PDF processing (after adding new PDFs)
python scripts/pdf_safeguards.py validate

# Shard regeneration (after bulk recipe additions)
python scripts/create_shards.py

# JPEG optimization (periodic, reduces repo size)
python scripts/optimize_images.py --dry-run
python scripts/optimize_images.py
```

---

## Maintenance Schedules

### Before Every Commit

| Task | Command | Expected Output |
|------|---------|-----------------|
| Validate recipes | `python scripts/validate-recipes.py` | "0 ERROR(S)" |
| Check image refs exist | (included in validation) | No missing refs |
| Verify JSON syntax | (included in validation) | No parse errors |

**If validation fails:** See [TROUBLESHOOTING.md](TROUBLESHOOTING.md) for common fixes.

---

### After Adding New Recipe Images

Run in this order:

1. **Process images for AI compatibility**
   ```bash
   python scripts/process_images.py
   ```
   - Resizes images >2000px to fit Claude API limits
   - Creates processed versions in `data/processed/`
   - Generates `data/processing_log_YYYYMMDD_HHMMSS.json`

2. **Validate image manifest**
   ```bash
   python scripts/image_safeguards.py validate
   ```
   - Updates `data/image_manifest.json`
   - Flags broken or oversized images

3. **Check status**
   ```bash
   python scripts/image_safeguards.py status
   ```
   - Shows counts of valid/oversized/broken images

---

### After Adding New PDFs

1. **Validate PDF sizes**
   ```bash
   python scripts/pdf_safeguards.py validate
   ```
   - Checks against size limits (soft: 10MB, hard: 50MB)
   - Updates `data/pdf_manifest.json`

2. **For oversized PDFs, extract text**
   ```bash
   python scripts/pdf_safeguards.py extract "filename.pdf"
   ```
   - Creates `.txt` file for processing instead of raw PDF

3. **Mark as processed when done**
   ```bash
   python scripts/pdf_safeguards.py mark "filename.pdf" processed
   ```

---

### After Bulk Recipe Additions (10+ recipes)

1. **Validate all recipes**
   ```bash
   python scripts/validate-recipes.py
   ```

2. **Regenerate category shards**
   ```bash
   python scripts/create_shards.py
   ```
   - Updates `data/recipes-index.json`
   - Updates `data/recipes-{category}.json` files
   - **Critical:** Website uses shards for performance

3. **Verify shard counts match**
   ```bash
   python -c "import json; d=json.load(open('data/recipes.json')); print(f'Master: {len(d[\"recipes\"])} recipes')"
   python -c "import json; d=json.load(open('data/recipes-index.json')); print(f'Index: {len(d[\"recipes\"])} recipes')"
   ```
   - Both counts should match

---

### Monthly Maintenance

| Task | Command | Purpose |
|------|---------|---------|
| Optimize images | `python scripts/optimize_images.py` | Reduce repo size 30%+ |
| Clean old logs | See below | Remove accumulated logs |
| Review manifests | Manual check | Ensure no stale entries |
| Check dependencies | `pip list --outdated` | Security updates |

**Clean old processing logs:**
```bash
# List logs older than 30 days
find data -name "processing_log_*.json" -mtime +30

# Remove logs older than 30 days (after review)
find data -name "processing_log_*.json" -mtime +30 -delete
```

---

### Quarterly Maintenance

| Task | Purpose |
|------|---------|
| Full validation sweep | Catch any accumulated issues |
| Dependency updates | Security and compatibility |
| Backup verification | Ensure backups are current |
| Schema review | Check for needed migrations |

**Full validation sweep:**
```bash
# Run all validations
python scripts/validate-recipes.py
python scripts/image_safeguards.py validate
python scripts/pdf_safeguards.py validate

# Check for orphaned files
python scripts/image_safeguards.py status
```

---

## Data Ingestion Procedures

### Adding Recipes from a New Source

When adding recipes from a new source (like Eat the Weeds, Honest Food, etc.):

1. **Create a batch script** following the pattern:
   ```
   scripts/add_{source}_batch{N}.py
   ```

2. **Script structure:**
   ```python
   #!/usr/bin/env python3
   """Add {Source} recipes - Batch {N}"""

   import json
   from pathlib import Path

   RECIPES_FILE = Path(__file__).parent.parent / "data" / "recipes.json"

   RECIPES = [
       {
           "id": "unique-slug-source",
           "collection": "mommom",
           "collection_display": "MomMom Baker",
           "title": "Recipe Title",
           # ... full recipe schema
       },
   ]

   def main():
       with open(RECIPES_FILE, 'r') as f:
           data = json.load(f)

       existing_ids = {r['id'] for r in data['recipes']}

       for recipe in RECIPES:
           if recipe['id'] not in existing_ids:
               data['recipes'].append(recipe)
               print(f"  Added: {recipe['title']}")

       data['meta']['total_recipes'] = len(data['recipes'])

       with open(RECIPES_FILE, 'w') as f:
           json.dump(data, f, indent=2)

   if __name__ == "__main__":
       main()
   ```

3. **Run the script:**
   ```bash
   python scripts/add_{source}_batch{N}.py
   ```

4. **Post-ingestion checklist:**
   - [ ] Run `python scripts/validate-recipes.py`
   - [ ] Run `python scripts/create_shards.py`
   - [ ] Commit with descriptive message
   - [ ] Push to branch

### Existing Batch Script Inventory

| Source | Batches | Total Recipes | Status |
|--------|---------|---------------|--------|
| Eat the Weeds | 1-12 | ~157 | Complete |
| Honest Food | 1-5 | ~45 | In progress |
| Foxfire | Multiple | ~35 | Complete |
| BHG (Better Homes) | 1 | Various | Complete |

---

## Shard System

### What Are Shards?

The website loads recipes in two stages for performance:
1. **Index** (`recipes-index.json`) - Minimal metadata for browsing/search
2. **Category shards** (`recipes-{category}.json`) - Full recipes loaded on-demand

### When to Regenerate Shards

Regenerate shards when:
- Adding 10+ recipes at once
- Changing recipe categories
- Modifying recipe IDs
- After any bulk data operation

**Command:**
```bash
python scripts/create_shards.py
```

### Shard Files Generated

| File | Purpose | Size |
|------|---------|------|
| `recipes-index.json` | Browse/search index | ~1.1 MB |
| `recipes-appetizers.json` | Appetizer recipes | Varies |
| `recipes-beverages.json` | Beverage recipes | Varies |
| `recipes-breads.json` | Bread recipes | Varies |
| `recipes-breakfast.json` | Breakfast recipes | Varies |
| `recipes-desserts.json` | Dessert recipes | Varies |
| `recipes-main dishes.json` | Main dish recipes | Varies |
| `recipes-salads.json` | Salad recipes | Varies |
| `recipes-sides.json` | Side dish recipes | Varies |
| `recipes-soups.json` | Soup recipes | Varies |
| ... | (32 total category files) | ... |

### Verifying Shard Freshness

```bash
# Compare timestamps
ls -la data/recipes.json data/recipes-index.json

# Compare recipe counts
python3 << 'EOF'
import json
master = json.load(open('data/recipes.json'))
index = json.load(open('data/recipes-index.json'))
print(f"Master: {len(master['recipes'])} recipes")
print(f"Index:  {len(index['recipes'])} recipes")
if len(master['recipes']) != len(index['recipes']):
    print("WARNING: Shards are STALE - run create_shards.py")
else:
    print("OK: Shards are current")
EOF
```

---

## Manifest Files

### Image Manifest (`data/image_manifest.json`)

Tracks the validation status of all images:

| Status | Meaning |
|--------|---------|
| `valid` | Image is within size limits |
| `oversized` | Image exceeds 2000px limit |
| `resized` | Image was resized to fit limits |
| `broken` | Image file is corrupted |
| `recoverable` | Broken but can be recovered |
| `processed` | OCR/transcription complete |
| `skipped` | Not a recipe (notes, etc.) |

**Commands:**
```bash
python scripts/image_safeguards.py status        # View summary
python scripts/image_safeguards.py next          # Get next to process
python scripts/image_safeguards.py mark "file" status  # Update status
```

### PDF Manifest (`data/pdf_manifest.json`)

Tracks PDF validation and processing status:

| Status | Meaning |
|--------|---------|
| `valid` | PDF within size limits |
| `large` | Exceeds soft limit (10MB), extraction recommended |
| `oversized` | Exceeds hard limit (50MB) |
| `extracted` | Text extracted to .txt file |
| `processed` | Recipes extracted from this PDF |

**Size Limits:**
| Metric | Soft Limit | Hard Limit |
|--------|------------|------------|
| File size | 10 MB | 50 MB |
| Page count | 100 pages | 500 pages |

---

## Backup Procedures

### Critical Files to Back Up

| File | Size | Criticality |
|------|------|-------------|
| `data/recipes.json` | ~8 MB | CRITICAL |
| `data/*.jpeg` (originals) | ~500 MB | CRITICAL |
| `data/image_manifest.json` | ~500 KB | Important |
| `data/pdf_manifest.json` | ~4 KB | Important |
| `data/foraging_tips.json` | ~50 KB | Important |

### Backup Strategy

1. **Git provides version history** - All committed changes are recoverable
2. **GitHub is off-site backup** - Push regularly
3. **Local backups recommended** for large binary files (images)

### Recovery from Backup

If `recipes.json` becomes corrupted:
```bash
# Restore from git history
git checkout HEAD~1 -- data/recipes.json

# Or from a specific commit
git checkout abc1234 -- data/recipes.json
```

---

## Log File Management

### Processing Logs

Location: `data/processing_log_YYYYMMDD_HHMMSS.json`

These accumulate with each `process_images.py` run. Clean periodically:

```bash
# View all logs
ls -la data/processing_log_*.json

# Count logs
ls data/processing_log_*.json | wc -l

# Remove logs older than 30 days
find data -name "processing_log_*.json" -mtime +30 -delete
```

### Optimization Manifest

Location: `data/optimization_manifest.json`

Tracks which images have been optimized. Do not delete - prevents re-optimization.

---

## Health Checks

### Quick Health Check

Run this to verify repository health:

```bash
#!/bin/bash
echo "=== MomsRecipes Health Check ==="

echo -e "\n1. Recipe count:"
python3 -c "import json; print(f\"  {len(json.load(open('data/recipes.json'))['recipes'])} recipes\")"

echo -e "\n2. Validation:"
python scripts/validate-recipes.py 2>&1 | tail -5

echo -e "\n3. Image status:"
python scripts/image_safeguards.py status 2>&1 | head -10

echo -e "\n4. Shard freshness:"
python3 -c "
import json
m = len(json.load(open('data/recipes.json'))['recipes'])
i = len(json.load(open('data/recipes-index.json'))['recipes'])
print(f'  Master: {m}, Index: {i}')
print('  ' + ('OK' if m == i else 'STALE - regenerate shards'))
"

echo -e "\n5. Processing logs:"
echo "  $(ls data/processing_log_*.json 2>/dev/null | wc -l) log files"

echo -e "\n=== Health Check Complete ==="
```

### Full Validation Suite

```bash
# Run all validators
python scripts/validate-recipes.py
python scripts/image_safeguards.py validate
python scripts/pdf_safeguards.py validate

# Check for stale shards
python scripts/create_shards.py --dry-run  # if available
```

---

## Troubleshooting Quick Reference

| Issue | Solution |
|-------|----------|
| Validation errors | See [TROUBLESHOOTING.md](TROUBLESHOOTING.md) |
| Missing image refs | Add images to `data/` or remove refs from recipe |
| Oversized images | Run `python scripts/process_images.py` |
| Stale shards | Run `python scripts/create_shards.py` |
| Corrupted JSON | Restore from git: `git checkout HEAD~1 -- data/recipes.json` |
| Missing dependencies | Run `pip install -r requirements.txt` |

---

## Related Documentation

- [CLAUDE.md](CLAUDE.md) - AI assistant guidelines
- [DATA_SCHEMA.md](DATA_SCHEMA.md) - Recipe JSON schema reference
- [SCRIPTS.md](SCRIPTS.md) - Complete script documentation
- [TROUBLESHOOTING.md](TROUBLESHOOTING.md) - Common issues and fixes
- [README.md](README.md) - Project overview
