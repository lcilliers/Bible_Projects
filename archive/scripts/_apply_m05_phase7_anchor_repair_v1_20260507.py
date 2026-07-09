"""_apply_m05_phase7_anchor_repair_v1_20260507.py — DB-modifying.

Repairs the anchor-overwrite bug from the prior phase-7 apply: the DUAL
phase used the same upsert function as the ANCHOR phase, with
is_anchor=0 default, which clobbered freshly-set anchors on the same
(vr, mti, group) tuples.

This repair re-clears + re-sets all M05 group anchors. It does not
touch any other state. Idempotent.

Also fixes book-lookup gaps revealed in diagnosis:
  - Song of Solomon short_code is "Son" not "Sng"
  - Single-chapter book references like "3Jo 15" → resolve to chap=1
"""
from __future__ import annotations

import os
import re
import sqlite3
import sys
from datetime import datetime, timezone

DB_PATH = os.path.join("database", "bible_research.db")

# Same anchor list as the prior apply (101 entries plus split anchors set
# in their own logic — splits already handled correctly).
ANCHORS = [
    # M05-A
    (1537, "Mat 22:37", 571), (1538, "Joh 13:1", 571),
    (1539, "Mat 5:44", 571), (1540, "Joh 13:34", 571),
    (1541, "Joh 3:19", 571), (1542, "1Jo 4:8", 562),
    (1543, "1Cor 13:4", 562), (1544, "2Cor 5:14", 562),
    (1555, "Tit 1:8", 566), (1556, "Heb 13:1", 558),
    (1557, "1Pe 3:8", 567), (1558, "Tit 2:4", 561),
    (1559, "Tit 3:4", 556), (1562, "Joh 11:36", 572),
    (1563, "Mat 10:37", 572), (1564, "Joh 21:17", 572),
    (1567, "Jam 4:4", 1588), (157, "Tit 1:8", 1582),
    (158, "1Pe 4:9", 1582), (159, "Heb 13:2", 1585),
    (1572, "Joh 15:15", 1579), (1573, "Rom 12:10", 554),
    (1574, "Tit 2:4", 559), (1576, "Pro 18:24", 1600),
    (1577, "Pro 5:19", 539), (1578, "Jer 31:3", 537),
    (1579, "2Sa 1:26", 537), (1580, "Pro 10:12", 537),
    (1584, "Rut 3:10", 536), (1585, "Hos 6:6", 536),
    (1586, "Psa 4:3", 540), (1588, "Jer 12:7", 535),
    (1598, "2Sa 16:16", 1623), (1823, "1Pe 3:8", 1009),
    (343, "2Sa 22:26", 1635),
    # M05-B
    (1596, "Isa 54:7", 544), (1595, "Psa 103:13", 551),
    (1594, "Exo 34:6", 1614), (1672, "Dan 2:18", 988),
    (349, "Lam 4:10", 1616), (1638, "2Cor 1:3", 992),
    (1639, "Luk 6:36", 3158), (331, "Rom 9:15", 731),
    (333, "Luk 15:20", 730), (2717, "Eph 4:32", 593),
    (334, "Heb 4:15", 734), (335, "1Pe 3:8", 3980),
    (337, "Jon 4:11", 3182), (338, "Deu 13:8", 3182),
    (630, "2Ch 36:15", 487), (339, "Isa 63:9", 2192),
    # M05-C
    (1628, "Rom 9:16", 981), (1629, "Mar 10:48", 981),
    (1630, "Mat 18:33", 981), (1631, "Heb 2:17", 3164),
    (1632, "Eph 2:4", 983), (1633, "Jam 2:13", 983),
    (1625, "Rom 1:31", 3165), (1626, "Jam 2:13", 993),
    (328, "Rev 3:17", 3168),
    # M05-D
    (1111, "Rom 11:22", 886), (1112, "Gal 5:22", 886),
    (1469, "Luk 6:35", 954), (1467, "1Cor 13:4", 5729),
    (1096, "Mar 10:18", 881), (1097, "Mat 12:35", 881),
    (1098, "Eph 2:10", 881), (1099, "Rom 8:28", 881),
    (1100, "Rom 7:19", 881), (1093, "1Pe 2:20", 1638),
    (1092, "1Ti 6:18", 1640), (1094, "1Pe 4:19", 1641),
    (1095, "1Pe 2:14", 1642), (687, "2Cor 11:3", 810),
    (688, "2Cor 9:11", 810), (2290, "2Cor 8:21", 1187),
    # M05-E
    (1104, "2Cor 10:1", 882), (1261, "1Pe 3:4", 46),
    (1262, "Jam 1:21", 47), (1102, "2Cor 10:1", 883),
    (1103, "Phili 4:5", 5425), (1272, "Pro 22:4", 189),
    (1271, "2Sa 22:36", 188), (867, "2Ti 2:24", 856),
    # M05-F
    (1741, "Isa 40:1", 445), (1742, "Isa 66:13", 445),
    (2741, "Song 4:9", 587), (3079, "Psa 94:19", 1292),
    (602, "2Cor 1:4", 510), (603, "Mar 5:23", 510),
    (3073, "2Cor 1:3", 1290), (3074, "Rom 15:4", 1290),
    (3075, "Phile 7", 1290),
    # M05-G
    (1055, "1Jo 1:3", 873), (1056, "Act 2:42", 873),
    (1057, "2Pe 1:4", 5367), (1058, "Mat 23:30", 5367),
    (1813, "1Pe 3:8", 1008), (1795, "Phili 2:20", 1402),
    (2069, "2Cor 5:19", 1093), (2849, "Eph 2:20", 7064),
]


