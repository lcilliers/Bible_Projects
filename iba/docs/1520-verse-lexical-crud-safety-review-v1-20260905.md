# Window 1 verse-lexical CRUD safety review — findings and proposed fix

**2026-09-05.** Triggered by escalation #1520 (Rom.9.14 orphaned notes) and the researcher's direct
follow-up: *"I get the impression you built a badly design high risk CRUD process for the lexical
with a high risk of duplicates, orphans and inconsistencies."* That #1520 fix (a precheck in
`VerseLexical.ps1`) only closed one symptom at one entry point. This traces the actual write paths
and schema to find what's structurally wrong, not just what broke once.

## What's actually sound

`verse_lexical` has a real DB-level guard against true duplicates:

```
idx_verse_lexical_live_unique : UNIQUE INDEX ON verse_lexical (span_id, code_ordinal) WHERE deleted=0
```

Two live rows for the same code slot is already impossible at the database level, not just by
application discipline. **Duplication is not the live risk. Orphaning and silent inconsistency are.**

## Root cause 1 — `write_readings_for_span` always churns ids, even on a genuine no-op

`iba/app/lib/lexical.py:write_readings_for_span` — the ONE write path for `verse_lexical`, reached
from every caller (`build_for_verse` → `build_for_range` and `build_for_verse_ids`, i.e. every
book/range build AND the per-word `new-word` rebuild chain):

```python
existing = conn.execute(
    "SELECT id FROM verse_lexical WHERE span_id=? AND code_ordinal=? AND deleted=0", ...)
if existing:
    conn.execute("UPDATE verse_lexical SET deleted=1 WHERE id=?", (existing["id"],))
    c["superseded"] += 1
conn.execute("INSERT INTO verse_lexical (...) VALUES (...)", ...)
```

No comparison against the existing row's content. The docstring says this out loud: *"always,
even when content is unchanged, so created_at reflects the last run that confirmed it — cheap;
verse_lexical is not high-write-volume."* That reasoning was fine in isolation — it stopped being
fine the moment Layer 2 (`verse_lexical_note`) started holding a durable FK into `verse_lexical.id`,
and nothing was ever updated to account for that. **This is the actual root cause of #1520**, not
a defect in the one PS1 script that happened to trigger it — any caller of `lexical.build`,
including the per-word rebuild chain, reproduces it on any verse that already has Layer 2 notes.

## Root cause 2 — `verse_lexical_note` has zero orphan protection, and a wider blast radius than one verse

```
verse_lexical_note.verse_lexical_id          -- FK -> verse_lexical.id, plain, no ON DELETE
verse_lexical_note.target_verse_lexical_id   -- FK -> verse_lexical.id, plain, no ON DELETE
verse_lexical_note.related_verse_lexical_ids -- TEXT (JSON list of ids), no FK at all
```

Three problems stacked here:

1. Even where a real FK exists, SQLite's default is `NO ACTION`, and it's moot anyway because
   nothing here does a real `DELETE` — superseding is `UPDATE ... SET deleted=1`, which no FK
   constraint ever fires on. The schema cannot catch this class of break; nothing can, short of
   explicit application logic.
2. `related_verse_lexical_ids` is a bare JSON blob with no FK at all — not even a theoretical
   constraint stands between it and staleness.
3. **The blast radius is bigger than "this verse's own notes."** `target_verse_lexical_id` and
   `related_verse_lexical_ids` let a note anchored on verse A point at a `verse_lexical` row on
   verse B (a `related_word`/cross-verse `entity_link` typically will). Rebuilding verse B's Layer
   1 — for any reason, including a genuine correction — silently breaks verse A's note too, and
   nothing surfaces that: verse A's own reconciliation check never touches verse B's rebuild at
   all. #1520's fix (a same-verse precheck in one script) does not see this at all.

## Root cause 3 — reconciliation is keyed on the churning id itself, not a stable key

