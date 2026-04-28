# VC Corrective-Action Strategy — Pivot Proposal

**Document version:** v1 (proposal — for researcher review; supersedes nothing yet)
**Date:** 2026-04-26
**Author:** Claude Code, drafted under researcher direction
**Linked predecessor:** [vc-corrective-strategy-v1-20260425.md](vc-corrective-strategy-v1-20260425.md)
**Status:** **DRAFT for review.** No DB or contract changes proposed in this file. If approved, becomes `vc-corrective-strategy-v2-20260426.md`.

---

## 1. Position

**The current VC corrective-action strategy treats the 1,800-term legacy-Complete bucket as work-in-progress to be re-classified per-term under v3_10 contracts.** Today's evidence indicates this is the wrong cost-benefit shape.

**Proposed pivot:**

> Stop running the per-term v3 VC pass over the legacy-Complete bucket. Treat legacy classifications as **acceptable input to Session B analysis** with a documented caveat. Surface the genuine quality problems through analysis-stage findings, and resolve them with surgical VCGROUP / VCVERSE patches at the moment they surface — not by re-classifying every term in advance.

This is a **strategy pivot** (v1 → v2), not a minor revision: it changes the routing of the legacy bucket from "VC redo → Session B" to "Session B direct, VC patches on demand."

---

## 2. Evidence supporting the pivot (snapshot 2026-04-26)

### 2.1 Ledger (VCB-7..13, N=56 RE-EVAL)

| Routing | Count | % |
|---------|------:|--:|
| NO-CHANGE | 47 | **84%** |
| REVISE-ONLY | 8 | 14% |
| MIXED | 1 | 2% |

After VCB-14 (11 terms, 8 NO-CHANGE + 3 MIXED), the recent 25-term window drops to 76% NO-CHANGE — below the strategy v1 §6 trigger of 80%. **In v1's framework that triggers a "stop and re-evaluate" event.** This document is that re-evaluation.

### 2.2 VCB-Q01 (flag-driven quality pinpoint, today)

Six terms targeted by unresolved quality flags (PH2_BOUNDARY_QUESTION, PH2_DATA_SPLIT_REQUIRED HIGH, SB_FINDING). Outcome: **all 6 NO-CHANGE under v3_10**. Even the three "active review" candidates (paroxusmos, apeitheō, paga — including the HIGH-priority paga 3-sense split) were judged correctly classified as-is.

The 2 new SB findings raised by VCB-Q01 (apistia and spoudē over-fragmentation) are explicit Session-B-domain observations — the classifier is saying "these grouping patterns are something Session B should think about", not "these classifications are wrong."

**This is the pivot's most direct evidence:** flag-driven targeting plus current v3_10 contracts confirms the existing classification holds up. The "fix it before analysis" logic doesn't survive contact with the data.

### 2.3 Outlier scan (today)

Three statistical outlier categories were investigated:

| Outlier | Hypothesis | Reality |
|---|---|---|
| **1** Extraction-anomaly residue (6 terms with function-words/pronouns/animals lumped into 1-group catch-alls) | Real bug | Real bug — 6 terms deleted, 1024 verses soft-deleted |
| **2** Listen (213) coherence (4 terms ≥80% set_aside including the literal "to listen to" verb) | Registry concept may be broken | False alarm — legacy classification artefacts, registry has substantial real listen content (H7181 96% relevant, H8085H 98% relevant) |
| **3** Integrity (92) H8549G "unblemished" 88% set_aside | Root-bleed contamination | False alarm — same lemma, different sense applications (sacrificial vs character); classifier correctly distinguished |

**Hit rate: 1 of 3 statistical signals was actual pathology.** The other two were correct classification under noise.

### 2.4 Real fixes today, by surfacing path

