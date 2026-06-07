# Characteristic-grouping + cluster observation — schema and load proposal

**Date:** 2026-05-18
**Author:** CC
**Trigger:** M04 characteristic map v4 is researcher-approved at the analytical level; need to (a) capture the 7-characteristic structure in the DB so Phase 9 can run per characteristic, and (b) capture the analytical observations in the map's "Notes for Phase 9" section so they're carried forward to post-findings evaluation.
**Status:** PROPOSAL FOR DECISION. Not applied. Decision blanks at §6 for researcher mark-up.

**Required inputs:**

| # | Document | Purpose |
|---|---|---|
| 1 | This proposal | Schema + data load + observation capture design |
| 2 | M04 characteristic map v4 — `Sessions/Session_Clusters/M04/WA-M04-characteristic-map-v4-20260518.md` | The analytical source — 7 characteristics + sub-group mapping + Phase 9 notes |
| 3 | Structural-terms clarification — `Workflow/methodology/WA-structural-terms-clarification-v1-20260518.md` | The corrected hierarchy this schema implements |
| 4 | v2_5 instruction §A1 — `Workflow/Instructions/wa-sessionb-cluster-instruction-v2_5-20260518.md` | Existing cluster-process tables (for compatibility) |

---

## 1. What needs to be captured

From the M04 v4 map, two distinct artefacts must persist in the DB:

### 1.1 The characteristic-grouping

- **7 characteristics** for M04 (Exultation, Joy, Gladness, Delight, Pleasure, Wonder, Suffering-Joy)
- **Each sub-group → characteristic mapping**, with the per-sub-group qualifier text (e.g., "M04-B → Joy, the communal-festive qualifier — Joy enacted in community...")
- **One-sub-group-serves-multiple-characteristics support**: M04-E uniquely contributes to both Joy (eschatological register) and Suffering-Joy (paradox register)

### 1.2 The Phase 9 carry-forward observations

From the map's "Notes for Phase 9" and inline notes:

- M04-B and M04-C inter-relationship: carry both Joy and Gladness registers; expected significant Phase 9 finding to surface this
- M04-E split: Phase 9 should apply 189 prompts under both Characteristic 2 (Joy) and Characteristic 7 (Suffering-Joy)
- Delight's breadth: inter-relationships between M04-G (affective) and M04-H (volitional) expected analytically significant
- M04-L under Gladness: Phase 9 findings for M04-L should integrate with M04-O's findings under Characteristic 3

These observations need to be:

- Queryable (researcher / AI / CC can pull them at Phase 9 time)
- Categorisable (inter-relationship, split-handling, integration-note, follow-up)
- Lifecycle-aware (status: open / confirmed / refined / closed)
- Traceable to the phase that raised them

---

## 2. Schema additions — three new tables

All three tables are **additive** — no changes to existing tables. Migration is simple INSERT-only on schema_version + new table creation.

### 2.1 `characteristic`

One row per distinct inner-being characteristic within a cluster.

```sql
CREATE TABLE characteristic (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    cluster_code TEXT NOT NULL,                  -- FK to cluster.cluster_code
    char_seq INTEGER NOT NULL,                   -- 1..N within cluster (e.g., 1=Exultation, 2=Joy)
    short_name TEXT NOT NULL,                    -- e.g., 'Exultation', 'Joy', 'Suffering-Joy'
    definition TEXT NOT NULL,                    -- the full definition paragraph from the map
    source TEXT,                                 -- e.g., 'M04-characteristic-map-v4-20260518'
    version TEXT DEFAULT 'v1',
    notes TEXT,
    delete_flagged INTEGER DEFAULT 0,
    created_at TEXT NOT NULL,
    last_updated_date TEXT NOT NULL,
    UNIQUE(cluster_code, char_seq),
    UNIQUE(cluster_code, short_name)
);

CREATE INDEX idx_characteristic_cluster ON characteristic(cluster_code);
```

### 2.2 `characteristic_subgroup`

M:N link between `characteristic` and `cluster_subgroup`. Supports one-sub-group-multiple-characteristics (M04-E case).

```sql
CREATE TABLE characteristic_subgroup (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    characteristic_id INTEGER NOT NULL,          -- FK to characteristic.id
    cluster_subgroup_id INTEGER NOT NULL,        -- FK to cluster_subgroup.id
    qualifier_note TEXT,                          -- e.g. 'The communal-festive qualifier — Joy enacted in community...'
    is_partial INTEGER DEFAULT 0,                -- 1 if sub-group serves multiple characteristics (e.g. M04-E)
    partial_register_note TEXT,                  -- e.g. 'Eschatological register' for M04-E under Joy
    delete_flagged INTEGER DEFAULT 0,
    created_at TEXT NOT NULL,
    last_updated_date TEXT NOT NULL,
    UNIQUE(characteristic_id, cluster_subgroup_id),
    FOREIGN KEY (characteristic_id) REFERENCES characteristic(id),
    FOREIGN KEY (cluster_subgroup_id) REFERENCES cluster_subgroup(id)
);

CREATE INDEX idx_charsg_char ON characteristic_subgroup(characteristic_id);
CREATE INDEX idx_charsg_sg ON characteristic_subgroup(cluster_subgroup_id);
```

