# Finding-table landscape — full inventory, the `wa_finding_catalogue_links` question, and normalisation

Triggered by: three "finding"-named tables visible in today's catalogue extract
(`cluster_finding`, `finding_question_link`, `wa_finding_catalogue_links`) — are there more, is
`wa_finding_catalogue_links` really an index table, and can the real findings tables be normalised
into one.

## 1. Full inventory — 10 tables, not 3

A live sweep (`name LIKE '%finding%'`) turns up 10, not the 3 visible in the catalogue extract.
Split by what they actually are, not what their name implies:

**Content tables — hold the actual finding text/value:**

| table | rows | status |
|---|---|---|
| `finding` | 438,099 | **live** — the current universal store (`finding_value`) |
| `cluster_finding` | 19,997 | legacy, real content (`finding_text`), frozen since 2026-06-19 |
| `wa_session_b_findings` | 2,883 | legacy, real content (`finding`), **already migrated** into `finding` |

**Link/junction tables — map a finding to something else, no independent content of their own:**

| table | rows | links | resolves cleanly? |
|---|---|---|---|
| `finding_question_link` | 332,204 | finding ↔ question (live) | 100% (332,204/332,204 into `finding`) |
| `wa_finding_catalogue_links` | 6,199 | finding ↔ question (legacy) | 88% (5,456/6,199 into `wa_session_b_findings`) — **see §2** |
| `finding_citation` | 51,148 | polymorphic evidence citation | 100%, but only ever `cluster_finding`/`cluster_observation` — **never** the live `finding` table |
| `finding_verse_link` | 3,659 | finding ↔ verse | — |
| `wa_finding_entity_links` | 287 | finding ↔ arbitrary entity (legacy) | 100% (287/287 into `wa_session_b_findings`) |
| `finding_revision` | 0 | finding field-change audit trail | unused |
| `prose_section_finding_link` | 0 | prose section ↔ finding | unused |

## 2. Is `wa_finding_catalogue_links` really an index table? No — you read it right

Its schema (`finding_id`, `question_id`, `coverage`, `status`, `session_b_note`) *looks* like a
plain link. Checked what's actually in it:

- **6,169 of 6,199 rows (99.5%) carry a populated `session_b_note`** — and that field holds a full
  analytical write-up, not a coverage annotation. Sample (id=1):
  > "Goodness originates in God — this is stated explicitly in the registry description (OBS-001)
  > and confirmed by the verse evidence. Psa 119:68 (OBS-026) models the being/doing relationship
  > at the divine level... Mic 6:8 (OBS-027, OBS-028) confirms this — 'He has told you, O man, what
  > is good' positions the definition of goodness as divinely revealed, not humanly generated."
- **Only 3,232 distinct `session_b_note` texts exist across the 6,199 rows** — the same
  finding write-up is copied verbatim onto every `(finding_id, question_id)` pairing it was judged
  to satisfy, rather than stored once and referenced. Rows 1–5 in the sample above are four
  *different* `finding_id`s carrying the *identical* note for the same question.
- Its `finding_id` only resolves into `wa_session_b_findings` for 5,456/6,199 rows (88%) — a real,
  separate integrity gap on top of the content-duplication one.

So: it's doing double duty. It's a link record AND, via `session_b_note`, an independent (and
duplicated) copy of the finding's substance — a genuine normalisation violation, not a naming
quirk.

## 3. Can the real findings tables be normalised into one?

**The finding ↔ question relationship itself is already correctly normalised — don't touch that
shape.** `finding_question_link` proves the pattern works: 332,198 distinct findings linked to just
40 distinct questions, a clean many-to-many, 100% resolving. One content table (`finding`) + one
link table (`finding_question_link`) is exactly right — merging them would force either the
finding's content to repeat once per question (`wa_finding_catalogue_links`'s exact mistake) or a
multi-valued column. The M:N structure you spotted is real and is the *reason* the two-table split
is correct, not a reason to merge.

**The actual consolidation opportunity is the 3 content tables, not the link tables:**

- `wa_session_b_findings` (2,883 rows) is **already fully migrated** — `finding` has exactly 2,883
  rows tagged `provenance='session_b_migration'`, each traceable back via `source_legacy_ref`
  (format `SB:{registry}-{finding_id}|type:...`). This one is redundant *today* — a mark-inactive
  candidate, same treatment as `wa_flag_type_question_link` earlier.
- `cluster_finding` (19,997 rows, real content — 16,284 tagged `finding`, plus
  `cluster_synthesis`/`gap`/`silent`) is **not migrated at all**: zero rows in `finding` reference
  it anywhere (checked `source_legacy_ref LIKE '%cluster_finding%'` — zero hits; the `CLUSTER`-level
  rows already in `finding` are from the *session_b* migration, a coincidental level-name overlap,
  not `cluster_finding` content). It sits completely outside the unified store, frozen since
  2026-06-19 — the day before the 2026-06-25 method reset that declared all pre-reset lexical work
  legacy-to-be-revisited (CLAUDE.md top banner). Whether this is in scope for a real migration or
  already covered by that reset ruling is worth checking before any build work starts here.
- `finding_citation` is a live, well-used mechanism (51,148 rows, 100% resolving) — but it has
  never once been used for the live `finding` table, only for `cluster_finding`/`cluster_observation`.
  Worth a separate look: either the live finding pipeline should start citing evidence there too,
  or citations for live findings are handled some other way not covered by this review.

## 4. My read (not a decision)

1. **Low-risk, same pattern as today's `wa_flag_type_question_link` fix:** mark
   `wa_session_b_findings` inactive in `cfg_table` — its content is safely present in `finding`
   already, fully traceable.
2. **Same treatment, once you're satisfied nothing still needs `session_b_note` specifically:**
   `wa_finding_catalogue_links` — its source table is already migrated, and its own real value
   (the note text) is a duplicate-riddled snapshot already superseded by the live
   `finding`/`finding_question_link` pair.
3. **A genuine, larger decision, not something to just run:** whether `cluster_finding`'s 19,997
   rows of real, un-migrated content get folded into `finding` (mapping `obs_id` into
   `finding_question_link`, `cluster_code` carrying over directly, `level='CLUSTER'` already valid)
   or are left parked as pre-reset legacy.
4. **Flagged, not chased further here:** `finding_citation` never citing the live `finding` table.

Nothing above has been applied — this is the review, awaiting your call on items 2–4 (item 1 I can
process the same way as `wa_flag_type_question_link` if you'd like it done now).
