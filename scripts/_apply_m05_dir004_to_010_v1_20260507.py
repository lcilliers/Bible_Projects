"""_apply_m05_dir004_to_010_v1_20260507.py — DB-modifying.

Applies seven M05 cluster-process directives (Phase 7 group-verse mapping):

  DIR-20260507-M05-004  M05-A Love
  DIR-20260507-M05-005  M05-B Compassion
  DIR-20260507-M05-006  M05-C Mercy
  DIR-20260507-M05-007  M05-D Kindness and Goodness
  DIR-20260507-M05-008  M05-E Gentleness
  DIR-20260507-M05-009  M05-F Comfort and Encouragement
  DIR-20260507-M05-010  M05-G Fellowship and Participation

Operations applied:
  1. Anchor designations (108 anchor flips — clear stale per group, set new)
  2. P-verse assignments to groups (33 verses promoted from P → assigned)
  3. Cross-group dual assignments (~36 secondary verse_context rows)
  4. Group splits — 629 (M05-B) and 604 (M05-F) applied from explicit verse
     lists; 1583 (M05-A) HALT — 182 rows in DB but only ~13 explicitly
     routed in the directive; needs AI per-verse table follow-up

Operations NOT applied (per cluster-process discipline §8.4):
  - Group description "refinements" where the directive describes the
    refinement qualitatively rather than providing exact text. AI to
    follow up with explicit description text.
  - 1583 split (full-scale verse routing requires AI per-verse table).

Idempotent. Halt-on-error before any write. Backed up first.
"""
from __future__ import annotations

import os
import shutil
import sqlite3
import sys
from datetime import datetime, timezone

DB_PATH = os.path.join("database", "bible_research.db")
BACKUP_DIR = "backups"
DIR_TAG = "DIR-20260507-M05-004..010"

# ============================================================================
# 1. Anchor designations — (group_id, reference, mti_id)
#    Set is_anchor=1 on the verse_context row matching (vr_id_for(ref, mti_id),
#    mti_id, group_id). Stale anchors per group cleared first.
# ============================================================================
ANCHORS = [
    # M05-A (dir-004) — 37 anchors
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
    # M05-B (dir-005) — 16 anchors (excluding 629-a/-b which are in splits)
    (1596, "Isa 54:7", 544), (1595, "Psa 103:13", 551),
    (1594, "Exo 34:6", 1614), (1672, "Dan 2:18", 988),
    (349, "Lam 4:10", 1616), (1638, "2Cor 1:3", 992),
    (1639, "Luk 6:36", 3158), (331, "Rom 9:15", 731),
    (333, "Luk 15:20", 730), (2717, "Eph 4:32", 593),
    (334, "Heb 4:15", 734), (335, "1Pe 3:8", 3980),
    (337, "Jon 4:11", 3182), (338, "Deu 13:8", 3182),
    (630, "2Ch 36:15", 487), (339, "Isa 63:9", 2192),
    # M05-C (dir-006) — 9 anchors
    (1628, "Rom 9:16", 981), (1629, "Mar 10:48", 981),
    (1630, "Mat 18:33", 981), (1631, "Heb 2:17", 3164),
    (1632, "Eph 2:4", 983), (1633, "Jam 2:13", 983),
    (1625, "Rom 1:31", 3165), (1626, "Jam 2:13", 993),
    (328, "Rev 3:17", 3168),
    # M05-D (dir-007) — 16 anchors
    (1111, "Rom 11:22", 886), (1112, "Gal 5:22", 886),
    (1469, "Luk 6:35", 954), (1467, "1Cor 13:4", 5729),
    (1096, "Mar 10:18", 881), (1097, "Mat 12:35", 881),
    (1098, "Eph 2:10", 881), (1099, "Rom 8:28", 881),
    (1100, "Rom 7:19", 881), (1093, "1Pe 2:20", 1638),
    (1092, "1Ti 6:18", 1640), (1094, "1Pe 4:19", 1641),
    (1095, "1Pe 2:14", 1642), (687, "2Cor 11:3", 810),
    (688, "2Cor 9:11", 810), (2290, "2Cor 8:21", 1187),
    # M05-E (dir-008) — 8 explicit anchors (anoche new group handled below)
    (1104, "2Cor 10:1", 882), (1261, "1Pe 3:4", 46),
    (1262, "Jam 1:21", 47), (1102, "2Cor 10:1", 883),
    (1103, "Phili 4:5", 5425), (1272, "Pro 22:4", 189),
    (1271, "2Sa 22:36", 188), (867, "2Ti 2:24", 856),
    # M05-F (dir-009) — 9 anchors (excluding 604-a/-b in splits)
    (1741, "Isa 40:1", 445), (1742, "Isa 66:13", 445),
    (2741, "Song 4:9", 587), (3079, "Psa 94:19", 1292),
    (602, "2Cor 1:4", 510), (603, "Mar 5:23", 510),
    (3073, "2Cor 1:3", 1290), (3074, "Rom 15:4", 1290),
    (3075, "Phile 7", 1290),
    # M05-G (dir-010) — 8 anchors
    (1055, "1Jo 1:3", 873), (1056, "Act 2:42", 873),
    (1057, "2Pe 1:4", 5367), (1058, "Mat 23:30", 5367),
    (1813, "1Pe 3:8", 1008), (1795, "Phili 2:20", 1402),
    (2069, "2Cor 5:19", 1093), (2849, "Eph 2:20", 7064),
]

