# #2173 session routines: test plan and run (v1, 2026-10-20)

> Escalation #2173 (and #2174). `cfg_behaviour_rule` 46 test-plan-per-module-utility. Runner:
> `iba/app/tools/temp_2173_test_plan_run.py` (temporary), against a migrated **copy** of iba.db
> and a scratch file tree; live iba.db and live project files are never written by it. Git is
> read from the real repository. STEP is read for the spine's gap codes only.
>
> **Run 2026-10-20: 49 of 49 pass** (results `results-2173.json` in the session scratch folder;
> the table below is that run). The live checks after the migration are in §3.

## 1. Cases (one synthetic bad case per check, read back)

| id | module | case | expected | result |
|---|---|---|---|---|
| G1.1 | lib/escalation.py | state groups read from cfg_enum | open = raised, in-progress, re-assigned; parked = on-hold | Pass |
| G1.2 | escalation.list | list header | "N open, M parked" | Pass |
| G1.3 | lib/escalation.py | a group switched off in config | RuntimeError, never a silent default | Pass |
| P1.1 | escalation.context | an escalation naming a file that does not exist | finding `missing` | Pass |
| P1.2 | escalation.context | a bare filename (`run.py`) | finding `bare` (rule 7) | Pass |
| P1.3 | escalation.context | a path naming v1 when v2 exists | resolved to v2, status `newer` | Pass |
| P1.4 | escalation.context | an on-hold (parked) escalation | not read | Pass |
| P5 T-a | escalation.thread_audit | item `cluster:M99` | handle does not resolve | Pass |
| P5 T-b | escalation.thread_audit | item with no note | finding | Pass |
| P5 T-c | escalation.thread_audit | item `escalation:#1962` (completed) | referred work closed | Pass |
| P5 T-d | escalation.thread_audit | item `cluster:M02` (#1963 completed) | should have been cleared | Pass |
| P5 T-e | escalation.thread_audit | item on a verse a chapter tells | already told | Pass |
| P5 T-g | escalation.thread_audit | register file older than the table | finding | Pass |
| P3.0 | spine.compute | the live copy | 0 FATAL, 6 gaps by design | Pass |
| P3.1 | spine.compute | a span whose verse does not exist | `SC2:span:` | Pass |
| P3.2 | spine.compute | a span code with no strong | `SC2:desync:` | Pass |
| P3.3 | spine.compute | a meaning-tree row removed where STEP holds the text | `SC2:meaning:` (FATAL) | Pass |
| P3.4 | spine.compute | a strong's cluster_strong row removed | `SC2:cluster:` | Pass |
| P3.5 | spine.compute | gaps where STEP holds nothing | listed by design, not FATAL | Pass |
| P3.6 | spine.compute | STEP not asked | gaps reported unverified, FATAL | Pass |
| P2.1 | compliance.check_start | the blank template | one finding per rule (blank) | Pass |
| P2.2 | compliance.check_start | a filled file (acknowledgement, every row, retired-name rules in conflicts) | passes | Pass |
| P2.3 | compliance.check_start | a row that copies the rule text | finding "copies" | Pass |
| P2.4 | compliance.check_start | acknowledgement altered | finding `ack` | Pass |
| P2.5 | compliance.check_close | engaged row, no evidence | finding | Pass |
| P2.6 | compliance.check_close | evidence naming a missing file and a #n vN older than the session | two findings | Pass |
| P2.8 | compliance.check_evidence | evidence naming `Logs/compliance/COMPLIANCE-20261020-d7696d1d.md` | the hex in the file name is not taken for a commit | Pass |
| P2.7 | compliance.copied | a short genuine restatement ("no wipe of the escalation table") | not judged a copy (under compliance.copy_min_words) | Pass |
| G14.1 | lib/quotecheck.py | a true quote, a misquote and a gloss | only the misquote fails | Pass |
| SC.1 | session.close | open findings | condition findings-open (Session-Close.ps1 exits 3) | Pass |
| SC1 | session.close | no boundary record | `SC1:boundary`, the close fails | Pass |
| SC3 | session.close | an unrecorded researcher message; `/start-project`; "proceed" | the first and the third are findings (a message under session_close.message_min_words words always needs its disposition), the command is not | Pass |
| SC4a | session.close | an Open items line with no handle; one naming OT-999.1 | both findings | Pass |
| SC4a.3 | session.close | an Open items bullet wrapped onto a second line that holds its handle | read whole, no finding | Pass |
| SC4a.4 | session.close | a changed close report with a heading 'Open items in the register' | not read (session_close.open_items_exclude) | Pass |
| SC4b | session.close | a message with "hold" | needs its register item | Pass |
| SC5a | session.close | a chapter file changed, no weave recorded | finding | Pass |
| SC5b | session.close | a misquote added to a chapter | finding | Pass |
| SC5c | session.close | a register finding absent from the previous close's list | finding `new` | Pass |
| SC5d | session.close | a verse named in a reading with no placement row | finding | Pass |
| SC6 | session.close | the compliance file is found and checked | no `SC6:file` | Pass |
| SC8 | session.close | no log; then a log with its six sections | finding; then none | Pass |
| SC9 | session.close | a decision line with no target; one naming a changed file | only the first is a finding | Pass |
| SC10 | session.close | a code file changed and not named in BUILD.md's added lines; one that is named | the first is a finding, the second not | Pass |
| SC12 | session.close | a chapter changed | narrative copy needed | Pass |
| SC.2 | session.close | a disposition `carried #2173` and one `carried OT-999.1` | the first clears, the second stays open | Pass |
| S6 | sessionwindow.last_close_findings | real git | runs; names uncommitted paths and the commits since the last close | Pass |

## 2. Config validation on the copy (before applying live)

`configmaint` `_validate_live` and the advisory checks, live vs migrated copy: 0 coherence
errors; no new orphan config; the 5 new lib modules registered (unregistered 5 -> 0); no new
location or density finding (exemptions recorded with reasons); migration idempotent (second run:
94 unchanged). The first pass found 17 coherence errors (setting modules not in
`config_module`) and 3 orphan enum groups; both fixed before the live run.

## 3. Live, after the migration (read-only steps)

| step | result |
|---|---|
| `Escalation.ps1 -Action List` | "6 open, 8 parked escalation(s)" |
| `Escalation.ps1 -Action Context` | 6 open escalations, 26 file references, 11 findings (2 missing, 9 bare) |
| `Escalation.ps1 -Action ThreadAudit` | 187 findings (T-b 141, T-c 4, T-d 11, T-e 30, T-g 1); T-g is real: the register embeds rule 74, which the migration restated |
| `Spine-Check.ps1` | 0 FATAL, 6 meaning gaps by design |
| stop hook | reads the state groups from cfg_enum; still lists #2173 |

P2.7 was added after the acceptance start run found the false positive on rule E:11 (fixed in lib/compliance.py with the setting compliance.copy_min_words). SC10's case was changed when the real BUILD.md entry began naming compliance.py, which the old case assumed it did not.

The acceptance close run then found two more faults, fixed with tests: the hex in a file name was read as a commit hash (P2.8), and a short message such as "proceed" matched any comment by substring, which proves nothing (SC3; setting session_close.message_min_words); and a bullet wrapped onto a second line was read as one physical line (SC4a.3, SC9); and the close report's own heading 'Open items in the register' was read as an authored Open items section (SC4a.4; setting session_close.open_items_exclude).

**Acceptance, start:** `Compliance.ps1 -Action Check -Phase Start` on this session's file passed (after the E:11 fix). The close run is recorded on #2173 and in the session log.
