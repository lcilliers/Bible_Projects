# Programme open-items register

**Canonical home:** `Workflow/Programme/Program_reports/` (per [docs/file-organisation-rules.md](../../../docs/file-organisation-rules.md) §3.10). **Living document** — single stable filename; do not spawn parallel docs or `-vN` copies.
**Doc version:** 8 · **Created:** 2026-05-30 · **Last updated:** 2026-06-01
**Versioning:** version tracked in this header; full history + rollback in git (`git log --follow <file>`, `git show <rev>:<file>`). [living-doc policy, 2026-05-31] Increment Doc version + Last updated on each substantive revision.
**v8 change (2026-06-01):** **A2 reframed + resolved** — old-VCG dissolution is per-cluster Phase C work (v3_0 §C.3), not a programme-wide soft-delete; 125 truly-orphan old VCGs (no term in any M-cluster) dissolved this session, the rest fold into each cluster's pass. (Session also did the base-up term-integrity remediation + FLAG triage + pointer linking — see git log 2026-06-01; not all tracked here.) v7: M4b retro-validation run + applied. Earlier versions in git history.
**Covers:** sessions 2026-05-29 (v3_0 refinement, M38 chapter authoring) and 2026-05-30 (audit, BOUNDARY check, programme readiness).
**Purpose:** single working list of everything in flight — decision / cleanup / instruction edit / script work / data fix. Sign off items as they close.

---

## Item status convention

Mark every item with one status. Update in place — do not create a new file.

| Status | Meaning |
|---|---|
| `OPEN` | not started |
| `DECIDED` | researcher ruling made; implementation may still be pending |
| `IN PROGRESS` | actively being worked |
| `DONE` | complete — append `(YYYY-MM-DD note)` |
| `DROPPED` | will not do — append reason |

> When an item changes status, edit its row here in place and add the date. Both researcher and CC use this same set.

---

## How to use this list

Each section has an ID prefix. Walk the list and for each item:
- Confirm the item description matches your recollection of what was discussed.
- Decide: do it now, schedule, defer indefinitely, drop.
- Mark complete with date + brief note when done.

The cross-references in `[brackets]` are the documents / scripts where the detail lives. Open the linked file for context before acting.

---

## §A. Policy calls — `DECIDED` 2026-05-31

All six resolved by researcher ruling. **Net effect: the *Analysis Complete* contract is now strict** — a cluster is not validly Analysis Complete if it has any of (a) unresolved cluster-linked SB/SD pointers [A1], (b) coverage gaps [A3], (c) open BOUNDARY items [A4], or (d) unresolved cluster-linked research flags [A4]. Clusters currently marked Analysis Complete that fail this are **provisionally incomplete** until cleanup closes the items.

### A1 — Session B / Session D pointers · `DECIDED`

SB/SD pointers belong to a **pre-cluster** research stage: valuable data, but they don't fit cluster methodology and are often unconnected to a cluster.
**Ruling:** run a **separate dedicated session** to convert *all* SB and SD pointers into cluster-related objects, so they can be handled inside cluster analysis. Once converted, any pointer **related to a cluster must be resolved before that cluster is Analysis Complete.**
*(Supersedes the "warning by default" recommendation.)* → cascades to §K, §L L1/L2.

### A2 — Old-format VCG codes · `DECIDED` → `DONE` 2026-06-01

Old-format VCG codes must **no longer surface** in any analysis or evaluation.
**Ruling:** they are to be (soft-)deleted.

**RESOLUTION 2026-06-01 (corrected understanding).** The "soft-delete the 572" framing was wrong: it would have orphaned live evidence. Investigation against the methodology established that **old-VCG dissolution is per-cluster Phase C work, not a programme-wide cleanup** — v2_9 Phase 8 / **v3_0 §C.3** dissolve a cluster's inherited VCGs *as part of that cluster's processing*, with the safe op set (soft-delete VCG **+ `verse_context.group_id=NULL` + soft-delete `vcg_term`**). Of the 567 active old VCGs (567 not 572 now): **498 belong to clusters** (210 in-progress → dissolved by their differential pass; 163 not-started → by their full run; 125 ready-for-re-analysis M05/M11) and dissolve **in place** when each cluster runs Phase C. **The only standalone remnant = 125 truly-orphan old VCGs** whose terms are all excluded/T2 (no M-cluster term → no Phase C reaches them). **Those 125 were dissolved this session** via the C.3 method (`scripts/_repair_dissolve_orphan_old_vcgs_v1_20260601.py`: 1,283 verse_context detached, 125 VCGs + 125 vcg_term soft-deleted; audit `research/investigations/orphan-old-vcg-dissolution-audit-20260601.md`; backup `backups/bible_research_pre_vcg_dissolution_20260601.db`). **A2 as a standalone item is closed**; residual old VCGs are now solely a per-cluster Phase C responsibility (no separate gate needed). → §M3/N7 (M06) old VCGs dissolve when M06 runs Phase C; §F6 old-format-VCG audit filter still valid as a guard.

