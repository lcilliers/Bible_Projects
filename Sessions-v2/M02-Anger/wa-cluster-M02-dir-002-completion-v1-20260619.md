# DIR-20260619-002 — completion confirmation (M02 C7 scope) · 2026-06-19

**Directive:** `wa-cluster-M02-dir-002-c7-scope-v1-20260619.md` · **Applied by:** Claude Code
**Script (reversible):** `scripts/_apply_m02_dir002_c7_scope_20260619.py` · **Backup:** `backups/bible_research_pre-m02-dir002_20260619.db`
**Resolution:** Option 1 (document/constrain). No membership change; M03 untouched. Integrity `ok`.

## Completion items (directive §Completion confirmation)

1. **cluster_finding row recorded — 1** ✅
   - `id=20572` · `cluster_code='M02'` · `obs_id=400` (**T7.1.8** — OT-Hebrew/NT-Greek vocabulary continuity, the
     question the directive's motivation cites) · `finding_status='cluster_synthesis'`
   - `source_file='wa-m02-marah-mar-bitterness-lookup-v1-20260619.md'` · `notes` cite DIR-002 + originating flag F-D
   - `finding_text`: *"C7 (Bitterness) is NT-pikria-only (G4088, 4 occ) by design. The OT bitterness-of-soul family
     (mar/marah — H4751, H4843…) is owned and analysed in M03 (Grief)… C7 is therefore not expanded; the OT field
     remains in M03."* (verbatim per the directive)
2. **Session D cross-cluster pointer registered** ✅
   - mechanism resolved = `wa_session_research_flags`, `flag_code='SD_POINTER'`, `session_target='D'`
   - `id=717` · `flag_label='M02C7-SD001'` · `registry_id=13` (bitterness) → `cross_registry_id=5` (anguish) ·
     `cluster_link='M02,M03'` · `cluster_link_basis='sense-split (pikria vs mar/marah)'` · `strongs_reference='G4088'`
   - description registers the NT-pikria (M02) ↔ OT-mar-nephesh (M03) bitterness seam for cross-cluster synthesis.
3. **No collateral change** ✅
   - M02 active-term count (`status IN ('extracted','extracted_thin')`): **48 before / 48 after — unchanged**.
   - M03 `mti_terms`: **211 rows / 128 delete_flagged — unchanged** (0 M03 rows modified).

## Dependency resolved (directive §Scope / §Notes)

- **The c1–c7 sub-group structure is NOT persisted.** The DB holds the *old* 6-characteristic M02 model:
  characteristics 71–76 + subgroups M02-A…M02-F + M02-BOUNDARY. There is no C7/Bitterness characteristic or subgroup.
- **This did not block the finding.** All 1,645 `cluster_synthesis` rows are cluster-level (obs_id only; no
  characteristic/subgroup link), so the C7 scope finding is recorded at cluster level with its identity in the
  `finding_text`. When the c1–c7 structure is later persisted, this finding stands as-is (no subgroup backfill required).

## Observation (flagged, not actioned — per directive §Notes)

- H4843 *ma.rar* is present in M02 in its "provoke/embitter" sense with `status = NULL` → excluded from
  active-term queries (GR-DATA-001). Whether that NULL is intentional is a separate question; **noted for awareness,
  not actioned** (out of scope for the C7 fix).

*DIR-002 complete. Independent of DIR-001.*
