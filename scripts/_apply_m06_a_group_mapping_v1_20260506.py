"""_apply_m06_a_group_mapping_v1_20260506.py — DB-modifying.

Apply the M06-A group/verse mapping captured in
Sessions/Session_Clusters/M06/WA-M06-A-group-verse-mapping-v1-20260506.md.

Operations (decisions 1A / 2A / 3 / 4 confirmed by researcher 2026-05-06):
  1. UPDATE descriptions of 5 existing groups (1601, 3590, 1199, 1201, 1602).
  2. INSERT 5 new verse_context_group rows (M06-A-NEW-01..04 per term):
     - 550-NEW-01  marital disfavour          (H8130 only)
     - 550-NEW-02  righteous hatred           (H8130 only)
     - 550-NEW-03  divine hatred of sin       (H8130 only)
     - 550-NEW-04  divine response to haters  (H8130: 12 verses)
     - 1663-NEW-04 divine response to haters  (H8131: Dan 4:19)
  3. For every (verse, term, group) listed in the doc:
     UPDATE existing verse_context row (set group_id, is_relevant=1, clear
     set_aside_reason, store analysis_note) OR INSERT if none.
     Set-asides are NOT re-evaluated unless the doc explicitly re-includes
     the verse (decision 4).
  4. For each cross-group dual-assignment row (10 rows):
     INSERT a second verse_context row with the secondary group_id (the
     UNIQUE index on (vr_id, mti_id, group_id) permits this).
  5. Anchor designation: clear is_anchor=0 for any prior anchor on the
     group, then set is_anchor=1 on the chosen row.

Read-only pre-flight halt-on-error:
  - All verse refs must resolve to wa_verse_records for the named term.
  - All terms must belong to cluster M06 + sub-group M06-A.
  - All existing group_ids must match the term they're listed under.
  - Verse counts per group must match the doc's stated counts.

Outputs:
  - DB writes (transactional)
  - Workflow application report:
    Sessions/Session_Clusters/M06/
      WA-M06-A-group-mapping-applied-v1-20260506.md

Invocation:
  --dry-run   parse + validate + report only (no DB writes)
  --live      apply (default behaviour requires explicit --live)
"""
from __future__ import annotations

import argparse
import os
import re
import shutil
import sqlite3
import sys
from collections import defaultdict
from datetime import datetime, timezone

DB_PATH = os.path.join("database", "bible_research.db")
BACKUP_DIR = "backups"
DOC_PATH = os.path.join(
    "Sessions", "Session_Clusters", "M06",
    "WA-M06-A-group-verse-mapping-v1-20260506.md",
)
REPORT_DIR = os.path.join("Sessions", "Session_Clusters", "M06")

# Term → mti_id pre-resolved (verified earlier).
TERM_MTI = {
    "H8130": 550,    # sa.ne
    "H8131": 1663,   # se.na
    "H8135": 902,    # sin.ah
    "H4895": 903,    # mas.te.mah
    "H7852": 5518,   # sa.tam
}
M06_A_SUBGROUP_CODE = "M06-A"


# ---------- Parsing helpers --------------------------------------------------

REF_RE = re.compile(
    r"^(?P<book>\d?[A-Za-z]{2,5})\s+(?P<chap>\d+):(?P<verse>\d+)$"
)


def now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def backup_db() -> str:
    os.makedirs(BACKUP_DIR, exist_ok=True)
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    dest = os.path.join(
        BACKUP_DIR, f"bible_research_{ts}_pre_m06_a_mapping.db"
    )
    shutil.copy2(DB_PATH, dest)
    return dest


def build_book_lookup(conn) -> dict:
    out = {}
    for r in conn.execute(
        "SELECT id, name, abbreviation, short_code FROM books"
    ).fetchall():
        bid = r["id"]
        for k in (r["abbreviation"], r["short_code"], r["name"]):
            if k:
                out[k.lower()] = bid
    aliases = {
        "1cor": "1Co", "2cor": "2Co", "1th": "1Th", "2th": "2Th",
        "song": "Sng", "ps": "Psa",
        "1sam": "1Sa", "2sam": "2Sa", "1kgs": "1Ki", "2kgs": "2Ki",
        "1chr": "1Ch", "2chr": "2Ch",
        "deut": "Deu", "prov": "Pro", "eccl": "Ecc", "ecc": "Ecc",
        "isa": "Isa", "jer": "Jer", "josh": "Jos", "judg": "Jdg",
        "ezek": "Eze", "zech": "Zec",
        "amos": "Amo", "mic": "Mic", "hos": "Hos", "mal": "Mal",
        "dan": "Dan", "job": "Job", "num": "Num",
    }
    for alt, can in aliases.items():
        if can.lower() in out:
            out[alt.lower()] = out[can.lower()]
    return out


# Section parser
GROUP_HEADER_RE = re.compile(
    r"^### GROUP\s+(?P<head>[^\n]+)$",
    re.MULTILINE,
)


def extract_section(text: str, start: int, end: int) -> str:
    return text[start:end]


