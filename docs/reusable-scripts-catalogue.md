# Reusable Scripts & Report Generators — canonical catalogue

> The **non-task-specific** scripts that should be **reused** (not recreated) for consistency. Created 2026-06-14. Referenced from `docs/project-orientation-core-memory-map.md`.
>
> **Three governing rules:**
> 1. **Reuse, don't recreate.** Check this catalogue (and `python scripts/build_file_manifest.py --search "..."`) *before* writing a new generator. Recreating an existing report wastes time and forks the logic.
> 2. **Comparability — never silently change a report's shape.** If a report's format/columns/scope must change, **version the script (`-vN`) and say so**, so a regenerated report is not mistaken for being comparable to prior ones. Changing a generator in place breaks longitudinal comparison the researcher relies on.
> 3. Read-only unless marked **✎** (modifies DB) / **✎NAS** (writes backups).
>
> ⚠ **Curation caveat:** the `scripts/` tree is sprawling (~150 cluster-related scripts, ~40 `_exploratory_*`, ~25 `_generate_cluster_*` variants) with **no canonical registry and no superseded-markers** — the same silent-supersession problem at the script level. Dated one-offs and `_exploratory_*` / `_check_*` / `_probe_*` / `_tmp_*` / `_assess_*` diagnostics are **not** listed here (they are per-task). A canonical, ideally DB-resident, **script registry is an open item**.

---

## Engine — `python -m engine.engine`
`--db-status` · `--migrate [--dry-run]` · `--check-locks` · `--clear-lock --registry=N` · `--mode=audit_word --registry=N` (ingest+sync+audit) · `--report --registry=N` · `--export-word --registry=N` · `--export-registry`

## Programme-level reports
| Script | Produces |
|---|---|
| `generate_programme_snapshot.py` | Markdown snapshot — registries, statuses, term/verse counts, clusters (`--registry-only`/`--strongs-only`/`--out`/`--date`) |
| `_generate_programme_report.py` | Comprehensive programme status report |
| `generate_registry_overview.py` | Registry overview JSON (RMG §6c.3) |

## Cluster reports & audit (current M-code model)
| Script | Produces |
|---|---|
| `audit_cluster_v1_20260601.py` | **The canonical reusable cluster auditor** (read-only; implements the audit aspect spec) |
| `generate_full_cluster_audit_v1_20260603.py` | Sweeps every *started* cluster through `audit_cluster()` |
| `generate_cluster_summary_v1_20260603.py` | Current per-cluster summary (status, counts) for the M-model |
| `build_cluster_findings_digest.py` | A cluster's active findings as a navigable digest (characteristic→sub-group→finding+cited verses) |
| `_generate_cluster_findings_report_v1_20260506.py` | Renders `cluster_finding` rows for a cluster |
| `_generate_cluster_overview_v1_20260508.py` | Programme-wide cluster overview (older — ⚠ may be superseded by `generate_cluster_summary`; confirm) |

## Word / registry extracts
| Script | Produces |
|---|---|
| `build_complete_extract.py` | Comprehensive 9-layer registry extract (`--scope full|final`) |
| `word_full_extract.py` | All DB records for a word |
| `_produce_registry_full_extract.py` | Every table linked to a registry (created 2026-06-14; `--registry`) |
| `_produce_vc_word_report.py` | Verse-Context word report for one registry |
| `export_word_json.py` | Word JSON export |
| `word_study_extract.py` | STEP pull, no DB write (`--word`, `--anchors`) |
| `generate_session_a_extract.py` | Session A extract |

## Schema / integrity / manifest
| Script | Produces |
|---|---|
| `export_database_schema.py` | Live schema → JSON (AI project reference) |
| `build_file_manifest.py` | Whole-tree file manifest (`--search`, `--stats`) |
| `_integrity_full_check.py` | Full DB integrity check — ⚠ **BUG: hardcodes the old Drive path `G:\My Drive\Bible_study_projects\...` (project moved off Drive 2026-06-03); points at the dead/stale DB — fix before use** |

## Correlation / dimension analytics
| Script | Produces |
|---|---|
| `build_correlation_extract.py` | Inter-word correlation scoring |
| `build_dimension_extract.py` | Dimension extracts (`--cluster`/`--pointers`/`--rootfamily`) |

## Reference-as-DB extract builders (M32–34 governance)
`build_reference_snapshot.py` · `build_rules_extract.py` · `build_vocab_extract.py` · `build_obs_catalogue_export.py` · `build_obs_catalogue_tiered_extract.py` · `build_file_patterns_extract.py` · `build_label_patterns_extract.py` · `build_patch_types_extract.py` · `build_programme_prose_extract.py` · `build_corpus_prose.py` · `build_session_a_prose.py`

## Process / pipeline (reusable; modifies state)
| Script | Action |
|---|---|
| `_apply_verse_read_meaning.py` ✎ | L2 verse-read = meaning (API, Sonnet 4.6; idempotent/resumable) |
| `_cc_verse_read.py` ✎ | CC-generation mode of the verse-read (Opus subscription) |
| `apply_session_patch.py` ✎ | Patch applicator (`--dry-run`) — the only sanctioned write path for Claude AI output |
| `backup_db_to_nas.py` ✎NAS | Daily DB backup to NAS |
| `mirror_to_nas.ps1` ✎NAS | Daily full folder + memory mirror to NAS |

## `scripts/analytics/` library (import, not run)
`step_client.py` (STEP API) · `db_client.py` · `word_export.py` · `bible_analytics.py` · `zotero_client.py`

---

## Issues surfaced 2026-06-14 (errors & omissions)
1. **`_integrity_full_check.py` points at the old Google-Drive DB path** — a reusable "common operation" (CLAUDE.md §11) that would check the dead/stale Drive copy, not the live `database/bible_research.db`. **Concrete bug — fix the path.**
2. **No canonical script registry + heavy proliferation.** ~25 `_generate_cluster_*` and ~40 `_exploratory_*` variants, dated, with no "this is current" / superseded markers. → **open item:** a DB-resident or single-doc script registry (this catalogue is the start).
3. **Comparability risk (your concern b).** Several report types have multiple dated variants; without a canonical marker, a regenerated report can differ in shape from a prior one assumed comparable. The fix is rule 2 above — version on change, never mutate in place.
