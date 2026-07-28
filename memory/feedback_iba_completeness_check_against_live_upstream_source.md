---
name: feedback_iba_completeness_check_against_live_upstream_source
description: "When auditing whether an IBA extract/JSON captures 'everything' about a Strong's number, compare against the live upstream source (STEP getInfo) directly, not just the DB tables already sourced from it — DB population can lag or omit fields the source actually provides."
metadata:
  type: feedback
  originSessionId: 21fa5b5d-274b-4153-accc-4050bc134ad7
  modified: 2026-07-25T11:53:08.786Z
---

Asked to check whether STEP contains information about a Strong's number "on all levels" not captured
in the lexicon-combined JSON, the right move was calling STEP's live `getInfo` endpoint directly and
diffing its full field set against every DB table already feeding the extract — not just re-checking
the extract logic against the DB. This surfaced two real, confirmed gaps: (1) the `strong` table
(`accentedUnicode`, `stepGloss`, `stepTransliteration`, `count`, `freqList`) was already fully
populated in `iba.db` (3463/3463 rows) but never wired into any extract script; (2) `relatedNos`
(cross-references to other related Strong's numbers) wasn't stored anywhere in the DB at all — STEP
has it, nothing captures it. Got an explicit "good find" after delivering both as working, verified
output.

**Why:** `strong_lexicon`/`strong_meaning_tree` were themselves populated FROM STEP at some point, but
DB population can be partial, stale, or scoped narrower than what the live source actually returns —
auditing only the DB (even thoroughly) cannot surface a field the DB never captured in the first place.
The live source is the only place that question can actually be answered.

**How to apply:** for any "does X have more than we've captured" question about IBA lexicon/Strong's
data, call the live STEP endpoint for a real sample term, inspect the FULL raw response (all keys, not
just the ones the existing extract already reads), and cross-check each field against DB table content
byte-for-byte before concluding it's already covered vs. genuinely missing. Distinguish "missing from
the DB" (needs new capture, bigger decision — e.g. changing the governed `raw.detail` onboarding step)
from "in the DB but never extracted" (cheap fix — just wire in a new source). Don't guess which bucket a
gap falls into; check the actual table for it. Related: [[feedback_iba_gap_analysis_requires_live_build_inspection]]
(same principle, applied to internal code+DB rather than an external upstream source).
