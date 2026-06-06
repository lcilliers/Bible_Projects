---
name: feedback_patch_format
description: Enforce patch spec strictly; cross-check handoff expectations against actual patch data
type: feedback
---

When Claude AI sends patches that deviate from the v5.1/v5.2 spec, do NOT update the applicator to accommodate the error. Let it fail so Claude AI corrects the format.

Also: when Claude AI provides a handoff validation block with expected counts, cross-check those expectations against the actual patch operations — the patch data is authoritative, not the handoff summary text. Report discrepancies rather than silently adjusting.

**Why:** (1) Researcher caught that accommodating Claude AI's format error would mask the problem. The spec is authoritative. (2) Claude AI handoff text contained a count error (said 22, patch had 23). Catching this avoids false validation failures and builds trust in the verification process.

**How to apply:** When a patch fails validation or format mismatch, report the specific deviation. When validating results, always check against the patch file itself first, then compare to handoff expectations. If they differ, report the discrepancy clearly.
