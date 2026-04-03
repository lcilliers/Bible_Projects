# Session Log — Multiple Registries
**Date:** 2026-03-14
**Programme:** Framework B Soul Word Analysis — Phase 1 Session A
**Specification:** Session A Instruction v7
**MTI input:** WA-MTI-framework-b-terms-2026-03-13.json (439 terms at session start)
**MTI output:** WA-MTI-framework-b-terms-2026-03-14.json (517 terms at session end)

---

## Registries Completed This Session

| Registry | Word | Parts | Hebrew Terms | Greek Terms | Verses | Notes |
|----------|------|-------|-------------|------------|--------|-------|
| 135 | repentance | 1 | 9 canonical | — | 372 | Includes shuv sub-glosses and na.cham dual glosses |
| 026 | conscience | 1 | 1 | 1 | 29 | suneidēsis XREF to guilt 073 |
| 043 | desire | 2 | 33 | 25 | 614 | ne.phesh transferred to soul 182 |

**Also updated this session:**
- Registry 007 (anxiety): MTI advanced from pending to extracted (6 terms)

---

## Files Produced

| File | Description |
|------|-------------|
| WA-135-repentance-data-2026-03-14.json | Repentance JSON (72K) |
| WA-026-conscience-data-2026-03-14.json | Conscience JSON |
| WA-043-desire-data-part1-2026-03-14.json | Desire Part 1 Hebrew (381 verses) |
| WA-043-desire-data-part2-2026-03-14.json | Desire Part 2 Greek (233 verses) |
| WA-MTI-framework-b-terms-2026-03-14.json | Updated MTI (517 terms) |
| word_repentance.md | Repentance source file (produced and filled in session) |
| word_conscience.md | Conscience source file (produced and filled in session) |
| word_desire_Part1.md | Desire Part 1 source file |
| word_desire_Part2.md | Desire Part 2 source file |

---

## Key Decisions — Registry 135 Repentance

**Single file** — 9 canonical lemmas (under 12 threshold).

**na.cham (H5162G/H):** Two STEP glosses (comfort; relent) share one verse set. Two separate word analysis blocks in source; two MTI entries (H5162G, H5162H).

**shuv (H7725):** Five STEP glosses (again/J, recall/N, repent/O, return/I, turn-back) share 966-verse set. Separate word analysis blocks per gloss; five MTI sub-entries.

**metameleia:** STEP returned no analysis. Recorded as NO_WORD_ANALYSIS / NO_VERSES / THIN_DATA. Provisional MTI key retained.

**Strong's reconciled:** G0279→G0278 (ametamelētos); PENDING-metamellomai→G3338; H5162 split to H5162G/H; H7725 split to H7725J/N/O/I + unletter suffix.

**Specification note:** Source JSON produced under Session A v6 (anxiety 007 pre-existing). Repentance produced under v7. MTI updated to extracted for both.

---

## Key Decisions — Registry 026 Conscience

**Source list:** Missing Inner Being Words (first registry from this list in programme).

**Category:** Identity/Selfhood — first non-null category in programme. Question deferred: should prior registries be assigned categories retroactively? Deferred to synthesis review.

**XREF:** suneidēsis (G4893) owned by guilt 073. also_used_in updated to include 026.

**kil.yah (H3629):** Somatic-inner-being bridge term. Physical kidney = OT locus of emotion/affection/inner reflection (Psa 7:9, 16:7, 26:2, 73:21, 139:13; Jer 11:20, 17:10; Pro 23:16). The sacrificial verse set (Lev/Exo majority) and inner-being verse set (Psalms/Prophets) are functionally distinct — Phase 2 should treat as two subsets.

**suneidō (G4894):** 1Cor 4:4 (primary definitional citation) absent from STEP verse list. Three Acts verses extracted. Flagged THIN_DATA.

---

## Key Decisions — Registry 043 Desire

**Two-part language split:** 33 Hebrew terms (Part 1) + 25 Greek terms (Part 2).

**ne.phesh (H5315) transferred to soul (182):** Before Phase 2 began, ne.phesh ownership was transferred from desire 043 to the new soul registry 182. Desire Part 1 source file updated to mark it as XREF. Soul session run in separate chat; updated MTI returned and applied here.

**na.sa (H5375O) and da.var (H1697H) — no verses:** Researcher decision. Both terms have 659 and 1381 occurrences respectively across many sub-glosses; only one desire-relevant sub-gloss captured. Verse sets deliberately omitted due to volume and peripheral semantic fit. Phase 2 note recorded in data_quality_flags: if Session B analysis produces weak conclusions or unanswered questions regarding these terms, the researcher must conduct additional independent research before drawing synthesis-level conclusions.

