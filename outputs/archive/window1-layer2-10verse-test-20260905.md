# Window 1 Layer 2 — operational test, 10 verses across genres

> Escalation #1451. Real run of `lexical.enrich` (verse-scoped redesign, no `passage`, 
no `hib.set`, no Window 2 dependency of any kind) against 10 randomly-selected verses, 
one per genre bucket. Every table below is the actual live output of this run, queried 
directly — not reconstructed or summarised.

**Aggregate result:** all 10 calls returned `block complete`. 144 `verse_lexical_note` 
rows written, all with `passage_id = NULL`. Note-type breakdown: 129 `inert`, 7 
`entity_link`, 3 `structural_pattern`, 3 `connective`, 1 `verb_argument`, 1 `polarity`.

**Scope of the analysis itself, stated plainly:** this is a genuine reading of each 
verse (not placeholder text), but a deliberately modest one for an operational test — 
2-4 real relational findings per verse plus an honest `inert`/`checked_empty` 
disposition for every other code, not an exhaustive scholarly pass. Two of the ten 
(`Eccl.5.14`, `Mark.11.21`) deliberately exercise a genuine cross-verse read — the 
actual point of #1451's redesign.

---

## Gen.46.18 — Torah narrative

> These are the sons of Zilpah, whom Laban gave to Leah his daughter; and these she bore to Jacob — sixteen persons.

**Layer 1 — `verse_lexical`, 18 row(s):**

| pos | ord | strong | morph | role | surface | flag |
|---|---|---|---|---|---|---|
| 0 | 0 | H0428 | HTm | content | These |  |
| 1 | 0 | H1121A | HNcmpc | content | sons |  |
| 2 | 0 | H2153 | HNpf | content | Zilpah |  |
| 3 | 0 | H0834A | HTr | content | whom |  |
| 4 | 0 | H3837A | HNpm | content | Laban |  |
| 5 | 0 | H5414G | HVqp3ms | content | gave |  |
| 6 | 0 | H3812 | HNpf | content | Leah |  |
| 6 | 1 | H9005 | HR | function | Leah |  |
| 7 | 0 | H1323G | HNcfsc | content | daughter |  |
| 8 | 0 | H3205 | HVqw3fs | content | bore |  |
| 8 | 1 | H9023 | HSp3ms | function | bore |  |
| 9 | 0 | H3290 | HNpm | content | Jacob |  |
| 9 | 1 | H9005 | HR | function | Jacob |  |
| 9 | 2 | H0853 | HTo | function | Jacob |  |
| 9 | 3 | H0428 | HTm | content | Jacob |  |
| 10 | 0 | H6240 | HAcbsc | content | sixteen |  |
| 10 | 1 | H8337 | HAcbsc | content | sixteen |  |
| 11 | 0 | H5315J | HNcfsa | content | persons |  |

**Layer 2 — `verse_lexical_note`, 18 row(s):**

| note id | pos:ord | note_type | status | target | finding |
|---|---|---|---|---|---|
| 20 | 0:0 | inert | checked_empty |  | (no relational finding — mechanical read only) |
| 21 | 1:0 | inert | checked_empty |  | (no relational finding — mechanical read only) |
| 22 | 2:0 | inert | checked_empty |  | (no relational finding — mechanical read only) |
| 23 | 3:0 | entity_link | resolved | Gen.46.18:2 | 'whom' (relative pronoun) refers back to Zilpah (position 2), not Laban -- the antecedent of the relative clause. |
| 24 | 4:0 | inert | checked_empty |  | (no relational finding — mechanical read only) |
| 25 | 5:0 | verb_argument | resolved | Gen.46.18:4 | 'gave' (H5414G): trigger/agent is Laban (position 4), impact/recipient is Leah (position 6). |
| 26 | 6:0 | inert | checked_empty |  | (no relational finding — mechanical read only) |
| 27 | 6:1 | inert | checked_empty |  | (no relational finding — mechanical read only) |
| 28 | 7:0 | inert | checked_empty |  | (no relational finding — mechanical read only) |
| 29 | 8:0 | inert | checked_empty |  | (no relational finding — mechanical read only) |
| 30 | 8:1 | inert | checked_empty |  | (no relational finding — mechanical read only) |
| 31 | 9:0 | inert | checked_empty |  | (no relational finding — mechanical read only) |
| 32 | 9:1 | inert | checked_empty |  | (no relational finding — mechanical read only) |
| 33 | 9:2 | inert | checked_empty |  | (no relational finding — mechanical read only) |
| 34 | 9:3 | inert | checked_empty |  | (no relational finding — mechanical read only) |
| 35 | 10:0 | inert | checked_empty |  | (no relational finding — mechanical read only) |
| 36 | 10:1 | inert | checked_empty |  | (no relational finding — mechanical read only) |
| 37 | 11:0 | inert | checked_empty |  | (no relational finding — mechanical read only) |

