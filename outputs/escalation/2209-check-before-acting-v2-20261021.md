# 2209 — Check before acting: every operation knows its rules, and they are put in front of Claude at the point of use

Escalation: #2209 (an element of the #2177 reset). v1 (archived) gave the evidence and a first
design.

## The instruction

Researcher, chat 2026-10-21 (verbatim): "making this rule work, would do two things: a) verify that
every process know exactly what rules should be in place, are are in place for each operation b) get
rid of this layer on layer of secondary double check validations and elaborate reads which have
become just a waste as it has never delivered any consistent and repeatable behaviour. maybe the
change is too big, and the expectation is unrealistic. if that is the case, then do not proceed with
going down this track. if it is realistic, and achievable, then proceed with doing it accross the
board for the project."

## Assessment: realistic, with one stated limit

**Size, measured 2026-10-21:**

| Item | Count |
|---|---|
| PS tools | 38 |
| Active steps | 97 |
| Behaviour rules (always or developer_mode) | 80 |
| Behaviour rules (study_active) | 26 |
| Escalation rules | 13 |
| Governance settings that are rules | 44 |
| Method rules | 116 |

The method rules are already tied to a step (`cfg_method_rule.step`). What is missing is the link for
the other about 160 rules. Linking them is a one-time classification of known size, and validate can
then check it every run.

**Mechanism.** A `PreToolUse` hook can refuse a command and hand the reason to Claude. The project's
retired-script gate (`.claude/hooks/gate_retired_script.py`) already works this way. The same
mechanism can put the rules of an operation in front of Claude the first time that operation is used
in a session. Claude then re-issues the command with the rules in view.

**What it covers.** Every PS tool (by action and step), git, migrations and database queries, and
every file write (Edit and Write, by path). That is where all 6 slips of this session happened (v1),
and where the study rules apply (files under `_analytics/`).

**The limit.** About 45 rules are conduct rules with no single point of action: no guessing, show
the evidence, record open items, confirm before non-trivial work, and similar. They stay as a short
general set read at start. The hook makes sure the right rules are in front of Claude at the moment
of acting. It cannot make Claude apply a rule well; only the refusals for a missing required
parameter are fully mechanical.

**Verdict.** Achievable across the project in this and the next session.

- Part (a) is fully achievable: a link table, plus a validate check that every rule is linked and
  every tool has its rules.
- Part (b) follows once (a) is live. The start read drops from 138 rows to the general set. Each
  remaining check is then assessed on its origin, as in #2206, before any is removed.

## Design

**Table `cfg_rule_scope`** (iba.db), one row per link:
- `rule_ref`: `B:<id>`, `E:<id>` or `G:<key>`
- `scope_kind`: `cfg_enum rule_scope_kind`, one of:
  - `general`
  - `ps`
  - `command`
  - `path`
- `scope_value`, by kind:
  - `ps`: a script name, with or without an action or step (`Escalation.ps1`,
    `Escalation.ps1 -Action Update`)
  - `command`: one of `git`, `migration`, `sqlite`
  - `path`: a glob (`iba/app/**`, `_analytics/**`, `**`)
- `inactive`

Method rules keep their own `step` link: a PS tool brings the method rules of its work package's
steps.

**Hook `.claude/hooks/rules_at_point_of_use.py`** (PreToolUse; Bash, PowerShell, Edit, Write):
1. Find the operations in the call:
   - PS scripts with their `-Action` or `-Step`;
   - `git`, a migration run, a `sqlite3` use;
   - the path being written.
2. Collect the linked rules and, for a PS tool, the method rules of its steps.
3. If any of those operations has not been shown in this session, refuse once. The reason gives each
   rule's full text from the database, and for a PS tool its own help lines for that action. Record
   the operations as shown.
4. The re-issued call passes. An internal error lets the call through and is logged, as the retired
   gate does.

**Validate check** `find_rule_scope_gaps`:
- every delivered rule has at least one link;
- every PS tool and every write area has at least one rule;
- every method rule names an active step.

The last point finds 2 today: `lexical.enrich` and `passage.suggest_boundary`.

**Start routine:** delivers only `general` rules once the hook is live. That is a change to #2173
P2, which you asked for. It is done in step (b), as its own decision with its origin set out.

## The mapping

The mapping is Claude's classification and is inferential (rule 4). It is in the migration, and
listed by rule in the test results for review as a whole, not item by item (rule 106).
