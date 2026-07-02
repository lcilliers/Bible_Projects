# Verse-analysis method — v1 (the live lexical process, 2026-07-02)

> The authoritative method for producing the verse-lexical under the **verse-first / passage / self-learning** model. Companion: `Workflow/Catalogue/wa-ve-lexical-catalogue-v1-20260702.md` (the item list). Supersedes the per-verse `01b`/tier framing for process. **The programme has fundamentally shifted to a self-learning, self-checking, passage-anchored, term-driven process** — this doc records it.

## 1. Governing principles (what changed)
- **Verse-first.** The verse is the unit; it yields a term-list + verse-level items. (memory `project_ve_lexical_is_verse_first`)
- **Passage = a consecutive run.** A passage is a maximal run of consecutive verses (sort by book, chapter, verse_num; length ≥ 2). Purely mechanical — no isolable/openers/semantic detection, **no reading to establish boundaries**. `verse.passage_id`; anchor = first verse (`is_passage_anchor`). The lexical is derived **on the passage as one unit**, anchored on the first verse.
- **Term-driven batching.** Work an OWNER term at a time: its **anchor verse's passage first**, then **every verse of the term, one by one**. This makes the **focus point emerge** (reading a term across all its verses).
- **Genre-aware.** `verse.genre` decides the passage treatment (§3).
- **Self-learning + self-checking.** Read back every result and evaluate it for **sensibility**; when uncertain, write a **D11 note** rather than assert. **Discovering and adjusting the rules is part of the process, not an afterthought.**
- **Completion-marked.** `verse.process_marker` records done verses; re-runs skip them.
- **The span is the unit within the verse** (span-completeness pre-pass, §5).

## 2. The processing pipeline (per passage)
1. **Select** an owner term → its verses → passages (anchor passage first). Skip any verse already marked complete.
2. **VALIDATOR A — passage membership.** Look up the consecutive run (`verse.passage_id`). (Trivial — no walking.)
3. **VALIDATOR B — spans present.** Every member verse must have `verse_morphology`. If any is missing → write `process_marker='B-BLOCKED:<refs>'` and **move on** (do not halt the batch).
4. **Anchor** = the first verse (the ve-records attach here).
5. **Read all passage morphology together** (one batch) — READ ONCE, USE MANY.
6. **Derive** each term's items across the passage span-set (per the catalogue rules), genre-gated (§3).
7. **Read back / sensibility check** — does each value make sense against the text? Uncertain or odd → **D11 note**. Wrong-in-general → **adjust the rule** and note the learning.
8. **Mark complete** (`process_marker`), and move to the next verse/passage.

## 3. Genre treatment (the key refinement)
- **prose** (law/narrative · narrative · prophetic · gospel-narrative · epistle) → passage = consecutive run; **cross-verse items ON** (source D2, effect D8, process D7). Validated on narrative (Exo 1, Gen 4, 1Sa 1).
- **poetic/wisdom** (Job · Psalms · Proverbs · Ecclesiastes · Song) → **TWO PHASES** (consecutive verses are independent, so cross-verse items would be noise):
  1. **Phase 1 — per-verse.** Use the **chapter/poem as the batch**; derive a per-verse lexical for **each** verse (per-verse items only; cross-verse OFF).
  2. **Phase 2 — poem read.** On completion, **read the whole poem** and **enrich** the verse-lexicals from the **interrelatedness** of its verses (discover cross-verse links deliberately, not by proximity).
- **Prophetic / Song of Solomon / Proverbs** may each need their own tuning — treat as open, flag with D11.
- **Option-3 (require a grammatical cross-verse link)** is itself a **method to test**, not to assume.

## 4. Self-learning loop (why accuracy jumped)
Different treatment of passage/verse in different scenarios sharply increases accuracy; **reading back and evaluating for sensibility makes a huge difference.** The loop: derive → read back → is it sensible? → (yes: keep) / (uncertain: D11 note) / (systematically wrong: **fix the rule, record the learning, re-run**). Example learning (perek trial): the `source` rule cannot yet tell a **driver** (dread→ruthlessness) from a **restraint** (fear-of-God restrains ruthlessness) — banked as a refinement.

## 5. Span-completeness pre-pass (the term-list, decided ahead)
Before analysis, for each verse: **verse → spans** (`verse_span_index`) → is each span a primary term? if not, should it be (a **missing primary** or a **qualifier**)? → confirm it is pulled into the DB → the confirmed set is the **term-list**. Mechanical narrows to a candidate list; judgement confirms per occurrence. (memory `project_ve_lexical_is_verse_first`)

## 6. Storage + markers
- Values → `ve_lexical` (+ pair columns `from_span/to_span/direction/resolution/pair_kind`). Verse-level → `verse.passage_id/is_passage_anchor/genre`.
- **Completion:** `verse.process_marker` (e.g. `lexical-v7-20260702`, `B-BLOCKED:…`, `A-REVIEW:…`). Re-runs skip completed verses.

