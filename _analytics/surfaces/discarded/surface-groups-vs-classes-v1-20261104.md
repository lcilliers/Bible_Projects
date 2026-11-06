# Surface groups against the judged surface classes (#2359, perspective 1)

> Developer Mode session 5dc90923, 2026-11-04. Escalation #2359, scope (a) behaviour and states only. Inferential (B:4): every class is the Ollama judge's (qwen3:30b) single judgement of the surface, from #2354 `first-split-v3-20261103.jsonl` (finished 08:10Z, 6,069 of 6,069, 0 failed; where a surface has a retry line the last line is used). The judgement is made on the English surface alone; no Strong's code is used here. A "surface group" here is a `cluster_subgroup` of kind group, taken through `surface_subgroup` (one row per cluster, code, surface); a surface is counted once per group. This is a view, not a finding, and not an input to concept forming.

## 1. All four kinds of subgroup, by distinct surface

| kind | subgroups | distinct surfaces | behaviour | inner_being_state | being | other | unjudged |
|---|---|---|---|---|---|---|---|
| group | 406 | 4840 | 1164 | 2144 | 500 | 1032 | 0 |
| qualifier | 5 | 80 | 1 | 51 | 5 | 23 | 0 |
| not_this_sense | 78 | 2028 | 352 | 752 | 283 | 641 | 0 |
| anomaly | 43 | 125 | 15 | 34 | 20 | 55 | 1 |

A surface can sit in subgroups of more than one kind, so the kind rows do not add up to the total.

Judged surfaces: 6069 = behaviour 1294, inner_being_state 2500, being 719, other 1556. Judged surfaces in no subgroup row at all: 0; of these: .

## 2. Each group of kind `group`: classes of its surfaces, and the missing ones

"Missing" = a surface in the group that the judge placed as being or other, so it is in neither behaviour nor state. The full surface-by-surface file is `outputs/concept-mapping/surface-group/subgroup-surface-classes-v1-20261104.csv`.

