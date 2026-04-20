# WA Dimension Review Observations Log — C01

| Field | Value |
|---|---|
| Filename | wa-dim-c01-observations-v1_0-20260420.md |
| Governing instruction | wa-dimensionreview-instruction-v3_3-20260418.md |
| Mode | Registry Mode — target registries: Reg 112 (mind), Reg 183 (heart) |
| Cluster extract | wa-dim-C01-extract-2026-04-20.json (275 groups, 6 registries) |
| Root family extract | wa-dim-C01-rootfamily-2026-04-20.json (61 roots, 5 cross-registry flagged) |
| Existing pointers extract | wa-dim-C01-existing-pointers-2026-04-20.json (29 Session B findings, 37 Session D pointers) |
| Session date | 2026-04-20 |
| Session scope | Phase A only — full cluster coherence assessment |
| Researcher direction | Phase B scope narrowed to r112 + r183 only (explicit override of instruction §2.2). Recorded as `[INSTRUCTION-NOTE]` below. |

---

## Previous output reference

No prior observations log for C01 under v3_3. First session. Previous work on C01 registries (r182 Soul, r184 spirit, r185 flesh, r211 being reaching `dim_review_status = Complete`) was performed under earlier instruction versions — historical artefacts, not available to this session.

---

## [INSTRUCTION-NOTE] 2026-04-20 — Flags file not provided at session start

OBSERVATION: GR-LOAD-001 requires the global flags file (`wa-global-flags-v[version]-[date].md`) to be loaded immediately after the global rules file. The flags file was not uploaded to this session. Claude AI cannot load a file not provided.

PROPOSED CHANGE: None to the instruction. This is a session-start procedural note. Researcher may supply the flags file at the start of the next C01 session.

ACTION: Flagged. Proceeding without flags-file context for this Phase A session. Any pointer numbering decisions in later phases will need the flags file to confirm programme-wide `finding_id` / `flag_label` uniqueness (DR-9).

---

## [INSTRUCTION-NOTE] 2026-04-20 — Handoff override of §2.2 Phase B scope

OBSERVATION: CC handoff document `wa-dim-C01-handoff-kickoff-v1-20260420.md` §3 directs Phase B quality sweep to "review targets only: r112, r183". Instruction §2.2 (Registry Mode) requires Phase B to span the full cluster regardless of target scope, with the explicit rationale that QA-TERMCENTRIC screening needs cluster context. Researcher confirmed 2026-04-20 that the handoff governs — Phase B narrows to r112 + r183 only.

CONSEQUENCE: Phase B will not produce QA findings on the four already-Complete registries (r182, r184, r185, r211). Phase A coherence assessment (this entry) reads all six registries, but subsequent Phase B and Phase C will not. Coherence observations on the four non-target registries are captured here for the record only — they do not convert into patch operations this cycle.

PROPOSED CHANGE: Not for this instruction. This is a researcher-directed operational override specific to C01's mixed-vintage state. If similar overrides recur, §2.2 may warrant amendment language ("unless the full cluster has already been reviewed under a prior version and researcher has narrowed scope") — but this is a judgement for a later review cycle.

ACTION: Flagged. Phase A observations record the full-cluster reading; Phase B scope is narrowed per researcher direction.

---

## [PHASE-A] C01 | 2026-04-20

### Excluded registries (Analysis Complete)

None. No C01 registry carries `session_b_status = "Analysis Complete"`. All six registries are non-excluded and reached `verse_context_status = Complete`. Four registries already carry `dim_review_status = Complete` from prior review cycles under earlier instruction versions; these are informational for Phase A and out-of-scope for Phase B/C per researcher direction.

### Active registries

| Reg | Word | Groups | DR status | MO locked | MO open | dimension_confidence snapshot |
|---:|---|---:|---|---:|---:|---|
| 112 | mind | 73 | NULL → target | 71 | 2 | 71 CLAUDE_AI, 2 KEYWORD_WEAK |
| 182 | Soul | 61 | Complete (prior) | 61 | 0 | 61 CLAUDE_AI |
| 183 | heart | 59 | NULL → target | 51 | 8 | 51 CLAUDE_AI, 4 KEYWORD_WEAK, 3 KEYWORD_STRONG, 1 UNCLASSIFIED |
| 184 | spirit | 37 | Complete (prior) | 37 | 0 | 37 CLAUDE_AI |
| 185 | flesh | 30 | Complete (prior) | 30 | 0 | 30 CLAUDE_AI |
| 211 | being | 15 | Complete (prior) | 15 | 0 | 15 CLAUDE_AI |
| **Total** | | **275** | | **265** | **10** | — |

