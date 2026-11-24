"""surface_relation_schema_2548_v1_20261124.py -- escalation #2548, stage 1: the tables and the config of the surface relations.

The researcher's decisions of 2026-11-24 (brief outputs/escalation/2548-surface-relation-build-brief-v1-20261124.md): capture the WordNet
study of the single-word surfaces (#2545) in iba.db so it lives and is used in analysis. Follows the #2361 pattern
(iba/app/migration/archive/surface_cycle_schema_2361_v1_20261106.py).

  NEW (data)   surface_relation        one row per unordered pair of surfaces that an outside source (WordNet 3.0) links
               surface_network_group   one row per surface per grouping: the connected group of the pair network it sits in
  EXTENDED     surface_flag.kind       the value wordnet_no_pair (the surfaces WordNet leaves with no pair), enum and column note
               surface_cycle_module    the value relation (for the working files of the step set)
  NEW (config) surfaces.relation_scope, surfaces.relation_pair_rules (cfg_setting): which surfaces the relation study covers and
               how a pair gets its type and weight, so neither is held in code.
Every cfg_* write goes through configmaint.apply_logged(); the physical tables are built from their cfg_column rows
(lib/db.table_ddl). A named rollback snapshot is taken before a live apply. Idempotent. One transaction. Writes no data row.

Usage:
    python iba/app/migration/archive/surface_relation_schema_2548_v1_20261124.py [--db PATH] [--dry-run] [--no-snapshot]
"""
import argparse
import json
import pathlib
import sys

ROOT = next(p for p in pathlib.Path(__file__).resolve().parents if (p / "iba" / "app").is_dir())
sys.path.insert(0, str(ROOT))
from iba.app.handlers.configmaint import apply_logged  # noqa: E402
from iba.app.lib.cfg import Cfg  # noqa: E402
from iba.app.lib.db import table_ddl  # noqa: E402

DEFAULT_DB = pathlib.Path(r"C:\Bible_study_projects\iba\app\db\iba.db")
RUN_ID = "DEVMODE-2548-SURFACE-RELATION-SCHEMA-20261124"
MODULE = "surface_relation_schema_2548_v1_20261124"
SOURCE = "escalation #2548, the researcher's decisions of 2026-11-24 (brief v1 of 2026-11-24)"
FILLED = ("the step Surface-Relation.ps1 (stage 2 of #2548): Load for surface_relation, Groups for surface_network_group; "
          "no row is written by this migration")
NOW = "(strftime('%Y-%m-%dT%H:%M:%SZ','now'))"
WHO = "who wrote the row: Claude, Researcher, migration, or 'direct edit' (the default, a row inserted outside the tool)"

ENUMS = {
    "surface_relation.pair_type": ["synonym", "antonym", "derivational", "similar", "same_base", "both"],
    "surface_relation.source": ["wordnet"],
    "surface_network_group.kind": ["main", "small", "no_pair"],
    "surface_network_group.status": ["indicative", "confirmed"],
}
# added to an enum that already exists (the value is defined in the note of the column that uses the enum)
ENUM_ADD = {"surface_flag.kind": ["wordnet_no_pair"], "surface_cycle_module": ["relation"]}

FLAG_KIND_USE_OLD = "phrase_no_match (a phrase that no word and no own Strong code connects to a collection: to inspect, #2437), other"
FLAG_KIND_USE_ADD = (", wordnet_no_pair (a single-word surface of the relation study that WordNet pairs with no other surface: to be "
                     "dealt with by hand, #2548; the class of the review and who acts are in the note)")


def c(name, typ, use, *, pk=0, nn=0, dflt=None, fk=None, exp=None):
    return {"name": name, "type": typ, "use": use, "pk": pk, "nn": nn, "dflt": dflt, "fk": fk, "exp": exp}


def tail():
    return [
        c("run_id", "TEXT", "the run that wrote the row (run.run_id)"),
        c("created_at", "TEXT", "when (ISO-8601 UTC)", nn=1, dflt=NOW),
        c("updated_at", "TEXT", "when last changed (ISO-8601 UTC)"),
        c("created_by", "TEXT", WHO, nn=1, dflt="'direct edit'"),
        c("deleted", "INTEGER", "soft delete, version-aware as in verse_lexical: 1 when the row is no longer the current one "
          "(superseded by a later load or grouping); nothing in this cycle is ever physically deleted", nn=1, dflt="0"),
        c("load_ref", "TEXT", "for a row loaded from a recorded file: the file and line it came from; NULL for a row made by a step"),
    ]


def pk():
    return c("id", "INTEGER", "surrogate PK", pk=1, nn=1)


T = {}

