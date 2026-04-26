# VC Corrective-Action Strategy — v2

**Document version:** v2 (active strategy)
**Date:** 2026-04-26
**Author:** Claude Code, under researcher direction
**Supersedes:** [vc-corrective-strategy-v1-20260425.md](vc-corrective-strategy-v1-20260425.md) — frozen 2026-04-26 as evidence-of-decision
**Decision record:** [vc-strategy-pivot-proposal-v1-20260426.md](vc-strategy-pivot-proposal-v1-20260426.md) — proposal + researcher response that produced this v2
**Status:** **Active.** Bump minor version (`v2_1`, `v2_2`, …) on substantive edit; bump major (`v3`) on next strategy pivot.

---

## 1. Position

> **Legacy-Complete VC classifications are accepted as Session B input as-is. The programme does not run a per-term v3 re-classification pass over the legacy bucket. Quality issues surface during analysis and are corrected with surgical patches (VCGROUP / VCVERSE / VCSBFLAGS / REPAIR) at the moment they are encountered. The bridge between Verse Context and Session B is a structured Analysis Readiness `.md` that catalogues every term's classification state explicitly — so analysis can apply extra scrutiny to legacy-VC terms where it matters.**

This is a routing change, not a quality compromise: it shifts the work of catching real classification problems from a costly pre-analysis pass (mostly NO-CHANGE) to the analytical lens itself, where context and materiality are already engaged.

---

## 2. Decision rationale (evidence summary)

Full evidence in the predecessor docs. Headline:

| Source | Number |
|---|---|
| VCB-7..14 ledger NO-CHANGE rate (RE-EVAL cohort, N=67) | ~84% overall, 76% in last 25-term window |
| VCB-Q01 (today, flag-targeted) | 6 of 6 NO-CHANGE under v3_10 contracts |
| Outlier-scan hit rate (today) | 1 of 3 statistical signals was actual pathology |
| Real fixes today (diligence, H4639H/I, Outlier-1) | None required a per-term VC pass to surface — all caught by focused scans operating on existing data |

**Conclusion:** the per-term v3 pass over the legacy bucket was confirming what was already there. Cost was high; signal was low. Statistical-outlier scans plus flag-driven targeting were already producing the actionable real fixes without needing the bulk pass.

---

## 3. Scope

### 3.1 Applies to

- Registries with `verse_context_status='Complete'` and OWNER terms at `mti_terms.vc_status='not_done'` (the **legacy-Complete bucket**, ~169 registries / ~1,800 OWNER terms as of 2026-04-26).

### 3.2 Does NOT apply to

| Out of scope | Treatment unchanged |
|---|---|
| 6 reset registries (compassion 23, fellowship 62, forgiveness 64, grace 68, love 103, mercy 111) | Full v3 re-classification per Q12 mandate (2026-04-19) |
| NULL / excluded registries | Excluded |
| FRESH terms (no prior verse_context rows) | Full v3 classification via VCNEW |
| Partial-completion gaps (prior rows + missing verses on the same term) | VCNEW for missing verses required; existing rows accepted as-is unless analysis-stage materiality test escalates |
| `verse_context_status='In Progress'` | Not eligible until status resolves |

### 3.3 Audit signal

`mti_terms.vc_status` carries the audit trail:

| Value | Meaning |
|---|---|
| `vc_completed` | Classified under v3_x contracts; trusted within v3 grouping doctrine |
| `not_done` | **Legacy-Complete; no v3 pass performed; subject to materiality-driven escalation during analysis** |
| `to_revise` | Reset registries (Q12) — pending full v3 reclassification |

No new vocabulary value is needed. The existing field IS the audit signal.

---

## 4. The Analysis Readiness `.md` — load-bearing mechanism

The handoff between Verse Context and Session B Analytic-output is **a structured `.md` document** generated from the database at the start of Session B Stage 2 for each registry.

### 4.1 Purpose

- Presents the registry's data **as available facts** — Analytic-output reads, does not query.
- **Explicitly catalogues** every term's vc_status; legacy-VC terms get a dedicated section.
- Carries verbatim verse text, so DB consultation is not needed.
- Encodes the analytical instruction: *legacy-VC classifications are facts on the ground; if a finding depends materially on one of them, raise an escalation flag.*

### 4.2 Structure (canonical)

The `.md` carries the following sections (full spec in §10 of the [pivot proposal](vc-strategy-pivot-proposal-v1-20260426.md), refined during pilot):

