# M05 audit against wa-sessionb-cluster-instruction-v2_5-20260518

**Date:** 2026-05-21 07:09
**Script:** `scripts/_audit_cluster_against_instruction_v25_v1_20260521.py`
**Instruction version checked against:** v2_5
**Cluster status at audit time:** 'Analysis Completed'
**Cluster version:** 'v6'

---

## §1 — Corrective-actions plan

**Plan verdict:** `SYSTEMIC`

1 systemic action(s) affect >50% of cluster scope. Bounded fixes are insufficient; consider phase-restart on the affected scope. Other actions are bounded surgical.

**Cluster corpus reference (denominators for scope):**
- relevant verse_context rows: 1593
- term count: 88
- set-aside vc rows: 249
- existing cluster_finding rows: 1517

### Canonical cascade

1. **Phase 2** — Pass A meaning — author verse_context.analysis_note
2. **Phase 5/6** — Sub-group review — fit existing sub-group OR propose new
3. **Phase 7** — VCG review — fit existing VCG in target sub-group OR create new (with anchor)
4. **Phase 9/11** — Findings review — does the verse confirm / extend / contradict an existing finding, or open a new one
5. **Session C** — Publication review — re-publish any chapter whose cited findings substantively changed

### Actions (sorted by cascade entry step)

| # | Error type | Entry step | Count | Scope | Work | % of denominator |
|---|---|---:|---:|---|---|---|
| 1 | `missing_pass_a_meaning` | 1 | 1427 | systemic | very large | 90% of relevant verses |
| 2 | `terse_setaside` | 1 | 7 | bounded | small | 3% of set-aside verses |
| 3 | `missing_subgroup` | 2 | 165 | bounded | large | 10% of relevant verses |
| 4 | `missing_vcg` | 3 | 33 | bounded | medium | 2% of relevant verses |
| 5 | `placeholder_finding` | 4 | 705 | bounded | very large | 46% of cluster_finding rows |
| 6 | `completeness_gap` | 4 | 661 | bounded | very large | — |
| 7 | `ungrounded_finding` | 4 | 470 | bounded | large | 31% of cluster_finding rows |

### Per-action detail

#### Action 1 — `missing_pass_a_meaning` (1427 items, systemic)

**Cascade entry:** step 1
  (Phase 2 — Pass A meaning — author verse_context.analysis_note)

**Action pattern:** Run Phase 2 Pass A on the affected vc_ids → cascade through 2/3/4/5 as needed

**Cascade steps that may apply:**
  - Step 1 (Phase 2): Pass A meaning — author verse_context.analysis_note — applies
  - Step 2 (Phase 5/6): Sub-group review — fit existing sub-group OR propose new — may apply (cascade may short-circuit)
  - Step 3 (Phase 7): VCG review — fit existing VCG in target sub-group OR create new (with anchor) — may apply (cascade may short-circuit)
  - Step 4 (Phase 9/11): Findings review — does the verse confirm / extend / contradict an existing finding, or open a new one — may apply (cascade may short-circuit)
  - Step 5 (Session C): Publication review — re-publish any chapter whose cited findings substantively changed — may apply (cascade may short-circuit)

**Notes:** Cascade may short-circuit at step 1 if the verse turns out to be a legitimate set-aside (no inner-being state). Otherwise full cascade applies.

**Sample affected entities:**
- G5382 filoxenos 1Ti 3:2 (vc=1893)
- G5382 filoxenos 1Pe 4:9 (vc=1894)
- G5382 filoxenos Tit 1:8 (vc=1895)
- G5381 filoxenia Rom 12:13 (vc=1896)
- G5381 filoxenia Heb 13:2 (vc=1897)
- G1652 eleeinos Rev 3:17 (vc=6210)
- G1652 eleeinos 1Cor 15:19 (vc=6211)
- G3627 oikteirō Rom 9:15 (vc=6226)

---

#### Action 2 — `terse_setaside` (7 items, bounded)

**Cascade entry:** step 1
  (Phase 2 — Pass A meaning — author verse_context.analysis_note)

**Action pattern:** Researcher reviews each: confirm with proper §4.5.1 evidence-based reason (no cascade) OR RESCUE → relevant + cascade

**Cascade steps that may apply:**
  - Step 1 (Phase 2): Pass A meaning — author verse_context.analysis_note — applies
  - Step 2 (Phase 5/6): Sub-group review — fit existing sub-group OR propose new — may apply (cascade may short-circuit)
  - Step 3 (Phase 7): VCG review — fit existing VCG in target sub-group OR create new (with anchor) — may apply (cascade may short-circuit)
  - Step 4 (Phase 9/11): Findings review — does the verse confirm / extend / contradict an existing finding, or open a new one — may apply (cascade may short-circuit)
  - Step 5 (Session C): Publication review — re-publish any chapter whose cited findings substantively changed — may apply (cascade may short-circuit)

