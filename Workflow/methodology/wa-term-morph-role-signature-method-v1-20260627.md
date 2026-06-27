# Method — Term morphological-role signature (shared-term → role repertoire)

- **File:** wa-term-morph-role-signature-method-v1-20260627.md · **2026-06-27 · Author:** Claude Code.
- **Origin (researcher, 2026-06-27):** from the span-vs-term insight — *the term is shared across verses; each span instantiates one morphology.* So: pull a term's spans, group by morphology, and **decode each to the grammatical role it signals.** Captured as a reusable building block to build further on.

## 1. The principle
- A **term** (lemma) is a **shared, reusable** concept — one dictionary entry, referenced by many verses (e.g. `chen` "favour" in 526 verses; `charis` "grace" in 142 spans).
- A **span** is the **unique** instantiation of that term in one verse — its morphology + its role/relations there.
- Therefore a term has a **repertoire of morphologies** across the corpus, and that repertoire **is its grammatical role/operation signature** — built **once** per term (shared layer), drawn from by each span (unique layer).

## 2. The role axis (what part of the morphology carries the role)
The full `morph_code` is too granular (person/number/suffix split verbs into dozens of codes). Collapse to the **role-relevant axis**:
| language · part | role axis | what it tells you |
|---|---|---|
| **Greek noun/adj/pron** | **CASE** | Nominative=agent/subject · Accusative=object/patient · Genitive=source/of · Dative=recipient/instrument/means · Vocative=address |
| **Greek verb** | **VOICE + MOOD** | active/middle/passive ; indicative / infinitive (purpose) / participle |
| **Hebrew noun/adj** | **STATE** | absolute (stands alone) vs construct ("X of…" = bound) |
| **Hebrew verb** | **STEM** | Qal=simple · Niphal=passive/reflexive · Piel=intensive · **Hiphil=CAUSATIVE** · Hophal=passive-causative · Hithpael=reflexive/iterative |

## 3. Worked examples (real data)
**`charis` (grace) — 142 spans → 4-case repertoire:** Nominative 50 (grace as **agent** — "grace abounded") · Accusative 41 (**object** — "receive grace") · Genitive 27 (**source** — "of grace") · Dative 24 (**means** — "by grace"). Grace behaves as agent, object, source, and means across Scripture.

**`chanan` (be gracious) — 77 spans → 4-stem repertoire:** Qal 54 (God **shows** favour) · **Hithpael 17 (humans IMPLORE favour** — the reflexive plea) · Piel 4 · Hophal 2 (be **shown** favour). The stem signature distinguishes *giving* grace from *seeking* grace — an operation distinction read straight off morphology.

## 4. How it feeds the build
- This is the **shared term-level layer**: the term's role/operation **repertoire**, computed once.
- In the per-verse meaning graph, a span doesn't invent its role — it **selects which repertoire entry applies here** (this occurrence of `charis` is Dative → it's the *means* edge in this verse). Reference the shared repertoire; instantiate the unique edge.
- For **verbs**, the stem axis is also the seed for **operations morphing** (Hiphil = caused change), tying back to the event-structure science.

## 5. The tool
`scripts/_explore_term_morph_roles_v1_20260627.py` (read-only, reusable):
```
python -X utf8 scripts/_explore_term_morph_roles_v1_20260627.py --strong G5485
python -X utf8 scripts/_explore_term_morph_roles_v1_20260627.py --strong H2580,H2603
python -X utf8 scripts/_explore_term_morph_roles_v1_20260627.py --word grace
```
Output → `outputs/markdown/validation/wa-term-morph-roles-<key>-<date>.md`: per term, the **role repertoire** (collapsed) + a foldable full morphology list, each decoded.

## 6b. CAVEATS — what this does NOT do (researcher critique, 2026-06-27)
Three honest limits the first write glossed over:

1. **"Family of the term" was determined WRONGLY (by English gloss).** The `--word` resolver matched the lexicon *gloss* ("grace"/"favour") — which is the **English-string error P2 forbids**, and it polluted the set: it pulled `qiqalon` "disgrace" (M07) and `hileōs` "propitious" (M38) into "grace." **The real, grounded family is the CLUSTER** (grace = **M39**: charis/chen/chanan/charizō/charitoō…), assigned from original-language analysis — plus the **registry word** (the 215 canonical words), **`wa_term_root_family`** (Hebrew/Greek roots), and **`wa_term_related_words`**. *Fix: key the tool on `cluster_code`/registry, never gloss.*

2. **Collapsing to the role axis DROPS interpretively-live content.** The stem/case summary is a **lens, not the term's full meaning.** Collapsing a verb to its stem discards **person/number** (WHO — God-3ms vs "I"-1cs vs "you"-2ms = the experiencer/agent identity), **suffixes** (the object/possessor — "be gracious to ME", "YOUR grace"), **tense/aspect** (when/how it unfolds), and the **attached particles** (which ARE the relation-edges). These are preserved in the full list (not deleted), but the collapse must **never be mistaken for the content** — it answers one question (what role), not all of them.

3. **It is SINGLE-TERM. It does not surface terms operating TOGETHER.** See §6c.

## 6c. The interweaving — where grace+mercy operating together is captured (NOT here)
The per-term signature is a **building block**, not the analysis. By itself it **cannot** see grace and mercy operating together — and they do: grace (**M39**) and mercy (**M05**) are **separate clusters**, yet **89 verses have both**, and "merciful and gracious" (rachum + channun, Exo 34:6 / Psa 103:8) is a recurrent paired inner-being movement.

**If the per-term / per-cluster lens were treated as THE analysis, it WOULD filter out the interweaving** — reproducing the parts-inventory failure the RESET diagnosed. The web is captured at two levels *above* the signature:
- **The per-verse meaning graph** — when two primary terms co-occur, they are **both nodes**, joined by a **binding edge** (coordinate pair / one as the manner-or-ground of the other). The graph is *built* for inter-term operation.
- **The cross-cluster synthesis** — RESET makes clusters **porous workspaces** (patterns assemble *across* clusters, never within one; `wa-synthesis-B-spec-reset-v1` §2a). A grace+mercy movement spanning M39 and M05 is assembled there, not lost in silos.

**So the architecture must be:** term-signature (shared building block) → per-verse graph (binds co-occurring terms) → cross-cluster synthesis (assembles the web). The signature **feeds** the web; it must never **replace** it.

## 6. To build further on (open threads)
- **Cross with sense:** add the per-occurrence STEP sense so the repertoire is morphology × sense (does the Dative-charis carry a different sense than Nominative-charis?).
- **Cross with co-term:** which role correlates with which binding partner (grace-as-means co-occurs with what?).
- **Greek verb axis** could be enriched (tense-aspect for event shape, not just voice/mood).
- **Build the shared "term repertoire" as a persistent table** so the graph builder reads it instead of recomputing — the natural next artifact after `verse_span_index`.
