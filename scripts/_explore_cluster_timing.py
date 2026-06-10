"""
_explore_cluster_timing.py — READ-ONLY timing analysis of completed L2 verse-read clusters.

Compares M01 (Fear), M02 (Anger), M15 (Wisdom) on:
  - total processing duration (wall-clock span)
  - actual processing time (active work)
  - total wait / gap time (idle)

CRUCIAL: two execution modes are measured differently by the engine log, so the
metrics are computed mode-aware (not naively compared):

  API mode (M01, M15) — Sonnet, unattended, term-driven. Each engine_stream_checkpoint
    cycle is `term:<strongs>` and started_at->completed_at IS the active compute time
    for that term. Cycles run back-to-back; wait = gaps between cycles/sub-runs.

  CC mode (M02) — Opus via Claude Code, attended, batch-driven. Each checkpoint
    (`cc:M02:cycleNN`) is an INSTANTANEOUS ingest (~80 ms). The real work happens
    BETWEEN checkpoints (emit + read + write). So active work = inter-cycle gaps below
    an idle threshold; wait = gaps at/above it (sessions ending, /compact, breaks).

Output: outputs/markdown/cluster-processing-timing-<YYYYMMDD>.md   (read-only; no DB writes)
"""
import os, sqlite3, datetime, statistics

DB = os.path.join('database', 'bible_research.db')
IDLE_THRESHOLD_S = 1800   # 30 min: CC inter-cycle gaps >= this are treated as idle pauses

def P(t):
    return datetime.datetime.strptime(t[:23], '%Y-%m-%dT%H:%M:%S.%f')

def hm(seconds):
    s = int(round(seconds)); h, rem = divmod(s, 3600); m, _ = divmod(rem, 60)
    return f'{h}h {m:02d}m'

