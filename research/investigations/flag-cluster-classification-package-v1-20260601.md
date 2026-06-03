# FLAG cluster — classification package (Claude AI / chat)

**Type:** AI-facing classification package · **Generated:** 2026-06-01 · **Terms:** 433 live FLAG terms.

## Required inputs (self-declaration)

- **Brief:** none separate — this package is self-contained for the FLAG-term classification task.
- **Structural inputs (embedded below):** §A cluster taxonomy (targets) · §C the 433 FLAG terms.
- **Controlling principles (embedded):** §B disposition rules incl. the T1/T2 ontology and the two governing principles.
- **Authoritative provenance (background, not required to act):** `wa-cluster-overview [current]` (cluster model); term-anchor model (clusters are agnostic to registries — a term reaches a cluster only via its own meaning, not its source registry).
- **Pre-decisions already made:** these 433 terms are confirmed live (active verse usage) and currently parked in the FLAG holding cluster; they must each be dispositioned.
- **Out of scope:** characteristic/sub-group placement *within* a cluster (a later step); verse-level relevance; any DB write (CC applies the returned patch).

## Task

For **each** FLAG term, assign exactly one **disposition**:

| disposition | meaning | target_clusters |
|---|---|---|
| `cluster` | a T1 characteristic term — names an inner-life faculty/characteristic that belongs to a cluster | one cluster code (the primary home) |
| `boundary` | genuinely sits between clusters — its meaning bridges two (rarely three) characteristics | the 2–3 candidate cluster codes |
| `t2` | a recipient / effect / modifier / particle / function word — NOT a faculty itself (prepositions, negation, "beloved", etc.) | [] |
| `set_aside` | no inner-life content, or not genuinely attested (object/place/relation only) | [] |

## Disposition rules

