# Investigation: Mechanical Chapter Assembly from v1.8 DB

**Date:** 2026-04-30
**Test case:** R067 goodness — richest v1.8 capture in the DB (49 OBS findings + 167 v2 Q&A + 28 synthesis with chapter routing + 27 SD pointers).
**Question.** Under v1.8, Stage 2c was rewritten away from AI-authored prose chapters into structured synthesis findings. Session C still needs the 6 chapters. Can CC assemble them mechanically from DB content alone?

**Verdict:** **Strongly feasible.** Prototype Ch1 for R067 produced 26 KB / 134 lines of coherent chapter prose drawn entirely from DB rows. See [R067-goodness-ch1-assembled-prototype.md](R067-goodness-ch1-assembled-prototype.md).

---

## 1. Data sources available per chapter

The v1.8 DB carries every structured signal needed:

| Source | Table | Available for R067 |
|---|---|---:|
| Registry description, dimensions, cluster | `word_registry` | ✓ |
| Term inventory (OWNER + XREF) | `wa_term_inventory` + `mti_terms` | 3 OWNER + 42 XREF |
| Lexical sense data | `wa_meaning_parsed` + `wa_meaning_sense` | 3/3 OWNER terms parsed |
| VC groups + descriptions + anchors | `verse_context_group` + `verse_context` | 12 groups, 14 anchors |
| Anchor-verse text | `wa_verse_records.verse_text` | All 14 anchors |
| Anchor analysis notes | `verse_context.analysis_note` | 14/14 populated |
| Stage 2b Q&A bodies | `wa_finding_catalogue_links.session_b_note` (where finding_type='OBSERVATION') | 167 entries |
| Stage 2c synthesis findings | `wa_session_b_findings` (finding_type='SYNTHESIS_*') with `session_c_chapter` routing | 28 (all D outcome) |
| SD pointers | `wa_session_research_flags` (flag_code='SD_POINTER') | 27 open |
| Co-occurrence with other registries | computed via `wa_verse_records` cross-registry shared verses | computable |
| Shared anchor verses | computed via `verse_context.is_anchor` cross-registry | computable |
| Quality flags | `wa_data_quality_flags` | 118 |

## 2. Chapter-to-source mapping

Synthesis findings carry `session_c_chapter` routing tags (all 28 R067 entries are tagged Ch1, Ch2, Ch4, or Ch5). Q&A entries are routed via their `component_code` to chapter scope.

| Chapter | Primary sources | R067 instance counts |
|---|---|---:|
| **Ch1 — Meaning** | T1.1–T1.4 Q&A + T7.1 Q&A + SYN-INTRA-T1 + term inventory + registry description | 1 SYN-INTRA + ~24 Q&A entries |
| **Ch2 — How It Works** | T1.5, T1.6, T1.7, T2, T3, T4, T5 Q&A + 14 SYN-INTER tagged Ch2 + 4 SYN-INTRA tagged Ch2 | 18 synthesis + ~80 Q&A |
| **Ch3 — Verses** | Anchor verses (text + analysis_note) + Q&A entries with anchor_verses populated | 14 anchors + Q&A subset |
| **Ch4 — Language** | T7.1, T7.2 Q&A + T2.6–T2.8 (Body) + 6 SYN-INTER tagged Ch4 + SYN-INTRA-T7 + term/meaning data | 7 synthesis + ~16 Q&A + lexical |
| **Ch5 — Interrelationships** | T6 Q&A + 7 SYN-INTER tagged Ch5 + SYN-INTRA-T6 + co-occurrence + shared anchors | 8 synthesis + ~25 Q&A |
| **Ch6 — Open Questions** | All SD pointers ordered by priority | 27 pointers |

**Ch3 has no synthesis routing in R067** — synthesis didn't get tagged Ch3, by design (anchor-verse content is data-driven, not synthesis-derived). Ch3 is purely assembled from anchor verses + Q&A entries that name those verses in their `Anchor verses:` field.

## 3. Prototype results — R067 Chapter 1

Prototype script: [scripts/_tmp_assemble_chapter_prototype.py](../../../scripts/_tmp_assemble_chapter_prototype.py)

**Output:** [R067-goodness-ch1-assembled-prototype.md](R067-goodness-ch1-assembled-prototype.md) — 26,447 chars / 134 lines.

**Section structure produced:**

1. *What it is* — registry description (verbatim) + T1.2.3 working description
2. *Name and naming* — T1.1.1, T1.1.2, T1.1.3 Q&A bodies
3. *Kind* — T1.2.1, T1.2.2 Q&A bodies
4. *Boundary — what it is not* — T1.3.1, T1.3.2, T1.3.3 Q&A bodies
5. *Modes of operation* — T1.4.1, T1.4.2, T1.4.3 Q&A bodies
6. *Synthesis — what T1 reveals as a whole* — SYN-INTRA-067-001
7. *Lexical foundation* — OWNER term table + T7.1.1–T7.1.10 Q&A bodies

**Quality observations:**

- **Reads coherently as a chapter.** Each section is substantive (~600–1200 words per Q&A body) and OBS citations are preserved inline.
- **Citations intact.** `(OBS-067-OBS-001, OBS-067-OBS-026, OBS-067-OBS-036)`-style citations carry through from Q&A source — no reference rot.
- **No invented content.** Every paragraph traces to a finding row. No AI prose generation.
- **Reasonable length.** Comparable to the AI-authored R067 Ch1 in `prose_section.sb_s2c_ch1` (8,609 chars current v2). Assembled is longer because it shows all Q&A explicitly rather than synthesising 24 entries into one narrative.

