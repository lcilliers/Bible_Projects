# WA-M01-passa-meanings-applied-v1-20260515

Pass A meaning record for cluster M01 via Claude API (Sonnet 4.6).
Governing instruction: wa-sessionb-cluster-instruction-v2_0-20260515 §5.

## Summary

- Verses targeted: 1031
- Verses with meaning filled: 1031
- Batches: 21
- Sentinel violations (meanings containing group/sub-group/VCG references): 0

## API usage totals

- Input tokens: 121,976
- Output tokens: 79,967
- Cache create tokens: 1,400
- Cache read tokens: 28,000

## Sample meanings (first 5)

- Gen 3:10 (H3372G ya.re): Adam's fear arises from exposed nakedness before God, driving him to hide—the inner state is shame-triggered dread of divine presence, felt immediately in the will as flight.
- Gen 9:2 (H2844A chat): Terror is an instilled inner disposition placed upon all animals toward humanity after the flood, making every creature fear humans as a divinely ordered reality.
- Gen 9:2 (H4172A mo.rah): Fear of humanity is decreed upon all living creatures; this fear functions as an embedded inner orientation in animals that ensures human dominion over the natural world.
- Gen 9:2 (H4172B mo.ra): Fear directed toward humans is placed upon every creature as a permanent condition; it shapes animals' inner response to mankind, producing avoidance and submission.
- Gen 15:1 (H3372G ya.re): God commands Abram not to fear, grounding the call on God's own protective presence as shield—the fear addressed is an inward anxiety about threat, countered by divine reassurance.

## Sentinel violations

_(none — all meanings free of group/sub-group/VCG references)_

## Patch

- File: `wa-cluster-M01-patch-passa-meanings-v1-20260515.json`
- Operations: 1031 VCREVISE updates
- Apply: `python scripts/apply_session_patch.py --dry-run G:/My Drive/Bible_study_projects/Sessions/Session_Clusters/M01/wa-cluster-M01-patch-passa-meanings-v1-20260515.json` then live