# Do G3–G5 measure dimension quality/completeness? — gap analysis + proposed additions (2026-07-09)

> Researcher challenge: do the gates cover (1) all qualifiers considered; (2) all pairs identified; (3) pairs read back for sense; (4) qualifiers considered for hidden meaning; (5) a missing dimension is deliberate, not a gap. **Verdict: G3–G5 test the fidelity of what IS recorded; they do NOT test the completeness of what SHOULD be recorded. Four of the five are not adequately covered.**

## What G3–G5 actually measure
- **G3** — every recorded value carries a resolution state (grounded), and no imported/over-called characteristic. *Checks recorded values; says nothing about absent ones.*
- **G4** — recurring terms not flattened. *Distinction, not completeness.*
- **G5** — cohesive multi-verse units show at least one cross-verse pair. *A narrow subset — cross-verse pairs only; silent on in-verse pairs, which are the majority.*

## Your five concerns vs current coverage
| # | concern | covered? | why |
|---|---|---|---|
| 1 | all **qualifiers** considered | ❌ no | nothing checks that every relational span is pulled into a characteristic as a pair member, nor that a qualifier-roled span actually binds to a characteristic |
| 2 | all **pairs** identified | ❌ no | no completeness check on pairs; G5 only counts *cross-verse* pairs in cohesive units |
| 3 | pairs **read back** for sense | ⚠ partial | only in the sampled 25-unit audit, loosely; no gate; pair *structural* integrity unchecked |
| 4 | qualifiers for **hidden meaning** | ⚠ partial | only via G6 (a discovery entry exists per verse); not qualifier-specific. NB: "hidden meaning" was **dropped as a dimension** (catalogue §4 D12) — it now lives in the discovery channel (114) + figurative/exegesis routing |
| 5 | missing dimension **deliberate, not a gap** | ❌ no | **the biggest hole.** G7 catches blank rows that *exist*; it does NOT catch a dimension with **no row at all**. An absent dimension is invisible to every current gate |

**Root cause:** the gates never assert a **completeness ledger** — that every applicable dimension of a characteristic is *explicitly present* with a state. Under the P4 model a dimension must be `resolved | none | unknown`; "absent" is not a legal fourth state, but nothing enforces it.

## Proposed additions

### G3b — completeness ledger (answers #5, and underpins #1/#2)
Every characteristic span must carry an **explicit entry** (`resolution ∈ span/inferred/unknown/none`) for each dimension in a **mandatory-consideration set M**. An *absent* mandatory dimension = fail; `none` must be written, not omitted — that is what makes a missing value **deliberate and auditable**.
- Proposed **M** (confirm): 101 sense · 102 type · 103 source · 104 seat · 105 bearer · 106 operation · 107 target · 108 manner · 111 effect · 112 coupling. (Optional/rare — 109 intensity, 110 specifier, 113 prohibition, 116 locus — may default to none.)
```sql
-- characteristic spans missing an explicit entry for any mandatory dimension
WITH M(ve_nr) AS (VALUES (101),(102),(103),(104),(105),(106),(107),(108),(111),(112))
SELECT COUNT(*) FROM verse_span_index s JOIN verse v ON v.id=s.verse_id
WHERE v.book_id=20 AND s.role='characteristic' AND s.role_provenance='read-2026'
  AND EXISTS (SELECT 1 FROM M WHERE NOT EXISTS (
     SELECT 1 FROM ve_lexical l WHERE l.verse_span_id=s.id AND l.ve_nr=M.ve_nr
        AND l.source_provenance='reread-pro-2026' AND COALESCE(l.delete_flagged,0)=0));
```
**PASS = 0.** *(Note: this requires the read to emit explicit `none` rows — a real write-behaviour requirement, not just a query.)*

### G9 — pair & qualifier integrity (answers #1, #2, structural half of #3)
```sql
-- (a) ORPHAN qualifiers: roled qualifier but bound to no active pair (violates 'qualifiers always pair')
SELECT COUNT(*) FROM verse_span_index s JOIN verse v ON v.id=s.verse_id
WHERE v.book_id=20 AND s.role IN ('qualifier','process-qualifier') AND s.role_provenance='read-2026'
  AND NOT EXISTS (SELECT 1 FROM ve_lexical l WHERE (l.from_span=s.id OR l.to_span=s.id)
     AND l.pair_kind IS NOT NULL AND COALESCE(l.delete_flagged,0)=0);
-- (b) MALFORMED pairs: pair_kind set but an endpoint missing, or no resolution
SELECT COUNT(*) FROM ve_lexical l JOIN verse_span_index s ON s.id=l.verse_span_id JOIN verse v ON v.id=s.verse_id
WHERE v.book_id=20 AND l.source_provenance='reread-pro-2026' AND COALESCE(l.delete_flagged,0)=0
  AND l.pair_kind IS NOT NULL AND (l.from_span IS NULL OR l.to_span IS NULL OR l.resolution IS NULL);
-- (c) DANGLING endpoints: a pair points at a span outside the unit's passage/verse-set
--     (join to_span -> verse -> passage/segment membership; count out-of-unit endpoints)
```
**PASS = 0 / 0 / 0.** (a) every qualifier binds to a characteristic; (b) every pair is well-formed; (c) every pair endpoint is a real span in scope.

### Audit rubric additions (the judgment layer — what queries cannot prove)
The gates prove *presence and structure*; only a read-back can prove the calls are *right*. Add scored items to the 25-unit audit:
- **`none`-call correctness** — spot-check dimensions marked `none`: was a value really absent, or was a pair/qualifier **missed**? *(This is the true test of "all pairs/qualifiers identified" — #1/#2.)*
- **pair sensibility** — is each pair's direction, `pair_kind`, and resolution semantically right? *(#3)*
- **standalone-vs-qualifier** — is any relational span wrongly left standalone that should bind as a qualifier? *(#1)*
- **hidden/figurative sense** — for each qualifier, was a non-literal sense considered (body-part→faculty, "clean hands"→conduct) and logged in discovery(114)? *(#4)*
- **threshold unchanged:** ≥90% sound, zero fidelity failures; any missed pair on a `none`-call = a fidelity failure.

## Net effect
- #5 (missing = deliberate) → **enforced by G3b** (absent dimension fails; `none` must be explicit).
- #1/#2 (qualifiers/pairs complete) → **structural half by G9**, **semantic half by the `none`-call + standalone-vs-qualifier audit**.
- #3 (pairs make sense) → **structural half by G9(b/c)**, **semantic half by pair-sensibility audit**.
- #4 (hidden meaning) → **discovery presence by G6**, **qualifier-figurative check by audit** (hidden meaning is not a dimension — it is a discovery/exegesis concern).

## Decisions for the researcher
1. Confirm the **mandatory-consideration set M** (above) — which dimensions must always be explicitly stated.
2. Confirm we adopt **G3b + G9 + the four audit items**, and that the read must **emit explicit `none` rows** (write-behaviour change).
3. On confirm: update the success-criteria doc, extend the measurement script, and **re-run the baseline** (the numbers will shift — G3b/G9 will likely fail hard on the prior data, which is correct: it never recorded a completeness ledger).

*Filed 2026-07-09. The gaps are real; the additions close them. Awaiting confirmation before baking in.*
