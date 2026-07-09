# Reading the re-read measures — interpretation guidance, evaluation limits, and cross-book baselines (2026-07-09)

> Guidance for reading the gate results **and the processes behind them**, the honest limits of what the evaluation can surface, and baselines run across three books (Proverbs, Psalms, Isaiah) to prove which gaps are **systemic** vs **book-specific**. Companion to the success-criteria + baseline docs. Runner: `scripts/_check_reread_measures_v3_20260709.py --book <name>` (read-only, unit-model-aware).

## 1. What the measures are — and are not
Each gate is a **query that counts violations**. In the tables: **"failing now"** = the count of items still to correct; **"pass at"** = 0 (the goal); **status ❌** iff failing-now > 0. A column of 0s under "pass at" is the *target*, never a statement that the data is empty (Proverbs holds 24,260 lexical rows; Psalms 76,321). The gates measure **presence, grounding-state, structure, and completeness — not correctness.**

## 2. Two families of gate (the split that matters)
- **Quality of what EXISTS** — G3 (grounding), G4 (no flattening), G7 (no silent blanks), G9(b) (well-formed pairs). These inspect only rows that are *there*; passing means *what was recorded is not wrong*. They **cannot see a missing dimension.**
- **Completeness of what SHOULD exist** — G1 (undecided), G2 (no operation), G6 (no discovery), G10 (missing mandatory dimensions). These flag what is *absent*.
- **Structural precondition** — G0 (unit digestibility).
> So "G3/G4/G7 pass" means **the sound core that exists is sound** — a *narrow* statement. It does **not** mean the characteristic was fully worked. And **G9(a)/(c) are unverified, not passed** (see §5).

## 3. Obstacle vs cause (the process behind the numbers)
- **Unit over-size (G0) and undecided spans (G1) are OBSTACLES** — a 35-verse / 129-char-span unit forces selective, shallow reading. Fixing them *enables* a thorough read.
- **The completeness gaps (G2/G6/G10) and integrity defects (§5) are caused by the old METHOD**, not the unit layout: the mechanical pass never read source/effect, never ran the discovery-lookout, never wrote explicit `none`, and encoded pairs by Strong's.
- **Therefore fixing G0/G1 is necessary but NOT sufficient.** It removes the obstacle; the **new reading method** (read source & effect, complete operation, run discovery, write `none`, encode pairs as span-ids) is what closes the completeness/integrity gates. This is a genuine re-read that *reuses the sound core*, not "good data that just needs its passages fixed."

## 4. The self-challenge — will evaluation surface ALL issues? **No.**
The gates surface **structural / completeness / integrity** gaps. They **cannot** surface **correctness or judgment** issues:
| a gate CANNOT tell you… | only caught by… |
|---|---|
| is a recorded value actually *right* (operation, sense)? | scored read-back audit |
| is the *role* correct (char vs qualifier vs standalone)? | audit |
| is a `none` a true absence or a **missed** pair/qualifier? | audit (the real test of "all pairs identified") |
| did the seed **miss** a characteristic (wrongly standalone)? | discovery-lookout + audit |
| is a pair's direction/kind/sense right? | audit |
| is a meaning **imported** (eisegesis) vs grounded? | audit |
| is the cross-verse **movement** correct? | audit |
**Consequence: the scored read-back audit is not optional garnish — it is the ONLY route to correctness. Gates + audit together; neither alone suffices.**

The multi-book run also exposed **meta-gaps in the evaluation itself** (now fixed in v3): the gates had to become **unit-model-aware** (Psalms uses passages, not segments — a segment-only gate would falsely pass it), and **G0 is genre-inappropriate for poetic whole-chapter reading** (Psalms 150 "over budget" is largely by design — needs a poetic threshold or N/A).

## 5. Systemic integrity defects (surfaced identically in ALL three books)
- **source (103) and effect (111) have ZERO rows in every book** — never read by the old method. Not a coverage gap; a method gap.
- **Pair endpoints are Strong's-encoded** (`H0693@Pro 1:11`), not span-ids — **violates the "key on span id, never strong" rule**, and makes G5/G9(a)/G9(c) unmeasurable until the re-read writes span-ids. Corpus-wide, not Proverbs-specific.

## 6. Cross-book baseline (2026-07-09) — systemic vs book-specific
| gate (failing now) | Proverbs (seg) | Psalms (passage) | Isaiah (seg) | reading |
|---|--:|--:|--:|---|
| G0 units over budget | 36 | 150† | 71 | over-size everywhere (†poetic caveat) |
| G1 undecided spans | 40 | **0** | **157** | book-specific — Psalms fully decided, Isaiah a big tail |
| G2 chars no operation | 1,139 | 1,847 | 1,054 | **systemic** — ~½ of chars unworked everywhere |
| G3 grounding | 0 ✅ | 0 ✅ | 0 ✅ | pass (what exists is grounded) |
| G4 flattening | 0 ✅ | **4** | 0 ✅ | mostly pass; minor Psalms signal |
| G5 belonging | N/A | N/A | N/A | **systemic** — Strong's encoding blocks it |
| G6 no discovery | 438 | 976 | 298 | **systemic** — lookout never run |
| G7 silent blanks | 0 ✅ | 0 ✅ | 0 ✅ | pass |
| G9(b) malformed | 0 ✅ | 0 ✅ | 0 ✅ | pass; (a)/(c) N/A (encoding) |
| G10 chars missing a mandatory dim | 1,708 (all) | 3,810 (all) | 2,296 (all) | **systemic** — no ledger, no `none` |
| G10 dims with ZERO rows | 103,111 | 103,111 | 103,111 | **systemic** — source & effect never read |

**Headline: even the best-covered book (Psalms — a deliberate span-level re-read) fails every completeness/integrity gate the same way.** So the gaps are **method-level, not coverage-level** — which means **one corrective method applies to every book**, not per-book bespoke fixes (the reassurance this exercise was run to obtain).
Book-specific residues to note: Isaiah's **157 undecided** (G1) and missing **locus** (only run on the 5 wisdom books); Psalms' **4** flattened terms (G4) and the **poetic G0** interpretation.

## 7. Implications for the corrective (re-read) action
1. **Universal method requirements** (every book): read **source & effect** (first time), **complete operation**, **run the discovery-lookout** on every verse, **write explicit `none`** (the ledger), **encode pairs as span-ids**.
2. **Genre-aware G0**: set a poetic/whole-chapter threshold (or mark G0 N/A for poetic) so Psalms isn't falsely failed.
3. **Clear the undecided tails** (Isaiah 157, Proverbs 40) as part of G1.
4. **Audit is mandatory** — gates certify structure/completeness; only the scored read-back certifies correctness.
5. **Corrective action is validated as reusable** — because the gaps are systemic, the same re-read method + gate suite drives every book; the baseline-then-delta proves improvement per book.

*Filed 2026-07-09. Read-only. Baselines: Proverbs/Psalms/Isaiah via v3. This doc is the lens for reading every future gate run.*
