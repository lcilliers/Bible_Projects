"""_assess_qa_method_quality_review.py — qualitative-review-oriented Q&A coverage.

Restructured from `_assess_qa_method_effectiveness.py` per researcher direction
(2026-04-28): "I read the text of the question and answers to assess if it is
valid; statistics only plays a part to discover trends that is not contextual.
I am in particular interested in generic questions with low or no answer
coverage; answers that is attributed to multiple questions."

Output:
  research/investigations/wa-qa-quality-review-{YYYYMMDD}.md
  research/investigations/wa-qa-quality-review-{YYYYMMDD}.json

Scope:
  - Universal generic catalogue ONLY (Sections 1-5 → 155 questions).
    Word-specific Extensions and Evidence-Flag Q-COV-* are excluded —
    they're different categories with their own purpose.
  - All words at session_b_status='Analysis Complete' or 'Session B Complete'.

Sections of the report:

  §A — Coverage gaps. Three sub-tables:
       A.1 Questions never addressed (0 word answers) — full text per Q.
       A.2 Questions addressed by 1 word — full text + the one answer.
       A.3 Questions addressed by 2 words — full text + both answers
            side-by-side (where comparison starts to be meaningful).

  §B — Reused answers (same answer text across multiple questions for one
       word). Indicator that AI may be paraphrasing or generalising rather
       than answering each question on its own merits. Per case shows:
         - The reused answer text (full)
         - The list of questions it was attached to (with full question text)

  §C — Fully-addressed questions (3+ word answers). For each, the question
       and all word answers stacked — these are the cross-word comparison
       points the catalogue is designed to produce.

Read-only against `database/bible_research.db`.

Usage:
  python scripts/_assess_qa_method_quality_review.py
  python scripts/_assess_qa_method_quality_review.py --max-answer-chars 1200
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


def truncate(s: str | None, n: int) -> str:
    if not s:
        return ""
    s = s.strip()
    if len(s) <= n:
        return s
    return s[: n - 1].rstrip() + "…"


def get_words(conn) -> list:
    rows = conn.execute("""
        SELECT id, no, word, session_b_status
          FROM word_registry
         WHERE session_b_status IN ('Analysis Complete', 'Session B Complete')
         ORDER BY no
    """).fetchall()
    return [dict(r) for r in rows]


def get_universal_questions(conn) -> list:
    """Section 1-5 questions only — the 'universal catalogue' the readiness
    sweep includes for every word."""
    rows = conn.execute("""
        SELECT obs_id, question_code, section, question_text
          FROM wa_obs_question_catalogue
         WHERE (deleted = 0 OR deleted IS NULL)
           AND section LIKE 'Section %'
         ORDER BY section, obs_id
    """).fetchall()
    return [dict(r) for r in rows]


def get_qa_links(conn) -> list:
    rows = conn.execute("""
        SELECT fcl.id AS link_id, fcl.question_id, fcl.coverage,
               fcl.session_b_note, f.finding_id, wr.no AS registry_no, wr.word
          FROM wa_finding_catalogue_links fcl
          JOIN wa_session_b_findings f ON f.id = fcl.finding_id
          JOIN word_registry wr ON wr.id = f.registry_id
         WHERE wr.session_b_status IN ('Analysis Complete', 'Session B Complete')
           AND (fcl.delete_flagged = 0 OR fcl.delete_flagged IS NULL)
    """).fetchall()
    return [dict(r) for r in rows]


def section_sort_key(section: str) -> tuple:
    section = section or ""
    if section.startswith("Section "):
        try:
            n = int(section.split()[1].rstrip("—:").strip())
            return (0, n, section)
        except (ValueError, IndexError):
            pass
    return (1, 0, section)


def render_md(data: dict, max_answer_chars: int) -> str:
    L = []
    meta = data["meta"]
    words = data["words"]

    L.append("# Q&A Method Quality Review — Coverage Gaps and Reused Answers")
    L.append("")
    L.append(f"_Generated {meta['generated_at']}_  ·  _DB schema {meta['schema_version']}_")
    L.append("")
    L.append("**Scope:** universal generic catalogue (Sections 1-5 only — 155 questions). "
             "Word-specific Extensions and Evidence-Flag Q-COV are excluded as separate categories.")
    L.append("")
    L.append(f"**Words analysed:** {len(words)} — " + ", ".join(f"R{w['no']:03d} {w['word']}" for w in words))
    L.append("")
    L.append("---")
    L.append("")

    # Quick coverage summary (statistical orientation only — researcher reads text below)
    L.append("## Coverage at a glance")
    L.append("")
    L.append("| Word answer count | Questions |")
    L.append("|---:|---:|")
    for k in sorted(data["coverage_distribution"].keys()):
        L.append(f"| {k} word(s) | {data['coverage_distribution'][k]} |")
    L.append(f"| **Total universal questions** | **155** |")
    L.append("")
    L.append("---")
    L.append("")

    # ── §A — Coverage gaps ────────────────────────────────────────────────
    L.append("## §A — Coverage gaps in the universal catalogue")
    L.append("")
    L.append("Questions where the catalogue method has produced limited or no")
    L.append("cross-word data. Read each question's text to judge whether the")
    L.append("question itself is well-formed, whether it's word-specific in disguise,")
    L.append("or whether the analysed words simply don't exhibit the property asked")
    L.append("about.")
    L.append("")

    # A.1 — never addressed
    a1 = data["never_addressed"]
    L.append(f"### §A.1 Questions never addressed ({len(a1)} of 155 — {len(a1)/155*100:.0f}%)")
    L.append("")
    if not a1:
        L.append("_None — every universal question has at least one word's answer._")
        L.append("")
    else:
        L.append("These got no answer from any of the analysed words.")
        L.append("")
        for q in sorted(a1, key=lambda x: (section_sort_key(x["section"]), x["question_code"])):
            L.append(f"#### `{q['question_code']}` — {q['section']}")
            L.append("")
            L.append(f"> {q['question_text']}")
            L.append("")

    # A.2 — single word
    a2 = data["single_word_addressed"]
    L.append(f"### §A.2 Questions addressed by only 1 word ({len(a2)} of 155 — {len(a2)/155*100:.0f}%)")
    L.append("")
    if a2:
        for q in sorted(a2, key=lambda x: (section_sort_key(x["question"]["section"]), x["question"]["question_code"])):
            qtext = q["question"]
            ans = q["answer"]
            L.append(f"#### `{qtext['question_code']}` — {qtext['section']}")
            L.append("")
            L.append(f"**Question:** {qtext['question_text']}")
            L.append("")
            L.append(f"**R{ans['registry_no']:03d} {ans['word']}** — `{ans['coverage']}`")
            L.append("")
            for line in truncate(ans["session_b_note"], max_answer_chars).split("\n"):
                L.append(f"> {line}")
            L.append("")

    # A.3 — two words
    a3 = data["two_word_addressed"]
    L.append(f"### §A.3 Questions addressed by 2 words ({len(a3)} of 155 — {len(a3)/155*100:.0f}%)")
    L.append("")
    if a3:
        for q in sorted(a3, key=lambda x: (section_sort_key(x["question"]["section"]), x["question"]["question_code"])):
            qtext = q["question"]
            answers = q["answers"]
            L.append(f"#### `{qtext['question_code']}` — {qtext['section']}")
            L.append("")
            L.append(f"**Question:** {qtext['question_text']}")
            L.append("")
            for ans in sorted(answers, key=lambda a: a["registry_no"]):
                L.append(f"**R{ans['registry_no']:03d} {ans['word']}** — `{ans['coverage']}`")
                L.append("")
                for line in truncate(ans["session_b_note"], max_answer_chars).split("\n"):
                    L.append(f"> {line}")
                L.append("")
    L.append("---")
    L.append("")

    # ── §B — Reused answers ────────────────────────────────────────────────
    L.append("## §B — Reused answers (same text attributed to multiple questions)")
    L.append("")
    L.append("Each entry below shows a single answer text that AI attached to")
    L.append("two or more distinct catalogue questions for the same word. May")
    L.append("indicate: (a) the questions are too similar (refine catalogue),")
    L.append("(b) the answer is generic where a question-specific answer was needed,")
    L.append("or (c) bookkeeping shortcut (legitimate when one observation supports")
    L.append("genuinely different questions on the same evidence). Read each case.")
    L.append("")
    reused = data["reused_answers"]
    if not reused:
        L.append("_No reused-answer cases detected at the 200-char prefix threshold._")
        L.append("")
    else:
        L.append(f"**{len(reused)} case(s) detected.**")
        L.append("")
        for i, case in enumerate(reused, 1):
            L.append(f"### Case {i} — R{case['registry_no']:03d} {case['word']}: same answer attached to {len(case['questions'])} questions")
            L.append("")
            L.append("**Reused answer text:**")
            L.append("")
            for line in truncate(case["answer_text"], max_answer_chars).split("\n"):
                L.append(f"> {line}")
            L.append("")
            L.append("**Attached to these questions:**")
            L.append("")
            for q in case["questions"]:
                L.append(f"- `{q['question_code']}` ({q['section']}): {q['question_text']}")
            L.append("")
    L.append("---")
    L.append("")

    # ── §C — Fully-addressed questions (3+ words) ─────────────────────────
    L.append(f"## §C — Fully-addressed questions ({len(data['multi_word_addressed'])}+ word answers each)")
    L.append("")
    L.append("These are the cross-word comparison points the catalogue is")
    L.append("designed to produce. Read all answers in parallel to see whether")
    L.append("the answers are genuinely comparable or whether each word is")
    L.append("answering on its own terms with the question merely as a prompt.")
    L.append("")
    multi = data["multi_word_addressed"]
    if multi:
        for q in sorted(multi, key=lambda x: (section_sort_key(x["question"]["section"]), x["question"]["question_code"])):
            qtext = q["question"]
            answers = q["answers"]
            L.append(f"### `{qtext['question_code']}` — {qtext['section']}")
            L.append("")
            L.append(f"**Question:** {qtext['question_text']}")
            L.append("")
            for ans in sorted(answers, key=lambda a: a["registry_no"]):
                L.append(f"**R{ans['registry_no']:03d} {ans['word']}** — `{ans['coverage']}`")
                L.append("")
                for line in truncate(ans["session_b_note"], max_answer_chars).split("\n"):
                    L.append(f"> {line}")
                L.append("")
    L.append("---")
    L.append("")
    L.append(f"_End of report. Answer text truncated to {max_answer_chars} chars in this view; "
             "full text is in the companion .json._")

    return "\n".join(L)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default=DB_PATH)
    ap.add_argument("--out-dir", default=OUT_DIR)
    ap.add_argument("--max-answer-chars", type=int, default=1500,
                    help="Truncate answer text to this many chars in the .md (full in .json)")
    args = ap.parse_args()

    conn = sqlite3.connect(args.db)
    conn.row_factory = sqlite3.Row

    schema_version = conn.execute(
        "SELECT version_code FROM schema_version ORDER BY id DESC LIMIT 1"
    ).fetchone()[0]

    words = get_words(conn)
    questions = get_universal_questions(conn)
    qa_links = get_qa_links(conn)
    questions_by_id = {q["obs_id"]: q for q in questions}

    # Group answers by (question_id, registry, note_prefix) — dedup
    grouped = {}
    for r in qa_links:
        if r["question_id"] not in questions_by_id:
            continue  # not a universal generic question
        note = r.get("session_b_note") or ""
        key = (r["question_id"], r["registry_no"], note[:200])
        if key not in grouped:
            grouped[key] = {
                "registry_no": r["registry_no"],
                "word": r["word"],
                "coverage": r["coverage"],
                "session_b_note": note,
                "source_findings": [],
            }
        if r["finding_id"] and r["finding_id"] not in grouped[key]["source_findings"]:
            grouped[key]["source_findings"].append(r["finding_id"])
        rank = {"full": 4, "partial": 3, "not_applicable": 2, "no_finding": 1}
        if rank.get(r["coverage"], 0) > rank.get(grouped[key]["coverage"], 0):
            grouped[key]["coverage"] = r["coverage"]

    # Per-question answer aggregation
    answers_per_q = defaultdict(list)
    for (qid, _reg, _key), entry in grouped.items():
        answers_per_q[qid].append(entry)

    # Categorize questions by # of word answers
    never_addressed = []
    single_word_addressed = []
    two_word_addressed = []
    multi_word_addressed = []
    coverage_distribution = defaultdict(int)
    for q in questions:
        ans = answers_per_q.get(q["obs_id"], [])
        n = len({a["registry_no"] for a in ans})
        coverage_distribution[n] += 1
        if n == 0:
            never_addressed.append(q)
        elif n == 1:
            single_word_addressed.append({"question": q, "answer": ans[0]})
        elif n == 2:
            two_word_addressed.append({"question": q, "answers": ans})
        else:
            multi_word_addressed.append({"question": q, "answers": ans})

    # Reused answers detection: within each registry, look for note_prefix that
    # appears for multiple distinct question_ids
    reused = []
    by_reg_prefix = defaultdict(list)
    for (qid, reg_no, prefix), entry in grouped.items():
        # Skip very short notes (likely "Not applicable" boilerplate)
        if len(prefix) < 80:
            continue
        by_reg_prefix[(reg_no, prefix)].append((qid, entry))
    for (reg_no, prefix), entries in by_reg_prefix.items():
        if len({qid for qid, _ in entries}) > 1:
            sample = entries[0][1]
            reused.append({
                "registry_no": reg_no,
                "word": sample["word"],
                "answer_text": sample["session_b_note"],
                "questions": [
                    {
                        "question_code": questions_by_id[qid]["question_code"],
                        "question_text": questions_by_id[qid]["question_text"],
                        "section": questions_by_id[qid]["section"],
                    }
                    for qid, _ in entries
                ],
            })

    data = {
        "meta": {
            "generated_at": now_iso(),
            "schema_version": schema_version,
            "max_answer_chars": args.max_answer_chars,
            "scope": "Universal generic catalogue (Sections 1-5 only)",
        },
        "words": words,
        "coverage_distribution": dict(coverage_distribution),
        "never_addressed": never_addressed,
        "single_word_addressed": single_word_addressed,
        "two_word_addressed": two_word_addressed,
        "multi_word_addressed": multi_word_addressed,
        "reused_answers": reused,
    }

    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    today = today_compact()

    md_path = out_dir / f"wa-qa-quality-review-{today}.md"
    json_path = out_dir / f"wa-qa-quality-review-{today}.json"

    md_path.write_text(render_md(data, args.max_answer_chars), encoding="utf-8")
    json_path.write_text(json.dumps(data, indent=2, ensure_ascii=False, default=str), encoding="utf-8")

    print(f"Wrote: {md_path}  ({md_path.stat().st_size/1024:.1f} KB)")
    print(f"Wrote: {json_path}  ({json_path.stat().st_size/1024:.1f} KB)")
    print()
    print("Coverage distribution (universal generic catalogue, 155 questions):")
    for k in sorted(coverage_distribution.keys()):
        print(f"  {k} word answer(s): {coverage_distribution[k]} questions")
    print()
    print(f"Never addressed:                 {len(never_addressed)}")
    print(f"Addressed by 1 word:             {len(single_word_addressed)}")
    print(f"Addressed by 2 words:            {len(two_word_addressed)}")
    print(f"Addressed by 3+ words:           {len(multi_word_addressed)}")
    print(f"Reused-answer cases:             {len(reused)}")

    conn.close()
    return 0


if __name__ == "__main__":
    sys.exit(main())
