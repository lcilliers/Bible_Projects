# Glossary mechanism — design proposal (v1)

**Date:** 2026-09-02 · **Escalation:** #1377 (all notes/links/process control for this build live
there). **Stage:** DESIGN / PROPOSE — not built. **Supersedes**
[`archive/vocabulary-mechanism-design-v1-20260902.md`](archive/vocabulary-mechanism-design-v1-20260902.md),
rejected by the researcher same-day: it proposed two new `cfg_*` tables
(`cfg_vocabulary_index`, `cfg_vocabulary_usage`) around prose instead of actually using what
prose already does. Nomenclature switched completely from "vocabulary" to "glossary" per
researcher instruction — this document, and everything it proposes building, uses "glossary"
throughout.

## 0. What was wrong with v1 — stated plainly, not glossed over

The researcher's question was exactly right: *"did you map the prose engine properly into this
requirement, or just building more tables around it?"* Checked again, properly, and the answer is
no, I hadn't. Four concrete misses:

1. **Cited dead evidence as precedent.** v1 pointed to `prose_section_dimension_link` and
   `prose_section_finding_link` as proof of an established prose cross-reference pattern. Their
   own `cfg_column.use` text says plainly: *"Never populated."* They are scaffolding, not a
   working pattern — citing them was wrong.
2. **Invented a column that doesn't exist.** v1's "reuse the existing `supersedes_id` self-
   referential column" was wrong — `prose_section` has no such column (checked live:
   `id, registry_id, section_type_id, heading, body, word_count, status, version, author,
   created_at, approved_at, approved_by, metadata_json, delete_flagged, cluster_code,
   characteristic_id, cluster_subgroup_id, updated_at` — that's all of them). `supersedes_id` is
   a field name inside the **archived JSON patch** `prosestore.py` writes on import/edit
   (`iba/app/lib/prosestore.py:817-819`) — prose revision history lives in
   `archive/patches/`, not as a live DB column. A real difference from what v1 claimed.
3. **Didn't read the one `cfg_setting` row that already answers most of this.**
   `governance.prose_canonical_authority` (iba.db `cfg_setting`) was sitting there, unread before
   v1 was written. It states the intended pattern directly: *"`cfg_prose_concept` points a key
   project concept... at the prose section that defines it, rather than restating the definition
   as a separate rule."* That's the cross-reference convention this whole design needs — already
   decided, just not followed.
4. **Missed the direct precedent against the exact mistake made.** The same `cfg_setting` row
   cites **escalation #918**: `cfg_prose_chapter` (a sibling table to what v1 proposed) was
   **removed** because *"it was workflow DATA about content state, not a rule, and required the
   full config-approval cycle for what is an ordinary content edit."* `cfg_vocabulary_index`
   tracking a glossary entry's status/aliases/supersession is the same shape of mistake —
   ordinary glossary maintenance (add an alias, retract a term) would have been forced through
   `configmaint.propose`'s approval cycle for what is, and should stay, an ordinary prose edit.

## 1. Objective (unchanged from v1 — researcher, 2026-09-02)

Regulate project terms, especially loaded/confusable ones. Record outdated terms. Handle a
definition's lifecycle — reset, extend, retract. `cfg_enum` plays a part for strict column-value
vocabularies; the definition itself belongs elsewhere, cross-referenced. This round adds two firm
corrections: **no separate index table** — prose is already fully indexed and searchable, use
that, don't rebuild it. **No usage-link table** — a config referencing a glossary term does so by
**directly citing the prose section**, in its own existing field, not through an intermediate
table.

## 2. What prose already does, checked properly this time

