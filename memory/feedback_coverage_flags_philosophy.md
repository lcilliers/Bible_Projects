---
name: Coverage flags — informational not gating
description: Programme-level principle — term verse-coverage ≠ analytical value; coverage flags must inform approach, not limit inclusion
type: feedback
originSessionId: 62ef2dc4-cbcd-4fc0-9a07-8c2ace3bedec
---
Coverage/volume flags (SMALL_VERSE_SAMPLE, THIN_DATA, HIGH_FREQUENCY_ANCHOR, NO_VERSES, SPAN_FILTER_APPLIED, etc.) were introduced early in the project with an implicit "less volume = less attention" logic — a way to limit scope when data was thin.

**The study has disproven this assumption.** Verse count has little correlation with a term's analytical value. Context and contents drive significance. Even **absence of expected evidence** (a term the researcher expected to see but doesn't) can be analytically significant.

**Therefore:**

- Coverage information IS worth knowing — it may indicate a different analytical approach is warranted (e.g., a single-verse term may require close reading rather than statistical pattern analysis).
- Coverage information MUST NOT be inconsistent, erroneous, or used to gate/limit inclusion.
- Current flags are inconsistent (multiple overlapping codes with unclear semantics), wrong (e.g., SMALL_VERSE_SAMPLE mis-triggered via ratio when the flag defines absolute count), and send the wrong signal (imply downgraded attention).

**Why:** le Roux's empirical finding from the research itself — low-volume terms have yielded some of the highest-value analytical insights; absence-where-presence-expected is itself a discovery pattern.

**How to apply:**

- When designing new flags or reviewing existing ones, classify each as either (a) informational diagnostic — captures data shape, informs approach — or (b) gate/filter — restricts downstream processing. Prefer (a); any (b) must be justified explicitly.
- When a flag name or description implies reduced analytical priority ("thin", "small", "insufficient"), reword to describe the data shape neutrally (e.g., "concentrated verse set", "single-occurrence term", "span-filtered coverage").
- Never let coverage flags gate Session A/B/C/D inclusion or Dimension Review processing.
- The pilot's Path 1 emitters that set coverage flags need redesign alongside the flag catalogue review.
