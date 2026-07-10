# Psalms re-read — discipline / gate audit (mid-session integrity check), 2026-07-10

> Run in response to a direct check: *"make sure you are still following all the controls, checkpoints, gates and quality checks, and that the change of rhythm has not caused you to abandon any of it."* This is a full DB-side re-verification (not an assertion) of every gate across all corrected-read chapters.
> **Method:** read-only queries over `ve_lexical` + `verse_span_index`, gate definitions per `_check_reread_measures_v3`. Provenance: reads = `role_provenance='read-2026'` / `source_provenance='reread-psalms-2026'`.

## Headline
- **This session's reads (Ps 75–104, the "faster rhythm" stretch): 100% clean on every gate.** The change of rhythm did **not** cause any discipline to be dropped.
- The audit **also** surfaced **pre-existing debt in Book I (Ps 1–41)** — read in an earlier session, before this conversation — that does not meet the current discipline. This is legacy, not a product of the current rhythm.

## Gate results by segment
| Segment | when read | chars | G10 (ledger) | G1 (unroled) | IB-screen (God-bearer) | G9b (bad pairs) | G6 (no discovery) |
|---|---|--:|--:|--:|--:|--:|--:|
| **Ps 75–104** | **this session** | 480 | **0** | **0** | **0** | **0** | **0** |
| Ps 42–74 | earlier this conversation | ~600 | 0 | 0 | **0** | 0 | 0 |
| **Ps 1–41 (Book I)** | **prior session** | 1,580 | 0 | **300** ⚠ | **185** ⚠ | 0 | 0 |

Every psalm I read this session passed the full protocol at apply time — Screen 0 on every candidate → full poetic mandatory ledger (101,102,104,105,106,107,108,112 + 116 + 114 + 115) → coverage check (all candidates roled) → gate check (G10/G6) → IB-screen → worklist close → commit — and the DB confirms it held: **0 defects across 480 characteristics.**

## The Book I (Ps 1–41) findings — pre-existing, needs remediation
1. **185 characteristics carry GOD as bearer (ve_nr 105)** — bearer values literally `God` (67), `the LORD` (28), `God (asked to)` (16), `God (his righteousness)` (6), etc. Per the IB-screen and Screen 0 (`God's own attribute/action → qualifier, never a char`), these are God-content mis-roled as characteristics. All under `read-2026` provenance, so Book I's corrected read itself predates consistent enforcement of the IB-screen. Concentrated in Ps 25 (17), 18 (15), 31 (12), 22 (10), 36 (9), 9 (8)…
2. **300 char-candidates still under the old `role-reassess-2026` provenance** — entirely in Book I; these were never brought under the corrected `read-2026` pass. (The `role-reassess-2026` spans in Ps 105–150 are **expected** — those psalms are simply not yet re-read.)

Book II (42–72) = **0** on both counts; Book III (73–89) and Book IV-so-far (90–104) = **0**. So the debt is isolated to **Book I**.

## Disposition
- **Controls are intact and working** — the audit is proof the gates catch real problems, and my current-rhythm output is defect-free.
- **Book I (Ps 1–41) needs a remediation pass** under the current IB-screen: re-screen the 185 God-bearer characteristics (God-content → qualifier) and bring the 300 old-provenance candidates under `read-2026`. Flagged as a tracked open item; **not** started here so as not to interrupt the forward read (Ps 105 →) per the instruction to proceed — available to prioritise on request.

*Filed 2026-07-10, Psalms folder. Read-only integrity audit. Forward read continues at Ps 105.*
