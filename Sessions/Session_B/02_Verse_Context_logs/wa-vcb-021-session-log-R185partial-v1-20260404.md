# WA-VCB-021 Session Log — Classification Session 1
**Batch:** VCB-021
**Breakpoint:** Reg 185 partial — after 4 of 9 terms
**Session date:** 2026-04-04
**Governing instruction:** WA-VerseContext-Instruction-v2.4-20260403.md
**Observations file at time of this log:** wa-vcb-021-term-observations-v1.4-20260404.md
**Previous output files:** None (first session for VCB-021)

---

## Batch Overview

| Field | Value |
|---|---|
| Batch ID | VCB-021 |
| Terms in batch | 109 |
| Total verses (header) | 2,438 |
| Actual verses in extract arrays | 4,550+ (see metadata discrepancy note below) |
| Registries | Reg 185 (flesh, 9 terms), Reg 186 (gladness, 5 terms), Reg 187 (strength, 95 terms) |
| Patch construction | Deferred (109 terms > 50-term threshold) |

---

## Critical Batch-Level Data Integrity Finding

**Multiple extract metadata discrepancies detected.** The `total_verses` field in the batch JSON header does not match the actual verse array counts for at least 4 of the first 4 terms inspected:

| mti | Term | Header `total_verses` | Actual array count | Discrepancy |
|---|---|---|---|---|
| 625 | G4561 sarx | 85 | 121 | +36 |
| 618 | H1320 ba.sar | 205 | 244 | +39 |
| 617 | H1321 be.shar | 3 | 239 | +236 (severe) |
| 621 | H3318G ya.tsa | 323 | 974 | +651 (severe) |

**Classification proceeded from the actual array** (individual inspection of all verses, as required). The metadata discrepancy does not block classification but **must be flagged to Claude Code** for investigation before patch application. The actual total verse count across the batch is likely materially higher than the 2,438 stated in the header.

Additionally, H1321 (be.shar, mti=617) has `total_verses = 3` (the correct Aramaic occurrence count) but the array contains 239 verses — the full Hebrew ba.sar corpus. This indicates a batch construction error for this term.

---

## Terms Classified This Session

### Registry 185 (flesh)

#### G4561 (sarx) — flesh | mti=625
- **Array verses:** 121 | **Relevant:** 86 | **Set aside:** 35
- **Groups:** 4
  - 625-001: Sarx as governing principle of fallen human desire and moral incapacity (57 v) — Anchors: Rom 8:7; Gal 5:17
  - 625-002: Sarx as creaturely mortal condition of embodied existence (12 v) — Anchors: Php 1:22; 1Cor 15:50
  - 625-003: Sarx in Christological confession — Christ's incarnate flesh (12 v) — Anchors: Joh 1:14; 1Jn 4:2
  - 625-004: Sarx in covenantal union — "one flesh" (5 v) — Anchor: Mat 19:5
- **Deferred flags:** None
- **Anchor integrity:** Confirmed — 7 active anchors across 4 groups

#### H1320 (ba.sar) — flesh | mti=618
- **Array verses:** 244 | **Relevant:** 75 | **Set aside:** 169
- **Groups:** 6
  - 618-001: Kinship bond and solidarity — "bone and flesh" (17 v) — Anchors: Gen 2:23; 2Sa 5:1
  - 618-002: Creaturely condition before God — mortality, fragility, universal humanity (24 v) — Anchors: Num 16:22; Isa 40:6
  - 618-003: Misplaced creaturely trust — flesh as insufficient basis for confidence (8 v) — Anchors: Jer 17:5; Isa 31:3
  - 618-004: Covenant sign in flesh — circumcision/uncircumcision (9 v) — Anchors: Gen 17:11; Eze 44:7
  - 618-005: Body mediating inner states — flesh as site of longing, fear, awe, grief (13 v) — Anchors: Psa 63:1; Pro 14:30
  - 618-006: Prophetic transformation — heart of flesh replacing heart of stone (4 v) — Anchors: Eze 36:26; Eze 37:6
- **Deferred flags:** None
- **Anchor integrity:** Confirmed — 12 active anchors across 6 groups

