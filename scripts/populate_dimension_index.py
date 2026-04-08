"""
populate_dimension_index.py
───────────────────────────
Populates the wa_dimension_index table from verse_context_group data,
denormalising the full cross-reference chain from group → term → registry.

The `dimension` field is left NULL for Claude AI to classify.
Preliminary mechanical classification is applied where keyword patterns
in the context_description are unambiguous.

Usage:
    python scripts/populate_dimension_index.py
    python scripts/populate_dimension_index.py --clear    # clear and repopulate
    python scripts/populate_dimension_index.py --dry-run  # show counts only
"""
import sqlite3
import argparse
import os
import re
from datetime import date

DB_PATH = os.path.join('data', 'bible_research.db')

# Confirmed dimension vocabulary — v1.6 (WA-DimensionReview-Instruction-v1.6-2026-04-08)
# 11 dimensions. Keyword classifier produces starting hypotheses using these labels.
# Claude AI applies the authoritative assignment during Phase C review.
DIMENSIONS = [
    'Emotion \u2014 Positive',          # 01
    'Emotion \u2014 Negative',          # 02
    'Cognition',                         # 03
    'Volition',                          # 04
    'Moral Character',                   # 05
    'Relational Disposition',            # 06
    'Vitality / Existence',              # 07
    'Transformation',                    # 08
    'Agency / Power',                    # 09
    'Dependence / Creatureliness',       # 10
    'Divine-Human Correspondence',       # 11
]


