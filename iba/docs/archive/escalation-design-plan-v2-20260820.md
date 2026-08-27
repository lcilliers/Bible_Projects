# Escalation design plan (v2, 2026-08-20)

Supersedes [`escalation-design-plan-v1-20260820.md`](escalation-design-plan-v1-20260820.md) in
approach, not in its verified facts (the live-system findings there — the id collision, the stale
`cfg_table.use` text, the two dropped directives, the `GOVERNANCE.md` gap — all still stand and are
carried forward, not re-litigated). v1's failure, named directly by the researcher: it answered the
prompt's headings as questions to look up, one at a time, in isolation. This is not that. **This is
a design** — a proposed, reasoned answer to "how should this utility actually work," built by
treating every item, every rule, every relationship as belonging to one coherent picture, not a
checklist. Nothing here is built. Every proposal below is a decision for the researcher, laid out
with its reasoning, not a fact retrieved.

---

## Resources

Unchanged from v1's list (all still the basis for this document) — not repeated in full here. Two
additions this round, both the researcher's own direct correction, in this conversation, not a
document: (1) task/issue/notice are not interchangeable "item" instances — each is a different kind
of stream with a different purpose and a different shape of life; (2) an item's history is not its
own row's version log in isolation — it is the whole connected arc of documents, decisions, and
related items that bear on it, read together as one story. Both are load-bearing for every section
below.

---

## Purpose

**What the utility is for, stated practically:** this project runs as a continuous stream of three
genuinely different kinds of activity — deciding what to do, doing it, and recording what happened —
plus two automatic streams that the system itself generates. The utility's job is to be the single
place all five of those are captured, in a shape that matches what each one actually is, so that
nothing gets lost, nothing gets treated as more or less than it is, and the researcher can always
answer "what's actually open, what's actually settled, and how did we get here" without re-reading a
pile of prose to reconstruct it. That last clause is the part v1 didn't meet — the mechanism can
currently answer "what's open" (barely — see below) but not "how did we get here," because the
connective tissue between items is a loose text label, not a real structure.

**How the current design falls short of that, concretely, stated once here so every later section
can refer back to it instead of re-deriving it:**
1. Every type is forced through the same state machine, so a debate (issue) is tracked as if it were
   a piece of work (task), and an FYI (notice) is tracked as if it needed a decision at all.
