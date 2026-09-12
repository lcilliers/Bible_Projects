# Escalation #1690 — `cluster_subgroup`/`mti_term_subgroup` (replacing family) — columns + governing rules

**Status:** design proposal, decision_required. The fresh tables are built with the SAME shape as
the ones being renamed to `zz_legacy_*` (no reason to invent a competing shape when reverting to
the concept). Restructured this round to match #1691/#1692's LLM-session/table-update-procedure
split, per the researcher's instruction — process (b) (family/subgroup assignment) is itself an
LLM session with no DB access, same as process (c)/(d)/(e).

## 1. Columns — final list as decided so far

```sql
CREATE TABLE cluster_subgroup (
    id                  INTEGER PRIMARY KEY AUTOINCREMENT,  -- assigned by TABLE UPDATE PROCEDURE
    cluster_code        TEXT NOT NULL REFERENCES cluster(cluster_code),
    subgroup_code       TEXT NOT NULL,   -- the family's own code, e.g. "H_guilt", "FLAG"
    label               TEXT NOT NULL,   -- REQUIRED -- see §2 item 1, a real gap in process (b)
    core_description    TEXT,
    sort_order          INTEGER DEFAULT 0,
    status              TEXT,
    version             TEXT,
    source              TEXT,
    notes               TEXT,
    delete_flagged      INTEGER DEFAULT 0,
    created_at          TEXT,
    last_updated_date   TEXT,
    UNIQUE (cluster_code, subgroup_code)
)

CREATE TABLE mti_term_subgroup (
    id                  INTEGER PRIMARY KEY AUTOINCREMENT,  -- assigned by TABLE UPDATE PROCEDURE
    mti_term_id         INTEGER NOT NULL REFERENCES mti_terms(id),
    cluster_subgroup_id INTEGER NOT NULL REFERENCES cluster_subgroup(id),
    placement_note      TEXT,
    delete_flagged      INTEGER NOT NULL DEFAULT 0,
    created_at          TEXT NOT NULL,
    last_updated_date   TEXT NOT NULL,
    UNIQUE (mti_term_id)   -- TIGHTENED from the legacy (mti_term_id, cluster_subgroup_id) --
                              enforces "one strong, one family" structurally, see §4 item 2
)
```

| Column | Usage |
|---|---|
| `cluster_code` | required, singular — a family is structurally one-cluster-only by construction |
| `subgroup_code` | the family's stable code, unique per `(cluster_code, subgroup_code)` |
| `label` | short human title — **not currently produced, see §2 item 1** |
| `core_description` | one sentence on the family's shared commonality |
| `sort_order`/`status`/`version`/`source`/`notes` | reused as-is, same as the legacy table (descriptive `source` values, not invented short codes) |
| `mti_term_id` | the strong, resolved to `mti_terms.id` — real FK, an upgrade over free-text strong codes |
| `placement_note` | free text — the home for a FLAG signpost's rationale (§3 item 3) |

## 2. The LLM session (process b) — what it must produce

1. **A real `label` per family — not currently produced.** Process (b)'s JSON today leaves
   `family_label` always empty; `cluster_subgroup.label` is `NOT NULL`. This is a change the
   generation script needs, not a naming pick: every family needs an actual short title (e.g. for
   `H_guilt`: "Guilt — forensic liability and self-recognized wrongdoing").
2. Every strong placed in exactly one family (already process (b)'s own rule, now given a
   structural backstop by `mti_term_subgroup`'s tightened `UNIQUE(mti_term_id)`, §4 item 2).
3. A strong that doesn't fit any real family is signposted to `"FLAG"` (§3 item 3) — the LLM writes
   this the same way it writes any other family placement, just under that special code.

## 3. The table-update procedure — what it must do

1. Assigns `cluster_subgroup.id` and `mti_term_subgroup.id` — the LLM never sees these.
2. Resolves each strong to its `mti_terms.id` (not a bare text code).
3. **Writes `subgroup_code = "FLAG"` as a family belonging to the SAME cluster being read** (e.g.
   M10's own FLAG bucket) — never a placement under the separate `cluster_code='FLAG'` cluster,
   which would itself already be a reallocation, the opposite of a signpost. **Stated plainly since
   it's a reading, not confirmed by the researcher yet — flag if wrong.**
4. Enforces `UNIQUE(mti_term_id)` on `mti_term_subgroup` — a term already placed elsewhere gets
   rejected or requires an explicit re-placement decision, not a silent second row.

## 4. Confirmed this round / already resolved

1. `label`'s `NOT NULL` gap — identified, needs a process-(b) generation-script fix, not a schema
   change.
2. `mti_term_subgroup`'s uniqueness constraint tightened to `UNIQUE(mti_term_id)` — answers the
   original "should one-strong-one-family be structural" question: yes.
3. A family is structurally single-cluster by construction (`cluster_code` required, singular).

## 5. Still not settled

1. **FLAG signposting mechanism (§3 item 3)** — my reading, not yet confirmed by the researcher.
2. Family re-grouping/versioning if M10's families are ever re-derived — `version`/`status` exist
   as a starting point, not designed further than that.
3. Table name — `cluster_subgroup`/`mti_term_subgroup` themselves are confirmed (reverting to the
   existing names once the legacy data is renamed away), no open naming question here unlike
   `ib_observation`/`ib_node`.

## 6. What "finalized" would mean

Once §5 item 1 is confirmed: the rename of the 8 legacy tables (per #1683) executes first, then
fresh `characteristic`/`characteristic_subgroup`/`cluster_subgroup`/`mti_term_subgroup` tables are
created per the DDL in §1, registered in `cfg_table`/`cfg_column`. The table-update-procedure
responsibilities in §3 become part of #1693's full spec, same as #1691/#1692.
