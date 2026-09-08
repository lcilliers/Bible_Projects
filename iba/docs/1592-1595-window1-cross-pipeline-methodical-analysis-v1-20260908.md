# Window 1 (Layer 1 / Layer 2) — full column-purpose validation and pipeline gap analysis

- **filename:** 1592-1595-window1-cross-pipeline-methodical-analysis-v1-20260908.md
- **date:** 2026-09-08 (rerun, same file, in-place per review-mode convention)
- **escalations covered:** #1592, #1593, #1594, #1595, plus #1596 (raised from the first pass) and
  the new corrective-action items this rerun raises
- **researcher instruction, verbatim, this rerun:** *"the purpose of every column in the pipeline
  must be validated and explained. the values of each column must meet the purpose, and if it does
  not, include a new section that will prompt the corrective action the ensure that it does. when
  you evaluate the layer 2 pipeline processing, and window 2 pipeline processing, are there any data
  missing, or it would be ideal to have it, that is not available. where does the data come from.
  can it be added to the columns of layer 1 or 2 to support the next stage in the pipeline."*

## 0. What changed in this rerun, and why

The first pass reported column *distributions* and cross-checked *design-document* claims against
the live code. That was not what was asked. This rerun does three things differently:

1. **Purpose is now taken from the live, authoritative `cfg_column.use` text** (per
   `governance.table_columns` — this is *the* record of a column's purpose, not the 2026-09-04
   design proposal, which can and did drift from it). Every column below quotes its live `use` text
   verbatim, then checks the real data against *that* text specifically.
2. **Every column got a real live check, corpus-wide where feasible** — not sampled, not asserted.
   Several checks below were not run at all in the first pass (`updated_at`'s own `cfg_column`
   registration, `evidence_text`'s population rate, `position`/`verse_id` mismatch counts run against
   the *whole* corpus rather than "spot-checked").
3. **A dedicated Window 1→Window 2 missing-data section** (§5) — for each concrete gap, what's
   missing, where the data would come from, and whether it belongs on a Layer 1 or Layer 2 column —
   not just "this catalogue question is unanswerable," which is as far as the first pass went.

Everything found is collected in one **Corrective Actions Register** (§6) for direct disposition.

---

## 1. Layer 1 — `verse_lexical`, column-by-column (544,572 live rows, 29,754 verses)

Format: live `cfg_column.use` text (verbatim) → live check → verdict. "MET" means the value
population genuinely satisfies what the purpose text claims; anything else gets a corrective action
(CA-n, collected in §6).

### `id`
**Purpose:** surrogate PK. **Check:** structural only. **MET.**

### `span_id`
**Purpose:** "which span this reading is for." **Check:** 0/544,572 rows reference a deleted or
missing `span` (corpus-wide, not sampled). **MET.**

### `verse_id`
**Purpose:** "denormalized from span... query without joining through span." **Check:** 0/544,572
rows where `verse_lexical.verse_id != span.verse_id` (corpus-wide join). **MET.**

### `code_ordinal`
**Purpose:** "position of this code within the span's space-joined `strong_variant`, 0-based."
**Check:** 0 duplicate `(span_id, code_ordinal)` pairs among live rows — the grain's own uniqueness
invariant holds, checked corpus-wide. **MET.**

### `strong`
**Purpose:** "the single code this row resolves — may be NULL only if `strong_variant` itself is
empty (**should not occur in practice**)." **Check:** 0/544,572 NULL. **MET — confirmed empirically
against the purpose's own stated expectation, not merely assumed.**

