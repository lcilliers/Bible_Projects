# Cluster-finding citation model — design proposal

_Generated: 2026-05-07. Follow-up to the linkage analysis. Goal: a
DB-relational citation list per `cluster_finding` row, ready for
M05 forward-population and M06 back-fill tomorrow._

## What needs to exist

For each `cluster_finding` row, a list of zero or more **citations**:
pointers to the specific evidence (verse(s), verse-context group(s),
term(s), occasionally another finding) that supports the finding's
claim. Joinable, filterable, deletable, idempotent under re-apply.

## Existing pattern to model on

`wa_finding_entity_links` already encodes exactly this pattern for
the legacy `wa_session_b_findings` table:

```sql
CREATE TABLE wa_finding_entity_links (
    id              INTEGER PRIMARY KEY,
    finding_id      INTEGER NOT NULL,
    entity_type     TEXT NOT NULL,           -- 'verse' | 'group'
    entity_id       INTEGER,                 -- FK based on entity_type
    entity_strongs  TEXT,                    -- (currently unused)
    raised_date     TEXT NOT NULL,
    delete_flagged  INTEGER NOT NULL DEFAULT 0,
    FOREIGN KEY (finding_id) REFERENCES wa_session_b_findings(id)
)
```

Population in this table is sparse (287 rows across 2,883 findings, all
raised in 2026-04). The entity_strongs column was provisioned but not
used. Two entity types only: `verse` (220) and `group` (67).

We **cannot** reuse this table directly: its FK pins it to
`wa_session_b_findings`. A parallel table for cluster_finding is the
clean move.

## Proposed table — `cluster_finding_citation`

```sql
CREATE TABLE cluster_finding_citation (
    id              INTEGER PRIMARY KEY,
    finding_id      INTEGER NOT NULL,
    entity_type     TEXT NOT NULL
                     CHECK (entity_type IN
                            ('verse','group','term','subgroup','finding')),
    entity_id       INTEGER NOT NULL,
    entity_ref      TEXT,             -- human-readable label, e.g.
                                      -- "Psa 11:5" / "550-NEW-02" /
                                      -- "H8130 sa.ne". Stable across
                                      -- mti renumbering; useful for
                                      -- audit + report rendering.
    citation_role   TEXT,             -- 'primary' | 'illustrative' |
                                      -- 'contrast' | 'cross-ref' |
                                      -- 'silence' | NULL
    citation_seq    INTEGER,          -- 1-based position within the
                                      -- finding (preserves narrative
                                      -- order Psa 11:5 → Isa 1:14 …)
    quoted_excerpt  TEXT,             -- optional short pull-quote
                                      -- supplied by the AI author
    notes           TEXT,
    extract_method  TEXT,             -- 'authored' (set at find-time)
                                      -- | 'parsed_from_text'
                                      -- | 'manual_repair'
    raised_date     TEXT NOT NULL,
    last_updated_date TEXT,
    delete_flagged  INTEGER NOT NULL DEFAULT 0,
    FOREIGN KEY (finding_id) REFERENCES cluster_finding(id)
);

CREATE INDEX idx_cfc_finding ON cluster_finding_citation(finding_id);
CREATE INDEX idx_cfc_entity  ON cluster_finding_citation(entity_type, entity_id);
CREATE INDEX idx_cfc_active  ON cluster_finding_citation(delete_flagged);
```

### Entity-type semantics

| `entity_type` | `entity_id` resolves to | When to use |
|---|---|---|
| `verse` | `wa_verse_records.id` | A specific verse cited by the finding |
| `group` | `verse_context_group.id` | A whole group (a meaning-bucket) cited as the locus, e.g. "(group 550-NEW-02)" |
| `term` | `mti_terms.id` | The finding asserts something about a term in the abstract (rare; usually the verse already implies the term) |
| `subgroup` | `cluster_subgroup.id` | Cross-cluster comparisons / contrast ("M06-A is structurally distinct from M06-B …") |
| `finding` | `cluster_finding.id` | Cross-reference to another finding (typically a synthesis row pointing at evidence rows) |

Stay minimal initially — start with `verse`, `group`, `term`. Add
`subgroup` and `finding` only when a real instance demands them.

### `citation_role` controlled vocabulary (proposed)

| role | meaning |
|---|---|
| `primary` | the load-bearing evidence the finding rests on |
| `illustrative` | additional verses supporting the same claim |
| `contrast` | a verse that bounds the claim ("but cf. Psa 119:163, where …") |
| `cross-ref` | pointer to another sub-group / cluster finding |
| `silence` | cited *as* an absence (e.g. "no equivalent OT term, see …") |

`role` is nullable. For the M06 back-fill we'd populate just
`primary`/`illustrative`; `contrast`/`silence` come into play for the
T0 / T7 tier work where claims rest on patterns rather than single
verses.

## Population workflow

### M05 (forward, starts tomorrow)

Findings authored by Claude AI in Phase 8/9 already include verse refs
inline. The AI patch should also emit a structured citations array
alongside finding_text:

