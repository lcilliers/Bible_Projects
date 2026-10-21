# #2177 reset backlog: plan for #2188, #2191, #2192, #2193 (and #2198)

Session 3cea0e6c, Developer Mode, 2026-10-21. Researcher instruction (verbatim): "proceed with
developer-mode.  the base escalation is 2177. start with 2195, then 2188,2191,2192, and 2193."

#2195 is done (rule 59 pointer dropped, `iba/app/BUILD.md` §365). It turned up two more items:
#2196, the nine 2026-10-21 migrations, which had no `cfg_utility` row (fixed, also §365), and
#2198 (a decision, below). Each remaining item had only a *proposed* approach. Rule 105 means I
build nothing before its approach is approved. All figures below were measured read-only today.

Approve each item, change it, or answer its decision.

---

## 1. #2188: the 8 instruction files and the iba/config JSON, into config

**Found.** The 8 files total 111 KB:

| file | size | read by code |
|---|---|---|
| `Workflow/Instructions/wa-inner-being-narrative-style-guide-v2-20261001.md` | 15.9 KB | `narrative.inner_being_style_guide_path` |
| `Workflow/Instructions/WA-inner-being-narrative-guidance-v1-2026-07-28.md` | 8.3 KB | `method.inner_being_narrative_guidance_path` |
| `Workflow/Instructions/WA-inner-being-narrative-hard-constraints-v1-2026-07-30.md` | 8.2 KB | `method.narrative_hard_constraints_path` (`iba/app/lib/narrativegenerate.py:115`) |
| `Workflow/Instructions/WA-passage-read-guidance-v1.5-2026-08-02.md` | 13.2 KB | `method.passage_read_guidance_path` (`iba/app/lib/passagedebatereport.py:128`) |
| `Workflow/Instructions/WA-interpretation-questions-v1.4-2026-08-02.md` | 14.9 KB | `method.interpretation_questions_path` (`iba/app/lib/passagedebatereport.py:129`) |
| `Workflow/Instructions/wa-verse-reading-by-role-guide-v2-20261019.md` | 18.0 KB | no |
| `Workflow/Instructions/wa-verse-analysis-method-v1-20260702.md` | 25.9 KB | no |
| `Workflow/Instructions/wa-operational-governance-v1_0-20260614.md` | 6.6 KB | no; its §4 points at the retired `docs/interaction-preferences.md` |

Also in scope: `iba/config/DBSchema/DBSchema.json` and `iba/config/utility/{DBSchema_maintenance,step}.json`,
read by `iba/scripts/build_dbschema.py` and `iba/scripts/probe_step_api.py`.

**Proposed: step 1 is a mapping only, no cfg write.** For each instruction in each file, one of:
(a) already covered by a cfg row (named), so the file line becomes a pointer; (b) a new
`cfg_behaviour_rule` or setting, with draft wording; (c) history, to be removed from the live file under rule 96;
(d) a study principle, which goes to #2190 (parked until the study re-opens). Narrative files come first,
then the reading and method files, then operational governance, then the JSON. The deliverable is
`outputs/escalation/2188-instruction-files-to-config-mapping-v1-20261021.md`, handed to you for
approval. Step 2, writing the rows through `apply_logged`, runs only after you approve the mapping.

**Decision 1A: the four files code reads.** Code reads them as whole documents and passes them to
narrative and passage-debate generation.
- **Option 1 (recommended):** they stay as files, because they are generation inputs. Only the
  rules about how Claude must work move to cfg, and the file then points to the rule (rule 3:
  no rule in two places).
- **Option 2:** their content becomes cfg rows, and the code builds the input from those rows. That
  means a code change in `narrativegenerate.py` and `passagedebatereport.py`.

