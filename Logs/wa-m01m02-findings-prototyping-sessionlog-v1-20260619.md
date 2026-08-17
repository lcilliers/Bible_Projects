# Session Log — M01/M02 findings prototyping phase (close-out)

- **File:** `wa-m01m02-findings-prototyping-sessionlog-v1-20260619.md` · **Date:** 2026-06-19 · **Prefix:** WA · **Version:** v1
- **Phase:** prototyping the cluster pipeline (ve-lexical analysis → tier findings → DB capture) through **M01 (Fear)** and **M02 (Anger)**, and **deciding how findings are saved**.
- **Scope:** what was done, what was decided (esp. findings capture), current DB state, and what is parked/open.
- **Commits:** `f8c38c0` … `66f21b4` (14 commits, all `session 20260619:`). DB snapshots in `backups/bible_research_pre-*-20260619.db`.

---

## 1. What this phase was for

To take the new **verse-analysis method** (L2 verse-read = meaning + the ve-lexical measure layer) through two
full clusters end-to-end, produce the new findings, compare them against the old (2026-05-16) findings, and
settle **how the findings are stored in the DB for future prose/essay generation** — without prematurely
discarding the previous work structure.

## 2. Work done (by thread)

1. **VE engine signal-list completeness audit + full base rerun** (`6bbcd71`). Generalised the location-seat-fix
   discipline to every hand-seeded list; expanded DIVINE/PERCEPTION/COGNITION/INTENSIFIER; re-ran the base over
   all **38,969** characteristic-related units (298k mechanical rows, 30.5k narrations); all **65,966 API reads
   preserved**; net new readable residue read = divine-involvement +432.
2. **M02 ve-lexical extracts regenerated** on the corrected base (`ce56cac`); **fixed stale "valence PARKED"
   provenance** (valence was unparked + read 2026-06-18) (`91d0a97`).
3. **Tier-catalogue v2_1 refit applied to the DB** (`c11f4ef`): de-biased question rewrites — **173 → 126 active**
   (126 keep-codes rewritten + 47 obsolete soft-deleted, folded into primaries); added an `update` handler to
   `apply_session_patch.py`; regenerated the current-state extract (v2). Tiers design docs archived (`3b525da`).
4. **OLD vs NEW findings extracts for AI assessment** — M01 (`2c2b0f3`) and M02 (`1c48a6b`): produced paired
   by-tier MDs (OLD = DB `cluster_finding`; NEW = the 2026-06-19 files) + a capture-model proposal.
