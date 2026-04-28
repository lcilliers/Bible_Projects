# DB Capture Architecture — Approach Comparison

**Document version:** v1
**Date:** 2026-04-27
**Author:** Claude Code, under researcher direction
**Linked predecessor:** `wa-obslog-ro-067-goodness-anlys-v2-20260426.md` §"Design Discussion — DB Capture Architecture" (lines 3021-3084)
**Status:** Working analysis — for researcher decision

---

## The two approaches

### Approach (a) — AI obslog → CC parse-and-import

- **AI's role:** produce one comprehensive obslog per session. Narrative + structured sections (SD pointer table, Q&A entries, chapter prose). Same artefact that's already produced today.
- **CC's role:** build parsers and validators that read the obslog and emit DB writes. CC owns:
    - Schema awareness for every category (SD pointers, findings, prose, catalogue, dimensions, status)
    - Validators that confirm completeness ("all 147 questions have a disposition", "all chapters drafted", "all dimension assignments resolved")
    - The parser that lifts structured fields out of the obslog and writes via the existing applicator
- **AI never touches JSON patches.**

### Approach (b) — AI obslog + AI patches per instruction

- **AI's role:** produce obslog AND construct JSON patches alongside (current pattern, formalised). Patches conform to `wa-patch-instruction` per category.
- **CC's role:** apply patches via the existing applicator. CC validates patch JSON shape (already does this) but does not interpret obslog content.
- **Instruction must specify patch construction in detail for every category** — including the four current gaps (CAT-B-001, CAT-C-001, CAT-D-001, CAT-E-001).

---

## Cost dimensions

### Per-session cost (recurring across ~200 words)

| Item | (a) | (b) |
|---|---|---|
| AI tokens for analytical work | Same | Same |
| AI tokens for patch construction | **0 — AI doesn't construct patches** | Substantial — 7 categories × patch JSON, with strict field shapes |
| AI tokens for obslog formatting | Slightly higher (more rigid template) | Same as today |
| CC compute (parsing obslog) | Real but bounded | Near-zero |
| CC compute (applying patches) | Same | Same |
| Researcher review of patches | Lower — review obslog only | Higher — review obslog + patches |
| **Net per-session AI token estimate** | ~50-65% of current | Current (100%) |

### One-time / capability cost

| Item | (a) | (b) |
|---|---|---|
| Parser script build | **High — one-time** | Not needed |
| Parser maintenance (when obslog format shifts) | Recurring small | None |
| Instruction expansion for new categories | Low (loose obslog format) | High (strict patch spec per category) |
| Instruction-gap closure cost (CAT-B/C/D/E-001) | Avoided — instruction stops being patch-shape-spec | High — must close all four gaps before scaling |
| AI training drift risk (patch format) | **Eliminated** (no AI patches) | Recurring — AI must keep current with v2_9, v3, v4… |

### Risk profile

