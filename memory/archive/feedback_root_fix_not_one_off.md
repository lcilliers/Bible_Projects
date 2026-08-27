---
name: feedback_root_fix_not_one_off
description: Fix the cause not the instance; one-off/per-case patches are rarely appropriate and NEVER when the problem may recur.
metadata:
  type: feedback
---

**Fix the root cause, not the instance.** A one-off / per-term / per-book / per-file patch is **rarely appropriate, and NEVER appropriate when the problem may recur** (researcher, 2026-07-13). When a defect is an instance of a class — a shared method, extractor, or pipeline step is wrong — fix it at the **shared mechanism** so every future case is correct, rather than remediating case-by-case and leaving the mechanism broken.

**Why:** a case-by-case remediation leaves the bug live for the next book/term; the same failure recurs and re-costs. The double-control (e.g. morphology vs verse-records) will keep surfacing it, but only a root fix stops it.

**How to apply:** when you catch yourself hand-patching one case (constructing a corrected extract for one term, editing one record), STOP and ask "is this an instance of a class?" If yes, fix the mechanism. **Worked example:** the STEP multi-variant verse drop (`_resolved_strong` collapsing a Strong's to `vocabInfos[0]`, dropping sibling codes' verses) was fixed in the shared extractor `word_study_extract.fetch_verses` (union the morphology-attested variants), NOT patched per Proverbs term. Baked into `wa-term-add-update-AUTHORITATIVE-pipeline-v1` (Governance + STEP-2 amendment) and `docs/interaction-preferences.md`. Relates to [[feedback_bake_guidance_into_authoritative_instructions]], [[feedback_reusable_engine_scripts_and_continuous_learning]], [[feedback_no_rework_paid_twice]].
