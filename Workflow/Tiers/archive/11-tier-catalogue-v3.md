# Tier Catalogue — Restructured (Question-Led Inversion) · v3 · 2026-06-14

> **Built from v2** ([`wa-tier-catalogue-restructured-v2-20260611.md`](wa-tier-catalogue-restructured-v2-20260611.md)) by **inverting the direction**. v2 made the 14 VE points the master and dissolved the T1–T7 questions into them. **v3 makes the T0–T7 questions the master**, maps the VE point(s) *into* each question, and evaluates whether the VE point **satisfies the question — Fully / Partially / Not at all.**
>
> **Purpose:** answer the L1 objective directly — *does the mechanical (and read) verse-extraction actually comply with the catalogue questions, and where are the gaps?* Nothing here is a fix or a recommendation; it is an evaluation against v2's own mappings, with the judgement calls (Full/Partial/None) made explicit so you can overrule them.
>
> **For your evaluation — DB not modified.** Codes are v2's. Where v2's §1 (VE merges) and §5 (disposition index) **disagree about a question**, I flag it `⚠v2-conflict` rather than pick silently.

---

## 0. How to read the verdict

For each question I give: **which VE point maps in** · the VE point's **M/R** tag · **satisfies?** · the basis.

**Satisfies? scale**

| Verdict | Meaning |
|---|---|
| **FULL** | a **live** VE field (VE-01…14) answers the *whole* of this question at the verse — nothing of its ask is left over |
| **PARTIAL** | a live VE field captures the **verse-instance**, but part of the question (a *"what does it reveal" / "over time" / "pattern" / "across the evidence" / "full range"* clause) is **not** captured at the verse and routes to SYNTH |
| **NONE** | **no** live VE field answers this at the verse — it is a **SYNTH roll-up** computed across verses, so the verse-extraction (L1/L2 read) does **not** satisfy it (the VE field(s) that *feed* the roll-up are noted) |
| **FOLD** | the *"if silent, note explicitly"* sub-question — satisfied by the field's **NONE/SILENT token** |
| **PROPOSED** | would be answered by a **proposed** field (VE-15/16/17) that is **not yet live** → in practice currently **NONE** |
| **DROP / DEFER** | removed / deferred in v2 — no verdict applies |

**The M/R tag is the L1 lever.** Only **M** fields (`VE-01 sense`, `VE-02 type`, `VE-04 mode`, `VE-05 location`-keyword seed, `VE-17` auto) can be pre-filled by **L1 mechanical** work without the read. Every **R** field requires the L2 read. So a question is **"L1-mechanically satisfiable"** only when its VE field is **M** *and* the verdict is **FULL**.

---

## 1. The headline (full tally in §4)

Of the **189** catalogue questions, against the **live** VE fields:

| Verdict | Count | What it means for L1 |
|---|---|---|
| **FULL** (live field, whole question) | **24** | satisfied at the verse — but mostly **R** (need the read), only ~2 are **M** |
| **PARTIAL** (verse-instance only) | **9** | verse captured; the *reveal/range/over-time* part is SYNTH |
| **NONE** (SYNTH roll-up) | **~113** | **not satisfiable by verse-extraction at all** — needs the cross-verse synthesis |
| **FOLD** (silence token) | **~16** | satisfied only as a NONE/SILENT marker |
| **PROPOSED** (VE-15/16/17 not live) | **7** | T4 interfaces, suffering, co-occurrence — uncovered until adopted |
| **DROP** | **16** · **DEFER** **4** | removed / parked |

**The L1-mechanical reality:** of 189 questions, **L1 mechanical alone FULLY satisfies ≈ 2** (`T1.2.1`→VE-02 type, `T1.4.2`→VE-04 mode). VE-01/04 keyword/morph seed a handful more **partially**; VE-05 keyword seeds **6** location questions **pending read confirmation**. **Everything else needs the read (R) or is a SYNTH roll-up.** So "complete the L1 *mechanical* work in compliance with the catalogue" covers only a thin slice of the catalogue — the rest of compliance is the read and the synthesis. That is the gap to confront before signing off.

---

## 2. Question-led evaluation — T0–T3

