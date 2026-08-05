# B3 + B5 — phenomena/operations DB schema + working-record control, design proposal

**Date:** 2026-08-05. **Status: design only — nothing built.** Per the digest's own failure-mode
(a) ("don't do everything at once") this is deliberately scoped to the schema + control-gate design
— the write-mechanism question at the end is flagged, not resolved, and B4 (passage-boundary
redefinition) stays a separate pass even though it consumes one of these tables.

## Grounding

Digest steps this schema exists to serve: Step 1 (HIB identification), Step 3 (phenomena register,
with its phase-gate control question), Step 4-5 (operations + description), Step 7 (closing
sections), and B5's own "list of passages; list of HIBs; list of phenomena; control totals" —
answered here as **computed on demand from these tables**, not a separately-maintained file kept in
sync by hand. Same principle as `verse_lexical`/`report.verse_lexical`: DB is the source of truth,
any Markdown is a generated view, never itself written to directly.

## Core tables (Step 1, 3, 4-5 — the actual analytical record)

**`hib`** — one row per Human Inner Being identified in a scope (Step 1's scope-wide sweep, not
passage-scoped — the same HIB, e.g. "Daniel," recurs across many passages of a book).

| column | type | notes |
|---|---|---|
| id | INTEGER PK | |
| book | TEXT | OSIS code, same convention as `verse.osisId`'s book segment |
| label | TEXT | e.g. "Daniel", "the four youths", "King Belshazzar" |
| kind | TEXT | `named` \| `collective` \| `referential` (Step 1: presumptive-candidate / collective / referential rules) |
| first_verse_id | INTEGER FK verse.id | anchor — where first identified |
| created_at | TEXT | |
| deleted | INTEGER | version-aware soft-delete, standard convention |

**`hib_referent_option`** — child of `hib`, only populated for genuinely ambiguous referents (T4):
every grammatically-live reading considered, not just the one adopted.

