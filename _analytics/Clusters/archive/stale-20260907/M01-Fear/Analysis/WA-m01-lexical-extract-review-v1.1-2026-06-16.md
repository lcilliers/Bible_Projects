# M01 Lexical Extract — Review

**File:** WA-m01-lexical-extract-review-v1.1-2026-06-16.md
**Date:** 2026-06-16
**Prefix:** WA
**Document type:** Internal analysis (reusable; markdown)

**Data reviewed (v1.1):** the five-file fan-out extract — `wa-ve-lexical-extract-M01-20260616-b1of5.json` … `b5of5.json`. These replace the earlier `-b1of3` and full-M01 files, which are set aside.

**Previous output:** Supersedes `WA-m01-lexical-extract-review-v1.0-2026-06-16.md`.

**Change control:** v1.1 (minor) — assesses the revised five-file extract against the v1.0 findings. Adds §0 (improvement assessment). Marks earlier flags as *resolved / improved / persists / new*. Underlying schema is unchanged (3.34.0) but the file is now self-documenting and the interpretive fields are read-resolved.

---

## 0. Has the situation improved? — verdict

**Yes, materially.** The verse set is identical (922 verses; OT 763 / NT 159), but three classes of improvement are evident, and the two structural concerns from v1.0 persist with one new minor gap.

| v1.0 finding | Status in the new extract |
|---|---|
| `cause` near-total blind spot (12/1,036 resolved, 141 UNRESOLVED) | **Resolved** — now read-resolved: 179 resolved, **0 UNRESOLVED** on focus terms |
| `UNRESOLVED` meaning unclear; large backlog | **Resolved** — convention now explicit (absent = NONE/genuinely silent; UNRESOLVED = rare). Backlog cleared on read fields |
| Reverence vs dread undrawn within the cluster | **Resolved (new field)** — `valence` present on 99.7% of focus terms |
| `object_type` thin / fear-of-God not separable | **Improved** — read-classified; God 174, person 140, situation 122, threat 4, etc. |
| `divine_involvement` coarse (present/agent) | **Improved** — now God's *role*: object 165, agent 82, giver 7, addressee 2 |
| No documentation of fields/provenance | **Resolved** — full data dictionary now embedded in `meta` |
| Co-occurrence buried in `compound` strings | **Improved (new structure)** — co-terms are now first-class records with `cluster` codes |
| `anankē` ("necessity") cluster-membership doubt | **Persists** — still `focus_cluster=true`; read fields now *confirm* it reads as neutral, not fear |
| Book codes diverge from Session A spec | **Persists** — `Phili`, `Phile`, `1Jo`, `Jude` unchanged |
| `location` thin (~11%) | **Persists** — ~9% (97/1,036), now read-disambiguated and includes `spirit` |
| — | **New gap:** `mode` field documented in `meta` but populated nowhere (0 of 2,645) |

*All comparisons are like-for-like on the 1,036 focus-cluster terms, which are the same set the v1.0 "full" file held.*

---

## 1. What these files are now

Five batches (200/200/200/200/122 verses) aggregating to the same **922 verses**, but occurrences rise from 1,036 to **2,645**. The rise is structural, not new fear data: the layout is now a **verse-based fan-out** — each verse lists *every* inner-being term in it, with `focus_cluster=true` marking the M01 terms (1,036 of them, the original set) and the remaining 1,609 being co-terms.

The `meta` is now self-documenting: `what_this_is`, `structure`, `layout_fan_out`, `conventions`, a full `fields` dictionary, and a `provenance` note. Provenance is the key addition: **most fields are mechanical (01b v2), but `cause`, `location`, `divine_involvement`, `object_type`, and `valence` are read-resolved by a focused verse-read API pass.** That is exactly the set that was weakest in v1.0.

New term-level fields: `term.cluster` and `term.focus_cluster`. New lexical fields: `mode`, `valence`, `cause_clause`.

---

## 2. Observation — the read-resolved fields (focus terms, n=1,036)

**`cause`** (the v1.0 blind spot): resolved 179, absent/NONE 857, UNRESOLVED 0. Up from 12 resolved. `cause_clause` (mechanical "because/for" hint) is populated on 795 occurrences across all terms and is explicitly superseded by `cause` once read.

**`valence`** (new): present on 1,033 — neutral 542, righteous 195, forbidden 139, commanded 87, sinful 70. Fear is now morally framed per occurrence: *commanded* (fear of God enjoined), *forbidden* ("do not be afraid"), *righteous*, *sinful*, *neutral*.

