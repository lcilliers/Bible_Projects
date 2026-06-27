# Discovery architecture — linear pipeline vs a toolkit feeding the layered build

- **File:** wa-discovery-architecture-linear-vs-toolkit-v1-20260627.md · **2026-06-27 · Author:** Claude Code · reflection + evidence (researcher is deciding).
- **Question (researcher, 2026-06-27):** should meaning discovery follow a **linear** approach, or is the term-signature tool **one of a range** of tools that feed the **layered** approach?

## 1. The evidence in front of us (this session)
- **Two orthogonal tools already surface different facets.** The **term-signature** (shared repertoire) is *blind* to co-operation; a **separate binding tool** (grace × mercy) surfaces it (6 co-occurrence verses; "Grace, mercy and peace" = adjacent/coordinate). Neither subsumes the other.
- **"Family" is not one thing — it is several lenses.** Grace by **registry** = charis/chen/charizō/charitoō/*tachanun*; by **cluster** = M39 (no *tachanun*; it's M21); by **root** / **related-words** = others again. There is no single canonical decomposition — there are multiple valid groupings.
- **The verse_span_lexical index** is a third, different lens (coverage/completeness). The **meaning graph**, **sense**, **transition**, **frame-completeness** are yet others.
- Each of these is **partial and verifiable** on its own, and **none is the whole**.

## 2. Why NOT a linear pipeline
- **The subject is a web.** A linear pipeline imposes a single sequence/order; the inner being has no single sequence (RESET §0 — the parts/boundaries won't hold). Forcing a line reproduces the very failure the RESET diagnosed.
- **The facets are orthogonal.** We *proved* that one pass (term-signature) cannot see what another (binding) sees. A single linear pass cannot capture orthogonal facets — you would have to choose one and lose the others.
- **There is no canonical decomposition** (the family lenses) — so "step 1: decompose the term" has no single right answer to be the first link of a chain.

## 3. The proposed shape — a TOOLKIT (DAG) feeding the LAYERED build
**Lean: the term-signature is one instrument in a kit; meaning is discovered by a *range* of lenses feeding the layered assembly — not a line.**

- **A kit of lenses**, each surfacing one verifiable facet:
  - coverage (verse_span_index) · term-signature (repertoire) · **binding** (inter-term operation) · sense (per-occurrence) · roles/graph (per-verse) · transition (morphing) · frame-completeness (core slots) · discovery-lookout (emergence).
- **They feed the LAYERED build** (the base-layer→directed-layers idea): the layering is the **assembly strategy** (start from the clearest, highest-confidence meaning; let the harder layers be drawn in by what the base reveals) — *not* a pipeline order.
- **Order exists where it is real — as a DAG, not a line.** Some lenses are foundational and feed others: span/coverage + sense + term-repertoire **→** roles/graph + binding **→** transition **→** synthesis. That gives genuine dependency ordering **without** forcing a false global sequence. It is a *directed-acyclic-graph of tools*, not a chain and not chaos.

```
            ┌── coverage (span index) ──┐
spans ──────┤── sense (per occurrence) ──┼──► roles / meaning GRAPH ──┐
            └── term-repertoire ─────────┘          │                  ├──► LAYERED synthesis
                          binding (inter-term) ──────┘   transition ────┘     (base → directed)
                          discovery-lookout  ── feeds new lenses back in (emergence)
```

## 4. Where the term-signature sits
It is **one lens** — the *shared* term layer. It **feeds** the graph (which role applies to this span) and **informs** binding (what each term brings to a pairing). It is **not the spine**, and must not be mistaken for the analysis (per `wa-term-morph-role-signature-method` §6c — the interweaving lives in the graph + cross-cluster synthesis, never the term lens).

## 5. Recommendation (yours to decide)
- **Adopt the toolkit-feeding-layered model, not a linear pipeline.** Build a small set of **orthogonal, individually-verifiable lenses**; wire their **real dependencies** as a DAG; let the **layered** strategy assemble meaning from the clearest outward.
- **Next concrete step to test it:** take ONE verse-set (e.g. a few grace+mercy verses) and run *several* lenses on it together — coverage, term-repertoire, binding, roles — and see whether the **assembled** picture is richer than any single lens and richer than a linear pass. If yes, the toolkit model is confirmed by doing.
- **Guardrail:** every lens stays a *building block* feeding the web; the moment any single lens (term, cluster, role) is treated as the analysis, the interweaving is filtered out.

## 6. Open data-quality note (surfaced by the prototype)
The registry "mercy" family still carries noise (terms surfacing as "again"/"longer" in the binding scan) — the **family sets themselves need a cleanliness pass** before the binding lens is trusted at scale. A lens is only as good as the grounded family it runs on.

Tools: `scripts/_explore_term_morph_roles_v1_20260627.py` (now registry/cluster-keyed) · `scripts/_explore_term_pair_binding_v1_20260627.py` (binding prototype).
