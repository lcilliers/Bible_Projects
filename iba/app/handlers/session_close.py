"""session_close.py -- session-close detection (escalation #1875; rebuilt 2026-10-20, escalation
#2173, session-close change proposal v1 SC1-SC14).

What session-close is for: to end a session so that nothing done, decided or left open in it exists
only in the chat or in an unrecorded file, and so that the base data and the narrative are sound.
The old checks compared records with records (the CLI's own write confirmations against
escalation_history, C1), listed files instead of checking them (C2), were cleared by any BUILD.md
edit (C3) and passed when the git window was missing (C4). This handler now checks the work
against its record. Detection only: it never writes a fix (remediation is Claude's, in
.claude/commands/session-close.md). Every finding has a stable key; it is cleared only by being
fixed (it no longer appears) or by a disposition in the session compliance file's
`## Close dispositions` section that names an open item carrying it (checked here).

  SC1  session and window   no session id or no boundary record FAILS the close (C4)
  SC2  spine                handlers/spine.compute: span->strong, verse<->span, strong->cluster,
                            strong->meaning vs STEP. FATAL findings come first.
  SC3  researcher's words   every researcher message in the transcript must appear (normalised)
                            in an escalation_history comment written in the window, or be
                            dispositioned (`recorded in #n vN` / `no record needed: reason`).
                            Session-start command names (session_close.no_record_messages) need
                            none.
  SC4  open items           (a) every line of an `Open items` section in a file changed in the
                            window names an OT-nn[.n] or #nnnn that exists and is still open;
                            (b) researcher messages with a holding word (session_close.held_words)
                            need `in register OT-nn.n|#nnnn` or `not held: reason`.
  SC5  analysis integrity   (a) every chapter file changed is a chapter's current file and a
                            narrative_update was recorded in the window; (b) the quote check on
                            the lines each changed chapter added against its previous version;
                            (c) register check: a finding new since the previous session's close,
                            and a standing finding on a chapter changed now (rule 77 as amended,
                            #2152), are findings; (d) every verse a changed reading file names has
                            its placement row and a `told` verse is told (behaviour rule
                            reading-file-placement-per-verse).
  SC6  rule compliance      compliance.check_close on the session compliance file.
  SC8  session log          a log for this session in governance.session_log_dir, naming the
                            session id, with the six required sections.
  SC9  decisions' targets   every line of the log's decisions section names a target that changed
                            in the window (a changed file, a cfg_* table with a cfg_change_detail
                            row in the window, or #nnnn vN written in the window).
  SC10 BUILD.md coverage    every code/config file changed (session_close.build_scope) is NAMED
                            in the lines BUILD.md gained in the window (C3).
  SC12 publish              whether the narrative copy (a chapter changed) and the threads export
                            (a thread row changed, or the register file differs from the table --
                            it embeds rule text) are needed; each runs only then.
  SC15 control files        every file of the control-map kinds in session_close.control_kinds
                            (cfgquality.find_control_file_problems, #2186): it exists; every path it
                            names resolves and is not in an archive/ unless the line marks it as
                            history; no replaced-history text (rule 96); an always-read file within
                            session_close.always_read_max_bytes.
SC7 (remediation), SC11 (re-run) and SC13 (commit, blocked while any finding is open) are steps of
the command; Session-Close.ps1 exits 3 while any finding is open. SC14: this report is the close's
persisted record.
"""

from __future__ import annotations

import datetime
import fnmatch
import hashlib
import json
import pathlib
import re

from .base import Ctx, Outcome, ok, fail
from . import spine as spine_mod
from ..lib import (cfgquality, compliance, escalation as esc, narrativeregister as nr, quotecheck,
                   reportkit, sessionwindow as sw)

_HANDLE_RX = re.compile(r"\bOT-(\d+)(?:\.(\d+))?\b|#(\d+)\b")
_HIST_RX = re.compile(r"#(\d+)\s*v(\d+)")


def _now() -> str:
    return datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _h(*parts: str) -> str:
    return hashlib.sha1("|".join(parts).encode("utf-8")).hexdigest()[:8]