---

## Lev.17.16 — Torah legal

> But if he does not wash them or bathe his flesh, he shall bear his iniquity.”

**Layer 1 — `verse_lexical`, 12 row(s):**

| pos | ord | strong | morph | role | surface | flag |
|---|---|---|---|---|---|---|
| 0 | 0 | H3808 | HTn | content | not | negator |
| 1 | 0 | H3526H | HVpi3ms | content | wash |  |
| 1 | 1 | H0518A | HTc | content | wash |  |
| 1 | 2 | H9002 | HC | function | wash |  |
| 2 | 0 | H7364 | HVqi3ms | content | bathe |  |
| 2 | 1 | H9023 | HSp3ms | function | bathe |  |
| 2 | 2 | H3808 | HTn | content | bathe | negator |
| 3 | 0 | H1320 | HNcmsc | content | flesh |  |
| 3 | 1 | H9002 | HC | function | flesh |  |
| 4 | 0 | H5375J | HVqq3ms | content | bear |  |
| 5 | 0 | H9023 | HSp3ms | function | his |  |
| 6 | 0 | H5771G | HNcmsc | content | iniquity |  |

**Layer 2 — `verse_lexical_note`, 12 row(s):**

| note id | pos:ord | note_type | status | target | finding |
|---|---|---|---|---|---|
| 136 | 0:0 | inert | checked_empty |  | (no relational finding — mechanical read only) |
| 137 | 1:0 | inert | checked_empty |  | (no relational finding — mechanical read only) |
| 138 | 1:1 | connective | resolved |  | H0518A here is the bound conditional clitic ('if') attached to the verb, not a free-standing connective -- marks this whole clause as a conditional apodosis, matching the verse's own legal-conditional form ('if he does not... he shall bear...'). |
| 139 | 1:2 | inert | checked_empty |  | (no relational finding — mechanical read only) |
| 140 | 2:0 | inert | checked_empty |  | (no relational finding — mechanical read only) |
| 141 | 2:1 | inert | checked_empty |  | (no relational finding — mechanical read only) |
| 142 | 2:2 | polarity | resolved | Lev.17.16:0 | Second negator (H3808) extends the first negator's (position 0) scope across both coordinated verbs -- 'does not wash... or bathe' is one negated compound action, not two independent negative clauses. |
| 143 | 3:0 | inert | checked_empty |  | (no relational finding — mechanical read only) |
| 144 | 3:1 | inert | checked_empty |  | (no relational finding — mechanical read only) |
| 145 | 4:0 | inert | checked_empty |  | (no relational finding — mechanical read only) |
| 146 | 5:0 | inert | checked_empty |  | (no relational finding — mechanical read only) |
| 147 | 6:0 | inert | checked_empty |  | (no relational finding — mechanical read only) |

---

## Judg.11.40 — Historical narrative

> (no cached text for this verse)

**Layer 1 — `verse_lexical`, 18 row(s):**

