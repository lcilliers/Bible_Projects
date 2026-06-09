"""_apply_l2_write_refit.py — L2 writer on the REFIT basis (wa-catalogue-refit-two-layer / verse-extraction
spec). For a cluster's OWN terms, rewrites the verse-level findings with: sense (T7.1) · type (T1.2) · mode
(T1.4) · FACULTY per-term multi-select derived from the term's meaning (T3.x.1, the fix) · CONSTITUTIONAL
LOCATION multi-level from the verse text (T2.x.1) · CO-OCCURRENCE array (T6.1.1). Read-layer fields (origin,
attributed_to_God, purpose, response, produces…) are NOT asserted here — they are the read layer. Clears the
cluster's own prior l2_mechanical findings first (reversible). Faculty/location are closed vocabularies;
NONE/SILENT first-class (state-not-induce).

Usage:  python scripts/_apply_l2_write_refit.py --cluster M15 --dry-run|--live --out <file>.md
"""
import argparse, os, re, sqlite3, sys
from collections import Counter
sys.stdout.reconfigure(encoding="utf-8")
DB = os.path.join("database", "bible_research.db")
POSm = {"V": "ACTION", "N": "STATUS", "A": "QUALITY"}
STEM_MARK = re.compile(r"\((Qal|Niphal|Piel|Pual|Hiphil|Hophal|Hithpael)\)", re.I)
SUBSHADE = re.compile(r"\d+[a-z]\d+\)")
THREAT = re.compile(r"\b(enemy|enemies|sword|army|slay|kill|death|die|nations|destroy|flee|afraid of)\b", re.I)
NEG = re.compile(r"\b(do not fear|fear not|be not afraid|not be afraid|no fear)\b", re.I)
T_LEX, T_KIND, T_MODE, T_COOC = 395, 239, 245, 369
# faculty obs_id -> meaning-keyword stems (per-term, from the TERM's gloss)
FACULTY = {
    294: ["know", "knew", "understand", "discern", "wisdom", "wise", "insight", "prudent", "comprehend", "sensible", "skill", "ponder", "intellig", "reason", "perceive and"],  # cognition
    300: ["fear", "dread", "terror", "afraid", "love", "hate", "joy", "glad", "grief", "sorrow", "anger", "wrath", "delight", "anxiety", "distress", "compassion", "pity", "jealous", "envy", "feel", "grieve", "rejoice", "mourn", "anguish"],  # affect
    306: ["will,", "to will", "choose", "chose", "choice", "decide", "determine", "intend", "intent", "purpose", "resolve", "consent", "refuse", "wish", "desire"],  # volition
    297: ["remember", "recall", "memor", "forget", "mindful", "recollect"],  # memory
    291: ["see ", "saw", "hear", "behold", "sight", "taste", "smell", "observe"],  # perception
    309: ["accomplish", "execute", "carry out", "bring about", "initiate"],  # agency (narrow; avoid 'to make afraid' etc.)
    312: ["righteous", "just", "judge", "evaluat", "wicked", "holy", "pure", "moral", "upright", "condemn", "guilt", "iniquit", "transgress", "sin"],  # moral-evaluation
    315: ["conscience", "convict", "shame", "remorse", "contrit"],  # conscience
    321: ["fellowship", "neighbour", "neighbor", "brother", "covenant", "companion", "kinsman"],  # relational
    303: ["imagin", "create", "devise", "invent", "conceiv", "fashion"],  # creativity
}
# location obs_id -> verse-text keyword
LOCATION = {260: ["spirit"], 264: ["soul"], 267: ["heart"], 270: ["mind"],
            276: ["bowel", "kidney", "liver", "breast", "belly", "womb", "inward part"]}