5. **M02 read-field directives** — DIR-001 (`5838e40`): 6 divine-wrath valence `sinful→neutral`, 2 `cha.rah`
   `divine_involvement→agent` (C1→C2 reroute); then researcher decision **valence→righteous** (`d9e7796`) with the
   **marah/mar bitterness lookup** (Hebrew bitterness family is M03's, not M02). DIR-002 (`b332ee6`): C7 scope
   resolved NT-pikria-only + an M02↔M03 Session-D pointer. H4843 empty-shell soft-delete documented (`09db580`).
6. **Findings capture + reversal** (`6350932`, `66f21b4`) — see §3.

## 3. DECISIONS on saving the findings (the core of this phase)

- **D1 — File-as-finding, NO dissection.** Each findings file is stored **whole** as one record; findings are
  digested at **cluster level** for prose, so atomic per-question rows are unnecessary and dissecting risks loss
  and a false grain. **Grain may differ per cluster** (M01 atomic = question-level collating chars; M02 = per
  characteristic × question) — accepted.
- **D2 — Home = `prose_section`** (purpose-built; not the `finding` table): native `cluster_code` +
  `characteristic_id` + `cluster_subgroup_id`, whole `body`, `supersedes_id`/`superseded_by_id` lifecycle,
  `source_file`, and **FTS5** (`prose_section_fts`) search. New `prose_section_type`s: `cf_char_synth`,
  `cf_cluster_synth`, `cf_atomic` (`source_stage='findings'`). Conventions: `status='approved'`, `author='claude_ai'`.
- **D3 — New characteristics created** from the `*-characteristics` files: **M01 c1–c11** (ids 129–139), **M02
  c1–c7** (ids 140–146). `char_seq = 100 + c` to avoid the `UNIQUE(cluster_code,char_seq)` collision with the
  legacy 7/6-char model (the new model is keyed by id).
- **D4 — OLD structure NOT disassembled (key reversal).** A restrict-marker (`delete_flagged=1` + "superseded…"
  reason) was applied to the old `cluster_finding` (2026-05-16 consolidated, 1,118), the CLUSTER-level `finding`
  rows (37), and the legacy characteristics (13) — **then fully REVERSED**. Researcher: *it is too early to tell
  what of the previous structure will be reused; do not break the old structures apart yet.* The restrict
  mechanism is built, proven, reversible, and **PARKED**.
- **D5 — Chosen model = alternative #1:** capture the new analysis **additively** in `prose_section`, leaving the
  old structure fully intact and visible. (Alternative #2 — defer capture, leave in files — was considered and not
  taken.)
- **D6 — KEEP visible:** the verse-level `finding` `l2_meaning` reads (1,737 — the L2 verse-reads ARE the new
  method's output and the evidence the files cite), plus `ve_lexical`, VCGs, terms, verses.
- **HELD (not actioned — need a future scoping decision):** (a) `wa_session_b_findings` (legacy, registry-keyed;
  cluster scope unreliable — `cluster_link` tags few, registry-map over-includes shared registries); (b) old
  `cluster_subgroup` rows (structural, referenced by `mti_term_subgroup`/VCGs).

## 4. Current DB state (end of phase)

- **Added (additive, live):** 18 new characteristics (M01 11, M02 7); **22 `prose_section` file-findings** —
  M01: 11 per-char synth + 1 cluster-synthesis + 1 atomic; M02: 7 per-char tier-analyses + 2 cluster-synthesis
  (by-tier + F1–F10). All FTS-searchable.
- **Intact (unchanged / restored):** all OLD findings + legacy characteristics/sub-groups (Stage C reversed);
  verse-level `l2_meaning`; `ve_lexical`; VCGs; terms; verses.
- **Other DB changes this phase:** tier catalogue 173→126; M02 ve-lexical read-field corrections (DIR-001/002);
  M02 valence righteous; H4843 shells documented. Integrity `ok` throughout.

## 5. Reusable artefacts produced

- Scripts: `_check_ve_signal_lists.py`, `build_tier_catalogue_update_patch_*`, `build_m0{1,2}_findings_oldnew_extract.py`,
  `_apply_m02_dir00{1,2}_*`, `_apply_findings_stage{A,B,C}_*`, `_reverse_findings_stageC_restrict_*`,
  `export_tier_catalogue.py` (now `--version/--asof`).
- Docs: capture **plan** + **completion** (`wa-findings-supersede-and-capture-{plan,completion}-v1-20260619.md`),
  capture-**model proposal**, the marah lookup, DIR-001/002 directives + completion confirmations, the OLD/NEW
  comparison extracts.
- Memory: `project_findings_capture_file_as_finding` (governing model for future clusters).

## 6. Open items / next steps

1. **Proceed with analytics through more clusters** (M03+) on the now-settled method; revisit the retire-decision
   for the old structures once the pattern is proven across many clusters (the restrict mechanism is parked, ready).
2. **HELD scoping decisions** (D-HELD above) — `wa_session_b_findings` and old `cluster_subgroup` — to be taken
   when disassembly is judged safe.
3. Per-cluster capture for new clusters follows the **file-as-finding → `prose_section`** pattern (D1–D3).
4. Minor: `wa_session_b_findings` uses `delete_flag` (not `delete_flagged`); M02 H4843 "provoke" shell status NULL
   (noted, not actioned).

*End of phase close-out v1.*
