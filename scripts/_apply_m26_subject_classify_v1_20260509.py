"""_apply_m26_subject_classify_v1_20260509.py — God/man classifier.

Step A produced one meaning per (verse, term). This script adds a
classification: does THIS verse use THIS term to speak of the
righteousness of God, of man, of both, or of neither?

Reads the Step A JSONL (one record per (vr_id, mti_term_id)).
Writes a parallel JSONL with the same key + a small classification.

Atomic per-record. Resumable. Sub-group filterable so we can do
M26-A only first as a step proof before extending.

Output JSON shape:
  {vr_id, mti_term_id, strong, subject, justification}

subject ∈ {"God", "man", "both", "neither"}
"""
from __future__ import annotations

import argparse
import json
import os
import sqlite3
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

try:
    from dotenv import load_dotenv
    load_dotenv(".env")
except ImportError:
    pass

DB_PATH = os.path.join("database", "bible_research.db")
OUT_DIR = os.path.join("outputs", "markdown")


SYSTEM_PROMPT = """You are an analyst on the Soul Word Analysis Programme — Step B-1 (subject classifier) for cluster M26 — Righteousness and Justice.

# Task

You receive ONE verse + ONE term + the already-extracted meaning of that verse via that term. Classify whether THIS verse uses THIS term to refer to:

- "God" — God the Father, Yahweh, the Lord, Christ Jesus, the Spirit. Includes divine attributes, divine judgments, divine standard, divine titles ("the Righteous One"), the LORD's character or actions.
- "man" — a human person's character, status, action, or class. Named individuals (Joseph, Cornelius, Lot, Abel), named groups, and the generic class "the righteous" / "the just" used of persons.
- "both" — the verse genuinely speaks of both God's righteousness and man's righteousness in the same use of the term (rare; e.g., "Christ the righteous for the unrighteous" — Christ as God-person + the unrighteous class).
- "neither" — the term qualifies a non-personal noun: the law, the commandment, a decree, a judgment as event, a way, a word, an offering, a sacrifice; or the term is used adverbially ("rightly"); or the use is figurative/idiomatic and not about a personal inner-being characteristic.

# Discipline

- Christ / Jesus → "God".
- "the righteous" as a generic class of obedient persons → "man".
- "the Righteous One" as a divine title → "God".
- "righteous judgment of God" / "just are your ways, O Lord" → "God" (the attribute is God's even if the noun is judgment).
- "the law is righteous" / "the commandment is just" → "neither" (qualifies an impersonal noun).
- "righteousness of faith" / "credited as righteousness" — if the verse focuses on God's act of crediting and the standard is God's, classify "God"; if it focuses on the human believer's resulting status, "man"; "both" only when both are foregrounded.
- When in doubt between "man" and "neither" (e.g., a corporate group like "the nation"), prefer "man".
- Use the verse text and the supplied meaning. Do not import outside theology.

# Output JSON shape — exactly

{
  "vr_id": <int — copied from input>,
  "mti_term_id": <int — copied from input>,
  "strong": "<copied from input>",
  "subject": "God" | "man" | "both" | "neither",
  "justification": "<≤12 word phrase pointing to the cue in verse or meaning>"
}
"""


OUTPUT_SCHEMA = {
    "type": "object",
    "properties": {
        "vr_id": {"type": "integer"},
        "mti_term_id": {"type": "integer"},
        "strong": {"type": "string"},
        "subject": {"type": "string",
                    "enum": ["God", "man", "both", "neither"]},
        "justification": {"type": "string"},
    },
    "required": ["vr_id", "mti_term_id", "strong", "subject",
                 "justification"],
    "additionalProperties": False,
}


def now_iso():
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def today_compact():
    return datetime.now(timezone.utc).strftime("%Y%m%d")


