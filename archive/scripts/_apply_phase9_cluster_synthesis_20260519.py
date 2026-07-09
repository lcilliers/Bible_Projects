"""Phase 9 cluster-synthesis findings loader.

Parses a cluster-synthesis findings markdown file and writes 189 rows to
`cluster_finding` with:

    cluster_code           = <cluster_code>
    characteristic_id      = NULL
    cluster_subgroup_id    = NULL
    vcg_scope              = NULL
    obs_id                 = derived from T#.#.# code
    finding_status         = 'cluster_synthesis' for all rows (E/S/G
                              outcome distinction folded into finding_text;
                              schema constraint requires this enum value)
    finding_text           = scope marker + outcome + body (as authored)
    source_file            = the findings .md path
    version                = parsed from filename

The synthesis output uses the **[CLUSTER]** scope marker (not [CHAR-N]).
The free-form prose appendix (Output B per the brief) is detected and
split off into a sibling file `*-appendix-...` for the researcher's
record; appendix content is NOT inserted into cluster_finding.

Usage:
    python scripts/_apply_phase9_cluster_synthesis_20260519.py \\
        --findings Sessions/Session_Clusters/M04/WA-M04-phase9-cluster-synthesis-findings-v1-20260519.md \\
        --cluster-code M04 [--dry-run]
"""
from __future__ import annotations

import argparse
import re
import sqlite3
from datetime import datetime, timezone
from pathlib import Path

DB_PATH = Path('database/bible_research.db')
NOW_UTC = datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')

PROMPT_HEADER_RE = re.compile(r'^\*\*(T\d+\.\d+\.\d+) —', re.MULTILINE)
OUTCOME_LINE_RE = re.compile(r'^\*\*\[CLUSTER\]\*\* ([ESG]) — (.*)$', re.DOTALL)
FORBIDDEN_SCOPE_RE = re.compile(r'\*\*\[(CHAR|SUB|VCG)-')
APPENDIX_RE = re.compile(r'^##\s+Appendix\b', re.MULTILINE | re.IGNORECASE)


def parse_synthesis_md(path: Path):
    """Return (body_text_for_189_rows, appendix_text_or_empty).

    Body is the document up to (but not including) the '## Appendix'
    heading. Appendix is everything from that heading onward.
    """
    text = path.read_text(encoding='utf-8')

    forbidden = FORBIDDEN_SCOPE_RE.findall(text)
    if forbidden:
        raise SystemExit(
            f"FAIL: forbidden scope markers in synthesis file: {set(forbidden)}. "
            "Cluster synthesis output must use only **[CLUSTER]**."
        )

    m = APPENDIX_RE.search(text)
    if m:
        body = text[:m.start()].rstrip()
        appendix = text[m.start():].rstrip()
    else:
        body = text
        appendix = ""

    return body, appendix


