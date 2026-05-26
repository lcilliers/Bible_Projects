# Audit framework — design (draft for review)

**Status:** DRAFT v0.1 — not yet ratified
**Date:** 2026-05-26
**Author:** CC
**Audience:** Researcher
**Supersedes:** No prior audit framework (the previous ad-hoc audits were not real audits — see §1)

---

## §0. Purpose

Define what "audit" means in this programme and how it should be performed. Audit answers four questions per the researcher's framing (2026-05-26):

1. **Has all evidence and support for findings been captured?** (completeness)
2. **Does it hold together?** (internal consistency)
3. **Can it be back-tracked?** (traceability)
4. **Are there cross-cluster inconsistencies that need to be flagged or fixed?** (cross-cluster integrity)

Audit is about **analytic integrity** — does the database faithfully and completely represent the analytical work; can downstream consumers trust what they read.

---

## §1. Background — why a redesign is needed

Prior "audits" run by CC during M10/M10b closure were not audits in the sense above. They were **filename-to-source_file diffs** that:

- Drove the check from the file inventory ("which files are mentioned in `cluster_observation.source_file`?") rather than from the principle ("for each analytical artefact category produced by the pipeline, is it in DB?")
- Used a hand-rolled `is_legitimate_input()` regex to classify files, treating filename patterns as criteria
- Never compared **content depth** — a file mentioned in `source_file` was marked "captured" even if only a one-paragraph extract was loaded from a 30 KB analytical document
- Surfaced cross-cluster inconsistencies not at all
- Missed: 8 thematic-observation sections (66 KB), 22 per-char Self-check blocks, 6 VCG-design rationale docs (160 KB), 56 Phase 3 STAYS verdict rationales, sub-group-design rationale, split-design rationale — all on disk only, none in DB.

The redesign starts from the principle and works downward: enumerate every authored analytical artefact category, declare its DB target, verify presence + depth — then add the three other dimensions on top.

---

## §2. Audit Dimension 1 — Evidence completeness

### §2.1 The core check

For each pipeline event that produces authored analytical content, the audit verifies that the content lives in DB at appropriate depth.

Driven by an **artefact-category registry** (declarative list, not file inventory). Each entry:

- **Pipeline event** (Phase 1 borderline disposition, Phase 5 sub-group design, Phase 9 Self-check, etc.)
- **Authored artefact type** (per-verse, per-term, per-sub-group, per-VCG, per-prompt, etc.)
- **DB target** (which table + column holds the content)
- **Depth check** (minimum content size, or cross-reference to source-doc size)
- **Cardinality check** (one per term, one per sub-group, 189 per char, etc.)

### §2.2 The artefact-category registry (initial draft)

