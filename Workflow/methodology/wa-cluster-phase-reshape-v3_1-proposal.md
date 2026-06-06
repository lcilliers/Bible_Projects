# Cluster phase reshape — verse meaning moves out of Phase A into the VCG process (v3_1 proposal)

> **Living document · Doc version: 1 · 2026-06-06 · DRAFT for review.** Reshapes v3_0 §5 (Phase A) and §6
> (Phase B) per `feedback_phase_a_light_meaning_at_vcg`. **Phase A becomes light similarity-only; the
> verse-meaning discipline (`wa-verse-analysis-methodology.md`) is built into the VCG process.** Not yet
> applied to the live v3_0 instruction — for review, then fold into v3_1.

## Why (the evidence)

- The **4-verse reality test** (2026-06-05): deriving a full meaning **early, per-verse, in isolation**
  reproduced the §0 AI biases — wrong 4/4. (`feedback_term_corpus_anchors_meaning`)
- The **M10-D and M10-H VCG-redo tests**: reading the **actual verses together** produced honest,
  sense-true groups, reunited a split inner core, and surfaced scope errors the early lexical/keyword
  signal missed — *most* valuable exactly where that signal was least reliable (M10-H).
- Conclusion: **don't commit meaning early.** Derive it at the VCG stage, from the actual grouped verses.

## The reshape at a glance

| | v3_0 (now) | v3_1 (reshaped) |
|---|---|---|
| **Phase A (§5)** | Read + **meaning + keywords** | **Read + *light similarity*** — meaning **removed** |
| **Phase B / VCG (§6)** | meaning *grouping* (consumes the pre-derived meaning) | grouping + **the verse-meaning discipline derived here, from actual verses** |

---

## NEW Phase A — Read + light similarity  *(replaces v3_0 §5)*

**Owner:** CC (programmatic). **Purpose:** classify relevance and emit a **light similarity signal** good
enough to group similar verses — **no interpretive meaning is committed.**

- **A.1 Relevance review** *(unchanged)* — classify each verse `IB` (`is_relevant=1`) or set-aside
  (`is_relevant=0` + `set_aside_reason ∈ {no_inner_being | physical_only | spatial_only | unclear}`).
- **A.2 Light similarity signal** *(replaces "Pass A meaning + keywords")* — emit **only a surface signal**
  sufficient for preliminary grouping: candidate **atomic keywords / lexical features / span + term + root**.
  **Not** a meaning sentence; **not** an interpretive reading.
  > 【DECISION】 **What the signal is** — atomic keywords (the original clustering design), or lexical/root
  > features, or both. This is the parked keyword question resolved *into its proper role*: Phase A gets the
  > **light/atomic** keywords (the clustering signal); the **rich** interpretive keywords + meaning are a
  > VCG-stage output. Settle the exact signal here.
- **Output:** `is_relevant`, `set_aside_reason`, the light similarity signal. **No `analysis_note` meaning.**
- **Gate:** every `is_relevant` verse carries a similarity signal.
- **Status:** `Not started`/`Data - In Progress` → `Data - In Progress`.

---

## NEW VCG process — read the actual verses, derive meaning in context  *(within Phase B / §6.3)*

**Purpose:** form VCGs by reading the **actual verse texts** of a group **together**, and **derive the
verse meaning here, late and grounded** — applying the verse-meaning discipline
(`wa-verse-analysis-methodology.md`), **not** a pre-derived per-verse meaning, **not** just the anchor.

- **Inputs:** the **actual verse texts** of the population (the sub-group — feasible: M10's largest is 205
  verses ≈ one pass), the spans **tagged T1 / T2 / FLAG**, and the **term corpus** for clarification. The
  light similarity signal seeds the *preliminary* groups; inherited structure stays suppressed.
