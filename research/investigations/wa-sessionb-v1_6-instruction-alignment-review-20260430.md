# Session B Analysis Output v1_6 — Instruction Alignment Review

**Date:** 2026-04-30
**Reviewed file:** [Workflow/Instructions/wa-sessionb-analysis-output-v1_6-20260430.md](../../Workflow/Instructions/wa-sessionb-analysis-output-v1_6-20260430.md) (1,406 lines)
**Reviewer:** Claude Code
**Scope:** Confirm alignment with (a) the v2 architecture, (b) the second-tier catalogue and capture work landed 2026-04-30, (c) the researcher's stated understanding that "the only output from this instruction is the obslog and session log."

---

## 1. Headline finding — researcher's understanding is correct

**Under v2, the only AI outputs are the obslog and the session log.** §v2.2 in the instruction body states this directly: *"No patches submitted by AI. AI produces one comprehensive obslog `.md`. CC's Phase 2 writer parses the obslog and writes every category to its DB target."* §v2.6 reinforces it: *"What changes under v2 is the **delivery mechanism**: obslog → CC → DB instead of obslog → AI patches → CC apply."*

**The legacy v1 body of the instruction (lines 425–1399) still describes the patch model** — Type (b) patch construction, closing patches, the Analytic Word Output as a separate file, and a Handoff Signal listing five mandatory outputs. §v2.6 hand-waves that the body is "authoritative for the discipline" and only the delivery mechanism changes — but the body's prose is unambiguously patch-centric and contradicts §v2 in many concrete places. A reader following the body without §v2 would build a Type (b) patch and produce a separate analytic-word-output file. A reader following §v2 would not.

**Recommendation in one sentence:** strip the legacy patch-and-analytic-output mechanics out of the body, keep the analytical *discipline* the body describes, and consolidate the v2 mechanics that today live awkwardly in the §v2.x addendum.

---

## 2. Concrete contradictions inside the document (highest impact first)

### 2.1 Stage 2c output — separate file vs obslog block

| What §v2 says | What the body says |
|---|---|
| §v2.2 line 39: "Stage 2c chapters → `prose_section` with section_type_id `sb_s2c_ch1`..`sb_s2c_ch5`" | Stage 2c Output table line 1090–1098: output is `wa-[nnn]-[word]-sessionb-analytic-v1-[date].md` — a separate six-chapter document |
| §v2.8 markers expect chapters embedded in the obslog under `## Stage 2c — Chapter N: {title}` | Stage 2c Production Protocol (line 1223) walks the AI through writing chapters as if to an external file |
| §v2.10 line 307: "*Standalone second-tier output file retired*" | Naming Conventions table line 1395 still lists `wa-[nnn]-[word]-sessionb-analytic-v1-[date].md` |

**Recommendation:** delete the Stage 2c "external file" framing. Restate Stage 2c as: chapters are written **into the obslog** under the §v2.8 marker headings. CC parses them into `prose_section` rows.

### 2.2 Type (b) patch construction — fully contradicted

Lines 985–1017 walk the AI through:
> "Step 1 — Compile patch operations from Q&A Log. … Step 3 — Construct the patch. Patch name: `PATCH-[YYYYMMDD]-[nnn]-SESSIONB-V1.json`. Step 4 — Present for researcher approval. Step 5 — CC applies patch."

§v2.2 says "No patches submitted by AI" and the actual capture pipeline that ran for R023/R030/R062/R064/R068 today did NOT use any patch — CC parsed the obslog directly.

**Recommendation:** delete the entire `Type (b) Patch Construction` section (lines 985–1017). The §v2.8 obslog markers fully replace it. Delete §v2.6's reconciliation paragraph too — it tries to bridge two designs that don't need bridging once the patch language is removed.

### 2.3 Closing patch — fully contradicted

Lines 1322–1334:
> "Construct the closing patch: `word_registry.session_b_status = 'Analysis Complete'`. Patch name: `PATCH-[YYYYMMDD]-[nnn]-ANALYSIS-V1.json`. Present for researcher approval. Submit to CC."

§v2.8 already specifies that the obslog ends with `## Session Close` carrying `session_b_status: 'Analysis Complete'` and CC's parser writes it.

**Recommendation:** delete the Closing Patch section. Replace with: *"At session close, CC's writer extracts `session_b_status` from the `## Session Close` block (per §v2.8) and updates `word_registry.session_b_status` accordingly."*

