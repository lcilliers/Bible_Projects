# Analytic Processing — Focus Brief

**Date:** 2026-05-03
**Scope:** Stage 2 analysis-output: governing rules, validation, .md artefacts, scripts, and processes. Built from a fresh re-read of current instruction docs and a live-folder survey, not from memory.

---

## 1. Current governing instructions (resolved `[current]` versions)

| Document | Current file | Notes |
|---|---|---|
| Analysis Output (Stage 2) | [wa-sessionb-analysis-output-v1_8-20260430.md](../../Workflow/Instructions/wa-sessionb-analysis-output-v1_8-20260430.md) | v1.8 — Stage 2c rewritten as analytical synthesis (28 entries, T0 excluded). v1_7 also exists in folder; v1_8 supersedes. |
| Analysis Readiness (Stage 1) | [wa-sessionb-analysis-readiness-v1_10-20260501.md](../../Workflow/Instructions/wa-sessionb-analysis-readiness-v1_10-20260501.md) | v1.10 — §L embeds v2 catalogue (T0–T7, 189 prompts). |
| Patch instruction | [wa-patch-instruction-v2_10-20260427.md](../../Workflow/Instructions/wa-patch-instruction-v2_10-20260427.md) | Under v1.8 there are **no AI-produced patches** for Stage 2. The patch path now applies only to (a) supplementary Type (a) for Stage 1 corrections found in Stage 2a, and (b) REPAIR / SESSIONB-COMPLETE / VC patches outside Stage 2. |
| Claude Code instruction | [wa-claudecode-instruction-v4_4-20260428.md](../../Workflow/Instructions/wa-claudecode-instruction-v4_4-20260428.md) | CC owns readiness generation, validation, and obslog parsing/writing. |
| Dimension Review | [wa-dimensionreview-instruction-v3_3-20260418.md](../../Workflow/Instructions/wa-dimensionreview-instruction-v3_3-20260418.md) | Hard gate before readiness validates. |
| Registry management | [wa-registry-management-guide-v5_10-20260418.md](../../Workflow/registry/wa-registry-management-guide-v5_10-20260418.md) | Lives under `Workflow/registry/`, not `Workflow/Instructions/`. |
| Reference | [wa-reference-v5_6-20260418.md](../../Workflow/archive/wa-reference-v5_6-20260418.md) | **Latest copy is in `Workflow/archive/`** — flagged as a possible structural anomaly worth confirming. |
| Global rules | [wa-global-rules-all-v2-20260427.md](../../Workflow/Global_rules/wa-global-rules-all-v2-20260427.md) | Post-restructure naming. |

---

## 2. Pipeline at a glance — what flows through Stage 2

```
DB state for registry N
   │
   ▼
Phase A prose (sa_s1_d1..d6)  ─── precondition (§v2.R0)
   │
   ▼
[CC] _pilot_build_readiness_output_v2_*.py  --registry N
   │   → Sessions/Session_B/07_Analysis_Readiness_Status/
   │     wa-{NNN}-{word}-readiness-output-v{n}-{date}.{md,json}
   │     (sections A–N + M; §L embeds 189-prompt second-tier catalogue)
   │
   ▼ (revision sessions only)
[CC] _pilot_build_analytic_status_v1_*.py  --registry N
   │   → same folder; wa-{NNN}-{word}-analytic-status-v{n}-{date}.{md,json}
   │
   ▼
[CC] _pilot_validate_readiness_v1_*.py  --registry N
   │   → same folder; wa-{NNN}-{word}-readiness-validation-v1-{date}.{md,json}
   │   → 15 checks (C01..C15) → READY or BLOCKED. FAIL≥1 ⇒ stop.
   │
   ▼   READY only
[AI Stage 2a / 2b / 2c] consumes:
   • readiness output .md (data package)
   • validation report .md (WARN list to track)
   • analytic status .md (revision sessions)
   │
   ▼
AI produces TWO .md artefacts:
   • wa-{NNN}-{word}-obslog-v{n}-{date}.md         (parsed by CC)
   • wa-{NNN}-{word}-sessionb-sessionlog-v{n}-{date}.md  (handoff doc, not parsed)
   │
   ▼
[CC] obslog parser + writer (Phase 1 manifest → Phase 2 DB write)
   │   → wa_session_b_findings, wa_finding_catalogue_links,
   │     wa_session_research_flags, verse_context.analysis_note,
   │     wa_obs_question_catalogue, wa_prose_section_citations,
   │     word_registry.session_b_status
   │
   ▼
Session C reads from DB; Session D notified of new SD pointers.
```