| Fix | How surfaced | Where pinpoint pass would have caught it |
|---|---|---|
| Diligence (48) excluded — 5 HFA terms deleted | Outlier scan + "registry has 0 active groups" investigation | Per-term VC pass would have re-classified the 7 H0629 verses but missed the registry-level "concept already in zeal" issue |
| H4639H/I (98 justice) marked delete | Quality flag scan + STEP investigation | Per-term VC pass cannot fix a 0-verse term |
| Outlier-1 (6 anomaly terms) deleted | Statistical outlier scan + visual triage | Per-term VC pass would have re-classified the catch-all groups verse-by-verse — high cost, same outcome |

**None of today's real fixes required a per-term VC re-classification to surface.** All were caught by focused scans operating on existing data.

---

## 3. What changes structurally

### 3.1 Routing of the legacy-Complete bucket

| Aspect | Strategy v1 | Strategy v2 (proposed) |
|---|---|---|
| Default treatment | Per-term VCREVISE under v3_10 contracts | **Use legacy classification as-is** |
| When VC patches are issued | Always (NO-CHANGE → empty-ops VCREVISE; REVISE → full VCREVISE) | **Only on demand** — when Session B / DimReview / Session D surface a specific issue |
| Patch types in active use | VCREVISE, VCNEW, VCSBFLAGS, VCSDPOINTERS, VCGROUP, VCVERSE | **VCGROUP, VCVERSE, VCSBFLAGS** become primary; VCREVISE only for the 6 reset registries |
| Cost (estimate) | ~120 classifier batches | **Near-zero** for legacy bucket; analysis-driven surgical patches as encountered |
| `mti_terms.vc_status` for legacy bucket | Eventually all advanced to `vc_completed` | **Stays `not_done`** — accurate (no v3 pass was done) |
| Audit-trail signal that VC was/wasn't redone | `vc_status` field + `md_version` | **Same** — `vc_status='not_done'` IS the audit trail |

### 3.2 The Session B readiness gate

`wa-sessionb-analysis-readiness` (current minor version v1_6) carries a hard VC gate: a registry must have `verse_context_status='Complete'` and (per v3 contracts) `mti_terms.vc_status='vc_completed'` for all OWNER terms before Session B Stage 2 may proceed.

Under the pivot, this gate **changes shape** rather than weakens:

| Acceptable as Session B input | Strategy v1 | Strategy v2 (proposed) |
|---|---|---|
| `verse_context_status='Complete'` + all `vc_completed` | ✓ | ✓ |
| `verse_context_status='Complete'` + `vc_status='not_done'` (legacy) | ✗ — must be redone | **✓ — with caveat acknowledgement** |
| `verse_context_status='Verse Context Reset'` (the 6 reset registries) | ✗ | ✗ — still must be reclassified per Q12 mandate |
| `verse_context_status` NULL (excluded) | ✗ | ✗ — still excluded |
| `verse_context_status='In Progress'` | ✗ | ✗ |

The "caveat acknowledgement" means the Session B classifier **declares aloud at registry start** something like:

> *"Registry NN word loaded for analysis. VC source: legacy-Complete (pre-v3 contracts). Classification accepted as-is; quality issues surfaced during analysis will be resolved via VCGROUP/VCVERSE/VCSBFLAGS patches at the point they're encountered. No bulk pre-analysis VC pass required."*

This is symmetric with the existing posture-declaration pattern in VC instruction §6.1.

### 3.3 Analysis-stage correction protocol

When Session B (or DimReview, or Session C) surfaces a quality problem during analysis, the routing is:

| Symptom | Patch type | Applicator effect |
|---|---|---|
| Single verse mis-classified (is_relevant flip, set_aside_reason wrong, group reassignment) | **VCVERSE** | Updates the specific `verse_context` row |
| Group description / anchor / dissolve | **VCGROUP** | Updates `verse_context_group` |
| Term needs deletion / status change (extraction anomaly) | **REPAIR** | Updates `mti_terms.status` |
| Term needs full re-classification | **VCREVISE** with explicit "to_revise" flag | Same as today's flow |
| Concept-level / boundary issues for downstream attention | **VCSBFLAGS** raising SB_FINDING | Already in active use |
| Registry-level coherence problem | **REPAIR** + `verse_context_status` reset (the Q12 path) | Already in active use |

