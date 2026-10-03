# Life and death strand: handoff for the next chat

**Date:** 2026-10-02 · **Update (2026-10-03):** **unit 3 pulled, read and ledgered** (`life-death-observation-ledger-unit3-v1-20261003.md`, LD-92 to LD-138, faces L01–L32, 690 hits / 629 verses); **awaiting researcher approval (#1940)**, with four decisions in its §F. Next after approval: weave → records → session-close. Unit 4 continues from **LD-139**. · **Update (later 2026-10-02):** unit 2 pulled, read and ledgered (`life-death-observation-ledger-unit2-v1-20261002.md`, LD-43 to LD-91); **approved and woven 2026-10-03 (#1939)**. **Next: unit 3, living before God** (H2416A / H2416E / G2198 / G2222 / H0748). Unit 3 continues from **LD-92**; unit 2 used faces D01–D28. Current versions: Ch 2 v8 · 10.1 v10 · 10.3 v4 · 10.4 v5 · 10.5 v11 · 10.6 v6 · 10.7 v8 · 10.9 v12 · 10.10 v10 · 10.11 v2 · 11 v11 · 12 v10 · 13 v7 · 14 v11 · claim register v10. New reusable pull script: `strand-unit-pull-v1-20261002.py OUT.csv <strongs…>` (then `--faces`). · **State before that:** unit 1 woven (#1934). Ch 9 moved to Ch 2 (#1936) and Ch 2 rewritten as the scene-setting chapter (#1937). · **Next:** unit 2, dying and death.

## ★ Next chat starts here (written 2026-10-03, end of session)

**Where it stopped:** unit 3 (living before God) has finished steps 1–4 of the rhythm (register check, pull, read by surface, ledger). It is committed (`1b29d24d`). **Step 5, researcher approval, is open as #1940.** Nothing from unit 3 is woven yet. No chapter, claim register, index, linkage map or open-threads row has changed for unit 3.

**First action:** read `life-death-observation-ledger-unit3-v1-20261003.md` §F and get the researcher's answer on #1940. The four decisions:
1. NS **"Living before God"** in Ch 2, after "Life set before a person" (oaths LD-92–96, the living God LD-97–100, the days lived LD-103, LD-118, the land of the living LD-119). The alternative is to put the oaths only in 10.5 and 10.9.
2. **"Life weighed"** (LD-111, 112, 114–116): a new Ch 2 section before "Facing death" (recommended), or folded into "Wanting to die" and "Where life flows from".
3. **LD-101 and LD-102 side by side** in "Life set before", unreconciled, or hold LD-102 in the register.
4. **LD-138**: a supplement reading the H2416C "life" hits (Job 33:18–28; Isa 57:10; Psa 74:19 H2416D), recommended, or leave them. If approved, faces and observations continue from LD-139, and unit 4 shifts on.

**Then (steps 6–8):**
- Weave per §F. Version-bump every chapter touched and archive the prior version: Ch 2 v8 → v9, and the 10.x, 11, 12, 13 and 14 files named in §F.
- Update the claim register (v10 → v11), `00-index-and-status`, `life-death-linkage-map.md` (add unit 3 rows; mark M02 / H0748 "read", LD-134) and `../open-threads-register.md` (rows from §F "Register at approval"; LD-106 goes to **OT-01**).
- Add "Woven — where" to the unit 3 ledger.
- Run the quote check (`--prose`) on every chapter changed.
- Then `/session-close`.

**Unfinished edges to keep in view:**
- Joh 7:38's "heart" is *koilia* (G2836). Do not cite it as a heart verse anywhere.
- Unit 3 data: the pull CSV and faces CSV, plus `life-death-unit3-face-assign-v1-20261003.py` (re-runnable).
- After unit 3: unit 4, H5782 "roused and stirred". **The researcher has still to confirm that it belongs in this strand** (candidate v2 §5). The focused pulls for Q2 (soul and spirit with death) and Q3 (heart with death or Sheol) are still owed. Then fear units 3–4 (#1933).
- **Not committed, deliberately:** `.github/workflows/publish-learning4comfort-content.yml` and `publishing/learning4comfort/SOURCE-SETUP.md` (a Learning4Comfort publishing sync, made outside this session). They are left for the researcher to decide. A workflow file is persistent repo configuration.

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
