# candidate_seed tag corrections — proposal for review (v1, 2026-07-22)

> Source: the 244 `decision='exception'` rows from `candidate.load`'s revalidation pass
> (`iba/app/reports/candidate-load.md`). For each, I read the row's own `strong.stepGloss` +
> `strong_sense.head` + `strong_meaning_tree` (already captured in the DB — no new STEP calls)
> and propose a single clean concept per the tag-cleanliness principle (§3 of the curation
> method doc). **This file is the review surface — mark each row's `Decision` cell, save, tell me
> to process it.** Nothing is applied yet.
>
> Three outcomes per row:
> - **Proposed** — I'm reasonably confident, with the lexical data backing it. Default action:
>   apply as proposed unless you write something different in `Decision`.
> - **AMBIGUOUS** — the lexical data genuinely supports more than one concept and I won't guess;
>   candidates listed, `Decision` blank for you to pick or write your own.
> - **NO DATA** — this `strong_variant` has no `strong`/`strong_sense`/`strong_meaning_tree` row at
>   all yet (never raw-fetched) — I have nothing to derive from; likely needs `-Field decision
>   rejected` (no real content to curate) or a raw fetch first, your call.
>
> `Decision` column: leave blank to accept `Proposed`, write a replacement tag, or write `REJECT`
> (the lemma doesn't belong as a candidate at all) / `SKIP` (leave as exception for now).

| lemma_key | strong_variant | current tag | Proposed | Decision |
|---|---|---|---|---|
| G0769 | G0769 | weakness: weak | weakness | |
| G0770 | G0770 | be weak: weak | weak | |
| G1252 | G1252 | to judge/doubt | **AMBIGUOUS** (judge / doubt — distinct NT senses, e.g. Jas.1:6 "doubting") | |
| G1492 | G1492 | to perceive: understand | to know | |
| G1679 | G1679 | to hope/expect | to hope | |
| G1771 | G1771 | thought/purpose | purpose | |
| G1879 | G1879 | to rest/rely on | to rely on | |
| G1929 | G1929 | to give/deliver | to deliver | |
| G1941 | G1941 | to call (on)/name | to call on | |
| G1951 | G1951 | to call/choose | **AMBIGUOUS** (call / choose — tree splits passive "be called" vs middle "choose") | |
| G1987 | G1987 | to know/understand | to understand | |
| G2042 | G2042 | to provoke/irritate | to provoke | |
| G2127 | G2127 | to praise/bless | to bless | |
| G2171 | G2171 | a vow/prayer | **AMBIGUOUS** (vow / prayer — tree gives both as primary senses) | |
| G2172 | G2172 | to pray/wish for | to pray | |
| G2213 | G2213 | a question/dispute | dispute | |
| G2294 | G2294 | courage/confidence | courage | |
| G2307 | G2307 | will/desire | will | |
| G2309 | G2309 | to will/desire | to will | |
| G2323 | G2323 | to serve/heal | to heal | |
| G2334 | G2334 | to see/experience | to behold | |
| G2348 | G2348 | to die/be dead | to die | |
| G2551 | G2551 | to curse/revile | to revile | |
| G2554 | G2554 | to do evil/harm | to do harm | |
| G2556 | G2556 | evil/harm: evil | evil | |
| G2564 | G2564 | to call: call | to call | |
| G2577 | G2577 | be weary/sick: weak | weary | |
| G2578 | G2578 | to bend/bow | to bow | |
| G2787 | G2787 | ark: covenant | ark | |
| G2827 | G2827 | to bow/lay down | to bow down | |
| G2836 | G2836 | belly/womb/stomach | **AMBIGUOUS** (belly / womb — both attested, context-dependent) | |
| G2875 | G2875 | to cut/mourn | to mourn | |
| G3027 | G3027 | robber/rebel | robber | |
| G3117 | G3117 | long/distant | distant | |
| G3540 | G3540 | mind/thought | mind | |
| G3870 | G3870 | to plead/comfort | to comfort | |
| G3986 | G3986 | temptation/testing: temptation | temptation | |
| G4100 | G4100 | to trust (in) | to trust | |
| G4151 | G4151 | spirit/breath: spirit | spirit | |
| G4190 | G4190 | evil/bad | evil | |
| G4267 | G4267 | to know/choose | to foreknow | |
| G4332 | G4332 | to sit near/serve | to serve | |
| G4341 | G4341 | to call to/summon | to summon | |
| G4377 | G4377 | to call to/summon | to address | |
| G4483 | G4483 | to say: will say | to say | |
| G4698 | G4698 | affection/entrails | affection | |
| G4820 | G4820 | to ponder/confer | to ponder | |
| G4824 | G4824 | counsel/council | counsel | |
| G5278 | G5278 | to remain/endure | to endure | |
| G5287 | G5287 | confidence/essence | confidence | |
| G5316 | G5316 | to shine/appear | to appear | |
| G5456 | G5456 | voice/sound: voice | voice | |
| G5480 | G5480 | image/mark | mark | |
| G5543 | G5543 | good/kind | kind | |
| H0157 | H0157 | to love: lover | love | |
| H0191 | H0191 | fool[ish] | foolish | |
| H0205 | H0205 | evil: wickedness | wickedness | |
| H0270 | H0270 | seize (achaz) | **NO DATA** | |
| H0380 | H0380 | keep me as the apple of your eye | **NO DATA** (sentence, no strong row — likely not a real candidate) | |
| H0398 | H0398 | eat up / devour (akal - eat up my people) | to devour | |
| H0423 | H0423 | mouth full of cursing and deceit | oath | |
| H0481 | H0481 | I was mute, and my distress grew worse | be dumb | |
| H0559 | H0559 | 'God has forgotten, he won't see' | to say | |
| H0571 | H0571 | truth: faithful | faithfulness | |
| H0639 | H0639 | face: anger | anger | |
| H0693 | H0693 | lie in wait / ambush (arab - they lie in wait for my life) | to ambush | |
| H0817 | H0817 | guilt [offering] | guilt | |
| H0935 | H0935 | come before (bo) | **NO DATA** | |
| H0981 | H0981 | speak rashly (bata) | to speak rashly | |
| H1272 | H1272 | flee (barach) God's presence | to flee | |
| H1290 | H1290 | knees (berek) | knee | |
| H1319 | H1319 | I told the glad news, I did not restrain my lips | to bear tidings | |
| H1350 | H1350 | to redeem: redeem | to redeem | |
| H1364 | H1364 | haughty (gaboah) | haughty | |
| H1396 | H1396 | 'with our tongue we will prevail' | to prevail | |
| H1413 | H1413 | band together (gadad) | to attack | |
| H1481 | H1481 | stir up strife / band together (gur - they stir up strife) | to stir up strife | |
| H1556 | H1556 | commit your way to the LORD | to roll | |
| H1692 | H1692 | cling (dabaq) | to cling | |
| H1696 | H1696 | enemies speak lies (v11) | to speak | |
| H1747 | H1747 | wait in silence / be still (dumiyyah - my soul waits in silence) | silence | |
| H1777 | H1777 | judge / govern (din - may he judge your people with righteousness) | to judge | |
| H1811 | H1811 | melt away (dalaph) | to drip | |
| H1818 | H1818 | bloodthirsty / men of blood (dam - save me from bloodthirsty men) | blood | |
| H1826 | H1826 | quiet (damam) | to be silent | |
| H1892 | H1892 | man is a mere breath, a shadow | vanity | |
| H1949 | H1949 | moan / be in commotion (hum - I moan) | **NO DATA** | |
| H1980 | H1980 | walk (halak) | **NO DATA** | |
| H1993 | H1993 | moan / murmur (hamah - and moan) | to murmur | |
| H2015 | H2015 | you turned my mourning into dancing | to overturn | |
| H2026 | H2026 | kill (harag) | to kill | |
| H2076 | H2076 | sacrifice (zabach) | to sacrifice | |
| H2107 | H2107 | to lavish/despise | to despise | |
| H2114 | H2114 | be estranged / alienated (zur - estranged from the womb) | to be estranged | |
| H2254 | H2254 | conceives evil, births lies | to corrupt | |
| H2308 | H2308 | he has ceased to act wisely | to cease | |
| H2310 | H2310 | rejected/fleeting | fleeting | |
| H2342 | H2342 | to twist: tremble | to tremble | |
| H2363 | H2363 | hasten (chush) | to hasten | |
| H2372 | H2372 | behold your face, satisfied with your likeness | to behold | |
| H2388 | H2388 | to strengthen: strengthen | to strengthen | |
| H2428 | H2428 | strength: soldiers | strength | |
| H2459 | H2459 | unfeeling (tapash) | fat (fig. unfeeling) | |
| H2470 | H2470 | be weak: weak | weak | |
| H2487 | H2487 | change (chaliphah - they do not change) | change | |
| H2490 | H2490 | profane / violate (chalal - he violated his covenant) | to profane | |
| H2505 | H2505 | he flatters himself about his sin | to flatter | |
| H2556-b | H2556 | be embittered / soured (chamets - when my soul was embittered) | **AMBIGUOUS** (tree only gives "to be red" — doesn't obviously support "embittered"; may be a different homonym root) | |
| H2648 | H2648 | in alarm I said 'I am cut off' | **NO DATA** | |
| H2664 | H2664 | search out (chaphas - a diligent search) | to search | |
| H2790 | H2790 | to plow/plot | to devise | |
| H2795 | H2795 | like a deaf, mute man I do not answer | deaf | |
| H2803 | H2803 | to devise: design | to devise | |
| H2986 | H2986 | bring / present (yabal - let all bring gifts) | **NO DATA** | |
| H3021 | H3021 | be weary/toil | weary | |
| H3051 | H3051 | ascribe glory, worship in holiness | to ascribe | |
| H3176 | H3176 | to wait: wait | to wait | |
| H3201 | H3201 | prevail (yakol, negated) | to be able | |
| H3238 | H3238 | proud (yonah/gaayon) | **AMBIGUOUS** (tag names two DIFFERENT roots — yonah/gaayon vs the resolved strong H3238 "to oppress"; tag itself looks mismatched to this lemma) | |
| H3289 | H3289 | plan / take counsel (yaats - they only plan to thrust him down) | to counsel | |
| H3365 | H3365 | precious (yaqar) esteeming | precious | |
| H3427 | H3427 | dwell in unity (yashab) | to dwell | |
| H3477 | H3477 | upright:right | upright | |
| H3513 | H3513 | to honor: honour | to honour | |
| H3582 | H3582 | hide (kachad, refused) | to hide | |
| H3615 | H3615 | pass away (kalah) | to be complete | |
| H3680 | H3680 | I have not hidden your righteousness in my heart | to conceal | |
| H3689 | H3689 | foolish confidence / folly (kesel) | folly | |
| H3885 | H3885 | abide (lun) | to abide | |
| H3898 | H3898 | fight / attack (lacham - many attack me) | to fight | |
| H3905 | H3905 | oppress (lachats) | to oppress | |
| H3925 | H3925 | learn (lamad) | to learn | |
| H4036 | H4036 | \`Terror on Every Side\` | **REJECT candidate** (a person's name/epithet — Pashhur — not an IB concept at all) | |
| H4102 | H4102 | delay (mahah, negated) | to delay | |
| H4171 | H4171 | exchange (mur) | to exchange | |
| H4405 | H4405 | word (millah) before the tongue | **NO DATA** | |
| H4487 | H4487 | number (manah) | **NO DATA** | |
| H4672 | H4672 | suffer (matsa) | to find | |
| H4941 | H4941 | justice: judgement | judgement | |
| H4974 | H4974 | no soundness in my flesh because of sin | soundness | |
| H5027 | H5027 | see (nabat) | to look | |
| H5042 | H5042 | pour forth fame + sing | **NO DATA** | |
| H5046 | H5046 | I confess my iniquity, I am sorry for my sin | to confess | |
| H5071 | H5071 | offer freely (nedabah) | freewill offering | |
| H5081 | H5081 | noble: willing | willing | |
| H5087 | H5087 | vow (nadar) | to vow | |
| H5088 | H5088 | perform my vows before the fearers | vow | |
| H5102 | H5102 | those who look to him are radiant | **NO DATA** | |
| H5112 | H5112 | tossings / restless wanderings (nod - my tossings) | wandering | |
| H5136 | H5136 | be in despair / be sick (anash - I am in despair) | to be sick | |
| H5145 | H5145 | consecration: Nazirite vow | **REJECT candidate** (a proper-noun religious-office entry, not an IB concept) | |
| H5162 | H5162 | to be sorry: comfort | to comfort | |
| H5186 | H5186 | turn aside (natah) | to turn aside | |
| H5341 | H5341 | observe (natsar) | to guard | |
| H5375 | H5375 | lift up (nasa) | to lift up | |
| H5392 | H5392 | no usury, no bribe | interest | |
| H5472 | H5472 | turn back / fall away (sug - they have all fallen away) | to backslide | |
| H5493 | H5493 | turn aside (sur, negated) | to turn aside | |
| H5543-b | H5543 | \`valor\` | **REJECT candidate** (a person's name — Sallai — not an IB concept) | |
| H5564 | H5564 | lean / be sustained (samak - upon you I have leaned from before my birth) | to lean upon | |
| H5588 | H5588 | double-minded (seeph) | divided | |
| H5608 | H5608 | declare (saphar) | to recount | |
| H5641 | H5641 | hide oneself (sathar - then I could hide from him) | to hide oneself | |
| H5753 | H5753 | commit iniquity (avah) | to distort | |
| H5769 | H5769 | forever: enduring | everlasting | |
| H5771 | H5771 | iniquity: crime | iniquity | |
| H5774 | H5774 | fly away (uph - I would fly away) | **NO DATA** | |
| H5800 | H5800 | forsake (azab) | to forsake | |
| H5949 | H5949 | wrongdoings (alilah) | wanton deeds | |
| H5956 | H5956 | secret sins (alum) | to conceal | |
| H6031 | H6031 | be hurt (anah) | **AMBIGUOUS** (tree only gives "to be occupied, be busied with" — doesn't support "be hurt"; likely a homonym-root mismatch, same pattern as H2556) | |
| H6135 | H6135 | barren woman (aqar) | barren | |
| H6141 | H6141 | perverse (iqqesh) | perverse | |
| H6148 | H6148 | mix (arab) | **AMBIGUOUS** (tag "mix" vs tree "to pledge/exchange" — mismatch, possibly wrong homonym root resolved) | |
| H6199 | H6199 | destitute (arar) | **NO DATA** | |
| H6213 | H6213 | practice (asah) | to do | |
| H6323 | H6323 | helpless (pun) | to distract (fig. helpless) | |
| H6340 | H6340 | distribute freely (pazar) | **NO DATA** | |
| H6466 | H6466 | do no wrong (paal) | to do | |
| H6473 | H6473 | open the mouth (paar) | **NO DATA** | |
| H6485 | H6485 | into your hand I commit my spirit | to attend to | |
| H6601 | H6601 | flatter / deceive (pathah) | **AMBIGUOUS** (tag "flatter/deceive" vs tree "to be spacious/open" — mismatch, likely wrong homonym root) | |
| H6845 | H6845 | store up (tsaphan) | to treasure up | |
| H6869 | H6869 | the troubles of my heart enlarged | distress | |
| H6884 | H6884 | invite God to test the heart | to refine | |
| H6887 | H6887 | be afflicted (tsarar) | to be in distress | |
| H6923 | H6923 | come (qadam) | **NO DATA** | |
| H6937 | H6937 | I mourned for them as for kin | be dark (fig. mourn) | |
| H6942 | H6942 | to consecrate: consecate | to consecrate | |
| H6974 | H6974 | awake (qits) still with God | to awake | |
| H7032 | H7032 | voice: sound | voice | |
| H7043 | H7043 | curse (qalal) | **AMBIGUOUS** (tag "curse" vs tree "to be slight/swift/trifling" — mismatch, likely wrong homonym root) | |
| H7067 | H7067 | Jealous [God] | **REJECT candidate** (a divine-name/epithet entry, not a general IB concept) | |
| H7121 | H7121 | to call: call to | to call | |
| H7128 | H7128 | war / conflict (qerab - war was in his heart) | battle | |
| H7200 | H7200 | see (raah) | to see | |
| H7279 | H7279 | murmur (ragan) | to murmur | |
| H7291 | H7291 | pursue (radaph) | to pursue | |
| H7300 | H7300 | be restless / roam in distress (rud - I am restless) | to roam | |
| H7301 | H7301 | they feast on the abundance of your house | **NO DATA** | |
| H7311 | H7311 | extol (rum) | to be exalted | |
| H7318 | H7318 | high praise with sword in hand | extolling | |
| H7323 | H7323 | run (ruts) | to run | |
| H7342 | H7342 | arrogant (rachab) | **NO DATA** | |
| H7442 | H7442 | shout (ranan) | **AMBIGUOUS** (tag "shout" vs tree "to overcome" — mismatch, likely wrong homonym root) | |
| H7451 | H7451 | bad: harmful | evil | |
| H7503 | H7503 | refrain from anger, forsake wrath | to slacken (fig. relent) | |
| H7521 | H7521 | hold dear (ratsah) | to accept | |
| H7523 | H7523 | murder (ratsach) | to murder | |
| H7580 | H7580 | I groan from the tumult of my heart | to roar | |
| H7592 | H7592 | pray (shaal) | to ask | |
| H7623 | H7623 | glory (shabach) | **AMBIGUOUS** (tag "glory" vs tree "to soothe, still" — mismatch, likely wrong homonym root, cf. Aramaic shabach "praise" vs Hebrew shabach "soothe") | |
| H7650 | H7650 | swear (shaba) | to swear | |
| H7663 | H7663 | hope (yachal/sabar) | to hope | |
| H7683 | H7683 | go astray (shagag) | to err | |
| H7686 | H7686 | wander (shagah, negated) | to err | |
| H7723 | H7723 | vain (shav) | vanity | |
| H7725 | H7725 | return (shuv) | to return | |
| H7760 | H7760 | make (sim) | to set | |
| H7814 | H7814 | laughter (sechoq) | laughter | |
| H7832 | H7832 | laugh / deride (sachaq - laugh at him) | to deride | |
| H7853 | H7853 | accusers (satan) | to oppose | |
| H7854 | H7854 | accuser (satan) | **REJECT candidate** (Satan as proper noun — a being, not an IB characteristic; candidate for the new `ib_referent_type='other_being'` marker instead, see note below) | |
| H7896 | H7896 | set (shith) | to set | |
| H7901 | H7901 | lie down and sleep in trust | to lie down | |
| H7908 | H7908 | my soul bereft, repaid evil for good | bereavement | |
| H7931 | H7931 | be at rest / settle (shakan - and be at rest) | to dwell | |
| H7971 | H7971 | stretch out the hands (shalach) | to send | |
| H7993 | H7993 | cast / throw (shalak - cast your burden on the LORD) | to cast | |
| H8047 | H8047 | horror: destroyed | horror | |
| H8104 | H8104 | to keep: obey | obey | |
| H8159 | H8159 | look away, that I may smile again | to gaze | |
| H8173 | H8173 | delight (shaashua/shaa/sus) | **AMBIGUOUS** (tag "delight" vs tree "to be smeared over, be blinded" — mismatch, likely wrong homonym root) | |
| H8199 | H8199 | defend / judge for (shaphat - may he defend the cause of the poor) | to judge | |
| H8210 | H8210 | pour out (shaphak) | to pour out | |
| H8216 | H8216 | low estate (shephel) | poverty | |
| H8217 | H8217 | lowly (shaphal) | low | |
| H8264 | H8264 | longing (shaqaq) | to long for | |
| H8266 | H8266 | be false / deal falsely (shaqar - to your covenant, negated) | to deal falsely | |
| H8438 | H8438 | I am a worm, not a man | worm | |
| H8451 | H8451 | the law in his heart, steps not slipping | instruction | |
| H8539 | H8539 | be astounded / amazed (tamah) | to be astounded | |
| H8615 | H8615 | hope / expectation (tiqvah - my hope is from him) | **AMBIGUOUS** (tag "hope" vs tree "cord" — mismatch, likely wrong homonym root, cf. tiqvah "cord" vs "hope") | |
| H8668 | H8668 | deliverance: salvation | salvation | |

## Notes on what this surfaced beyond simple tag cleanup

- **7 likely wrong-homonym-root matches** (H2556, H6031, H6148, H6601, H7043, H7442, H7623, H8173,
  H8615 — 9 actually): the CURRENT tag describes one meaning, but the `strong_meaning_tree` data
  captured for the RESOLVED Strong's code describes something else entirely. Hebrew/Greek often
  has multiple homonym roots sharing a spelling (e.g. `shabach` "to soothe" vs a separate root
  "to praise"); this looks like the seed migration matched the tag's intended sense to the wrong
  one of several codes. These need your judgement on which Strong's code was actually meant, not
  just a tag reword — flagging rather than guessing.
- **3 proper-noun / non-IB entries** (H4036 "Terror on Every Side" — a person's epithet; H5145
  "Nazirite vow" — a religious office; H7067 "Jealous [God]" — a divine epithet; H5543 "valor" — a
  person's name): these look like the independent net swept in named entities, not IB
  characteristics. Proposed `-Field decision rejected` unless you see IB relevance I'm missing.
- **H7854 "Satan"** — a genuine "other being" case, exactly the kind escalation `#228`'s new
  `ib_referent_type` marker exists for. Once this batch is applied, worth a follow-up pass
  specifically classifying such rows via the `other-being`/`body-part` `cfg_candidate_rule` kinds
  (currently empty — no curated lists exist yet; that's a separate, smaller task).
- **~28 rows with NO strong/sense/meaning-tree data at all** — these lemma_keys were never
  raw-fetched (no word's `raw.detail` step has pulled them yet), so there is nothing here for me
  to derive a clean tag from. Most look like real IB-relevant lemmas worth keeping as
  candidates once fetched (e.g. `H1980` walk/halak, `H7200`'s sibling `H0935` "come/bo") — I'd
  suggest leaving these as-is (still flagged exception) until a word registration happens to pull
  their `strong` data in, rather than guessing blind.
