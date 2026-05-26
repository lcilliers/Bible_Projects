# WA-M11-passa-meanings-applied-v1-20260526

Pass A meaning record for cluster M11 via Claude API (Sonnet 4.6).
Governing instruction: wa-sessionb-cluster-instruction-v2_0-20260515 §5.

## Summary

- Verses targeted: 1
- Verses with meaning filled: 1
- Batches: 1
- Sentinel violations (meanings containing group/sub-group/VCG references): 0

## API usage totals

- Input tokens: 160
- Output tokens: 108
- Cache create tokens: 0
- Cache read tokens: 1,540

## Sample meanings (first 5)

- Rom 11:15 (G0580 apobolē): The rejection of one people paradoxically becomes the very mechanism through which the world is brought into reconciliation with God, suggesting that divine restoration operates through loss, not desp

## Sentinel violations

_(none — all meanings free of group/sub-group/VCG references)_

## Patch

- File: `wa-cluster-M11-patch-passa-meanings-v1-20260526.json`
- Operations: 1 VCREVISE updates
- Apply: `python scripts/apply_session_patch.py --dry-run G:/My Drive/Bible_study_projects/Sessions/Session_Clusters/M11/wa-cluster-M11-patch-passa-meanings-v1-20260526.json` then live