# Obslog — M01 OLD vs NEW findings comparison

- Reference: m01
- Session topic: oldnew-cmp (old/new findings content comparison)
- Version: v1 · Date: 2026-06-19
- Prior output context: builds on the two attached extracts — `WA-m01-findings-OLD-dbexport-bytier-v1-20260619.md` (DB export of `cluster_finding`, 7-characteristic model) and `WA-m01-findings-NEW-merged-bytier-v1-20260619.md` (2026-06-18 authoring, 11-characteristic model).

## Session startup
- Global rules `wa-global-rules-all-v2-20260427.md` loaded — 34 rules / 12 categories.
- Obslog initialised (this file).
- Cadence discipline M1+M4 active.
- Prefix confirmed: WA.

## Task (researcher, verbatim sense)
Compare M01 OLD findings vs NEW findings. Focus on *content*, not statistics. Researcher expectation: "ultimately there should not be a large difference between the two in principles." Wants Claude's perspective on the differences and a sense of where they diverge.

## What was read
- OLD file in full (1955 lines). NEW file in full (1994 lines).
- Header-grep on both confirms identical tier-question catalogue T0.1.1 → T7.3.4; same 47 `[refit]` questions in both.

## Observations (grounded in the two files)
1. **Characteristic model differs — the dominant structural difference.** OLD = 7 named characteristics (M01-A Reverential Fear … M01-G Timidity), thematic/phenomenological, organised around VCGs with anchor verses. NEW = 11 characteristics (c1 reverent fear … c11 cowardice), lexically/term-anchored and more granular.
2. **Capture mode differs.** OLD = consolidated whole-cluster row + one row per sub-group per question (heavy verbatim repetition where consolidated text copied into each sub-group). NEW = one finding per question, with explicit per-characteristic (c1–c11) breakdown. NEW carries spliced Session B "folded" findings in OLD (e.g. DIM-61-001 fobeō tripartite) — actually present in OLD, not NEW.
3. **Grounding differs.** OLD = theological synthesis from VCG anchors and verse readings; few raw counts. NEW = quantitative JSON-field grounding (valence counts, divine_involvement, type distribution action/status/quality, location counts, immediate_response fill rates) + verbatim verse quotes.
4. **Substantive principle-level AGREEMENT confirmed on the core spine:** (a) fear never borne by God as experiencer — creaturely; (b) reverent fear of God = the one positively-ordered / created-design form; (c) heart is the dominant constitutional seat; (d) cluster is overwhelmingly NOT spirit-level; (e) Isa 66:2 trembling is the clearest spirit-level case; (f) reverent fear is epistemologically/relationally constitutive; (g) cowardice/timidity = the disordered pole answered by 2Ti 1:7.
5. **Genuine content DIVERGENCES flagged for researcher:**
   - **Mind-location.** OLD: mind is "a secondary but evidenced" location (M01-D dismay, M01-F anxiety). NEW: mind = **0 across all 11** ("never a recorded location"). Direct conclusion conflict — flows from interpretive-reading (OLD) vs location-field-literal (NEW).
   - **Second spirit-level case.** OLD: 2Ti 1:7 timidity counted as spirit-level (M01-G). NEW: c11 cowardice **silent** on spirit-level; instead Ecc 7:9 (bahal) for c7 dismay is the 2nd spirit case. Likely OLD read "spirit God gave" as constitutional-location; NEW reads it as the Spirit's gift, not a location claim.
   - **Granularity of conclusions.** NEW separates dread (c3) / terror (c4) / shuddering (c6) / alarm (c8) / astonishment (c10) that OLD folds into M01-B and M01-C. NEW therefore surfaces distinctions OLD's coarser grouping cannot (e.g. c4 terror reaching the soul ≥ heart; c9 anxiety near-total divine silence).