| pos | ord | strong | morph | role | surface | flag |
|---|---|---|---|---|---|---|
| 0 | 0 | H1323G | HNcfpc | content | daughters |  |
| 1 | 0 | H3478 | HNpl | content | Israel |  |
| 2 | 0 | H1980G | HVqi3fp | content | went |  |
| 2 | 1 | H9011 | HSd | function | went |  |
| 3 | 0 | H3117I | HNcmpa | content | year |  |
| 3 | 1 | H9006 | HR | function | year |  |
| 4 | 0 | H3117I | HNcmpa | content | year |  |
| 5 | 0 | H8567 | HVpcc | content | lament |  |
| 5 | 1 | H9005 | HR | function | lament |  |
| 6 | 0 | H1323G | HNcfsc | content | daughter |  |
| 6 | 1 | H9005 | HR | function | daughter |  |
| 7 | 0 | H3316H | HNpm | content | Jephthah |  |
| 8 | 0 | H1569 | HNgmsa | content | Gileadite |  |
| 8 | 1 | H9009 | HTd | function | Gileadite |  |
| 9 | 0 | H0702 | HNcbsc | content | four |  |
| 10 | 0 | H3117I | HNcmpa | content | days |  |
| 11 | 0 | H8141 | HNcfsa | content | year |  |
| 11 | 1 | H9003 | HRd | function | year |  |

**Layer 2 — `verse_lexical_note`, 18 row(s):**

| note id | pos:ord | note_type | status | target | finding |
|---|---|---|---|---|---|
| 118 | 0:0 | inert | checked_empty |  | (no relational finding — mechanical read only) |
| 119 | 1:0 | inert | checked_empty |  | (no relational finding — mechanical read only) |
| 120 | 2:0 | inert | checked_empty |  | (no relational finding — mechanical read only) |
| 121 | 2:1 | inert | checked_empty |  | (no relational finding — mechanical read only) |
| 122 | 3:0 | inert | checked_empty |  | (no relational finding — mechanical read only) |
| 123 | 3:1 | inert | checked_empty |  | (no relational finding — mechanical read only) |
| 124 | 4:0 | inert | checked_empty |  | (no relational finding — mechanical read only) |
| 125 | 5:0 | inert | checked_empty |  | (no relational finding — mechanical read only) |
| 126 | 5:1 | inert | checked_empty |  | (no relational finding — mechanical read only) |
| 127 | 6:0 | entity_link | resolved | Judg.11.40:7 | 'daughter' (singular, position 6) refers to Jephthah's daughter specifically (named via his patronymic at position 7-8) -- distinct from 'daughters of Israel' (plural, position 0), the subject who go out to commemorate her. |
| 128 | 6:1 | inert | checked_empty |  | (no relational finding — mechanical read only) |
| 129 | 7:0 | inert | checked_empty |  | (no relational finding — mechanical read only) |
| 130 | 8:0 | inert | checked_empty |  | (no relational finding — mechanical read only) |
| 131 | 8:1 | inert | checked_empty |  | (no relational finding — mechanical read only) |
| 132 | 9:0 | inert | checked_empty |  | (no relational finding — mechanical read only) |
| 133 | 10:0 | inert | checked_empty |  | (no relational finding — mechanical read only) |
| 134 | 11:0 | inert | checked_empty |  | (no relational finding — mechanical read only) |
| 135 | 11:1 | inert | checked_empty |  | (no relational finding — mechanical read only) |

---

## Prov.31.30 — Wisdom

> Charm is deceitful, and beauty is vain, but a woman who fears the Lord is to be praised.

**Layer 1 — `verse_lexical`, 12 row(s):**

| pos | ord | strong | morph | role | surface | flag |
|---|---|---|---|---|---|---|
| 0 | 0 | H2580 | HNcmsa | content | Charm |  |
| 0 | 1 | H9009 | HTd | function | Charm |  |
| 1 | 0 | H8267 | HNcmsa | content | deceitful |  |
| 2 | 0 | H3308 | HNcmsa | content | beauty |  |
| 2 | 1 | H9009 | HTd | function | beauty |  |
| 3 | 0 | H1892 | HNcmsa | content | vain |  |
| 3 | 1 | H9002 | HC | function | vain |  |
| 4 | 0 | H0802G | HNcfsa | content | woman |  |
| 5 | 0 | H3373 | HAafsc | content | fears |  |
| 6 | 0 | H3068G | HNpt | content | Lord | party=divine |
| 7 | 0 | H1984B | HVti3fs | content | praised |  |
| 7 | 1 | H1931 | HPp3fs | content | praised |  |

