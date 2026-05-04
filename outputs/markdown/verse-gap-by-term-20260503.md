# Verse Gap by Term — Where the Unclassified Verses Live

_Generated 2026-05-03T13:29:48Z_  ·  source: `scripts/_exploratory_verse_gap_by_term_v1_20260503.py`

For each active OWNER term: how many verses STEP pulled in, how many have been classified by VC, and the gap (verses_pulled − vc_classified). The gap is the cohort of verses that are in `wa_verse_records` for this term but have no `verse_context` row at all.

## Programme totals

- Active OWNER terms: **2,538**
- Total verses pulled (`wa_verse_records`): **57,619**
- Total vc rows written: **39,585**  (68.7% classified)
- Of vc rows: relevant=33,533, anchor=4,507
- **Total gap (pulled but not classified): 18,034**  (31.3% of pulled)

## Per-registry — top 30 by absolute gap

| Reg | Word | Terms | Verses pulled | VC classified | Gap | Gap % |
|---:|---|---:|---:|---:|---:|---:|
| 187 | strength | 176 | 3,380 | 1,985 | 1,395 | 41.3% |
| 57 | evil | 26 | 1,303 | 283 | 1,020 | 78.3% |
| 173 | will | 28 | 1,375 | 454 | 921 | 67.0% |
| 156 | surrender | 11 | 787 | 1 | 786 | 99.9% |
| 117 | peace | 56 | 1,429 | 687 | 742 | 51.9% |
| 198 | might | 22 | 881 | 275 | 606 | 68.8% |
| 6 | anointing | 51 | 735 | 136 | 599 | 81.5% |
| 5 | anguish | 45 | 735 | 160 | 575 | 78.2% |
| 4 | anger | 35 | 823 | 250 | 573 | 69.6% |
| 51 | distress | 71 | 1,182 | 633 | 549 | 46.4% |
| 90 | innocence | 20 | 800 | 337 | 463 | 57.9% |
| 197 | authority | 70 | 1,942 | 1,487 | 455 | 23.4% |
| 210 | deadness | 11 | 689 | 242 | 447 | 64.9% |
| 121 | praise | 35 | 783 | 400 | 383 | 48.9% |
| 99 | kindness | 20 | 912 | 561 | 351 | 38.5% |
| 44 | despair | 15 | 1,002 | 653 | 349 | 34.8% |
| 167 | unity | 7 | 562 | 218 | 344 | 61.2% |
| 151 | sorrow | 46 | 671 | 329 | 342 | 51.0% |
| 185 | flesh | 16 | 661 | 322 | 339 | 51.3% |
| 123 | pride | 48 | 800 | 487 | 313 | 39.1% |
| 76 | holiness | 8 | 418 | 110 | 308 | 73.7% |
| 52 | division | 25 | 395 | 124 | 271 | 68.6% |
| 33 | courage | 25 | 625 | 356 | 269 | 43.0% |
| 140 | seeking | 6 | 541 | 279 | 262 | 48.4% |
| 89 | iniquity | 9 | 375 | 114 | 261 | 69.6% |
| 126 | purpose | 11 | 400 | 161 | 239 | 59.8% |
| 149 | slander | 17 | 313 | 86 | 227 | 72.5% |
| 98 | justice | 33 | 875 | 656 | 219 | 25.0% |
| 159 | testimony | 9 | 277 | 66 | 211 | 76.2% |
| 176 | worship | 30 | 718 | 508 | 210 | 29.2% |

## Per-term — top 50 by absolute gap

Terms with the largest unclassified-verse cohort. These are the highest-leverage VC processing targets.

