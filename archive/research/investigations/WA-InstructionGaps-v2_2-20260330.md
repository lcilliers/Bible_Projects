# WA-InstructionGaps-v2.2-20260330

**Project:** Framework B — Soul Word Analysis Programme
**Version:** 2.2
**Date:** 2026-03-30
**Purpose:** Complete unified gap register — updated with pipeline status review findings (G06-A through G06-F) and all instruction updates applied this session.
**Supersedes:** WA-InstructionGaps-v2.1-20260330.md
**Change note v2.2:** G06-B through G06-F resolved by instruction updates. G06-A resolved by documentation (RMG v5.7, DataPrep v5.6, patch_specification v1.5). New instruction updates applied: DataPrep v5.6, Analysis v5.6, Extraction v5.6, RMG v5.7, patch_specification v1.5, VerseContext v1.5, CC Instructions v3.2. SQL policy: G01/G08 note added to VerseContext v1.5 and CC Instructions v3.2. Status counts updated.
**Produced by:** Claude AI — WA session 2026-03-30

---

## How to Read This Register

### Inflection Point Definition

An inflection point (IP) is any point in the pipeline where data moves between the pipeline and the database — DB Read or DB Write.

**SQL policy:** SQL queries and scripts are Claude Code's responsibility. Claude AI instructions provide field names, table names, derivation rules, expected outcomes, and a clear handoff statement. Where these are present, gaps requiring explicit SQL are closed by policy.

A gap exists if the instruction document as it currently stands does not contain complete and correct information for that IP.

### Severity

| Code | Meaning |
|---|---|
| BLOCKING | Pipeline cannot proceed correctly without resolution |
| MISSING | Output will be incomplete or incorrect |
| AMBIGUOUS | Can proceed but action may be wrong |

### Gap Status

| Code | Meaning |
|---|---|
| CLOSED | Fully specified in current instruction documents |
| OPEN | Gap exists — instruction update pending or researcher decision needed |

---

## Complete Gap Status Register

