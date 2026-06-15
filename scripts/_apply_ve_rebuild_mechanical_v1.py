"""_apply_ve_rebuild_mechanical_v1.py (2026-06-15) — mechanical rebuild of ve_lexical fields
VE 1,2,3,5,6,7,8,13 for every active term-in-verse, STRICTLY per research/VE-lexical/01b §1d.

Discipline (01b): assign only where the signal is self-contained; where attachment/subject can't be
confirmed mechanically, emit UNRESOLVED (the backtrack worklist) — never guess. Absence of a row =
NONE/not-stated (present-only). Every assigned row's `notes` cites the signal that forced it.

Attachment proxy: the "term neighbourhood" = context_before + target_word + context_after (~9 words
around the span). Signal in neighbourhood => attached (assign); signal only elsewhere in verse =>
UNRESOLVED; no signal => NONE.

  python scripts/_apply_ve_rebuild_mechanical_v1.py --dry-run
  python scripts/_apply_ve_rebuild_mechanical_v1.py --live
"""
import argparse, os, re, sqlite3, sys
from collections import Counter, defaultdict
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "analytics"))
import morph_util  # noqa: E402
sys.stdout.reconfigure(encoding="utf-8")
DB = os.path.join("database", "bible_research.db")
STAMP = "ve-rebuild-mechanical-v1-20260615"
PROV = "mechanical_v1"

# ---- signal-lists, transcribed VERBATIM from 01b §1d (iteration-1 seeds) ----
LOC_SEAT = ["heart", "soul", "mind", "spirit", "conscience", "flesh"]
LOC_BODY = ["eyes", "ears", "neck", "shoulder", "hand", "lips", "members", "back"]
LOC_TIER = {"spirit": "T2.1.1", "soul": "T2.2.1", "heart": "T2.3.1", "mind": "T2.4.1",
            "conscience": "T2.5.1", "flesh": "T2.6.1"}
ORIG_WITHIN = ["within", "internal", "own", "self"]
ORIG_BESTOWED = ["give", "pour", "fill", "grant", "show"]      # → bestowed-by-God (needs subject)
ORIG_RECEIVED = ["from"]                                       # "from"+source → received (needs source)
FACULTY = {
    "perception": ["see", "hear", "behold", "eyes", "ears"],
    "cognition": ["know", "understand", "consider", "counsel", "wisdom"],
    "memory": ["remember", "forget"],
    "volition": ["will", "choose", "ask"],
    "affect": ["fear", "joy", "sorrow", "longing", "zeal", "delight"],
    "moral_evaluation": ["justice", "judge", "search"],
    "conscience": ["conscience", "guilt", "integrity"],
}
FACULTY_TIER = {"perception": "T3.1", "cognition": "T3.2", "memory": "T3.3", "volition": "T3.6",
                "affect": "T3.4", "moral_evaluation": "T3.8", "conscience": "T3.9"}
DIVINE_WORDS = ["lord", "god", "almighty", "yhwh"]
DIVINE_PHRASE = ["holy one", "holy spirit"]
DIVINE_POSSESS = ["of god", "god's", "of the lord", "lord's", "of the almighty"]
REL_DIR = ["to", "toward", "from", "for", "against", "before", "into", "upon"]
REL_VERB = ["give", "show", "serve", "seek", "deliver", "call", "choose", "forsake", "covenant"]

_SUFFIX = r"(?:s|es|ed|ing|d|n|en)?"


def _rx(word):
    if " " in word:
        return re.compile(r"\b" + re.escape(word) + r"\b", re.I)
    return re.compile(r"\b" + re.escape(word) + _SUFFIX + r"\b", re.I)


_RX = {w: _rx(w) for w in set(LOC_SEAT + LOC_BODY + ORIG_WITHIN + ORIG_BESTOWED + ORIG_RECEIVED
                              + sum(FACULTY.values(), []) + DIVINE_WORDS + DIVINE_PHRASE
                              + DIVINE_POSSESS + REL_DIR + REL_VERB)}


def hits(words, text):
    """listed words whose regex matches text (case-insensitive)."""
    t = text or ""
    return [w for w in words if _RX[w].search(t)]


