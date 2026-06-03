# M-tables — which existing tables they depend on

**Date:** 2026-05-05
**Companion to:** [wa-db-architecture-decision-v1-20260505.md](wa-db-architecture-decision-v1-20260505.md) (Option B)
**Purpose:** identify which of the 64 existing tables become structural dependencies of the new `m_*` analytical layer (foreign-key targets or required-read sources), versus which are enrichment-only, reference-only, or dropped.

---

## 1. Proposed M-table set (recap)

| New table | What it holds |
|---|---|
| `m_cluster` | M01..M46 + T2 + FLAG identity (id, label, description, version) |
| `m_cluster_term` | term → M-cluster assignment + bucket (T1/T2/QUALIFIER/LOCUS) + cluster_source provenance |
| `m_term_verse_analysis` | per (term, verse) row: brief meaning reading, status, decision, set_aside_reason if any, group_ref if any |
| `m_cluster_relation` | cross-cluster claims, with anchor verse refs (e.g. M11 forgiveness → M05 love at Luk 7:47) |
| `m_term_status` | derived view (or table) — per-term coverage roll-up against `m_term_verse_analysis` |

---

## 2. Integral dependencies — TIER 1 (foreign-keyed or strictly required)

These are the tables the new schema **cannot operate without**. They become the canonical backbone of the new pipeline.

| Existing table | Used by | Role |
|---|---|---|
| **`mti_terms`** | `m_cluster_term`, `m_term_verse_analysis` | The Strong's master. Every M-cluster term row FKs here for `strongs_number`, `gloss`, `transliteration`, `language`. Non-negotiable. |
| **`wa_verse_records`** | `m_term_verse_analysis` | The canonical verse record (one row per term-occurrence-in-verse). Every analysis row FKs here for `reference`, `verse_text`, `book_id`, `chapter`, `verse_num`, `mti_term_id`. Non-negotiable. |
| **`books`** | (indirect) | All verse references resolve through `book_id`. Never queried directly by m_tables but verses depend on it. |

That's the irreducible core: **3 tables, ~237k rows, ~120 MB of the DB.** Everything else is either enrichment, reference, or dropped.

---

## 3. Enrichment dependencies — TIER 2 (read at construction or display time)

These are read by m_table-building scripts to populate term records and present analytical context. Not FK'd, but heavily used.

| Existing table | What it adds |
|---|---|
| **`wa_term_inventory`** | `meaning` text, `step_search_gloss`, `short_def_mounce`, `term_owner_type` (OWNER/XREF), `evidential_status`, `parsed_meaning_id`. Critical for showing the term-level meaning in analysis prompts. |
| **`wa_meaning_parsed`** + **`wa_meaning_sense`** | Structured sub-sense breakdown of each term's meaning. Used to brief Claude AI when classifying a verse's meaning of a term. |
| **`wa_verse_term_links`** | Span-level links (`step_subgloss_code`, `step_subgloss_label`, `target_word`). Useful when displaying *which exact span in the verse* the term occurs as. |
| **`wa_term_root_family`** | Root-family membership. Used for cross-cluster bridge analysis (e.g. M01 Hebrew yare-family ↔ M01 Greek phobos-family share root-class). |
| **`wa_term_related_words`** | Cognate/near-synonym pool. Useful for term-level discovery — "what other terms is this related to?" |
| **`mti_term_flags`** | Term-level flags (evidential, retention notes). |
| **`mti_term_cross_refs`** | Strong's-to-Strong's cross-references. |
| **`wa_file_index`** | Provenance — which STEP file the term/verse came from (audit trail only). |

These would not become FK targets in the new schema. They are **read-only sources** that feed analytical scripts. None of them needs to change for the new pipeline to work.

---

## 4. Reference-only — TIER 3 (legacy archive, occasional dipping)

These are the analytical outputs of the old pipeline. The researcher said: *"keep the existing findings and pointers as references and every now and then dip into it"*. They stay in the DB but are not in the new pipeline's path.

| Existing table | Why it's now reference-only |
|---|---|
| `verse_context` | Old verse-classification — partial / methodologically broken. Replaced by `m_term_verse_analysis`. |
| `verse_context_group` | Old contextual meaning groups — superseded by M-cluster/per-term grouping in the new layer. |
| `wa_session_b_findings` | Q&A findings — registry-scope shotgun, marginal value (per memory). Useful occasionally for cross-cluster claims. |
| `wa_session_research_flags` | SD pointers + flags — same as findings, marginal but contains anchor-verse signals worth dipping into. |
| `wa_finding_catalogue_links` | Q&A → catalogue question links — only meaningful within the old findings model. |
| `wa_finding_entity_links` | Finding → verse/group links — only meaningful within the old findings model. |
| `wa_dimension_index` | Dimensional classification — explicitly rejected by program reset. |
| `wa_dim_review_cluster_log` | Dimension review history — not relevant to new pipeline. |
| `wa_session_b_dimensions` | (2 rows) — vestigial. |
| `wa_data_quality_flags` | Engine-derived flags from old pipeline (~19k rows) — useful for term-level diagnostics if filtered. |
| `wa_obs_question_catalogue` | M31 observation catalogue — old methodology. |
| `prose_section` (+ FTS) | DB-canonical prose store (M20) — useful repository if cross-cluster prose is needed but not load-bearing for term-level work. |
| `wa_prose_section_citations` | Prose citation links — same. |
| `prose_section_dimension_link` / `prose_section_finding_link` | Empty. |
| `session_d_*` (4 tables) | Empty — never populated. |
| `phase2_flag_types`, `wa_term_phase2_flags` (1,570 rows) | Old phase-2 flag schema — unused in new pipeline. |
| `wa_quality_flag_types`, `wa_flag_type_question_link` | Quality-flag controlled vocab from old pipeline. |
| `wa_addendum_registry`, `wa_cross_registry_links`, `wa_crosslink_type` | Registry-level cross-linking — registry deprecated. |
| `wa_vocab_set`, `wa_vocab_member` | (~47 rows total) — old vocabulary control. |
| `word_registry` | Kept for **historical crosswalk** (legacy_cluster_id in m_cluster_term provenance) but no longer the analytical unit. |
| `wa_rule_registry`, `wa_patch_type_registry`, `wa_label_pattern`, `wa_file_name_pattern`, `book_code_variants` | Engine controlled vocabularies — keep for engine if it stays alive. |

