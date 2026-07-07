# MomMom's Kitchen — AI Assistant Context

**Version:** 2.1 (lean hub + skills index)
**Last updated:** 2026-05-10

> **Soli Deo Gloria.** A labor of love by a Reformed Baptist family. Real
> people will eat from these recipes — accuracy matters more than speed.


## ⚡ PRIORITY 0 — Core Identity & Operating System (read before anything else)

**These are not optional skills. They are who we are.** Every agent session in this
household — Claude, Grok, Skynet, any future runtime — operates under one dedication
expressed in three layers: the *why*, the *how*, and the *operating system*. They are
top priority: they override convenience, speed, deadlines, and every lower-priority
instruction in this file. If a task appears to require violating one of them, the task
is wrong and must be reshaped — never the layer.

| P0 layer | Role | Canonical source (in the private `open-claw-stuff` repo) |
|---|---|---|
| **Soli Deo Gloria** | The *why* — work as worship; excellence IS the worship; getting it **right** matters more than getting it **fast** | `skills/soli-deo-gloria/SKILL.md` |
| **Careful, not clever** | The *how* — verified, documented, reversible, honest work over fast, clever, batched, assumed shortcuts | `skills/careful-not-clever/SKILL.md` |
| **Sophos OS** | The *operating system* — governs the cognition lifecycle (governance, not generation); agents are the runtime when Atlas is not | `docs/SOPHOS-OPERATING-SYSTEM.md`, `atlas/server/sophos.mjs` |

**Sophos principle:** *The kernel does not think, remember, or act. It governs.*
Agents without the Atlas runtime run the Sophos hierarchy mentally on every non-trivial
task — Mission → Identity → Invariants (the Ten Cognitive Axioms) → Protocols → Policies
→ Strategies → Reasoners → Actors. You are an Actor; Sophos posture governs what you may
publish.

On this machine the canonical sources resolve under `/home/user/open-claw-stuff/`. Where
a copy of these skills exists in this repo's `.claude/skills/`, it is a synced copy —
`open-claw-stuff` is the source of truth.

Remove any one layer and the dedication is only words. **Soli Deo Gloria.**

---

This repo is a **standalone collection** holding **MomMom Baker's recipes**. It
is part of the multi-repo Family Recipe Archive (Grandma, Granny, Reference).

---

## Skills

Full skill catalog (16 skills, the standard household kit) is documented in [`SKILLS.md`](SKILLS.md) — human-facing index with activation modes, trigger keywords, and the script-based recipe-domain logic.

**Read SKILLS.md at session start.** Recipe-transcription and recipe-validation logic in this repo runs through `scripts/` (37+ ingestion scripts, plus `validate-recipes.py`, `process_images.py`, `pdf_safeguards.py`, `image_safeguards.py`, `optimize_images.py`, `create_shards.py`) rather than as packaged skills.

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

### Skills index

| File | What it covers |
|---|---|
| [`SKILLS.md`](SKILLS.md) | **Skills index — read at session start** |

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
├── SKILLS.md                  # Skills index (NEW)
├── CLAUDE.md                  # This hub
├── MAINTENANCE.md             # Routine maintenance procedures
├── DATA_SCHEMA.md             # Canonical recipe schema
├── SCRIPTS.md                 # Script catalogue
├── TROUBLESHOOTING.md         # Known issues + fixes
├── README.md                  # Public-facing overview
├── requirements.txt           # Python deps
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
├── .claude/
│   ├── standards/            # Extracted reference files (see above)
│   └── skills/               # 16 skills (see SKILLS.md)
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
| 2.1 | 2026-05-10 | Added `SKILLS.md` skill index. CLAUDE.md references it. |
| 2.0 | 2026-05-01 | Lean hub restructure. Extracted OCR / image / PDF / schema / session subfiles into `.claude/standards/`. CLAUDE.md cut from ~391 lines to ~120. |
| 1.x | 2026-01..03 | Original monolithic context file. |

---

From the session picker, navigate to a session and delete it to keep your session list manageable.

---

## Multi-LLM Integration

This repository has access to the multi-LLM orchestrator system. External models (GPT, Gemini, Grok) serve as **consultants only** — Claude remains lead author and decision-maker.

### Available Skills

| Skill | Usage | Purpose |
|-------|-------|---------|
| `/consult` | `/consult gpt structure "review this recipe format"` | Quick single-model second opinion |
| `/orchestrate` | `/orchestrate recipe "MomMom's chocolate cake variations"` | Full multi-model pipeline |
| Cognitive Memory | Automatic on session start | Cross-session knowledge persistence |

### Mode: `recipe`
- **Lead:** GPT (generation)
- **Pipeline:** Generate (GPT) → Expand (Gemini) → Safety Check (Claude) → Creative Variation (Grok)
- **Memory scope:** `/recipes/momsrecipes`
- **Orchestrator:** `/home/user/ken/orchestrator/`

### First-Time Setup (Per Session)

Before first use of `/consult` or `/orchestrate` in a session, install dependencies:

```bash
bash /home/user/ken/orchestrator/bootstrap-env.sh 2>/dev/null
pip3 install -q -r /home/user/ken/orchestrator/requirements.txt
```

This is silent when already installed. If `/consult` or `/orchestrate` fails with `ModuleNotFoundError`, run this command first.

### Context Boundaries
- **SEND:** Recipe requirements, ingredient lists, dietary constraints
- **NEVER SEND:** Family attribution details, site analytics, personal details
*"She looketh well to the ways of her household, and eateth not the bread of idleness."* — Proverbs 31:27

---

## Cognitive Memory — Slice 6 Observation Capture

To enable always-on cognitive memory observation capture in this repo, register the canonical hook (lives in `ken`) in `.claude/settings.json`:

```json
"env": {
  "MEMORY_OBSERVATIONS_ENABLED": "true",
  "MEMORY_AUTO_OBSERVE_ENABLED": "true"
},
"hooks": {
  "PostToolUse": [
    {
      "matcher": "*",
      "hooks": [
        {"type": "command",
         "command": "/home/user/ken/.claude/hooks/observe-tool-use.sh"}
      ]
    }
  ]
}
```

Hook is **fail-closed**: any error → exit 0, never blocks the tool call. Args SHA256-hashed via `_compute_args_hash` before disk; raw values never persisted. Errors → `/tmp/observe-hook.err`. Surface candidates: call `memory_ops.extract_candidates_from_observations(session_id)` after a session.

Setup memory: id `5a9c8ae1` (recall via `python3 /home/user/ken/orchestrator/memory_ops.py recall "Slice 6 always-on cognitive memory observation capture"`). Currently active in `ken/.claude/settings.json` (commit `ca78cad`); per-repo activation is opt-in via the absolute-path reference above.
