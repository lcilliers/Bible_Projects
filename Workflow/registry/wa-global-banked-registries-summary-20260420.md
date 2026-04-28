# BANKED Registries — Formal Banking Summary — 2026-04-20

| Field | Value |
|---|---|
| Filename | wa-global-banked-registries-summary-20260420.md |
| Source sweeps | SWEEP-20260419-002 (r62) + SWEEP-20260420-001..004 (r35, r134, r206, r207) |
| Purpose | Formal record of the 5 registries banked on scorecard v2 criteria |
| Action | P (from programme control v1 queue) |
| Produced | 2026-04-20 |

---

## Banking criteria (scorecard v2)

A registry is BANKED when its readiness sweep returns:

- 0 Path 1 findings (no mechanical remediation needed)
- 0 Path 2 findings (no sub-process directive needed)
- 0 Path 4 findings (no researcher disposition required)
- `verse_context_status = Complete`
- `dim_review_status = Complete`

Programme-wide deferred items (`word_synopsis` researcher authoring, Session A extract not yet generated) are acceptable — they apply to all 213 registries, not any specific one.

---

## The 5 BANKED registries

| no | word | cluster | OWN | XREF | V | G | D | Sweep ID | Completion record |
|---:|---|---|---:|---:|---:|---:|---:|---|---|
| 35 | covetousness | C13 | 7 | 4 | 25 | 10 | 10 | SWEEP-20260420-001 | [wa-035-covetousness-sweep-completion-20260420.md](outputs/reports/wa-035-covetousness-sweep-completion-20260420.md) |
| 62 | fellowship | C17 | 13 | 0 | 89 | 19 | 19 | SWEEP-20260419-002 | [wa-062-fellowship-sweep-completion-20260419.md](outputs/reports/wa-062-fellowship-sweep-completion-20260419.md) |
| 134 | renewal | C21 | 7 | 3 | 22 | 5 | 5 | SWEEP-20260420-002 | [wa-134-renewal-sweep-completion-20260420.md](outputs/reports/wa-134-renewal-sweep-completion-20260420.md) |
| 206 | vulnerability | C22 | 17 | 1 | 128 | 34 | 34 | SWEEP-20260420-003 | [wa-206-vulnerability-sweep-completion-20260420.md](outputs/reports/wa-206-vulnerability-sweep-completion-20260420.md) |
| 207 | blindness (spiritual) | C21 | 7 | 2 | 103 | 12 | 12 | SWEEP-20260420-004 | [wa-207-blindness-sweep-completion-20260420.md](outputs/reports/wa-207-blindness-sweep-completion-20260420.md) |

**Totals across BANKED tier:**

| Metric | Total |
|---|---:|
| OWNER terms | 51 |
| XREF terms | 10 |
| Verse records | 367 |
| Groups | 80 |
| Dimensions | 80 |

---

## Cluster spread

5 BANKED across 4 clusters:

- **C13** (cognition / moral-cognitive) — 1 (covetousness)
- **C17** (covenantal disposition) — 1 (fellowship)
- **C21** (transformation lifecycle) — 2 (renewal, blindness)
- **C22** (meta-personhood / psychological structure) — 1 (vulnerability)

Clusters not yet represented in BANKED tier: C01, C02, C03, C04, C05, C06, C07, C08, C09, C10, C11, C12, C14, C15, C16, C18, C19, C20 (most of these are in SUBPROCESS_NEEDED — queued under macro step M2/M3).

---

## What "BANKED" unlocks

Once macro step M4 (Session A extract generator + `word_synopsis` authoring) completes, BANKED registries flow straight through to Stage 1 entry:

1. `generate_session_a_extract.py` produces Session A prose for the BANKED registry
2. Researcher authors `word_synopsis` (1–2 sentences)
3. `PREANALYSIS` gate opens immediately — 0 new data work needed
4. Registry advances into Session B pool processing

**These 5 registries are the first cohort that will demonstrate the full Session A → Session B → Session D → Session C workflow.**

---

## Common gate state

All 5 share:

- `verse_context_status = Complete`
- `dim_review_status = Complete`
- `session_b_status = Verse Context Reset` (post Q12 2026-04-19 — prior Session B work retained as historical `.md` for reference)
- 0 Path 1/2/4 findings (post OT-DBR-010 XREF join fix)
- Meaning parse coverage 100% (all OWNER terms have `wa_meaning_parsed`)
- 0 God-flagged / 0 Somatic-flagged terms in live data (would have shown in `mti_term_flags` if present)

---

## Common outstanding items (programme-wide — not registry-specific)

Both items apply to all 213 registries, not the 5 BANKED specifically:

| Item | OT reference | Unblocks |
|---|---|---|
| `word_synopsis` authored | (M21 column; researcher task) | Per-registry — trivial once prioritised |
| Session A extract generator not built | OT-DBR action S in control v1 | Programme-wide — single engineering effort |

---

## Banking signoff

All 5 registries banked on identical criteria (0 P1/P2/P4), all confirmed via:

1. Pilot run on live DB post OT-DBR-010 fix
2. Cross-check against scorecard v2 tier assignment (all 5 match)
3. Per-registry completion record produced and cross-linked here

**Action P closed — 2026-04-20.**

---

## Next actionable moves for these 5 registries

Independent of any other work, once M4 completes these 5 are first in line to pilot the full Session A → B → D → C analytical chain. Suggested ordering when M4 lands:

1. **r62 fellowship** (C17, 0 XREF) — cleanest, zero XREF complications; ideal first pilot
2. **r134 renewal** (C21, small) — second-cleanest; cross-cluster validation (C21)
3. **r35 covetousness** (C13, medium) — third pilot; different cluster (C13 cognition)
4. **r207 blindness (spiritual)** (C21, mid-size) — fourth; validates C21 cluster twice
5. **r206 vulnerability** (C22, largest) — fifth; largest BANKED — data-density validation

This ordering puts the smallest / simplest first and the largest last — the standard "pilot small, scale large" pattern.

---

*End of BANKED registries summary — 2026-04-20*
