# Strong's codes linked to more than one registry word

> Requested follow-up to `verse-lexical-by-registry-20260810.md` §— that report's
headline noted ‘80 Strong's codes are linked to more than one registry word’ without
listing them. This is that list, in full: every `word_strong.strong` value held by 2+
active `word_registry` words, with the actual words named.

## Context — what this means about `word_registry`'s own integrity model

Confirmed live: `word_registry` is the only table in `iba.db` matching `%registry%` —
there is no separate `registry` table/entity constraining it. Registering a new word IS
just one `INSERT INTO word_registry`. There is one automated overlap check
(`handlers/registry.py:_possible_duplicates`, run on every `New-Word.ps1` call) — but it
only escalates a special warning when an existing word already holds **100% of the new
word's Strong's** (`registry.duplicate_shared_threshold`, default 1.0), and even then it
only *asks* ("register it as a SEPARATE word anyway?") — the researcher can still say
yes. Every *partial* overlap — which is what all 880 rows below are — passes through
with no check or warning at all. That matches the observation: nothing in the schema
prevents, flags, or even surfaces two registry words sharing a Strong's unless they
share literally all of them.

## Distribution — 880 shared Strong's codes, by how many words share them

| words sharing | # Strong's codes |
| --- | --- |
| 9 | 1 |
| 7 | 3 |
| 6 | 10 |
| 5 | 24 |
| 4 | 70 |
| 3 | 185 |
| 2 | 587 |
| **total** | **880** |

## Full list, most-shared first

