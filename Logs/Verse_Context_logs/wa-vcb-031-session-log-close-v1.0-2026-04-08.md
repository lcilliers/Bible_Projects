# wa-vcb-031-session-log-close-v1.0-2026-04-08

**Session:** VCB-031 + Vertical Pass Experiment
**Date:** 2026-04-08
**Registries touched:** 213 (listen) — Complete; 183 (heart) — In Progress
**Governing instruction:** WA-VerseContext-Instruction-v2.4-20260403.md
**Previous log:** wa-vcb-031-session-log-full-v1.0-2026-04-08.md

---

## 1. Session summary

This session accomplished three distinct bodies of work:

1. **VCB-031 — Registry 213 (listen) classified and patched.** 36 terms, 748 verses, 49 groups, patch applied and verified. Registry 213 verse_context_status = Complete.

2. **Vertical pass experiment — initiated and run on three verses.** Jer 7:24, Rom 10:17, Isa 55:3 pulled from the database and analysed across all registry faces. The experiment surfaced a significant programme-level methodological insight and a database error.

3. **REPAIR — H3820A lev restored.** mti=581 incorrectly set to delete during bulk cleanup. Restored to extracted; 331 verse records reactivated; Registry 183 reset to In Progress.

---

## 2. VCB-031 outputs (complete)

| File | Purpose |
|---|---|
| PATCH-20260408-VCB031-VERSECONTEXT-V1.json | Applied — Registry 213 Complete |
| wa-vcb-031-term-observations-v1.1-2026-04-08.md | Final classification record |
| wa-vcb-031-flags-register-v1.0-2026-04-08.md | 57 flags, all resolved |
| wa-vcb-031-session-log-full-v1.0-2026-04-08.md | Full session log |
| wa-vcb-031-schema-instruction-v1.0-2026-04-08.md | Schema additions (applied) |

**Schema additions applied to database:**
- `verse_context_group.vertical_pass_flag` INTEGER DEFAULT 0
- `verse_context.vertical_pass_flag` INTEGER DEFAULT 0
- `verse_context.set_aside_reason` TEXT DEFAULT NULL (5 controlled values)

---

## 3. Vertical pass experiment — findings

### 3.1 The experiment

Three verses pulled from the database with all cross-registry term links and existing VC classifications:

| Verse | Active term links | Registries |
|---|---|---|
| Jer 7:24 | 4 | counsel (32), stubbornness (153), listen (213) ×2 |
| Rom 10:17 | 4 | anointing (6), faith (59), seeking (140), listen (213) |
| Isa 55:3 | 8 | appetite (8), compassion (23), covenant (34) ×2, despair (44), love (103), soul (182), listen (213) |

### 3.2 Core findings

**Finding 1 — Many-to-many confirmed in live data**
All three verses show term links across multiple registries simultaneously. Isa 55:3 touches eight terms across six registries. The database already holds the multi-face reality; it has not previously been read this way.

**Finding 2 — Two functional term types confirmed**
The distinction between characteristic terms and property terms holds clearly:
- *Characteristic terms* (soul, faith, stubbornness, counsel, steadfast love, covenant) name inner-being states and structures
- *Property terms* (o.zen, sha.ma, akoē) name the mechanism, condition or expression of those characteristics
The same property term can serve different characteristics across its verse corpus, and can serve the same characteristic in opposite ways (hearing as channel of faith; refused hearing as expression of heart-hardness).

**Finding 3 — The vertical pass model works**
Reading a verse from multiple registry faces simultaneously produces richer analytical output than any single face. Each face contributes a partial but coherent picture; the whole exceeds the sum of its parts.

**Finding 4 — VCB-031 group descriptions validated**
Group 7498-001 ("faith reception — akoē as the channel through which faith arrives") is confirmed by the cross-registry data. Faith registry 59 classifies Rom 10:17 as relevant independently — the two registries face the same verse from complementary angles.

**Finding 5 — The vertical pass is a data quality probe**
The experiment surfaced that data completeness cannot be assumed. Even for core terms, specific verse instances may be missing or suppressed. The vertical pass revealed the H3820A lev error that would otherwise have remained invisible until Session B.

