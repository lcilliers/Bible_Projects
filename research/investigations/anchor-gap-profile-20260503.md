# Anchor Gap Profile — Post-Cleanup

_Generated 2026-05-03T13:15:54Z_  ·  source: `scripts/_exploratory_anchor_gap_profile_v1_20260503.py`

Three views of where anchors are missing in the analytical record. All counts reflect the state after today's three cleanup patches (POS noise Tier 1, R212→R122 merge, homonym mistarget).

## Programme totals (active state)

- Active registries (not Excluded): **183**
- Active groups (`verse_context_group` not delete_flagged): **3,535**
- Active relevant `verse_context` rows: **33,855**
- Active anchor `verse_context` rows: **4,576**

## View 1 — Registries with no active anchors

**11 registries** have **zero** active anchors. **11** more have only 1–2 anchors (at-risk).

### Zero-anchor registries

| Reg | Word | Cluster | Active OWNER terms | Relevant vc | Status |
|---:|---|---|---:|---:|---|
| 27 | consciousness | C22 | 0 | 0 | Verse Context Reset |
| 48 | diligence | C08 | 0 | 0 | ? |
| 104 | loyalty | C18 | 0 | 0 | Verse Context Reset |
| 109 | meekness | C08 | 0 | 0 | Verse Context Reset |
| 129 | recognition | C22 | 0 | 0 | Verse Context Reset |
| 137 | resolve | C14 | 0 | 0 | Verse Context Reset |
| 138 | reverence | C15 | 0 | 0 | Verse Context Reset |
| 144 | sensuality | C12 | 0 | 0 | Verse Context Reset |
| 200 | energy | C20 | 0 | 0 | Verse Context Reset |
| 205 | resentment | C07 | 0 | 0 | Verse Context Reset |
| 214 | suffering | C05 | 0 | 0 | Ready for Analysis |

### Low-anchor registries (1–2 anchors)

| Reg | Word | Cluster | Active OWNER | Relevant vc | Anchors |
|---:|---|---|---:|---:|---:|
| 132 | rejoicing | C03 | 1 | 1 | 1 |
| 156 | surrender | C14 | 11 | 1 | 1 |
| 179 | yearning | C04 | 1 | 1 | 1 |
| 203 | treachery | C11 | 1 | 3 | 1 |
| 29 | contentment | C03 | 2 | 3 | 2 |
| 41 | defilement | C12 | 2 | 4 | 2 |
| 87 | indignation | C07 | 2 | 2 | 2 |
| 139 | righteousness | C10 | 1 | 10 | 2 |
| 148 | sincerity | C10 | 2 | 5 | 2 |
| 189 | malice | C12 | 1 | 3 | 2 |
| 209 | likeness | C19 | 2 | 3 | 2 |

## View 2 — OWNER terms with active classifications but no anchor

These terms have at least one relevant `verse_context` row, plus at least one active group, but no anchor has been designated. Without an anchor the group's meaning has no exemplar verse to ground the analytical reading.

**368 active OWNER terms** have verses pulled in but zero anchors:
  - With relevant vc rows but no anchor (analytical gap): 0
  - With stranded group(s) but no anchor (group orphan): 51
  - With no classifications at all (verses pulled, never inspected): 317

### Top 30 registries by no-anchor term count

| Reg | Word | # terms missing anchor | Total verses pulled on those terms |
|---:|---|---:|---:|
| 187 | strength | 31 | 367 |
| 6 | anointing | 28 | 206 |
| 5 | anguish | 17 | 136 |
| 151 | sorrow | 14 | 254 |
| 99 | kindness | 13 | 212 |
| 51 | distress | 11 | 39 |
| 19 | calling | 10 | 277 |
| 156 | surrender | 10 | 700 |
| 213 | listen | 9 | 17 |
| 90 | innocence | 8 | 588 |
| 198 | might | 8 | 189 |
| 117 | peace | 7 | 579 |
| 52 | division | 7 | 72 |
| 8 | appetite | 7 | 658 |
| 31 | corruption | 6 | 47 |
| 57 | evil | 6 | 835 |
| 33 | courage | 6 | 87 |
| 123 | pride | 6 | 14 |
| 2 | agony | 6 | 16 |
| 24 | condemnation | 5 | 43 |
| 44 | despair | 5 | 784 |
| 121 | praise | 5 | 70 |
| 177 | worth | 5 | 37 |
| 197 | authority | 5 | 11 |
| 28 | consecration | 5 | 25 |
| 147 | sin | 4 | 216 |
| 158 | terror | 4 | 44 |
| 120 | perverseness | 4 | 7 |
| 134 | renewal | 4 | 7 |
| 180 | yielding | 4 | 14 |

