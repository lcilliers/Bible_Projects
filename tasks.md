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

### VC four-output model + A-02..A-05 resolution (2026-04-24)

- [ ] _VC-7 Pilot: one small term on renewal (reg 134) under the per-term model; then full renewal in per-term mode; then programme-wide roll-out to the 180 registries at `Verse Context Reset`. Under v3_4 the patch submitted must declare `_patch_meta.input_versions[mti_term_id] = md_version` matching the per-term .md the session classified against; applicator will reject on stale mismatch._

### Other open

- [ ] _Global_Rule: update OBS to set default reference _
- [ ] _Glbal_Rule: _resolve issue that obslog is not consistently complied with on start of new session.
- [ ] _Claude_Code_Rules:  _all outputs that is regularly produced or updated to carry version [major].[minor] both in file name and internal meta_
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

### VC per-term rollout (approved 2026-04-24 — 4 decision gates passed, see [alignment analysis v4 §8](outputs/investigations/vc-instruction-session-a-md-alignment-v4-20260424.md))

- [x] _VC-1 M37 migration: mti_terms.vc_status + companion fields. Schema 3.14.0 → 3.15.0. Commit `5368b22`._
- [x] _VC-2 Applicator: VC-2 helper per-term validation + registry aggregation. Commit `7955b01`._
- [x] _VC-3 Patch meta: _patch_meta.terms_covered required for VC patches. Commit `7955b01`._
- [x] _VC-4 Instruction v3_1: per-OWNER-term primary input; §0.1 / §5 / §6.1 / §7.2 / §13 updated. Commit `e490931`._
- [x] _VC-5 Renderer: --term mode in build_session_a_prose.py; pilot on renewal. Commit `8cc71f3`._
- [x] _VC-6 Prose: prog_instr_session_a v2 → v3 supersede. Commit `07b1677`._

### VC four-patch output model (A-01 resolved, 2026-04-24 — see [four-patch design brief](outputs/investigations/vc-four-patch-design-v1-20260424.md))

- [x] _Patch-type registry: seed VCNEW, VCREVISE, VCSBFLAGS, VCSDPOINTERS in wa_patch_type_registry. Commit `51622d4`._
- [x] _Patch instruction v2_4 → v2_5: add 4 new rows to §3.3/§3.4/§3.6; new §15 VC Session Four-Patch Catalogue. Commit `51622d4`._
- [x] _Applicator extension: sb_exempt_types + VC-2 handler + terms_covered validation widened to VCNEW + VCREVISE. Commit `51622d4`._
- [x] _VC instruction v3_2 → v3_3: new §7.9 four-patch model; §6.2 Step 6 SB/SD routing; §6.6 sessionb-flags.md demoted to companion; §13.3 A-01 resolved (DB state is the gate). Commit `156dcbd`._
- [x] _Prose: prog_instr_verse_context v2 → v3 supersede — describes four output classes in governance narrative. Commit `f27972c`._

### VC A-02 / A-03 / A-04 / A-05 resolution (2026-04-24 — see [ambiguities doc](outputs/investigations/vc-v3_1-ambiguities-needing-researcher-decision-v1-20260424.md))

- [x] _A-02 vc_status vocab simplified: approved dropped; complete renamed vc_completed. M38 migration; applicator writes vc_completed; aggregation queries updated. Commit `d50061f`._
- [x] _A-03 per-term .md freshness version-gated: mti_terms.md_version column; .md header carries md_version; patch _patch_meta.input_versions map required for VCNEW/VCREVISE; applicator rejects stale mismatches and bumps on apply. Commit `d50061f`._
- [x] _A-04 session identifier optional: batch_id no longer operationally required. Per-term version gate is the correlation. Commit `d50061f`._
- [x] _A-05 cross-term duplicate classifications: not a VC concern — handled at Session B. No instruction change required. Noted in v3_4 change note._
- [x] _VC instruction v3_3 → v3_4: change-note documents A-02/A-03/A-04/A-05 resolutions; §0.1 / §6.1 / §7.2 / §13 updated. Commit `d50061f`._
- [x] _Patch instruction v2_5 → v2_6: §15 VCNEW/VCREVISE/VCSBFLAGS/VCSDPOINTERS updated with input_versions field; batch_id marked optional; self-check extended. This commit._
- [x] _Ambiguities doc updated with resolution status table. This commit._

---

*Created 2026-04-22.*
