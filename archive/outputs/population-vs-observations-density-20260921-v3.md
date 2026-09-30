# Population anchors vs. observation counts — M49/M67/M83

> Escalation #1806 deliverable (researcher instruction, this chat, verbatim: 'create some stats for the three clusters already completed: number of verses in total, number of unique spans, number of spans per strong; number of spans per strong per cluster; number of verses per sub group, number strongs per subgroup... then use this stats to look at the number of observations in each of these groupings to get a view if the number of observations done is reasonable in relation to the population to be evaluated.'). Scope: M49, M67, M83 -- the only 3 clusters that have reached `ib_observation.stage='char-answers'`.

**Definition used (a judgment call, stated plainly, not hidden):** 'span' = a live `span` whose `strong_variant` contains one of the cluster's own OWNED strongs (`cluster_strong`) -- the actual per-occurrence unit the word-level battery operates on. This is narrower than #1806's earlier round-trip check, which counted EVERY word in the verse regardless of cluster ownership -- a different question (mapping completeness, not population sizing).

Three CSVs, one per grouping level, full disclosure, no truncation: `cluster-population-vs-observations-20260921-v3.csv`, `strong-population-vs-observations-20260921-v3.csv`, `subgroup-population-vs-observations-20260921-v3.csv` (same folder as this report).

## Headline finding — population coverage is uneven within at least one cluster

**M83 / A_general_seeking** (Generic active seeking/searching) is still `ready_for_reading` while its sibling subgroups in M83 are `answer_complete` — confirmed directly via `cluster_subgroup.status`, not inferred from the zero observation counts alone. This subgroup alone accounts for **328 of M83's 496 total verses (66.13%)** and 341 spans (strongs G2212, H1245) -- meaning M83's current char-reading/char-answers observation counts reflect analysis of only its OTHER, smaller subgroups. Checked the other two clusters for the same pattern: M49, M67 have every subgroup at the same status as its siblings -- this is isolated to M83, not a systemic pattern across all three.

## 1. Cluster level

| cluster_code | verse_count | span_count | strong_count | obs_verse_reading | obs_char_subgroup | obs_char_reading | obs_char_answers | total_obs | obs_per_verse | obs_per_span | obs_per_strong |
|---|---|---|---|---|---|---|---|---|---|---|---|
| M49 | 193 | 201 | 5 | 1579 | 5 | 37 | 273 | 1894 | 9.81 | 9.42 | 378.8 |
| M67 | 35 | 37 | 9 | 302 | 7 | 26 | 259 | 594 | 16.97 | 16.05 | 66.0 |
| M83 | 496 | 539 | 7 | 2890 | 7 | 55 | 216 | 3168 | 6.39 | 5.88 | 452.57 |

**Reading this:** `obs_per_verse`/`obs_per_span`/`obs_per_strong` are TOTAL observations (all 4 stages combined) divided by that population count -- a rough density figure, not a completeness measure (verse-reading answers ~14-16 questions per strong occurrence by design, so an `obs_per_span` well above 1 is expected and not itself evidence of thoroughness beyond what the battery structurally produces).

## 2. Strong level (spans per strong, per cluster)

