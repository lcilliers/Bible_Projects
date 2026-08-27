# Characteristic coverage audit — emerging vocabulary vs the registry (2026-07-03)

> Prompted by the researcher: *"compare the characteristic list… against your emerging lists — it almost seems as if some words I would have expected are not arising."* Confirmed. This audit harvests the **raw** characteristic vocabulary from the lexical and checks it against the 29‑item `ib_characteristic` registry. Visual: Artifact `char-coverage-audit` (published 2026-07-03).

## Method (counts objective; clustering interpretive)
Harvested every active `ve_lexical` span with `role = characteristic` across Psalms (book 19) + Proverbs (book 20), took its `sense` gloss, summed by word: **1,142 distinct characteristic-words, 5,144 occurrences.** Reusable: the query in `scripts/` (inline). The counts are data; the clustering and the arena/characteristic call are interpretive.

## Finding — the registry (a clustering) has dropped or subsumed real vocabulary
The registry is organised around **movements/operations**; several discrete **characteristics/emotions/faculties** that the evidence raises heavily are not first‑class.

### MISSING — surfaced strongly, no registry home (6)
| candidate | representative words (freq) | note |
|---|---|---|
| **Praise / thanksgiving** | praise 116 · give-thanks 31 · bless 31 · sing-praises 16 · sing 13 | **the single largest omission** — the 4th most frequent characteristic-word; the Psalter's terminus (150:6). No home. |
| **Compassion / mercy / grace (human)** | steadfast-love 54 · gracious 26 · favor 19 · mercy 16 · merciful 11 | most *steadfast love* is God's (arena), but human mercy/tenderness is real and unhoused |
| **Faithfulness / fidelity** | faithfulness 41 · covenant 18 · faithful 16 · truth 10 | loyalty / emet / keeping-faith; only obliquely via integrity + memory |
| **Hate / hatred** | hate 40 · hates 12 · hatred 9 | only love's foil; hating-evil vs the wicked's hate = two colours |
| **Shame / disgrace** | put-to-shame 28 · shame 18 · disgrace 9 | "let me not be put to shame" — a core Psalter dread; honour/shame axis; no home |
| **Deceit / falsehood** | false 15 · deceit 13 · deceitful 10 · lying 10 | folded inside integrity-legibility; deserves its own colour-map |

### FOLDED / PARTIAL — present but subsumed under a movement (8)
| candidate | representative words (freq) | subsumed under |
|---|---|---|
| **Wisdom / understanding** (the faculty) | wise 44 · knowledge 43 · understanding 41 · sense 15 · prudent 13 | wisdom-formation (but the *faculty itself* is under-represented) |
| **Life / vitality** | life 80 · live 14 · give-me-life 9 | restoration ("revive me"); much is arena |
| **Strength / courage** | strength 43 · strong 16 · power 16 · might/mighty 20 | fearlessness (mostly God's; human courage thin) |
| **Sin / guilt** | sin 20 · iniquity 20 · abomination 20 · transgression 10 | forgiveness-confession (the *condition*, not just its pardon) |
| **Folly** | folly 18 · fool 13 · sluggard 13 | teachability/wisdom (foil) |
| **Counsel / planning** | plans 15 · counsel 13 | entrustment/the-will |
| **Anger / wrath** | wrath 15 · angry 8 · strife 9 | self-mastery (governing it, not the operation) |
| **Meditation** | meditate 13 | the-heart (flagged thin) |

### FIRST-CLASS — the registry carries these well (12)
the-heart (heart 160/soul 93/flesh 17) · joy-gladness (glad 45/rejoice 44/joy 26) · fear-of-the-lord (fear 64…) · trust-refuge (trust 38/refuge 22…) · love-aheb (love 41/loves 25) · desire-appetite (delight 26/desire 18) · seeking (seek 40) · waiting-hope (hope 30/wait 14) · memory (remember 31) · rest-stillness (peace 25) · humility (humble 11) · self-mastery (keep 41/rules 23/silent 9).

### ARENA — high-frequency, correctly NOT characteristics (3)
the moral poles (wicked 152 · righteous 122 · upright 39 · holy 36) · God's attributes/acts (glory 47 · justice 29 · good 56 · judge 17) · circumstance (trouble 26 · wealth 16 · riches 14). Shown so nothing high-frequency is unaccounted for.

## Recommended registry additions (10)
**Praise/thanksgiving · Faithfulness/fidelity · Shame/disgrace · Hate/hatred · Compassion/mercy(human) · Deceit/falsehood · Wisdom/understanding(faculty) · Sin/guilt · Anger/wrath · Zeal** (thin but real — Ps 69:9). Each would get a discovery doc in the same mode (colour-range, junctions, thin evidence, open questions).

## Why this happened (a methodological note)
The registry was seeded from my *synthesis rosters* — themselves a compression. Compressing twice (readings → synthesis → registry) let discrete affect-words (shame, gratitude, hate, deceit) dissolve into broader movements. **Discovery mode's correction:** grow the registry to meet the *raw vocabulary*, not the reverse. The harvest above should be the seed, not the summaries.

## Recommendation
Before building more discovery docs: **expand the registry with the 10 additions** (status `emerging`, seeded from the raw vocabulary), then continue — so the remaining discovery docs are drawn against the *fuller* map. Awaiting researcher go-ahead.