### A3 — Large-coverage-gap clusters · `DECIDED`

**Ruling:** the cluster audit **must surface** coverage-gap clusters; any gap from the audit *or any other process* **must be resolved**. A cluster **cannot hold Analysis Complete while a gap exists.** Root-cause diagnostic still runs first (§I), but the gap is a **hard gate**, not a deferral.
*(Supersedes "defer per-cluster work until cause known".)* → cascades to §H, §I.

### A4 — BOUNDARY items + flags · `DECIDED`

BOUNDARY is the mechanism for **reclassifying a VCG or verse** that needs further clarification / research / decision **before it can become another sub-group object**.
**Ruling:** a cluster **cannot be Analysis Complete while BOUNDARY items remain**, and **BOUNDARY and flags must be evaluated together**. **CC verification 2026-05-31 — suspicion confirmed:** the audit reports flags and BOUNDARY as separate columns but never folds them into the completeness gate (`BOUNDARY_DECISION_PENDING`=39, `SD_POINTER`=273, `SB_FINDING`=183 were treated as §L housekeeping). → cascades to §G, §L, §F6/§F7.

### A5 — Re-produce all cluster inputs · `DECIDED`

**Ruling:** **all** cluster inputs will be **re-produced** during cleanup — not just M10/M10b/M10c — because the investigation found **serious gaps in the input documents** themselves.
**Dependency:** the input generator must be **fixed first** (§F1/§F2 + the §I tier-query diagnostic), or the re-production inherits the same defects.
*(Supersedes "generate M10 now, others likely fine".)* → cascades to §J, §F1/§F2, §N1.

### A6 — M38 T5.7.3 row · `DECIDED`

The analytic process generated this anomalous `cluster_synthesis` row whose body is a gap acknowledgment.
**Ruling:** do **not** silently reclassify it. **Surface it as a specific tracked item to resolve**, and root-cause why the analytic process emitted it (fix the behaviour, not just the row). → cascades to §H1, §M2.

### Revised implementation sequence

1. Fix the input generator (§F1/§F2) + run the §I diagnostic (one read-only investigation explains M04/M07/M08/M09 gaps and pinpoints the generator fix).
2. Dedicated SB/SD pointer-conversion session (A1) — also feeds the A4 flag-gate.
3. Redefine the completeness gate (A3+A4): gaps + BOUNDARY + cluster-linked flags all hard-blocking; update audit (§F6/§F7) to enforce and to **demote** failing clusters.
4. A2 cleanup: soft-delete the 572 active old-format VCGs.
5. BOUNDARY dispositions (§G), considered with flags.
6. A6: surface + root-cause the M38 T5.7.3 generator behaviour.
7. Re-produce all cluster inputs (A5) on the corrected generator.
8. Re-run the programme audit; clusters failing the new gate lose Analysis Complete until resolved.

---

## §B. Publishing instruction edits

Pending edits to `[Workflow/Instructions/wa-cluster-publishing-instruction-v1_0-20260530.md]`. Cannot proceed until §A is settled.

| ID | Edit | Depends on |
|---|---|---|
| B1 | Add **§4.1 Evidence inclusion contract** — Category A (must appear) / Category B (must not) / Category C (informational). | — |
| B2 | Add **§4.2 BOUNDARY readiness pre-condition** — no active BOUNDARY sub-group members; no unresolved `BOUNDARY_DECISION_PENDING` flags. | — |
| B3 | Add **§4.3 Stray-findings policy** — warning vs hard fail decision from A1. | A1 |
| B4 | Add **§4.4 Step 1 gate behaviour** — audit script invocation, exit code semantics, halt conditions. | A1, A2 |
| B5 | Add **§4.5 Per-chapter routing rules** — which findings / observations route to which chapter (this is currently implicit in the generator script, not in the instruction). | — |
| B6 | Optional: add a `wa-publishing-instruction-changelog.md` so future edits to this single document are tracked. | — |

