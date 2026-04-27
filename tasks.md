# Tasks

Lightweight task ledger for the Bible_study_projects repo. Check off items as they complete.

**Usage**
- `- [ ]` = open
- `- [x]` = done
- Group under the headings below; move items between sections as status changes.
- For anything with real analytical weight (investigations, design decisions), link to the underlying `.md` in `outputs/investigations/` or `Logs/` rather than duplicating the content here.

---

## In Progress

- [ ] _Enrich programme prose with the inputs and outcomes of methodology review sessions_
- [ ] _Phase_A_Prose: generate phase A prose_
- [ ] _Phase_B_Verse_Context: Run through all verse context again — VC-7 pilot done (renewal); VC-8 done (yearning, treachery, jealousy, righteousness — malice carry-over to VC-9); VC-9 done (5 registries, 9 terms); VC-10 done (5 three-term registries, 12 terms); VC-11 done (5 three-term registries, 15 terms incl. 3 partial-completion mti=916/1364/5111); 47 of ~3,891 mti_terms at vc_completed across 16 registries; 169 legacy-Complete registries still pending under v3_9 contracts._

## Open

### DB Capture Architecture — Approach (a) (researcher approved 2026-04-27)

Source-of-truth: [db-capture-phase1-results-and-table-architecture-v1-20260427.md](outputs/investigations/db-capture-phase1-results-and-table-architecture-v1-20260427.md). All decisions locked in Part 12.

**Phase 1 (parser) — DONE**
- [x] Phase 1 parser + validator built (`scripts/_pilot_parse_obslog_to_db_v1_20260427.py`)
- [x] Pilot run on reg 067 obslog v2: 147 Q&A · 10 SD · 49 obs · 6 chapters · 8+6 questions · 41 review notes · 6 issues — all extracted clean
- [x] Coverage gap analysis: 119 of 141 answered Q&As + 6 chapters + 49 obs + 14 Qs + 41 notes were lost under Approach (b). Phase 1 captures all.

**Phase 2 (writer) work items**
- [x] **A. Schema migrations M40-M43** — DB at v3.17.0. `verse_context.analysis_note` · `wa_prose_section_citations` · `wa_obs_question_catalogue.review_note` · `wa_finding_catalogue_links.finding_id` NULL. Pre-migration backups at `bible_research_pre_M40_*`.
- [x] **B. Phase 2 writer** (`scripts/_pilot_capture_obslog_to_db_v1_20260427.py`) — full implementation: status_update, observations, chapters, sd_pointers, new_questions, qa_findings (with entity links + lifecycle resolution), catalogue_completeness (no_finding rows), review_notes (append), anchor_verse_analyses (Unit 7 extraction). Idempotent, transactional, pre-write backup.
- [x] **C. Readiness generator v5** — §N "Open Session B Items" rendered with four resolution paths. Output v5 includes `open_session_b_items` in JSON.
- [x] **D. Analytic Status `.md` generator** (`scripts/_pilot_build_analytic_status_v1_20260427.py`) — 7-section structure: lifecycle / coverage / resolved_qa / resolved_sd / not_relevant / chapters / anchor analyses / open items.
- [x] **E. Phase 2 writer pilot run on reg 067 obslog v2** — applied 2026-04-27. Backup: `backups/bible_research_pre_capture_writer_20260427.db`. Outcomes:
    - 49 observations → wa_session_b_findings (status='open' initially; 21 then resolved_qa via Q&A links)
    - 5 chapters → prose_section (sb_s2c_ch1..ch5; ~42 KB total body)
    - 14 new catalogue entries (8 generic gap + 6 Goodness Extensions)
    - 61 Q&A catalogue links (48 full + 7 partial + 6 not_applicable, plus 8 no_finding from catalogue_completeness)
    - 89 entity links (55 verse + 34 group)
    - 13 verse_context.analysis_note populated from Unit 7 anchor readings
    - 34 review notes appended across catalogue questions
    - 109 Q&As did not cite OBS-NNN refs in their answers — those remained as 'open' observations (28 of the 49 stay open). This is correct behaviour — they're research tasks for next session.
