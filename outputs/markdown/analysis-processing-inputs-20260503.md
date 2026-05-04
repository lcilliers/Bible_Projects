# Analytic Processing — Input Tables & Fields

**Date:** 2026-05-03
**Scope:** What the DB hands to AI at the start of a Stage 2 session — every table and field that flows into the three input `.md` artefacts (readiness output, validation report, analytic status). Built by tracing the SQL in [_pilot_build_readiness_output_v2_20260426.py](../../scripts/_pilot_build_readiness_output_v2_20260426.py), [_pilot_validate_readiness_v1_20260427.py](../../scripts/_pilot_validate_readiness_v1_20260427.py), and [_pilot_build_analytic_status_v1_20260427.py](../../scripts/_pilot_build_analytic_status_v1_20260427.py).

**Companion brief:** [analysis-processing-focus-20260503.md](analysis-processing-focus-20260503.md) — pipeline overview.

---

## 1. Inputs at a glance

| Input `.md` (+ paired `.json`) | Builder script | Folder | Used in |
|---|---|---|---|
| Readiness output | `_pilot_build_readiness_output_v2_*.py` | `Sessions/Session_B/07_Analysis_Readiness_Status/` | Every Stage 2 session |
| Validation report | `_pilot_validate_readiness_v1_*.py` | same folder | Every Stage 2 session — gate (READY/BLOCKED) |
| Analytic status | `_pilot_build_analytic_status_v1_*.py` | same folder (per v1.10 instruction) | Revision sessions only |

---

## 2. Readiness output — section-by-section table & field map

The readiness output has **14 sections** (A–N + M). Each section has a defined source set in the DB. The table below traces every query in [build()](../../scripts/_pilot_build_readiness_output_v2_20260426.py).

### §A — Registry overview *(Unit 1)*

**Source:** `word_registry` (single row, `WHERE no = ?`).

**Fields read:** `id`, `no`, `word`, `verse_context_status`, `session_b_status`, `dim_review_status`, `dim_review_version`, `cluster_assignment`, `sb_classification`, `sb_classification_reasoning`, `carry_forward`, **`inference_note`** (verbatim quote), **`word_synopsis`** (verbatim quote), `description`, `dimensions`, `phase1_status`, `phase1_term_count`, `phase1_verse_count`.

**Also surfaced inline:** counts of open flags (§H) and existing findings (§H).

---

### §B — Stage 1 Completion Record *(synthesised)*

**Source:** Re-uses §A registry row, OWNER terms (§C), and `schema_version` (latest `version_code`).

**Derived facts:**
- OWNER `md_version` set distinct (`mti_terms.md_version` per OWNER) — the project's audit equivalent of `meta.export_version`.
- `vc_completed` count vs total OWNER terms.
- Legacy-VC count (`vc_status IN ('not_done','to_revise')`).
- Seven-domain pass status table (Data completeness · VC completeness · Group integrity · Verse coverage · Cross-registry · Flag closure · Researcher fields).

---

### §C — OWNER term inventory *(Unit 1 prep)*

**Sources:**
- `mti_terms` JOIN `wa_term_inventory` JOIN `wa_file_index` (filter `term_owner_type='OWNER'`, not `delete_flagged`, not `status IN ('delete','excluded')`).
- Per OWNER: `wa_verse_records`, `verse_context_group`, `verse_context` (counts) — see `get_term_state()`.

**Fields per row:** `mt.id` (mti) · `strongs_number` · `transliteration` · `gloss` · `language` · `status` · `vc_status` · `md_version` · `anchor_note` · `ti.id` (ti_id).

**Computed counts per term (subquery columns in `get_term_state`):**
- `verses_active` / `verses_deleted` — `wa_verse_records WHERE term_inv_id = ? AND delete_flagged = 0|1`
- `groups_active` / `groups_dissolved` — `verse_context_group WHERE mti_term_id = ?`
- `vc_rows_active` — `verse_context WHERE mti_term_id = ? AND delete_flagged=0`
- `vc_relevant` — same + `is_relevant=1`
- `vc_set_aside` — same + `is_relevant=0 AND set_aside_reason IS NOT NULL`
- `anchor_count` — same + `is_anchor=1`

---

### §D — OWNER lexical foundation *(Unit 3)*

**Sources (per term, via `get_term_lexical()`):**

