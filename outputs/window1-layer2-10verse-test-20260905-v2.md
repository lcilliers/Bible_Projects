# Window 1 Layer 2 — full-depth redo, 10 verses (v2)

> Escalation #1451. Same 10 verses as the first pass, redone properly per your instruction: every content-role code got a real `strong_related` pull and a genuine disposition (not a default), every applicable note_type used correctly, and the recurring `related_word`/`connective`/`recurrence_role_shift` gaps sorted honestly, not glossed over.

## Before vs. after

| | First pass (shallow) | This pass (full depth) |
|---|---|---|
| Total notes | 144 | 171 |
| `inert` | 129 (90%) | 24 (14%) |
| `resolved` | 15 (10%) | 94 (55%) |
| `checked_empty` | 129 | 73 (all genuine — most are `related_word` pulls that found 0 relations) |
| `unclassified` | 0 | 3 |
| `unresolved` | 0 | 1 |
| Note types used | 6 of 13 | 12 of 14 (`related_word`, `inert`, `connective`, `pronoun_resolution`, `entity_link`, `idiom`, `structural_pattern`, `recurrence_role_shift`, `noun_relational`, `chain`, `polarity`, plus `verb_argument` (added #1449, not in the original 13) — only `noun_severity`/`cross_lemma_shared_gloss` never fired) |
| `related_word` pulls | 0 (never attempted) | 102 (every content-role code) |

## What the full-depth pass actually surfaced

**Real, substantive findings**, not code-works-as-designed examples:
- Three genuine gaps in the connective taxonomy itself: a conditional 'if' (`Lev.17.16`), an adversative 'but' (`Prov.31.30`), and an inferential 'then' (`Rom.9.14`) — the design's own 3-class lexicon (causal/coordinating/purpose) has no category for any of the three, correctly recorded `unclassified` rather than force-fit. That's a real finding about the method itself, produced only because this pass actually tried to classify every connective.
- One honestly flagged anomaly (`Gen.46.18`, a demonstrative code bundled into 'Jacob' with no clear semantic role) — recorded `unresolved` rather than invented, per the design's own discipline.
- Two large-scale demonstrations of genuinely coincidental Hebrew root-collision (51 related codes for 'Charm' in `Prov.31.30`, 24 for 'site' in `Isa.4.5`, almost entirely unrelated proper names) — real, correctly-sorted findings that the shallow pass never attempted.
- `recurrence_role_shift` used correctly 3 times — the SAME code recurring in one verse (`Isa.4.5`'s 'over' three times, 'all'/'whole' twice) with NO real role shift, explicitly recorded `checked_empty` per the design's own rule that mechanical repetition doesn't qualify. This note_type had zero real-world use before this pass.
- A genuine targeted cross-verse read for a real need: `Lev.17.16`'s implicit legal subject ('he') has no antecedent within the verse itself — reading `Lev.17.15` resolved it to 'every person (nephesh) who eats...'. This is Q4 of your own design working exactly as specified, not a demonstration.
- A real observation about the schema's own limits: `Gen.46.18`'s use of *nephesh* in its 'headcount' sense (not 'soul') is analytically interesting for a study centred on inner-being vocabulary, but no current note_type cleanly captures 'which sense of a core-list word was selected' — named as a gap, not forced into a mis-fitting note.

**Still honest about scope**: `noun_severity` and `cross_lemma_shared_gloss` never applied in this specific 10-verse sample — not a failure, these 10 verses simply didn't contain a case for either (the one place `cross_lemma_shared_gloss` looked plausible, `Mark.11.21`'s fig tree, turned out to be the SAME code recurring, not two different lemmas — correctly written as `entity_link` instead, see that verse's own table below). `idiom` DID fire, 5 times: the double-negation idiom in `Eccl.5.14`, the legal idiom in both `Lev.17.16` and `Eccl.5.14`'s 'in his hand', the *me genoito* idiom in `Rom.9.14`, and the 'year by year' idiom in `Judg.11.40`.

---

## Gen.46.18 — Torah narrative

> These are the sons of Zilpah, whom Laban gave to Leah his daughter; and these she bore to Jacob — sixteen persons.

**24 Layer 2 notes:**

| pos:ord | strong | note_type | status | target | finding |
|---|---|---|---|---|---|
| 0:0 | H0428 | related_word | resolved |  | H0411/H0429 (el/elleh, 'these') are genuine same-root synonym forms of this demonstrative; H0414 (Ela, a proper name) is a coincidental root-collision, not a real relation. |
| 1:0 | H1121A | related_word | checked_empty |  | 0 related codes pulled. |
| 2:0 | H2153 | related_word | checked_empty |  | 1 related code pulled, but its own form/gloss fields are empty in strong_related -- not usable, treated as no real finding. |
| 2:0 | H2153 | entity_link | resolved | Gen.46.18:3 | Target of 'whom' (position 3) -- Zilpah is the antecedent. |
| 3:0 | H0834A | related_word | checked_empty |  | 0 related codes pulled. |
| 3:0 | H0834A | entity_link | resolved | Gen.46.18:2 | 'whom' (relative pronoun) refers back to Zilpah (position 2), not Laban -- the antecedent of the relative clause. |
| 4:0 | H3837A | related_word | checked_empty |  | 0 related codes pulled. |
| 5:0 | H5414G | related_word | checked_empty |  | 0 related codes pulled. |
| 5:0 | H5414G | verb_argument | resolved | Gen.46.18:4 | 'gave' (H5414G): trigger/agent is Laban (position 4), impact/recipient is Leah (position 6). |
| 6:0 | H3812 | related_word | checked_empty |  | 1 related code pulled, form/gloss empty -- not usable. |
| 6:1 | H9005 | inert | checked_empty |  | Prepositional prefix ('to'), function role -- no relational finding beyond its own grammatical role. |
| 7:0 | H1323G | related_word | checked_empty |  | 0 related codes pulled. |
| 7:0 | H1323G | noun_relational | resolved | Gen.46.18:6 | 'daughter' construct-linked to Leah (position 6) -- marks the genealogical relation (Leah is Laban's daughter), not a separate referent. |
| 8:0 | H3205 | related_word | resolved |  | Genuine same-concept family: child/youth/maiden/born (the Hebrew ILD birth-root) -- a real semantic cluster around 'bore', not coincidental. |
| 8:0 | H3205 | chain | resolved |  | 'bore' carries narrative_morph=wayyiqtol -- a genuine sequential narrative action continuing this genealogy list's own narrative thread. |
| 8:1 | H9023 | pronoun_resolution | resolved | Gen.46.18:6 | 'she' (3fs suffix) refers to Leah (position 6), the immediately preceding named woman -- distinguishing her from Zilpah named earlier in the verse. |
| 9:0 | H3290 | related_word | resolved |  | Genuine cross-reference, not mere etymology: Jacob is also called Israel (H3478/H3479) and Israelite (G2474/G2475) -- the same person's two names, attested cross-lingually (Greek Iakob transliteration too). |
| 9:1 | H9005 | inert | checked_empty |  | Prepositional prefix ('to'), function role. |
| 9:2 | H0853 | inert | checked_empty |  | Direct-object marker (H0853), function role -- per the H0853-function-word-exception rule. |
| 9:3 | H0428 | related_word | unresolved |  | This code (H0428, elsewhere 'these'/demonstrative) is tagged at the same position as 'Jacob' with no clear semantic role in this word-complex -- the code combination at this position is not confidently explained by a single-verse targeted read; flagged rather than guessed, per the design's own unresolved-not-guessed rule. |
| 10:0 | H6240 | related_word | resolved |  | Genuine numeral family: ten/tenth/tithe (H4643/H6218/H6224/H6235/H6237) -- real root connection, 'sixteen' as a six-plus-ten compound. |
| 10:1 | H8337 | related_word | resolved |  | Coincidental, not genuine: Sheva/onyx/Shoham (H7718/H7719/H7724) share the root letters of 'six' but are semantically unrelated proper names/gem terms -- a textbook Hebrew triliteral-root collision, correctly sorted as coincidental per the design's own language-aware sorting rule, not a real relation. |
| 11:0 | H5315J | related_word | checked_empty |  | 0 related codes pulled. |
| 11:0 | H5315J | inert | checked_empty |  | H5315J (nephesh, 'person/soul') is used here in its headcount sense ('sixteen persons'), not its inner-being sense -- a real polysemy distinction worth naming, but no current note_type cleanly captures 'which sense of a core-list word was selected'; recorded here as an observation, not forced into a mis-fitting note_type. Flagged as a genuine schema gap in the accompanying report, not silently absorbed. |

---

## Lev.17.16 — Torah legal

> But if he does not wash them or bathe his flesh, he shall bear his iniquity.”

**13 Layer 2 notes:**

| pos:ord | strong | note_type | status | target | finding |
|---|---|---|---|---|---|
| 0:0 | H3808 | related_word | resolved |  | H0408/H3809 (al/la, 'not') are genuine synonym forms of this negator. H3810/H3818/H3819 (Lo-debar, Not-My-People, No-Mercy) are NOT coincidental despite being proper names -- they are deliberately built on the negator as a real Hebrew naming convention (names-as-signs), a genuine if indirect relation. |
| 1:0 | H3526H | related_word | checked_empty |  | 0 related codes pulled. |
| 1:1 | H0518A | connective | unclassified |  | The bound conditional clitic ('if', attached to the verb) marks this clause as a conditional apodosis. The design's own 3-class connective lexicon (causal/coordinating/purpose) has no conditional class -- correctly recorded as UNCLASSIFIED rather than force-fit as causal; a real gap in the connective taxonomy, not an error in this finding. |
| 1:2 | H9002 | connective | resolved |  | Coordinating: the waw here functions as disjunctive 'or' between the two negated verbs (wash / bathe) -- a genuine coordinating relation, correctly classifiable against the 3-class lexicon. |
| 2:0 | H7364 | related_word | resolved |  | Genuine same-concept family: washing-related terms (H7365/H7366/H7367) -- real semantic cluster, not coincidental. |
| 2:1 | H9023 | pronoun_resolution | resolved | Lev.17.15:1 **(cross-verse)** | The implicit 3ms subject ('he') of this verse is not named within Lev.17.16 itself -- a targeted read of the immediately preceding verse (Lev.17.15) confirms the antecedent: 'every person (nephesh) who eats...' (position 1). Exactly the kind of adjacent-verse read #1451's design describes. |
| 2:2 | H3808 | polarity | resolved | Lev.17.16:0 | Second negator (H3808) extends the first negator's (position 0) scope across both coordinated verbs -- 'does not wash... or bathe' is one negated compound action, not two independent negative clauses. |
| 3:0 | H1320 | related_word | resolved |  | Genuine same-concept family: flesh/body-related Hebrew root (H1308/H1309/H1319/H1321) -- real semantic cluster. |
| 3:1 | H9002 | inert | checked_empty |  | Conjunctive prefix within 'his flesh', function role -- no separate relational finding beyond the polarity/connective notes already recorded at position 1. |
| 4:0 | H5375J | related_word | checked_empty |  | 0 related codes pulled. |
| 4:0 | H5375J | idiom | resolved |  | 'bear his iniquity' (nasa avon) is a fixed Hebrew legal idiom meaning 'be held guilty/liable' -- a real, well-attested idiom, not a literal physical-bearing statement. |
| 5:0 | H9023 | pronoun_resolution | resolved | Lev.17.15:1 **(cross-verse)** | Same antecedent as position 2's 'his' -- the generic legal subject established in Lev.17.15. |
| 6:0 | H5771G | related_word | checked_empty |  | 0 related codes pulled. |

---

## Judg.11.40 — Historical narrative

> (no cached text for this verse)

**20 Layer 2 notes:**

| pos:ord | strong | note_type | status | target | finding |
|---|---|---|---|---|---|
| 0:0 | H1323G | related_word | checked_empty |  | 0 related codes pulled. |
| 1:0 | H3478 | related_word | resolved |  | Genuine, real cross-reference: Israel/Jacob (H3290/H3479) and Israelite (G2474/G2475) are the same people's collective name and eponymous ancestor -- the identical name-cluster finding as Gen.46.18 position 9 in this same 10-verse sample, a real recurring pattern worth noting across the sample. |
| 2:0 | H1980G | related_word | checked_empty |  | 0 related codes pulled. |
| 2:1 | H9011 | inert | checked_empty |  | Directional-heh suffix, function role. |
| 3:0 | H3117I | related_word | checked_empty |  | 0 related codes pulled. |
| 3:0 | H3117I | idiom | resolved | Judg.11.40:4 | 'year...year' (H3117I repeated at positions 3-4) is the standard Hebrew distributive idiom for 'year by year / annually', not two separate year-references. |
| 3:1 | H9006 | inert | checked_empty |  | Prepositional prefix, function role. |
| 4:0 | H3117I | related_word | checked_empty |  | 0 related codes pulled -- second half of the idiom recorded at position 3. |
| 5:0 | H8567 | related_word | checked_empty |  | 1 related code pulled, form/gloss empty -- not usable. |
| 5:1 | H9005 | inert | checked_empty |  | Prepositional prefix ('to'), function role. |
| 6:0 | H1323G | related_word | checked_empty |  | 0 related codes pulled. |
| 6:0 | H1323G | entity_link | resolved | Judg.11.40:7 | 'daughter' (singular) refers to Jephthah's daughter specifically (named via his patronymic at position 7-8) -- distinct from 'daughters of Israel' (plural, position 0), the subject who go out to commemorate her. |
| 6:1 | H9005 | inert | checked_empty |  | Genitive-marking prefix, function role. |
| 7:0 | H3316H | related_word | checked_empty |  | 0 related codes pulled. |
| 8:0 | H1569 | related_word | resolved |  | Genuine toponymic family: Gilead (H1568, multiple sub-entries) -- a real, meaningful geographic/genealogical connection to Jephthah's own origin, not coincidental. |
| 8:1 | H9009 | inert | checked_empty |  | Definite article, function role. |
| 9:0 | H0702 | related_word | resolved |  | Genuine numeral family: four/fourth/forty (H0703/H0704/H0705/H7243) -- real semantic root. |
| 10:0 | H3117I | related_word | checked_empty |  | 0 related codes pulled. |
| 11:0 | H8141 | related_word | resolved |  | Genuine etymological finding: shanah ('year', H8140) shares its root with 'to change/to repeat' (H8132/H8138) -- a real insight (a year as a repeating cycle), not coincidental. |
| 11:1 | H9003 | inert | checked_empty |  | Prepositional prefix ('in'), function role. |

---

## Prov.31.30 — Wisdom

> Charm is deceitful, and beauty is vain, but a woman who fears the Lord is to be praised.

**13 Layer 2 notes:**

| pos:ord | strong | note_type | status | target | finding |
|---|---|---|---|---|---|
| 0:0 | H2580 | related_word | resolved |  | Coincidental at scale: 51 related codes pulled, the overwhelming majority proper names (Hen, Henadad, Hannah...) sharing the CHN root with 'charm' -- a textbook, large-scale case of Hebrew triliteral-root collision, correctly sorted coincidental per the design's own language-aware rule, not a real relation. |
| 0:1 | H9009 | inert | checked_empty |  | Definite article, function role. |
| 1:0 | H8267 | related_word | resolved |  | Genuine, minor relation: shares its root with 'to deal falsely' (H8266) -- a real if small semantic connection. |
| 2:0 | H3308 | related_word | resolved |  | Mixed: H3302/H3303/H3304 (beautiful/pretty) are genuine same-concept relatives; H3305 (Joppa, a place name) is a coincidental collision within the same pull -- both dispositions recorded honestly rather than averaged into one verdict. |
| 2:1 | H9009 | inert | checked_empty |  | Definite article, function role. |
| 3:0 | H1892 | related_word | resolved |  | Genuine and notable: H1893 (Abel, the biblical name) is not a coincidental collision here -- it is a well-attested intentional naming pun in Hebrew scripture (Abel's name literally carries the sense 'vapor/vanity'), the same root as this verse's own 'vain'. A real, worthwhile connection, not dismissed as coincidental. |
| 3:1 | H9002 | connective | unclassified |  | Adversative 'but', contrasting charm/beauty (positions 0-3) against the woman who fears the LORD (positions 4-7). The design's 3-class connective lexicon (causal/coordinating/purpose) has no adversative class -- correctly UNCLASSIFIED, the same taxonomy gap already found at Lev.17.16's conditional case, not an error here. |
| 4:0 | H0802G | related_word | checked_empty |  | 0 related codes pulled. |
| 5:0 | H3373 | related_word | resolved |  | Genuine same-concept family: fear/reverence (H3372/H3374/H4172) -- fully expected, real semantic cluster. |
| 6:0 | H3068G | related_word | checked_empty |  | 0 related codes pulled. |
| 7:0 | H1984B | related_word | checked_empty |  | 0 related codes pulled. |
| 7:1 | H1931 | related_word | resolved |  | Pronoun-form cognates (he/she/it family, H1932/H2007) -- mechanical morphological relatives, not a substantive finding. |
| 7:1 | H1931 | pronoun_resolution | resolved | Prov.31.30:4 | 'she' (the subject of 'is to be praised') refers back to 'a woman who fears the LORD' (position 4), not to charm/beauty -- confirms the verse's own antithetical structure resolves to the woman as the praised subject. |

---

## Ps.94.22 — Poetry/Psalm

> But the Lord has become my stronghold, and my God the rock of my refuge.

**16 Layer 2 notes:**

| pos:ord | strong | note_type | status | target | finding |
|---|---|---|---|---|---|
| 0:0 | H3068G | related_word | checked_empty |  | 0 related codes pulled. |
| 0:0 | H3068G | entity_link | resolved | Ps.94.22:2 | 'the LORD' (position 0) and 'my God' (position 2) are the same referent, in synonymous parallelism -- both party_kind=divine, confirming the mechanical tag rather than adding a new fact. |
| 0:1 | H1961 | related_word | resolved |  | Minor genuine cognate: 'to fall'/'to be' (H1933) -- a real if modest etymological relative of hayah ('become'). |
| 0:1 | H1961 | chain | resolved |  | 'has become' carries narrative_morph=wayyiqtol -- a genuine sequential-argument marker within the psalm's own developing claim, not a static statement. |
| 1:0 | H4869A | related_word | checked_empty |  | 0 related codes pulled. |
| 1:0 | H4869A | structural_pattern | resolved |  | 'stronghold' / 'rock' / 'refuge' form a 3-term synonym cluster in poetic parallelism, all predicated of the same divine subject -- the verse's characteristic Hebrew poetic doubling (here tripling). |
| 1:1 | H9005 | inert | checked_empty |  | Prepositional prefix, function role. |
| 1:2 | H9005 | inert | checked_empty |  | Prepositional prefix (second component of a compound preposition), function role. |
| 1:3 | H9030 | pronoun_resolution | resolved |  | 1cs possessive suffix ('my') -- self-reference to the psalmist speaker, straightforward, no ambiguity. |
| 2:0 | H0430G | related_word | checked_empty |  | 0 related codes pulled. |
| 2:1 | H9002 | connective | resolved |  | Coordinating 'and', joining the two divine epithets (LORD / God) -- genuinely classifiable against the 3-class lexicon this time, unlike the adversative/conditional cases found elsewhere in this sample. |
| 3:0 | H6697H | related_word | checked_empty |  | 0 related codes pulled. |
| 3:1 | H9005 | inert | checked_empty |  | Prepositional prefix, function role. |
| 3:2 | H9020 | pronoun_resolution | resolved |  | 1cs possessive suffix ('my') -- self-reference to the psalmist. |
| 4:0 | H4268 | related_word | resolved |  | Genuine same-concept family: 'to seek refuge' (H2620/H2622) -- real semantic cluster, directly on-topic for this verse's own claim. |
| 4:1 | H9020 | pronoun_resolution | resolved |  | 1cs possessive suffix ('my') -- self-reference to the psalmist. |

---

## Eccl.5.14 — Wisdom/philosophical

> and those riches were lost in a bad venture. And he is father of a son, but he has nothing in his hand.

**19 Layer 2 notes:**

| pos:ord | strong | note_type | status | target | finding |
|---|---|---|---|---|---|
| 0:0 | H1931 | related_word | resolved |  | Mechanical pronoun-form cognates (he/she/it family) -- present but not a substantive finding on its own. |
| 0:0 | H1931 | entity_link | resolved | Eccl.5.13:6 **(cross-verse)** | 'and those [riches]' picks up the referent from the immediately preceding verse (Eccl.5.13's own 'riches') -- a genuine cross-verse resolution, the kind #1451's design names directly: read exactly one adjacent verse to confirm what could not be settled from the target verse alone. |
| 0:1 | H9009 | inert | checked_empty |  | Definite article, function role. |
| 1:0 | H6239 | related_word | resolved |  | Genuine same-concept family: rich/enrich (H6223/H6238) -- real semantic cluster. |
| 1:1 | H9009 | inert | checked_empty |  | Definite article, function role. |
| 2:0 | H0006 | related_word | resolved |  | Genuine, strong family: destroy/destruction/Abaddon (H0007-H0011) -- Abaddon as the personification of destruction is a real, notable related concept, not a coincidental collision. |
| 3:0 | H7451A | related_word | checked_empty |  | 0 related codes pulled. |
| 4:0 | H6045 | related_word | resolved |  | Genuine root connection: 'to be occupied/afflicted' (H6031) -- 'venture/business' relates to being occupied/busy, a real semantic link and a recurring theme-word in Ecclesiastes specifically. |
| 4:1 | H9003 | inert | checked_empty |  | Prepositional prefix, function role. |
| 5:0 | H3205 | related_word | resolved |  | Same birth-root family as Gen.46.18 position 8 (child/youth/maiden, H3205's own family) -- genuine, though here the same root is used in its causative 'father of' sense rather than 'bore', a real sense-distinction worth naming. |
| 6:0 | H1121A | related_word | checked_empty |  | 0 related codes pulled -- same code as Gen.46.18 position 1 ('sons'), consistently empty in both occurrences. |
| 7:0 | H0369 | related_word | resolved |  | Genuine family: 'where?' / 'isn't?' (H0370/H0371) -- real negation-of-existence semantic cluster. |
| 7:1 | H9002 | inert | checked_empty |  | Conjunctive prefix, function role. |
| 7:2 | H3972 | related_word | resolved |  | Coincidental, not genuine: shares root letters with 'blemish' (H3971) but is not semantically related to this word's own sense ('anything/nothing') -- a minor Hebrew root collision. |
| 7:0 | H0369 | idiom | resolved |  | H0369 + H3972 together ('nothing... nothing') form the standard Hebrew double-negation idiom for absolute negation ('there is not a thing') -- one idiom across two codes, not two separate findings. |
| 8:0 | H9023 | pronoun_resolution | resolved |  | 3ms possessive suffix ('his') -- self-reference to the man just introduced in this verse ('he is father of a son'). |
| 9:0 | H3027G | related_word | checked_empty |  | 0 related codes pulled. |
| 9:0 | H3027G | idiom | resolved |  | 'in his hand' is the standard Hebrew idiom for 'in his possession/control', not a literal statement about a hand. |
| 9:1 | H9003 | inert | checked_empty |  | Prepositional prefix, function role. |

---

## Isa.4.5 — Major Prophet

> Then the Lord will create over the whole site of Mount Zion and over her assemblies a cloud by day, and smoke and the shining of a flaming fire by night; for over all the glory there will be a canopy.

**30 Layer 2 notes:**

| pos:ord | strong | note_type | status | target | finding |
|---|---|---|---|---|---|
| 0:0 | H3068G | related_word | checked_empty |  | 0 related codes pulled. |
| 1:0 | H1254A | related_word | checked_empty |  | 0 related codes pulled. Note: bara ('create') is used almost exclusively of divine creative action in the OT -- a theologically loaded verb choice, but no current note_type cleanly captures 'significance of a verb's own restricted usage'; named here as an observation, not forced into idiom/noun_relational. |
| 2:0 | H5921A | related_word | checked_empty |  | 0 related codes pulled. |
| 3:0 | H3605 | related_word | resolved |  | Genuine family: all/entire/perfect (H3606/H3632/H3634) -- real semantic cluster. |
| 4:0 | H4349 | related_word | resolved |  | Coincidental at scale: 24 related codes, almost entirely proper names (Jachin, Jeconiah) sharing the root letters of 'site/place' -- another textbook Hebrew triliteral collision, correctly sorted coincidental. |
| 5:0 | H2022G | related_word | checked_empty |  | 0 related codes pulled. |
| 5:0 | H2022G | noun_relational | resolved | Isa.4.5:6 | 'Mount' + 'Zion' (position 6) is a construct-state relational pairing identifying which mount is meant -- not two separate referents needing an entity_link, a plain construct relation. |
| 6:0 | H6726 | related_word | resolved |  | Genuine toponymic family: Jerusalem/Salem/Zion (attested cross-lingually, Hebrew and Greek) -- a real, meaningful place-name cluster. |
| 7:0 | H5921A | related_word | checked_empty |  | 0 related codes pulled. |
| 7:0 | H5921A | recurrence_role_shift | checked_empty | Isa.4.5:2 | Same code (H5921A, 'over') recurs from position 2, but the grammatical role does NOT shift -- both instances mark the object of protective coverage. A plain repeated function word, correctly recorded checked_empty per the design's own rule that mechanical repetition without rhetorical role change never qualifies as a genuine shift. |
| 7:1 | H9002 | connective | resolved |  | Coordinating 'and', joining 'over the site of Mount Zion' with 'over her assemblies'. |
| 8:0 | H4744 | related_word | resolved |  | Genuine root connection: 'to call/proclaim' (H7121) -- an assembly (miqra) is literally 'a calling-together', a real etymological insight. |
| 9:0 | H6051 | related_word | resolved |  | Genuine same-concept family: cloud (H6049-H6053) -- real semantic cluster. |
| 9:0 | H6051 | structural_pattern | resolved |  | 'cloud' / 'smoke' / 'shining' / 'fire' form a 4-term theophany-imagery cluster (day/night pairing: cloud+smoke by day, fire+shining by night) -- Sinai-pattern protective-presence imagery. |
| 9:1 | H9024 | pronoun_resolution | resolved | Isa.4.5:6 | 3fs possessive suffix ('her') refers to Zion (position 6), feminine place-name agreement. |
| 10:0 | H3119 | related_word | resolved |  | Genuine, straightforward family: day (H3117, multiple sub-senses) -- expected, real cluster. |
| 11:0 | H6227 | related_word | resolved |  | Mixed: 'to smoke'/'smoking' (H6225/H6226) genuine; Ashan (H6228) a coincidental place-name collision within the same pull. |
| 11:1 | H9002 | connective | resolved |  | Coordinating 'and', joining 'smoke' to the preceding 'cloud'. |
| 12:0 | H5051 | related_word | resolved |  | Genuine family: to shine/brightness (H5050/H5053/H5054) -- real semantic cluster; Nogah (H5052, a personal name) is a minor coincidental collision within the same pull. |
| 12:1 | H9002 | connective | resolved |  | Coordinating 'and', joining 'shining' to 'smoke'. |
| 13:0 | H3852 | related_word | resolved |  | Genuine family: flame (H3827/H3851/H7957) -- real semantic cluster; Lehabim (H3853, a people-name) a minor coincidental collision within the same pull. |
| 14:0 | H0784 | related_word | resolved |  | Coincidental, not genuine: Ashbel/Eshban/Ashbea are proper names sharing root letters with 'fire' but semantically unrelated -- another Hebrew triliteral-root collision. |
| 15:0 | H3915 | related_word | resolved |  | Mostly coincidental: Letushim (a tribe-name), 'to sharpen' -- tenuous or unrelated collisions with 'night', not a genuine semantic family. |
| 16:0 | H3588A | connective | resolved |  | Causal 'for' -- genuinely classifiable against the 3-class lexicon as causal, introducing the reason/basis for the preceding description. |
| 17:0 | H5921A | related_word | checked_empty |  | 0 related codes pulled. |
| 17:0 | H5921A | recurrence_role_shift | checked_empty | Isa.4.5:2 | Third occurrence of H5921A ('over') in this verse -- again no role shift from its first occurrence (position 2), correctly recorded checked_empty. |
| 18:0 | H3605 | related_word | resolved |  | Genuine family: all/entire/perfect (same root as position 3's 'whole') -- real semantic cluster. |
| 18:0 | H3605 | recurrence_role_shift | checked_empty | Isa.4.5:3 | Same code (H3605) as position 3 ('whole'), but both occurrences are the same distributive-quantifier role modifying a noun -- no genuine role shift, correctly recorded checked_empty rather than silently skipped. |
| 19:0 | H3519 | related_word | resolved |  | Genuine and notable: honor/heavy/glory (H3513-H3515) -- the well-known Hebrew 'weight = glory' semantic connection (kavod), a real and important finding for a study of this kind, not incidental. |
| 20:0 | H2646 | related_word | resolved |  | Mixed: Huppah/Huppim (proper names derived from the same root) alongside 'to cover'/'to shield' (H2645/H2653) -- a genuine, if modest, semantic connection to 'canopy' as a covering. |

---

## Amos.8.4 — Minor Prophet

> Hear this, you who trample on the needy and bring the poor of the land to an end,

**11 Layer 2 notes:**

| pos:ord | strong | note_type | status | target | finding |
|---|---|---|---|---|---|
| 0:0 | H8085G | related_word | checked_empty |  | 0 related codes pulled. |
| 1:0 | H2063 | related_word | resolved |  | Minor genuine relation: 'this' (H2088) shares the demonstrative family, real if trivial. |
| 2:0 | H7602B | related_word | checked_empty |  | 0 related codes pulled. |
| 2:1 | H9009 | inert | checked_empty |  | Definite article, function role. |
| 3:0 | H0034 | related_word | resolved |  | Genuine etymological finding: 'needy' (evyon) shares its root with 'to desire/be willing' (H0014/H0035) -- the needy are, at root, 'those who lack/desire', a real semantic insight. |
| 4:0 | H6041 | related_word | resolved |  | Genuine, strong family: afflict/poor/gentleness (H6031-H6038) -- a real, substantial semantic cluster central to this verse's own social-justice vocabulary. |
| 5:0 | H0776G | related_word | checked_empty |  | 0 related codes pulled. |
| 6:0 | H7673A | related_word | checked_empty |  | 0 related codes pulled. |
| 6:0 | H7673A | structural_pattern | resolved |  | 'trample on' / 'needy' / 'poor' form the indictment's own accusation cluster -- the verb and its two victim-terms named together as one social-justice charge. |
| 6:1 | H9002 | inert | checked_empty |  | Conjunctive component within the compound verb phrase, function role. |
| 6:2 | H9005 | inert | checked_empty |  | Prepositional component within the compound verb phrase, function role. |

---

## Mark.11.21 — Gospel narrative

> And Peter remembered and said to him, “ Rabbi, look! The fig tree that you cursed has withered.”

**14 Layer 2 notes:**

| pos:ord | strong | note_type | status | target | finding |
|---|---|---|---|---|---|
| 0:0 | G2532 | connective | resolved |  | Coordinating 'And' -- narrative sequencer opening the verse, genuinely classifiable against the 3-class lexicon. |
| 1:0 | G4074G | related_word | checked_empty |  | 0 related codes pulled. |
| 2:0 | G0363 | related_word | resolved |  | Genuine, direct family: remembrance / to remember (G0364/G3403) -- real cognates, expected. |
| 3:0 | G3004G | related_word | checked_empty |  | 0 related codes pulled. |
| 4:0 | G0846 | related_word | resolved |  | Minor genuine relation: reflexive-pronoun morphological family (G1438/G1683) -- real cognates, not a substantive finding on its own. |
| 4:0 | G0846 | entity_link | resolved |  | 'him' (dative) refers to Jesus, the addressee of Peter's remark -- confirmed from the target verse's own grammar (a vocative 'Rabbi' immediately follows), no adjacent-verse read needed. |
| 5:0 | G4461 | related_word | resolved |  | Genuine, direct cognate: Rabboni (G4462) -- the same honorific family, real. |
| 6:0 | G2396 | related_word | resolved |  | Genuine, direct cognate: 'to perceive/know' (G1492) -- 'look/behold' shares its root with 'to see', real and expected. |
| 7:0 | G4808 | related_word | resolved |  | Genuine botanical-term cluster: mulberry/sycamore/fig (G4807/G4809/G4810) -- real, all fruit-tree names sharing a root, not coincidental. |
| 7:0 | G4808 | entity_link | resolved | Mark.11.13:4 **(cross-verse)** | 'fig tree' (G4808) is the same tree Jesus approached in Mark.11.13 -- same strong code, same referent, confirmed by a targeted read of the earlier verse, exactly the kind of on-demand adjacent-verse check #1451's design describes. NOT cross_lemma_shared_gloss -- that note_type is for two DIFFERENT lemmas sharing a sense, not the same code recurring. |
| 8:0 | G3739 | related_word | checked_empty |  | 1 related code pulled, form/gloss empty -- not usable. |
| 8:0 | G3739 | pronoun_resolution | resolved | Mark.11.21:7 | 'that' (relative pronoun) refers to 'fig tree' (position 7) -- the relative clause's antecedent within the same verse. |
| 9:0 | G2672 | related_word | resolved |  | Genuine, direct family: cursed/curse (G1944/G2671) -- real cognates. |
| 10:0 | G3583 | related_word | resolved |  | Genuine, direct cognate: 'dried up/withered' (G3584) -- real, expected. |

---

## Rom.9.14 — Epistle/didactic

> What shall we say then? Is there injustice on God’s part? By no means!

**11 Layer 2 notes:**

| pos:ord | strong | note_type | status | target | finding |
|---|---|---|---|---|---|
| 0:0 | G5101 | related_word | resolved |  | Genuine interrogative-pronoun family: why?/one?/which? (G2444/G5100) -- real cognates, expected. |
| 1:0 | G4483 | related_word | resolved |  | Genuine, large cognate family: say/speak (G2036/G2046/G4482/G4487/G4489) -- the classic Greek verb-of-speech cluster, real. |
| 2:0 | G3767 | connective | unclassified |  | 'then' (oun) here is inferential -- drawing a conclusion from the preceding argument. The design's 3-class connective lexicon (causal/coordinating/purpose) has no inferential class -- correctly UNCLASSIFIED, the same taxonomy gap already found at Lev.17.16 (conditional) and Prov.31.30 (adversative); a real, recurring gap across this sample, not three unrelated one-offs. |
| 3:0 | G3361 | related_word | checked_empty |  | 0 related codes pulled. |
| 3:0 | G3361 | connective | resolved |  | Part of the me genoito ('by no means') rhetorical-denial construction together with positions 7-8 -- not an independent negation of a separate clause. |
| 4:0 | G0093 | related_word | resolved |  | Genuine, rich family: harm/crime/unjust/opponent/justice (G0091-G1341) -- a substantial semantic cluster directly relevant to Paul's own argument about justice/righteousness in Romans, a real and valuable finding for this letter specifically. |
| 5:0 | G3844 | related_word | checked_empty |  | 0 related codes pulled. |
| 6:0 | G2316 | related_word | resolved |  | Genuine, theologically rich family: without-God/goddess/divine/God-fighting/God-breathed (G0112-G2315) -- a real, significant cluster directly relevant to a study of divine-referring vocabulary specifically. |
| 7:0 | G3361 | related_word | checked_empty |  | 0 related codes pulled. |
| 7:0 | G3361 | idiom | resolved | Rom.9.14:8 | me genoito ('by no means') is a fixed, well-known Pauline rhetorical idiom for emphatic denial, spanning positions 7-8 -- not a literal statement. |
| 8:0 | G1096 | related_word | checked_empty |  | Only a self-referential match (ginomai to itself) -- not a genuine external relation. |

---
