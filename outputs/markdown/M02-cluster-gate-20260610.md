# M02 — Per-Cluster Gate Report

> Read-only mechanical gate for the L2 verse-read. Generated 2026-06-10. Tier profile built by value-classification (positional storage; no slot decode). This report does not sign off the cluster — it surfaces the evidence for the researcher to.

## 1. Coverage

- **703 / 703 own term-in-verses have a meaning (100%)**

| provenance | findings |
|---|---:|
| l2_api | 15,482 |
| l2_meaning | 703 |
| session_b_migration | 5 |

- Fan-out ratio: 22.0 tier findings (l2_api) per meaning paragraph (l2_meaning).

## 2. Mechanical tier profile

Distribution of the controlled-vocabulary tier values across all l2_api findings. Free-text fields (sense_applied, mode, purpose_equips, produces_effect, relational_implication) are not profiled here (2,967 free-text values).

### type  (703 values)

| value | n | share |
|---|---:|---|
| status | 560 | █████████████████████████······· 80% |
| action | 117 | █████··························· 17% |
| quality | 26 | █······························· 4% |

### origin  (696 values)

| value | n | share |
|---|---:|---|
| within-person | 585 | ███████████████████████████····· 84% |
| received-from-outside | 96 | ████···························· 14% |
| bestowed-by-God | 15 | █······························· 2% |

### attributed_to_God  (703 values)

| value | n | share |
|---|---:|---|
| no | 372 | █████████████████··············· 53% |
| yes | 331 | ███████████████················· 47% |

### typology_direction  (703 values)

| value | n | share |
|---|---:|---|
| divine->human | 337 | ███████████████················· 48% |
| none | 285 | █████████████··················· 41% |
| human->divine | 81 | ████···························· 12% |

### faculty  (1,064 values)

| value | n | share |
|---|---:|---|
| affect | 520 | ████████████████················ 49% |
| moral-evaluation | 446 | █████████████··················· 42% |
| relational | 54 | ██······························ 5% |
| agency | 36 | █······························· 3% |
| volition | 6 | ································ 1% |
| cognition | 2 | ································ 0% |

### constitutional_location  (16 values)

| value | n | share |
|---|---:|---|
| heart | 10 | ████████████████████············ 62% |
| spirit | 4 | ████████························ 25% |
| soul | 2 | ████···························· 12% |

### literary_setting  (702 values)

| value | n | share |
|---|---:|---|
| narrative | 243 | ███████████····················· 35% |
| prophecy | 217 | ██████████······················ 31% |
| poetry | 93 | ████···························· 13% |
| wisdom | 60 | ███····························· 9% |
| epistle | 49 | ██······························ 7% |
| law | 33 | ██······························ 5% |
| gospel | 7 | ································ 1% |

### immediate_response  (589 values)

| value | n | share |
|---|---:|---|
| SILENT | 589 | ████████████████████████████████ 100% |

## 3. Flag-rate analysis

- **56 / 703 meanings flagged (8.0%)**, of which:
  - **6 genuine** homonym / wrong-sense artifacts to set aside (0.9% of cluster) — see §4.
  - **50 benign** self-audit notes (a non-null field, typically `immediate_response=SILENT`, not reflected in the prose of forensic/siege records) — no quality problem.

## 4. Homonym & clustering-misfit surfacing

Genuine flagged meanings (artifacts whose true sense is **not** this cluster):

- In 2Ki 12:10 tsur is "bagged / tied up" — "they bagged and counted the money that was found in the house of the LORD." This is the HOMONYM of tsur meaning to bind up / tie in a bag, NOT the M02 sense ...
- In 2Ki 5:23 tsur is "tied up / bagged" — "he... tied up two talents of silver in two bags." This is the HOMONYM of tsur meaning to bind up / tie in a bag, NOT the M02 sense "to show hostility / besieg...
- In Deu 14:25 tsur is "bind up" — "you shall turn it into money and bind up the money in your hand." This is the HOMONYM of tsur meaning to bind up / tie, NOT the M02 sense "to show hostility / besiege...
- In Eze 5:3 tsur is "bind" — "take from these a small number and bind them in the skirts of your robe." This is the HOMONYM of tsur meaning to bind up / tie, NOT the M02 sense "to show hostility / besi...
- In Psa 139:5 this tsur (H6696B, the "show hostility" entry) does NOT carry the hostility sense here: "You hem me in, behind and before." The verse's meaning is God's loving, all-encompassing enclosure...
- In Song 8:9 tsur is "enclose / wall" — "if she is a door, we will enclose her with boards of cedar." Here the term carries the enclose / board-up sense, NOT the M02 "show hostility" reading: the broth...

**Clustering-misfit signal:** 29 meanings carry a military-siege sense (`besiege`). Pure siege is an external act of war with thin inner-being content (affect SILENT). Recommend the researcher adjudicate whether this term belongs in M02.

## 5. Spot-check

- Random-sample spot-check: `python scripts/_generate_meaning_quality_check.py --cluster M02` → `outputs/markdown/M02-meaning-quality-check-20260610.md`.
- Full meaning export: `python scripts/_generate_verse_meanings_export.py --cluster M02` → `outputs/markdown/M02-verse-meanings-20260610.md`.

## 6. Mechanical verdict (not a sign-off)

- [x] Coverage 100%
- [x] Genuine-artifact rate < 2%
- [x] Type/origin/faculty profiles populated

> Mechanical checks are necessary, not sufficient. Cluster sign-off remains a non-mechanical researcher judgement (per the analysis rules).
