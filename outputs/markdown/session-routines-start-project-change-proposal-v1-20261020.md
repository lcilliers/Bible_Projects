# start-project: change proposal (with the parts that move to session-close)

> v1, 2026-10-20, escalation #2173. Follows the description
> `session-routines-start-close-description-v1-20261020.md`, whose §2 has the step numbers used
> here. Researcher's direction (chat 2026-10-20, verbatim):
>
> *"starting with start-project: 1) 2.4 the reports or links mentioned in every open escalation
> must be read and taken into account, not only the folders mentioned in 2.4 ; 2.4cont behaviour
> rules: counting the rules are meaningless. the rules must be read:- return a confirmation a) you
> read and will apply the behaviour rules b) explicitely name any behaviour rule that is a conflict
> or not followed with the reason; 2.4A the spine: move the spine check to the session-close, do
> not do the spine check at session start. fix and extend the base-data spine integrity check. the
> meaning tables (3) must be checked for completeness and not ignored as currently; add analysis
> integrity check: confirm that each observation in the session was recorded in the claims tables
> and that each open/referred/to be clarified item is recorded in the open item register. 2.4B the
> threads start up work is incomplete. it does not do any quality or validity work, does not do any
> integrity checks. Counts and stats are meaningless if they do not lead to real disclosure. I
> noticed your start-project finding - include fixing these also."*
>
> **Status: proposal. Nothing is built.** Q1–Q3 answered 2026-10-20 (§7); edited in place
> (review mode).

---

## 1. Principle for every change

The researcher's point *"counts and stats are meaningless if they do not lead to real
disclosure"* applies to the whole routine. Every check below therefore:

- names each finding (which escalation, which rule, which thread item, which verse), with the
  reason it is a finding;
- persists that list to a report (`governance.reports_must_persist`);
- is reported in chat by its findings, never by a total alone. "0 findings" is reported only when
  the check actually ran over a stated scope.

## 1a. P0: no meaningless reports or checks at start (added 2026-10-20)

Researcher (verbatim): *"then stop printing reports that have no meaning. If I want to inspect
the report, I request it on demand. scale down every any start up check that is meaningless."*

The rule: **a start-up item is kept only if it can change what happens in the session. A kept
item is silent when it passes and speaks only when it finds something.** Reports are written on
demand, not at every start. The exception is a report that carries findings the session must act
on.

| Item at start today | Decision | What remains |
|---|---|---|
| `git status` / last commit | keep, scaled down | silent when clean; speaks if the tree is dirty, a session log is uncommitted, or commits were made after the last close (S6) |
| STEP port probe (step 2) | keep as launcher only | starts STEP if it is down; no report line |
| `Start-Iba`: config loaded, data tables present, database paths | keep the checks | silent when they pass; a problem is reported and stops the start |
| `Start-Iba`: STEP known-answer probe | keep | silent when it passes; NOT READY is reported |
| `Start-Iba`: BUILD.md / GOVERNANCE.md one-line "orientation" | **drop** | — (the docs are read when work on the app is in hand) |
| `Start-Iba`: "first run: New-Word.ps1" hint | **drop** | — |
| `Start-Iba`: governance settings printed | **change** | no longer a printed report: delivered in full with the behaviour and escalation rules as the input to the compliance file (P2 B), which is what makes them read |
| behaviour-rule count by `enforcement_status` | **drop** | replaced by P2 |
| `Escalation.ps1 -Action List`: a new versioned report every start (v178 on 2026-10-20) | **drop at start** | on demand only. Start uses P1 (`-Action Context`, open escalations only), and chat names the open items with what their files show |
| spine check, report every start (v65) | **drop at start** | moves to session-close (P3) |
| `-Action ThreadCheck` | keep | silent unless it moves a thread or closes an item; then each move is named |
| `-Action Thread`: a new versioned threads report every start (v21), and counts by state | **drop at start** | on demand only. Replaced by P5 `ThreadAudit`, which reports findings by item and is silent when there are none |
| `-Action Match` for the strand in progress | keep, conditional | only when a strand is in progress; with the study on hold it does not run |
| threads waiting on the researcher | keep, scaled down | named only when the researcher's answer is what blocks the work in hand |
| recent `outputs/markdown` and session-log files | **drop** | P1 reads what the open escalations point to; the last session log is read when S6 says the last close is incomplete |