Target-registry active group count: **132** (73 + 59).
All 275 groups carry `dominant_subject = null` (Python None). No literal `'NONE'` strings observed — C01 has no OT-DBR-012 remediation to perform.

### Coherence assessment

**The thematic anchor holds.** C01 gathers the six core inner-being nouns that scripture uses to name the human interior: mind, Soul, heart, spirit, flesh, being. These are the vocabulary out of which every other registry's analytical frame is built. A cluster containing these six has self-evident coherence: they are the inner being, directly named. No registry in C01 looks misplaced on the face of the data. The coherence of C01 is structural — it is the reference cluster for the programme's governing question (GR-PROG-002: the characterisation of the human inner being).

**What this means for dimension assignment.** Because the C01 terms are the inner-being words themselves (not property terms expressing an aspect of inner being), each group in this cluster typically engages one of the widest-possible dimension ranges. `lev` alone covers at least cognition, volition, moral character, emotion, relational disposition, and God-ward orientation across its sense-splits. `ne.phesh` does the same. This is the pattern you would expect: a characteristic term that *is* the inner being will show dimensional breadth across its corpus because the inner being itself engages every dimension. This observation has implications for Session D (below).

**Cluster size is healthy.** Six registries is within §5.3 norms (4–13 active words). No size-driven reassignment pressure.

### Boundary observations

**None on registry placement.** No registry in C01 looks like it belongs in another cluster. The six terms share the strongest possible inner-being affinity: they are the inner being.

**Description-style heterogeneity is visible.** Reading across the six registries, `context_description` prose style and length vary materially. Reg 185 (flesh) contains some very short, term-prefix descriptions (e.g., *"Ya.tsa as expression of inner states going outward"*, *"Be.shar as site of the covenant sign: circumcision"*) that read as abbreviated and term-centric. Reg 184 (spirit) and Reg 182 (Soul) carry longer descriptions more consistently starting with *"Term names…"*. This is not a Phase A reassignment issue — it is a heterogeneity of vintage and scribal convention across registries reviewed at different times under different versions. It is noted here because any Phase A coherence claim about what the cluster "shows" must acknowledge that the descriptions themselves are not uniformly written. **This constrains cross-cluster claims later.**

**Every description I sampled across all six registries identifies an inner-being engagement.** I did not encounter a description that was purely external-circumstance or purely lexical. The Phase B.5 QA-TERMCENTRIC risk in r112 and r183 (when we reach it) is about descriptions that name *what the term does* rather than *what inner-being characteristic the term serves* — not about descriptions that fail to engage the inner being at all. This is a different problem grade than would apply to externalised descriptions.

### Cross-registry root families

The root family extract reports 5 cross-registry roots. On inspection, the signal breaks into two categories:

**Genuine cross-registry roots (2):**

- **CHASHAV** (Hebrew, "invention") — 7 terms, 12 groups, spans Reg 112 (mind), Reg 126 (purpose), Reg 160 (thought). Core verbal meaning across all three is devising/thinking/counting as inner planning. The root runs through mind (as the faculty), purpose (as the product), and thought (as the act). **This is analytically significant.** When we assign dimensions to the r112 groups derived from this root, the assignments should be comparable to (not necessarily identical to) those in r126 and r160, and divergence will be informative rather than alarming.

- **BOUL** (Greek, "plan") — 5 terms, 7 groups, spans Reg 32 (counsel) and Reg 112 (mind). `bouleuō` ("to plan") lives in mind; the nouns `boulē`, `epiboulē`, `sumboulion`, `sumboulos` live in counsel. The verb-in-mind / noun-in-counsel pattern is exactly the kind of root-family structure the programme would expect: the *act* of planning belongs to the mind faculty, the *plan* belongs to the relational/advisory vocabulary. The dimensional assignment on `bouleuō` in r112 should sit near Volition or Cognition; the boulē-family terms in r32 should sit near Relational Disposition or Cognition depending on verse context. The structural pattern is worth recording as a Session D candidate.

**Likely false-positive cross-registry roots (3):**

