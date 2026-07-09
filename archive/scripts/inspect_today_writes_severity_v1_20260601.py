"""Severity of today's term-writes, judged on the COMPLETE evidence signal (term_id),
using the 2026-05-28 backup to identify exactly which rows today's writes changed.

For every mti_terms row whose (delete_flagged, exclusion_reason) differs from the
backup (= touched today), group by strongs_number and classify:
  - has active term_id verse records (df=0)?  -> my mti_term_id guard may have missed it
  - does the strongs still have ANY live (df=0) mti_terms row?
      no  -> FULLY DELETED real-evidence term (G3958 class: term gone, verses live)
      yes -> has a live sibling row (concept survives; a secondary row was touched)

Read-only.
Output: research/investigations/today-writes-severity-20260601.md
  python scripts/inspect_today_writes_severity_v1_20260601.py
"""
import os
import sqlite3
from collections import defaultdict

DB = os.path.join("database", "bible_research.db")
BACKUP = os.path.join("backups", "bible_research_backup_20260528_065554_wa-cluster-M38-patch-borderline-resolution-v1-20260528.db")
OUT = os.path.join("research", "investigations", "today-writes-severity-20260601.md")


def load(path):
    c = sqlite3.connect(path, timeout=10); c.row_factory = sqlite3.Row
    d = {r["id"]: (r["COALESCE(delete_flagged,0)" if False else "df"], r["rsn"])
         for r in c.execute("SELECT id, COALESCE(delete_flagged,0) df, COALESCE(exclusion_reason,'') rsn FROM mti_terms")}
    c.close(); return d


def main():
    livec = sqlite3.connect(DB, timeout=10); livec.row_factory = sqlite3.Row
    live = {r["id"]: (r["df"], r["rsn"], r["strongs_number"], r["cluster_code"], r["status"])
            for r in livec.execute("SELECT id, COALESCE(delete_flagged,0) df, COALESCE(exclusion_reason,'') rsn, strongs_number, cluster_code, status FROM mti_terms")}
    bak = load(BACKUP)

    # active verse records by term_id (the COMPLETE signal)
    active = defaultdict(int)
    for r in livec.execute("SELECT term_id, COALESCE(delete_flagged,0) df FROM wa_verse_records WHERE term_id IS NOT NULL"):
        if r["df"] == 0:
            active[r["term_id"]] += 1

    # strongs -> does it have any live (df=0) mti_terms row (in LIVE db)?
    has_live_row = defaultdict(bool)
    for _id, (df, rsn, sn, cc, st) in live.items():
        if df == 0:
            has_live_row[sn] = True

    # rows touched today = (df or reason) differs from backup
    touched = [(_id, v) for _id, v in live.items() if bak.get(_id) and (v[0] != bak[_id][0] or v[1] != bak[_id][1])]

    touched_strongs = sorted({v[2] for _id, v in touched})
    with_ev = [sn for sn in touched_strongs if active.get(sn, 0) > 0]
    fully_deleted = [sn for sn in with_ev if not has_live_row[sn]]      # G3958 class
    live_sibling = [sn for sn in with_ev if has_live_row[sn]]

    fd_verses = sum(active[sn] for sn in fully_deleted)
    ls_verses = sum(active[sn] for sn in live_sibling)

    livec2 = livec.cursor()
    def gloss(sn):
        r = livec2.execute("SELECT gloss FROM mti_terms WHERE strongs_number=? LIMIT 1", (sn,)).fetchone()
        return r["gloss"] if r else ""

    L = ["# Severity of today's term-writes (judged on term_id, the complete signal)", "",
         f"**Backup baseline:** `{os.path.basename(BACKUP)}` (pre-today).",
         f"- mti_terms rows changed today (delete_flagged or exclusion_reason): **{len(touched)}**",
         f"- distinct strongs touched today: **{len(touched_strongs)}**",
         f"- of those, strongs with ACTIVE verses under term_id (guard should have spared them): **{len(with_ev)}**", "",
         f"## A. FULLY DELETED yet have live verses (G3958 class — term gone, evidence stranded): {len(fully_deleted)} strongs / {fd_verses} active verses",
         "These are the serious cases: no live mti_terms row remains, yet live verses exist under term_id.", "",
         "| strongs | gloss | active term_id verses |", "|---|---|---:|"]
    for sn in sorted(fully_deleted, key=lambda s: -active[s]):
        L.append(f"| {sn} | {(gloss(sn) or '').replace('|','/')} | {active[sn]} |")
    L += ["", f"## B. Still have a LIVE sibling row (concept survives; a secondary row was touched): {len(live_sibling)} strongs / {ls_verses} active verses", "",
          "| strongs | gloss | active term_id verses |", "|---|---|---:|"]
    for sn in sorted(live_sibling, key=lambda s: -active[s]):
        L.append(f"| {sn} | {(gloss(sn) or '').replace('|','/')} | {active[sn]} |")

    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as f:
        f.write("\n".join(L) + "\n")
    print(f"touched_rows={len(touched)} touched_strongs={len(touched_strongs)} with_active_termid_verses={len(with_ev)}")
    print(f"  A fully-deleted (G3958 class): {len(fully_deleted)} strongs / {fd_verses} verses")
    print(f"  B has live sibling row: {len(live_sibling)} strongs / {ls_verses} verses")
    print(f"wrote: {OUT}")
    livec.close()


if __name__ == "__main__":
    main()
