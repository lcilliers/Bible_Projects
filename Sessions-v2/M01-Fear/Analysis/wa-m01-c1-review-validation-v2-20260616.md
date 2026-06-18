# Review, validation & insight-coverage audit — M01 Characteristic 1 (Reverent Fear) vs the VE items — v2 — 2026-06-16

**Prefix:** wa · **Document type:** Internal review (CC) · **Date:** 2026-06-16
**Supersedes:** `wa-m01-c1-review-validation-v1-20260616.md` (in `archive/`). v2 adds **Part B — the insight-coverage audit** (the substantive part): does the analysis comment on *every* aspect the lexical features can yield, or only the ones it happened to use? v1 was the statistical validation only.

**What this reviews.** [WA-m01-c1-reverent-fear-v1.2-2026-06-16.md](../../Sessions-v2/M01-Fear/WA-m01-c1-reverent-fear-v1.2-2026-06-16.md) — the AI-Chat per-characteristic analysis. Data basis = the doc's stated source, the five-file fan-out `wa-ve-lexical-extract-M01-20260616-b{1..5}of5.json` (195 reverent-fear occurrences: H3372H · H3373 · H4172A · H4172B · H6345 · G6015).

---

## 1. Verdict (two parts)

**Part A — the numbers are faithful.** Every aggregate the doc cites is exact against the data, including the whole §8.1 convergence test. (Detail in Part A below.)

**Part B — but the insight coverage is partial.** The analysis mines **~9 of the 17 derivable lexical fields well, and leaves 8 fields carrying real insight under-mined or untouched** — including the **single richest field, `compound` (filled 170/195 = 87%)**, which it parked wholesale under T7, and **`immediate_response`** (the behavioural fruit of fear — Abraham withholding his son, Sabbath-keeping, law-walking, joy), which it treated as excluded but which is populated. This is the gap you flagged: the review must be about *what insight is hidden in the lexical*, not whether the counts are right.

The verse-read fields (cause, location, object_type, divine_involvement, valence) were the focus; the **mechanical relational/structural fields** (compound, how, experiencer, intensity, mode, origin, response) were the blind spot.

---

## PART A — Statistical validation (carried from v1, condensed)

All counts recomputed from the extract; **all exact**:

| Claim | Data | |
|---|---|---|
| faculty=affect all 195 · type action 123/quality 48 · valence righteous 104/commanded 46/sinful 10/forbidden 4 | matches | ✅ |
| object_type=God 95 of 122 named · object Lord 37/God 17/name 5 · divine_involvement object 98/agent 4 | matches | ✅ |
| location absent 181; spiritual-being Judg 6:10(forbidden), 2Ki 17:7(sinful) | matches | ✅ |
| §8.1 lemma-anchor 195 / field-defined 123 / overlap 81 / over-114 (31/55/14/10/4) / miss-42 (Greek 10, H3372G 10) | matches | ✅ |

**One internal slip (fix in the doc):** T1's "Name" line sums to 184, not 195 — it writes H4172 "(A/B, 11)" but A=11 *and* B=11 = **22**; correct sum 107+64+**22**+1+1=195. T8.1 is right ("both counted = 195"); only the T1 enumeration conflates *11 references* with *occurrences*.

---

## PART B — Insight-coverage audit (the substantive review)

For each lexical field: how much it carries for reverent-fear, whether the doc mined it, and the insight left on the table.

| VE field | fill (of 195) | did the doc mine it? | insight status |
|---|---|---|---|
| sense (1) | 195 | ✅ T1 (root range) | mined |
| type (2) | 195 | ✅ T1/T6 | mined |
| valence | 195 | ✅ T1 (the spine of its argument) | mined |
| object / object_type (N1) | 122 | ✅ T5 | mined |
| divine_involvement (8) | 104 | ⚠ T5 (object/agent only) | **missed `giver`=2 → the God→human direction** |
| cause (N2) | 24 | ✅ T5 (good — surfaced examples) | mined |
| location (5) | 14 | ✅ T2 | mined |
| faculty (7) | 195 | ⚠ T3 (term-intrinsic only) | **uniform affect; the cognition/volition it engages is in `compound`, not read** |
| **compound (3)** | **170 (87%)** | ❌ **parked (T7)** | **the richest field — entire synergy web unmined (see B1)** |
| **immediate_response (11)** | **19** | ❌ assumed excluded | **the behavioural fruit of fear unmined (see B2)** |
| **experiencer** | **99** | ❌ named once, no distribution | **the commanded-to-others stance unmined (see B3)** |
| **mode / morph (4)** | 195 | ❌ not listed at all | **the Niphal "to-be-feared/awesome" group + imperatives unmined (see B4)** |
| intensity (N4) | 35 | ⚠ T6 (durative only) | **partial — the *kol* "all/totality" frame under-read (see B5)** |
| how (N3) | 52 | ❌ not mentioned | **the predicates fear is enacted through unmined (see B6)** |
| origin (6) | 2 | ❌ not mentioned | **near-silent — but the silence is itself a finding (see B7)** |
| relational (13) | 16 | ⚠ T5 borrows the *name* | the `relational` field itself (incl. "above all gods") not cited |
| purpose (9) / typology (10) | — | n/a | **excluded from VE generation by design** (01b §4d — no lexical basis); the doc should *say* so |

