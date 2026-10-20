"""compliance.py -- rule compliance: read at start, proved at close (escalation #2173 P2).

Researcher, chat 2026-10-20 (verbatim): *"You print the config report, but you ignore the content.
What step can I take as part of the behaviour section to ensure that you read and understood the
governance and config rules and acknowledge that you will comply with it."* An acknowledgement at
start is what already failed (governance.session_log_required_content was printed at every start
in October and no log was written), so the control is a restatement at start checked against
evidence at close:

  A  deliver   init.py prints, in full, every active governance setting, behaviour rule and
               escalation rule (deliver_lines). Method rules are delivered by area when work in
               that area starts (method_rule_lines), not all at start.
  B  restate   Claude writes the session compliance file (template() makes the skeleton): one row
               per rule id -- what the rule requires of me in this session, in my words, or
               "not engaged" with the reason. check_start(): every active id has a row, none is
               blank, none copies the rule text, the statuses are known.
  C  conflicts the acknowledgement sentence, and by id every rule in conflict or not followed.
               retired_mentions() lists rules naming a retired table, step, setting or a file that
               no longer exists; each must be named in the conflicts section.
  D  prove     check_close(): every engaged rule carries evidence, and every evidence item that can
               be checked (a file, #id vN, a commit hash) checks.

File format (markdown, parsed here): a `## Rules` table `| id | status | requires / reason |
evidence |`, a `## Acknowledgement` section, a `## Conflicts and rules not followed` section (one
`- <id>: reason` line per rule) and a `## Close dispositions` section used by session-close (one
`- <finding key> :: <disposition>` line per finding).
Rule ids: G:<governance setting key>, B:<cfg_behaviour_rule id>, E:<cfg_escalation id>.
"""

from __future__ import annotations

import datetime
import json
import pathlib
import re

from . import sessionwindow as sw

_ROW_RE = re.compile(r"^\|\s*(?P<id>[GBE]:[^|]+?)\s*\|\s*(?P<status>[^|]*?)\s*\|"
                     r"\s*(?P<req>[^|]*?)\s*\|\s*(?P<ev>[^|]*?)\s*\|\s*$")
_HIST_RE = re.compile(r"#(\d+)\s*v(\d+)")
_COMMIT_RE = re.compile(r"\b[0-9a-f]{7,40}\b")


def _today() -> str:
    return datetime.date.today().strftime("%Y%m%d")


def rules(conn) -> list[dict]:
    """Every active rule of the three sets delivered at start, in delivery order."""
    out = []
    for r in conn.execute("SELECT key, value FROM cfg_setting WHERE module='governance' AND "
                          "inactive=0 ORDER BY key"):
        try:
            text = json.loads(r[1])
        except Exception:
            text = r[1]
        out.append(dict(id=f"G:{r[0]}", key=r[0], text=str(text)))
    for r in conn.execute("SELECT id, class, rule_key, rule_text, enforcement_status FROM "
                          "cfg_behaviour_rule WHERE active=1 ORDER BY id"):
        out.append(dict(id=f"B:{r[0]}", key=f"{r[1]}.{r[2]}", text=r[3],
                        status=r[4]))
    for r in conn.execute("SELECT id, rule_key, rule_text FROM cfg_escalation WHERE active=1 "
                          "ORDER BY id"):
        out.append(dict(id=f"E:{r[0]}", key=r[1], text=r[2]))
    return out


def deliver_lines(conn) -> list[str]:
    """P2 A: the full text, from the DB, never from memory."""
    L = []
    heads = {"G": "governance settings (cfg_setting module=governance)",
             "B": "behaviour rules (cfg_behaviour_rule, active)",
             "E": "escalation rules (cfg_escalation, active)"}
    last = None
    for r in rules(conn):
        k = r["id"][0]
        if k != last:
            L += ["", f"  -- {heads[k]} --"]
            last = k
        st = f" [{r['status']}]" if r.get("status") else ""
        L.append(f"  {r['id']}  {r['key']}{st}: {r['text']}")
    return L


def method_rule_lines(conn, area: str) -> list[str]:
    """Method rules for one area (a cfg_method_rule.step prefix, e.g. 'spine', 'narrative')."""
    return [f"  M:{r[0]}  {r[1]}: {r[2]}" for r in conn.execute(
        "SELECT id, rule_key, rule_text FROM cfg_method_rule WHERE active=1 AND (step LIKE ? OR "
        "rule_key LIKE ?) ORDER BY id", (f"{area}%", f"{area}%"))]


def file_path(cfg, session_id: str, date: str | None = None) -> pathlib.Path:
    d = sw.repo_root() / cfg.required_setting("compliance.dir")
    return d / f"COMPLIANCE-{date or _today()}-{session_id[:8]}.md"


def find_file(cfg, session_id: str) -> pathlib.Path | None:
    d = sw.repo_root() / cfg.required_setting("compliance.dir")
    hits = sorted(d.glob(f"COMPLIANCE-*-{session_id[:8]}.md")) if d.is_dir() else []
    return hits[-1] if hits else None


