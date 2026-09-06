# Layer 1 (`verse_lexical`) — the definition, column by column

- **filename:** 1527-layer1-verse-lexical-definition-reference-v1-20260906.md
- **date:** 2026-09-06
- **escalation:** #1527
- **status:** Pure specification. No live data queried for this document, no reconciliation, no
  fix proposed. Sourced from (1) the live `cfg_method_rule` rows where one exists for a column,
  (2) the governing build specification's own prose where no `cfg_method_rule` row exists, and
  (3) the actual code in `iba/app/lib/lexical.py`, read in full, quoted/paraphrased with exact
  function names and line numbers. Where the recorded rule and the code visibly diverge, both are
  stated plainly, without a verdict — that judgement is yours.

---

## The grain — how many rows per verse

`verse_lexical` is **one row per Strong's code within a span** (`span_id`, `code_ordinal`) — a
span is one HTML `<span>` tag of a verse (`cfg_table`, `iba.span`: "ONE ROW PER HTML `<span>` tag
of a verse"), and a single span can carry more than one code (a "compound span" — e.g. a
prefix+stem combination), so one span can yield several `verse_lexical` rows. **A verse therefore
maps to many `verse_lexical` rows — one per code, not one per verse or one per span.** Everything
below applies at that per-code-row grain, and the same column/rule/logic applies identically to
every row of every verse; there is no per-verse variation in which rules apply.

The build entry point is `build_for_verse()` (`lexical.py:441`): for a given `verse_id`, it fetches
every live `span` (`_fetch_spans`, ordered by `position`), splits each span's `strong_variant`/
`morph_code` into its individual codes, resolves each code (`resolve_code`), computes the 7
per-row Layer-1 fields (`_layer1_fields`), then — needing the *whole verse's* rows together —
computes `gloss_consistent_in_verse` in one final pass (`_apply_gloss_consistency`) before writing.

---

## Column by column

### `id` (PK)
- **Rule:** surrogate primary key.
- **Code:** SQLite `INTEGER PRIMARY KEY` autoincrement, assigned on `INSERT` (`write_readings_for_span`, line ~398).

### `span_id`
- **Rule:** FK to `span.id` — "which span this reading is for."
- **Code:** passed in directly from the caller (`build_for_verse` iterates `_fetch_spans()`'s own `id` per span) — not derived, a straight pass-through.

### `verse_id`
- **Rule:** FK to `verse.id`, denormalized "from span... query without joining through span."
- **Code:** the `verse_id` argument `build_for_verse()` itself was called with — passed straight through, no re-derivation.

### `code_ordinal`
- **Rule:** "position of this code within the span's space-joined `strong_variant`, 0-based."
- **Code:** `enumerate(resolved)` in `write_readings_for_span()` (line 391) — the 0-based Python
  list index of this code within the span's already-split `codes` list (`build_for_verse`, line
  456: `codes = (sp["strong_variant"] or "").split()`).

### `strong`
- **Rule:** "the single code this row resolves."
- **Code:** one element of `codes` (the space-split `strong_variant`), passed into `resolve_code(conn, code, ...)` and stored verbatim as `row["strong"] = code` (`resolve_code`, line 175).

### `morph_code`
- **Rule:** "this code's own morph slice."
- **Code:** the corresponding element of `morphs` (the space-split `span.morph_code`), matched to
  `codes` by list index (`build_for_verse`, line 461: `morphs[i] if i < len(morphs) else None`) —
  **not** re-derived from anything; a positional pairing of two independently-split strings.

### `role`
- **Rule (live `cfg_method_rule`, `h0853-function-word-exception`, id 45):** "H0853 (the Hebrew
  direct-object marker, stepGloss='[Obj.]') is classified role='function' — classify_role's H9xxx
  regex gets an explicit, evidence-commented exception set (starting with H0853), not a widened
  range." (No separate live rule row states the general Hebrew-H9xxx / Greek-tag logic below —
  only this one named exception is promoted to `cfg_method_rule`; the general rule lives only in
  the module's own code comments, quoted here as the rule since no other source states it.)