class _Handles:
    """Resolve OT-nn / OT-nn.n / #nnnn against the escalation and thread item tables."""

    def __init__(self, db):
        self.db = db
        self.live = set(esc.live_states(db))
        self.state = {r["id"]: r["state"] for r in db.rows("SELECT id, state FROM escalation")}
        self.alias = {}
        for r in db.rows("SELECT id, alias, state FROM escalation WHERE alias IS NOT NULL"):
            self.alias[self._norm_alias(r["alias"])] = (r["id"], r["state"])
        self.items = {}
        for r in db.rows("SELECT e.alias, i.item_no, i.status FROM escalation_thread_item i JOIN "
                         "escalation e ON e.id=i.escalation_id"):
            self.items[f"{self._norm_alias(r['alias'])}.{r['item_no']}"] = r["status"]

    @staticmethod
    def _norm_alias(a: str) -> str:
        m = re.match(r"OT-0*(\d+)", a or "")
        return f"OT-{int(m.group(1))}" if m else a

    def check(self, text: str) -> tuple[list[str], list[str]]:
        """(open handles, problems) for every handle named in text."""
        good, bad = [], []
        for m in _HANDLE_RX.finditer(text or ""):
            if m.group(3):
                eid = int(m.group(3))
                st = self.state.get(eid)
                if st is None:
                    bad.append(f"#{eid} does not exist")
                elif st not in self.live:
                    bad.append(f"#{eid} is {st}")
                else:
                    good.append(f"#{eid}")
                continue
            alias = f"OT-{int(m.group(1))}"
            if m.group(2):
                st = self.items.get(f"{alias}.{m.group(2)}")
                if st is None:
                    bad.append(f"{alias}.{m.group(2)} does not exist")
                elif st != "open":
                    bad.append(f"{alias}.{m.group(2)} is {st}")
                else:
                    good.append(f"{alias}.{m.group(2)}")
            else:
                a = self.alias.get(alias)
                if a is None:
                    bad.append(f"{alias} does not exist")
                elif a[1] not in self.live:
                    bad.append(f"{alias} is {a[1]}")
                else:
                    good.append(alias)
        return good, bad


def _sections(text: str, heading_rx: re.Pattern) -> list[tuple[int, list[tuple[int, str]]]]:
    """[(heading line no, [(line no, line)])] for every heading matching heading_rx."""
    out, cur, level = [], None, 0
    for i, line in enumerate(text.splitlines(), 1):
        m = re.match(r"^(#{1,6})\s+(.*)$", line)
        if m:
            if cur is not None and len(m.group(1)) <= level:
                cur = None
            if heading_rx.search(m.group(2)):
                cur, level = [], len(m.group(1))
                out.append((i, cur))
            continue
        if cur is not None:
            cur.append((i, line))
    return out


def _bullets(lines: list[tuple[int, str]]) -> list[tuple[int, str]]:
    """Each bullet with its wrapped continuation lines joined (an indented, non-bullet line that
    follows a bullet belongs to it)."""
    out: list[list] = []
    cur = None
    for n, l in lines:
        if re.match(r"^\s*(?:[-*+]|\d+[.)])\s+\S", l):
            cur = [n, l.strip()]
            out.append(cur)
        elif cur is not None and l.strip() and l.startswith((" ", "\t")):
            cur[1] += " " + l.strip()
        elif l.strip():
            cur = None                     # a plain paragraph ends the bullet
    return [(n, t) for n, t in out if not t.startswith("_(")]