def pos_of(m):
    if not m: return None
    p = m[1] if m[0] == "H" and len(m) > 1 else (m[2] if m[0] == "G" and len(m) > 2 and m[1] == "-" else m[0])
    return POSm.get(p)


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--cluster", required=True)
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--dry-run", action="store_true"); g.add_argument("--live", action="store_true")
    ap.add_argument("--out", required=True); a = ap.parse_args()
    conn = sqlite3.connect(DB); conn.row_factory = sqlite3.Row; c = conn.cursor(); c2 = conn.cursor()
    now = c.execute("SELECT datetime('now')").fetchone()[0]
    clus = {r["id"]: r["cluster_code"] for r in c.execute("SELECT id, cluster_code FROM mti_terms WHERE COALESCE(delete_flagged,0)=0 AND cluster_code NOT IN ('T2','FLAG') AND cluster_code IS NOT NULL")}

    # cluster own terms: gloss text (for faculty) + sense branches (for sense/mode)
    meta = {}
    for r in c.execute("SELECT m.id mid, m.transliteration tl, m.gloss gloss, ti.meaning meaning, ti.parsed_meaning_id pmid "
                       "FROM mti_terms m LEFT JOIN wa_term_inventory ti ON ti.strongs_number=m.strongs_number "
                       "AND COALESCE(ti.delete_flagged,0)=0 WHERE m.cluster_code=? AND COALESCE(m.delete_flagged,0)=0 GROUP BY m.id", (a.cluster,)):
        fac_gl = " ".join(filter(None, [r["gloss"], r["meaning"]])).lower()
        br = {}
        if r["pmid"]:
            st = c2.execute("SELECT group_concat(sense_text,'\n') s FROM wa_meaning_sense WHERE parsed_meaning_id=?", (r["pmid"],)).fetchone()["s"] or ""
            fac_gl += " " + st.lower()[:200]  # head ~200 chars of the sense (core definition; avoids deep-example noise)
            marks = list(STEM_MARK.finditer(st))
            for i, m in enumerate(marks):
                end = marks[i + 1].start() if i + 1 < len(marks) else len(st)
                seg = st[m.end():end]
                br[m.group(1).capitalize()] = (re.split(r"\s\d+\)\s", re.sub(r"\s+", " ", seg).strip().strip(":"))[0][:80], len(SUBSHADE.findall(seg)))
            if not br:
                br["_"] = (re.sub(r"\s+", " ", st).strip()[:80], 1)
        # derive faculties from the head gloss
        facs = [oid for oid, kws in FACULTY.items() if any(k in fac_gl for k in kws)]
        meta[r["mid"]] = {"tl": r["tl"], "br": br, "facs": facs}

    mids = list(meta); qm = ",".join("?" * len(mids))
    # CLEAR prior l2_mechanical findings for these own terms
    old = [r[0] for r in c.execute(f"SELECT id FROM finding WHERE provenance='l2_mechanical' AND level='VERSE' AND mti_term_id IN ({qm})", mids)]
    rows = c.execute(f"SELECT vc.id vcid, vc.mti_term_id mid, vr.id vrid, vr.stem stem, vr.morph_code morph, "
                     f"vr.reference ref, vr.verse_text txt FROM verse_context vc JOIN wa_verse_records vr ON vr.id=vc.verse_record_id "
                     f"WHERE COALESCE(vc.delete_flagged,0)=0 AND vc.mti_term_id IN ({qm})", mids).fetchall()
    # co-occurring in-scope terms per reference
    refs = list({r["ref"] for r in rows}); qr = ",".join("?" * len(refs))
    cooc = {}
    for r in c.execute(f"SELECT vr.reference ref, m.transliteration tl, m.cluster_code cc FROM wa_verse_records vr "
                       f"JOIN mti_terms m ON m.id=vr.mti_term_id WHERE COALESCE(vr.delete_flagged,0)=0 AND vr.reference IN ({qr}) "
                       f"AND m.cluster_code NOT IN ('T2','FLAG') AND m.cluster_code IS NOT NULL", refs):
        cooc.setdefault(r["ref"], []).append(f"{r['tl']}({r['cc']})")

    nfind = Counter(); facc = Counter(); locc = Counter(); nverse = 0; samples = []
    if a.live and old:
        qo = ",".join("?" * len(old))
        c.execute(f"DELETE FROM finding_question_link WHERE finding_id IN ({qo})", old)
        c.execute(f"DELETE FROM finding WHERE id IN ({qo})", old)
    for r in rows:
        d = meta[r["mid"]]; stem = r["stem"] or "_"; txt = r["txt"] or ""
        ttype = pos_of(r["morph"]) or ("STATUS" if not r["stem"] else "?")
        seg = d["br"].get(stem) or d["br"].get("_") or ("", 1)
        lexical, nsub = seg
        tri = "ACCEPT" if (nsub <= 1 or THREAT.search(txt) or NEG.search(txt)) else "ESCALATE"
        # faculties (term-derived); locations (verse-text)
        facs = d["facs"]
        locs = [oid for oid, kws in LOCATION.items() if any(re.search(r"\b" + k, txt, re.I) for k in kws)]
        tf = [(T_LEX, lexical or "", "STATED_UNRESOLVED" if tri == "ESCALATE" else ("ANSWERED" if lexical else "STATED_UNRESOLVED")),
              (T_KIND, ttype, "ANSWERED"),
              (T_MODE, stem if r["stem"] else "n/a (noun)", "ANSWERED" if r["stem"] else "STATED_SILENT")]
        for oid in facs:
            tf.append((oid, "engaged", "ANSWERED")); facc[oid] += 1
        for oid in locs:
            tf.append((oid, "located here", "ANSWERED")); locc[oid] += 1
        if not locs:
            tf.append((276, "no constitutional locus named", "STATED_SILENT"))
        others = [x for x in cooc.get(r["ref"], []) if not x.startswith(d["tl"] + "(")]
        tf.append((T_COOC, "; ".join(others) if others else "none", "ANSWERED" if others else "STATED_SILENT"))
        nverse += 1
        if a.live:
            c.execute("UPDATE verse_context SET thing_type=?, triage_status=?, meaning_provenance=?, flagged_for_review=? WHERE id=?",
                      (ttype, tri, "l2_refit", 1 if tri == "ESCALATE" else 0, r["vcid"]))
            for oid, val, st in tf:
                cur = c.execute("INSERT INTO finding (level, verse_context_id, mti_term_id, finding_value, finding_status, provenance, created_at, last_updated_date, delete_flagged) VALUES ('VERSE',?,?,?,?,?,?,?,0)",
                                (r["vcid"], r["mid"], val, st, "l2_mechanical", now, now))
                c.execute("INSERT INTO finding_question_link (finding_id, question_id, coverage, created_at, delete_flagged) VALUES (?,?,?,?,0)", (cur.lastrowid, oid, "full", now))
        for _o, _v, st in tf: nfind[st] += 1
        if len(samples) < 12:
            samples.append((r["ref"], d["tl"], ttype, stem, tri, [k for k in d["facs"]], locs, (lexical or "")[:34]))
    if a.live:
        conn.commit()

    FNAME = {291: "perception", 294: "cognition", 297: "memory", 300: "affect", 303: "creativity", 306: "volition", 309: "agency", 312: "moral-eval", 315: "conscience", 321: "relational"}
    LNAME = {260: "spirit", 264: "soul", 267: "heart", 270: "mind", 276: "body"}
    L = [f"# L2 refit — {'LIVE' if a.live else 'DRY-RUN'} — {a.cluster} (per-term faculty · multi-location · co-occurrence)", ""]
    L.append(f"**{nverse} term-in-verses · faculty per-term (term-derived) · cleared {len(old)} old findings.**")
    L.append("")
    L.append("**Faculty distribution (term-derived):** " + ", ".join(f"{FNAME[o]}:{n}" for o, n in facc.most_common()))
    L.append("\n**Location distribution:** " + (", ".join(f"{LNAME[o]}:{n}" for o, n in locc.most_common()) or "none"))
    L.append("\n**Finding status:** " + ", ".join(f"{k}:{v}" for k, v in nfind.most_common()))
    L.append("\n## Sample")
    L.append("| Ref | term | type | stem | triage | faculties | locations | lexical |"); L.append("|---|---|---|---|---|---|---|---|")
    for ref, tl, tt, stem, tri, facs, locs, lex in samples:
        L.append(f"| {ref} | {tl} | {tt} | {stem} | {tri} | {','.join(FNAME[f] for f in facs) or '—'} | {','.join(LNAME[l] for l in locs) or '—'} | {lex} |")
    os.makedirs(os.path.dirname(a.out), exist_ok=True)
    open(a.out, "w", encoding="utf-8").write("\n".join(L))
    print(f"{'LIVE' if a.live else 'DRY'}: {a.cluster} {nverse} term-verses; cleared {len(old)}; "
          f"faculties {dict((FNAME[o],n) for o,n in facc.items())}; wrote {a.out}")


if __name__ == "__main__":
    main()
