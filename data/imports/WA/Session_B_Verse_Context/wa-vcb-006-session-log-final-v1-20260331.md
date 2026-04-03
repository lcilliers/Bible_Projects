# wa-vcb-006-session-log-final-v1-20260331.md

**Framework B — Soul Word Analysis Programme**
**VCB-006 Final Session Log — All Registries Complete**
**Version:** v1 | **Date:** 2026-03-31 | **Governing instruction:** WA-VerseContext-Instruction-v2.0-20260331.md

Outputs: wa-vcb-006-term-observations-v1-20260331.md | wa-vcb-006-session-log-R051-v1, R052-v1, R053-R055-R056-v1

---

## Batch VCB-006 — Complete

| Registry | Word | Terms | Verses | Relevant | Set Aside | Groups | All-Fail | Rate |
|---|---|---|---|---|---|---|---|---|
| 051 | Distress | 69 | 1,181 | 810 | 371 | 85 | 12 | 68.6% |
| 052 | Division | 25 | 395 | 135 | 260 | 25 | 7 | 34.2% |
| 053 | Dread | 5 | 111 | 79 | 32 | 8 | 2 | 71.2% |
| 055 | Endurance | 4 | 110 | 36 | 74 | 5 | 1 | 32.7% |
| 056 | Envy | 14 | 218 | 169 | 49 | 24 | 0 | 77.5% |
| 057 | Evil | 18 | 457 | 139 | 318 | 20 | 2 | 30.4% |
| **TOTAL** | | **135** | **2,472** | **1,368** | **1,104** | **167** | **24** | **55.3%** |

---

## Researcher Decisions

| ID | Decision |
|---|---|
| RD-VCB006-001 | Registry 054 gap confirmed expected |
| RD-VCB006-002 | H1931 treat as likely all-fail — light survey first |
| RD-VCB006-003 | H6696B (to provoke): classify independently on own gloss |

---

## Programme Flags

| Flag | Term | Note |
|---|---|---|
| PROG-VCB006-001 | H1931 (mti_id=849) | All-fail pronoun; Claude Code must not gate Registry 057 completion on H1931 having an anchor |
| PROG-VCB006-002 | H2787 (mti_id=5184) | Inner suffering of Psa 69:3 and 102:3 carried by adjacent terms |
| PROG-VCB006-003 | H2506B (mti_id=5238) | All-fail — smoothness sense not instantiated in verse population; Claude Code must not gate Registry 052 completion on H2506B having an anchor |

---

## All-Verses-Fail Terms (24)

**Registry 051 (12):** G0316, G1876, G4661, H0206G, H2787, H3377, H3737, H3744, H3745, H4748, H5781, H6697G

**Registry 052 (7):** G2183, G2184, G3312, H2506B, H2515, H6302, H6306A

**Registry 053 (2):** H4637, H6178

**Registry 055 (1):** H5332

**Registry 056 (0):** none

**Registry 057 (2):** G0824, H1931

---

## Registry 057 — Evil: Notable Findings

**Registry 057 relevance rate (30.4%)** is heavily distorted by H1931 (291 all-fail verses). Excluding H1931, the rate for the 17 substantive terms would be 139/166 = **83.7%** — the highest single-registry rate in the batch.

**G4190 (ponēros — evil):** 64 of 71 relevant; four groups. The "evil thoughts from the heart" group (Mat 15:19, Mar 7:23) anchors the inner-being origin of all harmful action. The "evil one" group is extensive and structurally significant — it establishes personal evil agency as an inner-spiritual opponent. Heb 3:12 ("evil unbelieving heart") and Heb 10:22 ("evil conscience") are explicitly inner-being anchors.

**G0987 (blasphemy):** All 11 relevant; the Rev 16 cluster (cursed God and did not repent) is a stark inner moral portrait of hardened rebellion — directly relevant to the hardening of heart material in Registry 051.

**G0420 (not resentful):** Single verse; 2Ti 2:24 (patiently enduring evil) is a positive inner disposition — forbearance as an inner character quality. Structurally connects to the endurance/perseverance cluster.

---

## Cross-Registry Observations (for Session B awareness)

1. **The inner origin of evil:** G4190 (evil heart → evil actions), H7451I (evil devised inwardly), Mat 15:19 (evil thoughts come from within), Mar 7:23 (all these evil things come from within) — these collectively establish a strong programme-wide finding that the biblical witness locates the origin of evil within the inner person. Session B will have rich material on this.

2. **The zeal/jealousy continuum:** Registry 056 produces a complex picture in which the same root vocabulary (zeal/jealousy/fervour) names both divine passion and human envy. The semantic range from destructive envy (G5355) to consuming devotion (G2205) to divine jealousy (H7067H) is unusual and will warrant close Session B analysis.

3. **The crying-out cluster:** H2199 (to cry out), H2201, H6682 (outcry) in Registry 051 produce a large body of material under §3.4. The inner state → outward cry direction of travel is one of the most evidenced inner-being expressions in the programme.

4. **The "Lord is my portion" cluster:** H2506A in Registry 052 produces one of the most concentrated expressions of inner relational identity and trust in the programme. God as portion/lot/inheritance names a disposition of soul (Lam 3:24 explicitly: "says my soul"). This will be structurally significant for Session B.

5. **The "how long?" lament:** H5331 in Registry 055 concentrates the inner experience of perceived divine abandonment — Psa 13:1, 74:1, 77:8, 89:46, Lam 3:18. This cluster names one of the sharpest inner-being conditions in Scripture: the grief of apparent perpetual absence.

---

## Notes for Patch Construction Session

- Patch construction is deferred per programme discipline. A separate session reads this observations file and the batch JSON.
- Dual verse_record_id entries noted for: Phili 1:15 (G5355), Phili 3:6 (G2205), 1Jo 1:1 / 1Jn 1:1, 1Jo 2:11 / 1Jn 2:11, 1Jo 2:16 / 1Jn 2:16 — patch builder must classify only the version with full text and set aside the other.
- H6696A and H6696B have distinct verse_record_id sets (confirmed programmatically); no deduplication needed in patch.
- All group structures and anchor designations are fully specified in the observations file Classification blocks. Patch builder reads these directly.
- Anchor reference verification against actual verse_record_ids required before patch finalisation per programme discipline.

---

## Completion Status

All 135 OWNER terms in VCB-006 classified. All 6 registries (051, 052, 053, 055, 056, 057) complete. Registry 054 absent from batch by design (confirmed expected).

**Next step: Patch construction session — reads wa-vcb-006-term-observations-v1-20260331.md and wa-vcb-006-extract-20260331.json.**

---

*wa-vcb-006-session-log-final-v1-20260331.md | VCB-006 | All registries complete | 2026-03-31*
