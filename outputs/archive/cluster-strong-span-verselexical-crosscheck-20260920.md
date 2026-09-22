# Cluster -> strong -> strong-verse -> span -> strong -> verse-lexical -> cluster round trip

> Escalation #1806 follow-up (researcher instruction, this chat turn, verbatim: 'prepare a report cluster - strong - strong-verse - span -> strong -> verse-lexical -> cluster. use the three clusters already analysed as scope. for every cluster get every strong and every verse then get every strong in each verse-span (ALL the strong) matched to verse-lexical and check that every strong are mapped back to a cluster. report all discrepancies.'). Scope: the 3 clusters confirmed live to have reached the `char-answers` stage (`ib_observation.stage`) -- M49 (Thanksgiving), M67 (Sloth & Diligence), M83 (Seeking & Inquiring) -- the only clusters with any row at that stage; every other live cluster sits at `verse-reading` or earlier. Read-only, three-connection-hop trace per cluster: `cluster_strong` (cluster->strong) -> `strong_verse` (strong->verse) -> `span` (verse-> EVERY strong actually present, not just the cluster's own) -> `verse_lexical` (span->resolved lexical record) -> live `cluster_strong` recompute (strong->cluster, any cluster, not just the scope cluster).

**Headline: 0 of 2528 occurring, live strongs across the 3 clusters' analysed verses are unmapped to any cluster** (`not_mapped_to_any_cluster` = 0 in every cluster). 0 span(s) with no live `verse_lexical` record (0 found). The one real discrepancy found: **1694 `verse_lexical` row(s) whose stored `role` column is stale** relative to a live recompute of `cluster_strong` -- see Finding 1.

## Contents

- [Finding 1 — stale `verse_lexical.role`](#finding-1)
- [Finding 2 — everything else checked clean](#finding-2)
- [Per-cluster detail](#detail)

<a id='finding-1'></a>
## Finding 1 — stale `verse_lexical.role` (real, but not a mapping gap)

`verse_lexical.role` stores a JSON array of `cluster_strong.cluster_code` values captured at Layer-1 build time (`handlers/lexical.py`). `cluster_strong` keeps changing after that (cluster reassignment/dedup work, e.g. the M10->M10b->M58 and old-system-migration retirement history visible in `cluster_strong.rationale`) and nothing re-syncs `role` when it does -- the codebase already documents this exact risk (`handlers/lexical.py` computes cluster tags "at request time, never a stored verse_lexical column (cluster_strong keeps changing)" for its own briefing-pack reads, precisely to avoid trusting this column).

**Every single mismatch found (100%, 0 exceptions) is an EXTRA, now-stale code still sitting in `role` that `cluster_strong` no longer carries for that strong** -- never a live cluster_strong allocation missing from `role`. So this is over-inclusion (a consumer trusting the stored `role` column directly would see a verse tagged for a cluster it no longer belongs to), not under-inclusion -- it does not create the "strong unmapped to any cluster" failure mode this report was scoped to check, but it is a real, measurable divergence between two places the same fact is recorded.

| cluster | verse_lexical rows checked | rows with stale role | % stale | distinct strongs affected | distinct verses affected | top stale-extra codes |
|---|---|---|---|---|---|---|
| M49 | 2726 | 423 | 15.5% | 111 | 134 | T10×173, T2×160, T3×42, T8×26, M08×24, M16×23 |
| M67 | 287 | 5 | 1.7% | 4 | 4 | M72×2, T7×1, T3×1, M61×1 |
| M83 | 10325 | 1266 | 12.3% | 228 | 373 | T2×520, T10×477, T7×95, T8×91, T3×71, M02×69 |

<a id='finding-2'></a>
## Finding 2 — everything else checked clean

| cluster | owned strongs (cluster_strong) | verses (strong_verse) | spans in those verses (ALL strongs) | distinct strong codes in those spans | spans with no live verse_lexical row | span codes not a live `strong` row | occurring strongs unmapped to ANY cluster | cluster's own strongs missing self-tag |
|---|---|---|---|---|---|---|---|---|
| M49 | 5 | 155 | 1808 | 625 | 0 | 0 | 0 | 0 |
| M67 | 9 | 17 | 273 | 172 | 0 | 0 | 0 | 0 |
| M83 | 7 | 496 | 7168 | 1731 | 0 | 0 | 0 | 0 |

All four right-hand columns are 0 for all 3 clusters: every span in every verse these clusters' own strongs occur in has a live `verse_lexical` record; every occurring span code resolves to a live `strong` row; every occurring strong has at least one live `cluster_strong` allocation to SOME cluster; and every one of the cluster's own strongs carries that cluster's own code in `role` wherever it occurs (no self-tag omission).

<a id='detail'></a>
## Per-cluster detail

### M49

Stale-role sample (verse_lexical_id, strong, extra-in-role-not-live, missing-from-role, live cluster codes):

| verse_lexical_id | strong | extra_in_role | missing_from_role | live |
|---|---|---|---|---|
| 1291758 | H3068G | T10 | - | T7 |
| 1291762 | H0639G | T2 | - | M02,T14 |
| 1291763 | H7725I | M11,M81 | - | T3 |
| 1291766 | H5162G | M11 | - | M45 |
| 1199240 | H7200G | T7 | - | T3 |
| 1199247 | H3068G | T10 | - | T7 |
| 1199249 | H1004B | T10 | - | T2 |
| 1199252 | H0639I | M02,T14 | - | T2 |
| 1199253 | H0776H | T10 | - | T13 |
| 1199260 | H3068G | T10 | - | T7 |
| 1199263 | H2896A | M05,T2 | - | M18 |
| 1199265 | H2617A | M07 | - | M50 |
| 1495567 | G2564G | M37 | - | M42 |
| 1250760 | H1419A | T8 | - | T2 |
| 1250764 | H6918G | M13 | - | M61 |

### M67

Stale-role sample (verse_lexical_id, strong, extra-in-role-not-live, missing-from-role, live cluster codes):

| verse_lexical_id | strong | extra_in_role | missing_from_role | live |
|---|---|---|---|---|
| 1476384 | G2962G | M72 | - | T7 |
| 1411703 | G2962H | T7 | - | M72 |
| 1411711 | G1492I | T3 | - | M15 |
| 1512324 | G0040H | M61 | - | M13 |
| 1494694 | G2962G | M72 | - | T7 |

### M83

Stale-role sample (verse_lexical_id, strong, extra-in-role-not-live, missing-from-role, live cluster codes):

| verse_lexical_id | strong | extra_in_role | missing_from_role | live |
|---|---|---|---|---|
| 1246985 | H7451C | M58 | - | M24 |
| 1246986 | H1696G | T3 | - | M42 |
| 1135618 | H0935P | T10 | - | T3 |
| 1135619 | H7218A | M24,M72,T2 | - | T14 |
| 1135627 | H4428G | T2,T7 | - | M72 |
| 1135629 | H7218A | M24,M72,T2 | - | T14 |
| 1135640 | H3068G | T10 | - | T7 |
| 1135646 | H4428G | T2,T7 | - | M72 |
| 1151046 | H4428G | T2,T7 | - | M72 |
| 1151050 | H3092I | T10 | - | T8 |
| 1151053 | H0376G | T2 | - | T8 |
| 1151056 | H3068G | T10 | - | T7 |
| 1151072 | H2896A | M05,T2 | - | M18 |
| 1151075 | H7451B | M24 | - | M58 |
| 1151077 | H3092I | T10 | - | T8 |