def parse_prompt_blocks(body_text: str):
    """Yield (q_code, outcome, full_body) from the body section.

    Each block is from a **T#.#.# — line up to the next prompt header or
    the Self-check heading.
    """
    lines = body_text.splitlines()
    blocks = []
    current = None
    for ln in lines:
        m = PROMPT_HEADER_RE.match(ln)
        if m:
            if current is not None:
                blocks.append(current)
            current = {'q_code': m.group(1), 'header': ln, 'body_lines': []}
            continue
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

    seen = set()
    for b in blocks:
        if b['q_code'] in seen:
            raise SystemExit(f"FAIL: duplicate q_code {b['q_code']}")
        seen.add(b['q_code'])

    parsed = []
    for b in blocks:
        body = '\n'.join(b['body_lines']).strip()
        body = re.sub(r'\n---\s*$', '', body).strip()
        m = re.search(r'^(\*\*\[CLUSTER\]\*\* [ESG] — .*?)(?=\n\n|\Z)',
                      body, re.DOTALL | re.MULTILINE)
        if not m:
            raise SystemExit(
                f"FAIL: {b['q_code']} body does not start with **[CLUSTER]** marker. "
                f"First 200 chars: {body[:200]!r}"
            )
        outcome_para = m.group(1)
        outcome_match = OUTCOME_LINE_RE.match(outcome_para)
        if not outcome_match:
            raise SystemExit(f"FAIL: {b['q_code']} outcome paragraph not parseable")
        outcome = outcome_match.group(1)
        parsed.append({
            'q_code': b['q_code'],
            'outcome': outcome,
            'body': body,
        })
    return parsed


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--findings', required=True, type=Path)
    ap.add_argument('--cluster-code', required=True)
    ap.add_argument('--version', default=None)
    ap.add_argument('--dry-run', action='store_true')
    args = ap.parse_args()

    if not args.findings.exists():
        raise SystemExit(f"FAIL: {args.findings} not found")

    version = args.version
    if version is None:
        m = re.search(r'-v(\d+)-', args.findings.name)
        if not m:
            raise SystemExit("Cannot parse version from filename; pass --version")
        version = f"v{m.group(1)}"

    conn = sqlite3.connect(DB_PATH)
    conn.execute('PRAGMA foreign_keys = ON')
    cur = conn.cursor()

    # Verify cluster exists
    row = cur.execute(
        "SELECT cluster_code FROM cluster WHERE cluster_code=?",
        (args.cluster_code,),
    ).fetchone()
    if not row:
        raise SystemExit(f"No cluster {args.cluster_code}")
    print(f"Target: cluster_code={args.cluster_code}, characteristic_id=NULL (cluster synthesis)")

    # q_code -> obs_id mapping
    q_to_obs = dict(cur.execute(
        "SELECT question_code, obs_id FROM wa_obs_question_catalogue "
        "WHERE tier IS NOT NULL AND deleted=0"
    ).fetchall())
    print(f"obs_id mapping loaded: {len(q_to_obs)} question codes")

    # Parse
    body_text, appendix_text = parse_synthesis_md(args.findings)
    print(f"Body section: {len(body_text):,} chars; appendix: {len(appendix_text):,} chars")
    parsed = parse_prompt_blocks(body_text)
    print(f"Parsed {len(parsed)} prompt blocks")

    # Verify mappings
    missing = [p['q_code'] for p in parsed if p['q_code'] not in q_to_obs]
    if missing:
        raise SystemExit(f"FAIL: {len(missing)} q_codes have no obs_id mapping: {missing[:5]}")

    # Outcome tally
    tally = {'E': 0, 'S': 0, 'G': 0}
    for p in parsed:
        tally[p['outcome']] += 1
    print(f"Outcome tally: E={tally['E']}, S={tally['S']}, G={tally['G']}")

    # UNIQUE preflight: no existing cluster-scope rows for (cluster, NULL char, NULL sg, NULL vcg, version)
    existing = cur.execute(
        "SELECT COUNT(*) FROM cluster_finding "
        "WHERE cluster_code=? AND characteristic_id IS NULL "
        "AND cluster_subgroup_id IS NULL AND vcg_scope IS NULL "
        "AND version=? AND COALESCE(delete_flagged,0)=0",
        (args.cluster_code, version),
    ).fetchone()[0]
    if existing > 0:
        raise SystemExit(
            f"FAIL: {existing} cluster-synthesis rows already exist for "
            f"cluster={args.cluster_code} version={version}. Bump version first."
        )
    print(f"Preflight UNIQUE check: 0 existing rows for this (cluster, synthesis, version)")

    # Save appendix to sibling file
    appendix_path = None
    if appendix_text:
        appendix_path = args.findings.with_name(
            args.findings.stem.replace('-findings', '-appendix') + args.findings.suffix
        )
        appendix_path.write_text(appendix_text, encoding='utf-8')
        print(f"Appendix saved: {appendix_path} ({len(appendix_text):,} chars)")
    else:
        print("No appendix section detected (Output B missing or untagged)")

    if args.dry_run:
        print("\n=== DRY RUN — no writes ===")
        for p in parsed[:3] + parsed[-2:]:
            print(f"  {p['q_code']} obs_id={q_to_obs[p['q_code']]} outcome={p['outcome']} body_len={len(p['body'])}")
        return

    source_file = str(args.findings).replace('\\', '/')
    rows = []
    for p in parsed:
        rows.append((
            q_to_obs[p['q_code']],
            args.cluster_code,
            None,  # characteristic_id
            None,  # cluster_subgroup_id
            None,  # vcg_scope
            'cluster_synthesis',
            p['body'],
            source_file,
            version,
            f"outcome={p['outcome']}",  # notes capture E/S/G distinction
            0,
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
            rows,
        )
        conn.commit()
        print(f"\nCommitted: {len(rows)} cluster-synthesis rows.")
    except Exception:
        conn.rollback()
        print("ROLLED BACK")
        raise

    post = cur.execute(
        "SELECT COUNT(*) FROM cluster_finding "
        "WHERE cluster_code=? AND characteristic_id IS NULL AND version=? "
        "AND COALESCE(delete_flagged,0)=0",
        (args.cluster_code, version),
    ).fetchone()[0]
    print(f"Post-insert verify: {post} cluster-synthesis rows for {args.cluster_code} v={version}")
    assert post == 189
    print("Post-verify OK.")
    conn.close()


if __name__ == '__main__':
    main()
