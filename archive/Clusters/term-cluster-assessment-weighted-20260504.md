# Term cluster assessment — registry vs cluster alignment

**Generated:** 2026-05-04T07:03:28Z
**Aligned terms:** 2491 (2491 with OWNER registry)
**Granularities (k):** [40, 80, 120, 180]

## Summary by run

| run | k | avg dominant-cluster % | avg fragmentation | cross-cutting clusters |
|---|---|---|---|---|
| semantic__k40 | 40 | 56.8% | 4.2 | 27/40 |
| semantic__k80 | 80 | 55.7% | 4.7 | 32/80 |
| semantic__k120 | 120 | 54.9% | 5.1 | 44/120 |
| semantic__k180 | 180 | 55.4% | 5.4 | 56/180 |
| usage__k40 | 40 | 36.3% | 7.5 | 39/40 |
| usage__k80 | 80 | 31.5% | 9.0 | 78/80 |
| usage__k120 | 120 | 30.6% | 9.7 | 115/120 |
| usage__k180 | 180 | 27.7% | 10.6 | 160/180 |
| combined__k40 | 40 | 37.0% | 7.7 | 37/40 |
| combined__k80 | 80 | 35.1% | 8.9 | 73/80 |
| combined__k120 | 120 | 36.2% | 9.3 | 107/120 |
| combined__k180 | 180 | 40.1% | 8.8 | 134/180 |

**Reading the table:**
- Higher *avg dominant %* and lower *avg fragmentation* = registries align well with clusters (registry stays).
- Lower *avg dominant %* and higher *avg fragmentation* = registries miscut the data (cluster pivot is supported).
- *Cross-cutting clusters* = clusters that pull from 3+ registries without a dominant one (analytical units the registry-driven structure misses).

## Worst-aligned registries — `combined__k120`

| registry | OWNER terms | distinct clusters | dominant cluster % |
|---|---|---|---|
| R043 desire | 47 | 33 | 6.4% |
| R051 distress | 71 | 41 | 7.0% |
| R112 mind | 54 | 33 | 7.4% |
| R080 humility | 12 | 12 | 8.3% |
| R126 purpose | 11 | 11 | 9.1% |
| R187 strength | 162 | 70 | 9.9% |
| R007 anxiety | 10 | 10 | 10.0% |
| R042 delight | 30 | 21 | 10.0% |
| R023 compassion | 18 | 14 | 11.1% |
| R117 peace | 53 | 31 | 11.3% |
| R005 anguish | 44 | 26 | 11.4% |
| R149 slander | 17 | 16 | 11.8% |
| R160 thought | 25 | 18 | 12.0% |
| R183 heart | 25 | 20 | 12.0% |
| R103 love | 56 | 34 | 12.5% |
| R026 conscience | 8 | 8 | 12.5% |
| R168 uprightness | 8 | 8 | 12.5% |
| R002 agony | 23 | 19 | 13.0% |
| R151 sorrow | 46 | 32 | 13.0% |
| R198 might | 22 | 19 | 13.6% |

## Best-aligned registries — `combined__k120`

| registry | OWNER terms | distinct clusters | dominant cluster % |
|---|---|---|---|
| R139 righteousness | 1 | 1 | 100.0% |
| R096 jealousy | 1 | 1 | 100.0% |
| R203 treachery | 1 | 1 | 100.0% |
| R093 intention | 1 | 1 | 100.0% |
| R179 yearning | 1 | 1 | 100.0% |
| R060 faithfulness | 1 | 1 | 100.0% |
| R132 rejoicing | 1 | 1 | 100.0% |
| R077 honesty | 2 | 1 | 100.0% |
| R189 malice | 1 | 1 | 100.0% |
| R008 appetite | 11 | 2 | 90.9% |
| R015 boastfulness | 9 | 2 | 88.9% |
| R017 bondage | 8 | 2 | 87.5% |
| R170 weakness | 8 | 3 | 75.0% |
| R207 blindness (spiritual) | 7 | 3 | 71.4% |
| R102 longing | 15 | 5 | 66.7% |
| R083 idolatry | 6 | 3 | 66.7% |
| R085 imagination | 3 | 2 | 66.7% |
| R069 gratitude | 3 | 2 | 66.7% |
| R188 weeping | 9 | 4 | 66.7% |
| R115 passion | 3 | 2 | 66.7% |

## Top cross-cutting clusters — `combined__k120`

| cluster | total terms | n distinct registries | top 3 registries (count/pct) |
|---|---|---|---|
| 70 | 72 | 43 | R099 kindness (4/5.6%); R173 will (4/5.6%); R051 distress (4/5.6%) |
| 60 | 66 | 43 | R187 strength (5/7.6%); R051 distress (3/4.5%); R032 counsel (3/4.5%) |
| 56 | 52 | 38 | R051 distress (5/9.6%); R061 fear (4/7.7%); R187 strength (3/5.8%) |
| 48 | 47 | 32 | R187 strength (7/14.9%); R051 distress (3/6.4%); R065 generosity (2/4.3%) |
| 17 | 43 | 29 | R059 faith (4/9.3%); R019 calling (4/9.3%); R043 desire (3/7.0%) |
| 61 | 56 | 29 | R004 anger (9/16.1%); R073 guilt (9/16.1%); R146 shame (4/7.1%) |
| 38 | 44 | 27 | R089 iniquity (6/13.6%); R120 perverseness (4/9.1%); R005 anguish (3/6.8%) |
| 106 | 37 | 26 | R128 rebellion (4/10.8%); R112 mind (4/10.8%); R034 covenant (3/8.1%) |
| 20 | 43 | 24 | R187 strength (6/14.0%); R062 fellowship (6/14.0%); R117 peace (3/7.0%) |
| 89 | 26 | 22 | R160 thought (2/7.7%); R112 mind (2/7.7%); R085 imagination (2/7.7%) |
| 23 | 27 | 22 | R013 bitterness (3/11.1%); R121 praise (2/7.4%); R190 contempt (2/7.4%) |
| 26 | 26 | 21 | R197 authority (3/11.5%); R051 distress (2/7.7%); R006 anointing (2/7.7%) |
| 22 | 25 | 21 | R184 spirit (2/8.0%); R117 peace (2/8.0%); R042 delight (2/8.0%) |
| 45 | 23 | 20 | R066 gentleness (2/8.7%); R176 worship (2/8.7%); R192 comfort (2/8.7%) |
| 119 | 24 | 20 | R135 repentance (3/12.5%); R064 forgiveness (2/8.3%); R059 faith (2/8.3%) |
| 34 | 28 | 20 | R187 strength (2/7.1%); R122 prayer (2/7.1%); R078 hope (2/7.1%) |
| 35 | 25 | 20 | R034 covenant (3/12.0%); R112 mind (2/8.0%); R197 authority (2/8.0%) |
| 74 | 24 | 20 | R157 temptation (4/16.7%); R043 desire (2/8.3%); R131 rejection (1/4.2%) |
| 44 | 24 | 19 | R187 strength (4/16.7%); R058 experience (2/8.3%); R197 authority (2/8.3%) |
| 93 | 27 | 19 | R117 peace (5/18.5%); R078 hope (4/14.8%); R051 distress (2/7.4%) |
