"""_load_m06_findings_fulltext_v1_20260506.py — DB-modifying.

Full-text loader for M06 consolidated findings (DIR-20260506-002, Path A).

Reads the four consolidated findings parts from disk:
  Sessions/Session_Clusters/M06/
    WA-M06-consolidated-findings-v1-20260506-part1.md
    WA-M06-consolidated-findings-v1-20260506-part2-T2.md
    WA-M06-consolidated-findings-v1-20260506-part3-T3-T4.md
    WA-M06-consolidated-findings-v1-20260506-part4-T5-T7.md

Parses each prompt block and the per-scope answer markers within, then
UPDATEs the corresponding cluster_finding rows with verbatim finding_text
and the correct finding_status (finding | silent | gap | cluster_synthesis).

Supports marker forms:
  **[A — Hatred]** ...           → scope=A, status=finding
  **[A]** ...                     → scope=A, status=finding
  **[A, B, C]** ...               → scopes=[A,B,C], status=finding
  **[A, B, C — Label]** ...       → scopes=[A,B,C], status=finding
  **[CLUSTER]** ...               → scope=CLUSTER, status=cluster_synthesis
  **[CLUSTER — Label]** ...       → scope=CLUSTER, status=cluster_synthesis
  **S — [CLUSTER]** ...           → scope=CLUSTER, status=silent
  **S — [B, D, F]** ...           → scopes=[B,D,F], status=silent
  **G** ...                        → scope=CLUSTER, status=gap
  **G — [CLUSTER]** ...           → scope=CLUSTER, status=gap

Idempotent — re-running re-applies the same updates.
"""
from __future__ import annotations

import os
import re
import shutil
import sqlite3
import sys
from collections import defaultdict
from datetime import datetime, timezone

DB_PATH = os.path.join("database", "bible_research.db")
BACKUP_DIR = "backups"
M06_DIR = os.path.join("Sessions", "Session_Clusters", "M06")
PARTS = [
    ("part1",        "WA-M06-consolidated-findings-v1-20260506-part1.md"),
    ("part2-T2",     "WA-M06-consolidated-findings-v1-20260506-part2-T2.md"),
    ("part3-T3-T4",  "WA-M06-consolidated-findings-v1-20260506-part3-T3-T4.md"),
    ("part4-T5-T7",  "WA-M06-consolidated-findings-v1-20260506-part4-T5-T7.md"),
]
CLUSTER_CODE = "M06"
VERSION = "v1"

# Marker regex — matches one scope-answer block
# The pattern handles:
#   **G** (bare gap)
#   **G — [...]**
#   **S — [...]**
#   **[...]**  (with various scope contents)
MARKER_RE = re.compile(
    r"\*\*"
    r"(?P<marker>"
    r"(?:G\s*—\s*\[[^\]]+\])"     # G — [...]
    r"|(?:S\s*—\s*\[[^\]]+\])"     # S — [...]
    r"|(?:G(?!\w))"                # bare G
    r"|(?:\[[^\]]+\])"             # [...]
    r")"
    r"\*\*"
    r"\s*",
    re.UNICODE,
)

PROMPT_RE = re.compile(
    r"^\*\*(?P<code>T\d+\.\d+\.\d+)\*\*\s*[—-]\s*(?P<text>[^\n]+)$",
    re.MULTILINE,
)


def now_iso():
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def backup_db():
    os.makedirs(BACKUP_DIR, exist_ok=True)
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    dest = os.path.join(
        BACKUP_DIR, f"bible_research_{ts}_pre_m06_findings_fulltext.db"
    )
    shutil.copy2(DB_PATH, dest)
    return dest


def parse_marker(marker: str):
    """Parse a marker string and return (status, [scopes])."""
    s = marker.strip()
    if s.startswith("S"):
        status = "silent"
        m = re.search(r"\[([^\]]+)\]", s)
        scope_text = m.group(1) if m else "CLUSTER"
    elif s.startswith("G"):
        status = "gap"
        m = re.search(r"\[([^\]]+)\]", s)
        scope_text = m.group(1) if m else "CLUSTER"
    else:
        m = re.search(r"\[([^\]]+)\]", s)
        scope_text = m.group(1) if m else ""
        if "CLUSTER" in scope_text.upper():
            status = "cluster_synthesis"
        else:
            status = "finding"

    # Strip a label after em-dash or hyphen (e.g. "A — Hatred" → "A")
    scope_part = re.split(r"\s+[—–-]\s+", scope_text, 1)[0]

    if "CLUSTER" in scope_part.upper():
        scopes = ["CLUSTER"]
    else:
        scopes = [
            x.strip().upper()
            for x in scope_part.split(",")
            if x.strip() and re.fullmatch(r"[A-G]", x.strip())
        ]

    return status, scopes


