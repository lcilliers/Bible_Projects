# Cluster Roll-Up Instruction — V3_2 (DRAFT)

> **Instruction · v3_2 DRAFT · 2026-06-07 · CC.** The operational procedure for running a cluster through the
> reshaped roll-up. **Design basis (rationale):** `wa-cluster-rollup-design.md` (v4, the V3_2 base) — this
> instruction is the *how-to-execute* of its §1–§9; do not duplicate the rationale, consult it. **Audit:**
> `wa-cluster-audit-design-v1`. **Schema:** requires the V3_2 fields (`wa-v3_2-schema-migration-plan-v1`) —
> **prerequisite, must be applied first.** Verse-meaning discipline: `wa-verse-analysis-methodology.md`.
> One open dependency: **B3** (L8b cross-cluster mechanics) — does not block L1–L7.

---

## 1. Scope & roles

Run **one cluster at a time**, level by level (L1 → … → L7 → L8a; L8b once all clusters are done). Each
level's `Output→next` is the next level's input. **Roles** (D1): the process is **run by CC with researcher
input**, referring select analytical operations to **AI** (API or chat, whichever is best). Per level:

| Owner | Levels / work |
|---|---|
| **CC (mechanical)** | L1 mechanical · L2 provisional partition · all gates' completeness checks · all DB writes · audit runs |
| **AI (analytical)** | L3 deep verse reading · L4/L5/L6 aggregate observations · finding authorship |
| **Researcher (judgement)** | every sign-off gate · the L1-ambiguity / pole-metaphor / reroute calls · cluster confirmation |

**Cost (D2):** submit a costing for any **API operation > \$2**; otherwise the researcher monitors
cumulative cost.

---

## 2. Governing operating rules (from the 7 disciplines)

1. **STEP-anchored meaning.** L1 meaning is built from the STEP sense-set; it cannot diverge from the lexicon.
2. **Never force-settle ambiguity.** L1 assigns **only the unambiguous**; **any potential double meaning →
   residue for L2.** *(This protects the discovery of unique characteristic scenarios — the study's greatest
   value. The L1-vs-L2 line turns on downstream mis-interpretation risk: a judgement, not a mechanism.)*
3. **One home per statement; findings level-anchored** (most L5, some L6/L7).
4. **Mop-up + no orphans** — every object consumed or named-and-linked; the L6 orphan-check is the closing
   gate.
5. **Forward enrichment; prior findings are inputs** — never discard; a material change re-opens the level.
6. **Task-level execution; coarse decision points.** Run **one command per level / sub-group cycle** that
   **performs the whole task, then reports the full result**. The researcher interacts at **gate boundaries
   with proper information**, not via a stream of pointed per-item decisions. *A need for fine-grained
   decisions signals an unrobust design — fix the design.* (L1 = one command → report → the **L1→L2 gate**
   is the first decision point; **L2 is the finalising "second round"**.)

---

## 3. Pre-flight (per cluster)

1. **Backup** the DB (off-Drive) before any write.
2. **Status** — record the cluster's starting state (fresh vs re-run; existing sub-groups / findings).
3. **PRE-L2 completeness — assemble the whole cluster in focus:** gather **terms · verses · flags · pointers
   · existing VCGs · previous findings** + the T2-surfaced candidate terms for this cluster. *(This is the
   precondition the L2 audit checks.)*

---

## 4. Level procedures

### L1 · Verse establishment (mechanical) — Owner: CC
**Inputs:** `verse_context` spans + `wa_verse_records` (+ STEP morphology) + the term's STEP sense-set.
**Procedure (per relevant span):**
1. **Phase-1 classify** — relevance (relevant vs set-aside reason) · UT (create a `verse_context` row for any
   untouched (verse,term) pair) · related-pass · light keywords.
2. **Attach** the STEP sense-set + STEP-capture keywords (apply the **noise + homonym filters**).
3. **Stem-narrow** — read the verse `morph_code` → `stem`; narrow the sense-set to the stem's branch
   (Hebrew; Greek has no stem aid).
