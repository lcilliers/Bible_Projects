# Session Log — Memory & Governance Hardening

**Date:** 2026-06-14 · **Owner:** le Roux Cilliers · **Executor:** Claude Code (Opus 4.8)
**Topic:** Reliability remediation — reconstruct true project state from the written record; refresh and harden the governing documents and project memory.
**Filed:** `Workflow/Sessionlogs/` (cross-stage governance log, per `docs/file-organisation-rules.md` §3.12).

---

## 1. How it started

A routine request ("search for *patience* in the DB", then "write a full extract of patience to a `.md`") surfaced a deeper concern the researcher then raised directly: **the memory / history / governing material used to work with the database is inconsistent and out of date, and is causing consistent errors.**

This was confirmed against hard facts:
- **Live schema 3.31.0**, but CLAUDE.md claimed **v3.17.0** (§3) *and* **v3.11.0** (§10) — stale and internally contradictory.
- The live **finding-centric architecture** (`finding` 343k rows; `cluster`/`characteristic`/`cluster_subgroup`/`cluster_finding`) was **absent from CLAUDE.md** entirely.
- CLAUDE.md framed `word_registry` as "the 214-word anchor" when it is now scaffolding (C-code dimension layer coexisting with the live M-code cluster model).
- **MEMORY.md was 44 KB against a 24.4 KB load cap** → only part of memory loaded each session → session-to-session inconsistency.

## 2. The method correction (the core lesson)

Two early attempts were wrong and were corrected by the researcher:
1. Reconstructing architecture **from the DB** (row counts) — that is *fabrication* (row-count ≠ relevance); the same failure mode as `project_meaning_duplicates_then_fabricates`, applied to structure.
2. Proposing the researcher **re-classify by hand** — ignoring that the answer was already written down.

**Established method (now memory `source-of-truth-is-written-record`):** establish project truth from the **written record** the researcher authored (session logs, docs, instructions, methodology, archive), driven by the **file manifest in ascending date order**; cite every claim; treat DB row-counts/last-write as *evidence*, not verdict; flag silences as open questions — never guess. **CLAUDE.md is the entry point; from there it fans out.**

## 3. The reconstruction (manifest-driven, written-record-grounded)

Built `outputs/markdown/project-reconstruction/`:
- `00-spine-index-ascending` — the 523-doc dated reading list.
- `01-project-status-reconstruction` — true status oldest→newest, cited; + "what is missing/incomplete (methodology)".
- `02-failures-oversights-rework-log` — ~55 cited failures + digested implications (two roots: **over-structuring an integrated subject** + **decision↔artefact drift**).
- `03-table-data-relevancy-map` — every table by usage/last-write into current/foundation/stale-relevant/dead/empty + issues to ratify.
- `04-open-loops-and-incomplete-methodology` — open actions, DRAFT/awaiting-approval work, **silent supersession** (~12 docs replaced without markers).

Method: five date-bucketed reader agents (Mar→Jun) reading the narrative spine with citation-required, no-inference rules; cross-checked against live DB forensics (last-write + row counts per table).

## 4. The recurring governance-omission pattern (researcher-flagged: "not the first time")

The reconstruction repeatedly **under-weighted the governance / operational layers** and had to be corrected in turn for omitting:
- **Filing / file-organisation** governance,
- **Operational & safeguard** governance (git/commit, backups & recovery, manifest),
- **Reusable scripts / report generators**.

Recorded as a first-class failure mode (memory `check-governance-layers-not-just-pipeline`): in any audit/reconstruction, **sweep every governance layer first** — analytical pipeline · filing · git/commit · backups & recovery · manifest · interaction/cost · reusable scripts — using the orientation map as the checklist.

## 5. The seven-item hardening (all done, committed incrementally)

