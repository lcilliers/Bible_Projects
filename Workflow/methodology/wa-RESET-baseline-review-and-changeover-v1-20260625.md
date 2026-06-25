# THE RESET — development review, new baseline & change-over point · v1 · 2026-06-25

> **A milestone document.** It records how the study reached a fundamental reset of its rules and methods, captures the new baseline, triages the impact on the database, and registers the change-over from which all subsequent work follows. **Authoritative reference for the paradigm shift.**

---

## 1. The milestone, in one sentence

**The study's central aim — to *identify, name, and describe individual characteristics* of the inner being — is set aside, and replaced by *movements, associations, interlocking, and emergence*.** The inner being is no longer modelled as a set of named parts (characteristics / faculties / object-types) into which verses are sorted; it is modelled as a **process / relational web** read off **what each verse does**, from which patterns are allowed to **emerge**.

This is the second deep reset the programme has undergone (the first retired registry/dimension/VC-group clustering for term-anchors); it is larger, because it changes the *object* of study, not just its organising key.

---

## 2. How we got here — the development arc (the past weeks)

The reset was not a sudden idea; it was **forced by the work**, step by step:

1. **Progressive lexical development.** The L1/L2 verse-read, the 14 VE fields, the measure layer, the "meaning = the composed fields" model (01b). This built a sound, traceable **decomposition** layer.
2. **M10 (Sin) analysis — the first crack.** Trying to bring sin into *logical units* (32) kept failing; the observation pass found the cluster was **largely NOT characteristics** — it surfaced *object-kinds* (record, identity, condition, expression, mechanism, remedy, external-agency). The "characteristic" frame visibly did not fit the material.
3. **The object-kind expansion (M11/M12).** The lens grew to six object-types (characteristic · state · expression · qualifier · identity · bivalent-faculty). M12 produced the pivotal functional insight: **"giving is not a characteristic; it is the *expression* of one"** — what matters is the manner/relation that binds to the act.
4. **The cold-read VALIDATION — the decisive pointer.** Validating M10/M11 against the lexical found **~70–85% of the analytical claims imported meaning the verses don't carry.** The base sense-readings were sound; **the entire superstructure (object-kinds, units, pole-pairs, faculty-seatedness) was eisegesis.** The mechanical cause: **`faculty` and `type` are lemma-constants** — the grid was *relabelling fixed tags as per-verse discoveries.* "It made sense, it was satisfying — but it was not right."
5. **The M03–M09 diagnostic.** Most older clusters had kept the verse-lexical discipline; M07 (Shame) was the lone deviation. A review-backlog formed.
6. **The faculty saga.** "Did we get the grips with faculty?" — **No.** It was English-gloss-stem derived, 36% coverage, missed *trust*. Re-founded on a curated lemma→faculty map — then the researcher's deeper move: **faculty is intrinsic to a characteristic**, then **"does the verse address a faculty"** (observation, not ontology).
7. **The behavioural-science reckoning.** Asked cold, the field's answer: there is **no agreed anatomy of the inner being**; faculty psychology is discredited; the parts-intuition is borrowed from bodies and may not transfer. The diagnosis: **the repeated unit-failure was information** — a part-sorting method applied to a non-part subject. "Faculties" was the most part-committed frame of all.
8. **THE RESET.** Stop asking *"what part/category does this word name?"*; ask *"what does this word DO in the verse?"* Record the functional/relational edges; let patterns **emerge as attractors**; run a **discovery-lookout** on every verse; reframe faculty to the observable.
9. **Synthesis-B (the assembly half).** Designed hand-in-glove: the **unit of synthesis is the movement, not the term**; a four-level cascade (in-verse → similar-verses → cluster → cross-cluster); **clusters are porous workspaces, not meanings**; the established **B+D pointers** traverse the web *across time, on focus*; **measurement informs but never decides**; **a movement of one is a movement**; the **discard↔include balance is calibrated in situ**.

---

## 3. The pointers that changed the thinking

