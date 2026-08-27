---
name: feedback_iba_config_first_not_doc_archaeology
description: IBA app work must start at cfg_work_package/cfg_step/cfg_setting to find the registered routine and its config-resolved inputs — never start by reading old instruction docs or prior output files and inferring process from them.
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 9999a431-8c24-4b9f-80e5-21dbc8953d5a
  modified: 2026-07-27T06:16:54.968Z
---

For any IBA app task, the entry point is the config layer — query `cfg_work_package` /
`cfg_step` for the registered routine (handler, ps_script, scope), then `cfg_setting` for the
values that routine reads (e.g. `method.passage_read_guidance_path`,
`method.interpretation_questions_path`, `report.passage_debate_naming_pattern`). Only once the
config has named the actual routine and its inputs is it correct to open the docs/files it
points to.

**What went wrong (2026-07-27):** asked to "re-run" the Dan 3:1-7 passage debate, went straight to
reading the existing scaffold file's citation line, the referenced method/interrogative docs, and
a prior completed debate (Dan 2:31-49) to copy its style/format — then hand-authored the full
debate content and overwrote the file. Never queried `cfg_work_package`/`cfg_step` to find that
this is the `passage-debate-report` work package (`report.passage_debate` step, handler
`iba.app.handlers.reports:passage_debate_report`) before doing any of that. The researcher's
correction: "you did not build this process into the configs... If you have built this into the
app and followed the app governance, you would have gone straight to the configs to get the
routines that run, and from the routines would have gone to the configs, and then would know what
you need to do." This is precisely the failure mode [[feedback_iba_fixes_are_config_and_registered_utilities_not_code_patches]]
and [[feedback_iba_gap_analysis_requires_live_build_inspection]] already warn about, applied here
to a different kind of task (content authoring, not a fix/gap-check) — the same discipline holds:
config names the routine, the routine is authoritative, docs are only consulted once the config
has pointed at them.

**Note on what the config actually showed, checked after the fact:** the registered
`report.passage_debate` step explicitly does **not** generate interpretive content — it only
verifies the base extract + current method-doc settings exist and writes a placeholder skeleton;
filling the skeleton in is left to "the researcher/AI." So content-authoring itself isn't a
config-automatable step here. But the *method doc paths* and the *output filename pattern* (no
`-vN-`/date in the name; reportkit archives the prior version on regenerate) are both config
settings (`method.passage_read_guidance_path`, `method.interpretation_questions_path`,
`report.passage_debate_naming_pattern`) — they must be read from `cfg_setting`, not assumed
correct because a scaffold file or a sibling debate happened to cite them.

**Why:** the whole IBA governance model is config-as-master ([[project_iba_db_is_master_over_legacy_json_seeds]]) —
docs restate what config already governs, they are not themselves the source. Inferring "what to
do" from a doc trail or from what was done last time silently reintroduces exactly the
doc-vs-config drift the governance layer exists to prevent (cf. `governance.rules_must_be_config_driven`:
"no operational or process rule may exist only in GOVERNANCE.md/BUILD.md/... without a backing
cfg_* row").

**How to apply:** before starting ANY IBA task — fix, report, content-authoring, whatever —
query `cfg_work_package` and `cfg_step` first for a matching routine/handler; if one exists, run
it or read its handler to see what it actually does and what `cfg_setting` rows it consults.
Only fall back to reading docs/prior output directly when config confirms there is no registered
routine, or (as here) the routine itself defers the remaining work to the researcher/AI — and even
then, pull the specific setting rows (method paths, naming patterns, thresholds) from
`cfg_setting` rather than trusting whatever a file happens to cite.
