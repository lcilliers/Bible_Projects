# Psalms — folder index

> **The DB is the corpus.** Every reading lives in `database/bible_research.db`; the files here are governance records, regenerable views, or build provenance. If a file and the DB disagree, the DB wins.

## ★ Current authoritative state — the corrected char-arc re-read (2026-07-11)

**All 150 psalms have been re-read by char-arc under the corrected method, and are gate-clean.** This is the live Psalms analysis. It lives in the DB as `ve_lexical` rows stamped `source_provenance='reread-psalms-2026'` with `verse_span_index.role_provenance='read-2026'`.

- **Method (how it was done, repeatable):** [`Workflow/Instructions/wa-corrected-charac-arc-reread-repeatable-process-v1-20260711.md`](../../Workflow/Instructions/wa-corrected-charac-arc-reread-repeatable-process-v1-20260711.md) — the executable pipeline + the issues-expressly-prevented table. Subordinate to the per-book corrective method (`wa-per-book-corrective-method-authoritative-v1-20260707.md`).
- **Lens correction that reshaped it:** [`wa-ib-relevance-screen-correction-20260709.md`](wa-ib-relevance-screen-correction-20260709.md) — Screen 0 (God-content → qualifier; human IB → characteristic).
- **Final state:** [`wa-psalms-reread-snapshot-v6-FINAL-20260711.md`](wa-psalms-reread-snapshot-v6-FINAL-20260711.md) — 150/150, every content gate at zero, 0 God-bearer / 0 old-provenance book-wide.

### Progress trail (snapshots — baseline → close → final)
| doc | measurement point |
|---|---|
| [`wa-psalms-reread-baseline-20260709.md`](wa-psalms-reread-baseline-20260709.md) | pre-reread baseline |
| [`wa-psalms-reread-snapshot-20260710.md`](wa-psalms-reread-snapshot-20260710.md) | 51/150 |
| [`-v2-`](wa-psalms-reread-snapshot-v2-20260710.md) · [`-v3-`](wa-psalms-reread-snapshot-v3-20260710.md) · [`-v4-`](wa-psalms-reread-snapshot-v4-20260710.md) | Book II / III / IV closes |
| [`-v5-`](wa-psalms-reread-snapshot-v5-20260711.md) | Psalter close (150/150) |
| [`-v6-FINAL-`](wa-psalms-reread-snapshot-v6-FINAL-20260711.md) | **after Book I remediation — fully corrected** |
| [`wa-psalms-reread-discipline-audit-20260710.md`](wa-psalms-reread-discipline-audit-20260710.md) | mid-session gate/discipline audit |

### Planning / pilot docs (provenance of the intervention)
`wa-psalms-intervention-plan-20260709.md` · `wa-psalm-004-pilot-delta-20260709.md` · `wa-psalms-pilots-validation-and-scale-20260709.md` · `wa-reread-automation-worklist-design-20260709.md`

### Reusable scripts (do not rebuild — see the method doc §3)
`scripts/_reread_ledger_lib.py` · `_reread_finish_v1_20260709.py` · `_reread_worklist_v1_20260709.py` · `_apply_reread_lexical_v1_20260709.py` · `_check_reread_measures_v3_20260709.py`

### Next phase
Express the corrected read as **findings** and run the **scored read-back audit** (the gates prove structure/completeness; correctness/fidelity/movement need the audit — see method doc §5). Then prepare narratives.

---

## ⚠ SUPERSEDED — the pre-correction Phase-1/Phase-2 views (legacy, 2026-07-02/03)

These predate Screen 0 and the char-arc read. They are **DB-backed regenerable views**, kept for browsing only; the corrected read above is authoritative.

- **`readings/`** — the 150 Phase-2 chapter-readings (`prose_section` type `lexical_prose_chapter`, id 104). Whole-chapter readings, superseded by the char-arc read.
- **`phase1-views/`** — Phase-1 lexical inspection dumps of the *old* `ve_lexical` rows. Superseded.
- Regenerate/verify: `python scripts/_export_prose_to_md_v1_20260703.py --verify|--export`.

## `_archive/` — build provenance (this-session intermediates, applied to the DB)
- **`_archive/_read/`** — the 150 per-psalm builder JSONs the char-arc read was applied from.
- **`_archive/_roles/`** — per-psalm role JSONs.
Kept as provenance; the DB is the source of truth. Safe to delete.

## Cross-cutting outputs (in `../_reports/`, DB-canonical)
Psalter syntheses (`prose_section` id 580/581) + harvest grid — these were built on the **old** read and will be regenerated from the corrected read in the findings/narrative phase.
