---
name: feedback-audit-before-prose
description: Cluster audit must run at end of Phase D before any Phase E prose authoring; issues caught after prose is wasted re-work
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 7401fa55-df1f-434c-9ff3-b60b0138422f
---

The cluster audit (currently `_audit_cluster_against_instruction_v25_v1_20260518.py`, eventually v3_0 successor) must run at the close of Phase D, before Phase E prose authoring begins. Findings flagged by the audit — even low-impact ones like rescue candidates, missing anchors, ungrounded findings — should be triaged before they get quoted in essays.

**Why:** 2026-05-29 — M38 audit ran after the essay was drafted and rendered. It surfaced 1 real RESCUE (Act 27:34), 5 missing anchor flags, and 177 ungrounded char-scope findings. The essay quoted some of these underlying findings; any correction now creates rework on prose that was already authored and rendered.

**How to apply:**
- After Phase D Stage B loads cluster_finding rows and the status flips to `Analysis Complete`, CC runs the audit script automatically and writes the report to the cluster folder.
- Audit verdict gates Phase E:
  - **BOUNDED-FIXES with no real issues** → proceed to Phase E
  - **BOUNDED-FIXES with real issues** (rescue candidates, missing anchors, ungrounded findings with material impact) → surface to researcher; researcher decides between (a) patch now, (b) defer with note, (c) proceed and patch later
  - **PHASE-RESTART verdict** → stop; surface to researcher
- The audit report becomes a structural input to Phase E (the essay author knows which findings are fully evidence-grounded and which are flagged).
- If the audit is v2_5 against v3_0 data, the audit-run script header should declare the version mismatch so the researcher reads the flags through the right lens.

Related: [[feedback-cc-only-pipeline-verdict]] (audit was one of the four lessons); [[project-v25-audit-tool]].
