---
name: project-v3_0-active
description: "v3_0 is the active Session B cluster instruction as of 2026-05-27. Six phases (A-F). v2_9 superseded. Test cluster: M11 un-park."
metadata: 
  node_type: memory
  type: project
  originSessionId: 7401fa55-df1f-434c-9ff3-b60b0138422f
---

**Status as of 2026-05-27:** `wa-sessionb-cluster-instruction-v3_0-20260527.md` is the active cluster instruction. v2_9 superseded.

**Six-phase structure:**

| Phase | Owner | Purpose |
|---|---|---|
| A | CC API | Read + meaning (UT + Pass A, single API pass) |
| B | AI (3 sessions) | Meaning grouping (B.1 constitution, B.2 sub-groups, B.3 VCGs) |
| C | CC | Structural cleanup (single apply: term transfers, sub-groups, VCGs, characteristics) |
| D | AI (N+1) | Analytics findings (per-char + cluster synthesis) — **NO embedded prose** |
| E | AI (N+1) | Publication prose (per-char tier prose + cluster synthesis prose) — **separate, re-runnable, backfillable** |
| F | CC | Validation + closure (single op) |

Plus §11 publication pipeline = CC assembly from `prose_section`. Session C as AI session is **retired**.

**Two governing principles codified at top of doc:**
- GP-1: verse meaning rules all analytics
- GP-2: all observations recorded, no bias-screening

**Status path:** `Not started` → `Data - In Progress` → `Structurally Ready` → `Analysis - In Progress` → `Analysis Complete` → `Publication Ready` → `Closed`.

**Phase B internal structure** (the key design decision raised 2026-05-27): three AI sessions with CC stage gates between them, NOT one undifferentiated session. Each stage carries the v2_9 disciplines (B.1: §6.3.1+§6.3.2; B.2: §8.4.1+§8.6 40% gate; B.3: §10.7 staged write-out + §10.8 no-sampling). The v3_0 saving over v2_9 is structural (one Phase C apply, shared input scaffolding) not session-count (3 sessions in both).

**Cycle reductions vs v2_9 (N=7 cluster):**
- CC mechanical ops: 8 → 4 (-50%)
- Verse-corpus AI reads: ~18 → ~9 (-50%) — the headline win
- Session C AI sessions: 8 → 0-1 (-88% to -100%)
- AI session count for grouping work: 3 → 3 (unchanged; the v3_0 contribution is structural cleanliness)

**Supporting design docs (sibling files):**
- [[wa-v3_0-phase-b-control-design]] (file: `Workflow/Instructions/wa-v3_0-phase-b-control-design-v1-20260527.md`) — Phase B internal staging rationale
- [[wa-v2_9-vs-v3_0-cycle-comparison]] (file: `Workflow/Instructions/wa-v2_9-vs-v3_0-cycle-comparison-v1-20260527.md`) — cycle quantification with corrigendum

**Outstanding for v3_0 readiness:**
1. **Test cluster** — M11 un-park is the planned test. M11 was parked 2026-05-26 after Phase 3 surfaced characteristic-legs-elsewhere diagnosis (only 103/421 forgive-text verses in M11). v3_0 first run will validate Phase B → Phase F.
2. **Phase 9 batch builder extension** — current builders need Phase E counterparts (the per-char tier-prose builder + cluster-synthesis prose builder). Not blocking M11 if findings-only Phase D first; Phase E builders can come after.
3. **Phase B / C / F validators** — `_validate_cluster_phase_b1/b2/b3_*.py` and `_validate_cluster_closure_*.py` referenced in v3_0. Build as needed during M11 run.
4. **`_apply_phase_d_*` / `_apply_phase_e_prose_*` loaders** — extend existing v2_9 loaders or write fresh.

**Pre-v3_0 closed clusters (M01, M02, M03, M05, M06, M15, M20, M26, M39, M46):**
- Characteristic backfill done 2026-05-27 (see [[project-characteristic-backfill-backlog]]).
- Phase E prose backfill deferred until each cluster is scheduled for publication (per §9.7 + §12 of v3_0).
- M01, M03, M09, M15 have chapter drafts already in `prose_section` as `sc_v2_ch{N}` rows — assembler handles them directly without per-tier reconstruction.
