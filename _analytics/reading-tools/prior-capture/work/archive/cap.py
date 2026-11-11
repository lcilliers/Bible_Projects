"""Shared helper for the hand fills of the #2305 prior-work capture (not a registered tool: the fills are judgement).
Usage in a fill script:  from cap import Fill ; c = Fill(12, "M01") ; c.f(...) ; c.rec(...) ; c.not_(...) ; c.done()
"""
import json, glob, pathlib, re
OUT = pathlib.Path("outputs/prior-capture")
WORK = OUT / "work"


class Fill:
    def __init__(self, fid: int, cluster: str):
        src = sorted(glob.glob(str(OUT / f"capture-{fid:03d}-2*.json")))[-1]
        self.fid, self.CL = fid, cluster
        self.d = json.loads(pathlib.Path(src).read_text(encoding="utf-8"))
        self.vw = self.d["verse_words"]
        self.by_line = {l["line_no"]: l for l in self.d["lines"]}
        self.IDS = {**self.d["october_same_prefix"], **self.d["october"]}
        self.F, self.ANS = [], {}

    def verses_of(self, lines):
        out = []
        for n in lines:
            for r in self.by_line[n]["refs"]:
                if r["verse"] and r["verse"] not in out:
                    out.append(r["verse"])
        return out

    def nodes(self, verses, text, disp=None, note=None):
        out, seen, low = [], set(), (text or "").lower()
        for v in verses:
            ws = [w for w in self.vw.get(v, []) if w["surface"] and any(c[0] == "M" for c in w["clusters"]) and
                  re.search(chr(92) + "b" + re.escape(w["surface"].lower()) + chr(92) + "b", low)]
            if not ws:
                out.append({"verse": v})
            for w in ws:
                k = (v, w["strong"], w["surface"])
                if k not in seen:
                    seen.add(k)
                    n = {"verse": v, "strong": w["strong"], "surface": w["surface"],
                         "role": "characteristic" if self.CL in w["clusters"] else "standalone"}
                    if self.CL in w["clusters"]:
                        n["cluster"] = self.CL
                    out.append(n)
        for n in out:
            if disp:
                n["disposition"] = disp
            if note:
                n["disposition_note"] = note
        return out

    def f(self, key, kind, text, lines, basis="stated", route=None, stable=None, disp=None, note=None, traced=(),
          flag=None, verses=None, meaning=None):
        vs = verses if verses is not None else self.verses_of(lines)
        if not vs and not traced:                          # a chapter named, no verse: the chapter's first verse (design 1)
            import sqlite3
            db = sqlite3.connect("file:iba/app/db/iba.db?mode=ro", uri=True)
            q = ",".join("?" * len(lines))
            r = db.execute(f"SELECT ref_normalised, ref_as_written FROM reading_ref WHERE file_id=? AND deleted=0 AND "
                           f"kind='whole chapter' AND line_no IN ({q}) ORDER BY id LIMIT 1", (self.fid, *lines)).fetchone()
            db.close()
            if r:
                vs = [f"{r[0]}:1"]
                note = (note + "; " if note else "") + f"chapter pointer: {r[1]}"
        if not vs and not traced:                          # bare references only: the nearest earlier line's verse
            prev = [k for k in sorted(self.by_line) if k < min(lines) and self.verses_of([k])]
            if prev:
                vs = self.verses_of([prev[-1]])[:1]
                flag = (flag + "; " if flag else "") + "verse taken from the nearest earlier line: this line's references are bare"
        ns = self.nodes(vs, text, disp, note) + [{"traced": t} for t in traced]
        self.F.append({"key": key, "kind": kind, "text": text, "basis": basis, "route": route, "stable_key": stable,
                       "flag": flag, "meaning": meaning, "nodes": ns})
        for n in lines:
            self.ANS.setdefault(n, {}).setdefault("captured", []).append(key)

    def rec(self, line, stable_key):
        self.ANS[line] = {"already_recorded": [self.IDS[stable_key]]}

    def not_(self, lines, cls, reason):
        for n in ([lines] if isinstance(lines, int) else lines):
            self.ANS[n] = {"not_an_observation": cls, "reason": reason}

    def done(self):
        for l in self.d["lines"]:
            l["answer"] = self.ANS.get(l["line_no"])
        missing = [l["line_no"] for l in self.d["lines"] if not l["answer"]]
        self.d["findings"] = self.F
        p = WORK / f"capture-{self.fid:03d}-filled.json"
        p.write_text(json.dumps(self.d, ensure_ascii=False), encoding="utf-8")
        print(len(self.F), "findings;", sum(len(x["nodes"]) for x in self.F), "nodes; unanswered:", missing, "->", p)


