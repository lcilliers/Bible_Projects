"""_apply_l2_write.py — the L2 WRITER (first version, mechanical-accept path). Per in-cluster term per verse:
mechanical pass (stem→sense-branch, type, faculty, locus) → triage → write the per-term TIER FINDINGS to the
universal `finding` table (level=VERSE, anchored on verse_context) + `finding_question_link`, and set
verse_context finding fields. STATE_SILENT recorded explicitly. Escalations written as STATED_UNRESOLVED +
flagged (API/researcher step not built). Surfaces OPEN Session B findings anchored to each verse.

Idempotent (skips verse_contexts already written, provenance='l2_mechanical'). Reversible (delete finding
rows where provenance='l2_mechanical'; null the verse_context fields).

Usage:  python scripts/_apply_l2_write.py --cluster M01 [--strongs H..,H..] --dry-run|--live --out <file>.md
"""
import argparse, os, re, sqlite3, sys
from collections import Counter
sys.stdout.reconfigure(encoding="utf-8")
DB = os.path.join("database", "bible_research.db")
POSm = {"V": "ACTION", "N": "STATUS", "A": "QUALITY"}
HEB_STEM = {"q": "Qal", "N": "Niphal", "p": "Piel", "P": "Pual", "h": "Hiphil", "H": "Hophal", "t": "Hithpael", "c": "Tiphil", "u": "Polpal"}
STEM_MARK = re.compile(r"\((Qal|Niphal|Piel|Pual|Hiphil|Hophal|Hithpael)\)", re.I)
SUBSHADE = re.compile(r"\d+[a-z]\d+\)")
THREAT = re.compile(r"\b(enemy|enemies|sword|army|armies|slay|kill|death|die|pursue|nations|destroy|siege|flee|afraid of)\b", re.I)
NEG = re.compile(r"\b(do not fear|fear not|be not afraid|not be afraid|no fear)\b", re.I)
LOCUS = [("heart", 267), ("mind", 270), ("bowel", 276), ("kidney", 276), ("inward", 276), ("breast", 276)]
# tier obs_ids
T_LEX, T_KIND, T_MODE, T_AFFECT, T_BODY = 395, 239, 245, 300, 276