| Table | Fields read |
|---|---|
| `wa_meaning_parsed` | `id`, `top_sense_count`, `stem_count`, `has_causative_stem`, `has_domain_tags`, `parsed_at`, `parse_version` |
| `wa_meaning_sense` (FK `parsed_meaning_id`) | `level_code`, `level_depth`, `parent_level_code`, `sense_text`, `is_stem_label`, `stem_label`, `domain_tag`, `sort_order` |
| `wa_meaning_stem` | `stem_name`, `stem_type`, `sense_count`, `top_sense_text` |
| `wa_term_root_family` | `root_code`, `root_language`, `root_gloss`, `note` (LIMIT 5) |
| `wa_term_related_words` | `strongs_number`, `transliteration`, `gloss`, `relationship_note` (LIMIT 30 + total count) |
| `wa_lsj_parsed` | `lsj_gloss`, `lsj_domains`, `lsj_philosophical_note`, `lsj_etymology_note`, `lsj_cognate_forms`, `raw_lsj` |

When `wa_meaning_parsed` is absent the section explicitly notes the gap; same for missing LSJ on Greek terms.

---

### §E — XREF terms *(Unit 2)*

**Source:** `mti_terms` JOIN `wa_term_inventory` (filter `term_owner_type='XREF'`).

**Fields per row:** `mti`, `strongs_number`, `transliteration`, `gloss`, `language`, `status`, `vc_status`, `ti_id`.

**Two correlated subqueries per row:**
- `owner_registry` — `wr.no || ' ' || wr.word` for the registry that OWNs this Strong's.
- `owner_verse_count` — verse count on the OWNER copy.

---

### §F — Verse Context Group landscape *(Unit 4)*

**Source:** `verse_context_group` LEFT JOIN `wa_dimension_index` (per OWNER mti_term).

**Fields per group:** `vcg.id`, `group_code`, `context_description`, `notes`, plus computed `rel_n` (relevant count) and `anchor_n` (anchor count) from `verse_context`.

**From `wa_dimension_index`:** `dimension`, `cluster_assignment`. The dimension assignment is the analytical lens AI applies in Unit 4.

---

### §G — Correlation signals *(Unit 5; computed)*

Three multi-table aggregations across all OWNER mti_term ids (`get_correlation_signals()`):

| Signal | Tables joined | Output fields |
|---|---|---|
| **G.1 XREF sharing** | `mti_terms` ↔ `wa_term_inventory` (XREF) ↔ `wa_file_index` ↔ `word_registry` | `reg_no`, `reg_word`, `shared_terms`, `strongs_list` |
| **G.2 Verse co-occurrence** | `verse_context` ↔ `wa_verse_records` (self-join on book/chap/verse) ↔ `wa_term_inventory` (OWNER) ↔ `wa_file_index` ↔ `word_registry` ↔ second `verse_context` (`is_relevant=1`) — HAVING `shared_verses ≥ 3`, LIMIT 25 | `reg_no`, `reg_word`, `shared_verses` |
| **G.3 Shared anchors** | Same chain, both sides constrained to `is_anchor=1` | `reg_no`, `reg_word`, `verse_ref`, `n` |

These signals do not exist in any single table — they are computed at generation time and feed the §G "no signals at threshold" or top-N tables.

---

### §H — Existing SD pointers + findings *(Units 6 + 9)*

**H.1 — `wa_session_b_findings`** (`get_session_b_findings()`):
Read `id`, **`finding_id`** (the `OBS-NNN-seq` / `SP-NNN-seq` style label), `finding_type`, `finding`, `anchor_verses`, `raised_date`, `status`, `thin_evidence`, `session_b_instruction`, `pass_ref`, `study_segment`, `obsolete_reason`, `superseded_by_id`, `related_finding_id`, `resolution_note`, `term_id`. Filter: `registry_id = ? AND (delete_flag = 0 OR delete_flag IS NULL)`.

**H.2 — `wa_session_research_flags`** (`get_open_flags()`):
Read `flag_code`, `flag_label`, `priority`, `session_target`, `raised_date`, `session_raised`, `description`. Filter: `(resolved = 0 OR resolved IS NULL)`.

---

### §I — Thin-evidence phase2 flags *(Unit 8)*

