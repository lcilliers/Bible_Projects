# 10 random OT verses — morphology positions & the 16 dimensions (what morphology can / cannot give)

> Demonstration for the mechanical-fill proposal (generate lexicals from morphology, verse-by-verse, over the OT no-lexical spans). For 10 random OT verses: the morphology laid out per word-position (the `verse_span_index` rows), then the 16 per-span dimensions (`ve_nr` 101–116) with a verdict on whether each can be derived from morphology alone. Grounded in the ve-lexical catalogue reliability ratings + `wa-lexical-14dim-validation-final-20260702.md`.

## The 16 dimensions — morphology derivability

| ve_nr | dimension | shape | from morphology? | basis |
|--:|---|---|---|---|
| 101 | **sense** | value | **DERIVABLE** | strong + STEP sub-gloss keyed by the morph form |
| 102 | **type** | value | **DERIVABLE** | from POS: verb->action, noun->status, adjective->quality |
| 103 | **source** | pair | **PARTIAL** | driver/antecedent structurally approximable from argument order; the actual DRIVER vs restraint is semantic |
| 104 | **seat** | pair | **DERIVABLE** | construct state (heart-of-X) is in the morph; "is a seat" via a seat lexeme-list |
| 105 | **bearer** | pair | **PARTIAL** | subject agreement + suffix are in the morph; resolving WHO (the referent) is contextual |
| 106 | **operation** | event | **DERIVABLE** | the predicate = the verb; morph pos flags every verb |
| 107 | **target** | pair | **PARTIAL** | object-marker HTo/word-order give the object; object-TYPE (person/God/thing) is semantic |
| 108 | **manner** | pair | **DERIVABLE** | prep-marked adverbial (HR) is in the morph; which term it binds is syntactic |
| 109 | **intensity** | value | **DERIVABLE** | lexeme match: me’od (H3966) / kol (H3605) |
| 110 | **specifier** | pair | **PARTIAL** | genitive/of-phrase (construct + noun) is morph; the bound term partial |
| 111 | **effect** | pair | **PARTIAL** | stem (Piel/Hiphil) + adjacency are morph; the causal "produces-state" link is semantic (narrative ok, poetry weak) |
| 112 | **coupling** | pair | **DERIVABLE** | defined AS the morphological weld (construct/preposition binding) — purely morph |
| 113 | **prohibition** | flag | **DERIVABLE** | negation particle HTn (lo/al) adjacent to the term — mechanical proximity |
| 114 | **discovery** | note | **N/A** | not a derivation — the uncertainty/notes channel written during read-back |
| 115 | **role** | value | **NOT DERIVABLE** | characteristic/qualifier/standalone — requires the meaning evaluation; explicitly not set at build |
| 116 | **locus** | value | **PARTIAL** | proper-noun/place morph gives external:proper; the semantic locus role partial |

**Summary**
- **Fully derivable from morphology (8):** sense, type, operation, seat, manner, intensity, coupling, prohibition.
- **Partial — morph gives structure/hint, meaning needed to finalise (6):** source, bearer, target, effect, specifier, locus.
- **NOT derivable — needs the meaning read (1):** **role**. (This is the one the mechanical pass must leave NULL.)
- **N/A — not a derivation (1):** discovery (the read-back notes channel).

So a morphology-only pass can honestly fill the 8 reliable dimensions, *approximate* the 6 partials (flag as provisional), and **must leave `role` empty** for the separate meaning pass.

### morph_code legend (the signals the derivable dims read)
`HV`=verb `HN c/p`=common/proper noun `HA`=adjective `HP`=pronoun `HD`=adverb `HS`=suffix &nbsp;|&nbsp; prefixes: `HR`=preposition `HTd`=definite article `HTo`=object-marker (’et) `HC`=conjunction `HTn`=negation `HTc`=conj &nbsp;|&nbsp; noun state: `...c`=construct (weld/seat/specifier signal) `...a`=absolute &nbsp;|&nbsp; stems: Qal/Piel/Hiphil/Hophal/Niphal (Piel/Hiphil → effect signal)

---

