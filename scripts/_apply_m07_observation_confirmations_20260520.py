"""M07 Phase 11 — confirm the 5 carry-forward observations based on synthesis.

Synthesis appendix surfaced each observation explicitly:
- INTEGRATION_NOTE CHAR-1 → Theme 1
- INTER_RELATIONSHIP CHAR-5 ↔ M06 → Theme 2
- INTER_RELATIONSHIP CHAR-6 ↔ M12 → Theme 3
- CROSS_CLUSTER_HANDOFF M09 Pro 16:19 → referenced in Theme 6 + appendix context
- CROSS_CLUSTER_HANDOFF M09 Pro 29:23 → referenced in Theme 6 + appendix context

Updates status open → confirmed with resolution_note citing the
appendix theme.
"""
import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

import sqlite3
from datetime import datetime, timezone
from pathlib import Path

DB = Path('database/bible_research.db')
NOW = datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
SOURCE = 'Sessions/Session_Clusters/M07/WA-M07-phase9-cluster-synthesis-appendix-v1-20260520.md'

UPDATES = [
    ('INTEGRATION_NOTE', 'CHAR-1 volume-split across M07-A / M07-B / M07-C',
     "CONFIRMED via synthesis Theme 1 (The CHAR-1 Volume-Split: Three Registers, One Characteristic). The appendix established the analytical coherence holding the three registers together as one inner-being faculty manifesting in distinct moral-direction contexts (unjust-wound, moral-consequence, divine-encounter). Volume-split per §8.0 rule 2 validated."),
    ('INTER_RELATIONSHIP', 'M07-G shame ↔ M06 contempt as relational complements',
     "CONFIRMED via synthesis Theme 2 (The M06 ↔ M07 Contempt-Shame Relational Pair). The appendix articulated the bidirectional contempt-shame dynamic: M06 holds the projection face; M07-G holds the recipient face. The mechanism is one phenomenon viewed from two cluster perspectives. M06's eventual Phase 9 will see the contempt side; Phase 9 T6 prompts in this cluster carry the relationship explicitly."),
    ('INTER_RELATIONSHIP', 'M07-H innocence ↔ M12 purity as structural counters to shame',
     "CONFIRMED via synthesis Theme 3 (The M12 ↔ M07 Innocence-Purity Polarity). The appendix established the structural function: innocence is the moral state that shields against guilt-shame; its absence sustains the shamed condition. Niq.qa.von / qe.ha.von remain in M07 because every verse evidences the innocence-shame polarity directly; M12 carries the broader purity register."),
    ('CROSS_CLUSTER_HANDOFF', 'M09 pickup note: Pro 16:19 sha.phel (set-aside at Phase 8.5)',
     "CONFIRMED as a handoff to M09. Synthesis appendix (Theme 6 Shame Removed vs Shame Imposed) acknowledged the verse as the canonical M09 voluntary-lowliness case and confirmed its set-aside from M07 as analytically correct. The handoff stands; M09 session-start prep should pick up Pro 16:19 under sha.phel (H8213) when M09 opens."),
    ('CROSS_CLUSTER_HANDOFF', 'M09 pickup note: Pro 29:23 sha.phel (kept in M07-D at Phase 8.5; M09 dimension present)',
     "CONFIRMED as a Phase 9 T6 carry-forward. The verse pairs M07 enforced-humiliation with M09 voluntary-lowliness in one proverb; synthesis appendix referenced the cross-cluster pairing. Handoff to M09 stands; sha.phel at Pro 29:23 may need secondary pickup in M09 as a shared-anchor cross-cluster case."),
]

conn = sqlite3.connect(DB)
conn.row_factory = sqlite3.Row
cur = conn.cursor()

cur.execute('BEGIN')
try:
    for obs_type, title, note in UPDATES:
        row = cur.execute(
            "SELECT id, status FROM cluster_observation "
            "WHERE cluster_code='M07' AND observation_type=? AND title=?",
            (obs_type, title),
        ).fetchone()
        if not row:
            raise SystemExit(f"FAIL: {obs_type} '{title}' not found")
        print(f"obs#{row['id']} ({obs_type}: {title[:50]:.50}) pre={row['status']!r}")
        cur.execute(
            "UPDATE cluster_observation "
            "SET status='confirmed', resolution_note=?, resolved_date=?, "
            "last_updated_date=? "
            "WHERE id=?",
            (note, NOW, NOW, row['id']),
        )
    conn.commit()
    print(f"\nCommitted: {len(UPDATES)} observation status updates.")
except Exception:
    conn.rollback()
    print("ROLLED BACK")
    raise

# Verify
print()
print("=== M07 cluster_observation status (post) ===")
for r in cur.execute(
    "SELECT id, observation_type, status FROM cluster_observation "
    "WHERE cluster_code='M07' AND COALESCE(delete_flagged,0)=0 ORDER BY id"
).fetchall():
    print(f"  obs#{r['id']:>3} {r['observation_type']:<24} {r['status']}")
conn.close()
