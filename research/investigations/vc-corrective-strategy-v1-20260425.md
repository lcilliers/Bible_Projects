# VC Corrective Action Strategy — planning document

**Doc version:** v1
**Date:** 2026-04-25
**Author:** Claude Code (drafted under researcher direction)
**Status:** Living document. Update statistical assumptions and decision triggers as evidence accumulates. Bump minor version on substantive edit (`v1_1`, `v1_2`, …); bump major version on strategy pivot (`v2`).
**Tracked in:** `tasks.md` → "VC corrective action strategy"

---

## 1. Position

The current rolling pattern (VCB-7..11) is full per-term re-evaluation under v3_9 contracts of every legacy-Complete registry. The accumulating evidence is that the vast majority of legacy classifications come back **NO-CHANGE** — only a small minority require any revision.

**Researcher position (2026-04-25):** Avoid full re-classification of the entire backlog. It is expensive, and the empirical risk of leaving correct legacy classifications in place is low. When analysis surfaces specific groups or verses as suspect, revisit them **pinpointedly** using the existing VCGROUP / VCVERSE patch types — not the bulk per-term VCREVISE path.

**Implication:** the corrective-action strategy must be evidence-driven, signal-targeted, and avoid bulk reclassification. Existing surgical patch types (VCGROUP, VCVERSE) are the primary delivery mechanism for revisions; a new lighter-touch advancement path may be needed for the bulk of low-risk terms (provisionally **VCCONFIRM**).

---

## 2. Pending-term stratification (snapshot 2026-04-25)

Total pending OWNER terms: **2,497**

| Stratum | Count | % | Treatment |
|---------|------:|--:|-----------|
| Legacy-Complete RE-EVAL (prior rows fully cover active verses) | 1,390 | 56% | **Lighter-touch candidate** — bulk of the backlog. Strategy applies primarily here. |
| Partial-completion (prior rows + missing verses) | 748 | 30% | VCNEW for missing verses only. No shortcut for the gap; existing rows can be lighter-touch confirmed if no risk signal. |
| True FRESH (no prior verse_context rows) | 233 | 9% | Full classifier review required. No lighter-touch path applicable. |
| Reset registries (`vc_status='to_revise'`, the 6 reset registries) | 126 | 5% | Researcher decision Q12 (2026-04-19) was explicit re-classification under v3_9. No shortcut. |

**The lighter-touch strategy targets the 1,390 (and the prior-rows portion of the 748) — about 1,800 of the 2,497 pending terms.**

---

## 3. Statistical assumptions (v1 — to be revised as evidence accumulates)

### 3.1 NO-CHANGE rate (primary assumption)

Estimate from VCB-7..11 outcomes: **~93% of legacy-Complete RE-EVAL terms return NO-CHANGE on full re-evaluation.**

- Sample: ~30 terms across VCB-7..11 (renewal pilot + VCB-8 + VCB-9 + VCB-10 + VCB-11).
- Confidence: low (small N). Worth re-validating after every batch.
- Source patches:
  - VCB-9 VCREVISE: 8 NO-CHANGE + 1 REVISE-ONLY (defilement family + indignation)
  - VCB-10 VCREVISE: 2 NO-CHANGE confirmation entries
  - VCB-11 VCREVISE: 11 NO-CHANGE empty-ops + 1 REVISE-ONLY (mti=917 G1761 group description sharpening)

If the assumption holds, applying lighter-touch to the 1,390 legacy-Complete RE-EVAL terms saves the cost of ~1,290 full classifier reviews while accepting ~100 untouched legacy errors that pinpoint analysis can later catch.

### 3.2 Revision shape (when revision happens, what kind)

Observed revisions to date: **description sharpening dominates.** Group dissolves and anchor swaps are rare. Verse-level reclassifications (is_relevant flips) are rare. New group creation is rare in RE-EVAL.

- VCB-9 indignation revision: dropped a "burning of suffering" clause that didn't survive the v3_9 §3 term-level filter.
- VCB-11 G1761 enthumēsis revision: description re-shaped to centre the inner-being characteristic (cognition + heart-content perception) rather than a term-centric phrasing.

Both fit the "characteristic-perspective grouping" doctrine in v3_9 §6.2 Step 3. Both are surgical edits, not group rebuilds.

### 3.3 Partial-completion incidence

Observed in **~25%** of recent batches (4 of 16 audited cases — 916, 1364, 5111 in VCB-11; plus 884, 934, 6065, 1221 in the VCB-13 candidate set; plus 5111 partial actually tracked above).