`iba/app/lib/lexicalenrich.py:_reconcile` classifies every incoming note against the block's
current live state by key **`(verse_lexical_id, note_type)`**. But `resolve_verse_lexical_id`
(used to build the *incoming* side) resolves a payload note by the stable natural key
**`(verse_id, position, code_ordinal)`** — deliberately, so a payload written once still resolves
correctly after a rebuild. The mismatch: once Layer 1 churns, `_reconcile`'s "current" dict is
still keyed on the OLD dead id, the "incoming" dict is keyed on the NEW live id, and they can never
intersect — every existing note reads as neither `unchanged` nor `changed`, only as
`unreconciled`/lost, and a resubmitted identical payload comes back as all-`new`. This is exactly
what #1520 showed live, and it's why the repair required a delete-and-reinsert rather than the
reconciler recognising "this is the same note, just re-pointed" on its own.

## What #1520's fix actually covered, and what it doesn't

The `VerseLexical.ps1` precheck (`layer1_state`, BUILD.md #234) stops the *unnecessary* case: it
won't auto-rebuild Layer 1 for a verse that already has it, by default. It does **not** protect:

- A **genuine** content-driven rebuild of a verse that already has notes (real correction to
  `strong_meaning_parsed`, a span re-segmentation, etc.) — `-ForceRebuild` still only warns, it
  doesn't prevent or repair the orphaning.
- `lexical.build` invoked any other way — directly via `python -m iba.app.run`, or via the
  per-word `new-word`/`raw.lexical` rebuild chain (`build_for_verse_ids`), which has no precheck
  at all.
- Cross-verse `target_verse_lexical_id`/`related_verse_lexical_ids` references from OTHER verses
  into the one being rebuilt.

So the researcher's read is correct: what's shipped so far treats one symptom at one call site,
not the mechanism.

## Proposed fix — scoped, at the two actual write paths, not a rewrite of the versioning convention

The soft-delete-and-reinsert convention itself is the established house style for these
audit-trailed tables (`verse`/`span`/`strong` all do the same) and doesn't need replacing. The fix
is to make the two write paths that touch it *aware of what depends on the id being churned*,
which they currently are not at all.

**A. Content-diff before supersede (`write_readings_for_span`)** — the actual root fix, and it
covers every caller automatically, not just one script. Compare the freshly resolved row's content
fields against `existing`'s stored values; if identical, leave `existing` untouched (same id, same
`created_at`) and skip the delete+insert entirely. This alone removes the id churn from the common
case — most rebuilds re-confirm already-correct data and currently mint new ids for no reason.

**B. When a row genuinely must be superseded and something depends on its id — repoint, don't
orphan.** In the same transaction as the supersede, before soft-deleting `existing`:

```sql
UPDATE verse_lexical_note SET verse_lexical_id=:new_id
  WHERE verse_lexical_id=:old_id AND deleted=0;
UPDATE verse_lexical_note SET target_verse_lexical_id=:new_id
  WHERE target_verse_lexical_id=:old_id AND deleted=0;
-- related_verse_lexical_ids: read/patch the JSON list the same way, same WHERE shape
```

This is the semantically correct move, not just a safety patch: the note's analytical content
didn't change — only the mechanical Layer 1 row underneath it moved. Repointing preserves note
history (id, `created_at`) intact; nothing needs re-entering. Covers the cross-verse case too,
since the `UPDATE` isn't scoped to "notes on this verse" — it's scoped to "notes pointing at this
exact id," wherever they live.

**C. Fix `_reconcile`'s identity key** to the same stable natural key
`resolve_verse_lexical_id` already uses — `(verse_id, position, code_ordinal, note_type)` — instead
of `(verse_lexical_id, note_type)`. With B in place this mostly stops mattering (ids won't be
dangling), but it's the correct fix in its own right and removes the last place a churn could still
produce a false reconciliation failure.

**D. A cheap standing integrity check**, worth adding regardless of A-C landing:
`verse_lexical_note` rows whose `verse_lexical_id` (or `target_verse_lexical_id`) points at a
`deleted=1` row should always be zero. One query, run it now to confirm the corpus is currently
clean beyond Rom.9.14, and it's worth a permanent home (an existing quality-check pass, if one
already sweeps `verse_lexical_note`, or a new one-off if not) so a future regression surfaces on
its own rather than via a failed `enrich` call.

## Resolution — implemented 2026-09-05, same day

