"""versescope.py -- the scope resolver (escalation #2228; design
outputs/escalation/2228-scope-resolver-design-v1-20261022.md, approved 2026-10-22).

Any request becomes the collection of verses it stands for. A request is one or more selectors,
combined as a union, and an optional filter (only_strong). Every verse carries the route(s) that
brought it in; everything that could not be resolved is listed with its reason, never dropped.
Read-only: no table is written.

Selectors: cluster, subgroup, strand, word, strong, verse, chapter (with an optional section heading),
claim, observation, item (a thread item, OT-nn.n) and thread (every open item of OT-nn).

Strong's codes follow cfg_behaviour_rule bare-strong-decomposed-to-derivatives (#2233): a bare code
that does not occur itself stands for every lettered derivative of its base that occurs in
verse_lexical; a suffixed code is taken as it is. No base carries both a bare and a lettered code
(checked 2026-10-22).

A chapter, block or claim gives only the verses it cites; pulling in other verses is a judgement
call made outside this tool (the neighbour-verse review, #2228 tool 6).

A request that is too wide is refused (researcher 2026-10-23): still resolving after
verse_scope.max_seconds, to be reformed; or more verses in the result than verse_scope.max_verses (2500),
held for review -- it proceeds only with request['reviewed'] (-Reviewed "<the review>"), which is kept in
the answer.
"""
from __future__ import annotations

import json
import re
import sqlite3
import time

from . import narrativeregister as nr

SELECTORS = ("cluster", "subgroup", "strand", "word", "strong", "verse", "chapter", "claim",
             "observation", "item", "thread")
NO_VERSE_ROW = "no verse row (by design: governance.verse_gap_by_design)"
_CODE = re.compile(r"([HG])0*(\d{1,4})([A-Za-z]*)")


class ScopeError(ValueError):
    """A request that cannot be answered as given (an unknown cluster, a code that occurs nowhere)."""


def _ids(xs) -> str:
    return json.dumps(sorted(set(xs)))


def _split(v) -> list[str]:
    """A command-line value ('M02,M01') or a request-file list, as a list of trimmed strings."""
    if v is None:
        return []
    if isinstance(v, (list, tuple)):
        out = []
        for x in v:
            out += _split(x) if isinstance(x, str) else [str(x)]
        return out
    return [x.strip() for x in str(v).split(",") if x.strip()]


def _chapter_key(v: str) -> str:
    """'02' and '2' are the same chapter; '10.1' stays '10.1' (as threadaudit reads it)."""
    head, _, rest = str(v).strip().partition(".")
    if head.isdigit():
        head = head.lstrip("0") or "0"
    return f"{head}.{rest}" if rest else head


