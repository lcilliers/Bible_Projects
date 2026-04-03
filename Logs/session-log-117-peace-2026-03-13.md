# Session Log — Registry 117 Peace
**Date:** 2026-03-13
**Programme:** Framework B Soul Word Analysis — Phase 1 Session A
**Specification:** Session A Instruction v7
**MTI input:** WA-MTI-framework-b-terms-2026-03-12.json (382 terms at session start for registry 078; 413 terms at start of 117)
**MTI output:** WA-MTI-framework-b-terms-2026-03-13.json (439 terms)

---

## Files Produced

| File | Description |
|------|-------------|
| WA-117-peace-data-part1-2026-03-13.json | Hebrew terms (72K) |
| WA-117-peace-data-part2-2026-03-13.json | Greek terms (24K) |
| WA-117-peace-data-part3-2026-03-13.json | Theological anchors (12K) |
| WA-MTI-framework-b-terms-2026-03-13.json | Updated MTI (439 terms) |

Note: Registry 078 hope was also completed in the same session. Its files (WA-078-hope-data-part1 and part2) were produced earlier and are captured in the previous transcript/compacted summary.

---

## Structure Decisions

**Three-part split** — first registry in the programme to use three parts:
- Part 1: Hebrew (16 canonical terms)
- Part 2: Greek (10 terms)
- Part 3: Theological Anchors (8 terms) — new part type, first use in programme

**Category:** null — deferred to Phase 2. "Relational/Social" was considered and rejected as too narrow.

---

## Key Decisions — Part 1 (Hebrew)

**sha.lom sub-glosses:** 6 separate word analysis blocks in Part 1 (H7965G parent + H7965L/J/K/I/H sub-glosses). All 240 verses assigned to sha.lom parent. Sub-entries are meaning-only blocks with no verse records. Check C soft exception pre-approved.

**sha.lam / sha.lem consolidation:** sha.lem (H7999A) is canonical; sha.lam is a sub-gloss meaning entry only, no separate verse record. Same Check C soft exception pattern. Both map to H7999A in MTI — sha.lam carries `status_note: "Consolidated sub-gloss of sha.lem (H7999A). No separate verse record."`

**da.mam (H1826):** XREF to patience 116 (owning registry). `also_used_in` updated to include 117 in previous session.

**she.lam (H8001):** THIN_DATA — no verses captured in STEP. Flagged for future follow-up. Also appears as XREF in Part 3.

**cha.resh (H2790B) / cha.rash (H2790A):** CONSOLIDATION_CANDIDATE — near-identical verse sets, both retained as separate entries pending Phase 2 review.

---

## Key Decisions — Part 2 (Greek)

**ēremos (G2263) / anesis (G0425):** Source file initially had word analysis blocks transposed. Researcher corrected and re-uploaded. Final JSON uses corrected data — both terms fully populated.

**eirēnē (G1515):** 91 NT occurrences total; 54 verses extracted from STEP source.

---

## Key Decisions — Part 3 (Theological Anchors)

**New part type:** Part 3 created specifically for divine-name terms surfaced by the sha.lom STEP related-words cluster. These sit at the Framework A/B boundary — not soul-words in the standard Framework B sense.

**New MTI status marker:** `extracted_theological_anchor` — first use in programme. All 8 Part 3 terms carry this status plus `phase2_flags: ["THEOLOGICAL_ANCHOR"]`.

**Verse extraction:** `verse_extraction_mode: anchor_only`. All verse arrays are empty. Anchor verse extraction deliberately deferred — not a data gap to chase. Researcher found it difficult to identify the right anchor verses, and the relevance of Part 3 only becomes apparent at synthesis stage when the Framework A/B intersection question is formally opened. MTI registry note records this explicitly.

**she.lam XREF:** she.lam appears in Part 3 as an XREF only — full extraction held in Part 1.

**Phase 2 synthesis question recorded:** If YHWH himself is peace (YHWH-Shalom), righteousness (YHWH-Tsidkenu), the jealous guardian (qan.na), the warrior who establishes peace (tsa.va) — what does this imply about the origin and nature of the corresponding soul characteristics in Framework B?

---

## MTI Updates — Registry 117

**Terms added:** 34 total
- 26 standard `extracted` terms (16 Hebrew + 10 Greek)
- 8 `extracted_theological_anchor` terms (Part 3)

**Strong's reconciled:** All provisional `PENDING-117-*` keys replaced with authoritative numbers from source JSONs.

**Registry note added to MTI metadata:** `registry_notes["117"]` — records Part 3 anchor verse deferral decision.

**MTI totals after session:**
- Total terms: 439
- Extracted: 343
- Theological anchors: 8
- Pending: 85

---

## Data Quality Flags — Summary

| Flag | Term | Note |
|------|------|------|
| THIN_DATA | she.lam (H8001) | No verses captured in STEP |
| THIN_DATA | ra.ga (H7280B) | 6 occurrences |
| THIN_DATA | has (H2013) | 8 occurrences |
| THIN_DATA | ge.mar (H1585) | 6 occurrences |
| THIN_DATA | eirēnikos (G1516) | 2 occurrences |
| THIN_DATA | eirēnopoieō (G1517) | 1 occurrence |
| THIN_DATA | ēremos (G2263) | 1 occurrence |
| CONSOLIDATION_CANDIDATE | cha.resh / cha.rash | Near-identical verse sets; both retained, Phase 2 review |
| ANCHOR_VERSES_NOT_CAPTURED | All Part 3 terms | Deliberately deferred — see above |

---

## Programme State at Session End

**Next word in sequence:** shame (registry number TBC at next session startup)

**Agreed sequence (remaining):** shame, envy, anxiety, joy, hope [done], peace [done], repentance, conscience, desire, wisdom, love

**Synthesis review milestone:** at 25 completed registries

**Session B:** Deliberately deferred until full dataset assembled.

**SQLite database build:** Planned for synthesis phase.
