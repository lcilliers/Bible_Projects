# Data Validity Checking — Status as of 2026-04-23

**Question asked:** how far have we got checking the validity of the data in the database?

**Short answer:** several layers, at very different levels of coverage. Mechanical checks are at 100 %; the deeper readiness sweep is at about 6 % piloted.

---

## 1. Engine audit (WR-01 … WR-20)

The per-word audit embedded in `engine/audit.py`, run automatically by `--mode=audit_word`, checks 20 structural invariants (file index present, terms present, all Strong's in `mti_terms`, verse/occurrence ratio, meaning populated, transliteration, language, span back-population, etc.) and returns PASS / REVIEW / STOP.

| Metric | Count |
|---|---:|
| Total registries | 214 |
| Non-excluded registries | 184 |
| Registries that have a successful AUDIT_WORD run | 184 |
| Latest outcome distribution | `COMPLETE: 184` |
| Registries never AUDIT_WORD'd | 30 (all Phase 1 `Excluded`) |
| Total AUDIT_WORD runs logged | 415 |
| Latest AUDIT_WORD run | 2026-04-13 |

**Verdict:** 100 % coverage on all relevant registries. All completed. This is the baseline check — it confirms structural integrity of terms, verses, spans, meanings, flags.

---

## 2. Data-quality flags (informational)

`wa_data_quality_flags` holds the informational flags derived by `engine/flag_engine.py`. Post-M29 these are advisory-only (no gating).

| Flag code | Rows |
|---|---:|
| NO_WORD_ANALYSIS | 7,492 |
| PROSE_ONLY_MEANING | 5,640 |
| VERSE_EVIDENCE_CONCENTRATED | 5,060 |
| VERSE_EVIDENCE_MINIMAL | 513 |
| CONCRETE_PHYSICAL | 315 |
| VERSE_EVIDENCE_HIGH | 278 |
| **Total** | **19,298** |

| Metric | Count |
|---|---:|
| Registries with at least one quality flag | 182 |

**Verdict:** every non-excluded registry has been through flag derivation. These flags feed the readiness-sweep investigation (see §5) — they are inputs to validity checking, not results.

---

## 3. Session research flags (open work items)

`wa_session_research_flags` tracks investigation items raised during research. These are not automated validity checks — they are researcher-observed items needing analytical follow-up.

| Flag code | Rows | Registries |
|---|---:|---:|
| SD_POINTER | 247 | 60 |
| VERSE_EVIDENCE_BREADTH_NOTE | 52 | 19 |
| PH2_DATA_ERROR | 11 | 9 |
| DIMREVIEW_SESSION_D | 8 | 7 |
| PH2_CROSS_REGISTRY_REQUIRED | 7 | 5 |
| PH2_CROSS_REF_ENRICHMENT | 6 | 2 |
| PH2_THEOLOGICAL_DEPTH_REQUIRED | 4 | 3 |
| PH2_DATA_QUALITY | 3 | 2 |
| (other) | 7 | various |
| **Total** | **345 open** | — |

All 345 are `resolved = 0`. None closed yet.

---

## 4. Pipeline status (current programme gating)

| Phase | Status | Count |
|---|---|---:|
| Phase 1 | Complete | 182 |
| | Excluded | 30 |
| | In Progress | 2 (grace 68, suffering 214) |
| Verse Context | Complete | 180 |
| | In Progress | 2 |
| | NULL | 32 |
| Session B | **Verse Context Reset** | **182** |
| | Ready for Analysis | 2 |
| | NULL | 30 |

**Verdict:** the programme has deliberately reset all 182 completed registries to `Verse Context Reset` (per 2026-04-19 Q12 decision noted in `CLAUDE.md` §10). The plan is to re-run VC, dimension review, readiness, then Session B under the current instruction set. No word has yet returned to `Pre-Analysis Complete` under the reset framework.

---

## 5. Readiness sweep (deepest validity check)

The readiness sweep — specified in [wa-global-readiness-sweep-design-v1-20260419.md](wa-global-readiness-sweep-design-v1-20260419.md) — is the programme-level validity pass: term coverage, verse completeness, meaning quality, lexical-layer consistency, evidence-flag appropriateness, dimension placement, cross-registry consistency. It is the check that answers "is this word analysis ready for Session B?"

| Registry | Piloted | Completed |
|---|:---:|:---:|
| 001 abomination | ✓ | |
| 018 brokenness | ✓ | |
| 035 covetousness | ✓ | ✓ |
| 062 fellowship | ✓ | ✓ |
| 068 grace | ✓ | ✓ |
| 134 renewal | ✓ | ✓ |
| 182 Soul | ✓ | |
| 184 spirit | ✓ | |
| 206 vulnerability | ✓ | ✓ |
| 207 blindness (spiritual) | ✓ | ✓ |
| 214 suffering | ✓ | |

| Metric | Count |
|---|---:|
| Non-excluded registries | 182 |
| Piloted | 11 (6 %) |
| With completion report | 6 (3 %) |
| Remaining | 176 piloted-to-do |

**Verdict:** this is the layer where the programme has furthest to go. The design is in place; 11 words have been run through pilots; 6 have been formally closed on scorecard v2 as `BANKED` (covetousness, fellowship, renewal, vulnerability, blindness, plus grace per memory). The remaining 176 non-excluded registries still need the full sweep.

The task-ledger item `Phase_B_Analysis_Readiness: Run all words through readiness` in `tasks.md` tracks this.

---

## 6. Database review items (DBR)

Separate from the flag tables, the DB-wide review raised findings tracked as **OT-DBR-NNN** (observed tasks, database review). Per `CLAUDE.md` §10:

- OT-DBR-001 / 002 — **Resolved** 2026-04-19 (audit_word + audit.py rewritten for post-DBR schema).
- OT-DBR-009 — **Open HIGH** (mti_terms dedup; designed as Action R, awaiting approval).
- OT-DBR-015 / 016 — dimension review vocabulary vintage + rootfamily cross-registry over-reporting (per memory file; check current state if acting).

---

## Summary of coverage by layer

| Layer | Coverage |
|---|---|
| Engine structural audit (WR-01…WR-20) | 100 % of 184 non-excluded |
| Data-quality flag derivation | 100 % of 182 non-excluded |
| Session research flags raised | 345 open items, 60 registries involved |
| Pipeline gating (Session B status) | 182 at Verse Context Reset awaiting re-run |
| Readiness sweep (deepest check) | 11 of 182 piloted (6 %), 6 formally BANKED |
| DB-wide review (OT-DBR) | 2 resolved, 1 open HIGH, others tracked externally |

---

*Report produced 2026-04-23 in response to the question of data-validity progress.*