1. **Verse meaning is the data.** Classify on what the term *means in use*, not its source registry. Clusters are agnostic to registries.
2. **T1 vs T2 (ontology):** T1 = the characteristic *in operation* (the faculty) → `cluster`. T2 = the recipient/effect/modifier/particle → `t2`. *Example: "beloved" (agapētos) is T2, not the love faculty.*
3. **Particles / function words → `t2`.** A term whose lexical HINT sprays across many clusters (e.g. *para*, *sun*, *mē*) is almost always a preposition/particle — that spray is the signal, not a real multi-cluster membership.
4. **Use `boundary` sparingly** — only when the term truly carries two distinct characteristics, not merely co-occurs with other terms.
5. **`set_aside`** for terms with no inner-life faculty content (physical objects, places, pure relations) or zero genuine attestation.
6. **HINT is a suggestion only** (lexical match of transliteration against a cluster's example-term gloss). Confirm or override on meaning.
7. **Record a one-line `reason` for every term**, grounded in its meaning (all observations recorded — the two governing principles).

## Output (return EXACTLY this JSON, no prose)

```json
{
  "package": "flag-cluster-classification-v1-20260601",
  "classifications": [
    {"strongs": "G2588", "disposition": "cluster",  "target_clusters": ["M30"],        "reason": "kardia = heart; seat of the inner life; core characteristic term."},
    {"strongs": "G3844", "disposition": "t2",       "target_clusters": [],              "reason": "preposition 'para'; function word, not a faculty."},
    {"strongs": "Hxxxx", "disposition": "boundary", "target_clusters": ["M05","M07"],  "reason": "carries both X and Y characteristics."},
    {"strongs": "Hyyyy", "disposition": "set_aside", "target_clusters": [],             "reason": "no inner-life content / not attested."}
  ]
}
```

Process in **batches** (e.g. Greek-high-span first, then Hebrew) — the term list is in a stable order so batches are reproducible. Return one JSON block per batch covering every `strongs` in that batch.


## §A. Cluster taxonomy — the `cluster` / `boundary` targets

| code | short_name | description | example terms |
|---|---|---|---|
| M01 | Fear | Fear, Dread and Terror | afraid (emfobos), afraid (ya.re), agony (sha.vats), amazement (thambos… |
| M02 | Anger | Anger, Wrath and Indignation | anger (parorgismos), be angry (a.naph), be angry (qa.tsaph), be disple… |
| M03 | Grief | Grief, Sorrow and Mourning | anguish (odunē), anguish (o.du.ne), anguish (sunochē), anguish (tsu.qa… |
| M04 | Joy | Joy, Gladness and Delight | be cheerful (euthumeō), be cheerful (ba.lag), be confident (tharreō), … |
| M05 | Love | Love, Compassion and Kindness | affectionate (filostorgos), assembly (ekklēsia), assembly (miq.ra), as… |
| M06 | Hate | Hate, Contempt and Hostility | abhorrence (de.ra.on), adversary (qim), be hostile (a.yav), contempt (… |
| M07 | Shame | Shame, Disgrace and Humiliation | be ashamed (aischunō), be ashamed (bosh), be ashamed (cha.pher), be hu… |
| M08 | Pride | Pride, Arrogance and Boasting | arrogance (fusiōsis), arrogance (za.don), arrogant (huperēfanos), arro… |
| M09 | Humility | Humility, Meekness and Submission | be gentle (metriopatheō), be humble (ka.na), be humble (tsa.na), contr… |
| M10 | Sin | Sin, Guilt and Transgression | apostasy (apostasia), atonement (kip.pu.rim), be guilty (a.sham), be u… |
| M10b | Wickedness | Wickedness, Evil and Abomination | abominable (bdeluktos), abomination (bdelugma), abomination (shiq.quts… |
| M10c | Defilement | Defilement and Impurity | defilement (miasmos), defilement (molusmos), impurity (akatharsia), im… |
| M11 | Repentance | Repentance, Forgiveness and Restoration | forgiveness (afesis), forgiveness (se.li.chah), forgiving (sal.lach), … |
| M12 | Purity | Purity, Holiness and Consecration | be pure (ta.her), clean (katharos), cleansing (katharismos), clearness… |
| M13 | Truth | Truth, Faithfulness and Integrity | be faithful (a.man), be truthful (alētheuō), confirmation (bebaiōsis),… |
| M14 | Deceit | Deceit, Hypocrisy and Falsehood | be cunning (katasofizomai), be devious (luz), charm (la.chash), crafti… |
| M15 | Wisdom | Wisdom, Understanding and Knowledge | arbiter (meristēs), be ignorant (agnoeō), be of sound mind (sōfroneō),… |
| M16 | Folly | Folly, Madness and Foolishness | be foolish (mōrainō), be foolish (ya.al), be insane (parafroneō), be m… |
| M17 | Counsel | Counsel, Planning and Purpose | beginning (archē), beginning (te.chil.lah), cause (div.rah), counsel (… |
| M18 | Hope | Hope, Expectation and Waiting | eager expectation (apokaradokia), expectation (prosdokia), expectation… |
| M19 | Trust | Trust, Confidence and Security | be careful (frontizō), be convinced (pistoō), be eager (zēloō), be eag… |
| M20 | Doubt | Doubt, Despair and Anxiety | be anxious (da.ag), be discouraged (athumeō), be disheartened (ka.ah),… |
| M21 | Prayer | Prayer, Worship and Devotion | God-loving (filotheos), a vow/prayer (euchē), be devout (sebomai), fas… |
| M22 | Praise | Praise, Thanksgiving and Glory | adornment (ha.da.rah), blessing (be.ra.khah), extolling (ro.mam), glor… |
| M23 | Strength | Strength, Power and Dominion | active energy (energeia), almighty (pantokratōr), authority (exousia),… |
| M24 | Weakness | Weakness, Vulnerability and Suffering | afflicted (a.ni), affliction (o.ni), be sick (noseō), be sick (da.vah)… |
| M25 | Life | Life, Vitality and Existence | alive (chay), be refreshed (na.phash), kinsfolk (chay), living (chay.y… |
| M26 | Righteousness | Righteousness and Justice | Righteousness [God] (tse.deq), accountable (hupodikos), avenging (ekdi… |
| M27 | Evil | Evil, Wickedness and Abomination | bad: harmful (ra), be desolate: destroyed (sha.mem), be evil (ra.a), d… |
| M28 | Envy | Envy, Greed and Lust | debauchery (aselgeia), debauchery (asōtia), desirable thing (cha.mu.da… |
| M29 | Desire | Desire, Longing and Will | acceptance (ra.tson), be willing (ya.al), be willing (na.dav), be will… |
| M30 | Obedience | Obedience and Disobedience | be insensitive (ta.phash), disobedience (apeitheia), disobedience (par… |
| M31 | Faith | Faith, Belief and Unbelief | be permitted (exesti exon), called (klētos), calling (klēsis), devout … |
| M33 | Peace | Peace, Rest and Quietness | Peace [God] (sha.lom ), be at peace (eirēneuō), be quiet (siōpaō), be … |
| M34 | Perseverance | Perseverance, Endurance and Steadfastness | a struggle (agonia), a struggle (agōnia), be bold (apotolmaō), be bold… |
| M35 | Testing | Testing, Temptation and Trial | fight (agōn), not stumbling (aproskopos), stumbling (proskopē), stumbl… |
| M36 | Service | Service, Slavery and Labour | be a slave (douleuō), female slave (doulē), service (a.vo.dah), servic… |
| M37 | Calling | Calling, Election and Vocation | firstborn (prōtotokos), foreknowledge (prognōsis), to call (on)/name (… |
| M38 | Salvation | Salvation, Redemption and Deliverance | free gift (dōrea), free gift (dōrēma), propitiation (hilasmos), propit… |
| M39 | Blessing | Blessing, Favour and Grace | be good (te.ev), be good (ya.tav), be gracious (cha.nan), be gracious … |
| M41 | Remembrance | Remembrance and Memory | attentive (qash.shav), attentive (qash.shuv), attentiveness (qe.shev),… |
| M42 | Speech | Speech, Voice and Cry | answer (ma.a.neh), be silent (sigaō), be silent (cha.shah), cry (rin.n… |
| M43 | Prophecy | Prophecy and Revelation | discernment (diakrisis), image (eikōn), image (tse.lem), insight (aist… |
| M44 | Relational | Relational Disposition | brotherhood (adelfotēs), community (chay.yah), companion (cha.ver), en… |
| M45 | Transformation | Transformation and Renewal | change (cha.li.phah), conformed (summorfos), new (kainos), renewal (an… |
| M46 | Abundance | Abundance, Prosperity and Wealth | abundance (mar.veh), abundance (rov), goodness (agathōsunē), greatness… |

## §C. FLAG terms to classify (433) — stable order (language, span desc)

span = distinct active-span verses (usage). HINT = lexical-match suggestion (confirm/override on meaning).

| strongs | translit | gloss | lang | span | reg | HINT |
|---|---|---|---|--:|---|---|
| G2588 | kardia | heart | Greek | 120 | 183 | M30 |
| G3686 | onoma | name | Greek | 120 | 204 |  |
| G5547 | christos | Christ | Greek | 120 | 6 | M14 |
| G3844 | para | from/with/beside | Greek | 118 | 4 | M05;M07;M10;M16;M17;M28;M30;M33 |
| G4862 | sun | with | Greek | 99 | 184 | M03;M04;M07;M09;M10;M14;M15;M16;M22;M23;M26;M34;M44;M46 |
| G2919 | krinō | to judge | Greek | 97 | 160 | M14;M15;M26 |
| G4561 | sarx | flesh | Greek | 85 | 185 |  |
| G0027 | agapētos | beloved | Greek | 60 | 103 |  |
| G3361 | mē | not | Greek | 60 | 173 |  |
| G4352 | proskuneō | to worship | Greek | 54 | 176 |  |
| G3779 | houtōs | thus(-ly) | Greek | 53 | 198 |  |
| G5590G | psuchē | soul | Greek | 46 | 182 |  |
| G1377 | diōkō | to pursue | Greek | 44 | 214 |  |
| G3958 | paschō | to suffer | Greek | 41 | 163 | M03 |
| G3313 | meros | part | Greek | 40 | 52 |  |
| G5056 | telos | goal/tax | Greek | 39 | 126 |  |
| G3842 | pantote | always | Greek | 38 | 191 |  |
| G5590H | psuchē | soul: life | Greek | 33 | 182 |  |
| G3195 | mellō | to ensue | Greek | 31 | 173 |  |
| G1242 | diathēkē | covenant | Greek | 30 | 34 |  |
| G4893 | suneidesis | conscience | Greek | 29 | 73 |  |
| G3563 | nous | mind | Greek | 22 | 112 |  |
| G4137 | plēroō | to fulfill | Greek | 20 | 198 |  |
| G0230 | alēthōs | truly | Greek | 18 | 164 |  |
| G2560 | kakōs | badly | Greek | 16 | 57 |  |
| G3804 | pathēma | suffering | Greek | 16 | 23 |  |
| G3077 | lu.pe | grief | Greek | 14 | 71 | M03 |
| G0303 | ana | each | Greek | 12 | 51 | M02;M12;M15;M23;M41;M45 |
| G1271 | dianoia | mind | Greek | 12 | 112 |  |
| G5177 | tunchanō | to obtain/happen | Greek | 12 | 94 | M21;M37 |
| G1375 | diōgmos | persecution | Greek | 9 | 214 |  |
| G2920 | krisis | judgment | Greek | 9 | 24 | M14;M26;M43 |
| G3843 | pantōs | surely | Greek | 8 | 191 |  |
| G5021 | tassō | to appoint | Greek | 8 | 197 | M09;M23 |
| G5590J | psuchē | soul: person | Greek | 8 | 182 |  |
| G3837 | pantachou | everywhere | Greek | 7 | 191 |  |
| G4993 | sōfroneō | be of sound mind | Greek | 6 | 112 | M15 |
| G5590I | psuchē | soul: myself | Greek | 6 | 182 |  |
| G1346 | dikaiōs | rightly | Greek | 5 | 98 | M26 |
| G2965 | kuōn | dog | Greek | 5 | 176 |  |
| G3310 | meris | part | Greek | 5 | 52 | M15 |
| G3346 | metatithēmi | to transport | Greek | 5 | 135 |  |
| G5591 | psuchikos | natural | Greek | 5 | 182 | M15 |
| G0747 | archēgos | founder | Greek | 4 | 197 |  |
| G0870 | afobōs | fearlessly | Greek | 4 | 61 |  |
| G2234 | hēdeōs | gladly | Greek | 3 | 42 |  |
| G2553 | kakopatheō | to endure | Greek | 3 | 23 |  |
| G3609 | oikeios | of one’s household | Greek | 3 | 187 |  |
| G3806 | pathos | passion | Greek | 3 | 115 |  |
| G4400 | procheirizō | to appoint | Greek | 3 | 173 |  |
| G4880 | sunapothnēskō | to die with | Greek | 3 | 210 |  |
| G4997 | sōfrosunē | mental soundness | Greek | 3 | 142 | M15 |
| G0841 | autarkeia | self-sufficiency | Greek | 2 | 29 | M15 |
| G2115 | euthumos | encouraging | Greek | 2 | 35 |  |
| G2236 | hēdista | most gladly | Greek | 2 | 42 |  |
| G2907 | kreas | meat | Greek | 2 | 185 |  |
| G3663 | homoiopathēs | like | Greek | 2 | 23 |  |
| G3838 | pantelēs | completely | Greek | 2 | 191 |  |
| G3840 | pantothen | from all sides | Greek | 2 | 191 |  |
| G4090 | pikrōs | bitterly | Greek | 2 | 13 |  |
| G4275 | proeidon | to foresee | Greek | 2 | 26 |  |
| G4777 | sunkakopatheō | to suffer with | Greek | 2 | 23 |  |
| G0043 | ankalē | arm | Greek | 1 | 51 |  |
| G0055 | hagnōs | purely | Greek | 1 | 125 |  |
| G0095 | adikōs | unjustly | Greek | 1 | 98 |  |
| G0317 | anankastōs | necessarily | Greek | 1 | 51 |  |
| G0552 | apeiros | unacquainted | Greek | 1 | 157 |  |
| G0563 | aperispastōs | undistracted | Greek | 1 | 46 |  |
| G0574 | haplōs | without reserve | Greek | 1 | 46 |  |
| G0811 | asōtōs | wildly | Greek | 1 | 39 |  |
| G1259 | diallassō | be reconciled | Greek | 1 | 130 |  |
| G1876 | epanankes | necessarily | Greek | 1 | 51 |  |
| G2552 | kakopatheia | suffering | Greek | 1 | 23 |  |
| G3116 | makrothumōs | patiently | Greek | 1 | 115 |  |
| G3510 | nefros | mind | Greek | 1 | 112 |  |
| G3743 | hosiōs | devoutly | Greek | 1 | 111 |  |
| G3805 | pathētos | suffering | Greek | 1 | 23 |  |
| G3832 | panoiki | with all the house | Greek | 1 | 187 |  |
| G3839 | pantē | always | Greek | 1 | 191 |  |
| G4049 | perispaō | to distract | Greek | 1 | 46 |  |
| G4184 | polusplanchnos | very compassionate | Greek | 1 | 23 |  |
| G4191 | ponēroteros | more evil | Greek | 1 | 57 |  |
| G4290 | prothumōs | eagerly | Greek | 1 | 35 |  |
| G4353 | proskunētēs | worshiper | Greek | 1 | 176 |  |
| G4415 | prōtotokia | birthright | Greek | 1 | 103 |  |
| G4823 | sumbouleuō | to consult | Greek | 1 | 32 |  |
| G4833 | summorfoomai | to make like | Greek | 1 | 209 |  |
| G4944 | sunōdinō | to labor together | Greek | 1 | 2 |  |
| G4994 | sōfronizō | to train | Greek | 1 | 112 | M15 |
| G4996 | sōfronōs | in self-control | Greek | 1 | 112 |  |
| G5112 | tolmēroteron | more boldly | Greek | 1 | 16 |  |
| G5364 | filanthrōpōs | benevolently | Greek | 1 | 3 |  |
| G5390 | filofronōs | hospitably | Greek | 1 | 3 |  |
| G5430 | fronimōs | shrewdly | Greek | 1 | 160 |  |
| G0772 | asthenēs | weak | Greek | 0 | 187 | M24 |
| G0928 | basanizō | to torture: anguish | Greek | 0 | 5 | M03 |
| G1100 | glōssa | tongue | Greek | 0 | 212 |  |
| G1169A | deos | fear | Greek | 0 | 61 | M01 |
| G1169B | deilos | timid | Greek | 0 | 61 | M01 |
| G1777 | enochos | liable for | Greek | 0 | 73 |  |
| G1870 | epaischunomai | be ashamed of | Greek | 0 | 146 |  |
| G2308 | thelēsis | will | Greek | 0 | 43 |  |
| G2631 | katakrima | condemnation | Greek | 0 | 73 |  |
| G4658 | potheinos | desirable | Greek | 0 | 43 |  |
| G6041 | zēleuō | to envy | Greek | 0 | 56 |  |
| G6110 | agalliama | a leap for joy | Greek | 0 | 97 |  |
| G6347 | anischus | without strength | Greek | 0 | 187 |  |
| G6354 | antakouō | to listen in turn | Greek | 0 | 213 |  |
| G6657 | barukardios | heavy-hearted | Greek | 0 | 183 |  |
| G6928 | dikastērion | court of justice | Greek | 0 | 98 |  |
| G7143 | eksarkizomai | to tear off flesh | Greek | 0 | 185 |  |
| G7214 | enakouō | to listen to attentively | Greek | 0 | 213 |  |
| G7681 | thnēsimaios | decaying flesh | Greek | 0 | 185 |  |
| G7684 | thrasukardios | bold-hearted | Greek | 0 | 183 |  |
| G7774 | kakofrōn | evil-minded | Greek | 0 | 112 |  |
| G7798 | kardioō | to take heart | Greek | 0 | 183 |  |
| G7949 | katafobos | fear | Greek | 0 | 61 |  |
| G8272 | megalofrōn | high-minded | Greek | 0 | 112 |  |
| G8419 | nōthrokardios | dull of heart | Greek | 0 | 183 |  |
| G8878 | prauthumos | gentle-minded | Greek | 0 | 112 |  |
| G9073 | sthenos | strength (physical) | Greek | 0 | 187 |  |
| G9107 | sklērokardios | hard-hearted | Greek | 0 | 183 |  |
| G9131 | sofoo | to give wisdom | Greek | 0 | 174 |  |
| G9165 | stereokardios | hard-hearted | Greek | 0 | 183 |  |
| G9320 | suneufrainomai | be glad with | Greek | 0 | 186 |  |
| G9559 | huperischuō | to excel in strength | Greek | 0 | 187 |  |
| G9610 | hupsēlokardios | a proud heart | Greek | 0 | 183 |  |
| H5971H | am | People's [Gate] | Hebrew | 430 | 99 |  |
| H5971I | am | [Ibleam]-am | Hebrew | 430 | 99 |  |
| H8034 | shem | name | Hebrew | 364 | 204 | M10 |
| H0859B | t.ti | you [f.s.] | Hebrew | 359 | 156 | M01 |
| H3820A | lev | heart | Hebrew | 331 | 183 |  |
| H3605 | kol | all | Hebrew | 285 | 57 | M07 |
| H6963A | qol | voice | Hebrew | 273 | 146 |  |
| H6963B | qol | frivolity | Hebrew | 273 | 146 |  |
| H6963K | qol | voice: [sound of] | Hebrew | 273 | 146 |  |
| H6963L | qol | voice: listen | Hebrew | 273 | 146 |  |
| H1285 | be.rit | covenant | Hebrew | 236 | 34 |  |
| H3966 | me.od | much | Hebrew | 220 | 187 |  |
| H4941G | mish.pat | justice: judgement | Hebrew | 208 | 98 |  |
| H3824 | le.vav | heart | Hebrew | 207 | 183 |  |
| H1320 | ba.sar | flesh | Hebrew | 205 | 185 |  |
| H0136 | a.do.na | Lord [God] | Hebrew | 187 | 117 |  |
| H7311B | ra.mam | be rotten | Hebrew | 184 | 123 |  |
| H8199 | sha.phat | to judge | Hebrew | 182 | 98 |  |
| H5315H | ne.phesh | soul: life | Hebrew | 180 | 182 |  |
| H5315G | ne.phesh | soul | Hebrew | 179 | 182 |  |
| H5750 | od | still | Hebrew | 170 | 111 |  |
| H2233H | ze.ra | seed: children | Hebrew | 160 | 180 |  |
| H4941H | mish.pat | justice | Hebrew | 158 | 24 |  |
| H2416E | chay.yim | life | Hebrew | 137 | 8 |  |
| H5315I | ne.phesh | soul: myself | Hebrew | 126 | 182 |  |
| H2346G | cho.mah | wall | Hebrew | 121 | 178 |  |
| H6310G | peh | lip | Hebrew | 120 | 32 |  |
| H1431 | ga.dal | to magnify | Hebrew | 114 | 187 |  |
| H3678G | kis.se | throne | Hebrew | 114 | 197 |  |
| H0410G | el | God | Hebrew | 107 | 196 |  |
| H6963H | qol | voice: sound | Hebrew | 107 | 146 |  |
| H3615G | ka.lah | to end: finish | Hebrew | 103 | 102 |  |
| H2428A | cha.yil | strength: soldiers | Hebrew | 101 | 187 | M23 |
| H3162B | ya.che.dav | together | Hebrew | 97 | 167 |  |
| H2015 | ha.phakh | to overturn | Hebrew | 92 | 120 | M14 |
| H6106G | e.tsem | bone | Hebrew | 88 | 187 |  |
| H3772H | ka.rat | to cut: make [covenant] | Hebrew | 87 | 34 |  |
| H2220 | ze.ro.a | arm | Hebrew | 84 | 187 |  |
| H5315J | ne.phesh | soul: person | Hebrew | 83 | 182 |  |
| H2603B | cha.nan | be loathsome | Hebrew | 72 | 23 | M39 |
| H2654B | cha.phats | to sway | Hebrew | 69 | 42 |  |
| H6186A | a.rakh | to arrange | Hebrew | 67 | 177 | M26;M39 |
| H1168I | ba.al | [Bamoth]-baal | Hebrew | 64 | 199 |  |
| H1397 | ga.ver | great man | Hebrew | 64 | 187 |  |
| H2506A | che.leq | portion | Hebrew | 62 | 52 |  |
| H2506B | che.leq | smoothness | Hebrew | 62 | 52 |  |
| H4043 | ma.gen | shield | Hebrew | 60 | 151 |  |
| H3615H | ka.lah | to end: destroy | Hebrew | 53 | 102 |  |
| H7706 | shad.day | Almighty [God] | Hebrew | 48 | 117 |  |
| H5315L | ne.phesh | soul: appetite | Hebrew | 45 | 182 |  |
| H3162A | ya.chad | unitedness | Hebrew | 43 | 167 |  |
| H2008 | hen.nah | here/thus | Hebrew | 41 | 90 |  |
| H2233G | ze.ra | seed | Hebrew | 38 | 180 |  |
| H2470H | cha.lah | be weak: ill | Hebrew | 38 | 71 | M03 |
| H3615J | ka.lah | to end: expend | Hebrew | 37 | 102 |  |
| H2428H | cha.yil | strength: rich | Hebrew | 36 | 187 | M23 |
| H1588M | gan | garden | Hebrew | 35 | 151 | M02;M08 |
| H3335G | ya.tsar | to form: formed | Hebrew | 35 | 51 |  |
| H6231 | a.shaq | to oppress | Hebrew | 35 | 214 | M28;M44 |
| H0748 | a.rakh | to prolong | Hebrew | 34 | 116 | M26;M39 |
| H2796 | cha.rash cha.ra.shim | artificer | Hebrew | 34 | 117 |  |
| H5923 | ol | yoke | Hebrew | 34 | 187 |  |
| H3513H | ka.ved | to honor: heavy | Hebrew | 32 | 15 |  |
| H1167G | ba.al | master | Hebrew | 31 | 199 |  |
| H2600 | chin.nam | for nothing | Hebrew | 31 | 73 |  |
| H0374 | e.phah | ephah | Hebrew | 29 | 177 |  |
| H6187 | e.rekh | valuation | Hebrew | 29 | 177 |  |
| H0194 | u.lay | perhaps | Hebrew | 28 | 160 |  |
| H0860 | a.ton | she-ass | Hebrew | 28 | 187 |  |
| H7185 | qa.shah | to harden | Hebrew | 28 | 51 |  |
| H1730G | dod | beloved | Hebrew | 27 | 103 |  |
| H2498 | cha.laph | to pass | Hebrew | 27 | 202 |  |
| H3629 | kil.yah | kidney | Hebrew | 26 | 26 |  |
| H8552 | ta.mam | to finish | Hebrew | 26 | 147 |  |
| H3474 | ya.shar | to smooth | Hebrew | 25 | 98 | M13 |
| H6887D | tsa.rar | to vex | Hebrew | 25 | 51 | M06;M24 |
| H0543 | a.men | amen | Hebrew | 24 | 44 |  |
| H1777 | din | to judge | Hebrew | 24 | 98 | M03;M08;M15;M24;M28;M41 |
| H5397 | ne.sha.mah | breath | Hebrew | 24 | 184 |  |
| H1823 | de.mut | likeness | Hebrew | 22 | 201 |  |
| H6887B | tsa.rar | to constrain | Hebrew | 22 | 51 | M06;M24 |
| H2423 | che.va | beast | Hebrew | 19 | 187 |  |
| H2513A | chel.qah | portion | Hebrew | 19 | 52 |  |
| H2552 | cha.mam | to warm | Hebrew | 19 | 4 |  |
| H3617 | ka.lah | consumption | Hebrew | 19 | 102 |  |
| H5178A | ne.cho.shet | bronze | Hebrew | 19 | 105 |  |
| H6106H | e.tsem | bone: same | Hebrew | 18 | 187 |  |
| H1730I | dod | beloved: male relative | Hebrew | 17 | 103 |  |
| H1779 | din | judgment | Hebrew | 17 | 98 | M03;M08;M15;M24;M28;M41 |
| H4634 | ma.a.ra.khah | rank | Hebrew | 17 | 177 |  |
| H7607 | she.er | flesh | Hebrew | 16 | 185 |  |
| H8201 | she.phet | judgment | Hebrew | 16 | 24 |  |
| H0750 | a.rekh | slow | Hebrew | 15 | 116 |  |
| H1419K | ga.dol | great: old | Hebrew | 15 | 187 |  |
| H2470B | cha.lah | to beg | Hebrew | 15 | 71 | M03 |
| H3335H | ya.tsar | to form: potter | Hebrew | 15 | 51 |  |
| H6087B | a.tsav | to shape | Hebrew | 15 | 71 | M03;M24;M27 |
| H6233 | o.sheq | oppression | Hebrew | 15 | 214 |  |
| H1167H | ba.al | master: husband | Hebrew | 14 | 199 |  |
| H7114A | qa.tser | be short | Hebrew | 14 | 5 |  |
| H1167I | ba.al | master: men | Hebrew | 13 | 199 |  |
| H1167K | ba.al | master: [master of] | Hebrew | 13 | 199 |  |
| H5315M | ne.phesh | soul: dead | Hebrew | 13 | 182 |  |
| H6963I | qol | voice: thunder | Hebrew | 13 | 146 |  |
| H6963J | qol | voice: message | Hebrew | 13 | 146 |  |
| H0424 | e.lah | oak | Hebrew | 12 | 187 | M16 |
| H1419J | ga.dol | Great [Sea] | Hebrew | 12 | 187 |  |
| H1593 | gan.nah | garden | Hebrew | 12 | 151 |  |
| H5315K | ne.phesh | soul: animal | Hebrew | 12 | 182 |  |
| H1166I | ba.al | rule: to marry | Hebrew | 11 | 199 |  |
| H3245 | ya.sad | to found | Hebrew | 11 | 32 |  |
| H5998 | a.mal | to toil | Hebrew | 11 | 71 | M03;M05 |
| H7308 | ru.ach | spirit | Hebrew | 11 | 4 |  |
| H2011H | hin.nom | [Topheth of son of] Hinnom | Hebrew | 10 | 90 |  |
| H2023G | hor | [Mount] Hor | Hebrew | 10 | 120 | M01;M03;M06;M10;M12;M16;M23 |
| H2470A | cha.lah | be weak: weak | Hebrew | 10 | 71 | M03 |
| H2504 | cha.lats | loin | Hebrew | 10 | 183 |  |
| H2787 | cha.rar | to scorch | Hebrew | 10 | 51 |  |
| H3615I | ka.lah | to end: decides | Hebrew | 10 | 102 |  |
| H3772J | ka.rat | to cut: lack | Hebrew | 10 | 34 |  |
| H6693 | tsuq | to press | Hebrew | 10 | 51 |  |
| H6944H | qo.desh | Most Holy Place | Hebrew | 10 | 28 | M22 |
| H0551 | om.nam | truly | Hebrew | 9 | 191 |  |
| H1167J | ba.al | master: owning | Hebrew | 9 | 199 |  |
| H1730H | dod | beloved | Hebrew | 9 | 103 |  |
| H2795 | che.resh | deaf | Hebrew | 9 | 117 |  |
| H3678I | kis.se | throne: seat | Hebrew | 9 | 197 |  |
| H4635 | ma.a.re.khet | row | Hebrew | 9 | 177 |  |
| H4865 | mish.be.tsot | filigree | Hebrew | 9 | 2 |  |
| H7668 | she.ver | grain | Hebrew | 9 | 18 | M24 |
| H2233I | ze.ra | seed: semen | Hebrew | 8 | 180 |  |
| H3039A | ya.did | beloved | Hebrew | 8 | 103 |  |
| H4436G | mal.kah | Queen [of Sheba] | Hebrew | 8 | 199 |  |
| H5201 | na.tar | to keep | Hebrew | 8 | 4 |  |
| H5798G | uz.za | [Garden of] Uzza | Hebrew | 8 | 74 |  |
| H6045 | in.yan | task | Hebrew | 8 | 214 |  |
| H0629 | os.par.na | diligently | Hebrew | 7 | 48 |  |
| H1598 | ga.nan | to defend | Hebrew | 7 | 151 |  |
| H2428I | cha.yil | strength: worthy | Hebrew | 7 | 187 | M23 |
| H3826 | lib.bah | heart | Hebrew | 7 | 183 |  |
| H2513B | chel.qah | smoothness | Hebrew | 6 | 52 |  |
| H3335I | ya.tsar | to form: plan | Hebrew | 6 | 112 |  |
| H3825 | le.vav | heart | Hebrew | 6 | 183 |  |
| H4114 | mah.pe.khah | overthrow | Hebrew | 6 | 120 |  |
| H4714J | mits.ra.yim | [Brook of] Egypt | Hebrew | 6 | 123 |  |
| H6089B | e.tsev | vessel | Hebrew | 6 | 71 | M03 |
| H7280A | ra.ga | to disturb | Hebrew | 6 | 117 | M01;M33 |
| H0328B | it.ti | mutterer | Hebrew | 5 | 184 | M01 |
| H0552 | um.nam | truly | Hebrew | 5 | 44 |  |
| H2259 | cho.vel | pilot | Hebrew | 5 | 2 |  |
| H5317 | no.phet | honey | Hebrew | 5 | 182 |  |
| H6001B | a.mel | laborious | Hebrew | 5 | 71 | M24 |
| H8503 | takh.lit | limit | Hebrew | 5 | 102 |  |
| H1594 | gin.nah | garden | Hebrew | 4 | 151 |  |
| H3514 | ko.ved | heaviness | Hebrew | 4 | 15 |  |
| H4245B | ma.cha.lah | sickness | Hebrew | 4 | 71 |  |
| H4518 | me.naq.qiy.yah | bowl | Hebrew | 4 | 90 |  |
| H4928 | mish.ma.at | guard | Hebrew | 4 | 213 |  |
| H5946 | el.yon | Most High [God] | Hebrew | 4 | 117 |  |
| H0181 | ud | firebrand | Hebrew | 3 | 187 |  |
| H0425L | e.lah | [Valley of] Elah | Hebrew | 3 | 187 | M16 |
| H1321 | be.shar | flesh | Hebrew | 3 | 185 |  |
| H1748 | du.mam | silence | Hebrew | 3 | 117 |  |
| H2258A | cha.vol | pledge | Hebrew | 3 | 2 |  |
| H2258B | cha.vo.lah | pledge | Hebrew | 3 | 2 |  |
| H2508 | cha.laq | portion | Hebrew | 3 | 199 |  |
| H2573 | che.met | bottle | Hebrew | 3 | 178 |  |
| H2758 | cha.rish | plowing | Hebrew | 3 | 117 |  |
| H2793H | cho.resh | wood | Hebrew | 3 | 117 |  |
| H3157L | yiz.re.el | [Valley of] Jezreel | Hebrew | 3 | 180 |  |
| H3513J | ka.ved | to honor: dull | Hebrew | 3 | 15 |  |
| H4026G | mig.dal | [Hananel] Tower | Hebrew | 3 | 187 |  |
| H6090B | o.tsev | idol | Hebrew | 3 | 71 | M03 |
| H6217 | a.shu.qim | oppression | Hebrew | 3 | 214 |  |
| H6946H | qa.desh | [Meribath]-kadesh | Hebrew | 3 | 28 |  |
| H0248 | ez.ro.a | arm | Hebrew | 2 | 187 |  |
| H0578 | a.nah | to lament | Hebrew | 2 | 151 | M04;M13;M24;M28 |
| H1166H | ba.al | rule: to rule | Hebrew | 2 | 199 |  |
| H1434 | ge.di.lim | tassel | Hebrew | 2 | 187 |  |
| H1588G | gan | Garden [of Uzza] | Hebrew | 2 | 151 | M02;M08 |
| H2011G | hin.nom | [Topheth of] Hinnom | Hebrew | 2 | 90 |  |
| H2023H | hor | [Mount] Hor | Hebrew | 2 | 120 | M01;M03;M06;M10;M12;M16;M23 |
| H2118 | za.chach | to remove | Hebrew | 2 | 187 |  |
| H2256C | cho.ve.lim | union | Hebrew | 2 | 2 |  |
| H2346H | cho.mah | [Broad] Wall | Hebrew | 2 | 178 |  |
| H2631 | cha.san | to possess | Hebrew | 2 | 197 |  |
| H2794 | cho.resh | artificer | Hebrew | 2 | 117 |  |
| H2799 | cha.ro.shet | carving | Hebrew | 2 | 117 |  |
| H2844B | chat | shattered | Hebrew | 2 | 61 | M01;M07;M08;M10;M19;M27;M33 |
| H2910 | tu.chot | inner parts | Hebrew | 2 | 183 | M19 |
| H3513I | ka.ved | to honor: many | Hebrew | 2 | 15 |  |
| H3764 | kor.se | throne | Hebrew | 2 | 197 |  |
| H4206A | me.zach | belt | Hebrew | 2 | 187 |  |
| H4206B | me.zi.ach | belt | Hebrew | 2 | 187 |  |
| H4245A | ma.cha.leh | sickness | Hebrew | 2 | 71 |  |
| H4254 | ma.cha.la.tsah | robe | Hebrew | 2 | 187 |  |
| H4281 | ma.cha.re.shah | plowshare | Hebrew | 2 | 117 |  |
| H4618 | ma.a.nah | furrow | Hebrew | 2 | 214 |  |
| H4642 | ma.a.shaq.qah | oppression | Hebrew | 2 | 214 |  |
| H5315N | ne.phesh | soul: neck | Hebrew | 2 | 182 |  |
| H5587B | se.ip.pim | disquietings | Hebrew | 2 | 112 |  |
| H5808 | iz.zuz | mighty | Hebrew | 2 | 74 |  |
| H5822 | oz.niy.yah | vulture | Hebrew | 2 | 74 |  |
| H6031A | a.nah | be occupied | Hebrew | 2 | 198 | M04;M13;M24;M28 |
| H6106I | e.tsem | bone: body | Hebrew | 2 | 187 |  |
| H6383 | pil.i | incomprehensible | Hebrew | 2 | 175 |  |
| H6599 | pit.gam | edict | Hebrew | 2 | 128 |  |
| H6756A | tsal.mon | [Mount] Zalmon | Hebrew | 2 | 201 |  |
| H8651 | te.ra | door | Hebrew | 2 | 187 |  |
| H0197H | u.lam | Hall [of Justice] | Hebrew | 1 | 98 |  |
| H0197I | u.lam | Hall [of the Throne] | Hebrew | 1 | 98 |  |
| H0206G | a.ven | [Valley of] Aven | Hebrew | 1 | 51 | M10;M10b |
| H0240 | a.zen | weapon | Hebrew | 1 | 213 |  |
| H0436G | e.lon | [Diviners'] Oak | Hebrew | 1 | 187 |  |
| H1079 | bal | mind | Hebrew | 1 | 183 | M01;M07;M45 |
| H1180 | ba.a.li | Baal [used for God] | Hebrew | 1 | 117 |  |
| H1286 | be.rit | [Baal]-berith | Hebrew | 1 | 34 |  |
| H1585 | ge.mar | to complete | Hebrew | 1 | 117 |  |
| H1588H | gan | [Beth]-haggan | Hebrew | 1 | 151 | M02;M08 |
| H1773 | de.yo | ink | Hebrew | 1 | 151 |  |
| H1825 | dim.yon | likeness | Hebrew | 1 | 201 |  |
| H1831 | de.ma | juice | Hebrew | 1 | 188 | M33 |
| H2016 | he.phekh | contrariness | Hebrew | 1 | 120 |  |
| H2018 | ha.phe.khah | overthrow | Hebrew | 1 | 120 |  |
| H2021 | ho.tsen | weapon | Hebrew | 1 | 120 |  |
| H2235A | ze.ro.a | vegetable | Hebrew | 1 | 180 |  |
| H2235B | ze.re.on | vegetable | Hebrew | 1 | 180 |  |
| H2260 | chib.bel | mast | Hebrew | 1 | 2 |  |
| H2272 | cha.var.bu.rah | spot | Hebrew | 1 | 62 |  |
| H2574H | cha.mat | [Zobah]-Hamath | Hebrew | 1 | 178 |  |
| H2579 | cha.mat rab.bah | Hamath the great | Hebrew | 1 | 178 |  |
| H2594 | cha.ni.nah | favor | Hebrew | 1 | 23 |  |
| H2759 | cha.ri.shi | scorching | Hebrew | 1 | 117 |  |
| H2791A | che.resh | silently | Hebrew | 1 | 117 |  |
| H2791B | che.resh | craftily | Hebrew | 1 | 117 |  |
| H3517 | ke.ve.dut | heaviness | Hebrew | 1 | 15 |  |
| H3676 | kes | throne | Hebrew | 1 | 197 |  |
| H3678H | kis.se | [Hall of] the Throne | Hebrew | 1 | 197 |  |
| H3737 | kar.be.la | helmet | Hebrew | 1 | 51 |  |
| H3821 | lev | heart | Hebrew | 1 | 183 |  |
| H4026H | mig.dal | Tower [of the Hundred] | Hebrew | 1 | 187 |  |
| H4026I | mig.dal | Tower [Of the Ovens] | Hebrew | 1 | 187 |  |
| H4192 | lab.ben | [Muth-]labben | Hebrew | 1 | 210 |  |
| H4251 | ma.cha.luy | suffering | Hebrew | 1 | 71 |  |
| H4252 | ma.cha.laph | knife | Hebrew | 1 | 134 |  |
| H4263 | mach.mal | compassion | Hebrew | 1 | 179 | M05 |
| H4622 | ma.tsor | restraint | Hebrew | 1 | 142 |  |
| H4623 | ma.tsar | restraint | Hebrew | 1 | 142 |  |
| H4714I | mits.ra.yim | [Sea of] Egypt | Hebrew | 1 | 123 |  |
| H4941K | mish.pat | [Hall of] Judgment | Hebrew | 1 | 24 |  |
| H5330 | ne.tsach | to distinguish oneself | Hebrew | 1 | 55 | M34 |
| H5452 | se.var | to intend | Hebrew | 1 | 176 |  |
| H5588 | se.eph | divided | Hebrew | 1 | 112 |  |
| H5769H | o.lam | Everlasting [God] | Hebrew | 1 | 117 |  |
| H5796 | ez | goat | Hebrew | 1 | 74 |  |
| H6033 | a.na | to afflict | Hebrew | 1 | 71 | M02;M03;M04;M05;M09;M13;M19;M24;M28;M39;M42 |
| H6039 | e.nut | affliction | Hebrew | 1 | 71 | M28 |
| H6092 | a.tsev | worker | Hebrew | 1 | 71 |  |
| H6216 | a.shoq | oppressor | Hebrew | 1 | 214 |  |
| H6229 | a.saq | to contend | Hebrew | 1 | 214 |  |
| H6234 | osh.qah | oppression | Hebrew | 1 | 214 |  |
| H6697G | tsur | Rocks [of Goats] | Hebrew | 1 | 51 | M02;M12;M23 |
| H6941 | qe.do.ran.nit | mournfully | Hebrew | 1 | 113 |  |
| H6944I | qo.desh | [Way of] Holiness | Hebrew | 1 | 28 | M22 |
| H6968 | qo.me.miy.yut | uprightness | Hebrew | 1 | 187 |  |
| H7067G | qan.na | Jealous [God] | Hebrew | 1 | 117 | M02 |
| H7315 | rom | hight | Hebrew | 1 | 123 | M01;M08;M15 |
| H7317 | ro.mah | haughtily | Hebrew | 1 | 123 |  |
| H7433 | ra.mot  | Ramoth [Gilead] | Hebrew | 1 | 123 |  |
| H7465 | ro.ah | to shatter | Hebrew | 1 | 151 |  |
| H7490 | re.a | to break | Hebrew | 1 | 57 | M01;M15 |
| H7851H | shit.tim | [Valley of] Shittim | Hebrew | 1 | 31 |  |
| H7907 | sekh.vi | heart | Hebrew | 1 | 183 |  |
| H8400 | te.val.lul | defect | Hebrew | 1 | 6 | M07 |
| H8406 | te.var | to break | Hebrew | 1 | 18 |  |
| H0014 | a.vah | be willing | Hebrew | 0 | 43 | M01;M03;M04;M05;M08;M10;M14;M17;M18;M24;M28 |
| H0034 | ev.yon | needy | Hebrew | 0 | 43 |  |
| H0035 | a.viy.yo.nah | desire | Hebrew | 0 | 43 |  |
| H0193 | ul | strength | Hebrew | 0 | 187 |  |
| H0639 | aph | face: anger | Hebrew | 0 | 116 | M02;M06;M10;M18;M23 |
| H1101 | ba.lal | to mix | Hebrew | 0 | 6 |  |
| H1826 | da.mam | to silence: silent | Hebrew | 0 | 116 | M33 |
| H2119 | za.chal | to fear | Hebrew | 0 | 61 | M01 |
| H2388 | cha.zaq | to strengthen: strengthen | Hebrew | 0 | 187 | M23;M34 |
| H2428 | cha.yil | strength | Hebrew | 0 | 187 | M23 |
| H2502 | cha.lats | to arm | Hebrew | 0 | 187 |  |
| H2844 | chat | terror | Hebrew | 0 | 61 | M01;M07;M08;M10;M19;M27;M33 |
| H2898 | tuv | goodness | Hebrew | 0 | 103 |  |
| H3027 | yad | hand: power | Hebrew | 0 | 187 |  |
| H3068G | ye.ho.vah | YHWH/Yahweh | Hebrew | 0 | 117 |  |
| H3071 | ye.ho.vah nis.si | YHWH-Nissi | Hebrew | 0 | 117 |  |
| H3072 | ye.ho.vah tsid.qe.nu | YHWH-Tsidkenu | Hebrew | 0 | 117 |  |
| H3073 | ye.ho.vah sha.lom | YHWH-Shalom | Hebrew | 0 | 117 |  |
| H3176 | ya.chal | to wait: wait | Hebrew | 0 | 116 | M18 |
| H3332 | ya.tsaq | to pour: pour | Hebrew | 0 | 6 |  |
| H3581 | ko.ach | reptile | Hebrew | 0 | 187 | M23 |
| H4805G | me.ri | Egypt | Hebrew | 0 | 128 | M02;M30 |
| H5258 | ya.sakh | to pour | Hebrew | 0 | 6 |  |
| H5689 | a.gav | to lust | Hebrew | 0 | 43 | M28 |
| H5953 | a.lal | to thrust | Hebrew | 0 | 187 | M08;M16;M22 |
| H6106 | e.tsem | bone | Hebrew | 0 | 187 |  |
| H6440G | pa.neh | face: before | Hebrew | 0 | 112 |  |
| H6697 | tsur | rock | Hebrew | 0 | 187 | M02;M12;M23 |
| H7444 | ran.nen | to sing | Hebrew | 0 | 97 |  |
| H7725 | shuv | to return: turn back | Hebrew | 0 | 135 | M11;M41;M45 |
| H8632 | te.qoph | might | Hebrew | 0 | 187 |  |
