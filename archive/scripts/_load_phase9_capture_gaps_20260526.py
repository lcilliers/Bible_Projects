"""Capture analytical content gaps for M10 + M10b into cluster_observation.

Per researcher direction 2026-05-26: all analytical evidence must be in the
database; on-disk-only findings violate a core programme principle. This loader
captures the gaps identified in the M10 / M10b audits.

Each gap-source file becomes 1+ cluster_observation rows. Source files captured:

  M10b (priority — cluster was already closed without these):
    - wa-cluster-M10b-phase9-cluster-synthesis-appendix-v1-20260525.md (10 themes)
    - 6 VCG design docs (M10b-A..F) — per-VCG rationale beyond verse_context_group.context_description
    - WA-M10b-phase3-constitution-verdicts-v1-20260525.md — per-term STAYS verdict rationales

  M10:
    - wa-cluster-M10-subgroup-design-v1-20260523.md (original Phase 5 design rationale)
    - wa-cluster-M10-subgroup-design-revision-v1-20260523.md (Phase 5 revision rationale)
    - wa-cluster-M10-split-design-v1-20260522.md (pre-Phase-1 split decision)
    - 22 per-char findings file Self-check blocks (meta-observations)
    - wa-m10-phase3-constitution-verdicts-v1-20260522.md — STAYS verdict rationales (57 terms; 6 BOUNDARY already captured)

Idempotent: skips any source_file already represented in cluster_observation.
"""
from __future__ import annotations
import argparse, io, re, sqlite3, sys
from datetime import datetime, timezone
from pathlib import Path

if sys.platform == "win32":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

REPO = Path(__file__).resolve().parent.parent
DB = REPO / "database" / "bible_research.db"
NOW = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def already_loaded(conn, source_rel: str) -> int:
    return conn.execute(
        "SELECT COUNT(*) FROM cluster_observation "
        "WHERE source_file=? AND COALESCE(delete_flagged,0)=0",
        (source_rel,),
    ).fetchone()[0]


def insert_obs(conn, *, cluster, source_phase, observation_type, target_phase,
               title, description, source_file, characteristic_id=None,
               cluster_subgroup_id=None):
    conn.execute(
        "INSERT INTO cluster_observation "
        "(cluster_code, characteristic_id, cluster_subgroup_id, source_phase, "
        " observation_type, target_phase, title, description, status, "
        " raised_date, source_file, delete_flagged, created_at, last_updated_date) "
        "VALUES (?, ?, ?, ?, ?, ?, ?, ?, 'open', ?, ?, 0, ?, ?)",
        (cluster, characteristic_id, cluster_subgroup_id, source_phase,
         observation_type, target_phase, title, description, NOW,
         source_file, NOW, NOW),
    )


# ========== M10b: synthesis appendix (10 themes) ==========
def load_m10b_synthesis_appendix(conn, live: bool) -> int:
    src = REPO / "Sessions/Session_Clusters/M10b/wa-cluster-M10b-phase9-cluster-synthesis-appendix-v1-20260525.md"
    rel = "Sessions/Session_Clusters/M10b/wa-cluster-M10b-phase9-cluster-synthesis-appendix-v1-20260525.md"
    if already_loaded(conn, rel):
        print(f"  already loaded: {rel}")
        return 0
    text = src.read_text(encoding="utf-8")
    # H3 themes
    matches = list(re.finditer(r"^### Theme (\d+) — (.+?)$", text, re.MULTILINE))
    n = 0
    for i, m in enumerate(matches):
        num = int(m.group(1))
        title = m.group(2).strip()
        body_start = m.end()
        body_end = matches[i+1].start() if i+1 < len(matches) else len(text)
        body = text[body_start:body_end].strip()
        if live:
            insert_obs(conn, cluster='M10b',
                       source_phase='phase_9_synthesis_appendix',
                       observation_type='CLUSTER_SYNTHESIS',
                       target_phase='session_c',
                       title=f"M10b synthesis appendix Theme {num} — {title}",
                       description=body, source_file=rel)
        n += 1
        print(f"    Theme {num} ({len(body):,}c): {title}")
    return n


