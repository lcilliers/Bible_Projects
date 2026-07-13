# Proverbs re-read — Stage-1 onboarding worklist (registry path) v1, 2026-07-12

> **Stage 1** of the staged sequence (`wa-book-lexical-readiness-assessment-AUTHORITATIVE-v1` §2.2): register every candidate characteristic's word as a term, **existing-registry-first**. This worklist covers the **30 base-Strong's** that are candidates in Proverbs but absent from `mti_terms` (= 71 of the 104 I2-uncovered candidate spans; the other 33 have a registered term but no verse-record → Stage 2). Read-only planning doc; no DB writes yet. Tool: `_run_gate1_onboard_batch_v1` (word_study_extract → curate terms array → audit_word → verse_context). Selection rule applied: **associate with an existing registry** (23 from the seed tag, 5 my pick); **new registry only where none fits** (1 case: healing).

## A. Terms with an existing-registry association (28)

Registry taken from the seed `char_candidate_tag` (23) or my existing-registry pick (5, marked *pick*).

| strong | surface(s) | spans | → registry (id) | source |
|---|---|--:|---|---|
| H0159 | love | 1 | love (103) | tag |
| H0404 | urges | 1 | desire (43) | tag |
| H0936 | belittles/despise | 8 | contempt (190) | tag |
| H1566 | quarreling | 3 | strife (152) | tag |
| H2054 | guilty | 1 | guilt (73) | tag |
| H2134 | pure | 3 | purity (125) | tag |
| H2502 | delivered | 2 | salvation (220) | tag |
| H2904 | cast | 1 | rejection (131) | tag |
| H3093 | haughty | 1 | pride (123) | tag |
| H3832 | ruin | 2 | corruption (31) | tag |
| H3994 | curse | 2 | cursing (219) | tag |
| H4072 | ruin | 1 | corruption (31) | tag |
| H4079 | discord/quarreling | 10 | strife (152) | tag |
| H4090 | discord/strife | 2 | strife (152) | tag |
| H4426 | saying | 1 | contempt (190) | tag |
| H4860 | deception | 1 | deceit (40) | tag |
| H5889 | thirsty | 1 | weakness (170) | tag |
| H6337 | fine gold | 1 | purity (125) | tag |
| H6895 | curse/cursed | 2 | cursing (219) | tag |
| H7189 | right/truth | 1 | worship (176) | tag |
| H7390 | soft/tender | 3 | compassion (23) | tag |
| H7456 | hungry | 3 | appetite (8) | tag |
| H7703 | destroys/violence | 3 | corruption (31) | tag |
| H3944 | scoffing | 1 | contempt (190) | *pick* (scorner ≈ contempt) |
| H4878 | turning away | 1 | rebellion (128) | *pick* (backsliding) |
| H5916 | troubles/hurts | 4 | strife (152) | *pick* (akar = stir up trouble) |
| H8367 | ceases | 1 | peace (117) | *pick* (quieting of strife) |
| H3856 | madman | 1 | despair (44) | *pick, SOFT* — H3856 languish/rage; despair is nearest existing (flag for review) |

## B. Healing — folded into an existing registry (researcher direction 2026-07-12)

Healing is **not substantive enough for a new registry** → folded into the **best-fit existing registry: `peace` (117)** (*marpe* = healing/**soundness**/health; shalom = wholeness/welfare/soundness — the nearest existing sense; "a sound heart is life to the body").

| strong | surface(s) | spans | → registry (id) | source |
|---|---|--:|---|---|
| H4832 marpe | healing/health | 8 | peace (117) | *fold (best-fit)* |
| H7500 riphuth | healing | 1 | peace (117) | *fold (best-fit)* |

**All 30 terms now map to an existing registry. No new registry created.**

## C. Execution plan (Stage 1 → 2 → 3)

1. **Stage 1 — onboard the 28 existing-registry terms** (§A) via `_run_gate1_onboard_batch_v1` extended with this worklist: `word_study_extract --anchors <strong>` → auto-curate terms array → `audit_word --add-terms` (inserts `mti_terms`, verse-records, span-links) → `verse_context`. **Dry-curate first** (`--dry-curate`, no writes) to confirm STEP resolution per strong; then live in one batch; snapshot the DB first.
2. **Healing (§B)** — on your nod: create the `healing` registry, then onboard H4832/H7500 the same way. (Held pending confirmation.)
3. **Stage 2 — the 33 term-present-no-record spans** — these have a registered term but no `wa_verse_records`; build the records (same engine path, `audit_word` for the owning registry pulls the verses). Re-run readiness I2 → expect 0.
4. **Stage 3 — v2 candidate-driven passages** — write/extend the v2 passage builder (v1 is misaligned), build Proverbs passages, fix I4 (Pro 22:27 +). Re-run readiness → expect READY.
5. Then **Stage 4** the lexical read (with `_reread_ledger_lib` made D2-conformant).

## D. Status — cleared to execute

All 30 terms map to an existing registry (healing folded → peace, researcher direction). **No open decisions.** Stage 1 is a mechanical existing-registry onboard: dry-curate (STEP resolution check) → snapshot → live batch → re-check I2. (The one soft pick, H3856 "madman" → despair, is noted for later read-time review; it does not block onboarding.)

*Filed 2026-07-12. Read-only plan. No DB writes performed. Stage-1 of the Proverbs registry-path rework.*