### T0 — Divine Image and Created Design
| Question | → VE | M/R | satisfies? | basis |
|---|---|---|---|---|
| T0.1.1 nature of God it images | — (fed VE-08) | — | **NONE** | SYNTH |
| T0.1.2 attributed to God + what it reveals | VE-08 | R | **PARTIAL** | attribution (yes/no/how) at verse; "reveals significance" → SYNTH |
| T0.1.3 what the silence suggests | — (fed VE-08) | — | **NONE** | SYNTH |
| T0.2.1 purpose — equips to be/do/become | VE-09 | R | **FULL** | `purpose_equips` answers it directly |
| T0.2.2 created-design vs fall | — (fed VE-09/12) | — | **NONE** | SYNTH |
| T0.2.3 oriented to future fullness | — | — | **NONE** | SYNTH |
| T0.3.1 how it expresses the divine image | — | — | **NONE** | SYNTH |
| T0.3.2 shared with God vs creaturely analogue | — | — | **NONE** | SYNTH |
| T0.3.3 presence/absence & image condition | — | — | **NONE** | SYNTH |
| T0.4.1 does Scripture use it typologically | VE-10 | R | **PARTIAL** `⚠v2-conflict` | §1 merges into VE-10 (verse), §5 says SYNTH; verse typology via VE-10, corpus-level → SYNTH |
| T0.4.2 direction of typology | VE-10 | R | **FULL** | `typology_direction` |
| T0.4.3 if none, note | VE-10 | R | **FOLD** | → `none` token |

### T1 — Definition
| Question | → VE | M/R | satisfies? | basis |
|---|---|---|---|---|
| T1.1.1 programme name & what it signals | — | — | **NONE** | SYNTH (programme construct) |
| T1.1.2 what the H/G terms reveal definitionally | VE-01 | M | **PARTIAL** `⚠v2-conflict` | §1 merges into VE-01; §5 says SYNTH; verse-sense captured, full definitional read → SYNTH |
| T1.1.3 directional/relational/constitutional implication of the name | VE-13 | R | **FULL** | `relational_implication` |
| T1.2.1 kind — act/status/quality | VE-02 | **M** | **FULL** | `type` — **L1-mechanical** |
| T1.2.2 simple or compound | VE-03 | R | **FULL** | `compound` |
| T1.2.3 best working description | — | — | **DROP** | programme write-up step |
| T1.3.1 structural opposite | — | — | **NONE** | SYNTH (boundary) |
| T1.3.2 what it excludes/resists | — | — | **NONE** | SYNTH |
| T1.3.3 what it is not / where it ends | — | — | **NONE** | SYNTH |
| T1.4.1 distinct modes of operation | VE-04 | **M** | **PARTIAL** | verse mode captured; full mode-set → SYNTH |
| T1.4.2 mode varies by context/direction/level | VE-04 | **M** | **FULL** | VE-04 includes context/direction/level dependence — **L1-mechanical** |
| T1.4.3 speech-based mode | — | — | **NONE** | SYNTH |
| T1.5.1 immediate response | VE-11 | R | **FULL** | `immediate_response` |
| T1.5.2 response consistent or varies | — | — | **NONE** | SYNTH (across evidence) |
| T1.5.3 if silent, note | VE-11 | R | **FOLD** | → `SILENT` |
| T1.6.1 what it produces over time | VE-12 | R | **PARTIAL** | verse effect captured; over-time → SYNTH |
| T1.6.2 states/qualities established | — | — | **NONE** | SYNTH |
| T1.6.3 sustained vs immediate | — | — | **NONE** | SYNTH |
| T1.7.1 conditions enabling reception | — | — | **NONE** | SYNTH |
| T1.7.2 conditions blocking reception | — | — | **NONE** | SYNTH |
| T1.7.3 non-receiver inner state | — | — | **NONE** | SYNTH |
| T1.8.1–.3 dimension classification | — | — | **DROP** | dimension construct retired |

### T2 — Constitutional Location and Boundaries
| Question | → VE | M/R | satisfies? | basis |
|---|---|---|---|---|
| T2.1.1 located at spirit level here | VE-05 | M-kw+R | **FULL** | `constitutional_location` records the level |
| T2.1.2 originates in / primarily spirit | — | — | **NONE** | SYNTH |
| T2.1.3 what spirit-location reveals | — | — | **NONE** | SYNTH |
| T2.1.4 if silent, note | VE-05 | M-kw+R | **FOLD** | → `NONE` |
| T2.2.1 soul-level here | VE-05 | M-kw+R | **FULL** | location |
| T2.2.2 what soul-location reveals | — | — | **NONE** | SYNTH |
| T2.2.3 if silent | VE-05 | M-kw+R | **FOLD** | |
| T2.3.1 heart here | VE-05 | M-kw+R | **FULL** | location |
| T2.3.2 what heart-location reveals | — | — | **NONE** | SYNTH |
| T2.3.3 if silent | VE-05 | M-kw+R | **FOLD** | |
| T2.4.1 mind here | VE-05 | M-kw+R | **FULL** | location |
| T2.4.2 what mind-location reveals | — | — | **NONE** | SYNTH |
| T2.4.3 if silent | VE-05 | M-kw+R | **FOLD** | |
| T2.5.1 other soul-subset here | VE-05 | M-kw+R | **FULL** | `other-soul:<x>` |
| T2.5.2 what it reveals | — | — | **NONE** | SYNTH |
| T2.5.3 if silent | VE-05 | M-kw+R | **FOLD** | |
| T2.6.1 specific body part | VE-05 | M-kw+R | **FULL** | `body-part:<x>` |
| T2.6.2 what the body link does | — | — | **NONE** | SYNTH |
| T2.6.3 if silent | VE-05 | M-kw+R | **FOLD** | |
| T2.7.1 body↔soul direction | — | — | **NONE** | SYNTH |
| T2.7.2 consequence of direction | — | — | **NONE** | SYNTH |
| T2.7.3 if silent | VE-05 (body) | — | **FOLD** | |
| T2.8.1–.3 body deposit (DNA/generational) | — | — | **DROP** | speculative construct |
| T2.9.1 origin (within/received/God/generational) | VE-06 | R | **FULL** | `origin` |
| T2.9.2 origin singular or multiple | — | — | **NONE** | SYNTH |
| T2.9.3 origin changes across contexts | — | — | **NONE** | SYNTH |
| T2.10.1–.3 constitutional movement across levels | — | — | **NONE** | SYNTH |