---

## §C. Cluster instruction reconciliation

| ID | Item | Notes |
|---|---|---|
| C1 | Amend `[Workflow/Instructions/wa-sessionb-cluster-instruction-v3_0-20260527.md]` **§9 Phase E** to a one-paragraph stub pointing to the new publishing instruction. | The current §9 describes a tier-prose model never used in practice. |
| C2 | Add **note in §6** of the new publishing instruction confirming Phase F (validation/closure) still references the v3_0 §10 check list — Phase E completeness criteria in the v3_0 §10.2 (item 5) need updating to match the new chapter-prose model. | Cross-reference change. |

---

## §D. Files to archive (loose files retired by the new instruction)

| ID | File | Action |
|---|---|---|
| D1 | `Workflow/Instructions/wa-sessionc-cluster-style-method-v1_1-20260512.md` | Move to `Workflow/archive/` with note "absorbed into wa-cluster-publishing-instruction-v1_0 §7". |
| D2 | `Workflow/Instructions/wa-sessionc-cluster-ch1-instruction-v1_0-20260512.md` through ch7 | Same — note "absorbed into §8.1–§8.7". |
| D3 | `Workflow/Instructions/wa-sessionc-cluster-appendices-instruction-v1_0-20260512.md` | Same — note "appendices retired by publishing instruction §9". |
| D4 | `Workflow/Instructions/wa-v3-publication-pipeline-design-v1-20260527.md` | Same — note "superseded by wa-cluster-publishing-instruction-v1_0". |
| D5 | M38's loose appendix drafts in `Sessions/Session_Clusters/M38/publishing/wa-cluster-M38-appa/b/c-*.md` | Decide: archive (they were authored) or delete (appendices retired). |

---

## §E. Section-type codes to retire in `prose_section_type`

| ID | Code | Action |
|---|---|---|
| E1 | `sc_v2_tier_T0` through `sc_v2_tier_T7` (8 codes) | Mark `delete_flagged=1`. Never held data. |
| E2 | `sc_v2_synth_opening` | Mark `delete_flagged=1`. Never held data. |
| E3 | `sc_v2_synth_divine_pattern` | Mark `delete_flagged=1`. Never held data. |
| E4 | `sc_v2_synth_appendix` | Mark `delete_flagged=1`. Never held data. |

Confirm with a query first — if any rows do exist, investigate before deleting.

---

## §F. Generator / script updates

**Discovery source (cross-ref).** The input-generation problems were investigated in two reports:

- [publishing_input_audit_findings_v1](../../../outputs/markdown/publishing_input_audit_findings_v1_20260530.md) — **SUPERSEDED**
- [publishing_input_audit_v2_findings](../../../outputs/markdown/publishing_input_audit_v2_findings_20260530.md) — **current framing**

v2 supersedes v1: v1 tested for standalone VCG `context_description` and term-inventory blocks; v2 retired those as *informational* (Category C) because v3_0 findings carry that content verbatim. Any action inherited from v1 §6.1/§6.2 is **void** — see the correlation note below.

**Scope caveat.** The discovery audited **M38, M15, M06 only**. The large-gap clusters in F3 / §I (M04/M07/M08/M09) were surfaced by a *different* audit — the all-clusters driver (F7) — and were **never examined by the input-generation discovery**. F3 is therefore a genuinely open investigation, not a discovery conclusion.

