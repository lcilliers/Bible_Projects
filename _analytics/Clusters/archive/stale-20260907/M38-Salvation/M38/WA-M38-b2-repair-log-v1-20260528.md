# M38 B.2 sub-group repair log (v2)

**Date:** 2026-05-28
**Trigger:** Initial B.2 output had coverage issues — 46 duplicates, 15 missing, 1 extra.
**Resolution:** Targeted API repair preserving the 7 sub-group design and assigning each affected vc_id to exactly one sub-group.

## Coverage stats

- Expected cluster vc_ids: 310
- Final assigned vc_ids: 310
- Missing after repair: 0 []
- Extras after repair: 0 []
- Repair API call: 61 vc_id assignments returned

## Final sub-group counts

- **M38-A** — Eschatological salvation received by faith: 121 verses (39.0%)
- **M38-B** — Physical rescue from mortal danger: 15 verses (4.8%)
- **M38-C** — Healing wholeness through faith exercised: 12 verses (3.9%)
- **M38-D** — Conscience cleansed through atonement received: 39 verses (12.6%)
- **M38-E** — Priestly mediation machinery of atonement: 44 verses (14.2%)
- **M38-F** — Salvation anticipated and hope sustained: 37 verses (11.9%)
- **M38-G** — Ransomed identity gratitude and memory: 42 verses (13.5%)

Sum: 310 (✓ matches)

## API usage

- Input: 9,640
- Output: 3,806
- Duration: 70.0s