| Reg | Word | Strong's | Translit | Gloss | Lang | Pulled | Classified | Gap | Gap% |
|---:|---|---|---|---|---|---:|---:|---:|---:|
| 156 | surrender | `H0859E` | at.ten | you [f.p.] | H | 359 | 0 | 359 | 100.0% |
| 57 | evil | `H1931` | hu | he/she/it | H | 291 | 0 | 291 | 100.0% |
| 185 | flesh | `H3318G` | ya.tsa | to come out: come | H | 323 | 46 | 277 | 85.8% |
| 44 | despair | `H3808` | lo | not | H | 331 | 56 | 275 | 83.1% |
| 167 | unity | `H1571` | gam | also | H | 404 | 132 | 272 | 67.3% |
| 117 | peace | `H5769G` | o.lam | forever: enduring | H | 272 | 0 | 272 | 100.0% |
| 187 | strength | `H4725` | ma.qom | place | H | 295 | 34 | 261 | 88.5% |
| 89 | iniquity | `H4480A` | min- | from | H | 284 | 25 | 259 | 91.2% |
| 140 | seeking | `H4672` | ma.tsa | to find | H | 320 | 74 | 246 | 76.9% |
| 57 | evil | `H3605` | kol | all | H | 285 | 41 | 244 | 85.6% |
| 173 | will | `H6213A` | a.sah | to make: do | H | 263 | 20 | 243 | 92.4% |
| 76 | holiness | `H6944G` | qo.desh | holiness | H | 286 | 44 | 242 | 84.6% |
| 210 | deadness | `H4191` | mut | to die | H | 299 | 62 | 237 | 79.3% |
| 156 | surrender | `H0859D` | at.tem | you [m.p.] | H | 234 | 0 | 234 | 100.0% |
| 90 | innocence | `H2009` | hin.neh | behold | H | 319 | 98 | 221 | 69.3% |
| 126 | purpose | `H4616` | ma.an | because | H | 228 | 38 | 190 | 83.3% |
| 4 | anger | `H0639G` | aph | face: anger | H | 212 | 23 | 189 | 89.2% |
| 57 | evil | `H1992` | hem.mah | they [masc.] | H | 189 | 0 | 189 | 100.0% |
| 149 | slander | `H7272` | re.gel | foot | H | 229 | 43 | 186 | 81.2% |
| 173 | will | `H3427` | ya.shav | to dwell | H | 216 | 40 | 176 | 81.5% |
| 175 | wonder | `H0176B` | o | desire | H | 175 | 0 | 175 | 100.0% |
| 173 | will | `H1980G` | ha.lakh | to go: went | H | 220 | 50 | 170 | 77.3% |
| 198 | might | `H0935G` | bo | to come [in]: come | H | 296 | 126 | 170 | 57.4% |
| 57 | evil | `H4994` | na | please | H | 195 | 27 | 168 | 86.2% |
| 121 | praise | `H0259` | e.chad | one | H | 181 | 14 | 167 | 92.3% |
| 173 | will | `H5159` | na.cha.lah | inheritance | H | 183 | 18 | 165 | 90.2% |
| 100 | knowledge | `H3045` | ya.da | to know | H | 421 | 264 | 157 | 37.3% |
| 117 | peace | `H6635B` | tsa.va | Hosts | H | 156 | 0 | 156 | 100.0% |
| 111 | mercy | `H5750` | od | still | H | 170 | 14 | 156 | 91.8% |
| 6 | anointing | `H8081` | she.men | oil | H | 176 | 28 | 148 | 84.1% |
| 5 | anguish | `H7451C` | ra.ah | distress: harm | H | 151 | 4 | 147 | 97.4% |
| 90 | innocence | `H2005` | hen | look! | H | 223 | 77 | 146 | 65.5% |
| 204 | name | `H8034` | shem | name | H | 364 | 223 | 141 | 38.7% |
| 117 | peace | `H6635A` | tsa.va | army | H | 136 | 0 | 136 | 100.0% |
| 185 | flesh | `H1320` | ba.sar | flesh | H | 205 | 75 | 130 | 63.4% |
| 187 | strength | `H3966` | me.od | much | H | 220 | 93 | 127 | 57.7% |
| 197 | authority | `H7235A` | ra.vah | to multiply | H | 211 | 88 | 123 | 58.3% |
| 60 | faithfulness | `H5414G` | na.tan | to give: give | H | 242 | 120 | 122 | 50.4% |
| 197 | authority | `H3027G` | yad | hand | H | 375 | 255 | 120 | 32.0% |
| 99 | kindness | `H0120G` | a.dam | man | H | 162 | 48 | 114 | 70.4% |
| 58 | experience | `H7200G` | ra.ah | to see: see | H | 273 | 165 | 108 | 39.6% |
| 123 | pride | `H7311B` | ra.mam | be rotten | H | 184 | 77 | 107 | 58.2% |
| 146 | shame | `H0954` | bosh | be ashamed | H | 113 | 10 | 103 | 91.2% |
| 187 | strength | `H0341` | o.yev | enemy | H | 244 | 141 | 103 | 42.2% |
| 98 | justice | `H8199` | sha.phat | to judge | H | 182 | 80 | 102 | 56.0% |
| 4 | anger | `H2534` | che.mah | rage | H | 115 | 15 | 100 | 87.0% |
| 51 | distress | `H7451I` | ra.ah | distress: evil | H | 137 | 37 | 100 | 73.0% |
| 198 | might | `H3627` | ke.li | article/utensil | H | 104 | 5 | 99 | 95.2% |
| 123 | pride | `H7311A` | rum | to exalt | H | 184 | 85 | 99 | 53.8% |
| 6 | anointing | `G5547` | christos | Christ | G | 120 | 22 | 98 | 81.7% |

