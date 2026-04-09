"""
backfill_root_families.py
─────────────────────────
Backfill wa_term_root_family from wa_term_related_words data.

Uses connected-component clustering: terms that STEP lists as related to each other
form a root family. Root code derived from shortest transliteration in the family.

Usage:
    python scripts/backfill_root_families.py                # dry-run (report only)
    python scripts/backfill_root_families.py --apply        # insert into database
    python scripts/backfill_root_families.py --registry=98  # single registry
"""
import sqlite3
import argparse
import os
import re
from collections import defaultdict
from datetime import date

DB_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "bible_research.db")


def derive_root_code(family_terms):
    """Derive a root code from the family's terms.

    Strategy:
    - Find the term with the shortest base transliteration (likely the root verb/noun)
    - For Hebrew: extract consonantal skeleton
    - For Greek: strip common suffixes to get the stem
    """
    if not family_terms:
        return "UNKNOWN"

    # Sort by transliteration length
    sorted_terms = sorted(family_terms, key=lambda t: len(t.get("transliteration", "") or ""))
    base = sorted_terms[0]
    translit = (base.get("transliteration") or "").strip()
    language = base.get("language", "")

    # Clean dots, hyphens, brackets
    clean = re.sub(r'[.\-\[\]():]', '', translit).strip()

    if language == "Greek":
        # Strip common Greek suffixes
        lower = clean.lower()
        for suffix in ['omai', 'oō', 'izō', 'euō', 'eō', 'aō', 'oō',
                        'sis', 'mos', 'ma', 'tēs', 'tos', 'os', 'on',
                        'is', 'ia', 'ē', 'a']:
            if lower.endswith(suffix) and len(lower) > len(suffix) + 2:
                clean = clean[:len(clean) - len(suffix)]
                break
        return clean.upper()[:10]
    else:
        # Hebrew/Aramaic: take consonantal form, max 6 chars
        # Remove common prefixes (ma-, me-, mi-, te-)
        lower = clean.lower()
        for prefix in ['ma', 'me', 'mi', 'te', 'ti']:
            if lower.startswith(prefix) and len(lower) > 4:
                # Only strip if the remaining part is 3+ chars
                remainder = lower[len(prefix):]
                if len(remainder) >= 3:
                    # Check if the base Strong's starts with the prefix — if so, keep it
                    base_strongs = base.get("strongs", "")
                    if not base_strongs.endswith(("A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K")):
                        clean = clean[len(prefix):]
                    break

        return clean.upper()[:8] if len(clean) > 8 else clean.upper()


def get_root_language(family_terms):
    """Determine language from the majority of terms."""
    langs = [t.get("language", "?") for t in family_terms]
    from collections import Counter
    most_common = Counter(langs).most_common(1)
    return most_common[0][0] if most_common else "?"


def find_root_families(conn, reg_id):
    """Find root families for a registry using related_words clustering."""

    terms = conn.execute("""
        SELECT ti.id as ti_id, ti.strongs_number, ti.transliteration, ti.language,
               ti.step_search_gloss, ti.word_analysis_gloss
        FROM wa_term_inventory ti
        JOIN wa_file_index fi ON fi.id = ti.file_id
        WHERE fi.word_registry_fk = ?
        AND ti.term_owner_type = 'OWNER' AND ti.delete_flagged = 0
        ORDER BY ti.language, ti.strongs_number
    """, (reg_id,)).fetchall()

    if not terms:
        return []

    registry_strongs = {t["strongs_number"] for t in terms}
    term_info = {}
    adjacency = defaultdict(set)

    for t in terms:
        term_info[t["strongs_number"]] = {
            "ti_id": t["ti_id"],
            "strongs": t["strongs_number"],
            "transliteration": t["transliteration"],
            "gloss": t["step_search_gloss"] or t["word_analysis_gloss"] or "",
            "language": t["language"] or "?",
        }

        related = conn.execute(
            "SELECT strongs_number FROM wa_term_related_words WHERE term_inv_id = ?",
            (t["ti_id"],),
        ).fetchall()

        for r in related:
            if r["strongs_number"] in registry_strongs:
                adjacency[t["strongs_number"]].add(r["strongs_number"])
                adjacency[r["strongs_number"]].add(t["strongs_number"])

    # Connected components
    visited = set()
    families = []

    for strongs in [t["strongs_number"] for t in terms]:
        if strongs in visited:
            continue
        family = set()
        queue = [strongs]
        while queue:
            s = queue.pop(0)
            if s in visited:
                continue
            visited.add(s)
            family.add(s)
            for nb in adjacency.get(s, set()):
                if nb not in visited:
                    queue.append(nb)
        families.append(family)

    # Build result
    result = []
    for family in families:
        family_terms = [term_info[s] for s in sorted(family) if s in term_info]
        if not family_terms:
            continue

        root_code = derive_root_code(family_terms)
        language = get_root_language(family_terms)

        # Root gloss: use the shortest/simplest gloss
        glosses = [t["gloss"] for t in family_terms if t["gloss"]]
        root_gloss = min(glosses, key=len) if glosses else ""

        result.append({
            "root_code": root_code,
            "root_language": language,
            "root_gloss": root_gloss,
            "terms": family_terms,
        })

    return result