| column | notes |
|---|---|
| id, hib_id (FK) | |
| reading_text | the candidate reading, e.g. one option for "we" in Obad 1 |
| textual_grounds | why this reading is live |
| adopted | boolean — exactly one `true` per `hib_id` (the explicit choice, Step 1's "adopt one explicitly") |
| ordinal, created_at, deleted | |

**`verse_hib`** — one row per HIB actually present/candidate in a given verse (Step 1's per-verse
sweep). This is the table both the phenomena-register control total (below) **and** B4's future
passage-boundary computation read from — a HIB-continuity boundary is exactly "where the set of
`verse_hib` rows for consecutive verses stops overlapping."

| column | notes |
|---|---|
| id, verse_id (FK), hib_id (FK) | |
| created_at, deleted | |
| — | `cfg_unique (verse_id, hib_id)` |

**`phenomenon`** — the phenomena register itself (Step 3 output), one row per HIB per verse (an
`ordinal` allows more than one phenomenon for the same HIB in the same verse, since v1.5 step3
note c doesn't rule it out, just says each must be justified in its own right).

| column | notes |
|---|---|
| id, passage_id (FK passage.id), verse_id (FK), hib_id (FK) | |
| description | the phenomenon: a state, disposition, or characteristic |
| textual_warrant | the verb/clause/stated-silence that grounds it (step 3b) |
| status | `stated` \| `inferred` \| `silent` — "no phenomenon found, silent" is itself a valid row (Part B.4), never an omitted one |
| ordinal, created_at, deleted | — `cfg_unique (passage_id, verse_id, hib_id, ordinal)` |

**`operation`** — Step 4-5 output. **`phenomenon_id` is `NOT NULL`** — this is the actual DB-level
enforcement of Part B.12 ("an operation may only originate from an already-registered phenomenon"):
there is no way to write an operation row without a real phenomenon row to hang it from.

| column | notes |
|---|---|
| id, phenomenon_id (FK phenomenon.id, NOT NULL) | |
| process | text — state/status, or a movement (come from/go to/impact on/emerge/go away/become evident) |
| action_type | short verb-based label (Q11) — a label, not a controlled vocabulary (Part B.10) |
| decision | `retain` \| `set_aside` \| `retain_referential` \| `recorded_silence` |
| observation_text | what the text/span-data states, Strong's codes cited |
| description_text | Step 5's descriptive write-up |
| created_at, deleted | |

**`operation_party`** — child of `operation`, one row per source/target (plural-capable: v1.5 step1
note a — "the source and target could be singular, multiple, mixed or non existent" — a flat
source/target column pair on `operation` itself couldn't hold that).

| column | notes |
|---|---|
| id, operation_id (FK) | |
| role | `source` \| `target` |
| kind | `self` \| `human` \| `non_human` \| `object_situation` \| `none` |
| detail | text — which human/object, if named |
| enablement_only | boolean, `source` rows only — Part B.5's state-vs-enablement distinction, kept structurally separate rather than folded into `kind` |
| ordinal, created_at, deleted | |

## Closing-section tables (Step 7) — lighter tier, deliberately simpler

These carry less structured weight than the core four — mostly short prose pinned to a passage (and
sometimes a specific operation), not multi-part records. Proposing them, but they're the easiest
thing to cut from this pass if you'd rather they stay MD-only prose in the rendered report for now:

- **`passage_linkage`** (passage_id, from_operation_id FK, to_operation_id FK, note) — Q7.
- **`passage_insufficiency`** (passage_id, verse_id nullable FK, note) — Q9/Part B.7.
- **`passage_emergent_question`** (passage_id, verse_id nullable FK, question_text, kind:
  `interpretive_fork` \| `literary_structural` \| `other`) — Q10/Part B.9/B.12 (T5's genre
  observations land here too).
- **`passage_validation_note`** (passage_id, phenomenon_id nullable FK, finding_text, corrected
  boolean) — Phase 3/step 6.
- "Open decisions / next steps" — proposing this stays a single free-text column on `passage`
  itself (`passage.open_decisions_note`) rather than its own table; it's normally short prose, not
  a repeating structured list.

## The Step 3 control gate (this is what "how does phase separation get controlled" actually cashes out to)

One new column: **`passage.phenomena_complete_at`** (TEXT, nullable UTC timestamp). `NULL` until
Phase 1 is confirmed complete for the whole passage; set only by an explicit control-check (not by
trust) that compares `COUNT(phenomenon WHERE passage_id=?)` — allowing for `ordinal`, i.e. distinct
`(verse_id, hib_id)` pairs covered — against `COUNT(verse_hib)` for every verse in the passage. Any
`operation` write is **blocked in code** (a `_may`-style guard, same shape as every other write-grant
check in this app) when `passage.phenomena_complete_at IS NULL` for that operation's passage — Step
4 genuinely cannot start early, not just "shouldn't."

**No other counters are stored.** Expected/actual counts for HIBs, phenomena, and operations are
always computed live from `verse_hib`/`phenomenon`/`operation` — deliberately not cached into
redundant columns that could drift out of sync with what's actually in the tables. This is also
what B5's "working record" collapses into: **a report, not a file to maintain** — `report.
passage_control` (name open to bikeshedding), rendered on demand, listing the passage's HIBs, its
verse×HIB control total, current phenomena/operations counts, any `verse_hib` pair with no matching
`phenomenon` row (a visible gap — directly answers failure-mode (d), "not following all the
sub-processes"), and whether the phase gate is set. Readable at any point without re-deriving state
from memory (failure-mode (e)) — same shape as every other on-demand report this session built.

## Governance path

Same carve-out class as `verse_lexical` (BUILD.md §56/§59): new tables are DDL, so a direct,
documented, idempotent migration (not row-by-row `configmaint.propose`) — this design document,
once you've reviewed it, is the up-front approval that carve-out requires. `cfg_table`/`cfg_column`
registered for all nine tables + the one new `passage` column; `cfg_write_grant` for whichever
step(s) end up writing them (see below); `cfg_unique` for the two natural keys named above.

## Flagged, not resolved: how does an analytical pass actually get written into these tables?

Every table above holds **analytical content** — an AI/researcher's judgment (what phenomenon, what
process, what decision), not a mechanically-derivable value the way `verse_lexical` was. This app
has no existing mechanism for "AI analytical output → validated DB write" (the main Bible-study
programme, `Sessions/Patches/`, has one — a JSON-patch pattern applied via `apply_session_patch.py`
— but nothing equivalent exists yet in `iba.db`). Two shapes worth naming, not choosing between yet:

1. **A registered write step** (`hib.set`, `phenomenon.set`, `operation.set` or similar) taking
   structured params/JSON, validated and grant-checked like every other write in this app —
   consistent with how everything else here works, but means designing a real input contract for
   each.
2. **A lighter patch-style ingestion**, closer to the main programme's own pattern — a JSON file
   the analysis pass produces, applied by one script that validates against the phase gate and
   write grants before committing.

Not resolved here — this is the next real decision once the schema itself is confirmed, and it's
where B4 (passage creation/update wired into the debate process) and this schema actually meet: the
write mechanism needs to know which `passage_id` an operation belongs to, which only exists once a
passage has been created under the redefined (HIB-continuity) boundary rule.
