# #2286 prototype step 11: the scope under the surface and subgroup model (ruled)

Date: 2026-10-25. Escalation #2286 v31. **v2** carries the researcher's rulings on S1 to S5. The
facts and the path-by-path analysis of v1 are in
`outputs/escalation/archive/2286-scope-under-surface-model-v1-20261025.md`. Nothing is built.

## 0. The rulings (v31, verbatim)

> S1 and S2 is linked. Until all the verses have been analysed, it must be assumed that the scope
> subgroup is the home. I can envisage that a second reading of the analysis and claims will be made
> where all the M-codes in a verse are synergised together, but that can only be considered and done
> later. S3 - yes, if you mean by occurance, every verse. however, when it comes to claims, duplicity
> is handled through ib_observations that will group all the observations that is the same for the
> underlying verses as a single claim with a anchor verse as citation but trackleable to all the other
> related verses. S4 NEVER through word_strong. ALWAYS through surface. there should be a config for
> this already in place. S5 when this happens it is material that there are multiple sub groups and
> it should be included in the reading.

## 1. What is decided

| # | decision |
|---|---|
| S1 + S2 | **The scope's subgroup is the home** until all the verses have been analysed. The other subgroups in a verse are read in it, and their other verses do not join the scope. |
| later | **A second reading** that synergises all the M-codes in a verse together may be made later. It is not part of the first pass. |
| S3 | **The record of reading is kept per occurrence** (see section 2 for what an occurrence is). |
| claims | **Duplication is handled in `ib_observation`.** Observations that say the same thing over several verses are one observation (RW-03: one observation, many nodes), and they give one claim. That claim cites an anchor verse and can be traced to all the related verses. |
| S4 | **A word enters a scope through the surface, never through `word_strong`.** |
| S5 | **When a Strong's code lands in several subgroups, that is material,** and every one of them is included in the reading. |

## 2. One point to confirm: what an occurrence is

You wrote "if you mean by occurance, every verse". By occurrence I mean **each word in each verse**:
one row of `verse_lexical`, which is a code, its surface and its position in that verse. A verse that
brings three subgroups holds three or more occurrences.

The difference matters for R3. If reading is recorded per verse, then reading Psa 51:10 for one
subgroup (say *heart*) would mark it read for the others (clean, renew, right, spirit) too. That is
the same mistake #2262 describes ("gap analysis counts any observation as read"). Recorded per
occurrence, each subgroup's reading of the verse is kept on its own. Every one of the 16,901 nodes in
`ib_node` already holds its code and surface, so it can be placed on its occurrence.

| per occurrence (each word in each verse), as defined above? | your answer |
|---|---|
| | **Confirmed** (#2286 v34): "an occurrence is each word in each verse (one verse_lexical row); reading is recorded per occurrence." |

## 3. S4: no config found

You expected a config for "always through surface" to be in place. I searched `cfg_behaviour_rule`
and `cfg_setting` for "surface" and every cfg table's text for "word_strong", and found none that
states it. The nearest is rule 110 (surface-is-the-sensitivity-lens): "For every term in a verse read,
verse_lexical.surface is analysed per Strong's first". That is about reading a term, not about how a
word enters a scope.

The scope resolver as built does the opposite: `iba/app/lib/versescope.py` `Resolver.word` (lines 174
to 180) goes from `word_registry` through `word_strong` to codes. Under
governance.rules_must_be_config_driven, a rule with no config row is a gap. It is recorded on #2287
(v2) with the resolver's other finding, and the rule goes into config with the #2286 design.

## 4. What the decisions mean for the queries (from v1, now ruled)

| path | under the model |
|---|---|
| a) cluster, subgroup, verses | through `surface_subgroup`, occurrence-exact; the subgroup is the home (S1) |
| a) Strong's entry | lands in every subgroup its surfaces belong to, and all are read (S5) |
| b) word | **through the surface only** (S4): the word is matched to `verse_lexical.surface`, then to its subgroups |
| c) verse | the verse's occurrences and their subgroups are shown and read; no expansion to other verses (S2) |
| d) chapter or block, e) claim | to verses, then as c; a claim's observation sources as f |
| f) observation | nodes to occurrences to subgroups directly |
| output JSON | per verse, its occurrences (code, surface, subgroup, cluster, two-sense flag, home or not); T-coded occurrences as context |

## 5. Decided so far on #2286, for the design

The design will gather these together: E1, E2, E3a, C1 to C5 (step 9), T-1, T-a to T-c, T-2 (step
10), rule 70 as amended (#2289), and S1 to S5 (this step). E4 is settled (#2286 v33): the
T-b principle applies to M-coded qualifiers too. The point in section 2 is confirmed (#2286 v34). Nothing on the work unit is still open.
