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
| `ANTHROPIC_API_KEY` | only for the steps that call the Claude API: the cluster-reading stages (§7) and `iba/app/ps/Book-Narrative.ps1` (§6); from the environment or the repo-root `.env` |

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
iba\app\ps\Start-Iba.ps1                              # bootstrap; prints NEEDS ACTION, then the rules
iba\app\ps\Compliance.ps1 -Action Template            # this session's compliance file
iba\app\ps\Compliance.ps1 -Action Check -Phase Start  # exit 3 until it passes
iba\app\ps\Escalation.ps1 -Action Context             # open escalations and the files they name
iba\app\ps\Escalation.ps1 -Action ThreadCheck -AnsweredBy Claude
iba\app\ps\Escalation.ps1 -Action ThreadAudit
```

**`iba/app/ps/Start-Iba.ps1`** (`init.py`) is idempotent. It:
- validates the config and loads it into the database if needed
- builds missing data tables
- probes STEP with a known answer (H0430 must gloss "God"; the probe values are in config)
- checks how the last session ended: uncommitted paths, an uncommitted session log, a newest
  commit that is not a close's final commit, or a log naming no commit

A check that passes prints nothing. It then prints, in full from the database, the rules that apply
this session, and ends `READY` or `NOT READY`. Runs refuse to start without STEP
(`step.required_for_runs`).

- `-Reload` reseeds the config from the JSON seeds.
- `-Reset` rebuilds the data tables. It drops all data and keeps the config.

**The compliance file** (`Logs/compliance/COMPLIANCE-<date>-<session8>.md`) has one row per rule
delivered in the session's mode, keyed `G:<governance setting>`, `B:<behaviour rule id>`,
`E:<escalation rule id>`. A behaviour rule is delivered by `cfg_behaviour_rule.deliver_when`:
- `always`
- `study_active`, while `cfg_setting behaviour.study_state` is `active`
- `developer_mode`, only with `-Mode Developer`

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
# see what's open (with each item's history); one item's full story
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
iba\app\ps\Escalation.ps1 -Action Context    # every file any version names, resolved to its latest live version
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

Item notes:
- **Naming an item:** `-Item` takes `OT-16.2`, the bare number, `cluster:M03`, or a value unique in
  the thread.
- **A note** follows ` :: `.
- **Matching:** M10 matches M10c; a Strong's number matches its exact code, else its zero-padded
  base; a verse matches inside a range or chapter.
- **Linked tasks:** when a task an item references changes state, the item follows it.

---

## 4. Configuration

```powershell
iba\app\ps\Config-Maintenance.ps1 -Step Validate     # read-only coherence check; findings escalate once
iba\app\ps\Config-Maintenance.ps1 -Step Report       # the config report, at configmaint.report_path

iba\app\ps\Config-Maintenance.ps1 -Step Propose -Table cfg_setting -Op update `
    -Where '{"key":"passage.review_over"}' -Set '{"value":"12"}' -Question "why, and what it affects"
#   PAUSED: a decision_required escalation. After approval (§3.2), re-run the same command with -RunId <run_id>.
```

- **App Mode:** Propose is the only path for a `cfg_*` row. It writes one row, after a coherence
  check, and commits only on approval. Every write is logged in `cfg_change_detail`.
- **Developer Mode:** config work is one idempotent migration under `iba/app/migration/`, writing
  through `configmaint.apply_logged()` (rule 75). Single-row Propose is not used there.
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
iba\app\ps\Build-Passages.ps1 -Book Gal -Suggest                       # propose a boundary; no write
iba\app\ps\Build-Passages.ps1 -Book Gal -Suggest -Confirm -PayloadPath <json>
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

**4. Book-level outputs:**

```powershell
iba\app\ps\WholeBookRead-Report.ps1 -Book Amos -BookLabel Amos
iba\app\ps\Book-Narrative.ps1 -Book Amos -BookLabel Amos
```

`iba/app/ps/WholeBookRead-Report.ps1` reads the filled scaffold-model debates (Amos, Hosea, Joel, Jonah,
Micah, Obadiah). It does not yet read books produced by `iba/app/ps/Debate-Run.ps1`.

