# M01 — Data Quality Verdict & Scope Approach (re-based on 2026-06-18 refresh) · v2.0

**File:** WA-m01-scope-comparison-v2.0-2026-06-18.md
**Date:** 2026-06-18 · **Prefix:** WA · **Type:** Internal analytical assessment (markdown)
**Supersedes:** `WA-m01-scope-comparison-v1.0-2026-06-17.md` (interim C1/C2 read on the pre-refresh data).
**Change note:** Re-run against the refreshed extract (`wa-ve-lexical-extract-M01-20260618-b{1..5}of5`) and the new per-characteristic file (`wa-m01-by-characteristic-verse-records-20260618`). Answers two questions: (1) the true quality of the data; (2) which membership approach to use going forward. Includes an **independent verse-read of `valence`** (the field you flagged as AI-generated), reading the verse text directly rather than trusting the field.
**Data basis:** verse lexical data only. Read-only; nothing re-based in the database.

---

## 1. What the refresh actually changed (old → new, focus terms)

Comparing the two five-file extracts occurrence-by-occurrence (1,036 focus occurrences in both):

| Field | Occurrences changed |
|---|---:|
| `divine_involvement` | **50** (None→object 39, None→agent 10, None→giver 1) |
| `location` | 5 (the de-dup fix) |
| `object_type` | **0** |
| `valence` | **0** |
| `faculty`, `type`, `sense`, `cause` | 0 |

