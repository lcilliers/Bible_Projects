"""
report.py
─────────
Word overview report — engine.py --report [--registry=N]

Prints a structured summary of a word's Phase 1 data to stdout.
Optionally exports to Markdown or CSV.

Sections:
  1 — Registry header (word, source_list, phase1_status, counts)
  2 — wa_file_index entries
  3 — Terms (wa_term_inventory: strongs, gloss, occurrence, testament, meanings)
  4 — Quality flags (wa_data_quality_flags)
  5 — Audit state (latest word_run_state)
  6 — Verse record summary (by term, by testament)
"""

from __future__ import annotations

import json
from datetime import datetime, timezone


def print_word_report(conn, registry_id: int,
                      format: str = "text",
                      out=None) -> None:
    """Print a complete word overview report.

    Args:
        conn:         Open database connection.
        registry_id:  word_registry.no for the target word.
        format:       'text' (default) or 'markdown'.
        out:          File-like object; defaults to sys.stdout.
    """
    import sys
    out = out or sys.stdout

    def p(line: str = "") -> None:
        print(line, file=out)

    def h1(title: str) -> None:
        if format == "markdown":
            p(f"# {title}")
        else:
            p(f"\n{'='*70}")
            p(f"  {title}")
            p(f"{'='*70}")

    def h2(title: str) -> None:
        if format == "markdown":
            p(f"\n## {title}")
        else:
            p(f"\n── {title} {'─' * (60 - len(title))}")

    def kv(key: str, val) -> None:
        if val is None:
            val = "(null)"
        p(f"  {key:<28} {val}")

    # ── Section 1: Registry ────────────────────────────────────────────────────
    reg_row = conn.execute(
        "SELECT * FROM word_registry WHERE no = ?", (registry_id,)
    ).fetchone()
    if not reg_row:
        p(f"[ERROR] No word_registry row for no={registry_id}")
        return

    h1(f"Word Report — {reg_row['word']} (registry no={registry_id})")
    p(f"  Generated: {datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%S')} UTC")

    h2("Registry")
    kv("word", reg_row["word"])
    kv("registry id", reg_row["id"])
    kv("registry no", reg_row["no"])
    kv("source_list", reg_row["source_list"])
    kv("category_hint", reg_row["category_hint"])
    kv("phase1_status", reg_row["phase1_status"])
    kv("phase1_term_count", reg_row["phase1_term_count"])
    kv("phase1_verse_count", reg_row["phase1_verse_count"])
    kv("automation_eligible", reg_row["automation_eligible"])
    kv("last_automation_run", reg_row["last_automation_run"])
    kv("automation_run_id", reg_row["automation_run_id"])
    kv("phase1_input_file", reg_row["phase1_input_file"])

    # ── Section 2: File index ─────────────────────────────────────────────────
    fi_rows = conn.execute(
        "SELECT * FROM wa_file_index WHERE registry_id = ? ORDER BY id",
        (str(registry_id),),
    ).fetchall()

    h2(f"File Index ({len(fi_rows)} entries)")
    for fi in fi_rows:
        p(f"  id={fi['id']}  {fi['filename']}")
        p(f"    specification: {fi['specification']}  phase: {fi['phase']}")
        p(f"    testament_coverage: {fi['testament_coverage']}  "
          f"produced_date: {fi['produced_date']}")
        p(f"    is_split: {fi['is_split']}  "
          f"part: {fi['part_number']}/{fi['total_parts']}")

    if not fi_rows:
        p("  (no file_index entries)")
        return

    file_ids = [fi["id"] for fi in fi_rows]

    # ── Section 3: Terms ──────────────────────────────────────────────────────
    terms = conn.execute(
        """SELECT ti.id, ti.strongs_number, ti.term_id, ti.language,
                  ti.transliteration, ti.step_search_gloss, ti.occurrence_count,
                  ti.occurrence_count_qualifier, ti.testament, ti.meaning,
                  ti.short_def_mounce,
                  (SELECT COUNT(*) FROM wa_verse_records vr WHERE vr.term_inv_id = ti.id
                   AND (vr.span_strong_match = 1 OR vr.span_strong_match IS NULL)) AS verse_count_confirmed,
                  (SELECT COUNT(*) FROM wa_verse_records vr WHERE vr.term_inv_id = ti.id
                   AND vr.span_strong_match = 0) AS verse_count_filtered
           FROM wa_term_inventory ti
           WHERE ti.file_id IN ({})
           ORDER BY ti.id""".format(",".join("?" * len(file_ids))),
        file_ids,
    ).fetchall()

    h2(f"Terms ({len(terms)})")
    for t in terms:
        strongs = t["strongs_number"] or t["term_id"]
        occ = t["occurrence_count"]
        occ_q = t["occurrence_count_qualifier"]
        occ_str = f"{occ_q} {occ}" if occ_q else str(occ) if occ else "?"
        p(f"  [{strongs}] {t['transliteration']}  '{t['step_search_gloss']}'"
          f"  ({t['language']})")
        p(f"    occurrences: {occ_str}  testament: {t['testament']}")
        p(f"    verses stored (confirmed): {t['verse_count_confirmed']}")
        if t["verse_count_filtered"]:
            p(f"    verses filtered: {t['verse_count_filtered']}")
        if t["short_def_mounce"]:
            p(f"    Mounce: {t['short_def_mounce'][:100]}")
        if t["meaning"]:
            first_line = t["meaning"].splitlines()[0][:100]
            p(f"    meaning: {first_line}{'…' if len(t['meaning']) > 100 else ''}")

    # ── Section 4: Quality flags ───────────────────────────────────────────────
    flags = conn.execute(
        """SELECT dqf.term_id, qft.flag_group, qft.flag_code, dqf.description
           FROM wa_data_quality_flags dqf
           JOIN wa_quality_flag_types qft ON qft.id = dqf.flag_id
           WHERE dqf.file_id IN ({})
           ORDER BY qft.flag_group, qft.flag_code""".format(
            ",".join("?" * len(file_ids))),
        file_ids,
    ).fetchall()

    h2(f"Quality Flags ({len(flags)})")
    if flags:
        for fl in flags:
            t_id = fl["term_id"] or "(file-level)"
            p(f"  [{fl['flag_group']}] {fl['flag_code']:35} term: {t_id}")
            if fl["description"]:
                wrapped = _wrap(fl["description"], 70, "      ")
                p(f"      {wrapped}")
    else:
        p("  (none)")

    # ── Section 5: Audit state ─────────────────────────────────────────────────
    audit_row = conn.execute(
        """SELECT run_id, phase_reached, audit_result, audit_detail, stop_reason
           FROM word_run_state WHERE registry_id = ?
           ORDER BY id DESC LIMIT 1""",
        (str(registry_id).zfill(3),),
    ).fetchone()

    h2("Latest Audit")
    if audit_row:
        kv("run_id", audit_row["run_id"])
        kv("phase_reached", audit_row["phase_reached"])
        kv("audit_result", audit_row["audit_result"])
        if audit_row["stop_reason"]:
            kv("stop_reason", audit_row["stop_reason"])
        if audit_row["audit_detail"]:
            try:
                checks = json.loads(audit_row["audit_detail"])
                non_pass = {k: v for k, v in checks.items() if v.get("r") != "PASS"}
                if non_pass:
                    p("  Non-PASS checks:")
                    for check_id, info in non_pass.items():
                        p(f"    {check_id}: [{info.get('r')}] {info.get('d', '')}")
            except (json.JSONDecodeError, TypeError, AttributeError):
                pass
    else:
        p("  (no audit run recorded)")

    # ── Section 6: Verse summary ───────────────────────────────────────────────
    h2("Verse Summary")
    for fi in fi_rows:
        p(f"  file_id={fi['id']}:")
        by_term = conn.execute(
            """SELECT vr.term_id, vr.testament,
                      SUM(CASE WHEN vr.span_strong_match = 1 OR vr.span_strong_match IS NULL THEN 1 ELSE 0 END) AS confirmed,
                      SUM(CASE WHEN vr.span_strong_match = 0 THEN 1 ELSE 0 END) AS filtered
               FROM wa_verse_records vr
               WHERE vr.file_id = ?
               GROUP BY vr.term_id, vr.testament
               ORDER BY vr.term_id, vr.testament""",
            (fi["id"],),
        ).fetchall()
        for btr in by_term:
            tid = btr['term_id'] or '(null)'
            tst = btr['testament'] or '?'
            p(f"    {tid:12} {tst:3}  "
              f"confirmed={btr['confirmed']}  filtered={btr['filtered']}")
        if not by_term:
            p("    (no verse records)")

    p()


def _wrap(text: str, width: int, indent: str = "") -> str:
    """Simple word-wrap helper."""
    words = text.split()
    lines, line = [], []
    for w in words:
        if sum(len(x) + 1 for x in line) + len(w) > width:
            lines.append(" ".join(line))
            line = [w]
        else:
            line.append(w)
    if line:
        lines.append(" ".join(line))
    return f"\n{indent}".join(lines)
