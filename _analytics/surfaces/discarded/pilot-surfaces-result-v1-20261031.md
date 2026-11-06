# Pilot: surfaces classified by the local model (#2339)

Model qwen2.5:7b-instruct, Ollama, CPU only. Read-only; nothing written to iba/app/db/iba.db. Phrases and group names are the model's output: inferential (B:4), not confirmed.

## Measures
- rows run: 200 of 200; valid output: 200 (100%)
- seconds per surface: mean 8.2, max 23.7; sum 27 min for 200 rows
- repeat (temperature 0.5 against the temperature 0 run), 20 rows: identical phrase 16, at least one word shared 20

## Groups (2 named; phrases 174; unplaced 7)
- **anger** (15 surfaces; {'feeling': 15}): to wrath (H7107); incensed (H2734); temper (H0639G); jealous (H7072); trembling (H7578); fearful (H3372G); tremble (H7264); terror (H4032); trembled (H7264); envy (H7068); brokenhearted (H7665); afraid (H1763)
- **blessing** (190 surfaces; {'feeling': 93, 'other': 58, 'authority_M72': 20, 'wealth_M46': 19}): happier (G3107); call her blessed (H0833); break (H7665); fanned (H5301); longs (H6315); up (G2026); cry (G0994); quieted (G2687); mischief (H5999); troubled (H6470); trouble yourself (G4660); trouble (H1804)

## Every sampled row (stratum, surface, strong, model phrase)

