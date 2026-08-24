> **Superseded by [prose-change-log-design-v2-20260824.md](prose-change-log-design-v2-20260824.md).**
> Kept on disk for history only.

# Prose change log design — versioning integrity (#836)

Status: **opening section only** — objective, control scope, and a survey of existing project
methods. No design/recommendation yet — filed for review before going further, per the standing
plan/propose/design → approve → build → approve cycle (escalation #828).

Spawned from: escalation #829 §6a (D5/D6/D7), which is on-hold pending this. Addresses D5, D6, D7
together, per #836's own scope statement.

---

## 1. Objective

Establish a correct, complete, and connected change-tracking discipline for the two core prose
tables, replacing the current state where change-tracking is either unreliable or absent:

| Table | Current state |
|---|---|
| `prose_section` | Has `created_at` only. For the (almost) supersede-only write pattern this doubles as "when this version was made" — but the one sanctioned in-place exception, `session_a_replace`, writes an `UPDATE` that touches no timestamp at all, so that row's `created_at` goes silently stale relative to its real last change. |
| `prose_section_type` | Has **neither** a version column **nor** any last-modified column. Rows are edited in place routinely (this proposal's own build writes `book_label`/`book_order`/etc. onto existing rows) with **zero trace** that a change happened, when, or what it was. |

Two further facts, both checked live (not assumed), sharpen the problem beyond "add a
last-modified column":

- **The version mechanism isn't reliably ordinal.** Where the supersede chain is followed cleanly,
  `prose_section.version` does increment by exactly 1 per link (id 1 → version 1 → superseded by
  id 15 → version 2). But some rows carry mixed-type legacy values (`'1_0'`, `'v1'`, `'v2'` strings
  from earlier, less-disciplined imports) that break trusting the column as a clean ordinal today.
- **`source_file` cannot be relied on as "one file = one change event."** Checked live:
  `prose_section` ids 17 and 19 — two different sections, different content — both carry
  `source_file = 'wa-prose-ch3-obslog-v1_0-20260422.md'`. One import file produced two separate
  section changes. Any design that assumes a change event maps 1:1 to a source file is already
  wrong against live data.

The objective is to settle, **before #829's build proceeds further**, whether version/change
integrity belongs as columns directly on the two tables (current-state facts: version number,
last-modified datetime), as a separate append-only change-log table (event history: who, when,
source, bundled-with — the researcher's own **"process_change_log"** framing), or both — and to do
so in a way that holds up against the two live facts above, not just the happy-path case.

One direct piece of coupling this must not leave dangling: #829 §5 already drafts a
`cfg_behaviour_rule` (`prose-section-supersede-only-discipline`) whose text asserts
`version = old.version + 1` as a settled rule. This design either confirms that text as correct or
revises it — it doesn't get left standing as asserted fact while this item is still open.

---

## 2. What we need to control

Framed as control questions, not solutions — the solution comes after this is agreed:

1. **Current-state answerability.** For a given row in either table, can the system answer "what
   version is this, and when did it last change" reliably? Today: sometimes for `prose_section`,
   never for `prose_section_type`.
2. **Change-event capture.** When a change happens, is there a durable record of *what* changed,
   *who/what* made the change, and *where it came from* — distinct from `created_at` (a timestamp
   with no actor or reason attached) and `source_file` (already proven not to equal one change
   event)?
3. **Independent-but-sometimes-joint versioning.** The two tables change independently (researcher's
   own framing: "these two tables may change independently, so versioning on the two tables is not
   connected") — but a single editorial action can touch both at once (e.g. a chapter restructure
   that adds a new `prose_section_type` row and supersedes several `prose_section` rows in the same
   pass). Does control need to be purely per-table, or does it need a way to say "these changes
   happened together"?
3a. Note: the researcher's "may solve more than one problem" framing (opening instruction for this
   item) is read as pointing at exactly this joint-visibility question, alongside the two tables'
   own individual gaps — not yet confirmed, worth checking explicitly once design starts.
4. **The real change-event unit.** If `source_file` doesn't reliably equal one change, what does?
   Needs a definition that survives the ids-17/19 case above.
5. **Where the record lives.** Current-state columns only vs. a separate change-log table (log every
   event: who/when/source/bundled-with) vs. both — normalizing what belongs on-record against what
   belongs in a log, per the researcher's own framing of the question.
6. **Downstream correctness.** Whatever is decided must leave #829 §5's `version = old.version + 1`
   rule either confirmed or corrected — not silently stranded as an unverified assertion.

---

## 3. Relevant methods already in use in this project

Three existing mechanisms were checked live (schema read directly, not assumed) as candidate
shapes or cautionary comparisons. Summary first, detail below.

| Mechanism | Tracks | Actor/reason captured? | Delta or snapshot? | Applicable here? |
|---|---|---|---|---|
| Escalation history (`escalation` + `escalation_history`) | Content/state change of a project item | Yes — `originator` every version | **Delta** (`NULL` unless that transaction set the field) | Closest match — same shape of problem (a mutable current-state row needing a trustworthy per-change audit trail) |
| Run control (`run` table; old engine's `engine_run_log`/`engine_stream_checkpoint`/`word_run_state`) | That a *process* executed, how far it got, how it ended | No content actor/reason — tracks execution, not data | N/A — one row per run | Different axis, not directly reusable. See below. |
| Per-item incremental numbering (`prose_section.version`; chapter-edit export filenames; project-wide `-v{n}-` file convention) | A bare sequential count | No | N/A — just a number | Proven insufficient on its own — same gap this item exists to close |

### 3.1 Escalation history — the closest existing shape

`escalation` is the current cumulative state (one row per escalation, `version INTEGER` incremented
each update). `escalation_history` holds one row per `(escalation_id, version)` — but critically,
its content fields (`comment`/`context`/`resolution`/`tried`/`short_description`/`related_activity`)
are **true deltas**: `NULL` unless that specific transaction actually set that field. This is a
deliberate, hard-won design choice — an earlier version of this same mechanism (rebuilt
2026-08-20) stored full cumulative snapshots in the history table instead, which the researcher
rejected outright ("the system is not ready for production... go back and do a proper design") once
it became clear that shape loses the ability to see *what actually changed* each round, only what
the state was.

Every version also carries `raised_at`/`answered_at` and `originator` — so each row in the history
answers who, when, and what changed, together. State transitions themselves are config-driven
(`cfg_escalation_transition`), not hardcoded — worth noting as a project convention (rules-in-config,
not in code) that would likely apply to whatever this item designs too.

This is a proven, already-approved, two-table pattern (current-state table + delta-history table)
directly analogous to the prose problem: `prose_section`/`prose_section_type` would play the role of
`escalation`; a `prose_section_history`/`prose_section_type_history`-shaped table would play the role
of `escalation_history`.

### 3.2 Engine and run controls — a different axis, not directly applicable

IBA's own `run` table (one row per `run_id`, tracking `state`/`resume_point`/`outcome`/
`started_at`/`ended_at`) is **execution** tracking — did this operation run, how far did it get,
how did it end. The old (pre-IBA, now superseded/provenance-only) Python engine's equivalent tables
— `engine_run_log`, `engine_stream_checkpoint`, `word_run_state` — are the same shape for the same
reason: audit rows for a *process run*, not for a *content change*.

This is a useful negative check, not a candidate mechanism: it confirms the project already keeps
process/run history and content/data history as two separate concerns. `escalation.py`'s own header
states this distinction explicitly for its own domain ("NOT a run-logging mechanism... a standard
operational routine is logged by the engine... escalates only on genuine error"). The prose change
log is a content-versioning problem, matching escalation's shape, not a run-logging problem matching
`run`'s shape.

### 3.3 Per-item incremental numbering — the pattern already in place, and its limit

Three places already do "simple incremental numbering per item," confirming the researcher's own
framing of current practice:

- `prose_section.version` itself — increments by 1 per supersede link when the chain is followed
  cleanly (§1 above notes where this breaks).
- Chapter-edit export filenames (`prosestore.py`'s `_next_edit_version`) — `-v{n}-` scanned across
  the active folder and its archive for the next free number. Purely filesystem-derived, no DB
  backing at all.
- The project-wide file-organisation convention (`docs/file-organisation-rules.md`, "same-name =
  version bump") — the same filesystem-only `-v{n}-` pattern, applied to every proposal/report
  document in the project, including every prior revision of #829's own proposal.

All three share the same limitation: none of them separately records *who* made the change, *why*,
or *what the delta was* — just the sequential count. That is exactly the gap this item exists to
close, and exactly what §3.1's delta-history shape (unlike a bare version number) already solves
elsewhere in the project.

---

## 4. Not yet decided

Nothing below is settled — this section exists so the next round starts from an explicit list, not
a re-derivation:

- Whether the shape is "escalation-style: current-state + delta-history table" (§3.1), applied to
  one or both prose tables, or something narrower (e.g. columns only, no separate log table).
- What the real change-event unit is, if not `source_file` (§2 item 4).
- Whether/how joint changes across both tables get linked (§2 item 3).
- Whether this also needs to touch the already-built flag mechanism (#833) or the deferred
  change-history/diff idea (#829 §12.7, decided "not now" for the external-editor use case) — not
  assumed to be the same problem, flagged as adjacent, to be checked once design starts, not before.