class Resolver:
    def __init__(self, cfg):
        self.conn: sqlite3.Connection = cfg.conn
        self.vx = nr.VerseIndex(cfg)
        self.routes: dict[int, list[dict]] = {}
        self.not_resolved: list[dict] = []
        self.selectors: list[dict] = []
        self._codes: set[str] | None = None

    # ── shared ────────────────────────────────────────────────────────────────────────────────
    def occurring_codes(self) -> set[str]:
        if self._codes is None:
            self._codes = {r[0] for r in self.conn.execute(
                "SELECT DISTINCT strong FROM verse_lexical WHERE deleted=0")}
        return self._codes

    def _derived(self, base: str) -> list[str]:
        return sorted(c for c in self.occurring_codes() if c.startswith(base) and c[len(base):].isalpha())

    def decompose(self, given: str) -> list[str]:
        """One Strong's code as the codes it stands for (rule bare-strong-decomposed-to-derivatives)."""
        m = _CODE.fullmatch(given.strip())
        if not m:
            raise ScopeError(f"{given!r} is not a Strong's code")
        base = f"{m.group(1)}{m.group(2).zfill(4)}"
        if m.group(3):
            code = base + m.group(3)
            if code not in self.occurring_codes():
                hint = self._derived(base)
                raise ScopeError(f"{given!r} occurs in no verse"
                                 + (f" -- did you mean {', '.join(hint)}?" if hint else ""))
            return [code]
        if base in self.occurring_codes():
            return [base]
        derived = self._derived(base)
        if not derived:
            raise ScopeError(f"{given!r} occurs in no verse and has no derivative that does")
        return derived

    def senses(self, codes) -> dict[str, str]:
        return {r[0]: r[1] for r in self.conn.execute(
            "SELECT strong, head FROM strong_sense WHERE deleted=0 AND strong IN "
            "(SELECT value FROM json_each(?))", (_ids(codes),))}

    def add(self, verse_id: int, route: dict) -> None:
        self.routes.setdefault(verse_id, []).append(route)

    def miss(self, kind: str, value, reason: str) -> None:
        self.not_resolved.append({"kind": kind, "value": value, "reason": reason})

    def _expand_codes(self, raw: list[str], kind: str | None = None, value: str | None = None) -> list[str]:
        """Codes from a grouping table (kind/value given): one that occurs nowhere is reported, not raised,
        so a stale code does not refuse the whole grouping. Codes the request names itself raise."""
        out: list[str] = []
        for c in raw:
            try:
                out += self.decompose(c)
            except ScopeError as exc:
                if kind is None:
                    raise
                self.miss(kind, f"{value}: {c}", str(exc))
        return list(dict.fromkeys(out))

    def _by_codes(self, kind: str, value: str, codes: list[str], name: str | None = None,
                  route_kind: str | None = None, route_value: str | None = None) -> int:
        """Every verse holding one of `codes` (one set-based query); returns the verse count."""
        seen = set()
        for vid, code in self.conn.execute(
                "SELECT DISTINCT verse_id, strong FROM verse_lexical WHERE deleted=0 AND strong IN "
                "(SELECT value FROM json_each(?))", (_ids(codes),)):
            self.add(vid, {"kind": route_kind or kind, "value": route_value or value, "via": code})
            seen.add(vid)
        sense = self.senses(codes)
        self.selectors.append({"kind": kind, "value": value, **({"name": name} if name else {}),
                               "strongs": [{"code": c, "sense": sense.get(c)} for c in sorted(set(codes))],
                               "verses": len(seen)})
        return len(seen)

    # ── selectors ─────────────────────────────────────────────────────────────────────────────
    def cluster(self, code: str, **route) -> int:
        row = self.conn.execute("SELECT cluster_code, short_name FROM cluster WHERE cluster_code=? "
                                "AND coalesce(deleted,0)=0", (code,)).fetchone()
        if row is None:
            raise ScopeError(f"cluster {code!r} is not a live cluster")
        raw = [r[0] for r in self.conn.execute(
            "SELECT DISTINCT strong FROM cluster_strong WHERE cluster_code=? AND deleted=0", (code,))]
        return self._by_codes("cluster", code, self._expand_codes(raw, "cluster", code), row[1], **route)

    def subgroup(self, code: str, **route) -> int:
        row = self.conn.execute("SELECT id, label FROM cluster_subgroup WHERE subgroup_code=? AND "
                                "coalesce(delete_flagged,0)=0", (code,)).fetchone()
        if row is None:
            raise ScopeError(f"subgroup {code!r} is not a live cluster subgroup")
        raw = [r[0] for r in self.conn.execute(
            "SELECT strong FROM cluster_subgroup_strong WHERE cluster_subgroup_id=? AND "
            "coalesce(delete_flagged,0)=0", (row[0],))]
        return self._by_codes("subgroup", code, self._expand_codes(raw, "subgroup", code), row[1], **route)

    def strand(self, code: str, **route) -> int:
        row = self.conn.execute("SELECT id, title FROM reading_strand WHERE code=?", (code,)).fetchone()
        if row is None:
            raise ScopeError(f"strand {code!r} is not a defined strand (reading_strand)")
        raw = [r[0] for r in self.conn.execute(
            "SELECT strong FROM reading_strand_strong WHERE strand_id=?", (row[0],))]
        return self._by_codes("strand", code, self._expand_codes(raw, "strand", code), row[1], **route)

    def word(self, word: str, **route) -> int:
        row = self.conn.execute("SELECT id FROM word_registry WHERE word=? AND deleted=0", (word,)).fetchone()
        if row is None:
            raise ScopeError(f"word {word!r} is not in word_registry")
        raw = [r[0] for r in self.conn.execute(
            "SELECT strong FROM word_strong WHERE word_id=? AND deleted=0", (row[0],))]
        return self._by_codes("word", word, self._expand_codes(raw, "word", word), None, **route)

    def strong(self, given: str, **route) -> int:
        return self._by_codes("strong", given, self.decompose(given), None, **route)

    def verse(self, text: str, route_kind: str | None = None, route_value: str | None = None) -> int:
        refs = nr.parse_refs(text, self.vx)
        if not refs:
            self.miss("verse", text, "no verse reference found in the text")
            return 0
        seen = set()
        for r in refs:
            rk = {"kind": route_kind or "verse", "value": route_value or text, "via": r.normalised}
            if r.verse_id is not None:
                self.add(r.verse_id, rk)
                seen.add(r.verse_id)
            elif r.kind == "whole chapter" and not nr.unresolved(self.vx, r.normalised, None):
                book, ch = r.normalised.split(" ")
                for (b, c, _v), vid in self.vx.ids.items():
                    if b == book and c == int(ch):
                        self.add(vid, rk)
                        seen.add(vid)
            else:
                self.miss("verse", r.normalised, NO_VERSE_ROW if r.kind == "verse"
                          else "the book has no such chapter")
        self.selectors.append({"kind": "verse", "value": text, "verses": len(seen)})
        return len(seen)

    def chapter(self, chapter: str, section: str | None = None, route_kind: str | None = None,
                route_value: str | None = None) -> int:
        key = _chapter_key(chapter)
        rows = [r for r in self.conn.execute(
            "SELECT id, chapter_no, title FROM narrative_chapter WHERE inactive=0")
            if _chapter_key(r[1]) == key]
        if not rows:
            raise ScopeError(f"chapter {chapter!r} is not an active narrative chapter")
        cid, cno, title = rows[0]
        blocks = self.conn.execute(
            "SELECT id, heading FROM narrative_section WHERE chapter_id=? AND last_version IS NULL "
            "ORDER BY ordinal", (cid,)).fetchall()
        if section:
            blocks = [b for b in blocks if (b[1] or "").strip().lower() == section.strip().lower()]
            if not blocks:
                raise ScopeError(f"chapter {cno} has no current block headed {section!r}")
            if len(blocks) > 1:
                raise ScopeError(f"chapter {cno} has {len(blocks)} current blocks headed {section!r}")
        value = cno + (f" / {section}" if section else "")
        heading = {b[0]: b[1] for b in blocks}
        cited = {b[0]: 0 for b in blocks}
        seen = set()
        for sid, vid, written in self.conn.execute(
                "SELECT section_id, verse_id, ref_as_written FROM narrative_citation WHERE last_version IS NULL "
                "AND section_id IN (SELECT value FROM json_each(?))", (_ids(cited),)):
            if vid is None:
                self.miss("citation", f"{cno} / {heading[sid]}: {written}", "citation does not resolve to a verse")
                continue
            cited[sid] += 1
            self.add(vid, {"kind": route_kind or "chapter", "value": route_value or value, "via": heading[sid]})
            seen.add(vid)
        for sid, n in cited.items():
            if not n:
                self.miss("block", f"{cno} / {heading[sid]}", "block cites no verse")
        self.selectors.append({"kind": "chapter", "value": value, "name": title, "blocks": len(blocks),
                               "verses": len(seen)})
        return len(seen)

    def claim(self, ref: str) -> int:
        row = self.conn.execute("SELECT id, claim_ref, claim_text, status FROM narrative_claim WHERE claim_ref=? "
                                "OR CAST(id AS TEXT)=?", (ref, ref)).fetchone()
        if row is None:
            raise ScopeError(f"claim {ref!r} is not in the register")
        seen = set()
        for kind, vid, written in self.conn.execute(
                "SELECT source_kind, verse_id, ref_as_written FROM narrative_claim_source WHERE claim_id=?",
                (row[0],)):
            if kind != "verse":
                self.miss("claim source", f"{row[1]}: {written or kind}", f"source is a {kind}, not a verse")
            elif vid is None:
                self.miss("claim source", f"{row[1]}: {written}", "source does not resolve to a verse")
            else:
                self.add(vid, {"kind": "claim", "value": row[1], "via": written})
                seen.add(vid)
        if not seen:
            self.miss("claim", row[1], "claim has no verse source")
        self.selectors.append({"kind": "claim", "value": row[1], "name": row[2], "status": row[3],
                               "verses": len(seen)})
        return len(seen)

    def observation(self, oid: str) -> int:
        row = self.conn.execute("SELECT id, status FROM ib_observation WHERE id=?", (oid,)).fetchone()
        if row is None:
            raise ScopeError(f"observation {oid!r} does not exist")
        seen = set()
        for vid, osis in self.conn.execute(
                "SELECT DISTINCT v.id, n.verse_reference FROM ib_node n JOIN verse v ON v.osisId=n.verse_reference "
                "AND v.deleted=0 WHERE n.observation_id=?", (row[0],)):
            self.add(vid, {"kind": "observation", "value": str(row[0]), "via": osis})
            seen.add(vid)
        if not seen:
            self.miss("observation", str(row[0]), "observation is grounded on no verse")
        self.selectors.append({"kind": "observation", "value": str(row[0]), "status": row[1],
                               "verses": len(seen)})
        return len(seen)

    def _thread(self, alias: str):
        m = re.fullmatch(r"OT-0*(\d+)", alias.strip(), re.I)
        if not m:
            raise ScopeError(f"{alias!r} is not a thread (OT-nn)")
        row = self.conn.execute("SELECT id, alias FROM escalation WHERE type='thread' AND "
                                "CAST(substr(alias, 4) AS INTEGER)=?", (int(m.group(1)),)).fetchone()
        if row is None:
            raise ScopeError(f"thread {alias!r} does not exist")
        return row

    def _item(self, kind: str, value: str, label: str) -> None:
        """One thread item, resolved by its kind; a kind that names no verse, or a value that does not
        resolve, is reported, not raised (a thread may hold items of every kind)."""
        route = {"route_kind": "item", "route_value": f"{label} {kind}:{value}"}
        before = len(self.selectors)
        try:
            if kind == "verse":
                self.verse(value, **route)
            elif kind == "cluster":
                self.cluster(value, **route)
            elif kind == "strong":
                self.strong(value, **route)
            elif kind == "chapter":
                self.chapter(value, **route)
            elif kind == "strand":
                self.strand(value, **route)
            else:
                self.miss("item", label, f"kind {kind!r} names no verse")
        except ScopeError as exc:
            self.miss("item", f"{label} {kind}:{value}", str(exc))
        for s in self.selectors[before:]:
            s["item"] = label

    def item(self, ref: str) -> None:
        m = re.fullmatch(r"(OT-\d+)\.(\d+)", ref.strip(), re.I)
        if not m:
            raise ScopeError(f"{ref!r} is not a thread item (OT-nn.n)")
        tid, alias = self._thread(m.group(1))
        it = self.conn.execute("SELECT kind, value FROM escalation_thread_item WHERE escalation_id=? AND item_no=?",
                               (tid, int(m.group(2)))).fetchone()
        if it is None:
            raise ScopeError(f"thread item {ref!r} does not exist")
        self._item(it[0], (it[1] or "").strip(), f"{alias}.{int(m.group(2))}")

    def thread(self, ref: str) -> None:
        tid, alias = self._thread(ref)
        items = self.conn.execute("SELECT item_no, kind, value FROM escalation_thread_item WHERE escalation_id=? "
                                  "AND status='open' ORDER BY item_no", (tid,)).fetchall()
        if not items:
            self.miss("thread", alias, "thread has no open item")
        for no, kind, value in items:
            self._item(kind, (value or "").strip(), f"{alias}.{no}")

    # ── filter and answer ─────────────────────────────────────────────────────────────────────
    def only_strong(self, raw: list[str]) -> dict:
        codes = self._expand_codes(raw)
        keep = {r[0] for r in self.conn.execute(
            "SELECT DISTINCT verse_id FROM verse_lexical WHERE deleted=0 AND strong IN (SELECT value FROM json_each(?)) "
            "AND verse_id IN (SELECT value FROM json_each(?))", (_ids(codes), _ids(self.routes)))}
        dropped = len(self.routes) - len(keep)
        self.routes = {v: r for v, r in self.routes.items() if v in keep}
        sense = self.senses(codes)
        return {"strongs": [{"code": c, "sense": sense.get(c)} for c in codes], "verses_dropped": dropped}

    def verses(self) -> list[dict]:
        rank = {osis: self.vx.book_rank.get(code, 999) for code, osis in self.vx.osis.items()}
        rows = self.conn.execute("SELECT id, osisId, reference FROM verse WHERE id IN (SELECT value FROM json_each(?))",
                                 (_ids(self.routes),)).fetchall()

        def key(r):
            b, c, v = (r[1].split(".") + ["0", "0"])[:3]
            return (rank.get(b, 999), int(c), int(v))
        return [{"verse_id": r[0], "osis": r[1], "reference": r[2], "routes": self.routes[r[0]]}
                for r in sorted(rows, key=key)]