Partial-completion is mostly the result of post-VC `audit_word` re-runs adding verses the original VC pass never returned to cover. **Cannot be skipped** — VCNEW for the missing verses is mandatory. Existing rows in partial-completion terms are still subject to the NO-CHANGE rate hypothesis above.

### 3.4 Predictive signals (HYPOTHESES — NOT YET TESTED)

Each of the following is a candidate predictor of revision-need. **None has been empirically validated.** The first analysis pass (Step 1 of §5 below) will score each.

| Signal | Hypothesis | Mechanism |
|--------|------------|-----------|
| Active group count > 5 | Higher revision risk | Fragmentation — groups likely too narrow; consolidation candidate |
| Single-group terms with high verse counts | Higher revision risk | Lumping — groups likely too broad |
| Property terms (per v3_9 §6.2 Step 3) | Higher revision risk | More prone to term-centric vs. characteristic-perspective drift |
| Existing `set_aside_reason` gap (notes-but-no-reason) | Vocab revision needed | Direct evidence of legacy vocab-discipline lapse |
| Term carries prior SB_FINDING / PH2 flag | Higher revision risk | Already flagged for attention |
| Registry has unresolved dimension flags | Higher revision risk | Registry-level pattern of methodology drift |
| 1-group + low verse count (≤3) | Lower revision risk | Trivial / hapax — limited surface for error |
| Hebrew vs. Greek | Probably orthogonal | Cheap to test, may be surprising |

### 3.5 Cost model

- **Status quo (full re-eval of 1,800 terms):** ~120 batches at ~15 terms/batch. Each batch = one classifier session + CC apply + post-validation.
- **Lighter-touch path (10% revision rate, classifier reviews only the suspect 180 terms):** ~12 batches of revisions + 1 bulk metadata advance for the cleared 1,620 terms.
- **Net saving:** roughly 100+ classifier sessions if assumptions hold.

---

## 4. Corrective-action pathways (proposed)

Three pathways, picked per-term based on signals:

### 4.1 VCCONFIRM (new, design candidate)

Bulk advancement of low-risk terms to `vc_completed` + `md_version` bump **without classifier review**. Patch type to be designed. Carries:

- `terms_covered`: list of mti_term_ids
- `input_versions`: per-term md_version map (must match DB at apply time)
- `confirmation_basis`: signal-set that justified inclusion (e.g. "1-group ∧ verse_count ≤ 3 ∧ no_prior_flag")
- `operations`: empty (advancement is metadata-only)
- Applicator semantics: same A-03 version-gate, same per-term aggregation, but no `verse_context*` row writes.

**Open design questions:**

- Does VCCONFIRM need an instruction-doc amendment (likely yes — a new §7.9.x and a new §15 entry in the patch instruction)?
- Does it need explicit researcher sign-off per batch, or can it proceed automatically once signal thresholds are met?
- How do we record the confirmation basis for audit (a `notes` column on `mti_terms.vc_status_note` perhaps)?

### 4.2 VCGROUP / VCVERSE (existing, repurposed for pinpoint corrections)

Already supported in the applicator. When analysis surfaces a specific suspect group or verse:

- **VCGROUP** for description sharpening, group dissolve, anchor swap. Single op, surgical.
- **VCVERSE** for individual verse reclassifications (is_relevant flip, set_aside_reason vocab fix, group reassignment).

These are already documented in v3_9 §8 and §9. No instruction change needed; just need to start using them more directly instead of routing everything through VCREVISE.

### 4.3 VCREVISE (existing, used selectively)

When a term has multiple suspect groups or systemic issues that a surgical patch can't cleanly express, fall back to full per-term VCREVISE. Same as today, but applied only to terms flagged by signal scoring.

---

## 5. Operational steps (what we'll actually do)

### Step 1 — Build the empirical ledger (next concrete action)

Read VCB-7..11 patches + DB. For every term in those batches, record:

```
(mti_term_id, batch_id, routing, registry_no, language, group_count_pre,
 verse_count_active, term_owner_type, prior_set_aside_gap,
 prior_sb_flag, prior_ph2_flag, dim_flag_on_registry,
 single_group_high_verse_flag, outcome)
```

Where `outcome ∈ {NO-CHANGE, REVISE-DESC, REVISE-DISSOLVE, REVISE-ANCHOR, REVISE-VERSE, MIXED, NEW-ONLY}`.

Output: `outputs/investigations/vc-revision-ledger-v1-{date}.md` + companion CSV.

