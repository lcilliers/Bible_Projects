> **Superseded by [prose-change-log-design-v3-20260824.md](prose-change-log-design-v3-20260824.md).**
> Kept on disk for history only.

# Prose change log design — versioning integrity (#836)

Supersedes: [prose-change-log-design-v1-20260824.md](prose-change-log-design-v1-20260824.md) (v1 kept
on disk for history). Sections 1–4 below are v1 unchanged. Sections 5–9 are new this round, answering
the researcher's follow-up (2026-08-24): sources of change, full-text retention, insert/update/delete
scope, whether `version` becomes the change-log id, and a column-by-column relocation candidate list.

Status: still **design/analysis only** — genuine open decisions are named as such, not silently
picked. Filed for review, per the standing plan/propose/design → approve → build → approve cycle
(escalation #828).

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

Structurally: `escalation_history.id` is its own independent autoincrement PK (physical row
identity); `escalation_history.version` is a *separate* business column, a small per-escalation
ordinal mirrored from `escalation.version` at write time, with `UNIQUE(escalation_id, version)`
enforcing there's exactly one history row per version per item. `id` and `version` are deliberately
two different numbers, not one collapsed into the other. This is directly relevant to §8 below.

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

## 4. Not yet decided (carried from v1)

- Whether the shape is "escalation-style: current-state + delta-history table" (§3.1), applied to
  one or both prose tables, or something narrower (e.g. columns only, no separate log table).
- What the real change-event unit is, if not `source_file` (§2 item 4).
- Whether/how joint changes across both tables get linked (§2 item 3).
- Whether this also needs to touch the already-built flag mechanism (#833) or the deferred
  change-history/diff idea (#829 §12.7, decided "not now" for the external-editor use case) — not
  assumed to be the same problem, flagged as adjacent, to be checked once design starts, not before.

---

## 5. Sources of prose change (researcher, 2026-08-24) — checked live against the actual code paths

The researcher named four sources. Each checked against `apply_session_patch.py`'s live operation
set, not assumed:

| Source | Live status | What it touches |
|---|---|---|
| **Update/edit script (multi-table, multi-section)** | **Built and live.** The chapter-edit export/import round-trip (`prosestore.py` `run_export_chapter`/`run_import_chapter` → a `PROSE`-typed patch applied by `apply_session_patch.py`). Confirmed live: a single patch file can carry multiple `prose_section:supersede` operations (one per changed section in the chapter) **and** a `prose_section_type:update` operation in the same file/transaction — e.g. a chapter restructure that both renumbers `prose_section_type.chapter_no`/`sort_order` and supersedes the sections that moved. This is the concrete "multi table, multi section" case. | `prose_section` (supersede, possibly several), `prose_section_type` (update) |
| **Data-quality flag update** | **Not built.** This is #829 §12.4 angle (b) / escalation #835 (on-hold, "will become operational when prose editing comes into action") — search flagged rows → propose fix → researcher approval → apply via the existing supersede path. Whatever this item designs must be usable by that future editing routine too, not just today's chapter-edit script. | `prose_section` (supersede, when built) |
| **Direct update** (chapter sequence, paragraph sequencing, book names, etc.) | **Built and live, and currently the least governed.** `prose_section_type` has exactly two write operations registered: `insert` and `update`. `update` is a bare in-place `UPDATE` — no version column, no timestamp touch, no actor recorded, on ANY of its mutable fields (`chapter_no`, `sort_order`, `book_order`, `book_label`, `section_order`, `section_label`, `description`, etc.). A silent chapter-order or book-name change today leaves no trace at all that it happened, by whom, or why. `prose_section`'s own in-place exception (`session_a_replace`) has the same shape of gap — it does touch `created_at`, but records no actor and no delta. | `prose_section_type` (update, unlogged); `prose_section` (`session_a_replace`, timestamp only) |
| **Findings generators** | **Not conceptualised yet**, per the researcher's own framing — a future automated pathway where an analysis/finding change programmatically alters prose. Named here only as a forward placeholder; no code path exists to check. | Unknown — likely `prose_section` (new content or supersede), possibly triggering the flag mechanism above rather than writing directly |

**On "the rules need to ensure integrity of the log is maintained":** the risk this names is real and
already demonstrated by the current code — two of `prose_section`'s six operations
(`session_a_replace`, and by omission `prose_section_type.update`) already bypass proper
change-tracking, precisely because tracking was added piecemeal per call site rather than enforced
at one shared point. Whatever mechanism this item designs needs a **single choke point** — one
shared write helper (or a trigger, or a dispatcher-level check) that every one of the sources above
goes through, including the not-yet-built flag-fix routine and the not-yet-conceptualised
findings-generator path — rather than each caller being individually responsible for remembering to
log its own change. Otherwise the log inherits exactly the same silent-gap failure mode the tables
have today, just one layer further out. This is a design requirement to carry into §8/§9's shape, not
a separate open question.

---

## 6. Full previous-version text in the live tables — bulk/search-bloat question

**Live measurement, checked today (not estimated):**

| Metric | Value |
|---|---|
| `prose_section` row count | 1,040 |
| Total `body` text | ~14.05 MB (avg 13.5 KB/row, max single row 408 KB) |
| Rows that have ever been superseded (an "old" version, no longer current) | 91 (8.75% of rows) |
| Total body bytes belonging to those 91 superseded rows | ~1.0 MB (~7% of the 14 MB total) |
| `prose_section_fts` (FTS5 search index) row count | 1,040 — **every row, including all 91 superseded ones** |

**Two separate findings here, not one:**

1. **Not yet a large problem in absolute terms** — superseded-row bloat is ~1 MB today, a small
   fraction of the 14 MB total. The researcher's concern is about trajectory, not current pain: as
   editing volume grows through the analytics/publishing phase (the explicit reason this whole
   prose-management effort exists), a design that keeps every prior full-text version live and
   indexed forever will scale worse than one that doesn't. Worth designing against the trend, not
   just today's number.
2. **A real defect independent of the change-log question, found while checking this:** all 91
   superseded rows are *still fully searchable* today — `prose_section_fts` indexes every row
   regardless of `superseded_by_id`. A search can currently surface stale, no-longer-authoritative
   text alongside the current version with no way to tell them apart from the search result alone.
   This isn't something this item needs to fix by itself, but it's a concrete reason to prefer
   whichever design option below also narrows the FTS index to current rows only.

**Options for where prior-version body text lives (not decided — genuine design choice):**

| Option | Shape | Effect on current-state table | Effect on FTS/search | Effect on log/history table |
|---|---|---|---|---|
| **A — move history out** | Superseded rows are removed from `prose_section` entirely (physically, not soft-deleted) once a change-log table exists to hold them; the current-state table contains only ever-current rows. | Shrinks to ~13 MB and stays close to that going forward, not growing with edit *volume*, only with section *count*. | FTS naturally only indexes current rows — fixes finding 2 above as a side effect, no separate exclusion logic needed. | Change-log table carries the full old body text (or at minimum a diff/pointer) — grows unboundedly, but is a plain non-indexed audit table, not part of the live search surface. |
| **B — status quo, filtered index** | Superseded rows stay in `prose_section` exactly as now; only the FTS index is filtered to exclude them. | No change — keeps growing with every edit, indefinitely. | Fixes finding 2 (search hygiene) without addressing storage bloat. | No new table needed for this question specifically — but doesn't answer §2/§5's actor/reason/when gap either, so isn't a full answer on its own. |
| **C — log carries metadata + reference, not full body duplicate** | A change-log table records who/when/source/what-changed, but does NOT duplicate full body text — the old text stays exactly where it is today (in `prose_section`, per Option B) unless/until a separate, later pruning policy physically removes it. | Same growth profile as B. | Same as B unless combined with B's index filter. | Log stays small (metadata only); storage/search bloat is a separate, later problem, explicitly deferred rather than solved now. |

Recommendation, stated as a recommendation not a decision: **Option A** most directly answers the
researcher's own stated concern (bulk, search time, index bloat) and fixes the already-live FTS
defect as a side effect, at the cost of being the largest build (a real archival/migration step, not
just a new table). B and C are smaller, faster to build, but leave the growth trajectory concern
unaddressed — B only patches search hygiene, C only patches the "who/when" gap. Genuinely open for
the researcher's call, not assumed.

---

## 7. Scope — does the log need to cover insert / update / delete?

Checked live: `prose_section` already has **six** distinct write operations registered in
`apply_session_patch.py`, not just "update":

| Operation | What it does today | Currently logged anywhere? |
|---|---|---|
| `insert` | New row, version 1, no predecessor | No — first-ever state isn't recorded as a change event either, only implicitly via `created_at` on the row itself |
| `supersede` | New row (new body/version), old row's `superseded_by_id` set | Partially — only via the `version`/`supersedes_id` chain on the rows themselves (§1's "not reliably ordinal" problem); no actor/reason captured beyond `author` on the new row |
| `delete` | Soft-delete — `delete_flagged = 1` | **No** — no timestamp, no actor, no reason recorded anywhere. 59 of 1,040 rows are currently delete-flagged with zero trace of when or why. |
| `approve` | Status → `approved`, stamps `approved_at`/`approved_by` | Yes, but only the current state (no history if a row were ever un-approved and re-approved — not currently possible, but the log design should decide whether that's future-proofed) |
| `session_a_replace` | In-place body rewrite (Session A mechanical extracts only) | Timestamp only (`created_at` touched), no actor, no delta — the exact gap named in §1 |
| `bulk_supersede` | Same as `supersede`, batched across many targets in one transaction | Same gaps as `supersede`, individually per row — no record that a batch of rows changed *together* (directly relevant to §2 item 3/3a, joint-change visibility) |

`prose_section_type` has only **two** operations — `insert` and `update` — and confirmed live:
**no `delete` operation exists for it at all**, despite the table declaring a `delete_flagged`
column (currently 0/108 rows use it — the column is dead code, a separate finding, not this item's
problem to fix but worth naming plainly so it isn't lost).

**Answer to the researcher's question:** yes — the log needs to cover the realistic operation set as
it actually exists today (six ops on `prose_section`, two on `prose_section_type`), not just
"update." A design that only logs `supersede`/`update` and leaves `insert`, `delete`,
`session_a_replace`, and `bulk_supersede`'s batch-grouping uncovered would reproduce the exact
selective-coverage problem §5 already found in the current code (some write paths tracked, some
silently not).

---

## 8. Does the `version` number literally become the change-log id?

Two genuinely different answers, both viable, laid out with the escalation precedent (§3.1) as the
tiebreaker consideration:

**Option A — mirrored business column (the escalation precedent, exactly).** `version` stays its
own small integer on the current-state row (as today), and the change-log table stores that same
number as its own business column (not its PK) alongside a `UNIQUE(section_id, version)` constraint
— exactly how `escalation_history.version` mirrors `escalation.version` while `escalation_history.id`
remains a separate, independent autoincrement PK. `version` is never "the log row's id" — it's a
join key between the two tables. Cost: two numbers to keep in sync (the same class of mechanism that
produced today's mixed-type drift — `'1_0'`/`'v1'` — so the write path that maintains it must be the
single choke point named in §5, not left to each caller). Benefit: a human-readable "this is version
3 of this section" that matches how the researcher and every prior document already talk about prose
versions, and directly reuses a pattern already proven and approved in this exact project.

**Option B — the log row's own id IS the version.** Drop the separate `version` column entirely;
"how many times has this section changed" becomes a derived fact (count/rank the log rows for that
`section_id`), not a stored one. Simpler to maintain — nothing to keep in sync, no drift possible —
but loses the friendly small-per-item-counter semantics current usage expects ("version 3" becomes a
query result, not a fact you can read off the row), and log-table ids are global/monotonic across
every section, not restarting at 1 per item, so a log row's raw `id` alone doesn't mean anything
per-item without that same count/rank query — which is effectively re-deriving Option A's number on
every read instead of storing it once on write.

**Recommendation, not a decision:** lean Option A — it's the pattern this exact project already
built, tested, and approved for the identical shape of problem (§3.1), and keeps "version 3" as a
readable fact rather than a computed one. Worth deciding alongside §6 (if Option A there is chosen,
the log table already needs to exist and carry per-item data, so mirroring `version` onto it costs
nothing extra) — genuinely the researcher's call, not assumed here.

---

## 9. Columns on the two tables — relocation candidates

Every column on both tables, checked against the live schema, with a recommended disposition. "Stays"
= belongs on the current-state row regardless of what else is decided. "Move" = the historical value
belongs in the change-log table, not (only) on the live row. "Depends on §6" = the answer changes
based on which retention option is chosen there.

### `prose_section`

| Column | Disposition | Why |
|---|---|---|
| `id`, `registry_id`, `section_type_id` | Stays | Current-state identity/scope |
| `heading` | Stays (log captures prior value only when it differs) | Needed live for display/search of the current section |
| `body` — **current version** | Stays | Needed live for display/search |
| `body` — **prior versions** | **Depends on §6** | Option A (§6) moves this fully to the log table; Options B/C leave it on `prose_section` as today |
| `word_count` | Stays | Cheap to keep cached on current-state; derivable from `body` if ever dropped |
| `status` | Stays | Current-state workflow field |
| `version` | Stays (current-state), **and** mirrored onto the log per §8 Option A | Both a live-lookup fact and (if Option A) a log join key |
| `supersedes_id` / `superseded_by_id` | **Move — this pairing IS today's makeshift change log** | These self-referencing FKs on the live table are the mechanism currently standing in for a real history table; §6 Option A replaces this same-table linked-list shape with a proper log table, which is the researcher's underlying question |
| `author` | Stays (current-state: last author), **move** the full per-version trail to the log | Mirrors `escalation_history.originator` — every version's author belongs in history, not just the latest |
| `created_at` | Reframe as "current-state last-modified" (fixed to update on every write path, including `session_a_replace`); **move** the per-version creation timestamp to the log | Same treatment as `version`/`author` — one clean current-state fact, full trail in history |
| `approved_at` / `approved_by` | Stays (current-state) | Needed live for workflow; log coverage of the `approve` operation itself is a §7 scope question, not a column-relocation one |
| `metadata_json` | Stays, review case-by-case | Free-form; likely still relevant to current state |
| `source_file` | Stays **and** feeds the log's "where it came from" field | Already proven (§1) not to equal one change event on its own — the log needs to record it per change-event, not rely on it alone to define the event |
| `delete_flagged` | Stays (current-state) | But per §7, the delete *event* (who/when/why) needs logging — currently has no trace anywhere, live or historical |
| `cluster_code`, `characteristic_id`, `cluster_subgroup_id` | **Not this item's relocation** | Already flagged by #829 D5/D6 as belonging to a *future index/Concordance table* — a different relocation, for a different reason (citation columns, not change-history) — noted here only so the two aren't conflated |

### `prose_section_type`

| Column | Disposition | Why |
|---|---|---|
| `id`, `code`, `label` | Stays | Current-state identity |
| `source_stage`, `lifecycle_tag`, `description`, `expected_length_min`/`max` | Stays (current-state); **move** — every change to these is currently a silent in-place `UPDATE` with no version/timestamp/actor at all (§5), so the log needs a matching entry regardless of which specific field changed | This table has no supersede-only discipline at all — everything mutable is update-in-place, so the log's job here is fuller than for `prose_section` |
| `chapter_no`, `sort_order`, `book_order`, `book_label`, `section_order`, `section_label` | Stays (current-state); **move** | These are exactly the "chapter sequence, paragraph sequencing, book names" fields the researcher named directly — structural/navigational, currently the least-traced fields in the whole prose store |
| `delete_flagged` | Stays (declared, unused) | Confirmed live: no code path sets it at all — a real, separate gap (dead column), not this item's fix, named so it isn't lost |
| `created_at` | Reframe as "last-modified," same treatment as `prose_section.created_at` | Currently row-creation-time only; needs the same fix |

---

## 10. Still open, carried forward

- §6 (bulk/retention: A/B/C) and §8 (version-number shape: A/B) are the two genuine either/or
  decisions this round surfaces — both recommended, neither assumed.
- Everything from v1 §4 remains open (log-table shape overall, real change-event unit if not
  `source_file`, joint-change linking across both tables, relationship to #833/#829 §12.7).
- Not yet addressed: whether `approve` and the future flag-fix/findings-generator sources (§5) need
  their own distinct log-entry "reason" vocabulary, or share one open-text/enum field with
  `supersede`/`update`/`delete` — worth deciding once the log table's own shape (§6/§8) is settled,
  not before.
