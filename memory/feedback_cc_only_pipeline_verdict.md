---
name: feedback-cc-only-pipeline-verdict
description: "M38 ran entirely through CC (API + CC drafting) as an experiment; verdict — prose not fluent, costs duplicate the subscription, audit-after-prose is the wrong order, speed gain not realized"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 7401fa55-df1f-434c-9ff3-b60b0138422f
---

The M38 experiment — running the entire cluster pipeline through CC including API calls for Phase A/B/D and CC-drafted Phase E essay — was instructive but not a success on its primary objectives.

**What failed:**
- **Prose fluency.** The essay reads as sentence-by-sentence construction from the findings rather than as integrated prose. Claude AI chat (where M11 prose was authored) holds holistic context across the whole essay in a way that the API-fed CC-drafted version did not. The CC-authored M38 essay quotes findings accurately but sentences often don't connect into a coherent flow.
- **Cost duplication.** The Claude AI subscription is paid; API spend ($9.40 for M38) is additional. The API does not draw from the subscription. So CC-driven pipelines effectively double the cost compared to AI-chat-driven equivalents.
- **Audit ordering.** Audit run after prose surfaced two real issues (Act 27:34 RESCUE candidate, 5 missing anchors) and 177 hygiene items. These should have been caught before the prose was authored, not after. Audit-before-prose is a phase gate.
- **Speed.** The CC-orchestrated pipeline was not faster than chat-driven. Background tasks, segment chunking, error recovery, and re-runs absorbed the time gain.

**Why:** 2026-05-29 — researcher retrospective at the end of the M38 experiment. The end product (prose) was the diagnostic.

**How to apply:**
- **Prose authoring belongs in AI chat.** Findings are CC's domain (data layer, audit-ready); essays are AI chat's domain (integrated voice across the whole piece).
- **Audit gates prose.** Run the v2_5 (or successor) audit at the end of Phase D before any Phase E essay is drafted. Real issues must be resolved or consciously deferred before prose authoring begins.
- **Re-think API use.** The Sonnet 4.6 API was useful for high-volume atomic work (Pass A meanings, B.3 VCG design per sub-group, Stage A per-characteristic findings) but the same work paid for inside the chat subscription is cheaper-per-equivalent. Reserve API for genuinely chat-unsuitable atomic work (output volume that won't fit) — and even then, verify the engine quality matches chat-level work.
- **Diagnostic move: re-author M38 prose in chat from existing findings.** If chat produces fluent prose from the same findings, the findings are fine and CC drafting was the bottleneck. If chat also struggles, the findings themselves need regeneration.

Related: [[feedback-chat-vs-api-for-classification]] (default to chat for one-shot batch work); [[feedback-small-chunks-over-elaborate-pipelines]]; [[feedback-obslog-discipline-for-cc]].
