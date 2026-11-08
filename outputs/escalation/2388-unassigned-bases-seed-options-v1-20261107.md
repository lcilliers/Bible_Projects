# #2388 Bases not yet in a collection: summary and seed options (v1, 2026-11-07)

> Inferential (B:4): the clusters and subgroups come from surface_subgroup (provisional); nothing here is confirmed. Read-only: no table was written. Source tables read: surface_term (cfg_table.use, cfg_column.use for group, base_id, base_state, collection_state), collection_link, surface_subgroup, cluster_subgroup, verse_lexical.

## 1. What is not yet assigned

A base is a surface_term row whose collection_state is untouched (in no collection and not listed). Live rows only.

| group | form | bases untouched |
|---|---|---|
| NULL (never judged) | word | 103 |
| behaviour | phrase | 378 |
| behaviour | word | 224 |
| entity | word | 17 |
| inner_being_state | phrase | 788 |
| inner_being_state | word | 381 |
| other | word | 11 |

- **Words in scope (behaviour or inner_being_state): 605** (381 inner_being_state, 224 behaviour). These are the seed material.
- **Phrases: 1166**, all base_state phrase_not_tested. Ruling D2: a phrase is assigned last, so they are not seeded here.
- **103 computed bases (origin computed) have no group at all** (examples: brother, day, ash, begin, cost). A computed base is not a corpus surface, so its group was never judged. They cannot be seeded until a group is set. Open question for the researcher: judge their group first, or leave them out.

Base_state of the 605 words: resolved_own 301, ai_none 197, matched_sibling 62, ai_failed 23, matched_structure 20, ai_answered 2.

Share of a word base's subgroup pairs that fall in its dominant M cluster: 50 to 79% 213, 80% or more 260, under 50% 132.

## 2. Seed option A: dominant M cluster

For each word base: take every surface that has it as its base, count their surface_subgroup pairs per M cluster, and take the cluster with most pairs. The proposed seed for a cluster is its word base with most verse occurrences among those whose dominant share is 80% or more (so the cluster is clear). Bases below 80% are listed as mixed and need a judge or the researcher.