**Source:** `wa_term_phase2_flags` LEFT JOIN `wa_quality_flag_types`.

**Fields per term:** `flag_id`, `description`, `source`, `raised_date`, `flag_code`, flag-type `description`. Filter: `term_inv_id = ?` per OWNER, not `delete_flagged`.

---

### §J — Anchor verse material — verbatim verse text *(Unit 7 — primary analytical input)*

**Source (per term, via `get_term_verses()`):**
`wa_verse_records vr` LEFT JOIN `verse_context vc` (`mti_term_id = ?`) LEFT JOIN `verse_context_group g`.

**Fields per row:** From `wa_verse_records`: `id` (vr_id), `book_id`, `chapter`, `verse_num`, **`reference`**, **`verse_text`**, `target_word`, `span_strong_match`. From `verse_context`: `id`, `is_relevant`, `is_anchor`, `is_related`, `set_aside_reason`, `notes`. From `verse_context_group`: `group_code`.

**Render contract:**
- Group by `group_code` (with `SET-ASIDE` and `UNCLASSIFIED` buckets).
- Anchor verses marked 🔵 and sorted first.
- Full verbatim `verse_text` blockquoted; `set_aside_reason` and `target_word` annotated; group-level anchor list summarised.

This is the largest section and the analytical core of the package.

---

### §K — Legacy-VC notice *(v2 corrective strategy)*

**Source:** Filtered subset of OWNER terms where `vc_status IN ('not_done','to_revise')` from §C state.

**Fields surfaced:** `strongs_number`, `gloss`, `vc_status`, plus state counts (`verses_active`, `groups_active`, `vc_rows_active`).

The instruction text mandates the `ANALYSIS_VC_UNVERIFIED_MATERIAL` flag if any finding depends materially on a legacy-VC term.

---

### §L — Stage 2b foundational input — second-tier catalogue *(T0–T7, 189 prompts)*

**Source:** `wa_obs_question_catalogue` filtered to `tier IS NOT NULL AND status='active' AND (deleted=0 OR deleted IS NULL)`.

**Fields per prompt:** `obs_id`, `question_code`, `section`, `tier`, `component_code`, `component_title`, `prompt_seq`, `source_word`, `source_registry_no`, `question_text`, `pattern_type`, `scope`, `status`.

**Embedded as JSON** under §L grouped tier → component → prompts. Catalogue version stamp: `v2-2026-04-29`.

**Plus registry-specific extensions:** same table filtered to `tier IS NULL AND source_registry_no = ?` (word-specific GAP/extension prompts that have been carried into the catalogue).

---

### §N — Open Session B Items *(must resolve this session)*

**Source:** `wa_session_b_findings WHERE registry_id = ? AND status = 'open' AND (delete_flag=0 OR delete_flag IS NULL)`.

**Fields per item:** `id`, `finding_id`, `finding_type`, `finding`, `anchor_verses`, `raised_date`, `status`, `thin_evidence`, `term_id`, `session_b_instruction`, `pass_ref`.

**Each item must reach one of four outcomes by session close:** Q&A resolution → SD pointer → new GAP question → not_relevant.

---

### §M — Readiness verification *(self-check)*

Reads back: registry status fields populated (`verse_context_status` / `session_b_status`), OWNER inventory non-empty, all OWNER terms have ≥1 active verse, researcher fields present. Surfaces concerns inline (e.g. `session_b_status='Verse Context Reset'`, `dim_review_status NULL`).

---

## 3. Validation report — what gets checked against what

[_pilot_validate_readiness_v1_20260427.py](../../scripts/_pilot_validate_readiness_v1_20260427.py) — 15 checks, READY/BLOCKED gate.

