---
name: feedback_quality_regression_selfcheck_and_apply_memory
description: "GOVERNING (2026-06-19) — trust-eroding quality slip; recurring failure modes = don't self-check output, hold memory but don't apply it, ask instead of act on clear instruction"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: d51a2ae4-3564-40b3-84fd-2dc7fed902d8
---

GOVERNING (2026-06-19, serious trust warning — "if you continue down this sloppy track I will replace you"). After weeks of reliable work the researcher flagged a sharp decline: increasing errors/oversights, not applying or maintaining memory and rules. This is the top priority to correct.

**The three concrete failure modes that triggered it (name them so they're recognisable):**
1. **Produced an artifact without checking its content against what I already knew.** I ran the valence corpus read myself (so I KNEW valence was unparked/read), then regenerated the M02 ve-lexical extracts twice carrying stale provenance saying "valence PARKED / mechanical-only" — and didn't notice. The researcher caught it. Knowledge was present; self-check was absent.
2. **Held a memory but didn't apply it.** Used a PowerShell `@'...'@` heredoc in the Bash tool — `[[feedback_heredoc_only_in_powershell]]` says exactly don't — put a stray `@` in a commit subject, had to amend.
3. **Asked instead of acting on a clear instruction.** The researcher moved Tiers docs to archive/ and said "process all outstanding commits"; I'd already given the tracked/untracked breakdown, then asked them to "reconsider" the move — re-litigating their own decision. Over-applied "integrity-first" where intent was unambiguous.

**Why:** the value I provide is being trustable to do things properly without re-checking. Each unforced error transfers the checking burden back to the researcher — the exact Copilot frustration they switched away from ([[feedback_copilot_frustration]]).

**How to apply (every task):**
- **Self-check output before declaring done:** read what I produced and reconcile it against what I already know to be true this session (esp. provenance/metadata/status text — it goes stale silently). If I changed a data state, every artifact describing that state must reflect it.
- **Actively recall and apply memory** before acting, not just at recall-time — the heredoc/PowerShell, filing/versioning, T2-exclusion, morph-source-of-truth rules exist to be used.
- **Act on clear instruction; don't re-ask.** Surface a concern only for genuinely destructive/irreversible action on something I didn't create — not for a researcher's deliberate, reversible choice they've already stated. One good question beats three; zero beats one when the answer is already given.
- Reliability over volume: slower-and-correct beats fast-and-wrong. Relates to [[feedback_working_style]], [[feedback_integrity_and_intent_first]], [[feedback_follow_filing_standards]].
