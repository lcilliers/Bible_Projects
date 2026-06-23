# WA M10-family — Logical-units gap register (living tracker)

- **File:** wa-m10-family-logical-units-gap-register-v1-20260623.md · **Version:** v1 · **Date:** 2026-06-23 · **Author:** Claude Code.
- **Purpose:** the **living tracker** for the 32 M10-family units across two phases — **(A) evidence-gathering** and **(B) by-unit synthesis** — recording, per unit, the **actual files** that hold its evidence and (later) its synthesis. **Update protocol:** when an evidence or synthesis file is completed for a unit, **add its filename and flip the status column**. This lets the researcher monitor progress and review by file. Detail per unit: the ledger (`…-ledger-v1-20260623.md`).

## Phase model (per unit)
```
(A) EVIDENCE-GATHERING ──▶ [GATE §10: define characteristic vs status vs other] ──▶ (B) BY-UNIT SYNTHESIS
```
- **(A) statuses:** `COMPLETE` (freshly read, neutral method, + DB) · `RINGS` (terms freshly read in the M10 rings) · `PARTIAL` (some terms read; core terms not) · `DB-ONLY` (only the prior l2_meaning layer; core not re-read) · `SCRATCH` (only wrong-format scratch reads).
- **GATE:** the pre-synthesis exploration (framework §10) — *what is a characteristic, a status, an other-object, a hybrid?* No unit enters (B) before this is settled.
- **(B) statuses:** `NOT STARTED` for all until the gate is passed.

## Evidence-file legend (short code → file in `Sessions-v2/M10-Sin/findings/`)
| Code | File(s) |
|---|---|
| **DB** | `finding` table, level=VERSE, provenance=`l2_meaning` (not a file) — the prior per-verse layer |
| **R1** | `wa-m10-ring1-evidence-v1_1-20260621.json` (+ `-digest-v1_0`, `-gapaudit-v1_0`) |
| **R2g** | `wa-m10-ring2-guilt-evidence-v1_0-20260621.json` (+ `-digest-v1_0`) |
| **R2p** | `wa-m10-ring2-parts2to5-evidence-v1_0-20260621.json` (+ `wa-m10-ring2-close-evidence-digest-v1_0-20260621.md`) |
| **R3** | `wa-m10-ring3-evidence-v1_0-20260621.json` (+ `-digest-v1_0`) |
| **R4** | `wa-m10-ring4-evidence-v1_0-20260621.json` (+ `-digest-v1_0`) |
| **B1** | `wa-m10b-b1-rasha-sp1..sp5recovered-evidence-v1_0-20260622.json` (+ digests) · `wa-m10b-b1-resha-mirshaat-evidence-v1_0-20260622.json` · `wa-m10b-b1-audit-evidence-digest-v1_0-20260622.md` |
| **B2** | `wa-m10b-b2-toevah-sp1law..sp4rem-evidence-v1_0-20260622.json` · `wa-m10b-b2-shiqquts-bdel-evidence-v1_0-20260622.json` · `wa-m10b-b2-audit-evidence-digest-v1_0-20260622.md` |
| **B3** | `wa-m10b-b3-aven-sp1psa..sp3isa-evidence-v1_0-20260622.json` · `wa-m10b-b3-roa-evidence-v1_0-20260622.json` · `wa-m10b-b3-audit-evidence-digest-v1_0-20260622.md` |
| **B4** | `wa-m10b-b4-poneros-evidence-v1_0-20260622.json` · `wa-m10b-b4-kakia-evidence-v1_0-20260622.json` · `wa-m10b-b4-audit-evidence-digest-v1_0-20260622.md` |
| **B5** | `wa-m10b-b5-blasf-adikia-evidence-v1_0-20260622.json` |
| **Bsum** | `wa-m10b-complete-summary-evidence-digest-v1_0-20260622.md` (M10b overview) |
| **Pn** | `wa-m10-perverse-niddah-v1_0-20260622.md` — **SCRATCH** (wrong format) |
| **Pd** | `wa-m10-perverse-nt-defilement-v1_0-20260622.md` — **SCRATCH** (wrong format) |
| **HA** | `wa-m10-core-hata-evidence-digest-v1_0-20260623.md` (ḥāṭāʾ family; + `…-hata-assembly-…json`) — CORE read 2026-06-23 |
| **AV** | `wa-m10-core-avon-evidence-digest-v1_0-20260623.md` (a.von; + assembly) — CORE read 2026-06-23 |
| **PE** | `wa-m10-core-pesha-evidence-digest-v1_0-20260623.md` (pe.sha+pa.sha; + assembly) — CORE read 2026-06-23 |
| **HM** | `wa-m10-core-hamart-evidence-digest-v1_0-20260623.md` (NT hamart-; + assembly) — CORE read 2026-06-23 |
| **MC** | `wa-m10-core-m10c-evidence-digest-v1_0-20260623.md` (M10c defilement, 4 mechanisms; + assembly) — clean read 2026-06-23 (supersedes scratch Pn/Pd) |