**All these patch types already exist and are applicator-supported.** The pivot doesn't require new instrumentation — it changes when they fire (analysis-time, not pre-analysis-time).

### 3.4 What stays unchanged

- **The 6 reset registries** (compassion, fellowship, forgiveness, grace, love, mercy) still get explicit Q12-mandated re-classification. Pivot does not apply to them.
- **NULL/excluded registries** stay excluded. Pivot is silent on them.
- **VC instruction v3_10** remains the contract for *new* VC work (the reset registries, FRESH terms, partial-completion gaps). Pivot doesn't touch the spec — it changes when it's invoked.
- **The applicator** is unchanged. All patch types continue to work as today.
- **Quality flags** (PH2_*, SB_FINDING, evidence flags) continue to be raised + resolved on the same patterns. The pivot makes them more important, not less — they are now the primary signal for analysis-driven corrections.

---

## 4. Cost / benefit / risk

### 4.1 Cost saved

| Item | Strategy v1 | Strategy v2 |
|---|---|---|
| Classifier batches for legacy bucket | ~120 | 0 |
| CC batch-prep cost | ~120 sessions of session_a per-term renders | 0 |
| Patch application cost | ~120 patches | analysis-driven (estimate <30 over the programme lifetime, based on today's signal density) |
| Researcher review cycles | ~120 | <30 |

Order-of-magnitude saving on VC-pipeline work for the legacy bucket: **~75% of remaining VC effort eliminated.**

### 4.2 Benefit captured

- Analysis cycles arrive sooner — Session B work is no longer gated on per-term VC for the legacy bucket.
- Real quality issues are surfaced *in the context that needs them*, with the analytical lens already engaged. A Session B classifier reading a registry's verses in a thematic frame will catch grouping/relevance problems faster than a VC classifier reading them in isolation.
- The two SB findings raised by VCB-Q01 today (apistia / spoudē fragmentation) are exactly this pattern — the *VC* classifier said "these are correctly classified" while *Session B* would say "these groupings are too fine for downstream consolidation." Session B was always going to be the right place to catch that.

### 4.3 Risks and mitigations

| Risk | Mitigation |
|---|---|
| **Legacy classifications use older grouping doctrine.** Pre-v3 work didn't enforce the "characteristic-perspective grouping" rule of v3_10 §6.2 Step 3. Some legacy groups may be too broad or too narrow by current standards. | (1) Today's evidence (84% NO-CHANGE on the very dimension that v3_10 was tightened on) shows this risk is small in practice. (2) When Session B encounters a problematic legacy group, VCGROUP patches handle it surgically. (3) The 25-term window dipping to 76% NO-CHANGE is real but represents 6 revisions across 25 terms — manageable through pinpoint correction, not bulk re-eval. |
| **Audit trail risk: mixing v3-confirmed and pre-v3-legacy work.** Future analysis may ask "was this registry's VC done under v3?" and need to distinguish. | `mti_terms.vc_status` IS the audit field. `not_done` = legacy, `vc_completed` = v3-confirmed. The field stays accurate under the pivot. Reports / extracts can filter on it. |
| **Session B sees more quality issues than its protocol expects.** If 16% of terms have something to revise, Session B sessions will more often fork into VC-correction patches. | Session B already has the patch-correction routing established (the four-patch model + REPAIR). Volume of analysis-stage corrections is bounded by today's evidence (~8-15% of terms touch any change). |
| **VCCONFIRM design effort wasted.** v1 strategy §4.1 listed VCCONFIRM as a future patch-type to design. Pivot makes it unnecessary. | No code was committed; no instructions amended. Design discussion archived in v1 strategy doc. Net cost of obsolescence: zero. |
| **Some registries may have systemic issues that are easier to catch in pre-analysis VC than in mid-analysis Session B.** | Counter-evidence: today's diligence/H4639/Outlier-1 fixes were all caught by focused scans, not by per-term VC. The signal-targeted scan is a better detector than per-term re-classification. We can keep the scan as a preflight tool — see §6 below. |

### 4.4 Bounded by triggers

The strategy v1 §6 trigger conditions remain, with rewording for v2:

| Trigger | v2 response |
|---|---|
| Multiple unrelated registries showing the same downstream Session B / Session C / DimReview issue (systemic legacy error) | Stop and re-evaluate the pivot; consider a targeted re-classification pass on the affected pattern |
| A revised group or verse later found wrong (revision was the error, legacy was correct) | Single-instance correction; if pattern, re-evaluate |
| Downstream stages report classification gaps at >X% rate | TBD threshold; provisional 15% |

If any of these fire, v2 is itself revised — same self-correcting loop as v1.

---

## 5. Migration plan

If approved, the pivot rolls out in three steps:

### Step 1 — Strategy v1 → v2 supersede

- Mark `vc-corrective-strategy-v1-20260425.md` as superseded; cross-reference v2.
- Issue `vc-corrective-strategy-v2-20260426.md` based on this proposal (with any researcher edits from review).

### Step 2 — Session B readiness gate edit

- `wa-sessionb-analysis-readiness` minor bump (current v1_6 → v1_7).
- New gate spec accepts legacy-Complete with `vc_status='not_done'` provided the caveat declaration is made at session start.
- Companion: brief addition to the classifier handoff note documenting the new posture declaration.

### Step 3 — Optional pre-flight scan tool

To capture today's lesson (focused scans are better signal-detectors than per-term VC), retain a periodic outlier-scan utility:

- Adapts the queries used in today's outlier scan into a scheduled or on-demand check.
- Run before each Session B session on a registry, OR run programme-wide every N weeks.
- Output: a short list of statistical outliers (1-group lumping, high % set_aside, anomaly-pattern term-glosses) with quick triage labels.
- Each outlier confirmed as real → REPAIR / VCGROUP / VCVERSE patch.

This is a small enhancement, not part of the core pivot. Can be deferred or skipped.

---

## 6. What the pivot does NOT replace

- **Session B Stage 1 readiness checks** that AREN'T about VC: data-integrity flags, schema-conformance, dimension-review status, B-target status — all stay as hard gates.
- **The four-patch model** (VCNEW, VCREVISE, VCSBFLAGS, VCSDPOINTERS) — stays in active use for new VC work.
- **The per-term Session A `.md` renderer** (`build_session_a_prose.py`) — stays in active use, especially for the reset registries and any analysis-driven full-term re-eval.
- **The version gate (A-03)** — stays. Whatever VC work IS done continues to be version-anchored.

The pivot is narrow: it changes how the **legacy-Complete bucket** is handled. Everything else continues.

---

## 7. Open questions for researcher decision

1. **Approval of the pivot itself.** Is the evidence sufficient? Is the cost-benefit case compelling enough to commit? Today's data is strong but the sample is still <100 terms; if you want one more rolling batch (VCB-15) before committing, that's a defensible pre-condition.
2. **Caveat acknowledgement language** — what exactly does the Session B classifier declare? Draft text in §3.2 above is a starting point; you may want it shorter / more formal / less.
3. **`vc_status='not_done'` semantics for legacy registries** — under the pivot this stays, indefinitely, for ~1,800 terms. Acceptable as a permanent signal, or do you want a new `vc_legacy_accepted` value to distinguish "not done and won't be" from "not done and pending"? The latter requires a small migration.
4. **Treatment of the ledger.** v1 strategy §5 Step 1 (the empirical ledger build) has produced N=56. Continue refreshing per batch (~30 min cost), or freeze it as evidence for the v2 decision and stop maintaining? My view: refresh once at N=73 (post-VCB-014/Q01), then freeze.
5. **VCCONFIRM design discussion in strategy v1 §4.1** — drop entirely from v2, or keep as "considered and rejected with reason"? My view: keep the rejection rationale, since it's part of the audit trail of the strategy decision.
6. **Pre-flight outlier-scan tool (§5 Step 3)** — build it, defer it, or skip it? My view: build it lightweight (a single script). It costs little and captured today's real fixes.

---

## 8. Comparison summary

| Dimension | Strategy v1 (current) | Strategy v2 (pivot, proposed) |
|---|---|---|
| **Default for legacy bucket** | Re-classify per-term under v3_10 | Use as-is, qualify during analysis |
| **Patch types in default flow** | VCREVISE (mostly NO-CHANGE) | VCGROUP / VCVERSE / VCSBFLAGS (analysis-driven) |
| **Session B readiness gate** | Hard `vc_completed` requirement | Accepts legacy-Complete with caveat |
| **Cost trajectory** | ~120 batches × ~classifier-session each | ~analysis-stage-bounded; today's signal: <30 patches estimated |
| **Audit field** | `vc_status='vc_completed'` after pass | `vc_status='not_done'` for legacy (accurate; conveys "no v3 pass run") |
| **Statistical assumption** | NO-CHANGE rate ≥80% required | NO-CHANGE rate sufficient as evidence; not a gate |
| **Trigger to revisit** | NO-CHANGE rate < 80% | Systemic downstream issues |
| **Reset registries (Q12)** | Full reclassification | **Same — full reclassification** |
| **NULL/excluded registries** | Excluded | **Same — excluded** |
| **VCCONFIRM design effort** | Pending (Step 5 of v1 §5) | Not needed |
| **Empirical ledger** | Live document | Frozen evidence-of-decision |

---

## 9. What to do next

If the proposal is acceptable in shape:

1. **Researcher approval** of the pivot (this document).
2. **Issue `vc-corrective-strategy-v2-20260426.md`** based on this proposal (with edits from review).
3. **Draft `wa-sessionb-analysis-readiness v1_7`** with the new gate spec + caveat-declaration template.
4. **Mark relevant tasks.md entries** as superseded by the pivot:
    - "VC programme roll-out: 174 legacy-Complete registries..." → superseded; replace with "Legacy-Complete bucket accepted as Session B input under v2 pivot."
    - "VCCONFIRM patch-type design (Step 5 of strategy)" → cancelled; reason: pivot.
    - "VC revision-ledger build (Step 1 of strategy §5)" → freeze; preserve as evidence-of-decision.

If the proposal is not acceptable, this document stays as the v1.1 update to the strategy doc — recording what was considered and why a different course was taken.

---

*Drafted 2026-04-26 by Claude Code under researcher direction. Not yet approved. No DB or contract changes implied. Successor document if approved: `vc-corrective-strategy-v2-20260426.md`.*

Researcher comments:
I agree that we must move forward without going through a reclassification of all the verse contexts.  The risk of making analytic errors without the opportunity to re-consider the outcome during analytics is manageable.
The Analytic readiness should not block on the basis of VCs not completed.
The .md that is generated as an output of Analytic reading must explicitly highlight the terms where there are unverified verse contexts.  These terms should get special treatment during analysis to assess if the potential impact on the analysis would result in a misplaced finding.
If a key finding is affected, then the Analytic-output session should raise a flag of further research required based on the potential impact of the classification gaps of the term.

I am comfortable that this approach can work based on a key change brought into the process.  This is that the input into the Analytic-output phase changes from a database record where AI need to assemble the data and trip over all the ifs and buts - to a .md document that presents the data available as available facts and request the AI to analyse it, rather than question the data.

The validation of the Analytic readiness phase, and the output of this phase into the creation of the .md becomes the key to success.

Did that answer all the questions regarding this strategy.

Actions include (although CC need to add the technical layer of actions):
a) update the programme prose to capture this change
b) Check and update Dimension review to accept incomplete verse contexts. The check should be that the terms that have incomplete verse contexts are not material in the classification of the word.
c) Check and update Analysis-readiness to modify the instruction to cater for the incomplete verse contexts and not block progress on it.
d) carefully craft the Analysis-readiness output to serve as the sound base for analysis. This output must also go into the prose.
e)craft the filters for Analysis-output to read from the prose, and deal with the incomplete verse context handling, if material.