# ========== M10b: 6 VCG design docs ==========
def load_m10b_vcg_designs(conn, live: bool) -> int:
    total = 0
    for sg_letter in ("A","B","C","D","E","F"):
        src = REPO / f"Sessions/Session_Clusters/M10b/files phase 7/wa-cluster-M10b-M10b-{sg_letter}-vcg-design-v1-20260525.md"
        rel = f"Sessions/Session_Clusters/M10b/files phase 7/wa-cluster-M10b-M10b-{sg_letter}-vcg-design-v1-20260525.md"
        if not src.exists():
            print(f"  missing: {rel}")
            continue
        if already_loaded(conn, rel):
            print(f"  already loaded: {rel}")
            continue
        text = src.read_text(encoding="utf-8")
        # Get the cluster_subgroup_id for M10b-{X}
        sg_id_row = conn.execute(
            "SELECT id FROM cluster_subgroup WHERE cluster_code='M10b' AND subgroup_code=? "
            "AND COALESCE(delete_flagged,0)=0", (f"M10b-{sg_letter}",)
        ).fetchone()
        sg_id = sg_id_row[0] if sg_id_row else None
        # H3 VCG sections (### M10b-X-VCG-NN — title)
        matches = list(re.finditer(
            r"^### (M10b-[A-Z]-VCG-\d+) — (.+?)$", text, re.MULTILINE
        ))
        if not matches:
            # Fall back: load whole doc as one observation
            if live:
                insert_obs(conn, cluster='M10b',
                           source_phase='phase_7_vcg_design',
                           observation_type='VCG_DESIGN_RATIONALE',
                           target_phase='session_c',
                           title=f"M10b-{sg_letter} VCG design rationale (whole document)",
                           description=text.strip(),
                           source_file=rel, cluster_subgroup_id=sg_id)
            total += 1
            print(f"  {rel}: 1 whole-doc obs ({len(text):,}c)")
        else:
            count = 0
            for i, m in enumerate(matches):
                vcg_code = m.group(1)
                title = m.group(2).strip()
                body_start = m.end()
                body_end = matches[i+1].start() if i+1 < len(matches) else len(text)
                body = text[body_start:body_end].strip()
                if live:
                    insert_obs(conn, cluster='M10b',
                               source_phase='phase_7_vcg_design',
                               observation_type='VCG_DESIGN_RATIONALE',
                               target_phase='session_c',
                               title=f"{vcg_code} — {title}",
                               description=body,
                               source_file=rel, cluster_subgroup_id=sg_id)
                count += 1
            total += count
            print(f"  {rel}: {count} VCG-level observations")
    return total


# ========== M10b: Phase 3 verdict STAYS rationales ==========
def load_m10b_phase3_verdicts(conn, live: bool) -> int:
    src = REPO / "Sessions/Session_Clusters/M10b/WA-M10b-phase3-constitution-verdicts-v1-20260525.md"
    rel = "Sessions/Session_Clusters/M10b/WA-M10b-phase3-constitution-verdicts-v1-20260525.md"
    if already_loaded(conn, rel):
        print(f"  already loaded: {rel}")
        return 0
    text = src.read_text(encoding="utf-8")
    # Match per-term verdict sections: ### {strongs} {translit} — {gloss} (mti_id={N}) — {VERDICT}
    matches = list(re.finditer(
        r"^### (\S+) (\S+) — (.+?) \(mti_id=(\d+)\) — (STAYS|TRANSFERS-TO-\S+|BOUNDARY)\s*$",
        text, re.MULTILINE
    ))
    n = 0
    for i, m in enumerate(matches):
        strongs = m.group(1)
        translit = m.group(2)
        gloss = m.group(3).strip()
        mti_id = int(m.group(4))
        verdict = m.group(5)
        body_start = m.end()
        body_end = matches[i+1].start() if i+1 < len(matches) else len(text)
        body = text[body_start:body_end].strip()
        # Cut at "## " (section boundary)
        cut = re.search(r"\n## ", body)
        if cut:
            body = body[:cut.start()].strip()
        if live:
            insert_obs(conn, cluster='M10b',
                       source_phase='phase_3_constitution_debate',
                       observation_type='VERDICT_RATIONALE',
                       target_phase='session_c',
                       title=f"M10b Phase 3 {verdict} — {strongs} {translit} ({gloss})",
                       description=body, source_file=rel)
        n += 1
    print(f"  {rel}: {n} per-term verdict observations")
    return n


# ========== M10: sub-group design + revision + split ==========
def load_m10_subgroup_design(conn, live: bool) -> int:
    src = REPO / "Sessions/Session_Clusters/M10/files phase 5/wa-cluster-M10-subgroup-design-v1-20260523.md"
    rel = "Sessions/Session_Clusters/M10/files phase 5/wa-cluster-M10-subgroup-design-v1-20260523.md"
    if already_loaded(conn, rel):
        print(f"  already loaded: {rel}")
        return 0
    text = src.read_text(encoding="utf-8")
    # H2 sections: §1 Characteristics identified, §2 Sub-group design, §3 Multi-faceted terms
    matches = list(re.finditer(r"^## (§\d+\..+?)$", text, re.MULTILINE))
    n = 0
    for i, m in enumerate(matches):
        title = m.group(1).strip()
        body_start = m.end()
        body_end = matches[i+1].start() if i+1 < len(matches) else len(text)
        body = text[body_start:body_end].strip()
        if live:
            insert_obs(conn, cluster='M10',
                       source_phase='phase_5_subgroup_design',
                       observation_type='SUBGROUP_DESIGN_RATIONALE',
                       target_phase='session_c',
                       title=f"M10 sub-group design (original) — {title}",
                       description=body, source_file=rel)
        n += 1
        print(f"    {title} ({len(body):,}c)")
    return n


