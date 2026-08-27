---
name: feedback_verse_change_revalidation
description: Material verse-data changes invalidate findings; a closed cluster touched by one must reset for re-analysis
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 55b65c4e-7bc5-4e5a-98db-5d25382b8a12
---

A **material** verse change — verse-record deletion, meaning/keyword change, is_relevant/anchor re-classification — invalidates findings that rest on it. If such a change touches an `Analysis Complete` cluster, that cluster must reset to `Ready for re-analysis` (extending reset-if-complete from pointer assignment to verse-data changes). *Identity-preserving* changes (e.g. re-pointing `verse_record_id` to a surviving duplicate) do NOT reset.

**Why:** the researcher surfaced this (2026-06-02) — we marked 4 clusters Analysis Complete without considering that later verse changes could stale their findings. We had reset-if-complete for *pointers* only.

**How to apply:** verse-changing appliers carry the reset rule; the dedup-ghost repair (`_repair_dedup_ghost_verses_v1`) + the auditor's VRACT guard (B1a/B1b/B2 exclude verses whose verse-record is soft-deleted) implement the data side. Documented in the orchestrator design doc. Relates to [[feedback_integrity_and_intent_first]], [[feedback_two_governing_principles]] (verse meaning is the data and rules analytics).
