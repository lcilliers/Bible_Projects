# Session log — STEP 60-cap truncation: root-cause fix + programme-wide recovery

- **File:** wa-sessionlog-20260622-step-truncation-fix-and-recovery-v1.md · **Date:** 2026-06-22
- **Author:** Claude Code
- **Scope:** a single-thread session — diagnose, fix and remediate the STEP client's silent 60-result truncation. Triggered by a researcher observation; ran end-to-end through root-cause, a programme-wide sweep, and recovery of every confirmed truncation. (Session terminated unexpectedly before the log was written; reconstructed 2026-06-23 from the two working docs and the day's commits.)
- **Backing docs (authoritative detail):**
  - `outputs/markdown/wa-m10-rasha-coverage-gap-20260622.md` — the rāšāʿ investigation + H7563 repair, stage by stage.
  - `outputs/markdown/wa-step-truncation-sweep-20260622.md` — the programme-wide sweep and the six confirmed truncations + recoveries.

## 1. Headline

The STEP API caps every search at **60 results** but reports the true `total`. `step_client` beat the cap with a two-level canonical split (5 sections → halve a section if >60). When a *halved* section still exceeded 60, the client did **not** recurse — it silently truncated and the DB faithfully stored the short result. High-frequency terms therefore lost the back of their densest books with no error.

- **Root cause found and FIXED** — `scripts/analytics/step_client.py` now uses a cap-proof **forward-walk** (`_paginate_all`) that self-validates against STEP's reported total and warns on any shortfall. Silent truncation can no longer recur.
- **Programme-wide sweep** (2,396 terms) found only **6 genuine truncations** — all six now **recovered**. The other 56 high-gap terms are legitimate scope / span-filter, not truncation.

## 2. The trigger

Researcher observation: the well-known "wicked" verses of **Proverbs 24/28/29** (Pro 28:1, 29:2, 29:16, 24:19–20 …) were missing from the M10 / M10b / M10c extracts.

**Verdict: correct and serious, but imprecise in wording.** The verses exist in the corpus (some appear in M10 under *other* terms — Pro 29:16 via H6588 *pesha*); the real defect was that the **anchor term H7563 (rāšāʿ, "the wicked")** — anchor of M10b (Wickedness) — was occurrence-truncated, carrying **180** of its **~250** OT verses, with Proverbs coverage cutting off dead at chapter 21 (a contiguous-from-start-then-stops signature = truncation, not natural distribution). One genuine verse-level absence found: **Pro 24:20** had no verse-record at all.

## 3. Root cause, exactly

STEP total for H7563 = **249**. The Poetry section (~134) was halved into `Poetry_A` (Job+Psalms ≈108) and `Poetry_B` (Proverbs+Ecc+Song ≈86) — **each half still >60**, and the client never recursed. Each half silently truncated: **Psalms 34/80, Proverbs 60/77, Ecclesiastes 0/6** → 180 stored. The DB stored exactly what the client returned, so this was an **upstream pull defect**, not an ingestion error.

### The fix
`scripts/analytics/step_client.py` — replaced the two-level split with a single cap-proof **forward-walk** (`_paginate_all`): query `<frontier>-Rev.22.21`, absorb the ≤60 rows, advance the frontier to the canonically-last verse seen, repeat until the remaining total fits one page. Needs only canonical book *order* (`_OSIS_ORDER`), no versification map. **Self-validates against STEP's reported total and warns on any shortfall.** All four paginating methods now share it. Verified: `get_verse_records('H7563')` → **249** (was 180); small terms unaffected; previously-missing verses now present.

## 4. H7563 (rāšāʿ) repair — executed

Researcher decisions: (1) **skip ke.mo** (H3644G, T2 particle) → targeted H7563-only, no registry-wide `audit_word`; (2) **leave the legitimate set-asides** (Num 35:31 forensic-sense scope call preserved); (3) produce the 69 as a **separate additional JSON** so the in-progress M10b work stays clean.

Pre-op snapshot: `backups/bible_research_pre-h7563-ingest_20260622.db`.

1. `_apply_h7563_ingest_missing_69_20260622.py --live` — inserted **69 `wa_verse_records`** (mti_term 1223, OWNER, registry 172) + **69 `verse_context` shells**; dedup-guarded.
2. `_apply_ingest_verse_morphology.py --live` — created the **3 canonical verse rows** (Pro 24:20, Psa 94:3, Psa 106:18) + set `verse_id` on all 69 + fetched morphology (measure layer).
3. `_apply_generate_ve_lexical_v2.py --live --vcids @…` (new `--vcids` scope) — **686 `ve_lexical` rows + 69 narration findings** for exactly the 69.
4. `build_ve_lexical_extract.py --cluster M10b --only-refs @…` (new `--only-refs` scope) — separate additional JSON `Sessions-v2/M10b-Wickedness/Data/wa-ve-lexical-extract-M10b-additional-h7563-20260622.json` (69 verses · 170 occ · ~43k tokens).

