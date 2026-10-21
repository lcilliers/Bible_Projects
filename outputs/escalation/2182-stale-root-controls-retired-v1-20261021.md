# #2182: Stale root controls retired (v1, 2026-10-21)

Escalation #2182 (option D of the #2179 review; an element of the IBA app reset, #2177). A file is retired
by moving it to its folder's `archive/` (the control map's history home), not by deleting it. It stays
findable for a deliberate read of a past state, and no routine reads it.

**How "stale" was decided:** a file was retired only if nothing live names it. "Live" means:
- every text column of every active rule-category `cfg_*` table
- the context, resolution and title of every open or parked escalation
- every `.py` and `.ps1` under `iba/app/` (migrations excluded)
- the `.claude/` commands and hooks
- CLAUDE.md, CHARTER.md, GOVERNANCE.md and USER-GUIDE.md

## 1. Root files

| File | Now | Why |
|---|---|---|
| `README.md` | `archive/docs/readme-md-history-to-20261021.md` | Described the Google Drive setup, schema v3.1.0, engine 1.0.0; nothing read it |
| `tasks.md` | `archive/docs/tasks-md-history-to-20261021.md` | A second task ledger beside the escalation table (rule 40); 27 open tasks, last changed 2026-07-14 (§4) |

## 2. `Workflow/Instructions/`: 19 files to `archive/`, 8 kept

Kept (each named by config, code or another kept file): `WA-inner-being-narrative-guidance-v1-2026-07-28.md`, `WA-inner-being-narrative-hard-constraints-v1-2026-07-30.md`, `WA-interpretation-questions-v1.4-2026-08-02.md`, `WA-passage-read-guidance-v1.5-2026-08-02.md`, `wa-inner-being-narrative-style-guide-v2-20261001.md`, `wa-operational-governance-v1_0-20260614.md`, `wa-verse-analysis-method-v1-20260702.md`, `wa-verse-reading-by-role-guide-v2-20261019.md`.

Retired, including all five named `AUTHORITATIVE` (the July pre-IBA pipeline):

- `01b-VE-field-reliability-and-rules.md`
- `01c-T2-treatment-and-API-governance.md`
- `WA-analytic-input-spec-2.0-2026-07-13.md`
- `WA-projection-spec-1.2-2026-07-13.md`
- `wa-book-lexical-readiness-assessment-AUTHORITATIVE-v3-20260714.md`
- `wa-characteristic-role-lexical-cycle-authoritative-v1-20260708.md`
- `wa-claudecode-instruction-v4_5-20260514.md`
- `wa-corrected-charac-arc-reread-repeatable-process-v1-20260711.md`
- `wa-db-integrity-definition-authoritative-v1-20260711.md`
- `wa-directive-instruction-v1_4-20260506.md`
- `wa-gate1-span-orphan-audit-method-rule-v1-20260705.md`
- `wa-narrative-style-instruction-v1-20260702.md`
- `wa-passage-completeness-rule-v2-20260708.md`
- `wa-patch-instruction-v2_11-20260507.md`
- `wa-per-book-corrective-method-authoritative-v1-20260707.md`
- `wa-reread-operating-model-cadence-v2-20260714.md`
- `wa-synthesis-B-spec-reset-v1-20260624.md`
- `wa-term-add-update-AUTHORITATIVE-pipeline-v1-20260711.md`
- `wa-two-narrative-rollout-method-v1-20260712.md`

The style guide's list of the sources it carried forward now points at the archived copy of `wa-narrative-style-instruction-v1-20260702.md`.

## 3. `iba/docs/`: 169 files to `archive/`, 35 kept

Retired: the working files of completed, closed or superseded escalations, and old plans and proposals
(July–September) that nothing live names. Superseded versions are among them, e.g. prose-change-log
proposals v1–v3 beside design v9. Kept: the files an open or parked escalation, a config row, code or
a live document names, and the two Excel tool worksheets. The full list is in git (`git log --stat`
for this commit) and in the file manifest (`research/discovery/file-manifest-v8-20261021.md`).

## 4. The 27 open tasks of `tasks.md`: for your decision

All 27 belong to pipelines that have since been retired or shelved:
- the projection re-reads of July (the VE dimensions `effect(111)`, `type(102)`, `locus(116)`)
- Verse Context, Session B and the Phase A/B prose plans (April–May)

The old study method was closed on 2026-08-03, and full-corpus AI verse analysis was shelved on 2026-09-24.
**Proposed:** withdraw all 27 as overtaken. The list stays in the archived file. If any is still wanted,
name it and it becomes an escalation.

