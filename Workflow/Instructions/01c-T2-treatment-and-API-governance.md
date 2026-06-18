# 01c — T2 treatment & API governance — CANONICAL (v1 · 2026-06-17)

> Companion to [01b](01b-VE-field-reliability-and-rules.md) (the VE generation rules). This document is **canonical and binding** on the scripts: it fixes (A) how T2 is treated in generation, JSON extraction, and API reads; and (B) the governance every API read pass must obey. Status: SETTLED 2026-06-17 (researcher direction). Linked memory: [[feedback_t2_reference_flag_reclassify]], [[project_t2_flag_are_seats_and_qualifiers]].

---

## A. T2 treatment

### A1. What T2 is
T2 = **reference / qualifier** terms — the "how", the constitutional seats, relational nodes and modifiers that combine with T1 inner-being terms. **Governing rule: T2 is NEVER analysed standalone** ([[feedback_t2_reference_flag_reclassify]]); it is engaged **only as context** to a T1 term.

### A2. The split (NEW — from the M01 review, 2026-06-17)
T2 as registered is **mixed**. Of 10,391 T2 units, ~2,000 are **grammatical function-words** wrongly carrying inner-being lexical records (`et` "[Obj.]", `I`, `to[wards]`, `also`, `behold`, `not`). These are noise. T2 is therefore sub-classified **by the term's own part-of-speech** (from the measure layer / `morph_util.morph_category`):

- **T2-content** — POS ∈ {**noun · verb · adjective**}. Genuine qualifier / seat / relational context. (~9,374 occ: `entrails: inner parts`, `hand: power`, `lip`, `name`, `to bow`, …)
- **T2-grammatical** — POS ∉ {noun, verb, adjective}, i.e. preposition · pronoun · particle · adverb · conjunction · interjection · conditional · suffix. **Function words, not inner-being content.** (~2,011 occ.)

The contribution a grammatical word *would* make is already captured on the T1 term itself by a dedicated VE: the preposition → VE13 relational; the pronoun → experiencer; the quantifier-adverb → VE N4 intensity. So excluding it as a standalone T2 loses nothing.

### A3. Treatment by context (BINDING on the scripts)

| Context | T2-content | T2-grammatical |
|---|---|---|
| **Generation** (`ve_lexical`, the engine) | generate the mechanical lexical so it is available as context; **never narrate** (no `l2_meaning` finding — already enforced) | **EXCLUDE — generate no `ve_lexical` rows** (it is a function word, not an inner-being term) |
| **JSON extract** (`build_ve_lexical_extract`) | include as a `focus_cluster:false` co-term so the compound web resolves in-payload | **EXCLUDE from the fan-out** (token waste + noise) |
| **API reads** | **EXCLUDE** (never analysed standalone) | **EXCLUDE** |

### A4. Implementation points (where each script enforces A3)
- `_apply_generate_ve_lexical_v2.py` — in the unit loop, **skip** a unit where `cluster='T2'` and the term's POS ∉ {noun,verb,adjective} (write nothing).
- `build_ve_lexical_extract.py` — in the fan-out, **drop** occurrences where `cluster='T2'` and `morph_category(morph) ∉ {noun,verb,adjective}`.
- `build_field_api_package.py` / `build_cause_api_package.py` — read packages **exclude all T2** (`m.cluster_code <> 'T2'`).
- Classification is by `morph_util.morph_category` (single source of truth) so the rule is consistent everywhere.

### A5. Existing data
The current `ve_lexical` already contains rows for ~1,768 T2-grammatical units (generated before this rule). They are **disposed on the next base rerun**: in live mode the generator **deletes** the excluded unit's existing `v2_engine_iter1`/`audit` rows and writes nothing back (it does not merely skip them, which would leave stale rows). A targeted standalone soft-delete is **not** needed; the rerun is the disposal path. (Snapshot first, per 01b §6.)

---

## B. API governance (binding on every read pass)

> Applies to Phase-2 reads only. **Engine alignment + compliance comes first; no API runs until the mechanical layer is to spec** (researcher direction 2026-06-17).

### B0. The governing principle — API is not an opt-out
**API is used to CLARIFY and ENRICH only where the mechanical process is not / cannot be decisive.** It is never an easy substitute for a deterministic rule. Before any field is sent to a read, its mechanical rule must be implemented to 01b spec; the read then receives **only the residue** — the units the rule legitimately leaves `UNRESOLVED` / ambiguous (the expectation test, P5). A field whose mechanical rule is a stub is **fixed in the engine, not papered over by the API.**

### B1. Batched & ordered
- Reads run **one field-type at a time**, in a fixed order; within a field, items are submitted in **deterministic order** (book/chapter/verse) in **fixed-size batches**.
- **Batch by verse, not by unit** — a verse's text/morphology is sent **once**, with all its in-scope terms asked together. (Eliminates the per-term re-read: 40,739 unit-submissions over 18,966 verses.)

### B2. Token-minimal package
- Include **only what the read needs**: the verse text once, the term(s) in question, the specific field prompt, and the minimal disambiguating context. **No** full lexical dump, no unrelated fields, no narration.
- Exclude T2 (A3) and any unit the mechanical rule already resolved.

### B3. Processing monitor + circuit-breaker (mandatory)
- The runner **measures and reports the wall-clock time of every batch/round**, with a running mean.
- Any round whose time is **out of range** (> a configured threshold, e.g. `N×` the running mean or an absolute ceiling) **triggers an immediate STOP of the API run** (mirrors the engine's per-verse circuit-breaker). The partial result is saved; the run is resumable.
- The monitor's per-round log is written to the run's audit file.

### B4. Self-verification — completeness & accuracy (per field, before "complete")
- **Completeness:** `submitted = applied + NONE + no-row` — reconcile exactly; **no silent drops**. Every in-scope unit is accounted for.
- **Provenance:** every applied value tagged `<field>_read_api` (survives rebuilds).
- **Accuracy (sampled):** N items read back against the verse (judgement); distribution sanity vs the pilot shape (no degenerate all-NONE / all-one-value).
- Result written to `wa-ve-corpus-rollout-audit-{field}-<date>.md`; **STOP and confirm before the next field**.

### B5. Resumability
- Reads are reversible (provenance-tagged UPDATE/INSERT). A stopped run resumes from the last saved batch; a re-run is idempotent (already-resolved units are out of scope by B0).

---

*Authority: researcher direction 2026-06-17. Binding on `_apply_generate_ve_lexical_v2.py`, `_ve_engine_v2.py`, `build_ve_lexical_extract.py`, `build_field_api_package.py`, `build_cause_api_package.py`, `_run_cause_api.py`, `_apply_field_from_api.py`.*