def classify_dimension(context_description):
    """Attempt mechanical dimension classification from context_description keywords.

    Returns (dimension, confidence) tuple using the v1.6 vocabulary.
    Confidence levels:
        KEYWORD_STRONG  — primary keyword match, high-specificity phrase
        KEYWORD_WEAK    — secondary keyword match, could belong to multiple dimensions
        UNCLASSIFIED    — no keyword match, requires Claude AI assessment
    """
    text = (context_description or '').lower()

    # ── Strong matches — high-specificity phrases ──

    # 11 Divine-Human Correspondence — strong
    if any(w in text for w in ['divine anger', 'divine wrath', 'divine judgment',
                                'divine displeasure', 'divine compassion', 'divine grief',
                                "god's anger", "god's wrath", "god's compassion",
                                "god's delight", "god's response", "god's inner",
                                'divine jealousy', 'divine mercy',
                                'divine-human', 'god and human',
                                'across the divine', 'both god and']):
        return ('Divine-Human Correspondence', 'KEYWORD_STRONG')

    # 01 Emotion — Positive — strong
    if any(w in text for w in ['inner joy', 'inner delight', 'inner satisfaction',
                                'inner gladness', 'inner exultation', 'inner wonder',
                                'inner contentment', 'felt delight']):
        return ('Emotion \u2014 Positive', 'KEYWORD_STRONG')

    # 02 Emotion — Negative — strong
    if any(w in text for w in ['inner anguish', 'inner grief', 'inner sorrow',
                                'inner fear', 'inner terror', 'inner agony',
                                'inner distress', 'inner shame', 'inner anxiety',
                                'inner dread', 'inner bitterness']):
        return ('Emotion \u2014 Negative', 'KEYWORD_STRONG')

    # 03 Cognition — strong
    if any(w in text for w in ['cognitive', 'intellectual', 'reasoning faculty',
                                'mental capacity', 'thought as inner',
                                'inner act of knowing', 'inner perception']):
        return ('Cognition', 'KEYWORD_STRONG')

    # 04 Volition — strong
    if any(w in text for w in ['volitional', 'act of will', 'deliberate choice',
                                'inner resolve', 'inner purposing',
                                'inner act of choosing']):
        return ('Volition', 'KEYWORD_STRONG')

    # 05 Moral Character — strong
    if any(w in text for w in ['moral quality', 'moral character', 'moral nature',
                                'moral disposition', 'stable inner quality',
                                'enduring quality of', 'moral standing']):
        return ('Moral Character', 'KEYWORD_STRONG')

    # 06 Relational Disposition — strong
    if any(w in text for w in ['inner orientation toward', 'relational stance',
                                'oriented toward another', 'inner disposition toward',
                                'compassion toward', 'hostility toward']):
        return ('Relational Disposition', 'KEYWORD_STRONG')

    # 07 Vitality / Existence — strong
    if any(w in text for w in ['animating life', 'breath of life', 'life-force',
                                'fragility of existence', 'post-mortem',
                                'continuation beyond death', 'preciousness of life']):
        return ('Vitality / Existence', 'KEYWORD_STRONG')

    # 08 Transformation — strong
    if any(w in text for w in ['inner transformation', 'renewal of the heart',
                                'circumcision of the heart', 'hardening of the heart',
                                'inner change', 'inner formation',
                                'purification', 'inner deterioration']):
        return ('Transformation', 'KEYWORD_STRONG')

    # 09 Agency / Power — strong
    if any(w in text for w in ['sovereignty', 'exercise of authority',
                                'exercise of power', 'inner capacity exercised',
                                'self-giving', 'deliberate restraint']):
        return ('Agency / Power', 'KEYWORD_STRONG')

    # 10 Dependence / Creatureliness — strong
    if any(w in text for w in ['creaturely dependence', 'humble dependence',
                                'posture of reliance', 'clay before the potter',
                                'acknowledging limitation']):
        return ('Dependence / Creatureliness', 'KEYWORD_STRONG')

    # ── Weak matches — broader keywords ──

    # 01 Emotion — Positive — weak
    if any(w in text for w in ['joy', 'delight', 'gladness', 'contentment',
                                'exultation', 'pleasure', 'satisfaction']):
        return ('Emotion \u2014 Positive', 'KEYWORD_WEAK')

    # 02 Emotion — Negative — weak
    if any(w in text for w in ['anger', 'wrath', 'grief', 'sorrow', 'fear',
                                'dread', 'anguish', 'shame', 'anxiety',
                                'bitterness', 'restlessness', 'distress']):
        return ('Emotion \u2014 Negative', 'KEYWORD_WEAK')

    # 03 Cognition — weak
    if any(w in text for w in ['knowledge', 'understanding', 'wisdom',
                                'reasoning', 'discernment', 'thinking',
                                'mental', 'perception', 'recognition',
                                'memory', 'attentiveness', 'insight']):
        return ('Cognition', 'KEYWORD_WEAK')

    # 04 Volition — weak
    if any(w in text for w in ['choosing', 'decision', 'intention',
                                'determination', 'resolve', 'willing',
                                'purpose', 'desire', 'longing', 'obedience']):
        return ('Volition', 'KEYWORD_WEAK')

    # 05 Moral Character — weak
    if any(w in text for w in ['moral', 'conscience', 'ethical',
                                'righteousness', 'integrity', 'faithfulness',
                                'purity', 'holiness', 'uprightness',
                                'justice', 'goodness', 'truthfulness']):
        return ('Moral Character', 'KEYWORD_WEAK')

    # 06 Relational Disposition — weak
    if any(w in text for w in ['love', 'compassion', 'mercy', 'favour',
                                'grace', 'attachment', 'hostility', 'contempt',
                                'rejection', 'patience toward', 'fellowship',
                                'relational', 'toward others', 'interpersonal']):
        return ('Relational Disposition', 'KEYWORD_WEAK')

    # 07 Vitality / Existence — weak
    if any(w in text for w in ['life', 'death', 'vitality', 'resurrection',
                                'mortal', 'existence', 'breath']):
        return ('Vitality / Existence', 'KEYWORD_WEAK')

    # 08 Transformation — weak
    if any(w in text for w in ['renewal', 'transformation', 'formation',
                                'healing', 'degradation', 'madness',
                                'hardening', 'purified']):
        return ('Transformation', 'KEYWORD_WEAK')

    # 09 Agency / Power — weak
    if any(w in text for w in ['authority', 'power', 'strength', 'dominion',
                                'sovereignty', 'capacity', 'exercise',
                                'self-giving', 'sacrifice', 'calling']):
        return ('Agency / Power', 'KEYWORD_WEAK')

    # 10 Dependence / Creatureliness — weak
    if any(w in text for w in ['humility', 'dependence', 'trust', 'security',
                                'lowliness', 'reliance', 'prayer as',
                                'inadequacy']):
        return ('Dependence / Creatureliness', 'KEYWORD_WEAK')

    # 11 Divine-Human Correspondence — weak
    if any(w in text for w in ['divine', "god's", 'god as subject',
                                'both divine and human']):
        return ('Divine-Human Correspondence', 'KEYWORD_WEAK')

    # Catch-all for sinful/vice language — map to Moral Character (was Sin & Vice)
    if any(w in text for w in ['sinful', 'wickedness', 'transgression',
                                'corruption', 'defilement']):
        return ('Moral Character', 'KEYWORD_WEAK')

    return (None, 'UNCLASSIFIED')


