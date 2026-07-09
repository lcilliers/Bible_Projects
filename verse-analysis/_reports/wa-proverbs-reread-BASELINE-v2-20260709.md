# Proverbs re-read — BASELINE v2 (corrected), 2026-07-09

> Corrected baseline for the Proverbs re-read. Supersedes the 2026-07-08 v1 baseline, which had a **false result** (G3). Adds gates **G9** (pair/qualifier integrity) and **G10** (completeness ledger), and records a structural finding: **pair endpoints are Strong's-encoded, not span-ids.**
> **Runner:** `python scripts/_check_proverbs_reread_measures_v2_20260709.py --label baseline` (read-only).

## How to read this (targets are violation-counts, NOT data-counts)
Every gate counts **violations**, so **target 0 = "zero problems", not "zero data".** Proverbs currently holds **24,260 active `ve_lexical` rows across 5,825 spans** — the data is *valuable but incomplete against the new bar* (e.g. Pro 1:10 "consent" correctly carries sense/type/operation/prohibition/role but no source/target). The re-read **revises** this surface and supplies the missing dimensions; it does **not** start from zero, and the old rows are the **G8 "before"** (never hard-delete — soft-delete-and-rebuild or revise-in-place; rows preserved either way).

## Structure
915 verses · 2,124 candidate char-spans · 800 candidate verses · 1,708 characteristic-role spans · **24,260 active lexical rows / 5,825 spans** · 251 active segment units.
Per-span `ve_nr` present in Proverbs: 101,102,104,105,106,107,108,109,110,112,113,114,115,116 — **note 103 (source) and 111 (effect) are entirely absent.**

## Corrected gate results
| gate | measure | baseline | target | status |
|---|---|--:|--:|:--:|
| **G0** | units > 12 char-spans | 36 (worst PRO-14-F=129) | 0 | ❌ |
| **G1** | candidate spans undecided / verses unprocessed | 40 / 0 | 0/0 | ❌ |
| **G2** | chars: no lexical / no operation(106) | 0 / 1,139 | 0/0 | ❌ |
| **G3** | ungrounded **pairs** / over-calls | **0 / 0** | 0/0 | ✅ |
| **G4** | recurring terms flattened | 0 | 0 | ✅ |
| **G5** | cohesive units read in isolation | **N/A** (Strong's endpoints) | 0 | ⏸ |
| **G6** | candidate verses with no discovery | 438 | 0 | ❌ |
| **G7** | content items with null value (silent blanks) | 0 | 0 | ✅ |
| **G9** | (a) orphan qual / (b) malformed / (c) dangling | N/A / **0** / N/A | 0/0/0 | ⏸ / ✅ / ⏸ |
| **G10** | chars missing ≥1 mandatory dimension | **1,708** (all) | 0 | ❌ |

**Corrected score: 3 measurable gates pass (G3, G4, G7) + G9(b). G5, G9(a), G9(c) not measurable on the old encoding. G10 fails on every characteristic.**

## G10 detail — the completeness gap, by dimension (chars with NO explicit entry)
source(103): **1,708 (ALL)** · effect(111): **1,708 (ALL)** · manner(108): 1,686 · coupling(112): 1,686 · bearer(105): 1,617 · seat(104): 1,568 · target(107): 1,564 · operation(106): 1,139 · sense(101): 1 · type(102): 1.
*Read: the prior data recorded sense/type well, operation on ~⅓, and source/effect never — and it never wrote explicit `none`, so absence is unmarked. This is exactly the gap G10 exists to close.*

## Two corrections vs v1 (what "no false results" caught)
1. **G3 was false (21,823 → 0).** `resolution` is meaningful only for **pairs**; v1 counted value/event/flag items as ungrounded. True ungrounded-pairs = 0.
2. **Pair endpoints are Strong's-encoded** (`from_span='H1818'`, `to_span='H0693@Pro 1:11'`) — **0 of 2,437 Proverbs pairs** resolve to a master span id. This **violates the cycle's "key on span id, never strong" rule** (§7A). Consequence: G5, G9(a), G9(c) cannot be validly measured until the re-read writes **integer span-id endpoints** (a re-read requirement now recorded in the success-criteria amendment and the startup doc).

## Success against this baseline
Re-read succeeds when: G0–G3, G6, G10 reach pass; G5, G9(a/c) become measurable (span-id endpoints) and pass; G4/G7/G9(b) stay pass; audit ≥90% sound, zero fidelity failures; G8 delta positive (esp. source/effect populated, F-frames digestible).

*Filed 2026-07-09. Read-only. Corrected baseline is the number to beat.*