So the refresh moved **only `divine_involvement` and `location`**. This is the key to reading everything below: the foundational zero-pad fix (Strong's seed lists were short-form, so *Elohim* H430 and the negation/faculty lemmas silently never matched) surfaced in **`divine_involvement`**, not `object_type`. The data-quality problem flagged in v1.0 was real, and this is its fix — but it lands in a different field than v1.0 assumed.

## 2. Data quality — field by field (your first question)

**`divine_involvement` — much improved; now the reliable "Godward" signal, but still incomplete when None.**
The 50 restored detections are all correct on inspection: the reverence verses that v1.0 saw as `object_type=None` (Gen 22:12 "fear God"; Job 1:1, 1:8 "feared God"; Psa 25:12 "fears the Lord") now correctly carry `divine_involvement=object`. Of the 73 C1-lemma occurrences with `object_type=None`, 40 now show `divine_involvement=object` and 4 `agent`. **Verdict: high precision when positive — trust a positive value.** But it still has **false-negatives**: the substantival reverence forms ("those who fear him", "fear your name") frequently remain `divine_involvement=None` (see §3, SET B — 41 such cases). The fix caught explicit-object "fear God"; it did not catch implied-object "those who fear him". **So `divine_involvement=None` cannot be read as "not Godward."**

**`object_type` — unchanged; incomplete for Godward construct forms; do not use it as the Godward signal.**
`object_type` stayed `None` on the construct/genitive and substantival reverence forms ("the fear of the Lord", "those who fear him"). The new file's own caveat calls `object_type` read-authoritative and "trust it on disagreement" — that holds for *what kind of thing* the named object is, but it under-captures the *divine* object in these grammatical forms. **Verdict: reliable when populated, but the wrong field for detecting reverence-of-God. Use `divine_involvement` for that.**

**`valence` — unchanged (the parked AI-read), but on independent verse-reading it is substantially better than its "parked" status implies.** Detail in §3. **Verdict: usable for M01 with boundary confirmation; not yet safe as a sole, unverified key corpus-wide.**

**`faculty`, `type`, `sense`, `cause` — stable mechanical fields, unchanged.** These were already derived from morphology/POS/lexicon and carry no new risk.

**`location` — minor improvement** (the de-dup; spirit/breath sense-gating). Does not affect the scope question.

**Term-list residue (not a field issue):** Mic 7:17 **H2119B** ("crawling things of the earth") is still a focus term tagged `object_type=God, valence=righteous`. The word means "crawl"; it belongs in the homonym group (B3), not in the reverence evidence. A term-list cleanup item, not a field error.

## 3. The independent `valence` read (reading the verses, not the field)

Because `valence` is the parked AI-read, I set the field aside and read the verse text directly for the two boundary sets where a valence error would distort membership.

**SET A — God is involved, but `valence` is *not* righteous/commanded (18 cases).** If `valence` were unreliable, these would be reverence mis-tagged as non-reverence. Reading them, **`valence` is right in almost every case**: it correctly tags the *absence* of fear as **sinful** ("you do not yet fear the Lord", Exo 9:30; "they do not fear the Lord", 2Ki 17:34; "we do not fear the Lord", Hos 10:3), God's *terrible deeds* as **neutral** ("great deeds of terror", Deu 4:34 — *mora* meaning terror, not reverence), *prohibitions* as **forbidden** ("you shall not fear the gods of the Amorites", Judg 6:10), and *fear of a human superior* as **neutral** ("I fear my lord the king", Dan 1:10). It even handles the hard syncretism case sensibly ("they feared the Lord but also served their own gods", 2Ki 17:33 → neutral). The few questionable `divine_involvement` positives here (false gods in Judg 6:10; the human king in Dan 1:10) are *divine_involvement* over-reach, not valence errors.

**SET B — `valence` is righteous/commanded, but `divine_involvement=None` (41 cases).** If `valence` were over-eager, these would be non-reverence mis-tagged as reverence. Reading them, **`valence` is right and `divine_involvement` is the one at fault**: these are the classic substantival reverence verses — "those who fear him" / "fear your name" / "fear me forever" (Psa 25:14, 31:19, 111:5, 119:63, 145:19; Neh 1:11; Jer 32:39; Mal 4:2). They are unmistakably reverent; the engine simply failed to attach God as the object because the form is substantival. Valence carried the reverence signal these cases needed.

**Two genuine `valence` edge-errors found** (out of ~60 read): Deu 7:21 ("you shall not be in dread of them, for the Lord your God is in your midst") is tagged *righteous* but is really commanded fearlessness toward enemies — a "fear not", not reverence; and the **person-directed awe** cases (Jos 4:14 "[Israel] stood in awe of [Joshua]"; 1Ki 3:28 awe of Solomon) are tagged *righteous* but are reverence of a human leader, not of God.

**Valence verdict:** on the M01 reverence boundary, independent reading **confirms `valence` in the large majority of cases** (well over 90% of the ~60 boundary cases read). It is more trustworthy than "parked AI-read" suggested. Its residual weakness is narrow and definable: it does not by itself distinguish (a) commanded *fearlessness* from reverent *fear*, or (b) reverence of God from reverence of human/sacred authority. Those two are exactly the boundary cases a verse-read confirmation must cover — a small, targeted set, not the whole corpus.

## 4. The re-based comparison — the material finding, quantified

C1 lemma membership (195) vs three signature definitions, on the refreshed data:

| Definition | Size | Greek (NT) reverence captured |
|---|---:|---:|
| Lemma anchor (word-list) | 195 | **1** |
| Signature A — `object_type=God` + reverent valence (the v1.0 signal) | 123 | 10 |
| Signature B — `divine_involvement` + reverent valence (improved signal) | 172 | 15 |
| Signature C — reverence-capable lemma + reverent valence, excl. person-object | 231 | **33** |

The decisive column is the last. **The lemma anchor captures essentially none of the New Testament reverence (1 occurrence); the signature methods capture 15–33.** The NT "Fear God" material (Act 10:2; 1Pe 2:17; Rev 14:7) is carried by the ordinary-fear lemma *phobeomai* and is invisible to a reverence word-list. This is unchanged in direction by the refresh and now sharper: under the lemma anchor, *Reverent fear* reads as an Old-Testament characteristic with no christological dimension, **and that is an artefact of the method, not a fact about Scripture.** Moving to a signature method also confirms the improved Godward signal works — Signature B catches 49 more reverence occurrences than the old `object_type` signature (172 vs 123).

## 5. A semantic finding the comparison surfaced (not a data error)

Reverence has **legitimate non-God objects**: human leaders (Jos 4:14; 1Ki 3:28) and the sacred (sanctuary, parents — Lev 19:3, 30), all tagged righteous with `object_type=person`. A signature keyed only to *God* mishandles these by design. **"Reverent fear" likely needs sub-distinguishing — reverence of God vs reverence of sacred/delegated authority** — a distinction the lemma method hides entirely and the signature method exposes.

## 6. Recommendation — which approach going forward (your second question)

**Adopt the gather-by-lemma / assign-by-signature hybrid, with `divine_involvement` (not `object_type`) as the Godward signal and `valence` as the reverence-quality key, confirmed by a targeted verse-read on the boundary.** Concretely:

1. **Gather** the candidate pool by lemma (the fear word-list) — reproducible, complete, keeps the audit trail.
2. **Assign reverence** by signature: Godward where `divine_involvement` is positive **OR** (substantival "fear/those-who-fear" form with reverent valence) — the second clause recovers the false-negatives §3 SET B exposed.
3. **Refine by `valence`:** righteous/commanded = reverence; sinful = failed/absent reverence (a real contrastive category, keep it labelled); neutral/forbidden = not reverence.
4. **Verse-read confirmation on the boundary only** — the two definable weak spots: (a) reverent valence + `divine_involvement=None`, and (b) reverent valence + `object_type=person`. Small, targeted; everything else rides on the now-reliable fields.
5. **Separate reverence-of-God from reverence-of-authority/sacred** (§5) as part of the assignment.

**Why not the alternatives.** The lemma anchor is demonstrably wrong for reverent fear (§4 — loses the NT dimension). A pure object-based signature is wrong because `object_type` under-captures the Godward construct forms (§2). A pure `valence`-based signature is close but inherits valence's two edge-errors (§3) and the parked-read status. The hybrid uses each field where it is now strong and confirms only where it is weak.

**Expectation for C2–C11** (a hypothesis to test, not a result): the *state* fears (dread, terror, horror, dismay) should show little material lemma-vs-signature difference because their portraits do not lean on object or Godward direction at all; the divergence will concentrate where a characteristic has a Godward or moral axis (reverent fear, and to a lesser extent fear/afraid and cowardice).

## 7. Items for the engine owner (CC's domain, not Claude AI's)

1. **`divine_involvement` false-negatives on substantival reverence forms** ("those who fear him", "fear your name"): the fix caught explicit objects but not implied/substantival ones — ~41 reverence occurrences in C1 alone still read `None`. Worth a targeted rule.
2. **`object_type` Godward construct gap:** "the fear of the Lord" genitive forms read `None`; if `object_type` is meant to be the authoritative object field, these need the divine object attached.
3. **Term-list cleanup:** Mic 7:17 H2119B ("crawl") should move to the homonym group (B3).
4. **Parked corpus `valence` read:** the M01-pilot valence is good enough to proceed *on M01* (§3), so it is not blocking here — but the corpus read should be completed before `valence` is relied on in other clusters.

## 8. Next step
On your decision to adopt the hybrid (§6), I can re-derive C1's membership on it as a worked example — gather, assign by `divine_involvement`+`valence`, confirm the boundary set by verse-read, and split God-ward from authority-ward reverence — and show the before/after against the lemma anchor. Then extend the same to C2–C11. Nothing is written to the database; this stays analytical until you direct a re-base.

*End of v2.0.*