# ── the checks ───────────────────────────────────────────────────────────────────────────────
def _sc3_sc4b(cfg, db, messages, since) -> tuple[list[dict], list[dict]]:
    comments = " ".join(sw.normalise(r["comment"] or "") for r in db.rows(
        "SELECT comment FROM escalation_history WHERE COALESCE(answered_at, raised_at) >= ?",
        (since,)))
    no_record = [sw.normalise(x) for x in cfg.required_setting("session_close.no_record_messages")]
    held_rx = re.compile(r"\b(" + "|".join(re.escape(w) for w in
                                           cfg.required_setting("session_close.held_words"))
                         + r")\b", re.IGNORECASE)
    min_words = int(cfg.required_setting("session_close.message_min_words"))
    padded = f" {comments} "
    f3, f4 = [], []
    for m in messages:
        n = sw.normalise(m["text"])
        if not n or any(n == x or n.startswith(x + " ") and len(n) <= len(x) + 12 for x in no_record):
            continue
        key = m["uuid"][:8]
        # a short message ("proceed", "yes") is found inside almost any comment, which proves
        # nothing: it always needs its disposition (recorded in #n vN / no record needed: ...)
        if len(n.split()) < min_words or f" {n} " not in padded:
            f3.append(dict(key=f"SC3:{key}", step="SC3",
                           text=(f"researcher message {m['at'][:16]} is too short to be matched; "
                                 f"name where it is recorded: " if len(n.split()) < min_words else
                                 f"researcher message {m['at'][:16]} is in no escalation comment "
                                 f"written this session: ") + f"\"{m['text'][:160]}\""))
        if held_rx.search(m["text"]):
            f4.append(dict(key=f"SC4b:{key}", step="SC4",
                           text=f"researcher message {m['at'][:16]} holds, defers or asks to "
                                f"check something; name its register item: \"{m['text'][:160]}\""))
    return f3, f4


def _sc4a(cfg, root, changed, handles) -> list[dict]:
    F = []
    rx = re.compile(r"\bopen items\b", re.IGNORECASE)
    skip = cfg.required_setting("session_close.open_items_exclude")   # generated reports
    for rel in changed:
        p = root / rel
        if p.suffix.lower() != ".md" or not p.is_file() or "/archive/" in f"/{rel}" \
                or any(fnmatch.fnmatch(rel, g) for g in skip):
            continue
        try:
            text = p.read_text(encoding="utf-8")
        except Exception:
            continue
        for _, lines in _sections(text, rx):
            for n, line in _bullets(lines):
                good, bad = handles.check(line)
                if bad or not good:
                    F.append(dict(key=f"SC4a:{_h(rel, line)}", step="SC4",
                                  text=f"`{rel}` line {n}: open item "
                                       + ("names no OT-nn.n or #nnnn" if not (good or bad)
                                          else "; ".join(bad))
                                       + f": \"{line[:140]}\""))
    return F


def _chapter_changes(cfg, root, changed) -> list[str]:
    cdir = nr.chapter_dir(cfg)
    try:
        crel = cdir.resolve().relative_to(root).as_posix()
    except ValueError:
        crel = str(cdir).replace("\\", "/")
    return [rel for rel in changed if rel.startswith(crel + "/") and rel.count("/") == crel.count("/") + 1
            and rel.endswith(".md") and (root / rel).is_file()]


def _previous_version(path: pathlib.Path) -> pathlib.Path | None:
    fv = nr.file_version(path.name)
    if not fv:
        return None
    stem, n = fv
    best = None
    for d in (path.parent, path.parent / "archive"):
        for f in d.glob(f"{stem}-v*.md") if d.is_dir() else []:
            v = nr.file_version(f.name)
            if v and v[0] == stem and v[1] < n and (best is None or v[1] > best[0]):
                best = (v[1], f)
    return best[1] if best else None