## Exo 26:31  — Exodus (prose/law)

> Exo 26:31 “And you shall make a veil of blue and purple and scarlet yarns and fine twined linen . It shall be made with cherubim skillfully worked into it .

| wi | surface | pos | morph_code | stem | strongs | primary | role (master) |
|--:|---|---|---|---|---|---|---|
| 0 | make | verb | `HVqq2ms` | Qal | H6213H | H6213 | — (NULL) |
| 1 | veil | noun | `HNcfsa` |  | H6532 | H6532 | — (NULL) |
| 2 | blue | noun | `HNcfsa` |  | H8504 | H8504 | — (NULL) |
| 3 | purple | noun | `HNcmsa HC` |  | H0713 H9002 | H0713 | — (NULL) |
| 4 | scarlet | noun | `HNcmsa HNcfsc HC` |  | H8144 H8438B H9002 | H8144 | — (NULL) |
| 5 | fine twined | verb | `HVHsmsa` | Hophal | H7806 | H7806 | — (NULL) |
| 6 | linen | noun | `HNcmsa HC` |  | H8336B H9002 | H8336 | — (NULL) |
| 7 | made | verb | `HVqi3ms` | Qal | H6213H | H6213 | — (NULL) |
| 8 | cherubim | noun | `HNcmpa HTo HSp3fs` |  | H3742 H0853 H9034 | H3742 | — (NULL) |
| 9 | skillfully | verb | `HVqrmsa` | Qal | H2803G | H2803 | — (NULL) |
| 10 | it | noun | `HNcmsc` |  | H4639G | H4639 | — (NULL) |

## Psa 132:13  — Psalms (poetry)

> Psa 132:13 For the Lord has chosen Zion ; he has desired it for his dwelling place :

| wi | surface | pos | morph_code | stem | strongs | primary | role (master) |
|--:|---|---|---|---|---|---|---|
| 0 | Lord | noun | `HNpt` |  | H3068G | H3068 | standalone |
| 1 | chosen | verb | `HVqp3ms HTc` | Qal | H0977 H3588A | H0977 | qualifier |
| 2 | Zion | noun | `HNpl HR` |  | H6726 H9003 | H6726 | standalone |
| 3 | desired | verb | `HVpp3ms` | Piel | H0183 | H0183 | characteristic |
| 4 | his | preposition | `HR HSp3ms` |  | H9005 H9033 | H9005 | — (NULL) |
| 5 | dwelling place | noun | `HNcmsa HR HSp3fs` |  | H4186 H9005 H9034 | H4186 | qualifier |

## Pro 28:6  — Proverbs (wisdom)

> Pro 28:6 Better is a poor man who walks in his integrity than a rich man who is crooked in his ways .

| wi | surface | pos | morph_code | stem | strongs | primary | role (master) |
|--:|---|---|---|---|---|---|---|
| 0 | Better | adjective | `HAamsa` |  | H2896A | H2896 | characteristic |
| 1 | poor man | verb | `HVqrmsa` | Qal | H7326 | H7326 | standalone |
| 2 | walks | verb | `HVqrmsa` | Qal | H1980I | H1980 | standalone |
| 3 | integrity | noun | `HNcmsc HR` |  | H8537 H9003 | H8537 | process-qualifier |
| 4 | rich man | adjective | `HAamsa HPp3ms HC` |  | H6223 H1931 H9002 | H6223 | characteristic |
| 5 | crooked | adjective | `HAamsa HR HSp3ms` |  | H6141 H9006 H9023 | H6141 | standalone |
| 6 | ways | noun | `HNcbda` |  | H1870G | H1870 | standalone |

## Song 1:2  — Song of Solomon (poetry)

> Song 1:2 Let him kiss me with the kisses of his mouth ! For your love is better than wine ;

