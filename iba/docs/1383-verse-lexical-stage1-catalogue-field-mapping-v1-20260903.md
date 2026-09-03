# Stage 1 (Window 1) — catalogue questions mapped to the exact answering field

**Filename:** 1383-verse-lexical-stage1-catalogue-field-mapping-v1-20260903.md
**Escalation:** #1383
**Purpose, verbatim (researcher):** the questions answered by Stage 1's lexical must be clearly
isolated and added to the catalogue so there's no doubt where the answer comes from. For every
question, describe practically which field answers it; if the question needs a derived answer, the
lexical build must produce that derivation now, not defer it.

**Scope of this document**: every catalogue question already identified (companion coverage
document) as answerable at Stage 1's own grain — either directly from a single field, or via a
derivation/rollup that Stage 1's own stored data can support without needing Window 2/HIB
information. Questions requiring HIB identification, characteristic-wide behaviour synthesis, or
theological interpretation are out of scope here — they're Stage 2's (or later) job, not
re-litigated in this document.

**Every derivation named below is either already a stored field, or has been folded into the
schema (design doc, revised §5) specifically so it is — nothing here is left as "aggregatable in
principle, build the query later."**

---

## 1. Directly answered by one field

| Question | Field | How |
|---|---|---|
| T7.2.2 — literary form (genre) | `passage.genre` | Direct read. Set once per passage, at the read's own first move. |
| T1.4.1 (half) — grammatical/stem form | `verse_lexical.morph_code` | Direct read — the morph code itself *is* the grammatical/stem-form answer. |

## 2. Directly answered by a `verse_lexical_note` row (one note_type, no join needed)

