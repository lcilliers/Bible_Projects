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
Every hard gate G0–G8 returns its pass value, the audit clears 90% sound with zero fidelity failures, and the G8 delta is positive — then Proverbs is successfully re-read.

*Filed 2026-07-08. The queries are the acceptance test; run them at chapter close and at book close.*
