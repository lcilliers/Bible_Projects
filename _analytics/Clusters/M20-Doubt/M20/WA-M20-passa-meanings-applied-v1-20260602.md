# WA-M20-passa-meanings-applied-v1-20260602

Pass A meaning record for cluster M20 via Claude API (Sonnet 4.6).
Governing instruction: wa-sessionb-cluster-instruction-v2_0-20260515 §5.

## Summary

- Verses targeted: 1
- Verses with meaning filled: 1
- Batches: 1
- Sentinel violations (meanings containing group/sub-group/VCG references): 0

## API usage totals

- Input tokens: 152
- Output tokens: 120
- Cache create tokens: 1,528
- Cache read tokens: 0

## Sample meanings (first 5)

- Psa 10:10 (H3512A ka.ah): The helpless are crushed and brought low under the oppressor's power, depicting a spirit broken and collapsed — the inner person sinks into utter disheartening through violent domination.

## Sentinel violations

_(none — all meanings free of group/sub-group/VCG references)_

## Patch

- File: `wa-cluster-M20-patch-passa-meanings-v1-20260602.json`
- Operations: 1 VCREVISE updates
- Apply: `python scripts/apply_session_patch.py --dry-run G:/My Drive/Bible_study_projects/Sessions/Session_Clusters/M20/wa-cluster-M20-patch-passa-meanings-v1-20260602.json` then live