# Cluster input coverage audit — M15

**Generated:** 2026-05-30 07:06

**Inputs audited:** 7 chapter input file(s) in `Sessions/Session_Clusters/M15/inputs/`
- `ch1`
- `ch2`
- `ch3`
- `ch4`
- `ch5`
- `ch6`
- `ch7`

---

## DB evidence inventory

| Evidence type | Total in DB |
|---|---|
| `cluster_finding` (active) | 1724 |
| ` - cluster-synthesis` | 212 |
| ` - per-characteristic` | 1512 |
| `cluster_subgroup` (active) | 9 |
| `characteristic` (active) | 8 |
| `verse_context_group` (active) | 55 |
| `verse_context.is_anchor=1` (active) | 55 |
| `cluster_observation` (active) | 0 |
| `mti_term_subgroup` links (active) | 123 |

### Findings by tier

| Tier | Total | Cluster-synth | Per-char |
|---|---|---|---|
| T0 | 111 | 15 | 96 |
| T1 | 218 | 26 | 192 |
| T2 | 292 | 44 | 248 |
| T3 | 297 | 33 | 264 |
| T4 | 216 | 24 | 192 |
| T5 | 189 | 21 | 168 |
| T6 | 221 | 29 | 192 |
| T7 | 180 | 20 | 160 |

### Findings by status

| Status | Count |
|---|---|
| cluster_synthesis | 23 |
| finding | 1454 |
| gap | 9 |
| silent | 238 |

---

## Coverage gaps

**Total missing evidence rows: 12**

### Findings (1701 scope-groups in DB, 9 not referenced)

**Missing by tier:** T7=9

**Missing by status:** finding=1, gap=8

**Missing by scope:** cluster-synth=1, per-char=8

First 30 missing finding scope-groups:

| question_code | tier | status | scope | char | preview |
|---|---|---|---|---|---|
| T7.1.8 | T7 | gap | char#92 | Wisdom as holistic inner character and orientation | LXX investigation required for M15-A. The LXX rendering of cha.kham/chok.mah by sophia establishes the primary Greek-Heb |
| T7.1.8 | T7 | gap | char#93 | Understanding as inner perceptive faculty | LXX investigation required for M15-B. The LXX rendering of bin/te.vu.nah vocabulary and its relationship to the NT sunes |
| T7.1.8 | T7 | gap | char#94 | Knowledge as inner content and covenantal knowing | LXX investigation required for M15-C. The LXX rendering of ya.da vocabulary and the relationship between Hebrew relation |
| T7.1.8 | T7 | gap | char#95 | Discernment and practical judgment | LXX investigation required for M15-D. The LXX rendering of sa.khal, cha.shav, ta.am and their relationship to NT diakrin |
| T7.1.8 | T7 | gap | char#96 | Deliberative planning, counsel, and purposive intent | LXX investigation required for M15-E. The LXX rendering of ya.ats/e.tsah and its relationship to NT boulē/boulomai requi |
| T7.1.8 | T7 | gap | char#97 | Meditative and reflective inner activity | LXX investigation required for M15-F. The LXX rendering of si.ach/ha.gut vocabulary and its relationship to NT dialogizo |
| T7.1.8 | T7 | gap | char#98 | Inner thought-content — the mind's formed thoughts | LXX investigation required for M15-G. The LXX rendering of ra.yon/re.a/mad.da and their relationship to NT noēma/ennoia/ |
| T7.1.8 | T7 | gap | char#91 | Logos — the word as inner-being engagement | LXX investigation required for M15-H. The LXX use of logos and its relationship to the NT logos theology (especially in  |
| T7.1.8 | T7 | finding | synth | — | [BOUNDARY — structural characterisation note only; full catalogue pass not applicable per §11 BOUNDARY treatment rule] |

### Sub-groups (non-BOUNDARY: 8, missing: 0)

All non-BOUNDARY sub-groups referenced.

BOUNDARY sub-groups: 1 in DB; 0 referenced; 1 missing.
- `BOUNDARY` — Functional, supporting, and cluster-reassignment candidates

### Characteristics (8 in DB, 0 missing)

All characteristic short_names referenced.

### Verse-context groups (55 in DB, 1 missing)

- `M15-BOUNDARY-VCG01`

### Anchor verses (55 active anchors in DB, 1 not referenced)

Missing anchors group by VCG (first 30):
- `M15-BOUNDARY-VCG01` — 1 unreferenced anchor(s)

### Cluster observations (0 in DB, 0 not in any chapter input)

No active observations to route.

### Sub-group term inventory (123 term-links in DB, 31 not in chapter inputs)

**Term metadata (Strong's / transliteration / gloss) is not in chapter inputs.** Previously surfaced in appendix A; retired by v1_0 publishing instruction.

- **Wisdom as holistic inner character and orientation** — 4 terms not in inputs: H8454 (tu.shiy.yah), G4679 (sofizo), H2445 (chak.kim), H0999 (bi.nah)
- **Understanding as inner perceptive faculty** — 9 terms not in inputs: H0999 (bi.nah), G1226 (diabebaioō), G1328 (diermēneutēs), G1503 (eikō), G2058 (hermēneia) + 4 more
- **Discernment and practical judgment** — 2 terms not in inputs: G0145 (aisthētērion), H6191 (a.rom)
- **Deliberative planning, counsel, and purposive intent** — 6 terms not in inputs: H5779 (uts), H2808 (chesh.bon), G4388 (protithēmi), H6245B (a.shat), H6246 (a.shit) + 1 more
- **Functional, supporting, and cluster-reassignment candidates** — 10 terms not in inputs: G4894 (suneidō), G3177 (methermēneuō), G1231 (diaginōskō), G3312 (meristēs), G2058 (hermēneia) + 5 more

### VCG context descriptions (55 in DB, 55 not in chapter inputs)

**VCG context descriptions (the meaning-group definitions) are not surfaced in chapter inputs.** These define what each meaning-group is about. AI must rely on inferring from the anchor verses + their analysis_note.
- 55 VCGs have a `context_description` in the DB that is not in the chapter inputs.

---

## Verdict

FAIL — DB evidence is not fully represented in the 7 chapter input files. See gaps above. Either update the generator to include the missing evidence, or update the publishing instruction to explicitly exclude these row types.
