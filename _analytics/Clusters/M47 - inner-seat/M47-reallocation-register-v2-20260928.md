# M47 re-allocation register — cluster membership changes flagged by the M47 work (v2)

**Date:** 2026-09-28
**Status:** **READY FOR APPROVAL — escalation #1880.** Nothing has been applied.
**Supersedes:** v1 (`archive/`). **v2 changes**, per the researcher's #1880 update (verbatim: "proceed to prepare this excalation for ready for approval"):
- Every item now carries a concrete proposal. The five v1 "decision" items (T-03, T-04, C-R4, C-R5, E-R6) are resolved to proposals: C-R5 by a STEP check; the rest as no-change or a file-only change.
- The apply script is built and has been run **dry-run** over all 72 items as if approved: 0 skips, 0 problems (§3).

**How approval works:** approving #1880 approves **every item as proposed**. To reject or amend individual items, name them (by ID) in the approval comment. Those items are then set to your ruling, and only the rest are applied.
**Researcher instruction (verbatim, 2026-09-28):** "1 - yes draft the list; 2 - if you have access, then apply it, as long as you follow governance and the configs 3 - yes, anything identified in the M47 work and the batches that flags a re-allocation should be included."
**Machine-readable twin:** `iba/docs/m47-cluster-reallocation-spec-v2-20260928.json` (same items; `"approved"` is set to true only after you approve #1880).
**Apply script:** `iba/app/migration/apply_m47_reallocation_1880_v1_20260928.py`.
**Background:** `M47-t-code-to-m-code-question-v1-20260928.md` (why it matters; risk) · `M47-seat-coverage-and-unseated-verses-v1-20260928.md` (why it comes first).
**This register also closes Batch A R7** (option b: one consolidated register, one approval point).

---

## 1. How to use this file

- One row per item. The Ruling boxes are optional: use them, or list exceptions in your #1880 approval comment.
- **Strength:**
  - **clear** — the verses and the cluster description agree on the move
  - **weak** — defensible, but another home is possible
  - **proposed** — a resolved v1 "decision" item: the proposal is stated in the Note
  - **by-design** — the current filing matches the cluster's own description; no change proposed
- **Live now** is read from `cluster_strong` today: code, then confidence or source, then the verse count from `verse_lexical`.
- **Operations:**
  - **add** — a second code; nothing removed (dual-coding precedent: H0639G is M02 + T14)
  - **move** — soft-delete the old row, insert the new one
  - **remove** — soft-delete one row, where another correct row remains
  - **alt** — record an alternative cluster on the row
  - **review_flag** — mark for later review

## 2. Scale and checks (measured 2026-09-28)

- **72 items; 114 Strong's.** 50 items change membership; 17 only add an alternative or a review flag, or change nothing. Every operation was validated against live rows: **0 problems** (each source row exists; no target is already present).
- **Clusters touched:** 49 M-clusters and 6 T-clusters. All are at `t_cluster_assignment_completed`, **except M67 Sloth & Diligence** (`ready_for_observations`, with draft verse-reading observations) — see caution 2.
- **Observations:** 7 live observations sit under a cluster that a word would leave (B-R3 G0746/M16, D-R2 G0080/M14, E-R2 H5650/M36, S-02 G1731/M05, S-14 H7235A/M23 ×2, S-17 G5342/M70). They are verse-reading notes, and they stay as recorded; nothing is deleted.

**Cautions:**
1. **Order.** Apply this register **before** the seat-coverage tie-profile and pilot, so those run on the corrected membership.
2. **M67** gains H7423B (D-R9) and H5647I (E-R3). Its verse-reading will then stop at the stale-role gate (#1719) until Layer 1 is rebuilt for those verses. That is the gate working as designed, but M67 reading is in progress. **Rule on these two knowing that.**
3. **The dual-code items** (T-01, T-02, T-06) add inner-being codes to words with many verses: "die" (699 + 99 verses), "death" (151 + 106). M25's verse set grows accordingly.
4. **Group V and the resolved items** T-03, T-04, C-R5 and E-R6 change nothing in `cluster_strong`. **C-R4 is file-only:** the spirit classification CSV goes v1 → v2 (Psa 106:33 → [U]).

## 3. Dry run and what approval sets in motion

**Dry run (2026-09-28, all 72 items as if approved; nothing written):**
- 0 items skipped; 0 missing source rows
- **88 Strong's** change membership, occurring in **6,696 verses** (of 29,760)
- The largest by verse count are: H1696G "speak" 971 · H5650 "servant" 715 · H4191 "die" 699 · H3548 "priest" 628 · H6965B "arise" 370 · H5002 "utterance" 358 · G0080 "brother" 315 · H1697I "thing" 272
- **Role-refresh scope:** `lexical.build` works per chapter, so 1,119 chapters in all 66 books (about 66 per-book runs). This is local compute, with the precedent of the full Layer-1 rebuild on 2026-09-16. It needs the STEP server up (`step.required_for_runs`).

**On approval, in order:**
1. `"approved": true` is set on every item (except any you name), and your approval comment is recorded as the ruling.
2. The migration runs: `--dry-run`, then live. It is soft-delete-and-insert, with source `researcher-ruling-1880-20260928` and a rationale quoting item, ruling and #1880.
3. `VerseLexical.ps1 -Step lexical.build` runs per book over the affected chapters, then a stale-role check on every touched cluster (#1719).
4. The spirit CSV goes v1 → v2 (C-R4).
5. A `BUILD.md` entry is written; #1880 is updated with the outcome; `Session-Close.ps1` runs.
6. The M47 surface and pairs CSVs are regenerated and diffed; Batches A–H are revisited for the delta only. The seat-coverage tie-profile follows.


## Group T — inner-being terms currently hidden in T-codes

| ID | Source | Strong's | Live now | Proposed | Strength | Note | **Ruling** |
|---|---|---|---|---|---|---|---|
| T-01 | today: T/M question §1; Batch G §0.2 | H4191, G0599 'to die' | G0599: T3(high) · 99v<br>H4191: T3(llm) · 699v | H4191: add **M25**<br>G0599: add **M25** | clear | Death side of Life & Death is invisible to every M reading. M25 description names 'death, dying'. Keep T3 (operation) row; add M25 as a second code (dual-code precedent H0639G M02+T14). | ☐ approve ☐ amend ☐ reject |
| T-02 | today §1; Batch G §0.2 | H4194, G2288 'death' | G2288: T10(old) · 106v<br>H4194: T10(old) · 151v | H4194: add **M25**<br>G2288: add **M25** | clear | In T10 by researcher-approved decision (#1598: death as a realm). M25 names 'death'. Keep T10 (realm) row; add M25. | ☐ approve ☐ amend ☐ reject |
| T-03 | today §1; Batch B R2; depiction §2.1c | H0559 'to say' (4,340 verses) | — | no change | proposed | Inner-being only in 'said in his heart'. Coding all 4,340 verses to an M-cluster would flood it. PROPOSED: no re-code. Include T3 'say' (H0559) in the M47 angle as a tie class in the seat-coverage work, so the 'said in his heart' series is covered without flooding an M-cluster. | ☐ approve ☐ amend ☐ reject |
| T-04 | today §1; seat-coverage §2 | H7130G qereb 'entrails: among' | — | no change | proposed | Mostly the preposition 'in the midst of'; the 'inward parts' sense is a minority. PROPOSED: no re-code. Treat qereb as a body-seat tie class in the seat-coverage work (ruling 4 unchanged). | ☐ approve ☐ amend ☐ reject |
| T-05 | today §1; seat-coverage §2; ruling 4 | H3629 kidney, H4578 bowels/belly, H0990G/H/J belly, H7358 womb | H0990G: T2(medium) · 16v<br>H0990H: T2(medium) · 45v<br>H0990J: T2(medium) · 9v<br>H3629: T2(old) · 26v<br>H4578: T2(old) · 30v<br>H7358: T2(old) · 25v | H3629: T2 → **T14**<br>H4578: T2 → **T14**<br>H0990G: T2 → **T14**<br>H0990H: T2 → **T14**<br>H0990J: T2 → **T14**<br>H7358: T2 → **T14** | clear | Body parts filed in the T2 catch-all; T14's own description names 'entrails/bowels = compassion'. T2 -> T14 only. Ruling 4 (not separate M47 study words) is unchanged. Adding any of them to M47 is a separate researcher decision. | ☐ approve ☐ amend ☐ reject |
| T-06 | today §1 | G4698 splanchna 'affection / entrails' | G4698: T2(old) · 11v | G4698: T2 → **T14**<br>G4698: add **M50** | weak | NT use is mostly 'affection, compassion' (Phi 1:8; Col 3:12). T2 -> T14 (body part) plus M50 Grace & Mercy (compassion). Alternative M51 Love (affection). | ☐ approve ☐ amend ☐ reject |

## Group R — formal ruling items, Batches A–E

| ID | Source | Strong's | Live now | Proposed | Strength | Note | **Ruling** |
|---|---|---|---|---|---|---|---|
| A-R1 | Batch A R1 | H3513H 'to honor: heavy' | H3513H: T3(llm), M03(heuris) · 32v | H3513H: M03 → **M75** | clear | 'heavy' = hardened heart (Pharaoh); M03 by family heuristic. M75 names 'hardening'. M03 -> M75; T3 row kept. | ☐ approve ☐ amend ☐ reject |
| A-R2 | Batch A R2 | H2256M, H5688, H3499B 'cord' | H2256M: M03(auto), T12(heuris) · 46v<br>H3499B: M03(auto), T12(heuris) · 6v<br>H5688: M03(auto), T12(heuris) · 23v | H2256M: remove M03<br>H5688: remove M03<br>H3499B: remove M03 | clear | Cord sense of the cord/pang homograph; T12 row already records no inner-being significance. Remove M03; keep T12. | ☐ approve ☐ amend ☐ reject |
| A-R3 | Batch A R3 | H7451C 'distress: harm' | H7451C: M24(heuris) · 152v | H7451C: M24 + alt M55/M58 | weak | Mostly evil done/suffered; some verses are inner distress. Keep M24, alternatives M55 / M58. | ☐ approve ☐ amend ☐ reject |
| A-R4 | Batch A R4 | H7186 'severe / hard / stubborn' | H7186: M24(old) · 36v | H7186: M24 → **M30** | clear | Heart sense is stubbornness (M30). M24 -> M30. | ☐ approve ☐ amend ☐ reject |
| A-R5 | Batch A R5 | H0926 'to dismay; hasten' | H0926: M24(heuris) · 39v | H0926: M24 + alt M69 | weak | Two senses; haste = restraint of heart/spirit. Keep M24, alternative M69. | ☐ approve ☐ amend ☐ reject |
| A-R6 | Batch A R6 | H5641, H3582, H2244, H2934, G2928 'to hide' | G2928: M20(auto) · 17v<br>H2244: M20(auto) · 33v<br>H2934: M20(auto) · 28v<br>H3582: M20(high) · 30v<br>H5641: M20(old) · 80v | H5641: M20 review_flag<br>H3582: M20 review_flag<br>H2244: M20 review_flag<br>H2934: M20 review_flag<br>G2928: M20 review_flag | weak | Hiding is not doubt; the M20 link is God hiding his face. Keep M20; set review_flag. | ☐ approve ☐ amend ☐ reject |
| B-R1 | Batch B R1 | H1696G, H1696I, H0981 'to speak' | H0981: M42(low) · 3v<br>H1696G: M42(low) · 971v<br>H1696I: M42(low) · 78v | H1696G: M42 → **M65**<br>H1696I: M42 → **M65**<br>H0981: M42 → **M65**<br>H1696G: M65 + alt M42 | clear | Ordinary speech filed under Prayer (keyword, low confidence, already review-flagged). M42 -> M65; H1696G keeps M42 as alternative for 'entreat'. | ☐ approve ☐ amend ☐ reject |
| B-R3 | Batch B R3 | G0746 archē 'beginning / rule' | G0746: M16(old) · 55v | G0746: M16 → **M72** | clear | Came into M16 via the M17 merge; senses are time and rule. M16 -> M72. | ☐ approve ☐ amend ☐ reject |
| B-R4 | Batch B R4 | H1697I 'word: thing' | H1697I: M65(heuris) · 272v | H1697I: M65 → **T2** | clear | Non-speech sense of dāvār. M65 -> T2. | ☐ approve ☐ amend ☐ reject |
| C-R1 | Batch C R1 | H2638 'lacking' | H2638: M18(heuris) · 18v | H2638: M18 → **M16** | clear | A lack, not a desire; 'lacking heart' = folly. M18 -> M16. | ☐ approve ☐ amend ☐ reject |
| C-R2 | Batch C R2 | H8003 'complete / whole' | H8003: M34(high) · 27v | H8003: M34 → **M12** | clear | Whole (integral) heart, not endurance. M34 -> M12. | ☐ approve ☐ amend ☐ reject |
| C-R3 | Batch C R3 | H1793A 'contrite' | H1793A: M11(old) · 2v | H1793A: M11 → **M09**<br>H1793A: M09 + alt M11 | clear | Crushed spirit; M09's description names 'contrition'. M11 -> M09 (description match), M11 as alternative. | ☐ approve ☐ amend ☐ reject |
| C-R4 | Batch C R4 | Psa 106:33 whose spirit | — | no change | proposed | Spirit class, not cluster membership. Lives in the M47 spirit CSV, not a DB table. PROPOSED (file, not DB): mark Psa 106:33 H7307G as [U] in the spirit classification CSV (v1 -> v2), noting both readings (Moses' spirit / God's Spirit). | ☐ approve ☐ amend ☐ reject |
| C-R5 | Batch C R5 | 1Sa 30:6 tagged H4784 'rebel' | — | no change | by-design | Verse-level tagging (mārâ / mārar), not membership. PROPOSED: no change. Checked 2026-09-28: STEP itself tags 1Sa 30:6 'bitter' as H4784, and verse_lexical follows the source faithfully. Recorded as a lexical note (mārâ / mārar), not corrected. | ☐ approve ☐ amend ☐ reject |
| D-R1 | Batch D R1 | H6965B 'arise' | H6965B: M08(medium) · 370v | H6965B: M08 → **T3** | clear | Movement verb inflating M08. M08 -> T3. | ☐ approve ☐ amend ☐ reject |
| D-R2 | Batch D R2 | G0080 'brother' | G0080: M14(medium), T8(heuris) · 315v | G0080: remove M14 | clear | Duplicate of the correct T8 row with a wrong sense. Remove M14; keep T8. | ☐ approve ☐ amend ☐ reject |
| D-R3 | Batch D R3 | clean / unclean family | G2511: M12(old) · 28v<br>G2513: M12(old) · 23v<br>G2514: M12(auto) · 1v<br>H1249: M12(old) · 7v<br>H2134: M12(high) · 11v<br>H2135: M12(old) · 8v<br>H2889: M12(old) · 87v<br>H2891: M12(old) · 79v<br>H2932: M56(heuris) · 31v | H2889: M12 → **M61**<br>H2891: M12 → **M61**<br>H2135: M12 → **M61**<br>H1249: M12 → **M61**<br>H2134: M12 → **M61**<br>G2513: M12 → **M61**<br>G2511: M12 → **M61**<br>G2514: M12 → **M61**<br>H2932: M56 → **M10c** | clear | Split across M12, M56, M61, M10c. Clean/pure words M12 -> M61; H2932 uncleanness M56 -> M10c. | ☐ approve ☐ amend ☐ reject |
| D-R4 | Batch D R4 | H5081G 'willing / generous' | H5081G: M09(old) · 5v | H5081G: M09 → **M64** | clear | Readiness to give, not lowliness. M09 -> M64. | ☐ approve ☐ amend ☐ reject |
| D-R5 | Batch D R5 | H4102, G5549, G1299, G0757, G2117 | G0757: M08(old) · 86v<br>G1299: M09(old) · 16v<br>G2117: M62(heuris) · 18v<br>G5549: M09(auto) · 5v<br>H4102: M09(high) · 9v | H4102: M09 → **T3**<br>G5549: M09 → **T3**<br>G1299: M09 → **T3**<br>G0757: M08 → **T3**<br>G2117: M62 + alt T6 | clear | Function verbs/adverbs (delay, direct, begin, immediately). Four to T3; G2117 keeps M62 with T6 alternative. | ☐ approve ☐ amend ☐ reject |
| D-R6 | Batch D R6 | H0034, H1800, H7326, H6035, G4434 poverty | H0034: M09(heuris) · 58v<br>H1800: M09(heuris) · 46v<br>H7326: M09(heuris) · 24v | H0034: M09 + alt M46<br>H1800: M09 + alt M46<br>H7326: M09 + alt M46 | by-design | M09's own description names 'being needy/poor' — by design. Keep M09 (description match); alternative M46 on the three mainly-material words. | ☐ approve ☐ amend ☐ reject |
| D-R7 | Batch D R7 | H7451A 'bad', H7489A 'be evil' | H7451A: M58(old) · 64v<br>H7489A: M58(old) · 94v | H7451A: M58 + alt M03/M28<br>H7489A: M58 + alt M03/M28 | weak | raʿ covers every register of 'bad'. Keep M58, alternatives M03 / M28. | ☐ approve ☐ amend ☐ reject |
| D-R8 | Batch D R8 | H4974, H5352, H8235, H1305 in M61 | H1305: M61(heuris) · 16v<br>H4974: M61(heuris) · 4v<br>H5352: M61(heuris) · 33v<br>H8235: M61(heuris) · 1v | H4974: M61 → **M73**<br>H5352: M61 → **M26**<br>H8235: M61 → **T13**<br>H1305: M61 review_flag | clear | Heuristic misfits. As listed; H1305 flagged. | ☐ approve ☐ amend ☐ reject |
| D-R9 | Batch D R9 | H1892, H7423B, H3908 (+H3584, H3868, H5956) in M14 | H3908: M14(old) · 5v<br>H7423B: M14(old) · 5v | H7423B: M14 → **M67**<br>H3908: M14 → **T12** | clear | Partial fits to 'deceit'. H7423B -> M67; H3908 -> T12; the rest stay (verse-level notes). | ☐ approve ☐ amend ☐ reject |
| D-R10 | Batch D R10 | H2778A, H1984H (+H3887, height words) in M08 | H1984H: M08(old) · 21v<br>H2778A: M08(heuris) · 38v | H2778A: M08 → **M53**<br>H1984H: M08 + alt M22 | clear | Reproach is disgrace; hālal splits praise/boast. H2778A -> M53; H1984H alternative M22. | ☐ approve ☐ amend ☐ reject |
| E-R1 | Batch E R1 | H5002 'utterance' (declares the Lord) | H5002: M42(low) · 358v | H5002: M42 → **M43** | clear | Oracle formula, not prayer (keyword, low, review-flagged). M42 -> M43. | ☐ approve ☐ amend ☐ reject |
| E-R2 | Batch E R2 | H5650 'servant' | H5650: M36(medium) · 715v | H5650: M36 → **T8**<br>H5650: T8 + alt M36 | clear | Social role; only 'servant of the Lord' is worship. M36 -> T8, M36 as alternative. | ☐ approve ☐ amend ☐ reject |
| E-R3 | Batch E R3 | G2323 heal, H6633 wage war, H5647I labour in M36 | G2323: M36(medium) · 42v<br>H5647I: M36(old) · 30v<br>H6633: M36(medium) · 12v | G2323: M36 → **M45**<br>H6633: M36 → **T3**<br>H5647I: M36 → **M67** | clear | Healing, war, farm work. As listed (H6633 to T3 rather than M10). | ☐ approve ☐ amend ☐ reject |
| E-R4 | Batch E R4 | salvation family M45 / M79 | G1295: M45(high) · 8v<br>G4982: M45(old) · 100v<br>H2502A: M45(auto) · 23v<br>H3467: M45(high) · 199v<br>H5337: M45(low) · 194v<br>H8668G: M45(old) · 21v | H8668G: M45 → **M79**<br>H3467: M45 + alt M79<br>H5337: M45 + alt M79<br>H2502A: M45 + alt M79<br>G4982: M45 + alt M79<br>G1295: M45 + alt M79 | weak | Verb 'save' in Renewal, noun 'salvation' in Salvation. Move the noun H8668G; save-verbs keep M45 with M79 alternative (respects the M38 merge). | ☐ approve ☐ amend ☐ reject |
| E-R5 | Batch E R5 | H1285, H3772H, G1242, G1303 covenant | G1242: M44(old) · 30v<br>G1303: M44(heuris) · 6v<br>H1285: M44(old) · 264v<br>H3772H: M44(old) · 87v | H1285: M44 → **M32**<br>H3772H: M44 → **M32**<br>G1242: M44 → **M32**<br>G1303: M44 → **M32** | weak | M32 'Covenant' holds only circumcision words. M44 -> M32 — unless the 2026-08-13 decision meant M32 as circumcision only. | ☐ approve ☐ amend ☐ reject |
| E-R6 | Batch E R6 | faith family M13 / M31 / M19 | — | no change | proposed | A cluster-structure question. PROPOSED: no change in this escalation. Record for a separate cluster-structure review (merge M31 into M13; G4100 believe). | ☐ approve ☐ amend ☐ reject |
| E-R7 | Batch E R7 | H0269, G0079 sister; H7378, G1264 contend in M44 | G0079: M44(old) · 24v<br>G1264: M44(medium) · 1v<br>H0269: M44(auto) · 94v<br>H7378: M44(old) · 59v | H0269: M44 → **T8**<br>G0079: M44 → **T8**<br>H7378: M44 → **M26**<br>G1264: M44 → **M26** | clear | Kin nouns are parties; contend is legal dispute. As listed. | ☐ approve ☐ amend ☐ reject |
| E-R8 | Batch E R8 | H7311A rûm, H1431 gādal in M22 | H1431: M22(old) · 114v<br>H7311A: M22(heuris) · 184v | H7311A: M22 + alt M08<br>H1431: M22 + alt M08 | weak | 'Lift up the heart' is the pride idiom. Keep M22, alternative M08. | ☐ approve ☐ amend ☐ reject |
| E-R9 | Batch E R9 | G0040H 'saints' | G0040H: M13(heuris) · 52v | G0040H: M13 → **M61** | clear | Same lemma as G0040G 'holy' (M61). M13 -> M61. | ☐ approve ☐ amend ☐ reject |
| E-R10 | Batch E R10 | H5375O lift [soul], H8667 pledge | H5375O: M19(old) · 9v<br>H8667: M19(high) · 1v | H5375O: M19 + alt M18<br>H8667: M19 → **M46** | clear | Trust/desire split; pledge is financial. H5375O alternative M18; H8667 -> M46. | ☐ approve ☐ amend ☐ reject |
| E-R11 | Batch E R11 | G3140, H5749B 'testify' | G3140: M35(heuris) · 74v<br>H5749B: M35(heuris) · 36v | G3140: M35 → **M82**<br>H5749B: M35 → **M82** | weak | Test and testify joined on the English word. M35 -> M82 (receiving cluster weak; M65 possible). | ☐ approve ☐ amend ☐ reject |

## Group S — Strong's-level misfiles from the §0 lists

| ID | Source | Strong's | Live now | Proposed | Strength | Note | **Ruling** |
|---|---|---|---|---|---|---|---|
| S-01 | Batch F §0.2 | H2763A, H2764A ḥērem 'devote to destruction' | H2763A: M51(heuris) · 47v<br>H2764A: M51(heuris) · 22v | H2763A: M51 → **M55**<br>H2764A: M51 → **M55** | clear | Filed under Love & Devotion on the English 'devote'. M51 -> M55. | ☐ approve ☐ amend ☐ reject |
| S-02 | Batch F §0.2 | H3384B teach, H2324 / G1166 / G1731 show | G1166: M05(auto) · 29v<br>G1731: M05(old) · 11v<br>H2324: M05(auto) · 13v<br>H3384B: M05(auto) · 47v | H3384B: M05 → **M16**<br>H2324: M05 → **T3**<br>G1166: M05 → **T3**<br>G1731: M05 → **T3** | weak | Teaching/showing filed under Kindness. Teach -> M16 (names 'teaching'); show -> T3. | ☐ approve ☐ amend ☐ reject |
| S-03 | Batch F §0.2 | G0268 'sinful / sinner' | G0268: M10(old) · 45v | G0268: M10 → **M56** | clear | Filed under Violence & Cruelty. M10 -> M56. | ☐ approve ☐ amend ☐ reject |
| S-04 | Batch F §0.2 | H8263 'detestable thing' (Lev 11) | H8263: M06(old) · 11v | H8263: M06 → **M10c** | weak | Ritual abomination filed under Malice. M06 -> M10c. | ☐ approve ☐ amend ☐ reject |
| S-05 | Batch C §0.8 | H6569 'dung' | H6569: M30(heuris) · 6v | H6569: M30 → **T2** | clear | Filed under Rebellion via the gloss 'refuse'. H1561 'dung' is in T2. M30 -> T2 (H1561 precedent). | ☐ approve ☐ amend ☐ reject |
| S-06 | Batch C §0.8 | H0014 'be willing' | H0014: M30(old) · 52v | H0014: M30 → **M64**<br>H0014: M64 + alt M30 | weak | Willingness filed under Rebellion because it occurs as 'would not'. M30 -> M64, M30 as alternative (refusal). | ☐ approve ☐ amend ☐ reject |
| S-07 | Batch C §0.8 | H6424 pālas 'weigh / level' | H6424: M28(high) · 6v | H6424: M28 → **T3** | clear | Filed under Envy & Greed. M28 -> T3. | ☐ approve ☐ amend ☐ reject |
| S-08 | Batch D §0.7 | H7806 'twist' (twined linen) | H7806: M57(heuris) · 19v | H7806: M57 → **T12** | clear | Filed under Corruption & Perversion. M57 -> T12. | ☐ approve ☐ amend ☐ reject |
| S-09 | Batch E §0.3 | H7121H 'call by name' | H7121H: M42(heuris) · 208v | H7121H: M42 → **T3** | clear | Naming, filed under Prayer. M42 -> T3. | ☐ approve ☐ amend ☐ reject |
| S-10 | Batch E §0.3 | G5455 phōneō 'call / crow' | G5455: M42(old) · 38v | G5455: M42 → **M84** | weak | Generic calling out. M42 -> M84 Outcry. G2564G 'call' left in M42 (mixed). | ☐ approve ☐ amend ☐ reject |
| S-11 | Batch E §0.3 | H2487 'change (of garments)' | H2487: M45(old) · 11v | H2487: M45 → **T12** | clear | Filed under Renewal on the gloss 'change'. M45 -> T12. | ☐ approve ☐ amend ☐ reject |
| S-12 | Batch E §0.3 | G2021 'attempt / undertake' | G2021: M35(old) · 3v | G2021: M35 → **T3** | clear | Filed under Being Tested. M35 -> T3. | ☐ approve ☐ amend ☐ reject |
| S-13 | Batch E §0.3 | H3548 'priest' | H3548: M36(medium) · 628v | H3548: M36 → **T8**<br>H3548: T8 + alt M36 | weak | Party term (Lev 13 procedure); parallels E-R2. M36 -> T8, M36 alternative. | ☐ approve ☐ amend ☐ reject |
| S-14 | Batch G §0.3 | H7235A 'multiply' | H7235A: M23(old) · 211v | H7235A: M23 → **T3** | clear | Generic verb in Strength & Courage. M23 -> T3. | ☐ approve ☐ amend ☐ reject |
| S-15 | Batch G §0.3 | H3201 'be able / can' | H3201: M23(old) · 183v | H3201: M23 → **T3**<br>H3201: T3 + alt M23 | weak | Generic verb; 'prevail' sense is strength. M23 -> T3, M23 alternative. | ☐ approve ☐ amend ☐ reject |
| S-16 | Batch G §0.3 | H7122G 'meet / toward' | H7122G: M37(old) · 83v | H7122G: M37 → **T3** | clear | Encounter, filed under Firstborn & Foreknowledge. M37 -> T3. | ☐ approve ☐ amend ☐ reject |
| S-17 | Batch G §0.3 | G5342 'bring / lead' | G5342: M70(heuris) · 60v | G5342: M70 → **T3** | clear | Generic verb in Lifting & Bearing. M70 -> T3. | ☐ approve ☐ amend ☐ reject |
| S-18 | Batch H §0.2 | H5329 nāṣaḥ 'choirmaster / oversee' | H5329: M76(heuris) · 65v | H5329: M76 → **T3**<br>H5329: T3 + alt M22 | weak | Psalm superscription filed under Walk & Conduct via 'conduct'. M76 -> T3, M22 alternative (music). | ☐ approve ☐ amend ☐ reject |
| S-19 | Batch H §0.2 | H4487 mānâ 'count / appoint' | H4487: M26(auto) · 27v | H4487: M26 → **T3** | clear | Filed under Judgment. M26 -> T3. | ☐ approve ☐ amend ☐ reject |
| S-20 | Batch H §0.2 | H4931 mišmeret 'charge / safekeeping' | H4931: M26(medium) · 69v | H4931: M26 → **M74** | clear | Guarding, filed under Judgment. M26 -> M74. | ☐ approve ☐ amend ☐ reject |
| S-21 | Batch H §0.2 | H7230 rōv 'abundance / multitude' | H7230: M46(old) · 144v | H7230: M46 review_flag | weak | Mostly quantity (multitude of iniquity, idols). Keep M46; set review_flag. | ☐ approve ☐ amend ☐ reject |
| S-22 | Batch C §0.8 | H5493H 'turn aside: depart', G5290 'return' | G5290: M11(auto) · 34v<br>H5493H: M11(heuris) · 66v | H5493H: M11 review_flag<br>G5290: M11 review_flag | weak | Mostly literal travel. Keep M11 (names 'returning'); set review_flag. | ☐ approve ☐ amend ☐ reject |

## Group V — verse-level or by design: no `cluster_strong` change

| ID | Source | Strong's | Live now | Proposed | Strength | Note | **Ruling** |
|---|---|---|---|---|---|---|---|
| V-01 | Batch A §0.2 | H6381 'wonder' (hard / special) | — | no change | by-design | Sense varies by verse. No change. | ☐ approve ☐ amend ☐ reject |
| V-02 | Batch A §0.2 | H5708, G4509 'filth' | — | no change | by-design | M53 names 'filth'. No change. | ☐ approve ☐ amend ☐ reject |
| V-03 | Batch B §0.3 | H4609A 'thought' (Psa 131 'Ascents'), H8454 (Job 30:22 'toss') | — | no change | by-design | Verse-level tag / text difficulty. No change. | ☐ approve ☐ amend ☐ reject |
| V-04 | Batch C §0.8 | H5800A leave (oath formula), H3176G wait (Jer 4:19), H2803 devise | — | no change | by-design | Verse-level sense; M30 names 'forsaking'. No change; Jer 4:19 Kethiv/Qere is a tagging note. | ☐ approve ☐ amend ☐ reject |
| V-05 | Batch D §0.7 | G0950 confirm, H7451H bad (ugly cows) | — | no change | by-design | Verse-level sense. No change. | ☐ approve ☐ amend ☐ reject |
| V-06 | Batch E §0.3 | H3680 cover, H4171 change, H5737A help (M45); H5254H test; H5203 leave, G0630G release (M59); G2564G, H7121G call (M42); G2129 flattery | — | no change | by-design | Verse-level senses; several match the cluster description. No change. | ☐ approve ☐ amend ☐ reject |
| V-07 | Batch F §0.2-3 | H5117 rest (put / leave); H2790B be quiet | — | no change | by-design | M33 names 'quiet, stillness'. No change. | ☐ approve ☐ amend ☐ reject |
| V-08 | Batch G §0.3 | H2416 alive (raw / wild beasts); M71 H4768, G5092, H2122; H3027H hand | — | no change | by-design | Verse-level senses. No change. | ☐ approve ☐ amend ☐ reject |
| V-09 | Batch H §0.2; Batch D §0.7 | H5110 nûd (pity), M46 quantity uses; M47's own H7307I 'side', H5315 'perfume box', H5315N 'neck' | — | no change | by-design | Ruling 1 keeps all M47 senses. No change (ruling 1). | ☐ approve ☐ amend ☐ reject |