**`object_type`** (read-classified): present 541 — God 174, person 140, situation 122, abstract 77, thing 13, spiritual-being 11, threat 4.

**`divine_involvement`** (now role): present 256 — object 165 (God as the object feared), agent 82 (God arousing/acting), giver 7, addressee 2.

**`location`**: present 97 — heart 58, soul 20, flesh 7, spirit 2, plus 10 multi-seat. Now includes `spirit` and read-disambiguation.

**`UNRESOLVED`** across all 2,645 terms is now genuinely rare: `type` 122 and `location` 60, both on co-terms; **0 on focus-term `cause`**.

---

## 3. Interpretation (held appropriately, now better grounded)

The provenance split changes how much weight the data can bear. In v1.0 the interpretive slots were mechanical fallbacks; the safe reading was "shape and vocabulary only." Now the five fields that carry the inner-being meaning — what arouses the state, where it is seated, how God stands to it, what it targets, and how it is morally framed — are read-resolved. The data can now support **graded** claims about fear's relational and moral structure, not merely its vocabulary, provided each claim is checked against the verse (the pass is described as high quality, but it remains an automated read).

The single most useful gain is `valence` paired with `object_type`: together they let the long-standing reverence-vs-dread question be drawn from the data rather than asserted — e.g. fear directed at God (object_type=God, 174) and fear that is *commanded* (87) or *righteous* (195) can be separated from fear that is *forbidden* (139) or *sinful* (70). I have not yet cross-tabulated these; that is the natural next analytical step and should be done verse-checked, not taken from the fields alone.

---

## 4. Reflection (consequences and affected perspectives)

- The reverence/dread distinction that different reading communities weight so differently is now **encoded** rather than collapsed. That is a real gain, but it also means an automated moral judgement (`valence`) now sits on each verse. Where a tradition would contest whether a given fear is "commanded" or merely "neutral," the field has already taken a position. The `valence` calls deserve spot-checking before they are built upon — an automated moral framing carries more interpretive freight than a mechanical part-of-speech tag.
- The fan-out makes **synergy analysis** possible without leaving the verse: a fear term's co-seated and partner terms are present as full records tagged with their own cluster (T2 qualifiers 478, then M23, M47, M05/love, M15/wisdom, M26/righteousness, M04/joy, and others). Fear's networked character is now first-class data.

---

## 5. Flags that persist or are new

**5.1 `anankē` (G0318) membership — persists, now better evidenced.** Still `focus_cluster=true` across its 9 occurrences, with senses "necessity / compulsion / under compulsion / hardships / affliction / distress" and `valence=neutral` throughout, `object_type` mostly absent or "abstract". The read pass now *confirms* these do not read as fear/dread/terror — yet the term remains a focus member. The improvement sharpens the evidence; the membership decision remains a researcher call.

**5.2 Book codes — persists.** Still `Phili`, `Phile`, `1Jo`, `Jude` (with OSIS ids alongside), diverging from the Session A v8 import spec (Php, Phm, 1Jn, Jud). Unchanged reconciliation risk if these references are ever joined to import-spec data.

**5.3 `mode` field — new gap.** Documented in `meta.fields` ("language · part-of-speech · (verb stem)") but populated on **0 of 2,645** occurrences. A documented-but-empty field.

**5.4 `faculty` — low discrimination, as before.** Affect on 973 focus terms; 56 informative blends (affect+perception/cognition/memory/volition); 7 absent (terms that are not themselves faculties, per the new convention). The signal remains in the blends.

**5.5 Co-term enrichment is light by design.** Of 1,609 co-terms, only 26 carry `valence`; the read pass concentrated on the focus cluster. Co-terms give structure (cluster, gloss, role) but not full interpretive depth — appropriate, but worth knowing before relying on co-term fields.

---

## 6. Open interpretive choices (carried forward, updated)

1. **Unit of analysis** — verse (922), focus term-occurrence (1,036), or now also the co-term layer (2,645 total)?
2. **Residual M-/T-cluster codes** — now first-class `term.cluster` values on co-terms. Honour as the co-occurrence map, or hold aside?
3. **`UNRESOLVED`** — largely answered by the new convention; remaining cases (type/location on co-terms) to treat as gaps.
4. **Task with this layer** — the read-resolved fields are strong enough to *read as-is for graded findings*, but `valence` in particular warrants verse-checked validation before publication-level claims.
5. **`anankē` and minority-sense members** — decide membership; the data now supports excluding the "necessity/compulsion" uses.

---

*End of v1.1.*
