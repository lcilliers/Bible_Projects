# M38 audit against wa-sessionb-cluster-instruction-v2_5-20260518

**Date:** 2026-05-28 18:52
**Script:** `scripts/_audit_cluster_against_instruction_v25_v1_20260528.py`
**Instruction version checked against:** v2_5
**Cluster status at audit time:** 'Analysis Complete'
**Cluster version:** 'v6'

---

## §1 — Corrective-actions plan

**Plan verdict:** `BOUNDED-FIXES`

All actions are bounded surgical fixes. Existing cluster structure remains intact. Cluster status does not change (§17.5).

**Cluster corpus reference (denominators for scope):**
- relevant verse_context rows: 309
- term count: 13
- set-aside vc rows: 46
- existing cluster_finding rows: 1512

### Canonical cascade

1. **Phase 2** — Pass A meaning — author verse_context.analysis_note
2. **Phase 5/6** — Sub-group review — fit existing sub-group OR propose new
3. **Phase 7** — VCG review — fit existing VCG in target sub-group OR create new (with anchor)
4. **Phase 9/11** — Findings review — does the verse confirm / extend / contradict an existing finding, or open a new one
5. **Session C** — Publication review — re-publish any chapter whose cited findings substantively changed

### Actions (sorted by cascade entry step)

| # | Error type | Entry step | Count | Scope | Work | % of denominator |
|---|---|---:|---:|---|---|---|
| 1 | `forbidden_setaside` | 1 | 1 | bounded | small | 2% of set-aside verses |
| 2 | `missing_anchor` | 3 | 5 | bounded | small | 2% of relevant verses |
| 3 | `completeness_gap` | 4 | 1747 | bounded | very large | — |
| 4 | `ungrounded_finding` | 4 | 177 | bounded | large | 12% of cluster_finding rows |

### Per-action detail

#### Action 1 — `forbidden_setaside` (1 items, bounded)

**Cascade entry:** step 1
  (Phase 2 — Pass A meaning — author verse_context.analysis_note)

**Action pattern:** RESCUE candidate review — re-classify each as relevant under v2_5 §1.1 scope; if rescued, run Pass A + cascade. If confirmed set-aside, rewrite reason with §4.5.1-valid ground.

**Cascade steps that may apply:**
  - Step 1 (Phase 2): Pass A meaning — author verse_context.analysis_note — applies
  - Step 2 (Phase 5/6): Sub-group review — fit existing sub-group OR propose new — may apply (cascade may short-circuit)
  - Step 3 (Phase 7): VCG review — fit existing VCG in target sub-group OR create new (with anchor) — may apply (cascade may short-circuit)
  - Step 4 (Phase 9/11): Findings review — does the verse confirm / extend / contradict an existing finding, or open a new one — may apply (cascade may short-circuit)
  - Step 5 (Session C): Publication review — re-publish any chapter whose cited findings substantively changed — may apply (cascade may short-circuit)

**Notes:** Strong RESCUE candidates — the original reason is bias-flagged.

**Sample affected entities:**
- G4991 soteria Act 27:34 (vc=66071)

---

#### Action 2 — `missing_anchor` (5 items, bounded)

**Cascade entry:** step 3
  (Phase 7 — VCG review — fit existing VCG in target sub-group OR create new (with anchor))

**Action pattern:** Designate one relevant verse of the term as is_anchor=1

**Cascade steps that may apply:**
  - Step 3 (Phase 7): VCG review — fit existing VCG in target sub-group OR create new (with anchor) — applies
  - Step 4 (Phase 9/11): Findings review — does the verse confirm / extend / contradict an existing finding, or open a new one — applies
  - Step 5 (Session C): Publication review — re-publish any chapter whose cited findings substantively changed — applies

**Notes:** Surgical — no cascade beyond Phase 7 anchor flag.

**Sample affected entities:**
- G2436 hileōs  (vc=None)
- G2433 hilaskomai  (vc=None)
- G4992 sōtērion  (vc=None)
- G1431 dōrea  (vc=None)
- G1434 dōrēma  (vc=None)

---

#### Action 3 — `completeness_gap` (1747 items, bounded)