## 7. Status (2026-07-02)
- **Solid:** per-verse items across genres; narrative cross-verse movement (source/manner/effect/process); passage layer (3,650 consecutive-run passages); term-driven order + markers.
- **Open (tracked in the catalogue §6 + validation reports):** source driver/restraint split; bearer (D3); target word-order; the poetic two-phase (to exercise on a Psalms/Proverbs term); item convergence + `ib_observation` retirement (pending finalised derivation).
- **Trials/harnesses:** `_probe_lexical_derivation_all14_v6_20260701.py` (14-item genre-aware) · `_apply_term_driven_lexical_ruthlessness_v7_20260702.py` (term-driven) · results in `verse-analysis/_reports/wa-lexical-*`, `wa-term-driven-ruthlessness-trial-20260702.md`.

---

## 8. The full term pipeline (researcher, 2026-07-02)
The end-to-end pipeline for one OWNER term. Per-verse lexical is the substrate; the **story** is a synthesis pass on top; both are grounded and traceable.

1. **Select the owner term → its ANCHOR verse.**
2. **Build the anchor ve-lexical** — process the anchor verse's passage (all D1–D14), read back, mark complete.
3. **Select all the term's related verses → build ve-lexical for each** (each verse via its passage; genre-aware; term-driven, one by one; completion-marked). *This completes the term's per-verse substrate.*
4. **SYNTHESIS (a task that runs only AFTER all the term's verses are complete):** collate the term's verse-lexicals and **synthesise across them** — the recurring operations, the movement, the source, the moral condition. **Inputs = the LEXICALS ONLY** (researcher, 2026-07-02): **no old fanout** (not pursued going forward) and **no old findings/`ib_observation`**. The aim is to see what story the lexicals alone yield. **Cohabitation is NOT part of the single-term synthesis** — it is not evident in the lexicals nor in the single-term rollup; it emerges only at the **cross-term** story layer (§9).
5. **Correction loop:** if the synthesis finds issues in individual verse-lexicals (a mis-derivation, an over-read, an inconsistency), **update/correct the individual lexicals** and re-collate. Synthesis and lexical are kept consistent.
6. **On synthesis completion → BUILD THE STORY:** narrate the operation in the researcher's voice per `wa-narrative-style-instruction-v1-20260702.md` — single-term order **act → impact → source/moral-condition** (NO cohabitation; that is cross-term, §9), **with citations**.
7. **Save the story in the PROSE TABLES** (`prose_section` term-synthesis type + `wa_prose_section_citations` linking verses/findings/ve_lexical). One story per term, versioned; regenerated if the lexicals change.

**Ordering rule:** the story is an OUTPUT of the synthesis; the synthesis is a POST-COMPLETION task (never run mid-term). The per-verse lexical never waits on the synthesis; the synthesis never runs before the verses are done.

### Build status of the pipeline (2026-07-02)
- Steps 1–3 (per-verse lexical, term-driven, marked): **built + validated** (ruthlessness: 6 OT verses written, `prov=lexical-model-2026`).
- Steps 4–7 (synthesis task → story → prose): **designed, not yet built** — the story voice + citations are set (style instruction + worked ruthlessness exemplar); the synthesis operation and the prose-save are the next build.

---

## 9. The CROSS-TERM story layer (where cohabitation lives) — researcher, 2026-07-02
Cohabitation — the company an operation keeps and the shared root that company reveals — is **not** derivable from a single term's lexicals, nor from that term's rollup across its own verses. It becomes evident **only when cross-term stories are built**: relating one operation's story to others (which operations recur together, in the same passages/contexts, toward a common root). So:
- **Single-term synthesis (§8.4)** → the story of one operation, from its lexicals only. **No cohabitation.**
- **Cross-term synthesis (later, separate layer)** → compares/relates the completed single-term stories → **cohabitation** and the emergent root appear here. This is the natural home of the (dropped-as-a-per-verse-item) D13.
- **Old fanout / old findings are not inputs** at either layer going forward (avoided where possible).

---

## 10. Evidence → narrative: a SCALABLE, REPEATABLE operation (researcher, 2026-07-02)
The synthesis (§8.4-6) is split into two parts so it **scales to any number of verses** (5 today, 15 later — same operation):
1. **COLLATE (mechanical, scales trivially):** `_produce_term_evidence_digest_v1_20260702.py --strong <S>` assembles the **evidence digest** — every new-model verse-lexical for the term + its passage co-terms, ordered by passage/verse, the term marked `<TERM>`. This is the **synthesis input**, not the narrative.
2. **SYNTHESISE (the reading/inference):** read the digest → the narrative, through the lens *"what does it say about the inner being"*, in the set voice (`wa-narrative-style-instruction-v1`), grounded + cited, tagging stated vs inferred.

**Regeneration rule:** the narrative is **always regenerated from the FULL current digest — never patched.** Adding verses = write their lexicals (§8.1-3) → re-collate (automatic) → re-synthesise the **whole** set. The narrative therefore always reflects **all** current evidence, consistently. The evidence layer is the term's verse-lexicals; the narrative is a lens over that evidence, re-derivable at will.

---

## 11. The GRAIN is the rollup unit (researcher, 2026-07-02) — supersedes "lemma"
A "term" for rollup is a **GRAIN** — a per-occurrence STEP sub-gloss — **not the bare lemma/Strong's**. The **grain index = `wa_verse_term_links`** (keyed to `wa_verse_records`; `step_subgloss_code` = the grain). Reader: `_produce_grain_index_v1_20260702.py`.
- **§8.1/8.3 restated:** "select the owner term → all its verses" = **select the owner GRAIN → all the grain's verses** (index lookup). Mono-grain lemmas (perek "severity", radah) are unchanged; polysemous lemmas (abad = serve/minister/labour/burden) roll up **per grain** — never aggregated across grains.
- **"Related verses" = same-grain occurrences** (not same-Strong's).
- **Cross-ref mappings carry the span (`strong@verse`)**, which resolves to a grain via the index — fix any bare-Strong's mapping (e.g. `coupling`) to `strong@verse`.
- **`mti_terms.owning_word` is NOT authoritative for sense** (e.g. "worship" mislabels the H5647G "to serve" grain); use the grain code.

---

## 12. The build is INDEX-DRIVEN — the two gates (fix, 2026-07-02)
The lexical build **starts from `verse_span_index` (every span)**, not from a pre-tagged term list. Two gates per content span:
- **Gate 1 — primary term:** the span is a tagged non-T2 term (has a `verse_context`) → lexicalise + link `verse_context_id`.
- **Gate 2 — relevant, not yet a term:** the span is a **content word not yet tagged** → lexicalise anyway, keyed on **`verse_span_id`** (`gate='2-relevant'`, relevance = candidate for confirmation). *Content words carry the IB impact; skipping them guts the lexical.*
- **Function words** (particle/preposition/conjunction/suffix/pronoun) are skipped.
- **T2** stays excluded from standalone analysis.

**Storage (schema 3.36.0, M62):** `ve_lexical` is now **span-keyable** — `verse_context_id` nullable + `verse_span_id`→`verse_span_index` + `gate`. Gate-1 rows carry both; gate-2 rows carry `verse_span_id` only.

**Proof (ruthlessness passages):** content-span coverage rose from **14% → 94%** (197/210 content spans; 52 function words skipped). The earlier build skipped ~86% of spans incl. `dread`, `deal-shrewdly` (deceit), `taskmasters` — all now lexicalised. Writer: `_apply_write_ruthlessness_index_driven_v3_20260702.py`; coverage check: `wa-span-index-coverage-5passages-20260702.md`.

---

## 13. SANITY CHECK + role-based rollup (researcher, 2026-07-02)
The index-driven initial build (§12) is a **fast mechanical DRAFT — not trusted**. The A/B/C classification noise proved it: derive-fast without evaluation produces mis-derived bearer/target, spurious source, and mis-classified roles. Two governing rules:

**13a. SANITY CHECK — mandatory post-build gate.** After the initial build, every span's derived values are **evaluated against the verse** for correctness/sensibility → corrected, or flagged in **D11**. Each span is assigned a **ROLE**. Only then is the lexical trusted / rolled up. ("Derive fast, THEN evaluate" — the read-back loop as a distinct gate, not an afterthought.)

**13b. Rollup scope is by ROLE, not every span.**
- **characteristic** (the focus disposition, e.g. ruthlessness) → full term-driven rollup (all its verses → story, §8).
- **qualifier / process-element** that binds to a characteristic → gives **value/context to the binding pair in place**; **does NOT get its own verse rollup**.
- **standalone** → no rollup.
- **exception (later circles):** a qualifier whose *usage varies across contexts* may earn its own verses — surfaced in subsequent **refinement circles**, not the initial build.

So "pull all the term's verses" (§8.3) is a **characteristic** operation. This settles abad/radah: `abad` (enslave) serves the ruthlessness pair as its bound action — no own-verse rollup needed *for ruthlessness*; only its own variation (a later circle) would earn one.

**Consequence for the build order:** initial index-driven build → **sanity check (evaluate + assign role)** → rollup **characteristics** only → story → (later) refinement circles for context-varying qualifiers. The role assignment is a candidate for a stored **role** lexical item (so it isn't re-derived).
