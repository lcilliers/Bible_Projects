"""Pass A meaning record via Claude API (cluster-agnostic).

Per v2_0 §5 — for each is_relevant=1 active verse_context row in a cluster, AI writes
a one-line meaning to `verse_context.analysis_note`. Atomic per-row work via JSON
template; no sub-groups, no inherited VCGs, no anchor info visible to AI.

Usage:
  python scripts/_run_passa_via_api_v1_20260515.py --m-cluster M01 [--batch-size 50] [--limit 0] [--dry-run-fetch] [--characteristic-file PATH]

Outputs (under Sessions/Session_Clusters/{code}/):
  - wa-cluster-{code}-patch-passa-meanings-v1-{YYYYMMDD}.json   (VCREVISE patch, applier-ready)
  - WA-{code}-passa-meanings-applied-v1-{YYYYMMDD}.md           (per-batch counts, sample meanings)
  - WA-{code}-passa-api-raw-responses-{YYYYMMDD}.json           (raw API output)

Then apply via:
  python scripts/apply_session_patch.py --dry-run "<patch path>"
  python scripts/apply_session_patch.py "<patch path>"
"""
from __future__ import annotations
import argparse, json, os, re, sqlite3, sys, time
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

# Load .env for ANTHROPIC_API_KEY
env_path = Path(".env")
if env_path.exists():
    for line in env_path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if line.startswith("ANTHROPIC_API_KEY=") and "ANTHROPIC_API_KEY" not in os.environ:
            os.environ["ANTHROPIC_API_KEY"] = line.split("=", 1)[1].strip()
            break

import anthropic

REPO = Path(__file__).resolve().parent.parent
DB = REPO / "database" / "bible_research.db"
MODEL = "claude-sonnet-4-6"
DEFAULT_BATCH_SIZE = 50

# Sentinel patterns we refuse to accept in meaning output
# (catches AI re-anchoring on group/sub-group structure)
SENTINEL_PATTERNS = [
    re.compile(r"\bM\d{2}-[A-Z]"),                  # sub-group code like M01-A
    re.compile(r"\b\d{2,4}-\d{3}\b"),               # VCG group_code like 7577-001
    re.compile(r"\bsub-?group\s+[A-Z]\b", re.I),    # "subgroup A" etc.
    re.compile(r"\b(?:VCG|verse_context_group)\b", re.I),
    re.compile(r"^\s*\*\*\[[A-Z]+", re.M),          # "**[A]" Phase 9 marker form
]


def build_system_prompt(cluster_code: str, cluster_description: str, gloss: str,
                         characteristic_override: str | None) -> str:
    """Build the system prompt for Pass A meaning record."""
    if characteristic_override:
        characteristic_block = characteristic_override
    else:
        characteristic_block = (
            f"Cluster {cluster_code} — {cluster_description}.\n\n"
            f"The cluster's term set (auto-extracted gloss): {gloss}"
        )

    return f"""You are Claude AI performing Pass A meaning record for Session B cluster analysis under wa-sessionb-cluster-instruction-v2_0-20260515 §5.

CLUSTER CHARACTERISTIC

{characteristic_block}

YOUR TASK

For each verse in the batch, write a one-line meaning answering: **what does this verse say about the inner-being characteristic the term names, in this verse's specific context?**

DISCIPLINE — non-negotiable

1. Read the verse text. Write what *this* verse says about *this* term's inner-being content.
2. The meaning must be verse-specific — name what is in this verse, not the term's general sense.
3. Plain English. 1–2 sentences. Maximum ~300 characters.
4. No group framing — do not write "M01-A territory", "VCG 7577-001 register", "[A] sub-group", or any sub-group / VCG / anchor language. These have no place in a Pass A meaning.
5. No back-anchoring — do not validate against any pre-existing structure. The verse and the term are the only inputs that matter.
6. If the verse genuinely does not evidence inner-being content for this term in this verse, note that briefly in the meaning. Do not omit the row.

T1 FRAMEWORK — what to look for in the verse

A characteristic-bearing verse evidences one or more of:
- Constitutional location — heart, mind, will, conscience, soul, spirit, body — where in the inner person it sits.
- Inner faculties engaged — perception, thought, memory, feeling, conscience, will, agency.
- Inner impact — what the characteristic does to the person, to relationships, to action.
- Structural opposite — the characteristic implicitly defines its contour by what it stands against.
- Direction or object — toward what / produced by what / operating against what.

If the verse evidences any of these, your meaning names which one(s) and how.

OUTPUT FORMAT — strict JSON

Respond with exactly one JSON array. One object per verse, in the same order the verses were given. Each object must have these fields:

  {{
    "vc_id": <integer — copy from input>,
    "reference": "<string — copy from input>",
    "meaning": "<one-line plain-English meaning, ~250 chars, verse-specific>"
  }}

Do not include any text outside the JSON array. No prose, no preamble, no markdown fence. Just the JSON.
"""