| ID | Tables / fields read | Verdict |
|---|---|---|
| C01 | `schema_version.version_code` (latest) | FAIL if < `3.17.0` |
| C02 | `word_registry.last_automation_run` | WARN if not `'AUDITED'` |
| C03 | `word_registry.phase1_status` | FAIL if not `'Complete'` |
| C04 | `word_registry.verse_context_status` | FAIL if not `'Complete'` |
| C05 | `word_registry.dim_review_status`, `dim_review_version` | FAIL if not `'Complete'` |
| C06 | `prose_section` JOIN `prose_section_type` (`source_stage='session_a'`, `superseded_by_id IS NULL`) — expects 6 rows: `sa_s1_d1`..`sa_s1_d6` | FAIL if < 6 |
| C07 | Filesystem: `Sessions/Session_B/07_Analysis_Readiness_Status/wa-{NNN}-{word}-readiness-output-v*.{md,json}` | FAIL if missing |
| C08 | `mti_terms` ↔ `wa_term_inventory` (OWNER) ↔ `wa_file_index` ↔ `wa_verse_records` (count per term) | FAIL if no OWNER terms; WARN if any zero-verse term |
| C09 | `verse_context_group` LEFT JOIN `wa_dimension_index.dimension` | FAIL if any group lacks dimension |
| C10 | `wa_dimension_index.anchor_count` per group | WARN if any group has 0 anchors |
| C11 | `wa_dimension_index.{anchor_count, related_count, set_aside_count, total_verse_count}` per group | WARN if any `set_aside / total > 0.90` |
| C12 | `mti_terms.vc_status` per OWNER | WARN if all `not_done` (legacy-VC) or mixed |
| C13 | `wa_dimension_index.dimension_confidence` per group | WARN if any `'queried'` or no `'confirmed'` |
| C14 | `wa_session_b_findings WHERE finding_type LIKE 'DATA_ANOMALY_%' AND status='open'` | FAIL if any |
| C15 | `word_registry.inference_note`, `word_registry.word_synopsis` | WARN if either absent |

The validation report's `.json` payload carries `meta`, `verdict_summary` (PASS/WARN/FAIL counts), `overall` (READY/BLOCKED), and per-check `{id, label, category, verdict, detail}`.

---

## 4. Analytic status — additional inputs for revision sessions

[_pilot_build_analytic_status_v1_20260427.py](../../scripts/_pilot_build_analytic_status_v1_20260427.py) sources prior analytical state. Six sections, each backed by a specific table or join.

| Section | Tables | Fields read |
|---|---|---|
| §1 Lifecycle summary | `wa_session_b_findings` (GROUP BY `status`) + `wa_obs_question_catalogue` (universal count) + `wa_finding_catalogue_links` (GROUP BY `coverage`) | finding `status` counts; catalogue universal total; per-coverage counts |
| §2 Resolved Q&A | `wa_session_b_findings` JOIN `wa_finding_catalogue_links` JOIN `wa_obs_question_catalogue` | `finding_id` (label), `finding`, `raised_date`, `term_id`, `coverage`, **`session_b_note`** (the answer body), `validated_date`, `obs_id`, `question_code`, `section`, `question_text` |
| §3 Resolved SD pointers | `wa_session_b_findings` LEFT JOIN `wa_session_research_flags` (`flag_code='SD_POINTER'`, FK on `related_finding_id`) | `finding_id`, `finding`, `flag_label`, `priority`, `description` |
| §4 Not-relevant | `wa_session_b_findings WHERE status='not_relevant'` | `finding_id`, `finding_type`, `finding`, `obsolete_reason`, `raised_date`, `obsolete_date` |
| §5 Stage 2c chapters (legacy / pre-v1.8) | `prose_section` JOIN `prose_section_type` (`code LIKE 'sb_s2c_%'`) | `id`, `heading`, `body`, `version`, `author`, `created_at`, type `code`, type `label` |
| §6 Anchor verse analytical notes | `verse_context vc` JOIN `verse_context_group g` JOIN `wa_verse_records vr` JOIN `mti_terms mt` JOIN `wa_term_inventory ti` (OWNER) JOIN `wa_file_index fi` — `WHERE vc.analysis_note IS NOT NULL` | `vc_id`, `mti_term_id`, `verse_record_id`, **`analysis_note`**, `is_anchor`, `is_relevant`, `group_code`, `reference`, `strongs_number` |
| §7 Open items | `wa_session_b_findings WHERE status='open'` | `id`, `finding_id`, `finding_type`, `finding`, `raised_date`, `term_id` (mirrors §N of readiness output for redundancy) |

---

## 5. Master table-by-table summary

What every Stage 2 input ultimately reads from:

| Table | Read by readiness | Read by validation | Read by analytic status |
|---|:-:|:-:|:-:|
| `word_registry` | §A, §B, §M | C02–C05, C15 | §1 |
| `schema_version` | §B, §M | C01 | — |
| `mti_terms` | §C, §D, §E | C08, C12 | §6 |
| `wa_term_inventory` | §C, §D, §E (joins) | C08, C12 (joins) | §6 (joins) |
| `wa_file_index` | (joins) | (joins) | (joins) |
| `wa_verse_records` | §C state, §J (verbatim text) | C08 | §6 (joins) |
| `verse_context` | §C state, §F counts, §J | — | §6 |
| `verse_context_group` | §C state, §F | C09, C10 | §6 |
| `wa_dimension_index` | §F | C09–C11, C13 | — |
| `wa_meaning_parsed` / `_sense` / `_stem` | §D | — | — |
| `wa_term_root_family` | §D | — | — |
| `wa_term_related_words` | §D | — | — |
| `wa_lsj_parsed` | §D | — | — |
| `wa_term_phase2_flags` | §I | — | — |
| `wa_quality_flag_types` | §I (lookup) | — | — |
| `wa_session_b_findings` | §A counts, §H, §N | C14 | §1, §2, §3, §4, §7 |
| `wa_session_research_flags` | §H | — | §3 |
| `wa_finding_catalogue_links` | — | — | §1, §2 |
| `wa_obs_question_catalogue` | §L (T0–T7 + extensions) | — | §1, §2 |
| `prose_section` / `_type` | — | C06 (Phase A only) | §5 |

**Tables consciously NOT read at session start:** `prose_section_fts` (FTS index, not source-of-truth); engine control tables (`engine_run_log`, `word_run_state`, `term_fetch_log`); `mti_term_flags` / `mti_term_cross_refs`; `session_d_*`; `wa_obs_question_catalogue` rows with `status='redundant_v1'` (the retired generic catalogue).

---

## 6. Key derived signals AI can rely on

Things AI sees in the inputs that are not raw fields but computed:

- **§B seven-domain pass status** — synthesised from registry + OWNER state (not stored).
- **§G correlation signals** — three multi-registry aggregations computed at generation time.
- **§J grouped verse list with anchor markers** — re-shaped from `verse_context` + `wa_verse_records`.
- **§K legacy-VC subset** — derived from `mti_terms.vc_status`.
- **§L grouped catalogue payload** — restructured from flat `wa_obs_question_catalogue` rows to nested tier→component→prompts JSON.
- **§M readiness self-check booleans** — computed from registry + OWNER state.
- **Validation `verdict_summary` and `overall`** — computed by tallying the 15 checks.
- **Analytic status §1 lifecycle counts and coverage by `wa_finding_catalogue_links.coverage`** — GROUP BY aggregations.

These computed signals are not derivable from a single SELECT in the DB — re-running the builder is the only way to refresh them.

---

## 7. What the inputs do NOT include (worth knowing)

- **No raw `mti_term_flags`** rows (`mti_terms` row is shown but its flag children are not). If a flag matters for analysis it must reach AI through a finding or Phase 2 flag.
- **No T0–T7 prior Q&A answers** — those live in `wa_finding_catalogue_links.session_b_note` and reach AI only via the **analytic status** input on revision sessions, not via the readiness output.
- **No `verse_context.analysis_note` content** in the readiness output — it appears only in analytic status §6 (revision input). Initial Stage 2 sessions cannot see prior anchor analyses through the readiness `.md` alone.
- **No prose chapter bodies** in the readiness output — those appear only in analytic status §5 (revision input).
- **No `wa_dimension_index.review_state` / `dim_review_version` per group** — rendered only at registry level in §A; per-group dimension review provenance is not surfaced.

This is by design — the readiness output is the *current data state*, the analytic status is the *prior analytical state*. They serve different roles at session start.

---

*Built from: full read of `_pilot_build_readiness_output_v2_20260426.py` (1251 lines) and `_pilot_validate_readiness_v1_20260427.py` (489 lines); first 360 lines + structural skim of `_pilot_build_analytic_status_v1_20260427.py` (421 lines). Cross-checked against [wa-sessionb-analysis-readiness-v1_10](../../Workflow/Instructions/wa-sessionb-analysis-readiness-v1_10-20260501.md) §v2.R2 (14 sections) and [wa-sessionb-analysis-output-v1_8](../../Workflow/Instructions/wa-sessionb-analysis-output-v1_8-20260430.md) §1 (input contract).*
