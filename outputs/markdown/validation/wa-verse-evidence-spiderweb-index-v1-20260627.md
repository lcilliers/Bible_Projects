# Verse↔evidence spiderweb index — build + usage

- **File:** wa-verse-evidence-spiderweb-index-v1-20260627.md · **2026-06-27 · Author:** Claude Code.
- **Goal (researcher):** a trustworthy, complete, superfast, well-grounded binding of a verse to ALL related evidence, built from every end, never blind to something just because one FK is broken. Foundation for the verse-fan-out operating model.

## 1. What was built (reversible: DROP the 3 tables; rebuild with the script)
- **`verse_evidence_index`** (804,805 rows, indexed on verse_id) — every DIRECT, verse-specific evidence item bound to its verse, with the bind path recorded:
  - `span` 305,961 (all 23,593 verses) · `lexical` 423,968 (19,172 verses) · `unit` 42,871 (19,477) · `finding_verse` 32,005 (16,929).
  - Every verse (23,593) has ≥1 evidence (at minimum its spans).
- **`verse_term_index`** (275,593 verse-term pairs, indexed) — the lateral web foundation: verse↔term and term↔verse.
- **`verse_evidence_orphan`** (222 rows) — the not-blind guarantee: only 222 empty `unit`s on verse-records with NULL verse_id. **0 orphan lexicals, 0 orphan findings.**

## 2. Built from all ends (trust)
- **Verse → evidence:** spans/units/lexicals/findings resolved via the verse_record path (`vc → wa_verse_records.verse_id`), each row tagged with its `bind_path` + `confidence='direct'`.
- **Term → verses:** `verse_term_index` (from morphology, the source of truth) — gives every verse a term carries, and confirms the verse→term and term→verse lists are the same set by construction.
- **Every finding asked "can this bind to a verse?":** VERSE findings → bound directly (32,005, 0 orphan); CLUSTER/GLOBAL findings (2,892) are **not verse-specific** → bound *indirectly* through term→cluster (see §3), never dropped.
- **Span / lexical:** bound directly; orphan-checked (0).

## 3. Retrieval patterns (superfast — 24–42 ms full, including indirect)
**Direct evidence for a verse (one indexed query):**
```sql
SELECT evidence_type, COUNT(*) FROM verse_evidence_index WHERE verse_id=? GROUP BY evidence_type;
```
**Indirect — cluster/global findings reachable from a verse (via its terms):**
```sql
-- verse -> verse_term_index -> mti_terms.cluster_code -> finding(CLUSTER/GLOBAL)
```
**Indirect — related verses (sharing a term):**
```sql
SELECT DISTINCT vti.verse_id FROM verse_term_index vti
WHERE vti.primary_strong IN (SELECT primary_strong FROM verse_term_index WHERE verse_id=?) AND vti.verse_id!=?;
```
**Proof:** Exo 1:13 (never analysed; spans only) reaches 1 cluster finding + 3,691 related verses via term M36. Gen 6:8 reaches 19 cluster findings + 5,420 related verses.

## 4. Honest limit — "related" is currently COARSE
"Related verses (shared term)" returns large sets (3,691 / 5,420) because *any* shared term links verses. **The index provides the complete lateral substrate; it does NOT pre-decide what counts as *meaningfully* related** — that is the open methodological question (operating-model §5). Future relatedness measures (shared *movement*, shared observation/question, weighted by term rarity, context-adjacency) ride on top of this substrate without rebuilding it.

## 5. Why it is trustworthy
- **Anchored on `verse`** (the stable control total) — verse-king.
- **Every bind path is recorded** (auditable, not hopeful).
- **Orphans surfaced, not hidden** (222, all empty-unit FK breaks).
- **Rebuildable + reversible** (`scripts/_apply_build_verse_evidence_index_v1_20260627.py`).
- Fast by construction (indexed; sub-50ms full retrieval).
