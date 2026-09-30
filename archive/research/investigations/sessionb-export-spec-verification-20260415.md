# Session B Export Spec v1.1 — CC Verification Report

> Date: 2026-04-15
> Spec: `data/imports/WA/Patches/wa-global-sessionb-export-spec-v1_1-20260415.json`
> Status: **Exploratory** — for AI feedback. Not incorporated into production.
> Sample export: `data/exports/sessionb_spec_v1_1/wa-023-compassion-sessionb-export-v2-20260415.json` (123 KB)
> New script: `scripts/_exploratory_sessionb_export_v1_20260415.py` (production `analytics/word_export.py` left untouched)

---

## 1. Overall Result

The full spec was implemented in a new exploratory script and successfully produced an export for registry 023 (compassion). All 17 spec sections are populated where data exists. Several gaps and one schema question were surfaced — see §5.

| CV Task | Status | Outcome |
|---------|--------|---------|
| **CV-001** | Done | `word_export.py` covers ~40% of the spec. 9 sections missing entirely; 4 sections partial. See §2. |
| **CV-002** | Done | Correlation signals are in a **separate file** at `data/exports/session_d/wa-correlations-{date}.json`. Per-registry slice extracted. See §3. |
| **CV-003** | Done | All 24 statistics in the spec are producible from the database. The exploratory script computes them all. See §4. |
| **CV-004** | Done | Sample export for compassion produced — 123 KB, covers all 17 sections. See §5 for what surfaced. |

---

## 2. CV-001 — word_export.py vs Spec Coverage

`analytics/word_export.py` (483 lines) was written before the 2026-04-15 schema changes and does not implement the v1.1 spec.

### 2.1 Sections present and complete

| Spec section | word_export.py status |
|--------------|---------------------|
| meta (`_export`) | Present — but missing `export_version`, `export_date`, `instruction_version`, `registry_no` (uses `registry`, `word`, `scope`, `exported_at`, `schema_version`) |
| registry | Present — full row dump |
| file_index (`files`) | Present — full row dump |
| terms.active_terms (mostly) | Present — but no OWNER/XREF separation; mti embedded as `term["mti"]` rather than denormalised top-level fields |
| patch_history.engine_runs | Present — limited to mode='SESSION_PATCH' |
| run_history (`word_run_state`) | Present |
| cross_registry_links | Present |

### 2.2 Sections partial / wrong shape

| Spec section | Gap |
|--------------|-----|
| terms (no separation) | Active and deleted terms returned as one flat list. Spec requires explicit `active_terms` / `deleted_terms` partition. |
| terms (mti shape) | Spec wants `mti_term_id`, `mti_status`, `mti_gloss`, `owning_registry_no`, `owning_registry_word` denormalised onto the term. Current export nests them under `term["mti"]`. |
| terms (mti_flags) | Present but only emits `flag_code`, no description or flag_id. |
| session_research_flags | Present but flat list — spec requires split by `session_target` (B vs D vs other) and `category` lookup from `wa_quality_flag_types`. |
| statistics | Only 15 of 24 fields. Missing: OWNER/XREF/null breakdown, group counts, dim/dom_subject completeness, thin_evidence, gas/somatic consistency, sb_dimensions, root_family_gap. |

### 2.3 Sections missing entirely

| Spec section | Status in word_export.py |
|--------------|------------------------|
| **terms.deleted_terms** (separate) | Not separated |
| **verse_records_summary** | Per-term aggregates not produced (full verse rows are emitted at term level instead) |
| **verse_context_groups** | Entirely missing — no verse_context, verse_context_group, or wa_dimension_index reads |
| **set_aside_verses** | Entirely missing |
| **session_b_findings** | Entirely missing — no read of wa_session_b_findings (incl. 9 new lifecycle fields from 2026-04-15) |
| **finding_entity_links** | Entirely missing — new table from 2026-04-15 |
| **session_b_dimensions** | Entirely missing |
| **dimension_review_log** | Entirely missing — no read of wa_dim_review_cluster_log |
| **correlation_signals** | Entirely missing |

