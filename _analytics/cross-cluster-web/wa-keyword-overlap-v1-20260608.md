# Cluster keyword overlap (roll-up angle 5)

> READ-ONLY (`scripts/_assess_keyword_overlap.py`). Each cluster's keyword set from its terms' STEP meaning (whole-word, P1 filters); pairwise Jaccard. Correlate to angle 1: do co-occurring clusters also share meaning-vocabulary, or is the link purely contextual? No DB writes.

## A · Most keyword-similar cluster pairs (top 30 by Jaccard)

| Cluster A | Cluster B | shared kw | Jaccard | sample shared |
|---|---|---|---|---|
| Repentance | Transformation | 51 | 0.23 | allow, answer, apostatise, away, back, backward |
| Grief | Weakness | 69 | 0.16 | afflict, afflicted, agony, angry, anguish, band |
| Speech | Prophecy | 22 | 0.13 | aramaic, continued, divine, encouraging, faculty, forth |
| Prayer | Remembrance | 28 | 0.10 | ask, care, cause, demand, desire, earnestly |
| Pride | Folly | 23 | 0.10 | act, become, boast, boasters, boastful, commended |
| Strength | Perseverance | 62 | 0.10 | action, aramaic, authority, bear, bearing, become |
| Love | Blessing | 50 | 0.09 | act, aramaic, bearing, beneficence, benefit, bestow |
| Hope | Trust | 20 | 0.09 | bent, confidence, desire, eager, earnest, earnestly |
| Righteousness | Faith | 29 | 0.09 | actions, called, charge, conviction, credit, found |
| Strength | Righteousness | 60 | 0.09 | abba, almighty, baal, banner, being, called |
| Joy | Blessing | 23 | 0.09 | act, aramaic, beauty, benefit, desire, equivalent |
| Pride | Praise | 29 | 0.09 | act, aramaic, boast, boasters, boastful, commended |
| Wickedness | Evil | 17 | 0.09 | abominable, bad, corrupt, deeds, detestable, evil |
| Wisdom | Righteousness | 48 | 0.08 | account, act, calculate, called, cause, charge |
| Righteousness | Peace | 32 | 0.08 | abba, almighty, avenging, baal, banner, called |
| Repentance | Obedience | 20 | 0.08 | away, become, care, cause, come, depart |
| Love | Peace | 48 | 0.08 | blessing, cheering, clemency, comfort, compassion, consolation |
| Love | Strength | 71 | 0.08 | active, activity, advance, aramaic, bearing, become |
| Sin | Deceit | 27 | 0.08 | act, aside, bait, corrupt, crookedness, deal |
| Truth | Faith | 18 | 0.08 | belief, believer, christian, confidence, credit, faith |
| Peace | Perseverance | 28 | 0.08 | action, anxiety, circumstance, control, delaying, difficult |
| Truth | Trust | 18 | 0.08 | adv, bear, belief, certain, confidence, confirm |
| Trust | Perseverance | 23 | 0.07 | assist, bear, bring, confidence, eager, earnest |
| Wisdom | Strength | 62 | 0.07 | ability, address, aramaic, bring, called, christ |
| Love | Prayer | 44 | 0.07 | affection, aramaic, ask, beg, beseech, care |
| Wisdom | Remembrance | 36 | 0.07 | act, announcement, attention, bring, called, care |
| Fear | Grief | 28 | 0.07 | agitated, agony, anguish, anxiety, anxious, cause |
| Sin | Wickedness | 20 | 0.07 | contexts, corrupt, crime, depravity, detestable, evil |
| Desire | Blessing | 13 | 0.07 | acceptance, desire, favour, freely, god, goodwill |
| Love | Wisdom | 58 | 0.07 | act, aramaic, beforehand, but, care, cause |

## B · Per-cluster signature keywords (most term-frequent)

