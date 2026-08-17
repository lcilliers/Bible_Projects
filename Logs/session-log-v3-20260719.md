# IBA Session Log — v3, 2026-07-19

**Topic:** Fix the rushed candidate-characteristic seeding module (and confirm passage-module config parity), driven by the already-defined rules. Bring remote git up to date.

**Outcome:** ✅ Root cause found and fixed; all 66 books re-stamped and re-passaged; documented; committed and pushed (remote now 0-ahead/0-behind).

---

## 1. Trigger

Researcher flagged that the candidate-characteristic seeding + `Set-Candidates.ps1` module was
built without proper module-dedicated config rules, and that it was not following the IBA app
rules. Asked, in order: (a) surface the PS runner; (b) list the config rules it uses; (c) explain
what logic was actually used and whether the fault is in the seedlist; (d) fix both the candidate
and passage modules using the rules **already defined** (no rule reset), config-driven, autonomously.

## 2. Diagnosis

- **Module** = [`iba/app/ps/Set-Candidates.ps1`](../app/ps/Set-Candidates.ps1) — a thin config-driven
  runner. It hardcodes nothing: reads the step sequence from `cfg_step` and runs each via
  `python -m iba.app.run set-candidates --step <step>`. Steps: `candidate.seed` (global) →
  `candidate.set` (book).
- **Config store** (`iba/app/db/iba.db`, `cfg_*` tables) properly governs *orchestration*
  (sequence, scope, on-fail, write-grants, enums, tables/columns). The **dedicated
  `cfg_candidate_rule` table exists but was empty**.
- **Root cause (code, not config)** — `candidate.seed` in
  [`iba/app/handlers/candidate.py`](../app/handlers/candidate.py) had a block that **created a
  candidate for any lemma whose base-Strong's was carried by any registry word's `word_strong`
  list** — i.e. seeding from registry *co-occurrence*. This is the route the method docs
  (`wa-characteristic-role-lexical-cycle-authoritative-v1-20260708.md` §4/§11) **explicitly reject**
  ("LORD→lust" noise; registry lists validate, never impute).
- **Evidence** — ~1,073 of 2,805 candidates were this noise. Top candidates by span-frequency were
  function words / generic verbs: **H5921 "upon"** (5,774 spans, admitted via registry word
  "reasoning"), **H1961 "to be"**, **H3117 "day"**, **H3027 "hand"**, **H6440 "face"**. Under the
  char-continuity passage rule these never break, so passages over-chained.
- **Seedlist itself was clean** — the independent net (inventory `char_matched` / `ib_candidate`,
  1,555 gloss/judgement lemmas) does NOT contain the function words (`char_matched=None` for
  H5921/H1961/…). The fault was entirely the handler's registry-coverage-creates-candidate block.

## 3. Fix applied

- **`candidate.py seed()`** — removed the `word_strong`-creates-candidate block. Registry coverage
  is now the **double-control only**: it sets `registry_match` on already-independent candidates and
  never confers candidacy. Candidacy is meaning-based only — migrated independent net (gloss/synonym
  `char_matched` + `ib_candidate`) + read-emergent + the editable `cfg_candidate_rule`
  (synonym/accept/reject, config seed [`iba/app/config/candidate.json`](../app/config/candidate.json)).
  Docstring + return message aligned; no rule reset.
- **Passages** — confirmed already config-driven via `cfg_setting` `passage.*`
  (`default_rule=char-continuity`, `min_shared_strongs=1`, `cross_chapter=false`, `review_over=10`),
  matching passage-completeness-rule v2. **No new table built** (scalar rules belong in `cfg_setting`
  by app design; list-inputs in `cfg_candidate_rule`) — avoided over-engineering.

## 4. Re-run + verification

- Snapshotted `iba.db` → `iba/app/db/iba.db.bak-20260719-precandidatefix` (git-ignored).
- Re-ran `python -m iba.app.migration.import_seed` → `candidate_seed` reset to the clean independent
  net: **1,732 candidates** (1,353 registry-direct gloss, 202 ib-judgement, 177 read-emergent,
  74 reject); was 2,805.
- Re-ran fixed `candidate.seed` (global) → **0 new candidates from `word_strong`** (no noise added).
- Re-ran `candidate.set` + `passage.build` for **all 66 books** in one process →
  72,381 candidate spans, **18,571 passages**.

| metric | before | after |
|---|---|---|
| candidates | 2,805 | 1,732 |
| function words as candidates | upon / to-be / day / hand… | none |
| passage length distribution | runaway chains | 15,027 single-verse · 2,953 of 2–3 · 484 of 4–6 · 82 of 7–10 · 25 of 11+ |
| max passage length | (runaway) | 26 |
| needs_review (>10 verses) | — | 25 |

- **Residual (by design, not a bug):** top remaining candidates are generic motion/speech verbs
  (asah, bo, halak, amar, raah, shuv) promoted by the read-emergent layer with verse-specific tags.
  Meaning-based, intentionally over-inclusive, tested at the lexical (Axis B role) stage; they no
  longer over-chain passages. Tightening them, if wanted, is a `cfg_candidate_rule` reject-list
  decision for the researcher — not a code change.

## 5. Housekeeping

- Refreshed the stale config CSV exports in `iba/app/config/` (they had only shown `new-word`).
- `.gitignore` — added `iba/app/db/*.db-shm`, `*.db-wal`, `*.bak-*` (the 113 MB `.bak` was not
  previously ignored; prevents the large-file push-block recurring).
- Committed `d0e4a127` (candidate.py + config CSVs + review doc + .gitignore).
- **Pushed** — scanned pending commits first (largest blob 2.6 MB, safe); `git push origin main`
  fast-forwarded `f4796fba..d0e4a127`, delivering all 85 pending commits. Remote now 0-ahead/0-behind.

## 6. Artefacts

- Review doc: [`docs/iba-set-candidates-config-review-v1-20260719.md`](../../docs/iba-set-candidates-config-review-v1-20260719.md) (§7A diagnosis, §7B fix).
- Memory updated: `project_iba_candidate_seeding_registry_direct_noise` → **RESOLVED**.
- Pre-fix DB snapshot: `iba/app/db/iba.db.bak-20260719-precandidatefix` (prune when confident).

## 7. Open / next

- Optional: decide whether read-emergent generic verbs need `cfg_candidate_rule` reject entries.
- Optional: make the registry-direct layer a **live** gloss-match against the current registry
  (currently frozen from the migration's `char_matched`); noted as a future refinement, not needed
  for correctness.