1. Phase-2 EFFECT read — Psalms (then bake into every book read). effect(111) currently ships derivation-grade (97.7% NONE = a floor, not measured silenc…
2. type(102) reader-drift — retire from analytical use OR re-read to a fixed controlled vocab in one pass (currently records reading-order, not text). Hi…
3. locus(116) Ps 1–25 re-read — break the blanket 100% internal:ib-state early-reading convention.
4. DQ-05 direction-consistency audit — seat-word + give-thanks subset (Psa 86:12 vs 111:1 tag inward vs toward-god on identical fields; ~20% on subset).
5. (consider) Vehicle-node materialisation — simile/metaphor vehicles are carried as readable text + 5 span-edges; most vehicle nouns are not indexed IB …
6. Re-run content-validity on every re-read book (not just Psalms/Proverbs) — the drift/domain/tag failures are likely systemic (source(103)/effect(111) …
7. Decide type(102) disposition — the confirmed reader-drift dimension. Retire from analysis, or re-read to a fixed vocab in one pass. Blocks any type-ba…
8. Enrich programme prose with the inputs and outcomes of methodology review sessions
9. PhaseAProse: generate phase A prose — instruction filed [Workflow/Instructions/wa-sessiona-prose-instruction-v10-20260427.md](Workflow/Instructions/wa…
10. PhaseBVerseContext: Run through all verse context again — VC-7 pilot done (renewal); VC-8 done (yearning, treachery, jealousy, righteousness — malice …
11. VC corrective action strategy — avoid full re-classification of the 1,800-term legacy-Complete bucket; rely on signal-targeted revision and pinpoint V…
12. VC revision-ledger build (Step 1 of strategy §5) — extract per-term routing outcomes from VCB-7..11 patches + DB; score univariate predictors (group c…
13. VCCONFIRM patch-type design (Step 5 of strategy) — gated on ≥1 reliable predictor surfacing in the ledger. Will need wa-patch-instruction §15 entry + …
14. Outlier-1 — Extraction-anomaly residue, 6 terms. Function-word / pronoun / animal terms lumped into 1 catch-all group across legacy-Complete registrie…
15. Outlier-2 — Listen (213) registry coherence. Four terms ≥80% setaside including the literal "to listen to" verb (G1522, 100% setaside). Possible regis…
16. Outlier-3 — Integrity (92) H8549G unblemished root-bleed. 45 of 51 verses setaside (88%); registry-level setaside 73%. Likely root-bleed from physical…
17. VC programme roll-out: 174 legacy-Complete registries + 6 reset registries (compassion, fellowship, forgiveness, grace, love, mercy) all need processi…
18. VC-Prose-v4 (post-pilot): supersede proginstrversecontext v3 → v4 after VC-9/VC-10 confirms the contracts at scale. Minimal addition — one governance-…
19. Applicator hardening (extend to Session B/D paths): mtiterms match-update, waterminventory, watermphase2flags, wordregistry match-update, waruleregist…
20. Normalise out-of-vocab setasidereason values: "Material goods/property -- set aside" (17 rows) and "avfhomograph" (1 row) → controlled vocab via REPAI…
21. Audit preserved-with-notes versecontext rows (4,366 active rows where isrelevant=0 AND setasidereason IS NULL AND notes IS NOT NULL survived M39). Sam…
22. VScode: reset folder destinations for prose and references
23. Worddata: Archive after Phase A prose is done.
24. PhaseBDimensions: Revisit all dimensions not yet through second round
25. PhaseBAnalysisReadiness: Run all words through readiness
26. PhaseBProse:  Prepare prose ready for analysis
27. PhaseBOutput:  Prepare output and update database for all words.

## 5. Permission settings: for you to change

These are Claude Code permission settings. Changing them is yours to do, not mine.

- **`.claude/settings.json`, `permissions.allow`:** two entries for run `RUN-20260722_065351_662-CONFIGMAINT` (an `AnswerRun` and a `Validate`). That run has no open escalation; the entries allow nothing in use and can be removed.
- **`~/.claude/settings.json`, `autoMode`:**
  - the allow line for `python -m engine.engine --report/--db-status/--export-word`
  - the soft-deny lines for `python -m engine.engine --migrate` and `scripts/apply_session_patch.py`

  These name the engine and the patch applier, superseded since 2026-08-17 (the files still exist). Keep the deny lines if you want the old tools still blocked; the allow line can go.
- **`.claude/settings.local.json`:** allows `Bash(*)`, `Write` and `Edit` outright. That isn't stale; I note it only because it overrides narrower allows elsewhere.

## 6. Not retired here

- `iba/config/README.md`: the second configurator, a known fork (CHARTER §3, GOVERNANCE §6), for its own decision.
- `docs/interaction-preferences.md` and `docs/file-organisation-rules.md`: they restate rules held in config (classes `chat`, `filing`). That is the duplication E (#2184) removes.
- `iba/app/tools/temp_*` (15 one-off scripts, e.g. `temp_2110_test_plan_run.py` for the completed #2110): `governance.redundancy_archiving` wants them archived; G (#2186) checks for this at close.