def _sc5(cfg, db, root, changed, since, base, state) -> tuple[list[dict], dict]:
    conn = db.conn
    F, info = [], {}
    chapters = _chapter_changes(cfg, root, changed)
    info["chapters_changed"] = chapters
    current = {r["current_file"]: r for r in db.rows(
        "SELECT * FROM narrative_chapter WHERE inactive=0 AND current_file IS NOT NULL")}
    updates = db.rows("SELECT id FROM narrative_update WHERE created_at >= ?", (since,))
    # (a)
    for rel in chapters:
        name = pathlib.PurePosixPath(rel).name
        if name not in current:
            F.append(dict(key=f"SC5a:{name}", step="SC5",
                          text=f"chapter file `{name}` changed but is no chapter's current file in "
                               f"the register (record the weave: Narrative-Register.ps1 -Action "
                               f"Record)"))
        elif not updates:
            F.append(dict(key=f"SC5a:{name}", step="SC5",
                          text=f"chapter file `{name}` changed and no narrative_update was "
                               f"recorded this session"))
    # (b)
    if chapters:
        corpus = quotecheck.Corpus(conn)
        skip = quotecheck.titles(conn)
        mw = int(cfg.required_setting("narrative.quote_min_words"))
        n_parts = 0
        for rel in chapters:
            p = root / rel
            prev = _previous_version(p)
            old = prev.read_text(encoding="utf-8") if prev else sw.file_at(base, rel) if base else None
            n, bad = quotecheck.check_lines(corpus, quotecheck.added_lines(old, p.read_text(
                encoding="utf-8")), mw, skip)
            n_parts += n
            for b in bad:
                F.append(dict(key=f"SC5b:{_h(rel, b)}", step="SC5",
                              text=f"`{p.name}`: quotation not found in the ESV text: \"{b[:150]}\""))
        info["quote_parts"] = n_parts
    # (c)
    lines, _ = nr.check(cfg, {})
    problems = [l[2:] for l in lines if l.startswith("- ")]
    baseline = set(state.get("baseline") or [])
    info["register_findings"] = len(problems)
    changed_ch = {current[pathlib.PurePosixPath(r).name]["id"] for r in chapters
                  if pathlib.PurePosixPath(r).name in current}
    ch_no = {r["id"]: r["chapter_no"] for r in db.rows("SELECT id, chapter_no FROM narrative_chapter")}
    claim_ch = {r["claim_ref"]: r["main_chapter_id"] for r in db.rows(
        "SELECT claim_ref, main_chapter_id FROM narrative_claim")}
    for pr in problems:
        if state.get("have_baseline") and pr not in baseline:
            F.append(dict(key=f"SC5c:new:{_h(pr)}", step="SC5",
                          text=f"register check, new since the previous close: {pr}"))
            continue
        m = re.match(r"claim (\S+) is current but no current passage tells it", pr)
        cid = claim_ch.get(m.group(1)) if m else None
        m2 = re.match(r"Ch (\S+):", pr)
        touched = (cid in changed_ch) or (m2 and any(ch_no.get(c) == m2.group(1) for c in changed_ch))
        if touched:
            F.append(dict(key=f"SC5c:standing:{_h(pr)}", step="SC5",
                          text=f"register check, standing finding on a chapter changed this "
                               f"session (reconcile under rule 77): {pr}"))
    info["register_problems"] = problems
    # (d)
    F += _sc5d(cfg, db, root, changed)
    return F, info