### 2.3 `cluster_observation`

Captures observations carried forward across phases — analytical hints, expected findings, integration notes, follow-up flags.

```sql
CREATE TABLE cluster_observation (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    cluster_code TEXT NOT NULL,                  -- FK to cluster.cluster_code
    characteristic_id INTEGER,                    -- optional FK to characteristic.id (if observation pertains to a specific characteristic)
    cluster_subgroup_id INTEGER,                  -- optional FK to cluster_subgroup.id (if pertains to specific sub-group)
    source_phase TEXT NOT NULL,                  -- e.g. 'characteristic_mapping', 'phase_5_subgroup_design', 'phase_7_vcg_design'
    observation_type TEXT NOT NULL,              -- 'INTER_RELATIONSHIP', 'SPLIT_SUBGROUP', 'INTEGRATION_NOTE', 'EXPECTED_FINDING', 'FOLLOW_UP'
    target_phase TEXT,                            -- e.g. 'phase_9_findings', 'phase_10_reconciliation', 'session_c_publication'
    title TEXT NOT NULL,                          -- short title for the observation
    description TEXT NOT NULL,                    -- full observation text
    status TEXT DEFAULT 'open',                  -- 'open' | 'confirmed' | 'refined' | 'closed' | 'superseded'
    resolution_note TEXT,                         -- filled at target phase
    raised_date TEXT NOT NULL,
    resolved_date TEXT,
    source_file TEXT,                             -- e.g. 'WA-M04-characteristic-map-v4-20260518.md'
    delete_flagged INTEGER DEFAULT 0,
    created_at TEXT NOT NULL,
    last_updated_date TEXT NOT NULL,
    FOREIGN KEY (characteristic_id) REFERENCES characteristic(id),
    FOREIGN KEY (cluster_subgroup_id) REFERENCES cluster_subgroup(id)
);

CREATE INDEX idx_obs_cluster ON cluster_observation(cluster_code);
CREATE INDEX idx_obs_target ON cluster_observation(target_phase) WHERE status = 'open';
CREATE INDEX idx_obs_char ON cluster_observation(characteristic_id);
```

---

## 3. Data load for M04 v4 map

### 3.1 `characteristic` rows (7)

| char_seq | short_name | source |
|---:|---|---|
| 1 | Exultation | M04-characteristic-map-v4-20260518 |
| 2 | Joy | M04-characteristic-map-v4-20260518 |
| 3 | Gladness | M04-characteristic-map-v4-20260518 |
| 4 | Delight | M04-characteristic-map-v4-20260518 |
| 5 | Pleasure | M04-characteristic-map-v4-20260518 |
| 6 | Wonder | M04-characteristic-map-v4-20260518 |
| 7 | Suffering-Joy | M04-characteristic-map-v4-20260518 |

Each row carries the full definition paragraph from the v4 map's body.

### 3.2 `characteristic_subgroup` rows (17 links — 16 sub-groups + 1 partial)

| Char | Sub-group | is_partial | partial_register_note |
|---|---|---:|---|
| 1 Exultation | M04-A | 0 | — |
| 2 Joy | M04-B | 0 | — |
| 2 Joy | M04-C | 0 | — |
| 2 Joy | M04-D | 0 | — |
| 2 Joy | M04-E | 1 | Eschatological register (sa.s.von) |
| 3 Gladness | M04-L | 0 | — |
| 3 Gladness | M04-O | 0 | — |
| 4 Delight | M04-G | 0 | — |
| 4 Delight | M04-H | 0 | — |
| 4 Delight | M04-M | 0 | — |
| 4 Delight | M04-N | 0 | — |
| 4 Delight | M04-P | 0 | — |
| 5 Pleasure | M04-J | 0 | — |
| 5 Pleasure | M04-K | 0 | — |
| 6 Wonder | M04-I | 0 | — |
| 7 Suffering-Joy | M04-E | 1 | Suffering-paradox register (agalliao) |
| 7 Suffering-Joy | M04-F | 0 | — |

Each link carries its qualifier_note from the v4 map (e.g., "The communal-festive qualifier — Joy enacted in community...").

### 3.3 `cluster_observation` rows (4)

