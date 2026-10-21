"""export_ve_status_reports.py (2026-06-17) — two read-only status reports over `ve_lexical`:
  A. API-updated overview  — every row resolved by an API read pass (source_provenance LIKE '%_read_api')
  B. status by cluster x VE item — mechanical / read / UNRESOLVED-or-pending coverage per (cluster, ve_label)

  python scripts/export_ve_status_reports.py
"""
import os, sqlite3, datetime
DB = os.path.join("database", "bible_research.db")
OUTA = "outputs/wa-ve-api-updated-overview-20260617.md"
OUTB = "outputs/wa-ve-status-by-cluster-by-veitem-20260617.md"
PENDING = ("UNRESOLVED", "pending-read", "thing/abstract")   # not-yet-final tokens


def main():
    c = sqlite3.connect(DB); c.row_factory = sqlite3.Row
    stamp = "2026-06-17"

    # rows joined to cluster
    base = """FROM ve_lexical x
        JOIN verse_context vc ON vc.id = x.verse_context_id
        JOIN mti_terms m ON m.id = vc.mti_term_id
        WHERE COALESCE(x.delete_flagged,0)=0 AND m.cluster_code IS NOT NULL"""

    # ---------- Report A: API-updated overview ----------
    a = [f"# VE — API-updated items: overview — {stamp}", "",
         "> Every `ve_lexical` row resolved by an **API read pass** (`source_provenance LIKE '%_read_api'`). "
         "Read-only snapshot; regenerate with `python scripts/export_ve_status_reports.py`.", ""]
    tot = c.execute(f"SELECT COUNT(*) n {base} AND x.source_provenance LIKE '%\\_read\\_api' ESCAPE '\\'").fetchone()["n"]
    a += [f"**Total API-updated rows:** {tot:,}", "",
          "## By VE item × provenance", "", "| VE item | provenance | rows | clusters |", "|---|---|---:|---:|"]
    for r in c.execute(f"""SELECT x.ve_label, x.source_provenance, COUNT(*) n, COUNT(DISTINCT m.cluster_code) cl
        {base} AND x.source_provenance LIKE '%\\_read\\_api' ESCAPE '\\'
        GROUP BY x.ve_label, x.source_provenance ORDER BY n DESC"""):
        a.append(f"| {r['ve_label']} | {r['source_provenance']} | {r['n']:,} | {r['cl']} |")

    a += ["", "## By cluster (API-updated rows per cluster)", "", "| cluster | API rows | VE items touched |", "|---|---:|---:|"]
    for r in c.execute(f"""SELECT m.cluster_code cc, COUNT(*) n, COUNT(DISTINCT x.ve_label) vi
        {base} AND x.source_provenance LIKE '%\\_read\\_api' ESCAPE '\\'
        GROUP BY m.cluster_code ORDER BY n DESC"""):
        a.append(f"| {r['cc']} | {r['n']:,} | {r['vi']} |")

    a += ["", "## Read-resolved value distributions (per read field)", ""]
    for fld in ("cause", "location", "divine-involvement", "object-type", "valence"):
        rows = c.execute(f"""SELECT x.value, COUNT(*) n {base}
            AND x.ve_label=? AND x.source_provenance LIKE '%\\_read\\_api' ESCAPE '\\'
            GROUP BY x.value ORDER BY n DESC LIMIT 12""", (fld,)).fetchall()
        if not rows:
            continue
        a.append(f"**{fld}** — " + " · ".join(f"{r['value']}={r['n']}" for r in rows))
    open(OUTA, "w", encoding="utf-8").write("\n".join(a))

    # ---------- Report B: status by cluster x VE item ----------
    labels = [r["ve_label"] for r in c.execute(f"SELECT DISTINCT x.ve_label {base} ORDER BY x.ve_label")]
    clusters = [r["cc"] for r in c.execute(f"SELECT DISTINCT m.cluster_code cc {base} ORDER BY m.cluster_code")]

    # per (cluster, label): mechanical, read, pending counts
    grid = {}
    for r in c.execute(f"""SELECT m.cluster_code cc, x.ve_label lab,
            SUM(CASE WHEN x.source_provenance LIKE '%\\_read\\_api' ESCAPE '\\' THEN 1 ELSE 0 END) rd,
            SUM(CASE WHEN x.source_provenance NOT LIKE '%\\_read\\_api' ESCAPE '\\' THEN 1 ELSE 0 END) mech,
            SUM(CASE WHEN x.value IN ('UNRESOLVED','pending-read','thing/abstract') THEN 1 ELSE 0 END) pend,
            COUNT(*) tot
        {base} GROUP BY m.cluster_code, x.ve_label"""):
        grid[(r["cc"], r["lab"])] = (r["mech"], r["rd"], r["pend"], r["tot"])

    b = [f"# VE — status by cluster × VE item — {stamp}", "",
         "> Per (cluster, VE item): **m** = mechanical rows · **r** = API-read rows · **p** = still pending "
         "(`UNRESOLVED`/`pending-read`/`thing/abstract`). Cell = `m/r/p`. Read-only; regenerate with the script.", "",
         "Legend: a high **p** means that field still needs a read for that cluster. **r>0** = a read pass has run.", ""]
    # compact matrix for the read-relevant fields
    key_fields = ["cause", "location", "divine-involvement", "object-type", "valence"]
    b += ["## Read fields — coverage matrix (m / r / p)", "",
          "| cluster | " + " | ".join(key_fields) + " |", "|---|" + "---|" * len(key_fields)]
    for cc in clusters:
        cells = []
        for lab in key_fields:
            g = grid.get((cc, lab))
            cells.append(f"{g[0]}/{g[1]}/{g[2]}" if g else "—")
        b.append(f"| {cc} | " + " | ".join(cells) + " |")

    # full per-cluster breakdown (all VE items)
    b += ["", "## Full breakdown — every (cluster, VE item)", "",
          "| cluster | VE item | mechanical | read | pending | total |", "|---|---|---:|---:|---:|---:|"]
    for cc in clusters:
        for lab in labels:
            g = grid.get((cc, lab))
            if g:
                b.append(f"| {cc} | {lab} | {g[0]:,} | {g[1]:,} | {g[2]:,} | {g[3]:,} |")
    open(OUTB, "w", encoding="utf-8").write("\n".join(b))

    print(f"WROTE {OUTA}  (API-updated rows: {tot:,})")
    print(f"WROTE {OUTB}  ({len(clusters)} clusters × {len(labels)} VE items)")


if __name__ == "__main__":
    main()
