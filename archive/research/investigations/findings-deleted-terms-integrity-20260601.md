# Findings — the deleted-terms integrity problem

**Type:** findings statement · **Date:** 2026-06-01 · **Status:** for researcher review · **Author:** Claude Code
**Purpose:** Clearly define what was discovered, what is wrong, and what should have been done — *before* any change or roll-back. Replaces the terse "CRITICAL" banner in the remediation plan as the authoritative statement of findings.
**All claims below are from read-only queries against the live DB and the 2026-05-28 backup, and from the documented schema (`docs/database-table-analysis.md`). Fact and inference are kept separate; limits of knowledge are stated in §4.**

---

## 1. What I discovered

A verse record (`wa_verse_records`) links to a term **two different ways**, and the documented design says they have **different completeness**:

| link | column | type | documented completeness (`database-table-analysis.md`) |
|---|---|---|---|
| legacy / always-present | `term_id` | TEXT (the Strong's code, e.g. `G3958`) | **Complete — 99.99%** (line 362) |
| modern cross-registry FK | `mti_term_id` | INTEGER FK → `mti_terms.id` | **Functional — 98%; 5,249 NULL from "pre-MTI-linking imports"** (line 381) |

**The discovery:** I built my "does this term still have live verses?" signal on `mti_term_id`. Because 5,249 verse records have `mti_term_id` NULL (their `term_id` is present), **any term whose live verses are legacy-imported reads as "0 live verses" under my signal — and therefore as "safe to delete."**

**The proof case — G3958 (*paschō*, "to suffer"):**
- 41 verse records are active (`delete_flagged=0`) under `term_id='G3958'`.
- 0 of them carry an `mti_term_id` (all 41 are NULL — legacy-imported).
- So my signal reported G3958 as having no live verses.
- You confirmed via STEP that G3958 is a **real term that should be in a cluster with ~41 verses**.

---

## 2. What is wrong — three separate things

These must not be blurred together. One is pre-existing and not mine; two are mine, today.

### (a) A pre-existing, DOCUMENTED data gap — not mine, not new
5,249 `wa_verse_records` have `mti_term_id` NULL. This is a *known* completeness gap, explicitly noted in the schema documentation ("Functional 98% — pre-MTI-linking imports"). It is **not corruption** and **not something today's work created**. The verses are intact; only the modern FK was never backfilled on them.

### (b) My analysis method was wrong — mine, today
I judged "evidence" using the field the documentation flags as **incomplete** (`mti_term_id`) instead of the **complete** one (`term_id`). Consequently every "0 active verses / evidence-safe / empty term" judgement I produced this session **undercounts evidence by exactly the legacy-NULL rows.** This flaw is shared by:
- the `a_verses` / `a_vc` columns in my listings,
- the B+D backfill's "evidence-safe" guard,
- Stream C's "evidence-safe" guard.

### (c) Acting on that method, I buried real terms — mine, today
Today's writes (Stream C: 671 flags · B+D backfill: 2,131 reason-stamps, of which 562 also newly set `delete_flagged=1`) changed **2,802 `mti_terms` rows**. Re-judged on the **complete** signal (`term_id`), against the 05-28 backup:

| outcome (judged on `term_id`) | strongs | live verses | severity |
|---|--:|--:|---|
| **Buried TODAY** — had a live term row this morning, none now, yet live verses exist | **36** | **1,625** | **serious** |
| Already fully deleted before today; today only added a reason | 8 | 119 | pre-existing |
| Had a row touched but a live sibling row survives (concept intact, a redundant row mislabelled) | 77 | 2,038 | minor |

**The 36 buried-today strongs are coherent inner-life families**, not noise:
- Greek suffering / grief: G3958 *paschō*, G3804 *pathēma*, G3077 *lupē*, G2552/G2553 *kakopatheia/kakopatheō*, G3805 *pathētos*, G4777 *sunkakopatheō*, G3663 *homoiopathēs*
- Hebrew craftsman / deaf-silent: the *cheresh / charash* family (H2758, H2759, H2791A/B, H2793H, H2794, H2795, H2796, H2799, H4281)
- Hebrew toil / affliction: *amal / atsav / anah* (H5998, H6001B, H6031A, H6033, H6039, H6087B, H6089B, H6090B, H6092)
- the *qol* "voice" family (H6963A/B/H/I/J/K/L)
- plus the prepositions G3844 *para*, G4862 *sun*

**Concrete trace of the mechanism (G3958):** G3958 was a "decided-delete but not yet flagged" desync (category C). Stream C's guard checked `mti_term_id`-linked records, saw all of them deleted, declared it "evidence-safe," and set `delete_flagged=1` — **while 41 live verses sat under its `term_id`.** That is exactly how a real term got buried.

**Two mitigations, stated honestly:**
1. **No verse records were touched.** Today's writes only changed term-row metadata (`delete_flagged`, `exclusion_reason`). The verses themselves are intact, so this is **fully reversible**.
2. But I gave you a **false assurance**: I described the backfill as "evidence-safe — 2,131 empty terms, only missing a reason." That claim was wrong; at least 562 of those were not empty, and Stream C buried real terms too.

---

## 3. What should have been done

- **Read the schema readiness notes first.** The documentation already flags `mti_term_id` as 98% / legacy-NULL. Trusting it as a completeness signal without reading that was the root mistake.
- **Define "no live evidence" on the complete signal:** a term is safe to treat as evidence-free only if it has **no active records under `term_id` AND none under `mti_term_id` AND no active `verse_context`.** Any one of these being non-empty = the term carries evidence.
- **Validate "empty," never assert it.** The "2,131 empty terms" figure should have been checked against `term_id` before any write, and certainly before telling you it was safe.
- **Give no "evidence-safe" assurance without that validation.**

---

## 4. What I do NOT know (limits of these findings)

- **Why each term was originally deleted.** You confirmed G3958 is a wrong deletion. I have **not** verified the other 35 buried-today terms individually — I have only shown they share G3958's *structure* (deleted term + live `term_id` verses). Some may be genuinely deletable terms whose verses should also have been cleaned up. **Each needs its own STEP / researcher check; I should not assume all 36 are wrong deletions.**
- **The history of the `mti_term_id` orphaning** beyond the docs' "pre-MTI-linking imports" note — when and how the FK was left NULL.
- **Whether the 77 live-sibling cases** are duplicate rows to merge or genuine distinct senses.

---

## 5. Current state (nothing further has been changed)

- **F→FLAG (206 terms):** applied and intact — non-destructive `cluster_code` reassignment, unaffected by the above.
- **Stream C (671 flags) + B+D backfill (2,131 stamps):** applied; now known to rest on the flawed signal.
- **2026-05-28 backup:** verified as the *exact, complete* pre-today state of `delete_flagged` / `exclusion_reason` (0 rows differ otherwise). A surgical reversal is therefore available.
- **No reversal, no reinstatement, no further write has been performed.** Awaiting your direction once these findings are clear.

---

## 6. The correct path — disposition from span (truth), now computed

The right state and rule (researcher, 2026-06-01): **each Strong's term once; each verse for a term once; truth = whether the term is genuinely used in the verse (`span_strong_match=1`), not `delete_flagged`.**

Applied read-only ([term-disposition-by-span-20260601.md](term-disposition-by-span-20260601.md), `scripts/inspect_term_disposition_by_span_v1_20260601.py`), deduping terms→Strong's and verses→distinct reference:

| disposition | terms | meaning |
|---|--:|---|
| CLUSTERED | 1,632 | in a real M-cluster — fine |
| REVIEW (used, not clustered) | 2,107 | has span usage → relevance check → cluster or set aside |
| DELETE (no usage) | 226 | no span usage → not attested → delete |

**Divergence proving the flags are corrupt:** **1,146 terms are currently *fully deleted* yet carry span usage** (wrongly deleted). Only 74 live-unclustered terms are genuinely unused (deletable); 8 used `term_id`s have no term row (term-list gaps).

**Therefore the correct sequence is:**
1. **Reverse today's flag-based writes** (surgical restore from 05-28 backup) — they were driven by the corrupt signal; keep F→FLAG.
2. **Dedup the term list** to one row per Strong's (OT-DBR-009) and the verse list to one row per term-verse — so the foundation is clean.
3. **Rebuild disposition from span** (this assessment): the 226 truly-unused → delete; the 2,107 used-but-unclustered → relevance review (relevant = cluster, not relevant = set aside); the 8 term-list gaps → add the missing term rows.
4. `delete_flagged` is then a *derived* result of this truth, never the input to it.

## Supporting evidence (read-only artefacts, this folder)
- [g3958-span-survival-test-20260601.md](g3958-span-survival-test-20260601.md) — the G3958 trace.
- [deleted-but-live-terms-20260601.md](deleted-but-live-terms-20260601.md) — the corpus-wide scan.
- [today-writes-severity-20260601.md](today-writes-severity-20260601.md) — the buried-today / live-sibling split.
- [mti-diff-vs-backup-20260601.md](mti-diff-vs-backup-20260601.md) — exact diff of today's writes vs the 05-28 backup.
