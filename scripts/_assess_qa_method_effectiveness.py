"""_assess_qa_method_effectiveness.py — read-only Q&A coverage extraction.

For every catalogue question, list which analysed words answered it and what
they answered. Companion view to evaluate how effective the Q&A-driven
catalogue method is at producing comparable cross-word findings.

Output:
  research/investigations/wa-qa-method-effectiveness-{YYYYMMDD}.md
  research/investigations/wa-qa-method-effectiveness-{YYYYMMDD}.json

The .md is human-readable; the .json carries the same data for programmatic
re-use. Read-only against `database/bible_research.db`.

Coverage values present in the DB:
  full              — Q&A answered with source observation linked
  partial           — Q&A partially answered with source observation linked
  not_applicable    — Q&A judged not relevant to the word; rationale recorded
  no_finding        — universal Q not surfaced in the analytical session (CC's
                      catalogue completeness sweep filled the gap row)

Usage:
  python scripts/_assess_qa_method_effectiveness.py
  python scripts/_assess_qa_method_effectiveness.py --include-no-finding
  python scripts/_assess_qa_method_effectiveness.py --max-answer-chars 400
"""
from __future__ import annotations

import argparse
import json
import os
import sqlite3
import sys
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

DB_PATH = os.path.join("database", "bible_research.db")
OUT_DIR = os.path.join("research", "investigations")


def now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def today_compact() -> str:
    return datetime.now(timezone.utc).strftime("%Y%m%d")


def get_analysed_words(conn) -> list:
    """Return word_registry rows for all 'Analysis Complete' (or 'Session B Complete') registries."""
    rows = conn.execute("""
        SELECT id, no, word, session_b_status
          FROM word_registry
         WHERE session_b_status IN ('Analysis Complete', 'Session B Complete')
         ORDER BY no
    """).fetchall()
    return [dict(r) for r in rows]


def get_questions(conn) -> list:
    """Return all active catalogue questions."""
    rows = conn.execute("""
        SELECT obs_id, question_code, section, question_text, scope, status,
               source_registry_no, source_word, date_added, catalogue_version
          FROM wa_obs_question_catalogue
         WHERE deleted = 0 OR deleted IS NULL
         ORDER BY section, obs_id
    """).fetchall()
    return [dict(r) for r in rows]


def get_qa_links_with_finding(conn) -> list:
    """Q&A links tied to a source observation (finding_id NOT NULL).

    These are the actual ANSWERED / PARTIAL Q&As where AI produced an answer
    grounded in an explicit source observation.
    """
    rows = conn.execute("""
        SELECT fcl.id AS link_id,
               fcl.question_id, fcl.coverage, fcl.session_b_note, fcl.mapped_date,
               f.id AS finding_pk, f.finding_id, f.registry_id, f.finding_type, f.status,
               wr.no AS registry_no, wr.word
          FROM wa_finding_catalogue_links fcl
          JOIN wa_session_b_findings f ON f.id = fcl.finding_id
          JOIN word_registry wr ON wr.id = f.registry_id
         WHERE wr.session_b_status IN ('Analysis Complete', 'Session B Complete')
           AND (fcl.delete_flagged = 0 OR fcl.delete_flagged IS NULL)
         ORDER BY fcl.question_id, wr.no, fcl.id
    """).fetchall()
    return [dict(r) for r in rows]


def get_null_finding_links(conn) -> list:
    """Q&A links with finding_id IS NULL — not_applicable or no_finding rows.

    These don't have a direct registry FK; we infer registry from the
    session_b_note text where possible (rare case — usually no_finding rows
    are programme-wide catalogue completeness with no specific registry).
    """
    rows = conn.execute("""
        SELECT fcl.id AS link_id,
               fcl.question_id, fcl.coverage, fcl.session_b_note, fcl.mapped_date
          FROM wa_finding_catalogue_links fcl
         WHERE fcl.finding_id IS NULL
           AND (fcl.delete_flagged = 0 OR fcl.delete_flagged IS NULL)
    """).fetchall()
    return [dict(r) for r in rows]