- [ ] **F. Spec revisions (researcher-gated)** — four documents:
    - [ ] `wa-patch-instruction` (account for the new categories)
    - [ ] `wa-sessionb-analysis-readiness` (now mostly a CC operation — major shift)
    - [ ] `wa-sessionb-analysis-output` (citation discipline; §N resolution discipline)
    - [ ] `wa-claudecode-instruction` (CC's extensive new responsibilities)
- [ ] **G. Programme prose update (researcher-gated)** — `prog_instr_session_a` / `prog_instr_session_b` / `prog_instr_verse_context` updated to reflect the new architecture.
- [ ] **H. tasks.md kept current** — this section. Check items off as completed.

**Catalogue completeness scope (decision #2 approved):**
- [ ] Phase 2 writer must record `coverage='no_finding'` in `wa_finding_catalogue_links` for every universal Q (147) per word that wasn't surfaced. Volume: ~29.4K rows at programme completion. Enables backfill + monitoring.

**CC anomaly-raising (decision #3 approved):**
- [ ] `DATA_ANOMALY_*` controlled list seeded with: `_ANCHOR_UNCITED`, `_DIMENSION_DRIFT`, `_ANSWER_UNGROUNDED`, `_EMPTY_TERM`, `_ORPHAN_ANALYSIS`. Expandable as patterns emerge.

**Backfill of historical 195 findings (decision #7):** Resolved by attrition — will be addressed naturally as those words are resubmitted for analysis. **No active backfill task.**

---

### VC corrective action strategy (raised 2026-04-25)

- [ ] _VC corrective action strategy — avoid full re-classification of the 1,800-term legacy-Complete bucket; rely on signal-targeted revision and pinpoint VCGROUP/VCVERSE corrections. Strategy + statistical assumptions captured in [vc-corrective-strategy-v1-20260425.md](outputs/investigations/vc-corrective-strategy-v1-20260425.md). Living document — bump version on each substantive update; pivot on triggers in §6._
- [ ] _VC revision-ledger build (Step 1 of strategy §5) — extract per-term routing outcomes from VCB-7..11 patches + DB; score univariate predictors (group count, term type, set_aside_reason gap, prior flags); record in `outputs/investigations/vc-revision-ledger-v1-{date}.md` + CSV. Threshold for action: predictor must hit ≥90% precision on ≥30-term validation before promotion to triage rule._
- [ ] _VCCONFIRM patch-type design (Step 5 of strategy) — gated on ≥1 reliable predictor surfacing in the ledger. Will need wa-patch-instruction §15 entry + applicator extension. Pilot scope tbd._

### VC outlier corrective actions (raised 2026-04-26)

- [ ] _**Outlier-1 — Extraction-anomaly residue, 6 terms.** Function-word / pronoun / animal terms lumped into 1 catch-all group across legacy-Complete registries, all `vc_status=not_done`. Same precedent as today's diligence/H4639H/I cleanups. Targets: H2088 "this" (reg 99 kindness, 245v), H0369 "nothing" (142 self-control, 218v), H0595 "I" (140 seeking, 156v), H5704 "till" (173 will, 260v), H0352A "ram" (187 strength, 139v), H4997 "wineskin" (213 listen, 6v). Cleanest action: mark `mti_terms.status='delete'` with documented reason + soft-delete verses._
- [ ] _**Outlier-2 — Listen (213) registry coherence.** Four terms ≥80% set_aside including the literal "to listen to" verb (G1522, 100% set_aside). Possible registry-scope drift during VC. Read inference_note + SB findings on the 4 terms; decide whether to follow the diligence path (cover-by-other-registry) or Phase 1 re-discovery._
- [ ] _**Outlier-3 — Integrity (92) H8549G unblemished root-bleed.** 45 of 51 verses set_aside (88%); registry-level set_aside 73%. Likely root-bleed from physical "unblemished" sense, parallel to rachamim/womb root-bleed in 103 love (PH2-103-002). Pinpoint VCVERSE patch or term-status adjustment expected._

### VC four-output model + A-02..A-05 resolution (2026-04-24)

- [ ] _VC programme roll-out: 174 legacy-Complete registries + 6 reset registries (compassion, fellowship, forgiveness, grace, love, mercy) all need processing under v3_8 contracts. VC-7 (renewal) + VC-8 + VC-9 are the rolling pilot/early-batches. Hardening blockers cleared 2026-04-24/25 (v3_8 + applicator A-06 rowcount gate). **Approach revision (2026-04-25):** strategy now signal-targeted, not bulk — see [vc-corrective-strategy-v1](outputs/investigations/vc-corrective-strategy-v1-20260425.md)._
- [ ] _VC-Prose-v4 (post-pilot): supersede `prog_instr_verse_context` v3 → v4 after VC-9/VC-10 confirms the contracts at scale. Minimal addition — one governance-level paragraph elevating the A-03 snapshot-anchoring principle (every classification is anchored to the data snapshot it read; if data has changed, re-read rather than silently apply). Mechanical details (md_version, input_versions, vocab renames) remain at instruction level — they do not enter prose._

### VC-7 pilot follow-ups (raised 2026-04-24 from renewal apply)


- [ ] _Applicator hardening (extend to Session B/D paths): mti_terms match-update, wa_term_inventory, wa_term_phase2_flags, word_registry match-update, wa_rule_registry, wa_addendum_registry, wa_dimension_index — same `_exec_update_strict` pattern. Pending._
- [ ] _Normalise out-of-vocab `set_aside_reason` values: "Material goods/property -- set aside" (17 rows) and "avf_homograph" (1 row) → controlled vocab via REPAIR patch._
- [ ] _Audit preserved-with-notes verse_context rows (4,366 active rows where `is_relevant=0 AND set_aside_reason IS NULL AND notes IS NOT NULL` survived M39). Sample-and-categorise: how many notes carry classification intent that should be lifted to `set_aside_reason` (controlled vocab) vs. legacy Session-D-deferral markers vs. other content. Output: `outputs/investigations/preserved-with-notes-audit-v1-{date}.md` with proposed REPAIR patch scope. Listed registry distribution earlier showed 271 in listen, 38 contrition, 35 fellowship, 28 grief, etc._

### Other open

- [ ] _VS_code: reset folder destinations for prose and references_
- [ ] _Word_data: Archive after Phase A prose is done.
- [ ] _Phase_B_Dimensions: Revisit all dimensions not yet through second round_
- [ ] _Phase_B_Analysis_Readiness: Run all words through readiness_
- [ ] _Phase_B_Prose:  Prepare prose ready for analysis_
- [ ] _Phase_B_Output:  Prepare output and update database for all words.
- [ ] 


## Done
- [x ] _VS_Code: automate commit-push_
- [x] _Workflow: create tasks.md at repo root_
- [x] _Programme_prose: create prose for programme chapters _
- [x ] _Global_Rule: update OBS to request and allow for changing of a reference if it not supplied on creation of the OBS. The default for the reference segment is "proc-ref-xx" _
  
### VC per-term rollout (approved 2026-04-24 — 4 decision gates passed, see [alignment analysis v4 §8](outputs/investigations/vc-instruction-session-a-md-alignment-v4-20260424.md))

- [x] _VC-1 M37 migration: mti_terms.vc_status + companion fields. Schema 3.14.0 → 3.15.0. Commit `5368b22`._
- [x] _VC-2 Applicator: VC-2 helper per-term validation + registry aggregation. Commit `7955b01`._
- [x] _VC-3 Patch meta: _patch_meta.terms_covered required for VC patches. Commit `7955b01`._
- [x] _VC-4 Instruction v3_1: per-OWNER-term primary input; §0.1 / §5 / §6.1 / §7.2 / §13 updated. Commit `e490931`._
- [x] _VC-5 Renderer: --term mode in build_session_a_prose.py; pilot on renewal. Commit `8cc71f3`._
- [x] _VC-6 Prose: prog_instr_session_a v2 → v3 supersede. Commit `07b1677`._
- [x] _VC-7 Pilot (full renewal, reg 134) — VCNEW + VCREVISE + VCSBFLAGS + VCRECOVERY applied 2026-04-24. All 7 OWNER terms at vc_completed, md_version=2/3, registry Complete. R1/R2/R3 clean. Two systemic issues surfaced → v3_5 amendment + applicator hardening (new tasks below)._
  

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

- [x] _VC-Instruction-v3_5..v3_8: A-06 (per-verse insert/update rule + applicator rowcount gate), A-07 (no-row = not analysed), A-08 (empty-ops VCREVISE), per-term patch-routing classifier (NEW-ONLY/REVISE-ONLY/MIXED/NO-CHANGE), match-shape fix. Live at `wa-versecontext-instruction-v3_8-20260425.md`. Companion patch instruction at v2_8._
- [x] _Applicator hardening (VC paths): `_exec_update_strict` on `verse_context` + `verse_context_group` UPDATE — rowcount=0 raises `ApplicatorError`, transaction rolls back. Verified live with deliberate failing test on 2026-04-24._
- [x ] _Encode GR-FILE-003 enforcement into automation: pre-edit check that any change to an instruction document file triggers a minor-version bump (or explicit "pre-publication" exemption). Ties to "Claude_Code_Rules: all outputs to carry version [major]_[minor] in name and internal meta" below._
- [x] _Reconstruct missed minor-version chain on VC instruction (v3_5..v3_8) and patch instruction (v2_7..v2_8). Archived intermediate states with corrected headers; live files renamed and own the lapse in their change-notes. Commit `dc2b654`._
---

*Created 2026-04-22.*
