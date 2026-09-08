# M/T-code cluster reallocation — scope and method (seed document)

- **filename:** 1598-cluster-reallocation-scope-and-method-v1-20260908.md
- **date:** 2026-09-08
- **escalation:** #1598
- **seeded from:** §4 of `1592-1595-window1-cross-pipeline-methodical-analysis-v1-20260908.md`
  ("T-code clusters — completeness, checked, not just sized")
- **researcher instruction, verbatim, this round:** *"M-codes and T-codes are a precursor for the
  lexical. we first need to determine if the categorisation of strongs are feasible as suggested in
  §4. lexical does not determine this categorisation, it just use it. [if] this is not reliable
  enough, then the entire lexical analysis colapses. a) create a new escalation for the reallocation
  of clusters, seed it with §4 and lets start working on it."*

## 0. Session checklist — status against the researcher's own 6-phase plan, refreshed

Rebuilt this round (researcher: *"how are we doing against our checklist"*) — §0/§0a's earlier
versions are now stale; this replaces them with live-verified state, not a running commentary.
Live cluster counts, checked this turn: `T2`=2,097, `T3`=2,502, `T4`=6, `T7`=10, `T8`=20, `T9`=5,
`T10`=19, `T11`=19, `T12`=22, `T13`=2, `T14`=11, all-M-codes total=3,072.

### Phase-by-phase (the original 6-step plan)

| Phase | Status | Detail |
|---|---|---|
| 1. M → T | **Done** (partial scope) | 388 M-tagged adjectives/adverbs reviewed (§5a); ~380 correct, 5 exceptions resolved. **Gap:** 2,352 M-tagged nouns/verbs never checked. |
| 2. T3 → T* | **Done** (growth); splitting question closed | Growth: 441 untagged + 401 from `T2` = 842 verbs processed (B1–B5), `T3` now 2,502. Splitting: **decided — `T3` stays one bucket**, verbs move to `M` only when directly characteristic-specific (your own rule, applied consistently since). T3's own purity audited (99% verbs after fixing an Aramaic-morph blind spot); 9 contaminants cleaned (Phase B4). |
| 3. T2 → T* | **In progress** | Targeted scans (Places/Corporate/Objects/Adversarial/Body-Parts) + the verb pool are done. `T2` down from 2,402 to 2,097. **Remaining, unscanned:** ~1,225 of the original ~1,265 common nouns (Phase C1–C3 only covered ~40), ~188 adjectives, ~41 proper nouns, ~93 adverbs, ~217 "other." |
| 4. Evaluate residual T2/T3 | **Not started** | Waiting on 3 being substantially complete. |
| 5. Re-evaluate every cluster code | **Not started** | Waiting on 1–4. |
| 6. M-code naming check | **Not started** | Waiting on enough reallocation to have happened. |

### New groups created this session (side effect of 2–3, not in the original 6 steps)

`T10` Places, `T11` Corporate/Collective, `T12` Objects/Artifacts, `T13` Natural World, `T14` Body
Parts (figurative/significant) — all live. `T4` Adversarial expanded from 3→6, not yet at T7/T8/T9
parity (scope confirmed: devil/evil spirits/Satan; more candidates not yet scanned).

### Resolved this session (no longer open)

