# #2107 config findings: triage and fixes

> Escalation #2107 · 2026-10-12 · source: `configmaint.validate`, `outputs/configs/CONFIG-REPORT-v555-20261012.md` §0 (151 numbered findings)
> Researcher, chat 2026-10-12 (verbatim): *"fix the issue on2107"*

Each category below gives the evidence (checked live), what was done in this session, and what is left. The left-over items fall into three kinds:
- **config rows:** a `cfg_*` change. In a standard session these go through `Config-Maintenance.ps1 -Step Propose`, one row and one approval each.
- **code:** a change to the app's own code.
- **researcher decision:** a judgement call that is the researcher's.

## Summary

| # | Category | Count | Real? | Done now | Left |
|---|---|---|---|---|---|
| A | Stale filled_by | 29 | 28 false positives, 1 real | detector fixed | 1 config row |
| B | Query file convention | 2 | real | both renamed | none |
| C | Orphan configs | 5 | 1 detector gap, 4 real | none | code (enum checks), or config |
| D | Unregistered lib module | 1 | real | none | 1 config row (`cfg_utility` insert) |
| E | Low config-density utilities | 18 | mostly legitimate zeros | none | config rows (`config_exempt=1`) after a per-module look |
| F | Hand-rolled versioning | 5 | 1 deliberate, 4 one-off analysis scripts | none | researcher decision on scope |
| G | PS/worksheet drift | 5 | real | none | worksheet edits |
| H | Unenforced behaviour rules | 48 | 47 informational, 1 real | none | 1 config row (rule 67 status) |
| I | Undelivered conversational rules | 4 | real (delivery not cited) | none | 4 config rows (`enforced_by` text) |
| J | PS scripts bypassing run.py | 2 | real | none | code (Behaviour.ps1, VerseMeta.ps1) |
| K | Escalation-file naming drift | 27 | real but historical (13 in `archive/`) | none | researcher decision (rename or accept) |
| L | Config hedge phrases | 5 | 2 real open items, 3 wording | none | config rows (wording) |

## A. Stale filled_by (29): 28 false positives, detector fixed

- **Found:** `cfgquality.find_filled_by_referencing_inactive_step` read every `cfg_column` row, including rows already `inactive=1`. 28 of the 29 findings were on inactive columns, whose dormancy is already settled:
  - `strong_meaning_parsed`, `strong_lsj_parsed`, `strong_mounce_parsed`: retired and frozen 2026-09-10
  - `verse_lexical_note`: retired
  - `passage.genre`: retired 2026-09-09, #1608
- **Fixed:** the query now adds `AND inactive=0` (`iba/app/lib/cfgquality.py`).
- **Left (1 real):** `passage.lexical_complete_at` (active column) names `lexical.enrich`, which is inactive.
  - Checked live: 0 of the passage rows have it set.
  - Its only writer is `lib/lexicalenrich.py`, behind the inactive step.
  - Its sibling `passage.genre` and the `verse_lexical_note` table from the same build are both inactive.
  - **Proposed:** set `cfg_column` passage.lexical_complete_at `inactive=1`, matching its siblings (1 config row).

## B. Query file convention (2): fixed

`scripts/SQLite/IBA_DB/explore clusters-2.sqlite3-query` → `explore-clusters-2.sqlite3-query`; `explore verses.sqlite3-query` → `explore-verses.sqlite3-query` (git mv).

## C. Orphan configs (5)

- `cfg_setting narrative.inner_being_style_guide_path`: Claude reads it, not code. CLAUDE.md names it as the writing standard, and the governance-module exemption in `find_orphan_configs` exists for exactly this kind of reader. **Proposed:** extend that exemption to any setting cited by key in CLAUDE.md (a detector change), or move the key to module `governance` (1 config row). The detector change is the root fix.
- `cfg_enum ib_observation.meaning_source` (3 values): several generators **write** `meaning_source`:
  - `lib/versereadinggenerate.py`, `subgroupgenerate.py`, `charreadinggenerate.py`, `charanswergenerate.py`, `recordingpass.py`
  - `handlers/observationenhancer.py`

  None checks the value against the enum, which is the gap `governance.project_lookups_and_naming_convensions` describes. **Proposed:** validate at the write through `cfg.enum('ib_observation.meaning_source')` (code).
- `cfg_enum wa_obs_question_catalogue.scope / .status / .tier`: the catalogue is read (`charanswergenerate.py` reads `scope`), but no write path checks these values. **Proposed:** the same enum check where the catalogue is written (`lib/cataloguewrite.py`), or accept them as documentation of the column values (researcher decision).

## D. Unregistered lib module (1)

`iba/app/lib/taggingguidance.py` has no `cfg_utility` row. It is live: four generators import it. **Proposed:** a `cfg_utility` insert (module `taggingguidance`), as `bootstrap_cfg_utility.py` registers modules (1 config row).

## E. Low config-density utilities (18)

Nine are one-off migrations or tools that have already run:
- `apply_1598_*` (2)
- `create_verse_meta_table_*`, `drop_verse_meta_genre_column_*`, `add_verse_meta_status_column_*`, `add_lexicon_header_pos_tags_setting_*`, `create_vw_strong_meaning_raw_*`
- `_apply_verse_plaintext_column`
- `VerseMeta.ps1`

For these, zero config reads is legitimate. **Proposed:** `config_exempt=1` (config rows).

