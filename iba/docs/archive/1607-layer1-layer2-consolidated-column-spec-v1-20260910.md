# Layer 1 / Layer 2 — consolidated column spec, for final review before the build

- **filename:** 1607-layer1-layer2-consolidated-column-spec-v1-20260910.md
- **date:** 2026-09-10
- **consolidates:** the full #1607 review arc — `1607-layer1-layer2-six-point-column-map-v1-20260909.md`
  (the original per-column analysis), `1607-open-items-action-plan-v1-20260909.md` (every D/E
  decision, edited in place through 2026-09-10), plus this session's own work: `resolved_sense`
  revived from `strong_meaning_parsed` sort=0 (BUILD.md #257), `gloss_consistent_in_verse`
  confirmed already-sound (#257), the E1 config-text batch (BUILD.md #258), and the
  `lib/lexiconparse.py` parse-routine fix that makes `strong_meaning_parsed` itself trustworthy
  (BUILD.md #259, escalation #1668).
- **Purpose:** one place that says, per column, what it will actually contain once the batch is
  built — not a re-argument of any finding, not a re-listing of the investigation. Read this,
  confirm or correct each row, then say go.
- **Legend:** ✅ decided, matches what's live today, no build needed · 🔧 decided, needs a code/
  schema change (queued for the batch) · ❓ still genuinely open — no decision given yet.

---

## 1. Layer 1 — `verse_lexical`

| # | Column | Final content | 🔧/✅/❓ |
|---|---|---|---|
| 1 | `id` | Surrogate PK, unchanged | ✅ |
| 2 | `span_id` | FK to `span`, unchanged | ✅ |
| 3 | `verse_id` | Denormalized from `span.verse_id`, unchanged | ✅ |
| 4 | `code_ordinal` | Position within the span's codes, 0-based, unchanged | ✅ |
| 5 | `strong` | The Strong's code this row resolves, unchanged | ✅ |
| 6 | `morph_code` | This code's own morph slice, unchanged (see note below — CA-1 gap, unrelated to this batch) | ✅ |
| 7 | `role` | **Redesigned.** JSON array of every live `cluster_strong.cluster_code` this strong belongs to (M01–M80ish/T2–T15/FLAG, not just the T4/T5/T7/T8/T9 subset `is_negator`/`party_kind` use). An empty set is an ERROR, gated by a pre-run validator — see §3 below, storage/gate mechanics not fully specified yet | 🔧 (partially open — see §3) |
| 8 | `status` | **Stays as today's simple model** (`resolved` / `unregistered`) — the proposed 3-value "meaning-readiness" redefinition (D2) is dropped; `resolved_sense` itself (NULL vs. non-NULL) is now the readiness signal | ✅ |
| 9 | `resolved_sense` | Gloss of the `strong_meaning_parsed` row with `sort=0` for this code (exact `strong_variant` match, or the base-lemma's `sort=0` row) — every code, no M-code restriction, **untruncated** (no length cap applied). Now reads from a corrected parse (escalation #1668) | 🔧 (needs the corpus `verse_lexical` rebuild — parse itself is already fixed and applied) |
| 10 | `ambiguity_note` | **Retires.** `pairing` moves to Layer 2 entirely; coverage backed by `role`'s completeness instead | 🔧 (drop column + stop writing it in `resolve_code()`) |
| 11 | `created_at` | Row creation timestamp, unchanged | ✅ |
| 12 | `deleted` | Soft-delete flag, unchanged | ✅ |
| 13 | `position` | Denormalized from `span.position`, unchanged | ✅ |
| 14 | `surface` | Denormalized from `span.surface`, unchanged mechanism — **192 live rows have a known alignment defect (escalation #1591), repair method drafted but not approved** | ❓ (repair approval, not a design question) |
| 15 | `language` | **Retires.** `verse_meta.language` (verse-level, already built) becomes the one true source; Layer 2 reads it directly instead of this per-code copy | 🔧 (drop column — **must** re-point `_narrative_morph_for`'s language check to `verse_meta.language` in the SAME unit of work, or Hebrew `narrative_morph` detection silently breaks) |
| 16 | `testament` | `'OT'`/`'NT'` from `cfg_book_order`, unchanged — no denormalization risk (re-derived fresh every build) | ✅ |
| 17 | `is_negator` | Unchanged mechanism (`cluster_strong` T5) — kept deliberately alongside `role`, same fast-trigger rationale confirmed for `party_kind` (§6 of the six-point map); not separately re-confirmed this round for `is_negator` itself | ✅ (by inference from `party_kind`'s confirmed rationale — flag if that doesn't hold) |
| 18 | `narrative_morph` | Hebrew wayyiqtol/az-imperfect detection unchanged and sound. **Greek signal: "keep and fix" confirmed, but the actual pattern to detect is not yet specified** — not buildable from that alone | ❓ (signal design) |
| 19 | `gloss_consistent_in_verse` | **Stays on `verse_lexical`, no promotion to `span`.** Formula unchanged (keyed on `surface`, not `resolved_sense` — confirmed already correct, re-verified against the full corpus this session) | ✅ |
| 20 | `party_kind` | Unchanged mechanism (`cluster_strong` T4/T7/T8/T9) — kept deliberately alongside `role`, confirmed closed (§5.2 of the six-point map) | ✅ |
| 21 | `updated_at` | Unchanged — set only on a real content correction, not on every INSERT (read as the intended scope; flag if "required" meant something stricter) | ✅ (pending confirmation of the reading) |

**Schema actions for the batch:** drop `ambiguity_note`, drop `language` (+ re-point
`_narrative_morph_for` first); `role`'s content changes (same column, new JSON-array values, no
type change). No other Layer 1 column adds or drops.

---

## 2. Layer 2 — `verse_lexical_note`

| # | Column | Final content | 🔧/✅/❓ |
|---|---|---|---|
| 1 | `id` | Surrogate PK, unchanged | ✅ |
| 2 | `verse_lexical_id` | FK anchor to the Layer 1 row this note is about, unchanged | ✅ |
| 3 | `verse_id` | Denormalized, unchanged | ✅ |
| 4 | `passage_id` | Live: always NULL (verse-scoped mode is the only one that runs) — **drop, or repurpose? No decision given.** | ❓ |
| 5 | `note_type` | Unchanged column; doc-string now lists all 15 live values including `verb_argument`/`compound_unit` (applied, E1) | ✅ |
| 6 | `resolution_status` | Unchanged, sound | ✅ |
| 7 | `target_verse_lexical_id` | Unchanged column; doc text now also names the `verb_argument` agent/trigger use (applied, E1) | ✅ |
| 8 | `related_verse_lexical_ids` | Unchanged column; doc text now also names the `verb_argument` recipient/impact use (applied, E1) | ✅ |
| 9 | `value_text` | Unchanged, sound, 100% populated | ✅ |
| 10 | `evidence_text` | **0/173 live rows have ANY value, ever.** Enforce as required going forward, or formally merge into `value_text`? No decision given — flagged high priority (Window 2 synthesis currently cannot audit any finding's grounding without this) | ❓ |
| 11 | `created_at` | Unchanged | ✅ |
| 12 | `deleted` | Unchanged | ✅ |

**Schema actions for the batch:** none certain yet — depends entirely on the D7/D8 decisions
above.

---

## 3. `role` — the one column needing more than a yes/no before it's buildable

Confirmed: **JSON array**, the complete live `cluster_strong.cluster_code` set per strong (your
instruction: *"the storage option should be consistent for all columns... I would suggest we use
json as a standard"*). Confirmed: an empty set is an ERROR, not a silent absence — your preferred
approach is **(b) pre-validate the scope of each run before it starts**: *"if role is null for any
word in the span for the scope, the validation fails and the run does not proceed."*

**Still needed before this is buildable, not decided yet:**
- The pre-validator itself — a real routine, registered, with its own quality check and failure
  message, gating `lexicon.run`/whatever produces a `verse_lexical` build. Not designed yet.
- Exact JSON shape (a bare array `["T5","M12"]`, or array of objects carrying more per membership?)
  — "JSON" is settled, the internal shape isn't.
- Your instruction *"the current 500k rows, plus the deleted rows are all redundant... effectively
  all lexicals will be redone"* and *"soft delete all current lexicals before first actual run
  starts"* — confirms the REBUILD scope (everything, not incremental) but the soft-delete-first
  step itself isn't built.

## 4. `verb_argument` (D9) — Layer 2, still open

The one live example (Gen, "gave" — agent Laban via `target_verse_lexical_id`, recipient Leah via
`related_verse_lexical_ids`) works and the field docs now describe it correctly (E1). Not decided:
which T3 (operation-verb) rows should get a `verb_argument` attempted (the trigger condition), and
wiring the mechanism to check the T7–T14 referent-identity tag on the resolved target. Likely
answered by `role`'s own completeness once built (§3 above), per D4's cross-reference — worth
confirming explicitly when this is worked, not assumed here.

## 5. Known data-quality gates — not this batch's design scope, but affect what these columns will actually hold

- **`surface`** — 192 live rows (0.035%) have a real word-alignment defect (escalation #1591), repair
  method drafted, not yet approved.
- **`role`'s own source** — escalation #1590 (Greek article `T` role-tag misclassification) is still
  `ready_for_approval`; whatever it decides changes what some `role` values will actually be.
- **`morph_code`** — 1,082/544,572 rows (0.2%) NULL, unexplained (CA-1), silently defaults
  `classify_role`'s Greek branch to `content` today. Not re-examined this round.
- **`language`/John.1.18** — the one live mixed-language verse (`H5207` where `G5207` is almost
  certainly meant) is still unfixed; moving `language` to `verse_meta` doesn't fix this specific row,
  it just changes where the (still-wrong) value would be read from.

## 6. Full still-open list (nothing here was decided — genuinely need your call)

| Item | Question |
|---|---|
| §3 above | `role` pre-validator design, exact JSON shape |
| D3 | `resolved_sense`: keep untruncated (live today), or apply a length cap after all? |
| D5 | `narrative_morph`: what should the Greek signal actually detect? |
| D6 | Confirm: `updated_at` required on correction only (as read), or on every row from INSERT? |
| D7 | `verse_lexical_note.passage_id`: drop, or repurpose? |
| D8 | `evidence_text`: enforce as required, or merge into `value_text`? |
| D9 | `verb_argument` trigger condition + T7–T14 wiring |
| D10 | `H3477H`: does "refers to Jashar" confirm T3-only? |
| #1590 | Greek article role-tag misclassification — approve the fix? |
| #1591 | `surface` 192-row repair — approve the method? |

---

**Once you've been through this:** say go, and the batch runs as one unit — the two schema drops
(`ambiguity_note`, `language` + the `narrative_morph` re-point), `role`'s pre-validator + rebuild,
and the `resolved_sense`/`gloss_consistent_in_verse` refresh against the now-corrected parse, all
together, one `verse_lexical` rebuild, not several.
