"""conceptedit.py -- the researcher's edits to the concept grouping (escalation #2355): the description of a
domain or a concept, a new domain, and a domain's delete flag. Rows of concept_domain and concept are soft-deleted
(deleted=1), never removed. Each function takes the grant-checked Writer of its step (lib/narrativeregister.py) and
raises EditError on a refusal; the caller runs the unit in one savepoint, so a refusal writes nothing.

A domain is not deleted while it holds live concepts: what becomes of those concepts is the researcher's decision,
so the refusal names them. concept_subgroup (the link table) is not touched here."""
from __future__ import annotations

import datetime
import sqlite3

TABLES = {"domain": "concept_domain", "concept": "concept"}


class EditError(Exception):
    """A refusal: the reason is shown to the researcher and nothing is written."""


def _now() -> str:
    return datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _table(level: str) -> str:
    try:
        return TABLES[(level or "").strip().lower()]
    except KeyError:
        raise EditError(f"-Level is Domain or Concept, not {level!r}") from None


def _cur(conn: sqlite3.Connection) -> sqlite3.Cursor:
    """A cursor whose rows read by column name; the shared connection's own row factory is left alone."""
    cur = conn.cursor()
    cur.row_factory = sqlite3.Row
    return cur


def _row(conn: sqlite3.Connection, table: str, id_: int) -> sqlite3.Row:
    row = _cur(conn).execute(f'SELECT * FROM "{table}" WHERE id=?', (id_,)).fetchone()
    if row is None:
        raise EditError(f"no {table} row with id {id_}")
    return row


def list_rows(conn: sqlite3.Connection, level: str | None, domain_id: int | None, deleted: bool) -> list[str]:
    """Lines for the domains (and their concepts when level is Concept or empty); deleted rows only if asked."""
    cur = _cur(conn)
    live = "" if deleted else "AND deleted=0"
    show = lambda d: (d or "-").replace("\n", " ")  # noqa: E731
    out = []
    if level is None or level.lower() == "domain":
        for r in cur.execute(f"SELECT * FROM concept_domain WHERE 1=1 {live} ORDER BY ordinal, id"):
            out.append(f"domain {r['id']} | {r['ordinal']} | {r['name']}{' | DELETED' if r['deleted'] else ''}"
                       f" | {show(r['description'])}")
    if level is None or level.lower() == "concept":
        sql = f"SELECT * FROM concept WHERE 1=1 {live}" + (" AND domain_id=?" if domain_id else "")
        for r in cur.execute(sql + " ORDER BY domain_id, ordinal, id", (domain_id,) if domain_id else ()):
            out.append(f"concept {r['id']} | domain {r['domain_id']} | {r['ordinal']} | {r['name']}"
                       f"{' | DELETED' if r['deleted'] else ''} | {show(r['description'])}")
    return out


def describe(w, level: str, id_: int, text: str, run_id: str) -> str:
    """Set the description of one live domain or concept. The wording it replaces is shown in the line returned."""
    table = _table(level)
    text = (text or "").strip()
    if not text:
        raise EditError("the description is empty: nothing to set")
    row = _row(w.conn, table, id_)
    if row["deleted"]:
        raise EditError(f"{table} {id_} ({row['name']}) is deleted: restore it first")
    w.update(table, {"id": id_}, {"description": text, "updated_at": _now(), "run_id": run_id})
    was = row["description"]
    return f"{table} {id_} {row['name']}: description set" + (f" (was: {was})" if was else " (was empty)")


def add_domain(w, name: str, ordinal: int | None, description: str | None, who: str, run_id: str) -> str:
    """A new live domain, last in order unless an ordinal is given; the name and the ordinal are free among live ones."""
    name = (name or "").strip()
    if not name:
        raise EditError("-Name is required")
    if w.conn.execute("SELECT 1 FROM concept_domain WHERE name=? AND deleted=0", (name,)).fetchone():
        raise EditError(f"a live domain named {name!r} exists")
    if ordinal is None:
        ordinal = w.conn.execute("SELECT COALESCE(MAX(ordinal),0)+1 FROM concept_domain WHERE deleted=0").fetchone()[0]
    elif w.conn.execute("SELECT 1 FROM concept_domain WHERE ordinal=? AND deleted=0", (ordinal,)).fetchone():
        raise EditError(f"ordinal {ordinal} is taken by a live domain: leave -Ordinal off for the next free one")
    row = {"name": name, "ordinal": ordinal, "run_id": run_id, "created_by": who}
    if (description or "").strip():
        row["description"] = description.strip()
    new_id = w.insert("concept_domain", row)
    return f"domain {new_id} added: {name} (ordinal {ordinal})"


def set_deleted(w, id_: int, deleted: int, run_id: str) -> str:
    """Set (1) or clear (0) the delete flag of a domain."""
    if deleted not in (0, 1):
        raise EditError("-Deleted is 0 or 1")
    row = _row(w.conn, "concept_domain", id_)
    if row["deleted"] == deleted:
        raise EditError(f"domain {id_} ({row['name']}) already has deleted={deleted}")
    if deleted:
        held = [f"{r['id']} {r['name']}" for r in _cur(w.conn).execute(
            "SELECT id, name FROM concept WHERE domain_id=? AND deleted=0 ORDER BY ordinal", (id_,))]
        if held:
            raise EditError(f"domain {id_} ({row['name']}) still holds {len(held)} live concept(s): "
                            + "; ".join(held) + ". What becomes of them is for the researcher to decide first")
    elif w.conn.execute("SELECT 1 FROM concept_domain WHERE name=? AND deleted=0", (row["name"],)).fetchone():
        raise EditError(f"a live domain named {row['name']!r} exists: restoring {id_} would duplicate it")
    w.update("concept_domain", {"id": id_}, {"deleted": deleted, "updated_at": _now(), "run_id": run_id})
    return f"domain {id_} {row['name']}: deleted={deleted}"
