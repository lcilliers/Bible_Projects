# M02 — evidence verification against the four `ve_lexical` extracts

**File:** `wa-m02-evidence-verification-v1_0-20260619.md` · **Date:** 2026-06-19
**Prefix:** WA · **Reference:** m02 · **Version:** v1_0 (first issue)
**Prior output:** `wa-m02-cluster-synthesis-bytier-v1_0-20260619.md` (2026-06-19, cluster synthesis by tier).

**Change-control note (v1_0):** first issue. Verifies the NEW per-characteristic syntheses and the standing flags against the four `wa-ve-lexical-extract-M02-20260619-b[1–4]of4.json` files now in hand.

**Method.** All four batches loaded and flattened (verse-based fan-out; the `focus_cluster` flag marks M02 terms). Group sizes use a lemma approximation of the c1–c7 split (burning-heat lemmas split into C1/C2 by the `divine_involvement` field), which is not identical to the read-resolved c1–c7 assignment in the source documents, so counts can differ by a few. No new evidence is introduced; this report only verifies and resolves.

---

## 1. Corpus and completeness — confirmed

The extract holds **634 verses**, **1683 total term-occurrences**, and **703 focus-cluster occurrences** across **47 distinct focus lemmas**. `tsur` (H6696B) accounts for 32 of these, so 671 + 32 = 703 — matching the NEW completeness statement (0 orphans). The completeness claim is sound.

## 2. Quantitative backbone — verified

Reproducing the NEW synthesis's two load-bearing tables from the extract:

**Faculty (F3).** C1 affect 221/221; C2 affect 142/142; **C6 affect 1, faculty-NONE 82/83**; **C7 faculty-NONE 4/4**. The F3 claim — C1–C5 are affects, C6 an external event, C7 a settled disposition — reproduces from the extract essentially exactly.

**Valence (F4).** By lemma-approx group: C7 sinful 3 / forbidden 1 (**exact**), C6 41/0/33/1 (**exact**), C4 28/24/16/5 (**exact**), C5 29/4/7/2 (**exact**); C2 ≈ 95/7/6 (findings 97/7/7); C1 ≈ 119/12/52/8 (findings 117/13/58/8); C3 dominant-sinful (50+). The small deltas are the lemma-approximation against the read-resolved assignment.

**Conclusion.** The per-characteristic syntheses are **well-grounded in the extract**. The "necessary evidence" the instruction asked about is present and accurate — a wholesale redraft of the characteristic files is **not** warranted for evidence-completeness. What the verification surfaces instead is one over-reading to close and two data issues to patch (below).

## 3. Flag resolutions

### F-A — Spirit-level seat (resolves L1 / S1): CLOSE as a correctly-dropped over-reading

The extract seats **0 of 703** occurrences in "spirit". The three verses the OLD findings used for spirit-level location are all present, but each carries `location = NONE`:

| Verse | Focus term | `location` | `faculty` |
|---|---|---|---|
| Eze 3:14 | che.mah | NONE | affect |
| Act 17:16 | paroxunō | NONE | affect |
| 1Sa 11:6 | cha.rah | NONE | affect |

Moreover the spirit-word (*ruach* / *pneuma*) is **not** captured as a compound partner of the anger term in any of the three (Eze 3:14 → *cha.zaq* "strengthen"; Act 17:16 → *kateidōlos* "idolatrous"; 1Sa 11:6 → *me.od* "much"). So the OLD spirit-seat reading attributed to the *anger term* a seat that, at the term level, belongs to a separate co-occurring word. The NEW position (no spirit-level seat) is the **term-level-correct** one per GR-PROG-007.

*Recommendation.* Accept the NEW position; treat the OLD spirit-seat finding as a verse-theme over-reading, not a loss. **Optional researcher judgement:** Eze 3:14 ("the heat of my spirit" — *che.mah* in construct with *ruach*) and Act 17:16 ("his spirit was provoked within him") are the two places where a *spirit co-seat* (a compound link, not a term-level seat) could legitimately be added; this would be a `compound`/`location` enrichment, not a change to the characteristic's seat profile. *(The synthesis-by-tier T2 section has been updated to this resolution.)*

### F-B — C2 divine-wrath "sinful" tags: EXPLAINED (data artefact) → patch candidate

Six divine-wrath occurrences (div = possessor/agent) carry `valence = sinful`. The verse evidence shows the sinful framing belongs to the **provoking human sin**, mis-attached to the wrath term:

