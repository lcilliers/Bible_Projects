# Term cluster assessment — registry vs cluster alignment

**Generated:** 2026-05-04T06:40:08Z
**Aligned terms:** 2491 (2491 with OWNER registry)
**Granularities (k):** [40, 80, 120, 180]

## Summary by run

| run | k | avg dominant-cluster % | avg fragmentation | cross-cutting clusters |
|---|---|---|---|---|
| semantic__k40 | 40 | 49.4% | 5.5 | 34/40 |
| semantic__k80 | 80 | 50.1% | 6.1 | 57/80 |
| semantic__k120 | 120 | 50.3% | 6.4 | 81/120 |
| semantic__k180 | 180 | 47.2% | 6.5 | 98/180 |
| usage__k40 | 40 | 44.2% | 6.4 | 39/40 |
| usage__k80 | 80 | 43.6% | 7.3 | 67/80 |
| usage__k120 | 120 | 43.7% | 7.7 | 93/120 |
| usage__k180 | 180 | 42.1% | 8.2 | 131/180 |
| combined__k40 | 40 | 52.4% | 5.5 | 34/40 |
| combined__k80 | 80 | 52.4% | 5.6 | 59/80 |
| combined__k120 | 120 | 50.6% | 5.9 | 76/120 |
| combined__k180 | 180 | 50.9% | 6.4 | 96/180 |

**Reading the table:**
- Higher *avg dominant %* and lower *avg fragmentation* = registries align well with clusters (registry stays).
- Lower *avg dominant %* and higher *avg fragmentation* = registries miscut the data (cluster pivot is supported).
- *Cross-cutting clusters* = clusters that pull from 3+ registries without a dominant one (analytical units the registry-driven structure misses).

## Worst-aligned registries — `combined__k120`

| registry | OWNER terms | distinct clusters | dominant cluster % |
|---|---|---|---|
| R151 sorrow | 46 | 19 | 13.0% |
| R051 distress | 71 | 25 | 14.1% |
| R187 strength | 162 | 36 | 14.2% |
| R140 seeking | 6 | 6 | 16.7% |
| R173 will | 28 | 16 | 17.9% |
| R198 might | 22 | 11 | 18.2% |
| R126 purpose | 11 | 9 | 18.2% |
| R116 patience | 11 | 9 | 18.2% |
| R197 authority | 70 | 27 | 18.6% |
| R177 worth | 15 | 11 | 20.0% |
| R160 thought | 25 | 13 | 20.0% |
| R192 comfort | 5 | 5 | 20.0% |
| R112 mind | 54 | 17 | 20.4% |
| R174 wisdom | 24 | 14 | 20.8% |
| R211 being | 14 | 10 | 21.4% |
| R185 flesh | 14 | 10 | 21.4% |
| R196 power | 14 | 10 | 21.4% |
| R002 agony | 23 | 12 | 21.7% |
| R159 testimony | 9 | 6 | 22.2% |
| R015 boastfulness | 9 | 6 | 22.2% |

## Best-aligned registries — `combined__k120`

| registry | OWNER terms | distinct clusters | dominant cluster % |
|---|---|---|---|
| R065 generosity | 6 | 1 | 100.0% |
| R164 truthfulness | 5 | 1 | 100.0% |
| R029 contentment | 2 | 1 | 100.0% |
| R063 foolishness | 12 | 1 | 100.0% |
| R139 righteousness | 1 | 1 | 100.0% |
| R020 character | 4 | 1 | 100.0% |
| R017 bondage | 8 | 1 | 100.0% |
| R083 idolatry | 6 | 1 | 100.0% |
| R069 gratitude | 3 | 1 | 100.0% |
| R110 memory | 2 | 1 | 100.0% |
| R041 defilement | 2 | 1 | 100.0% |
| R096 jealousy | 1 | 1 | 100.0% |
| R203 treachery | 1 | 1 | 100.0% |
| R124 prophecy | 10 | 1 | 100.0% |
| R074 hardness | 2 | 1 | 100.0% |
| R181 zeal | 3 | 1 | 100.0% |
| R209 likeness | 2 | 1 | 100.0% |
| R155 submission | 2 | 1 | 100.0% |
| R171 whoredom | 3 | 1 | 100.0% |
| R008 appetite | 11 | 1 | 100.0% |

## Top cross-cutting clusters — `combined__k120`

| cluster | total terms | n distinct registries | top 3 registries (count/pct) |
|---|---|---|---|
| 4 | 96 | 47 | R187 strength (9/9.4%); R151 sorrow (5/5.2%); R160 thought (5/5.2%) |
| 14 | 96 | 43 | R187 strength (14/14.6%); R006 anointing (10/10.4%); R151 sorrow (5/5.2%) |
| 108 | 49 | 33 | R031 corruption (4/8.2%); R117 peace (4/8.2%); R187 strength (3/6.1%) |
| 22 | 51 | 30 | R019 calling (6/11.8%); R173 will (5/9.8%); R034 covenant (4/7.8%) |
| 58 | 52 | 29 | R099 kindness (8/15.4%); R057 evil (4/7.7%); R090 innocence (4/7.7%) |
| 78 | 48 | 28 | R187 strength (6/12.5%); R198 might (4/8.3%); R099 kindness (3/6.2%) |
| 50 | 41 | 27 | R198 might (4/9.8%); R034 covenant (4/9.8%); R006 anointing (3/7.3%) |
| 93 | 42 | 25 | R187 strength (4/9.5%); R103 love (3/7.1%); R043 desire (2/4.8%) |
| 114 | 39 | 20 | R191 doubt (7/17.9%); R107 meaning (6/15.4%); R130 reconciliation (3/7.7%) |
| 96 | 31 | 20 | R111 mercy (4/12.9%); R151 sorrow (3/9.7%); R023 compassion (3/9.7%) |
| 29 | 49 | 19 | R187 strength (14/28.6%); R033 courage (5/10.2%); R123 pride (5/10.2%) |
| 113 | 40 | 18 | R187 strength (13/32.5%); R002 agony (3/7.5%); R058 experience (3/7.5%) |
| 7 | 23 | 17 | R185 flesh (3/13.0%); R043 desire (2/8.7%); R157 temptation (2/8.7%) |
| 115 | 33 | 16 | R187 strength (8/24.2%); R005 anguish (4/12.1%); R006 anointing (3/9.1%) |
| 84 | 27 | 16 | R051 distress (5/18.5%); R152 strife (4/14.8%); R187 strength (3/11.1%) |
| 105 | 39 | 16 | R051 distress (10/25.6%); R005 anguish (7/17.9%); R187 strength (5/12.8%) |
| 23 | 29 | 15 | R173 will (5/17.2%); R043 desire (4/13.8%); R111 mercy (3/10.3%) |
| 111 | 24 | 15 | R117 peace (7/29.2%); R112 mind (3/12.5%); R031 corruption (2/8.3%) |
| 37 | 29 | 14 | R206 vulnerability (12/41.4%); R187 strength (4/13.8%); R184 spirit (2/6.9%) |
| 83 | 19 | 13 | R108 meditation (4/21.1%); R160 thought (3/15.8%); R112 mind (2/10.5%) |