**Notes:** Terse values may be legitimate but lack the verse-specific rationale §4.5.1 requires.

**Sample affected entities:**
- reason='physical_only'

---

#### Action 3 — `missing_subgroup` (165 items, bounded)

**Cascade entry:** step 2
  (Phase 5/6 — Sub-group review — fit existing sub-group OR propose new)

**Action pattern:** Review analysis_note vs existing sub-groups; assign to fit OR propose new sub-group; cascade through 3/4/5

**Cascade steps that may apply:**
  - Step 2 (Phase 5/6): Sub-group review — fit existing sub-group OR propose new — applies
  - Step 3 (Phase 7): VCG review — fit existing VCG in target sub-group OR create new (with anchor) — applies
  - Step 4 (Phase 9/11): Findings review — does the verse confirm / extend / contradict an existing finding, or open a new one — applies
  - Step 5 (Session C): Publication review — re-publish any chapter whose cited findings substantively changed — applies

**Notes:** Pass A meaning already exists. Sub-group decision drives Phase 7 + Phase 9/11 follow-on.

---

#### Action 4 — `missing_vcg` (33 items, bounded)

**Cascade entry:** step 3
  (Phase 7 — VCG review — fit existing VCG in target sub-group OR create new (with anchor))

**Action pattern:** Review meaning + sub-group placement vs existing VCGs; assign or create new VCG (with anchor)

**Cascade steps that may apply:**
  - Step 3 (Phase 7): VCG review — fit existing VCG in target sub-group OR create new (with anchor) — applies
  - Step 4 (Phase 9/11): Findings review — does the verse confirm / extend / contradict an existing finding, or open a new one — applies
  - Step 5 (Session C): Publication review — re-publish any chapter whose cited findings substantively changed — applies

**Notes:** Sub-group placement already exists. VCG-level analysis only.

---

#### Action 5 — `placeholder_finding` (705 items, bounded)

**Cascade entry:** step 4
  (Phase 9/11 — Findings review — does the verse confirm / extend / contradict an existing finding, or open a new one)

**Action pattern:** Either: revise finding_text with substantive evidence (read sub-group verses, author) OR change finding_status to 'silent' with explicit silence rationale

**Cascade steps that may apply:**
  - Step 4 (Phase 9/11): Findings review — does the verse confirm / extend / contradict an existing finding, or open a new one — applies
  - Step 5 (Session C): Publication review — re-publish any chapter whose cited findings substantively changed — applies

**Notes:** No verse impact. Phase 9 micro-pass on the affected finding rows only.

_Estimated split from sample of 30 (placeholder ratio 60%)_

**Sample affected entities:**
- T0.1.3 × M05-A
- T0.1.3 × M05-B
- T0.1.3 × M05-C
- T0.1.3 × M05-D
- T0.1.3 × M05-E
- T0.1.3 × M05-F
- T0.1.3 × M05-G
- T0.3.2 × M05-A

---

#### Action 6 — `completeness_gap` (661 items, bounded)

**Cascade entry:** step 4
  (Phase 9/11 — Findings review — does the verse confirm / extend / contradict an existing finding, or open a new one)

**Action pattern:** Phase 9 micro-pass: author E (with verse evidence) / S (silent with rationale) / G (gap) for each missing cell; INSERT cluster_finding row

**Cascade steps that may apply:**
  - Step 4 (Phase 9/11): Findings review — does the verse confirm / extend / contradict an existing finding, or open a new one — applies
  - Step 5 (Session C): Publication review — re-publish any chapter whose cited findings substantively changed — applies

**Notes:** Phase 9 cell-by-cell completion. Researcher may opt to filter to v2_5 T0–T7 prompts if catalogue includes legacy codes.

**Sample affected entities:**
- C-001 × M05-A
- C-001 × M05-B
- C-001 × M05-C
- C-001 × M05-D
- C-001 × M05-E
- C-001 × M05-F
- C-001 × M05-G
- C-001 × M05-BOUNDARY

---

#### Action 7 — `ungrounded_finding` (470 items, bounded)

**Cascade entry:** step 4
  (Phase 9/11 — Findings review — does the verse confirm / extend / contradict an existing finding, or open a new one)

**Action pattern:** Read finding's source verses, add explicit verse references to finding_text. If genuinely a cluster-synthesis without specific verses, add sub-group references at minimum.