| wi | surface | pos | morph_code | stem | strongs | primary | role (master) |
|--:|---|---|---|---|---|---|---|
| 0 | kiss | verb | `HVqi3ms` | Qal | H5401A | H5401 | — (NULL) |
| 1 | kisses | noun | `HNcfpc` |  | H5390 | H5390 | — (NULL) |
| 2 | mouth | noun | `HNcmsc` |  | H6310G | H6310 | — (NULL) |
| 3 | For | particle | `HTc HSp3ms` |  | H3588A H9023 | H3588 | — (NULL) |
| 4 | love | noun | `HNcmpc` |  | H1730H | H1730 | — (NULL) |
| 5 | better | adjective | `HAampa` |  | H2896A | H2896 | — (NULL) |
| 6 | than | preposition | `HR HSp1bs` |  | H9006 H9030 | H9006 | — (NULL) |
| 7 | wine | noun | `HNcmsa HR HSp2ms` |  | H3196 H9006 H9021 | H3196 | — (NULL) |

## Gen 11:10  — Genesis (narrative)

> Gen 11:10 These are the generations of Shem. When Shem was 100 years old, he fathered Arpachshad two years after the flood.

| wi | surface | pos | morph_code | stem | strongs | primary | role (master) |
|--:|---|---|---|---|---|---|---|
| 0 | generations | noun | `HNcfpc HTm` |  | H8435 H0428 | H8435 | — (NULL) |
| 1 | Shem | noun | `HNpm` |  | H8035 | H8035 | — (NULL) |
| 2 | Shem | noun | `HNpm` |  | H8035 | H8035 | — (NULL) |
| 3 | 100 | adjective | `HAcfsc` |  | H3967 | H3967 | — (NULL) |
| 4 | years | noun | `HNcfsa` |  | H8141 | H8141 | — (NULL) |
| 5 | old | noun | `HNcmsc` |  | H1121L | H1121 | — (NULL) |
| 6 | fathered | verb | `HVhw3ms` | Hiphil | H3205 | H3205 | — (NULL) |
| 7 | Arpachshad | noun | `HNpm HTo` |  | H0775 H0853 | H0775 | — (NULL) |
| 8 | years | noun | `HNcfda` |  | H8141 | H8141 | — (NULL) |
| 9 | after | adjective | `HAcmsc` |  | H0310A | H0310 | — (NULL) |
| 10 | flood | noun | `HNcmsa HTd` |  | H3999 H9009 | H3999 | — (NULL) |

## Isa 41:2  — Isaiah (prophetic)

> Isa 41:2 Who stirred up one from the east whom victory meets at every step ? He gives up nations before him, so that he tramples kings underfoot; he makes them like dust with his sword , like driven stubble with his bow .

| wi | surface | pos | morph_code | stem | strongs | primary | role (master) |
|--:|---|---|---|---|---|---|---|
| 0 | Who | pronoun | `HPi` |  | H4310 | H4310 | — (NULL) |
| 1 | stirred up | verb | `HVhp3ms` | Hiphil | H5782 | H5782 | characteristic |
| 2 | from | preposition | `HR` |  | H9006 | H9006 | — (NULL) |
| 3 | east | noun | `HNcmsa` |  | H4217H | H4217 | standalone |
| 4 | victory | noun | `HNcmsa` |  | H6664G | H6664 | characteristic |
| 5 | meets | verb | `HVqi3ms` | Qal | H7121G | H7121 | characteristic |
| 6 | step | noun | `HNcfsc HR HSp3ms` |  | H7272 H9005 H9033 | H7272 | — (NULL) |
| 7 | He | suffix | `HSp3ms` |  | H9023 | H9023 | — (NULL) |
| 8 | up | verb | `HVqi3ms` | Qal | H5414G | H5414 | characteristic |
| 9 | nations | noun | `HNcmpa HSp3ms` |  | H1471A H9023 | H1471 | standalone |
| 10 | before | noun | `HNcmpc HR` |  | H6440G H9005 | H6440 | process-qualifier |
| 11 | tramples | verb | `HVhj3ms` | Hiphil | H7287A | H7287 | characteristic |
| 12 | kings | noun | `HNcmpa HC` |  | H4428G H9002 | H4428 | standalone |
| 13 | makes | verb | `HVqi3ms` | Qal | H5414P | H5414 | characteristic |
| 14 | dust | noun | `HNcmsa HRd` |  | H6083 H9004 | H6083 | process-qualifier |
| 15 | sword | noun | `HNcfsc` |  | H2719 | H2719 | standalone |
| 16 | driven | verb | `HVNrmsa` | Niphal | H5086 | H5086 | standalone |
| 17 | stubble | noun | `HNcmsa HR HSp3ms` |  | H7179 H9004 H9023 | H7179 | process-qualifier |
| 18 | his | suffix | `HSp3ms` |  | H9023 | H9023 | — (NULL) |
| 19 | bow | noun | `HNcfsc` |  | H7198 | H7198 | standalone |