- **Process (the discipline, per `wa-verse-analysis-methodology.md`):**
  1. **Read the actual verses of the population together** — not the meaning, not just the anchor.
  2. Apply the **span-focal Seven Principles** + **span influence-test** (weave T2/T1 only when it
     influences; independent siblings flow through) + **surroundings (from/to)** + **clarify-by-corpus**
     (the term's other occurrences settle valence/sense) + **open questions** where unsettled.
  3. **Classify scope by the 3 poles** — **inner-being core** vs **external pole** (imposed consequence) vs
     **physical pole** (bodily/cosmic decay); external/physical are **cross-referenced**, not housed as
     inner (`feedback_external_pole_not_inner_state`).
  4. **Form / refine VCGs by sense-in-context** — verses with the same *application of the term* grouped;
     each VCG gets an anchor. (Groups are derived from the reading, then human-confirmed.)
  5. **Derive the verse meaning** (`analysis_note`) **here**, from the actual-verses reading — including the
     paired T2 expansion and any named T1 sibling.
- **Flags & pointers — surface here, adopt at findings.** The VCG process **surfaces** the cluster's
  term-anchored pointers/flags for the verses it reads (`SD_POINTER`, `SB_FINDING`, `VERSE_EVIDENCE_*`
  notes) — never silently ignored (no-orphans) — and **establishes the verse evidence that validates them.**
  It does **not adopt** them: adoption into a finding (xref + close) or set-aside stays at the **findings
  stage (Phase D)**, which is the output unit (audit A6/A7/D2 enforce it). Other flag types resolve
  elsewhere: `PH2_*` data-quality in structural cleanup (Phase C); `BOUNDARY_DECISION_PENDING` in
  constitution / sub-group design (upstream). *(Flags/pointers are term/registry-anchored via
  `strongs_reference` + `cluster_link`, not verse-anchored.)*
- **Complexity triage** (possible-set-aside / single-span / T2+T1 / multi-T1) scales the effort; multi-T1
  reuses a prior combination's meaning rather than redesigning.
- **Outputs:** VCGs (from actual verses) · the derived meanings · scope-pole classifications + cross-refs ·
  open questions (the corroboration worklist) · reciprocal finding-seeds for influencing multi-T1 siblings.
- **Gate:** every `is_relevant` verse is in a VCG; every VCG anchored; meaning derived; scope poles
  classified; open questions recorded.

---

## Emergent aggregate questions — the structured fix for "general observation" drift

**The past failure:** "cluster-level" / "general observation" was an **unstructured catch-all**. An
observation that belongs to a *collection* (true of the whole, not of any single member) had **no specific
home** — so it drifted, got mis-assigned, or was lost. This caused many of the historic misses.

**The fix (researcher, 2026-06-06):** ask an explicit **emergent question at each aggregation rung**,
anchored to that level's members, and record the answer as a **level-anchored observation**:

1. **Verses → VCG:** *What does this collection of verses jointly say about the VCG that no single verse
   captures?* (not every verse gives the complete picture). → recorded **on the VCG**.
2. **VCGs → sub-group:** *What do these VCGs jointly say about the sub-group — how do its dimensions operate
   together?* → recorded at **sub-group** level.
3. **Sub-groups → cluster:** *What do these sub-groups jointly say about the cluster — how do they operate
   together?* → recorded at **cluster** level.

Each answer is an **emergent observation** — true of the collection, not reducible to the parts — and now
has a **definite home** (no drift). The aggregate Q&A runs **up** the ladder as the VCG read completes and
the structure firms.

**The payoff — characteristics EMERGE.** The sub-group and cluster aggregate questions ("how do these
operate together") are exactly the questions whose answers *are* the characteristics. So the characteristic
structure **crystallises bottom-up from the data — discovered, not imposed** (resolves foundations §c-Q4 and
the forced-structure risk). This is the mechanism by which `feedback_phase5_subgroups_represent_characteristics`
actually happens, instead of being pre-designed and back-filled.

**Recording surface:** `cluster_observation` already anchors at `cluster_code` / `characteristic_id` /
`cluster_subgroup_id`, and its existing types (`CLUSTER_SYNTHESIS`, `INTER_RELATIONSHIP`, `INTEGRATION_NOTE`)
are exactly these emergent observations — they were just **unstructured by level**. The ladder structures
them.
> 【DATA GAP】 `cluster_observation` has **no VCG (`group_id`) anchor** — a VCG-level emergent observation
> needs either a `group_id` column on `cluster_observation` or a home on `verse_context_group`
> (`context_description` / `notes`). Small schema decision to resolve.

## Knock-on & open items (for the review)

1. **B.1 constitution debate + B.2 sub-group design** currently consume the **Pass A meaning corpus**
   (v3_0 §6.1/§6.2). With meaning removed from Phase A, they must run on the **light similarity signal +
   the actual verses** (preliminary grouping), with the meaning **firming at the VCG read**. *This needs its
   own reshape pass — flagged, not yet drafted.*
2. **Phase A's exact light-similarity signal** — the 【DECISION】 above.
3. **Field reconciliations** (carried): `analysis_note` vs `meaning_pass_a`; `is_relevant`+`set_aside_reason`
   vs a `ut_class` column.
4. **Keyword two-role split is now resolved by structure:** light/atomic keywords = Phase A (clustering);
   rich descriptive meaning + keywords = VCG output.

## Sources
- `wa-verse-analysis-methodology.md` (the VCG-stage discipline) · `feedback_phase_a_light_meaning_at_vcg` ·
  `feedback_term_corpus_anchors_meaning` · `feedback_external_pole_not_inner_state` ·
  `feedback_span_pairing_and_reciprocal_findings`.
- Evidence: `research/investigations/verse-analysis-methodology-test-20260605.md`,
  `…/m10d-vcg-redo-test-20260605.md`, `…/m10-h-vcg-redo-test-20260605.md`.
