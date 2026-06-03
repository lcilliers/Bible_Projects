# Foreign-key audit + remediation proposal

**Date:** 2026-05-05
**Trigger:** *"Nothing should be hidden in scripts. (a) Does every term have a cluster field referenced to a cluster table? (b) Does every anchor verse have a column referencing the term?"*

---

## 1. Audit answers — both NO

### (a) Term → cluster: **NO** ❌

- `mti_terms` has **no cluster column**. Existing FKs from `mti_terms` are only `owning_registry_fk` → `word_registry` and `word_data_ref_fk` → `wa_file_index`.
- M-cluster identity (M01..M46 + T2 + FLAG) exists **only in JSON** (`outputs/markdown/wa-term-anchor-v6-20260504.json`).
- There is no `m_cluster` table in the database.
- `word_registry.cluster_assignment` (e.g. `'C17'`) is a TEXT field, not FK'd, and refers to *legacy* C-clusters — not M-clusters.
- Every script that needs to know "what M-cluster does this term belong to?" must load JSON.

### (b) Anchor verse → term: **NO** ❌

- `wa_session_b_findings.anchor_verses` is plain TEXT — comma-separated references like `"Gen 8:1, Exo 2:24, Deu 5:15"`.
- No FK to `wa_verse_records`. No FK to `mti_terms`. No normalised child table.
- Every script that wants to know "which terms does this finding's anchor verses point to?" must:
  1. Parse the text.
  2. Look up book name → book_id.
  3. Expand verse ranges.
  4. Query `wa_verse_records` for matching (book_id, chapter, verse_num).
- `wa_session_b_findings.term_id` IS a FK to `mti_terms` — but it is `NULL` on all 2,883 active rows (the field exists but was never populated).

### Adjacent issue worth flagging

- `wa_session_research_flags.strongs_reference` is plain TEXT (e.g. `"G3340"`), not FK'd to `mti_terms.strongs_number`. SD pointer → term is also script-only.

---

## 2. The principle being enforced

**Data relationships should live in the schema, not in scripts.** Scripts that have to parse text fields and resolve at runtime hide the structure of the data, prevent indexing/querying, and rely on undocumented contracts (like the book-name aliases I added to the resolver). Foreign keys make the relationships:

- Discoverable by any tool that reads the schema
- Enforceable (referential integrity)
- Indexable (for performance)
- Queryable in plain SQL without parsing

This is consistent with the *"don't pay twice"* principle: we are **not redoing analysis**, only normalising relationships that already exist (currently in JSON or in parsed text). No data is thrown away; existing analytical content is preserved verbatim alongside the new FKs.

---

## 3. Proposed minimum schema additions

### 3.1 New table: `m_cluster`

```sql
CREATE TABLE m_cluster (
  cluster_id    TEXT PRIMARY KEY,        -- 'M01'..'M46', 'T2', 'FLAG'
  label         TEXT NOT NULL,           -- 'Love, Compassion and Kindness'
  description   TEXT,                    -- (optional, free-form)
  generated_date TEXT,                   -- ISO date when this row entered
  source        TEXT                     -- 'meaning_v1', 'meaning_v2_supplement_2', etc.
);
```

**Initial population:** 47 rows from `wa-term-anchor-v6-20260504.json` `meaning_cluster_labels` field.

### 3.2 New columns on `mti_terms`

```sql
ALTER TABLE mti_terms ADD COLUMN m_cluster_id          TEXT REFERENCES m_cluster(cluster_id);
ALTER TABLE mti_terms ADD COLUMN m_bucket              TEXT;     -- 'T1','T2','QUALIFIERS','LOCI','EXTRACTION-NOISE','GENERICS','FLAG'
ALTER TABLE mti_terms ADD COLUMN m_cluster_source      TEXT;     -- provenance: 'meaning_v1','meaning_v2_supplement_2','bucket_sweep_FLAG', etc.
ALTER TABLE mti_terms ADD COLUMN legacy_cluster_id     TEXT;     -- 'H011','G003' from v1 anchor (preserved provenance)
ALTER TABLE mti_terms ADD COLUMN legacy_cluster_label  TEXT;     -- 'mourning/mourn/weep' etc.
```

**Initial population:** join from `wa-term-anchor-v6-20260504.json` `term_anchors` keyed by Strong's. 2,491 OWNER terms get populated; remaining mti_terms rows (~5,080 XREF / non-anchored) get NULLs.

**Index:** `CREATE INDEX idx_mti_terms_mcluster ON mti_terms(m_cluster_id);`

### 3.3 New table: `wa_finding_anchor_verse`

```sql
CREATE TABLE wa_finding_anchor_verse (
  id              INTEGER PRIMARY KEY,
  finding_id      INTEGER NOT NULL REFERENCES wa_session_b_findings(id),
  book_id         INTEGER NOT NULL REFERENCES books(id),
  chapter         INTEGER NOT NULL,
  verse_num       INTEGER NOT NULL,
  raw_ref         TEXT,                     -- the original 'Lev 19:17' text, for audit
  parsed_date     TEXT
);

CREATE INDEX idx_finding_anchor_verse_finding ON wa_finding_anchor_verse(finding_id);
CREATE INDEX idx_finding_anchor_verse_locator ON wa_finding_anchor_verse(book_id, chapter, verse_num);
```