### 2.4 Handoff Signal — five mandatory outputs reduces to two

Lines 1352–1357 list:

```
[ ] Observations log
[ ] Session log
[ ] Analytic Word Output: wa-[nnn]-[word]-sessionb-analytic-v1-[date].md
[ ] Type (b) patch: PATCH-[YYYYMMDD]-[nnn]-SESSIONB-V1.json (applied)
[ ] Closing patch: PATCH-[YYYYMMDD]-[nnn]-ANALYSIS-V1.json (applied)
```

Three of these (Analytic Word Output file, Type (b) patch, Closing patch) don't exist under v2.

**Recommendation:** reduce to two — observations log (= obslog, in current terminology) + session log. Optionally promote the obslog filename to drop the dated-suffix-and-version pair to a single canonical `wa-[nnn]-[word]-obslog-v[n]-[date].md` form (which is the form the existing capture work used: `wa-obslog-ro-067-goodness-anlys-v2-20260426.md` etc.).

### 2.5 Naming Conventions table — half the rows obsolete

Lines 1389–1399 list seven file conventions. Under v2, only the observations log and session log are produced by AI. The other five (analytic word output, Type (b) patch, supplementary patch, closing patch, Type (a) supplementary patch) either don't exist or are CC-internal mechanics.

**Recommendation:** trim to two rows. If supplementary Type (a) patches for Stage 1 corrections are still in the workflow (they are — see §3.4 below), keep that row but move it to the readiness instruction where it logically belongs.

### 2.6 Pipeline Position diagram — closing patch language

Line 350: *"Closing patch → session_b_status = Analysis Complete"*.

**Recommendation:** replace with *"Status update in obslog → CC writes `session_b_status`"*.

---

## 3. Alignment with the catalogue v2 work that landed today (2026-04-30)

### 3.1 question_code format — instruction proposes one form, DB carries another

**Instruction (§v2.8 line 173, §v2.10):**
> "`{tier_prompt_code}` is the prompt reference in the form `T{n}.{component}.P{prompt}` (e.g. `T1.3.P2`) — this becomes the `question_code` in `wa_obs_question_catalogue`."

**A RESEARCHER_DECISION item is flagged in the instruction itself** (line 179): *"CC must confirm this resolves correctly against `wa_obs_question_catalogue.question_code` before first application."*

**DB state today** (after the v2 catalogue migration I ran 2026-04-30):

| question_code in DB | tier | component_code | prompt_seq |
|---|---|---|---|
| `T0.1.1` | T0 | T0.1 | 1 |
| `T0.1.2` | T0 | T0.1 | 2 |
| `T0.1.3` | T0 | T0.1 | 3 |
| `T1.3.2` | T1 | T1.3 | 2 |

The DB uses `T{n}.{component}.{prompt}` (no `P` prefix on the prompt). The instruction proposes `T{n}.{component}.P{prompt}` (with `P`).

**Resolution required.** Two options:

- **(a) Update the instruction** to use `T{n}.{component}.{prompt}` — matches DB, simpler, parser doesn't need to strip `P`.
- **(b) Update the DB** — re-write 189 question_code values to add the `P` prefix. Mechanical but visible everywhere.

I recommend **(a)** — adjust the instruction. Less risk, and the DB-resident form is the operational truth the parser will hit.

### 3.2 finding_id format — instruction format vs what was written

**Instruction (§v2.7 line 94):** *"Tokens use the full finding_id format (`OBS-{registry:03d}-OBS-{seq:03d}`, …)"*

**DB state after capture today:** the 725 v2-derived findings written 2026-04-30 use `OBS-{registry:03d}-T2-{seq:03d}` (e.g. `OBS-064-T2-001`). The `T2` segment marks "catalogue v2" so the catalogue-v1 OBS-067-OBS-NNN tradition is preserved alongside.

**Resolution required.** Either:

- **(a) Update the instruction** to recognise `OBS-NNN-T2-MMM` as a valid token form — additive, doesn't disrupt v1 tokens.
- **(b) Stop using T2 and write second-tier findings as `OBS-NNN-OBS-MMM`** continuing the v1 sequence — would mean re-numbering 725 rows + breaking the deliberate distinction the capture script encoded.

I recommend **(a)** — the T2 marker is genuinely useful as it lets you write `WHERE finding_id LIKE 'OBS-%-T2-%'` to slice catalogue-v2 findings cleanly.