---

## 5. Engine / control — separate concern

| Existing table | What it does |
|---|---|
| `engine_run_log`, `engine_stream_checkpoint`, `term_fetch_log`, `word_run_state` | Engine audit trail — only relevant if the engine continues running for STEP-ingest. |
| `schema_version` | Migration history — needs an entry for the new `m_*` schema (3.18.0 or similar). |

---

## 6. Visual relationship — what the new layer leans on

```
                        ┌────────────────────────┐
                        │      m_cluster         │
                        │ (M01..M46 + T2 + FLAG) │
                        └──────────┬─────────────┘
                                   │ 1:N
                                   ▼
                        ┌────────────────────────┐         ┌──────────────────┐
                        │   m_cluster_term       │ ───FK──▶│   mti_terms      │  ← TIER 1
                        │ (cluster, strong, …)   │         │  (Strong's master)│
                        └──────────┬─────────────┘         └──────────────────┘
                                   │ 1:N
                                   ▼
                        ┌────────────────────────┐         ┌──────────────────┐
                        │ m_term_verse_analysis  │ ───FK──▶│ wa_verse_records │  ← TIER 1
                        │ (term, verse, status, │         │  (verse + term)   │
                        │  meaning, decision)    │         └────────┬─────────┘
                        └──────────┬─────────────┘                  │ FK
                                   │                                 ▼
                                   │                       ┌──────────────────┐
                                   │                       │      books       │  ← TIER 1
                                   │                       └──────────────────┘
                                   │
                       (read at build/display time)
                                   │
                                   ▼
        ┌─────────────────────────────────────────────────┐
        │ TIER 2 ENRICHMENT (read-only, not FK'd)         │
        │   wa_term_inventory, wa_meaning_parsed,         │
        │   wa_meaning_sense, wa_verse_term_links,        │
        │   wa_term_root_family, wa_term_related_words,   │
        │   mti_term_flags, mti_term_cross_refs           │
        └─────────────────────────────────────────────────┘

  ── Below the line — not part of the new pipeline ──

        ┌─────────────────────────────────────────────────┐
        │ TIER 3 LEGACY (reference-only, occasional dips) │
        │   verse_context, verse_context_group,           │
        │   wa_session_b_findings, wa_session_research_   │
        │   flags, wa_dimension_index, wa_finding_*,      │
        │   prose_section, word_registry, …               │
        └─────────────────────────────────────────────────┘
```

---

## 7. Summary count

Of 64 existing tables:

| Tier | Count | What happens to them |
|---|---:|---|
| **TIER 1 — Integral (FK targets)** | **3** | `mti_terms`, `wa_verse_records`, `books`. Backbone. |
| **TIER 2 — Enrichment (read-only)** | **8** | Term + verse metadata. Read at build/display. |
| **TIER 3 — Legacy reference** | **~30** | Stay in DB, frozen, queryable by ad-hoc SQL only. |
| **Engine / control** | **~10** | Used only by engine — independent of new pipeline. |
| **Empty / vestigial** | **~5** | Could be dropped but harmless to leave. |

So the new analytical layer **structurally depends on 3 core tables and enriches against 8 more**. The remaining ~45 tables are not part of the new pipeline — they're either legacy archive, engine machinery, or empty.

---

## 8. Implication for engine + audit

The engine's `audit_word` mode writes to `wa_data_quality_flags`, `wa_term_phase2_flags`, etc. Under Option B, those tables become legacy.

Two paths:
- **Retire `audit_word` mode** entirely. The new pipeline doesn't need it; STEP-ingest validation can be a thinner script.
- **Keep `audit_word` for STEP-ingest only** — when fresh STEP data is loaded, run audit to populate flags and quality data. The new analytical layer ignores those flags.

Recommend **keep for STEP-ingest only** unless we're certain there will be no more STEP refreshes. Audit results stay in their legacy tables and don't pollute the new schema.

---

## 9. Decision sought (to advance)

If Option B is approved, the next concrete step is the **schema design pass** for the 5 `m_*` tables (column lists, types, indexes, FK constraints). That's a ~½ day exercise.

Before that, two small ratifications:

1. **Tier 1 = `mti_terms` + `wa_verse_records` + `books`** — confirm these are the structural dependencies (nothing else sneaks in).
2. **Tier 3 freeze** — agree that no new pipeline code writes to any Tier 3 table. Reads from Tier 3 are allowed only for "occasional dips" and must be explicit (no implicit joins).

Once those are confirmed, schema design is the next deliverable.