def main():
    parser = argparse.ArgumentParser(description="Backfill wa_term_root_family from related_words")
    parser.add_argument("--apply", action="store_true", help="Insert into database (default: dry-run)")
    parser.add_argument("--registry", type=int, help="Process single registry")
    args = parser.parse_args()

    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    today = date.today().isoformat()

    # Get registries to process
    if args.registry:
        regs = conn.execute(
            "SELECT id, no, word FROM word_registry WHERE no = ?", (args.registry,)
        ).fetchall()
    else:
        # All registries without existing root data
        regs = conn.execute("""
            SELECT wr.id, wr.no, wr.word FROM word_registry wr
            WHERE wr.phase1_status != 'Excluded'
            AND wr.id NOT IN (
                SELECT DISTINCT fi.word_registry_fk FROM wa_file_index fi
                JOIN wa_term_inventory ti ON ti.file_id = fi.id
                JOIN wa_term_root_family rf ON rf.term_inv_id = ti.id
            )
            ORDER BY wr.no
        """).fetchall()

    print(f"{'DRY RUN' if not args.apply else 'APPLYING'} — {len(regs)} registries to process")
    print()

    total_families = 0
    total_rows = 0
    total_multi = 0

    for reg in regs:
        families = find_root_families(conn, reg["id"])

        multi = [f for f in families if len(f["terms"]) > 1]
        single = [f for f in families if len(f["terms"]) == 1]

        if not families:
            continue

        rows_for_reg = sum(len(f["terms"]) for f in families)
        total_families += len(families)
        total_multi += len(multi)
        total_rows += rows_for_reg

        print(f"Reg {reg['no']:4d} ({reg['word']:20s}): {len(families)} families "
              f"({len(multi)} multi, {len(single)} single) = {rows_for_reg} rows")

        if args.apply:
            for family in families:
                for term in family["terms"]:
                    # Check not already exists
                    existing = conn.execute(
                        "SELECT 1 FROM wa_term_root_family WHERE term_inv_id = ? AND root_code = ?",
                        (term["ti_id"], family["root_code"]),
                    ).fetchone()
                    if existing:
                        continue

                    conn.execute("""
                        INSERT INTO wa_term_root_family
                        (term_inv_id, root_code, root_language, root_gloss, note)
                        VALUES (?, ?, ?, ?, ?)
                    """, (
                        term["ti_id"],
                        family["root_code"],
                        family["root_language"],
                        family["root_gloss"],
                        f"Backfilled {today} from wa_term_related_words clustering",
                    ))
            conn.commit()

    print()
    print(f"Total: {total_families} families ({total_multi} multi-term), {total_rows} rows")

    if args.apply:
        new_total = conn.execute("SELECT COUNT(*) FROM wa_term_root_family").fetchone()[0]
        new_roots = conn.execute("SELECT COUNT(DISTINCT root_code) FROM wa_term_root_family").fetchone()[0]
        regs_covered = conn.execute("""
            SELECT COUNT(DISTINCT fi.word_registry_fk) FROM wa_file_index fi
            JOIN wa_term_inventory ti ON ti.file_id = fi.id
            JOIN wa_term_root_family rf ON rf.term_inv_id = ti.id
        """).fetchone()[0]
        print(f"\nPost-backfill: {new_total} total rows, {new_roots} distinct roots, {regs_covered} registries covered")

    conn.close()


if __name__ == "__main__":
    main()