| Capability needed | Already exists in `prose_section` / `prosestore.py`? | Evidence |
|---|---|---|
| Full-text lookup by term | Yes — `prose_section_fts` (FTS5, porter+unicode61 tokenizer) over `heading`+`body`, queried via `search_prose()`/`Prose.ps1 -Step Search`, filterable by `book`. | `iba/app/lib/prosestore.py:527` (`search_prose`), FTS5 table definition, live. |
| Narrative definition + disambiguation text | Yes — `body` is free-form prose; nothing about the schema limits how a definition explains multiple senses, warns about a loaded interpretation, or narrates its own history. | `prose_section.body`. |
| Lifecycle status | Yes — `prose_section.status`, governed by existing `cfg_enum` group `prose_section_status`: `draft / in_review / approved / archived`. `archived` already means "no longer current." | `cfg_enum WHERE name='prose_section_status'` (live, 4 values). |
| Revision history on edit | Yes — `prosestore.py:run_import_chapter`'s edit path writes a `supersedes_id`-tagged entry into the archived PROSE patch (`archive/patches/`, per `cfg_prose.patch_output_dir`) and bumps `prose_section.version` in place. No new mechanism needed. | `prosestore.py:817-819`, `cfg_prose` key `patch_output_dir`. |
| Structured extras alongside the narrative (e.g. an alias list) | Yes, already used for exactly this shape of thing — `metadata_json` already carries structured non-prose data on live rows today (e.g. `{"roundtrip_import": ..., "source_version": ...}`). An alias list is the same kind of extra. | Sampled live rows, e.g. `prose_section.id=22`. |
| A place for other config to point *at* prose instead of restating it | Yes — this is `governance.prose_canonical_authority`'s own stated pattern for `cfg_prose_concept`, just not yet generalised past those 2 rows. | `cfg_setting` key `governance.prose_canonical_authority`. |

**Conclusion: nothing new needs building to store or search a glossary entry.** The only real gap
is a **book** to hold them in and a **place to add glossary-specific status values** if
`draft/in_review/approved/archived` turns out not to be granular enough (see §5).

> **Correction, 2026-09-02 (building the full schema-mirrored write plan — researcher instruction —
> surfaced this):** the line above originally called the new book "an ordinary content addition,
> not a schema change." **That was wrong.** `prose_section_type.book_label` carries a live CHECK
> constraint — `CHECK (book_label IS NULL OR book_label IN ('Programme','Detail design','Findings',
> 'Essays'))` — that does not include `'Glossary'`. SQLite has no `ALTER` for a CHECK constraint;
> adding the value requires rebuilding the table (new `prose_section_type` with the updated CHECK,
> copy all 1,039 existing rows across, drop the old table, rename). This IS a schema change, on the
> live schema this whole design was built to avoid touching. See
> [`glossary-draft-entries-v1-20260902.json`](glossary-draft-entries-v1-20260902.json)'s
> `target_schemas`/`proposed_writes` for exactly where this blocks, and the choice it now forces:
> migrate the CHECK constraint, or file Glossary entries under an existing `book_label` instead of
> a new one. Not decided here — a real consequence of this correction, not silently worked around.

## 3. Architecture (corrected)

**No new tables. No new columns.** Everything lives inside the existing prose mechanism:

- **A new prose book: `book_label = 'Glossary'`.** One (or a small few) new `prose_section_type`
  row(s) with `book_label='Glossary'` — an ordinary data insert into an existing table, exactly
  like `Essays` or `Findings` already are. Registered in `cfg_prose.book_stage_map` and
  `cfg_prose.book_output_dir` (both already keyed by `book_label`) — data additions to existing
  `cfg_setting` values, not schema changes.
- **One `prose_section` row per glossary entry — one per distinct SENSE of a term**, not per
  word (unchanged reasoning from v1 §7: `cluster` M-code and `cluster` C-code are two entries,
  because conflating them is exactly the bug this mechanism exists to catch). `heading` carries
  the term + sense qualifier (e.g. "cluster — M-code sense"); this is what FTS5 already searches.
  `body` carries the full definition, disambiguation from other senses, loaded-term warnings, and
  its own history — written as narrative, because that is what prose is for and what makes it
  readable to a human doing a lookup, not just machine-queryable.
- **Aliases / old spellings**: recorded in `metadata_json` on the row itself (e.g.
  `{"glossary_key": "delete_marker", "aliases": ["deleted", "delete_flag", "deprecated"]}`),
  reusing the existing precedent for structured extras on a `prose_section` row — not a new
  column, not a new table.
- **Lifecycle (reset / extend / retract)**: an ordinary prose edit through the existing
  `Prose.ps1` export → edit → import cycle. Extending or resetting a definition is a normal body
  edit (new `version`, old text preserved in the archived patch, exactly as every other prose
  edit already works). Retracting/superseding a term sets `status='archived'` (existing enum
  value) and the `body` itself states what replaced it, in plain readable prose — no new status
  values needed unless a real case shows `archived` alone is too coarse (see §5, left open).

## 4. Cross-referencing — direct, no link table

