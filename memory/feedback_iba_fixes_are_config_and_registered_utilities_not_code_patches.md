---
name: feedback_iba_fixes_are_config_and_registered_utilities_not_code_patches
description: "IBA app \"gap fixes\" are almost all missing/stale config content or missing utilities that must be registered as a work_package/step in cfg_step (with their own config), not ad hoc code patches — triage every gap into that framework before proposing anything."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 7608c281-70c1-41bb-8181-d9ebf468771f
  modified: 2026-07-21T13:46:29.631Z
---

The researcher's correction on a 2026-07-21 gap-fix list: *"80% of the items you are showing as fixes
are entries in the config files of the apps that will then be used to design the associated code to
apply the config to prevent the issue... very few of the fixes are straight fixes in the code. And the
rules already state that everything should be driven through the methods and utilities, which should
all be registered in the run table. This whole design is completely not achievable in the way you are
approaching it."*

**Why:** the app's architecture (`GOVERNANCE.md` rules c/d/e, `iba-application-design-v2` §0) is: every
rule lives in `cfg_*` config; every operating module has its own config; every method/utility runs
through the `run.py` dispatcher via steps registered in `cfg_work_package`/`cfg_step` (the "run table")
— never as an ad hoc script or an inline code patch bolted onto a handler. Treating a "gap" as "go
write/patch code" skips this entirely. Confirmed by direct inspection (2026-07-21): even
`configuration_maintenance` itself — `cfgload.py`/`cfgcheck.py`/`cfgreport.py` — is **not** registered
as a work package/step; it's invoked as standalone scripts outside `run.py`'s dispatcher (legitimately,
for the bootstrap load, since it can't read its own config before the config store exists — but its
ongoing validate/report/reconcile operations could and should be registered once bootstrap is done).

**The triage, every time, before proposing anything:**
1. **Genuine code defect** (rare) — e.g. a stale file path, an import that doesn't resolve. A direct
   code fix is fine.
2. **Missing or stale config content, applied by already-generic code** — e.g. `passage.*` settings,
   `cfg_candidate_rule`'s `reject`/`synonym` lists. No code change at all — author/correct the config
   row(s); the handler already reads them generically.
3. **Missing capability** — a check, report, or process that doesn't exist as a registered step yet
   (e.g. a naming-collision checker, an automatic config-report trigger). This must be **designed as a
   new registered utility/work-package/step with its own config** (rule e), then populated — never
   written as bespoke logic living outside that registration.

**How to apply:** for any future "list the gaps" / "fix this" task on the IBA app, sort every item into
these three buckets explicitly before proposing action, and say which bucket each falls in. Bucket 1 is
usually small; expect most items to land in 2 or 3. For bucket 3 items, the deliverable is a
work-package/step design + its config shape, not code. Related: [[feedback_iba_gap_analysis_requires_live_build_inspection]],
[[feedback_simple_steps_not_engineered_designs]].