**Cascade entry:** step 4
  (Phase 9/11 — Findings review — does the verse confirm / extend / contradict an existing finding, or open a new one)

**Action pattern:** Phase 9 micro-pass: author E (with verse evidence) / S (silent with rationale) / G (gap) for each missing cell; INSERT cluster_finding row

**Cascade steps that may apply:**
  - Step 4 (Phase 9/11): Findings review — does the verse confirm / extend / contradict an existing finding, or open a new one — applies
  - Step 5 (Session C): Publication review — re-publish any chapter whose cited findings substantively changed — applies

**Notes:** Phase 9 cell-by-cell completion. Researcher may opt to filter to v2_5 T0–T7 prompts if catalogue includes legacy codes.

**Sample affected entities:**
- C-001 × M38-A
- C-001 × M38-B
- C-001 × M38-C
- C-001 × M38-D
- C-001 × M38-E
- C-001 × M38-F
- C-001 × M38-G
- C-001 × CLUSTER

---

#### Action 4 — `ungrounded_finding` (177 items, bounded)

**Cascade entry:** step 4
  (Phase 9/11 — Findings review — does the verse confirm / extend / contradict an existing finding, or open a new one)

**Action pattern:** Read finding's source verses, add explicit verse references to finding_text. If genuinely a cluster-synthesis without specific verses, add sub-group references at minimum.

**Cascade steps that may apply:**
  - Step 4 (Phase 9/11): Findings review — does the verse confirm / extend / contradict an existing finding, or open a new one — applies
  - Step 5 (Session C): Publication review — re-publish any chapter whose cited findings substantively changed — applies

**Notes:** Phase 9 §15.2 check 1 compliance. No verse impact.

**Sample affected entities:**
- T0.1.3 × None
- T1.1.1 × None
- T1.1.3 × None
- T2.7.2 × None
- T2.2.3 × None
- T2.3.3 × None
- T2.5.3 × None
- T2.6.3 × None

---

## §2 — Legacy verdict (phase-restart framing)

**Level:** `MIXED`

**Recommendation:** Restart from Phase 7. Blocking findings cannot be repaired surgically. Advisory findings can be handled as surgical fixes either during the restart or before it.

**Restart-from-phase:** Phase 7

Per v2_5 §17.3.2, the cluster.status transition for this restart is:
  `Analysis Completed` → `Analysis - In Progress`

---

## §3 — Summary by check

| Check code | Count | Threshold | Severity | Section |
|---|---:|---:|---|---|
| `AUDIT-V25-STATUS-SUFFIX` | 0 | 1 | clean | §2.6 (status discipline) + cluster.status conventions |
| `AUDIT-V25-PIPELINE-INCOMPLETE` | 5 | 1 | blocking | §4 (Phase 1) + §5 (Phase 2) + §9 (Phase 6) + §10 (Phase 7) |
| `AUDIT-V25-BOUNDARY-PENDING` | 0 | 5 | clean | §11A (Phase 8.5) + §15.2 check 8 |
| `AUDIT-V25-FORBIDDEN-SETASIDE` | 1 | 10 | advisory | §4.5.1 (forbidden grounds for SET_ASIDE) |
| `AUDIT-V25-TERSE-SETASIDE` | 0 | 20 | clean | §4.5.1 (valid SET_ASIDE reasons require specific evidence ground) |
| `AUDIT-V25-BOUNDARY-PARKING` | 0 | 10 | clean | §8.4.1 (BOUNDARY is not a parking lot) |
| `AUDIT-V25-EVIDENCE-GROUNDING` | 177 | 5 | blocking | §15.2 check 1 (evidence-grounding) |
| `AUDIT-V25-COMPLETENESS` | 1747 | 5 | blocking | §15.2 check 2 (completeness) |
| `AUDIT-V25-REGISTER-FAMILIES` | 0 | 8 | clean | §1.1 + §8.4.1 |

---

## §4 — Per-check detail

### AUDIT-V25-STATUS-SUFFIX — cluster.status carries a post-closure suffix indicating un-processed additions

**Section reference:** §2.6 (status discipline) + cluster.status conventions
**Count:** 0
**Blocking threshold:** 1
**If blocking, restart from:** Phase 1

