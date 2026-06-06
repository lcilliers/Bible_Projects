---
name: feedback_heredoc_only_in_powershell
description: "PowerShell @'...'@ here-strings do NOT work in the Bash tool; use the PowerShell tool for multiline git commit messages"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: eae3184c-630b-48c2-9ac1-b0b494ccf689
---

The `@'...'@` here-string is **PowerShell-only**. In the **Bash** tool it is not a here-string — `@` is a literal character — so `git commit -m @'...'@` wraps the message in stray `@` lines and the subject becomes `@`.

**Why:** On 2026-05-31 five commits were made via the Bash tool using `@'...'@`; every one got a bogus `@` subject line and had to be repaired with `git filter-branch --msg-filter`.

**How to apply:**
- For multiline git commit messages in this PowerShell-primary environment, **use the PowerShell tool** with `git commit -m @'...'@` (the closing `'@` must be at column 0).
- If committing via the **Bash** tool, do NOT use `@'...'@`. Use a normal double/single-quoted string, multiple `-m` flags (one per paragraph), or `git commit -F <file>`.
- The mandatory `Co-Authored-By: Claude Opus 4.8 (1M context) <noreply@anthropic.com>` trailer still applies.
