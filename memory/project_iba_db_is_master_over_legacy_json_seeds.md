---
name: project_iba_db_is_master_over_legacy_json_seeds
description: "IBA app — the live DB (cfg_* config AND candidate_seed/lemma_inventory) is master; old JSON/file seed sources are historical, substantially reworked already, and are a one-time completeness reference only, never a reload source."
metadata: 
  node_type: memory
  type: project
  originSessionId: 7608c281-70c1-41bb-8181-d9ebf468771f
  modified: 2026-07-21T14:02:49.499Z
---

Researcher ruling (2026-07-21), applying to **both** the app-config store (`cfg_*`) and the
candidate/characteristic seed (`candidate_seed`/`lemma_inventory`): the **live DB content is master**,
not the old JSON-based sources. The archived app-config JSONs (`iba/app/config/archive/*.json`, moved
there 2026-07-19 by commit `216314b9`) and the old-study candidate/lemma files `import_seed.py` reads
(`research/discovery/lemma-inventory-master-*.json`, `ib-judgement-rejected-*.md`, read-emergent
extension files) are historical inputs, substantially reworked in producing the current DB content —
in the researcher's words, they "potentially have a lot of noise, and issues, and must not be included
or used in the app." Their only legitimate ongoing role is a **one-time cross-check**: does the DB
already have everything relevant that these files once held — never "reload from them."

**Why:** the DB reflects curation/rework beyond what any one JSON snapshot captured. Treating a JSON
file as the authoritative reload source (which `cfgload.py`/`cfgcheck.py` literally do as written today)
risks silently overwriting or reverting that rework the moment someone reloads — this is exactly what
produced the stale 289-row `cfg_candidate_rule` finding on 2026-07-21 (the live table didn't match the
now-empty archived seed, and the archived seed is not to be treated as correcting the DB).

**How to apply:** never propose "reload/reconcile from the archived/old JSON" as a fix for DB content
that looks stale or wrong. Treat the live DB as ground truth. Use the old files only as a manual
completeness check (does the JSON name anything not present in the DB that's still relevant) — surface
that as a question to the researcher, never auto-apply it. Related:
[[feedback_iba_config_changes_require_researcher_approval_never_silent]],
[[feedback_iba_gap_analysis_requires_live_build_inspection]].
