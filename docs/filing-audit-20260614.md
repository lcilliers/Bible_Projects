# Filing Audit — `file-organisation-rules.md` ↔ actual layout (2026-06-14)

> Reconciles the governing filing doc against the live tree. Method: existence-check every `§3` path. This is a **read-only audit + safe documentation corrections** to the living rules doc — **no files were moved** (moves are the researcher's call). Companion to the reconstruction 02/03/04.

## Discrepancies found (path references that no longer match reality)

| Rule | Doc says | Actual (verified 2026-06-14) | Action |
|---|---|---|---|
| §3.7 governing instructions | `data/imports/WA/Workflow/Framework_B/Session_B/` — **MISSING** | `Workflow/Instructions/` (35 files) | ✅ corrected in rules doc |
| §3.9 schema (DDL + snapshots) | `data/schema/` — **MISSING** | `Workflow/schema/` (17 files) | ✅ corrected |
| §3.15 analytics library | `analytics/` (top-level) — **MISSING** | `scripts/analytics/` | ✅ corrected |
| §3.1 STEP extracts / exports | `data/exports/Session C`, `/vertical_pass`, `/pool_analysis` — **MISSING** | canonical = `Sessions/Session_A/STEP Extracts/` (196 files, per CLAUDE.md §8); `data/exports/` (10 residual files) = legacy | ✅ noted; `data/exports/` flagged legacy |
| §3.1 VC process input | `Sessions/Session_B/01_Verse_Context_Process_input` | exists but **empty** (0 files) | informational |

## The `data/` vs `Sessions/` duality (the root of "folders aren't reliable")

A top-level **`data/`** exists (`data/exports` 10 files, `data/imports/WA` 3 files) but is **absent from CLAUDE.md §2's directory map**, and the post-restructure canonical homes are under `Sessions/`, `Workflow/`, `database/`. So two parallel location systems coexist for exports/imports/schema — exactly why browsing folders is unreliable and the manifest is the reliable locator.

**Recommendation (researcher decision — not executed):** confirm `Sessions/` + `Workflow/` as canonical, migrate the ~13 residual files out of `data/`, and retire `data/`. Until then, `data/` is legacy-but-live.

## Schema-snapshot staleness

The newest on-disk schema snapshot predates the live **3.31.0** (newest found: `Workflow/schema/archive/database-schema-v3.10.0-…`). **Recommendation:** regenerate with `python scripts/export_database_schema.py` to produce a current `Workflow/schema/database-schema-…3.31.0` snapshot.

## Other filing hygiene (surfaced by the #6 script registry)

- **15 `_tmp_*.py` scripts still present** — rule §5 says delete/archive at session end.
- **13 version-duplicate supersession candidates** + **140 off-convention script names** — see `docs/script-registry-generated-20260614.md`.
- **~12 silently-superseded docs** (reconstruction 04 §4) sit un-archived in active folders — rule §4 says archive them.

## Corrections applied this session (to the living `file-organisation-rules.md`)

§3.7 → `Workflow/Instructions/` · §3.9 → `Workflow/schema/` · §3.15 → `scripts/analytics/` · §3.1 STEP-extract canonical home noted + `data/exports` flagged legacy · header `Updated 2026-06-14` with a pointer to this audit.

## Open items (researcher / future)

1. Resolve the `data/` vs `Sessions/`/`Workflow/` duality (keep+document, or migrate+retire `data/`).
2. Regenerate the schema snapshot to 3.31.0.
3. Archive the 15 `_tmp_*` scripts and the ~12 silently-superseded docs; triage the 13 supersession candidates.
4. Bring 140 off-convention scripts into the naming convention (or mark intentionally exempt).
