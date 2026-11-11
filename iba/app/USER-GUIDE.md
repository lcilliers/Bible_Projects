# IBA app — user guide

How to run each tool, as it is now. What the app is for: [`CHARTER.md`](CHARTER.md). How config
governs the code: [`GOVERNANCE.md`](GOVERNANCE.md). Rules are not restated here; where a tool
enforces one, the rule is named by key (`cfg_behaviour_rule`, `cfg_setting`). The earlier guide is
history at `archive/docs/user-guide-md-history-to-20261021.md`.

**Conventions for every command below:**
- Run from the repo root, `C:\Bible_study_projects`.
- `-Book` is the OSIS code stored in `verse.osisId` (`Dan`, `1Chr`). `-BookLabel` is the
  human-facing folder name (`Daniel`), and defaults to `-Book`.
- Every script that does project work dispatches through `python -m iba.app.run` and records a
  `run` row. `-Trace` (or `IBA_TRACE=1`) prints every config read.
- A script's own help gives its full parameter detail: `Get-Help .\iba\app\ps\<Script>.ps1 -Full`.
- Report paths come from `cfg_setting` (`*.report_path`) or `cfg_report`. A report that
  regenerates archives its previous version to `archive/` beside it and, where it is set up, writes
  a CSV of its tables to `export/`.

---

## 1. Environment

| Requirement | Detail |
|---|---|
| Python 3.14 | with `requests` (`python -m pip install requests`) |
| STEP Bible | the local server at `http://localhost:8989`, module `ESV_th`; the app never uses the web |
| `ANTHROPIC_API_KEY` | only for the steps that call the Claude API: the cluster-reading stages (§7); from the environment or the repo-root `.env` |

The database is `iba/app/db/iba.db` (git-ignored). `bible_research.db` is the prose store only
(`governance.scope_research_db`).

**STEP looks closed but the app says it's up:** closing the STEP window doesn't always stop its
server. Find and stop a stale `step.exe`:

```powershell
Get-NetTCPConnection -LocalPort 8989 -State Listen | Select-Object OwningProcess
Get-Process -Id <pid>        # confirm it is step.exe
Stop-Process -Id <pid>
```

---

## 2. Session routines

### 2.1 Start: `/start-project`

The command (`.claude/commands/start-project.md`) runs these, in order:

```powershell
iba\app\ps\Start-Iba.ps1                              # bootstrap; prints NEEDS ACTION, then the general rules
iba\app\ps\Compliance.ps1 -Action Template            # this session's compliance file
iba\app\ps\Compliance.ps1 -Action Check -Phase Start  # exit 3 until it passes
iba\app\ps\Escalation.ps1 -Action List                # open escalations, latest version only
iba\app\ps\Escalation.ps1 -Action ThreadCheck -AnsweredBy Claude
iba\app\ps\Escalation.ps1 -Action ThreadAudit
```

**`iba/app/ps/Start-Iba.ps1`** (`init.py`) is idempotent. It:
- validates the config and loads it into the database if needed
- builds missing data tables
- probes STEP with a known answer (H0430 must gloss "God"; the probe values are in config)
- checks how the last session ended: uncommitted paths, an uncommitted session log, a newest
  commit that is not a close's final commit, or a log naming no commit

A check that passes prints nothing. It then prints, in full from the database, the general rules
that apply this session (those with a `general` link in `cfg_rule_scope`; the rest come at their
point of use), and ends `READY` or `NOT READY`. Runs refuse to start without STEP
(`step.required_for_runs`).

- `-Reset` rebuilds the data tables. It drops all data and keeps the config.
- The config lives only in iba.db. If it is missing, the bootstrap refuses to start; restore a
  snapshot (`iba/app/db/snapshots/`) or the NAS backup.

**The compliance file** (`Logs/compliance/COMPLIANCE-<date>-<session8>.md`) has one row per general
rule delivered in the session's mode, keyed `G:<governance setting>`, `B:<behaviour rule id>`,
`E:<escalation rule id>`. A behaviour rule is delivered by `cfg_behaviour_rule.deliver_when`:
- `always`
- `study_active`, while `cfg_setting behaviour.study_state` is `active`
- `developer_mode`, only with `-Mode Developer`

Governance settings that hold a plain value (a path, a format) are not delivered and get no row:
they are listed in `cfg_setting compliance.value_settings`.

The mode is written into the file, and Check reads it from there. Each row is filled with status
`engaged` or `not engaged` and, in your own words, what the rule requires this session or why it is
not engaged. A copied rule text is a finding. Also filled: the acknowledgement sentence
(`compliance.acknowledgement`), and in `## Conflicts and rules not followed`, every rule in
conflict, not followed, or naming a retired thing. During the session each engaged row gains its
evidence (a file path, `#nnnn vN`, a commit hash, a command output).

A Developer Mode session (`/developer-mode`) writes its own file:

```powershell
iba\app\ps\Compliance.ps1 -Action Template -Mode Developer
```

**Rules at the point of use.** The first time in a session that Claude runs a PS tool action, git
commit or push, a migration or a database query, or writes a file in a governed area, the hook
`.claude/hooks/rules_at_point_of_use.py` refuses the call once. It shows the rules for that operation
(`cfg_rule_scope`) and the tool's usage from this guide, and Claude re-issues the call. To change
which rules govern an operation, change its `cfg_rule_scope` rows.

### 2.2 Close: `/session-close`

```powershell
iba\app\ps\Session-Close.ps1     # report at session_close.report_path; exit 3 while any finding is open
```

It checks the session's work against its record. Each finding has a stable key:

| Step | Finding |
|---|---|
| SC1 | the session or its boundary record cannot be found (the git window is unknown) |
| SC2 | a spine FATAL finding (§2.3) |
| SC3 | a researcher message that appears in no escalation comment written this session |
| SC4 | an `Open items` line (in a file changed this session; a session log only when it names this session's id) with no open `OT-nn.n`/`#nnnn`; a researcher message with a holding word (`session_close.held_words`) |
| SC5 | a chapter file changed with no recorded weave; a quotation not in the ESV text; a new register-check finding; a verse in a changed reading file with no placement (rule 79) |
| SC6 | an engaged compliance row with no evidence, or evidence that does not check |
| SC8 | no session log for this session in `governance.session_log_dir`, or a missing section |
| SC9 | a decision line in the log naming no target that changed this session |
| SC10 | a code or config file changed (`session_close.build_scope`) not named in what BUILD.md gained |
| SC12 | whether the narrative copy and the threads export are needed |
| SC15 | a control file (`session_close.control_kinds`) missing, naming a path that does not resolve or points into an archive without marking it as history, carrying replaced-history text, or (read every conversation) over `session_close.always_read_max_bytes` |
| SC16 | a PS tool action that failed twice in the session, or any other call that failed twice with the same error; a designed stop (`session_close.sc16_designed_stops`: COMMIT BLOCKED, NOT PASSED, a Propose waiting for approval, a hook's refusal `hook error: `) is not a failure |

**To clear a finding:** fix it, or write a disposition in the compliance file's
`## Close dispositions` section as `- <key> :: <disposition>`:
- `carried OT-nn.n` or `carried #nnnn`
- for SC3, `recorded in #n vN` or `no record needed: <reason>`
- for SC4(b), `in register …` or `not held: <reason>`
- for a quotation, `not scripture: <reason>`

The check verifies each one. Nothing is committed while the script exits 3 (rule 82). The close
writes the session log (`governance.session_log_required_content`) and commits twice
(`governance.session_log_triggers_commit`).

### 2.3 Spine check

```powershell
iba\app\ps\Spine-Check.ps1       # report at spine.quality_report_path
```

Read-only. Each of these is FATAL:
- a span code with no live `strong`
- a live span with no live verse, or a live verse with no live span
- a strong in a live span with no live `cluster_strong` row
- a meaning gap where STEP holds the content

A verse with no row at all is a gap by design (`governance.verse_gap_by_design`). Session-close runs
this as SC2.

---

## 3. Escalations

Every open item, task, issue, decision and thread is an escalation (rule 40), worked only through
`iba\app\ps\Escalation.ps1`.

### 3.1 What an item is

- **`escalation`** holds an item's current state. `comment` and `context` accumulate: pass only
  what is new.
- **`escalation_history`** holds one row per change, holding only what that change set.
- **Shape:**
  - dispatcher-tied: raised by a paused run, `run_id` `RUN-…`; answered with `-Action AnswerRun`
  - manual: raised by hand; worked with `-Action Update`
- **Type:** `task`, `run_error`, `issue`, `notice` (closes on arrival), `config`, `note`, `thread`.
  The type is fixed at Raise.
- **`resolution_kind`** (required at Raise):
  - `DecisionRequired`: closing needs a new decision
  - `SelfCorrectable`: an execution slip against something already decided
- **States:** open is `raised`, `in-progress`, `re-assigned` (`cfg_enum escalation_state_open`).
  Parked is `on-hold`. Terminal is `completed`, `closed`, `withdraw`, `supersede`. The state a
  change produces comes from `cfg_escalation_transition`; required fields come from
  `cfg_escalation_requirement`.
- **The title** (`-Question` at Raise) is immutable, at most 60 characters, and must read as a
  title.

### 3.2 Commands

```powershell
# see what's open (latest version of each item; parked items one line each); one item's full story
iba\app\ps\Escalation.ps1 -Action List
iba\app\ps\Escalation.ps1 -Action History -Id 741

# raise a manual item
iba\app\ps\Escalation.ps1 -Action Raise -Question "Short title, 60 chars max" -Comment "what it is about" `
    -ResolutionKind DecisionRequired -AnsweredBy Claude [-Type task] [-AssignedTo Claude] [-Context "files"] [-State in-progress]

# every later change to a manual item
iba\app\ps\Escalation.ps1 -Action Update -Id <id> -AnsweredBy Claude|Researcher `
    [-NextAction ready_for_approval|approved|reject|revise|noted|review] [-AssignedTo Claude|Researcher] `
    [-State on-hold|in-progress|closed|withdraw|supersede|completed] [-Resolution "…"] [-Tried "…"] `
    [-Comment "…"] [-Context "…"] [-NeedsFollowup 1|0]

# answer a dispatcher-tied pause
iba\app\ps\Escalation.ps1 -Action AnswerRun -RunId <run_id> -Decision Approve|Reject|Revise|Hold|Noted -AnsweredBy …

# self-correctable items
iba\app\ps\Escalation.ps1 -Action ResolveSelfCorrectable -Id <id> -Resolution "what was wrong, what changed" -AnsweredBy …
iba\app\ps\Escalation.ps1 -Action EscalateToDecision -Id <id> -Tried "what was attempted, what it showed" -AnsweredBy …

# fix something recorded wrong, in any state (also the only way to change a title)
iba\app\ps\Escalation.ps1 -Action Correction -Id <id> -AnsweredBy … [-ShortDescription "…"] [-State …] [-Resolution "…"] [-Comment "why"]
```

**Working an item:**
- **Starting work:** a comment, context or tried text cannot be added while the item is `raised`.
  Move it to `-State in-progress` first.
- **File links go in `-Context`**, not `-Resolution`. The resolution says what was decided or done.
- **Handing an item to the researcher** is one call: `-NextAction ready_for_approval -AssignedTo
  Researcher -Resolution "…"`. Setting `ready_for_approval` without `-AssignedTo` leaves the item
  with Claude. What a hand-over must state is rule 63.
- **An interim approval** (one whose result needs further work by Claude) carries `-NeedsFollowup
  1`, so `approved` sends the item back to Claude (`re-assigned`) instead of closing it. When the
  follow-up is done, close it with `-NeedsFollowup 0`; don't re-send `-NextAction approved`.
- **Approving:** the reviewer sets `-NextAction approved`. Only the party the item was assigned to
  for approval may approve it.
- **A decision_required item** is answered through Update, never AnswerRun (rule 45).
- **A change Claude proposes** through `configmaint.propose`, which the researcher has already
  decided in chat, goes straight to `ready_for_approval` with the decision quoted.
- **A dispatcher-tied pause** (a config proposal, a quality-check finding, a crash) records the
  answer against its exact paused run.
- **Superseding an item:**
  1. Raise the replacement, naming the old item in `-Comment` or `-Context`.
  2. Update the old item with `-NextAction reject -State supersede -Comment "superseded by #nnnn — why"`.
- **Parameters:** pass every one by name. A bare trailing argument is refused.

**What open escalations point to** (read at every start):

```powershell
iba\app\ps\Escalation.ps1 -Action Context -Id <id>   # when an item is taken up: every file it names, resolved to its latest live version
iba\app\ps\Escalation.ps1 -Action Context            # the same for every open escalation
```

Findings: `missing` (no live version) and `bare` (a bare filename).

### 3.3 Threads (the open threads register)

A thread (type `thread`, alias `OT-nn`, every `-Id` accepts it) holds items (`OT-nn.n`). Each item
is a cluster, Strong's, verse, strand, chapter, event, researcher question or escalation that a
strand is matched against. Claude manages each thread's lifecycle (rule 74). An item is open, or
settled as closed, withdrawn or superseded. A thread rests `on-hold`, is `in-progress` while
in-progress work references it, and completes when its last item is settled. The only
`-NextAction` used on a thread is `reject`, to end it early.

| To… | Command |
|---|---|
| see the open threads | `.\Escalation.ps1 -Action Thread` (`-State in-progress` narrows) |
| see one thread with its responses | `.\Escalation.ps1 -Action Thread -Id OT-16` |
| find threads bearing on a strand | `.\Escalation.ps1 -Action Match -Cluster M18 -Strong H2530 -Verse "Rom 7:15"` (add `-For <id> -AnsweredBy Claude` to record it) |
| bring threads into line | `.\Escalation.ps1 -Action ThreadCheck -AnsweredBy Claude` |
| audit the threads | `.\Escalation.ps1 -Action ThreadAudit` (T-a unresolved handle … T-g register file out of date) |
| answer an item | `.\Escalation.ps1 -Action Update -Id OT-16 -Item OT-16.2 -ResponseKind closed -Respond "…" -Via <id> -AnsweredBy …` |
| forward an item | `… -Item OT-16.2 -ResponseKind forward -Respond "…" -AddItem cluster:M58 …` |
| withdraw / supersede an item | `… -ResponseKind withdrawn -Respond "reason"` / `… -ResponseKind superseded -Respond "carried by OT-41.3"` |
| add an item | `.\Escalation.ps1 -Action Update -Id OT-16 -AddItem "verse:Rom 7:15-21 :: note" -AnsweredBy …` |
| withdraw a thread | `.\Escalation.ps1 -Action Update -Id OT-40 -NextAction reject -State withdraw -Comment "reason" -AnsweredBy Claude` |
| supersede a thread | `… -NextAction reject -State supersede -SupersededBy OT-41 -Comment "reason" …` |
| raise a thread | `.\Escalation.ps1 -Action Raise -Type thread -Question "title" -Comment "…" -ComesBackWhen "…" -Item cluster:M15 -ResolutionKind SelfCorrectable -AnsweredBy Claude` |
| regenerate the register file | `.\Escalation.ps1 -Action Export -Type thread` (never edit the file) |

**Registering an item to a clear purpose** (`iba/app/ps/Open-Item.ps1`, #2236, rule B:115): an
open item points from the analysis in hand to related work without interrupting it. It has a target
scoped to verses, says what to read for and why it is open, and is cleared at some point.

```powershell
iba\app\ps\Open-Item.ps1 -Action Add -Thread OT-103 -Origin 2172 -Anchor strong:H0639G -Source H0639G -TargetCluster M58 -TargetTerms H7489A -ReadFor "…" -Why "…" -ComesBackWhen "…"
iba\app\ps\Open-Item.ps1 -Action Add -Thread OT-102 -Origin 2172 -Anchor verse:"Num 11:15" -Verse "Num 11:10-15" -ReadFor "…" -Why "…" -ComesBackWhen "…"
iba\app\ps\Open-Item.ps1 -Action Reword -Item OT-103.1 <the same parameters>      # or -File <specs.json> for many
iba\app\ps\Open-Item.ps1 -Action Split -Item OT-97.1 -File <parts.json>          # one purpose per item
iba\app\ps\Open-Item.ps1 -Action Due -Cluster M58                               # items that come back when M58 is worked
iba\app\ps\Open-Item.ps1 -Action Review                                         # stragglers -> open_item.output_dir
```

- **The target:**
  - **A cluster item** reads the target cluster's related term(s) against the source analysis's strong. Its verses are the ones holding both.
  - **Or a verse target:** `-Verse`.
  - **The limit:** at most `open_item.max_verses` (200). A wider target is refused: split it.
- **Refused, nothing written:** no target, `-ReadFor`, `-Why` or `-ComesBackWhen` in words; an
  origin that is not a task or issue; an anchor that does not resolve; a target term not in the target
  cluster; source and target never in the same verse; the same target read for the same thing on the
  thread. A `-File` batch is one unit: one refusal writes none of it.
- **A worded item** (kind `scope`) matches a scope on its target verses only (Match,
  Verse-Collate, a reading's Open and Synergy). Its target cluster is its home: `-Action Due`.
- **Reword** keeps the earlier wording in the item's history. **Split** records the old item
  superseded by the new ones. Answering and closing stay with `iba/app/ps/Escalation.ps1` (or a reading's gate 2).

Item notes:
- **Naming an item:** `-Item` takes `OT-16.2`, the bare number, `cluster:M03`, or a value unique in
  the thread.
- **A note** follows ` :: `.
- **Matching:** M10 matches M10c (T codes too: T3); a Strong's number matches its exact code, else
  its zero-padded base; a verse matches inside a range or chapter. A reading uses the same
  matching (section 8.2).
- **Linked tasks:** when a task an item references changes state, the item follows it.

---

## 4. Configuration

```powershell
iba\app\ps\Config-Maintenance.ps1 -Step Validate     # read-only coherence check; only findings new since the last approved one escalate
iba\app\ps\Config-Maintenance.ps1 -Step Report       # the config report, at configmaint.report_path

iba\app\ps\Config-Maintenance.ps1 -Step Propose -Table cfg_setting -Op update `
    -Where '{"key":"passage.review_over"}' -Set '{"value":"12"}' -Title "short name, 60 chars max" -Question "why, and what it affects"
#   PAUSED: a decision_required escalation. After approval (§3.2), re-run the same command with -RunId <run_id>.
```

- **App Mode:** Propose is the only path for a `cfg_*` row. It writes one row, after a coherence
  check, and commits only on approval. Every write is logged in `cfg_change_detail`.
- **Developer Mode:** config work is one idempotent migration under `iba/app/migration/`, writing
  through `configmaint.apply_logged()` (rule 75). Single-row Propose is not used there. A migration
  registers itself inactive, runs once, and then moves to `iba/app/migration/archive/`.
- **Glossary currency:** `-Step Validate` reports a term of `glossary.currency_check` that has no approved entry
  in the programme glossary (`bible_research.db`, kept through `iba/app/ps/Prose.ps1`; drafts are flagged until approved).
- **The control map** (`cfg_control_home`, config report section 15) says where each kind of
  control lives.

**Behaviour rules:**

```powershell
iba\app\ps\Behaviour.ps1 -Action List [-Class chat|terminal|sqlite|documentation|llm_output|development|filing|study_method]
```

This lists the rules; it never writes them.

---

## 5. Base data

```powershell
iba\app\ps\New-Word.ps1 -Word <word> -Source "<why>"     # register a word and build its raw layer from STEP
iba\app\ps\Raw-Backfill.ps1 -Book Dan [-Range 1:1-7]     # meaning only, for strongs a book's spans reference
iba\app\ps\Lexicon-Parse.ps1 -Step Parse|Related|Validate
iba\app\ps\Lexical-Readiness.ps1                         # read-only three-part lexical readiness check
iba\app\ps\Cluster-Report.ps1                            # cluster taxonomy and assignment coverage (read-only)
iba\app\ps\Cluster-Assign.ps1 -Step Validate|Assign      # Assign: DB-wide mechanical exact-gloss assignment
iba\app\ps\VerseMeta.ps1 -Step SetStatus -References "Gen.1.1,Rom 1:3" -Status analysed
python -m iba.app.tools.purge_word --word "<word>" [--yes]   # remove a test word; dry-run without --yes
```

**New-Word:**
- The word is normalised (stray brackets, case) and de-duplicated at entry.
- An existing word holding the same Strong's is noted in the step's own line, not a pause.
- `registry.exists` reports the word's true state: new, approved but not built, rejected before,
  or already built (stops).

**The other base-data tools:**
- **Raw-Backfill** rebuilds the lexicon-parsed layer for what it pulls, so Lexicon-Parse is for a
  manual full rebuild or check.
- **Lexicon-Parse:** `Related` makes one STEP call per row.
- **Cluster-Assign:** `Assign` is idempotent. It matches exact glosses only. A wrongly clustered
  group is re-tagged only on the researcher's instruction (rule 70).
- **purge_word** matches the word literally and removes only that word's own rows, not the shared
  raw layer.

---

## 6. Verse lexical and the debate pipeline (book-scoped)

**1. Build the lexical once per book**, ahead of any debate:

```powershell
iba\app\ps\VerseLexical.ps1 -Book Dan -Chapters 1-12 -BookLabel Daniel
```

`VerseLexical.ps1 -Step` also takes:
- `lexical.enrich -PayloadPath <json>`: Layer 2 notes for one registered passage-block
- `report.lexical_exceptions`
- `report.lexical_extract` (with `-PassageFilter`/`-VerseFilter`/`-SurfaceFilter`/`-StrongFilter`)
- `lexical.notes`
- `report.verse_lexical`

`-SkipBuild` and `-ForceRebuild` control the build.

**2. Register a passage:**

```powershell
iba\app\ps\Build-Passages.ps1 -Book Gal -Range 5:16-17 -PayloadPath <json>
```

**3. Run the debate**, one chapter or range at a time:

```powershell
iba\app\ps\Debate-Run.ps1 -Book Dan -Chapters 1-3 -BookLabel Daniel
iba\app\ps\Debate-Run.ps1 -Book Dan -Range 8:1-27 -BookLabel Daniel [-Step hib.set]
```

It walks `passage.debate_run_sequence` (`hib.set` → `passage.build` → `phenomenon.set` →
`operation.set` → `closing.set`). For each step it:
- skips the step if it is already satisfied
- runs it with the staging payload at `passage.debate_staging_path_pattern`, if there is one
- otherwise stops and prints the path it expects

Write the payload, then re-run the same command. After `closing.set`, the report is written under
`iba/app/verse-analysis/<BookLabel>/`.
- A correction that removes an item others depend on is refused (`*-has-dependent-*`). Remove the
  dependant first.
- A step can be run on its own with
  `Operations-Ingest.ps1 -Step <step> -Book … -Chapters|-Range … -PayloadPath …`.

**4. Book-level output:**

```powershell
iba\app\ps\WholeBookRead-Report.ps1 -Book Amos -BookLabel Amos
```

`iba/app/ps/WholeBookRead-Report.ps1` reads the filled scaffold-model debates (Amos, Hosea, Joel, Jonah,
Micah, Obadiah). It does not yet read books produced by `iba/app/ps/Debate-Run.ps1`.

---

## 7. Cluster-reading pipeline (cluster-scoped)

Each stage previews by default: a cost estimate, with no API call and nothing written. Add `-Live`
to run it. Each stage refuses a cluster or subgroup not at its required status.

```powershell
iba\app\ps\VerseReading.ps1 -ClusterCode M67 [-Live]                    # Stage 1, word level (lexical.meaning)
iba\app\ps\RelationalReading.ps1 -ClusterCode M67 [-VerseList "2Cor.8.8,Rom.12.8"] [-Live]   # Stage 1, relational half
iba\app\ps\Run-Stage1Batch.ps1 -ClusterCodes "M35,M51,M61" [-Live -MaxTotalCostUsd 15.00]  # several clusters, unattended
iba\app\ps\Observation-Enhancer.ps1 -Action Preview|Apply -RuleKey <key>   # apply a confirmed rule to ib_observation
```

**How the stages run:**
- **Stage 1** refuses to run when Layer 1's `role` arrays are stale for the cluster.
- **Stages 2 to 4 are retired** (#2299): `cluster.subgroup`, `cluster.reading` and `cluster.answer` are
  inactive. Subgroups are made by the surface mapping (§7.1), and reading is the reading process (§8).
- **Corrections to `ib_observation`** happen only by re-running a stage (rule 68). The enhancer is
  for researcher-confirmed rules only.

### 7.1 Surface subgroups (`iba/app/ps/Surface-Map.ps1`)

A cluster's subgroups are groups of (Strong's code, surface) pairs, made per M cluster at the
clustering stage (behaviour rules B:117, B:118; escalation #2293). Run the steps in this order for
each cluster:

```powershell
iba\app\ps\Surface-Map.ps1 -Step Pairs -Cluster M18                 # the pairs file (reads only)
iba\app\ps\Surface-Map.ps1 -Step Apply -Cluster M18 -File <file>    # the filled file written
iba\app\ps\Surface-Map.ps1 -Step Tail -Cluster M18 [-Live]          # the rest, by the API
iba\app\ps\Surface-Map.ps1 -Step Check -Cluster M18                 # the report (reads only)
```

- **Pairs** writes `_analytics/surfaces/exports/surface-map/<cluster>-pairs-<date>.json` (setting
  `cluster.surface_map.output_dir`). It lists every pair with its hits, verses, gloss and two
  sample references, and marks it head or tail. The head is the pairs covering
  `cluster.surface_map.head_share` (0.8) of the cluster's hits. For M49, M67 and M83 each pair
  comes pre-filled with the subgroup its code already had.
- **In the file,** Claude adds the groups (code `<cluster>_<slug>`, label, description, and a kind
  of `group`, `qualifier` or `not_this_sense`). Every head pair then gets a group and a reason; tail
  pairs may be left blank. Set `two_sense` to 1 where a pair carries two senses. To move an
  inherited pair, start its reason with `correction:`.
- **Apply** refuses the whole file if anything is wrong, and lists every problem. It makes the
  cluster's anomaly group, `<cluster>_anomaly`, and puts pairs with an empty surface in it.
- **Tail** sends the pairs still unplaced to the API: code, gloss, surface and one sample verse. It
  uses the `lexical.llm_*` settings, with `cluster.surface_map.tail_max_output_tokens` as the
  output ceiling. Without `-Live` it is a preview showing the cost. It refuses while any head pair
  is unplaced, and refuses a call over `lexical.llm_max_cost_per_batch`.
- **Check** writes `<cluster>-check-<date>.md`. It flags a group of kind `group` holding more than
  `cluster.surface_map.max_group_share` (0.3) of the cluster's hits: look at that group, but it is
  not a forced split. It also lists the cluster's **stale** pairs: pairs whose code has left the
  cluster, or whose surface no longer occurs. The next Apply soft-deletes them, keeping the reason.
- **A cluster is not read until it is mapped** (#2294). `Reading.ps1 -Step Open` refuses a reading
  whose home is an M cluster with any unallocated or stale pair, and its message names the counts
  and the step to run. `Cluster-Assign.ps1 -Step Validate` counts every M cluster's mapping:
  stale pairs and partly mapped clusters are findings, while an unmapped cluster is only counted.

### 7.2 Capture of prior study documents (`iba/app/ps/Prior-Capture.ps1`)

A migration, not part of the standard analytic process (escalation #2305; design
`outputs/escalation/2305-prior-work-capture-design-v2-20261026.md`; method rules CP-01 to CP-10 on
`prior_capture.record`). Every material observation a study document makes about a verse it names is
captured into `ib_observation` and `ib_node` as written: the verse is not read again, and nothing is
checked, corrected or rejected. It runs in a chat session on the Sonnet model; there is no API route.
Per document:

```powershell
iba\app\ps\Prior-Capture.ps1 -Step Prepare -File "<repo-relative path or reading_file id>"   # the JSON (reads only)
iba\app\ps\Prior-Capture.ps1 -Step Record -File <the filled JSON>                           # written whole, or refused whole
iba\app\ps\Prior-Capture.ps1 -Step Report                                                   # where the capture stands (reads only)
```

- **Prepare** writes `_analytics/reading-tools/prior-capture/capture-<file id>-<date>.json` (setting
  `prior_capture.output_dir`): every line of the document that names a verse (with its text, section
  and verses resolved), the M- and T-coded words of each verse with their clusters and subgroups, the
  October ids already recorded for the document, and the references that resolve to no single verse.
  It refuses a document changed since the reading index was built (run `Reading-Index.ps1 -Step
  Build`) and a document already captured.
- **In the file,** Claude reads the document and fills `findings` (one per observation: kind, text,
  basis, route on a party or link finding, and the nodes it applies to, each a verse and a word with
  its role and the document's disposition) and the `answer` of **every** line: `captured` (the
  finding keys), `already_recorded` (October observation ids) or `not_an_observation` with its class
  and reason. A material observation that fits none of the eight kinds takes the tag `unfitted`.
- **Record** refuses the whole file if any line is unanswered or anything is wrong, and lists every
  problem. It writes the observations (stage `prior-capture`, status `draft`, `revisit_note` naming the
  document and its lines), their nodes (the occurrence, cluster and subgroup from the tables, never
  from the document), the line answers (`prior_capture_line`) and the document's `capture_status`, in
  one transaction, and writes `capture-<file id>-report.md`: the unfitted observations, the flags the
  document carries, the nodes with no occurrence, the references to no single verse and quotations not
  found in the ESV text. No check for duplicates is made across documents; an identical live
  description joins the first observation as further nodes.
- **Report** writes the status report, versioned (`capture-status`, in `_analytics/reading-tools/prior-capture/`): documents by `capture_status`, observations by tag, line
  answers, and the nodes with no `verse_lexical_id`.

### 7.3 The node reference sweep (`iba/app/ps/Node-Resolve.ps1`)

A migration step (escalation #2308), run after the capture: it looks up, through the strong and the verse, the
occurrence (`verse_lexical_id`), the morph code and the sub_group code of the nodes that lack them, in every stage and
cluster. Method rules NR-01 to NR-06 on `node_resolve.apply`.

```powershell
iba\app\ps\Node-Resolve.ps1 -Step Plan                                   # what would be filled, and what cannot (reads only)
iba\app\ps\Node-Resolve.ps1 -Step Apply -File outputs\node-resolve\resolve-plan-<date>.json
```

- **Plan** writes the plan JSON (each node's values before and after) and a report to `_analytics/reading-tools/node-resolve/`,
  and lists the nodes it leaves with the reason (no sub_group defined for the strong in the cluster; the occurrences
  disagree; several occurrences and no matching surface).
- **Apply** writes the plan whole, into null columns only, and skips and lists a node that no longer holds what the
  plan saw. A second Plan after Apply finds nothing to fill.

---

## 8. The inner-being narrative

### 8.1 The claim register (`iba/app/ps/Narrative-Register.ps1`)

The register of the claims the narrative tells, in iba.db (rules 76, 77, 78). Every write action
takes `-By Claude|Researcher`, and a refusal writes nothing. The published files are regenerated
after every write; never edit them:
- `narrative.claim_register_path`
- `narrative.claim_changes_path`
- `narrative.citation_index_path`

```powershell
# write
iba\app\ps\Narrative-Register.ps1 -Action AddClaim -Text "…" -BeyondText "…" -Source "Ecc 7:9; Job 36:13" -MainChapter 8 -By Claude
iba\app\ps\Narrative-Register.ps1 -Action Edit -Claim C-12 -Text "…" -Verdict Restated -By Claude
iba\app\ps\Narrative-Register.ps1 -Action Tell -Claim C-12 -Chapter 8 -Section "<heading>" -Kind "in part" -Part "…" -By Claude
iba\app\ps\Narrative-Register.ps1 -Action Untell -Claim C-12 -Chapter 8 -Section "<heading>" -By Claude
iba\app\ps\Narrative-Register.ps1 -Action Withdraw -Claim C-12 -Note "why" -By Researcher
iba\app\ps\Narrative-Register.ps1 -Action EditNote -Heading "…" -Text "…" -By Researcher
iba\app\ps\Narrative-Register.ps1 -Action AddChapter -Chapter 10.16 -Title "…" -Kind "key characteristic" -Purpose "…" -PurposeRef "#nnnn" -After 10.15 -CurrentFile "<file>.md" -Note "why" -By Claude
iba\app\ps\Narrative-Register.ps1 -Action EditChapter -Chapter 9 -NewNumber 2 -By Claude
iba\app\ps\Narrative-Register.ps1 -Action EditSection -Chapter 10.1 -Section "<heading>" -NewHeading "<new>" -By Claude

# read-only (reports in narrative.register_report_dir)
iba\app\ps\Narrative-Register.ps1 -Action Find -Verse "1 Samuel 24:5"
iba\app\ps\Narrative-Register.ps1 -Action Find -Chapter 10.12 -Section "…" -Verdict Held
iba\app\ps\Narrative-Register.ps1 -Action Find -NotInNarrative
iba\app\ps\Narrative-Register.ps1 -Action Find -ToldInMoreThanOne
iba\app\ps\Narrative-Register.ps1 -Action History -Claim K-2
iba\app\ps\Narrative-Register.ps1 -Action Check
iba\app\ps\Narrative-Register.ps1 -Action Export
iba\app\ps\Narrative-Register.ps1 -Action QuoteCheck -File <chapter.md> [-Against <previous.md>]
```

**Parameters:**
- **`-Source`** is one string. Items are separated by `;` or ` | `. Each is a verse reference in any
  spelling the chapters use (ranges and lists included), or `lexical:`, `science:` or `study file:`
  followed by text. A new claim needs `-BeyondText` and at least one source.
- **`-Section`** names a block by its heading. Where a heading repeats in a chapter under
  different parents (10.1: "The words" under Fear and under Anxiety), name it as
  `"Parent > Heading"`; the chapter's opening is `"(opening)"`.

**The narrative is held in the database, in blocks (#2172).** A block is a heading and its text
(`narrative_section.block_text`); a claim is told by a block (`narrative_claim_telling.section_id`,
one current telling per claim and block). The chapter files are exports: each change to a block is
followed by the chapter written from the database as its next version, and the file it replaces
moves to the folder's `archive/`. The narrative text is written through `Reading.ps1 -Step
Narrate` (section 8.2), never in a chapter file.

**Actions:**
- **`EditSection`** renames a block (the old row stays as history and its tellings move to the
  new one), changes its level or place, adds an empty block (`-Level`), or retires it
  (`-LastVersion`); the chapter is then published.
- **Chapters** are added and changed only through `AddChapter`/`EditChapter`. `AddChapter` needs
  `-Kind`, `-Purpose`, `-PurposeRef`, and `-After` or `-ReadingOrder`, plus a `-CurrentFile` on disk
  unless the kind is in `narrative.chapter_kinds_without_file`.
- **`QuoteCheck`** checks every quotation in `-File` (or only the lines added against `-Against`)
  against the ESV text in iba.db `verse`. Session-close runs it on every chapter changed.
- **Unresolved references** are written with `verse_id` NULL, listed, and raised as one escalation
  per run. `Check` lists every current one.
- **Direct edits in the database** are logged as `direct edit`. Run `Export` and then `Check`
  afterwards.
- **`AddChapter`** imports a new chapter from its file once (`-CurrentFile`); after that the chapter
  lives in the database.
- **`Check`** reports a chapter file that differs from the database (the file was edited outside the
  register), a newer chapter file than the register's, a block not opening with its heading line,
  two current tellings of one claim in one block, a telling in a block no longer in the narrative,
  and current claims no block tells.
- **`narrative_passage`** is history: the paragraphs that told claims before #2172. It is no longer
  written; a coverage scan reads the blocks (`render_chapter`).

### 8.2 A reading (`iba/app/ps/Reading.ps1`)

The reading process (#2228; on the phases of the analytic process, #2273, design
`outputs/escalation/2273-2274-reading-phases-and-observation-record-design-v6-20261024.md`): a
**reading** is the work on one scope with its objective, anchored on a task or issue. It passes four
gates in order: pre, observe, claims, narrate. Each gate is checked by the tool from the tables, not
asserted. Claude reads and writes in the session; the app resolves the scope, gives everything already
known, writes the findings as rows and checks. Write steps take `-By Claude|Researcher`; a refusal
writes nothing. Files go to `reading.output_dir`, one folder per reading.

```powershell
iba\app\ps\Reading.ps1 -Step Open -Label m21-asking -Escalation 2320 -Objective "the asking words in their verses" -Subgroup M21_asking -By Claude
iba\app\ps\Reading.ps1 -Step Observe -Label m21-asking -By Claude       # the next verses in hand: their sheets
iba\app\ps\Reading.ps1 -Step Record -Label m21-asking -By Claude        # the filled sheets written; the verses done
iba\app\ps\Reading.ps1 -Step Reopen -Label m21-asking -Verse "Gen 37:15; Gen 43:27" -Note "redo under the new parts" -By Claude   # done verses back to waiting
iba\app\ps\Reading.ps1 -Step Check -Label m21-asking -By Claude         # the Observe gate (open -> observed)
iba\app\ps\Reading.ps1 -Step Synergy -Label m21-asking -By Claude
iba\app\ps\Reading.ps1 -Step Apply -Label m21-asking -By Claude         # the synergy JSON, filled
iba\app\ps\Reading.ps1 -Step Check -Label m21-asking -By Claude         # claims gate
iba\app\ps\Reading.ps1 -Step Narrate -Label m21-asking -By Claude       # the narrate JSON, filled
iba\app\ps\Reading.ps1 -Step Check -Label m21-asking -By Claude         # narrate gate
iba\app\ps\Reading.ps1 -Step Publish -Label m21-asking -By Claude
iba\app\ps\Reading.ps1 -Step Account -Label m21-asking
```

**Reopen (#2331).** A done verse of an open reading is put back in hand only by `-Step Reopen`: `-Verse` names the done verses, `-Note` is the reason. The verse goes to waiting; its reason, time and last result stay with it in the scope JSON (`reopened`); no observation changes. Observe then puts it in hand and Record redoes it, modifying its observations in place. Never edit the scope JSON by hand to do this.

States: `open` -> `observed` -> `synergised` -> `narrated` -> `published`. (`gathered` belongs to readings made before
Analysis_phase_1; the step `Gather` is retired, #2320.)

**Analysis_phase_1 (#2320): the verse understanding.** Open, Observe, Record and the Observe gate are one
process, specified in `outputs/escalation/2318-analysis-phase-1-specification-v5-20261030.md`. It creates the
observations for understanding the verse; formulating the claim is the claims work (Synergy onwards), which
uses the surrounding verses. **The scope JSON is an index** (`<label>.json`: the verses, the route that brought
each in, its progress, and the evaluation of its surfaces); it copies no observation. **Each verse is worked by a
query of the database**: Observe reads the verse's surfaces, its existing observations and nodes and the ledger
faces from the tables when the verse is put in hand, so that what earlier verses wrote is seen.

**Open refuses an unmapped home (#2294).** A reading whose subgroup's cluster is an M cluster with any
unallocated or stale surface pair is refused, with the counts. Map the cluster first with
`iba/app/ps/Surface-Map.ps1` (section 7.1).

**What a reading records: findings (#2274, #2320).** A finding is one `ib_observation`: its text, meaning,
implication, basis (stated or read), its kind as tag, on a party or link finding its route, and its structured
`parts` (`ib_observation.parts`, a JSON object: sense, evidence, **polarity** (refusal or pursuit), content,
enactment, party, circumstance, chain, primary_operation, and typed `flags`: data-quality or discovery). Its
`ib_node` rows apply it to every verse and word it covers, each with the occurrence (`verse_lexical_id`), the
word's cluster and **subgroup**, the word's role in the finding, the reading that applied it, and later where
the verse ends up (disposition). The roles of a new node (`cfg_setting reading.node_roles`): for a surface
evaluated `relevant`, characteristic or qualifier; for a surface that `bears_on` the act, object, relational
target or enactment. `standalone` is not a role of a new node. A word with no cluster of its own is given the T-code
it is classified under as `cluster`. The kinds (`reading.observation_parts`): face, qualification, party,
statement, link, use, term, silence (silence is not used by Analysis_phase_1). A description already live is
never written again: the finding names it as `existing` and gains nodes. Every change to a finding or a node is
kept with its reason in `ib_observation_change`. The finding shape (`iba/app/lib/observationrecord.py`):

```json
{"key": "f1", "kind": "statement", "text": "...", "meaning": "...", "basis": "stated",
 "parts": {"sense": "...", "polarity": "refusal", "flags": [{"type": "discovery", "text": "..."}]},
 "nodes": [{"occurrence": 123456, "strong": "H3820A", "cluster": "M64", "role": "characteristic"},
           {"occurrence": 123460, "strong": "H1351", "cluster": "T3", "role": "object"}]}
```

- **`Open`** (0.C) takes `-Objective` (required), `-Escalation` (an open task or issue) and **one**
  `-Subgroup`, which is the home (a qualifier group is refused; `-Home` and the other selectors are refused). A
  segment of the subgroup: `-Surface asks,asked` (the subgroup's surfaces) or `-Verse "Mat 7:8; Job 42:4"` (the
  verses of the subgroup it keeps). A selection above 2,500 verses is held until `-Reviewed`. It writes
  `<label>.json` and the reading row (and `reading_verse`, still, because the claims steps read it). No
  observation is written.
- **`Observe`** puts the next verses in hand (`-Count`, default `reading.verse_loop` `verses_per_sheet`; `-Verse`
  to name one). Each gets a **sheet** in the JSON, read from the tables then: the text and passage; every
  **surface** of the verse (identical Strong and surface once; a grammar hint from `reading.focus_words`), with an
  `evaluation` to fill. A multi-term unit (one STEP span with several codes) is one item: the surface of its one
  content code carries the unit (`units`: its rendering, its parts in word order with each part's own STEP gloss and
  role, and the construct, for example `to/for + smoothness + their + them` for "slippery paths"), and the unit's
  prefixes and suffixes are in that surface's `occurrences`, not separate surfaces; where a unit has several content
  codes (or none) each code is its own surface and says it is part of the unit (`shared` where the word is not
  decided). See section 8.16 (`verse_lexical` and the unit columns). The **existing observations** with a live node on the verse (every stage, any subgroup),
  with their nodes, each with an `action` to fill and, where a node lacks its occurrence or subgroup, a `suggest`;
  the **ledger faces** of the verse not yet linked to an observation; `findings` for new observations. A sheet
  already in hand is not rebuilt.
- **`Record`** checks the filled sheets whole (nothing is written if any is wrong), then writes in one
  transaction. Every surface is evaluated `{"result": "relevant" | "bears_on" | "not_relevant", "reason": "..."}`
  (the reason is `min_reason_chars` or more) and the evaluation is kept in the JSON, not in the tables. A
  surface with no inner-being role gets no observation. Every existing observation takes an `action`: `accept`;
  `modify` (changed **in place**: `set` the columns of `reading.verse_loop` `observation_set`, and per node
  `node_set`; the old value, the new value and the reason go to `ib_observation_change`); `delete` (soft
  delete: the `deleted` column of `ib_observation` or `ib_node` set to 1, with the reason; nothing is
  physically deleted; an observation whose last node is deleted is itself soft deleted); or `merge`
  (`{"action": "merge", "into": id, "reason": ...}`: a duplicate description, identical text, moves its nodes
  to the observation kept and is soft deleted). The sheet lists the errors the check found in `flags`, each
  with a `propose` where a fix is known (duplicate description → merge; silence kind → delete; kind not in
  `reading.observation_parts`, same word with the same role in two observations, node role standalone → no
  automatic fix, modify or delete). The fixes are part of the check and need no separate confirmation (researcher, 2026-10-27): an observation without an action takes its proposed fix when the verse is recorded, and a node's occurrence and subgroup are always completed from `surface_subgroup`; name an `action` to do otherwise. What needs the reading's judgement has no automatic fix and is refused until it has an action: a tag that is not a kind (modify the tag to the kind of what the verse says, `"set": {"tag": "statement"}`, or delete), a same-word-same-role overlap, a standalone role. `fill_nodes` and `confirm_fixes` are no longer needed. Every observation on the verse is on the sheet, whatever its stage (the stage is not used to filter: it was used inconsistently). The reading decides by the wording of each one: `leave` (`{"action": "leave", "reason": ...}`) leaves an observation exactly as it is when its wording shows it is not verse understanding; it is not changed, needs no kind or subgroup and does not count for a surface. What the reading writes has the stage `Analysis_phase_1`. Record enforces the rules for stating an observation (spec 4.1, 4.2; RS-10; #2329 v3): each surface with the role `characteristic` is explored for the nine items (cfg_setting `reading.observation_items`, also on the sheet as `items`), and each applicable item is its own observation: `parts` is `{"item": key}` and, where the item needs them, `polarity` (refusal or pursuit), `mode` (of an operation: done, foreseen, commanded, negated, reported), `flag_type` (data-quality or discovery) and `grounds` (a read observation names the words of the verse that ground it); the kind and the basis are those the item allows (meaning is a face, a stated party is a party with its route, the chain is a link, the rest are statements; role may also be a qualification). An observation true of several characteristics is written once, with a node on each; the items that are not shared (meaning, polarity, object, enactment, operation) are one observation per characteristic. An item the verse does not show gets no observation: state it in that surface's `items_absent` (`{"item": "why the verse shows none"}`); the meaning item is never absent, and the verse always has an observation of the operation (an action description of who or what does what, with its mode). No observation restates a run of the verse text (more than `max_verse_words_copied` words). The sheet's `nuances` (cfg_setting `reading.nuance_pointers`) say where each nuance is recorded, with a verse that shows it; a nuance met with no row gets a row. The old twelve-part form (sense, evidence, before, after, the typed party) is refused: an existing observation in it is modified to its item, or soft deleted. Each surface on the Observe sheet carries `meaning`: the meaning tree, the sense head, the STEP gloss, the related words and, for Greek, the lexicon, as the tables hold them (cfg_setting `reading.sheet_meaning`); a source with nothing held reads as empty and is named as a gap, never filled from memory, and a data-quality flag about meaning sources is written from it; the words that bear on an act are nodes of the observation of the act (a node modify setting `observation_id` moves one, and it takes the next `seq` of the observation it moves to; an observation whose nodes all bear on an act is refused). The time of a verse is in the scope JSON: `in_hand_at` when Observe put it in hand, and in its `result` `in_hand_at`, `at` and `elapsed_seconds` (work one verse per sheet, `-Count 1`, for a time per verse). A surface is shown as STEP glosses the code (`word`, with `span_surface` and `step_gloss` beside it when the span's word is another code's, as `still` for H5750 in `alive`); an existing node written with the span's word is fixed when the verse is recorded. A finding that names an `existing` observation gains the nodes of this verse whatever its kind (a party or link observation too): its kind, route and parts are the live observation's, and a new description, kind or route on it is refused. A reading is filed in its home cluster's folder, `_analytics/Clusters/<cluster_code> - <short name>/<label>/` (cfg_setting `reading.output_dir`, by the filing convention): the scope JSON, the account, the synergy and the narrate files. The rules Record enforces are config, not code: `reading.observation_rules` (the stage written, the kinds not used, the kinds that carry a route, the bears-on refusal, the merge rule), `reading.observation_items` (the nine items: their kinds, bases, sharing and what each carries; the modes; the characteristic roles; the grounds and verse-text checks) and `reading.nuance_pointers`, `lexical.span_surface` (the surface of a code in a multi-code span) and `report.cluster_folder_name_rule` (the cluster folder name); change a rule by changing its row. Record writes verse by verse: a verse with an error stays `in_hand`, its errors are written to
  the sheet's `errors`, and the other verses are recorded (refused only when no verse could be). A relevant surface must be named by a live node with a role of its group; a `not_relevant` surface by
  none. A ledger face is linked `{"observation": id}` or given a `{"reason"}`. The verses become `done` and their
  sheets leave the JSON, with a result (counts and the surface evaluations).
- **`Check`** at `open` passes the **Observe gate** when every verse is `done` and the evaluations in the JSON
  still agree with the live nodes (checked from the tables); the reading becomes `observed` and its verses are
  marked `analysed`, the only way a verse becomes `analysed`. Open items are not part of Analysis_phase_1: they
  are cleared after the claims (specification 4.5).
- **`Synergy`** builds the **synergy JSON** from the tables (B:114): the reading's findings with their
  live nodes, the current or held claims on the scope (with whether each rests on a finding), and the
  open items matched to the scope.
- **`Apply`** (D4 claims) refuses a file not built by this reading's last Synergy. It writes new
  claims (resting on findings or verses), edits and withdrawals; each finding's `dispose` for this
  reading's nodes: `claim`, `held` (an item or a `new_item`), `data`, `context` or `withdrawn`, with its
  reason or carrier; and each matched open item settled: `closed`, `withdrawn`, `superseded`,
  `forward`, or `touched` for an item whose target reaches past the reading (#2250).
- **`Check`** passes the **claims gate** when every node of this reading is disposed (a `claim`
  disposition carried by a current claim), every current claim on the scope rests on a finding, and
  every matched open item is settled or read in part. It then builds the **narrate JSON**.
- **`Narrate`** writes tellings (`tell`), claims held (`hold`) and blocks rewritten whole (`rewrite`,
  the `Narrative-Register` rewrite shape; cited verses marked `citated`), to the narrative rules on
  `reading.narrate`. The nodes whose claim is told are marked `told`.
- **`Check`** passes the **narrate gate** when every current claim on the scope is told or held, and
  every verse of the reading cited in a block has a finding or a claim behind it.
- **`Publish`** publishes each chapter the reading touched whose file differs from the database,
  copies the chapters to the learning4comfort inbox (section 8.6) and checks each is there
  byte-identical.
- **`Account`** writes the reading from the tables: its objective, its gates, the findings it applied
  and the gaps at the gate it is at.
- **The close gate:** the escalation that anchors a reading cannot reach `completed` or `closed`
  while the reading is not published or withdrawn.

**The strand steps are retired (#2228 D-a, 2026-10-23).** `iba/app/ps/archive/Strand-Reading.ps1` (history) and its handler are
in `archive/`, and the four strands (fear, anger, life-death, origin-of-thought) are `superseded`.
Their rows stay: their hits and faces are read as table sources. A hit still unread is a `face_not_gathered`
gap in any reading that reaches its verse. `lib/strandreading.py` stays as the library the reading
reuses (observation checks, `derive_core`).

### 8.3 The verses of a request (`iba/app/ps/Verse-Scope.ps1`)

The scope resolver (#2228; occurrence-shaped, #2295): any request becomes the collection of verses it
stands for, with their occurrences, written as a JSON file. It reads only. Selectors add verses and are combined as a union; give as many as the
request needs. A group or batch is given on the command line or kept in a request file.

```powershell
iba\app\ps\Verse-Scope.ps1 -Label anger-bosom -Cluster M02 -OnlyStrong H3708A
iba\app\ps\Verse-Scope.ps1 -Label ot108 -Thread OT-108
iba\app\ps\Verse-Scope.ps1 -Label batch-1 -File "<request.json>"
```

| Selector | Example | Gives |
|---|---|---|
| `-Cluster` | `M02` or `M02,M01` | a mapped M cluster: the occurrences of its (code, surface) pairs; a T cluster or an unmapped one: the occurrences of its live strongs |
| `-Subgroup` | `M18_desire` | the occurrences of the subgroup's (code, surface) pairs, after settlements; a qualifier group is refused (rule 120) |
| `-Strand` | `anger` | the verses of a strand's word family |
| `-Word` | `anger` | the occurrences whose surface is the word, case aside; never `word_strong` (rule 119). Surfaces holding the word among others are listed, not taken |
| `-Strong` | `H0430` or `G3563G` | a bare code stands for all its derivatives (H0430G, H0430H, ...); a suffixed code for itself |
| `-Verse` | `"Psa 10:2; Luk 14:12-14; Rom 8"` | the verses named: lists, ranges, ranges across chapters, whole chapters |
| `-Chapter` [`-Section`] | `10.1`, `-Section "The bosom"` | the verses the chapter's current blocks cite, or one block's |
| `-Claim` | `C-330` | the claim's verse sources |
| `-Observation` | `12478` | the verses the observation is grounded on |
| `-Item` / `-Thread` | `OT-108.3` / `OT-108` | a thread item by its kind (a scope item: its stored verses), or every open item of the thread |
| `-Home` | `M18_desire` or `M18` | the home, when not the subgroups and M clusters named; never a qualifier group or a T cluster (rule 120) |
| `-File` | a request file (JSON) | the same keys as lists, e.g. `{"cluster": ["M02"], "verse": ["Psa 10:2"], "chapter": [{"chapter": "10.1", "section": "The bosom"}], "only_strong": ["H3708A"]}` |

- **Each verse lists its occurrences** (one `verse_lexical` row each): an M-coded word with its
  subgroup, cluster, kind, two-sense flag, `in_scope` (it brought the verse in) and `home`; an M-coded
  word with no pair is marked `unplaced`; the other clustered words are `context`. A current
  `subgroup-settlement` observation places its occurrence in its own subgroup (rule 122). The other
  subgroups in a verse are shown, to be read, and add no verse (rule 120). The file carries
  `"version": 2`, the `home`, and counts of occurrences in scope, in the home and other subgroups.
- **`-OnlyStrong`** keeps only the verses holding one of the given codes (a bare code again stands for
  its derivatives): the focus on some of the derivatives.
- **A chapter, block or claim gives only the verses it cites.** Whether to pull in more verses through
  a narrative or a claim is a judgement call, not made here.
- **The file** goes to `verse_scope.output_dir` as `<label>-<YYYYMMDD>.json`; a second run with the
  same label on the same day writes `-v2` and archives the first. Each verse carries `routes`: which
  selector brought it in, through which code, heading or reference. `not_resolved` lists, with the
  reason, every reference with no verse row (missing by design, `governance.verse_gap_by_design`),
  block that cites no verse, claim source that is not a verse, thread item whose kind names no verse,
  and code in a cluster, word or strand list that occurs nowhere.
- **Refused, nothing written:** no selector, an unknown cluster, subgroup, strand, word, chapter,
  block, claim, observation or thread, or a Strong's code the request names that occurs nowhere (the
  message suggests its derivatives).
- **Held for review:** a result of more verses than `verse_scope.max_verses` (2,500; above it: M72,
  M47, M65, every T cluster, a thread of many clusters). Reform it (fewer selectors, or
  `-OnlyStrong`), or, once the researcher has reviewed it, re-run with `-Reviewed "<the review>"`;
  the review is kept in the JSON. **Refused:** a request still resolving after
  `verse_scope.max_seconds` (30). Either message lists the verses per selector, widest first.

### 8.4 Where the cluster files name a verse (`iba/app/ps/Reading-Index.ps1`)

The cluster reading index (#2228): the study files under `reading_index.roots` (only
`_analytics/Clusters`; `archive/` folders skipped) read once, every verse reference recorded with
its file, heading section and line (`reading_file`, `reading_section`, `reading_ref`).

```powershell
iba\app\ps\Reading-Index.ps1 -Step Build     # new and changed files read; removed ones marked
iba\app\ps\Reading-Index.ps1 -Step Report    # coverage report -> reading_index.output_dir
```

- **Build** reads a file again only when its content changed (sha256). The earlier rows of a
  changed or removed file are kept, marked deleted. A build stops between files once past
  `reading_index.max_seconds` (120) and says how many are left; run it again to carry on.
- **What counts as a reference:** a book named (`Jer 8:18`, `explicit`); a follow-on that takes its
  book from the reference before it, `(8:21)` (`follow-on c:v`) or `(v. 22)` (`follow-on v.`). A
  bare number in brackets, `(220)`, is not taken: in these files it is mostly a word count. A
  whole chapter (`Psa 51`) is kept as a chapter. A reference that resolves to nothing is kept with
  its reason and listed in the report.
- **Each row** carries the line it stands on and its kind (`heading`, `table row`, `bullet`,
  `paragraph`). A file whose rows are already in `ib_observation` (the October ledgers) is indexed
  too, with the count in `reading_file.imported_observations`.

### 8.5 What is known and what is missing for a scope (`iba/app/ps/Verse-Collate.ps1`)

The collation (#2228): the scope is resolved as `iba/app/ps/Verse-Scope.ps1` resolves it (the same selectors
and the same guard), then for every verse in it everything the project already holds, and the gaps.
It reads only. This is the step before any recording, so that work already done is not done again.

```powershell
iba\app\ps\Verse-Collate.ps1 -Label anger-bosom -Cluster M02 -OnlyStrong H3708A
```

- **Per verse:** the ESV text; the inner-being words (M clusters) with sense and cluster; `verse_meta`
  status; the draft observations (with any October disposition); the strand hits with face or
  reason; the claims resting on the verse and the blocks that tell them; the blocks citing it; the
  matching open thread items (as `Escalation.ps1 -Action Match` matches: the verse, its M strongs,
  their clusters); and the lines of the cluster files that name it, with file, section and line
  (only those lines are read). **Once per strong:** sense, meaning-tree senses, and for Greek the
  Mounce entry (LSJ given only as its size).
- **Gaps per verse:** `not read` (no observation and no strand face; `analysed` alone does not
  count), `read in files only`, `hit unread`, `observed, no claim`, `claim not told`, `open item`,
  `meaning missing`.
- **Files:** `verse_collate.output_dir/<label>-<YYYYMMDD>.json` (the full record) and `.md` (gap
  counts, one line per verse, the lexicon). A cluster file changed since it was indexed is named;
  run `Reading-Index.ps1 -Step Build`.
- **Guard:** the scope's own (`verse_scope.max_verses`, `verse_scope.max_seconds`), and
  `verse_collate.max_seconds` (120). Past it the run is refused: reform the scope.

### 8.6 Copying the narrative to learning4comfort

```powershell
iba\app\ps\Copy-NarrativeToLearning4Comfort.ps1 [-DryRun]
```

This copies the active chapters' current files to `narrative.learning4comfort_inbox_dir`.
Nothing is published to GitHub from here (`governance.no_direct_github_publish`).

### 8.7 Editing the concept grouping (`iba/app/ps/Concept-Edit.ps1`)

The concept grouping is three tables: `concept_domain` (a domain, a chapter of the narrative), `concept` (a
sub-chapter in a domain) and `concept_subgroup` (the link table to the base data, not touched by this tool).
`description` on a domain and on a concept is free text, empty until written (escalation #2355).

```powershell
iba\app\ps\Concept-Edit.ps1 -Action List [-Level Domain|Concept] [-DomainId 3] [-IncludeDeleted]
iba\app\ps\Concept-Edit.ps1 -Action Describe -Level Domain|Concept -Id 3 -Description "<text>"
iba\app\ps\Concept-Edit.ps1 -Action Describe -File <list.json>      # [{"level":"Concept","id":12,"description":"..."}, ...]
iba\app\ps\Concept-Edit.ps1 -Action AddDomain -Name "<name>" [-Ordinal 15] [-Description "<text>"]
iba\app\ps\Concept-Edit.ps1 -Action SetDeleted -Id 15 -Deleted 1      # 0 restores
```

- **Describe** sets the description of a live row and prints the wording it replaces (the replaced text is kept
  only in that run's output). A `-File` list is one unit: if any entry is refused, nothing is written.
- **AddDomain** puts the new domain last in order unless `-Ordinal` is given; the name must be free among live
  domains and the ordinal must not be one a live domain has. The new domain has no concepts and no narrative chapter.
- **SetDeleted** sets (`1`) or clears (`0`) the delete flag of a domain; the row stays. A domain that still holds
  live concepts is not deleted: the refusal names them, because what becomes of them is the researcher's call.
  A domain cannot be restored while a live domain has its name.
- Every change is stamped with the run id and the time (`run_id`, `updated_at`); `-By Claude|Researcher` names who
  made it (default Claude). A refusal writes nothing and is not an escalation.

### 8.8 The first split of the concept surfaces (`iba/app/ps/Surface-Judge.ps1`)

The list is the distinct `surface` of the live rows of `surface_subgroup` (the surfaces the concepts are built on;
rows with a blank surface are left out). Each surface goes to the Ollama server on its own, with no verse, no Hebrew
or Greek code and no neighbouring word, and comes back as one of `behaviour`, `inner_being_state`, `being` or
`other`. A surface goes to the first three only when it definitely belongs there, otherwise to `other`, the list
that is cleaned up in a later pass (escalation #2354). Every answer is inferential until the researcher confirms it.
**Nothing is written to `iba.db`**: the answers are appended, one JSON line per surface as it finishes, to
`<surface_judge.batch_dir>/<Batch>.jsonl`.

```powershell
iba\app\ps\Surface-Judge.ps1 -Action Run -Batch first-split-v1-20261102 -Limit 20     # a pilot of 20
iba\app\ps\Surface-Judge.ps1 -Action Run -Batch first-split-v1-20261102               # the rest of the list
iba\app\ps\Surface-Judge.ps1 -Action Status -Batch first-split-v1-20261102
```

- **-Batch** is the batch file's name: lower-case words joined by hyphens, then `-v` and a number, then `-yyyymmdd`.
- **Run** judges the surfaces not yet judged, most frequent first, and prints each as it finishes. `-Limit n` stops
  after n surfaces. It is resumable: run it again with the same `-Batch` and it carries on; a surface that failed
  (no usable answer after one retry) is recorded with no group and tried again on the next run. Ctrl+C stops after
  the surface in hand has been written. **Before the first surface** the tool checks the server (it must answer
  within `ollama.connect_timeout_seconds` and have the model in `ollama.model`); if not, it refuses at once, names
  the address and writes nothing. If `surface_judge.max_consecutive_failures` (3) surfaces in a row get no usable
  answer, the run halts (condition `halted`) and says so; what was judged is kept.
- **The whole list, unattended: `Cycle`.** It runs for hours, so it is started outside the Claude session (see
  **Running a long job** below), never in a Claude terminal tab. The commands:

  ```powershell
  iba\app\ps\Surface-Judge.ps1 -Action Cycle    -Batch first-split-v3-20261103   # start, or resume after any stop
  iba\app\ps\Surface-Judge.ps1 -Action Progress -Batch first-split-v3-20261103   # from any other terminal, any time
  iba\app\ps\Surface-Judge.ps1 -Action Stop     -Batch first-split-v3-20261103   # end it after the surface in hand
  ```

  It judges in **work periods** of `surface_judge.cycle_work_minutes` (60), opening the ssh tunnel for the period and
  closing it at the end, then **rests** for `surface_judge.cycle_cooldown_minutes` (10) so the server's CPUs cool, and
  repeats until every surface has an answer. If a period ends with the server or the tunnel not answering (or
  surfaces that keep failing) it waits `surface_judge.cycle_halt_wait_minutes` (10) and tries again; after
  `surface_judge.cycle_max_halts_in_a_row` (3) periods in a row with no progress it ends (state `halted`, condition
  `halted`; fix the cause and run `Cycle` again). The machine is kept from sleeping while it runs. The four timings
  are settings: change one by `configmaint`, no code.
- **Progress** reads `<Batch>.progress.json`, which the cycle rewrites after every surface and every 30 s of a rest:
  state (`running`, `cooling`, `waiting_after_halt`, `stopped`, `halted`, `finished`), judged per group, failed, left,
  the mean seconds per surface over the last 50, when work resumes, and an **estimated finish** (work left at that
  mean plus the rests). It says **NOT running** when the file has not moved for longer than a surface can take
  (the cycle was interrupted, for example by the machine sleeping or the Claude app closing). **Stop** writes `<Batch>.stop`; the cycle ends
  after the surface in hand (or within 5 s of a rest) with state `stopped`. Ctrl+C in the cycle's terminal does the
  same. **Restart** is `Cycle` again with the same `-Batch`: it clears the stop flag, keeps everything judged and
  carries on. A second `Cycle` on a batch whose progress is fresh is refused.
- **Running a long job (rule B:125, `long-running-job-starts-outside-the-session`).** A job that runs longer than a
  few minutes (the cycle above, any batch or loop) must not depend on the Claude session. A Claude terminal tab, a
  child of the Bash or PowerShell tool, and a window opened from them all sit in the app's job object and end when the
  app sleeps, restarts or closes its session: the 2026-11-03 cycle died that way at 22:57 UTC, its run row left at
  `running` (researcher, #2354, 2026-11-04). Start it through Windows' own process service instead, output to a log:

  ```powershell
  Invoke-CimMethod -ClassName Win32_Process -MethodName Create -Arguments @{
      CommandLine = '"C:\Program Files (x86)\PowerShell\7\pwsh.exe" -NoProfile -Command ".\iba\app\ps\Surface-Judge.ps1 -Action Cycle -Batch first-split-v3-20261103 *> C:\Bible_study_projects\Logs\surface-judge-cycle-20261104.log"'
      CurrentDirectory = 'C:\Bible_study_projects' }          # ReturnValue 0 and a ProcessId = started
  ```

  Then check before reporting it started: the process's parent is `WmiPrvSE` and it is not in a job object (Win32
  `IsProcessInJob` false), and `Progress` shows `judged` rising. The job has no window; its output is the log. Tell the
  researcher how it was launched, where the log is, how to check, stop and resume it, and that **Windows sleep still
  ends it** (resume with the same command). The machine's sleep setting is the researcher's to change.
- **Status** reads the batch file against the list: judged per group, failed, left, and any surface in the file that
  is no longer on the list.
- Each line holds `surface`, `group`, `reason` (for `other` only), `judged_by` (the model), `errors`, `secs` and the
  server's own token counts. A failed surface has `group` null.
- How the server is reached is config too: `ollama.host` (the address), `ollama.connect_timeout_seconds`, and for ssh
  to the machine `ollama.ssh_target` and `ollama.ssh_key` (a batch key, because the researcher's own key has a
  passphrase; only its path is held). A refused run names them. Read these settings and the record before trying any
  other route.
- The server's own port (11434) does not connect from this machine while ssh does, so a run opens an ssh tunnel by
  itself: from `127.0.0.1:<ollama.tunnel_local_port>` (11435) to the server's own port, with the batch key, and closes
  it when the run ends. Nothing is started by hand and no passphrase is asked. If the tunnel cannot be opened the run
  refuses at once, naming the target and key, and writes nothing. Without the setting the server is called at
  `ollama.host` directly. The port must differ from 11434, the port of the local Ollama on this machine.
- The server, model, limits, the four groups and the question itself are `cfg_setting` rows: modules `ollama` and
  `surface_judge` (`surface_judge.groups`, `surface_judge.word_prompt`). The values `behaviour`,
  `inner_being_state`, `entity` and `other` are also the enum values of `surface_term.surface_group`, the
  group stored for each surface (the group is stored under the name the model is given: `surface_judge.group_stored_as` is empty).

---

### 8.9 The base form of a surface word (`iba/app/ps/Surface-Base.ps1`)

Module 3 of 5. For the words the word-structure methods leave unmatched, each word goes to the AI on its own (no verse, no Hebrew or Greek code, no neighbouring word) and comes back as a base word and its relation to it: `inflection` (tense, plural, participle, comparative, irregular forms), `derivation` (a suffix or prefix that keeps the core meaning) or `none` (no base of the same root meaning, the base is then the word itself). The rule of similar root meaning is in the prompt `base.word` (the register, section 8.13). Every answer is inferential until the researcher confirms it (escalation #2359). The words and the answers are in the tables; **no file is read or written**.

```powershell
iba\app\ps\Surface-Base.ps1 -Action Ask -Limit 20       # a pilot: the first 20 words waiting
iba\app\ps\Surface-Base.ps1 -Action Ask                  # all the words waiting
iba\app\ps\Surface-Base.ps1 -Action Ask -Retry           # also the words whose last answer was not usable
iba\app\ps\Surface-Resolve.ps1 -Action Run               # then: decide the bases from the answers (section 8.12)
```

- **Ask** takes the words the resolve module leaves `unmatched` (no AI call yet), asks the AI through the client, and writes one `ai_call` row per attempt and one `run_batch` row per run. A word with no usable answer after one retry is `ai_failed` and is asked again only with `-Retry`. Before the first word the client checks the server (answers within `ollama.connect_timeout_seconds`, has the model) and refuses at once if not; after `ai.max_consecutive_failures` words in a row with no usable answer the run halts (condition `halted`); what was answered is kept.
- The server is reached through an ssh tunnel the run opens itself (section 8.8: `ollama.ssh_target`, `ollama.ssh_key`, `ollama.tunnel_local_port`). A run of more than a few minutes (the whole list is about two hours) is started outside the Claude session (rule B:125).
- The earlier file route (`-Action Status` and `Run` with a batch file) was retired in stage 6 of #2361; its 676 answers and 31 refusals are in `ai_call` and `surface_derivation`.

### 8.10 The structure of a surface word (`iba/app/ps/Surface-Structure.ps1`, escalation #2361)

Module 2 of 5 of the surface cycle. It matches a surface to a base by the shape of the word: removing an ending (`sins` to `sin`), restoring an e (`abased` to `abase`), undoing a doubled letter (`begged` to `beg`) or removing a prefix gives another surface of the list. Negating affixes and other prefixes are kept as leads, never as bases. Unmatched words get starts-with leads, outside-list bases and sibling groups. What it finds is evidence about shape, not meaning (B:4). It reads `surface_term`, `cfg_base_construct` (one row per construct; `result_kind` says what a match means; switch a row off with `inactive`) and the thresholds in `cfg_setting` module `structure`; **no file is read**.

```powershell
iba\app\ps\Surface-Structure.ps1 -Action Status               # how the structure stands against the evidence rows
iba\app\ps\Surface-Structure.ps1 -Action Match -Check         # preview the difference
iba\app\ps\Surface-Structure.ps1 -Action Match                # write it
iba\app\ps\Surface-Structure.ps1 -Action Show -Surface hides  # one surface and its evidence
```

- **Match** adds the new evidence rows (`surface_derivation`, `accepted` 0, so nothing is chosen) and sets rows no longer produced to `deleted = 1`; a second Match with the same inputs changes nothing. The run's settings and counts are kept on the `run` row.
- A surface the structure finds two bases for (`hides`: hid, hide) is `base_ambiguous` with `base_id` empty and an open `structure_conflict` flag, until the resolve step or the researcher chooses.
- A missing setting is refused and nothing is written. Change a threshold with `configmaint.propose`, then run Match again.

### 8.11 Group corrections of a surface (`iba/app/ps/Surface-Group.ps1`, escalation #2361)

Module 1 of 5. A word of collection a (behaviour or inner_being_state) can have a base that the judge put in `being` or `other`, judged alone, without the sense its derived words show. The repoint corrects such a base from its derived words, as the recorded repoint of 2026-11-04 did (56 changes, 52 held pairs). It reads the tables and `cfg_setting` module `group`; **no file is read**.

```powershell
iba\app\ps\Surface-Group.ps1 -Action Status                 # what the rule would do
iba\app\ps\Surface-Group.ps1 -Action Repoint -Check         # preview
iba\app\ps\Surface-Group.ps1 -Action Repoint                # write
iba\app\ps\Surface-Group.ps1 -Action Repoint -Base build    # accept a proposed base
iba\app\ps\Surface-Group.ps1 -Action Set -Group other -Surface all,much -Reason "Researcher, verbatim: '...' (#2388)" -Check   # preview a group set by ruling
```

- **Judge -Surface a,b,c** (escalation #2388) asks the AI for the group of the named terms only, including a computed base (which the plain `Judge` never asks, since it takes `origin = surface`); a name that is not a live term refuses the call and nothing is asked; a term whose group is confirmed or corrected is not asked. A long list is started outside the session (B:125).
- **Set** (escalation #2388) sets the group of the named surfaces by the researcher's ruling: `-Group` is a value of `surface_term.surface_group`, `-Surface` a comma list of live surface texts, `-Reason` the ruling, quoted, with the escalation id (required). Each surface becomes `confirmed`, judged by `researcher`, with a `surface_event` (`set_group`). A surface that is not a live term refuses the whole call and nothing is written; `-Check` previews; a second run changes nothing. A base moved to `other` leaves collection a: run `Surface-Resolve.ps1 -Action Run -Check` and `Surface-Group.ps1 -Action Repoint -Check` after it.

- A base is corrected by itself when its derived words are inflections (plural, tense, participle, comparative), all in one group, and the base is in an automatic group (`group.repoint_auto_base_groups`, now `other`). It takes the group of its derived words; its state becomes `corrected` and a `surface_event` records the derived words.
- A base judged `being` is **proposed**, never changed by the step alone: you name it with `-Base`. Any pair that is not an inflection, or whose derived words disagree, becomes an open `held_pair` flag; a base a flag already names is left to that reading.
- After a correction run `Surface-Structure.ps1 -Action Match`: the base is now inside collection a. A second Repoint with the same inputs changes nothing.

### 8.12 The base of a surface (`iba/app/ps/Surface-Resolve.ps1`, escalation #2361)

Module 4 of 5. It decides the base of every surface of collection a from the evidence in the tables: the shape of the word (Surface-Structure), a sibling group, the AI base call (`ai_call`), or the word itself. It reads `cfg_setting` module `resolve`; **no file is read**.

```powershell
iba\app\ps\Surface-Resolve.ps1 -Action Status               # how far the stored bases are from what the evidence decides
iba\app\ps\Surface-Resolve.ps1 -Action Run -Check           # preview
iba\app\ps\Surface-Resolve.ps1 -Action Run                  # write
iba\app\ps\Surface-Resolve.ps1 -Action Show -Surface hides  # stored state, decision, evidence rows
```

- The order of the evidence is `resolve.order` (structure, sibling, ollama, own). The states: `matched_structure`, `matched_sibling`, `ai_answered`, `ai_none`, `ai_failed`, `resolved_own`, `phrase_not_tested`, `out_of_scope`, `unmatched` (no AI call yet) and `base_ambiguous`.
- A term outside collection a is `out_of_scope` with no base and, when it was `untouched`, no `collection_state` (the column is empty for a term that is not a base). This holds for a corpus word and, since #2388, for a computed base whose group is judged and is `other` or `entity`; a term already in a collection keeps its state. A computed base not yet judged is left as it is.
- `base_ambiguous` means the structure found more than one base (hides: hid, hide). Nothing is accepted and the word has no base until the AI step or you choose; each has an open `structure_conflict` flag.
- A base you confirmed (`confirmed` or `resolved`) is never changed. Every changed term gets a `surface_event` with the state before and after. A second Run with the same evidence changes nothing.
- Order of a normal pass: Surface-Group Repoint, Surface-Structure Match, the AI base step, Surface-Resolve Run.

### 8.13 Using zeta-assist: the AI client and its control (`iba/app/ps/Ai-Control.ps1`, escalation #2361)

Every AI call of the project goes through one route, `lib/aiclient.py`. It uses the **active model of the role** (`cfg_ai_model`: judge, embed, embed_fast, quick, reviewer) and the **active version of the prompt key** (`cfg_ai_prompt`), keeps the options within `ai.allowed_options`, checks the server and tunnel first, halts after `ai.max_consecutive_failures` questions in a row with no usable answer, and writes one `ai_call` row per attempt. Nothing else calls the server. A write of the `ai_call` row that meets a locked database is tried again `ai.log_write_retries` times, `ai.log_write_wait_seconds` apart, after the connection's own 30 s wait, and then fails as before (#2405).

```powershell
iba\app\ps\Ai-Control.ps1 -Action Status -Live                       # registers, calls made, the models on the server
iba\app\ps\Ai-Control.ps1 -Action Prompts -Key base.word             # every version of a prompt
iba\app\ps\Ai-Control.ps1 -Action PromptAdd -Key base.word -Text '...{surface}...' -Note 'why' -Activate
iba\app\ps\Ai-Control.ps1 -Action Replay -Call 6070                  # is the answer to a stored request the same?
iba\app\ps\Ai-Control.ps1 -Action Compare -Step base                 # prompt versions and models side by side
iba\app\ps\Surface-Base.ps1 -Action Ask -Limit 20                    # the AI base of the words waiting (pilot)
iba\app\ps\Surface-Group.ps1 -Action Judge -Limit 20                 # the AI group of surfaces not yet judged
```

- **Prompts are versions.** A version's text never changes; `PromptAdd` makes a new one with a change note and `-Activate` makes it the one used. `Compare` shows, per version and model, how many calls were answered, refused or failed, and the seconds and tokens, so which prompt worked best is read from the calls, never stored as a claim. A prompt is edited only through this step: a text that no longer matches its hash is refused.
- **Outcomes.** `answered` a usable answer; `refused` the server answered but the check found it not usable; `failed` the call itself failed; `halted` the run stopped on the failure rule. A word with no usable answer is `ai_failed` (base) or `failed` (group) and is asked again only with `-Retry`.
- **Order of a normal pass:** Surface-Group Judge, Surface-Group Repoint, Surface-Structure Match, Surface-Base Ask, Surface-Resolve Run. Ask and Judge read the words from the tables; a run of more than a few minutes is started outside the Claude session (section 8.8, B:125). The test cases used by Compare are provisional (they inform, never decide).

### 8.14 Collections of words (`iba/app/ps/Collection-Build.ps1`, escalation #2361)

Module 5 of 5. A collection has a core word (`love`). The AI judged candidate words against it (synonym, opposite or distinct) and, for the words that are neither, whether they are still associated by meaning; this step turns those judgements in the tables into the members of each collection. It reads and writes tables; **no file is an input**.

```powershell
iba\app\ps\Collection-Build.ps1 -Action Status                                   # stored members against what the judgements decide
iba\app\ps\Collection-Build.ps1 -Action Links -Check                             # preview
iba\app\ps\Collection-Build.ps1 -Action Links                                    # write
iba\app\ps\Collection-Build.ps1 -Action Show -Collection love                    # members by tier, shared ones starred
iba\app\ps\Collection-Build.ps1 -Action Export                                   # a CSV view of the collections to the exports folder
iba\app\ps\Collection-Build.ps1 -Action ExportMembers                                    # member surfaces, one row per verse, cluster and tier, with the verse text
iba\app\ps\Collection-Build.ps1 -Action ExportSurfaces                                   # surfaces of the behaviour and inner-being-state groups, with collection and tier
iba\app\ps\Collection-Build.ps1 -Action Evidence -Collection search                       # the stored entries for a collection, base data to narrative (a list: -Collection love,hate)
iba\app\ps\Collection-Build.ps1 -Action Evidence -Collection search -ByType            # the same rows, one section for each type
iba\app\ps\Collection-Build.ps1 -Action Evidence -Verse "Pro 6:14-16; Mat 11:29"   # the same report for verses, in Scripture order
iba\app\ps\Collection-Build.ps1 -Action Set -Collection love -Status confirmed -Reason 'checked'
iba\app\ps\Collection-Build.ps1 -Action Merge -From insult -Into slander -Reason 'one collection'
```

- **Evidence (#2464, #2467).** `Evidence` writes, for one collection or a list (`-Collection love,hate`), or for a verse or a list of verses (`-Verse "..."`), the entries that exist in the database for every aspect of the words in scope, from the base data through the observations and the claims into the narrative: for a collection the collection row and every link (live first, then removed or superseded) and the member terms; then each member surface's (for a verse: each word's) occurrences in `verse_lexical` with the verse text, every observation on those occurrences with its nodes, the change history of those observations, the claims that rest on them (by observation, or by naming one of the verses) and the narrative sections that tell the claims, with their text. It evaluates nothing, infers nothing, calls no model and writes nothing to a table. Where a link in the chain has no row it says so; the last section lists the blatant errors and omissions found, each rule in words with its rows (for example a live node whose observation is deleted, or a node in a verse of the report with no `verse_lexical_id`). Give `-Collection` or `-Verse`, never both and never neither.
  - **Nodes and Strong's codes in context (#2469).** A node is never listed alone. Each observation is a card: its text fields, then **Supports**, every node of the observation (inside the report or not, marked), grouped by verse in Scripture order with the verse text once, each node with its word, Strong's code (native word, transliteration, gloss), role, disposition, note and cluster. In the occurrences table each word also lists the observations that ground on it, with the node's role and disposition, and shows its stored `verse_lexical` columns (unit size, role as a cluster list, negator, party kind). Each Strong's code of the occurrences has an entry, shown once at its first use and cited by place after that (in `-ByType`, in its own section): language, native word, transliteration, STEP gloss, sense head, the counts as three different measures (STEP token count, verses STEP attests in `strong_verse`, `verse_lexical` rows), the meaning trees stored under the lemma (a lemma's trees are stored together for its variants, so H3820A and H3820B show the same trees, and a tree stored twice shows twice), related terms, LSJ senses and Mounce (Greek only), the cluster assignments with confidence, review flag and rationale, and the placement of the surfaces in subgroups with concept and domain. Morph codes are shown as stored; no table decodes them. The CSV has the Strong's transliteration and gloss beside the code and the observation text beside the node.
  - **Collection members** are those of the exports (a live link of a tier in `collection.export_tiers`: the term and the terms whose base it is); links of the other tiers (possible_opposite, associated, phrase, set_aside) are listed with their reason and do not reach verses here. An unknown or repeated collection name is refused and nothing is written.
  - **Verse references (`-Verse`).** Put the references in quotes and separate the items with a semicolon; each item starts with its book. One verse `Pro 6:14`; a range `Pro 6:14-16`; a range across chapters `Pro 6:30-7:2`; a whole chapter `Pro 6`; several verses of one book `Pro 6:14, 16`; a list `"Pro 6:14-16; Mat 11:29; 1Sa 24:5"`. The book is written as the verse table writes it (`Mat`, `Mar`, `Luk`, `Joh`, `1Sa`, `2Cor`, `Phili`, `Phile`, `Song`; the first letter a capital) or as any alias of `narrative.book_alias_map` (`Matt`, `Matthew`, `1Sam`, `Ps`, `Psalms`, `Philemon`). The order you give them in does not matter. A bad book, a verse or chapter that is not in the verse table (it holds only the verses of the study), a verse given twice (overlapping items) or an item that is a bare number (`Pro 6:14; 7:2`: write `Pro 7:2`) is refused, naming the item, and nothing is written. The verse table does not hold every verse of the Bible: `Gen 1:1` is not in it.
  - **Order.** Verses are always in Scripture order: book in `cfg_book_order`, then chapter, then verse, whatever order they were asked in. The default layout is by unit then by type: a collection report has a section for each member word (alphabetical) and a verse report one for each verse, and inside it the types in chain order (occurrences, observations and nodes, change history, claims, narrative tellings and sections). `-ByType` gives one section for each type across the whole scope instead (the same rows). An observation, claim or narrative section that serves several words or verses is printed in full at the first and cited by its place at the later ones in the default layout.
  - **Files.** They go to `surfaces.exports_root` (`_analytics/surfaces/exports`, the folder of the other collection exports) as `<collection.evidence_name>-<names>-v<n>-<yyyymmdd>.md` and `.csv` (a verse report `<collection.evidence_verse_name>-<references>-...`; with `-ByType` the name ends `-by-type`, with its own version line); the CSV is the sortable chain (one row for each occurrence, node, claim and telling, in the report's order); the previous live versions are archived. If a previous version is open in another program (Excel, a viewer) the run is refused with nothing written and the files left as they were: close it and run again. `-Check` builds the report and prints its counts without writing a file. A large scope gives a large file (the `search` collection: about 2.4 MB, 685 occurrences, 2,316 observations; the chapter `Pro 6`: 377 occurrences). Register the files with `iba/app/ps/Manifest-Rebuild.ps1`. The code is `iba/app/lib/collectionevidence.py`; the joins are its docstring.
- **The two #2379 exports (#2393):** `ExportMembers` and `ExportSurfaces` write the two files the explore-and-analyse work of 2026-11-07 used, from the tables, as often as you ask; the file is a view, never an input. Each row is one surface in one verse of `verse_lexical`, under one cluster of its Strong's code, with its subgroup, concept, domain and the unit columns (`surface_kind`, `unit_surface`, `unit_role`). `ExportMembers` has the members of the collections (tiers of `collection.export_tiers`), one row per tier, with the verse text. `ExportSurfaces` has every surface of the groups of `surfaces.export_groups` and the surfaces not yet grouped, with the collection and strongest tier of each membership (blank when none). The three exports (`Export`, `ExportMembers`, `ExportSurfaces`) take no name (#2413): the file name is `collection.export_names` for the view, the file goes to `surfaces.exports_root` as `<name>-v<n>-<yyyymmdd>.csv`, `n` is the next version over the live and archived files, and the previous live version is moved to the `archive` folder beside it (one live file per export). Register the file with `iba/app/ps/Manifest-Rebuild.ps1`. The code is `iba/app/lib/collectionexport.py`; the rules of the join are its docstring.
- **Tiers:** `core`, `synonym` and `opposite` are members (an opposite is a synonym of the core's pole); `possible_opposite` is a lead, never a member; `associated` and `set_aside` are filed beside the collection. The latest judgement of a pair decides. A word that is a member of more than one collection is `shared`.
- **Your decisions hold.** `Set` and `Merge` are made only on your instruction and carry a reason and an event. A link you remove (set `deleted` to 1 with no successor) is not linked again by `Links`; the 18 pairs the prototype left out are recorded that way. Status lists them as withheld.
- **Changes are traceable.** A link whose tier changes is set to deleted and points to its successor; nothing is physically deleted.
- **Seed and Ask (the front of the process, through the AI client).** `Seed -Word X` makes a collection of a single word of collection a: the AI names its pole (`collection.pole`), whether the pole is a real word, the pole of the pole (reciprocal when it names X again), and lists synonyms and opposites into `collection_listing`. `Ask -Collection X [-Limit n]` judges the candidates: the listed words first, then the words nearest X by embedding (`collection.shortlist_size`, the vectors are a regenerable cache under the working files). Each candidate is judged synonym, opposite or distinct; a distinct word is scored and from `collection.score_threshold` (8) counts as a synonym; an opposite is checked against the pole; a word that is neither is asked for association. One `ai_call` row per question (step candidate, score, pole_check, associated), the collection as subject. Then run `Links`. A run of more than a few minutes is started outside the session (section 8.8, B:125).
- **Gather (#2388).** `Gather -Name <name> -Surface <a,b,c> -Reason <text> [-Check]` makes one collection of the surfaces you name, without the AI: every word is a member at the tier `gathered`, no word is judged the core, and there is no pole. The first word named is only the anchor the collection table requires. It is for words that sit in no collection and are to be assessed together (`iba/app/ps/Engagement.ps1`, section 8.18); `-Reason` is your instruction, quoted, with the escalation id. It refuses, writing nothing, a name already in use, a word named twice, an unknown word and a word that is not untouched; `-Check` previews. `Links` never touches a gathered collection. The tier `gathered` is in `collection.export_tiers`, which is how Engagement and `ExportMembers` find the members.
- **AttachPhrases (#2437).** `AttachPhrases -Reason <text> [-Check]` connects each phrase of the behaviour and inner-being-state groups to collections, without the AI. Every word of the phrase that is a surface is read as its base, and the phrase is linked (tier `phrase` in `collection_link`) to each collection that base is a member of; a phrase no word reaches is read through its own Strong's codes instead (never the shared codes), linking it to the collections of the other surfaces those codes carry. Each link's reason says which route and which word or code. A phrase neither route reaches gets an open flag `phrase_no_match` in `surface_flag`, to inspect. `-Reason` is your instruction, quoted, with the escalation id; `-Check` previews; a second run changes nothing. Phrases are not in the exports (the tier is not in `collection.export_tiers`).

```powershell
iba\app\ps\Collection-Build.ps1 -Action Seed -Word trust
iba\app\ps\Collection-Build.ps1 -Action Ask -Collection trust -Limit 10     # a pilot
iba\app\ps\Collection-Build.ps1 -Action Links -Check
```

### 8.15 The surface cycle as a whole — the order, the recipes, where things moved (escalation #2361)

The cycle turns the English surfaces of the ESV into collections of related words. Five modules, each repeatable alone, all reading and writing tables; the AI is used only through the AI client (section 8.13). The current map of steps, tables and settings, and of the AI use, is generated into the config report (sections 16 and 17), so it is never out of date.

| module | script | what it decides | section |
|---|---|---|---|
| 1 group | `iba/app/ps/Surface-Group.ps1` | the group of each surface (Judge asks the AI; Repoint corrects a base from its derived words) | 8.11 |
| 2 structure | `iba/app/ps/Surface-Structure.ps1` | a surface matched to a base by the shape of the word, as evidence | 8.10 |
| 3 AI base | `Surface-Base.ps1 -Action Ask` | the base of the words the shape leaves unmatched | 8.9 |
| 4 resolve | `iba/app/ps/Surface-Resolve.ps1` | the base chosen from the evidence | 8.12 |
| 5 collections | `iba/app/ps/Collection-Build.ps1` | the members of each collection; Seed and Ask use the AI | 8.14 |
| AI control | `iba/app/ps/Ai-Control.ps1` | models, prompts, calls, replay, compare | 8.13 |

**A normal pass** (each step has a `-Check` or a Status first):

```powershell
iba\app\ps\Surface-Group.ps1 -Action Judge -Limit 20          # new surfaces: their group (AI)
iba\app\ps\Surface-Group.ps1 -Action Repoint -Check           # corrections from the derived words
iba\app\ps\Surface-Structure.ps1 -Action Match -Check         # the shape of the word
iba\app\ps\Surface-Base.ps1 -Action Ask -Limit 20             # the AI base of the words left unmatched
iba\app\ps\Surface-Resolve.ps1 -Action Run -Check            # decide the bases
iba\app\ps\Collection-Build.ps1 -Action Seed -Word trust      # a new collection (AI)
iba\app\ps\Collection-Build.ps1 -Action Ask -Collection trust -Limit 10
iba\app\ps\Collection-Build.ps1 -Action Links -Check          # the members from the judgements
```

**Recipes.** *Why is a word's base this?* `Surface-Resolve.ps1 -Action Show -Surface hides` (stored state, the decision, every evidence row), then `Surface-Structure.ps1 -Action Show`. *Which prompt works better?* `Ai-Control.ps1 -Action PromptAdd` a new version (a draft), `-Activate` it, run a pilot, then `-Action Compare -Step base`. *Is an answer reproducible?* `Ai-Control.ps1 -Action Replay -Call <id>`. *A word is wrong in a collection:* remove the link (set it deleted with no successor, so `Links` keeps it out) or `Set` and `Merge` the collection, with a reason. *Something looks off:* `Config-Maintenance.ps1 -Step Validate` includes the "Surface cycle hygiene" check (a junk surface not marked deleted, an analytic file outside the three folders).

**Working files.** `_analytics/surfaces/working_files` (inputs that were loaded, kept as a record), `_analytics/surfaces/exports` (views generated from the tables) and `_analytics/surfaces/discarded` (methods that will not be needed again, not registered). The paths are `surfaces.*` settings; the tables hold the state. The only cache is the embedding vectors under the working files, which are regenerable. No module reads a working file.

**Where things moved** (the earlier prototype, in the tables now):

| earlier | now |
|---|---|
| the group run files (`first-split-*.jsonl`, the human tests) | `surface_term` (group, reason, state), `ai_call` (step group), `surface_eval_case` (provisional) |
| the repoint workbook (56 changes, 52 held pairs) | `surface_event` (correct), `surface_flag` (held_pair), and the rule `Surface-Group.ps1 -Action Repoint` |
| the structure control (`surface-match-control-v3`) | `surface_derivation` (structure, sibling), the rule `iba/app/ps/Surface-Structure.ps1` |
| the base-form answer files | `ai_call` (ai_base), `surface_derivation` (ollama), `Surface-Base.ps1 -Action Ask` |
| the combined-base workbook | `surface_term` (base_id, base_source, base_state), the rule `iba/app/ps/Surface-Resolve.ps1` |
| the collections, judge, association, list and pole files, the tally and status workbooks | `collection`, `collection_link`, `collection_listing`, `ai_call`; the views by `Collection-Build.ps1 -Action Export` |
| prompts in scripts and settings | `cfg_ai_prompt` (every version), models in `cfg_ai_model` |
| the junk surfaces of the past | `surface_term` with `deleted = 1` (and `surface_flag` junk_surface, settled) |

### 8.16 `verse_lexical` and the multi-term unit (`iba/app/lib/lexical.py`, escalation #2381)

STEP tags one span with every code of a rendering unit ("slippery paths" is `H2519 H9028 H9005 H9038`). `verse_lexical`
keeps one row per code, and tells the code's own word from the unit's meaning:

| Column | Holds |
|---|---|
| `surface` | what belongs to THIS code: its own word, or for an affix code its own STEP gloss (`to/for`, `his`) |
| `unit_surface` | the unit's whole rendering, on every row of the unit |
| `surface_kind` | `own` (its own word), `shared` (a content code of a unit with two or more content codes whose word is not decided: `surface` is the unit's rendering), `gloss` (an affix: `surface` is its own gloss) |
| `unit_size`, `unit_role` | codes in the unit; `sole`, `head` (the one content code), `content_part`, `prefix`, `suffix`, `affix` |

The rules are `cfg_setting lexical.span_surface` (the look-back, `prefix_morph_classes`, `suffix_morph_classes`,
`not_affix_codes`) and are applied by `lexical.build` (`VerseLexical.ps1 -Step lexical.build`). A unit is read with
`lexical.unit_view` (rendering, parts in word order: prefixes, content, suffixes; the construct, for example
`to/for + smoothness + their + them`); the reading sheet, the scope resolver and reports use it. A word enters the
scope resolver through `surface` of rows that are not `gloss`: an affix gloss is not the ESV word at that place.
A join from a surface word to its occurrences (for a count, an export, a collection's evidence) takes `surface_kind`
`own` and `shared` only. Three M-coded rows stay as the 28 October migration left them (held, see the changes file
`outputs/escalation/2326-verse-lexical-surface-changes-v1-20261028.tsv`).

### 8.17 Long jobs against the Ollama server: start, watch, stop (`iba/app/ps/Long-Run.ps1`, escalation #2388)

Every long job that asks the Ollama server keeps the same three files under `Logs/longrun/`, named by the job: `<job>.progress.json` (rewritten after each item and every 30 seconds), `<job>.stop` (the flag a stop asks by) and `<job>.log`. The first job is `collection-batch`: for each sub-group of the bases not yet in a collection, a seed word is made into a collection (`Seed`) and the AI judges its candidates (`Ask`); `Links` runs after every 10 collections and at the end.

```powershell
iba\app\ps\Long-Run.ps1 -Action Plan     -Job collection-batch              # one seed word per sub-group; says how many
iba\app\ps\Long-Run.ps1 -Action Start    -Job collection-batch [-Limit 3]   # detached; -Limit stops after that many sub-groups
iba\app\ps\Long-Run.ps1 -Action Progress -Job collection-batch              # read-only, any time, from any terminal
iba\app\ps\Long-Run.ps1 -Action Stop     -Job collection-batch              # ends after the collection in hand (about 12 minutes)
```

- **Progress** says the state (`running`, `finished`, `stopped`, `halted`), done of total, skipped, failed, what is in hand and since when, the mean seconds per item over the last 20 and an estimated finish, the process id and the last problem. It says **NOT running** when the file has not moved for 2 minutes: the job was interrupted and Start resumes it.
- **Detached.** Start launches the job through Windows' own process service (rule B:125), so it does not end when the Claude app closes or restarts. It keeps the machine from idle sleep while it runs (the display may still sleep). Closing the lid or sleeping the machine by hand still ends it; Progress then says NOT running, and Start again carries on where it stopped (finished sub-groups are skipped, an existing collection is not seeded again, a judged word is not asked again). The Ollama server is another machine and is not affected.
- **Halts.** Three sub-groups in a row that fail (a refusal, a halt, a timeout of 90 minutes) end the job in state `halted`; what was done is kept.
- **Seeds.** A sub-group's seed is the most frequent word of the sub-group whose own sub-group share is at least 0.5, else the most frequent word. A sub-group with only computed bases has no seed and is skipped. The plan is `Logs/longrun/collection-batch.plan.json`; Plan rebuilds it from what is still unassigned.

### 8.18 What each surface does for the inner being (`iba/app/ps/Engagement.ps1`, escalation #2406)

The step between the collections and the narration. A collection's member surfaces (the link's own term and the terms whose base is that term, tiers `collection.export_tiers`) are each assessed in every verse they occur in, with the role they take there; the surface-level group then follows from the roles and replaces the draft group. Claude reads and writes in the session from a working file; the app pulls the file, checks the filled assessment whole and writes it. Everything assessed is inferential (B:4) until you confirm it. No outside word is ever brought in (R4): a verse the member surfaces cannot account for, or a member that does not fit its collection, is a question on the collection and is not repaired here.

```powershell
iba\app\ps\Engagement.ps1 -Action Pull -Collection aloud                       # the working file of the collection
iba\app\ps\Engagement.ps1 -Action Pull -Collection uncovered-words -Batch 1    # only batch 1 of the verses (#2388)
iba\app\ps\Engagement.ps1 -Action Record -File <assessment.json> -Check          # preview the filled assessment
iba\app\ps\Engagement.ps1 -Action Record -File <assessment.json>                 # write it
iba\app\ps\Engagement.ps1 -Action Group -Collection aloud -Check                 # preview the surface-level groups
iba\app\ps\Engagement.ps1 -Action Group -Collection aloud                        # write them
iba\app\ps\Engagement.ps1 -Action Review -Collection aloud                       # the no-bearing verses to read again
iba\app\ps\Engagement.ps1 -Action Close -File <review-assessment.json> -Check    # preview the decisions on the review file
iba\app\ps\Engagement.ps1 -Action Close -File <review-assessment.json>           # write them
iba\app\ps\Engagement.ps1 -Action Check -Collection aloud                        # a report of every member surface against its verses
```

- **Batches (#2388).** `Pull -Batch n` writes only batch n of a large collection, named `engagement-<collection>-pull-batch<n>-<yyyymmdd>.json`; without `-Batch` it writes the whole collection as before. The batches are fixed by a rule (`batch_plan` in `iba/app/lib/engagement.py`), so a collection always gives the same ones: the surfaces in alphabetical order, each whole into the batch in hand while it fits within `engagement.batch_size` verse items, else into a new batch; a surface larger than that is split in its verse order. An existing observation is carried in the lowest batch that holds one of its verses, so it takes one action in one batch only. `Record` checks an assessment against the pull file it names, so a batch is assessed, checked and recorded on its own, one batch at a time. `Group` and `Review` run once after every batch is recorded; `Group` refuses a surface that is not yet assessed in every verse. A surface split over batches gets one observation for each batch and role.
- **Pull** writes `engagement-<collection>-pull-<yyyymmdd>.json` to `engagement.working_dir` (a second pull of the day is `-v2` and the earlier file moves to `archive`, the filing convention). It holds the collection, each member surface with its tier, draft group and state, each of its verses (`verse_lexical` id, reference, ESV text, Strong's code, cluster) and every live observation and node on those verses, any stage. Nothing is written to a table; the assessment reads the file, never the tables.
- **The assessment file** (`pull` names the pull file) has `evaluations` (one for each surface item: `surface`, `vl_id`, `result` relevant, bears_on or not_relevant, `reason`; for a relevant surface a `role` characteristic or qualifier, `gives` for a qualifier, and the `test` of specification 4.1 it passed, `engagement.tests`; for bears_on a role object, relational_target or enactment), `observations` (one for each surface and role: `key`, `surface`, `kind`, `role`, `gives`, `basis`, `text`, `vl_ids`, the verses where it holds; a surface with no bearing is the kind `silence`, with no role) and `existing` (an action for each existing observation of those verses: accept, modify with `set`, delete, merge with `into`, leave; a reason for all but accept).
- **Record** checks the file whole and writes in one transaction: nothing is written if anything is wrong, and the message lists every problem. The observations have the stage `engagement` (not `Analysis_phase_1`, whose check forbids the silence kind), a node for each verse item (its `verse_lexical_id`, Strong's code, cluster and subgroup), and the cluster of the first node. A node's cluster is the cluster of the surface's own `surface_subgroup` row for the code, else the first live `cluster_strong` row. Changes to existing observations are made in place with the reason in `ib_observation_change`, by the same functions as the reading. A second Record of the same file writes nothing new.
- **Group** (rule `engagement.group_rule`): `behaviour` if the surface is a characteristic in any verse; else `inner_being_state` if it is a qualifier in any verse; else `other`, which leaves the study group. The draft is replaced in one write: `group_state` becomes `corrected`, `group_judged_by` `rule:engagement`, and a `surface_event` (`set_group`) keeps the value before. A surface not assessed in every one of its verses takes no group; a group you confirmed is held and listed. A surface that moves to `other` is reported and raised as one escalation for the collection; the collection is never changed (R4). After it run `Surface-Resolve.ps1 -Action Run -Check` and `Surface-Group.ps1 -Action Repoint -Check` (section 8.11).
- **Check** writes `engagement-<collection>-check-<yyyymmdd>.md` to `engagement.report_path`: each member surface, its verse items, how many are assessed, the roles found, its group; the condition `not_assessed` names the surfaces still open.
- **Review** (ruling B of #2411) writes `engagement-<collection>-review-<yyyymmdd>.json`: the verses where every member surface was assessed with no bearing, and the items in them not yet confirmed (the surface, the verse and its text, the no-bearing observation and node). A verse with any surface that has bearing, or any surface not yet assessed, is not in it. With nothing to review it writes no file and says how many verses are already set aside.
- **Close** takes the review file filled in (`review` names it) with `decisions`, one for each item: `confirm` (still no bearing, with a `reason`) or `reopen` (it has bearing: `result` relevant or bears_on, `role`, `gives`, `test`, `reason`), and `observations` for the reopened items as in an assessment. It checks the file whole and writes in one transaction (`-Check` previews). A confirm is kept in `ib_observation_change` (column `reviewed`, with its reason). A reopen deletes the no-bearing node with its reason and writes a node with the role on an observation (an observation left with no live node is soft deleted). A verse is set aside only when all its surfaces are confirmed; `Review` counts those, and `Check` reports the no-bearing items and how many the review confirmed.
- The rules are config (`cfg_setting` module `engagement`): `engagement.stage`, `.roles`, `.group_rule`, `.no_bearing_kind`, `.tests`, `.working_dir`, `.report_path`, `.group_judged_by`. The code is `iba/app/lib/engagement.py`; the test run is `iba/app/tools/temp_2406_engagement_test_run.py`.

## 9. Reports and exports

```powershell
iba\app\ps\Reports.ps1 -Step ReportWord|ValidationWord -Word <word>
iba\app\ps\Reports.ps1 -Step ValidationBook -Book <book>
iba\app\ps\StrongMeaning-Report.ps1                  # meaning-parse coverage
iba\app\ps\SpanAnalysis-Report.ps1                   # span coverage per book
iba\app\ps\SchemaOverview-Report.ps1                 # iba.db data schema, live
iba\app\ps\SchemaOverview-BibleResearch-Report.ps1   # bible_research.db schema, live
iba\app\ps\Registry-Report.ps1                       # word_registry, joined to strong, grouped by sense
iba\app\ps\StrongVerse-Report.ps1 -Word blessing -Strong G2127   # every verse of one Strong's, annotated
iba\app\ps\Passage-Quality.ps1 [-Book <book>]        # passage size distribution
iba\app\ps\Log-Retention.ps1                         # run/escalation/validation log health (read-only)
iba\app\ps\Catalogue-Report.ps1                      # wa_obs_question_catalogue structure (bible_research.db)
iba\app\ps\Catalogue-Update.ps1 -ObsId 224 -Set '{"review_note":"…"}'   # validated update of one catalogue row
iba\app\ps\Export-Tables.ps1 [-Table a,b] [-Out <dir>]   # data tables to CSV, verbatim (not cfg_*)
```

**Report notes:**
- **Which reports are configurable:** report content is set by `report.*` and `validation.show_*`
  settings, changed through §4.
- **StrongVerse:** an unknown word, or a Strong's not linked to the word, fails cleanly.
- **StrongVerse:** shows exact `strong_variant` senses only. It labels combined-tag spans, and
  flags as `UNRESOLVED` any surface that doesn't match its verse exactly once.

---

## 10. Project files and housekeeping

```powershell
iba\app\ps\Manifest-Rebuild.ps1                       # rescan every file in the project (path metadata only); updates by path
iba\app\ps\Manifest-Search.ps1 -Query "type:iba-migration"   # field:value or free text against the path
iba\app\ps\FolderPurpose.ps1 -Action Seed|CrossCheck|AutoAssess|List|Show [-FolderPath …] [-Status …]
iba\app\ps\FolderPurpose.ps1 -Action Set -FolderPath "outputs/escalation" -Type operations -Status authoritative -UsageDescription "…"
iba\app\ps\PathAudit.ps1 -Action Scan                 # hardcoded path literals in scripts (advisory)
iba\app\ps\ContentIndex-SizeProfile.ps1               # .md files by size
iba\app\ps\ContentIndex-Search.ps1 -Query "strong:H2734" [-Csv]   # also gloss:… and word:…; refreshes incrementally first
iba\app\ps\Purge-SoftDeletes.ps1 [-Action Audit|Execute|Retire] [-Live] [-Database …]
```

**What each tool needs:**
- **Manifest search fields:** `registry:`, `type:`, `category:`, `currency:`, `cluster:`, `word:`,
  `date:`, `archived:`, `ext:`.
- **Manifest-Rebuild:** run it after moving files, before relying on a search. A file under an
  `archive/` folder is always `archived`, whatever currency its parent folder has in `folder_purpose`
  (an `_archive/` folder is not an archive folder). The rebuild updates `file_manifest` **by path**: new
  paths are added, changed ones updated, vanished ones removed. The analytic columns of a working file of the
  surface cycle (`module`, `run_id`, `sha256`, `analytic_status`, `migrated_from`) are kept for every file that is
  still there. A moved file is a new path: the module or migration that moves it registers the new path
  (`manifest.register_analytic`) with `migrated_from`. A discarded file is not registered.
- **Where a report goes (rule B:128, #2475):** every analytic report and extract of the study's data is filed under `_analytics/`, in the folder of its module: the surface cycle, collections and engagement under `_analytics/surfaces/exports/`, the reading-process tools under `_analytics/reading-tools/<tool>/`. The tool's `*.report_path` or `*.output_dir` setting points there and the folder is registered with `FolderPurpose.ps1 -Action Set` (type `results`) in the same unit of work. `outputs/` holds the app's own operational output (configs, escalations, validations, the content index, the narrative-register quote checks, cost history, the prose tools). The rule is `cfg_behaviour_rule` B:128 `analytic-reports-and-extracts-in-analytics`; `cfg_control_home` kinds `study_output` and `generated_report` say it.
- **FolderPurpose:** run `Seed` after a reorganisation, before `Manifest-Rebuild`. `Set` is the only
  way to hand-set a folder's type, status or description.
- **ContentIndex:** exclusions are rows of `cfg_content_index_exclude`, changed through §4.
- **Purge-SoftDeletes:** `Execute` without `-Live` is a dry run.

---

## 11. Prose (`bible_research.db`)

```powershell
iba\app\ps\Prose.ps1 -Step Extract -Book Programme [-AlsoMarkdown] [-AlsoDocx] [-IncludeBody]
iba\app\ps\Prose.ps1 -Step Search -Query "grace" [-Book Programme] [-Limit 50] [-Fts]
iba\app\ps\Prose.ps1 -Step ExportChapter -Book "Detail design" -Chapter 1
iba\app\ps\Prose.ps1 -Step ImportChapter -InputFile <edited-file>.md
iba\app\ps\Prose.ps1 -Step SetStatus -SectionIds 22 -Status draft|in_review|approved|archived
iba\app\ps\Prose.ps1 -Step Flag -FlagCode "Terminology change" -Description "…"
iba\app\ps\Prose.ps1 -Step FlagFixPropose -FlagCode "…" -Find "old" -Replace "new"
iba\app\ps\Prose.ps1 -Step FlagFixApply -ProposalFile <report>.json -SectionIds 12,47 -FlagCode "…"
iba\app\ps\Prose.ps1 -Step ApplyPatch -PatchFile <patch>.json [-DryRun]
```

**How the steps write:**
- **Patch-generating steps:** `ImportChapter`, `SetStatus` and `FlagFixApply` write a `PROSE` patch
  to `prose.patch_output_dir`. These steps write no row themselves.
- **`ApplyPatch`** applies a reviewed patch: every operation in one transaction, or none. Run it
  with `-DryRun` first: that applies the operations and rolls them back, so it checks them against
  the live rows. It refuses a patch already applied, and a patch touching a table the
  `apply_session_patch` writer has no `cfg_write_grant` for.
- **`Flag`** writes one `wa_data_quality_flags` row directly.
- **`ImportChapter`** refuses an edit file from which a section has disappeared. Retire a section
  with status `archived` instead.
- **Prose rules:** a new `prose_section_type` needs the researcher's instruction (rule 55). Every
  prose write goes through `record_change_log` (rules 48–50).

**The flag-fix cycle:**
1. Raise the flag with `Flag`.
2. Run `FlagFixPropose` and read its report.
3. Run `FlagFixApply` for the chosen sections, then `ApplyPatch` on the patch it writes.
4. Close the flag on its row once the patch is applied.

---

## 12. Retired scripts

Every script that is in no utility or module is retired: it sits in its folder's `archive/`
(e.g. `iba/app/ps/archive/`, `scripts/archive/`, `iba/app/migration/archive/`) with an inactive
`cfg_utility` row. That includes the PS scripts of inactive work packages and every applied
migration. The full list is `outputs/escalation/2200-retire-list-v1-20261021.json`.

- **To use a retired script,** the researcher approves it: Claude raises an escalation naming the
  script's path and why it's needed, and the researcher's `approved` on it lets that one script run.
  Without it, the hook `.claude/hooks/gate_retired_script.py` refuses the command. Reading a retired
  file is always allowed.
- **A new script** is registered in `cfg_utility` in the same unit of work; `configmaint.validate`
  fails on any live script in no utility or module (`temp_*` excepted).

**Database copies and rollback** (cfg_setting `backup.rollback_method`). A rollback point is not a full copy of iba.db for every run. A run takes a snapshot in `iba/app/db/snapshots/` only when the newest is older than `min_interval_minutes`; the newest `keep_recent` and the newest of each of the last `keep_daily` calendar days are kept. Before a migration or a bulk change take a **named** snapshot on purpose: it is kept in `iba/app/db/snapshots/kept/`, never pruned by the run snapshots (the newest `keep_named` are kept). To roll back, restore the newest snapshot from before the damaging change, then replay what came after from the change records (`cfg_change_detail`, `ib_observation_change`, `escalation_history`), the reading files and git; the NAS keeps a daily copy. To test against a copy of iba.db, make it with the backup API, never a file copy (which misses writes still in `iba.db-wal`):

```powershell
python -m iba.app.lib.dbsnapshot --copy-to <path>.db           # a test copy of iba.db
python -m iba.app.lib.dbsnapshot --reason <id> --named         # a named rollback point, before a migration or bulk change
python -m iba.app.lib.dbsnapshot --list                        # the snapshots kept (run and named)
python -m iba.app.lib.dbsnapshot --prune                       # apply the retention now
```

---

## 13. Where things are

The control map (`cfg_control_home`, config report section 15) names the home of each kind of
control. In `iba/app/`:
- `ps/`: the scripts above
- `run.py`: the dispatcher
- `init.py`: the bootstrap
- `lib/`: the modules
- `handlers/`: the step handlers
- `migration/`: a migration being written; applied ones are in `migration/archive/`
- `tools/`: utilities
- `db/iba.db`: the database
- `db/snapshots/`: the run snapshots, and `kept/` the named ones (backup.rollback_method)
- `reports/`: tool reports

Escalation deliverables are in `outputs/escalation/`. Session logs are in `Logs/`.
