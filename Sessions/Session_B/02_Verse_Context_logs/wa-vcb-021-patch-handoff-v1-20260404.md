# PATCH SUBMISSION TO CLAUDE CODE

**Patch file:** wa-vcb-021-patch-v1-20260404.json  
**Patch type:** VERSECONTEXT  
**Batch:** VCB-021  
**Date:** 2026-04-04  
**Governing instruction:** WA-VerseContext-Instruction-v2.4-20260403.md §7.8

---

## Action Required

1. **Apply patch** — insert verse_context_group and verse_context records per operations list
2. **Resolve group_code strings to integer ids** for all new groups in this patch (all 125 groups are new)
3. **Validate consistency rules R1–R4** after application
4. **Run integrity validation** (§13)
5. **Handle XREF coverage check** for all affected registries (§0.2): Reg 185, Reg 186, Reg 187
6. **For each registry whose OWNER terms appear in this batch:**
   - Run completion check (§14.5)
   - If complete: SET verse_context_status = 'Complete', re-export full word JSON
7. **Report:** records inserted/updated, registries advanced to Complete, XREF coverage status, any integrity violations

---

## Patch Summary

| Field | Value |
|---|---|
| Total operations | 3,527 |
| Group inserts | 125 |
| verse_context inserts | 3,402 |
| Relevant verses | 1,180 |
| Set aside verses | 2,222 |
| Anchor verses | 222 |
| Dual-context verses | 1 (vid=12683, Isa 11:2 — in groups 651-001 and 651-002) |
| Revisions to prior | 0 |

---

## Registries in This Batch

| Registry | Word | Terms in batch | Status expected |
|---|---|---|---|
| 185 | flesh | 8 OWNER terms | All classified — check XREF coverage |
| 186 | gladness | 5 OWNER terms | All classified — check XREF coverage |
| 187 | strength | 96 OWNER terms (incl 26 AVF) | All classified — check XREF coverage |

---

## Data Integrity Flags — Investigate After Application

These do not block patch application but require Claude Code investigation:

1. **mti=625 sarx:** `total_verses` header = 85, actual verse array = 121. Batch construction metadata error.
2. **mti=618 ba.sar:** header = 205, actual = 244.
3. **mti=617 be.shar:** header = 3, actual = 239. Severe discrepancy.
4. **mti=621 ya.tsa:** header = 323, actual = 974.
5. **mti=7021 H0352C a.yil (leader):** All 139 verses set aside. Suspected wrong verse pool — all verses appear to be H0352A (ram) verses. The leader/mighty-man sense does not appear. Investigate verse pool assignment before any reclassification. DF-025.
6. **mti=7022 H0352D a.yil (terebinth):** Same as above — 139 verses all SA, suspected wrong pool. DF-026.
7. **mti=6877 ez.ro.a (vid=215365 Jer 32:21):** Included as relevant per RD-PC-001. Marked in patch notes as borderline. Researcher may review at any time via VCVERSE patch if desired.

---

## Notes on AVF Terms

26 terms confirmed all-verses-fail (DF-001 through DF-026). All verses for these terms are set aside in the patch (is_relevant=0, group_id=NULL). No verse_context_group records are created for these terms. The patch notes field for DF-025 and DF-026 records includes the wrong-pool flag.

| DF | mti | Strongs | AVF reason |
|---|---|---|---|
| DF-001 | 620 | H3894 le.chum | Physical body references |
| DF-002 | 616 | H6371 pi.mah | Physical fat description |
| DF-003 | 622 | H8270 shor | Physical cord/body |
| DF-004 | 7097 | G0194 akratos | Wine concentration |
| DF-005 | 7071 | G0456 anoikodomeō | Physical building/restoration |
| DF-006 | 7098 | G2767 kerannumi | Physical mixing |
| DF-007 | 7069 | G3351 metoikizō | Physical deportation |
| DF-008 | 7073 | G3612 oikēma | Physical prison cell |
| DF-009 | 7074 | G3616 oikodespoteō | Household management role |
| DF-010 | 7075 | G3621 oikonomeō | Administrative stewardship |
| DF-011 | 7076 | G3626 oikouros | Domestic role |
| DF-012 | 7078 | G4039 perioikeō | Neighbours as people-group |
| DF-013 | 7011 | H0193A ul | Physical body (Psa 73:4) |
| DF-014 | 7012 | H0193B ul | Same verse as DF-013 |
| DF-015 | 7027 | H0436G e.lon | Topographical location |
| DF-016 | 6906 | H1434 ge.di.lim | Physical tassels/decoration |
| DF-017 | 7044 | H1680 da.vav | Physical sensation (wine) |
| DF-018 | 6887 | H2118 za.chach | Physical fastening of garments |
| DF-019 | 7067 | G3350 metoikesia | Genealogical chronological markers |
| DF-020 | 7024 | H0425L e.lah | Geographical location markers |
| DF-021 | 7019 | H0436H e.lon | Geographical/topographical |
| DF-022 | 7015 | H0361 e.lam | Architectural measurements (Eze 40) |
| DF-023 | 6902 | H1419J ga.dol | Great Sea — territorial marker |
| DF-024 | 7014 | H0352B a.yil | Temple doorpost measurements (Eze 40-41) |
| DF-025 | 7021 | H0352C a.yil | Wrong verse pool suspected |
| DF-026 | 7022 | H0352D a.yil | Wrong verse pool suspected |

---

## Session B Flags

No Session B flags document was raised for VCB-021. All flags were deferred flags (AVF findings). No Session B analytical insights require carry-forward.

---

*Handoff: wa-vcb-021-patch-handoff-v1-20260404.md | 2026-04-04*  
*Patch: wa-vcb-021-patch-v1-20260404.json*  
*Observations: wa-vcb-021-term-observations-v3.3-20260404.md*