def load_m10_subgroup_revision(conn, live: bool) -> int:
    src = REPO / "Sessions/Session_Clusters/M10/files phase 5 b/wa-cluster-M10-subgroup-design-revision-v1-20260523.md"
    rel = "Sessions/Session_Clusters/M10/files phase 5 b/wa-cluster-M10-subgroup-design-revision-v1-20260523.md"
    if already_loaded(conn, rel):
        print(f"  already loaded: {rel}")
        return 0
    text = src.read_text(encoding="utf-8")
    matches = list(re.finditer(r"^## (§\d+\..+?)$", text, re.MULTILINE))
    n = 0
    if matches:
        for i, m in enumerate(matches):
            title = m.group(1).strip()
            body_start = m.end()
            body_end = matches[i+1].start() if i+1 < len(matches) else len(text)
            body = text[body_start:body_end].strip()
            if live:
                insert_obs(conn, cluster='M10',
                           source_phase='phase_5_subgroup_design_revision',
                           observation_type='SUBGROUP_DESIGN_RATIONALE',
                           target_phase='session_c',
                           title=f"M10 sub-group design REVISION — {title}",
                           description=body, source_file=rel)
            n += 1
            print(f"    {title} ({len(body):,}c)")
    else:
        # Whole doc fallback
        if live:
            insert_obs(conn, cluster='M10',
                       source_phase='phase_5_subgroup_design_revision',
                       observation_type='SUBGROUP_DESIGN_RATIONALE',
                       target_phase='session_c',
                       title="M10 sub-group design REVISION (whole document)",
                       description=text.strip(), source_file=rel)
        n = 1
        print(f"    whole doc ({len(text):,}c)")
    return n


def load_m10_split_design(conn, live: bool) -> int:
    src = REPO / "Sessions/Session_Clusters/M10/wa-cluster-M10-split-design-v1-20260522.md"
    rel = "Sessions/Session_Clusters/M10/wa-cluster-M10-split-design-v1-20260522.md"
    if already_loaded(conn, rel):
        print(f"  already loaded: {rel}")
        return 0
    text = src.read_text(encoding="utf-8")
    if live:
        insert_obs(conn, cluster='M10',
                   source_phase='pre_phase_1_split_design',
                   observation_type='SPLIT_DESIGN_RATIONALE',
                   target_phase='session_c',
                   title="M10 pre-Phase-1 split design (M10 / M10b / M10c)",
                   description=text.strip(), source_file=rel)
    print(f"  {rel}: 1 whole-doc obs ({len(text):,}c)")
    return 1


# ========== M10: per-char Self-check blocks (22 chars) ==========
def load_m10_char_self_checks(conn, live: bool) -> int:
    total = 0
    char_files = sorted(
        (REPO / "Sessions/Session_Clusters/M10/files phase 9").glob(
            "wa-cluster-M10-phase9-char*-findings-v1-20260523.md"))
    for f in char_files:
        rel = f"Sessions/Session_Clusters/M10/files phase 9/{f.name}"
        # Source-file collisions: we'd be re-loading a file already loaded for cluster_finding.
        # Use a marker in source_file to distinguish:
        source_marker = rel + "#self-check"
        if already_loaded(conn, source_marker):
            continue
        text = f.read_text(encoding="utf-8")
        m = re.search(r"^## Self-check.*?\Z", text, re.MULTILINE | re.DOTALL)
        if not m:
            print(f"  {f.name}: no Self-check block")
            continue
        sc = m.group(0).strip()
        # Extract char_seq from filename: wa-cluster-M10-phase9-char{N}-...
        cs_m = re.match(r"wa-cluster-M10-phase9-char(\d+)-", f.name)
        char_seq = int(cs_m.group(1)) if cs_m else None
        # Look up characteristic_id
        char_id = None
        if char_seq:
            r = conn.execute(
                "SELECT id FROM characteristic WHERE cluster_code='M10' AND char_seq=? "
                "AND COALESCE(delete_flagged,0)=0", (char_seq,)
            ).fetchone()
            char_id = r[0] if r else None
        if live:
            insert_obs(conn, cluster='M10',
                       source_phase='phase_9_self_check',
                       observation_type='SELF_CHECK_OBSERVATION',
                       target_phase='session_c',
                       title=f"M10 Char {char_seq} Phase 9 Self-check meta-observations",
                       description=sc, source_file=source_marker,
                       characteristic_id=char_id)
        total += 1
    print(f"  per-char Self-check blocks: {total}")
    return total


