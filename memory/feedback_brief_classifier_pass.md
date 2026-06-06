---
name: Brief classifier pass — per-verse architecture, group-first
description: Brief plain-English classifier for grouping unclassified verses. Per-verse architecture — one call per verse with all spans, N atomic per-term decisions per call.
type: feedback
originSessionId: 0d41cb24-79b1-4e0f-9ed8-483f94c8ba5e
---
For unclassified-verse processing, the user has chosen a stripped-down brief classifier over the rich per-verse "meaning router" contract.

**Architecture (settled 2026-05-04):** pairing is **(verse text + all spans) ⇒ one decision per programme-relevant term in the verse**. One API call per verse; output is an array of N atomic per-term decisions. The earlier per-(verse, term) architecture re-transmitted each verse and span set on average 2.5× (16× for dense verses like Neh 9:17) — wasteful and made `wrong_face` necessary to handle inner-being content carried by sibling terms. With the per-verse architecture every term gets its own decision in the same call, so `wrong_face` is **dropped** from the set-aside enum (now: `no_inner_being | physical_only | spatial_only | unclear`).

**Contract per term:** one short plain-English sentence (≤25 words) saying what the verse says about the inner-being characteristic via that term, OR `set_aside` with one reason. No morphology essay, no §3 framing, no unresolved pointers.

**Why brief, not deep:** the rich meaning-router preserved atomic discipline at scale but cost $300–$2,100 for the full corpus. The user reframed the first objective as "group verses with similar meaning together" — a brief summary is enough for grouping; only survivors need deeper analysis. "I think we are over engineering."

**Why per-verse, not per-pair:** 57,703 OWNER pair-rows over 23,290 distinct verses. Per-verse cuts redundancy ~50–65% and lets the model see all sibling terms together when deciding any one. Sonnet 4.6 + medium effort runs ~$0.008/verse.

**How to apply:** when designing classifier passes for the unclassified-verse cohort, default to the **per-verse brief** contract. Reach for the deeper meaning-router only after the grouping pass has narrowed the survivors. Don't reintroduce morphology essays, §3 framing, unresolved-pointer fields, or `wrong_face` set-aside reasons into the brief pass.

**Reference scripts (2026-05-04):**
- [`scripts/_exploratory_unclassified_verse_sample_v1_20260504.py`](g:/My%20Drive/Bible_study_projects/scripts/_exploratory_unclassified_verse_sample_v1_20260504.py) — per-verse sample builder
- [`scripts/_exploratory_brief_verse_router_v1_20260504.py`](g:/My%20Drive/Bible_study_projects/scripts/_exploratory_brief_verse_router_v1_20260504.py) — per-verse brief classifier
- [`scripts/_exploratory_brief_meaning_router_v1_20260504.py`](g:/My%20Drive/Bible_study_projects/scripts/_exploratory_brief_meaning_router_v1_20260504.py) — earlier per-pair version (kept as fallback)