| ID | Script | Change | Status |
|---|---|---|---|
| F1 | generator | Remove appendix + Ch8 generation (`build_ch8`, `build_app_a/b/c`, `appa/appb/appc` registry, `--only` keys). Produce exactly 7 chapter files. (Ch8 = *"What this study does not yet address"* — a gap-findings **prose chapter**, not a readiness/BOUNDARY chapter; retired by the v1_0 7-chapter model.) | `OPEN` — confirmed **not done** 2026-05-31: generator still defines `build_ch8` (L521) + `build_app_a/b/c` (L546+) |
| F2 | generator | Update internal references to the new publishing instruction (currently points to retired style/method + per-chapter + ch8/appendix instruction docs). | `OPEN` |
| F3 | generator | Diagnose large-gap clusters (M04/M07/M08/M09): findings keyed to old `question_code` schema? tier query mismatch? **Not covered by discovery — see scope caveat.** This is step 1 of the §A revised sequence. | `OPEN` (A3 decided → hard gate) |
| F4 | `_ingest_chapter_prose_v1_{date}.py` (NEW) | Read chapter drafts, ingest into `prose_section`, idempotent via body-hash, fire status transition on 7th chapter. | `OPEN` |
| F5 | `_consolidate_cluster_essay_v1_{date}.py` (NEW) | Read 7 chapter rows from DB, package for AI consolidation, save .md + render .docx. | `OPEN` |
| F6 | `_audit_cluster_input_coverage_v2` | A2 decided: add old-format-VCG filter (gate matches modern code pattern only). A1 decided: cluster-linked pointers gate. Wire both. | `OPEN` (A1, A2 decided) |
| F7 | `_audit_all_analysis_complete_clusters_v1` | Re-run after each cleanup pass. A3+A4: extend to **enforce** gaps + BOUNDARY + cluster-linked flags and **demote** failing clusters (§A4). | `IN PROGRESS` — runnable; gate-enforcement extension `OPEN` |
| F8 | `_generate_cluster_overview_v1` | SC-published check now DB-based. | `DONE` (2026-05-30) |
| F9 | Step 1 wrapper (NEW) | Orchestrate Step 1 as **readiness gate (F13) → generate → coverage gate (F6)**, halting on either failure. | `OPEN` — depends F1, F6, F13 |
| **F10** | generator | **NEW (v2 Category A / v1 §6.3): route publication-targeted `cluster_observation` rows to chapters by `observation_type`.** Generator currently has **zero** observation routing; M38 passed the gate only because it has no publication-targeted observations. Any cluster that does will FAIL. | `OPEN` |
| **F11** | generator | **NEW (A6 / v2 §3): route `cluster_synthesis` findings to their tier chapter.** Current handling (L119) routes synthesis to Ch1/Ch3 only; M38 T5.7.3 (a tier-5 synthesis row) orphaned. Fix routing **and** root-cause the gap-acknowledgment row (A6). | `OPEN` |
| **F12** | generator | **NEW (v1 §6.4): gap-status finding handling.** Keep `finding_status='gap'` excluded (Category B), but emit a per-chapter gap-count line so the AI knows how many expected answers the analytical record could not produce. | `OPEN` |
| **F13** | generator | **REFRAMED 2026-05-31 (researcher): a *simple status check*, not a heavy gate.** At the top of the generator's `main()`: abort (nonzero exit, **zero** files) unless `cluster.status='Analysis Complete'`. It *trusts* the status — the heavy validation lives in F14 (the contract that produces the status). Confirmed gap: `main()` (L665–719) currently writes unconditionally. | `OPEN` — small |
| **F14** | `_close_cluster_analysis.py` (NEW) + shared predicate | **NEW (A1+A2+A3+A4): Analysis-Complete completion contract.** The canonical closure routine that enforces C1–C7 (BOUNDARY, flags, pointers, old VCGs, term linkage, status) and only on full pass writes `status='Analysis Complete'` (one canonical spelling). **Replaces the ad-hoc per-cluster `UPDATE` flips** (`_apply_*_phase12_closure` etc.) which do **no validation** — confirmed 2026-05-31: closure scripts only assert prior status then bare-flip. Shared predicate imported by F7 so "validly complete" is defined once. | `OPEN` — design drafted, awaiting review |

**Status lifecycle + gates (reframed 2026-05-31).** Full design: [wa-cluster-readiness-gate-design.md](../../methodology/wa-cluster-readiness-gate-design.md). The heavy validation belongs to the transition that *produces* `Analysis Complete`, not to input generation:

1. **Completion contract (F14) — produces `Analysis Complete`.** Enforces C1–C7 (BOUNDARY / flags / pointers / old VCGs / linkage). A cluster cannot earn the status unless these pass. This is the real gate; today nothing enforces it (bare `UPDATE` flips), which is why F7 keeps finding invalid "complete" clusters.
2. **F13 — before generation, trivial status check.** Abort unless `status='Analysis Complete'`. Trusts the contract.
3. **Coverage gate (F6) — after generation, halts Step 2.** Validates the produced *inputs* reference all required evidence (discovery v2 §5).
4. **New status `Publishing Ready`** — set when inputs + prose + prose-in-DB complete (fired by F4); gates combined-doc/derivative assembly. Controlled-vocabulary addition pending researcher sign-off; relates to §M4.