**No AI-produced JSON patches anywhere in Stage 2.** Every DB write is performed by CC's writer reading the obslog. This is the architectural shift v1.7 / v1.8 cemented.

---

## 3. The 15-check validation gate (READY/BLOCKED)

Implemented in [scripts/_pilot_validate_readiness_v1_20260427.py](../../scripts/_pilot_validate_readiness_v1_20260427.py). Output: paired `.md` + `.json` validation report alongside the readiness output. Verdict policy per check is FAIL = blocking, WARN = informational, PASS = green.

| ID | Check | Verdict policy |
|---|---|---|
| C01 | `schema_version` ≥ 3.17.0 (M40–M43 applied) | FAIL if lower |
| C02 | `last_automation_run = 'AUDITED'` | WARN if not |
| C03 | `phase1_status = 'Complete'` | FAIL if not |
| C04 | `verse_context_status = 'Complete'` | FAIL if not |
| C05 | `dim_review_status = 'Complete'` | FAIL if not |
| C06 | Phase A prose: 6 `sa_s1_d*` rows present | FAIL if < 6 |
| C07 | Readiness `.md` + `.json` present | FAIL if missing |
| C08 | OWNER terms non-empty, ≥ 1 verse each | FAIL if no terms; WARN on any zero-verse term |
| C09 | All VC groups have a dimension | FAIL if any lack |
| C10 | All VC groups have ≥ 1 anchor | WARN if any lack |
| C11 | No group at set-aside ratio > 90 % | WARN if any (drift signal) |
| C12 | Per-term `vc_status` not all `not_done` | WARN (informational, legacy-VC) |
| C13 | Dimension confidence has `confirmed`, no `queried` | WARN if `queried` or no `confirmed` |
| C14 | No open `DATA_ANOMALY_*` findings | FAIL if any |
| C15 | `inference_note` and `word_synopsis` present | WARN (informational) |

Overall: **READY** when FAIL = 0; **BLOCKED** when FAIL ≥ 1. Stage 2 cannot begin under BLOCKED.

---

## 4. Stage discipline (what AI produces in the obslog)

**Stage 2a — Comprehensive analysis (free-form).** Nine reading units (1 Registry overview · 2 XREF terms · 3 OWNER lexical · 4 VC groups landscape · 5 Correlation signals · 6 Existing SD pointers / findings · 7 Anchor verse reading · 8 Thin-evidence phase2 flags · 9 Existing findings input review). Observations recorded inline as `**OBS-{NNN}-{seq:03d}:**`. SD pointers raised on discovery.

**Stage 2b — Second-tier catalogue (T0–T7, 189 prompts, structured).** Each prompt receives one Q&A entry under `### Stage 2b Q&A Log`, marker `**Q&A-{seq:03d} | {tier_prompt_code}**` with bullet fields (Tier · Component · Prompt · Disposition A/P/S/N · Notation · Answer with `OBS-NNN-{seq}` citations · Anchor verses · Finding type · Stage 2b note). Closing summary appended after T7.

**Stage 2c — Analytical synthesis (T1–T7 only; T0 excluded).** Exactly **28 mandatory entries**: 7 intra-tier + 21 inter-tier pairs. Markers `**SYN-INTRA-{NNN}-{seq:03d}**` and `**SYN-INTER-{NNN}-{seq:03d}**` under `## Stage 2c — Synthesis Entries`. Each entry carries one outcome: **D** (Described — needs ≥ 2 `Q&A-NNN` source citations), **F** (Further research — produces an SD pointer), **N** (Not applicable — needs one-sentence rationale). Inter-tier D entries also name a `Structural relationship` (causal / enabling / sequential / constitutive / tension / parallel).

**Closure.** `## SD Pointer Accumulator — Final` · `## RESEARCHER_DECISION Accumulator — Final` · `## Session Close` block carrying `session_b_status: 'Analysis Complete'`.

---

## 5. Closure checklist — six domains (run before session close)

Per [analysis-output v1.8 §Closure](../../Workflow/Instructions/wa-sessionb-analysis-output-v1_8-20260430.md):

