# Proverbs re-read — success criteria + how success is measured (2026-07-08)

> The study objective for re-reading Proverbs and the **quantified** tests that decide whether it was achieved. Two kinds of measure: **HARD GATES** (mechanical queries, pass/fail, must all pass) and **AUDIT MEASURES** (a scored read-back sample — for the things a query cannot prove, judged honestly). A book is "successfully re-read" only when **every hard gate = its pass value AND the audit clears its threshold with zero critical fidelity errors.**
>
> **Provenance tags this read stamps** (so before/after is queryable): `verse_span_index.role_provenance = 'read-2026'`; `ve_lexical.source_provenance = 'reread-pro-2026'`; `verse.process_marker = 'reread-pro-2026'`. Scope in every query: `verse.book_id = 20`.

## The objective (plain)
Understand and describe **how the characteristics of the inner being actually work, as the verses of Proverbs express them** — completely, faithfully to the text, with distinctions preserved, and with the interaction between verses that belong together brought to light.

---

## HARD GATES (all must pass)

### G0 — Digestion budget (the structural pre-condition)
*Aim: no reading unit is so crowded it forces selective analysis.*
```sql
-- char-spans per reading unit that exceed the budget
SELECT su.unit_code, COUNT(*) AS char_spans
FROM segment_unit su
JOIN segment_unit_verse suv ON suv.unit_id = su.id
JOIN verse_span_index s ON s.verse_id = suv.verse_id AND s.char_candidate = 1
WHERE su.book='Pro' AND COALESCE(su.delete_flagged,0)=0
GROUP BY su.unit_code
HAVING COUNT(*) > 12;         -- budget = 12 char-spans/unit (tunable)
```
**PASS = 0 rows.** (Every unit is digestible; the 6 F-frames must be gone.)

### G1 — Nothing passed over (completeness of attention)
*Aim: every char is actually read and accounted for.*
```sql
-- (a) candidate char spans with no re-read decision
SELECT COUNT(*) FROM verse_span_index s JOIN verse v ON s.verse_id=v.id
WHERE v.book_id=20 AND s.char_candidate=1
  AND (s.role_provenance IS NULL OR s.role_provenance <> 'read-2026');
-- (b) char-bearing verses not marked read by this pass
SELECT COUNT(DISTINCT v.id) FROM verse v
WHERE v.book_id=20
  AND EXISTS (SELECT 1 FROM verse_span_index s WHERE s.verse_id=v.id AND s.char_candidate=1)
  AND (v.process_marker IS NULL OR v.process_marker <> 'reread-pro-2026');
```
**PASS = 0 and 0.**

### G2 — Every characteristic is *worked*, not just named
*Aim: a characteristic carries its working, never a bare label.*
```sql
-- characteristic spans with no read-derived lexical at all
SELECT COUNT(*) FROM verse_span_index s JOIN verse v ON s.verse_id=v.id
WHERE v.book_id=20 AND s.role='characteristic' AND s.role_provenance='read-2026'
  AND NOT EXISTS (SELECT 1 FROM ve_lexical l WHERE l.verse_span_id=s.id
     AND l.source_provenance='reread-pro-2026' AND COALESCE(l.delete_flagged,0)=0);
-- characteristic spans missing the operation dimension (106) = named but its action not read
SELECT COUNT(*) FROM verse_span_index s JOIN verse v ON s.verse_id=v.id
WHERE v.book_id=20 AND s.role='characteristic' AND s.role_provenance='read-2026'
  AND NOT EXISTS (SELECT 1 FROM ve_lexical l WHERE l.verse_span_id=s.id AND l.ve_nr=106
     AND l.source_provenance='reread-pro-2026' AND COALESCE(l.delete_flagged,0)=0);
```
**PASS = 0 and 0.**

### G3 — Read *from* the verse, not into it (grounding)
*Aim: every value is warranted; nothing imported; silence left silent.*
```sql
-- (a) values asserted with no resolution state (ungrounded)
SELECT COUNT(*) FROM ve_lexical l
JOIN verse_span_index s ON s.id=l.verse_span_id JOIN verse v ON v.id=s.verse_id
WHERE v.book_id=20 AND l.source_provenance='reread-pro-2026'
  AND COALESCE(l.delete_flagged,0)=0 AND l.value IS NOT NULL AND l.resolution IS NULL;
-- (b) over-call: read as characteristic but seed never flagged it AND no discovery note
SELECT COUNT(*) FROM verse_span_index s JOIN verse v ON v.id=s.verse_id
WHERE v.book_id=20 AND s.role='characteristic' AND s.role_provenance='read-2026'
  AND s.char_candidate=0
  AND NOT EXISTS (SELECT 1 FROM ve_lexical l WHERE l.verse_span_id=s.id AND l.ve_nr=114);
```
**PASS = 0 and 0** (every over-call must be justified by a recorded discovery).

