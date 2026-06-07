# cluster_observation resolution — M5 / M10 / M10b — 2026-05-27

**Trigger:** researcher review of cluster_observation state. M10 had 155 open rows, M10b had 67 open, M5 had 1 open — unexpected backlog.

## Investigation

Open rows split into two distinct categories:

| Category | Status `open` is | Action |
|---|---|---|
| Session-C / Session-D targeted carry-forwards | **Designed behavior** — the row is queued for the next session level to consume | Annotate `resolution_note` to make the intent self-documenting; leave `status='open'` |
| Phase-8.5 / Phase-9 targeted rows that target ran | **Stuck** — target phase ran but status never advanced | Advance `status='open'` → `'confirmed'` with a resolution_note recording when/why |

## Changes applied

### 15 rows advanced to `confirmed` (M10 only)

- 6 INTEGRATION_NOTE rows with `target_phase='phase_8_5_boundary_resolution'` (Phase 3 BOUNDARY parking notes — Phase 8.5 ran and resolved 322 BOUNDARY verses)
- 9 INTEGRATION_NOTE rows with `target_phase='phase_9_findings'` (Phase 8.5 closure notes + 7 INTER_RELATIONSHIP cross-register pointers — Phase 9 authored 4,158 findings)

Resolution note pattern:
> *"Target phase (Phase 8.5 BOUNDARY resolution) ran for this cluster. Auto-advanced to confirmed 2026-05-27T07:41:02Z per researcher review 2026-05-27."*

### 207 rows annotated (open by design)

206 Session-C-targeted rows (M10: 139, M10b: 67) + 1 Session-D-targeted row (M10) — all received an explicit resolution_note so future analysts immediately see the open status is intentional, not a forgotten-to-resolve:

> *"Open by design — carry-forward awaiting Session C consumption. Status will advance to confirmed/refined when Session C addresses this observation in its narrative."*

### M05 retrofit observation annotated (1 row, id=15)

Records the M07 → M05 term transfer (H2616B cha.sad + H2617B che.sed transferred 2026-05-19). With M05 now `Ready for re-analysis` (2026-05-27), this observation is the pointer for the retrofit. Resolution note:

> *"Open by design — carry-forward awaiting M05 re-analysis (cluster.status='Ready for re-analysis' as of 2026-05-27). The two terms added post-closure (H2616B cha.sad + H2617B che.sed) will be incorporated when the cluster is re-processed."*

## Post-state

| Cluster | confirmed | open | open target phases |
|---|---:|---:|---|
| M05 | 0 | 1 | m05_retrofit (M05 re-analysis pointer) |
| M10 | 15 | 140 | session_c (139) + session_d (1) |
| M10b | 3 | 67 | session_c (67) |

**Total open rows across the three clusters: 208.** All have explicit `resolution_note` documenting their carry-forward status. No "stuck" observations remain.

## Programme-wide implication

The cluster_observation lifecycle (`open → confirmed/refined`) should be enforced at each phase's exit, not aspirational. Two patterns to standardize in v3_0:

1. **Same-phase observations** (target_phase = current phase): must advance to `confirmed`/`refined` before phase exits. Phase 12 closure should verify this — no observations targeted at completed phases may remain `open`.
2. **Forward-targeted observations** (target_phase = later phase / session): SHALL remain `open` with a populated `resolution_note` explaining the carry-forward intent. The `open` state is meaningful, not a defect.

This avoids the M10/M10b drift: the 15 stuck rows happened because Phase 8.5 and Phase 9 ran without an exit check that advanced their targeted observations.

---

*Resolution v1 — 2026-05-27. No further open observations are "stuck" in M5/M10/M10b.*
