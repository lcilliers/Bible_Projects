# #2189: Permission settings — what each does, for a decision (v1, 2026-10-21)

Escalation #2189 (from #2182 §5; an element of the IBA app reset, #2177). Researcher, verbatim:
*"§5 permissions: create escalation to resolve these - I need more information before
decision."* These are Claude Code permission settings. Claude doesn't change them; each change
below is yours to make.

**How the three levels combine.** Claude Code merges the user file (`~/.claude/settings.json`), the
project file (`.claude/settings.json`, committed to git) and the local file
(`.claude/settings.local.json`, not committed). An `allow` entry in any of them lets a tool call
run without asking. A `deny` entry blocks it everywhere. The `autoMode` lines guide the classifier
that decides, in auto mode, whether an action not otherwise allowed runs, needs approval, or is
refused.

## 1. `.claude/settings.json` (project, in git)

| Entry | What it does | Effect of removing it |
|---|---|---|
| `deny: AskUserQuestion` | blocks the question tool (rule 16) | the ban would rest on the rule alone. **Keep.** |
| `allow: Escalation.ps1 -Action AnswerRun -RunId RUN-20260722_065351_662-CONFIGMAINT -Decision Approve` | pre-approves one exact command for one run from 22 July; that run has no open escalation | none. It can't match anything again, and it is also covered by the local file's `PowerShell(.\iba\app\ps\*)`. **Safe to remove.** |
| `allow: Config-Maintenance.ps1 -Step Validate -RunId RUN-20260722_065351_662-CONFIGMAINT` | the same, for one Validate run | none, for the same reasons. **Safe to remove.** |

## 2. `.claude/settings.local.json` (this machine only, not in git)

| Entry | What it does | Effect of removing it |
|---|---|---|
| `Bash(*)` | every Bash command runs without asking | Bash commands would ask unless another entry or auto mode allows them. This is the broadest entry, and it makes most of the narrower Bash entries below redundant. |
| `Read`, `Glob`, `Grep` | read-only file tools run without asking | more prompts on reads; no safety gain |
| `Write`, `Edit`, `NotebookEdit` | file writes run without asking | each file change would ask; this is the setting that most changes how much you approve by hand |
| `Agent`, `WebFetch`, `WebSearch` | subagents and web access run without asking | each would ask. Subagents are banned by default for cost, so prompting would add a check. |
| `Bash(export PYTHONUTF8=1)`, `Bash(python -c ' *)`, one `build_dbschema.py --digest …` command | narrow Bash entries | none while `Bash(*)` stays (they're redundant under it) |
| four `PowerShell(… iba/app/ps/*)` patterns | every IBA PowerShell tool runs without asking, in any of the four ways it's written | IBA tools would ask each time; these match how the app is meant to be run |

## 3. `~/.claude/settings.json` (your user file, all projects)

| Entry | What it does | Effect of removing it |
|---|---|---|
| `allow: Bash(export PYTHONUTF8=1)`, `Bash(git add *)`, `Bash(git commit *)`, two `build_dbschema.py` commands | run without asking in every project | `git add`/`git commit` would ask in other projects too; the session-close commit cycle would ask here unless the local `Bash(*)` stays |
| `allow: PowerShell(Config-Maintenance.ps1 -Step Validate)` | read-only validate without asking | none while the local PowerShell pattern stays |
| `autoMode.allow`: `sqlite3 database/bible_research.db` | the classifier treats reading the research DB with `sqlite3` as routine | reads of that DB would be judged case by case; it is the prose store and still read |
| `autoMode.allow`: `python -m engine.engine --report/--db-status/--export-word` | the classifier treats the old engine's read-only commands as routine | none in practice: the engine has been superseded since 2026-08-17 and nothing calls it. **Safe to remove.** |
| `autoMode.soft_deny`: `python -m engine.engine --migrate` | the classifier asks before an engine migration | none in practice for the same reason. Keeping it does no harm and still guards against an accidental run. |
| `autoMode.soft_deny`: `scripts/apply_session_patch.py` without `--dry-run` | the classifier asks before a live patch to the research DB | **Still in use.** The prose steps (`Prose.ps1` ImportChapter, SetStatus, FlagFixApply) produce patches that this script applies. **Keep.** |

The two `autoMode` text lines show `â€”` where a dash was meant (an encoding slip when they were
written). It is cosmetic; the classifier reads the rest.

## Decisions

1. **Remove the two dead project allows** (§1, rows 2–3)? These are the only entries that are plainly dead.
2. **Remove the engine `autoMode.allow` line** (§3)? It's dead. The engine `soft_deny` can stay as a guard.
3. **`Bash(*)`, `Write` and `Edit` in the local file** are a choice about how often you approve by
   hand, not about stale entries. Nothing in the reset requires changing them.

To make a change, edit the file in a terminal you open yourself. From an interactive `claude`
terminal you can also use `/permissions`.