| Question | note_type | How |
|---|---|---|
| Chain/sequencing test (checklist item, not a catalogue code — feeds T7.2.1's "argument" half partially) | `chain` | `resolution_status`='resolved' if `narrative_morph` fired and a link is recorded; the note itself names the linked code. |
| Logical/causal connective | `connective` | `value_text` names the type (causal/coordinating/purpose) per the connective lexicon (design doc §5.1's `is_negator`-style mechanical lexicon, extended to connectives). |
| Related-words (raw pull) | `related_word` | One row per pulled `strong_related` code — the pull itself is mechanical and total; sorting (same-concept vs. coincidental) is the judgement half, recorded in `resolution_status`. |
| Idiom/combined-span | `idiom` | `value_text` states the combined sense; `resolution_status`='resolved' or 'checked_empty' (negative result recorded explicitly, not omitted). |
| Structural pattern (merism/chiasm/parallelism — Stage 1's detection half only, per the #1443 split) | `structural_pattern` (new) | `related_verse_lexical_ids` names every span involved; `value_text` names the pattern type. Interpretation of what it means stays Stage 2. |

## 3. Answered by a join/derivation across two already-stored fields — the party-kind class

This is the class the researcher's own correction on T0.1.1 opened up (§2/§5 of the coverage
document) — genuinely derived, but from data Stage 1 itself stores, no Window 2 dependency.

| Question | Derivation, stated exactly |
|---|---|
| T0.1.1 — is the characteristic predicated of God, this verse | For the characteristic-term's own `verse_lexical` row: follow its `entity_link` note's `target_verse_lexical_id` (if any) to the target row; read that row's `party_kind`. If the term's own code IS itself a name (no entity_link needed), read its own `party_kind` directly. `party_kind='divine'` → yes; `party_kind='human'` → no, attributed to the human/IB; no resolvable target → `unresolved`, not guessed. |
| T4.1.1 / T4.2.1 — operates from God toward the person / toward God | Same join, both directions: the characteristic-verb's own subject (`entity_link` target) and object (governed-clause target, same note mechanism) are each checked against `party_kind`. `subject.party_kind='divine' AND object.party_kind='human'` → T4.1.1 yes; reversed → T4.2.1 yes. |
| T0.1.2 (raw-fact half only — "is it ever borne by God") | Aggregation of the T0.1.1 derivation above, across every verse in the characteristic-candidate's assembled set (Stage 2's own input-assembly, §4 of the blueprint) — a `COUNT(... WHERE party_kind='divine') > 0` over Stage 1's own per-verse answers. The interpretive half ("what that indicates") stays Stage 2/T0.2.1-class, per §7 of the coverage document. |
| T4.3.1 / T4.4.1 (person-to-person direction) | Same mechanism, needs the human-name lexicon (§5.1 of the design doc — flagged as not yet built). Once built: `subject.party_kind='human' AND object.party_kind='human'`. **Not yet answerable in practice** — the derivation path is designed, the lexicon isn't built. Named here as a build item, not silently assumed done. |
| T4.6.1 (angelic/adversarial relation) | Same mechanism, needs the angelic/adversarial-name lexicon (design doc §5.1 — also flagged, not yet built). **Not yet answerable in practice**, same status as the row above. |

**Build implication, stated plainly**: T0.1.1/T4.1.1/T4.2.1/T0.1.2's raw-fact half are answerable
the moment the divine-name lexicon (already verified) is wired into `party_kind` at build time.
T4.3.1/T4.4.1/T4.6.1 need two more lexicons built first — **this is now a concrete pre-build task,
not an open question**, since A5 rules out deferring it.

## 4. Answered by a rollup across a term's full occurrence set (needs the corpus-wide view, not one verse)

These need Stage 1 to have run across every verse containing the relevant Strong's code(s) —
answerable once that's true, with no Stage 2 dependency; the rollup itself is a plain query over
already-stored per-occurrence fields, not a new capture requirement.

| Question | Field(s) rolled up | Rollup, stated exactly |
|---|---|---|
| T7.1.2 — grammatical range of the primary term | `verse_lexical.morph_code` | `SELECT DISTINCT` the part-of-speech prefix across every row with this `strong` code. |
| T7.1.8 — OT/NT vocabulary relationship | `verse_lexical.testament` | `GROUP BY testament` across every row sharing the term's root/family (via `strong_related`), counted per side. |
| T7.1.9 — newly-coined-in-NT term | `verse_lexical.testament` | Same rollup as T7.1.8 — a term with zero `testament='OT'` rows anywhere in its `strong_related` family. |
| T7.1.1 / T1.1.2 — what the primary terms show at the definitional level | `verse_lexical.resolved_sense`, every occurrence | Rolled-up list of every distinct resolved sense the term carries across its full occurrence set — confirmed live this session that `resolved_sense` genuinely narrows per-stem (§A6 correction), so this rollup reflects real variation, not a repeated flat gloss. |
| T7.1.10 — full vocabulary arc | All of the above, combined | Not a separate derivation — the union of T7.1.1/T7.1.2/T7.1.8/T7.1.9's own rollups. |
| T6.4.1 / T6.1.1 — vocabulary/characteristic co-occurrence | `strong_related` (raw pull, §2 above) + the term→characteristic-candidate linkage (Stage 2's own input-assembly mechanism, not a Stage 1 field) | The related-words pull is Stage 1's own mechanical output; **cross-referencing which *characteristic* each related code belongs to needs Stage 2's segmentation linkage** — flagged as a genuine two-stage dependency, not purely Stage 1, unlike the rows above it. |
| T6.4.2 — root-level architecture sharing | Same as T6.4.1, plus a lemma/root match across the pulled `strong_related` sets of two different characteristic-candidates' term families | Same two-stage dependency as T6.4.1. |

## 5. Explicitly NOT answered by Stage 1 — named here so the boundary is exact, not implied

| Question | Why not, precisely |
|---|---|
| T7.2.1 (argument half), T7.2.3 — logical structure, premises/conclusions | The connective/chain notes give local clause-linkage edges; nothing assembles them into an actual premise→conclusion argument map. Real gap, named in the coverage document §2, unchanged by this pass. |
| T7.1.3 — semantic range | Not a Stage-1 rollup at all — a property of `strong_meaning_tree`/`strong_meaning_parsed` directly, independent of any specific verse's occurrence. Stage 1 correctly *draws on* this resource (confirmed working, §A6) rather than re-deriving it. |
| T7.1.4 / T7.1.5 / T7.1.6 / T7.1.7 (the non-lexicon-dependent halves) | Term-family semantic classification (disposition-vs-act, structural opposites, person-type/supplication forms) — needs judgement on top of the T7.1.2-style rollup, not a field Stage 1 stores directly. Real gap, unchanged from the coverage document. |
| Every T0.2.1-class question (§7 of the coverage document, ~85 questions) | By definition — behaviour-synthesis over a whole characteristic's evidence base, Stage 2 Pass 2b's job, never Stage 1's. |

---

## 6. What this means for "finalising the proposal"

- **3 mechanical lexicons need building as part of this same increment**, not designed-but-deferred:
  the connective-type lexicon (causal/coordinating/purpose — already prototyped), the divine-name
  lexicon (already verified), and the human-name / angelic-name lexicons (designed, not yet built —
  named explicitly in §3 above as the reason T4.3.1/T4.4.1/T4.6.1 aren't answerable yet).
- **`party_kind` is now part of the schema** (design doc §5.1) specifically because §3 of this
  document showed it's the derivation four separate catalogue questions actually depend on — not
  added speculatively.
- **The T6.4.x/T6.1.1 two-stage dependency (§4) is the one place this mapping found where "Stage 1
  answers it" was too strong a claim** — Stage 1 supplies the raw pull, but the characteristic
  cross-reference needs Stage 2's own input-assembly linkage to complete the answer. Named exactly,
  not glossed over.
- **§5's list is the honest boundary** — these do not become build items for this increment; they
  stay named gaps with no owner yet, exactly as the coverage document already recorded them.