- **AT** (root_language: None, root_gloss: None) — lists personal-pronoun forms (`antah`, `att`, `attem`, `atten`) in Reg 156 (surrender) with `it.ti` ("mutterer") in Reg 184 (spirit). The pronouns and the mutterer term do not share a morphologically real root; they appear to be grouped by a spurious string-match on the consonantal skeleton. Not analytically meaningful.
- **YATSA** (root_language: None, root_gloss: None) — links `tse.e.tsa` ("offspring") in Reg 156 (surrender) with `ya.tsa` ("to come out") in Reg 185 (flesh). Lexically these *do* share the root yts', but the sense-distance between "offspring" and "come out" makes the root-family link analytically thin for Dimension Review purposes. Possibly a grouping worth noting for Session D but not a strong cross-registry signal.
- **TAAM** (Hebrew, "delicacy") — links `ta.am` ("to perceive") in Reg 49 (discernment) with `ta.am` ("be double") in Reg 211 (being), plus `mat.am` ("delicacy") in Reg 49. The perceive/double pair is a genuine homonym coincidence; the root-family linkage is string-match rather than semantic. The delicacy/perceive pair inside r49 is real; the cross-registry link via "be double" is not.

**Consequence for Phase C Session D pointer candidates:** Two strong cross-registry pointers (CHASHAV, BOUL) are worth formalising when we reach Phase C for r112. These are candidates for Session D pointer capture per §7.5 and the handoff §4.2. The three weak cross-registry roots are not candidates and should be noted as false-positive signals rather than suppressed (the CC extract tool may want to know it over-reports).

### Dimension vocabulary vintage

The single most consequential Phase A observation concerns dimension labels. Of 275 groups:

- **265** carry labels from a legacy vocabulary: `Moral/Conscience`, `Theological/Divine-Human`, `Affective/Emotional`, `Spiritual/God-ward`, `Cognitive/Mind`, `Character/Disposition`, `Volitional/Will`, `Volitional/Capacity`, `Relational/Social`, `Identity/Selfhood`, `Somatic/Embodied`. These labels do not appear in the current §7.7 vocabulary.
- **10** carry labels from the current §7.7 vocabulary (`Cognition`, `Moral Character`, `Volition`, `Emotion — Positive`, `Relational Disposition`) — and these 10 are exactly the 10 groups at `manual_override = 0`. All 10 sit in the target registries (2 in r112, 8 in r183).

The pattern is consistent: **anchored groups carry legacy labels; unanchored groups carry current labels.** The legacy vocabulary was the working vocabulary at the time these registries were reviewed and anchored; the current vocabulary has been refined since. No group in C01 has yet been reviewed under the current §7.7 vocabulary and anchored.

**Mapping from legacy to current vocabulary is not one-to-one.** On first reading:

| Legacy label | Group count | Apparent mapping to current §7.7 | Reliability |
|---|---:|---|---|
| Moral/Conscience | 57 | 05 Moral Character (majority) or 03 Cognition (if conscience-as-awareness) | ambiguous |
| Theological/Divine-Human | 55 | 11 Divine-Human Correspondence | probable |
| Affective/Emotional | 37 | 01 Emotion — Positive or 02 Emotion — Negative (split needed per group) | requires per-group judgement |
| Spiritual/God-ward | 25 | No direct counterpart; closest is 11 Divine-Human Correspondence or 10 Dependence / Creatureliness | no clean mapping |
| Cognitive/Mind | 23 | 03 Cognition | probable |
| Character/Disposition | 17 | 05 Moral Character or 06 Relational Disposition | ambiguous |
| Volitional/Will | 15 | 04 Volition | probable |
| Relational/Social | 14 | 06 Relational Disposition | probable |
| Identity/Selfhood | 9 | No direct counterpart; candidate for a new dimension or distributed across existing | no clean mapping |
| Volitional/Capacity | 7 | 09 Agency / Power | probable |
| Somatic/Embodied | 6 | No direct counterpart; possibly 07 Vitality / Existence | no clean mapping |

**The three legacy labels with no clean mapping — `Spiritual/God-ward` (25 groups), `Identity/Selfhood` (9 groups), `Somatic/Embodied` (6 groups) — are analytically significant.** They may represent either (a) legacy labels that map unevenly across current dimensions on a per-group basis, or (b) genuine inner-being characteristics that the current vocabulary does not capture and that may warrant new dimension candidates raised as Session D pointers per handoff §4.4.

The current vocabulary already added Dimension 11 (Divine-Human Correspondence) from C18 data (§3.3 note: *"Dimension 11 added from C18 data at v1.6"*), so the vocabulary is understood to be iterative. C01 is the cluster most likely to surface further candidates, precisely because it contains the inner-being nouns themselves.

**Consequence for Phase B/C on target registries:** When we review r112 and r183 groups, where a group appears to require `Spiritual/God-ward`, `Identity/Selfhood`, or `Somatic/Embodied`, the correct action per §7.3 Rule 3 is to name what the group shows in plain language and present to the researcher for decision — not to force-fit into an existing dimension. These may be legitimate Session D candidate dimensions.