def parse_doc(path: str):
    """Yield {key, action, existing_id_or_None, term, group_code,
              description, notes, verses=[(ref, term, obs)], anchor_ref}.
    Plus a separate dual-assignment list."""
    with open(path, encoding="utf-8") as f:
        text = f.read()

    # Split on group headers
    headers = list(GROUP_HEADER_RE.finditer(text))
    sections = []
    for i, m in enumerate(headers):
        s = m.end()
        e = headers[i + 1].start() if i + 1 < len(headers) else len(text)
        sections.append((m.group("head").strip(), text[s:e]))

    groups = []
    dual_section_text = ""
    for head, body in sections:
        # The cross-group / set-aside trailing material is a "### VERSES"
        # block which doesn't match GROUP_HEADER_RE; we'll handle that
        # separately below from text post the last GROUP block.
        groups.append(parse_group_section(head, body))

    # Locate the dual-assignment section.
    m = re.search(
        r"### VERSES REQUIRING ADDITIONAL REVIEW[^\n]*\n([\s\S]*?)(?=\n## |\Z)",
        text,
    )
    duals = parse_dual_section(m.group(1)) if m else []

    return groups, duals


VERSE_TABLE_RE = re.compile(
    r"^\|\s*(?P<ref>[^|]+?)\s*\|\s*(?P<term>H\d{4}[A-Za-z]?|G\d{4}[A-Za-z]?)\s+\S+\s*\|\s*(?P<obs>[^|]+?)\s*\|$",
    re.MULTILINE,
)
ANCHOR_LINE_RE = re.compile(
    r"\*\*Anchor verse for [^*]+?:\*\*\s*\*\*(?P<ref>[^*]+?)\*\*",
)
EXISTING_CODE_RE = re.compile(r"\*\*Existing code:\*\*\s*(\d+)")
PROVISIONAL_CODE_RE = re.compile(r"\*\*Provisional code:\*\*\s*(\S+)")
REVISED_DESC_RE = re.compile(
    r"\*\*Revised description(?:[^:]*?):\*\*\s*([^\n]+)"
)
REFINED_DESC_RE = re.compile(
    r"\*\*Refined description(?:[^:]*?):\*\*\s*([^\n]+)"
)
RETAINED_DESC_RE = re.compile(
    r"\*\*Retained description(?:[^:]*?):\*\*\s*([^\n]+)"
)
PROVISIONAL_DESC_RE = re.compile(
    r"\*\*Description:\*\*\s*([^\n]+)"
)
NOTE_RE = re.compile(r"\*\*Note:\*\*\s*([^\n]+)")


def parse_group_section(head: str, body: str) -> dict:
    # head e.g. "1601 — RETAINED AND REFINED" or "M06-A-NEW-01 — NEW"
    # Split on em-dash; treat hyphens as part of the key (e.g. M06-A-NEW-01).
    parts = [p.strip() for p in head.split("—", 1)]
    head_key = parts[0].strip()
    head_status = parts[1].strip() if len(parts) > 1 else ""
    # Status synthesis
    if "NEW" in head_status:
        action = "INSERT"
    elif "RETAINED AND REFINED" in head_status or "RETAINED AND REFINED" in head:
        action = "UPDATE"
    elif "REVIEW AND DECISION" in head:
        action = "UPDATE"
    elif "RETAINED" in head:
        action = "UPDATE"  # may be no-op if description identical
    else:
        action = "UPDATE"

    existing_id = None
    m = EXISTING_CODE_RE.search(body)
    if m:
        existing_id = int(m.group(1))

    # Description: priority — Revised > Refined > Retained > Description
    desc = None
    for rgx in (REVISED_DESC_RE, REFINED_DESC_RE, RETAINED_DESC_RE,
                PROVISIONAL_DESC_RE):
        m = rgx.search(body)
        if m:
            desc = m.group(1).strip()
            break

    notes = None
    m = NOTE_RE.search(body)
    if m:
        notes = m.group(1).strip()

    # Anchor
    anchor_ref = None
    m = ANCHOR_LINE_RE.search(body)
    if m:
        anchor_ref = m.group("ref").strip()

    # Verses table
    verses = []
    for vm in VERSE_TABLE_RE.finditer(body):
        ref = vm.group("ref").strip()
        if ref.lower() == "verse" or "---" in ref:
            continue
        term = vm.group("term").strip()
        obs = vm.group("obs").strip()
        verses.append((ref, term, obs))

    # The first row of every markdown table is the header — VERSE_TABLE_RE
    # was designed to skip it (header has "Verse" in col 1, not a real ref),
    # but the term column wouldn't match HXXXX so it's fine.

    # Strip any column "What the verse shows"
    verses = [(r, t, o) for (r, t, o) in verses
              if not r.lower().startswith("verse")]

    return {
        "key": head_key,
        "head": head,
        "status": head_status,
        "action": action,
        "existing_id": existing_id,
        "description": desc,
        "notes": notes,
        "anchor_ref": anchor_ref,
        "verses": verses,
    }


DUAL_ROW_RE = re.compile(
    r"^\|\s*(?P<ref>[^|]+?)\s*\|\s*(?P<term>[^|]+?)\s*\|\s*(?P<primary>[^|]+?)\s*\|\s*(?P<secondary>[^|]+?)\s*\|\s*(?P<reason>[^|]+?)\s*\|$",
    re.MULTILINE,
)


RANGE_REF_RE = re.compile(
    r"^(?P<book>\d?[A-Za-z]{2,5})\s+(?P<chap>\d+):"
    r"(?P<v1>\d+)-(?P<v2>\d+)$"
)


