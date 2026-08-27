# WA-M10b-passa-meanings-applied-v1-20260525

Pass A meaning record for cluster M10b via Claude API (Sonnet 4.6).
Governing instruction: wa-sessionb-cluster-instruction-v2_0-20260515 §5.

## Summary

- Verses targeted: 514
- Verses with meaning filled: 514
- Batches: 11
- Sentinel violations (meanings containing group/sub-group/VCG references): 0

## API usage totals

- Input tokens: 59,239
- Output tokens: 55,398
- Cache create tokens: 1,547
- Cache read tokens: 15,470

## Sample meanings (first 5)

- Gen 18:23 (H7563 ra.sha): The wicked are those whose moral status is the opposite of the righteous — Abraham's question implies that wickedness and righteousness are distinct inner conditions that ought to receive distinct jud
- Gen 18:25 (H7563 ra.sha): The wicked are those who deserve death as a just consequence of their condition — conflating them with the righteous would violate the divine judge's moral character.
- Exo 2:13 (H7563 ra.sha): The man in the wrong is the aggressor in the fight — his wickedness is an active behavioral choice to strike a companion, a relational violation observed and named by an outsider.
- Exo 9:27 (H7563 ra.sha): Pharaoh acknowledges being in the wrong in contrast to God's rightness — this is a moment of conscience surfacing under pressure, even if the admission is situational rather than transformative.
- Exo 23:1 (H7563 ra.sha): The wicked man recruits others into complicity through false testimony — wickedness here is a social and moral force that corrupts the will of bystanders drawn into alliance with it.

## Sentinel violations

_(none — all meanings free of group/sub-group/VCG references)_

## Patch

- File: `wa-cluster-M10b-patch-passa-meanings-v1-20260525.json`
- Operations: 514 VCREVISE updates
- Apply: `python scripts/apply_session_patch.py --dry-run G:/My Drive/Bible_study_projects/Sessions/Session_Clusters/M10b/wa-cluster-M10b-patch-passa-meanings-v1-20260525.json` then live