def derive(u, coterms):
    """u = unit dict; coterms = list of co-occurring (mti_term_id, translit, cluster) at same ref.
    returns list of (ve_nr, ve_label, tier, value, note)."""
    out = []
    vtext = u["vtext"] or ""
    gloss = (u["gloss"] or "")
    nb = " ".join(x for x in [u["cb"], u["tw"], u["ca"]] if x)  # neighbourhood window

    # VE1 sense — per-occurrence STEP subgloss (mechanical floor)
    sub = (u["sub"] or "").strip()
    if sub:
        out.append((1, "sense", "T7.1.3", sub, "STEP per-occurrence subgloss"))
    else:
        out.append((1, "sense", "T7.1.3", "UNRESOLVED", "no STEP subgloss source"))

    # VE2 type — morphology POS (precede; sense-supersede deferred)
    cat = morph_util.morph_category(u["morph"])
    tmap = {"verb": "action", "noun": "status", "adjective": "quality"}
    if cat in tmap:
        out.append((2, "type", "T1.2.1", tmap[cat], f"morph POS={cat}"))
    elif u["morph"]:
        out.append((2, "type", "T1.2.1", "UNRESOLVED", f"POS={cat} not act/status/quality"))
    else:
        out.append((2, "type", "T1.2.1", "UNRESOLVED", "no morph"))

    # VE3 compound — web-edge per co-occurring term (present-only)
    seen = set()
    for mid, tr, cc in coterms:
        if mid is None or mid == u["mti_term_id"] or mid in seen:
            continue
        seen.add(mid)
        if cc == "T2":
            out.append((3, "compound", "T1.2.2", f"{tr}(T2-qualifier)", "co-occurs in verse"))
        else:
            out.append((3, "compound", "T6.1.1", f"{tr}({cc})", "co-occurs in verse"))

    # VE5 location — co-occurrence (01b location rule: no attachment gate), multi
    for w in hits(LOC_SEAT, vtext):
        out.append((5, "location", LOC_TIER[w], w, f"seat word '{w}' in verse"))
    for w in hits(LOC_BODY, vtext):
        out.append((5, "location", "T2.6.1", f"body-part:{w}", f"body word '{w}' in verse"))

    # VE6 origin — internal cue assignable; bestowed/received need subject/source -> UNRESOLVED
    win = hits(ORIG_WITHIN, nb)
    best = hits(ORIG_BESTOWED, nb)
    recv = hits(ORIG_RECEIVED, nb)
    if win and not (best or recv):
        out.append((6, "origin", "T2.9.1", "within-person", f"internal cue '{','.join(win)}' in neighbourhood"))
    elif win and (best or recv):
        out.append((6, "origin", "T2.9.1", "UNRESOLVED", f"conflicting cues: within={win} bestowed/received={best+recv}"))
    elif best or recv:
        out.append((6, "origin", "T2.9.1", "UNRESOLVED", f"source cue '{','.join(best+recv)}' present; subject/source attachment unconfirmed"))
    # else not-stated -> no row

    # VE7 faculty — R1 direct (gloss) / R2 indirect (neighbourhood) / R4 unresolved / R5 none
    assigned = []
    for fac, words in FACULTY.items():
        g = hits(words, gloss)
        n = hits(words, nb)
        if g:
            assigned.append((fac, f"direct(gloss): {','.join(g)}"))
        elif n:
            assigned.append((fac, f"indirect(neighbourhood): {','.join(n)}"))
    if assigned:
        for fac, note in assigned:
            out.append((7, "faculty", FACULTY_TIER[fac], fac, note))
    else:
        # any faculty word in the verse but not attributable -> UNRESOLVED (R4)
        verse_hits = {fac: hits(words, vtext) for fac, words in FACULTY.items()}
        present = {f: h for f, h in verse_hits.items() if h}
        if present:
            note = "; ".join(f"{f}:{','.join(h)}" for f, h in present.items())[:200]
            out.append((7, "faculty", "T3.0", "UNRESOLVED", f"faculty word(s) in verse not attributable to term: {note}"))
        # else NONE -> no row

    # VE8 attributed-to-God — possessive adjacent -> yes; any divine word -> UNRESOLVED; none -> no
    poss = hits(DIVINE_POSSESS, nb)
    div_verse = hits(DIVINE_WORDS, vtext) + hits(DIVINE_PHRASE, vtext)
    if poss:
        out.append((8, "attributed_to_God", "T0.1.2", "yes", f"divine possessor '{','.join(poss)}' adjacent"))
    elif div_verse:
        out.append((8, "attributed_to_God", "T0.1.2", "UNRESOLVED", f"divine word '{','.join(div_verse)}' present; subject/possessor unconfirmed"))
    # else no -> no row

    # VE13 relational — directional/relational node in neighbourhood -> assign; verse-only -> UNRESOLVED
    rel_nb = hits(REL_DIR, nb) + hits(REL_VERB, nb)
    if rel_nb:
        for w in dict.fromkeys(rel_nb):
            out.append((13, "relational_implication", "T1.1.3", w, "directional/relational node in neighbourhood"))
    else:
        rel_v = hits(REL_DIR, vtext) + hits(REL_VERB, vtext)
        if rel_v:
            out.append((13, "relational_implication", "T1.1.3", "UNRESOLVED",
                        f"relational node '{','.join(dict.fromkeys(rel_v))}' in verse, not attached to term"))
        # else NONE -> no row
    return out


