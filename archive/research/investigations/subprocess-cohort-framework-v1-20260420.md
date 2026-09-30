# SUBPROCESS_NEEDED Cohort — Framework + Execution Plan — v1 — 2026-04-20

| Field | Value |
|---|---|
| Filename | subprocess-cohort-framework-v1-20260420.md |
| Trigger | Scorecard v2 SUBPROCESS_NEEDED tier (154 registries, 72% of programme) |
| Purpose | Framework for batching + executing the 1,361 Path 2 findings across the cohort |
| Action reference | Programme control v1 — Action T |
| Status | **DRAFT v1 — awaiting researcher review of execution plan** |
| Produced | 2026-04-20 |

---

## 1. Headline

**1,361 Path 2 findings across 154 registries** — all fall into three well-defined directive families. All three are **currently unblocked** (OT-DBR-001 + OT-DBR-004 resolved 2026-04-19). No single blocker stops execution.

This is the real analytical backlog. Clearing it moves ~72% of the programme from SUBPROCESS_NEEDED to STRUCTURALLY_CLEAN / BANKED.

---

## 2. Path 2 taxonomy

| # | Directive family | Findings | Typical issue | Resolution path | Unblock status |
|---:|---|---:|---|---|---|
| A | `audit_word` re-run — **span-failure** | 902 | "span filter failure (span=N, all deleted)" | Re-extract + audit_word + VC rerun for affected term(s) | UNBLOCKED 2026-04-19 (OT-DBR-001) |
| B | `audit_word` re-run — **zero-extraction** | 254 | "zero extraction (occ=N, no verse records)" | Re-extract + audit_word rerun for affected term(s) | UNBLOCKED 2026-04-19 (OT-DBR-001) |
| C | Dimension Review sub-process | 205 | NULL dimension / non-reviewed confidence | Cluster DimReview with DIMREVIEW patch | UNBLOCKED (e.g. C01 in progress via Action U) |

Phase distribution:

| Phase | Count |
|---:|---:|
| R.B (term inventory) | 1,156 (85%) |
| R.E (dimension assignments) | 205 (15%) |

---

## 3. Cohort shape

### 3.1 Registries affected: 154 of 213 carry_forward=1 registries (72%)

### 3.2 Top 10 registries by Path 2 finding count

| no | word | cluster | P2 count | Estimated directive class mix |
|---:|---|---|---:|---|
| 43 | desire | C04 | 106 | mostly A (span failures) |
| 126 | purpose | C02 | 73 | mostly A |
| 4 | anger | C07 | 71 | mostly A |
| 146 | shame | C06 | 56 | mostly A |
| 23 | compassion | C17 | 52 | mostly A (reset word) |
| 160 | thought | C02 | 52 | mostly A |
| 42 | delight | C03 | 46 | mostly A |
| 197 | authority | C20 | 41 | mostly A |
| 117 | peace | C17 | 40 | mostly A (reset word) |
| 61 | fear | C06 | 32 | mostly A |

Top 10 account for 569 findings (42% of total). These are the large-cluster words where a single audit_word re-run could close 30-100 findings in one sweep.

### 3.3 Distribution tail

Most affected registries have <10 Path 2 findings — quick to clear once the directive is authored.

---

## 4. Directive families — templates

Each directive follows `wa-directive-instruction [current]` (v1.1) 5-element format. The three families share common structure but differ in scope/outcome.

### 4.1 Family A — `audit_word` span-failure re-run

**Motivation template:**
> Registry {N} ({word}) has {M} term(s) where the STEP span filter discarded all verse records during initial extraction — `span filter failure (span={k}, all deleted)`. These terms are present in wa_term_inventory but carry no active verse records. The registry's Path 2 queue cannot clear and session_b_status cannot advance until these are re-extracted. OT-DBR-001 (audit_word rewrite for post-DBR schema) resolved 2026-04-19, unblocking this directive.

**Scope template:**
> Tables: `wa_term_inventory` + downstream `wa_verse_records`, `wa_data_quality_flags`.
> Criterion: `wa_term_inventory.delete_flagged=0` AND exists `wa_data_quality_flags.flag_code='SPAN_RESOLUTION_CONFLICT' OR similar` in pilot output.
> Registry filter: `wa_file_index.word_registry_fk = N`.
> Expected term count: {M}.

