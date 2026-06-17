# Review & validation — M01 Characteristic 1 (Reverent Fear) vs the VE items — v1 — 2026-06-16

**Prefix:** wa · **Document type:** Internal review (CC) · **Date:** 2026-06-16

**What this is.** A CC review of [WA-m01-c1-reverent-fear-v1.2-2026-06-16.md](../../Sessions-v2/M01-Fear/WA-m01-c1-reverent-fear-v1.2-2026-06-16.md) (the AI-Chat per-characteristic analysis) on two axes the researcher asked for:
1. **Validate the findings against the VE items** — recompute every count the doc cites against its stated data basis.
2. **Improve the VE items** — what the validation reveals about the `ve_lexical` generation (01b rules) that should change.

**Method.** Recomputed all counts directly from the doc's stated data basis — the five-file fan-out `wa-ve-lexical-extract-M01-20260616-b{1..5}of5.json` (922 verses, 1,036 M01 focus occurrences). Reverent-fear occurrence set = the doc's six anchor forms **H3372H · H3373 · H4172A · H4172B · H6345 · G6015 = 195 occurrences** (matches the doc). Scripts: `_tmp_validate_m01_c1.py`, `_tmp_validate_m01_c1b.py` (read-only; removed after run).

---

## 1. Verdict

**The findings are faithful to the data.** Of ~30 quantitative claims, **every aggregate is exact** against the extract — including the full §8.1 convergence test (195 / 123 / 81 / over-114 / miss-42, every sub-figure). This is a high-quality analysis: the numbers can be trusted and the template can propagate to Characteristics 2–11.

Three things to fix, in priority order:
- **One internal arithmetic inconsistency** in the doc (T1 H4172 count) — cosmetic, fix in the doc.
- **One VE generation rule-gap the data actively contradicts** — the C-5 giver↔origin pairing (I2 below) — fix in the generator.
- **Two VE precision issues** the analysis had to work around — multi-value duplication (I1) and determiner-leak in `object` (I3).

---

## 2. Validation table (doc claim → data → verdict)

| Doc location | Claim | Data | Verdict |
|---|---|---|---|
| T1 Kind | faculty=affect on **all 195** | affect=195 | ✅ exact |
| T1 Kind | object_type=God on **95 of 122** named | God=95; present=122 (absent=73) | ✅ exact |
| T1 Kind | divine_involvement=object **98** | object=98 | ✅ exact |
| T1 Kind | valence righteous **104** / commanded **46** = 77% | 104 / 46; (150/195)=76.9% | ✅ exact |
| T1 Kind | type quality **48** / action **123** | action=123, quality=48 (status=24) | ✅ exact |
| T1 Boundary | forbidden **4**, sinful **10** | forbidden=4, sinful=10 | ✅ exact |
| T2 | location absent **181 of 195** | absent=181 | ✅ exact |
| T2 | heart **9**, soul **3** + 2 blends (heart+soul; triple-heart) | raw heart=13, soul=4; reconciles to 9 single-heart + 3 single-soul + 1 heart+soul + 1 triple-heart | ✅ reconciles (see I1) |
| T3 | faculty=affect all 195, no blends | affect=195, no other faculty value | ✅ exact |
| T5 | object Lord **37** / God **17** / name **5** | 37 / 17 / 5 | ✅ exact |
| T5 | divine_involvement object **98** (agent only **4**) | object=98, agent=4 (**giver=2 also present**) | ⚠ exact but incomplete (I6) |
| T5 | object_type=person **21** | person=21 | ✅ exact |
| T5 | spiritual-being = "other gods", all condemned (Judg 6:10 forbidden; 2Ki 17:7 sinful) | spiritual-being=2: Judg 6:10 forbidden, 2Ki 17:7 sinful | ✅ exact |
| T6/T8 | type quality 48; OT-weighted 194/195; 1 Greek | quality=48; Hebrew=194, Greek (G6015)=1 | ✅ exact |
| §8.1 | lemma-anchor **195** | 195 | ✅ exact |
| §8.1 | field-defined (object=God ∧ valence∈{righteous,commanded}) **123** | 123 | ✅ exact |
| §8.1 | overlap **81** | 81 | ✅ exact |
| §8.1 | over-includes **114** = neutral 31 / righteous-not-God 55 / commanded-not-God 14 / sinful 10 / forbidden 4 | 31 / 55 / 14 / 10 / 4 = 114 | ✅ exact |
| §8.1 | misses **42**, incl. all 10 Greek (G5399 8, G5401 2), H3372G 10 | 42; Greek 10 (G5399=8, G5401=2); H3372G=10 | ✅ exact |

---

## 3. The one internal inconsistency (fix in the doc)

**T1 "Name" line sums to 184, not 195.** As written: H3372H 107 + H3373 64 + H4172 (A/B, **11**) + H6345 1 + G6015 1 = **184**. The data shows H4172**A** = 11 *and* H4172**B** = 11 (separate forms) = **22**. The correct sum is 107 + 64 + **22** + 1 + 1 = **195**.