---

## 10. Technical layer for the action plan (CC response, 2026-04-26)

The researcher's refinement is significant: it shifts the load-bearing gate from a *binary VC-status check* to **a structured `.md` handoff between Analytic-readiness and Analytic-output**. The `.md` is the artefact that:

- presents the data as **available facts** (not as a gating threshold),
- explicitly **catalogues unverified-VC terms** so the analyst can apply extra scrutiny where it matters,
- moves **materiality judgement to the analytical stage**, where the analytical lens is engaged.

This is a stronger design than the caveat-declaration model in §3.2 of this proposal. The technical layer below replaces §3.2's "declare aloud" approach with a "structured `.md` handoff" approach.

### 10.1 Programme prose update (researcher action a)

Two prose sections need amendment; both go through the standard prose-supersede pipeline (`prog_instr_*` family in `prose_section`).

| Section handle | Current version | New version | Change |
|---|---|---|---|
| `prog_instr_verse_context` | v3 | v4 | Add a governance paragraph: "The programme accepts legacy-Complete VC classifications as analysable input. Per-term v3 re-classification is reserved for the 6 reset registries (Q12) and for terms surfaced by analysis-stage findings. The `vc_status='not_done'` field is the audit signal for legacy-state terms." |
| `prog_instr_session_b_readiness` (new section if absent) OR `prog_instr_session_b` | tbd | new / minor | Document the `.md` handoff: the readiness output is the canonical input for Analytic-output. Analytic-output reads the `.md` as facts; the database is consulted for verbatim verse text only. |

