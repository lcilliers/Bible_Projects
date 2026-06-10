# L2 Verse-Read — Processing Timing: M01 vs M02 vs M15

> Read-only engine-log analysis. Generated 2026-06-10. Source: `engine_stream_checkpoint`. **Mode-aware** — the two execution modes are measured differently by the engine, so the metrics below are computed per-mode, not naively compared (see notes).

## Headline comparison

| Cluster | Mode | Cycles | Total duration | Actual processing | Wait / gap | Utilisation |
|---|---|---:|---:|---:|---:|---:|
| **M01** | API (Sonnet, unattended) | 91 | 5h 03m | 4h 49m | 0h 13m | 95% |
| **M15** | API (Sonnet, unattended) | 86 | 7h 25m | 7h 24m | 0h 00m | 100% |
| **M02** | CC (Opus, attended) | 97 | 11h 56m | 5h 50m | 6h 05m | 49% |

## Per-cluster detail

### M01 (Fear) — API (Sonnet, unattended)

- Cycles: **91**  ·  meanings written: **1,036**  ·  tier findings (l2_api): **23,160**
- **Total duration (wall-clock span):** 5h 03m (5.06 h)
- **Actual processing time:** 4h 49m (4.83 h)
- **Total wait / gap time:** 0h 13m (0.23 h)
- Throughput: **3.6 meanings/min** of active work  ·  11.4 meanings/cycle
- _Note:_ active = sum of per-term compute; wait = inter-cycle/sub-run gaps

### M15 (Wisdom) — API (Sonnet, unattended)

- Cycles: **86**  ·  meanings written: **1,734**  ·  tier findings (l2_api): **38,903**
- **Total duration (wall-clock span):** 7h 25m (7.42 h)
- **Actual processing time:** 7h 24m (7.40 h)
- **Total wait / gap time:** 0h 00m (0.02 h)
- Throughput: **3.9 meanings/min** of active work  ·  20.2 meanings/cycle
- _Note:_ active = sum of per-term compute; wait = inter-cycle/sub-run gaps

### M02 (Anger) — CC (Opus, attended)

- Cycles: **97**  ·  meanings written: **703**  ·  tier findings (l2_api): **15,482**
- **Total duration (wall-clock span):** 11h 56m (11.94 h)
- **Actual processing time:** 5h 50m (5.85 h)
- **Total wait / gap time:** 6h 05m (6.09 h)
- Throughput: **2.0 meanings/min** of active work  ·  7.2 meanings/cycle
- _Note:_ active = batch gaps <30m (read+write); wait = 4 pauses >=30m

## Reading the numbers

- **The modes are not directly comparable on wall-clock.** M01/M15 ran as an unattended Sonnet API job (near-continuous, ~95–100% utilisation — actual ≈ total). M02 ran attended through Claude Code/Opus, human-paced, so roughly half its wall-clock was idle waiting (sessions ending, `/compact`, breaks) — that idle is human pacing, not engine slowness.
- **Fair "active work" comparison** (engine compute for API; read+write for CC): M01 4h 49m, M15 7h 24m, M02 5h 50m.
- **Per-meaning active cost:** M01 16.8s, M15 15.4s, M02 30.0s (CC/Opus is the costliest per meaning — it writes the prose by hand; the API streams it).