def parse_dual_section(text: str):
    rows = []
    for m in DUAL_ROW_RE.finditer(text):
        ref = m.group("ref").strip()
        if ref.lower() == "verse" or "---" in ref:
            continue
        term = m.group("term").strip()
        primary = m.group("primary").strip()
        secondary = m.group("secondary").strip()
        reason = m.group("reason").strip()
        # Expand verse ranges (e.g. "Psa 139:21-22" -> two rows).
        rng = RANGE_REF_RE.match(ref)
        if rng:
            book = rng.group("book")
            chap = rng.group("chap")
            v1 = int(rng.group("v1"))
            v2 = int(rng.group("v2"))
            for v in range(v1, v2 + 1):
                rows.append({
                    "ref": f"{book} {chap}:{v}",
                    "term_raw": term,
                    "primary": primary,
                    "secondary": secondary,
                    "reason": reason,
                })
            continue
        rows.append({
            "ref": ref,
            "term_raw": term,
            "primary": primary,
            "secondary": secondary,
            "reason": reason,
        })
    return rows


# ---------- Reference resolution --------------------------------------------

def resolve_ref(ref: str, book_lookup: dict):
    m = REF_RE.match(ref.strip())
    if not m:
        return None
    book_token = m.group("book")
    chap = int(m.group("chap"))
    verse = int(m.group("verse"))
    bid = book_lookup.get(book_token.lower())
    if not bid:
        return None
    return (bid, chap, verse)


def vr_id_for(conn, bid, chap, verse, mti_id):
    r = conn.execute("""
        SELECT id FROM wa_verse_records
         WHERE book_id=? AND chapter=? AND verse_num=? AND mti_term_id=?
           AND COALESCE(delete_flagged,0)=0
    """, (bid, chap, verse, mti_id)).fetchone()
    return r["id"] if r else None


# ---------- Main -------------------------------------------------------------

