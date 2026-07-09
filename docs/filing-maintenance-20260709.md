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

## Flagged — need a policy decision before action
### 1. `scripts/` root is bloated — 774 `.py`, of which ~600 are dated one-offs
Breakdown: `_apply_*` 328 · `_exploratory_*` 41 · `_assess_*` 32 · `_generate_*` 28 · `_repair_*` 28 · `build_*` 26 · `_probe_*` 18 · `_check_*` 13 · … §3.13/§4 say served one-off `_check_*`/`_probe_*`/`_tmp_*` and old utility scripts belong in `archive/scripts/`. Most dated `_apply_*`/`_repair_*`/`_probe_*`/`_assess_*` have served their purpose — but "served" can't be determined mechanically, and some dated scripts may still be reused. **Recommend a curated archive pass with a retention policy** (e.g. "archive all dated `_apply_`/`_repair_`/`_probe_`/`_assess_`/`_exploratory_` older than 30 days; keep `build_`/`generate_`/`export_`/`apply_session_patch` and anything parameterised & reusable"). Not done here to avoid archiving something still live.

### 2. `docs/` still holds ~7 cross-referenced assessment/report files
Per §3.11 these belong in `research/investigations/`, but each is referenced by other docs, so moving them needs the referrers updated too: `assessment-wa-session-b-findings` (1 ref), `assessment-wa-session-research-flags` (2), `assessment-wa-term-phase2-flags` (1), `database-table-analysis` (2), `flag-tables-extract-joins-20260415` (1), `open-items-currency-and-table-disposition-20260614` (1), `script-registry-generated-20260614` (4). **Recommend moving + updating refs in a dedicated pass**, or leave (docs/ is a defensible-enough home).

## Not touched (correct as-is)
Project root (CLAUDE.md, README.md, tasks.md — standard); `Workflow/Instructions/` (cleaned 2026-07-08, 13 current docs); `outputs/markdown/` (established de-facto subfolder, in use); the DB (single source of truth for findings).

*Filed 2026-07-09. Manifest rebuilt after these moves.*