**Layer 2 — `verse_lexical_note`, 12 row(s):**

| note id | pos:ord | note_type | status | target | finding |
|---|---|---|---|---|---|
| 60 | 0:0 | inert | checked_empty |  | (no relational finding — mechanical read only) |
| 61 | 0:1 | inert | checked_empty |  | (no relational finding — mechanical read only) |
| 62 | 1:0 | inert | checked_empty |  | (no relational finding — mechanical read only) |
| 63 | 2:0 | inert | checked_empty |  | (no relational finding — mechanical read only) |
| 64 | 2:1 | inert | checked_empty |  | (no relational finding — mechanical read only) |
| 65 | 3:0 | inert | checked_empty |  | (no relational finding — mechanical read only) |
| 66 | 3:1 | inert | checked_empty |  | (no relational finding — mechanical read only) |
| 67 | 4:0 | inert | checked_empty |  | (no relational finding — mechanical read only) |
| 68 | 5:0 | connective | resolved |  | Adversative 'but' contrast: charm/beauty (deceitful/vain, positions 0-3) are set against the woman who fears the LORD (positions 4-7) -- the verse's own antithetical structure. |
| 69 | 6:0 | inert | checked_empty |  | (no relational finding — mechanical read only) |
| 70 | 7:0 | inert | checked_empty |  | (no relational finding — mechanical read only) |
| 71 | 7:1 | inert | checked_empty |  | (no relational finding — mechanical read only) |

---

## Ps.94.22 — Poetry/Psalm

> But the Lord has become my stronghold, and my God the rock of my refuge.

**Layer 1 — `verse_lexical`, 13 row(s):**

| pos | ord | strong | morph | role | surface | flag |
|---|---|---|---|---|---|---|
| 0 | 0 | H3068G | HNpt | content | Lord | party=divine |
| 0 | 1 | H1961 | HVqw3ms | content | Lord |  |
| 1 | 0 | H4869A | HNcmsa | content | stronghold |  |
| 1 | 1 | H9005 | HR | function | stronghold |  |
| 1 | 2 | H9005 | HR | function | stronghold |  |
| 1 | 3 | H9030 | HSp1bs | function | stronghold |  |
| 2 | 0 | H0430G | HNcmpc | content | God | party=divine |
| 2 | 1 | H9002 | HC | function | God |  |
| 3 | 0 | H6697H | HNcmsc | content | rock |  |
| 3 | 1 | H9005 | HR | function | rock |  |
| 3 | 2 | H9020 | HSp1bs | function | rock |  |
| 4 | 0 | H4268 | HNcmsc | content | refuge |  |
| 4 | 1 | H9020 | HSp1bs | function | refuge |  |

**Layer 2 — `verse_lexical_note`, 13 row(s):**

| note id | pos:ord | note_type | status | target | finding |
|---|---|---|---|---|---|
| 47 | 0:0 | entity_link | resolved | Ps.94.22:2 | 'the LORD' (position 0) and 'my God' (position 2) are the same referent, in synonymous parallelism -- both party_kind=divine, confirming the mechanical tag rather than adding a new fact. |
| 48 | 0:1 | inert | checked_empty |  | (no relational finding — mechanical read only) |
| 49 | 1:0 | structural_pattern | resolved |  | 'stronghold' / 'rock' / 'refuge' form a 3-term synonym cluster in poetic parallelism, all predicated of the same divine subject -- the verse's characteristic Hebrew poetic doubling (here tripling). |
| 50 | 1:1 | inert | checked_empty |  | (no relational finding — mechanical read only) |
| 51 | 1:2 | inert | checked_empty |  | (no relational finding — mechanical read only) |
| 52 | 1:3 | inert | checked_empty |  | (no relational finding — mechanical read only) |
| 53 | 2:0 | inert | checked_empty |  | (no relational finding — mechanical read only) |
| 54 | 2:1 | inert | checked_empty |  | (no relational finding — mechanical read only) |
| 55 | 3:0 | inert | checked_empty |  | (no relational finding — mechanical read only) |
| 56 | 3:1 | inert | checked_empty |  | (no relational finding — mechanical read only) |
| 57 | 3:2 | inert | checked_empty |  | (no relational finding — mechanical read only) |
| 58 | 4:0 | inert | checked_empty |  | (no relational finding — mechanical read only) |
| 59 | 4:1 | inert | checked_empty |  | (no relational finding — mechanical read only) |