- **Domain A — Data completeness.** `evidential_status` and `mti_terms.status` set on all active OWNER terms; `verse_context_status = Complete`; all dim-index rows at CLAUDE_AI/RESEARCHER confidence; `dominant_subject` set.
- **Domain B — Findings completeness.** ≥ 1 active MEANING_OBSERVATION; SPIRIT_SOUL_BODY treatment present; thin-evidence findings dispositioned; questioned prior-phase findings actioned.
- **Domain C — Flag resolution.** Zero open `wa_session_research_flags` with `session_target='B'` and `resolved=0`; SD accumulator count matches per-tier totals; phase2 flags dispositioned.
- **Domain D — Entity links.** Every A/P Q&A cites ≥ 1 OBS reference; SUPERSEDE blocks name the superseding finding.
- **Domain E — Catalogue links (post-CC-parse).** Every active v2 finding has a `wa_finding_catalogue_links` row; CC raises `DATA_ANOMALY_FINDING_UNCITED` otherwise.
- **Domain F — Stage 2c synthesis.** Intra = 7, Inter = 21, Total = 28 (hard gate); every entry has D/F/N; N has rationale; F has SD pointer; D inter-tier names structural relationship.

Integrity rules **SB-1, SB-2, SB-9, SB-11–SB-18, SB-25–SB-29** govern conformance.

---

## 6. Scripts and what they govern — current map

### Live in `scripts/` (called by user as the operative pipeline)

| Script | Role | Inputs | Outputs |
|---|---|---|---|
| [_pilot_build_readiness_output_v2_20260426.py](../../scripts/_pilot_build_readiness_output_v2_20260426.py) | Builds the 14-section registry data package (A–N + M); embeds v2 catalogue at §L | DB state | `Sessions/Session_B/07_Analysis_Readiness_Status/wa-{NNN}-{word}-readiness-output-v{n}-{date}.{md,json}` |
| [_pilot_build_analytic_status_v1_20260427.py](../../scripts/_pilot_build_analytic_status_v1_20260427.py) | Builds analytic status for revision sessions (lifecycle summary, prior chapters, anchor analyses, open items) | DB state | Same folder; `wa-{NNN}-{word}-analytic-status-v{n}-{date}.{md,json}` |
| [_pilot_validate_readiness_v1_20260427.py](../../scripts/_pilot_validate_readiness_v1_20260427.py) | 15-check validation, READY/BLOCKED gate | DB + filesystem (readiness `.md` + `.json`) | Same folder; `wa-{NNN}-{word}-readiness-validation-v1-{date}.{md,json}` |
| [_pilot_parse_obslog_v2_format_v1_20260428.py](../../scripts/_pilot_parse_obslog_v2_format_v1_20260428.py) | **Pre-v1.8** obslog parser → Phase 1 manifest. Recognises older R030 / R067 v2 obslog format (OBS markers + `**Q&A NNN** — date` + `**SD POINTER N (NEW)**` + `### CHAPTER N`). Does **not** recognise `SYN-INTRA` / `SYN-INTER`. Warns when chapters ≠ 6. | Obslog `.md` | `Sessions/Session_B/words/{NNN}_{word}/obslog/wa-{NNN}-{word}-obslog-parse-manifest-v1-{date}.json` and validation `.md` |
| [_pilot_capture_obslog_to_db_v1_20260427.py](../../scripts/_pilot_capture_obslog_to_db_v1_20260427.py) | **Pre-v1.8** Phase 2 writer. Reads manifest, writes status / observations / chapters / SD pointers / Q&A links / catalogue completeness / review notes / new questions / anchor-verse analyses / prose supersedes (+ supersede citations + audit). Idempotent, transactional, with pre-write backup. | Manifest JSON (and obslog text for Unit 7 anchor extraction) | DB writes + console summary |
| [apply_session_patch.py](../../scripts/apply_session_patch.py) | Generic patch applicator for non-Stage-2 patches (PROSE, REPAIR, VC, SESSIONB-COMPLETE, etc.) | Patch JSON | DB writes; archive to `archive/patches/` |

### Archived — applied 2026-04-30 then moved aside

| Script | Role |
|---|---|
| [scripts/archive/_apply_v1_8_obslog_capture_v1_20260430.py](../../scripts/archive/_apply_v1_8_obslog_capture_v1_20260430.py) | **Direct v1.8 obslog → DB writer.** Recognises `**Q&A-NNN \| Tn.x.y**`, `**SYN-INTRA-NNN-NNN**`, `**SYN-INTER-NNN-NNN**`, `**SP-NNN-NNN**`, `**RD-NNN-NNN**`, the `## Session Close` block. Writes synthesis findings as `SYNTHESIS_INTRA_TIER` / `SYNTHESIS_INTER_TIER` with `synthesis_outcome / tiers_engaged / structural_relationship / session_c_chapter / sd_pointer_ref`. Raises `DATA_ANOMALY_QA_GAP`, `DATA_ANOMALY_SYNTHESIS_INCOMPLETE`, `DATA_ANOMALY_FINDING_UNCITED` post-write. Idempotent; single-step (no separate manifest stage). |
| [scripts/archive/_apply_synthesis_schema_v1_20260430.py](../../scripts/archive/_apply_synthesis_schema_v1_20260430.py) | One-shot schema migration that added the v1.8 synthesis-finding columns (`synthesis_outcome`, `tiers_engaged`, `structural_relationship`, `session_c_chapter`, `sd_pointer_ref`) and the `SYNTHESIS_INTRA_TIER` / `SYNTHESIS_INTER_TIER` finding types. |

