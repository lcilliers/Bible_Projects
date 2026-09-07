# wa-obslog-M07-phase1-ut-v1-20260519

**Cluster:** M07 — Shame, Disgrace and Humiliation
**Phase:** 1 — UT verse review (CC, JSON template + API)
**Session date:** 2026-05-19
**Researcher:** Leroux
**AI:** Claude API (claude-sonnet-4-6) for batch classification
**CC:** Claude Opus 4.7
**Governing instruction:** `Workflow/Instructions/wa-sessionb-cluster-instruction-v2_6-20260519.md` §4
**Preceding session:** `WA-M07-session-start-prep-v1-20260519.md`

---

## SESSION OPEN — 2026-05-19

### Step 1 — Global rules loaded

`wa-global-rules-all-v{current}.md` loaded; startup ceremony per `wa-global-rules-startup [current]` complete.

### Step 2 — Cluster status check

- Cluster: M07 (Shame, Disgrace and Humiliation)
- Pre-session `cluster.status`: `Not started` (per v2_6 §3 — valid entry state).
- M04 just closed (`Analysis Completed`, dir-006-closure applied 2026-05-19).

### Step 3 — Schema check

- `EXPECTED_SCHEMA_VERSION=3.24.0` (M50 applied).
- DB schema_version = 3.24.0 ✓.

### Step 4 — Phase 1 entry inventory

From `WA-M07-session-start-prep-v1-20260519.md`:

| Metric | Value |
|---|---|
| mti_terms in scope | 36 |
| Existing verse_context rows | 565 (431 relevant + 134 set-aside) |
| **UT verse-term pairs to classify** | **112** |
| Pass A meanings populated (carry-forward for Phase 2) | 0 / 431 |

UT pair distribution (per term, sorted):

| Strong's | Translit | UT count |
|---|---|---:|
| H0954 | bosh | 103 |
| H8213 | sha.phel | 5 |
| H2659 | cha.pher | 1 |
| (3 more, 1 each) | | 3 |
| **Total** | | **112** |

103 of the 112 UT pairs are on `bosh` (the primary OT shame term). One API batch will handle most of the work.

### Step 5 — Housekeeping: stale `reg#146 shame.phase1_status='In Progress'`

Pre-flight DB anomaly: `word_registry.id=146 (shame)` carries `phase1_status='In Progress'` despite `last_automation_run='AUDITED'` (RUN-20260325) and `verse_context_status='Complete'`. Engine work finished March 2026. This is a stale value; advancing to `Complete` to clean the registry table state before Phase 1 fires.

### Step 6 — Phase 1 entry: advance cluster.status

Per v2_6 §3, valid entry states are `Not started` and `Data - In Progress`. M07 is at `Not started`; advance to `Data - In Progress` as the first cluster Phase 1 directive runs.

---

## PHASE 1 — UT VERSE REVIEW

### Inputs

Per v2_6 §4.1:

- **mti_terms** rows where `cluster_code='M07' AND status IN ('extracted','extracted_thin')` — 36 terms.
- **UT load**: `wa_verse_records` LEFT JOIN `verse_context` where the (verse_record_id, mti_term_id) pair has no `verse_context` row — 112 pairs.
- **System prompt** (constructed for M07): cluster characteristic statement (shame) + T1 framework + classification rubric (relevant / set_aside / borderline) + §1.1 in-scope examples block + strict-JSON output spec.
- **Per-verse data**: vc_id placeholder + vr_id + reference + Strong's + transliteration + gloss + language + verse_text + context_before + context_after + translation.

### Script

`scripts/_apply_m07_ut_review_via_api_20260519.py` — model: `claude-sonnet-4-6`. Chunk size 50 verses per call. System prompt cached.

### Outputs

- VCNEW patch: `Sessions/Session_Clusters/M07/wa-cluster-M07-patch-vcnew-utreview-api-v1-20260519.json`
- Review log: `Sessions/Session_Clusters/M07/WA-M07-UT-verse-review-api-v1-20260519.md`
- Raw API responses: `Sessions/Session_Clusters/M07/WA-M07-UT-api-raw-responses-20260519.json`

### Apply

`python scripts/apply_session_patch.py wa-cluster-M07-patch-vcnew-utreview-api-v1-20260519.json`

### Post-check

- UT pair count after apply = 0 (or equals the borderline count if any deferred).
- `verse_context` row count delta = (relevant + set_aside) = 112 minus borderlines.
- Borderlines logged in the review document for researcher decision.

---

*Phase 1 obslog opening complete. Next steps: status advance + housekeeping + run the API.*

---

## PHASE 1 — APPLIED (2026-05-19)

- Session-open script `_apply_m07_session_open_20260519.py` ran clean: cluster.status `Not started` → `Data - In Progress`; reg#146 shame.phase1_status `In Progress` → `Complete`.
- UT API run via `_apply_m07_ut_review_via_api_20260519.py` (claude-sonnet-4-6, system prompt cached across 6 term calls).
- Outcome tally (parser): **relevant 99 · set_aside 12 · borderline 1 = 112 ✓**.
- VCNEW patch `wa-cluster-M07-patch-vcnew-utreview-api-v1-20260519.json` applied: 111 inserts, 6 terms marked `vc_completed`.
- Borderline held: Judg 3:25 (`bosh` — ambiguous between social-awkwardness-from-delay and inner shame). Researcher decision deferred.
- `G0880 afōnos` flagged as "all-verses-fail" by the applier (its single UT verse classified set_aside). Candidate for exclusion review later.

Post-state: `verse_context` 565 → 676 (530 is_relevant + 146 set_aside). UT remaining: 1 (the borderline).

---

## PHASE 2 — PASS A MEANING RECORD (v2_6 §5)

- Fetch: 527 of 530 is_relevant rows needing analysis_note (the other 3 are orphan vc rows whose underlying `wa_verse_records.delete_flagged=1`; excluded from fetch by design).
- API run via `scripts/_run_passa_via_api_v1_20260515.py --m-cluster M07`: 11 batches × 50 (last 27). claude-sonnet-4-6.
- Total usage: input 71,993 · output 41,585.
- VCREVISE patch `wa-cluster-M07-patch-passa-meanings-v1-20260519.json` (527 ops) applied clean: 527 verse_context UPDATEs; all 36 M07 mti_terms now `vc_completed`.
- System prompt saved to `WA-M07-passa-system-prompt-20260519.txt`.
- Sample meanings spot-checked good (per-verse, plain English, no group/VCG language).
- AI correctly flagged Jer 9:24 (`H2617B che.sed`) as "positive steadfast love — does not evidence shame content"; this kind of signal is exactly what Phase 3 / Phase 8.5 will use for re-classification.

### Phase 2 cleanup queue (carried forward)

3 orphan vc rows (vc.is_relevant=1, vc.delete_flagged=0, but vr.delete_flagged=1) need disposition:

| vc_id | reference | strongs | translit |
|---:|---|---|---|
| 34973 | Php 3:19 | G0152 | aischunē |
| 37337 | Pro 25:10 | H2616B | cha.sad |
| 49397 | Php 3:2 | G2699 | katatomē |

Same pattern as M04 Step 1 orphan cleanup precedent. Resolution at Phase 3 or before Phase 8.5: either soft-delete the orphan vc rows, restore the vr rows if they should be active, or treat as out-of-scope. Not blocking Phase 2 completion.

**Phase 2 functionally complete on 527 healthy rows.** Ready for Phase 3 — Cluster constitution debate (v2_6 §6).