### 3.3 Specific verse findings

**Jer 7:24** — "stubbornness of their evil hearts"
- Primary characteristic: *she.ri.rut* (stubbornness) as the root inner state
- Secondary characteristic: *mo.e.tsah* (counsel) as the autonomous inner substitute for God's direction
- Property terms: *sha.ma* (refused covenantal act) and *o.zen* (refused receptive faculty) — both expressing the stubbornness, not causing it
- Missing: H3820A lev ("their hearts" — *libbam*) — the seat of the stubbornness. Absent because mti=581 was incorrectly deleted. Now restored. → Feeds VCB-032.
- Additional terms deleted at verse-record level: H7451H ra (evil), H5186 na.tah (to incline), H6440G pa.neh (face/before) — normal programme filtering, not anomalous

**Rom 10:17** — "faith comes from hearing"
- Generative chain: Christ → word → hearing → faith
- Primary characteristic: *pistis* (faith) — the destination
- Property term: *akoē* (hearing) — the channel
- Directional connector: *ek* (out from, Reg 140 seeking) — worth examining at Session B reg 140
- G5547 christos set aside in anointing registry — correct; Christ here is source of the word, not anointing referent. Pre-VCB-031 set_aside_reason is NULL.

**Isa 55:3** — "incline your ear… that your soul may live"
- Most complex: soul (ne.phesh) as the overarching subject; ear (o.zen) as entry point; covenant/faithfulness/steadfast love as the framework and content; vitality (cha.yah) as the outcome
- H0539 a.man in despair registry (44) unexpected — worth examining at Session B reg 44
- H2617B che.sed set aside in compassion registry (23) with NULL set_aside_reason — pre-VCB-031 record, reason not captured

### 3.4 vr_del pattern baseline established
- Programme-wide active ratio: 27.3% (62,064 active / 227,423 total)
- Jer 7:24 at 19% active — within normal range; Jer 7:22 is 0% active
- High deletion rate reflects normal Session A extraction and audit filtering, not specific anomalies

---

## 4. REPAIR — H3820A lev

**Patch applied:** PATCH-20260408-REPAIR-LEV-H3820A-V1.json

**What happened:** mti=581 H3820A lev was incorrectly set to `status=delete` during a bulk cleanup pass. The status_note on the record explicitly identified it as "THE primary Hebrew heart term — must be extracted as the registry's anchor term." The bulk operation caught mti=581 alongside five legitimate phantom entries (mti=1436, 2265, 4183, 4922, 6603).

**What was restored:**
- mti=581 status → extracted
- mti=581 delete_flagged → 0
- mti=581 term_owner_type → OWNER
- 331 verse records reactivated (delete_flagged → 0)
- Registry 183 verse_context_status → In Progress

**Phantom entries untouched:** mti=1436, 2265, 4183, 4922, 6603 remain at status=delete.

**Note on patch scope:** The applicator correctly restored delete_flagged and term_owner_type on mti=581 in addition to the two explicit patch operations. For future REPAIR patches involving term restoration, all three fields (status, delete_flagged, term_owner_type) should be specified explicitly in the patch.

---

## 5. Methodological discovery — characteristic-perspective grouping model

This session produced a significant revision to the programme's grouping methodology. Full documentation in wa-vcb-031-session-log-full-v1.0-2026-04-08.md §5. Summary:

**The error identified:** Groups were term-centric — descriptions named what the term does rather than what the verse is about. The correction: groups should name the inner-being characteristic the verse cluster is primarily about, with the term's role stated accurately.

**The two-type distinction:** Terms fall on a spectrum from pure characteristic terms (name an inner-being state) to property terms (describe how characteristics operate). Property terms can serve different characteristics across their verse corpus and serve the same characteristic in opposite ways.

**The vertical pass model:** Rather than keeping the entire corpus horizontal at the same depth, the programme should slice vertically — go deep on a focused characteristic or term cluster, hold the rest as available context. Each analytical pass is a face through the data. No single face shows everything; the underlying data is complete regardless.

**The set_aside_reason field:** Added to verse_context in VCB-031 to enable rediscovery of wrong_face set-asides under future analytical passes.