**Important gap to flag.** The v1.8 instruction says CC's writer parses v1.8 markers; the **only** script that does so is in `scripts/archive/`. The live `scripts/_pilot_parse_obslog_v2_format_v1_*.py` and `_pilot_capture_obslog_to_db_v1_*.py` predate v1.8 and do not handle SYN-INTRA / SYN-INTER. Re-running the live two-step pipeline against a v1.8 obslog would silently miss the synthesis entries (or warn that chapters ≠ 6). If continued v1.8 work is expected, the archived capture script either needs reinstating to live `scripts/`, or its logic folded into the `_pilot_parse_*` + `_pilot_capture_*` pair.

---

## 7. Folder layout in practice (vs. instruction)

The instruction (`v1_10`) says obslog pipeline outputs go to `Sessions/Session_B/09_Analysis_output_logs/words/`. The actual current layout, post-2026-04-28 restructure (commit `9b58d55`), is per-word:

```
Sessions/Session_B/
├── 07_Analysis_Readiness_Status/   ← matches instruction (readiness + validation + analytic status)
└── words/{NNN}_{word}/
    ├── inputs/      ← readiness output copies, R{NNN}-{word}-data.md, analytic status
    ├── obslog/      ← obslog .md, parse-manifest .json, validation .md, sessionlog .md
    ├── chapters/    ← assembled prose chapter prototypes
    ├── prior/       ← prior VC reports etc.
    └── README.md
```

`Sessions/Session_B/09_Analysis_output_logs/words/` is now near-empty (two stale March 2026 reports). The instruction text has not caught up to the per-word folder convention. Worth flagging when next touching the readiness instruction or `wa-claudecode-instruction`.

---

## 8. Live registries operating under v1.8

From the obslog inventory in [Sessions/Session_B/words/](../../Sessions/Session_B/words/):

- **Stage 2c-only sessions (v1.8 28-entry synthesis applied 2026-04-30):** R023 compassion, R068 grace.
- **v1.8 obslogs (full Stage 2):** R030 contrition (v2), R062 fellowship (v2), R064 forgiveness (v2), R067 goodness (v4), R103 love (v1+v2), R111 mercy (v1).
- **v1.8 in-flight (post 2026-05-01):** R034 covenant (v1), R099 kindness (v1+v2), R117 peace (v1+v2), R060 faithfulness (v1).
- **Validation reports present** for 27+ registries through the `_06`-prefix range pushed 2026-05-02 (`077 honesty`, `090 innocence`, `092 integrity`, `125 purity`, `139 righteousness`, `148 sincerity`, `164 truthfulness`, `168 uprightness`).

---

## 9. Summary — what governs Stage 2 analysis-output

1. **Two .md artefacts AI produces:** comprehensive obslog (parsed) + session log (informational).
2. **Three .md artefacts AI consumes:** readiness output, validation report, and (for revisions) analytic status — all `.md` + paired `.json`, all in `07_Analysis_Readiness_Status/`.
3. **The 15-check validator** is the only gate between Stage 1 and Stage 2 — `READY` mandatory.
4. **Obslog markers are precise** (§8 of v1.8): `OBS-NNN-seq`, `Q&A-seq | tier_prompt_code`, `SP-NNN-seq`, `RD-NNN-seq`, `SYN-INTRA-NNN-seq`, `SYN-INTER-NNN-seq`, `## Session Close` block.
5. **Closure has six domains** (A–F), with Domain F (28-entry synthesis count) the newest hard gate from v1.8.
6. **Live obslog parser/writer pair is pre-v1.8;** the v1.8-aware single-step capture is in `scripts/archive/`. This is an active loose end.

---

*Built by reading: wa-sessionb-analysis-output-v1_8 (full); wa-sessionb-analysis-readiness-v1_10 (full); _pilot_validate_readiness (full); _pilot_parse_obslog_v2_format (full); _pilot_capture_obslog_to_db (skim with grep); _apply_v1_8_obslog_capture (head); R068 grace v1.8 obslog (head); folder surveys for instructions, scripts, and Sessions/Session_B/words/.*
