---
name: feedback_heredoc_only_in_powershell
description: "Bash mangles quoting: PowerShell @'...'@ here-strings don't work, and backticks in double-quoted strings get command-substituted — silently corrupting written content"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: eae3184c-630b-48c2-9ac1-b0b494ccf689
---

Two ways the **Bash tool** silently mangles text. Both have caused real damage.

## 1. `@'...'@` here-strings are PowerShell-only

In Bash, `@` is a literal character — `git commit -m @'...'@` wraps the message in stray `@` lines and the subject becomes `@`.

**Why:** 2026-05-31, five commits made via Bash with `@'...'@`; every one got a bogus `@` subject and needed `git filter-branch --msg-filter` to repair.

## 2. ★ Backticks inside double-quoted Bash strings are COMMAND-SUBSTITUTED

`python -c "...text with \`some_word\`..."` → Bash runs `some_word` as a command, it fails, and **the empty output is substituted in**. The word vanishes. The script still exits 0 and the file is written — **corrupted, silently**.

**Why:** 2026-07-15, this happened **three times in one session** while authoring the IBA configurator. It emptied `enum.decision_status`'s value descriptions (leaving `"Not yet ruled.  is null."`) and gutted four numbered findings in a report. The config kernel **PASSED** the corrupted enum — a mangled string is still a non-empty string, so the description check saw content that was not there. Only a manual spot-check caught it.

**The trap:** the failure is invisible at every layer. Exit code 0. Valid JSON. Non-empty strings. It looks like it worked.

## How to apply

- **Prose containing backticks → use the Write or Edit tool, never Bash.** Those tools don't parse anything. This is the root fix; the rest are workarounds.
- Markdown and JSON destined for this project are *full* of backticks (rule ids, filenames, `[current]` tokens), so this is the normal case, not an edge case.
- If a script must run via Bash, **write it to a file with Write first**, then `python path/to/script.py`. Never `python -c "..."` with backticked content.
- For multiline git commit messages: use the **PowerShell tool** with `@'...'@` (closing `'@` at column 0), or `git commit -F <file>`. Via Bash, `<<'EOF'` (quoted delimiter) is safe — but **unquoted** `<<EOF` still substitutes.
- The mandatory `Co-Authored-By: Claude Opus 4.8 (1M context) <noreply@anthropic.com>` trailer still applies.
