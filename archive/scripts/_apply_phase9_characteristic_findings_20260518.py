"""Phase 9 characteristic-findings loader.

Parses a per-characteristic findings markdown file
(`WA-{cluster}-phase9-char{N}-{short}-findings-v{V}-{date}.md`) and writes
189 rows to `cluster_finding` with:

    cluster_code           = <cluster_code>
    characteristic_id      = <id of the named characteristic>
    cluster_subgroup_id    = NULL  (characteristic-scope only)
    vcg_scope              = NULL  (not VCG-scoped)
    obs_id                 = derived from T#.#.# code via wa_obs_question_catalogue.question_code
    finding_status         = 'finding' (E) | 'silent' (S) | 'gap' (G)
    finding_text           = full body for the prompt
    source_file            = the findings .md path (relative to repo root)
    version                = parsed from filename or --version override

Strict expectations:
- Exactly 189 prompt blocks
- Each block opens with **T#.#.# — ...**
- Each block has exactly one outcome line **[CHAR-N]** {E|S|G} — ...
- The CHAR-N marker number must match --char-seq
- No SUB-/CLUSTER-/VCG-scope markers in the file

Usage:
    python scripts/_apply_phase9_characteristic_findings_20260518.py \
        --findings Sessions/Session_Clusters/M04/WA-M04-phase9-char1-Exultation-findings-v1-20260518.md \
        --cluster-code M04 --char-seq 1 [--dry-run]
"""
from __future__ import annotations

import argparse
import re
import sqlite3
import sys
from datetime import datetime, timezone
from pathlib import Path

DB_PATH = Path('database/bible_research.db')
NOW_UTC = datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')

PROMPT_HEADER_RE = re.compile(r'^\*\*(T\d+\.\d+\.\d+) —')
OUTCOME_LINE_RE = re.compile(r'^\*\*\[CHAR-(\d+)\]\*\* ([ESG]) — (.*)$', re.DOTALL)
FORBIDDEN_SCOPE_RE = re.compile(r'\*\*\[(SUB|CLUSTER|VCG)-')

OUTCOME_TO_STATUS = {'E': 'finding', 'S': 'silent', 'G': 'gap'}


