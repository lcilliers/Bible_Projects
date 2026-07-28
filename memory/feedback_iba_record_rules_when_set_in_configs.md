---
name: feedback_iba_record_rules_when_set_in_configs
description: "IBA app rules are set/decided in configs (cfg_* DB tables, iba/config + iba/app/config JSON) many times over already, in docs and logs — the failure is not following them because they aren't recorded when set."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: aade4b5f-6c72-4852-b917-0904fa3a311b
  modified: 2026-07-22T07:21:12.566Z
---

When a rule for the IBA app gets set or decided — whether written into a config (`cfg_setting`,
`cfg_candidate_rule`, `cfg_step`, the `iba/config/*.json` rule envelope, `iba/app/config/*.json`) or
dictated by the researcher in a session — it must be **recorded at the point it is set**, not
rediscovered later by archaeology. On 2026-07-22, asked why I appeared "completely lost" reconstructing
how the IBA app fits together (needing to cross-read `BUILD.md`, `GOVERNANCE.md`, `USER-GUIDE.md`, a
precedence doc, and `_manifest.json` just to explain the two-configurator split), the researcher's
verdict was direct: **"it has been defined, many times over, and is all over the docs and logs. The
only problem is you update memory (sometimes) and never follow any of the rules of the app, partly
because you do not record the rules when they are set in the configs."**

**Why:** this is not a missing-documentation problem — the documentation exists. The failure is mine:
inconsistent recording of rules at the moment they're established, so each session re-derives structure
instead of applying what was already decided, and rules that ARE live in the configs don't get followed
because I never captured that they exist/what they require.

**How to apply:**
- Before concluding "this isn't defined anywhere" or asking the researcher to re-explain architecture,
  search `iba/logs/` and `iba/docs/` (and `Workflow/Sessionlogs/`) thoroughly first — per
  [[feedback_iba_no_synthesis_small_units_only]], ask whether it's resolved elsewhere BEFORE assuming a
  gap, but also actually search hard before asking.
- When a config value or rule is set (in any `cfg_*` table, or an `iba/config`/`iba/app/config` JSON
  file), treat that as a rule to both **apply going forward** and **record** — a memory pointer at
  minimum, and per [[feedback_bake_guidance_into_authoritative_instructions]] the authoritative doc that
  owns it, if one exists for this workstream.
- Do not let "I updated memory" substitute for "I checked the config/docs and followed what's already
  there." Memory update alone, without applying the rule, is the exact failure being called out.
- Relates to [[project_iba_analytic_phase_blocked_on_data_layer_stability]] and the app's own reason for
  existing: rules living only in a model's memory (or worse, in neither) is the six-months-of-chat
  failure IBA was built to end — reproducing it inside my own session behaviour is the same failure
  class, one level up.