| M cluster | name | word bases | clear (80%+) | proposed seed (occurrences) | next candidates |
|---|---|---|---|---|---|
| M23 | Strength & Courage | 42 | 22 | might (273) | mighty, strengthen, large, prevail |
| M24 | Faintness & Despair | 40 | 15 | famine (111) | dry, torn, wither, barren |
| M25 | Life & Death | 24 | 12 | live (879) | die, kill, alive, arise |
| M05 | Kindness & Friendship | 21 | 11 | kiss (51) | produce, tender, adorned, fellowship |
| M15 | Knowing & Understanding | 21 | 6 | taste (32) | train, suppose, insight, gaze |
| M45 | Renewal & Transformation | 20 | 9 | new (96) | covered, change, covers, exchange |
| M42 | Prayer & Petition | 17 | 4 | invite (42) | supplication, entreaty, interceding |
| M12 | Righteousness & Integrity | 17 | 7 | righteous (537) | upright, innocent, complete, equity |
| M18 | Desire & Longing | 16 | 4 | ready (65) | cold, pant, dear |
| M65 | Speech & Tongue | 15 | 6 | speak (1134) | saying, vision, preach, doctrine |
| M16 | Wisdom & Folly | 13 | 5 | gather (303) | folly, conceive, crafty, intimate |
| M33 | Rest & Peace | 12 | 4 | light (236) | settle, visit, deaf |
| M06 | Malice & Enmity | 11 | 2 | surround (22) | strange |
| M08 | Pride & Arrogance | 11 | 7 | above (137) | height, stature, span, willful |
| M57 | Corruption & Perversion | 10 | 5 | adultery (31) | burst, adulterers, adulterous, degenerate |
| M34 | Patience & Perseverance | 10 | 7 | forever (475) | always, sit, eternal, everlasting |
| M21 | Fasting & Piety | 10 | 1 | piety (1) |  |
| M10 | Violence & Cruelty | 10 | 2 | consumes (10) | combat |
| M74 | Keeping & Guarding | 9 | 4 | guard (126) | watch, performing, tends |
| M01 | Fear & Awe | 9 | 4 | awe (10) | quaked, quakes, cautious |
| M04 | Joy & Gladness | 9 | 4 | aroma (41) | gladden, smile, entertain |
| M36 | Worship & Service | 9 | 3 | minister (82) | result, cultivate |
| M72 | Authority & Dominion | 9 | 6 | reign (323) | only, chief, mastered, mastery |
| M44 | Covenant & Fellowship | 9 | 6 | partake (6) | impart, solemn, united, unity |
| M22 | Praise & Song | 9 | 5 | magnify (14) | renown, nourished, excelled, nourishes |
| M28 | Envy & Greed | 8 | 5 | whoring (34) | whoredom, sensual, misconduct, self-seeking |
| M73 | Sickness & Weakness | 8 | 5 | disease (86) | sickness, defeat, illness, ailment |
| M76 | Walk & Conduct | 8 | 4 | flee (243) | drive, wander, stray |
| M26 | Judgment & Condemnation | 8 | 4 | repay (43) | virtue, chide, impartial |
| M03 | Grief & Lament | 8 | 5 | fruit (189) | woe, tumult, deeply, howl |
| M48 | Astonishment & Wonder | 7 | 4 | wonders (51) | marvel, difficult, confused |
| M61 | Purity & Holiness | 7 | 4 | ordain (11) | imperishable, sharpen, rational |
| M30 | Rebellion & Stubbornness | 7 | 3 | shut (56) | deserts, wayward |
| M47 | Inner Seat | 7 | 4 | within (91) | conscience, double, heart’s |
| M64 | Will & Resolve | 7 | 1 | intend (21) |  |
| M71 | Glory & Splendor | 6 | 0 | -- none clear |  |
| M14 | Deceit & Falsehood | 6 | 3 | steal (21) | fleeting, flatter |
| M56 | Sin & Guilt | 6 | 0 | -- none clear |  |
| M63 | Reasoning & Interpretation | 6 | 0 | -- none clear |  |
| M55 | Destruction & Ruin | 6 | 4 | devour (67) | error, ravage, destructive |
| M41 | Being Heard | 5 | 3 | hear (1183) | listen, attentive |
| M78 | Slavery & Bondage | 5 | 2 | burden (65) | bondage |
| M35 | Being Tested | 5 | 2 | test (102) | character |
| M77 | Stumbling & Trial | 5 | 3 | stumble (68) | entice, hindrance |
| M53 | Dishonor & Disgrace | 5 | 1 | filthy (7) |  |
| M83 | Seeking & Inquiring | 5 | 2 | seek (402) | search |
| M10c | Defilement | 5 | 3 | unclean (266) | uncleanness, pollutes |
| M11 | Turning & Repentance | 5 | 1 | without (182) |  |
| M09 | Humility & Lowliness | 4 | 1 | deeper (11) |  |
| M32 | Covenant | 4 | 4 | uncircumcised (47) | assign, uncircumcision, circumcise |
| M07 | Shame & Confusion | 4 | 1 | blush (4) |  |
| M37 | Firstborn & Foreknowledge | 4 | 0 | -- none clear |  |
| M69 | Self-Control & Zeal | 4 | 1 | sober (9) |  |
| M02 | Anger & Wrath | 4 | 1 | fret (2) |  |
| M20 | Doubt & Discouragement | 4 | 3 | hid (42) | murmur, double-minded |
| M58 | Wickedness | 4 | 3 | evildoer (61) | rotten, serious |
| M84 | Outcry & Shouting | 4 | 2 | roar (51) | mutter |
| M75 | Disobedience & Lawlessness | 4 | 2 | lawless (16) | laden |
| M50 | Grace & Mercy | 4 | 4 | sight (300) | partial, loyalty, tenderhearted |
| M31 | Faith | 3 | 2 | backsliding (4) | religion |
| M13 | Faith & Faithfulness | 3 | 1 | real (1) |  |
| M80 | Blessing | 3 | 1 | walk (177) |  |
| M46 | Wealth & Riches | 3 | 1 | heritage (56) |  |
| M68 | Hope & Waiting | 3 | 0 | -- none clear |  |
| M67 | Sloth & Diligence | 3 | 0 | -- none clear |  |
| M19 | Trust & Refuge | 3 | 0 | -- none clear |  |
| M82 | Reminder & Report | 3 | 1 | witness (152) |  |
| M39 | Gift & Favor | 2 | 2 | reward (48) | adornment |
| M62 | Truth & Sincerity | 2 | 2 | establishes (5) | irrevocable |
| M52 | Encouragement | 1 | 1 | build (138) |  |
| M59 | Release & Reconciliation | 1 | 0 | -- none clear |  |
| M60 | Confession & Forgiveness | 1 | 1 | profess (2) |  |
| M43 | Prophecy & Vision | 1 | 1 | prophesy (134) |  |
| M81 | Memory (act) | 1 | 1 | recount (7) |  |

