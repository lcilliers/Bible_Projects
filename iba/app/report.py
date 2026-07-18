"""report.py — the word-raw output. CONFIG-GOVERNED.

What the report shows is read from config (cfg_setting report.*): how many sample
verses, whether the verse text appears, which columns per section. This module only
knows HOW to render a section (a markdown table) — a report shape, not a choice.

    python -m iba.app.report --word hypocrisy
"""

from __future__ import annotations

import argparse
import pathlib

from .lib.cfg import Cfg, DB_PATH
from .lib.db import Db
from .lib.stepapi import strip_html

APP = pathlib.Path(__file__).resolve().parent
B = "http://localhost:8989"


def esc(s) -> str:
    return str(s if s is not None else "").replace("|", "\\|").replace("\n", " ").strip()


def clip(s, n) -> str:
    s = esc(s)
    return s if len(s) <= n else s[: n - 1] + "…"


# how to fetch a field's value — the only per-field code; the LIST of fields is config
def _strong_val(db, code, field):
    s = db.get("strong", strongNumber=code) or {}
    if field in ("stepGloss", "accentedUnicode", "stepTransliteration", "count"):
        return s[field] if field in s.keys() else ""
    if field == "head":
        se = db.get("strong_sense", strong=code)
        return f"**{clip(se['head'], 34)}**" if se else ""
    if field == "verses":
        return db.count("strong_verse", strong=code)
    return ""


def _span_val(db, sp, field, held):
    if field in ("position", "surface", "strong_variant", "morph_code"):
        v = sp[field] if field in sp.keys() else ""
        return f"`{esc(v)}`" if field in ("strong_variant", "morph_code") else esc(v)
    if field == "is_particle":
        return "·" if sp["is_particle"] else ""
    if field == "sense":
        se = db.get("strong_sense", strong=sp["strong_variant"])
        return f"**{clip(se['head'], 24)}**" if (sp["strong_variant"] in held and se) else ""
    return ""


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--word", required=True)
    a = ap.parse_args()
    cfg = Cfg()
    db = Db(cfg)

    # ── config: what to show ──
    sample_n = int(cfg.setting("report.sample_verses", 3))
    show_text = bool(cfg.setting("report.show_verse_text", True))
    show_val = bool(cfg.setting("report.show_validation", True))
    strong_fields = cfg.setting("report.strong_fields", ["stepGloss", "head", "count", "verses"])
    span_fields = cfg.setting("report.span_fields",
                              ["position", "surface", "strong_variant", "morph_code", "is_particle", "sense"])

    w = db.get("word_registry", word=a.word)
    if not w:
        print(f"{a.word!r} not in the DB.")
        return 1
    wid = w["id"]
    strongs = [r["strong"] for r in db.rows(
        "SELECT strong FROM word_strong WHERE word_id=? ORDER BY strong", (wid,))]
    ph = ",".join("?" * len(strongs))
    held = set(strongs)

    L = [f"# Raw layer — `{a.word}`", "",
         f"> Built by the IBA app into `{DB_PATH.relative_to(pathlib.Path.cwd())}`. "
         f"What this report shows is config (`cfg_setting report.*`). Every row is checkable "
         f"against STEP.", "",
         f"**word_registry** — id {wid} · status `{w['status']}` · source {esc(w['source'])}", ""]

    # ── validation (util.validation) ──
    if show_val:
        vr = db.rows("SELECT check_name, result, detail, ran_at FROM validation_result "
                     "WHERE word=? ORDER BY id", (a.word,))
        L += ["## Validation", ""]
        if vr:
            L += ["| check | result | detail |", "|---|---|---|"]
            for r in vr:
                mark = "✓ pass" if r["result"] == "pass" else "✗ **FAIL**"
                L.append(f"| {r['check_name']} | {mark} | {clip(r['detail'], 70)} |")
        else:
            L += ["_No validation recorded — raw.validate has not run for this word._"]
        L += [""]

    # ── strongs and their meaning ──
    L += ["## The strongs and their meaning (L1 → L2)", "",
          "| strong | " + " | ".join(strong_fields) + " |",
          "|---|" + "---|" * len(strong_fields)]
    for code in strongs:
        L.append("| `" + code + "` | " +
                 " | ".join(str(_strong_val(db, code, f)) for f in strong_fields) + " |")
    L += [""]

    # ── sample verses — the span layer, with verse text if config says so ──
    sample = db.rows(
        f"SELECT v.* FROM verse v JOIN strong_verse sv ON sv.verse_id=v.id "
        f"WHERE sv.strong IN ({ph}) GROUP BY v.id "
        f"ORDER BY (SELECT COUNT(*) FROM span s WHERE s.verse_id=v.id) DESC LIMIT ?",
        strongs + [sample_n])
    L += ["## Sample verses — the span layer (one row per code)", ""]
    for v in sample:
        L += [f"### {v['reference']} — `{v['osisId']}`", ""]
        if show_text:                                     # <- config toggle
            L += [f"> {clip(strip_html(v['preview']), 400)}", ""]
        spans = db.rows("SELECT * FROM span WHERE verse_id=? ORDER BY position", (v["id"],))
        L += ["| " + " | ".join(span_fields) + " |", "|" + "---|" * len(span_fields)]
        for sp in spans:
            L.append("| " + " | ".join(str(_span_val(db, sp, f, held)) for f in span_fields) + " |")
        L += [""]

    out = APP / f"report-{a.word}.md"
    out.write_text("\n".join(L).rstrip() + "\n", encoding="utf-8")
    print(f"wrote {out.relative_to(pathlib.Path.cwd())}")
    db.close()
    return 0


if __name__ == "__main__":
    import sys
    sys.exit(main())