**Cascade steps that may apply:**
  - Step 4 (Phase 9/11): Findings review — does the verse confirm / extend / contradict an existing finding, or open a new one — applies
  - Step 5 (Session C): Publication review — re-publish any chapter whose cited findings substantively changed — applies

**Notes:** Phase 9 §15.2 check 1 compliance. No verse impact.

**Sample affected entities:**
- T0.1.1 × M05-G
- T0.1.2 × M05-G
- T0.2.1 × M05-F
- T0.2.2 × M05-A
- T0.2.2 × M05-C
- T0.2.2 × M05-F
- T0.2.2 × M05-G
- T0.2.3 × M05-A

---

## §2 — Legacy verdict (phase-restart framing)

**Level:** `MIXED`

**Recommendation:** Restart from Phase 2. Blocking findings cannot be repaired surgically. Advisory findings can be handled as surgical fixes either during the restart or before it.

**Restart-from-phase:** Phase 2

Per v2_5 §17.3.2, the cluster.status transition for this restart is:
  (see §17.3.2 table)

---

## §3 — Summary by check

| Check code | Count | Threshold | Severity | Section |
|---|---:|---:|---|---|
| `AUDIT-V25-STATUS-SUFFIX` | 0 | 1 | clean | §2.6 (status discipline) + cluster.status conventions |
| `AUDIT-V25-PIPELINE-INCOMPLETE` | 1625 | 1 | blocking | §4 (Phase 1) + §5 (Phase 2) + §9 (Phase 6) + §10 (Phase 7) |
| `AUDIT-V25-BOUNDARY-PENDING` | 0 | 5 | clean | §11A (Phase 8.5) + §15.2 check 8 |
| `AUDIT-V25-FORBIDDEN-SETASIDE` | 0 | 10 | clean | §4.5.1 (forbidden grounds for SET_ASIDE) |
| `AUDIT-V25-TERSE-SETASIDE` | 7 | 20 | advisory | §4.5.1 (valid SET_ASIDE reasons require specific evidence ground) |
| `AUDIT-V25-BOUNDARY-PARKING` | 0 | 10 | clean | §8.4.1 (BOUNDARY is not a parking lot) |
| `AUDIT-V25-EVIDENCE-GROUNDING` | 1175 | 5 | blocking | §15.2 check 1 (evidence-grounding) |
| `AUDIT-V25-COMPLETENESS` | 661 | 5 | blocking | §15.2 check 2 (completeness) |
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
**Count:** 1625
**Blocking threshold:** 1
**If blocking, restart from:** Phase 2

Total gap items: 1625

By category:
- missing_pass_a_meaning: 1427
- missing_subgroup: 165
- missing_vcg: 33

By term (highest-gap-count first):
- H2617A che.sed (term_id=536): {'missing_pass_a_meaning': 240, 'missing_vcg': 3}
- H2617B che.sed (term_id=1633): {'missing_subgroup': 162}
- G0025 agapaō (term_id=571): {'missing_pass_a_meaning': 130}
- G3870 parakaleō (term_id=510): {'missing_pass_a_meaning': 119}
- G0026 agapē (term_id=562): {'missing_pass_a_meaning': 105}
- G0018 agathos (term_id=881): {'missing_pass_a_meaning': 90}
- H5162G na.cham (term_id=445): {'missing_pass_a_meaning': 67}
- G5384 filos (term_id=1579): {'missing_pass_a_meaning': 38, 'missing_vcg': 11}
- H0160 a.ha.vah (term_id=537): {'missing_pass_a_meaning': 45}
- H7355 ra.cham (term_id=551): {'missing_pass_a_meaning': 43}
- H2550 cha.mal (term_id=487): {'missing_pass_a_meaning': 38, 'missing_vcg': 1}
- H7356B ra.cha.mim (term_id=544): {'missing_pass_a_meaning': 39}
- H2436G cheq (term_id=575): {'missing_pass_a_meaning': 34}
- H2623 cha.sid (term_id=540): {'missing_pass_a_meaning': 33}
- G1653 eleeō (term_id=981): {'missing_pass_a_meaning': 30, 'missing_vcg': 1}