## Eze 6:10  — Ezekiel (prophetic)

> Eze 6:10 And they shall know that I am the Lord . I have not said in vain that I would do this evil to them.”

| wi | surface | pos | morph_code | stem | strongs | primary | role (master) |
|--:|---|---|---|---|---|---|---|
| 0 | know | verb | `HVqq3cp` | Qal | H3045 | H3045 | standalone |
| 1 | that | particle | `HTc` |  | H3588A | H3588 | — (NULL) |
| 2 | I | pronoun | `HPp1bs` |  | H0589 | H0589 | — (NULL) |
| 3 | Lord | noun | `HNpt` |  | H3068G | H3068 | standalone |
| 4 | not | particle | `HTn` |  | H3808 | H3808 | — (NULL) |
| 5 | said | verb | `HVpp1cs` | Piel | H1696G | H1696 | standalone |
| 6 | vain | adverb | `HD HR` |  | H2600 H0413 | H2600 | — (NULL) |
| 7 | do | verb | `HVqcc HR` | Qal | H6213A H9005 | H6213 | standalone |
| 8 | this | particle | `HTm HTd` |  | H2063 H9009 | H2063 | — (NULL) |
| 9 | evil | noun | `HNcfsa HTd HR HSp3mp` |  | H7451I H9009 H9005 H9038 | H7451 | process-qualifier |

## Eze 46:8  — Ezekiel (prophetic)

> Eze 46:8 When the prince enters, he shall enter by the vestibule of the gate, and he shall go out by the same way.

| wi | surface | pos | morph_code | stem | strongs | primary | role (master) |
|--:|---|---|---|---|---|---|---|
| 0 | prince | noun | `HNcmsa HTd` |  | H5387A H9009 | H5387 | standalone |
| 1 | enters | verb | `HVqcc HC HR` | Qal | H0935G H9002 H9003 | H0935 | standalone |
| 2 | enter | verb | `HVqi3ms` | Qal | H0935G | H0935 | standalone |
| 3 | by | noun | `HNcbsc` |  | H1870J | H1870 | standalone |
| 4 | vestibule | noun | `HNcmsc` |  | H0197J | H0197 | standalone |
| 5 | gate | noun | `HNcmsa HTd` |  | H8179G H9009 | H8179 | standalone |
| 6 | go out | verb | `HVqi3ms HSp3ms` | Qal | H3318G H9023 | H3318 | standalone |
| 7 | way | noun | `HNcbsc HC HR` |  | H1870J H9002 H9003 | H1870 | process-qualifier |

## Obd 3  — Obadiah (prophetic)

> Obd 3 The pride of your heart has deceived you, you who live in the clefts of the rock , in your lofty dwelling , who say in your heart , “ Who will bring me down to the ground ?”

