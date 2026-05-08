# Term cluster assessment — registry vs cluster alignment

**Generated:** 2026-05-04T06:55:27Z
**Aligned terms:** 2491 (2491 with OWNER registry)
**Granularities (k):** [40, 80, 120, 180]

## Summary by run

| run | k | avg dominant-cluster % | avg fragmentation | cross-cutting clusters |
|---|---|---|---|---|
| semantic__k40 | 40 | 49.4% | 5.5 | 34/40 |
| semantic__k80 | 80 | 50.1% | 6.1 | 57/80 |
| semantic__k120 | 120 | 50.3% | 6.4 | 81/120 |
| semantic__k180 | 180 | 47.2% | 6.5 | 98/180 |
| usage__k40 | 40 | 36.3% | 7.5 | 39/40 |
| usage__k80 | 80 | 31.5% | 9.0 | 78/80 |
| usage__k120 | 120 | 30.6% | 9.7 | 115/120 |
| usage__k180 | 180 | 27.7% | 10.6 | 160/180 |
| combined__k40 | 40 | 35.0% | 8.1 | 40/40 |
| combined__k80 | 80 | 33.3% | 8.9 | 76/80 |
| combined__k120 | 120 | 32.6% | 9.6 | 110/120 |
| combined__k180 | 180 | 31.6% | 10.1 | 154/180 |

**Reading the table:**
- Higher *avg dominant %* and lower *avg fragmentation* = registries align well with clusters (registry stays).
- Lower *avg dominant %* and higher *avg fragmentation* = registries miscut the data (cluster pivot is supported).
- *Cross-cutting clusters* = clusters that pull from 3+ registries without a dominant one (analytical units the registry-driven structure misses).

## Worst-aligned registries — `combined__k120`

| registry | OWNER terms | distinct clusters | dominant cluster % |
|---|---|---|---|
| R112 mind | 54 | 34 | 7.4% |
| R187 strength | 162 | 71 | 8.0% |
| R183 heart | 25 | 20 | 8.0% |
| R051 distress | 71 | 35 | 8.5% |
| R126 purpose | 11 | 11 | 9.1% |
| R117 peace | 53 | 34 | 9.4% |
| R103 love | 56 | 30 | 10.7% |
| R199 dominion | 28 | 22 | 10.7% |
| R078 hope | 27 | 19 | 11.1% |
| R197 authority | 70 | 41 | 11.4% |
| R040 deceit | 17 | 13 | 11.8% |
| R111 mercy | 25 | 19 | 12.0% |
| R160 thought | 25 | 18 | 12.0% |
| R026 conscience | 8 | 8 | 12.5% |
| R043 desire | 47 | 33 | 12.8% |
| R157 temptation | 15 | 12 | 13.3% |
| R176 worship | 30 | 17 | 13.3% |
| R198 might | 22 | 17 | 13.6% |
| R049 discernment | 7 | 7 | 14.3% |
| R056 envy | 14 | 12 | 14.3% |

## Best-aligned registries — `combined__k120`

| registry | OWNER terms | distinct clusters | dominant cluster % |
|---|---|---|---|
| R139 righteousness | 1 | 1 | 100.0% |
| R096 jealousy | 1 | 1 | 100.0% |
| R203 treachery | 1 | 1 | 100.0% |
| R074 hardness | 2 | 1 | 100.0% |
| R155 submission | 2 | 1 | 100.0% |
| R093 intention | 1 | 1 | 100.0% |
| R179 yearning | 1 | 1 | 100.0% |
| R060 faithfulness | 1 | 1 | 100.0% |
| R132 rejoicing | 1 | 1 | 100.0% |
| R077 honesty | 2 | 1 | 100.0% |
| R189 malice | 1 | 1 | 100.0% |
| R008 appetite | 11 | 3 | 81.8% |
| R050 disobedience | 3 | 2 | 66.7% |
| R085 imagination | 3 | 2 | 66.7% |
| R087 indignation | 2 | 2 | 50.0% |
| R029 contentment | 2 | 2 | 50.0% |
| R017 bondage | 8 | 5 | 50.0% |
| R083 idolatry | 6 | 4 | 50.0% |
| R148 sincerity | 2 | 2 | 50.0% |
| R094 intercession | 4 | 3 | 50.0% |

## Top cross-cutting clusters — `combined__k120`

| cluster | total terms | n distinct registries | top 3 registries (count/pct) |
|---|---|---|---|
| 32 | 118 | 56 | R187 strength (13/11.0%); R051 distress (6/5.1%); R042 delight (6/5.1%) |
| 51 | 74 | 45 | R051 distress (5/6.8%); R063 foolishness (3/4.1%); R187 strength (3/4.1%) |
| 8 | 62 | 40 | R103 love (5/8.1%); R035 covetousness (3/4.8%); R051 distress (3/4.8%) |
| 111 | 65 | 36 | R099 kindness (5/7.7%); R187 strength (5/7.7%); R057 evil (5/7.7%) |
| 88 | 46 | 33 | R043 desire (6/13.0%); R051 distress (3/6.5%); R098 justice (2/4.3%) |
| 77 | 54 | 33 | R173 will (5/9.3%); R128 rebellion (5/9.3%); R019 calling (5/9.3%) |
| 5 | 37 | 29 | R117 peace (4/10.8%); R051 distress (3/8.1%); R187 strength (2/5.4%) |
| 95 | 66 | 28 | R005 anguish (9/13.6%); R061 fear (5/7.6%); R072 groaning (5/7.6%) |
| 27 | 42 | 27 | R051 distress (4/9.5%); R103 love (3/7.1%); R004 anger (3/7.1%) |
| 114 | 28 | 27 | R071 grief (2/7.1%); R187 strength (1/3.6%); R004 anger (1/3.6%) |
| 100 | 45 | 24 | R090 innocence (5/11.1%); R098 justice (4/8.9%); R059 faith (3/6.7%) |
| 86 | 37 | 23 | R098 justice (8/21.6%); R073 guilt (2/5.4%); R050 disobedience (2/5.4%) |
| 67 | 27 | 23 | R187 strength (2/7.4%); R183 heart (2/7.4%); R191 doubt (2/7.4%) |
| 28 | 30 | 22 | R057 evil (4/13.3%); R123 pride (3/10.0%); R149 slander (2/6.7%) |
| 74 | 31 | 20 | R043 desire (4/12.9%); R180 yielding (4/12.9%); R197 authority (2/6.5%) |
| 44 | 31 | 20 | R174 wisdom (8/25.8%); R063 foolishness (3/9.7%); R100 knowledge (2/6.5%) |
| 31 | 25 | 20 | R121 praise (2/8.0%); R190 contempt (2/8.0%); R028 consecration (2/8.0%) |
| 46 | 27 | 19 | R103 love (4/14.8%); R023 compassion (3/11.1%); R187 strength (2/7.4%) |
| 68 | 28 | 19 | R120 perverseness (4/14.3%); R089 iniquity (3/10.7%); R187 strength (2/7.1%) |
| 52 | 44 | 19 | R151 sorrow (9/20.5%); R008 appetite (9/20.5%); R052 division (5/11.4%) |