def populate(conn, dry_run=False):
    """Populate wa_dimension_index from verse_context_group + cross-references.

    Groups with manual_override = 1 are preserved — their dimension,
    dimension_confidence, notes, and last_modified are not overwritten.
    New groups (not yet in the index) are always inserted.
    Existing groups with manual_override = 0 are updated with fresh
    mechanical classification.
    """

    # Build set of manually overridden groups (preserve these)
    manual_ids = set(r[0] for r in conn.execute(
        'SELECT verse_context_group_id FROM wa_dimension_index WHERE manual_override = 1'
    ).fetchall())
    if manual_ids:
        print(f"Manual overrides preserved: {len(manual_ids)}")

    # Get all active groups with full cross-reference chain
    groups = conn.execute('''
        SELECT vcg.id as vcg_id, vcg.mti_term_id, vcg.group_code, vcg.context_description,
               mt.strongs_number, mt.transliteration, mt.gloss, mt.language,
               wr.no as reg_no, wr.word as reg_word, wr.cluster_assignment,
               (SELECT COUNT(*) FROM verse_context vc
                WHERE vc.group_id = vcg.id AND vc.is_anchor = 1 AND vc.delete_flagged = 0) as anchor_count,
               (SELECT COUNT(*) FROM verse_context vc
                WHERE vc.group_id = vcg.id AND vc.is_related = 1 AND vc.delete_flagged = 0) as related_count,
               (SELECT COUNT(*) FROM verse_context vc
                WHERE vc.mti_term_id = vcg.mti_term_id AND vc.is_relevant = 0 AND vc.delete_flagged = 0) as set_aside_count,
               (SELECT COUNT(*) FROM verse_context vc
                WHERE vc.group_id = vcg.id AND vc.delete_flagged = 0) as total_verse_count
        FROM verse_context_group vcg
        JOIN mti_terms mt ON mt.id = vcg.mti_term_id AND mt.delete_flagged = 0
        JOIN word_registry wr ON wr.id = mt.owning_registry_fk
        WHERE vcg.delete_flagged = 0
        ORDER BY wr.no, mt.strongs_number, vcg.group_code
    ''').fetchall()

    print(f"Groups to index: {len(groups)}")

    counts = {'KEYWORD_STRONG': 0, 'KEYWORD_WEAK': 0, 'UNCLASSIFIED': 0}
    skipped_manual = 0
    inserted = 0
    updated = 0
    now = date.today().isoformat()

    for g in groups:
        vcg_id = g['vcg_id']

        # Skip manually overridden groups
        if vcg_id in manual_ids:
            skipped_manual += 1
            continue

        dimension, confidence = classify_dimension(g['context_description'])
        counts[confidence] += 1

        if dry_run:
            continue

        # Check if row already exists
        existing = conn.execute(
            'SELECT id FROM wa_dimension_index WHERE verse_context_group_id = ?',
            (vcg_id,)
        ).fetchone()

        if existing:
            # Update existing row (mechanical refresh)
            conn.execute('''
                UPDATE wa_dimension_index SET
                    mti_term_id = ?, strongs_number = ?, transliteration = ?,
                    gloss = ?, language = ?,
                    owning_registry_no = ?, owning_registry_word = ?,
                    cluster_assignment = ?, group_code = ?,
                    context_description = ?, dimension = ?,
                    dimension_confidence = ?,
                    anchor_count = ?, related_count = ?,
                    set_aside_count = ?, total_verse_count = ?,
                    last_modified = ?
                WHERE id = ?
            ''', (
                g['mti_term_id'], g['strongs_number'], g['transliteration'],
                g['gloss'], g['language'],
                g['reg_no'], g['reg_word'], g['cluster_assignment'],
                g['group_code'], g['context_description'], dimension,
                confidence,
                g['anchor_count'], g['related_count'],
                g['set_aside_count'], g['total_verse_count'],
                now, existing[0]
            ))
            updated += 1
        else:
            # Insert new row
            conn.execute('''
                INSERT INTO wa_dimension_index
                    (verse_context_group_id, mti_term_id, strongs_number,
                     transliteration, gloss, language,
                     owning_registry_no, owning_registry_word, cluster_assignment,
                     group_code, context_description, dimension,
                     dimension_confidence, manual_override, last_modified,
                     anchor_count, related_count, set_aside_count, total_verse_count)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, 0, ?, ?, ?, ?, ?)
            ''', (
                vcg_id, g['mti_term_id'], g['strongs_number'],
                g['transliteration'], g['gloss'], g['language'],
                g['reg_no'], g['reg_word'], g['cluster_assignment'],
                g['group_code'], g['context_description'], dimension,
                confidence, now,
                g['anchor_count'], g['related_count'],
                g['set_aside_count'], g['total_verse_count']
            ))
            inserted += 1

    if not dry_run:
        conn.commit()

    total = len(groups)
    print(f"\nResults:")
    print(f"  Inserted:        {inserted}")
    print(f"  Updated:         {updated}")
    print(f"  Manual skipped:  {skipped_manual}")
    print(f"\nClassification:")
    print(f"  KEYWORD_STRONG:  {counts['KEYWORD_STRONG']:>5d} ({counts['KEYWORD_STRONG']/max(total-skipped_manual,1)*100:.1f}%)")
    print(f"  KEYWORD_WEAK:    {counts['KEYWORD_WEAK']:>5d} ({counts['KEYWORD_WEAK']/max(total-skipped_manual,1)*100:.1f}%)")
    print(f"  UNCLASSIFIED:    {counts['UNCLASSIFIED']:>5d} ({counts['UNCLASSIFIED']/max(total-skipped_manual,1)*100:.1f}%)")

    # Dimension distribution
    if not dry_run:
        print("\nDimension distribution:")
        for r in conn.execute('''
            SELECT COALESCE(dimension, 'UNCLASSIFIED') as dim, COUNT(*) as c
            FROM wa_dimension_index WHERE delete_flagged = 0
            GROUP BY dimension ORDER BY c DESC
        '''):
            print(f"  {r[0]:>30s}: {r[1]}")


def main():
    parser = argparse.ArgumentParser(description='Populate wa_dimension_index')
    parser.add_argument('--clear', action='store_true', help='Clear table before populating')
    parser.add_argument('--dry-run', action='store_true', help='Show counts without writing')
    args = parser.parse_args()

    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row

    if args.clear:
        manual_count = conn.execute(
            'SELECT COUNT(*) FROM wa_dimension_index WHERE manual_override = 1'
        ).fetchone()[0]
        conn.execute('DELETE FROM wa_dimension_index WHERE manual_override = 0')
        conn.commit()
        remaining = conn.execute('SELECT COUNT(*) FROM wa_dimension_index').fetchone()[0]
        print(f"Cleared non-manual rows. Preserved {manual_count} manual overrides. {remaining} rows remain.")

    populate(conn, dry_run=args.dry_run)
    conn.close()


if __name__ == '__main__':
    main()