T["surface_relation"] = dict(
    category="data", grain="one row per unordered pair of surfaces that an outside source links, per source",
    use=("Relations between English surfaces (#2548). Until now no table related one English surface to another: strong_related "
         "relates Strong's codes, collection_link places a base in a collection. A row here says that an OUTSIDE source "
         "(today WordNet 3.0, read through NLTK) links two surfaces of the relation study (scope in cfg_setting "
         "surfaces.relation_scope): the two terms, what kind of link (pair_type), how strong (weight) and how many links of "
         "each kind were counted. The pair is unordered: term_a_id < term_b_id, so a pair is held once. The source is modern "
         "general English, not the Bible: a row is a candidate relation to read, not a study finding, and carries no "
         "inner-being reading; a surface can be linked through a sense its verses never use. The row is derived: the step "
         "recomputes it from the source, and a changed rule or source version adds new rows and flips the earlier to "
         "deleted = 1. The distance matrices (hops, weighted: shortest path over these pairs, length 1 / weight) are not "
         "stored; they are regenerated from this table. Navigate: term_a_id and term_b_id to surface_term; the collections "
         "of the two through collection_link on their bases; the group in surface_network_group"),
    cols=[
        pk(),
        c("term_a_id", "INTEGER", "points to surface_term.id: the first surface of the pair; always the lower id of the two",
          nn=1, fk="surface_term.id"),
        c("term_b_id", "INTEGER", "points to surface_term.id: the second surface of the pair; always the higher id", nn=1,
          fk="surface_term.id"),
        c("pair_type", "TEXT", "the kind of link, the first that holds in the order in cfg_setting surfaces.relation_pair_rules: "
          "same_base (the two resolve to one WordNet base form: walk, walked), both (they share a synset and an antonym link "
          "also holds), synonym (they share at least one synset), derivational (a derivationally related form or pertainym: "
          "bold, boldness, boldly), similar (similar-to between adjective sense groups: generous, bountiful), antonym (an "
          "antonym link between their lemmas)", nn=1, exp="enum.surface_relation.pair_type"),
        c("weight", "INTEGER", "the strength of the pair: synsets_shared + antonym_links + derivational_links + similar_links "
          "(a pair that holds several links has them added); the length of the pair in the distance matrices is 1 / weight",
          nn=1),
        c("synsets_shared", "INTEGER", "how many WordNet synsets (senses) the two share; 0 when none", nn=1, dflt="0"),
        c("antonym_links", "INTEGER", "how many antonym links join a lemma of one to a lemma of the other; 0 when none", nn=1,
          dflt="0"),
        c("derivational_links", "INTEGER", "1 when WordNet lists the two as derivationally related forms or pertainyms, else 0",
          nn=1, dflt="0"),
        c("similar_links", "INTEGER", "how many similar-to links join a sense group of one to a sense group of the other; 0 when "
          "none", nn=1, dflt="0"),
        c("source", "TEXT", "the outside source that links the two", nn=1, dflt="'wordnet'", exp="enum.surface_relation.source"),
        c("source_version", "TEXT", "the version of the source the row was computed from (WordNet 3.0), so a later version does "
          "not overwrite the earlier", nn=1),
    ] + tail(),
    unique=["term_a_id", "term_b_id", "source"],
    indexes=[("idx_surface_relation_term_a", ["term_a_id"]), ("idx_surface_relation_term_b", ["term_b_id"]),
             ("idx_surface_relation_pair_type", ["pair_type"])],
)

T["surface_network_group"] = dict(
    category="data", grain="one row per surface per grouping of the relation network",
    use=("The connected groups of the surface relation network (#2548): a group is a set of surfaces joined by surface_relation "
         "pairs, directly or through other surfaces. One row per surface of the relation study (scope in cfg_setting "
         "surfaces.relation_scope), including the surfaces with no pair (kind no_pair, a group of one) and those WordNet "
         "does not hold (in_wordnet = 0). group_no numbers the groups by size, largest first, within one grouping; the "
         "largest group (kind main) is the loose mass of surfaces joined through shared senses; kind small is a group of 2 "
         "or more outside it. The grouping is derived: a later grouping (a changed rule or source version) flips the "
         "earlier rows to deleted = 1 and adds its own, so the earlier is kept. status stays indicative; confirmed only "
         "when the researcher recognises the group as a concept. The researcher's views of the groups are recorded as "
         "views in the escalation record (#2545, #2548), never as findings here. Navigate: term_id to surface_term; the "
         "pairs of the group in surface_relation where term_a_id or term_b_id is a member"),
    cols=[
        pk(),
        c("term_id", "INTEGER", "points to surface_term.id: the surface this row places in a group", nn=1, fk="surface_term.id"),
        c("group_no", "INTEGER", "the number of the group within its grouping, 1 the largest; surfaces with the same number "
          "and the same run_id are one group", nn=1),
        c("group_size", "INTEGER", "how many surfaces the group holds; 1 for a surface with no pair", nn=1),
        c("kind", "TEXT", "main (the largest group), small (a group of 2 or more that is not the largest), no_pair (a group of "
          "one: WordNet pairs the surface with no other surface of the study)", nn=1, exp="enum.surface_network_group.kind"),
        c("in_wordnet", "INTEGER", "1 when the source holds the surface, 0 when it does not (a no_pair row of a surface the "
          "source does not hold)", nn=1),
        c("status", "TEXT", "indicative (the computed grouping, the default) or confirmed (the researcher recognised the "
          "group)", nn=1, dflt="'indicative'", exp="enum.surface_network_group.status"),
    ] + tail(),
    unique=["term_id"],
    indexes=[("idx_surface_network_group_no", ["group_no"]), ("idx_surface_network_group_kind", ["kind"])],
)

