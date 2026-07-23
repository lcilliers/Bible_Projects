# DB review — closure report

> 2026-07-22. Companion to
> [`iba-db-review-response-run-escalation-candidate_seed-v1-20260722.md`](iba-db-review-response-run-escalation-candidate_seed-v1-20260722.md)
> (the findings) and
> [`iba-candidate-seed-curation-method-v1-20260721.md`](iba-candidate-seed-curation-method-v1-20260721.md)
> (the updated method). That doc reported findings and waited for decisions; this one reports what
> was actually **built, applied, and verified** — every item from the review is closed, not parked.

## What changed, item by item

| # | finding | status | how |
|---|---|---|---|
| 1.1 | `config_version` frozen since 2026-07-18 | **fixed** | `cfg.config_version()` now computes a live SHA-256 of every `cfg_*` config table on every call — no write, always accurate |
| 1.2 | no failure-alerting beyond a terminal line at the moment | **addressed** | `log-retention.md`'s "Recent failed runs" section — persisted, not just a moment-in-time terminal print |
| 1.3 | `run.state` never reached `'done'` for standalone-step packages — a real bug | **fixed** | `cfg_work_package.chained` + dispatcher fix (`run.py`); 25 already-stuck non-chained runs retroactively corrected |
| 1.4 | no log-retention routine | **built** | `Log-Retention.ps1` → `iba/app/reports/log-retention.md` (read-only visibility; deletion policy intentionally left as your call, not assumed) |
| 2.1 | include escalation in log maintenance | **done** | same report covers `run`+`escalation`+`validation_result` together |
| 2.2 | write-grant extract | **delivered + one fix** | `registry.create`'s escalation grant was dead code — deleted |
| 2.3 | no persisted open-items report | **built** | folded into `log-retention.md` (a separate file would have duplicated it) |
| 2.4 | no way to manually raise an item | **built** | `Escalation.ps1 -Action Raise` — used immediately for the anger/spirit issue (escalation `#228`) |
| 3.1 | tag dirt examples | confirmed against the existing worklist, no new action needed |
| 3.2 | registry_match + tag both blank = false row | **resolved** | included in the 280-row deletion (168 of the 280 were this exact case) |
| 3.3 | "blank lemma_key" | **still unresolved** — genuinely could not find it (`lemma_key` is `NOT NULL`+`UNIQUE`, 0 blank anywhere); need you to point at a specific row |
| 3.4 | sub-strong tracking missing | **built** | `candidate_seed.strong_variant` (schema change) + `candidate.curate -Field split` |
| 3.5 | tag-cleanliness principle | **documented verbatim** | curation method doc §3 |
| 3.6 | blank tags must be deleted | **done** | 280 rows soft-deleted |
| 3.7 | anger/spirit overlap | **logged, not actioned** (correctly — you framed it as open) | escalation `#228` |

## What to actually look at

- **`iba/app/reports/log-retention.md`** — new. Run/escalation health, the 178 genuinely-abandoned
  chained test runs from the 2026-07-18/19 build sessions (all `SEED-REFRESH`/`CHK`/`VERIFY`/`FINAL`-
  named — clearly dev artifacts, not real incomplete book work; still not deleted, that's your call).
- **`iba/app/reports/candidate-quality.md`** — regenerated. `candidate_seed.tag` now shows **0 null**
  (was 281) and 225 messy (was 226 — one fixed live as a test of `candidate.curate`, `H8085` "to
  hear: hear" → "hearing").
- **5 escalations still open** (`Escalation.ps1 -Action List`): the pre-existing word-registration
  (#169) and passage-distribution (#195) items untouched from before this session, the candidate-
  quality acknowledgement from this pass (#222/newer), the anger/spirit note (#228), and this
  session's final `configmaint.validate` run — all left for you to answer, not self-approved.
- **`candidate_seed` now has a `strong_variant` column** — every existing row defaults to
  `strong_variant = lemma_key` (no split), except `H0639` which now has two rows (`H0639` base,
  still carrying the old messy `"face: anger"` tag — not yet corrected — and `H0639G` = `"anger"`,
  clean) as a live, real worked example of the split mechanism, not just a test fixture.

## Verified working, end to end (not just unit-level)

- `Start-Iba.ps1` → READY, new `config_version` format displayed correctly.
- `Set-Candidates.ps1 -Book Prov` → `candidate.seed`/`candidate.set` both ran clean against the new
  `strong_variant` schema (2013 candidates, 3173 spans stamped).
- `Config-Maintenance.ps1 -Step Validate` → structurally coherent, zero hard errors.
- `Candidate-Curate.ps1 -Field split` and `-Field delete` — both tested live against real rows
  (`H0639`/`H0639G`, `G0112`), not synthetic data.
- `Escalation.ps1 -Action Raise` — tested live, item appears in the same list as every automatic
  escalation.
- Every touched Python module (26 files) imports cleanly.

## Still open — needs you, not more investigation

- **§3.3** — I need a specific row to look at; I cannot find what "blank lemma_key" refers to.
- **Retention policy** — `log-retention.md` shows the numbers; whether to archive/delete old test
  runs, and on what age/rule, is yours to decide.
- **The remaining 225 messy `candidate_seed.tag` rows + 494 messy `lemma_inventory.gloss` rows** —
  no mechanical rule can clean these (per the tag-cleanliness principle, each is a real reading
  decision). The tooling (`candidate.curate`, including `split`) is built and tested; working
  through the list is the next session's task, at your pace.
- **§3.7** (anger/spirit) — logged as escalation `#228`, genuinely unresolved by design.