**Decision 1B: the study hold.** These are study-method files and the study is on hold
(`governance.study_status`). Moving their rules into config is control work, not reading or
writing. I propose to go ahead (you named #2188 today), but I won't edit study content and will send study
principles to #2190. Confirm, or park #2188 with the study.

## 2. #2191: retirement check for the old files in `docs/`

**Found.** `docs/` holds 36 files. I applied #2182's test: is the file named by any active cfg_*
row, open or parked escalation, `iba/app` code (not migrations or archive), `.claude/`, or CLAUDE.md?
- **35 are named by nothing live.** The only hits for two of them are history:
  `governance-alignment-register.md` (BUILD.md and an August report) and
  `project-orientation-core-memory-map.md` (BUILD.md, cfg_change_detail, and inactive rule 35).
- **1 is live:** `docs/prose-store-architecture.md`. It is named by `iba/app/lib/prosestore.py:28`
  and by the `source` text of active rules 52 and 53 (prose_section replace gate and two-patch ordering).

**Proposed.** `git mv` the 35 files to `docs/archive/`, list them by name in BUILD.md, and rebuild the
manifest as #2182 did. This is `governance.redundancy_archiving` applied with #2182's approved test.

**Decision 2: `prose-store-architecture.md`.**
- **Option 1 (recommended):** move it to `iba/docs/`, the home for engineering notes
  (`governance.engineering_documentation_folder`). Update the path in `prosestore.py` and in
  rules 52 and 53's `source` through `apply_logged`. `docs/` is then empty apart from `archive/`.
- **Option 2:** leave it in `docs/`.

## 3. #2192: replaced history in code comments and docstrings

**Found.** I scanned 120 Python files (`iba/app` without migrations or archive, plus `.claude/hooks`)
for comment and docstring lines with history markers ("escalation #n", dates, "found live",
"verbatim", "previously", "no longer", "superseded" and similar). The result: 1,276 marked lines out of
9,287 comment lines, in 105 files. The top five:

| file | marked lines | comment lines |
|---|---|---|
| `iba/app/lib/escalation.py` | 146 | 781 |
| `iba/app/lib/cfgquality.py` | 112 | 642 |
| `iba/app/handlers/configmaint.py` | 71 | 302 |
| `iba/app/lib/recordingpass.py` | 70 | 341 |
| `iba/app/handlers/lexical.py` | 68 | 295 |

A marked line is not always history. A bare `#nnnn` pointing to a line's source is allowed under rule 96.
An example of what has to go is the opening of `iba/app/lib/dbsnapshot.py`, which starts "THE GAP
FOUND 2026-07-22: ..." and then tells the incident.

**Proposed rewrite rule.** A comment says what the code does now and why, and ends with its
escalation id as a pointer. Incident stories, dated amendment notes, verbatim quotes and "used to /
previously" text come out (they already sit in the escalation and in BUILD.md). Only comments and
docstrings change. **Safety test per file:** the AST with docstrings stripped must be identical before
and after, the file must compile, and the PS tool or the test that uses the module is run once.

**Decision 3: batch size.**
- **Option 1 (recommended):** first the ten files with the most marked lines, about 600 lines. I hand you a before/after sample to
  check the rewrite rule, then do the remaining 95 files.
- **Option 2:** all 105 files in this session, without stopping for a sample.

## 4. #2193: test copies of a database must use the SQLite backup API

**Found.** `iba/app/lib/dbsnapshot.py` takes the pre-run snapshot as a WAL checkpoint and then a
plain `shutil.copy2`. If the checkpoint can't complete (another connection busy), the copy misses
writes still in `iba.db-wal`, the same failure #2193 records for the #2185 test copies. There's no
shared helper for test copies. Each session made its own (this session used `sqlite3.backup`
inline).

**Proposed.**
- Add `copy_db(dest, src=DB_PATH)` to `iba/app/lib/dbsnapshot.py`, using `sqlite3.Connection.backup`,
  and a `--copy-to PATH` option on its command line. This reuses the module rather than adding one
  (rule 39).
- Rule 104 check: rule 97 (developer-mode-scope-and-conduct) already requires testing "against a
  copy". I propose to amend rule 97 to say how the copy is made (through `dbsnapshot.copy_db`, never a file copy),
  rather than add a new rule.
- **Test plan:**
  - Synthetic: write a row on an open WAL connection, then copy two ways. The file copy should miss
    the row and `copy_db` should have it.
  - Real: `copy_db` of live iba.db, then compare row counts for every table.
- USER-GUIDE.md and the ps tools worksheet only if a PS entry point is added. None is proposed:
  the module is called from code and the command line.

**Decision 4: the snapshot itself.**
- **Option 1 (recommended):** `snapshot()` also switches to `copy_db`. This fixes the shared
  mechanism (rule 38): a run's rollback snapshot has the same WAL gap. The cost is a slightly slower snapshot
  (iba.db is about 110 MB).
- **Option 2:** test copies only. `snapshot()` stays as it is.

## 5. #2198: no validate check covers `iba/app/` scripts other than `lib/`

**Found.** `find_unregistered_project_scripts` (`iba/app/lib/cfgquality.py:665`) skips `iba/app/`,
saying "handler/tool/migration checks" cover it, but only the `lib/` check exists. Unregistered in
`cfg_utility` today:

| folder | unregistered |
|---|---|
| `iba/app/handlers` | 12 of 23 |
| `iba/app/tools` | 20 of 22 |
| `iba/app/migration` | 186 of 262 |
| `iba/app/lib` | 0 of 63 |

**Not in today's list; raised so it is not lost.** Decisions, for when you want it taken up:
(a) whether handlers count as registered through `cfg_work_package` and `cfg_step` instead of `cfg_utility`;
(b) whether the 186 old migrations are registered after the fact, or exempted by date, with the check
starting from 2026-10-21; (c) whether the check is advisory, as the project-wide one is, or hard.

---

**Order once approved:** #2188 step 1 (the mapping), then #2191, #2192 (first batch), #2193.
Each one is tested on a backup-API copy where it writes data, and committed and pushed as it completes.
