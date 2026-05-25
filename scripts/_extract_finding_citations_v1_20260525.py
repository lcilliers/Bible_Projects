"""Extract structured citations from cluster_finding + cluster_observation prose.

Loads `finding_citation` (table created by M52). Three citation types:
  - verse      : canonical book abbr + chap:verse, ranges expanded to atomic verses
  - strongs    : H/G prefix + digits + optional sub-letter
  - cross_char : `CHAR-N` references mid-body, EXCLUDING the opening
                 `**[CHAR-N]**` scope marker on cluster_finding rows
                 (that marker declares the row's scope, not a citation)

cluster_observation rows are cluster-scope (no opening CHAR marker) —
all `CHAR-N` matches are citations.

Idempotent: on each run, deletes existing finding_citation rows whose
(source_table, source_id) pair falls within the scope of this run, then
re-inserts.

Default scope: cluster_code='M10'. Override with --cluster.
"""
from __future__ import annotations
import argparse, io, re, sqlite3, sys
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path

if sys.platform == "win32":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

REPO = Path(__file__).resolve().parent.parent
DB = REPO / "database" / "bible_research.db"
NOW = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

# --- patterns --------------------------------------------------------------
# Leading CHAR scope marker on cluster_finding bodies. Tolerate `**[CHAR-N]**`
# with or without trailing status letter/dash.
SCOPE_MARKER_RE = re.compile(r'^\*\*\[CHAR-(\d{1,3})\]\*\*\s*[A-Z]?\s*[–—\-]?\s*')

# Verse: book token (optional 1-3 prefix + space) + space + chap:verse[range]
# Verse range separators: en/em-dash, hyphen, comma, semicolon (NOT slash —
# slash is used for parallel-passage delimiters across chapters in some refs).
VERSE_RE = re.compile(
    r'(?<![A-Za-z])([1-3]?\s?[A-Z][a-z]{1,4})\s+'
    r'(\d{1,3}):(\d{1,3}(?:[–—\-,;]\s*\d{1,3})*)\b'
)

# Strong's: H or G + 1-5 digits, optional uppercase sub-letter.
STRONGS_RE = re.compile(r'(?<![A-Za-z0-9])([HG])(\d{1,5})([A-Z])?(?![A-Za-z0-9])')

# CHAR-N anywhere in the text.
CHAR_RE = re.compile(r'\bCHAR-(\d{1,3})\b')

# Book aliases observed in AI output that aren't the DB-canonical abbreviation.
EXTRA_ALIASES = {
    "1Jo": "1Jn", "2Jo": "2Jn", "3Jo": "3Jn",
    "Amos": "Amo", "Jhn": "Joh", "Ize": "Eze",
    "Song": "Sng", "SoS": "Sng", "Phil": "Phi",
    "Eccl": "Ecc",
}


def build_book_canon(conn: sqlite3.Connection) -> dict[str, str]:
    rows = conn.execute("SELECT abbreviation, short_code FROM books").fetchall()
    canon: dict[str, str] = {}
    for r in rows:
        ab = r["abbreviation"]
        if ab:
            canon[ab] = ab
        sc = r["short_code"]
        if sc and sc != ab:
            canon[sc] = ab
    canon.update(EXTRA_ALIASES)
    return canon


def expand_verse_range(spec: str) -> list[int]:
    """Expand a verse spec like '4', '4-5', '4,6', '4-6,8' into [4], [4,5], etc.

    Safety cap: ranges > 30 verses are collapsed to the lower bound only
    (defensive against parse errors). Returns deduped, sorted ascending.
    """
    out: list[int] = []
    for piece in re.split(r"[,;]", spec):
        piece = piece.strip()
        if not piece:
            continue
        m = re.match(r"(\d+)\s*[–—\-]\s*(\d+)$", piece)
        if m:
            a, b = int(m.group(1)), int(m.group(2))
            if a <= b and (b - a) <= 30:
                out.extend(range(a, b + 1))
            else:
                out.append(a)
        else:
            try:
                out.append(int(piece))
            except ValueError:
                pass
    return sorted(set(out))


