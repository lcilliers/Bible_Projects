"""_apply_m26_dir001_findings_v1_20260511.py — DB-modifying.

Apply DIR-20260511-M26-001: Phase 8 findings record load.

Parses four consolidated findings markdown files and inserts cluster_finding
rows for cluster M26 (one row per authored (question_code x scope) cell,
following the M06 precedent — authored-only, no stub rows).

Special-section handling:
  - Part 4 '## M26-BOUNDARY ...' section -> 1 row at obs_id=236 (T1.1.1),
    sg=M26-BOUNDARY, status='finding'.
  - Part 4 '## Cross-Sub-Group Review Pass' section -> 9 rows mapped to
    pre-approved obs_ids, status='cluster_synthesis', sg=NULL.

Qualification entries (directive §"Qualification entries") are appended to
the matching primary cell text rather than creating duplicate rows
(unique constraint is (obs_id, cluster_code, cluster_subgroup_id, version)).

Usage:
  python scripts/_apply_m26_dir001_findings_v1_20260511.py --dry-run
  python scripts/_apply_m26_dir001_findings_v1_20260511.py --live
"""
from __future__ import annotations

import argparse
import os
import re
import shutil
import sqlite3
import sys
from collections import defaultdict
from dataclasses import dataclass
from datetime import datetime, timezone

DB_PATH = os.path.join("database", "bible_research.db")
BACKUP_DIR = "backups"
PHASE8_DIR = os.path.join(
    "archive", "Sessions", "Session_Clusters", "M26", "files phase 8"
)

PART_FILES = [
    "WA-M26-consolidated-findings-v1-20260510-part1.md",
    "WA-M26-consolidated-findings-v1-20260510-part2-T2.md",
    "WA-M26-consolidated-findings-v1-20260510-part3-T3-T4.md",
    "WA-M26-consolidated-findings-v1-20260510-part4-T5-T7.md",
]

CLUSTER_CODE = "M26"
VERSION = "v1"
DIRECTIVE_ID = "DIR-20260511-M26-001"
OBSLOG_REF = "WA-obslog-M26-phase8-catalogue-v1-20260510.md"

# Maps the scope label after '[' to internal key. Sub-group labels come from
# the consolidated findings files; the second half after the em-dash is the
# sub-group title.
SCOPE_KEY_BY_LABEL = {
    "A1": "A1",
    "A2": "A2",
    "B": "B",
    "C": "C",
    "D": "D",
    "E": "E",
    "F": "F",
    "G": "G",
}

# Sub-group code lookup (resolved at runtime from cluster_subgroup table).
# All entries below are filled in main() before parsing.
SUBGROUP_ID_BY_KEY: dict[str, int] = {}

# Cross-cluster findings -> obs_id mapping (researcher-approved 2026-05-11).
# Each tuple: (finding_number, question_code, obs_id_resolved_later, scope='CLUSTER')
CROSS_CLUSTER_QCODES = {
    1: "T2.1.1",   # Complete silence at spirit level
    2: "T2.3.1",   # Heart as primary constitutional location
    3: "T1.2.1",   # Governing state, not peer
    4: "T3.9.1",   # Conscience as primary judicial faculty
    5: "T6.3.1",   # F as inner appropriation mechanism for C
    6: "T2.9.1",   # Origin asymmetry
    7: "T5.6.1",   # Pervasive eschatological orientation
    8: "T6.5.1",   # A2/C tension (Ezekiel vs NT security)
    9: "T7.1.8",   # OT implicit / NT explicit (single finding, two focal lengths)
}

BOUNDARY_NOTE_QCODE = "T1.1.1"  # researcher-approved single mapping


@dataclass
class Cell:
    qcode: str
    scope_key: str  # A1..G, CLUSTER, BOUNDARY, A2_QUAL, NOTE_BIDIR
    status: str | None  # 'finding' | 'silent' | 'gap' | 'cluster_synthesis' | None
    text: str
    source_file: str


_QHEADER_RE = re.compile(r"^\*\*(T\d+\.\d+\.\d+)\*\*")
_MARKER_RE = re.compile(r"^\*\*\[(.+?)\]\*\*\s*(.*)$")

