# V3_2 schema migration plan

> **Plan · v1 · 2026-06-07 · CC.** The schema changes the V3_2 base design requires (rollup design §10).
> **✅ APPLIED 2026-06-08 as migration M55** (backup `backups/bible_research_pre_v3_2_20260608.db`;
> dry-run verified; via the history-aware runner). DB now at **`version_code = 3.29.0`**; M39 (no-op) + M55
> recorded; registry == history (no pending). 12 columns added, `vertical_pass_flag` dropped; integrity ok.
> CONSULT defaults taken: `sense_id` INTEGER; `vertical_pass_flag` dropped (0 rows); `is_homonym` added
> (population later). **Population passes (`stem_label`, `morph`/`stem`, `is_homonym`) still pending — run
> within L1 of the first cluster.** Original plan below.

---

## 0. Application caveat (read first)

`engine/migrate.py` registers migrations **M01–M39**, but the DB `migration_history` records up to **M54**
— so **M40–M54 were applied outside the registry** (one-off scripts, as M16–M18 were). **The registry and
the history are out of sync.** Before adding a new migration to `migrate.py` and running `--migrate`, we must
confirm the application path (the runner applies *registered* migrations not yet in history — with the gap,
its behaviour needs checking). **Options:** (a) author the migration as a one-off script (matching how
M40–M54 were applied) — lowest-risk given the drift; or (b) reconcile the registry first. **〔CONSULT〕**
which path. The SQL below is identical either way.

**Pre-apply checklist:** DB backup (`scripts/backup_db_to_nas.py` / off-Drive copy) · `--dry-run` first ·
verify counts after · all ADD COLUMN are idempotent (`_add_column_if_missing`).

---

## 1. New columns

All nullable / defaulted, so **additive and safe** (no data rewrite). Types follow the engine's conventions.

### `verse_context` — the L1 verse-establishment fields (7 new)
| Column | Type | Purpose |
|---|---|---|
| `step_meaning_applied` | TEXT | the terse STEP-applied meaning (L1) — STEP-specific, **separate from `analysis_note`** |
| `sense_id` | INTEGER | the selected STEP sub-sense — FK → `wa_meaning_sense(id)` **〔CONSULT〕** FK vs a `sense_code` TEXT (level_code) |
| `sense_multiplicity` | TEXT | `single` \| `multi` |
| `step_envelope_note` | TEXT | the full STEP sense-set, kept for further analysis |
| `pole` | TEXT | `inner` \| `external` \| `physical` |
| `pole_is_metaphor` | INTEGER DEFAULT 0 | flag heat/tremble/melt metaphor for L2 judgement (R6) |
| `residue_flag` | INTEGER DEFAULT 0 | needs-advanced (within-stem multi / metaphor / novel) → L2 |

*(`keywords` already exists — re-purposed as STEP-capture, no schema change. UT = no field. `is_relevant`,
`set_aside_reason`, `is_related`, `analysis_note` retained.)*

### `cluster_finding` — finding typing (2 new)
| Column | Type | Purpose |
|---|---|---|
| `finding_type` | TEXT | `tier` \| `cross_vcg` \| `cross_subgroup` \| `intra_cluster` \| `cross_cluster` |
| `needs_research` | INTEGER DEFAULT 0 | open-question findings (E7) |

*(Scope anchors `cluster_code` + `cluster_subgroup_id` + `vcg_scope` already exist. `finding_status` exists
— confirm it carries the `draft`/`reviewed`/`confirmed` lifecycle values.)*

### `wa_verse_records` — morphology (2 new)
| Column | Type | Purpose |
|---|---|---|
| `morph_code` | TEXT | per-occurrence STEP morphology (e.g. `HVqw3ms`) |
| `stem` | TEXT | the parsed binyan (Qal / Niphal / …) — derived from `morph_code` |

### `wa_meaning_sense` — homonym filter (1 new)
| Column | Type | Purpose |
|---|---|---|
| `is_homonym` | INTEGER DEFAULT 0 | mark a non-biblical homonym sense to exclude from the sense-set (e.g. `ya.re` "shoot/pour", `che.mah` "bottle") |

*(`is_stem_label` + `stem_label` already exist — to be **populated**, see §3.)*

---

## 2. Retirements (the only structural removals)