def fetch_pass_a_load(conn, cluster_code: str) -> list[dict]:
    """Fetch all is_relevant=1 active vc rows lacking analysis_note, in canonical order."""
    rows = list(conn.execute("""
        SELECT vc.id AS vc_id, vc.verse_record_id, vc.mti_term_id,
               vr.book_id, vr.chapter, vr.verse_num, vr.reference,
               vr.verse_text, vr.context_before, vr.context_after, vr.translation,
               mt.strongs_number, mt.transliteration, mt.gloss, mt.language
        FROM verse_context vc
        JOIN mti_terms mt ON mt.id = vc.mti_term_id
        JOIN wa_verse_records vr ON vr.id = vc.verse_record_id
        WHERE mt.cluster_code = ?
          AND COALESCE(mt.delete_flagged, 0) = 0
          AND COALESCE(vc.delete_flagged, 0) = 0
          AND COALESCE(vr.delete_flagged, 0) = 0
          AND vc.is_relevant = 1
          AND vc.analysis_note IS NULL
        ORDER BY vr.book_id, vr.chapter, vr.verse_num, mt.strongs_number, vc.id
    """, (cluster_code,)))
    return [dict(r) for r in rows]


def build_batch_message(batch_num: int, total_batches: int, verses: list[dict]) -> str:
    """Per-batch user message: just the verses, in canonical order."""
    parts = [
        f"Batch {batch_num} of {total_batches} — {len(verses)} verses to read.",
        "",
        "Read each verse below. Write the one-line meaning per the rubric in the system prompt.",
        "",
    ]
    for v in verses:
        parts.append("---")
        parts.append(f"vc_id: {v['vc_id']}")
        parts.append(f"reference: {v['reference']}")
        parts.append(f"strongs: {v['strongs_number']}")
        parts.append(f"transliteration: {v['transliteration']}")
        parts.append(f"gloss: {v['gloss']}")
        parts.append(f"language: {v['language']}")
        parts.append(f"verse_text ({v.get('translation') or 'ESV'}): {v['verse_text'] or ''}")
        cb = (v.get("context_before") or "")[:200]
        ca = (v.get("context_after") or "")[:200]
        if cb: parts.append(f"context_before: {cb}")
        if ca: parts.append(f"context_after: {ca}")
    parts.append("")
    parts.append("Return the JSON array now. No prose.")
    return "\n".join(parts)


