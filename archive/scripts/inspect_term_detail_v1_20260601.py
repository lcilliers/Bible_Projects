"""Verbatim, read-only dump of EVERYWHERE a Strong's term is referenced in the DB.

Sweeps every table and emits every matching row with every column, no analysis.
Matches by: strongs_number/strongs_reference/strongs_id LIKE '<S>%'; FK columns
(mti_term_id, term_inv_id, verse_record_id, verse_id, term_id) against the term's
resolved id sets; referenced entity ids (group_id, cluster_subgroup_id); and a
text sweep of TEXT columns for the Strong's code and the transliteration.

Usage:
  python scripts/inspect_term_detail_v1_20260601.py --strongs G2285 [--translit thambos]
"""
import argparse, os, sqlite3
from datetime import datetime

DB = os.path.join("database", "bible_research.db")


def inclause(col, ids):
    return (f"{col} IN ({','.join('?' for _ in ids)})", list(ids)) if ids else (None, [])


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--strongs", required=True)
    ap.add_argument("--translit", default=None)
    ap.add_argument("--out", default=None)
    a = ap.parse_args()
    S = a.strongs
    conn = sqlite3.connect(DB); conn.row_factory = sqlite3.Row
    cur = conn.cursor()

    # resolve anchor id sets
    mti_ids = [r["id"] for r in cur.execute("SELECT id FROM mti_terms WHERE strongs_number LIKE ?", (S + "%",))]
    inv_ids = [r["id"] for r in cur.execute("SELECT id FROM wa_term_inventory WHERE strongs_number LIKE ?", (S + "%",))]
    vr_ids = []
    if mti_ids or inv_ids:
        conds, ps = [], []
        c1, p1 = inclause("mti_term_id", mti_ids);
        if c1: conds.append(c1); ps += p1
        c2, p2 = inclause("term_inv_id", inv_ids)
        if c2: conds.append(c2); ps += p2
        c3, p3 = inclause("term_id", inv_ids)
        if c3: conds.append(c3); ps += p3
        if conds:
            vr_ids = [r["id"] for r in cur.execute("SELECT id FROM wa_verse_records WHERE " + " OR ".join(conds), ps)]
    # referenced groups / sub-groups (from verse_context + mti_term_subgroup of this term)
    grp_ids, sg_ids, cluster_codes = set(), set(), set()
    if mti_ids:
        ph = ",".join("?" for _ in mti_ids)
        for r in cur.execute(f"SELECT group_id, cluster_subgroup_id FROM verse_context WHERE mti_term_id IN ({ph})", mti_ids):
            if r["group_id"]: grp_ids.add(r["group_id"])
            if r["cluster_subgroup_id"]: sg_ids.add(r["cluster_subgroup_id"])
        for r in cur.execute(f"SELECT cluster_subgroup_id FROM mti_term_subgroup WHERE mti_term_id IN ({ph})", mti_ids):
            if r["cluster_subgroup_id"]: sg_ids.add(r["cluster_subgroup_id"])
    for r in cur.execute("SELECT DISTINCT cluster_code FROM mti_terms WHERE strongs_number LIKE ?", (S + "%",)):
        if r["cluster_code"]: cluster_codes.add(r["cluster_code"])
    if sg_ids:
        ph = ",".join("?" for _ in sg_ids)
        for r in cur.execute(f"SELECT cluster_code FROM cluster_subgroup WHERE id IN ({ph})", list(sg_ids)):
            if r["cluster_code"]: cluster_codes.add(r["cluster_code"])

    kw = [S]
    if a.translit:
        kw.append(a.translit)

    L = [f"# Verbatim DB dump — {S}" + (f" ({a.translit})" if a.translit else ""),
         "",
         f"Resolved ids: mti_terms={mti_ids} · wa_term_inventory={inv_ids} · wa_verse_records={vr_ids}",
         f"Referenced: group_ids={sorted(grp_ids)} · cluster_subgroup_ids={sorted(sg_ids)} · cluster_codes={sorted(cluster_codes)}",
         f"Text sweep keywords: {kw}",
         ""]

    tables = [r["name"] for r in cur.execute("SELECT name FROM sqlite_master WHERE type='table' ORDER BY name")]
    grand = 0
    counts = {}
    for t in tables:
        info = list(cur.execute(f"PRAGMA table_info({t})"))
        cols = [c["name"] for c in info]
        types = {c["name"]: (c["type"] or "") for c in info}
        conds, ps = [], []
        def add(c, p=()):
            conds.append(c); ps.extend(p)
        for sc in ("strongs_number", "strongs_reference", "strongs_id"):
            if sc in cols: add(f"{sc} LIKE ?", (S + "%",))
        # term-specific FKs only. group_id / cluster_subgroup_id are NOT matched here
        # (that would pull every sibling term in the same group/sub-group). The
        # VCG / sub-group / cluster *definition* rows are fetched explicitly below.
        for col, ids in (("mti_term_id", mti_ids), ("term_inv_id", inv_ids),
                         ("verse_record_id", vr_ids), ("verse_id", vr_ids)):
            if col not in cols:
                continue
            c, p = inclause(col, ids)
            if c: add(c, p)
        if t == "mti_terms" and mti_ids: c, p = inclause("id", mti_ids); add(c, p)
        if t == "wa_term_inventory" and inv_ids: c, p = inclause("id", inv_ids); add(c, p)
        if t == "wa_verse_records" and vr_ids: c, p = inclause("id", vr_ids); add(c, p)
        if t == "verse_context_group" and grp_ids: c, p = inclause("id", list(grp_ids)); add(c, p)
        if t == "cluster_subgroup" and sg_ids: c, p = inclause("id", list(sg_ids)); add(c, p)
        if t == "cluster" and cluster_codes: c, p = inclause("cluster_code", list(cluster_codes)); add(c, p)
        if "term_id" in cols and t in ("wa_verse_records", "wa_verse_term_links") and inv_ids:
            c, p = inclause("term_id", inv_ids); add(c, p)
        # text sweep
        for cn in cols:
            ty = types[cn].upper()
            if ty in ("TEXT", "") or "CHAR" in ty or "CLOB" in ty:
                for k in kw:
                    add(f"{cn} LIKE ?", (f"%{k}%",))
        if not conds:
            continue
        try:
            rows = cur.execute(f"SELECT * FROM {t} WHERE " + " OR ".join(conds), ps).fetchall()
        except sqlite3.OperationalError as e:
            L.append(f"## {t} — QUERY ERROR: {e}"); L.append(""); continue
        if not rows:
            continue
        counts[t] = len(rows); grand += len(rows)
        L.append(f"## {t} — {len(rows)} row(s)")
        L.append("")
        for r in rows:
            L.append("```")
            for k in r.keys():
                L.append(f"{k}: {r[k]!r}")
            L.append("```")
            L.append("")
    L.insert(5, "Per-table row counts: " + ", ".join(f"{k}={v}" for k, v in counts.items()) + f"  (total {grand})")
    L.insert(6, "")

    out = a.out or os.path.join("research", "investigations", f"term-{S}-{a.translit or 'detail'}-verbatim-{datetime.now():%Y%m%d}.md")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    open(out, "w", encoding="utf-8").write("\n".join(L) + "\n")
    conn.close()
    print(f"Matched {grand} rows across {len(counts)} tables:")
    for k, v in counts.items():
        print(f"  {k}: {v}")
    print(f"Dump: {out}")


if __name__ == "__main__":
    main()
