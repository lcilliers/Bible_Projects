# M01 + M02 — supersede OLD findings & capture NEW findings: COMPLETION · 2026-06-19

**Plan:** `wa-findings-supersede-and-capture-plan-v1-20260619.md` (researcher-approved: "proceed with both").
**Backup:** `backups/bible_research_pre-findings-capture-20260619.db`. **Integrity:** `ok` after every stage.
Done in dependency order, each stage its own reversible `_apply_` script with dry-run → live.

## Stage A — new characteristics created (additive)

`_apply_findings_stageA_characteristics_20260619.py` — parsed the characteristic-definition files and created
**18** rows: **M01 c1–c11** (ids 129–139) from `WA-m01-characteristics-v1.0`, **M02 c1–c7** (ids 140–146) from
`wa-m02-ve-characteristics-v1_0`. `char_seq = 100 + c` to avoid the `UNIQUE(cluster_code,char_seq)` collision with
the legacy 7/6-char model (the legacy is restricted in Stage C; the new model is keyed by id).

## Stage B — NEW findings captured as `prose_section` (file-as-finding, no dissection)

`_apply_findings_stageB_capture_20260619.py` — each findings file → one `prose_section` row (whole body), tagged
`cluster_code` + `characteristic_id` (per-char files) + a new `section_type`. **22 rows** (FTS auto-populated):

| | cf_char_synth | cf_cluster_synth | cf_atomic |
|---|---|---|---|
| **M01** | 11 (c1–c11 synth → chars 129–139) | 1 (cluster-synthesis) | 1 (NEW-merged-bytier) |
| **M02** | 7 (c1–c7 tier-analysis → chars 140–146, latest versions) | 2 (cluster-synthesis-bytier + cluster-findings F1–F10) | — |

New `prose_section_type`s: `cf_cluster_synth`, `cf_char_synth`, `cf_atomic` (source_stage `findings`).
`status='approved'`, `author='claude_ai'`. Full-text searchable via `prose_section_fts`.

## Stage C — OLD findings restricted (soft-delete + reason; retained, hidden from analysis)

`_apply_findings_stageC_restrict_20260619.py` — `delete_flagged=1` + documented reason
("superseded by 2026-06-19 NEW findings…"):
- `cluster_finding` (old consolidated-2026-05-16): **1,118** (M01 755 + M02 363) — *not* the DIR-002 C7 row.
- `finding` CLUSTER-level (`session_b_migration` + `l2_rollup`): **37** (M01 32 + M02 5).
- legacy `characteristic` (Pre-v2_6 7/6-char model): **13** (M01 7 + M02 6).

**KEEP — verified untouched after the run:** verse-level `l2_meaning` reads **1,737** (M01 1,034 + M02 703 — the
grounding), the DIR-002 C7 `cluster_synthesis` row, the 22 new `prose_section` rows, the 18 new characteristics,
`ve_lexical`, VCGs, terms, verses.

## HELD — flagged for a separate scoping decision (NOT restricted)

1. **`wa_session_b_findings`** (legacy, registry-keyed, 2,883 rows programme-wide). Cluster scope is unreliable:
   `cluster_link` tags only 27 (M01) + 5 (M02); the registry-map gives 13 + 211 but **over-includes** (registries
   span clusters — 3 shared M01↔M02 and feeding other clusters). Restricting by registry would wrongly hide other
   clusters' findings. **Decision needed:** restrict the 32 `cluster_link`-tagged rows only, or a broader scope?
2. **Old `cluster_subgroup` rows** (M01-A…G, M02-A…F + BOUNDARY). Referenced by `mti_term_subgroup` placements and
   potentially VCGs; restricting them is structural, not just "findings". **Decision needed:** restrict, or leave?

## Reversal

Fully reversible: `UPDATE … SET delete_flagged=0 WHERE notes/source_legacy_ref LIKE '%superseded by 2026-06-19%'`
restores all restricted rows; the 22 prose_section rows and 18 characteristics are identifiable by their 2026-06-19
sources and removable. Pre-run snapshot retained.

## Net result

For prose generation, the DB now holds the NEW findings as searchable, cluster/characteristic-tagged
`prose_section` documents (the prose-foundation), the OLD findings are retained-but-hidden, and the verse-read
grounding stays live. Remaining: the two HELD scoping decisions above.

## UPDATE 2026-06-19 — Stage C REVERSED (researcher: too early to disassemble)

Researcher reconsidered: it is too early to tell what of the previous structure will be reused, so the OLD
structure should NOT be broken apart yet. **Stage C was fully reversed** (`_reverse_findings_stageC_restrict_20260619.py`):
1,168 rows un-restricted (cluster_finding 1118 · finding 37 · characteristic 13), marker stripped, integrity ok.
**The old structure is intact and visible again.**

Current state = the researcher's **alternative #1**: the NEW analysis is captured in a *new* construct
(`prose_section`, additive — Stages A+B remain) **without** breaking the old structures apart. Stages A (18 new
characteristics) and B (22 prose_section file-findings) are additive and fully reversible if **alternative #2**
(leave findings in files, defer capture until analytics run through more clusters) is preferred — that would
remove the 22 prose_section rows + 18 new characteristics, returning to a zero-DB-footprint defer.

**Open:** keep alternative #1 (additive capture, old intact) or switch to alternative #2 (reverse A+B, defer)?