def pos_of(m):
    if not m: return None
    p = m[1] if m[0] == "H" and len(m) > 1 else (m[2] if m[0] == "G" and len(m) > 2 and m[1] == "-" else m[0])
    return POSm.get(p)


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--cluster", required=True); ap.add_argument("--strongs")
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--dry-run", action="store_true"); g.add_argument("--live", action="store_true")
    ap.add_argument("--out", required=True); a = ap.parse_args()
    conn = sqlite3.connect(DB); conn.row_factory = sqlite3.Row; c = conn.cursor(); c2 = conn.cursor()
    now = c.execute("SELECT datetime('now')").fetchone()[0]

    # term meta + sense branches (sub-shade counts)
    terms = {}
    qfilt = ""
    args = [a.cluster]
    if a.strongs:
        qfilt = " AND m.strongs_number IN (%s)" % ",".join("?" * len(a.strongs.split(",")))
        args += a.strongs.split(",")
    for r in c.execute("SELECT m.id mid, m.strongs_number sn, m.transliteration tl, ti.parsed_meaning_id pmid "
                       "FROM mti_terms m LEFT JOIN wa_term_inventory ti ON ti.strongs_number=m.strongs_number "
                       "AND COALESCE(ti.delete_flagged,0)=0 WHERE m.cluster_code=? AND COALESCE(m.delete_flagged,0)=0"
                       + qfilt + " GROUP BY m.id", args):
        br = {}
        if r["pmid"]:
            st = c2.execute("SELECT group_concat(sense_text,'\n') s FROM wa_meaning_sense WHERE parsed_meaning_id=?", (r["pmid"],)).fetchone()["s"] or ""
            marks = list(STEM_MARK.finditer(st))
            for i, m in enumerate(marks):
                end = marks[i+1].start() if i+1 < len(marks) else len(st)
                seg = st[m.end():end]
                txt = re.sub(r"\s+", " ", seg).strip().strip(":")
                txt = re.split(r"\s\d+\)\s", txt)[0][:80]
                br[m.group(1).capitalize()] = (txt, len(SUBSHADE.findall(seg)))
            if not br:  # noun / no stems
                head = re.sub(r"\s+", " ", st).strip()[:80]
                br["_"] = (head, 1)
        terms[r["mid"]] = {"sn": r["sn"], "tl": r["tl"], "br": br}

    mids = list(terms)
    qm = ",".join("?" * len(mids))
    already = {r[0] for r in c.execute("SELECT verse_context_id FROM finding WHERE provenance='l2_mechanical' AND verse_context_id IS NOT NULL")}
    rows = c.execute(f"SELECT vc.id vcid, vc.mti_term_id mid, vc.step_meaning_applied sma, vr.stem stem, vr.morph_code morph, "
                     f"vr.reference ref, vr.verse_text txt FROM verse_context vc "
                     f"JOIN wa_verse_records vr ON vr.id = vc.verse_record_id "
                     f"WHERE COALESCE(vc.delete_flagged,0)=0 AND vc.mti_term_id IN ({qm})", mids).fetchall()

    nverse = 0; nfind = Counter(); triage = Counter(); sb_hits = 0; samples = []
    writes = []  # (table, sql, params)
    for r in rows:
        if r["vcid"] in already:
            continue
        t = terms[r["mid"]]; stem = r["stem"] or "_"
        ttype = pos_of(r["morph"]) or ("STATUS" if not r["stem"] else "?")
        br = t["br"].get(stem) or t["br"].get("_") or (r["sma"] or "", 1)
        lexical, nsub = br
        txt = r["txt"] or ""
        # triage
        if nsub <= 1:
            tri = "ACCEPT"
        elif THREAT.search(txt) or NEG.search(txt):
            tri = "ACCEPT"   # signal read in verse
        else:
            tri = "ESCALATE"
        lex_status = "STATED_UNRESOLVED" if tri == "ESCALATE" else "ANSWERED"
        # locus (T2)
        locus = next((lab for (w, oid), lab in [((w, oid), w) for (w, oid) in LOCUS] if re.search(r"\b"+w, txt, re.I)), None)
        # tier findings: (obs_id, value, status)
        tf = [
            (T_LEX,    lexical or "", lex_status),
            (T_KIND,   ttype, "ANSWERED"),
            (T_MODE,   stem if r["stem"] else "n/a (noun)", "ANSWERED" if r["stem"] else "STATED_SILENT"),
            (T_AFFECT, "affect (fear engages the affective faculty)", "ANSWERED"),
            (T_BODY,   locus if locus else "no locus named", "ANSWERED" if locus else "STATED_SILENT"),
        ]
        nverse += 1; triage[tri] += 1
        # SB findings anchored here (OPEN)
        sb = c.execute("SELECT COUNT(*) FROM finding f JOIN finding_verse_link l ON l.finding_id=f.id "
                       "WHERE l.reference=? AND f.finding_status='OPEN'", (r["ref"],)).fetchone()[0]
        sb_hits += sb
        if a.live:
            c.execute("UPDATE verse_context SET thing_type=?, triage_status=?, meaning_provenance=?, "
                      "step_meaning_applied=COALESCE(step_meaning_applied,?), flagged_for_review=? WHERE id=?",
                      (ttype, tri, "l2_mechanical", lexical, 1 if tri == "ESCALATE" else 0, r["vcid"]))
            for oid, val, stt in tf:
                cur = c.execute("INSERT INTO finding (level, verse_context_id, mti_term_id, finding_value, "
                                "finding_status, provenance, created_at, last_updated_date, delete_flagged) "
                                "VALUES ('VERSE',?,?,?,?,?,?,?,0)", (r["vcid"], r["mid"], val, stt, "l2_mechanical", now, now))
                c.execute("INSERT INTO finding_question_link (finding_id, question_id, coverage, created_at, delete_flagged) "
                          "VALUES (?,?,?,?,0)", (cur.lastrowid, oid, "full", now))
        for _o, _v, stt in tf:
            nfind[stt] += 1
        if len(samples) < 10:
            samples.append((r["ref"], t["tl"], ttype, stem, tri, lexical[:40], locus or "-", sb))
    if a.live:
        conn.commit()

    L = [f"# L2 writer — {'LIVE' if a.live else 'DRY-RUN'} — {a.cluster}" + (f" ({a.strongs})" if a.strongs else ""), ""]
    L.append("> `scripts/_apply_l2_write.py`. Per term-in-verse: mechanical tier findings (T7.1 lexical · T1.2 "
             "kind · T1.4 mode · T3.4 affect · T2 locus) → `finding`+`finding_question_link`, verse_context "
             "fields set. STATE_SILENT explicit; escalations = STATED_UNRESOLVED + flagged. Idempotent/reversible.")
    L.append("")
    L.append(f"**{nverse} term-verses processed · {sum(nfind.values())} tier findings "
             f"({'written' if a.live else 'to write'}) · {sb_hits} OPEN SB findings surfaced at these verses.**")
    L.append("")
    L.append("| triage | n |"); L.append("|---|---|")
    for k, v in triage.most_common(): L.append(f"| {k} | {v} |")
    L.append("")
    L.append("| finding status | n |"); L.append("|---|---|")
    for k, v in nfind.most_common(): L.append(f"| {k} | {v} |")
    L.append("")
    L.append("## Sample term-verses (the findings)")
    L.append(""); L.append("| Ref | term | type | stem | triage | lexical (T7.1) | locus (T2) | SB-open |")
    L.append("|---|---|---|---|---|---|---|---|")
    for s in samples: L.append("| " + " | ".join(str(x) for x in s) + " |")
    os.makedirs(os.path.dirname(a.out), exist_ok=True)
    open(a.out, "w", encoding="utf-8").write("\n".join(L))
    print(f"{'LIVE' if a.live else 'DRY'}: {nverse} term-verses, {sum(nfind.values())} findings, "
          f"triage {dict(triage)}, SB-open {sb_hits}; wrote {a.out}")


if __name__ == "__main__":
    main()