| wi | surface | pos | morph_code | stem | strongs | primary | role (master) |
|--:|---|---|---|---|---|---|---|
| 0 | pride | noun | `HNcmsc` |  | H2087 | H2087 | characteristic |
| 1 | heart | noun | `HNcmsc` |  | H3820A | H3820 | characteristic |
| 2 | deceived | verb | `HVhp3ms HSp2ms` | Hiphil | H5377 H9021 | H5377 | standalone |
| 3 | live | verb | `HVqrmsc HSp2ms` | Qal | H7931 H9031 | H7931 | standalone |
| 4 | clefts | noun | `HNcmpc HR` |  | H2288 H9003 | H2288 | process-qualifier |
| 5 | rock | noun | `HNcmsa` |  | H5553H | H5553 | standalone |
| 6 | lofty | noun | `HNcmsc` |  | H4791 | H4791 | characteristic |
| 7 | dwelling | verb | `HVqcc` | Qal | H7675 | H7675 | standalone |
| 8 | say | verb | `HVqrmsa HSp3ms` | Qal | H0559 H9023 | H0559 | standalone |
| 9 | heart | noun | `HNcmsc HR` |  | H3820A H9003 | H3820 | process-qualifier |
| 10 | Who | pronoun | `HPi HSp3ms` |  | H4310 H9023 | H4310 | — (NULL) |
| 11 | down | verb | `HVhi3ms` | Hiphil | H3381 | H3381 | standalone |
| 12 | ground | noun | `HNcfsa HSp1bs` |  | H0776H H9030 | H0776 | standalone |

## Num 7:59  — Numbers (prose/law)

> Num 7:59 and for the sacrifice of peace offerings , two oxen , five rams , five male goats , and five male lambs a year old . This was the offering of Gamaliel the son of Pedahzur .

| wi | surface | pos | morph_code | stem | strongs | primary | role (master) |
|--:|---|---|---|---|---|---|---|
| 0 | sacrifice | noun | `HNcmsc HC HR` |  | H2077 H9002 H9005 | H2077 | — (NULL) |
| 1 | peace offerings | noun | `HNcmpa HTd` |  | H8002 H9009 | H8002 | — (NULL) |
| 2 | two | adjective | `HAcbda` |  | H8147 | H8147 | — (NULL) |
| 3 | oxen | noun | `HNcbsa` |  | H1241 | H1241 | — (NULL) |
| 4 | five | adjective | `HAcbsa` |  | H2568 | H2568 | — (NULL) |
| 5 | rams | noun | `HNcmpa` |  | H0352A | H0352 | — (NULL) |
| 6 | five | adjective | `HAcbsa` |  | H2568 | H2568 | — (NULL) |
| 7 | male goats | noun | `HNcmpa` |  | H6260 | H6260 | — (NULL) |
| 8 | five | adjective | `HAcbsa` |  | H2568 | H2568 | — (NULL) |
| 9 | male lambs | noun | `HNcmpa` |  | H3532 | H3532 | — (NULL) |
| 10 | year | noun | `HNcfsa` |  | H8141 | H8141 | — (NULL) |
| 11 | old | noun | `HNcmpc` |  | H1121H | H1121 | — (NULL) |
| 12 | This | particle | `HTm` |  | H2088 | H2088 | — (NULL) |
| 13 | offering | noun | `HNcmsc` |  | H7133A | H7133 | — (NULL) |
| 14 | Gamaliel | noun | `HNpm` |  | H1583 | H1583 | — (NULL) |
| 15 | son | noun | `HNcmsc` |  | H1121A | H1121 | — (NULL) |
| 16 | Pedahzur | noun | `HNpm` |  | H6301 | H6301 | — (NULL) |

---

# Candidate characteristics by list-match (method test — inclusive of synonyms)

> New method (existing roles ignored): judge each span's **meaning** (gloss/definition) against the `characteristic` table (277 active), **casting the net wide across synonyms**. A span yields a **set** of candidate characteristics — every list entry it plausibly matches — which the verse-sense gate then narrows. Recall-oriented on purpose: the list-match maximises candidates; the verse read is the precision step. Match is on *meaning*, not surface.

### Verses with candidates (span → full candidate set)

**Exo 26:31** — 1 candidate span
- `skillfully` (H2803, devise/think/plan/esteem) → M15 *Deliberative planning, counsel & purposive intent* · M15 *Meditative/reflective inner activity* · M15 *Inner thought-content*  ⚠ weak (craft context)

**Psa 132:13** — 2 candidate spans
- `desired` (H0183, desire/incline/covet/long) → M28 *Longing / thirst* · M28 *Craving / disordered appetite* · M28 *The insatiable* · M28 *Satisfied desire* · M28 *Consolidated desire (the one thing)*
- `chosen` (H0977, choose/elect/decide) → M15 *Deliberative planning & purposive intent* (will/choice)  ⚠ weak