The researcher's response to the A-vs-B framing above: *"No use for you to ask me to select
between A or B. You should [k]now what a proper CRUD system with proper controls look like, that
is what I approved, not selection [of] one or other cop out."* Correct — repoint-after-supersede
was still a workaround bolted beside the actual defect, not a fix of it. Implemented instead:

**`write_readings_for_span` redesigned to be identity-stable**, not "supersede with a repoint
step." This wasn't invented from scratch — it applies a principle this exact codebase had already
worked out correctly elsewhere and simply never carried over here:
`handlers/operations.py:phenomenon_set` already does real in-place `UPDATE` for a changed
`phenomenon` row, specifically *because* `phenomenon.id` has a downstream FK dependent
(`operation.phenomenon_id`) — its own docstring names that as the reason. `verse_lexical` is in
exactly that position via `verse_lexical_note` and was never updated to match.

Per `(span_id, code_ordinal)` slot, per rebuild:

| case | action | id |
|---|---|---|
| no live row yet | INSERT | fresh (correct — genuinely new) |
| live row, content identical | **nothing written** | unchanged |
| live row, content differs | real `UPDATE ... WHERE id=?` | **unchanged** |
| live row, slot no longer exists (span shrank) | soft-delete | gone (the one legitimate case) |

A small additive migration (`migration/add_verse_lexical_updated_at_v1_20260905.py`) added
`verse_lexical.updated_at`, nullable — replaces the old design's stated reason for churning every
id ("so `created_at` reflects the last run that confirmed it") without requiring the id to move to
get that signal.

**What this collapses, not just patches:**

- **Root cause 1 (unnecessary churn on no-op)** — gone. A rebuild of already-correct data now
  writes nothing.
- **Root cause 2 (orphaning on a genuine content change)** — gone. The id never moves, so
  `verse_lexical_note.verse_lexical_id`/`target_verse_lexical_id` never go stale from an UPDATE
  path, same-verse or cross-verse, from any caller (`build_for_range` OR the per-word
  `build_for_verse_ids` chain — both go through the same one write path now).
- **Root cause 3 (reconciliation keyed on the churning id)** — moot as a side effect, no separate
  code change needed: `_reconcile`'s `(verse_lexical_id, note_type)` key only ever broke because
  the id used to move out from under it; with the id stable, it matches correctly on its own.
- **The genuine-removal case** (a slot really disappearing) still soft-deletes for real — correctly,
  since there's nothing to preserve — but now counts and reports `removed_with_live_notes` rather
  than leaving a live note to dangle silently. Wired into `report.lexical_exceptions` as a real
  standing integrity section (0 expected always), not left as a one-off query someone has to
  remember to run — pending researcher approval for its `cfg_report_section` row (escalation
  #1522; the section still renders via the existing unregistered-section fallback until then).

**Verified live, not just argued:** backed up `iba.db`; ran the corpus-wide orphan check clean
before touching anything (0 across all three FK directions); force-rebuilt `Rom.9.14` with no
content change — result `0 inserted, 0 updated, 9 unchanged, 0 removed`, ids and the 9-code set
byte-identical to before; deliberately corrupted one live row's `resolved_sense` and rebuilt again
— result `1 updated`, same `id` (975452), `created_at` untouched, `updated_at` newly stamped,
content correctly restored, and the note already attached to that row (id 492) required zero
re-run, zero reconciliation, zero manual repair. Then force-rebuilt all 10 of this session's review
verses the same way — 9 came back all-unchanged, `Prov.31.30` had one genuine field difference
(`1 updated`), and the orphan sweep across all 10 came back 0 both before and after. Two
downstream message strings (`handlers/lexical.py:build`, `handlers/raw.py`'s per-word rebuild path)
that read the old `inserted`/`superseded` count keys were found and fixed in the same pass — would
otherwise have thrown `KeyError` on first use.

**Files:** `iba/app/lib/lexical.py` (`write_readings_for_span`, `build_for_verse`,
`build_for_range`, `build_for_verse_ids`, module docstring), `iba/app/handlers/lexical.py` (build
message), `iba/app/handlers/raw.py` (per-word rebuild message), `iba/app/handlers/reports.py`
(`lexical_exceptions_report`'s new integrity section), `iba/app/migration/
add_verse_lexical_updated_at_v1_20260905.py`.
