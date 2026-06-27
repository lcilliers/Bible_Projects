# Baseline dataset status — span · working-of-span · lexicon · hybrid lens

- **File:** wa-baseline-dataset-status-v1-20260627.md · **2026-06-27 · Author:** Claude Code · read-only inventory.
- **Question:** what is in the DB for the span/lexicon/hybrid baseline, its status, and what can we start exploring with.

## 1. FOUNDATION — complete, clean, verse-king (THE baseline)
| table | rows | what it is | status |
|---|---:|---|---|
| `verse` | 23,593 | canonical verses + text | complete |
| `verse_morphology` | 305,961 | every word of every verse, tagged (surface, strongs, morph, pos, stem, language) | complete — STEP, **every word** |
| `verse_span_index` | 305,961 | the spine: **verse · span · term**, built this session | complete (1:1 with morphology) |
| `lexicon` | 11,666 | STEP meaning per term (gloss + medium_def) | **99% of span terms** (only 36 H9xxx grammatical markers uncovered — not lemmas) |

This is solid and grounded. No pull needed.

## 2. THE WORKING OF THE SPAN — 100% derivable from the foundation
The inputs the hybrid lens needs are **all present** in `verse_span_index`:
- `morph_code` on **100%** of spans · `pos` on **100%**.
- `stem` on **19%** — correct, not a gap: stems exist only for **Hebrew verbs** (~60k spans); Greek and Hebrew nouns/particles have none.
- From morphology we derive, mechanically: **case** (Greek role: Nom/Acc/Gen/Dat), **state** (Hebrew construct/absolute), **stem** (Hebrew verb operation/causation), **pos**. Plus the term meaning from `lexicon`.
- → **The role/operation reading of any span can be computed right now**, with nothing to fetch.

## 3. ANALYSIS LAYER — `ve_lexical` (partial, term-centric, legacy frame)
- **423,968 active rows across 40,511 units** (term-in-verse). That is the **study-term spans only** — ~9% of all spans (the fan-out finding).
- Active items: compound 82k · sense/type/lexical_note/discovery ~40k each · experiencer 27k · **faculty 20,636 (verse-grounded reset)** · object 20,577 · object-type 18,900 · how 16k · divine-involvement 10,327 (rule-b: mention) · cause_clause · from-source · relational · location · etc.
- **valence and origin are gone from active** (quarantined). faculty is the cleaned version.
- **Honest read:** this is the **old, term-centric** analysis (the debunked unit), cleaned this session but still partial and built on the list-of-things frame. **Use it as reference evidence, not as the baseline going forward.**

## 4. QUARANTINED / reversed this session (recoverable, NOT active)
valence 26,993 · origin 3,623 · faculty-pre-reset 29,203 · object-type-premap 9,534 · divine-roles-premap 5,187 · faculty-seat 1,492 · overlay 1,387 · divinv 860. All snapshotted; reversible.

## 5. NOT in the DB (not built — be clear)
- The **hybrid meaning graph** (per-span roles/edges/transitions, the operations) — **not persisted.** It exists as *method* (demonstrated on ~6 verses) + *logic* in exploratory scripts, but no dataset.
- A persistent **term repertoire** table and a **binding/co-occurrence** layer — not built (only exploratory scripts).

## 6. What we can explore with — right now, no pull needed
- **`verse_span_index` + `lexicon` + morphology** = the full operations substrate. For any verse or verse-set we can read off **what the verse describes happening** (the operation) — the verse-derived unit the focus-point reframe needs.
- **Tools that exist:** `verse_span_index` (queryable spine) · the JSON fan-out index (coverage) · `_explore_term_morph_roles` (term role repertoire) · `_explore_term_pair_binding` (inter-term operation) · `ve_lexical` (legacy evidence, with caveats).

## 7. Exploration entry points (options — researcher to choose, not to be rushed)
Aligned with the reframe (Scripture = data source; infer operations off verses; don't impose a list):
- **A. Operation-reading of a verse-set** — pick a handful of verses; from morphology+lexicon, read the operation each describes (what acts / changes / responds / binds), with nothing imposed. Tests "what is the loggable operation unit."
- **B. Map the operations substrate's shape** — across all spans, what *kinds* of operations the morphology already exposes (Greek voice/mood distribution, Hebrew stem distribution, role/case spread) — the raw material, before any naming.
- **C. Convergence probe** — take one candidate dynamic and see whether Scripture's described operation + a scientific aspect converge (the validity test from the reframe), on a tiny scale.
- **D. Stress the loggable unit** — on 3–5 contrasting verses, try to record *only the operation* (not the focus point), and see what's genuinely capturable vs what must stay inferred.

None of these builds a persistent layer yet — they're explorations to learn the unit before committing.
