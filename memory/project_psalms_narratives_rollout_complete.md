---
name: project_psalms_narratives_rollout_complete
description: Psalms two-narrative rollout COMPLETE 46/46; verifier script; DB-load + cross-term open loops; base-source 112/116 transposition finding.
metadata:
  type: project
---

★ LIVE (2026-07-12). The **Psalms two-narrative rollout is COMPLETE — all 46 families**, 2,048 narrative records total (this session added the final 12, ~481 records).

**What it is:** per family base source (`verse-analysis/psalms/_base-sources/psalms__<fam>.json`), one record per **anchor reading** (a `lexicals[]` row without `same_as`/`duplicate`; duplicates cross-ref'd in `recurrences`) carrying an analytical `narrative` (walks dimensions 101–116 incl. absences; cites verses/ve_lexical) + a plain-reader `story` (ZERO study jargon) + `citations`/`recurrences`/`variation_note`. Output: `_narratives/psalms__<fam>__narratives.json` + `.md`. **The contract is embedded in each base source at `meta.WORK_CONTRACT`** (record shape, directives 1–10, completeness) — no external prompt needed. Voice = [[project_lexical_prose_endpoint_and_ve_lexical_phase1]] / `wa-narrative-style-instruction-v1-20260702.md`.

**Process (proven, reusable) — PRESERVED as an instruction for all remaining books: `Workflow/Instructions/wa-two-narrative-rollout-method-v1-20260712.md`.** 3 stages: A) base source (script `_produce_family_passage_base_source_v2_20260712.py --book <id> --family <slug>`, takes `--book`; two Psalms-hardcoded lines to parameterise per book) → B) one subagent per family obeying its base source's WORK_CONTRACT (prompt MUST say "ONE worker, do NOT spawn agents"; recommend **Sonnet** not Opus for cost) → C) render `scripts/_render_narratives_to_md_20260712.py --family <fam>` + gate `scripts/_check_family_narratives_20260712.py --family <fam>` (or `--all`) = anchor coverage + both narratives + citations + count==distinct_readings + story jargon gate, then commit incrementally. Gate passed 46/46.

**Lesson:** for the largest families, the worker prompt MUST say "you are ONE worker, do NOT spawn or wait for other agents" — the first trust-refuge agent's context corrupted, hallucinated a coordinator role, and spawned 6 rogue fragment sub-subagents; a fresh clean agent produced the correct file.

**Open loops:** (1) **narratives → DB** — WORK_CONTRACT names the DB as ultimate destination (JSON=transport, md=view); the patch-to-DB step is outstanding for all 46. (2) **cross-term / cohabitation layer** — single-family stories done; the cross-term story (style §3b) is the natural next phase. (3) **base-source coupling(112)/locus(116) transposition** — verified 666/2168 rows, all 46 families, onset at Psa 89; narratives unaffected (agents read by content) but base-source/DB needs a fix + regen. Full write-up: `outputs/markdown/validation/wa-psalms-base-source-coupling-locus-transposition-v1-20260712.md`. Session log: `Workflow/Sessionlogs/wa-session-log-20260712-psalms-narratives-rollout-complete.md`.
