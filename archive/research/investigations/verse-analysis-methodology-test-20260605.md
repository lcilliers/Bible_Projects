# Verse Analysis Methodology — reality test (one verse per complexity group)

> Read-only test, 2026-06-05. Worked **one real M01 verse in each of the four complexity groups**
> (`wa-verse-analysis-methodology.md` §6), applying the 6-step workflow + span rules + keyword spec, and
> measured the cost. Scripts: `_exploratory_select_complexity_group_verses_v1`,
> `_exploratory_assemble_verse_packages_v1`.
>
> **What "cost" means here:** *assembly* (DB queries to build the verse's input pack) is directly measured.
> *Analysis* (the AI meaning derivation) cannot be self-timed, so it is reported as **cycles** — the count
> of distinct lookups/decisions the methodology required — plus a relative-effort read. In the real
> pipeline each verse is ~1 API call (~$0.008, per `feedback_brief_classifier_pass`); complexity scales the
> **prompt + output size**, not the call count (except multi-T1's reuse lookup).

## Measurement summary

| Group | Verse | Spans | Assembly | Analysis cycles | Output |
|---|---|---|---|---|---|
| Possible set-aside | Deu 1:19 | 1 | 4.2 ms / 2 q | **1** (read → reject) | set-aside (physical, implied dread noted) |
| Single span | Exo 1:17 | 1 | 0.8 ms / 2 q | **1** (sense → meaning+kw) | meaning + keywords |
| T2 + T1 | Exo 3:6 | 2 | 0.3 ms / 2 q | **2** (pair T2 → meaning) | meaning + keywords (T2 paired) |
| Multi-T1 | Lev 19:3 | 2 | 0.5 ms / 2 q | **3+** (classify T1 → meaning+kw → seed reciprocal; + reuse check) | meaning + keywords + reciprocal finding |

**Group sizes for M01** (of 834 verses): possible-set-aside **78** · single **116** · T2+T1 **128** ·
**multi-T1 527 (63%)**. The expensive group is the *majority* for M01.

---

## 1. Possible set-aside — Deu 1:19

**Input:** *"…we set out from Horeb and went through all that great and **terrifying** wilderness…"* —
1 span: `terrifying` (H3372G, "to fear: revere"). Corpus: 194.

**Analysis.** [Step 1–2] The span describes the **wilderness** as terrifying — a descriptive attribute of a
*place*, not a named inner state of a person. [Step 3] single span. **Decision:** set aside as
`physical_only` — but the evidence-note records the *implied* inner reaction (a dread-evoking environment;
P3 "implied from/to"): the wilderness is fearsome **to** the people who saw it. So the term's semantic
record keeps it; the cluster corpus does not.
**Cost:** 1 cycle. Genuinely quick — but **not zero**: it still required a real (if fast) judgement that the
fearsomeness is environmental, plus the implied-subject note.

---

## 2. Single span — Exo 1:17

**Input:** *"But the midwives **feared** God and did not do as the king of Egypt commanded…"* — 1 span:
`feared` (H3372H). Corpus: 107.

**Analysis.** [Step 2] sense-in-use = reverent fear of God that **governs conduct**. [Step 4] from = the
midwives (subject); to = **God** (object, spirit being); situational = under Pharaoh's command (conflict);
genre = narrative. [Step 5] clear, no clarification. [Step 6] →
- **Meaning:** *"The midwives' reverent fear of God governs their action: fearing God, they refuse
  Pharaoh's order to kill the infants — fear of God as the controlling orientation that overrides human
  command."*
- **Keywords (new spec):** `fear revere` (gloss) · `reverence god` · `fear of god` · `governs conduct` ·
  `defies command` · `god (to)` · `moral courage`.
**Cost:** 1 cycle. Light — one clean pass.

---

## 3. T2 + T1 — Exo 3:6

**Input:** *"…Moses hid his face, for he was **afraid** to **look** at God."* — 2 spans: `afraid`
(H3372G, M01) + `look` (H5027, **T2** "to look"). Corpus: 194.

**Analysis.** [Step 3] classify the sibling: `look` is **T2** — the *action the fear inhibits*. **Pair it
in:** the fear's object/trigger is *looking at God*; Moses is afraid **to behold** the divine. [Step 4]
from = Moses; to = **God** (theophany); somatic expression = *hid his face*. [Step 6] →
- **Meaning:** *"At the burning-bush theophany Moses is afraid to look at God and hides his face — reverent
  dread before the divine presence that inhibits the very act of beholding (T2 'look'), expressed
  somatically by covering the face."*
- **Keywords:** `fear revere` (gloss) · `afraid to look` (T2 paired) · `hides face` (somatic) · `reverent
  dread` · `divine presence` · `god (to)` · `beholding inhibited`.
**Cost:** 2 cycles — recognising `look` as the inhibited object-action, then pairing it into the meaning.
The T2 pairing *did* add real work and *did* enrich the meaning (the fear is specifically of *beholding*).

---

## 4. Multi-T1 — Lev 19:3

**Input:** *"Every one of you shall **revere** his mother and his father, and you shall **keep** my
Sabbaths…"* — 2 spans: `revere` (H3372H, M01) + `keep` (H8104G, **T1: M30 Obedience**, "to keep: obey").
Corpus: 107.

**Analysis.** [Step 3] the sibling `keep` is **T1 (M30)** → multi-T1. Both directions: reverence runs
*horizontally* (subject → mother/father, other humans); keeping runs *vertically* (subject → God's
sabbaths). [Step 4] genre = apodictic law, the two commands set in **parallel**. [Step 6 + span rules] →
- **Meaning (names the T1 sibling):** *"Each Israelite is commanded to revere mother and father —
  reverential fear directed horizontally to parents — set in deliberate parallel with keeping God's
  sabbaths (T1: M30 Obedience); the verse binds reverence-of-parents and obedience-to-God as twin
  covenant duties."*
- **Keywords (incl. M01 gloss + M30 gloss + principles):** `fear revere` (M01 gloss) · `keep obey`
  (**M30 gloss**) · `reverence parents` · `revere mother father` · `obedience sabbath` · `covenant duty` ·
  `parents (to/horizontal)` · `god (to/vertical)` · `apodictic parallel`.
- **Reciprocal finding:** seed a candidate finding in **M30 (Obedience)** — "keep my sabbaths," co-occurring
  with reverence-of-parents, for M30's consideration.
- **Reuse check:** has the `revere + keep/obey` combination been analysed before? If yes → bring that prior
  meaning into focus and compare rather than re-derive.
**Cost:** 3+ cycles — classify the T1 sibling, pull its gloss/cluster, weave it into meaning + keywords,
seed the reciprocal, run the reuse check. Clearly the heaviest, and the **output is richest** (two
characteristics, two findings).

---

## What the test shows

1. **Data assembly is a non-issue** — <5 ms, 2 queries per verse. The cost is entirely in the *analysis*.
2. **The complexity gradient is real and the triage is justified:** 1 → 1 → 2 → 3+ cycles, with output
   richness rising in step. Set-aside and single-span are genuinely cheap; multi-T1 is several times the
   work and emits reciprocal findings.
3. **But the cheap groups are not the bulk** — for M01, **multi-T1 is 63%**. Triage saves real effort on the
   37% that are set-aside/single/T2, but the majority still need the heavy path. (Study-wide ~30% are
   multi-T1 — still the dominant single cost.)
4. **Keyword finding — your worry is confirmed.** The new keyword spec (gloss + *all* T1 glosses +
   7-principle capture, no cap) produces a **heterogeneous bag**: faculty tokens (`reverent dread`), glosses
   (`fear revere`, `keep obey`), relational/direction tags (`god (to)`, `parents (horizontal)`), somatic
   tags (`hides face`), genre tags (`apodictic parallel`). That is **excellent as a descriptive record**,
   but it is **poor as a clustering signal** — the original keyword purpose (atomic, reused faculty tokens
   that aggregate into faculty axes) is *diluted* by mixing in glosses, subjects, objects and principle
   tags that don't repeat cleanly across verses. **This test supports separating two keyword roles:**
   - **atomic faculty keywords** — few, reused, the clustering signal (the original design);
   - **descriptive tags** — gloss / relation / direction / somatic / genre — rich, for the record and the
     audit, *not* for clustering.
   Folding both into one undifferentiated list looks like the "wrong direction" you sensed.

## Verdicts (researcher grading, 2026-06-05) — and what they reveal

All four CC analyses were graded. **All four were wrong, each in a different way** — and that *is* the finding.

| Verse | Verdict | The error | Which §0 AI-bias it is |
|---|---|---|---|
| Deu 1:19 | **FAIL** | Set aside as physical. But *terrifying* **names an inner-being state** (terror); the wilderness is just its **cause/situation (from)**. In scope. | **Narrowing** — treating the grammatical object as making it non-inner |
| Exo 1:17 | **PARTIAL** | Read as fear "controlling" conduct. But the reverence is **strengthening their resolve** (greater than Pharaoh's threat) — *not* negative, *not* controlling. | **Imposed framing** — defaulting to fear-as-constraint; "reasonable over correct" |
| Exo 3:6 | **OPEN** | Stated a confident "reverent dread." But it is genuinely unsettled: court **custom** (not looking at a superior)? *frightened* vs *reverent*? | **False confidence** — failing to surface the open questions |
| Lev 19:3 | **WRONG PAIRING** | Wove M30 obedience into M01's meaning/keywords. But the two spans **do not influence each other** — reverence and sabbath-keeping are independent; clouding M01 with the obedience part is an error. | **Forced structure** — pairing where there is none |

**The four errors are exactly the §0 AI tendencies the foundations named** (narrowing, imposed framing,
false confidence, forced order). So the test **empirically proved the gravest risk is real**: cold,
per-verse, in-isolation Pass A reproduces those biases — confidently. The researcher's review caught every
one, which is itself the foundations' predicted mitigation (researcher review) working.

**The single remedy runs through all four:** the **term's wider use (its corpus)**.
- Exo 1:17 — compare H3372's other uses to settle **valence**: is fear-of-God positive/negative,
  controlling/strengthening? (Here: strengthening.)
- Exo 3:6 — wider use to resolve **sense**: frightened vs reverence/respect; and the cultural custom.
- Deu 1:19 — the term's range shows *terror* is an inner state regardless of its grammatical object.
- Lev 19:3 — reading reverence across its corpus shows the obedience span is **independent**, so it
  flows to M30, it does not cloud M01.

**The span rule is refined by Lev 19:3:** weave a sibling into the target meaning/keywords **only if it
influences the target span**. Independent siblings are **not silently ignored** — they **flow through to
their own cluster** (reciprocal finding) — but they do **not cloud** the target. "Never ignore" ≠ "always
weave in."

## Where this gets us

This is the pivot, not a dead end. Four cheap verses bought three conclusions:

1. **Per-verse-in-isolation Pass A is unreliable** — it produces confident, biased readings (4/4). Reading a
   verse cold is the problem.
2. **The term's corpus is the unit that disambiguates** — valence, sense, and the influence test all resolve
   only by reading the span against the term's *other occurrences*. This is the analogy of Scripture
   (Principle 6) and the v2_9 "per-term meaning corpus", pulled forward **into the meaning stage**.
3. **Open questions are first-class output** — where the corpus doesn't settle it (Exo 3:6), Pass A emits the
   question, it does not invent an answer.

→ **The process should be term-anchored, not verse-cold:** take a term, read its whole corpus together so
each occurrence is calibrated against the term's range; emit per-verse meaning + open questions from that
vantage; apply the influence test for siblings. This also reinforces the meaning-centric direction and is
more efficient (one term, all its verses, read once).

## Rough extrapolation (~80k verses)

At ~1 API call/verse (~$0.008) a single full pass is on the order of **~$650 + wall-time**, *before*
multi-T1's larger prompts/outputs and any reuse lookups. The triage lets the 2/3-ish cheap verses use a
smaller call; the multi-T1 majority (per cluster) carries the real cost. **Implication:** the methodology is
affordable per-pass, but **the keyword design choice is the live risk** — a bloated keyword contract
multiplies output tokens on every verse and degrades the very grouping it is meant to feed.

## Recommendation

- **Keep** the 6-step span-focal workflow and the complexity triage — both validated.
- **Revisit the keyword spec** (the §7 open decision) along the two-role split above *before* any bulk run —
  this is the cheapest moment to get it right.
- Optional next probe: run the same 4 verses through a **two-list keyword** variant and compare clustering
  behaviour, to settle the keyword design on evidence.