- **Code (`classify_role`, lines 84–93):**
  - Hebrew (`strong` starts with `H`): `function` if the code's base is in `_H_FUNCTION_EXCEPTIONS`
    (currently just `{"H0853"}`), **or** if the code matches `_H_FORMATIVE_RE` (`^H9\d{3}[A-Z]?$` —
    STEP's reserved H9000–H9999 grammatical-formative range: article, prefixed prep/conj, pronominal
    suffixes, directional-he). Otherwise `content`.
  - Greek (`strong` starts with `G`, morph slice present): `function` if the morph slice's leading
    tag (before the first `-`) is one of `_GREEK_FUNCTION_TAGS = ("PREP", "PRT", "CONJ", "ART")`.
    Otherwise `content`. (Code comment, line 77–80: "verified only against G1722/G0505 this
    session, not exhaustively" — an explicit, on-record limit on how far this was checked.)
  - Anything else (no strong, or Greek with no morph slice): defaults to `content`.

### `status`
- **Rule:** "'resolved' or 'unregistered'."
- **Code (`resolve_code`, lines 175/182/197/228):** starts `"unregistered"`. Stays `unregistered`
  only if the `strong` code has no row at all in the `strong` table (line 182: `strong_row is
  None`). In every other case — whether or not `strong_meaning_parsed` has any sense rows for it —
  it is set to `"resolved"` (lines 197 and 228). **There is no third status value in the code**
  despite `resolved_sense` sometimes being a full raw-gloss fallback (see below) rather than a
  narrowed sense — both cases are recorded as `status='resolved'`.

### `resolved_sense`
- **Rule (build spec §B.4):** "stem/voice-selected sense text for 'resolved' rows."
- **Code (`resolve_code`, lines 186–229), exactly, both branches:**
  1. Look up `strong_meaning_parsed` rows for the exact code (`exact_rows`); if none, fall back to
     the code's *base* lemma's rows (`_base(code)`).
  2. **If no sense rows exist at all (line 196–199):** `resolved_sense = f"stepGloss: {stepGloss}"`
     — the raw `strong.stepGloss` text, verbatim, with no narrowing. This is the entire value.
  3. **If sense rows do exist (line 210–229):** determine `stem_name` from the morph code
     (`_stem_name_for` — Hebrew binyan letter or Greek voice letter, via `_HEBREW_STEM_MAP`/
     `_GREEK_VOICE_MAP`), then `_select_stem_text()` narrows the sense-row list to that stem's own
     branch (plus the shared root-level summary row) if a match is found, else falls back to every
     sense row's text joined together. **Either way, the final value is
     `f"stepGloss: {stepGloss} — {narrowed_or_fallback_text}"`** (line 213) — the raw `stepGloss`
     text is **always** prepended, in both the narrowed and un-narrowed cases. For Greek codes, LSJ
     and Mounce parsed-gloss text is further appended if present (lines 214–226).
  - **Note, stated plainly, not as a verdict:** in neither branch does the code ever produce a bare
    "selected sense" with no raw-gloss text attached — the rule's "stem/voice-selected sense text"
    and the code's actual output ("raw stepGloss + selected/fallback text") are not the same shape.
    Whether that's the intended reading of the rule is not decided by this document.

### `ambiguity_note`
- **Rule:** "set only when the sibling/base-fallback ambiguity check fires."
- **Code (`resolve_code`, lines 201–208):** only reachable in the branch where sense rows *do*
  exist. Computed only when **all** of: (a) sibling variant codes exist for this code's base
  (`sibling_variant_codes`), (b) this row used the *base-fallback* lookup rather than an exact
  variant match (`not exact_variant`), and (c) the base's own `stepGloss` text does not already
  support/contain the joined sense-row text (`not gloss_supported_by_tree(...)`). When all three
  hold, `ambiguity_note` is set to a fixed-shape string naming the shared base and sibling codes,
  plus a live STEP API lookup for context (`live_step_meaning`). Otherwise stays `None`.

### `created_at`
- **Rule:** ISO-8601 UTC.
- **Code (`_now()`, line 235–236):** `datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")`, set once at `INSERT` time only (`write_readings_for_span`, line 406) — never touched again once a row exists (per the identity-stable write redesign, #1520).

### `deleted`
- **Rule:** "version-aware soft-delete... rewriting a (span_id, code_ordinal) inserts a fresh row." *(This phrasing is the original, pre-#1520 rule — see the discrepancy noted directly below.)*
- **Code, as it actually behaves today (`write_readings_for_span`, lines 357–438, redesigned 2026-09-05, escalation #1520):** a `(span_id, code_ordinal)` slot's `id` is **never** re-minted while the slot continues to exist. `deleted` is set to `1` **only** when a code_ordinal that was previously live no longer appears in a fresh build for that span (the span's own content genuinely shrank) — not on every rewrite, and not as the mechanism for recording a content *correction* (a changed value is a real `UPDATE ... WHERE id=?` in place, `deleted` stays `0`). **The column's live rule and its documented rule text differ** — stated here as fact per your instruction, not resolved.

### `position`
- **Rule (live `cfg_method_rule` id 47, `mechanical-columns-run-on-every-code-no-selection`):** computed for every row unconditionally, no selection.
- **Code (`_layer1_fields`, line 321):** `row["position"] = span["position"]` — a straight copy of the parent span's own `position` column. Identical for every code within the same span.

### `surface`
- **Rule:** same rule id 47 as `position`.
- **Code (`_layer1_fields`, line 322):** `row["surface"] = span["surface"]` — straight copy, identical for every code within the same span.

### `language`
- **Rule (live `cfg_method_rule` id 44, `language-testament-derivation`):** "language = strong.language (verbatim copy)... mechanical, no judgement, run on every row."
- **Code:** set twice, redundantly, by two different paths — once inside `resolve_code()` (line 184: `row["language"] = strong_row["language"]`, from the `strong` table directly), and again overwritten in `_layer1_fields()` (line 323: `row["language"] = language`, the value threaded down from `build_for_verse`'s own `resolve_code(...)["language"]` result for that same code) — the two values are sourced from the same underlying lookup, so they agree in practice, but the column is written from two call sites, not one.

### `testament`
- **Rule:** same rule id 44 as `language`: "'OT' if `cfg_book_order.ordinal<=38` else 'NT' (Mal=38/Matt=39 boundary)."
- **Code (`_testament_for`, lines 290–294):** looks up `cfg_book_order.ordinal` for the verse's own book (derived from `verse.osisId`'s prefix before the first `.`, `build_for_verse` line 450); `NULL` if the book has no `cfg_book_order` row at all. Computed **once per verse** (line 451), not per code — every code in the verse shares the same value, matching the rule's own "run on every row" via the same single lookup, not one lookup per row.

### `is_negator`
- **Rule (live `cfg_method_rule` id 46, `lexical-code-class-lookup-not-hardcoded`):** "queried row in `cfg_lexical_code_class`... never a hardcoded list/dict... a code absent from the table is reported UNCLASSIFIED/NULL." **This rule's own text names the wrong table** — see the code below and the note under it.
- **Code (`load_code_classes`, lines 244–278, and `_layer1_fields`, line 327):** sourced from
  **`cluster_strong`**, not `cfg_lexical_code_class` — the module's own docstring states this
  explicitly (line 251–257): "architecture correction, researcher verdict 2026-09-05... not cfg
  territory" (BUILD.md #228/#229/#230). A code's *base* (`_base(strong)`) is looked up against
  every live `cluster_strong` row whose `cluster_code` is `T5` (mapped internally to the class
  `"negator"`); `is_negator = 1` if present in that set, else `None` (never `0` — absence is a
  genuine unclassified state, not a negative finding). **Note, stated plainly:** the live
  `cfg_method_rule` row (id 46) was written before the #1501 rewiring and still names
  `cfg_lexical_code_class` as the source; the code has moved to `cluster_strong` and the rule text
  was not updated to match. Both facts as they stand, no verdict offered.

### `narrative_morph`
- **Rule (live `cfg_method_rule` id 48, `narrative-morph-hebrew-only`):** "derived only for
  language='Hebrew' rows; Greek rows get NULL unconditionally."
- **Code (`_narrative_morph_for`, lines 297–312):** `NULL` unless `language=='Hebrew'` and the
  morph code starts with `HV` and is ≥4 characters. Then: if the 4th character (`morph_slice[3]`,
  the TAM slot) is `'w'` → `"wayyiqtol"`. If it's `'i'` (imperfect) **and** some *other* code in the
  same span has a base strong of `H0227` ("az"/"then") → `"az_imperfect_opening"`. Otherwise `NULL`.
  The sibling-code check is the only field on this list whose value can depend on another code in
  the same span, not solely on the code's own row.

### `gloss_consistent_in_verse`
- **Rule (build spec §D.1):** "100% (never NULL — always 0 or 1)." Quality-checked against a named
  calibration case ("re-run against Dan 1:8's known H0834A case, confirm 0").
- **Code (`_apply_gloss_consistency`, lines 333–349), run once per verse after every span in it has
  been resolved:** groups all of the verse's own resolved rows by the exact pair `(strong,
  morph_code)`. For a given row, `gloss_consistent_in_verse = 1` unless that pair's group contains
  **more than one distinct `resolved_sense` value** among the verse's own rows, in which case `0`.
  Rows with `strong` or `morph_code` missing default to `1`.

### `party_kind`
- **Rule (build spec §B.5):** "'divine'/'human'/'non_human' — set ONLY when this code IS ITSELF a
  name... a pronoun's own `party_kind` is NOT stored here."
- **Code (`load_code_classes` + `_layer1_fields`, lines 266–269, 286–287, 328–329):** the code's
  base is checked against `cluster_strong` rows tagged `T7`→`party_divine`, `T8`→`party_human`,
  `T9`→`party_angelic`, or `T4`→`party_adversarial`; the first matching class (of possibly several)
  maps through `_PARTY_CLASS_TO_KIND` — `party_divine→"divine"`, `party_human→"human"`,
  `party_angelic→"non_human"`, **`party_adversarial→"non_human"` also** (this fourth mapping is not
  named in the build spec's own B.5 text, which only lists three `cfg_lexical_code_class` classes
  for this column — `party_adversarial`/`T4` is a later addition, per BUILD.md #228's own note that
  this exact mapping gap was flagged live and has since been added to the code). `NULL` if no class
  matches.

### `updated_at`
- **Rule:** not part of the original #1383 build specification at all (that document's column list,
  §B.4/§B.5, ends at `party_kind`). Its rule is stated only in `lexical.py`'s own module docstring
  and `write_readings_for_span`'s docstring (lines 12–22, 374–376): set "to record when the
  correction was confirmed" — i.e., the timestamp of the most recent real `UPDATE` to an
  already-existing row's content, added by the 2026-09-05 identity-stable-write redesign
  (escalation #1520) specifically so a content correction has a timestamp without requiring the
  row's `id` (and therefore `created_at`) to change.
- **Code (`write_readings_for_span`, line 420/426):** set to `_now()` only on the `UPDATE` path (a
  genuine content change to an existing row); left untouched on `INSERT` (implicitly `NULL` unless
  the column has a default) and untouched on the `unchanged` no-write path.
