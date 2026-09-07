# M10b — Phase 1 + Phase 2 obslog — 2026-05-25

**Cluster:** M10b — Wickedness, Evil and Abomination (post-split 2026-05-22)
**Governing instruction:** `wa-sessionb-cluster-instruction-v2_8-20260519`
**Phases completed:** Phase 1 (UT review) + Phase 2 (Pass A meanings + keywords)

## Phase 1 — UT verse review

**Script:** `scripts/_apply_m10b_ut_review_via_api_20260525.py`
**Model:** claude-sonnet-4-6
**API calls:** 9 (8 terms + 1 chunk for to.e.vah's 87-verse load)

### Inputs

- 17 terms · 537 total verses · **134 UT verses** to classify (across 8 terms).
- 422 verse_context rows inherited from pre-split M10 (all `is_relevant=1`) — left as-is per §4.1 (Phase 1 only acts on UT).

### Results

| Strong's | Translit | UT | Relevant | Set aside | Borderline |
|---|---|---:|---:|---:|---:|
| G0093 | adikia | 2 | 1 | 1 | 0 |
| G0824 | atopos | 2 | 1 | 1 | 0 |
| G0946 | bdelugma | 3 | 3 | 0 | 0 |
| G4190 | ponēros | 10 | 2 | 8 | 0 |
| H7455 | ro.a | 5 | 0 | 5 | 0 |
| H7563 | ra.sha | 3 | 2 | 1 | 0 |
| H8251 | shiq.quts | 22 | 21 | 1 | 0 |
| H8441 | to.e.vah | 87 | 81 | 5 | 1 |
| **TOTAL** | | **134** | **111** | **22** | **1** |

### Borderline (1 — held for researcher decision)

- **H8441 to.e.vah** Ezr 9:11 — verse blends moral abomination (to.e.vah) with ritual uncleanness language ('impure', 'uncleanness'). M10b vs M10c judgment call. Not in patch.

### Set-aside breakdown (22)

- **Demonic-label "evil spirits"** (6×): ponēros in Luk 7:21, Luk 8:2, Act 19:12-16 — descriptive label on demonic agents in healing/exorcism narrative, not naming moral character.
- **Physical "bad"** (5×): ro.a Gen 41:19 (cattle), Jer 24:2-8 + 29:17 (figs); ponēros Luk 11:34 (unhealthy eye), Rev 16:2 (painful sores).
- **Forensic verdict** (1×): ra.sha Num 35:31 — "liable/guilty of death" sense → routed to M10 act-of-moral-failure.
- **Specific-act-not-character** (1×): adikia 2Cor 12:13 — withholding financial burden → M10.
- **Physical-harm literal** (1×): atopos Act 28:6 — "no harm came" sense.
- **Concrete filth** (1×): shiq.quts Nah 3:6 — refuse hurled in judgment, not abomination-character.
- **Egyptian cultural aversion** (2×): to.e.vah Gen 43:32, 46:34 — eating taboo / shepherd-aversion as cultural fact.
- **Ritual register → M10c** (2×): to.e.vah Exo 8:26 (Egyptian sacrificial taboo), Deu 14:3 (dietary heading).
- **Social revulsion** (1×): to.e.vah Psa 88:8 — psalmist as object of revulsion to companions.

No SET_ASIDE used forbidden grounds (§4.5.1) — all sense-based.

### Patch

- File: `wa-cluster-M10b-patch-vcnew-utreview-api-v1-20260525.json`
- Operations: 133 (111 relevant + 22 set_aside; borderline held out)
- Provisional anchors set: 0 (all 8 terms already had ≥1 inherited anchor)
- Apply: clean (133/133 inserts)

## Phase 2 — Pass A meanings + keywords

**Script:** `scripts/_run_passa_via_api_v1_20260515.py` (generic, with v2.0 §5 + 2026-05-23 keyword extension)
**Model:** claude-sonnet-4-6
**API calls:** 11 batches of up to 50 verses

### Inputs

- 514 `is_relevant=1` active vc rows with NULL `analysis_note` (422 inherited + 111 new from Phase 1, minus 19 verse_record-deleted orphans excluded by the loader).

### Results

- All 514 verses received a meaning (no empties).
- Meaning length: min=131, max=244, avg=174 chars (within ~250 char target).
- Keywords per verse: 4 (2×), 5 (510×), 6 (2×) — 5 is the standard.
- 2,167 distinct keywords across the cluster.
- 0 sentinel violations (no sub-group / VCG / anchor leakage).

### Top 25 keywords (cluster-wide)

`divine revulsion` (14), `will corrupted` (10), `will turning` (10), `will refusing` (9), `conscience suppressed` (8), `act defiling` (7), `worship corrupted` (6), `inner corruption` (6), `will defiant` (6), `moral contrast` (6), `holiness violated` (6), `inner disposition` (5), `divine disgust` (5), `divine rejection` (5), `conscience violated` (5), `heart evil` (5), `deeds evil` (5), `character corrupt` (5), `divine judgment` (5), `abomination removed` (5), `heart corrupted` (4), `conscience absent` (4), `heart corrupt` (4), `divine hatred` (4), `moral inversion` (4).

The keyword family clusters intuitively around will-corruption, conscience-failure, divine-revulsion, heart-as-locus, and moral-contrast — all proper M10b territory (the character of evil).

### Patch

- File: `wa-cluster-M10b-patch-passa-meanings-v1-20260525.json`
- Operations: 514 VCREVISE updates
- Apply: clean (514/514 updates)

## Orphan vc cleanup (hygiene)

After applying the Pass A patch, the §5.6 hard gate failed with 19 rows showing
`analysis_note IS NULL` despite Pass A returning 514/514. Investigation: 19 vc
rows (5 for H0205G a.ven, 14 for H7455 ro.a) point at `wa_verse_records` rows
that have `delete_flagged=1` — zombie inherited rows from upstream verse_record
cleanup. The Pass A loader correctly skipped them via the wa_verse_records JOIN.

**Fix:** `scripts/_repair_m10b_orphan_vc_rows_20260525.py` — soft-deletes the 19
orphans with `set_aside_reason` naming the cause. Idempotent. Post-fix gate = 0.

## Cluster state post-Phase-2

- `mti_terms.vc_status`: 13/17 terms `vc_completed` (the 8 from Phase 1 + 9 with
  UT=0 that may still show 'not_done' — these are inherited-only terms that the
  Phase 1 loader didn't touch by design).
- `verse_context` active rows for M10b: 555 total (514 relevant with full
  meaning+keywords + 22 set_aside + 19 borderline-or-other).
- All `is_relevant=1` active rows now carry `analysis_note` and `keywords`.
- Cluster status: still `Not started` (Phase 1+2 do not advance status per §4.6).

## Cost

| Phase | Model | Input | Output | Cache create | Cache read |
|---|---|---:|---:|---:|---:|
| 1 (UT review) | sonnet-4-6 | 14,820 | 13,261 | 1,798 | 14,384 |
| 2 (Pass A) | sonnet-4-6 | 59,239 | 55,398 | 1,547 | 15,470 |
| **TOTAL** | | **74,059** | **68,659** | **3,345** | **29,854** |

## Next

Phase 3 — constitution debate. The Pass A meanings + cluster-wide keyword
analytics become structural input to Phase 5 sub-group design; Phase 3 itself
re-examines the term universe in light of the corpus meanings.