**Cost:** small. Both edits are governance-level prose, not analytical content. Same pipeline as past prose-supersede patches (PROSE patch type via `apply_session_patch.py`).

### 10.2 Dimension review acceptance (researcher action b)

`wa-dimensionreview-instruction` (current v3_3 — let me verify before drafting) needs:

- **Acceptance clause:** dim-review accepts registries where some OWNER terms have `vc_status='not_done'`.
- **Materiality check:** for each cluster's classification work, the dim-review classifier identifies whether any unverified-VC term is **material to the dimensional classification** (i.e. its weight in the SBQ scoring, or its role as an anchor of the dimensional concept). The "material" test: would the dimension classification change if this term's VC were redone and produced different groupings/anchors?
- **Output flag:** if material → the dim-review output flags that registry's dimension classification as "VC-dependent" with a specific list of which terms drove the dependency. This becomes a SD_POINTER or new flag-type; route it to Session D for follow-up if pointer-pattern, else to Session B for analytical correction.
- **Non-material default:** if not material → proceed normally; record the unverified-VC presence in the dim-review note for audit but no action needed.

**Bump:** v3_3 → v3_4 (per GR-FILE-003).

### 10.3 Analysis-readiness gate (researcher action c)

`wa-sessionb-analysis-readiness` (current v1_6) — minor bump to v1_7. Specific edits:

- **Replace the hard VC gate** ("all OWNER terms must be vc_completed") with a **structural gate**: the readiness output `.md` must catalogue every OWNER term with its vc_status, and explicitly list `vc_status='not_done'` terms in a dedicated "Legacy-VC terms" section.
- **Stage 1 pass criterion** becomes: the `.md` is well-formed (no missing terms, no orphan verse_context rows, no dimension-review-blocking flags) — *not* "all terms vc_completed".
- **Add §X "VC source classification"** documenting:
  - `vc_completed`: classified under v3_x contracts; trusted as accurate within the v3 grouping doctrine.
  - `not_done` (legacy-Complete registries): classified under pre-v3 contracts; presented as facts to analysis; subject to materiality-driven escalation.
  - `to_revise` (the 6 reset registries): out of scope for routine readiness — these are blocked from Stage 2 until reclassified per Q12.
- **Caveat removed.** No verbal declaration. The `.md` carries the discipline.

### 10.4 Analysis-readiness output design (researcher action d)

This is **the load-bearing artefact**. Per registry, output filename: `wa-{NNN}-{word}-readiness-output-v{n}-{YYYYMMDD}.md`.

Proposed structure (subject to refinement):

```markdown
# Registry NN word — Analysis Readiness Output (v{n})

## 1. Registry overview
- session_b_status, dim_review_status, cluster_assignment, BANKED status,
  inference_note, word_synopsis (researcher fields preserved verbatim)

## 2. Term inventory (OWNER, all)
- Each term: strongs, gloss, language, status, **vc_status (PROMINENT)**,
  md_version, verses (active/deleted), groups (active/dissolved), vc_rows
  (relevant/set_aside), prior SB findings on this term
- Sorted by analytical weight (high-verse-count + multi-group + flagged first)

## 3. Legacy-VC terms — UNVERIFIED UNDER v3 CONTRACTS
- Dedicated section listing every term with vc_status='not_done'
- Per term: existing groups + verse classifications presented as "facts on the
  ground"; classification quality NOT independently re-assessed
- **Analytical instruction (for Analytic-output):** "These classifications are
  legacy. Treat as the available state of evidence. If during analysis you
  conclude a finding depends materially on a verse or group from this list,
  raise a 'further research required' flag specifying the term, the verses,
  and the alternative classification that would change the finding."

## 4. v3-confirmed terms
- Terms with vc_status='vc_completed': trusted within v3 grouping doctrine.

## 5. Cross-registry context
- XREF terms, SD_POINTERs, cluster siblings.

## 6. Open flags carried forward
- Unresolved PH2_*, SB_FINDING, PH2_DATA_QUALITY etc. with disposition note.

## 7. Verbatim verse text
- All active verses for all OWNER terms, grouped by term, with the existing
  group_code and is_relevant indicator. This is the analyst's primary text
  source — no need to re-fetch from STEP or re-query the DB.

## 8. Readiness verification
- Stage 1 checks: all hard gates pass (data integrity, dim review,
  B-target). Stage 2 readiness asserted.
- Generated timestamp and DB md_version snapshot.
```