4. **Assign-if-unambiguous, else residue** — one sense left → `step_meaning_applied` + `sense_id`. **Any
   residual ambiguity (within-stem multi, metaphor, double meaning) → `residue_flag=1`, NO assignment.**
5. **Pole** — default `inner`; literal-physical/external lexicons assign those; **heat/tremble/melt →
   `pole_is_metaphor=1`** (do not auto-assign physical).
**Writes:** `verse_context`: `is_relevant`, `set_aside_reason`, `step_meaning_applied`, `sense_id`,
`sense_multiplicity`, `step_envelope_note`, `pole`, `pole_is_metaphor`, `keywords`, `residue_flag`;
`analysis_note` **preserved**. `wa_verse_records.morph_code`/`stem`.
**Gate + A3:** run the audit (FC-L1-* + SC-L1-*). **Clean & no residue → researcher review → proceed;
clean & residue → L2; FAIL → remediation.** No `DIVERGENT` may arise here.

### L2 · Sub-group formation (provisional) — Owner: CC
**Inputs:** the PRE-L2 inventory + L1 establishments + similarity signal.
**Procedure:** partition the relevant verses/terms into **provisional** sub-groups from the L1 similarity /
keyword signal + term structure. Mark un-placeable terms **BOUNDARY**. *(If CC struggles on a fresh cluster,
hand the data to AI in chat — E1.)*
**Writes:** `cluster_subgroup` (provisional); `mti_term_subgroup`; BOUNDARY marks.
**Gate:** every in-focus item in a sub-group **or** cluster-level **or** BOUNDARY. Nothing unaccounted.

### L3 · VCG formation + deep verse reading *(per sub-group)* — Owner: AI
**Inputs:** the sub-group's verses + L1 establishments + residue flags; T1/T2/FLAG spans; the term corpus;
pointers.
**Procedure:** read the verses **deeply, together** (the verse-analysis methodology — Seven Principles ·
influence-test · clarify-by-corpus · 3-pole · open questions); form/refine **VCGs** by sense-in-context;
write the **rich `analysis_note`**; designate **anchors**. **Resolve the L1 residue here.** May **revise the
sub-group, reroute (term = unit of movement), or set aside** — and **reuse-vs-recreate per C2** (identical →
reuse; differs → surface the *why* to the researcher, then new + soft-delete old).
**Writes:** `verse_context_group`; `verse_context.group_id`, `is_anchor`, `analysis_note`, `keywords` (rich);
open questions → findings (E7). **Clarify-by-corpus across the unit → surface to researcher (C1).**
**Gate:** every sub-group verse in exactly one VCG (or rerouted/set-aside); every VCG ≥1 anchor.

### L4 · VCG-emergent observation *(per sub-group)* — Owner: AI
**Procedure:** per VCG, answer *what do its verses jointly say that no single verse captures?*
**Writes:** `verse_context_group.context_description` (the VCG-emergent observation — reused field).
**Gate:** every VCG has an emergent observation; not duplicated onto verses.

### L5 · Sub-group-emergent + findings *(per sub-group)* — Owner: AI → researcher gate
*Characteristic is assessed at L6 (after all sub-groups), NOT here (note 4, 2026-06-08).*
**Inputs:** the sub-group's VCGs + L4 observations + **prior findings for this sub-group** + routed pointers.
**Procedure:** answer *what do these VCGs jointly say about the sub-group?* → the sub-group's **emergent
meaning** (a *candidate* characteristic — not firmed here). **Submit findings (most land here):** answer the
**tier questions** (framework retained); validate/adopt pointers; **evaluate + refine prior findings**;
create findings (incl. **into other clusters**). **VCG re-evaluation:** compare against existing VCGs and
present a **side-by-side new/changed/set-aside surface** for the researcher (M01 note 3).
**Writes:** `cluster_subgroup.core_description`; `cluster_observation` (sub-group); `cluster_finding`
(`finding_type`, scope anchor, `finding_status=draft`, `needs_research` for open questions) +
`finding_citation`; `wa_session_research_flags.resolved`; prior findings refined; cross-cluster findings.
*(No `characteristic` write here.)*
**Gate (A4):** every pointer / prior-finding evaluated; **findings → draft, submitted for researcher review →
reviewed before the next sub-group.** **↻ next sub-group → L3.**

