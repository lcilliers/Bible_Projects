# The Cluster Audit — per-level compliance check (design)

> **Methodology design · v1 · 2026-06-07 · CC.** Designs **open item A2** of
> `wa-cluster-rollup-design.md` (v3). The audit is a **compliance check**, not a remedial program: it
> validates a cluster against the **v3+ instruction and expectation**, level by level, and reports each level
> **PASS / FAIL**. Remediation is a *separate* act (pointed intervention or a re-run of the v3 instruction).
> Governed by the v3 roll-up; informed by memory `feedback_audit_must_be_self_critical`,
> `feedback_audit_before_prose`, `project_v25_audit_tool`. **Each level's audit is derived from that level's
> rollup pattern** (Needs · Updates → FC · Does → SC · Gate → mop-up). **The audit is the *precondition* for
> the A3 researcher sign-off gate, not a substitute for it.** **L1 check spec is complete** (L1 design done);
> L2–L8 specs are stubbed (resequenced spine: L2 sub-group formation; L3–L5 per sub-group; L6 cross-sub-group;
> L7 cluster synthesis; L8 whole-study), to be filled as each level's design settles.

---

## 1. What the audit is — and is not

- **Is:** a **compliance check**. For each roll-up level, it evaluates the cluster's actual DB state and
  process trail against the **standard** the v3 instruction defines for that level, and returns **PASS** or
  **FAIL** with the evidence. It is **step-by-step, per level** — L1 is checked as L1, L2 as L2, and so on.
- **Is not:** a remedial program. The audit **does not fix** anything. It **reports** non-compliance and
  **routes** it. *(This is the clean separation the researcher asked for: compliance vs repair.)*
- **Remediation (downstream, not the audit):** either a **pointed intervention** (fix the specific gap) or a
  **re-run of the v3 instruction** for the affected scope (verse / term / VCG / sub-group / cluster). The
  audit's job ends at emitting the FAIL + enough detail to choose the route.

**Self-critical clause** (`feedback_audit_must_be_self_critical`): the audit interrogates **its own coverage**
— if a level produced an outcome the current checks don't test, that gap is itself a finding ("check not yet
written"), not a silent pass.

## 2. The audit maps onto the roll-up pattern (so it is written *from* the design)

Every roll-up level in `wa-cluster-rollup-design.md` is defined by the same four-part pattern —
**Needs · Does · Updates · Output→next** (+ a mop-up **Gate**). **The audit checks a level against exactly
those four parts**, so each level's audit is *derived directly* from its rollup definition:

| Rollup part | Audit check | Question | How | Cost |
|---|---|---|---|---|
| **Needs** | **Precondition** | Were the **inputs** present and valid — i.e. did the prior level's `Output→next` actually arrive? | the prior level **PASSED** + spot the handoff exists | trivial |
| **Updates** | **(a) Field-completeness (FC)** | Are the fields this level **writes** filled in, on **every** in-scope object, with valid values? | pure SQL over the level's `Updates` columns; NULL/invalid where required = FAIL | script |
| **Does** | **(b) Instruction-adherence (SC)** | Was the **process** actually followed — or is a field filled but *wrong*? | mechanical pre-screens + a **stratified sample** read by AI/researcher | script + read |
| **Gate** | **Mop-up** | Does the level's **gate** hold — nothing of the level below left unconsumed before `Output→next`? | SQL count of orphans (no verse without a VCG, etc.) = 0 | script |

FC catches *omission*; SC catches *mal-execution*; the Gate catches *orphans*; the Precondition stops a level
being audited on a broken input. A level **PASSES** iff: Precondition met **and** FC 100% **and** SC sampled
failure ≤ threshold **and** Gate = 0 orphans. **To write a level's audit, read its rollup `Updates` (→ FC),
its `Does` (→ SC), and its `Gate` (→ mop-up).**

## 3. Reporting format

A per-level grid, one row per check, plus a level verdict:

```text
Cluster M01 — v3 compliance audit
LEVEL  CHECK            SCOPE            RESULT
L1     PRE-L1  source   ok               PASS
L1     FC-L1-1 relev    945/945          PASS
L1     FC-L1-3 stepmn   945/945          PASS
L1     SC-L1-1 corrob   30 sampled, 30✓  PASS
L1     SC-L1-2 stem     30 sampled, 28✓  FAIL (2 sense↔stem mismatch → route)
L1     GT-L1-1 orphans  0                PASS
...
L1 VERDICT: FAIL (1 spot-check below threshold)   → remediation: pointed (2 verses) | re-run term
```

Level verdict = **PASS** iff **Precondition** met **and** all **FC** = 100% **and** all **SC** ≥ threshold
**and** **Gate** = 0 orphans. Cluster verdict = the per-level vector (a cluster is not "passed" globally until
every designed level passes — and a level cannot pass if its **Needs** precondition — the prior level — has
not).