def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--live", action="store_true")
    args = ap.parse_args()

    if not args.dry_run and not args.live:
        print("Specify --dry-run or --live.")
        return 2

    print(f"Doc: {DOC_PATH}")
    print(f"DB:  {DB_PATH}")

    groups, duals = parse_doc(DOC_PATH)
    print(f"Parsed {len(groups)} group sections, {len(duals)} dual rows.")

    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    book_lookup = build_book_lookup(conn)

    # ---- Decision-1A reshape: NEW-04 spans H8130 + H8131; split into 2 rows.
    # The doc has it in one section. We split at apply time by which term
    # each verse uses. So we emit two synthetic group records keyed
    # NEW-04-H8130 and NEW-04-H8131.

    expanded = []
    for g in groups:
        if g["key"] == "M06-A-NEW-04":
            for term in ("H8130", "H8131"):
                gv = [v for v in g["verses"] if v[1] == term]
                if not gv:
                    continue
                anchor_ref = g["anchor_ref"]
                # Anchor stays only on the term it belongs to
                anchor_ok = False
                if anchor_ref:
                    for vref, vterm, _ in gv:
                        if vref == anchor_ref and vterm == term:
                            anchor_ok = True
                            break
                expanded.append({
                    **g,
                    "key": f"M06-A-NEW-04-{term}",
                    "term": term,
                    "verses": gv,
                    "anchor_ref": anchor_ref if anchor_ok else None,
                    "group_code": f"{TERM_MTI[term]}-NEW-04",
                })
        else:
            # Determine the term: take from the first verse if not explicit.
            terms_in_grp = {v[1] for v in g["verses"]}
            if len(terms_in_grp) == 1:
                term = next(iter(terms_in_grp))
            elif len(terms_in_grp) == 0:
                term = "H8130"  # singleton 1602/1199 cases handled below
            else:
                # Should not happen for any group except NEW-04; fallback
                # to dominant term.
                from collections import Counter
                term = Counter([v[1] for v in g["verses"]]).most_common(1)[0][0]
            group_code = None
            if g["action"] == "INSERT":
                # New group: code = "{mti}-{NEW-NN}"
                # key like "M06-A-NEW-01"  → suffix "NEW-01"
                suffix = g["key"].replace("M06-A-", "")
                group_code = f"{TERM_MTI[term]}-{suffix}"
            expanded.append({
                **g,
                "term": term,
                "group_code": group_code,
            })

    # ---- Pre-flight validation
    issues = []
    resolved_by_group = []  # list of (group_obj, resolved_verses=[(vr_id,...)])
    for g in expanded:
        rv = []
        for ref, term, obs in g["verses"]:
            r = resolve_ref(ref, book_lookup)
            if not r:
                issues.append(f"{g['key']}: unparseable ref '{ref}'")
                continue
            if term not in TERM_MTI:
                issues.append(
                    f"{g['key']}: unknown term '{term}' on {ref}"
                )
                continue
            mti_id = TERM_MTI[term]
            vr_id = vr_id_for(conn, *r, mti_id)
            if not vr_id:
                issues.append(
                    f"{g['key']}: no wa_verse_records row for "
                    f"{term} {ref}"
                )
                continue
            rv.append({
                "ref": ref, "term": term, "mti_id": mti_id,
                "vr_id": vr_id, "obs": obs,
            })
        # Anchor lookup
        anchor_vr_id = None
        if g["anchor_ref"]:
            r = resolve_ref(g["anchor_ref"], book_lookup)
            if r:
                # Anchor term is the group's term unless it's a multi-term
                # case (handled by the split above).
                term_for_anchor = g.get("term")
                if term_for_anchor:
                    anchor_vr_id = vr_id_for(
                        conn, *r, TERM_MTI[term_for_anchor]
                    )
            if not anchor_vr_id:
                issues.append(
                    f"{g['key']}: anchor verse '{g['anchor_ref']}' "
                    f"not resolvable"
                )

        # Existing-id sanity
        if g["existing_id"]:
            chk = conn.execute(
                "SELECT mti_term_id FROM verse_context_group "
                " WHERE id=? AND COALESCE(delete_flagged,0)=0",
                (g["existing_id"],),
            ).fetchone()
            if not chk:
                issues.append(
                    f"{g['key']}: existing group id {g['existing_id']} "
                    f"not found"
                )
            elif chk["mti_term_id"] != TERM_MTI[g["term"]]:
                issues.append(
                    f"{g['key']}: existing group id {g['existing_id']} "
                    f"has mti_term_id={chk['mti_term_id']}, doc expects "
                    f"{TERM_MTI[g['term']]}"
                )

        resolved_by_group.append((g, rv, anchor_vr_id))

    # Resolve dual-assignment rows
    dual_resolved = []
    dual_skipped = []  # (ref, term, reason) — non-blocking
    # Build group-key → group-obj map (post-expansion)
    key_to_group = {g["key"]: g for g in expanded}
    # Also keep raw ID lookups for existing groups
    id_to_group = {g["existing_id"]: g for g in expanded if g["existing_id"]}

    def resolve_group_token(tok: str):
        """Map 'M06-A-NEW-04', '1601', etc. into a group dict."""
        s = tok.strip()
        # If numeric, treat as existing id
        m = re.match(r"^(\d+)\b", s)
        if m:
            gid = int(m.group(1))
            return id_to_group.get(gid)
        # If M06-A-NEW-XX or NEW-XX, look for matching key
        # The dual table sometimes uses "M06-A-NEW-04" — we'll route
        # by Strong's of the verse to NEW-04-H8130 or NEW-04-H8131.
        for k, g in key_to_group.items():
            if k == s or k.startswith(s):
                return g
            if k.endswith("-" + s):
                return g
        return None

    for d in duals:
        # Term column: "H8130" or "H8130 + H8135"
        terms = re.findall(r"H\d{4}[A-Za-z]?|G\d{4}[A-Za-z]?", d["term_raw"])
        ref_resolved = resolve_ref(d["ref"], book_lookup)
        if not ref_resolved:
            issues.append(f"DUAL: unparseable ref '{d['ref']}'")
            continue
        for term in terms:
            if term not in TERM_MTI:
                issues.append(f"DUAL {d['ref']}: unknown term {term}")
                continue
            mti_id = TERM_MTI[term]
            vr_id = vr_id_for(conn, *ref_resolved, mti_id)
            if not vr_id:
                dual_skipped.append(
                    (d["ref"], term,
                     "no wa_verse_records row "
                     "(term not present at this verse)")
                )
                continue
            # Route NEW-04 to the term-specific row
            primary = d["primary"]
            secondary = d["secondary"]
            # Strip helper text ("(human hatred...)" etc.) — take the
            # first numeric-or-NEW token
            def first_token(s):
                m = re.match(
                    r"\s*([A-Z0-9\-]+(?:-NEW-\d{2})?)", s,
                )
                if m:
                    return m.group(1)
                return s.split()[0] if s.split() else s
            primary_tok = first_token(primary)
            secondary_tok = first_token(secondary)
            # Refine NEW-04 routing by term suffix
            if primary_tok == "M06-A-NEW-04":
                primary_tok = f"M06-A-NEW-04-{term}"
            if secondary_tok == "M06-A-NEW-04":
                secondary_tok = f"M06-A-NEW-04-{term}"
            pgrp = resolve_group_token(primary_tok)
            sgrp = resolve_group_token(secondary_tok)
            if not pgrp:
                issues.append(
                    f"DUAL {d['ref']} {term}: primary "
                    f"'{primary}' unresolved"
                )
            if not sgrp:
                issues.append(
                    f"DUAL {d['ref']} {term}: secondary "
                    f"'{secondary}' unresolved"
                )
            dual_resolved.append({
                "ref": d["ref"], "term": term, "vr_id": vr_id,
                "mti_id": mti_id,
                "primary_grp": pgrp, "secondary_grp": sgrp,
                "reason": d["reason"],
            })

    # Doc-stated counts (from §Summary table at the end)
    DOC_COUNTS = {
        "1601": 49,
        "M06-A-NEW-01": 9,
        "M06-A-NEW-02": 16,
        "M06-A-NEW-03": 17,
        "M06-A-NEW-04": 13,
        "1200": 6,
        "1201": 5,
        "1202": 2,
        "1203": 2,
        "3590": 4,
        "1199": 2,
        "1602": 1,
    }

    print()
    print("Verse-count check (doc expectation vs parsed):")
    # Aggregate parsed counts back to original doc keys (NEW-04 sums two parts).
    parsed_counts = defaultdict(int)
    for g, rv, _ in resolved_by_group:
        canonical_key = g["key"]
        if canonical_key.startswith("M06-A-NEW-04"):
            canonical_key = "M06-A-NEW-04"
        parsed_counts[canonical_key] += len(rv)
    for k, want in DOC_COUNTS.items():
        got = parsed_counts.get(k, 0)
        ok = "OK" if got == want else "MISMATCH"
        print(f"  {k:18s}  parsed={got:3d}  doc={want:3d}  {ok}")
        if got != want:
            issues.append(
                f"COUNT: {k} parsed={got} doc={want}"
            )

    if issues:
        print()
        print(f"! {len(issues)} pre-flight issue(s):")
        for i in issues[:30]:
            print(f"  - {i}")
        if len(issues) > 30:
            print(f"  - ... +{len(issues) - 30} more")
        if args.live:
            print()
            print("Aborting --live: pre-flight issues must be resolved.")
            return 3

    # ---- Apply phase
    actions_log = []  # for the report

    if args.dry_run:
        print()
        print("--dry-run: no DB writes.")
    else:
        print()
        print("Backing up DB...")
        bak = backup_db()
        print(f"  -> {bak}")

        try:
            conn.execute("BEGIN")

            # Step 1 — INSERT new groups, capture new IDs
            for g, rv, anchor_vr_id in resolved_by_group:
                if g["action"] != "INSERT":
                    continue
                cur = conn.execute("""
                    INSERT INTO verse_context_group
                      (mti_term_id, group_code, context_description,
                       notes, delete_flagged, vertical_pass_flag)
                    VALUES (?, ?, ?, ?, 0, 0)
                """, (
                    TERM_MTI[g["term"]], g["group_code"],
                    g["description"],
                    (g.get("notes") or "")
                    + " | Source: WA-M06-A-group-verse-mapping-v1-20260506",
                ))
                new_id = cur.lastrowid
                g["resolved_id"] = new_id
                actions_log.append({
                    "type": "INSERT_GROUP",
                    "key": g["key"],
                    "group_id": new_id,
                    "group_code": g["group_code"],
                    "term": g["term"],
                    "mti_id": TERM_MTI[g["term"]],
                })

            # Step 2 — UPDATE existing group descriptions
            for g, rv, _ in resolved_by_group:
                if g["action"] != "UPDATE":
                    continue
                if not g["existing_id"]:
                    continue
                # Skip pure RETAINED with no description change
                # (we'll always UPDATE — idempotent if same).
                conn.execute("""
                    UPDATE verse_context_group
                       SET context_description = COALESCE(?, context_description),
                           notes = ?
                     WHERE id = ?
                """, (
                    g["description"],
                    (g.get("notes") or "")
                    + " | Refined per WA-M06-A-group-verse-mapping-v1-20260506",
                    g["existing_id"],
                ))
                g["resolved_id"] = g["existing_id"]
                actions_log.append({
                    "type": "UPDATE_GROUP",
                    "key": g["key"],
                    "group_id": g["existing_id"],
                })

            # Step 3 — Target-set reassignment for each (vr_id, mti_id).
            #
            # The doc tells us the EXACT set of groups each verse-term pair
            # should belong to — primary plus any duals. We:
            #   1. Build the target set per (vr_id, mti_id).
            #   2. Reuse existing live rows where possible (preserves ids,
            #      provenance, audit trail).
            #   3. Soft-delete legacy M06-A rows that are no longer in
            #      the target set (this is the migration step — e.g.
            #      Gen 29:31's old group_id=1601 row gets converted to
            #      group_id=NEW-01).
            #   4. Set-aside rows are never touched (decision 4).

            # Build per-pair target list.
            target_per_pair = defaultdict(list)
            # primary memberships
            for g, rv, anchor_vr_id in resolved_by_group:
                gid = g.get("resolved_id")
                if not gid:
                    continue
                for v in rv:
                    target_per_pair[(v["vr_id"], v["mti_id"])].append({
                        "group_id": gid,
                        "obs": v["obs"],
                        "source": f"primary ({g['key']})",
                    })
                # Anchor verse: if the doc names an anchor for this group
                # but the anchor verse isn't enumerated in the verse table
                # (which the doc allows), treat it as an implicit primary
                # membership so the (vr_id, mti_id) pair gets processed.
                if anchor_vr_id:
                    anchor_mti = TERM_MTI[g["term"]]
                    pair = (anchor_vr_id, anchor_mti)
                    if not any(
                        t["group_id"] == gid for t in target_per_pair[pair]
                    ):
                        target_per_pair[pair].append({
                            "group_id": gid,
                            "obs": (
                                f"Anchor verse for group "
                                f"{g['key']} (named as anchor in "
                                f"the mapping doc; not separately "
                                f"enumerated in the verse table)"
                            ),
                            "source": f"anchor-implicit ({g['key']})",
                        })
            # dual memberships
            for d in dual_resolved:
                sgrp = d["secondary_grp"]
                if not sgrp:
                    continue
                sgid = sgrp.get("resolved_id") or sgrp.get("existing_id")
                if not sgid:
                    continue
                target_per_pair[(d["vr_id"], d["mti_id"])].append({
                    "group_id": sgid,
                    "obs": (
                        "Dual assignment (secondary, source from "
                        "cross-group table): " + d["reason"]
                    ),
                    "source": f"dual-secondary",
                })

            # anchor flag map: (vr_id, mti_id, group_id) -> 1
            anchors_to_set = set()
            for g, _, anchor_vr_id in resolved_by_group:
                gid = g.get("resolved_id")
                if anchor_vr_id and gid:
                    anchors_to_set.add(
                        (anchor_vr_id, TERM_MTI[g["term"]], gid)
                    )

            # Clear existing anchors on every group we touched (we'll
            # re-set the chosen ones below).
            touched_gids = {
                t["group_id"]
                for tlist in target_per_pair.values() for t in tlist
            }
            for gid in touched_gids:
                conn.execute("""
                    UPDATE verse_context
                       SET is_anchor = 0
                     WHERE group_id = ?
                       AND is_anchor = 1
                       AND COALESCE(delete_flagged,0) = 0
                """, (gid,))

            n_upd = n_ins = n_repurposed = n_softdel = 0

            for (vr_id, mti_id), targets in target_per_pair.items():
                target_gids = {t["group_id"] for t in targets}

                # Existing live, non-set-aside rows for this pair.
                existing = conn.execute("""
                    SELECT id, group_id
                      FROM verse_context
                     WHERE verse_record_id=? AND mti_term_id=?
                       AND COALESCE(delete_flagged,0)=0
                       AND set_aside_reason IS NULL
                """, (vr_id, mti_id)).fetchall()
                existing_by_gid = {r["group_id"]: r["id"] for r in existing}
                used_ids = set()

                for t in targets:
                    gid = t["group_id"]
                    is_anchor = 1 if (vr_id, mti_id, gid) in anchors_to_set else 0
                    if gid in existing_by_gid:
                        # Already there — just refresh fields.
                        conn.execute("""
                            UPDATE verse_context
                               SET is_relevant=1, is_anchor=?, is_related=0,
                                   set_aside_reason=NULL,
                                   analysis_note=?,
                                   notes=?
                             WHERE id=?
                        """, (
                            is_anchor, t["obs"],
                            "M06-A group mapping v1 (2026-05-06)",
                            existing_by_gid[gid],
                        ))
                        used_ids.add(existing_by_gid[gid])
                        n_upd += 1
                    else:
                        # Try to repurpose a spare existing row whose
                        # current group_id is NOT one of our targets.
                        spare = next((
                            r for r in existing
                            if r["group_id"] not in target_gids
                            and r["id"] not in used_ids
                        ), None)
                        if spare:
                            conn.execute("""
                                UPDATE verse_context
                                   SET group_id=?, is_relevant=1,
                                       is_anchor=?, is_related=0,
                                       set_aside_reason=NULL,
                                       analysis_note=?,
                                       notes=?
                                 WHERE id=?
                            """, (
                                gid, is_anchor, t["obs"],
                                "M06-A group mapping v1 (2026-05-06)",
                                spare["id"],
                            ))
                            used_ids.add(spare["id"])
                            n_repurposed += 1
                        else:
                            conn.execute("""
                                INSERT INTO verse_context
                                  (verse_record_id, mti_term_id, group_id,
                                   is_anchor, is_relevant, is_related,
                                   notes, delete_flagged, set_aside_reason,
                                   analysis_note)
                                VALUES (?, ?, ?, ?, 1, 0, ?, 0, NULL, ?)
                            """, (
                                vr_id, mti_id, gid, is_anchor,
                                "M06-A group mapping v1 (2026-05-06)",
                                t["obs"],
                            ))
                            n_ins += 1

                # Soft-delete any remaining live, non-set-aside rows
                # whose group_id isn't in the target set — these are
                # legacy M06-A memberships that the doc has migrated away
                # from, e.g. Gen 29:31's group_id=1601 row when the verse
                # is now NEW-01 only.
                for r in existing:
                    if r["id"] in used_ids:
                        continue
                    if r["group_id"] in target_gids:
                        continue
                    conn.execute("""
                        UPDATE verse_context
                           SET delete_flagged = 1,
                               notes = COALESCE(notes,'')
                                       || ' | superseded by M06-A '
                                       || 'group mapping v1 (2026-05-06)'
                         WHERE id = ?
                    """, (r["id"],))
                    n_softdel += 1

            actions_log.append({
                "type": "VC_REASSIGN_SUMMARY",
                "n_updated": n_upd,
                "n_inserted": n_ins,
                "n_repurposed": n_repurposed,
                "n_softdeleted": n_softdel,
            })

            # Anchor actions for the report
            for (vr_id, mti_id, gid) in anchors_to_set:
                actions_log.append({
                    "type": "ANCHOR",
                    "vr_id": vr_id, "mti_id": mti_id, "group_id": gid,
                })

            conn.execute("COMMIT")
            print("[ok] DB writes committed.")
        except Exception as e:
            conn.execute("ROLLBACK")
            print(f"[err] ERROR — rolled back: {e}")
            raise

    # ---- Build the "addressed by doc" set + the list of unaddressed
    # M06-A verses currently in any M06-A group, for the AI handoff.
    doc_refs = set()
    for g, rv, _ in resolved_by_group:
        for v in rv:
            doc_refs.add((v["vr_id"], v["mti_id"]))
    for d in dual_resolved:
        doc_refs.add((d["vr_id"], d["mti_id"]))

    # M06-A mti_ids
    sub = conn.execute(
        "SELECT id FROM cluster_subgroup WHERE subgroup_code='M06-A'"
    ).fetchone()
    if sub:
        m06a_mti_ids = [
            r["id"] for r in conn.execute(
                "SELECT id FROM mti_terms "
                " WHERE cluster_subgroup_id=? "
                "   AND COALESCE(delete_flagged,0)=0",
                (sub["id"],),
            )
        ]
    else:
        m06a_mti_ids = []

    unaddressed = []
    if m06a_mti_ids:
        ph = ",".join("?" * len(m06a_mti_ids))
        for r in conn.execute(f"""
            SELECT vc.id AS vc_id, vc.verse_record_id, vc.mti_term_id,
                   vc.group_id, vc.is_anchor,
                   vr.reference, mt.strongs_number
              FROM verse_context vc
              JOIN wa_verse_records vr
                ON vr.id = vc.verse_record_id
              JOIN mti_terms mt ON mt.id = vc.mti_term_id
             WHERE vc.mti_term_id IN ({ph})
               AND COALESCE(vc.delete_flagged,0) = 0
               AND vc.set_aside_reason IS NULL
               AND vc.group_id IS NOT NULL AND vc.group_id > 0
             ORDER BY vr.book_id, vr.chapter, vr.verse_num
        """, m06a_mti_ids):
            if (r["verse_record_id"], r["mti_term_id"]) not in doc_refs:
                unaddressed.append(dict(r))

    # ---- Application report
    write_report(
        path=os.path.join(
            REPORT_DIR,
            "WA-M06-A-group-mapping-applied-v1-20260506.md"
            if args.live else
            "WA-M06-A-group-mapping-dryrun-v1-20260506.md"
        ),
        groups=resolved_by_group,
        duals=dual_resolved,
        dual_skipped=dual_skipped,
        actions_log=actions_log,
        issues=issues,
        unaddressed=unaddressed,
        is_dry=args.dry_run,
    )

    conn.close()
    return 0


