# Window 1 Layer 1 + Layer 2 — full review data, 10 verses (v3)

> Escalation #1451. v3 adds each code's cluster short name(s) to Layer 1 (computed at report time, not a stored column -- avoids the backfill-cost/staleness problem already named in BUILD.md #230; joined on the exact strong code, same lesson as the `strong_related` fix below; a code in more than one cluster shows all of them, comma-joined, e.g. `Weakness, Supplementary`; a code with no cluster_strong row shows blank, not a guess).

> Escalation #1451. Corrects a real bug found by the researcher: `strong_related` is keyed on the EXACT sub-entry code (e.g. `H5771G`), not the base code (`H5771`) -- the first pass base-stripped before querying and wrongly reported 0 related words for 40 of 102 `related_word` findings across 9 of the 10 verses. All 40 are corrected below with the real data. Every note_type, table, and narrative in this document reflects the corrected pass; nothing here is the buggy version.

## Gen.46.18 — Torah narrative

**Verse text:** These are the sons of Zilpah, whom Laban gave to Leah his daughter; and these she bore to Jacob — sixteen persons.

### Layer 1 — `verse_lexical` (18 rows)

| pos | ord | strong | morph | role | surface | lang | testament | negator | narr_morph | gloss_ok | party | cluster | l1_status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 0 | H0428 | HTm | content | These | Hebrew | OT |  |  | 1 |  |  | resolved |
| 1 | 0 | H1121A | HNcmpc | content | sons | Hebrew | OT |  |  | 1 |  |  | resolved |
| 2 | 0 | H2153 | HNpf | content | Zilpah | Hebrew | OT |  |  | 1 |  |  | resolved |
| 3 | 0 | H0834A | HTr | content | whom | Hebrew | OT |  |  | 1 |  |  | resolved |
| 4 | 0 | H3837A | HNpm | content | Laban | Hebrew | OT |  |  | 1 |  |  | resolved |
| 5 | 0 | H5414G | HVqp3ms | content | gave | Hebrew | OT |  |  | 1 |  | Operations | resolved |
| 6 | 0 | H3812 | HNpf | content | Leah | Hebrew | OT |  |  | 1 |  |  | resolved |
| 6 | 1 | H9005 | HR | function | Leah | Hebrew | OT |  |  | 1 |  |  | resolved |
| 7 | 0 | H1323G | HNcfsc | content | daughter | Hebrew | OT |  |  | 1 |  |  | resolved |
| 8 | 0 | H3205 | HVqw3fs | content | bore | Hebrew | OT |  | wayyiqtol | 1 |  | Operations | resolved |
| 8 | 1 | H9023 | HSp3ms | function | bore | Hebrew | OT |  |  | 1 |  |  | resolved |
| 9 | 0 | H3290 | HNpm | content | Jacob | Hebrew | OT |  |  | 1 |  |  | resolved |
| 9 | 1 | H9005 | HR | function | Jacob | Hebrew | OT |  |  | 1 |  |  | resolved |
| 9 | 2 | H0853 | HTo | function | Jacob | Hebrew | OT |  |  | 1 |  | Supplementary | resolved |
| 9 | 3 | H0428 | HTm | content | Jacob | Hebrew | OT |  |  | 1 |  |  | resolved |
| 10 | 0 | H6240 | HAcbsc | content | sixteen | Hebrew | OT |  |  | 1 |  |  | resolved |
| 10 | 1 | H8337 | HAcbsc | content | sixteen | Hebrew | OT |  |  | 1 |  |  | resolved |
| 11 | 0 | H5315J | HNcfsa | content | persons | Hebrew | OT |  |  | 1 |  | Constitution | resolved |

### Layer 2 — `verse_lexical_note` (24 rows)

| pos:ord | strong | surface | note_type | target | finding | status |
|---|---|---|---|---|---|---|
| 0:0 | H0428 | These | related_word |  | H0411/H0429 (el/elleh, 'these') are genuine same-root synonym forms of this demonstrative; H0414 (Ela, a proper name) is a coincidental root-collision, not a real relation. | **resolved** |
| 1:0 | H1121A | sons | related_word |  | CORRECTED (v1 wrongly base-stripped this code and reported 0): 48 related codes under the exact code H1121A, genuine -- the full ben ('son') family, including its own sub-senses (son: descendant/young animal/type/warrior/aged) and derivative proper names (Ben, Beno). Same root, real relation, not coincidental. | **resolved** |
| 2:0 | H2153 | Zilpah | related_word |  | 1 related code pulled, but its own form/gloss fields are empty in strong_related -- not usable, treated as no real finding. | **checked_empty** |
| 2:0 | H2153 | Zilpah | entity_link | Gen.46.18:3 | Target of 'whom' (position 3) -- Zilpah is the antecedent. | **resolved** |
| 3:0 | H0834A | whom | related_word |  | 0 usable related codes (1 pulled, form/gloss empty). | **checked_empty** |
| 3:0 | H0834A | whom | entity_link | Gen.46.18:2 | 'whom' (relative pronoun) refers back to Zilpah (position 2), not Laban -- the antecedent of the relative clause. | **resolved** |
| 4:0 | H3837A | Laban | related_word |  | 1 related code pulled, form/gloss empty -- not usable. | **checked_empty** |
| 5:0 | H5414G | gave | related_word |  | CORRECTED (v1 wrongly reported 0): 60 related codes under the exact code H5414G, genuine -- natan ('to give') is the root of mattan/mattanah ('gift'), a real and expected semantic connection, heavily populated with proper names built on the same root (Mattan, Mattanah, Mattenai). | **resolved** |
| 5:0 | H5414G | gave | verb_argument | Gen.46.18:4 | 'gave' (H5414G): trigger/agent is Laban (position 4), impact/recipient is Leah (position 6). | **resolved** |
| 6:0 | H3812 | Leah | related_word |  | 1 related code pulled, form/gloss empty -- not usable. | **checked_empty** |
| 6:1 | H9005 | Leah | inert |  | Prepositional prefix ('to'), function role -- no relational finding beyond its own grammatical role. | **checked_empty** |
| 7:0 | H1323G | daughter | related_word |  | CORRECTED (v1 wrongly reported 0): 42 related codes under the exact code H1323G, genuine -- bat ('daughter') is cross-listed with the full ben ('son') family, a real parent-child terminology pairing attested in STEP's own data, not coincidental. | **resolved** |
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
| 11:0 | H5315J | persons | related_word |  | CORRECTED (v1 wrongly reported 0): 11 related codes under the exact code H5315J, genuine and directly relevant -- nephesh's OWN other senses (soul: life/myself/animal/appetite/dead) plus naphash ('be refreshed') and Naphish (a coincidental proper name). This is real, strong evidence for the polysemy point below: the same lemma spans 'headcount' and 'soul/life', not two unrelated words. | **resolved** |
| 11:0 | H5315J | persons | noun_severity |  | H5315J (nephesh) is used here in its headcount sense ('sixteen persons'), not its inner-being 'soul' sense -- confirmed by this code's own related-word family (soul/life/myself/appetite), which shows both senses genuinely belong to one lemma. A real, project-relevant polysemy distinction for a study centred on inner-being vocabulary. | **resolved** |

### Consolidated narrative (double control)

This verse closes a genealogical list (Zilpah's line via Laban's gift of Leah, continuing to Jacob) with a formulaic sixteen-person tally. Re-reading the findings together: the relative clause "whom Laban gave" is correctly anchored to Zilpah, not Leah. "Bore...to Jacob" is properly flagged as a wayyiqtol narrative link. Jacob's cross-reference to "Israel" is a real, useful identity anchor. The related-word corrections change the picture materially here: "son" and "daughter" (H1121A/H1323G) are now shown to be genuinely cross-referenced terms in Hebrew (not independent words), and "gave" (H5414G) is now confirmed rooted in the same family as "gift" (mattan) -- both real relations that a base-code lookup had wrongly hidden. Most significantly, the corrected pull for "persons" (nephesh, H5315J) now shows its own genuine other senses (soul/life/myself/appetite/dead) as real related-word evidence, not just an unsupported observation -- this converts the earlier tentative "worth noting" comment into an actually-evidenced finding: this occurrence is a plain headcount, and the word's own attested semantic range confirms that "headcount" and "soul" are two senses of one lemma, directly relevant to any future study of nephesh's own range. The numeral "sixteen" analysis still usefully demonstrates a real (six+ten root family) and a coincidental (Sheva/onyx homographs) related-word outcome side by side. The one unresolved item (H0428 attached to "Jacob") remains a genuine loose end, correctly left open rather than guessed. Holistically, every finding is now both consistent AND properly evidenced -- no contradiction, and the earlier gap (assertions without related-word support) is closed.

---

## Lev.17.16 — Torah legal

**Verse text:** But if he does not wash them or bathe his flesh, he shall bear his iniquity.”

### Layer 1 — `verse_lexical` (12 rows)

