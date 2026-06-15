"""_apply_faculty_rederive_v1.py (2026-06-15) — re-derive VE7 (faculty) against the actual faculty
signal-list IN THE CONTEXT OF THE VERSE, replacing the previous GENERIC faculty statements.

Rule (present-only, not imputed): a faculty is assigned to a term-in-verse only if one of its signal words
actually occurs (word-boundary) in (a) the term's gloss [DIRECT] or (b) the verse text [INDIRECT].
One ve_lexical row per faculty actually signalled; notes record the matched word(s) + direct/indirect.
This is ITERATION 1 for researcher review — signal-lists are seed lists, will be refined.

  python scripts/_apply_faculty_rederive_v1.py --dry-run
  python scripts/_apply_faculty_rederive_v1.py --live
"""
import argparse, os, re, sqlite3, sys
sys.stdout.reconfigure(encoding="utf-8")
DB = os.path.join("database", "bible_research.db")
STAMP = "faculty-rule-v1-20260615"

# faculty -> (tier, [signal word-stems]).  Conservative seed lists; word-boundary matched.
FACULTIES = {
    "perception": ("T3.1", ["see", "saw", "seen", "sees", "seeing", "look", "looked", "behold", "beheld",
                            "eye", "eyes", "hear", "heard", "hears", "hearing", "ear", "ears", "watch",
                            "gaze", "perceive", "perceived", "sight", "witness"]),
    "cognition": ("T3.2", ["know", "knew", "known", "knows", "knowing", "understand", "understood",
                           "understanding", "consider", "considered", "counsel", "wisdom", "wise",
                           "knowledge", "thought", "thoughts", "think", "discern", "discerned", "ponder",
                           "comprehend"]),
    "memory": ("T3.3", ["remember", "remembered", "remembrance", "forget", "forgot", "forgotten",
                        "mindful", "recall", "memorial"]),
    "affect": ("T3.4", ["fear", "feared", "afraid", "joy", "joyful", "rejoice", "rejoiced", "glad",
                        "gladness", "sorrow", "grief", "grieve", "grieved", "mourn", "mourning", "zeal",
                        "zealous", "delight", "delighted", "love", "loved", "hate", "hated", "anger",
                        "angry", "wrath", "anguish", "distress", "comfort", "comforted", "pity",
                        "compassion", "weep", "wept", "dread", "terror", "desire", "longing"]),
    "creativity": ("T3.5", ["create", "created", "fashion", "fashioned", "devise", "devised", "design",
                            "imagine", "invent"]),
    "volition": ("T3.6", ["willing", "choose", "chose", "chosen", "resolve", "resolved", "determine",
                          "determined", "intend", "decide", "decided", "refuse", "refused", "consent",
                          "vow", "vowed"]),
    "agency": ("T3.7", ["accomplish", "perform", "performed", "strive", "strove", "labor", "labored",
                        "endeavour", "endeavor"]),
    "moral_evaluation": ("T3.8", ["justice", "judge", "judged", "judgment", "righteous", "righteousness",
                                  "wicked", "wickedness", "condemn", "condemned", "upright", "blame",
                                  "worthy", "approve"]),
    "conscience": ("T3.9", ["conscience", "guilt", "guilty", "integrity", "blameless", "innocent",
                            "innocence", "shame", "ashamed", "convict"]),
    "relational_capacity": ("T3.11", ["fellowship", "covenant", "friend", "neighbor", "neighbour",
                                      "reconcile", "reconciled", "communion", "devotion"]),
}
_RX = {f: re.compile(r"\b(" + "|".join(re.escape(w) for w in words) + r")\b", re.I) for f, (t, words) in FACULTIES.items()}


def main():
    ap = argparse.ArgumentParser()
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--dry-run", action="store_true"); g.add_argument("--live", action="store_true")
    a = ap.parse_args()
    conn = sqlite3.connect(DB, timeout=600); conn.row_factory = sqlite3.Row
    cur = conn.cursor()

    # the analysed term-in-verses (those with ve_lexical rows): their verse text + term gloss
    rows = cur.execute("""
        SELECT DISTINCT vc.id vcid, vr.verse_text vtext, m.gloss gloss
        FROM ve_lexical x
        JOIN verse_context vc ON vc.id = x.verse_context_id
        JOIN wa_verse_records vr ON vr.id = vc.verse_record_id
        LEFT JOIN mti_terms m ON m.id = vc.mti_term_id
        WHERE COALESCE(x.delete_flagged,0)=0
    """).fetchall()

    inserts = []
    for r in rows:
        vtext = r["vtext"] or ""
        gloss = r["gloss"] or ""
        for fac, (tier, _w) in FACULTIES.items():
            rx = _RX[fac]
            d = rx.findall(gloss)
            i = rx.findall(vtext)
            if d or i:
                src = "direct(gloss)" if d else "indirect(verse)"
                hits = ",".join(sorted(set([h.lower() for h in (d or i)])))[:60]
                inserts.append((r["vcid"], tier, fac, f"{src}: {hits}"))

    # current generic VE7 rows to retire
    old = [r[0] for r in cur.execute("SELECT id FROM ve_lexical WHERE ve_nr=7 AND COALESCE(delete_flagged,0)=0")]
    print(f"analysed term-in-verses scanned: {len(rows):,}")
    print(f"OLD generic VE7 rows to soft-delete: {len(old):,}")
    print(f"NEW rule-derived VE7 rows: {len(inserts):,}")
    from collections import Counter
    print("  new faculty distribution:", dict(Counter(i[2] for i in inserts)))
    if a.live:
        for k in range(0, len(old), 400):
            ch = old[k:k+400]
            cur.execute(f"UPDATE ve_lexical SET delete_flagged=1 WHERE id IN ({','.join('?'*len(ch))})", ch)
        cur.executemany(
            "INSERT INTO ve_lexical (verse_context_id, ve_nr, ve_label, related_tier, value, notes, source_provenance, created_at) "
            "VALUES (?, 7, 'faculty', ?, ?, ?, 'rule_v1', ?)",
            [(vcid, tier, fac, note, STAMP) for (vcid, tier, fac, note) in inserts])
        conn.commit()
        print(f"LIVE: retired {len(old):,} generic · inserted {len(inserts):,} rule-derived VE7 rows")
    else:
        print("DRY-RUN — no writes.")


if __name__ == "__main__":
    main()
