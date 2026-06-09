# Finding correction cycle — prototype run

> READ-ONLY (`scripts/_prototype_finding_lifecycle.py`, 2026-06-09). Applies clarification-driven corrections to the findings store, recording provenance per change. Demonstrates (a) un-inducing a forced finding, (b) resolving an escalated finding by a new clarification. Not the DB.

**Store: 8 findings · 2 corrections applied.**

## M01-0007 — H3372G ya.re @ 1Sa 4:7
- **Clarification:** REVOKE god-present->reverence (it INDUCES); apply fear-of-God-as-threat->dread where the verse shows a dread/woe posture
- **Reason:** FORCED FINDING un-induced: 1Sa 4:7 'the Philistines were afraid ... Woe to us! ... who can deliver us from these mighty gods?' is dread of God-as-threat, not reverence. god-present alone does not resolve the shade; the dread posture, read in the verse, does.

| field | from | to |
|---|---|---|
| `lexical_meaning` | to revere | **to fear / dread** |
| `tiers.T7.1` | None | **to fear -> dread (Qal; fear of God-as-threat, dread/woe posture read in verse)** |
| `tiers.T1.4` | None | **Qal -> dread shade** |
| `triage` | ACCEPT | **ACCEPT** |
| `provenance` | clarification:god-present->reverence (INDUCED — flagged for review) | **clarification:fear-of-God-as-threat->dread (signal read in verse) — supersedes the induced god->reverence** |

## M01-0008 — H3372G ya.re @ 1Ki 8:40
- **Clarification:** ADD god-addressed-as-'you' counts as a god-object; covenant-obedience-life context ('fear you all the days they live') -> reverence
- **Reason:** ESCALATED then RESOLVED by a new clarification: 1Ki 8:40 'that they may fear you all the days that they live' — God is the object (as 'you'), in a covenant-obedience-life frame -> reverence. The earlier escalate was a detection gap, not genuine silence.

| field | from | to |
|---|---|---|
| `lexical_meaning` | to fear (shade unresolved) | **to fear = revere** |
| `tiers.T7.1` | None | **to fear -> revere (Qal; God as 'you', covenant-obedience-life context)** |
| `tiers.T1.4` | None | **Qal -> reverence shade** |
| `tiers.T3` | affect | **affect + moral-evaluation (reverent obedience posture)** |
| `triage` | ESCALATE | **ACCEPT** |
| `provenance` | no object signal (god addressed as 'you' not detected) | **clarification:god-as-you-covenant-life->reverence (resolves prior escalate)** |

---
Updated store written: `wa-m01-findings-store-v2-20260609.json` — each corrected finding now carries its `corrections[]` provenance (from/to/reason/clarification/date); status -> `corrected`.