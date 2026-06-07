# Cross-cluster gloss analytics

_Generated: 2026-05-26 14:27 UTC_  
_Source: `database/bible_research.db` — `mti_terms.gloss`_  
_Scope: 1752 non-T2 active terms across 47 clusters_

**Purpose:** surface glosses that span multiple clusters — the diagnostic for the 'characteristic-legs scattered across clusters' pattern observed during M11 Phase 3 review. Four lenses:

- §1 Exact gloss matches across clusters
- §2 Gloss-base matches across clusters (strip `: qualifier`)
- §3 Token matches across clusters (split glosses to words, exclude stop-words)
- §4 Sister-Strong's sense-suffix spread (same root, different sense letters, different clusters)

---

## §1. Exact gloss collisions (22 glosses span 2+ clusters)

Identical gloss strings appearing on terms in different clusters. These are the strongest signal that the same concept is being captured under different anchor terms.

| Gloss | Clusters | Terms |
|---|---|---|
| `abundance` | M33, M46 | H4766 mar.veh [M33], H7230 rov [M46] |
| `be good` | M04, M39 | H2868 te.ev [M04], H3190 ya.tav [M39] |
| `beloved` | FLAG, M05 | G0027 agapētos [FLAG], H1730G dod [FLAG], H1730H dod [FLAG], H3039A ya.did [FLAG], H3033 ye.di.dut [M05] |
| `bitterness` | M02, M03 | G4088 pikria [M02], H4470 me.mer [M03], H4472 mam.ror [M03], H4786 mo.rah [M03], H4787 mor.rah [M03], H4844 ma.ror [M03] |
| `evil: trouble` | M10, M10b | H0205H a.ven [M10], H0205G a.ven [M10b] |
| `greatness` | M22, M23 | H1420 ge.dul.lah [M22], H1433 go.del [M22], H4768 mar.bit [M23] |
| `judgment` | FLAG, M26 | G2920 krisis [FLAG], H1779 din [FLAG], H8201 she.phet [FLAG], H8196 she.phot [M26] |
| `justice` | FLAG, M26 | H4941H mish.pat [FLAG], G1341 dikaiokrisia [M26] |
| `pleasure` | M04, M28 | H2656 che.phets [M04], G2237 hēdonē [M28] |
| `poor` | M24, M46 | G3993 penēs [M24], H6035 a.nav [M24], G4434 ptōchos [M46] |
| `pressure` | M01, M24 | H6125 a.qah [M01], G2347 thlipsis [M24] |
| `riches` | M22, M46 | H3520B ke.vud.dah [M22], G4149 ploutos [M46], H6239 o.sher [M46] |
| `shame` | M05, M07 | H2617B che.sed [M05], G0152 aischunē [M07], G1791 entropē [M07], H0955 bu.shah [M07], H1317 bosh.nah [M07], H1322 bo.shet [M07], H3639 ke.lim.mah [M07], H3640 ke.lim.mut [M07] |
| `terror` | M01, M24 | H0367 e.mah [M01], H1091 bal.la.hah [M01], H1205 be.a.tah [M01], H2283 chag.ga [M01], H2844A chat [M01], H2847 chit.tah [M01], H2849 chat.chat [M01], H2851 chit.tit [M01], H2866 cha.tat [M01], H4032 ma.gor [M01], H4288 me.chit.tah [M01], H4637 ma.a.ra.tsah [M01], H8606 tiph.le.tset [M01], H4712 me.tsar [M24] |
| `to despair` | M18, M20 | G0560 apelpizo [M18], G1820 exaporeō [M20], H2976 ya.ash [M20] |
| `to harden` | FLAG, M30 | H7185 qa.shah [FLAG], G4456 pōroō [M30] |
| `to judge` | FLAG, M26 | G2919 krinō [FLAG], H1777 din [FLAG], H8199 sha.phat [FLAG], H8200 she.phat [M26] |
| `to provoke` | M02, M03 | G3947 paroxunō [M02], H3707 ka.as [M02], H6696B tsur [M02], H4843 ma.rar [M03] |
| `to train` | FLAG, M15 | G4994 sōfronizō [FLAG], G1128 gumnazō [M15] |
| `toil` | M03, M36 | H6089A e.tsev [M03], H6093 its.tsa.von [M03], H8383 te.u.nim [M36] |
| `torment` | M03, M35 | G0931 basanos [M03], H4620 ma.a.tse.vah [M03], G0929 basanismos [M35] |
| `wickedness` | M10, M10b | H7564 rish.ah [M10], H4849 mir.sha.at [M10b], H7562 re.sha [M10b] |

---

## §2. Gloss-base collisions (37 bases span 2+ clusters)