Per the researcher's correction: any `cfg_*` row elsewhere that depends on a glossary entry cites
the **prose section directly**, in its own existing free-text field — exactly the pattern
`governance.prose_canonical_authority` already describes for `cfg_prose_concept`, generalised.
Concretely: `cfg_column.use`, `cfg_setting.use`, or a `GOVERNANCE.md`/`CLAUDE.md` prose passage
that needs to point at a glossary definition writes a plain citation into its own existing text —
e.g. `wa_quality_flag_types.delete_flagged`'s `cfg_column.use` gains a sentence such as *"see
Glossary: 'delete_flagged (soft-delete marker)', prose_section id=NNN"* — the same shape of
citation `cfg_column.use` rows already carry today for escalations and other `cfg_enum` groups
(e.g. `book_label`'s own `use` text: *"see `cfg_enum` group `prose_section_type_book_label`"*).
**No new table records this.** `cfg_prose_concept` itself is retired under this design — its 2
existing rows (`verse_primacy`, `inner_being_definition`) migrate into Glossary entries, and
`governance.prose_canonical_authority`'s own text is updated to describe the generalised direct-
citation pattern rather than naming the now-retired table.

## 5. Conflicts and fallout — a report against live citations, not a maintained table

v1 proposed a link table (`cfg_vocabulary_usage`) that every consumer would have to remember to
also write a row into — exactly the kind of parallel bookkeeping that drifts out of sync with the
citations it's supposed to track. Corrected: **a read-only report/utility**
(`report.glossary_fallout <heading-or-prose_section_id>`) that, given a glossary entry, scans
`cfg_column.use`, `cfg_setting.use`, and other `prose_section.body` text (via the same FTS5 index,
plus a plain `LIKE` fallback for non-FTS tables) for citations of that entry's heading or id, and
lists what it finds — reusing exactly the method #1377 itself already used twice over (the full
`cfg_column` scan, the full prose read) to surface real collisions, not inventing a new detection
mechanism. This runs **before** approving a status change on a glossary entry, showing the
blast radius from the live citations themselves, which can never drift out of sync with reality
the way a separately-maintained link table can.

## 6. Worked examples (unchanged from v1, re-expressed without the retired mechanism)

| Case | Glossary entries (`heading`) | `metadata_json.aliases` | Cross-reference example |
|---|---|---|---|
| 4-way delete-marker spelling | "delete_flagged (soft-delete marker)" — one entry, spelling variance only | `["deleted","delete_flag","deprecated"]` | `wa_obs_question_catalogue`'s `cfg_column.use` (already flags the `deleted`/`status` disagreement) gains a direct citation to this entry. |
| `cluster` column (M-code vs C-code) | "cluster — M-code sense", "cluster — C-code sense" | none | `wa_dim_review_cluster_log.cluster`'s `cfg_column.use` cites the C-code sense entry directly — the one place a bare `cluster` column disagrees with the usual M-code sense. |
| `characteristic` (3 grains) | "characteristic — programme concept (Ch.1)", "characteristic — Model A table", "characteristic — Model B `ib_characteristic` family" | none | Each grain's defining table/column cites its own entry. |
| `scope` (4+ meanings) | "scope — verse-coverage band", "scope — file-naming granularity", "scope — catalogue bucket", "scope — run-step parameter" | none | Four entries, four separate `cfg_column.use` citations, no shared row. |

## 7. What this design still leaves open (for you, not assumed)

1. **Whether `draft/in_review/approved/archived` is granular enough** for glossary lifecycle, or
   whether a genuine need emerges for a `deprecated` (still valid, discouraged) vs `archived`
   (wrong/retired) distinction once real entries are written — recommend deciding this against a
   real case during the build's own test plan, not speculatively now.
2. **Migration of `cfg_prose_concept`'s 2 rows** into Glossary entries, and updating
   `governance.prose_canonical_authority`'s text to describe the generalised pattern.
3. **Whether the full ~40-term seed list gets sorted into Glossary entries as part of this build**,
   or a small representative subset (the §6 worked examples) is the build's own test material,
   with the rest tracked as explicit follow-on under #1377.
4. **`report.glossary_fallout`'s exact matching strategy** (heading substring vs a stricter
   `metadata_json.glossary_key` tag) — a build-plan-stage decision once there are real entries to
   test it against.

## 8. Next steps

Per the cycle you asked for: this document is the corrected design/propose stage. On approval,
next is a test plan (creating an entry, aliasing an old spelling, extending via the normal edit
cycle, archiving one with existing citations and confirming the fallout report finds them, looking
up an ambiguous bare word and getting all its senses back), then a build plan, then the build.
Nothing further proceeds until this is approved or corrected again.
