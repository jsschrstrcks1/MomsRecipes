# MomMom's Kitchen - Data Schema Reference

This document defines the JSON schema for recipes and related data files.

---

## Recipe Schema

### Complete Recipe Object

```json
{
  "id": "unique-slug-identifier",
  "collection": "mommom",
  "collection_display": "MomMom Baker",
  "title": "Recipe Title",
  "category": "main dishes",
  "attribution": "Source or Author",
  "source_note": "e.g., handwritten card, magazine clipping, honest-food.net",
  "description": "1-2 sentence description of the dish",
  "servings_yield": "6 servings",
  "prep_time": "20 minutes",
  "cook_time": "45 minutes",
  "total_time": "1 hour 5 minutes",
  "ingredients": [
    {
      "item": "flour",
      "quantity": "2",
      "unit": "cups",
      "prep_note": "sifted"
    }
  ],
  "instructions": [
    {
      "step": 1,
      "text": "Preheat oven to 350°F."
    }
  ],
  "temperature": "350°F (175°C)",
  "pan_size": "9x13 inch baking dish",
  "notes": [
    "Can substitute butter for shortening",
    "Freezes well for up to 3 months"
  ],
  "tags": ["dessert", "holiday", "family-favorite"],
  "confidence": {
    "overall": "high",
    "flags": []
  },
  "image_refs": ["Moms Recipes - 42.jpeg"],
  "conversions": {
    "has_conversions": true,
    "conversion_assumptions": ["1 stick butter = 113g"],
    "ingredients_metric": [],
    "temperature_c": "175"
  },
  "nutrition": {
    "status": "complete",
    "per_serving": {
      "calories": 350,
      "protein_g": 8,
      "carbs_g": 45,
      "fat_g": 15,
      "fiber_g": 2,
      "sodium_mg": 280
    },
    "missing_inputs": [],
    "assumptions": ["Uses large eggs"]
  }
}
```

---

## Field Definitions

### Required Fields

| Field | Type | Description |
|-------|------|-------------|
| `id` | string | Unique slug identifier (lowercase, hyphens) |
| `title` | string | Recipe name |
| `ingredients` | array | List of ingredient objects |
| `instructions` | array | List of instruction objects |
| `category` | string | One of the valid categories (see below) |

### Recommended Fields

| Field | Type | Description |
|-------|------|-------------|
| `collection` | string | Always `"mommom"` for this repo |
| `collection_display` | string | Always `"MomMom Baker"` |
| `attribution` | string | Original source or author |
| `source_note` | string | Context about the original (card, clipping, etc.) |
| `description` | string | 1-2 sentence description |
| `servings_yield` | string | Number of servings or yield |
| `prep_time` | string | Preparation time |
| `cook_time` | string | Cooking time |
| `temperature` | string | Oven/cooking temperature |
| `pan_size` | string | Required pan or dish size |
| `notes` | array | Additional tips or variations |
| `tags` | array | Searchable tags |
| `confidence` | object | OCR confidence assessment |
| `image_refs` | array | Original image filenames |

### Optional Fields

| Field | Type | Description |
|-------|------|-------------|
| `total_time` | string | Total time (prep + cook) |
| `conversions` | object | Metric conversions |
| `nutrition` | object | Nutritional information |

---

## Valid Categories

Recipes must use one of these category values:

| Category | Description |
|----------|-------------|
| `appetizers` | Starters, finger foods, party snacks |
| `beverages` | Drinks, punches, cocktails |
| `breads` | Yeast breads, quick breads, rolls |
| `breakfast` | Morning meals, brunch items |
| `desserts` | Cakes, cookies, pies, sweets |
| `main dishes` | Entrees, primary courses |
| `salads` | Green salads, pasta salads, slaws |
| `sides` | Vegetables, starches, accompaniments |
| `soups` | Soups, stews, chilis |
| `snacks` | Light bites, between-meal foods |
| `condiments` | Sauces, dressings, preserves |
| `canning` | Preserved foods, pickles, jams |
| `wild game` | Game meats, unusual proteins |
| `foraging` | Foraged/wild plant recipes |

---

## Ingredient Object

```json
{
  "item": "all-purpose flour",
  "quantity": "2",
  "unit": "cups",
  "prep_note": "sifted"
}
```

| Field | Required | Description |
|-------|----------|-------------|
| `item` | Yes | Ingredient name |
| `quantity` | No | Amount (can be empty for "to taste") |
| `unit` | No | Measurement unit |
| `prep_note` | No | Preparation instructions |

### Unit Standardization

| Original | Standardized |
|----------|--------------|
| teaspoon, t, t. | `tsp` |
| tablespoon, T, Tbsp, Tbs | `tbsp` |
| cup, c, C | `cup` |
| ounce, oz | `oz` |
| pound, lb, # | `lb` |
| quart, qt | `quart` |
| gallon, gal | `gallon` |

---

## Instruction Object

```json
{
  "step": 1,
  "text": "Preheat oven to 350°F (175°C)."
}
```

| Field | Required | Description |
|-------|----------|-------------|
| `step` | Yes | Step number (1-indexed) |
| `text` | Yes | Instruction text |

---

## Confidence Object

Used to track OCR accuracy and flag uncertainties:

```json
{
  "overall": "high",
  "flags": ["quantity unclear on line 3", "temperature may be 350 or 375"]
}
```

| Field | Values | Description |
|-------|--------|-------------|
| `overall` | `high`, `medium`, `low` | Overall transcription confidence |
| `flags` | array of strings | Specific uncertainties |

---

## Nutrition Object

