# #2179: Control documentation structure review (v2, 2026-10-21)

> **v2 correction (2026-10-21, found during #2182):** v1 called `scripts/apply_session_patch.py` missing. It exists; it and the engine are superseded (since 2026-08-17), not missing. Corrected in §1 and §3. Nothing else changed.

Escalation #2179, an element of the IBA app reset (#2177). Researcher, verbatim: *"verify that the
main IBA control documentation (Claude, governance, cfg_*, user_guide) and any other controls that
I may not even be aware of a) is optimally structured to prevent confusion, miss read, confusing
duplication, and unnessary reading of out of date instructions."*

**Verdict: no.** The controls are not structured to prevent these four problems. Every one of the
four was found, with evidence below. Nothing has been changed; §5 lists the options for your
decision.

How this was checked: file sizes and last-change dates from the file system and git; every file
reference in CLAUDE.md tested against the file system; `cfg_*` tables, rules and path settings read
from `iba/app/db/iba.db` (read-only); sample rules counted across every control file; the memory
folder and its index compared. Where a statement is my reading and not a measured fact, it is
marked **(inferred)**.

---

## 1. The controls that exist, and when each one is read

| Control | Size | When it is read | Claims to be | Last changed |
|---|---|---|---|---|
| `CLAUDE.md` | 703 lines, 115 KB | **Every conversation, in full, automatically** | "IMPORTANT: these instructions OVERRIDE any default behaviour" | 2026-10-20 |
| Memory index `MEMORY.md` | 12 KB | **Every conversation, automatically** | "Foundational — always apply" | 2026-10-20 |
| Memory files | 345 files, 1.06 MB | When recalled | Rules, feedback, project state | ongoing |
| `cfg_*` tables (38) | 82 behaviour rules (76 active, 42 KB of text); 236 settings; 14 escalation rules | Printed **in full** at every session start (`Start-Iba.ps1`), then each active rule restated in the compliance file | "The rules ARE the config" | ongoing |
| `iba/app/CHARTER.md` | 110 lines, 8 KB | Named as "start here" by the three files below | "this document wins" | 2026-10-13 |
| `iba/app/GOVERNANCE.md` | 4,309 lines, 360 KB | On demand; required update on every rule change | Overview of the mechanism; "config wins" | 2026-10-20 |
| `iba/app/BUILD.md` | 17,318 lines, 1.4 MB | On demand; required update on every code change | Build history | 2026-10-20 |
| `iba/app/USER-GUIDE.md` | 2,104 lines, 137 KB | On demand | "How to run it" | 2026-10-20 |
| `.claude/commands/*.md` (5) | 407 lines | When invoked | Session procedures | 2026-10-20 |
| `docs/interaction-preferences.md` | 69 lines | Named by CLAUDE.md §9 | Interaction protocols | 2026-07-23 |
| `docs/file-organisation-rules.md` | 544 lines, 29 KB | Named by CLAUDE.md §9 | Filing rules | 2026-09-28 |
| `Workflow/Instructions/` | 27 live files | Named by CLAUDE.md §10, cfg paths | "Authoritative detail" | July–Oct |
| `README.md` (repo root) | 814 lines, 35 KB | Not read by any routine | Technical reference guide | 2026-08-15 |
| `tasks.md` (repo root) | 199 lines, 27 open tasks | Not read by any routine | Task ledger | 2026-07-14 |
| `iba/config/README.md` | 70 lines | Warned against in CLAUDE.md | A second configurator design | 2026-07-23 |

**Controls you may not be aware of.** These shape what Claude does without being part of the
documentation set:

- **Four hooks** in `.claude/settings.json`:
  - Stop: the escalation backlog check
  - SessionStart: records the session boundary
  - UserPromptSubmit: tracks the prompt sequence
  - UserPromptExpansion: the Developer Mode freshness gate
