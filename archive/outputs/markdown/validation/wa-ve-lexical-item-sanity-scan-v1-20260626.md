# ve_lexical — item inventory + sanity scan (hunting faculty-style non-sense)

- **File:** wa-ve-lexical-item-sanity-scan-v1-20260626.md · **2026-06-26 · Author:** Claude Code · read-only.
- **Goal:** list every active item in `ve_lexical` with coverage, and flag any item with "non-sensical properties" like the faculty over-fire we just fixed.

## 1. Full item inventory (active rows only)

| ve_nr | item | rows | units | verses | distinct values | const% (per-term) |
|---:|---|---:|---:|---:|---:|---:|
| 0 | lexical_note | 40,405 | 40,405 | 19,158 | 25,981 | — |
| 1 | sense | 40,405 | 40,405 | 19,158 | 5,204 | 34% |
| 2 | type | 40,405 | 40,405 | 19,158 | 4 | 89% |
| 3 | compound | 82,002 | 32,438 | 11,223 | 2,113 | — |
| 5 | location | 6,664 | 6,009 | 2,144 | 8 | 56% |
| 6 | **origin** | 3,623 | 3,623 | 2,512 | **1** | **100%** |
| 7 | faculty | 22,128 | 17,161 | 10,620 | 10 | 99%* |
| 8 | divine-involvement | 11,187 | 11,187 | 7,143 | 6 | 63% |
| 11 | immediate-response | 6,633 | 6,633 | 4,711 | 4,272 | — |
| 13 | relational | 8,609 | 7,983 | 5,884 | 351 | 41% |
| 16 | object | 20,577 | 20,577 | 13,230 | 3,264 | — |
| 16 | object-type | 20,028 | 20,028 | 12,815 | 8 | 46% |
| 17 | cause | 5,695 | 5,695 | 3,379 | 2,996 | — |
| 18 | how | 16,424 | 16,424 | 10,683 | 5,452 | — |
| 19 | intensity | 4,928 | 4,431 | 2,656 | 314 | 49% |
| 20 | experiencer | 27,478 | 27,478 | 15,437 | 3 | 43% |
| 21 | valence | 26,993 | 26,993 | 14,613 | 5 | 50% |
| 22 | cause_clause | 9,826 | 9,826 | 4,267 | 4,180 | — |
| 23 | from-source | 8,831 | 7,378 | 3,569 | 1,247 | 39% |
| 24 | instrument | 715 | 650 | 316 | 184 | — |
| 25 | purpose | 6,338 | 6,338 | 3,664 | 2,699 | — |
| 26 | quality-bearer | 2,088 | 2,088 | 1,654 | 635 | 40% |
| 27 | operation | 634 | 634 | 513 | 427 | 62% |
| 28 | isolable | 5,399 | 5,399 | 2,775 | 1 | 100% |
| 29 | discovery | 40,308 | 40,308 | 19,115 | 25,910 | — |

*const% = % of terms whose value never changes across any of its verses (the faculty over-fire signature). \*faculty's 99% is now legitimate (monovalent faculty-words are constant by nature; only seats vary).
**Totals:** 40,642 distinct units · 19,176 distinct verses.

## 2. Findings — flagged in priority order

### 🔴 origin (ve_nr 6) — the clearest non-sense, same class as old faculty
- **Only ONE value exists in the entire field:** `received-from-outside` (3,623 rows), 100% per-term constant.
- An "origin" property that can only ever say one thing carries **zero information** — it is a presence-flag wearing a property's name, or a half-built field that was meant to contrast (e.g. self-generated / innate / from-God / received-from-outside) but only the one branch was ever populated.
- **Action needed:** either (a) complete it — define the contrasting origin values and re-derive from the verse, or (b) retire/rename it to an honest flag. As-is it should not feed any analysis.

### 🟠 object-type (ve_nr 16) — overlapping/redundant taxonomy
- Values: person 5,349 · thing/abstract 4,443 · **abstract 4,128** · God 3,051 · situation 1,468 · **thing 1,256** · spiritual-being 286 · threat 47.
- `thing`, `abstract`, and `thing/abstract` are three overlapping buckets for what should be one decision — a taxonomy-hygiene problem that makes the field ambiguous. **Action:** collapse to a single clean scheme (e.g. person / God / spiritual-being / abstract / concrete-thing / situation / threat) and remap.

### 🟡 divine-involvement (ve_nr 8) — high UNRESOLVED
- `UNRESOLVED` = 5,140 of 11,187 rows (**46%**) — nearly half the field is a non-answer (inflates its 63% constancy). The other values (agent/object/possessor/addressee/giver) are sound. **Action:** this is a known exegesis-gate backlog item, not broken — but the field is half-empty-of-meaning until those resolve.

### 🟡 valence (ve_nr 21) — conflated axes
- Values: neutral · righteous · sinful · commanded · forbidden. This mixes a **moral-status** axis (righteous/sinful) with a **deontic** axis (commanded/forbidden) under one label. Not non-sensical, but two concepts in one field. **Action (optional):** split into moral-status + deontic, or rename to "moral_valence" and accept the blend.

### 🟢 By-design, not bugs (noted so they're not mistaken for faults)
- **isolable (1 value 'no'):** a presence-flag — a row exists only when the verse is *not* isolable. Constant by design.
- **experiencer (3 values: self / other / other-addressed):** a coarse grammatical role, verse-varying (57%). Fine, just coarse.
- **type (4 values, 89% constant):** action/status/quality is semi-intrinsic to a term, so high constancy is expected; 129 UNRESOLVED is minor.
- **faculty (post-reset):** verse-grounded now; constancy is the monovalent faculty-words, not over-fire.

## 3. Recommendation
**origin** is the next faculty-style fix (single-value = non-discriminating). **object-type** is a remap, not a rebuild. The rest are either by-design or known backlog. Suggest tackling **origin** the same way faculty was done: decide the contrasting values, derive from the verse, reversible write. Awaiting your direction.
