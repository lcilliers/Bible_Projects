# M38 Salvation — Phase A Plan

**Cluster:** M38 Salvation
**Phase:** A (Read + Meaning per v3_0 §5)
**Date:** 2026-05-28

Per v3_0 §5, Phase A is owned by CC programmatically (no AI chat). Two sub-steps: A.1 UT classification (IB / CONTEXTUAL / OUT per verse) and A.2 Pass A meaning + keywords (for IB verses).

---

## Inputs to Phase A

- 13 active mti_terms assigned to M38 (cluster_code='M38', delete_flagged=0)
- 356 active verses across these terms (via wa_verse_records.mti_term_id)
- 320 inherited verse_context rows from registry-level work (all is_relevant=1)
- 36 gap verses with no verse_context row yet

---

## Treatment of the 320 inherited records — RIGOROUS PATH (researcher direction 2026-05-28)

The 320 inherited records came from six different registries (mercy, debauchery, division, yielding, strength, power), each operating with its own registry-level inner-being lens. The is_relevant=1 verdict under "mercy" or "strength" may not equate to is_relevant=1 under "salvation". The propitiation set is already explicitly flagged vc_status='to_revise'.

**Researcher direction 2026-05-28:** "the previous assignments during registry work may have been biased and these verses is likely to belong to their own characteristic, which may also be relevant in mercy and strength clusters. if in doubt, then redo properly — cost is OK."

**Approach:** re-classify all 356 verses afresh via UT review under the M38 cluster lens.

- For gap verses (36): create new verse_context rows with the new UT verdict.
- For existing verses (320): update is_relevant + record ut_class for the new classification.
- Where the new UT verdict is is_relevant=0 (CONTEXTUAL or OUT), the verse moves out of M38's IB-relevant set. Prior anchor/related flags from registry-level work will be retained on the row but reviewed at Phase B (when sub-group structure decisions are made).
- Where the new UT verdict is is_relevant=1 (IB), Pass A then writes fresh meaning + keywords.

Pass A writes new content regardless — no inherited meanings or keywords exist (the analysis_note and keywords fields are empty across all 320 inherited records). The rigorous-path decision only affects the UT classification stage.

---

## Cluster characteristic statement (working — Pass A input)

This statement is **provisional** and is a Phase A input only. It is **not** a constitution decision. Phase B will revise as needed.

> M38's term inventory spans three related semantic registers:
> 1. Salvation / rescue / deliverance vocabulary (sōzō, sōtēr, soteria, sōtērion, ye.shu.ah, pa.dah) — the rescue/deliverance proper.
> 2. Propitiation / atonement vocabulary (hilaskomai, hilasmos, hilastērios, hileōs, ka.phar) — the means by which salvation is effected.
> 3. Giving / gift vocabulary (dōrea, dōrēma) — where the giving carries a salvation-relevant inner-being signal.
>
> For Phase A UT review: classify each verse for whether it evidences inner-being content related to any of these three registers — being saved, being atoned-for, or receiving as gift in a salvation-relevant context. Whether these three registers constitute one coherent cluster or should be partly carved off is a Phase B question that this Phase A must not pre-judge.

Pass A meanings should describe the verse's salvation/atonement/gift content in plain English, without forcing connections across the three registers.

---

## Phase A execution sequence

### Step 1 — Build M38 UT review script

Modelled on `scripts/_apply_m10c_ut_review_via_api_20260526.py` but extended to handle BOTH gap verses (insert new vc row) AND existing verses (update is_relevant on existing vc row). Cluster-specific system prompt encodes the working characteristic statement above. Output:

- `Sessions/Session_Clusters/M38/wa-cluster-M38-patch-utreview-api-v1-20260528.json` — combined VCNEW + VCREVISE patch
- `Sessions/Session_Clusters/M38/wa-cluster-M38-ut-verse-review-api-v1-20260528.md` — log
- `Sessions/Session_Clusters/M38/wa-cluster-M38-ut-api-raw-responses-v1-20260528.json` — raw API output

**Scope:** all 356 active verses (rigorous path per researcher direction).

**API cost:** ~356 × small Sonnet call ≈ $1.00–2.00.

### Step 2 — Apply UT patch

`python scripts/apply_session_patch.py --dry-run <path>` then live apply.

### Step 3 — Run Pass A across all is_relevant=1 verses

Uses cluster-agnostic `scripts/_run_passa_via_api_v1_20260515.py --m-cluster M38`.

The script requires a `--characteristic-file` argument pointing to a markdown file with the cluster characteristic statement. I will write `Sessions/Session_Clusters/M38/wa-cluster-M38-passa-characteristic-v1-20260528.md`.

**Scope:** ~320 inherited + (any IB classifications from step 1).

**API cost:** ~320 × medium Sonnet call ≈ $3–5.

### Step 4 — Apply Pass A patch

`python scripts/apply_session_patch.py --dry-run <path>` then live apply.

### Step 5 — Build keyword analytics report

Per v3_0 §5.2 final paragraph: `wa-cluster-M38-keyword-analytics-v1-{date}.md` — frequency tables, top tokens, top co-occurrence pairs, per-term keyword density. Cluster-level (no sub-groups exist yet at Phase A).

CC mechanical work. No API cost.

### Step 6 — Build Pass A summary report

Per v3_0 §5.3: `wa-cluster-M38-pass-a-summary-v1-{date}.md` — per-term verse counts, IB / CONTEXTUAL / OUT breakdown, sample meanings.

CC mechanical work. No API cost.

### Step 7 — Status transition

`cluster.status` `Not started` → `Data - In Progress`.

---

## Total Phase A cost estimate (rigorous path)

- API: ~$4–7 total
  - UT review on all 356 verses: ~$1–2
  - Pass A on resulting IB verses (likely ~300+): ~$3–5
- Time: ~30–60 minutes for the API runs depending on rate-limiting

---

## What to watch for during Phase A (per pre-analysis observations)

1. **The free-gift register (dōrea, dōrēma)** — 13 verses. If Pass A meanings show these verses are about general giving rather than salvation-gift, flag for Phase B B.1 TRANSFERS verdict.
2. **The propitiation set under registry "mercy" — vc_status='to_revise'** — Pass A meanings under M38 context may diverge from prior mercy-context meanings. Compare with M26 Righteousness's Justification characteristic (the previous atonement analysis) at Phase B.
3. **The volume-dominance of sōzō + ka.phar** — keyword analytics may be skewed by these two. Per-term keyword density helps see this.
4. **Hebrew/Greek asymmetry** — 7 Greek vs 3 Hebrew terms (+ ka.phar as the largest Hebrew). Whether the OT and NT salvation-registers differ structurally should emerge in keyword patterns.
5. **Sense-splits** — sōzō has at least three known senses (rescue from physical danger; heal; save eschatologically). Whether the Pass A meanings cluster around these senses or treat sōzō as one undifferentiated term is worth watching.

---

## Researcher direction received 2026-05-28

- ✅ Rigorous path approved — re-classify all 356 verses afresh under M38 lens.
- ✅ Cost budget approved (~$4–7 total).
- ⏳ Working cluster characteristic statement to be reviewed at next checkpoint (after CC writes the UT review script with it embedded).

CC proceeds to:
1. Write the M38 UT review script (with embedded cluster characteristic).
2. Write the Pass A characteristic file.
3. Dry-run test on small subset before live execution.
4. Execute UT review + apply patch.
5. Execute Pass A + apply patch.
6. Build keyword analytics + Pass A summary reports.
7. Status transition.

---

*Phase A plan v1 — 2026-05-28. Approved for rigorous-path execution.*
