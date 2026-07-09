"""_verify_m06_findings_references_v1_20260506.py — read-only.

Pre-flight verification for the M06 consolidated findings document
(WA-M06-consolidated-findings-v1-20260506, parts 1–4).

Three checks:
  1. Anchor verses claimed in the findings — exist in wa_verse_records
     for the implied mti_term, with current is_anchor state reported.
  2. NT verses cited in the findings — exist for the cited mti_term.
  3. Group codes / ids referenced — exist in DB; mti_term_id alignment
     matches the findings' implication.

Output: report to stdout + optionally to file.

Read-only — no DB modifications.
"""
from __future__ import annotations

import os
import sqlite3
import sys
from collections import defaultdict
from datetime import datetime, timezone

DB_PATH = os.path.join("database", "bible_research.db")


# ---------------------------------------------------------------------------
# Anchor claims from the findings document, per group.
# Each row: (group_code, expected_mti_strongs, anchor_ref).
# Where the findings document explicitly names an anchor verse for a group.
# ---------------------------------------------------------------------------
ANCHOR_CLAIMS = [
    # M06-A
    ("550-001",   "H8130", "Lev 19:17"),
    ("550-002",   "H8130", "Exo 1:10"),
    ("550-NEW-01","H8130", "Deu 22:13"),
    ("550-NEW-02","H8130", "Pro 8:13"),
    ("550-NEW-03","H8130", "Psa 11:5"),
    ("550-NEW-04","H8130", "Exo 20:5"),
    ("1663-001",  "H8131", "Dan 4:19"),
    ("902-001",   "H8135", "Pro 10:12"),
    ("902-002",   "H8135", "Deu 1:27"),
    ("902-003",   "H8135", "Ecc 9:6"),
    ("903-001",   "H4895", "Hos 9:7"),
    ("5518-001",  "H7852", "Gen 27:41"),
    # M06-B (anchors implied by the findings document — primary anchor refs
    # named at T7.2.5 / T7.2.6)
    ("172-001",   "H5006", "Num 14:11"),  # na.ats — primary verse
    ("1280-001",  "H0959", "Isa 53:3"),   # ba.zah — typological anchor
    # M06-C
    ("252-001",   "H8581", "Psa 119:163"),  # ta.av — primary co-occurrence anchor
    ("1283-001",  "H1860", "Dan 12:2"),    # de.ra.on — eschatological anchor
    # M06-D
    ("1775-002",  "H6184", "Psa 54:3"),  # a.rits — constitutional ground anchor
    # M06-E
    ("322-001",   "H2781", "Psa 69:20"),  # cher.pah — heart-breaking anchor
    # M06-F (corrected per verification response — G0476 lives in 3200-001)
    ("3200-001",  "G0476", "1Pe 5:8"),    # antidikos — cosmic adversary anchor
    ("3200-001",  "G0476", "Luk 18:3"),   # antidikos — second anchor (widow appeal)
    # M06-G
    ("1275-001",  "H7589", "Eze 25:6"),   # she.at — soul-located anchor
]

# ---------------------------------------------------------------------------
# NT verses cited in findings (term being cited → reference).
# These need to exist in wa_verse_records for the cited Strong's so that
# they can be linked from a cluster finding.
# ---------------------------------------------------------------------------
NT_CITATIONS = [
    # (Strong's of cited term, reference)
    ("G0948", "Rev 21:8"),     # bdelussomai — Revelation eschatological
    ("G0948", "Rom 2:22"),     # bdelussomai — Paul's challenge
    ("G0476", "1Pe 5:8"),      # antidikos — devil
    ("G0476", "Mat 5:25"),     # antidikos — legal
    ("G0476", "Luk 12:58"),    # antidikos
    ("G0476", "Luk 18:3"),     # antidikos — widow
    ("G0865", "2Ti 3:3"),      # afilagathos — last-days
    ("G5195", "1Th 2:2"),      # hubrizō — Paul's Philippi
    # Cited via Hebrew anchors that are quoted in NT (these need OT existence,
    # not NT — the OT is the source. Skip from this list.)
]

