"""surface_pair_verdict_2354_v1_20261102.py -- escalation #2354 (plan v5, outputs/escalation/2354-concepts-retry-plan-v5-20261102.md;
researcher, chat 2026-11-02: the Ollama server judges; P2 and P3 left to my judgement).

Builds the table that holds the verdict on every (strong, surface) pair of the corpus, and the settings of the Ollama
server that judges. Most pairs have no surface_subgroup row to carry a surface_group (13,462 of 101,458), so the verdicts
live here; surface_subgroup.surface_group is later filled from this table for the concept pairs only.

  surface_pair_verdict  one row per (strong, lower-cased surface): pair_kind (particle, own, span_shared -- how far the
                        surface is the code's own, from verse_lexical), surface_group (the five values of
                        surface_subgroup.surface_group), use (for a qualifier only: the use that makes it one), reason,
                        judged_by (rule:<name> or the model), run_id
  cfg_setting module 'ollama': host, model, timeout, keep-alive, context size, temperature, codes per call; and
                        'surface_judge': the folder of the batch files

The table is built from its cfg_column rows (lib/db.table_ddl). cfg_* writes go through configmaint.apply_logged();
no verdict row is written. Registers itself (inactive, at its archive path). Idempotent. One transaction.

Usage:
    python iba/app/migration/surface_pair_verdict_2354_v1_20261102.py [--db PATH] [--dry-run]
"""
import argparse
import json
import pathlib
import sys

ROOT = next(p for p in pathlib.Path(__file__).resolve().parents if (p / "iba" / "app").is_dir())  # live or archived
sys.path.insert(0, str(ROOT))
from iba.app.handlers.configmaint import apply_logged  # noqa: E402
from iba.app.lib.cfg import Cfg  # noqa: E402
from iba.app.lib.db import table_ddl  # noqa: E402

DEFAULT_DB = pathlib.Path(r"C:\Bible_study_projects\iba\app\db\iba.db")
RUN_ID = "DEVMODE-2354-PAIR-VERDICT-20261102"
MODULE = "surface_pair_verdict_2354_v1_20261102"
T = "surface_pair_verdict"
SOURCE = ("escalation #2354 (plan v5 outputs/escalation/2354-concepts-retry-plan-v5-20261102.md; researcher, chat "
          "2026-11-02: use the Ollama server, details left to my judgement)")
FILLED = f"iba/app/migration/archive/{MODULE}.py creates the table; no step writes it yet"
NOW = "(strftime('%Y-%m-%dT%H:%M:%SZ','now'))"
WHO = "who wrote the row: Claude, Researcher, migration, or 'direct edit' (the default, a row inserted outside the tool)"
INF = "Provisional and inferential (B:4) until the researcher confirms."

GROUPS = ["behaviour", "inner_being_state", "being", "qualifier", "not_allocated"]
USES = ["place", "time", "quantity", "quality", "manner", "reason", "negation", "pronoun", "article", "conjunction",
        "preposition", "particle", "other"]
KINDS = ["particle", "own", "span_shared"]
ENUMS = {f"{T}.surface_group": GROUPS, f"{T}.use": USES, f"{T}.pair_kind": KINDS}


def col(name, ordinal, typ, use, *, pk=0, nn=0, dflt=None, fk=None, enum=None):
    return {"database": "iba", "table_name": T, "name": name, "ordinal": ordinal, "type": typ, "is_pk": pk,
            "notnull": nn, "is_unique": 0, "dflt": dflt, "fk": fk, "use": use,
            "expectation": f"enum.{T}.{enum}" if enum else None, "source": SOURCE, "filled_by": FILLED, "inactive": 0}


