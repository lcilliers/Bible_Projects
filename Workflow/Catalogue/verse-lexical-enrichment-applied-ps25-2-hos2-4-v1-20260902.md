# Verse-lexical enrichment checklist — applied to Ps 25:2 and Hos 2:4

> Escalation #1379. Test-drive of `iba/docs/verse-lexical-enrichment-checklist-v1-20260902.md`
> against two real verses, per researcher instruction. Both chosen deliberately: different genre
> from Dan 1:8 (narrative) and from each other — Ps 25:2 (poetic/wisdom, prayer address) and
> Hos 2:4 (prophetic, divine oracle) — to stress-test genre-branching and turn up gaps the
> single-verse Dan 1:8 pass couldn't. All data pulled live from `iba.db` (`verse`/`span`/
> `verse_lexical`/`strong_related`), 2026-09-02.

## Ps 25:2

> *O my God, in you I trust; let me not be put to shame; let not my enemies exult over me.*

**Gate — genre/language/testament.** Poetic/wisdom (Psalm, prayer address), Hebrew, OT. This
already changes what fires below, live, not hypothetically.

| pos | surface | strong | morph | role | note |
|---|---|---|---|---|---|
| 0 | God | H0430G | HNcmpc | content | addressee |
| 1 | trust | H0982+H9020+H9003+H9031 | HVqp1cs+HSp1bs+HR+HSp2ms | content+function×3 | "I trust in you" |
| 2 | not | H0408 | HTn | content | polarity |
| 3 | put to shame | H0954 | HVqc1cs | content | governed by pos2 |
| 4 | not | H0408 | HTn | content | polarity |
| 5 | my | H9020 | HSp1bs | function | possessive, standalone particle span |
| 6 | enemies | H0341 | HVqrmpc | content | relational target |
| 7 | exult | H5970 | HVqj3mp | content | governed by pos4 |
| 8 | me | H9005+H9030 | HR+HSp1bs | function | object of pos7 |

**Idiom/combined-span test.** Pos 1 is a compound span (4 codes) but not idiomatic in the Dan 1:8
sense — a literal verb+preposition+object reading ("trust" + "in" + "you") matches the combined
surface directly. No divergent sense selected by the combination. Checked, negative result.

**Purposeful classification.**
- **Pronoun/suffix — who's it pointing to.** `H9031` ("you," 2ms, pos1) → **God**, named pos0,
  same verse, resolved. `H9020` ("my," 1cs, pos1 and pos5) → the speaker (1cs verb subject at
  pos1 confirms), resolved. `H9030` ("me," 1cs, pos8) → the speaker, same, resolved. **All four
  pronoun instances resolve same-verse — no unresolved cases in this verse.**
- **Noun — relational/addressee.** `H0430G` ("God," pos0) is the addressee of "trust" — resolved
  same-verse via the pos1 object suffix. `H0341` ("enemies," pos6) is a relational target — an
  adversarial party, bound to the speaker via "my" (pos5) — resolved same-verse.
- **Verb — triggered by what, impacts what.** `H0982` ("trust") — not chain-triggered (no
  preceding operation; opens the verse); impacts/targets God (its object). `H0954` ("put to
  shame") — triggered by the negation at pos2 (a negated wish/jussive sense, per the gloss's own
  "let not... be put to shame" framing); impacts the speaker (1cs, same subject as "trust").
  `H5970` ("exult") — triggered by the negation at pos4; subject is "enemies" (3mp, matching
  `H0341`'s own plural), impacts the speaker (pos8, "over me").

**Finding connections — chain/sequencing.** **Checked, does not fire.** No span in this verse
carries a wayyiqtol/waw-consecutive morph tag (`HVqp1cs`, `HVqc1cs`, `HVqj3mp` — perfect,
infinitive-construct, jussive; no `HVqw...` anywhere). This is poetic prayer, not narrative
sequence — confirms the gate matters in practice, not just in principle: a chain test built and
proven on Dan 1:8 (narrative) correctly finds nothing to report here, rather than forcing a
reading.

**Finding connections — logical/causal.** None present; the verse's three clauses are juxtaposed
(typical Hebrew poetic parallelism — trust / not-shamed / enemies-not-exulting), not linked by an
explicit connective the way Hos 2:4's `H3588A` links its clauses. Checked, negative result.

**Enhancing meaning — related words.**
- `H0982` ("trust") — 6 related codes, all same root (*bth*): security, trust (×2), confidence.
  Clean same-concept cluster, no surprises, no genuine-relative or coincidental cases to sort.
- `H0954` ("be ashamed") — 4 related codes: three straightforward "shame" variants, plus `H4016`
  *mavosh*, glossed "genitalia" — same root, a real but sharply divergent specific application
  (almost certainly a euphemistic use of the shame-root). Flagged, not asserted as relevant to
  this verse — recorded per the checklist's own rule (record the link, don't auto-decide its
  weight).