### 2.4 Approximate coverage

| Status | Sections | Approx. coverage |
|--------|----------|-----------------:|
| Present and matches spec | 7 | ~40% |
| Partial / wrong shape | 5 | ~20% |
| Missing entirely | 9 | ~40% |

**Verdict:** The current `word_export.py` is a Phase 1 exporter — it produces the data needed for engine audits and basic word reports, but it does not produce the analytical-input shape Session B v5.0 requires. A new export (this exploratory script, when finalised) is needed before Session B v5.0 can run.

---

## 3. CV-002 — Correlation Signals Source

**Answer: Separate file, programme-wide.**

### 3.1 Source

| Item | Value |
|------|-------|
| File | `data/exports/session_d/wa-correlations-{date}.json` |
| Latest | `wa-correlations-2026-04-09.json` (852 KB) |
| Producer | `scripts/build_correlation_extract.py` |
| Per-registry or programme-wide? | Programme-wide |

### 3.2 Structure

```
{
  "_extract_meta": {extract_type, produced_date, produced_at, produced_by, description},
  "statistics": {xref_pairs_above_threshold, cooccurrence_pairs_above_threshold,
                 dimension_overlap_pairs, root_family_connections, shared_anchor_verses,
                 total_composite_pairs, multi_signal_pairs, thresholds},
  "ranked_pairs": [200 items],
  "signals": {
    "xref_sharing":       [pairs with reg1, word1, reg2, word2, shared_terms, shared_strongs],
    "verse_cooccurrence": [pairs],
    "dimension_overlap":  [pairs],
    "root_families":      [pairs],
    "shared_anchor_verses": [pairs]
  }
}
```

### 3.3 Per-registry slice for compassion (registry 23)

The exploratory script slices the file at export time and embeds the result in the export under `correlation_signals.slice`:

| Signal | Pairs touching reg 23 |
|--------|---------------------:|
| ranked_pairs (top-200 composite) | 2 |
| xref_sharing | 16 |
| verse_cooccurrence | 3 |
| dimension_overlap | 0 |
| root_families | 0 |
| shared_anchor_verses | 28 |

### 3.4 Recommendation for spec

The spec section `correlation_signals.status` was marked "TBC". Confirmed:

> **The export embeds a per-registry slice of the programme-wide correlations file at export time.** Pass 6 receives the slice via the export — no separate file attachment needed at session start. The slice carries the freshness date from `_extract_meta.produced_date` so Session B can verify it is current.

If the correlation file is older than X days (suggest 14), the export should warn or refuse — the freshness gate is currently not enforced.

---

## 4. CV-003 — Statistics Block Producibility

**Answer: All 24 statistics are producible from the database. The exploratory script computes them all.**

Sample output for compassion (registry 023):

| Statistic | Value | Spec rule |
|-----------|------:|-----------|
| active_owner_term_count | 9 | — |
| active_xref_term_count | 0 | — |
| null_owner_type_count | 0 | "Should be 0" — ✅ |
| deleted_term_count | 89 | — |
| total_anchor_verses | 11 | — |
| total_related_verses | 13 | — |
| total_set_aside_verses | 49 | — |
| active_group_count | 9 | — |
| groups_without_dimension | 0 | "Should be 0 before Stage 2" — ✅ |
| groups_at_automated_confidence | 0 | "Should be 0 before Stage 2" — ✅ |
| groups_without_dominant_subject | 0 | "Should be 0 before Stage 2" — ✅ |
| terms_without_meaning_parse | 0 | "Should be 0" — ✅ |
| terms_without_mti_cross_refs | 8 | Note if unexpected — ⚠ 8/9 OWNER terms lack cross-refs |
| active_session_b_findings | 1 | — |
| thin_evidence_findings | 0 | "Must be 0 at session close" — ✅ |
| session_b_flags_unresolved | 1 | "Must be 0 at Stage 2 close" — ⚠ |
| sd_pointers_raised | 33 | — |
| phase2_flags_total | 3 | — |
| god_as_subject_inventory_count | 0 | — |
| god_as_subject_mti_flag_count | 4 | "Should equal inventory count" — ⚠ INCONSISTENT |
| somatic_link_inventory_count | 0 | — |
| somatic_link_mti_flag_count | 0 | "Should equal inventory count" — ✅ |
| session_b_dimensions_rows | 0 | "Expected 0 for most registries" — ✅ |
| root_family_gap_count | 0 | — |

