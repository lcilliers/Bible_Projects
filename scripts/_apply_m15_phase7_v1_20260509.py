"""_apply_m15_phase7_v1_20260509.py — DB-modifying.

Applies M15 Phase 7 group-verse mapping directives (dir-003 through
dir-009, one per sub-group A through G).

Each directive references its source mapping document (WA-M15-?-group-
verse-mapping-v?-2026050?.md). The mapping document is the canonical
analytical artefact; this script parses it and applies the per-verse
group assignments + anchor designations + analysis_note text to the DB.

Mapping-doc format expected:
  ## Group A-N — Title
  **Status:** NEW | RETAINED | RETAINED AND REFINED | (other)
  **Description from verses:** <text>
  **Anchor verse:** <Reference> ... — <rationale>

  | vr_id | Reference | Term | What the verse shows |
  | ----  | --------- | ---- | -------------------- |
  | 7326  | Exo 28:3  | H... | **ANCHOR** — text    |
  | 7327  | Exo 31:6  | H... | text                 |
  ...

Modes:
  --plan          parse all docs, show plan; NO DB writes
  --apply <subgroup-letter>   apply one directive (A..G)
  --apply-all     apply all 7 sequentially (A..G)

Per-directive transaction with PRAGMA foreign_keys=ON. Halt-on-error.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sqlite3
import sys
from datetime import datetime, timezone
from pathlib import Path

DB_PATH = os.path.join("database", "bible_research.db")
PHASE7_DIR = os.path.join(
    "Sessions", "Session_Clusters", "M15", "files phase 7"
)

# (sub_letter, directive_filename, mapping_doc_filename)
DIRECTIVES = [
    ("A", "wa-cluster-M15-dir-003-A-mapping-v1-20260509.md",
     "WA-M15-A-group-verse-mapping-v2-20260508.md"),
    ("B", "wa-cluster-M15-dir-004-B-mapping-v1-20260509.md",
     "WA-M15-B-group-verse-mapping-v1-20260508.md"),
    ("C", "wa-cluster-M15-dir-005-C-mapping-v1-20260509.md",
     "WA-M15-C-group-verse-mapping-v1-20260508.md"),
    ("D", "wa-cluster-M15-dir-006-D-mapping-v1-20260509.md",
     "WA-M15-D-group-verse-mapping-v1-20260508.md"),
    ("E", "wa-cluster-M15-dir-007-E-mapping-v1-20260509.md",
     "WA-M15-E-group-verse-mapping-v1-20260508.md"),
    ("F", "wa-cluster-M15-dir-008-F-mapping-v1-20260509.md",
     "WA-M15-F-group-verse-mapping-v1-20260508.md"),
    ("G", "wa-cluster-M15-dir-009-G-mapping-v1-20260509.md",
     "WA-M15-G-group-verse-mapping-v1-20260509.md"),
]


# ── Parser ────────────────────────────────────────────────────────────

GROUP_HEADING_RE = re.compile(
    r"^##\s+Group\s+([A-G]-\d+)"
    r"(?:\s*\(\s*(?:existing\s+code\s+)?(\d+)[^)]*\))?"
    r"\s+[—-]\s+(.+?)\s*$"
)
STATUS_RE = re.compile(r"^\*\*Status:\*\*\s*(.+?)\s*$")
DESC_RE = re.compile(r"^\*\*Description from verses:\*\*\s*(.+?)\s*$")
ANCHOR_HDR_RE = re.compile(r"^\*\*Anchor(?:\s+verse)?:\*\*\s*(.+?)\s*$")
H1_RE = re.compile(r"^#\s+")
H2_RE = re.compile(r"^##\s+")
# 4-column tables: vr_id | Reference | Term | What the verse shows
TABLE_ROW_4COL_RE = re.compile(
    r"^\|\s*(\d+)\s*\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|\s*(.+?)\s*\|\s*$"
)
# 3-column tables: vr_id | Reference | What the verse shows (no Term column)
TABLE_ROW_3COL_RE = re.compile(
    r"^\|\s*(\d+)\s*\|\s*([^|]+?)\s*\|\s*(.+?)\s*\|\s*$"
)
ANCHOR_MARKER_RE = re.compile(r"\*\*ANCHOR\*\*[\s—-]*", re.IGNORECASE)


def parse_mapping_doc(path: str) -> dict:
    text = Path(path).read_text(encoding="utf-8")
    lines = text.splitlines()
    groups = []
    cur_group = None
    in_table = False
    seen_header = False

    i = 0
    while i < len(lines):
        line = lines[i]

        # Group heading marks new section
        m = GROUP_HEADING_RE.match(line)
        if m:
            if cur_group:
                groups.append(cur_group)
            existing_code = m.group(2)
            cur_group = {
                "code": m.group(1),
                "title": m.group(3).strip(),
                "heading_existing_code": int(existing_code) if existing_code else None,
                "status_raw": None,
                "description": None,
                "anchor_raw": None,
                "verses": [],
            }
            in_table = False
            seen_header = False
            i += 1
            continue

        if cur_group is not None:
            ms = STATUS_RE.match(line)
            if ms:
                cur_group["status_raw"] = ms.group(1)
                i += 1
                continue
            md = DESC_RE.match(line)
            if md:
                cur_group["description"] = md.group(1)
                i += 1
                continue
            ma = ANCHOR_HDR_RE.match(line)
            if ma:
                cur_group["anchor_raw"] = ma.group(1)
                i += 1
                continue

            # Table rows: skip header and separator lines
            stripped = line.strip()
            if (stripped.startswith("| vr_id")
                    or (stripped.startswith("|---") and seen_header is False
                        and i > 0 and lines[i-1].strip().startswith("| vr_id"))
                    or stripped.startswith("|---")):
                # Header row OR separator row both mark table start
                if stripped.startswith("| vr_id"):
                    seen_header = True
                    in_table = True
                i += 1
                continue

            if seen_header:
                # Try 4-column first (richer); fall back to 3-column
                rm4 = TABLE_ROW_4COL_RE.match(line)
                rm3 = TABLE_ROW_3COL_RE.match(line) if not rm4 else None
                if rm4:
                    vr_id = int(rm4.group(1))
                    ref = rm4.group(2).strip()
                    term_str = rm4.group(3).strip()
                    note_raw = rm4.group(4).strip()
                elif rm3:
                    vr_id = int(rm3.group(1))
                    ref = rm3.group(2).strip()
                    term_str = ""
                    note_raw = rm3.group(3).strip()
                else:
                    if line.strip() == "":
                        in_table = False
                        seen_header = False
                    i += 1
                    continue

                is_anchor = bool(ANCHOR_MARKER_RE.search(note_raw))
                note_clean = ANCHOR_MARKER_RE.sub("", note_raw).strip()
                term_parts = term_str.split(maxsplit=1) if term_str else []
                strong = term_parts[0] if term_parts else ""
                cur_group["verses"].append({
                    "vr_id": vr_id,
                    "reference": ref,
                    "strong": strong,
                    "term_str": term_str,
                    "is_anchor": is_anchor,
                    "analysis_note": note_clean,
                })
                i += 1
                continue

        i += 1

    if cur_group:
        groups.append(cur_group)

    return {
        "path": path,
        "n_groups": len(groups),
        "groups": groups,
    }


EXISTING_CODE_RE = re.compile(
    r"existing\s+code(?:s)?\s+(\d+)(?:[\s,]+(?:and\s+)?(\d+))?",
    re.IGNORECASE,
)


def extract_existing_codes_from_status(status_raw: str | None) -> list[int]:
    """Pull integer existing-codes out of a status_raw line."""
    if not status_raw:
        return []
    out = []
    # Find all "code NNNN" mentions
    for m in re.finditer(r"\bcode(?:s)?\s+([\d,\s]+?)(?:\s+(?:and|—|-|\(|\)|$))", status_raw, re.IGNORECASE):
        chunk = m.group(1)
        for n in re.findall(r"\d+", chunk):
            try:
                out.append(int(n))
            except ValueError:
                pass
    # Also find bare 4-digit numbers in status (e.g. "2475")
    for n in re.findall(r"\b(\d{3,5})\b", status_raw):
        try:
            v = int(n)
            if v not in out:
                out.append(v)
        except ValueError:
            pass
    return out


def categorise_status(status_raw: str | None,
                      heading_existing_code: int | None = None) -> str:
    """Return canonical status: NEW / RETAINED / RETAINED_REFINED / OTHER."""
    if not status_raw:
        # F/G docs omit Status line. If heading has an existing code,
        # treat as RETAINED.
        if heading_existing_code is not None:
            return "RETAINED"
        return "UNKNOWN"
    s = status_raw.upper()
    if "RETAINED AND REFINED" in s or "RETAINED & REFINED" in s:
        return "RETAINED_REFINED"
    if "NEW GROUP" in s or s.startswith("NEW") or "NEW " in s:
        return "NEW"
    if "RETAINED" in s:
        return "RETAINED"
    return "OTHER"


# ── Plan generation ──────────────────────────────────────────────────

def cluster_subgroup_id(conn, sub_letter: str) -> int:
    r = conn.execute(
        "SELECT id FROM cluster_subgroup "
        " WHERE cluster_code='M15' AND subgroup_code=? "
        "   AND COALESCE(delete_flagged,0)=0",
        (f"M15-{sub_letter}",),
    ).fetchone()
    if not r:
        raise RuntimeError(f"M15-{sub_letter} cluster_subgroup not found")
    return r[0]


def existing_db_group_for_term_set(conn, vr_ids: list[int]) -> dict[int, dict]:
    """For each vr_id, find its current verse_context row + group info."""
    if not vr_ids:
        return {}
    placeholders = ",".join("?" * len(vr_ids))
    out: dict[int, dict] = {}
    for r in conn.execute(
        f"SELECT vc.id AS vc_id, vc.verse_record_id AS vr_id, "
        f"       vc.mti_term_id, vc.group_id, vc.is_anchor, vc.is_relevant, "
        f"       vc.set_aside_reason, vc.notes, vc.analysis_note, "
        f"       vcg.group_code, vcg.context_description "
        f"  FROM verse_context vc "
        f"  LEFT JOIN verse_context_group vcg ON vcg.id=vc.group_id "
        f"   AND COALESCE(vcg.delete_flagged,0)=0 "
        f" WHERE vc.verse_record_id IN ({placeholders}) "
        f"   AND COALESCE(vc.delete_flagged,0)=0",
        tuple(vr_ids),
    ):
        out[r["vr_id"]] = dict(r)
    return out


def parse_directive_scope(directive_path: str) -> dict:
    """Pull existing groups in scope + flags from directive markdown."""
    text = Path(directive_path).read_text(encoding="utf-8")
    out = {"groups_in_scope": [], "raw": text}
    # Look for "Groups in scope:" line
    m = re.search(r"Groups in scope:?\s*([^\n]+)", text, re.IGNORECASE)
    if m:
        ids = re.findall(r"\b(\d{2,5})\b", m.group(1))
        out["groups_in_scope"] = [int(x) for x in ids]
    return out


def build_plan(conn, sub_letter: str, directive_filename: str,
               mapping_filename: str) -> dict:
    """Parse directive + mapping doc; resolve DB group IDs; build plan."""
    sg_id = cluster_subgroup_id(conn, sub_letter)
    directive_path = os.path.join(PHASE7_DIR, directive_filename)
    mapping_path = os.path.join(PHASE7_DIR, mapping_filename)
    directive = parse_directive_scope(directive_path)
    parsed = parse_mapping_doc(mapping_path)

    # Collect all vr_ids touched
    vr_ids = []
    for g in parsed["groups"]:
        for v in g["verses"]:
            vr_ids.append(v["vr_id"])
    vc_state = existing_db_group_for_term_set(conn, vr_ids)

    # For each parsed group, decide DB action
    actions = []
    for g in parsed["groups"]:
        cat = categorise_status(g["status_raw"], g.get("heading_existing_code"))
        # Determine candidate existing group_id by majority of verses
        from collections import Counter
        gid_counts = Counter()
        anchor_vr_id = None
        for v in g["verses"]:
            vc = vc_state.get(v["vr_id"])
            if vc and vc["group_id"]:
                gid_counts[vc["group_id"]] += 1
            if v["is_anchor"]:
                anchor_vr_id = v["vr_id"]

        # Pick existing_group_id heuristic: most-common current group_id
        # within directive's groups_in_scope
        in_scope = set(directive["groups_in_scope"])
        candidates = [(gid, c) for gid, c in gid_counts.most_common()
                      if gid in in_scope]
        existing_gid = candidates[0][0] if candidates else None

        # Heading-declared existing code beats heuristic
        heading_gid = g.get("heading_existing_code")
        status_codes = extract_existing_codes_from_status(g.get("status_raw"))
        if heading_gid:
            existing_gid = heading_gid
        elif status_codes:
            # Pick first declared code; verify it exists in DB
            for sc in status_codes:
                r = conn.execute(
                    "SELECT id FROM verse_context_group WHERE id=? "
                    "  AND COALESCE(delete_flagged,0)=0",
                    (sc,),
                ).fetchone()
                if r:
                    existing_gid = sc
                    break

        actions.append({
            "code": g["code"],
            "title": g["title"],
            "status_raw": g["status_raw"],
            "category": cat,
            "description": g["description"],
            "anchor_raw": g["anchor_raw"],
            "anchor_vr_id": anchor_vr_id,
            "n_verses": len(g["verses"]),
            "heading_existing_code": heading_gid,
            "existing_group_id_candidate": existing_gid,
            "current_group_distribution": dict(gid_counts),
            "verses": g["verses"],
        })

    return {
        "subgroup_letter": sub_letter,
        "subgroup_id": sg_id,
        "directive_filename": directive_filename,
        "mapping_filename": mapping_filename,
        "groups_in_scope": directive["groups_in_scope"],
        "n_groups_parsed": parsed["n_groups"],
        "actions": actions,
    }


def print_plan(plan: dict, verbose: bool = False) -> None:
    print(f"=== M15-{plan['subgroup_letter']} plan ({plan['directive_filename']}) ===")
    print(f"  Sub-group id: {plan['subgroup_id']}")
    print(f"  Mapping: {plan['mapping_filename']}")
    print(f"  Directive groups_in_scope: {plan['groups_in_scope']}")
    print(f"  Parsed groups: {plan['n_groups_parsed']}")
    n_verses_total = sum(a["n_verses"] for a in plan["actions"])
    print(f"  Verses total: {n_verses_total}")
    print()
    print(f"  {'Code':>5}  {'Cat':18s}  {'#vrs':>4}  {'anchor_vr':>9}  "
          f"{'cand_gid':>9}  status_raw")
    for a in plan["actions"]:
        print(f"  {a['code']:>5}  {a['category']:18s}  "
              f"{a['n_verses']:4d}  "
              f"{a['anchor_vr_id'] or '-':>9}  "
              f"{a['existing_group_id_candidate'] or '-':>9}  "
              f"{(a['status_raw'] or '?')[:60]}")
        if verbose and a["current_group_distribution"]:
            for gid, n in a["current_group_distribution"].items():
                print(f"        currently in DB group {gid}: {n} verse(s)")
    print()


def now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def next_group_code_for_term(conn, mti_term_id: int) -> str:
    """Generate next sequential group_code like '<mti>-NNN'."""
    r = conn.execute(
        "SELECT group_code FROM verse_context_group "
        " WHERE mti_term_id=? ORDER BY id", (mti_term_id,)
    ).fetchall()
    max_n = 0
    for row in r:
        gc = row[0] or ""
        m = re.match(rf"^{mti_term_id}-(\d+)$", gc)
        if m:
            max_n = max(max_n, int(m.group(1)))
    return f"{mti_term_id}-{max_n + 1:03d}"


def apply_plan(conn, plan: dict, dry_run: bool = False) -> dict:
    """Apply one sub-group's plan in a single transaction.

    Returns counts dict.
    """
    counts = {
        "groups_inserted": 0,
        "groups_updated": 0,
        "vc_updated": 0,
        "anchors_set": 0,
        "anchors_cleared": 0,
        "skipped_missing_vc": 0,
    }

    cur = conn.cursor()
    ts = now_iso()
    sub_letter = plan["subgroup_letter"]

    cur.execute("BEGIN")
    try:
        for action in plan["actions"]:
            if not action["verses"]:
                # No verses to apply — skip
                continue

            # Resolve / create the DB group_id
            cat = action["category"]
            existing_gid = action["existing_group_id_candidate"]
            new_desc = action["description"] or action["title"]

            if cat == "NEW":
                # Create new group; mti_term_id from the most-common term
                # among this group's verses
                from collections import Counter
                term_counter = Counter()
                for v in action["verses"]:
                    # Look up mti_term_id from verse_context (current state)
                    vc = cur.execute(
                        "SELECT mti_term_id FROM verse_context "
                        " WHERE verse_record_id=? "
                        "   AND COALESCE(delete_flagged,0)=0 LIMIT 1",
                        (v["vr_id"],),
                    ).fetchone()
                    if vc:
                        term_counter[vc["mti_term_id"]] += 1
                if not term_counter:
                    raise RuntimeError(
                        f"NEW group {action['code']} has no resolvable "
                        f"mti_term_id from any verse"
                    )
                primary_mti = term_counter.most_common(1)[0][0]
                new_code = next_group_code_for_term(conn, primary_mti)

                cur.execute(
                    "INSERT INTO verse_context_group "
                    "  (mti_term_id, group_code, context_description, "
                    "   notes, delete_flagged) "
                    "VALUES (?, ?, ?, ?, 0)",
                    (primary_mti, new_code, new_desc,
                     f"Created by M15 Phase 7 (sub-group {sub_letter}, "
                     f"analytical code {action['code']})"),
                )
                action["resolved_group_id"] = cur.lastrowid
                counts["groups_inserted"] += 1
                print(f"  + verse_context_group INSERT {new_code} "
                      f"(mti={primary_mti}) -> id={action['resolved_group_id']}")
            elif cat in ("RETAINED", "RETAINED_REFINED"):
                if not existing_gid:
                    raise RuntimeError(
                        f"{cat} group {action['code']} has no existing "
                        f"group_id resolved"
                    )
                action["resolved_group_id"] = existing_gid
                # Update description for RETAINED_REFINED
                if cat == "RETAINED_REFINED":
                    cur.execute(
                        "UPDATE verse_context_group "
                        "   SET context_description=? "
                        " WHERE id=?",
                        (new_desc, existing_gid),
                    )
                    counts["groups_updated"] += 1
            else:
                raise RuntimeError(
                    f"Group {action['code']} category={cat} unsupported"
                )

            # For each verse: UPDATE verse_context
            anchor_set_for_group = False
            for v in action["verses"]:
                # Match by (verse_record_id, mti_term_id) — need mti_id
                # from current vc row
                vc = cur.execute(
                    "SELECT id, mti_term_id FROM verse_context "
                    " WHERE verse_record_id=? "
                    "   AND COALESCE(delete_flagged,0)=0",
                    (v["vr_id"],),
                ).fetchone()
                if not vc:
                    counts["skipped_missing_vc"] += 1
                    continue
                rc = cur.execute(
                    "UPDATE verse_context "
                    "   SET group_id=?, "
                    "       analysis_note=COALESCE(NULLIF(?, ''), analysis_note), "
                    "       is_anchor=? "
                    " WHERE id=?",
                    (action["resolved_group_id"], v["analysis_note"],
                     1 if v["is_anchor"] else 0, vc["id"]),
                ).rowcount
                if rc:
                    counts["vc_updated"] += 1
                if v["is_anchor"]:
                    counts["anchors_set"] += 1
                    anchor_set_for_group = True

            # Ensure exactly one anchor per group: if no anchor was
            # explicitly designated, leave existing anchors alone.
            # If any anchor WAS designated, clear other anchors in the group.
            if anchor_set_for_group:
                rc = cur.execute(
                    "UPDATE verse_context "
                    "   SET is_anchor=0 "
                    " WHERE group_id=? AND is_anchor=1 "
                    "   AND verse_record_id NOT IN ({}) "
                    "   AND COALESCE(delete_flagged,0)=0".format(
                        ",".join("?" * len([v for v in action["verses"]
                                            if v["is_anchor"]]))
                    ),
                    (action["resolved_group_id"],
                     *[v["vr_id"] for v in action["verses"] if v["is_anchor"]]),
                ).rowcount
                counts["anchors_cleared"] += rc

        if dry_run:
            cur.execute("ROLLBACK")
            counts["_dry_run_rolled_back"] = True
        else:
            cur.execute("COMMIT")
    except Exception as e:
        cur.execute("ROLLBACK")
        raise

    return counts


def main():
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

    ap = argparse.ArgumentParser()
    ap.add_argument("--plan", action="store_true",
                    help="Parse and show plan; no DB writes")
    ap.add_argument("--apply", default=None,
                    help="Apply one sub-group (A..G)")
    ap.add_argument("--apply-all", action="store_true",
                    help="Apply all 7 sub-groups in sequence")
    ap.add_argument("--apply-dry-run", action="store_true",
                    help="Run apply logic but ROLLBACK at end (validates SQL)")
    ap.add_argument("--subgroup", default=None,
                    help="Only one sub-group (A..G); default all")
    ap.add_argument("--verbose", action="store_true")
    args = ap.parse_args()

    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row

    if args.apply:
        targets = [d for d in DIRECTIVES if d[0] == args.apply.upper()]
        if not targets:
            print(f"Sub-group {args.apply} not in directive list")
            return 2
    elif args.apply_all:
        targets = DIRECTIVES
    elif args.subgroup:
        targets = [d for d in DIRECTIVES if d[0] == args.subgroup.upper()]
        if not targets:
            print(f"Sub-group {args.subgroup} not in directive list")
            return 2
    else:
        targets = DIRECTIVES

    if args.plan or (not args.apply and not args.apply_all):
        for sub_letter, dir_fn, map_fn in targets:
            plan = build_plan(conn, sub_letter, dir_fn, map_fn)
            print_plan(plan, verbose=args.verbose)
        conn.close()
        return 0

    # Apply mode
    summary = []
    for sub_letter, dir_fn, map_fn in targets:
        print()
        print("=" * 65)
        print(f"  APPLYING M15-{sub_letter}  ({dir_fn})")
        print("=" * 65)
        plan = build_plan(conn, sub_letter, dir_fn, map_fn)
        print_plan(plan, verbose=False)
        try:
            counts = apply_plan(conn, plan, dry_run=args.apply_dry_run)
        except Exception as e:
            print(f"  [HALT] {sub_letter}: {type(e).__name__}: {e}")
            print("  Stopping cascade — earlier sub-groups already committed.")
            break
        summary.append((sub_letter, counts))
        print()
        print(f"  M15-{sub_letter} applied:")
        for k, v in counts.items():
            print(f"    {k:30s} {v}")

    print()
    print("=" * 65)
    print("  CASCADE SUMMARY")
    print("=" * 65)
    print(f"  {'Sub':3s} {'+grps':>6} {'~grps':>6} {'~vc':>5} "
          f"{'+anc':>5} {'-anc':>5} {'skip':>5}")
    for sub_letter, counts in summary:
        print(f"  M15-{sub_letter:1s} "
              f"{counts.get('groups_inserted',0):>6d} "
              f"{counts.get('groups_updated',0):>6d} "
              f"{counts.get('vc_updated',0):>5d} "
              f"{counts.get('anchors_set',0):>5d} "
              f"{counts.get('anchors_cleared',0):>5d} "
              f"{counts.get('skipped_missing_vc',0):>5d}")
    conn.close()
    return 0


if __name__ == "__main__":
    sys.exit(main())