### B1 — `compound`: the synergy web (87% filled, entirely parked) — the biggest miss
The compound field already states each co-term **with its role** (partner / qualifier / co-seated). Across the 195 it resolves into clear **nexuses** — this is precisely the "insight hidden in the lexical":

- **Obedience / service nexus** — *sha.mar* "to keep:obey" (13) + *sha.ma* "to hear:obey" (5) + *a.vad* "to serve" (9) = **27 occurrences** pair reverent fear, *as a partner term*, with obeying/serving. **Finding the lexicon yields directly: reverent fear is the disposition that issues in obedience and service** — not parked T7 speculation, a counted partner relation.
- **Covenant / oath / faithfulness** — *be.rit* "covenant" (10) + *sha.va* "to swear" (5) + *e.met* "faithfulness" (4) + *che.sed* "kindness" (4): fear sits inside the covenantal frame.
- **God's manifest power & name** — *shem* "name" (17) + *yad/ze.ro.a* "hand/arm: power" (11+5) + *ka.vod* "glory" (5): the arouser/object is God's *self-revelation*, qualifier-role.
- **Cognition / memory** — *ya.da* "to know" (7) + *za.khar* "to remember" (4): **this answers T3's open question** — the doc said fear engages "neither cognition nor volition," but the compound web shows fear co-operating with *knowing* and *remembering* at the verse level (7+4 partner relations). The faculty *field* is term-intrinsic-uniform; the faculty *insight* is in compound.
- **Life / blessing / duration** — *chay.yim* "life" (7) + *a.rakh* "to prolong" (4): reverent fear linked to long life.

The doc parked **all** of this because "T7 is held silent." But T7-silence is about not advancing *structural findings*; it is not a licence to leave the **compound field uncommented**. The single most information-rich VE feature for this characteristic produced **zero analysis**.

### B2 — `immediate_response`: the behavioural fruit (populated, assumed absent)
19 occurrences carry the inner being's enacted response — and they are theologically central: **Gen 22:12 "withheld [his] son"** (Abraham), **Lev 19:3 keep Sabbaths**, **Deu 6:2 keeping all [commandments]**, **Jer 44:10 walked [in the] law**, **2Ch 6:33 built [for the] name**, **Psa 65:8 joy**. The doc's T6 (Formative/Developmental) called itself "near-silent" and the framework-fit map omits response/effect entirely — yet here is the **fruit of reverent fear in 19 verses**: obedience, covenant-keeping, worship, even joy. (Note: this also corrects the action-register assumption D-D that VE9–12 were excluded — `immediate_response` is live.)

### B3 — `experiencer`: the rhetorical stance (99 filled, no distribution given)
**other 52 · other-addressed 40 · self 7.** Reverent fear is overwhelmingly **enjoined on a second party** (40 *addressed* = "you shall fear") and **almost never first-person experience** (7 self). This is a real characterisation: reverent fear is **commanded and addressed, not introspected** — it corroborates the high `commanded` valence from the *experiencer* axis. The doc mentions experiencer in passing (the framework-fit map) but never reports the distribution or draws the insight.

### B4 — `mode` / morph: the Niphal "awesome" group + imperatives (untouched)
Stem split: **Qal 92 · Niphal 31** (plus 72 non-verb). The **31 Niphal** occurrences are the *nora* "to-be-feared / awesome" form — God as the **object/quality** of fear ("the great and *awesome* God"), grammatically distinct from active Qal "you fear." And among the Qal are the **2mp imperatives** (HVqi2mp, 8) — the grammatical home of the *commanded* valence. Mode is a bedrock field (01b stratum 1) and the doc does not list it at all, missing a clean grammatical-semantic axis: **active fearing (Qal) vs. God-is-fearsome (Niphal) vs. commanded fearing (imperative).**

