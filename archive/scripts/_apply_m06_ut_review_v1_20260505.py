"""_apply_m06_ut_review_v1_20260505.py — DB-modifying.

Parse Sessions/Session_Clusters/M06/WA-M06-UT-verse-review-v1-2026-05-05.md
and apply the reviewer's decisions to verse_context:

  - "No" decisions  → INSERT verse_context with set_aside_reason populated,
                      is_relevant=0, group_id=NULL
  - "Yes" decisions → INSERT verse_context with is_relevant=1; group_id set
                      if the proposal cites a single existing group; notes
                      capturing the proposal text; set_aside_reason=NULL
  - "Borderline"    → no DB write (per file: "needs researcher decision");
                      logged for follow-up

Idempotent: skips if a verse_context row already exists for
(verse_record_id, mti_term_id) with non-deleted state. Backed up first.
"""
from __future__ import annotations

import os
import re
import shutil
import sqlite3
import sys
from collections import defaultdict
from datetime import datetime, timezone

DB_PATH = os.path.join("database", "bible_research.db")
BACKUP_DIR = "backups"
REVIEW_FILE = os.path.join(
    "Sessions", "Session_Clusters", "M06",
    "WA-M06-UT-verse-review-v1-2026-05-05.md"
)


# Reviewer decision rows in the file follow:
# | H8130 sa.ne | Lev 26:17 | "verse text..." | term meaning ... |
#   **Yes** | Proposed group: ... |
ROW_RE = re.compile(
    r"^\|\s*(?P<strong>[HG]\d{4}[A-Z]?)\s+\S+\s*"  # column 1: strong + translit
    r"\|\s*(?P<ref>[^|]+?)\s*"                       # column 2: verse ref
    r"\|\s*[^|]*\s*"                                  # column 3: verse text (ignored)
    r"\|\s*[^|]*\s*"                                  # column 4: term meaning (ignored)
    r"\|\s*\**(?P<decision>Yes|No|Borderline)\**\s*"  # column 5: decision
    r"\|\s*(?P<note>.*?)\s*\|"                        # column 6: decision note
)
# Reference parsing (book chap:verse)
REF_RE = re.compile(
    r"^(?P<book>\d?[A-Za-z]+)\s+(?P<chap>\d+):(?P<verse>\d+)$"
)


def now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def backup_db() -> str:
    os.makedirs(BACKUP_DIR, exist_ok=True)
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    dest = os.path.join(
        BACKUP_DIR, f"bible_research_{ts}_pre_m06_ut_review.db"
    )
    shutil.copy2(DB_PATH, dest)
    return dest


def build_book_lookup(conn):
    out = {}
    for r in conn.execute(
        "SELECT id, name, abbreviation, short_code FROM books"
    ).fetchall():
        bid = r["id"]
        for k in (r["abbreviation"], r["short_code"], r["name"]):
            if k:
                out[k.lower()] = bid
    return out


def parse_review_file(path):
    """Yield dicts {strong, ref, decision, note}."""
    with open(path, encoding="utf-8") as f:
        for line in f:
            m = ROW_RE.match(line)
            if not m:
                continue
            yield {
                "strong": m.group("strong"),
                "ref": m.group("ref"),
                "decision": m.group("decision"),
                "note": m.group("note").strip(),
                "raw_line": line.rstrip(),
            }


def extract_group_proposal(note):
    """Return single int group_id if the note cites a single group cleanly,
    else None."""
    # Look for "group <num>" (single int)
    m = re.search(r"\bgroup\s+(\d+)\b", note, re.IGNORECASE)
    if m:
        # Check it isn't part of a range like "groups 136–138"
        following = note[m.end():m.end()+5]
        if re.match(r"\s*[–-]\s*\d", following):
            return None
        return int(m.group(1))
    return None