| Cluster | top keywords |
|---|---|
| Fear | terror, fear, afraid, trembling, awe, dread, fearful, terrified, reverence, dismay |
| Anger | anger, angry, indignation, provoke, strife, contention, wrath, dispute, hostility, irritate |
| Grief | pain, sorrow, distress, passive, anguish, mourning, grief, grieve, bitter, groaning |
| Joy | delight, joy, rejoice, glad, rejoicing, wonder, pleasure, gladness, aramaic, exultation |
| Love | love, compassion, kindness, pity, compassionate, good, gentleness, kind, people, loving |
| Hate | contempt, abhor, hate, adversary, cruel, despise, enemy, opponent, hating, detestable |
| Shame | shame, disgrace, ashamed, insult, dishonor, put, dishonour, ignominy, dishonorable, abuse |
| Pride | pride, proud, arrogant, arrogance, boasting, presumptuous, exalted, haughtiness, boast, lofty |
| Humility | humble, low, modest, obedience, adj, primarily, one's, respect, lowly, mind |
| Sin | sin, guilt, act, law, perversity, punishment, god, ruin, destruction, offering |
| Wickedness | evil, wickedness, wicked, wrong, abominable, detestable, abomination, god, bad, wrongdoing |
| Defilement | impure, unclean, filthiness, impurity, defilement, pollution, defile, motive, moral, uncleanness |
| Repentance | pardon, away, forgive, release, cancel, suffer, give, allow, remit, omit |
| Purity | innocent, pure, holy, sacred, devote, dedicate, consecrate, set, show, clean |
| Truth | true, faithfulness, truth, divine, truly, faithful, firmness, trustworthy, integrity, certain |
| Deceit | deceit, treachery, slander, plot, fraud, treacherous, pretend, answer, false, device |
| Wisdom | thought, consider, plan, understanding, purpose, make, think, knowledge, wisdom, mind |
| Folly | folly, foolish, foolishness, madness, fool, make, lack, wickedness, boastful, mind |
| Counsel | counsel, plan, purpose, beginning, first, decision, determination, counselor, cause, counsellor |
| Hope | hope, desire, expect, expectation, long, earnestly, longing, wait, confidence, trust |
| Trust | trust, confidence, support, refuge, self-controlled, safety, security, sure, firm, self-control |
| Doubt | perplexed, doubt, perplexity, anxious, discouraged, heart, lose, puzzled, wonder, hesitate |
| Prayer | prayer, pray, request, god, supplication, petition, ask, reverence, pious, beg |
| Praise | praise, god, glory, holiness, primarily, sanctity, holy, sacred, excellence, speaking |
| Strength | strength, power, strong, authority, mighty, dominion, rule, prevail, strengthen, force |
| Weakness | distress, ill, sick, primarily, afflicted, strength, oppress, weak, sickness, distressed |
| Life | life, breath, living, alive, live, bestowed, wind, mind, influence, influential |
| Righteousness | justice, act, right, righteous, judgment, just, sentence, righteousness, proper, primarily |
| Evil | idols, idol, evil, idolatry, primarily, heathen, sacrificed, image, wrong, cause |
| Envy | desire, desirable, lust, fornication, longing, pleasure, greedy, envy, love, lustfulness |
| Desire | willing, desire, design, pleasure, purpose, inclined, willingness, pleased, make, chooses |
| Obedience | take, rebellion, stubbornness, refrain, retain, restrain, obstinacy, hardness, perform, reserve |
| Faith | faith, trust, implication, gospel, belief, god, system, persuasion, based, follow |
| Peace | quiet, peace, rest, tranquillity, god, silent, still, silence, safety, health |
| Perseverance | struggle, strive, contend, bold, forth, earnest, strength, persevere, contest, public |
| Testing | test, trial, proof, sin, try, put, attempt, stumble, testing, character |
| Service | service, servant, slave, serve, work, labour, make, cause, slavery, servitude |
| Calling | call, summon, appoint, choose, name, invite, named, aloud, read, meet |
| Salvation | mercy, means, propitiation, god, salvation, free, gift, forgiveness, atonement, forgiven |
| Blessing | favor, gracious, gift, free, show, good, grace, kindness, pleasing, favour |
| Remembrance | call, make, hear, heard, listen, attention, cause, request, heed, report |
| Speech | cry, shout, sound, speak, utter, call, groan, voice, ringing, slander |
| Prophecy | insight, faculty, distinguishing, translate, interpret, explain, image, spiritual, warning, prophecy |
| Relational | fellow, contend, one's, self, share, part, enemy, faith, kinswoman, countrywoman |
| Transformation | change, mind, one's, repent, transform, mode, middle, changed, past, spiritual |
| Abundance | rich, riches, wealth, become, fat, wealthy, spiritually, abundantly, enriched, enrich |
