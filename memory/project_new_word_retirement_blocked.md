---
name: project_new_word_retirement_blocked
description: FINDING (2026-06-15) - new_word/gap_fill superseded for AUDITING but audit_word still DEPENDS on them for wa_file_index creation; cannot be cleanly archived until that handoff moves
metadata: 
  node_type: memory
  type: project
  originSessionId: 8a5e10ea-2d9d-4bb9-8ca3-fb979500309e
---

FINDING (2026-06-15): the decision to retire `new_word.py` (and `gap_fill.py`) and use `audit_word` for both new + existing words is **only partly true in the code**, so they are **NOT yet safe to archive**.

- `audit_word.py` header says it "Supersedes new_word.py and gap_fill.py (retained for reference only)", and CLAUDE.md §4 claims they're superseded. `audit_word` DOES handle the audit + re-sync + a "first-time population" path (A2).
- **BUT `audit_word` does NOT create `wa_file_index`** — it REQUIRES it (A1, audit_word.py:1638 stops with "Run --mode=new_word first" if absent). The only things that INSERT `wa_file_index` are `new_word.py:370`, `gap_fill.py:596`, and `scripts/_repair_03_wa_file_index.py`. So a brand-NEW word (no file_index) still needs new_word/gap_fill to onboard. Removing them breaks new-word onboarding.
- `--mode=new_word` is also **still wired** in `engine/engine.py` (import :54, choices :83, invocation :310-323).
- This matches the researcher's note that "new_word was not updated with many underlying routines/rules" — it's stale/divergent (no H4 link+morph at insert, etc.), so it should NOT be used for analysis, but it is still load-bearing for file_index creation.

**Proper retirement = complete the handoff FIRST:** move `wa_file_index` creation into `audit_word`'s first-time-population path (A2) or into `--register`, validate a brand-new word end-to-end through audit_word, THEN remove the CLI wiring + archive new_word + gap_fill and update the stale "Run --mode=new_word first" messages (audit_word.py:1638, 1698) and CLAUDE.md §4.

**H4 validated 2026-06-15** on a live audit of R211 'being': 497 verses inserted 0 errors, link-at-insert worked (511/572 linked), the H5 integrity check (A12) caught the residual 61 orphans of a dead term, which were then cleaned. See [[project_morph_is_source_of_truth]].
