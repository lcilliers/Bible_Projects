# M10 — Split design (3-way), v1

**Date:** 2026-05-22
**Cluster as defined (v6 / 2026-05-05):** M10 — Guilt, Sin and Transgression (88 OWNER terms, 26 contributing registries, ~2,287 verses)
**Decision:** Split into three sibling clusters before any Phase 1 work, on ontological grounds.

---

## 1. Why split

The 26 contributing registries assigned to M10 by v6 meaning-similarity cover three distinct ontological tracks of moral failure:

| Track | Question it answers | Lexical centre |
|---|---|---|
| **Act / state of failure** | *What did I do? What is my standing before God?* | sin, guilt, transgression, iniquity, rebellion |
| **Character of evil** | *What kind of person are they? What is the moral nature of this conduct?* | evil, wickedness, abomination |
| **Ritual / moral defilement** | *What state has this rendered me / this thing?* | impurity, defilement, uncleanness |

Per v2_8 §6.3.2 (verse-level relationship test) and §8.0 (sub-groups represent characteristics), forcing all three tracks through a single cluster would either:
- collapse the three tracks into one sub-group structure and lose ontological precision, or
- produce 3 top-level characteristics inside one cluster, which is the structural signature of an under-split cluster.

Splitting now, before Phase 1, is cheaper than splitting later. The cluster has `status='Not started'`, so no analytical work is invalidated.

## 2. Split assignment (registry-level cuts)

### M10 — Sin, Guilt and Transgression  (63 terms · 19 registries · ~1,475 V)

The act/state track: doing wrong, being guilty, breaking covenant, falling short.

| # | Reg | Word | Terms | V |
|---|---:|---|---:|---:|
| 1 |  73 | guilt ★ anchor | 16 | 965 |
| 2 | 128 | rebellion | 5 | 138 |
| 3 |  59 | faith (unfaithfulness terms ba.gad/ma.al) | 3 | 103 |
| 4 |  89 | iniquity | 6 | 66 |
| 5 | 147 | sin | 4 | 47 |
| 6 |  31 | corruption (corrupt-acts) | 6 | 34 |
| 7 | 162 | transgression | 4 | 30 |
| 8 | 149 | slander (blasphemy-as-act) | 2 | 22 |
| 9 | 120 | perverseness | 4 | 19 |
| 10 |  98 | justice (injustice-acts) | 3 | 15 |
| 11 |   2 | agony (cha.val/che.vel writhing-in-guilt) | 2 | 12 |
| 12 |  51 | distress (a.ven trouble/iniquity) | 1 | 11 |
| 13 | 111 | mercy (kip.pu.rim atonement, paired with sin) | 1 | 8 |
| 14 |  40 | deceit (deleazō entice) | 1 | 3 |
| 15 |   6 | anointing (te.vel perversion) | 1 | 2 |
| 16 |  71 | grief (pu.qah) | 1 | 1 |
| 17 |  81 | hypocrisy (sunupokrinomai) | 1 | 1 |
| 18 | 134 | renewal (cha.loph decay/destruction) | 1 | 1 |
| 19 | 190 | contempt (nav.lut lewdness) | 1 | 1 |

### M10b — Wickedness, Evil and Abomination  (17 terms · 4 registries · ~537 V)

The character track: what kind of person, what kind of conduct in its nature.

| # | Reg | Word | Terms | V |
|---|---:|---|---:|---:|
| 1 | 172 | wickedness ★ anchor (ra.sha, mir.sha.at) | 2 | 181 |
| 2 |   1 | abomination (to.e.vah, shiq.quts, bdelugma, bdeluktos) | 4 | 145 |
| 3 |  57 | evil ★ anchor (ponēros, kakia, adikia, ponēria, blasfēmeō, kakopoios, atopos, faulos, re.sha) | 9 | 126 |
| 4 | 151 | sorrow (a.ven, ro.a as evil-character/condition) | 2 | 85 |

### M10c — Defilement and Impurity  (8 terms · 3 registries · ~275 V)

The defilement track: ritual + moral uncleanness, separation language.

| # | Reg | Word | Terms | V |
|---|---:|---|---:|---:|
| 1 |  86 | impurity ★ anchor (ta.me, nid.dah, akatharsia, akathartos) | 5 | 270 |
| 2 |  41 | defilement (molunō, molusmos) | 2 | 4 |
| 3 | 115 | passion (miasmos) | 1 | 1 |

## 3. Cluster-row metadata for new siblings

| Field | M10 (revised) | M10b (new) | M10c (new) |
|---|---|---|---|
| `cluster_code` | M10 | M10b | M10c |
| `description` | Sin, Guilt and Transgression | Wickedness, Evil and Abomination | Defilement and Impurity |
| `short_name` | Sin | Wickedness | Defilement |
| `source` | meaning_v2 | meaning_v2_split_20260522 | meaning_v2_split_20260522 |
| `bucket` | NAMED | NAMED | NAMED |
| `status` | Not started | Not started | Not started |
| `version` | v6 | v6 | v6 |
| `gloss` | (regenerate from members) | (regenerate from members) | (regenerate from members) |

## 4. Term migration counts

```
Before:  M10 = 88 OWNER terms / 26 registries / ~2,287 V
After:   M10  = 63 terms / 19 registries / ~1,475 V
         M10b = 17 terms /  4 registries /   ~537 V
         M10c =  8 terms /  3 registries /   ~275 V
Total preserved: 63 + 17 + 8 = 88 ✓
```

## 5. Borderline terms — recorded for new-cluster Phase 1

These calls were made at registry-level to keep the apply script simple. The receiving cluster's Phase 1 may reroute individual terms:

- **R057.G0987 blasfēmeō** (verb, "to blaspheme") was moved with R057 → M10b, but R149 blasfēmia/blasfēmos stayed in M10. M10b Phase 1 should consider whether to push blasfēmeō back to M10 to keep the blasphemy lemma family together.
- **R057.G0093 adikia** ("unrighteousness/wickedness") and **R098.G0094 adikos** ("unjust") split across M10b and M10 by registry. Same root family — Phase 1 in each cluster should record the cross-reference.
- **R051.H0205H a.ven** stayed in M10 (distress home) but **R151.H0205G a.ven** moved with R151 → M10b. Same lexeme, different home-registry assignments in v6. Cross-cluster handoff observation required.
- **R134.H2475 cha.loph** ("change/decay") in M10 vs **R031.H4893B-H4889 mash.chet/mash.chit** ("destroyer") in M10 — coherent stay-call; just noting destruction-semantics is split between M10 (acts) and other M-clusters (not split here).

## 6. Apply order

1. INSERT cluster rows M10b, M10c.
2. UPDATE `cluster` SET description='Sin, Guilt and Transgression', short_name='Sin' WHERE cluster_code='M10'.
3. UPDATE `mti_terms.cluster_code` to 'M10b' for 17 terms (registries 1, 57, 151, 172).
4. UPDATE `mti_terms.cluster_code` to 'M10c' for 8 terms (registries 41, 86, 115).
5. Regenerate gloss strings for all three from current member terms.
6. Verify totals: M10=63, M10b=17, M10c=8.

Script: `scripts/_apply_m10_split_3way_20260522.py`

## 7. Downstream

- Cluster overview report: refresh once split is applied — should show 16 clusters now (M10 stayed, M10b/M10c added).
- Phase 1 work on each cluster is independent and can begin in any order.
- M10c is small (8 terms / 275 V) but has a clear anchor (impurity, 270 V) and survives §8.6 distribution gate easily.

---

*Split design v1 — apply pending researcher confirmation already given (Option A 3-way split, 2026-05-22).*
