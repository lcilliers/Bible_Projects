"""valuequality.py — the generic column-level VALUE-QUALITY engine.

Every validate step in this app checked STRUCTURE (a row exists, an FK resolves, a column is
not-null, a dedup key holds) but nothing checked that a column's actual VALUE serves what it is
declared for (`cfg_column.use`). Found 2026-07-21 via `candidate_seed.tag` (dirty IB labels
carrying raw dictionary glosses) and confirmed to repeat across `lemma_inventory.gloss`,
`strong_sense.head`, `word_registry.word`, `span.surface` — one systemic gap, not several.

This closes GOVERNANCE.md §6's named-but-unbuilt "V8" increment for real: `cfg_column.expectation`
now drives a genuine value-quality scan, not just FK/enum documentation. Three recognised forms:

    notblank        value is not NULL and not empty/whitespace after trim
    nohtml          value contains no '<' character (catches leftover markup / an unsplit tree)
    pattern:<key>   value matches the regex stored at cfg_setting <key> (reuses an existing
                    setting, e.g. candidate.tag_clean_pattern — never forks a parallel constant)

One column, one rule, one scan — added by setting `cfg_column.expectation`, nothing else. A new
column with the same kind of expectation is checked automatically, the same way `validation.py`'s
`_integrity`/`_references` already generalise notnull/FK checks from `cfg_column`.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field


@dataclass
class ValueFinding:
    table: str
    column: str
    rule: str
    total: int          # rows considered (non-null, where relevant)
    violations: int
    samples: list = field(default_factory=list)   # EVERY distinct violating (value, count) or bare
                                                    # value, most-frequent first — NOT capped. A
                                                    # persisted report is the actual review artifact
                                                    # (per the researcher's 2026-07-21 point: "the
                                                    # only way I can review it is to be exposed to
                                                    # the data" — a top-10 sample is not that).
                                                    # Truncate only at the point of DISPLAY (e.g. an
                                                    # escalation's inline prompt text), never here.


def _has_deleted(cfg, table: str) -> bool:
    return "deleted" in cfg.column_names(table)


def _where_live(cfg, table: str) -> str:
    return "WHERE deleted=0" if _has_deleted(cfg, table) else ""


def _scope(live: str, extra_where: str) -> str:
    """Combine the standard deleted=0 live-filter with an optional caller-supplied scope
    clause (e.g. restricting to one word's strongs, or one book's verses)."""
    parts = [p for p in (live.replace("WHERE ", "", 1), extra_where) if p]
    return ("WHERE " + " AND ".join(parts)) if parts else ""


def _scan_notblank(cfg, table: str, column: str, extra_where: str = "", params: tuple = ()) -> ValueFinding:
    where = _scope(_where_live(cfg, table), extra_where)
    total = cfg.conn.execute(f'SELECT COUNT(*) FROM "{table}" {where}', params).fetchone()[0]
    cond = f'"{column}" IS NULL OR trim("{column}")=\'\''
    where2 = _scope(_where_live(cfg, table), f"({cond})" + (f" AND {extra_where}" if extra_where else ""))
    n = cfg.conn.execute(f'SELECT COUNT(*) FROM "{table}" {where2}', params).fetchone()[0]
    return ValueFinding(table, column, "notblank", total, n, [])


def _scan_nohtml(cfg, table: str, column: str, extra_where: str = "", params: tuple = ()) -> ValueFinding:
    where = _scope(_where_live(cfg, table), extra_where)
    total = cfg.conn.execute(f'SELECT COUNT(*) FROM "{table}" {where}', params).fetchone()[0]
    cond = f'"{column}" LIKE \'%<%\'' + (f" AND {extra_where}" if extra_where else "")
    where2 = _scope(_where_live(cfg, table), cond)
    rows = cfg.conn.execute(f'SELECT "{column}" FROM "{table}" {where2}', params).fetchall()
    samples = [(r[0] or "")[:200] for r in rows]   # every violating value, not just the first 10
    return ValueFinding(table, column, "nohtml", total, len(rows), samples)


def _scan_pattern(cfg, table: str, column: str, setting_key: str,
                  extra_where: str = "", params: tuple = ()) -> ValueFinding:
    pattern = re.compile(cfg.setting(setting_key, r"^[A-Za-z][A-Za-z' -]*$"))
    cond = f'"{column}" IS NOT NULL' + (f" AND {extra_where}" if extra_where else "")
    where = _scope(_where_live(cfg, table), cond)
    total = cfg.conn.execute(f'SELECT COUNT(*) FROM "{table}" {where}', params).fetchone()[0]
    rows = cfg.conn.execute(
        f'SELECT "{column}" v, COUNT(*) n FROM "{table}" {where} GROUP BY "{column}"', params).fetchall()
    messy = [(r["v"], r["n"]) for r in rows if not pattern.match(r["v"] or "")]
    violations = sum(n for _, n in messy)
    samples = sorted(messy, key=lambda t: -t[1])   # every distinct violating value, not just top 10
    return ValueFinding(table, column, f"pattern:{setting_key}", total, violations, samples)


def scan_column(cfg, table: str, column: str, expectation: str,
                extra_where: str = "", params: tuple = ()) -> ValueFinding | None:
    """Scan ONE column against a given expectation string, optionally scoped (e.g. to one word's
    rows or one book's verses) — the piece validation.py's per-word/per-book reports reuse so a
    reviewer sees value-quality findings scoped to what they're actually looking at, not just the
    whole-table picture in candidate-quality.md."""
    if expectation == "notblank":
        return _scan_notblank(cfg, table, column, extra_where, params)
    if expectation == "nohtml":
        return _scan_nohtml(cfg, table, column, extra_where, params)
    if expectation.startswith("pattern:"):
        return _scan_pattern(cfg, table, column, expectation[len("pattern:"):], extra_where, params)
    return None    # enum.* — structural, see find_enum_violations


def find_value_quality_findings(cfg) -> list[ValueFinding]:
    """Every cfg_column row with a non-null expectation matching notblank/nohtml/pattern:*,
    scanned whole-table against the live data. Skips enum.* (handled separately, structurally, in
    handlers/configmaint.py — a coherence check, not a value-quality judgement call)."""
    out: list[ValueFinding] = []
    for r in cfg.conn.execute(
            "SELECT table_name, name, expectation FROM cfg_column WHERE expectation IS NOT NULL"):
        f = scan_column(cfg, r["table_name"], r["name"], r["expectation"])
        if f:
            out.append(f)
    return out


def find_enum_violations(conn) -> list[str]:
    """Every cfg_column row whose expectation is enum.<name>: confirm every live value in that
    column is a member of the declared cfg_enum set. A STRUCTURAL coherence check (like the FK/PK
    checks already in configmaint.py's _validate_live), not a researcher judgement call — an
    enum violation is a hard fault, always report-stop, never escalated.

    Found 2026-07-21: candidate_seed.decision/.layer already declared enum.candidate_decision/
    enum.candidate_source in cfg_column, but nothing ever checked live values against them —
    confirmed by grep, the enums are referenced nowhere in the app's code. Clean today by luck
    (2,013 candidate/73 rejected, no stray values), not by anything enforced."""
    out: list[str] = []
    for r in conn.execute(
            "SELECT table_name, name, expectation FROM cfg_column "
            "WHERE expectation LIKE 'enum.%'"):
        table, column, enum_name = r["table_name"], r["name"], r["expectation"][len("enum."):]
        valid = {v[0] for v in conn.execute(
            "SELECT value FROM cfg_enum WHERE name=?", (enum_name,))}
        if not valid:
            out.append(f"value-quality: {table}.{column} declares expectation enum.{enum_name!r} "
                       f"but that enum has no members in cfg_enum")
            continue
        live = "WHERE deleted=0" if conn.execute(
            "SELECT 1 FROM pragma_table_info(?) WHERE name='deleted'", (table,)).fetchone() else ""
        rows = conn.execute(f'SELECT DISTINCT "{column}" v FROM "{table}" {live}').fetchall()
        bad = sorted({r2["v"] for r2 in rows if r2["v"] is not None and r2["v"] not in valid})
        if bad:
            out.append(f"value-quality: {table}.{column} has value(s) outside enum.{enum_name} "
                       f"{sorted(valid)}: {bad}")
    return out
