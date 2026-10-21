# Session log 2026-10-21: IBA reset, uncontrolled scripts retired, retired-script gate

Session id: `3cea0e6c-e050-4cb4-9290-4e4885f10990` (Developer Mode, started 2026-10-21T08:55Z).

## 1. Scope

2026-10-21, Developer Mode, under #2177 (reset the IBA app as the project's primary process
controller). The researcher set the order: #2195, then #2188, #2191, #2192 and #2193.
- #2195: rule 59's dead pointer was dropped. #2196: the nine earlier migrations were registered.
- #2188 was paused until the study restarts.
- #2191: the 36 docs/ files were archived.
- #2192: replaced history was taken out of code comments.
- #2193: database copies now go through the SQLite backup API.
- #2198 and #2200: every script in no utility or module was retired (798). A gate hook now
  requires the researcher's approval to run a retired script. Validate errors on any unregistered
  script.
- #2199 and #2201: the researcher's decisions were applied (templates, seed path, word-audit, the
  narrative and word-registry-span stages, passage.suggest_boundary). The cluster backfill section
  was registered.

No study work: the study is on hold.

## 2. Escalations

**Raised and completed:**

| Id | Title | Outcome |
|---|---|---|
| #2195 | Rule 59 points at archived interaction-preferences.md | raised, completed (self-correctable) |
| #2196 | Nine 20261021 migrations have no cfg_utility row | raised, completed (self-correctable) |
| #2198 | No validate check for unregistered iba/app scripts | raised, completed (approved) |
| #2199 | Live cfg descriptions name docs/ files #2182 archived | raised, completed (approved) |
| #2200 | Archive iba/app code that serves no active function | raised, completed (approved) |
| #2201 | Open items found in code comments during #2192 | raised, completed (approved) |
| #2202 | validate hard error (deliberate test of the new check) | raised, completed (self-correctable) |
| #2203 | validate: 9 coherence errors (narrativegenerate import) | raised, completed (self-correctable) |
| #2204 | report.cluster crashed: division by zero | raised, completed (self-correctable) |

**Raised and still open:**

| Id | Title | Outcome |
|---|---|---|
| #2197 | cfg_* coherent, advisory findings (4 orphan enums) | raised by validate; with the researcher |
| #2205 | Six spine gaps not verified against STEP (STEP not running) | raised at session close; with Claude |

**Worked from earlier sessions:**

| Id | Title | Outcome |
|---|---|---|
| #2177 | Reset IBA app as the project's primary process controller | updated (v15-v19); open as the umbrella |
| #2181 | Cut CLAUDE.md to a short entry file | approved, completed |
| #2187 | Rewrite the user guide | approved, completed |
| #2188 | Move the 8 live instruction files into config | on-hold until the study restarts |
| #2189 | Permission settings: information for a decision | approved, completed |
| #2190 | Study-side controls to settle when the study re-opens | updated with #2192 exclusions; on-hold |
| #2191 | Retirement check for the 36 old files in docs/ | approved, completed |
| #2192 | Replaced history in code comments and docstrings | approved, completed |
| #2193 | Copy tests must use the SQLite backup API | approved, completed |

## 3. Files

- **Code and config:** named file by file in `iba/app/BUILD.md` sec 371, with the reasons in
  sec 365-370.
- **Config migrations** (each through `apply_logged`, in `iba/app/migration/archive/`), among them:
  - `register_20261021_migrations_v1_20261021.py`
  - `retire_uncontrolled_scripts_v1_20261021.py`
  - `register_active_app_files_v1_20261021.py`
  - `snapshot_policy_text_v1_20261021.py`
  - `apply_2199_2201_decisions_v1_20261021.py`
- **New:** `.claude/hooks/gate_retired_script.py`, wired in `.claude/settings.json`; live from the next
  session (hooks load at session start).
- **Control documents:**
  - `iba/app/BUILD.md` sec 365-371
  - `iba/app/GOVERNANCE.md`
  - `iba/app/USER-GUIDE.md`
  - `iba/docs/ps tools worksheet.xlsx`
- **Archived:**
  - 36 `docs/` files
  - 798 scripts, listed in `outputs/escalation/2200-retire-list-v1-20261021.json`
  - `iba/app/UTILITIES.md`
  - the #2201 modules (BUILD.md sec 370)
- **Deliverables** (`outputs/escalation/`):
  - `2177-reset-backlog-plan-v1-20261021.md`
  - `2192-retired-code-for-archiving-v1-20261021.md`
  - `2193-copy-db-test-results-v1-20261021.md`
  - `2200-retire-uncontrolled-scripts-plan-v1-20261021.md`
  - `2200-script-classification-v1-20261021.md`
  - `2200-retire-list-v1-20261021.json`
  - `2200-gate-test-results-v1-20261021.md`
- **Generated:**
  - `outputs/configs/CONFIG-REPORT-v602-20261021.md`
  - `_analytics/Clusters/cluster-v12-20261021.md`
- **Compliance:** `Logs/compliance/COMPLIANCE-20261021-3cea0e6c.md`

## 4. Decisions

- Researcher: pause #2188 until the study restarts (#2188 v5).
- Researcher: archive all of docs/, prose-store architecture included (#2191 v4).
- Researcher: take replaced history out of the code (#2192 v4). Exclude code serving retired
  functions from the sweep and list it for archiving (#2192 v7).
- Researcher: accept the backup-API proposal (#2193 v4).
- Researcher: a handler belongs to its work package, or else it is a utility, or it is retired
  (#2198 v4).
- Researcher: retire every script not in a utility or module, and gate the use of a retired script
  on the researcher's explicit approval; plan approved (#2200 v6, #2198 v8).
- Researcher: retire the templates (#2199 v4). The #2201 items: derive the version tables, register
  the backfill section, retire the seed code, word-audit, narrativegenerate and
  wordregistryspanreport, and passage.suggest_boundary (#2201 v4).
- Researcher: #2181, #2187 and #2189 approved (#2181 v6, #2187 v5, #2189 v4). #2171 stays open with
  the researcher (#2177 v19).
- Claude: the shared Claude-API helpers live in `iba/app/lib/lexicalenrichgenerate.py` (#2203 v2).
- Claude: the cluster report's backfill percentage shows a dash when nothing is untagged
  (`iba/app/lib/clusterreport.py`, #2204 v2).
- Claude: the 6 STEP-unverified spine gaps are carried, not verified, because STEP was not running
  (#2205 v1).

## 5. Open items

- #2171: with the researcher.
- #2197: with the researcher (4 orphan enums, advisory).
- #2205: for Claude, with STEP open (verify the 6 spine gaps).
- #2188, #2190, #2194: on hold until the study restarts.
- #2177: the umbrella, with Claude; progress in v18-v19.

## 6. Git

- Branch: `main`
- Session close commit: `f32e830c81bc2d36ca399b7b70d90d404155ac06` (Session-Close.ps1 exit 0,
  `iba/app/reports/session-close-v152-20261021.md`)
- Push: `2bba8e86..f32e830c  main -> main` to `https://github.com/lcilliers/Bible_Projects.git`
- Work commits this session: `17e202a9` through `2bba8e86`, each pushed when made.