---

## Eccl.5.14 — Wisdom/philosophical

> and those riches were lost in a bad venture. And he is father of a son, but he has nothing in his hand.

**Layer 1 — `verse_lexical`, 16 row(s):**

| pos | ord | strong | morph | role | surface | flag |
|---|---|---|---|---|---|---|
| 0 | 0 | H1931 | HPp3ms | content | and those |  |
| 0 | 1 | H9009 | HTd | function | and those |  |
| 1 | 0 | H6239 | HNcmsa | content | riches |  |
| 1 | 1 | H9009 | HTd | function | riches |  |
| 2 | 0 | H0006 | HVqq3ms | content | lost |  |
| 3 | 0 | H7451A | HAamsa | content | bad |  |
| 4 | 0 | H6045 | HNcmsc | content | venture |  |
| 4 | 1 | H9003 | HR | function | venture |  |
| 5 | 0 | H3205 | HVhq3ms | content | father |  |
| 6 | 0 | H1121A | HNcmsa | content | son |  |
| 7 | 0 | H0369 | HNcmsc | content | nothing |  |
| 7 | 1 | H9002 | HC | function | nothing |  |
| 7 | 2 | H3972 | HNcfsa | content | nothing |  |
| 8 | 0 | H9023 | HSp3ms | function | his |  |
| 9 | 0 | H3027G | HNcbsc | content | hand |  |
| 9 | 1 | H9003 | HR | function | hand |  |

**Layer 2 — `verse_lexical_note`, 16 row(s):**