| obs_type | title | target_phase | summary |
|---|---|---|---|
| INTER_RELATIONSHIP | Joy/Gladness inter-relationship in M04-B and M04-C | phase_9_findings | M04-B and M04-C carry both Joy (active rejoicing) and Gladness (settled warm) registers within their corpora. VCG analysis is expected to surface this; the inter-relationship is anticipated as a significant Phase 9 finding. |
| SPLIT_SUBGROUP | M04-E serves two characteristics — Joy + Suffering-Joy | phase_9_findings | Phase 9 should apply the 189 prompts to M04-E under Characteristic 2 (Joy, eschatological register) and Characteristic 7 (Suffering-Joy, paradox register) separately. VCG structure within M04-E will show which VCGs serve which characteristic. |
| INTER_RELATIONSHIP | Delight's breadth — affective/volitional/obedience/relational/corrupt inter-relationships | phase_9_findings | Characteristic 4 (Delight) spans 5 sub-groups (M04-G, H, M, N, P; 247 verses). Inter-relationships between sub-groups — especially M04-G (affective delight in God) and M04-H (volitional delight as directed will) — expected analytically significant. |
| INTEGRATION_NOTE | M04-L evaluative-cognitive face of Gladness | phase_9_findings | Phase 9 findings for M04-L (evaluative goodness as moral-cognitive faculty) should be integrated with M04-O's findings under Characteristic 3 (Gladness) — these together form Gladness's cognitive + experiential faces. |

---

## 4. How this affects Phase 9

Under the new model (researcher direction 2026-05-18 + the v2 proposal):

- The 189-question Tier prompts apply **per characteristic**, not per sub-group
- For each characteristic, AI reads the cluster's evidence **across its constituent sub-groups** (the characteristic_subgroup links tell us which)
- Cell count for M04 Phase 9 = 189 prompts × 7 characteristics + 189 × CLUSTER = ~1,512 cells (worst case)
- BUT: with the layered v2 approach (VCG-level synthesis at Layer 1; per-prompt aggregation at Layer 2), most prompts produce ONE cluster row + selective characteristic-level rows where the characteristic differentiates
- Realistic cell count: ~189 cluster + ~50-150 per-characteristic selective + ~50 per-sub-group T1.2.1 structural = ~300-400 rows

At Phase 9 start, the observations in `cluster_observation` are surfaced to AI as **analytical hints** — "the researcher expects these inter-relationships to emerge; flag if they don't; flag if other patterns emerge."

At post-findings evaluation (researcher review), each observation's `status` is updated to `confirmed` / `refined` / `superseded` with a `resolution_note`.

---

## 5. v2_6 instruction implications

Codifying this would add to v2_5 (becoming v2_6):

- New §A1 entries for the three new tables
- §8 Phase 5 (Sub-group formation): add output requirement to surface characteristic-mapping as part of the design (or as a separate Phase 5.5 — TBD)
- §12 Phase 9 (Catalogue prompts): reframe scope as per characteristic (across constituent sub-groups), not per sub-group
- §15.2 Phase 12 closure: add precondition that all cluster_observations with target_phase ≤ Phase 12 have status != 'open'
- New §N "Cluster observations" canonical reference

Recommend **drafting v2_6 after M04's Phase 9 validates the model**, not before.

---

## 6. Decisions needed from researcher

| # | Question | Options | Your decision |
|---|---|---|---|
| 1 | Approve the three-table schema design (§2)? | YES / NO / ADJUST: ... | _[YES / NO / ADJUST: ...]_ |
| 2 | Approve the M04 v4 data load per §3? | YES / MODIFY: ... | _[YES / MODIFY: ...]_ |
| 3 | Apply schema migration + data load now, or stage the schema first and load M04 after researcher reviews tables? | NOW (one shot) / STAGED (schema first, then load on confirm) | _[NOW / STAGED]_ |
| 4 | Defer v2_6 instruction draft until M04 Phase 9 validates the model? | YES (defer) / DRAFT NOW | _[YES / DRAFT NOW]_ |
| 5 | Should the proposal allow characteristics to span clusters (cross-cluster characteristic), or strictly cluster-local? | CLUSTER-LOCAL ONLY / ALLOW CROSS-CLUSTER (future) | _[CLUSTER-LOCAL / CROSS-CLUSTER]_ |
| 6 | observation_type vocabulary — accept the 5 proposed values (INTER_RELATIONSHIP / SPLIT_SUBGROUP / INTEGRATION_NOTE / EXPECTED_FINDING / FOLLOW_UP), or adjust? | ACCEPT / ADJUST: ... | _[ACCEPT / ADJUST: ...]_ |

---

## 7. Implementation sequence (after approvals)

1. **Schema migration**: CC writes a migration script under the engine's migration framework. Adds the three tables; bumps schema_version. ~5 min.
2. **M04 data load**: CC writes a load script that:
   - INSERTs the 7 characteristic rows for M04 (definitions lifted verbatim from v4 map)
   - INSERTs the 17 characteristic_subgroup links (with qualifier_notes)
   - INSERTs the 4 cluster_observation rows (with full descriptions)
3. **Verification**: CC runs queries showing every sub-group has at least one characteristic; M04-E has two; all observations are status='open' with target_phase='phase_9_findings'.
4. **Apply report** written to `Sessions/Session_Clusters/M04/WA-M04-characteristic-load-applied-v1-20260518.md`.
5. **Commit + push.**

---

*End of proposal. Mark §6 and ping me.*