The structure is deliberately verbose. The whole point is that Analytic-output should **never need to query the DB or trip over data-shape questions** — the `.md` is the answer.

**Generation:** new script (or extension to existing `build_session_a_prose.py` / `build_complete_extract.py`). Runs once per registry at the start of Stage 2.

**Storage:** The `.md` itself can be stored in the prose store (`prose_section` table, new section type `sb_readiness_output_{NNN}` or similar) so it's queryable and version-tracked. Researcher action d says "this output must also go into the prose" — the prose-store mechanism is the canonical home.

### 10.5 Analysis-output filters (researcher action e)

`wa-sessionb-analysis-output` (current v1_1) — minor bump.

- **Input source change.** Primary input is the readiness `.md` (or its prose-store equivalent), not the database. The DB is consulted only for verbatim verse text retrieval if not already in the `.md` (per §10.4 the .md should carry full verse text, so DB consultation should be rare).
- **Materiality protocol.** For each finding the analyst produces:
  1. Identify the source terms / verses underlying the finding.
  2. Check: is any source a "Legacy-VC term" (per the `.md` §3 list)?
  3. If yes → assess materiality: would the finding change if the classification of those source verses/groups were different? Document the assessment.
  4. If yes AND materiality is high → emit a `FURTHER_RESEARCH_REQUIRED` flag (new flag-type or use `PH2_DATA_QUALITY` with a specific subtype) with: source term(s), source verses, the alternative classification scenario, and the predicted change to the finding.
  5. If yes AND materiality is low → record the source-term flag in the finding's audit trail but proceed normally.
- **No escalation for v3-confirmed terms.** Findings sourced only from `vc_completed` terms get no extra step.

**Bump:** v1_1 → v1_2.

### 10.6 New flag type (or repurpose) — `FURTHER_RESEARCH_REQUIRED`

