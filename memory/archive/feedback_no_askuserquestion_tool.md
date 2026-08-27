---
name: feedback_no_askuserquestion_tool
description: Do not use the AskUserQuestion tool; the researcher does not work with it.
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 7a3d6e48-d97f-407e-83ba-ecef211af3af
---

The researcher does **not** work with the AskUserQuestion tool — a call to it was rejected
outright with "I dont work with ask question". Present decisions and options in a filed `.md`
(or briefly in chat prose) and let them respond in their own words instead.

**Why:** they read/decide via the written record, not interactive prompts; the tool interrupts
their flow. Reinforces [[feedback_review_via_files_not_chat]].

**How to apply:** never call AskUserQuestion. When a decision is genuinely theirs, write the
options and a recommendation into the relevant `.md` and ask in plain chat text; act on their
reply. When they say "proceed with all fixes", proceed — don't re-confirm via a prompt tool.