def main():
    ap = argparse.ArgumentParser()
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--dry-run", action="store_true"); g.add_argument("--live", action="store_true")
    a = ap.parse_args()
    conn = sqlite3.connect(DB, timeout=600); conn.row_factory = sqlite3.Row
    cur = conn.cursor()

    rows = cur.execute("""
        SELECT vc.id vcid, vc.verse_record_id vrid, vc.mti_term_id mti_term_id,
               vr.reference ref, vr.verse_text vtext, vr.target_word tw,
               vr.context_before cb, vr.context_after ca, vr.morph_code morph,
               vr.transliteration translit, m.gloss gloss, m.cluster_code cc,
               (SELECT l.step_subgloss_label FROM wa_verse_term_links l
                  WHERE l.verse_id = vr.id AND l.term_inv_id = vr.term_inv_id LIMIT 1) sub
        FROM verse_context vc
        JOIN wa_verse_records vr ON vr.id = vc.verse_record_id AND COALESCE(vr.delete_flagged,0)=0
        LEFT JOIN mti_terms m ON m.id = vc.mti_term_id
        WHERE COALESCE(vc.delete_flagged,0)=0
    """).fetchall()
    units = [dict(r) for r in rows]
    print(f"units loaded: {len(units):,}")

    # reference -> co-occurring terms (for VE3)
    refmap = defaultdict(list)
    for u in units:
        refmap[u["ref"]].append((u["mti_term_id"], u["translit"], u["cc"]))
    for k in refmap:
        seen = set(); uniq = []
        for t in refmap[k]:
            if t[0] not in seen:
                seen.add(t[0]); uniq.append(t)
        refmap[k] = uniq

    inserts = []
    for u in units:
        inserts.extend((u["vcid"], *row) for row in derive(u, refmap[u["ref"]]))

    # ---- distribution report ----
    by_ve = defaultdict(Counter)
    rowcount = Counter()
    for (_vc, ve_nr, _lab, _tier, val, _note) in inserts:
        rowcount[ve_nr] += 1
        key = "UNRESOLVED" if val == "UNRESOLVED" else (val if ve_nr in (2, 6, 8) else "<value>")
        by_ve[ve_nr][key] += 1
    LBL = {1: "sense", 2: "type", 3: "compound", 5: "location", 6: "origin", 7: "faculty",
           8: "attributed_to_God", 13: "relational"}
    print(f"\ntotal ve_lexical rows to write: {len(inserts):,}\n")
    print("VE   field               rows     breakdown")
    for ve in [1, 2, 3, 5, 6, 7, 8, 13]:
        unres = by_ve[ve].get("UNRESOLVED", 0)
        extra = ", ".join(f"{k}={v}" for k, v in sorted(by_ve[ve].items()) if k != "<value>")
        print(f"VE{ve:<2} {LBL[ve]:<18} {rowcount[ve]:>7,}   UNRESOLVED={unres:,}  {extra}")

    # ---- samples: 2 per field with the cited note ----
    print("\n--- samples (value · note) ---")
    shown = defaultdict(int)
    vc_ref = {u["vcid"]: (u["ref"], u["gloss"]) for u in units}
    for (vc, ve_nr, lab, tier, val, note) in inserts:
        if shown[ve_nr] < 2:
            ref, gl = vc_ref[vc]
            print(f"  VE{ve_nr} {ref} '{gl}' :: {val}  [{note[:70]}]")
            shown[ve_nr] += 1

    if a.live:
        n0 = cur.execute("SELECT COUNT(*) FROM ve_lexical").fetchone()[0]
        if n0:
            print(f"\nABORT: ve_lexical is not empty ({n0:,} rows). Expected 0 for a clean rebuild.")
            return
        cur.executemany(
            "INSERT INTO ve_lexical (verse_context_id, ve_nr, ve_label, related_tier, value, notes, source_provenance, created_at) "
            "VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
            [(vc, ve, lab, tier, val, note, PROV, STAMP) for (vc, ve, lab, tier, val, note) in inserts])
        conn.commit()
        print(f"\nLIVE: inserted {len(inserts):,} ve_lexical rows.")
    else:
        print("\nDRY-RUN — no writes.")


if __name__ == "__main__":
    main()
