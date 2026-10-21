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

---

## 8. Layer 1 redesign, round 1 — researcher instruction, verbatim, 2026-09-08 (this session)

> "section 4 is entirely changed in terms of how t-codes and m-codes will be used in the
> lexical.build. each word will be assigned its M or T code. To be decided: morph_code is only
> relevant for M-code words; its preliminary role is set based on the Cluster code
> (Char|qualifyer|None; status: redefined to show meaning data readiness - if full meaning of
> strong is available Meaning Ready|Meaning to be pulled| if T2 then Meaning not applicable.
> Resolved_sense : work with me to identify which field from meaning to pull in; ambiguity_note :
> this column is now redundant. what I would like to see is this column is renamed to pairing. this
> is where the morph is used to show the binding of the word to the other words in the verse;
> surface : cannot be blank and must be the word that is used in the strong for the surface, the
> actual translated word; is_negator - need attention not sure what you are saying in the analysis;
> narrative_morph - ensure greek is included - i want to know more about htis; gloss_consistent_in_verse
> : if the word is multi-ordinal then it is the gloss for the combined strong meaning in the verse;
> party_kind : is this where the cluster code goes? ; update_at is a required field. I suggest you
> first work on the refinement of layer 1 and lets get that right."

Nothing below is applied — same standing rule as §7. Per your own steer this round ("first work on
the refinement of layer 1"), this section is scoped to Layer 1 (`verse_lexical`) only; T-code
completeness / Window 2 (§4/§5 above) is superseded by the "each word gets an M or T code" framing
and will be revisited once Layer 1 is settled, not in parallel.

### 8.0 Architecture shift — §4 above is superseded

§4's own framing (T-code groups sized, most content words untagged) was already moving this
direction before this instruction — escalation #1598 (completed today, 13:47) reallocated the
M/T-code pools and left "4,155 common nouns + 2,651 proper nouns" in the still-untagged pool, not
zero. Universal M-or-T assignment is the target state this round names explicitly; §4/§5 are marked
provenance-only above, not repeated here.

### 8.1 Direct answers — questions you asked me, not decisions for you

**`is_negator` — what CA-5 was actually saying:** the column's own `cfg_column.use` text (the
governance record of its purpose) claims it's sourced from `cfg_lexical_code_class WHERE
class='negator'`. Confirmed live, again, this round: **that table is never read.** The real source,
in the actual running code (`lib/lexical.py:load_code_classes`), is `cluster_strong WHERE
cluster_code='T5'` (the T5/Negator cluster's own tagged strongs — 7 live). The *behaviour* is fine
and already matches your "cluster code" model; only the **documentation text is wrong** — it names a
dead table instead of `cluster_strong`. Same defect, same fix, on `party_kind` (CA-6, below).

**`party_kind` — yes, confirmed, this is exactly where the cluster code goes.** Live code
(`_PARTY_CLASS_TO_KIND` in `lib/lexical.py`): a code's `party_kind` is set only when that code
itself is a member of `cluster_strong` T4 (Adversarial), T7 (Party-Divine), T8 (Party-Human), or T9
(Party-Angelic) — `divine`/`human`/`non_human` respectively (T4 and T9 currently collapse together
into `non_human`, CA-15 in §7). Its own `cfg_column.use` text has the identical wrong-source-table
drift as `is_negator` (names `cfg_lexical_code_class`, not `cluster_strong`) — same fix.

**`narrative_morph` — what it currently is, live:** a Hebrew-only flag, set from `morph_code`'s own
TAM (tense-aspect-mood) slot at a fixed position (`HV<stem><TAM>...`, index 3). Two values today:
`wayyiqtol` (TAM='w' — the narrative "and-he-did" verb form that carries Hebrew narrative sequence)
and `az_imperfect_opening` (TAM='i' AND a sibling code in the same span is H0227 "az"/"then" — a
named, narrow idiom, verified live against Exod.15.1). It is deliberately restricted to Hebrew
because Greek's TVM tagging scheme doesn't use the same TAM-letter convention at all — there's no
direct equivalent slot to read the same way. **Extending it to Greek is a real design task, not a
one-line change:** it needs its own definition of what "narrative morph" means for Greek (Greek's
own narrative-sequencing signal is more the aorist-vs-imperfect-vs-historical-present distinction in
context than a single morph-code flag) before any code gets written — I don't have a Greek
equivalent to propose yet without more direction from you on what Greek narrative signal you want
this to capture.

### 8.2 Restated per-column, so you can correct anything I've misread before I go further

- **`morph_code`** — **flagged by you as "to be decided," open.** One real conflict worth surfacing
  before that's decided: `morph_code` is not only a resolved_sense input — it's *already* load-bearing
  for three other Layer 1 mechanisms that would need M-code words to still carry it, or a replacement:
  `role` classification (Greek PREP/PRT/CONJ/ART tags come from `morph_code`), `narrative_morph`
  (Hebrew TAM slot), and stem/voice selection. If `morph_code` becomes M-code-only, each of those
  three needs its own answer for T-coded words — not assumed here.
- **`role`** — restated: preliminary value set from the code's own cluster-code membership, not
  grammatical classification: **`characteristic`** (M-code member), **`qualifier`** (T-code member —
  which T-codes qualify is itself still open, see CA-18's own two unresolved buckets in §7, now
  reframed under this model rather than content/function), **`None`** (no cluster code yet — under
  8.0's "every word gets a code" target, is `None` meant as a permanent third value or a transitional
  state that should shrink to ~0 as coverage completes? Not decided here.)
- **`status`** — restated: no longer resolution-outcome, now meaning-data readiness —
  **`Meaning Ready`** / **`Meaning to be pulled`** / **`Meaning not applicable`** (T2). One thing to
  confirm before building this: "full meaning of strong is available" — ready against *what* store?
  Candidates checked live this round, §8.3.
- **`resolved_sense`** — per your instruction, joint: see §8.3.
- **`ambiguity_note` → `pairing`** — restated: renamed, redefined from "flag a sibling/base-fallback
  meaning ambiguity" to "show the morph-based binding of this code to other codes in the same verse."
  §8.4 below sets out what data is already on hand for this and what isn't decided yet.
- **`surface`** — restated as an invariant, not a redesign: never blank, and scoped to the single
  aligned English word for *this* code specifically. This is what escalation #1591 (192 rows) already
  found broken — 59 live rows are blank outright, and the confirmed defect cases (Deut.7.18 pos.2,
  1Thess.1.1 pos.17) are exactly the "not the actual word for this code" failure you're naming.
  Restates the existing gate, doesn't relax it — #1591 stays gated pending the repair-method decision
  already on record there.
- **`is_negator` / `party_kind`** — see §8.1, doc-text fix only (CA-5/CA-6 already had this; no
  behaviour change).
- **`narrative_morph`** — see §8.1; Greek extension needs your steer on what signal to capture before
  I can propose a mechanism.
- **`gloss_consistent_in_verse`** — restated: for a multi-ordinal span (>1 live code sharing one
  span/surface — 118,906 of 378,094 live spans, 31.4%, confirmed live this round; e.g. Rom (sample)
  span 534082: `G1722` "in" [PREP] + `G0054` "purity" [N-DSF] both surfaced as one English word
  "purity"), this column should read as the gloss for the **combined** sense of every code in that
  span, not evaluated per-code. This already supersedes escalation #1596 (the column was found
  structurally dead post-#1575) — not a second, separate fix.
- **`updated_at`** — restated: register it in `cfg_column` now (CA-7 already proposed this) — you've
  additionally called it *required*. Live check: 113,684/544,572 rows (20.9%) currently have
  `updated_at IS NOT NULL` (only rows that have gone through a real content correction since the
  #1520 identity-stable-write redesign get it set — `INSERT` never populates it). "Required" needs one
  clarification: required as in *every future correction must set it* (already true, mechanically, in
  `write_readings_for_span`), or required as in *every row must carry a non-NULL value*, which would
  mean stamping it on INSERT too (a real behaviour change, not just a `cfg_column` registration)?

### 8.3 `resolved_sense` — candidate source fields, checked live, for joint decision

Five live tables carry strong-level meaning text. Sampled against H0430G ("God") and G2192 ("to
have/be" — the same high-polysemy word #1575's own investigation used):

| Table.column | Grain | H0430G sample | G2192 sample | Shape |
|---|---|---|---|---|
| `strong.stepGloss` | 1 row/strong | "God" | "to have/be" | Shortest possible gloss — already denormalized onto `verse_lexical.language`'s sibling column? No — not currently pulled onto this table at all. |
| `strong_sense.head` | 1 row/strong | "God" | "to have/be" | Identical to `stepGloss` in both samples checked — worth confirming whether it ever diverges before treating it as a distinct source. |
| `strong_meaning_parsed.gloss` | many rows/strong (stem/sense-structured) | 1 row: "The Deity;" | 8+ short rows: "to hold", "to seize, possess", "to have, possess"... | The table `resolved_sense` used to pull from, stem/voice-narrowed (`_select_stem_text`) — this is the mechanism #1575 turned off for being unreliable at scale, not a table that's gone. |
| `strong_meaning_tree.sense_text` | many rows/strong | (thin/none for this word) | 1 row, ~2,400 chars, HTML-tagged LSJ prose with embedded `<ref>`/`<b>` markup | The exact "generic dump" #1575 removed — not a candidate as-is. |
| `strong_lsj_parsed.gloss` | many rows/strong, Greek only | n/a (Hebrew) | rows like "have, hold" / "possess, propertied class, wealthy man..." | Greek-only, still verbose (36,199 rows corpus-wide) — same class of problem as `strong_meaning_tree`. |

Given `resolved_sense` is now scoped to M-code words only (already decided, #1527/#1575) rather than
every code, the volume problem #1575 was solving (2,652-char values on ~277 strongs, all codes) is
much smaller if re-scoped to only the M-tagged subset — but which field, and whether stem-narrowing
comes back for that subset, is the open question. Need your steer on: (a) `stepGloss`/`strong_sense.
head` (shortest, safest, but a single fixed gloss with no stem sensitivity), or (b)
`strong_meaning_parsed.gloss` re-narrowed by stem/voice the way the old mechanism did (richer, but
this is exactly the mechanism that produced the values #1575 rejected — though that rejection was
about running it on *every* code, not the smaller M-code-only set), or (c) something else.

### 8.4 `pairing` (was `ambiguity_note`) — what's on hand, what isn't decided

The multi-ordinal span data in §8.2 (`gloss_consistent_in_verse`) is the same underlying fact this
would draw on — codes that already share a span/surface (`G1722`+`G0054` above) are the clearest
case of "binding." Two things not decided here: (1) does `pairing` cover *only* same-span
multi-ordinal binding, or also cross-span syntactic binding (e.g. a verb and its object in different
spans) — the latter would need a real dependency signal that doesn't exist in `morph_code` alone; (2)
value shape — a flag, a pointer to the paired `verse_lexical.id`(s), or free text describing the
binding. Not proposed here; needs your direction before it's built.

### 8.5 Open questions this round, consolidated

1. `morph_code` M-code-only scope — how do `role`, `narrative_morph`, and stem/voice selection work
   for T-coded words if `morph_code` stops being populated for them? (§8.2)
2. `role`'s `None` value — permanent third state, or transitional until M/T coverage is universal?
   (§8.2)
3. `status`'s "full meaning of strong is available" — ready against which table(s)? (§8.2, §8.3)
4. `resolved_sense` — which field (§8.3: (a)/(b)/(c))?
5. `updated_at` "required" — every correction (already true), or every row incl. INSERT (new
   behaviour)? (§8.2)
6. `narrative_morph` Greek — what signal should it capture? (§8.1)
7. `pairing` — same-span only, or cross-span too; and what value shape? (§8.4)

---

## 9. Round 2 — researcher answers, verbatim, 2026-09-08 (same session)

> "morph_code stay as is today, role is the M/T - code; resolve sense = strong_meaning_parsed.gloss
> (100 char only) ; pairing - same span only - not sure of format, would like to see examples."

Closes questions 1 and 7's scope half; narrows 2 and 4; leaves 7's format open pending examples,
below.

### 9.1 `morph_code` — closed

Stays exactly as it is today — populated for every code, no M-code restriction. Question 1's
dependency conflict (role/narrative_morph/stem-voice all reading it) doesn't arise; nothing changes
here.

### 9.2 `role` = the M/T-code — real conflict found, needs your call

Understood: `role`'s value becomes the code's own `cluster_strong.cluster_code` directly (e.g.
`"M16"`, `"T5"`), not a translated category label — simpler than the Char/Qualifier/None model,
and question 2 (is `None` permanent) dissolves on its own: `None` is just "no cluster code assigned
yet," and shrinks as coverage becomes universal (8.0).

**One real conflict, checked live, not assumed:** `role` is a single scalar column, but **96 live
strongs carry more than one `cluster_code` at once** (`cluster_strong`, deduped by strong, corpus-
wide check). Not a rare edge case — includes both M+T combinations (`H7665`: `M24,T3`; `H6819`:
`M31,T2`) and T+T combinations (`H7070J`: `T13,T14`). Three example rows:

| strong | live cluster_codes |
|---|---|
| H1544 / G1493 | M55, T2, T12 |
| H8615A | M03, T12 |
| H7070J | T13, T14 |

**Needs your decision:** does `role` take a priority pick (e.g. M-code wins over T-code if both
present — but which T-code wins if two T-codes are both present, as `H7070J` shows that's real too),
or does it become multi-valued (comma-list, same shape `cluster_code` values already take in the
`GROUP_CONCAT` above)? Not decided here — this is exactly the kind of conflict that only shows up
once real data is checked, not before.

### 9.3 `resolved_sense` = `strong_meaning_parsed.gloss`, 100-char cap — algorithm confirmed, one loose end

Plan: same exact-variant / base-fallback lookup `resolve_code()` already runs (unchanged), gloss rows
joined with `"; "` in existing sort order, then capped to 100 characters. Re-checked against the
three M-code strongs that had **zero exact-variant rows** in the first sample (§8.3) to confirm the
base-fallback catches them, not just the easy cases:

| strong | exact rows | base-fallback rows | joined (first 100 chars) |
|---|---|---|---|
| H4428G "king" | 0 | 2 | `king; Aramaic equivalent: me.lekh (מֶלֶךְ "king" H4430)` (fits whole, 55 chars) |
| G1492G "to perceive" | 0 | 4 | `to know, to possess information; recognize, realize, to come to know; to understand, to be able to u` |
| H1696G "to speak" | 0 | 9 | `to speak, declare, converse, command, promise, warn, threaten, sing; (Qal) to speak; (Niphal) to spe` |

Base-fallback works correctly for all three — no gap there. **One loose end, visible in the table
above:** a flat 100-char cut lands mid-word twice (`"...to u"`, `"...to spe"`). Confirm: hard cut at
exactly 100 regardless, or cut at the last complete clause (`;`-boundary) at-or-under 100 chars
(cleaner, but the resulting length then varies row to row rather than being a fixed 100)?

### 9.4 `pairing` — same-span confirmed; three real format candidates, from real spans

Scope closed: same-span only (question 7's first half). Format still open — you asked to see
examples, so here are three, applied to the same three real live spans (2, 3, and 4 codes), from
cheapest/thinnest to richest/most-built:

**Span A — 2Cor.6.6 span 534082, position 0, surface "purity" (Greek, preposition+noun elision):**
`G1722` [PREP, function] + `G0054` [N-DSF, content]

**Span B — Jer.23.12 span 534253, position 8, surface "for" (Hebrew, conj+prefix-prep+suffix-pronoun,
all function):** `H3588A` [HTc, content] + `H9003` [HRd, function] + `H9034` [HSp3fs, function]

**Span C — Jer.23.12 span 534248, position 3, surface "slippery paths" (Hebrew, noun+3×
prefix/suffix formatives):** `H2519` [HNcfpa, content] + `H9028`/`H9005`/`H9038` [function ×3]

| Format | What it stores | Span A → `pairing` values (ordinal 0, 1) | Span B → (0, 1, 2) |
|---|---|---|---|
| **1 — sibling ordinals** (cheapest — no new fact, just the existing span grouping made explicit on the row) | comma-list of the other `code_ordinal`s in this span | `"1"` / `"0"` | `"1,2"` / `"0,2"` / `"0,1"` |
| **2 — sibling code+role list** (self-contained — a reader never needs a second query to see what this code is bound to) | comma-list of sibling `strong (role)` | `"G0054 (content)"` / `"G1722 (function)"` | `"H9003 (function); H9034 (function)"` / `"H3588A (content); H9034 (function)"` / `"H3588A (content); H9003 (function)"` |
| **3 — interpreted binding** (richest, and closest to your original wording, "morph is used to show the binding" — but a real new build: needs a morph-code attachment lexicon, e.g. `HRd`=prefixed relator, `HSp3fs`=suffixed pronoun, `PREP`=governs its noun, not just a join against data already on hand) | free text naming the grammatical relationship | `"governs G0054 (dative, 'purity')"` / `"object of G1722 (preposition 'in')"` | `"prefixed by H9003 (relator); suffixed by H9034 (3fs pronoun)"` / … |

Format 1 is free (the grouping already exists via `span_id`/`code_ordinal`, this just surfaces it on
the row) but arguably adds nothing a reader couldn't already get by querying the span. Format 2 is
still cheap (one extra join, no new interpretation logic) and self-contained. Format 3 is the one
that actually reads as "binding," but is a real design+build task (a prefix/suffix morph-code
lexicon doesn't exist yet in this codebase), not a join. Your call on which — or a fourth shape not
listed here.

### 9.5 Open questions, carried forward

1. `role` multi-cluster-code conflict (§9.2) — priority pick, or multi-valued?
2. `resolved_sense` truncation boundary (§9.3) — hard 100-char cut, or clause-boundary cut ≤100?
3. `pairing` format (§9.4) — 1 / 2 / 3 / other?
4. Still open from §8.5, untouched this round: `status`'s meaning-readiness source table (Q3),
   `updated_at` "required" scope (Q5), `narrative_morph` Greek signal (Q6).

---

## 10. `role`'s multi-cluster-code conflict, checked — 59 of 96 are BY DESIGN, 37 are a real conflict

Researcher instruction, verbatim, this round: *"can you check the 96 multi codes to see if it is
errors or intended."* Checked live, all 96, not sampled.

### 10.1 What the check found

Every one of the 96 live `cluster_strong.cluster_code` values was traced against the `cluster`
table's own description text (the governing record of what each code means and whether it's meant
to coexist with an M-code):

- **59 of 96 are confirmed BY DESIGN, not an error.** `cluster.description` for T3 (Operations), T7
  (Party-Divine), T8 (Party-Human), T9 (Party-Angelic), T10 (Places), T11 (Corporate-Collective), T12
  (Objects-Artifacts), T13 (Natural-World), and T14 (Body-Parts) each say, verbatim, some form of
  *"referent-identity classification, orthogonal to the thematic M-code axis... a code can carry both
  an M-cluster assignment and this one"* — all nine created 2026-09-08 under escalation #1598,
  researcher-approved. `H0639G` ("face: anger," M02+T14) and `H3027H` ("hand: power," M72+T14) are
  named as the model examples directly in `cluster`'s own T14 description — "the body-part identity
  and its figurative characteristic sense are two different facts about the same code." This is not
  a `role` conflict at all — it's two genuinely different axes that happen to live in the same
  junction table. **Consequence for `role`:** T7-T14 (referent-identity) don't belong inside `role`'s
  own M/T value at all — they're a separate fact, the same shape `party_kind` already is for T7/T8/T9
  specifically. T10-T14 are the same kind of fact but don't have their own `verse_lexical` column yet
  (this is CA-13/CA-15/CA-16 from §7, now confirmed as one consistent pattern rather than three
  separate open items — a generalized referent-identity column, `party_kind` extended or a sibling
  column, not `role` itself).
- **7 are M-code + `FLAG`** — `FLAG` (`"Flagged for Review"`) isn't a competing classification, it's a
  review marker on the M-code assignment itself. Not a conflict; resolves when the flag is cleared,
  not by picking between two classifications.
- **37 are a real, live conflict: a `cluster_strong.cluster_code='T2'` row (Supplementary — the
  code the T-code system's own definition treats as excluded, no inner-being significance) coexists
  with a live M-code row for the SAME strong.** No `cluster.description` text says T2 and an M-code
  are meant to coexist the way T7-T14 explicitly do — T2 is the one code whose whole point is "not
  analytically relevant," directly contradicting an M-code's "this word IS a characteristic." Full
  list, checked corpus-wide:

  G1414(M23), G1415(M23), G1493(M55,+T12), G1494(M55), G1495(M55), G1654(M05), G1764(M15),
  G1832(M31), G1888(M26), G2192(M23), G2712(M55), G2900(M23), G2999(M36), G3873(M15), G3918(M15),
  G4229(M28), G4840(M15), G4894(M15), G4997(M61), G5379(M51), G5400(M01), G5591(M15), G5600(M28),
  H0034(M09), H0061(M03), H1544(M55,+T12), H2632(M72), H3027W(M23), H4751(M03), H4941I(M12),
  H4941J(M12), H6094(M10), H6105A(M23), H6640(M28), H6819(M31), H7218K(M24), H7293(M08)

  **Provenance splits this 37 into two distinct sub-shapes, not one uniform bug:**
  1. **~14 carry NO rationale on either row** (`source='old-system-migration'` on both, e.g. G1414,
     G1415, G1654, G2900, G2999, G5400, G5591, H3027W, H4751, H7293) — raw carry-over from the
     pre-T-code system, migrated wholesale with the two facts never reconciled against each other.
     Genuinely undeterminable which (if either) is right from the data alone.
  2. **~23 have the T2 row from the 2026-09-05 `heuristic-family-grouping-v1` bulk sweep**, carrying
     one of two shapes: (a) identical boilerplate rationale regardless of the word ("no inner-being
     significance -- place/person name, body part, divine/idol reference, or generic human-relational
     term") applied to words that already had a real, specific M-code from an earlier pass (e.g.
     `G0080`/"brother" already M14 with a real relational-meaning rationale, then bulk-tagged T2
     anyway) — the sweep does not appear to have checked for pre-existing M-code membership before
     tagging; or (b) the reverse — a real, specific M-code (`family=righteousness-integrity`,
     `family=purity-holiness-sanctification`, etc.) added by that SAME 2026-09-05 pass on top of an
     older, untouched T2 exclusion tag, i.e. the sweep reclassified the word into a characteristic
     family but never retracted the stale exclusion tag it was superseding.

### 10.2 What this means for `role`, and what's left to decide

`role` = the M/T-code (confirmed, round 2) now needs to read only against the **thematic axis** (an
M-code, or a non-referent T-code — T2/T3/T5/T6), not the referent-identity codes (T7-T14), which get
their own column instead. Under that narrower reading, **59 of the 96 stop being a `role` problem at
all.** The 37 T2-vs-M-code strongs are the real open item — not a `role` design question anymore, a
**data-reconciliation** one: for each of the 37, is the T2 tag stale (drop it, keep the M-code), or
was the M-code itself the mistake (drop it, keep T2), checked individually, not batch-decided either
way. Raised as its own escalation (#1605) rather than folded into this design thread, since it's a
concrete repair task with its own disposition, not a `role`-shape decision.
