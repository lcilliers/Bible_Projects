---
name: project_keyword_analytics_revision_parked
description: PARKED 2026-06-04 — keyword analytics + bias analysis must be rebuilt phrase-aware. Pass-A keywords are 2-word [HEAD faculty][QUALIFIER predicate] phrases (91%); single-token cuts are misleading; the QUALIFIER axis is where interpretive bias lives.
metadata:
  type: project
---

**Parked 2026-06-04**, to resume later. While exploring anchor-verse meaning+keywords (226 anchors, all
in the Sin/Repentance/Salvation family M10/M10b/M10c/M11/M38), two things surfaced:

1. **Serious verse-meaning "transgressions"** in the Pass-A readings (parked for deeper review) — e.g.
   `eschatological` applied reflexively to any salvation verse (Gen 49:18, Hab 3:8), "unclean spirits"
   conflated with ritual defilement (Mar 3:11, Luk 6:18), inner-being "will" language laid over
   involuntary bodily-ritual impurity. This is the verse-meaning-soundness risk made concrete
   ([[project_next_action_audit_surface_verses]]).
2. **The keyword analytics were methodologically flawed** and must be revised. Pass-A keywords are
   structured **2-word `[HEAD] [QUALIFIER]`** phrases (91% are exactly 2 words; noun-then-modifier):
   HEAD = inner-being faculty/entity (will, guilt, conscience, salvation…); QUALIFIER = interpretive
   predicate (eschatological, corrupted, absent, divine…). **Single-token frequency pools one word across
   dozens of different claims and destroys the signal.** The QUALIFIER axis is where bias concentrates.

**Plan captured:** `research/investigations/keyword-analytics-revision-plan-20260604.md` — rebuild both
`_exploratory_anchor_meaning_analytics_v1` and `_exploratory_keyword_bias_extract_v1` to be phrase-aware
(HEAD / QUALIFIER / HEAD×QUALIFIER cuts) with normalisation (hyphen/stem); drive the bias trap from a
qualifier-risk list. Open question: post-hoc normalisation now vs a controlled keyword vocabulary
enforced at Pass-A emission later (ties to §c keyword rule + the verse-meaning audit).
The misleading token table in `anchor-meaning-analytics-20260604.md` is banner-flagged as superseded.

Related: [[reference_analysis_rules_finding_lifecycle]] (Pass-A emits meaning+keywords) ·
[[feedback_two_governing_principles]].