_Suffix indicates post-closure work that has not been folded through the pipeline. The pipeline-completeness check (§AUDIT-V25-PIPELINE-INCOMPLETE) will name the affected terms/verses._

No items found. Check is clean.

---

### AUDIT-V25-PIPELINE-INCOMPLETE — Pipeline-completeness gaps (Phase 1/2/6/7 outputs missing on relevant verses)

**Section reference:** §4 (Phase 1) + §5 (Phase 2) + §9 (Phase 6) + §10 (Phase 7)
**Count:** 5
**Blocking threshold:** 1
**If blocking, restart from:** Phase 7

Total gap items: 5

By category:
- missing_anchor: 5

By term (highest-gap-count first):
- G2436 hileōs (term_id=3166): {'missing_anchor': 1}
- G2433 hilaskomai (term_id=3176): {'missing_anchor': 1}
- G4992 sōtērion (term_id=4989): {'missing_anchor': 1}
- G1431 dōrea (term_id=6838): {'missing_anchor': 1}
- G1434 dōrēma (term_id=6846): {'missing_anchor': 1}

Sample affected items (first 5):
- missing_anchor: G2436 hileōs  (phase owner: 7) [relevant verses=1, anchor count=0]
- missing_anchor: G2433 hilaskomai  (phase owner: 7) [relevant verses=2, anchor count=0]
- missing_anchor: G4992 sōtērion  (phase owner: 7) [relevant verses=5, anchor count=0]
- missing_anchor: G1431 dōrea  (phase owner: 7) [relevant verses=9, anchor count=0]
- missing_anchor: G1434 dōrēma  (phase owner: 7) [relevant verses=1, anchor count=0]

---

### AUDIT-V25-BOUNDARY-PENDING — BOUNDARY_DECISION_PENDING flags unresolved

**Section reference:** §11A (Phase 8.5) + §15.2 check 8
**Count:** 0
**Blocking threshold:** 5
**If blocking, restart from:** Phase 8.5

No items found. Check is clean.

---

### AUDIT-V25-FORBIDDEN-SETASIDE — set_aside_reason matches §4.5.1 forbidden grounds

**Section reference:** §4.5.1 (forbidden grounds for SET_ASIDE)
**Count:** 1
**Blocking threshold:** 10
**If blocking, restart from:** Phase 1

_Pattern-based scan; researcher should read each flagged reason in context._

Total matches: 1 (showing first 1)

- vc=66071 Act 27:34 (G4991 soteria)
  matched: FB12: not spiritual
  reason: Soteria here means physical survival/bodily safety in a shipwreck context, not spiritual salvation — outside M38 salvation/atonement/gift scope.

---

### AUDIT-V25-TERSE-SETASIDE — Terse set_aside_reason values lack specific ground

**Section reference:** §4.5.1 (valid SET_ASIDE reasons require specific evidence ground)
**Count:** 0
**Blocking threshold:** 20
**If blocking, restart from:** Phase 1

_Terse values like 'physical_only' are borderline. Each verse should carry a verse-specific evidence rationale._

No items found. Check is clean.

---

### AUDIT-V25-BOUNDARY-PARKING — BOUNDARY parking-lot residue (STAYS-verdict terms with verses in BOUNDARY)

**Section reference:** §8.4.1 (BOUNDARY is not a parking lot)
**Count:** 0
**Blocking threshold:** 10
**If blocking, restart from:** Phase 5

No items found. Check is clean.

---

### AUDIT-V25-EVIDENCE-GROUNDING — cluster_finding E-coded rows with no verse / VCG / anchor reference

**Section reference:** §15.2 check 1 (evidence-grounding)
**Count:** 177
**Blocking threshold:** 5
**If blocking, restart from:** Phase 9

Checked 1349 E-coded cluster_finding rows; 177 ungrounded.

- cf.id=20580 (T0.1.3) sg=None status=finding
  text head: **[CHAR-3]** E — The corpus is silent on God exercising faith as an inner faculty (see T0.1.2 and T0.3.2). This silence is structurally significant rather than 
- cf.id=20584 (T1.1.1) sg=None status=finding
  text head: **[CHAR-3]** E — The programme names this characteristic "Healing wholeness through faith exercised." The name signals several structural commitments simultaneo