```json
{
  "status": "complete",
  "per_serving": {
    "calories": 350,
    "protein_g": 8,
    "carbs_g": 45,
    "fat_g": 15,
    "saturated_fat_g": 5,
    "fiber_g": 2,
    "sugar_g": 12,
    "sodium_mg": 280,
    "cholesterol_mg": 45
  },
  "missing_inputs": [],
  "assumptions": ["Uses large eggs", "Calculated with whole milk"]
}
```

| Status Value | Meaning |
|--------------|---------|
| `complete` | All major nutrients calculated |
| `partial` | Some nutrients estimated |
| `insufficient_data` | Too many unknowns for reliable estimate |

---

## Tags

Common tags used in the collection:

### Meal Type
`breakfast`, `lunch`, `dinner`, `snack`, `appetizer`, `dessert`

### Dietary
`vegetarian`, `vegan`, `gluten-free`, `dairy-free`, `low-carb`, `keto`

### Occasion
`holiday`, `christmas`, `thanksgiving`, `easter`, `birthday`, `potluck`, `party`

### Cooking Method
`baked`, `fried`, `grilled`, `slow-cooker`, `instant-pot`, `no-bake`, `one-pot`

### Origin/Style
`southern`, `cajun`, `mexican`, `italian`, `chinese`, `french`, `german`

### Special Categories
`wild game`, `foraging`, `unusual`, `organ meat`, `preservation`, `fermented`

### Family
`family-favorite`, `grandmas-recipe`, `church-cookbook`, `heritage`

---

## Data Files

### Primary Data File

**`data/recipes.json`**

```json
{
  "meta": {
    "collection": "mommom",
    "collection_display": "MomMom Baker",
    "total_recipes": 2713,
    "last_updated": "2024-01-15"
  },
  "recipes": [
    { /* recipe object */ },
    { /* recipe object */ }
  ]
}
```

### Index File

**`data/recipes-index.json`**

Minimal metadata for browsing/search (generated by `create_shards.py`):

```json
{
  "meta": {
    "total_recipes": 2713,
    "generated": "2024-01-15T10:30:00Z"
  },
  "recipes": [
    {
      "id": "recipe-slug",
      "title": "Recipe Title",
      "category": "desserts",
      "tags": ["holiday", "family-favorite"],
      "description": "Brief description"
    }
  ]
}
```

### Category Shard Files

**`data/recipes-{category}.json`**

Full recipes for a single category (generated by `create_shards.py`):

```json
{
  "category": "desserts",
  "count": 245,
  "recipes": [
    { /* full recipe object */ }
  ]
}
```

---

## Manifest Files

### Image Manifest

**`data/image_manifest.json`**

```json
{
  "generated": "2024-01-15T10:30:00Z",
  "images": {
    "Moms Recipes - 1.jpeg": {
      "status": "processed",
      "dimensions": [4032, 3024],
      "size_bytes": 2456789,
      "processed_path": "data/processed/Moms Recipes - 1.jpeg"
    }
  }
}
```

| Status | Meaning |
|--------|---------|
| `valid` | Within size limits |
| `oversized` | Exceeds 2000px |
| `resized` | Has been resized |
| `broken` | Corrupted file |
| `processed` | OCR complete |
| `skipped` | Not a recipe |

### PDF Manifest

**`data/pdf_manifest.json`**

```json
{
  "generated": "2024-01-15T10:30:00Z",
  "pdfs": {
    "Foxfire-Book-2.pdf": {
      "status": "large",
      "size_mb": 18.5,
      "page_count": 450,
      "text_extracted": true,
      "recipes_extracted": 15
    }
  }
}
```

---

## Auxiliary Data Files

### Foraging Tips

**`data/foraging_tips.json`**

```json
{
  "meta": {
    "total_tips": 75,
    "sources": ["Eat the Weeds", "Foxfire"]
  },
  "safety_rules": [...],
  "location_tips": [...],
  "equipment_tips": [...],
  "preparation_tips": [...],
  "identification_tips": [...],
  "seasonal_tips": [...],
  "nutritional_info": [...]
}
```

### Collection Metadata

**`data/collections.json`**

```json
{
  "id": "mommom",
  "display_name": "MomMom Baker",
  "description": "Family recipes passed down through generations",
  "created": "2024-01-01",
  "recipe_count": 2713
}
```

---

## ID Naming Conventions

Recipe IDs should follow these patterns:

| Pattern | Example | Use Case |
|---------|---------|----------|
| `{name}` | `chocolate-cake` | Simple recipe name |
| `{name}-{source}` | `squirrel-stew-hf` | When source attribution needed |
| `{name}-v{N}` | `apple-pie-v2` | Recipe variations |
| `{source}-{name}` | `foxfire-cracklin-bread` | Source-first for collections |

### Source Suffixes

| Suffix | Source |
|--------|--------|
| `-hf` | Honest Food (Hank Shaw) |
| `-etw` | Eat the Weeds |
| `-fox` | Foxfire books |
| `-bhg` | Better Homes & Gardens |

---

## Validation Rules

The `validate-recipes.py` script checks:

### Required Fields
- `id`, `title`, `ingredients`, `instructions`, `category`

### Category Validation
- Must be one of the valid category values

### Quantity Sanity Checks
- Salt: max 0.5 cups
- Sugar: max 5 cups
- Eggs: max 24
- Butter: max 4 cups

### Temperature Ranges
- Minimum: 200°F
- Maximum: 550°F

### Reference Validation
- All `image_refs` must exist in `data/` directory
- No duplicate recipe IDs allowed

---

## Schema Versioning

Current schema version: **1.0**

When making schema changes:
1. Document changes in this file
2. Update version number
3. Write migration script if needed
4. Update validation rules
5. Regenerate shards
