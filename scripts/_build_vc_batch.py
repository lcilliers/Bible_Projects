"""
_build_vc_batch.py
──────────────────
Build a Verse Context batch JSON per WA-VerseContext-Instruction v1.5 Section 5.3.

Usage:
    python scripts/_build_vc_batch.py [--batch-id VCB-001] [--target-min 2000] [--target-max 2500]
"""
import sqlite3
import json
import os
import argparse
from datetime import date

DB_PATH = os.path.join('data', 'bible_research.db')
OUTPUT_DIR = os.path.join('data', 'exports', 'verse_context')

def get_eligible_terms(conn):
    """Get all OWNER terms needing Verse Context classification, ordered by owning_registry_fk.

    Uses a subquery to get the correct per-term_inv_id verse count (not inflated by
    cross-registry appearances of the same Strong's number).
    """
    return conn.execute('''
        SELECT mt.id as mti_term_id, mt.strongs_number, mt.transliteration, mt.gloss,
               mt.language, mt.status as mti_status, mt.owning_registry_fk,
               ti.id as term_inv_id, ti.term_owner_type,
               wr.no as registry_no, wr.word as registry_word,
               wr.verse_context_status,
               (SELECT COUNT(*) FROM wa_verse_records vr
                WHERE vr.term_inv_id = ti.id AND vr.delete_flagged = 0) as verse_count
        FROM mti_terms mt
        JOIN wa_term_inventory ti ON ti.strongs_number = mt.strongs_number
          AND ti.term_owner_type = 'OWNER' AND ti.delete_flagged = 0
        JOIN wa_file_index fi ON fi.id = ti.file_id
        JOIN word_registry wr ON wr.id = fi.word_registry_fk
        WHERE mt.delete_flagged = 0
          AND mt.status IN ('extracted', 'extracted_thin')
          AND NOT EXISTS (
              SELECT 1 FROM verse_context vc
              WHERE vc.mti_term_id = mt.id AND vc.delete_flagged = 0
          )
          AND (SELECT COUNT(*) FROM wa_verse_records vr
               WHERE vr.term_inv_id = ti.id AND vr.delete_flagged = 0) > 0
        ORDER BY mt.owning_registry_fk ASC, mt.strongs_number ASC
    ''').fetchall()


def select_batch_terms(terms_raw, target_min, target_max):
    """Accumulate terms up to target verse count. Never split a term."""
    selected = []
    cumulative = 0
    skipped_large = []

    for t in terms_raw:
        vc = t['verse_count']
        if vc > target_max:
            d2 = dict(t)
            d2['registry_verse_context_status'] = d2.get('verse_context_status')
            skipped_large.append(d2)
            continue
        if cumulative + vc > target_max and cumulative >= target_min:
            break
        if cumulative + vc > target_max:
            continue
        d = dict(t)
        d['registry_verse_context_status'] = d.get('verse_context_status')
        selected.append(d)
        cumulative += vc

    return selected, cumulative, skipped_large


def build_term_entry(conn, term):
    """Build the full term entry with existing groups and all verses."""
    mti_id = term['mti_term_id']
    ti_id = term['term_inv_id']

    # Existing groups (all, including delete_flagged)
    groups_raw = conn.execute('''
        SELECT id, group_code, context_description, notes, delete_flagged
        FROM verse_context_group WHERE mti_term_id = ?
    ''', (mti_id,)).fetchall()

    existing_groups = []
    for g in groups_raw:
        anchor_count = conn.execute(
            'SELECT COUNT(*) FROM verse_context WHERE group_id = ? AND is_anchor = 1 AND delete_flagged = 0',
            (g['id'],)).fetchone()[0]
        related_count = conn.execute(
            'SELECT COUNT(*) FROM verse_context WHERE group_id = ? AND is_related = 1 AND delete_flagged = 0',
            (g['id'],)).fetchone()[0]
        existing_groups.append({
            "id": g['id'],
            "group_code": g['group_code'],
            "context_description": g['context_description'],
            "notes": g['notes'],
            "delete_flagged": g['delete_flagged'],
            "anchor_count": anchor_count,
            "related_count": related_count
        })

    # All verse records (including delete_flagged for revision history)
    verses_raw = conn.execute('''
        SELECT vr.id as verse_record_id, vr.reference, vr.verse_text,
               vr.target_word, vr.span_strong_match, vr.delete_flagged as verse_delete_flagged
        FROM wa_verse_records vr
        WHERE vr.term_inv_id = ?
        ORDER BY vr.book_id, vr.chapter, vr.verse_num
    ''', (ti_id,)).fetchall()

    verses = []
    unclassified_count = 0
    for v in verses_raw:
        vc_row = conn.execute('''
            SELECT id, group_id, is_anchor, is_relevant, is_related, notes, delete_flagged
            FROM verse_context WHERE verse_record_id = ? AND mti_term_id = ?
        ''', (v['verse_record_id'], mti_id)).fetchone()

        if vc_row:
            gc = None
            if vc_row['group_id']:
                gc_row = conn.execute(
                    'SELECT group_code FROM verse_context_group WHERE id = ?',
                    (vc_row['group_id'],)).fetchone()
                gc = gc_row['group_code'] if gc_row else None
            verse_context = {
                "id": vc_row['id'],
                "group_id": vc_row['group_id'],
                "group_code": gc,
                "is_anchor": vc_row['is_anchor'],
                "is_relevant": vc_row['is_relevant'],
                "is_related": vc_row['is_related'],
                "notes": vc_row['notes'],
                "delete_flagged": vc_row['delete_flagged']
            }
        else:
            verse_context = None
            if v['verse_delete_flagged'] == 0:
                unclassified_count += 1

        verses.append({
            "verse_record_id": v['verse_record_id'],
            "reference": v['reference'],
            "verse_text": v['verse_text'],
            "target_word": v['target_word'],
            "span_strong_match": v['span_strong_match'],
            "verse_delete_flagged": v['verse_delete_flagged'],
            "verse_context": verse_context
        })

    total_active = sum(1 for v in verses if v['verse_delete_flagged'] == 0)
    classification_complete = (unclassified_count == 0) and (total_active > 0)

    return {
        "mti_term_id": mti_id,
        "strongs_number": term['strongs_number'],
        "transliteration": term['transliteration'],
        "gloss": term['gloss'],
        "language": term['language'],
        "mti_status": term['mti_status'],
        "term_owner_type": "OWNER",
        "owning_registry_id": term['registry_no'],
        "owning_registry_word": term['registry_word'],
        "registry_verse_context_status": term['registry_verse_context_status'],
        "term_classification_complete": classification_complete,
        "total_verses": total_active,
        "unclassified_count": unclassified_count,
        "existing_groups": existing_groups,
        "verses": verses
    }, total_active, unclassified_count