### B5 — `intensity`: the totality frame (partial)
35 filled, dominated by ***kol* "all" (23)** + "very/greatly" (4) + "forever/always" (durative). The doc read the *durative* tokens (T6 "all your days") but not the **totality** reading: "all your heart," "all the days," "all peoples/nations" — reverent fear is framed in terms of *wholeness/universality*, not just duration.

### B6 — `how`: the predicates fear is enacted through (untouched)
52 occurrences carry a governing predicate — *did/do* (H6213, 4), *lay* (H5414), *bless* (H1288), *make holy* (H6942), *bring*. For the noun-form occurrences this shows fear is **enacted ("do the fear"), bestowed ("lay the fear"), and tied to blessing/sanctification verbs.** Thin but real, and uncommented.

### B7 — `origin`: a meaningful silence (untouched)
Only **2/195** filled. Per the framework's own instruction (*note the silence rather than fill it*), this deserves a sentence: **the lexicon does not state where reverent fear originates** — and the 2 it does (Deu 11:25, God *lays* it) tie to the I2 generator gap (giver↔origin pairing, Part C). The doc lists origin under T5 carrying-fields but never discusses it.

---

## PART C — VE-item improvement opportunities

Carried from v1 (I1–I6) plus new ones (I7–I9) surfaced by the coverage audit.

**Generator fixes (the data needs these):**
- **I1 — multi-value de-dup.** `Deu 20:8` location=['heart','heart','heart'] (the "triple-heart"); collapse identical values (P3). Raw heart 13→11.
- **I2 — enforce C-5 giver↔origin.** `Deu 11:25` has divine_involvement=`giver` but origin=`None`; 01b §4a item 6 *states* "from God = received-from-outside + giver-source." The one rule the data actively contradicts.
- **I3 — N1 object precision.** "all/your/the/every" leak into `object` (should be N4 intensity or dropped). Inflates the "122 named" denominator.

**Known issue confirmed:**
- **I4 — uniform gloss can't split H3372G/H.** Both glossed "to fear: revere"; §8.1 shows 10 "danger" H3372G occurrences are reverent. Confirms A7/D-C on the scope-critical term → **valence is the right discriminator** (§8.1 verdict validated).

**Surfaced by the coverage audit (new):**
- **I7 — `compound` needs to be a first-class analytical output, not parked.** The richest field (87% filled, role-typed) carries the synergy web (obedience/covenant/cognition nexuses, B1). Recommend: even while T7 *findings* are held, the **compound field must be reported per characteristic** — it is the mechanical evidence for which other characteristics this one operates with. This is the C-4/C-6 "compound may grow into its own VE" flag, now urgent.
- **I8 — `faculty` (term-intrinsic) and `compound` (co-term faculties) should be read together.** Faculty=affect-uniform understates the characteristic; the cognition/volition it engages is in compound (B1). Either enable faculty R2 (co-occurring faculty-lemma → assign) or have the analysis template always cross-read compound for faculty co-terms.
- **I9 — `immediate_response`/`produces_effect` are live and must be in the template.** B2 shows real behavioural fruit; the analysis framework-fit map omitted them. Add a tier slot (these feed T6 formative + T5 outworking).

---

## PART D — Recommendation for the analysis & the template

The v1.2 doc is **accurate but under-reads its own data.** Before it becomes the template for Characteristics 2–11, the template should require a **field-completeness pass**: every VE field gets at least a sentence — *value(s) or a noted silence* — so no field with insight is silently dropped. Specifically the next revision of M01-c1 should add:
1. A **compound/synergy section** (B1) — the obedience, covenant, power-name, cognition, and life nexuses.
2. The **behavioural fruit** from `immediate_response` (B2) into T6.
3. The **experiencer stance** (B3 — commanded/addressed, not introspected).
4. The **mode axis** (B4 — Qal/Niphal/imperative).
5. A line each on **intensity-totality (B5), how (B6), origin-silence (B7)**.
6. A note that **purpose/typology are excluded by design** (not "silent" — *not lexically derivable*).

This turns the analysis from a statistics-of-nine-fields exercise into the full lexical read you're after.

---

*Recompute scripts were throwaway (`_tmp_*`, removed). The extract is the doc's stated basis; DB-vs-extract parity not separately re-verified (cheap follow-up if wanted).*
