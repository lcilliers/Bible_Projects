# M01-M47 family-grouping — iteration round 1: new-family candidates and real fringe

**2026-09-05.** Reusing `_apply_ib_char_family_grouping_v1_20260711.py`'s exact ordered-regex-rule
technique (49 established families, first-match-wins, errs toward leaving a word unclassified
rather than forcing it) against the full M01-M47 corpus. Working at the **`strong`/`stepGloss`
level** (2,971 distinct M01-M47-tagged strongs), not raw `verse_lexical.surface` — confirmed
earlier the same day that surface text is 65% uncategorised purely from per-verse translation
noise (euphemism, idiom, generic renderings of otherwise well-classified words), while `stepGloss`
gives a stable 54% baseline coverage on the same 49 families, unchanged from their original
Psalms/Proverbs-tuned design.

## Method

Dumped every uncategorised `(strong, stepGloss)` pair, grouped by its M-cluster, and read through
cluster by cluster (all 46 clusters that had any misses) looking for real thematic pockets — not
guessing keywords cold, but reading the actual glosses that washed out together. Every candidate
below is quantified against the live corpus, not asserted.

## Baseline

1,357 of 2,971 strongs (46%) uncategorised under the original 49 families.

## Round 1 — 25 new-family candidates found, quantified

| candidate family | pattern sketch (illustrative, not final) | strongs resolved |
|---|---|--:|
| sickness-weakness-infirmity | ill/sick/weak/illness/disease/blind/crippled/incurable | 46 |
| authority-dominion-rule | authority/dominion/kingdom/rule/govern/reign/lord over/royal | 46 |
| kindness-gentleness-friendship | kind/gentle/friend/hospitable/tender/sympathize/pious | 38 |
| reasoning-judgment-interpretation | reason/discuss/dispute/decide/judge/interpret/advise/ignorant | 38 |
| purity-holiness-sanctification | purify/sanctify/consecrate/sacred/holy/unblemished/sinless | 36 |
| corruption-perversion-immorality | adultery/corrupt/pervert/twist/lewd/unfaithful/apostasy | 31 |
| envy-greed-excess | envy/greed/lust/fornicate/debauchery/self-indulgent/wanton | 28 |
| doubt-discouragement-worry | anxious/discouraged/perplexed/doubt/grumble/hide/worry | 27 |
| judgment-condemnation-justice | judge/judgment/condemn/justify/avenge/vengeance/accountable | 26 |
| dishonor-mutilation-disgrace | dishonor/mute/mutilate/filth/revile/muzzle/indecency/abase | 25 |
| outcry-roaring-shouting | outcry/roar/shout/moan/mutter/voice | 23 |
| covenant-fellowship-unity | covenant/brotherhood/fellowship/share/unity/companion/agree | 23 |
| slavery-bondage-burden | slave/slavery/enslave/burden | 22 |
| gift-favor-goodwill | gift/favor/goodwill/goodness | 22 |
| stumbling-trial-temptation | stumble/trial/sift/entice/persuade | 18 |
| prophecy-vision-interpretation | prophesy/prophecy/interpret/insight/sign/image | 16 |
| astonishment-wonder-marvel | astonish/marvel/wonder/amazed/triumph | 15 |
| remembrance-reminder-report | remembrance/remind/news/tidings/report | 15 |
| renewal-transformation-change | new/change/transform/regeneration/conform | 15 |
| self-control-sobriety-zeal | self-control/sober/fervent/eager/careful | 14 |
| disobedience-hardness-lawlessness | disobedience/harden/hardness/lawless/insubordinate | 13 |
| patience-endurance-perseverance | patience/persevere/endure/put up with/remain | 12 |
| salvation-ransom-propitiation | salvation/savior/ransom/propitiate/redeem | 11 |
| encouragement-edification | encourage/build up/building | 8 |
| firstborn-foreknowledge | firstborn/foreknowledge/predetermine | 8 |
| **total** | | **576** |

**Projected coverage after round 1: 2,190 / 2,971 = 73%** (up from 54%). 781 strongs (26%) remain
uncategorised.

## A recurring MECHANICAL gap, not a missing family — worth fixing separately

Reading the misses surfaced the same failure shape repeatedly: a negated/prefixed form of an
**already-covered** root gets excluded by the ruleset's own correct word-boundary discipline.
`\bobedien` cannot match inside `disobedience` (no boundary before "obedien" — the "s" blocks it),
`\bbeliev` cannot match inside `disbelieve`/`unbelief`, `\bcurse\b`-style tokens don't match inside
`accursed`. This is NOT a bug — the boundary check is exactly what stops "sin" matching inside
"single" — but it means every `dis-`/`un-`/`in-` NEGATION of a word this ruleset already knows
(disobedience → torah-obedience-word, unbelief → faith-faithfulness-truth) currently reads as
unrelated rather than as that family's opposite pole. Two live examples caught directly:
`disobedience-hardness-lawlessness` above absorbs the M30 cluster largely BECAUSE it's phrased as
its own new family (side-stepping the boundary problem) rather than folding into
`torah-obedience-word` — that's a real design choice (is disobedience the *opposite* of the
obedience family, or its own family?), not something to decide unilaterally here.