The doc is *right* downstream — T8.1 says "Both are counted — distinct occurrences = 195," and "six anchor terms" only works if A and B count separately. The slip is local to the T1 enumeration, which conflates **11 shared verse references** with **occurrences**. Fix: render it "H4172A/B (11 references each = 22 occurrences)". No recomputation needed — the 195-based aggregates are all correct.

---

## 4. VE-item improvement opportunities (the substantive output)

These are what the validation surfaces about `ve_lexical` generation (01b v2 rules). I1–I3 are concrete generator fixes; I4 confirms an open issue; I5–I6 are consumption notes.

### I1 — Multi-value fields don't de-duplicate identical values *(generator fix)*
`Deu 20:8` (H3373) carries `location = ['heart','heart','heart']` — the "triple-heart" the analyst had to explain. The verse has three heart-seat terms (*levav*); each emitted a value and identical values were not collapsed. Per **P3** (one simple value; multiples = rows) and the seat being a *set*, one occurrence should carry `location=heart` **once**. **Fix:** dedupe identical values within an occurrence's multi-list at generation. **Impact:** corrects raw heart 13→11; removes an artefact every future analyst would otherwise re-derive and footnote.

### I2 — The C-5 giver↔origin pairing is not enforced *(generator fix — the data contradicts the rule)*
`Deu 11:25` (H4172A and H4172B) has `divine_involvement = giver` but `origin = None`. 01b §4a item 6 *states* the rule — "'From God' = `received-from-outside` + God's-role=`giver-source`" — and §3 resolves divine-involvement (item 8) **before** origin (item 6), so origin can read it. It isn't applied: only 2 rows carry `origin=received-from-outside`, and **neither is a giver case**. **Fix:** in the origin rule, `if item8 == giver-source → origin = received-from-outside`. This is the **one place the doc's data actively contradicts the settled rules** — worth doing before the pattern propagates.

### I3 — `object` (N1) captures determiners/quantifiers, inflating "named objects" *(generator fix)*
Among the 122 "named" objects: `object` = **"all" 5, "your" 4, "the" 2, "every" 2, "sight" 2**. "all/every/your/the" are determiners/quantifiers, not targets — "all/every" (*kol*) belong to **N4 intensity**, the bare article/possessive is parse noise. N1 should resolve to the **governed head noun**. **Impact:** the denominator in "God on 95 of 122 named" is inflated by non-objects; cleaning N1 sharpens object_type and the §8.1 field-test (which keys on object=God).

### I4 — Sense cannot separate the two H3372 sub-entries — confirms D-C / A7 *(known issue, now confirmed on the scoping-critical term)*
H3372**G** "to fear: revere" (194, the *danger* sense) and H3372**H** "to fear: revere" (107, the *reverence* sense) carry the **identical gloss** — only the Strong's sub-suffix separates them, and §8.1 shows **10 H3372G occurrences are actually reverent-of-God**. The uniform gloss means the **sense field cannot carry the G/H distinction**, so any lemma/sub-entry-anchored scope (like Characteristic 1's) misclassifies ~10+ occurrences. This is the open **A7/D-C uniform-gloss issue** ([wa-ve-iteration2-action-register-20260615.md](wa-ve-iteration2-action-register-20260615.md)), now demonstrated on the term that governs the scope decision. It strengthens the doc's own §8.1 conclusion — **valence is the better discriminator than lemma**.

### I5 — `faculty` is structurally uniform for single-faculty clusters *(design note)*
faculty=affect on all 195 because the rule is **term-intrinsic only (R1)** and every anchor term is an affect-lemma. The further faculties reverence engages (volition / moral-evaluation, via the obedience/serving co-terms) appear only as T7 co-occurrence. **R2** (a co-occurring faculty-lemma relates to the term → assign) *could* capture them but is effectively parked. Not an error — but for clusters whose terms share one lemma-faculty, the field adds nothing until R2 co-term faculty assignment is enabled. Flag for when T7 opens.

### I6 — `divine_involvement = giver` (2) dropped from the T5 framing *(consumption note)*
T5 reads "object 98 (agent only 4)" and concludes "Direction is human → God, not God → human." True for 98/100 divine rows — but the **2 `giver` rows (Deu 11:25)** are the opposite direction: God *lays* "the fear of you" on the nations (God → human, fear *of Israel*). The value space already distinguishes this; the analysis flattened it. Minor, but the template should surface `giver` as a small counter-direction rather than collapse divine roles to object/agent.

---

## 5. Bottom line for the scope decision (§8.1)

The validation **independently confirms** the doc's recommendation. The lemma anchor is leaky in both directions — it over-includes 114 non-reverent occurrences and misses 42 reverent ones (incl. all 10 Greek) — and I4 shows *why*: the anchoring term (H3372) can't be sense-split, so lemma membership ≠ reverence. **`valence` (righteous/commanded) generalises across all terms and both Testaments; `object`=God qualifies rather than gates.** The data supports adopting valence as the discriminator. (Decision remains the researcher's.)

---

*Source data: the five-file M01 extract (the doc's stated basis). The extract was built today from `ve_lexical` by `scripts/build_ve_lexical_extract.py`; DB-vs-extract parity was not separately re-verified here — a cheap follow-up if desired.*
