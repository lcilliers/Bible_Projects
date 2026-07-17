"""report.py — render a word's raw layer as markdown, for the researcher to inspect.

Reads only the DB. Every claim is checkable against STEP (the URLs are in the header).

    python -m iba.app.report --word hypocrisy
"""

from __future__ import annotations

import argparse
import pathlib

from .lib.db import Db, DB_PATH, SCHEMA

APP = pathlib.Path(__file__).resolve().parent
B = "http://localhost:8989"


def esc(s) -> str:
    return str(s if s is not None else "").replace("|", "\\|").replace("\n", " ").strip()


def clip(s, n) -> str:
    s = esc(s)
    return s if len(s) <= n else s[: n - 1] + "…"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--word", required=True)
    a = ap.parse_args()
    db = Db()
    w = db.get("word_registry", word=a.word)
    if not w:
        print(f"{a.word!r} not in the DB.")
        return 1
    wid = w["id"]

    L = [f"# Raw layer — `{a.word}`", "",
         f"> Built by the IBA app (`iba/app`) into `{DB_PATH.relative_to(pathlib.Path.cwd())}`. "
         "Every row is checkable against STEP:", ">",
         f"> - detail — `{B}/rest/module/getInfo/ESV_th//G5272//`",
         f"> - verses — `{B}/rest/search/masterSearch/strong=G5272|version=ESV_th`", "",
         f"**word_registry** — id {wid} · status `{w['status']}` · source {esc(w['source'])}", ""]

    # counts
    strongs = [r["strong"] for r in db.rows(
        "SELECT strong FROM word_strong WHERE word_id=? ORDER BY strong", (wid,))]
    ph = ",".join("?" * len(strongs))
    L += ["## The layer, in numbers", "", "| table | rows |", "|---|---|"]
    for t in ["word_strong", "strong", "strong_sense", "strong_meaning_tree", "strong_lexicon",
              "verse", "strong_verse", "span"]:
        if t == "word_strong":
            n = db.count(t, word_id=wid)
        elif t == "strong":
            n = db.rows(f"SELECT COUNT(*) n FROM strong WHERE strongNumber IN ({ph})", strongs)[0]["n"]
        elif t in ("strong_sense", "strong_lexicon"):
            n = db.rows(f"SELECT COUNT(*) n FROM {t} WHERE strong IN ({ph})", strongs)[0]["n"]
        elif t == "strong_verse":
            n = db.rows(f"SELECT COUNT(*) n FROM strong_verse WHERE strong IN ({ph})", strongs)[0]["n"]
        elif t == "verse":
            n = db.rows(f"SELECT COUNT(DISTINCT verse_id) n FROM strong_verse WHERE strong IN ({ph})", strongs)[0]["n"]
        elif t == "span":
            n = db.rows(f"SELECT COUNT(*) n FROM span WHERE verse_id IN "
                        f"(SELECT DISTINCT verse_id FROM strong_verse WHERE strong IN ({ph}))", strongs)[0]["n"]
        else:
            n = db.rows(f"SELECT COUNT(*) n FROM strong_meaning_tree WHERE lemma_key IN ({ph})", strongs)[0]["n"]
        L.append(f"| `{t}` | {n} |")
    L += [""]

    # L1 -> L2 the strongs and their meaning
    L += ["## The strongs and their meaning (L1 → L2)", "",
          "| strong | gloss | script | translit | **the sense (head)** | count | verses |",
          "|---|---|---|---|---|---|---|"]
    for code in strongs:
        s = db.get("strong", strongNumber=code)
        se = db.get("strong_sense", strong=code)
        nv = db.count("strong_verse", strong=code)
        if s:
            L.append(f"| `{code}` | {esc(s['stepGloss'])} | {esc(s['accentedUnicode'])} | "
                     f"{esc(s['stepTransliteration'])} | **{clip(se['head'] if se else '', 34)}** | "
                     f"{s['count']} | {nv} |")
    L += [""]

    # a sample verse with its spans — the backtrack
    sample = db.rows(
        f"SELECT v.* FROM verse v JOIN strong_verse sv ON sv.verse_id=v.id "
        f"WHERE sv.strong IN ({ph}) GROUP BY v.id "
        f"ORDER BY (SELECT COUNT(*) FROM span s WHERE s.verse_id=v.id) DESC LIMIT 3", strongs)
    L += ["## Sample verses — the span layer (one row per code)", ""]
    for v in sample:
        spans = db.rows("SELECT * FROM span WHERE verse_id=? ORDER BY position", (v["id"],))
        held = {code for code in strongs}
        L += [f"### {v['reference']} — `{v['osisId']}`", "",
              "| pos | surface | strong | morph | particle | held? · sense |",
              "|---|---|---|---|---|---|"]
        for sp in spans:
            se = db.get("strong_sense", strong=sp["strong_variant"])
            mine = sp["strong_variant"] in held
            mark = f"**{clip(se['head'],24)}**" if (mine and se) else ""
            L.append(f"| {sp['position']} | {esc(sp['surface'])} | `{sp['strong_variant']}` | "
                     f"`{esc(sp['morph_code'])}` | {'·' if sp['is_particle'] else ''} | {mark} |")
        L += [""]

    out = APP / f"report-{a.word}.md"
    out.write_text("\n".join(L).rstrip() + "\n", encoding="utf-8")
    print(f"wrote {out.relative_to(pathlib.Path.cwd())}")
    return 0


if __name__ == "__main__":
    import sys
    sys.exit(main())
