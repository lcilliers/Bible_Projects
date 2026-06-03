"""CORRECTED comprehensive linkage test for Session B/D pointers.

Supersedes the earlier no-link/retention analysis, which only checked
cluster_link + verse and wrongly ignored the subsidiary link tables. A pointer is
'genuinely orphaned' ONLY if it has none of the following linkage routes:

wa_session_b_findings:
  - cluster_link (named-term -> cluster)
  - wa_finding_catalogue_links  (tier/observation-catalogue question)  <-- previously missed
  - verse evidence: anchor_verses or inline verse ref
  - session_c_chapter (consumed into Session C)
  - sd_pointer_ref / related_finding_id

wa_session_research_flags (pointer codes):
  - cluster_link
  - strongs_reference
  - verse in flag_label/description
  - wa_prose_section_citations.cited_sd_pointer_id (cited in prose)
  - resolved=1 (already closed)

Read-only.
Output: research/investigations/pointer-full-linkage-20260601.md
"""
import os
import re
import sqlite3
from collections import Counter

DB = "database/bible_research.db"
OUT = "research/investigations/pointer-full-linkage-20260601.md"
VERSE_RE = re.compile(r"\b([1-3]?\s?[A-Z][a-zA-Z]{1,4})\.?\s+(\d{1,3}):(\d{1,3})")
FLAG_CODES = ("SD_POINTER", "SB_FINDING", "SB_INNER_BEING", "SD_CLUSTER")


def hasverse(*t):
    return any(x and VERSE_RE.search(x) for x in t)


def main():
    c = sqlite3.connect(DB, timeout=15); c.row_factory = sqlite3.Row

    cat = {r["finding_id"] for r in c.execute("SELECT DISTINCT finding_id FROM wa_finding_catalogue_links WHERE COALESCE(delete_flagged,0)=0")}
    cited_ptr = {r["cited_sd_pointer_id"] for r in c.execute("SELECT DISTINCT cited_sd_pointer_id FROM wa_prose_section_citations WHERE cited_sd_pointer_id IS NOT NULL")}

    # findings
    f = c.execute("SELECT id, finding_type ft, status, anchor_verses av, finding, cluster_link cl, session_c_chapter scc, sd_pointer_ref sdr, related_finding_id rfi FROM wa_session_b_findings WHERE COALESCE(delete_flag,0)=0").fetchall()
    route = Counter(); orphan_f = []
    for r in f:
        routes = []
        if r["cl"]:
            routes.append("cluster_link")
        if r["id"] in cat:
            routes.append("tier_question")
        if (r["av"] and r["av"].strip()) or hasverse(r["finding"]):
            routes.append("verse")
        if r["scc"]:
            routes.append("session_c")
        if r["sdr"] or r["rfi"]:
            routes.append("sd/related_ref")
        for x in routes:
            route[x] += 1
        if not routes:
            orphan_f.append(r)

    # flags
    fl = c.execute(f"SELECT id, flag_code fc, flag_label flb, description d, cluster_link cl, strongs_reference sr, COALESCE(resolved,0) res FROM wa_session_research_flags WHERE flag_code IN ({','.join('?'*len(FLAG_CODES))})", FLAG_CODES).fetchall()
    routef = Counter(); orphan_fl = []
    for r in fl:
        routes = []
        if r["cl"]:
            routes.append("cluster_link")
        if r["sr"] and r["sr"].strip():
            routes.append("strongs_ref")
        if hasverse(r["flb"], r["d"]):
            routes.append("verse")
        if r["id"] in cited_ptr:
            routes.append("prose_cited")
        if r["res"]:
            routes.append("resolved")
        for x in routes:
            routef[x] += 1
        if not routes:
            orphan_fl.append(r)

    L = ["# Session B/D pointers — CORRECTED full-linkage assessment", "",
         "**Generated:** 2026-06-01 (read-only). Supersedes pointer-nolink-retention: that omitted the subsidiary link tables (notably `wa_finding_catalogue_links`). A pointer is genuinely orphaned only if it has NO linkage route at all.", "",
         "## Subsidiary link tables now included",
         "- `wa_finding_catalogue_links` (6,199) — finding → tier/observation-catalogue question. **2,632/2,883 findings linked.**",
         "- `finding_citation` (75,080) — structured verse/strongs/vcg citations, but for `cluster_finding`/`cluster_observation` (NOT Session B findings).",
         "- `cluster_finding` (21,508) / `cluster_observation` (276) — the cluster-analysis finding layer (own citations).",
         "- `wa_prose_section_citations` — cited_sd_pointer_id (38), cited_finding_id (310).", "",
         "## wa_session_b_findings (2,883 active) — linkage routes (a finding may have several)", ""]
    for k, v in route.most_common():
        L.append(f"- {k}: {v}")
    L += ["", f"**Genuinely orphaned findings (NO route at all): {len(orphan_f)}**", "",
          "## wa_session_research_flags pointer flags — linkage routes", ""]
    for k, v in routef.most_common():
        L.append(f"- {k}: {v}")
    L += ["", f"**Genuinely orphaned flags (NO route, not resolved): {len(orphan_fl)}**", "",
          "## Genuinely orphaned — the true set-aside-non-evidenced candidates", "",
          "### findings", "", "| id | type | status | text |", "|---|---|---|---|"]
    for r in sorted(orphan_f, key=lambda r: len(r["finding"] or "")):
        t = (r["finding"] or "").replace("|", "/").replace("\n", " ")
        L.append(f"| {r['id']} | {r['ft']} | {r['status']} | {(t[:150]+'…') if len(t)>151 else t} |")
    L += ["", "### flags", "", "| id | code | text |", "|---|---|---|"]
    for r in sorted(orphan_fl, key=lambda r: len((r["flb"] or "")+(r["d"] or ""))):
        t = ((r["flb"] or "")+" — "+(r["d"] or "")).replace("|", "/").replace("\n", " ")
        L.append(f"| {r['id']} | {r['fc']} | {(t[:150]+'…') if len(t)>151 else t} |")

    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as fh:
        fh.write("\n".join(L) + "\n")
    print(f"findings genuinely orphaned: {len(orphan_f)} | flags genuinely orphaned: {len(orphan_fl)}")
    print("finding routes:", dict(route)); print("flag routes:", dict(routef))
    print("wrote:", OUT)
    c.close()


if __name__ == "__main__":
    main()