`iba/app/ps/Book-Narrative.ps1` generates a book's narrative through the Claude API, then checks it.
- It estimates the cost before calling.
- Over `narrative.generate_max_cost` it refuses.
- Under the cap it pauses for approval:

```powershell
iba\app\ps\Escalation.ps1 -Action AnswerRun -RunId <run_id> -Decision Approve -AnsweredBy Researcher
iba\app\ps\Book-Narrative.ps1 -Book Amos -BookLabel Amos -RunId <run_id>
```

The model and rates are `narrative.*` settings. The real usage of each call is appended to
`narrative.usage_log_path`.

---

## 7. Cluster-reading pipeline (cluster-scoped)

Each stage previews by default: a cost estimate, with no API call and nothing written. Add `-Live`
to run it. Each stage refuses a cluster or subgroup not at its required status.

```powershell
iba\app\ps\VerseReading.ps1 -ClusterCode M67 [-Live]                    # Stage 1, word level (lexical.meaning)
iba\app\ps\RelationalReading.ps1 -ClusterCode M67 [-VerseList "2Cor.8.8,Rom.12.8"] [-Live]   # Stage 1, relational half
iba\app\ps\Run-Stage1Batch.ps1 -ClusterCodes "M35,M51,M61" [-Live -MaxTotalCostUsd 15.00]  # several clusters, unattended
iba\app\ps\BatchProgress.ps1 [-Step lexical.meaning -SelectorKey M49]   # watch a running batch
iba\app\ps\ClusterSubgroup.ps1 -ClusterCode M67 [-Live]                 # Stage 2, subgroups (one call per cluster)
iba\app\ps\CharReading.ps1 -ClusterCode M67 -SubgroupCode <code> [-Live]   # Stage 3, per subgroup
iba\app\ps\CharAnswer.ps1 -ClusterCode M67 -SubgroupCode <code> [-Live]    # Stage 4, the question battery
iba\app\ps\Observation-Enhancer.ps1 -Action Preview|Apply -RuleKey <key>   # apply a confirmed rule to ib_observation
```

**How the stages run:**
- **Stage 1** refuses to run when Layer 1's `role` arrays are stale for the cluster.
- **Stage 2** refuses a cluster that already has live subgroups.
- **Corrections to `ib_observation`** happen only by re-running a stage (rule 68). The enhancer is
  for researcher-confirmed rules only.

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
iba\app\ps\Narrative-Register.ps1 -Action Tell -Claim C-12 -Chapter 8 -Passage "<opening words>" -Kind "in part" -Part "…" -By Claude
iba\app\ps\Narrative-Register.ps1 -Action Untell -Claim C-12 -Chapter 8 -Passage "<opening words>" -By Claude
iba\app\ps\Narrative-Register.ps1 -Action Withdraw -Claim C-12 -Note "why" -By Researcher
iba\app\ps\Narrative-Register.ps1 -Action EditNote -Heading "…" -Text "…" -By Researcher
iba\app\ps\Narrative-Register.ps1 -Action AddChapter -Chapter 10.16 -Title "…" -Kind "key characteristic" -Purpose "…" -PurposeRef "#nnnn" -After 10.15 -CurrentFile "<file>.md" -Note "why" -By Claude
iba\app\ps\Narrative-Register.ps1 -Action EditChapter -Chapter 9 -NewNumber 2 -By Claude
iba\app\ps\Narrative-Register.ps1 -Action EditSection -Chapter 10.1 -Section "<heading>" -NewHeading "<new>" -By Claude
iba\app\ps\Narrative-Register.ps1 -Action Record -File "<the weave's update JSON>" -By Claude

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
- **`-Passage`** is the passage's opening words. A passage is a paragraph, a bullet, a table row
  or a block quote. A list directly under a paragraph belongs to that paragraph's passage.

**Actions:**
- **`Record`** takes one weave's whole update as JSON (the shape is in `record()`'s docstring in
  `iba/app/lib/narrativeregister.py`). It refuses, writing nothing, when anything it names does not
  exist, a version does not match the file on disk, or the update was already recorded. It then
  lists the changed passages and other tellings to read for consistency. With `from_version` =
  `to_version`, it re-reads a chapter's citations without a version bump.
