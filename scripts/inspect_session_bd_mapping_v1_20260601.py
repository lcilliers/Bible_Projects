"""Session B & D pointers: status + mapping-to-terms (therefore clusters).

Read-only. Builds strongs -> cluster-home map, then assesses how far each pointer
population carries a term link that resolves to a cluster.

Cluster bucket per strongs (across its mti_terms rows):
  Mxx (real cluster) > FLAG > T2 > none(NULL only)   ; 'no-term' if strongs absent.

Output: research/investigations/session-bd-pointers-assessment-20260601.md
  python scripts/inspect_session_bd_mapping_v1_20260601.py
"""
import os
import re
import sqlite3
from collections import Counter, defaultdict

DB = "database/bible_research.db"
OUT = "research/investigations/session-bd-pointers-assessment-20260601.md"
M_RE = re.compile(r"^M\d")


def cluster_of(clusters):
    real = [c for c in clusters if c and M_RE.match(c)]
    if real:
        return real[0] if len(set(real)) == 1 else "Mxx(multi)"
    if "FLAG" in clusters:
        return "FLAG"
    if "T2" in clusters:
        return "T2"
    return "none(NULL)"


def bucket(strongs, smap):
    if not strongs:
        return "no-strongs-on-pointer"
    if strongs not in smap:
        return "no-matching-term"
    return smap[strongs]


def main():
    conn = sqlite3.connect(DB, timeout=10)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()

    # strongs -> set of cluster codes across its rows
    sc = defaultdict(set)
    for r in cur.execute("SELECT strongs_number sn, cluster_code cc FROM mti_terms"):
        sc[r["sn"]].add(r["cc"])
    smap = {sn: cluster_of(cl) for sn, cl in sc.items()}

    L = ["# Session B & D pointers — status & mapping to terms/clusters", "",
         "**Generated:** 2026-06-01 (read-only). Focus: how far each pointer population carries a term link that resolves to a cluster.",
         "Cluster bucket = the term's home: real M-cluster > FLAG > T2 > none(NULL); or no-matching-term / no-strongs-on-pointer.", ""]

    # ---- A. wa_session_b_findings ----
    f = cur.execute("SELECT id, finding_type, status, COALESCE(delete_flag,0) df, term_id, session_c_chapter, sd_pointer_ref FROM wa_session_b_findings").fetchall()
    active = [r for r in f if r["df"] == 0]
    L += ["## A. wa_session_b_findings", "",
          f"- total: {len(f)} | active (delete_flag=0): {len(active)} | deleted: {len(f)-len(active)}",
          f"- term_id populated (active): {sum(1 for r in active if r['term_id'])}/{len(active)}",
          f"- already routed to a Session C chapter (active): {sum(1 for r in active if r['session_c_chapter'])}",
          f"- carry an sd_pointer_ref (active): {sum(1 for r in active if r['sd_pointer_ref'])}", "",
          "**finding_type (active):** " + ", ".join(f"{k}={v}" for k, v in Counter(r["finding_type"] for r in active).most_common()), "",
          "**status (active):** " + ", ".join(f"{k}={v}" for k, v in Counter(r["status"] for r in active).most_common()), "",
          "**term_id → cluster bucket (active findings):**", ""]
    fb = Counter(bucket(r["term_id"], smap) for r in active)
    for k, v in fb.most_common():
        L.append(f"- {k}: {v}")

    # sample term_id values to expose format
    sample = [r["term_id"] for r in active if r["term_id"]][:8]
    L += ["", f"_term_id sample:_ {sample}", ""]

    # ---- B. wa_session_research_flags pointers ----
    L += ["## B. wa_session_research_flags (pointer flags)", ""]
    for code in ("SD_POINTER", "SB_FINDING", "SB_INNER_BEING", "SD_CLUSTER"):
        rows = cur.execute("SELECT registry_id, strongs_reference, COALESCE(resolved,0) resolved FROM wa_session_research_flags WHERE flag_code=?", (code,)).fetchall()
        if not rows:
            continue
        withs = sum(1 for r in rows if r["strongs_reference"])
        withreg = sum(1 for r in rows if r["registry_id"] is not None)
        res = sum(1 for r in rows if r["resolved"])
        bb = Counter(bucket(r["strongs_reference"], smap) for r in rows)
        L += [f"### {code} — {len(rows)} ({res} resolved)",
              f"- strongs_reference populated: {withs}/{len(rows)} | registry_id populated: {withreg}/{len(rows)}",
              "- strongs_reference → cluster bucket: " + ", ".join(f"{k}={v}" for k, v in bb.most_common()), ""]
        s2 = [r["strongs_reference"] for r in rows if r["strongs_reference"]][:6]
        L.append(f"  _strongs_reference sample:_ {s2}")
        L.append("")

    # ---- C. wa_finding_entity_links ----
    el = cur.execute("SELECT entity_type, entity_strongs, COALESCE(delete_flagged,0) df FROM wa_finding_entity_links").fetchall()
    ela = [r for r in el if r["df"] == 0]
    L += ["## C. wa_finding_entity_links", "",
          f"- total: {len(el)} | active: {len(ela)}",
          "- entity_type (active): " + ", ".join(f"{k}={v}" for k, v in Counter(r["entity_type"] for r in ela).most_common()),
          f"- entity_strongs populated (active): {sum(1 for r in ela if r['entity_strongs'])}/{len(ela)}",
          "- entity_strongs → cluster bucket: " + ", ".join(f"{k}={v}" for k, v in Counter(bucket(r["entity_strongs"], smap) for r in ela).most_common()), ""]

    # ---- D. session_d_* structured tables ----
    L += ["## D. session_d_* structured tables", "",
          "All four (`session_d_runs`, `session_d_observations`, `session_d_term_links`, `session_d_verse_links`) are **empty (0 rows)** — Session D's structured capture was never populated; SD pointers exist only as `SD_POINTER`/`SD_CLUSTER` flags (section B).", ""]

    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as fh:
        fh.write("\n".join(L) + "\n")
    print(f"wrote: {OUT}")
    print("findings active:", len(active), "| SB_findings term_id buckets:", dict(fb))
    conn.close()


if __name__ == "__main__":
    main()