- **Permissions at three levels**, which differ:
  - project `settings.json`: denies `AskUserQuestion`, and allows two commands for one July run id that no longer means anything
  - project `settings.local.json`: allows `Bash(*)`, Write and Edit outright
  - user `~/.claude/settings.json`: holds the auto-mode classifier's allow and deny text, which still names `engine.engine` and `scripts/apply_session_patch.py` (both superseded since 2026-08-17; the files still exist)
- **The statusline script** (`.claude/statusline-devmode.ps1`) and the Developer Mode marker file.
- **The compliance file** (`Logs/compliance/`), written and checked at every start and close.
- **Two Excel worksheets** that act as tool interfaces (`governance.ps_worksheet_path`, `governance.escalation_worksheet_path`).
- **208 non-archived files in `iba/docs/`** (proposals, test plans, phase records). No routine says which of them are live.
- **26 `README.md` files** under `_analytics/registry/word_registry/` and `_analytics/Bible_Books/`, from the old per-word layer.
- **The Windows scheduled tasks** for the NAS backups, described only in CLAUDE.md §13.

---

## 2. Unnecessary reading of out-of-date instructions

Before any work starts, a session reads about **200 KB of instructions**: CLAUDE.md (115 KB), the
memory index (12 KB) and the start-up print of rules and settings (about 70 KB). Much of it is out of date.

**CLAUDE.md is mostly a work diary, not instructions.** By line range:

| Part | Lines | Size | Share | State |
|---|---|---|---|---|
| Top banners (source, hold, ban, IBA start, superseded notes) | 1–74 | 7.0 KB | 6% | live |
| Narrative and strand history: M18, M64, M72, M09, M08, M07, flesh and body, OT-nn threads | 75–335 | **72.1 KB** | **63%** | a dated log; the study is on hold |
| Method reset banners (June–July) | 336–345 | 3.7 KB | 3% | legacy by its own wording |
| §1–§3 (project, directory map, schema v3.33.0) | 346–466 | 12.6 KB | 11% | §3 says its own framing is superseded |
| §4–§8 (engine, STEP client, pipeline, data flow) | 467–545 | 5.5 KB | 5% | marked "provenance only, not live" |
| §9–§10 (protocols, documents, "Current Programme State 2026-06-14") | 546–593 | 6.7 KB | 6% | §10 is four months old |
| §11–§14 (commands, git, environment, vocabulary) | 594–703 | 6.8 KB | 6% | §11 commands mostly retired |

So **about 75%** of the file read every conversation is history, superseded text or state that
belongs elsewhere: the narrative log, the method-reset banners, and §4–§8 and §10. It also carries
16 struck-through passages and 44 "superseded/stale/retired" markers that the reader has to work through.

**The start-up print** gives the full text of 76 rules, 52 governance settings and 14 escalation
rules, and the compliance file then asks for each of the 76 rules to be restated. Rules for study
work (classes `llm_output`, some `chat`) are printed and restated even in a Developer Mode session,
and in a session where the study is on hold. **(inferred)** This invites a rote pass over text that
doesn't apply, the opposite of what the restatement is for.

---

## 3. Misreading: stale content and pointers presented as live

**CLAUDE.md's file references.** 110 distinct file references were tested; **69 do not resolve**
from the project root:

- **6 full paths point to files since moved to an `archive/` folder:**
  - `wa-lexical-analysis-rules-reset-v1-20260624.md`
  - `m09-cluster-overview-v1-20261015.md`
  - `2000-open-threads-test-plan-v1-20261012.md`
  - `cost management 20260426.md`
  - `research/VE-lexical/00-INDEX.md`
  - `m18-strand-handoff-v2-20261009.md`

  Following the pointer finds nothing, or a newer version that the text doesn't mention.
- **About 55 are bare filenames** (e.g. `m72-group-B-reading-v1-20261012.md`). They can be found
  only by already knowing the folder, which is the same failure escalation rule 7 flags as `bare`
  for escalations.
- **Retired scripts are named as if usable:** `new_word.py` (deleted), `gap_fill.py` and `apply_session_patch.py` (superseded, still present), `scripts/build_file_manifest.py` and `database/file_manifest.json` (moved to archive).

