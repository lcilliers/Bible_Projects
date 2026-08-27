---
name: feedback-obslog-discipline-for-cc
description: CC (not just AI chat) must write workings to obslog continuously throughout a pipeline run; surfacing notes in chat are stale by the time the researcher sees them
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 7401fa55-df1f-434c-9ff3-b60b0138422f
---

CC must adopt the "write workings to obslog continuously" discipline that already applies to AI chat work. Background tasks, multi-stage script chains, and long pipeline runs (Phase A→B→C→D for a cluster) generate state changes that only surface in chat as terse notes, often after summarisation has compressed the trail. By the time the researcher checks in, the chat surface no longer reflects what is actually in the DB or on disk.

**Why:** 2026-05-28 — researcher got lost in the M38 pipeline (Phase D complete, essay drafted, status flipped to Analysis Complete) because the background runs and intermediate states surfaced only as fragments in chat. When asked to "continue with Phase D char3", the request was based on a stale mental model — Phase D was already done. Without an obslog, neither researcher nor CC could quickly reconstruct ground truth without re-querying the DB.

**How to apply:**
- For every cluster pipeline run, open or append to `Sessions/Session_Clusters/{CODE}/wa-cluster-{CODE}-obslog-v{n}-{date}.md` at the start.
- Log each material action with timestamp, file paths touched, DB writes (with row counts), and outcomes. Same discipline as AI chat obslogs.
- Update the obslog when state advances (Phase A complete, B.1 done, B.2 design surfaced, C applied, D loaded, essay drafted, DOCX rendered, committed).
- The obslog is the canonical record of what CC did; chat is for alerts and brief summaries.
- On every new turn in a cluster pipeline, CC should read the latest obslog before acting, not rely on chat memory or summaries.

Related: [[feedback-review-via-files-not-chat]] (multi-item decisions go to markdown files); [[feedback-interaction-protocols]] (workings to .md files).
