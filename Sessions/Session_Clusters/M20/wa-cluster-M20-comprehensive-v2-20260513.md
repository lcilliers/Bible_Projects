# M20 Doubt, Despair and Anxiety — comprehensive term + verse exposure

**Generated:** 2026-05-13T09:36:54Z  
**Cluster:** `M20` (bucket=NAMED, status=Data - In Progress, version=v6)  
**Source:** `database/bible_research.db`  

**Scope of this report:** every database fact that connects to a term in this cluster, exposed by term and by verse. Items currently linked only at registry / collection level (not yet resolvable to a specific term) are listed in the appendix as candidates for future linkage. Numbered paragraphs are used throughout to make every item directly referenceable.

---

<a id="toc"></a>
## Table of contents

- [§1. Cluster summary](#s1)
- [§2. Verses by sub-group](#s2)
  - [§2.1 _(unrouted / unassigned)_](#s2-1)
- [§3. Per-term comprehensive detail](#s3)
  - [H5074 na.dad — to wander (`mti_id=5571`)](#t-H5074)
  - [G3309 merimnaō — to worry (`mti_id=2709`)](#t-G3309)
  - [H1672 da.ag — be anxious (`mti_id=259`)](#t-H1672)
  - [G3308 merimna — concern (`mti_id=350`)](#t-G3308)
  - [H2976 ya.ash — to despair (`mti_id=394`)](#t-H2976)
  - [G1573 ekkakeō — to lose heart (`mti_id=603`)](#t-G1573)
  - [H3512A ka.ah — be disheartened (`mti_id=574`)](#t-H3512A)
  - [H3512B ka.eh — disheartened (`mti_id=1700`)](#t-H3512B)
  - [G1820 exaporeō — to despair (`mti_id=808`)](#t-G1820)
  - [G1365 distazō — to doubt (`mti_id=1288`)](#t-G1365)
  - [G1374 dipsuchos — double-minded (`mti_id=1398`)](#t-G1374)
  - [G0560 apelpizo — to despair (`mti_id=402`)](#t-G0560)
  - [G3642 oligopsuchos — fainthearted (`mti_id=1403`)](#t-G3642)
  - [G0120 athumeō — be discouraged (`mti_id=2078`)](#t-G0120)
- [§4. Appendix — items linked at registry or collection level](#s4)
  - [§4.1 Findings from contributor registries with no term-level link (39)](#s4-1)
  - [§4.2 SD pointers from contributor registries with no term-level link (39)](#s4-2)
  - [§4.3 Prose sections from contributor registries (0)](#s4-3)
  - [§4.4 Cluster-internal verse_context_group rows (18)](#s4-4)
  - [§4.5 Cross-cluster orphan findings/pointers](#s4-5)

---

<a id="s1"></a>
## §1. Cluster summary

1. Description: Doubt, Despair and Anxiety
2. Bucket / Status / Version: NAMED / Data - In Progress / v6
3. Last updated: 2026-05-13T09:32:17Z
4. Terms in cluster: **14** (Hebrew 5 · Greek 9)
5. Active OWNER verses (sum across terms): 83
6. Contributor registries: 10

**Verse status summary** (83 active verses)

| Status | Count | % | Meaning |
|---|---:|---:|---|
| G | 70 | 84.3% | group-assigned (analysed) |
| SA | 0 | 0.0% | set-aside (with reason) |
| NR | 0 | 0.0% | not-relevant (is_relevant=0) |
| P | 0 | 0.0% | pending (relevant but no group yet) |
| UT | 13 | 15.7% | untouched (no verse_context row) |
| **Total** | **83** | 100% | |

**By testament:** OT 45 · NT 38

7. Gloss list (14 entries — every distinct term currently in the cluster, disambiguated by transliteration):

be anxious (da.ag), be discouraged (athumeō), be disheartened (ka.ah), concern (merimna), disheartened (ka.eh), double-minded (dipsuchos), fainthearted (oligopsuchos), to despair (apelpizo), to despair (exaporeō), to despair (ya.ash), to doubt (distazō), to lose heart (ekkakeō), to wander (na.dad), to worry (merimnaō)

**Patch-authoring reference table:** integer values per term for the patch's `_patch_meta.terms_covered` (mti_id) and `_patch_meta.input_versions` (md_version). Sorted by Strong's.

| Strong's | Translit | mti_id | md_version | vc_status |
|---|---|---:|---:|---|
| G0120 | athumeō | 2078 | 1 | not_done |
| G0560 | apelpizo | 402 | 1 | not_done |
| G1365 | distazō | 1288 | 1 | not_done |
| G1374 | dipsuchos | 1398 | 1 | not_done |
| G1573 | ekkakeō | 603 | 1 | not_done |
| G1820 | exaporeō | 808 | 1 | not_done |
| G3308 | merimna | 350 | 1 | not_done |
| G3309 | merimnaō | 2709 | 1 | not_done |
| G3642 | oligopsuchos | 1403 | 1 | not_done |
| H1672 | da.ag | 259 | 1 | not_done |
| H2976 | ya.ash | 394 | 1 | not_done |
| H3512A | ka.ah | 574 | 1 | not_done |
| H3512B | ka.eh | 1700 | 1 | not_done |
| H5074 | na.dad | 5571 | 1 | not_done |

9. Connectivity health (broken or missing links along verse → vc → vcg / sub-group → term):

| Code | Check | Count |
|---|---|---:|
| `H1` ⚠ | Active vc rows in cluster with `cluster_subgroup_id` NULL — verse not routed to any sub-group | 71 |
| `H2` | Active vc rows with `is_relevant=1` but `group_id` NULL — relevant verse not yet in a meaning group | 0 |
| `H3` | vc.mti_term_id is not in its vcg's term set (`vcg_term`) — cross-term contamination, or vc points at a soft-deleted vcg | 0 |
| `H4` | vc.cluster_subgroup_id set but the term has no `mti_term_subgroup` link to that sub-group — orphaned verse routing | 0 |
| `H5` | Active `verse_context_group` rows with no active vc references — orphan meaning group | 0 |
| `H6` ⚠ | Cluster terms with no `mti_term_subgroup` mapping — term placed in cluster but unassigned to any sub-group | 14 |
| `H7` | Cluster terms with sub-group mapping but zero `verse_context_group` rows — sub-group placed but verses never contextually grouped | 0 |
| `H8` | vcgs whose active verses span multiple sub-groups — the same meaning is routed to different sub-groups; candidates for promotion, reassignment, or split | 0 |

_`H1` detail (showing 50 of 71):_

| vc_id | Reference | Strong's | mti_id |
|---|---|---|---|
| 8921 | Col 3:21 | G0120 | 2078 |
| 20591 | Luk 6:35 | G0560 | 402 |
| 54786 | Mat 14:31 | G1365 | 1288 |
| 54787 | Mat 28:17 | G1365 | 1288 |
| 32244 | Jam 1:8 | G1374 | 1398 |
| 32243 | Jam 4:8 | G1374 | 1398 |
| 47629 | 2Cor 4:1 | G1573 | 603 |
| 47630 | 2Cor 4:16 | G1573 | 603 |
| 47633 | 2Th 3:13 | G1573 | 603 |
| 47632 | Eph 3:13 | G1573 | 603 |
| 47631 | Gal 6:9 | G1573 | 603 |
| 47628 | Luk 18:1 | G1573 | 603 |
| 11061 | 2Cor 1:8 | G1820 | 808 |
| 11062 | 2Cor 4:8 | G1820 | 808 |
| 2676 | 1Pe 5:7 | G3308 | 350 |
| 2677 | 2Cor 11:28 | G3308 | 350 |
| 2672 | Luk 21:34 | G3308 | 350 |
| 2675 | Luk 8:14 | G3308 | 350 |
| 2674 | Mar 4:19 | G3308 | 350 |
| 2673 | Mat 13:22 | G3308 | 350 |
| 2693 | 1Cor 12:25 | G3309 | 2709 |
| 2690 | 1Cor 7:32 | G3309 | 2709 |
| 2691 | 1Cor 7:33 | G3309 | 2709 |
| 2692 | 1Cor 7:34 | G3309 | 2709 |
| 2687 | Luk 10:41 | G3309 | 2709 |
| 2689 | Luk 12:11 | G3309 | 2709 |
| 2684 | Luk 12:22 | G3309 | 2709 |
| 2685 | Luk 12:25 | G3309 | 2709 |
| 2686 | Luk 12:26 | G3309 | 2709 |
| 2688 | Mat 10:19 | G3309 | 2709 |
| 2679 | Mat 6:25 | G3309 | 2709 |
| 2680 | Mat 6:27 | G3309 | 2709 |
| 2681 | Mat 6:28 | G3309 | 2709 |
| 2682 | Mat 6:31 | G3309 | 2709 |
| 2683 | Mat 6:34 | G3309 | 2709 |
| 2694 | Phili 2:20 | G3309 | 2709 |
| 2678 | Phili 4:6 | G3309 | 2709 |
| 46884 | 1Th 5:14 | G3642 | 1403 |
| 14786 | 1Sa 10:2 | H1672 | 259 |
| 14783 | 1Sa 9:5 | H1672 | 259 |
| 14789 | Isa 57:11 | H1672 | 259 |
| 14784 | Jer 17:8 | H1672 | 259 |
| 14787 | Jer 38:19 | H1672 | 259 |
| 14788 | Jer 42:16 | H1672 | 259 |
| 14785 | Psa 38:18 | H1672 | 259 |
| 20839 | 1Sa 27:1 | H2976 | 394 |
| 20838 | Ecc 2:20 | H2976 | 394 |
| 20841 | Isa 57:10 | H2976 | 394 |
| 20843 | Jer 18:12 | H2976 | 394 |
| 20842 | Jer 2:25 | H2976 | 394 |

_`H6` detail (showing 14 of 14):_

| mti_id | Strong's | Translit | Gloss |
|---|---|---|---|
| 2078 | G0120 | athumeō | be discouraged |
| 402 | G0560 | apelpizo | to despair |
| 1288 | G1365 | distazō | to doubt |
| 1398 | G1374 | dipsuchos | double-minded |
| 603 | G1573 | ekkakeō | to lose heart |
| 808 | G1820 | exaporeō | to despair |
| 350 | G3308 | merimna | concern |
| 2709 | G3309 | merimnaō | to worry |
| 1403 | G3642 | oligopsuchos | fainthearted |
| 259 | H1672 | da.ag | be anxious |
| 394 | H2976 | ya.ash | to despair |
| 574 | H3512A | ka.ah | be disheartened |
| 1700 | H3512B | ka.eh | disheartened |
| 5571 | H5074 | na.dad | to wander |

<a id="s2"></a>
## §2. Verses by sub-group

All verses for cluster terms, grouped by the analytical sub-group the term belongs to. Within each sub-group the rows are sorted canonically (book · chapter · verse). The **Term** column shows the Strong's number and transliteration of the cluster term whose `wa_verse_records` row generated this entry; **Spans in verse** lists every term-span recorded at that verse location.

Status precedence: G = group-assigned (analysed) · SA = set-aside · NR = is_relevant=0 · P = pending in VC · UT = untouched (no VC row).

**ID columns:** `vr_id` is `wa_verse_records.id`; `mti_id` is `mti_terms.id` (also `wa_verse_records.mti_term_id` and `verse_context.mti_term_id`). Both are exposed so AI can author VCREVISE / VCNEW / VCVERSE patches directly from this report — no separate ID-resolver query needed. The `(vr_id, mti_id)` pair is the natural key for any `verse_context` operation.

<a id="s2-1"></a>
### §2.1 _(unrouted / unassigned)_

_Verses whose `verse_context.cluster_subgroup_id` is NULL, or whose term has no `mti_term_subgroup` mapping._

1. Terms (14): H1672 da.ag, G3308 merimna, H2976 ya.ash, G0560 apelpizo, H3512A ka.ah, G1573 ekkakeō, G1820 exaporeō, G1365 distazō, G1374 dipsuchos, G3642 oligopsuchos, H3512B ka.eh, G0120 athumeō, G3309 merimnaō, H5074 na.dad
2. Verse rows (83):

| vr_id | mti_id | Reference | Term | Status | Group | Set-aside reason | Spans in verse | Verse text |
|---:|---:|---|---|---|---|---|---|---|
| 169919 | 5571 | Gen 31:40 | H5074 na.dad | G | 5571-001 |  | H5074 na.dad (to wander) [fled] | Gen 31:40 There I was : by day the heat consumed me, and the cold by night , and my sleep fled from my eyes . |
| 2205 | 259 | 1Sa 9:5 | H1672 da.ag | G | 259-001 |  | H1672 da.ag (be anxious) [become anxious]; H0860 a.ton (she-ass) [donkeys] | 1Sa 9:5 When they came to the land of Zuph , Saul said to his servant who was with him, “ Come , let us go back , lest my father cease to care about the donkeys and become anxious about us .” |
| 2206 | 259 | 1Sa 10:2 | H1672 da.ag | G | 259-001 |  | H1672 da.ag (be anxious) [anxious]; H1245 ba.qash (to seek) [seek]; H5978 im.ma.di (with me) [meet]; H4672 ma.tsa (to find) [meet]; H0860 a.ton (she-ass) [donkeys] | 1Sa 10:2 When you depart from me today , you will meet two men by Rachel’s tomb in the territory of Benjamin at Zelzah , and they will say to you, ‘The donkeys that you went to seek are found , and now your father has ceased to care about the donkeys and is anxious about you, saying , “ What shall I do about my son ?”’ |
| 3540 | 394 | 1Sa 27:1 | H2976 ya.ash | G | 394-001 |  | H2976 ya.ash (to despair) [despair]; H1245 ba.qash (to seek) [seeking]; H3820A lev (heart) [heart]; H2896A tov (pleasant) [better] | 1Sa 27:1 Then David said in his heart , “ Now I shall perish one day by the hand of Saul . There is nothing better for me than that I should escape to the land of the Philistines . Then Saul will despair of seeking me any longer within the borders of Israel , and I shall escape out of his hand .” |
| 169917 | 5571 | 2Sa 23:6 | H5074 na.dad | UT |  |  | H5074 na.dad (to wander) [thrown away] | 2Sa 23:6 But worthless men are all like thorns that are thrown away , for they cannot be taken with the hand ; |
| 169918 | 5571 | Est 6:1 | H5074 na.dad | G | 5571-001 |  | H2146 zik.ka.ron (memorial) [memorable]; H7121J qa.ra (to call: read out) [read]; H5074 na.dad (to wander) [could not] | Est 6:1 On that night the king could not sleep . And he gave orders to bring the book of memorable deeds , the chronicles , and they were read before the king . |
| 3541 | 394 | Job 6:26 | H2976 ya.ash | G | 394-001 |  | H2976 ya.ash (to despair) [despairing]; H2803J cha.shav (to devise: think) [think] | Job 6:26 Do you think that you can reprove words , when the speech of a despairing man is wind ? |
| 169933 | 5571 | Job 15:23 | H5074 na.dad | G | 5571-001 |  | H1931 hu (he/she/it) [bread]; H3045 ya.da (to know) [knows]; H3027G yad (hand) [hand]; H5074 na.dad (to wander) [wanders] | Job 15:23 He wanders abroad for bread , saying, ‘ Where is it?’ He knows that a day of darkness is ready at his hand ; |
| 169934 | 5571 | Job 18:18 | H5074 na.dad | G | 5571-001 |  | H0413 el (to[wards]) [darkness]; H5074 na.dad (to wander) [driven] | Job 18:18 He is thrust from light into darkness , and driven out of the world . |
| 169935 | 5571 | Job 20:8 | H5074 na.dad | G | 5571-001 |  | H4672 ma.tsa (to find) [found]; H5074 na.dad (to wander) [chased away] | Job 20:8 He will fly away like a dream and not be found ; he will be chased away like a vision of the night . |
| 169939 | 5571 | Psa 31:11 | H5074 na.dad | G | 5571-001 |  | H2781 cher.pah (reproach) [reproach]; H3966 me.od (much) [especially]; H6887D tsa.rar (to vex) [adversaries]; H6343 pa.chad (dread) [dread]; H5074 na.dad (to wander) [flee] | Psa 31:11 Because of all my adversaries I have become a reproach , especially to my neighbors , and an object of dread to my acquaintances ; those who see me in the street flee from me . |
| 60694 | 259 | Psa 38:18 | H1672 da.ag | G | 259-002 |  | H1672 da.ag (be anxious) [sorry]; H5771G a.von (iniquity: crime) [iniquity]; H2403B chat.tat (sin) [sin] | Psa 38:18 I confess my iniquity ; I am sorry for my sin . |
| 169940 | 5571 | Psa 55:7 | H5074 na.dad | G | 5571-001 |  | H5074 na.dad (to wander) [wander]; H2009 hin.neh (behold) [yes] | Psa 55:7 yes , I would wander far away ; I would lodge in the wilderness ; Selah |
| 169941 | 5571 | Psa 64:8 | H5074 na.dad | UT |  |  | H5074 na.dad (to wander) [heads] | Psa 64:8 They are brought to ruin , with their own tongues turned against them; all who see them will wag their heads . |
| 169942 | 5571 | Psa 68:12 | H5074 na.dad | UT |  |  | H6635B tsa.va (Hosts) [armies]; H2505A cha.laq (to divide) [divide]; H5074 na.dad (to wander) [flee] | Psa 68:12 “The kings of the armies —they flee , they flee !” The women at home divide the spoil — |
| 7827 | 574 | Psa 109:16 | H3512A ka.ah | G | 574-001 |  | H3512A ka.ah (be disheartened) [brokenhearted]; H3824 le.vav (heart) [brokenhearted]; H4191 mut (to die) [death]; H3512B ka.eh (disheartened) [brokenhearted]; H2142 za.khar (to remember) [remember] | Psa 109:16 For he did not remember to show kindness , but pursued the poor and needy and the brokenhearted , to put them to death . |
| 65509 | 1700 | Psa 109:16 | H3512B ka.eh | G | 1700-001 |  | H3512A ka.ah (be disheartened) [brokenhearted]; H3824 le.vav (heart) [brokenhearted]; H4191 mut (to die) [death]; H3512B ka.eh (disheartened) [brokenhearted]; H2142 za.khar (to remember) [remember] | Psa 109:16 For he did not remember to show kindness , but pursued the poor and needy and the brokenhearted , to put them to death . |
| 169938 | 5571 | Pro 27:8 | H5074 na.dad | G | 5571-001 |  | H5074 na.dad (to wander) [strays]; H4725 ma.qom (place) [home] | Pro 27:8 Like a bird that strays from its nest is a man who strays from his home . |
| 3542 | 394 | Ecc 2:20 | H2976 ya.ash | G | 394-001 |  | H5999 a.mal (trouble) [toil]; H2976 ya.ash (to despair) [despair]; H0589 a.ni (I) [despair] | Ecc 2:20 So I turned about and gave my heart up to despair over all the toil of my labors under the sun , |
| 169922 | 5571 | Isa 10:14 | H5074 na.dad | UT |  |  | H6310G peh (lip) [mouth]; H3808 lo (not) [none]; H0589 a.ni (I) [I]; H3605 kol (all) [all]; H4672 ma.tsa (to find) [found]; H3027G yad (hand) [hand]; H5074 na.dad (to wander) [moved]; H5971H am (People's [Gate]) [peoples]; H5971I am ([Ibleam]-am) [peoples]; H5971L am (people: creatures) [peoples]; H2428H cha.yil (strength: rich) [wealth] | Isa 10:14 My hand has found like a nest the wealth of the peoples ; and as one gathers eggs that have been forsaken , so I have gathered all the earth ; and there was none that moved a wing or opened the mouth or chirped .” |
| 169923 | 5571 | Isa 10:31 | H5074 na.dad | UT |  |  | H3427 ya.shav (to dwell) [inhabitants]; H5074 na.dad (to wander) [flight] | Isa 10:31 Madmenah is in flight ; the inhabitants of Gebim flee for safety . |
| 169924 | 5571 | Isa 16:2 | H5074 na.dad | UT |  |  | H5074 na.dad (to wander) [fleeing] | Isa 16:2 Like fleeing birds , like a scattered nest , so are the daughters of Moab at the fords of the Arnon . |
| 169925 | 5571 | Isa 16:3 | H5074 na.dad | G | 5571-001 |  | H6098 e.tsah (counsel) [counsel]; H0408 al (not) [not]; H5074 na.dad (to wander) [fugitive] | Isa 16:3 “ Give counsel ; grant justice ; make your shade like night at the height of noon ; shelter the outcasts ; do not reveal the fugitive ; |
| 169926 | 5571 | Isa 21:14 | H5074 na.dad | G | 5571-001 |  | H3427 ya.shav (to dwell) [inhabitants]; H7122G qa.ra (to encounter: meet) [meet]; H5074 na.dad (to wander) [fugitive] | Isa 21:14 To the thirsty bring water ; meet the fugitive with bread , O inhabitants of the land of Tema . |
| 169927 | 5571 | Isa 21:15 | H5074 na.dad | UT |  |  | H3514 ko.ved (heaviness) [press]; H5074 na.dad (to wander) [fled] | Isa 21:15 For they have fled from the swords , from the drawn sword , from the bent bow , and from the press of battle . |
| 169928 | 5571 | Isa 22:3 | H5074 na.dad | UT |  |  | H4672 ma.tsa (to find) [found]; H3162A ya.chad (unitedness) [together]; H5074 na.dad (to wander) [fled]; H3162B ya.che.dav (together) [together] | Isa 22:3 All your leaders have fled together ; without the bow they were captured . All of you who were found were captured , though they had fled far away . |
| 169929 | 5571 | Isa 33:3 | H5074 na.dad | UT |  |  | H5074 na.dad (to wander) [flee]; H7427 ro.me.mut (uplifting) [yourself up] | Isa 33:3 At the tumultuous noise peoples flee ; when you lift yourself up , nations are scattered , |
| 3543 | 394 | Isa 57:10 | H2976 ya.ash | G | 394-001 |  | H2976 ya.ash (to despair) [hopeless]; H4672 ma.tsa (to find) [found]; H7230 rov (abundance) [length]; H3027H yad (hand: power) [strength]; H2416C chay.yah (living thing) [life] | Isa 57:10 You were wearied with the length of your way , but you did not say , “It is hopeless ”; you found new life for your strength , and so you were not faint . |
| 60693 | 259 | Isa 57:11 | H1672 da.ag | G | 259-001 |  | H0589 a.ni (I) [my]; H4310 mi (who?) [Whom]; H2142 za.khar (to remember) [remember]; H2814 cha.shah (be silent) [peace]; H1672 da.ag (be anxious) [dread]; H3820A lev (heart) [heart]; H3372H ya.re (to fear: revere) [fear] | Isa 57:11 Whom did you dread and fear , so that you lied , and did not remember me, did not lay it to heart ? Have I not held my peace , even for a long time , and you do not fear me? |
| 3544 | 394 | Jer 2:25 | H2976 ya.ash | G | 394-001 |  | H2976 ya.ash (to despair) [hopeless]; H1980G ha.lakh (to go: went) [go]; H7272 re.gel (foot) [feet] | Jer 2:25 Keep your feet from going unshod and your throat from thirst . But you said , ‘It is hopeless , for I have loved foreigners , and after them I will go .’ |
| 169930 | 5571 | Jer 4:25 | H5074 na.dad | UT |  |  | H0120G a.dam (man) [man]; H5074 na.dad (to wander) [fled] | Jer 4:25 I looked , and behold , there was no man , and all the birds of the air had fled . |
| 169932 | 5571 | Jer 9:10 | H5074 na.dad | UT |  |  | H1097 be.li (without) [no]; H1980G ha.lakh (to go: went) [gone]; H1065 be.khi (weeping) [weeping]; H5074 na.dad (to wander) [fled] | Jer 9:10 “I will take up weeping and wailing for the mountains , and a lamentation for the pastures of the wilderness , because they are laid waste so that no one passes through , and the lowing of cattle is not heard ; both the birds of the air and the beasts have fled and are gone . |
| 2207 | 259 | Jer 17:8 | H1672 da.ag | G | 259-001 |  | H1672 da.ag (be anxious) [anxious] | Jer 17:8 He is like a tree planted by water , that sends out its roots by the stream , and does not fear when heat comes , for its leaves remain green , and is not anxious in the year of drought , for it does not cease to bear fruit .” |
| 3545 | 394 | Jer 18:12 | H2976 ya.ash | G | 394-001 |  | H2976 ya.ash (to despair) [vain]; H4284 ma.cha.sha.vah (plot) [plans]; H8307 she.ri.rut (stubbornness) [stubbornness]; H3820A lev (heart) [heart] | Jer 18:12 “But they say , ‘That is in vain ! We will follow our own plans , and will every one act according to the stubbornness of his evil heart .’ |
| 2208 | 259 | Jer 38:19 | H1672 da.ag | G | 259-001 |  | H1672 da.ag (be anxious) [afraid]; H6435 pen- (lest) [lest]; H3027K yad (hand: to) [to them] | Jer 38:19 King Zedekiah said to Jeremiah , “ I am afraid of the Judeans who have deserted to the Chaldeans , lest I be handed over to them and they deal cruelly with me .” |
| 2209 | 259 | Jer 42:16 | H1672 da.ag | G | 259-001 |  | H1672 da.ag (be anxious) [afraid]; H4191 mut (to die) [die]; H3373 ya.re (afraid) [fear]; H0859D at.tem (you [m.p.]) [you] | Jer 42:16 then the sword that you fear shall overtake you there in the land of Egypt , and the famine of which you are afraid shall follow close after you to Egypt , and there you shall die . |
| 169931 | 5571 | Jer 49:5 | H5074 na.dad | UT |  |  | H6343 pa.chad (dread) [terror]; H0136 a.do.na (Lord [God]) [Lord]; H5074 na.dad (to wander) [fugitives] | Jer 49:5 Behold , I will bring terror upon you, declares the Lord God of hosts , from all who are around you, and you shall be driven out , every man straight before him, with none to gather the fugitives . |
| 7828 | 574 | Eze 13:22 | H3512A ka.ah | G | 574-001 |  | H3510 ka.av (to pain) [grieved]; H3512A ka.ah (be disheartened) [disheartened]; H7725O shuv (to return: repent) [turn]; H3512B ka.eh (disheartened) [disheartened]; H2421 cha.yah (to live) [life]; H2388G cha.zaq (to strengthen: strengthen) [encouraged]; H3027I yad (hand: themselves) [the]; H8267 she.qer (deception) [falsely]; H6662 tsad.diq (righteous) [righteous]; H7563 ra.sha (wicked) [evil] | Eze 13:22 Because you have disheartened the righteous falsely , although I have not grieved him, and you have encouraged the wicked , that he should not turn from his evil way to save his life , |
| 65508 | 1700 | Eze 13:22 | H3512B ka.eh | G | 1700-001 |  | H3510 ka.av (to pain) [grieved]; H3512A ka.ah (be disheartened) [disheartened]; H7725O shuv (to return: repent) [turn]; H3512B ka.eh (disheartened) [disheartened]; H2421 cha.yah (to live) [life]; H2388G cha.zaq (to strengthen: strengthen) [encouraged]; H3027I yad (hand: themselves) [the]; H8267 she.qer (deception) [falsely]; H6662 tsad.diq (righteous) [righteous]; H7563 ra.sha (wicked) [evil] | Eze 13:22 Because you have disheartened the righteous falsely , although I have not grieved him, and you have encouraged the wicked , that he should not turn from his evil way to save his life , |
| 7829 | 574 | Dan 11:30 | H3512A ka.ah | G | 574-001 |  | H2194 za.am (be indignant) [enraged]; H3512A ka.ah (be disheartened) [afraid]; H1285 be.rit (covenant) [covenant]; H0995 bin (to understand) [attention]; H3512B ka.eh (disheartened) [afraid] | Dan 11:30 For ships of Kittim shall come against him, and he shall be afraid and withdraw, and shall turn back and be enraged and take action against the holy covenant . He shall turn back and pay attention to those who forsake the holy covenant . |
| 65507 | 1700 | Dan 11:30 | H3512B ka.eh | G | 1700-001 |  | H2194 za.am (be indignant) [enraged]; H3512A ka.ah (be disheartened) [afraid]; H1285 be.rit (covenant) [covenant]; H0995 bin (to understand) [attention]; H3512B ka.eh (disheartened) [afraid] | Dan 11:30 For ships of Kittim shall come against him, and he shall be afraid and withdraw, and shall turn back and be enraged and take action against the holy covenant . He shall turn back and pay attention to those who forsake the holy covenant . |
| 169920 | 5571 | Hos 7:13 | H5074 na.dad | G | 5571-001 |  | H1992 hem.mah (they [masc.]) [they]; H4480A min- (from) [Destruction]; H6586 pa.sha (to transgress) [rebelled]; H6299 pa.dah (to ransom) [redeem]; H5074 na.dad (to wander) [strayed] | Hos 7:13 Woe to them, for they have strayed from me! Destruction to them, for they have rebelled against me! I would redeem them, but they speak lies against me. |
| 169921 | 5571 | Hos 9:17 | H5074 na.dad | G | 5571-001 |  | H3808 lo (not) [not]; H8085G sha.ma (to hear: hear) [listened]; H5074 na.dad (to wander) [be wanderers] | Hos 9:17 My God will reject them because they have not listened to him; they shall be wanderers among the nations . |
| 169937 | 5571 | Nah 3:7 | H5074 na.dad | G | 5571-001 |  | H4310 mi (who?) [who]; H7200G ra.ah (to see: see) [look]; H4480A min- (from) [from]; H1245 ba.qash (to seek) [seek]; H5162G na.cham (to be sorry: comfort) [comforters]; H5074 na.dad (to wander) [shrink]; H0370 a.yin (where?) [Where] | Nah 3:7 And all who look at you will shrink from you and say , “ Wasted is Nineveh ; who will grieve for her?” Where shall I seek comforters for you ? |
| 169936 | 5571 | Nah 3:17 | H5074 na.dad | UT |  |  | H3045 ya.da (to know) [knows]; H4502 min.zar (prince) [princes]; H5074 na.dad (to wander) [fly away]; H4725 ma.qom (place) [are] | Nah 3:17 Your princes are like grasshoppers , your scribes like clouds of locusts settling on the fences in a day of cold — when the sun rises , they fly away ; no one knows where they are . |
| 81689 | 2709 | Mat 6:25 | G3309 merimnaō | G | 2709-001 |  | G5590H psuchē (soul: life) [life]; G3309 merimnaō (to worry) [anxious] | Mat 6:25 “ Therefore I tell you , do not be anxious about your life , what you will eat or what you will drink , nor about your body , what you will put on . Is not life more than food , and the body more than clothing ? |
| 81690 | 2709 | Mat 6:27 | G3309 merimnaō | G | 2709-001 |  | G3309 merimnaō (to worry) [anxious]; G1410 dunamai (be able) [can] | Mat 6:27 And which of you by being anxious can add a single hour to his span of life ? |
| 81691 | 2709 | Mat 6:28 | G3309 merimnaō | G | 2709-001 |  | G3309 merimnaō (to worry) [anxious] | Mat 6:28 And why are you anxious about clothing ? Consider the lilies of the field , how they grow : they neither toil nor spin , |
| 81692 | 2709 | Mat 6:31 | G3309 merimnaō | G | 2709-001 |  | G3309 merimnaō (to worry) [anxious] | Mat 6:31 Therefore do not be anxious , saying , ‘ What shall we eat ?’ or ‘ What shall we drink ?’ or ‘ What shall we wear ?’ |
| 81693 | 2709 | Mat 6:34 | G3309 merimnaō | G | 2709-001 |  | G3309 merimnaō (to worry) [anxious]; G2549 kakia (evil) [trouble] | Mat 6:34 “ Therefore do not be anxious about tomorrow , for tomorrow will be anxious for itself . Sufficient for the day is its own trouble . |
| 81688 | 2709 | Mat 10:19 | G3309 merimnaō | G | 2709-002 |  | G3309 merimnaō (to worry) [anxious]; G3860 paradidōmi (to deliver) [deliver] | Mat 10:19 When they deliver you over, do not be anxious how you are to speak or what you are to say , for what you are to say will be given to you in that hour . |
| 1161 | 350 | Mat 13:22 | G3308 merimna | G | 350-001 |  | G3308 merimna (concern) [cares] | Mat 13:22 As for what was sown among thorns , this is the one who hears the word , but the cares of the world and the deceitfulness of riches choke the word , and it proves unfruitful . |
| 54659 | 1288 | Mat 14:31 | G1365 distazō | G | 1288-001 |  | G3640 oligopistos (of little faith) [little faith]; G1365 distazō (to doubt) [doubt] | Mat 14:31 Jesus immediately reached out his hand and took hold of him , saying to him , “O you of little faith , why did you doubt ?” |
| 54660 | 1288 | Mat 28:17 | G1365 distazō | G | 1288-001 |  | G1365 distazō (to doubt) [doubted]; G4352 proskuneō (to worship) [worshiped] | Mat 28:17 And when they saw him they worshiped him, but some doubted . |
| 1162 | 350 | Mar 4:19 | G3308 merimna | G | 350-001 |  | G3308 merimna (concern) [cares]; G1939 epithumia (desire) [desires] | Mar 4:19 but the cares of the world and the deceitfulness of riches and the desires for other things enter in and choke the word , and it proves unfruitful . |
| 3699 | 402 | Luk 6:35 | G0560 apelpizo | G | 402-001 |  | G0560 apelpizo (to despair) [return]; G0025 agapaō (to love) [love]; G4190 ponēros (evil/bad) [evil]; G0015 agathopoieō (to do good) [good]; G5543 chrēstos (good/kind) [kind] | Luk 6:35 But love your enemies , and do good , and lend , expecting nothing in return , and your reward will be great , and you will be sons of the Most High , for he is kind to the ungrateful and the evil . |
| 1163 | 350 | Luk 8:14 | G3308 merimna | G | 350-001 |  | G3308 merimna (concern) [cares]; G2237 hēdonē (pleasure) [pleasures] | Luk 8:14 And as for what fell among the thorns , they are those who hear , but as they go on their way they are choked by the cares and riches and pleasures of life , and their fruit does not mature . |
| 81683 | 2709 | Luk 10:41 | G3309 merimnaō | G | 2709-002 |  | G3309 merimnaō (to worry) [anxious] | Luk 10:41 But the Lord answered her , “ Martha , Martha , you are anxious and troubled about many things , |
| 81684 | 2709 | Luk 12:11 | G3309 merimnaō | G | 2709-002 |  | G1849 exousia (authority) [authorities]; G3309 merimnaō (to worry) [anxious]; G0746 archē (beginning) [rulers] | Luk 12:11 And when they bring you before the synagogues and the rulers and the authorities , do not be anxious about how you should defend yourself or what you should say , |
| 81685 | 2709 | Luk 12:22 | G3309 merimnaō | G | 2709-001 |  | G5590H psuchē (soul: life) [life]; G3309 merimnaō (to worry) [anxious] | Luk 12:22 And he said to his disciples , “ Therefore I tell you , do not be anxious about your life , what you will eat , nor about your body , what you will put on . |
| 81686 | 2709 | Luk 12:25 | G3309 merimnaō | G | 2709-001 |  | G3309 merimnaō (to worry) [anxious] | Luk 12:25 And which of you by being anxious can add a single hour to his span of life ? |
| 81687 | 2709 | Luk 12:26 | G3309 merimnaō | G | 2709-001 |  | G3309 merimnaō (to worry) [anxious] | Luk 12:26 If then you are not able to do as small a thing as that, why are you anxious about the rest ? |
| 9073 | 603 | Luk 18:1 | G1573 ekkakeō | G | 603-001 |  | G1573 ekkakeō (to lose heart) [lose heart]; G4336 proseuchomai (to pray) [pray]; G3842 pantote (always) [always] | Luk 18:1 And he told them a parable to the effect that they ought always to pray and not lose heart . |
| 1164 | 350 | Luk 21:34 | G3308 merimna | G | 350-001 |  | G3308 merimna (concern) [cares]; G2588 kardia (heart) [hearts] | Luk 21:34 “ But watch yourselves lest your hearts be weighed down with dissipation and drunkenness and cares of this life , and that day come upon you suddenly like a trap . |
| 81680 | 2709 | 1Cor 7:32 | G3309 merimnaō | G | 2709-003 |  | G0275 amerimnos (untroubled) [free from anxieties]; G2309 thelō (to will/desire) [want]; G3309 merimnaō (to worry) [anxious about] | 1Cor 7:32 I want you to be free from anxieties . The unmarried man is anxious about the things of the Lord , how to please the Lord . |
| 81681 | 2709 | 1Cor 7:33 | G3309 merimnaō | G | 2709-003 |  | G3309 merimnaō (to worry) [anxious about] | 1Cor 7:33 But the married man is anxious about worldly things, how to please his wife , |
| 81682 | 2709 | 1Cor 7:34 | G3309 merimnaō | G | 2709-003 |  | G0040G hagios (holy) [holy]; G4151G pneuma (spirit/breath: breath) [spirit]; G3309 merimnaō (to worry) [anxious about]; G3307 merizō (to divide) [divided] | 1Cor 7:34 and his interests are divided . And the unmarried or betrothed woman is anxious about the things of the Lord , how to be holy in body and spirit . But the married woman is anxious about worldly things , how to please her husband . |
| 81679 | 2709 | 1Cor 12:25 | G3309 merimnaō | G | 2709-003 |  | G4978 schisma (split) [division]; G3309 merimnaō (to worry) [care] | 1Cor 12:25 that there may be no division in the body , but that the members may have the same care for one another . |
| 19472 | 808 | 2Cor 1:8 | G1820 exaporeō | G | 808-001 |  | G1820 exaporeō (to despair) [despaired]; G2347 thlipsis (pressure) [affliction]; G2309 thelō (to will/desire) [want]; G1411 dunamis (power) [strength]; G0050 agnoeō (be ignorant) [unaware] | 2Cor 1:8 For we do not want you to be unaware , brothers , of the affliction we experienced in Asia . For we were so utterly burdened beyond our strength that we despaired of life itself . |
| 9074 | 603 | 2Cor 4:1 | G1573 ekkakeō | G | 603-001 |  | G1573 ekkakeō (to lose heart) [lose heart]; G1653 eleeō (to have mercy) [mercy] | 2Cor 4:1 Therefore , having this ministry by the mercy of God, we do not lose heart . |
| 19473 | 808 | 2Cor 4:8 | G1820 exaporeō | G | 808-001 |  | G2346 thlibō (to press on) [afflicted]; G4729 stenochōreō (to press upon) [crushed]; G1820 exaporeō (to despair) [despair]; G0639 aporeō (be perplexed) [perplexed] | 2Cor 4:8 We are afflicted in every way , but not crushed ; perplexed , but not driven to despair ; |
| 9075 | 603 | 2Cor 4:16 | G1573 ekkakeō | G | 603-001 |  | G1573 ekkakeō (to lose heart) [lose heart]; G1311 diaftheirō (to destroy) [wasting away]; G0341 anakainoō (to renew) [renewed] | 2Cor 4:16 So we do not lose heart . Though our outer self is wasting away , our inner self is being renewed day by day . |
| 1165 | 350 | 2Cor 11:28 | G3308 merimna | G | 350-002 |  | G3308 merimna (concern) [anxiety]; G1577 ekklēsia (assembly) [churches] | 2Cor 11:28 And, apart from other things , there is the daily pressure on me of my anxiety for all the churches . |
| 9076 | 603 | Gal 6:9 | G1573 ekkakeō | G | 603-001 |  | G1573 ekkakeō (to lose heart) [grow weary] | Gal 6:9 And let us not grow weary of doing good , for in due season we will reap , if we do not give up . |
| 9077 | 603 | Eph 3:13 | G1573 ekkakeō | G | 603-001 |  | G2347 thlipsis (pressure) [suffering]; G1573 ekkakeō (to lose heart) [lose heart]; G1391 doxa (glory) [glory] | Eph 3:13 So I ask you not to lose heart over what I am suffering for you , which is your glory . |
| 81694 | 2709 | Phili 2:20 | G3309 merimnaō | G | 2709-003 |  | G3309 merimnaō (to worry) [concerned]; G2473 isopsuchos (like-minded) [him] | Phili 2:20 For I have no one like him , who will be genuinely concerned for your welfare. |
| 81695 | 2709 | Phili 4:6 | G3309 merimnaō | G | 2709-001 |  | G3309 merimnaō (to worry) [anxious]; G2169 eucharistia (thankfulness) [thanksgiving]; G4335 proseuchē (prayer) [prayer]; G1162 deēsis (petition) [supplication] | Phili 4:6 do not be anxious about anything , but in everything by prayer and supplication with thanksgiving let your requests be made known to God . |
| 151231 | 2078 | Col 3:21 | G0120 athumeō | G | 2078-001 |  | G2042 erethizō (to provoke/irritate) [provoke]; G0120 athumeō (be discouraged) [become discouraged] | Col 3:21 Fathers , do not provoke your children , lest they become discouraged . |
| 62310 | 1403 | 1Th 5:14 | G3642 oligopsuchos | G | 1403-001 |  | G3114 makrothumeō (to have patience) [patient]; G3870 parakaleō (to plead/comfort) [urge]; G3642 oligopsuchos (fainthearted) [fainthearted]; G0772G asthenēs (weak) [weak] | 1Th 5:14 And we urge you , brothers , admonish the idle , encourage the fainthearted , help the weak , be patient with them all . |
| 9078 | 603 | 2Th 3:13 | G1573 ekkakeō | G | 603-001 |  | G1573 ekkakeō (to lose heart) [grow weary] | 2Th 3:13 As for you , brothers , do not grow weary in doing good . |
| 126404 | 1398 | Jam 1:8 | G1374 dipsuchos | G | 1398-001 |  | G1374 dipsuchos (double-minded) [double-minded] | Jam 1:8 he is a double-minded man , unstable in all his ways . |
| 126405 | 1398 | Jam 4:8 | G1374 dipsuchos | G | 1398-001 |  | G0268 hamartōlos (sinful) [sinners]; G1374 dipsuchos (double-minded) [double-minded]; G2511 katharizō (to clean) [Cleanse]; G0048 hagnizō (to purify) [purify] | Jam 4:8 Draw near to God , and he will draw near to you . Cleanse your hands , you sinners , and purify your hearts , you double-minded . |
| 1166 | 350 | 1Pe 5:7 | G3308 merimna | G | 350-002 |  | G3308 merimna (concern) [anxieties] | 1Pe 5:7 casting all your anxieties on him , because he cares for you . |

<a id="s3"></a>
## §3. Per-term comprehensive detail

Each term gets numbered sections: identity • meaning • anchor-verse linkages • groups • findings • pointers • auxiliary data. Verses are not repeated here — they are listed by sub-group in §2. Items linked only by registry are summarised here; exhaustive lists are in the appendix §4.

---

<a id="t-H5074"></a>
### H5074 na.dad — to wander (`mti_id=5571`)

**Identity & meaning**

1. Strong's: `H5074` · Lang: Hebrew · Owner: OWNER
2. Registry: R086 impurity · Legacy C-cluster: C12
3. Sub-group: —
4. Term status: extracted · Evidential: — · Occurrences: 28
5. Patch-authoring refs: `mti_id=5571` · `md_version=1` · `vc_status=not_done`

**Verses:** 26 distinct locations (see §2 for the verse table grouped by sub-group).

**Group memberships (1)**

| Group ID | Code | Description | Notes |
|---|---|---|---|
| 1306 | 5571-001 | Term names wandering or fleeing as an inner experience — restlessness of sleep fleeing, the anguish of spiritual straying, or the inner alienation expressed through wandering |  |

**Findings — direct (Strong's mention) (0)**

(none)

**Findings — via anchor verse (0 unique)**

(none)

**SD pointers — direct (0)**

(none)

**Auxiliary data**

_Root family (1):_

1. `NADAD` (Hebrew): filth

_Related words (4):_

1. H5075 ne.dad → to flee
2. H5076 ne.dud → tossing
3. H5079 nid.dah → impurity
4. H5206 ni.dah → filth

_Data-quality flags (1):_

1. flag_id=4 · meaning field is null for H5074. STEP returned no word analysis block for this term.

---

<a id="t-G3309"></a>
### G3309 merimnaō — to worry (`mti_id=2709`)

**Identity & meaning**

1. Strong's: `G3309` · Lang: Greek · Owner: OWNER
2. Registry: R007 anxiety · Legacy C-cluster: C06
3. Sub-group: —
4. Term status: extracted · Evidential: — · Occurrences: 25
5. Patch-authoring refs: `mti_id=2709` · `md_version=1` · `vc_status=not_done`
6. Mounce short-def: to worry, have anxiety, be concerned

**Verses:** 17 distinct locations (see §2 for the verse table grouped by sub-group).

**Group memberships (3)**

| Group ID | Code | Description | Notes |
|---|---|---|---|
| 222 | 2709-001 | Anxious inner preoccupation with material provision, bodily needs, and future security — orientation away from trust toward self-concerned worry |  |
| 223 | 2709-002 | Inner state of anticipatory anxiety in the face of threat — worry about what to say or do under pressure |  |
| 224 | 2709-003 | Divided or directed inner orientation of care — for the things of God or for worldly matters; also genuine care for others |  |

**Findings — direct (Strong's mention) (1)**

| Finding ID | Type | Anchor verses | Excerpt |
|---|---|---|---|
| DIM-7-001 | DIMENSION_REVIEW |  | merimnaō (G3309) operates in two distinct inner-being registers: anxious affective worry (2709-001, 2709-002) and volitional-attentional directed care (2709-003, 350-001). Session B should map how the same word spans these two registers and what this reveals about anxiety as both an affective state and a directional inner-being act. |

**Findings — via anchor verse (2 unique)**

| Finding ID | Type | Matched anchor refs | Excerpt |
|---|---|---|---|
| 182-F010 | VERSE_PATTERN | Phi 2:20 | The soul is constitutively relational: to God (Psa 42:1, 62:1, 63:1), to other souls (1Sa 18:1, Act 4:32), to its own orientation (dipsuchos — inner division). Soul-to-soul bonding (sumpsuchos, isopsuchos) documents genuine union of orientation between persons — community is possible when souls share direction. |
| DIM-69-001 | DIMENSION_REVIEW | Phili 4:6 | All three gratitude terms converge on Character/Disposition — gratitude is not a transient affective response but a stable inner reorientation of the whole person. The absence of gratitude as a diagnostic marker of inner corruption (5480-001) is a particularly significant finding. Session B should examine gratitude as a diagnostic indicator of inner-being health. |

**SD pointers — direct (0)**

(none)

**Auxiliary data**

_Related words (4):_

1. G3308 merimna → concern
2. G4305 promerimnaō → to worry beforehand
3. G3308 merimna → concern
4. G4305 promerimnaō → to worry beforehand

_Data-quality flags (4):_

1. flag_id=4 · meaning field is null for G3309. STEP returned no word analysis block for this term.
2. flag_id=47 · Meaning for G3309 stored as single prose block. STEP medium_def contains no structured sense numbering. No further subdivision available.
3. flag_id=4 · meaning field is null for G3309. STEP returned no word analysis block for this term.
4. flag_id=47 · Meaning for G3309 stored as single prose block. STEP medium_def contains no structured sense numbering. No further subdivision available.

---

<a id="t-H1672"></a>
### H1672 da.ag — be anxious (`mti_id=259`)

**Identity & meaning**

1. Strong's: `H1672` · Lang: Hebrew · Owner: OWNER
2. Registry: R061 fear · Legacy C-cluster: C06
3. Sub-group: —
4. Term status: extracted · Evidential: — · Occurrences: 7
5. Patch-authoring refs: `mti_id=259` · `md_version=1` · `vc_status=not_done`

**Verses:** 7 distinct locations (see §2 for the verse table grouped by sub-group).

**Group memberships (2)**

| Group ID | Code | Description | Notes |
|---|---|---|---|
| 887 | 259-001 | Term names the inner condition of anxiety — the worried, anxious state of the inner person in the face of uncertain or threatening circumstances |  |
| 888 | 259-002 | Term names inner sorrow over sin — the grief and contrition of the person who acknowledges wrongdoing |  |

**Findings — direct (Strong's mention) (0)**

(none)

**Findings — via anchor verse (0 unique)**

(none)

**SD pointers — direct (0)**

(none)

**Auxiliary data**

_Cross-references (2):_

1. 7 · anxiety · 
2. 53 · dread · 

_Root family (1):_

1. `DA.AG` (None): 

_Related words (17):_

1. None de.a.gah → anxiety
2. H1674 de.a.gah → anxiety
3. H1673 do.eg → Doeg
4. H1709G dag → Fish [Gate]
5. H1709H dag → fish
6. H1673 do.eg → Doeg
7. H1674 de.a.gah → anxiety
8. H1709G dag → Fish [Gate]
9. H1709H dag → fish
10. H1673 do.eg → Doeg
11. H1674 de.a.gah → anxiety
12. H1709G dag → Fish [Gate]
13. H1709H dag → fish
14. H1673 do.eg → Doeg
15. H1674 de.a.gah → anxiety
16. H1709G dag → Fish [Gate]
17. H1709H dag → fish

_Data-quality flags (8):_

1. flag_id=3 · Low occurrence count: 7. Statistical patterns unreliable with fewer than 20 occurrences.
2. flag_id=4 · meaning field is null for H1672. STEP returned no word analysis block for this term.
3. flag_id=3 · Low occurrence count: 7. Statistical patterns unreliable with fewer than 20 occurrences.
4. flag_id=4 · meaning field is null for H1672. STEP returned no word analysis block for this term.
5. flag_id=3 · Low occurrence count: 7. Statistical patterns unreliable with fewer than 20 occurrences.
6. flag_id=4 · meaning field is null for H1672. STEP returned no word analysis block for this term.
7. flag_id=3 · Low occurrence count: 7. Statistical patterns unreliable with fewer than 20 occurrences.
8. flag_id=4 · meaning field is null for H1672. STEP returned no word analysis block for this term.

---

<a id="t-G3308"></a>
### G3308 merimna — concern (`mti_id=350`)

**Identity & meaning**

1. Strong's: `G3308` · Lang: Greek · Owner: OWNER
2. Registry: R007 anxiety · Legacy C-cluster: C06
3. Sub-group: —
4. Term status: extracted · Evidential: — · Occurrences: 8
5. Patch-authoring refs: `mti_id=350` · `md_version=1` · `vc_status=not_done`
6. Mounce short-def: worry, concern, anxiety

**Verses:** 6 distinct locations (see §2 for the verse table grouped by sub-group).

**Group memberships (2)**

| Group ID | Code | Description | Notes |
|---|---|---|---|
| 220 | 350-001 | Anxious preoccupation with worldly concerns that competes with and displaces inner spiritual receptivity |  |
| 221 | 350-002 | Inner burden of care for others carried as expression of relational and pastoral orientation |  |

**Findings — direct (Strong's mention) (0)**

(none)

**Findings — via anchor verse (1 unique)**

| Finding ID | Type | Matched anchor refs | Excerpt |
|---|---|---|---|
| DIM-42-003 | DIMENSION_REVIEW | Luk 8:14 | Group 3090-001 (hēdonē — pleasure as the competing inner orientation, desires that war within) occupies a significant counter-position to the positive delight vocabulary. Pleasure as the adversary of the will toward God is a distinctive NT inner-being concept. Session B should examine the hēdonē / delight tension as a structural feature of the inner life. |

**SD pointers — direct (0)**

(none)

**Auxiliary data**

_Root family (1):_

1. `MERIMNA` (None): 

_Related words (9):_

1. None amerimnos → untroubled
2. None merimnaō → to worry
3. None promerimnaō → to worry beforehand
4. G3309 merimnaō → to worry
5. G4305 promerimnaō → to worry beforehand
6. G0275 amerimnos → untroubled
7. G0275 amerimnos → untroubled
8. G3309 merimnaō → to worry
9. G4305 promerimnaō → to worry beforehand

_Data-quality flags (6):_

1. flag_id=3 · Low occurrence count: 8. Statistical patterns unreliable with fewer than 20 occurrences.
2. flag_id=4 · meaning field is null for G3308. STEP returned no word analysis block for this term.
3. flag_id=47 · Meaning for G3308 stored as single prose block. STEP medium_def contains no structured sense numbering. No further subdivision available.
4. flag_id=3 · Low occurrence count: 8. Statistical patterns unreliable with fewer than 20 occurrences.
5. flag_id=4 · meaning field is null for G3308. STEP returned no word analysis block for this term.
6. flag_id=47 · Meaning for G3308 stored as single prose block. STEP medium_def contains no structured sense numbering. No further subdivision available.

---

<a id="t-H2976"></a>
### H2976 ya.ash — to despair (`mti_id=394`)

**Identity & meaning**

1. Strong's: `H2976` · Lang: Hebrew · Owner: OWNER
2. Registry: R078 hope · Legacy C-cluster: C04
3. Sub-group: —
4. Term status: extracted · Evidential: — · Occurrences: 6
5. Patch-authoring refs: `mti_id=394` · `md_version=1` · `vc_status=not_done`

**Verses:** 6 distinct locations (see §2 for the verse table grouped by sub-group).

**Group memberships (1)**

| Group ID | Code | Description | Notes |
|---|---|---|---|
| 1238 | 394-001 | Term names inner despair or hopelessness — the giving up of hope or expectation, whether as a state, a declaration, or the inner capitulation of pursuit |  |

**Findings — direct (Strong's mention) (0)**

(none)

**Findings — via anchor verse (0 unique)**

(none)

**SD pointers — direct (0)**

(none)

**Auxiliary data**

_Cross-references (1):_

1. 44 · despair · 

_Root family (1):_

1. `YAASH` (None): 

_Related words (2):_

1. H2979 ye.a.te.ray → Jeatherai
2. H2979 ye.a.te.ray → Jeatherai

_Data-quality flags (4):_

1. flag_id=3 · Low occurrence count: 6. Statistical patterns unreliable with fewer than 20 occurrences.
2. flag_id=4 · meaning field is null for H2976. STEP returned no word analysis block for this term.
3. flag_id=3 · Low occurrence count: 6. Statistical patterns unreliable with fewer than 20 occurrences.
4. flag_id=4 · meaning field is null for H2976. STEP returned no word analysis block for this term.

---

<a id="t-G1573"></a>
### G1573 ekkakeō — to lose heart (`mti_id=603`)

**Identity & meaning**

1. Strong's: `G1573` · Lang: Greek · Owner: OWNER
2. Registry: R183 heart · Legacy C-cluster: C01
3. Sub-group: —
4. Term status: extracted · Evidential: — · Occurrences: 6
5. Patch-authoring refs: `mti_id=603` · `md_version=1` · `vc_status=not_done`
6. Mounce short-def: to lose heart

**Verses:** 6 distinct locations (see §2 for the verse table grouped by sub-group).

**Group memberships (1)**

| Group ID | Code | Description | Notes |
|---|---|---|---|
| 2716 | 603-001 | Term names the inner loss of heart — the fading of inner courage and resolve in the face of suffering or opposition |  |

**Findings — direct (Strong's mention) (0)**

(none)

**Findings — via anchor verse (0 unique)**

(none)

**SD pointers — direct (0)**

(none)

**Auxiliary data**

_Root family (1):_

1. `COURAGE` (None): 

_Related words (6):_

1. G1537 ek → out from
2. G2556G kakos → evil/harm: evil
3. G2556H kakos → evil/harm: harm
4. G2556H kakos → evil/harm: harm
5. G2556G kakos → evil/harm: evil
6. G1537 ek → out from

_Data-quality flags (3):_

1. flag_id=3 · Low occurrence count: 6. Statistical patterns unreliable with fewer than 20 occurrences.
2. flag_id=4 · meaning field is null for G1573. STEP returned no word analysis block for this term.
3. flag_id=47 · Meaning for G1573 stored as single prose block. STEP medium_def contains no structured sense numbering. No further subdivision available.

_Term flags (1):_

1. mti_term_id=603, flag_id=1

---

<a id="t-H3512A"></a>
### H3512A ka.ah — be disheartened (`mti_id=574`)

**Identity & meaning**

1. Strong's: `H3512A` · Lang: Hebrew · Owner: OWNER
2. Registry: R183 heart · Legacy C-cluster: C01
3. Sub-group: —
4. Term status: extracted · Evidential: — · Occurrences: 3
5. Patch-authoring refs: `mti_id=574` · `md_version=1` · `vc_status=not_done`

**Verses:** 3 distinct locations (see §2 for the verse table grouped by sub-group).

**Group memberships (1)**

| Group ID | Code | Description | Notes |
|---|---|---|---|
| 2739 | 574-001 | Term names the disheartened inner state — the inner being made faint and discouraged by opposition |  |

**Findings — direct (Strong's mention) (0)**

(none)

**Findings — via anchor verse (0 unique)**

(none)

**SD pointers — direct (0)**

(none)

**Auxiliary data**

_Root family (1):_

1. `KA.AH` (None): 

_Related words (4):_

1. None ka.eh → disheartened
2. H3512B ka.eh → disheartened
3. H3512B ka.eh → disheartened
4. H3512B ka.eh → disheartened

_Data-quality flags (6):_

1. flag_id=3 · Only 3 confirmed verse records for H3512A. Threshold is 5.
2. flag_id=4 · meaning field is null for H3512A. STEP returned no word analysis block for this term.
3. flag_id=3 · Only 3 confirmed verse records for H3512A. Threshold is 5.
4. flag_id=4 · meaning field is null for H3512A. STEP returned no word analysis block for this term.
5. flag_id=3 · Only 4 confirmed verse records for H3512A. Threshold is 5.
6. flag_id=4 · meaning field is null for H3512A. STEP returned no word analysis block for this term.

---

<a id="t-H3512B"></a>
### H3512B ka.eh — disheartened (`mti_id=1700`)

**Identity & meaning**

1. Strong's: `H3512B` · Lang: Hebrew · Owner: OWNER
2. Registry: R061 fear · Legacy C-cluster: C06
3. Sub-group: —
4. Term status: extracted · Evidential: — · Occurrences: 1
5. Patch-authoring refs: `mti_id=1700` · `md_version=1` · `vc_status=not_done`

**Verses:** 3 distinct locations (see §2 for the verse table grouped by sub-group).

**Group memberships (1)**

| Group ID | Code | Description | Notes |
|---|---|---|---|
| 1014 | 1700-001 | Term names the inner condition of being disheartened — the faint, broken, or discouraged state of the inner person under pressure or affliction |  |

**Findings — direct (Strong's mention) (0)**

(none)

**Findings — via anchor verse (0 unique)**

(none)

**SD pointers — direct (0)**

(none)

**Auxiliary data**

_Related words (3):_

1. H3512A ka.ah → be disheartened
2. H3512A ka.ah → be disheartened
3. H3512A ka.ah → be disheartened

_Data-quality flags (9):_

1. flag_id=3 · Only 3 confirmed verse records for H3512B. Threshold is 5.
2. flag_id=4 · meaning field is null for H3512B. STEP returned no word analysis block for this term.
3. flag_id=47 · Meaning for H3512B stored as single prose block. STEP medium_def contains no structured sense numbering. No further subdivision available.
4. flag_id=3 · Only 3 confirmed verse records for H3512B. Threshold is 5.
5. flag_id=4 · meaning field is null for H3512B. STEP returned no word analysis block for this term.
6. flag_id=47 · Meaning for H3512B stored as single prose block. STEP medium_def contains no structured sense numbering. No further subdivision available.
7. flag_id=3 · Only 3 confirmed verse records for H3512B. Threshold is 5.
8. flag_id=4 · meaning field is null for H3512B. STEP returned no word analysis block for this term.
9. flag_id=47 · Meaning for H3512B stored as single prose block. STEP medium_def contains no structured sense numbering. No further subdivision available.

---

<a id="t-G1820"></a>
### G1820 exaporeō — to despair (`mti_id=808`)

**Identity & meaning**

1. Strong's: `G1820` · Lang: Greek · Owner: OWNER
2. Registry: R044 despair · Legacy C-cluster: C06
3. Sub-group: —
4. Term status: extracted · Evidential: — · Occurrences: 3
5. Patch-authoring refs: `mti_id=808` · `md_version=1` · `vc_status=not_done`
6. Mounce short-def: (<i>middle</i>) to despair; (<i>passive</i>) to be in despair

**Verses:** 2 distinct locations (see §2 for the verse table grouped by sub-group).

**Group memberships (1)**

| Group ID | Code | Description | Notes |
|---|---|---|---|
| 660 | 808-001 | Term names despair as the complete collapse of inner expectation and hope — the inner being brought beyond what it can sustain, unable to see forward |  |

**Findings — direct (Strong's mention) (0)**

(none)

**Findings — via anchor verse (0 unique)**

(none)

**SD pointers — direct (0)**

(none)

**Auxiliary data**

_Root family (1):_

1. `EXAPOR` (Greek): to despair

_Related words (2):_

1. G0639 aporeō → be perplexed
2. G1537 ek → out from

_Data-quality flags (3):_

1. flag_id=3 · Only 2 confirmed verse records for G1820. Threshold is 5.
2. flag_id=4 · meaning field is null for G1820. STEP returned no word analysis block for this term.
3. flag_id=47 · Meaning for G1820 stored as single prose block. STEP medium_def contains no structured sense numbering. No further subdivision available.

---

<a id="t-G1365"></a>
### G1365 distazō — to doubt (`mti_id=1288`)

**Identity & meaning**

1. Strong's: `G1365` · Lang: Greek · Owner: OWNER
2. Registry: R191 doubt · Legacy C-cluster: C16
3. Sub-group: —
4. Term status: extracted · Evidential: — · Occurrences: 2
5. Patch-authoring refs: `mti_id=1288` · `md_version=1` · `vc_status=not_done`
6. Mounce short-def: to doubt

**Verses:** 2 distinct locations (see §2 for the verse table grouped by sub-group).

**Group memberships (1)**

| Group ID | Code | Description | Notes |
|---|---|---|---|
| 3060 | 1288-001 | Term names doubt as the inner experience of wavering — faith faltering between trust and hesitation — addressed directly by Jesus | Revised during Dimension Review Phase B: VCB-022 patch truncated context_description at 80 characters. Full description restored from wa-vcb-022-term-observations-v2.8-20260404.md |

**Findings — direct (Strong's mention) (0)**

(none)

**Findings — via anchor verse (0 unique)**

(none)

**SD pointers — direct (0)**

(none)

**Auxiliary data**

_Root family (1):_

1. `DISTAZŌ` (Greek): to doubt

_Data-quality flags (3):_

1. flag_id=3 · Only 2 confirmed verse records for G1365. Threshold is 5.
2. flag_id=4 · meaning field is null for G1365. STEP returned no word analysis block for this term.
3. flag_id=47 · Meaning for G1365 stored as single prose block. STEP medium_def contains no structured sense numbering. No further subdivision available.

---

<a id="t-G1374"></a>
### G1374 dipsuchos — double-minded (`mti_id=1398`)

**Identity & meaning**

1. Strong's: `G1374` · Lang: Greek · Owner: OWNER
2. Registry: R112 mind · Legacy C-cluster: C01
3. Sub-group: —
4. Term status: extracted · Evidential: research_not_required · Occurrences: 2
5. Patch-authoring refs: `mti_id=1398` · `md_version=1` · `vc_status=not_done`
6. Mounce short-def: double-minded
7. Retention note: Legacy evidential_status=confirmed mapped to research_not_required (M29 remap 2026-04-20)

**Verses:** 2 distinct locations (see §2 for the verse table grouped by sub-group).

**Group memberships (1)**

| Group ID | Code | Description | Notes |
|---|---|---|---|
| 1792 | 1398-001 | Term names inner division of allegiance — the person whose loyalty is split between God and the world, producing instability |  |

**Findings — direct (Strong's mention) (1)**

| Finding ID | Type | Anchor verses | Excerpt |
|---|---|---|---|
| DIM-112-002 | DIMENSION_REVIEW |  | se.eph (4198-001, H5588) and dipsuchos (1398-001, G1374) form an OT/NT pair documenting inner division as a cross-testament moral pathology. Both assigned Moral/Conscience. Session B: analyse together as witnesses to the same inner-being phenomenon — the split allegiance that makes the person unstable before God. |

**Findings — via anchor verse (1 unique)**

| Finding ID | Type | Matched anchor refs | Excerpt |
|---|---|---|---|
| 112-F009 | VERSE_PATTERN | Jas 1:8, Jas 4:8 | Double-mindedness (dipsuchos/se.eph) documents inner division as a cross-testament pathology. James presents inner unity as a condition for receiving from God and for effective action; Ps 119:113 makes it a moral stance. |

**SD pointers — direct (2)**

| Pointer | Priority | Strong's ref | Description |
|---|---|---|---|
| 182-SD005 | MEDIUM | G1374 | G1374 dipsuchos shared with mind registry (112). Inner division documented in both soul and mind vocabularies — double-minded (soul) and double-minded (nous). Cross-registry pattern of inner unity vs division. |
| DIM-112-SD005 | MEDIUM |  | Inner-division theme across Greek and Hebrew vocabularies. dipsuchos G1374 (1398-001), se.eph H5588 (4198-001), dianoia-corrupted (995-002), nous-corrupted (994-002), isopsuchos G2473 (1402-001 — positive counterpart). Multiple terms from different roots/languages naming divided loyalty / split mind / darkened understanding. Distribution across 05 Moral Character, 03 Cognition, 06 Relational Disposition. Session D should trace across C17 and C22. |

**Auxiliary data**

_Root family (2):_

1. `G5590G` (Greek): 
2. `DIPSUCH` (Greek): like-minded

_Related words (56):_

1. G0674 apopsuchō → to faint — STEP relatedNos
2. G0895 apsuchos → lifeless — STEP relatedNos
3. G1364 dis → twice — STEP relatedNos
4. G1634 ekpsuchō → to expire — STEP relatedNos
5. G2174 eupsucheō → be glad — STEP relatedNos
6. G2473 isopsuchos → like-minded — STEP relatedNos
7. G3642 oligopsuchos → fainthearted — STEP relatedNos
8. G4861 sumpsuchos → harmonious — STEP relatedNos
9. G5590G psuchē → soul — STEP relatedNos
10. G5590H psuchē → soul: life — STEP relatedNos
11. G5590I psuchē → soul: myself — STEP relatedNos
12. G5590J psuchē → soul: person — STEP relatedNos
13. G5590K psuchē → soul: animal — STEP relatedNos
14. G5591 psuchikos → natural — STEP relatedNos
15. G0674 apopsuchō → to faint
16. G0895 apsuchos → lifeless
17. G1364 dis → twice
18. G1634 ekpsuchō → to expire
19. G2174 eupsucheō → be glad
20. G2473 isopsuchos → like-minded
21. G3642 oligopsuchos → fainthearted
22. G4861 sumpsuchos → harmonious
23. G5590G psuchē → soul
24. G5590H psuchē → soul: life
25. G5590I psuchē → soul: myself
26. G5590J psuchē → soul: person
27. G5590K psuchē → soul: animal
28. G5591 psuchikos → natural
29. G0674 apopsuchō → to faint
30. G0895 apsuchos → lifeless
31. G1364 dis → twice
32. G1634 ekpsuchō → to expire
33. G2174 eupsucheō → be glad
34. G2473 isopsuchos → like-minded
35. G3642 oligopsuchos → fainthearted
36. G4861 sumpsuchos → harmonious
37. G5590G psuchē → soul
38. G5590H psuchē → soul: life
39. G5590I psuchē → soul: myself
40. G5590J psuchē → soul: person
41. G5590K psuchē → soul: animal
42. G5591 psuchikos → natural
43. G0674 apopsuchō → to faint
44. G0895 apsuchos → lifeless
45. G1364 dis → twice
46. G1634 ekpsuchō → to expire
47. G2174 eupsucheō → be glad
48. G2473 isopsuchos → like-minded
49. G3642 oligopsuchos → fainthearted
50. G4861 sumpsuchos → harmonious
51. G5590G psuchē → soul
52. G5590H psuchē → soul: life
53. G5590I psuchē → soul: myself
54. G5590J psuchē → soul: person
55. G5590K psuchē → soul: animal
56. G5591 psuchikos → natural

_Data-quality flags (12):_

1. flag_id=3 · Only 2 confirmed verse records for G1374. Threshold is 5.
2. flag_id=4 · meaning field is null for G1374. STEP returned no word analysis block for this term.
3. flag_id=47 · Meaning for G1374 stored as single prose block. STEP medium_def contains no structured sense numbering. No further subdivision available.
4. flag_id=3 · Only 2 confirmed verse records for G1374. Threshold is 5.
5. flag_id=4 · meaning field is null for G1374. STEP returned no word analysis block for this term.
6. flag_id=47 · Meaning for G1374 stored as single prose block. STEP medium_def contains no structured sense numbering. No further subdivision available.
7. flag_id=3 · Only 2 confirmed verse records for G1374. Threshold is 5.
8. flag_id=4 · meaning field is null for G1374. STEP returned no word analysis block for this term.
9. flag_id=47 · Meaning for G1374 stored as single prose block. STEP medium_def contains no structured sense numbering. No further subdivision available.
10. flag_id=3 · Only 2 confirmed verse records for G1374. Threshold is 5.
11. flag_id=4 · meaning field is null for G1374. STEP returned no word analysis block for this term.
12. flag_id=47 · Meaning for G1374 stored as single prose block. STEP medium_def contains no structured sense numbering. No further subdivision available.

---

<a id="t-G0560"></a>
### G0560 apelpizo — to despair (`mti_id=402`)

**Identity & meaning**

1. Strong's: `G0560` · Lang: Greek · Owner: OWNER
2. Registry: R078 hope · Legacy C-cluster: C04
3. Sub-group: —
4. Term status: extracted · Evidential: — · Occurrences: 2
5. Patch-authoring refs: `mti_id=402` · `md_version=1` · `vc_status=not_done`
6. Mounce short-def: to expect nothing in return

**Verses:** 1 distinct locations (see §2 for the verse table grouped by sub-group).

**Group memberships (1)**

| Group ID | Code | Description | Notes |
|---|---|---|---|
| 1222 | 402-001 | Term names the inner disposition of expecting nothing in return — the absence of self-directed hope as the posture of genuine love |  |

**Findings — direct (Strong's mention) (0)**

(none)

**Findings — via anchor verse (4 unique)**

| Finding ID | Type | Matched anchor refs | Excerpt |
|---|---|---|---|
| OBS-099-T2-002 | OBSERVATION | Luke 6:35 | Scripture explicitly and extensively attributes kindness to God in three forms: (a) direct predication — "God is kind to the ungrateful and evil" (Luke 6:35); "the Lord is kind in all his works" (Psa 145:17 [XREG: H2623, OBS-099-095]); (b) superlative attribution — "abounding in steadfast love" (Exo 34:6), "steadfast love is better than life" (Psa 63:3 [XREG: H2617A, OBS-099-084]); (c) instrumental attribution — "God's kindness is meant to lead you to repentance" (Rom 2:4, OBS-099-076). The significance for the human person: divine kindness is God's defining attribute; the call for human kindness is ontological grounding — to be kind is to be what the image-bearer was created to be. The absence of kindness is not merely behavioural failure but dimming of the image. |
| OBS-099-T2-021 | OBSERVATION | Luke 6:35 | Yes — three contextual variations: (a) Divine vs. human scope: God's chesed inexhaustible; human chesed creaturely and can be withdrawn [XREG: H2617A, OBS-099-083, Q&A-008]. (b) Comfort vs. affliction: Job 6:4 (afflicting presence) vs. Psa 23:4 (comforting presence) — same term, different mode by context and divine purpose [OBS-099-067/066]. (c) Purposive vs. sustaining: Rom 2:4 — kindness aimed at repentance; Luke 6:35 — kindness to ungrateful without stated aim [OBS-099-076, OBS-099-078]. Purposive dimension present in some contexts; absent as explicit feature in others. |
| OBS-099-T2-055 | OBSERVATION | Luke 6:35 | Most extensively evidenced direction in the registry. H2617A group 536-001 (180 relevant verses, dominant subject GOD [XREG: H2617A, OBS-099-083]) documents the full range. (a) How: specific historical acts (Exo 15:13; 2Sa 7:15 [XREG: H2617A, OBS-099-089]); through his presence (Psa 23:4 [OBS-099-066]); through forgiveness (Exo 34:6–7); eschatologically through Christ (Eph 2:7 [XREG: G5544, OBS-099-093]). (b) Basis: covenantal (to those who love him — Exo 20:6) and unconditional in ultimate attribute (never ceases — Lam 3:22 [XREG: H2617A, OBS-099-085]; reaches ungrateful — Luke 6:35 [OBS-099-078]). Conditionality is in manifestation; attribute itself is unconditional. (c) What it reveals: God whose primary inner disposition toward the creature is committed faithful generous good will — chesed before, through, and after judgment. |
| OBS-099-T2-085 | OBSERVATION | Luke 6:35 | The evidence is not entirely silent on relational boundaries but is thin. Luke 6:35 — "love your enemies and do good... and you will be sons of the Most High, for he is kind to the ungrateful and the evil" — explicitly extends kindness beyond the deserving and beyond the covenant partner to include enemies and the ungrateful [OBS-099-078]. This is the most direct boundary-crossing statement in the evidence: kindness is not restricted to those who merit it or belong to the covenant community. The chesed evidence (Exo 20:6 — showing chesed to those who love God and keep his commandments) suggests covenantal conditionality in its sustained manifestation, but Luke 6:35 shows it reaching across that boundary in its initiating mode. The precise scope — how far the boundary extends and what distinguishes sustained chesed from initiating kindness — is not fully resolved from the evidence and requires Session D cross-registry examination. |

**SD pointers — direct (0)**

(none)

**Auxiliary data**

_Root family (1):_

1. `ELPIS` (None): 

_Related words (4):_

1. G0575 apo → away from
2. G1679 elpizō → to hope/expect
3. G1679 elpizō → to hope/expect
4. G0575 apo → away from

_Data-quality flags (3):_

1. flag_id=3 · Only 1 confirmed verse records for G0560. Threshold is 5.
2. flag_id=4 · meaning field is null for G0560. STEP returned no word analysis block for this term.
3. flag_id=47 · Meaning for G0560 stored as single prose block. STEP medium_def contains no structured sense numbering. No further subdivision available.

---

<a id="t-G3642"></a>
### G3642 oligopsuchos — fainthearted (`mti_id=1403`)

**Identity & meaning**

1. Strong's: `G3642` · Lang: Greek · Owner: OWNER
2. Registry: R182 Soul · Legacy C-cluster: C01
3. Sub-group: —
4. Term status: extracted · Evidential: research_not_required · Occurrences: 7
5. Patch-authoring refs: `mti_id=1403` · `md_version=1` · `vc_status=not_done`
6. Mounce short-def: timid, fainthearted, discouraged
7. Retention note: Legacy evidential_status=confirmed mapped to research_not_required (M29 remap 2026-04-20)

**Verses:** 1 distinct locations (see §2 for the verse table grouped by sub-group).

**Group memberships (1)**

| Group ID | Code | Description | Notes |
|---|---|---|---|
| 2657 | 1403-001 | Term names the fainthearted inner state — the soul diminished in courage, needing encouragement from others |  |

**Findings — direct (Strong's mention) (0)**

(none)

**Findings — via anchor verse (0 unique)**

(none)

**SD pointers — direct (0)**

(none)

**Auxiliary data**

_Root family (1):_

1. `G5590G` (Greek): 

_Related words (42):_

1. G0674 apopsuchō → to faint — STEP relatedNos
2. G0895 apsuchos → lifeless — STEP relatedNos
3. G1374 dipsuchos → double-minded — STEP relatedNos
4. G1634 ekpsuchō → to expire — STEP relatedNos
5. G2174 eupsucheō → be glad — STEP relatedNos
6. G2473 isopsuchos → like-minded — STEP relatedNos
7. G3641 oligos → little/few — STEP relatedNos
8. G4861 sumpsuchos → harmonious — STEP relatedNos
9. G5590G psuchē → soul — STEP relatedNos
10. G5590H psuchē → soul: life — STEP relatedNos
11. G5590I psuchē → soul: myself — STEP relatedNos
12. G5590J psuchē → soul: person — STEP relatedNos
13. G5590K psuchē → soul: animal — STEP relatedNos
14. G5591 psuchikos → natural — STEP relatedNos
15. G0674 apopsuchō → to faint
16. G0895 apsuchos → lifeless
17. G1374 dipsuchos → double-minded
18. G1634 ekpsuchō → to expire
19. G2174 eupsucheō → be glad
20. G2473 isopsuchos → like-minded
21. G3641 oligos → little/few
22. G4861 sumpsuchos → harmonious
23. G5590G psuchē → soul
24. G5590H psuchē → soul: life
25. G5590I psuchē → soul: myself
26. G5590J psuchē → soul: person
27. G5590K psuchē → soul: animal
28. G5591 psuchikos → natural
29. G0674 apopsuchō → to faint
30. G0895 apsuchos → lifeless
31. G1374 dipsuchos → double-minded
32. G1634 ekpsuchō → to expire
33. G2174 eupsucheō → be glad
34. G2473 isopsuchos → like-minded
35. G3641 oligos → little/few
36. G4861 sumpsuchos → harmonious
37. G5590G psuchē → soul
38. G5590H psuchē → soul: life
39. G5590I psuchē → soul: myself
40. G5590J psuchē → soul: person
41. G5590K psuchē → soul: animal
42. G5591 psuchikos → natural

_Data-quality flags (12):_

1. flag_id=3 · Only 1 confirmed verse records for G3642. Threshold is 5.
2. flag_id=4 · meaning field is null for G3642. STEP returned no word analysis block for this term.
3. flag_id=47 · Meaning for G3642 stored as single prose block. STEP medium_def contains no structured sense numbering. No further subdivision available.
4. flag_id=3 · Only 1 confirmed verse records for G3642. Threshold is 5.
5. flag_id=4 · meaning field is null for G3642. STEP returned no word analysis block for this term.
6. flag_id=47 · Meaning for G3642 stored as single prose block. STEP medium_def contains no structured sense numbering. No further subdivision available.
7. flag_id=3 · Only 1 confirmed verse records for G3642. Threshold is 5.
8. flag_id=4 · meaning field is null for G3642. STEP returned no word analysis block for this term.
9. flag_id=47 · Meaning for G3642 stored as single prose block. STEP medium_def contains no structured sense numbering. No further subdivision available.
10. flag_id=3 · Only 1 confirmed verse records for G3642. Threshold is 5.
11. flag_id=4 · meaning field is null for G3642. STEP returned no word analysis block for this term.
12. flag_id=47 · Meaning for G3642 stored as single prose block. STEP medium_def contains no structured sense numbering. No further subdivision available.

---

<a id="t-G0120"></a>
### G0120 athumeō — be discouraged (`mti_id=2078`)

**Identity & meaning**

1. Strong's: `G0120` · Lang: Greek · Owner: OWNER
2. Registry: R035 covetousness · Legacy C-cluster: C13
3. Sub-group: —
4. Term status: extracted_thin · Evidential: — · Occurrences: 8
5. Patch-authoring refs: `mti_id=2078` · `md_version=1` · `vc_status=not_done`
6. Mounce short-def: to be discouraged, lose heart

**Verses:** 1 distinct locations (see §2 for the verse table grouped by sub-group).

**Group memberships (1)**

| Group ID | Code | Description | Notes |
|---|---|---|---|
| 489 | 2078-001 | The inner state of discouragement — loss of heart produced by provocation |  |

**Findings — direct (Strong's mention) (0)**

(none)

**Findings — via anchor verse (0 unique)**

(none)

**SD pointers — direct (0)**

(none)

**Auxiliary data**

_Root family (1):_

1. `ATHUM` (Greek): eager

_Related words (54):_

1. G1937 epithumeō → to long for
2. G1938 epithumētēs → one who desires
3. G1939 epithumia → desire
4. G2114 euthumeō → be cheerful
5. G2115 euthumos → encouraging
6. G2372 thumos → wrath
7. G4288 prothumia → eagerness
8. G4289 prothumos → eager
9. G4290 prothumōs → eagerly
10. G1937 epithumeō → to long for
11. G1938 epithumētēs → one who desires
12. G1939 epithumia → desire
13. G2114 euthumeō → be cheerful
14. G2115 euthumos → encouraging
15. G2372 thumos → wrath
16. G4288 prothumia → eagerness
17. G4289 prothumos → eager
18. G4290 prothumōs → eagerly
19. G1937 epithumeō → to long for
20. G1938 epithumētēs → one who desires
21. G1939 epithumia → desire
22. G2114 euthumeō → be cheerful
23. G2115 euthumos → encouraging
24. G2372 thumos → wrath
25. G4288 prothumia → eagerness
26. G4289 prothumos → eager
27. G4290 prothumōs → eagerly
28. G1937 epithumeō → to long for
29. G1938 epithumētēs → one who desires
30. G1939 epithumia → desire
31. G2114 euthumeō → be cheerful
32. G2115 euthumos → encouraging
33. G2372 thumos → wrath
34. G4288 prothumia → eagerness
35. G4289 prothumos → eager
36. G4290 prothumōs → eagerly
37. G1937 epithumeō → to long for
38. G1938 epithumētēs → one who desires
39. G1939 epithumia → desire
40. G2114 euthumeō → be cheerful
41. G2115 euthumos → encouraging
42. G2372 thumos → wrath
43. G4288 prothumia → eagerness
44. G4289 prothumos → eager
45. G4290 prothumōs → eagerly
46. G1937 epithumeō → to long for
47. G1938 epithumētēs → one who desires
48. G1939 epithumia → desire
49. G2114 euthumeō → be cheerful
50. G2115 euthumos → encouraging
51. G2372 thumos → wrath
52. G4288 prothumia → eagerness
53. G4289 prothumos → eager
54. G4290 prothumōs → eagerly

_Data-quality flags (19):_

1. flag_id=3 · Low occurrence count: 8. Statistical patterns unreliable with fewer than 20 occurrences.
2. flag_id=1 · Zero confirmed verse records for G0120.
3. flag_id=4 · meaning field is null for G0120. STEP returned no word analysis block for this term.
4. flag_id=47 · Meaning for G0120 stored as single prose block. STEP medium_def contains no structured sense numbering. No further subdivision available.
5. flag_id=3 · Only 1 confirmed verse records for G0120. Threshold is 5.
6. flag_id=4 · meaning field is null for G0120. STEP returned no word analysis block for this term.
7. flag_id=47 · Meaning for G0120 stored as single prose block. STEP medium_def contains no structured sense numbering. No further subdivision available.
8. flag_id=3 · Only 1 confirmed verse records for G0120. Threshold is 5.
9. flag_id=4 · meaning field is null for G0120. STEP returned no word analysis block for this term.
10. flag_id=47 · Meaning for G0120 stored as single prose block. STEP medium_def contains no structured sense numbering. No further subdivision available.
11. flag_id=3 · Only 1 confirmed verse records for G0120. Threshold is 5.
12. flag_id=4 · meaning field is null for G0120. STEP returned no word analysis block for this term.
13. flag_id=47 · Meaning for G0120 stored as single prose block. STEP medium_def contains no structured sense numbering. No further subdivision available.
14. flag_id=3 · Only 1 confirmed verse records for G0120. Threshold is 5.
15. flag_id=4 · meaning field is null for G0120. STEP returned no word analysis block for this term.
16. flag_id=47 · Meaning for G0120 stored as single prose block. STEP medium_def contains no structured sense numbering. No further subdivision available.
17. flag_id=3 · Only 1 confirmed verse records for G0120. Threshold is 5.
18. flag_id=4 · meaning field is null for G0120. STEP returned no word analysis block for this term.
19. flag_id=47 · Meaning for G0120 stored as single prose block. STEP medium_def contains no structured sense numbering. No further subdivision available.

---

<a id="s4"></a>
## §4. Appendix — items linked at registry or collection level

<a id="s4-1"></a>
### §4.1 Findings from contributor registries with no term-level link (39)

These findings sit on a registry that contributes terms to this cluster, but their text and anchor verses don't resolve to any specific cluster term. Candidates for term-level enrichment.

| Finding ID | Type | Registry | Anchor verses | Excerpt |
|---|---|---|---|---|
| DIM-35-001 | DIMENSION_REVIEW | R035 covetousness |  | Reg 35 contains two analytically distinct sub-clusters: (1) willing-spirit/eager-disposition (prothumia, prothumos, prothumōs, euthumeō, euthumos, athumeō) and (2) covetous-desire proper (pleonexia). Session B should treat these as distinct inner-being phenomena requiring separate analytical attention. |
| DIM-44-001 | DIMENSION_REVIEW | R044 despair |  | The la/lo negation terms (H3809, H3808) build inner-being content through naming what is absent, refused, or withheld. The word does not carry inner-being content directly — it reveals inner states by negating them. Session B should examine this structural inversion as a distinctive biblical rhetoric for naming despair, faith-failure, and inner collapse. |
| DIM-78-001 | DIMENSION_REVIEW | R078 hope |  | Hope in Registry 78 divides into three distinct modes: (a) hope as orientation or act directed toward God (Spiritual/God-ward — 30 groups across cluster); (b) hope as a constitutive inner quality or capacity of the person (Character/Disposition — groups 385-001, 401-002, 402-001, 968-001); (c) hope's absence, collapse, or disappointment (Affective/Emotional). Session B should assess whether these are three aspects of one dimension or three distinct inner-being engagements. |
| 112-F001 | TERM_BEHAVIOUR | R112 mind | Gen 8:1, Exo 2:24, Deu 5:15, Deu 8:2, Joh 14:26 | Memory in biblical vocabulary is an active, covenantal, morally significant act — not passive cognitive retrieval. God's remembering produces redemptive action; Israel's commanded remembering constitutes covenant identity; forgetting is moral defection. |
| 112-F002 | THEOLOGICAL_NOTE | R112 mind | Rom 1:28, Rom 12:2, Eph 4:17, Col 1:21, 1Cor 2:16 | The mind is a moral organ before it is an intellectual one. It can be debased, blinded, corrupted, renewed, and transferred (mind of Christ). Romans 12:2 presents renewal of the nous as the locus of personal transformation. |
| 112-F003 | ETYMOLOGY | R112 mind | Gen 6:5, Gen 8:21, Isa 26:3 | The ye.tser (formed inclination) is the OT anthropology's closest approach to a foundational moral disposition. Gen 6:5 and 8:21 establish it as bent toward evil from youth — the dispositional substrate generating particular thoughts and plans. |
| 112-F004 | VERSE_PATTERN | R112 mind | Pro 12:5, Pro 15:26, Jer 29:11, Ps 140:2 | The cha.shav root documents that the same mental faculty produces artistic design, moral reasoning, and malicious plotting — there is no separate creative vs rational faculty in Hebrew anthropology. God's planning uses the same root as wicked scheming. |
| 112-F005 | THEOLOGICAL_NOTE | R112 mind | Rom 8:5, Rom 8:6, Rom 8:7 | Fronēma (the set mindset) in Romans 8:5-7 is the determinative factor for life or death, peace or enmity with God — making the mind's fundamental orientation soteriologically significant, not merely morally relevant. |
| 112-F006 | THEOLOGICAL_NOTE | R112 mind | Rom 2:15, 1Cor 8:7, Heb 9:14, 1Tim 4:2 | Suneidēsis (conscience) is the NT's distinctive contribution with no direct Hebrew equivalent. The conscience can be weak, clear, seared, or purified (Heb 9:14), and functions as a bridge between inner life and relational/covenantal domains. |
| 112-F007 | VERSE_PATTERN | R112 mind | Deu 4:9 | Deu 4:9 functionally links the sha.mar attentiveness cluster with the za.khar memory cluster: vigilant attentiveness is the means by which memory is maintained; forgetting is the product of failed attentiveness. |
| 112-F008 | TERM_BEHAVIOUR | R112 mind | 1Cor 14:14, 1Cor 14:15 | The 1 Cor 14:14-15 nous/pneuma distinction is the sharpest NT terminological boundary between mind-level and spirit-level inner operation — directly relevant to the Framework B spirit-soul-body boundary investigation. |
| 112-F010 | THEOLOGICAL_NOTE | R112 mind | Heb 8:10, Heb 10:16 | The Hebrews new covenant quotation (Heb 8:10; 10:16) names both dianoia (mind) and kardia (heart) as sites of internalized law — anticipating the structural relationship between Registries 112 and 183 for Session D investigation. |
| DIM-112-001 | DIMENSION_REVIEW | R112 mind |  | sha.mar family (H8104) spans four dimensions across Registry 112: Volitional/Will (G, covenantal obedience), Theological/Divine-Human (H, God's guarding), Moral/Conscience (H subset self-guarding; I attentive observation), Character/Disposition (J, vigilance). Session B: map the full sha.mar semantic range across all inner-being functions. |
| DIM-112-003 | DIMENSION_REVIEW | R112 mind |  | ye.tser (936-001/936-002, H3336) spans Moral/Conscience (formed moral inclination toward evil or good) and Theological/Divine-Human (creaturely formation known and addressed by God). The OT's closest approach to a foundational moral disposition is simultaneously a moral reality and a creaturely-relational one. Session B: the ye.tser as the dispositional substrate of moral life. |
| DIM-112-004 | DIMENSIONAL_PATTERN | R112 mind |  | Covenant-renewal convergence across registries — Dimension 11 cluster. Five groups across r112 and r183 describe God's inner-being covenant act renewing the human person: dianoia law-writing (995-003, Heb 8:10/10:16), mnaomai non-remembrance (4413-003, Heb 8:12/10:17), le.vav circumcision/renewal (179-009, Deut 30:6), qe.rev new covenant writing (577-003, Jer 31:33), enkainizō inaugural renewal (602-001, Heb 10:20). Coordinated Dimension 11 event across multiple inner-being terms and registries. |
| DIM-112-005 | DIMENSIONAL_PATTERN | R112 mind |  | sha.mar root family dimensional breadth. Five sense-splits in r112 occupy five different dimensions: 4379-001 (obedience) → 04 Volition; 4380-001 (divine guarding) → 11 D-H Correspondence GOD; 4380-002 (self-guarding) → 11 D-H Correspondence HUMAN; 4381-001 (moral observation) → 03 Cognition; 4382-001 (vigilance) → 05 Moral Character. Illustrates directionally-determined inner-faculty principle. |
| DIM-112-006 | DIMENSIONAL_PATTERN | R112 mind |  | Divine reckoning and divine remembrance as paired Dimension 11 patterns. cha.shav 3335-001 (imputation, Gen 15:6/Rom 4) and mnaomai 4413-002 (divine remembrance producing effect) both name divine inner acts determining human standing. Both Dimension 11 GOD. Foundational pair for Session B studies of reckoning/imputation vocabulary. |
| DIM-112-007 | DIMENSIONAL_PATTERN | R112 mind |  | Memorial vocabulary as Dimension 11. Three AZKARAH groups (3498-001 zikkaron institutional, 3498-002 zikkaron priestly, 3499-001 az.ka.rah memorial portion) plus anamnēsis 4426-001 (eucharistic) all engage divine-human correspondence. The memorial is a structure of mutual remembrance between God and community — unifies OT offering vocabulary and NT eucharist vocabulary on the dimension axis. |
| 182-F001 | ETYMOLOGY | R182 Soul | Psa 69:1, Psa 105:18, Gen 2:7 | Ne.phesh derives from the Hebrew word for throat — the passage through which breath and food move. The soul begins as somatic (throat, breath, hunger) and develops organically to denote the whole animated person, not by metaphorical extension but by the unity of breathing, desiring, and living. |
| 182-F002 | THEOLOGICAL_NOTE | R182 Soul | Lev 17:11, Gen 35:18, Num 19:11 | The soul is not an immortal substance lodged within the body — it is the animated body itself. Lev 17:11 identifies the soul with the blood. H5315M (dead soul = corpse) confirms the soul does not vacate a container at death but ceases to animate its flesh. The biblical soul is not Cartesian. |
| 182-F003 | THEOLOGICAL_NOTE | R182 Soul | Gen 1:20, Gen 1:24, Gen 2:7 | The human soul shares its category (ne.phesh cha.yah — living creature) with animals (Gen 1:20,21,24). What distinguishes the human soul is not the noun but the act — the direct divine inbreathing of Gen 2:7. The soul is not uniquely human as a category but is uniquely constituted in the human. |
| 182-F004 | TERM_BEHAVIOUR | R182 Soul | Psa 42:1, Deu 12:20, Ecc 6:7, Isa 5:14 | The soul is constitutively appetitive — it is always reaching toward something. H5315L establishes this as the soul's fundamental structure. The critical question is always the object of craving: the soul that pants for God (Psa 42:1) and the soul that hungers for food (Deu 12:20) are using the same capacity. |
| 182-F005 | VERSE_PATTERN | R182 Soul | Mat 10:39, Mat 16:25, Joh 12:25, Mar 8:35 | The soul-life paradox of the NT: the soul that clings to itself loses itself; the soul that gives itself away finds itself. Mat 10:39 and its parallels structure the soul as both the thing most desperately sought (self-preservation) and the thing that must be released to be truly found. This is the transformation dynamic at the heart of the NT soul vocabulary. |
| 182-F006 | THEOLOGICAL_NOTE | R182 Soul | 1Co 2:14, 1Co 15:44, 1Co 15:45, Jude 19 | G5591 psuchikos establishes the soul without the Spirit as a real condition — the natural creaturely mode of human existence. The soul is not evil in this mode, but incomplete. 1Co 15:45 establishes the eschatological trajectory: the psuchikon (Adamic) is raised as the pneumatikon (Christic). The soul is the beginning of the journey, not its end. |
| 182-F007 | VERSE_PATTERN | R182 Soul | Exo 31:17, Isa 42:1, Jer 32:41, Eze 18:4 | God employs soul-vocabulary for his own inner states: Exo 31:17 (God refreshed — na.phash), Isa 42:1 (God's soul delights), Jer 32:41 (God's whole-soul commitment). Soul-language is the available language for divine inner states analogous to human inner states — not asserting God has a creaturely soul but using soul vocabulary analogically for divine pathos. |
| 182-F008 | TERM_BEHAVIOUR | R182 Soul | Psa 42:5, Psa 42:11, Psa 43:5, Luk 12:19 | The soul's self-address in Psa 42-43 (the psalmist speaks to his own soul, diagnoses it, gives it a counter-command) is the OT's most psychologically sophisticated move. The person who can observe their own soul from outside and command it is more whole, not less — this reflexive capacity is a distinctive feature of the soul vocabulary. |
| 182-F009 | THEOLOGICAL_NOTE | R182 Soul | Heb 4:12, 1Th 5:23 | Heb 4:12 — the Word of God divides soul and spirit as a sword divides joints and marrow. The soul cannot reliably distinguish itself from the spirit by introspection alone. The soul-spirit distinction is real but requires divine speech to make it visible — it is not self-evident to the person. |
| DIM-182-001 | DIMENSION_REVIEW | R182 Soul |  | ne.phesh groups 1381-008 (Servant's soul poured out in self-offering, Isa 53) and 1392-002 (psuchē life laid down in love, Christ for the sheep) together form the atonement-love axis in the soul registry. Both assigned Theological/Divine-Human. Session B: these are the programme's primary soul-and-atonement texts — connect to existing SD flags 182-F005 (Isa 53 atonement) and PH2-182-005 (eschatological soul-substitution). |
| DIM-182-002 | DIMENSION_REVIEW | R182 Soul |  | Identity/Selfhood groups in the Soul registry (1385-001 human as living soul, 1391-001 psuchē as essential inner person, 1396-001/2 psuchikos as natural mode, 1400-001 apsuchos as negation) together define what the soul is constitutively. Session B: these form the ontological foundation of Registry 182 — the soul as a mode of being, not merely a function. |
| DIM-182-003 | DIMENSION_REVIEW | R182 Soul | Pro 27:7 | Soul (#182) carries 1 term with status=phase2_enrichment: H5317 (nophet/honey, 5 active verses). Pro 27:7 — one who is full loathes honey; to one who is hungry everything bitter is sweet — encodes the appetite dimension of nephesh through honey as archetype metaphor. Deliberately excluded from VCB — no verse_context records exist. Active verses remain unflagged by design. Decision carried forward from prior Session B. Session B DataPrep must include this term as contextual support for understanding the soul's appetitive dimension. Verses: Psa 19:10, Pro 5:3, Pro 24:13, Pro 27:7, Song 4:11. |
| DIM-183-001 | DIMENSION_REVIEW | R183 heart |  | qe.rev (H7130H) spans five groups across five dimensions: Theological/Divine-Human (God's indwelling in the midst), Moral/Conscience (seat of moral character; seat of hostile intent; location of false prophets' lies), Theological/Divine-Human (location of new covenant renewal). Session B: the inner parts as the site of both divine indwelling and moral corruption — a structural inner-being tension at the heart of the heart registry. |
| DIM-183-002 | DIMENSIONAL_PATTERN | R183 heart |  | Divine knowledge of the inner person — three-group cluster in r183 plus one in r112. 579-003 le.vav (known by God, 1 Sam 16:7), 598-004 kardia (known by God, multiple NT), 599-001 kardiognōstēs (heart-knower, Acts 1:24/15:8). All Dimension 11 with NONE or GOD dominant. Structural pattern: human heart as object of divine cognitive-searching act. Hebrew and Greek vocabulary naming the same structural relationship. Foundational for any word study of inner-knowledge vocabulary. |
| DIM-183-003 | DIMENSIONAL_PATTERN | R183 heart |  | Covenant-renewal pattern in heart vocabulary — four r183 members of the wider Dimension 11 covenant-renewal cluster. 579-009 le.vav (circumcised/renewed, Deut 30:6), 577-003 qe.rev (new covenant writing in inner parts, Jer 31:33 context), 581-008 lev (covenantal), 602-001 enkainizō (inaugural renewal, Heb 10:20). Together with r112 members 995-003 dianoia and 4413-003 mnaomai, forms an eight-term cluster where divine covenant act operates on the human inner-being. Pattern foundational for any word study of these terms. |
| DIM-183-004 | DIMENSIONAL_PATTERN | R183 heart |  | Somatic-to-figurative continuum in heart/bowel vocabulary. Six r183 groups (577-001 qe.rev midst, 585-001/002 cha.la.tsa.yim loins, 588-001 na.val withering, 590-003 splagchnon body, 1801-003 meim body) carry the somatic-physical sense of the inner organ/region, distinct from affective-moral-cognitive senses. Same roots engage both registers (e.g., splagchnon 590-001/002 affective vs 590-003 physical; meim 1801-001 yearning vs 1801-003 physical). Confirms biblical Hebrew and Greek retain physical-interior meaning alongside figurative inner-being. Word studies should acknowledge embodied register rather than reading all usage as metaphorical. |
| DIM-183-005 | DIMENSIONAL_PATTERN | R183 heart |  | Heart as site of divine indwelling — pattern distinct from divine knowing or covenant-writing. 598-007 kardia (Christ dwelling by faith Eph 3:17; Spirit poured out Rom 5:5; Father's word abiding) names a Dimension 11 structure where divine *presence* is in the human interior. Related to but distinct from 577-003 (covenant writing — act upon heart) and 579-009 (circumcision renewal — act upon heart). Indwelling is continued presence within, not a transformative act. Important distinction for systematic word study. |
| DIM-086-001 | DIMENSION_REVIEW | R086 impurity |  | Group 5574-001 (akathartos — unclean spirit) presents the unclean spirit as an inner occupant whose presence produces inner captivity and whose expulsion by Christ restores inner freedom. Session B should examine this as a model of inner-being occupation and liberation — the inner person as the site of spiritual occupancy — and how this relates to the programme's understanding of the inner being's relationship to spiritual forces. |
| DIM-61-001 | DIMENSION_REVIEW | R061 fear |  | fobeō (G5399) shows a tripartite inner-being structure: (1) theophanic/miraculous fear leading to worship (Spiritual/God-ward), (2) reverential life-shaping fear of God (Spiritual/God-ward), (3) practical self-interested fear before humans or consequences (Affective/Emotional). This tripartite structure is the most analytically important pattern in Registry 61 and should be the organising frame for Session B analysis. |
| DIM-61-002 | DIMENSION_REVIEW | R061 fear |  | ya.re (H3372G) groups add the divine 'Fear not' command (298-001) as a structuring element — showing the divine address to inner fear as a distinct inner-being category. The reassurance pattern (divine declaration of presence + commanded displacement of fear) is significant for understanding how the inner-being state of fear is meant to be transformed. |
| DIM-191-001 | DIMENSION_REVIEW | R191 doubt |  | Group 1286-001 (H2963 ta.raph, tearing) was assigned Emotion — Negative / HUMAN to capture the human experience of violent inner states: wrath, predatory character, destructive anger, and the suffering of being torn. The same group contains significant GOD-dimension content — divine wrath and fierce resolve to fight for his people. Session B should study both dimensions: (1) the human inner-being experience of violent states and of being torn under judgment or hostile power; and (2) the divine inner-being reality of wrath and fierce protective resolve, exploring whether these are the same phenomenon viewed from different subjects or whether they name distinct inner-being realities. |

<a id="s4-2"></a>
### §4.2 SD pointers from contributor registries with no term-level link (39)

| Pointer | Priority | Strong's ref | Description |
|---|---|---|---|
| DIM-35-SD001 | MEDIUM |  | The positive desire vocabulary (prothumia, prothumos, prothumōs) in Reg 35 may have natural affinity with volitional vocabulary elsewhere. The contrast between eager willing (prothumia) and acquisitive desire (pleonexia) in the same registry is analytically significant for understanding how Scripture distinguishes rightly-oriented from wrongly-oriented inner desire. Session D should examine this alongside Reg 70 (greed) and the broader desire vocabulary. |
| DIM-70-SD001 | MEDIUM |  | The greed vocabulary in C13 (pleonexia, pleonektēs, harpagē) shows consistent convergence on Character/Disposition. Session D should examine the relationship between greed (Reg 70), covetousness (Reg 35), and positive desire (prothumia) — the cluster's contrast between rightly- and wrongly-directed inner desire is a synthesis question. |
| DIM-023-SD015 | MEDIUM |  | Rev 3:17 — the pitiable condition (eleeinos) masked by prosperity — connects to Despair (Reg 44), Shame (Reg 146), and potentially Pride/Boastfulness (Reg 123). The verse shows that the inner condition requiring compassion can be concealed from the person who most needs it. This has implications for the programme's understanding of self-knowledge and the conditions under which compassion becomes operative. --- #### Term 20: G1654 eleēmosunē — charity/almsgiving (occ=36, extracted_thin) *Sense structure: The noun naming compassion made concrete in giving. Two groups: group 3167-001 (almsgiving as outward expression of inward mercy disposition). Mounce: "gift to the poor, alms, charitable gift." LSJ traces the semantic development: classical Greek pity/mercy → LXX almsgiving/charitable giving → NT acts of generosity to those in need. The word represents compassion arriving at its outward form — the inner disposition externalised as gift. Semantic observation: The semantic development from pity (classical) to almsgiving (LXX/NT) is significant: it shows how the inner characteristic of compassion was understood in Second Temple Judaism and early Christianity to have a normative outward form. Compassion that does not give alms has not fully arrived. Matt 6:2-4 and Luke 11:41 both address the manner* of almsgiving (not for public display; from inner purity) — establishing that the inner quality of compassion is what gives the outward act its validity. |
| DIM-78-SD001 | MEDIUM |  | The trust/refuge vocabulary of Registry 78 (hope) and the desiderative vocabulary of Registry 43 (desire) share the inner-being ground of orientation toward an object. Session D should examine the relationship between hope/trust and desire/longing as paired inner-being orientations, and how fear/reverence (other clusters) functions as their counterpart. |
| DIM-068-SD005 | HIGH |  | Hope (Reg 78) shared anchor Rom 5:2 (grace group 888-002 ↔ hope group 401-001) and cooccurrence 4 verses: 'we have obtained access by faith into this grace in which we stand, and we rejoice in hope of the glory of God.' Grace and hope co-constitute the same inner standing — the condition of the person who stands in grace and lives forward toward what grace promises. Session D should examine whether grace and hope are structurally linked as co-features of a single inner-being condition, and how the standing-in-grace (present) and rejoicing-in-hope (future-oriented) relate within that condition. |
| 112-SD001 | MEDIUM | G3340 | G3340 metanoeō, G3341 metanoia, G3338 metamellomai, and H5162H na.cham (relent) all present in Reg 112 and Reg 135 (repentance). Structural overlap at intersection of cognitive reorientation and mind-change. |
| 112-SD002 | MEDIUM | H5162G | H5162G na.cham (comfort) likely shared with Reg 071 (grief) and Reg 135. Na.cham root operates across mind-change (112), comfort of the grieving (071), and divine relenting (135). |
| 112-SD003 | MEDIUM | H5068 | H5068 na.dav (willing) likely shared with desire and will registries. Volitional inner movement of na.dav borders desire and will clusters. |
| 112-SD004 | MEDIUM | G4893 | G4893 suneidēsis has no Hebrew counterpart in this registry. Intersection with heart (183) and spirit (184) registries for Session D investigation of conscience as NT/Hellenistic category. |
| 112-SD005 | MEDIUM | H8104G | H8104G sha.mar/obey (195v) has significant overlap with will/obedience registries. Cross-registry boundary review recommended — may belong primarily to a different cluster. |
| 112-SD006 | MEDIUM | G1271 | Heb 8:10 and 10:16 name both dianoia (mind) and kardia (heart) as sites of new covenant law-writing. Structural overlap between Reg 112 and Reg 183. |
| 112-SD007 | MEDIUM | H2142 | H2142 za.khar operates across memory, worship, and ritual domains. Possible overlap with worship or praise registries (1 Chr 16:4 Levitical invoke/remember; Ps 38/70 memorial offering context). |
| 112-SD008 | MEDIUM | G3340 | Spirit-mind distinction in 1 Cor 14:14-15 is the sharpest NT terminological boundary between nous and pneuma. Session D: map against Reg 184 (spirit). |
| 112-SD009 | MEDIUM | H3336 | Ye.tser (formed inclination) in Gen 6:5 and 8:21 is the OT closest equivalent to fundamental moral disposition. Session D: relationship between ye.tser and will cluster. |
| 112-SD010 | MEDIUM | G5426 | 1 Cor 2:16 and Phil 2:5 present mind-orientation as transferable through participation in Christ. Key integration point for transformation of inner being across soul/mind/heart registries. |
| DIM-112-SD001 | MEDIUM |  | C01 Theological/Divine-Human density: 62 of 297 groups (21%) reflect a structural reality — the primary inner-being terms are constitutively relational to God. Session D: the structural vocabulary of the inner being is a theo-relational construct, not a neutral anthropological one. This pattern should be tested against all 22 clusters. |
| DIM-112-SD002 | MEDIUM |  | Absence of Sin & Vice from all six C01 structural registries. The inner-being structural terms (mind, soul, heart, spirit, flesh, being) name the capacity and theatre of sin — not sin itself. Session D: structural vocabulary vs characterological vocabulary as an analytical distinction across the programme. |
| DIM-103-SD021 | MEDIUM | G5384 | Joh 15:15 — friendship with Christ defined by shared knowledge of the Father's purposes. 'I have called you friends, for all that I have heard from my Father I have made known to you.' Love takes the form of disclosure: God's inner purposes made known. Cross-registry: love (103), knowledge/thought (160), mind (112), calling (19). Question: is there a structural link between love and knowledge in the programme — does love require knowing and being known, not merely feeling? |
| DIM-112-SD003 | MEDIUM |  | CHASHAV root family cross-registry structural pattern. Hebrew root chashav spans Reg 112 (mind), Reg 126 (purpose), Reg 160 (thought). Functions split: act of devising/thinking/counting (mind), plan as product (purpose), calculation/explanation (thought). r112 groups predominantly 03 Cognition + 04 Volition. Session D synthesis should test dimensional profile of r126 and r160 groups. |
| DIM-112-SD004 | MEDIUM |  | BOUL root family Greek counterpart to CHASHAV. Spans Reg 32 (counsel) and Reg 112 (mind). bouleuō G1011 (mind) vs boulē G1012, epiboulē G1917, sumboulion G4824, sumboulos G4825 (counsel). Same mental-act/product/relational-noun pattern as CHASHAV. Cross-language CHASHAV/BOUL convergence is a possible structural universal for Hebrew-Greek mental-act vocabulary. |
| DIM-112-SD006 | MEDIUM |  | Spiritual/God-ward vocabulary gap — potential Dimension 12 (DR-13). Phase A identified 25 C01 groups with legacy 'Spiritual/God-ward' label having no clean current-vocabulary counterpart. r112 Phase C resolved these mostly to Dimension 11 (where divine-human correspondence structure was present) or 03/04/06. No r112 group required new dimension. But the label may indicate distinct 'God-ward Orientation' dimension — human's directedness toward God without correspondence structure. 995-001 dianoia 'love God with all your mind' is clearest candidate. Will be more significant for r183 where 581-006 lev God-ward orientation is UNCLASSIFIED. |
| DIM-112-SD007 | MEDIUM |  | False-positive cross-registry roots — CC rootfamily extract pipeline observation. Three of five 'cross-registry' roots for C01 appear to be string-match false positives: AT (root_code None, personal pronouns vs mutterer); YATSA (offspring vs come-out homonym); TAAM (perceive vs be-double homonym). Researcher may wish to refine tool's matching logic to exclude None-root and zero-semantic-overlap pairs. Pipeline observation, not dimension finding. |
| 182-SD001 | MEDIUM | G5591 | G5591 psuchikos establishes soul-spirit boundary from within the soul registry. Structural overlap with spirit registry (184) — the soul without the Spirit is the soul's defining limit. |
| 182-SD002 | MEDIUM | H5315L | H5315L ne.phesh:appetite is a SHARED_TERM with desire registry (043). The soul IS the desiring capacity — ne.phesh and ta.a.vah used in synonymous parallelism in Deu 14:26. |
| 182-SD003 | MEDIUM | G5590H | Mat 10:28 — soul introduced as dimension surviving bodily death in fear context. Soul and fear registries share verse at the intersection of ultimate threat and ultimate protection. |
| 182-SD004 | MEDIUM | H5315G | H5315G ne.phesh connects to grief (071) — soul cast down in lament Psalter; hope (078) — Psa 42:5 soul addressed and commanded to hope; peace (117) — Lam 3:17 soul bereft of peace, Heb 6:19 soul anchored. |
| 182-SD006 | MEDIUM | H5314 | H5314 na.phash in Exo 31:17 — God refreshed after creation. Soul-vocabulary applied to God. Structural observation: soul-language used analogically for divine inner states alongside similar usage in Isa 42:1 and Jer 32:41. |
| 182-SD007 | MEDIUM | G5590G | 1Th 5:23 tripartite statement (spirit, soul, body) and Heb 4:12 (soul-spirit division) are the primary structural cross-registry verses linking soul (182), heart (183), and spirit (184). The soul's place in the triad cannot be fully mapped without all three registries. |
| 182-SD008 | MEDIUM | G5590H | Mat 10:39 soul-loss/soul-finding paradox connects to repentance (135) — the soul's release of self-preservation instinct is structurally related to repentance as cognitive-volitional reorientation. |
| DIM-103-SD004 | HIGH | G5368 | Joh 12:25 — whoever loves his life loses it, whoever hates his life keeps it for eternal life. Agapao/miseo applied to one's own life. Structural intersection of love (103), hatred (75), soul/life (182), surrender/will (156). Question: is this verse's paradox — loving the self leads to loss, hating it leads to eternal life — the programme's clearest statement about how love and self-orientation stand in opposition as inner-being structures? |
| DIM-183-SD001 | MEDIUM |  | Repentance vocabulary spans Registries 112 (na.cham, metanoia, metanoeo, metamellomai), 182 (na.cham soul-level), and 183 (le.vav circumcision/renewal, kardia renewal). Session D: map the full cross-registry repentance network against Registries 135 (repentance) and 134 (renewal). The inner-being act of turning is distributed across all three C01 structural terms. |
| DIM-183-SD002 | MEDIUM |  | God-ward orientation pattern — four groups across three roots and two registries name the characteristic of human inner-being oriented toward God without divine-act structure. 581-006 lev, 579-010 le.vav, 598-008 kardia (all r183), plus 995-001 dianoia (r112 — 'love God with all your mind'). All assigned Dimension 11 under the 'operates across the boundary' clause. Question for Session D: is this genuinely Dimension 11 (cross-boundary operation), or a distinct 'God-ward Orientation' Dimension 12 that current §7.7 does not name? Linked to DIM-112-SD006. The answer determines how Dimension 11's scope is drawn programme-wide. |
| DIM-183-SD003 | MEDIUM |  | Yearning correspondence — meim 1801-001 names divine yearning (Jer 31:20) and human yearning (Song of Songs 5:4) using the same term. Splagchnon in NT has similar divine-human pattern (Luke 1:78 Christ's tender mercy; Phil 1:8 Paul's affection in Christ). Session D question: is yearning a distinct Dimension 11 pattern (parallel to knowing, remembering, reckoning) or does it sit within 06 Relational Disposition with divine-human examples? Empirical question for cross-testament synthesis. |
| DIM-183-SD004 | MEDIUM |  | Somatic-figurative dimensional split within root families — pattern observed at Phase C r183. Multiple roots show dimensional breadth determined by the somatic/figurative distinction: splagchnon (06, 06, 07); meim (06, 02, 07); qe.rev (05, 04, 07, 11, delete_flagged). Pattern raises question: should dimension-assignment rules explicitly address somatic-senses of inner-being vocabulary as a first-order distinction (not subsidiary to semantic sense-splits)? Session D candidate. |
| DIM-183-SD005 | MEDIUM |  | H3820A lev + H3824 le.vav synthesis candidate. lev cluster: 8 sense-splits covering §7.7 dimensions 02, 03, 04, 05, 05, 11, 11, 11. le.vav cluster: 10 senses covering 03, 05, 11, 04, 06, 05, 02, 02, 11, 11. Widest single-term dimensional spreads in C01. Together the two lemmas cover the heart-vocabulary analytical ground. Session D should consider whether these two lemmas warrant synthesis-level treatment as a single analytical unit with two grammatical forms (vs. separate treatment). |
| SP-067-009 | MEDIUM |  | Jos 23:14 ('you know in your hearts and souls, all of you, that not one word has failed of all the good things the Lord your God promised') explicitly names heart and soul as the site of covenantal knowing. God's good word (R67 Group 884-005) is received and registered in the inner being. Session D should examine whether Jos 23:14 establishes a structural link between R67 (goodness) and R183 (heart) / R182 (soul) — specifically whether the reception of covenantal goodness is a heart-and-soul event that connects the goodness and anthropological registries. |
| DIM-61-SD001 | MEDIUM |  | C06 fear cluster shows a tripartite dimension pattern: fear-as-God-ward-orientation (Spiritual/God-ward ~18 groups), fear-as-inner-affect (Affective/Emotional ~37 groups), fear-as-volitional-collapse (Volitional/Will 5 groups). This tripartite structure — orientation, affect, will-collapse — may be a cross-registry finding about how negative inner states operate in biblical anthropology. Session D should examine whether the same pattern appears in other C06 registries and beyond. |
| DIM-33-SD001 | MEDIUM |  | Groups 763-001 and 763-002 (tharseō — divine 'Take heart/be courageous' address) in Reg 33 mirror the 'Fear not' pattern from Reg 61 (ya.re) in C06. The divine address directly to the inner being producing courage where there was fear is a structured biblical motif crossing C06 and C08. Session D should examine the divine courage-address as a cross-cluster pattern: how God's direct speech to the inner being (commanding against fear, commanding toward courage) functions as a distinctive inner-being transformation mechanism. |
| DIM-068-SD050 | LOW |  | Doubt (Reg 191, C16) cooccurrence 3 verses. Doubt is the inner oscillation between trust and distrust. Grace is received through faith (Eph 2:8). For Session D: do the 3 co-occurring verses show grace encountering the doubting person — and if so, does grace precede the resolution of doubt (grace given to the doubter) or follow it (doubt must resolve before grace is received)? Connects to the faith question (SD006) and to Dan 9:23 (grace responding before the plea is complete — SD028). |

<a id="s4-3"></a>
### §4.3 Prose sections from contributor registries (0)

(none)

<a id="s4-4"></a>
### §4.4 Cluster-internal verse_context_group rows (18)

Deduplicated list of all `verse_context_group` rows that appear in this cluster (post-M47: a vcg may be linked to multiple terms via `vcg_term`; the Strong's column is a comma-joined list of all linked terms).

| Group ID | Code | Strong's (linked terms) | Description | Notes |
|---|---|---|---|---|
| 3060 | 1288-001 | G1365 | Term names doubt as the inner experience of wavering — faith faltering between trust and hesitation — addressed directly by Jesus | Revised during Dimension Review Phase B: VCB-022 patch truncated context_description at 80 characters. Full description restored from wa-vcb-022-term-observations-v2.8-20260404.md |
| 1792 | 1398-001 | G1374 | Term names inner division of allegiance — the person whose loyalty is split between God and the world, producing instability |  |
| 2657 | 1403-001 | G3642 | Term names the fainthearted inner state — the soul diminished in courage, needing encouragement from others |  |
| 1014 | 1700-001 | H3512B | Term names the inner condition of being disheartened — the faint, broken, or discouraged state of the inner person under pressure or affliction |  |
| 489 | 2078-001 | G0120 | The inner state of discouragement — loss of heart produced by provocation |  |
| 887 | 259-001 | H1672 | Term names the inner condition of anxiety — the worried, anxious state of the inner person in the face of uncertain or threatening circumstances |  |
| 888 | 259-002 | H1672 | Term names inner sorrow over sin — the grief and contrition of the person who acknowledges wrongdoing |  |
| 222 | 2709-001 | G3309 | Anxious inner preoccupation with material provision, bodily needs, and future security — orientation away from trust toward self-concerned worry |  |
| 223 | 2709-002 | G3309 | Inner state of anticipatory anxiety in the face of threat — worry about what to say or do under pressure |  |
| 224 | 2709-003 | G3309 | Divided or directed inner orientation of care — for the things of God or for worldly matters; also genuine care for others |  |
| 220 | 350-001 | G3308 | Anxious preoccupation with worldly concerns that competes with and displaces inner spiritual receptivity |  |
| 221 | 350-002 | G3308 | Inner burden of care for others carried as expression of relational and pastoral orientation |  |
| 1238 | 394-001 | H2976 | Term names inner despair or hopelessness — the giving up of hope or expectation, whether as a state, a declaration, or the inner capitulation of pursuit |  |
| 1222 | 402-001 | G0560 | Term names the inner disposition of expecting nothing in return — the absence of self-directed hope as the posture of genuine love |  |
| 1306 | 5571-001 | H5074 | Term names wandering or fleeing as an inner experience — restlessness of sleep fleeing, the anguish of spiritual straying, or the inner alienation expressed through wandering |  |
| 2739 | 574-001 | H3512A | Term names the disheartened inner state — the inner being made faint and discouraged by opposition |  |
| 2716 | 603-001 | G1573 | Term names the inner loss of heart — the fading of inner courage and resolve in the face of suffering or opposition |  |
| 660 | 808-001 | G1820 | Term names despair as the complete collapse of inner expectation and hope — the inner being brought beyond what it can sustain, unable to see forward |  |

<a id="s4-5"></a>
### §4.5 Cross-cluster orphan findings/pointers

Findings + SD pointers that mention M-cluster vocabulary but originate from registries that do NOT contribute terms to this cluster — see [wa-cluster-m20-finding-orphans-v1-…](../../../outputs/markdown/) for the full scan.

