# Faculty audit — "did we really get the grips with faculty?" (honest answer)

- **File:** wa-faculty-audit-have-we-got-the-grips-v1-20260624.md · **2026-06-24 · Author:** Claude Code.
- **Question (researcher):** faculty has been a pain throughout; the collection-generator's faculty gap (trust untagged) reopened it. *Did we really get the grips with faculty?* — before any sweep.
- **Method:** empirical audit of the live faculty data + the actual derivation code. Not reassurance.

## Verdict: **No — partially. Faculty is the least-gripped lexical field, and it gates the collection layer. Do NOT sweep until it is re-founded.**

## The evidence

**1. Coverage is low and the gaps include genuine faculties.**
- Faculty present on **45% of term-in-verse units** (19,473 / 43,093) and **only 36% of clustered terms** (867 / 2,396); **1,529 terms have none.**
- Many no-faculty terms are *correct* (states/acts/things/persons: na.tan "give", a.von "iniquity", be.rit "covenant", o.yev "enemy" — rightly faculty-less). **But genuine faculty-bearers are missed:** **trust** — *both* `ba.tach` (117 occ) and `pisteuō` (212 occ) have **zero faculty**. Trust (faith/volition) is a core inner faculty and it is entirely absent.

**2. How the live data was actually derived (the root issue).** Live faculty = `v2_engine_iter1`, notes "R1 term-meaning" — i.e. **R1 only**, via `faculty_from_text(term's gloss)`: **English word-STEM matching against the term's own gloss (medium_def).**
- It is *half-right*: de-circularised to the term's **own meaning** (not the verse text) — which is why it's mostly per-term-stable and avoids the worst co-occurrence noise.
- But it is **still English-stem-based, not the canonical Strong's-lemma map.** 01b's own Q6 resolved "faculty lists are **Strong's-lemma sets**", and P2 (the error-eliminator) forbids English-string matching. **The live R1 derivation does not follow either.** "trust" isn't a stem in the list → trust gets nothing. The coverage gaps are the stem-list's incompleteness.
- A lemma-based map (`FACULTY_LEMMA`, Strong's→faculty) **exists in the engine but is the R2 (indirect/co-occurrence) path — and R2 was NOT applied** (the iteration ran "R1 only"). So the one P2-compliant piece is unused.

**3. My own earlier claim was over-general.** I had said "faculty is a pure lemma-constant (0% variation)" from M10/M11. Across **all** clustered terms it varies for **16% (135/867)** — sub-sense/homonym cases where the per-occurrence gloss differs. So faculty is *mostly* per-term but not strictly; the variation is gloss-driven, not a principled per-verse reading.

**4. The taxonomy is unsettled.** The live data has **7 faculties** (affect, cognition, perception, volition, moral_evaluation, conscience, memory). The T3 framework + the rederive script define **10–11** (adds **creativity, agency, relational_capacity, conscientiousness**). Creativity/agency/relational are **defined but absent from the data.** So we don't have one agreed faculty set.

**5. Three things are conflated under "faculty."** (a) the **term's own** intrinsic faculty (R1); (b) a **co-occurring** faculty term in the verse (R2 — which is *not* the term's faculty; it belongs to compound/binding); (c) the constitutional **seat/location** (item 5 — *where*, not *which faculty*). The design separates them but the gloss-stem R1 blurs (a), R2 is unapplied, and history repeatedly mixed faculty with seat.

## Why this blocks the sweep
The collection layer's **bivalent-faculty** and **characteristic** calls depend on faculty-presence. With faculty 36%-covered and missing genuine faculties (trust), the generator **cannot** distinguish a bivalent faculty (trust) from an expression, or confirm a characteristic — exactly the `bivalence_candidate` / `characteristic_candidate` deferrals we saw. **Sweeping now would bake the faculty gap into every cluster's collection layer.**

## What "getting the grips" requires (the path)
1. **Settle the taxonomy** (researcher decision): the canonical faculty set — reconcile the live 7 vs the framework's 10–11 (decide creativity / agency / relational-capacity / conscientiousness in or out, with definitions).
2. **Re-found R1 on a curated Strong's-lemma→faculty map** (01b Q6 + P2), replacing the English-gloss-stem matching. This is the lemma-list build — principled, complete (trust→affect+volition, hope→affect, etc.), original-language-grounded. Coverage rises and stops being arbitrary.
3. **Separate the axes:** faculty = the term's OWN faculty (R1, from the map); a co-occurring faculty (R2) is recorded as a **binding/compound** role (it is the *neighbour's* faculty), NOT the term's; seat/location stays item 5. Decide whether R2 is even needed as "faculty."
4. **Re-derive faculty** on the map (whole-verse reset, P6), validate coverage + spot-check, **then** re-run the collection generator (its faculty-dependent logic becomes sound).
5. Only then **sweep** the collection layer.

## §G — bias-guard
- This corrects my own over-claim (faculty as pure lemma-constant) — the audit is self-critical, not defensive.
- The finding is grounded in the live data counts + the actual derivation code (`_ve_engine_v2.py` `faculty_from_text`, `_apply_faculty_rederive_v1.py`), not impression.
- It is fair: the live method is *half-right* (de-circularised to the term's meaning) — the fix is to complete it (lemma-map, P2) and settle the taxonomy, not to start over.

*Faculty audit — NO, not gripped: live faculty is English-gloss-stem R1 (not the canonical Strong's-lemma map), 36% term coverage, misses genuine faculties (trust), taxonomy unsettled (7 vs 10–11), and faculty/co-faculty/seat are conflated. It gates the collection layer's bivalent/characteristic calls → re-found faculty (taxonomy + lemma-map, P2) BEFORE the sweep.*
