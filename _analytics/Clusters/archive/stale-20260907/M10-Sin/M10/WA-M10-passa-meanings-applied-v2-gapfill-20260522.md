# WA-M10-passa-meanings-applied-v1-20260522

Pass A meaning record for cluster M10 via Claude API (Sonnet 4.6).
Governing instruction: wa-sessionb-cluster-instruction-v2_0-20260515 §5.

## Summary

- Verses targeted: 3
- Verses with meaning filled: 3
- Batches: 1
- Sentinel violations (meanings containing group/sub-group/VCG references): 0

## API usage totals

- Input tokens: 394
- Output tokens: 264
- Cache create tokens: 0
- Cache read tokens: 1,130

## Sample meanings (first 5)

- Num 5:8 (H3725 kip.pu.rim): Atonement here is a required ritual offering (the ram) that restores a broken relationship with God when no human recipient exists for restitution, showing it functions as the necessary inner-relation
- Mic 3:10 (H5766B av.lah): Injustice here is the moral material used to construct Jerusalem—violence and wrongdoing are the foundation of civic building, showing injustice as an active inner disposition of the will that corrupt
- Rom 7:20 (G0266 hamartia): Sin is located as an indwelling force within the self, distinct from the person's conscious will—it operates inside the person, overriding chosen intent, revealing it as a constitutional inner power t

## Sentinel violations

_(none — all meanings free of group/sub-group/VCG references)_

## Patch

- File: `wa-cluster-M10-patch-passa-meanings-v1-20260522.json`
- Operations: 3 VCREVISE updates
- Apply: `python scripts/apply_session_patch.py --dry-run G:/My Drive/Bible_study_projects/Sessions/Session_Clusters/M10/wa-cluster-M10-patch-passa-meanings-v1-20260522.json` then live