| Verse | Term | div_role | Why "sinful" is mis-attached |
|---|---|---|---|
| Num 32:14 | cha.ron | possessor | "a brood of **sinful men**, to increase… the fierce anger of the LORD" |
| 2Ki 22:13 | che.mah | possessor | cause = "fathers **not obeying** the words of the book" |
| 2Ki 22:17 | che.mah | possessor | "because they have **forsaken me**… to provoke me to anger" |
| 2Ki 23:26 | cha.rah, cha.ron | agent/possessor | "because of all the **provocations** with which Manasseh had provoked him" |
| Job 42:7 | cha.rah | agent | "for you have **not spoken… what is right**" |

In each, the co-occurring C3 provoking term (*ka.as* / *ka.a.s*) is *correctly* sinful; the divine-wrath term should be **neutral** (or righteous). This is a valence-attribution artefact, not a claim that God's wrath is sinful. *(The findings cite 7; six are confirmed here — the exact set should be reconciled against the read c1–c7 assignment.)*

### F-C — C1/C2 boundary leak: CONFIRMED → patch candidate

| Verse | Term | `divine_involvement` | `experiencer` | Should be |
|---|---|---|---|---|
| Exo 4:14 | cha.rah | NONE | other | agent (God) → C2 |
| 2Ki 13:3 | cha.rah | NONE | other | agent (God) → C2 |

Both are explicitly "the anger of the LORD was kindled," yet `divine_involvement = NONE`, so under the bearer split they fall to C1 (human). Confirmed mis-resolution of the read field.

### F-D — C7 scope: CONFIRMED seed-limited (membership decision, not an evidence gap)

The only bitterness focus lemma in the extract is *pikria* (G4088, 4 occurrences). The OT *marah/mar* "bitterness of soul" field (Ruth 1:20; 1Sa 1:10; Job 7:11) is **absent** from the extract (the only *mar-* lemmas present are non-focus *mar.dut* H4780 "rebellion" and *mar.veh* H4766). So C7's evidence is **complete relative to its NT-only seed**; it cannot be "topped up" from this extract. Expanding C7 to the OT affliction-bitterness field is a **seed/registry membership decision** (researcher, with an M03-Grief cross-registry check), not an evidence omission.

### F-E — object_type under-population: CONFIRMED

`object_type` is NONE in **307** of 703 focus occurrences and populated in **396** (~44 % unpopulated). Any object-based signature for these characteristics remains provisional, as the findings noted (F10.2).

### F-F — C6 procedural senses: CONFIRMED

Of 83 C6 occurrences, roughly **29 are legal-procedural** (`sense` = cause 16, case 5, lawsuit 4, indictment 3, disputed cases 1). The GR-PROG-007 caveat — that the procedural strand is inner-being-peripheral and should be filtered at VC classification — is grounded; only the flesh-strife, cause-committing, and covenant-lawsuit strands engage the inner being.

---

## 4. CC patch candidates *(for researcher review per GR-PROC-004 — not applied)*

These touch the `ve_lexical` / measure layer, which is Claude Code's domain; the formal patch JSON is to be built per `wa-patch-instruction [current]` after researcher approval. Stated here as intended changes only.

1. **Valence re-tag (F-B)** — for the divine-wrath occurrences (div = possessor/agent) currently `valence = sinful`, re-read to `neutral` (or `righteous` where the text frames the wrath as just): Num 32:14 (cha.ron); 2Ki 22:13 (che.mah); 2Ki 22:17 (che.mah); 2Ki 23:26 (cha.rah, cha.ron); Job 42:7 (cha.rah). Rationale: the sinful framing belongs to the co-occurring provoking act, not the divine-wrath term. Confirm the exact set against the c1–c7 read-assignment first (findings cite 7).
2. **`divine_involvement` re-tag (F-C)** — Exo 4:14 and 2Ki 13:3: set `divine_involvement = agent` (God), re-resolve `experiencer`, and re-route the occurrence from C1 to C2. Rationale: both read "the anger of the LORD was kindled."

Both also bear on the F10.1 **circularity caution**: because the C1/C2 split rests on the read-resolved `divine_involvement` field, these corrections should be made by independent verse re-read, not by re-running the same read.

---

## 5. Outcome on "ensure the characteristic syntheses have the necessary evidence — redraft if needed"

The evidence **is present and verified** — the F3 and F4 backbones reproduce from the extract, and every standing flag now resolves. A redraft of the seven per-characteristic files is therefore **not** warranted for evidence-completeness. The warranted actions are narrow: close F-A as an over-reading (done in the synthesis-by-tier v1_1), and put the two data corrections (F-B, F-C) through the patch route for your review. C7's scope (F-D) is a membership decision awaiting your call; F-E and F-F are confirmed provisos already recorded in the findings' F10.
