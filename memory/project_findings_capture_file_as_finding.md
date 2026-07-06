---
name: project_findings_capture_file_as_finding
description: GOVERNING (2026-06-19) findings model — NEW cluster findings captured file-as-finding into prose_section (no dissection); OLD findings restricted via delete_flagged; new 11/7-char characteristics
metadata: 
  node_type: memory
  type: project
  originSessionId: d51a2ae4-3564-40b3-84fd-2dc7fed902d8
---

GOVERNING (2026-06-19, researcher direction). How cluster findings are captured into the DB and how old ones are retired. Established on M01 + M02; the pattern for all future clusters.

**File-as-finding (no dissection).** Each NEW findings file is stored WHOLE as one row — do NOT dissect into per-question/atomic rows. The files "stand on their own feet"; prose/essays are digested at **cluster level**, so atomic per-question grain is unnecessary and dissecting risks loss + a false grain. Grain may differ per cluster (M01 atomic = question-level collating chars; M02 atomic = char×question) — fine.

**Home = `prose_section`** (purpose-built; NOT the `finding` table): native `cluster_code` + `characteristic_id` + `cluster_subgroup_id`, whole `body`, `supersedes_id`/`superseded_by_id` lifecycle, `source_file`, and **`prose_section_fts` (FTS5)** search. New `prose_section_type`s: `cf_char_synth` (per-char synthesis/analysis), `cf_cluster_synth` (cluster-level), `cf_atomic` (question-level merged). CHECK constraints: `status IN (draft,in_review,approved,archived)` — use `approved`; `author IN (claude_ai,claude_code,researcher)` — use `claude_ai`. FTS is trigger-maintained (auto on insert).

**Characteristics.** NEW model created as `characteristic` rows from the `*-characteristics`/`*-ve-characteristics` files. M01=11 (c1-c11), M02=7 (c1-c7), **M03=10 (A-J)** (done 2026-06-20). Two UNIQUE constraints ignore delete_flagged, so the new rows must dodge the still-present legacy model: (1) `UNIQUE(cluster_code,char_seq)` → new rows use **char_seq = 100 + n**; (2) `UNIQUE(cluster_code,short_name)` → if a new name equals a legacy one (e.g. M03 F "Bitterness of soul"), **prefix the short_name** (M03 used "{LETTER} — {name}"). prose_section per-char files link by `characteristic_id`.

**M03 specifics (2026-06-20):** 10 chars A-J; per char TWO files — a *profile* (lexical evidence) + a *tier-findings* (the self-contained findings) — both captured as `cf_char_synth` (metadata `layer` = evidence_profile / tier_findings); + cluster-tier-synthesis (`cf_cluster_synth`) + the ve-out-of-scope record (`cf_cluster_synth`, layer=out_of_scope). 22 prose_section rows. Script `_apply_m03_findings_capture_20260620.py`. **The M03 out-of-scope SET-ASIDE (homonyms: che.vel cord, pid disaster, a.mal toil, etc.) is captured as a record but NOT applied as DB exclusions (cluster_code=NULL) — a separate researcher-reviewed patch per GR-PROG-005, still PENDING.**

**OLD findings — DO NOT disassemble yet (reversed 2026-06-19).** A restrict-marker pass (delete_flagged=1 + "superseded…" reason on old `cluster_finding` consolidated-2026-05-16, CLUSTER `finding` session_b_migration+l2_rollup, legacy `characteristic` Pre-v2_6) was applied then **fully REVERSED** — researcher: too early to tell what of the previous structure will be reused; do not break old structures apart. The mechanism works + is reversible (`_reverse_findings_stageC_restrict_20260619.py`) and is **PARKED** until the analytics have run through more clusters and the retire-decision is clearer. Current model = **alternative #1**: capture the NEW analysis additively in `prose_section` (A+B), leave the OLD structure fully intact/visible. (Alternative #2 = defer capture entirely, leave in files — would reverse A+B too.) Either way, **KEEP** verse-level `l2_meaning` (the L2 verse-reads = the new method's output), `ve_lexical`, VCGs, terms, verses.

**HELD — open scoping decisions (not yet actioned):** (1) `wa_session_b_findings` (legacy, registry-keyed — cluster scope unreliable: cluster_link tags few, registry-map over-includes shared registries) — restrict scope TBD; (2) old `cluster_subgroup` rows (structural, referenced by mti_term_subgroup/VCGs) — restrict or leave TBD.

Scripts: `_apply_findings_stageA_characteristics_/_stageB_capture_/_stageC_restrict_20260619.py`. Docs: `wa-findings-supersede-and-capture-{plan,completion}-v1-20260619.md`. Relates to [[feedback_all_study_work_in_db]], [[reference_canonical_tier_scheme_is_T0_T7]].
