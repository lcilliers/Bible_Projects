# IBA app — user guide

> **Start at [`CHARTER.md`](CHARTER.md) first** — the researcher's own statement of what this app
> is *for*. This file is how to run it.

## About the application

The **Inner Being Analysis (IBA) app** serves the Inner Being Analysis Programme — a structured
academic Bible-research programme whose object is **how Scripture expresses the workings of the
human inner being**: the whole inner life (moral, emotional, volitional, relational, vertical and
horizontal), with no theological bias and the human in focus. It works from a registry of ~214
inner-being words, growing over time, each mapped through the STEP Bible to its Hebrew/Greek
originals via Strong's — but the word registry is **scaffolding, not the object**. The analytical
unit is a **focus point**: a latent, emergent configuration of the inner being that is never
observed directly, only **inferred** from what a verse describes it doing. The method is therefore
**infer, don't extract**, with validity established by the **convergence** of independent
verse-grounded witnesses. *(Plan §1.1.)*

**Why the app exists.** For roughly six months the study was attempted through an AI chat interface
and failed repeatedly — the recurring root causes were rules that lived in a model's memory and
were ignored, extraction masquerading as inference, "completeness" measured as coverage rather than
sound reading, and a fragile, un-replayable chat loop. The application exists to make the study
reliable by moving **the rules, the verse-grounding, and the gates out of a model's memory and into
enforced software**: rules encoded and checked deterministically; the model used only for genuine
inference and always validated; runs that are gated, tracked, resumable and replayable in the
database. *(Plan §1.2, §1.4.)*

**How it is built.** PowerShell is the framework (orchestration and process logic); Python modules
do the work; **rules, settings and dependencies live in the configurator, never hard-coded** —
changing a study rule or the pipeline is a configuration change, not a code change. The app is
built out **operation by operation**, within a common framework. *(Plan §2.)*