# ============================================================================
# 2. P-verse assignments — (vr_id_or_None, reference, mti_id, target_group_id)
#    If vr_id is None, resolve from (reference, mti_id).
# ============================================================================
P_VERSES = [
    # M05-A — 22 (vr_ids explicit in directive)
    (68172, "1Ki 4:5",   1623, 1598),
    (3940,  "Neh 13:14", 536,  1584),
    (3942,  "Est 2:9",   536,  1584),
    (3943,  "Est 2:17",  536,  1584),
    (67683, "Est 5:10",  1600, 1576),
    (67684, "Est 5:14",  1600, 1576),
    (67685, "Est 6:13",  1600, 1576),
    (67690, "Pro 14:20", 1600, 1576),
    (67687, "Jer 20:4",  1600, 1576),
    (67688, "Jer 20:6",  1600, 1576),
    (66970, "Luk 7:6",   1579, 1572),
    (66961, "Luk 14:10", 1579, 1572),
    (66962, "Luk 14:12", 1579, 1572),
    (66963, "Luk 15:29", 1579, 1572),
    (66967, "Luk 21:16", 1579, 1572),
    (66968, "Luk 23:12", 1579, 1572),
    (66955, "Joh 19:12", 1579, 1572),
    (66946, "Act 10:24", 1579, 1572),
    (66947, "Act 19:31", 1579, 1572),
    (66948, "Act 27:3",  1579, 1572),
    (4614,  "Act 28:2",  556,  1559),
    (66945, "3Jo 15",    1579, 1572),
    # M05-B — 1 (Job 27:22 → 629-a; resolved via split logic below)
    # M05-C — 1
    (None,  "Mar 5:19",  981, 1629),
    # M05-G — 9
    (None,  "Luk 5:10",  5367, 1057),
    (None,  "2Cor 8:23", 5367, 1057),
    (None,  "Rom 15:26", 873,  1056),
    (None,  "2Cor 9:13", 873,  1056),
    (None,  "Heb 13:16", 873,  1056),
    (None,  "1Cor 3:10", 7064, 2849),
    (None,  "1Cor 3:12", 7064, 2849),
    (None,  "1Cor 3:14", 7064, 2849),
    (None,  "Eph 2:20",  7064, 2849),
]

