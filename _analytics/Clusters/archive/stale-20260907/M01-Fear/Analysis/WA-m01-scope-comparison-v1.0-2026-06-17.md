# M01 — Scope Comparison Test (lemma vs signature) · C1 & C2 · v1.0

**File:** WA-m01-scope-comparison-v1.0-2026-06-17.md
**Date:** 2026-06-17 · **Prefix:** WA · **Type:** Internal analytical test (markdown)
**Data basis:** five-file fan-out extract, focus terms only. Read-only; nothing re-based. **Verse lexical data only.**
**Purpose:** Run both membership methods side by side and surface the disagreements as readable verse cases, so the scope decision can be made on the data rather than in the abstract. This instalment covers **C1 (Reverent fear)** and **C2 (Fear/afraid)** — the known-divergent pair — as a format check before extending to C3–C11.
**Method definitions used here:**
- **Lemma membership:** occurrences of the characteristic's chosen word-list.
- **Signature membership (reverent):** any fear-occurrence with `object_type = God` AND `valence ∈ {commanded, righteous}`, regardless of word.

---

## 1. C1 Reverent fear — the headline numbers

| | count |
|---|---:|
| Lemma membership | 195 |
| Signature membership | 123 |
| Agreement (both) | 81 |
| Lemma-only (lemma includes, signature excludes) | 114 |
| Signature-only (signature includes, lemma misses) | 42 |

The two definitions of the *same* characteristic agree on fewer than half the occurrences. But — and this is the important part — **the raw disagreement is partly real and partly a data-quality artefact.** Reading the cases separates the two.

## 2. The strong case FOR switching: reverence the lemma list misses (signature-only, 42)