1. Registry overview (status fields, inference_note, word_synopsis preserved verbatim)
2. Term inventory (OWNER, all)
3. **Legacy-VC terms — unverified under v3 contracts** (the dedicated escalation-target section)
4. v3-confirmed terms
5. Cross-registry context
6. Open flags carried forward
7. Verbatim verse text
8. Readiness verification

### 4.3 Storage

Generated `.md` is stored both as a file (`outputs/reports/words/wa-{NNN}-{word}-readiness-output-v{n}-{YYYYMMDD}.md`) and as a `prose_section` row (so it's queryable, version-tracked, and accessible to downstream stages).

### 4.4 Generation

Initial generator script (to be built): extends or sits alongside `build_session_a_prose.py` and `build_complete_extract.py`. Runs once per registry at Stage 2 start. Same DB → `.md` rendering pattern as the existing renderers.

---

## 5. Materiality protocol at the analysis stage

For each finding produced by Analytic-output:

1. Identify the source terms / verses underlying the finding.
2. Check: does any source carry `vc_status='not_done'` (i.e. is it a legacy-VC term per the readiness `.md` §3)?
3. If **no** → proceed normally. The finding is sourced from v3-confirmed classification.
4. If **yes** → assess materiality:
    - Would the finding change if those source verses/groups were classified differently?
    - Is the legacy classification of those sources a load-bearing assumption of the finding?
5. If **material** → emit `ANALYSIS_VC_UNVERIFIED_MATERIAL` flag (new flag-type, see §6) carrying:
    - Source term(s) + mti_term_id
    - Source verses (verse_record_id list)
    - The alternative classification scenario
    - Predicted change to the finding under the alternative
6. If **non-material** → record the source-legacy-VC fact in the finding's audit trail, no escalation.

The materiality test is the analyst's judgement, not a mechanical rule. The protocol mandates that the question is asked, not how it is answered.

---

## 6. New flag type — `ANALYSIS_VC_UNVERIFIED_MATERIAL`

| Field | Value |
|---|---|
| `flag_code` | `ANALYSIS_VC_UNVERIFIED_MATERIAL` |
| Carrier table | `wa_session_research_flags` (existing) |
| Source session | Session B output (Stage 2 Analytic-output) |
| Mandatory fields | source mti_term_id list, source verse_record_id list, materiality assessment (free text), alternative classification scenario, predicted impact on finding |
| Resolution path | (a) reclassify the source term(s) under v3 if the finding is genuinely changed — VCREVISE on demand; or (b) the finding is robust to the classification uncertainty and the flag is documentation only — researcher decision per case |
| Naming chosen because | More specific than generic `FURTHER_RESEARCH_REQUIRED`; the resolution path is bounded (VC reclassification of named terms), not open-ended research |

Implementation: small schema migration (one new flag-code value); applicator extension to handle the mandatory-field validation.

---

## 7. Patch routing under v2

| Default flow | Patch type | Trigger |
|---|---|---|
| Routine analysis-stage corrections | **VCGROUP** | Group description / anchor / dissolve issue surfaced during analysis |
| Routine analysis-stage corrections | **VCVERSE** | Single-verse classification flip (is_relevant, set_aside_reason, group reassignment) |
| Cross-stage findings | **VCSBFLAGS** | Concept-level / boundary observations for downstream attention |
| Term-status fix | **REPAIR** (mti_terms.status update path) | Extraction anomaly, sub-gloss shell, registry-architecture decision |
| Reset-registry full reclassification | **VCREVISE** + **VCNEW** | Q12 mandate; the 6 reset registries |
| Partial-completion gap on any term | **VCNEW** | New verses surfaced by audit_word re-runs |
| Material analysis-time uncertainty | **VCREVISE** on demand | Triggered by `ANALYSIS_VC_UNVERIFIED_MATERIAL` resolution path (a) |

Routine VCREVISE on the legacy-Complete bucket — used heavily under v1 — is no longer the default flow.

---

## 8. Trigger conditions for re-evaluating v2

If any of the following surface, **stop and re-evaluate v2 before continuing**:

1. **Systemic downstream issues.** Multiple Session B / DimReview / Session C / Session D findings reporting classification gaps that target the same legacy-VC pattern (e.g. a recurring grouping fault in a class of terms). Implies a methodology-era drift, not random per-term variance.
2. **`ANALYSIS_VC_UNVERIFIED_MATERIAL` rate exceeds threshold.** Provisional threshold: more than **15% of Session B findings** carry the flag. If sustained over 5+ registries' Session B work, that's evidence the legacy classifications are not robust enough to support analysis without targeted preflight VC.
3. **A revised-after-flag classification is later found wrong** — i.e. when an `ANALYSIS_VC_UNVERIFIED_MATERIAL`-driven VCREVISE is run and the result of that VCREVISE produces a finding that itself proves wrong. Indicates the materiality test isn't catching what it should.
4. **Researcher-initiated review.** v2 is conditional; the researcher may revisit the strategy at any time.

Each trigger event lands a v2.X update to this document with the observed evidence and the decision taken (continue, refine, pivot back to v1-style bulk pass, or pivot forward to v3).

---

## 9. Why VCCONFIRM was rejected

Strategy v1 §4.1 proposed a **VCCONFIRM** patch type — bulk advancement of low-risk legacy terms to `vc_completed` without classifier review. v2 rejects this for two reasons:

1. **Unnecessary under the `.md` mechanism.** The whole point of VCCONFIRM was to let Session B's gate pass without per-term review. The `.md` mechanism achieves the same outcome more cleanly: legacy terms stay at `vc_status='not_done'` (accurate state), and the `.md` carries the analytical context Session B needs.
2. **Wrong epistemics.** VCCONFIRM would have advanced ~1,400 terms to `vc_completed` based on signal-targeted predictors that today's evidence shows are unreliable at small N. v2 keeps `vc_completed` honest — it means "classified under v3", nothing weaker. The audit trail is sharper.

VCCONFIRM design discussion and rationale-for-rejection retained in v1 (frozen) for audit. No applicator extension or instruction amendment was committed; net cost of obsolescence is zero.

---

## 10. Implementation roadmap

| Step | Item | Status |
|---|---|---|
| 1 | Issue v2 strategy doc (this file) | **Done 2026-04-26** |
| 2 | Pilot the readiness `.md` design on one v3-confirmed registry (researcher choice: 067 goodness) | **In progress 2026-04-26** |
| 3 | Iterate on `.md` structure based on pilot feedback | Pending |
| 4 | Mixed-state pilot on a registry with both vc_completed and legacy `not_done` terms (proposal: 094 intercession or 020 character) | Pending |
| 5 | Edit instruction docs in parallel (4 docs — see §11) | Pending |
| 6 | Schema migration for `ANALYSIS_VC_UNVERIFIED_MATERIAL` flag-type | Pending |
| 7 | Programme cutover — formally accept legacy-Complete bucket as Session B input | Pending |

Steps 2 and 3 are load-bearing. Steps 4–7 follow once the `.md` shape is settled.

---

## 11. Instruction-document edits required

| Document | Current | Target | Change |
|---|---|---|---|
| `prog_instr_verse_context` (programme prose) | v3 | v4 | Add governance paragraph: legacy-Complete bucket accepted as analysable input; v3 reclassification reserved for reset registries + analysis-driven escalations |
| `prog_instr_session_b_readiness` (new section if absent) | n/a | v1 | Document the `.md` handoff: readiness output is canonical input for Analytic-output |
| `wa-dimensionreview-instruction` | v3_3 | v3_4 | Accept incomplete VC; add materiality check protocol for cluster classifications |
| `wa-sessionb-analysis-readiness` | v1_6 | v1_7 | Replace hard VC gate with structural `.md` gate; spec the readiness output structure |
| `wa-sessionb-analysis-output` | v1_1 | v1_2 | Input source change (`.md`-driven); materiality protocol per finding; escalation to `ANALYSIS_VC_UNVERIFIED_MATERIAL` |

All five edits go through standard prose-supersede / instruction-supersede pipelines. No applicator-instruction shape changes required.

---

## 12. Outstanding strategy-level decisions

Two items not addressed in the pivot proposal that researcher should rule on:

1. **Empirical ledger treatment.** Refresh once at N=73 (post-VCB-014 + VCB-Q01) and freeze as evidence-of-decision, or continue rolling? **CC default:** refresh + freeze. Rationale: the evidence is now sufficient for the v2 commitment; ongoing batch-by-batch tracking has no decision-driving value once v2 is active.
2. **Pre-flight outlier-scan tool.** Build it lightweight (single script, on-demand or scheduled), defer it, or skip it? **CC default:** build it lightweight. Rationale: today's signal-detection insight is independent of the `.md` mechanism — focused scans surface real anomalies cheaply, regardless of the bulk-pass policy. Worth keeping as a programme tool.

If both defaults are accepted, no further input needed.

---

*v2 issued 2026-04-26. Next concrete output: pilot readiness `.md` for registry 067 goodness (Step 2).*
