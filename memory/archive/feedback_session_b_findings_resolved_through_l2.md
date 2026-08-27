---
name: feedback_session_b_findings_resolved_through_l2
description: Rule (2026-06-09). ALL Session B findings (wa_session_b_findings) must be RESOLVED by a finding. If a SB finding already has a finding reference -> it is CLOSED (only the related finding counts). If it is verse-anchored and has NO resolving finding -> it is part of the L2 stage and must be resolved/updated as its anchor verses are covered. Scope: 8 already-referenced (close); 1432 verse-anchored-unresolved (L2 work items); rest non-verse-anchored. SB findings are multi-verse-anchored -> needs a finding<->verse link table.
metadata:
  type: feedback
---

**Researcher rule (2026-06-09):** **all Session B findings must be resolved by a finding** (the new
universal `finding` model). Integration into the L2 verse-coverage stage:
- **SB finding already has a finding reference → CLOSED.** Only the related (new) finding is taken into
  account.
- **SB finding verse-anchored AND no resolving finding → part of THIS process** — resolved/updated during
  L2, as its anchor verses are covered.

**Scope (2026-06-09 counts, `wa_session_b_findings`, active 2883):** **8** have `related_finding_id` → close;
**1432** are verse-anchored (`anchor_verses` set) with `related_finding_id` NULL → **L2 work items**; the rest
(~1443, mostly `resolved_qa`, registry-level) are not part of the *verse* process. SB findings are
**multi-verse-anchored** (`anchor_verses` is a list) — they are higher-level (TERM/CLUSTER) observations over
many verses.

**Schema implication ([[feedback_all_study_work_in_db]], schema design v2):** SB findings migrate into the
universal `finding` model as **TERM/CLUSTER-level findings**, status **OPEN** (the 1432 unresolved) or
**RESOLVED/CLOSED** (the 8 referenced); their anchor verses populate a **`finding_verse_link`** M:N table so
**verse-coverage can surface the open SB findings anchored to the current verse and resolve them** (linking
via `justified_by_finding_id` / `supersedes_id`). The verse-read that resolves one closes the SB finding.
`cluster_finding` (19,996, cluster roll-up) is a separate, later reconciliation. Detail:
`research/investigations/wa-l2-finding-schema-design-v2-20260609.md`.