def upsert_verse_context(conn, v, group_id, observation, is_anchor=0):
    existing = conn.execute("""
        SELECT id, group_id, is_relevant, set_aside_reason
          FROM verse_context
         WHERE verse_record_id = ? AND mti_term_id = ?
           AND COALESCE(delete_flagged,0) = 0
           AND (group_id = ? OR group_id IS NULL OR group_id = 0)
    """, (v["vr_id"], v["mti_id"], group_id)).fetchone()
    if existing:
        conn.execute("""
            UPDATE verse_context
               SET group_id = ?,
                   is_relevant = 1,
                   is_anchor = ?,
                   is_related = 0,
                   set_aside_reason = NULL,
                   analysis_note = ?,
                   notes = ?
             WHERE id = ?
        """, (
            group_id, is_anchor, observation,
            "M06-A group mapping v1 (2026-05-06)",
            existing["id"],
        ))
    else:
        conn.execute("""
            INSERT INTO verse_context
              (verse_record_id, mti_term_id, group_id,
               is_anchor, is_relevant, is_related, notes,
               delete_flagged, set_aside_reason, analysis_note)
            VALUES (?, ?, ?, ?, 1, 0, ?, 0, NULL, ?)
        """, (
            v["vr_id"], v["mti_id"], group_id, is_anchor,
            "M06-A group mapping v1 (2026-05-06)", observation,
        ))