2. Nothing links an item to what it came from or what it produced — `related_activity` is a loose
   string, confirmed this session to already be inconsistently applied even by Claude's own hand
   (`#712`'s cascade landed under a different label than `#712` itself carried).
3. A large body of work has nowhere honest to live except as one oversized item (`#753`'s pattern) —
   because there is no first-class way to say "this issue, once decided, produced these five tasks."

The rest of this document is the design that closes those three gaps, worked through area by area.

---

## Type of entries

Five types exist in `cfg_enum('escalation_type')`. Each gets the same depth of treatment here — not
three examples and two afterthoughts.

### `task` — do something, get it confirmed done

**Real-world instances:** reseed the id sequence; register a missing `cfg_column` row; fix a stale
`enforced_by` claim. **Purpose:** track that one bounded piece of work happens and is verified.
**Shape of its life:** raised → someone works it (`in-progress`) → they believe it's done
(`ready_for_approval`, `resolution` filled in) → a *different* party confirms (`approved` →
`completed`) — or it turns out unnecessary/wrong (`reject` → `withdraw`/`supersede`). The two-stage
handshake already built this session fits a task exactly as designed — this is the one type the
current mechanism actually serves well.

**Sizing — the part not designed anywhere today:** a task should be sized to what one person can
complete and get confirmed in one sitting. `#753` was not that — it was a whole review programme
squeezed into one row because there was nowhere else for the sub-work to go. Under this design, a
body of work that size is not a task at all — it's an **issue** (below), and it *produces* the
individual tasks. This is a sizing discipline, not a schema rule — nothing can force a person to
raise a small task rather than a large one — but the mechanism should make the small-task path the
easy, natural one, which the issue→produces→task relationship (§tables and columns) does.

### `issue` — work out what should be done, through rounds, before anything is built

**Real-world instances, found by re-reading the actual resource chain rather than asserted:** the
entire `escalation-redesign-plan` v1→v2→v3 sequence; both config-review passes; `#677` (the
reassign/in-progress design gap, resolved only after the researcher pushed back on Claude's first
framing and reasoned through three named options). **Purpose:** a space for genuine deliberation —
proposal, feedback, revision, more feedback — until a direction is actually decided. **This is
categorically not a task with an approval step** — there is no single "the work is done, confirm it"
moment; there's a moving position that gets argued into a settled one.

**Where this currently, actually lives:** nowhere inside the escalation mechanism. Every one of the
real-world instances above happened as `.md` files in `iba/docs/` plus note files in
`Workflow/Chat_responses/`, with escalation only ever holding the occasional pause tied to it
(`#753`, `#746`) — never the debate itself, never its round count, never a structural note of which
document is the current live draft. `type='issue'` exists in the enum and is applied as a label
(this document's own predecessor findings are filed under it) but nothing in the mechanism treats an
issue differently from a task once it's raised. That gap is the direct cause of the researcher's
correction — the type carries no behaviour.

**Proposed shape of its life:** an issue does not use the manual `ready_for_approval → approved`
vocabulary at all — that vocabulary presumes a single deliverable someone else confirms, which is
the wrong shape for a debate. Propose a **third vocabulary**, `escalation_next_action_issue`:
`open` (still being argued, may go through several rounds — each round a new `escalation_history`
row, `comment`/`context` carrying that round's position, same delta mechanism already built) →
`decided` (a direction was chosen — `resolution` states what was decided and why) → `abandoned` (not
worth pursuing, `comment` states why). `state` follows the same shape `cfg_escalation_transition`
already provides — `open`→`in-progress` (still live), `decided`/`abandoned`→`completed`/`withdraw` —
just a fourth row-group in that same table, keyed by `type='issue'` in addition to `shape`.

**The document link, made real instead of conventional:** `document_reference_grouping`
(`cfg_escalation.rule_key`) already asks that a package's planning document go into
`context.reference_doc` — but this is currently a *convention*, checked nowhere for an issue
specifically, and not distinguished from the same field being used loosely on a task. Propose: for
`type='issue'`, `context.reference_doc` becomes **required** (a `cfg_escalation_requirement` row,
`action='raise'`, `condition_key='type_is_issue'`) — an issue without a document it's actually being
worked in is exactly the pattern that lost track of things before.

### `notice` — for the record, no action, no decision

**Real-world instances:** *"the module_blocking mechanism has been live since 2026-08-17"*;
*"backup completed with a non-fatal warning."* **Purpose:** something worth having written down that
nobody needs to act on or decide about. **Where the current design gets this wrong, concretely:** a
freshly-raised notice defaults to `state='raised'`, `next_action='review'` — the same "someone needs
to look at this and respond" posture a task gets — which is simply false for a notice by definition.
Worse: `cfg_escalation.module_blocking` (confirmed live in `run.py`, rule 3) blocks a module from
running while **any** item against it sits in `raised`/`re-assigned` state, **regardless of type** —
meaning a stray, entirely inert notice could, today, block real work from proceeding. That is not a
theoretical gap; it is the direct, structural consequence of treating every type identically that
the researcher's correction named.

**Proposed shape of its life:** at Raise, if `type='notice'`, skip the decision machinery entirely —
`next_action=NULL`, `state='closed'` immediately (one `escalation_history` row, no second
transaction needed to close it). `module_blocking`'s query gets an explicit `AND type != 'notice'`
(or, cleaner: since a closed-at-raise notice is never in `raised`/`re-assigned` state at all under
this design, the existing query already excludes it correctly once the defaulting fix lands — no
separate blocking-logic change needed, which is the simpler fix and the one to prefer).

### `run_error` — a defect exists, automatically detected

**Real-world instances:** the CLI crash-wrapper firing on this session's own title-shape mistakes
(escalations `#2`/`#3`); a dispatcher-tied crash pause in `run.py`. **Purpose:** record that
something broke, with enough detail (a traceback, the arguments that triggered it) to fix it — not a
debate, not an FYI. **The origin-vs-nature distinction, worth stating plainly since it isn't written
anywhere:** `source` already records *who/what* raised an item (a script name, `claude`,
`researcher`); `type` should record *what kind of resolution it needs* — a crash's nature is "a
defect exists, go fix it," which is a `task` in lifecycle terms, just tagged `run_error` for
provenance so it's queryable in aggregate (*"how often is module X crashing"* — a reporting need,
§report, currently unsupported: no aggregation over `type` exists in either report today).

**Proposed shape of its life:** the `task` vocabulary and transition rules apply unchanged — a
`run_error` is a task with a known cause. The only design addition is on the **report** side: a
`type` breakdown in the list report's summary line (today's report only splits by
active/in-progress/on-hold — adding a `run_error` count surfaces exactly the "is this module
unreliable" signal the type exists to carry).

### `config` — a proposed change to the app's own governing configuration

**Purpose:** the narrowest, most specific type — always a `configmaint.propose` pause, always
dispatcher-tied by construction, always backed by a real before/after audit row in
`cfg_change_detail` (confirmed live, 277 rows, the one genuinely audited write path in the whole
app). **Shape of its life:** unchanged — this is the dispatcher shape working as designed, three-way
approve/reject/revise, `resolution` should arguably be **more strictly required** here than the
generic rule gives it (every config change should carry a stated reason it was approved, not just
"a resolution field was non-empty") — flagged as a candidate `cfg_escalation_requirement` tightening,
not built here.

### Item relationships — the piece that makes many items "fit together"

This is the direct answer to *"it has related items... it all fits together... you make every item
the same."* Three real patterns were found this session, none of them structurally supported:

| Pattern found | Example | What's missing |
|---|---|---|
| A chain of peer revisions | `#648→#669→#670→#672→#677→#680→#699→#701`, one shared `related_activity` string | No typed relationship — "this supersedes the last one" and "this is unrelated but same topic" look identical |
| A cascade with a broken link | `#712` surfaced `#719–#724`, but they carry a *different* `related_activity` than `#712` itself | The parent→child fact exists only in `BUILD.md` prose, nowhere in the data |
| A whole programme folded into one row | `#753` | No way to say "this issue produced these five tasks" — so it never did; it just grew |

**Proposal:** a real `escalation_link` table — the option `escalation-redesign-plan-v1` §3 raised and
recommended, deferred in v3 as *"plain text at this stage, not a structural link table... decided"*
(`cfg_column.related_activity.use`). "At this stage" was the operative phrase — three sessions of
accumulated evidence since then is exactly the signal that stage has ended.

```sql
CREATE TABLE cfg_escalation_link (         -- deliberately in the cfg_ series: this is a rule/
    from_id INTEGER NOT NULL,              -- structure table, not a data table, same reasoning
    to_id INTEGER NOT NULL,                -- cfg_escalation_transition already uses
    link_type TEXT NOT NULL,               -- cfg_enum('escalation_link_type')
    created_at TEXT NOT NULL,
    created_by TEXT NOT NULL,
    PRIMARY KEY (from_id, to_id, link_type)
)
```

`escalation_link_type` (new `cfg_enum`): `produces` (issue → task, the resolution of a debate
spawning concrete work — inverse: `part_of`), `supersedes` (the existing title-correction pattern,
§4.7 `USER-GUIDE.md`, made structural instead of a `related_activity` string match), `duplicate_of`,
`blocks`/`blocked_by`. `related_activity` (free text) is **kept**, not replaced — it still serves a
real, looser purpose (a topic label a human can scan, e.g. `engine-controls-migration`), but it stops
being asked to carry structural weight it can't hold. `write_history_report()`'s traversal (currently
a `related_activity` `LIKE` match plus a regex over free text — both confirmed fragile this session)
is rewritten to walk `cfg_escalation_link` instead, which is exact instead of best-effort.

**The rollup this makes possible, as a report query, not a maintained column** (per
`feedback_simple_steps_not_engineered_designs` — a denormalised "all children done" flag is exactly
the kind of machinery this project's own history says to avoid; a query at read time does the same
job with no write-path complexity): an issue's deep-history report can now show, accurately, *"this
issue produced tasks #X, #Y, #Z — 2 completed, 1 still open"* — the actual question `#753` existed
to answer and could never answer for itself.

---

## transaction types

Two remain true at the mechanical level — the researcher's original *"in principle there are only
two transaction types... the resulting state is determined by the values in the fields"* still holds
— but **Raise now branches meaningfully by `type`**, and a third operation (**Link**) is new:

| Transaction | What changes under this design |
|---|---|
| **Raise** | For `task`/`run_error`/`config`: unchanged (today's manual/dispatcher flow). For `issue`: `next_action` defaults to `open`, not `review`; `context.reference_doc` becomes required. For `notice`: `next_action=NULL`, `state='closed'` immediately — no second transaction to close it. |
| **Update** | For `task`/`run_error`/`config`: unchanged. For `issue`: validates against `escalation_next_action_issue` (`open`/`decided`/`abandoned`), not the manual vocabulary — a round of debate is an `open`-to-`open` update (still in progress), same delta mechanism, new vocabulary. |
| **Link** *(new)* | `-Action Link -Id <from> -To <to> -LinkType produces\|supersedes\|duplicate_of\|blocks -AnsweredBy ...` — writes one `cfg_escalation_link` row. Read-heavy consumers (`-Action History`, the list report) read it back; nothing about the linked items' own state changes as a side effect of linking (kept deliberately simple — no cascading state logic, which is exactly the kind of trigger-like machinery this project has previously chosen not to build, §control items). |

---

## tables and columns

**Carried forward from v1, unchanged, still open (not re-argued here):**
- `escalation`'s id sequence collision with `escalations_old` (escalation `#5`).
- `escalation`/`escalation_history`'s stale `cfg_table.use` text (escalation `#4`).

**New this round:**
- `cfg_escalation_link` (schema above) + `cfg_enum('escalation_link_type')`.
- `cfg_escalation_transition`/`cfg_escalation_requirement` both gain an optional `type` column
  (`NULL` = applies to any type, matching how `next_action=NULL` already means "any" in the existing
  rows) — this is the concrete mechanism that makes `type` finally gate behaviour, the researcher's
  core correction, expressed as schema rather than left as a chat conclusion.
- `escalation.next_action`'s `cfg_column.use` needs a third vocabulary named alongside the existing
  two (currently: *"TWO vocabularies share this column: dispatcher-tied... and manual..."* — becomes
  three, `escalation_next_action_issue` added).
- `cfg_utility.escalation.purpose` — still carrying the pre-redesign one-liner (v1 finding, unfixed);
  the corrected text should now also name the type-differentiated model, not just the original
  broadened-scope wording from plan v1 §1.

---

## Governance

Rewritten in the shape the researcher asked for explicitly: **what's required → how this design
responds → what's still broken.** Every `governance.*` setting live at session start, checked again
against this round's proposal specifically (not re-copied from v1's table where the answer is
unchanged by this round's additions):

| Rule | Required | This design's response | Still broken |
|---|---|---|---|
| `governance.escalation.scope` | Every open item, anomaly, clarification recorded in escalation | The type/link model is *how* it can actually hold everything — a debate no longer has to either become one oversized task or live entirely outside the table | Until built, still true that debates live outside the mechanism |
| `governance.rules_must_be_config_driven` | No rule lives only in code/docs | Type-conditioned transition/requirement rules go into the *same* `cfg_escalation_transition`/`cfg_escalation_requirement` tables already built this session, extended with a `type` column — not a new parallel mechanism | `escalation_shape`'s orphan-check blind spot (v1 finding) unfixed; would recur for `escalation_link_type` if its own runtime lookup isn't wired carefully — a build-time risk to watch, not yet an error since nothing built |
| `governance.governance_md_on_rule_change` | `GOVERNANCE.md` updated same unit of work as any rule change | Not yet done for the ORIGINAL rebuild either (v1 finding, unfixed) — this round adds MORE undocumented mechanism on top if built without also writing the section | Open — and growing if this design is approved and built before that debt is paid down |
| `governance.table_columns` / `governance.tables` | Every table/column has accurate, current `use` text | `cfg_escalation_link`/`cfg_escalation_link_type` would be registered at build time per this project's own established discipline (confirmed followed correctly for the two tables built this session) | The two pre-existing stale rows (v1 finding) still open — a new table done right doesn't retroactively fix old rows done wrong |
| `feedback_simple_steps_not_engineered_designs` | Don't build machinery beyond real, evidenced need | Directly addressed above: the link table is proposed *because* three separate real failures were found this session (the chain, the broken cascade link, `#753`), not speculatively; the rollup is a query, not a maintained state; Link doesn't cascade side effects | This is a judgement call for the researcher to test, not something Claude can self-certify as "not over-engineered" |
| `governance.reports_must_persist` | Findings persist to a config-defined path | Unaffected by this round's proposals — still true | The two escalation reports still bypass `cfg_report` registration (v1 finding — directive 3, dropped once already, unfixed) |
| `governance.past_precedent_investigation_signals_missing_config` | Needing to read `BUILD.md`/session history to reconstruct a rule = the rule itself is missing from config | This document's own §Type of entries required exactly that kind of archaeology to establish what "issue" was actually supposed to mean — which is itself evidence the type-behaviour gap is real, not a design nicety | Confirms, doesn't yet resolve — resolved only once type-conditioned rows actually exist in config |

**A rule not yet in `governance.*` at all, surfaced by this round specifically:** nothing currently
states that *"a type change is behaviour, not decoration — every type must have its own transition
and requirement rules, reviewed as a set whenever a new type is added."* Proposed as a new setting,
`governance.escalation.type_is_structural`, precisely so the mistake this document exists to correct
can't recur silently the next time a sixth type gets added.

---

## control items

Redone per type, since type now genuinely changes which combinations are even reachable — not one
flat table pretending every type shares a state space:

**`task` / `run_error` / `config`** (the existing two-stage/dispatcher shapes, unchanged from v1's
table — not repeated in full; see v1 §control items) — `originator` ≠ last `ready_for_approval`
setter at `approved`, `type` still never gates *this* part of the machinery, correctly, since these
three genuinely do share one shape.

**`issue`** (new):

| Combination | Meaning | Illegal combination |
|---|---|---|
| `next_action=open`, `state=in-progress` | Still being argued — every round lands here | — |
| `next_action=decided`, `resolution` present | A direction was chosen | `decided` with empty `resolution` — nothing was actually decided if nothing states what |
| `next_action=abandoned`, `comment` present (why) | Not worth pursuing | `abandoned` with no reason given |
| Linked `produces` rows exist, issue still `open` | A direction is already spawning work before the debate formally closed | Not illegal — matches real practice (`#712`'s work started before every follow-on was fully scoped) — but the deep-history report should show this plainly as "still open, already producing work," not hide it |

**`notice`:**

| Combination | Meaning | Illegal combination |
|---|---|---|
| `state=closed` at v1, `next_action=NULL` | The only reachable combination — set automatically | Any notice sitting in `raised`/`re-assigned` — a defaulting bug if this design is built and one is ever observed there |

---

## automation

Carried forward from v1's per-column table (still accurate for the columns it covered) plus what's
new this round:

| What | Automated how |
|---|---|
| `next_action` default at Raise | Currently one hardcoded default (`review`) regardless of type — becomes a `type`-keyed lookup: `review` for task/run_error/config, `open` for issue, `NULL` for notice |
| `state` at Raise | Currently always `raised` — becomes `raised` for task/run_error/config/issue, `closed` for notice |
| `cfg_escalation_link` rows | Never automatically written by anything but `-Action Link` — deliberately no auto-linking (e.g. no "auto-detect this looks related") — matches the project's own preference for explicit, reviewable actions over inferred ones |
| Deep-history traversal | Currently regex-over-`related_activity` text — becomes a real join against `cfg_escalation_link`, still fully automatic, just accurate instead of best-effort |
| Report `type` breakdown | New — a count-by-type line in the list report header, alongside the existing active/in-progress/on-hold split |

---

## configs

Cross-checked the same way v1 attempted but actually following through this time — every new value
traced to a column, a rule, an automation point, and a validation, not left floating:

| New config | Column it governs | Rule that reads it | Automation | Validation |
|---|---|---|---|---|
| `escalation_next_action_issue` (open/decided/abandoned) | `escalation.next_action`, when `type='issue'` | `cfg_escalation_transition` rows keyed `type='issue'` | `Update`'s issue branch | `_check_next_action_issue()` (new function, same pattern as the existing two) |
| `escalation_link_type` (produces/part_of/supersedes/duplicate_of/blocks/blocked_by) | `cfg_escalation_link.link_type` | Read by the deep-history traversal and the new "produced tasks" rollup query | `-Action Link` | Validated against the enum at write time, same pattern as every other enum-backed column in this module |
| `governance.escalation.type_is_structural` | N/A (a governance statement, not a data column) | Read by nobody automatically (like most `governance.*` settings) — a documented standard, checked at review time | N/A | N/A — self-admittedly session-practice-only, same honest category as `resolution_precedence`/`chat_routing` already are |

**Redundancy check, as asked:** `escalation_type` (5 values) now has real behavioural consequences
for 3 of its 5 members (issue, notice, differ from task/run_error/config) — no longer a case of "5
values in an enum with only 2 practical states," which was the actual redundancy the researcher's
correction was naming, even though it wasn't phrased as a "redundant config" complaint. Nothing
proposed here is redundant with an existing table — `cfg_escalation_link` covers ground
`related_activity` structurally cannot; the `type` column addition to the two existing rule tables
reuses machinery already built rather than duplicating it.

---

## validation

| Validation | Applies to | Configured via | On violation |
|---|---|---|---|
| `context.reference_doc` required | `type='issue'` at Raise | `cfg_escalation_requirement(action='raise', field='context', condition_key='type_is_issue')` | `ValueError` — an issue with no document to point at is the exact failure this design closes |
| `resolution` required, non-empty reason | `type='issue'`, `next_action='decided'` | Same table, `condition_key='type_is_issue_decided'` | `ValueError` |
| `comment` required (the reason) | `type='issue'`, `next_action='abandoned'` | Same pattern | `ValueError` |
| Link type is a real enum member | `-Action Link` | `cfg_enum('escalation_link_type')` | `ValueError`, same pattern as every other enum check in this module |
| No self-link (`from_id == to_id`) | `-Action Link` | Code-only — not the kind of thing a `cfg_*` row states, same category as the existing two-stage same-party check | `ValueError` |
| A `notice` never reaches `raised`/`re-assigned` | Post-Raise invariant | The `type`-keyed default above | If ever observed, it's a defaulting bug, not a data problem — worth a `configmaint.validate` check (`find_stray_notices()`-shaped, matching the project's existing pattern of a Python function per specific integrity check) |

---

## scripts

Same code footprint as v1's inventory (`escalation.py`, `Escalation.ps1`, `run.py`, the 8 handlers,
`tools/purge_word.py`, `retention.py`/`cfgquality.py`/`validation.py`/`schemareport.py`) — **what
changes in each, under this design, stated as a plan, not built:**

- `escalation.py`: `_evaluate_transition`/`_check_requirements` both gain a `type` parameter, looked
  up alongside `shape`; a new `_check_next_action_issue()`; a new `link()` function writing
  `cfg_escalation_link`; `raise_new()`'s defaulting logic becomes `type`-keyed instead of a flat
  literal.
- `Escalation.ps1`: `-Action Link` added, mirroring the existing four; `-NextAction`'s `ValidateSet`
  needs to accept the issue vocabulary too (or a second, type-scoped parameter — a real UI decision,
  not resolved here, flagged for the researcher: one `-NextAction` parameter validated against
  whichever vocabulary the target item's `type` implies, or a separate `-IssueAction` parameter kept
  visibly distinct — my inclination is the former, matching "one column, `type`-scoped meaning,"
  which is the same pattern already chosen for `next_action` sharing dispatcher/manual).
- `write_list_report()`/`write_history_report()`: grouping and traversal rewritten to use
  `cfg_escalation_link` (§tables and columns); list report gains the type-breakdown line.
- No change needed to `run.py`, the 8 handlers, or `tools/purge_word.py` — none of them create
  issues or notices; they only ever raise dispatcher-tied (`config`) or `run_error` items, both
  unchanged by this design.

---

## report

| Report | Purpose, restated against this design | What changes |
|---|---|---|
| Open-items list | *"What's open, and what kind of open is it"* — currently answers only the second half by accident (state grouping), not by design | Grouped first by `type` (task/issue/notice-never-appears-here-since-it-closes-at-raise/run_error/config), then `related_activity` as today within each group; a summary line breaking counts down by type, not just by state |
| Deep-history | *"The whole story of one thread — every document, every related item, together"* — this is the direct answer to *"how does it relate to supporting documents... does it all fit together"* | Traversal via `cfg_escalation_link` (exact) instead of regex-over-text (best-effort); for an `issue`, explicitly lists its `produces` links with each task's current state — the "produced work" rollup, computed at read time |
| *(still not built, carried forward from v1, unfixed)* `cfg_report`/`reportkit` registration for both reports | The standard every other of the app's 22 reports meets | Unaffected by this round — still open, still the twice-dropped directive |

---

## Summary — what this document is actually asking the researcher to decide

Not a list of facts to confirm — a design to accept, reject, or correct, piece by piece:

1. **The five-type model above** — does it match how you actually think about task/issue/notice/
   run_error/config, or is a boundary drawn wrong somewhere?
2. **A real `cfg_escalation_link` table**, replacing structural weight `related_activity` was never
   built to carry (kept alongside, not replacing it, for its looser topic-label role).
3. **A third `next_action` vocabulary for issues** (`open`/`decided`/`abandoned`), instead of forcing
   debates through the task-shaped `ready_for_approval`/`approved` handshake.
4. **Type-keyed defaults at Raise** — notices close themselves immediately; issues open instead of
   defaulting to "needs review."
5. Everything carried forward unresolved from v1 (id collision, stale table text, the two dropped
   directives, the `GOVERNANCE.md` gap, `cfg_utility.escalation.purpose`) — still open, not
   superseded by this round's additions, and arguably more urgent now, since building type-aware
   behaviour on top of an already-undocumented mechanism compounds the same debt this document is
   trying to stop recurring.

Still nothing built. This module's own history is the argument for that discipline, not a formality.