Sample affected items (first 50):
- missing_pass_a_meaning: G5382 filoxenos 1Ti 3:2 (phase owner: 2)
- missing_pass_a_meaning: G5382 filoxenos 1Pe 4:9 (phase owner: 2)
- missing_pass_a_meaning: G5382 filoxenos Tit 1:8 (phase owner: 2)
- missing_pass_a_meaning: G5381 filoxenia Rom 12:13 (phase owner: 2)
- missing_pass_a_meaning: G5381 filoxenia Heb 13:2 (phase owner: 2)
- missing_pass_a_meaning: G1652 eleeinos Rev 3:17 (phase owner: 2)
- missing_pass_a_meaning: G1652 eleeinos 1Cor 15:19 (phase owner: 2)
- missing_pass_a_meaning: G3627 oikteirō Rom 9:15 (phase owner: 2)
- missing_pass_a_meaning: G4697 splanchnizō Luk 7:13 (phase owner: 2)
- missing_pass_a_meaning: G4697 splanchnizō Mat 9:36 (phase owner: 2)
- missing_pass_a_meaning: G4697 splanchnizō Mat 14:14 (phase owner: 2)
- missing_pass_a_meaning: G4697 splanchnizō Mat 15:32 (phase owner: 2)
- missing_pass_a_meaning: G4697 splanchnizō Mat 18:27 (phase owner: 2)
- missing_pass_a_meaning: G4697 splanchnizō Mat 20:34 (phase owner: 2)
- missing_pass_a_meaning: G4697 splanchnizō Mar 1:41 (phase owner: 2)
- missing_pass_a_meaning: G4697 splanchnizō Mar 6:34 (phase owner: 2)
- missing_pass_a_meaning: G4697 splanchnizō Mar 8:2 (phase owner: 2)
- missing_pass_a_meaning: G4697 splanchnizō Mar 9:22 (phase owner: 2)
- missing_pass_a_meaning: G4697 splanchnizō Luk 10:33 (phase owner: 2)
- missing_pass_a_meaning: G4697 splanchnizō Luk 15:20 (phase owner: 2)

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
**Count:** 0
**Blocking threshold:** 10
**If blocking, restart from:** Phase 1

_Pattern-based scan; researcher should read each flagged reason in context._

No items found. Check is clean.

---

### AUDIT-V25-TERSE-SETASIDE — Terse set_aside_reason values lack specific ground

**Section reference:** §4.5.1 (valid SET_ASIDE reasons require specific evidence ground)
**Count:** 7
**Blocking threshold:** 20
**If blocking, restart from:** Phase 1

_Terse values like 'physical_only' are borderline. Each verse should carry a verse-specific evidence rationale._

| Reason | Count |
|---|---:|
| `physical_only` | 7 |

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
**Count:** 1175
**Blocking threshold:** 5
**If blocking, restart from:** Phase 9

Checked 1478 E-coded cluster_finding rows; 1175 ungrounded.

- cf.id=1523 (T0.1.1) sg=M05-G status=finding
  text head: The "fellowship of the Holy Spirit" (2Cor 13:14 — Group 1055) names koinōnia as a quality of the divine inner life. God is "faithful, by whom you were called in
- cf.id=1530 (T0.1.2) sg=M05-G status=finding
  text head: Yes. 2Cor 13:14 (Group 1055); 1Cor 1:9 (Group 1055). Attribution reveals: fellowship in the human community participates in the inner communal reality of the Tr
- cf.id=1531 (T0.1.3) sg=M05-A status=finding
  text head: [Sub-group not separately addressed in source — see cluster-level finding for this prompt]
- cf.id=1532 (T0.1.3) sg=M05-B status=finding
  text head: [Sub-group not separately addressed in source — see cluster-level finding for this prompt]
- cf.id=1533 (T0.1.3) sg=M05-C status=finding
  text head: [Sub-group not separately addressed in source — see cluster-level finding for this prompt]
- cf.id=1534 (T0.1.3) sg=M05-D status=finding
  text head: [Sub-group not separately addressed in source — see cluster-level finding for this prompt]
- cf.id=1535 (T0.1.3) sg=M05-E status=finding
  text head: [Sub-group not separately addressed in source — see cluster-level finding for this prompt]
- cf.id=1536 (T0.1.3) sg=M05-F status=finding
  text head: [Sub-group not separately addressed in source — see cluster-level finding for this prompt]
- cf.id=1537 (T0.1.3) sg=M05-G status=finding
  text head: [Sub-group not separately addressed in source — see cluster-level finding for this prompt]
- cf.id=1543 (T0.2.1) sg=M05-F status=finding
  text head: Comfort equips the person to become a channel of the comfort they have received — "so that we may be able to comfort those who are in any affliction, with the c
- cf.id=1545 (T0.2.2) sg=M05-A status=finding
  text head: Both. The Song of Songs presents love in a creation-delight register without reference to sin. But chesed in its most evidenced form addresses human failure and
- cf.id=1547 (T0.2.2) sg=M05-C status=finding
  text head: Response to the fallen condition. Mercy presupposes guilt and condemnation — its judicial frame requires a broken relationship that needs gracious override. No 