**Polarity.** Two negation instances, both `H0408` (pos2, pos4) — same code both times. `H0408`
and `H3808` (the code seen in Hos 2:4 below) are themselves cross-listed in `strong_related` as
mutually related ("not"/"not") — worth having on record that this verse's negator and Hos 2:4's are
the *same functional family*, not two unconnected particles, should a later cross-verse comparison
need it.

**Entity-linking.** Every operative verb in this verse shares one grammatical subject (1cs — the
speaker) except `H5970` ("exult," 3mp — the enemies). That's itself a clean, mechanically-visible
structural fact: two subjects across three verbs, both correctly identifiable from morph alone
(1cs vs. 3mp), no interpretation required.

**Data-quality check — same code, different gloss.** `H0408` occurs at pos2 and pos4, identical
code, identical gloss both times. **Checked — no collision** (contrast with Dan 1:8's `H0834A`).
Recording the negative result explicitly, per the checklist's own inert-confirmation discipline.

**Inert/pure-grammar.** `H9003` (pos1, "in," prefix beth), `H9005` (pos8, "to/for," prefix lamed)
— function-role prepositional prefixes, contribute nothing beyond binding their host word
grammatically. Checked, confirmed empty.

## Hos 2:4

> *Upon her children also I will have no mercy, because they are children of whoredom.*

**Gate — genre/language/testament.** Prophetic (divine oracle/judgment speech), Hebrew, OT.

| pos | surface | strong | morph | role | note |
|---|---|---|---|---|---|
| 0 | children | H1121A+H0853+H9002 | HNcmpc+HTo+HC | content+**content**+function | see role note below |
| 1 | no | H3808 | HTn | content | polarity |
| 2 | mercy | H7355+H9024 | HVpi1cs+HSp3fs | content+function | "I will have no mercy on her" |
| 3 | because | H3588A | HTc | content | causal connective |
| 4 | they | H1992 | HPp3mp | content | pronoun |
| 5 | children | H1121A | HNcmpc | content | recurrence of pos0's code |
| 6 | whoredom | H2183 | HNcmpa | content | quality modifier |

**Idiom/combined-span test.** Pos0 and pos2 are compound spans; neither shows a literal-vs-
combined divergence the way Dan 1:8's "resolved" did. Checked, negative result on idiom, but see
the role-classification note below — a real observation, just not an idiom one.

**Role-classification observation (data-quality-adjacent, not in the original checklist draft).**
`H0853` (pos0, ordinal 1) is the **definite direct-object marker** — per its own gloss, "sign of
the definite direct object, not translated in English." This is pure grammatical marking, no
lexical content of its own, the same category as an H9xxx formative — but it is classified
`role=content` by the live `classify_role()` heuristic, because that heuristic's Hebrew rule only
tests the H9000-H9999 range and `H0853` falls outside it. **This looks like a genuine gap in the
existing T1-T3 role classifier**, not a new Window-1 field — flagged here because this checklist's
own data-quality-check item is exactly where it surfaced, but it's a correction to *existing*,
already-live logic (`lib/lexical.py:classify_role`), not a new enrichment field. Distinct from the
same-code/different-gloss check below; noted separately so it doesn't get lost inside either.

**Purposeful classification.**
- **Pronoun — who's it pointing to.**
  - `H9024` ("her," 3fs, pos2) — checked against every other span in this verse for a 3fs
    antecedent: `H1121A` ("children," pos0/pos5) is masculine plural (`Ncmpc`), not feminine;
    nothing else in the verse is 3fs. **No antecedent resolvable from this verse's own data.**
    Recorded **unresolved** — not guessed, per the checklist's own rule — even though a human
    reader familiar with Hosea 1-2 would supply "the mother" (the unfaithful wife/Israel figure
    named in the surrounding passage, not this verse). That's exactly the case this rule exists
    for: a genuine cross-verse crux, correctly refused rather than silently resolved from outside
    data, and hard-flagged for Window 2 (`hib.set`) to pick up with proper passage access.
  - `H1992` ("they," 3mp, pos4) — checked against this verse: `H1121A` (pos0/pos5, masculine
    plural) agrees in person/number/gender. **Resolved same-verse** — "they" = "children."
- **Noun.**
  - `H1121A` (pos0, pos5) — recurrence, identical code both occurrences (same discipline as Dan
    1:8's `H1351` repetition test) — no drift between the two occurrences.
  - `H2183` ("whoredom," pos6) — quality/severity modifier, characterizing what kind of
    "children" these are (construct-bound to `H1121A` at pos5), not a relational target — no
    other party is named or implied by this word itself.
- **Verb.** `H7355` ("have mercy," pos2) — subject 1cs (the speaking voice — God, per the oracle
  genre); triggered by nothing preceding in this verse (opens the clause); impacts `H9024` ("her,"
  the withheld-mercy's target) — which is itself the unresolved pronoun above. The verb's own
  reading is only half-complete without that pronoun's resolution, and this checklist is honest
  about that rather than papering over it.

**Finding connections — chain/sequencing.** Checked — `HVpi1cs` (Piel imperfect, pos2) carries no
wayyiqtol marker. Does not fire, same negative result as Ps 25:2 — **neither test verse is
narrative prose, so this item remains untested against a real positive Hebrew case beyond Dan 1:8
in this round.** Worth naming as a residual gap for the next prototype batch, not fixed here.

**Finding connections — logical/causal (new item, confirmed needed).** `H3588A` ("because," pos3,
`HTc`) explicitly links the "no mercy" clause (pos0-2) to the "children of whoredom" clause
(pos4-6) by **reason**, not narrated sequence. This is the concrete case that justifies adding
this as its own permanent checklist item, distinct from the narrative-chain test — Dan 1:8 had
nothing like it (its "resolve→ask" link was sequential, not causal), and without a dedicated test
this connective would have fallen through the cracks (it isn't a pronoun, isn't a noun in the
relational/modifier sense, isn't polarity — it doesn't fit any other slot).

**Enhancing meaning — related words.**
- `H7355` ("have mercy/compassion," *racham*) — a large related-code set. Sorted: several are
  coincidental (proper names sharing consonants — Jeroham, Jerahmeel, Rehum, ×several variants
  each). But a genuine, textually loaded cluster survives the sort: `H7349`/`H7362`
  ("compassionate"), `H7356B` ("compassion") — same-concept family, **and `H7356A`/`H7358`
  ("womb")** — the same Hebrew root covers both "compassion" and "womb," a real and well-attested
  semantic connection (compassion imaged as a mother's/womb's tenderness). Given this verse is
  specifically about a mother's compassion being withheld from *her children*, this related-word
  family is not incidental — it's a genuine enhancement the raw `resolved_sense` field alone
  doesn't carry, surfaced exactly the way the checklist's related-words step is meant to.
- `H3808` ("no," pos1) — related codes include `H0408`/`H3809` (same-concept "not" variants, as
  in Ps 25:2 above) **and `H3819`, glossed "No Mercy."** `H3819` is *Lo-Ruhamah* — the name given
  to a child earlier in Hosea (1:6), built from the same two roots this verse's own words
  represent: *lo* (`H3808`, "not") + *racham* (`H7355`'s own root, "mercy/compassion"). Hos 2:4's
  "I will have no mercy" is, lexically, a direct echo of that child's own name, and the
  related-word pull surfaces this mechanically — a genuinely load-bearing connection, not a
  coincidental root-share, found by following the checklist's own procedure rather than by
  reading the English and noticing the theme by eye.

**Polarity.** `H3808` (pos1) — same negator family as Ps 25:2's `H0408` (cross-listed as related
to each other), different specific code. One instance, no collision to check.

**Entity-linking.** The verse's one operative verb (`H7355`) is 1cs — the divine speaking voice
(oracle genre) — distinct from Ps 25:2's human 1cs speaker. Both mechanically visible from morph
alone; the *identity* of "I" (God vs. psalmist) is a genre/context fact this checklist doesn't
itself assert — flagged, not resolved, consistent with the discipline throughout.

**Data-quality check — same code, different gloss.** `H1121A` occurs at pos0 and pos5, identical
code and gloss both times. Checked — no collision.

**Inert/pure-grammar.** `H9002` (pos0, "and," conjunctive vav) — function, contributes nothing
beyond linking. Checked, confirmed empty.

## What this run adds to the checklist

- **Logical/causal connective** — confirmed needed, add permanently (Hos 2:4's `H3588A`).
- **Role-classification gap on `H0853`** — a fix to existing T1-T3 logic, not a new field; flagged
  separately, not folded into this checklist's own item list.
- **Chain/sequencing test** — negative-fired correctly on both non-narrative verses; still needs a
  genuine positive Hebrew narrative case beyond Dan 1:8 to be considered properly exercised.
- **Unresolved-pronoun marker** — worked exactly as specified on a real case (`H9024`, Hos 2:4) —
  no guessing, explicit flag, ready for Window 2.
- **Related-words step** — produced two genuinely load-bearing findings (womb/compassion;
  Lo-Ruhamah echo) from mechanical pulls, not manual insight — a real positive result for
  codifying this as part of what verse_lexical delivers.