| stratum | surface | strong | model phrase | secs |
|---|---|---|---|---|
| feeling | anguish | H6088 | suffering, sorrow | 23.7 |
| feeling | rejoiced | G4796 | joy, celebration | 9.8 |
| feeling | oppressors | H3905 | tyrants, exploitation | 8.9 |
| feeling | terrifying | H3372G | fear and intimidation | 7.6 |
| feeling | happier | G3107 | blessing, happiness | 8.5 |
| feeling | envy | H7068 | emotions, desires | 7.5 |
| feeling | groaning | H0585 | sorrow, distress | 7.2 |
| feeling | rejoices | H5970 | joy, celebration | 7.4 |
| feeling | hopes | G1680 | future expectations | 7.7 |
| feeling | take heart | G2114 | courage and joy | 8.9 |
| feeling | to wrath | H7107 | anger and displeasure | 9.1 |
| feeling | trembled | H7264 | emotional states, reactions | 9.5 |
| feeling | pleasure | G2237 | Sensual indulgence | 9.0 |
| feeling | perplexed | G1280 | confusion, wonder | 8.4 |
| feeling | enjoyment | H5965 | joy, celebration | 7.5 |
| feeling | be afraid | G5399 | fear and alarm | 9.1 |
| feeling | delight | H7797 | joy, celebration | 7.3 |
| feeling | looking forward | G1551 | waiting, expecting | 8.6 |
| feeling | woe | G3759 | judgment, lament | 10.4 |
| feeling | plunder | H0957 | warfare, loot | 8.2 |
| feeling | wither | H5034B | plant decay | 6.7 |
| feeling | rejoices | G5463 | joy, celebration | 7.7 |
| feeling | tremble | H7264 | emotional response, disturbance | 9.7 |
| feeling | jealous | H7072 | Emotional response | 6.7 |
| feeling | got relief | H5118 | Rest, Peace | 7.9 |
| feeling | tears | H1832 | emotional distress | 6.9 |
| feeling | rest | H8252 | Peace and Quiet | 9.1 |
| feeling | wait | H7663B | patience, expectation | 7.2 |
| feeling | broken down | H7665 | Destruction | 7.8 |
| feeling | dispute | G0485 | conflict, disagreement | 9.4 |
| feeling | fade | H5243A | decay | 8.3 |
| feeling | prostitute | H2181 | sexual misconduct | 8.5 |
| feeling | cruel man | H2556C | oppression | 7.0 |
| feeling | immorality | H2183 | sexual misconduct | 7.0 |
| feeling | worked | G2872 | labor and work | 9.6 |
| feeling | trembling | H7578 | emotional response | 7.3 |
| feeling | entertained | H6711 | laughter, mockery | 8.1 |
| feeling | woe | H0190 | judgment, lament | 7.3 |
| feeling | exceedingly | H7068 | emotions, passion | 8.2 |
| feeling | quieted | G2687 | calming, pacifying | 9.0 |
| feeling | troubled | G1568 | awe and fear | 9.3 |
| feeling | affliction | H6869B | suffering, hardship | 7.2 |
| feeling | weakening | H7503 | Physical and emotional weakening | 8.8 |
| feeling | shakes | H7264 | emotional disturbance | 10.5 |
| feeling | rejoicing | H8056 | joy and happiness | 7.8 |
| feeling | deeply | H4751 | bitter taste | 8.5 |
| feeling | incensed | H2734 | anger and fury | 10.1 |
| feeling | terror | H2189 | fearful experiences | 8.8 |
| feeling | stirring up | G5015 | emotional disturbance | 9.2 |
| feeling | afraid | H1763 | emotions, fear | 7.0 |
| feeling | lament | H5594 | mourning, sorrow | 8.9 |
| feeling | call her blessed | H0833 | blessing, progress | 8.6 |
| feeling | exults | H5937 | rejoicing, triumphing | 7.6 |
| feeling | terror on every side | H4036 | Terror and Fear | 9.9 |
| feeling | lust | H1942 | sexual欲望 | 6.8 |
| feeling | celebrated | H7832 | laughter, mockery | 7.6 |
| feeling | toil | H8383 | Labor, work | 7.2 |
| feeling | covetousness | G4124 | desire for wealth | 7.8 |
| feeling | gladden | H8055 | joy, happiness | 6.9 |
| feeling | fearful | H3372G | emotional response | 6.7 |
| feeling | brokenhearted | H7665 | emotions, destruction | 7.8 |
| feeling | troubled | H6470 | causing distress | 7.5 |
| feeling | gladness | H8057 | emotional happiness | 7.3 |
| feeling | disputing | G1261 | arguments and discussions | 7.8 |
| feeling | keep silence | H2814 | Silence and quietness | 7.4 |
| feeling | temper | H0639G | anger expression | 6.5 |
| feeling | weak | G0770G | physical or mental weakness | 6.7 |
| feeling | rare | H3368 | value and rarity | 7.1 |
| feeling | respite | H1826A | silence, stillness | 7.3 |
| feeling | heat | H2740 | God's anger | 7.1 |
| feeling | holiday | H2896A | pleasure | 6.4 |
| feeling | happiness | H2896A | pleasure, enjoyment | 7.5 |
| feeling | pleasant | H2530A | desire | 6.7 |
| feeling | awe | G6015 | religious respect | 8.6 |
| feeling | desires | H0183 | Desires and cravings | 11.3 |
| feeling | terror | H2851 | emotional fear | 7.3 |
| feeling | destruction | H7670 | physical or mental breaking apart | 8.2 |
| feeling | trouble | H1804 | causing disturbance | 8.8 |
| feeling | oppress | H3905 | forceful treatment | 8.0 |
| feeling | dries up | H3001 | drying, withering | 10.3 |
| feeling | grieved | H3510 | suffering, sorrow | 8.5 |
| feeling | trouble yourself | G4660 | causing distress | 9.7 |
| feeling | troubled | H0926 | emotional distress | 8.7 |
| feeling | happy | H8056 | joy, happiness | 7.7 |
| feeling | brought | H1809 | Condition, hanging | 8.1 |
| feeling | break | H7665 | Breaking, destruction | 8.2 |
| feeling | lamentation | G3602 | funeral sorrow | 8.9 |
| feeling | wait | G1551 | waiting, expectation | 8.8 |
| feeling | ignorant | G0050 | Lack of knowledge | 7.7 |
| feeling | glory | H3368 | Value and Rarity | 7.9 |
| feeling | choice | H2532A | preferences | 6.9 |
| feeling | ambition | G5389 | aspiring to honor | 8.2 |
| feeling | tormentors | H3013 | suffering, affliction | 8.8 |
| feeling | honor | H5082 | respect and dignity | 7.4 |
| feeling | godliness | G2150 | religious virtue | 8.2 |
| feeling | terror | H4032 | emotional state | 6.7 |
| feeling | fierce | H2740 | God's anger | 7.2 |
| feeling | rejoice | G5463 | joy, celebration | 7.9 |
| feeling | distress | H4691 | suffering situations | 7.1 |
| feeling | dread | H0367 | emotional fear | 8.2 |
| wealth_M46 | multitude | H7230 | groups, quantities | 7.2 |
| wealth_M46 | heritages | H5159 | family legacy | 7.2 |
| wealth_M46 | success | H6743B | prosperity | 6.8 |
| wealth_M46 | possession | H5159 | legal rights, property | 8.7 |
| wealth_M46 | abundantly | H7230 | quantity, abundance | 9.3 |
| wealth_M46 | wealth | H2633 | economic resources | 8.4 |
| wealth_M46 | prospered | G4147 | wealth and prosperity | 10.9 |
| wealth_M46 | plentiful | H7230 | quantity, abundance | 8.4 |
| wealth_M46 | secure | H7951 | Prosperity, Security | 10.2 |
| wealth_M46 | strongest | H4924B | abundance | 8.0 |
| wealth_M46 | untroubled | H7600 | peace of mind | 9.0 |
| wealth_M46 | abundance | H3502 | economic prosperity | 8.3 |
| wealth_M46 | prospers | H6743B | success, flourishing | 8.2 |
| wealth_M46 | wealth | H1991 | material prosperity | 7.5 |
| wealth_M46 | rich | G4147 | Wealth and prosperity | 9.4 |
| wealth_M46 | luxury | H8082 | wealth and abundance | 7.7 |
| wealth_M46 | acquire wealth | H6238 | wealth and riches | 7.9 |
| wealth_M46 | great quantities | H7230 | quantities, abundance | 7.4 |
| wealth_M46 | greatly | H7230 | quantity, magnitude | 7.2 |
| wealth_M46 | inheritances | H5159 | property rights | 7.3 |
| authority_M72 | authority over | G1850 | Power dynamics | 8.3 |
| authority_M72 | queen | H4427A | royal authority | 6.8 |
| authority_M72 | dominion | H4910 | Ruling, governance | 7.9 |
| authority_M72 | years | H4427A | royal rule | 7.0 |
| authority_M72 | order | H3027H | Power and authority | 7.7 |
| authority_M72 | kings | H4430 | royalty and leadership | 10.3 |
| authority_M72 | authority | H4474 | power and governance | 7.7 |
| authority_M72 | royal | G0937 | royalty, kingship | 10.0 |
| authority_M72 | kings | G0936 | royal authority | 8.2 |
| authority_M72 | helpless | H3027H | strength, ability | 6.9 |
| authority_M72 | get dominion | H7980 | power and control | 8.8 |
| authority_M72 | mastered | G2634 | dominion and control | 10.0 |
| authority_M72 | surrendered | H3027H | submission, offering | 7.4 |
| authority_M72 | king’s | H4428G | royalty | 7.1 |
| authority_M72 | service | H3027H | Labor, work | 7.0 |
| authority_M72 | leading | G2233 | Leadership and Governance | 8.1 |
| authority_M72 | seats | H3678G | royal authority | 7.8 |
| authority_M72 | chiefs | H8269 | Leadership and Authority | 9.3 |
| authority_M72 | kingship | H4437 | royal authority | 7.3 |
| authority_M72 | elementary | G0746 | Initial positions or authorities | 9.5 |
| other | cry | G0994 | calling out, shouting | 9.4 |
| other | greatly | H7451I | suffering: adversity | 6.9 |
| other | enticed | H6601B | Deception, temptation | 7.1 |
| other | had | H6113 | Restraint and prohibition | 8.4 |
| other | care | H8104H | guarding, protection | 7.3 |
| other | strong | G2901 | strength, reinforcement | 7.9 |
| other | take | H5358 | vengeance | 7.8 |
| other | storm | H4421 | conflict | 7.4 |
| other | consider | H0995 | Perception and Understanding | 7.5 |
| other | distinguish between | G1253 | Judgment and distinction | 8.5 |
| other | unloved | H8130 | hatred | 7.0 |
| other | chosen | G0140 | Selection, Favor | 8.7 |
| other | stronger | H0555 | physical or mental power | 7.2 |
| other | put confidence | H0982 | Faith and Trust | 8.4 |
| other | liars | H1696G | speaking | 7.6 |
| other | small | H3190 | feelings, emotions | 8.0 |
| other | endeavor | G2212 | seeking, striving | 9.8 |
| other | and | H1320 | Human physicality | 7.0 |
| other | choice | H0977 | Selection process | 7.4 |
| other | mischief | H5999 | causes, difficulties | 7.6 |
| other | valiant | H2428G | strength and courage | 6.6 |
| other | fanned | H5301 | Breathing, blowing | 8.2 |
| other | submitting | G5293 | submission, obedience | 9.4 |
| other | bright | H1249 | Purity | 6.5 |
| other | magnificent | H1431 | Growth and Honor | 8.1 |
| other | hidden | H2934 | concealment | 7.2 |
| other | vile | G5337 | morality, ethics | 8.9 |
| other | answered | H1697G | Response, reply | 6.5 |
| other | dress | H2388G | strengthening | 6.9 |
| other | service | H5656H | religious duty | 7.2 |
| other | breathed | H5397 | Life, Existence | 8.8 |
| other | fails | H2398 | sin and failure | 8.3 |
| other | paneling | H5603 | Interior decoration | 8.0 |
| other | judge | H8199 | legal and governance roles | 8.1 |
| other | meaning | G1411 | Power and Ability | 11.1 |
| other | outlived | H0748 | Duration, longevity | 7.5 |
| other | built | G3618 | Construction, Strengthening | 10.0 |
| other | valiant man | H2428G | strength | 6.1 |
| other | set up | H7311A | Exalting, elevating | 7.5 |
| other | prophesying | G4395 | divine messages, prophecy | 9.2 |
| other | creature | H1320 | human body | 6.7 |
| other | more evil | G4190 | moral negativity | 9.7 |
| other | awakens | H5782 | Awakening, Rousing | 8.2 |
| other | planned | H2161 | planning, intention | 7.5 |
| other | slanders | H7400 | false speech | 6.5 |
| other | stirred | H5782 | Awakening, Incitement | 8.5 |
| other | destroy | G2506 | demolition, destruction | 8.3 |
| other | kept ready | H8245 | Watchfulness, vigilance | 7.9 |
| other | upright | H2896A | pleasure | 6.5 |
| other | prevail | G2480 | Strength and Power | 8.5 |
| other | tested | H0974 | testing, examination | 7.4 |
| other | punish | G1557 | justice, punishment | 8.8 |
| other | up | G2026 | Building up structures | 8.6 |
| other | forgetting | G1950 | Memory and Neglect | 9.1 |
| other | became broader | H7337 | Expansion, Widening | 8.9 |
| other | pure | H5343 | Purity, cleanliness | 8.1 |
| other | wonders | H6381 | Miracles, Astonishment | 9.5 |
| other | pain | H3176G | waiting | 6.7 |
| other | longs | H6315 | breathing, blowing | 7.9 |
| other | stronger | G2478 | Strength, Power | 9.4 |
