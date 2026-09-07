# M10c — Phase 1 + Phase 2 obslog — 2026-05-26

**Cluster:** M10c — Defilement and Impurity (post-split 2026-05-22)
**Governing instruction:** `wa-sessionb-cluster-instruction-v2_8-20260519`
**Phases:** Phase 1 (UT review) + Phase 2 (Pass A meanings + keywords)

## Phase 1 — UT verse review

**Script:** `scripts/_apply_m10c_ut_review_via_api_20260526.py` (cloned from M10b's, with M10c-specific SYSTEM_PROMPT)
**Model:** claude-sonnet-4-6
**API calls:** 2 (one per term)

### Inputs

- 8 terms · 275 total verses · **58 UT verses** to classify (across 2 terms; other 6 terms had UT=0)
- 217 verse_context rows inherited from pre-split M10 (all is_relevant=1) — left as-is per §4.1
- 0 orphan vc rows (clean vs M10b's 19)

### Results

| Strong's | Translit | UT | Relevant | Set aside | Borderline |
|---|---|---:|---:|---:|---:|
| H2930A | ta.me (verb) | 19 | 19 | 0 | 0 |
| H2931 | ta.me (adj) | 39 | 27 | 12 | 0 |
| **TOTAL** | | **58** | **46** | **12** | **0** |

### Set-aside breakdown (12)

All 12 set_aside reasons cite **dietary-list / legal-category classifications with no inner-being state content** — purely lexical uses where ta.me appears as a classifier label without describing a defilement state:

- **9 dietary-list entries** (Lev 11 + Deu 14 — "this animal is unclean"): Lev 11:4, 11:5, 11:6, 11:7, 11:29; Deu 14:7, 14:8, 14:10, 14:19
- **3 legal-category labels** (vow-redemption / firstborn-redemption procedural): Lev 27:11, 27:27; Num 18:15

No SET_ASIDE used forbidden grounds (§4.5.1) — all sense-based. The "bodily/sensory rather than spiritual" trap was explicitly addressed in the system prompt; classifier correctly distinguished dietary-classifier uses from defilement-state uses.

### VCNEW patch

- File: `wa-cluster-M10c-patch-vcnew-utreview-api-v1-20260526.json`
- Operations: 58 (46 relevant + 12 set_aside)
- Provisional anchors set: 0 (all 8 terms had inherited anchors)
- Apply: clean (58/58 inserts)

## Phase 2 — Pass A meanings + keywords

**Script:** `scripts/_run_passa_via_api_v1_20260515.py` (generic; v2.0 §5 + 2026-05-23 keyword extension)
**Model:** claude-sonnet-4-6
**API calls:** 6 batches of up to 50 verses

### Inputs

- 263 `is_relevant=1` active vc rows with NULL `analysis_note` (217 inherited + 46 new from Phase 1)

### Results

- All 263 verses received meaning + keywords (no empties).
- 1,031 distinct keywords cluster-wide.
- 0 sentinel violations.

### Top 20 keywords (cluster-wide)

| Count | Keyword |
|---:|---|
| 22 | status ritual |
| 18 | impurity contact |
| 14 | impurity bodily |
| 13 | status pronounced |
| 11 | authority ritual |
| 11 | exclusion ritual |
| 9 | contamination spreading |
| 8 | duration evening |
| 8 | boundary sacred |
| 7 | exclusion communal |
| 7 | cleansing required |
| 7 | body state |
| 7 | impurity inherent |
| 6 | will refusing |
| 6 | boundary bodily |
| 6 | contamination categorical |
| 5 | purification required |
| 5 | defilement transmitted |
| 5 | purity threatened |
| 4 | violation inadvertent |

The keyword family clusters around: status/state, contact/contamination/transmission, ritual exclusion/duration, body, sacred boundary, cleansing/purification. The vocabulary is clearly M10c-distinctive — different in shape from M10's sin-act terms or M10b's evil-character terms.

### VCREVISE patch

- File: `wa-cluster-M10c-patch-passa-meanings-v1-20260526.json`
- Operations: 263 VCREVISE updates
- Apply: clean (263/263 updates)

## §5.6 hard gate verification

```sql
SELECT COUNT(*) FROM verse_context vc
JOIN mti_terms mt ON mt.id = vc.mti_term_id
WHERE mt.cluster_code='M10c' AND vc.is_relevant=1
  AND COALESCE(vc.delete_flagged,0)=0 AND vc.analysis_note IS NULL;
-- Returns 0 ✓
```

**PASS.** All is_relevant=1 active rows in M10c have `analysis_note` and `keywords` populated.

## Cluster state post-Phase-2

- `mti_terms.vc_status`: 8/8 terms `vc_completed`
- `verse_context` active rows for M10c: 287 total (263 relevant + 12 set_aside + 12 pre-existing set_aside from inherited)
- All `is_relevant=1` active rows now carry `analysis_note` and `keywords`
- Cluster status: still `Not started` (Phase 1+2 do not advance status per §4.6)

## Cost

| Phase | Model | Input | Output | Cache create | Cache read |
|---|---|---:|---:|---:|---:|
| 1 (UT review) | sonnet-4-6 | 6,344 | 5,915 | 1,950 | 1,950 |
| 2 (Pass A) | sonnet-4-6 | 32,916 | 31,131 | 1,475 | 7,375 |
| **TOTAL** | | **39,260** | **37,046** | **3,425** | **9,325** |

## Comparison: M10c vs siblings

| Cluster | Terms | Total V | UT | Active relevant post-Phase-1 | Status |
|---|---:|---:|---:|---:|---|
| M10 (Sin/Guilt/Transgression) | 63 | ~1,475 | 43 | 1,325 | Analysis Completed (aspect_based) |
| M10b (Wickedness/Evil/Abomination) | 17 | 537 | 134 | 514 (515 after borderline) | Analysis Completed |
| **M10c (Defilement/Impurity)** | **8** | **275** | **58** | **263** | **`Not started` → Phase 3 next** |

M10c is the smallest of the three siblings. Its 8-term universe is tightly focused on defilement/impurity register; no overlap with sin-act (M10) or evil-character (M10b).

## Next

Phase 3 — constitution debate (AI, chat). All 8 terms expected to STAY in cluster (all squarely defilement vocabulary); main work will be detecting any inner moral-defilement vs ritual-defilement sub-corpus signals worth flagging as cross-register notes.
