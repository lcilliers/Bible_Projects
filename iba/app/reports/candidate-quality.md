# Candidate quality report

> Generated 2026-07-22T19:36:22Z by `candidate.validate`. Read-only findings, not a gate. Covers the stamp (`span_candidate`), the seed decision (`candidate_seed`), and the independent substrate (`lemma_inventory`) — one worklist, not three separate checks.

- `span_candidate.candidate_tag` null: **15036** row(s)
- `candidate_seed.tag` null (candidate rows only): **0** row(s)
- `lemma_key` with no `strong` row: **44198** row(s) across 383 lemma(s)

## Contents

- [span_candidate.candidate_tag (the stamp)](#span-candidatecandidate-tag-the-stamp)
- [candidate_seed.tag (the seed decision — a worklist, not a verdict)](#candidate-seedtag-the-seed-decision-a-worklist-not-a-verdict)
- [lemma_inventory.gloss (the independent substrate)](#lemma-inventorygloss-the-independent-substrate)
- [Lemmas with no strong entry yet (by frequency)](#lemmas-with-no-strong-entry-yet-by-frequency)

## span_candidate.candidate_tag (the stamp)

**33584/70028** row(s) violate `pattern:candidate.tag_clean_pattern`, by category (of the samples shown below): parenthetical 17130, colon (dual-gloss) 7260, other 5700, slash (alt-gloss) 3494

| value | rows |
|---|---:|
| "'God has forgotten, he won't see'" | 4703 |
| 'practice (asah)' | 2475 |
| 'come before (bo)' | 2282 |
| 'walk (halak)' | 1383 |
| 'see (raah)' | 1159 |
| 'enemies speak lies (v11)' | 1069 |
| 'to hear: hear' | 1068 |
| 'dwell in unity (yashab)' | 1007 |
| 'return (shuv)' | 985 |
| 'stretch out the hands (shalach)' | 777 |
| 'eat up / devour (akal - eat up my people)' | 745 |
| 'bad: harmful' | 629 |
| 'to call: call to' | 622 |
| 'lift up (nasa)' | 596 |
| 'make (sim)' | 533 |
| 'to keep: obey' | 449 |
| 'forever: enduring' | 425 |
| 'justice: judgement' | 419 |
| 'suffer (matsa)' | 399 |
| 'to perceive: understand' | 396 |
| 'spirit/breath: spirit' | 379 |
| 'bloodthirsty / men of blood (dam - save me from bloodthirsty men)' | 349 |
| 'I confess my iniquity, I am sorry for my sin' | 335 |
| 'turn aside (sur, negated)' | 289 |
| 'to strengthen: strengthen' | 285 |
| 'face: anger' | 263 |
| 'strength: soldiers' | 244 |
| 'to trust (in)' | 243 |
| 'iniquity: crime' | 229 |
| 'the law in his heart, steps not slipping' | 218 |
| 'to will/desire' | 206 |
| 'turn aside (natah)' | 205 |
| 'forsake (azab)' | 204 |
| 'defend / judge for (shaphat - may he defend the cause of the poor)' | 197 |
| 'to love: lover' | 197 |
| 'pass away (kalah)' | 187 |
| 'extol (rum)' | 184 |
| 'prevail (yakol, negated)' | 172 |
| 'to consecrate: consecate' | 170 |
| 'fight / attack (lacham - many attack me)' | 168 |
| 'swear (shaba)' | 167 |
| 'pray (shaal)' | 160 |
| 'kill (harag)' | 151 |
| 'to call: call' | 147 |
| 'voice/sound: voice' | 140 |
| 'declare (saphar)' | 138 |
| 'pursue (radaph)' | 138 |
| 'profane / violate (chalal - he violated his covenant)' | 134 |
| 'sacrifice (zabach)' | 132 |
| 'be at rest / settle (shakan - and be at rest)' | 121 |
| 'cast / throw (shalak - cast your burden on the LORD)' | 121 |
| 'truth: faithful' | 121 |
| 'upright:right' | 119 |
| 'to devise: design' | 118 |
| 'pour out (shaphak)' | 112 |
| 'to honor: honour' | 110 |
| 'to plead/comfort' | 109 |
| 'be weak: weak' | 107 |
| 'to redeem: redeem' | 102 |
| 'to be sorry: comfort' | 99 |
| 'run (ruts)' | 91 |
| 'unfeeling (tapash)' | 90 |
| 'stir up strife / band together (gur - they stir up strife)' | 85 |
| 'learn (lamad)' | 84 |
| 'hide oneself (sathar - then I could hide from him)' | 79 |
| 'plan / take counsel (yaats - they only plan to thrust him down)' | 79 |
| 'be estranged / alienated (zur - estranged from the womb)' | 77 |
| 'be hurt (anah)' | 77 |
| 'evil/bad' | 77 |
| 'evil: wickedness' | 77 |
| 'curse (qalal)' | 76 |
| 'abide (lun)' | 75 |
| 'man is a mere breath, a shadow' | 73 |
| 'set (shith)' | 73 |
| 'to plow/plot' | 70 |
| 'see (nabat)' | 66 |
| 'observe (natsar)' | 63 |
| 'will/desire' | 62 |
| 'seize (achaz)' | 61 |
| 'do no wrong (paal)' | 57 |
| 'to see/experience' | 57 |
| 'to twist: tremble' | 57 |
| "flee (barach) God's presence" | 56 |
| 'behold your face, satisfied with your likeness' | 55 |
| 'hold dear (ratsah)' | 55 |
| 'be afflicted (tsarar)' | 54 |
| 'shout (ranan)' | 54 |
| 'vain (shav)' | 53 |
| 'cling (dabaq)' | 50 |
| 'evil/harm: evil' | 50 |
| 'lean / be sustained (samak - upon you I have leaned from before my birth)' | 47 |
| 'murder (ratsach)' | 47 |
| 'refrain from anger, forsake wrath' | 46 |
| 'guilt [offering]' | 45 |
| 'to serve/heal' | 43 |
| 'to praise/bless' | 42 |
| 'lie in wait / ambush (arab - they lie in wait for my life)' | 41 |
| 'haughty (gaboah)' | 40 |
| 'to wait: wait' | 40 |
| 'horror: destroyed' | 39 |
| 'I am a worm, not a man' | 38 |
| 'to call to/summon' | 38 |
| 'laugh / deride (sachaq - laugh at him)' | 36 |
| 'word (millah) before the tongue' | 36 |
| 'deliverance: salvation' | 34 |
| 'hope / expectation (tiqvah - my hope is from him)' | 34 |
| 'moan / murmur (hamah - and moan)' | 34 |
| 'store up (tsaphan)' | 32 |
| 'hide (kachad, refused)' | 31 |
| 'to call (on)/name' | 31 |
| 'to hope/expect' | 31 |
| 'to shine/appear' | 31 |
| 'quiet (damam)' | 30 |
| 'vow (nadar)' | 29 |
| 'noble: willing' | 28 |
| 'secret sins (alum)' | 28 |
| 'accuser (satan)' | 27 |
| 'conceives evil, births lies' | 27 |
| 'ascribe glory, worship in holiness' | 26 |
| 'be weary/toil' | 26 |
| 'come (qadam)' | 26 |
| 'flatter / deceive (pathah)' | 26 |
| 'fool[ish]' | 26 |
| 'number (manah)' | 26 |
| 'offer freely (nedabah)' | 26 |
| 'consecration: Nazirite vow' | 25 |
| 'I told the glad news, I did not restrain my lips' | 24 |
| 'fly away (uph - I would fly away)' | 24 |
| 'weakness: weak' | 24 |
| 'wrongdoings (alilah)' | 24 |
| 'awake (qits) still with God' | 22 |
| 'knees (berek)' | 22 |
| 'belly/womb/stomach' | 21 |
| 'search out (chaphas - a diligent search)' | 21 |
| 'temptation/testing: temptation' | 21 |
| 'wander (shagah, negated)' | 21 |
| "'with our tongue we will prevail'" | 20 |
| 'arrogant (rachab)' | 20 |
| 'judge / govern (din - may he judge your people with righteousness)' | 20 |
| 'mix (arab)' | 20 |
| 'proud (yonah/gaayon)' | 20 |
| 'hasten (chush)' | 19 |
| 'oppress (lachats)' | 19 |
| 'to judge/doubt' | 19 |
| 'bring / present (yabal - let all bring gifts)' | 17 |
| 'commit iniquity (avah)' | 17 |
| 'lowly (shaphal)' | 17 |
| 'to remain/endure' | 17 |
| 'laughter (sechoq)' | 15 |
| 'robber/rebel' | 15 |
| 'exchange (mur)' | 14 |
| 'to know/understand' | 14 |
| 'turn back / fall away (sug - they have all fallen away)' | 14 |
| 'foolish confidence / folly (kesel)' | 13 |
| 'long/distant' | 13 |
| 'look away, that I may smile again' | 13 |
| 'no usury, no bribe' | 12 |
| 'to say: will say' | 12 |
| 'affection/entrails' | 11 |
| 'glory (shabach)' | 11 |
| 'perverse (iqqesh)' | 11 |
| 'pour forth fame + sing' | 11 |
| 'precious (yaqar) esteeming' | 11 |
| 'change (chaliphah - they do not change)' | 10 |
| 'distribute freely (pazar)' | 10 |
| 'to die/be dead' | 10 |
| 'to give/deliver' | 10 |
| 'barren woman (aqar)' | 9 |
| 'delight (shaashua/shaa/sus)' | 9 |
| 'like a deaf, mute man I do not answer' | 9 |
| 'war / conflict (qerab - war was in his heart)' | 9 |
| 'I was mute, and my distress grew worse' | 8 |
| 'band together (gadad)' | 8 |
| 'be astounded / amazed (tamah)' | 8 |
| 'be embittered / soured (chamets - when my soul was embittered)' | 8 |
| 'counsel/council' | 8 |
| 'hope (yachal/sabar)' | 8 |
| 'image/mark' | 8 |
| 'to cut/mourn' | 8 |
| 'delay (mahah, negated)' | 7 |
| 'good/kind' | 7 |
| 'murmur (ragan)' | 7 |
| 'to bow/lay down' | 7 |
| 'to pray/wish for' | 7 |
| 'voice: sound' | 7 |
| 'Jealous [God]' | 6 |
| 'accusers (satan)' | 6 |
| 'ark: covenant' | 6 |
| 'longing (shaqaq)' | 6 |
| 'mind/thought' | 6 |
| 'to ponder/confer' | 6 |
| 'a question/dispute' | 5 |
| 'be false / deal falsely (shaqar - to your covenant, negated)' | 5 |
| 'confidence/essence' | 5 |
| 'moan / be in commotion (hum - I moan)' | 5 |
| 'to know/choose' | 5 |
| 'go astray (shagag)' | 4 |
| 'open the mouth (paar)' | 4 |
| 'speak rashly (bata)' | 4 |
| 'to bend/bow' | 4 |
| 'to curse/revile' | 4 |
| 'to do evil/harm' | 4 |
| 'wait in silence / be still (dumiyyah - my soul waits in silence)' | 4 |
| 'a vow/prayer' | 3 |
| 'be restless / roam in distress (rud - I am restless)' | 3 |
| 'melt away (dalaph)' | 3 |
| 'my soul bereft, repaid evil for good' | 3 |
| 'rejected/fleeting' | 3 |
| 'be weary/sick: weak' | 2 |
| 'low estate (shephel)' | 2 |
| 'thought/purpose' | 2 |
| 'to call/choose' | 2 |
| 'to lavish/despise' | 2 |
| 'to provoke/irritate' | 2 |
| 'to rest/rely on' | 2 |
| '`Terror on Every Side`' | 1 |
| '`valor`' | 1 |
| 'be in despair / be sick (anash - I am in despair)' | 1 |
| 'courage/confidence' | 1 |
| 'destitute (arar)' | 1 |
| 'double-minded (seeph)' | 1 |
| 'helpless (pun)' | 1 |
| 'to sit near/serve' | 1 |
| 'tossings / restless wanderings (nod - my tossings)' | 1 |

## candidate_seed.tag (the seed decision — a worklist, not a verdict)

**225/1733** row(s) violate `pattern:candidate.tag_clean_pattern`, by category (of the samples shown below): parenthetical 88, slash (alt-gloss) 78, colon (dual-gloss) 37, other 22

| value | rows |
|---|---:|
| 'be weak: weak' | 2 |
| 'to call to/summon' | 2 |
| "'God has forgotten, he won't see'" | 1 |
| "'with our tongue we will prevail'" | 1 |
| 'I am a worm, not a man' | 1 |
| 'I confess my iniquity, I am sorry for my sin' | 1 |
| 'I told the glad news, I did not restrain my lips' | 1 |
| 'I was mute, and my distress grew worse' | 1 |
| 'Jealous [God]' | 1 |
| '`Terror on Every Side`' | 1 |
| '`valor`' | 1 |
| 'a question/dispute' | 1 |
| 'a vow/prayer' | 1 |
| 'abide (lun)' | 1 |
| 'accuser (satan)' | 1 |
| 'accusers (satan)' | 1 |
| 'affection/entrails' | 1 |
| 'ark: covenant' | 1 |
| 'arrogant (rachab)' | 1 |
| 'ascribe glory, worship in holiness' | 1 |
| 'awake (qits) still with God' | 1 |
| 'bad: harmful' | 1 |
| 'band together (gadad)' | 1 |
| 'barren woman (aqar)' | 1 |
| 'be afflicted (tsarar)' | 1 |
| 'be astounded / amazed (tamah)' | 1 |
| 'be at rest / settle (shakan - and be at rest)' | 1 |
| 'be embittered / soured (chamets - when my soul was embittered)' | 1 |
| 'be estranged / alienated (zur - estranged from the womb)' | 1 |
| 'be false / deal falsely (shaqar - to your covenant, negated)' | 1 |
| 'be hurt (anah)' | 1 |
| 'be in despair / be sick (anash - I am in despair)' | 1 |
| 'be restless / roam in distress (rud - I am restless)' | 1 |
| 'be weary/sick: weak' | 1 |
| 'be weary/toil' | 1 |
| 'behold your face, satisfied with your likeness' | 1 |
| 'belly/womb/stomach' | 1 |
| 'bloodthirsty / men of blood (dam - save me from bloodthirsty men)' | 1 |
| 'bring / present (yabal - let all bring gifts)' | 1 |
| 'cast / throw (shalak - cast your burden on the LORD)' | 1 |
| 'change (chaliphah - they do not change)' | 1 |
| 'cling (dabaq)' | 1 |
| 'come (qadam)' | 1 |
| 'come before (bo)' | 1 |
| 'commit iniquity (avah)' | 1 |
| 'conceives evil, births lies' | 1 |
| 'confidence/essence' | 1 |
| 'consecration: Nazirite vow' | 1 |
| 'counsel/council' | 1 |
| 'courage/confidence' | 1 |
| 'curse (qalal)' | 1 |
| 'declare (saphar)' | 1 |
| 'defend / judge for (shaphat - may he defend the cause of the poor)' | 1 |
| 'delay (mahah, negated)' | 1 |
| 'delight (shaashua/shaa/sus)' | 1 |
| 'deliverance: salvation' | 1 |
| 'destitute (arar)' | 1 |
| 'distribute freely (pazar)' | 1 |
| 'do no wrong (paal)' | 1 |
| 'double-minded (seeph)' | 1 |
| 'dwell in unity (yashab)' | 1 |
| 'eat up / devour (akal - eat up my people)' | 1 |
| 'enemies speak lies (v11)' | 1 |
| 'evil/bad' | 1 |
| 'evil/harm: evil' | 1 |
| 'evil: wickedness' | 1 |
| 'exchange (mur)' | 1 |
| 'extol (rum)' | 1 |
| 'face: anger' | 1 |
| 'fight / attack (lacham - many attack me)' | 1 |
| 'flatter / deceive (pathah)' | 1 |
| "flee (barach) God's presence" | 1 |
| 'fly away (uph - I would fly away)' | 1 |
| 'fool[ish]' | 1 |
| 'foolish confidence / folly (kesel)' | 1 |
| 'forever: enduring' | 1 |
| 'forsake (azab)' | 1 |
| 'glory (shabach)' | 1 |
| 'go astray (shagag)' | 1 |
| 'good/kind' | 1 |
| 'guilt [offering]' | 1 |
| 'hasten (chush)' | 1 |
| 'haughty (gaboah)' | 1 |
| 'helpless (pun)' | 1 |
| 'hide (kachad, refused)' | 1 |
| 'hide oneself (sathar - then I could hide from him)' | 1 |
| 'hold dear (ratsah)' | 1 |
| 'hope (yachal/sabar)' | 1 |
| 'hope / expectation (tiqvah - my hope is from him)' | 1 |
| 'horror: destroyed' | 1 |
| 'image/mark' | 1 |
| 'iniquity: crime' | 1 |
| 'judge / govern (din - may he judge your people with righteousness)' | 1 |
| 'justice: judgement' | 1 |
| 'kill (harag)' | 1 |
| 'knees (berek)' | 1 |
| 'laugh / deride (sachaq - laugh at him)' | 1 |
| 'laughter (sechoq)' | 1 |
| 'lean / be sustained (samak - upon you I have leaned from before my birth)' | 1 |
| 'learn (lamad)' | 1 |
| 'lie in wait / ambush (arab - they lie in wait for my life)' | 1 |
| 'lift up (nasa)' | 1 |
| 'like a deaf, mute man I do not answer' | 1 |
| 'long/distant' | 1 |
| 'longing (shaqaq)' | 1 |
| 'look away, that I may smile again' | 1 |
| 'low estate (shephel)' | 1 |
| 'lowly (shaphal)' | 1 |
| 'make (sim)' | 1 |
| 'man is a mere breath, a shadow' | 1 |
| 'melt away (dalaph)' | 1 |
| 'mind/thought' | 1 |
| 'mix (arab)' | 1 |
| 'moan / be in commotion (hum - I moan)' | 1 |
| 'moan / murmur (hamah - and moan)' | 1 |
| 'murder (ratsach)' | 1 |
| 'murmur (ragan)' | 1 |
| 'my soul bereft, repaid evil for good' | 1 |
| 'no usury, no bribe' | 1 |
| 'noble: willing' | 1 |
| 'number (manah)' | 1 |
| 'observe (natsar)' | 1 |
| 'offer freely (nedabah)' | 1 |
| 'open the mouth (paar)' | 1 |
| 'oppress (lachats)' | 1 |
| 'pass away (kalah)' | 1 |
| 'perverse (iqqesh)' | 1 |
| 'plan / take counsel (yaats - they only plan to thrust him down)' | 1 |
| 'pour forth fame + sing' | 1 |
| 'pour out (shaphak)' | 1 |
| 'practice (asah)' | 1 |
| 'pray (shaal)' | 1 |
| 'precious (yaqar) esteeming' | 1 |
| 'prevail (yakol, negated)' | 1 |
| 'profane / violate (chalal - he violated his covenant)' | 1 |
| 'proud (yonah/gaayon)' | 1 |
| 'pursue (radaph)' | 1 |
| 'quiet (damam)' | 1 |
| 'refrain from anger, forsake wrath' | 1 |
| 'rejected/fleeting' | 1 |
| 'return (shuv)' | 1 |
| 'robber/rebel' | 1 |
| 'run (ruts)' | 1 |
| 'sacrifice (zabach)' | 1 |
| 'search out (chaphas - a diligent search)' | 1 |
| 'secret sins (alum)' | 1 |
| 'see (nabat)' | 1 |
| 'see (raah)' | 1 |
| 'seize (achaz)' | 1 |
| 'set (shith)' | 1 |
| 'shout (ranan)' | 1 |
| 'speak rashly (bata)' | 1 |
| 'spirit/breath: spirit' | 1 |
| 'stir up strife / band together (gur - they stir up strife)' | 1 |
| 'store up (tsaphan)' | 1 |
| 'strength: soldiers' | 1 |
| 'stretch out the hands (shalach)' | 1 |
| 'suffer (matsa)' | 1 |
| 'swear (shaba)' | 1 |
| 'temptation/testing: temptation' | 1 |
| 'the law in his heart, steps not slipping' | 1 |
| 'thought/purpose' | 1 |
| 'to be sorry: comfort' | 1 |
| 'to bend/bow' | 1 |
| 'to bow/lay down' | 1 |
| 'to call (on)/name' | 1 |
| 'to call/choose' | 1 |
| 'to call: call' | 1 |
| 'to call: call to' | 1 |
| 'to consecrate: consecate' | 1 |
| 'to curse/revile' | 1 |
| 'to cut/mourn' | 1 |
| 'to devise: design' | 1 |
| 'to die/be dead' | 1 |
| 'to do evil/harm' | 1 |
| 'to give/deliver' | 1 |
| 'to honor: honour' | 1 |
| 'to hope/expect' | 1 |
| 'to judge/doubt' | 1 |
| 'to keep: obey' | 1 |
| 'to know/choose' | 1 |
| 'to know/understand' | 1 |
| 'to lavish/despise' | 1 |
| 'to love: lover' | 1 |
| 'to perceive: understand' | 1 |
| 'to plead/comfort' | 1 |
| 'to plow/plot' | 1 |
| 'to ponder/confer' | 1 |
| 'to praise/bless' | 1 |
| 'to pray/wish for' | 1 |
| 'to provoke/irritate' | 1 |
| 'to redeem: redeem' | 1 |
| 'to remain/endure' | 1 |
| 'to rest/rely on' | 1 |
| 'to say: will say' | 1 |
| 'to see/experience' | 1 |
| 'to serve/heal' | 1 |
| 'to shine/appear' | 1 |
| 'to sit near/serve' | 1 |
| 'to strengthen: strengthen' | 1 |
| 'to trust (in)' | 1 |
| 'to twist: tremble' | 1 |
| 'to wait: wait' | 1 |
| 'to will/desire' | 1 |
| 'tossings / restless wanderings (nod - my tossings)' | 1 |
| 'truth: faithful' | 1 |
| 'turn aside (natah)' | 1 |
| 'turn aside (sur, negated)' | 1 |
| 'turn back / fall away (sug - they have all fallen away)' | 1 |
| 'unfeeling (tapash)' | 1 |
| 'upright:right' | 1 |
| 'vain (shav)' | 1 |
| 'voice/sound: voice' | 1 |
| 'voice: sound' | 1 |
| 'vow (nadar)' | 1 |
| 'wait in silence / be still (dumiyyah - my soul waits in silence)' | 1 |
| 'walk (halak)' | 1 |
| 'wander (shagah, negated)' | 1 |
| 'war / conflict (qerab - war was in his heart)' | 1 |
| 'weakness: weak' | 1 |
| 'will/desire' | 1 |
| 'word (millah) before the tongue' | 1 |
| 'wrongdoings (alilah)' | 1 |

## lemma_inventory.gloss (the independent substrate)

**494/11421** row(s) violate `pattern:candidate.tag_clean_pattern`, by category (of the samples shown below): slash (alt-gloss) 237, colon (dual-gloss) 144, other 98, parenthetical 15

| value | rows |
|---|---:|
| 'Most High [God]' | 3 |
| 'to set: make' | 3 |
| 'be weak: weak' | 2 |
| 'he/she/it' | 2 |
| 'servant/slave' | 2 |
| 'to call to/summon' | 2 |
| 'to give: give' | 2 |
| 'to pour: pour' | 2 |
| 'to return: return' | 2 |
| 'what?' | 2 |
| 'who?' | 2 |
| ' Appius' | 1 |
| ' Havens' | 1 |
| ' Portico' | 1 |
| ' Taverns' | 1 |
| '(Mount) Sinai' | 1 |
| '(Sea of) Tiberias' | 1 |
| 'Almighty [God]' | 1 |
| 'Baal [used for God]' | 1 |
| 'Banner [God]' | 1 |
| 'Caesarea [Philippi]' | 1 |
| 'Come, Lord!' | 1 |
| 'Corner [Gate]' | 1 |
| 'Dung [Gate]' | 1 |
| 'East [Gate]' | 1 |
| 'Fish [Gate]' | 1 |
| 'Garden [of Uzza]' | 1 |
| 'Gibeath-[elohim]' | 1 |
| 'Greek, Gentile' | 1 |
| 'Hall [of pillars]' | 1 |
| 'Hamon-gog [Valley]' | 1 |
| 'Jabesh [Gilead]' | 1 |
| 'Jealous [God]' | 1 |
| 'Lord [God]' | 1 |
| 'Lower [Beth Horon]' | 1 |
| 'Muster [Gate]' | 1 |
| 'New [Gate]' | 1 |
| 'Pit: hell' | 1 |
| 'Potsherd [Gate]' | 1 |
| 'Queen [of Sheba]' | 1 |
| 'Red (Sea)' | 1 |
| 'Red [Sea]' | 1 |
| 'Rocks [of Goats]' | 1 |
| 'Salt [Sea]' | 1 |
| 'Second [Quarter]' | 1 |
| "Serpent's [Stone]" | 1 |
| 'Valley [of Achor]' | 1 |
| 'Valley [of Jericho]' | 1 |
| 'YHWH/God' | 1 |
| '[Ben]jaminite' | 1 |
| '[Brook of] Willows' | 1 |
| '[City of] Destruction' | 1 |
| "[Diviners'] Oak" | 1 |
| '[Gate of the] Foundation' | 1 |
| '[Gate of the] Guard' | 1 |
| '[Gate of] Yeshanah' | 1 |
| '[Gilgal]-haaraloth' | 1 |
| '[Hananel] Tower' | 1 |
| '[Leb]-kamai' | 1 |
| '[Mount of] Olives' | 1 |
| '[Mount] Baal-hermon' | 1 |
| '[Mount] Baalah' | 1 |
| '[Mount] Gerizim' | 1 |
| '[Mount] Halak' | 1 |
| '[Mount] Hermon' | 1 |
| '[Mount] Hor' | 1 |
| '[Mount] Mizar' | 1 |
| '[Mount] Moriah' | 1 |
| '[Mount] Perazim' | 1 |
| '[Mount] Tabor' | 1 |
| '[Mount] Zalmon' | 1 |
| '[Muth-]labben' | 1 |
| '[Sea of] Chinnereth' | 1 |
| '[Shelah] Pool' | 1 |
| '[Tophet of] Baca' | 1 |
| '[Topheth of] Hinnom' | 1 |
| '[Topheth of] Slaughter' | 1 |
| '[Tower of] Hananel' | 1 |
| '[Tower of] the Hundred' | 1 |
| '[Tower of] the Ovens' | 1 |
| '[Valley of] Achor' | 1 |
| '[Valley of] Aven' | 1 |
| '[Valley of] Iphtahel' | 1 |
| '[Valley of] Sorek' | 1 |
| '`Terror on Every Side`' | 1 |
| '`great`' | 1 |
| '`steward`' | 1 |
| '`tribute`' | 1 |
| '`valor`' | 1 |
| '`wielded`' | 1 |
| '`worn out`' | 1 |
| 'a question/dispute' | 1 |
| 'a vow/prayer' | 1 |
| 'a yoke/pair' | 1 |
| 'about/through/for' | 1 |
| 'above/for' | 1 |
| 'adoption (as son)' | 1 |
| 'affection/entrails' | 1 |
| 'age/height' | 1 |
| 'alone: pole' | 1 |
| 'an age: age' | 1 |
| 'ancient/taken' | 1 |
| 'another’s' | 1 |
| 'appearance/vision' | 1 |
| 'ark: covenant' | 1 |
| 'article/utensil' | 1 |
| 'as/when' | 1 |
| 'attire/behaviour' | 1 |
| 'back/rim/brow' | 1 |
| 'bad: harmful' | 1 |
| 'bag/price' | 1 |
| 'baked [food]' | 1 |
| 'be (fiery) red' | 1 |
| 'be desolate: destroyed' | 1 |
| 'be devoted/empty' | 1 |
| 'be quiet/give up' | 1 |
| 'be weary/sick: weak' | 1 |
| 'be weary/toil' | 1 |
| 'belly/womb/stomach' | 1 |
| 'belly: abdomen' | 1 |
| 'belt/sash/girdle' | 1 |
| 'bond(age)' | 1 |
| 'border: boundary' | 1 |
| 'bosom: embrace' | 1 |
| 'brother: male-sibling' | 1 |
| 'burial (place)' | 1 |
| 'cause/charge' | 1 |
| 'citadel: palace' | 1 |
| 'common: unsanctified' | 1 |
| 'commotion/plot' | 1 |
| 'confidence/essence' | 1 |
| 'consecration: Nazirite vow' | 1 |
| 'copper/bronze/coin' | 1 |
| 'counsel/council' | 1 |
| 'courage/confidence' | 1 |
| 'course/wheel' | 1 |
| 'court/lawsuit' | 1 |
| 'cubit/hour' | 1 |
| 'cutting/separation' | 1 |
| 'damage/loss' | 1 |
| 'daughter-in-law: bride' | 1 |
| 'deaf/mute' | 1 |
| 'deed: work' | 1 |
| 'deliverance: salvation' | 1 |
| 'diadem/doom' | 1 |
| 'dried up/withered' | 1 |
| 'earth: planet' | 1 |
| 'earth: soil' | 1 |
| 'elder: Elder' | 1 |
| 'entrails: among' | 1 |
| 'evil/bad' | 1 |
| 'evil/harm: evil' | 1 |
| 'evil: wickedness' | 1 |
| 'face: anger' | 1 |
| 'face: before' | 1 |
| 'family: descendant' | 1 |
| 'far (away)' | 1 |
| 'first: beginning' | 1 |
| 'fool[ish]' | 1 |
| 'forever: enduring' | 1 |
| 'free/freedom' | 1 |
| 'friendly/friend' | 1 |
| 'from above/again' | 1 |
| 'furnace/oven' | 1 |
| 'goal/tax' | 1 |
| 'good/kind' | 1 |
| 'great: large' | 1 |
| 'guest room/inn' | 1 |
| 'guide/leader' | 1 |
| 'guilt [offering]' | 1 |
| 'habit/practice' | 1 |
| 'hell: Gehenna' | 1 |
| 'hell: Hades' | 1 |
| 'hell: Sheol' | 1 |
| 'hell: Tartarus' | 1 |
| 'here/thus' | 1 |
| 'horror: destroyed' | 1 |
| 'house: home' | 1 |
| 'how much/many?' | 1 |
| 'how often!' | 1 |
| 'image/mark' | 1 |
| 'implanted/ingrafted' | 1 |
| 'in/inner/inwardly' | 1 |
| 'in/on/among' | 1 |
| 'in/to this place' | 1 |
| 'iniquity: crime' | 1 |
| 'it/s/he' | 1 |
| 'jubilee/horn' | 1 |
| 'just as/how much' | 1 |
| 'justice: judgement' | 1 |
| 'labour[er]' | 1 |
| 'land: country/planet' | 1 |
| 'land: soil' | 1 |
| 'last/least' | 1 |
| 'late (rain)' | 1 |
| 'left/south' | 1 |
| 'less/worse' | 1 |
| 'let him/it be' | 1 |
| 'lifetime/world' | 1 |
| 'linen/wick' | 1 |
| 'little/few' | 1 |
| 'long/distant' | 1 |
| 'lord: God' | 1 |
| 'mark/example' | 1 |
| 'meddlesome/magic' | 1 |
| 'meeting: time appointed' | 1 |
| 'mighty: ox' | 1 |
| 'mind/thought' | 1 |
| 'mountain: mount' | 1 |
| 'nail/claw' | 1 |
| 'near/neighbor' | 1 |
| 'ninth (hour)' | 1 |
| 'noble: willing' | 1 |
| 'of one’s household' | 1 |
| 'offer: to burn' | 1 |
| 'officer/magistrate' | 1 |
| 'ointment pot/seasoning' | 1 |
| 'old: elder' | 1 |
| 'once/at once' | 1 |
| "one's own/private" | 1 |
| 'open!' | 1 |
| 'palace/courtyard' | 1 |
| 'parent/ancestor' | 1 |
| 'plague/blow/wound' | 1 |
| 'plot/ambush' | 1 |
| 'poison/rust' | 1 |
| 'prison/watch: prison' | 1 |
| 'propitious/gracious' | 1 |
| 'rain/teacher' | 1 |
| 'reed/stick/pen' | 1 |
| 'rejected/fleeting' | 1 |
| 'removal/change' | 1 |
| 'robber/rebel' | 1 |
| 'scroll: document' | 1 |
| 'seed: offspring' | 1 |
| 'sharp/swift' | 1 |
| 'side: beside' | 1 |
| 'sign: miraculous' | 1 |
| 'silver: money' | 1 |
| 'single/height' | 1 |
| 'slain: killed' | 1 |
| 'soft/effeminate' | 1 |
| 'son: child' | 1 |
| 'son: descendant/people' | 1 |
| 'spirit/breath: spirit' | 1 |
| 'statute: decree' | 1 |
| 'straw/stubble' | 1 |
| 'street/plaza' | 1 |
| 'strength: soldiers' | 1 |
| 'temptation/testing: temptation' | 1 |
| 'the Lord’s' | 1 |
| 'the/this/who' | 1 |
| 'they [fem.]' | 1 |
| 'they [masc.]' | 1 |
| 'this/these' | 1 |
| 'thought/purpose' | 1 |
| 'through/because of' | 1 |
| 'thumb/big toe' | 1 |
| 'thus(-ly)' | 1 |
| 'time/right time' | 1 |
| 'to abide in/by' | 1 |
| 'to add (to)' | 1 |
| 'to add: again' | 1 |
| 'to appoint/conduct' | 1 |
| 'to approach: approach' | 1 |
| 'to arrest/catch' | 1 |
| 'to arrive/invade' | 1 |
| 'to ascend: rise' | 1 |
| 'to ask/beg' | 1 |
| 'to awaken/rouse' | 1 |
| 'to be sorry: comfort' | 1 |
| 'to be/bear firstborn' | 1 |
| 'to bear/lead' | 1 |
| 'to bend [down]' | 1 |
| 'to bend/bow' | 1 |
| 'to bow/lay down' | 1 |
| 'to break up/open' | 1 |
| 'to bring/be repaid' | 1 |
| 'to bring/carry out' | 1 |
| 'to build up/upon' | 1 |
| 'to burn/pursue' | 1 |
| 'to burn: burn' | 1 |
| 'to burst/come out' | 1 |
| 'to call (on)/name' | 1 |
| 'to call/choose' | 1 |
| 'to call: call' | 1 |
| 'to call: call to' | 1 |
| 'to carry (around)' | 1 |
| 'to collect/crowd' | 1 |
| 'to come [in]: come' | 1 |
| 'to come near/agree' | 1 |
| 'to come out: come' | 1 |
| 'to come/be present' | 1 |
| 'to come/go' | 1 |
| 'to come/go down' | 1 |
| 'to confess/profess' | 1 |
| 'to consecrate: consecate' | 1 |
| 'to continue in/with' | 1 |
| 'to curse/revile' | 1 |
| 'to cut down/off' | 1 |
| 'to cut/mourn' | 1 |
| 'to cut: cut' | 1 |
| 'to demand/ask for' | 1 |
| 'to destroy/lodge' | 1 |
| 'to devise: design' | 1 |
| 'to devote/destroy' | 1 |
| 'to die/be dead' | 1 |
| 'to die/destroy with' | 1 |
| 'to dig through/out' | 1 |
| 'to dislocate/hang' | 1 |
| 'to do evil/harm' | 1 |
| 'to do/make: do' | 1 |
| 'to do/require' | 1 |
| 'to drag out/away' | 1 |
| 'to drag/chew/saw' | 1 |
| 'to draw [up/out]' | 1 |
| 'to draw/persuade' | 1 |
| 'to drip/prophesy' | 1 |
| 'to drive out: drive out' | 1 |
| 'to dwell in/with' | 1 |
| 'to encounter: meet' | 1 |
| 'to end: finish' | 1 |
| 'to entangle/involve' | 1 |
| 'to establish: prepare' | 1 |
| 'to explain/expose' | 1 |
| 'to fall/beat' | 1 |
| 'to fall/press upon' | 1 |
| 'to fall: fall' | 1 |
| 'to feed/dole out' | 1 |
| 'to find/meet' | 1 |
| 'to finish/furnish' | 1 |
| 'to flow: flowing' | 1 |
| 'to foresee/plan' | 1 |
| 'to form: formed' | 1 |
| 'to gather/restrain/fortify' | 1 |
| 'to give/deliver' | 1 |
| 'to go out/away' | 1 |
| 'to go/bring before' | 1 |
| 'to go: went' | 1 |
| 'to grasp/seize' | 1 |
| 'to have/be' | 1 |
| 'to have/cause sores' | 1 |
| 'to hear: hear' | 1 |
| 'to hold back/fast' | 1 |
| 'to hold fast/out' | 1 |
| 'to hold/oppress' | 1 |
| 'to honor: honour' | 1 |
| 'to hope/expect' | 1 |
| 'to judge/doubt' | 1 |
| 'to keep/guard: observe' | 1 |
| 'to keep: obey' | 1 |
| 'to keep: observe' | 1 |
| 'to kindle/burn' | 1 |
| 'to know/choose' | 1 |
| 'to know/understand' | 1 |
| 'to lavish/despise' | 1 |
| 'to lay/be appointed' | 1 |
| 'to lay/throw down' | 1 |
| 'to learn: teach' | 1 |
| 'to leave: forsake' | 1 |
| 'to lend/borrow' | 1 |
| 'to lie down: lay down' | 1 |
| 'to lift: raise' | 1 |
| 'to live/return' | 1 |
| 'to look for/into' | 1 |
| 'to look into/upon' | 1 |
| 'to look up/again' | 1 |
| 'to look upon/at' | 1 |
| 'to loosen/leave' | 1 |
| 'to love: lover' | 1 |
| 'to make: do' | 1 |
| 'to meditate/plot' | 1 |
| 'to mount/board' | 1 |
| 'to nourish/rear' | 1 |
| 'to obtain/happen' | 1 |
| 'to oversee/care for' | 1 |
| 'to pass by/through' | 1 |
| 'to pass on/over/away' | 1 |
| 'to perceive: understand' | 1 |
| 'to plan/present' | 1 |
| 'to plead/comfort' | 1 |
| 'to plow/plot' | 1 |
| 'to ponder/confer' | 1 |
| 'to possess: possess' | 1 |
| 'to praise/bless' | 1 |
| 'to pray/wish for' | 1 |
| 'to precede/arrive' | 1 |
| 'to present: come' | 1 |
| 'to provoke/irritate' | 1 |
| 'to put on/seize' | 1 |
| 'to put/lay on' | 1 |
| 'to reckon/appoint' | 1 |
| 'to reckon: list' | 1 |
| 'to redeem: redeem' | 1 |
| 'to refuse/excuse' | 1 |
| 'to release: leave' | 1 |
| 'to release: release' | 1 |
| 'to remain/endure' | 1 |
| 'to remain/keep on' | 1 |
| 'to remain/persist' | 1 |
| 'to rest upon/dwell' | 1 |
| 'to rest/rely on' | 1 |
| 'to run: run' | 1 |
| 'to saddle/tie' | 1 |
| 'to sail out/away' | 1 |
| 'to saw (in two)' | 1 |
| 'to say: did said' | 1 |
| 'to say: said' | 1 |
| 'to say: says' | 1 |
| 'to say: will say' | 1 |
| 'to see/experience' | 1 |
| 'to see: see' | 1 |
| 'to see: to see' | 1 |
| 'to seize/conceive/help' | 1 |
| 'to send out/away' | 1 |
| 'to send: depart' | 1 |
| 'to separate/leave' | 1 |
| 'to serve/heal' | 1 |
| 'to shake out/off' | 1 |
| 'to shine/appear' | 1 |
| 'to show/prove' | 1 |
| 'to silence: stationary' | 1 |
| 'to sit near/serve' | 1 |
| 'to speak: speak' | 1 |
| 'to spit on/at' | 1 |
| 'to spread/surpass' | 1 |
| 'to stand: rise' | 1 |
| 'to stand: stand' | 1 |
| 'to stoop/bend down' | 1 |
| 'to strengthen: strengthen' | 1 |
| 'to take out/select' | 1 |
| 'to take up/suppose' | 1 |
| 'to take/go around' | 1 |
| 'to take: take' | 1 |
| 'to talk to/with' | 1 |
| 'to teach/learn' | 1 |
| 'to test/tempt' | 1 |
| 'to test/tempt: tempt' | 1 |
| 'to throw/lay down' | 1 |
| 'to throw: throw' | 1 |
| 'to torture: torture' | 1 |
| 'to trust (in)' | 1 |
| 'to turn aside: remove' | 1 |
| 'to turn/wander away' | 1 |
| 'to turn: turn' | 1 |
| 'to twist: tremble' | 1 |
| 'to utter/proclaim' | 1 |
| 'to visit/care for' | 1 |
| 'to wait for/welcome' | 1 |
| 'to wait: wait' | 1 |
| 'to walk in/among' | 1 |
| 'to wall up/off' | 1 |
| 'to wash: wash' | 1 |
| 'to water: watering' | 1 |
| 'to will/desire' | 1 |
| 'to workout/produce' | 1 |
| 'to write/designate' | 1 |
| 'torrent: river' | 1 |
| 'trader/merchant' | 1 |
| 'tree: wood' | 1 |
| 'tribe: rod' | 1 |
| 'tribe: staff' | 1 |
| 'truth: faithful' | 1 |
| 'underneath: under' | 1 |
| 'upright:right' | 1 |
| 'valued/honored' | 1 |
| 'vanity: false' | 1 |
| 'voice/sound: voice' | 1 |
| 'voice: sound' | 1 |
| 'way: conduct' | 1 |
| 'weakness: weak' | 1 |
| 'well/abyss' | 1 |
| 'well/well done!' | 1 |
| 'where?' | 1 |
| 'which?' | 1 |
| 'who/which' | 1 |
| 'will/desire' | 1 |
| 'wind/breath' | 1 |
| 'yoke/scales' | 1 |
| 'you [m.s.]' | 1 |
| 'you be!' | 1 |

## Lemmas with no strong entry yet (by frequency)

| lemma_key | rows |
|---|---:|
| H3068 | 6297 |
| H6213 | 2475 |
| H0430 | 2354 |
| H0935 | 2282 |
| H1980 | 1383 |
| H8085 | 1160 |
| H7200 | 1159 |
| H1696 | 1069 |
| H7725 | 985 |
| H5869 | 873 |
| H7971 | 777 |
| H5315 | 754 |
| G2962 | 708 |
| H1870 | 669 |
| H7451 | 629 |
| H7121 | 622 |
| H5375 | 596 |
| H3820 | 595 |
| H2896 | 562 |
| H7760 | 533 |
| H5975 | 519 |
| H6310 | 491 |
| H6944 | 469 |
| H8104 | 449 |
| H0136 | 429 |
| H5769 | 425 |
| H4941 | 419 |
| G1492 | 396 |
| G4151 | 379 |
| H7307 | 378 |
| H3372 | 314 |
| H3069 | 303 |
| H2403 | 295 |
| H5493 | 289 |
| H5647 | 288 |
| H2388 | 285 |
| H0341 | 280 |
| H0639 | 269 |
| H6485 | 255 |
| H2617 | 247 |
| H2428 | 244 |
| G4102 | 243 |
| H7965 | 237 |
| H5771 | 229 |
| H0410 | 220 |
| H0899 | 213 |
| H5800 | 204 |
| H0157 | 197 |
| H3615 | 187 |
| H7901 | 185 |
| H7311 | 184 |
| H6942 | 170 |
| H3898 | 168 |
| H1984 | 165 |
| H2930 | 162 |
| G2564 | 147 |
| H3644 | 143 |
| G5456 | 140 |
| H5608 | 138 |
| H2490 | 134 |
| H0571 | 121 |
| H3477 | 119 |
| H6664 | 119 |
| H2803 | 118 |
| H3956 | 117 |
| H6918 | 116 |
| H7999 | 116 |
| H8210 | 112 |
| H3513 | 110 |
| H7489 | 104 |
| G5590 | 103 |
| H1350 | 102 |
| G2570 | 101 |
| H3722 | 100 |
| H5162 | 99 |
| H7323 | 91 |
| H0426 | 89 |
| H8074 | 86 |
| H1481 | 85 |
| H3925 | 84 |
| H8549 | 79 |
| H2603 | 78 |
| H5782 | 78 |
| H0205 | 77 |
| H2114 | 77 |
| H6031 | 77 |
| H1168 | 76 |
| H3988 | 76 |
| H2470 | 75 |
| H3885 | 75 |
| H2654 | 74 |
| H7896 | 73 |
| H2790 | 70 |
| H6186 | 70 |
| H6869 | 70 |
| H7919 | 62 |
| H0270 | 61 |
| H1730 | 61 |
| H2256 | 60 |
| G1140 | 59 |
| H2505 | 59 |
| H2342 | 57 |
| H0433 | 56 |
| H5766 | 54 |
| H6887 | 54 |
| H7442 | 54 |
| H7723 | 53 |
| G2556 | 50 |
| H3050 | 50 |
| H4148 | 50 |
| H6960 | 49 |
| H7356 | 45 |
| H2502 | 44 |
| H5749 | 44 |
| H4609 | 43 |
| H5355 | 43 |
| H3256 | 42 |
| G5092 | 41 |
| H2778 | 41 |
| H3245 | 41 |
| H3176 | 40 |
| H7706 | 40 |
| G2168 | 39 |
| H0842 | 39 |
| H8047 | 39 |
| H7194 | 38 |
| H8438 | 38 |
| G1228 | 37 |
| G4567 | 36 |
| H4405 | 36 |
| H5254 | 34 |
| H5401 | 34 |
| H8615 | 34 |
| H8668 | 34 |
| G0770 | 32 |
| H8213 | 31 |
| G2190 | 30 |
| H1826 | 30 |
| H7110 | 29 |
| H5081 | 28 |
| H8433 | 28 |
| G0772 | 27 |
| H2254 | 27 |
| H3708 | 26 |
| H3867 | 26 |
| H4487 | 26 |
| H4888 | 26 |
| H6601 | 26 |
| H6923 | 26 |
| H2530 | 25 |
| H5034 | 25 |
| H5145 | 25 |
| H5258 | 25 |
| G0769 | 24 |
| H2820 | 24 |
| H5175 | 24 |
| H5774 | 24 |
| H7921 | 23 |
| G3986 | 21 |
| H2532 | 21 |
| H5251 | 21 |
| H7737 | 21 |
| G5091 | 20 |
| H2186 | 20 |
| H7342 | 20 |
| H2363 | 19 |
| H6612 | 19 |
| H5496 | 18 |
| H8088 | 18 |
| H2986 | 17 |
| H5753 | 17 |
| H6087 | 17 |
| H3724 | 16 |
| H5848 | 16 |
| H4869 | 15 |
| H6233 | 15 |
| H7423 | 15 |
| H1606 | 14 |
| H7301 | 14 |
| H7602 | 14 |
| G1404 | 13 |
| H2000 | 13 |
| H2611 | 13 |
| H3906 | 12 |
| H4172 | 12 |
| H5273 | 12 |
| H7385 | 12 |
| H7386 | 12 |
| H1605 | 11 |
| H2836 | 11 |
| H5042 | 11 |
| H7623 | 11 |
| G1375 | 10 |
| G1497 | 10 |
| H2048 | 10 |
| H6049 | 10 |
| H6340 | 10 |
| H1524 | 9 |
| H2102 | 9 |
| H2748 | 9 |
| H3039 | 9 |
| H3948 | 9 |
| H5943 | 9 |
| H6670 | 9 |
| H8173 | 9 |
| G1727 | 8 |
| H2556 | 8 |
| H2648 | 8 |
| H4432 | 8 |
| H7663 | 8 |
| H7962 | 8 |
| H8175 | 8 |
| H1442 | 7 |
| H2427 | 7 |
| H3635 | 7 |
| H5183 | 7 |
| H5531 | 7 |
| H5849 | 7 |
| H6089 | 7 |
| H7032 | 7 |
| H8314 | 7 |
| G2787 | 6 |
| H2892 | 6 |
| H3882 | 6 |
| H5102 | 6 |
| H5172 | 6 |
| H6531 | 6 |
| H7067 | 6 |
| H7147 | 6 |
| H7461 | 6 |
| H7654 | 6 |
| H8649 | 6 |
| G0372 | 5 |
| G4288 | 5 |
| H1891 | 5 |
| H1949 | 5 |
| H2749 | 5 |
| H3908 | 5 |
| H5007 | 5 |
| H5356 | 5 |
| H7183 | 5 |
| H7343 | 5 |
| H8324 | 5 |
| H8639 | 5 |
| G0364 | 4 |
| G1142 | 4 |
| G2152 | 4 |
| H0380 | 4 |
| H1176 | 4 |
| H1947 | 4 |
| H2267 | 4 |
| H2844 | 4 |
| H3512 | 4 |
| H4531 | 4 |
| H5541 | 4 |
| H5920 | 4 |
| H5946 | 4 |
| H6090 | 4 |
| H6217 | 4 |
| H6473 | 4 |
| H6695 | 4 |
| H6848 | 4 |
| H7182 | 4 |
| H7294 | 4 |
| H7726 | 4 |
| H8178 | 4 |
| H8186 | 4 |
| G4705 | 3 |
| G4709 | 3 |
| H0943 | 3 |
| H1421 | 3 |
| H1793 | 3 |
| H2616 | 3 |
| H3272 | 3 |
| H4654 | 3 |
| H4915 | 3 |
| H5587 | 3 |
| H5730 | 3 |
| H5788 | 3 |
| H6121 | 3 |
| H7169 | 3 |
| H7332 | 3 |
| H7363 | 3 |
| H7475 | 3 |
| H7697 | 3 |
| H7728 | 3 |
| G0463 | 2 |
| G0884 | 2 |
| G2153 | 2 |
| G2577 | 2 |
| G4021 | 2 |
| G4460 | 2 |
| G4724 | 2 |
| G4763 | 2 |
| G5172 | 2 |
| G5304 | 2 |
| G5314 | 2 |
| G5381 | 2 |
| G5382 | 2 |
| G5468 | 2 |
| G5469 | 2 |
| G5512 | 2 |
| H0596 | 2 |
| H2559 | 2 |
| H3631 | 2 |
| H3856 | 2 |
| H4642 | 2 |
| H5010 | 2 |
| H5607 | 2 |
| H5765 | 2 |
| H6128 | 2 |
| H6145 | 2 |
| H6711 | 2 |
| H6800 | 2 |
| H7189 | 2 |
| H7329 | 2 |
| H7647 | 2 |
| H7700 | 2 |
| H7739 | 2 |
| H8385 | 2 |
| H8541 | 2 |
| H8586 | 2 |
| H8595 | 2 |
| H8632 | 2 |
| G0112 | 1 |
| G0127 | 1 |
| G0335 | 1 |
| G0640 | 1 |
| G1493 | 1 |
| G1559 | 1 |
| G2130 | 1 |
| G2133 | 1 |
| G2314 | 1 |
| G2315 | 1 |
| G2319 | 1 |
| G2432 | 1 |
| G2897 | 1 |
| G4224 | 1 |
| G4290 | 1 |
| G4708 | 1 |
| G4764 | 1 |
| G4994 | 1 |
| G5367 | 1 |
| G5373 | 1 |
| G5397 | 1 |
| G5425 | 1 |
| G5513 | 1 |
| G5542 | 1 |
| G5587 | 1 |
| G5588 | 1 |
| H0193 | 1 |
| H0973 | 1 |
| H1180 | 1 |
| H1948 | 1 |
| H2357 | 1 |
| H2541 | 1 |
| H2613 | 1 |
| H2927 | 1 |
| H3931 | 1 |
| H4783 | 1 |
| H4835 | 1 |
| H4890 | 1 |
| H5040 | 1 |
| H5543 | 1 |
| H5792 | 1 |
| H5868 | 1 |
| H6104 | 1 |
| H6122 | 1 |
| H6127 | 1 |
| H6129 | 1 |
| H6146 | 1 |
| H6199 | 1 |
| H6216 | 1 |
| H6234 | 1 |
| H6615 | 1 |
| H6712 | 1 |
| H7009 | 1 |
| H7283 | 1 |
| H7317 | 1 |
| H7790 | 1 |
| H8265 | 1 |
| H8437 | 1 |
| H8565 | 1 |
