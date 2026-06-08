# V3_2 L1/L2 architecture — synthesis from the prototyping session

> **Investigation · v1 · 2026-06-08 · CC.** The researcher's reflection after the P1/P2 prototyping
> (keywords · morph · sense-branch · scenario-typing · meaning run): the L1/L2 cycle is the crucial,
> failure-prone, *iterative* core of the study, and V3_2 must be built as a **multi-angle report pipeline
> whose results are synthesised into the DB update** — not a single mechanical pass. This consolidates the
> prototype learning into that architecture. **Input to the V3_2 update** (the planned "reread → update
> V3_2" step); not yet merged into the canonical rollup-design/instruction.

---

## 1. Three governing realisations (researcher, 2026-06-08)

a. **The L1/L2 cycle is crucial — and the most likely point of failure/oversight in the earlier research.**
   Verse meaning is the data; getting it wrong silently corrupts everything downstream. (Confirms
   verse-meaning quality as the gravest data risk — `project_next_action_audit_surface_verses`.)

b. **It is iterative between CC and researcher** — several review rounds per cluster, **partly to hone the
   scripts, partly to handle the many variations and situational differences**. Not a one-shot run. The
   prototypes proved this: each pass surfaced a real variation (homonym, within-stem shade, source-scope,
   qualifier co-presence) that only a review round caught.

c. **V3_2 builds on the prototype learning, but must (i) emit reports on the different angles, then (ii) build
   on *all* the angle results to generate the final output for the DB update.**

## 2. The angles the prototypes surfaced (each = an independently reviewable / honable report)

| Angle | Establishes | Report (per cluster) | Still to hone |
|---|---|---|---|
| **A · Morph → stem** | per-verse stem, 100% coverage | stem distribution | Greek decode (tense/voice/mood) |
| **B · Sense-branch parse** | BDB (Qal/Niphal/Piel) branch + within-stem shade count + homonym watch | applied branch + **shade-residue** + homonym flag | BDB-block parse edge cases |
| **C · Keyword build + self-check** | whole-word keywords, asserted clean | keyword list + self-check PASS/FAIL | source-scope normalise · concatenation clean |
| **D · Keyword digestion** | overlap→sub-group seeds · divergence→role flags · size→polysemy | sub-group seeds + role/relevance flags | family cut-lines |
| **E · Scenario typing** | S0–S6 per verse (relevance · multi-term · qualifier co-presence · cross-cluster) | type-vector distribution + worklists | qualifier-enhance vs incidental |
| **F · Span / qualifier-attach** | `span_strong_match` co-span | attach candidates | enhance-test (§6.4) |

## 3. The shape: report-per-angle → review → synthesise → DB

```
L1  (mechanical angles, each emits a per-cluster REPORT)
      A morph · B branch · C keyword · E typing · relevance gate
      → L1 NARROWS: stem branch, type-vector, clean keywords, residue worklists
      → it does NOT decide the residues; it surfaces and counts them

   ── REVIEW GATE 1 ── researcher inspects the angle reports; scripts honed;
                       situational variations captured as handled cases

L2  (SYNTHESIS — build on ALL angle results + the verse read)
      resolve the residues: within-stem shade (fear↔reverence) · qualifier-route ·
      cross-cluster reciprocal · homonym/numbered-sense · multi-term pairing
      → produce the FINAL per-verse output: applied meaning · keywords · sub-group ·
        routes · findings · open-questions

   ── REVIEW GATE 2 ── researcher inspects the synthesis

DB UPDATE  (single write step, from the synthesised result)
```

This is the **type → modules → synthesise** of [[project_p2_l2_decision_architecture]], now **fed by explicit
angle reports** and **bracketed by two review gates**.

## 4. Implications for the V3_2 script

1. **Not one pass — a pipeline of angle-reports + a synthesis step, with two review gates.** The "write to DB
   then report" principle applies at the *synthesis* step; the angle steps are read-only reports.
2. **Each angle is an independently runnable, independently honable sub-command.** A weak angle (e.g. Greek
   morph, keyword source-scope) is re-run/honed without re-running the whole cluster.
3. **Residues are first-class L1 outputs** — flagged, counted, listed — so L2 gets a precise worklist
   (e.g. "190 ya.re verses need the fear↔reverence shade call"), never a blank verse.
4. **Iteration is designed-in.** Expect several CC↔researcher rounds per cluster early; the scripts and a
   **handled-variation catalogue** grow over rounds. Speed comes later, from the catalogue, not from
   skipping the read.
5. **The synthesis is the only DB writer.** Angles never write; they inform. This keeps the verse-meaning
   write auditable against the angle reports that justified it.

## 5. What this does NOT change

- Verse meaning still rules; the angles are *structural inputs*, the verse read decides (the two governing
  principles). Morph/keyword/typing **narrow**; they never **overrule** the read.
- No forced structure: variation/ambiguity/open-questions are expected and recorded, not tidied away
  (`feedback_no_forced_structure_audit_surfaces_analysis_compensates`).

---

*Next: fold §3–§4 into the V3_2 instruction/rollup-design at the planned reread→update step. The prototype
scripts (`_prototype_step_morph` · `_prototype_meaning_run` · `_prototype_p1_keywords` ·
`_assess_p2_verse_scenarios`) are the seeds of the angle sub-commands.*
