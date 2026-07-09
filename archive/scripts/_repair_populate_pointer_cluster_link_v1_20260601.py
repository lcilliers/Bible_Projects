"""Populate cluster_link / cluster_link_basis on Session B/D pointers.

Resolution = named Strong's codes + named transliterations in the pointer text,
mapped to their term's cluster (Mxx > FLAG > T2). Verse refs are NOT used (they
over-link). Multi-value: cluster_link = comma-separated sorted cluster codes.
cluster_link_basis = 'strongs' / 'translit' / 'strongs+translit'.

Scope: wa_session_b_findings (active) + wa_session_research_flags pointer codes
(SD_POINTER, SB_FINDING, SB_INNER_BEING, SD_CLUSTER). Only sets where currently
NULL (every pointer — the columns are new), i.e. "not already connected".
Pointers that resolve to nothing keep cluster_link NULL (-> step a, retention).

DEFAULT IS DRY-RUN. Pass --apply to write.
"""
import argparse
import re
import sqlite3
import unicodedata
from collections import Counter, defaultdict

DB = "database/bible_research.db"
M_RE = re.compile(r"^M\d")
STRONGS_RE = re.compile(r"\b([HG]\d{1,4}[A-Z]?)\b")
FLAG_CODES = ("SD_POINTER", "SB_FINDING", "SB_INNER_BEING", "SD_CLUSTER")


def norm(s):
    s = unicodedata.normalize("NFKD", s or "")
    s = "".join(c for c in s if not unicodedata.combining(c))
    return re.sub(r"[\s.\-]", "", s.lower())


def cluster_of(clusters):
    real = [c for c in clusters if c and M_RE.match(c)]
    if real:
        return real[0] if len(set(real)) == 1 else None
    if "FLAG" in clusters:
        return "FLAG"
    if "T2" in clusters:
        return "T2"
    return None


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--apply", action="store_true"); a = ap.parse_args()
    conn = sqlite3.connect(DB, timeout=30); conn.row_factory = sqlite3.Row
    cur = conn.cursor()

    sc = defaultdict(set)
    for r in cur.execute("SELECT strongs_number sn, cluster_code cc FROM mti_terms"):
        sc[r["sn"]].add(r["cc"])
    smap = {sn: cluster_of(cl) for sn, cl in sc.items()}

    tmap = {}
    for r in cur.execute("SELECT transliteration tr, strongs_number sn FROM mti_terms WHERE transliteration IS NOT NULL"):
        n = norm(r["tr"])
        if len(n) >= 5 and smap.get(r["sn"]):
            tmap.setdefault(n, smap[r["sn"]])
    translits = sorted(tmap, key=len, reverse=True)

    def resolve(text):
        text = text or ""
        s_cl = set(); t_cl = set()
        for s in set(STRONGS_RE.findall(text)):
            if smap.get(s):
                s_cl.add(smap[s])
        ntext = norm(text)
        for t in translits:
            if t in ntext and tmap.get(t):
                t_cl.add(tmap[t])
        allc = s_cl | t_cl
        if not allc:
            return None, None
        basis = "strongs+translit" if (s_cl and t_cl) else ("strongs" if s_cl else "translit")
        return ",".join(sorted(allc)), basis

    updates = []   # (table, id, link, basis)
    ccount = Counter(); bcount = Counter(); nolink = Counter()

    for r in cur.execute("SELECT id, finding FROM wa_session_b_findings WHERE COALESCE(delete_flag,0)=0"):
        link, basis = resolve(r["finding"])
        if link:
            updates.append(("wa_session_b_findings", r["id"], link, basis))
            ccount[min(link.count(",") + 1, 3)] += 1; bcount[basis] += 1
        else:
            nolink["wa_session_b_findings"] += 1

    ph = ",".join("?" * len(FLAG_CODES))
    for r in cur.execute(f"SELECT id, flag_label fl, description d FROM wa_session_research_flags WHERE flag_code IN ({ph})", FLAG_CODES):
        link, basis = resolve((r["fl"] or "") + " " + (r["d"] or ""))
        if link:
            updates.append(("wa_session_research_flags", r["id"], link, basis))
            ccount[min(link.count(",") + 1, 3)] += 1; bcount[basis] += 1
        else:
            nolink["wa_session_research_flags"] += 1

    print(f"{'APPLY' if a.apply else 'DRY-RUN'}: pointers to link: {len(updates)}")
    print(f"  basis: {dict(bcount)}")
    print(f"  clusters-per-pointer: 1->{ccount.get(1,0)} 2->{ccount.get(2,0)} 3+->{ccount.get(3,0)}")
    print(f"  no-link (cluster_link stays NULL): {dict(nolink)}")
    if not a.apply:
        conn.close(); return

    cur.execute("BEGIN")
    try:
        for table, rid, link, basis in updates:
            cur.execute(f"UPDATE {table} SET cluster_link=?, cluster_link_basis=? WHERE id=?", (link, basis, rid))
        conn.commit()
    except Exception:
        conn.rollback(); raise
    print(f"APPLIED: linked {len(updates)} pointers.")
    conn.close()


if __name__ == "__main__":
    main()
