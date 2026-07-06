---
name: feedback_no_patch_to_nice_pointintime_result
description: "GOVERNING (2026-06-15) - the DB/scripts are fragile because of quick fixes/patch-over to reach a 'nice' result at a point in time; build foundationally, not to a momentary appearance"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 8a5e10ea-2d9d-4bb9-8ca3-fb979500309e
---

GOVERNING (2026-06-15): the researcher's diagnosis of why the database and scripts are fragile — *"all due to quick fixes and patch over to arrive at an unfounded 'nice' result at a point in time."* Examples uncovered in one session: `language` derived from the Strong's prefix (Aramaic-blind); `morph_code` populated only by a side backfill, never at verse creation; **`wa_verse_records.mti_term_id` written by NO maintained code at all** — so processed words (R213 'listen', Complete) sit unlinked; excluded registries (42) left with live downstream rows instead of soft-deleted.

**Why:** a fix that makes the current view look right but doesn't populate/maintain the downstream values leaves latent breakage that surfaces later as "inconsistency."

**How to apply:**
- Fix the DERIVATION at its source, never the symptom ([[project_morph_is_source_of_truth]], [[feedback_check_governance_layers_not_just_pipeline]]). morph is the source; stem/language/mode/link all derive and must be maintained wherever the source changes.
- A general-use script/routine MUST leave every downstream value correct (link, morph, stem, language) — not defer them to a remembered side-step.
- When something looks inconsistent, trace it to the create/derive routine and fix it there + a one-time backfill; surface the systemic cause, don't quietly patch the one row.
- Prefer reversible, verified operations over a quick result.