**Pro 28:6** — 3 candidate spans
- `integrity` (H8537, integrity/completeness) → M12 *Blamelessness / integrity of walk* · M12 *Purity of heart* · M12 *Innocence / clean hands* · M13 *Faithfulness / steadfastness*
- `crooked` (H6141, twisted/perverse) → M10 *Perversion as inner inversion* · M10 *Wickedness as settled identity* · M10 *Injustice as moral failure* · M14 *The double / divided heart*
- `Better` (H2896, good/pleasant) → M39 *Goodness*  ⚠ weak (comparative here)

**Song 1:2** — 2 candidate spans
- `love` (H1730, dodim/beloved) → M05 *Love / affectionate attachment* · M28 *Longing / desire* (dodim = desire/lovemaking)
- `kiss(es)` (H5401/H5390) → M05 *Love* (physical expression)  ⚠ weak

**Isa 41:2** — 3 candidate spans
- `victory` (H6664, *tsedeq* = righteousness/justice) → M26 *God Righteousness* · M26 *Human Righteousness* · M26 *Moral Uprightness* · M26 *Justification* · M26 *Avenging Justice / vindication* (best fit in context)
- `stirred up` (H5782, rouse/incite) → M23 *Courage / taking heart* · M02 *Zeal / provocation*  ⚠ weak
- `tramples` (H7287, rule/dominion) → M08 *Pride of power and position*  ⚠ weak

**Eze 6:10** — 2 candidate spans
- `know` (H3045, covenantal knowing) → M15 *Knowledge as covenantal knowing* · M15 *Understanding as inner perceptive faculty* · M15 *Discernment & practical judgment*
- `evil` (H7451, bad/harmful) → M10 *Evil as constitutional inner nature* · M10 *Wickedness as settled identity*  ⚠ **context-divergent** (here = calamity, not moral evil)

**Obd 3** — 3 candidate spans
- `pride` (H2087, arrogance/insolence/presumptuousness) → M08 *Arrogant self-elevation* · M08 *Settled pride* · M08 *Presumptuous defiance* · M08 *Insolence / contempt toward others* · M08 *Boasting and self-display* · M08 *Vain conceit* · M08 *Pride of power and position*
- `heart` (H3820, inner man/mind/will/heart/understanding) → M47 *Heart (leb/lebab)* · M47 *Inmost being* · M15 *Understanding as inner perceptive faculty* (heart = mind)
- `deceived` (H5377, beguile/deceive) → M14 *Deceit / guile* · M14 *The masking heart* · M14 *The double / divided heart* · M14 *Flattery* (here: self-deception)

### Verses with NO candidate (correctly abstains)
- **Gen 11:10** (genealogy) · **Eze 46:8** (temple procedure) · **Num 7:59** (offering list)

## What the corrected test shows
1. **Most candidate spans map to a SET, not one** — `pride` → 7 pride variants, `desired` → 5 desire variants, `know` → 3 knowledge faculties, `integrity` → 3–4. That is the intended behaviour: the fine-grained list returns everything in the semantic field, and the verse narrows it.
2. **Verses carry multiple characteristics** — Obd 3 = pride + heart + deceit (3 fields, ~14 candidate entries); Pro 28:6 = integrity + perversion (+goodness); Isa 41:2 = righteousness (5 entries).
3. **Recall vs precision split is clean** — the list-match is deliberately generous (all plausible matches); the verse-sense gate is where a span collapses from "7 pride variants" to the one it actually is (or to qualifier/standalone).
4. **Still abstains correctly** — the 3 non-IB verses yield nothing even with the wide net.
5. **Synonym-inclusive is doing the work** — surface "victory"→righteousness(M26), "arrogance"→pride(M08); none would string-match.

## Implication
The identifier's real output is a **candidate-characteristic vector per span** (often several list entries), not a single label. That vector is the input the verse read then resolves — which characteristic (if any) the span actually instantiates, and in what role.
