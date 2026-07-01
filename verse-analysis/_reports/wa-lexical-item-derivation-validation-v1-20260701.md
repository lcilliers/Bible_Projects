# Lexical-item derivation validation — tested against real verse data

- **File:** wa-lexical-item-derivation-validation-v1-20260701.md · **2026-07-01 · Author:** Claude Code · **status: validation round 1 (of an expected several).**
- **Mandate (researcher, OQ5):** *test every lexical item against real data to confirm each value can be properly derived; show results; expect >2–3 tries.* This is round 1.
- **Method:** pulled the full measure layer (`verse_morphology` spans) + existing `ve_lexical` for 4 worked verses spanning different phenomena, and judged each item's derivation against the actual text.
- **Worked verses:** `Exo 1:13` (ruthlessness/enslavement — manner-noun + causative verb) · `Gen 6:5` (heart/evil/thoughts — 8 terms, heavy T2) · `Lev 25:43` (prohibition + fear-of-God) · `Psa 34:4` (fear delivered by God).

## Verdict summary
| item (dim) | derivable? | evidence from the 4 verses |
|---|---|---|
| **sense (D1)** | ✅ **reliable** | STEP subgloss correct every time (ruthlessly, fear, heart, sought…). |
| **type (D1)** | ✅ **reliable** | POS→type correct (verb→action, noun→status). |
| **discovery (D11)** | ✅ **reliable + valuable** | flags the untagged spans (Exo: they/people/Israel; Gen: earth; Psa: answered) — this **is** the span-completeness signal working. |
| **operation/how (D4)** | ⚠ **partial** | captures the governing verb, but **conflates the term's own operation with what is done TO it** — Psa 34:4 `how=delivered` for *fears* (God removes the fear; not the fear's operation). |
| **target/object (D5)** | ⚠ **partial** | right sometimes (`sought`→object=Lord, type=God ✓), wrong often (`every`→object=intention). `object-type` defaults to "impersonal". |
| **seat/location (D3)** | ❌ **over-applied** | Gen 6:5 assigns `location=heart` to **all 8 terms** (incl. "every", "saw", "man") — heart is in the verse so it's smeared across every term. |
| **source (D2)** | ❌ **unreliable** | `cause="pending-read"` (unresolved) or `cause_clause` = a **bag of verse words** ("wickedness man great earth every intention…"), identical on every term. `from-source` **wrong direction**: Lev 25:43 `from-source=God` (God is the *object* of fear, not a source); Psa 34:4 `from-source=fears` for *sought* (fears aren't the source of seeking). |
| **manner (D6)** | ❌ **not captured** | Exo 1:13 `be-perek` **is** the manner of the causative `abad` — the core weld — but it lands in `how`, not as a manner-pair. |
| **coupling (D9)** | ❌ **explodes** | see OQ3 below. |
| **divine-involvement** | ⚠ **crude** | mostly `present` (read_api) or `UNRESOLVED` — same weakness as valence. |
| **valence (D10)** | — dropped | (99% AI, all soft-deleted; but note the **prohibition** "You shall **not** rule ruthlessly" in Lev 25:43 is a *mechanical* signal worth keeping — see below). |

## What round 1 proves
1. **The bedrock items (sense, type, discovery) are solid.** The **relational/pair items the new schema depends on (source D2, seat D3, target D5, manner D6, coupling D9) are NOT cleanly derivable as built** — they carry systematic errors (wrong direction, over-application, bag-of-words, explosion). **The new pair schema cannot be trusted from the current `v2_engine` output; the derivation rules themselves need rework** — which is why >2–3 tries is realistic.
2. **Term grounding is itself noisy** (OT-DBR-009 again): mti `owning_word` is often the wrong sense — Gen 6:5 tags "every"→*evil*, "man"→*kindness*, "saw"→*experience*; Exo 1:13 tags `abad` "enslave" under **"worship" (M36)**. The *sense at the verse* is right, but the term label/cluster is a homonym artifact. Any item that reads the term's cluster/label inherits this noise.

## OQ3 — how does D9 Coupling work per-term? (tested)
**As built, badly.** In Gen 6:5 every term's `compound` lists all 6–7 co-terms with a role (`partner`/`qualifier`/`co-seated`), and the roles are unreliable (e.g. `ra.ah "to see" — qualifier` on the *heart* term). So per-term D9 currently = "restate every other term in the verse" — which **is** the multi-term principle, so it mostly duplicates it (your D13 argument applies here too).

**BUT there is a real kernel D9 must keep:** the **tight grammatical weld** — `be-perek` (Exo 1:13) governs the causative `abad` as its **manner** (construct/preposition binding); `ra.dah` ⟷ `ya.re` paired by the prohibition syntax (Lev 25:43). That is a *specific* morphological binding between two spans, not "they co-occur." **Recommendation:** D9 = only the **morphologically-welded pair** (the word that governs/binds the term by construct/preposition/suffix), derived from the parse — **not** every co-occurrence. Everything looser is the multi-term web, not a D9 pair. *This requires the argument-structure parse (which word governs which) — not yet reliably in the data.*

## Answers to the other OQs
- **OQ1 (2nd new `ve_nr`):** **Recommend only ONE new item — `process` (D7).** With D13 and D12 dropped, nothing else is new; every other dimension reuses an existing number + gains the pair columns. Adding a second, unused number now is speculative — allocate it if/when a new item actually emerges (D11's discovery-lookout is the mechanism for that). *Reason: minimise schema churn; don't reserve empty slots.*
- **OQ2 (tier):** Accepted — **drop the `related_tier` (T0–T7)** as non-value-adding at the lexical level. (I'll confirm nothing queries it before removing.) And per 7.3 of the design, verse-level elements (passage, discovery) live **outside** the per-term rows — passage in the `passage` table (built), discovery as a note — so **no verse-level tier is added to `ve_lexical`** either.
- **OQ4 (sequence):** Confirmed — **convert existing lexical → new schema first, then the verse-analysis rerun validates all verses.** Recorded as the build order.
- **OQ5 (test-first):** This doc is round 1. **It already fails several items** — so the next step is **rework the derivation rules per failing item** (source-direction, seat-attachment, manner, D9-weld), re-test on these + more verses, and iterate until each item derives correctly, *before* any batch trial. I have **not** internalised each item well enough yet — the data proves the rules aren't right, and honest iteration is the path.

## Proposed round-2 plan
1. Pick the failing items (D2 source, D3 seat, D5 target, D6 manner, D9 weld) and **redefine each derivation rule** against the argument-structure parse (governing verb, construct/suffix owner, preposition complement) — the morphology already carries this.
2. Re-test on the 4 verses **+ a wider sample** (say 20 across genres), showing before/after per item.
3. Only when each item derives correctly on the sample → the batch trial run (OQ4/OQ5 sequence).

**Keep the mechanical prohibition signal** (Lev 25:43 "not…" = `H3808`/`mē`) — it is evidence-based (unlike AI-valence) and carries the moral framing; fold it into the item set as a mechanical flag, not "valence".

---

## Round 2 — reworked rules against the argument-structure parse (harness: `scripts/_probe_lexical_derivation_harness_v1_20260701.py`)

Architecture per researcher direction: **read once** (one batch query each for spans/terms/lexicon), **parse morph once** into per-span features, **one function per item**, rules run in dependency order. Read-only harness — prints derivations, no DB writes.

### Fixed this round (before → after)
| item | round 1 (v2_engine) | round 2 (reworked) | rule |
|---|---|---|---|
| **manner (D6)** | not captured (fell into `how`) | **`be-perek` → "manner-of: work/rule"** ✓ (Exo 1:13, Lev 25:43) | a **preposition-marked noun** (be-/ke-) is adverbial manner on the governing verb |
| **coupling (D9)** | exploded — 7 co-terms w/ arbitrary roles | **only the weld**: perek "welds work as its manner"; loose co-occurrence → NONE ✓ | keep only the **morphological weld** (prep-manner / construct to a co-term); the rest is the multi-term web |
| **seat (D3)** | smeared `heart` onto all 8 terms | **heart only on intention/thoughts/heart** (construct-chained); man/saw/every → NONE ✓ | seat attaches only via **construct chain**, never verse-wide |
| **source (D2) direction** | false `from-source=God` / `=fears` | no false sources (fires only on a causal particle) — *but now over-fires, see below* | assign only on `ki`; else NONE |
| **target (D5)** | mixed/impersonal default | sought→Lord ✓, fear→God ✓, saw→wickedness ✓ | object = noun governed to the right of the verb |

### Still to fix (round 3)
1. **`source` over-fires on `ki`.** Gen 6:5 has one `ki` ("saw **that**…") so source fires identically on all 8 terms — the same bag-of-words problem in new clothes. `ki` here marks the **object of perception**, not a cause. → source must distinguish *causal* `ki` from *complementiser* `ki`, and attach to the right term (probably NONE here).
2. **`target` grabs the manner-noun.** `rule over`→target=`ruthlessly` (wrong — that's the manner; the real object is the suffix "him"). → skip preposition-marked nouns; prefer the `et`-marked / suffixed object.
3. **`operation` conflates active vs passive.** `fears`→operation=`delivered` — but *delivered* is done **to** the fear (God removes it), not the fear's own operation. → for a term, separate "the term's own verb" from "a verb acting on the term."
4. **Skip T2 as standalone.** The harness still derived T2 qualifiers (every/saw/man/only); they should inform other terms, not be analysed standalone.

### Read
The **read-once + per-item-rule architecture is right** and each rule is now revisable in isolation. Three items fixed in one round on the reworked rules; three precise defects remain, each with a known fix. This is the iterate-to-correct loop the researcher expected — round 3 targets source/target/operation + T2-skip, re-tested on these 4 + a wider sample.

---

## Round 3 — PASSAGE-AWARE (researcher correction: Exo 1:13 must be read as its passage)

Harness: `scripts/_probe_lexical_derivation_harness_v2_passage_20260701.py`. Loads the whole passage once, derives across the combined span-set anchored on the first verse (the stated processing algorithm).

**Demo passage: Exo 1:11-14** (the oppression pericope). *Note: the DB only flags 1:11-12 as a passage — the `isolable` marker MISSED 1:13-14, though perek + abad repeat and "and made their lives bitter" plainly continues 1:13. Marker under-detection = a real gap to fix before passages can drive analysis.*

### Ruthlessness (perek H6531) — isolated vs passage
| item | isolated 1:13 | passage 1:11-14 |
|---|---|---|
| source (D2) | NONE | **dread (H6973) @1:12** ✓ |
| effect (D8) | NONE | **bitter (marar Piel) @1:14** (rule picked the operation verb; fix: pick the produced-state) |
| process (D7) | not captured | **set→afflict→oppressed→dread→enslave→bitter→slaves** ✓ (the escalation) |
| manner | "work" only | **ruthlessly frames 1:13 + 1:14** (perek 2×) ✓ |
| target (D5) | NONE/wrong | **people of Israel** ✓ |

### What this proves
1. **Passage scope is mandatory, not optional.** `source`, `effect`, `process` **do not exist** at single-verse scope — isolated evaluation is systematically impoverished. Every analysis must run on the passage.
2. **The passage layer must be corrected first.** The auto-marker missed 1:13-14; a passage-driven analysis on the current layer would wrongly treat 1:13 as isolated. → improve passage detection (forward links, not just backward `isolable`) + manual adjustment, before the lexical build.
3. **Round-3 refinements:** `effect` must skip the operation verb and take the produced-state (marar); `process` should filter to IB-relevant operations (drop "built/multiplied/spread" = the Israelites' response, keep afflict/oppress/dread/enslave/embitter).

### Consequence for the build order
Add a step **0** before the item build: **fix the passage layer** (detector + manual review), because the lexical is prepared per-passage. Sequence becomes: fix passages → settle per-item rules (passage-aware) → convert old→new schema → rerun all.
