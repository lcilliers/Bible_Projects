# Silent (no-evidence) answers — by cluster and characteristic

- **File:** wa-silent-answers-by-cluster-char-v1-20260621.md · **Date:** 2026-06-21 · **Author:** Claude Code · Read-only diagnostic.
- **Question:** how many tier-catalogue questions are answered "Silent" (evidence does not speak) per characteristic.
- **Source:** captured per-characteristic tier-answer bodies in prose_section (type cf_char_synth, layer tier_findings).

## ⚠ Important: the "Silent" marker is NOT standardised across clusters

Each cluster marks no-evidence answers differently, so a single grep would mislead. A unified detector (Silent · SILENT · "not evidenced" · "does not speak" · prose negatives such as "No mind-location"/"Negative") was applied, counting **distinct catalogue question-IDs** that fall in a no-evidence answer block.

| Cluster | Convention used | Captured? |
|---|---|---|
| M03 | prose negatives ("No mind-location", "Negative —") | yes (per-char) |
| M04 | "not evidenced" | yes (per-char) |
| M05 | "Silent" (+ coverage summary) | yes (per-char) |
| M06 | "SILENT" (+ answer-coverage summary) | yes (per-char) |
| M01 | only *by-tier merged* findings (NEW/OLD), **no per-characteristic split** | not in this format |
| M02 | per-char `cN-...-tieranalysis` files **on disk**, not captured to DB | not in DB |

**Comparability caveat:** clusters tag question-IDs at different granularity (M04/M05 reference all 126; M03/M06 group some), so the denominator of explicitly-tagged questions differs. The silent **count** is a good within-cluster ranking and an approximate cross-cluster guide — not an exact like-for-like. M03 in particular under-tags IDs (prose answers) so its true silence is likely higher than shown.

## Silent answers per characteristic

| Cluster | Characteristic | Silent answers | (silent / tagged-Qs) |
|---|---|---:|---|
| M03 | A — Inner pain / sorrow (felt interior state) | **10** | 10/51 |
| M03 | B — Distress / constriction (the straits) | **6** | 6/47 |
| M03 | C — Mourning / lament (bereavement observance) | **6** | 6/47 |
| M03 | D — Weeping / tears | **7** | 7/45 |
| M03 | E — Sighing / groaning | **6** | 6/44 |
| M03 | F — Bitterness of soul | **7** | 7/49 |
| M03 | G — Torment / acute affliction | **8** | 8/46 |
| M03 | H — Travail / labour-pangs (metaphor) | **4** | 4/39 |
| M03 | I — Debilitating grief (faint / weak / waste) | **8** | 8/44 |
| M03 | J — Voiced complaint / grievance | **11** | 11/45 |
| M04 | A — Rejoicing and gladness | **18** | 18/126 |
| M04 | B — Delight | **18** | 18/126 |
| M04 | C — Pleasantness | **19** | 19/126 |
| M04 | D — Wonder, marvel and amazement | **18** | 18/126 |
| M04 | E — Thankfulness and gratitude | **18** | 18/126 |
| M04 | F — Cheer, good courage and morale | **18** | 18/126 |
| M04 | G — Soothing / pleasing-aroma | **20** | 20/126 |
| M05 | A — Love / affectionate attachment | **14** | 14/126 |
| M05 | B — Compassion | **13** | 13/126 |
| M05 | C — Kindness / steadfast-love (chesed) | **14** | 14/126 |
| M05 | D — Comfort | **15** | 15/126 |
| M05 | E — Gentleness | **26** | 26/126 |
| M05 | F — Friendship | **20** | 20/126 |
| M06 | A — Aversive affect — felt hatred and settled rejection | **28** | 28/95 |
| M06 | B — Appraisive contempt — disdain | **23** | 23/92 |
| M06 | C — Loathing — visceral repugnance and detestation | **21** | 21/84 |
| M06 | D — Reproach, taunt and derision | **11** | 11/87 |
| M06 | E — Adversarial enmity — settled relational opposition | **20** | 20/71 |
| M06 | F — Cruelty and ruthlessness | **25** | 25/84 |

## Cluster totals

| Cluster | Characteristics | Silent answers (sum) | Tagged questions (sum) |
|---|---:|---:|---:|
| M03 | 10 | 73 | 457 |
| M04 | 7 | 129 | 882 |
| M05 | 6 | 102 | 756 |
| M06 | 6 | 128 | 513 |

## Notes
- **M05/M06** carry an explicit author coverage summary (the most authoritative per-char silent list); M06's "X of Y per tier" format is the cleanest model and worth standardising on.
- **M03/M04** have no coverage summary; counts here are detector-derived.
- **M01/M02** need separate handling: M01 has no per-char tier split; M02's per-char tier files exist on disk but were never captured into prose_section.
- To get a single exact, comparable "of 126 questions, N silent" per characteristic, the tier-answer files would need a standard coverage line (M06-style); that is the recommended fix.