def _sc5d(cfg, db, root, changed) -> list[dict]:
    F = []
    pats = cfg.required_setting("session_close.reading_scope")
    name_rx = re.compile(cfg.required_setting("session_close.reading_file_pattern"), re.IGNORECASE)
    allowed = cfg.required_setting("session_close.placement_kinds")
    vx = nr.VerseIndex(cfg)
    told = {r[0] for r in db.conn.execute(
        "SELECT nc.verse_id FROM narrative_citation nc JOIN narrative_chapter ch ON "
        "ch.id=nc.chapter_id AND ch.inactive=0 WHERE nc.last_version IS NULL AND nc.verse_id IS NOT NULL")}
    handles = _Handles(db)
    for rel in changed:
        p = root / rel
        if not p.is_file() or "/archive/" in f"/{rel}" or not any(fnmatch.fnmatch(rel, g) for g in pats):
            continue
        if p.suffix.lower() not in (".md", ".csv") or not name_rx.search(p.name):
            continue
        text = p.read_text(encoding="utf-8", errors="replace")
        named, placed = {}, {}
        if p.suffix.lower() == ".csv":
            import csv
            rows = list(csv.DictReader(text.splitlines()))
            cols = {c.lower(): c for c in (rows[0].keys() if rows else [])}
            if rows and ("placement" not in cols or "reference" not in cols):
                F.append(dict(key=f"SC5d:{_h(rel)}", step="SC5",
                              text=f"`{rel}`: a reading CSV needs `reference` and `placement` columns"))
                continue
            for r in rows:
                for ref in nr.parse_refs(r[cols["reference"]] or "", vx):
                    if ref.verse_id:
                        named[ref.verse_id] = ref.normalised
                        placed[ref.verse_id] = (r[cols["placement"]] or "").strip()
        else:
            secs = _sections(text, re.compile(r"^placements?\b", re.IGNORECASE))
            in_table = set()
            for _, lines in secs:
                for n, line in lines:
                    m = re.match(r"^\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|", line)
                    if not m or set(m.group(1)) <= set("-: "):
                        continue
                    for ref in nr.parse_refs(m.group(1), vx):
                        if ref.verse_id:
                            placed[ref.verse_id] = m.group(2).strip()
                            in_table.add(n)
            for ref in nr.parse_refs(text, vx):
                if ref.verse_id:
                    named.setdefault(ref.verse_id, ref.normalised)
        for vid, refn in named.items():
            pl = placed.get(vid)
            if not pl:
                F.append(dict(key=f"SC5d:{_h(rel, refn)}", step="SC5",
                              text=f"`{rel}`: {refn} is named but has no placement row"))
                continue
            kind = pl.split()[0].lower().rstrip(":,") if pl.split() else ""
            if kind not in allowed:
                F.append(dict(key=f"SC5d:{_h(rel, refn)}", step="SC5",
                              text=f"`{rel}`: {refn} placement {pl!r} is not one of {allowed}"))
            elif kind == "told" and vid not in told:
                F.append(dict(key=f"SC5d:{_h(rel, refn)}", step="SC5",
                              text=f"`{rel}`: {refn} is placed `told` but no current chapter tells it"))
            elif kind in ("forward", "held"):
                good, bad = handles.check(pl)
                if bad or not good:
                    F.append(dict(key=f"SC5d:{_h(rel, refn)}", step="SC5",
                                  text=f"`{rel}`: {refn} placement {pl!r}: "
                                       + ("; ".join(bad) or "names no open OT-nn.n or #nnnn")))
    return F


def _sc8_sc9(cfg, db, root, session_id, changed, since) -> tuple[list[dict], pathlib.Path | None]:
    F = []
    ldir = root / cfg.required_setting("governance.session_log_dir")
    log = None
    for p in sorted(ldir.glob("SESSION-LOG-*.md"), key=lambda x: x.stat().st_mtime, reverse=True):
        try:
            if session_id in p.read_text(encoding="utf-8", errors="replace"):
                log = p
                break
        except Exception:
            continue
    if log is None:
        F.append(dict(key="SC8:log", step="SC8",
                      text=f"no session log in {ldir.relative_to(root).as_posix()}/ names this "
                           f"session ({session_id}); write it (governance.session_log_required_content)"))
        return F, None
    text = log.read_text(encoding="utf-8")
    heads = cfg.required_setting("session_close.log_sections")
    for i, h in enumerate(heads, 1):
        secs = _sections(text, re.compile(r"^" + re.escape(h), re.IGNORECASE))
        if not secs:
            F.append(dict(key=f"SC8:section{i}", step="SC8",
                          text=f"`{log.name}`: no section headed '{h}'"))
        elif i < len(heads) and not any(l.strip() for _, l in secs[0][1]):
            F.append(dict(key=f"SC8:section{i}", step="SC8",
                          text=f"`{log.name}`: section '{h}' is empty"))
    # SC9
    dsecs = _sections(text, re.compile(r"^" + re.escape(heads[3]), re.IGNORECASE))
    cfg_tables = {r[0] for r in db.rows("SELECT DISTINCT table_name FROM cfg_change_detail WHERE "
                                         "applied_at >= ?", (since,))}
    changed_set = set(changed)
    for n, line in _bullets(dsecs[0][1] if dsecs else []):
        ok_target, problems = False, []
        from ..lib import escalationcontext as ec
        for raw in ec.extract_paths(line, [".md", ".py", ".ps1", ".json", ".csv", ".xlsx"]):
            p = raw.replace("\\", "/").strip("`")
            hit = [c for c in changed_set if c == p or c.endswith("/" + p) or c.endswith(p)]
            if hit:
                ok_target = True
            else:
                problems.append(f"{p} did not change this session")
        for t in re.findall(r"\bcfg_[a-z_]+\b", line):
            if t in cfg_tables:
                ok_target = True
            elif t != "cfg_change_detail":
                problems.append(f"{t}: no cfg_change_detail row this session")
        for m in _HIST_RX.finditer(line):
            row = db.rows("SELECT COALESCE(answered_at, raised_at) at FROM escalation_history WHERE "
                          "escalation_id=? AND version=?", (int(m.group(1)), int(m.group(2))))
            if row and (row[0]["at"] or "") >= since:
                ok_target = True
            else:
                problems.append(f"#{m.group(1)} v{m.group(2)} was not written this session")
        if not ok_target:
            F.append(dict(key=f"SC9:{_h(line)}", step="SC9",
                          text=f"`{log.name}` decision line {n} names no target that changed this "
                               f"session" + (f" ({'; '.join(problems)})" if problems else
                                             " (name a file, a cfg_* table or #nnnn vN)")
                               + f": \"{line[:140]}\""))
    return F, log


