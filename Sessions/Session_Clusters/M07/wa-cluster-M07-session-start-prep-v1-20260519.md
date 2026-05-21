# M07 session-start prep

**Date:** 2026-05-19
**Cluster:** M07 — Shame, Disgrace and Humiliation
**Governing instruction:** `Workflow/Instructions/wa-sessionb-cluster-instruction-v2_6-20260519.md`
**Author:** CC
**Purpose:** capture M07's starting state, identify Phase 1 entry point, and document the v2_6 phase plan so the next active session can pick up cleanly.

---

## 1. Starting state (DB snapshot, 2026-05-19)

| Item | Value |
|---|---|
| `cluster.status` | `Not started` (transition to `Data - In Progress` when Phase 1 begins) |
| `cluster.short_name` | Shame |
| `cluster.description` | *"Shame, Disgrace and Humiliation"* |
| `cluster.version` | v6 |
| `mti_terms` in scope | **36** (34 `extracted` + 2 `extracted_thin`) |
| `wa_term_inventory` OWNER copies | 37 |
| `wa_term_inventory` XREF copies | 15 |
| Contributing word registries | 14 |
| Existing `verse_context` rows | 565 (431 `is_relevant=1` + 134 set-aside) |
| **UT verse-term pairs (Phase 1 to-do)** | **112** |
| Total OWNER verse-term pairs | 547 |
| **Pass A meanings populated** | **0 / 431** (Phase 2 entirely to-do) |
| `cluster_subgroup` rows | 0 (Phases 5–8 entirely to-do) |
| `characteristic` rows | 0 (Phase 8.7 entirely to-do) |
| `cluster_observation` rows | 0 |
| `wa_session_b_findings` on M07 registries | 380 (42 `pending` + 1 `open` candidates for Phase 10) |
| Science extract | ✓ `Workflow/Sciences/wa-m07-shame-scienceextract-v1_0-20260513.md` (15.6 KB) |

---

## 2. Cluster characteristic statement (for Phase 1 system prompt)

From `word_registry.id=146` (shame) — the longest individual characteristic statement in M07's contributing registries:

> Shame is the painful inner awareness of being exposed as inadequate, wrong, or unworthy — and the accompanying fear of rejection or contempt. The Hebrew vocabulary is extensive and connected to honour and disgrace: to be shamed is to be publicly diminished, stripped of one's standing. The body is fully implicated: the face falls or is covered, the person wants to disappear. God is said to put to shame those who oppose his people, and to honour those who hope in him. Shame is addressed most directly in the gospel: the one who trusts in him will not be put to shame.

Adjacent inner-being content from contributing registries (anointing 6, compassion 23, corruption 31, evil 57, humility 80, impurity 86, innocence 90, meaning 107, peace 117, rejection 131, slander 149, flesh 185, contempt 190) provides cross-cluster boundary material to be exercised at Phase 3 (constitution debate) and Phase 8.5 (BOUNDARY resolution).

A finalised cluster characteristic statement will emerge from Phase 3 — for Phase 1 batch system prompts the registry-shame statement above is the operative seed.

---

## 3. Contributing word registries — Phase 1 / VC status

| Registry | Word | phase1_status | verse_context_status | session_b_status |
|---:|---|---|---|---|
| 6 | anointing | Complete | Complete | Verse Context Reset |
| 23 | compassion | Complete | Complete | Analysis Complete |
| 31 | corruption | Complete | Complete | Verse Context Reset |
| 57 | evil | Complete | Complete | Verse Context Reset |
| 80 | humility | Complete | Complete | Verse Context Reset |
| 86 | impurity | Complete | Complete | Verse Context Reset |
| 90 | innocence | Complete | Complete | Verse Context Reset |
| 107 | meaning | Complete | Complete | Verse Context Reset |
| 117 | peace | Complete | Complete | Analysis Complete |
| 131 | rejection | Complete | Complete | Verse Context Reset |
| **146** | **shame** | **In Progress** | Complete | Verse Context Reset |
| 149 | slander | Complete | Complete | Verse Context Reset |
| 185 | flesh | Complete | Complete | Verse Context Reset |
| 190 | contempt | Complete | Complete | Verse Context Reset |

**Anomaly:** `reg#146 shame.phase1_status='In Progress'` but `last_automation_run='AUDITED'` (audit completed 2026-03-25 — RUN-20260325_055019-AUDIT_WORD), and `verse_context_status='Complete'`. The `phase1_status` value looks stale — registry-level Phase 1 actually finished. **Not blocking** for cluster Phase 1, but flag for housekeeping (advance to `Complete` once the cluster session confirms no further Phase 1 work needed on that registry).

---

## 4. UT verse-term pair distribution (Phase 1 entry point)

Per v2_6 §4.1, Phase 1 classifies every verse-term pair without a `verse_context` row. M07's UT count is **112**, distributed:

| Registry | Word | UT pairs |
|---:|---|---:|
| 146 | shame | **105** |
| 80 | humility | 5 |
| 6 | anointing | 1 |
| 107 | meaning | 1 |
| (others) | — | 0 |
| **Total** | | **112** |

The shame registry holds 94% of M07's Phase 1 work — these are the M07-targeted verses for shame's terms that haven't been classified yet (the registry-level Phase 1 captured the in-registry set; cluster-level Phase 1 may add cross-registry verse-term pairs).

---

## 5. v2_6 phase plan for M07

Per the new (v2_6) cluster instruction, M07 will work through the following phases:

| Phase | § | Owner | Scope | M07 starting state |
|---:|---|---|---|---|
| 1 — UT verse review | §4 | CC (JSON+API) | 112 verse-term pairs to classify | Ready (system prompt: §2 above + the §1.1 in-scope examples block) |
| 2 — Pass A per-verse meaning | §5 | CC (JSON+API) | Every `is_relevant=1` row gets `analysis_note` | 0 / 431 done; whole-cluster work |
| 3 — Cluster constitution debate | §6 | AI (chat) | Refine characteristic statement; finalise term universe | To start |
| 4 — Term transfers + BOUNDARY directives | §7 | CC | Apply term moves from Phase 3 | To start |
| 5 — Sub-group formation | §8 | AI (chat) | Cluster verses by meaning; ≤40% max per sub-group (§8.6) | To start |
| 6 — Verse-to-sub-group routing | §9 | CC | Mechanical assignment | To start |
| 7 — VCG design | §10 | AI (chat) | VCG units within each sub-group | To start |
| 8 — Dissolve old VCGs | §11 | CC | Researcher comparison | To start |
| **8.5 — BOUNDARY resolution** | §11A | AI + researcher + CC | SET-ASIDE / ROUTE-TO-CLUSTER / PROMOTE-TO-SUBGROUP for every BOUNDARY-pending term | To start |
| **8.7 — Characteristic mapping (NEW v2_6)** | §11B | AI + researcher + CC | Identify inner-being characteristics + sub-group bindings; load to `characteristic`, `characteristic_subgroup`, `cluster_observation` | To start |
| **9 — Catalogue prompts (REVISED v2_6)** | §12 | AI (chat) | 189 prompts × N characteristics + 8th cluster-synthesis session | To start |
| 10 — Inherited-finding reconciliation | §13 | AI then CC | Disposition 42 pending + 1 open + flags | To start; scope choice at the time (M04 precedent: bare-minimum scope) |
| 11 — Fold + validation | §14 | CC | Inherited-findings fold (no-op if RBC=0); validation | To start |
| 12 — Closure | §15 | CC | `cluster.status → Analysis Completed` | To start |

The v2_6-specific phases (8.7 + revised 9) follow the **M04 worked precedent** — operational scripts retained as templates:

- `_build_m04_characteristic_phase9_package_20260518.py` — single-char Phase 9 brief + input builder (template; copy + rename for M07)
- `_build_m04_characteristic_phase9_bundle_20260519.py` — multi-char bundle builder
- `_build_m04_phase9_cluster_synthesis_20260519.py` — 8th-session synthesis builder
- `_apply_phase9_characteristic_findings_20260518.py` — per-batch loader (parametric; works for any cluster with `--cluster-code` parameterisation — currently hardcoded to M04, needs trivial generalisation when M07 starts Phase 9)
- `_apply_phase9_cluster_synthesis_20260519.py` — synthesis loader with appendix split
- `_merge_phase9_segments_20260519.py` — parametric segment merger (already cluster-agnostic)
- `_validate_m04_phase11_v1_20260519.py` — Phase 11 validation (template; copy + rename for M07)

Cluster-specific load scripts (M49 schema migration is already applied; M07 just needs its own characteristic/observation/cluster_finding writes).

---

## 6. Required inputs for the first AI-facing session (Phase 3 — constitution debate)

When the session reaches Phase 3, the AI package must declare these as required inputs (per `[feedback_ai_package_self_declaration]`):

1. Brief — written for Phase 3
2. Structural input — cluster meaning corpus (after Phase 2 Pass A meanings land)
3. Governing instruction — `wa-sessionb-cluster-instruction-v2_6-20260519.md` §6 (Phase 3 disciplines)
4. **Science extract — `Workflow/Sciences/wa-m07-shame-scienceextract-v1_0-20260513.md`** (mandatory per `[feedback_phase9_science_extract_required]`; though primarily for T7.3, the science framing benefits all AI phases for consistency)
5. Programme prose — `Workflow/Programme/programme_prose/wa-programme-prose-extract-{current}.md` Ch.1 'Defining Inner Being'
6. Global rules — `wa-global-general-rules` [current]

The Phase 9 packages (per-characteristic + cluster-synthesis) will use the same Required-inputs convention.

---

## 7. Session-open checklist (the first M07 active session does these)

Per v2_6 §3:

1. Create obslog at `Sessions/Session_Clusters/M07/wa-obslog-M07-{description}-v1-{YYYYMMDD}.md` (suggested description on first session: `cluster-open` or `phase1-ut`).
2. Confirm `cluster.status='Not started'` (current) — advance to `Data - In Progress` once Phase 1 fires the first directive.
3. Run any preflight checks (engine `--check-locks`, schema_version, etc.).
4. Resolve the `reg#146 shame.phase1_status='In Progress'` stale-flag housekeeping (advance to `Complete` after confirming there are no pending Phase 1 audit anomalies for that registry).
5. Begin Phase 1: build the UT-batch JSON loads against the 112 verse-term pairs; iterate batches against the Claude API per §4.2.

---

## 8. Open items for the researcher

- **Phase 10 scope for M07 (when we get there):** at M04 closure the researcher chose bare-minimum scope (only items explicitly citing M04 cluster code). M07 will face the same choice — flag for decision at that point.
- **M01/M02 BOUNDARY residue flags:** unrelated to M07 directly, but they're parked on registries (fear 61, distress 51, wonder 175) some of which contribute to other clusters. Tracked under M01/M03 audit-fix. Not blocking for M07.
- **Order of next clusters after M07:** to be decided; M08 (Pride) and M09 (Humility) are obvious adjacencies. M07's Phase 8.5 ROUTE-TO-CLUSTER work may identify verses that belong in M08/M09 and surface them as ingest candidates.

---

*End of M07 session-start prep. Hand off to the first active M07 session.*
