# Draft — prog_instr_session_a v2

**Target section handle:** `prog_instr_session_a` (Chapter 6 — Instruction corpus)
**Supersedes:** v1 (draft, 220 words, written at initial ch6 seed)
**Author:** claude_code (session findings, 2026-04-23)
**Status:** draft — awaiting researcher review before patch construction

This draft captures the findings from the 2026-04-23 session about Session A's role, its data sources, its strict content boundary, and the emergence of the per-word `.md` renderer as the new input vehicle for Verse Context.

---

## Proposed heading

**Programme — Session A — extraction and the Phase 1 data layer**

## Proposed body

Session A is the first analytical stage of the programme pipeline. It governs the mechanical extraction of Hebrew and Greek term data from STEP Bible into the database, the reconciliation of that data through the `audit_word` process, the assembly of the complete per-word record that downstream stages consume, and the handoff to Verse Context. The stage is mechanical in character: it runs primarily through Claude Code operations against STEP data, produces the structured records that populate `wa_term_inventory`, `mti_terms`, `wa_verse_records`, and the supporting tables, and renders the per-word data into a self-contained form that the rest of the pipeline reads. Interpretive judgement does not enter this stage; all analytical work is downstream.

The data this stage produces has a strict content boundary. Session A carries **only what STEP Bible and the engine extract can generate deterministically** — Strong's numbers, glosses, transliterations, lexical entries, verse text, verse references, span confirmation, quality flags derived from counts and structural checks. Session A carries **none** of the products of later stages: no Verse Context classifications, no dimensional placements, no Session B findings, no Session D synthesis, no Session C narrative. This boundary is the foundation of every downstream stage's integrity. A classifier reading Session A data must not see the conclusions that a classifier is expected to reach; an analyst reading Session A data must not see the analytical frames they are expected to build. Session A is the evidence layer, not an interpretation of the evidence.

The programme has held three artefact representations of Session A data at different points in its history. The earliest, surviving as 44 JSON files in `data/imports/WA/Session_A_Data/`, was produced by Claude AI in the programme's first weeks before the extraction engine existed; those files are now legacy and preserved for provenance only. They have been superseded in operational use by the engine's `--export-word` output in `data/exports/STEP Extracts/`, which renders the database's per-word state as JSON and is the form the Verse Context batch builder reads from. The third and current representation — emerging as the database-as-memory principle is carried into Session A — is the per-word `.md` produced by `scripts/build_session_a_prose.py` (when implemented), which renders the same underlying data as a single self-contained markdown document. The `.md` form is the input Verse Context is moving towards: a human- and AI-readable document containing all the data for one word, composed under the six Session A prose handles (Word Summary, Meaning, Verses, Terms, Pointers, Questions), read without requiring the AI to query the database at classification time. The three representations are views onto the same state; the database is the canonical source, and the three forms differ only in audience and moment of use.

Session A is the entry point of the analytical pipeline. Every word the programme investigates passes through this stage before any interpretive work begins; the data Session A produces is the substrate that Verse Context, Dimension Review, Session B, Session C, and Session D all read from. The discipline of Session A — mechanical, boundary-respecting, reproducible from STEP and the database rather than from session memory — is what allows the downstream stages to be interpretive without being unsourced. Every finding of the programme traces back here.

**Filing note:** a Word document form of the earlier Session A instruction (`Session-A-Instruction-v8-final.docx`) exists in the Session_B active instruction folder as a historical artefact. It predates the move to markdown and the prose store, and is retained for provenance; it is not the operational reference. The operational reference for Session A is this section of the programme prose and the engine's behaviour itself.

---

## Word count (approx)

~520 words.

## Why this supersedes v1, not extends

The prose store's discipline is supersede-only for narrative prose (per wa-patch-instruction [current] §4.17). A new row with `version = 2`, `supersedes_id = {v1.id}`, `author = claude_code`, `status = draft` is inserted; the v1 row gets `superseded_by_id = {v2.id}` set. Both rows are retained.

## Next step

On researcher approval:

1. Construct a PROSE patch with one `supersede` operation on `prose_section` where the predecessor is the current `prog_instr_session_a` v1 row.
2. File: `data/imports/WA/Prose/patches/wa-prose-programme-instr-session-a-supersede-v2-20260423.json`.
3. Apply via `scripts/apply_session_patch.py`.
4. Regenerate programme prose extract (though the docx may be locked — `--also-markdown --include-body` is sufficient).

---

*Draft produced 2026-04-23 by Claude Code to record the 2026-04-23 session findings about Session A's role and data-source layering into the programme prose store.*
