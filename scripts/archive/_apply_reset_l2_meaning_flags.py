"""_apply_reset_l2_meaning_flags.py — WRITES. Recomputes finding.flagged_for_review for ALL l2_meaning
paragraphs on a single uniform, reproducible basis: a FREE-TEXT content field (immediate_response,
produces_effect, relational_implication, purpose_equips) whose value shares NO significant word with the
paragraph = flag. Replaces the pilot's over-strict flags (which counted option-list fields + note-then-OK API
selfaudits). The API selfaudit text isn't persisted, so the CC free-text backstop is the durable signal.
"""
import sqlite3, re, sys, os
sys.stdout.reconfigure(encoding="utf-8")
DB = os.path.join("database", "bible_research.db")
FT_OBS = {248: "immediate_response", 251: "produces_effect", 238: "relational_implication", 227: "purpose_equips"}
NULL = {"none", "silent", "not-stated", "n/a", "na", ""}
STOP = {"the", "and", "that", "with", "from", "this", "into", "upon", "have", "been", "which", "their", "person", "something"}

c = sqlite3.connect(DB); c.row_factory = sqlite3.Row
# paragraph per (vcid, mid)
para = {(r["verse_context_id"], r["mti_term_id"]): (r["id"], r["finding_value"] or "")
        for r in c.execute("SELECT id, verse_context_id, mti_term_id, finding_value FROM finding WHERE provenance='l2_meaning'")}
# free-text field values per (vcid, mid)
ft = {}
for r in c.execute("""SELECT f.verse_context_id v, f.mti_term_id m, l.question_id q, f.finding_value val
                      FROM finding f JOIN finding_question_link l ON l.finding_id=f.id
                      WHERE f.provenance='l2_api' AND l.question_id IN (248,251,238,227)"""):
    ft.setdefault((r["v"], r["m"]), {})[FT_OBS[r["q"]]] = r["val"]

flag_on, flag_off = 0, 0
cur = c.cursor()
for key, (fid, p) in para.items():
    pw = set(re.findall(r"[a-z]{4,}", p.lower()))
    miss = False
    for k, val in ft.get(key, {}).items():
        low = (val or "").lower().strip()
        if low in NULL:
            continue
        w = {x for x in re.findall(r"[a-z]{4,}", low) if x not in STOP}
        if w and not (w & pw):
            miss = True; break
    cur.execute("UPDATE finding SET flagged_for_review=? WHERE id=?", (1 if miss else 0, fid))
    if miss: flag_on += 1
    else: flag_off += 1
c.commit()
print(f"recomputed flags on {len(para)} paragraphs: flagged={flag_on} ({100*flag_on/len(para):.0f}%) clear={flag_off}")