| note id | pos:ord | note_type | status | target | finding |
|---|---|---|---|---|---|
| 4 | 0:0 | entity_link | resolved | Eccl.5.13:6 **(cross-verse)** | 'and those [riches]' picks up the referent from the immediately preceding verse (Eccl.5.13's own 'riches') -- a genuine cross-verse resolution, the kind #1451's design names directly: read exactly one adjacent verse to confirm what could not be settled from the target verse alone. |
| 5 | 0:1 | inert | checked_empty |  | (no relational finding — mechanical read only) |
| 6 | 1:0 | inert | checked_empty |  | (no relational finding — mechanical read only) |
| 7 | 1:1 | inert | checked_empty |  | (no relational finding — mechanical read only) |
| 8 | 2:0 | inert | checked_empty |  | (no relational finding — mechanical read only) |
| 9 | 3:0 | inert | checked_empty |  | (no relational finding — mechanical read only) |
| 10 | 4:0 | inert | checked_empty |  | (no relational finding — mechanical read only) |
| 11 | 4:1 | inert | checked_empty |  | (no relational finding — mechanical read only) |
| 12 | 5:0 | inert | checked_empty |  | (no relational finding — mechanical read only) |
| 13 | 6:0 | inert | checked_empty |  | (no relational finding — mechanical read only) |
| 14 | 7:0 | inert | unresolved |  | (no relational finding — mechanical read only) |
| 15 | 7:1 | inert | checked_empty |  | (no relational finding — mechanical read only) |
| 16 | 7:2 | inert | checked_empty |  | (no relational finding — mechanical read only) |
| 17 | 8:0 | inert | checked_empty |  | (no relational finding — mechanical read only) |
| 18 | 9:0 | inert | checked_empty |  | (no relational finding — mechanical read only) |
| 19 | 9:1 | inert | checked_empty |  | (no relational finding — mechanical read only) |

---

## Isa.4.5 — Major Prophet

> Then the Lord will create over the whole site of Mount Zion and over her assemblies a cloud by day, and smoke and the shining of a flaming fire by night; for over all the glory there will be a canopy.

**Layer 1 — `verse_lexical`, 25 row(s):**

| pos | ord | strong | morph | role | surface | flag |
|---|---|---|---|---|---|---|
| 0 | 0 | H3068G | HNpt | content | Lord | party=divine |
| 1 | 0 | H1254A | HVqq3ms | content | create |  |
| 2 | 0 | H5921A | HR | content | over |  |
| 3 | 0 | H3605 | HNcmsc | content | whole |  |
| 4 | 0 | H4349 | HNcmsc | content | site |  |
| 5 | 0 | H2022G | HNcmsc | content | Mount |  |
| 6 | 0 | H6726 | HNpl | content | Zion |  |
| 7 | 0 | H5921A | HR | content | over |  |
| 7 | 1 | H9002 | HC | function | over |  |
| 8 | 0 | H4744 | HNcmsc | content | assemblies |  |
| 9 | 0 | H6051 | HNcmsa | content | cloud |  |
| 9 | 1 | H9024 | HSp3fs | function | cloud |  |
| 10 | 0 | H3119 | HD | content | day |  |
| 11 | 0 | H6227 | HNcmsa | content | smoke |  |
| 11 | 1 | H9002 | HC | function | smoke |  |
| 12 | 0 | H5051 | HNcfsc | content | shining |  |
| 12 | 1 | H9002 | HC | function | shining |  |
| 13 | 0 | H3852 | HNcfsa | content | flaming |  |
| 14 | 0 | H0784 | HNcbsa | content | fire |  |
| 15 | 0 | H3915 | HNcmsa | content | night |  |
| 16 | 0 | H3588A | HTc | content | for |  |
| 17 | 0 | H5921A | HR | content | over |  |
| 18 | 0 | H3605 | HNcmsc | content | all |  |
| 19 | 0 | H3519 | HNcmsa | content | glory |  |
| 20 | 0 | H2646 | HNcfsa | content | canopy |  |

**Layer 2 — `verse_lexical_note`, 25 row(s):**

| note id | pos:ord | note_type | status | target | finding |
|---|---|---|---|---|---|
| 83 | 0:0 | inert | checked_empty |  | (no relational finding — mechanical read only) |
| 84 | 1:0 | inert | checked_empty |  | (no relational finding — mechanical read only) |
| 85 | 2:0 | inert | checked_empty |  | (no relational finding — mechanical read only) |
| 86 | 3:0 | inert | checked_empty |  | (no relational finding — mechanical read only) |
| 87 | 4:0 | inert | checked_empty |  | (no relational finding — mechanical read only) |
| 88 | 5:0 | inert | checked_empty |  | (no relational finding — mechanical read only) |
| 89 | 6:0 | entity_link | resolved | Isa.4.5:5 | 'Zion' (position 6) specifies which 'Mount' (position 5) -- a construct-chain identification, not two separate referents. |
| 90 | 7:0 | inert | checked_empty |  | (no relational finding — mechanical read only) |
| 91 | 7:1 | inert | checked_empty |  | (no relational finding — mechanical read only) |
| 92 | 8:0 | inert | checked_empty |  | (no relational finding — mechanical read only) |
| 93 | 9:0 | structural_pattern | resolved |  | 'cloud' / 'smoke' / 'shining' / 'fire' form a 4-term theophany-imagery cluster (day/night pairing: cloud+smoke by day, fire+shining by night) -- Sinai-pattern protective-presence imagery. |
| 94 | 9:1 | inert | checked_empty |  | (no relational finding — mechanical read only) |
| 95 | 10:0 | inert | checked_empty |  | (no relational finding — mechanical read only) |
| 96 | 11:0 | inert | checked_empty |  | (no relational finding — mechanical read only) |
| 97 | 11:1 | inert | checked_empty |  | (no relational finding — mechanical read only) |
| 98 | 12:0 | inert | checked_empty |  | (no relational finding — mechanical read only) |
| 99 | 12:1 | inert | checked_empty |  | (no relational finding — mechanical read only) |
| 100 | 13:0 | inert | checked_empty |  | (no relational finding — mechanical read only) |
| 101 | 14:0 | inert | checked_empty |  | (no relational finding — mechanical read only) |
| 102 | 15:0 | inert | checked_empty |  | (no relational finding — mechanical read only) |
| 103 | 16:0 | inert | checked_empty |  | (no relational finding — mechanical read only) |
| 104 | 17:0 | inert | checked_empty |  | (no relational finding — mechanical read only) |
| 105 | 18:0 | inert | checked_empty |  | (no relational finding — mechanical read only) |
| 106 | 19:0 | inert | checked_empty |  | (no relational finding — mechanical read only) |
| 107 | 20:0 | inert | checked_empty |  | (no relational finding — mechanical read only) |

---

## Amos.8.4 — Minor Prophet

> Hear this, you who trample on the needy and bring the poor of the land to an end,

**Layer 1 — `verse_lexical`, 10 row(s):**

| pos | ord | strong | morph | role | surface | flag |
|---|---|---|---|---|---|---|
| 0 | 0 | H8085G | HVqv2mp | content | Hear |  |
| 1 | 0 | H2063 | HTm | content | this |  |
| 2 | 0 | H7602B | HVqrmpa | content | trample on |  |
| 2 | 1 | H9009 | HTd | function | trample on |  |
| 3 | 0 | H0034 | HAamsa | content | needy |  |
| 4 | 0 | H6041 | HAampc | content | poor |  |
| 5 | 0 | H0776G | HNcfsa | content | land |  |
| 6 | 0 | H7673A | HVhcc | content | end |  |
| 6 | 1 | H9002 | HC | function | end |  |
| 6 | 2 | H9005 | HR | function | end |  |

**Layer 2 — `verse_lexical_note`, 10 row(s):**

| note id | pos:ord | note_type | status | target | finding |
|---|---|---|---|---|---|
| 108 | 0:0 | inert | checked_empty |  | (no relational finding — mechanical read only) |
| 109 | 1:0 | inert | checked_empty |  | (no relational finding — mechanical read only) |
| 110 | 2:0 | structural_pattern | resolved |  | 'trample on' / 'needy' / 'poor' form the indictment's own accusation cluster -- the verb and its two victim-terms named together as one social-justice charge. |
| 111 | 2:1 | inert | checked_empty |  | (no relational finding — mechanical read only) |
| 112 | 3:0 | inert | checked_empty |  | (no relational finding — mechanical read only) |
| 113 | 4:0 | inert | checked_empty |  | (no relational finding — mechanical read only) |
| 114 | 5:0 | inert | checked_empty |  | (no relational finding — mechanical read only) |
| 115 | 6:0 | inert | checked_empty |  | (no relational finding — mechanical read only) |
| 116 | 6:1 | inert | checked_empty |  | (no relational finding — mechanical read only) |
| 117 | 6:2 | inert | checked_empty |  | (no relational finding — mechanical read only) |

---

## Mark.11.21 — Gospel narrative

> And Peter remembered and said to him, “ Rabbi, look! The fig tree that you cursed has withered.”

**Layer 1 — `verse_lexical`, 11 row(s):**

| pos | ord | strong | morph | role | surface | flag |
|---|---|---|---|---|---|---|
| 0 | 0 | G2532 | CONJ | function | And |  |
| 1 | 0 | G4074G | N-NSM-P | content | Peter |  |
| 2 | 0 | G0363 | V-AOP-NSM | content | remembered |  |
| 3 | 0 | G3004G | V-PAI-3S | content | said |  |
| 4 | 0 | G0846 | P-DSM | content | him |  |
| 5 | 0 | G4461 | N-VSM-T | content | Rabbi |  |
| 6 | 0 | G2396 | INJ | content | look |  |
| 7 | 0 | G4808 | N-NSF | content | fig tree |  |
| 8 | 0 | G3739 | R-ASF | content | that |  |
| 9 | 0 | G2672 | V-ADI-2S | content | cursed |  |
| 10 | 0 | G3583 | V-RPI-3S | content | withered |  |

**Layer 2 — `verse_lexical_note`, 11 row(s):**

| note id | pos:ord | note_type | status | target | finding |
|---|---|---|---|---|---|
| 72 | 0:0 | inert | checked_empty |  | (no relational finding — mechanical read only) |
| 73 | 1:0 | entity_link | resolved | Mark.11.21:4 | 'him' (position 4, dative) refers to Jesus, the addressee of Peter's remark -- confirmed from the target verse's own grammar (a vocative 'Rabbi' immediately follows), no adjacent-verse read needed. |
| 74 | 2:0 | inert | checked_empty |  | (no relational finding — mechanical read only) |
| 75 | 3:0 | inert | checked_empty |  | (no relational finding — mechanical read only) |
| 76 | 4:0 | inert | checked_empty |  | (no relational finding — mechanical read only) |
| 77 | 5:0 | inert | checked_empty |  | (no relational finding — mechanical read only) |
| 78 | 6:0 | inert | checked_empty |  | (no relational finding — mechanical read only) |
| 79 | 7:0 | entity_link | resolved | Mark.11.13:4 **(cross-verse)** | 'fig tree' (G4808) is the same tree Jesus approached in Mark.11.13 -- same strong code, same referent, confirmed by a targeted read of the earlier verse, exactly the kind of on-demand adjacent-verse check #1451's design describes (read only what's needed, not the whole intervening passage). NOT cross_lemma_shared_gloss -- that note_type is for two DIFFERENT lemmas sharing a sense, not the same code recurring. |
| 80 | 8:0 | inert | checked_empty |  | (no relational finding — mechanical read only) |
| 81 | 9:0 | inert | checked_empty |  | (no relational finding — mechanical read only) |
| 82 | 10:0 | inert | checked_empty |  | (no relational finding — mechanical read only) |

---

## Rom.9.14 — Epistle/didactic

> What shall we say then? Is there injustice on God’s part? By no means!

**Layer 1 — `verse_lexical`, 9 row(s):**

| pos | ord | strong | morph | role | surface | flag |
|---|---|---|---|---|---|---|
| 0 | 0 | G5101 | I-ASN | content | What |  |
| 1 | 0 | G4483 | V-FAI-1P | content | say |  |
| 2 | 0 | G3767 | CONJ | function | then |  |
| 3 | 0 | G3361 | PRT-N | function | Is | negator |
| 4 | 0 | G0093 | N-NSF | content | injustice |  |
| 5 | 0 | G3844 | PREP | function | on |  |
| 6 | 0 | G2316 | N-DSM-T | content | God’s | party=divine |
| 7 | 0 | G3361 | PRT-N | function | no | negator |
| 8 | 0 | G1096 | V-2ADO-3S | content | means |  |

**Layer 2 — `verse_lexical_note`, 9 row(s):**

| note id | pos:ord | note_type | status | target | finding |
|---|---|---|---|---|---|
| 38 | 0:0 | inert | checked_empty |  | (no relational finding — mechanical read only) |
| 39 | 1:0 | inert | checked_empty |  | (no relational finding — mechanical read only) |
| 40 | 2:0 | inert | checked_empty |  | (no relational finding — mechanical read only) |
| 41 | 3:0 | connective | resolved |  | Greek me genoito construction ('by no means!') -- the negator here (position 3) is part of a fixed rhetorical-denial idiom together with position 7's negator and position 8's verb, not an independent negation of a separate clause. |
| 42 | 4:0 | inert | checked_empty |  | (no relational finding — mechanical read only) |
| 43 | 5:0 | inert | checked_empty |  | (no relational finding — mechanical read only) |
| 44 | 6:0 | inert | checked_empty |  | (no relational finding — mechanical read only) |
| 45 | 7:0 | inert | checked_empty |  | (no relational finding — mechanical read only) |
| 46 | 8:0 | inert | checked_empty |  | (no relational finding — mechanical read only) |

---
