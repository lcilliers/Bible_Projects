# Readiness Validation — R168 uprightness

_Generated 2026-05-02T15:25:06Z_

## Verdict

**Overall: READY** — PASS=11  WARN=4  FAIL=0

Registry has cleared all blocking checks. Cleared for handoff to Session B Stage 2 (per wa-sessionb-analysis-output [current]). WARN items are informational and should be addressed during Stage 2a where they affect findings.

## Checks

| ID | Check | Verdict | Detail |
|---|---|---|---|
| C01 | Schema version | ✓ PASS | schema_version = 3.17.0 |
| C02 | Engine audit clean | ✓ PASS | last_automation_run = 'AUDITED' |
| C03 | Phase 1 status | ✓ PASS | phase1_status = 'Complete' |
| C04 | Verse Context status | ✓ PASS | verse_context_status = 'Complete' |
| C05 | Dimension Review status | ✓ PASS | dim_review_status = 'Complete' (version: wa-dimensionreview-instruction-v3_3-20260418) |
| C06 | Phase A prose captured | ✓ PASS | 6/6 sa_s1_d* rows present |
| C07 | Readiness output present | ✓ PASS | latest .md: wa-168-uprightness-readiness-output-v6-20260502.md; latest .json: wa-168-uprightness-readiness-output-v6-20260502.json |
| C08 | Term inventory health | ✓ PASS | 8 OWNER terms, all with ≥1 verse |
| C09 | All groups have dimensions | ✓ PASS | 18/18 groups have dimension assignments |
| C10 | All groups have anchors | ✓ PASS | 18/18 groups have ≥1 anchor |
| C11 | Set-aside ratio | ⚠ WARN | 6 group(s) with set-aside > 90%: ['1211-003 (2/2 = 100%)', '1216-004 (6/6 = 100%)', '1216-006 (6/1 = 600%)', '7492-001 (17/3 = 567%)', '7492-002 (17/3 = 567%)', '7492-003 (17/1 = 1700%)']. Possible VC drift; review Stage 2a. |
| C12 | Legacy-VC caveat | ⚠ WARN | all 8 OWNER terms are legacy-VC (vc_status='not_done'). §K of readiness output instructs AI to flag any material dependence. Not blocking, but registry has not been re-classified under v3 contracts. |
| C13 | Dimension confidence | ⚠ WARN | dimension_confidence: CLAUDE_AI: 4, KEYWORD_STRONG: 2, KEYWORD_WEAK: 12. No 'confirmed' assignments — Session B can promote during Stage 2. |
| C14 | No open DATA_ANOMALY_* findings | ✓ PASS | no open DATA_ANOMALY_* findings for this registry |
| C15 | Researcher fields | ⚠ WARN | inference_note: absent; word_synopsis: absent. Researcher-authored fields are informational; absence is not blocking. |