SETTINGS = {
    "surfaces.relation_scope": (
        {"form": "word", "origin": ["surface", "computed"], "groups": ["behaviour", "inner_being_state"],
         "moved_from_groups": ["behaviour", "inner_being_state"], "moved_since": "2026-11-09", "include_unjudged": True},
        "which surfaces the relation study covers (#2548): the live surface_term rows of form word that are in one of groups, "
        "or unjudged (include_unjudged), or whose surface_event for surface_group records a move from one of "
        "moved_from_groups on or after moved_since (the date the study list was fixed, 2026-11-09). origin lists the origins "
        "read: a computed base is a surface of the study when it is in the groups. Verified against the study list of "
        "2026-11-23: 2,742 surfaces, none more and none fewer. The scope of a surface is not stored: it follows from this rule"),
    "surfaces.relation_pair_rules": (
        {"source": "wordnet", "source_version": "3.0", "type_order": ["same_base", "both", "synonym", "derivational", "similar",
                                                                      "antonym"],
         "weight": "synsets_shared + antonym_links + derivational_links + similar_links", "distance": "1 / weight",
         "small_group_min": 2},
        "how a WordNet pair of surfaces gets its type and weight (#2548): the type is the first that holds in type_order "
        "(same_base: the two resolve to one WordNet base form; both: a shared synset and an antonym link; synonym: a shared "
        "synset; derivational: derivationally related form or pertainym; similar: similar-to between adjective sense groups; "
        "antonym); the weight is the sum of the link counts; the distance of a pair is 1 / weight. source_version is stored on "
        "every relation row. small_group_min is the size from which a group outside the largest is kind small"),
}


def cfg_col(table, ordinal, col):
    return {"database": "iba", "table_name": table, "name": col["name"], "ordinal": ordinal, "type": col["type"],
            "is_pk": col["pk"], "notnull": col["nn"], "is_unique": 0, "dflt": col["dflt"], "fk": col["fk"],
            "use": col["use"], "expectation": col["exp"], "source": SOURCE, "filled_by": FILLED, "inactive": 0}