# ============================================================================
# 3. Dual assignments — secondary verse_context row insert
#    (reference, primary_mti_id, primary_group, secondary_mti_id, secondary_group)
#    The verse_record_id is resolved per (ref, secondary_mti_id) — i.e. the
#    secondary row is for the term whose mti_id is the secondary_mti_id.
#    For shared-verse duals where two terms occupy the same verse, the
#    secondary row sits at the primary verse with mti_id being the term
#    being added to the secondary group.
# ============================================================================
# Format: (reference, target_mti_id_for_row, target_group_id, source_note)
DUAL_ROWS = [
    # M05-A (6)
    ("Rom 12:10", 554, 1573, "filostorgos secondary alongside filadelfia"),
    ("Tit 2:4",   559, 1574, "filoteknos secondary alongside filandros"),
    ("Tit 1:8",   566, 1555, "filagathos secondary alongside filoxenos"),
    ("1Pe 3:8",   567, 1557, "filadelfos secondary alongside filofrōn"),
    ("Joh 15:9",  562, 1542, "agapē secondary alongside agapaō"),
    ("Joh 17:26", 562, 1542, "agapē secondary alongside agapaō"),
    # M05-B (11)
    ("Deu 13:17", 544, 1596, "ra.cha.mim secondary alongside ra.cham"),
    ("1Ki 8:50",  544, 1596, "ra.cha.mim secondary alongside ra.cham"),
    ("2Ch 30:9",  544, 1596, "ra.cha.mim secondary alongside ra.chum"),
    ("Jer 13:14", 3182, 338, "chus secondary alongside cha.mal 629-b"),
    ("Jer 21:7",  3182, 338, "chus secondary alongside cha.mal 630"),
    ("Deu 13:8",  3182, 338, "chus secondary alongside cha.mal 629-b"),
    ("Eze 5:11",  3182, 338, "chus secondary alongside cha.mal 630"),
    ("Eze 7:4",   3182, 338, "chus secondary alongside cha.mal 630"),
    ("Eze 8:18",  3182, 338, "chus secondary alongside cha.mal 630"),
    ("Eze 9:5",   3182, 338, "chus secondary alongside cha.mal 630"),
    ("1Pe 3:8",   593, 2717, "eusplanchnos secondary alongside sumpathēs"),
    # M05-C (2)
    ("Mat 5:7",   3164, 1631, "eleēmōn secondary alongside eleeō"),
    ("Jam 2:13",  993,  1626, "anileōs secondary alongside eleos"),
    # M05-D (3)
    ("Rom 2:4",   954,  1469, "chrēstos secondary alongside chrēstotēs"),
    ("Rom 12:8",  810,  688,  "haplotēs secondary alongside parakaleō (cross-sub-group)"),
    ("1Cor 13:4", 562,  1543, "agapē secondary alongside chrēsteuomai (cross-sub-group)"),
    # M05-E (2)
    ("2Cor 10:1", 883,  1102, "epieikeia secondary alongside praotēs"),
    ("Tit 3:2",   47,   1262, "prautēs secondary alongside epieikēs"),
    # M05-F (6) — note: many already on the primary 602/3073 anchor rows
    # The duals here are secondary rows for the OTHER mti_id at the same vr
    ("2Cor 1:3",  1290, 3073, "paraklēsis secondary alongside parakaleō (already anchor of 3073)"),
    ("2Cor 1:4",  1290, 3073, "paraklēsis secondary alongside parakaleō"),
    ("2Cor 1:5",  1290, 3073, "paraklēsis secondary alongside parakaleō"),
    ("2Cor 1:6",  1290, 3073, "paraklēsis secondary alongside parakaleō"),
    ("2Cor 1:7",  1290, 3073, "paraklēsis secondary alongside parakaleō"),
    # Rom 12:8 cross-sub-group already in M05-D set above — skip duplicate
    # M05-G (6)
    ("Phili 2:1", 873,  1055, "koinōnia secondary in vertical fellowship"),
    ("1Jo 1:3",   873,  1056, "secondary in horizontal koinōnia"),
    ("1Jo 1:6",   873,  1056, "secondary in horizontal koinōnia"),
    ("1Jo 1:7",   873,  1056, "secondary in horizontal koinōnia"),
    ("2Cor 1:7",  1290, 3073, "paraklēsis secondary alongside koinōnos cross-sub-group"),
    # Act 2:42 dual (1056 anchor + 1055 secondary) handled by anchor + extra
    ("Act 2:42",  873,  1055, "vertical fellowship secondary alongside horizontal anchor"),
]