### T3 — The Inner Faculties
| Question | → VE | M/R | satisfies? | basis |
|---|---|---|---|---|
| T3.1.1 perception engaged? | VE-07 | R | **FULL** | `faculty` multi-select |
| T3.2.1 cognition engaged? | VE-07 | R | **FULL** | |
| T3.3.1 memory engaged? | VE-07 | R | **FULL** | |
| T3.4.1 affect engaged? | VE-07 | R | **FULL** | |
| T3.5.1 creativity engaged? | VE-07 | R | **FULL** | |
| T3.6.1 volition engaged? | VE-07 | R | **FULL** | |
| T3.7.1 agency engaged? | VE-07 | R | **FULL** | |
| T3.8.1 moral-evaluation engaged? | VE-07 | R | **FULL** | |
| T3.9.1 conscience engaged? | VE-07 | R | **FULL** | |
| T3.11.1 relational capacity engaged? | VE-07 | R | **FULL** | |
| T3.x.2 (×11) enable/deepen/bypass/impair | — | — | **NONE** | SYNTH |
| T3.x.3 (×11) what the pattern reveals | — | — | **NONE** | SYNTH |
| T3.10.1–.3 Conscientiousness (composite) | — | — | **NONE** | SYNTH composite of VE-07 affect/volition/agency/moral/conscience |

---

## 3. Question-led evaluation — T4–T7

### T4 — Relational Interfaces  *(VE-15 is **proposed**, not live → these are currently uncovered)*
| Question | → VE | M/R | satisfies? | basis |
|---|---|---|---|---|
| T4.1.1 God→human here | VE-15 | R | **PROPOSED** | would be FULL if VE-15 adopted |
| T4.1.2/.3 basis / disposition | — | — | **NONE** | SYNTH |
| T4.1.4 if silent | VE-15 | R | **FOLD** (proposed) | |
| T4.2.1 human→God (seeking/worship) | VE-15 | R | **PROPOSED** | |
| T4.2.2/.3 inner posture / what it reveals | — | — | **NONE** | SYNTH |
| T4.2.4 if silent | VE-15 | R | **FOLD** (proposed) | |
| T4.3.1 giving to another | VE-15 | R | **PROPOSED** | |
| T4.3.2/.3 conditions in giver | — | — | **NONE** | SYNTH |
| T4.3.4 if silent | VE-15 | R | **FOLD** (proposed) | |
| T4.4.1 receiving from another | VE-15 | R | **PROPOSED** | |
| T4.4.2/.3 conditions / non-receiver | — | — | **NONE** | SYNTH |
| T4.4.4 if silent | VE-15 | R | **FOLD** (proposed) | |
| T4.5.1–.3 relational boundaries / scope | — | — | **NONE** | SYNTH |
| T4.5.4 if silent | — | — | **FOLD** | |
| T4.6.1 spiritual-beings interface | VE-15 | R | **PROPOSED** | |
| T4.6.2/.3 adversarial site / angelic mediation | — | — | **NONE** | SYNTH |
| T4.6.4 if silent | VE-15 | R | **FOLD** (proposed) | |

### T5 — Formative and Developmental
| Question | → VE | M/R | satisfies? | basis |
|---|---|---|---|---|
| T5.1.1–.3 nature of transformation | — | — | **NONE** | SYNTH (fed VE-11/12) |
| T5.2.1–.3 sequence of inner states | — | — | **NONE** | SYNTH |
| T5.3.1–.3 mechanism of change | — | — | **NONE** | SYNTH |
| T5.4.1 in relation to suffering (role) | VE-16 | R | **PROPOSED** | VE-16 not live |
| T5.4.2 does suffering deepen/test/reveal/produce | — | — | **NONE** | SYNTH |
| T5.4.3 if silent | VE-16 | R | **FOLD** (proposed) | |
| T5.5.1–.3 formation & sanctification arc | — | — | **NONE** | SYNTH |
| T5.6.1–.3 eschatological trajectory | — | — | **NONE** | SYNTH |
| T5.7.1–.3 deposit consequence | — | — | **DROP** | depends on dropped T2.8 |