def strip_scope_marker(text: str) -> tuple[str, int | None]:
    """Strip the leading `**[CHAR-N]**` scope marker if present.

    Returns (stripped_text, scope_char_n or None). The scope char itself is
    NOT recorded as a cross_char citation.
    """
    if not text:
        return "", None
    m = SCOPE_MARKER_RE.match(text)
    if m:
        return text[m.end():], int(m.group(1))
    return text, None


def extract_from(
    text: str,
    canon: dict[str, str],
    strip_opening_char: bool,
    scope_char_seq: int | None = None,
) -> list[tuple[str, str, int]]:
    """Return list of (citation_type, citation_value, position) tuples.

    `strip_opening_char` controls whether the leading `**[CHAR-N]**` marker
    is stripped (True for cluster_finding; False for cluster_observation).

    `scope_char_seq` is the char_seq for the current row (cluster_finding rows
    only). CHAR-N citations equal to this scope are filtered out as
    self-references — these are not useful cross-references but appear
    naturally in prose like "the CHAR-N corpus shows...".
    """
    if strip_opening_char:
        body, _opener_n = strip_scope_marker(text)
    else:
        body = text or ""

    out: list[tuple[str, str, int]] = []

    # --- verse refs ---
    for m in VERSE_RE.finditer(body):
        tok = re.sub(r"\s+", "", m.group(1))
        if tok not in canon:
            continue
        book = canon[tok]
        chapter = int(m.group(2))
        verses = expand_verse_range(m.group(3))
        if not verses:
            continue
        pos = m.start()
        for v in verses:
            out.append(("verse", f"{book} {chapter}:{v}", pos))

    # --- strongs ---
    for m in STRONGS_RE.finditer(body):
        code = f"{m.group(1)}{m.group(2)}" + (m.group(3) or "")
        out.append(("strongs", code, m.start()))

    # --- cross_char (exclude self-references) ---
    for m in CHAR_RE.finditer(body):
        n = int(m.group(1))
        if scope_char_seq is not None and n == scope_char_seq:
            continue
        out.append(("cross_char", f"CHAR-{n}", m.start()))

    return out


def fetch_rows(
    conn: sqlite3.Connection, cluster: str
) -> tuple[list[sqlite3.Row], list[sqlite3.Row]]:
    findings = conn.execute(
        """
        SELECT cf.id, cf.finding_text, c.char_seq
        FROM cluster_finding cf
        LEFT JOIN characteristic c ON c.id = cf.characteristic_id
        WHERE cf.cluster_code = ?
          AND COALESCE(cf.delete_flagged, 0) = 0
        """,
        (cluster,),
    ).fetchall()
    observations = conn.execute(
        """
        SELECT id, description
        FROM cluster_observation
        WHERE cluster_code = ?
          AND COALESCE(delete_flagged, 0) = 0
        """,
        (cluster,),
    ).fetchall()
    return findings, observations