**Statements in the control documents that are now false:**

| Where | Says | Live fact |
|---|---|---|
| GOVERNANCE.md header | The live config snapshot is `iba/app/config/CONFIG-REPORT.md` | That file does not exist; `cfg_setting configmaint.report_path` = `outputs/configs/CONFIG-REPORT.md` |
| GOVERNANCE.md §2 title | "20 `cfg_*` tables" | 38 `cfg_*` tables |
| CLAUDE.md §13 | Project memory is committed to git under `memory/` (a mirror of `.claude` memory) | `memory/` holds only `archive/` (241 files); the live 345 are not mirrored there |
| CLAUDE.md §10 | "Current Programme State (2026-06-14)", entry point `docs/project-orientation-core-memory-map.md` | The map was retired on 2026-08-18 (the same file says so a few lines earlier) |
| CLAUDE.md banner | "Start each session via start-project (GOVERNANCE.md + BUILD.md…)" | start-project does not read either file |
| `README.md` (root) | File server `G:\My Drive\…`, schema v3.1.0, engine 1.0.0 | The project left Google Drive on 2026-06-03; CLAUDE.md's first banner says to ignore that copy |
| `docs/file-organisation-rules.md` | Names `Sessions-v2/` (3 times) | That folder no longer exists (CLAUDE.md §2) |
| user `settings.json` auto-mode | Allows `engine.engine --report`; deny-lists `apply_session_patch.py` | Both superseded since 2026-08-17 (the files still exist) |

**Superseded text left in place.** The practice is to strike through or annotate, not remove (e.g.
CHARTER §4 keeps the struck "never tested in this same session" line beside its replacement). The
reader has to decide what is live on each line. Most of the corrections you have had to make in
chat this year are exactly this kind of misread. **(inferred)**

---

## 4. Confusion and confusing duplication

**Several documents claim to be the top authority:**

1. `CLAUDE.md` (delivered as "IMPORTANT: these instructions OVERRIDE any default behaviour")
2. `CHARTER.md` ("this document wins")
3. `GOVERNANCE.md` ("the config wins, always")
4. the `cfg_*` rules (`governance.rules_must_be_config_driven`)
5. five `Workflow/Instructions` files named `AUTHORITATIVE`, all from July, describing the old engine pipeline (e.g. `wa-term-add-update-AUTHORITATIVE-pipeline-v1-20260711.md` runs `engine.engine --mode=audit_word`, which CLAUDE.md §4 marks superseded)
6. memory, which marks entries "★★★ READ FIRST" and "always apply"

Nothing says which wins when two disagree, except pairwise claims (charter over config, config
over GOVERNANCE).

**The same rule lives in several places.** Counts of files (or mentions in a single file) carrying the rule:

| Rule | CLAUDE.md | GOVERNANCE | USER-GUIDE | BUILD | memory files | docs | commands | cfg row |
|---|---|---|---|---|---|---|---|---|
| `AskUserQuestion` banned | 1 | 0 | 1 | 0 | **7** | 1 | 0 | rules 16, 19 + settings deny |
| Let Scripture speak | 3 | 0 | 0 | 0 | 1 | 0 | 0 | rule 69 |
| Claims register keeps narrative honest | 1 | 1 | 0 | 0 | 1 | 0 | 0 | rule 77 |
| Read by role | 2 | 3 | 0 | 0 | 4 | 0 | 0 | rule 73 |
| Session close commits | 1 | 3 | 0 | 1 | 1 | 0 | 1 | setting |
| No GitHub publish, copy to learning4comfort | 3 | 9 | 1 | 10 | 2 | 0 | 1 | setting |

Each copy is worded differently and changed at a different time. When a rule changes, the cfg row
is updated, and the other copies are updated only if someone remembers.

**Duplicates that already contradict each other:**

