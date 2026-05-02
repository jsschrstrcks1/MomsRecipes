# Recipe Schema — MomMom's Kitchen

Canonical reference. Mirrors `DATA_SCHEMA.md` and is what `validate-recipes.py`
enforces.

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

## Quality Checklist

- [ ] Cross-check ingredient quantities against instructions
- [ ] Flag implausible amounts (e.g., "4 cups salt" is probably an OCR error)
- [ ] Preserve original voice where possible
- [ ] Verify temperatures are reasonable (most baking: 300–425°F)
- [ ] Check liquid-to-dry ratios make sense

## Categories

`appetizers, beverages, breads, breakfast, desserts, mains, salads, sides, soups, snacks`
