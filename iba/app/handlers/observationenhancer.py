"""observationenhancer.py -- the observation_enhancer utility (escalation #1778, researcher-
approved design 2026-09-20: proposal doc iba/docs/1778-correction-rule-utility-proposal-v1-
20260919.md, verbatim researcher instruction "proceed with the build as planned").

Applies researcher-authored rules, stored in `cfg_observation_enhancer_rule` (added/edited via
the standard `configmaint.propose` cycle, same as any other cfg_* row -- NOT a bespoke mechanism
built here), to `ib_observation`. Each rule pairs a `selector_sql` (a single SELECT returning an
`id` column against `ib_observation`) with an `update_json` (column -> new value) applied via a
direct UPDATE. Every field actually changed is logged to `ib_observation_enhancer_log` (rule,
observation, field, before/after, when) -- the audit trail matching `ib_node`'s own
`traced_observation_id`/`source_stage` discipline.

Two steps, dispatched via run.py like any other cfg_step:

  preview(ctx) -- read-only. Runs the rule's selector_sql, returns the match count, a sample of
                  matched rows, and the update that would be applied. Any rule status.
  apply(ctx)   -- refuses unless the rule's status is 'confirmed' or 'active' -- the researcher's
                  own per-rule confirmation gate (#1778: safety is process, not a restricted
                  selector grammar -- look at a real preview run's actual matches, THEN confirm
                  via configmaint.propose, THEN apply). Runs selector_sql, applies update_json to
                  every matched row, logs each change, and promotes a first-time 'confirmed' rule
                  to 'active' on success.

selector_sql/update_json are re-validated live on every call (not just at authoring time): a
single SELECT only (no ';', no INSERT/UPDATE/DELETE/DROP/ATTACH/PRAGMA/ALTER, must reference
ib_observation, must return an 'id' column), and update_json may only name real ib_observation
columns, never the primary key.
"""

from __future__ import annotations

import datetime
import json
import sqlite3

from .base import Ctx, Outcome, ok, fail

_BANNED_KEYWORDS = ("INSERT", "UPDATE", "DELETE", "DROP", "ATTACH", "PRAGMA", "ALTER")
_SAMPLE_LIMIT = 10


def _now() -> str:
    return datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _get_rule(conn: sqlite3.Connection, rule_key: str) -> sqlite3.Row | None:
    return conn.execute(
        "SELECT * FROM cfg_observation_enhancer_rule WHERE rule_key=? AND active=1",
        (rule_key,)).fetchone()


def _applyable_statuses(conn: sqlite3.Connection) -> set[str]:
    """Live cfg_enum lookup, not a hardcoded tuple -- found live 2026-09-20 (escalation #1795):
    cfg_observation_enhancer_rule.status was registered as a cfg_enum group but nothing actually
    looked it up by name at runtime, exactly the orphan-enum pattern this build should not add to.
    'confirmed'/'active' are the two values that permit -Action Apply; intersected with the live
    enum (not just asserted) so a future cfg_enum edit that retires/renames one of them is caught
    here instead of silently still accepting the old name."""
    live = {r["value"] for r in conn.execute(
        "SELECT value FROM cfg_enum WHERE name='cfg_observation_enhancer_rule.status' "
        "AND inactive=0")}
    return live & {"confirmed", "active"}


def _validate_selector(sql: str) -> str | None:
    s = sql.strip()
    if ";" in s:
        return "selector_sql must not contain ';' (single statement only)"
    upper = s.upper()
    if not upper.startswith("SELECT"):
        return "selector_sql must start with SELECT"
    for banned in _BANNED_KEYWORDS:
        if banned in upper:
            return f"selector_sql must not contain {banned}"
    if "IB_OBSERVATION" not in upper:
        return "selector_sql must reference ib_observation"
    return None


def _validate_update_fields(conn: sqlite3.Connection, update: dict) -> str | None:
    if not update:
        return "update_json is empty -- a rule must change at least one field"
    info = list(conn.execute("PRAGMA table_info(ib_observation)"))
    cols = {r["name"] for r in info}
    pk = {r["name"] for r in info if r["pk"]}
    bad = set(update) - cols
    if bad:
        return f"update_json names unknown ib_observation column(s) {sorted(bad)}"
    locked = set(update) & pk
    if locked:
        return f"update_json cannot change primary key column(s) {sorted(locked)}"
    # Added 2026-09-20 (escalation #1796): for any column that has its own cfg_enum group
    # (ib_observation.<column>), the new value must be a live member of it -- e.g. a rule that
    # accidentally sets status to a typo/retired value now fails loudly at this gate instead of
    # writing an unvalidated string. Only checked for columns that actually have a registered enum
    # group (most don't) -- see meaning_source's own note in recordingpass.py for why THAT column's
    # live pipeline can't use this same strictness; a rule author targeting it deliberately through
    # this tool should still be held to the canonical values, unlike the hot LLM-write path.
    for col, value in update.items():
        enum_values = {r[0] for r in conn.execute(
            "SELECT value FROM cfg_enum WHERE name=? AND inactive=0", (f"ib_observation.{col}",))}
        if enum_values and value not in enum_values:
            return (f"update_json sets {col}={value!r}, not a live ib_observation.{col} enum "
                   f"value {sorted(enum_values)}")
    return None