def main() -> int:
    print(f"Review file: {REVIEW_FILE}")
    print(f"DB: {DB_PATH}")
    print(f"Backing up...", flush=True)
    bak = backup_db()
    print(f"  -> {bak}\n")

    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    book_lookup = build_book_lookup(conn)

    rows = list(parse_review_file(REVIEW_FILE))
    print(f"Parsed rows: {len(rows)}")

    # Group by decision
    by_decision = defaultdict(list)
    for r in rows:
        by_decision[r["decision"]].append(r)
    print(f"  Yes: {len(by_decision['Yes'])}")
    print(f"  No:  {len(by_decision['No'])}")
    print(f"  Borderline: {len(by_decision['Borderline'])}")

    # Build resolution plan
    plan = []
    issues = []
    for r in rows:
        ref = r["ref"]
        m = REF_RE.match(ref)
        if not m:
            issues.append(f"Cannot parse ref: '{ref}'")
            continue
        book_token = m.group("book")
        chap = int(m.group("chap"))
        verse = int(m.group("verse"))
        bid = book_lookup.get(book_token.lower())
        if not bid:
            issues.append(f"Unknown book: '{book_token}' for {ref}")
            continue
        # Find the wa_verse_record for this (book/chap/verse) where
        # mti_term_id has cluster_code='M06' AND strongs_number matches r['strong']
        vrs = conn.execute("""
            SELECT vr.id AS vr_id, vr.mti_term_id, mt.strongs_number
              FROM wa_verse_records vr
              JOIN mti_terms mt ON mt.id = vr.mti_term_id
             WHERE vr.book_id = ? AND vr.chapter = ? AND vr.verse_num = ?
               AND mt.strongs_number = ?
               AND COALESCE(vr.delete_flagged,0) = 0
        """, (bid, chap, verse, r["strong"])).fetchall()
        if not vrs:
            issues.append(f"No wa_verse_record for {r['strong']} {ref}")
            continue
        # Most often there is one (sometimes duplicates per mti_id duplicates)
        for vr in vrs:
            plan.append({
                "strong": r["strong"],
                "ref": ref,
                "book_id": bid,
                "chapter": chap,
                "verse_num": verse,
                "vr_id": vr["vr_id"],
                "mti_term_id": vr["mti_term_id"],
                "decision": r["decision"],
                "note": r["note"],
            })

    print(f"\nPlan rows: {len(plan)}")
    if issues:
        print(f"\n⚠ {len(issues)} resolution issues:")
        for i in issues[:10]:
            print(f"  - {i}")
        if len(issues) > 10:
            print(f"  - …{len(issues) - 10} more")

    # Resolve group proposals for Yes decisions
    yes_with_group = 0
    yes_no_group = 0
    for p in plan:
        if p["decision"] != "Yes":
            continue
        gid = extract_group_proposal(p["note"])
        p["proposed_group_id"] = gid
        if gid is not None:
            yes_with_group += 1
        else:
            yes_no_group += 1
    print(f"\nYes with single group_id: {yes_with_group}")
    print(f"Yes with no/range group:   {yes_no_group}")

    # Apply
    print("\nApplying...", flush=True)
    n_inserted = 0
    n_skipped = 0
    n_borderline_skipped = 0
    audit = []
    try:
        conn.execute("BEGIN")
        for p in plan:
            if p["decision"] == "Borderline":
                n_borderline_skipped += 1
                continue
            # Check if a verse_context row already exists
            existing = conn.execute("""
                SELECT id FROM verse_context
                 WHERE mti_term_id = ? AND verse_record_id = ?
                   AND COALESCE(delete_flagged,0) = 0
            """, (p["mti_term_id"], p["vr_id"])).fetchone()
            if existing:
                n_skipped += 1
                audit.append({
                    "strong": p["strong"], "ref": p["ref"],
                    "outcome": "SKIPPED-already-has-vc", "vc_id": existing["id"],
                })
                continue
            if p["decision"] == "No":
                # Set-aside: populate set_aside_reason
                reason = p["note"]
                # Strip leading "Set aside —" if present
                reason = re.sub(r"^Set aside\s*[—\-:]\s*", "", reason)
                conn.execute("""
                    INSERT INTO verse_context
                      (verse_record_id, mti_term_id, group_id,
                       is_anchor, is_relevant, is_related, notes,
                       delete_flagged, set_aside_reason, analysis_note)
                    VALUES (?, ?, NULL, 0, 0, 0, ?, 0, ?, ?)
                """, (
                    p["vr_id"], p["mti_term_id"],
                    "M06 UT review v1 (2026-05-05)",
                    reason,
                    "Source: WA-M06-UT-verse-review-v1-2026-05-05",
                ))
                n_inserted += 1
                audit.append({
                    "strong": p["strong"], "ref": p["ref"],
                    "outcome": "INSERTED-set-aside",
                    "set_aside_reason": reason,
                })
            elif p["decision"] == "Yes":
                gid = p.get("proposed_group_id")
                conn.execute("""
                    INSERT INTO verse_context
                      (verse_record_id, mti_term_id, group_id,
                       is_anchor, is_relevant, is_related, notes,
                       delete_flagged, set_aside_reason, analysis_note)
                    VALUES (?, ?, ?, 0, 1, 0, ?, 0, NULL, ?)
                """, (
                    p["vr_id"], p["mti_term_id"], gid,
                    "M06 UT review v1 (2026-05-05): "
                    + ("group=" + str(gid) if gid else "group pending")
                    + " — " + p["note"],
                    "Source: WA-M06-UT-verse-review-v1-2026-05-05",
                ))
                n_inserted += 1
                audit.append({
                    "strong": p["strong"], "ref": p["ref"],
                    "outcome": "INSERTED-relevant",
                    "group_id": gid,
                })
        conn.execute("COMMIT")
        print(f"  ✓ inserted: {n_inserted}")
        print(f"  ⏭ skipped (already had VC row): {n_skipped}")
        print(f"  ⏸ borderline (left UT — researcher review): "
              f"{n_borderline_skipped}")
    except Exception as e:
        conn.execute("ROLLBACK")
        print(f"  ✗ ERROR — rolled back: {e}")
        raise

    # Verification
    print("\nVerification — current verse_context status for all 34 "
          "review rows:")
    status_counts = defaultdict(int)
    for p in plan:
        rec = conn.execute("""
            SELECT id, group_id, is_relevant, set_aside_reason
              FROM verse_context
             WHERE mti_term_id = ? AND verse_record_id = ?
               AND COALESCE(delete_flagged,0) = 0
        """, (p["mti_term_id"], p["vr_id"])).fetchone()
        if not rec:
            status_counts["UT"] += 1
        elif rec["set_aside_reason"]:
            status_counts["SA"] += 1
        elif rec["group_id"] and rec["group_id"] > 0 and rec["is_relevant"] == 1:
            status_counts["G"] += 1
        elif rec["is_relevant"] == 1:
            status_counts["P-relevant-no-group"] += 1
        elif rec["is_relevant"] == 0:
            status_counts["NR"] += 1
        else:
            status_counts["other"] += 1
    for k, v in status_counts.items():
        print(f"  {k}: {v}")

    conn.close()
    return 0


if __name__ == "__main__":
    sys.exit(main())