If we go with a new flag-type (recommended for clarity, vs overloading PH2_DATA_QUALITY):

| Field | Value |
|---|---|
| `flag_code` | `ANALYSIS_VC_UNVERIFIED_MATERIAL` (or similar — clearer than `FURTHER_RESEARCH_REQUIRED` which is too generic) |
| Carrier table | `wa_session_research_flags` (existing) |
| Source session | Session B output |
| Resolution path | (a) reclassify the source term under v3 if the finding is genuinely changed by it, OR (b) the finding is robust to the classification uncertainty and the flag is documentation only. Researcher decision per case. |

### 10.7 Net cost summary

| Layer | Cost | Risk |
|---|---|---|
| 10.1 Prose updates | 1 patch (PROSE) | Low |
| 10.2 Dim-review instruction v3_3→v3_4 | doc edit + minor classifier protocol change | Low — already supports flag emission |
| 10.3 Readiness instruction v1_6→v1_7 | doc edit | Low — replaces hard gate with structural gate |
| 10.4 Readiness output `.md` design | new generator script + prose-store integration | **Medium — load-bearing; warrants careful design + a pilot run on one registry before programme rollout** |
| 10.5 Analysis-output instruction v1_1→v1_2 | doc edit | Low |
| 10.6 New flag type | 1 schema migration (small) + applicator extension | Low |

Total programme cost: **a few documents + one new script + one schema migration**. Bounded; no DB-wide rewrites.

---

## 11. Open questions revisited (researcher response 2026-04-26)

| Q | Original (§7) | Researcher response | Status |
|---|---|---|---|
| 1 | Approval of the pivot? | "I agree we must move forward without going through a reclassification of all the verse contexts. The risk is manageable." | **Approved** |
| 2 | Caveat acknowledgement language? | Replaced by §10.4 `.md` mechanism — explicit listing in readiness output, no verbal declaration needed. | **Approved (better mechanism)** |
| 3 | `vc_status='not_done'` semantics? | Implicit: stays as the audit signal; no new value needed. | **Settled** |
| 4 | Ledger treatment? | Not directly addressed. | **Open** — CC recommends: refresh once at N=73, then freeze as evidence-of-decision. |
| 5 | VCCONFIRM design discussion drop? | Implicit: drop. Pivot makes it unnecessary. | **Settled** — drop from v2; v1 retains the rejection rationale for audit. |
| 6 | Pre-flight outlier-scan tool? | Not directly addressed. | **Open** — CC recommends: build lightweight (single script). Today's signal-detection insight is independent of the .md mechanism and worth keeping. |

Two items still open (4 and 6). Both have CC default recommendations; if researcher accepts both defaults, no further input needed.

---

## 12. Proposed execution order (CC recommendation)

If the technical layer above is acceptable in shape:

1. **Issue `vc-corrective-strategy-v2-20260426.md`** as the canonical strategy doc. Captures the pivot + technical layer in researcher-facing form. Supersedes v1.
2. **Pilot `.md` readiness-output design on one registry** (suggest: a clean v3-confirmed registry like 067 goodness or 092 integrity — already at vc_completed, so the legacy-VC section will be empty; tests the structure without confusing variables).
3. **Iterate on the `.md` structure** based on the pilot. Get the shape right before scaling.
4. **Run a "mixed-state" pilot** on one legacy-Complete registry (suggest: 020 character — recently advanced to vc_completed in VCB-014, so its terms are at md_version=2 and the legacy section will be small/empty as a control; or pick a registry with mixed vc_status to test the legacy-VC section properly — e.g. 094 intercession with 4 terms now at vc_completed and partial-completion gaps).
5. **Edit the four instruction docs in parallel** (10.1 prose, 10.2 dim-review, 10.3 readiness, 10.5 analysis-output) once the `.md` shape is settled.
6. **Schema migration for the new flag-type** (small, low risk).
7. **Cut over the programme** — formally accept legacy-Complete bucket as Session B input.

Steps 1, 2, 3 are the load-bearing path. Steps 4-7 follow from them.