**Requires encoding in:** WA-VerseContext-Instruction v2.5 (group formation rule revision).

---

## 6. Database state at session close

| Registry | Word | verse_context_status | session_b_status |
|---|---|---|---|
| 183 | heart | In Progress | Verse Context Reset |
| 213 | listen | Complete | Verse Context Reset |

All other registries unchanged from session start.

---

## 7. Forward destinations — three sessions

### Destination A: VCB-032 — Registry 183 (heart), H3820A lev

**What:** Targeted VCB session for H3820A lev only. H3824 levav and G2588 kardia already classified.
**Scope:** 331 verses, mti=581, single term
**Extract:** Claude Code to build wa-vcb-032-extract-{date}.json
**Notes:**
- lev is the most central inner-being term in the Hebrew Bible — classification requires care
- Verse corpus will include many of the OT's most theologically significant inner-being passages
- The characteristic-perspective grouping model (from this session) should govern group formation
- Groups will cover: heart as seat of characteristics (positive and negative); heart directed toward God; hardened/uncircumcised heart; heart known by God; heart and covenant; heart as the locus of understanding, will, and emotion
- Governing instruction for this session: WA-VerseContext-Instruction-v2.4 with the characteristic-perspective amendment (v2.5 pending)
- Given corpus size and theological density, patch construction will likely be a separate session

### Destination B: Vertical pass continuation — Jer 7:24

**What:** Resume vertical pass analysis of Jer 7:24 once H3820A lev is classified in VCB-032
**Dependency:** VCB-032 must be applied before this session runs
**Scope:** Re-pull Jer 7:24 cross-registry data with lev now active; complete the characteristic map; produce the first full vertical pass annotation
**The question to answer:** Does lev's classification in Registry 183 for Jer 7:24 land in a "stubbornness of heart" group, a "heart refusing God" group, or a "heart as seat of evil" group? That group assignment is the face that completes the picture alongside stubbornness (153), counsel (32), and listen (213).

### Destination C: Vertical pass instruction document

**What:** WA-VerticalPass-Instruction-v1.0 — encoding the vertical pass methodology as a programme document
**Content to capture from this session:**
1. Purpose — what the vertical pass is and what it is not
2. The characteristic-perspective model — characteristic terms vs property terms; the spectrum
3. The face model — vertical slicing, depth on demand, context available
4. The many-to-many architecture — how verse_records, mti_terms, and registries create the multi-face data structure
5. Procedure — what queries to run, what to look for, how to annotate a vertical pass verse
6. The vertical_pass_flag field — what triggers it, who sets it, what it means
7. The set_aside_reason field — wrong_face rediscovery procedure
8. The three-verse experiment findings as illustrative examples
9. Relationship to Session B — how vertical pass findings feed into Session B analysis
10. Data quality probe function — using vertical pass to surface extraction gaps and repair needs
**Format:** Instruction document — WA-VerticalPass-Instruction-v1.0-{date}.md
**Note:** This document should be drafted before or alongside VCB-032, so the characteristic-perspective model is fully encoded before classifying the most important term in the programme.

---

## 8. Open items carried forward

| Item | Destination | Notes |
|---|---|---|
| G1537 ek in seeking registry (Rom 10:17) | Session B reg 140 | Preposition in seeking registry — examine role |
| H0539 a.man in despair registry (Isa 55:3) | Session B reg 44 | Faithfulness term in despair registry — unexpected |
| H2617B che.sed set aside null reason (Isa 55:3) | VCB repair | Pre-VCB-031 record, set_aside_reason not populated |
| WA-VerseContext-Instruction v2.5 | Instruction update | Encode characteristic-perspective grouping rule |
| REPAIR patch note | Programme record | Future REPAIR patches for term restoration should explicitly include status, delete_flagged, term_owner_type |
| Vertical pass baseline established | Programme record | Active ratio: 27.3%; vr_del pattern is normal filtering behaviour |

---

*Session log v1.0 | 2026-04-08 | VCB-031 Complete | REPAIR-LEV-H3820A applied | Vertical pass experiment initiated | Three forward destinations identified*