COLS = [
    col("id", 0, "INTEGER", "surrogate PK", pk=1, nn=1),
    col("strong", 1, "TEXT", "the Strong's code of the pair, with its suffix as in verse_lexical.strong", nn=1,
        fk="strong.strongNumber"),
    col("surface", 2, "TEXT", "the English rendering of the pair, lower-cased, as in verse_lexical.surface", nn=1),
    col("pair_kind", 3, "TEXT", "how far the surface is the code's own, read from verse_lexical: particle (the code "
        "is H9xxx; the surface is the span's English, not trusted), own (the code has an occurrence in a span with a "
        "single non-particle code), span_shared (only in spans with two or more non-particle codes, so the surface is "
        "the unit's English); BUILD 428 and the 2354 working log finding 28", nn=1, enum="pair_kind"),
    col("surface_group", 4, "TEXT", "the group of the pair: behaviour, inner_being_state, being, qualifier or "
        "not_allocated (held back for the researcher to inspect). " + INF, nn=1, enum="surface_group"),
    col("use", 5, "TEXT", "for a qualifier only: the use that makes the word one (place, time, quantity, quality, "
        "manner, reason, negation, pronoun, article, conjunction, preposition, particle, other); NULL for any other "
        "group. A pronoun is a qualifier of use pronoun: who it names is resolved when the verse is read (researcher, "
        "2026-11-02)", enum="use"),
    col("reason", 6, "TEXT", "one line on why, kept for a qualifier and for not_allocated; NULL otherwise"),
    col("judged_by", 7, "TEXT", "what decided it: rule:<name> (a rule on the code) or the Ollama model name with its "
        "tag, as in ollama.model at the time", nn=1),
    col("run_id", 8, "TEXT", "the run that wrote the row"),
    col("created_at", 9, "TEXT", "when (ISO-8601 UTC)", nn=1, dflt=NOW),
    col("updated_at", 10, "TEXT", "when last changed (ISO-8601 UTC)"),
    col("created_by", 11, "TEXT", WHO, nn=1, dflt="'direct edit'"),
    col("deleted", 12, "INTEGER", "soft delete: 1 when the row is no longer live", nn=1, dflt="0"),
]
GRAIN = "one row per (strong, surface) pair of the corpus"
USE = ("#2354: the verdict on every (Strong's code, English surface) pair of verse_lexical, made once per distinct "
       "pair (not per occurrence). The home of the surface group of the pairs that have no surface_subgroup row; "
       "surface_subgroup.surface_group is filled from it for the concept pairs. pair_kind says how far the surface "
       "can be trusted as the code's own (multi-code spans carry the span's English, BUILD 428). All verdicts "
       "inferential (B:4) until the researcher confirms")
UNIQUE = ["strong", "surface"]
INDEXES = [("idx_surface_pair_verdict_group", ["surface_group"])]

SETTINGS = [
    ("ollama.host", "http://192.168.83.114:11434", "the Ollama server that judges the surfaces (#2354); address changed "
     "from .113 on 2026-11-02; Ubuntu host zeta-assist, 8 cores, 76 GB RAM, no GPU", "ollama"),
    ("ollama.model", "qwen3:30b", "the model that judges the surfaces; chosen 2026-11-02 after a timing test "
     "(working log findings 26, 27)", "ollama"),
    ("ollama.timeout_seconds", 900, "seconds to wait for one call (CPU-only server, 23 to 29 s per surface measured; "
     "the first call after a load takes about 2 minutes)", "ollama"),
    ("ollama.keep_alive", "30m", "how long the server keeps the model in memory after a call", "ollama"),
    ("ollama.num_ctx", 4096, "context window of one call, in tokens (the prompt and the answer of one surface fit)",
     "ollama"),
    ("ollama.temperature", 0, "0 so that the same question gives the same answer", "ollama"),
    ("ollama.max_codes_per_call", 8, "most codes of one surface judged in one call; a surface with more runs in "
     "several calls", "ollama"),
    ("surface_judge.batch_dir", "outputs/concept-mapping/surface-group", "folder of the batch files of the surface "
     "judging (#2354): each batch is written here before anything is loaded to surface_pair_verdict", "surface_judge"),
]


