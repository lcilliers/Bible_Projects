# WA-VCB-023 Session Log — Reg 177 and 196 Complete
**File:** wa-vcb-023-session-log-reg177-196-v1-20260404.md
**Batch:** VCB-023 | **Date:** 2026-04-04
**Governing instruction:** WA-VerseContext-Instruction-v2.4-20260403.md
**Observations file at this breakpoint:** wa-vcb-023-term-observations-v1.0-20260404.md
**Preceding output:** wa-vcb-018 batch (separate session); this is first VCB-023 session log

---

## Scope of this log

Covers batch startup through completion of Reg 177 (worth) and Reg 196 (power).
Registries 187 (strength) and 196 (power) are both complete in this session segment.
Reg 197 (authority) and Reg 199 (dominion) remain.

---

## Terms classified in this segment: 14 of 73

| mti | Strong's | Gloss | Reg | Verses | Groups | Anchors | Set aside |
|---|---|---|---|---|---|---|---|
| 1263 | G5242 huperechō | be higher | 177 | 1 | 0 | 0 | 1 |
| 684 | G1411 dunamis | power | 187 | 107 | 3 | 5 | 32 |
| 689 | G1412 dunamoō | to empower | 187 | 1 | 1 | 1 | 0 |
| 694 | G1743 endunamoō | to strengthen | 187 | 8 | 1 | 2 | 0 |
| 682 | G1849 exousia | authority | 187 | 93 | 3 | 4 | 3 |
| 1302 | H0410G el | God | 196 | 107 | 3 | 4 | 5 |
| 1310 | H2429 cha.yil | strength | 196 | 5 | 1 | 1 | 2 |
| 1308 | H3201 ya.khol | be able | 196 | 86 | 2 | 4 | 39 |
| 1306 | H3444 ye.shu.ah | salvation | 196 | 22 | 1 | 2 | 0 |
| 1311 | H8592 ta.a.tsu.mah | power | 196 | 1 | 1 | 1 | 0 |
| 1305 | G1415 dunatos | able | 196 | 34 | 2 | 4 | 4 |
| 1307 | H2632 che.sen | authority | 196 | 2 | 1 | 1 | 0 |
| 1315 | H3028 yad | hand (Aramaic) | 196 | 16 | 1 | 2 | 6 |
| 1309 | H3709G kaph | palm | 196 | 133 | 4 | 8 | 51 |

**Subtotal verses processed:** 616
**Subtotal relevant:** 482 | **Set aside:** 134
**Subtotal groups:** 24 | **Total anchors:** 39

---

## Errors caught and corrected

**Cross-term vid contamination (G1411 dunamis):** During initial grouping of G1411, 6 verse_record_ids belonging to G1849 exousia were incorrectly included in the G1411 lists. These were detected by the programmatic invalid-vid check (assigned_set - all_vids). Corrected before writing to observations file. This is the verse-loss pattern flagged by the researcher. The check is now embedded in every term's verification loop.

**G3 anchor removal (G1411 dunamis):** Initial G3 anchor was vid=60466 (Act 26:18), which was subsequently identified as belonging to G1849 not G1411. G3 was left with one anchor (1Cor 15:56), which is sufficient under Rule R4.

---

## Deferred flags

None raised in this segment. No AVF findings. No structural integrity failures.

---

## Observations file status

File: wa-vcb-023-term-observations-v1.0-20260404.md
Current version: v1.0 (single version, incremental appends within this session)
Dual-written: yes

---

## Remaining work

- Reg 197 (authority): 58 terms, 1,675 verses — largest registry in batch
- Reg 199 (dominion): 1 term (H4910 ma.shal), 74 verses

Processing continues in next segment.