## Terms 100% unclassified — 212 terms

Terms where every pulled verse is unclassified — VC processing was never started for these terms.

Top 30 by verses pulled:

| Reg | Word | Strong's | Translit | Gloss | Lang | Status | Verses |
|---:|---|---|---|---|---|---|---:|
| 156 | surrender | `H0859E` | at.ten | you [f.p.] | H | `extracted` | 359 |
| 57 | evil | `H1931` | hu | he/she/it | H | `extracted` | 291 |
| 117 | peace | `H5769G` | o.lam | forever: enduring | H | `extracted_theological_anchor` | 272 |
| 156 | surrender | `H0859D` | at.tem | you [m.p.] | H | `extracted` | 234 |
| 57 | evil | `H1992` | hem.mah | they [masc.] | H | `extracted` | 189 |
| 175 | wonder | `H0176B` | o | desire | H | `extracted` | 175 |
| 117 | peace | `H6635B` | tsa.va | Hosts | H | `extracted_theological_anchor` | 156 |
| 117 | peace | `H6635A` | tsa.va | army | H | `extracted_theological_anchor` | 136 |
| 151 | sorrow | `H2491A` | cha.lal | slain: killed | H | `extracted` | 74 |
| 151 | sorrow | `H2491B` | cha.lal | profaned | H | `extracted` | 74 |
| 52 | division | `H2506B` | che.leq | smoothness | H | `extracted` | 62 |
| 198 | might | `H4481` | min- | from | H | `extracted` | 60 |
| 198 | might | `H1768` | di | that | H | `extracted` | 60 |
| 156 | surrender | `H0859C` | at | you [f.s.] | H | `extracted` | 57 |
| 147 | sin | `G3303` | men | on the other hand | G | `extracted` | 50 |
| 151 | sorrow | `H2490C` | cha.lal | to profane/begin: begin | H | `extracted` | 50 |
| 6 | anointing | `H1101A` | ba.lal | to mix | H | `extracted` | 40 |
| 6 | anointing | `H1101B` | ba.lal | to feed | H | `extracted` | 40 |
| 5 | anguish | `H6696C` | tsur | to form | H | `extracted` | 32 |
| 5 | anguish | `H7114B` | qa.tsar | to reap | H | `extracted` | 32 |
| 6 | anointing | `H3332G` | ya.tsaq | to pour: pour | H | `extracted` | 28 |
| 86 | impurity | `H2007` | hen.nah | they [fem.] | H | `extracted` | 28 |
| 99 | kindness | `H5980` | um.mah | close | H | `extracted` | 28 |
| 5 | anguish | `G5561` | chōra | country | G | `extracted` | 27 |
| 86 | impurity | `H1932` | hu | he/she/it | H | `extracted` | 22 |
| 6 | anointing | `H1881` | dat | law | H | `extracted` | 21 |
| 170 | weakness | `G0770H` | astheneō | be weak: ill | G | `extracted` | 18 |
| 103 | love | `H1730I` | dod | beloved: male relative | H | `extracted_thin` | 17 |
| 177 | worth | `H4634` | ma.a.ra.khah | rank | H | `extracted` | 17 |
| 158 | terror | `H8047G` | sham.mah | horror: destroyed | H | `extracted` | 15 |

