# 2177 — Reading waste: why each control exists, and what to change

Escalation: #2206 (an element of the #2177 reset). Status: for the researcher's decision. Nothing
built. v1 (archived) proposed options without asking why each control was there.

## The instructions

Researcher, chat 2026-10-21 (verbatim): "my observation is that the there is a lot of
inconsistencies, redundant routines, incoherent rules still in the active processes. a) configs have
a long list of incoherent notifications/warning (#2197). Remember everything you read which is not
necessary/just result in an error or exception/ not coherent is a waste of real money in terms of
costs and tokens. [...]"

Researcher, chat 2026-10-21 (verbatim), on v1: "how can I approve this if you have not even
investigated why the control was there in the first place and why it now suddenly become
redundant?"

## Summary

None of the five controls has become redundant: the reason each was built still holds. What is
wasteful is how three of them do their job. Each one now either:

- duplicates a control built later,
- re-asks a question already answered, or
- has drifted from the standard it was built to.

| # | Control | Built because | Reason still holds? | What is wasteful | Kind of change |
|---|---|---|---|---|---|
| 1 | Validate raises an escalation for advisory findings | Researcher, 2026-07-30 (BUILD.md sec 42) | Yes | The escalation stores the full findings (41 KB), against the sec 42 standard. 63 such escalations raised so far, 35 approved as "known". | **Standard deviation**: fixed by Claude without a decision (rule 98). The re-asking part needs your decision. |
| 2a | "Unenforced behaviour rules" list in validate | Researcher, 2026-09-03 (#1384, BUILD.md sec 221) | Yes | 68 of the 81 listed rules gained a control on 2026-10-20 (the compliance file), so the list double-counts them. | Decision |
| 2b | "Low config density" utilities in validate | governance.utility.config (2026-07-29/30, BUILD.md sec 42) | Yes | 10 utilities re-listed every run with no decision ever made on them. | Decision, once per utility |
| 3 | Compliance file restates every rule | Researcher, 2026-10-20 (#2173 P2, BUILD.md sec 353; scoped by #2185, sec 360) | Yes | 9 governance settings are plain values (paths, formats), not rules. | Decision |
| 4 | Escalation list shows full history | No ruling found. It came with the 2026-08-20 escalation rebuild (BUILD.md, the #715 history loss). | No ruling to hold | 13 parked items printed with every version. | Decision |
| 5 | Stop hook on Claude-held items | Researcher session 2026-08-31 (commit 790d0cfc). #1312/#1314 had gone stale, and a written rule had already failed. | Yes | It fires on items worked this same session, e.g. #2177 on every turn. | Decision |

## 1. Validate escalations

**Why it is there.** BUILD.md sec 42 (2026-07-30) records the researcher's feedback on an escalation
that "dumped all 14 low-config-density-utility findings inline":

> "really difficult to manage... a long list of a variety of defects requiring different types of actions."

The standard set then:

- the full detail goes to CONFIG-REPORT.md;
- the escalation carries counts and the report path;
- a capped sample is kept.

**What it does now.** `iba/app/handlers/configmaint.py` (`validate`, final `escalate(...)`) passes
every finding list as `preset`. That is stored in `escalation.context`: #2197 holds 41,180
characters, and the six before it (#2104 to #2113) hold 36-40 KB each. This breaks the sec 42
standard. Under rule 98 Claude fixes it: counts plus the report path only. It is built on a copy and
tested.

**The part that needs your decision.** The step ends `decision_required` whenever any advisory list
is non-empty: "approve to acknowledge as known/acceptable". Since then:

- 63 advisory escalations have been raised;
- 35 were approved as acknowledged;
- the rest were mostly superseded by the next run.

Rule 44 says a decision asked again run after run is a design gap.

**Option 1.** Validate fails, and raises an escalation, only on a finding that is NEW since the last
acknowledged run. Known findings stay in CONFIG-REPORT.md and are not re-asked. #2197 is closed:
its content predates #2198/#2200 (it reports 165 unregistered scripts that were since retired).

## 2a. Unenforced behaviour rules

**Why it is there.** #1384, researcher (BUILD.md sec 221):

> "you create half baked rules from instructions, do not persist to ensure that you get answers, and think the job is done if you make a note..."

The instruction was a permanent list of unenforced rules, with the reason, in every validate run.
It exists so that no rule is silently ignored.

**What changed.** On 2026-10-20 (#2173 P2) the compliance file was built for this exact gap:

- every `context_delivered` rule is restated at start;
- it is proved with evidence at close (SC6).

So the 68 `context_delivered` rules now have a control. The list still counts them as unenforced.
Live counts of the 81 listed:

| Status | Rules |
|---|---|
| context_delivered | 68 |
| partially_enforced | 9 |
| buildable_not_built | 3 |
| deliberately_deferred | 1 |

**Option 2a.** The list counts only rules with no control: partially enforced, buildable but not
built, and deferred (13). The 68 are covered by the compliance check. The list stays, as #1384
requires.

## 2b. Low config density

**Why it is there.** It is the check for `governance.utility.config`: each utility has its own
config. 11 utilities were already exempted through `cfg_utility.config_exempt` (BUILD.md, 2026-07-30).

**What is wasteful.** The 10 utilities still listed have been re-reported on every run, and no one
has decided on them.

**Option 2b.** Claude puts the 10 to you once, each with what the utility does and whether it reads
any setting. You exempt it or ask for its config. After that the check reports only new cases.

## 3. Compliance file

**Why it is there.** #2173 P2, researcher, 2026-10-20 (verbatim):

> "What step can I take as part of the behaviour section to ensure that you read and understood the governance and config rules and acknowledge that you will comply with it."

#2185 (option F) then scoped delivery to the session: study rules are left out while the study is
on hold, and code-building rules appear only in Developer Mode. The reason holds: the file is the
proof that rules are read.

**What is wasteful.** 9 of the 52 governance settings are plain values, not rules:

- `oneoff_report_dir`, `oneoff_report_naming_pattern`, `oneoff_report_format`,
  `oneoff_report_archive_dir`
- `scripts_ps_dir`, `scripts_python_dir`
- `session_log_dir`
- `ps_worksheet_path`, `escalation_worksheet_path`

The code that uses each of them reads it. Restating "md" or "Logs/" proves nothing. The rules that
govern them (naming-shape, filing, worksheet sync) are restated separately.

**Option 3.** The 9 plain-value settings leave the compliance file, and stay in `cfg_setting` as
they are. Further scoping by subject is not proposed: it would cut what is read, against P2's
intent, without your ruling.

## 4. Escalation list history

**Why it is there.** No ruling asks for it. It came with the 2026-08-20 escalation rebuild, after
the #715 history loss. The history itself is kept in `escalation_history` and shown by
`-Action History -Id n`, so the list does not need to carry it (inferential: the rebuild's record
does not say why history was put inline).

**Option 4.** The list shows each open item's latest version. Parked items appear as one line each
(id, state, title). Full history comes only from `-Action History`.

## 5. Stop hook

**Why it is there.** Commit 790d0cfc (2026-08-31): built "so backlog items assigned to Claude can't
silently go stale the way #1312/#1314 just had -- a written rule had already failed at exactly this
once." It was narrowed once already: on-hold threads are left out (BUILD.md, the thread import).
The reason holds.

**What is wasteful.** It fires on an item worked in this same session. #2177 was updated this
session (v20) and still triggered a full extra turn twice.

**Option 5.** The hook leaves out an item whose latest version was written in the current session,
since that item is not stale. Items untouched this session still block, as built.

## Decision

| Option | Approve / reject / revise | Comment |
|---|---|---|
| 1 (re-ask only new findings; close #2197) |  |  |
| 2a (unenforced list: only rules with no control) |  |  |
| 2b (10 utilities put to you once) |  |  |
| 3 (9 plain-value settings out of the compliance file) |  |  |
| 4 (list: latest version; parked one line) |  |  |
| 5 (stop hook skips items worked this session) |  |  |

Not a decision: the sec 42 deviation (full findings stored in the escalation) is fixed by Claude
under #2206.
