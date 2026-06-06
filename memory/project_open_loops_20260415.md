---
name: Open Loops — tracked items
description: Tracked items from flag remediation and instruction updates. Loop 1 closed, Loop 2 closed. Three applicator gaps remain.
type: project
originSessionId: c3605270-8f61-403f-810d-6d16c981d180
---
## 1. apply_session_patch.py — CLOSED 2026-04-16

Applicator updated to v20260416. All 20 findings fields, supersede_finding, insert_finding_entity_link, catalogue tables supported.

## 2. Session B instruction flush-through — CLOSED 2026-04-18

Major instruction restructure landed 2026-04-18. 13 documents refreshed/new. CC instruction renamed to wa-claudecode-instruction-v4_1. Patch spec renamed to wa-patch-instruction-v2_1. CLAUDE.md fully updated to match.

## 3. Applicator gaps (from wa-patch-instruction v2.1 §7.2)

**Status:** Open — not yet blocking but will be needed.

Three operations not yet supported in apply_session_patch.py:

1. `update` on `wa_session_research_flags` — needed for flag resolution
2. `insert` on `wa_dimension_index` — needed for new dimension entries
3. `SDPOINTERS` exempt patch type — needed for standalone SD pointer patches
