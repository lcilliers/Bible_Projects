# STEP extraction bug — multi-code words collapsed to one sub-code (v1, 2026-07-13)

> Found while closing Proverbs I2 (Stage 2). The STEP verse extract is **faulty for any Strong's that STEP splits into multiple lettered codes**: `step_client._resolved_strong` returns only `vocabInfos[0]`, so the sibling codes (and all their verses) are silently dropped. This is **not** the 60-cap truncation (that is fixed via `_paginate_all`, which self-validates). Read-only diagnosis; **no code changed yet** — the fix has a correctness fork that is the researcher's call.

## Evidence (H7307 *ruach*)

- `_resolved_strong('H7307')` → **`H7307G`** (`vocabInfos[0]`). `get_verse_records` then pulls only H7307G.
- STEP actually tags *ruach* under **three** codes: `H7307G` total **194** + `H7307H` **137** + `H7307I` **7** = **338** (≈ the ~359 you counted; base `H7307` = 0). All three are the **same lemma** *ru.ach*: glosses `spirit` / `spirit: breath` / `spirit: side`.
- Result: the extract kept 194, **dropped 144** verses — including Proverbs. Union of G+H+I covers **16 of the 19** master Proverbs *ruach* spans (the other 3 — Pro 14:29, 17:27, 29:11 — STEP does not tag under any code = genuine STEP gaps).
- Same pattern behind the other Stage-2 "term-present-no-record" gaps (H3001, H6424): the master (morphology, source of truth) attests the strong at the verse; STEP's pulled subset omits it.

## The correctness fork (why I did not just "union all siblings")

STEP's lettered siblings are **two different things** and share the same transliteration, so translit cannot tell them apart:
- **Grammatical / sub-sense variants of ONE word** → should be **unioned**. *ruach*: `H7307G/H/I` = spirit / spirit:breath / spirit:side.
- **Distinct homonyms** → must **NOT** be unioned. *chalats*: `H2502A` = "to rescue" vs `H2502B` = "to arm" (we deliberately picked A in Stage 1).

The **gloss head** (text before `:`) discriminates these two cases here: ruach → all "spirit" (same head → union); chalats → "to rescue" vs "to arm" (different heads → keep split). But that is a **heuristic**; a wrong call silently corrupts an extraction, and this method feeds **all** term onboarding programme-wide — hence the researcher decision.

## Fix options

- **(A) Gloss-head union** *(recommended)* — `_resolved_strong` returns all sibling codes whose **gloss head matches** the primary's; `get_verse_records` unions `_paginate_all` across them, dedup by osisId. Verified on both test cases: ruach → 338 (16 Proverbs); H2502A/B stay separate. Pragmatic, testable, big recovery.
- **(B) Union all siblings** — simplest, but **merges homonyms** (H2502 rescue+arm) → wrong. Rejected.
- **(C) Per-span coverage from the master** — build a verse-record using the **master span's own STEP code** (the morphology already disambiguated the sense per verse), instead of resolving from the registry term. Most correct, but changes the onboarding flow (per-span, not per-term). Bigger change.
- Residual **genuine STEP gaps** (e.g. 3/19 for ruach) remain under any option — a separate small decision (accept as I2 exception, or build from the master).

## Impact if fixed (option A)

Re-extract the affected terms → `audit_word` builds the recovered records → **Proverbs I2 drops toward the genuine-gap floor**. Also improves every future book's onboarding (any multi-code word was under-pulling).

## Recommendation

Implement **(A)** now (I can, with the ruach/H2502 tests as guardrails), then re-run Stage 2. Flag **(C)** as the more-correct long-term model and the residual genuine-gaps as a small follow-up. **Your call on the union rule** (A vs C) before I change the core extractor.

*Filed 2026-07-13. Read-only diagnosis. No engine code changed. Blocks Proverbs I2-closure via `audit_word` until the extractor is fixed.*