| # | Pipeline event | Authored artefact | DB target | Depth check | Cardinality |
|---|---|---|---|---|---|
| C1 | Phase 1 UT classification | Per-verse decision + reason | `verse_context.is_relevant` + `set_aside_reason` | set_aside_reason present for every is_relevant=0 row | 1 row per UT-classified (verse_record, term) |
| C2 | Phase 1 borderline disposition | Per-borderline-verse rationale | `cluster_observation` BORDERLINE_DISPOSITION | Row exists if cluster had Phase 1 borderlines | 1 row per parked borderline |
| C3 | Phase 2 Pass A | Per-verse meaning + keywords | `verse_context.analysis_note` + `keywords` | Both NOT NULL for every is_relevant=1 row | 1 row per is_relevant verse |
| C4 | Phase 3 constitution debate | Per-term verdict + rationale | `cluster_observation` VERDICT_RATIONALE | Description ≥ 200c, names verdict (STAYS/TRANSFERS/BOUNDARY) | 1 row per term |
| C5 | Phase 5 sub-group design | Per-sub-group rationale | `cluster_subgroup.core_description` PLUS `cluster_observation` SUBGROUP_DESIGN_RATIONALE if source-doc was longer | **Depth-delta:** if source design-doc has ≥1500c per sub-group AND `core_description` < 500c → SUBGROUP_DESIGN_RATIONALE row required | 1 row per sub-group; rationale obs per source-doc section |
| C6 | Phase 5 revision (if any) | Methodology-pivot rationale | `cluster_observation` SUBGROUP_DESIGN_RATIONALE with source_phase='phase_5_subgroup_design_revision' | Row exists if revision occurred (detectable via two design-doc versions) | 1+ rows per revision |
| C7 | Phase 7 VCG design | Per-VCG rationale | `verse_context_group.context_description` PLUS `cluster_observation` VCG_DESIGN_RATIONALE if source-doc was longer | **Depth-delta:** same pattern as C5 | 1 row per VCG; rationale obs per source-doc section |
| C8 | Phase 8.7 characteristic mapping | Char definition + per-(char,sg) note | `characteristic.definition` + `characteristic_subgroup.qualifier_note` | Both populated; definition ≥ 200c | 1 row per char + 1 link per (char, sg) |
| C9 | Phase 8.7 carry-forward observations | INTEGRATION_NOTE / SPLIT_SUBGROUP | `cluster_observation` INTEGRATION_NOTE / INTER_RELATIONSHIP / CROSS_CLUSTER_HANDOFF | All flagged carry-forwards in DB | 1+ rows per signal |
| C10 | Phase 9 per-char findings | 189 prompts × char | `cluster_finding` (char-scope) | finding_text ≥ 100c per row | 189 × N (char count) |
| C11 | Phase 9 per-char Self-check | Meta-observations | `cluster_observation` SELF_CHECK_OBSERVATION | Row per char-scope batch | 1 per characteristic |
| C12 | Phase 9 cluster synthesis (standard) | 189 cluster-scope rows | `cluster_finding` (characteristic_id=NULL, finding_status='cluster_synthesis') | finding_text ≥ 100c per row | 189 |
| C13 | Phase 9 cluster synthesis (aspect_based) | Tier guides + cluster-scope themes | `cluster_observation` TIER_READING_GUIDE + CLUSTER_SYNTHESIS | Per-tier guide count proportional to tier prompt count; cluster-scope themes per source doc | Cluster-dependent (M10 had 27 + 15 + 8 thematic) |
| C14 | Phase 9 synthesis appendix | Free-form prose themes | `cluster_observation` CLUSTER_SYNTHESIS | Theme-level rows | 1 per appendix theme |
| C15 | Phase 9 thematic exploration (when present) | Pre-synthesis analytical observations | `cluster_observation` CLUSTER_SYNTHESIS | Section-level rows | 1 per source-doc section |
| C16 | Pre-Phase-1 split design (derived clusters) | Split decision rationale | `cluster_observation` SPLIT_DESIGN_RATIONALE | Row per derived cluster | 1+ rows |
| C17 | Phase 10 inherited-finding reconciliation | Per-finding disposition + fold-back | `wa_session_b_findings.resolution_note` + folded text in `cluster_finding.finding_text` | Every RESOLVED-BY-CATALOGUE row points to fold-target ids | 1 per inherited finding |

### §2.3 The depth-delta check (the missed-failure-mode catcher)

The most important addition. For artefacts where DB has a short summary field AND a long source doc exists:

```
source_file_size = length(source_doc.md)
db_summary_size  = length(target_column)  -- e.g. core_description, context_description
depth_ratio = db_summary_size / source_file_size

If depth_ratio < THRESHOLD (suggest 0.2 — i.e. DB has < 20% of source content)
  AND no per-section cluster_observation rows exist for this source_file
  → FAIL: source-doc content not adequately captured at depth.
```

This would have caught my M10 / M10b sub-group design and VCG design failures immediately. The threshold is configurable; 0.2 is a starting suggestion.

### §2.4 Source-file discovery

The audit registry knows where each artefact CATEGORY's source file should be (by naming convention or directory). For each cluster:

- Phase 5 design doc: `Sessions/Session_Clusters/{code}/files phase 5/wa-cluster-{code}-subgroup-design-v*-*.md` OR `Sessions/Session_Clusters/{code}/WA-{code}-subgroup-design-v*-*.md` (M10b pattern)
- Phase 7 VCG design docs: `Sessions/Session_Clusters/{code}/files phase 7/wa-cluster-{code}-{sg}-vcg-design-v*-*.md`
- Phase 9 per-char findings: `Sessions/Session_Clusters/{code}/files phase 9/wa-cluster-{code}-phase9-char*-findings-v*-*.md`
- (etc. — full glob registry to be assembled during implementation)

For categories without a standard filename pattern (e.g. thematic exploration), the audit checks for ANY .md file in the cluster folder matching a content signature, then asks whether its content is represented.

---

## §3. Audit Dimension 2 — Internal consistency

Reference-integrity, cardinality, coverage. These are mostly SQL existence/join checks.

### §3.1 Reference integrity