def normalise_request(params: dict, file_request: dict | None = None) -> dict:
    """Command-line parameters (PS names, any case) and a request file merged into one request: a list per
    selector. A chapter is {'chapter': '10.1', 'section': heading or None}. Verse text is kept whole (it may
    hold ';' and ',')."""
    req: dict = {k: [] for k in SELECTORS}
    req["only_strong"] = []
    for src in (file_request or {}, {k.lower(): v for k, v in params.items()}):
        for k in ("cluster", "subgroup", "strand", "word", "strong", "claim", "observation", "item", "thread"):
            req[k] += _split(src.get(k))
        req["only_strong"] += _split(src.get("only_strong") or src.get("onlystrong"))
        if src.get("reviewed"):
            req["reviewed"] = str(src["reviewed"]).strip()
        v = src.get("verse")
        req["verse"] += [str(x) for x in (v if isinstance(v, list) else [v]) if x and str(x).strip()]
        ch = src.get("chapter")
        for c in (ch if isinstance(ch, list) else [ch]):
            if isinstance(c, dict):
                req["chapter"].append({"chapter": str(c.get("chapter")), "section": c.get("section")})
            elif c:
                for x in _split(c):
                    req["chapter"].append({"chapter": x, "section": src.get("section")})
    return {k: v for k, v in req.items() if v}