The other nine are live library or handler modules:
- `handlers_catalogue`, `lexicalenrich`, `lexicalscope`, `clusterfamilyscan`, `clusterstatus`, `recordingpass`, `batchcontrol`, `batchprogressreport`, `observationenhancer`

Each needs a look: is it a legitimate zero, or does it hold values that belong in config? Not judged here.

## F. Hand-rolled versioning (5)

- `iba/app/lib/prosestore.py`: **deliberate.** Its `_next_edit_version` is an edit-cycle counter that runs across days and scans `archive/`, so that each prose export can be traced to its edit session (#784). `filingkit.versioned_path()` bumps within a day only, so migrating would change the meaning. **Proposed:** accept, with an exemption recorded in the detector (code) — researcher decision.
- Four `_analytics/Clusters/...` scripts (M18, M64, M72): one-off analysis scripts that have already run. **Proposed:** keep `_analytics/` out of this check's scope (detector) or accept them as they are — researcher decision.

## G. PS/worksheet drift (5)

| Script | Missing from `iba/docs/ps tools worksheet.xlsx` |
|---|---|
| `Copy-NarrativeToLearning4Comfort.ps1` | no tab |
| `RelationalReading.ps1` | no tab |
| `Run-Stage1Batch.ps1` | no tab |
| `Purge-SoftDeletes.ps1` | columns `Action`, `Database`, `Live` |
| `VerseReading.ps1` | columns `Force`, `VerseList` |

**Proposed:** add the tabs and columns (worksheet edit; workbook tested for an open lock first).

## H. Unenforced behaviour rules (48)

- **47 are informational.** Each carries a settled `enforcement_status` (context_delivered, deliberately_deferred, partially_enforced or buildable_not_built) with its own reason. They list what is not code-checked and are not defects.
- **Real (1):** rule #67 `bible-research-db-excluded-from-iba-results` has no `enforcement_status` and no `enforced_by`. **Proposed:** classify it (config row). Its text is a rule about what goes into analysis results, the same class as the other `sqlite` rules marked `context_delivered`.

## I. Undelivered conversational rules (4)

The detector checks that a rule's `source`/`enforced_by` cites a delivery mechanism that exists: a memory file indexed in MEMORY.md, a `governance.*` setting, or a CLAUDE.md, GOVERNANCE.md or USER-GUIDE.md reference.

| Rule | Delivery that exists | Proposed `enforced_by` addition |
|---|---|---|
| #21 chat-items-become-escalations | `feedback_close_the_loop_not_just_investigate_and_report`, `feedback_document_scope_decisions_prominently_not_just_in_escalations` (memory) | cite the memory files |
| #27 heredoc-powershell-only | CLAUDE.md §13 (PowerShell 7+); to be checked | cite the actual delivery, or mark undelivered honestly |
| #65 audit-deliverable-cross-check-before-presenting | `feedback_audit_deliverables_need_cross_check_before_presenting` (memory) | cite the memory file |
| #69 let-scripture-speak-no-imputed-synthesis | CLAUDE.md ("rule 69"), `feedback_let_scripture_speak_no_imputed_synthesis` (memory) | cite CLAUDE.md and the memory file |

4 config rows (text only).

## J. PS scripts bypassing run.py (2)

`iba/app/ps/Behaviour.ps1` and `iba/app/ps/VerseMeta.ps1` call `iba.app.(lib|handlers)` directly. **Proposed:** route each through `run.py` as its own work package step (code + config). A small build each; not started.

## K. Escalation-file naming drift (27)

- 13 files are in `archive/` folders. 14 are live `iba/docs` or `Workflow/Catalogue` design documents from August and early September (#784, #795, #798, #863, #890, #971, #989, #1007/#1376, #1378/#1379).
- Renaming would break the links to them in BUILD.md, GOVERNANCE.md and escalation contexts.
- One more is a filename with a space in `archive/`.
- **Proposed (researcher decision):** either rename the 14 live files with an `{id}-` prefix and update their references, or accept the files written before the rule as they are, recorded as an exemption by date in the detector.

## L. Config hedge phrases (5)

- `cfg_method_rule #67 spine-on-demand-pull-mechanism`: a real open build item, tracked under #1613. **Proposed:** name its status as `buildable_not_built`, tracked on #1613, in words the detector does not read as a bare hedge (config row). Before that, check #1613's live state.
- `cfg_method_rule #106 battery-scope-excludes-verse-reading-and-science-extract`: "wiring not yet decided" for the science-extract questions. Science chapters come later (CLAUDE.md). **Proposed:** state it as deferred until the science stage (config row).
- `cfg_setting governance.prose_canonical_authority`, `governance.procedural_document_taxonomy`, `governance.engineering_documentation_folder`: each says a follow-on part is "not yet built/applied/resolved here". **Proposed:** reword each to name the follow-on and where it is held, or mark it deferred (3 config rows).

## Route for the config rows

The config rows proposed above come to about 30 to 40 (A 1, C 1, D 1, E 9 or more, H 1, I 4, L 5, plus any of E's live modules). Two routes:
1. **`Config-Maintenance.ps1 -Step Propose`**, one row at a time, each approved by the researcher.
2. **One audited migration** through `configmaint.apply_logged`, the path §339 built, which writes every row to `cfg_change_detail` with its prior state. It would run once the researcher has approved this list.

Not decided here; the researcher's choice.
