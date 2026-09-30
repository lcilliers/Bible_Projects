# Faculty field — state of the lexical across all verses (diagnosis)

- **File:** wa-faculty-state-diagnosis-v1-20260626.md · **2026-06-26 · Author:** Claude Code · read-only investigation.
- **Trigger:** researcher saw the faculty item in a report and judged it "simply looks wrong"; asked for a deep look at faculty across all verses before proceeding with the layered-strategy idea.
- **Verdict:** the concern is correct. Faculty as stored is a **dictionary lookup keyed on the lemma, not a reading of the verse.** Two distinct defects: (A) it never discriminates by verse, and (B) it is blank on half the corpus.

## 1. The headline facts (whole corpus, `ve_lexical` ve_nr=7)

- **29,205 faculty rows** across **19,857 units** (a unit = one term-in-verse = `verse_context_id`).
- **Faculty is 100 % a per-term constant.** Of **993 terms** that carry faculty, **993 have an identical faculty-set across every one of their verses; 0 terms vary by verse.** The field is computed once per lemma and stamped onto all its occurrences. It carries **no verse-level information at all.**
- **Coverage gap: 51.4 % of units have NO faculty.** 19,857 of 40,873 units carry one; **21,016 are blank.**
- **Provenance is mixed:** `faculty-map-v1-20260624` (26,386 rows) + `v2_engine_iter1` gap-fill (2,819 rows).

## 2. Defect A — over-firing on the seat terms (what you saw)

The "kardia → every faculty" problem is real and **concentrated in 8 lemmas — the constitutional seats** (heart / spirit). Because the set is per-lemma, the verse never narrows it:

| Strong's | term | gloss | occ | #facs | faculty-set (same on every verse) |
|---|---|---|---|---|---|
| G2588 | kardia | heart | 151 | **6** | affect, cognition, conscience, moral_evaluation, perception, volition |
| H3820A | lev | heart | 580 | 4 | cognition, conscience, perception, volition |
| G4151G | pneuma | spirit/breath | 341 | 4 | affect, cognition, perception, volition |
| H3824 | levav | heart | 237 | 4 | cognition, conscience, perception, volition |
| H3826/H3825/G4151H/H3821 | heart/spirit | — | 17 | 4 | (as above) |

That is **~1,326 units** where 4–6 faculties fire at once. The lemma genuinely *can* host all of these — but a given verse activates a **subset** (Mat 5:8 *kardia* is about moral purity, not memory or perception). The engine lists the lemma's **potential**, not the verse's **operation**. Distribution overall: 13,649 units fire 1 faculty, 4,696 fire 2, 186 fire 3, 1,175 fire 4, 151 fire 6.

## 3. Defect B — the blank half

51.4 % of units carry no faculty. Two causes mixed together:
- **Legitimate blanks** — many units are T2 qualifiers / objects / quality-adjectives that don't *address* a faculty at all (correct to be empty under the RESET "does the verse address a faculty?" test).
- **True misses** — terms the lemma-map simply doesn't cover. Per the 2026-06-24 audit (`project_faculty_not_gripped_audit_20260624`) the live signal was English-gloss-stem based at ~36 % coverage and missed whole categories (e.g. *trust* = 0). The current 10-value taxonomy (affect, volition, cognition, moral_evaluation, perception, conscience, relational_capacity, memory, creativity, agency) still has **no "trust"** and was never settled (7 vs 10–11 values).

We **cannot yet tell** how much of the 51 % is legitimate vs miss — that split is the first thing a fix must measure.

## 4. Why this matters for the layered strategy

If the base layer is built off the lexical, **faculty is one of its load-bearing signals** — and right now it cannot tell a "clear" verse from a noisy one, because it says the same thing on every occurrence of a word. For the seats specifically, a 6-faculty stamp is the *opposite* of the discrimination the base layer needs. This must be fixed (or explicitly demoted) before it can drive stratification.

## 5. Important nuance — it is NOT uniformly wrong

