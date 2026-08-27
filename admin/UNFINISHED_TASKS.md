# Unfinished Tasks

| library_task_id | priority | title |
|---|---|---|
| audit0827-mom-ci-missing-script | 0 | P0 AUDIT-0827: .github/workflows/rebuild-indexes.yml:27 runs python scripts/build-ingredient-index.py — the file does not exist in this repo, so every rebuild job fails at that step, and line 28's comment shows create_shards was never wired in. Mechanical cause of the 91-recipe gap (separate task). Fix the workflow: add the script (Allrecipes has one) or drop the step, and wire create_shards.py. |

<!-- library register 2026-08-27T05:05:37.552Z -->
| audit0827-mom-91-recipes-unsharded | 1 | P1 AUDIT-0827: data/recipes.json holds 2,644 recipes (2026-01-23); recipes-index.json + 36 shards hold 2,553 (2026-01-17) — 91 recipes (52 reference/BHG guides, 9 desserts, 8 main-dishes...) are in the master and in no shard, and since script.js:97 loads the index first, the fallback never fires: they appear in no list, A-Z, or search. Run scripts/create_shards.py (note: it has no CLI args despite MAINTENANCE.md:434 suggesting --dry-run) and re-verify counts. |

<!-- library register 2026-08-27T05:05:37.964Z -->
| audit0827-mom-auth-gate-wrong-name | 1 | P1 AUDIT-0827: index.html:19 renders the gate heading 'Grandma's Kitchen' on MomMom's site (copy-paste artifact), and :33-34 ship AUTH_KEY + CORRECT_ANSWER 'Baker' in plaintext client HTML. Fix the heading here; the shared-secret rotation across 4 repos is the household-wide task audit0827-xrepo-baker-secret. |

<!-- library register 2026-08-27T05:05:38.410Z -->
| audit0827-mom-ebook-wrong-collection | 2 | P2 AUDIT-0827: ebook/book.html is a copied artifact from Grandmasrecipes — title/cover 'Grandma Baker's Kitchen', 'In Loving Memory of Grandma' (:526), scan captions citing Grandmas-recipes images, 5-entry TOC for a 2,644-recipe collection. The ebook-builder skill exists and has never run here. Regenerate for MomMom (the byte-identical stale copies in the other 3 recipe repos are audit0827-xrepo-ebooks-stale). |

<!-- library register 2026-08-27T05:05:38.832Z -->
| audit0827-mom-nutrition-two-thirds | 2 | P2 AUDIT-0827: 923 of 2,644 recipes have no nutrition key (1,709 usable, 12 insufficient_data), and the nutrition-estimator skill documents --recipe-id/--force/--collection flags that scripts/estimate_nutrition.py does not implement (entire CLI is --dry-run, :1240) — three of four documented invocations silently no-op into a full-corpus run. Implement the flags and finish the corpus. |

<!-- library register 2026-08-27T05:05:39.226Z -->
| audit0827-mom-orphan-extractions | 2 | P2 AUDIT-0827: three finished extractions are read by no page code: data/tips.json (113 structured tips — the canonical preservation artifact per OVERLOOKED_TIPS_AUDIT, distinct from the reachable recipes-tips shard), data/foraging_tips.json (safety rules, ID tips, seasonal, nutritional), data/eattheweeds_recipes.json (41 recipes; only 1 id merged, 12 with no counterpart even by title — gorse-wine, kudzu-flower-wine, hawthorn-jelly, nettle-pesto...). Merge/wire them or record the decision not to. |

<!-- library register 2026-08-27T05:05:39.615Z -->
| audit0827-mom-transcription-backlog | 2 | P2 AUDIT-0827: data/processed_images.json tracks 10 incomplete, 16 partial, 5 continuation (page-2 images never joined to their recipe), 3 file_not_found — incl. damaged handwritten cards (entry 669); and ~342 page images across the three cookbook folders (FBC Jasmine 188/289, Green Chile Bible 90/152, Cooking With the Ancients 64/102) are referenced by no recipe (inferred — some are covers). Also ~510 recipes post-date the completed 2,134-recipe QA review. Finish the passes or mark them closed-incomplete. |

<!-- library register 2026-08-27T05:05:40.025Z -->
| audit0827-mom-image-optimization-unrun | 3 | P3 AUDIT-0827: data/image_manifest.json stats: total 1572, oversized 376 (over the 2000px limit in image_safeguards.py:41), processed: 0 — the optimization pass was never applied despite MAINTENANCE.md scheduling it. Run it. Also 11 near-identical processing_log_*.json (5 byte-identical) violate the 30-day prune rule. |

<!-- library register 2026-08-27T05:05:40.421Z -->
| audit0827-mom-cross-repo-stylesheet | 3 | P3 AUDIT-0827: index.html:11 and recipe.html:11 hard-code the stylesheet from https://jsschrstrcks1.github.io/Grandmasrecipes/styles.css — the local 39 KB styles.css is not what the pages load; a Grandmasrecipes change or outage restyles/breaks MomMom's site. Localize or make the dependency explicit and versioned. |

<!-- library register 2026-08-27T05:05:40.808Z -->
| audit0827-mom-stale-status-docs | 3 | P3 AUDIT-0827: SKILLS.md:3,7 claims 16 skills and that recipe-transcription/validation are 'not yet ported' — .claude/skills/ holds 35 incl. both; OVERLOOKED_TIPS_AUDIT.md:11 says RESOLVED while its own tail names a 'Primary gap' and its counts are 3 orders of magnitude stale; data/recipes-charcuterie.json uses a category absent from validate-recipes.py VALID_CATEGORIES (warn-level noise forever). Refresh/reconcile. |