# Canonical scope labels — only these are treated as scope markers; everything
# else inside [..] is plain content (e.g. **[Eze 18:20]** comparison headers).
_SUBGROUP_LABELS = {
    "A1": "God Righteousness",
    "A2": "Human Righteousness",
    "B": "Moral Uprightness",
    "C": "Justification",
    "D": "Avenging Justice",
    "E": "Condemnation",
    "F": "Moral Reckoning",
    "G": "Structural Opposites",
}


def parse_scope(scope_raw: str) -> tuple[str, str | None] | None:
    """Return (scope_key, status_override) or None if the marker is content
    rather than a scope. status_override is None unless the marker itself
    dictates a status (e.g. CLUSTER → cluster_synthesis).
    """
    s = scope_raw.strip()
    # CLUSTER variants
    if s == "CLUSTER" or s.startswith("CLUSTER —") or s.startswith("CLUSTER -"):
        return "CLUSTER", "cluster_synthesis"
    if s == "BOUNDARY" or s.startswith("BOUNDARY —"):
        return "BOUNDARY", "finding"
    # Bidirectionality note (T2.10.2 — appended to CLUSTER)
    if s.startswith("Note on bidirectionality"):
        return "NOTE_BIDIR", None
    # Sub-group scope markers — strict: must start with one of A1/A2/B..G
    # followed by ' — <expected label>' (em-dash or hyphen).
    for key, label_prefix in _SUBGROUP_LABELS.items():
        # Match "<key> — <label or qualification>"
        if re.match(rf"^{re.escape(key)}\s*[—-]\s*", s):
            tail = re.sub(rf"^{re.escape(key)}\s*[—-]\s*", "", s)
            if tail.lower().startswith("qualification"):
                return f"{key}_QUAL", None
            # Be permissive: any tail is accepted as a scope marker so long as
            # the key matches. The expected labels above are listed only for
            # reference; in practice the directive guarantees scope identity
            # via the leading key.
            return key, None
    # Plain '[A1]' (no label) — accept as scope too
    if s in _SUBGROUP_LABELS:
        return s, None
    # Otherwise: this is content, not a scope (e.g. [Eze 18:20], [logizomai])
    return None


def parse_status_letter(rest: str) -> tuple[str | None, str]:
    """rest is text immediately after '**[...]**'.
    Detect 'E.', 'S.', 'E —', 'S —', or 'G —' at start (period or em-dash
    continuation forms). Em-dash and hyphen both accepted.
    Returns (status_or_None, cleaned_rest).
    """
    r = rest.lstrip()
    # Letter + '.' form
    if r.startswith("E. ") or r == "E.":
        return "finding", r[2:].lstrip()
    if r.startswith("S. ") or r == "S.":
        return "silent", r[2:].lstrip()
    # Letter + em-dash form (em-dash —, en-dash –, or hyphen -)
    for sep in ("— ", "– ", "- "):
        if r.startswith(f"E {sep}"):
            return "finding", r[2 + len(sep):].lstrip()
        if r.startswith(f"S {sep}"):
            return "silent", r[2 + len(sep):].lstrip()
        if r.startswith(f"G {sep}"):
            return "gap", r[2 + len(sep):].lstrip()
    # Bare letter at start of line followed by nothing
    if r in ("E", "S", "G"):
        return {"E": "finding", "S": "silent", "G": "gap"}[r], ""
    # No letter detected — substantive-silence notes consistently open with
    # "No <...>" or "Not <...>". The directive's source markdown uses these
    # as silence-bodies where the author skipped the leading 'S —' letter.
    lc = r[:80].lower()
    if lc.startswith("no ") or lc.startswith("not "):
        return "silent", r
    return None, r


