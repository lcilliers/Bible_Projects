---
name: cluster table + mti_terms.cluster_code now live in DB (2026-05-05)
description: M-cluster identity is now in the database as proper FK relationships, populated from v6 JSON anchor. Scripts should query DB directly, not load JSON.
type: project
originSessionId: 0b9d95eb-ab3c-4fd3-9dd9-6341794c07de
---
The M-cluster identity that was finalised on 2026-05-04 (v6 term-anchor) is now **persisted as DB schema** as of 2026-05-05.

**Schema added:**

```sql
CREATE TABLE cluster (
    cluster_code      TEXT PRIMARY KEY,    -- 'M01'..'M46', 'T2', 'FLAG' (47 rows)
    description       TEXT,                -- longer-form description (initial = gloss)
    gloss             TEXT NOT NULL,       -- short canonical label
    source            TEXT,                -- 'meaning_v2'
    bucket            TEXT,                -- 'NAMED' (45) | 'SUPPLEMENTARY' (T2) | 'REVIEW' (FLAG)
    status            TEXT,                -- 'active'
    version           TEXT,                -- 'v6'
    last_updated_date TEXT
);
ALTER TABLE mti_terms ADD COLUMN cluster_code TEXT REFERENCES cluster(cluster_code);
CREATE INDEX idx_mti_terms_cluster ON mti_terms(cluster_code);
```

**Population:** all values from `outputs/markdown/wa-term-anchor-v6-20260504.json`. 47 cluster rows; 4,209 mti_terms rows updated (covering 2,364 distinct Strong's, matching v6 exactly).

**Why:** The user's principle — *"the database must have proper references (FK) for all key relations. Nothing should be hidden in scripts."* The previous arrangement (M-cluster lives only in JSON, scripts must load it) was rejected.

**Migration script:** `scripts/_apply_cluster_schema_v1_20260505.py` (idempotent, transactional, backed up DB before changes to `backups/bible_research_20260505_145214_pre_cluster_schema.db`).

**How to apply:**
- Term → cluster: `SELECT cluster_code FROM mti_terms WHERE strongs_number = 'H8130'`
- Cluster → terms: `SELECT strongs_number FROM mti_terms WHERE cluster_code = 'M06'`
- Cluster identity: `SELECT * FROM cluster WHERE cluster_code = 'M05'`

**Known caveat — mti_terms duplicates:** The mti_terms table has 3,616 duplicate rows (3,955 distinct Strong's in 7,571 rows) — this is the open OT-DBR-009 issue. Duplicate Strong's rows all carry the same `cluster_code` (consistency preserved). For analytical queries, group by `strongs_number` or use DISTINCT.

**Not yet migrated:**
- Anchor verses on findings (still TEXT in `wa_session_b_findings.anchor_verses` — proposed `wa_finding_anchor_verse` table awaiting approval).
- SD pointer term references (`wa_session_research_flags.strongs_reference` still TEXT, not FK'd).

**Implication for scripts:** The `_assess_m_cluster_*` family of scripts can now read from `mti_terms.cluster_code` instead of loading the v6 JSON. The v6 JSON remains the authoritative *historical record* of how the cluster table was populated, but is no longer the runtime source.