def main():
    parser = argparse.ArgumentParser(description='Build Verse Context batch JSON')
    parser.add_argument('--batch-id', default='VCB-001')
    parser.add_argument('--target-min', type=int, default=2000)
    parser.add_argument('--target-max', type=int, default=2500)
    args = parser.parse_args()

    os.makedirs(OUTPUT_DIR, exist_ok=True)

    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row

    today = date.today().isoformat()
    batch_num = args.batch_id.replace('VCB-', '').replace('vcb-', '')

    print(f"Building batch {args.batch_id}...")

    # Select terms
    terms_raw = get_eligible_terms(conn)
    print(f"  Eligible terms: {len(terms_raw)}")

    selected, cumulative, skipped_large = select_batch_terms(
        terms_raw, args.target_min, args.target_max)
    print(f"  Selected: {len(selected)} terms, {cumulative} verses")
    if skipped_large:
        print(f"  Skipped (>{args.target_max} verses, need dedicated batch): {len(skipped_large)}")

    # Build batch structure
    batch = {
        "batch_id": args.batch_id,
        "produced_date": today,
        "produced_by": "Claude Code \u2014 WA-VerseContext-Instruction v2.3",
        "governing_instruction": "WA-VerseContext-Instruction-v2.3-20260401.md",
        "total_verse_count": 0,
        "total_term_count": len(selected),
        "unclassified_verse_count": 0,
        "verse_context_summary": {
            "total_verses_in_batch": 0,
            "previously_classified": 0,
            "unclassified": 0,
            "set_aside_in_prior_batches": 0,
            "anchor_verses_existing": 0
        },
        "terms": []
    }

    total_verses = 0
    total_unclassified = 0

    for i, term in enumerate(selected):
        entry, active, unclassified = build_term_entry(conn, term)
        batch["terms"].append(entry)
        total_verses += active
        total_unclassified += unclassified
        if (i + 1) % 20 == 0:
            print(f"  Processed {i+1}/{len(selected)} terms...")

    batch["total_verse_count"] = total_verses
    batch["unclassified_verse_count"] = total_unclassified
    batch["verse_context_summary"]["total_verses_in_batch"] = total_verses
    batch["verse_context_summary"]["unclassified"] = total_unclassified

    # Write
    filename = f"wa-vcb-{batch_num.zfill(3)}-extract-{today.replace('-', '')}.json"
    outpath = os.path.join(OUTPUT_DIR, filename)
    with open(outpath, 'w', encoding='utf-8') as f:
        json.dump(batch, f, indent=2, ensure_ascii=False)

    fsize = os.path.getsize(outpath)
    print(f"\n  Written: {outpath}")
    print(f"  File size: {fsize:,} bytes ({fsize/1024/1024:.1f} MB)")

    # Registry summary
    reg_summary = {}
    for t in batch['terms']:
        key = f"{t['owning_registry_id']:03d}-{t['owning_registry_word']}"
        if key not in reg_summary:
            reg_summary[key] = {'terms': 0, 'verses': 0}
        reg_summary[key]['terms'] += 1
        reg_summary[key]['verses'] += t['total_verses']

    print(f"\n  BATCH {args.batch_id} SUMMARY")
    print(f"  Terms: {batch['total_term_count']}")
    print(f"  Verses: {batch['total_verse_count']}")
    print(f"  Unclassified: {batch['unclassified_verse_count']}")
    print(f"  Registries: {len(reg_summary)}")
    print(f"  File: {filename}")
    print()
    for k in sorted(reg_summary.keys()):
        r = reg_summary[k]
        print(f"    {k}: {r['terms']} terms, {r['verses']} verses")

    conn.close()


if __name__ == '__main__':
    main()
