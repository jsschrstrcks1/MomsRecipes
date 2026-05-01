# Claude Code Session Management — MomMom's Kitchen

## Resuming previous sessions

From the command line:

```bash
# Resume most recent session
claude --continue

# Resume a specific named session
claude --resume recipe-ocr-batch

# Browse all sessions interactively
claude --resume
```

Inside an active session:

```
/resume          # Open session picker
/rename task-name  # Name the current session
```

## Session Picker Shortcuts

| Key | Action |
|---|---|
| `↑` `↓` | Navigate sessions |
| `Enter` | Select session |
| `P` | Preview session content |
| `R` | Rename session |
| `/` | Search sessions |
| `Esc` | Exit picker |

## Best Practices

1. **Name by task** — `/rename ocr-batch-42`, `/rename foxfire-extraction`.
2. **Be descriptive** — include the image range or PDF being processed.
3. **Continue quickly** — `claude --continue` when returning to finish a task.
4. **Preview before resuming** — press `P` in the picker.

## Cleaning Up

```
/delete          # Delete current or selected session
```

From the picker, navigate and delete to keep your list manageable.