F9 orchestrates F13 → generate → F6. Lifecycle: `Analysis - In Progress` —(F14)→ `Analysis Complete` —(publish routine)→ `Publishing Ready`.

**Correlation note (§F vs discovery, 2026-05-31):**

- **Void — do NOT implement:** v1 §6.1 (surface VCG `context_description`) and v1 §6.2 (surface term inventory in Ch2). Retired by v2 as informational. F1's appendix removal is consistent — the appendix was the term-inventory home.
- **Discovery → §B, not §F:** the inclusion contract (Category A/B/C), BOUNDARY pre-condition, and Step-1 gate (v1/v2 §4.x, §6) are *instruction* edits, tracked in §B (B1–B5). §F carries only the generator/script changes that implement them.
- **Discovery → §M, not §F:** M38's missing `mti_term_subgroup` links (v1 §6.5) is a data backfill, tracked at §M1 — not a generator change.
- **Newly added:** F10/F11/F12 close the generator-side gaps the discovery surfaced that §F had not previously captured. **§F is now complete relative to the discovery.**

---

## §G. BOUNDARY cleanup — per-cluster work

> **Per A4 (decided): hard gate.** No cluster is Analysis Complete while BOUNDARY items remain, and BOUNDARY is evaluated **together with** cluster-linked flags (§L). Priority is no longer the question — all of these must close.

Each item is one researcher disposition pass. Each `BOUNDARY_DECISION_PENDING` flag is per-term (set aside / promote to sub-group / route to cluster / retain with rationale).

| ID | Cluster | Type | Volume | Status |
|---|---|---|---|---|
| G1 | M03 Grief | unresolved `BOUNDARY_DECISION_PENDING` flags | 28 of 28 | not started — worst backlog |
| G2 | M01 Fear | same | 7 of 12 | not started |
| G3 | M02 Anger | same | 4 of 6 | not started |
| G4 | M06 Hate | active BOUNDARY sub-group members | 56 verses + 4 terms + 5 VCGs | not started — sub-group needs emptying |
| G5 | M15 Wisdom | same | 14 verses + 13 terms + 1 VCG | not started — sub-group needs emptying |
| G6 | Programme-wide other unresolved `BOUNDARY_DECISION_PENDING` (not in G1-G3) | flags | 0 (the 39 unresolved all map to M01/M02/M03) | clean once G1-G3 done |

---

## §H. Coverage gap fixes — generator routing bugs

Small misses, look like tier-routing or finding-status edge cases. Each needs a per-cluster look in the report to confirm cause.

| ID | Cluster | Miss count | Detail report |
|---|---|---|---|
| H1 | M38 | 1 finding (T5.7.3) | [cluster_input_coverage_M38_v2_20260530.md](cluster_input_coverage_M38_v2_20260530.md) — depends A6 |
| H2 | M15 | 1 finding + 4 VCGs + 1 anchor (all BOUNDARY-derived) | [cluster_input_coverage_M15_v2_20260530.md](cluster_input_coverage_M15_v2_20260530.md) — resolves with G5 |
| H3 | M39 | 1 finding + 3 VCGs + 17 anchors | per-cluster report needed |
| H4 | M01 | 20 findings | per-cluster report needed |
| H5 | M02 | 44 findings | per-cluster report needed |
| H6 | M20 | 34 findings + 14 VCGs | per-cluster report needed |
| H7 | M46 | 46 findings + 31 VCGs + 7 anchors | per-cluster report needed |
| H8 | M26 | 60 findings + 18 VCGs + 47 anchors | per-cluster report needed |
| H9 | M03 | 75 findings + 7 characteristics | per-cluster report needed — likely BOUNDARY-related |

Per-cluster reports will exist at `outputs/markdown/cluster_input_coverage_{CODE}_v2_20260530.md` once each cluster's audit is captured. The driver script generated them for the run — confirm presence and review.

---

## §I. Large coverage gaps — root-cause investigation

