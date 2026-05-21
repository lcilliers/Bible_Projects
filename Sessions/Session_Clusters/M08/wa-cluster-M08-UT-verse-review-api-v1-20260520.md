# WA-M08-UT-verse-review-api-v1-20260520

Phase 1 UT review for cluster M08 — Claude API classification of 224 fresh UT verses across 14 terms (only terms with verses lacking verse_context rows).

## Per-term counts

| Strong's | Translit | Gloss | UT | Relevant | Set aside | Borderline |
|---|---|---|---:|---:|---:|---:|
| G0757 | archō | be first | 7 | 0 | 7 | 0 |
| G2744 | kauchaomai | to boast | 1 | 1 | 0 | 0 |
| G5243 | huperēfania | pride | 1 | 1 | 0 | 0 |
| G5308 | hupsēlos | high | 8 | 0 | 8 | 0 |
| H1342 | ga.ah | to rise up | 2 | 0 | 2 | 0 |
| H1346 | ga.a.vah | pride | 3 | 0 | 3 | 0 |
| H1347 | ga.on | pride | 6 | 1 | 5 | 0 |
| H1348 | ge.ut | majesty | 1 | 0 | 1 | 0 |
| H1363 | go.vah | height | 8 | 0 | 6 | 2 |
| H1364 | ga.vo.ah | high | 27 | 0 | 24 | 3 |
| H4791 | ma.rom | height | 20 | 2 | 17 | 1 |
| H6967 | qo.mah | height | 36 | 0 | 36 | 0 |
| H7311A | rum | to exalt | 103 | 7 | 93 | 3 |
| H7830 | sha.chats | pride | 1 | 0 | 1 | 0 |
| **TOTAL** | | | | **12** | **203** | **9** |

## Borderline entries — held for researcher decision (not in patch)

- **H1363 go.vah** vr=186359 Eze 19:11 — The vine's towering height among thick boughs is allegorical for Israel's rulers; the imagery may carry pride connotation but is not explicitly stated as inner arrogance.
  > Eze 19:11 Its strong stems became rulers ’ scepters ; it towered aloft among the thick boughs ; it was seen in its height with the mass of its branches .
- **H1363 go.vah** vr=186361 Eze 31:14 — Trees growing to towering height and setting tops among clouds is metaphor for arrogant self-exaltation judged by God, but the term here may be purely botanical imagery in the allegory.
  > Eze 31:14 All this is in order that no trees by the waters may grow to towering height or set their tops among the clouds , and that no trees that drink water may reach up to them in height . For they are all given over to death , to the world below , among the children of man , with those who go down to the pit .
- **H1364 ga.vo.ah** vr=154168 Isa 10:33 — The lofty/tall imagery in Isa 10:33 may be purely arboreal metaphor for Assyria's literal greatness hewn down, or may carry inner-being pride content; the metaphorical target is ambiguous without clear explicit pride vocabulary.
  > Isa 10:33 Behold , the Lord God of hosts will lop the boughs with terrifying power; the great in height will be hewn down , and the lofty will be brought low .
- **H1364 ga.vo.ah** vr=154162 Eze 17:24 — God bringing low the 'high tree' and raising the 'low tree' may metaphorically encode pride-humbling reversal (M08-adjacent) or may be purely arboreal/national allegory without explicit inner-pride content; ambiguous.
  > Eze 17:24 And all the trees of the field shall know that I am the Lord ; I bring low the high tree , and make high the low tree , dry up the green tree , and make the dry tree flourish . I am the Lord ; I have spoken , and I will do it .”
- **H1364 ga.vo.ah** vr=154164 Eze 31:3 — Assyria as a towering cedar of great height is part of an extended pride-judgment oracle (Eze 31), but this verse describes physical/metaphorical stature rather than explicitly naming inner pride; the pride content emerges in later verses.
  > Eze 31:3 Behold , Assyria was a cedar in Lebanon , with beautiful branches and forest shade , and of towering height , its top among the clouds .
- **H4791 ma.rom** vr=5739 Ecc 10:6 — ma.rom ('high places') likely refers to positions of social/political authority given to folly; could carry pride connotation but primarily denotes status positions, making this ambiguous.
  > Ecc 10:6 folly is set in many high places, and the rich sit in a low place.
- **H7311A rum** vr=186495 Num 33:3 — Israel going out 'triumphantly/with a high hand' could reflect bold confidence/defiance before Egypt; ambiguous between honourable vindication-march and arrogant pride display.
  > Num 33:3 They set out from Rameses in the first month , on the fifteenth day of the first month . On the day after the Passover , the people of Israel went out triumphantly in the sight of all the Egyptians ,
- **H7311A rum** vr=186446 Isa 2:13 — rum describes 'lofty' cedars of Lebanon; in context of Isa 2 these may be symbols of human pride, but the immediate referent is literal trees.
  > Isa 2:13 against all the cedars of Lebanon , lofty and lifted up ; and against all the oaks of Bashan ;
- **H7311A rum** vr=186447 Isa 2:14 — rum describes lofty mountains; in the Isa 2 pride oracle these may symbolize human arrogance, but the direct referent is literal physical elevation.
  > Isa 2:14 against all the lofty mountains , and against all the uplifted hills ;

## Patch

- File: `wa-cluster-M08-patch-vcnew-utreview-api-v1-20260520.json`
- Operations: 215
- Terms covered: 14