### Cross-registry coherence reflection

**This cluster is analytically a mixed-vintage dataset.** Four of six registries were reviewed and anchored under a prior vocabulary; two are unreviewed. Any Phase A claim about what C01 "shows" at the dimension level is necessarily a claim mixing two analytical models. The instruction's §2.2 Registry Mode rationale for full-cluster Phase B ("a group that looks term-centric in isolation may be interpretable when adjacent groups are seen") is partly defeated here: adjacent groups are from a different-vintage analysis. This supports rather than undermines the researcher's direction to narrow Phase B to the two targets — running QA-TERMCENTRIC screening on the four legacy registries would risk producing findings that are artefacts of vocabulary evolution rather than genuine quality problems.

**What the full-cluster read still contributes:** verse-level context, term-range orientation, and recognition of where the target registries' dimension assignments will need to *relate coherently* to already-anchored groups in the other four registries — even when the other four are tagged with legacy labels. When in Phase C we assign a current §7.7 dimension to an r112 group, we will often be able to see (from the legacy-tagged neighbours in r182, r184, r185, r211) that the neighbour groups name the same characteristic under a different label. That relation is usable information even though the legacy label is not.

### Recommendation

[✓] Confirm cluster as-is — no registry reassignment proposed.

No Phase A-initiated cluster-reassignment patch is warranted. The analytical work needed on C01 concerns dimension vocabulary and unassigned `dominant_subject`, both of which are within Phase B and Phase C scope on the target registries.

### Pointers identified for later phases

Captured here in Phase A so they are not lost, but formally written to the observations log as `[SESSION-D]` entries during the appropriate Phase C session per §7.5 and the correct `finding_id` / `flag_label` numbering discipline (requires the existing-pointers extract sequence check):

1. **CHASHAV root family** — cross-registry structural pattern between mind / purpose / thought. Session D candidate.
2. **BOUL root family** — cross-registry verb-in-mind / noun-in-counsel pattern. Session D candidate.
3. **Vocabulary gap: `Spiritual/God-ward`** — 25 groups programme-wide in C01 alone, with no clean current-vocabulary counterpart. Candidate new dimension or candidate distributive reassignment. Session D issue — must be raised via researcher decision per DR-13 (dimension vocabulary extension is a researcher decision).
4. **Vocabulary gap: `Identity/Selfhood`** — 9 groups in C01, concentrated in r182 Soul (5) and distributed elsewhere. Session D candidate.
5. **Vocabulary gap: `Somatic/Embodied`** — 6 groups in C01, concentrated in r185 flesh (5). Candidate new dimension. Session D candidate.
6. **Cross-registry root false-positive signal** — three cross-registry roots in the rootfamily extract (AT, YATSA, TAAM) appear to be string-match false positives. Not a dimension finding, but a data-pipeline observation for the CC rootfamily extractor. Record as Session D pointer or as a CC flag per researcher preference.

These are proposals; they will be formalised in the appropriate Phase C session when `finding_id` / `flag_label` numbering can be incremented from the existing-pointers extract (37 Session D pointers already exist in C01) and the flags file can confirm programme-wide uniqueness.

---

## Coverage verification note

Coverage verification (§6.5) is a Phase B step, not Phase A. It will be performed at Phase B startup for the target registries (r112 + r183) in the next session. This entry marks that the coverage check has not yet been performed — it is not an omission, it is the correct phase placement.

---

## [SESSION-END] 20260420 | Phase: A | Registry: N/A (cluster scope) | Last group completed: N/A

Next session begins: Phase B | Registry 112 (mind) | Starting from: beginning of Phase B r112
Observations log version: wa-dim-c01-observations-v1_0-20260420.md

Note on next session:
- Coverage verification (§6.5) to be run at Phase B startup for r112
- The 10 open groups (2 in r112, 8 in r183) are the groups that can proceed through Phase B → Phase C without DR-8 friction; their current labels already use §7.7 vocabulary
- The 63 locked groups in r112 and 51 locked groups in r183 will hit DR-8 at Phase C unless researcher authorises per-group unlocks; handoff §3 scope of Phase C ("Contents: update operations on wa_dimension_index rows") implies the unlocks are authorised as a block by the researcher-directed DR status change from NULL to Complete, but this interpretation needs explicit confirmation at Phase C startup
- Flags file to be supplied at next session start per GR-LOAD-001 if available

---

*End of observations log v1_0 — Phase A complete, session closing.*