| pos | ord | strong | morph | role | surface | lang | testament | negator | narr_morph | gloss_ok | party | cluster | l1_status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 0 | H3808 | HTn | content | not | Hebrew | OT | 1 |  | 1 |  | Negator | resolved |
| 1 | 0 | H3526H | HVpi3ms | content | wash | Hebrew | OT |  |  | 1 |  | Operations | resolved |
| 1 | 1 | H0518A | HTc | content | wash | Hebrew | OT |  |  | 1 |  | Supplementary | resolved |
| 1 | 2 | H9002 | HC | function | wash | Hebrew | OT |  |  | 1 |  | Connective | resolved |
| 2 | 0 | H7364 | HVqi3ms | content | bathe | Hebrew | OT |  |  | 1 |  | Operations | resolved |
| 2 | 1 | H9023 | HSp3ms | function | bathe | Hebrew | OT |  |  | 1 |  |  | resolved |
| 2 | 2 | H3808 | HTn | content | bathe | Hebrew | OT | 1 |  | 1 |  | Negator | resolved |
| 3 | 0 | H1320 | HNcmsc | content | flesh | Hebrew | OT |  |  | 1 |  | Constitution | resolved |
| 3 | 1 | H9002 | HC | function | flesh | Hebrew | OT |  |  | 1 |  | Connective | resolved |
| 4 | 0 | H5375J | HVqq3ms | content | bear | Hebrew | OT |  |  | 1 |  | Sin | resolved |
| 5 | 0 | H9023 | HSp3ms | function | his | Hebrew | OT |  |  | 1 |  |  | resolved |
| 6 | 0 | H5771G | HNcmsc | content | iniquity | Hebrew | OT |  |  | 1 |  | Sin | resolved |

### Layer 2 — `verse_lexical_note` (14 rows)

