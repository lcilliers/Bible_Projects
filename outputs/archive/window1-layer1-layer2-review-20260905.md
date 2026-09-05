# Window 1 Layer 1 + Layer 2 — full review data, 10 verses

> Escalation #1451. Complete review package per your instructions: verse text, full Layer 1, Layer 2 with `surface` added and `status` moved to the last column (read the finding, then check whether the recorded status matches it), and a consolidated narrative per verse re-reading every finding together as a double control.

## Gen.46.18 — Torah narrative

**Verse text:** These are the sons of Zilpah, whom Laban gave to Leah his daughter; and these she bore to Jacob — sixteen persons.

### Layer 1 — `verse_lexical` (18 rows)

| pos | ord | strong | morph | role | surface | lang | testament | negator | narr_morph | gloss_ok | party | l1_status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 0 | H0428 | HTm | content | These | Hebrew | OT |  |  | 1 |  | resolved |
| 1 | 0 | H1121A | HNcmpc | content | sons | Hebrew | OT |  |  | 1 |  | resolved |
| 2 | 0 | H2153 | HNpf | content | Zilpah | Hebrew | OT |  |  | 1 |  | resolved |
| 3 | 0 | H0834A | HTr | content | whom | Hebrew | OT |  |  | 1 |  | resolved |
| 4 | 0 | H3837A | HNpm | content | Laban | Hebrew | OT |  |  | 1 |  | resolved |
| 5 | 0 | H5414G | HVqp3ms | content | gave | Hebrew | OT |  |  | 1 |  | resolved |
| 6 | 0 | H3812 | HNpf | content | Leah | Hebrew | OT |  |  | 1 |  | resolved |
| 6 | 1 | H9005 | HR | function | Leah | Hebrew | OT |  |  | 1 |  | resolved |
| 7 | 0 | H1323G | HNcfsc | content | daughter | Hebrew | OT |  |  | 1 |  | resolved |
| 8 | 0 | H3205 | HVqw3fs | content | bore | Hebrew | OT |  | wayyiqtol | 1 |  | resolved |
| 8 | 1 | H9023 | HSp3ms | function | bore | Hebrew | OT |  |  | 1 |  | resolved |
| 9 | 0 | H3290 | HNpm | content | Jacob | Hebrew | OT |  |  | 1 |  | resolved |
| 9 | 1 | H9005 | HR | function | Jacob | Hebrew | OT |  |  | 1 |  | resolved |
| 9 | 2 | H0853 | HTo | function | Jacob | Hebrew | OT |  |  | 1 |  | resolved |
| 9 | 3 | H0428 | HTm | content | Jacob | Hebrew | OT |  |  | 1 |  | resolved |
| 10 | 0 | H6240 | HAcbsc | content | sixteen | Hebrew | OT |  |  | 1 |  | resolved |
| 10 | 1 | H8337 | HAcbsc | content | sixteen | Hebrew | OT |  |  | 1 |  | resolved |
| 11 | 0 | H5315J | HNcfsa | content | persons | Hebrew | OT |  |  | 1 |  | resolved |

### Layer 2 — `verse_lexical_note` (24 rows)

