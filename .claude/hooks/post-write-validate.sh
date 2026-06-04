#!/bin/bash
# Post-Write Validation Hook for MomMom Baker's Recipe Archive
# Automatically validates recipes after any edit

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_DIR="$(dirname "$(dirname "$SCRIPT_DIR")")"

FILE_PATH="${CLAUDE_FILE_PATH:-}"

if [[ "$FILE_PATH" == *"recipes"* && "$FILE_PATH" == *".json"* ]]; then
    cd "$PROJECT_DIR"
    python scripts/validate-recipes.py 2>&1 | grep -E "(ERROR|FAIL|Invalid)" || true
fi