### 4.1 Stage 1 audit findings surfaced for compassion

The statistics block immediately surfaces three issues:

1. **god_as_subject inconsistency:** 4 mti_term_flag rows assert GOD_AS_SUBJECT but `wa_term_inventory.god_as_subject = 0` for all of them. This is exactly the kind of consistency check the spec calls out (§terms.audit_notes.god_as_subject) — Stage 1 must raise a corrective patch.
2. **terms_without_mti_cross_refs = 8 of 9 OWNER terms:** Only 1 OWNER term has cross-refs. May indicate gap G-13 (root family completeness) or that compassion's terms genuinely have few cross-refs. Worth Session B noting.
3. **session_b_flags_unresolved = 1:** One session_target=B flag is open. Stage 2 cannot close until resolved.

These are all detectable without reading any verse data — just from the statistics block. The spec's design works.

---

## 5. CV-004 — Sample Export for Registry 023

### 5.1 File produced

| Item | Value |
|------|-------|
| Path | `data/exports/sessionb_spec_v1_1/wa-023-compassion-sessionb-export-v2-20260415.json` |
| Size | 123 KB |
| Sections | 17 (all spec sections) |

### 5.2 Section counts

| Section | Count |
|---------|------:|
| active_terms | 9 |
| deleted_terms | 89 |
| verse_context_groups | 9 |
| anchor_verses (across groups) | 11 |
| related_verses (across groups) | 13 |
| set_aside_verses | 49 |
| session_b_findings | 1 |
| finding_entity_links | 0 (new table empty) |
| session_b_dimensions | 0 |
| session_research_flags.session_b_flags | 1 |
| session_research_flags.sd_pointers | 33 |
| cross_registry_links | 0 (compassion is target-side, not source-side) |
| correlation_signals (cross-references) | 49 (across 5 signal types) |

### 5.3 Issues for AI to consider

**Naming and identity:**
- The spec's `meta.export_version` ("INTEGER auto-incremented per day") is not yet implemented as a discovery + increment — the script accepts `--version` from CLI. Production should auto-increment by scanning existing same-day exports.
- Filename pattern from spec is `data/exports/{word}_{registry}_full_{YYYYMMDD}_v{N}.json`. Exploratory script uses `wa-{NNN}-{word}-sessionb-export-v{N}-{date}.json` for clarity. **Recommend the spec adopt the wa- prefix pattern for consistency with other Session B outputs.**

**File index for OWNER vs XREF:**
- The spec says OWNER terms are the analytical set. Compassion has 0 XREF terms in this export — possibly because XREF terms have `delete_flagged=1` per the OWNER/XREF architecture. Worth confirming whether XREF terms should be surfaced separately (they do exist in mti_terms with status='extracted' but their wa_term_inventory rows are deleted-flagged).

**Compassion's 89 deleted terms:**
- This is a striking number. Many likely come from the audit_word filter for HIGH_FREQUENCY_ANCHOR or function-word contamination, but the high count warrants Stage 1 review. The export includes the full deleted_terms list with phase2_flags so Session B can assess each.