def _sc10(cfg, base, changed) -> list[dict]:
    globs = cfg.required_setting("session_close.build_scope")
    excl = cfg.required_setting("session_close.build_scope_exclude")
    code = [c for c in changed if any(fnmatch.fnmatch(c, g) for g in globs)
            and not any(fnmatch.fnmatch(c, g) for g in excl)]
    if not code:
        return []
    added = sw.diff_added_text(base, "iba/app/BUILD.md") if base else ""
    F = []
    for c in code:
        short = c[len("iba/app/"):] if c.startswith("iba/app/") else c
        if c not in added and short not in added:
            F.append(dict(key=f"SC10:{c}", step="SC10",
                          text=f"`{c}` changed this session and is not named in what BUILD.md "
                               f"gained this session"))
    return F


def _sc12(cfg, db, root, changed, since) -> dict:
    chapters = _chapter_changes(cfg, root, changed)
    thread_rows = db.rows(
        "SELECT COUNT(*) n FROM escalation_history h JOIN escalation e ON e.id=h.escalation_id "
        "WHERE e.type='thread' AND COALESCE(h.answered_at, h.raised_at) >= ?", (since,))[0]["n"]
    responses = db.rows("SELECT COUNT(*) n FROM escalation_thread_item_response WHERE "
                        "responded_at >= ?", (since,))[0]["n"]
    # the register also embeds rule text (cfg_behaviour_rule 74): export whenever the file on disk
    # differs from what Export would write now, not only when a thread row changed
    reg = pathlib.Path(cfg.required_setting("escalation.thread_register_path"))
    L, _ = esc.render_thread_register(cfg, db)
    stale = not reg.is_file() or reg.read_text(encoding="utf-8") != "\n".join(L) + "\n"
    return dict(narrative_copy=bool(chapters), thread_export=bool(thread_rows or responses or stale))


# ── dispositions ─────────────────────────────────────────────────────────────────────────────
def _apply_dispositions(F, disp, handles, db, since) -> None:
    """Mark each finding cleared / carried with the reason, in place."""
    for f in F:
        d = (disp.get(f["key"]) or "").strip()
        f["disposition"] = d
        f["cleared"] = False
        if not d:
            continue
        low = d.lower()
        if low.startswith("carried") or low.startswith("in register"):
            if f["step"] == "SC2" and low.startswith("in register"):
                f["note"] = "a spine finding is fixed or carried, not 'in register'"
                continue
            good, bad = handles.check(d)
            if good and not bad:
                f["cleared"] = True
            else:
                f["note"] = "; ".join(bad) or "names no open OT-nn.n or #nnnn"
        elif low.startswith("recorded in") and f["step"] == "SC3":
            m = _HIST_RX.search(d)
            row = db.rows("SELECT COALESCE(answered_at, raised_at) at FROM escalation_history WHERE "
                          "escalation_id=? AND version=?", (int(m.group(1)), int(m.group(2)))) if m else []
            if row and (row[0]["at"] or "") >= since:
                f["cleared"] = True
            else:
                f["note"] = "the named #n vN does not exist or was not written this session"
        elif (low.startswith("no record needed:") and f["step"] == "SC3") or \
                (low.startswith("not held:") and f["step"] == "SC4" and f["key"].startswith("SC4b")) or \
                (low.startswith("not scripture:") and f["key"].startswith("SC5b")):
            if len(d.split(":", 1)[1].strip()) >= 8:
                f["cleared"] = True
            else:
                f["note"] = "the reason is missing"
        elif low.startswith("fixed"):
            f["note"] = "marked fixed, but the check still finds it"
        else:
            f["note"] = "not a disposition this finding accepts"


