# Readiness Validation — R067 goodness

_Generated 2026-05-01T09:54:31Z_

## Verdict

**Overall: BLOCKED** — PASS=7  WARN=4  FAIL=4

Registry has at least one FAIL. Resolve the failing checks before handing off to Session B Stage 2.

## Checks

| ID | Check | Verdict | Detail |
|---|---|---|---|
| C01 | Schema version | ✓ PASS | schema_version = 3.17.0 |
| C02 | Engine audit clean | ✓ PASS | last_automation_run = 'AUDITED' |
| C03 | Phase 1 status | ✓ PASS | phase1_status = 'Complete' |
| C04 | Verse Context status | ✓ PASS | verse_context_status = 'Complete' |
| C05 | Dimension Review status | ✗ FAIL | dim_review_status = None; expected 'Complete' |
| C06 | Phase A prose captured | ✓ PASS | 6/6 sa_s1_d* rows present |
| C07 | Readiness output present | ✗ FAIL | missing readiness output for R067. Run `python scripts/_pilot_build_readiness_output_v2_20260426.py --registry 67`. |
| C08 | Term inventory health | ✓ PASS | 3 OWNER terms, all with ≥1 verse |
| C09 | All groups have dimensions | ✗ FAIL | 12 groups; 3 without dimension: ['884-007', '884-008', '884-009'] |
| C10 | All groups have anchors | ⚠ WARN | 3/12 groups without an anchor: ['884-007', '884-008', '884-009'] |
| C11 | Set-aside ratio | ⚠ WARN | 6 group(s) with set-aside > 90%: ['884-001 (142/22 = 645%)', '884-002 (142/37 = 384%)', '884-003 (142/35 = 406%)', '884-004 (142/33 = 430%)', '884-005 (142/16 = 888%)', '884-006 (142/21 = 676%)']. Possible VC drift; review Stage 2a. |
| C12 | Legacy-VC caveat | ✓ PASS | all 3 OWNER terms have vc_status set under v3 contracts |
| C13 | Dimension confidence | ⚠ WARN | dimension_confidence: (null): 3, KEYWORD_STRONG: 3, KEYWORD_WEAK: 6. No 'confirmed' assignments — Session B can promote during Stage 2. |
| C14 | No open DATA_ANOMALY_* findings | ✗ FAIL | 3 open DATA_ANOMALY_* findings: ['ANOMALY-067-001 (DATA_ANOMALY_FINDING_UNCITED)', 'ANOMALY-067-002 (DATA_ANOMALY_CITATION_GAP)', 'ANOMALY-067-068 (DATA_ANOMALY_QA_GAP)']. Resolve before handoff. |
| C15 | Researcher fields | ⚠ WARN | inference_note: absent; word_synopsis: absent. Researcher-authored fields are informational; absence is not blocking. |