> **Per A3 (decided): hard gate.** A gap blocks Analysis Complete. Diagnose the systemic cause first (one investigation covers all four), then resolve — the gaps are not deferrable. This is **step 1** of the revised sequence and also yields the §F1/§F2 generator fix.

These four are too big for per-cluster fixes. Diagnose the systemic cause first.

| ID | Cluster | Missing findings | Stray SB | Hypothesis to test |
|---|---|---|---|---|
| I1 | M09 Humility | 1068 | 186 | Findings exist but use old question_code schema; generator's tier query doesn't match |
| I2 | M07 Shame | 1051 | 41 | Same |
| I3 | M08 Pride | 901 | 11 | Same |
| I4 | M04 Joy | 1203 | 77 | Same |

**Diagnostic step (one investigation covers all four):** open a finding row from each cluster's DB record; compare `obs_id` / `question_code` against what `_generate_cluster_session_c_inputs_v2` expects. If the schema differs, decide: (a) re-key findings to the v3_0 catalogue, (b) amend the generator to handle both schemas, (c) accept these clusters need re-analysis under v3_0.

---

## §J. Clusters with NO chapter inputs

| ID | Cluster | Action |
|---|---|---|
| J1 | M10 Sin | Run `[scripts/_generate_cluster_session_c_inputs_v2_20260512.py] --cluster M10`, then audit |
| J2 | M10b Wickedness | Same |
| J3 | M10c Defilement | Same |

**Superseded by A5:** these are no longer a special case. *All* cluster inputs are re-produced during cleanup on the corrected generator, because the investigation found serious gaps in the input documents themselves. M10/M10b/M10c are simply part of that programme-wide re-run.

---

## §K. Stray Session B / Session D findings backlog

702 stray SB findings + 440 unresolved SB/SD research flags across 10 clusters. Depends on A1 (warning vs hard fail).

| ID | Cluster | Stray SB | Stray flags |
|---|---|---|---|
| K1 | M39 Blessing | **219** | 116 |
| K2 | M09 Humility | 186 | 66 |
| K3 | M04 Joy | 77 | 82 |
| K4 | M26 Righteousness | 49 | 37 |
| K5 | M07 Shame | 41 | 28 |
| K6 | M20 Doubt | 39 | 32 |
| K7 | M46 Abundance | 38 | 30 |
| K8 | M15 Wisdom | 35 | 31 |
| K9 | M08 Pride | 11 | 10 |
| K10 | M06 Hate | 7 | 8 |