| Risk | (a) | (b) |
|---|---|---|
| AI patch malformation | None | Real (memory: project already has documented "patch format errors" feedback) |
| Silent data loss via parser miss | Real — parser must recognise every category | None — applicator validates schema |
| Schema evolution cost | Parser update | Instruction update + AI re-alignment |
| Compliance breach risk (write-on-discovery) | **Lower** — AI focuses on analytical work | Higher — patch construction creates "save it for later" temptation (this session's compliance breach record cites exactly this) |
| Researcher reviewability | Single artefact (obslog) carries the audit trail | Two artefacts (obslog + patches) must be cross-checked |

---

## The natural division of labour

| Agent | Strength | Best applied to |
|---|---|---|
| **Claude AI** | Narrative synthesis, theological judgement, characteristic-perspective grouping, anchor-verse reading, cross-registry vision | Analytical work + structured observation in obslog |
| **Claude Code** | Schema awareness, JSON validation, transactional writes, deterministic transformations, audit trails | Mechanising DB persistence |

Approach (a) maps cleanly to these strengths. Approach (b) makes the AI do dual work — analytical (its strength) AND structural-mechanical (CC's strength) — and the dual-burden is where today's compliance breach surfaced (Stage 2b processed in memory rather than write-on-discovery, because the AI was holding patch construction in mind alongside the analytical work).

---

## Scaling break-even

Conservative estimates:

- **(a) parser build:** 2-3 days CC engineering effort (one-time). Categories: 7. Each category is a defined extraction routine over a section the obslog already produces.
- **(b) instruction-gap closure:** ~1 day per category × 4 open gaps = 4 days. Plus per-session AI cost forever.
- **Per-session AI saving in (a):** estimate 30-50% of analytical-session token cost (patch construction is non-trivial in v2_9).
- **Programme size:** ~200 word analyses planned (Session B) + parallel work in Session C + Session D using same outputs.

**Break-even point: roughly 6-10 sessions.** After that, (a) saves recurring cost on every session. Over 200 words, (a) saves ~150-180 sessions' worth of patch-construction cost.

---

## Hidden upside of (a)

1. **Single audit artefact.** The obslog IS the record. Researcher reviews one document. Future researcher returning to a registry reads the obslog. No need to cross-reference patches.
2. **Easier methodology iteration.** Want to change how Session B works? Update the obslog template, update the parser. AI continues doing analytical work the same way. Compare to (b) where every methodology shift means re-instructing the patch shape.
3. **AI compliance is simpler.** AI's only obligation is "write the obslog correctly". Compare to "write the obslog correctly AND construct the patches correctly AND keep them in sync".
4. **Catalogue growth becomes natural.** GAP/WS questions and review notes in the obslog get parsed into catalogue inserts/updates without needing CATALOGUE_POPULATION patch shape closure.
5. **Narrative content (chapters) is solved.** No need for PROSE patches with section_type code lookups — parser writes directly to `prose_section` (or chapters table), in transaction, with the right linkages.

## Hidden risk of (a)

1. **Parser becomes the bottleneck.** If the parser doesn't recognise an obslog format variation, content is dropped silently. Mitigation: validators that count expected items vs found items (e.g. "obslog declared 147 Q&A entries; parser found 147 — pass").
2. **AI must adhere to obslog template.** If AI deviates (subtly wrong heading, missed section), parser breaks. Mitigation: run parser dry-mode at session close; AI reviews the structured-extract preview before sign-off.
3. **Up-front cost is real.** 2-3 days CC engineering before any new word benefits.

## Hidden upside of (b)

1. **No new code. No parser maintenance.** Every patch type is already defined or definable in the existing instruction.
2. **Applicator's existing validation is the gate.** Patches that don't conform fail at apply-time, loudly. No silent parser misses.
3. **AI is already doing this.** Today's session shows AI can construct patches correctly when the instruction supports it. The four open gaps are tractable.

## Hidden risk of (b)

1. **Per-session AI cost compounds.** 200 words × 7 patch categories × non-trivial JSON construction = recurring tax on every session.
2. **Compliance pressure on AI.** Today's compliance breach (Stage 2b processed in memory) is partly because patch construction creates batching pressure. Patch-as-AI-output reinforces this.
3. **Instruction sprawl.** Every new finding type, schema field, or operation requires an instruction update. v2_9 already has gaps; v3, v4… each session may surface more.
4. **Two-artefact review burden.** Researcher must read obslog AND verify patches reflect it. Twice the surface area.

---

## Recommendation

**Approach (a) — AI produces obslog only; CC parses and patches.**

Rationale:
1. **Per-session cost is materially lower** — AI focuses on analytical work, which is its strength.
2. **Single audit artefact** simplifies researcher review and future-researcher recall.
3. **Methodology iteration is cheaper** — change the template, change the parser; AI's job stays clean.
4. **The structural finding from this session's obslog** ("if the programme principle is 'nothing should exist that is not captured in the DB,' then the observations themselves need a DB home") is solved naturally — parser captures everything in the obslog, including observations, into appropriate DB rows.
5. **The four open instruction gaps stop being blocking** — closing them is replaced by parser extensions (which are simpler than patch-spec writing).
6. **Today's compliance breach is unlikely to recur** — without patch construction in scope, AI has less reason to batch.

**Break-even is fast** (~6-10 sessions) and the saving compounds over the remaining ~190 words.

---

## Hybrid worth considering (Approach c)

Not (a) vs (b) exclusively — a hybrid can work well:

- **Obslog as the universal record** (AI writes everything here)
- **AI continues to produce JSON for the well-defined, structured patch categories** (SD pointers, status updates) — these are cheap to construct and benefit from applicator validation
- **CC parses the unstructured / loosely-structured categories from the obslog** — chapters, observations, GAP/WS questions, review notes
- **CC owns the catalogue maintenance path** entirely (no AI patches for catalogue updates)

This keeps the existing structured-patch path (low-risk, working today) while delegating the harder-to-formalise categories to a parser. The break-even comes faster because parser scope is narrower.

**If the researcher wants to commit to a single direction, (a) is cleaner.** If practical migration is preferred, (c) lets the existing patch types continue working while the parser extends coverage to the categories currently blocked by instruction gaps.

---

## What to do next (decision-ready proposal)

If (a) is approved:
1. **Spec the obslog template** as a strict structural contract (already mostly there).
2. **Build the parser** — one extraction routine per category, with validators.
3. **Pilot on registry 067's existing obslog v2** — re-derive what would have been patched, compare against the three patches just applied. Validate completeness.
4. **Roll out** — next Session B session uses the new path.

If (c) is approved:
1. **Define which categories AI continues to patch** — likely SD pointers, status updates, dimension assignments.
2. **Build a parser for the rest** — chapters, observations, GAP/WS questions, review notes.
3. **Same pilot on reg 067**, comparing AI patches vs parser output for the AI-patched categories.

If (b) is approved:
1. **Close the four instruction gaps** — CAT-B-001, CAT-C-001, CAT-D-001, CAT-E-001.
2. **Update wa-patch-instruction to v2_10** with the missing patch shapes.
3. **Pilot on the next word's Session B** under the closed-gap instruction.

---

*Drafted 2026-04-27 by Claude Code under researcher direction. Not yet decided. The decision shapes how the remaining ~190 word analyses integrate with the database.*

Researcher comments.
I agree to (a), with the following additional observations

 - the migration of the methodology towards a state where the database captures all the source data, and all the analytic outcomes, and allow for reproducing any result from any stage has made good progress, and the changes made towards it, is encouraging.
 - the recent introduction of the obslog enables the capturing of AI thinking, and the test demonstrated it can work
 - the move towards providing AI with .md files as input, reduced the need for AI to figure out the database schema and try to analyse it.
 - CC doing the database updates reduce the number of round trips between CC and AI to reconcile and understand the database
 - the instructions for Analysis-output must include AI auditing itself and confirming that the obslog is complete and that all analytics have been recorded.
 - The database schema already provide for all (or most) of the handles to capture the analytic result.
 - The data readiness step can almost entirely be controlled by CC. CC must include validation steps to check its own work as the entire data preparation and validation is now in its hands.

The risks are

 - single point of failure - the database. if this gets corrupted, proves to be unworkable then the entire corpus will collaps.
 - data and result visibility is fragmented throughout multiple interrelated tables and fields.  This makes evaluation and review much more difficult.
 - CC miss the capturing of important analytic observations
 - CC miss the significance of data errors and do not pass it through to AI for analysis