def now_iso():
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def build_book_lookup(conn):
    out = {}
    for r in conn.execute(
        "SELECT id, name, abbreviation, short_code FROM books"
    ):
        bid = r["id"]
        for k in (r["abbreviation"], r["short_code"], r["name"]):
            if k:
                out[k.lower()] = bid
    aliases = {
        "1cor": "1Co", "2cor": "2Co", "1th": "1Th", "2th": "2Th",
        "phili": "Php", "phil": "Php", "1ti": "1Ti", "2ti": "2Ti",
        "phile": "Phm", "1pe": "1Pe", "2pe": "2Pe",
        "1jo": "1Jn", "2jo": "2Jn", "3jo": "3Jn",
        "song": "Son", "ps": "Psa", "ec": "Ecc",
        "rev": "Rev", "rv": "Rev",
        "deut": "Deu", "ezek": "Eze", "judg": "Jdg",
    }
    for alt, can in aliases.items():
        if can.lower() in out:
            out[alt.lower()] = out[can.lower()]
    return out


REF_RE_FULL = re.compile(
    r"^(?P<book>\d?[A-Za-z]{2,5})\s+(?P<chap>\d+):(?P<v>\d+)"
)
REF_RE_SHORT = re.compile(
    r"^(?P<book>\d?[A-Za-z]{2,5})\s+(?P<v>\d+)\s*$"
)
SINGLE_CHAPTER_BOOKS = {"Oba", "Phm", "2Jn", "3Jn", "Jud"}


def parse_ref(ref, book_lookup):
    s = ref.strip()
    m = REF_RE_FULL.match(s)
    if m:
        bid = book_lookup.get(m.group("book").lower())
        if bid:
            return (bid, int(m.group("chap")), int(m.group("v")))
        return None
    m = REF_RE_SHORT.match(s)
    if m:
        book = m.group("book")
        bid = book_lookup.get(book.lower())
        if bid:
            return (bid, 1, int(m.group("v")))
        return None
    return None


def vr_lookup(conn, book_lookup, ref, mti_id):
    parsed = parse_ref(ref, book_lookup)
    if not parsed:
        return None
    bid, chap, verse = parsed
    r = conn.execute(
        "SELECT id FROM wa_verse_records "
        " WHERE book_id=? AND chapter=? AND verse_num=? AND mti_term_id=? "
        "   AND COALESCE(delete_flagged,0)=0",
        (bid, chap, verse, mti_id),
    ).fetchone()
    return r["id"] if r else None


def main():
    print(f"DB: {DB_PATH}")
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    book_lookup = build_book_lookup(conn)

    halts = []
    n_set = 0

    try:
        conn.execute("BEGIN")

        # Clear all anchors on these groups
        groups_to_clear = {gid for gid, _, _ in ANCHORS}
        for gid in groups_to_clear:
            conn.execute(
                "UPDATE verse_context SET is_anchor=0 "
                " WHERE group_id=? AND is_anchor=1 "
                "   AND COALESCE(delete_flagged,0)=0",
                (gid,),
            )

        # Set anchors fresh
        for gid, ref, mti_id in ANCHORS:
            vr = vr_lookup(conn, book_lookup, ref, mti_id)
            if not vr:
                halts.append((gid, ref, mti_id))
                continue
            # Find existing row for (vr, mti, group)
            row = conn.execute(
                "SELECT id FROM verse_context "
                " WHERE verse_record_id=? AND mti_term_id=? "
                "   AND group_id=? AND COALESCE(delete_flagged,0)=0",
                (vr, mti_id, gid),
            ).fetchone()
            if row:
                conn.execute(
                    "UPDATE verse_context SET is_anchor=1 WHERE id=?",
                    (row["id"],),
                )
            else:
                conn.execute(
                    "INSERT INTO verse_context "
                    "  (verse_record_id, mti_term_id, group_id, "
                    "   is_anchor, is_relevant, is_related, notes, "
                    "   delete_flagged, set_aside_reason) "
                    "VALUES (?, ?, ?, 1, 1, 0, ?, 0, NULL)",
                    (vr, mti_id, gid,
                     "anchor repair (DIR-20260507-M05-004..010)"),
                )
            n_set += 1

        conn.execute("COMMIT")
    except Exception as e:
        conn.execute("ROLLBACK")
        print(f"[err] rolled back: {e}")
        raise

    print(f"\nAnchors set: {n_set}")
    print(f"Anchors NOT resolved: {len(halts)}")
    if halts:
        print()
        print("Unresolved (require AI follow-up):")
        for gid, ref, mti in halts:
            print(f"  group {gid:5d}  ref={ref:14s}  mti={mti}")

    # Verification
    bad = list(conn.execute("""
        SELECT vcg.id AS gid, vcg.group_code,
               SUM(vc.is_anchor) AS anc, COUNT(vc.id) AS verses
          FROM verse_context_group vcg
          JOIN verse_context vc ON vc.group_id=vcg.id
          JOIN mti_terms mt ON mt.id=vcg.mti_term_id
         WHERE mt.cluster_code='M05'
           AND COALESCE(vcg.delete_flagged,0)=0
           AND COALESCE(vc.delete_flagged,0)=0
         GROUP BY vcg.id HAVING anc != 1
    """))
    print()
    print(f"M05 groups with non-1 anchor count: {len(bad)}")
    if bad:
        for r in bad[:20]:
            print(f"  gid={r['gid']:5d} code={r['group_code']:14s} "
                  f"anc={r['anc']} verses={r['verses']}")

    conn.close()
    return 0


if __name__ == "__main__":
    sys.exit(main())