| Gap ID | Stage | Description | Status | Governing document |
|---|---|---|---|---|
| G01 | Verse Context | Batch construction accumulation query — SQL policy applies | CLOSED | VerseContext v1.5 Section 5.2 — SQL policy statement added |
| G02 | Verse Context | Partial completion error rule | CLOSED | VerseContext v1.5 Section 6.1 |
| G03 | Verse Context | Revision documentation rule | CLOSED | VerseContext v1.5 Section 6.2 |
| G04 | Verse Context | Grouping criterion (materially different context) | CLOSED | VerseContext v1.5 Section 6.2 Step 3 |
| G05 | Verse Context | All-verses-fail error rule | CLOSED | VerseContext v1.5 Section 6.2 |
| G06 | Verse Context | Pipeline status lifecycle — escalated to G06-A through G06-F | See sub-gaps below | — |
| G06-A | All stages | Ready for Analysis unreachable for existing registries — pipeline diagram misaligned | CLOSED | RMG v5.7 Section 3.3; DataPrep v5.6 Section 4.2; patch_specification v1.5 Section 0 |
| G06-B | All stages | No failure patch on patch rejection | CLOSED | CC Instructions v3.2 Section 16; DataPrep v5.6 Section 8; Analysis v5.6 Section 12.4; Extraction v5.6 Sections 6.3 and 9 |
| G06-C | Analysis | No recovery if ANALYSIS patch rejected — detection at startup | CLOSED | Analysis v5.6 Section 4.4 (mid-pool detection); failure patch mechanism |
| G06-D | Analysis | No mid-pool interruption recovery | CLOSED | Analysis v5.6 Section 4.4; CC Instructions v3.2 Section 15.4 |
| G06-E | Verse Context | Re-extraction cascade on session_b_status undefined | CLOSED | CC Instructions v3.2 Section 15.2 (REPAIR-AUDITWORD-RERUN patch) |
| G06-F | Verse Context | No double-check after writing verse_context_status = Complete | CLOSED | VerseContext v1.5 Section 13.3 |
| G07 | Verse Context | Batch-level completion progress reporting | CLOSED | VerseContext v1.4 Section 13.4 — batch summary template |
| G08 | Verse Context | Batch JSON population — SQL policy applies | CLOSED | CC Instructions v3.2 Section 14.1 — SQL policy statement |
| G09 | Extraction | intra_pool column does not exist | CLOSED | Extraction v5.4 — finding_type = pool_observation |
| G10 | DataPrep | Pool membership for multi-cluster pools | CLOSED | DataPrep v5.5 Section 9.1; CC Instructions v3.1 Section 14.8 |
| G11 | DataPrep | pool_id values never defined | CLOSED | RMG v5.5 Section 7a |
| G12 | DataPrep | No-patch path leaves status unadvanced | CLOSED | DataPrep v5.4 Section 7.1 |
| G13 | DataPrep | update_mti_status vs update_evidential_status unexplained | CLOSED | DataPrep v5.5 Section 7.4 |
| G14 | Analysis | Simultaneous threshold undefined | CLOSED | Analysis v5.5 Section 4.2 — approx. 9 words |
| G15 | Analysis | Analysis patch contains bulk_update — remove | CLOSED | Analysis v5.4 Section 12 |
| G16 | Extraction | OWNER-only rule for update_evidential_status | CLOSED | Extraction v5.5 Section 6.1 Group A |
| G17 | Analysis | Quality flag handling in analysis undefined | CLOSED | Analysis v5.5 Section 7 Step 2 |
| G18 | Analysis | Root data absent from pool dataset | CLOSED | Analysis v5.5 Section 7 Step 4 |
| G19 | Analysis | pool_id format and valid values not defined | CLOSED | RMG v5.5 Section 7a |
| G20 | Extraction | intra_pool column (duplicate G09) | CLOSED | Same as G09 |
| G21 | Extraction | pool_observations not documented as file-only | CLOSED | Extraction v5.5 Section 8.1 |
| G22 | Extraction | Broken cross-reference to Reference Section 4.3 | CLOSED | Reference v5.3 Section 4.3 confirmed to exist |
| G23 | Extraction | word_registry.json source undefined | CLOSED | Extraction v5.4 Section 1 |
| G24 | Extraction | file_id selection rule unspecified | CLOSED | Extraction v5.4 Section 1 |
| G25 | Cross-doc | Two SESSIONB patches naming conflict | CLOSED | v5.3 naming fix; idempotency confirmed |
| G26 | Cross-doc | Analysis patch contains bulk_update | CLOSED | Analysis v5.4 Section 12 |
| G27 | Cross-doc | Session B Complete trigger undefined | CLOSED | Extraction v5.4 Section 9 |
| G28 | Cross-doc | update_mti_status XREF risk | CLOSED | DataPrep v5.5 Section 7.4 |
| G29 | Cross-doc | word_registry.dimensions not written | CLOSED | Extraction v5.5 Group F |
| G30 | Cross-doc | extracted_theological_anchor not handled | CLOSED | DataPrep v5.5 Section 6 |
| GAP-B | Cross-doc | inference_note redundant field | CLOSED | Reference v5.4 Section 13.1 |
| GAP-C | Cross-doc | wa_term_inventory.status_note redundant | CLOSED | Reference v5.4 Section 13.3 |
| GAP-E–J | Cross-doc | Engine-derived fields Phase 1 only | CLOSED | Reference v5.4 Section 13.1; RMG v5.6 Section 2 |
| GAP-K | Cross-doc | god_as_subject redundant | CLOSED | Reference v5.4 Section 13.3 |
| GAP-L | Cross-doc | somatic_link redundant | CLOSED | Reference v5.4 Section 13.3 |
| IP-PA-01a | Pool Assembly | Pre-construction check — SQL policy applies | CLOSED | CC Instructions v3.2 Section 14.8 |

---

## Summary Counts

| Status | Count |
|---|---|
| CLOSED | 42 |
| OPEN | 0 |
| **Total gaps** | **42** |

**All gaps resolved.** No BLOCKING items remain. The gratitude dry run may proceed.

---

## Document Version Registry — Current State

| Document | Latest version | Date |
|---|---|---|
| WA-InstructionGaps | v2.2 | 2026-03-30 |
| WA-PipelineStatusReview | v2 | 2026-03-30 |
| WA-VerseContext-Instruction | v1.5 | 2026-03-30 |
| WA-SessionB-DataPrep-Instruction | v5.6 | 2026-03-30 |
| WA-SessionB-Analysis-Instruction | v5.6 | 2026-03-30 |
| WA-SessionB-Extraction-Instruction | v5.6 | 2026-03-30 |
| WA-SessionB-ClaudeCode-Instructions | v3.2 | 2026-03-30 |
| WA-Reference | v5.4 | 2026-03-30 |
| WA-Registry-Management-Guide | v5.7 | 2026-03-30 |
| patch_specification | v1.5 | 2026-03-30 |

---

*WA-InstructionGaps-v2.2-20260330 | Supersedes v2.1-20260330 | 42 gaps: all closed | All BLOCKING gaps resolved | Dry run gate clear | No open items*