## Partial-coverage terms — 176 terms with ≥50% gap and ≥20 verses pulled

Top 30 by gap size:

| Reg | Word | Strong's | Gloss | Verses pulled | Classified | Gap% |
|---:|---|---|---|---:|---:|---:|
| 185 | flesh | `H3318G` | to come out: come | 323 | 46 | 85.8% |
| 44 | despair | `H3808` | not | 331 | 56 | 83.1% |
| 167 | unity | `H1571` | also | 404 | 132 | 67.3% |
| 187 | strength | `H4725` | place | 295 | 34 | 88.5% |
| 89 | iniquity | `H4480A` | from | 284 | 25 | 91.2% |
| 140 | seeking | `H4672` | to find | 320 | 74 | 76.9% |
| 57 | evil | `H3605` | all | 285 | 41 | 85.6% |
| 173 | will | `H6213A` | to make: do | 263 | 20 | 92.4% |
| 76 | holiness | `H6944G` | holiness | 286 | 44 | 84.6% |
| 210 | deadness | `H4191` | to die | 299 | 62 | 79.3% |
| 90 | innocence | `H2009` | behold | 319 | 98 | 69.3% |
| 126 | purpose | `H4616` | because | 228 | 38 | 83.3% |
| 4 | anger | `H0639G` | face: anger | 212 | 23 | 89.2% |
| 149 | slander | `H7272` | foot | 229 | 43 | 81.2% |
| 173 | will | `H3427` | to dwell | 216 | 40 | 81.5% |
| 173 | will | `H1980G` | to go: went | 220 | 50 | 77.3% |
| 198 | might | `H0935G` | to come [in]: come | 296 | 126 | 57.4% |
| 57 | evil | `H4994` | please | 195 | 27 | 86.2% |
| 121 | praise | `H0259` | one | 181 | 14 | 92.3% |
| 173 | will | `H5159` | inheritance | 183 | 18 | 90.2% |
| 111 | mercy | `H5750` | still | 170 | 14 | 91.8% |
| 6 | anointing | `H8081` | oil | 176 | 28 | 84.1% |
| 5 | anguish | `H7451C` | distress: harm | 151 | 4 | 97.4% |
| 90 | innocence | `H2005` | look! | 223 | 77 | 65.5% |
| 185 | flesh | `H1320` | flesh | 205 | 75 | 63.4% |
| 187 | strength | `H3966` | much | 220 | 93 | 57.7% |
| 197 | authority | `H7235A` | to multiply | 211 | 88 | 58.3% |
| 60 | faithfulness | `H5414G` | to give: give | 242 | 120 | 50.4% |
| 99 | kindness | `H0120G` | man | 162 | 48 | 70.4% |
| 123 | pride | `H7311B` | be rotten | 184 | 77 | 58.2% |

## Coverage-gap distribution across terms

| Gap % bucket | # terms | Description |
|---|---:|---|
| 0% | 1467 | fully classified |
| 1-25% | 323 | mostly classified |
| 26-50% | 222 | moderately classified |
| 51-75% | 141 | mostly unclassified |
| 76-99% | 126 | largely unclassified |
| 100% | 212 | never started |