6. **Naming-convention note.** Uploaded files use `WA-...-v1-...` (uppercase prefix, single-component version). GR-FILE-003/007 require lowercase + `v1_0`. Flagged; not actioned (the upload names are the researcher's).

## Decision point raised to researcher (see chat)
The map between the 7 OLD characteristics and 11 NEW characteristics, and the handful of true conclusion-divergences (mind-location; second spirit case), are interpretive forks. Paused for researcher direction on whether to (a) produce a full reconciled crosswalk, (b) drill the divergences, or (c) something else.

## Writes this session
- This obslog: `wa-obslog-m01-oldnew-cmp-v1-20260619.md`
- Deliverable: `wa-m01-oldnew-findings-cmp-v1_0-20260619.md`

---

## Researcher questions (2026-06-19) — verbatim sense
Aim restated by researcher: findings must be a self-sufficient grounding layer for generating various prose/essays WITHOUT returning to source. Redo was chosen because OLD findings had (i) bias, (ii) conclusions not grounded in verse evidence, (iii) missed verses from incomplete analysis. New lexical method designed to mitigate all three.
(a) Should the NEW findings go through another synthesis layer before they are prose-ready?
(b) Should BOTH datasets be retained in the DB as grounding for prose?

## Claude AI assessment — recorded for audit

### (a) Synthesis layer — assessment: YES, but thin and discipline-bound; two sub-needs to separate.
- Observation: NEW findings are organised by TIER QUESTION (T0.1.1…T7.3.4), per-characteristic (c1–c11). Each question already carries a cluster-level horizontal synthesis (the opening "Finding."). What is MISSING for prose: (i) vertical per-characteristic synthesis (c1's whole picture across all tiers — currently scattered across ~150 questions), and (ii) thematic synthesis (claims grouped by theme, not by question).
- Interpretation: prose is organised by theme/characteristic; findings are organised by question. That axis-gap + missing connective tissue is the prose-readiness gap. The OLD set HAD this synthesis (consolidated rows) — and that is exactly where its bias/ungrounded conclusions entered. So a synthesis layer is a CONTROLLED RISK.
- Two separable sub-needs: (1) RE-ORGANISATION (question-axis → characteristic/theme-axis) — low risk, mechanical; (2) CONNECTIVE SYNTHESIS (cross-question/cross-characteristic conclusions) — higher risk, the bias re-entry point.
- Recommendation: if cross-cutting prose is intended, add a thin synthesis layer bound by a NO-NEW-CLAIMS rule — every synthesised statement resolves to ≥1 grounded finding (→ verses); inferential material kept labelled per GR-PROG-009. This may already be Session C's role (GR-PROG-004: Session C primary). Decision needed: formalise an intermediate "consolidated findings" artifact, OR let Session C carry synthesis per-essay (risk: per-essay drift / re-introduced bias).
- Data needed: what KINDS of prose are envisioned (drives synthesis depth).

### (b) Retain both as grounding — assessment: NO (not both as grounding). Retain OLD as reference-only/superseded.
- Principle basis: GR-DATA-002 (current extract authoritative; prior outputs reference-only) + GR-REF-001 (single authoritative document per content type). Two parallel grounding datasets violates single-authority and lets authors pull from whichever supports a claim — re-introducing the bias the redo removed. OLD is KNOWN-FLAWED as grounding (researcher's own reason for redo).
- But OLD has residual value: audit (did NEW recover all genuinely-grounded OLD content?), provenance, and ORPHANED content (folded Session B findings e.g. DIM-61-001 absent from NEW).
- Recommendation: NEW = single authoritative grounding for prose. OLD = retained but marked superseded/reference-only, NOT a grounding source. Precondition: a reconciliation pass to rescue any grounded-and-valid OLD content (esp. folded Session B findings) into NEW BEFORE demoting OLD.
- DB caution: GR-DB-001 — do not assume the findings-table schema or whether a status/superseded field exists; confirm with CC. GR-PROG-005 — retention/marking is a decision (CAI advises, researcher decides); the DB operation is CC's via patch/directive.

## Open items raised to researcher (chat)
- Decide (a): formalise intermediate consolidated-findings artifact vs Session-C-carries-synthesis; and which prose types are in view.
- Decide (b): confirm NEW-as-sole-grounding + OLD-as-reference-only, with a reconciliation pass first.
- Confirm NEW field counts against the current versioned extract (GR-DATA-004) before any reconciliation is acted on.

## Writes this turn
- This obslog (appended): wa-obslog-m01-oldnew-cmp-v1-20260619.md

---

## Phase: synthesis authoring (researcher instruction 2026-06-19)
Researcher confirmed direction: M01 needs more synthesis to found the essays. Requested:
(a) ONE cluster-level synthesis across all tiers, all characteristics.
(b) ONE per-characteristic synthesis across all tiers, as SEPARATE files (c1–c11).
Offered additional source material if needed.

### Source sufficiency
- Grounding source = NEW findings file (full, in context). No additional source required.
- Caveat: working from the merged-by-tier file (derived from WA-m01-findings-t0..t7-v1_0-2026-06-18.md). If content was lost in the merge it would not be visible; merge appears complete (1 finding/question, all tiers).

### Authorship decisions (specialist calls, GR-HF-001 — not escalated)
- Format: structured markdown grounding documents (not Session C essays). GR-FILE-005.
- Discipline: NO-NEW-CLAIMS. Every claim resolves to a finding; tier-refs (T-x.x) + the findings' verse anchors carried for traceability (GR-PROC-002). Inferential/silence labels preserved (GR-PROG-009).
- Read completeness: entire NEW file read in full before authoring (T0–T7 + cross-cluster register).

### Files to produce (dual-write; lowercase; compact date; v1_0)
- wa-m01-cluster-synthesis-v1_0-20260619.md
- wa-m01-c01-reverent-synth … c11-cowardice-synth -v1_0-20260619.md (11 files)

### Findings spine carried into synthesis (grounded)
- God never experiencer (0/975); object/agent/giver only (T0.1.2/T4.1). Two-faced divine disposition: inflict on enemies / liberate his own (T4.1.3).
- Valence is the discriminator: c1 created-design/commanded-righteous; most fallen-response/neutral; c11 vice; c9 creaturely-neutral (T0.2).
- Image: only c1 positively instantiates (T0.3.1).
- Constitution: heart dominant (61 located records); MIND = 0 across all 11 (T2.4); not spirit-level except c5 Isa 66:2 + c7 Ecc 7:9 (T2.1); soul sparse, c4 notable (T2.2); body-crossing c5 (T2.6/2.7); origin received-from-outside (T2.9); movement inner→outer c5 / external-onto-person (T2.10).
- Faculties: constitutively affective all 11 (973/975) (T3.4); cognition c9 thinks / c1 knows / terror-alarm pre-cognitive (T3.2); volition+agency: reverent mobilises, terror/dismay/alarm disable (T3.6/3.7); perception triggers ordinary fear (T3.1); moral-eval concentrated c1/c11 (T3.8); creativity/conscience near-silent (T3.5/3.9).
- Relational: God largest object (203) (T4.2.1); "fear not" address = c2 mode (T1.4.3/T4.4); idolatrous fear forbidden (T4.6); spirit of bondage Rom 8:15 (T4.6.2).
- Over time: no transformation arc in lexicon (T5.1); suffering/Job strong signal (T5.4); sanctification only c1 inferential (T5.5); eschatology = judgement-orientation c2/c4/c5 (T5.6).
- Architecture: terror-complex c2/c3→c5→c6, c4/c7 (T6.2/6.3); shared roots yare/pachad/chatat (T6.4); hub characteristic; partners shame/wisdom/righteousness; foils peace-rest-trust (T6.1).
- T7: genre spread all major genres (T7.2.2); science — somatic density high, normativity divergence, vertical dimension (T7.3).
- Central seam: same affect named reverent when Godward/ordered, fear/terror/dread when threat-facing (T1.1.1/T6.4.3).
- Cross-cluster register (X1–X10) held → Session D.

### Synthesis authoring — COMPLETE (2026-06-19)
Produced and dual-written (working dir + outputs), all v1_0, lowercase, compact date:
1. wa-m01-cluster-synthesis-v1_0-20260619.md (cluster-level, all tiers, all 11 chars)
2–12. wa-m01-c01-reverent / c02-fear-afraid / c03-dread / c04-terror / c05-trembling / c06-shuddering / c07-dismay / c08-alarm / c09-anxiety / c10-astonishment / c11-cowardice -synth-v1_0-20260619.md
Per-characteristic files vary in length by evidential density (c1/c5/c2 fullest; c6/c8/c10/c11 thinner) — honest to findings.
Discipline applied: no-new-claims; every claim tier-tagged + verse-anchored to findings; inferential/silence labels preserved. Entire NEW findings file read in full before authoring.
Source caveat recorded: synthesised from merged-by-tier findings; counts inherited; would update if findings corrected vs current extract (GR-DATA-004).
Recorded divergence carried into c11 file: 2Ti 1:7 "spirit" treated as Spirit's gift, not spirit-location (NEW method); differs from OLD which read it as spirit-level location.

### Items flagged to researcher (chat)
- These are the grounding/foundation layer (per (a) decision); not Session C essays.
- Question (b) (retain OLD as reference-only; reconcile before demote) still open — not actioned this turn.
- Counts unverified vs current extract (GR-DATA-004) — recommend CC confirm before these found published prose.

### Writes this turn
- 12 synthesis files (above) + this obslog (appended).
