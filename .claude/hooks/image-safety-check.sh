#!/bin/bash
# Image Safety Check Hook for MomMom Baker's Recipe Archive
# Warns before reading potentially oversized images

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_DIR="$(dirname "$(dirname "$SCRIPT_DIR")")"

FILE_PATH="${CLAUDE_FILE_PATH:-$1}"

if [[ "$FILE_PATH" == *.jpeg ]] || [[ "$FILE_PATH" == *.jpg ]] || [[ "$FILE_PATH" == *.png ]]; then
    if [[ "$FILE_PATH" == *"/processed/"* ]]; then
        exit 0
    fi
    if [[ "$FILE_PATH" == *"/data/"* ]]; then
        BASENAME=$(basename "$FILE_PATH")
        PROCESSED_PATH="$PROJECT_DIR/data/processed/$BASENAME"
        if [[ -f "$PROCESSED_PATH" ]]; then
            echo "WARNING: Use processed version instead: data/processed/$BASENAME (original may exceed 2000px limit)"
        else
            echo "WARNING: Image may exceed 2000px limit. Run: python scripts/process_images.py"
        fi
    fi
fi
exit 0