> ### Scope of this guide — read this
>
> **The application is under active construction, and this guide grows with it — updated
> 2026-08-17 (§2's startup transcript brought current, BUILD.md §119).** Live today: the raw layer (**new-word**, §3; **raw-backfill**, §3a), **config
> maintenance** (§9), **standalone quality checks** (§11), **the lexicon-parsed layer** (§11a),
> **reports and CSV export** (§12), **log retention** (§13), **4 analysis reports** —
> strong-meaning, span-analysis, schema-overview, registry (§12a), and the **lexical-then-debate
> pipeline** (`VerseLexical.ps1`/`Debate-Run.ps1`) plus **whole-book-read / narrative-check**
> (§12b/§12c/§12d) — the live method for building a book's study content. **§8's
> candidate-stamping-and-passages pipeline (`Set-Candidates.ps1`/`Build-Passages.ps1`), §10's
> candidate curation (`Candidate-Curate.ps1`), `Candidate-Quality.ps1`, and `SeedCandidate-Report.ps1`
> are all RETIRED** (2026-07-23/26), as is §12b's own original scaffold-based
> `VerseSpanMeaning-Report.ps1`/`PassageDebate-Report.ps1` pair (2026-08-07) — do not run any of
> these; §12b/§12c/§12d is the current method. Every report auto-archives its previous version and
> pairs with a CSV export by default (§12). Book-scoped reports (lexical, debate, reconciliation,
> narrative) file under `iba/app/verse-analysis/<BookLabel or Book>/` — not `iba/app/reports/`
> (that's for one-off investigatory output only; corrected 2026-08-08, `BUILD.md` §84).
> Word-registry-scoped reports (§12e, added 2026-08-09) file the same way but under
> `iba/app/verse-analysis/word_registry/` — a registry word, not a book. Where this
> guide describes a command or a report, it describes what exists now. Companion docs: `BUILD.md`
> (what's built, how the parts fit) and `GOVERNANCE.md` (how config governs the code) — this guide
> is *how to run it*.

---

## 1. The environment — what the app needs

| requirement | detail |
|---|---|
| **Python 3.14** | with one package: `requests`. Install: `python -m pip install requests` |
| **the local STEP server** | running at `http://localhost:8989` with the tagged module `ESV_th`. The app never uses the web. |
| **nothing else, for everything except §12d** | **no `.env`, no secrets, no keys.** STEP is local and takes no key. The connection is in the config, not the environment. §12d's narrative generator is the one exception — it reads `ANTHROPIC_API_KEY` from the environment or the repo-root `.env` (added 2026-07-30; same key `scripts/_run_ve_reads_governed.py` at the repo root already uses, not a new provision). |

The app lives in `iba/app/`. The database it builds is `iba/app/db/iba.db` (git-ignored). Run all
commands from the repo root (`C:\Bible_study_projects`).

---

## 2. Startup — once per session

```powershell
iba\app\ps\Start-Iba.ps1
```

This prepares the environment and reports `READY`. Typical (repeat-session) output:

```
IBA app — startup
  ✓ config already loaded (use --reload to reseed)
    config_version: app-0.1.0+6c68c02fb4b8
  ✓ data tables present (40)
  ✓ STEP up and tagged (http://localhost:8989, ESV_th)
    known-answer probe: H0430 -> H0430G gloss 'God', 2088 verses

  orientation (read before making changes):
    BUILD.md      The IBA app — build record — ...
    GOVERNANCE.md How the app is governed by config — ...

  governance rules (must be complied with this session):
    governance.build_md_on_code_change: ...
    governance.escalation.scope: ...
    ... one line per `module='governance'` cfg_setting row, ALL of them, every run (currently
    33 rows) — read this block in full, not just the two doc-teaser lines above it ...

READY.
  first run:  iba\app\ps\New-Word.ps1 -Word <word> -Source "<why>"
```

Table/row/rule counts above are a real snapshot (2026-08-17), not fixed — they grow as config and
the DB grow. On a genuinely first-ever run (no config loaded yet), the first two lines instead read
`✓ config loaded (N rows in M cfg_* tables)`, and the data-tables line reads `created` rather than
`present`.

It is **idempotent** — safe to run any time. What it does, in order (`init.py`'s docstring, steps
1–7): validate the config; load it into the DB if not already there (or `--reload` to reseed);
build the data tables if missing (or `--reset` to rebuild); pre-flight STEP; print an orientation
pointer to `BUILD.md`/`GOVERNANCE.md` (added 2026-07-22); **print every `module='governance'`
`cfg_setting` row explicitly, in full** (added 2026-07-23, escalation #305) — not summarised, not
optional: per `governance.rules_must_be_config_driven`, a process rule unread at startup from its
own `cfg_*` row is a rule that exists only in a doc or in memory, which the config itself forbids;
print the `READY`/`NOT READY` status.

**The STEP check is a known-answer probe, not a ping.** It does not merely ask "did something
answer on the port" — it fetches a fixed Strong's (`H0430`) and requires the *expected* answer back:
the gloss must contain `God` and the verse count must clear a floor. A stale, degraded, or wrongly
tagged server that still answers the port **fails** the check with a specific reason — so a green
STEP line means STEP genuinely served the right data, and the probe line shows the evidence. (The
probe values live in config: `iba/app/config/step.json` → `preflight`.)

**If STEP is not running / not right**, it says so and stops short of ready — for example:

```
  ⚠ STEP not ready: STEP answered but the known answer is WRONG: H0430 glossed '…',
    expected to contain 'God'. Stale or wrong module.
```

Start (or restart) the STEP server and run `Start-Iba.ps1` again. Runs refuse to start without STEP
— governed by `cfg_setting step.required_for_runs` (`true`, approved 2026-07-26 — see
`GOVERNANCE.md` §16), not just this sentence; `init.py`'s exit code and every STEP-dependent tool
read that one row rather than each hardcoding the rule separately.

> **A note on "STEP looks closed but the app says up."** Closing the STEP *window* does not always
> stop its *server* — a `step.exe` process can keep holding port 8989 and answering. If the app
> reports up when you thought STEP was down, that stale process is why. Check what is really on the
> port and, if it is a leftover, stop it before restarting STEP:
>
> ```powershell
> Get-NetTCPConnection -LocalPort 8989 -State Listen | Select-Object OwningProcess
> Get-Process -Id <that-pid>          # confirm it is step.exe
> Stop-Process -Id <that-pid>         # only if it is a stale STEP you want gone
> ```

**Variants:**

```powershell
iba\app\ps\Start-Iba.ps1 -Reload    # reseed the config from the JSON (after editing a config file)
iba\app\ps\Start-Iba.ps1 -Reset     # rebuild the data tables — DROPS all data, keeps config
```

---

## 3. The first run — registering a word (the raw layer)

```powershell
iba\app\ps\New-Word.ps1 -Word <word> -Source "<why>"
# e.g.
iba\app\ps\New-Word.ps1 -Word hypocrisy -Source "gap scan 2026-07-18"
```

`-Word` is the English inner-being word; `-Source` is why you are registering it (it is recorded).

**The word is normalised and de-duplicated at entry.** Surrounding whitespace and stray characters
are stripped (`[hypocrisy]` → `hypocrisy`), and matching is **case-insensitive** (`Fear` and `fear`
are one word). So a typo like `[hypocrisy]` is recognised as the existing word, not registered as a
new one. A genuine qualifier like `blindness (spiritual)` is left alone — the stripping only removes
a stray bracket wrapping the *whole* word, not a parenthetical that's part of the word itself
(fixed 2026-07-22; see `BUILD.md` §9). Before registering, the app also checks whether an existing
word already holds the same Strong's — if so, it asks you to confirm it really is a distinct word
(see §4).

The run walks 7 steps. **As of 2026-08-20 (`BUILD.md` §153), `registry.create` no longer pauses for
approval** — it's a standard operational routine, not a design control, and the researcher decided
it doesn't need one: the word is created and the run proceeds straight through, with any
duplicate/typo warning logged in the step's own outcome message instead of blocking:

```
  registry.exists    ok    'malice' is not in the registry — a new word
  registry.create    ok    'malice' registered (id 412)
```

`registry.exists` tells you the true state of the word rather than a vague label:

| the word is… | you see |
| --- | --- |
| never seen | `'<w>' is not in the registry — a new word` |
| awaiting your approval | `'<w>' is in the registry awaiting your approval — will resume its approval` |
| approved, not yet built | `'<w>' is approved but its raw layer is not built — will build it` |
| previously rejected | `'<w>' was rejected before — will propose it again` |
| already built | **stops:** `'<w>' is already built (status raw-complete)` |

This is by design: the app will not add a new registry word without you.

---

## 3a. Backfilling meaning for supporting terms (`Raw-Backfill.ps1`)

`New-Word.ps1` only pulls `strong`/`strong_sense`/etc. for the strongs a *registered* word maps to.
A verse full of spans references many OTHER strongs too — words never onboarded as their own study
term but still needed to read the verse. `Raw-Backfill.ps1` pulls meaning **only** (never verses)
for every strong a book's (or one chapter/verse-range's) spans reference that has no `strong` row
yet — progressive, passage-driven coverage, not a full-Bible bulk pull:

```powershell
iba\app\ps\Raw-Backfill.ps1 -Book Dan                # whole book
iba\app\ps\Raw-Backfill.ps1 -Book Dan -Range 1:1-7   # just this chapter:verse-verse range
```

Self-contained: the lexicon-parsed layer (§11a) and `relatedNos` fetch for the newly-pulled strongs
happen automatically as part of this run — no separate `Lexicon-Parse.ps1` call needed afterward.
You will rarely need to run this by hand — `report.verse_span_meaning` (§12b) auto-backfills the
exact range it's about to render before writing the report (`report.auto_backfill_before_render`),
so this is here for when you want the pull done ahead of time, or on its own.

---

## 4. Escalations — the complete reference

**This is the one, complete place for how escalations work.** Every other section that mentions
`Escalation.ps1` (§9, §10a, §10b, §11, §13, §14) is just that section's own moment of using it —
come back here for the mechanism itself, rather than piecing it together from those examples.

**Full redesign, 2026-08-19/20** (`iba/docs/escalation-redesign-plan-v3-20260819.md`, `BUILD.md`
§152–154). Root cause: escalation `#715`'s updates were being silently overwritten with no trace —
every field on the old single-row table was a mutable value, not a history. Everything in this
section describes the live, rebuilt system — nothing below is the pre-2026-08-20 shape.

### 4.1 What an escalation is, and the two tables behind it

The authoritative record of open items in the project: errors, issues, and building tasks. **It is
not a run-logging mechanism** — a standard operational routine, run through an already-approved app
PS script, is logged by the engine (`run.state`/`resume_point`/`outcome`) and escalates only on a
genuine error; escalation itself is reserved for things that need a decision or need doing
(`BUILD.md` §153). `registry.create` (new-word registration) no longer escalates at all as of
2026-08-20 — see §4.5.

Two real tables, not one:

- **`escalation`** — one row per item, **current state**. `comment`/`context` are **cumulative**
  here — every update's text is appended onto the running total.
- **`escalation_history`** — append-only. Every update writes one row here, but **it's a true
  delta, not a snapshot** (rebuilt 2026-08-20 — the redesign the day before stored a full
  cumulative copy every version, which is wrong: a reader can't see what actually changed without
  diffing consecutive rows by hand). Envelope fields (`state`/`next_action`/`next_action_assigned_to`/
  `originator`/`answered_at`) are always present — they describe this transaction's outcome. Content
  fields (`comment`/`context`/`resolution`/`tried`/`short_description`) are
  `NULL` unless THIS version actually set them.

`-Action History -Id <id>` is how you actually see this — the full version-by-version story for
one item (§4.6).

### 4.2 Two shapes, two vocabularies — deliberately not unified

They answer genuinely different questions, so they don't share one decision vocabulary:

| shape | what it is | vocabulary | answered/updated with |
|---|---|---|---|
| **dispatcher-tied** | a real `run.py` pause — `configmaint.propose`/`validate`, a quality-check finding (`candidate.validate`/`passage.validate`/`lexicon.validate`), a crash, a report-stop. Correlated to the exact paused run via `run_id`. These are **development/design controls** — changes to the app's own behaviour — and correctly keep a real, gated approval. | `approve \| reject \| revise \| hold \| noted` — **unchanged from before the redesign** | `-Action AnswerRun` |
| **manual** | the researcher/Claude backlog-of-work-and-issues workflow — raised via `-Action Raise`, not by any running step | `ready_for_approval \| approved \| reject \| revise \| noted \| review` | `-Action Update` |

`escalation.type` — `task \| run_error \| issue \| notice \| config` — is a separate, orthogonal
axis: classification for humans reading the list, set at raise-time (`-Type` on `-Action Raise`,
default `task`; the app picks it for code-raised rows — crashes/report-stops are `run_error`, a
`configmaint.propose` pause is `config`). **One type DOES branch behaviour** (register v9, D12,
2026-08-21): `-Type notice` closes on arrival — `state='closed'`, no `next_action`, no review/
decision cycle at all, for a pure FYI that needs no response. Every other type (including `issue`,
which reuses this same manual vocabulary in full — no separate scheme) defaults identically:
`raised`/`review`.

### 4.3 States — config-driven, not hardcoded

`cfg_enum.escalation_state`, active members: `raised`, `re-assigned`, `on-hold`, `in-progress`,
`closed`, `completed`, `withdraw`, `supersede`. Which one a transaction produces is now read from
**`cfg_escalation_transition`** (rebuilt 2026-08-20 — the prior redesign had this as a hardcoded
`if`/`elif` chain with no config representation at all) — one row per rule, evaluated in `priority`
order per shape (`manual`/`dispatcher`), first match wins:

| priority | shape | next_action | fires when | → state |
|---|---|---|---|---|
| 1 | manual | `approved` | `resolution` present (this call or a prior one) | `completed` |
| 2 | manual | `reject` | always | the party's explicit `-State withdraw`/`supersede` choice, `-Comment` required |
| 3 | manual | `revise` | always | `in-progress` |
| 4 | manual | `noted` | always | `closed` |
| 5 | manual | `ready_for_approval` | always | `re-assigned` (register v9, D27 — its own explicit row; previously relied on rule 6's `-AssignedTo`-changed condition, which isn't guaranteed true) |
| 6 | manual | any | you gave an explicit `-State` | that `-State` (escalation #762, 2026-08-21 — outranks rule 7 below; previously `-AssignedTo X -State on-hold` silently landed on `re-assigned`, the explicit `-State` had no way to win) |
| 7 | manual | any | `-AssignedTo` changed, no more specific rule matched | `re-assigned` |
| 8 | manual | any | nothing else matched | state unchanged |
| 1 | dispatcher | `hold` | always | `on-hold` |
| 2 | dispatcher | `noted` | always | `closed` |
| 3 | dispatcher | any | always | `completed` |

Field requirements (comment@Raise, resolution@ready_for_approval and re-confirmed@approved,
state@reject, tried@Claude-revising-own-item) are config-driven too, in
**`cfg_escalation_requirement`** — same reason: no longer a rule a reader has to find by reading
Python. Register v9 (D26, 2026-08-21) added a mechanical guard: an Update carrying `-Comment`/
`-Context`/`-Tried` is refused outright if the resulting state would still be `raised` — move it off
`raised` first (`-State in-progress`, or via `-NextAction revise`/etc.).

**D14/D15 RETIRED 2026-08-27, escalation #909** — `from_id` (which item this one was spawned from)
and `related_activity`'s pairing/graph role are both gone, columns physically dropped from
`escalation`/`escalation_history`. Two live audits this session found the mechanism unreliable and
never actually used, on top of escalation #768's own 10-round closure (`GOVERNANCE.md` §56).
Researcher, verbatim: *"the related-activity and fromid columns in the table is unreliable, and
does not serve a purpose, and is very confusing and distracting in the history report... so scrap
it."* `-RelatedActivity`/`-FromId` no longer exist as parameters anywhere in this guide. Full
record: `GOVERNANCE.md` §57.

**Two-stage approval now actually enforces separation of duties — but as an AUTHORITY check, not an
identity check** (register v9, D25, 2026-08-21, correcting a shipped defect): `next_action=approved`
is refused only if you are NOT the party `ready_for_approval` most recently assigned the item to.
Same party is fine when that party holds the authority (Claude assigning an item to itself, then
approving it, is a legitimate, visible self-authorisation for items within Claude's own remit) —
what's refused is approving something `ready_for_approval` assigned to someone ELSE.

### 4.3a `resolution_kind` — decision-required vs self-correctable (2026-08-22, escalations #798/#799)

A second axis, orthogonal to shape/type/state: **every item raised now carries
`resolution_kind`** — `decision_required` or `self_correctable` — answering one question: *does
closing this item require deciding something new, or only correcting execution against something
already decided?* This is `cfg_behaviour_rule` `decision-points-are-terminal-not-inline` (class
`development`), the project's working-method rule, not just an escalation-module detail:

> *"A point that requires a NEW decision (a judgement call, an ambiguity, something not already
> specified) is TERMINAL: it must not be answered inline and resumed. It is recorded as an open
> item and routed back into design/specification... A point that instead reveals Claude's own
> execution error against an ALREADY-settled, already-approved design (a typo, a wrong parameter, a
> slip) is SELF-CORRECTABLE: Claude fixes it directly, records what was wrong and what changed, and
> continues — no new approval is required, because no new decision was made."*

`-ResolutionKind DecisionRequired|SelfCorrectable` is **required on `-Action Raise` — no default**,
same discipline as `-AnsweredBy`. `-Type` is respected as given regardless of `-ResolutionKind` —
it no longer forces `issue` under `decision_required` (removed 2026-08-26, escalation #872:
`task`/`note` must be usable types too). `type` stays immutable after Raise, same as
`run_id`/`source`/`at_step`/`raised_at`.

Two actions close a self-correctable item without a design-approval cycle, and one converts it
mid-flight if the "simple fix" turns out not to be simple:

- **`-Action ResolveSelfCorrectable`** — fixed it, done. No approval step, because the approval
  already happened when the design itself was approved; only the execution slipped.
- **`-Action EscalateToDecision`** — the attempted self-correction surfaced a genuine judgement call
  the design didn't anticipate. Converts the item to `resolution_kind=decision_required` and routes
  it to a real decision, same as any other decision-required item. This is what `-Tried` was
  originally for.

A `decision_required` dispatcher-tied pause (a `run.py` config proposal, crash, or report-stop) now
always routes to a terminal stop when answered — it never silently resumes inline the way a
`self_correctable` one can.

**A recurring `decision_required` result on the SAME routine, run after run, is itself a design
defect** — the rule's own words: *"it means a threshold or parameter that should have been
specified once, in config, during design, was left to be re-asked every time instead. That is a
design gap to close (add the missing config), not a pattern to formalise."* Three examples fixed
this way in the same build: `narrative.py` (an API cost cap — now a hard `narrative.generate_max_cost`
refusal, no question asked), `raw.py` (`raw.zero_strongs_action` config, default `reject`), and
`passage.py` (per-book thresholds `cfg_passage.passage.max_single_verse_pct`/
`max_avg_verses_per_passage` — a book within bounds is accepted automatically, only a genuine
breach still asks).

### 4.4 The two-stage approval (manual items only)

Splitting "I think this is done" from "confirmed done" was a deliberate correction — the researcher
wanted two real history rows for an approval, not one:

1. The party who did the work sets `-NextAction ready_for_approval`, `-AssignedTo <the reviewer>`,
   `-Resolution "<what was done>"` (resolution required here — register v9, D25). Lands on
   `re-assigned` (rule 5 above, its own explicit row as of D27).
2. The reviewer sets `-NextAction approved` (plus any further `-Comment`). Since `resolution` is
   already on the row, rule 1 fires → `completed`. **Refused if the approver is NOT the party
   `ready_for_approval` assigned it to** — an authority check (D25), not identity: the same party
   approving its own `ready_for_approval` is fine when it holds the authority.

Claude may complete its own straightforward, fully-recorded fixes this way without the researcher
in the loop for step 2 — e.g. Claude raises a code error, fixes it, records what was tried, and
self-approves once nothing further is needed. Researcher approval is for genuine judgement calls,
or anything the researcher raised — not a blanket rule on every item (researcher, 2026-08-19).

### 4.5 `registry.create` no longer escalates (2026-08-20, `BUILD.md` §153)

New-word registration is a standard operational routine, not a design control — it needs no
approval mechanism at all any more. A new word is created and logged straight through:

```powershell
iba\app\ps\New-Word.ps1 -Word hypocrisy -Source "gap scan 2026-07-18"
#   registry.create   ok   'hypocrisy' registered (id 412)
#   raw.discover … raw.validate   ok
#   COMPLETE — raw layer built for 'hypocrisy'.
```

The old duplicate/typo check (an existing word already holding all of the new word's Strong's) is
kept as a signal, not removed — it now surfaces as a note in that same `ok` line (`-- POSSIBLE
DUPLICATE: ...`), logged by the engine, not a blocking question.

### 4.6 The seven actions that exist today

(List, History, AnswerRun, Raise, Update, Correction, plus the two `resolution_kind` actions added
2026-08-22 — ResolveSelfCorrectable, EscalateToDecision, §4.3a.)

**List/History now dispatch through `run.py`** (register v9, D4/D16/D23, 2026-08-21) — work package
`escalation-reporting`, steps `escalation.list`/`escalation.history` — instead of `Escalation.ps1`
calling the Python module directly, matching every other report script's pattern. `-Action List`
no longer renders the D15 exception sections (Cycle/Dangling/Mismatched pairing/Missing link/
Incoherent link) — retired along with `from_id`/`related_activity` themselves, escalation #909.

```powershell
# see what's open, WITH FULL HISTORY inline underneath each item (not just current state) --
# writes escalation.list_report_path (default iba/app/reports/escalation-list.md, archived on
# regenerate):
iba\app\ps\Escalation.ps1 -Action List

# deep-history report for ONE item -- its full version-by-version story:
iba\app\ps\Escalation.ps1 -Action History -Id 741

# answer a DISPATCHER-TIED pause (config proposal, quality-check finding, crash, report-stop) --
# UNCHANGED from before the redesign. -AnsweredBy is REQUIRED -- no default, say who you are:
iba\app\ps\Escalation.ps1 -Action AnswerRun -RunId <run_id> -Decision Approve|Reject|Revise|Hold|Noted -AnsweredBy Claude|Researcher [-Comment "..."] [-Resolution "..."]

# raise a new MANUAL item -- -Question becomes the (immutable-after-raise) title, MAX 60
# CHARACTERS, must read like a title/subject -- a bare '--' anywhere in it is rejected (a reliable
# sign it's a compressed sentence, not a title). -Comment is required (minimum: what this is
# about). -AnsweredBy is REQUIRED. -ResolutionKind DecisionRequired|SelfCorrectable is REQUIRED --
# no default (§4.3a) -- -Type is respected as given regardless of -ResolutionKind (no longer forced
# to issue under decision_required, escalation #872, 2026-08-26).
# -Source (default 'researcher'), -Type (default task; task|run_error|issue|notice|config|note --
# 'notice' closes on arrival, D12; 'note' is a plain searchable category, no special behaviour),
# -AssignedTo (default Claude):
iba\app\ps\Escalation.ps1 -Action Raise -Question "Short Title, <=60 Chars" -Comment "what this item is about, and any detail" -ResolutionKind DecisionRequired|SelfCorrectable -AnsweredBy Claude|Researcher [-Type task|run_error|issue|notice|config|note] [-AssignedTo Claude]
# prints the new id -- update it with -Action Update

# close a SELF-CORRECTABLE item you already fixed -- no approval step, the design was already
# approved, only the execution slipped (§4.3a):
iba\app\ps\Escalation.ps1 -Action ResolveSelfCorrectable -Id <id> -Resolution "what was wrong, what changed" -AnsweredBy Claude|Researcher

# convert a SELF-CORRECTABLE item to DECISION_REQUIRED mid-fix -- the attempted correction
# surfaced a genuine judgement call the design didn't anticipate (§4.3a, -Tried's original
# purpose):
iba\app\ps\Escalation.ps1 -Action EscalateToDecision -Id <id> -Tried "what was attempted, what it revealed" -AnsweredBy Claude|Researcher

# every subsequent change to a MANUAL item -- comments, decisions, reassignment, state changes,
# ALL through this one action; resulting state is DERIVED from what you set via
# cfg_escalation_transition (§4.3), not chosen directly. -Comment/-Context are CUMULATIVE in
# `escalation` -- pass only the increment, it's appended onto the existing text -- but
# `escalation_history` stores only that increment for this version, not the running total.
# -AnsweredBy is REQUIRED:
iba\app\ps\Escalation.ps1 -Action Update -Id <id> -AnsweredBy Claude|Researcher [-NextAction ready_for_approval|approved|reject|revise|noted|review] [-AssignedTo Claude|Researcher] [-State on-hold|in-progress|closed|withdraw|supersede] [-Resolution "..."] [-Tried "..."] [-Comment "..."] [-Context "..."]
# -Comment must be passed with the -Comment flag, never as a bare trailing argument -- positional
# binding is off, so an unflagged argument errors instead of silently landing on the wrong parameter.

# ★ ERROR CORRECTION ONLY (escalation #774, 2026-08-21) -- NOT a normal workflow action, do not
# use this for ordinary changes (use -Action Update above for those). A copy of Update that works
# on an item in ANY state, including closed/completed (Update structurally refuses those), and can
# set -ShortDescription (Update has no such parameter at all -- the title is otherwise immutable
# after Raise, §4.7). state/next_action are taken EXACTLY as given, never auto-derived via
# cfg_escalation_transition -- if you omit them, the item's current state/assignment carry forward
# unchanged, which is the normal case: most corrections fix content, not workflow position.
iba\app\ps\Escalation.ps1 -Action Correction -Id <id> -AnsweredBy Claude|Researcher [-ShortDescription "corrected title, <=60 chars"] [-NextAction ...] [-AssignedTo Claude|Researcher] [-State raised|in-progress|on-hold|re-assigned|closed|withdraw|supersede|completed] [-Resolution "..."] [-Tried "..."] [-Comment "..."] [-Context "..."]
```

`-Action Raise`'s `-Question`/`-Comment` are stored **verbatim** — they don't get reworded or have
analysis folded in (beyond the title-shape check above). What you write is the record.
`short_description` (the `-Question` text) is **immutable after Raise** — see §4.7 for how to
correct a wrong one. **`-AnsweredBy` has no default inside `lib/escalation.py` itself** — a silent
`'Researcher'` default previously misattributed dozens of history rows to the wrong party in one
session, when Claude was the one actually running the command. `Escalation.ps1` (2026-08-21) adds
one safe, narrow auto-attribution on top of that: if `-AnsweredBy` is omitted AND the shell is NOT
running under Claude Code (`$env:CLAUDECODE` — set in every shell Claude Code drives, never set in
a terminal you open yourself), it defaults to `Researcher` — closing the friction of typing it by
hand every time, without reopening the original bug: Claude's own invocations always have
`$env:CLAUDECODE=1` set, so they still hit the hard stop, unchanged.

The six single-purpose pre-redesign actions (`Edit`/`Pause`/`Resume`/`Retract`/`Reassign`/
`Complete`) no longer exist — they're all just `-Action Update` calls now, with the right
`-NextAction`/`-State`/`-AssignedTo` combination (plan v3: *"there are only two transaction types...
the resulting state is determined by the values in the fields"*). Word-scoped `-Action Answer` is
retired outright, not replaced (§4.5).

### 4.7 Correcting a wrong title, or superseding an item entirely

`short_description` can't be edited via `-Action Update` — but it CAN via `-Action Correction`
(§4.6, escalation #774), which exists exactly for this: `-Action Correction -Id <id>
-ShortDescription "the real title" -AnsweredBy ... -Comment "why"`. Use this for a genuine mistake
(a typo, an over-long title the raise-time guardrail should have caught but predates it, a title
that turns out to describe the wrong thing) — it's still the SAME item, same history thread, just
with a corrected fact recorded on top (a new version, old versions untouched).

Superseding is a DIFFERENT situation — not a correction, a replacement: the item needs to be
replaced by newer, better-scoped work, not just have its title fixed. Raise a new item with the
correct title, naming the old one in `-Comment`/`-Context` ("supersedes #900"), then update the OLD
item with `-NextAction reject -State supersede -Comment "superseded by #901 — <why>"`. Check each
item's own `-Action History` separately (escalation #909, 2026-08-27: they're no longer linked
into one combined thread — see the retirement note above).

---

## 5. Removing test data

To remove a word you registered by mistake or while testing:

```powershell
python -m iba.app.tools.purge_word --word "[hypocrisy]"          # dry-run: shows what would go
python -m iba.app.tools.purge_word --word "[hypocrisy]" --yes    # actually delete
```

It matches the word **literally** (so you can target malformed residue exactly as it sits in the
registry) and removes only that word's own rows — its registry entry, discovery links, escalations,
runs, and validations. It **does not** touch the shared raw layer (strongs, verses, spans), which
other words may reference; a full cascading delete is a later operation. Always dry-run first.

---

## 6. The word report

```powershell
iba\app\ps\Reports.ps1 -Step ReportWord -Word hypocrisy      # -> iba/app/report-hypocrisy.md
```

It shows, per word: the **validation** results, the **strongs and their meaning**, and **sample
verses** with the verse text and every word's span (Strong's + morphology), each backtracking to
its sense. Every row is checkable against STEP — the `getInfo` / `masterSearch` URLs are in the
report header.

**The database** (`iba/app/db/iba.db`) holds the data directly — browse it with any SQLite tool, or
dump every table to CSV for a narrative-free look (§12).

---

## 7. What the reports show is configurable

Report content is config, not code — every toggle is a `cfg_setting` row, changed the sanctioned
way (§9), never by hand-editing a JSON seed:

| setting | effect |
|---|---|
| `report.sample_verses` | how many sample verses the word report shows |
| `report.show_verse_text` | show the verse text above its spans |
| `report.show_validation` | show the validation table |
| `report.span_fields` / `report.strong_fields` | which columns the span/strong tables show |
| `validation.show_health` / `show_delta` / `show_integrity` / `show_references` / `show_expectations` | word-report validation sections |
| `validation.show_health` / `show_candidate` / `show_passages` | book-report validation sections |

---

## 8. Building the base layer — candidates and passages — RETIRED, corrected 2026-07-29

**This whole pipeline is retired and must not be run.** `Set-Candidates.ps1`
(`candidate.seed`/`candidate.set`) was retracted 2026-07-23 (`GOVERNANCE.md` §15D);
`Build-Passages.ps1` (`passage.build`) was retired 2026-07-26 (`GOVERNANCE.md` §17/`BUILD.md`
§23) — *"the past use, and rules have moved on... there is nothing to migrate from the old to the
new"* (the researcher's own words). Both work packages are `inactive=1` in `cfg_work_package`
today. This section previously showed them as the live way to build a book's passages — stale
since 2026-07-26, found and corrected in the same 2026-07-29 audit that produced
`PLAN-config-system-remediation-v1-20260729.md`.

**Nothing today derives a passage's boundaries algorithmically.** A passage is now whatever range
`hib.set`/`passage.build` is run over — a judgement call per debate, per the reading method —
tracked (not generated) by `lib/passagetrack.py`. **See §12b below** for the current method:
`VerseLexical.ps1` (once, book-scoped) then `Debate-Run.ps1` (per chapter/range) — the
`VerseSpanMeaning-Report.ps1`/`PassageDebate-Report.ps1` pair named here previously was itself
retired 2026-08-07 (§12b).

`candidate_seed`/`span_candidate` remain in the DB (retracted data kept for provenance, not
purged — same as `passage`/`verse_passage`'s own retirement, §17) but nothing writes to them or
reads them for any live workflow.

---

## 9. Configuration maintenance — the only way to change a `cfg_*` row

**Never hand-edit a JSON seed or the DB directly.** Every config change — a setting, an enum value,
a candidate accept/reject rule, anything in a `cfg_*` table — goes through one gate:

```powershell
iba\app\ps\Config-Maintenance.ps1 -Step Validate
#   read-only coherence check: schema FKs, may_source, handlers resolve, on_fail paths, orphan
#   configs, settings needing justification — safe to run any time

iba\app\ps\Config-Maintenance.ps1 -Step Propose -Table cfg_setting -Op update `
    -Where '{"key":"passage.review_over"}' -Set '{"value":"12"}' `
    -Question "Raise passage.review_over from 10 to 12 — fewer long passages flagged needs_review."
#   PAUSED, run_id printed
iba\app\ps\Escalation.ps1 -Action AnswerRun -RunId <run_id> -Decision Approve
iba\app\ps\Config-Maintenance.ps1 -Step Propose -RunId <run_id> -Table cfg_setting -Op update `
    -Where '{"key":"passage.review_over"}' -Set '{"value":"12"}'
#   applied

iba\app\ps\Config-Maintenance.ps1 -Step Report
#   regenerates iba/app/config/CONFIG-REPORT.md — every cfg_* table, current, human-readable
```

`-Op insert|update|delete` on any `cfg_*` table. Coherence-checked before you ever see it (unknown
table/column, bad enum, invalid JSON, a new `cfg_setting` missing its `module`); only **Approve**
commits the write, logged row-by-row in `cfg_change_detail`. Full mechanism: `GOVERNANCE.md` §3A/§9A.

---

## 10. Candidate curation — correcting and adding to `candidate_seed` — RETIRED, corrected 2026-07-30

**This work package is retired and must not be run.** `Candidate-Curate.ps1`'s work package
(`candidate-curation`) is `inactive=1` — retired alongside the rest of the candidate system
(`GOVERNANCE.md` §15D, 2026-07-23; `candidate_seed`/`span_candidate` themselves kept in the DB for
provenance, nothing writes to them or reads them for any live workflow, same as §8's passage
tables). This section previously showed it as the live way to correct/add candidate rows — stale
since 2026-07-23, found and corrected in the same 2026-07-30 pass that added §3a/§11a/§12c. The
commands below are kept as a record of what this utility did; running any of them is now refused by
the dispatcher (`cfg_work_package.inactive`).

`candidate_seed` (the base-layer candidate assessment) is a **data** table, not a `cfg_*` one, so
`Config-Maintenance.ps1` can't touch it — it had its own utility, `Candidate-Curate.ps1`, in two
modes.

### 10a. `-Mode Curate` (default) — correct/split/delete ONE existing row

```powershell
# correct a wrong tag:
iba\app\ps\Candidate-Curate.ps1 -LemmaKey H8085 -Field tag -Value "hearing" `
    -Question "Replace the raw dual-gloss 'to hear: hear' with a clean IB label."
#   PAUSED, run_id printed
iba\app\ps\Escalation.ps1 -Action AnswerRun -RunId <run_id> -Decision Approve
iba\app\ps\Candidate-Curate.ps1 -RunId <run_id> -LemmaKey H8085 -Field tag -Value "hearing"
#   applied

# reject a lemma (soft, reversible):
iba\app\ps\Candidate-Curate.ps1 -LemmaKey H2000 -Field decision -Value rejected -Question "..."

# split a base lemma into a per-sub-strong concept row:
iba\app\ps\Candidate-Curate.ps1 -LemmaKey H0639 -StrongVariant H0639G -Field split -Value "anger" `
    -Question "H0639 covers face/nose/anger across sub-strongs -- split H0639G off as 'anger'."

# remove an invalid row entirely (soft-delete):
iba\app\ps\Candidate-Curate.ps1 -LemmaKey G0112 -Field delete -Question "No tag, no registry_match."
```

`-Field` is `tag | decision | split | delete`. `-StrongVariant` targets a specific sub-lettered
strong (omit to target the base row); **required** for `split`. Single-row, approval-gated, same
shape as `Config-Maintenance.ps1 -Step Propose`. `Field=tag|decision|delete` needs the row to
already exist; adding a brand-new candidate LEMMA (not in `candidate_seed` at all) is still the
`cfg_candidate_rule` `accept` route via `Config-Maintenance.ps1` + a `Set-Candidates.ps1` re-run.
Full method: `iba/docs/iba-candidate-seed-curation-method-v1-20260721.md`.

### 10b. `-Mode Load` (added 2026-07-22) — batch add from a JSON file, no approval gate on clean items

The bulk, JSON-driven counterpart. You supply plain **English words**, not Strong's codes — the
tool derives the lemma/Strong's itself:

```powershell
iba\app\ps\Candidate-Curate.ps1 -Mode Load -InputFile iba\app\config\my-batch.json
```

where the file is:

```json
{
  "items": [
    { "word": "hearing", "reason": "gap scan 2026-07-22 — H8085 shama covers both senses" },
    { "word": "joy/gladness", "reason": "split on delimiter into two attempts" }
  ]
}
```

- A **clean, genuinely new** word **auto-loads immediately — no approval pause.** (This is the one
  place in the app that behaves like `candidate.seed`'s bulk net-matching, not like the
  approval-gated pattern everywhere else — a deliberate choice for a batch tool, not an oversight.)
- A **duplicate** (already an active `candidate_seed` row) is skipped **untouched** — nothing
  written, nothing changed on the existing row.
- Anything else (special characters, a sentence, a bare transliteration, no lemma/Strong's match,
  or a mismatch against STEP's own gloss) is written as an inspectable
  `candidate_seed` row with `decision='exception'` — query it directly, or read
  `iba/app/reports/candidate-load.md`.
- A word containing `:` or `/` is split into separate concepts up front (each tried independently,
  each its own row via the new `sense_seq` column if it doesn't map to a distinct sub-strong).
- **Omit `-InputFile`** (or pass an empty `items` list) to just **revalidate the whole existing
  seed** — no new items, re-derives `step_status`/`ib_referent_type` for every row and re-flags any
  now-broken tag.
- **One escalation for the whole run**, only if unresolved `decision='exception'` rows remain
  afterward:
  ```powershell
  iba\app\ps\Escalation.ps1 -Action AnswerRun -RunId <run_id> -Decision Approve
  #   acknowledges the exceptions as a known worklist; it does NOT fix them — that's still 10a.
  ```

Full design: the plan approved 2026-07-22 (`melodic-foraging-bunny`); build + a real incident
(and its fix) found while testing this same feature: `GOVERNANCE.md` §12.

---

## 11. Standalone quality checks

Read-only pictures of data health, run **whenever you want them** — not tied to any build step:

```powershell
iba\app\ps\Passage-Quality.ps1                 # corpus-wide raw distribution
iba\app\ps\Passage-Quality.ps1 -Book Dan       # book-scoped: sanity-check that book's debate-range
                                                # sizes (§12b) instead — added 2026-07-28
#   -> iba/app/reports/passage-quality.md — verse-count distribution
```

Escalates (one run, one escalation, counts + samples) if it finds anything — acknowledging the
escalation (`Escalation.ps1 -Action AnswerRun ... -Decision Approve`) confirms you've seen the
picture; it doesn't fix anything.

**`Candidate-Quality.ps1` is retired**, corrected here 2026-07-30 — this section used to list it
alongside `Passage-Quality.ps1` as a normal, currently-usable command. Its work package
(`candidate-quality`) is `inactive=1` (retired with the rest of the candidate system, §8) — running
it is now refused outright by the dispatcher (`cfg_work_package.inactive`), not just pointless.

---

## 11a. The lexicon-parsed layer (`Lexicon-Parse.ps1`)

Not read-only like the checks above — `-Step Parse`/`-Step Related` actually write. Three
independent steps (run whichever you need, not a fixed pipeline):

```powershell
iba\app\ps\Lexicon-Parse.ps1 -Step Parse      # strong_meaning_tree/strong_lexicon -> the 3 parsed
                                               # tables. No network, deterministic, clears+rebuilds,
                                               # safe to re-run any time.
iba\app\ps\Lexicon-Parse.ps1 -Step Related    # strong -> strong_related, one live STEP getInfo
                                               # call per row. Can take a couple of minutes over the
                                               # full strong table.
iba\app\ps\Lexicon-Parse.ps1 -Step Validate   # read-only coverage + value-quality check across all
                                               # 4 tables -> iba/app/reports/lexicon-parse.md;
                                               # escalates once if it finds anything, same shape as
                                               # §11's checks.
```

**You will rarely need to run `Parse`/`Related` by hand.** `Raw-Backfill.ps1` (§3a) and
`New-Word.ps1`'s own raw-detail step both rebuild this layer automatically for whatever strongs
they just pulled — this script exists for a manual full rebuild/check, not as a required step in
the everyday flow.

---

## 12. Reports and raw CSV export

```powershell
iba\app\ps\Reports.ps1 -Step ReportWord -Word hypocrisy          # word-raw report (§6)
iba\app\ps\Reports.ps1 -Step ValidationWord -Word hypocrisy      # raw-layer validation report
iba\app\ps\Reports.ps1 -Step ValidationBook -Book Gen            # base-layer validation report

iba\app\ps\Export-Tables.ps1                                     # every DATA table -> iba/app/export/*.csv
iba\app\ps\Export-Tables.ps1 -Table candidate_seed,run           # just these tables
iba\app\ps\Export-Tables.ps1 -Out some\other\dir
```

`Export-Tables.ps1` (now the registered `table-export`/`table.export` step) dumps tables
**verbatim** — no report narrative, no interpretation — for direct review in a spreadsheet, or as a
point-in-time reference (this is exactly how a same-morning `candidate_seed.csv` export made a real
recovery possible on 2026-07-22 — see `GOVERNANCE.md` §12). It excludes `cfg_*` tables —
`Config-Maintenance.ps1 -Step Report` (§9) is the dedicated config snapshot/export.

**Every report now auto-archives and CSV-pairs by default (added 2026-07-22/23).** Every report in
this guide (§6, this section, §11, §13, §12a below) — when it regenerates — first copies its
*previous* version into an `archive/` subfolder beside it (timestamped), so a run never silently
overwrites the last snapshot; and it writes a matching CSV of its underlying table(s) into an
`export/` subfolder (git-ignored), so you get both the narrative analysis and the raw rows on every
run, no extra command needed. `schema-overview` (§12a) is the one exception — it already *is* the
schema, a CSV of it would just repeat the same information.

---

## 12a. The 4 analysis reports (added 2026-07-22/23; registry report added 2026-07-23; was 5, corrected 2026-07-30)

Read-only, run whenever you want them — same standalone shape as the quality checks (§11), each its
own work package. **`SeedCandidate-Report.ps1` is retired** (`seed-candidate-report` work package,
`inactive=1`) — it reports on `candidate_seed`, itself retired data (§10); running it is now refused
by the dispatcher. The remaining 4:

```powershell
iba\app\ps\StrongMeaning-Report.ps1
#   -> iba/app/reports/strong-meaning.md — meaning-parse coverage: strong rows with no strong_sense
#      yet, sense-count distribution, lsj/mounce lexicon completeness

iba\app\ps\SpanAnalysis-Report.ps1
#   -> iba/app/reports/span-analysis.md — span coverage per book, confirmed vs candidate span
#      counts, morph-code distribution

iba\app\ps\SchemaOverview-Report.ps1
#   -> iba/app/reports/schema-overview.md — every data table: columns, types, PK/FK, indexes, row
#      counts, introspected live (no CSV pairing — see above)

iba\app\ps\Registry-Report.ps1
#   -> iba/app/reports/registry.md — evaluate/review word_registry: summary (by status/source),
#      joined to strong via word_strong, and a sense report grouping registry words by the
#      gloss/broad meaning their strong carries
```

Full design + content rationale (first 4): `PLAN-reports-config-governance-v1-20260722.md` §3.1–3.4;
build account: `GOVERNANCE.md` §14. Registry report: escalation #272, `GOVERNANCE.md` §15A.

---

## 12b. Verse-analysis: lexical, then the debate pipeline (rewritten 2026-08-07 — supersedes the scaffold-based version of this section)

**This section replaces the scaffold-based workflow entirely.** The old two steps documented here
(`VerseSpanMeaning-Report.ps1` → `PassageDebate-Report.ps1`, added 2026-07-26/27) are both fully
retired — `report.verse_span_meaning` since `BUILD.md` §56-59 (2026-08-05, superseded by
`report.verse_lexical`/`lexical.build`), `report.passage_debate`/`Chapter-Generate.ps1`/
`passage-debate-sync` since 2026-08-07 (superseded by the DB-first `hib`/`phenomenon`/`operation`/
`closing` model, which is what the real Dan 8 debate actually used — `BUILD.md` §61-71). Leaving
both routes live side by side was a confirmed, live-hit source of confusion (a half-migrated
pipeline pointing at itself) — this rewrite is the fix, not a parallel option.

**The real pipeline, two separate tools:**

1. **The lexical** (`lexical.build`/`report.verse_lexical`, `VerseLexical.ps1`) — mechanical,
   deterministic, no analytical judgement. Book-scoped, run once ahead of time — independent of
   how many small debate chapters follow, since a debate is always chapter/range-scoped while the
   lexical is naturally a whole-book pass.
2. **The debate** (`Debate-Run.ps1`) — the single entry point for everything from HIB
   identification through the rendered report, for one chapter/range at a time.

### Step 1 — build the lexical for the whole book (once, ahead of time)

```powershell
iba\app\ps\VerseLexical.ps1 -Book Dan -Chapters 1-12
#   -> iba/app/verse-analysis/Daniel/dan-1-12-verse-lexical-v{n}-{date}.md
# -Range 8:1-27 also works for a sub-chapter slice, but the normal case is the WHOLE book at once.
```

`hib.set` (below) hard-refuses (`lexical-incomplete`) against any verse this hasn't covered yet —
build it first, for the whole book, and you won't hit that per-chapter.

### Step 2 — run the debate, one chapter/range at a time

```powershell
# single chapter
iba\app\ps\Debate-Run.ps1 -Book Dan -Chapters 1 -BookLabel Daniel

# multi-chapter range
iba\app\ps\Debate-Run.ps1 -Book Dan -Chapters 1-3 -BookLabel Daniel

# sub-chapter verse range
iba\app\ps\Debate-Run.ps1 -Book Dan -Range 8:1-27 -BookLabel Daniel

# targeted single-step rerun/correction (mirrors the real Dan 8 rollback/redo, BUILD.md §71)
iba\app\ps\Debate-Run.ps1 -Book Dan -Chapters 1 -BookLabel Daniel -Step hib.set
```

`-BookLabel` (added 2026-08-08, same shape as `VerseLexical.ps1`) defaults to `-Book` if omitted —
so `-Book Dan` alone files under `iba/app/verse-analysis/Dan/` rather than `Daniel/`. Always pass
both together for a book you already have a labelled folder for.

One call walks the whole sequence (`cfg_setting.passage.debate_run_sequence` — `hib.set` →
`passage.build` → `phenomenon.set` → `operation.set` → `closing.set`), each step still under its
own existing work package. **Per-step separation is unchanged and load-bearing** — each step still
needs its own genuinely-authored analytical content (the digest's "failure modes," `BUILD.md`
§61-71); what's gone is only the need to invoke five separate scripts by hand in a fixed order.

For each step, in order, the script:

1. **Checks if it's already done** for this exact scope (a DB read, mirroring that step's own
   gate) — if so, skips it silently.
2. **Looks for a staging payload** at a predictable path (`cfg_setting.
   passage.debate_staging_path_pattern`: `iba/app/staging/operations/{book}-{scope}-{step}.json`)
   — if present, runs the step with it.
3. **Otherwise stops**, printing the exact path expected. That payload is authored by whoever does
   that step's actual reading (the AI, in-session, from the lexical + prior DB state) — it is
   never something typed by hand at this command line. Once it exists, **rerun the exact same
   command** — readiness is re-derived from the DB and the staging files every time, no `-RunId`
   bookkeeping needed to resume.

Example of a stop, and what happens next:

```text
PS> iba\app\ps\Debate-Run.ps1 -Book Dan -Chapters 1

  hib.set              skip           already satisfied for this scope     <- example only;
                                                                                first run always
                                                                                stops at hib.set

STOPPED -- hib.set needs its analytical payload next.
  Write it to: iba\app\staging\operations\dan-1-hib.set.json
  Then rerun the exact same command -- readiness is re-derived from the DB
  and staging files each time, no run-id bookkeeping needed to resume.
```

Once `closing.set` succeeds, `Debate-Run.ps1` automatically renders the report
(`python -m iba.app.tools.build_debate_report`, standalone — deliberately not a `cfg_report` step,
`BUILD.md` §65) to `iba/app/verse-analysis/<BookLabel or Book>/{book}-{scope}-debate-report.md`
(book-scoped, versioned + archived-on-regenerate — corrected `BUILD.md` §84, 2026-08-08; this used
to land flat in `iba/app/reports/` with a date in the filename instead, a filing bug, not the
intended design). Every `hib.set`/`phenomenon.set`/`operation.set`/`closing.set` step's own
reconciliation report files the same way, same folder.

**Known gap, not yet updated for this model:** `WholeBookRead-Report.ps1`/`report.whole_book_read`
(`BUILD.md` §32) still reads the old scaffold's `debate_status='filled'` .md sections
(Emergent-questions/Passage-level-linkages) — it has not been rebuilt against the new
`passage_emergent_question`/`passage_linkage` DB tables. Still correct for the six pre-existing
scaffold-model books (Amos/Hosea/Joel/Jonah/Micah/Obadiah); not yet exercised against a
`Debate-Run.ps1`-produced book.

**New failure conditions (2026-08-07, `BUILD.md` §79 — full-app schema remediation).** A correction
payload for `hib.set`/`phenomenon.set`/`operation.set` naming an item under `remove` can now stop
with `hib-has-dependent-phenomena` / `phenomenon-has-dependent-operations` /
`operation-has-dependent-linkage` — the removal is refused because live analytical work is already
built on top of it. Not a bug: clear the dependent first (remove the phenomenon/operation/linkage
that depends on it, via that step's own `remove` list), or withdraw the item from `remove` and leave
it in place. A `changed` correction (same label/key, different content) no longer needs this —
corrections update the existing DB row in place now, they never orphan anything downstream.

`operation.set`'s `sources`/`targets` party objects also gained an optional `hib_label` field —
set it when a source/target genuinely IS a HIB already registered via `hib.set` (structurally links
`operation_party.hib_id`, not just the free-text `detail` gloss); omit it for a party that isn't its
own registered HIB. An unresolvable `hib_label` fails the call the same way an unresolvable verse or
HIB label already does.

---

## 12b-ii. Verse-lexical enrichment — Layer 2 judgement (`lexical.enrich`, added 2026-09-04, escalation #1383)

**Window 1 only — never determines phenomenon/HIB status.** `lexical.build` (§12b Step 1) is Layer
1: mechanical, no judgement, one row per code. `lexical.enrich` is Layer 2: still Window 1 (never
an inner-being/HIB concept — that stays entirely Window 2's `hib`/`phenomenon`/`operation`), but
judgement-bearing — idiom sense, related-word sorting, pronoun/entity resolution, structural
patterns, genre. Writes `verse_lexical_note` rows plus `passage.genre`/`lexical_complete_at`, one
already-registered **passage-block** (≤20 verses, `cfg_passage.passage.max_verses`) at a time — the
analytical judgement itself is made by the AI/researcher reading pass BEFORE this runs; this step
mechanises turning that already-decided reading into validated, grant-checked rows, the same
"payload in, structured rows out" shape `Debate-Run.ps1`'s own steps already use.

```powershell
# 1. a live passage must already cover the exact range (Build-Passages.ps1 / passage.build,
#    §12b-iii below for how to find/propose one) -- lexical.build must already have run for it.
iba\app\ps\VerseLexical.ps1 -Book Dan -Range 1:1-8 -Step lexical.enrich `
    -PayloadPath iba\app\staging\lexical\dan-1-1-8.json

# 2. the exception report -- what's unresolved/unclassified/checked_empty from that run, a plain
#    symmetric tally, never a "confirms/validates" highlights reel
iba\app\ps\VerseLexical.ps1 -Book Dan -Range 1:1-8 -Step report.lexical_exceptions

# 3. the Phase-2 JSON extract -- feeds Stage 2 input assembly, multi-filter (passage/verse/
#    surface/strong), never an unbounded full-corpus dump
iba\app\ps\VerseLexical.ps1 -Step report.lexical_extract -VerseFilter "Gal.5.16-Gal.5.17"
```

Payload shape (`notes`/`remove`, keyed by `verse`+`position`+`code_ordinal` — the `position`/
`code_ordinal` verse_lexical columns, not a free-text reference): each note carries `note_type`
(`idiom`/`pronoun_resolution`/`noun_relational`/`noun_severity`/`chain`/`connective`/
`related_word`/`polarity`/`entity_link`/`inert`/`structural_pattern`/`recurrence_role_shift`/
`cross_lemma_shared_gloss`), `resolution_status` (`resolved`/`unresolved`/`unclassified`/
`not_supported_this_language`/`checked_empty`), `finding`/`evidence` text, and — for
`pronoun_resolution`/`entity_link`/`recurrence_role_shift` — an optional `target_verse`+
`target_position` (may point at ANY verse in the currently-loaded passage-block, not just the same
verse); `structural_pattern`/`recurrence_role_shift` instead take `related_codes` (a list of
`{verse, position}`, ≥2 entries). A `changed` note (same verse_lexical_id+note_type, different
content) needs a `reconciliation_note`; every pre-existing note for the block must be repeated or
listed under `remove` with a `reason` — an unaddressed one is a hard stop (`unreconciled`), not a
silent drop. The block is only marked `lexical_complete_at` once every applicable code has ≥1 live
note (a finding, or an explicit `checked_empty`/`not_supported_this_language`/`unresolved`) —
`incomplete-block` otherwise, naming which codes are still missing.

**Mechanical columns, always on `verse_lexical` itself, no payload needed:** `position`/`surface`/
`language`/`testament`/`is_negator`/`narrative_morph`/`gloss_consistent_in_verse`/`party_kind` are
all computed by `lexical.build` (Layer 1) for every code, unconditionally — the negator/connective/
divine-name lexicon they read from is `cfg_lexical_code_class` (grown via `configmaint.propose`,
same as every other `cfg_*` table; currently seeded: 7 negator codes, 6 connective codes across 3
classes, 7 divine-name codes — `party_human`/`party_angelic` are not yet seeded, so
`party_kind='human'`/`'non_human'` never fires until they are).

## 12b-iii. Proposing the next passage boundary (`-Suggest`, `Build-Passages.ps1`, added 2026-09-04, escalation #1383)

`passage.build` (§12b, Step 2's own prerequisite) still requires an explicit `-Chapters`/`-Range` —
`-Suggest` is an optional first move that proposes one, from cheap mechanical proxy signals only
(narrative_morph density, the legacy book-level genre tag, a chapter-boundary stop) — **explicitly
NOT the real genre determination**, which still happens as `lexical.enrich`'s own first move once
the passage is confirmed:

```powershell
# propose only -- no table write, pauses (exit 2) for you to confirm or adjust
iba\app\ps\Build-Passages.ps1 -Book Gal -Suggest

# accept the suggestion verbatim, straight into passage.build (still needs its own payload)
iba\app\ps\Build-Passages.ps1 -Book Gal -Suggest -Confirm -PayloadPath iba\app\staging\passages\gal-next.json

# or ignore the suggestion and register your own scope, exactly as before
iba\app\ps\Build-Passages.ps1 -Book Gal -Range 5:16-17 -PayloadPath iba\app\staging\passages\gal-5.json
```

**Known dependency, not yet resolved (flagged live building this, not silently worked around):**
`passage.build` itself still refuses (`no-hibs`) any scope with no `verse_hib` data — i.e. `hib.set`
(Window 2, Debate-Run.ps1 Step 1) must already have run for that scope. `-Suggest` proposes a
range on Window-1-only signals, but confirming it still hits that same Window-2 gate underneath —
a real, currently-live coupling between the two windows this build did not attempt to redesign
(out of scope; `passage.build`'s own gate is Window 2 debate-pipeline code).

---

## 12c. Inner-being narrative — structural check (`BookNarrative-Validate.ps1`, added 2026-07-30)

Narrative writing itself is unmechanised analytical work (no pipeline produces it) — this is a
read-only check you run **on a finished narrative file**, before treating it as done. Confirms a
`## Scope self-check` section exists and cites all three required channels (non-human↔human,
human↔human, physical world↔human — see `WA-inner-being-narrative-guidance-v1-2026-07-28.md` §4)
with non-empty content. A presence check only — it does not judge whether the narrative's content or
citations are actually good.

```powershell
iba\app\ps\BookNarrative-Validate.ps1 -Path iba\app\verse-analysis\Daniel\WA-dan-inner-being-narrative-v3-consolidated-2026-07-28.md
#   -> iba/app/reports/book-narrative-scope-check.md
```

Fails (`scope-check-missing`/`scope-check-incomplete`) if the section is absent or any channel is
missing/empty — the message names exactly which.

---

## 12d. Generating the narrative itself (`BookNarrative-Generate.ps1`, added 2026-07-30)

Everything above through §12c gathers material and checks structure; this step is the one that
actually **writes** the narrative, by calling the Anthropic Messages API — the first place in this
app that costs real, pay-as-you-go money rather than running on the Claude Code subscription or a
free local STEP call.

```powershell
iba\app\ps\BookNarrative-Generate.ps1 -Book Dan -BookLabel Daniel
```

Requires at least one filled `report.passage_debate` for the book (§12b) and `ANTHROPIC_API_KEY` in
the environment or the repo-root `.env` (see §1 — the one exception to this app's "no secrets"
rule; the same key `scripts/_run_ve_reads_governed.py` at the repo root already uses). It assembles
every filled debate for the book plus the two governing docs — `method.narrative_hard_constraints_
path` (the book-agnostic hard constraints: nothing invented, open threads stay open, no forced
unity, plain language, no self-reference — generalized from the original Daniel-only brief) and
`method.inner_being_narrative_guidance_path` (the three-channel requirement + the `## Scope
self-check` section, §12c) — resolves both live from `cfg_setting`, not memory, then **estimates**
the token count/cost before ever calling the network.

- Over `narrative.generate_max_cost` (default $3.00): refused outright (`cost-cap-exceeded`) — raise
  the cap deliberately via `configmaint.propose` for a book large enough to need it, don't just
  re-run.
- Under the cap: **pauses** (`needs-approval`) with the exact estimate in the question — same
  approval shape as `configmaint.propose` (a spend/design decision, not a standard routine —
  `registry.create` no longer has an approval shape at all, `BUILD.md` §153), nothing spent yet:

  ```powershell
  iba\app\ps\Escalation.ps1 -Action AnswerRun -RunId <run_id> -Decision Approve
  iba\app\ps\BookNarrative-Generate.ps1 -Book Dan -BookLabel Daniel -RunId <run_id>   # resume — makes the live call
  ```

Once approved and resumed, ONE live API call is made, the result is filed under `report.verse_
analysis_output_dir/<BookLabel>/` (`narrative.output_pattern`, archived-on-regenerate like every
other report), and the call's real token/cost (from the API response itself, not the estimate) is
appended to `narrative.usage_log_path` — `scripts/cost_ledger.py` at the repo root only ingests
Console CSV exports, not this app's own calls, so this is the audit trail for those. Run
`BookNarrative-Validate.ps1` (§12c) on the result next.

Every one of these is a `cfg_setting` (module `narrative`), changeable via `configmaint.propose`,
never hard-coded: `narrative.generate_model` (default `claude-sonnet-5`), `narrative.generate_max_
output_tokens`, `narrative.generate_max_cost`, `narrative.rate_input_per_million`/`rate_output_per_
million`, `narrative.output_pattern`, `narrative.usage_log_path`. The `cfg_report` row for
`report.book_narrative_generate` governs the title/footer the same way every other report's does.

**What this doesn't do.** The actual writing is still not mechanized by this app's own code — the
model does the writing, working strictly from the assembled package; this step's job is making sure
that package is complete and consistent every time, not judging what the narrative should say.

**Proven live** on Daniel ($1.19, 328,276 in / 13,711 out tokens) and Joel ($0.35, 86,420 in / 5,740
out tokens), both 2026-07-30 — both passed `report.book_narrative_validate` clean.

**Flagged, not built: a cross-book mechanism.** A single book's narrative holds together on its own,
but nothing yet pulls information ACROSS books — recurring or varying themes and focal points. The
researcher is confident this can be drawn from the same debate corpus this step already reads, but
the shape of that data is not yet decided — nothing here should be read as a design for it. See
`BUILD.md` §52's closing note when that direction is given.

---

## 12e. Word-registry Strong's/span analysis (`WordRegistrySpan-Report.ps1`, added 2026-08-09, clustered by meaning + English-gloss index later the same day)

For one `word_registry` word: every linked Strong's, grouped into **meaning clusters** — same-root
word families (noun/verb/adjective forms of one lemma, e.g. G1167 "timidity" / G1168 "be timid" /
G1169 "timid") clustered together via `strong_related` (STEP's own root-family data), not listed
flat by Strong's number. Each cluster shows its member Strong's (gloss/transliteration/count), its
full parse-meaning breakdown, and its **unique surface-span applications** — the different ways
that Strong's actually shows up in the text (e.g. G5399 realised as "afraid"/"fear"/"feared"/
"awe"/"terrified"/… — 13 distinct surface forms), each with an occurrence count and one example
verse reference + text.

**The report body opens with a working table of contents**, one link per meaning cluster (heading
led by the shared meaning, e.g. "timidity, be timid, timid — G1167, G1168, G1169" — not by Strong's
number). Links are real `<a id>` anchors, not left to the viewer's own auto-generated heading ids
(that was a real bug, found and fixed app-wide the same day — every registered report's ToC now
works the same way; see `GOVERNANCE.md` §38 if curious). **The ToC additionally groups clusters
a second way**, by shared English gloss word — e.g. all 8 of `fear`'s distinct root-clusters that
happen to gloss as "fear" (φόβος, πτόησις, יָרֵא, …) are shown together under one **fear** heading
in the ToC, even though they're separate, unrelated root families; a shared row there does **not**
imply a shared root — it's a browsing aid only, clearly labelled as such, and the actual root
relationship (or lack of one) is always shown in the section itself.

```powershell
iba\app\ps\WordRegistrySpan-Report.ps1 -Word fear
#   -> iba/app/verse-analysis/word_registry/fear-strong-span-v4-20260809.md
#      (62 Strong's -> 33 meaning clusters for 'fear'; ToC additionally index-groups them by
#       shared English gloss word — 8 "fear" variants, 3 "trembling"/2 "tremble", 2 "devout",
#       2 "terror" — each still linking to its own root-based section)
```

Read-only, run whenever you want it. `-Word` must match a `word_registry.word` value (case-
insensitive) — an unrecognised word fails cleanly (`report-stop`, exit 3), it does not silently
produce an empty report. Output is dated/versioned (`fear-strong-span-v1-...`, `-v2-...` on a
same-day re-run) with prior versions auto-archived, same convention every other registered report
uses. Design/build record: `GOVERNANCE.md` §36/§37/§38, `BUILD.md` §85/§86/§87.

---

## 12f. On-demand verse restatement, by ONE Strong's reference (`StrongVerse-Report.ps1`, added 2026-08-10)

`§12e` shows every Strong's linked to a word, one example verse each. This is the other direction:
pick ONE Strong's code and see **every verse it occurs in** (whole Bible), each verse's text left
intact except that one occurrence, annotated inline with its exact parse-meaning senses. Built to
answer "what does this specific Strong's actually look like across every verse it's in" — scoping
to a single code (not a whole registry word's full verse set, which can run into the thousands,
see `verse-lexical-by-registry-20260810.md`) is what keeps this readable in one file.

```powershell
iba\app\ps\StrongVerse-Report.ps1 -Word blessing -Strong G2127
#   -> iba/app/verse-analysis/word_registry/blessing/blessing-G2127-verse-lexical-v1-{date}.md
```

`-Word` is both the filing folder and a validation check — the given `-Strong` must actually be
linked to that word (`word_strong`); an unrecognised word or an unlinked Strong's both fail
cleanly (`report-stop`, exit 3), never a silent empty/wrong report. Read-only, run whenever you
want it, no `verse_lexical.build` prerequisite beyond whatever's already been built for the books
that Strong's occurs in.

**What each verse shows:** the verse text, unchanged, with the matched span's surface text
annotated `**surface** [strong: senses]` — senses are **exact `strong_variant` matches only**, no
sibling/base-lemma fallback (unlike `§12e`, which does fall back — this report's whole reason to
exist is per-span exactness). Two data shapes get explicit handling rather than being smoothed
over:

- **Combined-tag spans** — STEP sometimes tags two Strong's codes on one rendering unit (e.g. the
  Greek conjunction "and" fused onto the following verb). Labelled `{strong}+{other code}
  combined tag` in the annotation, not presented as a pure single-code occurrence.
- **Empty-surface spans** — the other half of a combined tag can carry no independent English
  surface text at all. Rendered as a structured aside under the verse rather than forced into the
  running text.

A surface that doesn't match its own verse's text **exactly once** (a real bug found building
this — see `g2127-verse-lexical-by-strong-sample-20260810.md`: `"bless"` is a literal substring of
`"blessing"`, a DIFFERENT span in the same verse) is flagged `UNRESOLVED` rather than guessed —
word-boundary matching (`\bsurface\b`) resolves the ordinary case; anything that still doesn't
resolve to exactly one match is surfaced, never silently dropped.

Preview/build record: `iba/app/reports/g2128-verse-lexical-by-strong-sample-20260810.md` (first
test, 8 verses) and `g2127-verse-lexical-by-strong-sample-20260810.md` (second test, 40 verses —
found and fixed the substring-collision bug and the combined-tag/empty-surface cases above);
`BUILD.md` §91.

---

## 12g. Cluster taxonomy + assignment (`Cluster-Report.ps1` / `Cluster-Assign.ps1`, built 2026-08-11/12, documented 2026-08-13 — was missing from this guide entirely)

Two tools, read-only + mutating, same split as `Config-Maintenance.ps1`'s `Validate`/`Propose`:

```powershell
iba\app\ps\Cluster-Report.ps1
#   -> iba/app/reports/cluster.md — the cluster taxonomy (all 50 codes: FLAG, M01-M47 incl. M10b/
#      M10c/M32, T2, T3), word-origin strong-assignment coverage + gap list, and — every origin,
#      not just word — per-cluster strong/span/lexical/verse counts with the top stem-grouped
#      meanings per cluster, plus a "backfill vocabulary outside the taxonomy" section (typed:
#      proper nouns / grammatical markers / closed-class / real candidate vocabulary, the last
#      cross-matched against every cluster's own gloss and stem-grouped). Every per-cluster table
#      sorts by `cluster_code`, not count (2026-08-13 — findability over ranking). Read-only, run
#      whenever you want it.

iba\app\ps\Cluster-Assign.ps1 -Step Validate
#   read-only coverage/exception check — same escalate-once-then-pause shape as every other
#   -Step Validate in this guide. Answer with Escalation.ps1 -Action AnswerRun, then re-run
#   -Step Validate with the same -RunId to act on the answer.

iba\app\ps\Cluster-Assign.ps1 -Step Assign
#   DB-wide sweep: lib.strongreconcile.reconcile() against every strong row — mechanical
#   HIGH-precedent cluster match (exact gloss match only, P1/P2, no researcher decision needed)
#   plus the backfill->word promotion cascade (real STEP fetch + verse_lexical build) wherever a
#   non-T2 classification and a word_registry link both already hold. T2 classifications never
#   promote; T3 promotes with no word link required (by design — T3 "is inherently not word-
#   specific"). Safe to re-run, idempotent.
```

**What `-Step Assign`'s exact-match matcher can't reach, a researcher pass can.** Its P1/P2 rule
is deliberately narrow (exact stepGloss string match only, never substring — avoids the ill/kill,
sin/hissing false-positive class) and found genuinely low recall against the ~9,500-strong
untagged-backfill pool: a live run against that pool classified **zero** new codes. The real
backfill-scope work (typing the pool with `report.cluster`'s backfill section, hand-tagging the
clear T2/T3 cases, then re-running `-Step Assign` to do the actual promotion through this same
registered mechanism) is a manual, judgement-led pass on top of this tool, not something it does
alone — see `iba/app/reports/backfill-scope-triage-20260813.md` for the worked example (1,150
codes hand-classified T3, then 1,000 promoted by re-running `-Step Assign`) and `BUILD.md` §107-111
for the build history.

---

## 13. Log retention (read-only)

```powershell
iba\app\ps\Log-Retention.ps1
#   -> iba/app/reports/log-retention.md
```

Row counts and age for `run`/`escalation`/`validation_result`, every open escalation, recent real
failures, and a "stuck chained runs" section (runs that paused mid-sequence and were never
resumed) listed as archival **candidates** for you to judge — it does not prune or delete anything.

---

## 13a. File manifest — rebuild and search (added 2026-08-15)

Every file in the project tree (not `iba/` only — the whole repo, including every `archive/`
folder), indexed by filename/path metadata: category, type, currency (active/archived/cross-
reference/historical/backup/other), and any date/registry-number/version/cluster-code/word the
filename itself carries. **Filename/path metadata only — this does not read file contents.**
Replaces the old standalone `scripts/build_file_manifest.py` → `database/file_manifest.json`
(that script's logic now lives here, governed, instead of running unregistered and separately).

```powershell
iba\app\ps\Manifest-Rebuild.ps1
#   -> iba/app/reports/file-manifest.md  (counts by category, by currency)

iba\app\ps\Manifest-Search.ps1 -Query "type:iba-verse-analysis"
iba\app\ps\Manifest-Search.ps1 -Query "category:archived"
iba\app\ps\Manifest-Search.ps1 -Query "grace"
#   -> iba/app/reports/manifest-search-<query>-<date>.md
```

**Rebuild** (`manifest.rebuild`) is a full rescan — it replaces the `file_manifest` table's
contents each time, so run it again after adding/moving/renaming files before relying on a search.
Only VCS/build/cache machinery is skipped (`manifest.skip_dirs`/`manifest.exclude_exts`, both
`cfg_setting` — everything else, including every `archive/` subfolder anywhere in the tree, is
indexed on principle: archived material is put aside, not dead, and may hold data still needed).

**Search** (`manifest.search`) takes one `-Query`, either a **field query** —

| Field | Example | Matches |
| --- | --- | --- |
| `registry:N` | `registry:68` | exact registry number |
| `type:X` | `type:iba-migration` | file type contains X |
| `category:X` | `category:iba` | category contains X |
| `currency:X` | `currency:archived` | exact currency status |
| `cluster:X` | `cluster:c17` | exact cluster code |
| `word:X` | `word:grace` | exact extracted word |
| `date:X` | `date:2026-08` | date starts with X |
| `archived:true\|false` | `archived:true` | archived flag |
| `ext:X` | `ext:.md` | exact extension |

— or **free text**, matched as a substring against the file's path. Every search's results are
written to a report file (path/category/type/currency for each hit) — this is a read-only query,
nothing in `file_manifest` is changed by a search.

This is the baseline round B (below) cross-checks coverage against — prose itself is out of scope
for both (`prose_section_fts` already covers it).

---

## 13a-ii. `folder_purpose` — what every folder is for, and its status (added 2026-08-28)

One row per folder in the project tree (793 at build time, seeded from a full census) — a reference
table, like `books`, not a `cfg_*` rule table: it states facts about the project's own structure
(what a folder holds, what it's for), maintained directly, not through `Config-Maintenance.ps1
-Step Propose`. Escalation #971.

```powershell
iba\app\ps\FolderPurpose.ps1 -Action Seed
#   full reconciliation against the live tree: new folders added, folders no longer on disk marked
#   status='deleted' (soft, never removed), every row's file-count/extension/mtime columns refreshed

iba\app\ps\FolderPurpose.ps1 -Action CrossCheck
#   re-derives governed_by_setting from live cfg_setting *_dir/*_path values; pre-fills
#   type='operations'/status='authoritative' wherever a setting already makes that unambiguous;
#   reports anomalies (a folder in active system use with no governing cfg_setting, or vice versa)

iba\app\ps\FolderPurpose.ps1 -Action AutoAssess
#   fills type/status for every row still missing either, from Seed/CrossCheck's own gathered
#   facts (never guesses 'mixed'/'reallocate', or a type for a category-less folder -- those need
#   -Action Set by hand). Run after Seed/CrossCheck bring in new folders.

iba\app\ps\FolderPurpose.ps1 -Action Set -FolderPath "outputs/escalation" -Type operations `
    -Status authoritative -UsageDescription "Escalation.ps1's own list/history exports only."
#   the ONLY sanctioned way to hand-set Type/Status/UsageDescription — Seed/CrossCheck own every
#   other column and would overwrite a hand edit there on the next run anyway

iba\app\ps\FolderPurpose.ps1 -Action List -Status mixed
iba\app\ps\FolderPurpose.ps1 -Action Show -FolderPath "docs"
```

`-Type`: `archive` \| `operations` \| `results`. `-Status`: `authoritative` \| `mixed` \|
`reallocate` \| `stale` \| `deleted` (set automatically by `Seed` when a folder disappears from
disk). Run `-Action Seed` after any large-scale reorganisation, before `Manifest-Rebuild.ps1` — the
manifest's own classification (`file_manifest.category`/`currency`) reads `folder_purpose`'s
`manifest_category`/`manifest_currency` first, falling back to its own hardcoded rules only for a
folder not yet registered here.

---

## 13a-iii. Path audit — hardcoded location literals in scripts (added 2026-08-28)

Project-wide scan for a folder/file-path string literal hardcoded in a script instead of read from
`cfg_setting`/`cfg.module_setting()`. Escalation #971/#976, the automated successor to the one-off
manual sweep (escalation #648) for the location subset specifically.

```powershell
iba\app\ps\PathAudit.ps1 -Action Scan
#   -> outputs/configs/path-audit.md
```

Every `.py` file project-wide is scanned **except** one whose `cfg_utility` row is `inactive=1` (a
file with no `cfg_utility` row at all IS included — not being registered is a separate finding of
its own, `configmaint.validate`'s `unregistered_project_scripts`). `iba/app/migration/` is excluded
entirely — a migration script's job is writing a literal path *into* a config row as a one-time
seed, not a violation. ADVISORY — every finding needs a look (a real gap, or a previously-reviewed
deliberate hardcode like `prosestore.py`'s output-path constants), not an auto-fix. Full method and
known false-positive classes: `lib/pathaudit.py`'s own docstring.

---

## 13b. Content-index — search what's actually WRITTEN inside `.md` files (added 2026-08-17)

Round 2 of the manifest + content-search plan (governance-alignment register item #6). A
**predefined-key concordance** — not free-text search — over every `.md` file `file_manifest`
knows about: for each hit, which file, which line, and the line's own text. Three key types,
sourced live from `iba.db` (`strong`, `word_registry`), not cached separately:

| Key type | Source | Example |
| --- | --- | --- |
| `strong` | `strong.strongNumber` (15,293 rows) | `strong:H2734` |
| `gloss` | `strong.stepGloss` (9,165 distinct values) | `gloss:compassion` |
| `word` | `word_registry.word` (180 rows) | `word:anger` |

```powershell
iba\app\ps\ContentIndex-SizeProfile.ps1
#   -> iba/app/reports/content-index-size-profile.md — every .md file, largest first (file, folder,
#      size). Run this FIRST if you haven't reviewed exclusions yet (see below).

iba\app\ps\ContentIndex-Rebuild.ps1
#   -> iba/app/reports/content-index-rebuild.md — full rescan, clears and rebuilds from scratch.

iba\app\ps\ContentIndex-Search.ps1 -Query "strong:H2734"
iba\app\ps\ContentIndex-Search.ps1 -Query "gloss:compassion" -Csv
#   -> refreshes the index incrementally first (only .md files changed since last pass), then
#      queries, then writes results (type/key/file/line/category/snippet) as a one-off .md report
#      (capped at 500 rows for readability). Add -Csv for the FULL result set as a .csv (added
#      2026-08-17) — a common gloss/word query (e.g. gloss:compassion, 23,098+ hits) needs the
#      untruncated set for real spreadsheet review, not a terminal glance.
```

**`cfg_content_index_exclude` — "include all `.md` except"** (`Config-Maintenance.ps1 -Step
Propose -Table cfg_content_index_exclude -Op insert -Where '{}' -Set
'{"pattern":"...","reason":"...","added_at":"..."}'`). A path or folder-prefix per row; an empty
table excludes nothing. **Why this exists, found live 2026-08-17**: some generated dumps — large
per-book verse-analysis files, a couple of prose extracts — are dense with the exact biblical
vocabulary being indexed (the project's own analysis prose, naturally saturated with its own
subject matter). One file alone produced ~597,000 hits. Run `ContentIndex-SizeProfile.ps1` first
and decide exclusions from real data, not a guess — 74 of 7,874 `.md` files (≥1MB each) hold 270 of
558 total MB, almost entirely `iba/app/verse-analysis/**` plus a few `Workflow/Programme/
programme_prose/` extracts.

**Single-word gloss matches are excluded via a stopword list** (`contentindex._STOPWORDS`, ~100
common English function words) — `strong.stepGloss` genuinely carries entries like `"and"`/`"not"`/
`"this"` (real Hebrew/Greek conjunction/particle glosses), which as SEARCH KEYS would match nearly
every line in the project. Multi-word gloss phrases are unaffected — already specific enough.

**Matching is tokenize + n-gram + set lookup, deliberately not a regex alternation** — tested live
before building this: compiling one `re` pattern over the ~9,300 gloss+word keys hung outright.
Each line is tokenized once, then checked as 1–6-word windows (6 = the longest gloss, measured
live) against a lowercased key set — O(line length), independent of key count.

---

## 13c. Operational-behaviour rules — chat/terminal/sqlite/documentation/llm_output/development (built 2026-08-18, escalations #715/#732/#733; guide coverage added the same day it was found missing)

Project-wide (not `iba/app/**` only) discipline for *how work itself gets done*, as opposed to the
analytical `cfg_method_rule`/`cfg_quality_check` layer (§ elsewhere) which governs *what a passage
read finds*. Six classes, each with its own rule set — `cfg_behaviour_class` +
`cfg_behaviour_rule`, anchored by `governance.operational_behaviour_control`:

| Class | What it governs |
| --- | --- |
| `chat` | The interaction protocol with the researcher — confirm before non-trivial work, output to a file not chat alone, no guessing, cost awareness, AskUserQuestion banned |
| `terminal` | Command/script execution discipline — a step isn't done until its output is validated, git commit+push as one unit, diagnose a reported error rather than route around it |
| `sqlite` | Database-interaction discipline — verify live state, read-only by default, never write via an ad-hoc tool, writes must be replayable |
| `documentation` | Single-authority referencing — pointer not copy, a consolidation doc is only as good as its live enforcement, no hedging in a "complete" record |
| `llm_output` | Epistemic trust in generated content — inferential vs confirmed labelling, no unsubstantiated superlatives, cost-cap-before-call, never expose the API key |
| `development` | Engineering discipline for the work itself — root fix not one-off, simple steps not engineered designs, every interactive module needs a supporting PS script, every open item routes through escalation |

```powershell
iba\app\ps\Behaviour.ps1 -Action List
iba\app\ps\Behaviour.ps1 -Action List -Class chat
#   -> iba/app/reports/behaviour-rules-list.md
```

Content is written only by the one-off `bootstrap_behaviour_rules_*` migration scripts
(`iba/app/migration/`), never by `Behaviour.ps1` itself — it is a read-only query/report tool, the
same shape as `Escalation.ps1 -Action List`. **Not yet built:** a deviation-monitoring mechanism —
every rule currently states `enforced_by: not yet mechanically checked`; each rule is a declared
standard, not (yet) an automatically-checked one.

---

## 13d. Prose module (added 2026-08-24, escalation #829; `SetStatus` added 2026-08-27, escalation #920)

`Prose.ps1` — the DB-canonical prose store (`prose_section`/`prose_section_type`,
`bible_research.db`), 8 dispatcher steps, `kind='utility'`:

```powershell
iba\app\ps\Prose.ps1 -Step Extract -Book Programme [-AlsoMarkdown] [-AlsoDocx] [-IncludeBody]
iba\app\ps\Prose.ps1 -Step Search -Query "grace" [-Book Programme] [-Limit 50] [-Fts]
iba\app\ps\Prose.ps1 -Step ExportChapter -Book "Detail design" -Chapter 1
iba\app\ps\Prose.ps1 -Step ImportChapter -InputFile outputs\markdown\prose-edits\<edited-file>.md
iba\app\ps\Prose.ps1 -Step Flag -FlagCode "Terminology change" -Description "..."
iba\app\ps\Prose.ps1 -Step FlagFixPropose -FlagCode "Terminology change" -Find "old text" -Replace "new text"
iba\app\ps\Prose.ps1 -Step FlagFixApply -ProposalFile <report from FlagFixPropose>.json -SectionIds 12,47 -FlagCode "Terminology change"
iba\app\ps\Prose.ps1 -Step SetStatus -SectionIds 22 -Status approved
```

**`SetStatus`** — set or reset a section's own `status` (`draft` / `in_review` / `approved` /
`archived`, `cfg_enum prose_section_status`) directly, with no body change: the reviewer's "I've
read this" (or "reopen this") action, distinct from an `ImportChapter` content edit. `-SectionIds`
takes one or more comma-separated ids; a section already at the requested status is skipped as a
no-op, and an unrecognised `-Status` is refused against the live enum before a patch is even
written. Like `ExportChapter`/`ImportChapter`/`FlagFixPropose`/`FlagFixApply`, it writes no DB row
itself — it generates a `PROSE` patch (`prose_section`/`set_status`), applied the same way as
every other prose patch, via `scripts/apply_session_patch.py`. Added to close escalation #920: the
chapter-level review status previously tracked in `cfg_prose_chapter` (a `cfg_*`/`iba.db` table)
was workflow data about content, not a rule, and needed the full `Config-Maintenance.ps1 -Step
Propose` approval cycle for what is an ordinary content edit — `cfg_prose_chapter` is now removed
entirely (`iba/app/migration/retire_cfg_prose_chapter_v1_20260827.py`); `prose_section.status`,
set per section via this step and rolled up per chapter through `prose_section_type.chapter_no`,
is the live equivalent.

**The 4 live books:** `Programme` / `Detail design` / `Findings` / `Essays` — a 5th, `Concordance`,
is not yet built (out of scope, `iba/docs/prose-management-iba-first-layer-proposal-v9-20260824.md`
§7). `cfg_prose`'s `prose.book_stage_map` key validates the `--Book` argument's choice list only —
**D10 RESOLVED (escalation #890, 2026-08-26):** which book a row actually lands in is decided by
`prose_section_type.book_label` directly, always was; a prior claim that the stage-based map itself
misfiled 1 of 949 rows was checked against the real code and found false. See §13e.

**Extract/Search/ExportChapter/ImportChapter are read-only against the DB** — `ImportChapter`
generates a `PROSE` supersede patch file, applied separately via `scripts/apply_session_patch.py`
(never writes the database itself). Every `prose_section`/`prose_section_type` write that patch
script makes is routed through `record_change_log` (escalation #836, `GOVERNANCE.md` §52) — `version`
is a pointer to the log row describing the row's own last change, not an incrementing counter.

**`Flag` is the one step that writes directly** — one `wa_data_quality_flags` row
(`flag_group='PROSE_QUALITY'`), no `prose_section` reference. Deliberate design (escalation #829
§12.2): which prose rows a flag concerns is found by search *when the fix actually runs* (a separate,
not-yet-built "angle b" utility, escalation #835, on-hold until prose editing comes into active use),
not stored and kept in sync from the moment the flag is raised. Live `--FlagCode` values: query
`wa_quality_flag_types WHERE flag_group='PROSE_QUALITY' AND delete_flagged=0` (3 seeded today:
`Terminology change` / `Methodology change` / `Style change`, escalation #833 — more will be added
as real cases come up).

Config: `cfg_prose` (module table, 4 keys — `chapter_names`/`book_stage_map`/
`search_default_limit`/`edit_file_dir`); `cfg_enum` groups
`prose_section_status`/`prose_section_author`/`prose_section_type_source_stage`/
`prose_section_type_lifecycle_tag`/`prose_section_type_book_label` (documentation-of-record against
each table's own CHECK constraint, not a runtime lookup — same shape as `record_change_log`'s own 2
enum groups, `GOVERNANCE.md` §52.6); `cfg_write_grant` (`apply_session_patch`→`prose_section`/
`prose_section_type`, `prose_flag`→`wa_data_quality_flags`, all `database='bible_research'`).

Full design record: `iba/docs/prose-management-iba-first-layer-proposal-v9-20260824.md`. Build
record: `BUILD.md` §177.

## 13e. Prose add/edit operational rules (added 2026-08-26, escalation #890)

Builds on §13d — the storage/dispatcher layer there is unchanged; this adds the operational rules
around creating and editing prose, and the flag-fix "angle b" workflow.

**New `prose_section_type` rows are researcher-gated, not code-gated.** Discipline rule
(`cfg_behaviour_rule` `prose-section-type-creation-requires-researcher-instruction`, not
mechanically enforced): a new type may only be inserted on your explicit instruction — it's
controlled vocabulary, the same standard already applied to `cfg_enum`.

**`ImportChapter` now refuses if a section silently vanished from an edit file** — matching
`add`/`move`, which already refused. If you deliberately mean to retire a section, do that
explicitly (`status='archived'`) rather than by deleting its block from an edit file.

**Verse citations — `prose.verse_link`.** `prose_section_verse_link` (new table) records which
verse(s) a section discusses, as an explicit, patch-supplied `verse_reference` string (e.g.
`"Ps 32:1"`, matching how verses are referenced elsewhere in this DB) — not text-mined from body.
No dispatcher step of its own yet (write it via an `apply_session_patch.py` patch,
`table: "prose_section_verse_link", operation: "insert"`, same shape as the pre-existing
finding/dimension link operations).

**Flag-fix, angle (b) — `FlagFixPropose` / `FlagFixApply`.** Once a `PROSE_QUALITY` flag exists
(raised via `-Step Flag`, angle a):

1. `-Step FlagFixPropose -FlagCode <code> -Find <text> -Replace <text>` — searches every active
   section for a literal match, writes a review report (`.json`) listing every hit with its
   proposed replacement. No DB write, no patch yet.
2. Read the report, pick which `prose_section_id`s to actually fix.
3. `-Step FlagFixApply -ProposalFile <report> -SectionIds <comma-list> -FlagCode <code>` —
   re-checks each chosen section's *current* body (not the cached report) and generates a `PROSE`
   supersede patch, same shape as `ImportChapter`'s. Apply it the normal way,
   `scripts/apply_session_patch.py`.
4. Once that patch is actually applied, close the flag yourself — `corrective_action`/
   `correction_date` on the `wa_data_quality_flags` row. Not automated (deliberately — closing it
   before the patch is confirmed applied would let a flag read "fixed" before anything changed).

Full design + the 6 decisions behind this: `iba/docs/prose-add-edit-rules-proposal-v1-20260826.md`.
Build record: `BUILD.md` §184.

---

## 14. Everyday commands, in order

**Corrected 2026-08-08** — this list still showed the retired `VerseSpanMeaning-Report.ps1`/
`PassageDebate-Report.ps1` pair as "the current per-book study method," contradicting §12b's own
2026-08-07 rewrite, which retired that pair in favour of `VerseLexical.ps1`/`Debate-Run.ps1`. §14
was last corrected 2026-07-30 — before that rewrite — and was never brought back in sync. Replaced
below with the current two-tool pipeline (§12b). (Prior correction, 2026-07-30: this list used to
show the retired `Set-Candidates.ps1`/`Build-Passages.ps1`/`Candidate-Curate.ps1` as the normal
per-book workflow, contradicting §8/§10's own RETIRED markings; replaced then with the
verse-analysis/passage-debate method, and the 4 previously-undocumented scripts (§3a/§11a/§12b/§12c)
added.)

`-Book` below is always the **OSIS book code as stored in `verse.osisId`** (e.g. `Dan`, not
`Daniel`) — every script that also writes to a human-facing folder takes a separate `-BookLabel`
(e.g. `-BookLabel Daniel`) for that; the two are never the same parameter.

```powershell
# once, at the start of a session:
iba\app\ps\Start-Iba.ps1

# for each new word (no pause/approval step since 2026-08-20, BUILD.md §153 -- runs straight through):
iba\app\ps\New-Word.ps1 -Word <word> -Source "<why>"

# fill in supporting-term meaning for a book/range, if you want it done ahead of time (§3a):
iba\app\ps\Raw-Backfill.ps1 -Book <book> [-Range <ch:v-v>]

# the current per-book study method — lexical once, then debate per chapter/range (§12b):
iba\app\ps\VerseLexical.ps1 -Book <book> -Chapters <whole book, e.g. 1-12> [-BookLabel <Label>]
iba\app\ps\Debate-Run.ps1 -Book <book> -Chapters <n-n> [-BookLabel <Label>]
#   ... write each step's staging payload when it stops and asks for one, rerun the same command,
#   repeat per chapter/range. -BookLabel (added 2026-08-08) defaults to -Book if omitted -- every
#   step's own reconciliation report AND the final rendered debate report file under
#   iba/app/verse-analysis/<BookLabel or Book>/, same convention every sibling book tool uses
#   (see §12b) -- always pass it for a book you already have a labelled folder for.
#   WholeBookRead-Report.ps1 is a KNOWN GAP against this model (§12b) — still correct for the 6
#   pre-existing scaffold-model books (Amos/Hosea/Joel/Jonah/Micah/Obadiah), not yet rebuilt
#   against Debate-Run.ps1-produced books.

# generate the narrative itself — real API cost, approval-gated (§12d):
iba\app\ps\BookNarrative-Generate.ps1 -Book <book> -BookLabel <Label>

# structural check on a finished inner-being narrative (§12c):
iba\app\ps\BookNarrative-Validate.ps1 -Path <narrative file>

# see what's open, answer it:
iba\app\ps\Escalation.ps1 -Action List
iba\app\ps\Escalation.ps1 -Action AnswerRun -RunId <id> -Decision Approve|Reject|Revise|Hold|Noted

# read it:
iba\app\ps\Reports.ps1 -Step ReportWord -Word <word>

# check on data/config health, any time:
iba\app\ps\Passage-Quality.ps1 [-Book <book>]
iba\app\ps\Lexicon-Parse.ps1 -Step Validate
iba\app\ps\Config-Maintenance.ps1 -Step Validate
iba\app\ps\Log-Retention.ps1

# the 4 analysis reports, any time (§12a):
iba\app\ps\StrongMeaning-Report.ps1
iba\app\ps\SpanAnalysis-Report.ps1
iba\app\ps\SchemaOverview-Report.ps1
iba\app\ps\Registry-Report.ps1

# word-registry Strong's/span analysis, any time (§12e):
iba\app\ps\WordRegistrySpan-Report.ps1 -Word <word>

# on-demand verse restatement for ONE Strong's reference, any time (§12f):
iba\app\ps\StrongVerse-Report.ps1 -Word <word> -Strong <strong>

# cluster taxonomy report, any time; DB-wide mechanical assign is mutating (§12g):
iba\app\ps\Cluster-Report.ps1
iba\app\ps\Cluster-Assign.ps1 -Step Validate
iba\app\ps\Cluster-Assign.ps1 -Step Assign

# remove a test word (dry-run, then --yes):
python -m iba.app.tools.purge_word --word <word>

# start clean (drops data, keeps config):
iba\app\ps\Start-Iba.ps1 -Reset

# see every config the code reads, live:
iba\app\ps\New-Word.ps1 -Word <word> -Source "<why>" -Trace
```

---

## 15. Migrations (one-off setup)

These run **once** to bring the legacy study into the app. They live in `iba/app/migration/`
(kept separate from the standard methods) and are not part of the daily flow.

**Migrate the legacy registry** — load the old word list, running the new-word build for each word
in series:

```powershell
iba\app\migration\Import-LegacyRegistry.ps1 -DryRun     # preview the words (no changes, no STEP)
iba\app\migration\Import-LegacyRegistry.ps1 -Limit 5    # trial the first few
iba\app\migration\Import-LegacyRegistry.ps1             # the full run, in series
```

It reads the old registry **read-only** (excluding words marked deleted/excluded), auto-approves
each (the list is your own curated, already-approved registry), **skips words already built** — so
if it stops it can simply be re-run and it continues — and writes a transcript to
`iba/app/reports/`.

**Migrate the candidate seed** — historical record only, corrected 2026-07-30: this loaded the
independent candidate-characteristic seed that the now-retired `Set-Candidates.ps1`/§10 pipeline
depended on (§8/§10). Not part of the current method (§12b/§12c) and not needed for it.

```powershell
python -m iba.app.migration.import_seed
```

It imports the lemma inventory + candidate assessment from the old study and maps it against the
strongs already in the app.

---

## 16. Where things are

```text
iba/app/
  config/     schema/step/run/rules JSON seeds (archived — DB is master) · CONFIG-REPORT.md (generated,
              incl. a per-report governance rollup) · archive/ + export/ (auto-archived snapshots /
              CSV pairing for CONFIG-REPORT.md itself)
  db/iba.db   the database (config tables cfg_* + the data)
  db/snapshots/  pre-run DB snapshots (added 2026-07-22) — every new run copies iba.db here first
  ps/         Start-Iba.ps1 · New-Word.ps1 · Config-Maintenance.ps1 · Candidate-Quality.ps1 ·
              Lexicon-Parse.ps1 · Passage-Quality.ps1 · Reports.ps1 · Export-Tables.ps1 ·
              Escalation.ps1 · Log-Retention.ps1 · SeedCandidate-Report.ps1 ·
              StrongMeaning-Report.ps1 · SpanAnalysis-Report.ps1 · SchemaOverview-Report.ps1 ·
              Registry-Report.ps1 · WordRegistrySpan-Report.ps1 (§12e) ·
              StrongVerse-Report.ps1 (§12f) ·
              Cluster-Report.ps1 · Cluster-Assign.ps1 (§12g) ·
              **current per-book pipeline (§12b):** VerseLexical.ps1 · Debate-Run.ps1 ·
              Operations-Ingest.ps1 (the work package Debate-Run.ps1's hib/phenomenon/operation/
              closing steps run under) ·
              WholeBookRead-Report.ps1 (known gap against the current model, §12b) ·
              BookNarrative-Generate.ps1 (§12d — real API cost) · BookNarrative-Validate.ps1 ·
              **retired, kept on disk for provenance — do not use:** Set-Candidates.ps1 ·
              Build-Passages.ps1 · Candidate-Curate.ps1 (§8/§10) · VerseSpanMeaning-Report.ps1 ·
              PassageDebate-Report.ps1 · PassageDebate-Sync.ps1 · Chapter-Generate.ps1 (§12b) ·
              Book-Narrative.ps1 (superseded by the split BookNarrative-Generate.ps1/
              BookNarrative-Validate.ps1 above — not otherwise documented in this guide) ·
              create-iba-view-template.ps1 · create-passage-view-and-export.ps1 ·
              create-passages-by-book-view-and-export.ps1 · export-iba-config-tables.ps1 ·
              generate-iba-db-schema-report.ps1 (5 standalone investigation utilities, relocated
              here from iba\scripts\ 2026-07-23) ·
              _lib/Notify.ps1 (shared terminal wording, not run directly)
  init.py     the bootstrap (Start-Iba calls it)
  lib/        cfg (read) · cfgload+cfgcheck (load+validate) · cfgreport · cfgquality · valuequality ·
              dbsnapshot · db · stepapi · escalation · words · reportkit (shared report rendering +
              archiving, incl. CSV writes + CSV pairing + one-off naming) · seedreport ·
              strongreport · spanreport · schemareport · registryreport (the 5 analysis reports,
              §12a) · wordregistryspanreport (§12e) · strongversereport (§12f) · passagetrack ·
              passagedebatereport · wholebookread · versespanmeaningreport (§12b) ·
              narrativegenerate (§12d — assembly + Anthropic Messages API call + filing)
  handlers/   registry · raw · configmaint · candidate · passage · reports   (interpreters, no hard rules)
  migration/  one-off: Import-LegacyRegistry.ps1 · legacy_import · import_seed · ~20 further
              bootstrap/schema-addition scripts (see GOVERNANCE.md §7 for the full current list)
  tools/      purge_word · export_tables_csv · log_retention · _apply_verse_plaintext_column ·
              build_span_heatmap_v1 (2 relocated from iba\scripts\ 2026-07-23)
  run.py            the dispatcher
  report.py · validation.py   the two original output + validation reports
  reports/    every generated report (candidate-quality.md, seed-candidate.md, registry.md, ...) ·
              archive/ (auto-archived prior versions, incl. CSVs) · export/ (per-report CSV AND
              table-export's dump, consolidated into one folder 2026-07-23 — git-ignored)
  archive/    non-report historical files (new 2026-07-23) — e.g. a superseded pre-restructure
              New-Word.ps1 stub found outside iba/app/
  BUILD.md          what's built, how the parts fit
  GOVERNANCE.md     how config governs the code
  UTILITIES.md      the utilities around the run
  USER-GUIDE.md     this file
  PLAN-reports-config-governance-v1-20260722.md   the reports-config-governance design + build log
```

For the raw model (term → sense → span) and the data-layer design, see
`iba/docs/stream-registry-word-buildout-v7/v8` and `iba/docs/raw-config-design-v1`.