def parse_part(text: str, source_file: str):
    """Yield (question_code, status, [scopes], text) for each scope-answer."""
    # Find all prompt headers and split body between them
    prompt_matches = list(PROMPT_RE.finditer(text))
    for i, pm in enumerate(prompt_matches):
        code = pm.group("code")
        body_start = pm.end()
        body_end = (
            prompt_matches[i + 1].start()
            if i + 1 < len(prompt_matches)
            else len(text)
        )
        body = text[body_start:body_end]

        # Find all marker positions
        marker_matches = list(MARKER_RE.finditer(body))
        if not marker_matches:
            continue

        for j, mm in enumerate(marker_matches):
            marker = mm.group("marker")
            ans_start = mm.end()
            ans_end = (
                marker_matches[j + 1].start()
                if j + 1 < len(marker_matches)
                else len(body)
            )
            answer_text = body[ans_start:ans_end].strip()

            # Trim trailing horizontal rules and section breaks
            answer_text = re.sub(r"\n+---\s*$", "", answer_text).strip()

            status, scopes = parse_marker(marker)
            if not scopes:
                continue
            yield (code, status, scopes, answer_text, source_file)


def main():
    print(f"DB: {DB_PATH}")
    print("Backing up...", flush=True)
    bak = backup_db()
    print(f"  -> {bak}\n")

    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row

    obs_by_code = {
        r["question_code"]: r["obs_id"]
        for r in conn.execute(
            "SELECT obs_id, question_code FROM wa_obs_question_catalogue "
            " WHERE tier IS NOT NULL AND COALESCE(deleted,0)=0"
        ).fetchall()
    }
    print(f"Catalogue: {len(obs_by_code)} prompts loaded")

    sg_letter_to_id = {}
    for r in conn.execute(
        "SELECT id, subgroup_code FROM cluster_subgroup "
        " WHERE cluster_code=? AND COALESCE(delete_flagged,0)=0",
        (CLUSTER_CODE,),
    ):
        if r["subgroup_code"].startswith(f"{CLUSTER_CODE}-"):
            letter = r["subgroup_code"][len(CLUSTER_CODE) + 1:]
            sg_letter_to_id[letter] = r["id"]
        else:
            sg_letter_to_id[r["subgroup_code"]] = r["id"]
    print(f"Sub-groups: {sg_letter_to_id}")
    print()

    # Aggregate parsed (code, scope) → first-encountered (status, text, source)
    # so multi-letter markers expand to one row per letter.
    parsed = {}
    issues = []

    for source_tag, fname in PARTS:
        path = os.path.join(M06_DIR, fname)
        if not os.path.exists(path):
            issues.append(f"missing source file: {path}")
            continue
        with open(path, encoding="utf-8") as f:
            text = f.read()
        n = 0
        for code, status, scopes, answer_text, src in parse_part(
            text, source_tag
        ):
            for scope in scopes:
                key = (code, scope)
                if key in parsed:
                    # Already populated from earlier source — keep first;
                    # but log if conflict
                    if parsed[key]["status"] != status:
                        issues.append(
                            f"conflict {code}/{scope}: "
                            f"{parsed[key]['status']} vs {status}"
                        )
                    continue
                parsed[key] = {
                    "status": status,
                    "text": answer_text,
                    "source": fname,
                }
                n += 1
        print(f"  {fname}: {n} (code, scope) entries parsed")

    print()
    print(f"Total parsed entries: {len(parsed)}")
    if issues:
        print(f"! {len(issues)} parser issue(s):")
        for i in issues[:15]:
            print(f"  - {i}")
        if len(issues) > 15:
            print(f"  - ... +{len(issues) - 15}")

    # Apply UPDATEs
    n_updated = n_unmapped_obs = n_unmapped_scope = 0
    by_status = defaultdict(int)

    try:
        conn.execute("BEGIN")
        for (code, scope), entry in parsed.items():
            obs_id = obs_by_code.get(code)
            if not obs_id:
                n_unmapped_obs += 1
                continue
            if scope == "CLUSTER":
                sg_id = None
            else:
                sg_id = sg_letter_to_id.get(scope)
                if not sg_id:
                    n_unmapped_scope += 1
                    continue

            note = (
                f"DIR-20260506-002 (full-text load 2026-05-06); "
                f"source: {entry['source']}; "
                f"obslog: wa-obslog-M06-m06-method-v1-20260506"
            )

            if sg_id is None:
                cur = conn.execute("""
                    UPDATE cluster_finding
                       SET finding_status=?, finding_text=?,
                           source_file=?, notes=?,
                           last_updated_date=?
                     WHERE obs_id=? AND cluster_code=?
                       AND cluster_subgroup_id IS NULL
                       AND version=?
                """, (
                    entry["status"], entry["text"], entry["source"],
                    note, now_iso(),
                    obs_id, CLUSTER_CODE, VERSION,
                ))
            else:
                cur = conn.execute("""
                    UPDATE cluster_finding
                       SET finding_status=?, finding_text=?,
                           source_file=?, notes=?,
                           last_updated_date=?
                     WHERE obs_id=? AND cluster_code=?
                       AND cluster_subgroup_id=?
                       AND version=?
                """, (
                    entry["status"], entry["text"], entry["source"],
                    note, now_iso(),
                    obs_id, CLUSTER_CODE, sg_id, VERSION,
                ))
            if cur.rowcount == 0:
                # Row didn't exist (the structural loader didn't create it
                # for this combo). Insert it instead.
                conn.execute("""
                    INSERT INTO cluster_finding
                      (obs_id, cluster_code, cluster_subgroup_id,
                       finding_status, finding_text, source_file, version,
                       notes, delete_flagged, created_at, last_updated_date)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, 0, ?, ?)
                """, (
                    obs_id, CLUSTER_CODE, sg_id,
                    entry["status"], entry["text"], entry["source"], VERSION,
                    note, now_iso(), now_iso(),
                ))
            n_updated += 1
            by_status[entry["status"]] += 1
        conn.execute("COMMIT")
    except Exception as e:
        conn.execute("ROLLBACK")
        print(f"[err] ERROR — rolled back: {e}")
        raise

    print()
    print(f"Rows updated/inserted: {n_updated}")
    if n_unmapped_obs:
        print(f"Unmapped obs codes: {n_unmapped_obs}")
    if n_unmapped_scope:
        print(f"Unmapped scope letters: {n_unmapped_scope}")
    print()
    print("By status (this load):")
    for st in ("finding", "silent", "gap", "cluster_synthesis"):
        print(f"  {st:20s} {by_status[st]}")

    print()
    print("DB state — cluster_finding for M06 (final):")
    for r in conn.execute("""
        SELECT finding_status, COUNT(*) AS n,
               SUM(CASE WHEN finding_text LIKE '[Pending%' OR finding_text
                          LIKE '[Silent%' OR finding_text LIKE '[Gap%' OR
                          finding_text LIKE '[Cluster synthesis%'
                        THEN 1 ELSE 0 END) AS still_stub
          FROM cluster_finding
         WHERE cluster_code=? AND COALESCE(delete_flagged,0)=0
         GROUP BY finding_status
    """, (CLUSTER_CODE,)):
        print(f"  {r['finding_status']:20s} total={r['n']:5d}  "
              f"still_stub={r['still_stub']}")

    # Sample
    print()
    print("Sample rows (3 representative):")
    for r in conn.execute("""
        SELECT cf.id, cf.obs_id, oqc.question_code, cs.subgroup_code,
               cf.finding_status, SUBSTR(cf.finding_text,1,100) AS text100
          FROM cluster_finding cf
          JOIN wa_obs_question_catalogue oqc ON oqc.obs_id=cf.obs_id
          LEFT JOIN cluster_subgroup cs ON cs.id=cf.cluster_subgroup_id
         WHERE cf.cluster_code=? AND COALESCE(cf.delete_flagged,0)=0
           AND cf.finding_text NOT LIKE '[Pending%'
           AND cf.finding_text NOT LIKE '[Silent — no verse evidence%'
           AND cf.finding_text NOT LIKE '[Gap%'
           AND cf.finding_text NOT LIKE '[Cluster synthesis%'
         ORDER BY cf.id LIMIT 3
    """, (CLUSTER_CODE,)):
        sg = r["subgroup_code"] or "CLUSTER"
        print(f"  qcode={r['question_code']} sg={sg} "
              f"status={r['finding_status']}")
        print(f"    text: {r['text100']}...")

    # Gap rows
    print()
    print("Gap rows requiring follow-up CC query:")
    for r in conn.execute("""
        SELECT oqc.question_code, cs.subgroup_code, cf.finding_text
          FROM cluster_finding cf
          JOIN wa_obs_question_catalogue oqc ON oqc.obs_id=cf.obs_id
          LEFT JOIN cluster_subgroup cs ON cs.id=cf.cluster_subgroup_id
         WHERE cf.cluster_code=? AND cf.finding_status='gap'
           AND COALESCE(cf.delete_flagged,0)=0
         ORDER BY oqc.question_code, cs.sort_order
    """, (CLUSTER_CODE,)):
        sg = r["subgroup_code"] or "CLUSTER"
        snip = (r["finding_text"] or "")[:80]
        print(f"  {r['question_code']} / {sg}: {snip}")

    conn.close()
    return 0


if __name__ == "__main__":
    sys.exit(main())
