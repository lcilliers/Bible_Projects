# verse-reading observations exposed to contaminated `verse_lexical.role`

> Escalation #1810 extraction (BUILD.md #305 / escalation #1806: `role` was base-family-unioned instead of exact-strong until fixed 2026-09-20). Scope: `stage='verse-reading'` only -- confirmed live, `char-reading`/`char-answers` never reference `role` at all; `versereadinggenerate.py` is the only generator that reads it, and does so for EVERY live `verse_lexical` row in a batch's verses, not just the cluster's own member strongs. Current stored `role` values are used as ground truth for what the LLM actually saw: every one of 544667 live `verse_lexical` rows was built in one 2026-09-16 window, before the earliest verse-reading observation (2026-09-17), and only 128 have been touched since -- the pre-fix values are still what every prompt contained.

**4319 of 6161 verse-reading observations (70.1%)** were generated for a verse containing at least one contaminated `role` entry somewhere in its word list. 247 observations have no `ib_node` link at all and could not be checked (excluded, not counted either way).

**This is exposure, not demonstrated impact — three tiers, by actual risk:**

| tier | count | meaning |
|---|---|---|
| relational-question | 1013 | question_code is M0.6.5 or D7.7.1 -- these ask the LLM to relate this word to OTHER words' role/cluster tags BY DESIGN. Contamination here had a real chance of being read and acted on. |
| own-subject-strong | 341 | the OBSERVATION'S OWN subject strong had a contaminated role, on a non-relational question (M0.1.x/M0.5.x -- name/etymology/meaning). These questions' own instructions never ask about cluster/role membership (confirmed by inspecting sample obs_text) -- exposure without a plausible mechanism of influence. |
| context-only | 2965 | a DIFFERENT word in the same verse had a contaminated role, on a non-relational question. Weakest tier: the contaminated tag was present in the payload as background for an unrelated word, on a question that doesn't ask about role at all. |

## By cluster (top 15 by total exposed observations)

| cluster | relational-question | own-subject-strong | context-only | total |
|---|---|---|---|---|
| M83 | 665 | 68 | 1325 | 2058 |
| M49 | 334 | 65 | 779 | 1178 |
| M67 | 14 | 4 | 92 | 110 |
| M15 | 0 | 0 | 37 | 37 |
| M42 | 0 | 4 | 32 | 36 |
| M24 | 0 | 5 | 30 | 35 |
| M18 | 0 | 7 | 27 | 34 |
| M22 | 0 | 8 | 23 | 31 |
| M47 | 0 | 4 | 26 | 30 |
| M23 | 0 | 11 | 19 | 30 |
| M58 | 0 | 21 | 9 | 30 |
| M72 | 0 | 16 | 13 | 29 |
| M16 | 0 | 5 | 23 | 28 |
| M55 | 0 | 2 | 26 | 28 |
| M56 | 0 | 2 | 24 | 26 |

Full list (4319 rows, every field, no truncation): `verse-reading-observations-exposed-to-contaminated-role-20260920.csv` (same folder as this report).

## Recommendation (not a decision made here)

If any re-examination is warranted, the `relational-question` tier (M0.6.5/D7.7.1) is where to look first -- it's the only tier with a stated mechanism by which contamination could have changed what the LLM actually wrote, not just what it was shown.

