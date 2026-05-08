# Tier Questions ↔ Verses / Terms — DB linkage analysis

_Generated: 2026-05-07. Investigation prompted by the M06 prose-extract
design discussion: when feeding a tier-question finding into a prose
generator, does the schema let us also pull the supporting verse(s) and
term(s)?_

## Short answer

**For the cluster-process model (the one that produced the 1,516 M06
findings): no direct link exists.**

`cluster_finding` ties a tier question (`obs_id`) to a sub-group bucket
(`cluster_subgroup_id`) only. There is no FK from the finding to a
specific `wa_verse_records` row or `mti_terms` row. The cited verses /
terms inside `finding_text` are textual citations only — they are not
relational and cannot be enumerated by a join.

The verse/term inventory **for the sub-group as a whole** is reachable
(`mti_terms.cluster_subgroup_id` → terms; those terms' verses via
`wa_verse_records.mti_term_id`). But that is sub-group scope, not
finding scope.

## Linkage map (what the schema actually offers)

```
                  ┌─────────────────────────────────────────────┐
                  │   wa_obs_question_catalogue (412 rows)      │
                  │   obs_id · question_code · tier (T0..T7)    │
                  └─────────────────────────────────────────────┘
                              ▲              ▲              ▲
                              │              │              │
              obs_id          │   question_id│   question_id│
                              │              │              │
   ┌─────────────────────┐    │    ┌─────────────────────┐  │
   │ cluster_finding     │────┘    │ wa_finding_         │  │
   │ (1,516 rows, NEW)   │         │ catalogue_links     │  │
   │ obs_id              │         │ (6,199 rows, legacy)│  │
   │ cluster_code        │         │ finding_id ─────────┼──┐
   │ cluster_subgroup_id │         │ coverage / status   │  │
   │ finding_text        │         └─────────────────────┘  │
   └─────────────────────┘                                  │
              │                                             │
              │  cluster_subgroup_id                        │
              ▼                                             │
   ┌─────────────────────┐                                  │
   │ cluster_subgroup    │     ┌─────────────────────┐      │
   │ subgroup_code/label │     │ wa_session_b_       │      │
   └─────────────────────┘     │ findings (2,883)    │◀─────┘
              │                │ id · registry_id    │       finding_id
              │ via            │ term_id (FK)        │
              │ mti_terms.     │ anchor_verses (TXT) │
              │ cluster_       └─────────────────────┘
              │ subgroup_id              │
              ▼                          │ id
   ┌─────────────────────┐               │
   │ mti_terms (FK)      │     ┌─────────────────────┐
   └─────────────────────┘     │ wa_finding_         │
              │                │ entity_links (287)  │
              │                │ finding_id          │
              ▼                │ entity_type         │
   ┌─────────────────────┐     │  = verse | group    │
   │ wa_verse_records    │     │ entity_id           │
   └─────────────────────┘     └─────────────────────┘
                                        │
                                        ▼
                            (wa_verse_records.id  or
                             verse_context_group.id)
```

Plus a flag-routing channel for the 12 evidence-coverage questions:

```
   ┌─────────────────────┐
   │ wa_quality_flag_    │
   │ types (29 rows)     │
   └─────────────────────┘
           │   id
           ▼
   ┌─────────────────────┐    question_id
   │ wa_flag_type_       │────────────────► wa_obs_question_catalogue
   │ question_link (12)  │                  (only Q-COV-01..12, no tier)
   └─────────────────────┘
           │   flag_type_id
           ▼
   ┌─────────────────────┐
   │ wa_data_quality_    │
   │ flags (19,298 rows) │
   │ term_id  · file_id  │
   └─────────────────────┘
```

## What that means for prose-feeding

| Question | Has DB-level link to verses? | Has DB-level link to terms? |
|---|---|---|
| Tier T0–T7 question via `cluster_finding` | **No** — only sub-group bucket | **No** — only sub-group bucket |
| Tier T0–T7 question via legacy `wa_session_b_findings` | Partial (sparse, 220 verse rows in 287-row table) | **Yes** — `term_id` FK + `wa_finding_entity_links` |
| Q-COV-01..12 evidence flag questions | Yes — via flag instance on a verse-bearing term | **Yes** — `wa_data_quality_flags.term_id` |

Three usable consequences:

1. **Cluster prose seed cannot be assembled by SQL alone**: to attach
   verse/term evidence to a cluster finding, you must (a) parse the
   verse refs out of `finding_text` itself (textual extraction), or
   (b) treat the finding as scoped to the whole sub-group and pull the
   sub-group's anchor + verse-context evidence en bloc.

2. **The legacy registry-scope findings (`wa_session_b_findings`) DO
   give per-finding term/verse linkage** — via `term_id` and
   `wa_finding_entity_links`. If we wanted dense evidence-tied prose,
   the *registry-scope* path (older model) is actually richer in
   relational structure than the *cluster-scope* path.

3. **Anchor verses remain the cleanest evidence handle for cluster
   prose**: `verse_context_group` (with its `context_description`)
   plus `vc.is_anchor=1` gives one canonical verse per group-scope
   meaning, fully relational, no text parsing required. That is the
   spine the M06 prose extract is already using.

## Recommendation

For the cluster-prose-generator design, treat the unit as:

- **Sub-group** (label + core_description), with
- **anchor verses** (one per active group, with group context_description), plus
- **Findings filtered by sub-group + Q-code**, with
- **Term meaning detail** for the terms inside the sub-group.

Don't try to attach individual cluster-finding rows to specific
verse_record_ids in the schema — that link does not exist. If
finding-level verse provenance turns out to be necessary, add a new
join table (e.g. `cluster_finding_evidence_links` mirroring
`wa_finding_entity_links` but discriminated against `cluster_finding.id`)
and back-fill from the citations already embedded in `finding_text`.

## Investigation evidence

- `cluster_finding` schema: `id, obs_id, cluster_code,
  cluster_subgroup_id, finding_status, finding_text, source_file,
  version, notes, delete_flagged, created_at, last_updated_date` —
  **no verse_record_id, no term_id, no entity link.**
- `wa_finding_entity_links` finding_id range = 196..340; all 287 rows
  match `wa_session_b_findings.id` and 0 rows fall outside it. The
  numeric overlap with `cluster_finding.id` is coincidental; this
  table is a Session-B-only mechanism.
- `wa_finding_catalogue_links` finding_id range = 196..2,883 — also
  Session-B-scope.
- `wa_flag_type_question_link` only routes Q-COV-01..12 (the 12 evidence
  flag questions, all `tier=NULL`) to the four `VERSE_EVIDENCE_*` flag
  types. Tier T0–T7 questions are **not** in this routing table.
- `wa_data_quality_flags` ties a flag instance to a `term_id` (Strong's
  string), giving an indirect path question → flag → term, but only
  for the Q-COV evidence questions, not the analytical T0–T7 set.