- cf.id=1550 (T0.2.2) sg=M05-F status=finding
  text head: Primarily a response to the fallen condition. Grief, distress, and the need for comfort presuppose post-fall realities. The la.vav heart-stirring (Song 4:9 — Gr
- cf.id=1551 (T0.2.2) sg=M05-G status=finding
  text head: Both. The Trinitarian fellowship (2Cor 13:14 — Group 1055) is constitutive; katallagē (Group 2069) is constitutively remedial — reconciliation presupposes estra
- cf.id=1552 (T0.2.3) sg=M05-A status=finding
  text head: Yes — love is eschatologically permanent: "love never ends" (1Cor 13:8 — Group 1542).
- cf.id=1559 (T0.3.1) sg=M05-A status=finding
  text head: Love expresses the image as directed attachment — the human person is the creature whose fundamental orientation is toward God and neighbour, mirroring the divi
- cf.id=1561 (T0.3.1) sg=M05-C status=finding
  text head: Mercy expresses the image as gracious authority — the human who shows mercy from a position of authority images the God who overrides condemnation with favour t
- cf.id=1565 (T0.3.1) sg=M05-G status=finding
  text head: Fellowship expresses the image as communal participation — the person who holds life in common with others images the inner communal reality of the Trinitarian 
- cf.id=1566 (T0.3.2) sg=M05-A status=finding
  text head: [Sub-group not separately addressed in source — see cluster-level finding for this prompt]
- cf.id=1567 (T0.3.2) sg=M05-B status=finding
  text head: [Sub-group not separately addressed in source — see cluster-level finding for this prompt]
- cf.id=1568 (T0.3.2) sg=M05-C status=finding
  text head: [Sub-group not separately addressed in source — see cluster-level finding for this prompt]
- cf.id=1569 (T0.3.2) sg=M05-D status=finding
  text head: [Sub-group not separately addressed in source — see cluster-level finding for this prompt]
- cf.id=1570 (T0.3.2) sg=M05-E status=finding
  text head: [Sub-group not separately addressed in source — see cluster-level finding for this prompt]
- cf.id=1571 (T0.3.2) sg=M05-F status=finding
  text head: [Sub-group not separately addressed in source — see cluster-level finding for this prompt]
- cf.id=1572 (T0.3.2) sg=M05-G status=finding
  text head: [Sub-group not separately addressed in source — see cluster-level finding for this prompt]
- cf.id=1582 (T0.4.1) sg=M05-C status=finding
  text head: Yes — the mercy-economy of Mat 18 (servant who received mercy and withheld it — Group 1630) as a typological illustration of the mercy-logic that governs the di
- cf.id=1587 (T0.4.2) sg=M05-A status=finding
  text head: [Sub-group not separately addressed in source — see cluster-level finding for this prompt]
- cf.id=1588 (T0.4.2) sg=M05-B status=finding
  text head: [Sub-group not separately addressed in source — see cluster-level finding for this prompt]
- cf.id=1589 (T0.4.2) sg=M05-C status=finding
  text head: [Sub-group not separately addressed in source — see cluster-level finding for this prompt]
- cf.id=1590 (T0.4.2) sg=M05-D status=finding
  text head: [Sub-group not separately addressed in source — see cluster-level finding for this prompt]

---

### AUDIT-V25-COMPLETENESS — Catalogue prompt × scope cells with no cluster_finding row

**Section reference:** §15.2 check 2 (completeness)
**Count:** 661
**Blocking threshold:** 5
**If blocking, restart from:** Phase 9

Expected 2178 cells (prompts × scopes); found 1517; missing 661.

- C-001 × M05-A
- C-001 × M05-B
- C-001 × M05-C
- C-001 × M05-D
- C-001 × M05-E
- C-001 × M05-F
- C-001 × M05-G
- C-001 × M05-BOUNDARY
- C-001 × CLUSTER
- C-002 × M05-A
- C-002 × M05-B
- C-002 × M05-C
- C-002 × M05-D
- C-002 × M05-E
- C-002 × M05-F
- C-002 × M05-G
- C-002 × M05-BOUNDARY
- C-002 × CLUSTER
- C-003 × M05-A
- C-003 × M05-B
- … and 641 more

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

1. Review the blocking findings above and confirm or override the recommended phase restart (Phase 2).
2. If accepting the restart, CC will build a phase-restart directive per §17.3.2: backup affected rows + status transition + roll-back ops.
3. If pursuing surgical fixes despite the recommendation, approve a fix list and CC will build surgical directives per §17.5 — but note the recommendation indicates the fixes will not be sufficient on their own.

---

*End of compliance report. Read-only audit; no DB writes were performed.*