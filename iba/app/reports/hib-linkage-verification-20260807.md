# HIB table data — linkage verification (2026-08-07)

> Full data dump of the `hib` table family, live rows only unless noted, showing the FK chain
> retrofitted this session (`BUILD.md` §79): `hib` ← `verse_hib` → `verse`; `hib` ← `phenomenon` →
> `operation` → `operation_party` (→ `hib` again, the new link). Queried directly against
> `iba/app/db/iba.db`, not reconstructed from a report.

## 1. Live `hib` register — 8 rows (book: Dan)

| id | label | kind | first_verse | created_at |
|---|---|---|---|---|
| 23 | Belshazzar | named_individual | Dan.8.1 | 2026-08-06T16:18:07Z |
| 24 | the kings of Media and Persia | named_collection | Dan.8.3 | 2026-08-06T16:18:07Z |
| 25 | the king of Greece | named_individual | Dan.8.5 | 2026-08-06T16:18:07Z |
| 26 | the first king | unnamed_individual | Dan.8.5 | 2026-08-06T16:18:07Z |
| 27 | the four kingdoms | unnamed_collection | Dan.8.8 | 2026-08-06T16:18:07Z |
| 28 | the bold-faced king | unnamed_individual | Dan.8.9 | 2026-08-06T16:18:07Z |
| 29 | the people who are the saints | unnamed_collection | Dan.8.24 | 2026-08-06T16:18:07Z |
| 47 | Daniel | named_individual | Dan.8.1 | 2026-08-07T14:22:49Z |

**History (not shown above, `deleted=1`):** 39 further `hib` rows — correction history from prior
Dan 8 debate reconciliation passes. Total table: 47 rows. Confirms the soft-delete convention is
doing real work, not just declared.

## 2. `hib` → `verse_hib` → `verse` (which verses each HIB is present in)

| hib_id | label | verse count | verses (osisId) |
|---|---|---|---|
| 23 | Belshazzar | 1 | Dan.8.1 |
| 24 | the kings of Media and Persia | 5 | Dan.8.3, Dan.8.4, Dan.8.6, Dan.8.7, Dan.8.20 |
| 25 | the king of Greece | 5 | Dan.8.5, Dan.8.6, Dan.8.7, Dan.8.8, Dan.8.21 |
| 26 | the first king | 3 | Dan.8.5, Dan.8.8, Dan.8.21 |
| 27 | the four kingdoms | 2 | Dan.8.8, Dan.8.22 |
| 28 | the bold-faced king | 7 | Dan.8.9, Dan.8.10, Dan.8.11, Dan.8.12, Dan.8.23, Dan.8.24, Dan.8.25 |
| 29 | the people who are the saints | 1 | Dan.8.24 |
| 47 | Daniel | 17 | Dan.8.1-8.5, 8.6, 8.7, 8.13-8.20, 8.26, 8.27 |

## 3. `hib` → `phenomenon` → `operation` (Step 3/4-5 coverage per HIB)

| hib_id | label | live phenomena | live operations | operation decisions |
|---|---|---|---|---|
| 23 | Belshazzar | 1 | 1 | recorded_silence ×1 |
| 24 | the kings of Media and Persia | 5 | 5 | recorded_silence ×1, retain ×4 |
| 25 | the king of Greece | 5 | 5 | retain ×5 |
| 26 | the first king | 3 | 3 | retain ×3 |
| 27 | the four kingdoms | 2 | 2 | retain ×2 |
| 28 | the bold-faced king | 7 | 7 | retain ×7 |
| 29 | the people who are the saints | 1 | 1 | retain ×1 |
| **47** | **Daniel** | **0** | **0** | — |

**Daniel (id 47) has verse coverage but no phenomena/operations yet** — added 2026-08-07 (a day
after the other 7), `phenomenon.set` hasn't been run for it. Not a bug; the chain correctly shows
this HIB as not yet advanced past Step 1, exactly what the traceability fix is supposed to make
visible rather than silently absent.

Every phenomenon that exists has exactly one operation (24/24 = 100%, matches `phenomena_complete_at`
being set and `closing.set`'s own completeness gate).

## 4. `hib_referent_option` — 0 live rows (all 5 are correction history)

| id | hib_id (now superseded) | reading_text (the referent-crux reading) | adopted |
|---|---|---|---|
| 1 | 12 (dead — superseded by 24) | the kings of Media and Persia | 1 |
| 2 | 13 (dead — superseded by 25) | the king of Greece | 1 |
| 3 | 14 (dead — superseded by 26) | the first king (of Greece) | 1 |
| 4 | 15 (dead — superseded by 27) | four kingdoms arising from his (Greece's) nation, but not with his power | 1 |
| 5 | 16 (dead — superseded by 28) | a king of bold face, skilled in intrigue, who arises at the latter end of the [four kingdoms'] rule | 1 |

These 5 were written against an earlier `hib` id generation, before the id-preserving `changed`
fix landed today — each one's owning `hib` row was corrected at least once under the OLD
(new-id-per-correction) behaviour, which is exactly why they're orphaned-looking now (their
`hib_id` points at a dead row). Going forward, a `changed` correction preserves the `hib` id, so a
`hib_referent_option` written today will stay attached to the same live `hib` row across future
corrections instead of accumulating dead links like these five.

## 5. `operation_party.hib_id` — the new FK this session added (Finding 2)

**4 parties structurally linked to a live HIB, backfilled from exact `detail`↔`hib.label` matches:**

| operation_id | operation's own verse | owning HIB | party role | detail (free text, kept) | linked HIB (via `hib_id`) |
|---|---|---|---|---|---|
| 69 | Dan.8.6 | the king of Greece | target | the kings of Media and Persia | **the kings of Media and Persia** |
| 72 | Dan.8.7 | the king of Greece | target | the kings of Media and Persia | **the kings of Media and Persia** |
| 93 | Dan.8.24 | the bold-faced king | target | the people who are the saints | **the people who are the saints** |
| 94 | Dan.8.24 | the people who are the saints | source | the bold-faced king | **the bold-faced king** |

Rows 93/94 show the mirror-consistency check (`hib-fanout-dimensions` dimension B, technical
reference §3 Step 4-5) working exactly as intended: the bold-faced king's operation names "the
people who are the saints" as target, and that HIB's own operation names "the bold-faced king" back
as source — now both traceable by `hib_id`, not just by matching prose.

**5 human parties still `hib_id=NULL` — correctly left unlinked, not a residual gap:**

| detail | why not linked |
|---|---|
| the king of Greece, as agent of the defeat | descriptive phrase, not an exact `hib.label` match |
| the first king, as the one whose reign ends here | descriptive phrase, not an exact match |
| the first king, in whose place they arise | descriptive phrase, not an exact match |
| one of the four kingdoms, his point of origin | descriptive phrase, not an exact match |
| the first king, as the nation of origin | descriptive phrase, not an exact match |

These all clearly refer to HIBs 25/26/27 by *sense*, but the backfill deliberately used exact-label
matching only — inventing a fuzzy link here would be fabricating data the original analytical pass
never explicitly asserted. Correcting these (adding `hib_label` to each on a future `operation.set`
`changed` payload) is real remaining work, not something this session's retrofit was positioned to
guess at.