# ============================================================================
# 4. Group splits — 629 (M05-B) and 604 (M05-F) applied; 1583 HALT.
#    Split entry: (original_group_id, target_mti_id, [(new_code, anchor_ref,
#                  description, [verse_refs])])
# ============================================================================
SPLITS_TO_APPLY = [
    # 629 split (cha.mal, mti=487) — explicit verse lists in directive
    {
        "original_group_id": 629,
        "mti_id": 487,
        "new_groups": [
            {
                "group_code": "487-001-a",
                "description": (
                    "Term names human compassion as the inner disposition "
                    "of pity that moves toward and spares those in need — "
                    "whether a child, a prisoner, or an enemy; genuine "
                    "compassion as the inner motivation for sparing"
                ),
                "anchor_ref": "Exo 2:6",
                "verses": [
                    "Exo 2:6", "1Sa 23:21", "2Sa 21:7", "Mal 3:17",
                    "Job 27:22",  # P-verse
                ],
            },
            {
                "group_code": "487-001-b",
                "description": (
                    "Term names compassion toward commanded-destruction "
                    "targets as disobedience — where the inner disposition "
                    "of pity violates the covenantal obligation to carry "
                    "out judgment"
                ),
                "anchor_ref": "1Sa 15:9",
                "verses": [
                    "1Sa 15:3", "1Sa 15:9", "1Sa 15:15", "2Sa 12:4",
                    "2Sa 12:6", "Hab 1:17",
                ],
            },
        ],
    },
    # 604 split (parakaleō, mti=510) — extensive but enumerated
    {
        "original_group_id": 604,
        "mti_id": 510,
        "new_groups": [
            {
                "group_code": "510-003-a",
                "description": (
                    "Term names the pastoral or apostolic appeal — the "
                    "inner relational care and authority of the one urging "
                    "another toward faithful conduct, endurance, and inner "
                    "transformation; grounded in the mercies of God and "
                    "the authority of the gospel"
                ),
                "anchor_ref": "Rom 12:1",
                "verses": [
                    "Act 11:23", "Act 14:22", "Act 15:32", "Act 20:1",
                    "Act 20:2", "Rom 12:1", "Rom 12:8", "Rom 15:30",
                    "Rom 16:17", "1Cor 1:10", "1Cor 4:16", "1Cor 14:31",
                    "1Cor 16:12", "1Cor 16:15", "2Cor 2:8", "2Cor 5:20",
                    "2Cor 6:1", "2Cor 8:6", "2Cor 9:5", "2Cor 10:1",
                    "2Cor 12:18", "2Cor 13:11", "Eph 4:1", "Eph 6:22",
                    "Phili 4:2", "Col 2:2", "Col 4:8", "1Th 2:12",
                    "1Th 3:2", "1Th 4:1", "1Th 4:10", "1Th 4:18",
                    "1Th 5:11", "1Th 5:14", "2Th 2:17", "2Th 3:12",
                    "1Ti 1:3", "1Ti 2:1", "1Ti 5:1", "1Ti 6:2",
                    "2Ti 4:2", "Tit 1:9", "Tit 2:6", "Tit 2:15",
                    "Phile 9", "Phile 10", "Heb 3:13", "Heb 10:25",
                    "Heb 13:19", "Heb 13:22", "1Pe 2:11", "1Pe 5:1",
                    "1Pe 5:12", "Jude 3", "Luk 3:18", "Act 2:40",
                ],
            },
            {
                "group_code": "510-003-b",
                "description": (
                    "Term names the social or interpersonal request — "
                    "inviting, urging, asking someone to do or refrain "
                    "from something in the context of ordinary social or "
                    "relational life, without the pastoral or apostolic "
                    "authority dimension"
                ),
                "anchor_ref": "Act 16:15",
                "verses": [
                    "Act 8:31", "Act 9:38", "Act 16:15", "Act 16:39",
                    "Act 16:40", "Act 19:31", "Act 21:12", "Act 24:4",
                    "Act 25:2", "Act 27:33", "Act 27:34", "Act 28:14",
                    "Act 28:20", "Luk 15:28", "2Cor 12:8",
                ],
            },
        ],
    },
]

