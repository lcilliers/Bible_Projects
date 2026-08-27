# M10c — Phase 9 char-findings obslog — 2026-05-26

**Cluster:** M10c — Defilement and Impurity
**Phase:** 9 (catalogue findings — 4 per-characteristic batches; cluster-synthesis batch pending)
**Governing instruction:** `wa-sessionb-cluster-instruction-v2_9-20260526` §12
**Directive:** `wa-cluster-M10c-dir-004-phase9-char-findings-load-v1-20260526`

## AI batches delivered

The 4 per-characteristic Phase 9 batches were authored against the briefs + structural inputs built by `scripts/_build_m10c_characteristic_phase9_package_20260526.py` (committed cb89134). All 4 followed the v2_9 §12 tier-by-tier staged-execution protocol; per-tier self-evaluations PASS in every case; final Self-check blocks complete.

| Char | Short name | Verses | Brief size | Findings file size | E | S | G |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Ritual defilement-state | 133 | 15K | 157K | 158 | 27 | 4 |
| 2 | Moral-inner defilement-state | 26 | 15K | 150K | 177 | 9 | 3 |
| 3 | Corporate/covenantal defilement | 83 | 15K | 147K | 173 | 13 | 3 |
| 4 | Defilement by external spiritual agency | 21 | 15K | 111K | 145 | 41 | 3 |
| — | **Total** | **263** | — | — | **653** | **90** | **13** |

## Loader run

Script: `scripts/_apply_phase9_characteristic_findings_20260518.py` (generic, unchanged).

| Char | Loader output (final 3 lines) |
|---:|---|
| 1 | `Committed: 189 rows into cluster_finding` / `Post-insert verify: total=189 finding=158 silent=27 gap=4` / `Post-verify OK.` |
| 2 | `Committed: 189 rows into cluster_finding` / `Post-insert verify: total=189 finding=177 silent=9 gap=3` / `Post-verify OK.` |
| 3 | `Committed: 189 rows into cluster_finding` / `Post-insert verify: total=189 finding=173 silent=13 gap=3` / `Post-verify OK.` |
| 4 | `Committed: 189 rows into cluster_finding` / `Post-insert verify: total=189 finding=145 silent=41 gap=3` / `Post-verify OK.` |

**Total DB writes:** 756 cluster_finding rows (4 × 189).

## Parser-safety verification (per loader)

- No forbidden scope markers (`SUB-`, `CLUSTER-`, `VCG-`) appeared in any findings file.
- All `[CHAR-N]` markers matched the declared `--char-seq`.
- Each prompt block opens with `**T#.#.# — ...**` and contains exactly one outcome line `**[CHAR-N]** {E|S|G} — ...`.
- Outcome tallies (E + S + G) sum to 189 per file.

## Carry-forward observation status

All 4 cluster_observation rows (ids 247-250) remain at status='open'. The AI Self-checks reference them, but per §11B.3 the status advance to 'confirmed'/'refined' is a researcher-review step, not a Phase-9-loader automatic write. Deferred to post-cluster-synthesis review.

Self-check evidence from AI batches:

- **Char 1 (id 247, SPLIT_DESIGN_RATIONALE)**: AI confirms M10c-A and M10c-B treated as complementary mechanisms of one characteristic throughout the 189 prompts; integration documented at T1.2.1 (mechanism distinction) and elsewhere.
- **Char 4 (id 248, INTEGRATION_NOTE → M27)**: AI's T6 findings address unclean-spirit register cross-cluster signal (M10c ↔ M27).
- **Char 3 (id 249, INTEGRATION_NOTE → M10b)**: AI's T6 findings address Ezekiel idolatry cross-cluster signal (M10c-D ↔ M10b-D).
- **Char 2 (id 250, INTEGRATION_NOTE → M10/M11/M29/M08/M09)**: AI's T6 findings map the relational network around moral-inner defilement-state.

## T7.3 science-extract gap (carried into all 4 batches)

Char 1's Self-check flagged: *"Science extract (Section 4) not uploaded — this is a gap noted at T7.3. T7.3 findings are partial; researcher should supply Section 4 for completion if required."* Spot-check confirms chars 2/3/4 carry the same gap pattern. Decision: leave the gap as-is for now; if researcher wants T7.3 augmentation, run a follow-up fix-up batch with Section 4 loaded.

## File reconciliation

- 4 findings files moved from `files phase 9/` to canonical M10c folder.
- AI worklog renamed: `wa-obslog-M10c-phase3-v1_0-20260526.md` (1362 lines, now spans phases 3-5-7-9) → `wa-cluster-M10c-AI-worklog-phases3-5-7-9-v1-20260526.md`. Prior worklog `wa-cluster-M10c-AI-worklog-phases3-5-7-v1-20260526.md` removed (superseded; new file contains all prior content plus Phase 9 entries).
- Stale `files phase 9/` directory remains empty (Google Drive sync artefact; harmless).

## Cluster state post-Phase-9 (char batches)

- 756 cluster_finding rows (4 × 189)
- 4 characteristic-scope batches complete
- Cluster synthesis batch pending
- Cluster status: `Analysis - In Progress` (unchanged)

## Next

Cluster-synthesis batch — Phase 9's 5th session: per-prompt matrix (4 chars stacked) + free-form prose appendix. CC builds the synthesis brief + structural input via `scripts/_build_m10c_phase9_cluster_synthesis_*.py` (to be adapted from M10b's builder).