**Also found: a US/UK spelling gap.** `shame-confusion`'s pattern has `dishonou` (British spelling)
only — every `stepGloss` in this DB spells it `dishonor` (American), so the existing pattern
silently misses all of them. Purely mechanical, one character, worth fixing regardless of any
other decision (folded provisionally into the new `dishonor-mutilation-disgrace` candidate above,
but the simpler fix is just adding `dishono` — 4 fewer letters — to the existing family's own
pattern).

## What's left after round 1 (781 strongs) — real fringe vs. round-2 candidates

Not yet fully triaged (round 2 would need the same read-through discipline), but skimming the
residue shows two genuinely different shapes:

- **Genuine outer fringe** — proper names whose `stepGloss` IS the name (`Meribah`, `Jashar`,
  `Rahab`), a handful of very narrow ritual-specific concepts with little "movement" content
  (`circumcision`/`uncircumcision`, 9 strongs, no clear inner-being family), and bare auxiliary-
  shaped glosses too generic to carry thematic content alone (`be little`, `be permitted`, `be
  away`, `to collect`, `beginning`, `cause`). These will not resolve to any family, however far the
  ruleset is extended, and shouldn't be forced to.
- **Real round-2 candidates already visible**, not yet quantified: `glory-honor-splendor`
  (distinct from the existing `praise-extol-sing`, which is about the ACT of praising, not the
  STATE of being glorious/honored) — M08's `majesty`/`height`/`haughtiness` cluster overlaps this
  too; a `fasting-piety-intercession` pocket (M21); an `abundance-riches-self-sufficiency` pocket
  that mostly should just extend the EXISTING `wealth-poverty-riches` pattern (it currently
  requires the exact phrase `abundance of`, missing bare `abundance`, and `rich\b` misses `richly`
  for the same word-boundary reason as above).

## Round 2 (2026-09-05, same session) — target: ~100 families, ~100 residual

Researcher's target after round 1: *"approx 100 miscellaneous... about 100 groups in total also
sounds manageable."* Read through the round-1 residual (779 strongs) cluster by cluster the same
way. Finding: **most of what's left is not a missing family at all — it's a near-miss suffix/
spelling/word-form gap against an already-correct existing family** (the same word-boundary
discipline noted in round 1, generalised): `haughtiness` doesn't match `haughty`, `humility`
doesn't match `humbl` (irregular English pair), `indignant` doesn't match `indignat`, `truth`
doesn't match `true` (different words), `provocation` doesn't match `provoke` (c/k spelling).

**Extended 10 existing families** with this real, evidence-based near-miss vocabulary (fear,
anger, grief, joy, faith, desire, knowing, malice, pride, deceit, humility, strength, violence,
faint-despair) rather than spawning mirror families for each — keeps the family count controlled,
and is the linguistically correct call in every case checked (these are the *same* concept, not an
adjacent one). Added **6 more genuinely new families**: `destruction-ruin-devastation`,
`truth-sincerity-certainty`, `madness-recklessness-insanity`, `fasting-piety-intercession`,
`glory-honor-splendor`, `release-relinquish-reconcile`.

**Result, measured against the full corpus: 78 families (of 80 defined — 2 defined but not yet
hit by anything live), 87% coverage (2,600 / 2,971), 371 uncategorised (12%).** Close to the
~100/~100 target but not exactly there — coverage plateaued faster than the family count grew,
because round 2 spent most of its gains fixing existing-family near-misses rather than adding new
territory. Two of my own ruleset bugs caught and fixed in this same pass (a typo — `agoni` doesn't
match `agony` — and a missing `frighten` alongside `terrify`), for what it's worth as a reminder
that this whole exercise is self-auditing, not just applying a fixed tool.

**Checkpoint, not a finish.** Continuing to grind toward the exact 100/100 numbers by further
manual line-reading has real diminishing returns from here, and more importantly, the extend-
existing-vs-new-family calls above (10 of them) and the 31 new-family names (25 round 1 + 6 round
2) are genuine taxonomy judgement calls, not something to keep finalising solo. Stopping here to
check in before a further round.

## Decision needed before applying anything

Two live, un-mixed questions, both genuine judgement calls: (1) which of the 25 candidates above
are approved as real new families (name, scope, exact pattern) versus folded into an existing
family's pattern instead (the disobedience/dishonor cases above are the sharpest examples of this
fork); (2) whether to keep iterating rounds against the residual 781 before applying anything, or
apply round 1 now and iterate the remainder as a second pass. Nothing has been written to any
table — this is read-only analysis throughout, same as `lib/clusterassign.py`'s own convention.