def main():
    conn = sqlite3.connect(DB); conn.row_factory = sqlite3.Row
    c = conn.cursor()

    # owning cluster per strongs (to attribute API term-cycles)
    s2cl = {}
    for r in c.execute('SELECT strongs_number, cluster_code FROM mti_terms WHERE cluster_code IS NOT NULL'):
        s2cl.setdefault(r['strongs_number'], r['cluster_code'])

    # all verse-read checkpoints
    cps = list(c.execute("""SELECT run_id, stream_name, started_at, completed_at, rows_written
                            FROM engine_stream_checkpoint
                            WHERE (run_id LIKE 'vrm%' OR run_id LIKE 'ccvrm%')
                              AND completed_at IS NOT NULL ORDER BY started_at"""))

    # bucket into clusters
    api = {'M01': [], 'M15': []}    # API term-cycles
    cc = {'M02': []}                # CC ingest checkpoints
    for r in cps:
        sn = r['stream_name'] or ''
        if sn.startswith('term:'):
            cl = s2cl.get(sn.split(':', 1)[1])
            if cl in api:
                api[cl].append(r)
        elif sn.startswith('cc:'):
            cc['M02'].append(r)

    def meaning_count(cl):
        return list(c.execute("SELECT COUNT(*) FROM finding WHERE cluster_code=? AND provenance='l2_meaning'", (cl,)))[0][0]
    def api_findings(cl):
        return list(c.execute("SELECT COUNT(*) FROM finding WHERE cluster_code=? AND provenance='l2_api'", (cl,)))[0][0]

    rows_out = []   # (cluster, mode, n_cycles, total_s, active_s, wait_s, meanings, l2api, notes)

    # ---- API clusters ----
    for cl in ('M01', 'M15'):
        rs = api[cl]
        starts = [P(r['started_at']) for r in rs]
        comps = [P(r['completed_at']) for r in rs]
        total = (max(comps) - min(starts)).total_seconds()
        active = sum((P(r['completed_at']) - P(r['started_at'])).total_seconds() for r in rs)
        wait = total - active
        rows_out.append((cl, 'API (Sonnet, unattended)', len(rs), total, active, wait,
                         meaning_count(cl), api_findings(cl),
                         'active = sum of per-term compute; wait = inter-cycle/sub-run gaps'))

    # ---- CC cluster (M02) ----
    rs = cc['M02']
    starts = [P(r['started_at']) for r in rs]
    total = (max(starts) - min(starts)).total_seconds()
    gaps = [(starts[i+1] - starts[i]).total_seconds() for i in range(len(starts)-1)]
    active = sum(g for g in gaps if g < IDLE_THRESHOLD_S)
    idle = sum(g for g in gaps if g >= IDLE_THRESHOLD_S)
    big = [g for g in gaps if g >= IDLE_THRESHOLD_S]
    rows_out.append(('M02', 'CC (Opus, attended)', len(rs), total, active, idle,
                     meaning_count('M02'), api_findings('M02'),
                     f'active = batch gaps <30m (read+write); wait = {len(big)} pauses >=30m'))

    # ---- write report ----
    today = datetime.date.today().strftime('%Y%m%d')
    out = os.path.join('outputs', 'markdown', f'cluster-processing-timing-{today}.md')
    L = []
    L.append('# L2 Verse-Read — Processing Timing: M01 vs M02 vs M15')
    L.append('')
    L.append(f'> Read-only engine-log analysis. Generated {datetime.date.today().isoformat()}. '
             f'Source: `engine_stream_checkpoint`. **Mode-aware** — the two execution modes are measured '
             f'differently by the engine, so the metrics below are computed per-mode, not naively compared (see notes).')
    L.append('')
    L.append('## Headline comparison')
    L.append('')
    L.append('| Cluster | Mode | Cycles | Total duration | Actual processing | Wait / gap | Utilisation |')
    L.append('|---|---|---:|---:|---:|---:|---:|')
    for cl, mode, n, total, active, wait, *_ in rows_out:
        util = 100 * active / total if total else 0
        L.append(f'| **{cl}** | {mode} | {n} | {hm(total)} | {hm(active)} | {hm(wait)} | {util:.0f}% |')
    L.append('')

    L.append('## Per-cluster detail')
    L.append('')
    names = {'M01': 'Fear', 'M02': 'Anger', 'M15': 'Wisdom'}
    for cl, mode, n, total, active, wait, meanings, l2api, note in rows_out:
        L.append(f'### {cl} ({names[cl]}) — {mode}')
        L.append('')
        L.append(f'- Cycles: **{n}**  ·  meanings written: **{meanings:,}**  ·  tier findings (l2_api): **{l2api:,}**')
        L.append(f'- **Total duration (wall-clock span):** {hm(total)} ({total/3600:.2f} h)')
        L.append(f'- **Actual processing time:** {hm(active)} ({active/3600:.2f} h)')
        L.append(f'- **Total wait / gap time:** {hm(wait)} ({wait/3600:.2f} h)')
        if active:
            L.append(f'- Throughput: **{meanings/(active/60):.1f} meanings/min** of active work  ·  {meanings/n:.1f} meanings/cycle')
        L.append(f'- _Note:_ {note}')
        L.append('')

    L.append('## Reading the numbers')
    L.append('')
    L.append('- **The modes are not directly comparable on wall-clock.** M01/M15 ran as an '
             'unattended Sonnet API job (near-continuous, ~95–100% utilisation — actual ≈ total). '
             'M02 ran attended through Claude Code/Opus, human-paced, so roughly half its wall-clock '
             'was idle waiting (sessions ending, `/compact`, breaks) — that idle is human pacing, not engine slowness.')
    L.append('- **Fair "active work" comparison** (engine compute for API; read+write for CC): '
             + ', '.join(f'{cl} {hm(a)}' for cl, m, n, t, a, w, *_ in rows_out) + '.')
    L.append('- **Per-meaning active cost:** '
             + ', '.join(f'{cl} {a/max(meanings,1):.1f}s' for cl, m, n, t, a, w, meanings, *_ in rows_out)
             + ' (CC/Opus is the costliest per meaning — it writes the prose by hand; the API streams it).')
    L.append('')
    with open(out, 'w', encoding='utf-8') as fh:
        fh.write('\n'.join(L))
    print(f'wrote {out}\n')
    for cl, mode, n, total, active, wait, *_ in rows_out:
        print(f'  {cl}: total {hm(total)} | active {hm(active)} | wait {hm(wait)} | {100*active/total:.0f}% util ({mode})')


if __name__ == '__main__':
    main()
