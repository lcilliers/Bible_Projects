"""M08 observation lifecycle: close the 5 Phase 8.7 cluster_observation rows
that the Phase 9 synthesis surfaced and addressed.

Mirrors the M07 _apply_m07_observation_confirmations precedent.
"""
import sys, io, sqlite3
from datetime import datetime, timezone
from pathlib import Path

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
DB = Path('database/bible_research.db')
NOW = datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')

CONFIRMATIONS = [
    (10, 'confirmed', "Confirmed in Phase 9. CHAR-1's 4-sub-group volume-split was treated as a single characteristic throughout the per-batch findings and synthesis. The seat-of-pride axis (heart/eyes-bearing/national/general) structured T2 (constitutional location) findings and the per-prompt cluster-synthesis comparisons. CHAR-1 totals: 165 E + 20 S + 4 G."),
    (11, 'confirmed', "Confirmed in Phase 9 — M08-C-VCG-01/02/03 separated condemned self-boasting, Pauline examined-boasting, and God-directed glorying registers. CHAR-3 T6.4 + T7.1 cluster-synthesis findings explicitly articulate the M08↔M22 register-adjacency: same kauchaomai/ha.lal vocabulary expresses both M08 (self-boasting) and M22 (praise-of-God) content; register-distinction is verse-level. When M22 opens, the M08-C-VCG-03 verses are candidates for cross-cluster contribution."),
    (12, 'confirmed', "Confirmed in Phase 9 — M08-E findings articulate strength-misused-as-self-exaltation as the M08↔M23 pairing. CHAR-5 T6 findings name the misuse-of-faculty pattern: M23 carries strength/capacity as inner-being faculty; M08-E carries its corruption when it becomes self-aggrandisement. When M23 opens, M08-E's term list informs which strength terms have a documented misuse-pole at the verse level."),
    (13, 'confirmed', "Confirmed in Phase 9. Phase 5.5 set-aside (174 verses: 122 M22-register + 52 narrative-marker) was respected throughout — no set-aside verses cited as CHAR-N evidence. The conceptual implication (CHAR-1 as the creature's counterfeit of M22's divine register) surfaced in CHAR-1 T0.1, T6.4, and T7.1 findings and the synthesis prose appendix. 174 verses remain recoverable for cross-cluster analysis if M22 picks them up later."),
    (14, 'confirmed', "Confirmed in Phase 9. G0193 akratēs (2Ti 3:3) was successfully integrated into M08-A4-VCG-01 (NT vice-catalogue register) alongside filautos (2Ti 3:2) and huperēfanos (2Ti 3:2). The verse contributes to CHAR-1 findings at T3.6 (volition), T3.9 (conscience), and T6.3.2 (enabling-condition relationship). Phase 8.5 promotion treated as M08-internal supportive-qualifying register, not as a separate characteristic."),
]

conn = sqlite3.connect(DB)
cur = conn.cursor()

print('=== PRE ===')
for obs_id, _, _ in CONFIRMATIONS:
    r = cur.execute('SELECT status, title FROM cluster_observation WHERE id=?', (obs_id,)).fetchone()
    print(f'  obs id={obs_id} status={r[0]!r} title={r[1][:60]}')

print()
print('=== APPLYING ===')
cur.execute('BEGIN')
try:
    for obs_id, new_status, resolution_note in CONFIRMATIONS:
        cur.execute(
            "UPDATE cluster_observation SET status=?, resolution_note=?, resolved_date=?, last_updated_date=? "
            "WHERE id=? AND COALESCE(delete_flagged,0)=0 AND cluster_code='M08'",
            (new_status, resolution_note, NOW, NOW, obs_id),
        )
        assert cur.rowcount == 1, f'obs id={obs_id} not updated'
        print(f'  obs id={obs_id} → {new_status}')
    conn.commit()
    print(f'Committed at {NOW}')
except Exception:
    conn.rollback()
    print('ROLLED BACK')
    raise

print()
print('=== POST ===')
n_open = cur.execute("SELECT COUNT(*) FROM cluster_observation WHERE cluster_code='M08' AND status='open' AND COALESCE(delete_flagged,0)=0").fetchone()[0]
print(f'M08 cluster_observations still open: {n_open} (expected 0)')
assert n_open == 0
print()
print('=== M08 OBSERVATION CLOSURES COMPLETE ===')
conn.close()