- **Chapters** are added and changed only through `AddChapter`/`EditChapter`. `AddChapter` needs
  `-Kind`, `-Purpose`, `-PurposeRef`, and `-After` or `-ReadingOrder`, plus a `-CurrentFile` on disk
  unless the kind is in `narrative.chapter_kinds_without_file`.
- **`QuoteCheck`** checks every quotation in `-File` (or only the lines added against `-Against`)
  against the ESV text in iba.db `verse`. Session-close runs it on every chapter changed.
- **Unresolved references** are written with `verse_id` NULL, listed, and raised as one escalation
  per run. `Check` lists every current one.
- **Direct edits in the database** are logged as `direct edit`. Run `Export` and then `Check`
  afterwards.
- **`narrative_passage`** holds only passages that tell a claim. A coverage scan must split the
  chapter files (`parse_chapter`) and match rows by `opens_with`.

### 8.2 Copying the narrative to learning4comfort

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
iba\app\ps\WordRegistrySpan-Report.ps1 -Word fear    # a word's Strong's in meaning clusters, with their surface forms
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
- **WordRegistrySpan and StrongVerse:** an unknown word, or a Strong's not linked to the word,
  fails cleanly.
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
- **Manifest-Rebuild:** run it after moving files, before relying on a search.
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
```

**How the steps write:**
- **Patch-generating steps:** `ImportChapter`, `SetStatus` and `FlagFixApply` write a `PROSE` patch.
  Apply it with `scripts/apply_session_patch.py`; these steps write no row themselves.
- **`Flag`** writes one `wa_data_quality_flags` row directly.
- **`ImportChapter`** refuses an edit file from which a section has disappeared. Retire a section
  with status `archived` instead.
- **Prose rules:** a new `prose_section_type` needs the researcher's instruction (rule 55). Every
  prose write goes through `record_change_log` (rules 48–50).

**The flag-fix cycle:**
1. Raise the flag with `Flag`.
2. Run `FlagFixPropose` and read its report.
3. Run `FlagFixApply` for the chosen sections, and apply the patch.
4. Close the flag on its row once the patch is applied.

---

## 12. Scripts not in active use

Their work packages are inactive, so the dispatcher refuses them:
- `iba/app/ps/BookNarrative-Generate.ps1`
- `iba/app/ps/BookNarrative-Validate.ps1`
- `iba/app/ps/Candidate-Curate.ps1`
- `iba/app/ps/Candidate-Quality.ps1`
- `iba/app/ps/Chapter-Generate.ps1`
- `iba/app/ps/ContentIndex-Rebuild.ps1`
- `iba/app/ps/PassageDebate-Report.ps1`
- `iba/app/ps/PassageDebate-Sync.ps1`
- `iba/app/ps/SeedCandidate-Report.ps1`
- `iba/app/ps/Set-Candidates.ps1`
- `iba/app/ps/VerseSpanMeaning-Report.ps1`

These are standalone investigation utilities with no work package:
- `iba/app/ps/create-iba-view-template.ps1`
- `iba/app/ps/create-passage-view-and-export.ps1`
- `iba/app/ps/create-passages-by-book-view-and-export.ps1`
- `iba/app/ps/export-iba-config-tables.ps1`
- `iba/app/ps/generate-iba-db-schema-report.ps1`

`iba/app/migration/` holds one-off migrations, which are not part of any routine.

---

## 13. Where things are

The control map (`cfg_control_home`, config report section 15) names the home of each kind of
control. In `iba/app/`:
- `ps/`: the scripts above
- `run.py`: the dispatcher
- `init.py`: the bootstrap
- `lib/`: the modules
- `handlers/`: the step handlers
- `migration/`: one-off migrations
- `tools/`: utilities
- `db/iba.db`: the database
- `db/snapshots/`: the pre-run copies
- `reports/`: tool reports

Escalation deliverables are in `outputs/escalation/`. Session logs are in `Logs/`.
