"""_apply_link_mti_term_id.py — D2a (2026-06-15): populate the missing wa_verse_records.mti_term_id link
for ACTIVE verses whose term_id matches an existing mti_terms row but link is NULL.

First resolves the OT-DBR-009 ambiguity that blocks linking: where a link-target strongs has TWO active
mti_terms rows (one marked status='delete', one live, both with no active data), the status='delete' row
is soft-deleted (completing the deletion that was marked but never applied), leaving one canonical target.

Then links each active mti-NULL verse to the SINGLE live mti_terms row for its term_id. Records every
touched id to a sidecar JSON for reversal.

  python scripts/_apply_link_mti_term_id.py --dry-run --out <f>.md
  python scripts/_apply_link_mti_term_id.py --live    --out <f>.md   # writes <f>.ids.json
  python scripts/_apply_link_mti_term_id.py --reverse <f>.ids.json
"""
import argparse, json, os, sqlite3, sys
sys.stdout.reconfigure(encoding="utf-8")
DB = os.path.join("database", "bible_research.db")


def main():
    ap = argparse.ArgumentParser()
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--dry-run", action="store_true")
    g.add_argument("--live", action="store_true")
    g.add_argument("--reverse", metavar="IDS_JSON")
    ap.add_argument("--out")
    a = ap.parse_args()
    conn = sqlite3.connect(DB, timeout=120)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()

    if a.reverse:
        d = json.load(open(a.reverse, encoding="utf-8"))
        for vid in d.get("linked_verses", []):
            cur.execute("UPDATE wa_verse_records SET mti_term_id=NULL WHERE id=?", (vid,))
        for mid in d.get("softdeleted_mti", []):
            cur.execute("UPDATE mti_terms SET delete_flagged=0 WHERE id=?", (mid,))
        conn.commit()
        print(f"REVERSED: unlinked {len(d.get('linked_verses',[]))} verses, restored {len(d.get('softdeleted_mti',[]))} mti rows")
        return

    # ── 1. resolve blocking duplicates: status='delete' rows that share a strongs with a live row,
    #        for strongs that are link targets, with no active data ────────────────────────────────
    amb = cur.execute("""
        SELECT DISTINCT vr.term_id sn FROM wa_verse_records vr
        WHERE COALESCE(vr.delete_flagged,0)=0 AND vr.mti_term_id IS NULL AND vr.term_id IS NOT NULL
          AND (SELECT COUNT(*) FROM mti_terms m WHERE m.strongs_number=vr.term_id
                 AND COALESCE(m.delete_flagged,0)=0 AND COALESCE(m.status,'')<>'delete') = 1
          AND (SELECT COUNT(*) FROM mti_terms m WHERE m.strongs_number=vr.term_id
                 AND COALESCE(m.delete_flagged,0)=0 AND m.status='delete') >= 1
    """).fetchall()
    blockers = []
    for r in amb:
        for m in cur.execute("""SELECT id FROM mti_terms WHERE strongs_number=? AND status='delete'
                 AND COALESCE(delete_flagged,0)=0
                 AND NOT EXISTS(SELECT 1 FROM wa_verse_records vr WHERE vr.mti_term_id=mti_terms.id AND COALESCE(vr.delete_flagged,0)=0)
                 AND NOT EXISTS(SELECT 1 FROM finding f WHERE f.mti_term_id=mti_terms.id AND COALESCE(f.delete_flagged,0)=0)""",
                 (r["sn"],)):
            blockers.append(m["id"])

    # ── 2. link active mti-NULL verses to the single live mti_terms row for their term_id ──────────
    if not a.dry_run:
        for mid in blockers:
            cur.execute("UPDATE mti_terms SET delete_flagged=1 WHERE id=?", (mid,))
        conn.commit()

    to_link = cur.execute("""
        SELECT vr.id vid,
          (SELECT m.id FROM mti_terms m WHERE m.strongs_number=vr.term_id
             AND COALESCE(m.delete_flagged,0)=0 AND COALESCE(m.status,'')<>'delete') mtid
        FROM wa_verse_records vr
        WHERE COALESCE(vr.delete_flagged,0)=0 AND vr.mti_term_id IS NULL AND vr.term_id IS NOT NULL
          AND (SELECT COUNT(*) FROM mti_terms m WHERE m.strongs_number=vr.term_id
                 AND COALESCE(m.delete_flagged,0)=0 AND COALESCE(m.status,'')<>'delete') = 1
    """).fetchall()
    linked = [(r["vid"], r["mtid"]) for r in to_link]

    if a.live:
        for vid, mtid in linked:
            cur.execute("UPDATE wa_verse_records SET mti_term_id=? WHERE id=?", (mtid, vid))
        conn.commit()

    L = [f"# D2a — link mti_term_id ({'DRY-RUN' if a.dry_run else 'LIVE'})", "",
         f"- blocking status='delete' duplicate mti_terms soft-deleted: **{len(blockers)}**",
         f"- active verses linked to their mti_terms row: **{len(linked)}**"]
    print("\n".join(L[2:]))
    if a.live:
        ids = (a.out or "d2a") + ".ids.json"
        json.dump({"softdeleted_mti": blockers, "linked_verses": [v for v, _ in linked]},
                  open(ids, "w", encoding="utf-8"))
        L.append(f"\n**LIVE.** Reversal ids → `{ids}`.")
        print(f"LIVE done; reversal → {ids}")
    else:
        L.append("\n**DRY-RUN — no writes.**")
    if a.out:
        os.makedirs(os.path.dirname(a.out), exist_ok=True)
        open(a.out, "w", encoding="utf-8").write("\n".join(L))


if __name__ == "__main__":
    main()