def classify_batch(client, system_prompt: str, batch_num: int, total_batches: int,
                   verses: list[dict], max_retries: int = 2) -> tuple[list[dict], dict, str]:
    user_msg = build_batch_message(batch_num, total_batches, verses)
    last_err = None
    for attempt in range(max_retries + 1):
        try:
            resp = client.messages.create(
                model=MODEL,
                max_tokens=12000,
                system=[
                    {"type": "text", "text": system_prompt,
                     "cache_control": {"type": "ephemeral"}},
                ],
                messages=[{"role": "user", "content": user_msg}],
            )
            text = resp.content[0].text.strip()
            if text.startswith("```"):
                text = text.split("```", 2)[1]
                if text.startswith("json"):
                    text = text[4:]
                text = text.strip("`").strip()
            results = json.loads(text)
            if not isinstance(results, list):
                raise ValueError("response is not a JSON array")
            usage = {
                "input_tokens": resp.usage.input_tokens,
                "output_tokens": resp.usage.output_tokens,
                "cache_creation": getattr(resp.usage, "cache_creation_input_tokens", 0),
                "cache_read": getattr(resp.usage, "cache_read_input_tokens", 0),
            }
            return results, usage, text
        except (json.JSONDecodeError, ValueError) as e:
            last_err = e
            if attempt < max_retries:
                time.sleep(2)
                continue
            raise


def check_sentinels(meaning: str) -> list[str]:
    """Return list of sentinel-pattern names that fired on this meaning text."""
    hits = []
    for pat in SENTINEL_PATTERNS:
        if pat.search(meaning):
            hits.append(pat.pattern)
    return hits


def build_vcrevise_patch(cluster_code: str, all_verses: list[dict],
                          all_results: dict[int, dict], date_str: str) -> dict:
    """One UPDATE op per filled meaning. VCREVISE patch in applier shape."""
    ops = []
    seq = 1
    by_term = {}
    md_versions = {}
    conn = sqlite3.connect(DB); conn.row_factory = sqlite3.Row
    try:
        for v in all_verses:
            mti = v["mti_term_id"]
            by_term.setdefault(mti, None)
        for mti in by_term:
            r = conn.execute("SELECT md_version FROM mti_terms WHERE id=?", (mti,)).fetchone()
            md_versions[mti] = r["md_version"] if r else 1
    finally:
        conn.close()

    terms_covered = sorted(by_term.keys())

    for v in all_verses:
        r = all_results.get(v["vc_id"])
        if not r:
            continue
        meaning = r.get("meaning", "").strip()
        if not meaning:
            continue
        ops.append({
            "op_id": f"OP-{seq:04d}",
            "table": "verse_context",
            "operation": "update",
            "match": {"id": v["vc_id"], "delete_flagged": 0},
            "set": {"analysis_note": meaning},
            "_reference": v["reference"],
            "_strongs": v["strongs_number"],
        })
        seq += 1

    return {
        "_patch_meta": {
            "patch_type": "VCREVISE",
            "patch_id": f"wa-cluster-{cluster_code}-patch-passa-meanings-v1-{date_str}",
            "cluster_code": cluster_code,
            "session_ref": f"{cluster_code} Phase 2 Pass A meaning record via Claude API",
            "governing_instruction": "wa-sessionb-cluster-instruction-v2_0-20260515",
            "date": date_str,
            "terms_covered": terms_covered,
            "input_versions": {str(k): v for k, v in md_versions.items()},
            "op_count": len(ops),
            "source": f"Claude API meaning record (Sonnet 4.6); {len(all_verses)} verses across {len(by_term)} terms",
        },
        "operations": ops,
    }


