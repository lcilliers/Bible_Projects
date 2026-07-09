"""Step (a): inspect no-link pointers (cluster_link NULL) for retention/close.

Splits the no-link set so we DON'T wrongly close evidenced items:
  - TRULY NON-EVIDENCED : no cluster link AND no named term AND no verse evidence
                          (anchor_verses empty + no inline verse ref) -> clean set-aside candidate
  - VERSE-EVIDENCED      : no named-term link, but carries verse evidence
                          (anchor_verses or inline verse ref) -> NOT non-evidenced; needs a call

Read-only.
Output: research/investigations/pointer-nolink-retention-20260601.md
"""
import os
import re
import sqlite3
from collections import Counter

DB = "database/bible_research.db"
OUT = "research/investigations/pointer-nolink-retention-20260601.md"
VERSE_RE = re.compile(r"\b([1-3]?\s?[A-Z][a-zA-Z]{1,4})\.?\s+(\d{1,3}):(\d{1,3})")
FLAG_CODES = ("SD_POINTER", "SB_FINDING", "SB_INNER_BEING", "SD_CLUSTER")


def has_verse(*texts):
    for t in texts:
        if t and VERSE_RE.search(t):
            return True
    return False


def main():
    conn = sqlite3.connect(DB, timeout=15); conn.row_factory = sqlite3.Row
    cur = conn.cursor()

    findings = cur.execute("SELECT id, finding_type ft, status, anchor_verses av, finding FROM wa_session_b_findings WHERE COALESCE(delete_flag,0)=0 AND cluster_link IS NULL").fetchall()
    f_empty = []; f_verse = []
    for r in findings:
        if (r["av"] and r["av"].strip()) or has_verse(r["finding"]):
            f_verse.append(r)
        else:
            f_empty.append(r)

    ph = ",".join("?" * len(FLAG_CODES))
    flags = cur.execute(f"SELECT id, flag_code fc, flag_label fl, description d, strongs_reference sr FROM wa_session_research_flags WHERE flag_code IN ({ph}) AND cluster_link IS NULL", FLAG_CODES).fetchall()
    fl_empty = []; fl_verse = []
    for r in flags:
        if (r["sr"] and r["sr"].strip()) or has_verse(r["fl"], r["d"]):
            fl_verse.append(r)
        else:
            fl_empty.append(r)

    L = ["# No-link pointers — retention / close inspection (step a)", "",
         "**Generated:** 2026-06-01 (read-only). `cluster_link IS NULL` = no named-term link to a cluster. Split so evidenced items are NOT closed as 'non-evidenced'.", "",
         "## Summary", "",
         f"- **wa_session_b_findings no-link: {len(findings)}** → truly non-evidenced **{len(f_empty)}** · verse-evidenced (keep/decide) **{len(f_verse)}**",
         f"- **pointer flags no-link: {len(flags)}** → truly non-evidenced **{len(fl_empty)}** · has strongs-ref/verse (keep/decide) **{len(fl_verse)}**", "",
         "**Clean set-aside-non-evidenced candidates = the 'truly non-evidenced' rows** (no term, no verse). The verse-evidenced rows have evidence but no named subject term — closing them as non-evidenced would be wrong; they need a separate call (route via verse as last resort, or hold).", "",
         "finding_type of truly-non-evidenced findings: " + ", ".join(f"{k}={v}" for k, v in Counter(r["ft"] for r in f_empty).most_common(12)), "",
         "## Truly non-evidenced — wa_session_b_findings (clean close candidates)", "",
         "| id | type | status | text |", "|---|---|---|---|"]
    for r in sorted(f_empty, key=lambda r: len(r["finding"] or "")):
        txt = (r["finding"] or "").replace("|", "/").replace("\n", " ")
        txt = (txt[:150] + "…") if len(txt) > 151 else txt
        L.append(f"| {r['id']} | {r['ft']} | {r['status']} | {txt} |")

    L += ["", "## Truly non-evidenced — pointer flags (clean close candidates)", "", "| id | code | text |", "|---|---|---|"]
    for r in sorted(fl_empty, key=lambda r: len(((r["fl"] or "") + (r["d"] or "")))):
        txt = ((r["fl"] or "") + " — " + (r["d"] or "")).replace("|", "/").replace("\n", " ")
        txt = (txt[:150] + "…") if len(txt) > 151 else txt
        L.append(f"| {r['id']} | {r['fc']} | {txt} |")

    L += ["", "## Verse-evidenced but unanchored (NOT auto-close) — counts only", "",
          f"- findings: {len(f_verse)} (have `anchor_verses`/inline verse but no named subject term)",
          f"- flags: {len(fl_verse)}", "",
          "These need your call: they carry verse evidence, so they are not 'non-evidenced'. Options: (i) route via verse as a last-resort lower-confidence link, (ii) hold for the owning cluster's analysis, (iii) treat 'no named term' as itself disqualifying and set aside. Listed on request."]

    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as f:
        f.write("\n".join(L) + "\n")
    print(f"findings no-link {len(findings)}: empty {len(f_empty)}, verse {len(f_verse)}")
    print(f"flags no-link {len(flags)}: empty {len(fl_empty)}, verse {len(fl_verse)}")
    print("wrote:", OUT)
    conn.close()


if __name__ == "__main__":
    main()