A cluster is wider than a collection (a collection is a core word with synonyms and an opposite pole), so one cluster will give several collections. Option A gives the cluster, not the collection count; the dominant sub-cluster (option B) narrows it.

## 3. Seed option B: dominant sub-cluster

Same count, one level down: the cluster subgroup (cluster_subgroup.kind: group, qualifier, not_this_sense or anomaly). Top subgroups by number of word bases:

| cluster | subgroup | label | kind | word bases | proposed seed (occurrences) |
|---|---|---|---|---|---|
| M24 | M24_not_this_sense | Not the cluster's sense | not_this_sense | 15 | alone (126) |
| M05 | M05_not_this_sense | Not the cluster's sense | not_this_sense | 10 | appear (189) |
| M42 | M42_supplication | Supplication, pleading, begging | group | 9 | beg (39) |
| M25 | M25_not_this_sense | Not the cluster's sense | not_this_sense | 9 | arise (68) |
| M23 | M23_not_this_sense | Not the cluster's sense | not_this_sense | 9 | old (356) |
| M08 | M08_not_this_sense | Not the cluster's sense | not_this_sense | 8 | high (165) |
| M34 | M34_perpetuity | Forever, ever, always (a quality of time) | qualifier | 7 | forever (475) |
| M44 | M44_companionship | Companionship, sharing, brotherhood | group | 7 | share (44) |
| M65 | M65_word | Word, words, saying | group | 6 | saying (832) |
| M24 | M24_suffering | Suffering, pain, pangs | group | 6 | wound (74) |
| M25 | M25_living | Living, being alive | group | 6 | live (879) |
| M15 | M15_not_this_sense | Not the cluster's sense | not_this_sense | 6 | can (372) |
| M12 | M12_not_this_sense | Not the cluster's sense | not_this_sense | 6 | full (193) |
| M15 | M15_thinking | Thinking, supposing, judging | group | 6 | thought (110) |
| M23 | M23_power | Power, might, mighty works | group | 6 | work (586) |
| M22 | M22_not_this_sense | Not the cluster's sense | not_this_sense | 6 | much (537) |
| M73 | M73_sickness | Sickness, disease, illness | group | 5 | disease (86) |
| M21 | M21_asking | Asking, inquiring | group | 5 | ask (329) |
| M61 | M61_not_this_sense | Not the cluster's sense | not_this_sense | 5 | become (271) |
| M16 | M16_not_this_sense | Not the cluster's sense | not_this_sense | 5 | first (343) |
| M33 | M33_not_this_sense | Not the cluster's sense | not_this_sense | 5 | set (378) |
| M23 | M23_prevailing | Prevailing, conquering, overcoming | group | 4 | prevail (49) |
| M24 | M24_distress | Distress, trouble, anguish | group | 4 | trouble (150) |
| M48 | M48_marvelling | Marvelling, astonishment, amazement | group | 4 | marvel (41) |
| M05 | M05_doing_good | Doing good, generosity | group | 4 | generous (17) |
| M76 | M76_astray | Going astray, staggering | group | 4 | astray (46) |
| M36 | M36_ministry | Service, ministry, ministering | group | 4 | do (990) |
| M24 | M24_breaking | Breaking, broken, shattered | group | 4 | break (169) |
| M78 | M78_burden | Burden, load | group | 4 | carry (153) |
| M30 | M30_restraining | Restraining, withholding, shutting up | group | 4 | shut (56) |
| M18 | M18_not_this_sense | Not the cluster's sense | not_this_sense | 4 | get (47) |
| M23 | M23_strength | Strength, being strong, strengthening | group | 4 | strength (196) |
| M28 | M28_whoring | Whoring, prostitution, unfaithfulness | group | 4 | whoring (34) |
| M25 | M25_dying | Dying, being dead | group | 4 | die (619) |
| M55 | M55_destroying | Destroying, the destroyer | group | 4 | destruction (113) |
| M64 | M64_devising | Devising, planning, purposing | group | 4 | purpose (64) |
| M24 | M24_withering | Withering, drying up | group | 4 | whole (295) |
| M06 | M06_not_this_sense | Not the cluster's sense | not_this_sense | 4 | means (45) |
| M01 | M01_trembling | Trembling, shuddering, quaking | group | 4 | shake (53) |
| M23 | M23_enlarging | Enlarging, growing great | group | 4 | grow (59) |