def write_applied_report(cluster_code: str, all_verses: list[dict],
                          all_results: dict[int, dict], batch_stats: list[dict],
                          sentinel_violations: list[dict], usage_totals: dict,
                          patch_path: Path, log_path: Path) -> None:
    n_total = len(all_verses)
    n_filled = sum(1 for v in all_verses if v["vc_id"] in all_results)
    n_with_meaning = sum(1 for v in all_verses
                         if v["vc_id"] in all_results and all_results[v["vc_id"]].get("meaning"))

    # Sample 5 meanings
    samples = []
    for v in all_verses[:5]:
        r = all_results.get(v["vc_id"])
        if r:
            m = (r.get("meaning") or "")[:200]
            samples.append(f"- {v['reference']} ({v['strongs_number']} {v['transliteration']}): {m}")

    lines = [
        f"# WA-{cluster_code}-passa-meanings-applied-v1-{datetime.now().strftime('%Y%m%d')}",
        "",
        f"Pass A meaning record for cluster {cluster_code} via Claude API (Sonnet 4.6).",
        "Governing instruction: wa-sessionb-cluster-instruction-v2_0-20260515 §5.",
        "",
        "## Summary",
        "",
        f"- Verses targeted: {n_total}",
        f"- Verses with meaning filled: {n_with_meaning}",
        f"- Batches: {len(batch_stats)}",
        f"- Sentinel violations (meanings containing group/sub-group/VCG references): {len(sentinel_violations)}",
        "",
        "## API usage totals",
        "",
        f"- Input tokens: {usage_totals['input']:,}",
        f"- Output tokens: {usage_totals['output']:,}",
        f"- Cache create tokens: {usage_totals['cache_create']:,}",
        f"- Cache read tokens: {usage_totals['cache_read']:,}",
        "",
        "## Sample meanings (first 5)",
        "",
        *samples,
        "",
        "## Sentinel violations",
        "",
    ]
    if sentinel_violations:
        for sv in sentinel_violations[:50]:
            lines.append(f"- vc_id={sv['vc_id']} {sv['reference']} hit pattern `{sv['pattern']}`: "
                         f"{(sv['meaning'] or '')[:160]}")
        if len(sentinel_violations) > 50:
            lines.append(f"- ... and {len(sentinel_violations)-50} more")
        lines.append("")
        lines.append("**Action required:** re-run Pass A for these specific vc_ids with a corrective prompt, "
                     "or accept the meanings if researcher reviews and approves. Do not apply the patch "
                     "until violations are resolved.")
    else:
        lines.append("_(none — all meanings free of group/sub-group/VCG references)_")
    lines.append("")
    lines.append("## Patch")
    lines.append("")
    lines.append(f"- File: `{patch_path.name}`")
    lines.append(f"- Operations: {n_with_meaning} VCREVISE updates")
    lines.append(f"- Apply: `python scripts/apply_session_patch.py --dry-run {patch_path.as_posix()}` then live")
    log_path.write_text("\n".join(lines), encoding="utf-8")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--m-cluster", required=True, help="Cluster code, e.g. M01")
    ap.add_argument("--batch-size", type=int, default=DEFAULT_BATCH_SIZE)
    ap.add_argument("--limit", type=int, default=0, help="Limit to first N batches (0=all)")
    ap.add_argument("--dry-run-fetch", action="store_true",
                    help="Fetch + print Pass A load; do not call API.")
    ap.add_argument("--characteristic-file", type=str, default=None,
                    help="Path to a markdown file containing a cluster characteristic statement. "
                         "Overrides the auto-built cluster description.")
    args = ap.parse_args()

    code = args.m_cluster.strip()
    out_dir = REPO / "Sessions" / "Session_Clusters" / code
    out_dir.mkdir(parents=True, exist_ok=True)
    date_str = datetime.now(timezone.utc).strftime("%Y%m%d")
    patch_path = out_dir / f"wa-cluster-{code}-patch-passa-meanings-v1-{date_str}.json"
    log_path = out_dir / f"WA-{code}-passa-meanings-applied-v1-{date_str}.md"
    raw_path = out_dir / f"WA-{code}-passa-api-raw-responses-{date_str}.json"

    conn = sqlite3.connect(DB); conn.row_factory = sqlite3.Row
    cluster = conn.execute(
        "SELECT cluster_code, description, gloss FROM cluster WHERE cluster_code=?",
        (code,)
    ).fetchone()
    if not cluster:
        print(f"ERROR: cluster {code} not found.")
        return 1

    verses = fetch_pass_a_load(conn, code)
    conn.close()

    if not verses:
        print(f"Cluster {code}: no verses need Pass A (all is_relevant rows already have analysis_note).")
        return 0

    print(f"Cluster {code}: {cluster['description']}")
    print(f"Pass A load: {len(verses)} is_relevant verses needing meaning")

    # Build batches
    batches = []
    for i in range(0, len(verses), args.batch_size):
        batches.append(verses[i:i + args.batch_size])
    if args.limit:
        batches = batches[:args.limit]
    total_batches = len(batches)
    print(f"Batches: {total_batches} of size up to {args.batch_size}")

    if args.dry_run_fetch:
        print("[--dry-run-fetch] No API calls made.")
        # Show first 3 verses for confirmation
        for v in verses[:3]:
            print(f"  vc_id={v['vc_id']} {v['reference']} {v['strongs_number']} {v['transliteration']}")
        return 0

    # Build system prompt
    characteristic_override = None
    if args.characteristic_file:
        cp = Path(args.characteristic_file)
        if not cp.exists():
            print(f"ERROR: characteristic file not found: {cp}")
            return 1
        characteristic_override = cp.read_text(encoding="utf-8")
    system_prompt = build_system_prompt(code, cluster["description"], cluster["gloss"],
                                         characteristic_override)

    # Save the system prompt for audit
    (out_dir / f"WA-{code}-passa-system-prompt-{date_str}.txt").write_text(system_prompt, encoding="utf-8")

    client = anthropic.Anthropic()
    print(f"\nModel: {MODEL}\n")

    all_results: dict[int, dict] = {}
    raw_archive: list[dict] = []
    batch_stats: list[dict] = []
    sentinel_violations: list[dict] = []
    totals_u = {"input": 0, "output": 0, "cache_create": 0, "cache_read": 0}

    for i, batch in enumerate(batches, 1):
        print(f"[{i}/{total_batches}] {len(batch)} verses ...", end=" ", flush=True)
        t0 = time.time()
        results, usage, raw_text = classify_batch(client, system_prompt, i, total_batches, batch)
        elapsed = time.time() - t0
        totals_u["input"] += usage["input_tokens"]
        totals_u["output"] += usage["output_tokens"]
        totals_u["cache_create"] += usage["cache_creation"]
        totals_u["cache_read"] += usage["cache_read"]
        by_vc = {r.get("vc_id"): r for r in results if isinstance(r, dict) and r.get("vc_id")}
        # Sentinel check
        for v in batch:
            r = by_vc.get(v["vc_id"])
            if not r:
                continue
            meaning = (r.get("meaning") or "").strip()
            hits = check_sentinels(meaning)
            if hits:
                for h in hits:
                    sentinel_violations.append({
                        "vc_id": v["vc_id"],
                        "reference": v["reference"],
                        "meaning": meaning,
                        "pattern": h,
                    })
        n_filled = sum(1 for v in batch if by_vc.get(v["vc_id"]) and by_vc[v["vc_id"]].get("meaning"))
        all_results.update(by_vc)
        batch_stats.append({"batch": i, "size": len(batch), "filled": n_filled,
                            "elapsed_s": round(elapsed, 1), "usage": usage})
        print(f"filled={n_filled}/{len(batch)} ({elapsed:.1f}s, in={usage['input_tokens']} "
              f"out={usage['output_tokens']} cache_read={usage['cache_read']})")
        raw_archive.append({"batch": i, "usage": usage, "response": raw_text})

    print(f"\nTotal usage: input={totals_u['input']:,}  output={totals_u['output']:,}  "
          f"cache_create={totals_u['cache_create']:,}  cache_read={totals_u['cache_read']:,}")

    # Build patch
    flat_verses = [v for batch in batches for v in batch]
    patch = build_vcrevise_patch(code, flat_verses, all_results, date_str)
    patch_path.write_text(json.dumps(patch, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"\nPatch: {patch_path}  ({patch['_patch_meta']['op_count']} ops)")

    raw_path.write_text(json.dumps(raw_archive, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"Raw responses: {raw_path}")

    write_applied_report(code, flat_verses, all_results, batch_stats, sentinel_violations,
                          totals_u, patch_path, log_path)
    print(f"Applied report: {log_path}")

    if sentinel_violations:
        print(f"\nWARNING: {len(sentinel_violations)} sentinel violations detected. "
              f"See report before applying patch.")
        return 2

    return 0


if __name__ == "__main__":
    sys.exit(main())
