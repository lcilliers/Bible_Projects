# Task 5 — Zero-Term Registry Investigation

> Generated 2026-03-27 by Claude Code

## Summary

44 registries had `phase1_term_count = 0` or NULL. After investigation:

| Category | Count | Action Taken |
|----------|-------|-------------|
| Excluded (expected zero) | 31 | No action — these are excluded from Phase 1 by design |
| Data linkage (terms exist, count not recorded) | 6 | **Fixed** — updated phase1_term_count and phase1_verse_count |
| File index exists, no terms | 4 | Require Phase 1 extraction or investigation |
| No file index at all | 3 | Require Phase 1 setup or Conceptual Word Register designation |

## Data Linkage Fixes Applied

| No | Word | Terms | Verses |
|----|------|-------|--------|
| 3 | ambition | 5 | 10 |
| 51 | distress | 42 | 139 |
| 123 | pride | 26 | 285 |
| 151 | sorrow | 24 | 145 |
| 174 | wisdom | 15 | 595 |
| 178 | wrath | 4 | 14 |

## Remaining — Require Researcher Decision

### File Index Exists, No Terms (4)

| No | Word | Cluster | Category | Recommendation |
|----|------|---------|----------|---------------|
| 27 | consciousness | C22 | Identity/Selfhood | Possible Conceptual Word Register candidate — no direct Hebrew/Greek lexical equivalent |
| 109 | meekness | C08 | Character/Disposition | Data linkage likely — run Phase 1 extraction |
| 137 | resolve | C14 | Volitional/Will | Possible Conceptual Word Register candidate |
| 144 | sensuality | C12 | Affective/Emotional | Data linkage likely — run Phase 1 extraction |

### No File Index (3)

| No | Word | Cluster | Origin | Category | Recommendation |
|----|------|---------|--------|----------|---------------|
| 200 | energy | C20 | programme_addition | Volitional/Capacity | Recently added — needs Phase 1 setup and extraction |
| 205 | resentment | C07 | original_list | Affective/Emotional | Note: duplicate registry_no 136 (resentment) also exists as Excluded. Investigate duplication. |
| 211 | being | C01 | programme_addition | Anthropological/Structural | Possible Conceptual Word Register candidate — may not have direct lexical equivalent |