**The step-5 report becomes:** what is wrong or needs action (FATAL first); the open escalations
with what their files show; the compliance file result (P2); then the question of what to work
on. There is no line for a check that passed, and no totals.

**Reports on demand:** the escalation list, the threads list, the spine check and the config
report all stay available as commands; they are run when the researcher asks for them.
(`governance.reports_must_persist` still applies whenever one runs.)

The same rule is to be applied to session-close when it is taken up. Candidates are the "unchanged"
lines of the narrative copy, and the threads register regenerated at every close.

---

## 2. P1: read what every open escalation points to (step 4)

**Now:** Claude reads the escalation list report. That report cuts the `context` and `resolution`
cells to about 50 characters, so the files an escalation names cannot even be seen from it.

**Change:**

- **Scope (corrected 2026-10-20).** Researcher: *"there are only 4 open escalations. Where do you
  get 35?"* The 35 wrongly counted parked items as open: 12 tasks and issues (8 of them on-hold)
  plus 23 on-hold threads. **Open means raised, in-progress or re-assigned.** On 2026-10-20 those
  were #2161, #2166, #2171 and #2172, which is also the list report's own "3 active, 1
  in-progress". On-hold items are parked; their files are read when they are taken up. On-hold
  threads are covered by P5's integrity audit, not read in full at start.
- **[code] New `Escalation.ps1 -Action Context`.** For every open escalation (raised,
  in-progress, re-assigned), it collects every file path and link named anywhere in the item, in
  every version: the content (`comment`, `tried`, `short_description`), `context` and
  `resolution`. Researcher, 2026-10-20 (verbatim): *"check in content, context and resolution
  becuase you are not consistent in where you put the links."* The search does not rely on links
  being in `context`.
- **Latest versions only.** Researcher, same instruction: *"only read latest versions of the
  files"*. Each path is resolved to the newest live version of that file:
  - same base name, highest `-vN`, outside `archive/`;
  - a path that names an older or archived version is mapped to the current one;
  - the same file named more than once (across versions or fields) is listed once.
- **The report.** It writes `outputs/escalation/escalation-context-vN-*.md` with one section per
  escalation: its title, its latest state and next action. Then each resolved file: the path
  named, the field and version it was named in, the latest version it resolves to, and whether it
  exists (size, last change).
- **A file that cannot be found is a finding.** That means no live version under that base name.
  An escalation that points at nothing is broken.