**Initial population:** parse `anchor_verses` text on every active finding (1,432 with non-empty values) using the resolver already built in `_resolve_finding_anchor_verses_v1_20260505.py`. Expected: ~3,679 rows with ~3% unresolved (typos like "Phili" → can be resolved or skipped).

**To get from finding → term:** join `wa_finding_anchor_verse` → `wa_verse_records` on (book_id, chapter, verse_num) → filter `mti_term_id`. The relationship is then queryable in pure SQL, no scripts needed.

### 3.4 Optional: backfill `wa_session_research_flags.mti_term_fk`

```sql
ALTER TABLE wa_session_research_flags ADD COLUMN mti_term_fk INTEGER REFERENCES mti_terms(id);
```

**Initial population:** for every active SD pointer with a single-Strong's `strongs_reference`, look up `mti_terms.id` by `strongs_number` and populate. Multi-Strong's references (e.g. `"G3340 metanoeō, G3341 metanoia"`) need the existing TEXT field for now — a separate child table could normalise these but adds complexity.

Pointer → term FK fixes the pointer-affinity logic too.

### 3.5 Optional: a denormalised `m_finding_term` view (or table)

```sql
CREATE VIEW m_finding_term AS
SELECT DISTINCT
  fav.finding_id,
  vr.mti_term_id,
  mt.strongs_number,
  mt.m_cluster_id,
  fav.raw_ref AS via_anchor_ref
FROM wa_finding_anchor_verse fav
JOIN wa_verse_records vr
       ON vr.book_id = fav.book_id
      AND vr.chapter = fav.chapter
      AND vr.verse_num = fav.verse_num
      AND COALESCE(vr.delete_flagged,0) = 0
JOIN mti_terms mt ON mt.id = vr.mti_term_id;
```

Now any analyst can write:

```sql
SELECT finding_id, COUNT(*)
  FROM m_finding_term
 WHERE m_cluster_id = 'M06'
 GROUP BY finding_id
 ORDER BY 2 DESC;
```

— no parsing, no scripts, just SQL.

---

## 4. What this does NOT do

- **No data deletion.** `verse_context`, `wa_session_b_findings`, `wa_session_research_flags` content is unchanged; new columns/tables sit alongside.
- **No migration of legacy analytical content** (groups, dimensions, etc.). Those stay in their existing tables.
- **No engine impact.** Engine constants (`EXPECTED_SCHEMA_VERSION`) advance to a new version (e.g. 3.18.0); all engine flows are unaffected by the addition of M-cluster columns.
- **No re-paying for AI work.** All content is re-derived from existing JSON + existing TEXT fields. Zero new AI calls.

---

## 5. Migration path — one-shot script

```text
Step 1 — schema migration (creates m_cluster, adds columns, creates wa_finding_anchor_verse)
         engine.engine --migrate  (or one-off CREATE/ALTER script)

Step 2 — populate m_cluster from wa-term-anchor-v6-20260504.json (47 rows)

Step 3 — populate mti_terms columns from wa-term-anchor-v6-20260504.json
         (2,491 terms updated; 5,080 left NULL — by design, those aren't in the anchor)

Step 4 — populate wa_finding_anchor_verse by parsing anchor_verses on
         all active findings (~3,679 rows expected)

Step 5 — populate wa_session_research_flags.mti_term_fk for single-Strong's
         pointers (~600 of 657)

Step 6 — create m_finding_term view

Step 7 — verify with sanity queries:
           SELECT m_cluster_id, COUNT(*) FROM mti_terms WHERE m_cluster_id IS NOT NULL GROUP BY 1;  -- should match v6 cluster sizes
           SELECT COUNT(*) FROM wa_finding_anchor_verse;  -- should ~= 3,679
           SELECT m_cluster_id, COUNT(DISTINCT finding_id) FROM m_finding_term WHERE m_cluster_id='M06';  -- should = 51 for M06
```

Estimated effort: **2-3 hours** for the migration script + backfill + verification queries.

---

## 6. After migration — what changes in scripts

The `_assess_m_cluster_coverage_v1` script currently:
- Reads v6 JSON to get M-cluster term assignments
- Indexes wa_verse_records to resolve anchor verses
- Re-parses book names every run

After migration:
- Reads `mti_terms` directly: `SELECT strongs_number FROM mti_terms WHERE m_cluster_id = ?`
- Reads `m_finding_term` view directly: `SELECT * FROM m_finding_term WHERE m_cluster_id = ?`
- No JSON load, no parsing, faster, simpler.

The v6 JSON becomes the *audit trail of how the DB was populated* — useful for provenance but no longer the runtime source of truth.

---

## 7. Decision sought

Two confirmations before I write the migration:

1. **Approve schema additions** — m_cluster table, 5 columns on mti_terms, wa_finding_anchor_verse table, optional mti_term_fk on wa_session_research_flags, m_finding_term view.
2. **Confirm that the v6 JSON anchor is the source of truth for the initial backfill** — once populated to DB, future M-cluster changes should go through DB updates, not by re-loading JSON.

If approved, I'll write `engine/migrations/00XX_add_m_cluster_layer.sql` (or a one-shot script) and run it against `bible_research.db`.

If not approved as proposed (e.g. you want a different shape), I can iterate the design.