# ========== M10: Phase 3 STAYS verdict rationales ==========
def load_m10_phase3_verdicts(conn, live: bool) -> int:
    src = REPO / "Sessions/Session_Clusters/M10/wa-m10-phase3-constitution-verdicts-v1-20260522.md"
    rel = "Sessions/Session_Clusters/M10/wa-m10-phase3-constitution-verdicts-v1-20260522.md"
    # Check what's already loaded (the 6 BOUNDARY rows used this source_file; their titles start with "Phase 3 BOUNDARY:")
    existing_titles = [r[0] for r in conn.execute(
        "SELECT title FROM cluster_observation "
        "WHERE source_file=? AND COALESCE(delete_flagged,0)=0", (rel,)
    ).fetchall()]
    existing_boundary = sum(1 for t in existing_titles if t and t.startswith("Phase 3 BOUNDARY"))
    text = src.read_text(encoding="utf-8")
    matches = list(re.finditer(
        r"^### (\S+) (\S+) — (.+?) \(mti_id=(\d+)\) — (STAYS|TRANSFERS-TO-\S+|BOUNDARY)\s*$",
        text, re.MULTILINE
    ))
    n = 0
    for i, m in enumerate(matches):
        strongs = m.group(1)
        translit = m.group(2)
        gloss = m.group(3).strip()
        mti_id = int(m.group(4))
        verdict = m.group(5)
        # Skip BOUNDARY — already captured
        if verdict == "BOUNDARY":
            continue
        body_start = m.end()
        body_end = matches[i+1].start() if i+1 < len(matches) else len(text)
        body = text[body_start:body_end].strip()
        cut = re.search(r"\n## ", body)
        if cut:
            body = body[:cut.start()].strip()
        title = f"M10 Phase 3 {verdict} — {strongs} {translit} ({gloss})"
        # Idempotency by title
        if title in existing_titles:
            continue
        if live:
            insert_obs(conn, cluster='M10',
                       source_phase='phase_3_constitution_debate',
                       observation_type='VERDICT_RATIONALE',
                       target_phase='session_c',
                       title=title, description=body, source_file=rel)
        n += 1
    print(f"  M10 Phase 3 STAYS+TRANSFERS verdicts: {n} new (existing BOUNDARY: {existing_boundary})")
    return n


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--live", action="store_true")
    ap.add_argument("--only", help="run only one group: m10b-appendix | m10b-vcg | m10b-verdicts | m10-subgroup | m10-revision | m10-split | m10-self-checks | m10-verdicts")
    args = ap.parse_args()
    live = args.live
    print(f"=== Phase 9 capture-gap loader — mode={'LIVE' if live else 'DRY-RUN'} ===")

    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row
    if live:
        conn.execute("BEGIN")

    try:
        ops = [
            ("m10b-appendix",  "M10b synthesis appendix",           load_m10b_synthesis_appendix),
            ("m10b-vcg",        "M10b VCG design docs (6)",          load_m10b_vcg_designs),
            ("m10b-verdicts",   "M10b Phase 3 verdict rationales",   load_m10b_phase3_verdicts),
            ("m10-subgroup",    "M10 sub-group design (original)",   load_m10_subgroup_design),
            ("m10-revision",    "M10 sub-group design REVISION",     load_m10_subgroup_revision),
            ("m10-split",       "M10 split design rationale",        load_m10_split_design),
            ("m10-self-checks", "M10 per-char Self-check blocks",    load_m10_char_self_checks),
            ("m10-verdicts",    "M10 Phase 3 verdict rationales",    load_m10_phase3_verdicts),
        ]
        totals: dict[str, int] = {}
        for key, label, fn in ops:
            if args.only and args.only != key:
                continue
            print(f"\n--- {label} ---")
            totals[key] = fn(conn, live)

        if live:
            conn.commit()
            print(f"\nCOMMITTED at {NOW}")
        else:
            print(f"\n[DRY-RUN — no writes]")
        print(f"\n=== Summary ===")
        for key, n in totals.items():
            print(f"  {key}: {n} rows")
        print(f"  TOTAL: {sum(totals.values())} rows")
    except Exception:
        if live:
            conn.rollback()
            print("ROLLED BACK")
        raise
    finally:
        conn.close()
    return 0


if __name__ == "__main__":
    sys.exit(main())