## Programme-level gaps (the big rocks)
1. **M10 CORE not re-read** (13 lemmas, ~1,072 occ: ḥāṭāʾ family, a'von, pe'sha, hamart-) — the definitional pillar; blocks every core-anchored unit. **Top priority.**
2. **M10c not properly read** (~263 occ) — only scratch (Pn/Pd); redo clean. **Second priority.**
3. **GATE §10 unresolved** — characteristic/status/other definition. **Blocks all synthesis.**
4. **Two flagged recodes** (framework §6): session-B findings #167 (vulnerability), #1098/#1129 (goodness) — researcher to assign a home.
5. **Co-seated seating index** not yet built clean across the whole unit.

---

## Tracker — M10 Sin, Guilt, Transgression
| # | Unit | (A) | Evidence file(s) | (B) | Synthesis file(s) | Key remaining gap |
|---|---|---|---|---|---|---|
| 1 | Wilful sinning | COMPLETE | DB, HA, HM, R2p | NOT STARTED | — | intent-marker per-occurrence (lexical read done) |
| 2 | Unintentional sinning | COMPLETE | DB, HA | NOT STARTED | — | intent/awareness distinction (Lev "if anyone sins" read) |
| 3 | Confession | COMPLETE | DB, HA, HM | NOT STARTED | — | shared w/ M11 (home call) |
| 4 | Conscience suppression | COMPLETE | DB, HA, HM | NOT STARTED | — | conscience-seat thin (read confirms) |
| 5 | Refusal to repent | COMPLETE | DB, HA, HM | NOT STARTED | — | M11 seam |
| 6 | Habitual defection | COMPLETE | DB, HA, HM | NOT STARTED | — | over-time = data-shape (narrative read still owed) |
| 7 | Contagious sin | COMPLETE | DB, HA | NOT STARTED | — | relational transmission = data-shape |
| 8 | Political revolt | COMPLETE | DB, PE | NOT STARTED | — | political vs God-ward rebellion split (§10) |
| 9 | Sinful speech | COMPLETE | DB, R2p | NOT STARTED | — | reconcile w/ M10b #6 (verb); M06 |
| 10 | Specialised mechanisms | COMPLETE | DB, R1 | NOT STARTED | — | tiny corpus; M14/M08/M31 home calls |
| 11 | Sin as universal condition | COMPLETE | DB, HM, HA, R2p | NOT STARTED | — | status-candidate flagship |
| 12 | Sin as enslaving power | COMPLETE | DB, HM | NOT STARTED | — | Romans dominion register read (HM face a) |
| 13 | Sin as divine record | COMPLETE | DB, HA, AV | NOT STARTED | — | largest DB (528); written/recorded register read |
| 14 | Forgiveness sought/received | COMPLETE | DB, HA, HM, R4 | NOT STARTED | — | chat.tat sin-offering + kip.pu.rim read; split w/ M11 |
| 15 | Generational sin | COMPLETE | DB, HA, AV | NOT STARTED | — | lineage/visiting-iniquity read; over-time = data-shape |
| 16 | The sinner as moral character | COMPLETE | DB, HM, HA | NOT STARTED | — | pair w/ M10b #1 (hamartōlos/chat.ta read) |
| 17 | Guilt as inner-being state | COMPLETE | DB, AV, R2g, R1 | NOT STARTED | — | a'von guilt-sense read; M03 (pu.qah) |
| 18 | Iniquity as accumulated crime | COMPLETE | DB, AV | NOT STARTED | — | accumulation/measure register read; data-shape tail |
| 19 | Transgression boundary-crossing | COMPLETE | DB, PE, R2p, R1 | NOT STARTED | — | pe'sha/pa'sha read; status/action split (§10) |
| 20 | Faithlessness | COMPLETE | DB, R1 | NOT STARTED | — | M13/M31 home call |
| 21 | Perversion as inner inversion | COMPLETE | DB, R1, R2p, R3 | NOT STARTED | — | R3 heterogeneous; cha.val re-gloss; M03/M07/M23/M35 |
| 22 | Injustice | COMPLETE | DB, R2p | NOT STARTED | — | M26 home call |