### 3.3 wa_finding_catalogue_links.status — instruction expects 'suggested'/'validated', capture wrote 'active'

**Instruction (Domain E line 1298):** *"Every active finding has a `wa_finding_catalogue_links` row with `status IN ('suggested','validated')`."*

**DB state today:**

| `status` value | Count |
|---|---:|
| `'validated'` | 488 |
| `'active'` | 934 (all from today's capture) |

The capture script I built and you approved used `'active'`. The instruction expects `'suggested'` or `'validated'`.

**Resolution required.** This needs an explicit decision because Domain E's check is a hard gate at Closure. Two options:

- **(a) Update the capture script** going forward and **migrate today's 934 rows** to `'validated'` (since the AI did directly produce them and they are the final answer per prompt) or `'suggested'` (since they aren't researcher-validated yet).
- **(b) Update the instruction's controlled vocabulary** to accept `'active'` as a valid status, OR drop the Domain E status check entirely under v2 (the catalogue link's existence and the capture's coverage value — full/partial/no_finding/not_applicable — are what matters; the status field becomes redundant).

I recommend **(b)** — the status field is doing redundant work. The link's `coverage` field carries the analytic meaning; `status` was a v1 lifecycle marker for "this link has been reviewed". Under v2, lifecycle is implicit in catalogue_version + link existence.

### 3.4 §v2.2 obslog→DB target table — minor wording / scope updates needed

The table at lines 36–45 maps obslog content to DB targets. Two things need touching:

- *"Stage 2b Q&A pairs (second-tier catalogue) → `wa_finding_catalogue_links` (with finding_id → source observation; coverage='full' / 'partial' / 'not_applicable')"* — missing `'no_finding'` (status S → silent). Today's capture script writes `'no_finding'` for status S, matching the existing schema. Recommendation: add `'no_finding'` to the row.
- *"GAP + word-specific questions → `wa_obs_question_catalogue` inserts"* — under the v2 catalogue, GAP questions raised mid-session would be inserted with `tier`/`component_code`/`prompt_seq` set if they belong to a specific tier, or with NULL tier (loose extension) if not. The instruction doesn't address this; capture script doesn't yet either. Worth flagging.

---

## 4. Issues that aren't contradictions but are worth surfacing

### 4.1 Schema readiness gate doesn't check for catalogue_version='v2-2026-04-29'

Lines 432–436 check that the catalogue table has rows, but not that the **v2** catalogue is loaded. After the migration today, 159 rows are still in the table with `status='redundant_v1', deleted=1`. A naive gate counting all rows would pass. Recommendation: add a check `wa_obs_question_catalogue WHERE catalogue_version='v2-2026-04-29' AND deleted=0 → ≥189 rows`.

### 4.2 Stage 2c chapter source → finding type mapping is dated

Lines 1100–1218 map each chapter to specific finding types from a v1-era controlled vocabulary (`MEANING_OBSERVATION`, `ETYMOLOGY`, `ROOT_FINDING`, etc.). The v2 capture writes `finding_type='OBSERVATION'` for all 725 second-tier findings — the type discrimination has effectively collapsed for v2 work. The chapter-mapping prose still reads as if findings will be tagged with these specific types.

**Recommendation:** acknowledge that under v2 the chapter-to-finding mapping is by content (and by `study_segment`/`pass_ref` carrying the tier-component pointer), not by `finding_type`. Or: re-introduce specific finding_type tagging in the capture path so the chapter mapping remains queryable. The first option is simpler.

### 4.3 §v2.7 prose-revision tokens reference more formats than CC currently extracts

Line 94 lists the citation token forms CC extracts: `OBS-{registry:03d}-OBS-{seq:03d}`, `SP-{registry:03d}-{seq:03d}`, `Q&A-NNN`, `Q###`, `DIM-NN-NNN`. Under v2 there's also:

- `OBS-{registry:03d}-T2-{seq:03d}` — second-tier finding (today's writes)
- `SB-{registry:03d}-T2-{seq:03d}` — second-tier gap flag (today's writes)
- `SP-{registry:03d}-T2-{seq:03d}` — second-tier SD pointer (today's writes)
- `RD-{registry:03d}-{seq:03d}` — RESEARCHER_DECISION flag (today's writes — new flag_code)

CC's chapter citation extractor will need to know about these. Recommendation: extend the v2.7 token list and the v2.9 resolution table accordingly.

### 4.4 §v2.10 closing summary requires CC parsing of stat tables

The closing summary (lines 271–288) requires AI to write a "Status Code Totals Across T0–T7" table by tier. CC's parser currently doesn't extract this — it would need to, if Closure depends on it being present. Recommendation: either drop the closing-summary requirement (the same data is computable from the per-prompt Q&A entries CC has already written), or add the table to CC's required-parse list.

### 4.5 Integrity rules SB-14 / SB-15 / SB-16 / SB-17 still reference patches

Lines 1377–1380 carry rules that explicitly require Type (b) patch confirmation, closing patch confirmation, and the five mandatory outputs. Under v2 these collapse to a much simpler discipline: did the obslog parse and write cleanly? Did the §N items reach a closure? Recommendation: rewrite these four rules in v2 terms.

---

## 5. What's actually working and well-aligned

To give a balanced picture — the §v2.x addendum sections are largely consistent with the catalogue work that landed today:

- §v2.1 inputs (registry data package + validation report + analytic status) — matches the per-word data packages [research/investigations/ai_question_test_bundle_20260429/](../../research/investigations/ai_question_test_bundle_20260429/) and the in-folder structure.
- §v2.3 §N open-item resolution discipline — the four resolution paths (Q&A / GAP / SD pointer / not_relevant) map cleanly to the capture script's output categories (catalogue link / new question / SD_POINTER flag / status note).
- §v2.4 citation discipline — was actually applied during capture (the OBS-NNN cross-references in finding bodies are detectable and the capture preview's `obs_refs` array verifies it).
- §v2.5 catalogue completeness — the capture handles all four coverage values (full/partial/no_finding/not_applicable) correctly.
- §v2.8 obslog format markers — these are the **single most important contribution of v1.6**. They are precise, consistent, and CC's parser can be built (or already is) to depend on them. Subject to the question_code format adjustment in §3.1 above, this section is the v2 spec.
- §v2.10 second-tier catalogue framing — accurate; matches the [WA-obs-question-catalogue-v2-2026-04-29.json](../../research/investigations/ai_question_test_bundle_20260429/WA-obs-question-catalogue-v2-2026-04-29.json) and the [data-adequacy-assessment](data-adequacy-assessment-v2-20260430.md).

---

## 6. Recommended next steps in priority order

1. **High — v1.7 cleanup pass.** Strip the legacy patch and analytic-output-file mechanics from the body. ~400 lines of deletions, no functional changes since v2 already supersedes them. Expected size: v1.6 → v1.7 drops from 1,406 → ~1,000 lines. Most of the deletions are §985–1017 (Type (b) patch), §1322–1334 (Closing patch), §1352–1357 (Handoff Signal), Stage 2c output table, Naming Conventions rows, integrity rules SB-14..SB-17.
2. **High — resolve the question_code format mismatch (§3.1).** Either adjust the instruction's `T{n}.{component}.P{prompt}` to `T{n}.{component}.{prompt}` (recommended), or migrate the DB. Do this before any AI session starts using the obslog markers.
3. **Medium — resolve link.status semantics (§3.3).** Either migrate the 934 'active' rows to 'validated', or drop the status check from Domain E. Hard gate; needs decision before the next Closure check fires.
4. **Medium — extend §v2.7 / §v2.9 citation token list (§4.3).** Add the new T2 / RD / SB-T2 forms that today's capture writes.
5. **Low — schema readiness gate to check catalogue_version (§4.1).** One-line addition, prevents the gate from being satisfied by stale v1 rows.
6. **Low — chapter source mapping cleanup (§4.2).** Either drop the finding_type discrimination or re-introduce it.

---

## 7. The user's stated understanding — confirmed

> "I notice that this instruction still include details about patches and other outputs that I am not sure it is any longer relevant. My understanding is that the only output from this instruction is the obslog and session log."

**Correct.** Under v2, AI produces exactly two artefacts: the obslog (containing Stage 2a observations, Stage 2b Q&A, Stage 2c chapters, SD pointer accumulator, Session Close) and the session log (handoff document). Everything else in the body (the Analytic Word Output as a separate six-chapter file, Type (b) patches, supplementary patches, closing patches) is v1 mechanics that v1.6 didn't fully clean up. The §v2 addendum says so explicitly; the body still reads as if they exist.

A v1.7 cleanup pass would resolve this without changing any analytical discipline.
