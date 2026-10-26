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
| SC4 | an `Open items` line (in a file changed this session) with no open `OT-nn.n`/`#nnnn`; a researcher message with a holding word (`session_close.held_words`) |
| SC5 | a chapter file changed with no recorded weave; a quotation not in the ESV text; a new register-check finding; a verse in a changed reading file with no placement (rule 79) |
| SC6 | an engaged compliance row with no evidence, or evidence that does not check |
| SC8 | no session log for this session in `governance.session_log_dir`, or a missing section |
| SC9 | a decision line in the log naming no target that changed this session |
| SC10 | a code or config file changed (`session_close.build_scope`) not named in what BUILD.md gained |
| SC12 | whether the narrative copy and the threads export are needed |
| SC15 | a control file (`session_close.control_kinds`) missing, naming a path that does not resolve or points into an archive without marking it as history, carrying replaced-history text, or (read every conversation) over `session_close.always_read_max_bytes` |
| SC16 | a PS tool action that failed twice in the session, or any other call that failed twice with the same error; a designed stop (`session_close.sc16_designed_stops`: COMMIT BLOCKED, NOT PASSED, a Propose waiting for approval) is not a failure |

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
    -Where '{"key":"passage.review_over"}' -Set '{"value":"12"}' -Question "why, and what it affects"
#   PAUSED: a decision_required escalation. After approval (§3.2), re-run the same command with -RunId <run_id>.
```

- **App Mode:** Propose is the only path for a `cfg_*` row. It writes one row, after a coherence
  check, and commits only on approval. Every write is logged in `cfg_change_detail`.
- **Developer Mode:** config work is one idempotent migration under `iba/app/migration/`, writing
  through `configmaint.apply_logged()` (rule 75). Single-row Propose is not used there. A migration
  registers itself inactive, runs once, and then moves to `iba/app/migration/archive/`.
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

- **Pairs** writes `outputs/surface-map/<cluster>-pairs-<date>.json` (setting
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

- **Prepare** writes `outputs/prior-capture/capture-<file id>-<date>.json` (setting
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
- **Report** writes the status report, versioned (`capture-status`, in `outputs/prior-capture/`): documents by `capture_status`, observations by tag, line
  answers, and the nodes with no `verse_lexical_id`.

### 7.3 The node reference sweep (`iba/app/ps/Node-Resolve.ps1`)

A migration step (escalation #2308), run after the capture: it looks up, through the strong and the verse, the
occurrence (`verse_lexical_id`), the morph code and the sub_group code of the nodes that lack them, in every stage and
cluster. Method rules NR-01 to NR-06 on `node_resolve.apply`.

```powershell
iba\app\ps\Node-Resolve.ps1 -Step Plan                                   # what would be filled, and what cannot (reads only)
iba\app\ps\Node-Resolve.ps1 -Step Apply -File outputs\node-resolve\resolve-plan-<date>.json
```

- **Plan** writes the plan JSON (each node's values before and after) and a report to `outputs/node-resolve/`,
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
iba\app\ps\Reading.ps1 -Step Open -Label anger-bosom -Escalation 2172 -Home M02 -Objective "what the bosom shows of anger" -Strong H2436 -By Claude
iba\app\ps\Reading.ps1 -Step Gather -Label anger-bosom -By Claude          # the pre-gap JSON, filled
iba\app\ps\Reading.ps1 -Step Check -Label anger-bosom -By Claude           # pre gate
iba\app\ps\Reading.ps1 -Step Observe -Label anger-bosom -By Claude
iba\app\ps\Reading.ps1 -Step Record -Label anger-bosom -By Claude          # the observe JSON, filled
iba\app\ps\Reading.ps1 -Step Check -Label anger-bosom -By Claude           # observe gate
iba\app\ps\Reading.ps1 -Step Synergy -Label anger-bosom -By Claude
iba\app\ps\Reading.ps1 -Step Apply -Label anger-bosom -By Claude           # the synergy JSON, filled
iba\app\ps\Reading.ps1 -Step Check -Label anger-bosom -By Claude           # claims gate
iba\app\ps\Reading.ps1 -Step Narrate -Label anger-bosom -By Claude         # the narrate JSON, filled
iba\app\ps\Reading.ps1 -Step Check -Label anger-bosom -By Claude           # narrate gate
iba\app\ps\Reading.ps1 -Step Publish -Label anger-bosom -By Claude
iba\app\ps\Reading.ps1 -Step Account -Label anger-bosom
```

States: `open` -> `gathered` -> `observed` -> `synergised` -> `narrated` -> `published`.

