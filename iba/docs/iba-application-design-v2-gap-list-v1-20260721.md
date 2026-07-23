# IBA Application Design v2 — Gap List (v1)

> **Purpose:** Step 2 of the original three-step instruction ("list the gaps between the current build
> and the approved design"), now run against `iba-application-design-v2-20260721.md`. Every item below
> is pulled directly from that document — nothing is re-derived, re-judged, or invented; each row cites
> its source section. **Phase 1 (Data Layer) is the actionable list** — these are the gaps to close now.
> **Phase 2 (Analytic Layer) is not in scope until the §13 gate opens** — it is listed only for
> completeness, as one line per area, since virtually everything there is "not built" by design rather
> than a gap in an existing build.

---

## Part 1 — Phase 1 (Data Layer): full gap list

### Already-directed build todos (§A8 — the four items you've already scoped)

| # | gap | source | directed fix |
|---|---|---|---|
| 1 | JSON-collation (`iba/config/*.json`) not yet audited against the live build | §A3.3 / §A8.2 | run the one completeness pass, confirm nothing still-relevant is missed, then archive |
| 2 | Passage table fragmented (avg 1.56 verses/passage) | §A5.3 / §A8.4 | rebuild the passage table; refine every config rule feeding `passage.build` (`passage.default_rule`, `passage.min_shared_strongs`, `passage.cross_chapter`, `passage.review_over`) |
| 3 | No `reject` kind in `cfg_candidate_rule` — a deliberate exclusion has no recorded transition | §A3.1 / §A8.5 | add a `reject` kind (config fix) |
| 4 | `cfg_change_log` logs config *reloads* only, not individual row-level `cfg_*` writes; rule c's exclusive-write-path is convention, not enforced | §A4 / §A8.6 | extend `cfg_change_log` (or add a sibling table) for row-level logging + enforce the write path through `configuration_maintenance` |

### Newly surfaced sweeping the rest of the document (not previously punch-listed)

| # | gap | source |
|---|---|---|
| 5 | `cfg_enum` naming-collision check (principle k) — no check runs against it today | §0.1 row k |
| 6 | No unified verb dispatcher — still 4 separate PS scripts instead of one `run`/`status`/`resume`/`stop`/`validate`/`config …`/`debug`/`report` surface | §A1, §A2, §A6 |
| 7 | No live `config show`/`set`/`diff` surface — config only changes via CSV/JSON seed + `-Reload` | §A6 |
| 8 | Three operations are duplicated ad hoc instead of shared utilities: (a) STEP-call retry/cap/forward-walk logic, currently only in `raw.py`; (b) config self-validation pattern, currently only in `cfgload.py`; (c) pre/post validation-gate envelope, currently informal in `run.py` | §A4 "standing extraction debt" |
| 9 | Morphology parser utility + `stem` table — not built at all | §A4, §A5.3 |
| 10 | Git operations utility — not built | §A4 |
| 11 | File management (archive/version/manifest) utility — no in-app equivalent of the legacy manifest script | §A4 |
| 12 | Replayable-patch writes — writes today are direct commits, not patch records | §A7 |
| 13 | Formal backtrack/rerun-by-provenance mechanism — not built | §A7 |
| 14 | ~4,190 verses (14.4% of 29,037) are not yet passage-assigned | §A5.3 |
| 15 | `initialise-concordances` bulk op — not built (structure only; does not need D4's grouping to proceed) | §A6 |
| 16 | Specific data-layer ops not built: add/remove seed · add/remove candidate characteristic · reassign a Strong to another registry · start new study unit | §A6 |
| 17 | Reports not built: register status · book status · validations & errors — data for the last one already sits in `validation_result` (15,334 rows), just has no report surface | §A6 |
| 18 | `BUILD.md`'s run-command list is incomplete — documents only `New-Word.ps1`'s invocation today; needs the other 3 scripts folded in and kept current as commands are added | §A1 (standing requirement) |

**Phase-1 total: 18 gaps** — 4 already directed, 14 newly surfaced in this sweep.

### One documentation inconsistency found during the sweep (needs your call, not a code fix)

- **§0.1's table tags principle g** (non-module governance, `wide/governance.json`) **as Phase 1**, but
  **§B7 places the actual authoring of `wide/governance.json` in Phase 2**, pending on the Phase-1
  JSON-collation audit (item 1 above) settling what rules remain to be encoded. These two statements
  conflict on which phase owns it. Flagging rather than picking one — which is correct: build it now
  (Phase 1), or only once the audit narrows what's left to encode (Phase 2)?

---

## Part 2 — Phase 2 (Analytic Layer): not actionable yet, listed for completeness only

Not a gap list in the same sense — nothing here exists yet, by design (§13's gate hasn't opened). One
line per area, cross-referencing the full detail already in Part B of the design document:

| area | status | source |
|---|---|---|
| Interpretation/Prose schema (`operation`, `meaning`, `prose`, `prose_type`, `verse_meaning`, `verse_operation`) | not built (proposal stage) | §B1 |
| Claude API adapter | not built | §B2 |
| `analyse-characteristic` + internals (screen-inclusion → analyse-operation → record → reconcile → refine-rule) | not built | §B3.2 |
| `consolidate` / `reconcile` / `refine-rule` | not built | §B3.2 |
| `seed-update`, `prepare-for-read` | not built | §B3.2 |
| Researcher-specific analytic ops (work a study unit, start new char focus) | not built | §B4 |
| Analytic reports (concordance, study-unit status, char status) | not built | §B4 |
| Quality validation (dimension rules, content-validity V1–V3, drift, acceptance-sample) | not built — structurally can't exist yet | §B5 |
| Outputs & Products (Layer 4) | deliberately deferred | §B6 |
| `wide/governance.json`, `wide/patterns.json` | not authored | §B7 |

---

## Summary

- **Phase 1: 18 gaps to close**, 4 already directed by you, 14 newly surfaced here, plus 1 documentation
  inconsistency to resolve before it propagates further.
- **Phase 2: 10 areas**, entirely un-built by design, waiting on the §13 gate.
- Recommended next step: confirm/prioritise the 14 newly-surfaced Phase-1 items (§ above) and resolve the
  governance.json phase question, then this becomes the working punch list for Step 3 (close the gaps).