- **[Claude] Read intelligently.** Claude reads the latest version of each listed file, with the
  escalation's question in mind. The aim is what the file shows that bears on the item's next
  action: for example, what is decided and what is still open in it. A newer version that
  supersedes what the escalation describes is said so. In the step-5 report Claude says per
  escalation what the files show (for example "#2171: M53 summary v2 awaits review; batch 1
  corrections Neh 6:13 and Psa 69:9 not applied"). It does not just name the escalation.

## 3. P2: rule compliance, read at start and proved at close (step 4 cont.; rewritten 2026-10-20)

**Now:** a count by `enforcement_status`, and `Start-Iba` prints the governance settings, whose
content is then ignored.

**Why the first draft was not enough.** Researcher, 2026-10-20 (verbatim): *"i am now not
convinced that the behaviour section is complete, as the behaviours is insufficient to ensure that
you comply with the governance rules and config. You print the config report, but you ignore the
content. What step can I take as part of the behaviour section to ensure that you read and
understood the governance and config rules and acknowledge that you will comply with it."* Then:
*"incomplete"*.

The first draft was incomplete in two ways:

1. **It covered one rule set of four.** The live rules are:
   - 52 `governance.*` settings (about 17k characters)
   - 74 active behaviour rules (about 40k characters): 23 mechanically enforced, 41
     context-delivered only, 6 partial, 3 buildable but not built, 1 deferred
   - 14 escalation rules (`cfg_escalation`)
   - 116 method rules (`cfg_method_rule`)
2. **It ended at an acknowledgement.** An acknowledgement at start is what already failed.
   `governance.session_log_required_content` was printed at every start in October, and no log was
   written. Nothing at start can prove that a rule is understood; only what is done can show it.
   So the control has to be **a statement of what each rule requires at start, checked against
   evidence at close**.

**The change has four parts:**

- **A. Deliver (code).**
  - `Start-Iba` prints in full every active governance setting, behaviour rule and escalation rule.
  - Method rules are delivered by area, when work in that area starts (a strand, a word run, a
    weave). They are not all printed at session start, because most concern work not in hand.
  - The text comes from the DB, never from memory.
- **B. Restate what each rule requires (Claude, checked by code).** Claude writes a session
  compliance file, `Logs/compliance/COMPLIANCE-{date}-{session}.md`. It has one line per rule id:
  - **what the rule requires of me in this session**, in Claude's own words and applied to the
    work in hand (for example, for `governance.session_log_required_content`: "end with
    `Logs/SESSION-LOG-20261020-*.md` holding the six items, before the commit");
  - or **"not engaged this session"**, with the reason (for example, a STEP-run rule when no word
    run is planned).

  Code checks that every active rule id has a line, with none missing. It also flags any line
  that copies the rule text instead of restating it, by text similarity. A copied line is not
  understanding.
- **C. Acknowledge and name conflicts (Claude).** The compliance file and the step-5 report carry:
  - the statement "I have read the governance settings, behaviour rules and escalation rules, and
    will comply with them";
  - by id, every rule that conflicts with another rule, a CLAUDE.md banner or memory (both sides
    named);
  - by id, every rule that is not being followed or cannot be, with the reason. The code aid
    supports this: a rule that names a retired file, table, step or setting is listed.
- **D. Prove at close (session-close, code and Claude).**
  - Every rule marked as engaged gets its evidence: a file path, an escalation id and version, a
    commit hash, or a command's output.
  - Code checks every evidence item that can be checked mechanically (the file exists, the
    escalation version exists, the commit exists).
  - **An engaged rule with no evidence, or with evidence that does not check, is a finding** in
    the close report, by rule id. A rule that turned out to be engaged although the start said
    "not engaged" is to be added with its evidence.
  - Over time, each context-delivered rule gets an `evidence_check` in config. The 41 rules that
    today are only printed then become rules whose compliance is checked.

**What you can do, as the step in the behaviour section:**

- **Review the close return**, not the start acknowledgement. The close report lists, by rule id,
  every rule without evidence and every rule not followed. That list tells you whether the rules
  were applied.
- **Spot-check the start file.** Pick any rule id and compare its line with the rule. A wrong,
  vague or copied restatement means the rule was not understood. The session stops there and the
  rule is re-read before any work.
- **Make the gate hard.** Step 5 does not end with "what shall we work on" until the compliance
  file passes code check B. Session-close does not commit while any engaged rule is without
  evidence, unless that rule is named in the close report with its reason.

**What this cannot do.** No step proves understanding in advance. Part B makes ignoring a rule
visible at the start; part D makes not applying it visible at the end. Between the two, it is
your review of the D list that confirms compliance.

- **The count is dropped.**

## 4. P3: the spine check moves to session-close, fixed and extended (step 4A)

**Start-project:** step 4A is removed. Step 5 no longer reports the spine.

**Session-close:** a new step runs `Spine-Check.ps1`, and its FATAL findings come first in the
close report. The check is extended:

| Check | Now | Proposed |
|---|---|---|
| span → strong | every span Strong's code exists as a live `strong` row | kept |
| verse ↔ span | **not checked**, despite the name | every live span belongs to a live verse; every live verse that has been onboarded has spans. The exact rule is to be read from the schema and `governance.verse_gap_by_design`, so that a verse gap by design is not flagged. |
| strong → meaning | **removed 2026-09-11** | **(answered Q1)** Every live `strong` has its meaning, checked directly in the three core meaning tables, which are the extracts from STEP: `strong_sense` (`head`, from mediumDef), `strong_meaning_tree` (the lemma's range, by `lemma_key`/`strong_variant`) and `strong_lexicon` (`lsj`/`mounce`). **What counts as complete depends on what STEP has for that Strong's, not on the table.** The method: (1) find the local gaps in each table: no row, a deleted row, or empty text; (2) for those codes only, ask STEP, through the app's own STEP client, what it holds; (3) STEP holds content that the table lacks → a finding, by code and table; STEP holds nothing → a gap by design, listed as such (as the "no known meaning" shells already are). The parse tables stay retired and are not read. |
| result | FATAL → one escalation and a pause | the same for verse/span/strong desync and for a meaning gap where STEP has the content. Each code is listed. |

## 5. P4: the analysis integrity check (new, in session-close)

The aim: confirm that each observation in the session was recorded in the claims tables, and
that each open, referred or to-be-clarified item is recorded in the open items register. This
answers #2172's point that the controls checked records against records, not readings against
the narrative.

**Scope:** files created or changed in the session's git window (as session-close already
computes it) under `_analytics/Clusters/**`, `_analytics/cross-cluster-web/**` and the narrative
folder.

1. **[code] Narrative changes are recorded.** For every chapter file changed, a `narrative_update`
   must be recorded in the window, and `Narrative-Register.ps1 -Action Check` must give 0 findings.
   Each chapter changed without a recorded update is a finding.
2. **[code] Every observation in a reading is placed.** For every reading, account or ledger file
   changed (`.md`, `.csv`), the trace logic of `reading-to-narrative-trace-v1` (the #2172 tool,
   moved into the app) lists each verse the file names. For each verse it looks for:
   - a current narrative citation;
   - a claim source;
   - an explicit route in the file: *data*, *forward OT-nn.n*, *parked*, *held #nnnn*.

   A verse with none of these is a finding, listed by verse and file.
   - **Convention (Q2, approved 2026-10-20: *"yes. not sure how else you would control it."*):**
     every reading file carries one placement per verse it names: told / claim / data /
     forward OT-nn.n / held #nnnn / context. The check reads that placement and compares it with
     the register: a "told" verse that the narrative does not tell is a finding, and so is a verse
     with no placement. This becomes a `cfg_behaviour_rule` (reading-file placement per verse),
     enforced by this check.
3. **[code] Every open item has a handle.** Each reading file changed carries an *Open items*
   section. Every line in it must name an `OT-nn.n` or `#nnnn` that exists and is open. A line
   with no handle, or a handle that does not resolve, is a finding.
4. **[Claude]** Claude re-reads the session transcript for what the researcher held, referred or
   asked to be clarified ("hold", "later", "check", "clarify", "come back to") and confirms each
   one is in the register by id. Any it is not in becomes a raised item the same turn (rule 21).
5. **Study on hold:** while no reading is done, the check reports "no analysis files changed this
   session". That is a real, stated scope, not a skipped check.

## 6. P5: thread quality, validity and integrity (step 4B)

**Now:** `ThreadCheck` (state moves), counts, and `Match` for the current strand.

**Change: [code] new `Escalation.ps1 -Action ThreadAudit`**, read-only, persisted to
`outputs/escalation/escalation-thread-audit-vN-*.md`. Each finding is listed by `OT-nn.n` with
its reason:

| # | Check | Finding when |
|---|---|---|
| T-a | handle resolves | `cluster:` not in `cluster`; `strong:` not a live `strong`; `verse:` does not resolve (the register's own verse parser); `chapter:` not an active `narrative_chapter`; `escalation:` not an escalation |
| T-b | handle carries its note | an item with no note saying what to pick up (the OT-05 ruling: a handle says what to pick up) |
| T-c | referred work still open | an `escalation:` item whose escalation is closed while the item is open; it should be closed or carried on |
| T-d | should have been cleared | an open item whose cluster, Strong's or verse belongs to a strand already worked (for example M02, M18, M64, M72, M09, M08, M25, M47), listed with that strand, because threads are "cleared as their clusters are worked". The worked-strand list is to come from the strand escalations' completed state, not from memory. |
| T-e | already told | an open `verse:` item whose verse the narrative now tells: either the item was done and not closed, or the telling does not cover what the item asks. Listed for reading. |
| T-f | thread shape | an open thread with no open item; a thread with no "comes back when"; a superseded or withdrawn item whose successor does not exist |
| T-g | register file current | `open-threads-register.md` differs from what `Export` would write now |

**[Claude] in step 5:** the threads are reported by their findings (T-a to T-g, by item), then
the threads bearing on the work in hand (as now), then the items waiting on the researcher. With
the study on hold, "the strand in progress" is stated as none, and `Match` runs against the last
strand worked (#2171, M07/M53).

## 7. Questions, answered 2026-10-20

- **Q1 (meaning tables).** Researcher, verbatim: *"you need to check that each strong have its
  meaning, the three tables are the extracts from STEP, so it is not about which table, it depend
  on what the STRONG has in step. parsed table stay retired. the check is done directly to the
  three core meaning tables."* Built into P3: each Strong's meaning is checked against what STEP
  holds for it, in `strong_sense`, `strong_meaning_tree` and `strong_lexicon`. The parse tables
  stay retired.
- **Q2 (placement per verse in reading files).** Researcher, verbatim: *"yes. not sure how else
  you would control it."* Built into P4 item 2 as a new behaviour rule.
- **Q3 (session logs).** Researcher, verbatim: *"session logs production is behaviour rule which
  you obviously ignored for the whole of Oct, or you just not looking the the right place because
  you are ignoring the configs."* **Both were true.**
  - The config is right: `governance.session_log_dir` = `Logs/`, and the logs are there. My S3
    finding said `Logs/` holds none. That came from listing only the last three entries of the
    folder instead of reading the setting, and it is withdrawn.
  - The newest log is `Logs/SESSION-LOG-20260929-m02-unit2-divine-anger.md`. **No session log was
    written from 2026-09-30 to 2026-10-19**, although `governance.session_log_required_content` and
    `governance.session_log_triggers_commit` are printed by `Start-Iba` at every start. The rule
    was not followed for the whole of October.
  - **Fix:** session-close writes the session log to `governance.session_log_dir`, with the six
    required contents, before step 7 commits. The close fails (detection) if no log for the
    session exists in that folder. P2(b) would have named this rule as "not followed" at every
    start.
  - The October sessions' records are their commit messages, the session-close reports and the
    escalation updates. Whether to rebuild logs for them from those is your call. I do not
    propose it unasked (no backfill).

## 8. Fixing the start-project findings (S1–S6)

| Finding | Fix |
|---|---|
| S1 spine step describes removed checks | step 4A leaves start-project (P3). The session-close step describes the extended check exactly. |
| S2 wrong report path | the command text reads the path from `escalation.list_report_path`. |
| S3 session logs stopped (no log 2026-09-30 to 2026-10-19). ~~`Logs/` holds none~~ (wrong: withdrawn, see Q3) | session-close writes the log to `Logs/` with the six required contents, and the close detection fails without it (Q3). `governance.session_log_dir` stays as it is. |
| S4 full governance dump each start | kept, since you want rules read. P2 adds the behaviour rules beside it. |
| S5 two STEP checks | kept: the port check only launches STEP, and init proves it answers. The command text is to say so. |
| S6 no check on how the last session ended | **[code]** start-up compares the last session-close report's time with the commits after it. Commits after the last close, or a missing close, are reported first. |

## 8a. Contradictions in rules, config and docs found during this audit (added 2026-10-20)

Researcher (verbatim): *"did you include fixing the incoherent behaviour / governance / configs
that you uncovered above."* They were not included; the S-list covered only the command text.
Each item below was checked live. Each is fixed in the build, through a config migration (Developer
Mode, `configmaint.apply_logged`), a doc edit, or code, as named.

| # | What contradicts what | Fix |
|---|---|---|
| G1 | **"Open" means two things.** `lib/escalation.py` hardcodes `_OPEN_STATES` = raised, re-assigned, **on-hold**, in-progress, and the list report heads with "12 open escalation(s)". The researcher's meaning is raised, in-progress, re-assigned. This is what led to "35". The definition also lives in code, not config (`governance.rules_must_be_config_driven`). | Put the state groups in config (`cfg_enum` grouping: open / parked / terminal), with on-hold as **parked**. The code reads the groups from config. The list report heads with "N open, M parked". The module-blocking gate and duplicate suppression keep their current behaviour by using open + parked explicitly. |
| G2 | **Session logs: the commit rule permits what the content rule forbids.** `governance.session_log_triggers_commit` makes the session-close commit valid "OR" a completed log, so October's closes committed without logs. `governance.session_log_required_content` requires a log for every session. | Reword `session_log_triggers_commit`: a session-close includes writing the session log, and the commit follows the log. The session-close detection fails without the log (Q3). |
| G3 | **CLAUDE.md §2 calls `Logs/` "Pre-restructure session logs (historical)".** `governance.session_log_dir` makes it the live folder. | Correct the CLAUDE.md §2 line to "session logs (live; `governance.session_log_dir`)". |
| G4 | **`governance.session_log_required_content` hardcodes "Logs/SESSION-LOG-*.md".** That duplicates `session_log_dir` and would drift if it moved. | Reword it to refer to `governance.session_log_dir`. |
| G5 | **The governance rules have no enforcement record.** The 52 `governance.*` settings carry no `enforcement_status` and no `evidence_check`. That is why a printed rule could go unfollowed for a month with nothing showing it. | P2 B and D cover them like the behaviour rules. The evidence check per setting is added to config alongside the behaviour rules' (P2 D). |
| G6 | **Method rule 66 contradicts the Q1 ruling.** `spine-extended-meaning-accepted-anomaly` accepts a missing meaning row on the strong's classification (T2, T3–T15, backfill). Q1 rules that completeness depends on what STEP holds for the Strong's. | Supersede rule 66 by a new rule stating Q1: complete = matches what STEP holds; "STEP has nothing" is the only gap by design. The P3 meaning check enforces it. |
| G7 | **Method rule 67 routes meaning through the retired parse tables.** `spine-on-demand-pull-mechanism` says "verse -> strong -> parse is the whole route" and "pull the extended meaning and parse through". The parse tables are retired. | Restate rule 67 without the parse: the route is verse → strong → the three core meaning tables, and a missing meaning is pulled into those tables at the point of discovery. |
| G8 | **The spine check claims more than it does.** `cfg_step` `spine.check.does` and method rule 68 say "verse/span/strong sync". The code checks only span → strong. | P3 extends the code to verse ↔ span. `does` and rule 68 are restated to match what the check then actually does. |
| G9 | **Escalation rule 3 names an inactive state.** `module_blocking` lists "raised, re-assign"; `re-assign` is inactive in `cfg_enum`, and the code uses `re-assigned`. | Reword rule 3 to `re-assigned`. |
| G10 | **Escalation rules 6 and 7 are stated but not enforced.** Rule 6 (`document_reference_grouping`) names a function removed in 2026-08. Rule 7 (full-path file references) is unchecked. That is the same gap that makes P1 search every field for links. | Rule 7: the P1 Context action reports any bare filename it cannot resolve as a finding. Rule 6: P2(b) names it as not followed. Whether to keep it, rebuild it or retire it is the researcher's call, raised as its own item. |
| G11 | **The command texts contradict the code.** start-project 4A describes removed checks (S1), and step 4 gives the wrong path (S2). | Fixed with P0 and the S-list. The command text is rewritten from the code, not edited line by line. |
| G12 | **The behaviour-rule count was meant to show the unenforced rules.** The 41 context-delivered rules are exactly those that rest on reading alone. | P2 D gives each one an evidence check over time. Until it has one, its close evidence is given by Claude and listed. |

Session-close contradictions (C1–C7 in the description) are taken up with the session-close
design.

**Going forward:** P2's code aid (rules naming retired things) and the compliance file's
"conflicts" list are the standing means of finding the next contradiction. A contradiction found
mid-session is raised the same turn (rule 21), not left in a file.

## 9. How it would be built

- **Config first.** New steps (`escalation.context`, `escalation.thread_audit`,
  `analysis.integrity`), report-path settings, the extended spine rule in `cfg_method_rule`, and
  the changed command texts. The behaviour rules affected are rule 21 (applied in P4.4) and any
  rule found in P2(b).
- **Developer Mode is needed** for the code (handlers, `init.py`, `Escalation.ps1`, the worksheets
  per `governance.ps_worksheet_sync_on_change`). The Developer Mode gate requires a fresh session,
  so the build runs in a new Developer Mode session, not this one.
- **Test plan per part:** one synthetic bad case per check (a missing linked file, a rule naming a
  retired table, an unresolvable thread handle, a span with no verse, a strong with no meaning
  row, a changed reading verse with no placement), run against live data, with the output read
  back.
- **BUILD.md entry and GOVERNANCE.md** in the same unit of work.
- **Order:** P2 → P1 → P5 → S6/S2/S5 text → P3 → P4. The start-project parts come first, because
  you asked to start there. P3 and P4 land in session-close and are designed further when we take
  up session-close.