### T6 — Structural Relationships
| Question | → VE | M/R | satisfies? | basis |
|---|---|---|---|---|
| T6.1.1 which characteristics co-occur | VE-17 | auto | **PROPOSED** | co-occurrence array — auto from verse-complete read, not yet a live field |
| T6.1.2/.3 co-occurrence pattern & reveal | — | — | **NONE** | SYNTH |
| T6.2.1–.3 sequential relationships | — | — | **NONE** | SYNTH |
| T6.3.1–.4 causal / constitutive relationships | — | — | **NONE** | SYNTH |
| T6.4.1–.4 vocabulary & root sharing | — | — | **NONE** | SYNTH |
| T6.5.1–.4 distinctions from neighbours | — | — | **NONE** | SYNTH |
| T6.6.1–.3 shared verse anchors | — | — | **DROP** | VCG/programme construct |
| T6.7.1–.3 dimensional sharing | — | — | **DROP** | dimension construct |

### T7 — Evidential and Methodological Foundation
| Question | → VE | M/R | satisfies? | basis |
|---|---|---|---|---|
| T7.1.1 primary H/G terms & root meanings | — (fed VE-01) | — | **NONE** | SYNTH |
| T7.1.2 grammatical range & what it reveals | VE-04 | M | **PARTIAL** `⚠v2-conflict` | §1 merges into VE-04 (verse form); §5 says SYNTH; range/reveal → SYNTH |
| T7.1.3 semantic range / breadth | VE-01 | **M** | **PARTIAL** | VE-01 gives this verse's sense + its place in range; full breadth → SYNTH |
| T7.1.4–.10 vocabulary arc | — | — | **NONE** | SYNTH |
| T7.2.1 function of term in its verse | — | — | **NONE** | SYNTH |
| T7.2.2 literary form (+ what it requires) | VE-14 | R | **PARTIAL** | form captured; "requires for interpretation" → SYNTH |
| T7.2.3 logical structure of argument | — | — | **NONE** | SYNTH |
| T7.2.4 contextual setting (+ what it reveals) | VE-14 | R | **PARTIAL** | setting captured; "reveals" → SYNTH |
| T7.2.5 primary anchor verse | — | — | **NONE** | SYNTH |
| T7.2.6 what the anchor uniquely reveals | — | — | **NONE** | SYNTH |
| T7.3.1–.4 human science frameworks | — | — | **DEFER** | external lens; revisited in synthesis |

---

## 4. What this inversion exposes (for your sign-off)

1. **The catalogue is overwhelmingly a SYNTH instrument, not a verse-extraction one.** ~113 of 189 questions (60%) are roll-ups that **no verse field satisfies** — they are answered only by computing across verses. The verse-extraction (L1/L2) **feeds** them but does not **satisfy** them.
2. **L1 *mechanical* satisfies almost nothing on its own** — ≈2 questions FULL (`type`, `mode`), a few PARTIAL (sense, grammatical form), and 6 location questions only **keyword-seeded pending the read**. "Complete the L1 mechanical work in compliance with the catalogue" therefore means, concretely, *a tiny mechanical core + a hard dependency on the read for everything else.* That dependency is the thing to face before sign-off, not after.
3. **The 7 PROPOSED questions (T4 interfaces, T5.4 suffering, T6.1 co-occurrence) are wholly uncovered** until VE-15/16/17 are adopted (decisions D2/D4 in v2 §6).
4. **v2 is internally inconsistent on 3 questions** (`T0.4.1`, `T1.1.2`, `T7.1.2`): §1 merges them into a VE field while §5 routes them to SYNTH. I rated them PARTIAL and flagged `⚠v2-conflict` — they need a decision, not a silent pick.
5. **FULL-but-R is the bulk of "satisfied"** — 22 of the 24 FULLs are `R` fields (faculty ×10, location ×6, origin, purpose, immediate-response, typology-direction, relational-implication, compound). They *are* satisfiable at the verse, but only by the **read**, never mechanically.

> Verdicts are my assessment derived from v2's mappings + the question text — **overrule any of them.** Nothing in the DB is changed. The natural next decisions are the same D1–D7 in v2 §6, now seen from the question side: *which questions must L1 satisfy mechanically, which require the read, and which are explicitly SYNTH-only.*