```json
{
  "type": "CLUSTER_FINDING",
  "cluster_code": "M05",
  "obs_id": 1234,
  "cluster_subgroup_id": 18,
  "finding_status": "finding",
  "finding_text": "...",
  "citations": [
    {"entity_type":"verse","ref":"Joh 13:34",
     "role":"primary","seq":1,"quoted_excerpt":"A new commandment..."},
    {"entity_type":"verse","ref":"Mat 5:44",
     "role":"illustrative","seq":2},
    {"entity_type":"group","ref":"571-001","role":"primary","seq":3}
  ]
}
```

`apply_session_patch.py` resolves `ref` strings to entity_ids
(verse: book+chap+verse + matching mti_term in the cluster; group:
group_code lookup) and writes both `cluster_finding` and the citation
rows in one transaction. If any ref fails to resolve, the patch halts
— the AI author must use canonical refs.

### M06 (back-fill)

814 findings already exist with verse refs embedded in `finding_text`.
Two paths:

1. **Parser-driven seed + AI validation**: a regex parser extracts
   verse refs (and `group NNN-…` mentions), creates citation rows with
   `extract_method='parsed_from_text'`, role=NULL. Then a single-pass
   AI sweep promotes the load-bearing one(s) to `role='primary'` per
   finding. Cheap, auditable, leaves AI judgment narrow.
2. **AI re-emits citations directly**: the AI re-reads each finding
   and emits a citations patch keyed by `cluster_finding.id`. Higher
   cost but role assignment in one step.

Recommend Path 1 for M06 (cheaper, the parser scaffolding becomes
reusable for any future text-only inputs); Path 2 for M05 since
findings haven't been written yet.

## Volume sanity

| Cluster | Findings (active, non-placeholder) | Verses in cluster | Terms |
|---|---|---|---|
| M05 | 0 (to author tomorrow) | 1,393 | 86 |
| M06 | 814 | 429 | 34 |

If average M06 finding cites ~2 entities, the M06 back-fill produces
~1,600 citation rows. Programme-wide at completion (assume ~46 clusters
× ~800 findings × 2 cites) the table sits around ~75k rows — well
within SQLite comfort.

## Cluster-prose extract impact

Once citations exist, the §1 Findings section of the prose extract
gains a citation column rendered as compact refs:

```
| Sub-group | Status | Finding | Citations |
|---|---|---|---|
| M06-A | finding | God himself is extensively the subject of hatred… | Psa 11:5*, Isa 1:14, Hos 9:15, Pro 8:13†, Psa 97:10, Psa 139:21 |
```

`*` = primary, `†` = contrast (or some other compact key). And the
prose generator can join through the citation table to retrieve the
actual `verse_text` for any cited verse without text-parsing.

## Decisions to confirm before tomorrow

1. **Table name** — `cluster_finding_citation` (verbose, clear) vs
   `cluster_finding_evidence` vs `cf_citation`. Recommend the first.
2. **Required vs optional fields** — make `citation_role` and
   `citation_seq` and `quoted_excerpt` nullable initially? (Yes —
   start permissive, tighten if the data warrants.)
3. **Entity-type set for v1** — `verse`, `group`, `term` only? Defer
   `subgroup` and `finding` until a real case appears?
4. **Patch-instruction shape** — should citations be a sub-array
   inside the existing CLUSTER_FINDING patch op, or a separate
   op-type (e.g. `CLUSTER_FINDING_CITATION`)? Recommend sub-array —
   keeps a finding and its citations in one atomic patch unit.
5. **Resolution rule when verse ref appears in multiple terms** —
   e.g. "Psa 11:5" exists for several Strong's in M06-A (sa.ne).
   Choose: (a) cite the verse against the term named by `entity_id`
   on the finding's sub-group anchor (preferred), or (b) cite all
   matching wa_verse_records rows (clutters). Recommend (a).
6. **Q-COV / coverage findings** — do these get citations too, or are
   they about the absence/concentration of evidence and therefore
   citation-free? Probably citation-free, but worth confirming.
7. **Should the cluster comprehensive report (`_generate_cluster_
   comprehensive_v1`) also render citations once populated?** Probably
   yes; one-line tweak to the report.

## Migration shape

Single migration adds the table + indexes; no data movement. Existing
`cluster_finding` rows untouched. Population is opt-in per cluster.

```sql
-- migration NN_add_cluster_finding_citation.sql
BEGIN;

CREATE TABLE cluster_finding_citation ( … as above … );
CREATE INDEX idx_cfc_finding ON cluster_finding_citation(finding_id);
CREATE INDEX idx_cfc_entity  ON cluster_finding_citation(entity_type, entity_id);

INSERT INTO schema_version (version, applied_at, description)
  VALUES ('3.20.0', strftime('%Y-%m-%dT%H:%M:%fZ','now'),
          'Add cluster_finding_citation for per-finding evidence linkage.');

COMMIT;
```

(Version bump is a placeholder — slot into the next available
schema_version when applied.)
