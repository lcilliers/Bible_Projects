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

## Status roll-up (2026-06-23, after the M10 CORE + M10c reads)
- **(A) Evidence: COMPLETE 32/32** — all M10 ×22 + M10b ×6 + M10c ×4 freshly read under the neutral method. **Evidence-gathering for the family is COMPLETE.**
- **(B) Synthesis:** NOT STARTED 32/32 (gated behind §10).
- **Residual within the COMPLETE units (NOT lexical gaps — different kinds, handled at/with synthesis):**
  - (i) **data-shape** items needing a verse-narrative pass, not more lexical reading (over-time #M10-6, lineage #M10-15, transmission #M10-7, corporate #M10c-3).
  - (ii) **home calls** for conceptually-shared units (M10 #9/#20/#22/#10/#14 → M06/M13/M31/M26/M11; M10c all → opposite M12) — a §10/synthesis decision.
  - (iii) flagged hygiene items: cha.val re-gloss; valence over-tag (political-revolt pešaʿ; chat.tat sin-offering; M10c neutral ritual-state is correct); the M10c **pneuma = unclean-spirit-agent** caution (not an inner seat); hamart- **volition** faculty tag (cross-language).
- **NEXT (the gate):** the **§10 definitional exploration** — *what is a characteristic vs a status vs an other-object/hybrid?* Now armed with concrete test cases from the evidence: chat.tat's sin/sin-offering seam · a.von's crime/guilt/punishment tri-fold · pešaʿ status/action split · hamart- `volition` tag · M10c's ritual-state and external-agency object-kinds. **No (B) synthesis until this gate is passed.**

*Living document — on completion of any evidence or synthesis file, record its filename in the relevant unit row and update the status column.*
