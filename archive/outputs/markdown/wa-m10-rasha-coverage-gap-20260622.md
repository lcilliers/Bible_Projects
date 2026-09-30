# M10-family coverage gap — rāšāʿ (H7563) occurrence truncation

**Date:** 2026-06-22 · **Prompted by:** a researcher observation that the well-known "wicked" verses of Proverbs 24/28/29 are missing from the M10 / M10b / M10c extracts. · **Status:** confirmed real; remediation proposed (not yet applied).

## The claim, tested

> "Proverbs 24, 28, and 29 are not in the extract at all — Pro 28:1, 29:2, 29:16, 24:19–20 … are simply absent from M10, M10b, and M10c."

**Verdict: the core observation is correct and important, but the wording is imprecise on two points.**

### What is TRUE (and serious)
- **H7563 (rāšāʿ, "the wicked") — the anchor term of M10b (Wickedness) — is occurrence-truncated.** It carries **180 distinct verses** in the study; rāšāʿ actually occurs in **~250 OT verses**, so **~70 verses (~28%) of its occurrences are missing.**
- **Its Proverbs coverage stops dead at chapter 21.** Chapters covered: 2–5, 9–21. **Chapters 22–31 are entirely empty** for H7563 — zero links — even though those verses exist in the corpus and contain "wicked": Pro 25:5 "take away the wicked from the king", 28:1 "the wicked flee", 29:16 "when the wicked increase", etc.
- This is the **signature of an extraction truncation**, not natural distribution: the coverage is contiguous from the start of the book and then cuts off — i.e. "took the first ~60 and stopped." (STEP caps query results at 60; H7563 has exactly **60** Proverbs links. Most-likely cause: the STEP pull for this high-frequency term hit the 60-row cap and the back third of Proverbs was silently dropped. **Mechanism to be confirmed**, but the gap itself is proven.)

### What is IMPRECISE in the statement
- **The verses are not "absent from M10/M10b/M10c entirely."** They are in the *corpus*; some are even in the M10 family under *other* terms — e.g. **Pro 29:16 IS in M10** via H6588 *pesha* "transgression"; Pro 28:1 is in the study under M19 (trust) and M26 (righteous). The gap is specifically the **rāšāʿ "wicked" term-linkage**, not the verses themselves.
- **One exception is a genuine verse-level absence: Pro 24:20** has **no verse-record at all** in the corpus ("the evil man has no future; the lamp of the wicked will be put out" — missing).

## Impact

- **M10b (Wickedness) is anchored on rāšāʿ.** Missing ~28% of its primary term's occurrences — concentrated in Proverbs 22–31, the densest "wicked vs righteous" material in Scripture — means the **M10b extract built 2026-06-22 inherits this gap**. Distilling M10b on it now would under-represent the term.
- M10 (Sin) and M10c (Defilement) are less affected (different anchor terms), but the same truncation mechanism could affect any high-frequency term pulled from STEP.

## Recommended remediation (not yet applied — researcher decision)

1. **Re-pull H7563 from STEP** with the canonical section-split logic (the client is supposed to halve sections that exceed 60; verify it did for Poetry/Proverbs) → recover the missing ~70 verses, ingest, and link into `verse_context` under M10b.
2. **Add Pro 24:20** (and audit for other verse-level absences in the wicked material).
3. **Regenerate the M10b extract** after re-linking; re-reconcile.
4. **Systemic check:** audit other high-frequency M10-family anchor terms (and beyond) for the same "stops mid-book" truncation signature before trusting their extracts. A quick test per term: does its book-by-book coverage cut off contiguously rather than spread across the whole book?

**Bottom line:** the researcher's instinct was right — there is a real, ~28% coverage hole in the central "wicked" term, with Proverbs 22–31 the visible casualty. It should be repaired (and the truncation checked for elsewhere) **before** M10b is distilled.

---

# Investigation + repair (2026-06-22) — full cycle

## Root cause (found + FIXED): the STEP client truncated the pull

STEP caps every search at **60 results** but reports the true `total`. `step_client.get_verse_records` beat the cap with a fixed **two-level** split (5 canonical sections → halve a section if >60). For rāšāʿ (H7563, true total **249**), the Poetry section (~134) was halved into `Poetry_A` (Job+Psalms ≈108) and `Poetry_B` (Proverbs+Ecc+Song ≈86) — **each half still exceeded 60**, and the client never recursed, so each silently truncated: **Psalms 34/80, Proverbs 60/77, Ecclesiastes 0/6.** The DB faithfully stored exactly what the client returned (180), so the gap was an *upstream pull* defect, not an ingestion error.

**Fix applied** — `scripts/analytics/step_client.py`: replaced the two-level split with a single cap-proof **forward-walk** (`_paginate_all`): query `<frontier>-Rev.22.21`, absorb the ≤60 rows, advance the frontier to the canonically-last verse seen, repeat until the remaining total fits one page. Needs only canonical book *order* (`_OSIS_ORDER`), no versification map. **Self-validates against STEP's reported total and warns on any shortfall** — silent truncation can never recur. All four paginating methods now share it. Verified: `get_verse_records('H7563')` → **249** (was 180); small terms unaffected; previously-missing verses now present.