# ── state between closes (SC5c baseline) ─────────────────────────────────────────────────────
def _load_state(cfg, session_id) -> dict:
    path = sw.repo_root() / cfg.required_setting("session_close.state_path")
    try:
        s = json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return dict(have_baseline=False, baseline=[])
    if s.get("session_id") == session_id:
        return dict(have_baseline=s.get("have_baseline", False), baseline=s.get("baseline", []))
    return dict(have_baseline=True, baseline=s.get("last", []))


def _save_state(cfg, session_id, state, problems) -> None:
    path = sw.repo_root() / cfg.required_setting("session_close.state_path")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(dict(session_id=session_id, at=_now(),
                                    have_baseline=state.get("have_baseline", False),
                                    baseline=state.get("baseline", []), last=problems), indent=1),
                    encoding="utf-8")


# ── report ───────────────────────────────────────────────────────────────────────────────────
_STEP_TITLES = {"SC1": "SC1 Session and window", "SC2": "SC2 Spine (FATAL)",
                "SC3": "SC3 Researcher's words recorded", "SC4": "SC4 Open items in the register",
                "SC5": "SC5 Analysis integrity", "SC6": "SC6 Rule compliance",
                "SC8": "SC8 Session log", "SC9": "SC9 Decisions reached their targets",
                "SC10": "SC10 BUILD.md coverage", "SC15": "SC15 Control files"}


def _write_report(ctx, ident, F, info) -> pathlib.Path:
    path = pathlib.Path(ctx.cfg.required_setting("session_close.report_path"))
    open_f = [f for f in F if not f["cleared"]]
    intro = [f"> Generated {_now()} by `session.close` (#1875, rebuilt #2173). Detection only; "
             f"remediation is Claude's (`.claude/commands/session-close.md`). A finding is cleared "
             f"by fixing it, or by a disposition in the compliance file's `## Close dispositions` "
             f"that the check accepts. **The commit is blocked while any finding is open.**", "",
             f"- session: `{ident.get('session_id')}` ({ident.get('how')}); started "
             f"{ident.get('start')}; window base commit `{ident.get('base') or '--'}`",
             f"- compliance file: `{ident.get('compliance') or '--'}`; session log: "
             f"`{ident.get('log') or '--'}`",
             f"- **open findings: {len(open_f)}**; cleared by disposition: "
             f"{len(F) - len(open_f)}", ""]
    body: dict[str, list[str]] = {}
    for step in _STEP_TITLES:
        mine = [f for f in F if f["step"] == step]
        L = []
        for f in mine:
            mark = "cleared" if f["cleared"] else "**OPEN**"
            extra = f" -- disposition: {f['disposition']}" if f.get("disposition") else ""
            note = f" ({f['note']})" if f.get("note") else ""
            L.append(f"- {mark} `{f['key']}`: {f['text']}{extra}{note}")
        body[step] = L or ["_no finding_"]
    pub = info.get("publish", {})
    body["SC5"] = ([f"Chapters changed: {', '.join(pathlib.PurePosixPath(c).name for c in info.get('chapters_changed', [])) or 'none'}; "
                    f"quote parts checked: {info.get('quote_parts', 0)}; register check findings "
                    f"now: {info.get('register_findings', '?')}.", ""] + body["SC5"])
    body["SC12"] = [f"- narrative copy: {'RUN (a chapter changed)' if pub.get('narrative_copy') else 'not needed (no chapter changed)'}",
                    f"- threads register export: {'RUN (a thread row changed)' if pub.get('thread_export') else 'not needed (no thread row changed)'}"]
    sections = {"summary": [f"{len(open_f)} open finding(s); "
                            + (", ".join(f"{s} {sum(1 for f in open_f if f['step'] == s)}"
                                         for s in _STEP_TITLES if any(f['step'] == s for f in open_f))
                               or "none")]}
    for step in list(_STEP_TITLES) + ["SC12"]:
        sections[step.lower()] = body[step]
    L = reportkit.render_scaffold(ctx.db.conn, "session.close", sections, intro=intro)
    return reportkit.write_report(ctx.db.conn, "session.close", path, L)


