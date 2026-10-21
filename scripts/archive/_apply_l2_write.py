"""_apply_l2_write.py — the L2 WRITER (verse-complete). Enters by --cluster (the verses that contain a
cluster's terms) and processes each verse COMPLETELY: writes the per-term TIER FINDINGS for EVERY in-scope
term in the verse — across all clusters — each saved to its own term's cluster (via finding.mti_term_id).
Implements feedback_characteristic_is_typed_term_in_verse (one verse-read completes all its terms, to each
cluster) + verse-coverage/no-double-work (idempotent skip of already-written term-in-verses).

Per term-in-verse: mechanical (stem→sense-branch, type, faculty, locus) → triage → finding (level=VERSE,
anchored on verse_context) + finding_question_link; verse_context fields set. STATE_SILENT explicit;
escalations = STATED_UNRESOLVED + flagged. Faculty asserted only where the term's cluster is mapped
(state-not-induce; faculty per-term derivation is a pending refinement). Reversible (provenance='l2_mechanical').

Usage:  python scripts/_apply_l2_write.py --cluster M01 [--strongs H..] --dry-run|--live --out <file>.md
"""
import argparse, os, re, sqlite3, sys
from collections import Counter
sys.stdout.reconfigure(encoding="utf-8")
DB = os.path.join("database", "bible_research.db")
POSm = {"V": "ACTION", "N": "STATUS", "A": "QUALITY"}
STEM_MARK = re.compile(r"\((Qal|Niphal|Piel|Pual|Hiphil|Hophal|Hithpael)\)", re.I)
SUBSHADE = re.compile(r"\d+[a-z]\d+\)")
THREAT = re.compile(r"\b(enemy|enemies|sword|army|armies|slay|kill|death|die|pursue|nations|destroy|siege|flee|afraid of)\b", re.I)
NEG = re.compile(r"\b(do not fear|fear not|be not afraid|not be afraid|no fear)\b", re.I)
LOCUS = [("heart", 267), ("mind", 270), ("bowel", 276), ("kidney", 276), ("inward", 276), ("breast", 276)]
T_LEX, T_KIND, T_MODE, T_BODY = 395, 239, 245, 276
# per-cluster PRIMARY faculty (T3) — asserted only where mapped (faculty per-term derivation is pending).
# M15 removed: its cognition was induced for a mixed-faculty cluster (boulomai=volition). M01 affect verified uniform.
CLUSTER_FACULTY = {"M01": (300, "affect (fear engages the affective faculty)")}


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

    # all in-scope terms: cluster + pmid (for lazy branch parse)
    clus, pmid_of, tl_of = {}, {}, {}
    for r in c.execute("SELECT m.id mid, m.cluster_code cc, m.transliteration tl, ti.parsed_meaning_id pmid "
                       "FROM mti_terms m LEFT JOIN wa_term_inventory ti ON ti.strongs_number=m.strongs_number "
                       "AND COALESCE(ti.delete_flagged,0)=0 WHERE m.cluster_code NOT IN ('T2','FLAG') "
                       "AND m.cluster_code IS NOT NULL AND COALESCE(m.delete_flagged,0)=0 GROUP BY m.id"):
        clus[r["mid"]] = r["cc"]; pmid_of[r["mid"]] = r["pmid"]; tl_of[r["mid"]] = r["tl"]
    br_cache = {}

    def branches(mid):
        if mid in br_cache: return br_cache[mid]
        br = {}; pm = pmid_of.get(mid)
        if pm:
            st = c2.execute("SELECT group_concat(sense_text,'\n') s FROM wa_meaning_sense WHERE parsed_meaning_id=?", (pm,)).fetchone()["s"] or ""
            marks = list(STEM_MARK.finditer(st))
            for i, m in enumerate(marks):
                end = marks[i+1].start() if i+1 < len(marks) else len(st)
                seg = st[m.end():end]
                txt = re.split(r"\s\d+\)\s", re.sub(r"\s+", " ", seg).strip().strip(":"))[0][:80]
                br[m.group(1).capitalize()] = (txt, len(SUBSHADE.findall(seg)))
            if not br:
                br["_"] = (re.sub(r"\s+", " ", st).strip()[:80], 1)
        br_cache[mid] = br; return br

    # ENTRY: references containing a --cluster term (+ optional strongs)
    entry = [mid for mid, cc in clus.items() if cc == a.cluster]
    if a.strongs:
        want = set(a.strongs.split(","))
        entry = [mid for mid in entry if c.execute("SELECT strongs_number FROM mti_terms WHERE id=?", (mid,)).fetchone()[0] in want]
    qe = ",".join("?" * len(entry))
    refs = [r[0] for r in c.execute(f"SELECT DISTINCT vr.reference FROM verse_context vc JOIN wa_verse_records vr ON vr.id=vc.verse_record_id "
                                    f"WHERE COALESCE(vc.delete_flagged,0)=0 AND vc.mti_term_id IN ({qe})", entry)]
    already = {r[0] for r in c.execute("SELECT verse_context_id FROM finding WHERE provenance='l2_mechanical' AND verse_context_id IS NOT NULL")}

    # ALL in-scope term-in-verses at those references (verse-complete)
    qr = ",".join("?" * len(refs))
    rows = c.execute(f"SELECT vc.id vcid, vc.mti_term_id mid, vc.step_meaning_applied sma, vr.stem stem, vr.morph_code morph, "
                     f"vr.reference ref, vr.verse_text txt FROM verse_context vc JOIN wa_verse_records vr ON vr.id=vc.verse_record_id "
                     f"WHERE COALESCE(vc.delete_flagged,0)=0 AND vr.reference IN ({qr})", refs).fetchall()

    nverse = 0; nfind = Counter(); triage = Counter(); by_cluster = Counter(); sb_hits = 0; samples = []
    for r in rows:
        if r["mid"] not in clus or r["vcid"] in already:
            continue
        cc = clus[r["mid"]]; fac = CLUSTER_FACULTY.get(cc)
        stem = r["stem"] or "_"; ttype = pos_of(r["morph"]) or ("STATUS" if not r["stem"] else "?")
        br = branches(r["mid"]); seg = br.get(stem) or br.get("_") or (r["sma"] or "", 1)
        lexical, nsub = seg; txt = r["txt"] or ""
        tri = "ACCEPT" if (nsub <= 1 or THREAT.search(txt) or NEG.search(txt)) else "ESCALATE"
        lex_status = "STATED_UNRESOLVED" if tri == "ESCALATE" else "ANSWERED"
        locus = next((w for (w, _o) in LOCUS if re.search(r"\b" + w, txt, re.I)), None)
        tf = [
            (T_LEX,  lexical or "", lex_status),
            (T_KIND, ttype, "ANSWERED"),
            (T_MODE, stem if r["stem"] else "n/a (noun)", "ANSWERED" if r["stem"] else "STATED_SILENT"),
            (T_BODY, locus if locus else "no locus named", "ANSWERED" if locus else "STATED_SILENT"),
        ]
        if fac:
            tf.append((fac[0], fac[1], "ANSWERED"))
        nverse += 1; triage[tri] += 1; by_cluster[cc] += 1
        sb_hits += c.execute("SELECT COUNT(*) FROM finding f JOIN finding_verse_link l ON l.finding_id=f.id WHERE l.reference=? AND f.finding_status='OPEN'", (r["ref"],)).fetchone()[0]
        if a.live:
            c.execute("UPDATE verse_context SET thing_type=?, triage_status=?, meaning_provenance=?, "
                      "step_meaning_applied=COALESCE(step_meaning_applied,?), flagged_for_review=? WHERE id=?",
                      (ttype, tri, "l2_mechanical", lexical, 1 if tri == "ESCALATE" else 0, r["vcid"]))
            for oid, val, stt in tf:
                cur = c.execute("INSERT INTO finding (level, verse_context_id, mti_term_id, finding_value, finding_status, "
                                "provenance, created_at, last_updated_date, delete_flagged) VALUES ('VERSE',?,?,?,?,?,?,?,0)",
                                (r["vcid"], r["mid"], val, stt, "l2_mechanical", now, now))
                c.execute("INSERT INTO finding_question_link (finding_id, question_id, coverage, created_at, delete_flagged) VALUES (?,?,?,?,0)",
                          (cur.lastrowid, oid, "full", now))
        for _o, _v, stt in tf:
            nfind[stt] += 1
        if len(samples) < 10 and cc != a.cluster:
            samples.append((r["ref"], tl_of[r["mid"]], cc, ttype, tri, (lexical or "")[:38]))
    if a.live:
        conn.commit()

    L = [f"# L2 writer (verse-complete) — {'LIVE' if a.live else 'DRY-RUN'} — entry {a.cluster}" + (f" ({a.strongs})" if a.strongs else ""), ""]
    L.append("> `scripts/_apply_l2_write.py`. Enters by cluster's verses; writes tier findings for EVERY "
             "in-scope term in each verse, to each term's cluster (finding.mti_term_id). Idempotent/reversible.")
    L.append("")
    L.append(f"**{len(refs)} entry verses · {nverse} term-in-verses {'written' if a.live else 'to write'} "
             f"({sum(nfind.values())} tier findings) · {sb_hits} OPEN SB surfaced.**")
    L.append("")
    L.append("| triage | n |"); L.append("|---|---|")
    for k, v in triage.most_common(): L.append(f"| {k} | {v} |")
    L.append("")
    L.append("## Findings written BY CLUSTER (multi-term spread)")
    L.append(""); L.append("| cluster | term-verses |"); L.append("|---|---|")
    for k, v in by_cluster.most_common(15): L.append(f"| {k} | {v} |")
    L.append(f"\n_… {len(by_cluster)} clusters touched from {a.cluster} entry verses._")
    L.append("")
    L.append("## Sample OTHER-cluster findings written from these verses")
    L.append(""); L.append("| Ref | term | cluster | type | triage | lexical |"); L.append("|---|---|---|---|---|---|")
    for s in samples: L.append("| " + " | ".join(str(x) for x in s) + " |")
    os.makedirs(os.path.dirname(a.out), exist_ok=True)
    open(a.out, "w", encoding="utf-8").write("\n".join(L))
    print(f"{'LIVE' if a.live else 'DRY'}: entry {a.cluster}, {len(refs)} verses, {nverse} term-verses across "
          f"{len(by_cluster)} clusters, {sum(nfind.values())} findings, triage {dict(triage)}; wrote {a.out}")


if __name__ == "__main__":
    main()
