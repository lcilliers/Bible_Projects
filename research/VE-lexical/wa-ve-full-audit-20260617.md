# VE / engine / reads — complete audit — 2026-06-17

**Prefix:** wa · **Type:** State audit (read-only evidence) · **Scope:** the full day's work — engine alignment, base rerun, corpus API reads — and the resulting `ve_lexical` state. Evidence gathered via `scripts/_check_ve_full_audit.py` + targeted queries on the live DB.

---

## 0. Verdict

**The database is healthy and internally consistent.** Integrity clean, no orphans, no FK violations, all M01 pilot reads preserved, the day's engine fixes verified on real data. The corpus is in a **known, documented, resumable** state. The only incomplete work is the **two remaining read fields (divine-involvement, object-type ~13k M-cluster items)**, halted by an **API usage cap** (credits were loaded, but a configured spend limit is reached; resets 2026-07-01 or raise it in the Console — §5) — not a code or data fault. Nothing requires rollback.

---

## 1. Integrity (all pass)

| Check | Result |
|---|---|
| `pragma quick_check` | **ok** |
| `pragma foreign_key_check` | **0 violations** |
| schema_version | 3.34.0 |
| ve_lexical rows on delete-flagged verse_context (orphans) | **0** |
| divine `present` non-value rows remaining | **0** (old stub fully replaced) |
| M01 pilot reads preserved through base rerun | ✅ valence 1036 · divine 331 · object-type (incl new) · cause (≥297) |
| Rollback snapshot | `backups/bible_research_pre-baserun-20260617.db` (500 MB) |

---

## 2. Scale & provenance

- `ve_lexical`: **364,160 rows** (358,693 active). **38,971 active v2 units** (= 40,739 − 1,768 T2-grammatical disposed; reconciles exactly).
- Provenance: `v2_engine_iter1` 308,200 · `audit` (lexical_note) 38,971 · **read-API 16,989** (cause 7,743 · object-type 6,774 · location 1,105 · valence 1,036 · divine 331).
- Narration: **30,571 active** `l2_meaning`; 69,509 soft-deleted (supersession history).

---

## 3. Read coverage — the core status

Residue = items still mechanically unresolved (the read target). **M-cluster** is the analytical scope; **T2** is reference-only and **never read by design** (01c §A3), so its residue is expected and permanent until a future decision.

| Field | M-cluster resolved | M-cluster residue | T2 residue (by design) | Status |
|---|---|---|---|---|
| **location** | full | **0** | 226 | ✅ DONE (26 spirit-seat · ~1,058 NONE) |
| **cause** | full | **0** | 1,882 | ✅ DONE (3,253 causes · ~4,193 NONE) |
| **object-type** | 7,573 | **3,019** | ~2,900 | ◍ PARTIAL — blocked |
| **divine-involvement** | 256 (M01 only) | **9,944** | 2,900 | ⏸ NOT STARTED — blocked |
| **valence** | mech only | n/a (no UNRESOLVED token) | — | ⏸ PARKED (your next-cluster eval) |

**True remaining read work (M-cluster): divine 9,944 + object-type 3,019 = 12,963 items**, blocked on the API usage cap (§5). Estimated ~$8 to finish.

---

## 4. Engine compliance (post-fix state)

The five Phase-0 changes committed today (full matrix in [wa-ve-engine-compliance-audit-v1-20260617.md](wa-ve-engine-compliance-audit-v1-20260617.md)):

| Item | State |
|---|---|
| **Zero-pad fix** (`H430`→`H0430`) | ✅ foundational — restored Elohim/`'al`/`'et`/faculty detection; *much of the earlier "stub" appearance was this bug* |
| valence context | ✅ prohibition→forbidden mechanical (~80%, al-tira ceiling — flagged for next-cluster eval); rest → read |
| divine-involvement | ✅ object (adjacency/`'et`) mechanical @92%; rest → read; `present` removed |
| location dedup (I1) | ✅ one row per distinct seat-level |
| T2 treatment (01c) | ✅ grammatical T2 excluded from generation/JSON/reads |

