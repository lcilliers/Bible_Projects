# Life and death strand: handoff for the next chat

**Date:** 2026-10-02 · **Update (2026-10-04, later):** **unit 4 approved and woven (#1949)**; next is the rework #1940–#1948. · **Update (2026-10-04):** **unit 3 approved and woven (#1940)**; unit 4 (H5782) pulled and read; next is the unit 4 ledger from **LD-143**. · **Update (2026-10-03):** **unit 3 pulled, read and ledgered** (`life-death-observation-ledger-unit3-v1-20261003.md`, LD-92 to LD-138, faces L01–L32, 690 hits / 629 verses); **awaiting researcher approval (#1940)**, with four decisions in its §F. Next after approval: weave → records → session-close. Unit 4 continues from **LD-139**. · **Update (later 2026-10-02):** unit 2 pulled, read and ledgered (`life-death-observation-ledger-unit2-v1-20261002.md`, LD-43 to LD-91); **approved and woven 2026-10-03 (#1939)**. **Next: unit 3, living before God** (H2416A / H2416E / G2198 / G2222 / H0748). Unit 3 continues from **LD-92**; unit 2 used faces D01–D28. Current versions: Ch 2 v8 · 10.1 v10 · 10.3 v4 · 10.4 v5 · 10.5 v11 · 10.6 v6 · 10.7 v8 · 10.9 v12 · 10.10 v10 · 10.11 v2 · 11 v11 · 12 v10 · 13 v7 · 14 v11 · claim register v10. New reusable pull script: `strand-unit-pull-v1-20261002.py OUT.csv <strongs…>` (then `--faces`). · **State before that:** unit 1 woven (#1934). Ch 9 moved to Ch 2 (#1936) and Ch 2 rewritten as the scene-setting chapter (#1937). · **Next:** unit 2, dying and death.

## ★ Next chat starts here (written 2026-10-04, after unit 4)

**Where it stopped:** M25 units 3 and 4 are **approved and woven**.
- Unit 3 (#1940) is woven and waits for the researcher's approval in the escalation tool.
- Unit 4 (#1949) is approved and woven: the new Ch 2 section "Sleep and waking", and the H6974 supplement §H (LD-150 to LD-155).
- Current versions: Ch 2 v10 · 10.9 v14 · 11 v13 · 12 v12 · 13 v9 · claim register v12. The other versions are as after unit 3.

**Sequencing (researcher, verbatim, 2026-10-04):** *"I personally think we must first complete unit 3 and 4 of M25 as you have already done the preparatory work. and then go back to 1940-1948 to do the rework; else we will stop M25 verse analysis in the middle."*

**Next: the rework, #1940–#1948.** Ask the researcher where to start. The items:
- **#1941** publishing alignment (waits on the researcher)
- **#1942** H5782 as several strands. Inputs: unit 4 ledger §E, LD-149, LD-155
- **#1943** weaving method from now on (applied first in the unit 4 ledger)
- **#1944–#1947** Ch 10 revisit: missing meaning; emerging findings and impacts; chains of operation; fitting verses into a fixed list
- **#1948** Ch 2 revisit of units 2–3 for meaning

**Q2 and Q3 done (#1950, 2026-10-04):** ledger `life-death-q2-q3-soul-spirit-heart-ledger-v1-20261004.md`. Woven: Ch 2 v11 "Soul, spirit and heart at death" (reworked from "The inner person dying"); "Delivered from death" restated by count; "After death" widened; Ch 4 v10. OT-04 resolved (no verse on the heart after death). Claim register v13. #1950 waits for the researcher's approval in the tool. **M25's units and Q1–Q4 are now all read.** Held for Ch 13 at the rework: LD-154. After the rework: fear units 3–4 (#1933).

**Unfinished edges:**
- Joh 7:38's "heart" is *koilia* (G2836). Do not cite it as a heart verse.
- **Not committed, deliberately:** `.github/` and `publishing/` (#1941).

### Previous stop (2026-10-03)

Unit 3 had been pulled, read and ledgered, awaiting #1940 with four decisions in §F. All four were approved as recommended on 2026-10-04.

## Working rhythm

Each unit runs in this order:
1. **register check**
2. pull
3. read by surface
4. ledger
5. researcher approval
6. weave
7. records (claim register, index, **linkage map**, register)
8. session-close (commit + push)

Then a new chat starts the next unit.

## Read first, in this order

1. `../open-threads-register.md`: match unit 2's Strong's numbers against "comes back when". OT-02 (Q1 What is death?) and OT-08 (the frame) apply. Q2 and Q3 may be touched.
2. `life-death-strand-candidate-v2-20261002.md`: §5 for the units, §7 for the researcher's questions.
3. `life-death-observation-ledger-unit1-v1-20261002.md`: the format to copy, faces A–X, LD-01 to LD-42, and "Woven — where". Unit 2 continues from **LD-43**. Faces may be reused or new.
4. `life-death-linkage-map.md`: add unit 2 rows; part B shows which cluster links are still "not yet read".
5. `../../essay/spirit_soul_body/inner-being-narrative/02-life-breath-and-death-v6-20261002.md`: unit 2 mainly fills the section "What death is" and the movement around it.
6. `Workflow/Instructions/wa-inner-being-narrative-style-guide-v2-20261001.md`.

## Data and method (do not re-derive)

- **Overview:** `strand-overview-v1-20261002.py <code> <slug>` (reusable for any cluster). Its outputs for M25 are in this folder.
- **Unit pull pattern:** `life-death-unit1-life-revived-breath-pull-v1-20261002.csv`. One row per hit, with the full ESV text and a face. Build it from iba.db, not from the web pull.
- **Quote check:** `../fear/fear-quote-check-v1-20261001.py <file> [--prose]`.
- **Language (researcher):** never "umbrella". Use the verses' own phrases (Ch 2 proposal §2).

## Unit 2 scope

- **H4191** (to die, 840), **H4194** (death, 156), **G0599** (to die, 110), **G2288** (death, 120), **G3499** (put to death, 3), **G1312** (decay, 6), **G4881**, **G2253**
- **H4191 is large and mostly narrative or legal** ("he died", "put to death"). Read it by surface. Narrative and legal hits are accounted for as data. Focus on the inner-being verses: death and sin, fear of death, wanting to die, the heart that dies, death as an enemy, death swallowed up.
- **Expected verses** (pointers only, to be confirmed by the pull): Rom 5:12; 6:23; 1Cor 15:26, 54–56; Heb 2:14–15; 1Jo 3:14; Pro 14:12; Pro 18:21 ("Death and life are in the power of the tongue").

## Later units (from candidate v2 §5)

- **Unit 3:** living before God. H2416A / H2416E / G2198 / G2222 / H0748: "as the LORD lives"; long life; "slow to anger" (H0748, the anger link); eternal life.
- **Unit 4:** roused and stirred (H5782). Researcher to confirm whether it belongs in this strand.
- **Focused pulls for Q2–Q4** (OT-03 to OT-05): soul and spirit with death; heart with death or Sheol; body and resurrection, the glorified body.

## After the life-death strand (#1933)

1. Fear units 3 and 4, first.
2. Then M12 and M64 as candidate strands.
3. OT-09, the pass for gold nuggets, at a point the researcher chooses.

## Current versions after unit 1

- **Chapters:** 01 v4 · 02 v6 · 03 v2 · 04 v8 · 05 v2 · 06 v5 · 07 v5 · 08 v4 · 09 v2 · 10.0 v5 · 10.1 v8 · 10.2 v8 · 10.3 v3 · 10.4 v4 · 10.5 v10 · 10.6 v4 · 10.7 v7 · 10.8 v5 · 10.9 v11 · 10.10 v9 · 10.11 v1 · 11 v10 · 12 v9 · 13 v5 · 14 v9 · 15 v7
- **Claim register:** v8 (4-8 and 8-4 verdict changes proposed, for the researcher to confirm)
- **Escalations awaiting the researcher's close:** #1934, #1936, #1937