Full data (every word base with its members, occurrences, dominant cluster, share, dominant subgroup): outputs/escalation/2388-unassigned-word-bases-v1-20261107.json.

## 4. Bases that should not be a behaviour or state

Heuristic, inferential (B:4): a word base that is on a short list of quantifiers, modals and adverbs, or whose AI base answer was none and that occurs 150 times or more. This finds candidates; it does not decide them. The group judge gave "all" the group inner_being_state with the reason that "all the heart" is a total state, which is why such words got in.

| base | group | occurrences | base_state | judge reason (group) |
|---|---|---|---|---|
| all | inner_being_state | 5477 | ai_none | The word 'all' in the ESV Bible often refers to a comprehensive state or condition of a person's inner being,  |
| life | inner_being_state | 584 | ai_none | Life as a state of being in Scripture. |
| much | inner_being_state | 537 | ai_none | The word 'much' describes a degree or extent of a state, not an action or entity. |
| forever | inner_being_state | 475 | ai_none | The term 'forever' describes a lasting condition or state, not an action or entity. |
| can | inner_being_state | 372 | ai_none | The word 'can' in the ESV Bible typically describes a capacity or ability, which is a state of being rather th |
| first | inner_being_state | 343 | ai_none | The word 'first' describes a position or priority, not an act or entity. |
| nothing | inner_being_state | 323 | ai_none | Bible uses 'nothing' to describe a state of emptiness or lack. |
| sight | inner_being_state | 300 | ai_none |  |
| whole | inner_being_state | 295 | ai_none | The word 'whole' describes a condition of completeness or wholeness, fitting the inner_being_state definition. |
| end | inner_being_state | 277 | ai_none | The word 'end' in the ESV Bible often refers to a state or condition of the heart or inner being, such as 'the |
| light | inner_being_state | 236 | ai_none |  |
| very | inner_being_state | 216 | ai_none | The word 'very' is an adverb that intensifies an adjective or another adverb. In the ESV Bible, it does not de |
| only | inner_being_state | 200 | ai_none |  |
| full | inner_being_state | 193 | ai_none | The word 'full' describes a condition of being, such as being filled with something (e.g., full of joy, full o |
| fruit | inner_being_state | 189 | ai_none |  |
| without | inner_being_state | 182 | ai_none | The word 'without' in the ESV Bible typically describes a state or condition, such as 'without sin' or 'withou |

The group is decided per surface text (surface_term.surface_group), not per sense, so a word like "all" is judged on one text; the reason recorded for "all" cites only its inner-being uses (inferential). A correction would be surface_event with group other, or a rule. That is a design choice for the researcher (B:44, B:105): see decisions below.

## 5. Decisions needed

1. Seed rule: option A (dominant cluster), option B (dominant sub-cluster), or the dominant sub-cluster only where its share is clear and the AI judge otherwise?
2. The 103 computed bases with no group: judge their group first, or exclude?
3. Non-state words (section 4): how to take them out: a group correction to other for each confirmed word (researcher confirms the list), or a stop-word rule in config that the group step applies?
4. Relation to #2385 (dominant M-code of surfaces) and #2383 (collection rows with no strong): fold in, supersede or keep apart.