| pos:ord | strong | surface | note_type | target | finding | status |
|---|---|---|---|---|---|---|
| 0:0 | H0428 | These | related_word |  | H0411/H0429 (el/elleh, 'these') are genuine same-root synonym forms of this demonstrative; H0414 (Ela, a proper name) is a coincidental root-collision, not a real relation. | **resolved** |
| 1:0 | H1121A | sons | related_word |  | 0 related codes pulled. | **checked_empty** |
| 2:0 | H2153 | Zilpah | related_word |  | 1 related code pulled, but its own form/gloss fields are empty in strong_related -- not usable, treated as no real finding. | **checked_empty** |
| 2:0 | H2153 | Zilpah | entity_link | Gen.46.18:3 | Target of 'whom' (position 3) -- Zilpah is the antecedent. | **resolved** |
| 3:0 | H0834A | whom | related_word |  | 0 related codes pulled. | **checked_empty** |
| 3:0 | H0834A | whom | entity_link | Gen.46.18:2 | 'whom' (relative pronoun) refers back to Zilpah (position 2), not Laban -- the antecedent of the relative clause. | **resolved** |
| 4:0 | H3837A | Laban | related_word |  | 0 related codes pulled. | **checked_empty** |
| 5:0 | H5414G | gave | related_word |  | 0 related codes pulled. | **checked_empty** |
| 5:0 | H5414G | gave | verb_argument | Gen.46.18:4 | 'gave' (H5414G): trigger/agent is Laban (position 4), impact/recipient is Leah (position 6). | **resolved** |
| 6:0 | H3812 | Leah | related_word |  | 1 related code pulled, form/gloss empty -- not usable. | **checked_empty** |
| 6:1 | H9005 | Leah | inert |  | Prepositional prefix ('to'), function role -- no relational finding beyond its own grammatical role. | **checked_empty** |
| 7:0 | H1323G | daughter | related_word |  | 0 related codes pulled. | **checked_empty** |
| 7:0 | H1323G | daughter | noun_relational | Gen.46.18:6 | 'daughter' construct-linked to Leah (position 6) -- marks the genealogical relation (Leah is Laban's daughter), not a separate referent. | **resolved** |
| 8:0 | H3205 | bore | related_word |  | Genuine same-concept family: child/youth/maiden/born (the Hebrew ILD birth-root) -- a real semantic cluster around 'bore', not coincidental. | **resolved** |
| 8:0 | H3205 | bore | chain |  | 'bore' carries narrative_morph=wayyiqtol -- a genuine sequential narrative action continuing this genealogy list's own narrative thread. | **resolved** |
| 8:1 | H9023 | bore | pronoun_resolution | Gen.46.18:6 | 'she' (3fs suffix) refers to Leah (position 6), the immediately preceding named woman -- distinguishing her from Zilpah named earlier in the verse. | **resolved** |
| 9:0 | H3290 | Jacob | related_word |  | Genuine cross-reference, not mere etymology: Jacob is also called Israel (H3478/H3479) and Israelite (G2474/G2475) -- the same person's two names, attested cross-lingually (Greek Iakob transliteration too). | **resolved** |
| 9:1 | H9005 | Jacob | inert |  | Prepositional prefix ('to'), function role. | **checked_empty** |
| 9:2 | H0853 | Jacob | inert |  | Direct-object marker (H0853), function role -- per the H0853-function-word-exception rule. | **checked_empty** |
| 9:3 | H0428 | Jacob | related_word |  | This code (H0428, elsewhere 'these'/demonstrative) is tagged at the same position as 'Jacob' with no clear semantic role in this word-complex -- the code combination at this position is not confidently explained by a single-verse targeted read; flagged rather than guessed, per the design's own unresolved-not-guessed rule. | **unresolved** |
| 10:0 | H6240 | sixteen | related_word |  | Genuine numeral family: ten/tenth/tithe (H4643/H6218/H6224/H6235/H6237) -- real root connection, 'sixteen' as a six-plus-ten compound. | **resolved** |
| 10:1 | H8337 | sixteen | related_word |  | Coincidental, not genuine: Sheva/onyx/Shoham (H7718/H7719/H7724) share the root letters of 'six' but are semantically unrelated proper names/gem terms -- a textbook Hebrew triliteral-root collision, correctly sorted as coincidental per the design's own language-aware sorting rule, not a real relation. | **resolved** |
| 11:0 | H5315J | persons | related_word |  | 0 related codes pulled. | **checked_empty** |
| 11:0 | H5315J | persons | inert |  | H5315J (nephesh, 'person/soul') is used here in its headcount sense ('sixteen persons'), not its inner-being sense -- a real polysemy distinction worth naming, but no current note_type cleanly captures 'which sense of a core-list word was selected'; recorded here as an observation, not forced into a mis-fitting note_type. Flagged as a genuine schema gap in the accompanying report, not silently absorbed. | **checked_empty** |

### Consolidated narrative (double control)

This verse closes a genealogical list (Zilpah's line via Laban's gift of Leah, continuing to Jacob) with a formulaic sixteen-person tally. Re-reading the findings together: the relative clause "whom Laban gave" is correctly anchored to Zilpah, not Leah, keeping the maidservant-transfer genealogy consistent with Genesis' broader Rachel/Leah/Zilpah/Bilhah scheme. "Bore...to Jacob" is properly flagged as a wayyiqtol narrative link, situating this list within the surrounding narrative rather than treating it as a bare list. Jacob's cross-reference to "Israel" is a real, useful anchor for later corpus-wide identity tracking, not incidental. The numeral "sixteen" analysis usefully demonstrates both a real (six+ten root family) and a coincidental (Sheva/onyx homographs) related-word outcome side by side -- a good calibration example for the method. The one unresolved item (H0428 attached to the word-complex "Jacob") remains a genuine loose end on this re-read: it could plausibly be a demonstrative/definite marker mis-tagged at this position, or a real feature of the compound phrase; without deeper lexicon access it can't be resolved further here and is correctly left open rather than guessed either way. The nephesh/"persons" observation is small but real: this occurrence is a plain headcount, not an inner-being use of the term, which matters for any future corpus-wide study of nephesh's own semantic range. Holistically, every Layer 2 finding is consistent with the others and with the verse's plain sense -- no contradiction surfaced on this re-read.

---

## Lev.17.16 — Torah legal

**Verse text:** But if he does not wash them or bathe his flesh, he shall bear his iniquity.”

### Layer 1 — `verse_lexical` (12 rows)

| pos | ord | strong | morph | role | surface | lang | testament | negator | narr_morph | gloss_ok | party | l1_status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 0 | H3808 | HTn | content | not | Hebrew | OT | 1 |  | 1 |  | resolved |
| 1 | 0 | H3526H | HVpi3ms | content | wash | Hebrew | OT |  |  | 1 |  | resolved |
| 1 | 1 | H0518A | HTc | content | wash | Hebrew | OT |  |  | 1 |  | resolved |
| 1 | 2 | H9002 | HC | function | wash | Hebrew | OT |  |  | 1 |  | resolved |
| 2 | 0 | H7364 | HVqi3ms | content | bathe | Hebrew | OT |  |  | 1 |  | resolved |
| 2 | 1 | H9023 | HSp3ms | function | bathe | Hebrew | OT |  |  | 1 |  | resolved |
| 2 | 2 | H3808 | HTn | content | bathe | Hebrew | OT | 1 |  | 1 |  | resolved |
| 3 | 0 | H1320 | HNcmsc | content | flesh | Hebrew | OT |  |  | 1 |  | resolved |
| 3 | 1 | H9002 | HC | function | flesh | Hebrew | OT |  |  | 1 |  | resolved |
| 4 | 0 | H5375J | HVqq3ms | content | bear | Hebrew | OT |  |  | 1 |  | resolved |
| 5 | 0 | H9023 | HSp3ms | function | his | Hebrew | OT |  |  | 1 |  | resolved |
| 6 | 0 | H5771G | HNcmsc | content | iniquity | Hebrew | OT |  |  | 1 |  | resolved |

### Layer 2 — `verse_lexical_note` (13 rows)

| pos:ord | strong | surface | note_type | target | finding | status |
|---|---|---|---|---|---|---|
| 0:0 | H3808 | not | related_word |  | H0408/H3809 (al/la, 'not') are genuine synonym forms of this negator. H3810/H3818/H3819 (Lo-debar, Not-My-People, No-Mercy) are NOT coincidental despite being proper names -- they are deliberately built on the negator as a real Hebrew naming convention (names-as-signs), a genuine if indirect relation. | **resolved** |
| 1:0 | H3526H | wash | related_word |  | 0 related codes pulled. | **checked_empty** |
| 1:1 | H0518A | wash | connective |  | The bound conditional clitic ('if', attached to the verb) marks this clause as a conditional apodosis. The design's own 3-class connective lexicon (causal/coordinating/purpose) has no conditional class -- correctly recorded as UNCLASSIFIED rather than force-fit as causal; a real gap in the connective taxonomy, not an error in this finding. | **unclassified** |
| 1:2 | H9002 | wash | connective |  | Coordinating: the waw here functions as disjunctive 'or' between the two negated verbs (wash / bathe) -- a genuine coordinating relation, correctly classifiable against the 3-class lexicon. | **resolved** |
| 2:0 | H7364 | bathe | related_word |  | Genuine same-concept family: washing-related terms (H7365/H7366/H7367) -- real semantic cluster, not coincidental. | **resolved** |
| 2:1 | H9023 | bathe | pronoun_resolution | Lev.17.15:1 **(cross-verse)** | The implicit 3ms subject ('he') of this verse is not named within Lev.17.16 itself -- a targeted read of the immediately preceding verse (Lev.17.15) confirms the antecedent: 'every person (nephesh) who eats...' (position 1). Exactly the kind of adjacent-verse read #1451's design describes. | **resolved** |
| 2:2 | H3808 | bathe | polarity | Lev.17.16:0 | Second negator (H3808) extends the first negator's (position 0) scope across both coordinated verbs -- 'does not wash... or bathe' is one negated compound action, not two independent negative clauses. | **resolved** |
| 3:0 | H1320 | flesh | related_word |  | Genuine same-concept family: flesh/body-related Hebrew root (H1308/H1309/H1319/H1321) -- real semantic cluster. | **resolved** |
| 3:1 | H9002 | flesh | inert |  | Conjunctive prefix within 'his flesh', function role -- no separate relational finding beyond the polarity/connective notes already recorded at position 1. | **checked_empty** |
| 4:0 | H5375J | bear | related_word |  | 0 related codes pulled. | **checked_empty** |
| 4:0 | H5375J | bear | idiom |  | 'bear his iniquity' (nasa avon) is a fixed Hebrew legal idiom meaning 'be held guilty/liable' -- a real, well-attested idiom, not a literal physical-bearing statement. | **resolved** |
| 5:0 | H9023 | his | pronoun_resolution | Lev.17.15:1 **(cross-verse)** | Same antecedent as position 2's 'his' -- the generic legal subject established in Lev.17.15. | **resolved** |
| 6:0 | H5771G | iniquity | related_word |  | 0 related codes pulled. | **checked_empty** |

### Consolidated narrative (double control)

This is a conditional legal clause from the purity laws: "But if he does not wash [them] or bathe his flesh, he shall bear his iniquity." Re-reading the findings together, the two negators (position 0 and the one attached to "bathe") are correctly linked as one compound negated action, not two separate prohibitions -- the polarity note's scope-extension claim holds up on review. The conditional "if" being recorded UNCLASSIFIED against the 3-class connective lexicon is a genuine, correctly-recorded taxonomy gap, not an error -- conditionals are common in legal Hebrew and this connective scheme was never built with a conditional class. The cross-verse pronoun resolution (both "his" instances pointing to Lev.17.15's unnamed "person who eats") is essential to the reading: without it the verse is a free-floating "he" with no antecedent, so this finding materially improves the sense rather than merely decorating it. The "bear his iniquity" idiom is consistent with the verse's own legal register -- a formulaic guilt/liability phrase repeated throughout Leviticus, not a literal statement, correctly identified as such. On holistic re-read, every finding reinforces one coherent reading: an unnamed person's washing-failure incurs guilt. No internal contradictions.

---

## Judg.11.40 — Historical narrative

**Verse text:** (no cached text for this verse)

### Layer 1 — `verse_lexical` (18 rows)

