# MomMom's Kitchen - Troubleshooting Guide

Solutions to common issues when working with the MomsRecipes repository.

---

## Quick Fixes

| Problem | Quick Fix |
|---------|-----------|
| Validation errors | `python scripts/validate-recipes.py` then fix reported issues |
| Missing dependencies | `pip install -r requirements.txt` |
| Stale shards | `python scripts/create_shards.py` |
| Oversized images | `python scripts/process_images.py` |
| Corrupted JSON | `git checkout HEAD~1 -- data/recipes.json` |

---

## Validation Errors

### Missing Required Field

**Error:**
```
ERROR [recipe-id]: Missing required field: category
```

**Solution:**
Add the missing field to the recipe in `data/recipes.json`:

```json
{
  "id": "recipe-id",
  "title": "Recipe Title",
  "category": "main dishes",  // Add this
  "ingredients": [...],
  "instructions": [...]
}
```

**Required fields:** `id`, `title`, `ingredients`, `instructions`, `category`

---

### Invalid Category

**Error:**
```
ERROR [recipe-id]: Invalid category: "mains"
```

**Solution:**
Use one of the valid category values:

| Invalid | Valid |
|---------|-------|
| `mains` | `main dishes` |
| `entrees` | `main dishes` |
| `drinks` | `beverages` |
| `bread` | `breads` |
| `soup` | `soups` |
| `side` | `sides` |
| `dessert` | `desserts` |

---

### Suspicious Quantity

**Warning:**
```
WARNING [recipe-id]: Suspicious quantity: 4 cups salt
```

**Solutions:**

1. **OCR error** - Check original image and correct:
   - "4 cups" might be "4 tsp"
   - "1" might be "½"

2. **Actually correct** - Some recipes (like brining) use large amounts. Add to notes:
   ```json
   "notes": ["Large amount of salt is correct - this is a brine recipe"]
   ```

3. **Add confidence flag:**
   ```json
   "confidence": {
     "overall": "medium",
     "flags": ["Salt quantity verified against original"]
   }
   ```

---

### Temperature Out of Range

**Warning:**
```
WARNING [recipe-id]: Temperature out of range: 150°F
```

**Solutions:**

1. **Legitimate low temp** - Add to notes explaining why:
   ```json
   "notes": ["Low temperature is correct for slow drying/dehydrating"]
   ```

2. **OCR error** - Common mistakes:
   - "350" misread as "150"
   - "°F" misread as "°C"

3. **Missing digit** - "50°F" should be "350°F"

---

### Missing Image Reference

**Error:**
```
ERROR [recipe-id]: Image reference not found: Moms Recipes - 99.jpeg
```

**Solutions:**

1. **Image not yet added:**
   ```bash
   # Add the image to data/
   cp /path/to/image.jpeg data/"Moms Recipes - 99.jpeg"
   ```

2. **Typo in reference:**
   ```json
   // Wrong
   "image_refs": ["Moms Recipes - 99.jpeg"]
   // Correct
   "image_refs": ["Moms Recipes - 099.jpeg"]
   ```

3. **Remove reference if image doesn't exist:**
   ```json
   "image_refs": []
   ```

---

### Duplicate Recipe ID

**Error:**
```
ERROR: Duplicate recipe ID found: chicken-casserole
```

**Solution:**
Make IDs unique by adding a suffix:

```json
// Original
{"id": "chicken-casserole", ...}

// Duplicate - add distinguishing suffix
{"id": "chicken-casserole-v2", ...}
{"id": "chicken-casserole-grandmas", ...}
{"id": "chicken-casserole-hf", ...}
```

---

## Image Processing Issues

### Pillow Not Installed

**Error:**
```
ModuleNotFoundError: No module named 'PIL'
```

**Solution:**
```bash
pip install Pillow
# or
pip install -r requirements.txt
```

---

### Image Too Large for Claude API

**Error:**
```
Image exceeds 2000px limit: 4032x3024
```

**Solution:**
```bash
# Process oversized images
python scripts/process_images.py

# Use processed images (not originals)
# CORRECT:   data/processed/*.jpeg
# WRONG:     data/*.jpeg
```

