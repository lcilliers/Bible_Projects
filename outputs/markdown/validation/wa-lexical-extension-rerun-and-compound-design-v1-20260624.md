# Extended lexical — re-run/re-assess implications + the compound refinement (design addendum)

- **File:** wa-lexical-extension-rerun-and-compound-design-v1-20260624.md · **v1 · 2026-06-24 · Author:** Claude Code.
- **Companion to** `wa-lexical-extension-deepdive-into-01b-DESIGN-v1`. Captures two things the researcher raised (2026-06-24): (a) the **implications of re-running / re-assessing / re-deep-diving** once the lexical carries the deep-dive understanding, and (b) the **compound refinement** (does a compound change type by situation?). The model **will be added to further** — so this is about keeping it regenerable as it grows.

## §1. The compound finding — measured, and what it means

Measured across M12/M13/M14: a co-term takes **>1 role in ~0–1%** of cases; **94% of all compound rows are "partner"** (3-value vocabulary: partner/co-seated/qualifier).

**This is an artefact of a coarse field, not evidence that compounds don't vary.** The role is defaulted to "partner"; the vocabulary cannot express the relationships the deep-dive surfaced (manner / expresses / object / cause / seat / pole-opposite). So:
- **LRT verdict on the compound element: NOT fully revealing** — the role field is under-developed (its own "expected-but-empty" gap).
- **Refinement:** compound/binding gets (i) a **richer role-type vocabulary** — `partner · qualifier · object · cause · manner · expresses · seat · pole-opposite · unmarked`; (ii) **per-verse determination** (the role is read per occurrence, like sense/object) — so it **will** vary by situation, which is exactly the researcher's hypothesis. 01b anticipated this ("compound may grow into its own VE / need a head↔partner pairing field").
- **Consequence for the model:** the `binding` element (design §5) is the **synthesis-relevant subset** of this richer compound (roles `manner`/`expresses`/`seat`/`pole-opposite`). Enriching compound is a **prerequisite** for the binding-web to be real — and it is itself a **re-deep-dive driver** (when compound is enriched, the affected verses re-run).

## §2. Re-run / re-assess / re-deep-dive — the implications

The per-verse layer (01b) is deterministic and regenerates cleanly (P6 whole-verse reset; automatic supersession). The **new collection layer** (object_type, mutability, binding, pole-relation, the type-conditioned answers) is derived from the per-verse layer **+ cross-verse rules + deep-dive understanding** — and *some* of that understanding is judgement. The governing risk is the one that killed the narrated meaning: **judgement that can't be reproduced drifts on re-run.** So:

**Principle R1 — split every collection value into MECHANICAL-derived vs JUDGEMENT-captured.**
- *Mechanical-derived* (regenerates identically): object_type (from the per-verse-varying rules), mutability (does any verse show the state set/removed), pole-relation (co-seating/cross-ownership), binding roles (the enriched compound). These re-derive from the per-verse rows + cross-verse rules → **reproducible, no preservation needed.**
- *Judgement-captured* (preserved across re-runs, like 01b §4e researcher notes): a read decision the rules can't force (e.g. a contested object_type, a recovered manner that needed reading an adjacent verse). Stored with `source=read|researcher` and **never overwritten by regeneration.**
- The aim: **maximise the mechanical share** so re-running reproduces almost everything; the captured judgement is small, explicit, and survives.

**Principle R2 — reset granularity has three scopes.**
- *Per-verse change* → reset that verse (01b P6) **and** re-derive the affected term's collection layer (a verse change can flip object_type/mutability/binding).
- *Term/collection change* → re-derive the term across all its verses.
- *Model change* ("we add to it further") → programme-wide re-derive of the mechanical layer; **migration-style**, not ad hoc.

**Principle R3 — version every derived value with the model-version that produced it.** When the model grows (new item/type), a re-assess (a) re-derives mechanical values under the new rules, (b) preserves still-valid judgement-captures, (c) **emits a diff** — what reclassified (e.g. a new 7th object-type pulls terms out of "bivalent-faculty"). Re-assessment is a *reviewable migration*, not a silent rewrite.

**Principle R4 — re-run IS a drift detector (a quality gate).** Re-running unchanged inputs under an unchanged model must be **idempotent**. If a mechanical value changes with no input/model change, that is a **judgement leak** (a rule isn't actually deterministic) → fix the rule. This turns regeneration into the test that keeps the lexical honest — the discipline the validation demanded.

**Principle R5 — re-deep-dive (the parked clusters) = re-run the pipeline at the current model version.** M07/M10/M11 (and M01/M02) re-enter by running the *same* cluster-agnostic tooling (generic reader → LRT → object-type rules → collection layer) at the live model version. No bespoke per-cluster method — that consistency is what makes the backlog tractable.

**Principle R6 — the LRT recovery must be a RULE where possible.** "Fill the blank" (e.g. recover the manner from an adjacent verse) should be a deterministic recovery rule (scan the passage / the bound term) so it regenerates; only where recovery genuinely needs a read is it judgement-captured (R1). Otherwise the fills drift.

## §3. What this means for building (and for the two-term test)

- The collection layer is a set of `ve_lexical` rows at **term scope**, each tagged `derivation = mechanical | read | researcher` (R1) and `model_version` (R3) — regenerable, diffable, drift-checkable.
- The **two-term test** (tamim characteristic + cleanness state) should, for each value, record **how it would regenerate** (mechanical rule vs captured read) and whether sourcing it needed an **adjacent verse** (R6) — so the test doubles as a check that the model is *reproducible*, not just expressive.
- Enriching **compound** (§1) is sequenced **before** a full binding-web build — but the two-term test can use the enriched role vocabulary by hand to prove it out.

## §G — bias-guard
- R4 (re-run = drift detector) is the structural guarantee against the exact failure we spent this session removing: it makes non-reproducibility *detectable* rather than invisible.
- The compound finding resists the reflex: the near-zero variation looked like a clean "compounds don't change type," but the LRT-on-compound shows it's a coarse-field artefact — *measure the field's adequacy before believing its distribution.*

*Addendum — compound needs a richer per-verse role-type (current 94%-"partner" is a coarse-field artefact, not a finding; enriching it lets compounds change type by situation as hypothesised). Re-run is kept safe by: mechanical-vs-captured split (R1), three reset scopes (R2), versioned re-assess-with-diff (R3), idempotence-as-drift-detector (R4), pipeline re-run for the parked clusters (R5), recovery-as-rule (R6).*
