# VC Quality — Practical View (flags + missing groups)

_Generated 2026-04-26 · Scope: registries with `verse_context_status` set, excluding NULL/excluded_

---

## (a) Registries with NO verse_context_groups

**One** registry is in this state:

| reg | word | VC status | OWNER terms | Active verses | Active groups |
|---:|---|---|---:|---:|---:|
| 48 | diligence | **Complete** | 6 | 82 | **0** |

**Action:** marked Complete but no classification work present. Either the work was lost / never imported, or the status flag is wrong. Worth investigating before any downstream stage trusts this registry.

---

## (b) Flags that put a question mark on existing VC groups

Filtered for **unresolved flags** that bear on classification quality (not extraction errors / occurrence_count anomalies that are upstream).

### Most VC-actionable (8 flags across 7 registries)

| reg | word | flag | term | issue |
|---:|---|---|---|---|
| 4 | anger | PH2_BOUNDARY_QUESTION | G3948 paroxusmos | pos/neg sense split (Acts 15:39 sharp dispute vs. Heb 10:24 stir-up to love) — single grouping likely conflates the two |
| 50 | disobedience | SB_FINDING | G3878 parakouo | 2 senses in 1 group (refuse-to-listen vs. overhear) |
| 98 | justice | PH2_DATA_QUALITY ×2 | H4639H, H4639I | sub-gloss labels with NO verses — extracted_thin shells, no classification basis |
| 103 | love | PH2_DATA_QUALITY | H7356B rachamim | 69 verses but significant root-bleed from H7358 (physical womb) — group context likely contaminated |
| 165 | unbelief | SB_FINDING | G0570 apistia | flagged for 8-group fragmentation across 11 verses — current grouping under-segmented |
| 165 | unbelief | PH2_BOUNDARY_QUESTION | G0544 apeitheō | straddles registry 165 ↔ 50 boundary (disbelief vs. disobedience) |
| 181 | zeal | SB_FINDING | G4710 spoudē | flagged for 11-group fragmentation across 12 verses — current grouping under-segmented |
| 212 | pray | **PH2_DATA_SPLIT_REQUIRED** (HIGH priority) | H6293 paga | 3 distinct senses in 43 verses (meet / attack / intercede) — needs split |

### Already in flight

`H6293 paga` (mti=937, registry 212 pray) is already in **VCB-014** which was just applied. Worth checking the VCB-014 patch's grouping decision for this term against the PH2-212-001 split flag — the flag predates the v3_10 contracts. Either the v3_10 classification surfaced the same split (good — flag can resolve) or it didn't (flag stays open).

### Other SB_FINDING flags worth noting (lower urgency)

| reg | word | flag | nature |
|---:|---|---|---|
| 67 | goodness | SBF-VCB013-001 | tripartite engagement pattern (chrēstotēs) — narrative finding, not classification fault |
| 69 | gratitude | SBF-VCB013-002 | tripartite engagement pattern (eucharisteō) — narrative finding |
| 85 | imagination | VCB11-SB-004 / -008 | classifier judgement calls on individual verses (mas.kit, enthumesis) |
| 115 | passion | VCB11-SB-001 | judgement call on Joh 18:28 |
| 139 | righteousness | SBF-vc139-001 | wide characteristic span across 10 verses — group breadth flagged |
| 202 | transformation | VCB11-SB-007 / -009 | individual verse judgement calls on cha.laph |

These are mostly Session-B-stage observations rather than VC-stage faults — treat as input to Session B narrative, not as a "redo VC" signal.

---

## What this means in practical terms

- **From flag evidence alone, ~7 specific terms have a concrete quality question over their VC grouping** — most concentrated in registries 165 unbelief, 181 zeal, 103 love, 4 anger, 212 pray, 98 justice, 50 disobedience.
- **One registry (48 diligence) needs a separate look** — its Complete status is unsupported by any actual VC group rows.
- This is a much smaller, named, evidence-anchored list than the 1,800-term legacy-Complete bucket the strategy doc was sizing. **A pinpoint pass over these ~7 terms + the diligence anomaly is feasible without invoking any bulk-decision machinery.**
- Pinpoint corrections for these would use existing VCGROUP / VCVERSE patches per `vc-corrective-strategy v1 §4.2` — already supported by the applicator, no instruction-doc work needed.

## Suggested next concrete action

1. **Investigate diligence (48):** is the Complete status accurate? If not, reset to NULL or `In Progress` and queue for proper VC classification.
2. **Schedule a pinpoint VCGROUP/VCVERSE batch** covering the 7 terms in the table above. Small, surgical, no full re-classification — just the named issues.
3. **Defer the bulk-decision question** until predictors stabilise. The flag-driven list above gives you tangible progress while the statistical evidence accumulates.