**Outcome required template:**
> For each affected term:
> 1. Re-fetch via `step_client.get_verse_records_with_html()` with expanded span matching
> 2. Run `engine.audit_word` on the registry (post-REPAIR gate)
> 3. Verify verse records populated; update quality flags (SPAN_FILTER_APPLIED if filter ran clean)
> 4. Verify `verse_context_status` reset to 'In Progress' for any registry with new unclassified verses

**Completion confirmation template:**
> 1. `SELECT COUNT(*) FROM wa_term_inventory WHERE file_id IN (SELECT id FROM wa_file_index WHERE word_registry_fk=N) AND delete_flagged=0 AND id NOT IN (SELECT term_inv_id FROM wa_verse_records WHERE delete_flagged=0)` → expected 0
> 2. Re-run pilot on registry N → Path 2 count for span-failure findings → expected 0

### 4.2 Family B — `audit_word` zero-extraction re-run

Same structure as A; criterion differs: "terms with `occurrence_count > 0` but zero verse records". Motivation names the zero-extraction pattern specifically.

### 4.3 Family C — Dimension Review sub-process

Same structure as C01 handoff (see [wa-dim-C01-handoff-kickoff-v1-20260420.md](../../data/imports/WA/Session_B_Dimension_Review/wa-dim-C01-handoff-kickoff-v1-20260420.md)). Scope: groups with NULL dimension OR `dimension_confidence IN ('KEYWORD_*','ROOT_INFERRED','UNCLASSIFIED')`. Resolution: cluster-level DimReview producing DIMREVIEW patches.

---

## 5. Execution sequencing strategy

The cohort is too large for a single-pass execution. Propose **three-wave** rollout.

### Wave 1 — Pilot (1 registry, ~1 day)

Pick a single small-cohort registry for the pilot:

- **r188 weeping** (cluster C05): 1 P2 finding — minimal-risk pilot for Family A
- OR **r134 renewal** (BANKED already — no P2): skip
- OR **r30 contrition** (cluster C13, Family A small): check

Scope: 1 directive, 1 patch cycle, 1 end-to-end validation. Validates the directive template + the full re-run cycle against post-DBR code.

**Deliverables:** one signed-off directive + one successful re-run, with per-step diagnostic capture.

### Wave 2 — Bulk (span-failure cohort, ~86 registries)

After pilot success, roll out Family A to all 86 registries with span-failure findings. Ordering:

1. Reset-6 words first (compassion, fellowship, forgiveness, grace, love, mercy) — they are already queued for reprocess per Q12
2. Then cluster-by-cluster, starting with smaller clusters (C13, C14, C17 — already partial)
3. Leave largest clusters (C01, C02, C07, C11) for last — these have the biggest registries and longest audit_word runtimes

### Wave 3 — Remaining families (B + C, ~68 registries)

Family B (zero-extraction) + Family C (dim review) often overlap with Family A. Many registries need all three. Run them sequentially per registry after Wave 2's audit_word work clears.

---

## 6. Estimates

### Per-registry effort

- Directive authoring (per registry): 10–20 minutes (templated)
- `audit_word` re-run runtime: 5 minutes (small registries) to 60 minutes (r43 desire, r126 purpose, r4 anger)
- Verse Context re-run if new verses surface: depends on VC batch throughput
- Post-run sweep + scorecard refresh: 2 minutes

### Programme-level effort

| Wave | Registries | Effort estimate |
|---|---:|---|
| 1 (pilot) | 1 | ~0.5 day |
| 2 (span-failure bulk) | 86 | ~4–5 working days |
| 3 (zero-extraction + dim) | 68 | ~3–4 working days |
| **Total** | **155** | **~8–10 working days** |

Parallelisable? Partially — Wave 2 registries are independent; can run 3–4 in parallel with multiple directive-patch cycles.

---

## 7. Pilot directive — pre-drafted

Below is a ready-to-use Wave 1 pilot directive for **r188 weeping** (C05; 1 Path 2 finding; small enough to complete in one afternoon).