def delete_existing(
    conn: sqlite3.Connection, source_table: str, source_ids: list[int]
) -> int:
    if not source_ids:
        return 0
    n = 0
    chunk = 900
    for i in range(0, len(source_ids), chunk):
        ids = source_ids[i:i + chunk]
        placeholders = ",".join(["?"] * len(ids))
        cur = conn.execute(
            f"DELETE FROM finding_citation WHERE source_table=? AND source_id IN ({placeholders})",
            (source_table, *ids),
        )
        n += cur.rowcount
    return n


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--cluster", default="M10")
    ap.add_argument("--live", action="store_true", help="Apply (default: dry-run)")
    args = ap.parse_args()
    cluster = args.cluster.strip()
    dry = not args.live

    print(f"=== finding_citation extraction — cluster={cluster} "
          f"mode={'DRY-RUN' if dry else 'LIVE'} ===")

    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row
    canon = build_book_canon(conn)

    findings, observations = fetch_rows(conn, cluster)
    print(f"cluster_finding rows: {len(findings)}")
    print(f"cluster_observation rows: {len(observations)}")
    print()

    # Extract
    rows_to_insert: list[tuple[str, int, str, str, int]] = []
    ctype_counter = Counter()
    per_table_counter = Counter()
    sample_per_type: dict[str, list[str]] = defaultdict(list)

    for r in findings:
        for ctype, cval, pos in extract_from(
            r["finding_text"] or "", canon,
            strip_opening_char=True,
            scope_char_seq=r["char_seq"],
        ):
            rows_to_insert.append(("cluster_finding", r["id"], ctype, cval, pos))
            ctype_counter[ctype] += 1
            per_table_counter[("cluster_finding", ctype)] += 1
            if len(sample_per_type[ctype]) < 5:
                sample_per_type[ctype].append(cval)

    for r in observations:
        for ctype, cval, pos in extract_from(
            r["description"] or "", canon, strip_opening_char=False
        ):
            rows_to_insert.append(("cluster_observation", r["id"], ctype, cval, pos))
            ctype_counter[ctype] += 1
            per_table_counter[("cluster_observation", ctype)] += 1
            if len(sample_per_type[ctype]) < 5:
                sample_per_type[ctype].append(cval)

    # Reporting
    print("--- Extracted totals ---")
    for ct in ("verse", "strongs", "cross_char"):
        print(f"  {ct:11s}: {ctype_counter[ct]}")
    print(f"  TOTAL      : {sum(ctype_counter.values())}")
    print()
    print("--- Per-source-table breakdown ---")
    for st in ("cluster_finding", "cluster_observation"):
        line = f"  {st:20s}"
        for ct in ("verse", "strongs", "cross_char"):
            line += f"  {ct}={per_table_counter[(st, ct)]:6d}"
        print(line)
    print()
    print("--- Samples ---")
    for ct in ("verse", "strongs", "cross_char"):
        print(f"  {ct}: {sample_per_type[ct][:5]}")
    print()

    # Top values per type
    top = defaultdict(Counter)
    for _st, _sid, ct, cv, _pos in rows_to_insert:
        top[ct][cv] += 1
    for ct in ("verse", "strongs", "cross_char"):
        print(f"--- Top 10 most-cited {ct} ---")
        for v, n in top[ct].most_common(10):
            print(f"  {v}: {n}")
        print()

    if dry:
        print("[DRY-RUN — no writes]")
        conn.close()
        return 0

    # LIVE — wipe existing rows for the affected source_ids, then insert
    finding_ids = [r["id"] for r in findings]
    obs_ids = [r["id"] for r in observations]
    print("--- Wiping prior rows for affected sources ---")
    cur = conn.cursor()
    cur.execute("BEGIN")
    try:
        n_del_f = delete_existing(conn, "cluster_finding", finding_ids)
        n_del_o = delete_existing(conn, "cluster_observation", obs_ids)
        print(f"  deleted cluster_finding citations:    {n_del_f}")
        print(f"  deleted cluster_observation citations: {n_del_o}")

        # Insert in batches
        ins_sql = (
            "INSERT INTO finding_citation "
            "(source_table, source_id, citation_type, citation_value, position, "
            "delete_flagged, created_at) "
            "VALUES (?, ?, ?, ?, ?, 0, ?)"
        )
        batch = []
        BATCH_SIZE = 500
        n_ins = 0
        for st, sid, ct, cv, pos in rows_to_insert:
            batch.append((st, sid, ct, cv, pos, NOW))
            if len(batch) >= BATCH_SIZE:
                cur.executemany(ins_sql, batch)
                n_ins += len(batch)
                batch.clear()
        if batch:
            cur.executemany(ins_sql, batch)
            n_ins += len(batch)

        conn.commit()
        print(f"  inserted: {n_ins}")
        print(f"COMMITTED")
    except Exception:
        conn.rollback()
        print("ROLLED BACK")
        raise
    finally:
        # Post-verify
        post = conn.execute(
            "SELECT COUNT(*) FROM finding_citation"
        ).fetchone()[0]
        print(f"  finding_citation total rows post: {post}")
        conn.close()

    return 0


if __name__ == "__main__":
    sys.exit(main())
