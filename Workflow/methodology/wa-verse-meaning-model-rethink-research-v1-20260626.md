# Verse-meaning model — rethink (research before building the lexical out across all spans)

- **File:** wa-verse-meaning-model-rethink-research-v1-20260626.md · **2026-06-26 · Author:** Claude Code · research/proposal to steer, **not** an instruction yet.
- **Trigger (researcher, 2026-06-26):** we need a proper control method around **compounds**; the border between what is *meaningful for the workings of a verse* and what is not is unclear; we must relook at how we deal with verses, meaning, **operations morphing into each other**, and how to improve interpretation — **before** building the lexical out across every span.
- **Discipline:** this session's lesson applies — no imported story. Frameworks below are grounded in cited sources; recommendations are options, not decisions.

## 1. The problem, precisely (from our data + method)
- **Compounds today** (`ve_lexical` ve_nr 3, 82,002 rows, all engine, tier T6.1.1) pair the focal span with **any co-occurring tagged term**, typed coarsely as `partner` (58k) · `qualifier` (19.5k) · `co-seated` (4.3k). The control is **mere co-occurrence in the verse** — there is no test that the paired span actually *participates in the focal term's operation*. That is the uncontrolled border.
- **The RESET method already wants more** (`wa-lexical-analysis-rules-reset-v1` §3): the *relational-web/binding* line names richer relations (partner · object · cause · manner · expresses · seat · pole-opposite) and §3 has *transition/becomes* (= "operations morphing"). But the **compound field as built doesn't implement that** — it's flat co-occurrence, not typed participation.
- **The border question** = *which spans are meaningful for the verse's workings?* We proved (today) that the STEP meaning of **every** span is available (`lexicon`, 100% of real lemmas). So the question is not "do we have meanings" but "**which spans, and in what relation, constitute the inner-being movement of this verse** — and which are scenery."

## 2. Established frameworks that answer this (grounded)
| Framework | What it gives us | Fit to our problem |
|---|---|---|
| **Predicate–argument structure / valency / dependency** | a head predicate + its *bound* arguments (core) vs *adjuncts* (peripheral) vs unrelated words | **the compound control**: a span is a compound only if it fills an argument/adjunct slot of the focal operation, by morphology — not by co-occurrence |
| **Semantic Role Labeling / PropBank** | typed roles: ARG0 agent, ARG1 patient, ARGM-MNR manner, ARGM-CAU cause, ARGM-TMP time… | names our §3 edges in a standard, joinable vocabulary (operation/object/manner/cause = the same roles) |
| **Frame Semantics / FrameNet — incl. Hebrew FrameNet** | a predicate evokes a **frame**; frame elements are **core** (essential) vs **non-core** (peripheral) | **the meaningful border, principled**: core frame elements must be filled or UNRESOLVED; non-core are optional. Already demonstrated for Biblical Hebrew |
| **AMR (Abstract Meaning Representation)** | the sentence as a **rooted directed graph**: meaning-bearing concepts = nodes; relations = edges; **function words are not nodes** (they become edges or drop) | **the verse-as-web model**, and a clean answer to "what's a node vs scenery": particles/articles never become nodes; only concepts do |
| **RRG + Dowty decomposition / Aktionsart** | logical structure: `state` → `BECOME state` (inchoative) → `do/activity` → `CAUSE` (causative); Hebrew encodes these in the **stem** | **operations morphing into each other**: a transition is a typed edge between operation-nodes, derivable in part from `stem`/aspect we already store |
| **Force dynamics (Talmy) / event structure** | agonist/antagonist, letting/causing/resisting; sub-events | models inner-being *dynamics* (e.g. a desire overcoming restraint) as relations, not flat fields |

