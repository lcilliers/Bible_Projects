"""_check_ve_seat_completeness.py — standing guard: is the location SEAT vocabulary complete?

Read-only. Scans every lemma that appears as a tagged term in the corpus, flags those whose lexicon
definition denotes an inner-being SEAT/organ, and reports any that are NOT in the engine's SEAT map.
This is the check the 2026-06-18 review found missing — the SEAT list was an 8-lemma stub ("expand later")
and nothing verified it against the actual Hebrew/Greek seat vocabulary. Run it after any engine change
and as part of the VE audit. Non-zero exit if a seat-denoting lemma is unmapped (so CI/audit can gate).

  python scripts/_check_ve_seat_completeness.py
"""
import os, re, sqlite3, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__)))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "analytics"))
import _ve_engine_v2 as eng

DB = os.path.join("database", "bible_research.db")
# words whose gloss denotes a constitutional SEAT/organ (not a faculty-act like 'remember'/'discern'/'will').
SEAT_GLOSS = re.compile(r"\b(heart|soul|spirit|mind|conscience|bowel|kidney|reins|inward|inmost|liver|"
                        r"flesh|belly|womb|breath|midst|entrails|viscera|breast)\b", re.I)
# faculty-act / non-seat senses that the keyword net catches but are NOT seats (exclude from the flag).
FACULTY_ACT = re.compile(r"\b(remember|recall|discern|understand|knowledge|will\b|decide|want|wish|prophes|"
                         r"return|grace|sin\b|forgive|repent|persever|covenant|love|merc|eye|house|poor)\b", re.I)


def main():
    c = sqlite3.connect(DB); c.row_factory = sqlite3.Row
    rows = c.execute("""SELECT DISTINCT m.strongs_number sn FROM mti_terms m
        JOIN verse_context vc ON vc.mti_term_id=m.id AND COALESCE(vc.delete_flagged,0)=0""").fetchall()
    unmapped = []
    for r in rows:
        b = re.match(r"([HG]\d+)", r["sn"] or "")
        if not b:
            continue
        base = b.group(1)
        canon = eng._canon(base)
        lx = c.execute("SELECT medium_def FROM lexicon WHERE strong=?", (base,)).fetchone()
        md = (lx["medium_def"] if lx else "") or ""
        first = re.split(r"[\n;]", md)[0].strip()
        # seat-denoting gloss, not already mapped, and not a faculty-act false-positive
        if SEAT_GLOSS.search(md) and canon not in eng.SEAT and not FACULTY_ACT.search(first):
            units = c.execute("""SELECT COUNT(DISTINCT vc.id) FROM verse_context vc JOIN mti_terms m
                ON m.id=vc.mti_term_id WHERE COALESCE(vc.delete_flagged,0)=0 AND m.strongs_number LIKE ?""",
                (base + "%",)).fetchone()[0]
            unmapped.append((units, base, first[:60]))
    unmapped.sort(reverse=True)
    print(f"SEAT map currently holds {len(set(eng.SEAT))} lemmas -> levels {sorted(set(eng.SEAT.values()))}")
    if unmapped:
        print(f"\n⚠ {len(unmapped)} seat-denoting lemma(s) present in the corpus but NOT in SEAT "
              f"(review — add to SEAT or confirm non-seat):")
        print(f'{"units":>6}  {"strong":7} gloss')
        for u, s, g in unmapped:
            print(f"{u:6}  {s:7} {g}")
        print("\nNOTE: some may be genuine non-seats the keyword net caught — review each, don't blind-add.")
        return 1
    print("\nOK — every seat-denoting lemma in the corpus is mapped in SEAT.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