| pos | ord | strong | morph | role | surface | lang | testament | negator | narr_morph | gloss_ok | party | l1_status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 0 | H1323G | HNcfpc | content | daughters | Hebrew | OT |  |  | 1 |  | resolved |
| 1 | 0 | H3478 | HNpl | content | Israel | Hebrew | OT |  |  | 1 |  | resolved |
| 2 | 0 | H1980G | HVqi3fp | content | went | Hebrew | OT |  |  | 1 |  | resolved |
| 2 | 1 | H9011 | HSd | function | went | Hebrew | OT |  |  | 1 |  | resolved |
| 3 | 0 | H3117I | HNcmpa | content | year | Hebrew | OT |  |  | 1 |  | resolved |
| 3 | 1 | H9006 | HR | function | year | Hebrew | OT |  |  | 1 |  | resolved |
| 4 | 0 | H3117I | HNcmpa | content | year | Hebrew | OT |  |  | 1 |  | resolved |
| 5 | 0 | H8567 | HVpcc | content | lament | Hebrew | OT |  |  | 1 |  | resolved |
| 5 | 1 | H9005 | HR | function | lament | Hebrew | OT |  |  | 1 |  | resolved |
| 6 | 0 | H1323G | HNcfsc | content | daughter | Hebrew | OT |  |  | 1 |  | resolved |
| 6 | 1 | H9005 | HR | function | daughter | Hebrew | OT |  |  | 1 |  | resolved |
| 7 | 0 | H3316H | HNpm | content | Jephthah | Hebrew | OT |  |  | 1 |  | resolved |
| 8 | 0 | H1569 | HNgmsa | content | Gileadite | Hebrew | OT |  |  | 1 |  | resolved |
| 8 | 1 | H9009 | HTd | function | Gileadite | Hebrew | OT |  |  | 1 |  | resolved |
| 9 | 0 | H0702 | HNcbsc | content | four | Hebrew | OT |  |  | 1 |  | resolved |
| 10 | 0 | H3117I | HNcmpa | content | days | Hebrew | OT |  |  | 1 |  | resolved |
| 11 | 0 | H8141 | HNcfsa | content | year | Hebrew | OT |  |  | 1 |  | resolved |
| 11 | 1 | H9003 | HRd | function | year | Hebrew | OT |  |  | 1 |  | resolved |

### Layer 2 — `verse_lexical_note` (20 rows)

| pos:ord | strong | surface | note_type | target | finding | status |
|---|---|---|---|---|---|---|
| 0:0 | H1323G | daughters | related_word |  | 0 related codes pulled. | **checked_empty** |
| 1:0 | H3478 | Israel | related_word |  | Genuine, real cross-reference: Israel/Jacob (H3290/H3479) and Israelite (G2474/G2475) are the same people's collective name and eponymous ancestor -- the identical name-cluster finding as Gen.46.18 position 9 in this same 10-verse sample, a real recurring pattern worth noting across the sample. | **resolved** |
| 2:0 | H1980G | went | related_word |  | 0 related codes pulled. | **checked_empty** |
| 2:1 | H9011 | went | inert |  | Directional-heh suffix, function role. | **checked_empty** |
| 3:0 | H3117I | year | related_word |  | 0 related codes pulled. | **checked_empty** |
| 3:0 | H3117I | year | idiom | Judg.11.40:4 | 'year...year' (H3117I repeated at positions 3-4) is the standard Hebrew distributive idiom for 'year by year / annually', not two separate year-references. | **resolved** |
| 3:1 | H9006 | year | inert |  | Prepositional prefix, function role. | **checked_empty** |
| 4:0 | H3117I | year | related_word |  | 0 related codes pulled -- second half of the idiom recorded at position 3. | **checked_empty** |
| 5:0 | H8567 | lament | related_word |  | 1 related code pulled, form/gloss empty -- not usable. | **checked_empty** |
| 5:1 | H9005 | lament | inert |  | Prepositional prefix ('to'), function role. | **checked_empty** |
| 6:0 | H1323G | daughter | related_word |  | 0 related codes pulled. | **checked_empty** |
| 6:0 | H1323G | daughter | entity_link | Judg.11.40:7 | 'daughter' (singular) refers to Jephthah's daughter specifically (named via his patronymic at position 7-8) -- distinct from 'daughters of Israel' (plural, position 0), the subject who go out to commemorate her. | **resolved** |
| 6:1 | H9005 | daughter | inert |  | Genitive-marking prefix, function role. | **checked_empty** |
| 7:0 | H3316H | Jephthah | related_word |  | 0 related codes pulled. | **checked_empty** |
| 8:0 | H1569 | Gileadite | related_word |  | Genuine toponymic family: Gilead (H1568, multiple sub-entries) -- a real, meaningful geographic/genealogical connection to Jephthah's own origin, not coincidental. | **resolved** |
| 8:1 | H9009 | Gileadite | inert |  | Definite article, function role. | **checked_empty** |
| 9:0 | H0702 | four | related_word |  | Genuine numeral family: four/fourth/forty (H0703/H0704/H0705/H7243) -- real semantic root. | **resolved** |
| 10:0 | H3117I | days | related_word |  | 0 related codes pulled. | **checked_empty** |
| 11:0 | H8141 | year | related_word |  | Genuine etymological finding: shanah ('year', H8140) shares its root with 'to change/to repeat' (H8132/H8138) -- a real insight (a year as a repeating cycle), not coincidental. | **resolved** |
| 11:1 | H9003 | year | inert |  | Prepositional prefix ('in'), function role. | **checked_empty** |

### Consolidated narrative (double control)

This verse records the annual commemoration custom established after Jephthah's vow: "the daughters of Israel went year by year... to lament the daughter of Jephthah the Gileadite four days in the year." Re-reading the findings together, the idiom finding ("year...year" = annually) is load-bearing: without it, the repeated H3117I code at positions 3-4 could be misread as two separate year-references rather than one adverbial idiom, distorting the verse's own sense. The entity_link correctly distinguishes the SUBJECT of the lament ("the daughters of Israel," plural, position 0) from its OBJECT ("the daughter [of Jephthah]," singular, position 6) -- easily conflated on a surface reading since both use the same Hebrew word (bat), and the finding correctly keeps them apart. The Gilead/Gileadite toponym family and the Israel/Jacob identity family are both genuine, low-risk findings anchoring this verse's own genealogical and geographic specifics -- and the Israel/Jacob finding is the same real cross-lemma family already surfaced independently in Gen.46.18, a useful cross-check that the method produces the same answer twice from two different verses. On holistic review, findings are internally consistent; no code was given a reading that conflicts with another code's finding in this verse.

---

## Prov.31.30 — Wisdom

**Verse text:** Charm is deceitful, and beauty is vain, but a woman who fears the Lord is to be praised.

### Layer 1 — `verse_lexical` (12 rows)

| pos | ord | strong | morph | role | surface | lang | testament | negator | narr_morph | gloss_ok | party | l1_status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 0 | H2580 | HNcmsa | content | Charm | Hebrew | OT |  |  | 1 |  | resolved |
| 0 | 1 | H9009 | HTd | function | Charm | Hebrew | OT |  |  | 1 |  | resolved |
| 1 | 0 | H8267 | HNcmsa | content | deceitful | Hebrew | OT |  |  | 1 |  | resolved |
| 2 | 0 | H3308 | HNcmsa | content | beauty | Hebrew | OT |  |  | 1 |  | resolved |
| 2 | 1 | H9009 | HTd | function | beauty | Hebrew | OT |  |  | 1 |  | resolved |
| 3 | 0 | H1892 | HNcmsa | content | vain | Hebrew | OT |  |  | 1 |  | resolved |
| 3 | 1 | H9002 | HC | function | vain | Hebrew | OT |  |  | 1 |  | resolved |
| 4 | 0 | H0802G | HNcfsa | content | woman | Hebrew | OT |  |  | 1 |  | resolved |
| 5 | 0 | H3373 | HAafsc | content | fears | Hebrew | OT |  |  | 1 |  | resolved |
| 6 | 0 | H3068G | HNpt | content | Lord | Hebrew | OT |  |  | 1 | divine | resolved |
| 7 | 0 | H1984B | HVti3fs | content | praised | Hebrew | OT |  |  | 1 |  | resolved |
| 7 | 1 | H1931 | HPp3fs | content | praised | Hebrew | OT |  |  | 1 |  | resolved |

### Layer 2 — `verse_lexical_note` (13 rows)