## Tracker — M10b Wickedness, Evil, Abomination
| # | Unit | (A) | Evidence file(s) | (B) | Synthesis file(s) | Key remaining gap |
|---|---|---|---|---|---|---|
| 1 | Wickedness as person-identity | COMPLETE | DB, B1, Bsum | NOT STARTED | — | re'sha ownership; pair w/ M10 #16 |
| 2 | Evil as constitutional nature | COMPLETE | DB, B4, B5, Bsum | NOT STARTED | — | "the evil one" object-kind (§10) |
| 3 | Abomination — divine revulsion | COMPLETE | DB, B2, Bsum | NOT STARTED | — | #3 vs #4 split; M10c bridge |
| 4 | Idolatrous abomination | COMPLETE | DB, B2, Bsum | NOT STARTED | — | moral-vs-idolatrous split |
| 5 | Iniquity as active scheming | COMPLETE | DB, B3, Bsum | NOT STARTED | — | clearest lifecycle — key §10 test case |
| 6 | Evil expressed through speech | COMPLETE | DB, B5, B4, Bsum | NOT STARTED | — | reconcile w/ M10 #9 (noun) |

## Tracker — M10c Defilement, Impurity
| # | Unit | (A) | Evidence file(s) | (B) | Synthesis file(s) | Key remaining gap |
|---|---|---|---|---|---|---|
| 1 | Ritual defilement-state | COMPLETE | DB, MC | NOT STARTED | — | ritual STATE (neutral valence); ta.me verb/adj split read |
| 2 | Moral-inner defilement-state | COMPLETE | DB, MC | NOT STARTED | — | inner-moral core read (sarx/kardia/conscience seats); link M10 #12 |
| 3 | Corporate/covenantal defilement | COMPLETE | DB, MC | NOT STARTED | — | corporate read; data-shape tail; M10b bridge |
| 4 | Defilement by external agency | COMPLETE | DB, MC (+ finding #108) | NOT STARTED | — | external-agent object-kind (§10 test case) |

---

## Cross-cluster bonds (where each unit is ALSO dealt with elsewhere)

> Two factual signals (script: `scripts/_check_m10_cross_cluster_bonds_20260623.py`, read-only — re-run to refresh):
> - **Bonds (co-occurrence) — primary:** the count = how many of the unit's verses also contain a term *owned by* another cluster. This is the real "bonds with" signal (the unit's content shares scriptural ground with that cluster).
> - **XREF-adds (term-architecture):** extra clusters reached via an XREF copy of the unit's Strong's in a non-family registry. Thin by design — every sin-term is M10-family-**owned**, so XREF rarely crosses clusters; shown only where it adds a cluster the co-occurrence missed.
> Distinct from the "home-call" flags in the gap column (which are about *remapping* a term): a **bond** means the unit *engages* another cluster, not that it should move there.