def parse_findings_md(path: Path, expected_char_seq: int):
    """Yield (q_code, outcome, body_text) for each of the 189 prompts.

    Body text is the full multi-paragraph content from the outcome marker up
    to the next prompt header (or the Self-check section).
    """
    text = path.read_text(encoding='utf-8')

    # Hard-fail on forbidden scope markers
    forbidden = FORBIDDEN_SCOPE_RE.findall(text)
    if forbidden:
        raise SystemExit(
            f"FAIL: forbidden scope markers in findings file: {set(forbidden)}. "
            "Phase 9 char-scope output must use only **[CHAR-N]**."
        )

    # Split into prompt blocks by walking line-by-line so we keep order + body
    lines = text.splitlines()
    blocks = []  # list of {q_code, body_lines}
    current = None
    for ln in lines:
        m = PROMPT_HEADER_RE.match(ln)
        if m:
            if current is not None:
                blocks.append(current)
            current = {'q_code': m.group(1), 'header': ln, 'body_lines': []}
            continue
        # Stop bucketing once we hit the Self-check section
        if ln.startswith('## Self-check'):
            if current is not None:
                blocks.append(current)
                current = None
            break
        if current is not None:
            current['body_lines'].append(ln)
    if current is not None:
        blocks.append(current)

    if len(blocks) != 189:
        raise SystemExit(f"FAIL: expected 189 prompt blocks, got {len(blocks)}")

    # Verify each q_code is unique
    seen = set()
    for b in blocks:
        if b['q_code'] in seen:
            raise SystemExit(f"FAIL: duplicate q_code in findings: {b['q_code']}")
        seen.add(b['q_code'])

    # Extract outcome + body from each block
    parsed = []
    for b in blocks:
        body = '\n'.join(b['body_lines']).strip()
        # body starts with the outcome line:
        # **[CHAR-N]** {E|S|G} — finding text...
        # then optional continuation paragraphs until `---`
        # Trim trailing `---` separators
        body = re.sub(r'\n---\s*$', '', body).strip()
        # First non-empty paragraph must be the outcome line
        first_para_match = re.search(r'^(\*\*\[CHAR-\d+\]\*\* [ESG] — .*?)(?=\n\n|\Z)',
                                     body, re.DOTALL | re.MULTILINE)
        if not first_para_match:
            raise SystemExit(
                f"FAIL: {b['q_code']} body does not start with an outcome line. "
                f"First 200 chars: {body[:200]!r}"
            )
        outcome_para = first_para_match.group(1)
        m = OUTCOME_LINE_RE.match(outcome_para)
        if not m:
            raise SystemExit(
                f"FAIL: {b['q_code']} outcome paragraph not parseable: {outcome_para[:200]!r}"
            )
        char_seq_in_marker = int(m.group(1))
        outcome = m.group(2)
        if char_seq_in_marker != expected_char_seq:
            raise SystemExit(
                f"FAIL: {b['q_code']} has [CHAR-{char_seq_in_marker}] but expected "
                f"[CHAR-{expected_char_seq}]"
            )
        parsed.append({
            'q_code': b['q_code'],
            'outcome': outcome,
            'body': body,  # full body including outcome line — preserves continuation paragraphs
        })

    return parsed


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--findings', required=True, type=Path,
                    help='Path to per-characteristic findings .md file')
    ap.add_argument('--cluster-code', required=True,
                    help='Cluster code, e.g. M04')
    ap.add_argument('--char-seq', required=True, type=int,
                    help='Characteristic sequence number (1..N)')
    ap.add_argument('--version', default=None,
                    help='Version string; default parsed from filename (-v{N}-)')
    ap.add_argument('--dry-run', action='store_true',
                    help='Parse + validate; report row counts; do not write')
    args = ap.parse_args()

    if not args.findings.exists():
        raise SystemExit(f"FAIL: findings file not found: {args.findings}")

    # Parse version from filename if not given
    version = args.version
    if version is None:
        m = re.search(r'-v(\d+)-', args.findings.name)
        if not m:
            raise SystemExit(f"FAIL: cannot parse version from filename {args.findings.name}; "
                             f"pass --version explicitly")
        version = f"v{m.group(1)}"

    conn = sqlite3.connect(DB_PATH)
    conn.execute('PRAGMA foreign_keys = ON')
    cur = conn.cursor()

    # Look up characteristic_id
    row = cur.execute(
        "SELECT id, short_name FROM characteristic "
        "WHERE cluster_code=? AND char_seq=? AND delete_flagged=0",
        (args.cluster_code, args.char_seq),
    ).fetchone()
    if not row:
        raise SystemExit(
            f"FAIL: no characteristic for cluster={args.cluster_code} seq={args.char_seq}"
        )
    characteristic_id, short_name = row
    print(f"Target: characteristic_id={characteristic_id} ({args.cluster_code} #{args.char_seq} {short_name})")

    # Build q_code -> obs_id map
    q_to_obs = dict(cur.execute(
        "SELECT question_code, obs_id FROM wa_obs_question_catalogue "
        "WHERE tier IS NOT NULL AND deleted=0"
    ).fetchall())
    print(f"obs_id mapping loaded: {len(q_to_obs)} question codes")

    # Parse findings file
    parsed = parse_findings_md(args.findings, args.char_seq)
    print(f"Parsed {len(parsed)} prompt blocks from {args.findings.name}")

    # Verify every q_code maps to obs_id
    missing = [p['q_code'] for p in parsed if p['q_code'] not in q_to_obs]
    if missing:
        raise SystemExit(f"FAIL: {len(missing)} q_codes have no obs_id mapping: {missing[:5]}...")

    # Outcome tally
    tally = {'E': 0, 'S': 0, 'G': 0}
    for p in parsed:
        tally[p['outcome']] += 1
    print(f"Outcome tally: E={tally['E']}, S={tally['S']}, G={tally['G']} (total {sum(tally.values())})")

    # UNIQUE-constraint preflight: no existing row for (obs_id, cluster_code, characteristic_id, NULL, NULL, version)
    existing = cur.execute(
        "SELECT COUNT(*) FROM cluster_finding "
        "WHERE cluster_code=? AND characteristic_id=? AND cluster_subgroup_id IS NULL "
        "AND vcg_scope IS NULL AND version=? AND delete_flagged=0",
        (args.cluster_code, characteristic_id, version),
    ).fetchone()[0]
    if existing > 0:
        raise SystemExit(
            f"FAIL: {existing} cluster_finding rows already exist for "
            f"cluster={args.cluster_code} char_id={characteristic_id} version={version}. "
            f"Bump version or soft-delete prior rows first."
        )
    print(f"Preflight UNIQUE check: 0 existing rows for this (cluster,char,version) — clean to insert")

    if args.dry_run:
        print("\n=== DRY RUN — no writes ===")
        # Print a sample of what would be written
        for p in parsed[:3] + parsed[-2:]:
            print(f"  {p['q_code']} obs_id={q_to_obs[p['q_code']]} status={OUTCOME_TO_STATUS[p['outcome']]} body_len={len(p['body'])}")
        return

    # Live insert
    source_file = str(args.findings).replace('\\', '/')
    rows_to_insert = []
    for p in parsed:
        rows_to_insert.append((
            q_to_obs[p['q_code']],
            args.cluster_code,
            characteristic_id,
            None,  # cluster_subgroup_id
            None,  # vcg_scope
            OUTCOME_TO_STATUS[p['outcome']],
            p['body'],
            source_file,
            version,
            None,  # notes
            0,     # delete_flagged
            NOW_UTC,
            NOW_UTC,
        ))

    cur.execute('BEGIN')
    try:
        cur.executemany(
            "INSERT INTO cluster_finding "
            "(obs_id, cluster_code, characteristic_id, cluster_subgroup_id, vcg_scope, "
            " finding_status, finding_text, source_file, version, notes, delete_flagged, "
            " created_at, last_updated_date) "
            "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
            rows_to_insert,
        )
        conn.commit()
        print(f"\nCommitted: {len(rows_to_insert)} rows into cluster_finding")
    except Exception:
        conn.rollback()
        print("ROLLED BACK")
        raise

    # Post-verify
    post = cur.execute(
        "SELECT COUNT(*), "
        "SUM(CASE WHEN finding_status='finding' THEN 1 ELSE 0 END), "
        "SUM(CASE WHEN finding_status='silent' THEN 1 ELSE 0 END), "
        "SUM(CASE WHEN finding_status='gap' THEN 1 ELSE 0 END) "
        "FROM cluster_finding WHERE cluster_code=? AND characteristic_id=? AND version=? AND delete_flagged=0",
        (args.cluster_code, characteristic_id, version),
    ).fetchone()
    print(f"Post-insert verify: total={post[0]} finding={post[1]} silent={post[2]} gap={post[3]}")
    assert post[0] == 189, f"expected 189 rows, got {post[0]}"
    assert post[1] == tally['E']
    assert post[2] == tally['S']
    assert post[3] == tally['G']
    print("Post-verify OK.")
    conn.close()


if __name__ == '__main__':
    main()