### `morph_code`
**Purpose:** "this code's own morph slice (space-split from `span.morph_code`...)." **Check:**
**1,082/544,572 (0.2%) are NULL.** The purpose text says nothing about whether this is expected.
**Not fully MET — CA-1.** This has a real downstream consequence, not just a bookkeeping gap:
`classify_role`'s Greek branch requires a morph slice to decide `content` vs. `function`; a Greek
code with `morph_code IS NULL` silently defaults to `content` (confirmed in the #1527 code-reference
document). These 1,082 rows may therefore be inflating the `content` count with codes nobody has
actually classified — a second, distinct contributor to `role`'s known inaccuracy, not previously
named alongside the Greek-tag bug (#1590).

### `role`
**Purpose:** "'content' (independent lexical item) or 'function' (grammatical formative...).
Classification metadata only — does NOT gate resolution." **Check, this rerun, against the actual
code (not taking the purpose text's own claim on faith):** confirmed independently in both
`handlers/lexical.py` and `lexicalenrich.py` that `role` gates nothing in Layer 2 (§ Layer 2
findings, prior round). **Purpose (non-gating) MET.** **Value accuracy NOT MET** — the confirmed
Greek `T`-tag defect (#1590, 82 rows) plus `morph_code`'s 1,082 NULLs (CA-1, above) together mean
`role`'s `content`/`function` split is less trustworthy than its face-value 363,253/181,319 split
implies. Cross-referenced to #1590, not re-raised as a new item — but sized more precisely here.

### `status`
**Purpose:** "'resolved' (strong row found, sense pulled...) or 'unregistered' (no strong row yet —
**a genuine coverage gap**, regardless of role)." **Check:** 559/544,572 (0.1%) unregistered. The
purpose text itself frames this as a gap to be *closed*, not tolerated — and a real closing
mechanism exists and runs: `handlers/lexical.py:79` calls `raw_mod.backfill_meaning_for` before every
build specifically to shrink this population (`"(auto-backfilled N previously-unregistered strong(s)
before building)"`). **MET as a tracked, actively-shrinking gap** — but **CA-2**: nothing confirms
what the surviving 559 actually are (permanently absent from STEP, or simply not yet re-run through
backfill) — worth a direct check before treating 559 as an acceptable steady-state number.

### `resolved_sense`
**Purpose (live `cfg_column`, unchanged since before #1575):** "stem/voice-selected sense text for
'resolved' rows... **NULL only for 'unregistered' rows** — a real gap, not a hedge." **Check:**
0/544,572 non-null, **including all 544,013 'resolved' rows the purpose text says should carry real
content.** **NOT MET — total mismatch, and the documentation itself is now false, confirmed live, not
inferred.** **CA-3 (governance-compliance gap):** escalation #1575 (2026-09-07) correctly changed the
*code* so this column is permanently `NULL`, and updated `BUILD.md` and `cfg_method_rule` — but never
touched this column's own `cfg_column.use` text, which still describes behaviour that no longer
exists anywhere in the live system. This is exactly what `governance.table_columns`
("updating a column in any routine must validate the use of the column against this config") exists
to prevent, and it was missed at the time.

### `ambiguity_note`
**Purpose:** "set only when the sibling/base-fallback ambiguity check fires — live senses named, not
resolved (**T4's job**, not this table's)." **Check:** 1,755/544,572 (0.3%) non-null — fires at a
plausible rate; not independently re-verified against a hand-picked case this pass. **Rate: MET.**
**CA-4, found reading this column's own purpose text closely:** "T4" here is neither the T-code
*cluster* `T4` (Adversarial, §2) nor the catalogue's `T4.x` (Divine/Human Interface) — it's a third,
older **processing-tier** naming scheme (`T1`–`T9` as pipeline stages; the live `lexical` utility's
own `cfg_utility` purpose text still reads *"T1-T3 of the verse-lexical technique"*). **Three
unrelated `T`-numbering schemes now coexist in this project's live documentation**, and this
session's own investigation lost real time to that exact collision working out what "T-code
clusters" meant for #1593. Recommend disambiguating the names before it causes a real misreading,
not just an inconvenient one.

### `created_at` / `position` / `verse_id` (already above) / `language` / `testament`
- `created_at`: mechanical, ISO-8601 UTC. **MET.**
- `position`: "span.position, denormalized." **Check:** 0/544,572 mismatches vs. `span.position`,
  corpus-wide (the first pass only claimed a "spot-check equals"; this is the full check). **MET, to
  a stronger standard than previously stated.**
- `language`: "strong.language, denormalized." **Check:** 559 NULL, **exactly** matching the
  `status='unregistered'` count (a code with no `strong` row has no language to copy). Internally
  consistent. **MET.**
- `testament`: "'OT' if `cfg_book_order.ordinal`<=38 else 'NT'..." **Check:** 0/544,572 NULL — every
  verse's book resolves against `cfg_book_order`, independent of whether the code itself resolved.
  **MET** (not checked at all in the first pass).

### `deleted`
**Purpose:** version-aware soft-delete. **Check:** 430,888 rows currently `deleted=1` against
544,572 live — a 44% churn ratio, from the cumulative effect of multiple full-corpus rebuild waves
(#1520's identity-stable-write redesign, ordinary re-development churn). Not itself a defect; noted
as scale context, no corrective action.

### `surface`
Already-escalated defect (#1591, 192 rows) — cross-referenced, not re-litigated; gated pending your
approval of the surface-column rewrite.

### `is_negator`
**Purpose (live `cfg_column`, unchanged):** "1 if `strong` is in `cfg_lexical_code_class` WHERE
`class='negator'`..." **Check:** the actual code (`load_code_classes`, `lib/lexical.py`) sources this
from **`cluster_strong` WHERE `cluster_code='T5'`**, not `cfg_lexical_code_class` at all —
`cfg_lexical_code_class` is dead code, confirmed twice already (its own docstring, and
`lexicalenrich.py`'s unused `code_classes = None` placeholder). **NOT MET — this is a documentation
defect in the *authoritative* `cfg_column` table itself**, not only in `cfg_method_rule` id 46 as the
first pass found. **CA-5.**

### `narrative_morph`
**Purpose:** Hebrew-only wayyiqtol/az+imperfect flag. **Check:** 0 non-null Greek rows — matches.
**MET.**

### `gloss_consistent_in_verse`
**Purpose:** "1 unless this `(strong, morph_code)` pair carries >1 distinct `resolved_sense` value...
— mechanical data-quality check." **Check:** since `resolved_sense` is now permanently `NULL`
corpus-wide (confirmed above), a group of all-`NULL` values can never show ">1 distinct value" —
**the purpose is now structurally unsatisfiable**, and 106,658/544,572 (19.6%) rows still carry a
stale `0` computed before `#1575`. **NOT MET — already raised as escalation #1596; cross-referenced,
not duplicated.**

### `party_kind`
**Purpose (live `cfg_column`, unchanged):** "'divine'/'human'/'non_human'... `cfg_lexical_code_class`
class IN party_divine/party_human/party_angelic..." **Check:** same drift as `is_negator` — the real
source is `cluster_strong` T7/T8/T9/T4. **NOT MET — same class of defect as CA-5, in the
authoritative `cfg_column` record. CA-6.** The purpose text's own 3-value grain (no adversarial vs.
angelic distinction) is a separate, already-known gap (#1549) — addressed as a missing-data item in
§5, not repeated here as a fresh finding.

### `updated_at`
**Purpose: NONE — this column has NO `cfg_column` row at all.** Confirmed live: 20 of the table's 21
live columns are registered; `updated_at` (added by the #1520 identity-stable-write redesign) was
never migrated into `cfg_column`. **This is a direct, unambiguous `governance.table_columns`
violation** ("each column in each table... must be listed in `cfg_column` with a proper use text"),
not a judgement call — the column's actual behaviour is already well documented in code and in the
#1527 genealogy document, it was simply never carried into the governance record. **CA-7.**

---

## 2. Layer 2 — `verse_lexical_note`, column-by-column (173 live rows)

### `id` / `verse_lexical_id`
**Purpose:** PK / "the code-row this note is about." **Check:** 0/173 orphaned references (every
note resolves to a live `verse_lexical` row). **MET.**

### `verse_id`
**Purpose:** "denormalized, matches phenomenon's own precedent." **Check:** 0/173 mismatches against
the note's own `verse_lexical_id`'s actual `verse_id` (corpus-wide join, not sampled). **MET.**

### `passage_id`
**Purpose (live `cfg_column`, unchanged since the original design):** "denormalized, matches
`phenomenon`'s own precedent." **Check:** 0/173 rows carry a non-null `passage_id` — every live
Layer 2 write happens in the verse-scoped mode `#1451` made the default. **The column's stated
purpose no longer describes how the table is actually used at all — NOT MET, and this is not a new
finding but a concrete instance of a gap `#1451` itself named and left open** ("`verse_lexical_note.
passage_id`... needs a decision: drop it, or repurpose it... not designed here"). **CA-8.**

### `note_type` / `resolution_status`
Enum-governed, both structurally sound (every live value is a real enum member). Content-fit issues
(6 of 15 `note_type` values never defined or ever used) are #1589/#1595's own subject, cross-
referenced, not repeated here. **New, minor finding:** `resolution_status='not_supported_this_language'`
has **0/173 occurrences ever** — an enum value that exists but has never actually been exercised.
**CA-9 (low priority):** worth a deliberate test (a Hebrew-only rule like `chain` run against a Greek
verse) to confirm this path actually writes correctly when it should, since nothing has forced it
yet.

### `target_verse_lexical_id` / `related_verse_lexical_ids`
**Check:** 21/173 rows use `target_verse_lexical_id`, 0 unresolved/orphaned; 1/173 uses
`related_verse_lexical_ids`, valid. Thin samples, but what exists is clean. **MET.**

### `value_text`
**Purpose:** "the finding itself, free text." **Check:** 0/173 NULL — 100% populated. **MET.**

### `evidence_text`
**Purpose:** "what in the verse's own data supports it (morph marker, related-word pull, etc.)."
**Check: 0/173 rows have ANY value — 100% NULL, universally, across every note_type, every
resolution_status, without exception.** **NOT MET — this is the single largest concrete defect found
in this whole rerun.** Sample `value_text` content shows the practice has informally folded evidence
into that field instead (e.g. one `related_word` note's `value_text` reads *"Genuine same-concept
family: rich/enrich (H6223/H6238)"* — the Strong's codes ARE the evidence, just not in the column
built to hold it). **CA-10 (high priority).** Consequence, directly on point for your own §1595
requirement ("clear reason why not answered must be authentic"): **there is currently no way to check
any of the 173 live findings' grounding against the verse's own data**, because the column meant to
carry that grounding has never once been used.

### `created_at` / `deleted`
Mechanical. `deleted`: 0/173 (nothing superseded yet, consistent with the thin, early-stage sample).
**MET.**

---

## 3. `passage.genre` / `passage.lexical_complete_at`

### `genre`
**Purpose:** "manual, set as part of `lexical.enrich`'s own first move... NOT ported from
`bible_research.db.verse.genre` (too coarse)." **Check:** since `#1451`, `lexical.enrich` never
resolves a real `passage_id` in its live default mode — every call that supplies a genre value gets
`genre_dropped=true` back (confirmed in code, prior round) and nothing persists it. **NOT MET in
practice — every real Layer 2 run to date has silently discarded whatever genre value was supplied.**
**CA-11**, developed concretely in §5.4 below (genre needs a *verse*-level home, not a
*passage*-level one — the `passage` table is the wrong grain now, not just an unwired pipe).

### `lexical_complete_at`
**Purpose:** "NULL until every verse in this passage has a `verse_lexical` row for every code AND...
a `verse_lexical_note` disposition... set only by an explicit control check." **Check:** the same
`if genre is not None and passage_id is not None` guard structure applies to `set_lexical_complete`
— since `passage_id` is always `None` in the live default mode, **this column can never be set by the
live pipeline either.** **NOT MET — a second, previously-untraced consequence of the same `#1451`
redesign** (that document named `genre`'s own homelessness explicitly but did not trace through that
completeness-tracking is orphaned the same way). **CA-12.**

---

## 4. T-code clusters — completeness, checked, not just sized

The prior round only sized the T-code groups (T2 Supplementary=2,402; T3 Operations=1,912; T4
Adversarial=3; T5 Negator=7; T6 Connective=6; T7 Party-Divine=9; T8 Party-Human=12; T9
Party-Angelic=5) — it did not check whether any group is actually *complete*, or whether the
existing groups even cover the distinct *kinds* of lookup the pipeline needs. **Researcher, this
round: "the refinement of the M and T codes must take place [before role/status]... I am also not
convinced that the T-code clusters map properly onto the different types of lookups that is
required... action verbs, the signals for faculties, other objects/beings that act like beings —
have [these] been properly isolated."** Checked directly against live data, not asserted either way.

### 4.1 A concrete completeness-check method, demonstrated (not just proposed)

The check that was missing: pull the highest-frequency `content`-role codes that carry **no**
cluster tag at all, and read what they actually are. This is itself the validation check §4 lacked —
demonstrated here, not left as a future to-do:

| strong | language | live occurrences | gloss | what it actually is |
|---|---|---|---|---|
| G0846 | Greek | 5,482 | "it/s/he" | **personal pronoun**, morph `P-*` |
| H0834A | Hebrew | 5,448 | "which" | **relative particle**, morph `HTr` |
| G3739 | Greek | 1,257 | "which" | **relative pronoun**, morph `R-*` |
| G3778 | Greek | 1,210 | "this/these" | **demonstrative pronoun**, morph `D-*`/`P-*` |
| H5973A | Hebrew | 943 | "with" | **preposition**, morph `HR`/`HRd` |
| H0854 | Hebrew | 916 | "with" | **preposition**, morph `HTo`/`HR`/`HRd` |
| H0859A | Hebrew | 742 | "you [m.s.]" | **personal pronoun**, morph `HPp2ms` |
| H0310A | Hebrew | 710 | "after" | adjective/construct-form, borderline |
| G2064 | Greek | 619 | "to come/go" | **a genuine action verb — not in T3** |
| H5927G | Hebrew | 604 | "to ascend: rise" | **a genuine action verb — not in T3** |
| H3478/H4428G/H0776G/H1732/… | both | 1,000s each | Israel, king, land, David… | proper nouns / ordinary concrete nouns, correctly carrying no analytic tag |

### 4.2 What this confirms — your scepticism was right, on two distinct counts

1. **`T3` (Operations) is not exhaustive.** `G2064` ("to come/go," 619 occurrences) and `H5927G`
   ("to ascend/rise," 604 occurrences) are genuine action verbs, glossed exactly like T3's own
   sampled members (checked: `T3`'s live rows are consistently "to `<verb>`" glosses, so T3 is
   internally coherent as a category — it's just not complete). **Action verbs have not been fully
   isolated, confirmed.** Also found: 10 strongs are tagged *both* an M-code and `T3` — a verb can be
   a characteristic in its own right and generically an "operation" at the same time; the two
   groups are not fully disjoint, which any completeness check needs to account for rather than
   assume away.
2. **A real, previously-underestimated `role`-classification defect, bigger than #1590's own
   record.** `classify_role`'s Greek function-tag list is `("PREP", "PRT", "CONJ", "ART")` — it does
   **not** include `P` (personal pronoun), `R` (relative pronoun), or `D` (demonstrative pronoun),
   confirmed directly against the morph codes above. On the Hebrew side, `classify_role` only
   recognises the reserved `H9xxx` grammatical-formative range — Hebrew pronouns and prepositions
   live in a **different** morph-code namespace (`HP*` personal pronoun, `HR*` preposition/relator,
   `HTr` relative particle) that the existing regex never matches at all. **`G0846` alone (5,482
   occurrences) and `H0834A` alone (5,448 occurrences) each outweigh #1590's entire previously-known
   82-row Greek-article-tag count by more than 60×** — this is not a marginal addition to that
   escalation, it changes its scale. Logged against #1590 directly (§6.4 below), not folded silently
   into this section.

### 4.3 Faculty-domain signals — confirmed still entirely absent (restated, not new this round)

No lexicon, no column, no note_type rule exists anywhere for the 11 faculty domains — unchanged from
the first pass (§ prior "5.2"). Nothing new to add beyond what escalation #1593's own resolution
already states.

### 4.4 "Objects/beings that act like beings" — checked, and it is a different KIND of gap than the other two

Checked whether personifiable terms (a classic case: "wisdom cries out," Prov. 1:20) are simply
missing from the lexicon system the way faculty-domain terms are. **They are not** — `wisdom`
(`G4678`) is already tagged `M16` (Wisdom & Folly), because the study's own characteristic
vocabulary already includes exactly these nouns as its primary subject matter. **The gap is not a
missing lexicon entry — it is that nothing currently detects *when* an already-tagged (or even an
untagged, e.g. "the earth," "the sea") noun is being used as the grammatical subject of an active
verb in a specific verse**, i.e. treated as an acting being in that verse's own grammar, regardless
of its ordinary party_kind. That is a **per-verse, contextual** question, not a fixed lexicon-
membership one — structurally, it is exactly what the already-designed `verb_argument` note_type's
`target_verse_lexical_id` ("trigger" = grammatical subject) exists to capture, cross-checked against
whether that subject resolves to a non-`divine`/non-`human`/non-`non_human` (i.e. inanimate, no
`party_kind` at all) noun. **This note_type has only 1 live example ever written** — so whether it
actually catches personification in practice is completely unvalidated, not merely under-tested.
**Recommend treating this as a Layer 2 validation question (does `verb_argument` actually surface
personified subjects when tested against real cases), not a new T-code lexicon-building task** — a
materially different kind of fix than 4.2's action-verb gap or 4.3's faculty gap, and should not be
scoped as if it were the same kind of work.

### 4.5 What a real completeness check needs, going forward — not decided here

The method demonstrated in §4.1 (highest-frequency untagged codes, read against their actual gloss
and morph code) is repeatable and cheap — it surfaced two genuine, differently-shaped defects in one
pass. Recommend it become a standing check run *before* any T-code group is declared complete, not a
one-off audit — but whether that's a new report step, a `configmaint.validate`-style check, or a
manual per-group review is a design choice, not decided here.

---

## 5. Layer 2 → Window 2 — missing data, sourced, and where it belongs

For each concrete gap: what Window 2 needs, where the data would actually come from, and whether it
is a **Layer 1** (mechanical, identity-based) or **Layer 2** (judgement, context-dependent) addition
— the same test already implicit in how `party_kind`/`is_negator` (Layer 1, mechanical name-lexicon)
differ from `polarity`/`connective` (Layer 2, context judgement).

### 5.1 Constitutional-location (T2.1: spirit/soul/heart/mind/body)
**Missing:** no lexicon, no column, anywhere. **Source:** a bounded, closed set of Hebrew/Greek nouns
(`ruach`/`nephesh`/`lev`/`basar` and their Greek equivalents `pneuma`/`psyche`/`kardia`/`sarx`,
etc.) — the SAME shape as `party_kind`'s own name-lexicon (a fixed vocabulary, not a context
judgement). **Recommend: Layer 1, mechanical.** A new column (e.g. `constitutional_level`) populated
from a new T-code cluster (parallel to T7/T8/T9), using the identical mechanism `party_kind` already
uses — no new architecture, just a new lexicon and one more `cluster_strong` lookup in
`_layer1_fields`.

### 5.2 Faculty domain (T3.1–T3.11: perception/cognition/memory/affect/creativity/volition/agency/
moral-evaluation/conscience/conscientiousness/relational-capacity) — **RETIRED, 2026-09-08**

**Update, superseding everything below in this subsection:** traced to full provenance and retired
by researcher verdict, escalation #1598 Phase D
(`iba/docs/1598-phase-d-faculties-provenance-v1-20260908.md`) — faculties are real but not
verse-derivable, foreign to the Bible's own vocabulary, and no individual faculty exists or acts on
its own; no harm to the study if omitted. All 33 `T3.x` catalogue rows set `status='dropped'`,
verified live. **The gap this subsection originally described no longer needs closing** — the
"missing lexicon/column/note_type" analysis below is retained for provenance only, not as an open
item.

**Missing:** no lexicon, no column, no note_type rule — the single biggest gap (~30/131 catalogue
rows). **Source:** harder than 5.1 — many faculty terms are genuinely polysemous in context (a
"seeing" verb can be literal sight or spiritual perception), so a pure mechanical tag would
mis-classify real cases. **Recommend: hybrid**, mirroring a pattern the schema already uses
(`is_negator` mechanical + `polarity` judgement is the live precedent for exactly this shape): a
mechanical *candidate* tag from a new T-code lexicon (cheap, runs on every code, flags likely
domain-membership) **plus** a Layer 2 note_type (`noun_relational` and/or `noun_severity`, pending
your own pairing decision from the first pass) to confirm or override in context. Neither half
replaces the other.

### 5.3 Angelic vs. adversarial party distinction (T1.7 / T4.6 / T2.10)
**Missing:** `party_kind`'s 3-value grain collapses both to `non_human`. **Source: already exists —
T4 (Adversarial) and T9 (Party-Angelic) are already separate, populated `cluster_strong` groups.**
The data is not missing at all; it is discarded at the `_PARTY_CLASS_TO_KIND` mapping step in code.
**This is the cheapest fix in the whole report** — no new lexicon, no new judgement call: either
expose the finer `cluster_strong.cluster_code` directly as an additional Layer 1 column (e.g.
`party_class`, keeping `party_kind` as the coarse rollup), or stop collapsing and make `party_kind`
itself 4-valued. Pure code change against data already on hand.

### 5.4 Genre / literary register (T7.2.2 / T7.2.4)
**Missing:** no verse-level home since `#1451` dropped `passage` dependency (§3, CA-11/CA-12).
**Source options:** (a) manual/LLM judgement per verse — expensive, Layer 2; (b) a mechanical proxy —
**the retired `passage.suggest_boundary` step already computed exactly this kind of cheap proxy
signal** (`narrative_morph` density, legacy book-level genre tag, paragraph/chapter markers) before
it was orphaned by the same `#1451` redesign that dropped `passage_id`. **Recommend:** revisit
whether that already-written signal-computation logic can be repointed at a per-verse column instead
of a per-passage one — the mechanism exists and was built once already; it lost its storage target,
not its logic.

### 5.5 Aspect/tense for eschatological trajectory (T5.6)
**Missing:** no dedicated column — `#1549` itself notes "aspect is genuinely relevant and already
mechanical," but nothing extracts it; an analyst or the Layer 2 LLM call has to re-parse
`morph_code`'s aspect slot from scratch every time. **Source: fully available in `morph_code`
already**, unextracted. **Recommend: Layer 1, mechanical** — a cheap `aspect` column
(perfect/imperfect/durative, etc.), parsed the same way `testament`/`narrative_morph` already are.
Side benefit, not the main point: removes repeated re-parsing from every future Layer 2 LLM call,
which is also a token-cost saving.

### 5.6 Evidence grounding (not a catalogue gap, but the same "missing data" logic)
`evidence_text` (§2, CA-10) is the same class of problem in the other direction: the *column* exists,
the *data* doesn't. Window 2 synthesis has no way to audit any Window-1 finding's grounding without
it. Flagged here as a Window-2-facing consequence, not only a Layer-2 internal defect.

---

## 6. `role`/`status` redesign — researcher proposal, checked against live data

**Researcher's model, verbatim, this round:** *"role is important. to me it defines weather the word
has analytic value. broadly speaking: likely to be a characteristic (this can be deducted from the
M-code); likely to be a qualifyer (most probably deductable from the morh_code) a qualifyer is a word
that enrich or is coupled with a M-code; function: a word that is gramatical but with no real pact.
the latter two roles is likely to be T-code. if strong is a backfill, it need to surface hear."*

**Restated, to confirm the model before validating it:** `role` should stop being a pure grammatical
classification and become an **analytic-value** classification, with (at least) three values —
**characteristic** (the word IS a characteristic term — signalled by M-code cluster membership),
**qualifier** (a word that enriches/couples with a characteristic without being one itself — signalled
by `morph_code`, e.g. its part of speech), and **function** (grammatical, no analytic weight — the
current `function` value, largely unchanged). Qualifier and function are both expected to end up
T-code-classified, not M-code-classified. Separately: a code whose `strong` row originated from an
automated backfill sweep, rather than deliberate registry-word onboarding, needs that fact visible
at the row level, not buried in a run-level message.

### 6.1 Checked against real data — how well would characteristic/qualifier/function actually split the corpus

Cross-tabbed every live `verse_lexical` row's current `role` against its `strong`'s cluster
membership (`cluster_strong`, corpus-wide, not sampled):

| Current `role` | Cluster bucket | Rows | Share of that role |
|---|---|---|---|
| content (363,253) | **UNTAGGED anywhere** | 132,477 | 36.5% |
| content | T2 excluded-from-analysis | 86,469 | 23.8% |
| content | **M-tagged (characteristic candidate)** | 60,077 | 16.5% |
| content | T3 Operations | 59,106 | 16.3% |
| content | T4–T9 special (negator/connective/party) | 24,654 | 6.8% |
| content | FLAG needs-review | 470 | 0.1% |
| function (181,319) | **UNTAGGED anywhere** | 113,185 | 62.4% |
| function | T4–T9 special (negator/connective/party) | 39,217 | 21.6% |
| function | T2 excluded-from-analysis | 28,900 | 15.9% |
| function | M-tagged | 15 | ~0% |
| function | T3 Operations | 2 | ~0% |

### 6.2 What this confirms, and what it complicates — real, not glossed over

- **The `characteristic` half of the model is directly buildable today, cheaply:** 60,077 content-role
  rows already resolve to an M-tagged strong — `characteristic` could be computed the same
  mechanical way `party_kind` already is (a `cluster_strong` lookup, no new lexicon needed).
- **`function` is only partly a T-code story.** The model says function is "likely to be T-code," but
  **62.4% of function-role rows have no cluster tag of any kind** — these are the raw Hebrew H9xxx /
  Greek PREP-PRT-CONJ-ART formatives, whose function-ness already comes entirely from `morph_code`
  pattern-matching (`classify_role`), not from any strong-code lexicon. Only the T5 (Negator)/T6
  (Connective) minority genuinely needs a `cluster_strong` lookup. **The two mechanisms are different
  and both real — this model should keep them distinct, not imply function reduces to "look up its
  T-code."**
- **Two large, unresolved buckets stand between the model and a clean three-way split — genuine
  open questions, not decided here:**
  1. **132,477 content-role rows (36.5%, the single largest bucket) have no cluster tag at all.**
     Are these `qualifier` candidates not yet T-coded, ordinary un-analytic vocabulary (e.g. "house,"
     "day" in a narrative aside), or a mix that needs its own sub-classification? At over a third of
     all content words, this can't be a residual category — it needs its own answer before
     `qualifier` can be built.
  2. **86,469 content-role rows (23.8%) are tagged T2 — "excluded from analysis" by the T-code
     system's own definition** (`cfg_table.use` for `cluster`). Under the proposed model, does T2
     membership mean these are correctly excluded (genuinely non-analytic), or does it mean some of
     them are actually `qualifier`s that were bulk-dumped into the exclusion bucket before this
     finer distinction existed? This is consequential — it's the second-largest content bucket.
- **T3 "Operations" (59,106 content rows) is my own inference as the `qualifier` candidate, not a
  confirmed mapping.** Its own live `cfg_column` definition is narrower and different: *"1 if the
  code denotes a human operation/movement"* — a verb-of-action classification, not explicitly "a word
  that enriches or is coupled with a characteristic." These may turn out to be the same thing in
  practice, or T3 may need to be split, or `qualifier` may need an entirely new, not-yet-built T-code
  group. **Not decided here — flagged for your confirmation before anything is built on top of it.**

### 6.3 Backfill provenance — the data already exists, just isn't surfaced

Checked live: `strong.origin` (`'word'` | `'backfill'`, stamped at creation, `bootstrap_strong_
origin_column_20260811.py`) **already records exactly the distinction asked for** — `'word'` = a
registry word's own deliberate onboarding (`detail()`); `'backfill'` = an automated book-sweep
completeness pull (`backfill_meaning_for()`), run specifically to fill `status='unregistered'` gaps
before a build.

**This is a far bigger population than `status='unregistered'` tracks, and a different question
entirely** — `unregistered` (559 rows) means *no* `strong` row exists yet; `origin='backfill'` means
a `strong` row *does* exist, but arrived through the automated sweep rather than deliberate
registry-word study. Checked live: **10,517 of 15,293 strongs (68.8%) originated via backfill, not
registry-word onboarding — and 398,405 of 544,572 live `verse_lexical` rows (73.2%, nearly three
-quarters of the entire corpus) rest on a backfill-origin strong.** This is the majority state of the
corpus, not an edge case, and it is currently **invisible on `verse_lexical` and absent from
`cfg_column` entirely** — confirmed, 0 columns reference it.

**This is a clean, low-risk fix, the same shape as every other Layer-1 denormalization already
built** (`language`, `testament`, `surface` all copy from elsewhere onto `verse_lexical` for exactly
this reason — so a reader/LLM never has to chase a second table for a fact already known at build
time): denormalize `strong.origin` onto `verse_lexical` (e.g. a new `strong_origin` column), right
alongside `role`/`status` where this analysis is actually used.

### 6.4 Architecture correction, confirmed by the researcher on escalation #1598

`characteristic`/`qualifier` are **confirmed interchangeable per-occurrence** (the same lexeme can be
either, depending on the verse — the researcher's own instruction, not inferred) — the same swap
applies to characteristic-action vs. generic-operation on the verb side. The specialist T-codes
classify by **content/meaning**, the same way M-codes do — the part-of-speech breakdown in §3a/§3b of
`1598-cluster-reallocation-scope-and-method-v1-20260908.md` was a triage signal for finding candidates,
never the classification rule itself, and dual M-code/T-code membership is the expected shape of a
genuinely dual-natured word, not an anomaly. **Consequence for `role`'s own redesign:** the
characteristic/qualifier axis cannot be a single static Layer 1 value — it needs the same two-stage
shape `is_negator` (Layer 1, mechanical candidate) → `polarity` (Layer 2, per-verse judgement)
already proves out in this schema. Full detail and the standing-rule constraints on how the
underlying reallocation itself must proceed: escalation #1598.

---

## 7. Corrective Actions Register

| CA# | Item | Column / table | Type | Proposed action | Blocked on |
|---|---|---|---|---|---|
| CA-1 | `morph_code` NULL, 1,082 rows, feeds a silent `role='content'` default | `verse_lexical.morph_code` | data gap, downstream accuracy | Confirm whether NULL is expected for these codes; if not, source the missing morph slice; either way, stop the silent content-default for NULL-morph Greek codes | — |
| CA-2 | `status='unregistered'` residual (559) — permanent or backfill-pending? | `verse_lexical.status` | needs verification | Run a direct check: are the 559 genuinely absent from STEP, or just not yet re-run through `backfill_meaning_for`? | — |
| CA-3 | `resolved_sense`'s `cfg_column.use` text is false (says populated for 'resolved' rows; is 0% populated) | `cfg_column` row for `verse_lexical.resolved_sense` | governance-compliance / doc drift | Update `cfg_column.use` to state the column is permanently NULL by design (#1575) | Small, no judgement needed |
| CA-4 | Three unrelated live "T"-numbering schemes (T-code clusters, catalogue T-codes, legacy processing tiers) | project-wide documentation | naming collision | Disambiguate the names (rename or explicitly annotate one scheme) | Design choice |
| CA-5 | `is_negator`'s `cfg_column.use` text names the wrong source table (`cfg_lexical_code_class` vs. real `cluster_strong`) | `cfg_column` row for `verse_lexical.is_negator` | governance-compliance / doc drift | Correct the `use` text | Small, no judgement needed |
| CA-6 | `party_kind`'s `cfg_column.use` text has the same wrong-source-table drift | `cfg_column` row for `verse_lexical.party_kind` | governance-compliance / doc drift | Correct the `use` text | Small, no judgement needed |
| CA-7 | `updated_at` has no `cfg_column` row at all | `cfg_column` (missing row) | governance-compliance | Register the column now — behaviour already documented in code/#1527 | Small, no judgement needed |
| CA-8 | `verse_lexical_note.passage_id`'s purpose no longer matches live use (always NULL post-#1451) | `cfg_column` row for `verse_lexical_note.passage_id` | doc drift / open design item | Decide: drop the column, or update its purpose text to reflect vestigial status — matches #1451's own still-open item | Researcher decision |
| CA-9 | `resolution_status='not_supported_this_language'` never exercised, 0/173 | `verse_lexical_note.resolution_status` | untested path | Deliberately test a Hebrew-only rule against a Greek verse | Low priority |
| CA-10 | `evidence_text` 100% unpopulated, every row, ever | `verse_lexical_note.evidence_text` | **purpose not met at all — high priority** | Decide: enforce as a required field (write-time gate), or formally merge into `value_text` since practice already folds evidence there | Researcher decision |
| CA-11 | `passage.genre` purpose no longer achievable in the live pipeline | `cfg_column` row for `passage.genre` | doc drift / open design item, high value | Give genre a real per-verse home (see §5.4's proxy-signal recommendation) | Researcher decision |
| CA-12 | `passage.lexical_complete_at` orphaned by the same #1451 redesign, not previously traced | `cfg_column` row for `passage.lexical_complete_at` | doc drift / open design item | Same disposition as CA-11 — completeness tracking needs a new home too, not just genre | Researcher decision |
| CA-13 | Constitutional-location lexicon missing (§5.1) | new `verse_lexical` column | missing data | Build as Layer 1 mechanical, new T-code cluster | Researcher decision (scope/timing) |
| CA-14 | Faculty-domain classification missing (§5.2) | new `verse_lexical` column + note_type | missing data | Build as hybrid (mechanical candidate tag + Layer 2 judgement) | Researcher decision (scope/timing, and the noun_relational/noun_severity pairing question) |
| CA-15 | Angelic/adversarial collapsed at the code level despite data existing (§5.3) | `verse_lexical.party_kind` (or new `party_class`) | cheapest fix in this report | Stop collapsing T4/T9 in `_PARTY_CLASS_TO_KIND`, or add a finer column alongside the existing one | Researcher decision (which shape) |
| CA-16 | Genre proxy-signal logic already built, then orphaned (§5.4) | new verse-level column | missing data, reusable code | Repoint the retired `passage.suggest_boundary` proxy logic at a per-verse target | Researcher decision |
| CA-17 | Aspect not extracted from `morph_code` despite being "already mechanical" (§5.5) | new `verse_lexical` column | missing data, low cost | Add a mechanical `aspect` column, same pattern as `testament`/`narrative_morph` | Researcher decision (scope/timing) |
| CA-18 | `role` redesign (content/function → characteristic/qualifier/function) — 36.5% of content rows and 62.4% of function rows don't cleanly resolve under the proposed model yet (§6.2) | `verse_lexical.role` | design decision, large | Resolve the two open buckets (untagged content, T2-tagged content) and confirm/build the `qualifier` T-code group before building the 3-way split | Researcher decision — two open sub-questions in §6.2 |
| CA-19 | `strong.origin` ('word'/'backfill') exists but is not surfaced on `verse_lexical` at all (§6.3) | new `verse_lexical` column (`strong_origin`) | missing data, low cost, high value | Denormalize `strong.origin` onto `verse_lexical`, same pattern as `language`/`testament`/`surface` — 73.2% of the live corpus rests on backfill-origin strongs, currently invisible at the row level | Researcher decision (scope/timing) — no design ambiguity, purely additive |

Nothing in this register has been applied. Per your own instruction this round and the standing rule
against deciding judgement calls unilaterally, every item above is presented for your disposition,
not actioned.