---

### Broken/Corrupted Image

**Error:**
```
Cannot identify image file: data/Moms Recipes - 42.jpeg
```

**Solutions:**

1. **Attempt recovery:**
   ```bash
   python scripts/process_images.py --fix-broken
   ```

2. **Mark as broken in manifest:**
   ```bash
   python scripts/image_safeguards.py mark "Moms Recipes - 42.jpeg" broken
   ```

3. **Re-obtain original** from source if possible

---

### EXIF Orientation Issues

**Symptom:** Image appears rotated incorrectly

**Solution:**
The `process_images.py` script should handle EXIF orientation automatically. If not:

```python
from PIL import Image, ImageOps
img = Image.open("image.jpeg")
img = ImageOps.exif_transpose(img)  # Fix orientation
img.save("image_fixed.jpeg")
```

---

## PDF Processing Issues

### PyMuPDF Not Installed

**Error:**
```
ModuleNotFoundError: No module named 'fitz'
```

**Solution:**
```bash
pip install PyMuPDF
# or use alternative
pip install pypdf
```

---

### PDF Too Large

**Error:**
```
PDF exceeds size limit: 50MB (hard limit)
```

**Solution:**
```bash
# Extract text instead of reading PDF directly
python scripts/pdf_safeguards.py extract "large-file.pdf"

# This creates: large-file.txt
# Process the text file instead
```

---

### PDF Text Extraction Failed

**Error:**
```
Failed to extract text from PDF
```

**Solutions:**

1. **Try alternative library:**
   ```python
   # If PyMuPDF fails, try pypdf
   from pypdf import PdfReader
   reader = PdfReader("file.pdf")
   text = ""
   for page in reader.pages:
       text += page.extract_text()
   ```

2. **Scanned PDF (no text layer):**
   - These require OCR, not text extraction
   - Mark as needing manual processing

---

## JSON Issues

### JSONDecodeError

**Error:**
```
json.decoder.JSONDecodeError: Expecting ',' delimiter: line 1542 column 5
```

**Solutions:**

1. **Find the error location:**
   ```bash
   # Check syntax with Python
   python -m json.tool data/recipes.json > /dev/null
   ```

2. **Common JSON errors:**
   - Missing comma between items
   - Trailing comma after last item
   - Unescaped quotes in strings
   - Missing closing bracket

3. **Restore from git:**
   ```bash
   git checkout HEAD~1 -- data/recipes.json
   ```

---

### Large JSON File Slow to Edit

**Problem:** `recipes.json` (8MB) is slow to open/edit

**Solutions:**

1. **Use command-line tools:**
   ```bash
   # Pretty print
   python -m json.tool data/recipes.json | less

   # Search for specific recipe
   grep -n "recipe-id" data/recipes.json
   ```

2. **Use jq for queries:**
   ```bash
   # Count recipes
   jq '.recipes | length' data/recipes.json

   # Find recipe by ID
   jq '.recipes[] | select(.id == "recipe-id")' data/recipes.json
   ```

3. **Edit specific recipe via script:**
   ```python
   import json
   with open('data/recipes.json', 'r') as f:
       data = json.load(f)

   for r in data['recipes']:
       if r['id'] == 'target-recipe':
           r['category'] = 'new-category'
           break

   with open('data/recipes.json', 'w') as f:
       json.dump(data, f, indent=2)
   ```

---

## Shard Issues

### Stale Shards

**Symptom:** Website shows fewer recipes than `recipes.json` contains

**Solution:**
```bash
python scripts/create_shards.py
```

**Verification:**
```bash
python3 -c "
import json
m = len(json.load(open('data/recipes.json'))['recipes'])
i = len(json.load(open('data/recipes-index.json'))['recipes'])
print(f'Master: {m}, Index: {i}')
if m != i:
    print('STALE - run create_shards.py')
"
```

---

### Missing Category Shard

**Error:**
```
FileNotFoundError: data/recipes-new category.json
```

**Solution:**

1. Verify category name is valid (see DATA_SCHEMA.md)
2. Regenerate shards:
   ```bash
   python scripts/create_shards.py
   ```

