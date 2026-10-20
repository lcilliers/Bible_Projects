# The two session routines: `start-project` and `session-close`

> v1, 2026-10-20. What each routine does, step by step, as the code runs today. Written on the
> researcher's request (verbatim): *"I want to audit, check and modify the start-project and
> session-close routine, describe in a md exactly what each of these two routines accomplish"*.
> This file is the description (part 1). §4 lists what I found to be stale or weak while tracing
> the code. Those are findings for the audit. **Nothing has been changed yet.**

Sources read: `.claude/commands/start-project.md`, `.claude/commands/session-close.md`,
`iba/app/ps/Start-Iba.ps1`, `iba/app/init.py`, `iba/app/ps/Spine-Check.ps1`,
`iba/app/handlers/spine.py`, `iba/app/ps/Session-Close.ps1`, `iba/app/handlers/session_close.py`,
`iba/app/ps/Copy-NarrativeToLearning4Comfort.ps1`, `.claude/settings.json` (hooks),
`.claude/hooks/*.py` (headers), and the live `cfg_setting` paths.

---

## 1. How the routines are built

Both are Claude Code slash commands: markdown instruction files in `.claude/commands/`. **The
command file is a script for Claude, not for the machine.** Each step either runs a PowerShell tool
(which runs real code) or tells Claude to read, judge and write. So each step below is labelled:

- **[code]**: a script does it, and the outcome does not depend on Claude's judgement.
- **[Claude]**: Claude does it by reading and judging. Nothing checks that it was done, or done well.

Some session work runs outside both routines, as hooks in `.claude/settings.json`:

| Hook | When it fires | What it does |
|---|---|---|
| `SessionStart` → `session_boundary_track.py` | every session start, resume, clear, compact or fork | Records the session's start in `.claude/session-boundary/{session_id}.json`. `session-close` uses this record to fix its git window, and the Developer Mode gate uses it too. |
| `UserPromptSubmit` → `track_prompt_submit.py` | every prompt | Tracks the order of prompts. |
| `Stop` → `stop_check_escalation_backlog.py` | end of every turn | Blocks the stop once if escalations assigned to Claude are open. On-hold threads are not counted. |
| `UserPromptExpansion` (developer-mode) → `gate_developer_mode_entry.py` | `/developer-mode` | Refuses Developer Mode unless the session is new. |

---

## 2. `start-project`: what it does

**Purpose, as the command states it:** make the environment ready, orient on the open items, then
report and **stop**. It ends with a status report and a question, and never with work.