```markdown
# Directive DIR-20260421-001 — audit_word re-run for r188 weeping span-failure

> Produced by: wa-directive-instruction-v1_1-20260418 (template)
> Governed by: wa-global-general-rules-v2_11-20260418
> Registry: 188 (weeping)
> Produced date: 2026-04-21
> Researcher approval: PENDING

---

## Motivation

Readiness sweep 2026-04-19 identified 1 Path 2 finding in registry 188 (weeping, C05) — a single term with span filter failure (all verse records deleted during initial extraction). This term cannot contribute to the C05 analytical picture until re-extracted. With OT-DBR-001 resolved, audit_word re-runs are now supported.

## Scope

- Table: `wa_term_inventory`
- Criterion: `file_id IN (SELECT id FROM wa_file_index WHERE word_registry_fk = 188)` AND `delete_flagged = 0` AND `id NOT IN (SELECT term_inv_id FROM wa_verse_records WHERE delete_flagged = 0)`
- Expected count: 1 (verify in Phase 1 of execution)

## Outcome required

- Affected term(s) have active `wa_verse_records` rows after re-extraction
- Quality flags updated (`SPAN_FILTER_APPLIED` set if filter ran clean)
- `verse_context_status` set to 'In Progress' if any new unclassified OWNER verses surface
- Audit report shows PASS or REVIEW (not STOP)

## Completion confirmation

1. `SELECT COUNT(*) FROM wa_term_inventory ti WHERE ti.file_id IN (SELECT id FROM wa_file_index WHERE word_registry_fk=188) AND ti.delete_flagged=0 AND ti.id NOT IN (SELECT term_inv_id FROM wa_verse_records WHERE delete_flagged=0);` → expected 0
2. Re-run `python scripts/readiness_sweep_pilot.py --registry=188` → expected Path 2 count 0

## Notes

- First use of audit_word re-run against post-DBR rewrite (OT-DBR-001 resolution 2026-04-19). Monitor for regressions against the rewrite; report any anomalies.
- If any unclassified OWNER verses surface, include them in next Verse Context batch (VCB-{nnn}).
- Runtime expected ≤ 10 minutes for this single-term case.
```

---

## 8. Risk assessment

| Risk | Severity | Mitigation |
|---|---|---|
| audit_word re-run post-DBR has regressions | MEDIUM | Pilot (Wave 1) catches it before bulk |
| Span filter still produces all-deleted results (STEP API limitation) | MEDIUM | Pilot instruments output; if unresolvable at source, escalate as engineering item |
| Re-extraction creates mass unclassified verses → VC queue swamped | MEDIUM | Stage re-runs, don't batch all 86 at once; VC batches of 2-2.5k verses per standard discipline |
| Cluster boundaries / shared terms → audit_word on one registry affects neighbours | MEDIUM | Per-registry locking + discipline already in place |
| OT-DBR-009 (mti_terms dedup) interaction with re-run | LOW | audit_word uses canonical mti_terms via strongs_number — already robust |

---

## 9. Interaction with other work

| Concurrent work | Interaction |
|---|---|
| Action R (mti_terms dedup, M32) | Orthogonal. Can run before, during, or after T. Dedup improves post-migration audit_word clarity but is not a prerequisite. |
| Action U (C01 DimReview) | Subset of T Family C. Executing U first validates the Family C pattern for broader rollout. |
| Session A extracts (Action S) | Independent. Session A extract regeneration post-T will reflect any new verses/dimensions — expected behaviour. |
| Coverage flag redesign (M29) | Independent. No conflict. |
| 6 reset words (compassion, fellowship, forgiveness, grace, love, mercy) | High overlap with T Wave 2. These words have Q12 reset marker (`session_b_status='Verse Context Reset'`). T Wave 2 ordering places them first. |

---

## 10. Open decisions for researcher

| # | Question | Recommendation |
|---|---|---|
| 1 | **Approve overall T framework?** | Yes — structure is clean, pilot validates before bulk |
| 2 | **Wave 1 pilot target registry** — r188 weeping vs another? | r188 (1 finding, small, clean verify path) |
| 3 | **Wave 2 sequencing** — reset-6 first, or small-clusters first? | Reset-6 first (already queued for reprocess; closes the Q12 decision) |
| 4 | **Directive per registry vs batch directives?** | Per registry — each registry gets its own DIRECTIVE ID and confirmation; auditable |
| 5 | **Parallelism — how many registries concurrent?** | Start with 1 (pilot); once stable, 2-3 parallel sweeps is safe |
| 6 | **Session B status during T execution** — does `Verse Context Reset` hold, or revert to NULL? | Preserve 'Verse Context Reset' for Q12 cohort; others remain at their existing status |

---

## 11. Recommended next move

**T stays queued.** Execution requires:

1. Researcher approval of §10 decisions
2. Wave 1 pilot directive authored (template ready in §7) and executed
3. Learnings from pilot folded into Wave 2 directive templates
4. Wave 2 bulk execution over 4-5 working days
5. Wave 3 over additional 3-4 days

Framework is now at the point where a single approval unlocks ~8-10 days of tractable work.

---

*Draft v1 — 2026-04-20. Awaiting researcher approval on §10.*