- **Asking before acting:**
  - CLAUDE.md §9.1 and memory `feedback_interaction_protocols` (from `docs/interaction-preferences.md`): "before non-trivial tasks… WAIT for explicit approval"
  - memory `feedback_proceed_autonomously_on_stable_rules`: "proceed autonomously… do not stop for approval"
  - memory `feedback_no_approval_steps_researcher_feedback_in_chat`: "do NOT insert researcher approval steps"

  All three are marked as standing guidance. Which one applies is left to judgement in the moment.
- **Narrative writing guidance:** `cfg_setting method.inner_being_narrative_guidance_path` and
  `method.narrative_hard_constraints_path` point at July documents, while
  `narrative.inner_being_style_guide_path` points at the October style guide v2. A fourth,
  `wa-narrative-style-instruction-v1-20260702.md`, is also live in `Workflow/Instructions/`.
  **(inferred)** These overlap in subject; I haven't checked whether their content conflicts.
- **Two task ledgers:** `tasks.md` has 27 open checkbox tasks, last touched 2026-07-14, beside the
  escalation table that rule 40 makes the only home for open items.
- **Two configurators:** `iba/config/` versus `iba/app/` (CHARTER §3, GOVERNANCE §6). This is a
  known, unresolved fork that CLAUDE.md has to warn about in a banner.

**Memory.** 345 memory files; the index lists 115, so 230 are not in the index (some deliberately
demoted). 50 files carry "superseded/obsolete/retired" wording. Many repeat rules that now have a
cfg row, so memory has become a second rule store beside config. That is the very thing CHARTER
§1.6 rules out: "No rule that lives only in… an AI's memory".

**History mixed with the rulebook.** GOVERNANCE.md (360 KB) has a short current overview (§1–§8)
followed by about 60 dated increments, some of which change §1–§8 without §1–§8 being restated.
BUILD.md is 1.4 MB. To learn the current state of one mechanism you have to read its history.

---

## 5. Why it happens, and the options for your decision

**Three causes, all structural:**

1. **No control map.** Nothing states, for each kind of control (a rule, a setting, a procedure,
   study state, history, a pointer), which store is its one home, and that every other place only
   points to it.
2. **Append-only change.** Each change adds a dated note to the document that is already read. Nothing
   moves superseded text out of the always-read path, so the always-read files only grow.
3. **Restating a rule to make it stick.** When a rule was missed, the response was to copy it into
   one more place: CLAUDE.md, memory, a command, a banner. Each copy then drifts on its own.

**Options.** Each one is a decision for you; none is started:

| # | Option | Effect |
|---|---|---|
| A | **A control map in config.** One `cfg_*`-held list: each kind of control → its home → who reads it and when. Documents point to it; nothing restates a rule held in a cfg row. | Removes the authority question and stops new duplicates |
| B | **Cut CLAUDE.md to a short entry file** (identity, the hard bans, the study hold, how to start), with study and strand state moved to iba.db or a generated status report, and §3–§14 moved to history. | Cuts most of the 115 KB read every conversation |
| C | **Separate current from history** in GOVERNANCE, USER-GUIDE and BUILD: a current-state part regenerated from config, plus history files read only on demand. | Current state readable without the diary |
| D | **Retire the stale roots:** `README.md`, `tasks.md` (open items moved to escalations first), the five July `AUTHORITATIVE` instruction files, the dead `settings.json` entries and the user-level auto-mode lines, and the stale `iba/docs` files. | Removes the files most likely to be misread |
| E | **Memory pruned to what config cannot hold**, with the approval-behaviour contradiction resolved by one ruling and the copies of cfg rules removed. | One rule store, not two |
| F | **Scope the start-up print and the compliance restatement** to the rules that bear on the session's mode and the work in hand. | Restatement becomes real, not rote |
| G | **A mechanical check at session close:** every path in a control file resolves and is not archived; the always-read files stay within a size limit. | Stops drift coming back |

Suggested order, if you take them up: A first, since every other option depends on knowing each
control's home; then B and D, the largest reading load and misread risk for the least work; then E,
C, F and G.