**Open refuses an unmapped home (#2294).** A reading whose `-Home` is an M cluster with any
unallocated or stale surface pair is refused, with the counts. Map the cluster first with
`iba/app/ps/Surface-Map.ps1` (section 7.1).

**What a reading records: findings (#2274).** A finding is one `ib_observation`: its text, meaning,
implication, basis (stated or read), its kind as tag and, on a party or link finding, its route. Its
`ib_node` rows apply it to every verse and word it covers, each with the word's own cluster, the word's
role in the finding (characteristic, qualifier, standalone), the reading that applied it, and later
where the verse ends up (disposition). The kinds (`cfg_setting reading.observation_parts`): face,
qualification, party, statement, link, use, term, silence. A description already live is never written
again: the finding names it as `existing` and gains nodes. Every change to a finding or a node is kept
with its reason in `ib_observation_change`. The finding shape (`iba/app/lib/observationrecord.py`):

```json
{"key": "f1", "kind": "qualification", "text": "...", "meaning": "...", "basis": "stated",
 "nodes": [{"verse": "Jon 1:10", "strong": "H1419A", "cluster": "T2", "role": "qualifier"},
           {"verse": "Jon 1:10", "strong": "H3372G", "cluster": "M01", "role": "characteristic"}]}
```

A word with no cluster gets no node (a node is a classification); it is carried in the finding's text.
A qualifier is evaluated for what it gives the characteristic, recorded as a qualification finding.

- **`Open`** (0.C) takes `-Objective` (required: it defines the home of what the reading records), the
  scope selectors of `iba/app/ps/Verse-Scope.ps1` (section 8.3; a selection above 2,500 verses is held
  until `-Reviewed`), `-Escalation` (an open task or issue) and `-Home` (the cluster the scope is
  anchored on; `-Home` is the alias of `-HomeCluster`). A list of codes is quoted:
  `-OnlyStrong 'H0977,H0972'`. It keeps the verses (`reading_verse`), collates the scope (section 8.5;
  `<label>-collation.json`) and writes the **pre-gap JSON** (`<label>-gaps.json`): one section per gap
  type of phase `pre`, each with its guide text. The gap types are config: `cfg_enum reading_gap_type`
  and `cfg_setting reading.gap_types` (phase pre, observe, post or narrate; guide; the table each
  records into).
- **`Gather`** (0.GAP pre) writes each pre-gap item's `record`: `{"finding": {...}}` (a finding,
  quote-checked against the ESV text), `{"table", "id"}` (an existing row), `{"reason": "..."}`, a
  face on a strand hit (`face`, `parties`, `observation`, or `reason`), or for an open item
  `{"response": "..."}` (a `touched` response). New open items go in `new_items` (the
  `Open-Item.ps1 -Action Add` shape). The ids are written back into the file.
- **`Check`** passes the **pre gate** when every item has a row that exists or a reason, and every new
  item is added.
- **`Observe`** builds the **observe JSON** from the tables: per verse its passage, every finding
  already applied to it with its nodes (RO2), and the **words in focus** (`cfg_setting
  reading.focus_words`: every M-coded word, every word in `reading.non_characteristic_strongs`, every
  T2 qualifier that is not a function word by its morph, every T5 negator); the claims on the scope;
  and the catalogue's one-verse questions as prompts by kind (`reading.observe_prompts`; a prompt that
  does not apply is not answered).
- **`Record`** (D4 observe) refuses a file not built by this reading's last Observe. It writes the
  `findings`; the `withdraw` list (a node or a finding no longer supported, with its reason); and each
  word's `record` where no finding is applied to it: `{"reason"}`, `{"item": "OT-nn.n|#n"}` or
  `{"new_item": {...}}`.
- **`Check`** passes the **observe gate** when every word in focus has a live node of this reading,
  an open item or a reason, and every finding in the file is written. The reading's verses are then
  marked `analysed`, the only way a verse becomes `analysed`.
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

---

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
iba\app\ps\Manifest-Rebuild.ps1                       # rescan every file in the project (path metadata only)
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
  (an `_archive/` folder is not an archive folder).
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

**Database copies.** Every run takes a pre-run snapshot in `iba/app/db/snapshots/`. To test against
a copy of iba.db, make it with the backup API, never a file copy (which misses writes still in
`iba.db-wal`):

```powershell
python -m iba.app.lib.dbsnapshot --copy-to <path>.db       # a test copy of iba.db
python -m iba.app.lib.dbsnapshot --reason <why>            # a snapshot now
python -m iba.app.lib.dbsnapshot --list                    # the snapshots kept
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
- `db/snapshots/`: the pre-run copies
- `reports/`: tool reports

Escalation deliverables are in `outputs/escalation/`. Session logs are in `Logs/`.