Stripping the `: qualifier` suffix from each gloss yields a 'base' sense. Bases appearing in multiple clusters reveal where the programme captures the same root sense across different anchor terms (often the same Strong's with sense-letter suffixes).

| Gloss base | Clusters | Term-rows |
|---|---|---|
| `to boast` | M08, M16, M22 (3 clusters, 4 term-rows) | `G2744` kauchaomai → `to boast` [M08]; `H1984H` ha.lal → `to boast: boast` [M08]; `H1984I` ha.lal → `to boast: rave madly` [M16]; `H1984B` ha.lal → `to boast: praise` [M22] |
| `abundance` | M33, M46 (2 clusters, 2 term-rows) | `H4766` mar.veh → `abundance` [M33]; `H7230` rov → `abundance` [M46] |
| `be good` | M04, M39 (2 clusters, 2 term-rows) | `H2868` te.ev → `be good` [M04]; `H3190` ya.tav → `be good` [M39] |
| `be weak` | M03, M24 (2 clusters, 3 term-rows) | `H2470I` cha.lah → `be weak: grieved` [M03]; `G0770G` astheneō → `be weak: weak` [M24]; `G0770H` astheneō → `be weak: ill` [M24] |
| `beloved` | FLAG, M05 (2 clusters, 6 term-rows) | `G0027` agapētos → `beloved` [FLAG]; `H1730G` dod → `beloved` [FLAG]; `H1730H` dod → `beloved` [FLAG]; `H1730I` dod → `beloved: male relative` [FLAG]; `H3039A` ya.did → `beloved` [FLAG]; `H3033` ye.di.dut → `beloved` [M05] |
| `bitterness` | M02, M03 (2 clusters, 6 term-rows) | `G4088` pikria → `bitterness` [M02]; `H4470` me.mer → `bitterness` [M03]; `H4472` mam.ror → `bitterness` [M03]; `H4786` mo.rah → `bitterness` [M03]; `H4787` mor.rah → `bitterness` [M03]; `H4844` ma.ror → `bitterness` [M03] |
| `distress` | M03, M27 (2 clusters, 8 term-rows) | `H4157` mu.a.qah → `distress` [M03]; `H4689` ma.tsoq → `distress` [M03]; `H4691` me.tsu.qah → `distress` [M03]; `H6695A` tsoq → `distress` [M03]; `H6862B` tsar → `distress` [M03]; `H6869B` tsa.rah → `distress` [M03]; `H7451C` ra.ah → `distress: harm` [M03]; `H7451I` ra.ah → `distress: evil` [M27] |
| `evil` | M10, M10b (2 clusters, 6 term-rows) | `H0205H` a.ven → `evil: trouble` [M10]; `G2549` kakia → `evil` [M10b]; `G4189` ponēria → `evil` [M10b]; `G5337` faulos → `evil` [M10b]; `H0205G` a.ven → `evil: trouble` [M10b]; `H7455` ro.a → `evil` [M10b] |
| `greatness` | M22, M23 (2 clusters, 3 term-rows) | `H1420` ge.dul.lah → `greatness` [M22]; `H1433` go.del → `greatness` [M22]; `H4768` mar.bit → `greatness` [M23] |
| `holy` | M12, M22 (2 clusters, 4 term-rows) | `H6918H` qa.dosh → `holy: saint` [M12]; `G0040G` hagios → `holy` [M22]; `H6918G` qa.dosh → `holy` [M22]; `H6922` qad.dish → `holy` [M22] |
| `judgment` | FLAG, M26 (2 clusters, 4 term-rows) | `G2920` krisis → `judgment` [FLAG]; `H1779` din → `judgment` [FLAG]; `H8201` she.phet → `judgment` [FLAG]; `H8196` she.phot → `judgment` [M26] |
| `justice` | FLAG, M26 (2 clusters, 3 term-rows) | `H4941G` mish.pat → `justice: judgement` [FLAG]; `H4941H` mish.pat → `justice` [FLAG]; `G1341` dikaiokrisia → `justice` [M26] |
| `noble` | M09, M34 (2 clusters, 3 term-rows) | `H5081G` na.div → `noble: willing` [M09]; `G4586` semnos → `noble` [M34]; `H5081H` na.div → `noble` [M34] |
| `pleasure` | M04, M28 (2 clusters, 2 term-rows) | `H2656` che.phets → `pleasure` [M04]; `G2237` hēdonē → `pleasure` [M28] |
| `poor` | M24, M46 (2 clusters, 3 term-rows) | `G3993` penēs → `poor` [M24]; `H6035` a.nav → `poor` [M24]; `G4434` ptōchos → `poor` [M46] |
| `pressure` | M01, M24 (2 clusters, 2 term-rows) | `H6125` a.qah → `pressure` [M01]; `G2347` thlipsis → `pressure` [M24] |
| `riches` | M22, M46 (2 clusters, 3 term-rows) | `H3520B` ke.vud.dah → `riches` [M22]; `G4149` ploutos → `riches` [M46]; `H6239` o.sher → `riches` [M46] |
| `rule` | FLAG, M23 (2 clusters, 3 term-rows) | `H1166H` ba.al → `rule: to rule` [FLAG]; `H1166I` ba.al → `rule: to marry` [FLAG]; `H4896` mish.tar → `rule` [M23] |
| `shame` | M05, M07 (2 clusters, 8 term-rows) | `H2617B` che.sed → `shame` [M05]; `G0152` aischunē → `shame` [M07]; `G1791` entropē → `shame` [M07]; `H0955` bu.shah → `shame` [M07]; `H1317` bosh.nah → `shame` [M07]; `H1322` bo.shet → `shame` [M07]; `H3639` ke.lim.mah → `shame` [M07]; `H3640` ke.lim.mut → `shame` [M07] |
| `strength` | FLAG, M23 (2 clusters, 22 term-rows) | `H2428A` cha.yil → `strength: soldiers` [FLAG]; `H2428H` cha.yil → `strength: rich` [FLAG]; `H2428I` cha.yil → `strength: worthy` [FLAG]; `G2479` ischus → `strength` [M23]; `H0193A` ul → `strength` [M23]; `H0202` on → `strength` [M23]; `H0353` e.yal → `strength` [M23]; `H0360` e.ya.lut → `strength` [M23]; `H0555` o.mets → `strength` [M23]; `H0556` am.tsah → `strength` [M23]; `H1679` do.ve → `strength` [M23]; `H2391` che.zeq → `strength` [M23]; `H2392` cho.zeq → `strength` [M23]; `H2393` chez.qah → `strength` [M23]; `H2428G` cha.yil → `strength` [M23]; `H2429` cha.yil → `strength` [M23]; `H3581B` ko.ach → `strength` [M23]; `H5794` e.zuz → `strength` [M23]; `H5797` oz → `strength` [M23]; `H5807` e.zuz → `strength` [M23]; `H6108` o.tsem → `strength` [M23]; `H6109` ots.mah → `strength` [M23] |
| `terror` | M01, M24 (2 clusters, 14 term-rows) | `H0367` e.mah → `terror` [M01]; `H1091` bal.la.hah → `terror` [M01]; `H1205` be.a.tah → `terror` [M01]; `H2283` chag.ga → `terror` [M01]; `H2844A` chat → `terror` [M01]; `H2847` chit.tah → `terror` [M01]; `H2849` chat.chat → `terror` [M01]; `H2851` chit.tit → `terror` [M01]; `H2866` cha.tat → `terror` [M01]; `H4032` ma.gor → `terror` [M01]; `H4288` me.chit.tah → `terror` [M01]; `H4637` ma.a.ra.tsah → `terror` [M01]; `H8606` tiph.le.tset → `terror` [M01]; `H4712` me.tsar → `terror` [M24] |
| `to be sorry` | M05, M11 (2 clusters, 2 term-rows) | `H5162G` na.cham → `to be sorry: comfort` [M05]; `H5162H` na.cham → `to be sorry: relent` [M11] |
| `to call` | M37, M42 (2 clusters, 6 term-rows) | `G2564G` kaleō → `to call: call` [M37]; `H7121G` qa.ra → `to call: call to` [M37]; `H7121H` qa.ra → `to call: call by` [M37]; `H7121I` qa.ra → `to call: call out` [M37]; `H7121J` qa.ra → `to call: read out` [M37]; `G5455` fōneō → `to call` [M42] |
| `to despair` | M18, M20 (2 clusters, 3 term-rows) | `G0560` apelpizo → `to despair` [M18]; `G1820` exaporeō → `to despair` [M20]; `H2976` ya.ash → `to despair` [M20] |
| `to form` | FLAG, M12 (2 clusters, 5 term-rows) | `H3335G` ya.tsar → `to form: formed` [FLAG]; `H3335H` ya.tsar → `to form: potter` [FLAG]; `H3335I` ya.tsar → `to form: plan` [FLAG]; `G3445` morfoō → `to form` [M12]; `H6696C` tsur → `to form` [M12] |
| `to harden` | FLAG, M30 (2 clusters, 2 term-rows) | `H7185` qa.shah → `to harden` [FLAG]; `G4456` pōroō → `to harden` [M30] |
| `to honor` | FLAG, M22 (2 clusters, 4 term-rows) | `H3513H` ka.ved → `to honor: heavy` [FLAG]; `H3513I` ka.ved → `to honor: many` [FLAG]; `H3513J` ka.ved → `to honor: dull` [FLAG]; `H1921` ha.dar → `to honor` [M22] |
| `to judge` | FLAG, M26 (2 clusters, 4 term-rows) | `G2919` krinō → `to judge` [FLAG]; `H1777` din → `to judge` [FLAG]; `H8199` sha.phat → `to judge` [FLAG]; `H8200` she.phat → `to judge` [M26] |
| `to keep` | FLAG, M30 (2 clusters, 5 term-rows) | `H5201` na.tar → `to keep` [FLAG]; `H8104G` sha.mar → `to keep: obey` [M30]; `H8104H` sha.mar → `to keep: guard` [M30]; `H8104I` sha.mar → `to keep: look at` [M30]; `H8104J` sha.mar → `to keep: careful` [M30] |
| `to provoke` | M02, M03 (2 clusters, 4 term-rows) | `G3947` paroxunō → `to provoke` [M02]; `H3707` ka.as → `to provoke` [M02]; `H6696B` tsur → `to provoke` [M02]; `H4843` ma.rar → `to provoke` [M03] |
| `to return` | M11, M45 (2 clusters, 3 term-rows) | `H5749A` ud → `to return` [M11]; `H7725N` shuv → `to return: recall` [M11]; `H7725O` shuv → `to return: repent` [M45] |
| `to strengthen` | M23, M34 (2 clusters, 8 term-rows) | `G1743` endunamoō → `to strengthen` [M23]; `G4599` sthenoō → `to strengthen` [M23]; `G4732` stereoō → `to strengthen` [M23]; `H2388G` cha.zaq → `to strengthen: strengthen` [M23]; `H2388H` cha.zaq → `to strengthen: hold` [M23]; `H2388I` cha.zaq → `to strengthen: ensure` [M23]; `H2388J` cha.zaq → `to strengthen: prevail over` [M23]; `H2388K` cha.zaq → `to strengthen: persevere` [M34] |
| `to train` | FLAG, M15 (2 clusters, 2 term-rows) | `G4994` sōfronizō → `to train` [FLAG]; `G1128` gumnazō → `to train` [M15] |
| `toil` | M03, M36 (2 clusters, 3 term-rows) | `H6089A` e.tsev → `toil` [M03]; `H6093` its.tsa.von → `toil` [M03]; `H8383` te.u.nim → `toil` [M36] |
| `torment` | M03, M35 (2 clusters, 3 term-rows) | `G0931` basanos → `torment` [M03]; `H4620` ma.a.tse.vah → `torment` [M03]; `G0929` basanismos → `torment` [M35] |
| `upright` | M13, M26 (2 clusters, 3 term-rows) | `H3477G` ya.shar → `upright:right` [M13]; `H3477I` ya.shar → `upright:straight` [M13]; `H5229` ne.kho.chah → `upright` [M26] |
| `wickedness` | M10, M10b (2 clusters, 3 term-rows) | `H7564` rish.ah → `wickedness` [M10]; `H4849` mir.sha.at → `wickedness` [M10b]; `H7562` re.sha → `wickedness` [M10b] |

---

## §3. Token collisions (127 tokens appear in 2+ clusters)

Each gloss is split into tokens (excluding stop-words: `to, a, an, the, of, in, on, at, by, with, from, as, be, is, it, or, and, for, into`). Tokens appearing in 2+ clusters' gloss vocabulary are listed by cluster-spread (most clusters first), then by term count. Truncated to top 50 by spread; full list in §3.1 below.

| Token | # Clusters | # Term-rows | Clusters (term count per cluster) |
|---|---:|---:|---|
| `self` | 7 | 11 | FLAG=1, M08=1, M19=5, M26=1, M28=1, M29=1, M46=1 |
| `make` | 6 | 7 | FLAG=2, M05=1, M15=1, M21=1, M28=1, M36=1 |
| `good` | 5 | 11 | M04=1, M05=7, M06=1, M22=1, M39=1 |
| `loving` | 4 | 7 | M02=1, M05=3, M21=1, M28=2 |
| `have` | 4 | 6 | M04=1, M05=3, M23=1, M34=1 |
| `judge` | 4 | 6 | FLAG=3, M15=1, M26=1, M41=1 |
| `heart` | 4 | 5 | M20=1, M23=2, M26=1, M30=1 |
| `cause` | 4 | 4 | M07=1, M17=1, M26=1, M35=1 |
| `give` | 4 | 4 | M05=1, M22=1, M33=1, M39=1 |
| `evil` | 3 | 10 | M10=1, M10b=6, M27=3 |
| `plan` | 3 | 10 | FLAG=1, M15=6, M17=3 |
| `distress` | 3 | 9 | M03=7, M24=1, M27=1 |
| `seek` | 3 | 6 | M19=1, M21=1, M41=4 |
| `boast` | 3 | 5 | M08=3, M16=1, M22=1 |
| `eager` | 3 | 5 | M18=1, M19=2, M34=2 |
| `sound` | 3 | 5 | FLAG=1, M13=2, M42=2 |
| `harm` | 3 | 4 | M03=1, M24=2, M27=1 |
| `out` | 3 | 4 | M11=1, M37=2, M42=1 |
| `trouble` | 3 | 4 | M03=2, M10=1, M10b=1 |
| `complete` | 3 | 3 | FLAG=1, M12=1, M34=1 |
| `labor` | 3 | 3 | FLAG=1, M03=1, M24=1 |
| `mind` | 3 | 3 | FLAG=1, M15=1, M45=1 |
| `obey` | 3 | 3 | M09=1, M30=1, M41=1 |
| `up` | 3 | 3 | M05=1, M08=1, M33=1 |
| `worthy` | 3 | 3 | FLAG=1, M22=1, M26=1 |
| `strength` | 2 | 22 | FLAG=3, M23=19 |
| `desire` | 2 | 15 | M28=13, M29=2 |
| `call` | 2 | 14 | M37=13, M42=1 |
| `terror` | 2 | 14 | M01=13, M24=1 |
| `shame` | 2 | 10 | M05=2, M07=8 |
| `peace` | 2 | 9 | M05=1, M33=8 |
| `strengthen` | 2 | 9 | M23=8, M34=1 |
| `rule` | 2 | 8 | FLAG=3, M23=5 |
| `love` | 2 | 7 | M05=6, M28=1 |
| `slander` | 2 | 7 | M14=5, M42=2 |
| `trust` | 2 | 7 | M19=6, M31=1 |
| `weak` | 2 | 7 | M03=1, M24=6 |
| `beloved` | 2 | 6 | FLAG=5, M05=1 |
| `bitterness` | 2 | 6 | M02=1, M03=5 |
| `comfort` | 2 | 6 | M05=2, M33=4 |
| `groan` | 2 | 6 | M03=3, M42=3 |
| `holiness` | 2 | 6 | M12=1, M22=5 |
| `master` | 2 | 6 | FLAG=4, M23=2 |
| `rich` | 2 | 6 | FLAG=1, M46=5 |
| `form` | 2 | 5 | FLAG=3, M12=2 |
| `gift` | 2 | 5 | M38=2, M39=3 |
| `honor` | 2 | 5 | FLAG=3, M22=2 |
| `keep` | 2 | 5 | FLAG=1, M30=4 |
| `listen` | 2 | 5 | M21=3, M41=2 |
| `provoke` | 2 | 5 | M02=4, M03=1 |

### §3.1 Token detail (all 127 tokens with cluster-spread ≥ 2)

For each token, the full list of terms per cluster.

#### `self` — 7 clusters, 11 term-rows

- **FLAG** (Flagged for Review) — 1 term(s):
  - `G0841` autarkeia — `self-sufficiency`
- **M08** (Pride, Arrogance and Boasting) — 1 term(s):
  - `G0829` authadēs — `self-willed`
- **M19** (Trust, Confidence and Security) — 5 term(s):
  - `G1466` enkrateia — `self-control`
  - `G1467` enkrateuomai — `to self-control`
  - `G1468` enkratēs — `self-controlled`
  - `G4995` sōfronismos — `self-discipline`
  - `G4998` sōfrōn — `self-controlled`
- **M26** (Righteousness and Justice) — 1 term(s):
  - `G0843` autokatakritos — `self-condemned`
- **M28** (Envy, Greed and Lust) — 1 term(s):
  - `G0192` akrasia — `self-indulgence`
- **M29** (Desire, Longing and Will) — 1 term(s):
  - `G0830` authairetos — `self-chosen`
- **M46** (Abundance, Prosperity and Wealth) — 1 term(s):
  - `G0842` autarkēs — `self-sufficient`

#### `make` — 6 clusters, 7 term-rows

- **FLAG** (Flagged for Review) — 2 term(s):
  - `G4833` summorfoomai — `to make like`
  - `H3772H` ka.rat — `to cut: make [covenant]`
- **M05** (Love, Compassion and Kindness) — 1 term(s):
  - `G1517` eirēnopoieō — `to make peace`
- **M15** (Wisdom, Understanding and Knowledge) — 1 term(s):
  - `G4679` sofizo — `to make wise`
- **M21** (Prayer, Worship and Devotion) — 1 term(s):
  - `G1303` diatithēmi — `to make a covenant`
- **M28** (Envy, Greed and Lust) — 1 term(s):
  - `G3863` parazēloō — `to make envious`
- **M36** (Service, Slavery and Labour) — 1 term(s):
  - `H5648` a.vad — `to make`

#### `good` — 5 clusters, 11 term-rows

- **M04** (Joy, Gladness and Delight) — 1 term(s):
  - `H2868` te.ev — `be good`
- **M05** (Love, Compassion and Kindness) — 7 term(s):
  - `G0014` agathoergeō — `to do good`
  - `G0015` agathopoieō — `to do good`
  - `G0016` agathopoiia — `doing good`
  - `G0017` agathopoios — `doing good`
  - `G0018` agathos — `good`
  - `G5358` filagathos — `lover of good`
  - `G5543` chrēstos — `good/kind`
- **M06** (Hate, Contempt and Hostility) — 1 term(s):
  - `G0865` afilagathos — `hating good`
- **M22** (Praise, Thanksgiving and Glory) — 1 term(s):
  - `G2162` eufēmia — `good report`
- **M39** (Blessing, Favour and Grace) — 1 term(s):
  - `H3190` ya.tav — `be good`

#### `loving` — 4 clusters, 7 term-rows

- **M02** (Anger, Wrath and Indignation) — 1 term(s):
  - `G5380` filoneikos — `dispute-loving`
- **M05** (Love, Compassion and Kindness) — 3 term(s):
  - `G5361` filadelfos — `loving the brothers`
  - `G5362` filandros — `husband-loving`
  - `G5388` filoteknos — `child loving`
- **M21** (Prayer, Worship and Devotion) — 1 term(s):
  - `G5377` filotheos — `God-loving`
- **M28** (Envy, Greed and Lust) — 2 term(s):
  - `G5366` filarguros — `money-loving`
  - `G5369` filēdonos — `pleasure-loving`

#### `have` — 4 clusters, 6 term-rows

- **M04** (Joy, Gladness and Delight) — 1 term(s):
  - `G3685` oninemi — `to have joy`
- **M05** (Love, Compassion and Kindness) — 3 term(s):
  - `G1653` eleeō — `to have mercy`
  - `G3627` oikteirō — `to have compassion`
  - `H7355` ra.cham — `to have compassion`
- **M23** (Strength, Power and Dominion) — 1 term(s):
  - `G1850` exousiazō — `to have authority`
- **M34** (Perseverance, Endurance and Steadfastness) — 1 term(s):
  - `G3114` makrothumeō — `to have patience`

#### `judge` — 4 clusters, 6 term-rows

- **FLAG** (Flagged for Review) — 3 term(s):
  - `G2919` krinō — `to judge`
  - `H1777` din — `to judge`
  - `H8199` sha.phat — `to judge`
- **M15** (Wisdom, Understanding and Knowledge) — 1 term(s):
  - `G1252` diakrinō — `to judge/doubt`
- **M26** (Righteousness and Justice) — 1 term(s):
  - `H8200` she.phat — `to judge`
- **M41** (Remembrance and Memory) — 1 term(s):
  - `H8085K` sha.ma — `to hear: judge`

#### `heart` — 4 clusters, 5 term-rows

- **M20** (Doubt, Despair and Anxiety) — 1 term(s):
  - `G1573` ekkakeō — `to lose heart`
- **M23** (Strength, Power and Dominion) — 2 term(s):
  - `G2292` tharseō — `take heart`
  - `G2293` tharseō — `take heart`
- **M26** (Righteousness and Justice) — 1 term(s):
  - `G2589` kardiognōstēs — `heart-knower`
- **M30** (Obedience and Disobedience) — 1 term(s):
  - `G4641` sklērokardia — `hardness of heart`

#### `cause` — 4 clusters, 4 term-rows

- **M07** (Shame, Disgrace and Humiliation) — 1 term(s):
  - `G1788` entrepō — `to cause shame`
- **M17** (Counsel, Planning and Purpose) — 1 term(s):
  - `H1701` div.rah — `cause`
- **M26** (Righteousness and Justice) — 1 term(s):
  - `G0156` aitia — `cause/charge`
- **M35** (Testing, Temptation and Trial) — 1 term(s):
  - `G4624` skandalizō — `to cause to stumble`

#### `give` — 4 clusters, 4 term-rows

- **M05** (Love, Compassion and Kindness) — 1 term(s):
  - `G1433` dōreō — `to give`
- **M22** (Praise, Thanksgiving and Glory) — 1 term(s):
  - `H3034` ya.dah — `to give thanks`
- **M33** (Peace, Rest and Quietness) — 1 term(s):
  - `G2270` hēsuchazō — `be quiet/give up`
- **M39** (Blessing, Favour and Grace) — 1 term(s):
  - `G5483` charizō — `to give grace`

#### `evil` — 3 clusters, 10 term-rows

- **M10** (Sin, Guilt and Transgression) — 1 term(s):
  - `H0205H` a.ven — `evil: trouble`
- **M10b** (Wickedness, Evil and Abomination) — 6 term(s):
  - `G2549` kakia — `evil`
  - `G4189` ponēria — `evil`
  - `G4190` ponēros — `evil/bad`
  - `G5337` faulos — `evil`
  - `H0205G` a.ven — `evil: trouble`
  - `H7455` ro.a — `evil`
- **M27** (Evil, Wickedness and Abomination) — 3 term(s):
  - `G2554` kakopoieō — `to do evil/harm`
  - `H7451I` ra.ah — `distress: evil`
  - `H7489A` ra.a — `be evil`

#### `plan` — 3 clusters, 10 term-rows

- **FLAG** (Flagged for Review) — 1 term(s):
  - `H3335I` ya.tsar — `to form: plan`
- **M15** (Wisdom, Understanding and Knowledge) — 6 term(s):
  - `G1011` bouleuō — `to plan`
  - `G1014` boulomai — `to plan`
  - `G4388` protithēmi — `to plan/present`
  - `H2161` za.mam — `to plan`
  - `H5779` uts — `to plan`
  - `H6246` a.shit — `to plan`
- **M17** (Counsel, Planning and Purpose) — 3 term(s):
  - `G1012` boulē — `plan`
  - `G1013` boulēma — `plan`
  - `H2162` za.mam — `plan`

#### `distress` — 3 clusters, 9 term-rows

- **M03** (Grief, Sorrow and Mourning) — 7 term(s):
  - `H4157` mu.a.qah — `distress`
  - `H4689` ma.tsoq — `distress`
  - `H4691` me.tsu.qah — `distress`
  - `H6695A` tsoq — `distress`
  - `H6862B` tsar — `distress`
  - `H6869B` tsa.rah — `distress`
  - `H7451C` ra.ah — `distress: harm`
- **M24** (Weakness, Vulnerability and Suffering) — 1 term(s):
  - `H6887C` tsa.rar — `to distress`
- **M27** (Evil, Wickedness and Abomination) — 1 term(s):
  - `H7451I` ra.ah — `distress: evil`

#### `seek` — 3 clusters, 6 term-rows

- **M19** (Trust, Confidence and Security) — 1 term(s):
  - `H2620` cha.sah — `to seek refuge`
- **M21** (Prayer, Worship and Devotion) — 1 term(s):
  - `G1934` epizēteō — `to seek after`
- **M41** (Remembrance and Memory) — 4 term(s):
  - `G2212` zēteō — `to seek`
  - `H1245` ba.qash — `to seek`
  - `H1875` da.rash — `to seek`
  - `H7836` sha.char — `to seek`

#### `boast` — 3 clusters, 5 term-rows

- **M08** (Pride, Arrogance and Boasting) — 3 term(s):
  - `G2744` kauchaomai — `to boast`
  - `H1984H` ha.lal — `to boast: boast`
  - `H1984H` ha.lal — `to boast: boast`
- **M16** (Folly, Madness and Foolishness) — 1 term(s):
  - `H1984I` ha.lal — `to boast: rave madly`
- **M22** (Praise, Thanksgiving and Glory) — 1 term(s):
  - `H1984B` ha.lal — `to boast: praise`

#### `eager` — 3 clusters, 5 term-rows

- **M18** (Hope, Expectation and Waiting) — 1 term(s):
  - `G0603` apokaradokia — `eager expectation`
- **M19** (Trust, Confidence and Security) — 2 term(s):
  - `G2206` zēloō — `be eager`
  - `G4704` spoudazō — `be eager`
- **M34** (Perseverance, Endurance and Steadfastness) — 2 term(s):
  - `G4289` prothumos — `eager`
  - `G4705` spoudaios — `eager`

#### `sound` — 3 clusters, 5 term-rows

- **FLAG** (Flagged for Review) — 1 term(s):
  - `G4993` sōfroneō — `be of sound mind`
- **M13** (Truth, Faithfulness and Integrity) — 2 term(s):
  - `G0573` haplous — `sound`
  - `H8088A` she.ma — `sound`
- **M42** (Speech, Voice and Cry) — 2 term(s):
  - `G5456H` fōnē — `voice/sound: noise`
  - `H7032G` qal — `voice: sound`

#### `harm` — 3 clusters, 4 term-rows

- **M03** (Grief, Sorrow and Mourning) — 1 term(s):
  - `H7451C` ra.ah — `distress: harm`
- **M24** (Weakness, Vulnerability and Suffering) — 2 term(s):
  - `G0091` adikeō — `to harm`
  - `G2559` kakoō — `to harm`
- **M27** (Evil, Wickedness and Abomination) — 1 term(s):
  - `G2554` kakopoieō — `to do evil/harm`

#### `out` — 3 clusters, 4 term-rows

- **M11** (Repentance, Forgiveness and Restoration) — 1 term(s):
  - `G1813` exaleifō — `to blot out`
- **M37** (Calling, Election and Vocation) — 2 term(s):
  - `H7121I` qa.ra — `to call: call out`
  - `H7121J` qa.ra — `to call: read out`
- **M42** (Speech, Voice and Cry) — 1 term(s):
  - `H2199` za.aq — `to cry out`

#### `trouble` — 3 clusters, 4 term-rows

- **M03** (Grief, Sorrow and Mourning) — 2 term(s):
  - `G4660` skullō — `to trouble`
  - `H5999` a.mal — `trouble`
- **M10** (Sin, Guilt and Transgression) — 1 term(s):
  - `H0205H` a.ven — `evil: trouble`
- **M10b** (Wickedness, Evil and Abomination) — 1 term(s):
  - `H0205G` a.ven — `evil: trouble`

#### `complete` — 3 clusters, 3 term-rows

- **FLAG** (Flagged for Review) — 1 term(s):
  - `H1585` ge.mar — `to complete`
- **M12** (Purity, Holiness and Consecration) — 1 term(s):
  - `H8549I` ta.mim — `unblemished: complete`
- **M34** (Perseverance, Endurance and Steadfastness) — 1 term(s):
  - `H8535` tam — `complete`

#### `labor` — 3 clusters, 3 term-rows

- **FLAG** (Flagged for Review) — 1 term(s):
  - `G4944` sunōdinō — `to labor together`
- **M03** (Grief, Sorrow and Mourning) — 1 term(s):
  - `G5605` ōdinō — `be in labor`
- **M24** (Weakness, Vulnerability and Suffering) — 1 term(s):
  - `G5604` ōdin — `labor`

#### `mind` — 3 clusters, 3 term-rows

- **FLAG** (Flagged for Review) — 1 term(s):
  - `G4993` sōfroneō — `be of sound mind`
- **M15** (Wisdom, Understanding and Knowledge) — 1 term(s):
  - `G3540` noēma — `mind/thought`
- **M45** (Transformation and Renewal) — 1 term(s):
  - `G3328` metaballō — `to change mind`

#### `obey` — 3 clusters, 3 term-rows

- **M09** (Humility, Meekness and Submission) — 1 term(s):
  - `G5219` hupakouō — `to obey`
- **M30** (Obedience and Disobedience) — 1 term(s):
  - `H8104G` sha.mar — `to keep: obey`
- **M41** (Remembrance and Memory) — 1 term(s):
  - `H8085H` sha.ma — `to hear: obey`

#### `up` — 3 clusters, 3 term-rows

- **M05** (Love, Compassion and Kindness) — 1 term(s):
  - `G2026` epoikodomeō — `to build up/upon`
- **M08** (Pride, Arrogance and Boasting) — 1 term(s):
  - `H1342` ga.ah — `to rise up`
- **M33** (Peace, Rest and Quietness) — 1 term(s):
  - `G2270` hēsuchazō — `be quiet/give up`

#### `worthy` — 3 clusters, 3 term-rows

- **FLAG** (Flagged for Review) — 1 term(s):
  - `H2428I` cha.yil — `strength: worthy`
- **M22** (Praise, Thanksgiving and Glory) — 1 term(s):
  - `G0514` axios — `worthy`
- **M26** (Righteousness and Justice) — 1 term(s):
  - `G0515` axioō — `to deem worthy`

#### `strength` — 2 clusters, 22 term-rows

- **FLAG** (Flagged for Review) — 3 term(s):
  - `H2428A` cha.yil — `strength: soldiers`
  - `H2428H` cha.yil — `strength: rich`
  - `H2428I` cha.yil — `strength: worthy`
- **M23** (Strength, Power and Dominion) — 19 term(s):
  - `G2479` ischus — `strength`
  - `H0193A` ul — `strength`
  - `H0202` on — `strength`
  - `H0353` e.yal — `strength`
  - `H0360` e.ya.lut — `strength`
  - `H0555` o.mets — `strength`
  - `H0556` am.tsah — `strength`
  - `H1679` do.ve — `strength`
  - `H2391` che.zeq — `strength`
  - `H2392` cho.zeq — `strength`
  - … and 9 more

#### `desire` — 2 clusters, 15 term-rows

- **M28** (Envy, Greed and Lust) — 13 term(s):
  - `G1939` epithumia — `desire`
  - `G2442` himeirō — `to desire`
  - `G2691` katastrēniaō — `to desire`
  - `H0176B` o — `desire`
  - `H0183` a.vah — `to desire`
  - `H1942` hav.vah — `desire`
  - `H2530A` cha.mad — `to desire`
  - `H2532A` chem.dah — `desire`
  - `H2836A` cha.shaq — `to desire`
  - `H2837` che.sheq — `desire`
  - … and 3 more
- **M29** (Desire, Longing and Will) — 2 term(s):
  - `G2307` thelēma — `will/desire`
  - `G2309` thelō — `to will/desire`

#### `call` — 2 clusters, 14 term-rows

- **M37** (Calling, Election and Vocation) — 13 term(s):
  - `G1793` entunchanō — `to call on`
  - `G1941` epikaleō — `to call (on)/name`
  - `G2564G` kaleō — `to call: call`
  - `G2564G` kaleō — `to call: call`
  - `G4341` proskaleō — `to call to/summon`
  - `G4377` prosfōneō — `to call to/summon`
  - `H7121G` qa.ra — `to call: call to`
  - `H7121G` qa.ra — `to call: call to`
  - `H7121H` qa.ra — `to call: call by`
  - `H7121H` qa.ra — `to call: call by`
  - … and 3 more
- **M42** (Speech, Voice and Cry) — 1 term(s):
  - `G5455` fōneō — `to call`

#### `terror` — 2 clusters, 14 term-rows

- **M01** (Fear, Dread and Terror) — 13 term(s):
  - `H0367` e.mah — `terror`
  - `H1091` bal.la.hah — `terror`
  - `H1205` be.a.tah — `terror`
  - `H2283` chag.ga — `terror`
  - `H2844A` chat — `terror`
  - `H2847` chit.tah — `terror`
  - `H2849` chat.chat — `terror`
  - `H2851` chit.tit — `terror`
  - `H2866` cha.tat — `terror`
  - `H4032` ma.gor — `terror`
  - … and 3 more
- **M24** (Weakness, Vulnerability and Suffering) — 1 term(s):
  - `H4712` me.tsar — `terror`

#### `shame` — 2 clusters, 10 term-rows

- **M05** (Love, Compassion and Kindness) — 2 term(s):
  - `H2616B` cha.sad — `to shame`
  - `H2617B` che.sed — `shame`
- **M07** (Shame, Disgrace and Humiliation) — 8 term(s):
  - `G0152` aischunē — `shame`
  - `G1788` entrepō — `to cause shame`
  - `G1791` entropē — `shame`
  - `H0955` bu.shah — `shame`
  - `H1317` bosh.nah — `shame`
  - `H1322` bo.shet — `shame`
  - `H3639` ke.lim.mah — `shame`
  - `H3640` ke.lim.mut — `shame`

#### `peace` — 2 clusters, 9 term-rows

- **M05** (Love, Compassion and Kindness) — 1 term(s):
  - `G1517` eirēnopoieō — `to make peace`
- **M33** (Peace, Rest and Quietness) — 8 term(s):
  - `G1514` eirēneuō — `be at peace`
  - `G1515` eirēnē — `peace`
  - `H7965G` sha.lom — `peace`
  - `H7965H` sha.lom — `peace`
  - `H7965I` sha.lom — `peace: well-being`
  - `H7965J` sha.lom — `peace: friendship`
  - `H7965K` sha.lom — `peace: greeting`
  - `H7965L` sha.lom — `peace: completely`

#### `strengthen` — 2 clusters, 9 term-rows

- **M23** (Strength, Power and Dominion) — 8 term(s):
  - `G1743` endunamoō — `to strengthen`
  - `G4599` sthenoō — `to strengthen`
  - `G4732` stereoō — `to strengthen`
  - `H2388G` cha.zaq — `to strengthen: strengthen`
  - `H2388G` cha.zaq — `to strengthen: strengthen`
  - `H2388H` cha.zaq — `to strengthen: hold`
  - `H2388I` cha.zaq — `to strengthen: ensure`
  - `H2388J` cha.zaq — `to strengthen: prevail over`
- **M34** (Perseverance, Endurance and Steadfastness) — 1 term(s):
  - `H2388K` cha.zaq — `to strengthen: persevere`

#### `rule` — 2 clusters, 8 term-rows

- **FLAG** (Flagged for Review) — 3 term(s):
  - `H1166H` ba.al — `rule: to rule`
  - `H1166H` ba.al — `rule: to rule`
  - `H1166I` ba.al — `rule: to marry`
- **M23** (Strength, Power and Dominion) — 5 term(s):
  - `G2715` katexousiazō — `to rule`
  - `H4896` mish.tar — `rule`
  - `H4910` ma.shal — `to rule`
  - `H7287A` ra.dah — `to rule`
  - `H7981` she.let — `to rule`

#### `love` — 2 clusters, 7 term-rows

- **M05** (Love, Compassion and Kindness) — 6 term(s):
  - `G0025` agapaō — `to love`
  - `G0026` agapē — `love`
  - `G5360` filadelfia — `brotherly love`
  - `G5368` fileō — `to love`
  - `H0157H` a.hev — `to love: friend`
  - `H0160` a.ha.vah — `love`
- **M28** (Envy, Greed and Lust) — 1 term(s):
  - `G5365` filarguria — `love of money`

#### `slander` — 2 clusters, 7 term-rows

- **M14** (Deceit, Hypocrisy and Falsehood) — 5 term(s):
  - `G1426` dusfēmia — `slander`
  - `G2636` katalalia — `slander`
  - `H1681` dib.bah — `slander`
  - `H1848` do.phi — `slander`
  - `H7400` ra.khil — `slander`
- **M42** (Speech, Voice and Cry) — 2 term(s):
  - `G2635` katalaleō — `to slander`
  - `H3960` la.shan — `to slander`

#### `trust` — 2 clusters, 7 term-rows

- **M19** (Trust, Confidence and Security) — 6 term(s):
  - `H0540` a.man — `to trust`
  - `H0982` ba.tach — `to trust`
  - `H0985` bit.chah — `trust`
  - `H0986` bit.ta.chon — `trust`
  - `H5375O` na.sa — `to lift: trust`
  - `H7365` re.chats — `to trust`
- **M31** (Faith, Belief and Unbelief) — 1 term(s):
  - `G4100` pisteuō — `to trust (in)`

#### `weak` — 2 clusters, 7 term-rows

- **M03** (Grief, Sorrow and Mourning) — 1 term(s):
  - `H2470I` cha.lah — `be weak: grieved`
- **M24** (Weakness, Vulnerability and Suffering) — 6 term(s):
  - `G0769G` astheneia — `weakness: weak`
  - `G0770G` astheneō — `be weak: weak`
  - `G0770G` astheneō — `be weak: weak`
  - `G0770H` astheneō — `be weak: ill`
  - `G0772G` asthenēs — `weak`
  - `G0772H` asthenēs — `weak: ill`

#### `beloved` — 2 clusters, 6 term-rows

- **FLAG** (Flagged for Review) — 5 term(s):
  - `G0027` agapētos — `beloved`
  - `H1730G` dod — `beloved`
  - `H1730H` dod — `beloved`
  - `H1730I` dod — `beloved: male relative`
  - `H3039A` ya.did — `beloved`
- **M05** (Love, Compassion and Kindness) — 1 term(s):
  - `H3033` ye.di.dut — `beloved`

#### `bitterness` — 2 clusters, 6 term-rows

- **M02** (Anger, Wrath and Indignation) — 1 term(s):
  - `G4088` pikria — `bitterness`
- **M03** (Grief, Sorrow and Mourning) — 5 term(s):
  - `H4470` me.mer — `bitterness`
  - `H4472` mam.ror — `bitterness`
  - `H4786` mo.rah — `bitterness`
  - `H4787` mor.rah — `bitterness`
  - `H4844` ma.ror — `bitterness`

#### `comfort` — 2 clusters, 6 term-rows

- **M05** (Love, Compassion and Kindness) — 2 term(s):
  - `G3870` parakaleō — `to plead/comfort`
  - `H5162G` na.cham — `to be sorry: comfort`
- **M33** (Peace, Rest and Quietness) — 4 term(s):
  - `G3890` paramuthion — `comfort`
  - `G3931` parēgoria — `comfort`
  - `H5150` ni.chum — `comfort`
  - `H5165` ne.cha.mah — `comfort`

#### `groan` — 2 clusters, 6 term-rows

- **M03** (Grief, Sorrow and Mourning) — 3 term(s):
  - `G4726` stenagmos — `groan`
  - `G4959` sustenazō — `to groan with`
  - `H5009` ne.a.qah — `groan`
- **M42** (Speech, Voice and Cry) — 3 term(s):
  - `G4727` ste.na.zo — `to groan`
  - `H5008` na.aq — `to groan`
  - `H5098` na.ham — `to groan`

#### `holiness` — 2 clusters, 6 term-rows

- **M12** (Purity, Holiness and Consecration) — 1 term(s):
  - `H6942K` qa.dash — `to consecrate: holiness`
- **M22** (Praise, Thanksgiving and Glory) — 5 term(s):
  - `G0038` hagiasmos — `holiness`
  - `G0041` hagiotēs — `holiness`
  - `G0042` hagiōsunē — `holiness`
  - `G3742` hosiotēs — `holiness`
  - `H6944G` qo.desh — `holiness`

#### `master` — 2 clusters, 6 term-rows

- **FLAG** (Flagged for Review) — 4 term(s):
  - `H1167G` ba.al — `master`
  - `H1167H` ba.al — `master: husband`
  - `H1167I` ba.al — `master: men`
  - `H1167J` ba.al — `master: owning`
- **M23** (Strength, Power and Dominion) — 2 term(s):
  - `G2634` katakurieuō — `to master`
  - `G2962H` kurios — `lord: master`

#### `rich` — 2 clusters, 6 term-rows

- **FLAG** (Flagged for Review) — 1 term(s):
  - `H2428H` cha.yil — `strength: rich`
- **M46** (Abundance, Prosperity and Wealth) — 5 term(s):
  - `G3045` liparos — `rich`
  - `G4145` plousios — `rich`
  - `G4147` plouteō — `be rich`
  - `H6223` a.shir — `rich`
  - `H8082` sha.men — `rich`

#### `form` — 2 clusters, 5 term-rows

- **FLAG** (Flagged for Review) — 3 term(s):
  - `H3335G` ya.tsar — `to form: formed`
  - `H3335H` ya.tsar — `to form: potter`
  - `H3335I` ya.tsar — `to form: plan`
- **M12** (Purity, Holiness and Consecration) — 2 term(s):
  - `G3445` morfoō — `to form`
  - `H6696C` tsur — `to form`

#### `gift` — 2 clusters, 5 term-rows

- **M38** (Salvation, Redemption and Deliverance) — 2 term(s):
  - `G1431` dōrea — `free gift`
  - `G1434` dōrēma — `free gift`
- **M39** (Blessing, Favour and Grace) — 3 term(s):
  - `G1435` dōron — `gift`
  - `G5486` charisma — `gift`
  - `H7862` shay — `gift`

#### `honor` — 2 clusters, 5 term-rows

- **FLAG** (Flagged for Review) — 3 term(s):
  - `H3513H` ka.ved — `to honor: heavy`
  - `H3513I` ka.ved — `to honor: many`
  - `H3513J` ka.ved — `to honor: dull`
- **M22** (Praise, Thanksgiving and Glory) — 2 term(s):
  - `H1921` ha.dar — `to honor`
  - `H5082` ne.di.vah — `honor`

#### `keep` — 2 clusters, 5 term-rows

- **FLAG** (Flagged for Review) — 1 term(s):
  - `H5201` na.tar — `to keep`
- **M30** (Obedience and Disobedience) — 4 term(s):
  - `H8104G` sha.mar — `to keep: obey`
  - `H8104H` sha.mar — `to keep: guard`
  - `H8104I` sha.mar — `to keep: look at`
  - `H8104J` sha.mar — `to keep: careful`

#### `listen` — 2 clusters, 5 term-rows

- **M21** (Prayer, Worship and Devotion) — 3 term(s):
  - `G1522` eisakouō — `to listen to`
  - `G1873` epakouō — `to listen to`
  - `G1874` epakroaomai — `to listen ro`
- **M41** (Remembrance and Memory) — 2 term(s):
  - `H0238` a.zan — `to listen`
  - `H7181` qa.shav — `to listen`

#### `provoke` — 2 clusters, 5 term-rows

- **M02** (Anger, Wrath and Indignation) — 4 term(s):
  - `G2042` erethizō — `to provoke/irritate`
  - `G3947` paroxunō — `to provoke`
  - `H3707` ka.as — `to provoke`
  - `H6696B` tsur — `to provoke`
- **M03** (Grief, Sorrow and Mourning) — 1 term(s):
  - `H4843` ma.rar — `to provoke`

#### `slave` — 2 clusters, 5 term-rows

- **M36** (Service, Slavery and Labour) — 4 term(s):
  - `G1398` douleuō — `be a slave`
  - `G1399` doulē — `female slave`
  - `G1401` doulos — `slave`
  - `G3610` oiketēs — `slave`
- **M44** (Relational Disposition) — 1 term(s):
  - `G4889` sundoulos — `fellow slave`

#### `covenant` — 2 clusters, 4 term-rows

- **FLAG** (Flagged for Review) — 3 term(s):
  - `G1242` diathēkē — `covenant`
  - `H1285` be.rit — `covenant`
  - `H3772H` ka.rat — `to cut: make [covenant]`
- **M21** (Prayer, Worship and Devotion) — 1 term(s):
  - `G1303` diatithēmi — `to make a covenant`

#### `destroy` — 2 clusters, 4 term-rows

- **FLAG** (Flagged for Review) — 1 term(s):
  - `H3615H` ka.lah — `to end: destroy`
- **M10** (Sin, Guilt and Transgression) — 3 term(s):
  - `G1311` diaftheirō — `to destroy`
  - `G5351` ftheirō — `to destroy`
  - `H2254B` cha.val — `to destroy`

#### `gracious` — 2 clusters, 4 term-rows

- **M38** (Salvation, Redemption and Deliverance) — 1 term(s):
  - `G2436` hileōs — `propitious/gracious`
- **M39** (Blessing, Favour and Grace) — 3 term(s):
  - `H2587` chan.nun — `gracious`
  - `H2603A` cha.nan — `be gracious`
  - `H2604` cha.nan — `be gracious`

#### `holy` — 2 clusters, 4 term-rows

- **M12** (Purity, Holiness and Consecration) — 1 term(s):
  - `H6918H` qa.dosh — `holy: saint`
- **M22** (Praise, Thanksgiving and Glory) — 3 term(s):
  - `G0040G` hagios — `holy`
  - `H6918G` qa.dosh — `holy`
  - `H6922` qad.dish — `holy`

#### `judgment` — 2 clusters, 4 term-rows

- **FLAG** (Flagged for Review) — 3 term(s):
  - `G2920` krisis — `judgment`
  - `H1779` din — `judgment`
  - `H8201` she.phet — `judgment`
- **M26** (Righteousness and Justice) — 1 term(s):
  - `H8196` she.phot — `judgment`

#### `oppress` — 2 clusters, 4 term-rows

- **M23** (Strength, Power and Dominion) — 1 term(s):
  - `G4912` sunechō — `to hold/oppress`
- **M24** (Weakness, Vulnerability and Suffering) — 3 term(s):
  - `G2616` katadunasteuō — `to oppress`
  - `G2669` kataponeō — `to oppress`
  - `H5065` na.ga.s — `to oppress`

#### `poor` — 2 clusters, 4 term-rows

- **M24** (Weakness, Vulnerability and Suffering) — 2 term(s):
  - `G3993` penēs — `poor`
  - `H6035` a.nav — `poor`
- **M46** (Abundance, Prosperity and Wealth) — 2 term(s):
  - `G4433` ptōcheuō — `be poor`
  - `G4434` ptōchos — `poor`

#### `report` — 2 clusters, 4 term-rows

- **M22** (Praise, Thanksgiving and Glory) — 1 term(s):
  - `G2162` eufēmia — `good report`
- **M41** (Remembrance and Memory) — 3 term(s):
  - `H2045` hash.ma.ut — `report`
  - `H8088B` she.ma — `report`
  - `H8089` sho.ma — `report`

#### `willing` — 2 clusters, 4 term-rows

- **M09** (Humility, Meekness and Submission) — 1 term(s):
  - `H5081G` na.div — `noble: willing`
- **M29** (Desire, Longing and Will) — 3 term(s):
  - `H2974` ya.al — `be willing`
  - `H5068` na.dav — `be willing`
  - `H5069` ne.dav — `be willing`

#### `act` — 2 clusters, 3 term-rows

- **M10** (Sin, Guilt and Transgression) — 1 term(s):
  - `H0898` ba.gad — `to act treacherously`
- **M26** (Righteousness and Justice) — 2 term(s):
  - `G1345` dikaiōma — `righteous act`
  - `H5765` a.val — `to act unjustly`

#### `anxiety` — 2 clusters, 3 term-rows

- **M01** (Fear, Dread and Terror) — 2 term(s):
  - `H1674` de.a.gah — `anxiety`
  - `H8312` sar.ap.pim — `anxiety`
- **M33** (Peace, Rest and Quietness) — 1 term(s):
  - `G0253` alupos — `without anxiety`

#### `bold` — 2 clusters, 3 term-rows

- **M08** (Pride, Arrogance and Boasting) — 1 term(s):
  - `G5113` tolmētēs — `bold man`
- **M34** (Perseverance, Endurance and Steadfastness) — 2 term(s):
  - `G0662` apotolmaō — `be bold`
  - `G5111` tolmaō — `be bold`

#### `cut` — 2 clusters, 3 term-rows

- **FLAG** (Flagged for Review) — 2 term(s):
  - `H3772H` ka.rat — `to cut: make [covenant]`
  - `H3772J` ka.rat — `to cut: lack`
- **M03** (Grief, Sorrow and Mourning) — 1 term(s):
  - `G2875` koptō — `to cut/mourn`

#### `despair` — 2 clusters, 3 term-rows

- **M18** (Hope, Expectation and Waiting) — 1 term(s):
  - `G0560` apelpizo — `to despair`
- **M20** (Doubt, Despair and Anxiety) — 2 term(s):
  - `G1820` exaporeō — `to despair`
  - `H2976` ya.ash — `to despair`

#### `dispute` — 2 clusters, 3 term-rows

- **M02** (Anger, Wrath and Indignation) — 2 term(s):
  - `G0485` antilogia — `dispute`
  - `G5380` filoneikos — `dispute-loving`
- **M15** (Wisdom, Understanding and Knowledge) — 1 term(s):
  - `G1256` dialegō — `to dispute`

#### `do` — 2 clusters, 3 term-rows

- **M05** (Love, Compassion and Kindness) — 2 term(s):
  - `G0014` agathoergeō — `to do good`
  - `G0015` agathopoieō — `to do good`
- **M27** (Evil, Wickedness and Abomination) — 1 term(s):
  - `G2554` kakopoieō — `to do evil/harm`

#### `faint` — 2 clusters, 3 term-rows

- **M03** (Grief, Sorrow and Mourning) — 1 term(s):
  - `H1742` dav.va — `faint`
- **M24** (Weakness, Vulnerability and Suffering) — 2 term(s):
  - `G0674` apopsuchō — `to faint`
  - `H3286` ya.eph — `to faint`

#### `faithfulness` — 2 clusters, 3 term-rows

- **M13** (Truth, Faithfulness and Integrity) — 2 term(s):
  - `H0530` e.mu.nah — `faithfulness`
  - `H0544` o.men — `faithfulness`
- **M31** (Faith, Belief and Unbelief) — 1 term(s):
  - `G4102H` pistis — `faith: faithfulness`

#### `gentle` — 2 clusters, 3 term-rows

- **M05** (Love, Compassion and Kindness) — 2 term(s):
  - `G1933` epieikēs — `gentle`
  - `G4239` praus — `gentle`
- **M09** (Humility, Meekness and Submission) — 1 term(s):
  - `G3356` metriopatheō — `be gentle`

#### `god` — 2 clusters, 3 term-rows

- **FLAG** (Flagged for Review) — 1 term(s):
  - `H0410G` el — `God`
- **M21** (Prayer, Worship and Devotion) — 2 term(s):
  - `G2317` theosebeia — `reverence for God`
  - `G5377` filotheos — `God-loving`

#### `greatness` — 2 clusters, 3 term-rows

- **M22** (Praise, Thanksgiving and Glory) — 2 term(s):
  - `H1420` ge.dul.lah — `greatness`
  - `H1433` go.del — `greatness`
- **M23** (Strength, Power and Dominion) — 1 term(s):
  - `H4768` mar.bit — `greatness`

#### `grow` — 2 clusters, 3 term-rows

- **M23** (Strength, Power and Dominion) — 2 term(s):
  - `H7236` re.vah — `to grow great`
  - `H8631` te.qeph — `to grow strong`
- **M46** (Abundance, Prosperity and Wealth) — 1 term(s):
  - `H8080` sha.men — `to grow fat`

#### `justice` — 2 clusters, 3 term-rows

- **FLAG** (Flagged for Review) — 2 term(s):
  - `H4941G` mish.pat — `justice: judgement`
  - `H4941H` mish.pat — `justice`
- **M26** (Righteousness and Justice) — 1 term(s):
  - `G1341` dikaiokrisia — `justice`

#### `know` — 2 clusters, 3 term-rows

- **M15** (Wisdom, Understanding and Knowledge) — 2 term(s):
  - `G6063` oida — `to know`
  - `H3045` ya.da — `to know`
- **M37** (Calling, Election and Vocation) — 1 term(s):
  - `G4267` proginōskō — `to know/choose`

#### `like` — 2 clusters, 3 term-rows

- **FLAG** (Flagged for Review) — 1 term(s):
  - `G4833` summorfoomai — `to make like`
- **M05** (Love, Compassion and Kindness) — 2 term(s):
  - `G2473` isopsuchos — `like-minded`
  - `G3675` homofrōn — `like-minded`

#### `minded` — 2 clusters, 3 term-rows

- **M05** (Love, Compassion and Kindness) — 2 term(s):
  - `G2473` isopsuchos — `like-minded`
  - `G3675` homofrōn — `like-minded`
- **M20** (Doubt, Despair and Anxiety) — 1 term(s):
  - `G1374` dipsuchos — `double-minded`

#### `name` — 2 clusters, 3 term-rows

- **FLAG** (Flagged for Review) — 2 term(s):
  - `G3686` onoma — `name`
  - `H8034` shem — `name`
- **M37** (Calling, Election and Vocation) — 1 term(s):
  - `G1941` epikaleō — `to call (on)/name`

#### `noble` — 2 clusters, 3 term-rows

- **M09** (Humility, Meekness and Submission) — 1 term(s):
  - `H5081G` na.div — `noble: willing`
- **M34** (Perseverance, Endurance and Steadfastness) — 2 term(s):
  - `G4586` semnos — `noble`
  - `H5081H` na.div — `noble`

#### `not` — 2 clusters, 3 term-rows

- **M05** (Love, Compassion and Kindness) — 2 term(s):
  - `G0420` anexikakos — `not resentful`
  - `G0866` afilarguros — `not greedy`
- **M35** (Testing, Temptation and Trial) — 1 term(s):
  - `G0677` aproskopos — `not stumbling`

#### `pleasure` — 2 clusters, 3 term-rows

- **M04** (Joy, Gladness and Delight) — 1 term(s):
  - `H2656` che.phets — `pleasure`
- **M28** (Envy, Greed and Lust) — 2 term(s):
  - `G2237` hēdonē — `pleasure`
  - `G5369` filēdonos — `pleasure-loving`

#### `press` — 2 clusters, 3 term-rows

- **FLAG** (Flagged for Review) — 1 term(s):
  - `H6693` tsuq — `to press`
- **M03** (Grief, Sorrow and Mourning) — 2 term(s):
  - `G2346` thlibō — `to press on`
  - `G4729` stenochōreō — `to press upon`

#### `purpose` — 2 clusters, 3 term-rows

- **M15** (Wisdom, Understanding and Knowledge) — 1 term(s):
  - `G1771` ennoia — `thought/purpose`
- **M17** (Counsel, Planning and Purpose) — 2 term(s):
  - `G4286` prothesis — `purpose`
  - `G5427` fronēma — `purpose`

#### `return` — 2 clusters, 3 term-rows

- **M11** (Repentance, Forgiveness and Restoration) — 2 term(s):
  - `H5749A` ud — `to return`
  - `H7725N` shuv — `to return: recall`
- **M45** (Transformation and Renewal) — 1 term(s):
  - `H7725O` shuv — `to return: repent`

#### `revere` — 2 clusters, 3 term-rows

- **M01** (Fear, Dread and Terror) — 2 term(s):
  - `H3372G` ya.re — `to fear: revere`
  - `H3372H` ya.re — `to fear: revere`
- **M21** (Prayer, Worship and Devotion) — 1 term(s):
  - `G2125` eulabeomai — `to revere`

#### `riches` — 2 clusters, 3 term-rows

- **M22** (Praise, Thanksgiving and Glory) — 1 term(s):
  - `H3520B` ke.vud.dah — `riches`
- **M46** (Abundance, Prosperity and Wealth) — 2 term(s):
  - `G4149` ploutos — `riches`
  - `H6239` o.sher — `riches`

#### `silent` — 2 clusters, 3 term-rows

- **M33** (Peace, Rest and Quietness) — 1 term(s):
  - `H1826H` da.mam — `to silence: silent`
- **M42** (Speech, Voice and Cry) — 2 term(s):
  - `G4601` sigaō — `be silent`
  - `H2814` cha.shah — `be silent`

#### `sing` — 2 clusters, 3 term-rows

- **M22** (Praise, Thanksgiving and Glory) — 1 term(s):
  - `G5567` psallō — `to sing praise`
- **M42** (Speech, Voice and Cry) — 2 term(s):
  - `H2167` za.mar — `to sing`
  - `H7442B` ra.nan — `to sing`

#### `thing` — 2 clusters, 3 term-rows

- **M25** (Life, Vitality and Existence) — 1 term(s):
  - `H2416C` chay.yah — `living thing`
- **M28** (Envy, Greed and Lust) — 2 term(s):
  - `H2530B` cha.mu.dah — `desirable thing`
  - `H2532B` cha.mu.dah — `desirable thing`

#### `toil` — 2 clusters, 3 term-rows

- **M03** (Grief, Sorrow and Mourning) — 2 term(s):
  - `H6089A` e.tsev — `toil`
  - `H6093` its.tsa.von — `toil`
- **M36** (Service, Slavery and Labour) — 1 term(s):
  - `H8383` te.u.nim — `toil`

#### `torment` — 2 clusters, 3 term-rows

- **M03** (Grief, Sorrow and Mourning) — 2 term(s):
  - `G0931` basanos — `torment`
  - `H4620` ma.a.tse.vah — `torment`
- **M35** (Testing, Temptation and Trial) — 1 term(s):
  - `G0929` basanismos — `torment`

#### `understand` — 2 clusters, 3 term-rows

- **M15** (Wisdom, Understanding and Knowledge) — 2 term(s):
  - `G4920` suniēmi — `to understand`
  - `H0995` bin — `to understand`
- **M41** (Remembrance and Memory) — 1 term(s):
  - `H8085J` sha.ma — `to hear: understand`

#### `upright` — 2 clusters, 3 term-rows

- **M13** (Truth, Faithfulness and Integrity) — 2 term(s):
  - `H3477G` ya.shar — `upright:right`
  - `H3477I` ya.shar — `upright:straight`
- **M26** (Righteousness and Justice) — 1 term(s):
  - `H5229` ne.kho.chah — `upright`

#### `wickedness` — 2 clusters, 3 term-rows

- **M10** (Sin, Guilt and Transgression) — 1 term(s):
  - `H7564` rish.ah — `wickedness`
- **M10b** (Wickedness, Evil and Abomination) — 2 term(s):
  - `H4849` mir.sha.at — `wickedness`
  - `H7562` re.sha — `wickedness`

#### `abundance` — 2 clusters, 2 term-rows

- **M33** (Peace, Rest and Quietness) — 1 term(s):
  - `H4766` mar.veh — `abundance`
- **M46** (Abundance, Prosperity and Wealth) — 1 term(s):
  - `H7230` rov — `abundance`

#### `bad` — 2 clusters, 2 term-rows

- **M10b** (Wickedness, Evil and Abomination) — 1 term(s):
  - `G4190` ponēros — `evil/bad`
- **M27** (Evil, Wickedness and Abomination) — 1 term(s):
  - `H7451A` ra — `bad: harmful`

#### `bless` — 2 clusters, 2 term-rows

- **M22** (Praise, Thanksgiving and Glory) — 1 term(s):
  - `G2127` eulogeō — `to praise/bless`
- **M39** (Blessing, Favour and Grace) — 1 term(s):
  - `H1288` ba.rakh — `to bless`

#### `careful` — 2 clusters, 2 term-rows

- **M19** (Trust, Confidence and Security) — 1 term(s):
  - `G5431` frontizō — `be careful`
- **M30** (Obedience and Disobedience) — 1 term(s):
  - `H8104J` sha.mar — `to keep: careful`

#### `christ` — 2 clusters, 2 term-rows

- **FLAG** (Flagged for Review) — 1 term(s):
  - `G5547` christos — `Christ`
- **M14** (Deceit, Hypocrisy and Falsehood) — 1 term(s):
  - `G5580` pseudochristos — `false Christ`

#### `count` — 2 clusters, 2 term-rows

- **M15** (Wisdom, Understanding and Knowledge) — 1 term(s):
  - `H2803H` cha.shav — `to devise: count`
- **M26** (Righteousness and Justice) — 1 term(s):
  - `G3049` logizomai — `to count`

#### `destroyed` — 2 clusters, 2 term-rows

- **M01** (Fear, Dread and Terror) — 1 term(s):
  - `H8047G` sham.mah — `horror: destroyed`
- **M27** (Evil, Wickedness and Abomination) — 1 term(s):
  - `H8074G` sha.mem — `be desolate: destroyed`

#### `devout` — 2 clusters, 2 term-rows

- **M21** (Prayer, Worship and Devotion) — 1 term(s):
  - `G4576` sebomai — `be devout`
- **M31** (Faith, Belief and Unbelief) — 1 term(s):
  - `G2126` eulabēs — `devout`

#### `doubt` — 2 clusters, 2 term-rows

- **M15** (Wisdom, Understanding and Knowledge) — 1 term(s):
  - `G1252` diakrinō — `to judge/doubt`
- **M20** (Doubt, Despair and Anxiety) — 1 term(s):
  - `G1365` distazō — `to doubt`

#### `endure` — 2 clusters, 2 term-rows

- **M34** (Perseverance, Endurance and Steadfastness) — 1 term(s):
  - `G5278` hupomenō — `to remain/endure`
- **M35** (Testing, Temptation and Trial) — 1 term(s):
  - `G0430` anechō — `to endure`

#### `friendship` — 2 clusters, 2 term-rows

- **M05** (Love, Compassion and Kindness) — 1 term(s):
  - `G5373` filia — `friendship`
- **M33** (Peace, Rest and Quietness) — 1 term(s):
  - `H7965J` sha.lom — `peace: friendship`

#### `greedy` — 2 clusters, 2 term-rows

- **M05** (Love, Compassion and Kindness) — 1 term(s):
  - `G0866` afilarguros — `not greedy`
- **M28** (Envy, Greed and Lust) — 1 term(s):
  - `G4123` pleonektēs — `greedy`

#### `guard` — 2 clusters, 2 term-rows

- **FLAG** (Flagged for Review) — 1 term(s):
  - `H4928` mish.ma.at — `guard`
- **M30** (Obedience and Disobedience) — 1 term(s):
  - `H8104H` sha.mar — `to keep: guard`

#### `harden` — 2 clusters, 2 term-rows

- **FLAG** (Flagged for Review) — 1 term(s):
  - `H7185` qa.shah — `to harden`
- **M30** (Obedience and Disobedience) — 1 term(s):
  - `G4456` pōroō — `to harden`

#### `husband` — 2 clusters, 2 term-rows

- **FLAG** (Flagged for Review) — 1 term(s):
  - `H1167H` ba.al — `master: husband`
- **M05** (Love, Compassion and Kindness) — 1 term(s):
  - `G5362` filandros — `husband-loving`

#### `hypocrisy` — 2 clusters, 2 term-rows

- **M10** (Sin, Guilt and Transgression) — 1 term(s):
  - `G4942` sunupokrinomai — `to join hypocrisy`
- **M14** (Deceit, Hypocrisy and Falsehood) — 1 term(s):
  - `G5272` hupokrisis — `hypocrisy`

#### `labour` — 2 clusters, 2 term-rows

- **M03** (Grief, Sorrow and Mourning) — 1 term(s):
  - `H2254C` cha.val — `be in labour`
- **M36** (Service, Slavery and Labour) — 1 term(s):
  - `H5647I` a.vad — `to serve: labour`

#### `look` — 2 clusters, 2 term-rows

- **M18** (Hope, Expectation and Waiting) — 1 term(s):
  - `G4328` prosdokaō — `to look for`
- **M30** (Obedience and Disobedience) — 1 term(s):
  - `H8104I` sha.mar — `to keep: look at`

#### `one` — 2 clusters, 2 term-rows

- **M10** (Sin, Guilt and Transgression) — 1 term(s):
  - `H5760` a.vil — `unjust one`
- **M29** (Desire, Longing and Will) — 1 term(s):
  - `G1938` epithumētēs — `one who desires`

#### `patience` — 2 clusters, 2 term-rows

- **M33** (Peace, Rest and Quietness) — 1 term(s):
  - `G3115` makrothumia — `patience`
- **M34** (Perseverance, Endurance and Steadfastness) — 1 term(s):
  - `G3114` makrothumeō — `to have patience`

#### `pleasing` — 2 clusters, 2 term-rows

- **M04** (Joy, Gladness and Delight) — 1 term(s):
  - `G0701` arestos — `pleasing`
- **M39** (Blessing, Favour and Grace) — 1 term(s):
  - `H2895` tov — `be pleasing`

#### `pressure` — 2 clusters, 2 term-rows

- **M01** (Fear, Dread and Terror) — 1 term(s):
  - `H6125` a.qah — `pressure`
- **M24** (Weakness, Vulnerability and Suffering) — 1 term(s):
  - `G2347` thlipsis — `pressure`

#### `remove` — 2 clusters, 2 term-rows

- **FLAG** (Flagged for Review) — 1 term(s):
  - `H2118` za.chach — `to remove`
- **M30** (Obedience and Disobedience) — 1 term(s):
  - `H5493G` sur — `to turn aside: remove`

#### `show` — 2 clusters, 2 term-rows

- **M05** (Love, Compassion and Kindness) — 1 term(s):
  - `G1731` endeiknumi — `to show`
- **M21** (Prayer, Worship and Devotion) — 1 term(s):
  - `G2151` eusebeō — `to show piety`

#### `smooth` — 2 clusters, 2 term-rows

- **FLAG** (Flagged for Review) — 1 term(s):
  - `H3474` ya.shar — `to smooth`
- **M14** (Deceit, Hypocrisy and Falsehood) — 1 term(s):
  - `G5542` chrēstologia — `smooth talk`

#### `sober` — 2 clusters, 2 term-rows

- **M19** (Trust, Confidence and Security) — 1 term(s):
  - `G3524` nēfaleos — `sober`
- **M33** (Peace, Rest and Quietness) — 1 term(s):
  - `G3525` nēfō — `be sober`

#### `sorry` — 2 clusters, 2 term-rows

- **M05** (Love, Compassion and Kindness) — 1 term(s):
  - `H5162G` na.cham — `to be sorry: comfort`
- **M11** (Repentance, Forgiveness and Restoration) — 1 term(s):
  - `H5162H` na.cham — `to be sorry: relent`

#### `soundness` — 2 clusters, 2 term-rows

- **FLAG** (Flagged for Review) — 1 term(s):
  - `G4997` sōfrosunē — `mental soundness`
- **M12** (Purity, Holiness and Consecration) — 1 term(s):
  - `H4974` me.tom — `soundness`

#### `suffer` — 2 clusters, 2 term-rows

- **M03** (Grief, Sorrow and Mourning) — 1 term(s):
  - `G4841` sumpaschō — `to suffer with`
- **M24** (Weakness, Vulnerability and Suffering) — 1 term(s):
  - `H3013` ya.gah — `to suffer`

#### `train` — 2 clusters, 2 term-rows

- **FLAG** (Flagged for Review) — 1 term(s):
  - `G4994` sōfronizō — `to train`
- **M15** (Wisdom, Understanding and Knowledge) — 1 term(s):
  - `G1128` gumnazō — `to train`

#### `upon` — 2 clusters, 2 term-rows

- **M03** (Grief, Sorrow and Mourning) — 1 term(s):
  - `G4729` stenochōreō — `to press upon`
- **M05** (Love, Compassion and Kindness) — 1 term(s):
  - `G2026` epoikodomeō — `to build up/upon`

#### `wicked` — 2 clusters, 2 term-rows

- **M10b** (Wickedness, Evil and Abomination) — 1 term(s):
  - `H7563` ra.sha — `wicked`
- **M26** (Righteousness and Justice) — 1 term(s):
  - `H7561` ra.sha — `be wicked`

#### `without` — 2 clusters, 2 term-rows

- **M33** (Peace, Rest and Quietness) — 1 term(s):
  - `G0253` alupos — `without anxiety`
- **M34** (Perseverance, Endurance and Steadfastness) — 1 term(s):
  - `G0679` aptaistos — `without falling`

---

## §4. Sister-Strong's sense-suffix spread (28 Strong's roots have sense-rows in 2+ clusters)

Strong's numbers with letter-suffixes (e.g. `H2930A`, `H2930B`) are sense-splits of one Hebrew/Greek lemma. When the sense-rows sit in different clusters, the same lexical root is split analytically by sense.

| Root | Senses | Cluster spread |
|---|---|---|
| `H0205` | `H0205H` a.ven — `evil: trouble` [M10]; `H0205G` a.ven — `evil: trouble` [M10b] | M10, M10b (2 clusters) |
| `H1984` | `H1984H` ha.lal — `to boast: boast` [M08]; `H1984C` ha.lal — `to be foolish` [M16]; `H1984I` ha.lal — `to boast: rave madly` [M16]; `H1984B` ha.lal — `to boast: praise` [M22] | M08, M16, M22 (3 clusters) |
| `H2254` | `H2254C` cha.val — `be in labour` [M03]; `H2254B` cha.val — `to destroy` [M10] | M03, M10 (2 clusters) |
| `H2256` | `H2256B` che.vel — `pain` [M03]; `H2256M` che.vel — `pain` [M03]; `H2256D` che.vel — `destruction` [M10] | M03, M10 (2 clusters) |
| `H2388` | `H2388G` cha.zaq — `to strengthen: strengthen` [M23]; `H2388H` cha.zaq — `to strengthen: hold` [M23]; `H2388I` cha.zaq — `to strengthen: ensure` [M23]; `H2388J` cha.zaq — `to strengthen: prevail over` [M23]; `H2388K` cha.zaq — `to strengthen: persevere` [M34] | M23, M34 (2 clusters) |
| `H2416` | `H2416A` chay — `alive` [M25]; `H2416B` chay — `kinsfolk` [M25]; `H2416C` chay.yah — `living thing` [M25]; `H2416D` chay.yah — `community` [M44] | M25, M44 (2 clusters) |
| `H2428` | `H2428A` cha.yil — `strength: soldiers` [FLAG]; `H2428H` cha.yil — `strength: rich` [FLAG]; `H2428I` cha.yil — `strength: worthy` [FLAG]; `H2428G` cha.yil — `strength` [M23] | FLAG, M23 (2 clusters) |
| `H2654` | `H2654B` cha.phats — `to sway` [FLAG]; `H2654A` cha.phets — `to delight in` [M04] | FLAG, M04 (2 clusters) |
| `H2790` | `H2790A` cha.rash — `to plow/plot` [M14]; `H2790B` cha.resh — `be quiet` [M33] | M14, M33 (2 clusters) |
| `H2836` | `H2836A` cha.shaq — `to desire` [M28]; `H2836B` cha.shaq — `to connect` [M44] | M28, M44 (2 clusters) |
| `H2844` | `H2844B` chat — `shattered` [FLAG]; `H2844A` chat — `terror` [M01] | FLAG, M01 (2 clusters) |
| `H3722` | `H3722A` kip.per — `to atone` [M11]; `H3722B` ka.phar — `to cover` [M38] | M11, M38 (2 clusters) |
| `H4893` | `H4893A` mish.chat — `mutilation` [M07]; `H4893B` ma.she.chat — `corruption` [M10] | M07, M10 (2 clusters) |
| `H5081` | `H5081G` na.div — `noble: willing` [M09]; `H5081H` na.div — `noble` [M34] | M09, M34 (2 clusters) |
| `H5162` | `H5162G` na.cham — `to be sorry: comfort` [M05]; `H5162H` na.cham — `to be sorry: relent` [M11] | M05, M11 (2 clusters) |
| `H5273` | `H5273A` na.im — `pleasant` [M04]; `H5273B` na.im — `musical` [M22] | M04, M22 (2 clusters) |
| `H5749` | `H5749A` ud — `to return` [M11]; `H5749B` ud — `to testify` [M13] | M11, M13 (2 clusters) |
| `H6186` | `H6186A` a.rakh — `to arrange` [FLAG]; `H6186B` a.rakh — `to value` [M26] | FLAG, M26 (2 clusters) |
| `H6696` | `H6696B` tsur — `to provoke` [M02]; `H6696C` tsur — `to form` [M12]; `H6696A` tsur — `to confine` [M23] | M02, M12, M23 (3 clusters) |
| `H6862` | `H6862B` tsar — `distress` [M03]; `H6862D` tsar — `hard` [M23]; `H6862C` tsar — `enemy` [M44] | M03, M23, M44 (3 clusters) |
| `H6869` | `H6869B` tsa.rah — `distress` [M03]; `H6869A` bats.tsa.rah — `dearth` [M24]; `H6869C` tsa.rah — `vexer` [M24] | M03, M24 (2 clusters) |
| `H6887` | `H6887B` tsa.rar — `to constrain` [FLAG]; `H6887D` tsa.rar — `to vex` [FLAG]; `H6887C` tsa.rar — `to distress` [M24]; `H6887E` tsa.rar — `to rival` [M28] | FLAG, M24, M28 (3 clusters) |
| `H6918` | `H6918H` qa.dosh — `holy: saint` [M12]; `H6918G` qa.dosh — `holy` [M22] | M12, M22 (2 clusters) |
| `H7280` | `H7280A` ra.ga — `to disturb` [FLAG]; `H7280B` ra.ga — `to rest` [M33] | FLAG, M33 (2 clusters) |
| `H7311` | `H7311B` ra.mam — `be rotten` [FLAG]; `H7311A` rum — `to exalt` [M08] | FLAG, M08 (2 clusters) |
| `H7451` | `H7451C` ra.ah — `distress: harm` [M03]; `H7451A` ra — `bad: harmful` [M27]; `H7451I` ra.ah — `distress: evil` [M27] | M03, M27 (2 clusters) |
| `H7725` | `H7725N` shuv — `to return: recall` [M11]; `H7725O` shuv — `to return: repent` [M45] | M11, M45 (2 clusters) |
| `H8088` | `H8088A` she.ma — `sound` [M13]; `H8088B` she.ma — `report` [M41] | M13, M41 (2 clusters) |

---

## Summary

- **Total non-T2 terms scanned:** 1752
- **Clusters in scope:** 47
- **Exact gloss collisions:** 22
- **Gloss-base collisions:** 37
- **Token collisions (≥ 2 clusters):** 127
- **Sister-Strong's spread across clusters:** 28
