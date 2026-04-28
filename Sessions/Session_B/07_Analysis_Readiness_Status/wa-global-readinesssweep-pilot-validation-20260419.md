# Readiness Sweep Pilot — Validation Report — 2026-04-19

| Field | Value |
|---|---|
| Filename | wa-global-readinesssweep-pilot-validation-20260419.md |
| Purpose | Validate `wa-global-readiness-sweep-instruction-v1_0-20260419.md` phases R.A–R.H against live post-DBR schema using a sample of 3 diverse registries |
| Produced | 2026-04-19 |
| Pilot script | `scripts/readiness_sweep_pilot.py` (new — read-only implementation) |
| Mode | **Read-only** — no patches applied; no DB writes |
| Status | **VALIDATION PASS** — sweep instruction is executable |

---

## Summary

Three registries run through phases R.A–R.H with contrasting states:

| Registry | State | Path 1 | Path 2 | Path 3 | Path 4 | Path 5 | Total |
|---|---|---|---|---|---|---|---|
| r62 fellowship | reset-from-complete (1 of the 6 Q12 reset) | 0 | 0 | 1 | 0 | 1 | **2** |
| r1 abomination | VC Complete, dim_review=None, many term issues | 7 | 16 | 1 | 44 | 1 | **69** |
| r214 suffering | VC In Progress, new large word | 0 | 0 | 1 | 15 | 1 | **17** |

**Key observations:**

- **r62 (fellowship)** — clean as expected. It was Analysis Complete; data holds up after DBR reset. Only finding is Session A extract not yet generated (Path 5) + word_synopsis NULL (Path 3 — researcher authors). Confirms the 6-word Q12 reset did not corrupt structural data.
- **r1 (abomination)** — highly active. 14 span filter failures / zero-extraction cases (`H0873`, `H0889`, `H0891`, `G5087` with 85 span matches all deleted etc.), 1 NULL dimension, 26 groups at non-reviewed confidence (consistent with `dim_review_status = None`). **Path 2 items are execution-blocked pending OT-DBR-001 (audit_word.py rewrite).**
- **r214 (suffering)** — VC in progress. Path 4 items dominated (15 RD items) — likely NULL `dominant_subject` across groups + group description gaps. No span filter failures surface yet because VC is still in progress.

---

## Post-DBR Schema Compatibility — CONFIRMED

Every pilot query relies on the new schema shape:

| Query area | Post-DBR adaptation | Pilot outcome |
|---|---|---|
| R.B term checks | `mti_term_flags` joins for god/somatic flags (not direct column reads) | PASS — 4 god flags, 1 somatic on r1; 0 on r62; counts reflect post-M23 population |
| R.B three-number diagnostic | Still works — `span_strong_match` column retained | PASS — 14 failures detected on r1 |
| R.E dimension checks | Joins through `verse_context_group` and `mti_terms` for dropped columns | PASS — 26 rows retrieved on r1; 19 on r62 |
| R.H prose coverage | `prose_section` + `prose_section_type` joined | PASS — tables present, 0 rows for all test registries (expected — no Session A extracts yet) |
| `word_synopsis` column | Read from `word_registry` | PASS — column present; NULL for all 3 (expected — researcher-authored) |

---

## Findings by Path — Interpretation

### Path 1 (mechanical patch candidates)

r1 alone produced 7 Path 1 items. Pattern shows:

- XREF terms with `mti_terms.status = NULL` (need `xref_[word]`) — repeated for same term_inv_id=4658 across multiple file rows. (**Pilot bug noted below:** deduplication needed.)
- SMALL_VERSE_SAMPLE flag gaps (inferred from thin-sample terms lacking the quality flag)

### Path 2 (sub-process directives — currently BLOCKED by OT-DBR-001)

r1: 14 term-level Path 2 items for span filter failure / zero extraction + 2 dimension-level (NULL dimension, AUTOMATED confidence).

These are **legitimate re-extraction candidates** but cannot execute until `engine/audit_word.py` is rewritten for `mti_term_flags` joins. Sweep correctly marks each with "BLOCKED: OT-DBR-001" annotation.

### Path 3 (deferred to per-word Stage 1)

Consistently surfaces `word_synopsis NULL` per registry — this is **expected behaviour** — researcher authors these.

### Path 4 (RESEARCHER_DECISION)

r1's 44 Path 4 items are a mix of:

- `dim_review_status = None` (hard gate) — 1 item
- OWNER terms with `mti_terms.status IN ('delete','candidate_delete')` — many items (suggests stale term classifications)
- XREF with unexpected status — several

r214's 15 Path 4 items are group-level (dominant_subject NULL, context_description short/empty — consistent with VC In Progress).

### Path 5 (outstanding tasks)

Consistently: Session A extract not yet generated (generate_session_a_extract.py to be built).

---

## Known Pilot Limitations (Minor)

1. **XREF duplicate flagging** — pilot joins via `strongs_number` which can yield multiple rows per term; same `wa_term_inventory.id` can surface 2–3 times. Mitigation: deduplicate in the full sweep runner.
2. **No patch construction** — pilot is read-only; findings not converted to JSON patch operations. Full runner will construct `wa-{nnn}-{word}-readinesssweep-v1-{date}.json` from Path 1 items.
3. **No obslog integration** — pilot writes a single `.md` report; full runner writes phased entries to the sweep obslog per phase R.A–R.L.
4. **Phase R.K idempotence check not exercised** — would require two runs with intermediate patch application.

These are acceptable for pilot validation; full sweep runner addresses them.

---

## Pilot Artefacts

- `scripts/readiness_sweep_pilot.py` (new — ~620 lines)
- `outputs/reports/wa-062-fellowship-readinesssweep-pilot-20260419.md`
- `outputs/reports/wa-001-abomination-readinesssweep-pilot-20260419.md`
- `outputs/reports/wa-214-suffering-readinesssweep-pilot-20260419.md`
- `outputs/reports/wa-global-readinesssweep-pilot-validation-20260419.md` (this file)

---

## Validation Outcome

**The sweep instruction v1.0 is executable against live post-DBR schema.** Phases R.A–R.H all resolve correctly; queries use new schema shapes correctly (mti_term_flags joins, wa_dimension_index 15-column shape, prose_section tables).

**Critical blocker confirmed:** Path 2 directive execution requires OT-DBR-001 resolution (audit_word.py rewrite) before any re-extraction directives can run. The sweep itself runs fine; it just surfaces Path 2 items as BLOCKED until that lands.

**Ready for full sweep runner development:**

1. Build full sweep runner (`scripts/readiness_sweep.py` or `engine/readiness_sweep.py`) based on the pilot pattern
2. Add obslog integration (per phase R.A–R.L writes)
3. Add patch JSON construction from Path 1 findings
4. Add approval gate polling (per Q6: reads obslog for `APPROVED:` / `REJECT:` markers)
5. Add idempotence self-check (R.K)
6. Add Programme Readiness Scorecard generation (post-sweep per Q11)

These are separable tasks. Pilot demonstrates the instruction is sound; the full runner is an engineering extension.

---

## Next Actions

| Priority | Action |
|---|---|
| HIGH | Fix OT-DBR-001 (audit_word.py rewrite) — unblocks Path 2 execution across the programme |
| MEDIUM | Build full sweep runner (extends pilot to full cycle with obslog + patch construction) |
| MEDIUM | Fix pilot duplicate-flagging issue (deduplication by wa_term_inventory.id) |
| LOW | Session A extract generator (generate_session_a_extract.py) to unblock Path 5 Session A coverage |

---

*End of pilot validation report — 2026-04-19*