| # | Step | Kind | What it actually accomplishes |
|---|---|---|---|
| 1 | Git state | [code] + [Claude] | Runs `git status` and `git log -1`. Claude reports whether the tree is clean or dirty. It flags any uncommitted `SESSION-LOG-*.md` and commits nothing. |
| 2 | STEP server | [code] | Checks port 8989. If nothing is listening, it starts `C:\Program Files (x86)\STEP\step.exe` and polls every 5 s for up to 90 s. This only proves that the port is open. |
| 3 | IBA bootstrap: `Start-Iba.ps1` → `python -m iba.app.init` | [code] | (0) Checks that Python and `requests` are installed; if not, it exits 1. (1–2) If the config is not in `iba.db` yet, it validates and loads the config seeds (`cfgload.load`) and refuses incoherent config. Otherwise it leaves the config alone. (3) It creates the data tables if any are missing. (3b) It confirms that each `database.*.path` setting points at a real file. (4) It pre-flights STEP with a known-answer probe (a Strong's lookup that must give the expected gloss and verse count), so STEP is shown to answer, not just to be up. If STEP is required (`step.required_for_runs`) and does not answer, it prints NOT READY and exits 1. (5) It prints one orientation line each from `BUILD.md` and `GOVERNANCE.md`. (6) It prints **every** `governance.*` `cfg_setting` in full. This is the only place those rules are "used" (#305). (7) It prints READY. |
| 4 | Open escalations | [code] + [Claude] | `Escalation.ps1 -Action List` writes a versioned report (`outputs/escalation/escalation-list-vN-*.md`). Claude reads it and names the items relevant to the session. It may also look at recent `outputs/markdown/` and `outputs/session-logs/` files. |
| 4 (cont.) | Behaviour rules not mechanically enforced | [Claude] (ad-hoc SQL) | Counts active `cfg_behaviour_rule` rows by `enforcement_status`, other than `mechanically_enforced`. Any `judgment_call_pending` rows are named. A non-zero count of the old `not_mechanically_checkable` value is flagged as drift. |
| 4A | Spine check: `Spine-Check.ps1` → `handlers/spine.py` | [code] | **What it actually checks:** every Strong's code on a live `span` row must exist as a live `strong` row. Any missing code is FATAL; it is escalated once and the run pauses. It always writes `research/discovery/spine-check-vN-*.md`. It checks nothing else (see §4, S1). |
| 4B.1 | Thread check | [code] | `Escalation.ps1 -Action ThreadCheck`: an on-hold thread that in-progress work refers to moves to in-progress, and a thread item whose task has closed is closed. |
| 4B.2 | List threads | [code] + [Claude] | `-Action Thread` writes `outputs/escalation/escalation-threads-vN-*.md`. Claude reports the counts by state and names the in-progress threads. |
| 4B.3 | Threads bearing on the current strand | [Claude] + [code] | Claude works out the current strand from the CLAUDE.md strand queue and the last commit message. Then it runs `-Action Match -Cluster … -Strong … -Verse …`, which is read-only. |
| 4B.4 | Threads waiting on the researcher | [Claude] | Names open threads that have a researcher item. |
| 5 | Report and stop | [Claude] | A chat summary covering git, STEP, bootstrap, the spine check (FATAL findings first), escalations, threads and the rule count. It ends by asking what to work on. |

**What it changes on disk:** the config and data tables only when they are missing, and only
through init. It writes new versioned reports for the escalation list, the threads and the spine
check. The thread check may change thread states. **It never commits.**

**What it does not do:** it reads no memory or CLAUDE.md banners beyond what the harness loads
anyway. It does not check whether the narrative copy or the register is current. It does not check
the learning4comfort side. It does not check whether the last session ended with a session-close.

---

## 3. `session-close`: what it does

**Purpose, as the command states it (#1875, 2026-09-24):** check three things before hand-off.
(a) Every escalation touched in the session got a proper update. (b) Governance, config and doc
text that the chat decided should change did change, with superseded text marked. (c) Build work
is recorded in `BUILD.md`. Then copy the narrative, regenerate the threads register, commit and
push. **Detection is code and remediation is Claude.**

| # | Step | Kind | What it actually accomplishes |
|---|---|---|---|
| 1 | Detection: `Session-Close.ps1` → `handlers/session_close.py` | [code] | **Finding the session:** `CLAUDE_CODE_SESSION_ID`, or else the newest transcript that contains the `Session-Close.ps1` call. **Session start:** read from the SessionStart hook's boundary record. **(a)** It scans this session's JSONL transcript for the two confirmation lines that `Escalation.ps1` prints after a write (`raised — #N. Update with` and `escalation #N vV ->`), and takes the highest version seen for each id. A gap is counted only when the live `escalation_history` version is **lower** than the version the transcript shows. **(b)** It lists which of `iba/app/GOVERNANCE.md`, `CLAUDE.md` and `iba/app/USER-GUIDE.md` changed in the git window, from the last commit before the session start to HEAD, plus uncommitted files. It judges nothing. **(c)** If any file under `iba/app/` changed (excluding `reports/`, `.md` and `.db`) and `iba/app/BUILD.md` did not change, every such file is a gap. It always writes `iba/app/reports/session-close.md` (versioned) and always exits 0. |
| 2 | Read the report | [Claude] | — |
| 3 | Fix the (a) gaps | [Claude] | For each gap id, Claude re-reads the chat and writes an `Escalation.ps1 -Action Update` (or `Correction`). The entry carries the researcher's words verbatim, the design debate, the decisions and anything skipped. No approval is needed. |
| 4 | Fix the (b) drift | [Claude] | Claude re-reads the session's decisions against GOVERNANCE.md, CLAUDE.md, USER-GUIDE.md and any relevant `cfg_*` row. It makes the missing doc edits, files config changes through `Config-Maintenance.ps1 -Step Propose`, and marks superseded text. A genuinely new conflict becomes a new `decision_required` escalation. |
| 5 | Fix the (c) gaps | [Claude] | Claude writes a `BUILD.md` entry (`## N.`, with Build, Test plan run, Not done here and Files). |
| 6 | Re-run the detection | [code] | Confirms 0 (a) gaps and 0 (c) gaps. |
| 6a | Copy the narrative: `Copy-NarrativeToLearning4Comfort.ps1` → `lib/narrativecopy` | [code] | Copies the current file of each active `narrative_chapter` row (`narrative.copy_source_dir`) to the learning4comfort inbox (`narrative.learning4comfort_inbox_dir`). Older versions of the same file are replaced, and nothing else there is touched. It runs no git. It runs every close, even when nothing has changed. |
| 6b | Regenerate the threads register: `Escalation.ps1 -Action Export -Type thread` | [code] | Rewrites `_analytics/cross-cluster-web/open-threads-register.md` from the escalation table. |
| 7 | Commit and push | [Claude] + git | This step is standing pre-authorisation (`governance.session_log_triggers_commit`). It stages **all** outstanding changes (excluding `bible_research.db` and `backups/`), reading anything unfamiliar first. It commits `session YYYYMMDD: …`, pushes, and shows `git status` and the push output. |
| 8 | Report | [Claude] | A chat summary of the findings, the fixes, any new decision items and the commit/push output. |

**What it changes:** escalation history, docs and config proposals, BUILD.md, the learning4comfort
inbox and the threads register file. It also makes a git commit and push.

---

## 4. Findings from tracing the code (input to the audit; nothing changed)

Each finding is something I checked against the code or the live data.

### start-project

- **S1. Step 4A describes a check that no longer exists.** The command says the spine check covers
  "strong-extended-meaning-parse completeness" and "a discoverability pass". Both were **removed
  on 2026-09-11** (#1681/#1684/#1686; see the `handlers/spine.py` docstring and the
  `Spine-Check.ps1` synopsis). The live check is one set difference: span Strong's codes minus
  live `strong` rows. Despite its name, it does **not** check that verses and spans are in sync.
- **S2. Step 4 gives the wrong report path.** It says `iba/app/reports/escalation-list.md`. The
  live setting `escalation.list_report_path` is `outputs/escalation/escalation-list.md`
  (versioned).
- **S3. Session logs have stopped.** The newest is `Logs/SESSION-LOG-20260929-…`. No log was
  written from 2026-09-30 to 2026-10-19, although `governance.session_log_required_content`
  requires one and **neither routine writes one**. ~~`Logs/` holds no session logs; either the
  setting or the practice needs to be ruled on~~ (corrected 2026-10-20: wrong; `Logs/` is the
  configured folder and holds the logs. I listed only part of the folder instead of reading the
  setting. The practice is what failed.)
- **S4. Step 3 prints every `governance.*` setting in full** (about 40 long values) at every
  start. This is by design (#305), but it is a large, mostly unread block in every session's
  context. Raise it if cost matters.
- **S5. Two STEP checks.** Step 2 (port) and init step 4 (known answer) overlap by design. Only
  the second proves that STEP works.
- **S6. No check on how the last session ended.** Start does not check whether the last
  session-close report is clean or whether the newest commit is a session-close commit. A missed
  close shows up only as a dirty tree.

### session-close

- **C1. Check (a) compares records with records.** The transcript lines it looks for are printed
  by `Escalation.ps1` *after* the database write succeeds. So the live history is almost always at
  or above the transcript version, and a gap can arise only if a write was later lost. **The check
  cannot detect what it was built for:** an escalation discussed or decided in chat but never
  updated, an update that leaves out the researcher's words, or an open item raised in chat but
  never raised as an escalation (rule 21). This is the same weakness #2172 records for the study,
  where controls check records against records rather than the work against its record.
- **C2. Check (b) is a list, not a check.** It names three changed files. Whether the decisions
  reached the docs and config depends entirely on Claude, and the step 6 re-run cannot fail on it.
  It does not look at `cfg_*` changes, the CLAUDE.md strand queue, memory files, the narrative
  chapters or the claim register.
- **C3. Check (c) is cleared by any change to BUILD.md.** One BUILD.md edit clears every code gap,
  whatever it covers. `.claude/` files (hooks and commands, such as these two routines) are
  outside its scope. The `.md` exclusion also leaves USER-GUIDE.md and GOVERNANCE.md changes out
  of the BUILD check.
- **C4. The git window depends on the hook record.** If the SessionStart boundary record is
  missing, (b) and (c) are skipped. The report says so, but the step still exits 0 and the step 6
  "re-confirm clean" can pass.
- **C5. Study controls are not part of the routine.** The commit history shows that narrative
  work was closed with quote checks, the register `Check` and the "copy verified 35" line. Of
  these, only the copy (6a) and the threads export (6b) are in the command. The register check,
  quote checks and narrative/register consistency are run (or not) at Claude's discretion. This
  is part of #2172's "no control enforces completeness".
- **C6. No session log** (see S3), although `governance.session_log_triggers_commit` names a
  session log as one of the two commit triggers.
- **C7. "Report" means chat only** (step 8). The close's own decisions and remediations are not
  persisted anywhere except in the escalation updates and the commit message.

---

## 5. Next step

These findings are not a change plan. Proposed modifications will follow in a v2 or a separate
proposal file, once the researcher has said which findings to act on and in what direction.
Tracked on escalation #2173.