def check(ctx: Ctx) -> Outcome:
    cfg, db = ctx.cfg, ctx.db
    root = sw.repo_root()
    F: list[dict] = []
    info: dict = {}
    session_id, tpath, how = sw.identify("Session-Close.ps1")
    record = sw.boundary_record(session_id) if session_id else None
    since = sw.session_start(record)
    ident = dict(session_id=session_id, how=how, start=since)
    # SC1
    if not session_id:
        F.append(dict(key="SC1:session", step="SC1", text=f"the session cannot be identified: {how}"))
    elif not record or not since:
        F.append(dict(key="SC1:boundary", step="SC1",
                      text=f"no boundary record .claude/session-boundary/{session_id}.json: the "
                           f"session's start and git window are unknown"))
    base = sw.commit_before(since) if since else None
    ident["base"] = base
    if since and not base:
        F.append(dict(key="SC1:base", step="SC1", text=f"no commit before the session start {since}"))
    changed = sw.changed_files(base) if base else []
    # SC2 -- FATAL first
    from ..lib.stepapi import Step
    sf = spine_mod.compute(cfg, db.conn, Step(cfg))
    F += [dict(key=k, step="SC2", text=t) for k, t in spine_mod.finding_lines(sf)]
    handles = _Handles(db)
    state = {"have_baseline": False, "baseline": []}
    if session_id and since:
        messages = sw.user_messages(tpath) if tpath else []
        f3, f4b = _sc3_sc4b(cfg, db, messages, since)
        F += f3 + _sc4a(cfg, root, changed, handles) + f4b
        state = _load_state(cfg, session_id)
        f5, info = _sc5(cfg, db, root, changed, since, base, state)
        F += f5
        # SC6
        cpath = compliance.find_file(cfg, session_id)
        ident["compliance"] = cpath.relative_to(root).as_posix() if cpath else None
        if cpath is None:
            F.append(dict(key="SC6:file", step="SC6",
                          text="no session compliance file (Compliance.ps1 -Action Template, "
                               "written at start-project)"))
        else:
            F += [dict(key=f"SC6:{x['key']}", step="SC6", text=x["reason"])
                  for x in compliance.check_close(cfg, cpath, since)]
        f89, log = _sc8_sc9(cfg, db, root, session_id, changed, since)
        ident["log"] = log.relative_to(root).as_posix() if log else None
        F += f89
        F += _sc10(cfg, base, changed)
        F += [dict(key=k, step="SC15", text=t)
              for k, t in cfgquality.find_control_file_problems(db.conn, root)]
        info["publish"] = _sc12(cfg, db, root, changed, since)
        disp = compliance.parse(cpath)["dispositions"] if cpath else {}
    else:
        disp = {}
    _apply_dispositions(F, disp, handles, db, since or "")
    for f in F:
        f.setdefault("cleared", False)
    report_path = _write_report(ctx, ident, F, info)
    if session_id and since:
        _save_state(cfg, session_id, state, info.get("register_problems", []))
    open_n = sum(1 for f in F if not f["cleared"])
    pub = info.get("publish", {})
    counts = dict(open_findings=open_n, cleared=len(F) - open_n,
                  fatal=sum(1 for f in F if f["step"] == "SC2" and not f["cleared"]),
                  narrative_copy=int(bool(pub.get("narrative_copy"))),
                  thread_export=int(bool(pub.get("thread_export"))), report=str(report_path))
    if open_n == 0:
        return ok(f"session-close: 0 open findings -- report {report_path}", **counts)
    return fail("findings-open", f"{open_n} open finding(s) -- commit blocked; report {report_path}",
                **counts)