For **monovalent** terms (e.g. a fear-verb → affect, a know-verb → cognition) the per-lemma assignment is correct and verse-stable; nothing to fix there. The defect is specifically: **(a) the ~8 polyvalent seats over-fire, and (b) the coverage gap.** A fix should be **targeted**, not a wholesale rebuild — single-faculty terms can stand.

## 6. Fix options (for your decision — not yet actioned)

1. **Discriminate the seats by verse (targeted).** For the 8 seat lemmas only, narrow the faculty-set per occurrence using the verse's own signals already in `ve_lexical` — the governing predicate / `operation` / co-occurring faculty-verb / `sense`. Mechanical-partial: it will narrow many but not all (the ceiling still bites on figurative cases). ~1,326 units touched.
2. **Re-found coverage on a lemma-map (close the gap).** Replace the gloss-stem signal with a proper Strong's-lemma → faculty map, settle the taxonomy (decide on *trust* etc.), and measure the legitimate-blank vs true-miss split. This is the P2 item the 2026-06-24 audit already flagged as a blocker.
3. **Demote faculty to "potential" + add a verse-active sub-signal.** Keep the lemma-map as `faculty-potential` (honest about what it is), and add a separate, sparser `faculty-active` that only fires when the verse actually narrows it. Cleanest conceptually; most work.
4. **Do (1) now, schedule (2).** Fix the visible over-fire immediately (small, high-value), then re-found coverage as its own pass.

I'd lean **option 4**: the over-fire is what you saw and it's a small, contained fix; the coverage re-founding is a bigger, separate piece that shouldn't block it.

## 8. GOVERNING RULE (researcher, 2026-06-26) — supersedes §6

> **Faculty appears on a verse only if it is explicitly mentioned or inferred ON THE VERSE — never derived from the lemma.**

Consequence: **all 29,205 stored faculty rows are invalid by method** — every one came from the lemma-map (`faculty-map-v1` + `v2_engine_iter1`), the exact mechanism the rule forbids. This is not a tuning problem (§6 options 1/3/4 assumed the lemma-map stays); it is a **mechanism replacement**:

- **Faculty must be verse-grounded.** Two admissible sources, in order:
  1. **Explicit** — the verse text names a faculty or a seat in a faculty mode (a seat word: heart/mind/conscience/spirit/inward parts; or a faculty-verb: know, think, remember, devise, choose, desire, discern, perceive…). Mechanically detectable from the verse's own terms + predicate. **Note the faculty may come from a *different* term in the verse than the one being analysed** (e.g. "heart" gets cognition/volition from the governing verb "devises", not from *lev* the lemma).
  2. **Inferred** — the verse describes an operation that implies a faculty without naming it ("he chose" → volition). This is a reading, not a lookup — ceiling-bound.
- **The lemma-map is retired as a faculty source.** At most it can become a *candidate prompt* ("this verse contains a seat term — check whether the verse activates a faculty"), never the value itself.
- A verse with no explicit and no inferable faculty signal correctly has **no faculty** — empty is a valid, expected answer.

**Rebuild plan (proposed):**
1. **Scope (read-only, next step):** measure how many units have an *explicit* faculty signal in-text (mechanical, do-able now) vs how many would need *inference* vs how many are legitimately empty. Settle the faculty taxonomy in passing (incl. the *trust* gap).
2. **Rebuild explicit faculty mechanically** — derive from verse terms + predicate, provenance-tag `faculty-verse-explicit`.
3. **Inferred faculty** — either a mechanical best-effort pass (flagged lower-confidence) or deferred to the depth-on-demand layer; **researcher's call**.
4. **Soft-delete the lemma-derived rows** (reversible, provenance lets us select them exactly).

## 7. Provenance / repro

- All read-only; no DB writes. Queries against `ve_lexical` joined to `verse_context.mti_term_id`.
- Related memory: `project_faculty_not_gripped_audit_20260624`, `feedback_faculty_must_be_per_term_not_per_cluster`, `project_lexical_rules_reset_process_reframe`, `feedback_transitive_faculty_verb_is_qualifier`.