def _run_selector(conn: sqlite3.Connection, selector_sql: str):
    """Returns (ids, sample_rows) or raises sqlite3.Error / ValueError("no-id-column")."""
    cur = conn.execute(selector_sql)
    cols = [d[0].lower() for d in cur.description] if cur.description else []
    if "id" not in cols:
        raise ValueError("no-id-column")
    ids = [r["id"] for r in cur.fetchall()]
    sample = []
    if ids:
        sample_ids = ids[:_SAMPLE_LIMIT]
        ph = ",".join("?" * len(sample_ids))
        sample = [dict(r) for r in conn.execute(
            f"SELECT id, cluster_code, stage, tag, strong, status, obs_text FROM ib_observation "
            f"WHERE id IN ({ph})", sample_ids)]
    return ids, sample


def preview(ctx: Ctx) -> Outcome:
    conn = ctx.db.conn
    rule_key = ctx.params.get("RuleKey")
    if not rule_key:
        return fail("missing-rule-key", "RuleKey is required")
    rule = _get_rule(conn, rule_key)
    if not rule:
        return fail("rule-not-found", f"no active cfg_observation_enhancer_rule with "
                    f"rule_key={rule_key!r}")
    err = _validate_selector(rule["selector_sql"])
    if err:
        return fail("invalid-selector", err)
    try:
        update = json.loads(rule["update_json"])
    except json.JSONDecodeError as exc:
        return fail("invalid-update-json", f"update_json is not valid JSON: {exc}")
    try:
        ids, sample = _run_selector(conn, rule["selector_sql"])
    except ValueError:
        return fail("selector-missing-id", "selector_sql must return an 'id' column")
    except sqlite3.Error as exc:
        return fail("selector-error", f"selector_sql failed: {exc}")
    return ok(f"rule {rule_key!r} (status={rule['status']}) matches {len(ids)} row(s); would set "
             f"{update} on each", matched_count=len(ids), status=rule["status"], update=update,
             sample=sample)


def apply(ctx: Ctx) -> Outcome:
    conn = ctx.db.conn
    rule_key = ctx.params.get("RuleKey")
    if not rule_key:
        return fail("missing-rule-key", "RuleKey is required")
    rule = _get_rule(conn, rule_key)
    if not rule:
        return fail("rule-not-found", f"no active cfg_observation_enhancer_rule with "
                    f"rule_key={rule_key!r}")
    if rule["status"] not in _applyable_statuses(conn):
        return fail("rule-not-confirmed",
                    f"rule {rule_key!r} has status={rule['status']!r} -- run -Action Preview and "
                    f"confirm it (configmaint.propose: cfg_observation_enhancer_rule update "
                    f"status='confirmed') before it can be applied")
    sel_err = _validate_selector(rule["selector_sql"])
    if sel_err:
        return fail("invalid-selector", sel_err)
    try:
        update = json.loads(rule["update_json"])
    except json.JSONDecodeError as exc:
        return fail("invalid-update-json", f"update_json is not valid JSON: {exc}")
    upd_err = _validate_update_fields(conn, update)
    if upd_err:
        return fail("invalid-update", upd_err)
    try:
        ids, _sample = _run_selector(conn, rule["selector_sql"])
    except ValueError:
        return fail("selector-missing-id", "selector_sql must return an 'id' column")
    except sqlite3.Error as exc:
        return fail("selector-error", f"selector_sql failed: {exc}")
    if not ids:
        return ok(f"rule {rule_key!r} matched 0 row(s) -- nothing to apply", matched_count=0,
                  applied=0)

    now = _now()
    set_cols = list(update)
    quoted_cols = ",".join(f'"{c}"' for c in set_cols)
    set_clause = ", ".join(f'"{c}"=?' for c in set_cols)
    changed = 0
    for obs_id in ids:
        before = conn.execute(
            f'SELECT {quoted_cols} FROM ib_observation WHERE id=?', (obs_id,)).fetchone()
        conn.execute(f'UPDATE ib_observation SET {set_clause} WHERE id=?',
                    [update[c] for c in set_cols] + [obs_id])
        for c in set_cols:
            conn.execute(
                "INSERT INTO ib_observation_enhancer_log (rule_id, rule_key, observation_id, "
                "field_changed, before_value, after_value, applied_at, run_id) "
                "VALUES (?,?,?,?,?,?,?,?)",
                (rule["id"], rule_key, obs_id, c, str(before[c]) if before else None,
                 str(update[c]), now, ctx.run_id))
        changed += 1

    if rule["status"] == "confirmed":
        conn.execute("UPDATE cfg_observation_enhancer_rule SET status='active' WHERE id=?",
                    (rule["id"],))

    return ok(f"rule {rule_key!r} applied to {changed} row(s)", matched_count=len(ids),
             applied=changed)
