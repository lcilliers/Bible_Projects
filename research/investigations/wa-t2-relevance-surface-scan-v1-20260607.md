# T2 (Supplementary) — STEP-sense relevance surfacing

> READ-ONLY (`scripts/_assess_t2_relevance_surface.py`). Overlaps each parked T2 term's STEP sense-set against every named cluster's sense-envelope, idf-weighted so **distinctive** matches rank. A high score = the term's lexical sense lands in that cluster's semantic field → a candidate home for the eventual T2 rework. Candidate ≠ decision: the researcher judges.

- T2 active terms scored: **412** (of 620; the rest had no cluster-token overlap)
- Surfaced at score ≥ 6.0: **121**

## Surfaced candidates (strongest first)

| Score | T2 term | Gloss | Parked-under | Top candidate cluster(s) — matched sense tokens |
|---|---|---|---|---|
| 16.6 | H3201 ya.khol | be able | power | **M23 (Strength)** 16.6 [over, power, prevail, strength]  ·  **M46 (Abundance)** 4.2 [gain]  ·  **M35 (Testing)** 3.8 [endure] |
| 16.6 | H0817 a.sham | guilt [offering] | guilt | **M10 (Sin)** 16.6 [guilt, guilti, trespas, offer] |
| 15.2 | H7123 qe.ra | to read | to read | **M42 (Speech)** 15.2 [shout, aloud, call, out]  ·  **M37 (Calling)** 15.2 [read, summon, out, call]  ·  **M41 (Remembrance)** 4.2 [proclaim] |
| 12.5 | H7293 ra.hav | Rahab | Rahab | **M08 (Pride)** 12.5 [first, arrogance, pride]  ·  **M37 (Calling)** 4.2 [name]  ·  **M15 (Wisdom)** 4.2 [mean] |
| 12.5 | H6635B tsa.va | Hosts | peace | **M23 (Strength)** 12.5 [host, lord, almighty]  ·  **M26 (Righteousness)** 7.6 [righteous, god]  ·  **M33 (Peace)** 7.2 [peace, god] |
| 12.5 | H5943 il.lay | Most High [God] | Most High [God] | **M23 (Strength)** 12.5 [host, lord, almighty]  ·  **M26 (Righteousness)** 7.6 [righteous, god]  ·  **M33 (Peace)** 7.2 [peace, god] |
| 12.5 | H5144A na.zar | to dedicate | to dedicate | **M12 (Purity)** 12.5 [consecrate, dedicate, sacr]  ·  **M30 (Obedience)** 4.2 [keep] |
| 12.5 | H3027W yad | hand: owner | hand: owner | **M23 (Strength)** 12.5 [power, strength, rule]  ·  **M44 (Relational)** 4.2 [share]  ·  **M43 (Prophecy)** 4.2 [sign] |
| 12.5 | H2632 che.sen | authority | power | **M23 (Strength)** 12.5 [author, power, strength] |
| 12.5 | G5400 fobētron | fearful thing | fear | **M01 (Fear)** 12.5 [terror, terrible, fear] |
| 12.5 | G3000 latreuō | to minister | worship | **M36 (Service)** 12.5 [serve, service, minister]  ·  **M10 (Sin)** 7.9 [offer, act]  ·  **M27 (Evil)** 4.2 [sacrific] |
| 12.5 | G2900 krataios | mighty | mighty | **M23 (Strength)** 12.5 [strong, mighty, power] |
| 12.5 | G2373 thumoō | to anger | anger | **M02 (Anger)** 12.5 [anger, angry, provoke]  ·  **M30 (Obedience)** 4.2 [become] |
| 12.5 | G2192 echō | to have/be | to have/be | **M23 (Strength)** 12.5 [power, subject, hold]  ·  **M15 (Wisdom)** 8.3 [present, knowledge]  ·  **M30 (Obedience)** 4.2 [keep] |
| 12.5 | G1654 eleēmosunē | charity | charity | **M05 (Love)** 12.5 [kind, compassion, pity]  ·  **M46 (Abundance)** 4.2 [substance]  ·  **M28 (Envy)** 4.2 [money] |
| 12.5 | G1415 dunatos | able | power | **M23 (Strength)** 12.5 [author, mighty, power]  ·  **M33 (Peace)** 7.6 [being, god]  ·  **M26 (Righteousness)** 7.2 [act, god] |
| 12.5 | G1414 dunateō | be able | be able | **M23 (Strength)** 12.5 [strong, mighty, power]  ·  **M21 (Prayer)** 3.8 [show]  ·  **M05 (Love)** 3.8 [show] |
| 12.1 | H7665 sha.var | to break | will | **M24 (Weakness)** 12.1 [crippl, break, crush]  ·  **M03 (Grief)** 3.8 [crush]  ·  **M42 (Speech)** 3.5 [out] |
| 12.1 | H7235A ra.vah | to multiply | to multiply | **M23 (Strength)** 12.1 [enlarge, grow, great]  ·  **M30 (Obedience)** 4.2 [become]  ·  **M10 (Sin)** 4.2 [transgres] |
| 12.1 | H4941J mish.pat | justice: custom | justice: custom | **M26 (Righteousness)** 12.1 [judg, justice, act]  ·  **M13 (Truth)** 4.2 [right]  ·  **M17 (Counsel)** 3.8 [plan] |
| 12.1 | H4941I mish.pat | justice: rule | justice: rule | **M26 (Righteousness)** 12.1 [judg, justice, act]  ·  **M23 (Strength)** 4.2 [rule]  ·  **M13 (Truth)** 4.2 [right] |
| 12.1 | G6048 katadikē | judgment | condemnation | **M26 (Righteousness)** 12.1 [judg, condemnation, act]  ·  **M10 (Sin)** 3.8 [act] |
| 12.1 | G5379 filoneikia | love of dispute | love | **M02 (Anger)** 12.1 [strife, rivalry, dispute]  ·  **M28 (Envy)** 3.8 [love]  ·  **M15 (Wisdom)** 3.8 [dispute] |
| 12.1 | G3948 paroxusmos | stirring up | stirring up | **M02 (Anger)** 12.1 [anger, angry, dispute]  ·  **M26 (Righteousness)** 3.8 [act]  ·  **M15 (Wisdom)** 3.8 [dispute] |
| 12.1 | G3619 oikodomē | building | building | **M05 (Love)** 12.1 [build, encourage, love]  ·  **M43 (Prophecy)** 4.2 [spiritual]  ·  **M15 (Wisdom)** 4.2 [word] |
| 12.1 | G3618 oikodomeō | to build | strength | **M05 (Love)** 12.1 [build, encourage, love]  ·  **M15 (Wisdom)** 8.3 [word, knowledge]  ·  **M43 (Prophecy)** 4.2 [spiritual] |
| 11.8 | H4672 ma.tsa | to find | seeking | **M37 (Calling)** 11.8 [encounter, meet, out]  ·  **M19 (Trust)** 8.3 [secur, secure]  ·  **M15 (Wisdom)** 8.3 [devise, present] |
| 8.3 | H8632B te.qoph | might | might | **M23 (Strength)** 8.3 [strength, might] |
| 8.3 | H8334 sha.rat | to minister | worship | **M36 (Service)** 8.3 [serve, minister] |
| 8.3 | H7621 she.vu.ah | oath | calling | **M07 (Shame)** 8.3 [innocence, curse] |
| 8.3 | H7453 re.a | neighbor | neighbor | **M44 (Relational)** 8.3 [companion, fellow]  ·  **M05 (Love)** 4.2 [friend] |
| 8.3 | H7413 ra.mah | high place | high place | **M08 (Pride)** 8.3 [high, height] |
| 8.3 | H7270 ra.gal | to spy | slander | **M15 (Wisdom)** 8.3 [mean, teach]  ·  **M42 (Speech)** 7.2 [slander, out]  ·  **M14 (Deceit)** 3.8 [slander] |
| 8.3 | H7200G ra.ah | to see: see | experience | **M15 (Wisdom)** 8.3 [present, perceive]  ·  **M21 (Prayer)** 7.9 [after, show]  ·  **M37 (Calling)** 7.6 [choose, out] |
| 8.3 | H7130H qe.rev | entrails: inner parts | heart | **M15 (Wisdom)** 8.3 [sense, thought] |
| 8.3 | H7043 qa.lal | to lighten | contempt | **M07 (Shame)** 8.3 [curse, dishonour]  ·  **M31 (Faith)** 4.2 [little]  ·  **M06 (Hate)** 4.2 [contempt] |
| 8.3 | H6293 pa.ga | to fall on | intercession | **M37 (Calling)** 8.3 [encounter, meet]  ·  **M35 (Testing)** 4.2 [strike]  ·  **M21 (Prayer)** 4.2 [intercession] |
| 8.3 | H6172 er.vah | nakedness | nakedness | **M07 (Shame)** 8.3 [shame, indecency] |
| 8.3 | H6094 ats.tse.vet | injury | grief | **M03 (Grief)** 8.3 [pain, sorrow]  ·  **M24 (Weakness)** 4.2 [hurt] |
| 8.3 | H5730A e.den | delicacy | delicacy | **M04 (Joy)** 8.3 [delight, dainty]  ·  **M46 (Abundance)** 4.2 [luxury] |
| 8.3 | H5414G na.tan | to give: give | faithfulness | **M12 (Purity)** 8.3 [consecrate, dedicate]  ·  **M11 (Repentance)** 7.6 [permit, out]  ·  **M22 (Praise)** 7.0 [report, give] |
| 8.3 | H5327B na.tsah | to desolate | to desolate | **M27 (Evil)** 8.3 [ruin, desolate]  ·  **M34 (Perseverance)** 3.8 [fall]  ·  **M02 (Anger)** 3.8 [fall] |
| 8.3 | H5031 ne.vi.ah | prophetess | prophetess | **M14 (Deceit)** 8.3 [false, prophet]  ·  **M42 (Speech)** 4.2 [song]  ·  **M15 (Wisdom)** 4.2 [word] |
| 8.3 | H5030 na.vi | prophet | courage | **M14 (Deceit)** 8.3 [false, prophet] |
| 8.3 | H4751 mar | bitter | anguish | **M03 (Grief)** 8.3 [bitter, pain]  ·  **M42 (Speech)** 4.2 [cry]  ·  **M10b (Wickedness)** 3.8 [wicked] |
| 8.3 | H4574 ma.a.dan | delicacy | delight | **M04 (Joy)** 8.3 [delight, dainty] |
| 8.3 | H4194 ma.vet | death | death | **M24 (Weakness)** 8.3 [death, dead] |
| 8.3 | H4191 mut | to die | deadness | **M24 (Weakness)** 8.3 [death, put] |
| 8.3 | H3027X yad | hand: swear | hand: swear | **M23 (Strength)** 8.3 [power, strength]  ·  **M44 (Relational)** 4.2 [share]  ·  **M43 (Prophecy)** 4.2 [sign] |
| 8.3 | H3027V yad | hand: certainly | hand: certainly | **M23 (Strength)** 8.3 [power, strength]  ·  **M44 (Relational)** 4.2 [share]  ·  **M43 (Prophecy)** 4.2 [sign] |
| 8.3 | H3027U yad | hand: undertake | hand: undertake | **M23 (Strength)** 8.3 [power, strength]  ·  **M44 (Relational)** 4.2 [share]  ·  **M43 (Prophecy)** 4.2 [sign] |
| 8.3 | H3027T yad | hand: expend | hand: expend | **M23 (Strength)** 8.3 [power, strength]  ·  **M44 (Relational)** 4.2 [share]  ·  **M43 (Prophecy)** 4.2 [sign] |
| 8.3 | H3027S yad | hand: vow | hand: vow | **M23 (Strength)** 8.3 [power, strength]  ·  **M44 (Relational)** 4.2 [share]  ·  **M43 (Prophecy)** 4.2 [sign] |
| 8.3 | H3027R yad | hand: donate | hand: donate | **M23 (Strength)** 8.3 [power, strength]  ·  **M44 (Relational)** 4.2 [share]  ·  **M43 (Prophecy)** 4.2 [sign] |
| 8.3 | H3027Q yad | hand: spacious | hand: spacious | **M23 (Strength)** 8.3 [power, strength]  ·  **M44 (Relational)** 4.2 [share]  ·  **M43 (Prophecy)** 4.2 [sign] |
| 8.3 | H3027P yad | hand: bank | hand: bank | **M23 (Strength)** 8.3 [power, strength]  ·  **M44 (Relational)** 4.2 [share]  ·  **M43 (Prophecy)** 4.2 [sign] |
| 8.3 | H3027O yad | hand: tool | hand: tool | **M23 (Strength)** 8.3 [power, strength]  ·  **M44 (Relational)** 4.2 [share]  ·  **M43 (Prophecy)** 4.2 [sign] |
| 8.3 | H3027M yad | hand: monument | hand: monument | **M23 (Strength)** 8.3 [power, strength]  ·  **M44 (Relational)** 4.2 [share]  ·  **M43 (Prophecy)** 4.2 [sign] |
| 8.3 | H3027L yad | hand: times | hand: times | **M23 (Strength)** 8.3 [power, strength]  ·  **M44 (Relational)** 4.2 [share]  ·  **M43 (Prophecy)** 4.2 [sign] |
| 8.3 | H3027K yad | hand: to | hand: to | **M23 (Strength)** 8.3 [power, strength]  ·  **M44 (Relational)** 4.2 [share]  ·  **M43 (Prophecy)** 4.2 [sign] |
| 8.3 | H3027J yad | hand: by | hand: by | **M23 (Strength)** 8.3 [power, strength]  ·  **M44 (Relational)** 4.2 [share]  ·  **M43 (Prophecy)** 4.2 [sign] |
| 8.3 | H3027I yad | hand: themselves | hand: themselves | **M23 (Strength)** 8.3 [power, strength]  ·  **M44 (Relational)** 4.2 [share]  ·  **M43 (Prophecy)** 4.2 [sign] |
| 8.3 | H3027H yad | hand: power | hand: power | **M23 (Strength)** 8.3 [power, strength]  ·  **M44 (Relational)** 4.2 [share]  ·  **M43 (Prophecy)** 4.2 [sign] |
| 8.3 | H3027G yad | hand | hand | **M23 (Strength)** 8.3 [power, strength]  ·  **M44 (Relational)** 4.2 [share]  ·  **M43 (Prophecy)** 4.2 [sign] |
| 8.3 | H2417 chay | living | living | **M25 (Life)** 8.3 [alive, liv] |
| 8.3 | H1819 da.mah | to resemble | thought | **M15 (Wisdom)** 8.3 [think, resemble] |
| 8.3 | H1368 gib.bor | mighty man | dread | **M23 (Strength)** 8.3 [strong, mighty]  ·  **M08 (Pride)** 4.2 [man] |
| 8.3 | H0516 al tash.chet | Do Not Destroy | Do Not Destroy | **M22 (Praise)** 8.3 [melody, musical]  ·  **M42 (Speech)** 3.5 [call]  ·  **M37 (Calling)** 3.5 [call] |
| 8.3 | H0120G a.dam | man | kindness | **M08 (Pride)** 8.3 [first, man]  ·  **M33 (Peace)** 4.2 [being] |
| 8.3 | G5204 hudōr | water | water | **M25 (Life)** 8.3 [refresh, liv]  ·  **M43 (Prophecy)** 4.2 [spiritual] |
| 8.3 | G5020 tartaroō | hell: Tartarus | hell: Tartarus | **M03 (Grief)** 8.3 [torture, tor]  ·  **M26 (Righteousness)** 4.2 [condemn]  ·  **M23 (Strength)** 4.2 [hold] |
| 8.3 | G4305 promerimnaō | to worry beforehand | to worry beforehand | **M20 (Doubt)** 8.3 [anxiou, worry] |
| 8.3 | G4177 politēs | citizen | citizen | **M23 (Strength)** 8.3 [kingdom, subject]  ·  **M26 (Righteousness)** 3.8 [act]  ·  **M10 (Sin)** 3.8 [act] |
| 8.3 | G4176 politeuō | be a citizen | be a citizen | **M23 (Strength)** 8.3 [govern, lead]  ·  **M25 (Life)** 4.2 [live]  ·  **M22 (Praise)** 4.2 [conduct] |
| 8.3 | G3625 oikoumenē | world | world | **M15 (Wisdom)** 8.3 [mean, word]  ·  **M12 (Purity)** 4.2 [form]  ·  **M26 (Righteousness)** 3.8 [act] |
| 8.3 | G3498 nekros | dead | deadness | **M24 (Weakness)** 8.3 [death, dead]  ·  **M23 (Strength)** 8.3 [power, subject]  ·  **M33 (Peace)** 7.2 [without, god] |
| 8.3 | G3009 leitourgia | ministry | worship | **M36 (Service)** 8.3 [service, ministry]  ·  **M12 (Purity)** 4.2 [sacr]  ·  **M05 (Love)** 4.2 [kind] |
| 8.3 | G2999 latreia | ministry | worship | **M36 (Service)** 8.3 [service, ministry] |
| 8.3 | G2288 thanatos | death | death | **M15 (Wisdom)** 8.3 [sense, natural]  ·  **M43 (Prophecy)** 4.2 [spiritual]  ·  **M38 (Salvation)** 4.2 [salvation] |
| 8.3 | G1840 exischuō | to have power | strength | **M23 (Strength)** 8.3 [strong, power] |
| 8.3 | G1537 ek | out from | seeking | **M15 (Wisdom)** 8.3 [mean, word]  ·  **M38 (Salvation)** 4.2 [free]  ·  **M24 (Weakness)** 4.2 [put] |
| 8.3 | G1457 enkainizō | to inaugurate | heart | **M12 (Purity)** 8.3 [consecrate, dedicate]  ·  **M24 (Weakness)** 4.2 [put]  ·  **M05 (Love)** 4.2 [open] |
| 8.3 | G1096 ginomai | to be | might | **M23 (Strength)** 8.3 [subject, grow]  ·  **M26 (Righteousness)** 7.2 [act, god]  ·  **M30 (Obedience)** 4.2 [become] |
| 8.3 | G1067 geenna | hell: Gehenna | hell: Gehenna | **M10 (Sin)** 8.3 [punish, corruption]  ·  **M33 (Peace)** 4.2 [well]  ·  **M24 (Weakness)** 4.2 [dead] |
| 8.3 | G0318 anankē | necessity | distress | **M01 (Fear)** 8.3 [hardship, constraint]  ·  **M24 (Weakness)** 7.9 [affliction, distres]  ·  **M43 (Prophecy)** 4.2 [spiritual] |
| 7.9 | H6485A pa.qad | to reckon: list | to reckon: list | **M26 (Righteousness)** 7.9 [charge, count]  ·  **M21 (Prayer)** 7.6 [after, seek]  ·  **M30 (Obedience)** 7.2 [look, care] |
| 7.9 | H6213A a.sah | to make: do | will | **M10 (Sin)** 7.9 [offer, act]  ·  **M24 (Weakness)** 4.2 [put]  ·  **M22 (Praise)** 4.2 [celebrate] |
| 7.9 | H4720 miq.dash | sanctuary | sanctuary | **M12 (Purity)** 7.9 [sacr, holy]  ·  **M27 (Evil)** 4.2 [temple]  ·  **M22 (Praise)** 3.8 [holy] |
| 7.9 | H4549 ma.sas | to melt | fear | **M01 (Fear)** 7.9 [fear, faint]  ·  **M23 (Strength)** 4.2 [grow]  ·  **M07 (Shame)** 4.2 [away] |
| 7.9 | H4399 me.la.khah | work | purpose | **M36 (Service)** 7.9 [service, work]  ·  **M23 (Strength)** 3.8 [work] |
| 7.9 | H3818 lo am.mi | Not My People | Not My People | **M14 (Deceit)** 7.9 [prophet, brother]  ·  **M37 (Calling)** 4.2 [name]  ·  **M25 (Life)** 4.2 [liv] |
| 7.9 | H3727 kap.po.ret | mercy seat | mercy | **M08 (Pride)** 7.9 [high, chosen]  ·  **M21 (Prayer)** 7.6 [covenant, god]  ·  **M38 (Salvation)** 4.2 [propitiation] |
| 7.9 | H3377 ya.rev | `great` | `great` | **M23 (Strength)** 7.9 [king, great]  ·  **M25 (Life)** 4.2 [liv]  ·  **M08 (Pride)** 4.2 [first] |
| 7.9 | H2402 chat.ta.ah | sin offering | sin | **M10 (Sin)** 7.9 [offer, sin]  ·  **M12 (Purity)** 3.8 [sin] |
| 7.9 | G4655 skotos | darkness | darkness | **M10 (Sin)** 7.9 [punish, act]  ·  **M43 (Prophecy)** 4.2 [spiritual]  ·  **M26 (Righteousness)** 3.8 [act] |
| 7.9 | G3788 ophthalmos | eye | envy | **M28 (Envy)** 7.9 [enviou, envy]  ·  **M15 (Wisdom)** 7.9 [mental, understand]  ·  **M10 (Sin)** 7.0 [act, evil] |
| 7.9 | G3422 mnēmosunon | memorial | memory | **M10 (Sin)** 7.9 [offer, act]  ·  **M41 (Remembrance)** 4.2 [remembrance]  ·  **M26 (Righteousness)** 3.8 [act] |
| 7.9 | G3054 logomacheō | to quarrel | to quarrel | **M15 (Wisdom)** 7.9 [word, dispute]  ·  **M02 (Anger)** 7.9 [quarrel, dispute]  ·  **M44 (Relational)** 4.2 [contend] |
| 7.9 | G2001 epischuō | to insist | to insist | **M23 (Strength)** 7.9 [strength, strengthen]  ·  **M15 (Wisdom)** 4.2 [insist]  ·  **M03 (Grief)** 4.2 [pres] |
| 7.9 | G1765 enischuō | to strengthen | strength | **M23 (Strength)** 7.9 [strength, strengthen]  ·  **M46 (Abundance)** 4.2 [gain]  ·  **M34 (Perseverance)** 3.8 [strengthen] |
| 7.9 | G1291 diastellō | to give orders | to give orders | **M26 (Righteousness)** 7.9 [charge, act]  ·  **M09 (Humility)** 4.2 [direct]  ·  **M10 (Sin)** 3.8 [act] |
| 7.9 | G0039G hagion | Holy Place | holiness | **M12 (Purity)** 7.9 [saint, holy]  ·  **M08 (Pride)** 4.2 [first]  ·  **M22 (Praise)** 3.8 [holy] |
| 7.6 | H6485K pa.qad | to reckon: missing | to reckon: missing | **M21 (Prayer)** 7.6 [after, seek]  ·  **M30 (Obedience)** 7.2 [look, care]  ·  **M19 (Trust)** 6.9 [care, seek] |
| 7.6 | H6485J pa.qad | to reckon: overseer | to reckon: overseer | **M21 (Prayer)** 7.6 [after, seek]  ·  **M30 (Obedience)** 7.2 [look, care]  ·  **M19 (Trust)** 6.9 [care, seek] |
| 7.6 | H6485I pa.qad | to reckon: visit | to reckon: visit | **M21 (Prayer)** 7.6 [after, seek]  ·  **M30 (Obedience)** 7.2 [look, care]  ·  **M19 (Trust)** 6.9 [care, seek] |
| 7.6 | H6485H pa.qad | to reckon: punish | to reckon: punish | **M21 (Prayer)** 7.6 [after, seek]  ·  **M30 (Obedience)** 7.2 [look, care]  ·  **M19 (Trust)** 6.9 [care, seek] |
| 7.6 | H6168 a.rah | to uncover | vulnerability | **M11 (Repentance)** 7.6 [leave, out]  ·  **M42 (Speech)** 3.5 [out]  ·  **M37 (Calling)** 3.5 [out] |
| 7.6 | H4905 mas.kil | Maskil | wisdom | **M42 (Speech)** 7.6 [song, call]  ·  **M22 (Praise)** 4.2 [musical]  ·  **M37 (Calling)** 3.5 [call] |
| 7.6 | H3772G ka.rat | to cut: cut | covenant | **M11 (Repentance)** 7.6 [permit, out]  ·  **M24 (Weakness)** 4.2 [fail]  ·  **M21 (Prayer)** 4.2 [covenant] |
| 7.6 | H1884 de.ta.var | judge | judge | **M15 (Wisdom)** 7.6 [interpreter, judge]  ·  **M41 (Remembrance)** 3.5 [judge]  ·  **M26 (Righteousness)** 3.5 [judge] |
| 7.6 | H0423 a.lah | oath | covenant | **M21 (Prayer)** 7.6 [covenant, god]  ·  **M07 (Shame)** 4.2 [curse]  ·  **M33 (Peace)** 3.5 [god] |
| 7.6 | G3687 onomazō | to name | to name | **M37 (Calling)** 7.6 [name, call]  ·  **M26 (Righteousness)** 3.8 [act]  ·  **M10 (Sin)** 3.8 [act] |
| 7.5 | H6944J qo.desh | Holy Place | Holy Place | **M22 (Praise)** 7.5 [holy, holi]  ·  **M12 (Purity)** 7.5 [holy, holi]  ·  **M37 (Calling)** 4.2 [name] |
| 7.5 | H3334 ya.tsar | be distressed | distress | **M24 (Weakness)** 7.5 [distres, suffer]  ·  **M03 (Grief)** 7.5 [distres, suffer]  ·  **M01 (Fear)** 4.2 [distress] |
| 7.5 | H1736 du.day | mandrake | mandrake | **M28 (Envy)** 7.5 [love, desire]  ·  **M29 (Desire)** 3.8 [desire]  ·  **M05 (Love)** 3.8 [love] |
| 7.5 | G5383 filoprōteuō | to love to be first | love | **M28 (Envy)** 7.5 [desire, love]  ·  **M08 (Pride)** 4.2 [first]  ·  **M29 (Desire)** 3.8 [desire] |
| 7.4 | H8264 sha.qaq | to rush | longing | **M18 (Hope)** 7.4 [long, eager]  ·  **M28 (Envy)** 3.8 [greedy]  ·  **M05 (Love)** 3.8 [greedy] |
| 7.4 | H7427 ro.me.mut | uplifting | uplifting | **M19 (Trust)** 7.4 [lift, self]  ·  **M28 (Envy)** 3.2 [self]  ·  **M15 (Wisdom)** 3.2 [self] |
| 7.2 | G5548 chriō | to anoint | anointing | **M26 (Righteousness)** 7.2 [act, god]  ·  **M23 (Strength)** 4.2 [power]  ·  **M09 (Humility)** 4.2 [dign] |
| 7.2 | G3614G oikia | home | home | **M05 (Love)** 7.2 [build, good]  ·  **M27 (Evil)** 4.2 [temple]  ·  **M15 (Wisdom)** 4.2 [mean] |
| 7.2 | G1348 dikastēs | magistrate | magistrate | **M26 (Righteousness)** 7.2 [act, judge]  ·  **M10 (Sin)** 3.8 [act]  ·  **M41 (Remembrance)** 3.5 [judge] |