These are unmistakable reverence-of-God occurrences that the C1 word-list does not contain, because they are carried by the *ordinary-fear* lemmas (Hebrew *yare'*, Greek *phobeomai/phobos*) or by trembling/dread/dismay words used Godward. A sample, with the decisive group first:

**The entire New Testament reverence set — all missed by lemma (this is the material finding):**
- Luk 23:40 "Do you not fear God, since you are under the same sentence of condemnation?"
- Act 10:2 "a devout man who feared God with all his household"
- Act 10:22 "an upright and God-fearing man"
- 2Cor 5:11 "knowing the fear of the Lord, we persuade others"
- Eph 6:5 "obey your earthly masters with fear and trembling"
- Col 3:22 / 1Pe 2:17 "Fear God." / Rev 11:18; 14:7 "Fear God and give him glory"; 15:4 "Who will not fear, O Lord… ?"

Under the lemma anchor, C1 is OT-only and its christological/NT dimension reads as *absent*. **It is not absent — it was lost to a missing word.** Switching (or the hybrid) makes C1 bi-testamental and restores the NT reverence material. This alone is a material consequence: a published claim about reverent fear being an Old-Testament characteristic would be wrong.

**Classic Hebrew reverence also missed:**
- Job 28:28 "the fear of the Lord, that is wisdom"
- Pro 10:27 "The fear of the Lord prolongs life"; Pro 16:6 "by the fear of the Lord one turns away from evil"
- Isa 11:3 "his delight shall be in the fear of the Lord"
- 1Ch 16:25 "he is to be feared above all gods"; 2Ki 17:36, 39 "you shall fear the Lord"

These are central reverence verses sitting under the ordinary-fear lemma — exactly the occurrences a lemma-bounded C1 should contain and does not.

## 3. The reasonableness check: where the data itself is suspect

Reading the **lemma-only (114)** cases shows the signature method, as defined, **cannot be trusted as-is** — for a reason that is itself a finding about data quality.

Breakdown of the 114 C1-lemma occurrences the signature *excludes*, by `object_type × valence`:

| object_type | valence | n | what these actually are |
|---|---|---:|---|
| **None** | **righteous** | **46** | mostly genuine reverence-of-God with `object_type` left unset (e.g. Gen 22:12 "fear God"; Exo 18:21 "men who fear God"; Gen 28:17 "How awesome is this place") |
| None | neutral/commanded | 22 | mixed: some reverence, some neutral |
| person | neutral/righteous/commanded | 21 | reverence of **parents/people** (Lev 19:3 "revere his mother and father") and fear *of* persons |
| God | neutral | 9 | God-directed but tagged neutral |
| God | sinful | 5 | failure to fear God (Exo 9:30 "you do not yet fear the Lord") — a real category |

The decisive row is the first: **46 reverence occurrences have `object_type = None`**, so the signature filter (`object_type = God`) wrongly drops them. The signature is not finding "non-reverence"; it is being defeated by an **under-populated `object_type` field**. A naive object=God signature would therefore *exclude genuine reverence* — the opposite of what we want.

**Two specific data-quality flags (verses to re-test):**
1. **`object_type` is unreliable for reverence.** At minimum the 46 "None/righteous" cases and the 9 "God/neutral" cases need re-checking — the verses are reverent (Gen 22:12, Exo 18:21, Isa 29:23, etc.) but the field does not record `object = God`. Until this field is cleaned, any object-based signature is built on sand.
2. **A homonym-noise term leaked into the reverent signature.** Mic 7:17 H2119B ("the crawling things of the earth") is tagged `object=God, righteous` — almost certainly a mis-set field (the word means "crawl," not reverence). This is the kind of suspect cell the test exists to catch.

There is also a genuine *semantic* complication the cases reveal, separate from field quality: **reverence has legitimate non-God objects** — parents and the sanctuary (Lev 19:3, 19:30, "revere his mother and father," "reverence my sanctuary"). A signature keyed only to `object = God` mishandles these by design. So "reverent fear" may itself need sub-distinguishing (reverence of God vs reverence of the sacred/parental) — a question the lemma method hides and the signature method exposes.

## 4. C2 Fear/afraid — the 28 movers

Defining C2 by its lemma list and asking which of those occurrences are reverent-of-God by signature gives the C1↔C2 overlap: **28 occurrences** that, under signature scope, would leave *Fear/afraid* and join *Reverent fear*. They are the same verses as the signature-only set above that use C2's lemmas — the NT reverence (Act 10, 1Pe 2:17, Rev 14:7, etc.) and the Hebrew "fear the Lord" verses (Job 28:28, Pro 10:27, 2Ki 17:36). Reading them, they are **not ambiguous**: every one is reverence of God expressed with the ordinary-fear word. Under the lemma anchor they inflate C2 and hollow out C1; under signature they sort correctly.

The effect of moving them: C2 becomes more purely "forbidden/neutral fear of circumstance" (its "fear not" character sharpens), and C1 gains its NT dimension. Both characteristics read *truer* after the move — which is the substantive argument for signature membership.

## 5. Interim read (C1 & C2 only)

- **The method difference is real and material — decisively so for C1.** The missed NT Greek reverence changes C1 from an OT-only characteristic to a bi-testamental one and restores its christological dimension. This is not count-drift; it is a portrait change and a potential finding reversal. On the evidence so far, the lemma anchor is *wrong* for reverent fear.
- **But pure object-based signature is not trustworthy yet,** because the `object_type` field is under-populated (46 reverence occurrences tagged None) and carries at least one homonym-noise leak. A signature run on the field as it stands would mis-drop genuine reverence.
- **Practical implication, matching the test's purpose:** the most defensible route is the **gather-by-lemma / assign-by-signature hybrid**, but with the signature **led by valence (righteous/commanded) and verified per verse**, not keyed blindly to `object_type` — and with the `object_type` field sent back for a cleaning/re-test pass first. Where the field and the verse disagree, the verse wins and the field is corrected.
- **A new sub-question surfaced:** reverence of God vs reverence of parents/sanctuary (Lev 19) may warrant separating — the lemma method conceals it.

## 6. Format check and next step
This instalment shows the format: numbers, then **readable cases** for both disagreement directions, with field-quality flags called out separately from genuine method-differences. If this is the right shape, the same treatment extends to **C3–C11**. Expectation (a hypothesis, not a result): the *state* fears (dread, terror, horror) will show little material difference because their portraits do not lean on object at all, while characteristics with a God-ward dimension will behave like C1. The C3–C11 pass will also widen the `object_type` data-quality audit across the cluster.

*End of v1.0 — C1 & C2 instalment.*