| Unit | Bonds — co-occurrence (verses shared) | XREF-adds |
|---|---|---|
| **M10 #1** Wilful sinning | M26(31) · M11(18) · M12(17) · M38(16) | M35 |
| **M10 #2** Unintentional sinning | M26(21) · M12(17) · M47(13) · M11(13) | M35 |
| **M10 #3** Confession | M26(26) · M12(17) · M11(16) · M47(14) | M35 |
| **M10 #4** Conscience suppression | M26(26) · M12(17) · M11(16) · M47(14) | M35 |
| **M10 #5** Refusal to repent | M11(40) · M26(40) · M41(27) · M38(26) | M35 |
| **M10 #6** Habitual defection | M26(26) · M12(17) · M11(16) · M47(14) | M35 |
| **M10 #7** Contagious sin | M26(21) · M12(17) · M47(13) · M11(13) | M35 |
| **M10 #8** Political revolt | M23(7) · M11(4) · M41(4) · M47(3) | M30 |
| **M10 #9** Sinful speech | M11(4) · M15(4) · M08(3) · M28(3) | — |
| **M10 #10** Specialised sinful mechanisms | M28(3) · M35(1) · M47(1) · M15(1) | — |
| **M10 #11** Sin as universal condition | M11(59) · M26(39) · M38(27) · M23(26) | M30, M35 |
| **M10 #12** Sin as enslaving power | M11(33) · M26(20) · M23(15) · M39(9) | M35 |
| **M10 #13** Sin as divine record | M11(70) · M26(51) · M38(33) · M47(31) | M35 |
| **M10 #14** Forgiveness sought and received | M11(83) · M38(51) · M26(35) · M23(23) | M35 |
| **M10 #15** Generational sin | M26(21) · M12(17) · M47(13) · M11(13) | M35 |
| **M10 #16** The sinner as moral character | M26(12) · M05(7) · M37(4) · M45(4) | M35 |
| **M10 #17** Guilt as inner-being state | M41(10) · M23(8) · M26(7) · M25(7) | — |
| **M10 #18** Iniquity as accumulated moral crime | M41(17) · M47(15) · M11(13) · M15(10) | M26, M35 |
| **M10 #19** Transgression as boundary-crossing | M23(20) · M26(18) · M45(14) · M41(13) | M30 |
| **M10 #20** Faithlessness as covenant-breaking | M26(10) · M41(9) · M30(8) · M23(7) | M14 |
| **M10 #21** Perversion as inner inversion | M26(13) · M15(10) · M47(8) · M13(5) | M03 |
| **M10 #22** Injustice as moral failure | M26(19) · M13(9) · M41(6) · M45(6) | M30 |
| **M10b #1** Wickedness as settled person-identity | M26(81) · M47(16) · M02(14) · M06(14) | M03, M24, M27, M30 |
| **M10b #2** Evil as constitutional inner nature | M05(15) · M47(8) · M13(7) · M23(7) | M06, M26, M30 |
| **M10b #3** Abomination — divine revulsion | M13(7) · M47(7) · M30(6) · M28(6) | — |
| **M10b #4** Idolatrous abomination | M30(9) · M47(8) · M28(8) · M13(7) | — |
| **M10b #5** Iniquity as active inner scheming | M14(11) · M47(9) · M15(8) · M30(7) | M03, M06, M24, M26, M27 |
| **M10b #6** Evil expressed through speech | M05(5) · M42(2) · M26(2) · M23(2) | M14 |
| **M10c #1** Ritual defilement-state | M12(29) · M25(23) · M28(9) · M23(8) | — |
| **M10c #2** Moral-inner defilement-state | M25(19) · M12(14) · M23(9) · M28(9) | — |
| **M10c #3** Corporate/covenantal defilement | M12(29) · M28(8) · M25(7) · M47(7) | — |
| **M10c #4** Defilement by external spiritual agency | M25(16) · M23(6) · M24(2) · M04(1) | — |

