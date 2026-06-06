---
name: feedback-review-via-files-not-chat
description: "For non-trivial decisions or multi-item review, put proposals into a markdown file. Chat-based asks don't work for this researcher's workflow."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 7401fa55-df1f-434c-9ff3-b60b0138422f
---

When asking the researcher to review proposals, decisions across multiple items, or open questions — put them in a markdown file the researcher can read in their editor and mark up directly. **Do not present multi-item review menus in chat and ask "which option" — the researcher cannot review effectively that way.**

**Why:** stated 2026-05-18 — "in chat comments does not work for me." The researcher needs the persistent, side-by-side, mark-up-able review surface that markdown files provide. Chat is for status updates, alerts, and short questions; files are for substantive review.

**NEVER use the `AskUserQuestion` tool.** Confirmed 2026-06-01: "the autoquestion does not work for me … not the built-in method of three questions without content." The structured 3-question menu violates this researcher's global rules. Options and decisions are surfaced as *content* in a correctly-filed `.md`; the researcher reviews the file and responds. **Plan-mode note:** plan mode tries to force `AskUserQuestion`/`ExitPlanMode` endings — that conflicts with this protocol; write the content to the file and ask the researcher (in plain chat) to review / take you out of plan mode rather than firing the tool.

**How to apply:**
- For any decision request involving more than 2 options or more than 3 items, generate a review document in `Sessions/Session_Clusters/{code}/` (cluster work) or **`research/investigations/`** (cross-cluster / ad-hoc) — per [[feedback_follow_filing_standards]]. **Never `outputs/markdown/` (root is not a sanctioned location).**
- Each item gets its own block with: current state, proposed action, rationale, decision blank (e.g., `**Decision:** _[OPTION-A / OPTION-B / HOLD]_`), and rationale blank.
- Chat then carries only: "review document at `<path>`; ping me when you've marked decisions."
- The researcher annotates the file, saves it, and tells me to process the marked-up document.
- Existing precedent: [`WA-M04-terse-setaside-review-v1-20260518.md`](Sessions/Session_Clusters/M04/WA-M04-terse-setaside-review-v1-20260518.md) — 75 verses for review.

**Anti-pattern to avoid:** "Which sub-group should this go to — A or B? Let me know in chat." This forces the researcher into chat for a decision that belongs in a file.

Related: [[feedback-working-style]] (investigate first, show evidence, structured docs, wait for approval).