### Top 25 individual no-anchor terms by verses pulled

| Reg | Word | Strong's | Translit | Gloss | Lang | Status | Groups | Rel vc | Verses |
|---:|---|---|---|---|---|---|---:|---:|---:|
| 167 | unity | `H1571` | gam | also | H | `extracted` | 3 | 0 | 404 |
| 44 | despair | `H0589` | a.ni | I | H | `extracted` | 0 | 0 | 376 |
| 156 | surrender | `H0859E` | at.ten | you [f.p.] | H | `extracted` | 0 | 0 | 359 |
| 44 | despair | `H3808` | lo | not | H | `extracted` | 6 | 0 | 331 |
| 90 | innocence | `H2009` | hin.neh | behold | H | `extracted` | 7 | 0 | 319 |
| 13 | bitterness | `H0413` | el | to[wards] | H | `extracted` | 0 | 0 | 307 |
| 11 | awe | `H0853` | et | [Obj.] | H | `extracted` | 0 | 0 | 292 |
| 57 | evil | `H1931` | hu | he/she/it | H | `extracted` | 0 | 0 | 291 |
| 89 | iniquity | `H4480A` | min- | from | H | `extracted` | 4 | 0 | 284 |
| 117 | peace | `H5769G` | o.lam | forever: enduring | H | `extracted_theological_anchor` | 0 | 0 | 272 |
| 156 | surrender | `H0859D` | at.tem | you [m.p.] | H | `extracted` | 0 | 0 | 234 |
| 126 | purpose | `H4616` | ma.an | because | H | `extracted` | 2 | 0 | 228 |
| 90 | innocence | `H2005` | hen | look! | H | `extracted` | 6 | 0 | 223 |
| 4 | anger | `H0639G` | aph | face: anger | H | `extracted` | 5 | 0 | 212 |
| 8 | appetite | `H2416B` | chay | kinsfolk | H | `extracted` | 0 | 0 | 207 |
| 8 | appetite | `H2416D` | chay.yah | community | H | `extracted` | 0 | 0 | 207 |
| 57 | evil | `H4994` | na | please | H | `extracted` | 2 | 0 | 195 |
| 57 | evil | `H1992` | hem.mah | they [masc.] | H | `extracted` | 0 | 0 | 189 |
| 175 | wonder | `H0176B` | o | desire | H | `extracted` | 0 | 0 | 175 |
| 147 | sin | `H0408` | al | not | H | `extracted` | 9 | 0 | 163 |
| 57 | evil | `H4310` | mi | who? | H | `extracted` | 10 | 0 | 157 |
| 117 | peace | `H6635B` | tsa.va | Hosts | H | `extracted_theological_anchor` | 0 | 0 | 156 |
| 187 | strength | `H0352C` | a.yil | leader | H | `extracted` | 0 | 0 | 139 |
| 187 | strength | `H0352D` | a.yil | terebinth | H | `extracted` | 0 | 0 | 139 |
| 8 | appetite | `H2416E` | chay.yim | life | H | `extracted` | 0 | 0 | 137 |

## View 3 — Active relevant verses not connected to any anchor

Four sub-views at increasing scope:
- **3a:** relevant non-anchor vc row in a group with zero anchors (group-level orphan)
- **3b:** relevant non-anchor vc row whose group_id is NULL (no group attached)
- **3c:** relevant non-anchor vc row on a term that has zero anchors (term-level orphan)
- **3d:** canonical verse with active OWNER `wa_verse_records` but no anchor row anywhere in any registry (verse-level orphan)

**3a — relevant verses in anchor-less groups: 0** (out of 28,139 total non-anchor relevant rows in active groups)

### 3a — Top 20 anchor-less groups by orphan-verse count

| Reg | Word | Group | Strong's | Verses without anchor |
|---:|---|---|---|---:|

**3b — relevant verses with no group at all: 0**

**3c — relevant verses on terms with zero anchors (term-level orphan): 0** across 0 terms

### 3d — Canonical verses with active OWNER but no anchor anywhere

- Total distinct canonical verses with active OWNER `wa_verse_records`: 23,294
- Of those, anchored somewhere: **3,542** (15.2%)
- **Unanchored anywhere: 19,752** (84.8%)

## Summary

- Zero-anchor registries: **11**
- 1-2 anchor registries: **11**
- OWNER terms with verses pulled but no anchor: **368** (rel_vc>0: 0, group orphan: 51, never inspected: 317)
- Relevant verses in anchor-less groups (3a): **0**
- Relevant verses with no group (3b): **0**
- Relevant verses on terms with zero anchors (3c): **0**
- Canonical verses unanchored anywhere (3d): **19,752**