def load_meanings(jsonl_path: str) -> list[dict]:
    out = []
    with open(jsonl_path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            out.append(json.loads(line))
    return out


def load_verse_and_term_meta(conn, vr_ids: set[int],
                             mti_ids: set[int]) -> tuple[dict, dict]:
    """Return verse_meta {vr_id: {reference, verse_text}} and
    term_meta {mti_term_id: {strong, gloss, sg_code}}."""
    placeholders_v = ",".join("?" * len(vr_ids))
    placeholders_t = ",".join("?" * len(mti_ids))
    verses = {
        r["id"]: {"reference": r["reference"], "verse_text": r["verse_text"]}
        for r in conn.execute(
            f"SELECT id, reference, verse_text FROM wa_verse_records "
            f" WHERE id IN ({placeholders_v})",
            tuple(vr_ids),
        )
    }
    terms = {
        r["id"]: {
            "strong": r["strongs_number"], "gloss": r["gloss"],
            "translit": r["transliteration"],
            "sg_code": r["subgroup_code"] or "M26-UNASSIGNED",
        }
        for r in conn.execute(
            f"SELECT mt.id, mt.strongs_number, mt.gloss, mt.transliteration, "
            f"       cs.subgroup_code "
            f"  FROM mti_terms mt "
            f"  LEFT JOIN cluster_subgroup cs ON cs.id=mt.cluster_subgroup_id "
            f" WHERE mt.id IN ({placeholders_t})",
            tuple(mti_ids),
        )
    }
    return verses, terms


def load_completed_keys(jsonl_path: str) -> set[tuple[int, int]]:
    done = set()
    if not Path(jsonl_path).exists():
        return done
    with open(jsonl_path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                obj = json.loads(line)
                done.add((obj["vr_id"], obj["mti_term_id"]))
            except Exception:
                pass
    return done


def build_user_msg(meaning_rec: dict, verse: dict, term: dict) -> str:
    pkg = {
        "vr_id": meaning_rec["vr_id"],
        "mti_term_id": meaning_rec["mti_term_id"],
        "reference": verse["reference"],
        "verse_text": verse["verse_text"],
        "term": {
            "strong": term["strong"],
            "transliteration": term.get("translit"),
            "gloss": term["gloss"],
        },
        "step_a_meaning": meaning_rec["meaning"],
        "step_a_evidence": meaning_rec["evidence_quote"],
    }
    return (
        "Classify the subject (God / man / both / neither) for this "
        "(verse, term) pair. Return JSON in the schema above.\n\n"
        f"```json\n{json.dumps(pkg, ensure_ascii=False, indent=2)}\n```"
    )


def call_claude(client, meaning_rec, verse, term, model: str):
    user_msg = build_user_msg(meaning_rec, verse, term)
    text_parts = []
    response = None
    with client.messages.stream(
        model=model,
        max_tokens=300,
        output_config={
            "format": {"type": "json_schema", "schema": OUTPUT_SCHEMA},
        },
        system=[{
            "type": "text",
            "text": SYSTEM_PROMPT,
            "cache_control": {"type": "ephemeral"},
        }],
        messages=[{"role": "user", "content": user_msg}],
    ) as stream:
        for text in stream.text_stream:
            text_parts.append(text)
        response = stream.get_final_message()
    raw = "".join(text_parts).strip()
    parsed = json.loads(raw)
    return parsed, response


def main():
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

    ap = argparse.ArgumentParser()
    ap.add_argument("--meanings",
                    default=os.path.join(
                        OUT_DIR,
                        "m26-meanings-claude-sonnet-4-6-20260509.jsonl"
                    ),
                    help="Step A output JSONL")
    ap.add_argument("--model", default="claude-sonnet-4-6")
    ap.add_argument("--subgroup", default=None,
                    help="Filter to one sub-group code, e.g. M26-A")
    ap.add_argument("--limit", type=int, default=None)
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    if not args.dry_run and not os.getenv("ANTHROPIC_API_KEY"):
        print("ERROR: ANTHROPIC_API_KEY not set", file=sys.stderr)
        return 2

    if not Path(args.meanings).exists():
        print(f"ERROR: Step A JSONL not found: {args.meanings}",
              file=sys.stderr)
        return 2

    os.makedirs(OUT_DIR, exist_ok=True)
    today = today_compact()
    sg_tag = f"-{args.subgroup}" if args.subgroup else ""
    jsonl_path = os.path.join(
        OUT_DIR, f"m26-subject-{args.model}{sg_tag}-{today}.jsonl"
    )
    err_path = os.path.join(
        OUT_DIR, f"m26-subject-errors-{args.model}{sg_tag}-{today}.jsonl"
    )

    meanings = load_meanings(args.meanings)
    print(f"Step A meanings loaded: {len(meanings)}")

    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    vr_ids = {m["vr_id"] for m in meanings}
    mti_ids = {m["mti_term_id"] for m in meanings}
    verses, terms = load_verse_and_term_meta(conn, vr_ids, mti_ids)
    conn.close()

    if args.subgroup:
        meanings = [m for m in meanings
                    if terms.get(m["mti_term_id"], {}).get("sg_code")
                    == args.subgroup]
        print(f"Filtered to sub-group {args.subgroup}: {len(meanings)}")

    done = load_completed_keys(jsonl_path)
    if done:
        print(f"Resuming — {len(done)} already in {jsonl_path}")

    todo = [m for m in meanings
            if (m["vr_id"], m["mti_term_id"]) not in done]
    if args.limit:
        todo = todo[: args.limit]
    print(f"To process this run: {len(todo)}")
    print(f"Output: {jsonl_path}")

    if args.dry_run:
        if todo:
            m = todo[0]
            v = verses[m["vr_id"]]
            t = terms[m["mti_term_id"]]
            print()
            print("=== DRY RUN — first record ===")
            print(build_user_msg(m, v, t))
        return 0

    from anthropic import Anthropic
    client = Anthropic()

    in_tot = out_tot = cache_r_tot = 0
    n_ok = n_err = 0
    subj_counts = {"God": 0, "man": 0, "both": 0, "neither": 0}
    t_start = time.time()

    print(f"Calling {args.model}...\n")
    for i, m in enumerate(todo, 1):
        v = verses.get(m["vr_id"])
        t = terms.get(m["mti_term_id"])
        if not v or not t:
            n_err += 1
            err_record = {
                "vr_id": m["vr_id"],
                "mti_term_id": m["mti_term_id"],
                "error": "verse or term metadata missing",
                "ts": now_iso(),
            }
            with open(err_path, "a", encoding="utf-8") as f:
                f.write(json.dumps(err_record, ensure_ascii=False) + "\n")
            continue

        try:
            parsed, resp = call_claude(client, m, v, t, args.model)
        except Exception as e:
            n_err += 1
            err_record = {
                "vr_id": m["vr_id"],
                "mti_term_id": m["mti_term_id"],
                "reference": v["reference"],
                "error": f"{type(e).__name__}: {e}",
                "ts": now_iso(),
            }
            with open(err_path, "a", encoding="utf-8") as f:
                f.write(json.dumps(err_record, ensure_ascii=False) + "\n")
            print(f"  [{i:4d}/{len(todo)}] X {v['reference']:<14s} "
                  f"{t['strong']:8s} ERROR {type(e).__name__}: {e}")
            continue

        usage = resp.usage
        in_tot += usage.input_tokens
        out_tot += usage.output_tokens
        cache_r_tot += getattr(usage, "cache_read_input_tokens", 0) or 0

        with open(jsonl_path, "a", encoding="utf-8") as f:
            f.write(json.dumps(parsed, ensure_ascii=False) + "\n")
        n_ok += 1
        subj = parsed.get("subject", "?")
        subj_counts[subj] = subj_counts.get(subj, 0) + 1
        print(f"  [{i:4d}/{len(todo)}] + {v['reference']:<14s} "
              f"{t['strong']:8s} {subj:8s} {parsed.get('justification', '')[:50]}")

    elapsed = time.time() - t_start

    if "opus" in args.model:
        in_price, out_price = 15.0, 75.0
    elif "haiku" in args.model:
        in_price, out_price = 1.0, 5.0
    else:
        in_price, out_price = 3.0, 15.0
    cost = (in_tot / 1_000_000) * in_price + (out_tot / 1_000_000) * out_price

    print()
    print("=" * 60)
    print(f"  STEP B-1 (subject) SUMMARY")
    print("=" * 60)
    print(f"  Processed this run:     {n_ok + n_err}")
    print(f"  OK:                     {n_ok}")
    print(f"  Errors:                 {n_err}")
    print(f"  Total in JSONL:         {len(done) + n_ok}")
    print(f"  Subject distribution:")
    for s in ["God", "man", "both", "neither"]:
        print(f"    {s:8s}              {subj_counts.get(s, 0)}")
    print(f"  Tokens in/out/cache:    {in_tot:,} / {out_tot:,} / {cache_r_tot:,}")
    print(f"  Cost (this run):        ${cost:.4f}")
    print(f"  Wall time:              {elapsed:.1f}s "
          f"({elapsed / max(n_ok + n_err, 1):.2f}s/verse)")
    print(f"  Output:                 {jsonl_path}")
    if n_err:
        print(f"  Errors log:             {err_path}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