| Check | Pass criterion |
|---|---|
| Every `cluster_finding.obs_id` → `wa_obs_question_catalogue.obs_id` | 100% join |
| Every `cluster_finding.characteristic_id` → `characteristic.id` (NULL allowed for cluster-scope) | 100% join (where non-NULL) |
| Every `cluster_finding.cluster_subgroup_id` → `cluster_subgroup.id` (NULL allowed) | 100% join |
| Every `cluster_observation.characteristic_id` → `characteristic.id` (NULL allowed) | 100% join |
| Every `cluster_observation.cluster_subgroup_id` → `cluster_subgroup.id` (NULL allowed) | 100% join |
| Every `verse_context.cluster_subgroup_id` → `cluster_subgroup.id` | 100% join |
| Every `verse_context.group_id` → `verse_context_group.id` | 100% join |
| Every `vcg_term.vcg_id` + `mti_term_id` references active rows | 100% join, both sides active |
| Every `characteristic_subgroup.characteristic_id` + `cluster_subgroup_id` reference active rows | 100% join |
| Every `mti_term_subgroup.mti_term_id` + `cluster_subgroup_id` reference active rows | 100% join |
| Every `finding_citation.source_id` → `cluster_finding.id` or `cluster_observation.id` (by source_table) | 100% join |

### §3.2 Cardinality

| Check | Pass criterion |
|---|---|
| Per-cluster `cluster_finding` (char-scope) count | 189 × N characteristics |
| Per-cluster `cluster_finding` (cluster-synthesis) count | 189 for standard clusters; cluster-specific for aspect_based |
| Per-characteristic 189-prompt completeness | Every (obs_id, characteristic_id) pair has exactly 1 row |
| Per-cluster characteristic count vs sub-group count | Standard: each sub-group has ≥1 char link (except BOUNDARY); aspect_based: noted as exception |

### §3.3 Coverage (no orphans, no gaps)

| Check | Pass criterion |
|---|---|
| Every active is_relevant `verse_context` has `cluster_subgroup_id` AND `group_id` | 100% routed (post Phase 6/7) |
| R4 anchor gate | Every term with is_relevant ≥1 has is_anchor ≥1 |
| Phase 8 inherited VCG dissolution | 0 active is_relevant `verse_context` rows reference an inherited (non-cluster-pattern) VCG |
| `vcg_term` coverage | For every (vcg, term) pair seen in `verse_context.{group_id, mti_term_id}`, a `vcg_term` row exists |
| `mti_term_subgroup` coverage | For every (term, sub-group) pair seen in `verse_context.{mti_term_id, cluster_subgroup_id}`, an `mti_term_subgroup` row exists |
| `characteristic_subgroup` coverage | Every active sub-group (except BOUNDARY) has ≥1 char link |
| Soft-delete consistency | No `cluster_finding` row's obs_id is delete_flagged in catalogue; no active row references a deleted verse |

---

## §4. Audit Dimension 3 — Traceability

For any row in DB, the audit confirms it carries enough metadata to back-trace its origin.

### §4.1 Per-row trace checks

| For any... | The audit confirms... |
|---|---|
| `cluster_finding` row | `source_file` populated; `obs_id` resolves; `characteristic_id` (if non-NULL) resolves; verses anchored (via term + VCG path) discoverable |
| `cluster_observation` row | `source_file` populated OR `source_phase` populated (auto-generated rows); status + raised_date present |
| `verse_context` row | `verse_record_id` resolves; `mti_term_id` resolves; meaning + keywords present if is_relevant=1; set_aside_reason present if is_relevant=0 |
| `verse_context_group` row | `context_description` populated; ≥1 active member via verse_context.group_id; ≥1 active anchor verse |
| `cluster_subgroup` row | `core_description` populated; ≥1 member term (except BOUNDARY); ≥1 char link |

### §4.2 Pipeline-level trace checks

| Check | Pass criterion |
|---|---|
| Every patch in `engine_run_log` exists as a file in `archive/patches/` | 100% present |
| Every schema migration is in `schema_version.migration_history` | 100% present |
| Every cluster directive referenced by `cluster_observation.source_file` actually exists in the cluster folder | 100% present |

### §4.3 NULL-source detection

Any row with NULL `source_file` AND NULL `source_phase` (where one is expected) is flagged. Helps surface rows that have no audit chain back to their origin.

---

## §5. Audit Dimension 4 — Cross-cluster consistency

The hardest dimension and the one no prior audit has touched.

### §5.1 Cross-register signal integrity

When a Phase 3 verdict in cluster A flags cross-register to cluster B (e.g., STAYS+flag, TRANSFERS), there should be a structured record:

| Source side (cluster A) | Target side (cluster B) | Pass criterion |
|---|---|---|
| `cluster_observation` INTER_RELATIONSHIP or CROSS_CLUSTER_HANDOFF or VERDICT_RATIONALE naming B | If B exists, no obligation (the flag is informational); if B receives the term via TRANSFERS, B's `mti_terms.cluster_code` reflects | Source flag explicitly names B; target accepts or notes |
| TRANSFERS verdict in cluster A → cluster B | `mti_terms.cluster_code` for transferred term = B; no `verse_context` rows under the old cluster for that term remain is_relevant=1 | Apply confirmed |
| BOUNDARY → ROUTE-TO-CLUSTER at Phase 8.5 | Source vc rows is_relevant=0 with set_aside_reason naming target; target cluster has the verse picked up via its own (different) term at same verse_record_id | Routing traceable |

### §5.2 Term uniqueness across clusters

| Check | Pass criterion |
|---|---|
| No Strong's number in two clusters' `mti_terms` at the same time | 0 duplicates |
| No `verse_record_id` × `mti_term_id` pair in two clusters' `verse_context` | 0 conflicts (one verse_context row per (vr, term)) |

### §5.3 Anchor verse policy

Anchor verses MAY appear in multiple clusters (a verse can anchor different inner-being characteristics across different clusters). But the audit lists these for review:

| Check | Output |
|---|---|
| Verses listed as anchor in multiple clusters | Report (not fail) — flagged for researcher review |

### §5.4 Inherited Session B findings reconciliation

For each cluster, the audit walks `wa_session_b_findings` rows that target the cluster's terms:

| Check | Pass criterion |
|---|---|
| Every targeted row has `resolution_note` from Phase 10 | 100% (post-Phase-10 clusters) |
| RESOLVED-BY-CATALOGUE rows have fold-back marker in target `cluster_finding.finding_text` | 100% |
| ROUTE-TO-CLUSTER dispositions reach a valid target cluster | 100% |

### §5.5 `cluster.char_structure` aware checks

Introduced 2026-05-26 to handle the M10 pattern.

| Check | Pass criterion |
|---|---|
| Aspect-based clusters (`char_structure='aspect_based'`) excluded from char-by-char cross-cluster comparison | Reports show aspect-based clusters separately, not aggregated against standard clusters |
| Standard clusters (NULL `char_structure`) included in all programme-wide aggregations | No accidental exclusions |
| `char_structure` value is one of the allowed enum: NULL ('standard') or 'aspect_based' | No unexpected values |

### §5.6 Programme-state coherence

| Check | Pass criterion |
|---|---|
| Cluster status distribution makes sense | Each cluster at exactly one known status; no orphaned clusters |
| Stalled clusters identified | Clusters in `Data - In Progress` or `Analysis - In Progress` longer than threshold (suggest 60 days) flagged |
| Schema version consistency | All clusters use the same schema version; no half-migrated state |
| Pipeline-phase progression | Cluster's actual artefact set matches its declared status (e.g., a cluster claiming `Analysis Completed` has Phase 9 findings + Phase 11/12 closure records) |

---

## §6. Implementation shape

### §6.1 Structure

```text
scripts/audit/
├── _audit_framework.py             — orchestrator + report writer
├── _check_completeness.py          — dimension 1 (per artefact category)
├── _check_consistency.py           — dimension 2 (referential / cardinality / coverage)
├── _check_traceability.py          — dimension 3 (source / audit trail)
├── _check_cross_cluster.py         — dimension 4 (programme-wide)
└── audit_registry.py               — declarative list of artefact categories (C1–C17 above + threshold config)
```

### §6.2 Invocation

```bash
# Per-cluster audit
python scripts/audit/_audit_framework.py --cluster M10

# Programme-wide audit (every cluster + cross-cluster checks)
python scripts/audit/_audit_framework.py --programme

# Dimension-specific (e.g. only run cross-cluster checks)
python scripts/audit/_audit_framework.py --programme --dimension cross-cluster

# Strict mode (every WARN becomes FAIL)
python scripts/audit/_audit_framework.py --cluster M10 --strict
```

### §6.3 Outputs

| Mode | Output file |
|---|---|
| Per-cluster | `Sessions/Session_Clusters/{code}/wa-cluster-{code}-audit-v{N}-{date}.md` |
| Programme-wide | `Workflow/audit/wa-programme-audit-v{N}-{date}.md` |

### §6.4 Report format

