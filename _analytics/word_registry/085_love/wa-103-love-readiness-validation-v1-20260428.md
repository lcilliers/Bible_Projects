# Readiness Validation — R103 love

_Generated 2026-04-28T06:25:26Z_

## Verdict

**Overall: BLOCKED** — PASS=9  WARN=5  FAIL=1

Registry has at least one FAIL. Resolve the failing checks before handing off to Session B Stage 2.

## Checks

| ID | Check | Verdict | Detail |
|---|---|---|---|
| C01 | Schema version | ✓ PASS | schema_version = 3.17.0 |
| C02 | Engine audit clean | ✓ PASS | last_automation_run = 'AUDITED' |
| C03 | Phase 1 status | ✓ PASS | phase1_status = 'Complete' |
| C04 | Verse Context status | ✓ PASS | verse_context_status = 'Complete' |
| C05 | Dimension Review status | ✓ PASS | dim_review_status = 'Complete' (version: WA-DimensionReview-Instruction-v1.9-2026-04-09) |
| C06 | Phase A prose captured | ✓ PASS | 6/6 sa_s1_d* rows present |
| C07 | Readiness output present | ✓ PASS | latest .md: wa-103-love-readiness-output-v5-20260428.md; latest .json: wa-103-love-readiness-output-v5-20260428.json |
| C08 | Term inventory health | ⚠ WARN | 57 OWNER terms; 1 with 0 verses: ['H2898'] |
| C09 | All groups have dimensions | ✗ FAIL | 67 groups; 1 without dimension: ['2898-001'] |
| C10 | All groups have anchors | ⚠ WARN | 1/67 groups without an anchor: ['2898-001'] |
| C11 | Set-aside ratio | ⚠ WARN | 5 group(s) with set-aside > 90%: ['533-001 (47/11 = 427%)', '1609-001 (19/6 = 317%)', '1619-001 (5/2 = 250%)', '556-001 (1/1 = 100%)', '565-001 (1/1 = 100%)']. Possible VC drift; review Stage 2a. |
| C12 | Legacy-VC caveat | ✓ PASS | all 57 OWNER terms have vc_status set under v3 contracts |
| C13 | Dimension confidence | ⚠ WARN | dimension_confidence: (null): 1, CLAUDE_AI: 66. No 'confirmed' assignments — Session B can promote during Stage 2. |
| C14 | No open DATA_ANOMALY_* findings | ✓ PASS | no open DATA_ANOMALY_* findings for this registry |
| C15 | Researcher fields | ⚠ WARN | inference_note: absent; word_synopsis: absent. Researcher-authored fields are informational; absence is not blocking. |