### Outstanding engine items (NOT yet done — for a later iteration)
These remain partial/unimplemented; none block the reads, but they are open per the compliance matrix:
- **faculty R2** — co-occurring faculty-lemma assignment unimplemented (R1 term-intrinsic only). `FACULTY_LEMMA` list still dead code for assignment.
- **compound multi-role** (C-4/C-6) — one role per co-term only; no object-of/cause-of.
- **produces-effect (VE12)** — not implemented (0 rows).
- **object-type N1 precision (I3)** — N1 still picks the wrong object word in some verses (`'of'`/`name`/`law`/determiners); the **read compensates**, so object-type is correct after reads, but the mechanical object is imperfect.
- **origin** — only `'from'`-prep→received; within-person/generational/C-5 giver↔origin pairing unimplemented.
- **relational** — preposition text only, no {direction→object}, no expectation test.
- **sense medium_def (P9)** — sense row carries `target_word` only; lemma `medium_def` is available downstream in the extract but not in the sense row.
- **type=UNRESOLVED 129** — measure-layer morph gap (terms with no POS); a small backfill worklist (down from 1,897 pre-rerun).

### Acceptance gate not yet run
The engine's own **read-back audit (01b §6b — founded + coverage, loop-until-dry)** has **not** been run as a per-cluster acceptance gate. Recommended before declaring any cluster's lexical "complete."

---

## 5. Blocked / outstanding (action needed)

1. **⛔ API usage cap reached** — credits were topped up (that blocker cleared), but a **configured usage/spend limit** is now hit: `400 invalid_request_error: "You have reached your specified API usage limits. You will regain access on 2026-07-01 at 00:00 UTC."` This is **distinct from credits** — it's a spend cap set in the Anthropic Console. **Action: raise the monthly usage limit (Console → Plans & Billing → Usage limits), or wait until 2026-07-01.** Then resume (resumable, residue-only):
   ```text
   python scripts/_run_ve_reads_governed.py --field object-type --live --verses-per-batch 45
   python scripts/_run_ve_reads_governed.py --field divine-involvement --live --verses-per-batch 45
   # re-run each once more to converge → 0, then regenerate reports:
   python scripts/export_ve_status_reports.py
   ```
2. **Valence** — parked for your next-cluster evaluation (forbidden ~80% ceiling; commanded/righteous/neutral interpretive).
3. **T2 interpretive fields** — cause/divine/object-type residue on T2-content is by design (T2 never analysed standalone). Confirm this is the intended permanent disposition, or decide a future treatment.

---

## 6. Risks / researcher attention

- **Read-rule validation scope.** The mechanical rules (valence, divine) were validated against the read on **M01 only**. They're applied corpus-wide via the base rerun. The next-cluster evaluation (esp. valence) is the check on generalisation.
- **Reads are the trusted interpretive layer**, mechanical the cheap floor — both confirmed reliable in their lane, but the corpus reads (location, cause, partial object-type) have **not been spot-audited for accuracy** beyond the driver's self-verify (completeness, not correctness). A sampled accuracy read-back is advisable.
- **Cross-cutting zero-pad risk** — other scripts that compare Strong's to hardcoded short literals may carry the same latent bug (memory `reference_strongs_zero_padded_4digit_in_db`).

---

## 7. Deliverables (the two requested reports)

- [wa-ve-api-updated-overview-20260617.md](../../outputs/wa-ve-api-updated-overview-20260617.md) — all API-updated items by field/cluster/value.
- [wa-ve-status-by-cluster-by-veitem-20260617.md](../../outputs/wa-ve-status-by-cluster-by-veitem-20260617.md) — cluster × VE-item coverage (mechanical/read/pending).
- Both **regenerate** with `python scripts/export_ve_status_reports.py` after the remaining reads complete.

---

*Read-only audit; no DB change. Snapshot retained for rollback. Session narrative: [wa-autonomous-session-log-20260617.md](wa-autonomous-session-log-20260617.md).*