## 4. L1 audit — the complete check spec

**L1 = verse establishment = old Phase 1 (relevance + UT-verse classification + related-pass + similarity)
+ the A1 mechanical STEP-sense application.** Its expected outputs (per relevant span): the retained Phase-1
fields (`is_relevant`, `set_aside_reason`, UT-class / `is_related`) **plus** the A1 fields
(`step_meaning_applied`, `sense_id`, `sense_multiplicity`, `step_envelope_note`, `morph_code`/`stem`, `pole`,
`keywords` STEP-capture, `analysis_note` AI-preserved, `residue_flag`). The audit checks **both** the
retained Phase-1 steps and the new A1 steps. Structured below against the rollup parts:
**Needs → Updates (FC) → Does (SC) → Gate.**

### Needs (precondition)
- **PRE-L1:** the source is present — every span has a `wa_verse_records` row with text/span/**morphology**,
  and the term has a resolvable **STEP sense-set** (`mti_terms`/`wa_term_inventory`/`wa_meaning_sense`). L1 is
  the first rung, so its Needs are *source data*, not a prior level. FAIL → cannot audit; fix extraction first.

### Updates → (a) Field-completeness — mechanical, exhaustive (SQL)

| ID | Check | FAIL condition |
|---|---|---|
| **FC-L1-1** | Every span classified for relevance | any `is_relevant IS NULL` |
| **FC-L1-2** | Set-aside spans carry a reason from the controlled list | `is_relevant=0` and `set_aside_reason` NULL/invalid |
| **FC-L1-3** | Every **relevant** span has an applied STEP meaning | `is_relevant=1` and `step_meaning_applied` empty |
| **FC-L1-4** | `sense_id` points to a **valid sense of this term** | `sense_id` NULL or not in the term's sense-set |
| **FC-L1-5** | Single/multi indicator set | `sense_multiplicity` NULL |
| **FC-L1-6** | STEP-capture keywords present | relevant span with empty `keywords` |
| **FC-L1-7** | Pole assigned | `pole` NULL or not in {inner, external, physical} |
| **FC-L1-8** | Morphology/stem captured (where STEP supplies it) | `morph_code`/`stem` NULL on a tagged span |
| **FC-L1-9** | **Dual meaning preserved** — AI note not overwritten | a verse that *had* an `analysis_note` now has it blanked/replaced by the STEP meaning |
| **FC-L1-10** | Residue flag set | `residue_flag` NULL on a relevant span |
| **FC-L1-11** | Retained Phase-1 classification present (UT-class / `is_related`) per the Phase-1 standard | a span missing a required retained-Phase-1 value |

All FC-L1 checks are SQL counts → 100% required. These are the "**database fields filled in**" axis. FC-L1-11
guards the **retained** old-Phase-1 steps (incl. UT-verse classification), so the consolidation into L1 does
not silently drop them.

### Does → (b) Instruction-adherence — pre-screen + stratified spot read

| ID | Check | Mechanical pre-screen | Sampled read |
|---|---|---|---|
| **SC-L1-1** | **Corroboration holds** — `step_meaning_applied` lies within the term's STEP sense-set | token-overlap scanner (`_assess_verse_corroboration.py`) flags the **residue** (no overlap) | read the residue + a sample of the corroborated set; verdict ALIGNED / DRIFT / **DIVERGENT** |
| **SC-L1-2** | **Sense ↔ stem consistency** — the selected `sense_id` belongs to the **stem-branch** the morphology indicates (Niphal verse → a Niphal-branch sense) | once `stem_label` is populated, compare `stem` to `sense_id`'s branch → mismatch list | read mismatches |
| **SC-L1-3** | **Keywords are STEP-derived**, not interpretive | keyword tokens trace to the sense-set tokens | spot-read a sample for interpretive leakage |
| **SC-L1-4** | **Multi-sense actually selected** — multi verses have a definite `sense_id`, else `residue_flag=1` with reason | SQL: `sense_multiplicity='multi'` AND `sense_id` NULL AND `residue_flag=0` | — |
| **SC-L1-5** | **Pole correctness** — pole matches the sense (physical sense → physical pole; metaphor flagged) | sense→pole map disagreement list | read disagreements + sample |
| **SC-L1-6** | **Set-aside correctness** — set-aside spans genuinely lack inner-being relevance (nothing real dropped) | — | stratified sample of set-asides, read against verse |
| **SC-L1-7** | **Dual-meaning integrity** — the AI `analysis_note` does **not contradict** the `step_meaning_applied` (this is where a real DIVERGENT surfaces) | overlap between the two | read divergences |

**Sampling:** stratify by `sense_multiplicity` (single/multi), by `stem`, and by `pole`; sample N per term
(or per cluster for thin terms). The pre-screens shrink the read to (residue + mismatch lists + a confirming
sample) — on M01 that was **28 residue of 949**, a ~34× reduction.

**Mechanical reuse:** SC-L1-1's pre-screen *is* the A1 corroboration scanner already built. SC-L1-2/5 become
mechanical once `stem_label` is populated and the sense→pole map exists (R6/R7). So most of L1's audit is
scriptable; only a small stratified sample needs a human/AI read.

### Gate (mop-up) — `Output→next` is sound
- **GT-L1-1:** no span left unclassified — `is_relevant IS NULL` count = 0 (the L1 gate).
- **GT-L1-2:** every relevant span carries the handoff L2 needs — `step_meaning_applied` + `keywords` present,
  `residue_flag` set. (A relevant span missing these would orphan at L2.)
- **GT-L1-3:** set-asides retained, not dropped — every `is_relevant=0` span keeps a `set_aside_reason`.

### L1 PASS criteria
**Precondition** PRE-L1 met **and** all **FC-L1-*** = 100% **and** **SC-L1-1/4/7** = 0 DIVERGENT (hard) **and**
**SC-L1-2/3/5/6** sampled failure ≤ threshold 〔TBD — propose 5%〕 **and** **GT-L1-*** = 0 orphans. Else
**FAIL**, with the gap/mismatch/orphan lists attached for routing.

## 5. Remediation routing (the audit emits, does not perform)

| FAIL type | Likely route |
|---|---|
| FC gap (fields missing) | **Re-run** the L1 mechanical step for the affected verses (or full L1 re-run if widespread) |
| SC isolated (a few verses) | **Pointed intervention** on those verses |
| SC systematic (a whole term/stem failing) | **Re-run the v3 instruction** for that term/scope (the process itself misfired) |
| DIVERGENT (corroboration broken) | **Stop-gate** → researcher review (the gravest signal; never auto-fixed) |

## 6. Where the audit runs in the roll-up

- **Per-level gate (preferred):** L1 is audited **before** its outputs roll up to L2 — a failing L1 must not
  feed sub-group formation. Likewise each level before the next. This is stricter than the v2_5 model
  (`feedback_audit_before_prose`: one audit at end of Phase D) and catches errors at the level they occur.
- **Audit → A3 sign-off:** a level's **audit PASS is the precondition** for its A3 researcher-review gate. The
  L1→L2 rule (`wa-cluster-rollup-design.md` §A3): audit clean **and no residue** → researcher review → proceed;
  audit clean **and residue** → L2 proceeds; audit **FAIL** → remediation (no gate).
- The end-of-cluster audit becomes the **union** of the per-level passes (no separate late pass needed),
  with the science (F1) and prose (F2) layers gated on a clean L1–L7 + cluster sign-off.

## 7. Relationship to prior audit work

- **Supersedes** the v2_5 compliance-audit cascade (`project_v25_audit_tool`) for v3 clusters — the
  per-level FC+SC structure replaces the 5-step cascade, but the **corrective-actions routing** idea is kept
  (§5).
- **Keeps** the self-critical clause (`feedback_audit_must_be_self_critical`) and the "audit surfaces all
  un-synthesised objects" principle (`feedback_no_forced_structure_audit_surfaces_analysis_compensates`) —
  the mop-up discipline's gates *are* audit checks (every verse→VCG, every VCG→sub-group, etc.).

## 8. To design as the higher levels settle (stubs — derived from each rollup level's parts)

Each stub reads straight off the rollup level: **Needs** (precondition = prior level PASSED), **FC** (= its
`Updates`), **SC** (= its `Does`), **Gate** (= its mop-up). To complete a stub, copy the level's `Updates`
into FC checks and its `Does` into SC checks. *(Resequenced spine: L2 = sub-group formation; L3–L5 iterate
per sub-group; L6 cross-sub-group; L7 cluster synthesis; L8 whole-study.)*

- **L2 (sub-group formation — provisional)** · *Needs (PRE-L2 completeness — whole cluster in focus):* L1
  PASS **and** the full cluster inventory gathered — **terms · verses · flags · pointers · existing VCGs ·
  previous findings**. *FC:* every relevant verse placed in a provisional `cluster_subgroup`;
  `mti_term_subgroup` populated. *SC:* the partition is justified by the L1 similarity/keyword signal (not
  arbitrary). *Gate (post-L2 completeness):* **every in-focus item allocated to a sub-group OR marked
  cluster-level** (or held for routing/set-aside) — nothing unallocated.
- **L3 (VCG formation + deep read, per sub-group)** · *Needs:* L2 PASS. *FC:* every sub-group verse has a
  `group_id`; every VCG has ≥1 anchor and a `group_code`; rich `analysis_note` present. *SC:* VCG membership
  coheres by sense; anchors apt; **L1 STEP meaning and L3 rich meaning consistent** (dual-meaning, the
  DIVERGENT surface); reroute/set-aside decisions justified. *Gate:* every sub-group verse in exactly one VCG
  (or rerouted/set-aside); pole verses cross-referenced.
- **L4 (VCG-emergent, per sub-group)** · *Needs:* L3 PASS. *FC:* every VCG has a `context_description` /
  VCG-emergent observation. *SC:* the emergent statement is genuinely *more than the sum* of the verses.
  *Gate:* every VCG has an emergent observation; **not duplicated** onto verses (no-overlap).
- **L5 (sub-group-emergent + characteristic + findings, per sub-group)** · *Needs:* L4 PASS + **prior findings
  for this sub-group**. *FC:* every non-BOUNDARY sub-group → `characteristic` + `characteristic_subgroup`,
  `core_description` firmed; **every finding has a `finding_type` (tier / cross-VCG…), a scope anchor naming
  its cluster (+ sub-group/VCG as the type requires), a `finding_citation`, and `finding_status`** (=`draft`
  at submission); **no finding without a cluster**; **every open question captured as a finding flagged
  `needs_research`** (E7); pointers routed here `resolved`; prior findings refined.
  *SC:* the characteristic genuinely *emerges* (not pre-imposed); findings are evidenced and **level-anchored**
  (the `finding_type` matches the level it emerged at); cross-cluster findings created in the right other
  cluster. *Gate (A4 sub-group draft-review):* every VCG in view; characteristic assigned (or BOUNDARY);
  every pointer / prior-finding evaluated; **findings submitted as `draft` for researcher review → `reviewed`
  before the next sub-group starts.**
- **L6 (cross-sub-group + closure)** · *Needs:* all sub-groups PASS L5. *FC:* cluster-level
  `cluster_observation` present; cross-sub-group findings cited; remaining pointers `resolved`. *SC:* the
  cluster-emergent statement is supported by the sub-groups; cross-sub-group findings genuinely cross-cut.
  *Gate — VCG-completion cross-check (the closing completeness check):* **(1)** citations cover **all
  verses** (every verse dealt with — cited / set-aside / rerouted); **(2)** every finding has **≥1 anchor**
  AND every **anchor used ≥1** (each `is_anchor` verse in ≥1 `finding_citation`); **(3)** **no orphaned VCGs
  or sub-groups** (every VCG in a sub-group + observed; every sub-group has a characteristic/cluster home);
  **(4)** **all BOUNDARY terms resolved** — placed / rerouted / set aside; **the audit must reveal any
  orphaned term** (E5); **(5)** **zero orphans overall**.
- **L7 (cluster synthesis)** · *Needs:* L6 PASS. *FC:* `char_structure`/`description`/`status` firmed;
  cluster-level findings cited; **every finding typed + cluster-anchored**. *SC:* the synthesis is supported
  by L6. *Gate (A4 cluster confirmation):* cluster account complete → **all findings submitted as a group →
  `confirmed`** = the **cluster sign-off**.
- **L8a (within-cluster cross-cluster finding generation, at cluster close)** · *Needs:* this cluster's
  findings. *FC:* every finding that implies a cross-cluster finding **has** one (outbound completeness).
  *SC:* the generated cross-cluster findings land in the correct other cluster. *Gate:* no implied
  cross-cluster finding missing.
- **L8b (study-level cross-cluster reconciliation, once all clusters done)** · *Needs:* **all** clusters PASS
  L7 + L8a. one pass over all cluster-level findings → resolve additional cross-cluster findings / adjustments
  (depends on B2/B3 mechanics).

## 9. Open questions

- **Threshold values** per SC check (start 5%, tune).
- **Sample size N** per term/cluster (power vs cost).
- **Audit cadence** — per-level gate vs on-demand vs both.
- **Where audit results live** — a `cluster_audit_run` table (level, check, result, scope, gaps) so PASS/FAIL
  is queryable and re-runs are comparable.
- **`stem_label` / sense→pole prerequisites** (R6/R7) must land before SC-L1-2/5 are fully mechanical.

---

## Recommendation / next build

L1 is designable into a script **now**: all FC-L1-* are SQL, and SC-L1-1's pre-screen already exists
(`_assess_verse_corroboration.py`). The natural next artifact is `scripts/_assess_cluster_compliance.py
--cluster M01 --level L1`, emitting the §3 grid. But note: it audits against the v3 *target* schema (the new
`verse_context` fields), so it can only run for real **after** R3/R7 land the fields and a cluster is taken
through the v3 L1 mechanical step. Until then, this spec is the contract the v3 instruction must satisfy.
