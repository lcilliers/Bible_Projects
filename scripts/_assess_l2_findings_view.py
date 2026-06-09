"""_assess_l2_findings_view.py — READ-ONLY. For each requested cluster, shows the L1 + L2 results per verse:
the verse text, each of the cluster's terms in it (L1: type · morph/stem), and the L2 tier findings on that
term-in-verse (T7.1 lexical · T1.2 kind · T1.4 mode · T2 body · T3 faculty) with status. A representative
sample (some ANSWERED, some escalated). NO DB writes.

Usage:  python scripts/_assess_l2_findings_view.py --clusters M15,M10,M26 --sample 12 --out <file>.md
"""
import argparse, os, re, sqlite3, sys
from collections import Counter
sys.stdout.reconfigure(encoding="utf-8")
DB = os.path.join("database", "bible_research.db")
QLABEL = {"T7.1.3": "T7.1 lexical", "T1.2.1": "T1.2 kind", "T1.4.1": "T1.4 mode",
          "T2.6.1": "T2 body", "T2.3.1": "T2 heart", "T2.4.1": "T2 mind",
          "T3.4.1": "T3 affect", "T3.2.1": "T3 cognition"}


def tier_findings(c, vcid, mid):
    out = []
    for r in c.execute("SELECT q.question_code qc, f.finding_value v, f.finding_status st "
                       "FROM finding f JOIN finding_question_link l ON l.finding_id=f.id "
                       "JOIN wa_obs_question_catalogue q ON q.obs_id=l.question_id "
                       "WHERE f.verse_context_id=? AND f.mti_term_id=? AND f.provenance='l2_mechanical' "
                       "ORDER BY q.question_code", (vcid, mid)):
        out.append((QLABEL.get(r["qc"], r["qc"]), r["st"], r["v"]))
    return out


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--clusters", required=True)
    ap.add_argument("--sample", type=int, default=12); ap.add_argument("--out", required=True)
    a = ap.parse_args()
    conn = sqlite3.connect(DB); conn.row_factory = sqlite3.Row; c = conn.cursor()
    name = {r["cluster_code"]: (r["short_name"] or r["cluster_code"]) for r in c.execute("SELECT cluster_code, short_name FROM cluster")}
    L = ["# L1/L2 findings view — verse text + findings", ""]
    L.append("> READ-ONLY (`scripts/_assess_l2_findings_view.py`). Per verse: text + each cluster term "
             "[L1 type·stem] and its L2 tier findings (status · value). Representative sample.")
    for CL in [x.strip() for x in a.clusters.split(",")]:
        mids = [r[0] for r in c.execute("SELECT id FROM mti_terms WHERE cluster_code=? AND COALESCE(delete_flagged,0)=0", (CL,))]
        qm = ",".join("?" * len(mids))
        # summary
        tv = c.execute(f"SELECT COUNT(DISTINCT vc.id) FROM verse_context vc WHERE vc.mti_term_id IN ({qm}) "
                       f"AND COALESCE(vc.delete_flagged,0)=0", mids).fetchone()[0]
        tri = {r[0]: r[1] for r in c.execute(f"SELECT triage_status, COUNT(*) FROM verse_context WHERE mti_term_id IN ({qm}) "
                                             f"AND meaning_provenance='l2_mechanical' GROUP BY triage_status", mids)}
        L.append(f"\n## {CL} ({name.get(CL, CL)}) — {tv} term-in-verses · triage {tri}\n")
        # OLD characteristic-level findings (cluster_finding) for the four tiers, for comparison
        TIERS = [("T1.2 Kind", ["T1.2"]), ("T1.4 Modes", ["T1.4"]),
                 ("T2 Constitution/Body", ["T2."]), ("T7.1 Lexical", ["T7.1"])]
        L.append("### OLD findings (characteristic-level, `cluster_finding`) — for comparison")
        for tlabel, comps in TIERS:
            if comps[0].endswith("."):
                oids = [r[0] for r in c.execute("SELECT obs_id FROM wa_obs_question_catalogue WHERE component_code LIKE ? AND COALESCE(deleted,0)=0", (comps[0] + "%",))]
            else:
                oids = [r[0] for r in c.execute("SELECT obs_id FROM wa_obs_question_catalogue WHERE component_code=? AND COALESCE(deleted,0)=0", (comps[0],))]
            qo = ",".join("?" * len(oids))
            old = c.execute(f"SELECT q.question_code qc, cf.finding_text ft FROM cluster_finding cf "
                            f"JOIN wa_obs_question_catalogue q ON q.obs_id=cf.obs_id WHERE cf.cluster_code=? "
                            f"AND cf.obs_id IN ({qo}) AND COALESCE(cf.delete_flagged,0)=0 "
                            f"AND cf.finding_text IS NOT NULL", [CL] + oids).fetchall()
            seen = []
            for r in old:
                key = (r["ft"] or "")[:60]
                if key in seen: continue
                seen.append(key)
            L.append(f"- **{tlabel}** ({len(old)} old findings):")
            for r in old[:4]:
                L.append(f"    - _{r['qc']}_: {re.sub(chr(10),' ',(r['ft'] or ''))[:150]}")
        L.append("\n### NEW per-verse findings (L2 mechanical)\n")
        # sample: take some references (ordered) + ensure a couple escalated
        rows = c.execute(f"SELECT vc.id vcid, vc.mti_term_id mid, vc.thing_type tt, vc.triage_status tri, "
                         f"m.transliteration tl, vr.reference ref, vr.verse_text txt, vr.stem stem, vr.morph_code morph "
                         f"FROM verse_context vc JOIN wa_verse_records vr ON vr.id=vc.verse_record_id "
                         f"JOIN mti_terms m ON m.id=vc.mti_term_id WHERE vc.mti_term_id IN ({qm}) "
                         f"AND vc.meaning_provenance='l2_mechanical' ORDER BY vr.book_id, vr.chapter, vr.verse_num", mids).fetchall()
        esc = [r for r in rows if r["tri"] == "ESCALATE"][:3]
        pick = rows[:a.sample] + [r for r in esc if r not in rows[:a.sample]]
        # group by reference
        seen_ref = []
        for r in pick:
            if r["ref"] in seen_ref:
                continue
            seen_ref.append(r["ref"])
            terms_here = [x for x in pick if x["ref"] == r["ref"]]
            txt = re.sub(r"\s+", " ", (r["txt"] or "")).strip()
            L.append(f"### {r['ref']}")
            L.append(f"> {txt}")
            for x in terms_here:
                L.append(f"- **{x['tl']}**  [L1: {x['tt']}{('·'+x['stem']) if x['stem'] else ''} · morph {x['morph']}] · triage **{x['tri']}**")
                for lab, st, val in tier_findings(c, x["vcid"], x["mid"]):
                    flag = "" if st == "ANSWERED" else f" _({st})_"
                    L.append(f"    - {lab}{flag}: {(val or '')[:90]}")
            L.append("")
    os.makedirs(os.path.dirname(a.out), exist_ok=True)
    open(a.out, "w", encoding="utf-8").write("\n".join(L))
    print(f"wrote {a.out}")


if __name__ == "__main__":
    main()