def plan(conn) -> list[tuple]:
    ops = []
    has = lambda sql, *a: conn.execute(sql, a).fetchone() is not None  # noqa: E731
    if not has("SELECT 1 FROM cfg_table WHERE database='iba' AND name=?", T):
        ops.append(("cfg_table", "insert", {}, {"database": "iba", "name": T, "grain": GRAIN, "use": USE,
                                                "inactive": 0, "category": "data"}))
    for w in ("migration",):
        if not has("SELECT 1 FROM cfg_write_grant WHERE writer=? AND table_name=? AND database='iba'", w, T):
            ops.append(("cfg_write_grant", "insert", {}, {"writer": w, "table_name": T, "database": "iba",
                                                          "inactive": 0}))
    for i, c in enumerate(UNIQUE):
        if not has("SELECT 1 FROM cfg_unique WHERE database='iba' AND table_name=? AND col=?", T, c):
            ops.append(("cfg_unique", "insert", {}, {"database": "iba", "table_name": T, "col": c, "ordinal": i}))
    for name, cols in INDEXES:
        for i, c in enumerate(cols):
            if not has("SELECT 1 FROM cfg_index WHERE table_name=? AND name=? AND col=?", T, name, c):
                ops.append(("cfg_index", "insert", {}, {"table_name": T, "name": name, "col": c, "ordinal": i}))
    for c in COLS:
        if not has("SELECT 1 FROM cfg_column WHERE database='iba' AND table_name=? AND name=?", T, c["name"]):
            ops.append(("cfg_column", "insert", {}, c))
    for enum, values in ENUMS.items():
        for i, v in enumerate(values):
            if not has("SELECT 1 FROM cfg_enum WHERE name=? AND value=?", enum, v):
                ops.append(("cfg_enum", "insert", {}, {"name": enum, "value": v, "ordinal": i, "inactive": 0}))
    for key, value, use, module in SETTINGS:
        if not has("SELECT 1 FROM cfg_setting WHERE key=?", key):
            ops.append(("cfg_setting", "insert", {}, {"key": key, "value": json.dumps(value), "use": use,
                                                      "module": module, "inactive": 0}))
    if not has("SELECT 1 FROM cfg_utility WHERE module=?", MODULE):
        ops.append(("cfg_utility", "insert", {}, {
            "module": MODULE, "file_path": f"iba/app/migration/archive/{MODULE}.py", "inactive": 1,
            "config_exempt": 1, "config_exempt_reason": "one-off migration script -- writes cfg_* rows through "
            "configmaint.apply_logged, same class as the other Developer Mode migrations",
            "purpose": f"ONE-OFF migration -- escalation #2354: table {T} and the ollama and surface_judge "
                       f"settings; run_id {RUN_ID}."}))
    return ops


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default=str(DEFAULT_DB))
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()
    cfg = Cfg(pathlib.Path(a.db))
    conn = cfg.conn
    live = {r[0] for r in conn.execute("SELECT name FROM sqlite_master WHERE type='table'")}
    ops = plan(conn)
    if a.dry_run:
        print(f"DRY RUN: {len(ops)} cfg write(s); table to create: {T not in live}")
        for t, op, where, set_ in ops:
            what = set_.get("name") or set_.get("module") or set_.get("key") or set_.get("col")
            print(f"  {t} {op} {set_.get('table_name', '')} {what} {set_.get('value', '')}")
        return 0
    if T in live and not ops:
        print("already applied: the table and its config exist; nothing changed")
        return 0
    try:
        conn.execute("SAVEPOINT pair_verdict")
        for t, op, where, set_ in ops:
            apply_logged(conn, RUN_ID, t, op, where, set_)
        if T not in live:
            create_sql, index_sql = table_ddl(cfg, T)
            conn.execute(create_sql)
            for sql in index_sql:
                conn.execute(sql)
        conn.execute("RELEASE pair_verdict")
        conn.commit()
    except Exception:
        conn.execute("ROLLBACK TO pair_verdict")
        conn.execute("RELEASE pair_verdict")
        raise
    print(f"applied (run {RUN_ID}): {len(ops)} cfg write(s); table {T} created: {T not in live}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