**Anchor verse text:**
- The export includes `verse_text` for anchor verses but NOT for related verses (related verses just have `reference` for brevity). Spec is ambiguous on this — it says related verses are "not primary reading material" but doesn't explicitly say to omit verse_text. **Recommend adding verse_text to related_verses for completeness** (small size impact since most groups have <10 related verses).

**Session A deleted/superseded terms still carrying phase2 flags:**
- Per the 2026-04-13 phase2_flags assessment (99% unverifiable), many deleted terms in this export carry phase2_flags. The spec says Session B "assesses each as irrelevant and notes in observations log". The export correctly includes these for review.

---

## 6. Schema Change Proposals

The spec implementation surfaced no NEW schema gaps that would require additional ALTER TABLE work. However, it raised these observations:

### 6.1 No schema changes required

The 2026-04-15 directives already added all fields the spec depends on:
- `wa_session_b_findings` lifecycle fields ✅
- `wa_finding_entity_links` table ✅
- `wa_quality_flag_types.category` for session_research_flags lookup ✅

### 6.2 Latent schema observations (not blocking)

| Observation | Suggested action |
|-------------|------------------|
| `wa_session_b_dimensions` is near-unused (2 rows programme-wide) but the spec retains it as a consistency check target. Could be retired once Session D synthesis confirms `wa_dimension_index` is the only source of truth. | Defer until Session D maturity |
| `wa_dimension_index.last_modified` is the only timestamp on the dimension assignment — no `created_at`. The spec audit asks Session B to verify confidence is at CLAUDE_AI or RESEARCHER. A `created_at` would help distinguish auto-promoted vs human-promoted assignments. | Optional — add `created_at` if Stage 1 audits show value |
| Correlation file freshness gate — there is no schema mechanism to enforce that an export embeds a current correlation slice. | Process control rather than schema — handle in export script, not DB |
| `wa_term_inventory.god_as_subject` and `somatic_link` are SUPERSEDED but still populated and used for consistency checks. The 0-vs-4 inconsistency on compassion shows the consistency check is meaningful. **Recommend not deprecating these fields yet** — they are the only way Session B can detect the bulk_patch error class. | Keep fields; document as "consistency-check only, do not write" |

### 6.3 One question for AI

The spec's `correlation_signals.status` says "TBC — CC to confirm". I have confirmed:
- Source: external file `data/exports/session_d/wa-correlations-{date}.json`
- Embedded as per-registry slice in the export
- Source date carried in `_extract_meta.produced_date`

**Question:** Should the export REFUSE to produce if the correlation file is older than N days? Currently the script just warns. Suggest N=14 days for Session B work. This would be a guard-rail, not a schema change.

---

## 7. Next Steps (proposed)

1. **AI feedback loop:** Send the exploratory export `wa-023-compassion-sessionb-export-v2-20260415.json` to AI for review. Confirm it covers everything Session B v5.0 needs.
2. **Spec refinements** (if any): Update `wa-global-sessionb-export-spec-v1.1-20260415.json` based on AI feedback. Possible refinements:
   - Adopt wa- prefix filename pattern
   - Clarify whether related_verses should include verse_text
   - Confirm correlation freshness gate days
3. **Promotion to production:** When spec is final, either (a) extend `analytics/word_export.py` to match the new spec, or (b) replace it with the exploratory script (renamed appropriately and tested). Update `scripts/export_word_json.py` CLI wrapper accordingly.
4. **Engine integration:** Update `engine/engine.py` `--export-word` mode to use the new export.
5. **Update `apply_session_patch.py`:** This is the open loop from yesterday — when the new export is in production, the patch applicator must be able to write back the 9 new finding lifecycle fields and the entity-link inserts.

---

*Exploratory artefacts:*
- *Script: `scripts/_exploratory_sessionb_export_v1_20260415.py`*
- *Sample export: `data/exports/sessionb_spec_v1_1/wa-023-compassion-sessionb-export-v2-20260415.json`*
- *This summary: `outputs/investigations/sessionb-export-spec-verification-20260415.md`*