# 1583 split — NOT applied this pass; 169 of 182 verses unrouted
SPLIT_HALTED_INFO = {
    "original_group_id": 1583,
    "mti_id": 536,
    "current_row_count": 182,
    "explicitly_routed_in_directive": 13,
    "halt_reason": (
        "1583 split requires a per-verse routing table for the 169 "
        "currently-unrouted rows. The directive provides diagnostics "
        "but only 13 of 182 verses are explicitly named. Per cluster-"
        "process discipline (wa-directive-instruction §8.4), CC does "
        "not make analytical judgements at this scale. AI must produce "
        "a per-verse routing supplement before the 1583 split can apply."
    ),
}

# Anochē — new group for G0463 (mti=7502), per dir-008 special case
ANOCHE_NEW_GROUP = {
    "mti_id": 7502,
    "group_code": "7502-001",
    "description": (
        "Term names divine forbearance/tolerance — God's inner "
        "disposition of restraining judgment that would be fully "
        "warranted; the patience that withholds what is deserved, "
        "revealing the inner character of sovereign mercy toward "
        "the disobedient"
    ),
    "anchor_ref": "Rom 2:4",
}


# ============================================================================
# Apply logic
# ============================================================================
def now_iso():
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def backup_db():
    os.makedirs(BACKUP_DIR, exist_ok=True)
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    dest = os.path.join(BACKUP_DIR,
                        f"bible_research_{ts}_pre_m05_dir004_010.db")
    shutil.copy2(DB_PATH, dest)
    return dest


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
        "song": "Sng", "ps": "Psa", "ec": "Ecc",
        "rev": "Rev", "rv": "Rev",
        "deut": "Deu", "ezek": "Eze", "judg": "Jdg",
    }
    for alt, can in aliases.items():
        if can.lower() in out:
            out[alt.lower()] = out[can.lower()]
    return out


def parse_ref(ref, book_lookup):
    import re
    m = re.match(
        r"^(?P<book>\d?[A-Za-z]{2,5})\s+(?P<chap>\d+):(?P<v>\d+)",
        ref.strip(),
    )
    if not m:
        return None
    book = m.group("book")
    chap = int(m.group("chap"))
    verse = int(m.group("v"))
    bid = book_lookup.get(book.lower())
    return (bid, chap, verse) if bid else None


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


def vc_upsert(conn, vr_id, mti_id, group_id, is_anchor=0,
              note="DIR-20260507-M05-004..010"):
    existing = conn.execute(
        "SELECT id FROM verse_context "
        " WHERE verse_record_id=? AND mti_term_id=? AND group_id=? "
        "   AND COALESCE(delete_flagged,0)=0",
        (vr_id, mti_id, group_id),
    ).fetchone()
    if existing:
        conn.execute(
            "UPDATE verse_context SET is_relevant=1, "
            "       set_aside_reason=NULL, "
            "       is_anchor=?, "
            "       notes=?, last_updated_date=? "  # last_updated_date may not exist
            " WHERE id=?",
            (is_anchor, note, now_iso(), existing["id"]),
        )
        return existing["id"], "updated"
    cur = conn.execute(
        "INSERT INTO verse_context "
        "  (verse_record_id, mti_term_id, group_id, is_anchor, "
        "   is_relevant, is_related, notes, delete_flagged, "
        "   set_aside_reason) "
        "VALUES (?, ?, ?, ?, 1, 0, ?, 0, NULL)",
        (vr_id, mti_id, group_id, is_anchor, note),
    )
    return cur.lastrowid, "inserted"