### G4 — Distinctions preserved (recurring terms not flattened)
*Aim: the same word doing different work is kept distinct.*
```sql
-- high-frequency candidate strongs whose readings collapse to ONE identical shape
-- (shape = concatenated ve_nr+value+resolution over the span's lexical)
WITH shape AS (
  SELECT s.id span_id, s.primary_strong,
         group_concat(l.ve_nr||':'||COALESCE(l.value,'')||':'||COALESCE(l.resolution,''),'|') sig
  FROM verse_span_index s JOIN verse v ON v.id=s.verse_id
  JOIN ve_lexical l ON l.verse_span_id=s.id AND l.source_provenance='reread-pro-2026'
  WHERE v.book_id=20 AND s.char_candidate=1 AND COALESCE(l.delete_flagged,0)=0
  GROUP BY s.id)
SELECT primary_strong, COUNT(*) occ, COUNT(DISTINCT sig) shapes
FROM shape GROUP BY primary_strong
HAVING COUNT(*) >= 5 AND COUNT(DISTINCT sig) = 1;
```
**PASS = 0 rows** (no term occurring ≥5× reads identically every time). Any hit → audit that verse-set.

### G5 — Belonging honoured (inter-verse interaction where it exists)
*Aim: multi-verse cohesive units read together, not in isolation.*
```sql
-- cohesive multi-verse units (D/T, ≥3 verses) with ZERO cross-verse links
SELECT su.unit_code, COUNT(DISTINCT suv.verse_id) verses
FROM segment_unit su JOIN segment_unit_verse suv ON suv.unit_id=su.id
WHERE su.book='Pro' AND COALESCE(su.delete_flagged,0)=0 AND su.unit_type IN ('D','T')
GROUP BY su.unit_code HAVING COUNT(DISTINCT suv.verse_id) >= 3
  AND NOT EXISTS (
    SELECT 1 FROM ve_lexical l
    JOIN verse_span_index a ON a.id=l.from_span
    JOIN verse_span_index b ON b.id=l.to_span
    WHERE a.verse_id IN (SELECT verse_id FROM segment_unit_verse WHERE unit_id=su.id)
      AND b.verse_id IN (SELECT verse_id FROM segment_unit_verse WHERE unit_id=su.id)
      AND a.verse_id <> b.verse_id AND l.source_provenance='reread-pro-2026');
```
**PASS = 0 rows** *(each such unit either shows a cross-verse link or is audited and confirmed to genuinely have none — the text may not afford one).*

### G6 — The unexpected surfaced (discovery-lookout ran everywhere)
*Aim: every read verse was interrogated for what we don't yet capture.*
```sql
-- read verses with NO discovery(114) entry (lookout skipped)
SELECT COUNT(DISTINCT v.id) FROM verse v
WHERE v.book_id=20 AND v.process_marker='reread-pro-2026'
  AND NOT EXISTS (SELECT 1 FROM verse_span_index s JOIN ve_lexical l ON l.verse_span_id=s.id
     WHERE s.verse_id=v.id AND l.ve_nr=114 AND COALESCE(l.delete_flagged,0)=0);
```
**PASS = 0** (each read verse records discovery — a finding or an explicit "none").

### G7 — Honest uncertainty (nothing smoothed over)
*Aim: what can't be settled is marked, not guessed.*
```sql
-- expected-but-blank: a relational dimension attempted with neither a value nor an
-- explicit none/unknown resolution (a silent blank = a smoothed-over gap)
SELECT COUNT(*) FROM ve_lexical l
JOIN verse_span_index s ON s.id=l.verse_span_id JOIN verse v ON v.id=s.verse_id
WHERE v.book_id=20 AND l.source_provenance='reread-pro-2026'
  AND COALESCE(l.delete_flagged,0)=0
  AND l.value IS NULL AND (l.resolution IS NULL OR l.resolution NOT IN ('none','unknown','inferred','span'));
```
**PASS = 0** (uncertainty is explicit, never a silent blank).

### G8 — Demonstrably better than the compromised read
*Aim: show what the prior read missed or got wrong.*
```sql
-- prior-read characteristics DROPPED by the new read with no recorded reason
SELECT COUNT(*) FROM verse_span_index s JOIN verse v ON v.id=s.verse_id
WHERE v.book_id=20
  AND EXISTS (SELECT 1 FROM ve_lexical l WHERE l.verse_span_id=s.id
     AND l.source_provenance IN ('lexical-model-2026') AND l.ve_nr=115 AND l.value='characteristic')
  AND s.role_provenance='read-2026' AND s.role<>'characteristic'
  AND NOT EXISTS (SELECT 1 FROM ve_lexical l WHERE l.verse_span_id=s.id AND l.ve_nr=114
     AND l.source_provenance='reread-pro-2026');   -- reason recorded in discovery
-- delta report (informational, must be POSITIVE):
--   new characteristics caught, roles corrected, blanks now filled vs prior provenance
```
**PASS = 0 unexplained drops**, and the delta report shows a **positive** net (new/corrected chars > 0; the 6 F-frame chapters now fully treated).