## The cycle, stage by stage

1. **STEP ground truth:** 249 verses (oracle = STEP's reported total). ✓
2. **DB presence:** 180 in `wa_verse_records` (mti_term_id=1223) → **69 missing** (Ecc 6, Pro 17, Psa 46; full list in `outputs/_tmp_h7563_missing.json`). **0 stale** (no DB row absent from STEP).
3. **Status of existing 180:** all clean — `delete_flagged=0`, OWNER term, `verse_id`/`morph_code`/`book_id` all set, 1 legitimate set-aside, full parity with `verse_context`.
4. **Cluster of existing 180:** all → **M10b** (correct).
5. **Lexicals of existing 180:** 180/180 have `ve_lexical` VE values.

## The 69 missing verses — what a complete repair requires

- **66** already exist as canonical verses with morphology (measure layer reusable).
- **3** are wholly absent from the corpus (**Pro 24:20, Psa 94:3, Psa 106:18**) → need measure-layer ingest (canonical `verse` + `verse_morphology` + lexicon via STEP `getBibleText`).
- Each missing verse then needs: `wa_verse_records` row (mti_term_id=1223, OWNER, verse_id, morph) → `verse_context` shell (mti_term_id=1223 → inherits M10b) → `ve_lexical` (mechanical VE engine). The rich analytical fields (`analysis_note`, `keywords`, l2 meaning, subgroup) are **not** needed for the lexical extract — they are produced later when M10b is re-distilled from the corrected extract.

## Blast radius

`audit_word` operates per-**registry**. H7563's owner is **registry 172 ("wickedness")**, which also owns: **H7561** ra.sha "be wicked" (M26, 34 verses — likely also truncated), H4849 (M10b, 1), G0458 (M30, 5), H3644G (T2, 306). A registry-wide re-audit would re-sync all five (and likely fix sibling truncation in H7561), but touches M26/M30/T2 too.

## Proposed remediation (awaiting go-ahead on scope)

**Pipeline (engine-correct):**
1. `python scripts/word_study_extract.py --word wickedness` — re-pull registry 172 via the **fixed** client (now returns 249 for H7563).
2. `python -m engine.engine --mode=audit_word --registry=172 --dry-run` then live — insert the missing `wa_verse_records` (additive; preserves analytical/phase-2/session flags; flags-not-deletes).
3. Measure-layer ingest for the 3 corpus-absent verses (M60 path).
4. Create `verse_context` shells for the new occurrences; run the VE engine (`_ve_engine_v2.py`) → `ve_lexical`.
5. Regenerate the **M10b** extract; reconcile (expect M10b in-scope to rise by the H7563 additions).

**Scope options:**
- **(A) Registry-wide (recommended):** run the pipeline on registry 172 — fixes H7563 *and* any sibling truncation (esp. H7561 in M26) in one pass. Wider, but uses the engine's own idempotent path.
- **(B) Targeted H7563-only:** ingest just H7563's 69 — narrowest blast radius, but hand-rolls steps the engine normally owns.

**Recommendation:** (A), with a dry-run at each write and reconciliation against the STEP oracle after each stage. The client fix (root cause) is already in place and is independently committable.

**Open:** systemic audit — re-pull every high-frequency anchor term (any term whose DB count looks low vs a whole-book STEP total) through the fixed client to find other truncations across the programme.

---

# Pre-flight audit for the registry-172 ingest (2026-06-22) — answering each guardrail

Researcher chose **(A) registry-wide** with five guardrails. Investigation per guardrail:

## (1) ALL missing terms in registry 172 — STEP total vs DB
| Strong's | term | cluster | STEP | DB | gap | verdict |
|---|---|---|---|---|---|---|
| **H7563** | rāšāʿ "wicked" | **M10b** | 249 | 180 | **69** | **cap-truncation** (Psa 46 / Pro 17 / Ecc 6 — whole ranges). **FIX.** |
| H3644G | kᵉmô "like/as" | T2 | 126 | 54 | 72 | cap-affected, but a **T2 grammatical particle** (comparison), excluded from extract fan-out, low value; has XREF + 37 legit set-asides. **Decide separately.** |
| G0458 | anomia | M30 | 13 | 5 | 8 | **NOT truncation** (13<60, no cap). The 8 are span-filter/English-tag differences; the 5 all carry span matches. **No action.** |
| H7561 | rāšāʿ "be wicked" | M26 | 34 | 34 | 0 | complete |
| H4849 | miršaʿaṯ | M10b | 1 | 1 | 0 | complete |

→ Only **H7563** is a clean, analytically-critical truncation. ke.mo is low-value T2; G0458 is not truncated.

## (2) Registry → cluster association
Cluster flows via `verse_context.mti_term_id → mti_terms.cluster_code`. New H7563 occurrences point to mti_term 1223 → **M10b** automatically. ✓ (verified on the existing 180).

## (3) XREF
**H7563 has NO XREF copies** — one `mti_terms` row (1223, OWNER), one `wa_term_inventory` (OWNER). Clean, nothing to mirror. (Only ke.mo H3644G has XREF copies — 3 mti rows, 2 XREF inventory — another reason to treat it separately.)

## (4) No duplicate verse-records
`wa_verse_records` is unique by (reference, term_id). The 69 are confirmed **genuinely absent** (0 stale; existing 180 all present). Ingest will be additive/idempotent — only the missing (reference, mti_term_id=1223) rows inserted; existing 180 untouched. Will verify post-write.

## (5) Set-aside reinstatement — ⚠ CONFLICT, needs your decision
The existing set-asides are **deliberate analytical decisions, not truncation artifacts**:
- **H7563 Num 35:31** — *"rāšāʿ in forensic/legal-verdict sense 'guilty of death', not the moral character of a wicked person — belongs to M10 act-of-moral-failure."* A sound scope call.
- **H7561 1Sa 14:47** — `no_inner_being`.
- **H3644G** — 37 set-asides, all `no_inner_being` (legit T2 comparison particles).

Reinstating these would **undo correct scope decisions**. Recommend **NOT** blindly reinstating; reinstate only if you judge a specific one wrong. (None of the 69 *new* verses are set-aside — they're net-new.)

## Cluster impact ≤ M11 (highlight)
**M10b "Wickedness" (Analysis Completed)** is the **only** sub-M11 cluster receiving additions — H7563's ~69 verses (minus any span-filter rejects). This grows the M10b corpus from 492 in-scope and **changes a completed cluster's evidence base** — which is exactly why it must be fixed before M10b is distilled. M26/M30 are >M11; T2 is a reference bucket. No other completed/in-progress cluster is touched.

## Recommended execution (H7563 only, engine-correct)
1. `word_study_extract.py --word wickedness` → fresh STEP JSON (fixed client).
2. `audit_word --registry=172 --dry-run` → confirm it proposes **only** H7563 verse inserts (+ ke.mo, which I'll exclude/hold) and **no** deletes/stale-resets on analysed data; then live.
3. Measure-layer ingest for the 3 corpus-absent verses (Pro 24:20, Psa 94:3, Psa 106:18).
4. verse_context shells (mti_term 1223) + VE engine → ve_lexical.
5. Regenerate M10b extract; reconcile to the new STEP oracle.

**Holds for your decision:** (a) include ke.mo (T2) or skip; (b) confirm leaving the legitimate set-asides as-is; (c) approve adding ~69 verses to the *completed* M10b.

---

# EXECUTED (2026-06-22) — H7563 repair complete

Researcher decisions: (1) **skip ke.mo** → targeted H7563-only (no registry-wide audit_word); (2) **leave the legitimate set-asides**; (3) produce the 69 as a **separate additional JSON** so the in-progress M10b work stays clean.

Pipeline run (pre-op snapshot `backups/bible_research_pre-h7563-ingest_20260622.db`):
1. `_apply_h7563_ingest_missing_69_20260622.py --live` — inserted **69 `wa_verse_records`** (mti_term 1223, OWNER, registry 172) + **69 `verse_context` shells**; dedup-guarded (0 duplicate-reference groups).
2. `_apply_ingest_verse_morphology.py --live` — created the **3 canonical verse rows** (Pro 24:20, Psa 94:3, Psa 106:18) + set `verse_id` on all 69 + fetched their morphology (measure layer).
3. `_apply_generate_ve_lexical_v2.py --live --vcids @…` (new `--vcids` scope) — generated **686 `ve_lexical` rows + 69 narration findings** for exactly the 69.
4. `build_ve_lexical_extract.py --cluster M10b --only-refs @…` (new `--only-refs` scope) — **separate additional JSON**: `Sessions-v2/M10b-Wickedness/Data/wa-ve-lexical-extract-M10b-additional-h7563-20260622.json` (69 verses · 170 occ · ~43k tokens).

**Verification (all guardrails):**
- H7563 now **249** distinct verses (was 180); all `verse_id`+`morph` set, `delete_flagged=0`, **0 duplicate references**.
- Cluster: all 249 → **M10b** (flows via mti_term 1223). XREF: H7563 has none — nothing to mirror.
- Set-asides: the 1 legitimate (Num 35:31) **preserved**, not reinstated.
- ve_lexical: **69/69** new verses carry a populated rāšāʿ node (sense/type/faculty/valence/how/compound).
- **M10b in-scope: 492 → 557** (the only ≤M11 cluster touched, as flagged).
- DB integrity `ok`, 0 FK violations.

**Client fix** (`step_client._paginate_all` forward-walk) committed value beyond H7563: it self-validates against STEP's total, so future high-frequency pulls can't silently truncate.

**Still open (separate tasks):** ke.mo (H3644G, T2) truncation left as-is per decision; the **systemic audit** of other high-frequency anchor terms for the same truncation signature.
