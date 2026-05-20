# wa-obslog-M08-phase1-ut-v1-20260520

**Cluster:** M08 — Pride, Arrogance and Boasting
**Phase:** 1 — UT verse review (CC, JSON template + API)
**Session date:** 2026-05-20
**Researcher:** Leroux
**AI:** Claude API (claude-sonnet-4-6) for batch classification
**CC:** Claude Opus 4.7
**Governing instruction:** `Workflow/Instructions/wa-sessionb-cluster-instruction-v2_8-20260519.md` §4
**Preceding cluster:** M07 (closed 2026-05-20)

---

## SESSION OPEN — 2026-05-20

### Step 1 — Global rules loaded

`wa-global-rules-all` [current]; startup ceremony per `wa-global-rules-startup` [current].

### Step 2 — Schema check

- `EXPECTED_SCHEMA_VERSION=3.24.0` (M50 applied); DB matches.

### Step 3 — Entry inventory

| Metric | Value |
|---|---|
| `cluster.status` pre-session | `Not started` (valid v2_8 §3 entry state) |
| `cluster.short_name` | Pride |
| mti_terms in scope | **49** (42 `extracted` + 7 `extracted_thin`) |
| Contributing registries | 13 (ambition, boldness, delight, dignity, mind, praise, **pride** [home], self-control, will, strength, power, authority, being) |
| Existing `verse_context` rows | 476 (466 `is_relevant=1` + 10 set-aside) |
| **UT verse-term pairs (Phase 1 to-do)** | **224** |
| Science extract | ✓ `Workflow/Sciences/wa-m08-pride-scienceextract-v1_0-20260513.md` (16.2 KB) |
| Stale registry-level flags | none (all 13 registries `phase1_status='Complete'`) |

UT pair distribution (top 15):

| Strong's | Translit | UT count |
|---|---|---:|
| H7311A | rum (to be high / lifted up) | 103 |
| H6967 | qo.mah (stature) | 36 |
| H1364 | ga.vo.ah (high / haughty) | 27 |
| H4791 | ma.rom (height) | 20 |
| H1363 | go.vah (pride / height) | 8 |
| G5308 | hupsēlos | 8 |
| G0757 | archō | 7 |
| H1347 | ga.on (pride / majesty) | 6 |
| H1346 | ga.a.vah (pride / majesty) | 3 |
| H1342 | ga.ah (to be exalted) | 2 |
| (5 more, 1 each) | | 5 |
| **Total** | | **224** |

The "height / lifted up / exaltation" vocabulary dominates — terms that operate across a pride / honour / majesty / divine-exaltation continuum, which makes the relevant/set-aside distinction analytically important.

### Step 4 — Session-open script

Advance `cluster.M08.status`: `Not started` → `Data - In Progress`.
(No stale registry flags to clear — all 13 contributing registries are clean.)

### Step 5 — Phase 1 UT review

Script: `scripts/_apply_m08_ut_review_via_api_20260520.py` — Pride-domain system prompt; claude-sonnet-4-6; chunk size 50.

Outputs:
- `Sessions/Session_Clusters/M08/wa-cluster-M08-patch-vcnew-utreview-api-v1-20260520.json`
- `Sessions/Session_Clusters/M08/WA-M08-UT-verse-review-api-v1-20260520.md`
- `Sessions/Session_Clusters/M08/WA-M08-UT-api-raw-responses-20260520.json`

Apply via `apply_session_patch.py`.

---

*Phase 1 obslog opening complete.*