Sources: AMR — [Wikipedia](https://en.wikipedia.org/wiki/Abstract_Meaning_Representation), [Survey 2025](https://arxiv.org/pdf/2505.03229); Frame semantics + BH — [Radical Frame Semantics and Biblical Hebrew (Brill)](https://brill.com/display/title/15230), [review](https://rbecs.org/2013/06/25/rfsbh/), [verb_semantics (GitHub)](https://github.com/codykingham/verb_semantics); RRG/Aktionsart BH — [JSEM case study on *yd'*](https://unisapressjournals.co.za/index.php/JSEM/article/view/9275), [Verbs of Judgment in BH](https://academia.edu/72348922); Hebrew stem = causation — [unfoldingWord Hebrew Grammar: Stem](https://uhg.readthedocs.io/en/latest/stem.html).

## 3. The synthesis — a proposed direction
**Move from "focal term + flat fields + co-occurrence compounds" to a per-verse MEANING GRAPH:**
- **Nodes** = meaning-bearing spans (the inner-being operation(s) + their participants/concepts). Function-word spans (the 36 `H9xxx`, articles, conjunctions) are **never nodes** — they become edge labels or are absorbed. *This is the border, made mechanical (AMR principle): node-worthiness = carries lexical concept content, not grammatical glue.*
- **Edges** = typed relations = our §3 web, in SRL/frame vocabulary: `operation`, `object/target`, `cause/antecedent`, `manner`, `effect/produces`, `response`, `binding`, **`transition/becomes`**. **A compound is an edge, not a co-occurrence** — it exists only where a span fills a role of the focal operation (morphology-bound), which *is the control method asked for.*
- **The focal inner-being operation is the root**; its **core frame elements** (per the operation's frame) must be resolved or UNRESOLVED; non-core are recorded if present, silent otherwise (P4). Salience/border = distance from the root in the graph + core-vs-non-core.
- **Operations morphing** = `transition` edges between operation-nodes within (and across, via adjacency `read_with`) verses, **typed by the change kind** (set / removed / reversed / intensified / caused / became), seeded from `stem`/aspect and the result/sequence conjunctions.

**What this changes concretely:**
1. The `compound` field is replaced by **typed, controlled edges** (relation + the role it fills), discarding bare co-occurrence pairings that fill no role.
2. The "meaningful border" gets a **rule**: node iff concept-bearing; edge iff role-bound; everything else is scenery (recorded as present-in-verse but not part of the movement).
3. "Operations morphing" becomes a **first-class, joinable relation** (already required by `wa-synthesis-B-spec-reset-v1`: cause/effect/transition recorded as node+kind, not free text).

## 4. Options (to steer — not yet building)
1. **Adopt a graph model wholesale** (AMR/frame-inspired, RRG for verbal dynamics). Most principled; largest build; needs a frame inventory for inner-being operations.
2. **Keep the flat `ve_lexical` rows but add the control** — redefine `compound` as *role-bound edges only* (drop pure co-occurrence), add a `transition` typed relation, and a node/scenery flag per span. Incremental; gets 80% of the value; reuses the engine.
3. **Frame-element completeness only** — define, per inner-being operation, its core frame elements; the lexical's job becomes "fill the core elements or mark UNRESOLVED." Directly fixes the border without a full graph.
4. **Pilot first** — take 10–20 verses (incl. the hard ones: Pro 24:20, Psa 24:4, Heb 9:14), hand-build the meaning graph three ways, and see which control the verses actually support before committing. *(Recommended first step — verse-led, cheap, no build.)*

**Recommendation:** option 4 → then likely option 2 as the build path (it implements the control and the transition relation on the existing store, with the frame-core idea from option 3 as the border rule), holding option 1 as the horizon. But this is yours to weigh.

## 5. Honest limits
- A meaning graph is partly mechanical (roles from morphology/stem) and partly a read (frame assignment, transition kind, figurative cases) — the depth-on-demand gate (§5 of the reset) still carries the hard minority.
- Frame inventory for *inner-being* operations does not exist off the shelf — Hebrew FrameNet is general; we'd adapt, and let frames **emerge** (consistent with RESET §6) rather than impose a frame grid (which would repeat the object-type-grid error).
- None of this is built. This is the relook you asked for, before building the lexical out across all spans.
