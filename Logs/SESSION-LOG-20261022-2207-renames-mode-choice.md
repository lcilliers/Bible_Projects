# Session log — 2026-10-22 — #2207 renames, and the mode for the rest of the backlog

Session id: `d74187d6-1173-4993-9516-9f985fd9ac3b` (standard mode). Close report:
`iba/app/reports/session-close-v157-20261022.md` (and its re-runs).

## 1. Scope

2026-10-22, standard mode. #2207 (fix, don't count) was continued: a live check of what is left, the
7 file renames, and a fix to the close's repeated-failure check (SC16). Every remaining item writes
cfg rows, so the researcher chose Developer Mode for the rest of the work.

## 2. Escalations

- #2207: updated v14 (live check, renames, the mode decision put to the researcher) and v15 (the
  researcher's choice). Open, with Claude, for a Developer Mode session.
- #2177 (reset parent) and #2206 (option 2b, folded into #2207): untouched; they move with #2207.

## 3. Files

- Renamed (`git mv`): `Workflow/Catalogue/1378-lexical-to-finding-worked-example-v1-20260901.md`,
  `iba/docs/795-escalation-type-routing-proposal-v1-20260822.md`,
  `iba/docs/798-escalation-decision-vs-defect-axis-proposal-v5-20260822.md`,
  `iba/docs/863-file-naming-and-location-governance-plan-v1-20260826.md`,
  `iba/docs/890-prose-add-edit-rules-proposal-v1-20260826.md`,
  `iba/docs/971-folder-purpose-governance-plan-v5-20260828.md`.
- Header corrected: `Workflow/Catalogue/1376-characteristic-tables-cross-db-inventory-v2-20260901.md`.
- References updated: `iba/app/ps/Escalation.ps1`, `iba/app/ps/FolderPurpose.ps1`,
  `iba/app/migration/add_resolution_kind_column_v1_20260822.py`,
  `iba/app/migration/bootstrap_decision_vs_defect_axis_v1_20260822.py`,
  `Workflow/Catalogue/1379-lexical-inner-being-checklist-v1-20260901.md`.
- Code: `iba/app/lib/sessionwindow.py` (`failed_calls`).
- Records: `iba/app/BUILD.md` (sec 380), `Logs/compliance/COMPLIANCE-20261022-d74187d6.md`, this log.
- Generated reports: `outputs/escalation/escalation-list-v187-20261022.md`,
  `outputs/escalation/escalation-thread-audit-v3-20261022.md`,
  `outputs/escalation/escalation-context-v4-20261022.md`, and their archived predecessors.

## 4. Decisions

- Researcher: the rest of #2207 is built in a fresh Developer Mode session (#2207 v15).
- Claude, self-correctable: `Workflow/Catalogue/1379-lexical-to-finding-worked-example-v1-20260901.md`
  renamed to 1378, because its header names #1378; the 1376 file's header now names #1376
  (`iba/app/BUILD.md` sec 380).
- Claude, self-correctable: SC16 counted one failure twice and treated two different tracebacks as one
  repeat; fixed in `iba/app/lib/sessionwindow.py` (`iba/app/BUILD.md` sec 380).

## 5. Open items

- #2207, with Claude, in Developer Mode: first the 7 cfg rows naming the old paths
  (`cfg_table folder_purpose.use`, `cfg_behaviour_class filing.authoritative_doc`,
  `cfg_behaviour_rule` 56 to 60 `source`), then the backlog in #2207 v14.

## 6. Git

- Branch: `main`
- Commit: `316cfe3dfb638fa00c1e1140f5ebf13ac5ed5d96`
- Push: `10d74a34..316cfe3d  main -> main` (https://github.com/lcilliers/Bible_Projects.git)
