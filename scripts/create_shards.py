#!/usr/bin/env python3
"""
Create category-based recipe shards for better performance.

This splits the monolithic recipes.json into:
- recipes-index.json: Minimal metadata for all recipes (for browsing/search)
- recipes-{category}.json: Full recipe data per category (loaded on-demand)
"""

import json
import os
import re


def sanitize_category(cat):
    """Sanitize category name for use in filenames (replace spaces with hyphens)."""
    return re.sub(r'\s+', '-', cat.strip().lower())


def create_shards():
    # Load existing recipes
    with open('data/recipes.json', 'r') as f:
        data = json.load(f)

    recipes = data['recipes']
    meta = data['meta']

    # Group by category (with sanitization check)
    by_category = {}
    problematic_categories = []
    for r in recipes:
        cat = r.get('category', 'uncategorized')
        sanitized = sanitize_category(cat)

        # Warn if category needs sanitization
        if cat != sanitized and cat not in [p[0] for p in problematic_categories]:
            problematic_categories.append((cat, sanitized))

        # Use sanitized category for grouping
        if sanitized not in by_category:
            by_category[sanitized] = []
        by_category[sanitized].append(r)

    # Report problematic categories
    if problematic_categories:
        print("⚠ WARNING: Found categories with spaces/inconsistent casing:")
        for orig, fixed in problematic_categories:
            print(f"  '{orig}' -> '{fixed}'")
        print("  Consider normalizing these in recipes.json\n")

    # Create index with minimal metadata for browsing/search
    index_recipes = []
    for r in recipes:
        index_recipes.append({
            'id': r.get('id'),
            'title': r.get('title'),
            'category': sanitize_category(r.get('category', 'uncategorized')),  # Sanitized for shard lookup
            'tags': r.get('tags', []),
            'collection': r.get('collection'),
            'description': (r.get('description', '') or '')[:100],
            'servings_yield': r.get('servings_yield', ''),
            'total_time': r.get('total_time', '') or r.get('cook_time', ''),
            # Include attribution for search
            'attribution': r.get('attribution', ''),
            # Include variant info for filtering
            'variant_of': r.get('variant_of'),
            'canonical_id': r.get('canonical_id'),
        })

    # Build shard manifest (categories are already sanitized)
    shards = [
        {
            'category': cat,  # Already sanitized
            'file': f'recipes-{cat}.json',
            'count': len(recs)
        }
        for cat, recs in sorted(by_category.items())
    ]

    # Write index
    index_data = {
        'meta': {
            **meta,
            'sharded': True,
            'shard_strategy': 'by_category',
            'shard_count': len(shards)
        },
        'shards': shards,
        'recipes': index_recipes
    }

    with open('data/recipes-index.json', 'w') as f:
        json.dump(index_data, f, indent=2)

    print(f"Created recipes-index.json with {len(index_recipes)} recipe summaries")

    # Write category shards
    for cat, cat_recipes in by_category.items():
        shard_data = {
            'meta': {
                'category': cat,
                'count': len(cat_recipes),
                'parent_collection': 'mommom'
            },
            'recipes': cat_recipes
        }

        filename = f'data/recipes-{cat}.json'
        with open(filename, 'w') as f:
            json.dump(shard_data, f, indent=2)

        print(f"Created {filename} with {len(cat_recipes)} recipes")

    print(f"\n✓ Created {len(shards)} shards from {len(recipes)} recipes")
    print(f"✓ Index file: data/recipes-index.json")
    print(f"✓ Shard files: data/recipes-{{category}}.json")
    print(f"\nFallback: Keep data/recipes.json for backward compatibility")

if __name__ == '__main__':
    os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    create_shards()
