# WA M10 — Logical-units gap register (living tracker, single 1–32 namespace)

- **File:** wa-m10-family-logical-units-gap-register-v1-20260623.md · **v1 · 2026-06-23 · Author:** Claude Code.
- **Purpose:** the **living tracker** for the 32 M10 units across two phases — **(A) evidence-gathering** and **(B) by-unit synthesis** — with a definitional **gate** between. Records per unit: status, the files holding its evidence/synthesis, and its key remaining gap. **Update protocol:** on completing an evidence or synthesis file, record its filename and flip the status. File→unit lookup: **`wa-m10-unit-index-1to32-v1-20260623.md`** (the navigation index).

> **MERGED 2026-06-23:** M10b + M10c collapsed into **M10**, single **1–32** numbering (old M10b #1–6 → #23–28; M10c #1–4 → #29–32; crosswalk in the unit index). Source-family kept as a tag: **core** (1–22) · **wick** (23–28) · **defi** (29–32). DB merge: `scripts/_apply_merge_m10bc_into_m10_20260623.py` (snapshot `backups/bible_research_pre-merge-m10bc_20260623.db`).

## Phase model (per unit)
```
(A) EVIDENCE-GATHERING ──▶ [GATE §10: define characteristic vs status vs other-object] ──▶ (B) BY-UNIT SYNTHESIS
```
- **(A):** `COMPLETE` (freshly read, neutral method, + DB) · `RINGS`/`PARTIAL`/`DB-ONLY`/`SCRATCH` (legacy states, now all resolved to COMPLETE).
- **GATE:** the §10 definitional exploration (framework §10 + architecture-reflection) — no unit enters (B) before it is settled.
- **(B):** `NOT STARTED` for all (gated).
- **File codes** (DB · HA · AV · PE · HM · MC · R1 · R2g · R2p · R3 · R4 · B1–B5 · Bsum): resolved in the **unit index** legend.

## Tracker — all 32 units
| # | Unit | Src | (A) | Evidence files | (B) | Synth files | Key remaining gap |
|---|---|---|---|---|---|---|---|
| 1 | Wilful sinning | core | COMPLETE | DB·HA·HM·R2p | — | — | intent-marker per-occurrence |
| 2 | Unintentional sinning | core | COMPLETE | DB·HA | — | — | intent/awareness distinction |
| 3 | Confession | core | COMPLETE | DB·HA·HM | — | — | shared w/ M11 (home call) |
| 4 | Conscience suppression | core | COMPLETE | DB·HA·HM | — | — | conscience-seat thin |
| 5 | Refusal to repent | core | COMPLETE | DB·HA·HM | — | — | M11 seam |
| 6 | Habitual defection | core | COMPLETE | DB·HA·HM | — | — | over-time = data-shape |
| 7 | Contagious sin | core | COMPLETE | DB·HA | — | — | relational transmission = data-shape |
| 8 | Political revolt | core | COMPLETE | DB·PE | — | — | political vs God-ward split (§10) |
| 9 | Sinful speech | core | COMPLETE | DB·R2p | — | — | reconcile w/ #28 (verb); M06 |
| 10 | Specialised sinful mechanisms | core | COMPLETE | DB·R1 | — | — | tiny corpus; M14/M08/M31 home calls |
| 11 | Sin as universal condition | core | COMPLETE | DB·HM·HA·R2p | — | — | status-candidate flagship |
| 12 | Sin as enslaving power | core | COMPLETE | DB·HM | — | — | Romans dominion register |
| 13 | Sin as divine record | core | COMPLETE | DB·HA·AV | — | — | largest DB; written/recorded register |
| 14 | Forgiveness sought and received | core | COMPLETE | DB·HA·HM·R4 | — | — | atonement seam (Thread 1); split w/ M11 |
| 15 | Generational sin | core | COMPLETE | DB·HA·AV | — | — | lineage = data-shape |
| 16 | The sinner as moral character | core | COMPLETE | DB·HM·HA | — | — | pair w/ #23 |
| 17 | Guilt as inner-being state | core | COMPLETE | DB·AV·R2g·R1 | — | — | no "guilt" sibling cluster; M03 (pu.qah) |
| 18 | Iniquity as accumulated moral crime | core | COMPLETE | DB·AV | — | — | accumulation = data-shape |
| 19 | Transgression as boundary-crossing | core | COMPLETE | DB·PE·R2p·R1 | — | — | status/action split (§10) |
| 20 | Faithlessness as covenant-breaking | core | COMPLETE | DB·R1 | — | — | M13/M31 home call |
| 21 | Perversion as inner inversion | core | COMPLETE | DB·R1·R2p·R3 | — | — | R3 heterogeneous; cha.val re-gloss |
| 22 | Injustice as moral failure | core | COMPLETE | DB·R2p | — | — | M26 home call |
| 23 | Wickedness as settled person-identity | wick | COMPLETE | DB·B1·Bsum | — | — | re'sha ownership; pair w/ #16 |
| 24 | Evil as constitutional inner nature | wick | COMPLETE | DB·B4·B5·Bsum | — | — | "the evil one" object-kind (§10) |
| 25 | Abomination — divine revulsion | wick | COMPLETE | DB·B2·Bsum | — | — | #25 vs #26 split; defilement bridge |
| 26 | Idolatrous abomination | wick | COMPLETE | DB·B2·Bsum | — | — | moral-vs-idolatrous split |
| 27 | Iniquity as active inner scheming | wick | COMPLETE | DB·B3·Bsum | — | — | clearest lifecycle — §10 test case |
| 28 | Evil expressed through speech | wick | COMPLETE | DB·B5·B4·Bsum | — | — | reconcile w/ #9 (noun) |
| 29 | Ritual defilement-state | defi | COMPLETE | DB·MC | — | — | ritual STATE (neutral valence) |
| 30 | Moral-inner defilement-state | defi | COMPLETE | DB·MC | — | — | inner-moral core; link #12 |
| 31 | Corporate/covenantal defilement | defi | COMPLETE | DB·MC | — | — | corporate = data-shape |
| 32 | Defilement by external spiritual agency | defi | COMPLETE | DB·MC (+#108) | — | — | external-agent object-kind (§10) |

## Cross-cluster bonds (where each unit is ALSO dealt with elsewhere)
> Signals (script `scripts/_check_m10_cross_cluster_bonds_20260623.py`, read-only): **Bonds (co-occurrence)** = how many of the unit's verses also contain a term *owned by* another cluster (the real bond). **XREF-adds** = extra clusters via an XREF copy (thin — all sin-terms are M10-owned). A bond means the unit *engages* another cluster (≠ the "home-call" remapping flags in the gap column).

| # | Unit | Bonds — co-occurrence | XREF-adds |
|---|---|---|---|
| 1 | Wilful sinning | M26(31)·M11(18)·M12(17)·M38(16) | M35 |
| 2 | Unintentional sinning | M26(21)·M12(17)·M47(13)·M11(13) | M35 |
| 3 | Confession | M26(26)·M12(17)·M11(16)·M47(14) | M35 |
| 4 | Conscience suppression | M26(26)·M12(17)·M11(16)·M47(14) | M35 |
| 5 | Refusal to repent | M11(40)·M26(40)·M41(27)·M38(26) | M35 |
| 6 | Habitual defection | M26(26)·M12(17)·M11(16)·M47(14) | M35 |
| 7 | Contagious sin | M26(21)·M12(17)·M47(13)·M11(13) | M35 |
| 8 | Political revolt | M23(7)·M11(4)·M41(4)·M47(3) | M30 |
| 9 | Sinful speech | M11(4)·M15(4)·M08(3)·M28(3) | — |
| 10 | Specialised sinful mechanisms | M28(3)·M35(1)·M47(1)·M15(1) | — |
| 11 | Sin as universal condition | M11(59)·M26(39)·M38(27)·M23(26) | M30,M35 |
| 12 | Sin as enslaving power | M11(33)·M26(20)·M23(15)·M39(9) | M35 |
| 13 | Sin as divine record | M11(70)·M26(51)·M38(33)·M47(31) | M35 |
| 14 | Forgiveness sought and received | M11(83)·M38(51)·M26(35)·M23(23) | M35 |
| 15 | Generational sin | M26(21)·M12(17)·M47(13)·M11(13) | M35 |
| 16 | The sinner as moral character | M26(12)·M05(7)·M37(4)·M45(4) | M35 |
| 17 | Guilt as inner-being state | M41(10)·M23(8)·M26(7)·M25(7) | — |
| 18 | Iniquity as accumulated moral crime | M41(17)·M47(15)·M11(13)·M15(10) | M26,M35 |
| 19 | Transgression as boundary-crossing | M23(20)·M26(18)·M45(14)·M41(13) | M30 |
| 20 | Faithlessness as covenant-breaking | M26(10)·M41(9)·M30(8)·M23(7) | M14 |
| 21 | Perversion as inner inversion | M26(13)·M15(10)·M47(8)·M13(5) | M03 |
| 22 | Injustice as moral failure | M26(19)·M13(9)·M41(6)·M45(6) | M30 |
| 23 | Wickedness as settled person-identity | M26(81)·M47(16)·M02(14)·M06(14) | M03,M24,M27,M30 |
| 24 | Evil as constitutional inner nature | M05(15)·M47(8)·M13(7)·M23(7) | M06,M26,M30 |
| 25 | Abomination — divine revulsion | M13(7)·M47(7)·M30(6)·M28(6) | — |
| 26 | Idolatrous abomination | M30(9)·M47(8)·M28(8)·M13(7) | — |
| 27 | Iniquity as active inner scheming | M14(11)·M47(9)·M15(8)·M30(7) | M03,M06,M24,M26,M27 |
| 28 | Evil expressed through speech | M05(5)·M42(2)·M26(2)·M23(2) | M14 |
| 29 | Ritual defilement-state | M12(29)·M25(23)·M28(9)·M23(8) | — |
| 30 | Moral-inner defilement-state | M25(19)·M12(14)·M23(9)·M28(9) | — |
| 31 | Corporate/covenantal defilement | M12(29)·M28(8)·M25(7)·M47(7) | — |
| 32 | Defilement by external spiritual agency | M25(16)·M23(6)·M24(2)·M04(1) | — |

**Cluster legend:** M02 Anger · M03 Grief · M04 Joy · M05 Love/Compassion · M06 Hate · M08 Pride · M11 Repentance/Forgiveness · M12 Purity · M13 Truth/Faithfulness · M14 Deceit/Hypocrisy · M15 Wisdom · M23 Strength/Power · M24 Weakness/Suffering · M25 Life · M26 Righteousness/Justice · **M27 Evil/Wickedness/Abomination** · M28 Envy/Greed/Lust · M30 Obedience/Disobedience · M35 Testing/Temptation · M37 Calling · M38 Salvation · M39 Blessing/Grace · M41 Remembrance · M42 Speech · M45 Transformation · M47 Constitution (inner-being seats).

**Bond highlights (held open):** **M26 Righteousness** = pervasive antithesis (peaks #23, 81); **M11 + M38 + M12** = the remedy/atonement web (peaks #14 — corroborates exploration Thread 1); **M12 Purity** = the structural opposite for all defilement units (#29/#31); **M47 Constitution** = where sin touches the inner being; **M41 Remembrance** = guilt/record units. **⚠ M27 "Evil, Wickedness and Abomination"** = the **characteristic-view** counterpart of the wickedness units (#23–28) per the dual-view reflection (not a duplication).

## Status roll-up (2026-06-23, post-merge + post-evidence)
- **(A) Evidence: COMPLETE 32/32.** Evidence-gathering for the cluster is COMPLETE.
- **(B) Synthesis: NOT STARTED 32/32** (gated behind §10).
- **Residual (not lexical gaps):** (i) data-shape items needing a verse-narrative pass (#6,#7,#15,#31); (ii) home-calls for conceptually-shared units (#9/#20/#22/#10/#14 → M06/M13/M31/M26/M11; defilement → opposite M12); (iii) hygiene flags (cha.val re-gloss; valence over-tag on political-revolt & sin-offering; M10c pneuma = unclean-spirit-agent not a seat; hamart- volition tag).
- **OPEN exploration threads (researcher-led, evidence layer):** atonement (Thread 1), a.von-as-process, pešaʿ split, hamart deepening — see `…-exploration-threads…`.
- **NEXT GATE:** §10 — define characteristic vs status vs other-object/hybrid (now informed by the dual-view reflection + concrete test cases). No (B) synthesis until passed.

*Living document — on completing any evidence/synthesis file, record its filename in the unit row and flip the status. Numbering is the single 1–32 (see unit index).*