def plan(conn) -> list[tuple]:
    ops = []
    has = lambda sql, *a: conn.execute(sql, a).fetchone() is not None  # noqa: E731
    for ename, values in ENUMS.items():
        for i, v in enumerate(values):
            if not has("SELECT 1 FROM cfg_enum WHERE name=? AND value=?", ename, v):
                ops.append(("cfg_enum", "insert", {}, {"name": ename, "value": v, "ordinal": i, "inactive": 0}))
    for ename, values in ENUM_ADD.items():
        top = conn.execute("SELECT COALESCE(MAX(ordinal),-1) FROM cfg_enum WHERE name=?", (ename,)).fetchone()[0]
        for v in values:
            if not has("SELECT 1 FROM cfg_enum WHERE name=? AND value=?", ename, v):
                top += 1
                ops.append(("cfg_enum", "insert", {}, {"name": ename, "value": v, "ordinal": top, "inactive": 0}))
    use = conn.execute("SELECT use FROM cfg_column WHERE table_name='surface_flag' AND name='kind'").fetchone()[0]
    if "wordnet_no_pair" not in use:
        if FLAG_KIND_USE_OLD not in use:
            raise RuntimeError("the note of surface_flag.kind is not the one this migration was written against")
        ops.append(("cfg_column", "update", {"table_name": "surface_flag", "name": "kind"},
                    {"use": use.replace(FLAG_KIND_USE_OLD, FLAG_KIND_USE_OLD + FLAG_KIND_USE_ADD)}))
    for t, d in T.items():
        if not has("SELECT 1 FROM cfg_table WHERE database='iba' AND name=?", t):
            ops.append(("cfg_table", "insert", {}, {"database": "iba", "name": t, "grain": d["grain"], "use": d["use"],
                                                    "inactive": 0, "category": d["category"]}))
            for i, col in enumerate(d["cols"]):
                ops.append(("cfg_column", "insert", {}, cfg_col(t, i, col)))
            for i, ucol in enumerate(d["unique"] or []):
                ops.append(("cfg_unique", "insert", {}, {"database": "iba", "table_name": t, "col": ucol, "ordinal": i}))
            for iname, icols in d["indexes"]:
                for i, icol in enumerate(icols):
                    ops.append(("cfg_index", "insert", {}, {"table_name": t, "name": iname, "col": icol, "ordinal": i}))
            ops.append(("cfg_write_grant", "insert", {}, {"writer": "migration", "table_name": t, "database": "iba",
                                                          "inactive": 0}))
    for key, (value, use_) in SETTINGS.items():
        if not has("SELECT 1 FROM cfg_setting WHERE key=?", key):
            ops.append(("cfg_setting", "insert", {}, {"key": key, "module": "surfaces", "inactive": 0,
                                                      "value": json.dumps(value), "use": use_}))
    if not has("SELECT 1 FROM cfg_utility WHERE module=?", MODULE):
        ops.append(("cfg_utility", "insert", {}, {
            "module": MODULE, "file_path": f"iba/app/migration/{MODULE}.py", "inactive": 1,
            "purpose": f"ONE-OFF migration -- escalation #2548 stage 1: the tables surface_relation and surface_network_group, the "
                       f"flag kind wordnet_no_pair and the settings of the relation study; run_id {RUN_ID}.",
            "config_exempt": 1, "config_exempt_reason": "one-off migration script -- writes cfg_* rows through "
            "configmaint.apply_logged, same class as the other Developer Mode migrations",
            "crash_escalation_reviewed": 0, "crash_escalation_note": None}))
    return ops


def physical(conn, cfg):
    live = {r[0] for r in conn.execute("SELECT name FROM sqlite_master WHERE type='table'")}
    for t in T:
        if t not in live:
            create_sql, index_sql = table_ddl(cfg, t)
            conn.execute(create_sql)
            for sql in index_sql:
                conn.execute(sql)


def verify(conn):
    bad = []
    for t in T:
        have = [r[1] for r in conn.execute(f'PRAGMA table_info("{t}")')]
        want = [r[0] for r in conn.execute("SELECT name FROM cfg_column WHERE table_name=? AND inactive=0 ORDER BY ordinal", (t,))]
        if sorted(have) != sorted(want):
            bad.append(f"{t}: physical {sorted(set(have) ^ set(want))}")
        n = conn.execute(f'SELECT count(*) FROM "{t}"').fetchone()[0]
        if n:
            bad.append(f"{t} holds {n} row(s)")
    for ename, values in {**ENUMS, **ENUM_ADD}.items():
        for v in values:
            if not conn.execute("SELECT 1 FROM cfg_enum WHERE name=? AND value=? AND inactive=0", (ename, v)).fetchone():
                bad.append(f"enum {ename}.{v} missing")
    for key in SETTINGS:
        if not conn.execute("SELECT 1 FROM cfg_setting WHERE key=? AND inactive=0", (key,)).fetchone():
            bad.append(f"setting {key} missing")
    return bad


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default=str(DEFAULT_DB))
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--no-snapshot", action="store_true", help="for a test copy: no rollback snapshot")
    a = ap.parse_args()
    cfg = Cfg(pathlib.Path(a.db))
    conn = cfg.conn
    ops = plan(conn)
    if a.dry_run:
        kinds = {}
        for t, op, _, _ in ops:
            kinds[(t, op)] = kinds.get((t, op), 0) + 1
        print(f"DRY RUN: {len(ops)} cfg write(s)")
        for (t, op), n in sorted(kinds.items()):
            print(f"  {t} {op}: {n}")
        return 0
    if not ops:
        print("already applied: nothing changed")
        return 0
    if not a.no_snapshot:
        from iba.app.lib import dbsnapshot
        print(f"named rollback snapshot: {dbsnapshot.snapshot('pre-2548-schema', named=True)}")
    try:
        conn.execute("SAVEPOINT surface_relation_schema")
        for t, op, where, set_ in ops:
            apply_logged(conn, RUN_ID, t, op, where, set_)
        physical(conn, cfg)
        bad = verify(conn)
        if bad:
            raise RuntimeError("verification failed: " + "; ".join(bad))
        conn.execute("RELEASE surface_relation_schema")
        conn.commit()
    except Exception:
        conn.execute("ROLLBACK TO surface_relation_schema")
        conn.execute("RELEASE surface_relation_schema")
        raise
    print(f"applied (run {RUN_ID}): {len(ops)} cfg write(s); tables built: {list(T)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
