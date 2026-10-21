"""Gate-1 onboarding audit — pre/post accountability for the orphan-term additions.

Every gate-1 onboarding stamps the new mti_terms with anchor_note='gate1-onboard-2026'.
This tool lets you (a) capture a BASELINE census of any DB (use the pre-onboarding backup),
and (b) REPORT: enumerate every stamped addition, compare live totals to the baseline, and
DETECT COLLATERAL — any change to pre-existing (non-gate1) data.

Usage:
  # baseline from the true pre-onboarding backup
  python scripts/_audit_gate1_additions_v1_20260706.py --baseline \
      --db backups/bible_research.pre-salvation-onboard-20260706T150356Z.db \
      --out outputs/integrity/gate1_baseline.json

  # reconciliation against the live DB
  python scripts/_audit_gate1_additions_v1_20260706.py --report \
      --baseline-file outputs/integrity/gate1_baseline.json \
      --out outputs/markdown/... (writes MD to stdout if no --out)
"""
import sqlite3, json, argparse, os

STAMP = 'gate1-onboard-2026'
LIVE = 'database/bible_research.db'

def census(db):
    c = sqlite3.connect(db); c.row_factory = sqlite3.Row
    def one(q, a=()): return c.execute(q, a).fetchone()[0]
    cen = {
        'mti_active':  one("SELECT COUNT(*) FROM mti_terms WHERE COALESCE(delete_flagged,0)=0"),
        'mti_all':     one("SELECT COUNT(*) FROM mti_terms"),
        'inv_owner':   one("SELECT COUNT(*) FROM wa_term_inventory WHERE term_owner_type='OWNER' AND COALESCE(delete_flagged,0)=0"),
        'inv_active':  one("SELECT COUNT(*) FROM wa_term_inventory WHERE COALESCE(delete_flagged,0)=0"),
        'vr_active':   one("SELECT COUNT(*) FROM wa_verse_records WHERE COALESCE(delete_flagged,0)=0"),
        'vc_active':   one("SELECT COUNT(*) FROM verse_context WHERE COALESCE(delete_flagged,0)=0") if _has(c,'verse_context','delete_flagged') else one("SELECT COUNT(*) FROM verse_context"),
        'word_registry': one("SELECT COUNT(*) FROM word_registry"),
        'file_index':  one("SELECT COUNT(*) FROM wa_file_index"),
        # gate1 stamped ACTIVE terms (baseline should be 0)
        'gate1_stamped': one("SELECT COUNT(*) FROM mti_terms WHERE anchor_note=? AND COALESCE(delete_flagged,0)=0", (STAMP,)),
    }
    # per-registry active OWNER-term count (to detect collateral flagging in existing registries)
    cen['per_reg_terms'] = {str(r['owning_registry_fk']): r['n'] for r in c.execute(
        "SELECT owning_registry_fk, COUNT(*) n FROM mti_terms WHERE COALESCE(delete_flagged,0)=0 GROUP BY owning_registry_fk")}
    c.close()
    return cen

def _has(c, tbl, col):
    return any(r[1] == col for r in c.execute(f"PRAGMA table_info({tbl})"))