```markdown
# Audit — {scope} — {date}

**Verdict:** PASS / PASS-WITH-WARNINGS / FAIL
**Checks run:** N
**Passed:** N
**Warned:** N
**Failed:** N

## Dimension 1 — Evidence completeness
### Check C5 — Phase 5 sub-group design rationale
- M10:  ⚠ WARN  source_doc 35,166c, core_description aggregate 7,630c (ratio 21.7%); 10 SUBGROUP_DESIGN_RATIONALE rows present — borderline depth, but coverage compensates
- M10b: ✓ PASS  source_doc 29,834c, core_description aggregate 6,612c (ratio 22.2%); 0 supplementary rows; FAIL under stricter threshold
- M01: ⛔ FAIL  source_doc 22,500c, core_description aggregate 1,800c (ratio 8%); 0 supplementary rows. Needs SUBGROUP_DESIGN_RATIONALE backfill.
...

## Dimension 2 — Internal consistency
### Check ref-1 — cluster_finding.obs_id resolves
- ALL CLUSTERS: ✓ 100% join
...

## Dimension 3 — Traceability
...

## Dimension 4 — Cross-cluster consistency
...
```

### §6.5 Configurability

Per-cluster overrides allowed (e.g., M10's `char_structure='aspect_based'` means C12 standard 189-row cluster-synthesis check is REPLACED by C13 tier-batched check). Override declarations live in the cluster row or in an audit-config table — decided at implementation time.

---

## §7. Out of scope (for later review per researcher direction)

These categories were considered for inclusion in audit scope but explicitly held out. Documented here in case future review wants to fold any back in.

### §7.1 Re-running validation

Phase 11 validation (`_validate_m{NN}_phase11_v1_*.py`) already covers some consistency + cardinality checks per-cluster. The audit should **reference** Phase 11 validator output where it exists, not duplicate the work. Audit is a higher-level integrity check; validation is a phase-specific gatekeeper.

### §7.2 Content judgement

The audit checks "is the row there with adequate depth?" — NOT "is the analysis correct?" or "is the conclusion sound?". Editorial / analytical-quality review is a separate human task. The audit can flag obviously thin content (e.g., `core_description` only 50c) but doesn't judge correctness.

### §7.3 Methodology compliance

The `_audit_cluster_against_instruction_v25_v1_20260518.py` family checks whether a cluster's pipeline followed the governing instruction's steps (5-step canonical cascade). That's a different concept — "did the right process run?" vs the audit's "is the resulting data intact?". They are complementary; audit doesn't duplicate.

### §7.4 Programme-wide editorial review

Audit is not a publication-readiness check. Session C cluster publication has its own review path. The audit confirms the inputs to Session C are present and queryable; it doesn't read for stylistic consistency.

### §7.5 Performance / index hygiene

Database index audits, query-performance audits, storage-size audits — out of scope. Audit is about analytical integrity, not infrastructure.

### §7.6 Anchor verse policy

§5.3 currently REPORTS multi-cluster anchor overlaps without judging them. A future audit revision might add policy (e.g., "no verse may be anchor in >N clusters") but that's a methodological decision, not yet ratified.

### §7.7 Closed-cluster retroactive completeness

The audit can be RUN against closed clusters (M01–M09, M15, M20, M26, M39, M46) to expose backfill gaps, but the audit framework itself doesn't prescribe what to do with the findings. Remediation policy (do nothing / capture-backfill / re-open) is a separate decision per cluster.

---

## §8. Open questions for review

1. **Depth-delta threshold (§2.3).** Suggest 0.2 (DB content ≥ 20% of source-file content). Too aggressive? Too lax?
2. **Source-file discovery patterns (§2.4).** The registry needs glob patterns per artefact category. Are the naming conventions stable enough to rely on?
3. **`char_structure` enum (§5.5).** Currently 2 values: NULL ('standard') and 'aspect_based'. Anticipate more values as other non-standard cluster types come into focus?
4. **Programme-wide audit cadence.** Run on every closure? Weekly? On-demand? Affects how often the report is regenerated.
5. **Audit-failure-handling policy.** Does a FAIL block any operation (e.g., cluster closure, Session C kickoff)? Or is it informational?
6. **§7.1 — Phase 11 validator integration.** Audit could ingest Phase 11 reports as a dependency, OR it could leave Phase 11 entirely separate. Either way, the boundary between "audit" and "validation" needs to be stated in the governing instruction.
7. **The artefact-category registry (§2.2) — completeness.** I've listed 17 categories (C1–C17). Are there categories I've missed? (Examples to consider: dimension review observations from earlier methodology, term-research-flags decisions, registry-level decisions, programme-prose linkage)

---

*End of design draft. Marking up welcome — comment in-line or in a companion file.*