- cf.id=20600 (T1.1.3) sg=None status=finding
  text head: **[CHAR-3]** E — The name "Healing wholeness through faith exercised" carries all three implications noted in the prompt. (1) Directional: "through" establishes
- cf.id=20624 (T2.7.2) sg=None status=finding
  text head: **[CHAR-3]** E — The primary soul-to-body direction, with secondary body-to-soul feedback (established in T2.7.1), has two consequences for understanding the ch
- cf.id=20629 (T2.2.3) sg=None status=finding
  text head: **[CHAR-3]** E — Evidence is not silent: soul-level location is positively evidenced. See T2.2.1 and T2.2.2. Faith as the interior activating faculty, conscienc
- cf.id=20630 (T2.3.3) sg=None status=finding
  text head: **[CHAR-3]** E — Evidence is not silent: heart-location is implied and supported by the corpus meanings. See T2.3.1 and T2.3.2. The keywords "heart trusting" (v
- cf.id=20632 (T2.5.3) sg=None status=finding
  text head: **[CHAR-3]** E — Evidence is not silent: conscience and the affective-volitional sub-region are both positively evidenced as soul sub-locations for this charact
- cf.id=20633 (T2.6.3) sg=None status=finding
  text head: **[CHAR-3]** E — Body-part links are positively evidenced. See T2.6.1 and T2.6.2. No silence note is required.
- cf.id=20634 (T2.7.3) sg=None status=finding
  text head: **[CHAR-3]** E — A body-characteristic link is positively evidenced with clear directionality. See T2.7.1 and T2.7.2. No silence note is required.
- cf.id=20637 (T2.10.3) sg=None status=finding
  text head: **[CHAR-3]** E — Constitutional movement is positively evidenced. See T2.10.1 and T2.10.2. The four-stage sequence (formation → expression → reception → consoli
- cf.id=20652 (T3.3.2) sg=None status=finding
  text head: **[CHAR-3]** E — The characteristic *enables* the deployment of memorial knowledge of Jesus as background substrate (prior testimony about Jesus recalled by fai
- cf.id=20656 (T3.7.2) sg=None status=finding
  text head: **[CHAR-3]** E — The characteristic strongly *enables* agency. As noted in T3.7.1, every instance in M38-C involves the faith-seeker as an active initiator. Jes
- cf.id=20661 (T3.1.3) sg=None status=finding
  text head: **[CHAR-3]** E — The pattern of perception engagement in M38-C reveals that this characteristic is *trans-sensory* in its perceptive requirement. The faith-heal
- cf.id=20663 (T3.3.3) sg=None status=finding
  text head: **[CHAR-3]** E — The partial and inferential engagement with memory (T3.3.1, T3.3.2) reveals that this characteristic is *dependent on received testimony* but n
- cf.id=20667 (T3.7.3) sg=None status=finding
  text head: **[CHAR-3]** E — The pattern of consistent, strong, and divinely-affirmed agency engagement across M38-C reveals that this characteristic exemplifies a distinct
- cf.id=20671 (T3.11.3) sg=None status=finding
  text head: **[CHAR-3]** E — The pervasive and consistent engagement of relational capacity across all three VCGs and all twelve verses reveals that this characteristic is 
- cf.id=20675 (T4.1.4) sg=None status=finding
  text head: **[CHAR-3]** E — The evidence is not silent on God-to-human operation; it is extensively evidenced across all three VCGs as established in obs_id=324, 325, and 
- cf.id=20679 (T4.2.4) sg=None status=finding
  text head: **[CHAR-3]** E — The evidence is not silent on human-to-God operation; it is thoroughly evidenced across all three VCGs as established in obs_id=328, 329, and 3
- cf.id=20687 (T4.4.4) sg=None status=finding
  text head: **[CHAR-3]** E — The evidence is not silent on reception; it is well-evidenced across VCG-01 and VCG-02 and partially in VCG-03 as noted in obs_id=336 and 337. 
- cf.id=20691 (T4.5.4) sg=None status=finding
  text head: **[CHAR-3]** E — The evidence is not silent on relational boundaries; it addresses them through the Samaritan leper example and the diversity of recipients as n
- cf.id=20698 (T5.1.3) sg=None status=finding
  text head: **[CHAR-3]** E — The evidence is not silent on transformation; it is central to the characteristic's operation as established in obs_id=348 and 349 above. No si
- cf.id=20700 (T5.2.2) sg=None status=finding
  text head: **[CHAR-3]** E — Drawing on the full VCG evidence, the sequence is: (1) Acute need registered in the inner being — physical suffering, mortal threat, or burdene
- cf.id=20701 (T5.2.3) sg=None status=finding
  text head: **[CHAR-3]** E — The evidence is not silent on sequence; it is substantially evidenced across VCG-01, VCG-02, and VCG-03 as established in obs_id=351 and 352 ab
- cf.id=20704 (T5.3.3) sg=None status=finding
  text head: **[CHAR-3]** E — The evidence is not silent on mechanism; it is evidenced with contextual differentiation across all three VCGs as established in obs_id=354 and
- cf.id=20707 (T5.4.3) sg=None status=finding
  text head: **[CHAR-3]** E — The evidence is not silent; suffering and affliction are present in every verse-account in M38-C as established in obs_id=357 and 358. No silen
- cf.id=20719 (T6.1.3) sg=None status=finding
  text head: **[CHAR-3]** E — Significant co-occurrence patterns do emerge across all three VCGs. This prompt does not apply as a silent finding. See T6.1.1 and T6.1.2 for d
- cf.id=20722 (T6.2.3) sg=None status=finding
  text head: **[CHAR-3]** E — A clear and repeated sequential pattern is evidenced across VCG-01 and VCG-02. This prompt does not require a null finding. See T6.2.1 and T6.2
- cf.id=20726 (T6.3.4) sg=None status=finding
  text head: **[CHAR-3]** E — Causal and constitutive relationships are evidenced throughout the corpus. This prompt does not require a null finding. See T6.3.1, T6.3.2, and
- cf.id=20730 (T6.4.4) sg=None status=finding
  text head: **[CHAR-3]** E — Significant vocabulary sharing is evidenced at both term and root levels. This prompt does not require a null finding. See T6.4.1, T6.4.2, and 
- cf.id=20733 (T6.5.3) sg=None status=finding
  text head: **[CHAR-3]** E — The distinction between Char-3 and M38-A is primarily one of **direction** and secondarily one of **constitutional level**.

**Direction**: In 

---

### AUDIT-V25-COMPLETENESS — Catalogue prompt × scope cells with no cluster_finding row

**Section reference:** §15.2 check 2 (completeness)
**Count:** 1747
**Blocking threshold:** 5
**If blocking, restart from:** Phase 9

Expected 1936 cells (prompts × scopes); found 189; missing 1747.

- C-001 × M38-A
- C-001 × M38-B
- C-001 × M38-C
- C-001 × M38-D
- C-001 × M38-E
- C-001 × M38-F
- C-001 × M38-G
- C-001 × CLUSTER
- C-002 × M38-A
- C-002 × M38-B
- C-002 × M38-C
- C-002 × M38-D
- C-002 × M38-E
- C-002 × M38-F
- C-002 × M38-G
- C-002 × CLUSTER
- C-003 × M38-A
- C-003 × M38-B
- C-003 × M38-C
- C-003 × M38-D
- … and 1727 more

---

### AUDIT-V25-REGISTER-FAMILIES — Inner-being register families detected in BOUNDARY (§1.1 scope) without substantive sub-group home

**Section reference:** §1.1 + §8.4.1
**Count:** 0
**Blocking threshold:** 8
**If blocking, restart from:** Phase 5

_Keyword-based scan of Pass A meanings. A significant cohort suggests Phase 5 sub-group design did not accommodate this register family._

No items found. Check is clean.

---

## §5 — Researcher next steps

1. Review the blocking findings above and confirm or override the recommended phase restart (Phase 7).
2. If accepting the restart, CC will build a phase-restart directive per §17.3.2: backup affected rows + status transition + roll-back ops.
3. If pursuing surgical fixes despite the recommendation, approve a fix list and CC will build surgical directives per §17.5 — but note the recommendation indicates the fixes will not be sufficient on their own.

---

*End of compliance report. Read-only audit; no DB writes were performed.*