- **Boundaries won't hold** (units bleed) → *information about the subject*, not a method failure.
- **The grid relabels lemma-constants** (faculty/type 0% per-verse variation) → the superstructure was imposed, not derived.
- **Plausibility ≠ truth** ("it made sense but it's not right") → the AI reflex of *concept-first, harvest-to-fit*; the only guard is grounding in per-verse-varying evidence.
- **Understand the term in-cluster, don't export** (na.tan) → frequency ≠ noise; verify before dismissing.
- **Giving is the expression of a characteristic** → the functional turn (the act vs the manner/binding it carries).
- **The inner being may have no parts** (behavioural science) → retire the parts-frame; model the process/web.
- **Meaning lives on the edges, not the nodes** (the project's own oldest insight) → returns, now carried *up a level*: clusters are nodes; the picture lives on the edges between them.

---

## 4. Lessons learnt (durable)

1. **Observe, don't impose.** Let categories emerge from the material; never sort into a pre-decided grid.
2. **Ground every claim in per-verse-*varying* evidence.** A lemma-constant (faculty/type) describes the word, not the verse.
3. **Measurement informs, never decides.** Frequency tracks emphasis, not truth or membership.
4. **Cold-read against the lexical** is the QC that catches eisegesis; **traceability** (every finding walks down to its verses) is the structural fix for the recomposition failure.
5. **A failed structure is data.** When sorting keeps failing the same way, suspect the frame, not the effort.
6. **Bias toward surfacing/keeping while unknowns are immature** — a wrongly-kept candidate is visible and correctable; a wrongly-discarded one is lost.

---

## 5. The new baseline (the two specs)

- **Decomposition — `wa-lexical-analysis-rules-reset-v1` (v1.1).** Per verse, record **what the word does** (antecedent · operation · object · manner · effect · response · transition · relational-web · direction); faculty → **"does the verse address a faculty/seat"**; **discovery-lookout** mandatory; patterns are outputs, never inputs.
- **Assembly — `wa-synthesis-B-spec-reset-v1` (v2).** Unit = the **movement**; the **four-level cascade** (lexical record → Session B → Session B → Session D); **clusters porous**; **B+D pointers** carry related-verse ties, traversed on focus; **instruments reveal, never decide**; **singleton rule**; **discard↔include calibrated in situ** (D3 flagged in-evaluation).
- **Shared:** P0 (measurement informs, never decides); P2 (original-language grounded); P5/P7 (expectation-test + citation/traceability).

---

## 6. Impact on the database — STANDS / SET ASIDE / TUNE

*(First-pass triage — items are **soft-quarantined for provenance, never hard-deleted**; confirm per item before any DB action.)*

| Verdict | Items | Why |
|---|---|---|
| **STANDS (the observable substrate)** | `verse` · `verse_morphology` · `lexicon` (measure layer) · `wa_verse_records` · `wa_verse_term_links` · `verse_context` · `mti_terms` (grounded) · the corpus extracts · `books`/reference tables · the **bedrock** `ve_lexical` rows (**sense, mode**) | observed, original-language-grounded; the reset is *built on* these. The validation confirmed the **base lexical is sound.** |
| **TUNE (carry forward, refit to the functional model)** | `ve_lexical` → refit to the **functional/relational considerations** + make **cause/effect/transition joinable** (node+kind, not free text) · the **faculty** rows → re-derive as the **observable "verse addresses a faculty"** (the ontology set aside; `lemma_faculty_map` becomes a *seat/faculty-word list* for detection, not a term-essence) · the VE generator `_ve_engine_v2` → produce the functional edges + the discovery-lookout · `l2_meaning` narration → re-derive from the functional fields · the **SD_POINTER** mechanism → the B+D pointer view (already established) | the *fields are mostly right but mis-ranked/mis-framed*; tuning, not rebuilding. |
| **SET ASIDE (the imposed superstructure — quarantine, keep for provenance)** | `term_collection_lexical` (object_type/characteristic/state calls) · the **characteristic / characteristic_subgroup / cluster_subgroup** structures *as the analytical unit* · `cluster_finding` / `cluster_observation` and `finding` rows tagged by object-kind/unit · the **pole-pairs / §10 object-kinds / 32 M10 units / cluster-synthesis outputs** · the **tier catalogue as a grid** (`wa_obs_question_catalogue` is **reused only as the areas-to-cover checklist**, reframed onto movements) | these are the part-committed framing the validation found imposed; retained as provenance, not as live structure. |
| **BUILD NEW** | the **movement layer** (synthesis-B storage) · the **B/D pointer view** over L1 edges · the **lexical_note `discovery`** + the lookout/D3/discard-include registers in the DB | the assembly half + the emergence engine. |

**Net:** the **expensive, trusted substrate stands** (measure layer, base lexical, corpus); the **interpretive superstructure is set aside**; a focused set of fields is **tuned** to the functional model; the **assembly layer is new.** This is a reframe of the analytical layer, **not** a from-scratch rebuild.

---

## 7. The CHANGE-OVER POINT (registered)

> **CHANGE-OVER — 2026-06-25 — "Characteristics → Movements" reset.**
> From this point: all lexical analysis is governed by the two reset specs (§5); the characteristic/object-kind/faculty-ontology framing is **closed** (provenance-only). Every analytical artefact carries, implicitly, a *before/after this point* status: pre-change-over analyses are **legacy (to be revisited)**; post-change-over analyses are **baseline**.

Governance to update as follow-through (flagged, not yet done): `CLAUDE.md` §3/§10, the orientation map, the instruction `[current]` set, the schema docs — to point at the reset as the live method.

---

## 8. Follow-through — scope & sequence of rework

**Scope (researcher's expectation, recorded):**
- **All lexical analysis is reset** — re-run under the decomposition spec.
- **All M01–M11 "completed" analyses are revisited** — they were produced under the characteristic/object-kind framing.
- **All in-progress work is revisited** (M12 + the review-backlog M01/M02/M07/M10/M11 + the "sound" M03–M09 — *all* now in scope, because the framing itself changed).

**Sequence (proposed):**
1. **Tune the dissection** — refit `ve_lexical`/the VE generator to the functional considerations; make cause/effect/transition joinable; re-derive faculty as observable; wire the discovery-lookout. *(The §4 synthesis-B requirement is the gating change.)*
2. **Build synthesis-B core** — the L2 movement-clustering engine + movement store + the pointer view + the non-deciding instruments.
3. **Pilot on one cluster end-to-end** — dissection → movements → cross-cluster pointers — to see real movements + the singleton/validity/D3 behaviour on actual verses **before any sweep.**
4. **Sweep** the dissection across all clusters; then the assembly cascade.
5. **Revisit M01–M11 + in-progress** under the new baseline; legacy analytical outputs are superseded as their clusters are re-run.

**Preserved through all of it:** the measure layer, the base lexical, the corpus, the validation method, the lessons (§4), and the genuinely per-verse-grounded findings that survived the cold read.

---

*The reset — the study's object shifts from named characteristics to the movements, associations, and emergent patterns of the inner being. The substrate stands; the superstructure is set aside; the dissection is tuned and the assembly is new. Change-over registered 2026-06-25; all prior lexical/cluster analysis becomes legacy to be revisited. The work of the past weeks — the lexical build, the M10 battle, the validation, the faculty saga, the behavioural-science reckoning — was the path that earned this baseline.*