| Strong's | gloss | language | # words | words |
| --- | --- | --- | --- | --- |
| H2617A | kindness | Hebrew | 9 | compassion,devotion,faith,faithfulness,goodness,grace,kindness,love,mercy |
| G1939 | desire | Greek | 7 | covetousness,desire,longing,lust,passion,flesh,craving |
| H0205G | evil: wickedness | Hebrew | 7 | malice,deceit,evil,iniquity,sin,slander,wickedness |
| H4209 | plot | Hebrew | 7 | deceit,discernment,evil,intention,purpose,thought,devious |
| H0205H | evil: trouble | Hebrew | 6 | distress,evil,iniquity,mourning,sorrow,wickedness |
| H0530 | faithfulness | Hebrew | 6 | faith,faithfulness,honesty,integrity,trust,truthfulness |
| H0998 | understanding | Hebrew | 6 | discernment,insight,knowledge,meaning,understanding,wisdom |
| H1942 | desire | Hebrew | 6 | malice,corruption,desire,evil,lust,craving |
| H2603A | be gracious | Hebrew | 6 | compassion,grace,groaning,kindness,mercy,being |
| H2623 | pious | Hebrew | 6 | faith,faithfulness,holiness,kindness,love,mercy |
| H3190 | be good | Hebrew | 6 | contentment,goodness,kindness,gladness,blessing,being |
| H3372G | to fear | Hebrew | 6 | awe,despair,dread,fear,terror,worship |
| H4603 | be unfaithful | Hebrew | 6 | faith,faithfulness,sin,transgression,treachery,being |
| H5797 | strength | Hebrew | 6 | boldness,hardness,stubbornness,strength,power,might |
| G1937 | to long for | Greek | 5 | covetousness,desire,longing,lust,craving |
| G3600 | be anguished | Greek | 5 | agony,anguish,distress,sorrow,being |
| H0183 | to desire | Hebrew | 5 | covetousness,desire,longing,lust,craving |
| H0539 | be faithful | Hebrew | 5 | endurance,faith,faithfulness,trust,being |
| H0559 | to say | Hebrew | 5 | calling,meditation,purpose,reasoning,thought |
| H1984C | to be foolish | Hebrew | 5 | boastfulness,foolishness,mind,praise,being |
| H2616A | be kind | Hebrew | 5 | faith,faithfulness,kindness,mercy,being |
| H2896A | pleasant | Hebrew | 5 | delight,goodness,kindness,love,gladness |
| H3027H | hand: power | Hebrew | 5 | surrender,strength,power,authority,dominion |
| H3708A | vexation | Hebrew | 5 | anger,grief,indignation,sorrow,wrath |
| H3708B | vexation | Hebrew | 5 | anger,grief,indignation,sorrow,wrath |
| H4578 | belly | Hebrew | 5 | yearning,Soul,heart,spirit,flesh |
| H5162G | to be sorry: comfort | Hebrew | 5 | compassion,mourning,repentance,comfort,being |
| H5162H | to be sorry: relent | Hebrew | 5 | compassion,mind,repentance,comfort,being |
| H5315L | soul: appetite | Hebrew | 5 | appetite,desire,mind,Soul,heart |
| H5810 | be strong | Hebrew | 5 | boldness,seeking,strength,power,being |
| H5999 | trouble | Hebrew | 5 | anguish,iniquity,perverseness,sorrow,wickedness |
| H7451C | distress: harm | Hebrew | 5 | anguish,distress,evil,grief,wickedness |
| H7760A | to set: make | Hebrew | 5 | calling,intention,purpose,transformation,name |
| H7922 | understanding | Hebrew | 5 | discernment,insight,knowledge,understanding,wisdom |
| H8056 | glad | Hebrew | 5 | delight,joy,rejoicing,heart,gladness |
| H8085G | to hear: hear | Hebrew | 5 | contentment,discernment,obedience,understanding,listen |
| H8378 | desire | Hebrew | 5 | delight,desire,longing,lust,craving |
| H8394 | understanding | Hebrew | 5 | discernment,insight,reasoning,understanding,wisdom |
| G1014 | to plan | Greek | 4 | desire,intention,mind,will |
| G1260 | to discuss | Greek | 4 | discernment,mind,reasoning,wonder |
| G1261 | reasoning | Greek | 4 | imagination,reasoning,thought,doubt |
| G1271 | mind | Greek | 4 | imagination,mind,thought,understanding |
| G1771 | thought/purpose | Greek | 4 | intention,mind,purpose,thought |
| G1849 | authority | Greek | 4 | strength,power,authority,dominion |
| G1971 | to long for | Greek | 4 | desire,longing,yearning,craving |
| G2052 | rivalry | Greek | 4 | ambition,contentment,seeking,strife |
| G2205 | zeal | Greek | 4 | envy,indignation,jealousy,zeal |
| G2372 | wrath | Greek | 4 | anger,indignation,passion,wrath |
| G2744 | to boast | Greek | 4 | boastfulness,joy,pride,rejoicing |
| G3713 | to aspire | Greek | 4 | covetousness,desire,longing,craving |
| G4189 | evil | Greek | 4 | malice,evil,iniquity,wickedness |
| G4907 | understanding | Greek | 4 | discernment,insight,knowledge,understanding |
| G5111 | be bold | Greek | 4 | boastfulness,boldness,courage,being |
| G5426 | to reason | Greek | 4 | intention,mind,reasoning,thought |
| G5463 | to rejoice | Greek | 4 | delight,joy,rejoicing,gladness |
| G5479 | joy | Greek | 4 | delight,joy,rejoicing,gladness |
| H0202 | strength | Hebrew | 4 | goodness,strength,power,wealth |
| H0571G | truth: faithful | Hebrew | 4 | faith,faithfulness,honesty,truthfulness |
| H0898 | to act treacherously | Hebrew | 4 | deceit,faith,faithfulness,transgression |
| H0995 | to understand | Hebrew | 4 | discernment,insight,thought,understanding |
| H1100I | Belial: worthless | Hebrew | 4 | corruption,meaning,wickedness,spirit |
| H1369 | might | Hebrew | 4 | courage,strength,power,might |
| H1523 | to rejoice | Hebrew | 4 | delight,joy,rejoicing,gladness |
| H1672 | be anxious | Hebrew | 4 | anxiety,dread,fear,being |
| H2161 | to plan | Hebrew | 4 | evil,imagination,intention,purpose |
| H2194 | be indignant | Hebrew | 4 | abomination,indignation,wrath,being |
| H2342I | to twist: writh in pain | Hebrew | 4 | agony,anguish,hope,sorrow |
| H2388G | to strengthen: strengthen | Hebrew | 4 | courage,hardness,strength,power |
| H2428G | strength | Hebrew | 4 | courage,strength,power,wealth |
| H2470I | be weak: grieved | Hebrew | 4 | grief,weakness,being,Incurability |
| H2530A | to desire | Hebrew | 4 | covetousness,delight,desire,lust |
| H2656 | pleasure | Hebrew | 4 | delight,desire,purpose,will |
| H2734 | to be incensed | Hebrew | 4 | anger,distress,wrath,being |
| H2836A | to desire | Hebrew | 4 | desire,longing,love,heart |
| H2865 | to to be dismayed | Hebrew | 4 | awe,brokenness,terror,being |
| H3336 | intention | Hebrew | 4 | imagination,intention,mind,purpose |
| H3372H | to fear: revere | Hebrew | 4 | awe,dread,fear,worship |
| H3512A | be disheartened | Hebrew | 4 | brokenness,fear,heart,being |
| H3559K | to establish: right | Hebrew | 4 | faith,faithfulness,trust,truthfulness |
| H3581B | strength | Hebrew | 4 | strength,power,might,wealth |
| H3868 | be devious | Hebrew | 4 | deceit,perverseness,being,devious |
| H4263 | compassion | Hebrew | 4 | compassion,delight,longing,yearning |
| H4284 | plot | Hebrew | 4 | imagination,intention,purpose,thought |
| H4604 | unfaithfulness | Hebrew | 4 | faith,faithfulness,transgression,treachery |
| H4751 | bitter | Hebrew | 4 | anguish,bitterness,distress,Ruthlessness |
| H4885 | rejoicing | Hebrew | 4 | delight,joy,rejoicing,gladness |
| H5034A | be senseless | Hebrew | 4 | foolishness,rejection,contempt,being |
| H5315G | soul | Hebrew | 4 | mind,Soul,heart,spirit |
| H5668 | for the sake of | Hebrew | 4 | intention,purpose,reasoning,the afflicted |
| H5771G | iniquity: crime | Hebrew | 4 | guilt,iniquity,sin,wickedness |
| H6031B | to afflict | Hebrew | 4 | brokenness,endurance,gentleness,the afflicted |
| H6087A | to hurt | Hebrew | 4 | distress,grief,indignation,mourning |
| H6206 | to tremble | Hebrew | 4 | awe,dread,fear,terror |
| H6213A | to make: do | Hebrew | 4 | knowledge,meaning,worship,yielding |
| H6342 | to dread | Hebrew | 4 | awe,dread,fear,terror |
| H6343 | dread | Hebrew | 4 | awe,dread,fear,terror |
| H6381 | to wonder | Hebrew | 4 | dread,hardness,wonder,power |
| H6937 | be dark | Hebrew | 4 | grief,mourning,sorrow,being |
| H6973 | to loathe | Hebrew | 4 | distress,dread,fear,terror |
| H7356B | compassion | Hebrew | 4 | compassion,kindness,love,mercy |
| H7451I | distress: evil | Hebrew | 4 | distress,evil,sin,wickedness |
| H7489A | be evil | Hebrew | 4 | distress,evil,hardness,being |
| H7797 | to rejoice | Hebrew | 4 | delight,joy,rejoicing,gladness |
| H7919A | be prudent | Hebrew | 4 | insight,understanding,wisdom,being |
| H8055 | to rejoice | Hebrew | 4 | delight,joy,rejoicing,gladness |
| H8057 | joy | Hebrew | 4 | delight,joy,rejoicing,gladness |
| H8342 | rejoicing | Hebrew | 4 | delight,joy,rejoicing,gladness |
| H8454 | wisdom | Hebrew | 4 | insight,knowledge,understanding,wisdom |
| G0018 | good | Greek | 3 | generosity,goodness,kindness |
| G0020 | joy | Greek | 3 | delight,joy,gladness |
| G0021 | to rejoice | Greek | 3 | joy,rejoicing,gladness |
| G0040G | holy | Greek | 3 | consecration,holiness,spirit |
| G0458 | lawlessness | Greek | 3 | iniquity,transgression,wickedness |
| G0544 | to disobey | Greek | 3 | disobedience,rejection,unbelief |
| G0570 | unbelief | Greek | 3 | faith,faithfulness,unbelief |
| G0572 | openness | Greek | 3 | generosity,holiness,sincerity |
| G0746 | beginning | Greek | 3 | power,authority,dominion |
| G1011 | to plan | Greek | 3 | counsel,mind,purpose |
| G1013 | plan | Greek | 3 | desire,intention,purpose |
| G1391 | glory | Greek | 3 | dignity,praise,worship |
| G1411 | power | Greek | 3 | strength,power,wealth |
| G1568 | be awe-struck | Greek | 3 | awe,distress,being |
| G1680 | hope | Greek | 3 | faith,faithfulness,hope |
| G1847 | be rejected | Greek | 3 | rejection,contempt,being |
| G1934 | to seek after | Greek | 3 | desire,seeking,craving |
| G1938 | one who desires | Greek | 3 | desire,lust,craving |
| G2118 | righteousness | Greek | 3 | justice,righteousness,uprightness |
| G2174 | be glad | Greek | 3 | gladness,comfort,being |
| G2206 | be eager | Greek | 3 | covetousness,envy,being |
| G2212 | to seek | Greek | 3 | desire,intention,seeking |
| G2292 | be confident | Greek | 3 | boldness,courage,being |
| G2293 | take heart | Greek | 3 | courage,heart,comfort |
| G2480 | be strong | Greek | 3 | strength,power,being |
| G2549 | evil | Greek | 3 | malice,evil,wickedness |
| G2564G | to call: call | Greek | 3 | calling,consecration,name |
| G2588 | heart | Greek | 3 | mind,heart,spirit |
| G2745 | pride | Greek | 3 | boastfulness,pride,rejoicing |
| G2746 | pride | Greek | 3 | boastfulness,pride,rejoicing |
| G2904 | power | Greek | 3 | strength,power,dominion |
| G3004G | to say: says | Greek | 3 | boastfulness,calling,meaning |
| G3049 | to count | Greek | 3 | reasoning,thought,understanding |
| G3076 | to grieve | Greek | 3 | distress,grief,sorrow |
| G3114 | to have patience | Greek | 3 | endurance,longing,patience |
| G3563 | mind | Greek | 3 | insight,mind,understanding |
| G3601 | anguish | Greek | 3 | anguish,grief,sorrow |
| G3709 | wrath | Greek | 3 | anger,indignation,wrath |
| G3715 | lust | Greek | 3 | desire,lust,passion |
| G3870 | to plead/comfort | Greek | 3 | calling,desire,comfort |
| G3958 | to suffer | Greek | 3 | endurance,experience,passion |
| G3997 | grief | Greek | 3 | grief,mourning,sorrow |
| G4100 | to trust (in) | Greek | 3 | faith,faithfulness,trust |
| G4102G | faith | Greek | 3 | faith,faithfulness,trust |
| G4102H | faith: faithfulness | Greek | 3 | faith,faithfulness,trust |
| G4124 | greediness | Greek | 3 | covetousness,greed,craving |
| G4147 | be rich | Greek | 3 | goodness,being,wealth |
| G4576 | be devout | Greek | 3 | fear,worship,being |
| G4893 | conscience | Greek | 3 | conscience,guilt,mind |
| G4894 | be aware | Greek | 3 | conscience,knowledge,being |
| G4993 | be of sound mind | Greek | 3 | mind,self-control,being |
| G5401 | fear | Greek | 3 | awe,fear,terror |
| G5428 | understanding | Greek | 3 | insight,understanding,wisdom |
| G5485 | grace | Greek | 3 | grace,gratitude,blessing |
| G5544 | kindness | Greek | 3 | gentleness,goodness,kindness |
| G5590G | soul | Greek | 3 | mind,Soul,heart |
| H0014 | be willing | Hebrew | 3 | will,yielding,being |
| H0047I | mighty: strong | Hebrew | 3 | mind,stubbornness,power |
| H0367 | terror | Hebrew | 3 | dread,fear,terror |
| H0529 | faithful | Hebrew | 3 | faith,faithfulness,truthfulness |
| H0540 | to trust | Hebrew | 3 | faith,faithfulness,trust |
| H0544 | faithfulness | Hebrew | 3 | faith,faithfulness,truthfulness |
| H0571H | truth: true | Hebrew | 3 | faith,faithfulness,truthfulness |
| H0571I | truth: certain | Hebrew | 3 | faith,faithfulness,truthfulness |
| H0585 | sighing | Hebrew | 3 | groaning,mourning,sorrow |
| H0605 | be incurable | Hebrew | 3 | despair,being,Incurability |
| H0639G | face: anger | Hebrew | 3 | anger,patience,wrath |
| H0639I | face | Hebrew | 3 | anger,pride,wrath |
| H0748 | to prolong | Hebrew | 3 | endurance,longing,patience |
| H0816 | be guilty | Hebrew | 3 | condemnation,guilt,being |
| H0954 | be ashamed | Hebrew | 3 | despair,shame,being |
| H1082 | be cheerful | Hebrew | 3 | strength,comfort,being |
| H1156 | to ask | Hebrew | 3 | desire,prayer,seeking |
| H1288 | to bless | Hebrew | 3 | praise,blessing,Cursing |
| H1419A | great: large | Hebrew | 3 | hardness,longing,power |
| H1481C | to dread | Hebrew | 3 | awe,dread,fear |
| H1524A | rejoicing | Hebrew | 3 | joy,rejoicing,gladness |
| H1674 | anxiety | Hebrew | 3 | anxiety,fear,sorrow |
| H1697G | word | Hebrew | 3 | counsel,prayer,Cursing |
| H1697M | word: because | Hebrew | 3 | iniquity,purpose,reasoning |
| H1897 | to mutter | Hebrew | 3 | imagination,meditation,mourning |
| H1984I | to boast: rave madly | Hebrew | 3 | boastfulness,foolishness,praise |
| H1993 | to roar | Hebrew | 3 | groaning,mourning,yearning |
| H2015 | to overturn | Hebrew | 3 | corruption,perverseness,transformation |
| H2142 | to remember | Hebrew | 3 | memory,mind,thought |
| H2154 | wickedness | Hebrew | 3 | evil,sin,wickedness |
| H2195 | indignation | Hebrew | 3 | anger,indignation,wrath |
| H2256B | pain | Hebrew | 3 | agony,anguish,sorrow |
| H2342A | to twist: tremble | Hebrew | 3 | anguish,distress,fear |
| H2342B | be firm | Hebrew | 3 | anguish,endurance,being |
| H2389 | strong | Hebrew | 3 | hardness,stubbornness,power |
| H2398 | to sin | Hebrew | 3 | guilt,reconciliation,sin |
| H2427A | agony | Hebrew | 3 | agony,anguish,sorrow |
| H2470B | to beg | Hebrew | 3 | prayer,seeking,weakness |
| H2532A | desire | Hebrew | 3 | delight,desire,wealth |
| H2534 | rage | Hebrew | 3 | anger,indignation,wrath |
| H2550 | to spare | Hebrew | 3 | compassion,desire,mercy |
| H2620 | to seek refuge | Hebrew | 3 | hope,seeking,trust |
| H2655 | delighting | Hebrew | 3 | delight,desire,will |
| H2790B | be quiet | Hebrew | 3 | peace,being,listen |
| H2803I | to devise: devise | Hebrew | 3 | imagination,mind,thought |
| H2844A | terror | Hebrew | 3 | dread,fear,terror |
| H2868 | be good | Hebrew | 3 | goodness,gladness,being |
| H2895 | be pleasing | Hebrew | 3 | goodness,love,being |
| H2898 | goodness | Hebrew | 3 | goodness,love,gladness |
| H2974 | be willing | Hebrew | 3 | contentment,will,being |
| H3013 | to suffer | Hebrew | 3 | grief,mourning,sorrow |
| H3015 | sorrow | Hebrew | 3 | anguish,grief,sorrow |
| H3027W | hand: owner | Hebrew | 3 | power,authority,dominion |
| H3045 | to know | Hebrew | 3 | discernment,knowledge,understanding |
| H3476 | uprightness | Hebrew | 3 | honesty,integrity,uprightness |
| H3510 | to pain | Hebrew | 3 | distress,grief,sorrow |
| H3511 | pain | Hebrew | 3 | distress,grief,sorrow |
| H3515 | heavy | Hebrew | 3 | hardness,sorrow,stubbornness |
| H3519 | glory | Hebrew | 3 | dignity,praise,wealth |
| H3581A | reptile | Hebrew | 3 | strength,power,might |
| H3629 | kidney | Hebrew | 3 | conscience,mind,heart |
| H3689 | loin | Hebrew | 3 | foolishness,hope,trust |
| H3700 | to long | Hebrew | 3 | desire,longing,shame |
| H3707 | to provoke | Hebrew | 3 | anger,indignation,sorrow |
| H3820A | heart | Hebrew | 3 | mind,heart,spirit |
| H4172A | fear | Hebrew | 3 | dread,fear,terror |
| H4261 | desire | Hebrew | 3 | delight,desire,love |
| H4334 | plain | Hebrew | 3 | justice,righteousness,uprightness |
| H4339 | uprightness | Hebrew | 3 | integrity,sincerity,uprightness |
| H4475 | dominion | Hebrew | 3 | power,authority,dominion |
| H4486 | knowledge | Hebrew | 3 | knowledge,reasoning,understanding |
| H4549 | to melt | Hebrew | 3 | despair,fear,weakness |
| H4616 | because | Hebrew | 3 | intention,purpose,reasoning |
| H4712 | terror | Hebrew | 3 | anguish,distress,terror |
| H4805H | rebellion | Hebrew | 3 | bitterness,bondage,rebellion |
| H4998 | be lovely | Hebrew | 3 | delight,love,being |
| H5006 | to spurn | Hebrew | 3 | anger,rejection,contempt |
| H5069 | be willing | Hebrew | 3 | mind,will,being |
| H5186 | to stretch | Hebrew | 3 | justice,longing,yielding |
| H5229 | upright | Hebrew | 3 | honesty,truthfulness,uprightness |
| H5315H | soul: life | Hebrew | 3 | Soul,spirit,strength |
| H5315I | soul: myself | Hebrew | 3 | mind,Soul,heart |
| H5375J | to lift: guilt | Hebrew | 3 | endurance,guilt,Incurability |
| H5375O | to lift: trust | Hebrew | 3 | desire,longing,trust |
| H5414G | to give: give | Hebrew | 3 | delight,surrender,yielding |
| H5674B | be angry | Hebrew | 3 | anger,wrath,being |
| H5690 | lust | Hebrew | 3 | desire,love,lust |
| H5766A | injustice | Hebrew | 3 | iniquity,sin,wickedness |
| H5766B | injustice | Hebrew | 3 | iniquity,perverseness,wickedness |
| H5771H | iniquity: guilt | Hebrew | 3 | guilt,iniquity,sin |
| H5771I | iniquity: punishment | Hebrew | 3 | guilt,iniquity,sin |
| H6040 | affliction | Hebrew | 3 | grief,sorrow,the afflicted |
| H6213H | to make | Hebrew | 3 | knowledge,mourning,yielding |
| H6315 | to breathe | Hebrew | 3 | longing,testimony,yearning |
| H6586 | to transgress | Hebrew | 3 | rebellion,sin,transgression |
| H6588 | transgression | Hebrew | 3 | rebellion,sin,transgression |
| H6663 | to justify | Hebrew | 3 | innocence,justice,righteousness |
| H6664G | righteousness | Hebrew | 3 | justice,righteousness,truthfulness |
| H6666 | righteousness | Hebrew | 3 | honesty,justice,righteousness |
| H6862B | distress | Hebrew | 3 | anguish,distress,sorrow |
| H6942I | to consecrate: forfeit | Hebrew | 3 | consecration,defilement,holiness |
| H6965B | to arise: rise | Hebrew | 3 | endurance,rebellion,power |
| H7065 | be jealous | Hebrew | 3 | envy,zeal,being |
| H7068 | jealousy | Hebrew | 3 | envy,jealousy,zeal |
| H7107 | be angry | Hebrew | 3 | anger,wrath,being |
| H7110A | wrath | Hebrew | 3 | anger,indignation,wrath |
| H7185 | to harden | Hebrew | 3 | distress,hardness,stubbornness |
| H7235A | to multiply | Hebrew | 3 | boastfulness,longing,authority |
| H7267 | turmoil | Hebrew | 3 | anger,fear,wrath |
| H7307G | spirit | Hebrew | 3 | courage,mind,spirit |
| H7307J | spirit: temper | Hebrew | 3 | anger,self-control,spirit |
| H7355 | to have compassion | Hebrew | 3 | compassion,love,mercy |
| H7379 | strife | Hebrew | 3 | contentment,distress,strife |
| H7440 | cry | Hebrew | 3 | joy,rejoicing,gladness |
| H7455 | evil | Hebrew | 3 | evil,sorrow,wickedness |
| H7521 | to accept | Hebrew | 3 | delight,devotion,likeness |
| H7561 | be wicked | Hebrew | 3 | condemnation,wickedness,being |
| H7562 | wickedness | Hebrew | 3 | evil,iniquity,wickedness |
| H7563 | wicked | Hebrew | 3 | condemnation,evil,wickedness |
| H7592 | to ask | Hebrew | 3 | desire,seeking,craving |
| H7725I | to return: turn back | Hebrew | 3 | iniquity,rejection,repentance |
| H7737A | be like | Hebrew | 3 | worth,likeness,being |
| H7878 | to muse | Hebrew | 3 | distress,meditation,praise |
| H8085K | to hear: judge | Hebrew | 3 | discernment,understanding,listen |
| H8130 | to hate | Hebrew | 3 | malice,hatred,love |
| H8199 | to judge | Hebrew | 3 | condemnation,justice,reasoning |
| H8537 | integrity | Hebrew | 3 | innocence,integrity,uprightness |
| H8549H | unblemished: blameless | Hebrew | 3 | integrity,sincerity,uprightness |
| H8633 | power | Hebrew | 3 | strength,power,authority |
| G0023 | be indignant | Greek | 2 | indignation,being |
| G0025 | to love | Greek | 2 | love,craving |
| G0037 | to sanctify | Greek | 2 | consecration,holiness |
| G0050 | be ignorant | Greek | 2 | understanding,being |
| G0053 | pure | Greek | 2 | innocence,sin |
| G0074 | a struggle | Greek | 2 | agony,anguish |
| G0085 | be distressed | Greek | 2 | distress,being |
| G0093 | unrighteousness | Greek | 2 | evil,iniquity |
| G0102 | unable | Greek | 2 | weakness,strength |
| G0144 | insight | Greek | 2 | discernment,insight |
| G0153 | be ashamed | Greek | 2 | shame,being |
| G0154 | to ask | Greek | 2 | desire,craving |
| G0156 | cause/charge | Greek | 2 | guilt,reasoning |
| G0159 | causer | Greek | 2 | guilt,reasoning |
| G0191 | to hear | Greek | 2 | understanding,listen |
| G0212 | boasting | Greek | 2 | boastfulness,pride |
| G0226 | be truthful | Greek | 2 | truthfulness,being |
| G0266 | sin | Greek | 2 | guilt,sin |
| G0407 | to act like a man | Greek | 2 | courage,likeness |
| G0430 | to endure | Greek | 2 | endurance,listen |
| G0485 | dispute | Greek | 2 | rebellion,strife |
| G0505 | genuine | Greek | 2 | hypocrisy,sincerity |
| G0506 | insubordinate | Greek | 2 | disobedience,rebellion |
| G0509 | from above/again | Greek | 2 | bondage,longing |
| G0543 | disobedience | Greek | 2 | disobedience,unbelief |
| G0560 | to despair | Greek | 2 | despair,hope |
| G0569 | to disbelieve | Greek | 2 | faith,faithfulness |
| G0581 | to cease to be | Greek | 2 | deadness,being |
| G0639 | be perplexed | Greek | 2 | doubt,being |
| G0662 | be bold | Greek | 2 | boldness,being |
| G0701 | pleasing | Greek | 2 | desire,reasoning |
| G0714 | be sufficient | Greek | 2 | contentment,being |
| G0766 | debauchery | Greek | 2 | debauchery,flesh |
| G0770G | be weak: weak | Greek | 2 | weakness,being |
| G0770H | be weak: ill | Greek | 2 | weakness,being |
| G0772G | weak | Greek | 2 | weakness,strength |
| G0801 | senseless | Greek | 2 | foolishness,understanding |
| G0861 | incorruptibility | Greek | 2 | integrity,sincerity |
| G0866 | not greedy | Greek | 2 | covetousness,love |
| G0928H | to torture: anguish | Greek | 2 | agony,anguish |
| G0979 | life | Greek | 2 | goodness,wealth |
| G0987 | to blaspheme | Greek | 2 | slander,Cursing |
| G1012 | plan | Greek | 2 | counsel,purpose |
| G1106 | resolution | Greek | 2 | mind,purpose |
| G1108 | knowledge | Greek | 2 | knowledge,understanding |
| G1133 | weak-willed woman | Greek | 2 | weakness,will |
| G1168 | be timid | Greek | 2 | fear,being |
| G1169 | timid | Greek | 2 | awe,fear |
| G1228G | Devil | Greek | 2 | slander,the afflicted |
| G1228H | slanderous | Greek | 2 | slander,the afflicted |
| G1252 | to judge/doubt | Greek | 2 | discernment,doubt |
| G1280 | be perplexed | Greek | 2 | doubt,being |
| G1342 | just | Greek | 2 | innocence,sincerity |
| G1343 | righteousness | Greek | 2 | justice,righteousness |
| G1349 | condemnation | Greek | 2 | condemnation,justice |
| G1380 | to think | Greek | 2 | imagination,thought |
| G1382 | test | Greek | 2 | character,experience |
| G1398 | be a slave | Greek | 2 | bondage,being |
| G1414 | be able | Greek | 2 | power,being |
| G1415 | able | Greek | 2 | power,authority |
| G1425 | hard to understand | Greek | 2 | hardness,understanding |
| G1426 | slander | Greek | 2 | evil,slander |
| G1492I | to perceive: know | Greek | 2 | knowledge,understanding |
| G1498 | may be | Greek | 2 | meaning,being |
| G1504 | image | Greek | 2 | image,likeness |
| G1514 | be at peace | Greek | 2 | peace,being |
| G1516 | peaceful | Greek | 2 | love,peace |
| G1520 | one | Greek | 2 | purpose,unity |
| G1609 | to spit out | Greek | 2 | rejection,contempt |
| G1612 | be warped | Greek | 2 | corruption,being |
| G1653 | to have mercy | Greek | 2 | compassion,mercy |
| G1656 | mercy | Greek | 2 | compassion,mercy |
| G1679 | to hope/expect | Greek | 2 | hope,trust |
| G1690 | be agitated | Greek | 2 | groaning,being |
| G1719 | afraid | Greek | 2 | fear,terror |
| G1757 | be blessed | Greek | 2 | blessing,being |
| G1761 | reflection | Greek | 2 | imagination,thought |
| G1783 | intercession | Greek | 2 | intercession,prayer |
| G1793 | to call on | Greek | 2 | calling,intercession |
| G1840 | to have power | Greek | 2 | strength,power |
| G1848 | to reject | Greek | 2 | rejection,contempt |
| G1850 | to have authority | Greek | 2 | power,authority |
| G1932 | gentleness | Greek | 2 | gentleness,kindness |
| G1933 | gentle | Greek | 2 | gentleness,reasoning |
| G1941 | to call (on)/name | Greek | 2 | calling,name |
| G1963 | thought | Greek | 2 | intention,thought |
| G1972 | longing | Greek | 2 | desire,longing |
| G1974 | longing | Greek | 2 | desire,longing |
| G1990 | knowing | Greek | 2 | knowledge,understanding |
| G2028 | to name | Greek | 2 | calling,name |
| G2036 | to say: said | Greek | 2 | calling,blessing |
| G2054 | quarrel | Greek | 2 | contentment,strife |
| G2071 | will be | Greek | 2 | will,being |
| G2106 | to delight | Greek | 2 | contentment,delight |
| G2107 | goodwill | Greek | 2 | desire,purpose |
| G2114 | be cheerful | Greek | 2 | courage,being |
| G2124 | reverence | Greek | 2 | awe,fear |
| G2127 | to praise/bless | Greek | 2 | praise,blessing |
| G2128 | praiseworthy | Greek | 2 | praise,blessing |
| G2129 | praise | Greek | 2 | praise,blessing |
| G2138 | compliant | Greek | 2 | devotion,reasoning |
| G2162 | good report | Greek | 2 | goodness,praise |
| G2165 | to celebrate | Greek | 2 | rejoicing,gladness |
| G2167 | joy | Greek | 2 | joy,gladness |
| G2237 | pleasure | Greek | 2 | lust,passion |
| G2261 | gentle | Greek | 2 | gentleness,kindness |
| G2270 | be quiet/give up | Greek | 2 | peace,being |
| G2307 | will/desire | Greek | 2 | desire,will |
| G2309 | to will/desire | Greek | 2 | desire,will |
| G2318 | godly | Greek | 2 | fear,worship |
| G2346 | to press on | Greek | 2 | distress,hardness |
| G2347 | pressure | Greek | 2 | anguish,distress |
| G2348 | to die/be dead | Greek | 2 | deadness,being |
| G2433 | to propitiate | Greek | 2 | mercy,reconciliation |
| G2436 | propitious/gracious | Greek | 2 | forgiveness,mercy |
| G2473 | like-minded | Greek | 2 | mind,likeness |
| G2478 | strong | Greek | 2 | strength,power |
| G2479 | strength | Greek | 2 | strength,power |
| G2551 | to curse/revile | Greek | 2 | evil,Cursing |
| G2555 | wrongdoing | Greek | 2 | evil,slander |
| G2564H | to call: name | Greek | 2 | calling,name |
| G2577G | be weary/sick: weak | Greek | 2 | weakness,being |
| G2617 | to dishonor | Greek | 2 | shame,Cursing |
| G2636 | slander | Greek | 2 | evil,slander |
| G2691 | to desire | Greek | 2 | desire,passion |
| G2761 | vainly | Greek | 2 | purpose,reasoning |
| G2799 | to weep | Greek | 2 | mourning,weeping |
| G2839G | common: unsanctified | Greek | 2 | defilement,impurity |
| G2840 | to profane | Greek | 2 | defilement,impurity |
| G2863 | be long-haired | Greek | 2 | longing,being |
| G2919 | to judge | Greek | 2 | condemnation,thought |
| G2920 | judgment | Greek | 2 | condemnation,justice |
| G2963 | lordship | Greek | 2 | authority,dominion |
| G3004H | to say: name | Greek | 2 | calling,name |
| G3053 | thought | Greek | 2 | imagination,thought |
| G3077 | grief | Greek | 2 | grief,sorrow |
| G3115 | patience | Greek | 2 | endurance,patience |
| G3141 | testimony | Greek | 2 | testimony,thought |
| G3173 | great | Greek | 2 | longing,power |
| G3191 | to meditate/plot | Greek | 2 | imagination,meditation |
| G3308 | concern | Greek | 2 | anxiety,thought |
| G3322 | be in the middle | Greek | 2 | being,the afflicted |
| G3356 | be gentle | Greek | 2 | gentleness,being |
| G3393 | defilement | Greek | 2 | corruption,defilement |
| G3394 | defilement | Greek | 2 | corruption,defilement |
| G3415 | to remember | Greek | 2 | mind,being |
| G3471 | be foolish | Greek | 2 | foolishness,being |
| G3525 | be sober | Greek | 2 | mind,being |
| G3539 | to understand | Greek | 2 | imagination,understanding |
| G3540 | mind/thought | Greek | 2 | mind,thought |
| G3543 | to think | Greek | 2 | imagination,thought |
| G3552 | be sick | Greek | 2 | craving,being |
| G3628 | compassion | Greek | 2 | compassion,mercy |
| G3634 | such as | Greek | 2 | kindness,likeness |
| G3640 | of little faith | Greek | 2 | faith,faithfulness |
| G3675 | like-minded | Greek | 2 | mind,likeness |
| G3686 | name | Greek | 2 | calling,name |
| G3687 | to name | Greek | 2 | calling,name |
| G3716 | be upright | Greek | 2 | uprightness,being |
| G3741 | sacred | Greek | 2 | holiness,mercy |
| G3776 | estate | Greek | 2 | goodness,wealth |
| G3801 | was, is, will be | Greek | 2 | will,being |
| G3806 | passion | Greek | 2 | lust,passion |
| G3856 | to disgrace | Greek | 2 | shame,contempt |
| G3892 | lawlessness | Greek | 2 | iniquity,transgression |
| G3900 | trespass | Greek | 2 | sin,transgression |
| G3912 | be insane | Greek | 2 | mind,being |
| G3949 | to anger | Greek | 2 | anger,wrath |
| G3950 | anger | Greek | 2 | anger,wrath |
| G3984 | test | Greek | 2 | endurance,experience |
| G3996 | to mourn | Greek | 2 | grief,mourning |
| G4006 | confidence | Greek | 2 | boldness,trust |
| G4103 | faithful | Greek | 2 | faith,faithfulness |
| G4123 | greedy | Greek | 2 | covetousness,greed |
| G4151G | spirit/breath: spirit | Greek | 2 | holiness,spirit |
| G4217 | of what kind? | Greek | 2 | kindness,wonder |
| G4240 | gentleness | Greek | 2 | gentleness,humility |
| G4276 | to hope beforehand | Greek | 2 | hope,trust |
| G4286 | purpose | Greek | 2 | consecration,purpose |
| G4574 | object of worship | Greek | 2 | devotion,worship |
| G4587 | dignity | Greek | 2 | dignity,honesty |
| G4601 | be silent | Greek | 2 | peace,being |
| G4623 | be quiet | Greek | 2 | peace,being |
| G4641 | hardness of heart | Greek | 2 | hardness,heart |
| G4643 | hardness | Greek | 2 | hardness,stubbornness |
| G4646 | crooked | Greek | 2 | corruption,perverseness |
| G4698 | affection/entrails | Greek | 2 | compassion,heart |
| G4727 | to groan | Greek | 2 | grief,groaning |
| G4730 | hardship | Greek | 2 | anguish,distress |
| G4796 | to rejoice with | Greek | 2 | joy,rejoicing |
| G4818 | be grieved | Greek | 2 | sorrow,being |
| G4908 | intelligent | Greek | 2 | discernment,understanding |
| G4912 | to hold/oppress | Greek | 2 | distress,hardness |
| G4920 | to understand | Greek | 2 | insight,understanding |
| G4928 | anguish | Greek | 2 | anguish,distress |
| G4980 | be devoted/empty | Greek | 2 | devotion,being |
| G4991 | salvation | Greek | 2 | strength,salvation |
| G5187 | be conceited | Greek | 2 | pride,being |
| G5242 | be higher | Greek | 2 | authority,being |
| G5272 | hypocrisy | Greek | 2 | hypocrisy,condemnation |
| G5278 | to remain/endure | Greek | 2 | endurance,patience |
| G5280 | remembrance | Greek | 2 | memory,mind |
| G5281 | perseverance | Greek | 2 | endurance,patience |
| G5292 | submission | Greek | 2 | obedience,submission |
| G5293 | to subject | Greek | 2 | obedience,submission |
| G5342 | to bear/lead | Greek | 2 | endurance,yielding |
| G5351 | to destroy | Greek | 2 | corruption,defilement |
| G5358 | lover of good | Greek | 2 | goodness,love |
| G5361 | loving the brothers | Greek | 2 | love,the afflicted |
| G5363 | benevolence | Greek | 2 | kindness,love |
| G5366 | money-loving | Greek | 2 | covetousness,love |
| G5379 | love of dispute | Greek | 2 | love,strife |
| G5383 | to love to be first | Greek | 2 | love,being |
| G5387 | affectionate | Greek | 2 | devotion,love |
| G5399 | to fear | Greek | 2 | fear,terror |
| G5400 | fearful thing | Greek | 2 | fear,terror |
| G5427 | purpose | Greek | 2 | mind,purpose |
| G5483 | to give grace | Greek | 2 | forgiveness,grace |
| G5541 | be kind | Greek | 2 | kindness,being |
| G5543 | good/kind | Greek | 2 | goodness,kindness |
| G5604 | labor | Greek | 2 | agony,sorrow |
| G6066 | little faith | Greek | 2 | faith,faithfulness |
| G6094 | to boast | Greek | 2 | boastfulness,authority |
| G6285 | to call by name | Greek | 2 | calling,name |
| G6786 | be in awe | Greek | 2 | awe,being |
| G6975 | be in power | Greek | 2 | power,being |
| G7124 | be willing | Greek | 2 | will,being |
| G7493 | to love passionately | Greek | 2 | love,passion |
| G7684 | bold-hearted | Greek | 2 | boldness,heart |
| G7774 | evil-minded | Greek | 2 | evil,mind |
| G8313 | be content | Greek | 2 | contentment,being |
| G8485 | be faint-hearted | Greek | 2 | heart,being |
| G8878 | gentle-minded | Greek | 2 | gentleness,mind |
| H0006 | to perish | Hebrew | 2 | brokenness,corruption |
| H0056 | to mourn | Hebrew | 2 | grief,mourning |
| H0057 | mourning | Hebrew | 2 | grief,mourning |
| H0060 | mourning | Hebrew | 2 | mourning,sorrow |
| H0157G | to love: lover | Hebrew | 2 | desire,love |
| H0185 | desire | Hebrew | 2 | desire,passion |
| H0386 | strong | Hebrew | 2 | endurance,strength |
| H0533 | strong | Hebrew | 2 | courage,strength |
| H0584 | to sigh | Hebrew | 2 | groaning,mourning |
| H0592 | lamentation | Hebrew | 2 | mourning,sorrow |
| H0639H | face: nose | Hebrew | 2 | anger,wrath |
| H0753 | length | Hebrew | 2 | longing,patience |
| H0817 | guilt [offering] | Hebrew | 2 | guilt,sin |
| H0819 | guiltiness | Hebrew | 2 | guilt,sin |
| H0833 | to bless | Hebrew | 2 | calling,blessing |
| H0887 | to stink | Hebrew | 2 | abomination,shame |
| H0888 | be displeased | Hebrew | 2 | distress,being |
| H0926 | to dismay | Hebrew | 2 | distress,terror |
| H0937 | contempt | Hebrew | 2 | shame,contempt |
| H0982 | to trust | Hebrew | 2 | hope,trust |
| H0986 | trust | Hebrew | 2 | hope,trust |
| H0999 | understanding | Hebrew | 2 | discernment,understanding |
| H1058 | to weep | Hebrew | 2 | mourning,weeping |
| H1068 | weeping | Hebrew | 2 | mourning,weeping |
| H1079 | mind | Hebrew | 2 | mind,heart |
| H1091 | terror | Hebrew | 2 | dread,terror |
| H1161 | terror | Hebrew | 2 | dread,terror |
| H1215 | unjust-gain | Hebrew | 2 | covetousness,greed |
| H1239 | to enquire | Hebrew | 2 | meditation,seeking |
| H1245 | to seek | Hebrew | 2 | desire,seeking |
| H1289 | to bless | Hebrew | 2 | praise,blessing |
| H1293 | blessing | Hebrew | 2 | peace,blessing |
| H1346 | pride | Hebrew | 2 | boastfulness,pride |
| H1361 | to exult | Hebrew | 2 | courage,pride |
| H1363 | height | Hebrew | 2 | dignity,pride |
| H1370 | might | Hebrew | 2 | power,might |
| H1518 | to burst/come out | Hebrew | 2 | agony,groaning |
| H1525 | rejoicing | Hebrew | 2 | joy,rejoicing |
| H1544 | idol | Hebrew | 2 | idolatry,image |
| H1602 | to abhor | Hebrew | 2 | defilement,rejection |
| H1669 | to languish | Hebrew | 2 | sorrow,weakness |
| H1670 | dismay | Hebrew | 2 | sorrow,terror |
| H1671 | sorrow | Hebrew | 2 | despair,sorrow |
| H1696G | to speak: speak | Hebrew | 2 | boastfulness,slander |
| H1701 | cause | Hebrew | 2 | intention,purpose |
| H1763 | to fear | Hebrew | 2 | dread,fear |
| H1777 | to judge | Hebrew | 2 | justice,strife |
| H1792 | to crush | Hebrew | 2 | brokenness,contrition |
| H1794 | to crush | Hebrew | 2 | brokenness,contrition |
| H1819 | to resemble | Hebrew | 2 | imagination,likeness |
| H1821 | be like | Hebrew | 2 | likeness,being |
| H1823 | likeness | Hebrew | 2 | image,likeness |
| H1847 | knowledge | Hebrew | 2 | knowledge,understanding |
| H1901 | meditation | Hebrew | 2 | groaning,meditation |
| H1926 | glory | Hebrew | 2 | dignity,blessing |
| H1961 | to be | Hebrew | 2 | endurance,being |
| H1984A | to shine | Hebrew | 2 | boastfulness,praise |
| H1984B | to boast: praise | Hebrew | 2 | boastfulness,praise |
| H1984H | to boast: boast | Hebrew | 2 | boastfulness,praise |
| H2103 | be proud | Hebrew | 2 | pride,being |
| H2143 | memorial | Hebrew | 2 | memory,name |
| H2181 | to fornicate | Hebrew | 2 | whoredom,the afflicted |
| H2183 | fornication | Hebrew | 2 | idolatry,whoredom |
| H2197 | rage | Hebrew | 2 | indignation,wrath |
| H2201 | outcry | Hebrew | 2 | distress,mourning |
| H2220 | arm | Hebrew | 2 | strength,power |
| H2254B | to destroy | Hebrew | 2 | brokenness,corruption |
| H2283 | terror | Hebrew | 2 | shame,terror |
| H2302 | to rejoice | Hebrew | 2 | rejoicing,gladness |
| H2304 | joy | Hebrew | 2 | joy,gladness |
| H2342K | to twist: anticipate | Hebrew | 2 | anguish,trust |
| H2347 | to pity | Hebrew | 2 | compassion,mercy |
| H2392 | strength | Hebrew | 2 | strength,power |
| H2393 | strength | Hebrew | 2 | strength,power |
| H2399 | sin | Hebrew | 2 | guilt,sin |
| H2401 | sin | Hebrew | 2 | guilt,sin |
| H2421 | to live | Hebrew | 2 | appetite,being |
| H2427B | agony | Hebrew | 2 | agony,sorrow |
| H2428A | strength: soldiers | Hebrew | 2 | strength,wealth |
| H2428H | strength: rich | Hebrew | 2 | strength,wealth |
| H2428I | strength: worthy | Hebrew | 2 | strength,wealth |
| H2429 | strength | Hebrew | 2 | strength,power |
| H2449 | be wise | Hebrew | 2 | wisdom,being |
| H2450 | wise | Hebrew | 2 | wisdom,heart |
| H2470A | be weak: weak | Hebrew | 2 | weakness,being |
| H2470H | be weak: ill | Hebrew | 2 | weakness,being |
| H2490H | to profane/begin: profane | Hebrew | 2 | brokenness,defilement |
| H2505B | to smooth | Hebrew | 2 | deceit,devious |
| H2528 | rage | Hebrew | 2 | anger,wrath |
| H2530B | precious thing | Hebrew | 2 | covetousness,desire |
| H2531 | delight | Hebrew | 2 | delight,desire |
| H2532B | desirable thing | Hebrew | 2 | delight,desire |
| H2551 | compassion | Hebrew | 2 | compassion,mercy |
| H2600 | for nothing | Hebrew | 2 | guilt,reasoning |
| H2603B | be loathsome | Hebrew | 2 | mercy,being |
| H2610 | to pollute | Hebrew | 2 | corruption,defilement |
| H2616B | to shame | Hebrew | 2 | kindness,shame |
| H2632 | authority | Hebrew | 2 | power,authority |
| H2633 | wealth | Hebrew | 2 | strength,wealth |
| H2654A | to delight in | Hebrew | 2 | delight,desire |
| H2659 | be ashamed | Hebrew | 2 | shame,being |
| H2729 | to tremble | Hebrew | 2 | fear,terror |
| H2731 | trembling | Hebrew | 2 | fear,terror |
| H2740 | burning anger | Hebrew | 2 | anger,wrath |
| H2778A | to taunt | Hebrew | 2 | shame,contempt |
| H2781 | reproach | Hebrew | 2 | shame,contempt |
| H2790A | to plow/plot | Hebrew | 2 | peace,being |
| H2814 | be silent | Hebrew | 2 | peace,being |
| H2837 | desire | Hebrew | 2 | desire,longing |
| H2844B | shattered | Hebrew | 2 | brokenness,terror |
| H2896C | welfare | Hebrew | 2 | goodness,gladness |
| H2930A | to defile | Hebrew | 2 | defilement,impurity |
| H2932 | uncleanness | Hebrew | 2 | defilement,impurity |
| H2940 | taste | Hebrew | 2 | discernment,understanding |
| H2942 | command | Hebrew | 2 | discernment,wisdom |
| H2954 | be insensitive | Hebrew | 2 | hardness,being |
| H2973 | be foolish | Hebrew | 2 | foolishness,being |
| H2976 | to despair | Hebrew | 2 | despair,hope |
| H3016 | fearing | Hebrew | 2 | dread,fear |
| H3025 | to fear | Hebrew | 2 | dread,fear |
| H3027M | hand: monument | Hebrew | 2 | memory,power |
| H3027R | hand: donate | Hebrew | 2 | consecration,power |
| H3046 | to know | Hebrew | 2 | discernment,understanding |
| H3052 | to give | Hebrew | 2 | surrender,yielding |
| H3176H | to wait: hope | Hebrew | 2 | hope,trust |
| H3191 | be good | Hebrew | 2 | goodness,being |
| H3201 | be able | Hebrew | 2 | endurance,being |
| H3289 | to advise | Hebrew | 2 | counsel,purpose |
| H3302 | be beautiful | Hebrew | 2 | delight,being |
| H3318G | to come out: come | Hebrew | 2 | surrender,flesh |
| H3334 | be distressed | Hebrew | 2 | distress,being |
| H3373 | afraid | Hebrew | 2 | fear,worship |
| H3374 | fear | Hebrew | 2 | dread,fear |
| H3415 | be ill | Hebrew | 2 | evil,being |
| H3615I | to end: decides | Hebrew | 2 | intention,longing |
| H3637 | be humiliated | Hebrew | 2 | shame,being |
| H3644G | like | Hebrew | 2 | worth,likeness |
| H3688 | be stupid | Hebrew | 2 | foolishness,being |
| H3722A | to atone | Hebrew | 2 | forgiveness,mercy |
| H3735 | be distressed | Hebrew | 2 | distress,being |
| H3782 | to stumble | Hebrew | 2 | brokenness,weakness |
| H3811 | be weary | Hebrew | 2 | patience,being |
| H3823A | to encourage | Hebrew | 2 | understanding,heart |
| H3824 | heart | Hebrew | 2 | mind,heart |
| H3825 | heart | Hebrew | 2 | mind,heart |
| H3826 | heart | Hebrew | 2 | mind,heart |
| H3885A | to lodge | Hebrew | 2 | endurance,the afflicted |
| H3891 | perversity | Hebrew | 2 | perverseness,devious |
| H4009 | confidence | Hebrew | 2 | hope,trust |
| H4010 | cheer | Hebrew | 2 | joy,comfort |
| H4032 | terror | Hebrew | 2 | fear,terror |
| H4034 | fear | Hebrew | 2 | dread,fear |
| H4035 | fear | Hebrew | 2 | fear,terror |
| H4044 | covering | Hebrew | 2 | hardness,sorrow |
| H4066 | strife | Hebrew | 2 | contentment,strife |
| H4079 | contention | Hebrew | 2 | contentment,strife |
| H4093 | knowledge | Hebrew | 2 | knowledge,thought |
| H4164 | constraint | Hebrew | 2 | anguish,distress |
| H4172B | fear | Hebrew | 2 | fear,terror |
| H4180 | possession | Hebrew | 2 | desire,thought |
| H4191 | to die | Hebrew | 2 | condemnation,deadness |
| H4268 | refuge | Hebrew | 2 | hope,trust |
| H4341 | pain | Hebrew | 2 | grief,sorrow |
| H4390 | to fill | Hebrew | 2 | consecration,contentment |
| H4395 | fruit | Hebrew | 2 | faith,faithfulness |
| H4427B | to advise | Hebrew | 2 | counsel,thought |
| H4474 | dominion | Hebrew | 2 | authority,dominion |
| H4553 | mourning | Hebrew | 2 | mourning,weeping |
| H4637 | terror | Hebrew | 2 | terror,power |
| H4656 | horror | Hebrew | 2 | abomination,image |
| H4676 | pillar | Hebrew | 2 | memory,image |
| H4683 | strife | Hebrew | 2 | contentment,strife |
| H4689 | distress | Hebrew | 2 | anguish,distress |
| H4691 | distress | Hebrew | 2 | anguish,distress |
| H4784 | to rebel | Hebrew | 2 | bitterness,disobedience |
| H4786 | bitterness | Hebrew | 2 | bitterness,grief |
| H4791 | height | Hebrew | 2 | dignity,pride |
| H4808 | provocation | Hebrew | 2 | contentment,strife |
| H4816 | weakness | Hebrew | 2 | despair,weakness |
| H4820 | deceit | Hebrew | 2 | deceit,treachery |
| H4832 | healing | Hebrew | 2 | gentleness,yielding |
| H4834 | be sick | Hebrew | 2 | bitterness,being |
| H4843 | to provoke | Hebrew | 2 | bitterness,weeping |
| H4888B | consecrated portion | Hebrew | 2 | anointing,consecration |
| H4906 | figure | Hebrew | 2 | imagination,image |
| H4910 | to rule | Hebrew | 2 | authority,dominion |
| H4915A | likeness | Hebrew | 2 | dominion,likeness |
| H4915B | dominion | Hebrew | 2 | authority,dominion |
| H5000 | lovely | Hebrew | 2 | delight,love |
| H5036 | foolish | Hebrew | 2 | foolishness,understanding |
| H5068 | be willing | Hebrew | 2 | will,being |
| H5079 | impurity | Hebrew | 2 | defilement,impurity |
| H5098 | to groan | Hebrew | 2 | groaning,mourning |
| H5100 | groaning | Hebrew | 2 | anguish,groaning |
| H5117 | to rest | Hebrew | 2 | peace,comfort |
| H5136 | be sick | Hebrew | 2 | despair,being |
| H5144A | to dedicate | Hebrew | 2 | consecration,devotion |
| H5144B | be a Nazarite | Hebrew | 2 | consecration,being |
| H5150 | comfort | Hebrew | 2 | compassion,comfort |
| H5164 | repentance | Hebrew | 2 | compassion,repentance |
| H5173 | divination | Hebrew | 2 | sorcery,Cursing |
| H5232 | wealth | Hebrew | 2 | goodness,wealth |
| H5273A | pleasant | Hebrew | 2 | delight,love |
| H5276 | be pleasant | Hebrew | 2 | delight,being |
| H5315M | soul: dead | Hebrew | 2 | Soul,deadness |
| H5344A | to pierce | Hebrew | 2 | name,Cursing |
| H5352 | to clear | Hebrew | 2 | innocence,meaning |
| H5375H | to lift: bear | Hebrew | 2 | endurance,yielding |
| H5397 | breath | Hebrew | 2 | Soul,spirit |
| H5414H | to give: put | Hebrew | 2 | devotion,purpose |
| H5475 | counsel | Hebrew | 2 | counsel,fellowship |
| H5528 | be foolish | Hebrew | 2 | foolishness,being |
| H5539 | to rejoice | Hebrew | 2 | joy,rejoicing |
| H5647G | to serve | Hebrew | 2 | bondage,worship |
| H5647H | to serve: minister | Hebrew | 2 | transgression,worship |
| H5674D | to pass: trespass | Hebrew | 2 | sin,transgression |
| H5678 | fury | Hebrew | 2 | anger,wrath |
| H5691 | lust | Hebrew | 2 | love,lust |
| H5753B | to pervert | Hebrew | 2 | iniquity,perverseness |
| H5769G | forever: enduring | Hebrew | 2 | endurance,longing |
| H5769J | forever: antiquity | Hebrew | 2 | endurance,longing |
| H5794 | strong | Hebrew | 2 | power,Ruthlessness |
| H5807 | strength | Hebrew | 2 | strength,power |
| H5869K | eye: sin | Hebrew | 2 | iniquity,sin |
| H5892A | excitement | Hebrew | 2 | anguish,wrath |
| H5947 | jubilant | Hebrew | 2 | boastfulness,rejoicing |
| H5953D | to thrust | Hebrew | 2 | defilement,strength |
| H5965 | to rejoice | Hebrew | 2 | delight,rejoicing |
| H6030B | to answer | Hebrew | 2 | calling,testimony |
| H6037 | gentleness | Hebrew | 2 | gentleness,humility |
| H6038 | gentleness | Hebrew | 2 | gentleness,humility |
| H6041 | afflicted | Hebrew | 2 | iniquity,the afflicted |
| H6087B | to shape | Hebrew | 2 | worship,image |
| H6089A | toil | Hebrew | 2 | hardness,sorrow |
| H6093 | toil | Hebrew | 2 | hardness,sorrow |
| H6094 | injury | Hebrew | 2 | grief,sorrow |
| H6098 | counsel | Hebrew | 2 | counsel,purpose |
| H6099 | mighty | Hebrew | 2 | strength,power |
| H6101 | be sluggish | Hebrew | 2 | sloth,being |
| H6105A | be vast | Hebrew | 2 | power,being |
| H6109 | strength | Hebrew | 2 | strength,power |
| H6184 | ruthless | Hebrew | 2 | power,Ruthlessness |
| H6213I | to make: offer | Hebrew | 2 | worship,wealth |
| H6279 | to pray | Hebrew | 2 | mercy,prayer |
| H6280 | be abundant | Hebrew | 2 | deceit,being |
| H6310I | lip: word | Hebrew | 2 | counsel,testimony |
| H6345 | dread | Hebrew | 2 | dread,fear |
| H6395 | be distinguished | Hebrew | 2 | wonder,being |
| H6427 | shuddering | Hebrew | 2 | fear,terror |
| H6485I | to reckon: visit | Hebrew | 2 | longing,mind |
| H6634 | to will | Hebrew | 2 | desire,will |
| H6662 | righteous | Hebrew | 2 | innocence,justice |
| H6693 | to press | Hebrew | 2 | distress,hardness |
| H6695B | anguish | Hebrew | 2 | anguish,distress |
| H6735C | pang | Hebrew | 2 | anguish,sorrow |
| H6754 | image | Hebrew | 2 | image,likeness |
| H6862C | enemy | Hebrew | 2 | anguish,distress |
| H6862D | hard | Hebrew | 2 | distress,hardness |
| H6869B | distress | Hebrew | 2 | anguish,distress |
| H6918G | holy | Hebrew | 2 | consecration,holiness |
| H6942G | to consecrate: consecate | Hebrew | 2 | consecration,holiness |
| H6942H | to consecrate: dedicate | Hebrew | 2 | consecration,holiness |
| H6942J | to consecrate: prepare | Hebrew | 2 | consecration,holiness |
| H6942K | to consecrate: holiness | Hebrew | 2 | consecration,holiness |
| H6944G | holiness | Hebrew | 2 | consecration,holiness |
| H6960A | to await | Hebrew | 2 | hope,trust |
| H6978 | might | Hebrew | 2 | power,might |
| H7043 | to lighten | Hebrew | 2 | contempt,Cursing |
| H7110B | splinter | Hebrew | 2 | anger,wrath |
| H7114A | be short | Hebrew | 2 | endurance,being |
| H7115 | shortness | Hebrew | 2 | anguish,brokenness |
| H7121G | to call: call to | Hebrew | 2 | calling,name |
| H7121H | to call: call by | Hebrew | 2 | calling,name |
| H7186 | severe | Hebrew | 2 | hardness,stubbornness |
| H7200G | to see: see | Hebrew | 2 | discernment,experience |
| H7200H | to see: examine | Hebrew | 2 | experience,understanding |
| H7265 | to enrage | Hebrew | 2 | anger,wrath |
| H7287A | to rule | Hebrew | 2 | authority,dominion |
| H7292 | to be assertive | Hebrew | 2 | boldness,being |
| H7293 | Rahab | Hebrew | 2 | pride,strength |
| H7296 | pride | Hebrew | 2 | pride,strength |
| H7300 | to roam | Hebrew | 2 | mourning,dominion |
| H7308 | spirit | Hebrew | 2 | mind,spirit |
| H7349 | compassionate | Hebrew | 2 | compassion,mercy |
| H7356A | womb | Hebrew | 2 | compassion,mercy |
| H7359 | compassion | Hebrew | 2 | compassion,mercy |
| H7363A | be weak | Hebrew | 2 | weakness,being |
| H7375 | be fresh | Hebrew | 2 | renewal,being |
| H7390 | tender | Hebrew | 2 | gentleness,weakness |
| H7399 | property | Hebrew | 2 | goodness,wealth |
| H7423B | slackness | Hebrew | 2 | deceit,sloth |
| H7442B | to sing | Hebrew | 2 | joy,rejoicing |
| H7451A | bad: harmful | Hebrew | 2 | distress,evil |
| H7451B | bad: evil | Hebrew | 2 | evil,wickedness |
| H7451H | bad: evil | Hebrew | 2 | evil,hardness |
| H7489B | to shatter | Hebrew | 2 | brokenness,evil |
| H7496 | shade | Hebrew | 2 | spirit,deadness |
| H7503 | to slacken | Hebrew | 2 | weakness,sloth |
| H7520 | to watch with envy | Hebrew | 2 | envy,hatred |
| H7522 | acceptance | Hebrew | 2 | delight,desire |
| H7564 | wickedness | Hebrew | 2 | sin,wickedness |
| H7589 | scorn | Hebrew | 2 | malice,contempt |
| H7602A | to long for | Hebrew | 2 | desire,longing |
| H7646 | to satisfy | Hebrew | 2 | contentment,endurance |
| H7650 | to swear | Hebrew | 2 | covenant,Cursing |
| H7661 | agony | Hebrew | 2 | agony,anguish |
| H7725G | to return: return | Hebrew | 2 | repentance,thought |
| H7737B | to set | Hebrew | 2 | yielding,likeness |
| H7739A | be like | Hebrew | 2 | likeness,being |
| H7739B | be set | Hebrew | 2 | likeness,being |
| H7760M | to set: name | Hebrew | 2 | calling,name |
| H7802 | Shushan-eduth | Hebrew | 2 | covenant,testimony |
| H7881 | meditation | Hebrew | 2 | meditation,prayer |
| H7901J | to lie down: be dead | Hebrew | 2 | deadness,being |
| H7907 | heart | Hebrew | 2 | mind,heart |
| H7924 | insight | Hebrew | 2 | insight,understanding |
| H7961 | at ease | Hebrew | 2 | contentment,peace |
| H7965I | peace: well-being | Hebrew | 2 | peace,being |
| H7965J | peace: friendship | Hebrew | 2 | peace,trust |
| H7971G | to send: depart | Hebrew | 2 | calling,mourning |
| H7980 | to domineer | Hebrew | 2 | authority,dominion |
| H7981 | to rule | Hebrew | 2 | power,authority |
| H7983 | power | Hebrew | 2 | power,authority |
| H7985 | dominion | Hebrew | 2 | authority,dominion |
| H7989 | domineering | Hebrew | 2 | power,authority |
| H7990 | ruling | Hebrew | 2 | power,authority |
| H7999B | to ally | Hebrew | 2 | covenant,peace |
| H8034 | name | Hebrew | 2 | calling,name |
| H8074H | be desolate: appalled | Hebrew | 2 | wonder,being |
| H8078 | horror | Hebrew | 2 | despair,dread |
| H8085H | to hear: obey | Hebrew | 2 | obedience,listen |
| H8085I | to hear: proclaim | Hebrew | 2 | calling,listen |
| H8085J | to hear: understand | Hebrew | 2 | understanding,listen |
| H8104I | to keep: look at | Hebrew | 2 | devotion,indignation |
| H8172 | to lean | Hebrew | 2 | trust,comfort |
| H8175C | to know | Hebrew | 2 | dread,fear |
| H8262 | to detest | Hebrew | 2 | abomination,defilement |
| H8264 | to rush | Hebrew | 2 | appetite,longing |
| H8267 | deception | Hebrew | 2 | deceit,slander |
| H8307 | stubbornness | Hebrew | 2 | imagination,stubbornness |
| H8312 | anxiety | Hebrew | 2 | anxiety,thought |
| H8403 | pattern | Hebrew | 2 | image,likeness |
| H8419 | perversity | Hebrew | 2 | deceit,perverseness |
| H8424 | grief | Hebrew | 2 | grief,sorrow |
| H8469 | supplication | Hebrew | 2 | grace,mercy |
| H8535 | complete | Hebrew | 2 | innocence,integrity |
| H8539 | to astounded | Hebrew | 2 | fear,wonder |
| H8544 | likeness | Hebrew | 2 | image,likeness |
| H8552 | to finish | Hebrew | 2 | innocence,uprightness |
| H8581 | to abhor | Hebrew | 2 | abomination,rejection |
| H8617 | standing | Hebrew | 2 | strength,power |
| H8632B | might | Hebrew | 2 | strength,might |
| H8649B | deceitfulness | Hebrew | 2 | deceit,treachery |
| H8655 | teraphim | Hebrew | 2 | idolatry,image |