---

## Git Issues

### Merge Conflict in recipes.json

**Symptom:**
```
<<<<<<< HEAD
...
=======
...
>>>>>>> branch-name
```

**Solution:**

1. **For simple conflicts** - manually edit to combine both sets of recipes

2. **For complex conflicts** - use a merge script:
   ```python
   import json

   # Load both versions
   with open('data/recipes_ours.json') as f:
       ours = json.load(f)
   with open('data/recipes_theirs.json') as f:
       theirs = json.load(f)

   # Merge by ID
   merged = {r['id']: r for r in ours['recipes']}
   for r in theirs['recipes']:
       if r['id'] not in merged:
           merged[r['id']] = r

   # Save
   result = {'meta': ours['meta'], 'recipes': list(merged.values())}
   result['meta']['total_recipes'] = len(result['recipes'])

   with open('data/recipes.json', 'w') as f:
       json.dump(result, f, indent=2)
   ```

---

### Accidentally Committed Large File

**Problem:** Committed a huge file that shouldn't be in git

**Solution:**
```bash
# Remove from git history (dangerous - backup first!)
git filter-branch --tree-filter 'rm -f path/to/large/file' HEAD

# Or use BFG Repo-Cleaner (faster)
bfg --delete-files large-file.pdf
git reflog expire --expire=now --all
git gc --prune=now --aggressive
```

---

## Website Issues

### Recipes Not Loading

**Symptoms:**
- Blank recipe list
- "Loading..." never completes
- JavaScript errors in console

**Solutions:**

1. **Check JSON syntax:**
   ```bash
   python -m json.tool data/recipes-index.json > /dev/null
   ```

2. **Regenerate shards:**
   ```bash
   python scripts/create_shards.py
   ```

3. **Check file permissions:**
   ```bash
   chmod 644 data/*.json
   ```

4. **Clear browser cache**

---

### Search Not Finding Recipes

**Cause:** Index file may be stale

**Solution:**
```bash
python scripts/create_shards.py
```

---

## Dependency Issues

### pip install fails

**Error:**
```
error: Microsoft Visual C++ 14.0 or greater is required
```

**Solution (Windows):**
1. Install Visual Studio Build Tools
2. Or use pre-built wheels:
   ```bash
   pip install --only-binary :all: Pillow PyMuPDF
   ```

---

### Version Conflicts

**Error:**
```
ERROR: pip's dependency resolver does not currently take into account...
```

**Solution:**
```bash
# Create fresh virtual environment
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
```

---

## Data Recovery

### Restore recipes.json from Git

```bash
# See recent versions
git log --oneline -10 -- data/recipes.json

# Restore from specific commit
git checkout abc1234 -- data/recipes.json

# Restore from previous commit
git checkout HEAD~1 -- data/recipes.json
```

---

### Recover Deleted Recipe

```bash
# Find commit where recipe existed
git log -p -- data/recipes.json | grep -B5 "recipe-id"

# Checkout that version
git checkout abc1234 -- data/recipes.json

# Extract just the recipe you need, then restore current version
```

---

### Rebuild Manifest from Scratch

If `image_manifest.json` is corrupted:

```bash
# Remove and regenerate
rm data/image_manifest.json
python scripts/image_safeguards.py validate
```

---

## Getting Help

If none of these solutions work:

1. **Check existing issues** on the repository
2. **Search CLAUDE.md** for related guidelines
3. **Run validation** to identify the exact problem:
   ```bash
   python scripts/validate-recipes.py
   ```
4. **Check file permissions** and paths
5. **Verify dependencies** are installed:
   ```bash
   pip list | grep -E "Pillow|PyMuPDF"
   ```

---

## Related Documentation

- [MAINTENANCE.md](MAINTENANCE.md) - Regular maintenance procedures
- [SCRIPTS.md](SCRIPTS.md) - Script reference
- [DATA_SCHEMA.md](DATA_SCHEMA.md) - JSON schema reference
- [CLAUDE.md](CLAUDE.md) - AI assistant guidelines