| # | Item | Outcome |
|---|---|---|
| 5 | Integrity-script bug | `_integrity_full_check.py` resolved the dead `G:\My Drive\…` DB path → script-relative; verified against live DB (229,957 rows, 0 orphans). |
| 1 | CLAUDE.md refresh | §3 → schema **v3.31.0** + finding/cluster table groups + new key-relationships + registry C/M duality; §10 programme state with **verified** live counts; `EXPECTED_SCHEMA_VERSION` line fixed (constant verified). |
| 4 | Operational governance | New consolidated governing doc `Workflow/Instructions/wa-operational-governance-v1_0-20260614.md`; gap closed. |
| 6 | Script registry | New reusable generator `scripts/build_script_registry.py` + `docs/script-registry-generated-20260614.md` (**626 scripts** classified); surfaced 15 lingering `_tmp_`, 13 version-dupes, 140 off-convention names. |
| 3 | Filing audit | `docs/filing-audit-20260614.md`; corrected 3 wrong path refs in the living `file-organisation-rules.md` (§3.7/§3.9/§3.15); flagged the `data/` vs `Sessions/`/`Workflow/` duality. |
| 7 | Open-items + tables | `docs/open-items-currency-and-table-disposition-20260614.md`: `wa-programme-open-items.md` **predates the DB-loss/reset/pivot — not reliable as-is**; table dispositions recommended (no irreversible DB change executed). |
| 2 | Memory trim | MEMORY.md **44 KB → 23.5 KB** (under the load cap); all 125 entries preserved, hooks word-boundary-trimmed; mirrored to git. |

## 6. Artefacts created / changed

**New governing/reference docs:**
- `docs/project-orientation-core-memory-map.md` — the "start here" fan-out map (CLAUDE.md → instructions → reconstruction → open-items → memory; + filing, operational, scripts governance).
- `Workflow/Instructions/wa-operational-governance-v1_0-20260614.md`.
- `docs/reusable-scripts-catalogue.md` + `docs/script-registry-generated-20260614.md` (+ generator `scripts/build_script_registry.py`).
- `docs/filing-audit-20260614.md`; `docs/open-items-currency-and-table-disposition-20260614.md`.
- `outputs/markdown/project-reconstruction/00–04`.
- `scripts/_produce_registry_full_extract.py` + the patience full extract.

**Edited governing docs:** `CLAUDE.md` (top pointer + §3 + §4 constant + §10); `docs/file-organisation-rules.md` (path corrections); `scripts/_integrity_full_check.py` (path fix).

**New memory entries (mirrored to git `memory/`):** `reference-core-memory-orientation-map`, `source-of-truth-is-written-record`, `project_reconstruction_baseline_20260614`, `filing-is-first-class-governance`, `operational-governance-git-backup-manifest`, `check-governance-layers-not-just-pipeline`, `reusable-scripts-catalogue`. Plus the MEMORY.md index trim.

## 7. Commits (14, all pushed; branch `main`)

`a73e949` reconstruction + patience extract · `60700e8` open-loops register (04) · `90b2d82` orientation map + memory · `227c04a` filing governance · `ec1dea6` operational governance · `91469fa` recurring-pattern + governance-checklist memory · `9e363b9` reusable-scripts catalogue · `2f6081e` #5 integrity fix · `044a5bc` #1 CLAUDE.md refresh · `3a3853f` #4 operational-governance doc · `86b24c4` #6 script registry · `7ea0cfc` #3 filing audit · `3ea4c75` #7 open-items + tables · `0fb7181` #2 memory trim.

## 8. Open items carried forward

**Researcher decisions (irreversible / scope):**
- Table dispositions (see #7 doc): drop empty tables (`session_d_*`, `sources`, `themes`, `prose_section_*_link`); migrate `wa_session_b_findings` → `finding`; retire `wa_prose_section_citations`; refresh-vs-demote the reference-as-DB registries; C-code layer long-term fate.

**Safe cleanup (CC, in progress this session after this log):**
- Regenerate the schema snapshot to v3.31.0.
- Archive the 15 `_tmp_*` scripts.
- Add SUPERSEDED markers to / archive the silently-superseded docs (04 §4) — coordinating with `wa-workflow-cleanup-register.md`.
- Re-issue `wa-programme-open-items.md` as v9 after re-validation against the live DB.

**Standing:** OT-DBR-009 (mti_terms dedup); science extracts not in DB; v3_2 instruction finalisation (open item B3); catalogue refit (not yet in DB).

---

*The net effect: CLAUDE.md and memory now reflect the live state, fully load each session, and fan out to a cited current-state reconstruction; filing/operational/scripts governance are surfaced and partially repaired; the recurring "miss the governance layer" pattern is recorded with a checklist to prevent recurrence.*
