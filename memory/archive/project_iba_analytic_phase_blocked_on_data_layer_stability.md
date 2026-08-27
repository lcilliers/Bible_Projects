---
name: project_iba_analytic_phase_blocked_on_data_layer_stability
description: "IBA app build sequencing: the researcher concluded (2026-07-21) that analytic-phase config gaps (e.g. span_candidate tagging) cannot be usefully resolved until the data layer is stable — paused analysis, returned to core data-layer build/fix."
metadata: 
  node_type: memory
  type: project
  originSessionId: 17d30e5a-09c0-4950-83c7-4ab98c83ccd4
  modified: 2026-07-21T12:51:12.442Z
---

On 2026-07-21 the researcher began analysing `outputs/csv/span_candidate-iba-20260721.csv` (spot-checking
candidate seeding output) and hit a concrete data gap: 281/489 `ib-judgement`-layer candidates have a
blank tag, traced to `iba/app/config/cfg_candidate_rule.csv` (the accept-list seed for
`iba/app/db/iba.db.cfg_candidate_rule`) having no column to carry a tag alongside an accept decision —
see [[reference_iba_live_config_is_db_resident]].

Their conclusion from this exchange: **questions/issues surfaced during analytic-phase work on the IBA app
cannot be resolved until the data layer underneath it is stable.** They are pausing this analysis thread
and going back to the previous session to continue building/fixing the core (data layer), rather than
chasing config gaps discovered from the analysis side.

**Why:** Analytic-phase findings (missing tags, blank fields) keep tracing back to structural gaps in the
still-being-built data/config layer — fixing them one discovery at a time from the analysis side is
premature when the layer itself isn't finished.

**How to apply:** Don't propose analytic-phase config fixes (candidate tagging, seed rules, etc.) as
live work until the researcher signals the data layer is stable again. If asked to analyse IBA app output
and a data/config gap surfaces, it's fine to trace and report it precisely (per
[[feedback_iba_no_synthesis_small_units_only]]) — but expect the response to be "note it, don't fix it,
we're not there yet" rather than a request to act.
