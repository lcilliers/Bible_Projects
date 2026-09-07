# WA-M10c-passa-meanings-applied-v1-20260526

Pass A meaning record for cluster M10c via Claude API (Sonnet 4.6).
Governing instruction: wa-sessionb-cluster-instruction-v2_0-20260515 §5.

## Summary

- Verses targeted: 263
- Verses with meaning filled: 263
- Batches: 6
- Sentinel violations (meanings containing group/sub-group/VCG references): 0

## API usage totals

- Input tokens: 32,916
- Output tokens: 31,131
- Cache create tokens: 1,475
- Cache read tokens: 7,375

## Sample meanings (first 5)

- Gen 34:5 (H2930A ta.me): A violent sexual act is named as defilement against a person; the inner impact is felt as violation of a daughter, prompting a father's restrained, simmering awareness of wrong done.
- Gen 34:13 (H2930A ta.me): The defilement of a sister becomes the moral justification the brothers invoke inwardly to authorize deceit; the sense of violated honour drives a calculated, vengeful will.
- Gen 34:27 (H2930A ta.me): The remembered defilement of a sister is cited as the moral cause that releases extreme retributive violence; the inner engine is a will acting from perceived obligation to avenge violated honour.
- Lev 5:2 (H2931 ta.me): Contact with a ritually unclean object transmits an impurity the person may not immediately know; guilt surfaces when awareness arrives, indicating conscience awakening after hidden violation.
- Lev 5:3 (H2930A ta.me): Unknowing contact with human uncleanness defiles a person; the guilt becomes real only when the person becomes aware, showing that defilement can precede conscious recognition.

## Sentinel violations

_(none — all meanings free of group/sub-group/VCG references)_

## Patch

- File: `wa-cluster-M10c-patch-passa-meanings-v1-20260526.json`
- Operations: 263 VCREVISE updates
- Apply: `python scripts/apply_session_patch.py --dry-run G:/My Drive/Bible_study_projects/Sessions/Session_Clusters/M10c/wa-cluster-M10c-patch-passa-meanings-v1-20260526.json` then live