#### H1321 (be.shar) — flesh [Aramaic] | mti=617
- **Array verses:** 239 | **Relevant:** 74 | **Set aside:** 165
- **Note:** Parallel to H1320 ba.sar — same biblical texts, different verse_record_ids. Groups 617-001 through 617-006 mirror 618-001 through 618-006. Filter decisions consistent with H1320. The three genuinely Aramaic be.shar verses (Dan 2:11, Dan 4:12, Dan 7:5) are included and classified.
- **Groups:** 6 (617-001 through 617-006, parallel to H1320)
  - 617-001: Kinship bond and solidarity (17 v) — Anchors: Gen 2:24 (vid=10029); Gen 37:27 (vid=10051)
  - 617-002: Creaturely condition before God (24 v) — Anchors: Num 16:22 (vid=10130); Lev 17:11 (vid=10114)
  - 617-003: Misplaced creaturely trust (7 v) — Anchors: 2Ch 32:8 (vid=10162); Jer 11:15 (vid=10224)
  - 617-004: Covenant sign in flesh (9 v) — Anchors: Gen 17:11 (vid=10044); Eze 44:7 (vid=10251)
  - 617-005: Body mediating inner states (13 v) — Anchors: 1Ki 21:27 (vid=10155); 2Ki 6:30 (vid=10159)
  - 617-006: Prophetic transformation (4 v) — Anchors: Eze 36:26 (vid=10245); Eze 37:6 (vid=10246)
- **Deferred flags:** None
- **Anchor integrity:** Confirmed — 12 active anchors across 6 groups

#### H3318G (ya.tsa) — to come out: come | mti=621
- **Array verses:** 974 | **Relevant:** 46 | **Set aside:** 928
- **Character of term:** Movement verb. Inner-being engagement is present in a minority of uses — primarily where the term names the going-out of souls/spirits, God's word/righteousness/judgment, inner states venting outward, or God acting in theophanic departure. The large Exodus deliverance corpus ("brought you out of Egypt") was individually inspected and classified as set aside — ya.tsa names the historical/physical event of departure, not an inner-being engagement.
- **Groups:** 4
  - 621-001: Soul/spirit going out — soul departing at death, spirits going forth to act (7 v) — Anchors: Gen 35:18; 2Sa 13:39
  - 621-002: God's word/righteousness/salvation going forth — divine inner purpose expressed outwardly (16 v) — Anchors: Isa 55:11; Isa 51:5
  - 621-003: Inner states going outward — folly, iniquity, joy, celebration expressed through going-out (14 v) — Anchors: Pro 29:11; Psa 41:6
  - 621-004: God going out — theophanic divine action and presence (9 v) — Anchors: Psa 68:7; Hab 3:13
- **Deferred flags:** None
- **Anchor integrity:** Confirmed — 8 active anchors across 4 groups

---

## Terms Remaining in Reg 185 (5 of 9)

| mti | Term | Gloss | Verses (header) |
|---|---|---|---|
| 620 | H3894 le.chum | intestine | 2 |
| 616 | H6371 pi.mah | excess fat | 1 |
| 619 | H7607 she.er | flesh | 16 |
| 3012 | H7608 sha.a.rah | kinswomen | 1 |
| 622 | H8270 shor | umbilical cord | 2 |

---

## Registry 186 — gladness (5 terms, 129 verses)

| mti | Term | Gloss | Verses |
|---|---|---|---|
| 634 | G2165 eufrainō | to celebrate | 14 |
| 630 | G2174 eupsucheō | be glad | 1 |
| 635 | H2302 cha.dah | to rejoice | 3 |
| 633 | H2868 te.ev | be good | 1 |
| 632 | H3190 ya.tav | be good | 110 |

---

## Registry 187 — strength (95 terms, 1,671 verses)

Not yet started. Full term list includes strength-core terms, oikos-family dwelling terms, enemy/hostility terms, animal/tree terms used for strength imagery, and other semantic clusters.

---

## Work Order for Next Session

1. Complete Reg 185 remaining 5 terms (small corpora — quick processing)
2. Process all 5 Reg 186 (gladness) terms
3. Begin Reg 187 (strength) — 95 terms, will require multiple sub-sessions
4. After all terms classified: produce flags register (if any deferred flags), then proceed to patch construction session

---

## Session Notes

- **No deferred flags** raised in this session.
- **Metadata discrepancies** (4 terms) accumulated as a batch-level data integrity note. Will be included in flags register / handoff to Claude Code.
- **Observations file** current version: **v1.4** (`wa-vcb-021-term-observations-v1.4-20260404.md`)
- **Patch construction** deferred per §6.4 (>50 terms).
- All file outputs dual-written to `/home/claude/` and `/mnt/user-data/outputs/`.
