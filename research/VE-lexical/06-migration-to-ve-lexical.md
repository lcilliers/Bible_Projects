# VE → ve_lexical migration — COMPLETE (2026-06-15)

> Built per researcher direction while out of office: normalise the analytic layer into verse-level (`verse_context`) + items (`ve_lexical`), retrofit the VE field-values out of `finding`, leave only real findings. Tables established; VALUES migrated as-is for the later rerun/validation. All reversible.

## What was done
1. **M59 (schema → 3.33.0):** created **`ve_lexical`** — `id · verse_context_id (key) · ve_nr · ve_label · related_tier · value · notes · source_provenance · delete_flagged · created_at`. One row per value.
2. **Migration** (`scripts/_apply_migrate_ve_findings_to_lexical.py`): moved the VE field-value findings (`VERSE` `l2_api`+`l2_mechanical`) into `ve_lexical`:
   - 298,096 source findings → **82,178 NONE dropped** (not actually in the verse) → **212,243 ve_lexical rows** written;
   - de-dup: where `l2_api` and `l2_mechanical` both valued the same (verse, question), **`l2_api` (the read) kept**;
   - source findings **soft-deleted** (reversible), not removed.

## Result
- **`ve_lexical`: 212,243 rows.** ve_nr split: 1 sense 29,546 · 2 type 38,257 · 3 compound 15,910 · 4 mode-of-operation 27,791 · 5 location 25,638 · 6 origin 8,172 · 7 faculty 14,490 · 8 attributed-God 8,173 · 9 purpose 8,173 · 10 typology 3,408 · 11 response 8,173 · 12 produces 8,169 · 14 literary 8,173 · 15 name 8,170.
- **`finding` now = real findings only:** ~309k → **11,066 active** = 2,892 synthesis (`CLUSTER` 1,901 + `GLOBAL` 991) + 8,174 `l2_meaning` (the composed narratives).

## Field → VE mapping used
`Lexical and Semantic Analysis`→1 sense · `Kind`→2 type · `Co-occurrence`→3 compound · `Modes of Operation`→4 · Heart/Mind/Soul/Spirit/Body→5 location · `Origin and Source`→6 · Perception/Cognition/Memory/Affect/Creativity/Volition/Agency/Moral-Eval/Conscience/Relational-Capacity→7 faculty · `Divine Nature Reflected`→8 · `Created Purpose`→9 · `Typological Significance`→10 · `Immediate Response`→11 · `Sustained Effect`→12 · `Verse and Literary Interpretation`→14 literary · `Name and Naming`→15.
`ve_label` keeps the specific component_title (readable); `related_tier` keeps the specific question_code (so faculty/location members stay distinct).

## OPEN — for the value rerun / validation phase (researcher's "we will rerun and validate the values")
The values were migrated **as-is** — *structure* is established, *values not yet corrected*:
- **Sense (VE1) still carries the uniform gloss** for the l2_mechanical-sourced rows (the impasse defect). The rerun applies the **per-occurrence subgloss** (`step_subgloss_label`), per `wa-sense-operation-setup-v1`. `source_provenance` flags which rows are `l2_mechanical` (weak) vs `l2_api` (read).
- **Sense+type are paired and can be multi** (researcher: a verse can have >1 sense, each with its own type) — the current data has 1 each; the rerun produces the pairs.
- **Values must be lookup/rule-driven, present-only** — the rerun applies the signal-lists + rules; the migration only carried what existed.
- **VE2 'Kind'** bundles two sub-questions (T1.2.1 status + T1.2.2 simple) → 2 rows/unit; may want to split T1.2.2 to VE3 compound in the rerun.
- **VE15 'Name and Naming'** sits outside the 14 — decide keep/fold.
- **Meaning (8,174 `l2_meaning`)** left in `finding` — to be **regenerated** as the templated narrative from the validated `verse_context` + `ve_lexical`, then it is the single lexical finding.

## Verse-level (1:1) columns — NOT yet added
`verse_context` is the verse-level table; the genuinely-1:1 VE (mode = read-through from `wa_verse_records`; literary; the composed meaning) were left as-is (literary currently sits in `ve_lexical` VE14). Decide in the rerun whether to promote literary/meaning to `verse_context` columns.

## Reversibility
- Drop `ve_lexical` rows: `DELETE FROM ve_lexical WHERE created_at='M59-migration-20260615'`.
- Restore source findings: `UPDATE finding SET delete_flagged=0 WHERE level='VERSE' AND provenance IN ('l2_api','l2_mechanical')`.
