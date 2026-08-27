# VE / engine / reads — complete audit — 2026-06-17

**Prefix:** wa · **Type:** State audit (read-only evidence) · **Scope:** the full day's work — engine alignment, base rerun, corpus API reads — and the resulting `ve_lexical` state. Evidence gathered via `scripts/_check_ve_full_audit.py` + targeted queries on the live DB.

---

## 0. Verdict

**The database is healthy, internally consistent, and the read pass is COMPLETE.** Integrity clean, no orphans, no FK violations, all M01 pilot reads preserved, the day's engine fixes verified on real data. **All four read fields converged to 0 M-cluster residue** (location · cause · object-type · divine-involvement); **valence parked** for your next-cluster evaluation. A sampled accuracy spot-check **passed** (read values correct and context-sensible). **31,182 read-API rows** in the corpus. Nothing requires rollback.

> **UPDATE 2026-06-17 (final):** the API usage-cap blocker was cleared (you raised the Console limit); object-type + divine-involvement reads ran to completion. This audit now reflects the **completed** state.

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
| **object-type** | full | **0** | ~2,900 | ✅ DONE (abstract 3,835 · person 3,537 · situation 1,360 · thing 1,151 · God 952 · spiritual-being 147 · threat 41) |
| **divine-involvement** | full | **0** | 2,900 | ✅ DONE (agent 1,667 · possessor 626 · object 545 · addressee 482 · giver 349) |
| **valence** | mech only | n/a (no UNRESOLVED token) | — | ⏸ PARKED (your next-cluster eval) |

**Read pass COMPLETE — 0 M-cluster residue across all four fields.** T2 residue is intentional (T2 never read by design). Total read spend across the session ≈ **$14** (location $0.5 · cause $3.5 · object-type ~$6 · divine $4.3).

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

1. **✅ RESOLVED — reads complete.** (History: credit-balance blocker → topped up; then a Console usage/spend cap → raised. object-type + divine then ran to 0 residue.) No outstanding read work except the parked valence.
2. **Valence** — parked for your next-cluster evaluation (forbidden ~80% ceiling; commanded/righteous/neutral interpretive).
3. **T2 interpretive fields** — cause/divine/object-type residue on T2-content is by design (T2 never analysed standalone). Confirm this is the intended permanent disposition, or decide a future treatment.

---

## 6. Risks / researcher attention

- **Read-rule validation scope.** The mechanical rules (valence, divine) were validated against the read on **M01 only**. They're applied corpus-wide via the base rerun. The next-cluster evaluation (esp. valence) is the check on generalisation.
- **Reads are the trusted interpretive layer**, mechanical the cheap floor. A **sampled accuracy spot-check passed** (Gen-1 samples: divine `agent`, object-type `thing`, cause "God's observation of…" — all correct). The check was a small sample, not exhaustive; a broader accuracy read-back per cluster is still worthwhile (folds into the 01b §6b read-back acceptance gate). Note also: some clustered terms are membership-questionable (e.g. Gen 1 "living creatures" = animals) — a *cluster-scope* question, separate from read accuracy.
- **Cross-cutting zero-pad risk** — other scripts that compare Strong's to hardcoded short literals may carry the same latent bug (memory `reference_strongs_zero_padded_4digit_in_db`).

---

## 7. Deliverables (the two requested reports)

- [wa-ve-api-updated-overview-20260617.md](../../outputs/wa-ve-api-updated-overview-20260617.md) — all API-updated items by field/cluster/value.
- [wa-ve-status-by-cluster-by-veitem-20260617.md](../../outputs/wa-ve-status-by-cluster-by-veitem-20260617.md) — cluster × VE-item coverage (mechanical/read/pending).
- Both **regenerate** with `python scripts/export_ve_status_reports.py` after the remaining reads complete.

---

*Read-only audit; no DB change. Snapshot retained for rollback. Session narrative: [wa-autonomous-session-log-20260617.md](wa-autonomous-session-log-20260617.md).*
