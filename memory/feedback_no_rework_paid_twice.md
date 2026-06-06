---
name: Don't pay twice for AI work that went wrong — re-align, don't re-architect
description: Methodology pivots should re-align existing data structures, not throw them away. Where the existing shape still fits the new model, reuse it. Where it doesn't, ignore it but don't replace it.
type: feedback
originSessionId: 0b9d95eb-ab3c-4fd3-9dd9-6341794c07de
---
When a methodology pivot reveals that earlier AI-driven work was flawed (e.g. registry-driven analysis, dimension review, Q&A findings), the response should be **re-alignment** of existing structures — not architectural replacement.

**Reasoning the researcher gave (2026-05-05):** *"some re-alignment is necessary, but a large part of what is already done is still part of the overall work, with some modifications. I don't fancy paying again for work that AI gone wrong in the first place."*

**The principle:**
- Cost is a real constraint. Rebuilding data in a new DB or new schema means re-doing ingest, re-validation, re-running embedding pipelines, etc.
- The canonical raw data (`wa_verse_records`, `mti_terms`, `wa_term_inventory`, root families, parsed meanings) is correct and already paid-for. Don't duplicate it.
- The legacy *analytical* output (verse_context, findings, dimensions) was paid-for in the wrong methodology, so its content is unreliable — but the *table shapes* may still fit a new methodology with adjustment.
- A separate DB or even a parallel `m_*` schema introduces synchronisation burden and signals "everything must be redone", which is wrong.

**How to apply:**
- Default to Option A (continue in current DB, untouched) unless there is a compelling structural reason to add new schema.
- Adapt existing tables' meaning under new methodology where the shape fits. E.g. `verse_context` can hold per-verse decisions under the new framework if we agree the columns map cleanly.
- Don't propose architectural changes ("new DB", "new schema layer") as the first response to methodological pivots. Propose minimal-touch re-alignments first.
- When existing data is wrong, leave it as historical archive and write fresh decisions to the same tables (or a small minimal addition) under new methodology — don't duplicate the structure.
- Reserve schema changes for cases where the new methodology genuinely cannot be expressed in the existing shape.

**Implication for the M-cluster work:**
- M-cluster identity and term assignment continues to live in the v6 JSON anchor (`outputs/markdown/wa-term-anchor-v6-20260504.json`) — no new tables for now.
- Term-level verse analysis can re-use `verse_context` (cleared/overwritten under new methodology) OR write to JSON outputs initially. Don't add new tables until the analysis itself proves the existing shape doesn't fit.
- Findings/pointers stay where they are — read-only reference, dipped into occasionally.
- The engine and audit pipeline stay alive for STEP-ingest only. No need to retire them.
