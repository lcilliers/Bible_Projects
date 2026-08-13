# Does IBA have a catalogue/dimensions equivalent? Scanned the config, not the docs

> Ad hoc investigation, 2026-08-13. Read-only. `iba.db` = `iba/app/db/iba.db`. Per
> `feedback_iba_config_first_not_doc_archaeology`: queried `cfg_step`/`cfg_setting`/`cfg_enum`/
> `cfg_method_rule` directly, not the method docs.

## Short answer

Yes, but shaped differently, and the difference is deliberate, not an oversight. The old system's
catalogue (424 pre-written questions) and dimension index (a fixed set of content categories every
verse gets sorted into) were both **closed vocabularies decided in advance**. IBA's book-debate
layer has a real equivalent scaffold — but it governs *how to identify things* (process rules) and
*a handful of structural types* (shape of the record), while deliberately leaving *what gets
identified* (the actual content — what phenomenon, what action) as free text. One method rule says
this outright (`operation.set` / `action-type-is-a-label`): *"a label for cross-passage/cross-book
comparison, not a taxonomy; no controlled vocabulary is being built."* That's the opposite design
choice from the old dimension index, made on purpose.

## Around the lexical (`lexical.build` / `report.verse_lexical`) — nothing, by design

Zero `cfg_method_rule` rows, one trivial `cfg_setting` (output filename pattern). The lexical layer
doesn't identify or classify content at all — `classify_role()` (`lib/lexical.py`) is pure
mechanical morphology (content vs. function role), no analytical judgement, matching
`USER-GUIDE.md` §12b's own description ("mechanical, deterministic"). There's nothing here that
plays the catalogue/dimension role because this layer isn't making the kind of call a
catalogue/dimension exists to govern.

## Around the book debate (`hib.set` → `phenomenon.set` → `operation.set` → `closing.set`) — the real scaffold

**`cfg_method_rule` — 38 active rows**, one per step, each citing its own source doc and how it's
enforced (schema constraint / code function / `None` = guidance-only, not yet enforced). This is
the closest functional equivalent to "the catalogue" — not a flat question list, a **rule
registry**:

| step | rules | enforcement mix |
| --- | --- | --- |
| `hib.set` | 8 | 2 schema, 2 code, 1 enum+code, 3 guidance-only |
| `phenomenon.set` | 8 | 2 schema, 1 code, 5 guidance-only |
| `operation.set` | 8 | 4 schema, 1 enum(+pending code note, see below), 3 guidance-only |
| `closing.set` | 6 | 4 schema, 2 guidance-only |
| `passage.build` | 6 | 4 code, 2 schema |
| `lexical.build`/`report.verse_lexical` | **0** | — |

**`cfg_enum` — the actual fixed typologies, and there are exactly three, all small:**

- **`hib_kind`** (6 values, enum + code-enforced via `operations.py:_valid_hib_kinds`) —
  `named_individual / unnamed_individual / named_collection / unnamed_collection /
  implicit_individual / implicit_collection`. Two axes (plurality × specificity), per the
  `six-type-scheme` rule. This is the nearest thing to a "dimension" in IBA — but it types **who**
  (the HIB itself), not **what** is happening.
- **`operation_decision`** (4 values, enum + code-enforced via `operations.py` line ~999) —
  `retain / set_aside / retain_referential / recorded_silence`. A workflow-decision typology, not a
  content classification.
- **`narrative_required_channel`** (3 values, referenced by
  `method.inner_being_narrative_guidance_path`'s "three-channel scope requirement") — `Non-human ↔
  human / Human ↔ human / Physical world ↔ human`. The one enum that's genuinely *content*-shaped
  (relational channels a narrative must cover), closest analogue to an old-style dimension —
  scoped to the narrative-generation step specifically, not the whole debate.

**What's deliberately NOT enum-governed:** `operation.action_type`, `operation_party.role`,
`operation_party.kind`, `phenomenon.description` — all free text. Checked the live data:
`action_type` across ~140 operation rows has ~98 distinct values, nearly all singletons ("self-
exalt-and-desecrate", "receive-vision", "advance-with-supernatural-speed"...) — genuinely emergent,
not converging on a reusable set. `operation_party.kind` (5 values in practice: self/human/
non_human/none/object_situation) and `.role` (2: target/source) *have* converged to a small set in
practice, but that's an empirical pattern, not an enforced schema — nothing stops a new value.

**One stale note, found in passing, not chased further:** `cfg_method_rule`'s `decision-enum` row
says operation.decision is *"free text, not yet enum-enforced -- see cfg_enum follow-up"* — but
`operations.py` (line 999) already validates it against `cfg_enum 'operation_decision'` live. The
method-rule note is out of date relative to the code; flagging, not fixing.

## The shape of the difference

| | old system (catalogue + dimensions) | IBA book-debate |
| --- | --- | --- |
| governs | what content-category a verse's meaning belongs to | how the identification process runs, and the record's structural shape |
| vocabulary | closed, pre-written (424 questions, ~14-16 D-codes) | 3 small closed enums (6/4/3 values) for *structure*; content fields explicitly free text |
| where it lives | DB data tables (`wa_obs_question_catalogue`, `wa_dimension_index`) | `cfg_method_rule` (rules) + `cfg_enum` (structural types) — config, not data |
| stated intent | classify into fixed categories | *"a label... not a taxonomy; no controlled vocabulary is being built"* (method rule, verbatim) |

Consistent with last session's closing correction (no more bulk-classifying backfill by keyword
match — assignment belongs to analysis, context has to play its part): the book-debate layer was
apparently already built on that same principle before it was ever stated for the cluster/backfill
work. The rule scaffold is real and substantial; the content vocabulary is deliberately open.