def truncate(s: str | None, n: int) -> str:
    if not s:
        return ""
    s = s.strip()
    if len(s) <= n:
        return s
    return s[: n - 1].rstrip() + "…"


def section_sort_key(section: str) -> tuple:
    """Sort sections: Section 1, Section 2, ... numerically; everything else alphabetically after."""
    section = section or ""
    if section.startswith("Section "):
        try:
            n = int(section.split()[1].rstrip("—:").strip())
            # Prefix '0' to sort numerical sections before non-numerical
            return (0, n, section)
        except (ValueError, IndexError):
            pass
    return (1, 0, section)


def render_md(data: dict, max_answer_chars: int, include_no_finding: bool) -> str:
    L = []
    meta = data["meta"]
    L.append("# Q&A Method Effectiveness — Coverage and Answers Cross-Reference")
    L.append("")
    L.append(f"_Generated {meta['generated_at']}_  ·  _DB schema {meta['schema_version']}_")
    L.append("")
    L.append("**Purpose:** survey the catalogue's Q&A coverage across all words that have")
    L.append("reached Session B Analysis Complete. Each catalogue question is listed with")
    L.append("the words that addressed it (answered, partially answered, or judged not")
    L.append("applicable) and the answer text per word.")
    L.append("")
    L.append("Words included (Analysis Complete):")
    for w in data["words"]:
        L.append(f"- R{w['no']:03d} {w['word']}")
    L.append("")
    L.append("---")
    L.append("")
    L.append("## Summary")
    L.append("")
    s = data["summary"]
    L.append(f"- Active catalogue questions: **{s['questions_total']}**")
    L.append(f"- Words analysed: **{s['words_analysed']}**")
    L.append(f"- Questions addressed by ≥1 word (any coverage): **{s['questions_addressed']}** ({s['pct_addressed']:.1f}% of catalogue)")
    L.append(f"- Questions never addressed by any word: **{s['questions_never_addressed']}**")
    L.append("")
    L.append("**By coverage type (link rows):**")
    L.append("")
    L.append("| Coverage | Count |")
    L.append("|---|---:|")
    for cov in ("full", "partial", "not_applicable", "no_finding"):
        L.append(f"| `{cov}` | {s['by_coverage'].get(cov, 0)} |")
    L.append("")
    L.append("**By word:**")
    L.append("")
    L.append("| Reg | Word | Distinct Qs answered | full | partial | not_applicable | no_finding |")
    L.append("|---:|---|---:|---:|---:|---:|---:|")
    for w in s["by_word"]:
        L.append(f"| {w['no']:03d} | {w['word']} | {w['distinct_qs']} | {w['full']} | {w['partial']} | {w['not_applicable']} | {w['no_finding']} |")
    L.append("")
    L.append("---")
    L.append("")

    # Coverage matrix: question × word
    L.append("## Coverage Matrix — Question × Word")
    L.append("")
    L.append("`F` = full · `P` = partial · `NA` = not applicable · `—` = not addressed by this word")
    L.append("")
    word_headers = " | ".join(f"R{w['no']:03d}" for w in data["words"])
    L.append(f"| Q | Section | {word_headers} |")
    L.append("|---|---|" + "---|" * len(data["words"]))
    for q in sorted(data["questions"], key=lambda x: (section_sort_key(x["section"]), x["question_code"])):
        coverage_per_word = data["coverage_matrix"].get(q["obs_id"], {})
        cells = []
        for w in data["words"]:
            cov = coverage_per_word.get(w["no"])
            cells.append({"full": "F", "partial": "P", "not_applicable": "NA", "no_finding": "·"}.get(cov, "—"))
        section_short = (q["section"] or "")[:28]
        L.append(f"| `{q['question_code']}` | {section_short} | " + " | ".join(cells) + " |")
    L.append("")
    L.append("---")
    L.append("")

    # Per-question detail
    L.append("## Per-Question Detail (with answers per word)")
    L.append("")

    by_section = defaultdict(list)
    for q in data["questions"]:
        by_section[q["section"] or "(no section)"].append(q)

    for section in sorted(by_section.keys(), key=section_sort_key):
        questions_in_section = by_section[section]
        n_addressed = sum(1 for q in questions_in_section if data["coverage_matrix"].get(q["obs_id"]))
        L.append(f"### {section} ({len(questions_in_section)} question(s); {n_addressed} addressed by ≥1 word)")
        L.append("")

        for q in sorted(questions_in_section, key=lambda x: x["question_code"]):
            answers = data["answers_per_question"].get(q["obs_id"], [])
            L.append(f"#### `{q['question_code']}` (obs_id {q['obs_id']})")
            L.append("")
            L.append(f"**Question:** {q['question_text']}")
            L.append("")
            if q.get("source_registry_no"):
                L.append(f"_Source: registry {q['source_registry_no']:03d} ({q.get('source_word') or '?'}); added {q.get('date_added') or '?'}; version {q.get('catalogue_version') or '?'}_")
                L.append("")
            if not answers:
                if include_no_finding:
                    L.append("_Not addressed by any analysed word._")
                else:
                    L.append("_No answers recorded._")
                L.append("")
                continue
            for ans in sorted(answers, key=lambda x: x["registry_no"]):
                sources = ans.get("source_findings") or []
                src_label = ", ".join(f"`{s}`" for s in sources) if sources else "—"
                L.append(f"**R{ans['registry_no']:03d} {ans['word']}** — `{ans['coverage']}` (sources: {src_label})")
                L.append("")
                note = truncate(ans.get("session_b_note"), max_answer_chars)
                for line in note.split("\n"):
                    L.append(f"> {line}")
                L.append("")
        L.append("---")
        L.append("")

    return "\n".join(L)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default=DB_PATH)
    ap.add_argument("--out-dir", default=OUT_DIR)
    ap.add_argument("--max-answer-chars", type=int, default=600,
                    help="Truncate answer text to this many chars in the .md (full text in .json)")
    ap.add_argument("--include-no-finding", action="store_true",
                    help="Also surface questions never addressed by any analysed word")
    args = ap.parse_args()

    conn = sqlite3.connect(args.db)
    conn.row_factory = sqlite3.Row

    # Schema version for the header
    schema_version = conn.execute(
        "SELECT version_code FROM schema_version ORDER BY id DESC LIMIT 1"
    ).fetchone()[0]

    words = get_analysed_words(conn)
    questions = get_questions(conn)
    qa_with_finding = get_qa_links_with_finding(conn)
    qa_null = get_null_finding_links(conn)

    # Dedup: a single Q&A answer may cite multiple source observations (one
    # link row per source obs, all with same session_b_note text). Group by
    # (question_id, registry_no, answer-text-prefix) and collapse source
    # findings into a comma-separated list. This produces a one-row-per-Q&A
    # view rather than one-row-per-source-observation.
    answers_per_question = defaultdict(list)
    coverage_matrix = defaultdict(dict)
    grouped = {}  # (qid, reg_no, note_prefix) -> dict
    for r in qa_with_finding:
        note = r.get("session_b_note") or ""
        # Use first 200 chars as group key — same Q&A answer text would match
        key = (r["question_id"], r["registry_no"], note[:200])
        if key not in grouped:
            grouped[key] = {
                "registry_no": r["registry_no"],
                "word": r["word"],
                "coverage": r["coverage"],
                "session_b_note": note,
                "source_findings": [],
                "finding_type": r["finding_type"],
                "mapped_date": r["mapped_date"],
            }
        # Append source finding if not already present
        if r["finding_id"] and r["finding_id"] not in grouped[key]["source_findings"]:
            grouped[key]["source_findings"].append(r["finding_id"])
        # Promote coverage: full > partial > not_applicable > no_finding
        rank = {"full": 4, "partial": 3, "not_applicable": 2, "no_finding": 1}
        if rank.get(r["coverage"], 0) > rank.get(grouped[key]["coverage"], 0):
            grouped[key]["coverage"] = r["coverage"]

    for (qid, _reg, _key), entry in grouped.items():
        answers_per_question[qid].append(entry)
        prior = coverage_matrix[qid].get(entry["registry_no"])
        if prior is None or rank.get(entry["coverage"], 0) > rank.get(prior, 0):
            coverage_matrix[qid][entry["registry_no"]] = entry["coverage"]

    # Summary stats
    questions_total = len(questions)
    addressed = set(answers_per_question.keys())
    questions_addressed = len(addressed)
    questions_never_addressed = questions_total - questions_addressed
    pct_addressed = (questions_addressed / questions_total * 100) if questions_total else 0

    by_coverage = defaultdict(int)
    for r in qa_with_finding:
        by_coverage[r["coverage"]] += 1
    for r in qa_null:
        by_coverage[r["coverage"]] += 1

    by_word = []
    for w in words:
        # Use deduped grouped answers (one row per Q&A) for the per-word stats
        word_answers = []
        for qid, ans_list in answers_per_question.items():
            for ans in ans_list:
                if ans["registry_no"] == w["no"]:
                    word_answers.append((qid, ans))
        by_word.append({
            "no": w["no"],
            "word": w["word"],
            "distinct_qs": len({qid for qid, _ in word_answers}),
            "full": sum(1 for _, ans in word_answers if ans["coverage"] == "full"),
            "partial": sum(1 for _, ans in word_answers if ans["coverage"] == "partial"),
            "not_applicable": sum(1 for _, ans in word_answers if ans["coverage"] == "not_applicable"),
            "no_finding": sum(1 for _, ans in word_answers if ans["coverage"] == "no_finding"),
        })

    data = {
        "meta": {
            "generated_at": now_iso(),
            "schema_version": schema_version,
            "max_answer_chars": args.max_answer_chars,
        },
        "words": words,
        "questions": questions,
        "summary": {
            "questions_total": questions_total,
            "questions_addressed": questions_addressed,
            "questions_never_addressed": questions_never_addressed,
            "pct_addressed": pct_addressed,
            "words_analysed": len(words),
            "by_coverage": dict(by_coverage),
            "by_word": by_word,
        },
        "answers_per_question": dict(answers_per_question),
        "coverage_matrix": dict(coverage_matrix),
        "null_finding_links": qa_null,
    }

    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    today = today_compact()

    md_path = out_dir / f"wa-qa-method-effectiveness-{today}.md"
    json_path = out_dir / f"wa-qa-method-effectiveness-{today}.json"

    md_path.write_text(
        render_md(data, args.max_answer_chars, args.include_no_finding),
        encoding="utf-8",
    )
    json_path.write_text(
        json.dumps(data, indent=2, ensure_ascii=False, default=str),
        encoding="utf-8",
    )

    md_size = md_path.stat().st_size / 1024
    json_size = json_path.stat().st_size / 1024
    print(f"Wrote: {md_path}  ({md_size:.1f} KB)")
    print(f"Wrote: {json_path}  ({json_size:.1f} KB)")
    print()
    print(f"Catalogue questions: {questions_total}")
    print(f"Words analysed: {len(words)}")
    print(f"Questions addressed by ≥1 word: {questions_addressed} ({pct_addressed:.1f}%)")
    print(f"Questions never addressed: {questions_never_addressed}")
    print()
    print("By coverage:")
    for cov, n in sorted(by_coverage.items(), key=lambda x: -x[1]):
        print(f"  {cov:18s} {n}")
    print()
    print("By word:")
    for w in by_word:
        print(f"  R{w['no']:03d} {w['word']:14s} distinct_Qs={w['distinct_qs']:3d}  full={w['full']:3d}  partial={w['partial']:3d}  na={w['not_applicable']:2d}")

    conn.close()
    return 0


if __name__ == "__main__":
    sys.exit(main())