def template(cfg, session_id: str) -> tuple[pathlib.Path, bool]:
    """The skeleton, one row per active rule id; never overwrites an existing file."""
    existing = find_file(cfg, session_id)
    if existing:
        return existing, False
    path = file_path(cfg, session_id)
    path.parent.mkdir(parents=True, exist_ok=True)
    ack = cfg.required_setting("compliance.acknowledgement")
    L = [f"# Session compliance -- {_today()} -- session {session_id}", "",
         "> Escalation #2173 P2. Written by Claude at session start, checked by "
         "`Compliance.ps1 -Action Check -Phase Start`; evidence added during the session and "
         "checked at close (`Session-Close.ps1`, SC6). One row per rule: what it requires of me "
         "in THIS session, in my own words, or `not engaged` with the reason. Never copy the rule "
         "text. The `|` character may not be used inside a cell.", "",
         "## Acknowledgement", "", f"_(write: {ack})_", "",
         "## Rules", "", "| id | status | requires / reason | evidence |", "|---|---|---|---|"]
    for r in rules(cfg.conn):
        L.append(f"| {r['id']} |  |  |  |")
    L += ["", "## Conflicts and rules not followed", "",
          "_(one line per rule: `- <id>: <the conflict, both sides named / why it is not or "
          "cannot be followed>`; every rule listed by the start check as naming a retired thing "
          "must be here)_", "", "## Close dispositions", "",
          "_(session-close: one line per finding still open: `- <finding key> :: fixed` | "
          "`:: carried OT-nn.n` / `:: carried #nnnn` | `:: no record needed: <reason>` (SC3 "
          "only) | `:: in register OT-nn.n` / `#nnnn` (SC4))_", ""]
    path.write_text("\n".join(L) + "\n", encoding="utf-8")
    return path, True


def parse(path: pathlib.Path) -> dict:
    text = path.read_text(encoding="utf-8")
    sections: dict[str, list[str]] = {}
    cur = None
    for line in text.splitlines():
        m = re.match(r"^##\s+(.*?)\s*$", line)
        if m:
            cur = m.group(1).lower()
            sections[cur] = []
            continue
        if cur:
            sections[cur].append(line)
    rows = {}
    for line in sections.get("rules", []):
        m = _ROW_RE.match(line)
        if m:
            rows[m.group("id").strip()] = dict(status=m.group("status").strip().lower(),
                                               req=m.group("req").strip(),
                                               ev=m.group("ev").strip())
    conflicts = {}
    for line in sections.get("conflicts and rules not followed", []):
        m = re.match(r"^\s*-\s*([GBE]:[^:\s]+(?::[^\s:]+)?)\s*:\s*(.+)$", line)
        if m:
            conflicts[m.group(1)] = m.group(2).strip()
    dispositions = {}
    for line in sections.get("close dispositions", []):
        m = re.match(r"^\s*-\s*(\S+)\s*::\s*(.+)$", line)
        if m:
            dispositions[m.group(1)] = m.group(2).strip()
    ack = " ".join(l.strip() for l in sections.get("acknowledgement", []) if l.strip()
                   and not l.strip().startswith("_("))
    return dict(rows=rows, conflicts=conflicts, dispositions=dispositions, ack=ack)


def _shingles(text: str, n: int) -> set[tuple]:
    w = sw.normalise(text).split()
    return {tuple(w[i:i + n]) for i in range(max(0, len(w) - n + 1))}


def copied(restatement: str, rule_text: str, n: int, share: float, min_words: int = 0) -> bool:
    """A restatement whose n-word runs mostly occur in the rule text is a copy, not a reading. A
    restatement under min_words words is not judged: a short line ("no wipe of the escalation
    table") shares most of its runs with any rule on the same subject without copying it."""
    if len(sw.normalise(restatement).split()) < min_words:
        return False
    mine = _shingles(restatement, n)
    if not mine:
        return False
    theirs = _shingles(rule_text, n)
    return len(mine & theirs) / len(mine) >= share