| cluster_code | strong | span_count | verse_count | obs_verse_reading | obs_char_reading | obs_char_answers | total_obs | obs_per_span |
|---|---|---|---|---|---|---|---|---|
| M49 | G2168 | 39 | 38 | 332 | 9 | 11 | 353 | 9.05 |
| M49 | G2169 | 15 | 15 | 154 | 5 | 57 | 217 | 14.47 |
| M49 | G2170 | 1 | 1 | 45 | 4 | 52 | 102 | 102.0 |
| M49 | H3034 | 114 | 111 | 677 | 14 | 8 | 700 | 6.14 |
| M49 | H8426 | 32 | 30 | 305 | 5 | 52 | 363 | 11.34 |
| M67 | G0691 | 1 | 1 | 16 | 3 | 3 | 23 | 23.0 |
| M67 | G0692 | 8 | 7 | 52 | 2 | 8 | 63 | 7.88 |
| M67 | G0812 | 1 | 1 | 16 | 4 | 2 | 22 | 22.0 |
| M67 | G3636 | 3 | 3 | 33 | 2 | 4 | 40 | 13.33 |
| M67 | G4709 | 3 | 3 | 48 | 4 | 2 | 55 | 18.33 |
| M67 | G4710 | 12 | 12 | 73 | 4 | 2 | 80 | 6.67 |
| M67 | H0149 | 1 | 1 | 2 | 2 | 0 | 4 | 4.0 |
| M67 | H0629 | 7 | 7 | 43 | 3 | 0 | 47 | 6.71 |
| M67 | H8220 | 1 | 1 | 15 | 2 | 3 | 21 | 21.0 |
| M83 | G1567 | 7 | 7 | 71 | 3 | 3 | 78 | 11.14 |
| M83 | G1934 | 14 | 13 | 126 | 2 | 1 | 130 | 9.29 |
| M83 | G2212 | 116 | 113 | 595 | 0 | 0 | 596 | 5.14 |
| M83 | G2614 | 1 | 1 | 16 | 3 | 52 | 72 | 72.0 |
| M83 | H1245 | 225 | 215 | 985 | 0 | 0 | 986 | 4.38 |
| M83 | H1875 | 164 | 152 | 844 | 43 | 56 | 944 | 5.76 |
| M83 | H7836 | 12 | 12 | 172 | 4 | 2 | 179 | 14.92 |

## 3. Subgroup level

| cluster_code | subgroup_code | label | status | strong_count | verse_count | span_count | obs_char_reading | obs_char_answers | total_obs | obs_per_verse | obs_per_strong |
|---|---|---|---|---|---|---|---|---|---|---|---|
| M49 | A_thanksgiving_act | The verbal act of giving thanks | answer_complete | 1 | 38 | 39 | 9 | 55 | 64 | 1.68 | 64.0 |
| M49 | B_thankfulness_state | The noun-named state and expression of gratitude | answer_complete | 1 | 15 | 15 | 5 | 57 | 62 | 4.13 | 62.0 |
| M49 | C_thankful_disposition | The settled character-trait of being thankful | answer_complete | 1 | 1 | 1 | 4 | 52 | 56 | 56.0 | 56.0 |
| M49 | D_yadah_praise_confess | Outward-cast acknowledgment: praise and confession before God | answer_complete | 1 | 111 | 114 | 14 | 57 | 71 | 0.64 | 71.0 |
| M49 | E_todah_offering_noun | The instituted noun-form of thanksgiving: hymn, choir, and offering | answer_complete | 1 | 30 | 32 | 5 | 52 | 57 | 1.9 | 57.0 |
| M67 | M67_A_dispositional_idleness | Idleness as inert state or condition | answer_complete | 3 | 9 | 10 | 7 | 98 | 105 | 11.67 | 35.0 |
| M67 | M67_B_dereliction_of_duty | Failure to fulfill an entrusted obligation | answer_complete | 2 | 4 | 4 | 6 | 55 | 61 | 15.25 | 30.5 |
| M67 | M67_C_earnest_diligence | Zealous, energetic application to a task or relationship | answer_complete | 2 | 15 | 15 | 8 | 54 | 62 | 4.13 | 31.0 |
| M67 | M67_D_administrative_thoroughness | Exact, complete execution of an official command | answer_complete | 2 | 8 | 8 | 5 | 52 | 57 | 7.12 | 28.5 |
| M83 | A_general_seeking | Generic active seeking/searching | ready_for_reading | 2 | 328 | 341 | 0 | 0 | 0 | 0.0 | 0.0 |
| M83 | B_intensified_seeking | Intensive/exhaustive seeking and demanding | answer_complete | 3 | 32 | 33 | 9 | 108 | 117 | 3.66 | 39.0 |
| M83 | C_hostile_pursuit | Seeking with lethal or hostile intent | answer_complete | 1 | 1 | 1 | 3 | 52 | 55 | 55.0 | 55.0 |
| M83 | D_consultative_inquiry | Formal consultation and diligent inquiry | answer_complete | 1 | 152 | 164 | 43 | 56 | 99 | 0.65 | 99.0 |

**Note on subgroup-level observation counts:** only `char-reading` and `char-answers` carry `cluster_subgroup_id` on their `ib_observation` rows -- `verse-reading` (the largest stage by volume) and `char-subgroup` (the allocation decision itself) do not, so their observations cannot be attributed to a subgroup and are excluded from this table's counts (they ARE included at the strong/cluster level above). Not silently dropped: stated here.

