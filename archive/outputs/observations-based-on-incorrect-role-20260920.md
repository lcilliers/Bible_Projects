# Observations based on incorrect `role` — v2 (corrected)

> Escalation #1810, v2 of this extraction. Corrects two things the researcher flagged in v1: (1) an 'own-subject-strong' tier was a false distinction -- verse-reading's word-level battery (M0.1.x/M0.5.x) answers what the verse/word SAYS, not what it says about the cluster, so a word's own role being wrong has no mechanism to matter there; dropped. (2) role's effect is not confined to verse-reading -- confirmed live this round that `charreadinggenerate.py`, `subgroupgenerate.py`, and `charanswergenerate.py` each independently pull `ib_observation WHERE strong=? AND stage='verse-reading'` (every question, unfiltered) as direct input context. A contaminated M0.6.5/D7.7.1 verse-reading answer (built FROM the wrong role tag) is fed verbatim into every char-subgroup/char-reading/char-answers call for that same strong.

**Two tiers, chained, not independent:**

| tier | count | meaning |
|---|---|---|
| A — root (verse-reading, M0.6.5/D7.7.1) | 1013 | the actual mechanism: question asks the LLM to relate this word to OTHER words via their role/cluster tags. Verse contained a contaminated role entry, so the answer may itself be substantively wrong (e.g. 'relates to an Operation-tagged word' when that word wasn't really Operation-tagged). |
| B — downstream (char-subgroup/char-reading/char-answers) | 380 | every observation, ANY question, for a strong that has a Tier-A root observation -- these stages received that root's (possibly wrong) obs_text verbatim as their own prompt context, confirmed by direct code inspection, not inferred. |

### Tier B by stage

| stage | count |
|---|---|
| char-subgroup | 16 |
| char-reading | 103 |
| char-answers | 261 |

**17 distinct strongs** carry a Tier-A root observation and are the seed of every Tier-B row. **1393 observations total** (1013 root + 380 downstream).

## By cluster

| cluster | tier A (root) | tier B (downstream) | total |
|---|---|---|---|
| M83 | 665 | 120 | 785 |
| M49 | 334 | 222 | 556 |
| M67 | 14 | 38 | 52 |

Full list (1393 rows): `observations-based-on-incorrect-role-20260920.csv` (same folder).

## Explicitly dropped from this extraction (per researcher correction)

v1's 'own-subject-strong' (341) and 'context-only' (2,965) tiers are not carried forward here -- neither M0.1.x nor M0.5.x asks about cluster/role membership, so a word's own or a neighbouring word's role being wrong has no stated path into those answers. Not silently dropped: recorded here as checked and excluded, not forgotten.