def retired_mentions(conn) -> dict[str, list[str]]:
    """{rule id: [retired things it names]} -- an aid for part C, never a verdict by itself."""
    from . import escalationcontext as ec
    tables = {r[0] for r in conn.execute("SELECT name FROM cfg_table WHERE inactive=1")} - \
             {r[0] for r in conn.execute("SELECT name FROM cfg_table WHERE inactive=0")}
    steps = {r[0] for r in conn.execute("SELECT step FROM cfg_step WHERE inactive=1")} - \
            {r[0] for r in conn.execute("SELECT step FROM cfg_step WHERE inactive=0")}
    settings = {r[0] for r in conn.execute("SELECT key FROM cfg_setting WHERE inactive=1")} - \
               {r[0] for r in conn.execute("SELECT key FROM cfg_setting WHERE inactive=0")}
    root = sw.repo_root()
    out: dict[str, list[str]] = {}
    word = lambda t: re.compile(r"(?<![\w.])" + re.escape(t) + r"(?![\w])")
    # a plain English word ('finding', 'books', 'sources') counts only when written as code
    code = lambda t: re.compile(r"`" + re.escape(t) + r"`")
    path_rx = re.compile(r"(?<![\w/.-])((?:\.?[\w-]+/)+[\w.*-]+\.(?:md|py|ps1|json|xlsx|csv))\b")
    for r in rules(conn):
        hits = [f"table {t}" for t in tables
                if (word(t) if "_" in t else code(t)).search(r["text"])]
        hits += [f"step {s}" for s in steps if word(s).search(r["text"])]
        hits += [f"setting {s}" for s in settings if word(s).search(r["text"])]
        for p in path_rx.findall(r["text"]):
            p = p[2:] if p.startswith("./") else p
            if "*" not in p and "..." not in p and not (root / p).exists():
                hits.append(f"file {p} (not on disk)")
        if hits:
            out[r["id"]] = sorted(set(hits))
    return out


def check_start(cfg, path: pathlib.Path) -> list[dict]:
    """Part B and C findings: [{key, reason}]."""
    conn = cfg.conn
    f = parse(path)
    n = int(cfg.required_setting("compliance.copy_shingle_words"))
    share = float(cfg.required_setting("compliance.copy_share_max"))
    min_words = int(cfg.required_setting("compliance.copy_min_words"))
    statuses = set(cfg.enum("compliance_rule_status"))
    ack = cfg.required_setting("compliance.acknowledgement")
    F = []
    if sw.normalise(ack) not in sw.normalise(f["ack"]):
        F.append(dict(key="ack", reason="the acknowledgement sentence is missing or altered"))
    live = {r["id"]: r for r in rules(conn)}
    for rid, r in live.items():
        row = f["rows"].get(rid)
        if row is None:
            F.append(dict(key=rid, reason="no row for this active rule"))
            continue
        if row["status"] not in statuses:
            F.append(dict(key=rid, reason=f"status {row['status']!r} is not one of "
                                          f"{sorted(statuses)}"))
        if not row["req"]:
            F.append(dict(key=rid, reason="blank: neither what it requires nor why it is not "
                                          "engaged"))
        elif copied(row["req"], r["text"], n, share, min_words):
            F.append(dict(key=rid, reason="the restatement copies the rule text (a copy is not a "
                                          "reading)"))
    for rid in f["rows"]:
        if rid not in live:
            F.append(dict(key=rid, reason="row for a rule that is not active (retired or unknown)"))
    for rid, hits in retired_mentions(conn).items():
        if rid not in f["conflicts"]:
            F.append(dict(key=rid, reason="names retired things (" + "; ".join(hits[:3])
                                          + ") and is not named in the conflicts section"))
    return F


def check_evidence(text: str, conn, root: pathlib.Path, since: str | None) -> list[str]:
    """Problems with the checkable items in one evidence cell."""
    from . import escalationcontext as ec
    bad = []
    for raw in ec.extract_paths(text, [".md", ".py", ".ps1", ".json", ".xlsx", ".csv", ".txt"]):
        p = raw.replace("\\", "/")
        p = p[2:] if p.startswith("./") else p
        words = p.split(" ")     # a cell may run prose into a path: try each suffix
        if "/" in p and not any((root / " ".join(words[i:])).exists() for i in range(len(words))):
            bad.append(f"file {p} does not exist")
    for m in _HIST_RE.finditer(text):
        row = conn.execute("SELECT COALESCE(answered_at, raised_at) FROM escalation_history WHERE "
                           "escalation_id=? AND version=?", (int(m.group(1)), int(m.group(2)))
                           ).fetchone()
        if not row:
            bad.append(f"#{m.group(1)} v{m.group(2)} does not exist")
        elif since and row[0] and row[0] < since:
            bad.append(f"#{m.group(1)} v{m.group(2)} was written before this session")
    stripped = _HIST_RE.sub(" ", text)
    for raw in ec.extract_paths(text, [".md", ".py", ".ps1", ".json", ".xlsx", ".csv", ".txt"]):
        stripped = stripped.replace(raw, " ")      # hex inside a file name is not a commit
    for h in _COMMIT_RE.findall(stripped):
        if any(c.isalpha() for c in h) and not sw.commit_exists(h):
            bad.append(f"commit {h} does not exist")
    return bad


def check_close(cfg, path: pathlib.Path, since: str | None) -> list[dict]:
    """Part D findings: [{key, reason}]."""
    f = parse(path)
    root = sw.repo_root()
    F = []
    engaged = set(cfg.required_setting("compliance.engaged_statuses"))
    for rid, row in f["rows"].items():
        if row["status"] not in engaged:
            continue
        if not row["ev"]:
            F.append(dict(key=rid, reason="engaged, with no evidence"))
            continue
        for b in check_evidence(row["ev"], cfg.conn, root, since):
            F.append(dict(key=rid, reason=f"evidence does not check: {b}"))
    return F
