# Readiness Validation — R111 mercy

_Generated 2026-04-28T06:25:26Z_

## Verdict

**Overall: READY** — PASS=12  WARN=3  FAIL=0

Registry has cleared all blocking checks. Cleared for handoff to Session B Stage 2 (per wa-sessionb-analysis-output [current]). WARN items are informational and should be addressed during Stage 2a where they affect findings.

## Checks

| ID | Check | Verdict | Detail |
|---|---|---|---|
| C01 | Schema version | ✓ PASS | schema_version = 3.17.0 |
| C02 | Engine audit clean | ✓ PASS | last_automation_run = 'AUDITED' |
| C03 | Phase 1 status | ✓ PASS | phase1_status = 'Complete' |
| C04 | Verse Context status | ✓ PASS | verse_context_status = 'Complete' |
| C05 | Dimension Review status | ✓ PASS | dim_review_status = 'Complete' (version: WA-DimensionReview-Instruction-v1.9-2026-04-09) |
| C06 | Phase A prose captured | ✓ PASS | 6/6 sa_s1_d* rows present |
| C07 | Readiness output present | ✓ PASS | latest .md: wa-111-mercy-readiness-output-v5-20260428.md; latest .json: wa-111-mercy-readiness-output-v5-20260428.json |
| C08 | Term inventory health | ✓ PASS | 25 OWNER terms, all with ≥1 verse |
| C09 | All groups have dimensions | ✓ PASS | 36/36 groups have dimension assignments |
| C10 | All groups have anchors | ✓ PASS | 36/36 groups have ≥1 anchor |
| C11 | Set-aside ratio | ⚠ WARN | 6 group(s) with set-aside > 90%: ['990-001 (156/7 = 2229%)', '990-002 (156/7 = 2229%)', '3169-002 (12/12 = 100%)', '3169-003 (12/9 = 133%)', '3173-002 (12/12 = 100%)', '3173-003 (12/9 = 133%)']. Possible VC drift; review Stage 2a. |
| C12 | Legacy-VC caveat | ✓ PASS | all 25 OWNER terms have vc_status set under v3 contracts |
| C13 | Dimension confidence | ⚠ WARN | dimension_confidence: CLAUDE_AI: 36. No 'confirmed' assignments — Session B can promote during Stage 2. |
| C14 | No open DATA_ANOMALY_* findings | ✓ PASS | no open DATA_ANOMALY_* findings for this registry |
| C15 | Researcher fields | ⚠ WARN | inference_note: absent; word_synopsis: absent. Researcher-authored fields are informational; absence is not blocking. |