def ensure_verse_context_row(conn, vr_id, mti_id, group_id, observation):
    existing = conn.execute("""
        SELECT id FROM verse_context
         WHERE verse_record_id = ? AND mti_term_id = ? AND group_id = ?
           AND COALESCE(delete_flagged,0) = 0
    """, (vr_id, mti_id, group_id)).fetchone()
    if existing:
        conn.execute("""
            UPDATE verse_context
               SET is_relevant = 1, set_aside_reason = NULL,
                   analysis_note = ?
             WHERE id = ?
        """, (observation, existing["id"]))
    else:
        conn.execute("""
            INSERT INTO verse_context
              (verse_record_id, mti_term_id, group_id,
               is_anchor, is_relevant, is_related, notes,
               delete_flagged, set_aside_reason, analysis_note)
            VALUES (?, ?, ?, 0, 1, 0, ?, 0, NULL, ?)
        """, (
            vr_id, mti_id, group_id,
            "M06-A dual assignment v1 (2026-05-06)", observation,
        ))


# ---------- Report writer ---------------------------------------------------

def write_report(path, groups, duals, dual_skipped, actions_log, issues,
                 unaddressed, is_dry: bool):
    L = []

    def add(s=""):
        L.append(s)

    add("# WA-M06-A — Group / verse mapping application report")
    add()
    add(f"**Generated:** {now_iso()}  ")
    add(f"**Mode:** {'DRY-RUN (no DB writes)' if is_dry else 'LIVE (applied)'}  ")
    add(f"**Source mapping doc:** "
        "`Sessions/Session_Clusters/M06/"
        "WA-M06-A-group-verse-mapping-v1-20260506.md`  ")
    add(f"**Sub-group:** `M06-A` (Hatred)  ")
    add(f"**Groups touched:** {len(groups)}  ")
    add(f"**Dual-assignment rows:** {len(duals)}  ")
    add()

    # Pre-flight summary
    add("## §1. Pre-flight validation")
    add()
    if not issues:
        add("All resolutions clean — every verse reference resolved to a "
            "`wa_verse_records` row for the named term, every existing "
            "group id matches the term it's listed under, and every "
            "verse-count matches the document's stated total.")
    else:
        add(f"! {len(issues)} issue(s):")
        add()
        for i in issues:
            add(f"- {i}")
    add()

    # Group-by-group
    add("## §2. Per-group changes")
    add()
    for g, rv, anchor_vr_id in groups:
        gid = g.get("resolved_id") or g.get("existing_id") or "(pending)"
        add(f"### {g['key']} ({g['action']}) — group_id `{gid}`")
        add()
        add(f"**Term:** {g['term']} (mti_id `{TERM_MTI[g['term']]}`)  ")
        if g.get("group_code"):
            add(f"**Group code:** `{g['group_code']}`  ")
        if g.get("description"):
            add(f"**Description:** {g['description']}  ")
        if g.get("notes"):
            add(f"**Note:** {g['notes']}  ")
        anchor_text = (g["anchor_ref"]
                       if g.get("anchor_ref")
                       else "(no anchor)")
        add(f"**Anchor verse:** {anchor_text}  ")
        add(f"**Verses ({len(rv)}):**")
        add()
        if rv:
            add("| Reference | Term | Observation |")
            add("|---|---|---|")
            for v in rv:
                obs = (v["obs"] or "").replace("|", "\\|")
                add(f"| {v['ref']} | {v['term']} | {obs} |")
        else:
            add("(none)")
        add()

    # Dual-assignment summary
    add("## §3. Dual-group assignments")
    add()
    if dual_skipped:
        add(f"_{len(dual_skipped)} dual row(s) skipped — verse/term "
            "combination has no `wa_verse_records` entry "
            "(term not present at this verse):_")
        add()
        for ref, term, reason in dual_skipped:
            add(f"- `{ref}` {term} — {reason}")
        add()
    if not duals:
        add("(none)")
    else:
        add("| Reference | Term | Primary group | Secondary group | Reason |")
        add("|---|---|---|---|---|")
        for d in duals:
            p = d["primary_grp"]
            s = d["secondary_grp"]
            p_id = (p.get("resolved_id") or p.get("existing_id")
                    if p else "(unresolved)")
            s_id = (s.get("resolved_id") or s.get("existing_id")
                    if s else "(unresolved)")
            reason = d["reason"].replace("|", "\\|")
            add(f"| {d['ref']} | {d['term']} | "
                f"{p['key'] if p else '?'} (`{p_id}`) | "
                f"{s['key'] if s else '?'} (`{s_id}`) | "
                f"{reason} |")
    add()

    # Actions log
    add("## §4. Database actions executed")
    add()
    if not actions_log:
        add("_(dry-run — no actions executed)_" if is_dry else "(none)")
    else:
        n_ins_grp = sum(1 for a in actions_log
                         if a["type"] == "INSERT_GROUP")
        n_upd_grp = sum(1 for a in actions_log
                         if a["type"] == "UPDATE_GROUP")
        n_anc = sum(1 for a in actions_log if a["type"] == "ANCHOR")
        vc_summary = next(
            (a for a in actions_log if a["type"] == "VC_REASSIGN_SUMMARY"),
            None,
        )
        add(f"- **`verse_context_group`** — {n_ins_grp} INSERT, "
            f"{n_upd_grp} UPDATE (description refresh)")
        if vc_summary:
            add(f"- **`verse_context`** target-set reassignment:")
            add(f"  - {vc_summary['n_updated']} existing rows refreshed "
                f"(group_id already correct)")
            add(f"  - {vc_summary['n_repurposed']} existing rows "
                f"repurposed (group_id reassigned — migration)")
            add(f"  - {vc_summary['n_inserted']} new rows inserted "
                f"(no spare row available — fresh insert)")
            add(f"  - {vc_summary['n_softdeleted']} legacy rows "
                f"soft-deleted (group_id no longer in target set)")
        add(f"- **Anchor designations:** {n_anc} verse_context rows "
            f"flagged is_anchor=1 (prior anchors on the same groups "
            f"cleared first)")
        add(f"- **Set-aside rows:** never touched (decision 4 — "
            f"set-asides not re-evaluated unless explicitly "
            f"re-discoverable)")
    add()

    # Unaddressed verses still in M06-A groups
    add("## §5. Verses currently assigned to an M06-A group but NOT "
        "enumerated in the mapping doc")
    add()
    add("These rows represent prior `verse_context` memberships in M06-A "
        "groups that the mapping document did **not** re-enumerate "
        "(neither in primary verse tables nor in the cross-group dual "
        "list). They have **not been touched** by this apply — left as-is "
        "per decision 4 (set-asides not re-evaluated; analogously, "
        "pre-existing memberships not addressed by the doc remain in "
        "place). Pass this list back to AI for review: are they "
        "oversights (should migrate to NEW-XX) or legitimate prior "
        "1601 / etc. memberships?")
    add()
    if not unaddressed:
        add("(none)")
    else:
        add(f"**Count:** {len(unaddressed)}")
        add()
        add("| Reference | Term | Current group_id | Anchor | vc_id |")
        add("|---|---|---:|:---:|---:|")
        for r in unaddressed:
            anc = "Y" if r["is_anchor"] else ""
            add(f"| {r['reference'].strip()} | {r['strongs_number']} "
                f"| {r['group_id']} | {anc} | {r['vc_id']} |")
    add()

    add("---")
    add()
    add("_End of report._")

    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(L) + "\n")
    print(f"Report: {path}")


if __name__ == "__main__":
    sys.exit(main())