| pos:ord | strong | surface | note_type | target | finding | status |
|---|---|---|---|---|---|---|
| 0:0 | H3808 | not | related_word |  | H0408/H3809 (al/la, 'not') are genuine synonym forms of this negator. H3810/H3818/H3819 (Lo-debar, Not-My-People, No-Mercy) are NOT coincidental despite being proper names -- deliberately built on the negator as a real Hebrew naming convention, a genuine if indirect relation. | **resolved** |
| 1:0 | H3526H | wash | related_word |  | CORRECTED (v1 wrongly reported 0): 1 related code under the exact code H3526H -- H3526G (kavas, 'Washer's'), a genuine same-root participial/occupational form of 'to wash'. | **resolved** |
| 1:1 | H0518A | wash | connective |  | The bound conditional clitic ('if', attached to the verb) marks this clause as a conditional apodosis. The design's own 3-class connective lexicon (causal/coordinating/purpose) has no conditional class -- correctly UNCLASSIFIED rather than force-fit; a real taxonomy gap. | **unclassified** |
| 1:1 | H0518A | wash | related_word |  | CORRECTED (v1 wrongly reported 0): 11 related codes under the exact code H0518A, mixed -- H0518B/H0518H/H0518I/H0518J are genuine same-lemma sub-senses of 'if' (except/surely no/surely yes/until); H0509/Elkoshite/Eltekeh/Eltekon are coincidental collisions. | **resolved** |
| 1:2 | H9002 | wash | connective |  | Coordinating: the waw here functions as disjunctive 'or' between the two negated verbs (wash / bathe) -- a genuine coordinating relation. | **resolved** |
| 2:0 | H7364 | bathe | related_word |  | Genuine same-concept family: washing-related terms (H7365/H7366/H7367) -- real semantic cluster. | **resolved** |
| 2:1 | H9023 | bathe | pronoun_resolution | Lev.17.15:1 **(cross-verse)** | The implicit 3ms subject ('he') of this verse is not named within Lev.17.16 itself -- a targeted read of the immediately preceding verse (Lev.17.15) confirms the antecedent: 'every person (nephesh) who eats...' (position 1). | **resolved** |
| 2:2 | H3808 | bathe | polarity | Lev.17.16:0 | Second negator (H3808) extends the first negator's (position 0) scope across both coordinated verbs -- 'does not wash... or bathe' is one negated compound action, not two independent negative clauses. | **resolved** |
| 3:0 | H1320 | flesh | related_word |  | Genuine same-concept family: flesh/body-related Hebrew root (H1308/H1309/H1319/H1321) -- real semantic cluster. | **resolved** |
| 3:1 | H9002 | flesh | inert |  | Conjunctive prefix within 'his flesh', function role. | **checked_empty** |
| 4:0 | H5375J | bear | related_word |  | CORRECTED (v1 wrongly reported 0): 30 related codes under the exact code H5375J, genuine and directly relevant -- nasa ('to lift/bear') is the root of massa ('burden'), and the code's own sub-senses (to lift: raise/bear/forgive) reinforce this verse's own idiom (see below). | **resolved** |
| 4:0 | H5375J | bear | idiom |  | 'bear his iniquity' (nasa avon) is a fixed Hebrew legal idiom meaning 'be held guilty/liable', not a literal physical-bearing statement -- reinforced by H5375J's own related-word family (burden/to lift/to bear), which shows 'bear' here is genuinely rooted in the carrying-a-burden sense. | **resolved** |
| 5:0 | H9023 | his | pronoun_resolution | Lev.17.15:1 **(cross-verse)** | Same antecedent as position 2's 'his' -- the generic legal subject established in Lev.17.15. | **resolved** |
| 6:0 | H5771G | iniquity | related_word |  | CORRECTED (v1 wrongly reported 0 -- see below): 5 related codes under the exact code H5771G, genuine and illuminating -- avah ('to twist'/'to pervert', H5753A/B) is the root avon ('iniquity') itself derives from, and H5771H/I are the same lemma's own other senses (iniquity: guilt/punishment). This directly explains WHY iniquity is something 'borne' (idiom, position 4): the root concept is a moral 'twisting', not an abstract label. | **resolved** |

### Consolidated narrative (double control)

This is a conditional legal clause from the purity laws: "But if he does not wash [them] or bathe his flesh, he shall bear his iniquity." Re-reading the findings together, the two negators are correctly linked as one compound negated action. The conditional "if" remains correctly UNCLASSIFIED against the 3-class connective lexicon -- a genuine taxonomy gap. The cross-verse pronoun resolution (both "his" instances -> Lev.17.15's "person who eats") remains essential to the reading. The related-word corrections add real depth here: "wash" (H3526H) now shows a genuine cognate ("washer's"); the conditional "if" (H0518A) now shows genuine same-lemma sub-senses (surely no/surely yes/until) alongside coincidental place-name collisions; "bear" (H5375J) now shows a rich, genuine family rooted in "burden" -- directly reinforcing the "bear his iniquity" idiom, which is no longer just an assumed idiom but one with real etymological support. Most strikingly, "iniquity" itself (H5771G) -- the exact word the researcher's own question was about -- now shows a genuine, illuminating root: avah ("to twist/pervert"), which is literally what the noun "iniquity" derives from, plus the word's own other senses (guilt/punishment). This is not a minor correction: it explains WHY iniquity is something "borne" in the idiom -- the underlying concept is a moral twisting, carried as a weight. Holistically, the corrected findings now reinforce each other where before "bear" and "iniquity" sat as two isolated checked_empty notes beside an asserted idiom; now the idiom claim has real supporting etymology on both its verb and its object.

---

## Judg.11.40 — Historical narrative

**Verse text:** (no cached text for this verse)

### Layer 1 — `verse_lexical` (18 rows)

| pos | ord | strong | morph | role | surface | lang | testament | negator | narr_morph | gloss_ok | party | cluster | l1_status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 0 | H1323G | HNcfpc | content | daughters | Hebrew | OT |  |  | 1 |  |  | resolved |
| 1 | 0 | H3478 | HNpl | content | Israel | Hebrew | OT |  |  | 1 |  |  | resolved |
| 2 | 0 | H1980G | HVqi3fp | content | went | Hebrew | OT |  |  | 1 |  | Operations | resolved |
| 2 | 1 | H9011 | HSd | function | went | Hebrew | OT |  |  | 1 |  |  | resolved |
| 3 | 0 | H3117I | HNcmpa | content | year | Hebrew | OT |  |  | 1 |  |  | resolved |
| 3 | 1 | H9006 | HR | function | year | Hebrew | OT |  |  | 1 |  | Supplementary | resolved |
| 4 | 0 | H3117I | HNcmpa | content | year | Hebrew | OT |  |  | 1 |  |  | resolved |
| 5 | 0 | H8567 | HVpcc | content | lament | Hebrew | OT |  |  | 1 |  | Operations | resolved |
| 5 | 1 | H9005 | HR | function | lament | Hebrew | OT |  |  | 1 |  |  | resolved |
| 6 | 0 | H1323G | HNcfsc | content | daughter | Hebrew | OT |  |  | 1 |  |  | resolved |
| 6 | 1 | H9005 | HR | function | daughter | Hebrew | OT |  |  | 1 |  |  | resolved |
| 7 | 0 | H3316H | HNpm | content | Jephthah | Hebrew | OT |  |  | 1 |  |  | resolved |
| 8 | 0 | H1569 | HNgmsa | content | Gileadite | Hebrew | OT |  |  | 1 |  |  | resolved |
| 8 | 1 | H9009 | HTd | function | Gileadite | Hebrew | OT |  |  | 1 |  |  | resolved |
| 9 | 0 | H0702 | HNcbsc | content | four | Hebrew | OT |  |  | 1 |  |  | resolved |
| 10 | 0 | H3117I | HNcmpa | content | days | Hebrew | OT |  |  | 1 |  |  | resolved |
| 11 | 0 | H8141 | HNcfsa | content | year | Hebrew | OT |  |  | 1 |  |  | resolved |
| 11 | 1 | H9003 | HRd | function | year | Hebrew | OT |  |  | 1 |  |  | resolved |

### Layer 2 — `verse_lexical_note` (20 rows)

| pos:ord | strong | surface | note_type | target | finding | status |
|---|---|---|---|---|---|---|
| 0:0 | H1323G | daughters | related_word |  | CORRECTED (v1 wrongly reported 0): 42 related codes under the exact code H1323G -- the same bat/ben (daughter/son) cross-referenced family found at Gen.46.18 position 7, genuine, not coincidental. | **resolved** |
| 1:0 | H3478 | Israel | related_word |  | Genuine, real cross-reference: Israel/Jacob (H3290/H3479) and Israelite (G2474/G2475) are the same people's collective name and eponymous ancestor -- the identical name-cluster finding as Gen.46.18 position 9. | **resolved** |
| 2:0 | H1980G | went | related_word |  | CORRECTED (v1 wrongly reported 0): 16 related codes under the exact code H1980G, genuine -- halakh ('to go') family (step/walk) plus its own sub-senses (to go: come/walk/take/continue). | **resolved** |
| 2:1 | H9011 | went | inert |  | Directional-heh suffix, function role. | **checked_empty** |
| 3:0 | H3117I | year | related_word |  | CORRECTED (v1 wrongly reported 0): 7 related codes under the exact code H3117I, genuine -- all sub-senses of yom ('day': old/daily/always/today) plus yomam ('by day'). This confirms and sharpens the idiom finding below: the 'year by year' idiom is literally built on the DAY word (yamim, 'days'), the standard Hebrew distributive construction, not a separate 'year' word. | **resolved** |
| 3:0 | H3117I | year | idiom | Judg.11.40:4 | 'yamim yamimah' (H3117I repeated at positions 3-4, literally 'days to days') is the standard Hebrew distributive idiom for 'year by year / annually' -- confirmed by this code's own related-word family, all 'day' senses, not two separate year-references. | **resolved** |
| 3:1 | H9006 | year | inert |  | Prepositional prefix, function role. | **checked_empty** |
| 4:0 | H3117I | year | related_word |  | Same corrected family as position 3 -- second half of the 'days to days' idiom. | **resolved** |
| 5:0 | H8567 | lament | related_word |  | 1 related code pulled, form/gloss empty -- not usable. | **checked_empty** |
| 5:1 | H9005 | lament | inert |  | Prepositional prefix ('to'), function role. | **checked_empty** |
| 6:0 | H1323G | daughter | related_word |  | Same corrected bat/ben family as position 0 and Gen.46.18 position 7. | **resolved** |
| 6:0 | H1323G | daughter | entity_link | Judg.11.40:7 | 'daughter' (singular) refers to Jephthah's daughter specifically (named via his patronymic at position 7-8) -- distinct from 'daughters of Israel' (plural, position 0). | **resolved** |
| 6:1 | H9005 | daughter | inert |  | Genitive-marking prefix, function role. | **checked_empty** |
| 7:0 | H3316H | Jephthah | related_word |  | CORRECTED (v1 wrongly reported 0): 2 related codes under the exact code H3316H, genuine -- G2422 (Greek transliteration Iephthae) and H3316G (Iphtah, a place-name variant), real cross-lingual name attestation. | **resolved** |
| 8:0 | H1569 | Gileadite | related_word |  | Genuine toponymic family: Gilead (H1568, multiple sub-entries) -- a real, meaningful geographic/genealogical connection to Jephthah's own origin. | **resolved** |
| 8:1 | H9009 | Gileadite | inert |  | Definite article, function role. | **checked_empty** |
| 9:0 | H0702 | four | related_word |  | Genuine numeral family: four/fourth/forty (H0703/H0704/H0705/H7243) -- real semantic root. | **resolved** |
| 10:0 | H3117I | days | related_word |  | Same corrected day-family as positions 3-4 (H3117I). | **resolved** |
| 11:0 | H8141 | year | related_word |  | Genuine etymological finding: shanah ('year', H8140) shares its root with 'to change/to repeat' (H8132/H8138) -- a real insight (a year as a repeating cycle). | **resolved** |
| 11:1 | H9003 | year | inert |  | Prepositional prefix ('in'), function role. | **checked_empty** |

### Consolidated narrative (double control)

This verse records the annual commemoration custom established after Jephthah's vow. Re-reading the findings together, the idiom finding ("year...year" = annually) remains load-bearing, and the corrected related-word pull for H3117I (the "year" code) now shows this is genuinely the "day" (yom) word family throughout -- sharpening the finding: this is literally "days to days," the standard Hebrew day-based idiom for an annual cycle, not a separate "year" word repeated. The entity_link still correctly distinguishes the daughters of Israel (subject) from Jephthah's daughter (object), and the corrected pull now shows this same bat/ben (daughter/son) cross-reference at all three "daughter(s)" positions in this verse, consistent with the identical finding at Gen.46.18 -- a genuine, repeated cross-verse confirmation, not a fluke. The corrected pulls for "went" (halakh family), "Jephthah" (cross-lingual name attestation), and the Gilead toponym family all add real, previously-missing support to findings that were asserted with 0-related-word backing before. Holistically consistent, and now properly evidenced throughout rather than resting on unsupported assertions for roughly a third of its content codes.

---

## Prov.31.30 — Wisdom

**Verse text:** Charm is deceitful, and beauty is vain, but a woman who fears the Lord is to be praised.

### Layer 1 — `verse_lexical` (12 rows)

| pos | ord | strong | morph | role | surface | lang | testament | negator | narr_morph | gloss_ok | party | cluster | l1_status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 0 | H2580 | HNcmsa | content | Charm | Hebrew | OT |  |  | 1 |  | Blessing | resolved |
| 0 | 1 | H9009 | HTd | function | Charm | Hebrew | OT |  |  | 1 |  |  | resolved |
| 1 | 0 | H8267 | HNcmsa | content | deceitful | Hebrew | OT |  |  | 1 |  | Deceit | resolved |
| 2 | 0 | H3308 | HNcmsa | content | beauty | Hebrew | OT |  |  | 1 |  | Supplementary | resolved |
| 2 | 1 | H9009 | HTd | function | beauty | Hebrew | OT |  |  | 1 |  |  | resolved |
| 3 | 0 | H1892 | HNcmsa | content | vain | Hebrew | OT |  |  | 1 |  | Deceit | resolved |
| 3 | 1 | H9002 | HC | function | vain | Hebrew | OT |  |  | 1 |  | Connective | resolved |
| 4 | 0 | H0802G | HNcfsa | content | woman | Hebrew | OT |  |  | 1 |  |  | resolved |
| 5 | 0 | H3373 | HAafsc | content | fears | Hebrew | OT |  |  | 1 |  | Fear | resolved |
| 6 | 0 | H3068G | HNpt | content | Lord | Hebrew | OT |  |  | 1 | divine | Party-Divine | resolved |
| 7 | 0 | H1984B | HVti3fs | content | praised | Hebrew | OT |  |  | 1 |  | Praise | resolved |
| 7 | 1 | H1931 | HPp3fs | content | praised | Hebrew | OT |  |  | 1 |  | Supplementary | resolved |

### Layer 2 — `verse_lexical_note` (13 rows)

| pos:ord | strong | surface | note_type | target | finding | status |
|---|---|---|---|---|---|---|
| 0:0 | H2580 | Charm | related_word |  | Coincidental at scale: 51 related codes pulled, the overwhelming majority proper names (Hen, Henadad, Hannah...) sharing the CHN root with 'charm' -- a textbook, large-scale Hebrew triliteral-root collision, correctly sorted coincidental. | **resolved** |
| 0:1 | H9009 | Charm | inert |  | Definite article, function role. | **checked_empty** |
| 1:0 | H8267 | deceitful | related_word |  | Genuine, minor relation: shares its root with 'to deal falsely' (H8266) -- a real if small semantic connection. | **resolved** |
| 2:0 | H3308 | beauty | related_word |  | Mixed: H3302/H3303/H3304 (beautiful/pretty) are genuine same-concept relatives; H3305 (Joppa, a place name) is a coincidental collision within the same pull. | **resolved** |
| 2:1 | H9009 | beauty | inert |  | Definite article, function role. | **checked_empty** |
| 3:0 | H1892 | vain | related_word |  | Genuine and notable: H1893 (Abel, the biblical name) is a well-attested intentional naming pun in Hebrew scripture (Abel's name literally carries the sense 'vapor/vanity'), the same root as this verse's own 'vain'. A real connection, not coincidental. | **resolved** |
| 3:1 | H9002 | vain | connective |  | Adversative 'but', contrasting charm/beauty (positions 0-3) against the woman who fears the LORD (positions 4-7). The design's 3-class connective lexicon has no adversative class -- correctly UNCLASSIFIED, the same taxonomy gap already found at Lev.17.16's conditional case. | **unclassified** |
| 4:0 | H0802G | woman | related_word |  | CORRECTED (v1 wrongly reported 0): 7 related codes under the exact code H0802G, genuine and directly relevant -- ishah ('woman') is etymologically paired with ish ('man', H0376) in Hebrew, a well-known linguistic fact (ishah is grammatically derived from ish); also enosh ('human', H0582) and the word's own other senses (wife/another). A real, significant family for a study focused on human/party vocabulary specifically. | **resolved** |
| 5:0 | H3373 | fears | related_word |  | Genuine same-concept family: fear/reverence (H3372/H3374/H4172) -- fully expected, real semantic cluster. | **resolved** |
| 6:0 | H3068G | Lord | related_word |  | CORRECTED (v1 wrongly reported 0): 39 related codes under the exact code H3068G, genuine and theologically significant -- the full divine-name/epithet cluster across Hebrew (Adonai, El, El-Berith) and Greek (Abba, Eloi, Eli, Sabaoth, Hupsistos), directly relevant to a study of divine-referring vocabulary. | **resolved** |
| 7:0 | H1984B | praised | related_word |  | CORRECTED (v1 wrongly reported 0): 14 related codes under the exact code H1984B, genuine and notable -- halal ('to praise') shares its single root with 'to shine' (H1984A), 'to boast/rave madly' (H1984H/I), and 'madness' (H1947/H1948). A real, nuanced finding: the word for 'praised' shares its root with boasting and even madness, worth naming rather than treating as a plain synonym-only relation. | **resolved** |
| 7:1 | H1931 | praised | related_word |  | Pronoun-form cognates (he/she/it family, H1932/H2007) -- present but not a substantive finding on its own. | **resolved** |
| 7:1 | H1931 | praised | pronoun_resolution | Prov.31.30:4 | 'she' (the subject of 'is to be praised') refers back to 'a woman who fears the LORD' (position 4), not to charm/beauty -- confirms the verse's own antithetical structure resolves to the woman as the praised subject. | **resolved** |

### Consolidated narrative (double control)

This is the concluding antithesis of the Proverbs 31 acrostic. Re-reading the findings together, the adversative "but" remains correctly UNCLASSIFIED. The Charm/Hen root-collision finding (51 mostly-irrelevant hits) and the vain/Abel wordplay finding stand as before. The corrected pulls add two genuinely significant findings that were wrongly reported empty: "woman" (ishah, H0802G) now shows its own real, well-known etymological pairing with "man" (ish) -- directly relevant to this project's own interest in human/party vocabulary, not a generic relation; and "Lord" (H3068G) now shows the full cross-lingual divine-epithet cluster (Adonai/El, and the Greek Abba/Eloi/Eli/Sabaoth/Hupsistos) that this study would want captured for any divine-vocabulary work, previously missed entirely. The corrected pull for "praised" (halal, H1984B) reveals something genuinely worth noting on its own: this root spans praise, boasting, and even madness -- the same word-family covers the God-fearing woman's due praise and a very different, less flattering kind of self-glorying, a nuance the shallow pull could never have surfaced. Holistically, the antithesis (charm/beauty vs. the God-fearing woman) still resolves cleanly to the woman via the final pronoun_resolution, and the newly-recovered findings deepen rather than complicate that reading.

---

## Ps.94.22 — Poetry/Psalm

**Verse text:** But the Lord has become my stronghold, and my God the rock of my refuge.

### Layer 1 — `verse_lexical` (13 rows)

| pos | ord | strong | morph | role | surface | lang | testament | negator | narr_morph | gloss_ok | party | cluster | l1_status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 0 | H3068G | HNpt | content | Lord | Hebrew | OT |  |  | 1 | divine | Party-Divine | resolved |
| 0 | 1 | H1961 | HVqw3ms | content | Lord | Hebrew | OT |  | wayyiqtol | 1 |  | Supplementary | resolved |
| 1 | 0 | H4869A | HNcmsa | content | stronghold | Hebrew | OT |  |  | 1 |  |  | resolved |
| 1 | 1 | H9005 | HR | function | stronghold | Hebrew | OT |  |  | 1 |  |  | resolved |
| 1 | 2 | H9005 | HR | function | stronghold | Hebrew | OT |  |  | 1 |  |  | resolved |
| 1 | 3 | H9030 | HSp1bs | function | stronghold | Hebrew | OT |  |  | 1 |  | Supplementary | resolved |
| 2 | 0 | H0430G | HNcmpc | content | God | Hebrew | OT |  |  | 1 | divine | Party-Divine | resolved |
| 2 | 1 | H9002 | HC | function | God | Hebrew | OT |  |  | 1 |  | Connective | resolved |
| 3 | 0 | H6697H | HNcmsc | content | rock | Hebrew | OT |  |  | 1 |  | Supplementary | resolved |
| 3 | 1 | H9005 | HR | function | rock | Hebrew | OT |  |  | 1 |  |  | resolved |
| 3 | 2 | H9020 | HSp1bs | function | rock | Hebrew | OT |  |  | 1 |  |  | resolved |
| 4 | 0 | H4268 | HNcmsc | content | refuge | Hebrew | OT |  |  | 1 |  | Trust | resolved |
| 4 | 1 | H9020 | HSp1bs | function | refuge | Hebrew | OT |  |  | 1 |  |  | resolved |

### Layer 2 — `verse_lexical_note` (16 rows)

| pos:ord | strong | surface | note_type | target | finding | status |
|---|---|---|---|---|---|---|
| 0:0 | H3068G | Lord | related_word |  | CORRECTED (v1 wrongly reported 0): 39 related codes under the exact code H3068G -- same divine-name/epithet cluster as Prov.31.30 position 6, genuine, confirming the same cross-verse family recurring. | **resolved** |
| 0:0 | H3068G | Lord | entity_link | Ps.94.22:2 | 'the LORD' (position 0) and 'my God' (position 2) are the same referent, in synonymous parallelism -- both party_kind=divine, confirming the mechanical tag rather than adding a new fact. | **resolved** |
| 0:1 | H1961 | Lord | related_word |  | Minor genuine cognate: 'to fall'/'to be' (H1933) -- a real if modest etymological relative of hayah ('become'). | **resolved** |
| 0:1 | H1961 | Lord | chain |  | 'has become' carries narrative_morph=wayyiqtol -- a genuine sequential-argument marker within the psalm's own developing claim, not a static statement. | **resolved** |
| 1:0 | H4869A | stronghold | related_word |  | CORRECTED (v1 wrongly reported 0): 4 related codes under the exact code H4869A, genuine -- misgav ('stronghold') shares its root with sagav ('to exalt') -- a stronghold is, at root, an exalted/high place, a real etymological connection directly relevant to this verse's own image. | **resolved** |
| 1:0 | H4869A | stronghold | structural_pattern |  | 'stronghold' / 'rock' / 'refuge' form a 3-term synonym cluster in poetic parallelism, all predicated of the same divine subject -- the verse's characteristic Hebrew poetic doubling (here tripling). | **resolved** |
| 1:1 | H9005 | stronghold | inert |  | Prepositional prefix, function role. | **checked_empty** |
| 1:2 | H9005 | stronghold | inert |  | Prepositional prefix (second component of a compound preposition), function role. | **checked_empty** |
| 1:3 | H9030 | stronghold | pronoun_resolution |  | 1cs possessive suffix ('my') -- self-reference to the psalmist speaker, straightforward. | **resolved** |
| 2:0 | H0430G | God | related_word |  | CORRECTED (v1 wrongly reported 0): 46 related codes under the exact code H0430G -- the SAME divine-name/epithet cluster as H3068G above (Abba/Eloi/Eli/Adonai/El), directly confirming the entity_link's own claim that 'the LORD' and 'my God' are parallel divine epithets from the same lexical family. | **resolved** |
| 2:1 | H9002 | God | connective |  | Coordinating 'and', joining the two divine epithets (LORD / God). | **resolved** |
| 3:0 | H6697H | rock | related_word |  | CORRECTED (v1 wrongly reported 0): 10 related codes under the exact code H6697H, genuine and relevant -- tsur ('rock') shares its root with 'to confine/besiege' (H6696A) -- a rock as a place of refuge is, at root, a place that confines/shelters from danger, directly relevant to this verse's own refuge theme. | **resolved** |
| 3:1 | H9005 | rock | inert |  | Prepositional prefix, function role. | **checked_empty** |
| 3:2 | H9020 | rock | pronoun_resolution |  | 1cs possessive suffix ('my') -- self-reference to the psalmist. | **resolved** |
| 4:0 | H4268 | refuge | related_word |  | Genuine same-concept family: 'to seek refuge' (H2620/H2622) -- real semantic cluster, directly on-topic. | **resolved** |
| 4:1 | H9020 | refuge | pronoun_resolution |  | 1cs possessive suffix ('my') -- self-reference to the psalmist. | **resolved** |

### Consolidated narrative (double control)

This verse is the psalm's own climactic confession. Re-reading the findings together, the entity_link (LORD = God) and the structural_pattern (stronghold/rock/refuge) still work together consistently. The corrected pulls now give this a much stronger evidentiary base: both "the LORD" (H3068G) and "my God" (H0430G) independently pull the SAME cross-lingual divine-epithet cluster -- direct confirmation, from the mechanical data itself, that the entity_link's claim (these are parallel names for one referent) is correct, not merely asserted. "Stronghold" (misgav) and "rock" (tsur) both now show genuine etymological roots -- "to exalt" and "to confine/besiege" respectively -- meaning the 3-term poetic cluster isn't just a surface synonym list but each term individually earns its place in the image (a high place; a place that shelters from danger). The chain finding on "has become" (wayyiqtol) and the three self-referential "my" pronouns stand as before. Holistically, this verse benefits the most visibly from the correction: what were four checked_empty related_word notes are now four genuine, mutually-reinforcing findings supporting the same poetic structure already identified.

---

## Eccl.5.14 — Wisdom/philosophical

**Verse text:** and those riches were lost in a bad venture. And he is father of a son, but he has nothing in his hand.

### Layer 1 — `verse_lexical` (16 rows)

| pos | ord | strong | morph | role | surface | lang | testament | negator | narr_morph | gloss_ok | party | cluster | l1_status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 0 | H1931 | HPp3ms | content | and those | Hebrew | OT |  |  | 1 |  | Supplementary | resolved |
| 0 | 1 | H9009 | HTd | function | and those | Hebrew | OT |  |  | 1 |  |  | resolved |
| 1 | 0 | H6239 | HNcmsa | content | riches | Hebrew | OT |  |  | 1 |  | Abundance | resolved |
| 1 | 1 | H9009 | HTd | function | riches | Hebrew | OT |  |  | 1 |  |  | resolved |
| 2 | 0 | H0006 | HVqq3ms | content | lost | Hebrew | OT |  |  | 1 |  | Operations | resolved |
| 3 | 0 | H7451A | HAamsa | content | bad | Hebrew | OT |  |  | 1 |  | Wickedness | resolved |
| 4 | 0 | H6045 | HNcmsc | content | venture | Hebrew | OT |  |  | 1 |  | Supplementary | resolved |
| 4 | 1 | H9003 | HR | function | venture | Hebrew | OT |  |  | 1 |  |  | resolved |
| 5 | 0 | H3205 | HVhq3ms | content | father | Hebrew | OT |  |  | 1 |  | Operations | resolved |
| 6 | 0 | H1121A | HNcmsa | content | son | Hebrew | OT |  |  | 1 |  |  | resolved |
| 7 | 0 | H0369 | HNcmsc | content | nothing | Hebrew | OT |  |  | 1 |  |  | resolved |
| 7 | 1 | H9002 | HC | function | nothing | Hebrew | OT |  |  | 1 |  | Connective | resolved |
| 7 | 2 | H3972 | HNcfsa | content | nothing | Hebrew | OT |  |  | 1 |  |  | resolved |
| 8 | 0 | H9023 | HSp3ms | function | his | Hebrew | OT |  |  | 1 |  |  | resolved |
| 9 | 0 | H3027G | HNcbsc | content | hand | Hebrew | OT |  |  | 1 |  | Supplementary | resolved |
| 9 | 1 | H9003 | HR | function | hand | Hebrew | OT |  |  | 1 |  |  | resolved |

### Layer 2 — `verse_lexical_note` (19 rows)

| pos:ord | strong | surface | note_type | target | finding | status |
|---|---|---|---|---|---|---|
| 0:0 | H1931 | and those | related_word |  | Mechanical pronoun-form cognates (he/she/it family) -- present but not a substantive finding on its own. | **resolved** |
| 0:0 | H1931 | and those | entity_link | Eccl.5.13:6 **(cross-verse)** | 'and those [riches]' picks up the referent from the immediately preceding verse (Eccl.5.13's own 'riches') -- a genuine cross-verse resolution. | **resolved** |
| 0:1 | H9009 | and those | inert |  | Definite article, function role. | **checked_empty** |
| 1:0 | H6239 | riches | related_word |  | Genuine same-concept family: rich/enrich (H6223/H6238) -- real semantic cluster. | **resolved** |
| 1:1 | H9009 | riches | inert |  | Definite article, function role. | **checked_empty** |
| 2:0 | H0006 | lost | related_word |  | Genuine, strong family: destroy/destruction/Abaddon (H0007-H0011) -- Abaddon as the personification of destruction is a real, notable related concept, not a coincidental collision. | **resolved** |
| 3:0 | H7451A | bad | related_word |  | CORRECTED (v1 wrongly reported 0): 8 related codes under the exact code H7451A, genuine -- the ra ('bad/evil') root's own same-lemma sub-senses (evil/distress:harm) plus a real cognate extending to 'to shatter' (H7489B), a wide semantic range for a single root. | **resolved** |
| 4:0 | H6045 | venture | related_word |  | Genuine root connection: 'to be occupied/afflicted' (H6031) -- 'venture/business' relates to being occupied/busy, a recurring theme-word in Ecclesiastes specifically. | **resolved** |
| 4:1 | H9003 | venture | inert |  | Prepositional prefix, function role. | **checked_empty** |
| 5:0 | H3205 | father | related_word |  | Same birth-root family as Gen.46.18 position 8 (child/youth/maiden, H3205's own family), here in its causative 'father of' sense rather than 'bore' -- a real sense-distinction worth naming. | **resolved** |
| 6:0 | H1121A | son | related_word |  | CORRECTED (v1 wrongly reported 0): 48 related codes under the exact code H1121A -- the same genuine ben ('son') family found at Gen.46.18 position 1, a good cross-verse consistency check (same code, same correct classification, two different verses). | **resolved** |
| 7:0 | H0369 | nothing | related_word |  | Genuine family: 'where?' / 'isn't?' (H0370/H0371) -- real negation-of-existence semantic cluster. | **resolved** |
| 7:1 | H9002 | nothing | inert |  | Conjunctive prefix, function role. | **checked_empty** |
| 7:2 | H3972 | nothing | related_word |  | Coincidental, not genuine: shares root letters with 'blemish' (H3971) but is not semantically related to this word's own sense ('anything/nothing') -- a minor Hebrew root collision. | **resolved** |
| 7:0 | H0369 | nothing | idiom |  | H0369 + H3972 together ('nothing... nothing') form the standard Hebrew double-negation idiom for absolute negation ('there is not a thing') -- one idiom across two codes, not two separate findings. | **resolved** |
| 8:0 | H9023 | his | pronoun_resolution |  | 3ms possessive suffix ('his') -- self-reference to the man just introduced in this verse. | **resolved** |
| 9:0 | H3027G | hand | related_word |  | CORRECTED (v1 wrongly reported 0): 22 related codes under the exact code H3027G, genuine and directly relevant -- yad ('hand') has an extremely wide range of its own idiomatic sub-senses (hand: power/by/to/times/monument/tool), which directly reinforces the idiom finding below. | **resolved** |
| 9:0 | H3027G | hand | idiom |  | 'in his hand' is the standard Hebrew idiom for 'in his possession/control', not a literal statement about a hand -- reinforced by yad's own related-word family showing this word's idiomatic range is extensive and well-attested. | **resolved** |
| 9:1 | H9003 | hand | inert |  | Prepositional prefix, function role. | **checked_empty** |

### Consolidated narrative (double control)

This verse depicts a reversal-of-fortune scene. Re-reading the findings together, the cross-verse entity_link (riches -> Eccl.5.13) remains essential, and the double-negation and "in his hand" idioms still intensify the verse's rhetorical point. The corrected pulls now give real support to two of those idioms: "hand" (yad, H3027G) shows an extremely wide family of its own idiomatic sub-senses, confirming "in his hand" sits within a well-attested idiomatic range, not an isolated reading; and "bad" (ra, H7451A) shows the same root extending to "to shatter," a wider semantic range than the plain gloss suggests. "Son" (H1121A) now correctly shows the same genuine ben family already found at Gen.46.18 -- the SAME code, correctly classified the same way in two different verses, a real cross-verse consistency check that the earlier bug had actually broken (both instances were wrongly checked_empty before the fix). Holistically consistent, and the correction closes a real internal inconsistency: two occurrences of the identical Strong's code no longer disagree with each other.

---

## Isa.4.5 — Major Prophet

**Verse text:** Then the Lord will create over the whole site of Mount Zion and over her assemblies a cloud by day, and smoke and the shining of a flaming fire by night; for over all the glory there will be a canopy.

### Layer 1 — `verse_lexical` (25 rows)

| pos | ord | strong | morph | role | surface | lang | testament | negator | narr_morph | gloss_ok | party | cluster | l1_status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 0 | H3068G | HNpt | content | Lord | Hebrew | OT |  |  | 1 | divine | Party-Divine | resolved |
| 1 | 0 | H1254A | HVqq3ms | content | create | Hebrew | OT |  |  | 1 |  | Operations | resolved |
| 2 | 0 | H5921A | HR | content | over | Hebrew | OT |  |  | 1 |  | Supplementary | resolved |
| 3 | 0 | H3605 | HNcmsc | content | whole | Hebrew | OT |  |  | 1 |  | Supplementary | resolved |
| 4 | 0 | H4349 | HNcmsc | content | site | Hebrew | OT |  |  | 1 |  | Supplementary | resolved |
| 5 | 0 | H2022G | HNcmsc | content | Mount | Hebrew | OT |  |  | 1 |  | Supplementary | resolved |
| 6 | 0 | H6726 | HNpl | content | Zion | Hebrew | OT |  |  | 1 |  |  | resolved |
| 7 | 0 | H5921A | HR | content | over | Hebrew | OT |  |  | 1 |  | Supplementary | resolved |
| 7 | 1 | H9002 | HC | function | over | Hebrew | OT |  |  | 1 |  | Connective | resolved |
| 8 | 0 | H4744 | HNcmsc | content | assemblies | Hebrew | OT |  |  | 1 |  | Love | resolved |
| 9 | 0 | H6051 | HNcmsa | content | cloud | Hebrew | OT |  |  | 1 |  |  | resolved |
| 9 | 1 | H9024 | HSp3fs | function | cloud | Hebrew | OT |  |  | 1 |  |  | resolved |
| 10 | 0 | H3119 | HD | content | day | Hebrew | OT |  |  | 1 |  |  | resolved |
| 11 | 0 | H6227 | HNcmsa | content | smoke | Hebrew | OT |  |  | 1 |  |  | resolved |
| 11 | 1 | H9002 | HC | function | smoke | Hebrew | OT |  |  | 1 |  | Connective | resolved |
| 12 | 0 | H5051 | HNcfsc | content | shining | Hebrew | OT |  |  | 1 |  |  | resolved |
| 12 | 1 | H9002 | HC | function | shining | Hebrew | OT |  |  | 1 |  | Connective | resolved |
| 13 | 0 | H3852 | HNcfsa | content | flaming | Hebrew | OT |  |  | 1 |  |  | resolved |
| 14 | 0 | H0784 | HNcbsa | content | fire | Hebrew | OT |  |  | 1 |  |  | resolved |
| 15 | 0 | H3915 | HNcmsa | content | night | Hebrew | OT |  |  | 1 |  |  | resolved |
| 16 | 0 | H3588A | HTc | content | for | Hebrew | OT |  |  | 1 |  | Connective | resolved |
| 17 | 0 | H5921A | HR | content | over | Hebrew | OT |  |  | 1 |  | Supplementary | resolved |
| 18 | 0 | H3605 | HNcmsc | content | all | Hebrew | OT |  |  | 1 |  | Supplementary | resolved |
| 19 | 0 | H3519 | HNcmsa | content | glory | Hebrew | OT |  |  | 1 |  | Praise | resolved |
| 20 | 0 | H2646 | HNcfsa | content | canopy | Hebrew | OT |  |  | 1 |  |  | resolved |

### Layer 2 — `verse_lexical_note` (31 rows)

| pos:ord | strong | surface | note_type | target | finding | status |
|---|---|---|---|---|---|---|
| 0:0 | H3068G | Lord | related_word |  | CORRECTED (v1 wrongly reported 0): 39 related codes under the exact code H3068G -- the same divine-name/epithet cluster found at Prov.31.30 and Ps.94.22, genuine, a recurring family across this 10-verse sample. | **resolved** |
| 1:0 | H1254A | create | related_word |  | CORRECTED (v1 wrongly reported 0): 3 related codes under the exact code H1254A, genuine but modest -- beriah ('creation', H1278) is a direct cognate noun. Bara ('create') is used almost exclusively of divine creative action in the OT -- a theologically loaded verb choice, now with real supporting related-word evidence rather than an unsupported observation. | **resolved** |
| 2:0 | H5921A | over | related_word |  | CORRECTED (v1 wrongly reported 0): 38 related codes under the exact code H5921A, genuine and interesting -- 'over' (al) relates etymologically to 'above' (ma'al) and 'lifting' (mo'al), and also cross-references H3588 (ki, 'for'/'that') -- the SAME code classified as a causal connective at position 16 of this verse. A real, small network of related Hebrew particles, not a coincidence worth ignoring. | **resolved** |
| 3:0 | H3605 | whole | related_word |  | Genuine family: all/entire/perfect (H3606/H3632/H3634) -- real semantic cluster. | **resolved** |
| 4:0 | H4349 | site | related_word |  | Coincidental at scale: 24 related codes, almost entirely proper names (Jachin, Jeconiah) sharing the root letters of 'site/place' -- a textbook Hebrew triliteral collision, correctly sorted coincidental. | **resolved** |
| 5:0 | H2022G | Mount | related_word |  | CORRECTED (v1 wrongly reported 0): 11 related codes under the exact code H2022G, genuine -- har ('mountain') family including its own sub-sense (hill country), Hor/Hara/Haran (place names genuinely built on the same root), and harar (a direct cognate, 'mountain'). | **resolved** |
| 5:0 | H2022G | Mount | noun_relational | Isa.4.5:6 | 'Mount' + 'Zion' (position 6) is a construct-state relational pairing identifying which mount is meant -- not two separate referents needing an entity_link, a plain construct relation. | **resolved** |
| 6:0 | H6726 | Zion | related_word |  | Genuine toponymic family: Jerusalem/Salem/Zion (attested cross-lingually, Hebrew and Greek) -- a real, meaningful place-name cluster. | **resolved** |
| 7:0 | H5921A | over | related_word |  | Same corrected H5921A family as position 2 -- second occurrence of 'over' in this verse. | **resolved** |
| 7:0 | H5921A | over | recurrence_role_shift | Isa.4.5:2 | Same code (H5921A, 'over') recurs from position 2, but the grammatical role does NOT shift -- both instances mark the object of protective coverage. A plain repeated function word, correctly recorded checked_empty. | **checked_empty** |
| 7:1 | H9002 | over | connective |  | Coordinating 'and', joining 'over the site of Mount Zion' with 'over her assemblies'. | **resolved** |
| 8:0 | H4744 | assemblies | related_word |  | Genuine root connection: 'to call/proclaim' (H7121) -- an assembly (miqra) is literally 'a calling-together', a real etymological insight. | **resolved** |
| 9:0 | H6051 | cloud | related_word |  | Genuine same-concept family: cloud (H6049-H6053) -- real semantic cluster. | **resolved** |
| 9:0 | H6051 | cloud | structural_pattern |  | 'cloud' / 'smoke' / 'shining' / 'fire' form a 4-term theophany-imagery cluster (day/night pairing) -- Sinai-pattern protective-presence imagery. | **resolved** |
| 9:1 | H9024 | cloud | pronoun_resolution | Isa.4.5:6 | 3fs possessive suffix ('her') refers to Zion (position 6), feminine place-name agreement. | **resolved** |
| 10:0 | H3119 | day | related_word |  | Genuine, straightforward family: day (H3117, multiple sub-senses) -- expected, real cluster. | **resolved** |
| 11:0 | H6227 | smoke | related_word |  | Mixed: 'to smoke'/'smoking' (H6225/H6226) genuine; Ashan (H6228) a coincidental place-name collision within the same pull. | **resolved** |
| 11:1 | H9002 | smoke | connective |  | Coordinating 'and', joining 'smoke' to the preceding 'cloud'. | **resolved** |
| 12:0 | H5051 | shining | related_word |  | Genuine family: to shine/brightness (H5050/H5053/H5054) -- real semantic cluster; Nogah (H5052, a personal name) a minor coincidental collision. | **resolved** |
| 12:1 | H9002 | shining | connective |  | Coordinating 'and', joining 'shining' to 'smoke'. | **resolved** |
| 13:0 | H3852 | flaming | related_word |  | Genuine family: flame (H3827/H3851/H7957) -- real semantic cluster; Lehabim (H3853, a people-name) a minor coincidental collision. | **resolved** |
| 14:0 | H0784 | fire | related_word |  | Coincidental, not genuine: Ashbel/Eshban/Ashbea are proper names sharing root letters with 'fire' but semantically unrelated. | **resolved** |
| 15:0 | H3915 | night | related_word |  | Mostly coincidental: Letushim (a tribe-name), 'to sharpen' -- tenuous or unrelated collisions with 'night'. | **resolved** |
| 16:0 | H3588A | for | related_word |  | CORRECTED (v1 wrongly reported 0): 11 related codes under the exact code H3588A, genuine and connected -- ki ('for') cross-references H0518A ('if', the SAME code found conditional at Lev.17.16), and its own sub-senses (that if: except / for as that: since). Confirms 'for' and 'if' are lexically related in STEP's own data, part of the same small conditional/causal-particle network noted at position 2's 'over'. | **resolved** |
| 16:0 | H3588A | for | connective |  | Causal 'for' -- genuinely classifiable against the 3-class lexicon as causal, introducing the reason/basis for the preceding description. | **resolved** |
| 17:0 | H5921A | over | related_word |  | Same corrected H5921A family as positions 2 and 7 -- third occurrence of 'over' in this verse. | **resolved** |
| 17:0 | H5921A | over | recurrence_role_shift | Isa.4.5:2 | Third occurrence of H5921A ('over') in this verse -- again no role shift from its first occurrence (position 2), correctly recorded checked_empty. | **checked_empty** |
| 18:0 | H3605 | all | related_word |  | Genuine family: all/entire/perfect (same root as position 3's 'whole') -- real semantic cluster. | **resolved** |
| 18:0 | H3605 | all | recurrence_role_shift | Isa.4.5:3 | Same code (H3605) as position 3 ('whole'), but both occurrences are the same distributive-quantifier role -- no genuine role shift, correctly recorded checked_empty. | **checked_empty** |
| 19:0 | H3519 | glory | related_word |  | Genuine and notable: honor/heavy/glory (H3513-H3515) -- the well-known Hebrew 'weight = glory' semantic connection (kavod), a real and important finding. | **resolved** |
| 20:0 | H2646 | canopy | related_word |  | Mixed: Huppah/Huppim (proper names derived from the same root) alongside 'to cover'/'to shield' (H2645/H2653) -- a genuine, if modest, semantic connection to 'canopy' as a covering. | **resolved** |

### Consolidated narrative (double control)

This is Isaiah's theophany vision over Zion. Re-reading the findings together, the structural_pattern (cloud/smoke/shining/fire) and the recurrence_role_shift findings (three "over"s, two "all/whole"s) still hold. The corrected pulls are extensive here -- this was the most heavily affected verse -- and they reveal something genuinely interesting the shallow pull missed entirely: "over" (al, H5921A), "for" (ki, H3588A), and the conditional "if" family (H0518A, from Lev.17.16) all cross-reference each other in STEP's own related-word data. This is a real, small network of Hebrew logical/relational particles that happen to share etymological ground -- worth naming as its own observation, not three unconnected corrections. "Mount" (har) and "Zion" now both show genuine toponymic support for the noun_relational finding. "LORD" (H3068G) again pulls the same cross-lingual divine cluster found in Prov.31.30 and Ps.94.22 -- the third independent confirmation of that same family in this 10-verse sample. "Create" (bara) now has a real, if modest, supporting cognate (creation) rather than resting on an unsupported theological observation. Holistically, the verse's own central theophany image is unchanged, but the connective/particle network finding is a genuinely new observation this correction surfaced, not merely a repair.

---

## Amos.8.4 — Minor Prophet

**Verse text:** Hear this, you who trample on the needy and bring the poor of the land to an end,

### Layer 1 — `verse_lexical` (10 rows)

| pos | ord | strong | morph | role | surface | lang | testament | negator | narr_morph | gloss_ok | party | cluster | l1_status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 0 | H8085G | HVqv2mp | content | Hear | Hebrew | OT |  |  | 1 |  | Remembrance | resolved |
| 1 | 0 | H2063 | HTm | content | this | Hebrew | OT |  |  | 1 |  | Supplementary | resolved |
| 2 | 0 | H7602B | HVqrmpa | content | trample on | Hebrew | OT |  |  | 1 |  | Weakness | resolved |
| 2 | 1 | H9009 | HTd | function | trample on | Hebrew | OT |  |  | 1 |  |  | resolved |
| 3 | 0 | H0034 | HAamsa | content | needy | Hebrew | OT |  |  | 1 |  | Weakness, Supplementary | resolved |
| 4 | 0 | H6041 | HAampc | content | poor | Hebrew | OT |  |  | 1 |  | Weakness | resolved |
| 5 | 0 | H0776G | HNcfsa | content | land | Hebrew | OT |  |  | 1 |  |  | resolved |
| 6 | 0 | H7673A | HVhcc | content | end | Hebrew | OT |  |  | 1 |  | Supplementary | resolved |
| 6 | 1 | H9002 | HC | function | end | Hebrew | OT |  |  | 1 |  | Connective | resolved |
| 6 | 2 | H9005 | HR | function | end | Hebrew | OT |  |  | 1 |  |  | resolved |

### Layer 2 — `verse_lexical_note` (11 rows)

| pos:ord | strong | surface | note_type | target | finding | status |
|---|---|---|---|---|---|---|
| 0:0 | H8085G | Hear | related_word |  | CORRECTED (v1 wrongly reported 0): 90 related codes under the exact code H8085G, mostly coincidental at scale but with one genuinely meaningful exception -- Ishmael/Yishma'el (H3458, 6 sub-entries) is not a pure coincidence: the name literally means 'God hears', a deliberate name-formation on this exact root, the same pattern already found at Lev.17.16 (Lo-debar/Not-My-People). hashma'ut ('report', H2045) is also a genuine direct cognate. | **resolved** |
| 1:0 | H2063 | this | related_word |  | Minor genuine relation: 'this' (H2088) shares the demonstrative family, real if trivial. | **resolved** |
| 2:0 | H7602B | trample on | related_word |  | 1 related code pulled, form/gloss empty -- not usable. | **checked_empty** |
| 2:1 | H9009 | trample on | inert |  | Definite article, function role. | **checked_empty** |
| 3:0 | H0034 | needy | related_word |  | Genuine etymological finding: 'needy' (evyon) shares its root with 'to desire/be willing' (H0014/H0035) -- the needy are, at root, 'those who lack/desire'. | **resolved** |
| 4:0 | H6041 | poor | related_word |  | Genuine, strong family: afflict/poor/gentleness (H6031-H6038) -- a real, substantial semantic cluster central to this verse's own social-justice vocabulary. | **resolved** |
| 5:0 | H0776G | land | related_word |  | CORRECTED (v1 wrongly reported 0): 7 related codes under the exact code H0776G, genuine -- eretz/ara ('earth/land') own sub-senses (soil/inferior/planet), a real same-concept family. | **resolved** |
| 6:0 | H7673A | end | related_word |  | CORRECTED (v1 wrongly reported 0): 8 related codes under the exact code H7673A, genuine and notable -- shabath ('to bring to an end/cease') shares its root with shabbat ('Sabbath', the day of cessation/rest) -- ending/ceasing shares its very root with the concept of sabbath-rest, a real and meaningful etymological connection. | **resolved** |
| 6:0 | H7673A | end | structural_pattern |  | 'trample on' / 'needy' / 'poor' form the indictment's own accusation cluster -- the verb and its two victim-terms named together as one social-justice charge. | **resolved** |
| 6:1 | H9002 | end | inert |  | Conjunctive component within the compound verb phrase, function role. | **checked_empty** |
| 6:2 | H9005 | end | inert |  | Prepositional component within the compound verb phrase, function role. | **checked_empty** |

### Consolidated narrative (double control)

This is Amos' prophetic indictment against those who exploit the poor. Re-reading the findings together, the structural_pattern (trample/needy/poor) still captures the verse's rhetorical shape. The corrected pulls add two real findings: "land" (eretz) now shows its own genuine sub-sense family, and "end" (shabath, H7673A) reveals something worth real attention -- it shares its root with "Sabbath," the day of cessation and rest. Bringing exploitation "to an end" and the concept of sabbath-rest share the same Hebrew root, a genuinely apt (if easy to miss) connection for a verse about ceasing exploitation. "Hear" (shama, H8085G) pulled 90 related codes, almost all coincidental, but with one real exception worth naming: Ishmael's own name means "God hears," the same deliberate name-on-a-root pattern already found in Lev.17.16 (Lo-debar, Not-My-People) -- a recurring, real feature of Hebrew naming this sample keeps surfacing, not a one-off. Holistically, the verse's social-justice argument is unchanged, but is now better evidenced.

---

## Mark.11.21 — Gospel narrative

**Verse text:** And Peter remembered and said to him, “ Rabbi, look! The fig tree that you cursed has withered.”

### Layer 1 — `verse_lexical` (11 rows)

| pos | ord | strong | morph | role | surface | lang | testament | negator | narr_morph | gloss_ok | party | cluster | l1_status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 0 | G2532 | CONJ | function | And | Greek | NT |  |  | 1 |  | Connective | resolved |
| 1 | 0 | G4074G | N-NSM-P | content | Peter | Greek | NT |  |  | 1 |  |  | resolved |
| 2 | 0 | G0363 | V-AOP-NSM | content | remembered | Greek | NT |  |  | 1 |  | Remembrance | resolved |
| 3 | 0 | G3004G | V-PAI-3S | content | said | Greek | NT |  |  | 1 |  | Operations | resolved |
| 4 | 0 | G0846 | P-DSM | content | him | Greek | NT |  |  | 1 |  |  | resolved |
| 5 | 0 | G4461 | N-VSM-T | content | Rabbi | Greek | NT |  |  | 1 |  |  | resolved |
| 6 | 0 | G2396 | INJ | content | look | Greek | NT |  |  | 1 |  | Supplementary | resolved |
| 7 | 0 | G4808 | N-NSF | content | fig tree | Greek | NT |  |  | 1 |  | Supplementary | resolved |
| 8 | 0 | G3739 | R-ASF | content | that | Greek | NT |  |  | 1 |  |  | resolved |
| 9 | 0 | G2672 | V-ADI-2S | content | cursed | Greek | NT |  |  | 1 |  | Hate | resolved |
| 10 | 0 | G3583 | V-RPI-3S | content | withered | Greek | NT |  |  | 1 |  | Operations | resolved |

### Layer 2 — `verse_lexical_note` (14 rows)

| pos:ord | strong | surface | note_type | target | finding | status |
|---|---|---|---|---|---|---|
| 0:0 | G2532 | And | connective |  | Coordinating 'And' -- narrative sequencer opening the verse. | **resolved** |
| 1:0 | G4074G | Peter | related_word |  | CORRECTED (v1 wrongly reported 0): 16 related codes under the exact code G4074G, genuine and directly relevant -- Peter's OWN other names/epithets (Cephas, Simon, Bar-Jonah) are cross-referenced here, the same identity-cluster pattern as Jacob=Israel elsewhere in this sample -- one person, multiple attested names. | **resolved** |
| 2:0 | G0363 | remembered | related_word |  | Genuine, direct family: remembrance / to remember (G0364/G3403) -- real cognates, expected. | **resolved** |
| 3:0 | G3004G | said | related_word |  | CORRECTED (v1 wrongly reported 0): 15 related codes under the exact code G3004G, genuine but a notably different semantic register -- this 'say' root's family skews toward dispute/rebuke/conviction (antilego 'to dispute', elenchos 'rebuke', exelencho 'to convict'), not plain neutral speech. Worth naming: the same verb root that means simple 'said' here extends elsewhere to argumentative/accusatory speech. | **resolved** |
| 4:0 | G0846 | him | related_word |  | Minor genuine relation: reflexive-pronoun morphological family (G1438/G1683) -- real cognates, not a substantive finding on its own. | **resolved** |
| 4:0 | G0846 | him | entity_link |  | 'him' (dative) refers to Jesus, the addressee of Peter's remark -- confirmed from the target verse's own grammar (a vocative 'Rabbi' immediately follows). | **resolved** |
| 5:0 | G4461 | Rabbi | related_word |  | Genuine, direct cognate: Rabboni (G4462) -- the same honorific family, real. | **resolved** |
| 6:0 | G2396 | look | related_word |  | Genuine, direct cognate: 'to perceive/know' (G1492) -- 'look/behold' shares its root with 'to see', real and expected. | **resolved** |
| 7:0 | G4808 | fig tree | related_word |  | Genuine botanical-term cluster: mulberry/sycamore/fig (G4807/G4809/G4810) -- real, all fruit-tree names sharing a root, not coincidental. | **resolved** |
| 7:0 | G4808 | fig tree | entity_link | Mark.11.13:4 **(cross-verse)** | 'fig tree' (G4808) is the same tree Jesus approached in Mark.11.13 -- same strong code, same referent, confirmed by a targeted read of the earlier verse. NOT cross_lemma_shared_gloss -- that note_type is for two DIFFERENT lemmas sharing a sense, not the same code recurring. | **resolved** |
| 8:0 | G3739 | that | related_word |  | 1 related code pulled, form/gloss empty -- not usable. | **checked_empty** |
| 8:0 | G3739 | that | pronoun_resolution | Mark.11.21:7 | 'that' (relative pronoun) refers to 'fig tree' (position 7) -- the relative clause's antecedent within the same verse. | **resolved** |
| 9:0 | G2672 | cursed | related_word |  | Genuine, direct family: cursed/curse (G1944/G2671) -- real cognates. | **resolved** |
| 10:0 | G3583 | withered | related_word |  | Genuine, direct cognate: 'dried up/withered' (G3584) -- real, expected. | **resolved** |

### Consolidated narrative (double control)

This verse records Peter's remembrance of the cursed fig tree. Re-reading the findings together, the cross-verse entity_link (fig tree -> Mark.11.13) remains the single most important finding, and the relative-pronoun and "him" resolutions still correctly disambiguate the verse's referring expressions. The corrected pulls (this verse was also affected, despite being Greek) add two genuine findings: "Peter" (G4074G) now shows his own attested other names -- Cephas, Simon, Bar-Jonah -- the same one-person-multiple-names pattern already found for Jacob/Israel in the Hebrew verses, a real cross-lingual parallel in how this sample's own findings recur. "Said" (G3004G) now shows a real family, but a notably different one than expected: this root's wider family skews toward dispute, rebuke, and conviction, not neutral speech -- worth naming as a genuine semantic-range observation rather than assuming "said" is always semantically plain. Holistically coherent: every finding, corrected or original, supports one clear narrative reading.

---

## Rom.9.14 — Epistle/didactic

**Verse text:** What shall we say then? Is there injustice on God’s part? By no means!

### Layer 1 — `verse_lexical` (9 rows)

| pos | ord | strong | morph | role | surface | lang | testament | negator | narr_morph | gloss_ok | party | cluster | l1_status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 0 | G5101 | I-ASN | content | What | Greek | NT |  |  | 1 |  |  | resolved |
| 1 | 0 | G4483 | V-FAI-1P | content | say | Greek | NT |  |  | 1 |  | Desire | resolved |
| 2 | 0 | G3767 | CONJ | function | then | Greek | NT |  |  | 1 |  |  | resolved |
| 3 | 0 | G3361 | PRT-N | function | Is | Greek | NT | 1 |  | 1 |  | Negator | resolved |
| 4 | 0 | G0093 | N-NSF | content | injustice | Greek | NT |  |  | 1 |  | Wickedness | resolved |
| 5 | 0 | G3844 | PREP | function | on | Greek | NT |  |  | 1 |  | Flag, Supplementary | resolved |
| 6 | 0 | G2316 | N-DSM-T | content | God’s | Greek | NT |  |  | 1 | divine | Party-Divine | resolved |
| 7 | 0 | G3361 | PRT-N | function | no | Greek | NT | 1 |  | 1 |  | Negator | resolved |
| 8 | 0 | G1096 | V-2ADO-3S | content | means | Greek | NT |  |  | 1 |  | Supplementary | resolved |

### Layer 2 — `verse_lexical_note` (11 rows)

| pos:ord | strong | surface | note_type | target | finding | status |
|---|---|---|---|---|---|---|
| 0:0 | G5101 | What | related_word |  | Genuine interrogative-pronoun family: why?/one?/which? (G2444/G5100) -- real cognates, expected. | **resolved** |
| 1:0 | G4483 | say | related_word |  | Genuine, large cognate family: say/speak (G2036/G2046/G4482/G4487/G4489) -- the classic Greek verb-of-speech cluster, real. | **resolved** |
| 2:0 | G3767 | then | connective |  | 'then' (oun) here is inferential -- drawing a conclusion from the preceding argument. The design's 3-class connective lexicon has no inferential class -- correctly UNCLASSIFIED, the same taxonomy gap already found at Lev.17.16 (conditional) and Prov.31.30 (adversative). | **unclassified** |
| 3:0 | G3361 | Is | related_word |  | 0 related codes pulled. | **checked_empty** |
| 3:0 | G3361 | Is | connective |  | Part of the me genoito ('by no means') rhetorical-denial construction together with positions 7-8. | **resolved** |
| 4:0 | G0093 | injustice | related_word |  | Genuine, rich family: harm/crime/unjust/opponent/justice (G0091-G1341) -- a substantial semantic cluster directly relevant to Paul's own argument about justice/righteousness in Romans. | **resolved** |
| 5:0 | G3844 | on | related_word |  | 0 related codes pulled. | **checked_empty** |
| 6:0 | G2316 | God’s | related_word |  | Genuine, theologically rich family: without-God/goddess/divine/God-fighting/God-breathed (G0112-G2315) -- a real, significant cluster directly relevant to a study of divine-referring vocabulary specifically. | **resolved** |
| 7:0 | G3361 | no | related_word |  | 0 related codes pulled. | **checked_empty** |
| 7:0 | G3361 | no | idiom | Rom.9.14:8 | me genoito ('by no means') is a fixed, well-known Pauline rhetorical idiom for emphatic denial, spanning positions 7-8. | **resolved** |
| 8:0 | G1096 | means | related_word |  | Only a self-referential match (ginomai to itself) -- not a genuine external relation. | **checked_empty** |

### Consolidated narrative (double control)

This is Paul's rhetorical question-and-denial. This verse was not affected by the related_word bug (none of its content codes carry a letter-suffix collision), so its findings stand unchanged: the inferential "then" remains the third and final instance of the same recurring connective-taxonomy gap found at Lev.17.16 and Prov.31.30 -- now confirmed as a genuine pattern across the whole 10-verse sample, not an artefact of the correction elsewhere. The idiom finding (me genoito) and the two rich, thematically load-bearing related-word families (injustice; God) stand as originally recorded. Holistically consistent, and this verse's own stability across both passes is itself a useful confirmation that the bug was specific to suffixed codes, not a general defect in the method.

---
