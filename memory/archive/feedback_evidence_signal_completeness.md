---
name: feedback_evidence_signal_completeness
description: "Never judge \"term has no evidence / safe to delete\" on mti_term_id; it is 98%-complete (5,249 legacy NULLs). Use term_id (99.99%) + verse_context. Read schema readiness notes before trusting a field as a signal."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: eae3184c-630b-48c2-9ac1-b0b494ccf689
---

When deciding whether a term carries live verse evidence, the reliable signal is the COMPLETE link, not the convenient one. In `wa_verse_records`: `term_id` (TEXT Strong's) is **99.99% complete**; `mti_term_id` (FK) is only **98% — 5,249 NULL from pre-MTI-linking imports** (documented in `docs/database-table-analysis.md` line 381). A term is evidence-free ONLY if empty under `term_id` AND `mti_term_id` AND active `verse_context`. Any one non-empty = it carries evidence.

**Why:** On 2026-06-01 I built an "evidence-safe" delete guard on `mti_term_id` alone. Terms whose live verses were legacy-imported (mti_term_id NULL) read as "0 verses / safe." Acting on that, today's writes (Stream C + B+D backfill) buried 36 real-evidence terms / 1,625 live verses, incl. G3958 *paschō* (researcher confirmed via STEP it was a real term). No verse rows were touched (reversible), but I also gave a false "2,131 empty terms, evidence-safe" assurance.

**How to apply:** (1) Before trusting ANY column as a signal, read its readiness/completeness note in the schema docs — a field flagged <100% must not be used as a completeness test. (2) Validate "empty," never assert it; check the complete signal first. (3) Give no "evidence-safe" assurance without that validation. (4) See [[feedback_integrity_and_intent_first]] — this is the same base-up-validation failure made concrete. Findings: `research/investigations/findings-deleted-terms-integrity-20260601.md`.