### L6 · Characteristic assessment + cross-sub-group + closure — Owner: AI → researcher
*(after ALL sub-groups)*
**Procedure:** **(1) assess characteristics** over the whole set — map sub-groups → characteristics (1:1
default; split only where forced), name/define, firm the characteristic structure (note 4); **(2)** answer
*what do the sub-groups jointly say about the cluster?* → submit cross-sub-group findings; adopt remaining
pointers; **(3) run the orphan check**.
**Writes:** `characteristic` + `characteristic_subgroup`; `cluster_observation` (cluster); `cluster_finding`
(cross-sub-group); pointers resolved.
**Gate — closing cross-check (all hold):** (1) citations cover **all verses**; (2) every finding has ≥1
anchor & every **anchor used ≥1**; (3) **no orphaned VCGs/sub-groups**; (4) **all BOUNDARY terms resolved**
(audit reveals any orphaned term); (5) **zero orphans overall**.

### L7 · Cluster synthesis + science — Owner: AI → researcher confirmation
**Procedure:** firm the cluster account; submit cluster-level-only findings (`intra_cluster`); consolidate
the **characteristic structure**. **Science layer (F1):** correlate the findings with the per-cluster
science extract (Scripture-primary, light-touch) → **science-derived findings**.
**Writes:** `cluster.description`/`.char_structure`/`.status`; `cluster_finding` (intra-cluster + science).
**Gate (A4 cluster confirmation):** **all findings submitted as a group → `confirmed`** = the cluster
sign-off.

### L8a · Cross-cluster finding generation *(at cluster close)* — Owner: CC + AI
**Procedure:** re-evaluate every finding → confirm **every cross-cluster finding it should generate has been
generated** (into the other clusters). **Then the cluster is ready for publication input-folder generation
(F2).**
**Gate:** no finding implying a cross-cluster finding left without one.

### L8b · Study-level cross-cluster reconciliation *(once all clusters done)* — **〔open: B3〕**
A single pass over all cluster-level findings to resolve additional cross-cluster findings/adjustments;
interdependent clusters finalise together (B2). **Mechanics open (B3) — does not block L1–L7.**

---

## 5. Finding model & lifecycle (operating rules)

- Every finding has a **`finding_type`** (tier / cross-VCG / cross-sub-group / intra-cluster / cross-cluster),
  a **scope anchor** (cluster required; sub-group / VCG per type), and a **`finding_status`**.
- **No finding without a cluster.** **Every open question is a finding** flagged `needs_research`.
- **Lifecycle:** `draft` (created) → `reviewed` (per-sub-group gate) → `confirmed` (cluster gate).
- Findings are **level-anchored** — submitted where they first become true; never restated up/down.

---

## 6. Re-run / idempotency (E2)

- The V3_2 process **re-runs any cluster and respects what is already done.**
- The **reason for a re-run must be clear and testable against this instruction before executing**
  (e.g. "a material verse-meaning change staled findings X").
- **Supersession:** soft-delete only; re-homed members in the same pass; a material verse-meaning change
  **re-opens** the affected level and stales its findings.

---

## 7. Prerequisites & open items

- **Schema:** the V3_2 fields must be migrated first (`wa-v3_2-schema-migration-plan-v1`).
- **Data population** (runs within L1 of the first cluster): `wa_meaning_sense.stem_label`,
  `wa_verse_records.morph_code`/`stem`, `wa_meaning_sense.is_homonym`.
- **First run target:** **M01 re-run completely** (R5); the M01/M02 prototype artifacts are investigatory,
  set aside.
- **Open:** B3 (L8b mechanics); the `〔CONSULT〕` schema details in the migration plan.

---

*DRAFT — for researcher review. Once the schema is migrated and B3 / the schema `〔CONSULT〕` items are
settled, this becomes the operative V3_2 instruction and M01 is the first cluster run.*
