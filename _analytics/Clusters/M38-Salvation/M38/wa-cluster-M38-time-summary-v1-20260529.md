# M38 processing time summary

**Generated:** 2026-05-29
**Source:** file mtimes in `Sessions/Session_Clusters/M38/`, `cluster_finding.created_at` rows in DB, `cluster_subgroup.created_at`, `cluster.last_updated_date`.

All timestamps below are local clock time on the day they occurred. M38 ran end-to-end across a single day (2026-05-28) plus the morning of 2026-05-29 for Session C inputs.

---

## Phase-by-phase timeline

| Phase | Start | End | Duration | Notes |
|---|---|---|---:|---|
| Pre-pipeline notes | 06:21 | 06:54 | 33 min | Researcher's pre-analysis observations; Phase A plan drafted |
| **Phase A** — read + meaning | 06:54 | 07:26 | 32 min | UT review (06:54→07:10) · Pass A meanings (07:10→07:23) · keyword analytics + summary (07:23→07:26) |
| **Phase B** — constitution + sub-groups + VCGs | 07:59 | 10:03 | 2 h 4 min | B.1 constitution (07:59→08:07) · B.2 sub-group design + repair (08:17→08:25) · B.3 VCG design across 6 sub-groups (08:53→08:57) · M38-A re-run (08:59→09:01) · final mapping v2 (10:03) |
| Inter-phase gap | 10:03 | 14:06 | 4 h | Lunch / orchestration / re-planning |
| **Phase C** — structural apply | 09:03 | 09:03 | < 1 min | `cluster_subgroup` rows written; status flip recorded |
| **Phase D Stage A** — char findings (1,323 rows) | 14:06 | 17:11 | 3 h 5 min | char3 (14:52→15:06) · char6 (16:22→16:36) · chars 2/4/1/5/7 batch with re-runs (16:57→17:11) |
| **Phase D Stage B** — cluster synthesis (189 rows) | 17:11 | 17:27 | 16 min | DB load complete at 17:27; tier files re-written at 18:26 after T2/T3/T7 re-runs |
| **Phase E** — essay drafting + DOCX render | 18:26 | 18:43 | 17 min | Essay md (18:43:05) + DOCX (18:43:33) |
| **Phase E.audit** — v2_5 audit run | 18:43 | 18:52 | 9 min | Surfaced 1 RESCUE + 5 missing anchors + 177 ungrounded |
| **Session C inputs** — chapter generator | 05:12 (2026-05-29) | 05:12 | < 1 min | 10 chapter input files generated |

### Totals

| Metric | Value |
|---|---:|
| Active processing (Phase A + B + C + D + E + audit) | **~6 h 45 min** |
| Wall clock (first action → essay + audit done) | **~12 h 31 min** (incl. ~4 h inter-phase gap) |
| Single-day pipeline (06:21 → 18:52) | yes — all phases done same day |

---

## Phase A detail

| Time | Event | Output |
|---|---|---|
| 06:21:46 | Pre-analysis notes | `wa-cluster-M38-pre-analysis-v1-20260528.md` |
| 06:54:46 | Phase A plan | `wa-cluster-M38-phase-a-plan-v1-20260528.md` |
| 07:10:04 | UT review (API) | 310 IB verses, 45 set-aside, 2 borderline |
| 07:12:51 | Pass A characteristic input | `wa-cluster-M38-passa-characteristic-v1-20260528.md` |
| 07:23:41 | Pass A meanings applied (API) | 310 meanings |
| 07:25:04 | Keyword analytics | 728 distinct keywords surfaced "priest mediating" axis |
| 07:26:06 | Pass A summary | Phase A close |

## Phase B detail

| Time | Event | Output |
|---|---|---|
| 07:59:00 | Constitution input | `wa-cluster-M38-constitution-v1-20260528.md` |
| 08:07:41 | B.1 constitution debate (API) | 11 STAYS + 2 BOUNDARY verdicts |
| 08:17:20 | B.2 input written | sub-group accommodation for 2 BOUNDARYs |
| 08:21:35 | B.2 design (API) | initial 7 sub-groups, coverage gaps surfaced |
| 08:25:07 | B.2 repair (API) | gaps closed, final 7 sub-groups |
| 08:53:14 → 08:57:27 | B.3 VCG design B/C/D/E/F/G (API) | per-sub-group VCG creation |
| 08:59:30 → 09:01:48 | M38-A re-run + repair | truncation fix for 121-verse sub-group |
| 10:03:32 | Mapping v2 + VCG creation v2 | Phase B close |

## Phase D detail

| Time | Event | Rows |
|---|---|---:|
| 14:06–17:11 | Stage A per-char findings (Sonnet 4.6 API) | 1,323 char-scope |
| 14:52–15:06 | char3 — Healing wholeness | ~189 |
| 16:22–16:36 | char6 — Salvation anticipated | ~189 |
| 16:57–17:11 | chars 1, 2, 4, 5, 7 batch + re-runs | ~945 |
| 17:11–17:27 | Stage B cluster synthesis load | 189 cluster-scope |
| Total | | **1,512** |

---

## Cost-to-time relationship

| Phase | Approx cost | Time | Cost/min |
|---|---:|---|---:|
| Phase A | $0.56 + $0.60 | 32 min | ~$0.036/min |
| Phase B | $0.20 + $0.30 + $0.70 | 2 h 4 min | ~$0.010/min |
| Phase D Stage A | ~$5.00 | 3 h 5 min | ~$0.027/min |
| Phase D Stage B | ~$2.00 | 16 min | ~$0.125/min |
| **Total** | **~$9.40** | **~6 h 45 min active** | **~$0.023/min** |

---

## Observations on the timing

1. **Phase A was the fastest substantive phase** (32 min) — API-driven UT classification and Pass A meanings ran quickly because each call was bounded and the prompts were tight.
2. **Phase B was the longest pre-D phase** (2 h 4 min) — because it includes the cascading B.1 → B.2 → B.3 dependency and a re-run for M38-A truncation. Each sub-group's VCG design ran ~4-5 minutes; the re-run added ~3 minutes.
3. **The 4-hour inter-phase gap** (10:03 → 14:06) between Phase B close and Phase D start was unstructured. Likely an artefact of the conversation context — orchestration time, breaks, re-reading. In a tighter run this could compress significantly.
4. **Phase D Stage A took the bulk of API time** (3 h 5 min) — 7 characteristics × 4 tier-segments per characteristic = 28 API calls, plus re-runs for q_code drift on chars 1/2/4/5/7. Each segment averaged ~4-5 minutes.
5. **Phase D Stage B was efficient** once the per-tier approach was settled (16 min wall-clock; ~$2). Earlier 4-segment Stage B attempts hit max_tokens truncation and were abandoned.
6. **Phase E (essay + DOCX) was 17 min** — Opus 4.7 drafting in chat directly, no API costs.

The pipeline's total active processing time (~6 h 45 min) means a tighter run with no re-runs could plausibly complete a cluster in **4–5 hours of API + drafting time**.

---

## Engine-log note

The `engine_run_log` table tracks word-audit (`audit_word` mode) runs — not cluster pipeline runs. M38 phase activity is therefore not in `engine_run_log`. Phase markers had to be reconstructed from file mtimes and `cluster_finding.created_at` / `cluster_subgroup.created_at` row timestamps. Going forward, the obslog discipline saved as memory yesterday will provide a single canonical timeline document per cluster run.