Intent: surface univariate predictors. With ~30 terms the bar is low — only strong signals (e.g. "every term with >5 groups was revised") would survive at this N. Weak signals are recorded but not acted on.

### Step 2 — Validate predictors as N grows

Continue regular VCB rolling (one batch / few days) and append each new batch's outcomes to the ledger. Re-score predictors at each increment of ~25 terms. Aim for ~100 terms before concluding.

### Step 3 — When a predictor is reliable

Promote it to a *signal triage rule*. Encode in batch composition (the batch-prep step in CC's flow): the lighter-touch terms get listed for VCCONFIRM (once VCCONFIRM exists), the suspect terms get listed for full VCREVISE.

### Step 4 — Pinpoint corrections

When ledger analysis or downstream stages (Session B, Dimension Review) surface a specific suspect group / verse, schedule a VCGROUP or VCVERSE patch. Record in `tasks.md` with reference to the surfacing source.

### Step 5 — VCCONFIRM design (after Step 2 + 3 establish ≥1 reliable signal)

Draft VCCONFIRM specification. Includes patch instruction amendment (§15 new entry), applicator extension, instruction-doc note in `wa-versecontext-instruction`. Pilot on a single low-risk batch (e.g. 50 terms with the cleanest signal profile) before bulk roll-out.

---

## 6. Decision triggers (when to revisit this strategy)

The strategy is conditional. If any of the following surface, **stop and re-evaluate before continuing on the lighter-touch path**:

1. **NO-CHANGE rate falls below 80%** in any ~20-term window. The ~93% assumption is the load-bearing assumption; if it weakens materially the lighter-touch path is no longer safe.
2. **Systemic legacy errors surface** — e.g. multiple unrelated terms in different registries showing the same misclassification pattern. This implies an instruction-era methodology drift, not random per-term variance, and requires a different (bulk audit-and-fix) intervention.
3. **A revised group or verse is later found wrong** — i.e. the legacy classification was correct and the v3_9 revision was the error. This would invalidate the "v3_9 reclassification is more accurate" implicit assumption that justifies the whole programme.
4. **Downstream stages (Session B, Dimension Review, Session C) report classification gaps** at a rate that suggests pinpointing isn't catching enough errors.

Each trigger event lands a v1.X update to this document with the observed evidence and the decision taken (continue, pivot, pause).

---

## 7. Cost / risk stance (formal)

**Cost** (status quo): high — proportional to pending-term count, ~120 sessions for the legacy-Complete bucket alone, plus partial-completion and FRESH workloads on top.

**Risk** (lighter-touch): bounded — proportional to (1 - NO-CHANGE-rate) × (impact of an undetected error). Empirical evidence so far: NO-CHANGE rate ≈93%, revisions are mostly description sharpenings (low downstream impact when missed). Risk dominates only if the rate drops or the revision shape changes.

**Position:** The cost saving is large, the risk is bounded and observable, the trigger conditions in §6 catch the failure modes. Therefore the lighter-touch path is the preferred default once a reliable predictor exists, with pinpoint corrections as the primary correction mechanism.

---

## 8. Open questions to resolve before committing to the strategy

1. **Reset-registry treatment.** The 6 reset registries (compassion, fellowship, forgiveness, grace, love, mercy — 126 terms) carry an explicit researcher decision (Q12 2026-04-19) to re-classify. Does the lighter-touch path apply to them or are they categorically excluded?
2. **VCCONFIRM patch-type design.** Confirm scope, semantics, applicator behaviour, instruction-doc amendments. Pilot scope.
3. **Audit trail.** What's the durable record that a term was advanced via VCCONFIRM rather than VCREVISE? Is `mti_terms.vc_status_note` sufficient, or do we need a dedicated audit table?
4. **Signal threshold.** How predictive does a signal need to be before it counts as "reliable"? Provisional answer: ≥90% precision on a held-out validation set of ≥30 terms (i.e. ≤10% of terms predicted-low-risk turn out to need revision when fully reviewed).
5. **Re-validation cadence.** How often do we sample lighter-touch-confirmed terms by sending them through full VCREVISE anyway, to keep the empirical NO-CHANGE rate honest? Provisional answer: ~5% re-validation sample per quarter.

---

## 9. Change log

- **v1 (2026-04-25):** Initial draft. Position recorded; statistical assumptions snapshotted at N=~30 terms; pathways and operational steps proposed. Ledger build (Step 1) is next concrete action.