# ---------------------------------------------------------------------------
# Group codes the findings reference (most are M06-cluster groups).
# Codes are "{mti}-{suffix}" — verify each row's mti_term_id matches the
# Strong's the findings imply.
# ---------------------------------------------------------------------------
GROUP_CODE_CLAIMS = [
    # M06-A
    ("550-001", "H8130"), ("550-002", "H8130"),
    ("550-NEW-01", "H8130"), ("550-NEW-02", "H8130"),
    ("550-NEW-03", "H8130"), ("550-NEW-04", "H8130"),
    ("1663-001", "H8131"), ("1663-NEW-04", "H8131"),
    ("902-001", "H8135"), ("902-002", "H8135"), ("902-003", "H8135"),
    ("903-001", "H4895"),
    ("5518-001", "H7852"),
    # M06-B (codes mentioned in the findings — verify mti)
    ("172-001", "H5006"), ("172-002", "H5006"), ("172-003", "H5006"),
    ("1567-001", "H5007B"),
    ("316-001", "H0937"),
    ("1280-001", "H0959"),
    ("1281-001", "H0963"),
    ("1277-001", "H7590"),
    # M06-C
    ("14-001", "G0948"), ("14-002", "G0948"),
    ("247-001", "H8263"), ("247-002", "H8263"),
    ("248-001", "H8374"),
    ("252-001", "H8581"), ("252-002", "H8581"), ("252-003", "H8581"),
    ("1283-001", "H1860"),
    # M06-D
    ("1775-001", "H6184"), ("1775-002", "H6184"),
    ("6966-001", "H0394"),
    ("6967-001", "H0393"),
    ("6968-001", "H0395"),
    # M06-E
    ("1568-001", "H5007A"),
    ("1664-001", "H8146"),
    ("337-001",  "G5195"),
    ("322-001", "H2781"), ("322-002", "H2781"),
    ("317-001", "H8103"),
    # M06-F (added per verification response)
    ("3200-001", "G0476"),    # antidikos
    ("5179-001", "H3401"),    # ya.riv
    ("7009-001", "H0340"),    # a.yav
    ("7001-001", "H7009"),    # qim
    # M06-G
    ("1275-001", "H7589"),    # she.at
    # BOUNDARY
    ("90-001",   "H0887"),    # ba.ash
    ("1643-001", "G0865"),    # afilagathos
    ("339-001",  "H2778A"),   # cha.raph
    ("339-002",  "H2778A"),   # cha.raph
    ("5519-001", "H7850"),    # sho.tet
]


def now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def build_book_lookup(conn):
    out = {}
    for r in conn.execute(
        "SELECT id, name, abbreviation, short_code FROM books"
    ).fetchall():
        bid = r["id"]
        for k in (r["abbreviation"], r["short_code"], r["name"]):
            if k:
                out[k.lower()] = bid
    aliases = {
        "1cor": "1Co", "2cor": "2Co",
        "song": "Sng", "ps": "Psa", "ec": "Ecc", "rv": "Rev",
        "1pe": "1Pe", "2pe": "2Pe", "1th": "1Th", "2th": "2Th",
        "1ti": "1Ti", "2ti": "2Ti", "rom": "Rom",
        "joh": "Joh", "jn": "Joh", "mt": "Mat", "mat": "Mat",
        "lk": "Luk", "luk": "Luk", "deut": "Deu", "deu": "Deu",
        "gen": "Gen", "exo": "Exo", "lev": "Lev",
        "num": "Num", "jos": "Jos", "jdg": "Jdg", "judg": "Jdg",
        "1sa": "1Sa", "2sa": "2Sa", "1ki": "1Ki", "2ki": "2Ki",
        "1ch": "1Ch", "2ch": "2Ch", "neh": "Neh", "est": "Est",
        "job": "Job", "psa": "Psa", "pro": "Pro", "ecc": "Ecc",
        "isa": "Isa", "jer": "Jer", "lam": "Lam", "eze": "Eze",
        "dan": "Dan", "hos": "Hos", "joe": "Joe", "joel": "Joe",
        "amo": "Amo", "amos": "Amo", "mic": "Mic", "zec": "Zec",
        "mal": "Mal", "heb": "Heb",
    }
    for alt, can in aliases.items():
        if can.lower() in out:
            out[alt.lower()] = out[can.lower()]
    return out


