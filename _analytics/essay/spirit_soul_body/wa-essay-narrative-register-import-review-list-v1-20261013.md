# Narrative claim register: import review list (v1-20261013)

Goes with `wa-essay-narrative-register-import-preview-v1-20261013.md` / `.json`. Escalation #2110, spec §6 *Review and import*: the correlation lists, changes found only by comparison, chapter numbers mapped across the 2026-10-02 renumbering, references that could not be resolved, and the Tally recount. **Each item is for your review; the import takes the preview as it stands unless you direct otherwise.**

## 1. How the import maps the register

- **Claim wording.** An original claim's `claim_text` is its *Evidence and restatement* cell when the verdict is Restated (the correction is what the narrative now says), and its original wording for every other verdict. The original wording is kept in `original_wording`; the full cells of each version stay in the 'claim created' and change rows. The R0 reading may restate a claim in its own plain wording; that is then a logged change.
- **Status.** Withdrawn → `withdrawn`; Held → `held`; every other verdict → `current`. A split verdict (Restated / Held) is `current`, with the second verdict in `part_verdict`.
- **in_narrative** is 0 for every claim at import: no passage is linked until the R0 batches read the chapters. `Check` will list current claims with no telling until then.
- **Main chapter** is the first chapter named in *New ch* (already in the 2026-10-02 numbering in v51).
- **Sources:** every verse reference in the original claim and in the evidence cell (one row per verse), and the M47 reading pointers (dep, A–H, SC) as one *study file* row.
- **Register lines that do not name an original claim** (the narrative's own statements a strand changed, and the 88 audit edits) cannot be attached to a claim yet: the claims they concern are found in R0. They are imported with their update and kept in the preview JSON for the correlation; nothing is dropped.

## 2. Tally recount

The register's Tally gives 15 + 8 + 37 + 15 + 11 = 86, counting part-held claims twice. The import finds **81 claim rows**: Withdrawn 14, Restated 36, Held 10, Widened 7, Stands 14. By status: withdrawn 14, current 57, held 10.

## 3. R2 accounted for

53 dated sections; 502 table lines (392 data rows, the rest headers and separators); 14 header shapes. Every data row is in the preview: 13 name an original claim (attached), the rest are narrative changes held for R0.

The 13 lines that name an original claim (the *# · Before (verdict) · Evidence now read · Now* tables) are carried by R1: the register version that added the section is the version in which the claim's cells changed, so the change row holds the cells before and after, and the section's full text (tables included) is kept verbatim in the update's notes.

**Spec §1 facts, re-measured.** The specification gave 551 table lines in 16 header shapes for the dated sections; the sections hold 502 table lines in 14 shapes (the 7 lines of the Tally are not in a dated section). It gave 33 chapter files and 323 headings: both counts included the index (00-index), so there are 32 chapter files with 315 headings, and 347 section rows with each chapter's opening.

## 4. Items found while building the preview

- 4-8: split verdict 'Withdrawn (model) / Held (word)' -- imported as verdict Withdrawn, part_verdict Held, status withdrawn
- 9-1: split verdict 'Restated (location) / Held (catalogue)' -- imported as verdict Restated, part_verdict Held, status current
- 9-5: split verdict 'Restated (verse) / Held (model)' -- imported as verdict Restated, part_verdict Held, status current
- index row '10' (Part 10 — The inner being at work) has no chapter file; imported as a chapter row with no file (state draft)
- index row 'science' ((science)) has no chapter file; imported as a chapter row with no file (state deferred)
- old Ch 13 *Under God's anger* (folded into 10.13, #1977; the number reused for *Other beings*, #1982) is added as a retired chapter row (inactive 1), so history can point to it
- Ch 02 v17 (2026-10-12): 2 register sections share its date and refs -- kept as its own update
- Ch 02 v15 (2026-10-09): 12 register sections share its date and refs -- kept as its own update
- Ch 03 v3 (2026-10-09): 12 register sections share its date and refs -- kept as its own update
- Ch 04 v14 (2026-10-09): 12 register sections share its date and refs -- kept as its own update
- Ch 04 v12 (2026-10-08): 5 register sections share its date and refs -- kept as its own update
- Ch 04 v11 (2026-10-05): 2 register sections share its date and refs -- kept as its own update
- Ch 05 v3 (2026-10-05): 2 register sections share its date and refs -- kept as its own update
- Ch 10.6 v8 (2026-10-08): 7 register sections share its date and refs -- kept as its own update
- Ch 10.10 v15 (2026-10-09): 12 register sections share its date and refs -- kept as its own update
- Ch 10.12 v2 (2026-10-08): 5 register sections share its date and refs -- kept as its own update
- Ch 11 v30 (2026-10-12): 2 register sections share its date and refs -- kept as its own update
- Correction section: its 34 removals are listed as prose (by chapter, 12 bullets), with no before/after; R4 (the archive comparison, with each chapter's R0 batch) supplies them

## 5. References with no verse row (citations)

Kept with `verse_id` NULL, never dropped. Whole-chapter references (e.g. *Psalm 23*) are among them.

- 1Cor 4:23 (verse) ×1
- 1Pe 10 (whole chapter) ×1
- 1Sa 10 (whole chapter) ×1
- 1Sa 17:19 (verse) ×1
- Act 10 (whole chapter) ×1
- Act 5 (whole chapter) ×1
- Col 13 (whole chapter) ×1
- Dan 10 (whole chapter) ×1
- Deu 10 (whole chapter) ×2
- Deu 12 (whole chapter) ×1
- Ecc 10 (whole chapter) ×2
- Ecc 15:28 (verse) ×1
- Eph 13 (whole chapter) ×1
- Exo 10 (whole chapter) ×2
- Exo 20 (whole chapter) ×1
- Eze 10 (whole chapter) ×2
- Eze 37 (whole chapter) ×1
- Gen 10 (whole chapter) ×2
- Gen 15:45 (verse) ×1
- Gen 15:49 (verse) ×1
- Hag 13 (whole chapter) ×1
- Hos 13 (whole chapter) ×1
- Isa 1 (whole chapter) ×2
- Isa 10 (whole chapter) ×2
- Isa 12:14 (verse) ×1
- Isa 12:15 (verse) ×1
- Isa 12:16 (verse) ×1
- Isa 12:17 (verse) ×1
- Isa 12:19 (verse) ×1
- Isa 12:20 (verse) ×1
- Isa 15:55 (verse) ×1
- Isa 30 (whole chapter) ×1
- Isa 65 (whole chapter) ×1
- Jer 10 (whole chapter) ×1
- Jer 18 (whole chapter) ×1
- Job 10 (whole chapter) ×2
- Job 13 (whole chapter) ×1
- Joh 10 (whole chapter) ×2
- Joh 6 (whole chapter) ×1
- Jos 10 (whole chapter) ×1
- Judg 16 (whole chapter) ×1
- Lev 26 (whole chapter) ×1
- Luk 13 (whole chapter) ×1
- Mar 13 (whole chapter) ×1
- Mat 10 (whole chapter) ×3
- Num 10 (whole chapter) ×2
- Phili 10 (whole chapter) ×1
- Pro 10 (whole chapter) ×3
- Pro 3 (whole chapter) ×1
- Pro 31 (whole chapter) ×1
- Psa 10 (whole chapter) ×8
- Psa 106 (whole chapter) ×1
- Psa 116:9 (verse) ×1
- Psa 119 (whole chapter) ×3
- Psa 13 (whole chapter) ×1
- Psa 135 (whole chapter) ×1
- Psa 143 (whole chapter) ×1
- Psa 16 (whole chapter) ×1
- Psa 2 (whole chapter) ×1
- Psa 25 (whole chapter) ×1
- Psa 30 (whole chapter) ×1
- Psa 37 (whole chapter) ×2
- Psa 3:21 (verse) ×1
- Psa 40 (whole chapter) ×1
- Psa 44 (whole chapter) ×1
- Psa 49 (whole chapter) ×1
- Psa 4:28 (verse) ×1
- Psa 4:29 (verse) ×1
- Psa 73 (whole chapter) ×1
- Psa 76 (whole chapter) ×1
- Psa 88 (whole chapter) ×1
- Song 10 (whole chapter) ×1
- Tit 10 (whole chapter) ×1
- Zec 13 (whole chapter) ×1

## 6. Index version notes linked to updates (R3)

| Ch | v | Date | Note | Update |
|---|---|---|---|---|
| 01 | 3 | 2026-10-01 | anger strand — roadmap | R3:2026-10-01:0 |
| 01 | 4 | 2026-10-02 | roadmap for the new order, #1936 | R3:2026-10-02:1 |
| 02 | 18 | 2026-10-13 | Psa 89:46–47, M02 pairing gaps, OT-29/30/51 | R2:Strand updates — anger (M02) pairings with strands alread |
| 02 | 17 | 2026-10-12 | Psa 49:14, 16, M72 group B, #1998 | R3:2026-10-12:2 |
| 02 | 16 | 2026-10-09 | 2Ch 21:20; Job 36:20; Job 7:2, M18 group A, #1993 | R2:Strand updates — desire (M18), group A: desire, craving,  |
| 02 | 15 | 2026-10-09 | Hezekiah's plea; "see good" (Psa 34:12, Job 7:7); Exo 14:12; Pro 8:35–36. OT-08 closed, #1993 | R3:2026-10-09:3 |
| 02 | 14 | 2026-10-08 | Job 7:13-16; Jer 8:2, #1992 | R2:Strand updates — the 18 include verses (2026-10-08, #1992 |
| 02 | 13 | 2026-10-08 | Jer 8:3 "preferred" is the choosing word; Rev 9:6 kept apart, #1991 | R2:Strand updates — citations to check (2026-10-08, #1991) |
| 02 | 12 | 2026-10-08 | 2Sa 14:14 set in Joab's staged plea, 14:3, #1990 | R2:Strand updates — citations needing attention (2026-10-08, |
| 02 | 11 | 2026-10-04 | **life-death Q2 and Q3**: "The inner person dying" reworked into "Soul, spirit and heart at death"; "Delivered from death" restated by count | R2:Strand updates — life and death (M25), Q2 and Q3: soul, s |
| 02 | 10 | 2026-10-04 | **life-death unit 4, roused and stirred**: new section "Sleep and waking" before "Life weighed" (death as sleep moved into it), #1949 | R2:Strand updates — life and death (M25), unit 4: roused and |
| 02 | 9 | 2026-10-04 | **life-death unit 3, living before God**: new sections "Living before God" (after "Life set before a person") and "Life weighed" (before "Fa | R2:Strand updates — life and death (M25), unit 3: living bef |
| 02 | 8 | 2026-10-03 | **life-death unit 2, dying and death**: "What death is" widened (Death and sin; Death in the living), new "Facing death" and "Dying to the L | R2:Strand updates — life and death (M25), unit 2: dying and  |
| 02 | 7 | 2026-10-02 | **"The body raised" expanded**, Q4 body and resurrection, #1938 | R2:Strand updates — life and death (M25), Q4: the body and t |
| 02 | 6 | 2026-10-02 | **rewritten as the scene-setting chapter**, life-death unit 1, #1937; **was Ch 9**; moved to Ch 2, #1936; anger, fear strands | R2:Strand updates — life and death (M25), unit 1 and the Ch  |
| 03 | 3 | 2026-10-09 | "not far from the kingdom" (Mar 12:34), #1993; was Ch 2, renumbered 2026-10-02, #1936 | R3:2026-10-09:4 |
| 04 | 15 | 2026-10-12 | the heart watching power (Ecc 8:9); the boast (Dan 4:30); Act 8:21–22; Judg 9:3; Jer 30:21, M72 group B, #1998 | R3:2026-10-12:2 |
| 04 | 14 | 2026-10-09 | the heart awake (Song 5:2–6); the heart hot (Psa 39:1–4); teaching that speaks on waking (Pro 6:21–22); Hos 7:7, #1993 | R3:2026-10-09:5 |
| 04 | 13 | 2026-10-09 | Pro 21:1 a heart directed, not a state; Mat 5:28, #1993 | R3:2026-10-09:5 |
| 04 | 12 | 2026-10-08 | the heart named beside the will, #1986 | R3:2026-10-08:6 |
| 04 | 11 | 2026-10-05 | anger and the heart, M47 step, #1974 ("The heart and anger") | R3:2026-10-05:7 |
| 04 | 10 | 2026-10-04 | life-death Q3, the heart and death, #1950 | R2:Strand updates — life and death (M25), Q2 and Q3: soul, s |
| 04 | 9 | 2026-10-04 | life-death unit 3, living before God, #1940 | R2:Strand updates — life and death (M25), unit 3: living bef |
| 04 | 8 | 2026-10-02 | life-death unit 1; was Ch 3, renumbered 2026-10-02, #1936; v4, v5: fear strand | R3:2026-10-02:1 |
| 04 | 6 | 2026-10-02 | M20 pointer to 10.11 | R3:2026-10-02:8 |
| 05 | 6 | 2026-10-13 | Pro 20:2 pointer corrected to 10.13, M02 pairing gaps, OT-29/30/51 | R2:Strand updates — anger (M02) pairings with strands alread |
| 05 | 5 | 2026-10-12 | Psa 103:22, M72 group B, #1998 | R3:2026-10-12:2 |
| 05 | 4 | 2026-10-09 | M18 × M47 read-back: "exhaustion" restated, each death-wish with its own ground; a life precious; the ransom; the want before God, #1993 | R3:2026-10-09:5 |
| 05 | 3 | 2026-10-05 | anger and the soul, M47 step, #1974; was Ch 4, renumbered 2026-10-02, #1936 | R3:2026-10-05:9 |
| 06 | 12 | 2026-10-09 | the stirred spirit, toward building and destroying (Haggai 1), #1942 | R2:Strand updates — desire (M18) × life and death (M25), and |
| 06 | 11 | 2026-10-09 | 1Sa 16:16, 23; the Spirit instructs, leads and carries (Neh 9:20; Psa 143:10; 2Pe 1:21), #1993 | R3:2026-10-09:5 |
| 06 | 10 | 2026-10-08 | Psa 51:12, the willing spirit has no possessive, #1991 | R2:Strand updates — citations to check (2026-10-08, #1991) |
| 06 | 9 | 2026-10-08 | Psa 32:2 restated, the forgiven man who confessed, 32:1, 5, #1990 | R2:Strand updates — citations needing attention (2026-10-08, |
| 06 | 8 | 2026-10-08 | hardened and willing spirit, #1986 | R3:2026-10-08:6 |
| 06 | 7 | 2026-10-05 | anger and the spirit, M47 step, #1974 (held back, heated, pressed, embittered; the Spirit with anger; grieved) | R3:2026-10-05:7 |
| 06 | 6 | 2026-10-04 | life-death unit 3, living before God, #1940 | R2:Strand updates — life and death (M25), unit 3: living bef |
| 06 | 5 | 2026-10-02 | life-death unit 1; was Ch 5, renumbered 2026-10-02, #1936; anger, fear strands | R3:2026-10-02:1 |
| 07 | 8 | 2026-10-12 | kin used to win rule; Eph 6:12; Jude 8–10, M72 group B, #1998 | R3:2026-10-12:2 |
| 07 | 7 | 2026-10-09 | what is done with the desires of the flesh; flesh as an outward mark, #1993 | R3:2026-10-09:5 |
| 07 | 6 | 2026-10-05 | Ecc 11:10, M47 step, #1974; was Ch 6, renumbered 2026-10-02, #1936; anger, fear strands | R3:2026-10-05:9 |
| 08 | 7 | 2026-10-12 | 1Co 8:9; Rom 13:1 beside 13:5, M72 group B, #1998 | R3:2026-10-12:2 |
| 08 | 6 | 2026-10-09 | Heb 13:18, #1993 | R3:2026-10-09:5 |
| 08 | 5 | 2026-10-05 | conscience beside the wrath, Rom 13:5, M47 step, #1974; was Ch 7, renumbered 2026-10-02, #1936; anger strand | R3:2026-10-05:9 |
| 10.1 | 20 | 2026-10-12 | joy turned (Luk 10:17–21), M72 group B, #1998 | R3:2026-10-12:2 |
| 10.1 | 19 | 2026-10-11 | delight beside meditating, under pressure, joined to doing; Psa 16:3; measure table +12, M18 group B remaining 94 by role, #1993 | R2:Strand updates — desire (M18), group B: the 94 remaining  |
| 10.1 | 18 | 2026-10-09 | *Delight* corrected: table *When delight is only the measure*, M18 group B correction by main operation, #1993 | R2:Strand updates — desire (M18), group B sets 1 and 2 corre |
| 10.1 | 17 | 2026-10-09 | *Delight*: **new** *What is found pleasant*; willing because it could not be borne (1Th 3:1), M18 group B set 2, #1993 | R3:2026-10-09:5 |
| 10.1 | 16 | 2026-10-09 | **new** *Delight* (a person’s delight; the 10.6 section moved in), M18 group B set 1, #1993 | R2:Strand updates — desire (M18), group B set 1: the delight |
| 10.1 | 15 | 2026-10-09 | Pro 6:34–35 "tender/hard" restated as a reading, #1993 | R3:2026-10-09:5 |
| 10.1 | 14 | 2026-10-09 | Ecc 7:2; Pro 15:15, #1993 | R3:2026-10-09:5 |
| 10.1 | 13 | 2026-10-08 | "It divides" restated as "Many things against one", Luk 10:40-42, #1991 | R2:Strand updates — citations to check (2026-10-08, #1991) |
| 10.1 | 12 | 2026-10-08 | a feeling holds the will, #1986 | R3:2026-10-08:6 |
| 10.1 | 11 | 2026-10-04 | life-death unit 3, living before God, #1940 | R2:Strand updates — life and death (M25), unit 3: living bef |
| 10.1 | 10 | 2026-10-03 | life-death unit 2, dying and death, #1939 (fear of death, grief at a death, vexation that kills) | R2:Strand updates — life and death (M25), unit 2: dying and  |
| 10.1 | 9 | 2026-10-02 | Q4 pointer, the groan that waits, #1938 | R2:Strand updates — life and death (M25), Q4: the body and t |
| 10.1 | 8 | 2026-10-02 | chapter pointers, #1936 | R3:2026-10-02:1 |
| 10.1 | 3 | 2026-10-01 | anger strand — **rewritten**; v4, v5: fear strand | R3:2026-10-01:10 |
| 10.1 | 6 | 2026-10-01 | fear account integrated for review, #1930 | R2:Fear account integrated for review (2026-10-01, #1930) |
| 10.1 | 7 | 2026-10-02 | M20 — Anxiety, Losing heart, #1931 | R2:Strand updates — doubt and discouragement (M20) (2026-10- |
| 10.2 | 17 | 2026-10-12 | Jer 44:16–18, M18 × M72, #1993 item H | R2:Strand updates — desire (M18) × authority (M72): the 51 n |
| 10.2 | 16 | 2026-10-12 | willing to receive a word; 2Pe 3:5, M18 group C (will) by role, #1993 | R2:Strand updates — desire (M18), group C: will, willing, ac |
| 10.2 | 15 | 2026-10-09 | ears that cannot listen (Jer 6:10–11), M18 group B correction by main operation, #1993 | R2:Strand updates — desire (M18), group B sets 1 and 2 corre |
| 10.2 | 14 | 2026-10-09 | hearing stopped at one word (Act 22:18–22); goads and nails (Ecc 12:10–12), #1993 | R3:2026-10-09:5 |
| 10.2 | 13 | 2026-10-09 | the word rare in Samuel's days (1Sa 3:1–9), #1993 | R3:2026-10-09:5 |
| 10.2 | 12 | 2026-10-09 | a famine of hearing (Amo 8:11–13), #1993 | R3:2026-10-09:5 |
| 10.2 | 11 | 2026-10-09 | Pro 17:4, #1993 | R3:2026-10-09:5 |
| 10.2 | 10 | 2026-10-09 | the woken ear (Isa 50:4–6; Zec 4:1–2); knowing in heart and soul (Jos 23:14–15), #1993, #1942 | R2:Strand updates — desire (M18) × life and death (M25), and |
| 10.2 | 9 | 2026-10-04 | life-death unit 3, living before God, #1940 | R2:Strand updates — life and death (M25), unit 3: living bef |
| 10.2 | 8 | 2026-10-02 | life-death unit 1 | R3:2026-10-02:11 |
| 10.2 | 7 | 2026-10-02 | chapter pointer, #1936; anger, fear strands | R3:2026-10-02:1 |
| 10.2 | 6 | 2026-10-02 | M20 — Perplexity, Understanding that is hidden, Doubt | R3:2026-10-02:12 |
| 10.3 | 7 | 2026-10-12 | Num 16:13; Tit 3:3; Gen 42:9, M72 group B, #1998 | R3:2026-10-12:2 |
| 10.3 | 6 | 2026-10-09 | Joh 2:17; Gen 37:11, #1993 | R3:2026-10-09:5 |
| 10.3 | 5 | 2026-10-04 | life-death unit 3, living before God, #1940 | R2:Strand updates — life and death (M25), unit 3: living bef |
| 10.3 | 4 | 2026-10-03 | life-death unit 2, dying and death, #1939 | R2:Strand updates — life and death (M25), unit 2: dying and  |
| 10.3 | 3 | 2026-10-02 | life-death unit 1 | R3:2026-10-02:11 |
| 10.3 | 2 | 2026-10-02 | chapter pointer, #1936; **new**, NS-M3 | R3:2026-10-02:1 |
| 10.4 | 13 | 2026-10-13 | Eze 20:32–33, M02 pairing gaps, OT-29/30/51 | R2:Strand updates — anger (M02) pairings with strands alread |
| 10.4 | 12 | 2026-10-12 | Mat 21:25–27, M72 group B, #1998 | R3:2026-10-12:2 |
| 10.4 | 11 | 2026-10-12 | Amos 6:2, M18 × M72, #1993 item H | R2:Strand updates — desire (M18) × authority (M72): the 51 n |
| 10.4 | 10 | 2026-10-09 | the centurion (Luk 7:4–9), #1993 | R3:2026-10-09:5 |
| 10.4 | 9 | 2026-10-09 | the lordly price (Zec 11:13; Mat 27:9), #1993 | R3:2026-10-09:5 |
| 10.4 | 8 | 2026-10-08 | 2Sa 14:14 set in Joab's plea; "those who have put themselves outside" removed, #1990 | R2:Strand updates — citations needing attention (2026-10-08, |
| 10.4 | 7 | 2026-10-08 | planning, #1986: Eze 38:10, Huram-abi, reckoning and being reckoned, Deu 19:19 | R2:Strand updates — planning (M64): the 77 inner-being verse |
| 10.4 | 6 | 2026-10-04 | life-death unit 3, living before God, #1940 ("Thinking and life") | R2:Strand updates — life and death (M25), unit 3: living bef |
| 10.4 | 5 | 2026-10-03 | life-death unit 2, dying and death, #1939 | R2:Strand updates — life and death (M25), unit 2: dying and  |
| 10.4 | 4 | 2026-10-02 | chapter pointer, #1936; anger strand) (was 10.3 | R3:2026-10-02:1 |
| 10.5 | 21 | 2026-10-12 | Gen 40:16; Shimei 1Ki 2:38, M18 × M72, #1993 item H | R2:Strand updates — desire (M18) × authority (M72): the 51 n |
| 10.5 | 20 | 2026-10-12 | Mat 27:43; 1Ti 1:5–7, M18 group C (will) by role, #1993 | R2:Strand updates — desire (M18), group C: will, willing, ac |
| 10.5 | 19 | 2026-10-11 | the vow and the mouth (Ecc 5:2–7), M18 group B remaining 94 by role, #1993 | R2:Strand updates — desire (M18), group B: the 94 remaining  |
| 10.5 | 18 | 2026-10-09 | cursing put on (Psa 109:16–18); mockery (Psa 22:7–9), M18 group B correction by main operation, #1993 | R2:Strand updates — desire (M18), group B sets 1 and 2 corre |
| 10.5 | 17 | 2026-10-09 | long prayers for a pretense, and the widow (Mar 12:38–44), #1993 | R3:2026-10-09:5 |
| 10.5 | 16 | 2026-10-09 | utter what is precious (Jer 15:18–19), #1993 | R2:Strand updates — desire (M18), group F: precious (2026-10 |
| 10.5 | 15 | 2026-10-09 | Job 6:2–3, weight and rash words, #1993 | R3:2026-10-09:5 |
| 10.5 | 14 | 2026-10-09 | silence held too long, the heart hot (Psa 39:1–4), #1993 | R2:Strand updates — desire (M18) × life and death (M25), and |
| 10.5 | 13 | 2026-10-09 | Psa 45:1; Pro 16:24, #1993 | R3:2026-10-09:5 |
| 10.5 | 12 | 2026-10-04 | life-death unit 3, living before God, #1940 ("The oath") | R2:Strand updates — life and death (M25), unit 3: living bef |
| 10.5 | 11 | 2026-10-03 | life-death unit 2, dying and death, #1939 | R2:Strand updates — life and death (M25), unit 2: dying and  |
| 10.5 | 10 | 2026-10-02 | life-death unit 1 | R3:2026-10-02:11 |
| 10.5 | 9 | 2026-10-02 | chapter pointer, #1936; anger, fear strands | R3:2026-10-02:1 |
| 10.5 | 7 | 2026-10-02 | M20 — Grumbling, Whispering | R3:2026-10-02:13 |
| 10.5 | 8 | 2026-10-02 | pointer to 10.11) (was 10.4 | R3:2026-10-02:14 |
| 10.6 | 22 | 2026-10-12 | Simon (Act 8:18–23); Ecc 5:19–20; Gen 37:8, M72 group B, #1998 | R3:2026-10-12:2 |
| 10.6 | 21 | 2026-10-12 | David 2Sa 11:2–4; 2Sa 18:27, M18 × M72, #1993 item H | R2:Strand updates — desire (M18) × authority (M72): the 51 n |
| 10.6 | 20 | 2026-10-12 | wanting to see Jesus; Luk 16:26; Job 6:8–10, M18 group C (will) by role, #1993 | R2:Strand updates — desire (M18), group C: will, willing, ac |
| 10.6 | 19 | 2026-10-11 | good eye; Ecc 11:7–9; Job 21:21; 1Ki 21:2; Jam 4:3, M18 group B remaining 94 by role, #1993 | R2:Strand updates — desire (M18), group B: the 94 remaining  |
| 10.6 | 18 | 2026-10-09 | *Delight* moved to 10.1, pointer kept, #1993 | R2:Strand updates — desire (M18), group B set 1: the delight |
| 10.6 | 17 | 2026-10-09 | Paul’s wish (Act 26:28–29), #1993 | R3:2026-10-09:5 |
| 10.6 | 16 | 2026-10-09 | M18 group F: **new** *Precious*; Psa 36:7–8 in *Aimed at God*; two ways to fill a house in *Possessions*; Babylon's cargo in *Taken away*, # | R2:Strand updates — desire (M18), group F: precious (2026-10 |
| 10.6 | 15 | 2026-10-09 | M18 group E: *Thirst answered* widened (rivers out of the heart; "I thirst"; thirst answered, forgotten, and as judgment; want borne for oth | R2:Strand updates — desire (M18), group E: thirst, hunger (2 |
| 10.6 | 14 | 2026-10-09 | M18 group D: zeal read into *Jealousy and envy*; **new** *Jealousy against a person* and *A husband's jealousy with no witness*, #1993 | R2:Strand updates — desire (M18), group D: jealousy, zeal (2 |
| 10.6 | 13 | 2026-10-09 | M18 group A: **new *Coveting***; the verbs of desire; Paul's longing; *tĕšûqāh*; craving filled and unsatisfied; greed's reasons; what is ta | R2:Strand updates — desire (M18), group A: desire, craving,  |
| 10.6 | 12 | 2026-10-09 | M18 × M02: Phinehas beside Elijah; Psa 37 and Pro 24 envy answered; jealousy as infancy (1Co 3); Rom 13; where desire ends; Lam 2:4, #1993 | R3:2026-10-09:5 |
| 10.6 | 11 | 2026-10-09 | **sectioned**; M18 × M25 read-back and the held items: through the eye (Gen 3:6), enjoyment given against the rich fool, wanting that owns,  | R2:Strand updates — desire (M18) × life and death (M25), and |
| 10.6 | 10 | 2026-10-09 | M18 × M47 read-back: desire in the heart and held there, the Preacher, delight, the wilderness craving, evil desire, wanting God and people, | R2:Strand updates — desire (M18) × M47: read-back of the nar |
| 10.6 | 9 | 2026-10-08 | a want met and refused; wanting toward harm, #1986 | R3:2026-10-08:6 |
| 10.6 | 8 | 2026-10-08 | wanting beside choosing, M64 §2a, #1978 | R3:2026-10-08:15 |
| 10.6 | 7 | 2026-10-04 | life-death unit 3, living before God, #1940 | R2:Strand updates — life and death (M25), unit 3: living bef |
| 10.6 | 6 | 2026-10-03 | life-death unit 2, dying and death, #1939 | R2:Strand updates — life and death (M25), unit 2: dying and  |
| 10.6 | 5 | 2026-10-02 | Q4 pointer, longing, #1938 | R2:Strand updates — life and death (M25), Q4: the body and t |
| 10.6 | 4 | 2026-10-02 | chapter pointers, #1936; anger strand) (was 10.5 | R3:2026-10-02:1 |
| 10.7 | 27 | 2026-10-12 | *Convinced that I ought*; *Rule offered, refused, and sought*, M72 group B, #1998 | R3:2026-10-12:2 |
| 10.7 | 26 | 2026-10-12 | the king's pleasure, asked for; Mal 3:1, M18 × M72, #1993 item H | R2:Strand updates — desire (M18) × authority (M72): the 51 n |
| 10.7 | 25 | 2026-10-12 | *Willing* widened (Rom 7:15–21; doing the will of God; the will asked; redirected; going back; Herod; willing heart), Paul's plans, M18 grou | R2:Strand updates — desire (M18), group C: will, willing, ac |
| 10.7 | 24 | 2026-10-11 | Eli; Balaam; 1Sa 14; Esther 3 and 8; 1Ch 13; Gen 20:15; 2Ki 10:5, M18 group B remaining 94 by role, #1993 | R2:Strand updates — desire (M18), group B: the 94 remaining  |
| 10.7 | 23 | 2026-10-09 | Gen 49:15, Pro 9:13–18, 2Sa 15:26, Isa 58:2, Psa 141:4–8, 2Sa 24:3, M18 group B correction by main operation, #1993 | R2:Strand updates — desire (M18), group B sets 1 and 2 corre |
| 10.7 | 22 | 2026-10-09 | aims (Rom 15:20; 2Co 5:9; 1Th 4:11), #1993 | R3:2026-10-09:5 |
| 10.7 | 21 | 2026-10-09 | Naaman in *Whose measure*; Luk 15:28; Dan 11:36, #1993 | R3:2026-10-09:5 |
| 10.7 | 20 | 2026-10-09 | Mat 19 (Isaiah 1 "one place" sentence restated); Joh 5:40–44; Ruth's redeemer; 2Ti 3:12; Joh 21:18; 2Ch 19:3; Pro 14:14; Isa 47:13–14, #1993 | R3:2026-10-09:5 |
| 10.7 | 19 | 2026-10-09 | Jer 6:16; Act 7:38-39; willing gifts with joy; a will under another, #1993 | R3:2026-10-09:5 |
| 10.7 | 18 | 2026-10-08 | Deu 30:14, 17, 20; Phili 1:22-25; Luk 10:39-42; Exo 36:2; Psa 51:13; 2Sa 14 Joab, #1992 | R2:Strand updates — the 18 include verses (2026-10-08, #1992 |
| 10.7 | 17 | 2026-10-08 | working note, Job's own voice beside the friends' verdicts; Job 7:15 also with life and death, #1990 | R2:Strand updates — citations needing attention (2026-10-08, |
| 10.7 | 16 | 2026-10-08 | working note, #1986 | R3:2026-10-08:6 |
| 10.7 | 15 | 2026-10-08 | **new section *Willing***, after *Planning*, from the will reading, #1986 | R3:2026-10-08:6 |
| 10.7 | 14 | 2026-10-08 | **new section *Planning***, the 77 inner-being plan verses, #1986 | R2:Strand updates — planning (M64): the 77 inner-being verse |
| 10.7 | 13 | 2026-10-08 | Moses and Levite placements confirmed, working-note line removed, #1978 | R3:2026-10-08:15 |
| 10.7 | 12 | 2026-10-08 | **new section *Others around a choice***, M64 choose §2c account, #1978 | R2:Strand updates — choosing (M64), §2c: 10.7 *Others around |
| 10.7 | 11 | 2026-10-08 | **new section *Being chosen***, M64 choose §2b account, #1978 | R2:Strand updates — choosing (M64), §2b: 10.7 *Being chosen* |
| 10.7 | 10 | 2026-10-08 | **reframed around the account of choosing**, M64 choose §2a, #1978 | R3:2026-10-08:15 |
| 10.7 | 9 | 2026-10-04 | life-death unit 3, living before God, #1940 | R2:Strand updates — life and death (M25), unit 3: living bef |
| 10.7 | 8 | 2026-10-03 | life-death unit 2, dying and death, #1939 | R2:Strand updates — life and death (M25), unit 2: dying and  |
| 10.7 | 7 | 2026-10-02 | life-death unit 1; anger, fear strands) (was 10.6 | R3:2026-10-02:16 |
| 10.8 | 7 | 2026-10-09 | judging without partiality (Pro 24:23–25), M18 group B correction by main operation, #1993 | R2:Strand updates — desire (M18), group B sets 1 and 2 corre |
| 10.8 | 6 | 2026-10-09 | pressure toward wrong (Psa 125:3–4), #1993 | R3:2026-10-09:5 |
| 10.8 | 5 | 2026-10-02 | chapter pointers, #1936; anger, fear strands) (was 10.7 | R3:2026-10-02:1 |
| 10.9 | 22 | 2026-10-13 | Deu 31:16–18; Psa 89:46–47; Jer 33:5–6, M02 pairing gaps, OT-29/30/51 | R2:Strand updates — anger (M02) pairings with strands alread |
| 10.9 | 21 | 2026-10-12 | new *Kept from what would rule*, *Under rule, and longing for his*, *Knowing who rules*, M72 group B, #1998 | R3:2026-10-12:2 |
| 10.9 | 20 | 2026-10-12 | Psa 145:19; the leper's plea, M18 group C (will) by role, #1993 | R2:Strand updates — desire (M18), group C: will, willing, ac |
| 10.9 | 19 | 2026-10-11 | Psa 90:13–17, M18 group B remaining 94 by role, #1993 | R2:Strand updates — desire (M18), group B: the 94 remaining  |
| 10.9 | 18 | 2026-10-09 | comforted as by a mother; told to depart; returned to; contending; not fearing; calling in distress, M18 group B correction by main operatio | R2:Strand updates — desire (M18), group B sets 1 and 2 corre |
| 10.9 | 17 | 2026-10-09 | sought and not far (Act 17:27); recognised and gone to (Joh 21:7–8), #1993 | R3:2026-10-09:5 |
| 10.9 | 16 | 2026-10-09 | envy undone in the sanctuary (Psa 73); new *Waiting, and pleading*; *Calling on God to wake* given its grounds and Isaiah's answer, #1993, # | R2:Strand updates — desire (M18) × life and death (M25), and |
| 10.9 | 15 | 2026-10-08 | plotting against God, his word reckoned strange, #1986 | R3:2026-10-08:6 |
| 10.9 | 14 | 2026-10-04 | life-death unit 4, roused and stirred, #1949 ("Calling on God to wake") | R2:Strand updates — life and death (M25), unit 4: roused and |
| 10.9 | 13 | 2026-10-04 | life-death unit 3, living before God, #1940 ("The living God") | R2:Strand updates — life and death (M25), unit 3: living bef |
| 10.9 | 12 | 2026-10-03 | life-death unit 2, dying and death, #1939 | R2:Strand updates — life and death (M25), unit 2: dying and  |
| 10.9 | 11 | 2026-10-02 | life-death unit 1 | R3:2026-10-02:11 |
| 10.9 | 10 | 2026-10-02 | chapter pointer, #1936; anger, fear strands | R3:2026-10-02:1 |
| 10.9 | 8 | 2026-10-02 | M20 — When God hides his face | R3:2026-10-02:17 |
| 10.9 | 9 | 2026-10-02 | pointers to 10.11) (was 10.8 | R3:2026-10-02:18 |
| 10.10 | 23 | 2026-10-12 | new *Holding authority over another* and *A right set aside for another*; Lev 25:46–55; 2Sa 23:3; Eph 6:9; Est 9:1, M72 group B, #1998 | R3:2026-10-12:2 |
| 10.10 | 22 | 2026-10-12 | golden rule; Act 14:13; Luk 9:54; Job 6:28, M18 group C (will) by role, #1993 | R2:Strand updates — desire (M18), group C: will, willing, ac |
| 10.10 | 21 | 2026-10-11 | 2Sa 3:36; 2Sa 19:18–30; Gen 19:8, M18 group B remaining 94 by role, #1993 | R2:Strand updates — desire (M18), group B: the 94 remaining  |
| 10.10 | 20 | 2026-10-09 | snare; refused duty; following past a body; before a king; Timothy sent; Elihu; betrayal, M18 group B correction by main operation, #1993 | R2:Strand updates — desire (M18), group B sets 1 and 2 corre |
| 10.10 | 19 | 2026-10-09 | the father and the son’s self-rating (Luk 15:19–22), #1993 | R3:2026-10-09:5 |
| 10.10 | 18 | 2026-10-09 | the visit kept seldom (Pro 25:16–17), #1993 | R3:2026-10-09:5 |
| 10.10 | 17 | 2026-10-09 | another's thirst met, refused or used (Mat 25; Rut 2:9; Jdg 4:19; Lam 4:4; Job 24:11), #1993 | R2:Strand updates — desire (M18), group E: thirst, hunger (2 |
| 10.10 | 16 | 2026-10-09 | Pro 14:35; 2Co 12:20, #1993 | R3:2026-10-09:5 |
| 10.10 | 15 | 2026-10-09 | Jonathan's delight (1Sa 19); the avenger's heat (Deu 19:6); new *Friends, company and care*, #1993, #1942 | R3:2026-10-09:19 |
| 10.10 | 14 | 2026-10-08 | 2Sa 19:23, #1992 | R2:Strand updates — the 18 include verses (2026-10-08, #1992 |
| 10.10 | 13 | 2026-10-08 | consent refused, a will pressed, intent pinned, #1986 | R3:2026-10-08:6 |
| 10.10 | 12 | 2026-10-08 | **new section *Plotting against another***, #1986 | R3:2026-10-08:6 |
| 10.10 | 11 | 2026-10-04 | life-death unit 3, living before God, #1940 ("Loyalty and honour") | R2:Strand updates — life and death (M25), unit 3: living bef |
| 10.10 | 10 | 2026-10-03 | life-death unit 2, dying and death, #1939 (loyalty to death, answerable for another's death) | R2:Strand updates — life and death (M25), unit 2: dying and  |
| 10.10 | 9 | 2026-10-02 | life-death unit 1; anger, fear strands | R3:2026-10-02:20 |
| 10.10 | 8 | 2026-10-02 | M20 — care, discouragement and hiding between people) (was 10.9 | R3:2026-10-02:21 |
| 10.11 | 8 | 2026-10-12 | Mat 21:27, M72 group B, #1998 | R3:2026-10-12:2 |
| 10.11 | 7 | 2026-10-12 | Hezekiah shows all, M18 × M72, #1993 item H | R2:Strand updates — desire (M18) × authority (M72): the 51 n |
| 10.11 | 6 | 2026-10-12 | Jesus not able to be hidden, M18 group C (will) by role, #1993 | R2:Strand updates — desire (M18), group C: will, willing, ac |
| 10.11 | 5 | 2026-10-11 | words of surrender (1Sa 11:9–11), M18 group B remaining 94 by role, #1993 | R2:Strand updates — desire (M18), group B: the 94 remaining  |
| 10.11 | 4 | 2026-10-09 | the guards’ report covered with money (Mat 28:11–15), #1993 | R3:2026-10-09:5 |
| 10.11 | 3 | 2026-10-08 | the friendly word as cover, Neh 6:2; Jer 11:19; Psa 140:5, #1986 | R3:2026-10-08:6 |
| 10.11 | 2 | 2026-10-03 | life-death unit 2, dying and death, #1939; **new**, NS-D1, M20 | R2:Strand updates — life and death (M25), unit 2: dying and  |
| 10.12 | 8 | 2026-10-13 | Psa 76:7–9; Rev 11:18; Pro 20:2–3, M02 pairing gaps, OT-29/30/51 | R2:Strand updates — anger (M02) pairings with strands alread |
| 10.12 | 7 | 2026-10-12 | Lev 26:17; Luk 12:5; Pilate; fear of the crowd; Jer 51:46; Dan 6:26, M72 group B, #1998 | R3:2026-10-12:2 |
| 10.12 | 6 | 2026-10-12 | Mar 6:48–50; Joh 6:21, M18 group C (will) by role, #1993 | R2:Strand updates — desire (M18), group C: will, willing, ac |
| 10.12 | 5 | 2026-10-09 | Exo 14:12, #1993 | R3:2026-10-09:5 |
| 10.12 | 4 | 2026-10-08 | Pro 1:29 and Isa 66:2, both "I read", #1992 | R2:Strand updates — the 18 include verses (2026-10-08, #1992 |
| 10.12 | 3 | 2026-10-08 | Psa 31:13-14, the psalmist answers in his own words, #1991 | R2:Strand updates — citations to check (2026-10-08, #1991) |
| 10.12 | 2 | 2026-10-08 | fear stops the will, #1986; **new**, #1961: the full account of fear, as its own sub-chapter | R3:2026-10-08:22 |
| 10.13 | 8 | 2026-10-13 | Deu 31:17, 27–29; Lam 2:20–22; Isa 51:17–22; Zep 2:3; Pro 11:4; Psa 76:7–9; Pro 29:8; Pro 20:2; Job 19:29; Rev 11:18; Chapter 2 hold note re | R2:Strand updates — anger (M02) pairings with strands alread |
| 10.13 | 7 | 2026-10-12 | Num 16:15; Act 26:10–11, M72 group B, #1998 | R3:2026-10-12:2 |
| 10.13 | 6 | 2026-10-09 | Gamaliel held in honour (Act 5:34), #1993 | R2:Strand updates — desire (M18) × life and death (M25), and |
| 10.13 | 5 | 2026-10-08 | Isa 10:12-15, #1992 | R2:Strand updates — the 18 include verses (2026-10-08, #1992 |
| 10.13 | 4 | 2026-10-08 | Saul's selective refusal; unwilling to listen, #1986 | R3:2026-10-08:6 |
| 10.13 | 3 | 2026-10-08 | Psa 37:12; Act 5:33, rage that wants to kill at once, #1986 | R3:2026-10-08:6 |
| 10.13 | 2 | 2026-10-05 | **Ch 13 folded in** as the section *Living under God's anger*, #1977 | R2:Ch 13 folded into 10.13 (2026-10-05, #1977, OT-13) |
| 10.13 | 1 | 2026-10-05 | **new**, #1963 step 4: the full account of anger, as its own sub-chapter | R2:Strand updates — anger (M02): new 10.13 "Anger" (2026-10- |
| 11 | 31 | 2026-10-12 | **retitled *Other sides of the inner being*** and opening restated (a gathering of what has no other home), #1998 | R2:Strand updates — authority (M72), group B: current though |
| 11 | 30 | 2026-10-12 | v30: §7 *Authority as a standing* (first reading; title under question, OT-100), M72 group B, #1998 | R3:2026-10-12:23 |
| 11 | 29 | 2026-10-12 | 2Sa 15:3, M18 × M72, #1993 item H | R2:Strand updates — desire (M18) × authority (M72): the 51 n |
| 11 | 28 | 2026-10-12 | §4 whose will, M18 group C (will) by role, #1993 | R2:Strand updates — desire (M18), group C: will, willing, ac |
| 11 | 27 | 2026-10-11 | §4 delight faces; "what seems good to you", M18 group B remaining 94 by role, #1993 | R2:Strand updates — desire (M18), group B: the 94 remaining  |
| 11 | 26 | 2026-10-09 | §4 delight faces: thanks and taunt, an offering refused then delighted in, being well pleased; two *What changes the character* entries, #19 | R3:2026-10-09:5 |
| 11 | 25 | 2026-10-09 | §4 precious, #1993 | R2:Strand updates — desire (M18), group F: precious (2026-10 |
| 11 | 24 | 2026-10-09 | §4 zeal and jealousy against a person, #1993 | R2:Strand updates — desire (M18), group D: jealousy, zeal (2 |
| 11 | 23 | 2026-10-09 | §4 *tĕšûqāh* and panting, #1993 | R3:2026-10-09:5 |
| 11 | 22 | 2026-10-09 | §6 zeal passes on (2Co 9:2), #1993 | R2:Strand updates — desire (M18), group D: jealousy, zeal (2 |
| 11 | 21 | 2026-10-09 | §4 five new faces (eat-drink-be-merry, jealousy, rousing oneself, the redeemer's will, whom the need is spoken to); §5 three voices, #1993 | R2:Strand updates — desire (M18), group B: three Ch 11 §4 fa |
| 11 | 20 | 2026-10-09 | §2 Ecc 9:7, #1993 | R3:2026-10-09:5 |
| 11 | 19 | 2026-10-08 | §1 "Even the leaning is formed" restated, the Gen 6:5 word link removed; §4 "many things or one"; §8 Gen 6:5-6 quoted as written, #1991 | R2:Strand updates — citations to check (2026-10-08, #1991) |
| 11 | 18 | 2026-10-08 | §4 face "Willing", #1986 | R3:2026-10-08:6 |
| 11 | 17 | 2026-10-08 | §4 faces "Purposing" and "Planning ahead", #1986 | R2:Strand updates — planning (M64): 13.1 *Purposing* (2026-1 |
| 11 | 16 | 2026-10-08 | §4 faces "Desire beside a choice", "Despising", "Knowing that a choice was made", fear beside a choice, M64 §2c, #1978 | R3:2026-10-08:15 |
| 11 | 15 | 2026-10-08 | §4 faces "Choosing a person" and "Holiness", factor "Who chooses", M64 §2b, #1978 | R2:Strand updates — choosing (M64): Ch 11 §4 five faces (202 |
| 11 | 14 | 2026-10-08 | choosing, M64 §2a, #1978, §4 five faces (good or evil in your eyes; knowing good and evil; refusing; choosing; delight), factor "Whose eyes, | R2:Strand updates — choosing (M64): Ch 11 §4 five faces (202 |
| 11 | 13 | 2026-10-04 | life-death unit 4, roused and stirred, #1949, §4 "Who rouses, and toward what" | R2:Strand updates — life and death (M25), unit 4: roused and |
| 11 | 12 | 2026-10-04 | life-death unit 3, living before God, #1940, §4 "Who swears it, and what for", "What it is joined to" | R2:Strand updates — life and death (M25), unit 3: living bef |
| 11 | 11 | 2026-10-03 | life-death unit 2, dying and death, #1939, §4 "What brings it about, and who acts" | R2:Strand updates — life and death (M25), unit 2: dying and  |
| 11 | 10 | 2026-10-02 | life-death unit 1, §4 "What it is set against" | R3:2026-10-02:24 |
| 11 | 9 | 2026-10-02 | chapter pointers, #1936; anger, fear strands | R3:2026-10-02:1 |
| 11 | 8 | 2026-10-02 | M20 faces and factors | R3:2026-10-02:25 |
| 12 | 20 | 2026-10-12 | Dan 4:30 beside 5:20, M72 group B, #1998 | R3:2026-10-12:2 |
| 12 | 19 | 2026-10-09 | *Pride*: Haman (Est 6:6–13), M18 group B correction by main operation, #1993 | R2:Strand updates — desire (M18), group B sets 1 and 2 corre |
| 12 | 18 | 2026-10-09 | Eze 28:13–17, #1993 | R3:2026-10-09:5 |
| 12 | 17 | 2026-10-09 | Eze 31:9–10, #1993 | R3:2026-10-09:5 |
| 12 | 16 | 2026-10-09 | Psa 5:9; Isa 44:9, #1993 | R3:2026-10-09:5 |
| 12 | 15 | 2026-10-09 | the idol-maker warmed and deceived (Isa 44:15–20; 47:14), #1993 | R3:2026-10-09:5 |
| 12 | 14 | 2026-10-09 | Pro 16:19, #1993 | R3:2026-10-09:5 |
| 12 | 13 | 2026-10-08 | Rom 8:7 "indeed, it cannot", #1992 | R2:Strand updates — the 18 include verses (2026-10-08, #1992 |
| 12 | 12 | 2026-10-04 | life-death unit 4, roused and stirred, #1949 | R2:Strand updates — life and death (M25), unit 4: roused and |
| 12 | 11 | 2026-10-04 | life-death unit 3, living before God, #1940 | R2:Strand updates — life and death (M25), unit 3: living bef |
| 12 | 10 | 2026-10-03 | life-death unit 2, dying and death, #1939 | R2:Strand updates — life and death (M25), unit 2: dying and  |
| 12 | 9 | 2026-10-02 | chapter pointers, #1936; anger, fear strands | R3:2026-10-02:1 |
| 12 | 8 | 2026-10-02 | M20 hidden trap | R3:2026-10-02:26 |
| 13 | 2 | 2026-10-08 | God bullet points to 13.1 choosing, #1978 | R3:2026-10-08:15 |
| 13 | 1 | 2026-10-07 | **new, replaces the pointer to 10.13**, #1982: why the chapter is included, and what has been found so far; old v10 pointer and earlier vers | R3:2026-10-07:27 |
| 13.1 | 23 | 2026-10-13 | *Ruling* gains Eze 20:32–37 and Rev 11:17–18, M02 pairing gaps, OT-29/30/51 | R2:Strand updates — anger (M02) pairings with strands alread |
| 13.1 | 22 | 2026-10-12 | new section *Ruling*, M72 group B, #1998 | R3:2026-10-12:2 |
| 13.1 | 21 | 2026-10-12 | his delight claimed for evildoers (Mal 2:17; 3:3), M18 × M72, #1993 item H | R2:Strand updates — desire (M18) × authority (M72): the 51 n |
| 13.1 | 20 | 2026-10-12 | the Son's and the Father's will; offerings accepted; his favor, M18 group C (will) by role, #1993 | R2:Strand updates — desire (M18), group C: will, willing, ac |
| 13.1 | 19 | 2026-10-11 | *Purposing* Isa 44, 46, 48; *Delight* 1Sa 15:22, Mal 1:10, Ecc 5:4, Psa 135:6, Num 24:1, Pro 8:30–31, M18 group B remaining 94 by role, #199 | R2:Strand updates — desire (M18), group B: the 94 remaining  |
| 13.1 | 18 | 2026-10-09 | Isa 55:10–11 to *Purposing*, M18 group B correction by main operation, #1993 | R2:Strand updates — desire (M18), group B sets 1 and 2 corre |
| 13.1 | 17 | 2026-10-09 | *Delight*: the voice on the mountain; his good pleasure gives; not pleased though they shared it all; Heb 10:5–10, #1993 | R3:2026-10-09:5 |
| 13.1 | 16 | 2026-10-09 | *Delight* widened: strength refused, truth within; whom he delights in; his delight in people’s mouths; not the offering itself; does what p | R2:Strand updates — desire (M18), group B set 1: the delight |
| 13.1 | 15 | 2026-10-09 | *Delight*: Ephraim my dear son (Jer 31:20); the price paid (1Pe 1:18–19), #1993 | R2:Strand updates — desire (M18), group B set 1: the delight |
| 13.1 | 14 | 2026-10-09 | *Jealousy* widened from M18 group D: his name in the commandment, roused by prayer, zeal that does the work, put on as a cloak, #1993 | R2:Strand updates — desire (M18), group D: jealousy, zeal (2 |
| 13.1 | 13 | 2026-10-09 | *What he desires*; Deu 7:7, 10:15, #1993 | R3:2026-10-09:5 |
| 13.1 | 12 | 2026-10-09 | *Jealousy* widened from the M18 × M02 read-back; Mic 7:18, Isa 60:10, Rom 9:22, #1993 | R3:2026-10-09:5 |
| 13.1 | 11 | 2026-10-09 | *Delight* widened (no pleasure in death; Psa 116:15; 1Sa 2:25; Pro 8:35); *Willing* (Joh 5:21; 6:38–40, Gethsemane sentence restated; 21:22) | R2:Strand updates — desire (M18) × life and death (M25), and |
| 13.1 | 10 | 2026-10-09 | **new section *Delight***, God's delight and pleasure, from the M18 × M47 read-back, #1993 | R2:Strand updates — desire (M18) × M47: read-back of the nar |
| 13.1 | 9 | 2026-10-08 | 2Sa 14:14 set in Joab's plea, #1990 | R2:Strand updates — citations needing attention (2026-10-08, |
| 13.1 | 8 | 2026-10-08 | *Choosing* gains his eyes and heart at the place he chose, 2Ch 7:12-20, and his servant chosen with delight and the Spirit, Mat 12:18 quotin | R2:Strand updates — the 29 M64 × M47 verses: 13.1 *Choosing* |
| 13.1 | 7 | 2026-10-08 | new section *Willing*, God's will, the Son's choosing, the Spirit's willing, Gethsemane, #1986 | R3:2026-10-08:6 |
| 13.1 | 6 | 2026-10-08 | the Spirit intercedes according to the will of God, Rom 8:26-27; the Spirit counted part of the divine for 13.1, #1986 | R2:Strand updates — planning (M64): 13.1, the Spirit (2026-1 |
| 13.1 | 5 | 2026-10-08 | new section *Purposing*, God's plans, from the plan-set verses, #1986 | R2:Strand updates — planning (M64): 13.1 *Purposing* (2026-1 |
| 13.1 | 4 | 2026-10-08 | from the §2c readings: he answers those set against his choosing; calls those who do not know him; blesses at the place he chose; what he ch | R2:Strand updates — choosing (M64), §2c: 10.7 *Others around |
| 13.1 | 3 | 2026-10-08 | from the §2b readings: he chooses before anything is in the one chosen; he searches hearts and acts on them, including giving over (2Th 2:11 | R2:Strand updates — choosing (M64), §2b: 10.7 *Being chosen* |
| 13.1 | 2 | 2026-10-08 | first content, "Choosing", from the M64 §2a readings, #1978; working note: God's wider choosing verses not yet placed | R3:2026-10-08:15 |
| 13.1 | 1 | 2026-10-07 | **new**, empty | R3:2026-10-07:28 |
| 13.2 | 5 | 2026-10-12 | angels with authority; Jude 6, 9; Hos 12:4; 1Co 11:10, M72 group B, #1998 | R3:2026-10-12:2 |
| 13.2 | 4 | 2026-10-12 | Psa 103:20–21, M18 group C (will) by role, #1993 | R2:Strand updates — desire (M18), group C: will, willing, ac |
| 13.2 | 3 | 2026-10-09 | an angel wakes a prophet to see (Zec 4:1–2), #1942 | R2:Strand updates — desire (M18) × life and death (M25), and |
| 13.2 | 2 | 2026-10-09 | first content, 1Pe 1:12, #1993; **new**, empty | R3:2026-10-09:5 |
| 13.3 | 3 | 2026-10-12 | authorities that are not human (Eph 6:12); Luk 10:17–20; Act 19:16; Luk 22:53; Rev 13, M72 group B, #1998 | R3:2026-10-12:2 |
| 13.3 | 2 | 2026-10-12 | first content, the devil's will, M18 group C (will) by role, #1993; **new**, empty | R2:Strand updates — desire (M18), group C: will, willing, ac |
| 13.4 | 5 | 2026-10-12 | lights that rule; creatures under man's dominion, M72 group B, #1998 | R3:2026-10-12:2 |
| 13.4 | 4 | 2026-10-09 | *Harm ended* (Isa 11:6–9), M18 group B correction by main operation, #1993 | R2:Strand updates — desire (M18), group B sets 1 and 2 corre |
| 13.4 | 3 | 2026-10-09 | Joe 1:20; Ecc 1:5, #1993 | R3:2026-10-09:5 |
| 13.4 | 2 | 2026-10-09 | **first content**: God's look on what he made; the creatures' thirst met; the ostrich, #1993; **new**, empty | R2:Strand updates — desire (M18), group E: thirst, hunger (2 |
| 14 | 15 | 2026-10-12 | new *Sin's rule ended* (Rom 6:12–16), M72 group B, #1998 | R3:2026-10-12:2 |
| 14 | 14 | 2026-10-09 | **new** *Brought near* (Eph 2:12–18), M18 group G, #1993 | R2:Strand updates — desire (M18), group G: gloss away from d |
| 14 | 13 | 2026-10-08 | 1Ch 29:18 given its referent, 29:17, #1991 | R2:Strand updates — citations to check (2026-10-08, #1991) |
| 14 | 12 | 2026-10-04 | life-death unit 3, living before God, #1940 | R2:Strand updates — life and death (M25), unit 3: living bef |
| 14 | 11 | 2026-10-03 | life-death unit 2, dying and death, #1939 | R2:Strand updates — life and death (M25), unit 2: dying and  |
| 14 | 10 | 2026-10-02 | Q4 pointers, #1938 | R2:Strand updates — life and death (M25), Q4: the body and t |
| 14 | 9 | 2026-10-02 | life-death unit 1; anger, fear strands | R3:2026-10-02:20 |
| 14 | 8 | 2026-10-02 | M20) (was 13 | R3:2026-10-02:29 |
| 15 | 7 | 2026-10-02 | chapter pointer, #1936; anger, fear strands | R3:2026-10-02:1 |
| 15 | 6 | 2026-10-02 | M20; "seat" removed) (was 14 | R3:2026-10-02:30 |

## 7. Multi-chapter cells, split one row per chapter (test 6.5)

4 register lines name more than one chapter. In the correlation each counts once per chapter (today's numbering).

| Update | Where | Chapters (today) |
|---|---|---|
| Strand updates — origin of thought (2026-10-01, #1918) | Ch 7, 9, 11, 13; 10.1, 10.5–10.9 | 08, 02, 11, 14, 10.1, 10.6, 10.7, 10.8, 10.9, 10.10 |
| Strand updates — life and death (M25), unit 1 and the Ch 2 rewrite (20 | Ch 4, 6; 10.2, 10.3, 10.5, 10.7, 10.9, 10.10; Ch 11 §4; Ch 13; Ch 14 | 04, 06, 10.2, 10.3, 10.5, 10.7, 10.9, 10.10, 11, 13 (retired: Under God's anger), 14 |
| Strand updates — life and death (M25), unit 2: dying and death (2026-1 | 10.1, 10.3, 10.4, 10.5, 10.6, 10.7, 10.9, 10.10, 10.11; Ch 11 §4; Ch 12; Ch 13;  | 10.1, 10.3, 10.4, 10.5, 10.6, 10.7, 10.9, 10.10, 10.11, 11, 12, 13 (retired: Under God's anger), 14 |
| Strand updates — life and death (M25), unit 3: living before God (2026 | Ch 4, 6; 10.1–10.7, 10.9, 10.10; Ch 11 §4; Ch 12; Ch 13; Ch 14 | 04, 06, 10.1, 10.2, 10.3, 10.4, 10.5, 10.6, 10.7, 10.9, 10.10, 11, 12, 13 (retired: Under God's anger), 14 |

## 8. Chapter numbers mapped across the renumberings (test 6.6)

25 register lines were written in older numbering (#1920 on 2026-10-01: 10.3–10.9 → 10.4–10.10, 13 → 14, 14 → 15; #1936 on 2026-10-02: 9 → 2, 2–8 → 3–9; Ch 13 between #1920 and #1982 is the retired *Under God's anger*).

| Date | Update | As written | Today |
|---|---|---|---|
| 2026-10-01 | Strand updates — origin of thought (2026-10-01, #1918) | 3 | 04 |
| 2026-10-01 | Strand updates — origin of thought (2026-10-01, #1918) | 3 | 04 |
| 2026-10-01 | Strand updates — origin of thought (2026-10-01, #1918) | 10.3 | 10.4 |
| 2026-10-01 | Strand updates — origin of thought (2026-10-01, #1918) | 7, 9, 11, 13, 10.1, 10.5, 10.6, 10.7, 10.8, 10.9 | 08, 02, 11, 14, 10.1, 10.6, 10.7, 10.8, 10.9, 10.10 |
| 2026-10-01 | Strand updates — change of character in the thought strand ( | 10.3 | 10.4 |
| 2026-10-01 | Strand updates — change of character in the thought strand ( | 10.3 | 10.4 |
| 2026-10-01 | Strand updates — change of character in the thought strand ( | 10.3 | 10.4 |
| 2026-10-01 | Strand updates — change of character in the thought strand ( | 10.8 | 10.9 |
| 2026-10-01 | Strand updates — change of character in the thought strand ( | 10.9 | 10.10 |
| 2026-10-01 | Strand updates — change of character in the thought strand ( | 10.4 | 10.5 |
| 2026-10-01 | Strand updates — change of character in the thought strand ( | 13 | 14 |
| 2026-10-01 | Strand updates — anger (M02) (2026-10-01, #1920) | 9 | 02 |
| 2026-10-01 | Strand updates — anger (M02) (2026-10-01, #1920) | 13 | 13 (retired: Under God's anger) |
| 2026-10-01 | Strand updates — fear (M01), unit 1 (2026-10-01, #1927, #192 | 3 | 04 |
| 2026-10-01 | Strand updates — fear (M01), unit 1 (2026-10-01, #1927, #192 | 6 | 07 |
| 2026-10-01 | Strand updates — fear (M01), unit 1 (2026-10-01, #1927, #192 | 9 | 02 |
| 2026-10-01 | Strand updates — fear (M01), unit 1 (2026-10-01, #1927, #192 | 13 | 13 (retired: Under God's anger) |
| 2026-10-01 | Strand updates — fear (M01), unit 2 (2026-10-01, #1929) | 3 | 04 |
| 2026-10-01 | Strand updates — fear (M01), unit 2 (2026-10-01, #1929) | 5 | 06 |
| 2026-10-01 | Strand updates — fear (M01), unit 2 (2026-10-01, #1929) | 6 | 07 |
| 2026-10-01 | Strand updates — fear (M01), unit 2 (2026-10-01, #1929) | 13 | 13 (retired: Under God's anger) |
| 2026-10-01 | Fear account integrated for review (2026-10-01, #1930) | 13 | 13 (retired: Under God's anger) |
| 2026-10-02 | Strand updates — life and death (M25), unit 1 and the Ch 2 r | 4, 6, 10.2, 10.3, 10.5, 10.7, 10.9, 10.10, 11, 13, 14 | 04, 06, 10.2, 10.3, 10.5, 10.7, 10.9, 10.10, 11, 13 (retired: Under God's anger), 14 |
| 2026-10-03 | Strand updates — life and death (M25), unit 2: dying and dea | 10.1, 10.3, 10.4, 10.5, 10.6, 10.7, 10.9, 10.10, 10.11, 11, 12, 13, 14 | 10.1, 10.3, 10.4, 10.5, 10.6, 10.7, 10.9, 10.10, 10.11, 11, 12, 13 (retired: Under God's anger), 14 |
| 2026-10-04 | Strand updates — life and death (M25), unit 3: living before | 4, 6, 10.1, 10.2, 10.3, 10.4, 10.5, 10.6, 10.7, 10.9, 10.10, 11, 12, 13, 14 | 04, 06, 10.1, 10.2, 10.3, 10.4, 10.5, 10.6, 10.7, 10.9, 10.10, 11, 12, 13 (retired: Under God's anger), 14 |

## 9. Escalations and threads named but not found (test 6.10)

None: every escalation and thread named in the updates exists in the escalation table.
