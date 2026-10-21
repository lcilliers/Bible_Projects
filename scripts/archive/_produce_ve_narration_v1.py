"""_produce_ve_narration_v1.py (2026-06-15) — compose the TEMPLATED NARRATION for a term-in-verse
from its ve_lexical fields (+ the mode column). Read-only — the narration is a DETERMINISTIC VIEW of
the findings (01b §1f), not authored prose.

Rules (researcher, 2026-06-15): every element present is included; multiples render as multiples;
an UNRESOLVED value renders as a [field: UNRESOLVED] placeholder; NONE/SILENT are not recorded so
are naturally absent.

  python scripts/_produce_ve_narration_v1.py --refs "Psa 139:23,2Sa 1:9,..."
  python scripts/_produce_ve_narration_v1.py --first 1
"""
import argparse, os, sqlite3, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "analytics"))
import morph_util  # noqa: E402
sys.stdout.reconfigure(encoding="utf-8")
DB = os.path.join("database", "bible_research.db")


def _join(vals):
    vals = list(dict.fromkeys(vals))
    if len(vals) == 1:
        return vals[0]
    return ", ".join(vals[:-1]) + " and " + vals[-1]


def narrate(unit, lex):
    """unit: dict(ref, translit, gloss, morph, stem); lex: dict ve_nr -> list of values."""
    def vals(nr):
        return lex.get(nr, [])

    def unresolved(nr):
        return any(v == "UNRESOLVED" for v in vals(nr))

    def resolved(nr):
        return [v for v in vals(nr) if v != "UNRESOLVED"]

    clauses = []
    # head
    head = f"In {unit['ref']}, {unit['translit']} (“{unit['gloss']}”)"
    # 1 sense
    if unresolved(1):
        clauses.append("carries an [sense: UNRESOLVED]")
    elif resolved(1):
        clauses.append(f"carries the sense “{_join(resolved(1))}”")
    # 2 type
    if resolved(2):
        clauses.append(f"functioning as a {_join(resolved(2))}")
    elif unresolved(2):
        clauses.append("functioning as an [type: UNRESOLVED]")
    # 4 mode (column, bedrock)
    mode = morph_util.morph_readable(unit["morph"], unit["stem"])
    if unit["morph"]:
        clauses.append(f"in {mode} form")
    # 5 location
    if resolved(5):
        clauses.append(f"located in the {_join(resolved(5))}")
    # 6 origin
    if resolved(6):
        clauses.append(f"originating {_join(resolved(6))}")
    elif unresolved(6):
        clauses.append("with [origin: UNRESOLVED]")
    # 7 faculty
    if resolved(7):
        clauses.append(f"engaging the {_join(resolved(7))} faculty")
    elif unresolved(7):
        clauses.append("engaging a [faculty: UNRESOLVED]")
    # 8 attributed-to-God
    if "yes" in vals(8):
        clauses.append("attributed to God")
    elif unresolved(8):
        clauses.append("[attributed-to-God: UNRESOLVED]")
    # 3 compound
    if resolved(3):
        clauses.append(f"combining with {_join(resolved(3))}")
    # 13 relational
    if resolved(13):
        clauses.append(f"directed {_join(resolved(13))}")
    elif unresolved(13):
        clauses.append("with a [relational: UNRESOLVED]")
    return head + " " + ", ".join(clauses) + "."


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--refs", help="comma-separated references")
    ap.add_argument("--first", type=int, default=0, help="first N units by verse_context id")
    a = ap.parse_args()
    conn = sqlite3.connect(DB, timeout=600); conn.row_factory = sqlite3.Row
    cur = conn.cursor()

    if a.refs:
        refs = [r.strip() for r in a.refs.split(",") if r.strip()]
        q = ("SELECT vc.id vcid, vr.reference ref, vr.transliteration translit, m.gloss gloss, "
             "vr.morph_code morph, vr.stem stem FROM verse_context vc "
             "JOIN wa_verse_records vr ON vr.id=vc.verse_record_id AND COALESCE(vr.delete_flagged,0)=0 "
             "LEFT JOIN mti_terms m ON m.id=vc.mti_term_id "
             "WHERE COALESCE(vc.delete_flagged,0)=0 AND vr.reference IN (%s) ORDER BY vr.reference, vr.id"
             % ",".join("?" * len(refs)))
        units = cur.execute(q, refs).fetchall()
    else:
        units = cur.execute(
            "SELECT vc.id vcid, vr.reference ref, vr.transliteration translit, m.gloss gloss, "
            "vr.morph_code morph, vr.stem stem FROM verse_context vc "
            "JOIN wa_verse_records vr ON vr.id=vc.verse_record_id AND COALESCE(vr.delete_flagged,0)=0 "
            "LEFT JOIN mti_terms m ON m.id=vc.mti_term_id "
            "WHERE COALESCE(vc.delete_flagged,0)=0 ORDER BY vc.id LIMIT ?", (a.first or 1,)).fetchall()

    for u in units:
        lex = {}
        for r in cur.execute("SELECT ve_nr, value FROM ve_lexical WHERE verse_context_id=? AND COALESCE(delete_flagged,0)=0 ORDER BY ve_nr, id", (u["vcid"],)):
            lex.setdefault(r["ve_nr"], []).append(r["value"])
        print(narrate(dict(u), lex))
        print()


if __name__ == "__main__":
    main()