**Per A1 (decided — not "warning"):** these stray SB/SD findings are converted to cluster-related objects in a dedicated pointer-conversion session, after which any cluster-linked pointer **must be resolved before that cluster is Analysis Complete**. K1 (M39's 219) is large enough to merit individual attention within that session.

---

## §L. Programme-wide research-flag housekeeping

> **No longer pure housekeeping (per A1 + A4).** Cluster-linked flags now **gate** that cluster's completeness and are evaluated with BOUNDARY (§G). L1 `SD_POINTER` and L2 `SB_FINDING` are the pointers converted in the A1 dedicated session. L3 `BOUNDARY_DECISION_PENDING` is resolved by §G. Only genuinely cluster-independent flags (L4–L8) remain "housekeeping".

Independent of any specific cluster — programme-level hygiene.

| ID | Flag code | Unresolved count | Action |
|---|---|---|---|
| L1 | `SD_POINTER` | 273 | Session D residue; mass-resolve with a status update if confirmed not needed |
| L2 | `SB_FINDING` | 183 | Session B residue; review per-registry |
| L3 | `BOUNDARY_DECISION_PENDING` | 39 (all in M01/M02/M03) | Resolved by §G G1–G3 |
| L4 | `VERSE_EVIDENCE_BREADTH_NOTE` | 43 | Informational notes; review |
| L5 | `PH2_DATA_ERROR` | 9 | Data quality issues; investigate |
| L6 | `DIMREVIEW_SESSION_D` | 5 | Stale review flags; close |
| L7 | `SB_INNER_BEING` | 4 | Review |
| L8 | Others (`RESEARCHER_DECISION`, `THEMATIC_LINK`, etc.) | <5 each | Per-flag triage |

---

## §M. Analysis-Complete validation + status (the gate everything depends on)

> **Full design:** [wa-cluster-readiness-gate-design.md](../../methodology/wa-cluster-readiness-gate-design.md) §3. **Build this before continuing cleanup** — it defines which clusters actually need work. *(M1/M2/M3 moved to §N, 2026-05-31.)*

### M4 — Proper validation of `Analysis Complete`

**Problem.** Many clusters hold `Analysis Complete` that should not. The status is a bare `UPDATE` in per-cluster closure scripts with **no validation** (confirmed: `_apply_*_phase12_closure` asserts prior status, then flips). The F7 audit only observes afterwards. So the status is a hand-set label, not a guarantee.

**The gate — researcher definition (2026-05-31).** A cluster is `Analysis Complete` when **(1)** its **verse/tier findings are captured**, and **(2)** every **leftover — boundary, flag, Session B/D pointer — is resolved** to a **validated observation** (impact described) **or excluded/deleted after researcher review**. Nothing survives in limbo or as nonsense. Enforced at the transition; checks analytical data-state only (not input coverage).

**Where each cleanup category lands:**

| Gate · Condition 1 (findings) | Gate · Condition 2 (leftovers) | Data-cleansing prereq | Publishing-stage (post-AC) | Housekeeping |
|---|---|---|---|---|
| §N finding-class (M38) · tier omissions | §G BOUNDARY · §L3 · §K/§L1–2 pointers · actionable observations | §N old-VCG (M06) · §N term-linkage (M38) | §H coverage · §J no-inputs · §I *if mis-keyed* | §L4–L8 · §P bulk-update (one-time) |

**The one unknown:** §I large gaps (M04/M07/M08/M09) cannot be bucketed until the F3 diagnostic decides *mis-keyed* (→ Publishing Ready) vs *genuinely absent* (→ Condition 1).

**Actions:**

- **M4a** — build the two-condition gate as the canonical closure routine (= §F **F14**); predicate shared with F7. *(First version exists as `scripts/_validate_analysis_complete_v1_20260531.py` — the validation/retro pass; the closure-on-transition wrapper is still to fold in.)*
- **M4b** — **retro-validate + demote.** `DONE 2026-05-31` (`--apply`): all **17** clusters at/beyond Analysis Complete validated → **0 pass / 17 fail**, all reset to `Analysis - In Progress`. Report: [cluster_ac_validation_v1_20260531.md](../../../outputs/markdown/cluster_ac_validation_v1_20260531.md). Failure types: gating flags (14), stray SB findings (13), BOUNDARY pending (3: M01/M02/M03), active BOUNDARY members (2: M06/M15), unconfirmed actionable obs (1: M10). **Remedial work begins next session.**
- **M4c** — fix the deficient audit (§F **F7**): gate not just report; demote on fail. *(The validation script is the gating engine; F7 driver to import its predicate.)*
- **M4d** — normalise status spelling + adopt lifecycle `Analysis - In Progress` → `Analysis Complete` → `Publishing Ready`. *(Spelling now moot for the 17 — all reset to one value; canonical-set decision still open for the forward path.)*

**Current programme state (post-reset 2026-05-31):** 0 clusters Analysis Complete; 17 `Analysis - In Progress` (the former "complete" set, now awaiting remedial work); 29 Not started; 1 Structurally Ready; 1 Ready for re-analysis. **The A1 pointer-conversion session + the §G BOUNDARY cleanup are the dominant remedial actions** (they clear the two top failure types).

**Open questions** (design §6): canonical statuses (q1); Condition-2 gating flag codes (q2); actionable-vs-informational observation types (q3); Condition-1 catalogue (q4); retro-validate? (q5); approve `Publishing Ready` (q6); sequence data-cleansing prereqs (q7).

---

## §N. Cluster-specific fixes

N1–N4: M38 publishing artefacts from the chapter-by-chapter experiment (may not belong in the v1_0 baseline). N5–N7: cluster-specific **data fixes** moved here from §M (2026-05-31) — per-cluster interventions, not programme-wide. **Flag:** researcher said "M38-specific", and N5/N6 are M38, but **N7 concerns M06**, not M38 — redirect if you meant only the M38 pair.

| ID | File(s) / issue | Action |
|---|---|---|
| N1 | `Sessions/Session_Clusters/M38/publishing/wa-cluster-M38-ch1-draft-v1-20260530.md` through ch7 | Already drafted. Once ingest script (F4) exists, ingest into `prose_section` as the M38 v1_0 publishing artefact. |
| N2 | `Sessions/Session_Clusters/M38/publishing/wa-cluster-M38-appa/b/c-draft-v1-20260530.md` | See D5 — appendices retired. Decide archive vs delete. |
| N3 | `Sessions/Session_Clusters/M38/publishing/wa-cluster-M38-book-v1-20260530.md` + .docx | Concatenated "book" from earlier experiment. Retire (replaced by 7-chapter prose_section + consolidated essay model). Archive on disk. |
| N4 | `Sessions/Session_Clusters/M38/publishing/wa-cluster-M38-essay-v1-20260528.md` + .docx | Single-pass essay from earlier experiment. Archive — not the canonical Step 3 output. |
| N5 (was M1) | **M38** has **0 `mti_term_subgroup` links** | Post-split data issue. Sub-groups + terms exist; linkage table empty. Backfill from M01 (split parent) or v3_0 split doc. **Gates Analysis Complete** (contract C6). |
| N6 (was M2) | **M38** T5.7.3 mis-classified row | `cluster_synthesis` row whose body is a gap acknowledgment. See A6. **Gates Analysis Complete** (contract C8). |
| N7 (was M3) | **M06** uses old-format VCG codes (`90-001` etc) | See A2. **Gates Analysis Complete** (contract C5). *Note: M06, not M38.* |

---

## §O. The v3_0 refinement workstream from yesterday

Five focus areas were discussed for v3_0 before M36. Some folded into the publishing instruction; others remain open.

| ID | Topic | Outcome |
|---|---|---|
| O1 | Dead time | Open — no resolution captured |
| O2 | Alerts framework | Open — no resolution captured |
| O3 | Self-healing audits | Partially addressed by the new audit/gate; full self-healing not designed |
| O4 | Load management | Open — no resolution captured |
| O5 | Phase E staging | Resolved — folded into the new publishing instruction. The v3_0 §9 description was a methodology dead-end; v1_0 publishing instruction is the working baseline. |

O1/O2/O4 may need separate sessions before any new v3_0 cluster work begins.

---

## §P. Items inherited from before this session

| ID | Item | Source |
|---|---|---|
| P1 | Review the bulk update slip-up (2026-05-27 catch-up + ingest) — what got into the DB during the auto-catch-up phase, what should be rolled back | Pre-session todo carried forward |

---

## §Q. Decisions about review process itself

| ID | Decision | Update |
|---|---|---|
| Q1 | Where does this open-items list live? Suggest: `Workflow/programme_state/open_items_{date}.md` rather than `outputs/markdown/`. Outputs is for derivations; programme_state is for working register. | Surface the guides for folder management again - this study has lost its way in terms of keeping the with guidelines. There is no Workflow/program_state folder - no need to surface a new folder. follow the guide. |
| Q2 | How are completed items marked? Strikethrough? Move-to-archive section at bottom? Separate "completed_{date}.md"? | put a section at the top to set the convention for the document completion.  I suggest a simple markdown row with a place to add a updated/agreed/completed convension that both you and me can use|
| Q3 | How often is this list re-generated from the audit driver vs hand-maintained? Suggest: re-run the audit driver after every cleanup pass; hand-maintain the decisions / policy sections. | no idea what you are talking about|

**Resolution (`DONE` 2026-05-31):**

- **Q1** — register relocated + renamed to `Workflow/Programme/Program_reports/wa-programme-open-items-v1-20260531.md` per [docs/file-organisation-rules.md](../../../docs/file-organisation-rules.md) §3.10 / §2.1. No new folder created.
- **Q2** — status convention added at the top of this document; both researcher and CC use it.
- **Q3** — clarified: this register is **hand-maintained**. The audit script (`_audit_all_analysis_complete_clusters_v1`) produces fresh per-cluster evidence reports that we read and cite; it does not regenerate this document. Q3 closed.


---

## What's next

§A is now `DECIDED`. Work proceeds in the **revised implementation sequence** under §A (above). The natural first concrete action is **step 1 — the §I diagnostic** (one read-only investigation that explains the M04/M07/M08/M09 gaps and pinpoints the §F1/§F2 generator fix), since A5's programme-wide input re-run must run on a corrected generator.

Still owned by researcher (not yet decided): **§M4** status-spelling normalisation.

---

*Single living register. Mark items with the status convention at the top and close them in place. Re-run the audit script for fresh evidence, but maintain this document by hand.*
