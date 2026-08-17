# Session log — 2026-06-26 — RESET corpus sweep (first DB write) + exegesis-gate scoping

> **STARTUP BRIEF for next session.** Read this first, then the linked docs. The live method is the RESET ("characteristics → movements"); see memory `project_RESET_characteristics_to_movements_changeover` and CLAUDE.md §0 banner.

## 1. Where we are (one line)
The reset fidelity fixes + 7 new fields (baked read-only 2026-06-25) are now **written to the DB across the whole corpus**. The lexicals reflect the tuned engine. The researcher is **deliberating whether to do verse studies in Logos** because the mechanical lexical ceiling looks lower than hoped — decision pending on his return.

## 2. What this session did
1. **Resumed** from the 2026-06-25 state (engine tuned, read-only, not yet written).
2. **Exegesis-gate dry-count** (read-only) — corrected an inflated "48% gated" framing: it was mostly automatable distributed-reads + two routine UNRESOLVED fields (divine-involvement 20,441 + cause 10,448 = 96% of UNRESOLVED), NOT manual Logos. → `wa-exegesis-gate-drycount-v1-20260626.md`. Probe: `scripts/_probe_exegesis_gate_drycount_20260626.py`.
3. **RESET CORPUS SWEEP — first DB write** (researcher-directed). Wired the runner, ran live over all verses, validated clean. → `wa-reset-sweep-outcome-and-honest-assessment-v1-20260626.md`.

## 3. The sweep — facts (committed `298376f`)
- Runner `scripts/_apply_generate_ve_lexical_v2.py`: `VE_MAP` ve_nr **23–29** added (`from-source · instrument · purpose · quality-bearer · operation · isolable · discovery`); `narrate()` extended; faculty-map preservation added; STAMP→2026-06-26. Engine `scripts/_ve_engine_v2.py` narration extended.
- Live: **40,308 units · 452,885 ve_lexical rows · 31,908 l2_meaning regenerated · 0 errors.**
- **Validated clean:** read-API overlays all preserved (66,400); faculty-map preserved (26,386) + 2,819 v2 gap-fill, **0 duplicates**; integrity = before-start baseline exactly.
- **Backup:** `backups/bible_research_pre-reset-sweep_20260626.db` (pre-write). + yesterday's KEEP milestone + NAS.

## 4. OPEN ITEMS / next actions (in priority order)
1. **Researcher decision (his):** Logos-deep-study vs continue mechanical-scaffold + depth-on-demand. He will apply his mind on return. Do NOT pre-empt.
2. **Measure the genuine deep-study load** (offered, not yet built): a *figurative-candidate proxy* — somatic body-part term (hands/eyes/lips/mouth/neck) co-occurring with an inner-being term — to put a REAL number on verses needing deep treatment (the figurative/theologically-loaded triggers are mechanically invisible; the dry-count is a lower bound only).
3. **Confirm ve_nr 23–29 TIER assignments** — currently PROVISIONAL best-fit (from-source≈T2.9.1, instrument/operation≈T1.4.1, purpose≈T2.9.2, quality-bearer≈T1.1.4, isolable/discovery=meta/None). Needs researcher confirm or correction.
4. **Known mechanical ceiling (documented, not a regression):** faculty over-fires (kardia→all faculties); object mis-grabs on adjectives; unbound residue → discovery-lookout; figurative/distributed invisible. These are the design ceiling, now visible on real data.

## 5. Governance state
- Working tree: **clean, committed `298376f`**, but **NOT pushed** (was 3 ahead before; now more). Push on next session if desired.
- DB-concern tracker (living): `outputs/markdown/validation/wa-reset-rollout-db-concern-tracker-v1-20260625.md` — interval log row added 2026-06-26, concern register still empty.
- All-in-DB rule honoured; everything reversible (provenance-tagged, snapshot exists).

## 6. Key docs to open on resume
- This log → then `wa-reset-sweep-outcome-and-honest-assessment-v1-20260626.md` (the honest read for the decision).
- `wa-exegesis-gate-drycount-v1-20260626.md` (the corrected gate scoping).
- Method: `Workflow/Instructions/wa-lexical-analysis-rules-reset-v1-20260624.md` + `wa-synthesis-B-spec-reset-v1-20260624.md`.
- Milestone: `Workflow/methodology/wa-RESET-baseline-review-and-changeover-v1-20260625.md`.
