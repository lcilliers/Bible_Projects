"""Refresh pointer cluster_link after the FLAG triage (full recompute + clear stale).

The earlier populate ran BEFORE FLAG terms got real cluster_codes, so links point
at FLAG (now empty) or at terms now excluded. This recomputes cluster_link for
EVERY pointer from current cluster_codes and OVERWRITES (sets NULL where nothing
resolves). Named Strong's + transliteration only (verse excluded, per design).

DEFAULT IS DRY-RUN. Pass --apply. Single transaction.
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


def cluster_of(cs):
    real = [c for c in cs if c and M_RE.match(c)]
    if real:
        return real[0] if len(set(real)) == 1 else None
    if "FLAG" in cs:
        return "FLAG"
    if "T2" in cs:
        return "T2"
    return None


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--apply", action="store_true"); a = ap.parse_args()
    c = sqlite3.connect(DB, timeout=30); c.row_factory = sqlite3.Row
    cur = c.cursor()

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
        s_cl = {smap[s] for s in set(STRONGS_RE.findall(text or "")) if smap.get(s)}
        nt = norm(text)
        t_cl = {tmap[t] for t in translits if t in nt}
        allc = {x for x in (s_cl | t_cl) if x}
        if not allc:
            return None, None
        basis = "strongs+translit" if (s_cl and t_cl) else ("strongs" if s_cl else "translit")
        return ",".join(sorted(allc)), basis

    updates = []  # (table, id, link, basis, old)
    before = Counter(); after = Counter()
    for r in cur.execute("SELECT id, finding, cluster_link cl FROM wa_session_b_findings WHERE COALESCE(delete_flag,0)=0"):
        link, basis = resolve(r["finding"])
        before["set" if r["cl"] else "null"] += 1
        after["set" if link else "null"] += 1
        if link != r["cl"]:
            updates.append(("wa_session_b_findings", r["id"], link, basis))
    ph = ",".join("?" * len(FLAG_CODES))
    for r in cur.execute(f"SELECT id, flag_label fl, description d, cluster_link cl FROM wa_session_research_flags WHERE flag_code IN ({ph})", FLAG_CODES):
        link, basis = resolve((r["fl"] or "") + " " + (r["d"] or ""))
        before["set" if r["cl"] else "null"] += 1
        after["set" if link else "null"] += 1
        if link != r["cl"]:
            updates.append(("wa_session_research_flags", r["id"], link, basis))

    print(f"{'APPLY' if a.apply else 'DRY-RUN'}: rows changing cluster_link: {len(updates)}")
    print(f"  before: {dict(before)} | after: {dict(after)}")
    if not a.apply:
        c.close(); return
    cur.execute("BEGIN")
    try:
        for table, rid, link, basis in updates:
            cur.execute(f"UPDATE {table} SET cluster_link=?, cluster_link_basis=? WHERE id=?", (link, basis, rid))
        c.commit()
    except Exception:
        c.rollback(); raise
    print(f"APPLIED: refreshed {len(updates)} pointers.")
    c.close()


if __name__ == "__main__":
    main()
