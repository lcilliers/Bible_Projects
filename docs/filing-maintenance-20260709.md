# Filing maintenance — 2026-07-09

> Housekeeping pass over the whole tree against `docs/file-organisation-rules.md`. Records what was tidied and the two larger items that need a policy decision before action. Follows the 2026-06-14 `filing-audit`.

## Done this pass
| area | rule | action |
|---|---|---|
| **`outputs/` root** | §3.10 "nothing in `outputs/` root" | **17 loose files** (old VE-read `.txt`/`.log` run-logs + June tier/ve-status/verse-span extracts, all superseded) → `outputs/archive/`. Root now empty. |
| **`scripts/` `_tmp_`** | §3.13 / §4 | `_tmp_m10_charcond_validate.py` → `archive/scripts/`. |
| **`verse-analysis/` root** | §1 no files in roots | `wa-book-coverage-assessment-20260703.md` → `verse-analysis/_reports/`. |
| **`Workflow/` root** | §1 | `wa-archive-decisions-for-guidance-v1-20260607.md`, `wa-workflow-cleanup-register.md` → `Workflow/methodology/`. |
| **`verse-analysis/` book folders** | §3.0b | **Convention drift fixed.** Two conventions coexisted — short-codes (`Gen`,`Exo`,`Lev`,`Pro`,`Ecc`,`Jer`,`Deu`,`Mar`; 19 files total) and full names (`genesis`,`psalms`,`proverbs`…; ~1,200 files). Full-name is the real convention, so the 6 short-code **stubs were merged into their full-name folders** (no collisions), and `Deu`→`deuteronomy`, `Mar`→`mark` renamed. **Rule §3.0b updated** to full-lowercase-name (was stale "short_code"). |
| **`docs/` assessments** | §3.11 "not here: investigation outputs" | 3 **zero-reference** assessments → `research/investigations/`: `assessment-session-d-tables`, `assessment-wa-cross-registry-links`, `cluster-naming-assessment-20260521`. |

## Second pass — the two flagged items, now DONE
### 1. `scripts/` root de-bloated — ✅ 774 → 281 `.py` (493 archived)
Ran a **reference-protected curated archive** (classifier: `scratchpad/classify_scripts.py`). KEEP if the exact filename is referenced in a **current-authoritative** doc (Workflow/Instructions + Catalogue + Global_rules + CLAUDE.md + memory + reusable-scripts-catalogue + project-orientation), OR a reusable prefix (`build_`/`generate_`/`export_`/`word_`/`apply_session_patch`), OR undated (named tool), OR July-dated (current era). Everything else — the cluster-era one-off bulk (`_apply_m*_phase*`, `_exploratory_*`, `_pilot_*`, `_generate_cluster_*`, `_build_m*`, `_validate_cluster_*`, `_repair_*`, …) — → `archive/scripts/` (now 670). **Verified no live current-method tool was swept** (passage_completeness, load_segmentation, locus_dimension, stamp_char_candidate, add_role_to_master, check_passage_reading, reread_measures, file_chapter_lexical_prose, inspect_unit_lexical all retained). Archive is recoverable + manifest-indexed, so any false-archive is one `mv` back.

### 2. `docs/` assessments relocated — ✅ 5 moved (was 30 → 26 `.md`)
Moved the unambiguous investigation/assessment outputs → `research/investigations/`: `assessment-wa-session-b-findings`, `assessment-wa-session-research-flags`, `assessment-wa-term-phase2-flags`, `open-items-currency-and-table-disposition-20260614`, `flag-tables-extract-joins-20260415`. Their cross-references are almost all in **historical records** (session logs, the reconstruction spine-index) which are point-in-time and were **not** rewritten (the manifest resolves the new location). **Deliberately kept in `docs/`:** `database-table-analysis.md` (functions as DB reference documentation; cited by live memory `feedback_evidence_signal_completeness`) and `script-registry-generated-20260614.md` (a generated snapshot — now **stale** after this scripts reorg; regenerate rather than move).

## Not touched (correct as-is)
Project root (CLAUDE.md, README.md, tasks.md — standard); `Workflow/Instructions/` (cleaned 2026-07-08, 13 current docs); `outputs/markdown/` (established de-facto subfolder, in use); the DB (single source of truth for findings).

*Filed 2026-07-09. Manifest rebuilt after these moves.*