**Cluster legend:** M02 Anger · M03 Grief · M04 Joy · M05 Love/Compassion/Kindness · M06 Hate/Contempt · M08 Pride · M11 Repentance/Forgiveness/Restoration · M12 Purity/Holiness/Consecration · M13 Truth/Faithfulness/Integrity · M14 Deceit/Hypocrisy/Falsehood · M15 Wisdom/Understanding/Knowledge · M23 Strength/Power/Dominion · M24 Weakness/Vulnerability/Suffering · M25 Life/Vitality/Existence · M26 Righteousness/Justice · **M27 Evil, Wickedness and Abomination** · M28 Envy/Greed/Lust · M30 Obedience/Disobedience · M35 Testing/Temptation/Trial · M37 Calling/Election/Vocation · M38 Salvation/Redemption/Deliverance · M39 Blessing/Favour/Grace · M41 Remembrance/Memory · M42 Speech/Voice/Cry · M45 Transformation/Renewal · M47 Constitution (inner-being seats).

**What the bonds show (held open — for synthesis, not decided here):**
- **M26 (Righteousness/Justice) — the pervasive antithesis** across M10 and especially **M10b #1 wickedness (81)**; sin is read against righteousness everywhere.
- **M11 (Repentance/Forgiveness/Restoration) — the remedy/turning bond**, strongest on the **atonement/forgiveness units (#14: M11 83, M38 51)** and the status/record units (#13 M11 70). This corroborates **exploration Thread 1 (atonement)**: the dealing-with-sin mechanism reaches into M11 + **M38 (Salvation)** + **M12 (Purity)**.
- **M12 (Purity) — the structural opposite, dominant for M10c defilement** (#1/#3 = M12 29 each), exactly as the unit definitions flag.
- **M47 (Constitution/seats) — where sin touches the inner being** (recurs across most units; consistent with the bounded co-seated evidence).
- **M41 (Remembrance) — for guilt/iniquity/record units** (#17/#18/#13) — sin as remembered/borne over time.
- **⚠ M27 "Evil, Wickedness and Abomination"** has a name nearly identical to **M10b "Wickedness, Evil and Abomination"** and bonds to M10b #1/#5 via XREF — possible **overlap/duplication** between M10b and M27 to investigate (flag, not resolved).

## Status roll-up (2026-06-23, after the M10 CORE + M10c reads)
- **(A) Evidence: COMPLETE 32/32** — all M10 ×22 + M10b ×6 + M10c ×4 freshly read under the neutral method. **Evidence-gathering for the family is COMPLETE.**
- **(B) Synthesis:** NOT STARTED 32/32 (gated behind §10).
- **Residual within the COMPLETE units (NOT lexical gaps — different kinds, handled at/with synthesis):**
  - (i) **data-shape** items needing a verse-narrative pass, not more lexical reading (over-time #M10-6, lineage #M10-15, transmission #M10-7, corporate #M10c-3).
  - (ii) **home calls** for conceptually-shared units (M10 #9/#20/#22/#10/#14 → M06/M13/M31/M26/M11; M10c all → opposite M12) — a §10/synthesis decision.
  - (iii) flagged hygiene items: cha.val re-gloss; valence over-tag (political-revolt pešaʿ; chat.tat sin-offering; M10c neutral ritual-state is correct); the M10c **pneuma = unclean-spirit-agent** caution (not an inner seat); hamart- **volition** faculty tag (cross-language).
- **NEXT (the gate):** the **§10 definitional exploration** — *what is a characteristic vs a status vs an other-object/hybrid?* Now armed with concrete test cases from the evidence: chat.tat's sin/sin-offering seam · a.von's crime/guilt/punishment tri-fold · pešaʿ status/action split · hamart- `volition` tag · M10c's ritual-state and external-agency object-kinds. **No (B) synthesis until this gate is passed.**

*Living document — on completion of any evidence or synthesis file, record its filename in the relevant unit row and update the status column.*
