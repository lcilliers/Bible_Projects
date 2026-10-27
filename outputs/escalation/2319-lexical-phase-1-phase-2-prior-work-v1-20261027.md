# What the earlier lexical work says about verse reading and characteristic assessment (v1, 2026-10-27)

Escalation #2319 (what the observations of Analysis_phase_1 must cover, and how a surface is evaluated for relevance to the inner being). This is the earlier work you pointed me to, read for section 4 of `outputs/escalation/2318-analysis-phase-1-specification-v4-20261027.md`. It is a digest with sources, not a proposal for section 4. Your quotations are verbatim from the files.

**What I read, and what I did not.**
- `Workflow/Catalogue/1378-lexical-to-finding-worked-example-v1-20260901.md` (escalation #1378): read to line 830 of 935. I did not read the last part, which includes the raw data dump.
- `Workflow/Catalogue/1379-lexical-inner-being-checklist-v1-20260901.md` (#1379): read whole.
- `iba/docs/1383-verse-lexical-window1-full-build-specification-v1-20260904.md` (#1383): read the correction at the top, the logic of the two steps (section C) and the Phase 2 extract (G.2). I did not read the governance and config tables (A, B), validation (D), error handling (E), PS variants (F) or the open-items list (I).
- All three are from 1 to 4 September 2026. I have not checked whether what #1383 proposed was built.

## 1. The discipline: every surface is evaluated

Your correction in #1378, verbatim: *"it is almost as if the discipline is read every lexical term in the verse, and ask what does it do vir[à-vis] understanding the inner being."*

- The first pass cherry-picked the terms that already looked inner-being and treated the rest as settled. That caused the misses: `asked` (H1245), `not` (H3808), and `king`, `chief`, `eunuchs` (Dan 1:8). (#1378, "The discipline, applied properly")
- The checklist therefore starts: **enumerate every live row, with no pre-filtering by role or gloss before the tests run.** (#1379, test 1)
- A row that contributes nothing is **recorded as checked and empty**, not silently skipped, so the mechanism does not manufacture content out of function words. (#1379, "inert check"; #1378)

## 2. How relevance is evaluated: by tests, not by vocabulary

The earlier test was whether the word's own gloss looks psychological. It missed everything that carries inner-being content by what it does, not by what it names. The twelve tests of #1379, in plain words:

| Test | What it catches |
|---|---|
| every live row enumerated | cherry-picking |
| genre or mode of the verse, recorded per verse | which of the other tests apply |
| language and testament, recorded per row | which version of the sequence test applies |
| declared vocabulary: does the gloss carry inner-being vocabulary | the obvious cases (heart) |
| idiom or combined span: does the surface gloss diverge from a code-by-code reading | inner-being content with no English word (heart hidden in "resolved") |
| outward enactment: a volitional or appetitive sense behind a plain action verb | asked |
| relational: does the row name or imply another party, tested against "relates" in the five-part definition (thinks, feels, chooses, relates, orients toward meaning, others and God) | king, chief, eunuchs |
| polarity: a negation or modifier on an operation | not (vocabulary-blind) |
| sequence or chain: a narrative-sequencing mark linking operations | the chain from resolve to ask |
| related terms: each related code sorted into same concept, genuine relative, or coincidence | bulk import of related words |
| primary operation or theme: the operation with nothing upstream | the verse's entry point |
| inert: confirmed to contribute nothing beyond grammar | invented content |

Two governing rules (#1379): every row's result is a **structured field**, never prose only and never ranked by assumed importance; and there are **two flag types kept separate**, data-quality flags and discovery flags.

## 3. The roles a surface can play

From #1378 (the taxonomy that came out of applying the discipline to all 25 rows of Dan 1:8): core inner-being vocabulary (heart); outward-enactment verb (asked); object or content of the act (defile, food, wine); polarity or modifier (not); relational target (king, chief of the eunuchs); severity or stakes (choice, feast); entity-linking (his, Daniel); pure grammar (articles, conjunctions, prepositions), which earns no role.

Your third correction decided how these are kept. Verbatim: *"the phase 2 work would never have picked it up if the phase 1 work demote or hide it."* And: *"the inner being operations described in the bible is not declarative, it is discoverable — it is there, it should be there, it is not named but it is expected."* So:
- **Declared roles:** the sense can be named on lexical evidence.
- **Structural roles:** the sense or motive cannot be asserted, but the structural fact must be preserved with full fidelity (a relational transaction occurred, with whom, in what sequence, under what polarity).
- Both are first-class, persisted fields, not a main finding with lesser notes behind it.

## 4. The shape of the finding

#1378 concludes that positions 1 to 4 of Dan 1:8 are **one finding with several required parts**, not five findings: subject, faculty and sense, polarity, content, enactment, context, evidence. It is a structured record, not one sentence per span. (Flagged there as a design implication, not decided.)

Also in the files:
- A **primary operation or theme** field, taken from the chain, because a process studying "ask" or "defile" would find the verse and wrongly record it as an "ask" or "defile" verse. There can be more than one. (#1378, #1379 test 11)
- **Genre per verse and language and testament per row, recorded explicitly**, because *"implicit does not trigger the mind."* The sequence test is Hebrew-specific (the waw-consecutive mark); Greek needs its own version, not built. (#1378)
- The test that sorted related words by `lemma_key` was **retracted** in #1378: it failed its own control case, and there is no reliable database-native test that overrides the curators' link. Related words are sorted one by one, never imported in bulk.

## 5. The line between verse reading and characteristic assessment

Two statements, written two days apart:

1. **#1378 (1 September):** Phase 1 asserts the declared roles and preserves the structural facts. The motive (for example that Daniel saw refusal as dishonourable to the king) is *"Phase 2: it uses this Phase 1 structure as its evidence rather than being identical to it."* Phase 2 was left undecided, with three options: (A) the same discipline at wider aperture; (B) resolving each discovery flag against specific evidence; (C) a characteristic-level rollup across verses.
2. **#1383 (4 September), your correction:** the boundary is **definitional, not mechanical**. `verse_lexical` and `verse_lexical_note` can **never** carry an inner-being concept, by definition, and nothing in Window 1 determines whether something is a phenomenon. The mechanical and judgement layers are both Window 1. The rollup across verses is Window 2.

These two are not obviously the same. #1378's Phase 1 assigns each surface a role relative to the inner-being act. #1383 says the lexical tables never carry an inner-being concept. Analysis_phase_1 writes to `ib_observation` and `ib_node`, whose finding kinds (face, party, statement, link and the others) are inner-being kinds. So it is neither Window 1 as #1383 defines it, nor the claims work. It sits between them: the verse reading that comes before the claims, which is the difference you named today.

## 6. What this gives section 4

For the first job of #2319, **relevance of a surface to the inner being**:
- Every surface of the verse is enumerated. Today the code skips function-word rows by their morph and records nothing for them; the earlier work requires an inert surface to be recorded as checked and empty. (Code fact: `surfaces_state`, element B04 of `outputs/escalation/2318-analysis-phase-1-description-v1-20261027.md`.)
- Relevance is judged by the tests in section 2, not by the gloss or cluster tag. In the code a surface is in focus because it is not a function word, and nothing evaluates it further.
- The result is a structured, queryable record for every surface, with its role from section 3, including the structural roles.

For the second job, **what the observations must cover**: the earlier work asks for more than role, face and term:
- polarity, content or object, enactment and chain, the relational target, the primary operation or theme, genre, language and testament;
- typed flags.
The current kinds and node fields (face, qualification, party, statement, link, use, term, silence; role, subgroup, and so on) have no home for polarity as a field, for the primary operation or theme, or for the chain as a field. (Code fact: element G13 and the node columns in G17 of the description file; I have not checked how the existing observation rows use the `link` kind for chains.)

## 7. Points for you

These are the points the earlier files leave open, and they bear on how you define the observation after step 3. I make no choice on them.

1. Which governs what Analysis_phase_1 writes: the #1383 boundary (nothing in the lexical layer carries an inner-being concept) or the #1378 taxonomy of roles relative to the inner-being act? My reading is that Analysis_phase_1 follows the #1378 taxonomy, because its kinds are inner-being kinds, and that claims are the later, characteristic-level work.
2. Is an inert surface recorded (checked and empty) in the tables, or only in the JSON?
3. Where do polarity, the primary operation or theme, and the chain live: as kinds of finding, as node fields, or inside the text of a finding?
4. #1378 option C (the characteristic-level rollup) is now what the claims step does. Do options A and B (wider aperture, targeted flag resolution) belong in Analysis_phase_1 or in the claims?
