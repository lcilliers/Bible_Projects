# Tasks

Lightweight task ledger for the Bible_study_projects repo. Check off items as they complete.

**Usage**
- `- [ ]` = open
- `- [x]` = done
- Group under the headings below; move items between sections as status changes.
- For anything with real analytical weight (investigations, design decisions), link to the underlying `.md` in `outputs/investigations/` or `Logs/` rather than duplicating the content here.

---

## In Progress

- [ ] _Enrich programme prose with the inputs and outcomes of methodology review sessions
- [ ] _Phase_A_Prose: generate phase A prose_
- [ ] _Phase_B_Verse_Context: Run through all verse context again_  

## Open

### VC per-term rollout (approved 2026-04-24 — 4 decision gates passed, see [alignment analysis v4 §8](outputs/investigations/vc-instruction-session-a-md-alignment-v4-20260424.md))

- [ ] _VC-1 Schema: M32 migration — add `vc_status`, `vc_instruction_version`, `vc_status_updated_at`, `vc_status_note` to `mti_terms` (controlled vocab: `not_done | to_revise | complete | approved`); backfill all rows to `not_done`; flag the 6 explicitly-reset registries' terms (compassion 23, fellowship 62, forgiveness 64, grace 68, love 103, mercy 111) as `to_revise`_
- [ ] _VC-2 Applicator: extend `scripts/apply_session_patch.py` VERSECONTEXT path — per-term R1-R4 + orphan-group + coverage validation → set `mti_terms.vc_status='complete'` + `vc_instruction_version` + `vc_status_updated_at`; derive affected registries (OWNER + XREF-via-OWNER); aggregate check; if all complete, set `word_registry.verse_context_status='Complete'` + trigger re-export_
- [ ] _VC-3 Patch format: add required `_patch_meta.terms_covered` array to VERSECONTEXT patches; applicator cross-checks against operated-on `mti_term_id`s_
- [ ] _VC-4 VC instruction v3_1: light supersede of v3_0 — §0.1 primary input is per-term `.md`; §5 input preparation per term; §6.1 posture per term; processing order = session-assembly order; §7.2 `terms_covered` required; §13 registry completion as CC-side derived aggregation; Annexure C legacy batch JSON noted as deprecated_
- [ ] _VC-5 Session A renderer: add `--term=<mti_term_id>` mode to `scripts/build_session_a_prose.py`; output `data/exports/session_a/terms/wa-{NNN}-{word}-{strongs}-session_a-{YYYYMMDD}.md`; retain `--registry` for hybrid per-registry view_
- [ ] _VC-6 Programme prose: supersede `prog_instr_session_a` v2 → v3 — one-paragraph clarification that the renderer can produce per-term (primary) or per-registry (hybrid) views from the same data; note the per-term as default VC input_
- [ ] _VC-7 Pilot: one small term on renewal (reg 134) under the per-term model; then full renewal in per-term mode; then programme-wide roll-out to the 180 registries at `Verse Context Reset`_

### Other open

- [ ] _Global_Rule: update OBS to set default reference _
- [ ] _Global_Rule: list memory and project files on start_up_
- [ ] _VS_Code: automate commit-push_
- [ ] _VS_code: reset folder destinations for prose and references_
- [ ] _Word_data: Archive after Phase A prose is done.
- [ ] _Phase_B_Dimensions: Revisit all dimensions not yet through second round_
- [ ] _Phase_B_Analysis_Readiness: Run all words through readiness_
- [ ] _Phase_B_Prose:  Prepare prose ready for analysis_
- [ ] _Phase_B_Output:  Prepare output and update database for all words.
- [ ] 


## Done

- [x] _Workflow: create tasks.md at repo root_
- [x] _Programme_prose: create prose for programme chapters _

---

*Created 2026-04-22.*
