# Exegesis-gate dry-count — how many verses would route to the L1.5 Logos gate

- **File:** wa-exegesis-gate-drycount-v1-20260626.md · **2026-06-26 · Author:** Claude Code.
- **What:** READ-ONLY dry-run of the tuned VE engine `derive()` over the corpus, counting how many **verses** trip a **mechanical** exegesis-gate trigger. **No DB write.** Harness: `scripts/_probe_exegesis_gate_drycount_20260626.py`.

## What "gated by exegesis" means here (and the honest limit)

The L1.5 gate (pilot review §4) has **four** triggers: figurative/somatic-metaphor · distributed-movement · heavy-UNRESOLVED · theologically-loaded. Only **two are mechanically detectable** by the current engine, so these counts are a **lower bound** for distributed + a **proxy** for heavy-UNRESOLVED:

| Trigger | Mechanical? | How detected |
|---|---|---|
| distributed-movement | ✅ yes | a unit emits `isolable=no` (verse opens with a causal/coordinating conjunction → must be read WITH the preceding verse) |
| heavy-UNRESOLVED | ✅ proxy | count of `UNRESOLVED` / `pending-read` values across the verse's units (threshold is a judgement) |
| figurative / somatic-metaphor | ❌ no | interpretive — surfaces only in the read (e.g. "clean hands"=conduct) |
| theologically-loaded | ❌ no | interpretive — surfaces only in the read |

So the **true** gated set is **≥** these numbers (the two interpretive triggers add more on top, found during the read).

## Results

### Whole DB (all clusters) — 19,425 distinct verses · 42,175 units · 0 errors · 19.2s

| Trigger | Verses | % |
|---|---:|---:|
| distributed (`isolable=no`) | 2,811 | 14.5% |
| UNRESOLVED ≥1 field | 12,752 | 65.6% |
| UNRESOLVED ≥2 fields | 7,685 | 39.6% |
| UNRESOLVED ≥3 fields | 4,485 | 23.1% |
| **GATED (isolable=no OR UNRES≥2)** | **9,401** | **48.4%** |

### M12 (Purity) — the active pilot/sweep cluster — 1,596 verses · 1,686 units · 0 errors

| Trigger | Verses | % |
|---|---:|---:|
| distributed (`isolable=no`) | 181 | 11.3% |
| UNRESOLVED ≥1 field | 1,106 | 69.3% |
| UNRESOLVED ≥2 fields | 270 | 16.9% |
| UNRESOLVED ≥3 fields | 19 | 1.2% |
| **GATED (isolable=no OR UNRES≥2)** | **411** | **25.8%** |

## Reading

- **The gated count is threshold-dominated.** Whole-DB heavy-UNRESOLVED swings 66% → 40% → 23% as the bar moves ≥1 → ≥2 → ≥3. The `isolable=no` (distributed) trigger is stable and unambiguous (~14.5% DB / 11.3% M12) — that is the **hard** gate; the UNRESOLVED bar is a **tunable** dial.
- **Distributed alone is the cleanest number:** ~2,811 verses DB-wide / 181 in M12 *must* be read with their neighbour — independent of any threshold.
- **The interpretive triggers (figurative, theologically-loaded) are not in these numbers** — they push the true gated set higher, but only the read finds them.
- M12's gated proportion (25.8% at iso-or-≥2) is **lower** than the DB average (48.4%) — M12 is comparatively well-resolved by the mechanics (the dissection was tuned on it), so other clusters will gate harder.

## Open decision (for the researcher)

The combined "GATED" row uses **UNRES≥2** as the heavy bar. That threshold is a judgement, not a fact — the table gives ≥1/≥2/≥3 so you can set it. Once set, the gate's pending→done→released lifecycle (synthesis-B §2b) governs which verses block L2.