def parse_question_section(path: str) -> list[Cell]:
    """Parse one source file; return list of Cell rows (pre-merge).
    Stops at top-level '## ' headers (e.g. ## M26-BOUNDARY, ## Cross-Sub-Group).
    """
    cells: list[Cell] = []
    src_name = os.path.basename(path)
    with open(path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    current_q: str | None = None
    current_cell: Cell | None = None
    buf: list[str] = []
    in_special_section = False

    def flush():
        nonlocal current_cell, buf
        if current_cell is not None:
            text = "\n".join(buf).rstrip()
            current_cell.text = text
            cells.append(current_cell)
        current_cell = None
        buf = []

    for raw in lines:
        line = raw.rstrip("\n")
        # Detect top-level boundary/cross-sub-group section start
        if line.startswith("## M26-BOUNDARY") or line.startswith("## Cross-Sub-Group"):
            flush()
            in_special_section = True
            continue
        if in_special_section:
            # Skip — handled by separate parser
            continue
        if line.strip() == "---":
            flush()
            continue
        m = _QHEADER_RE.match(line)
        if m:
            flush()
            current_q = m.group(1)
            continue
        m = _MARKER_RE.match(line)
        if m and current_q is not None:
            scope_raw, rest = m.group(1), m.group(2)
            parsed = parse_scope(scope_raw)
            if parsed is None:
                # Content-level [..] marker (e.g. [Eze 18:20]) — treat as
                # continuation of the current cell, do NOT flush.
                if current_cell is not None:
                    buf.append(line)
                continue
            flush()
            scope_key, override = parsed
            status: str | None
            cleaned: str
            if override == "cluster_synthesis":
                status = "cluster_synthesis"
                # CLUSTER blocks may still have E./S./G — letter; preserve in body.
                cleaned = rest
            elif override == "finding":
                status = "finding"
                cleaned = rest
            elif scope_key.endswith("_QUAL") or scope_key == "NOTE_BIDIR":
                status = None  # qualification — append-only
                cleaned = rest
            else:
                status, cleaned = parse_status_letter(rest)
            current_cell = Cell(
                qcode=current_q,
                scope_key=scope_key,
                status=status,
                text="",  # filled by flush
                source_file=src_name,
            )
            buf = [f"**[{scope_raw}]** {cleaned}".rstrip()]
            continue
        # Continuation line
        if current_cell is not None:
            buf.append(line)
        # Otherwise skip (preamble / blank line outside any cell)
    flush()
    return cells


def parse_boundary_section(path: str) -> str:
    """Return the verbatim text of the M26-BOUNDARY structural characterisation
    section (used for the single BOUNDARY row).
    """
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()
    m = re.search(
        r"## M26-BOUNDARY — Structural Characterisation Note\s*\n(.*?)\n##\s",
        text,
        re.DOTALL,
    )
    if not m:
        m = re.search(
            r"## M26-BOUNDARY — Structural Characterisation Note\s*\n(.*?)\Z",
            text,
            re.DOTALL,
        )
    if not m:
        return ""
    return m.group(1).strip()


def parse_cross_cluster_section(path: str) -> dict[int, str]:
    """Return {finding_number: text} for the 9 cross-cluster findings."""
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()
    m = re.search(r"## Cross-Sub-Group Review Pass\s*\n(.*?)\Z", text, re.DOTALL)
    if not m:
        return {}
    section = m.group(1)
    findings: dict[int, str] = {}
    # Each finding starts with **Cross-cluster finding N —
    pattern = re.compile(
        r"\*\*Cross-cluster finding (\d+) — .*?\*\*(.*?)(?=\n\*\*Cross-cluster finding |\Z)",
        re.DOTALL,
    )
    for m2 in pattern.finditer(section):
        n = int(m2.group(1))
        body = m2.group(2).strip()
        # Reattach the heading line so context is preserved
        heading_line = section[m2.start():m2.start() + len(m2.group(0))].split("\n", 1)[0]
        findings[n] = (heading_line + "\n" + body).strip()
    return findings


def merge_qualifications(cells: list[Cell]) -> list[Cell]:
    """Append <key>_QUAL rows into the <key> row of the same qcode, and
    NOTE_BIDIR rows into the CLUSTER row of the same qcode.
    """
    by_key: dict[tuple[str, str], Cell] = {}
    extras_subgroup: dict[tuple[str, str], list[Cell]] = defaultdict(list)
    extras_cluster: dict[str, list[Cell]] = defaultdict(list)
    for c in cells:
        if c.scope_key.endswith("_QUAL"):
            base = c.scope_key[:-len("_QUAL")]
            extras_subgroup[(c.qcode, base)].append(c)
            continue
        if c.scope_key == "NOTE_BIDIR":
            extras_cluster[c.qcode].append(c)
            continue
        by_key[(c.qcode, c.scope_key)] = c

    # Merge qualification append-ons
    for (qcode, base), lst in extras_subgroup.items():
        primary = by_key.get((qcode, base))
        appended = "\n\n".join(x.text for x in lst)
        if primary is not None:
            primary.text = primary.text.rstrip() + "\n\n" + appended
        else:
            by_key[(qcode, base)] = Cell(
                qcode=qcode,
                scope_key=base,
                status="finding",
                text=appended,
                source_file=lst[0].source_file,
            )
    for qcode, lst in extras_cluster.items():
        primary = by_key.get((qcode, "CLUSTER"))
        appended = "\n\n".join(x.text for x in lst)
        if primary is not None:
            primary.text = primary.text.rstrip() + "\n\n" + appended
        else:
            by_key[(qcode, "CLUSTER")] = Cell(
                qcode=qcode,
                scope_key="CLUSTER",
                status="cluster_synthesis",
                text=appended,
                source_file=lst[0].source_file,
            )

    # Stable order: by qcode then by canonical scope order
    order = ["A1", "A2", "B", "C", "D", "E", "F", "G", "CLUSTER", "BOUNDARY"]
    out = sorted(
        by_key.values(),
        key=lambda c: (c.qcode, order.index(c.scope_key) if c.scope_key in order else 99),
    )
    return out


def now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def today_compact() -> str:
    return datetime.now(timezone.utc).strftime("%Y%m%d")


def take_backup(label: str) -> str:
    os.makedirs(BACKUP_DIR, exist_ok=True)
    p = os.path.join(BACKUP_DIR, f"bible_research_pre_{label}_{today_compact()}.db")
    shutil.copy2(DB_PATH, p)
    return p


def resolve_obs_ids(conn: sqlite3.Connection, qcodes: set[str]) -> dict[str, int]:
    """Map qcode -> obs_id; raises ValueError on any unresolved."""
    out: dict[str, int] = {}
    rows = conn.execute(
        f"""SELECT obs_id, question_code FROM wa_obs_question_catalogue
             WHERE question_code IN ({",".join("?" * len(qcodes))})""",
        list(qcodes),
    ).fetchall()
    for r in rows:
        out[r[1]] = r[0]
    missing = qcodes - set(out)
    if missing:
        raise ValueError(f"unresolved question_codes: {sorted(missing)}")
    return out


def main() -> int:
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--live", action="store_true")
    args = ap.parse_args()
    if not args.dry_run and not args.live:
        print("ERROR: must pass --dry-run or --live", file=sys.stderr)
        return 2

    print("=" * 72)
    print(f"{DIRECTIVE_ID} apply (M26 cluster_finding load)")
    print(f"  Mode: {'DRY-RUN' if args.dry_run else 'LIVE'}")
    print("=" * 72)
    print()

    # Phase 1 — parse source files
    print("PARSE")
    print("-" * 72)
    all_cells: list[Cell] = []
    for fn in PART_FILES:
        path = os.path.join(PHASE8_DIR, fn)
        if not os.path.exists(path):
            print(f"  [ERR] missing: {path}")
            return 1
        cells = parse_question_section(path)
        print(f"  {fn}: {len(cells)} cells")
        all_cells.extend(cells)

    # Part 4 special sections
    part4_path = os.path.join(PHASE8_DIR, PART_FILES[-1])
    boundary_text = parse_boundary_section(part4_path)
    cross_cluster = parse_cross_cluster_section(part4_path)
    print(f"  BOUNDARY section: {len(boundary_text)} chars")
    print(f"  Cross-cluster findings parsed: {len(cross_cluster)} (expected 9)")
    if len(cross_cluster) != 9:
        print(f"  [ERR] expected 9 cross-cluster findings, got {len(cross_cluster)}")
        return 1

    # Merge qualification entries
    merged_cells = merge_qualifications(all_cells)
    print(f"  Cells after merging qualifications: {len(merged_cells)}")
    # Distribution
    by_scope: dict[str, int] = defaultdict(int)
    by_status: dict[str, int] = defaultdict(int)
    for c in merged_cells:
        by_scope[c.scope_key] += 1
        by_status[c.status or "(none)"] += 1
    print("  By scope:", dict(sorted(by_scope.items())))
    print("  By status:", dict(sorted(by_status.items())))

    # Collect all qcodes we need to resolve
    qcodes_needed: set[str] = {c.qcode for c in merged_cells}
    qcodes_needed.add(BOUNDARY_NOTE_QCODE)
    qcodes_needed.update(CROSS_CLUSTER_QCODES.values())

    # Phase 2 — open DB, resolve IDs, pre-flight checks
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")

    # baseline: existing M26 rows
    existing = conn.execute(
        "SELECT COUNT(*) FROM cluster_finding WHERE cluster_code=?",
        (CLUSTER_CODE,),
    ).fetchone()[0]
    if existing > 0:
        print(f"\n[ERR] cluster_finding already has {existing} rows for {CLUSTER_CODE}. "
              "Aborting; load expects empty baseline.")
        return 1

    # Resolve sub-group ids
    for r in conn.execute(
        "SELECT id, subgroup_code FROM cluster_subgroup "
        "WHERE cluster_code=? AND COALESCE(delete_flagged,0)=0",
        (CLUSTER_CODE,),
    ):
        code = r["subgroup_code"]
        if code.startswith("M26-"):
            key = code.replace("M26-", "")
            SUBGROUP_ID_BY_KEY[key] = r["id"]
    for key in ("A1", "A2", "B", "C", "D", "E", "F", "G", "BOUNDARY"):
        if key not in SUBGROUP_ID_BY_KEY:
            print(f"[ERR] missing M26 sub-group: {key}")
            return 1

    # Resolve obs_ids
    try:
        obs_by_qcode = resolve_obs_ids(conn, qcodes_needed)
    except ValueError as e:
        print(f"[ERR] {e}")
        return 1

    # Catalogue version (single row; choose v2-2026-04-29 if multiple match for T-codes)
    cv = conn.execute(
        "SELECT DISTINCT catalogue_version FROM wa_obs_question_catalogue "
        " WHERE question_code GLOB 'T[0-9]*'"
    ).fetchall()
    cv_names = [r[0] for r in cv]
    print(f"  catalogue_version(s) for T-codes: {cv_names}")

    # Phase 3 — build insert rows
    print()
    print("BUILD ROWS")
    print("-" * 72)
    ts = now_iso()
    notes_template = (
        f"{DIRECTIVE_ID} (full-text load {today_compact()[:4]}-{today_compact()[4:6]}-{today_compact()[6:]}); "
        f"source: {{src}}; obslog: {OBSLOG_REF}"
    )
    rows_to_insert: list[tuple] = []

    # 1. Per-cell rows (sub-group + CLUSTER)
    for c in merged_cells:
        if c.scope_key in ("A2_QUAL", "NOTE_BIDIR"):
            continue  # already merged
        sg_id: int | None
        if c.scope_key == "CLUSTER":
            sg_id = None
        elif c.scope_key == "BOUNDARY":
            sg_id = SUBGROUP_ID_BY_KEY["BOUNDARY"]
        else:
            sg_id = SUBGROUP_ID_BY_KEY[c.scope_key]
        status = c.status or "finding"  # default if not detected
        rows_to_insert.append((
            obs_by_qcode[c.qcode], CLUSTER_CODE, sg_id, status, c.text,
            c.source_file, VERSION,
            notes_template.format(src=c.source_file), 0, ts, ts,
        ))

    # 2. BOUNDARY structural-characterisation row
    if boundary_text:
        rows_to_insert.append((
            obs_by_qcode[BOUNDARY_NOTE_QCODE], CLUSTER_CODE,
            SUBGROUP_ID_BY_KEY["BOUNDARY"], "finding",
            boundary_text,
            PART_FILES[-1], VERSION,
            notes_template.format(src=PART_FILES[-1]) + " | BOUNDARY structural characterisation note",
            0, ts, ts,
        ))

    # 3. Cross-cluster synthesis rows
    # If a CLUSTER-scope row already exists in the payload for this obs_id,
    # append the cross-cluster finding to its text rather than creating a
    # duplicate (which would violate the unique constraint).
    obs_to_cluster_idx: dict[int, int] = {}
    for i, row in enumerate(rows_to_insert):
        if row[2] is None and row[3] == "cluster_synthesis":
            obs_to_cluster_idx[row[0]] = i
    appended_count = 0
    new_rows_count = 0
    for n, qcode in CROSS_CLUSTER_QCODES.items():
        text = cross_cluster.get(n)
        if not text:
            print(f"  [WARN] cross-cluster finding {n} missing from source")
            continue
        obs_id = obs_by_qcode[qcode]
        cc_note_suffix = (
            f" | Cross-cluster finding {n} appended "
            f"(researcher-approved obs_id mapping 2026-05-11)"
        )
        if obs_id in obs_to_cluster_idx:
            idx = obs_to_cluster_idx[obs_id]
            old = rows_to_insert[idx]
            new_text = old[4].rstrip() + "\n\n---\n\n" + text
            new_notes = old[7] + cc_note_suffix
            rows_to_insert[idx] = (
                old[0], old[1], old[2], old[3], new_text,
                old[5], old[6], new_notes, old[8], old[9], old[10],
            )
            appended_count += 1
        else:
            rows_to_insert.append((
                obs_id, CLUSTER_CODE, None, "cluster_synthesis",
                text,
                PART_FILES[-1], VERSION,
                notes_template.format(src=PART_FILES[-1])
                + f" | Cross-cluster finding {n} (researcher-approved obs_id mapping 2026-05-11)",
                0, ts, ts,
            ))
            new_rows_count += 1
    print(f"  Cross-cluster findings: {appended_count} appended to existing "
          f"CLUSTER row, {new_rows_count} added as new rows")

    print(f"  Rows ready to insert: {len(rows_to_insert)}")

    # Sanity: check no duplicate (obs_id, sg_id) within our payload
    seen: set[tuple] = set()
    dups: list[tuple] = []
    for row in rows_to_insert:
        key = (row[0], row[2])
        if key in seen:
            dups.append(key)
        seen.add(key)
    if dups:
        print(f"  [ERR] duplicate (obs_id, cluster_subgroup_id) pairs in payload: {dups[:10]}")
        return 1
    print("  [ok] no duplicate (obs_id, sg_id) pairs in payload")

    # Phase 4 — backup + write
    if args.live:
        b = take_backup("m26_dir001_findings")
        print(f"\nBackup: {b}")

    try:
        conn.execute("BEGIN")
        cur = conn.cursor()
        cur.executemany(
            """INSERT INTO cluster_finding
                 (obs_id, cluster_code, cluster_subgroup_id, finding_status,
                  finding_text, source_file, version, notes, delete_flagged,
                  created_at, last_updated_date)
               VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
            rows_to_insert,
        )
        # FK check
        fk = list(conn.execute("PRAGMA foreign_key_check"))
        if fk:
            raise RuntimeError(f"FK violations: {fk[:5]}")
        if args.dry_run:
            conn.execute("ROLLBACK")
        else:
            conn.execute("COMMIT")
    except Exception as e:
        conn.execute("ROLLBACK")
        print(f"\n[err] rolled back: {e}")
        raise

    # Phase 5 — verification queries
    print()
    print("VERIFICATION (after %s)" % ("ROLLBACK" if args.dry_run else "COMMIT"))
    print("-" * 72)
    # In dry-run nothing is persisted; the queries reflect prior state.
    # Re-run the same payload analysis from rows_to_insert.
    by_status_payload: dict[str, int] = defaultdict(int)
    by_scope_payload: dict[str, int] = defaultdict(int)
    for row in rows_to_insert:
        by_status_payload[row[3]] += 1
        sg_id = row[2]
        scope_label = "CLUSTER" if sg_id is None else (
            "M26-BOUNDARY" if sg_id == SUBGROUP_ID_BY_KEY["BOUNDARY"]
            else next((k for k, v in SUBGROUP_ID_BY_KEY.items() if v == sg_id), str(sg_id))
        )
        by_scope_payload[scope_label] += 1
    print("  Payload by status:")
    for k, v in sorted(by_status_payload.items()):
        print(f"    {k:25s} {v}")
    print("  Payload by scope:")
    for k, v in sorted(by_scope_payload.items()):
        print(f"    {k:25s} {v}")

    if args.live:
        # Re-query as committed
        print("\n  Live counts in cluster_finding for M26:")
        for r in conn.execute(
            """SELECT finding_status, COUNT(*) n FROM cluster_finding
                WHERE cluster_code=? GROUP BY finding_status""",
            (CLUSTER_CODE,),
        ):
            print(f"    {r[0]:25s} {r[1]}")
        for r in conn.execute(
            """SELECT COALESCE(cs.subgroup_code,'(CLUSTER)') AS sg, COUNT(*) n
                 FROM cluster_finding cf
                 LEFT JOIN cluster_subgroup cs ON cs.id=cf.cluster_subgroup_id
                WHERE cf.cluster_code=? GROUP BY sg ORDER BY sg""",
            (CLUSTER_CODE,),
        ):
            print(f"    {r[0]:25s} {r[1]}")

    conn.close()
    print()
    print("DONE.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