def _too_wide(r: Resolver, n: int, limit: int, what: str) -> ScopeError:
    """The refusal for a request past a guard: the selectors and their verse counts, widest first, so the
    request can be reformed (researcher 2026-10-23, #2228)."""
    parts = sorted(r.selectors, key=lambda s: -s["verses"])
    listed = "; ".join(f"{s['kind']} {s['value']}{' (' + s['item'] + ')' if s.get('item') else ''}: {s['verses']}"
                       for s in parts[:12])
    hold = ("it is held for review: reform it to a narrower scope, or, once the researcher has reviewed it, "
            "re-run with -Reviewed \"<the review>\"" if "verses" in what else "reform it to a narrower scope")
    return ScopeError(f"the request is too wide -- {what} ({n} against the limit {limit}); {hold}. "
                      f"Verses by selector, widest first: {listed}"
                      + (f"; and {len(parts) - 12} more" if len(parts) > 12 else ""))


def resolve(cfg, request: dict) -> dict:
    """The verse collection for a normalised request (see normalise_request): the selectors, the verses with
    their routes in canonical order, what was not resolved, and counts. Raises ScopeError on a request that
    cannot be answered as given, or that is too wide: more verses than verse_scope.max_verses, or still
    resolving after verse_scope.max_seconds. Reads only."""
    if not any(request.get(k) for k in SELECTORS):
        raise ScopeError("the request has no selector (-Cluster, -Subgroup, -Strand, -Word, -Strong, -Verse, "
                         "-Chapter, -Claim, -Observation, -Item, -Thread or -File)")
    max_verses = int(cfg.required_setting("verse_scope.max_verses"))
    max_seconds = float(cfg.required_setting("verse_scope.max_seconds"))
    t0 = time.monotonic()
    r = Resolver(cfg)

    def check_time():
        s = time.monotonic() - t0
        if s > max_seconds:
            raise _too_wide(r, int(s), int(max_seconds), "still resolving after the time limit, seconds")

    for k in ("cluster", "subgroup", "strand", "word", "strong", "verse", "claim", "observation"):
        for v in request.get(k, []):
            getattr(r, k)(str(v))
            check_time()
    for c in request.get("chapter", []):
        r.chapter(c["chapter"], c.get("section"))
        check_time()
    for v in request.get("item", []):
        r.item(v)
        check_time()
    for v in request.get("thread", []):
        r.thread(v)
        check_time()
    filt = r.only_strong(request["only_strong"]) if request.get("only_strong") else None
    if len(r.routes) > max_verses and not request.get("reviewed"):
        raise _too_wide(r, len(r.routes), max_verses, "verses in the result"
                        + (" after -OnlyStrong" if filt else ""))
    verses = r.verses()
    out = {"request": request, "selectors": r.selectors, "verses": verses, "not_resolved": r.not_resolved,
           "counts": {"verses": len(verses), "selectors": len(r.selectors), "not_resolved": len(r.not_resolved)}}
    if len(verses) > max_verses:
        out["reviewed"] = request["reviewed"]       # passed the size guard only on a recorded review
    if filt is not None:
        out["only_strong"] = filt
    return out