## 4. Where assembled differs from AI-authored

| Dimension | AI-authored prose | DB-assembled prose |
|---|---|---|
| Length | Compact (~6–13 KB per chapter) | Longer (~25–35 KB per chapter projected) |
| Reading flow | Smooth narrative — topic sentences, transitions, weighted emphasis | Sectional — each Q&A is a self-contained unit; clear but academic |
| Editorial judgment | AI selects which observations matter most, weights them | All Q&A bodies surfaced, no editorial filter |
| Citation style | Inline with prose claim | One block of citations per Q&A entry |
| Coherence across sections | AI weaves cross-references | Sections stand independently |
| Risk of error | AI may misrepresent or extrapolate | Cannot exceed what DB rows say |

**Net assessment:** assembled prose is **denser and more comprehensive but less elegant**. It is the right substrate for Session C reading where completeness matters more than narrative arc. AI polish (a separate pass) could reduce length and improve flow, but the assembly alone is usable.

## 5. Recommended architecture

### Storage target

Write to `prose_section` rows with the existing section_type_ids (`sb_s2c_ch1`..`sb_s2c_ch6`):

- `author='claude_code'` (distinguishable from `'claude_ai'` AI-authored rows)
- `version` increments per regeneration (assembly is repeatable as DB evolves)
- `source_file` = obslog filename that drove the underlying captures
- Use the supersede chain: when a new assembly is run, mark the prior assembled row as `superseded_by_id`; AI-authored rows remain in history

This keeps Session C's existing read path intact — it reads `prose_section` rows for the registry under `sb_s2c_ch*` codes, picks the current row (`superseded_by_id IS NULL`), and uses it.

### Two-tier model

**Tier 1: Mechanical assembly** (the prototype shows this works).
- Pure DB → markdown.
- Re-runnable any time DB state changes (adds, supersedes, gap-fills).
- 80% of the value of AI-authored chapters.

**Tier 2: Optional AI polish** (later, if needed).
- AI reads the assembled chapter and the source data.
- Produces a polished narrative version.
- Marked `author='claude_ai_polish'` and supersedes the mechanical version.
- 20% lift on readability, but the assembly alone is sufficient for Session C.

### Run cadence

- After every v1.8 obslog capture (R067, R103, R111, future revisions): re-assemble all 6 chapters automatically.
- Idempotent: writing the same content again is a no-op (compare body hash before supersede).
- Output is immediate — no AI session needed.

## 6. What needs to be built

### Phase 1 — Full assembler (1 day's work)

Extend the Ch1 prototype to all 6 chapters:

| Chapter | Logic to add |
|---|---|
| Ch2 How It Works | T1.5–T1.7 + T2 + T3 + T4 + T5 Q&A grouped by component, with the 18 Ch2-tagged synthesis findings interleaved by tier pair |
| Ch3 Verses | Walk anchor verses canonically; for each: (verse text, analysis_note, group description, dimension assignment, all Q&A entries naming that verse in their anchor_verses) |
| Ch4 Language | T7.1 + T7.2 + T2.6–T2.8 Q&A, plus full meaning_parsed/wa_meaning_sense tables for each OWNER term, plus the 7 Ch4-tagged synthesis |
| Ch5 Interrelationships | T6 Q&A + co-occurrence top-N + shared-anchor table + 8 Ch5-tagged synthesis. Apply SB-7/SB-8 (correlation-signal-supported only). |
| Ch6 Open Questions | SD pointers ordered HIGH/MEDIUM/LOW + new RESEARCHER_DECISION items + the 28 synthesis findings as a tier-by-tier compendium |

### Phase 2 — Writer to `prose_section`

Wraps the assembler output, computes word counts, supersedes prior rows, writes the new rows with `author='claude_code'`. Same backup/transactional pattern as other capture scripts.

### Phase 3 — Driver

A single command: `python scripts/build_assembled_chapters.py --registry 67` produces and writes all 6 chapters. With `--all`, runs over every registry that has v1.8 captures.

## 7. Open design decisions for researcher review

These don't block Phase 1 but should be answered before Phase 2 writes to DB.

1. **Authorship marker**: `author='claude_code'` vs new value like `'claude_code_assembly'`?
2. **Supersede behaviour for words with prior AI-authored chapters** (R067 has 5 such): supersede the AI versions automatically, or keep them as the "current" and write assembled as alternative? My recommendation: supersede — assembled is more current with v1.8 data; AI versions remain as `superseded_by_id` history.
3. **Re-assembly trigger**: manual after each capture, or hook into the v1.8 capture script as a post-step?
4. **Polish pass**: when (if ever) does an AI polish run? Probably only when a registry reaches Session C scope.
5. **Synthesis routing for Ch3**: AI didn't route any of R067's 28 syntheses to Ch3. Should the assembler include selected SYN-INTER entries that name verse-level evidence in Ch3 anyway? Or keep Ch3 purely data-driven?

## 8. Recommendation

**Build Phase 1 + 2 now.** The prototype proves the concept. The full assembler is a few hundred lines of straightforward SQL + markdown formatting. It produces immediately useful Session C input for the 4 registries currently at v1.8 (R067, R103, R111 once captured, plus the 5 v1.7-style captures that have catalogue v2 data even if not synthesis).

**Defer Phase 3 polish** until Session C work begins on a specific registry. The assembled version will be sufficient until then.

The legacy AI-authored chapters in R067 (~41 KB across 5 chapters, written 2026-04-27 under v1.5) become superseded history when assembly writes the new rows. They're preserved in the `superseded_by_id` chain for audit.
