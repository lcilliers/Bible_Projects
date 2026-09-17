"""Create the cluster-reading pipeline tables — the "sign-off pack" (#1690/#1691/#1692/#1693/#1697,
all `completed`/design-complete) — in `iba.db`. Escalation #1706 Phase D/E, build session
2026-09-16. **Confirmed live before this migration: none of these 5 tables/columns existed.**

Creates, in dependency order:
1. `cluster.status` column (#1697) — 8-value lifecycle enum, ordinals 1-2 historical/one-off
   (already-completed T/M-code classification work), 3-8 the real active lifecycle.
2. `cluster_subgroup` (#1690 §1, + `anchor_verse_reference` added post-approval 2026-09-16, #1526
   — see `1690-cluster-subgroup-family-columns-v1-20260912.md` §2A).
3. `cluster_subgroup_strong` (#1690 §1).
4. `ib_observation` (#1691 §1).
5. `ib_node` (#1692 §1).

Backfill: all 95 live `cluster` rows start at ordinal 2 (`t_cluster_assignment_completed`) — every
one already has `cluster_strong` members, confirmed by the researcher's own decision (#1706 §4
item 2/5): "all 95 live cluster rows start at ordinal 2... every one already has cluster_strong
members, so every one is past ordinal 1 already."

Every table/column is also registered in `cfg_table`/`cfg_column`; the 3 new enums
(`cluster.status`, `cluster_subgroup.status`, `ib_observation.stage`/`ib_observation.window`) are
registered in `cfg_enum`.

Safe to re-run: every step is guarded, no-ops if already applied.

Usage:
    python iba/app/migration/create_cluster_reading_pipeline_tables_v1_20260916.py [--db PATH] [--dry-run]
"""
import argparse
import sqlite3
import sys

DEFAULT_DB = r"C:\Bible_study_projects\iba\app\db\iba.db"

_CLUSTER_STATUS_ENUM = [
    (1, "strong_assignment_in_progress"),
    (2, "t_cluster_assignment_completed"),
    (3, "ready_for_subgroup_allocation"),
    (4, "ready_for_reading"),
    (5, "ready_for_observations"),
    (6, "ready_for_synthesis"),
    (7, "completed"),
    (8, "strongs_reassigned"),
]

_SUBGROUP_STATUS_ENUM = [
    (1, "allocated"),
    (2, "ready_for_reading"),
    (3, "ready_for_answer"),
    (4, "answer_complete"),
    (5, "completed"),
    (6, "re_read_needed"),
]

# ib_observation.stage — 'subgroup' added 2026-09-14 (#1691 §9 item 8) for process (b)'s own
# cluster-level observations; 'meaning' renamed to 'verse_meaning' 2026-09-16 (#1526/#1711) for the
# new pre-subgroup Layer 2 stage.
_STAGE_ENUM = [
    (1, "verse_meaning"),   # process (a-adjacent) — Layer 2, #1711, runs BEFORE subgroup
    (2, "subgroup"),        # process (b)
    (3, "reading"),         # process (c)
    (4, "answer"),          # process (d)
    (5, "synthesis"),       # process (e)
]

_WINDOW_ENUM = [
    (1, "lexical analysis"),
    (2, "verse-context reading"),
    (3, "answer stage"),
    (4, "multi-cluster synergising"),
]


def column_exists(cur, table: str, col: str) -> bool:
    return any(r[1] == col for r in cur.execute(f"PRAGMA table_info({table})"))


def table_exists(cur, table: str) -> bool:
    return cur.execute(
        "SELECT 1 FROM sqlite_master WHERE type='table' AND name=?", (table,)).fetchone() is not None


def register_table(cur, name: str, grain: str, use: str) -> None:
    if not cur.execute("SELECT 1 FROM cfg_table WHERE name=?", (name,)).fetchone():
        cur.execute("INSERT INTO cfg_table (database, name, grain, use, inactive, category) "
                   "VALUES ('iba', ?, ?, ?, 0, 'data')", (name, grain, use))