**Strong's splits (Part 1):**
- H4261 (consolidated mach.mod/mach.mad) → H4262 (mach.mod) + H4261 (mach.mad) — confirmed as separate lemmas
- H2532 (consolidated cha.mu.dah/chem.dah) → H2530B (cha.mu.dah) + H2532A (chem.dah) — different verse sets confirmed
- H2836 (consolidated che.sheq/cha.shaq) → H2837 (che.sheq noun) + H2836A (to desire) + H2836B (to connect/fillet)

**Strong's corrections (Part 1):** H2654→H2655, H5689→H5690, H0014→H0015, H2530→H2530A, H6633→H6634, H5375→H5375O, H7602→H7602A, H0157→H0157G, H1696→H1697H

**Strong's corrections (Part 2):** G3713(orexis)→G3715, PENDING-epithumetes→G1938, PENDING-oregō confirmed G3713

**No STEP data:** epithumētos, potheinos, epithumēma — all return no STEP analysis. Strong's provisional for all three.

**a.hev (H0157G) boundary note:** Love/desire boundary term. 211 occurrences. Also_used_in for love registry (TBD) to be added when that registry is processed.

**cha.mal (H2550) — peripheral:** Spare/pity/compassion sense; peripheral to desire. Phase 2 should assess whether it contributes to the desire dataset.

**parakaleō (G3870) cross-registry:** Comfort/consolation senses overlap with grief (071) and sorrow (154).

---

## MTI State at Session End

| Metric | Value |
|--------|-------|
| Total terms | 517 |
| Extracted | 427 |
| Pending | 79 |
| Theological anchors | 8 |

**Pending breakdown (79 terms):** These are the remaining unprocessed registries in the programme sequence — wisdom, love, and other words not yet started. The 79 pending count is correct; no terms from completed registries remain pending.

**Registries with extracted terms in MTI:**
abomination (001), ambition (003), anger (004), anguish (005), anointing (006),
anxiety (007), conscience (026), desire (043), distress (051), envy (056),
fear (061), grief (071), guilt (073), hope (078), humility (080),
joy (097), patience (116), peace (117), pride (123), repentance (135),
shame (146), sorrow (154), wrath (178), soul (182)

---

## Programme Sequence Status

| Word | Registry | Status |
|------|----------|--------|
| shame | 146 | ✅ extracted |
| envy | 056 | ✅ extracted |
| anxiety | 007 | ✅ extracted (JSON pre-existing, MTI updated this session) |
| joy | 097 | ✅ extracted |
| hope | 078 | ✅ extracted |
| peace | 117 | ✅ extracted |
| repentance | 135 | ✅ extracted (this session) |
| conscience | 026 | ✅ extracted (this session) |
| desire | 043 | ✅ extracted (this session) |
| soul | 182 | ✅ extracted (separate chat) |
| wisdom | TBD | ❌ not started |
| love | TBD | ❌ not started |

**25-word synthesis milestone:** Not yet reached. Continuing data collection phase.

---

## Soft Flags Carried Forward

| Registry | Term | Flag | Note |
|----------|------|------|------|
| 135 | metameleia | THIN_DATA / NO_WORD_ANALYSIS | No STEP data; Strong's provisional |
| 135 | shuv turn-back | NO_WORD_ANALYSIS | Letter suffix not confirmed |
| 026 | suneidō G4894 | THIN_DATA | 1Cor 4:4 absent from verse list |
| 026 | kil.yah H3629 | ANOMALY_NOTE | Sacrificial vs inner-being verse subsets |
| 043 | na.sa H5375O | NO_VERSES | Phase 2 research note recorded |
| 043 | da.var H1697H | NO_VERSES | Phase 2 research note recorded |
| 043 | epithumētos | NO_WORD_ANALYSIS | No STEP data |
| 043 | potheinos G4658 | NO_WORD_ANALYSIS | No STEP data |
| 043 | epithumēma | NO_WORD_ANALYSIS | No STEP data |
| 043 | a.hev H0157G | ANOMALY_NOTE | Boundary with love registry |
| 043 | cha.mal H2550 | ANOMALY_NOTE | Peripheral semantic fit |

---

## Next Session

**Next word:** wisdom (registry TBD) or love (registry TBD) — to be confirmed at session startup.

**MTI to bring:** WA-MTI-framework-b-terms-2026-03-14.json (517 terms)

**Specification:** Session A Instruction v7
