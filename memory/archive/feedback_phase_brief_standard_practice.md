---
name: phase-brief-standard-practice
description: "For every AI-facing phase in the cluster pipeline, CC drafts a phase-brief alongside the structural input report."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 7401fa55-df1f-434c-9ff3-b60b0138422f
---

For every AI-facing phase in the Session B cluster pipeline (v2_0: Phases 3, 5, 7, 9, 10), CC drafts a phase brief alongside the structural input report it generates. This is in addition to the report itself, not a replacement.

**Why:** Pure structural reports (constitution report, subgroup-meanings report, catalogue prompts) carry the analytical material but don't frame the task, name the decisions already made, or surface special-handling flags that emerged from prior phases. Without a brief, AI either has to re-derive context from the obslog (slow and error-prone) or makes assumptions that conflict with CC's operational state. With a brief, the handoff is bounded and the discipline reminders are explicit.

**How to apply:**

- Filename pattern: `WA-{code}-phase{N}-brief-to-AI-v1-{date}.md` in `Sessions/Session_Clusters/{code}/`.
- Reference the governing v2_0 instruction section.
- Sections to include: phase open state · task one-paragraph · inputs · decisions already made (so AI doesn't re-debate) · special-handling flags from prior phases (e.g. Deu 32:27 divine-inner-state set-aside for Phase 7) · output expected (filenames + structure) · discipline reminders from v2_0 §2.x and from prior failures · "when you're done" next-step pointer.
- Save alongside the structural report in the same `Sessions/Session_Clusters/{code}/` folder.

**First instances:** `WA-M01-phase5-brief-to-AI-v1-20260516.md` (Phase 5 sub-group formation) · `WA-M01-phase7-brief-to-AI-v1-20260516.md` (Phase 7 VCG design — written 2026-05-16). The Phase 5 brief is the canonical template; Phase 7 follows the same shape.

**Trigger:** any time CC generates a structural report intended for AI consumption in the next phase, also draft the brief.

Related: [[project_current_work]] for the v2_0 methodology context. [[feedback_chat_vs_api_for_classification]] for the chat-vs-API split (briefs apply to chat phases; API atomic-per-row phases don't need them).