def parse_ref(ref: str):
    import re
    m = re.match(
        r"^(?P<book>\d?[A-Za-z]{2,5})\s+(?P<chap>\d+):(?P<v>\d+)",
        ref.strip(),
    )
    if not m:
        return None
    return (m.group("book"), int(m.group("chap")), int(m.group("v")))


def vr_lookup(conn, book_lookup, book_token, chap, verse, mti_id):
    bid = book_lookup.get(book_token.lower())
    if not bid:
        return None, "BOOK_UNKNOWN"
    r = conn.execute("""
        SELECT id FROM wa_verse_records
         WHERE book_id=? AND chapter=? AND verse_num=? AND mti_term_id=?
           AND COALESCE(delete_flagged,0)=0
    """, (bid, chap, verse, mti_id)).fetchone()
    return (r["id"] if r else None), None


def main():
    print(f"Verification run: {now_iso()}")
    print(f"DB: {DB_PATH}")
    print()

    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    book_lookup = build_book_lookup(conn)

    # Pre-resolve Strong's → mti_id (active row preferred).
    strongs_to_mti = {}
    for r in conn.execute("""
        SELECT mt.strongs_number, mt.id
          FROM mti_terms mt
         WHERE COALESCE(mt.delete_flagged,0)=0
         ORDER BY mt.strongs_number, mt.id
    """).fetchall():
        if r["strongs_number"] not in strongs_to_mti:
            strongs_to_mti[r["strongs_number"]] = r["id"]

    flags = []  # collected issues for the final report

    # ---- Check 1: anchor claims
    print("=" * 70)
    print("§1. Anchor verse claims")
    print("=" * 70)
    print(f"{'Group code':14s} {'Term':6s} {'Anchor ref':12s} "
          f"{'Status':10s} {'Notes'}")
    for code, strongs, ref in ANCHOR_CLAIMS:
        mti = strongs_to_mti.get(strongs)
        if not mti:
            flags.append(f"ANCHOR — {code} term {strongs} not in mti_terms")
            print(f"{code:14s} {strongs:6s} {ref:12s} "
                  f"{'NO_MTI':10s} term not found")
            continue
        # group existence
        grow = conn.execute(
            "SELECT id, mti_term_id FROM verse_context_group "
            " WHERE group_code=? AND COALESCE(delete_flagged,0)=0",
            (code,),
        ).fetchone()
        if not grow:
            flags.append(f"ANCHOR — group_code {code} not in DB")
            print(f"{code:14s} {strongs:6s} {ref:12s} "
                  f"{'NO_GROUP':10s} group_code not found")
            continue
        if grow["mti_term_id"] != mti:
            flags.append(
                f"ANCHOR — group {code} has mti_term_id="
                f"{grow['mti_term_id']}, findings imply {mti} ({strongs})"
            )
        # verse resolution
        parsed = parse_ref(ref)
        if not parsed:
            flags.append(f"ANCHOR — unparseable ref '{ref}'")
            print(f"{code:14s} {strongs:6s} {ref:12s} "
                  f"{'BAD_REF':10s}")
            continue
        book, chap, verse = parsed
        vr_id, err = vr_lookup(conn, book_lookup, book, chap, verse, mti)
        if err:
            flags.append(f"ANCHOR — {ref} {err} for {strongs}")
            print(f"{code:14s} {strongs:6s} {ref:12s} "
                  f"{err:10s}")
            continue
        if not vr_id:
            flags.append(
                f"ANCHOR — {ref} has no wa_verse_records row for "
                f"{strongs} (mti={mti})"
            )
            print(f"{code:14s} {strongs:6s} {ref:12s} "
                  f"{'NO_VR':10s} verse not in DB for this term")
            continue
        # current anchor status
        anc = conn.execute(
            "SELECT is_anchor FROM verse_context "
            " WHERE verse_record_id=? AND mti_term_id=? AND group_id=? "
            "   AND COALESCE(delete_flagged,0)=0",
            (vr_id, mti, grow["id"]),
        ).fetchone()
        if not anc:
            flags.append(
                f"ANCHOR — {ref} has no verse_context row for "
                f"group {code} (id={grow['id']})"
            )
            status, note = "NO_VC", "no verse_context row in this group"
        elif anc["is_anchor"] == 1:
            status, note = "OK_ANCHOR", "is_anchor=1 set"
        else:
            status, note = "NOT_ANCHOR", "row exists but is_anchor=0"
            flags.append(
                f"ANCHOR — {ref} {code}: row exists but is_anchor=0"
            )
        print(f"{code:14s} {strongs:6s} {ref:12s} {status:10s} {note}")

    # ---- Check 2: NT citations
    print()
    print("=" * 70)
    print("§2. NT verse citations")
    print("=" * 70)
    print(f"{'Term':6s} {'NT ref':12s} {'Status':12s} {'Notes'}")
    for strongs, ref in NT_CITATIONS:
        mti = strongs_to_mti.get(strongs)
        if not mti:
            flags.append(f"NT — term {strongs} not in mti_terms")
            print(f"{strongs:6s} {ref:12s} {'NO_MTI':12s} term not found")
            continue
        parsed = parse_ref(ref)
        if not parsed:
            flags.append(f"NT — unparseable ref '{ref}'")
            print(f"{strongs:6s} {ref:12s} {'BAD_REF':12s}")
            continue
        book, chap, verse = parsed
        vr_id, err = vr_lookup(conn, book_lookup, book, chap, verse, mti)
        if err:
            flags.append(f"NT — {ref} {err} for {strongs}")
            print(f"{strongs:6s} {ref:12s} {err:12s}")
            continue
        if not vr_id:
            flags.append(
                f"NT — {ref} has no wa_verse_records row for {strongs}"
            )
            print(f"{strongs:6s} {ref:12s} {'NO_VR':12s} "
                  f"verse not in DB for this term")
            continue
        print(f"{strongs:6s} {ref:12s} {'OK':12s} vr_id={vr_id}")

    # ---- Check 3: group code claims
    print()
    print("=" * 70)
    print("§3. Group code references")
    print("=" * 70)
    print(f"{'Group code':14s} {'Term':6s} {'Status':14s} {'Notes'}")
    for code, strongs in GROUP_CODE_CLAIMS:
        mti = strongs_to_mti.get(strongs)
        if not mti:
            flags.append(f"GROUP — term {strongs} for code {code} not found")
            print(f"{code:14s} {strongs:6s} {'NO_MTI':14s}")
            continue
        grow = conn.execute(
            "SELECT id, mti_term_id FROM verse_context_group "
            " WHERE group_code=? AND COALESCE(delete_flagged,0)=0",
            (code,),
        ).fetchone()
        if not grow:
            flags.append(f"GROUP — group_code {code} not in DB")
            print(f"{code:14s} {strongs:6s} {'NO_GROUP':14s} "
                  f"code not found in verse_context_group")
            continue
        if grow["mti_term_id"] != mti:
            real_strongs = next(
                (s for s, m in strongs_to_mti.items() if m == grow["mti_term_id"]),
                "?",
            )
            flags.append(
                f"GROUP — {code} mti mismatch: DB has {real_strongs} "
                f"(mti={grow['mti_term_id']}), findings imply {strongs}"
            )
            print(f"{code:14s} {strongs:6s} {'MTI_MISMATCH':14s} "
                  f"DB has {real_strongs}")
            continue
        n_verses = conn.execute(
            "SELECT COUNT(*) AS n FROM verse_context "
            " WHERE group_id=? AND COALESCE(delete_flagged,0)=0",
            (grow["id"],),
        ).fetchone()["n"]
        n_anchors = conn.execute(
            "SELECT COUNT(*) AS n FROM verse_context "
            " WHERE group_id=? AND is_anchor=1 "
            "   AND COALESCE(delete_flagged,0)=0",
            (grow["id"],),
        ).fetchone()["n"]
        print(f"{code:14s} {strongs:6s} {'OK':14s} "
              f"id={grow['id']} verses={n_verses} anchors={n_anchors}")

    # ---- Summary
    print()
    print("=" * 70)
    print("SUMMARY")
    print("=" * 70)
    if not flags:
        print("[ok] All references resolve cleanly. No flags.")
    else:
        print(f"! {len(flags)} flag(s) for investigation:")
        print()
        for f in flags:
            print(f"  - {f}")

    conn.close()
    return 0 if not flags else 1


if __name__ == "__main__":
    sys.exit(main())
