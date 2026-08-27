---
name: C01 DimReview post-patch plan (2026-04-20)
description: Forward plan — when Claude AI's C01 Phase B/C DIMREVIEW patches arrive, CC runs FF-1..FF-10 checks, folds learnings into DV-6..DV-8 pre-checks, presents Option 1/2/3 decision for full C01 realignment
type: project
originSessionId: 62ef2dc4-cbcd-4fc0-9a07-8c2ace3bedec
---
**Pending work triggered 2026-04-20 evening:** Researcher about to hand CC the full C01 dimension analysis from Claude AI including DIMREVIEW patches for r112 mind and r183 heart.

**CC actions when patches arrive** (full detail in `outputs/investigations/dim-c01-post-patch-plan-20260420.md`):

1. Pre-apply validation + per-patch backup
2. Apply DIMREVIEW patch(es) via `scripts/apply_session_patch.py`
3. Run **FF-1..FF-10 free-flight checks** post-apply — produces `outputs/reports/wa-dim-C01-post-apply-verification-20260420.md`
4. Fold learnings into pre-handoff pipeline (DV-6+ pre-checks for next DimReview bundle)
5. Update OT-DBR-015 (vocabulary vintage) with post-apply state — r112+r183 now on current vocab; 4 of 6 C01 still legacy

**Outstanding researcher decision after patch applies:**

Should C01 be fully realigned under current §7.7 vocabulary? Three options (§3 of plan doc):
- Option 1: Accept mixed-vintage (4 legacy + 2 current in C01). Not recommended.
- Option 2: Full re-review of r182/r184/r185/r211 under current vocabulary. Thorough but expensive.
- **Option 3 (CC recommendation): Mapping patch + researcher review of 40 unmapped-legacy-label groups.** Mechanical migration per OT-DBR-015 mapping table; researcher decides on Spiritual/God-ward (25), Identity/Selfhood (9), Somatic/Embodied (6) only.

**Keep in mind:**
- OT-DBR-015 (vocabulary vintage — likely programme-wide, not just C01)
- OT-DBR-016 (rootfamily over-reports cross-registry roots)
- `build_dimension_extract.py --bundle` now produces standard handoff with DV-1..DV-5 pre-checks + --override block
- DimReview instruction §2.2 Registry Mode full-cluster rule — override formalism now in place
- GR-LOAD-001 flags-file load discipline
- Session A generator inlines Q-COV questions beneath evidence flags (post-M29 enhancement)