**Verification:** H7563 now **249** distinct verses; all `verse_id`+`morph` set, `delete_flagged=0`, 0 duplicate references; all → M10b (no XREF to mirror); the 1 legitimate set-aside preserved; 69/69 carry a populated rāšāʿ node. **M10b in-scope 492 → 557** (the only ≤M11 cluster touched). DB integrity `ok`, 0 FK violations.

## 5. Programme-wide truncation sweep

Read-only oracle (STEP true total) vs DB across **2,396 terms**, suspects confirmed by the chapter-cutoff test in each term's own densest book.

- **6 confirmed truncations** (clean canonical cutoff, recoverable).
- **56 scope / span-filter** high-gap suspects — legitimate (the cluster keeps only the inner-being sense); a high gap on a polysemous term is mostly span-filter, not a cap defect. Only a clean contiguous chapter cutoff proves truncation.

Scripts: `_check_step_truncation_sweep_20260622.py`, `_check_truncation_confirm_20260622.py`.

## 6. Recovery of all 6 confirmed truncations

Recovery script: `_apply_truncation_recover_term_20260622.py` (ingests absent occurrences via the fixed client; gained a `--full` mode and a ref-parse fix during the run). Each recovery → separate additional JSON in the cluster's `Data/` (gitignored); measure layer + ve_lexical generated; no new duplicate-reference groups; integrity ok.

**M47 seat-words** (studied in *every* book → every absent verse is genuine truncation, within-range ≈ 0):
| Term | cluster | active before → after |
|---|---|---|
| ne.phesh H5315G (soul) | M47 | 179 → **229** (+50; 1 within-range excluded) |
| lev H3820A (heart) | M47 | 331 → **550** (+219 across 12 books, 0 within-range = pure truncation) |

**Remaining 4 — recovered in `--full` mode** under researcher direction ("full recovery + co-term pickup"): recover **all** occurrences, not just each term's own truncation-tail, so the term is picked up as a **co-term** in other clusters' verse fan-outs (the fan-out only includes a co-term that has an active `verse_context` row in that verse, which truncation had removed):
| Term | cluster | active before → after |
|---|---|---|
| na.tan H5414G (give) | M12 Purity | 242 → **1187** (+945) |
| pisteuō G4100 (believe) | M31 Faith | 120 → **218** (+98) |
| o.yev H0341 (enemy) | M44 Relational | 244 → **276** (+32) |
| kaleō G2564G (call) | M37 Calling | 110 → **133** (+23) |

All at full STEP coverage, 0 duplicate-ref groups, verse_id + ve_lexical set, integrity ok. **Co-term pickup verified:** na.tan's recovered Eze 22:31 now co-occurs with za.am (M02); o.yev's Psa 138:7 with tsa.rah (M03) — both appear as co-terms with lexicals in those verses' fan-outs.

**Trade-off noted (rāšāʿ + the `--full` four):** these polysemous terms bring *all* occurrences active into the home cluster's focus verse-set too (na.tan especially — M12 grows by 945, mostly literal "give"). Keeping occurrences active (not set-aside) is exactly what makes them visible as co-terms; set-aside in the home cluster would also remove that co-term visibility. A fan-out design point to revisit if that conflict matters.

## 7. Scripts added / changed (key)

- `scripts/analytics/step_client.py` — `_paginate_all` forward-walk replacing the two-level split; all four paginating methods share it; self-validates against STEP total. **(committable independent of any recovery — the root-cause fix.)**
- `_apply_h7563_ingest_missing_69_20260622.py` — targeted H7563 ingest.
- `_apply_generate_ve_lexical_v2.py` — gained `--vcids` scope.
- `build_ve_lexical_extract.py` — gained `--only-refs` scope (+ earlier provenance/version fix).
- `_check_step_truncation_sweep_20260622.py`, `_check_truncation_confirm_20260622.py` — the sweep.
- `_apply_truncation_recover_term_20260622.py` — generic recovery (gained `--full` + ref-parse fix).

## 8. Outcome / state at session end

- **All 6 confirmed truncations recovered**: rāšāʿ (M10b), ne.phesh + lev (M47), na.tan (M12), pisteuō (M31), o.yev (M44), kaleō (M37). The 56 scope/span-filter suspects are legitimate. The client fix prevents recurrence.
- **M10b unblocked** — its truncation gap (the reason it shouldn't be distilled) is closed; inputs are the main M10b extract + the separate additional H7563 JSON.

## 9. Open / carried forward

- **ke.mo (H3644G, T2 comparison particle)** truncation left as-is per decision — decide separately if its grammatical fan-out is ever wanted.
- **Systemic re-assurance:** the sweep was a one-time oracle-vs-DB pass on the *current* data; the fixed client now self-warns, so future pulls are protected — but any term re-pulled before today should be spot-checked.
- **Main programme thread resumes at the M10 family** (Sin / Wickedness / Defilement): distillation (Chat) → findings-audit gate → capture → essay, then M11.

## Memory

Already recorded during the work: `project_step_60cap_truncation_and_forwardwalk_fix` (60-cap silently truncated high-freq terms; client now forward-walks + self-validates; audit anchor terms).
