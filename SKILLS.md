# Skills — MomsRecipes

> MomMom's kitchen at scale — 2,700+ recipes, 37+ ingestion scripts, PDF pipeline. The 16-skill standard household kit covers operations; recipe-domain skills are referenced from CLAUDE.md but not yet packaged under `.claude/skills/`.

This document is the human-facing index of all Claude Code skills configured in this repository. The agent-facing pointer lives in [`CLAUDE.md`](CLAUDE.md). Skills follow the agent-skills-spec format and live under `.claude/skills/`.

**Total skills configured: 16** (the standard household kit). Recipe-transcription and recipe-validation are in `Allrecipes`, `Grandmasrecipes`, and `Grannysrecipes` but not yet ported here — the equivalent logic runs through `scripts/validate-recipes.py` and the 37+ `add_*.py` ingestion scripts.

---

## Quick reference

| Skill | Activation | Default | Domain |
|---|---|---|---|
| Standard household kit (16 skills) | mixed | on | See [section below](#standard-household-kit) |

**Domain logic lives in scripts**, not skills (yet):

| Script | Purpose | When it runs |
|---|---|---|
| `scripts/validate-recipes.py` | Schema, slug uniqueness, image refs, category vocab | Before commit |
| `scripts/process_images.py` | Resize iPhone photos (4032×3024) to ≤2000 px | Before AI reads source images |
| `scripts/image_safeguards.py` | Manifest + size detection | Pre-flight check before reading any image |
| `scripts/pdf_safeguards.py` | PDF size + text extraction | Before reading any PDF (100 pages / 50 MB API limit) |
| `scripts/optimize_images.py` | JPEG optimization | Before commit if images are large |
| `scripts/create_shards.py` | Regenerate per-category shards | After bulk recipe additions |
| `scripts/add_*.py` (37+) | One ingestion script per source batch | When adding a new cookbook batch |

---

## How invocation works

Claude Code skills can fire three ways:

**1. Automatic activation** via YAML `keywords:` and surrounding context.

**2. Explicit invocation:**

```
"Use the verification-before-completion skill before claiming the migration is done."
/skill verification-before-completion
```

**3. Implicit invocation by task shape** — bulk edits trigger careful behavior, completion claims trigger verification, etc.

---

## Recipe-domain logic (not yet skills)

The non-negotiable rules that the recipe-domain skills enforce in sister repos are also enforced here — just through scripts and CLAUDE.md prose rather than packaged skills. They include:

- Never invent ingredients, steps, temperatures, times, or yields
- Mark unreadable text `[UNCLEAR]`
- Preserve original intent; normalize only spelling and formatting
- Keep family names and attributions verbatim
- Never discard `image_refs`, even on merged duplicates
- **Every recipe must have `"collection": "mommom"`**
- Never read images >2000 px directly — use `data/processed/`
- Never load a PDF >100 pages or >50 MB without `pdf_safeguards.py` first

When these rules need to be more explicitly enforceable, port `recipe-transcription` and `recipe-validation` from Allrecipes/Grandmasrecipes/Grannysrecipes into `.claude/skills/` here.

---

## Recipe sources

| Source | Batches | Recipes | Notes |
|---|---|---|---|
| MomMom's Cards | — | ~800 | Original family recipes |
| Eat the Weeds | 1–12 | ~157 | Wild edibles, foraging |
| Honest Food | 1–5 | ~45 | Wild game, unusual meats |
| Foxfire Books | Multiple | ~35 | Appalachian heritage |
| BHG Cookbooks | 1 | Various | Better Homes & Gardens |

Foraging tips live separately in `data/foraging_tips.json` because misidentifying a wild plant has different stakes than mistyping a sugar measurement.

---

## Standard household kit

Common to every sister repo. Canonical versions live in `ken/.claude/skills/`.

| Skill | Activation | One-line |
|---|---|---|
| `brainstorming` | automatic on creative work | Pre-implementation creative exploration. |
| `cognitive-memory` | automatic on session start | Cross-session knowledge persistence. Memory scope: `/MomsRecipes`. |
| `executing-plans` | explicit | Use when executing a written plan. |
| `finishing-a-development-branch` | explicit | Decide merge / PR / cleanup. |
| `prompt-optimizer` | automatic on prompt-improvement requests | Optimizes raw prompts. Advisory only. |
| `receiving-code-review` | explicit | Use when receiving review feedback. |
| `requesting-code-review` | explicit | Use when completing tasks before merging. |
| `safety-guard` | automatic on destructive ops | Prevents destructive operations. |
| `security-review` | automatic on auth/secrets/payment | Security checklist + patterns. |
| `security-scan` | explicit | Scans `.claude/` config. |
| `session-checkpoint` | automatic + explicit | Atomic commits, checkpoint summaries, rate-limit recovery. |
| `subagent-driven-development` | explicit | Implementation plans with independent tasks. |
| `systematic-debugging` | automatic on bug/test-failure | Use before proposing fixes. |
| `using-git-worktrees` | explicit | Isolate feature work. |
| `verification-before-completion` | automatic on completion claims | Refuses "complete/fixed/passing" without observed output. |
| `writing-plans` | explicit | Use when you have a spec for a multi-step task. |

---

## Multi-LLM orchestrator

This repo defaults to **`recipe` mode** in the orchestrator hosted in [ken](https://github.com/jsschrstrcks1/ken). Lead model: GPT.

| Slash command | Usage |
|---|---|
| `/consult` | `/consult gpt structure "review this Foxfire pp 99-108 transcription"` |
| `/orchestrate recipe "<task>"` | Full pipeline: transcribe → validate → integrate |

First-time setup per session:

```bash
pip3 install -q -r /home/user/ken/orchestrator/requirements.txt
```

---

## See also

- [`CLAUDE.md`](CLAUDE.md) — agent context
- [`README.md`](README.md) — public-facing overview
- [`DATA_SCHEMA.md`](DATA_SCHEMA.md) — canonical recipe schema
- [`MAINTENANCE.md`](MAINTENANCE.md) — routine maintenance procedures
- [`SCRIPTS.md`](SCRIPTS.md) — every script with usage examples
- [`TROUBLESHOOTING.md`](TROUBLESHOOTING.md) — common errors and fixes
- [`OVERLOOKED_TIPS_AUDIT.md`](OVERLOOKED_TIPS_AUDIT.md) — audit of small notes that originally lived only in family memory
- [`.claude/standards/`](.claude/standards/) — OCR_STANDARDS, IMAGE_WORKFLOW, PDF_WORKFLOW, RECIPE_SCHEMA, SESSION_MANAGEMENT
- `ken` — hosts the orchestrator; canonical versions of the standard household kit
