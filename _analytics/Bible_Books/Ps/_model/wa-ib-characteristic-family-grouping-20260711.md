# `ib_characteristic.family` — similarity grouping (Psalms) — for review

> Built 2026-07-11. The 877 meaning-records (§7D v3, meaning-keyed) grouped into **46 families by similarity**, written to `ib_characteristic.family` (book_scope 19). Builder: `scripts/_apply_ib_char_family_grouping_v1_20260711.py` (idempotent, re-runnable). **This is the "grouping" layer flagged as sensitive — filed here for your review; every assignment is reversible (re-run the script with edited rules, or re-map any record).**

## Method (transparent, auditable — no black box)
An **ordered keyword→family rule map** (first match wins), tested against each record's **name** first, then its **gloss + operation** as fallback. Each of the 46 families is a regex of semantic keywords; the mapping is the rule list in the script (readable, editable). Errs toward leaving a meaning **unassigned** (`other-uncategorised`) rather than force-fitting it — the residual is a deliberate honest floor, not a failure.

- **877 records → 46 families** (cap was 50).
- **2,112 of 2,168 instances assigned (97.4%)**; **56 records / 56 instances unassigned** — all singletons.

## The 46 families (by instance weight)
| family | records | instances | heaviest members |
|---|--:|--:|---|
| inner-seat-heart-soul-spirit | 31 | 185 | soul, heart, spirit, flesh |
| praise-extol-sing | 43 | 177 | Praise, sing, sing praises |
| prayer-petition-crying-out | 39 | 109 | call, prayer, cry, complaint |
| knowing-understanding | 43 | 99 | know, meditate, understanding, knowledge |
| joy-gladness | 27 | 95 | glad, rejoice, joyful noise, exult |
| desire-longing-appetite | 47 | 85 | delight, needy, crave, thirst |
| fear-of-god-awe | 24 | 79 | fear, afraid, revere |
| trust-refuge-security | 18 | 77 | trust, take refuge, refuge |
| righteousness-integrity | 25 | 69 | righteous, upright, blameless |
| blessing-benediction | 5 | 65 | bless, Blessed |
| wickedness-ungodliness | 20 | 56 | wicked, evil, wickedness, crime |
| malice-enmity-persecution | 26 | 56 | hate, plots, oppresses, curse |
| sin-guilt-iniquity | 21 | 55 | iniquity, sin, transgressions |
| faint-despair-languishing | 33 | 55 | afflicted, faint, dismayed, weary |
| thanksgiving | 6 | 49 | give thanks, thank, thanksgiving |
| keeping-guarding-vigilance | 10 | 49 | keep, observe, watch |
| walk-way-conduct | 24 | 47 | walk, wander, go astray |
| memory-remembrance | 7 | 46 | remember, forget, mindful |
| hope-waiting | 17 | 45 | hope, wait |
| deceit-falsehood | 29 | 45 | deceitful, false, falsehood, vain |
| speech-mouth-tongue | 24 | 42 | speak, declare, proclaim, tongue |
| pride-arrogance-scoffing | 26 | 42 | boast, taunt, haughty, insolent |
| wisdom-folly-teaching | 27 | 41 | wisdom, fool, wise, learn, stupid |
| seeking-inquiring | 9 | 37 | seek, sought, studied |
| love-devotion | 8 | 35 | love, clings, friends |
| will-resolve-vow-intent | 28 | 35 | perform, chosen, vows, cast, pay |
| grief-lament-sorrow | 22 | 31 | tears, groans, wept, mourning |
| rebellion-stubbornness | 20 | 31 | rebelled, rebellious, forsaken, refuses |
| shame-confusion | 13 | 28 | put to shame, reproach, dishonor |
| humility-lowliness-contrition | 16 | 27 | poor, humble, broken, contrite |
| worship-prostration-service | 13 | 25 | worship, serve, bow down, kneel |
| violence-cruelty | 14 | 21 | violence, strife, crush, ruthless |
| lifting-bearing | 7 | 21 | lift up, bear, raise |
| being-heard-listening | 6 | 20 | hear, listen, give ear |
| restoration-revival-satisfaction | 15 | 19 | comforted, satisfied, revive, redeems |
| faith-faithfulness-truth | 8 | 18 | believe, faithful, truth, faith |
| grace-mercy-compassion | 11 | 16 | mercy, pity, grace, gracious, kindness |
| anger-wrath-vexation | 14 | 15 | anger, wrath, venom |
| being-searched-tested-by-god | 7 | 14 | tested, proof, search, examine |
| turning-repentance | 12 | 14 | repent, turn, turn aside |
| rest-stillness-peace | 9 | 10 | still, silent, quieted, rest |
| life-death-vitality | 2 | 10 | life, live |
| strength-courage-steadfastness | 7 | 8 | strength, hold fast, valiantly |
| torah-obedience-word | 5 | 6 | obey, law |
| confession-forgiveness | 3 | 3 | confess, pardon |

## Honest caveats (for your review)
1. **`other-uncategorised` (56 singletons)** — genuine miscellany that shouldn't be forced: `judge, sacrificed, whore, unfaithful, knees, murder, war, injustice, laughter, anxious, cares, harden, hide, dwell, toil…`. Some are borderline (e.g. *anxious/cares* → could join faint-despair; *murder/war/injustice* → violence; *harden* → rebellion; *judge/injustice* → a possible **justice** family). Left out deliberately pending your call — say which to absorb and I re-run.
2. **Rule-based borderlines** (a handful, low count): bare *"Exalt"* sits in **praise** (default Godward; could be pride if self-exaltation); *"Depart"/"Commit"* landed in **trust** via the gloss-fallback (Commit ≈ entrustment); *"being"* in worship via fallback. These are the expected cost of keyword rules — visible, not hidden, and each record still carries its own evidence.
3. **`family` is a grouping, not a claim about the network.** Per your standing caution, this is a *capacity index* (so "how does the *praise* field behave across the Psalter" is answerable) — it does **not** assert the movements/flows between families. That relational reading stays at the instance level (the edges/pairs), untouched by this rollup.

## To refine
Edit the `RULES` list in the builder and re-run `--live` (idempotent — rewrites all 877). Or re-map individual records directly. Nothing here is baked in.

*Filed 2026-07-11. Read-only over `ib_characteristic` after the family write.*
