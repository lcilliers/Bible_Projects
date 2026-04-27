# Obslog Parse — Validation Report — Registry 067

_Generated 2026-04-27T04:26:50Z_
_Source: data/imports/WA/Patches/wa-obslog-ro-067-goodness-anlys-v2-20260426.md_

## Status

**Parser status:** ✅ OK
**Issues:** 0  ·  **Warnings:** 0

## Counts (declared vs parsed)

| Category | Declared | Parsed | Match |
|---|---:|---:|---|
| qa_findings | — | 147 | — |
| sd_pointers | 10 | 10 | ✓ |
| observations | 48 | 49 | ⚠️ mismatch |
| chapters | — | 6 | — |
| gap_questions | — | 8 | — |
| ws_questions | — | 6 | — |
| review_notes | — | 41 | — |
| issues | — | 6 | — |

## Comparison against applied patches (regression test)

### `wa-067-goodness-patch-sessionb-findings-v1-20260427.json` — type `SESSIONB_FINDINGS` — 22 ops
- **patch_qa_finding_count:** 22
- **parser_qa_total:** 147
- **parser_qa_answered:** 111
- **patch_q_codes_sample:** []
- **note:** Patch contains 22 findings; parser sees 147 total Q&A. The patch is the ANSWERED subset; mismatch in raw count is expected.

### `wa-067-goodness-patch-sessionb-v1-20260427.json` — type `SESSIONB` — 1 ops
- **patch_target_status:** Analysis Complete
- **parser_target_status:** Analysis Complete
- **match:** True

### `wa-067-goodness-patch-vcsdpointers-v1-20260427.json` — type `VCSDPOINTERS` — 10 ops
- **patch_sd_pointer_count:** 0
- **parser_sd_pointer_count:** 10
- **both_match:** False
- **only_in_patch:** []
- **only_in_parser:** ['SP-001', 'SP-002', 'SP-003', 'SP-004', 'SP-005', 'SP-006', 'SP-007', 'SP-008', 'SP-009', 'SP-010']
- **sample_patch_seqs:** []

## Parser samples (first 3 per category)

### qa_findings

- `{"qa_seq": 1, "q_code": "Q001", "section": "Section 1 — Word Characteristic Summary", "question": "What is the structural disposition of the word — where does it originate?", "disposition": "ANSWERED", "answer": "Goodness originates in God — this is stated explicitly in the registry description (OBS…`
- `{"qa_seq": 2, "q_code": "Q002", "section": "Section 1 — Word Characteristic Summary", "question": "What determines whether the word is extended or withheld?", "disposition": "PARTIALLY ANSWERED", "answer": "The question fits goodness imperfectly — goodness as inner character is not primarily \"exten…`
- `{"qa_seq": 3, "q_code": "Q003", "section": "Section 1 — Word Characteristic Summary", "question": "What are the distinct modes of operation of the word in the inner being?", "disposition": "ANSWERED", "answer": "Nine distinct modes identified from the H2896A group structure (OBS-048 — DIM-67-001 res…`

### sd_pointers

- `{"seq": "SP-001", "target": "Registries 65, 103 — agathos/agathōsunē boundary; semantic split sustainability", "priority": "HIGH", "unit_raised": "2"}`
- `{"seq": "SP-002", "target": "Registry 103 — H2898 (tuv) 0 active verses in owner registry", "priority": "LOW", "unit_raised": "2"}`
- `{"seq": "SP-003", "target": "Registry 197 (authority) — 884-008 volitional idiom as driver of high co-occurrence", "priority": "MEDIUM", "unit_raised": "5"}`

### observations

- `{"seq": "OBS-001", "content": "Registry description names 3 axes: aesthetic/moral/relational; human goodness is derivative", "unit": "1"}`
- `{"seq": "OBS-002", "content": "Registry-level dimension = Moral/Conscience; groups show wider spread — tension noted", "unit": "1"}`
- `{"seq": "OBS-003", "content": "Domain G failure (no researcher narrative) — documentation gap only, not analytical", "unit": "1"}`

### chapters

- `{"chapter_n": 1, "title": "Word Characteristic Summary", "source_questions": "Q001–Q020 (Section 1 Q&A) and word-specific questions WS-001, WS-002.", "body": "**Source questions:** Q001–Q020 (Section 1 Q&A) and word-specific questions WS-001, WS-002.\n\n---\n\n### Chapter 1 Draft\n\n**Registry 067 —…`
- `{"chapter_n": 2, "title": "Word Impact Description", "source_questions": "Q021–Q041 (Section 2 Q&A) and word-specific question WS-003.", "body": "**Source questions:** Q021–Q041 (Section 2 Q&A) and word-specific question WS-003.\n\n---\n\n### Chapter 2 Draft\n\n**Registry 067 — Goodness**\n*Word Imp…`
- `{"chapter_n": 3, "title": "Annotated Verse Evidence", "source_questions": "Q042–Q085 (Section 3 Q&A) and word-specific question WS-004.", "body": "**Source questions:** Q042–Q085 (Section 3 Q&A) and word-specific question WS-004.\n**Anchor verses covered:** All 14 anchors across 12 groups (per Stage…`

### gap_questions

- `{"id": "GAP-S1-001", "section": "S1", "question": "Where the word has multiple distinct semantic modes, does the verse evidence reveal a unified inner logic that holds the modes together — or are they genuinely independent phenomena?", "rationale": "Section 1 questions assume a single-mode word. Goo…`
- `{"id": "GAP-S1-002", "section": "S1", "question": "Does the word carry a structural negative or absence form — and if so, does the negative form engage the same inner-being faculty as the positive?", "rationale": "The presence/absence structure (SBF-VCB013-001, OBS-048, OBS-049) is analytically sign…`
- `{"id": "GAP-S2-001", "section": "S2", "question": "Where the word has both a positive (presence) and negative (absence/not-word) register, what does the negative register reveal about the inner-being mechanisms of the positive?", "rationale": "The not-good group (884-006) and Rom 3:12 provide substa…`

### ws_questions

- `{"id": "WS-001", "registry_no": 67, "question": "Does the comparative wisdom idiom (Group 884-004 — better-than sayings) operate as a distinct mode of goodness, or is it a subset of moral character?", "answer": "It is analytically distinct — tov in 884-004 functions as a comparative operator that ra…`
- `{"id": "WS-002", "registry_no": 67, "question": "What is the analytical relationship between agathōsunē (G0019 — goodness) and chrēstotēs (G5544 — kindness) as co-OWNER terms of this registry? Are they aspects of a single characteristic or genuinely distinct inner-being phenomena sharing a registry?…`
- `{"id": "WS-003", "registry_no": 67, "question": "What does the Haman instance (Est 5:9 — tov-lev, glad of heart) reveal about the difference between genuine inner well-being and morally ungrounded inner pleasure?", "answer": "Haman's tov-lev is immediately destroyed by a single sight (Mordecai's ref…`