`vertical_pass_flag` is **confirmed unused** (0 of 43,722 `verse_context` rows; 0 of 4,155
`verse_context_group` rows). SQLite 3.50.4 supports `DROP COLUMN`.

- `ALTER TABLE verse_context DROP COLUMN vertical_pass_flag;`
- `ALTER TABLE verse_context_group DROP COLUMN vertical_pass_flag;`

*(Drop any dependent index first — none found referencing it. If preferred, soft-retire instead: leave the
column, mark deprecated, stop reading/writing it. **〔CONSULT〕** drop vs soft-retire.)*

---

## 3. Data population (separate processes — NOT this migration)

The migration only adds columns. Populating them is process work, run later:

- **`wa_meaning_sense.stem_label` / `is_stem_label`** — parse the BDB stem branches (`(Qal)`, `(Niphal)`…)
  from `sense_text` into the structured columns. A one-off parse pass (the R7 prototype already extracts
  these). ~16,005 rows.
- **`wa_verse_records.morph_code` / `stem`** — pull per-occurrence morphology from STEP and parse the stem.
  **Large operation** (per term, paginated STEP calls) — runs as part of L1, cluster by cluster, not in one
  shot. The prototype `_prototype_l1_morph.py` is the basis.
- **`wa_meaning_sense.is_homonym`** — curation/parse pass to flag non-biblical homonym senses (TWOT markers,
  divergent roots). **〔CONSULT〕** the detection rule (TWOT-marker auto-flag vs curated list).

---

## 4. The migration (ready to register / script)

```python
@_register("M55", "V3_2: L1 verse fields, finding typing, morphology, homonym flag; retire vertical_pass_flag")
def _m55(conn):
    # verse_context — L1 establishment fields
    _add_column_if_missing(conn, "verse_context", "step_meaning_applied", "TEXT")
    _add_column_if_missing(conn, "verse_context", "sense_id",             "INTEGER")
    _add_column_if_missing(conn, "verse_context", "sense_multiplicity",   "TEXT")
    _add_column_if_missing(conn, "verse_context", "step_envelope_note",   "TEXT")
    _add_column_if_missing(conn, "verse_context", "pole",                 "TEXT")
    _add_column_if_missing(conn, "verse_context", "pole_is_metaphor",     "INTEGER DEFAULT 0")
    _add_column_if_missing(conn, "verse_context", "residue_flag",         "INTEGER DEFAULT 0")
    # cluster_finding — typing
    _add_column_if_missing(conn, "cluster_finding", "finding_type",   "TEXT")
    _add_column_if_missing(conn, "cluster_finding", "needs_research", "INTEGER DEFAULT 0")
    # wa_verse_records — morphology
    _add_column_if_missing(conn, "wa_verse_records", "morph_code", "TEXT")
    _add_column_if_missing(conn, "wa_verse_records", "stem",       "TEXT")
    # wa_meaning_sense — homonym filter
    _add_column_if_missing(conn, "wa_meaning_sense", "is_homonym", "INTEGER DEFAULT 0")
    # retire vertical_pass_flag (confirmed 0 rows)
    for tbl in ("verse_context", "verse_context_group"):
        cols = {r[1] for r in conn.execute(f"PRAGMA table_info({tbl})")}
        if "vertical_pass_flag" in cols:
            conn.execute(f"ALTER TABLE {tbl} DROP COLUMN vertical_pass_flag")
    conn.execute("UPDATE schema_version SET version_code = ?, applied_at = ? "
                 "WHERE id = (SELECT MAX(id) FROM schema_version)", ("3.29.0", _now()))
```

Schema bump: **3.28.0 → 3.29.0**. Update `engine/constants.py` `EXPECTED_SCHEMA_VERSION` to match
(after applying).

---

## 5. Summary

**12 new columns** (7 verse_context · 2 cluster_finding · 2 wa_verse_records · 1 wa_meaning_sense) +
**2 column drops** (vertical_pass_flag ×2). Additive and low-risk; the only removals are a confirmed-dead
flag. Three data-population passes follow separately (stem_label, morphology, homonym). **〔CONSULT〕** items:
application path (registry drift), `sense_id` FK vs code, drop vs soft-retire, homonym detection rule.

**Recommendation:** apply as a one-off script (matching M40–M54), after a backup and a dry-run, on the
researcher's go. The morphology + stem_label + homonym population then runs as part of the first V3_2 cluster
(M01 re-run).
