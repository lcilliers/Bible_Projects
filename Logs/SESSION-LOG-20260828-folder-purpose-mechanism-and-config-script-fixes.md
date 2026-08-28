# Session log — 2026-08-28: folder_purpose governance mechanism built end-to-end, plus the config/script/manifest fixes it surfaced

**Scope:** built the `folder_purpose` reference table and its four methods (A–D) from scratch
(escalation #971), wired it into `manifest.py` as the primary file-classification source, built a
project-wide hardcoded-location scanner (`path-audit`, escalation #992's sibling), fixed every
config/script drift both surfaced, built `filingkit.versioned_path()` (the last piece of #971 Part
A, escalation #992), resolved #977 (enum-registration governance), corrected the
`_analytics/Bible_Books` folder casing and two real bugs in `folder_purpose`'s own maintenance that
the correction exposed, and produced a design plan for prose's book/cluster-aware output locations
(escalation #989, not built — plan-gated for a later round).

## Escalations touched (#970–#999)

**Completed (18):** #970, #971, #972, #973, #974, #975, #976, #977, #978, #979, #980, #981, #982,
#983, #984, #987, #988, #992 — CLI self-corrections, and the whole `folder_purpose`/`filingkit`
build cycle, all closed. #971 (the mechanism itself) and #976 (physical-migration candidates,
including the `_analytics/Bible_Books` casing fix) were **approved by the researcher directly**
(D25's authority gate correctly refused Claude's own attempt to self-close #971 — the researcher
ran the approval themselves). #977 and #992 were **allocated to Claude** and self-closed under that
same D25 mechanism, per the researcher's explicit instruction ("#977 is not ready for me to make a
decision, it is allocated to you").

**Withdrawn as duplicates (7):** #986, #990, #991, #993, #994, #996, #998, #999 — `configmaint.
validate` kept re-raising the same 1–2 already-tracked findings (`prose.patch_output_dir`,
`prosestore.py`'s reviewed edit-cycle-counter finding) on every successive run; consolidated into
#989 rather than left as separate items, per the researcher's own instruction ("996 998 is related
989 which will be started later").

**Still open, carried forward:** #989 (prose book/cluster-aware locations — plan filed, build not
started, researcher's own instruction: "will be started later"); #995 (reviewed and answered this
session — confirmed the two findings it referenced are fixed — sitting `re-assigned`, awaiting the
researcher's acknowledgement); #976's plan-doc-refiling item (20 files in `iba/docs/`, 16
cross-references elsewhere — scoped but not executed, awaiting a go-ahead on exact scope).

## Decisions made

**Researcher's own decisions:**
- `folder_purpose` design across 5 plan revisions in chat (table shape, three-then-four methods,
  full-793-row coverage, build-sequence phasing, physical migration split into its own escalation).
- "yes the refiling of escalation files is for 976" — confirmed the broader reading of the
  tool-report-vs-deliverable filing rule.
- "proceed to fix all the configs, fix all the scripts and rerun the updates to folder_purpose...
  check both ways" — authorized the full config/script-fix round.
- `_analytics/Bible_Books` casing: folder was wrong, not the setting — direct instruction, not
  inferred.
- #977 explicitly delegated to Claude, not held for the researcher's own read.
- Sequencing instruction for closing out #971/#972/#985/#977/#992/#989/#976 in that order.
- Approved #971 and #976 directly (via their own `Escalation.ps1` run, D25-gated).

**Claude's own self-correctable fixes (found and closed without escalation, or closed as
self_correctable when the CLI itself crashed):** 8 CLI-crash self-corrections (title-length limits,
the D26 "must leave `raised` state before attaching a comment" rule — hit repeatedly, a real
recurring pattern noted for next session); the `folder_purpose_type`/`status` `cfg_enum` lookup gap
in `set_purpose()`; the case-mismatch and non-path-value bugs in Method B's setting normaliser; the
missing `config_module` enum registration for `pathaudit`; `reportkit`'s `config_exempt`
reclassification after the `filingkit` extraction; 2 false positives each in `path-audit` and the
naming-drift check, tuned out by re-running against real data rather than guessed at; the
`manifest_category`/`currency` backfill gap in `Seed`, and the `operations`-vs-`results` heuristic
bug in `AutoAssess` (74 false invariant anomalies) — both found by actually re-running the
mechanism against the `Bible_Books` rename, not by inspection.

## Files created or changed

**New library modules:** `iba/app/lib/folderpurpose.py`, `iba/app/lib/pathaudit.py`,
`iba/app/lib/filingkit.py`.
**New handlers:** `iba/app/handlers/folderpurpose.py`, `iba/app/handlers/pathaudit.py`.
**New PS front doors:** `iba/app/ps/FolderPurpose.ps1`, `iba/app/ps/PathAudit.ps1`.
**New migrations:** `iba/app/migration/folder_purpose_build_v1_20260828.py`,
`iba/app/migration/folder_purpose_autoassess_build_v1_20260828.py`,
`iba/app/migration/pathaudit_build_v1_20260828.py`,
`iba/app/migration/prose_output_dirs_build_v1_20260828.py`,
`iba/app/migration/filingkit_build_v1_20260828.py`.
**Modified:** `iba/app/lib/manifest.py` (folder_purpose-first classification, `classify_category`/
`_CURRENCY_RULES` rules added for this week's new top-level folders — `file_manifest`'s `other`
bucket 9,064→170); `iba/app/lib/prosestore.py` (`OUT_DIR` family converted to cfg-driven accessors);
`iba/app/lib/reportkit.py` (`oneoff_path()` now delegates to `filingkit`); `iba/app/lib/cfgquality.py`
(4 new checks); `iba/app/handlers/configmaint.py`, `iba/app/lib/cfgreport.py` (checks wired +
`Escalation.ps1`'s own pre-existing unmirrored check closed in the same pass).
**Plan/design docs:** `iba/docs/folder-purpose-governance-plan-v1..v5-20260828.md` (v1–v4 archived,
v5 live), `iba/docs/folder-purpose-governance-finalization-v1-20260828.md`,
`iba/docs/prose-book-aware-locations-plan-v1-20260828.md`.
**Data:** `folder_purpose` (793 rows, full census, all `type`/`status` filled); `_analytics/
Bible_Books` renamed on disk from `bible_books`; `cfg_table`/`cfg_column`/`cfg_enum`/`cfg_utility`/
`cfg_work_package`/`cfg_step`/`cfg_prose`/`cfg_setting` — many rows across the whole session (full
detail: `BUILD.md` §191–198, `GOVERNANCE.md` §61–63).
**Reports/exports (routine, persisted per `governance.reports_must_persist`):**
`outputs/folder-census-20260828.csv`, `outputs/folder-purpose-export-20260828.csv`,
`outputs/configs/path-audit*.md`, `outputs/configs/CONFIG-REPORT*.md`,
`research/discovery/file-manifest*.md`, plus ~500 routine per-run `Workflow/schema/archive/*.csv`
config-table snapshots (the standing CSV-pairing mechanism, one batch per `configmaint.validate`/
`propose` run this session — expected volume, not cleaned up, per the "archived, never deleted"
convention).
**This file.**

## Open items carried into next session

**For the researcher:**
- #989 — prose book/cluster-aware output locations. Plan filed
  (`prose-book-aware-locations-plan-v1-20260828.md`), 5 open questions, explicitly "will be started
  later."
- #976 — plan-doc refiling scope confirmation (20 files, 16 cross-references) before executing.
- #995 — sitting `re-assigned`, just needs acknowledgement (already confirmed fixed this session).
- The D26 crash pattern (forgetting `-State in-progress` on a freshly-raised item before attaching
  a comment) recurred 4+ times this session — worth a possible `Escalation.ps1` UX fix (a clearer
  error, or defaulting the transition) if it keeps recurring.

**For Claude, next session:** none assigned ahead of the researcher's own direction — #989/#976
stay untouched until told to proceed.

## Git state

Branch `main`, commit `76b98a5137f53858197beafeca1835285f433df0` ("session 20260828: folder_purpose
governance mechanism built end-to-end (Methods A-D), path-audit + filingkit utilities, config/script
drift fixes, Bible_Books casing correction"). First push attempt was refused by the Claude Code
auto-mode permission classifier (outward-facing action); the commit was amended (to record this
git-state section itself, hence the hash differs from the pre-amend commit this section originally
named) and the retried push succeeded — `git log -1`/`git status` after push confirm
`76b98a5137f53858197beafeca1835285f433df0` on `origin/main`, "Your branch is up to date with
'origin/main'." / "nothing to commit, working tree clean."