def report(baseline):
    c = sqlite3.connect(LIVE); c.row_factory = sqlite3.Row
    live = census(LIVE)
    # itemise every stamped addition
    rows = c.execute("""
        SELECT m.strongs_number, m.owning_word, m.owning_registry_fk, wr.word AS reg_word,
               m.cluster_code, m.status, m.delete_flagged
        FROM mti_terms m LEFT JOIN word_registry wr ON wr.id = m.owning_registry_fk
        WHERE m.anchor_note = ? ORDER BY wr.word, m.strongs_number""", (STAMP,)).fetchall()
    adds = []
    for r in rows:
        d = dict(r)
        # verse-records + VC for this strong under this registry
        d['vr'] = c.execute("""SELECT COUNT(*) FROM wa_verse_records vr JOIN mti_terms mt ON mt.id=vr.mti_term_id
            WHERE mt.strongs_number=? AND mt.owning_registry_fk=? AND COALESCE(vr.delete_flagged,0)=0""",
            (r['strongs_number'], r['owning_registry_fk'])).fetchone()[0]
        adds.append(d)
    c.close()

    L = []
    L.append(f"# Gate-1 onboarding audit — reconciliation report\n")
    L.append(f"> Stamp: `anchor_note='{STAMP}'`. Baseline = pre-onboarding census. Live = current DB.\n")
    L.append("## Global deltas (baseline → live)\n")
    L.append("| metric | baseline | live | delta |")
    L.append("|---|---:|---:|---:|")
    for k in ['word_registry','file_index','mti_active','mti_all','inv_owner','inv_active','vr_active','vc_active','gate1_stamped']:
        b = baseline.get(k, 0); v = live.get(k, 0)
        L.append(f"| {k} | {b} | {v} | {v-b:+d} |")
    L.append("")
    # collateral check: existing (non-gate1) active mti should be baseline.mti_active unchanged
    stamped = live['gate1_stamped']
    nongate1_live = live['mti_active'] - stamped
    collateral = nongate1_live - baseline['mti_active']
    L.append("## Collateral check (existing data integrity)\n")
    L.append(f"- gate1-stamped active terms (live): **{stamped}**")
    L.append(f"- non-gate1 active terms (live): {nongate1_live}  vs baseline active {baseline['mti_active']}  →  **delta {collateral:+d}**")
    L.append(f"- {'✅ NO collateral — existing terms preserved' if collateral==0 else '⚠ COLLATERAL: existing terms changed count — investigate'}\n")
    # per-registry collateral: any existing registry whose active count DROPPED
    L.append("### Per-registry active-term change (existing registries only; drops = collateral)\n")
    drops = []
    for reg, bn in baseline['per_reg_terms'].items():
        ln = live['per_reg_terms'].get(reg, 0)
        # subtract stamped additions to that reg
        if ln < bn:
            drops.append((reg, bn, ln))
    if drops:
        for reg, bn, ln in drops:
            L.append(f"- ⚠ reg {reg}: {bn} → {ln} (DROPPED {bn-ln})")
    else:
        L.append("- ✅ no existing registry lost active terms")
    L.append("")
    # itemised additions grouped by registry
    L.append(f"## Additions itemised — {len(adds)} terms across {len(set(a['owning_registry_fk'] for a in adds))} registries\n")
    L.append("| registry | strong | gloss | cluster | status | active? | verse-records |")
    L.append("|---|---|---|---|---|---|---:|")
    for a in adds:
        act = 'yes' if not a['delete_flagged'] else 'NO(flagged)'
        L.append(f"| {a['reg_word']} ({a['owning_registry_fk']}) | {a['strongs_number']} | {a['owning_word']} | {a['cluster_code'] or '—'} | {a['status'] or '—'} | {act} | {a['vr']} |")
    L.append("")
    L.append(f"**Totals:** {len(adds)} terms, {sum(a['vr'] for a in adds)} verse-records.")
    return "\n".join(L)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--baseline', action='store_true')
    ap.add_argument('--report', action='store_true')
    ap.add_argument('--db', default=LIVE)
    ap.add_argument('--baseline-file', default='outputs/integrity/gate1_baseline.json')
    ap.add_argument('--out')
    a = ap.parse_args()
    if a.baseline:
        cen = census(a.db)
        os.makedirs(os.path.dirname(a.baseline_file), exist_ok=True)
        json.dump(cen, open(a.baseline_file, 'w'), indent=1)
        print(f"baseline census from {a.db} -> {a.baseline_file}")
        print(f"  mti_active={cen['mti_active']} inv_owner={cen['inv_owner']} vr_active={cen['vr_active']} "
              f"word_registry={cen['word_registry']} gate1_stamped(baseline)={cen['gate1_stamped']}")
    elif a.report:
        baseline = json.load(open(a.baseline_file))
        md = report(baseline)
        if a.out:
            os.makedirs(os.path.dirname(a.out), exist_ok=True)
            open(a.out, 'w', encoding='utf-8').write(md)
            print(f"report -> {a.out}")
        else:
            print(md)
    else:
        ap.error("choose --baseline or --report")

if __name__ == '__main__':
    main()