def main():
    print(f"DB: {DB_PATH}")
    print("Backing up...", flush=True)
    bak = backup_db()
    print(f"  -> {bak}\n")

    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    book_lookup = build_book_lookup(conn)

    # Detect last_updated_date column on verse_context
    cols = {r[1] for r in conn.execute(
        "PRAGMA table_info(verse_context)"
    )}
    has_lu = "last_updated_date" in cols

    # Re-define vc_upsert without last_updated_date if absent
    if not has_lu:
        def vc_upsert_noLU(conn, vr_id, mti_id, group_id, is_anchor=0,
                           note="DIR"):
            existing = conn.execute(
                "SELECT id FROM verse_context "
                " WHERE verse_record_id=? AND mti_term_id=? AND group_id=? "
                "   AND COALESCE(delete_flagged,0)=0",
                (vr_id, mti_id, group_id),
            ).fetchone()
            if existing:
                conn.execute(
                    "UPDATE verse_context SET is_relevant=1, "
                    "       set_aside_reason=NULL, is_anchor=?, "
                    "       notes=? "
                    " WHERE id=?",
                    (is_anchor, note, existing["id"]),
                )
                return existing["id"], "updated"
            cur = conn.execute(
                "INSERT INTO verse_context "
                "  (verse_record_id, mti_term_id, group_id, is_anchor, "
                "   is_relevant, is_related, notes, delete_flagged, "
                "   set_aside_reason) "
                "VALUES (?, ?, ?, ?, 1, 0, ?, 0, NULL)",
                (vr_id, mti_id, group_id, is_anchor, note),
            )
            return cur.lastrowid, "inserted"
        upsert_fn = vc_upsert_noLU
    else:
        upsert_fn = vc_upsert

    counts = {
        "anchors_set": 0, "anchors_skipped": 0,
        "p_verses_assigned": 0, "p_verses_skipped": 0,
        "duals_inserted": 0, "duals_updated": 0, "duals_skipped": 0,
        "split_groups_created": 0, "split_verses_routed": 0,
        "split_verses_skipped": 0,
        "anoche_group_created": 0, "anoche_anchor_set": 0,
    }
    halts = []

    try:
        conn.execute("BEGIN")

        # -------- Phase 1: ANCHORS --------
        print("Phase 1: setting anchors")
        groups_to_clear = {gid for gid, _, _ in ANCHORS}
        for gid in groups_to_clear:
            conn.execute(
                "UPDATE verse_context SET is_anchor=0 "
                " WHERE group_id=? AND is_anchor=1 "
                "   AND COALESCE(delete_flagged,0)=0",
                (gid,),
            )
        for gid, ref, mti_id in ANCHORS:
            vr = vr_lookup(conn, book_lookup, ref, mti_id)
            if not vr:
                halts.append(f"ANCHOR not found: {ref} mti={mti_id} → group {gid}")
                counts["anchors_skipped"] += 1
                continue
            _, action = upsert_fn(conn, vr, mti_id, gid, is_anchor=1,
                                   note=f"{DIR_TAG} anchor")
            counts["anchors_set"] += 1

        # -------- Phase 2: P-VERSES --------
        print("Phase 2: assigning P-verses to groups")
        for vr, ref, mti_id, gid in P_VERSES:
            if vr is None:
                vr = vr_lookup(conn, book_lookup, ref, mti_id)
            if not vr:
                halts.append(f"P-VERSE not found: {ref} mti={mti_id} → group {gid}")
                counts["p_verses_skipped"] += 1
                continue
            upsert_fn(conn, vr, mti_id, gid, is_anchor=0,
                      note=f"{DIR_TAG} P-verse → group {gid}")
            counts["p_verses_assigned"] += 1

        # -------- Phase 3: DUALS --------
        print("Phase 3: inserting dual-assignment rows")
        for ref, mti_id, gid, src in DUAL_ROWS:
            vr = vr_lookup(conn, book_lookup, ref, mti_id)
            if not vr:
                halts.append(f"DUAL not found: {ref} mti={mti_id} → group {gid}")
                counts["duals_skipped"] += 1
                continue
            _, action = upsert_fn(conn, vr, mti_id, gid, is_anchor=0,
                                   note=f"{DIR_TAG} dual: {src}")
            if action == "inserted":
                counts["duals_inserted"] += 1
            else:
                counts["duals_updated"] += 1

        # -------- Phase 4: SPLITS (629 + 604) --------
        print("Phase 4: applying explicit splits (629, 604)")
        for split in SPLITS_TO_APPLY:
            orig_gid = split["original_group_id"]
            mti = split["mti_id"]
            for new in split["new_groups"]:
                # Insert new group (or update if it already exists)
                existing = conn.execute(
                    "SELECT id FROM verse_context_group "
                    " WHERE group_code=? AND COALESCE(delete_flagged,0)=0",
                    (new["group_code"],),
                ).fetchone()
                if existing:
                    new_gid = existing["id"]
                    conn.execute(
                        "UPDATE verse_context_group "
                        "   SET context_description=? "
                        " WHERE id=?",
                        (new["description"], new_gid),
                    )
                else:
                    cur = conn.execute(
                        "INSERT INTO verse_context_group "
                        "  (mti_term_id, group_code, context_description, "
                        "   notes, delete_flagged, vertical_pass_flag) "
                        "VALUES (?, ?, ?, ?, 0, 0)",
                        (mti, new["group_code"], new["description"],
                         f"Created by {DIR_TAG}"),
                    )
                    new_gid = cur.lastrowid
                    counts["split_groups_created"] += 1

                # Route the named verses from orig_gid → new_gid
                anchor_vr = None
                for ref in new["verses"]:
                    vr = vr_lookup(conn, book_lookup, ref, mti)
                    if not vr:
                        halts.append(
                            f"SPLIT {orig_gid}→{new['group_code']} verse "
                            f"not found: {ref} mti={mti}"
                        )
                        counts["split_verses_skipped"] += 1
                        continue
                    if ref == new["anchor_ref"]:
                        anchor_vr = vr
                    # Route: find existing row for (vr, mti) and update its
                    # group_id from orig_gid to new_gid; if multiple rows or
                    # other group, just upsert into new_gid
                    rows = conn.execute(
                        "SELECT id, group_id FROM verse_context "
                        " WHERE verse_record_id=? AND mti_term_id=? "
                        "   AND COALESCE(delete_flagged,0)=0",
                        (vr, mti),
                    ).fetchall()
                    routed = False
                    for r in rows:
                        if r["group_id"] == orig_gid:
                            conn.execute(
                                "UPDATE verse_context SET group_id=? "
                                " WHERE id=?",
                                (new_gid, r["id"]),
                            )
                            routed = True
                            break
                    if not routed:
                        upsert_fn(conn, vr, mti, new_gid, is_anchor=0,
                                  note=f"{DIR_TAG} split")
                    counts["split_verses_routed"] += 1
                # Set anchor on the new group
                if anchor_vr:
                    conn.execute(
                        "UPDATE verse_context SET is_anchor=0 "
                        " WHERE group_id=? AND is_anchor=1",
                        (new_gid,),
                    )
                    upsert_fn(conn, anchor_vr, mti, new_gid, is_anchor=1,
                              note=f"{DIR_TAG} split anchor")

        # -------- Phase 5: ANOCHE new group --------
        print("Phase 5: anoche new group (G0463 mti=7502)")
        ag = ANOCHE_NEW_GROUP
        existing = conn.execute(
            "SELECT id FROM verse_context_group "
            " WHERE group_code=? AND COALESCE(delete_flagged,0)=0",
            (ag["group_code"],),
        ).fetchone()
        if existing:
            anoche_gid = existing["id"]
        else:
            cur = conn.execute(
                "INSERT INTO verse_context_group "
                "  (mti_term_id, group_code, context_description, notes, "
                "   delete_flagged, vertical_pass_flag) "
                "VALUES (?, ?, ?, ?, 0, 0)",
                (ag["mti_id"], ag["group_code"], ag["description"],
                 f"Created by {DIR_TAG}"),
            )
            anoche_gid = cur.lastrowid
            counts["anoche_group_created"] = 1

        # Find anoche's verse_context rows; if any exist, set group_id;
        # set anchor on Rom 2:4
        anoche_vrs = conn.execute(
            "SELECT id, verse_record_id FROM verse_context "
            " WHERE mti_term_id=? AND COALESCE(delete_flagged,0)=0",
            (ag["mti_id"],),
        ).fetchall()
        if not anoche_vrs:
            halts.append(
                f"ANOCHE has 0 verse_context rows for mti={ag['mti_id']}; "
                f"new group created but unanchored"
            )
        else:
            for r in anoche_vrs:
                conn.execute(
                    "UPDATE verse_context SET group_id=?, is_relevant=1 "
                    " WHERE id=?",
                    (anoche_gid, r["id"]),
                )
            anchor_vr = vr_lookup(conn, book_lookup, ag["anchor_ref"],
                                   ag["mti_id"])
            if anchor_vr:
                conn.execute(
                    "UPDATE verse_context SET is_anchor=0 "
                    " WHERE group_id=? AND is_anchor=1",
                    (anoche_gid,),
                )
                conn.execute(
                    "UPDATE verse_context SET is_anchor=1 "
                    " WHERE verse_record_id=? AND mti_term_id=? "
                    "   AND group_id=?",
                    (anchor_vr, ag["mti_id"], anoche_gid),
                )
                counts["anoche_anchor_set"] = 1

        conn.execute("COMMIT")
    except Exception as e:
        conn.execute("ROLLBACK")
        print(f"[err] rolled back: {e}")
        raise

    # ---- Report
    print()
    print("=" * 70)
    print("APPLY SUMMARY")
    print("=" * 70)
    for k, v in counts.items():
        print(f"  {k:30s} {v}")
    print()
    if halts:
        print(f"! {len(halts)} resolution halt(s):")
        for h in halts[:20]:
            print(f"  - {h}")
        if len(halts) > 20:
            print(f"  - ... +{len(halts)-20}")
    print()
    print("HALTED — 1583 split (M05-A che.sed)")
    print("-" * 70)
    print(SPLIT_HALTED_INFO["halt_reason"])
    print()

    # Verification queries
    print("=" * 70)
    print("VERIFICATION QUERIES")
    print("=" * 70)

    # Anchor count per group (should be 1 for each group with an anchor)
    print("\nGroups with non-1 anchor count (M05 sub-groups):")
    bad = list(conn.execute("""
        SELECT vcg.id AS gid, vcg.group_code,
               SUM(vc.is_anchor) AS anc_count,
               COUNT(vc.id) AS verse_count
          FROM verse_context_group vcg
          JOIN verse_context vc ON vc.group_id=vcg.id
          JOIN mti_terms mt ON mt.id=vcg.mti_term_id
         WHERE mt.cluster_code='M05'
           AND COALESCE(vcg.delete_flagged,0)=0
           AND COALESCE(vc.delete_flagged,0)=0
         GROUP BY vcg.id
        HAVING anc_count != 1
    """))
    if not bad:
        print("  (none — every M05 group has exactly 1 anchor)")
    else:
        print(f"  {len(bad)} group(s) with non-1 anchor:")
        for r in bad:
            print(f"    gid={r['gid']} code={r['group_code']} "
                  f"anchors={r['anc_count']} verses={r['verse_count']}")

    # P-verse residue per M05 sub-group
    n_p = conn.execute("""
        SELECT COUNT(*) FROM verse_context vc
          JOIN mti_terms mt ON mt.id=vc.mti_term_id
         WHERE mt.cluster_code='M05'
           AND vc.is_relevant=1
           AND (vc.group_id IS NULL OR vc.group_id=0)
           AND COALESCE(vc.delete_flagged,0)=0
    """).fetchone()[0]
    print(f"\nP-status verses remaining for M05 (relevant w/no group): {n_p}")

    # Group 1583 row count (split deferred)
    n_1583 = conn.execute(
        "SELECT COUNT(*) FROM verse_context "
        " WHERE group_id=1583 AND COALESCE(delete_flagged,0)=0"
    ).fetchone()[0]
    print(f"Group 1583 row count (1583 split deferred): {n_1583}")

    # Group 629 split — should be 0 in original 629 if all routed
    n_629 = conn.execute(
        "SELECT COUNT(*) FROM verse_context "
        " WHERE group_id=629 AND COALESCE(delete_flagged,0)=0"
    ).fetchone()[0]
    print(f"Group 629 row count (post-split — should be near 0): {n_629}")

    # Group 604 split
    n_604 = conn.execute(
        "SELECT COUNT(*) FROM verse_context "
        " WHERE group_id=604 AND COALESCE(delete_flagged,0)=0"
    ).fetchone()[0]
    print(f"Group 604 row count (post-split — should be near 0): {n_604}")

    # wa_session_b_findings count check
    n_sb = conn.execute("""
        SELECT COUNT(*) FROM wa_session_b_findings
         WHERE COALESCE(raised_date,'') LIKE '2026-05-07%'
    """).fetchone()[0]
    print(f"wa_session_b_findings rows raised 2026-05-07: {n_sb}")

    conn.close()
    return 0


if __name__ == "__main__":
    sys.exit(main())
