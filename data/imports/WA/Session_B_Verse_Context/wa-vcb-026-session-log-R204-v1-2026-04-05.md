# wa-vcb-026-session-log-R204-v1-2026-04-05

**Framework B — Soul Word Analysis Programme**
**Session Log — VCB-026 | Registry 204 (name) | Session Close**
**Date:** 2026-04-05
**Governing instruction:** WA-VerseContext-Instruction-v2.4-20260403.md
**Observations file at session close:** wa-vcb-026-term-observations-v1.2-2026-04-05.md

---

## Session Summary

Batch VCB-026 — single registry (204, name). All three terms classified. Patch produced and validated. Session closed.

---

## Terms Classified

| Term | mti | Strongs | Verses | Relevant | Set Aside | Groups | Anchors |
|------|-----|---------|--------|----------|-----------|--------|---------|
| name | 1366 | H8034 shem | 364 | 224 | 140 | 5 | 10 |
| name | 1367 | G3686 onoma | 120 | 90 | 30 | 5 | 8 |
| to name | 7352 | G3687 onomazō | 11 | 10 | 1 | 4 | 5 |
| **Total** | | | **495** | **323** | **172** | **14** | **23** |

---

## Groups Established

H8034 shem and G3686 onoma share the same five-group structure. G3687 onomazō uses four groups (G1–G4; no G5 material).

| Group code (shem / onoma / onomazō) | Context description |
|-------------------------------------|---------------------|
| 1366-001 / 1367-001 / 7352-001 | Divine name as embodied self-disclosure of God's character, nature, and presence |
| 1366-002 / 1367-002 / 7352-002 | Human inner orientation toward the divine name — calling upon, trusting, praising, fearing, honouring, desecrating |
| 1366-003 / 1367-003 / 7352-003 | Person's name as bearer of character, moral quality, reputation, and identity |
| 1366-004 / 1367-004 / 7352-004 | Theologically weighted naming act — name given or changed expresses inner state, divine declaration, or identity transformation |
| 1366-005 / 1367-005 | Name as renown, social standing, and fame |

**Group consolidation review:** Five groups emerged for H8034 shem. Per §6.2 Step 3, a pause and consolidation assessment was conducted before proceeding. All five groups were judged warranted: G1 and G2 are opposite poles of the name-relationship (what the divine name discloses vs how the human orients toward it); G3 and G5 are materially different (inner character vs external standing); G4 concerns the act of naming rather than the name-as-thing. No consolidation was indicated.

---

## Anchor Designations

### H8034 shem (mti:1366)
| Group | Anchor 1 | Anchor 2 |
|-------|----------|----------|
| 1366-001 | Isa 57:15 (vid:54926) | Psa 8:1 (vid:55100) |
| 1366-002 | Psa 9:10 (vid:55110) | Isa 26:8 (vid:54900) |
| 1366-003 | Pro 22:1 (vid:55055) | Ecc 7:1 (vid:54818) |
| 1366-004 | Gen 17:5 (vid:54843) | Gen 29:32 (vid:54872) |
| 1366-005 | Gen 11:4 (vid:54832) | Gen 12:2 (vid:54834) |

### G3686 onoma (mti:1367)
| Group | Anchor 1 | Anchor 2 |
|-------|----------|----------|
| 1367-001 | Phili 2:9 (vid:55223) | 1Ti 6:1 (vid:55146) |
| 1367-002 | 1Jo 3:23 (vid:55142) | Mat 6:9 (vid:55220) |
| 1367-003 | Rev 3:1 (vid:55242) | Luk 10:20 (vid:55172) |
| 1367-004 | Mat 1:21 (vid:55203) | Rev 2:17 (vid:55240) |
| 1367-005 | Mar 6:14 (vid:55198) | — |

### G3687 onomazō (mti:7352)
| Group | Anchor 1 | Anchor 2 |
|-------|----------|----------|
| 7352-001 | Eph 1:21 (vid:231113) | — |
| 7352-002 | 2Ti 2:19 (vid:231111) | — |
| 7352-003 | 1Cor 5:11 (vid:231110) | — |
| 7352-004 | Luk 6:13 (vid:231116) | Eph 3:15 (vid:231114) |

---

## Flags and Decisions

**No flags requiring researcher decision were raised.**

One extract anomaly noted and set aside without decision required:
- **vid:231109** (1Cor 5:1, G3687 onomazō): target_word rendered as "tolerated" — onomazō not visible in the ESV rendering; verse set aside as target mismatch. No inner-being classification possible from the rendered text.

**Borderline retained (3 verses, all H8034 shem, all G2):**
- vid:54789 (1Sa 25:5) — "greet him in my name": name as extension of personal presence; retained per §3.3
- vid:54790 (1Sa 25:9) — "in the name of David": same pattern
- vid:55051 (Num 6:27) — "put my name upon the people, and I will bless them": priestly blessing through divine name; retained

---

## Patch Summary

**File:** wa-vcb-026-patch-v1-2026-04-05.json
**Total operations:** 509
- Group inserts: 14
- Verse context inserts: 495
- Relevant verses: 323
- Set aside verses: 172
- Anchor verses: 23
- Related verses: 300
- Dual-context verses: 0
- Revisions to prior: 0

**Pre-submission validation:** All 495 verse_record_ids accounted for exactly once per term. No missing, no duplicate assignments. R4 confirmed for all three terms (minimum one anchor per term). R1–R3 rules satisfied throughout.

---

## Observations File Version History

| Version | Content added |
|---------|--------------|
| v1.0 | H8034 shem classification complete |
| v1.1 | G3686 onoma classification appended |
| v1.2 | G3687 onomazō classification appended — final version |

---

## Outputs Produced This Session

| File | Description |
|------|-------------|
| wa-vcb-026-term-observations-v1.2-2026-04-05.md | Classification observations — all three terms, final version |
| wa-vcb-026-patch-v1-2026-04-05.json | VERSECONTEXT patch — 509 operations, ready for Claude Code |
| wa-vcb-026-session-log-R204-v1-2026-04-05.md | This session log |

---

## Next Steps for Claude Code

1. Apply patch `wa-vcb-026-patch-v1-2026-04-05.json` to `bible_research.db`
2. Run XREF coverage check for Registry 204 — confirm all XREF terms for registry 204 have OWNER classifications resolved
3. Run completion check — confirm all OWNER terms in registry 204 have verse_context records
4. If complete: advance `verse_context_status` to Complete for Registry 204
5. Re-export full word JSON: `wa-204-name-extract-{date}.json`
6. DataPrep gate for Registry 204 opens on re-export

---

## Programme State at Session Close

- VCB-026: Complete (all terms classified, patch produced)
- Registry 204 (name): Patch delivered — pending Claude Code application and completion check
- Previous completion count: 81/181 registries Complete
- After successful patch application: 82/181 registries Complete (pending Claude Code confirmation)