# ── generic pass for the unit ledgers (tables of ids, faces, factors; chain bullets; notes) ──────────────────────────
def _clean(s):
    return re.sub(r"\s+", " ", s.replace("**", "").replace("~~", "").replace("*", "")).strip()


def _auto(self, id_re=r"\|\s*([A-Z]{2}-\d+|[A-Z]{1,3}-H?\d+)\s*\|", skip=()):
    """Answer every line still unanswered: recorded id -> already recorded; id row -> an observation; table row -> an
    observation built from its column headers; chain bullet (with an arrow) -> a link; the rest -> a pass-over."""
    root = pathlib.Path(".")
    lines = (root / self.d["file"]["path"]).read_text(encoding="utf-8").replace("\r", "").split("\n")

    def header(n):
        i = n - 1
        while i > 0 and not (lines[i].startswith("|") and i + 1 < len(lines) and re.match(r"\|[\s:\-|]+\|\s*$", lines[i + 1])):
            i -= 1
            if lines[i].strip() == "" or not lines[i].startswith("|") and not lines[i].startswith("-"):
                if i < n - 40:
                    return []
        return [_clean(x) for x in lines[i].strip().strip("|").split("|")] if i > 0 else []

    kinds = {"face": 0, "statement": 0, "link": 0, "term": 0, "pass": 0, "rec": 0}
    for n in sorted(self.by_line):
        if n in self.ANS or n in skip:
            continue
        t = self.by_line[n]["text"]
        m = re.match(id_re, t)
        if m:
            key = m.group(1)
            sk = next((p + ":" + key for p in ("anger", "fear") if (p + ":" + key) in self.IDS), None)
            if sk:
                self.rec(n, sk); kinds["rec"] += 1
                continue
            h = [x.lower() for x in header(n)]
            x = [_clean(y) for y in t.strip().strip("|").split(" | ")]
            def col(*names):
                for nm in names:
                    for i, hh in enumerate(h):
                        if nm in hh and i < len(x):
                            return x[i]
                return ""
            text = col("observation", "what the verses state", "what the verse", "link") or (x[1] if len(x) > 1 else "")
            basis = col("basis")
            disp, touches = col("disposition"), col("touches")
            note = "; ".join(p for p in (disp, f"touches {touches}" if touches else "") if p)
            prefix = "anger"
            self.f(key, "statement", text.rstrip(".") + ".", [n], basis="read" if basis.startswith("R") else "stated",
                   stable=f"{prefix}:{key}", disp="told" if disp else None, note=note or None)
            kinds["statement"] += 1
            continue
        if t.startswith("|"):
            h = header(n)
            x = [_clean(y) for y in t.strip().strip("|").split(" | ")]
            if len(x) < 2:
                self.not_(n, "scope or method or process record", "a table line with no finding"); kinds["pass"] += 1
                continue
            parts = [f"{(h[i] if i < len(h) and h[i] else '')}: {v}".strip(": ") for i, v in enumerate(x[1:], 1)
                     if v and not (i < len(h) and h[i].lower() == "basis")]
            face = re.match(r"^\d*[A-Z]{1,3}\.\s", x[0]) is not None
            text = (f"Face {x[0]}" if face else x[0]) + ": " + "; ".join(parts) + "."
            self.f(f"r{n}", "face" if face else "statement", text, [n], basis="read" if face else "stated")
            kinds["face" if face else "statement"] += 1
            continue
        low = t.lower()
        if "quotes checked" in low or "quote check" in low or "checker" in low:
            self.not_(n, "weave or quote-check record", "the quote check and its result"); kinds["pass"] += 1
        elif t.startswith("- ") and ("→" in t or "->" in t):
            self.f(f"b{n}", "link", _clean(t[2:]).rstrip(".") + ".", [n], basis="stated"); kinds["link"] += 1
        else:
            self.not_(n, "scope or method or process record", "a note, open thread or count about the work, not a finding")
            kinds["pass"] += 1
    return kinds


Fill.auto = _auto