---

## AUDIT MEASURES (sampled read-back — for what a query cannot prove)
Queries prove *presence, grounding-state, and coverage*; they cannot prove the reading is **correct**. So a stratified read-back sample is scored:

- **Sample:** 25 units, stratified — the 6 former F-frame chapters (heaviest risk), plus a spread of D lectures, S sayings, and T threads.
- **Per unit, scored sound / weak / wrong on four points:** (1) *fidelity* — is each value actually warranted by the verse (no import)? (2) *working-completeness* — is the characteristic's operation + relations read where the verse affords them? (3) *movement* — for multi-verse units, is the genuine inter-verse movement captured (not fragments, not forced)? (4) *distinction* — are recurring terms read for their difference here?
- **Threshold:** ≥ 90% of sampled units "sound", **and zero "wrong" on fidelity** (an imported/fabricated warrant is a critical error → fix + re-audit the whole affected chapter).

## The one-line definition of "done"
Every hard gate returns its pass value, the audit clears 90% sound with zero fidelity failures, and the G8 delta is positive — then Proverbs is successfully re-read.

---

## AMENDMENT 2026-07-09 — dimension completeness gates + refinements (researcher-approved)
Runner: **`scripts/_check_proverbs_reread_measures_v2_20260709.py`** (supersedes v1).

### The dimension model — 18 dimensions (all must be gate-covered)
16 per-span (`ve_nr` 101–116) + 2 verse-level (`process`, `genre`). Each maps to a gate so **no dimension is an unmeasured gap**:
| # | dim (ve_nr) | gate that ensures it |
|---|---|---|
| 1–2 | sense 101 · type 102 | G10 (mandatory ledger) |
| 3 | source 103 | G10 + driver/restraint audit |
| 4–5 | seat 104 · bearer 105 | G10 |
| 6 | operation 106 | G10 + G2 |
| 7–8 | target 107 · manner 108 | G10 |
| 9–10 | intensity 109 · specifier 110 | G10 (optional — none allowed) |
| 11–12 | effect 111 · coupling 112 | G10 |
| 13 | prohibition 113 | G10 (optional) |
| 14 | discovery 114 | **G6** |
| 15 | role 115 | **G1** |
| 16 | locus 116 | G10 (optional, mechanical) |
| 17 | process | passage-level check / audit |
| 18 | genre | **G0** precondition (must be set) |
*(The 201-series — axis/polarity/source_domain… — is **Leviticus-only**, out of scope for Proverbs.)*
**Mandatory ledger set M = 101,102,103,104,105,106,107,108,111,112.**

### G3 stays; refinements to G3/G4/G7 (v1 false-result fixes)
- **G3** unchanged in intent, but grounding (resolution state) applies to **pairs only** (`pair_kind='pair'`). v1 wrongly flagged value/event/flag items → false 21,823; true value = pairs without resolution.
- **G4** signature uses **content items only** (`pair_kind IN value/event/flag`) so pair span-refs don't distort.
- **G7** silent-blank scoped to **content items** with a NULL value; pairs are checked by G9.

### NEW G9 — pair & qualifier integrity (PASS = 0/0/0)
(a) orphan qualifiers (a qualifier-roled span bound to no pair); (b) malformed pairs (endpoint or resolution missing); (c) dangling endpoints (a pair endpoint that is not a real in-scope span). **Requires span-id endpoints** (see below).

### NEW G10 — completeness ledger (PASS = 0) — the answer to "missing = deliberate"
Every characteristic must carry an **explicit** entry for each mandatory dimension M; an *absent* dimension fails; **`none` must be written, not omitted.** This is what makes an unrecorded dimension a *deliberate* decision rather than a silent gap.

### RE-READ REQUIREMENT — pair endpoints must be span ids
The current data encodes `from_span`/`to_span` as **Strong's strings** (e.g. `H0693@Pro 1:11`), not master span ids — which **violates the cycle's "key on span id, never strong" rule** (§7A). The re-read **must write integer span-id endpoints**. Until it does, G5/G9(a)/G9(c) are **not measurable** (they read as false-universal-fails on the old encoding and are reported `N/A`).

### Audit rubric additions (judgment layer)
`none`-call correctness (was a pair/qualifier *missed*?) · pair sensibility (direction/kind/resolution) · standalone-vs-qualifier correctness · qualifier hidden/figurative sense (logged in discovery 114). A missed pair on a `none`-call = a fidelity failure.

*Filed 2026-07-08; amended 2026-07-09. Run v2 at chapter close and book close.*
