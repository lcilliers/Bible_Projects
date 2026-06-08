# M01 — L2 decision-scenario typing + STEP-signal sufficiency (prototype)

> READ-ONLY (`scripts/_assess_p2_verse_scenarios.py --cluster M01`). Types every M01 verse into the L2 decision-scenario space and measures whether the STEP signal to decide it is present. A verse can trigger several scenarios (they compose).

**M01: 930 verses (references), 1044 in-cluster occurrences.**

## Scenario distribution (verses; non-exclusive)

| Scenario | Verses | % | Decision needed |
|---|---|---|---|
| S1 **none — pure L1 mechanical** | 39 | 4% | |
| S0 set-aside / relevance re-eval (Song-6 class) | 79 | 8% | |
| S2 L2 sense-resolution (which STEP sense) | 781 | 84% | |
| S3 L2 pair (sibling span) vs distinct | 96 | 10% | |
| S4 L2 route qualifier occurrence in | 414 | 45% | |
| S5 L2 reciprocal / multi-belong (cross-cluster) | 597 | 64% | |
| COMPOUND **>1 decision in one verse (compose)** | 688 | 74% | |

## STEP-signal population (over in-cluster occurrences)

| Signal | Present | Carries which decision |
|---|---|---|
| `span_strong_match` | 1044 (100%) | S3 pairing · S4 qualifier-attach |
| `morph_code` | 0 (0%) | S2 sense-resolution (stem→branch) |
| `stem` | 0 (0%) | S2 sense-resolution |

> If a signal is sparsely populated, L2 cannot lean on it yet — it needs a STEP backfill or a deeper read. That is the key finding for 'will L2 STEP meaning suffice'.

## Sample — S2 L2 sense-resolution (which STEP sense)

| Ref | In-cluster terms | Other | Qual | span | morph |
|---|---|---|---|---|---|
| 1Ch 10:4 | ya.re |  |  | span=Y | morph=- |
| 1Ch 13:12 | ya.re |  |  | span=Y | morph=- |
| 1Ch 14:17 | pa.chad |  |  | span=Y | morph=- |
| 1Ch 16:25 | ya.re | other=M22 |  | span=Y | morph=- |
| 1Ch 17:21 | ya.re | other=M22,M38 |  | span=Y | morph=- |
| 1Ch 17:9 | ra.gaz | other=M10 |  | span=Y | morph=- |

## Sample — S3 L2 pair (sibling span) vs distinct

| Ref | In-cluster terms | Other | Qual | span | morph |
|---|---|---|---|---|---|
| 1Cor 2:3 | fobos+tromos | other=M24 | qual=1 | span=Y | morph=- |
| 1Jo 4:18 | fobos+fobeo |  |  | span=Y | morph=- |
| 1Pe 3:14 | fobos+fobeo |  |  | span=Y | morph=- |
| 1Pe 3:6 | ptoesis+fobeo | other=M05,M23,M37 |  | span=Y | morph=- |
| 1Sa 14:15 | cha.rad+cha.ra.dah+ra.gaz | other=M27 | qual=1 | span=Y | morph=- |
| 1Sa 28:5 | cha.rad+ya.re |  |  | span=Y | morph=- |

## Sample — S4 L2 route qualifier occurrence in

| Ref | In-cluster terms | Other | Qual | span | morph |
|---|---|---|---|---|---|
| 1Cor 2:3 | fobos+tromos | other=M24 | qual=1 | span=Y | morph=- |
| 1Ki 1:51 | ya.re |  | qual=1 | span=Y | morph=- |
| 1Ki 8:40 | ya.re | other=M25,M44 | qual=1 | span=Y | morph=- |
| 1Ki 8:43 | ya.re | other=M37 | qual=1 | span=Y | morph=- |
| 1Sa 11:7 | pa.chad |  | qual=1 | span=Y | morph=- |
| 1Sa 12:14 | ya.re | other=M36 | qual=2 | span=Y | morph=- |

## Sample — S5 L2 reciprocal / multi-belong (cross-cluster)

| Ref | In-cluster terms | Other | Qual | span | morph |
|---|---|---|---|---|---|
| 1Ch 16:25 | ya.re | other=M22 |  | span=Y | morph=- |
| 1Ch 17:21 | ya.re | other=M22,M38 |  | span=Y | morph=- |
| 1Ch 17:9 | ra.gaz | other=M10 |  | span=Y | morph=- |
| 1Ch 22:13 | ya.re | other=M23,M30 |  | span=Y | morph=- |
| 1Ch 28:20 | ya.re | other=M23,M24,M36 |  | span=Y | morph=- |
| 1Cor 2:3 | fobos+tromos | other=M24 | qual=1 | span=Y | morph=- |
