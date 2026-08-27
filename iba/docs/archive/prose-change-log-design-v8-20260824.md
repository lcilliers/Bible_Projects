> **Superseded by [prose-change-log-design-v9-20260824.md](prose-change-log-design-v9-20260824.md).**
> Kept on disk for history only.

# Prose change log design — versioning integrity (#836)

Supersedes: [prose-change-log-design-v7-20260824.md](prose-change-log-design-v7-20260824.md) (v1–v7
kept on disk for history). Researcher answers this round (2026-08-24): table name settled
(`record_change_log`), findings-integration confirmed deferred, `batch_id` drop confirmed, and a
concrete migration instruction given. One direct question back — *"I thought we resolved how the
payload works... am I missing something?"* — surfaced a real inconsistency worth correcting, not a
misunderstanding on the researcher's part.

---

## 28. Decisions recorded, no longer open

| Item | Answer |
|---|---|
| Table name | **`record_change_log`** |
| Findings integration | **Confirmed deferred** — "will be dealt with when work on findings start." No action here. |
| `batch_id` | **Confirmed dropped.** Field list no longer carries it (§31). |

---

## 29. Migration — the researcher's instruction, plus one gap it doesn't cover

Researcher's instruction, verbatim: *"the 91 existing superseded sections are written out to the log
table to capture the history and then removed from the prose tables (hard deleted)."* Recorded as the
migration plan for those 91 rows — write each one's content to `record_change_log` as its own row,
then hard-delete it from `prose_section`. Matches Model A cleanly (§10) — once migrated, `prose_
section` genuinely contains current rows only, no exceptions.

**One thing this instruction doesn't cover, worth naming before treating migration as fully planned:**
the 91 superseded rows aren't the only ones that need a `record_change_log` entry. Every row that
*isn't* being removed also needs one — because `version` is being redefined as a literal pointer to a
`record_change_log.id` (§18/§23), and a row can't carry a valid `version` value pointing at nothing.
Concretely:

- The **949 currently-live `prose_section` rows** (1,040 total − 91 superseded) each need one
  baseline `record_change_log` row created at migration time, so their new `version` column has a
  real id to point at from day one.
- **All 108 `prose_section_type` rows** — which have never had any version/history concept at all —
  need the same baseline treatment, since §12 gives that table a `version` column for the first time.

These baseline rows aren't really "a change" in the sense the rest of this design has been describing
(insert/change/delete against a live event) — they're recording "this is what the row already
contained when the log started existing." Proposing `change_reason = 'migration baseline'` (or
similar) for exactly this batch, so they're honestly distinguishable from real future change events
rather than dressed up as one. Flagging this as an addition to the migration plan, not something the
instruction above already covered — confirm it's wanted, or correct the reading if the 949/108 rows
were meant to start with `version` left NULL instead (workable too, just a different, equally valid
choice, not assumed here).

---

## 30. The payload question — a real correction, not a misunderstanding

Direct answer to *"am I missing something?"*: no — the JSON-for-the-record concept itself was right
and settled in v7 §24. But re-checking it against §29's migration instruction surfaced a real
ambiguity this document had left unresolved: **does the payload capture the state going *into* the
change (what's being overwritten), or the state coming *out of* it (what the row's content actually
is at that version)?**

v7 §24 loosely described payload as "that one target row's relevant *prior-state* fields" —
prior-state language carried over from v4 §13's design, which was written for the old Model-B-style
picture (a history row capturing what got superseded). That framing is backwards for how this design
actually works now: with `version = record_change_log.id`, the log's job is "one row's content, per
version," not "a shadow of what got replaced." **Corrected: payload holds the *resulting* state — the
row's content as of that specific version/event**, not what came before it. This is also exactly what
§29's migration needs: the 91 superseded rows' payloads should be *their own* content (what that
version actually said), not the version before them — which only makes sense under the resulting-state
reading. Under an `insert`, there's no "prior state" to log anyway, so resulting-state is the only
reading that works uniformly across `insert`/`change`/`delete`.

Nothing else in v7 changes — this corrects one sentence's framing, not the shape of the design.

---

## 31. Final field list — `record_change_log`

| Field | Source |
|---|---|
| `id` | Own PK — the `version` value written onto a target row |
| `target_table`, `target_id` | Needed for "across tables and rows" to work mechanically |
| `change_type` | `insert` / `change` / `delete` |
| `change_datetime` | System-applied time (§18) |
| `change_source` | File name, or originating script/module |
| `change_reason` | Population rule per §18; `'migration baseline'` for the §29 backfill rows |
| `changed_by` | Who/what executed the change |
| `status` | `change_proposed` / `change_applied` / `declined` |
| `payload` | Gzip-compressed JSON — the row's **resulting** content at that version (§30) |

`batch_id` — dropped (§28). No other fields outstanding.

---

## 32. Still open

- §29's migration addition (baseline rows for the 949 live `prose_section` rows + all 108 `prose_
  section_type` rows) — confirm wanted, or correct if `version` should start `NULL` for those instead.
- Diff-based storage for `payload` (v5 §16.2) — still a named future option, not scheduled.
- §25's findings-integration choice — explicitly parked, not this item's decision.
