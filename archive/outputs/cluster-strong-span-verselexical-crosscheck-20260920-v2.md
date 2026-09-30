# Cluster -> strong -> strong-verse -> span -> strong -> verse-lexical -> cluster round trip

> Escalation #1806 follow-up (researcher instruction, this chat turn, verbatim: 'prepare a report cluster - strong - strong-verse - span -> strong -> verse-lexical -> cluster. use the three clusters already analysed as scope. for every cluster get every strong and every verse then get every strong in each verse-span (ALL the strong) matched to verse-lexical and check that every strong are mapped back to a cluster. report all discrepancies.'). Scope: the 3 clusters confirmed live to have reached the `char-answers` stage (`ib_observation.stage`) -- M49 (Thanksgiving), M67 (Sloth & Diligence), M83 (Seeking & Inquiring) -- the only clusters with any row at that stage; every other live cluster sits at `verse-reading` or earlier.

> **v2 correction (same day):** v1's Finding 1 wrongly explained the role/cluster_strong mismatch as a stale snapshot from cluster reassignment history. The researcher pointed at a concrete counter-example (verse_id 7478, strong H7725O) that disproved it. Finding 1 below has been rewritten with the verified mechanism -- base-family union, confirmed against all 1,694 cases in this report's scope with zero exceptions.

**Headline: 0 of 2528 occurring, live strongs across the 3 clusters' analysed verses are unmapped to any cluster** (`not_mapped_to_any_cluster` = 0 in every cluster). 0 span(s) with no live `verse_lexical` record (0 found). The one real discrepancy found: **1694 `verse_lexical` row(s) whose stored `role` differs from the exact occurring strong's own live `cluster_strong` allocation** -- see Finding 1 for the verified mechanism.

## Contents

- [Finding 1 — `verse_lexical.role` is base-family-unioned, not exact-strong](#finding-1)
- [Finding 2 — everything else checked clean](#finding-2)
- [Per-cluster detail](#detail)

<a id='finding-1'></a>
## Finding 1 — `verse_lexical.role` is base-family-unioned, not exact-strong

`role` (`iba/app/lib/lexical.py:load_role_codes`/`_role_for`, redesigned 2026-09-16 per escalation #1706 Phase B item 3 / #1607 D1-D4) is built by stripping the trailing suffix letter off a strong code (`_base()`) and **unioning live `cluster_strong.cluster_code` across every sub-lettered sibling that shares the same base number** -- not the exact occurring strong's own allocation alone.

**Worked example (the researcher's own case):** verse 1Kgs 8:35 (verse_id 7478), span 637365 surface "turn", `strong_variant = "H7725O H9028"`. Live `cluster_strong` for the EXACT code H7725O is only **M11**. But `role` for H7725O = `["M11","M81","T3"]`. Why: the H7725 base family also has H7725N (a separately-assigned strong) carrying **M81**, and six other separately-assigned siblings (H7725G/H/I/J/K/L/M) carrying **T3**. `role` for H7725O picks up all of it, even though none of those clusters were ever assigned to H7725O itself.

**Verified computationally against every case in this report's scope, not just the one example:** recomputing each mismatched row's role as "union of live `cluster_strong` codes across the whole base family" matches the stored value exactly for 1694 of 1694 cases (100%, 0 exceptions).

**Project-wide** (not just the 3 clusters in this report's scope): **69563 of 544667 live `verse_lexical` rows (12.8%)** have a `role` that differs from their exact strong's own live `cluster_strong` allocation via this same mechanism.

**Open design question (not resolved here):** `cluster_strong` treats sub-lettered codes as independently assigned -- H7725G/H/I/J/K/L/M, H7725N, and H7725O all carry different, separately-made cluster judgements. Unioning them back together in `role` means a verse can be tagged for a cluster that has nothing to do with the word actually occurring there -- only an unrelated sibling/homonym sharing the same root. Whether base-family union is `role`'s intended behaviour (e.g. a root-level coverage signal) or whether it should reflect only the exact occurring strong (which would mean rebuilding the affected live rows) is a researcher decision -- tracked on escalation #1806.

| cluster | verse_lexical rows checked | rows where role != exact-strong allocation | % of rows | distinct strongs affected | distinct verses affected | top codes only explained by a sibling |
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

All four right-hand columns are 0 for all 3 clusters: every span in every verse these clusters' own strongs occur in has a live `verse_lexical` record; every occurring span code resolves to a live `strong` row; every occurring strong has at least one live `cluster_strong` allocation to SOME cluster (exact-code match); and every one of the cluster's own strongs carries that cluster's own code in `role` wherever it occurs (no self-tag omission).

<a id='detail'></a>
## Per-cluster detail

### M49

Sample (verse_lexical_id, strong, extra-in-role-not-live-for-exact-strong, missing-from-role, live cluster codes for the exact strong):

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

Sample (verse_lexical_id, strong, extra-in-role-not-live-for-exact-strong, missing-from-role, live cluster codes for the exact strong):

| verse_lexical_id | strong | extra_in_role | missing_from_role | live |
|---|---|---|---|---|
| 1476384 | G2962G | M72 | - | T7 |
| 1411703 | G2962H | T7 | - | M72 |
| 1411711 | G1492I | T3 | - | M15 |
| 1512324 | G0040H | M61 | - | M13 |
| 1494694 | G2962G | M72 | - | T7 |

### M83

Sample (verse_lexical_id, strong, extra-in-role-not-live-for-exact-strong, missing-from-role, live cluster codes for the exact strong):

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