Adjective-rooted characteristics (empirically yes, the norm); `characteristic`/`qualifier`
interchangeable, Layer 2 disambiguates (pattern agreed: `is_negator`→`polarity` template, mechanism
itself still undesigned — see Todo); Death+Sheol→`Places`, Sin stays `M`; `H6001A` (dual-tag
`M24`+`T8`), `G2960` (→`T7`, noted as widening the definition); `H3477H`/`H8549J` (parked `T3`,
then genuinely `T3` per B4's own morph check being ambiguous — not yet moved to Objects); neighbor/
youth→`T8`; inheritance→`M46`.

### Todo — added and standing, not yet started

- **New prefix for the T4/T7/T8/T9/…/T14 endpoint-type family** — postponed by your own instruction,
  still clashes with the cluster T-code letter.
- **Layer 2 disambiguation mechanism** — the concrete note_type/build, not just the agreed pattern.
- **Layer 2 Mechanisms Index (0.2)** — a living index naming every Layer 2 mechanism with its
  expected pattern, "not a single mechanism silently ignored" — still not built.
- **T4 (Adversarial) full scan** — 6 of an unknown real total; not yet exhaustive.
- **T2's remaining ~1,225 nouns, ~188 adjectives, ~41 proper nouns** — the bulk of Phase 3.
- **Body-parts group (T14) — not yet exhaustive**: heart, ear, mouth, arm, bone, flesh, neck, loins
  never scanned.
- ~~Sorting out the faculties (T3.1–T3.11)~~ — **RESOLVED, not a todo any more.** Full trace:
  `iba/docs/1598-phase-d-faculties-provenance-v1-20260908.md`. Researcher's verdict: faculties are
  real but not verse-derivable, foreign to the Bible's own vocabulary, and no individual faculty
  exists or acts on its own — at most an emergent pattern across many characteristics, never a
  per-verse primitive. No harm to characteristic analysis or final assembly if omitted. **Retired**
  — all 33 `T3.x` catalogue rows (`obs_id` 291–323) set `status='dropped'` live via
  `Catalogue-Update.ps1`, verified 33/33. No replacement decided; the parties/players/operations/
  movements/outcomes work already underway in this escalation is the named active priority instead.

## 0a. Control list — status against the researcher's own 6-phase movement plan

Requested this round: *"provide me with a control list against my initial movement plan on what has
already been covered, what is covered in this json, what is undecided and what just need further
processing."*

| Phase (researcher's own plan) | Status | Covered | Still open |
|---|---|---|---|
| 1. M → T | **Done — partial scope** | All 388 M-tagged adjectives/adverbs reviewed against real content (§5a); ~380 confirmed correct; 5 exceptions resolved (§5b) | **2,352 M-tagged nouns/verbs never checked** — only the adjective/adverb slice was reviewed |
| 2. T3 → T* | **Not started** | Nothing | Growth (441 missing verbs, §3) and the splitting question (does `T3` fracture, or stay one bucket) both open |
| 3. T2 → T* | **Partially done** | 8 targeted relocations found via the Places/Corporate/Objects/Adversarial scans, in the JSON payload | Keyword-targeted only — most of `T2`'s 2,402 members never individually reviewed |
| 4. Evaluate residual T2/T3 | **Not started** | — | Blocked on 2 and 3 being substantially complete |
| 5. Re-evaluate every cluster code | **Not started** | — | Waiting on 1–4 |
| 6. M-code naming check | **Not started** | — | Waiting on enough reallocation to have happened |

**New groups created as a side effect** (not in the 6-phase list, but load-bearing for it): `T10`
Places (13 members), `T11` Corporate/Collective (16), `T12` Objects/Artifacts (7), `T4` Adversarial
(+3) — all in the JSON payload, pending the researcher's run.

**§0's open items, resolved vs. still open, as of this round:** adjective-rooted-characteristics
(resolved), new prefix (postponed), Death/Sheol/Sin boundary (resolved), `H6001A`/`G2960` (resolved,
in JSON), `H3477H`/`H8549J` (temporarily parked, in JSON), escalation #1599 (awaiting approval).
**§0.2's Layer 2 Mechanisms Index — not yet built, a real gap, not silently dropped:** the researcher
asked for a living index naming every Layer 2 mechanism with its expected pattern; this got absorbed
into the cluster-reallocation work instead of being started. Flagged here for the researcher's own
sequencing call, not deferred silently.

---

## 1. Why this is its own escalation, upstream of #1592–#1596

`lexical.build`/`lexical.enrich` **consume** `cluster_strong`'s M/T-code membership (`is_negator`,
`party_kind`, and every proposed new column in the main report's §5) — they never determine it. If
the categorisation itself is incomplete or wrong, every downstream Layer 1/Layer 2 column built on
top of it inherits that unreliability silently. §4 of the main report already found concrete evidence
this is a real risk, not a hypothetical one — restated here as this escalation's starting evidence,
plus new sizing work done this round to make the scope concrete rather than illustrative.

## 2. §4's findings, carried over verbatim (evidence already on record)

1. **`T3` (Operations) is not exhaustive** — genuine untagged action verbs found (`H5927G` "to
   ascend," `G2064` "to come/go") sitting alongside proper nouns and misclassified pronouns in the
   untagged bucket.
2. **M-code and `T3` are not fully disjoint** — 10 strongs carry both an M-code and `T3`.
3. **Faculty-domain signals (T3.1–T3.11 in the catalogue) have no lexicon at all.**
4. **"Objects/beings that act like beings" (personification) is not a lexicon gap** — the nouns
   themselves are typically already M-tagged (`wisdom`→`M16`) — it is a per-verse, contextual
   detection problem (whether a tagged/untagged noun is used as an active verb's grammatical
   subject in a specific verse), structurally closer to the `verb_argument` note_type (Layer 2, only
   1 live example ever) than to a new T-code lexicon.

## 3. New this round — the real scope, sized, not sampled

**8,268 distinct strongs** carry live `role='content'` occurrences and **no cluster tag of any
kind** (M, T, or FLAG). Broken down by part of speech (derived from each strong's own most common
live `morph_code`):

| Category | Count | Share | What this means for reallocation |
|---|---|---|---|
| Hebrew proper nouns | 2,618 | 31.7% | Correctly excludable — no cluster work needed |
| Nouns (Hebrew 2,397 + Greek 1,646) | 4,043 | 48.9% | **The main body of candidate work** — characteristic (M-code), a new group, or correctly non-analytic |
| Adjectives (Greek 451 + Hebrew 178) | 629 | 7.6% | Plausible **`qualifier`** candidates (matches the researcher's own morph_code-based definition from the prior round) |
| Verbs (Greek 271 + Hebrew 170) | 441 | 5.3% | Confirms `T3` undercounts by at least this many — direct evidence for finding #1 above |
| Adverbs (Greek 130 + Hebrew 28) | 158 | 1.9% | Also plausible `qualifier` candidates |
| Pronoun/preposition/conjunction/relative/demonstrative (all languages) | ~38 | 0.5% | **Not a cluster-reallocation problem at all** — this is the `role`-classification bug (#1590) wearing a different hat; fixing `classify_role`'s tag lists resolves these, not a cluster assignment |
| Unclassified by this pass's simple morph-prefix heuristic | 322 | 3.9% | Needs a closer, manual morph-code read — not force-classified here |

**A clarifying finding, not previously stated:** the *row-level* impact of the pronoun/preposition
role-bug is huge (`G0846` alone: 5,482 occurrences) but the *lemma-level* fix is tiny (~38 distinct
codes) — these two scales should not be confused when deciding what "the reallocation problem" is
made of. The cluster-reallocation work proper is the **~5,271 nouns/adjectives/verbs/adverbs**
(4,043 + 629 + 441 + 158), not the pronoun population.

## 3a. What will be left in the M-codes — checked against real data, not assumed

**Researcher's question, verbatim, this round:** *"I assume in the work above, the backfill strongs
will be scattered through the different types. On the basis that M-codes are the home for
characteristic type strongs, if you do all the re-allocations, what will be left in the M-codes."*

**The backfill assumption, confirmed:** of the 8,268 untagged candidates, **7,860 (95.1%) are
backfill-origin** — the reallocation pool is overwhelmingly words that entered the corpus through
the automated completeness sweep, not through deliberate registry-word study. This is expected and
coherent: the registry's own ~214 words and their term families were curated into M-codes through
the word-study pipeline; backfill exists specifically to fill in everything else the surrounding
text needs for full verse coverage.

**But the question cuts the other way too, and this is the more consequential finding: the CURRENT
M-code population is not as pure as "characteristic = M-tagged" implies.** Checked live, part of
speech breakdown of all 3,034 currently M-tagged strongs:

| Part of speech | Count | Share |
|---|---|---|
| Noun (Hebrew 781 + Greek 451) | 1,232 | 40.6% |
| Verb (Hebrew 568 + Greek 552) | 1,120 | 36.9% |
| **Adjective (Greek 222 + Hebrew 156)** | **378** | **12.5%** |
| Other/unclassified by this pass | 148 | 4.9% |
| No Layer 1 build yet | 140 | 4.6% |
| Adverb (Greek 9 + Hebrew 1) | 10 | 0.3% |
| Proper noun | 5 | 0.2% |
| Conjunction | 1 | ~0% |

Nouns and verbs together are 77.5% of the current M-code population — a good fit for
"characteristic." **But 388 currently M-tagged strongs (12.8%) are adjectives or adverbs** — exactly
the part-of-speech the researcher's own prior-round definition names as the `qualifier` signal, not
`characteristic`. Under a strict, consistent application of that definition, these 388 would need to
move OUT of M-codes into `qualifier`, not stay as characteristics — **M-codes would shrink before
the reallocation pool's own candidates are even considered for addition.**

**This is not a clean call, and is not made here.** Some characteristics are naturally adjective-
rooted concepts in their own right — M08 (Pride & Arrogance), M09 (Humility & Lowliness), and M53
(Dishonor & Disgrace) are plausible examples where the adjective form ("proud," "humble," "ashamed")
may genuinely BE the characteristic, not a qualifier of some other word. A pure part-of-speech rule
(adjective ⇒ always qualifier) would misclassify exactly these. The same ambiguity already showed up
on the verb side: **10 strongs are currently tagged both an M-code and `T3` (Operations)** — the
same word can apparently be both a characteristic and a generic "operation," so mutual exclusivity
between `characteristic` and `qualifier`/`T3` cannot simply be assumed either.

**Honest answer to "what will be left":** it cannot be predicted as a single number without doing
the actual verse-context work (§4's standing constraint applies to *removing* candidates from
M-codes exactly as much as it does to adding new ones — a bulk "all adjectives out" sweep would be
the same kind of error as a bulk "all backfill nouns in" sweep). What can be stated now: (a) the
net direction is **not purely additive** — this reallocation may shrink M-codes' adjective/adverb
membership as much as it grows their noun/verb membership from the untagged pool; (b) the open
design question — **can a characteristic be adjective-rooted, or is `characteristic` reserved for
noun/verb forms with adjectives always routed to `qualifier`** — needs your decision before either
direction of movement (out of M, into M) can be executed at all, since it is the rule that would
decide both.

## 3b. Researcher's response — content-based T-codes, dual membership expected, and a Layer 2 test needed

**Researcher, verbatim, this round:** *"that is expected. I expected that many strongs will move
from M-code to some of the specialist T-codes. The specialist T-Code is not by POS that is by
content, much like M-Codes. Yes, characteristic and qualifyer is definitely interchangeable.
Reallocation alone will not get this 100% right. Therefore, analytics must be guided to test the
role of the strong, especially for swapping between char and qualifyer. The same goes for
action/verb."*

Four points, each with a direct consequence for how this project proceeds:

1. **The specialist T-codes classify by content/meaning, the same way M-codes do — not by part of
   speech.** Correction to how §3/§3a's own POS breakdown should be read: **part of speech was a
   triage signal for finding untagged candidates, never the classification rule itself.** A
   `qualifier`-type T-code group (or, more likely, several — the same way `party` is really T7/T8/T9,
   not one flat group) needs its own content-defined boundary (e.g. "degree/intensity terms,"
   "manner-of-action terms" — actual proposed groupings not decided here), the same way each M-code
   is a semantic domain (Fear, Anger, Grief…), not a grammatical category.
2. **Dual membership is expected, not an anomaly to eliminate.** The 10 strongs already tagged both
   an M-code and `T3` are not a defect to resolve one way or the other — they are the expected shape
   of a genuinely dual-natured word. This reframes §3a's own "mutual exclusivity cannot be assumed"
   observation from an open worry into a confirmed design fact.
3. **Characteristic and qualifier are explicitly confirmed interchangeable** — the same lexeme can be
   either, depending on the verse. §3a's adjective-rooted-characteristic question (M08/M09/M53) is
   therefore not really "is this word A or B" — it's "this word can be both; which one is it doing
   *here*."
4. **Reallocation (the lexicon-level M/T-code work in §5) cannot make this determination alone, and
   was never going to.** A per-occurrence, per-verse test is needed on top of it — for the
   characteristic/qualifier swap, *and*, named explicitly by the researcher, for the same swap
   between a characteristic-action and a generic operation (the verb-side version of the exact same
   problem `T3`'s own M-overlap already demonstrates).

**What this implies for the pipeline, not decided or built here:** this is structurally the same
shape the schema already has a working precedent for — `is_negator` (Layer 1, mechanical) feeding
`polarity` (Layer 2, judgement, confirms/refines in context) is the existing pattern. The same shape
would apply here: Layer 1/the reallocation work supplies the **candidate** membership (a strong CAN
be a characteristic, CAN be a qualifier of some content-type, possibly both) from content-based
cluster tags; a **Layer 2 judgement call**, made per verse, would then decide which one the word is
actually doing in that occurrence. This is a real, needed addition to the note_type design (§1595's
own subject) — cross-referenced there, not designed in full here, since it's a decision that touches
the main report's own `role` redesign (§6) as much as it touches this escalation's reallocation work.

## 3c. The T4/T7/T8/T9 family reframed — movement-endpoint classification, not just "who is named"

**Researcher, verbatim, this round:** *"the role progression through layer 1 and layer 2 is a good
suggestion. Maybe the role indicator in layer 1 is the cluster allocation (after fixing clusters) and
layer 2 is the applied role when API had a chance to digest the verse. T7/T8/T9. T4 is definitely
not only 3 strongs and need to be on the same level as the other. I am debating in my head if there
is another group. Let me explain: these T groups (we need to get another prefix for it, the prefix
clashes with cluster T-codes) main purpose in relation to chars is to isolate and understand
purpose/trigger/target/impact and other movements. The T-groups divide the different types of the
end points of the movements — because it really impacts on the nature of the char. T4 is suppose to
be the devil, evil spirits, satan, the evil one etc. The group that is missing is the natural world
storm, cloud, water, fire, plants, animals, etc. Do you think there is another missing group."*

**§6.4's `role` progression confirmed, with a concrete Layer 1/Layer 2 split named:** Layer 1 = the
cluster-allocation-derived candidate (once §3a/§3b's reallocation is done); Layer 2 = the role the
LLM actually applies once it has read the verse. Matches the `is_negator`→`polarity` precedent
already proposed, now with the researcher's own framing of *why* each layer does what it does.

**T4 correction:** not a 3-strong stub — needs full, exhaustive treatment at the same level as
T7/T8/T9. Scope, as the researcher states it: the devil, evil spirits, Satan, the evil one — i.e.
personal adversarial spiritual beings, the same grain as T7's divine names/T9's angelic beings, not
a catch-all for every negative force (see the Death/Sin boundary question below).

**The real conceptual correction — this family's purpose:** T4/T7/T8/T9 are not simply "which party
does this name" lookups in isolation. Their purpose is to classify the **endpoints of a
characteristic's movement** — who or what triggers it, who or what it targets or impacts — because
the *type* of endpoint changes the nature of the characteristic itself (fear *of God* is not the same
phenomenon as fear *of a man* or fear *of the adversary*). This is not a new mechanism to build from
scratch — it is exactly what the already-designed `verb_argument` note_type (`target_verse_lexical_id`
= trigger/subject, `related_verse_lexical_ids` = impact/object) exists to capture; this
endpoint-type family is what gives that note_type's trigger/impact resolution real analytical
content once it resolves to a classified party, rather than just an unclassified noun.

**Naming collision, independently identified by the researcher — matches CA-4 already on record**
(the main report's own finding of three unrelated live "T"-numbering schemes). This family needs its
own prefix, distinct from the T2/T3/T5/T6 cluster codes it currently shares a letter with. Not
decided here — offered as options only: something built around "endpoint" or "party" (e.g. `E-`
codes), avoiding letters already loaded elsewhere in this project (`P` already means "personal
pronoun" in the live Greek morph-code convention, found earlier this session — reusing it here would
recreate the exact collision this correction is meant to fix).

**Is there another missing group? — offered as analysis, not a decision:**

- **Corporate/collective human entities (nations, peoples, cities) — the strongest candidate,
  distinct from individual `human` (T8).** Scripture routinely treats these as acting units in their
  own right, not just aggregates of individuals — personified cities ("daughter of Zion"), a nation
  addressed as "she" in covenant/marriage language, a people that collectively "sins," "repents," or
  "fears." A characteristic triggered by or directed at "Israel" or "the nations" is analytically
  different from one involving a single named person, and `T8`'s own live sample (`man`, `adam`)
  reads as individual-human-shaped, not corporate-shaped.
- **Man-made objects/artifacts (idols, wealth, weapons) — weaker, more speculative candidate.**
  Distinct from the researcher's own "natural world" group (storm/cloud/water/fire/plants/animals,
  which are not human-made) — idolatry and trust-in-riches are recurring, theologically loaded
  targets for exactly the characteristics this study tracks (fear, trust, love, pride), so a
  characteristic's endpoint being "an idol" vs "a natural phenomenon" vs "a person" may be worth
  distinguishing. Lower confidence than the corporate-entity candidate — flagged, not pressed.
- **A genuine boundary question, not a new group proposal:** where do personified abstract/adversarial
  forces that are not literally "the devil, evil spirits, Satan" belong — Death, Sin, Sheol/the grave,
  personified in Hebrew poetry as quasi-agents (Ps 49:14, Gen 4:7)? Under the researcher's own stated
  T4 scope (personal spiritual adversaries) these may not fit T4 cleanly, but they may not fit
  "natural world" either. Named as an open boundary case for the researcher's own call, not resolved
  here.

### 3c.1 Researcher's follow-up — "Places," and checking the debated terms against live data

**Researcher, verbatim:** *"corporate/collective and man-made are both good catches and behave
differently. Another you made me think is places. it could be argued that sheol is a place, as well
as heaven and earth. Death, sin, circumcision, fasting, baptise, are open for debate."*

**"Places" is a strong, distinct candidate — checked against live data, not left as a suggestion:**

| Term | Code | Live occurrences | Current tag |
|---|---|---|---|
| Heaven | H8064 / G3772 | 416 + 274 = **690** | **untagged entirely** |
| Earth/land | H0776G | **2,278** | **untagged entirely** |
| Sheol | H7585 | 66 | `T2` (excluded from analysis) |

Heaven and earth are two of the highest-frequency untagged terms in the whole corpus — nowhere near
edge cases — and Sheol is currently sitting in the "excluded" bucket, which is exactly the kind of
premature exclusion §4 of the main report already found reason to distrust. **`Places` looks like a
genuinely missing, high-value group, distinct from `natural world`** (a place is a location a
movement happens at/toward/from; storm/water/fire/animals are phenomena or creatures, not locations
— real overlap exists at the edges, e.g. "the sea," but the core distinction holds).

**The debated terms, checked directly — three of the five turn out to be already correctly homed,
not endpoint-type candidates at all:**

| Term | Code | Current tag | What this means |
|---|---|---|---|
| Sin | G0266 | **`M56`** (Sin & Guilt) | **Already a characteristic in its own right** — not an endpoint/party question |
| Circumcision | H4139 / G4061 | **`M32`** (Covenant) | **Already a characteristic in its own right** |
| Fasting (noun) | G3521 | **`M21`** (Fasting & Piety) | **Already a characteristic**; the verb form "to fast" (H6684) is separately `T3` (Operations) — a clean existing noun/verb split |
| Baptize (verb) | G0907 | `T3` (Operations) | Correctly an action verb |
| Baptism (noun) | G0908 | **untagged** | Minor asymmetry — its sibling concept (fasting, noun) got an M-code, baptism's noun form didn't. Small, separate follow-up, not part of this debate |
| **Death** | H4194 / G2288 | `T2` (excluded) | **The one genuinely still open** — could be (a) correctly excluded, (b) a `Places`-type (a realm/state, alongside Sheol), or (c) adversarial-adjacent personified force. Not resolved here. |

**So the "open for debate" list resolves to one real question, not five:** Sin, circumcision, and
fasting are already correctly classified as characteristics — they were never endpoint-type
candidates, the debate dissolves once checked against live data. Death is the one term still
genuinely open, and it sits at the same fork as Sheol (§3c's own boundary question) — plausibly a
`Places` member, plausibly adversarial-adjacent, plausibly correctly excluded. Not decided here.

### 3c.2 Locked-in architecture principle — cluster tagging never drives new verse/word onboarding

**Researcher, verbatim:** *"so in the new design — these backfill become cluster tagged (T-codes)
but not word-registry linked (and therefore does not drive new verse introductions)."* **Confirmed,
at the schema level, not just by design intent:**

```sql
CREATE TABLE "cluster_strong" (
  ..., FOREIGN KEY ("strong") REFERENCES "strong"("strongNumber"),
  FOREIGN KEY ("cluster_code") REFERENCES "cluster"("cluster_code")
)
```

`cluster_strong` has exactly two foreign keys — `strong` and `cluster_code` — and **no reference to
`word_registry` anywhere**, matching `cfg_table.use`'s own stated intent word-for-word ("Cluster
membership is a property of the Strong's code itself... deliberately has no FK/dependency on
[word_strong/word_registry]"). Cluster assignment is a pure classification act on a `strong` row that
**already exists** (whether `origin='word'` or `origin='backfill'`) — it cannot create a new `strong`
row, cannot trigger a STEP pull, and cannot promote a term to registry-word status. New verse/term
introduction is driven entirely by the two `detail_one()` origins (`'word'` — deliberate registry
onboarding; `'backfill'` — the automated completeness sweep) — cluster tagging sits strictly
downstream of both and feeds neither. **This means reallocating `heaven`/`earth`/the whole backfill
pool into `Places` or any other new T-code group is bounded, additive metadata work on data that
already exists — not a trigger for pulling more of the Bible in.** Locked in as a governing
architecture fact for this escalation, not merely a working assumption.

## 4. The standing constraint this work must operate under

`feedback_iba_backfill_cluster_assignment_via_analysis_not_bulk_automation` (already governing this
project): **no bulk keyword-crossmatch or LLM-crossmatch tagging into clusters — cluster assignment
happens via verse-context analysis, one candidate at a time.** This is not a new rule invented for
this escalation; it already applies, and it means the ~5,271-strong candidate pool above is a real
body of analytical work, not a script that can be run once and trusted. Sizing it (§3) is legitimate
scoping; assigning it is not something this document does or should do unilaterally.

## 5. Proposed method, for approval before any actual reallocation

Not decided here — offered as a starting point for your disposition, in the same spirit as the main
report's corrective-action register:

0. **Decide the adjective-rooted-characteristic question (§3a) first — it governs both directions of
   movement.** Whether `characteristic` can be adjective-form or is strictly noun/verb (with every
   adjective/adverb routed to `qualifier`) determines both what leaves the current 3,034 M-tagged
   strongs and what the untagged pool's 629 adjectives/158 adverbs become. Sequencing steps 1-4 below
   ahead of this would mean redoing work once the rule is set.
1. **Triage pass, not a blind sequential grind.** Order the ~5,271 candidates by how much they
   actually matter — live occurrence frequency first (a noun appearing 600 times is worth resolving
   before one appearing twice), and cross-reference against verses that already carry an M-coded
   characteristic (a candidate co-occurring heavily with an existing characteristic's verses is a
   stronger signal for either `qualifier` status or a missed characteristic than one that never
   co-occurs with any M-code at all).
2. **One candidate, one verse-context check, per the standing rule** — no batch LLM sweep assigning
   clusters from gloss text alone (the exact failure mode `T3`'s own incompleteness and the M/T3
   overlap already demonstrate can happen even from a real prior pass).
3. **The verb bucket (441) is the cheapest, highest-confidence first slice** — action verbs are the
   category `T3` already has a coherent, evidence-checked precedent for (§4.1 of the main report);
   closing this gap first tests the method on the smallest, best-understood bucket before tackling
   the much larger and more ambiguous noun bucket (4,043).
4. **The `qualifier` role (§6 of the main report) stays blocked until this reallocation reaches at
   least the verb and adjective/adverb buckets** — `qualifier`'s own working definition depends on
   knowing which words genuinely couple with a characteristic, which this reallocation is what would
   establish.

## 5a. Phase 1 done — M-code adjective/adverb review (researcher-directed sequencing: M → T first)

**Researcher, verbatim, this round:** *"I suggest that we proceed to methodically reclassify the
strongs into the correct M and T codes. I suggest to start by doing M -> T, then T3 -> T*, and T2 ->
T*. Then evaluate what is left in T2 and T3. Then re-evaluate every cluster code, special attention
to M-code naming to check if that has not changed."*

Phase 1 (M → T): read all 388 currently M-tagged adjectives/adverbs against their actual gloss and
M-code name — not the POS-only signal §3a used to size the question. Full dataset persisted:
`iba/docs/1598-phase1-m-adjective-review-v1-20260908.csv` (388 rows: strong, language, POS, gloss,
cluster_code, cluster_name, live occurrence count).

**Finding: §3a's own hypothesis was wrong, checked against real content, and the correction matters.**
The overwhelming majority — on this read, roughly 380 of 388 — are exactly where they belong.
`H1343`/`H3093` "proud" → `M08` (Pride & Arrogance); `H6800B`/`G5011` "humble"/"lowly" → `M09`
(Humility & Lowliness); `H6662`/`G1342` "righteous"/"just" → `M12`; `H2450`/`G4680` "wise" → `M16`;
`G3629`/`G2155`/`H7349` "compassionate" → `M50`; `H0394`/`H0393` "cruel" → `M10`; `G3524`/`G4705`
"sober"/"eager" → `M69` — these are not qualifiers of some other characteristic, they **are** the
characteristic, named in adjective form, matching the M-code's own theme directly. §3a's
part-of-speech signal was a legitimate way to *find* candidates worth checking; it was never a
reliable way to *decide* them, and this pass proves that concretely rather than leaving it as a
caveat. **Step 0's "adjective-rooted characteristic" question (§5) is answered empirically for the
overwhelming majority of cases: yes, and it is the norm here, not the exception.**

**A small number of genuine mismatches, found by the same read — candidates for a verse-context
check, not yet confirmed or moved:**

| Strong | Gloss | Currently in | Why it looks off |
|---|---|---|---|
| `G3117` | "long/distant" | `M18` (Desire & Longing) | A temporal/spatial adjective ("long" in time/distance) mapped to a desire-characteristic — plausible confusion with a different lemma (e.g. `makrothymia`, "long-suffering"), not confirmed |
| `G2960` | "the Lord's" | `M23` (Strength & Courage) | An ownership/relational adjective ("belonging to the Lord," as in "the Lord's day") has no obvious connection to strength |
| `H6001A` | "labour[er]" | `M24` (Faintness & Despair) | Plausible via "labour → weariness," but not a direct semantic match |
| `H3477H` | "Jashar" | `M13` (Faith & Faithfulness) | Reads as a proper noun (the Book of Jashar) rather than a common adjective — only 2 live occurrences, worth checking what they actually are |
| `H8549J` | "Thummim" | `M61` (Purity & Holiness) | Reads as the priestly object (Urim and Thummim) rather than the common adjective "unblemished" this code's other variants carry — 1 occurrence |

**Not moved.** These 5 need an actual verse read (per the standing one-candidate-at-a-time rule),
not a decision from gloss text alone — flagged here as Phase 1's real output, not resolved.

**Method note for Phase 2/3 (T3, T2), carried forward:** do not repeat the POS-based sizing mistake
at larger scale. §3's 4,043-noun and 441-verb buckets need the same content-read discipline this
adjective pass just demonstrated, not a lighter-touch pass because the numbers are bigger.

## 5b. Your dispositions on the 5 flagged candidates — verse-checked before writing, 3 of 4 more complex than the instruction implied

**Researcher, verbatim:** *"H6001A is a type of human -> T*; G2960 is divine -> T*; H3477H, H8549J
other objects -> T3; G3117 stay in M18."*

Pulled the actual live verses for the four being moved before writing anything (matching the
one-candidate-at-a-time verse-context rule) — the check is not a formality here, it changed the
picture for 3 of the 4:

| Strong | Real live occurrences | What this shows |
|---|---|---|
| `G3117` | — | **No change — confirmed, stays `M18`.** |
| `H6001A` | "workmen's" (Judg.5.26), "misery" (Job.3.20, Job.20.22), "worker's" (Prov.16.26) | **The code is genuinely polysemous, not a clean single move.** Two occurrences are a human-role noun (fits "type of human," `T8`); two are an abstract-state noun ("misery") that plausibly still belongs in `M24` (Faintness & Despair) — its current home. This looks like a **dual-tag case** (keep `M24` for the misery sense, add `T8` for the worker sense), matching §3b's own "dual membership is the norm" finding, not a straight relocation. |
| `G2960` | "Lord's" (Rev.1.10 "the Lord's day", 1Cor.11.20 "the Lord's supper") — only 2 occurrences | Confirmed divine-relational, but it is a **possessive/relational adjective** ("belonging to the Lord"), not itself a name of God. `T7`'s own live definition is "set ONLY when this code IS ITSELF a name." Adding `G2960` would quietly widen `T7`'s grain to cover divine-*relational* terms, not just divine names — a real definitional question, not just one more row, even though only 2 occurrences are at stake. |
| `H3477H` | "Jashar" (2Sam.1.18, Josh.10.13) | Confirmed: this is **"the Book of Jashar"** — a proper-noun reference to a document, genuinely an "object" as you said. |
| `H8549J` | "Thummim" (1Sam.14.41) | Confirmed: this is **the priestly artifact** (Urim and Thummim), genuinely an object. |

**`T3` doesn't fit `H3477H`/`H8549J` as literally stated** — `T3`'s own definition is human
operation/movement *verbs*; a book title and a priestly object are neither. The closest existing
candidate is the not-yet-created **man-made objects/artifacts** group named as a possibility in
§3c — not built yet, so there is nowhere to actually place these two today. Not written anywhere
yet, pending your confirmation of: (a) whether `T3` was shorthand for that not-yet-built group, and
(b) `H6001A`'s dual-tag treatment, and (c) whether `G2960`'s addition to `T7` should also formally
widen `T7`'s own stated definition, or wait for the endpoint-family rework in §3c/§3b.

## 6. What this document is not

Not a build plan, not an approval to start writing to `cluster_strong`. It is the seed and the sizing
§4/researcher instruction asked for — the method in §5 needs your confirmation (or correction) before
any candidate is actually reclassified.
