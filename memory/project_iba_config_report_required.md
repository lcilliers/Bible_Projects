---
name: project_iba_config_report_required
description: IBA app must auto-generate a full human-readable config report after every config change.
metadata: 
  node_type: memory
  type: project
  originSessionId: 7a3d6e48-d97f-407e-83ba-ecef211af3af
---

**Next task for the IBA app (directed 2026-07-18):** build a proper **configuration report** so
the researcher has **full visibility of ALL configurations**, and **regenerate it automatically
after each change** (every accepted `cfgload`).

- Read every `cfg_*` table from `iba/app/db/iba.db` and render a complete, readable **markdown**
  snapshot: connection, settings, apis, work-package steps, on_fail rules, write grants, status
  flow, schema tables/columns, enums, book order, and the `cfg_change_log` audit trail.
- Hook it into `cfgload.load()` so it is produced on every accepted load (the "after each change"
  trigger); overwrite the snapshot file in place (a live generated artefact, not a versioned
  deliverable). Spec: `iba/app/docs/cfg-report-spec-v1-20260718.md`.

**Why:** the researcher cannot see what the DB-held config actually contains without querying;
after a burn-heavy session with little to show, they want durable, self-updating visibility.
Reinforces [[feedback_all_study_work_in_db]] and [[feedback_source_of_truth_is_written_record]].

**How to apply:** build it first thing next session (it is a local read-only generator — running
it costs no AI allowance). Keep it simple per [[feedback_simple_steps_not_engineered_designs]].
Also economise the session itself: batch verification runs, read narrow file slices, avoid
re-verifying — see [[feedback_copilot_frustration]].