def register_column(cur, table: str, name: str, ordinal: int, ctype: str, is_pk: int,
                    notnull: int, is_unique: int, fk: str | None, use: str) -> None:
    if not cur.execute("SELECT 1 FROM cfg_column WHERE database='iba' AND table_name=? AND "
                       "name=?", (table, name)).fetchone():
        cur.execute(
            'INSERT INTO cfg_column (database, table_name, name, ordinal, type, is_pk, "notnull", '
            "is_unique, dflt, fk, use, expectation, source, filled_by, inactive) "
            "VALUES ('iba',?,?,?,?,?,?,?,NULL,?,?,NULL,NULL,NULL,0)",
            (table, name, ordinal, ctype, is_pk, notnull, is_unique, fk, use))


def register_enum(cur, name: str, values: list[tuple[int, str]], use: str) -> None:
    # cfg_enum has no `use` column (checked live, 2026-09-16: name/value/ordinal/inactive only) --
    # `use` is accepted here for the caller's own documentation value in this migration's source,
    # not persisted; the enum's rationale lives in the owning column's cfg_column.use instead.
    for ordinal, value in values:
        if not cur.execute("SELECT 1 FROM cfg_enum WHERE name=? AND value=?",
                          (name, value)).fetchone():
            cur.execute(
                "INSERT INTO cfg_enum (name, value, ordinal, inactive) VALUES (?,?,?,0)",
                (name, value, ordinal))


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default=DEFAULT_DB)
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    conn = sqlite3.connect(args.db)
    cur = conn.cursor()
    report: list[str] = []
    try:
        cur.execute("BEGIN")

        # ── 1. cluster.status ────────────────────────────────────────────────────────────────
        if not column_exists(cur, "cluster", "status"):
            cur.execute("ALTER TABLE cluster ADD COLUMN status TEXT")
            cur.execute("ALTER TABLE cluster ADD COLUMN status_changed_at TEXT")
            cur.execute("UPDATE cluster SET status='t_cluster_assignment_completed', "
                       "status_changed_at=strftime('%Y-%m-%dT%H:%M:%SZ','now') WHERE deleted=0")
            n = cur.execute("SELECT COUNT(*) FROM cluster WHERE deleted=0 AND "
                           "status='t_cluster_assignment_completed'").fetchone()[0]
            report.append(f"ADDED cluster.status/status_changed_at; backfilled {n} live cluster "
                          f"row(s) to ordinal 2 (t_cluster_assignment_completed)")
        else:
            report.append("cluster.status already present — skipped")
        register_column(cur, "cluster", "status", 5, "TEXT", 0, 0, 0, None,
                        "Cluster-level lifecycle, cfg_enum-governed (#1697). Ordinals 1-2 "
                        "historical/one-off (the T/M-code cluster_strong classification work, "
                        "already complete for all 95 live clusters) — no gating code needed for "
                        "these. Ordinals 3-8 are the real active lifecycle, rolled up from "
                        "cluster_subgroup.status (#1690 SS3a): can only progress past "
                        "ready_for_reading/ready_for_observations/ready_for_synthesis once EVERY "
                        "subgroup in the cluster (excluding FLAG) has itself reached the matching "
                        "level. strongs_reassigned raises a real escalation (decision_required) at "
                        "the moment it fires -- no automatic resubmission of process (b).")
        register_column(cur, "cluster", "status_changed_at", 6, "TEXT", 0, 0, 0, None,
                        "Timestamp of the last cluster.status transition.")
        register_enum(cur, "cluster.status", _CLUSTER_STATUS_ENUM,
                     "iba.cluster's own lifecycle (#1697) -- see cfg_column.use on cluster.status "
                     "for the full gating rule.")
        report.append("cfg_enum cluster.status registered (8 values)")

        # ── 2. cluster_subgroup ──────────────────────────────────────────────────────────────
        if not table_exists(cur, "cluster_subgroup"):
            cur.execute("""
                CREATE TABLE cluster_subgroup (
                    id                      INTEGER PRIMARY KEY AUTOINCREMENT,
                    cluster_code            TEXT NOT NULL REFERENCES cluster(cluster_code),
                    subgroup_code           TEXT NOT NULL,
                    label                   TEXT NOT NULL,
                    core_description        TEXT,
                    anchor_verse_reference  TEXT,
                    sort_order              INTEGER DEFAULT 0,
                    status                  TEXT,
                    version                 TEXT,
                    source                  TEXT,
                    notes                   TEXT,
                    delete_flagged          INTEGER DEFAULT 0,
                    created_at              TEXT,
                    last_updated_date       TEXT,
                    UNIQUE (cluster_code, subgroup_code)
                )
            """)
            report.append("CREATED cluster_subgroup")
        else:
            report.append("cluster_subgroup already exists — skipped")
        register_table(cur, "cluster_subgroup", "one row per subgroup (\"family\") within a "
                      "cluster, produced by process (b)",
                      "The cluster-reading pack's own subgroup table (#1690, design-complete "
                      "2026-09-13; anchor_verse_reference added post-approval 2026-09-16, #1526). "
                      "iba.db, replaces the legacy bible_research.db cluster_subgroup/"
                      "mti_term_subgroup tables, which stay untouched (DB fork, #737/#1682, "
                      "2026-09-13) -- no step in this pipeline reads or writes bible_research.db.")
        for ordinal, name, ctype, is_pk, notnull, is_unique, fk, use in (
            (0, "id", "INTEGER", 1, 1, 0, None, "surrogate PK, assigned by the recording pass (#1693)"),
            (1, "cluster_code", "TEXT", 0, 1, 0, "cluster(cluster_code)",
             "required, singular -- a family is structurally one-cluster-only by construction"),
            (2, "subgroup_code", "TEXT", 0, 1, 0, None,
             "the family's stable code, unique per (cluster_code, subgroup_code) -- expected to "
             "repeat as 'FLAG' across clusters, never otherwise"),
            (3, "label", "TEXT", 0, 1, 0, None, "short human title"),
            (4, "core_description", "TEXT", 0, 0, 0, None,
             "one sentence on the family's shared commonality"),
            (5, "anchor_verse_reference", "TEXT", 0, 0, 0, None,
             "ADDED 2026-09-16 (#1526). One representative verse per subgroup, selected by "
             "process (b)'s own LLM session as the verse that best describes the subgroup's "
             "shared characteristic (researcher, verbatim). Resolved fresh against "
             "iba.db.verse.reference, same convention as ib_node.verse_reference; written in the "
             "SAME DB update as the rest of the subgroup row (#1693's recording pass), never a "
             "separate pass or left null-then-backfilled."),
            (6, "sort_order", "INTEGER", 0, 0, 0, None, "display order"),
            (7, "status", "TEXT", 0, 0, 0, None,
             "subgroup-level lifecycle, cfg_enum-governed (cluster_subgroup.status, #1690 SS3a). "
             "Distinct from cluster.status (#1697) -- coarser grain, separate enum. NULL for the "
             "FLAG subgroup (never enters this lifecycle)."),
            (8, "version", "TEXT", 0, 0, 0, None, "reused as-is from the legacy table convention"),
            (9, "source", "TEXT", 0, 0, 0, None, "descriptive provenance text, not an invented code"),
            (10, "notes", "TEXT", 0, 0, 0, None, "free text"),
            (11, "delete_flagged", "INTEGER", 0, 0, 0, None, "soft-delete"),
            (12, "created_at", "TEXT", 0, 0, 0, None, "ISO-8601 UTC"),
            (13, "last_updated_date", "TEXT", 0, 0, 0, None, "ISO-8601 UTC"),
        ):
            register_column(cur, "cluster_subgroup", name, ordinal, ctype, is_pk, notnull,
                           is_unique, fk, use)
        register_enum(cur, "cluster_subgroup.status", _SUBGROUP_STATUS_ENUM,
                     "cluster_subgroup's own lifecycle (#1690 SS3a), one grain finer than "
                     "cluster.status -- a subgroup is read and answered independently of its "
                     "siblings. cluster.status is a rollup over this table, not a redundant check.")
        report.append("cfg_enum cluster_subgroup.status registered (6 values)")

        # ── 3. cluster_subgroup_strong ───────────────────────────────────────────────────────
        if not table_exists(cur, "cluster_subgroup_strong"):
            cur.execute("""
                CREATE TABLE cluster_subgroup_strong (
                    id                  INTEGER PRIMARY KEY AUTOINCREMENT,
                    strong              TEXT NOT NULL REFERENCES strong(strongNumber),
                    cluster_subgroup_id INTEGER NOT NULL REFERENCES cluster_subgroup(id),
                    placement_note      TEXT,
                    delete_flagged      INTEGER NOT NULL DEFAULT 0,
                    created_at          TEXT NOT NULL,
                    last_updated_date   TEXT NOT NULL,
                    UNIQUE (strong)
                )
            """)
            report.append("CREATED cluster_subgroup_strong")
        else:
            report.append("cluster_subgroup_strong already exists — skipped")
        register_table(cur, "cluster_subgroup_strong", "one row per strong-to-subgroup placement "
                      "(membership)",
                      "The cluster-reading pack's own subgroup-membership table (#1690, was "
                      "mti_term_subgroup, renamed 2026-09-13, design-complete). UNIQUE(strong) "
                      "enforces one strong, one family, structurally.")
        for ordinal, name, ctype, is_pk, notnull, is_unique, fk, use in (
            (0, "id", "INTEGER", 1, 1, 0, None, "surrogate PK, assigned by the recording pass (#1693)"),
            (1, "strong", "TEXT", 0, 1, 1, "strong(strongNumber)",
             "the Strong's code, resolved to strong.strongNumber (was mti_term_id/mti_terms.id "
             "pre-DB-fork). UNIQUE -- one strong, one family, structurally enforced"),
            (2, "cluster_subgroup_id", "INTEGER", 0, 1, 0, "cluster_subgroup(id)",
             "which subgroup this strong belongs to"),
            (3, "placement_note", "TEXT", 0, 0, 0, None,
             "free text -- REQUIRED for FLAG placements (the signpost's rationale); optional but "
             "available for any ordinary placement, captures whatever observation the LLM made "
             "while assigning that strong"),
            (4, "delete_flagged", "INTEGER", 0, 1, 0, None, "soft-delete"),
            (5, "created_at", "TEXT", 0, 1, 0, None, "ISO-8601 UTC"),
            (6, "last_updated_date", "TEXT", 0, 1, 0, None, "ISO-8601 UTC"),
        ):
            register_column(cur, "cluster_subgroup_strong", name, ordinal, ctype, is_pk, notnull,
                           is_unique, fk, use)

        # ── 4. ib_observation ────────────────────────────────────────────────────────────────
        if not table_exists(cur, "ib_observation"):
            cur.execute("""
                CREATE TABLE ib_observation (
                    id                          INTEGER PRIMARY KEY AUTOINCREMENT,
                    cluster_code                TEXT NULL REFERENCES cluster(cluster_code),
                    cluster_subgroup_id         INTEGER NULL REFERENCES cluster_subgroup(id),
                    stage                       TEXT NOT NULL,
                    tag                         TEXT NOT NULL,
                    strong                      TEXT NULL,
                    question_code               TEXT NULL,
                    window                      TEXT NULL,
                    obs_text                    TEXT NOT NULL,
                    meaning_source              TEXT NULL,
                    status                      TEXT NULL,
                    supersedes_observation_id   INTEGER NULL REFERENCES ib_observation(id),
                    stable_key                  TEXT NULL,
                    revisit_note                TEXT NULL,
                    source_json_serial          INTEGER NULL,
                    created_at                  TEXT NOT NULL,
                    updated_at                  TEXT NULL
                )
            """)
            report.append("CREATED ib_observation")
        else:
            report.append("ib_observation already exists — skipped")
        register_table(cur, "ib_observation", "one row per LLM-session claim/observation, across "
                      "every stage of the cluster-reading pipeline",
                      "The cluster-reading pack's universal observation store (#1691, "
                      "design-complete 2026-09-14/16). One table for verse_meaning/subgroup/"
                      "reading/answer/synthesis alike, distinguished by `stage`. Grounded via "
                      "ib_node (#1692) -- CHECK constraint there makes 'no way to check a "
                      "finding's grounding' structurally impossible, superseding the old "
                      "verse_lexical_note/evidence_text mechanism (#1597, resolution-by-"
                      "architecture). No edit-history table -- researcher's decision, not overkill "
                      "avoided by design.")
        for ordinal, name, ctype, is_pk, notnull, is_unique, fk, use in (
            (0, "id", "INTEGER", 1, 1, 0, None, "surrogate PK, assigned by the recording pass, never the LLM session"),
            (1, "cluster_code", "TEXT", 0, 0, 0, "cluster(cluster_code)",
             "NULL only for stage=synthesis (cross-cluster; the actual cluster(s) referenced are "
             "recorded via ib_node rows instead, one per cluster) -- required for every other stage"),
            (2, "cluster_subgroup_id", "INTEGER", 0, 0, 0, "cluster_subgroup(id)",
             "NULL for stage=synthesis and process (b)'s own cluster-level observations (both "
             "above single-subgroup scope)"),
            (3, "stage", "TEXT", 0, 1, 0, None,
             "cfg_enum-governed (ib_observation.stage): verse_meaning (pre-subgroup Layer 2, "
             "#1711) | subgroup (process b) | reading (process c) | answer (process d) | "
             "synthesis (process e, cross-cluster)"),
            (4, "tag", "TEXT", 0, 1, 0, None, "stage-specific enum, cfg_enum-governed"),
            (5, "strong", "TEXT", 0, 0, 0, None, "the strong this claim is grounded in"),
            (6, "question_code", "TEXT", 0, 0, 0, None,
             "answer/verse_meaning stages -- not yet an enforced FK; restore once the catalogue "
             "migration (#1696) lands wa_obs_question_catalogue into iba.db"),
            (7, "window", "TEXT", 0, 0, 0, None,
             "pipeline-window enum, all stages: 1=lexical analysis, 2=verse-context reading, "
             "3=answer stage, 4=multi-cluster synergising"),
            (8, "obs_text", "TEXT", 0, 1, 0, None, "self-standing claim text, no join required"),
            (9, "meaning_source", "TEXT", 0, 0, 0, None, "reading stage only"),
            (10, "status", "TEXT", 0, 0, 0, None,
             "provisional|corroborated|superseded -- synthesis stage only"),
            (11, "supersedes_observation_id", "INTEGER", 0, 0, 0, "ib_observation(id)",
             "synthesis stage only, self-referencing, the append-only supersedes chain"),
            (12, "stable_key", "TEXT", 0, 0, 0, None, "the generating JSON file's own name"),
            (13, "revisit_note", "TEXT", 0, 0, 0, None, "synthesis stage only"),
            (14, "source_json_serial", "INTEGER", 0, 0, 0, None,
             "the LLM session's own local numbering within its JSON, distinct from id"),
            (15, "created_at", "TEXT", 0, 1, 0, None, "ISO-8601 UTC"),
            (16, "updated_at", "TEXT", 0, 0, 0, None, "set whenever obs_text is broadened in place"),
        ):
            register_column(cur, "ib_observation", name, ordinal, ctype, is_pk, notnull,
                           is_unique, fk, use)
        register_enum(cur, "ib_observation.stage", _STAGE_ENUM,
                     "Which pipeline stage produced this observation (#1691 SS9 item 8, "
                     "#1706/#1711 -- verse_meaning added 2026-09-16, the new pre-subgroup Layer 2 "
                     "stage).")
        register_enum(cur, "ib_observation.window", _WINDOW_ENUM,
                     "Pipeline-window enum, all ib_observation stages (#1691 SS6).")
        report.append("cfg_enum ib_observation.stage registered (5 values, incl. verse_meaning)")
        report.append("cfg_enum ib_observation.window registered (4 values)")

        # ── 5. ib_node ───────────────────────────────────────────────────────────────────────
        if not table_exists(cur, "ib_node"):
            cur.execute("""
                CREATE TABLE ib_node (
                    id                      INTEGER PRIMARY KEY AUTOINCREMENT,
                    observation_id          INTEGER NOT NULL REFERENCES ib_observation(id),
                    cluster_code            TEXT NOT NULL,
                    cluster_subgroup_code   TEXT NULL,
                    strong                  TEXT NULL,
                    verse_reference         TEXT NULL,
                    surface                 TEXT NULL,
                    morph_code              TEXT NULL,
                    question_code           TEXT NULL,
                    traced_observation_id   INTEGER NULL REFERENCES ib_observation(id),
                    source_stage            TEXT NOT NULL,
                    seq                     INTEGER NOT NULL,
                    created_at              TEXT NOT NULL,
                    UNIQUE (observation_id, seq),
                    CHECK (strong IS NOT NULL OR verse_reference IS NOT NULL OR
                           cluster_subgroup_code IS NOT NULL OR cluster_code IS NOT NULL OR
                           question_code IS NOT NULL OR traced_observation_id IS NOT NULL)
                )
            """)
            report.append("CREATED ib_node")
        else:
            report.append("ib_node already exists — skipped")
        register_table(cur, "ib_node", "one row per grounding element an ib_observation cites "
                      "(strong/verse/subgroup/cluster/question/another observation)",
                      "The cluster-reading pack's own grounding table (#1692, design-complete "
                      "2026-09-14). Makes 'no way to check a finding's grounding' structurally "
                      "impossible via the CHECK constraint + the mandatory coverage self-check "
                      "(#1692 SS2: every strong/verse in a subgroup's membership must be grounded "
                      "by >=1 ib_node row, checked at LLM generation time and independently "
                      "re-checked by the recording pass at load time).")
        for ordinal, name, ctype, is_pk, notnull, is_unique, fk, use in (
            (0, "id", "INTEGER", 1, 1, 0, None, "surrogate PK, assigned by the recording pass"),
            (1, "observation_id", "INTEGER", 0, 1, 0, "ib_observation(id)",
             "which observation this grounding element belongs to"),
            (2, "cluster_code", "TEXT", 0, 1, 0, None,
             "a VALUE, not necessarily a copy of the parent observation's own cluster -- THE "
             "cluster this row references. One row per cluster when an observation touches "
             "multiple clusters."),
            (3, "cluster_subgroup_code", "TEXT", 0, 0, 0, None,
             "was family_key -- THE subgroup this row references (usually the observation's own, "
             "but can differ)"),
            (4, "strong", "TEXT", 0, 0, 0, None, "denormalized copy"),
            (5, "verse_reference", "TEXT", 0, 0, 0, None,
             "resolved FRESH against iba.db.verse.reference at load time, never trusted from the "
             "LLM's JSON directly (#1693's own fix)"),
            (6, "surface", "TEXT", 0, 0, 0, None, "was span_surface -- matches span.surface"),
            (7, "morph_code", "TEXT", 0, 0, 0, None, "was span_morph -- matches span.morph_code"),
            (8, "question_code", "TEXT", 0, 0, 0, None,
             "catalogue-question grounding -- not yet an enforced FK, restore once #1696 lands "
             "the catalogue into iba.db"),
            (9, "traced_observation_id", "INTEGER", 0, 0, 0, "ib_observation(id)",
             "set when grounded in ANOTHER observation instead of a verse"),
            (10, "source_stage", "TEXT", 0, 1, 0, None, "reading | answer | synthesis"),
            (11, "seq", "INTEGER", 0, 1, 0, None,
             "a plain per-observation ordinal -- ties together every ib_node row sharing one "
             "observation_id, in reading order when meaningful. UNIQUE(observation_id, seq) is "
             "the real natural key."),
            (12, "created_at", "TEXT", 0, 1, 0, None, "ISO-8601 UTC"),
        ):
            register_column(cur, "ib_node", name, ordinal, ctype, is_pk, notnull, is_unique, fk, use)

        if args.dry_run:
            conn.rollback()
            report.append("DRY-RUN: rolled back")
        else:
            conn.commit()
            report.append("COMMITTED")

        print("\n".join(report))
        return 0
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()


if __name__ == "__main__":
    sys.exit(main())
