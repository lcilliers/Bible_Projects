---
name: project_morph_is_source_of_truth
description: GOVERNING (2026-06-15) - morph_code is the authoritative linguistic fact; stem/language/mode all DERIVE from it and re-derive when morph changes
metadata: 
  node_type: memory
  type: project
  originSessionId: 8a5e10ea-2d9d-4bb9-8ca3-fb979500309e
---

GOVERNING ARCHITECTURE (2026-06-15): `wa_verse_records.morph_code` (STEP/OSHB tagging of the actual text) is the **source of truth** for a term-in-verse's linguistics. Everything else is a **derivation** of it and must be re-derived whenever morph changes:
- `stem` (binyan) — stored derivation, parsed from morph_code.
- `language` (Hebrew/Aramaic/Greek) — was buggily derived from the **Strong's prefix** (`step_client.py:200`, `audit_word.py:778`), which is **blind to Aramaic** (Aramaic words carry H-numbers). Now MORPH-AUTHORITATIVE via `reconcile_language()` in `scripts/_apply_language_reconcile.py`, **wired into `_apply_morph_backfill.py`** so it re-derives after every morph write (self-healing, no revert). Backfill relabelled 121 terms Hebrew→Aramaic; language↔morph mismatches 866→1 (lone H3201 *yakhol*).
- **mode (#4)** — derived from morph_code+stem; not yet emitted as a finding. When emitted it joins the same trigger.

Canonical morph helpers: `scripts/analytics/morph_util.py` (`morph_language`/`morph_category`/`morph_stem`/`morph_readable`/`term_language`) — one place so checks/visuals stop re-bugging the H/A/Greek discrimination. Key gotchas it encodes: Greek `A-NSM`=adjective, `ADV`/`CONJ`/`PREP`/`PRT`=Greek indeclinables (NOT Aramaic); Aramaic binyanim differ from Hebrew (`q`=Peal not Qal).

Aramaic = Hebrew-script: `meaning_parser.py:238`, `audit.py:300`, `new_word.py:735` now use `in ("Hebrew","Aramaic")` (Aramaic was wrongly routing to the Greek parser).

OPEN (flagged, not plastered): ~1,430 text-less lexicon-only terms can't get Aramaic-vs-Hebrew from morph (no occurrences) — needs the STEP lexicon language tag, a separate lower-stakes job.

**Meta-feedback (reinforces [[feedback_check_governance_layers_not_just_pipeline]]):** when a field looks inconsistent, fix the DERIVATION at its source, not the symptom — the researcher caught me about to plaster (overwrite the field / just fix the checker) when the root was the prefix-derivation bug. Also: NEVER use AskUserQuestion for decisions ([[feedback_review_via_files_not_chat]]) — put options in the filed .md.