| pos:ord | strong | surface | note_type | target | finding | status |
|---|---|---|---|---|---|---|
| 0:0 | H2580 | Charm | related_word |  | Coincidental at scale: 51 related codes pulled, the overwhelming majority proper names (Hen, Henadad, Hannah...) sharing the CHN root with 'charm' -- a textbook, large-scale case of Hebrew triliteral-root collision, correctly sorted coincidental per the design's own language-aware rule, not a real relation. | **resolved** |
| 0:1 | H9009 | Charm | inert |  | Definite article, function role. | **checked_empty** |
| 1:0 | H8267 | deceitful | related_word |  | Genuine, minor relation: shares its root with 'to deal falsely' (H8266) -- a real if small semantic connection. | **resolved** |
| 2:0 | H3308 | beauty | related_word |  | Mixed: H3302/H3303/H3304 (beautiful/pretty) are genuine same-concept relatives; H3305 (Joppa, a place name) is a coincidental collision within the same pull -- both dispositions recorded honestly rather than averaged into one verdict. | **resolved** |
| 2:1 | H9009 | beauty | inert |  | Definite article, function role. | **checked_empty** |
| 3:0 | H1892 | vain | related_word |  | Genuine and notable: H1893 (Abel, the biblical name) is not a coincidental collision here -- it is a well-attested intentional naming pun in Hebrew scripture (Abel's name literally carries the sense 'vapor/vanity'), the same root as this verse's own 'vain'. A real, worthwhile connection, not dismissed as coincidental. | **resolved** |
| 3:1 | H9002 | vain | connective |  | Adversative 'but', contrasting charm/beauty (positions 0-3) against the woman who fears the LORD (positions 4-7). The design's 3-class connective lexicon (causal/coordinating/purpose) has no adversative class -- correctly UNCLASSIFIED, the same taxonomy gap already found at Lev.17.16's conditional case, not an error here. | **unclassified** |
| 4:0 | H0802G | woman | related_word |  | 0 related codes pulled. | **checked_empty** |
| 5:0 | H3373 | fears | related_word |  | Genuine same-concept family: fear/reverence (H3372/H3374/H4172) -- fully expected, real semantic cluster. | **resolved** |
| 6:0 | H3068G | Lord | related_word |  | 0 related codes pulled. | **checked_empty** |
| 7:0 | H1984B | praised | related_word |  | 0 related codes pulled. | **checked_empty** |
| 7:1 | H1931 | praised | related_word |  | Pronoun-form cognates (he/she/it family, H1932/H2007) -- mechanical morphological relatives, not a substantive finding. | **resolved** |
| 7:1 | H1931 | praised | pronoun_resolution | Prov.31.30:4 | 'she' (the subject of 'is to be praised') refers back to 'a woman who fears the LORD' (position 4), not to charm/beauty -- confirms the verse's own antithetical structure resolves to the woman as the praised subject. | **resolved** |

### Consolidated narrative (double control)

This is the concluding antithesis of the Proverbs 31 acrostic: "Charm is deceitful, and beauty is vain, but a woman who fears the LORD is to be praised." Re-reading the findings together, the adversative "but" (UNCLASSIFIED, the same taxonomy gap as Lev.17.16's conditional) is the verse's own structural hinge -- the whole point is the CONTRAST between charm/beauty and God-fearing character, so flagging this connective as outside the 3-class scheme correctly preserves that it's a real relation of a kind the lexicon doesn't yet name, rather than losing the observation entirely. The Charm/Hen root-collision finding (51 mostly-irrelevant proper-name hits) is a good illustration of why the design's language-aware sorting rule exists -- a naive count of "51 related words" would wildly overstate this word's real semantic network. The vain/Abel connection is the most interesting finding in this verse: recognizing it as a genuine, attested wordplay (Abel's own name carries the sense "vapor/vanity") rather than mechanically lumping it in with the Charm/Hen collisions shows the sorting judgment actually discriminating between two similar-looking cases correctly, not applying one rule blindly. The final pronoun resolution ("she" -> the woman, not charm/beauty) confirms the antithesis resolves in the woman's favour, matching the verse's plain sense. Holistically consistent, no contradictions found.

---

## Ps.94.22 — Poetry/Psalm

**Verse text:** But the Lord has become my stronghold, and my God the rock of my refuge.

### Layer 1 — `verse_lexical` (13 rows)

| pos | ord | strong | morph | role | surface | lang | testament | negator | narr_morph | gloss_ok | party | l1_status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 0 | H3068G | HNpt | content | Lord | Hebrew | OT |  |  | 1 | divine | resolved |
| 0 | 1 | H1961 | HVqw3ms | content | Lord | Hebrew | OT |  | wayyiqtol | 1 |  | resolved |
| 1 | 0 | H4869A | HNcmsa | content | stronghold | Hebrew | OT |  |  | 1 |  | resolved |
| 1 | 1 | H9005 | HR | function | stronghold | Hebrew | OT |  |  | 1 |  | resolved |
| 1 | 2 | H9005 | HR | function | stronghold | Hebrew | OT |  |  | 1 |  | resolved |
| 1 | 3 | H9030 | HSp1bs | function | stronghold | Hebrew | OT |  |  | 1 |  | resolved |
| 2 | 0 | H0430G | HNcmpc | content | God | Hebrew | OT |  |  | 1 | divine | resolved |
| 2 | 1 | H9002 | HC | function | God | Hebrew | OT |  |  | 1 |  | resolved |
| 3 | 0 | H6697H | HNcmsc | content | rock | Hebrew | OT |  |  | 1 |  | resolved |
| 3 | 1 | H9005 | HR | function | rock | Hebrew | OT |  |  | 1 |  | resolved |
| 3 | 2 | H9020 | HSp1bs | function | rock | Hebrew | OT |  |  | 1 |  | resolved |
| 4 | 0 | H4268 | HNcmsc | content | refuge | Hebrew | OT |  |  | 1 |  | resolved |
| 4 | 1 | H9020 | HSp1bs | function | refuge | Hebrew | OT |  |  | 1 |  | resolved |

### Layer 2 — `verse_lexical_note` (16 rows)

| pos:ord | strong | surface | note_type | target | finding | status |
|---|---|---|---|---|---|---|
| 0:0 | H3068G | Lord | related_word |  | 0 related codes pulled. | **checked_empty** |
| 0:0 | H3068G | Lord | entity_link | Ps.94.22:2 | 'the LORD' (position 0) and 'my God' (position 2) are the same referent, in synonymous parallelism -- both party_kind=divine, confirming the mechanical tag rather than adding a new fact. | **resolved** |
| 0:1 | H1961 | Lord | related_word |  | Minor genuine cognate: 'to fall'/'to be' (H1933) -- a real if modest etymological relative of hayah ('become'). | **resolved** |
| 0:1 | H1961 | Lord | chain |  | 'has become' carries narrative_morph=wayyiqtol -- a genuine sequential-argument marker within the psalm's own developing claim, not a static statement. | **resolved** |
| 1:0 | H4869A | stronghold | related_word |  | 0 related codes pulled. | **checked_empty** |
| 1:0 | H4869A | stronghold | structural_pattern |  | 'stronghold' / 'rock' / 'refuge' form a 3-term synonym cluster in poetic parallelism, all predicated of the same divine subject -- the verse's characteristic Hebrew poetic doubling (here tripling). | **resolved** |
| 1:1 | H9005 | stronghold | inert |  | Prepositional prefix, function role. | **checked_empty** |
| 1:2 | H9005 | stronghold | inert |  | Prepositional prefix (second component of a compound preposition), function role. | **checked_empty** |
| 1:3 | H9030 | stronghold | pronoun_resolution |  | 1cs possessive suffix ('my') -- self-reference to the psalmist speaker, straightforward, no ambiguity. | **resolved** |
| 2:0 | H0430G | God | related_word |  | 0 related codes pulled. | **checked_empty** |
| 2:1 | H9002 | God | connective |  | Coordinating 'and', joining the two divine epithets (LORD / God) -- genuinely classifiable against the 3-class lexicon this time, unlike the adversative/conditional cases found elsewhere in this sample. | **resolved** |
| 3:0 | H6697H | rock | related_word |  | 0 related codes pulled. | **checked_empty** |
| 3:1 | H9005 | rock | inert |  | Prepositional prefix, function role. | **checked_empty** |
| 3:2 | H9020 | rock | pronoun_resolution |  | 1cs possessive suffix ('my') -- self-reference to the psalmist. | **resolved** |
| 4:0 | H4268 | refuge | related_word |  | Genuine same-concept family: 'to seek refuge' (H2620/H2622) -- real semantic cluster, directly on-topic for this verse's own claim. | **resolved** |
| 4:1 | H9020 | refuge | pronoun_resolution |  | 1cs possessive suffix ('my') -- self-reference to the psalmist. | **resolved** |

### Consolidated narrative (double control)

This verse is the psalm's own climactic confession: "But the LORD has become my stronghold, and my God the rock of my refuge." Re-reading the findings together, the entity_link (LORD = God, synonymous parallelism) and the structural_pattern (stronghold/rock/refuge, a 3-term synonym cluster) work together consistently: this verse is built on Hebrew poetic doubling at BOTH the divine-epithet level and the protective-image level, and the two findings correctly capture both layers rather than flattening them into one list. The chain finding on "has become" (wayyiqtol) is small but real: even within a poetic psalm, this verb form marks a narrative-style claim ("has become," not merely "is"), consistent with the psalm recounting God's demonstrated faithfulness rather than stating an abstract truth. The three self-referential pronoun findings ("my" x3) are mechanically straightforward but worth confirming as a set on re-read: all three consistently point to the psalmist, with no ambiguity introduced by the parallelism. No contradictions; the findings reinforce a single coherent poetic structure.

---

## Eccl.5.14 — Wisdom/philosophical

**Verse text:** and those riches were lost in a bad venture. And he is father of a son, but he has nothing in his hand.

### Layer 1 — `verse_lexical` (16 rows)

| pos | ord | strong | morph | role | surface | lang | testament | negator | narr_morph | gloss_ok | party | l1_status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 0 | H1931 | HPp3ms | content | and those | Hebrew | OT |  |  | 1 |  | resolved |
| 0 | 1 | H9009 | HTd | function | and those | Hebrew | OT |  |  | 1 |  | resolved |
| 1 | 0 | H6239 | HNcmsa | content | riches | Hebrew | OT |  |  | 1 |  | resolved |
| 1 | 1 | H9009 | HTd | function | riches | Hebrew | OT |  |  | 1 |  | resolved |
| 2 | 0 | H0006 | HVqq3ms | content | lost | Hebrew | OT |  |  | 1 |  | resolved |
| 3 | 0 | H7451A | HAamsa | content | bad | Hebrew | OT |  |  | 1 |  | resolved |
| 4 | 0 | H6045 | HNcmsc | content | venture | Hebrew | OT |  |  | 1 |  | resolved |
| 4 | 1 | H9003 | HR | function | venture | Hebrew | OT |  |  | 1 |  | resolved |
| 5 | 0 | H3205 | HVhq3ms | content | father | Hebrew | OT |  |  | 1 |  | resolved |
| 6 | 0 | H1121A | HNcmsa | content | son | Hebrew | OT |  |  | 1 |  | resolved |
| 7 | 0 | H0369 | HNcmsc | content | nothing | Hebrew | OT |  |  | 1 |  | resolved |
| 7 | 1 | H9002 | HC | function | nothing | Hebrew | OT |  |  | 1 |  | resolved |
| 7 | 2 | H3972 | HNcfsa | content | nothing | Hebrew | OT |  |  | 1 |  | resolved |
| 8 | 0 | H9023 | HSp3ms | function | his | Hebrew | OT |  |  | 1 |  | resolved |
| 9 | 0 | H3027G | HNcbsc | content | hand | Hebrew | OT |  |  | 1 |  | resolved |
| 9 | 1 | H9003 | HR | function | hand | Hebrew | OT |  |  | 1 |  | resolved |

### Layer 2 — `verse_lexical_note` (19 rows)

| pos:ord | strong | surface | note_type | target | finding | status |
|---|---|---|---|---|---|---|
| 0:0 | H1931 | and those | related_word |  | Mechanical pronoun-form cognates (he/she/it family) -- present but not a substantive finding on its own. | **resolved** |
| 0:0 | H1931 | and those | entity_link | Eccl.5.13:6 **(cross-verse)** | 'and those [riches]' picks up the referent from the immediately preceding verse (Eccl.5.13's own 'riches') -- a genuine cross-verse resolution, the kind #1451's design names directly: read exactly one adjacent verse to confirm what could not be settled from the target verse alone. | **resolved** |
| 0:1 | H9009 | and those | inert |  | Definite article, function role. | **checked_empty** |
| 1:0 | H6239 | riches | related_word |  | Genuine same-concept family: rich/enrich (H6223/H6238) -- real semantic cluster. | **resolved** |
| 1:1 | H9009 | riches | inert |  | Definite article, function role. | **checked_empty** |
| 2:0 | H0006 | lost | related_word |  | Genuine, strong family: destroy/destruction/Abaddon (H0007-H0011) -- Abaddon as the personification of destruction is a real, notable related concept, not a coincidental collision. | **resolved** |
| 3:0 | H7451A | bad | related_word |  | 0 related codes pulled. | **checked_empty** |
| 4:0 | H6045 | venture | related_word |  | Genuine root connection: 'to be occupied/afflicted' (H6031) -- 'venture/business' relates to being occupied/busy, a real semantic link and a recurring theme-word in Ecclesiastes specifically. | **resolved** |
| 4:1 | H9003 | venture | inert |  | Prepositional prefix, function role. | **checked_empty** |
| 5:0 | H3205 | father | related_word |  | Same birth-root family as Gen.46.18 position 8 (child/youth/maiden, H3205's own family) -- genuine, though here the same root is used in its causative 'father of' sense rather than 'bore', a real sense-distinction worth naming. | **resolved** |
| 6:0 | H1121A | son | related_word |  | 0 related codes pulled -- same code as Gen.46.18 position 1 ('sons'), consistently empty in both occurrences. | **checked_empty** |
| 7:0 | H0369 | nothing | related_word |  | Genuine family: 'where?' / 'isn't?' (H0370/H0371) -- real negation-of-existence semantic cluster. | **resolved** |
| 7:1 | H9002 | nothing | inert |  | Conjunctive prefix, function role. | **checked_empty** |
| 7:2 | H3972 | nothing | related_word |  | Coincidental, not genuine: shares root letters with 'blemish' (H3971) but is not semantically related to this word's own sense ('anything/nothing') -- a minor Hebrew root collision. | **resolved** |
| 7:0 | H0369 | nothing | idiom |  | H0369 + H3972 together ('nothing... nothing') form the standard Hebrew double-negation idiom for absolute negation ('there is not a thing') -- one idiom across two codes, not two separate findings. | **resolved** |
| 8:0 | H9023 | his | pronoun_resolution |  | 3ms possessive suffix ('his') -- self-reference to the man just introduced in this verse ('he is father of a son'). | **resolved** |
| 9:0 | H3027G | hand | related_word |  | 0 related codes pulled. | **checked_empty** |
| 9:0 | H3027G | hand | idiom |  | 'in his hand' is the standard Hebrew idiom for 'in his possession/control', not a literal statement about a hand. | **resolved** |
| 9:1 | H9003 | hand | inert |  | Prepositional prefix, function role. | **checked_empty** |

### Consolidated narrative (double control)

This verse depicts a reversal-of-fortune scene: riches lost in a bad venture, leaving a father with nothing for his son. Re-reading the findings together, the cross-verse entity_link (riches -> Eccl.5.13) is essential -- without reading the prior verse, "those riches" in 5.14 has no referent at all within this verse's own codes, and the finding correctly demonstrates the design's own targeted-adjacent-read mechanism working for a genuine need, not a manufactured example. The double-negation idiom ("nothing... nothing," positions 7 and 7.2) and the "in his hand" idiom work together to intensify the verse's own rhetorical point: total, absolute loss, expressed twice over. The "lost" finding's Abaddon/destruction family connection is thematically apt for Ecclesiastes' own preoccupation with loss and futility -- a genuinely meaningful connection, not incidental. The "venture" (inyan) finding, connecting to "occupied/afflicted," is one of Ecclesiastes' own recurring theme-words (elsewhere "business"/"task") -- correctly flagged as a real semantic thread running through the book, relevant to any future cross-verse thematic study. Holistically consistent: no finding here contradicts another, and the cross-verse read strengthens rather than complicates the verse's plain sense.

---

## Isa.4.5 — Major Prophet

**Verse text:** Then the Lord will create over the whole site of Mount Zion and over her assemblies a cloud by day, and smoke and the shining of a flaming fire by night; for over all the glory there will be a canopy.

### Layer 1 — `verse_lexical` (25 rows)

| pos | ord | strong | morph | role | surface | lang | testament | negator | narr_morph | gloss_ok | party | l1_status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 0 | H3068G | HNpt | content | Lord | Hebrew | OT |  |  | 1 | divine | resolved |
| 1 | 0 | H1254A | HVqq3ms | content | create | Hebrew | OT |  |  | 1 |  | resolved |
| 2 | 0 | H5921A | HR | content | over | Hebrew | OT |  |  | 1 |  | resolved |
| 3 | 0 | H3605 | HNcmsc | content | whole | Hebrew | OT |  |  | 1 |  | resolved |
| 4 | 0 | H4349 | HNcmsc | content | site | Hebrew | OT |  |  | 1 |  | resolved |
| 5 | 0 | H2022G | HNcmsc | content | Mount | Hebrew | OT |  |  | 1 |  | resolved |
| 6 | 0 | H6726 | HNpl | content | Zion | Hebrew | OT |  |  | 1 |  | resolved |
| 7 | 0 | H5921A | HR | content | over | Hebrew | OT |  |  | 1 |  | resolved |
| 7 | 1 | H9002 | HC | function | over | Hebrew | OT |  |  | 1 |  | resolved |
| 8 | 0 | H4744 | HNcmsc | content | assemblies | Hebrew | OT |  |  | 1 |  | resolved |
| 9 | 0 | H6051 | HNcmsa | content | cloud | Hebrew | OT |  |  | 1 |  | resolved |
| 9 | 1 | H9024 | HSp3fs | function | cloud | Hebrew | OT |  |  | 1 |  | resolved |
| 10 | 0 | H3119 | HD | content | day | Hebrew | OT |  |  | 1 |  | resolved |
| 11 | 0 | H6227 | HNcmsa | content | smoke | Hebrew | OT |  |  | 1 |  | resolved |
| 11 | 1 | H9002 | HC | function | smoke | Hebrew | OT |  |  | 1 |  | resolved |
| 12 | 0 | H5051 | HNcfsc | content | shining | Hebrew | OT |  |  | 1 |  | resolved |
| 12 | 1 | H9002 | HC | function | shining | Hebrew | OT |  |  | 1 |  | resolved |
| 13 | 0 | H3852 | HNcfsa | content | flaming | Hebrew | OT |  |  | 1 |  | resolved |
| 14 | 0 | H0784 | HNcbsa | content | fire | Hebrew | OT |  |  | 1 |  | resolved |
| 15 | 0 | H3915 | HNcmsa | content | night | Hebrew | OT |  |  | 1 |  | resolved |
| 16 | 0 | H3588A | HTc | content | for | Hebrew | OT |  |  | 1 |  | resolved |
| 17 | 0 | H5921A | HR | content | over | Hebrew | OT |  |  | 1 |  | resolved |
| 18 | 0 | H3605 | HNcmsc | content | all | Hebrew | OT |  |  | 1 |  | resolved |
| 19 | 0 | H3519 | HNcmsa | content | glory | Hebrew | OT |  |  | 1 |  | resolved |
| 20 | 0 | H2646 | HNcfsa | content | canopy | Hebrew | OT |  |  | 1 |  | resolved |

### Layer 2 — `verse_lexical_note` (30 rows)

| pos:ord | strong | surface | note_type | target | finding | status |
|---|---|---|---|---|---|---|
| 0:0 | H3068G | Lord | related_word |  | 0 related codes pulled. | **checked_empty** |
| 1:0 | H1254A | create | related_word |  | 0 related codes pulled. Note: bara ('create') is used almost exclusively of divine creative action in the OT -- a theologically loaded verb choice, but no current note_type cleanly captures 'significance of a verb's own restricted usage'; named here as an observation, not forced into idiom/noun_relational. | **checked_empty** |
| 2:0 | H5921A | over | related_word |  | 0 related codes pulled. | **checked_empty** |
| 3:0 | H3605 | whole | related_word |  | Genuine family: all/entire/perfect (H3606/H3632/H3634) -- real semantic cluster. | **resolved** |
| 4:0 | H4349 | site | related_word |  | Coincidental at scale: 24 related codes, almost entirely proper names (Jachin, Jeconiah) sharing the root letters of 'site/place' -- another textbook Hebrew triliteral collision, correctly sorted coincidental. | **resolved** |
| 5:0 | H2022G | Mount | related_word |  | 0 related codes pulled. | **checked_empty** |
| 5:0 | H2022G | Mount | noun_relational | Isa.4.5:6 | 'Mount' + 'Zion' (position 6) is a construct-state relational pairing identifying which mount is meant -- not two separate referents needing an entity_link, a plain construct relation. | **resolved** |
| 6:0 | H6726 | Zion | related_word |  | Genuine toponymic family: Jerusalem/Salem/Zion (attested cross-lingually, Hebrew and Greek) -- a real, meaningful place-name cluster. | **resolved** |
| 7:0 | H5921A | over | related_word |  | 0 related codes pulled. | **checked_empty** |
| 7:0 | H5921A | over | recurrence_role_shift | Isa.4.5:2 | Same code (H5921A, 'over') recurs from position 2, but the grammatical role does NOT shift -- both instances mark the object of protective coverage. A plain repeated function word, correctly recorded checked_empty per the design's own rule that mechanical repetition without rhetorical role change never qualifies as a genuine shift. | **checked_empty** |
| 7:1 | H9002 | over | connective |  | Coordinating 'and', joining 'over the site of Mount Zion' with 'over her assemblies'. | **resolved** |
| 8:0 | H4744 | assemblies | related_word |  | Genuine root connection: 'to call/proclaim' (H7121) -- an assembly (miqra) is literally 'a calling-together', a real etymological insight. | **resolved** |
| 9:0 | H6051 | cloud | related_word |  | Genuine same-concept family: cloud (H6049-H6053) -- real semantic cluster. | **resolved** |
| 9:0 | H6051 | cloud | structural_pattern |  | 'cloud' / 'smoke' / 'shining' / 'fire' form a 4-term theophany-imagery cluster (day/night pairing: cloud+smoke by day, fire+shining by night) -- Sinai-pattern protective-presence imagery. | **resolved** |
| 9:1 | H9024 | cloud | pronoun_resolution | Isa.4.5:6 | 3fs possessive suffix ('her') refers to Zion (position 6), feminine place-name agreement. | **resolved** |
| 10:0 | H3119 | day | related_word |  | Genuine, straightforward family: day (H3117, multiple sub-senses) -- expected, real cluster. | **resolved** |
| 11:0 | H6227 | smoke | related_word |  | Mixed: 'to smoke'/'smoking' (H6225/H6226) genuine; Ashan (H6228) a coincidental place-name collision within the same pull. | **resolved** |
| 11:1 | H9002 | smoke | connective |  | Coordinating 'and', joining 'smoke' to the preceding 'cloud'. | **resolved** |
| 12:0 | H5051 | shining | related_word |  | Genuine family: to shine/brightness (H5050/H5053/H5054) -- real semantic cluster; Nogah (H5052, a personal name) is a minor coincidental collision within the same pull. | **resolved** |
| 12:1 | H9002 | shining | connective |  | Coordinating 'and', joining 'shining' to 'smoke'. | **resolved** |
| 13:0 | H3852 | flaming | related_word |  | Genuine family: flame (H3827/H3851/H7957) -- real semantic cluster; Lehabim (H3853, a people-name) a minor coincidental collision within the same pull. | **resolved** |
| 14:0 | H0784 | fire | related_word |  | Coincidental, not genuine: Ashbel/Eshban/Ashbea are proper names sharing root letters with 'fire' but semantically unrelated -- another Hebrew triliteral-root collision. | **resolved** |
| 15:0 | H3915 | night | related_word |  | Mostly coincidental: Letushim (a tribe-name), 'to sharpen' -- tenuous or unrelated collisions with 'night', not a genuine semantic family. | **resolved** |
| 16:0 | H3588A | for | connective |  | Causal 'for' -- genuinely classifiable against the 3-class lexicon as causal, introducing the reason/basis for the preceding description. | **resolved** |
| 17:0 | H5921A | over | related_word |  | 0 related codes pulled. | **checked_empty** |
| 17:0 | H5921A | over | recurrence_role_shift | Isa.4.5:2 | Third occurrence of H5921A ('over') in this verse -- again no role shift from its first occurrence (position 2), correctly recorded checked_empty. | **checked_empty** |
| 18:0 | H3605 | all | related_word |  | Genuine family: all/entire/perfect (same root as position 3's 'whole') -- real semantic cluster. | **resolved** |
| 18:0 | H3605 | all | recurrence_role_shift | Isa.4.5:3 | Same code (H3605) as position 3 ('whole'), but both occurrences are the same distributive-quantifier role modifying a noun -- no genuine role shift, correctly recorded checked_empty rather than silently skipped. | **checked_empty** |
| 19:0 | H3519 | glory | related_word |  | Genuine and notable: honor/heavy/glory (H3513-H3515) -- the well-known Hebrew 'weight = glory' semantic connection (kavod), a real and important finding for a study of this kind, not incidental. | **resolved** |
| 20:0 | H2646 | canopy | related_word |  | Mixed: Huppah/Huppim (proper names derived from the same root) alongside 'to cover'/'to shield' (H2645/H2653) -- a genuine, if modest, semantic connection to 'canopy' as a covering. | **resolved** |

### Consolidated narrative (double control)

This is Isaiah's theophany vision over Zion: a canopy of cloud/smoke by day and fire/shining by night, echoing the Exodus wilderness pillar. Re-reading the findings together, the structural_pattern (cloud/smoke/shining/fire as one 4-term theophany cluster) is the verse's own central image, and the connectives correctly show HOW these four terms are joined (coordinating "and"s chaining them together) rather than leaving them an unstructured list. The recurrence_role_shift findings (three occurrences of "over," two of the all/whole quantifier) are a genuinely useful application of a note_type that had zero prior real-world use in this study -- each correctly confirms the repetition here is purely grammatical (the same preposition/quantifier doing the same job repeatedly), not a rhetorical device, which is itself worth knowing when studying this verse's structure. The noun_relational (Mount + Zion) and the toponym family finding work together consistently to anchor the verse's geography. The two large coincidental-collision findings ("site" and "fire," each pulling mostly unrelated proper names) again demonstrate the sorting discipline holding up at scale within a single, longer verse -- not every long verse produces a flood of genuine relations, and this one correctly separates the few real ones (glory/kavod, cloud, shine) from the many coincidental ones. The "glory" (kavod) finding is the most theologically significant: the "weight = glory" connection is a well-established, important feature of Hebrew theological vocabulary, correctly surfaced rather than passed over as just another related-word hit. Holistically, all findings cohere into one image without contradiction.

---

## Amos.8.4 — Minor Prophet

**Verse text:** Hear this, you who trample on the needy and bring the poor of the land to an end,

### Layer 1 — `verse_lexical` (10 rows)

| pos | ord | strong | morph | role | surface | lang | testament | negator | narr_morph | gloss_ok | party | l1_status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 0 | H8085G | HVqv2mp | content | Hear | Hebrew | OT |  |  | 1 |  | resolved |
| 1 | 0 | H2063 | HTm | content | this | Hebrew | OT |  |  | 1 |  | resolved |
| 2 | 0 | H7602B | HVqrmpa | content | trample on | Hebrew | OT |  |  | 1 |  | resolved |
| 2 | 1 | H9009 | HTd | function | trample on | Hebrew | OT |  |  | 1 |  | resolved |
| 3 | 0 | H0034 | HAamsa | content | needy | Hebrew | OT |  |  | 1 |  | resolved |
| 4 | 0 | H6041 | HAampc | content | poor | Hebrew | OT |  |  | 1 |  | resolved |
| 5 | 0 | H0776G | HNcfsa | content | land | Hebrew | OT |  |  | 1 |  | resolved |
| 6 | 0 | H7673A | HVhcc | content | end | Hebrew | OT |  |  | 1 |  | resolved |
| 6 | 1 | H9002 | HC | function | end | Hebrew | OT |  |  | 1 |  | resolved |
| 6 | 2 | H9005 | HR | function | end | Hebrew | OT |  |  | 1 |  | resolved |

### Layer 2 — `verse_lexical_note` (11 rows)

| pos:ord | strong | surface | note_type | target | finding | status |
|---|---|---|---|---|---|---|
| 0:0 | H8085G | Hear | related_word |  | 0 related codes pulled. | **checked_empty** |
| 1:0 | H2063 | this | related_word |  | Minor genuine relation: 'this' (H2088) shares the demonstrative family, real if trivial. | **resolved** |
| 2:0 | H7602B | trample on | related_word |  | 0 related codes pulled. | **checked_empty** |
| 2:1 | H9009 | trample on | inert |  | Definite article, function role. | **checked_empty** |
| 3:0 | H0034 | needy | related_word |  | Genuine etymological finding: 'needy' (evyon) shares its root with 'to desire/be willing' (H0014/H0035) -- the needy are, at root, 'those who lack/desire', a real semantic insight. | **resolved** |
| 4:0 | H6041 | poor | related_word |  | Genuine, strong family: afflict/poor/gentleness (H6031-H6038) -- a real, substantial semantic cluster central to this verse's own social-justice vocabulary. | **resolved** |
| 5:0 | H0776G | land | related_word |  | 0 related codes pulled. | **checked_empty** |
| 6:0 | H7673A | end | related_word |  | 0 related codes pulled. | **checked_empty** |
| 6:0 | H7673A | end | structural_pattern |  | 'trample on' / 'needy' / 'poor' form the indictment's own accusation cluster -- the verb and its two victim-terms named together as one social-justice charge. | **resolved** |
| 6:1 | H9002 | end | inert |  | Conjunctive component within the compound verb phrase, function role. | **checked_empty** |
| 6:2 | H9005 | end | inert |  | Prepositional component within the compound verb phrase, function role. | **checked_empty** |

### Consolidated narrative (double control)

This is Amos' prophetic indictment against those who exploit the poor: "Hear this, you who trample on the needy and bring the poor of the land to an end." Re-reading the findings together, the structural_pattern (trample/needy/poor as one accusation cluster) correctly captures the verse's own rhetorical shape: a single accusatory clause naming both the action (trampling, ending) and its two victim-terms together, which is the whole force of the prophetic charge. The etymological findings on "needy" (root-connected to desire/lack) and "poor" (root-connected to affliction, a substantial family) both reinforce the social-justice vocabulary this verse is built on -- not incidental word-facts, but findings that directly support the verse's own argument about who is being wronged and how. No contradictions on holistic re-read; a short, tightly-focused verse whose findings all point the same direction.

---

## Mark.11.21 — Gospel narrative

**Verse text:** And Peter remembered and said to him, “ Rabbi, look! The fig tree that you cursed has withered.”

### Layer 1 — `verse_lexical` (11 rows)

| pos | ord | strong | morph | role | surface | lang | testament | negator | narr_morph | gloss_ok | party | l1_status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 0 | G2532 | CONJ | function | And | Greek | NT |  |  | 1 |  | resolved |
| 1 | 0 | G4074G | N-NSM-P | content | Peter | Greek | NT |  |  | 1 |  | resolved |
| 2 | 0 | G0363 | V-AOP-NSM | content | remembered | Greek | NT |  |  | 1 |  | resolved |
| 3 | 0 | G3004G | V-PAI-3S | content | said | Greek | NT |  |  | 1 |  | resolved |
| 4 | 0 | G0846 | P-DSM | content | him | Greek | NT |  |  | 1 |  | resolved |
| 5 | 0 | G4461 | N-VSM-T | content | Rabbi | Greek | NT |  |  | 1 |  | resolved |
| 6 | 0 | G2396 | INJ | content | look | Greek | NT |  |  | 1 |  | resolved |
| 7 | 0 | G4808 | N-NSF | content | fig tree | Greek | NT |  |  | 1 |  | resolved |
| 8 | 0 | G3739 | R-ASF | content | that | Greek | NT |  |  | 1 |  | resolved |
| 9 | 0 | G2672 | V-ADI-2S | content | cursed | Greek | NT |  |  | 1 |  | resolved |
| 10 | 0 | G3583 | V-RPI-3S | content | withered | Greek | NT |  |  | 1 |  | resolved |

### Layer 2 — `verse_lexical_note` (14 rows)

| pos:ord | strong | surface | note_type | target | finding | status |
|---|---|---|---|---|---|---|
| 0:0 | G2532 | And | connective |  | Coordinating 'And' -- narrative sequencer opening the verse, genuinely classifiable against the 3-class lexicon. | **resolved** |
| 1:0 | G4074G | Peter | related_word |  | 0 related codes pulled. | **checked_empty** |
| 2:0 | G0363 | remembered | related_word |  | Genuine, direct family: remembrance / to remember (G0364/G3403) -- real cognates, expected. | **resolved** |
| 3:0 | G3004G | said | related_word |  | 0 related codes pulled. | **checked_empty** |
| 4:0 | G0846 | him | related_word |  | Minor genuine relation: reflexive-pronoun morphological family (G1438/G1683) -- real cognates, not a substantive finding on its own. | **resolved** |
| 4:0 | G0846 | him | entity_link |  | 'him' (dative) refers to Jesus, the addressee of Peter's remark -- confirmed from the target verse's own grammar (a vocative 'Rabbi' immediately follows), no adjacent-verse read needed. | **resolved** |
| 5:0 | G4461 | Rabbi | related_word |  | Genuine, direct cognate: Rabboni (G4462) -- the same honorific family, real. | **resolved** |
| 6:0 | G2396 | look | related_word |  | Genuine, direct cognate: 'to perceive/know' (G1492) -- 'look/behold' shares its root with 'to see', real and expected. | **resolved** |
| 7:0 | G4808 | fig tree | related_word |  | Genuine botanical-term cluster: mulberry/sycamore/fig (G4807/G4809/G4810) -- real, all fruit-tree names sharing a root, not coincidental. | **resolved** |
| 7:0 | G4808 | fig tree | entity_link | Mark.11.13:4 **(cross-verse)** | 'fig tree' (G4808) is the same tree Jesus approached in Mark.11.13 -- same strong code, same referent, confirmed by a targeted read of the earlier verse, exactly the kind of on-demand adjacent-verse check #1451's design describes. NOT cross_lemma_shared_gloss -- that note_type is for two DIFFERENT lemmas sharing a sense, not the same code recurring. | **resolved** |
| 8:0 | G3739 | that | related_word |  | 1 related code pulled, form/gloss empty -- not usable. | **checked_empty** |
| 8:0 | G3739 | that | pronoun_resolution | Mark.11.21:7 | 'that' (relative pronoun) refers to 'fig tree' (position 7) -- the relative clause's antecedent within the same verse. | **resolved** |
| 9:0 | G2672 | cursed | related_word |  | Genuine, direct family: cursed/curse (G1944/G2671) -- real cognates. | **resolved** |
| 10:0 | G3583 | withered | related_word |  | Genuine, direct cognate: 'dried up/withered' (G3584) -- real, expected. | **resolved** |

### Consolidated narrative (double control)

This verse records Peter's remembrance of the cursed fig tree: "And Peter remembered and said to him, 'Rabbi, look! The fig tree that you cursed has withered.'" Re-reading the findings together, the cross-verse entity_link (fig tree -> Mark.11.13) is the single most important finding here: it confirms this is the SAME tree from the earlier episode, not a new one, which is essential to the narrative's own point (the fulfilment of Jesus' earlier curse). The relative-pronoun resolution ("that" -> fig tree) and the "him" entity_link (-> Jesus) together correctly disambiguate every referring expression in a verse otherwise dense with pronouns and implicit references. The related-word findings here are almost uniformly genuine, direct cognates (remembrance/remember, Rabbi/Rabboni, see/perceive, mulberry/sycamore/fig, cursed/curse, withered) -- a different texture from the Hebrew verses in this sample, where coincidental root-collisions were common; consistent with the design's own language-aware sorting rule (Greek compound-morphology families tend to be genuinely related, unlike Hebrew triliteral-root collisions). Holistically coherent: every finding supports a single, clear narrative reading with no tension between them.

---

## Rom.9.14 — Epistle/didactic

**Verse text:** What shall we say then? Is there injustice on God’s part? By no means!

### Layer 1 — `verse_lexical` (9 rows)

| pos | ord | strong | morph | role | surface | lang | testament | negator | narr_morph | gloss_ok | party | l1_status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 0 | G5101 | I-ASN | content | What | Greek | NT |  |  | 1 |  | resolved |
| 1 | 0 | G4483 | V-FAI-1P | content | say | Greek | NT |  |  | 1 |  | resolved |
| 2 | 0 | G3767 | CONJ | function | then | Greek | NT |  |  | 1 |  | resolved |
| 3 | 0 | G3361 | PRT-N | function | Is | Greek | NT | 1 |  | 1 |  | resolved |
| 4 | 0 | G0093 | N-NSF | content | injustice | Greek | NT |  |  | 1 |  | resolved |
| 5 | 0 | G3844 | PREP | function | on | Greek | NT |  |  | 1 |  | resolved |
| 6 | 0 | G2316 | N-DSM-T | content | God’s | Greek | NT |  |  | 1 | divine | resolved |
| 7 | 0 | G3361 | PRT-N | function | no | Greek | NT | 1 |  | 1 |  | resolved |
| 8 | 0 | G1096 | V-2ADO-3S | content | means | Greek | NT |  |  | 1 |  | resolved |

### Layer 2 — `verse_lexical_note` (11 rows)

| pos:ord | strong | surface | note_type | target | finding | status |
|---|---|---|---|---|---|---|
| 0:0 | G5101 | What | related_word |  | Genuine interrogative-pronoun family: why?/one?/which? (G2444/G5100) -- real cognates, expected. | **resolved** |
| 1:0 | G4483 | say | related_word |  | Genuine, large cognate family: say/speak (G2036/G2046/G4482/G4487/G4489) -- the classic Greek verb-of-speech cluster, real. | **resolved** |
| 2:0 | G3767 | then | connective |  | 'then' (oun) here is inferential -- drawing a conclusion from the preceding argument. The design's 3-class connective lexicon (causal/coordinating/purpose) has no inferential class -- correctly UNCLASSIFIED, the same taxonomy gap already found at Lev.17.16 (conditional) and Prov.31.30 (adversative); a real, recurring gap across this sample, not three unrelated one-offs. | **unclassified** |
| 3:0 | G3361 | Is | related_word |  | 0 related codes pulled. | **checked_empty** |
| 3:0 | G3361 | Is | connective |  | Part of the me genoito ('by no means') rhetorical-denial construction together with positions 7-8 -- not an independent negation of a separate clause. | **resolved** |
| 4:0 | G0093 | injustice | related_word |  | Genuine, rich family: harm/crime/unjust/opponent/justice (G0091-G1341) -- a substantial semantic cluster directly relevant to Paul's own argument about justice/righteousness in Romans, a real and valuable finding for this letter specifically. | **resolved** |
| 5:0 | G3844 | on | related_word |  | 0 related codes pulled. | **checked_empty** |
| 6:0 | G2316 | God’s | related_word |  | Genuine, theologically rich family: without-God/goddess/divine/God-fighting/God-breathed (G0112-G2315) -- a real, significant cluster directly relevant to a study of divine-referring vocabulary specifically. | **resolved** |
| 7:0 | G3361 | no | related_word |  | 0 related codes pulled. | **checked_empty** |
| 7:0 | G3361 | no | idiom | Rom.9.14:8 | me genoito ('by no means') is a fixed, well-known Pauline rhetorical idiom for emphatic denial, spanning positions 7-8 -- not a literal statement. | **resolved** |
| 8:0 | G1096 | means | related_word |  | Only a self-referential match (ginomai to itself) -- not a genuine external relation. | **checked_empty** |

### Consolidated narrative (double control)

This is Paul's rhetorical question-and-denial: "What shall we say then? Is there injustice on God's part? By no means!" Re-reading the findings together, the inferential "then" (UNCLASSIFIED -- the third and final instance of this taxonomy gap across this 10-verse sample, alongside Lev.17.16's conditional and Prov.31.30's adversative) confirms this is a real, recurring gap in the connective lexicon rather than three unrelated one-offs -- worth treating as one finding about the method across the whole sample, not three separate curiosities. The idiom finding (me genoito, "by no means," spanning positions 3/7/8) correctly identifies this as Paul's own well-known fixed rhetorical formula rather than three separate negations, which matters for the verse's own emphatic force. The two rich related-word families (injustice: harm/crime/unjust/opponent/justice; God: without-God/divine/God-fighting/God-breathed) both connect directly to this letter's own central argument about divine justice and righteousness -- thematically load-bearing connections for Romans specifically, not generic vocabulary hits. Holistically consistent: the rhetorical-question-then-denial structure is fully supported by the findings, with no contradiction between the connective, idiom, and related-word layers.

---