| cluster | subgroup (label) | surfaces | behaviour | state | being | other | missing % | missing surfaces (up to 12) |
|---|---|---|---|---|---|---|---|---|
| M01 Fear & Awe | M01_awe Awe, reverence, fear of God | 28 | 5 | 19 | 1 | 3 | 14% | awesome [o], awesome deeds [B], awesome thing [o], terrifying [o] |
| M01 Fear & Awe | M01_fear Fear, dread, terror | 44 | 7 | 29 | 1 | 7 | 18% | away [o], dreadful assaults [o], fearsome [o], frightening [o], have [o], of him [o], terrifying [o], thing [B] |
| M01 Fear & Awe | M01_horror Horror, appalment | 19 | 1 | 11 | 1 | 6 | 37% | appalling [o], bristle [o], bristles [o], horrible thing [B], look aghast [o], shocked [o], wonder [o] |
| M01 Fear & Awe | M01_trembling Trembling, shuddering, quaking | 16 | 9 | 5 | 0 | 2 | 12% | come trembling [o], violently [o] |
| M02 Anger & Wrath | M02_anger Anger, indignation | 24 | 14 | 6 | 0 | 4 | 17% | feels [o], indignantly [o], sullen [o], was [o] |
| M02 Anger & Wrath | M02_burning Anger kindled, burning | 17 | 2 | 10 | 0 | 5 | 29% | blazed [o], heat [o], hot [o], hot displeasure [o], smoke [o] |
| M02 Anger & Wrath | M02_provocation Provocation, vexation | 18 | 10 | 5 | 0 | 3 | 17% | fretful [o], harass [o], irritable [o] |
| M02 Anger & Wrath | M02_strife Quarrel, strife | 15 | 5 | 7 | 0 | 3 | 20% | constant friction [o], quarrels about words [o], sharp disagreement [o] |
| M02 Anger & Wrath | M02_wrath Wrath, fury | 14 | 3 | 10 | 0 | 1 | 7% | bore [o] |
| M03 Grief & Lament | M03_bitterness Bitterness | 6 | 1 | 5 | 0 | 0 | 0% |  |
| M03 Grief & Lament | M03_groaning Groaning, sighing | 13 | 11 | 2 | 0 | 0 | 0% |  |
| M03 Grief & Lament | M03_mourning Mourning, lament, wailing | 27 | 20 | 6 | 0 | 1 | 4% | wailings [o] |
| M03 Grief & Lament | M03_sorrow Sorrow, grief, distress | 28 | 3 | 23 | 0 | 2 | 7% | bereavement [o], sorry [o] |
| M03 Grief & Lament | M03_torment Torment, pangs | 9 | 3 | 6 | 0 | 0 | 0% |  |
| M03 Grief & Lament | M03_trouble Trouble, toil, misery | 22 | 4 | 10 | 0 | 8 | 36% | brought trouble [o], disaster [o], hard labor [o], misfortune [o], trouble befalls [o], trouble yourself [o], which [o], whoever [o] |
| M03 Grief & Lament | M03_weeping Weeping, tears | 13 | 7 | 3 | 0 | 3 | 23% | after [o], at all [o], for [o] |
| M03 Grief & Lament | M03_woe Woe, alas | 6 | 1 | 2 | 0 | 3 | 50% | ah [o], alas [o], woe to [o] |
| M04 Joy & Gladness | M04_joy Joy, gladness, mirth | 34 | 7 | 20 | 0 | 7 | 21% | cheered [o], cheers [o], enjoyment [o], good cheer [o], jubilant [o], mirth [o], most gladly [o] |
| M04 Joy & Gladness | M04_laughter Laughter, play | 14 | 8 | 0 | 0 | 6 | 43% | entertained [o], jesting [o], merrymakers [o], play [o], playing [o], revelers [o] |
| M04 Joy & Gladness | M04_pleasing Pleasing another | 7 | 1 | 4 | 0 | 2 | 29% | displease [o], please [o] |
| M04 Joy & Gladness | M04_rejoicing Rejoicing, exulting | 21 | 9 | 7 | 0 | 5 | 24% | celebrate [o], celebrated [o], celebrating [o], exulting ones [o], joyously [o] |
| M05 Kindness & Friendship | M05_doing_good Doing good, generosity | 23 | 7 | 12 | 1 | 3 | 17% | alms [B], contribution [o], more good [o], provide [o] |
| M05 Kindness & Friendship | M05_friendship Friendship, fellowship, affection | 24 | 5 | 4 | 7 | 8 | 62% | children [B], friend [B], friends [o], friendship [o], him [o], husbands [B], partaker [B], partakers [B], participants [o], participation [o], participation in [o], partner [B] … +3 |
| M05 Kindness & Friendship | M05_godly The godly, the faithful | 10 | 0 | 8 | 2 | 0 | 20% | holy one [B], saints [B] |
| M05 Kindness & Friendship | M05_kindness Kindness, gentleness, tenderness | 22 | 2 | 19 | 0 | 1 | 5% | courtesy [o] |
| M05 Kindness & Friendship | M05_mercy Pity, sparing, compassion | 16 | 1 | 10 | 0 | 5 | 31% | divine forbearance [o], mercilessly [o], ruthlessly [o], spare [o], unsparing [o] |
| M06 Malice & Enmity | M06_cursing Cursing, reviling | 14 | 7 | 4 | 0 | 3 | 21% | curse [o], curses [o], revilings [o] |
| M06 Malice & Enmity | M06_enemies Enemies, adversaries, foes | 12 | 1 | 0 | 9 | 2 | 92% | accuser [B], adversaries [B], adversary [B], adversary’s [B], enemies [B], enemy [B], enemy’s [B], foe [B], foes [B], opponent [o], opponents [o] |
| M06 Malice & Enmity | M06_hatred Hatred, abhorring, loathing | 34 | 4 | 24 | 0 | 6 | 18% | abhorrent [o], abominably [o], disliked [o], more abominably [o], stench [o], stink [o] |
| M06 Malice & Enmity | M06_hostility Hostility, opposition, accusing | 20 | 6 | 8 | 1 | 5 | 30% | accusers [B], against [o], in [o], opposing [o], press [o], severely [o] |
| M06 Malice & Enmity | M06_oppression Oppression, harshness | 13 | 2 | 2 | 4 | 5 | 69% | driver [o], exacted [o], harshness [o], oppressor [B], oppressors [B], ruthlessly [o], taskmaster [o], taskmasters [B], tribute [B] |
| M06 Malice & Enmity | M06_plotting Plotting, devising | 29 | 8 | 10 | 1 | 10 | 38% | conspiracy [o], deal craftily [o], devices [B], mischief [o], plot [o], plow [o], plowed [o], scheme [o], schemer [o], schemes [o], vile deeds [o] |
| M06 Malice & Enmity | M06_scorn Contempt, scorn, derision | 25 | 8 | 13 | 0 | 4 | 16% | derided [o], insult [o], shamefully [o], stench to [o] |
| M07 Shame & Confusion | M07_confusion Confusion, disappointment | 4 | 0 | 4 | 0 | 0 | 0% |  |
| M07 Shame & Confusion | M07_curse Becoming a curse | 5 | 1 | 2 | 0 | 2 | 40% | curse [o], curses [o] |
| M07 Shame & Confusion | M07_disgrace Disgrace, dishonour | 21 | 2 | 15 | 0 | 4 | 19% | disrepute [o], put them [o], reputation [o], shamefully [o] |
| M07 Shame & Confusion | M07_reproach Reproach, taunt, scorn | 17 | 8 | 6 | 0 | 3 | 18% | cast reproach [o], insolently [o], insult [o] |
| M07 Shame & Confusion | M07_shame Shame, being ashamed | 19 | 6 | 12 | 0 | 1 | 5% | embarrassed [o] |
| M08 Pride & Arrogance | M08_boasting Boasting, glorying | 14 | 7 | 7 | 0 | 0 | 0% |  |
| M08 Pride & Arrogance | M08_majesty Majesty, exaltation | 16 | 1 | 13 | 0 | 2 | 12% | magnificence [o], preeminent [o] |
| M08 Pride & Arrogance | M08_mocking Mocking, scoffing, derision | 23 | 13 | 9 | 0 | 1 | 4% | deride [o] |
| M08 Pride & Arrogance | M08_pride Pride, arrogance, haughtiness | 48 | 0 | 38 | 0 | 10 | 21% | are [o], insolent [o], insolently [o], more highly [o], pomp [o], presumes [o], presumptuous [o], presumptuously [o], reckless [o], towered [o] |
| M09 Humility & Lowliness | M09_humility Humility, lowliness, meekness | 22 | 0 | 20 | 0 | 2 | 9% | asceticism [o], submissiveness [o] |
| M09 Humility & Lowliness | M09_poor Poor, needy, weak | 15 | 0 | 15 | 0 | 0 | 0% |  |
| M09 Humility & Lowliness | M09_subdued Subdued, brought low | 9 | 1 | 7 | 0 | 1 | 11% | down [o] |
| M10 Violence & Cruelty | M10_crushing Crushing, breaking | 18 | 4 | 10 | 1 | 3 | 22% | fine [o], pieces [B], powder [o], smashed [o] |
| M10 Violence & Cruelty | M10_destroying Destroying, laying waste | 43 | 4 | 20 | 5 | 14 | 44% | battering down [o], bring desolation [o], cut off [B], demolish [o], desolator [o], destroyer [B], destroyers [B], devastate [o], devastation [o], devastations [o], laid waste [o], made dust [B] … +7 |
| M10 Violence & Cruelty | M10_perishing Perishing, being lost | 7 | 2 | 5 | 0 | 0 | 0% |  |
| M10 Violence & Cruelty | M10_strife Strife, dispute, lawsuit | 20 | 7 | 6 | 1 | 6 | 35% | adversary [B], case [o], cause [o], controversy [o], disputed cases [o], indictment [o], lawsuit [o] |
| M10 Violence & Cruelty | M10_violence Violence, cruelty, ruthlessness | 32 | 7 | 13 | 6 | 6 | 38% | flung [o], inflicted cruelties [o], men [B], merciless foe [o], oppressors [B], pierce [B], plundered [o], robbery [B], ruthless [o], spoil [B], through [o], tyrant [B] |
| M10 Violence & Cruelty | M10_war War, battle, fighting | 26 | 9 | 4 | 5 | 8 | 50% | army [B], array [B], battle array [o], battle line [o], down [o], experienced warriors [o], line of battle [o], march [o], soldier [o], soldiers [B], storm [o], warrior [B] … +1 |
| M10c Defilement | M10c_defiling Defiling, being defiled | 14 | 7 | 3 | 2 | 2 | 29% | desecrated [o], pollute [B], soiled [o], things polluted [B] |
| M10c Defilement | M10c_detestable Detestable | 8 | 0 | 5 | 2 | 1 | 38% | filthy thing [B], tainted meat [o], unclean thing [B] |
| M10c Defilement | M10c_unclean Unclean, uncleanness, impurity | 23 | 0 | 17 | 1 | 5 | 26% | menstrual [o], menstrual impurity [o], menstruation [o], pronounce [o], pronounce him [o], unclean thing [B] |
| M11 Turning & Repentance | M11_departing Departing, turning away from | 9 | 5 | 3 | 0 | 1 | 11% | away [o] |
| M11 Turning & Repentance | M11_relenting Relenting, regret | 12 | 0 | 9 | 1 | 2 | 25% | back [B], regretted [o], sorry [o] |
| M11 Turning & Repentance | M11_removing Removing, taking away | 24 | 8 | 4 | 2 | 10 | 50% | away [o], cut off [B], deposed [B], deprive [o], deprives [o], far [o], go away [o], off [o], out [o], relieved [o], removal [o], take off [o] |
| M11 Turning & Repentance | M11_repenting Repenting, turning back to God | 17 | 10 | 6 | 0 | 1 | 6% | brought them back [o] |
| M11 Turning & Repentance | M11_returning Returning, going back | 5 | 2 | 2 | 0 | 1 | 20% | come back [o] |
| M11 Turning & Repentance | M11_turning_aside Turning aside, going astray | 20 | 8 | 6 | 0 | 6 | 30% | aside [o], banish [o], go in [o], turn your [o], turns aside [o], wander off [o] |
| M12 Righteousness & Integrity | M12_injustice Injustice, unrighteousness, wrong | 24 | 5 | 15 | 1 | 3 | 17% | bribe [B], dishonestly [o], falsely [o], gain [o] |
| M12 Righteousness & Integrity | M12_integrity Integrity, blamelessness, innocence | 22 | 0 | 21 | 1 | 0 | 5% | blemish [B] |
| M12 Righteousness & Integrity | M12_justice Justice, equity | 15 | 1 | 11 | 0 | 3 | 20% | cause [o], honest evidence [o], rights [o] |
| M12 Righteousness & Integrity | M12_righteousness Righteousness, the righteous | 19 | 3 | 16 | 0 | 0 | 0% |  |
| M12 Righteousness & Integrity | M12_rules Rules, judgments, decisions | 38 | 6 | 14 | 5 | 13 | 47% | adversary [B], appointment [o], arrangements [o], case [o], court [o], decision [o], decree [B], deserve [o], due [o], duties [o], law [B], prescribed [o] … +6 |
| M12 Righteousness & Integrity | M12_upright Upright, uprightness | 15 | 1 | 13 | 0 | 1 | 7% | level [o] |
| M13 Faith & Faithfulness | M13_faith Faith, believing | 13 | 3 | 9 | 1 | 0 | 8% | believers [B] |
| M13 Faith & Faithfulness | M13_faithfulness Faithfulness, being sure | 20 | 1 | 18 | 0 | 1 | 5% | honestly [o] |
| M13 Faith & Faithfulness | M13_truth Truth, being true | 12 | 0 | 10 | 0 | 2 | 17% | certainly [o], verified [o] |
| M14 Deceit & Falsehood | M14_crooked Crookedness, perversity | 15 | 0 | 12 | 0 | 3 | 20% | dishonest things [o], twist [o], upside down [o] |
| M14 Deceit & Falsehood | M14_deceit Deceit, deception, craft | 40 | 8 | 13 | 4 | 15 | 48% | came cringing [o], come cringing [o], come fawning [o], cringe [o], dealt shrewdly [o], deceitful brook [B], deceiver [B], deceivers [B], delude [o], flattery [o], illusions [o], impostor [o] … +7 |
| M14 Deceit & Falsehood | M14_hiding Hiding, concealing | 12 | 2 | 9 | 0 | 1 | 8% | ignore [o] |
| M14 Deceit & Falsehood | M14_hypocrisy Hypocrisy | 5 | 1 | 4 | 0 | 0 | 0% |  |
| M14 Deceit & Falsehood | M14_lying Lying, falsehood | 16 | 10 | 4 | 0 | 2 | 12% | falsely [o], wrongfully [o] |
| M14 Deceit & Falsehood | M14_pretenders False prophets, pretenders | 6 | 0 | 1 | 5 | 0 | 83% | false brothers [B], false christs [B], false prophet [B], false prophets [B], prophets [B] |
| M14 Deceit & Falsehood | M14_slander Slander, whispering, evil report | 16 | 11 | 1 | 1 | 3 | 25% | evil gossip [o], report [o], slanderer [B], slanderous [o] |
| M14 Deceit & Falsehood | M14_treachery Treachery, betrayal, faithlessness | 22 | 6 | 9 | 1 | 6 | 32% | be [o], faithlessly with [o], traitor [o], traitors [B], treacherously [o], treachery [o], we [o] |
| M14 Deceit & Falsehood | M14_vanity Vanity, emptiness, worthlessness | 19 | 0 | 13 | 4 | 2 | 32% | because [o], breath [B], empty talk [o], false gods [B], idols [B], wind [B] |
| M15 Knowing & Understanding | M15_considering Considering, meditating | 26 | 7 | 12 | 1 | 6 | 27% | closely [o], lay [o], mark [B], mused [o], note [o], reviewed [o], think over [o] |
| M15 Knowing & Understanding | M15_knowing Knowing, being known | 59 | 8 | 33 | 1 | 17 | 31% | acquainted [o], among [o], beforehand [o], concern [o], experienced [o], familiar [o], find out [o], found out [o], how [o], i [o], indeed [o], inform [o] … +6 |
| M15 Knowing & Understanding | M15_knowledge Knowledge | 2 | 0 | 2 | 0 | 0 | 0% |  |
| M15 Knowing & Understanding | M15_mind Mind | 5 | 0 | 5 | 0 | 0 | 0% |  |
| M15 Knowing & Understanding | M15_perceiving Perceiving by the senses | 7 | 4 | 2 | 0 | 1 | 14% | tastes [o] |
| M15 Knowing & Understanding | M15_teaching Teaching, training, making known | 17 | 7 | 9 | 1 | 0 | 6% | teacher [B] |
| M15 Knowing & Understanding | M15_thinking Thinking, supposing, judging | 47 | 5 | 31 | 0 | 11 | 23% | arguments [o], come into [o], fully expected [o], presume [o], seem [o], seemed [o], seemed best [o], seemed influential [o], seems [o], suppose [o], supposed [o] |
| M15 Knowing & Understanding | M15_understanding Understanding, insight, discernment | 55 | 6 | 42 | 1 | 6 | 13% | expert [o], gain [o], have [o], mark [B], never [o], shrewd [o], take note [o] |
| M16 Wisdom & Folly | M16_counsel Counsel, advice, plans | 26 | 3 | 13 | 4 | 6 | 38% | advice [o], agreed [o], consultation [o], council [B], counselor [B], counselors [B], devices [B], schemes [o], secret plots [o], strategy [o] |
| M16 Wisdom & Folly | M16_craftiness Craftiness, cunning | 5 | 0 | 5 | 0 | 0 | 0% |  |
| M16 Wisdom & Folly | M16_folly Folly, the fool, the simple | 43 | 3 | 28 | 1 | 11 | 28% | brutish [o], crazed [o], dullest [o], foolishly [o], insane [o], lacks [o], outrage [o], outrageous [o], outrageous thing [o], stupid [o], unsavory thing [o], vile thing [B] |
| M16 Wisdom & Folly | M16_skill Skill, craft | 12 | 1 | 6 | 5 | 0 | 42% | craftsman [B], craftsmen [B], men [B], skillful craftsman [B], skillful women [B] |
| M16 Wisdom & Folly | M16_teaching Teaching, instruction, discipline | 18 | 7 | 10 | 1 | 0 | 6% | teacher [B] |
| M16 Wisdom & Folly | M16_wisdom Wisdom, the wise, prudence | 40 | 1 | 36 | 0 | 3 | 8% | judicious [o], manifold [o], resource [o] |
| M18 Desire & Longing | M18_beauty Beauty | 11 | 0 | 7 | 0 | 4 | 36% | attractive [o], handsome [o], lovely [o], pleasant places [o] |
| M18 Desire & Longing | M18_delight Delight, pleasure, gladness | 23 | 1 | 18 | 0 | 4 | 17% | any [o], cheer [o], happiness [o], merry [o] |
| M18 Desire & Longing | M18_desire Desire, craving, longing | 53 | 10 | 32 | 1 | 10 | 21% | aspire [o], aspires [o], did [o], flesh [B], heat [o], lusty [o], pants [o], passions draw [o], sniffing [o], wish [o], you [o] |
| M18 Desire & Longing | M18_favour Favour, acceptance, approval | 20 | 0 | 16 | 0 | 4 | 20% | acceptance [o], please [o], suits [o], to him [o] |
| M18 Desire & Longing | M18_precious Precious, costly, valued | 22 | 1 | 12 | 4 | 5 | 41% | best place [o], darling [o], jewel [B], jewels [B], more rare [o], most rare [o], precious things [B], rare [o], treasures [B] |
| M18 Desire & Longing | M18_striving Striving after | 1 | 1 | 0 | 0 | 0 | 0% |  |
| M18 Desire & Longing | M18_thirst Thirst, hunger | 6 | 0 | 6 | 0 | 0 | 0% |  |
| M18 Desire & Longing | M18_will Will, wish, choosing, willingness | 74 | 14 | 32 | 2 | 26 | 38% | aim [o], anyone would [o], deliberately [o], freely offers [o], freewill offerings [B], he would [o], human will [o], i would [o], let [o], mean [o], offerings [B], please [o] … +16 |
| M18 Desire & Longing | M18_zeal Jealousy, zeal, envy | 13 | 1 | 12 | 0 | 0 | 0% |  |
| M19 Trust & Refuge | M19_believing Believing | 8 | 3 | 4 | 1 | 0 | 12% | believers [B] |
| M19 Trust & Refuge | M19_refuge Refuge, stronghold | 15 | 5 | 4 | 6 | 0 | 40% | fortress [B], fortresses [B], refuge [B], rock [B], strongest fortresses [B], strongholds [B] |
| M19 Trust & Refuge | M19_security Security, safety | 10 | 0 | 10 | 0 | 0 | 0% |  |
| M19 Trust & Refuge | M19_trust Trust, reliance, confidence | 26 | 3 | 21 | 2 | 0 | 8% | entrust [B], entrusted [B] |
| M20 Doubt & Discouragement | M20_anxiety Anxiety, worry, discouragement | 18 | 3 | 14 | 0 | 1 | 6% | concerned [o] |
| M20 Doubt & Discouragement | M20_grumbling Grumbling, murmuring | 6 | 5 | 0 | 0 | 1 | 17% | whisperer [o] |
| M20 Doubt & Discouragement | M20_hiding Hiding, concealment | 21 | 6 | 14 | 0 | 1 | 5% | undetected [o] |
| M20 Doubt & Discouragement | M20_perplexity Perplexity, doubt | 6 | 1 | 5 | 0 | 0 | 0% |  |
| M21 Fasting & Piety | M21_asking Asking, inquiring | 32 | 19 | 8 | 1 | 4 | 16% | demand [o], god [B], please [o], question [o], requested [o] |
| M21 Fasting & Piety | M21_entreaty Entreaty, begging | 17 | 14 | 2 | 0 | 1 | 6% | beg [o] |
| M21 Fasting & Piety | M21_fasting Fasting | 1 | 1 | 0 | 0 | 0 | 0% |  |
| M21 Fasting & Piety | M21_godliness Godliness, piety | 5 | 1 | 4 | 0 | 0 | 0% |  |
| M22 Praise & Song | M22_exalting Exalting, magnifying, lifting up | 27 | 6 | 20 | 0 | 1 | 4% | up [o] |
| M22 Praise & Song | M22_glorifying Glorifying | 6 | 3 | 3 | 0 | 0 | 0% |  |
| M22 Praise & Song | M22_glory Glory, honour, splendour | 27 | 3 | 16 | 1 | 7 | 30% | another [o], glorious ones [B], lifter [o], magnificent [o], nobility [o], renowned [o], splendid [o], surpass [o] |
| M22 Praise & Song | M22_praise Praise, blessing | 24 | 11 | 12 | 0 | 1 | 4% | joyously praise [o] |
| M22 Praise & Song | M22_singing Singing, song, music | 42 | 19 | 3 | 8 | 12 | 48% | both men [B], celebration [o], female [B], hymn [o], instruments [B], male [B], melody [o], music [o], musical [o], play [o], psalmist [B], sang responsively [o] … +8 |
| M23 Strength & Courage | M23_ability Ability, being able | 15 | 1 | 11 | 1 | 2 | 20% | could [o], could you [o], power [B] |
| M23 Strength & Courage | M23_army Army, forces, warriors | 17 | 1 | 2 | 11 | 3 | 82% | armed force [o], armies [B], army [B], captains [B], defenses [o], enemies [B], forces [B], host [B], men [B], mighty men [B], mighty throng [o], soldiers [B] … +2 |
| M23 Strength & Courage | M23_compelling Compelling, force | 11 | 6 | 1 | 1 | 3 | 36% | compulsion [o], enforce [o], force [B], urgent [o] |
| M23 Strength & Courage | M23_courage Courage, boldness, valour | 35 | 6 | 17 | 2 | 10 | 34% | bravest [o], courageously [o], dare [o], dared to [o], excellently [o], man [B], presume [o], valiant men [B], valiantly [o], valor [o], venture [o], would dare [o] |
| M23 Strength & Courage | M23_enlarging Enlarging, growing great | 20 | 4 | 16 | 0 | 0 | 0% |  |
| M23 Strength & Courage | M23_firm Firm, steadfast, reliable | 27 | 3 | 23 | 0 | 1 | 4% | takes effect [o] |
| M23 Strength & Courage | M23_hardening Hardening, hardness | 11 | 0 | 10 | 0 | 1 | 9% | hard-faced [o] |
| M23 Strength & Courage | M23_holding Holding, seizing, holding fast | 28 | 15 | 11 | 2 | 0 | 7% | bind [B], robe [B] |
| M23 Strength & Courage | M23_power Power, might, mighty works | 56 | 6 | 27 | 11 | 12 | 41% | active [o], activities [o], activity [o], aid [o], almighty [B], cruelly [o], dominion [B], energy [o], enhances [o], fierce men [o], fiercely [o], force [B] … +11 |
| M23 Strength & Courage | M23_prevailing Prevailing, conquering, overcoming | 24 | 10 | 9 | 0 | 5 | 21% | conquerors [o], defeated [o], defies [o], going against [o], prevail against [o] |
| M23 Strength & Courage | M23_strength Strength, being strong, strengthening | 30 | 0 | 26 | 2 | 2 | 13% | collect [o], must use [o], strong man [B], strong man’s [B] |
| M23 Strength & Courage | M23_subjection Subjection, submission | 12 | 5 | 7 | 0 | 0 | 0% |  |
| M24 Faintness & Despair | M24_affliction Affliction, being afflicted, humbled | 30 | 12 | 14 | 0 | 4 | 13% | harshly [o], inflicted [o], them [o], tormentors [o] |
| M24 Faintness & Despair | M24_breaking Breaking, broken, shattered | 24 | 0 | 19 | 1 | 4 | 21% | breaches [o], crash [o], pieces [B], that [o], wrecked [o] |
| M24 Faintness & Despair | M24_despair Despair, hopelessness | 5 | 0 | 5 | 0 | 0 | 0% |  |
| M24 Faintness & Despair | M24_dismay Dismay, alarm, terror | 15 | 2 | 12 | 0 | 1 | 7% | scare [o] |
| M24 Faintness & Despair | M24_distress Distress, trouble, anguish | 25 | 0 | 22 | 1 | 2 | 12% | calamities [o], discomfort [o], stomach [B] |
| M24 Faintness & Despair | M24_failing Failing the test, worthless | 8 | 2 | 5 | 0 | 1 | 12% | failed the test [o] |
| M24 Faintness & Despair | M24_fainting Fainting, weariness, exhaustion | 43 | 6 | 31 | 0 | 6 | 14% | drop [o], fall helpless [o], lagging [o], out [o], wore themselves [o], yourselves out [o] |
| M24 Faintness & Despair | M24_harm Disaster, harm, calamity | 22 | 10 | 5 | 0 | 7 | 32% | calamities [o], calamity [o], danger [o], disaster [o], disasters [o], down ruin [o], harm [o] |
| M24 Faintness & Despair | M24_oppression Oppression | 17 | 8 | 6 | 3 | 0 | 18% | man [B], oppressor [B], oppressors [B] |
| M24 Faintness & Despair | M24_plunder Plunder, spoil, prey | 7 | 0 | 1 | 2 | 4 | 86% | looter [o], plunder [B], plundered [o], plundering [o], prey [o], spoil [B] |
| M24 Faintness & Despair | M24_poor The poor, the fatherless | 14 | 0 | 6 | 6 | 2 | 57% | become orphans [o], fatherless [B], fatherless child [B], fatherless children [B], orphan [B], orphans [B], torn away [o], without father [B] |
| M24 Faintness & Despair | M24_seizing Seizing, snatching | 10 | 4 | 0 | 3 | 3 | 60% | away [o], caught up [B], force [B], snatch [o], snatched away [B], snatches away [o] |
| M24 Faintness & Despair | M24_suffering Suffering, pain, pangs | 36 | 12 | 17 | 2 | 5 | 19% | ache [o], bring me pain [o], childbirth [B], great pains [o], injured foot [B], labor pains [o], sore [o] |
| M24 Faintness & Despair | M24_toil Toil, labour | 9 | 6 | 3 | 0 | 0 | 0% |  |
| M24 Faintness & Despair | M24_withering Withering, drying up | 21 | 2 | 15 | 0 | 4 | 19% | dries [o], up [o], wither [o], withers [o] |
| M25 Life & Death | M25_death Death | 7 | 0 | 5 | 2 | 0 | 29% | death penalty [B], pestilence [B] |
| M25 Life & Death | M25_dying Dying, being dead | 24 | 1 | 16 | 2 | 5 | 29% | anyone [o], certainly [o], dead man [B], died out [o], man [B], shall [o], you shall [o] |
| M25 Life & Death | M25_killing Killing, putting to death | 21 | 12 | 2 | 2 | 5 | 33% | be [o], it shall [o], men [B], other [o], put her to death [B], put him [o], put me to death [o] |
| M25 Life & Death | M25_life Life, breath | 16 | 2 | 12 | 2 | 0 | 12% | breath [B], breathed [B] |
| M25 Life & Death | M25_living Living, being alive | 45 | 5 | 32 | 0 | 8 | 18% | let [o], lifelong [o], outlived [o], prolong [o], prolongs [o], recovering [o], save alive [o], spare [o] |
| M26 Judgment & Condemnation | M26_clearing Clearing, going unpunished | 14 | 2 | 10 | 0 | 2 | 14% | go unpunished [o], you [o] |
| M26 Judgment & Condemnation | M26_condemning Condemning, condemnation, punishment | 10 | 0 | 8 | 0 | 2 | 20% | penalty [o], sentenced [o] |
| M26 Judgment & Condemnation | M26_contending Contending, pleading a cause | 34 | 15 | 8 | 3 | 8 | 32% | adversaries [B], another [o], berated [o], brought charges [o], case [o], cause [o], court [o], defender [B], fatherless [B], lawsuits [o], rights [o] |
| M26 Judgment & Condemnation | M26_counting Counting, reckoning, regarding | 11 | 2 | 9 | 0 | 0 | 0% |  |
| M26 Judgment & Condemnation | M26_guilt Charge, guilt | 9 | 1 | 6 | 0 | 2 | 22% | accountable [o], charges [o] |
| M26 Judgment & Condemnation | M26_judging Judgment, judging | 6 | 1 | 5 | 0 | 0 | 0% |  |
| M26 Judgment & Condemnation | M26_justifying Justifying, acquitting, vindicating | 19 | 0 | 19 | 0 | 0 | 0% |  |
| M26 Judgment & Condemnation | M26_vengeance Vengeance, avenging, repaying | 25 | 13 | 4 | 2 | 6 | 32% | avenged [o], avenger [B], avenges [o], avenging [o], he shall [o], repaid [o], revengefully [o], vengeance [B] |
| M28 Envy & Greed | M28_envy Envy, rivalry, selfish ambition | 9 | 0 | 8 | 0 | 1 | 11% | rivalries [o] |
| M28 Envy & Greed | M28_greed Greed, covetousness, love of money | 10 | 1 | 8 | 0 | 1 | 10% | gain [o] |
| M28 Envy & Greed | M28_sensuality Sensuality, debauchery, the flesh | 14 | 3 | 6 | 1 | 4 | 36% | flesh [B], luxury [o], revel [o], self-indulgence [o], sings lustful [o] |
| M28 Envy & Greed | M28_whoring Whoring, prostitution, unfaithfulness | 26 | 9 | 6 | 7 | 4 | 42% | loose woman [o], molech [B], prostitute [B], prostitutes [B], prostitute’s [B], prostitution [B], themselves [o], whore [B], whored [o], whores [B], whorings [o] |
| M30 Rebellion & Stubbornness | M30_despising Despising, contempt | 21 | 5 | 11 | 1 | 4 | 24% | belittles [o], disregard [o], disrespectful [o], person [B], presume [o] |
| M30 Rebellion & Stubbornness | M30_forsaking Forsaking, abandoning, leaving | 16 | 8 | 4 | 1 | 3 | 25% | abandon [o], leaves [B], left [o], left me behind [o] |
| M30 Rebellion & Stubbornness | M30_harshness Harshness, hardness | 10 | 1 | 5 | 0 | 4 | 40% | harshly [o], roughly [o], stern [o], unbearable news [o] |
| M30 Rebellion & Stubbornness | M30_rebellion Rebellion, disobedience | 20 | 10 | 9 | 0 | 1 | 5% | revolters [o] |
| M30 Rebellion & Stubbornness | M30_refusing Refusing | 11 | 6 | 2 | 0 | 3 | 27% | have nothing to do with [o], nothing to do [o], refuse [o] |
| M30 Rebellion & Stubbornness | M30_rejecting Rejecting, casting off, spurning | 24 | 8 | 5 | 0 | 11 | 46% | aside [o], cast away [o], cast us off [o], discarded [o], disregards [o], have nothing more to do with [o], off [o], out [o], spurn [o], thwart [o], whoever disregards [o] |
| M30 Rebellion & Stubbornness | M30_restraining Restraining, withholding, shutting up | 26 | 7 | 11 | 1 | 7 | 31% | averted [o], banned [o], detain [o], detained [o], home [o], imprisoned him [B], shut him up [o], shut up [o] |
| M30 Rebellion & Stubbornness | M30_stubbornness Stubbornness, stiff neck, sullenness | 7 | 0 | 6 | 0 | 1 | 14% | impudent [o] |
| M31 Faith | M31_apostasy Apostasy, faithlessness | 9 | 1 | 7 | 0 | 1 | 11% | apostasies [o] |
| M31 Faith | M31_religion Religion | 3 | 1 | 1 | 0 | 1 | 33% | self-made religion [o] |
| M31 Faith | M31_unbelief Unbelief, the unbelieving | 10 | 0 | 8 | 1 | 1 | 20% | disbelieve [o], unbeliever [B] |
| M32 Covenant | M32_circumcision Circumcision | 14 | 3 | 3 | 8 | 0 | 57% | circumcise [B], circumcised [B], circumcision [B], flesh [B], foreskin [B], foreskins [B], he was circumcised [B], remove the marks of circumcision [B] |
| M32 Covenant | M32_covenant Covenant, making a covenant | 10 | 2 | 1 | 2 | 5 | 70% | allies [o], covenant [B], covenants [B], league [o], of [o], terms [o], treaty [o] |
| M33 Rest & Peace | M33_peace Peace | 12 | 3 | 8 | 0 | 1 | 8% | peaceably [o] |
| M33 Rest & Peace | M33_quiet Quiet, stillness, silence | 40 | 13 | 19 | 0 | 8 | 20% | down for [o], hush [o], hushed [o], keep quiet [o], quietly holds [o], quiets [o], say nothing [o], says nothing [o] |
| M33 Rest & Peace | M33_rest Rest, resting place, ease | 23 | 2 | 16 | 1 | 4 | 22% | eased [o], got relief [o], relax [o], respite [o], resting places [B] |
| M33 Rest & Peace | M33_wellbeing Well-being, welfare, safety | 20 | 3 | 10 | 1 | 6 | 35% | any safety [o], flock [B], friends [o], friendship [o], greeting [o], safely [o], well-being [o] |
| M34 Patience & Perseverance | M34_blameless Blameless, complete | 4 | 0 | 3 | 0 | 1 | 25% | he would [o] |
| M34 Patience & Perseverance | M34_endurance Endurance, steadfastness, bearing | 22 | 4 | 16 | 0 | 2 | 9% | put up with [o], with [o] |
| M34 Patience & Perseverance | M34_nobles Nobles, nobility | 14 | 0 | 7 | 5 | 2 | 50% | leaders [B], lords [B], nobility [o], noble birth [o], nobles [B], prince [B], princes [B] |
| M34 Patience & Perseverance | M34_patience Patience, long-suffering | 5 | 0 | 5 | 0 | 0 | 0% |  |
| M34 Patience & Perseverance | M34_striving Striving, struggle | 12 | 9 | 2 | 0 | 1 | 8% | athlete [o] |
| M35 Being Tested | M35_tempting Tempting, temptation | 6 | 4 | 1 | 1 | 0 | 17% | tempter [B] |
| M35 Being Tested | M35_testing Testing, proving, examining | 22 | 5 | 13 | 0 | 4 | 18% | accredit [o], attempted [o], did [o], interpret [o] |
| M35 Being Tested | M35_trials Trials | 5 | 0 | 5 | 0 | 0 | 0% |  |
| M36 Worship & Service | M36_ministry Service, ministry, ministering | 37 | 14 | 8 | 8 | 7 | 41% | administered [o], attending [o], bringing aid [o], deacons [B], distribution [o], duties [o], gift [B], helpers [B], ministers [B], ministry [B], priest [B], ritual duties [o] … +3 |
| M36 Worship & Service | M36_offering Offerings | 13 | 0 | 1 | 12 | 0 | 92% | a burnt offering [B], burnt offering [B], burnt offerings [B], burnt sacrifices [B], grain [B], grain offering [B], grain offerings [B], oblation [B], offering [B], offerings [B], sacrifice [B], sacrificial offering [B] |
| M36 Worship & Service | M36_serving Serving, worshiping a god | 8 | 6 | 0 | 2 | 0 | 25% | lord [B], worshipers [B] |
| M36 Worship & Service | M36_worship Worship, bowing down | 15 | 9 | 1 | 4 | 1 | 33% | bow [B], homage [o], knees [B], worshiper [B], worshipers [B] |
| M37 Firstborn & Foreknowledge | M37_calling Calling, summoning, naming | 15 | 5 | 4 | 1 | 5 | 40% | known as [o], named [B], sent for [o], summon [o], summoned [o], together [o] |
| M37 Firstborn & Foreknowledge | M37_firstborn Firstborn | 9 | 1 | 2 | 4 | 2 | 67% | first child [B], first open [o], first opens [o], first son [B], firstborn [B], son [B] |
| M37 Firstborn & Foreknowledge | M37_foreknowledge Foreknowledge | 2 | 0 | 2 | 0 | 0 | 0% |  |
| M39 Gift & Favor | M39_accepting Accepting, taking pleasure | 25 | 6 | 14 | 0 | 5 | 20% | declined [o], enjoy [o], favorite [o], please [o], popular [o] |
| M39 Gift & Favor | M39_favour Favour, grace | 8 | 0 | 5 | 0 | 3 | 38% | favor in your [o], graceful [o], please [o] |
| M39 Gift & Favor | M39_gifts Gifts, giving | 14 | 2 | 4 | 7 | 1 | 57% | bribe [B], bribes [B], contributed [o], gift [B], gifts [B], offerings [B], payment [B], tribute [B] |
| M39 Gift & Favor | M39_goodwill Goodwill, good pleasure | 8 | 0 | 8 | 0 | 0 | 0% |  |
| M41 Being Heard | M41_answering Answering | 10 | 7 | 1 | 0 | 2 | 20% | addressed [o], daniel [o] |
| M41 Being Heard | M41_hearing Hearing, listening | 39 | 23 | 6 | 3 | 7 | 26% | anyone who [o], attended [o], ear [B], ears [B], have [o], indeed [o], on [o], overheard [o], to [o], us [B] |
| M41 Being Heard | M41_obeying Obeying | 15 | 10 | 2 | 0 | 3 | 20% | indeed [o], strictly [o], you, do [o] |
| M42 Prayer & Petition | M42_calling Calling on, summoning, proclaiming | 37 | 20 | 4 | 1 | 12 | 35% | addressed [o], addressing [o], arms [B], guests [o], issued a proclamation [o], on [o], over [o], proclamation [o], rallied [o], summon [o], summoned [o], summoning [o] … +1 |
| M42 Prayer & Petition | M42_crying Crying out, cry for help | 27 | 23 | 1 | 0 | 3 | 11% | one crying [o], out [o], outcry [o] |
| M42 Prayer & Petition | M42_exhorting Exhorting, urging, comforting | 18 | 10 | 5 | 0 | 3 | 17% | after encouraging [o], appealing [o], exhortations [o] |
| M42 Prayer & Petition | M42_prayer Prayer, praying | 19 | 13 | 2 | 1 | 3 | 21% | fervently [o], i would [o], offering [B], you [o] |
| M42 Prayer & Petition | M42_supplication Supplication, pleading, begging | 40 | 24 | 9 | 0 | 7 | 18% | appeal [o], appealed [o], beg [o], earnestly to [o], mediate [o], pleas [o], wish [o] |
| M42 Prayer & Petition | M42_vocation Calling (vocation) | 5 | 2 | 3 | 0 | 0 | 0% |  |
| M43 Prophecy & Vision | M43_oracle The oracle: 'declares the LORD' | 5 | 3 | 0 | 2 | 0 | 40% | lord [B], oracle [B] |
| M43 Prophecy & Vision | M43_prophesying Prophesying | 10 | 4 | 0 | 3 | 3 | 60% | be the preacher [o], dropped [o], prophecies [B], prophecy [B], prophesies [B], prophetic powers [o] |
| M43 Prophecy & Vision | M43_prophets Prophets | 3 | 0 | 0 | 3 | 0 | 100% | prophet [B], prophets [B], prophet’s [B] |
| M43 Prophecy & Vision | M43_signs Signs | 2 | 0 | 0 | 2 | 0 | 100% | sign [B], signs [B] |
| M44 Covenant & Fellowship | M44_agreeing Agreeing, confessing | 10 | 3 | 5 | 0 | 2 | 20% | agreed [o], consented [o] |
| M44 Covenant & Fellowship | M44_assembly Assembly, congregation, church | 16 | 0 | 1 | 9 | 6 | 94% | assembled [o], assemblies [B], assembly [B], church [B], churches [B], company [B], congregation [B], convocation [o], convocations [o], festal gathering [o], great assembly [B], great congregation [B] … +3 |
| M44 Covenant & Fellowship | M44_betrothal Betrothal | 3 | 0 | 0 | 3 | 0 | 100% | betroth [B], betrothed [B], will betroth [B] |
| M44 Covenant & Fellowship | M44_companionship Companionship, sharing, brotherhood | 16 | 4 | 5 | 3 | 4 | 44% | associated [o], brotherhood [o], companion [B], companions [B], fellow [o], side [B], with him [o] |
| M45 Renewal & Transformation | M45_changing Changing, transforming | 19 | 1 | 11 | 1 | 6 | 37% | alter [B], be different [o], different [o], disguise [o], disguises [o], disguising [o], distort [o] |
| M45 Renewal & Transformation | M45_comforting Comforting, consoling | 15 | 0 | 12 | 2 | 1 | 20% | comforter [B], comforters [B], get relief [o] |
| M45 Renewal & Transformation | M45_covering Covering, concealing | 27 | 3 | 14 | 4 | 6 | 37% | body [B], cover [B], covering [B], let [o], overshadowed [o], overshadowing [o], screen [o], screened [o], swamped [o], wrapped [B] |
| M45 Renewal & Transformation | M45_delivering Delivering, rescuing | 18 | 7 | 9 | 2 | 0 | 11% | deliverer [B], rescue [B] |
| M45 Renewal & Transformation | M45_healing Healing, being made well | 9 | 1 | 6 | 0 | 2 | 22% | cure [o], cured [o] |
| M45 Renewal & Transformation | M45_helping Helping, helper | 14 | 6 | 4 | 2 | 2 | 29% | aid [o], benefited [o], helper [B], helpers [B] |
| M45 Renewal & Transformation | M45_refreshed Refreshed | 1 | 0 | 1 | 0 | 0 | 0% |  |
| M45 Renewal & Transformation | M45_renewing Renewing, the new | 15 | 0 | 12 | 1 | 2 | 20% | fan [o], new world [o], patch [B] |
| M45 Renewal & Transformation | M45_satisfying Satisfying, filling | 15 | 2 | 12 | 0 | 1 | 7% | gorge [o] |
| M45 Renewal & Transformation | M45_saving Saving, salvation, victory | 28 | 2 | 17 | 6 | 3 | 32% | deliverer [B], redeem [B], redeemer [B], rescue [B], safely [o], safely through [o], savior [B], saviors [B], spare [o] |
| M46 Wealth & Riches | M46_inheritance Inheritance, heritage | 6 | 0 | 2 | 4 | 0 | 67% | heritages [B], inheritance [B], inheritances [B], possession [B] |
| M46 Wealth & Riches | M46_money Money, silver | 4 | 0 | 0 | 2 | 2 | 100% | money [o], pieces of silver [B], revenue [o], silver [B] |
| M46 Wealth & Riches | M46_prospering Prospering, succeeding, ease | 18 | 0 | 11 | 0 | 7 | 39% | advanced [o], give success [o], prospered [o], succeed [o], success [o], successful [o], thrive [o] |
| M46 Wealth & Riches | M46_riches Riches, wealth, being rich | 29 | 0 | 14 | 9 | 6 | 52% | acquire wealth [o], delicacies [B], enrich [o], gained wealth [o], goods [B], hoarded [o], luxury [o], men [B], possessions [B], prospered [o], rich man [B], rich man’s [B] … +3 |
| M47 Inner Seat | M47_conscience Conscience | 4 | 0 | 3 | 0 | 1 | 25% | consciousness [o] |
| M47 Inner Seat | M47_flesh Flesh, body | 13 | 0 | 1 | 10 | 2 | 92% | and [o], another [o], belly [B], bodies [B], bodily [B], body [B], entrails [B], flesh [B], physical [B], same body [B], stomach [B], stomachs [B] |
| M47 Inner Seat | M47_heart Heart, mind | 60 | 6 | 40 | 5 | 9 | 23% | breast [B], encouragingly [o], from [o], him [o], himself [o], irresolute [o], me [B], myself [B], planned [o], soul [B], themselves [o], yours [B] … +2 |
| M47 Inner Seat | M47_life_self Life, self, person, breath | 69 | 5 | 26 | 14 | 24 | 55% | and they [o], and your [o], another [o], anyone [o], breath [B], everyone [o], forfeit [o], he [o], herself [o], himself [o], human being [B], i [o] … +26 |
| M47 Inner Seat | M47_soul Soul | 20 | 1 | 12 | 6 | 1 | 35% | he [o], me [B], myself [B], soul [B], souls [B], soul’s [B], spirit [B] |
| M47 Inner Seat | M47_spirit Spirit, spiritual | 17 | 1 | 10 | 3 | 3 | 35% | has the [o], i [o], no [o], spirit [B], spirits [B], spiritual gifts [B] |
| M48 Astonishment & Wonder | M48_marvelling Marvelling, astonishment, amazement | 16 | 3 | 8 | 0 | 5 | 31% | astonishing things [o], surprised [o], trance [o], wonder [o], wondering [o] |
| M48 Astonishment & Wonder | M48_wonders Wonders, signs, wondrous works | 23 | 0 | 10 | 5 | 8 | 57% | extraordinary [o], miracle [o], miracles [o], portent [o], portents [o], sign [B], things [B], upon wonder [o], wonder [o], wonderful deeds [B], wondrous deeds [B], wondrous works [B] … +1 |
| M49 Thanksgiving | A_thanksgiving_act The verbal act of giving thanks | 6 | 6 | 0 | 0 | 0 | 0% |  |
| M49 Thanksgiving | B_thankfulness_state The noun-named state and expression of gratitude | 4 | 2 | 1 | 0 | 1 | 25% | thanksgivings [o] |
| M49 Thanksgiving | C_thankful_disposition The settled character-trait of being thankful | 1 | 0 | 1 | 0 | 0 | 0% |  |
| M49 Thanksgiving | D_yadah_praise_confess Outward-cast acknowledgment: praise and confession | 22 | 17 | 1 | 1 | 3 | 18% | down [o], shoot [B], thanks to [o], thanksgiving and [o] |
| M49 Thanksgiving | E_todah_offering_noun The instituted noun-form of thanksgiving: hymn, ch | 8 | 4 | 1 | 1 | 2 | 38% | songs [o], thank offerings [B], thanksgivings [o] |
| M50 Grace & Mercy | M50_chesed Steadfast love, kindness, loyalty | 18 | 3 | 14 | 0 | 1 | 6% | loyally [o] |
| M50 Grace & Mercy | M50_forgiving Forgiving, granting freely | 8 | 3 | 2 | 0 | 3 | 38% | cancelled [o], debt [o], granted [o] |
| M50 Grace & Mercy | M50_grace Grace, favour, graciousness | 21 | 0 | 16 | 0 | 5 | 24% | gracious thing [o], graciously [o], granted [o], winning [o], won [o] |
| M50 Grace & Mercy | M50_mercy Mercy, compassion, pity | 27 | 3 | 21 | 0 | 3 | 11% | mercy on [o], ruthless [o], spare [o] |
| M50 Grace & Mercy | M50_partiality Partiality, showing favour, accepting | 11 | 2 | 7 | 1 | 1 | 18% | me [B], toward [o] |
| M50 Grace & Mercy | M50_pleading Pleading for grace | 9 | 7 | 2 | 0 | 0 | 0% |  |
| M51 Love & Devotion | M51_love Love | 17 | 5 | 9 | 1 | 2 | 18% | friend [B], loved one [o], lovely [o] |
| M52 Encouragement | M52_building_up Building up, edification | 11 | 4 | 3 | 2 | 2 | 36% | building [B], built [B], up [o], upbuilding [o] |
| M52 Encouragement | M52_encouragement Encouragement, comfort, exhortation | 10 | 1 | 8 | 0 | 1 | 10% | appeal [o] |
| M53 Dishonor & Disgrace | M53_brought_low Brought low, abased | 11 | 1 | 8 | 0 | 2 | 18% | bring down [o], down [o] |
| M53 Dishonor & Disgrace | M53_filth Filth, filthiness | 8 | 0 | 5 | 1 | 2 | 38% | dirt [o], dung [B], shabby [o] |
| M53 Dishonor & Disgrace | M53_indecency Indecency, exposure, mutilation | 4 | 0 | 2 | 1 | 1 | 50% | flesh [B], shameless acts [o] |
| M53 Dishonor & Disgrace | M53_reviling Taunting, reviling, insult | 25 | 21 | 2 | 0 | 2 | 8% | revilings [o], taunter [o] |
| M53 Dishonor & Disgrace | M53_silenced Mute, silenced | 8 | 1 | 5 | 2 | 0 | 25% | mute man [B], muzzle [B] |
| M54 Torah & Obedience | M54_commandments Commandments | 6 | 2 | 1 | 2 | 1 | 50% | commandment [B], commandments [B], obligation [o] |
| M54 Torah & Obedience | M54_law Law, instruction | 12 | 6 | 3 | 2 | 1 | 25% | law [B], laws [B], legal [o] |
| M55 Destruction & Ruin | M55_appalled Appalled, horrified | 8 | 1 | 5 | 0 | 2 | 25% | fate [o], horrified [o] |
| M55 Destruction & Ruin | M55_corrupting Corrupting, acting corruptly | 10 | 0 | 7 | 0 | 3 | 30% | corrupt practices [o], corruptly [o], deal corruptly [o] |
| M55 Destruction & Ruin | M55_desolation Desolation, ruin, waste | 17 | 0 | 10 | 0 | 7 | 41% | crash [o], devastation [o], harmful [o], heap [o], storm [o], waste [o], wasted [o] |
| M55 Destruction & Ruin | M55_destroying Destroying, the destroyer | 46 | 8 | 13 | 10 | 15 | 54% | abaddon [B], abolish [o], and destroy [o], battering [o], cut off [B], destroyer [B], destroyers [B], destroying them [B], destroys them [B], devastate [o], extinction [o], laid waste [o] … +13 |
| M55 Destruction & Ruin | M55_devoted Devoted to destruction | 17 | 4 | 3 | 9 | 1 | 59% | complete destruction [B], devote to destruction [B], devoted for destruction [B], devoted thing [B], devoted things [B], forfeited [o], thing [B], thing for destruction [B], utter destruction [B], utterly destroy [B] |
| M55 Destruction & Ruin | M55_idolatry Idols, idolatry | 15 | 0 | 0 | 15 | 0 | 100% | carved [B], carved idols [B], carved image [B], carved images [B], figure [B], idol [B], idolater [B], idolaters [B], idolatry [B], idols [B], image [B], images [B] … +3 |
| M55 Destruction & Ruin | M55_ungodliness Ungodliness, wrongdoing | 4 | 1 | 3 | 0 | 0 | 0% |  |
| M56 Sin & Guilt | M56_guilt Guilt, bearing iniquity, punishment | 27 | 6 | 14 | 0 | 7 | 26% | bore [o], done [o], go unpunished [o], incur [o], indeed [o], penalty [o], thereby become [o] |
| M56 Sin & Guilt | M56_immorality Sexual immorality | 6 | 2 | 3 | 0 | 1 | 17% | did [o] |
| M56 Sin & Guilt | M56_iniquity Iniquity | 7 | 2 | 5 | 0 | 0 | 0% |  |
| M56 Sin & Guilt | M56_offerings Sin and guilt offerings | 14 | 2 | 6 | 5 | 1 | 43% | compensation [o], guilt offering [B], guilt offerings [B], offering [B], sin offering [B], sin offerings [B] |
| M56 Sin & Guilt | M56_sin Sin, sinning, sinners | 20 | 10 | 9 | 0 | 1 | 5% | done [o] |
| M56 Sin & Guilt | M56_transgression Transgression, trespass | 24 | 16 | 6 | 0 | 2 | 8% | goes on ahead [o], treason [o] |
| M57 Corruption & Perversion | M57_adultery Adultery | 11 | 5 | 3 | 3 | 0 | 27% | adulterer [B], adulteress [B], adulteresses [B] |
| M57 Corruption & Perversion | M57_apostasy Apostasy, forsaking | 3 | 2 | 1 | 0 | 0 | 0% |  |
| M57 Corruption & Perversion | M57_corruption Corruption, decay, the perishable | 10 | 0 | 9 | 1 | 0 | 10% | perishable [B] |
| M57 Corruption & Perversion | M57_perversion Perversion, twisting, subverting | 31 | 7 | 13 | 0 | 11 | 35% | away [o], misleading [o], overthrows [o], perversion [o], seem tortuous [o], subvert [o], subverts [o], tortuous [o], twist [o], twisted things [o], wily [o] |
| M57 Corruption & Perversion | M57_unfaithfulness Unfaithfulness, breach of faith | 29 | 8 | 16 | 0 | 5 | 17% | breach [o], breach of faith [o], faithlessly [o], treacherously [o], treachery [o] |
| M58 Wickedness | M58_abomination Abomination, detestable things | 18 | 0 | 10 | 5 | 3 | 44% | abominable practices [o], abominable thing [B], abominations [B], despicable [o], despicable practices [o], detestable idols [B], detestable things [B], idol [B] |
| M58 Wickedness | M58_blasphemy Blasphemy, reviling | 27 | 16 | 3 | 2 | 6 | 30% | abusive [o], blasphemer [B], blasphemers [B], denounced [o], derided [o], malign [o], railed [o], slanderously [o] |
| M58 Wickedness | M58_evil Evil | 6 | 1 | 2 | 2 | 1 | 50% | evil one [B], evil things [o], evils [B] |
| M58 Wickedness | M58_harm Harm, trouble, disaster | 45 | 9 | 16 | 0 | 20 | 44% | bad things [o], badly [o], bring disaster [o], brought calamity [o], calamity [o], deal worse [o], disaster [o], disastrous [o], harm [o], harmful [o], harshly [o], misfortune [o] … +8 |
| M58 Wickedness | M58_lewdness Lewdness, depravity | 5 | 0 | 2 | 0 | 3 | 60% | done [o], lewd [o], lewdly [o] |
| M58 Wickedness | M58_malice Malice | 2 | 0 | 2 | 0 | 0 | 0% |  |
| M58 Wickedness | M58_wickedness Wickedness, the wicked | 64 | 14 | 42 | 1 | 7 | 12% | done great [o], evil things [o], evils [B], heinous crime [o], iniquitous [o], seems wrong [o], villainy [o], wretches [o] |
| M59 Release & Reconciliation | M59_divorce Divorce | 2 | 0 | 0 | 2 | 0 | 100% | divorce [B], woman divorced [B] |
| M59 Release & Reconciliation | M59_forsaking Forsaking, casting off, neglecting | 17 | 8 | 5 | 0 | 4 | 24% | away [o], forgo [o], left [o], neglected [o] |
| M59 Release & Reconciliation | M59_leaving Leaving, departing, withdrawing | 14 | 4 | 2 | 1 | 7 | 57% | away [o], going aside [o], leaves [B], left [o], quit [o], say farewell [o], took leave [o], went away [o] |
| M59 Release & Reconciliation | M59_permitting Permitting, letting, allowing | 9 | 2 | 1 | 0 | 6 | 67% | allowed [o], consented [o], go on [o], have [o], let [o], permit [o] |
| M59 Release & Reconciliation | M59_reconciliation Reconciliation | 6 | 0 | 5 | 0 | 1 | 17% | terms [o] |
| M59 Release & Reconciliation | M59_releasing Releasing, dismissing, sending off | 21 | 7 | 9 | 0 | 5 | 24% | away [o], dismissed [o], left [o], sent off [o], sent them off [o] |
| M60 Confession & Forgiveness | M60_atonement Atonement | 8 | 2 | 6 | 0 | 0 | 0% |  |
| M60 Confession & Forgiveness | M60_confession Confession, acknowledging | 9 | 5 | 4 | 0 | 0 | 0% |  |
| M60 Confession & Forgiveness | M60_forgiveness Forgiveness, pardon | 13 | 4 | 7 | 0 | 2 | 15% | at all [o], canceling [o] |
| M61 Purity & Holiness | M61_clean Clean, pure, cleansing | 31 | 5 | 22 | 1 | 3 | 13% | clean thing [o], pronounce [o], purifier [B], staining [o] |
| M61 Purity & Holiness | M61_consecrating Consecrating, sanctifying | 20 | 2 | 16 | 1 | 1 | 10% | apart [o], consecrated ones [B] |
| M61 Purity & Holiness | M61_holy Holy, holiness, the Holy One | 28 | 0 | 10 | 17 | 1 | 64% | consecrated offerings [B], consecrated things [B], dedicated things [B], gifts [B], holy donations [B], holy food [B], holy gift [B], holy land [B], holy name [B], holy offerings [B], holy one [B], holy thing [B] … +6 |
| M61 Purity & Holiness | M61_saints Saints | 5 | 0 | 1 | 3 | 1 | 80% | holy ones [B], ones [o], saint [B], saints [B] |
| M61 Purity & Holiness | M61_sanctuary Sanctuary | 3 | 0 | 0 | 3 | 0 | 100% | holy place [B], sanctuary [B], sanctuary’s [B] |
| M61 Purity & Holiness | M61_unblemished Without blemish, perfect | 4 | 0 | 2 | 1 | 1 | 50% | blemish [B], defect [o] |
| M62 Truth & Sincerity | M62_certainty Certainty, what stands sure | 7 | 0 | 7 | 0 | 0 | 0% |  |
| M62 Truth & Sincerity | M62_confirming Confirming, establishing | 9 | 0 | 8 | 0 | 1 | 11% | attested [o] |
| M62 Truth & Sincerity | M62_irrevocable Irrevocable, without regret | 2 | 0 | 2 | 0 | 0 | 0% |  |
| M62 Truth & Sincerity | M62_sincerity Sincerity, soundness, singleness | 5 | 0 | 5 | 0 | 0 | 0% |  |
| M62 Truth & Sincerity | M62_straight Straight, right | 5 | 0 | 5 | 0 | 0 | 0% |  |
| M63 Reasoning & Interpretation | M63_counsel Counsel, advising, planning | 25 | 7 | 8 | 3 | 7 | 40% | advice [o], advise [o], advisers [B], agreed together [o], conspire [o], consult together [o], counseled [o], counselor [B], counselors [B], planned [o] |
| M63 Reasoning & Interpretation | M63_doubt Doubt, making distinction | 9 | 0 | 8 | 0 | 1 | 11% | hesitation [o] |
| M63 Reasoning & Interpretation | M63_ignorance Ignorance, not knowing | 14 | 0 | 11 | 0 | 3 | 21% | unaware [o], uninformed [o], unknown [o] |
| M63 Reasoning & Interpretation | M63_interpretation Interpretation | 10 | 1 | 3 | 1 | 5 | 60% | interpret [o], interpretation [o], interpretations [o], interprets [o], translated [B], translation [o] |
| M63 Reasoning & Interpretation | M63_judging Judging, judgment, vindicating | 56 | 19 | 28 | 3 | 6 | 16% | accuser [B], cause [o], decide between [o], decree [B], give sentence [o], law [B], pronounce [o], reached [o], rights [o] |
| M63 Reasoning & Interpretation | M63_mind Mind, thinking, discernment | 24 | 5 | 15 | 0 | 4 | 17% | concern [o], concerned [o], harmony [o], view [o] |
| M63 Reasoning & Interpretation | M63_reasoning Reasoning, disputing, questioning | 31 | 11 | 9 | 0 | 11 | 35% | argument [o], argumentative [o], contradict [o], controversies [o], discussed [o], discussing [o], disputes [o], opinions [o], question [o], questioning [o], questions [o] |
| M63 Reasoning & Interpretation | M63_ruling Ruling, governing | 8 | 2 | 2 | 3 | 1 | 50% | govern [o], magistrates [B], ruler [B], rulers [B] |
| M64 Will & Resolve | M64_choosing Choosing, the chosen | 13 | 6 | 1 | 3 | 3 | 46% | best [o], choice men [B], chosen one [B], chosen ones [B], preferred [o], rather [o] |
| M64 Will & Resolve | M64_counting Counting, esteeming, regarding | 15 | 1 | 11 | 0 | 3 | 20% | calculate [o], classified [o], itself [o] |
| M64 Will & Resolve | M64_dedicating Dedicating, setting apart | 11 | 3 | 6 | 1 | 1 | 18% | dedicated gifts [B], donor [o] |
| M64 Will & Resolve | M64_devising Devising, planning, purposing | 42 | 10 | 22 | 1 | 9 | 24% | aim in life [o], decision [o], deliberate [o], formed [B], have [o], imagine [o], inventing [o], planned [o], plot [o], propose [o] |
| M64 Will & Resolve | M64_skill Skill, artistic design | 7 | 2 | 1 | 1 | 3 | 57% | designer [o], invent [o], skillful men [B], skillfully [o] |
| M64 Will & Resolve | M64_willing Willing, wanting, consenting | 35 | 8 | 15 | 0 | 12 | 34% | and would [o], desired to [o], he will [o], he would [o], i would [o], refuse [o], they would [o], to his will [o], wish [o], wishes [o], would [o], yet you would [o] |
| M65 Speech & Tongue | M65_command Command, the word of the mouth | 15 | 3 | 3 | 5 | 4 | 60% | as [o], commandment [B], commandments [B], decree [B], demand [o], direction [o], orders [B], what [o], word [B] |
| M65 Speech & Tongue | M65_preaching Preaching the good news | 12 | 7 | 1 | 1 | 3 | 33% | announced [o], gospel [B], gospel beforehand [o], news [o] |
| M65 Speech & Tongue | M65_promising Promising | 15 | 3 | 7 | 1 | 4 | 33% | decision [o], decree [B], foretold [o], passed [o], pronounced [o] |
| M65 Speech & Tongue | M65_speaking Speaking, saying, talking | 47 | 29 | 6 | 0 | 12 | 26% | addressed [o], conferred [o], eloquent [o], it [o], mentioned [o], on [o], persistently [o], rash [o], recited [o], speaker [o], this [o], to [o] |
| M65 Speech & Tongue | M65_telling Telling, declaring | 47 | 22 | 11 | 1 | 13 | 30% | another [o], could explain [o], describe [o], fully [o], inform [o], informs against [o], made it clear [o], oracles [B], pronounce [o], related [o], repeated [o], report [o] … +2 |
| M65 Speech & Tongue | M65_word Word, words, saying | 66 | 16 | 18 | 5 | 27 | 48% | advice [o], by [o], concerning [o], dictation [o], everything [o], it [o], letter [B], matter [o], mean [o], message [o], messages [o], news [o] … +20 |
| M66 Madness & Recklessness | M66_madness Madness, being out of one's mind | 9 | 0 | 6 | 0 | 3 | 33% | insane [o], madman [o], madmen [o] |
| M66 Madness & Recklessness | M66_recklessness Recklessness, rashness | 5 | 0 | 1 | 0 | 4 | 80% | furiously [o], rash [o], reckless [o], recklessness [o] |
| M67 Sloth & Diligence | M67_A_dispositional_idleness Idleness as inert state or condition | 9 | 0 | 3 | 0 | 6 | 67% | careless [o], idle [o], idlers [o], indolence [o], ineffective [o], slack [o] |
| M67 Sloth & Diligence | M67_B_dereliction_of_duty Failure to fulfill an entrusted obligation | 3 | 0 | 2 | 0 | 1 | 33% | idle [o] |
| M67 Sloth & Diligence | M67_C_earnest_diligence Zealous, energetic application to a task or relati | 9 | 2 | 5 | 0 | 2 | 22% | do your best [o], effort [o] |
| M67 Sloth & Diligence | M67_D_administrative_thoroughness Exact, complete execution of an official command | 4 | 1 | 2 | 0 | 1 | 25% | strictly [o] |
| M68 Hope & Waiting | M68_hope Hope | 11 | 0 | 10 | 0 | 1 | 9% | hope to [o] |
| M68 Hope & Waiting | M68_waiting Waiting, expecting, looking for | 23 | 10 | 11 | 0 | 2 | 9% | delay [o], suspense [o] |
| M69 Self-Control & Zeal | M69_self_control Self-control, discipline | 3 | 0 | 3 | 0 | 0 | 0% |  |
| M69 Self-Control & Zeal | M69_sobriety Sobriety, sober-mindedness | 2 | 0 | 2 | 0 | 0 | 0% |  |
| M69 Self-Control & Zeal | M69_zeal Zeal, eagerness, earnestness | 16 | 4 | 11 | 0 | 1 | 6% | do your best [o] |
| M70 Lifting & Bearing | M70_laying_hands Laying on of hands | 3 | 1 | 1 | 0 | 1 | 33% | lay [o] |
| M70 Lifting & Bearing | M70_lifting Lifting the hand, swearing | 10 | 5 | 4 | 0 | 1 | 10% | up [o] |
| M70 Lifting & Bearing | M70_tidings Bearing tidings, good news | 6 | 2 | 2 | 0 | 2 | 33% | news [o], publish [o] |
| M70 Lifting & Bearing | M70_upholding Upholding, supporting, sustaining | 19 | 2 | 16 | 0 | 1 | 5% | up [o] |
| M71 Glory & Splendor | M71_celebrating Celebrating, keeping a feast | 12 | 7 | 2 | 0 | 3 | 25% | celebrate [o], keeping festival [o], merry [o] |
| M71 Glory & Splendor | M71_greatness Greatness | 3 | 0 | 3 | 0 | 0 | 0% |  |
| M71 Glory & Splendor | M71_honour Honour, honouring | 10 | 1 | 9 | 0 | 0 | 0% |  |
| M71 Glory & Splendor | M71_splendour Majesty, splendour, glory | 13 | 0 | 10 | 0 | 3 | 23% | magnificent [o], splendid [o], stately [o] |
| M71 Glory & Splendor | M71_worthiness Worthiness, deserving | 12 | 1 | 6 | 0 | 5 | 42% | advisable [o], deserve [o], deserved [o], deserves [o], presume [o] |
| M72 Authority & Dominion | M72_authority Authority | 12 | 2 | 2 | 5 | 3 | 67% | authorities [B], authority over [B], cosmic powers [B], domain [B], exercised authority [o], jurisdiction [o], power [B], rightful claim [o] |
| M72 Authority & Dominion | M72_hand Hand as power | 21 | 3 | 3 | 7 | 8 | 71% | buyer [o], custody [B], direction [o], directions [o], dominion [B], hand [B], hands [B], his [o], king [B], leadership [o], possession [B], power [B] … +3 |
| M72 Authority & Dominion | M72_hosts Hosts (the LORD of hosts) | 3 | 0 | 0 | 3 | 0 | 100% | armies [B], hosts [B], lord [B] |
| M72 Authority & Dominion | M72_king King, reigning | 34 | 5 | 9 | 14 | 6 | 59% | became king [B], dominion [B], has dominion over [B], king [B], kings [B], king’s [B], made her queen [B], made him king [B], made me king [B], made you king [B], make him king [B], make me king [o] … +8 |
| M72 Authority & Dominion | M72_kingdom Kingdom | 14 | 2 | 1 | 7 | 4 | 79% | again rule [o], dominion [B], dominions [B], establishment [o], get dominion [B], government [o], kingdom [B], kingdoms [B], kingship [B], realm [o], royal power [B] |
| M72 Authority & Dominion | M72_master Master, lord | 15 | 0 | 3 | 7 | 5 | 80% | domineering [o], exercise lordship [o], lord [B], lord it [o], lorded [o], lords [B], master [B], masters [B], master’s [B], over [o], owner [B], owners [B] |
| M72 Authority & Dominion | M72_rulers Princes, officials, commanders, heads | 38 | 5 | 1 | 24 | 8 | 84% | authorities [B], became commander [B], became their commander [B], captain [B], captains [B], chiefs [B], commander [o], commanders [B], directors [o], general [o], governor [B], governors [B] … +20 |
| M72 Authority & Dominion | M72_throne Throne | 7 | 0 | 1 | 6 | 0 | 86% | royal [B], rulers [B], seat [B], seats [B], throne [B], thrones [B] |
| M73 Sickness & Weakness | M73_blindness Blindness | 6 | 1 | 2 | 2 | 1 | 50% | blind man [B], blind men [B], blinds [o] |
| M73 Sickness & Weakness | M73_crippled Crippled, incurable | 4 | 0 | 3 | 0 | 1 | 25% | incurable [o] |
| M73 Sickness & Weakness | M73_leprosy Leprosy | 5 | 0 | 0 | 5 | 0 | 100% | leper [B], lepers [B], leprous [B], leprous disease [B], leprous person [B] |
| M73 Sickness & Weakness | M73_sickness Sickness, disease, illness | 33 | 0 | 21 | 2 | 10 | 36% | became ill [o], disabling [o], diseases [B], fallen sick [o], fever [o], having seizures [o], invalid for [o], invalids [o], seizures [o], sickbed [o], unwell [o], wasting disease [B] |
| M73 Sickness & Weakness | M73_weakness Weakness, languishing | 29 | 2 | 26 | 0 | 1 | 3% | themselves out [o] |
| M74 Keeping & Guarding | M74_attending Paying attention, devoting oneself, beware | 10 | 6 | 2 | 0 | 2 | 20% | eyes on [o], watch out [o] |
| M74 Keeping & Guarding | M74_careful Being careful, taking care | 15 | 6 | 6 | 1 | 2 | 20% | looks well [o], mark [B], whoever [o] |
| M74 Keeping & Guarding | M74_charge Charge, duty, office | 18 | 6 | 5 | 3 | 4 | 39% | duties [o], guard duty [o], guards [B], have [o], offices [B], over [o], posts [B] |
| M74 Keeping & Guarding | M74_guarding Guarding, protecting, preserving | 41 | 11 | 21 | 6 | 3 | 22% | bodyguard [o], guards [B], in [o], keeper [B], keepers [B], saved himself [o], watchman [B], watchmen [B], watchtower [B] |
| M74 Keeping & Guarding | M74_keeping Keeping, observing (commands) | 12 | 9 | 1 | 0 | 2 | 17% | careful to [o], observance [o] |
| M74 Keeping & Guarding | M74_watching Watching, watchman, staying awake | 33 | 16 | 10 | 4 | 3 | 21% | eyed [o], post [o], watcher [B], watchman [B], watchman’s [B], watchmen [B], watchpost [o] |
| M75 Disobedience & Lawlessness | M75_disobedience Disobedience, insubordination | 5 | 0 | 3 | 0 | 2 | 40% | insubordinate [o], insubordination [o] |
| M75 Disobedience & Lawlessness | M75_hardening Hardening, heaviness of heart | 8 | 0 | 8 | 0 | 0 | 0% |  |
| M75 Disobedience & Lawlessness | M75_lawlessness Lawlessness, the lawless | 11 | 4 | 6 | 1 | 0 | 9% | lawless one [B] |
| M76 Walk & Conduct | M76_astray Going astray, staggering | 30 | 11 | 12 | 1 | 6 | 23% | deceiver [B], did [o], mistake [o], reel [o], stagger [o], unintentionally [o], wander about [o] |
| M76 Walk & Conduct | M76_led Being led, conducted | 6 | 5 | 0 | 0 | 1 | 17% | led forth [o] |
| M76 Walk & Conduct | M76_wandering Fleeing, wandering | 17 | 8 | 2 | 1 | 6 | 41% | flee away [o], flight [o], flitting [o], fly away [o], fugitive [o], fugitives [B], wanderer [o] |
| M76 Walk & Conduct | M76_way Way, ways, conduct | 13 | 6 | 2 | 1 | 4 | 38% | behavior [o], course [o], path [B], undertakings [o], walk among [o] |
| M77 Stumbling & Trial | M77_enticing Enticing, being deceived | 9 | 5 | 1 | 0 | 3 | 33% | allure [o], flattered [o], misleading [o] |
| M77 Stumbling & Trial | M77_persuading Persuading, being sure, trusting | 21 | 9 | 11 | 0 | 1 | 5% | advice [o] |
| M77 Stumbling & Trial | M77_stumbling Stumbling, offence, falling away | 34 | 15 | 11 | 2 | 6 | 24% | away [o], create obstacles [o], down [o], obstacle [o], obstruction [o], stagger [o], stumbling block [B], stumbling blocks [B] |
| M77 Stumbling & Trial | M77_trials Trials | 1 | 0 | 1 | 0 | 0 | 0% |  |
| M78 Slavery & Bondage | M78_burden Burden, load | 13 | 4 | 7 | 1 | 1 | 15% | burden-bearers [B], pressure [o] |
| M78 Slavery & Bondage | M78_servant Servant, slave, serving | 23 | 8 | 4 | 10 | 1 | 48% | bondservant [B], bondservants [B], fellow servant [B], fellow servants [B], female servants [B], forced labor [o], servant [B], servants [B], servant’s [B], slave [B], slaves [B] |
| M79 Salvation & Ransom | M79_avenger The avenger of blood | 1 | 0 | 0 | 1 | 0 | 100% | avenger [B] |
| M79 Salvation & Ransom | M79_redeeming Redeeming, ransom | 6 | 0 | 2 | 4 | 0 | 67% | ransom [B], ransomed [B], redeem [B], redeems [B] |
| M79 Salvation & Ransom | M79_salvation Salvation, Saviour | 11 | 2 | 8 | 1 | 0 | 9% | savior [B] |
| M80 Blessing | M80_blessedness Blessed (happy, fortunate) | 11 | 0 | 10 | 0 | 1 | 9% | happier [o] |
| M80 Blessing | M80_blessing Blessing, blessed (by another) | 17 | 6 | 8 | 1 | 2 | 18% | bless her [o], have [o], me [B] |
| M81 Memory (act) | M81_forgetting Forgetting | 10 | 2 | 4 | 0 | 4 | 40% | forgot [o], forgot the [o], live unforgotten [o], unmindful [o] |
| M81 Memory (act) | M81_remembering Remembering, remembrance | 24 | 7 | 10 | 0 | 7 | 29% | and did [o], invoke [o], lay [o], make mention [o], mention [o], mentioned [o], of them but you shall [o] |
| M82 Reminder & Report | M82_reminding Reminding, remembrance | 13 | 5 | 6 | 0 | 2 | 15% | mention [o], mentioning [o] |
| M82 Reminder & Report | M82_report News, report, fame, rumour | 9 | 2 | 0 | 2 | 5 | 78% | fame [o], message [o], news [o], report [o], rumor [o], us [B], word [B] |
| M82 Reminder & Report | M82_warning Warning, solemn charge | 14 | 8 | 4 | 0 | 2 | 14% | solemnly [o], you [o] |
| M82 Reminder & Report | M82_witness Witness, testimony | 20 | 10 | 8 | 0 | 2 | 10% | reputation [o], well spoken [o] |
| M83 Seeking & Inquiring | A_general_seeking Generic active seeking/searching | 39 | 29 | 5 | 0 | 5 | 13% | beg [o], demand [o], investigated [o], of [o], out [o] |
| M83 Seeking & Inquiring | B_intensified_seeking Intensive/exhaustive seeking and demanding | 13 | 7 | 6 | 0 | 0 | 0% |  |
| M83 Seeking & Inquiring | C_hostile_pursuit Seeking with lethal or hostile intent | 1 | 0 | 1 | 0 | 0 | 0% |  |
| M83 Seeking & Inquiring | D_consultative_inquiry Formal consultation and diligent inquiry | 35 | 21 | 10 | 0 | 4 | 11% | avenges [o], cares for [o], indeed [o], inquirer [o] |
| M84 Outcry & Shouting | M84_calling Calling, calling out | 8 | 5 | 3 | 0 | 0 | 0% |  |
| M84 Outcry & Shouting | M84_murmuring Murmuring, meditating, moaning | 15 | 13 | 2 | 0 | 0 | 0% |  |
| M84 Outcry & Shouting | M84_outcry Outcry, crying out | 9 | 5 | 1 | 1 | 2 | 33% | clamor [o], outcry [o], voice [B] |
| M84 Outcry & Shouting | M84_roaring Roaring, growling, groaning | 17 | 12 | 1 | 0 | 4 | 24% | beating wildly [o], howling [o], thunder [o], thundering [o] |
| M84 Outcry & Shouting | M84_shouting Shouting, joyful noise, triumph | 26 | 11 | 6 | 0 | 9 | 35% | against [o], battle cry [o], blast [o], call to battle [o], joyful noise [o], joyful shouting [o], loud [o], shoutings [o], war cry [o] |
| M84 Outcry & Shouting | M84_sound Sound, noise, uproar | 18 | 1 | 2 | 2 | 13 | 83% | crashing [o], instruments [B], loud [o], loud clashing [o], noise [o], noisy streets [o], rumbling [o], rumblings [o], sounded [o], thunderings [o], tone [o], trumpet call [o] … +3 |
| M85 Other Beings | M85_angel_nt Angels: heavenly beings of the New Testament | 5 | 0 | 0 | 5 | 0 | 100% | angel [B], angels [B], angel’s [B], messenger [B], messengers [B] |
| M85 Other Beings | M85_angel_ot Angel: the messenger of God (Hebrew and Aramaic) | 2 | 0 | 0 | 2 | 0 | 100% | angel [B], angels [B] |
| M85 Other Beings | M85_archangels Named archangels | 3 | 0 | 0 | 3 | 0 | 100% | archangel [B], gabriel [B], michael [B] |
| M85 Other Beings | M85_cherubim Cherubim and seraphim | 4 | 0 | 1 | 3 | 0 | 75% | cherub [B], cherubim [B], seraphim [B] |
| M85 Other Beings | M85_demons Demons and demonic oppression | 9 | 0 | 0 | 7 | 2 | 100% | demon [B], demon-oppressed [B], demon-possessed [B], demon-possessed man [B], demonic [B], demons [B], divinities [o], oppressed by demons [B], them [o] |
| M85 Other Beings | M85_devil The Devil: the slanderer | 1 | 0 | 0 | 1 | 0 | 100% | devil [B] |
| M85 Other Beings | M85_dragon The dragon | 1 | 0 | 0 | 1 | 0 | 100% | dragon [B] |
| M85 Other Beings | M85_envoy Human envoys and messengers | 5 | 1 | 0 | 4 | 0 | 80% | ambassadors [B], envoys [B], messenger [B], messengers [B] |
| M85 Other Beings | M85_mediums Mediums, necromancers, divination | 4 | 0 | 0 | 4 | 0 | 100% | divination [B], mediums [B], necromancer [B], necromancers [B] |
| M85 Other Beings | M85_satan Satan: the adversary and accuser | 5 | 1 | 0 | 4 | 0 | 80% | accuser [B], adversary [B], satan [B], satan’s [B] |

`[B]` = judged being, `[o]` = judged other.

## 3. How many groups have missing surfaces

| missing share of the group | groups |
|---|---|
| 0% | 56 |
| 1-24% | 163 |
| 25-49% | 115 |
| 50-74% | 37 |
| 75-99% | 18 |
| 100% | 17 |

Groups of kind group: 406. Distinct surfaces in them: 4840.
