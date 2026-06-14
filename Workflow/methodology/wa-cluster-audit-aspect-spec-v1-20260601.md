# Cluster audit — aspect specification (the canonical checklist)

> **SUPERSEDED (2026-06-14)** by `wa-cluster-audit-design-v1-20260607.md` (the v3_2-integrated audit design). Retained for reference; see reconstruction 04 §4.

**Living document** · **Doc version:** 2 · **2026-06-04** · grounds `scripts/audit_cluster_v1_20260601.py` (the reusable cluster auditor).
**Purpose:** the consolidated, well-founded set of aspects a cluster audit checks — synthesised from prior work, not re-imagined. Each aspect cites its source so the audit stays anchored to the methodology.

**v2 (2026-06-04):** added **Group E — Meaning & keyword quality** (E1–E8), the surfacing-now / active-later
angles emerging from the 2026-06-04 keyword/meaning exploration. Structural Groups A–D unchanged.

**Sources synthesised:**
- `archive/scripts/_validate_analysis_complete_v1_20260531.py` — the proven two-condition gate that reset the 17 clusters (8 checks).
- `Workflow/methodology/wa-cluster-readiness-gate-design.md` §3 — the gate definition (Conditions 1/2; four homes; data-substrate prerequisites §3.3).
- `Workflow/Instructions/wa-sessionb-cluster-instruction-v3_0-20260527.md` §10 — Phase F exit gate (10-point per-phase completeness checklist).
- `scripts/_audit_cluster_input_coverage_v2_20260530.py` (F6) — findings/anchor coverage.
- `scripts/_audit_all_analysis_complete_clusters_v1_20260530.py` (F7) — per-cluster summary shape.
- This session's registers — incremental-update inputs (new terms / pointers / boundaries).

**Severity key:** `GATE` = hard, blocks Analysis Complete (a single GATE failure ⇒ not validly complete). `STRUCT` = structural-completeness (v3_0 Phase F); a fresh-v3_0 cluster must pass, a legacy cluster reports for awareness. `INFO` = reported, never gates. `INCR` = an item to **re-submit/clear in the incremental update** (not a defect — work to do).

---

## A. Analysis-Complete gate — the two-condition contract  (source: validate-script + gate-design §3)

### Condition 1 — verse/tier findings captured (reads `cluster_finding`)
| ID | Aspect | DB read | Sev |
|---|---|---|---|
| A1 | Findings present | `cluster_finding` active rows > 0 | **GATE** |
| A2 | No nonsense/mis-classified rows | `cluster_synthesis` rows whose text is only a gap acknowledgment (M38 T5.7.3 pattern) | INFO* |
| A3 | Every characteristic has findings | each `characteristic` has ≥1 active `cluster_finding` | **GATE** |

### Condition 2 — every leftover resolved to observation-or-deleted
| ID | Aspect | DB read | Sev |
|---|---|---|---|
| A4 | No active BOUNDARY sub-group members | `cluster_subgroup` code='BOUNDARY' → live verse_context / mti_term_subgroup / VCG members = 0 | **GATE** |
| A5 | No unresolved BOUNDARY_DECISION_PENDING | `wa_session_research_flags` code=BOUNDARY_DECISION_PENDING, resolved=0, cluster named in label/desc | **GATE** |
| A6 | No unresolved gating flags | SD_POINTER/SB_FINDING/PH2_* resolved=0 on the cluster's registries (registry→cluster, **non-exclusive**) | **GATE** |
| A7 | No stray Session-B findings | `wa_session_b_findings` status∈(pending,open), linked term→sub-group→cluster | **GATE** |
| A8 | No unconfirmed actionable observations | `cluster_observation` type∈(CROSS_CLUSTER_HANDOFF, SELF_CHECK_OBSERVATION) status≠confirmed | **GATE** |
| A9 | No orphan findings | active non-synthesis `cluster_finding` with no characteristic AND no sub-group | INFO |

\*A2 is INFO not GATE because it's a heuristic (text match); surfaced for review, fixed under Condition 1.

---

## B. Structural / phase completeness  (source: v3_0 §10 Phase F exit gate)

**Researcher direction 2026-06-01:** verse meaning + keywords are a **cross-cluster analytic necessity, not optional** → B1a/B1b are **GATE**. VCG-anchor and anchor-coverage are likewise mandatory → B5/B7 GATE.

| ID | Aspect | DB read | Sev |
|---|---|---|---|
| B1a | Phase A — verse **meanings** | every is_relevant=1 `verse_context` has non-empty `analysis_note` | **GATE** |
| B1b | Phase A — **keywords** | every is_relevant=1 `verse_context` has non-empty `keywords` | **GATE** |
| B2 | Phase B — verses grouped | is_relevant `verse_context` have `cluster_subgroup_id` AND `group_id` | STRUCT |
| B3 | characteristics table complete | `characteristic` rows present; `characteristic_subgroup` links present; **every non-BOUNDARY sub-group is linked to a characteristic** | **GATE** |
| B4 | Phase D — findings per characteristic | active `cluster_finding` count per characteristic (legacy clusters vary; v3_0 expects 189 ea.) | INFO |
| B5 | every active VCG has an anchor | each active VCG (cluster's sub-groups) has ≥1 `is_anchor=1` verse | **GATE** |
| B6 | Citation traceability | `finding_citation` rows present for the cluster's findings | STRUCT |
| B7 | every anchor verse covered in findings | each active anchor verse's reference is cited (`finding_citation` verse) by a cluster finding | **GATE** |
| B8 | Distribution health (future) | no substantive sub-group > 40% of substantive verses (§6.2.7) — *not yet implemented* | INFO |

---

## C. Data-substrate prerequisites  (source: gate-design §3.3; this session's cleanups)

| ID | Aspect | DB read | Sev |
|---|---|---|---|
| C1 | Old-format VCGs dissolved | no active old-format (`^\d+-\d+`) VCG tied to the cluster's terms (else: dissolve at Phase C) | STRUCT |
| C2 | Term→sub-group linkage present | `mti_term_subgroup` links exist for the cluster's live terms (M38 had 0) | STRUCT |
| C3 | No live duplicate term rows | each of the cluster's strongs has exactly 1 live `mti_terms` row | INFO |

---

## D. Incremental-update inputs — the re-submit / clear worklist  (source: this session)

| ID | Aspect | DB read | Sev |
|---|---|---|---|
| D1 | New terms to place | terms with `cluster_code`=this cluster but no `mti_term_subgroup` link (e.g. FLAG-classified) → place + analyse | INCR |
| D2 | Unallocated pointers | findings/flags routed (`cluster_link`) here, not yet adopted into a finding | INCR |
| D3 | Unresolved boundaries | BOUNDARY_DECISION_PENDING for this cluster (= A5) | INCR |
| D4 | Old VCGs to dissolve | this cluster's own old VCGs awaiting Phase-C dissolution (= C1) | INCR |

---

## E. Meaning & keyword quality  (source: 2026-06-04 keyword/meaning exploration)

**Sequencing (researcher direction 2026-06-04):** the data is currently **too dirty to trap meaning
transgressions reliably**. First bank a good set of clusters to **clean** status (Groups A–D); the Group-E
quality angles then run as a dedicated **meaning–keyword audit phase**. So **E aspects are `INFO`
(surfacing) for now** and become active checks in that later phase — *not* gates today. They exist here so
the standard audit *highlights this class of problem routinely* rather than it being hunted ad-hoc.
Provenance: `research/investigations/anchor-meaning-analytics-20260604.md`,
`…/keyword-bias-extract-20260604.md`, `…/keyword-analytics-revision-plan-20260604.md`,
`…/rescue-physical-setaside-20260604.md`. This is the concrete form of the queued
*verse-meaning corroboration* audit angle.

| ID | Aspect | What it surfaces | Sev |
|---|---|---|---|
| E1 | **Keyword well-formedness** | keywords should be the `[faculty/head] [predicate/qualifier]` 2-word form (91% are); flag empty, 1-word, or >3-word / malformed entries | INFO |
| E2 | **Keyword normalisation duplicates** | the same concept split by hyphen/spacing/stem (`god-saving`=`god saving`; `corrupt`/`corrupted`/`corruption`); flag near-duplicate heads/qualifiers for canonicalisation | INFO |
| E3 | **Interpretive-label corroboration (QUALIFIER axis)** | loaded/abstract qualifiers (`eschatological`, `corrupted`, `defiled`, `perverted`…) must be warranted by the verse; flag a qualifier asserting a sense the text doesn't carry — esp. a label applied **reflexively across a whole sense** (e.g. `salvation eschatological` on plainly physical/temporal verses: Gen 49:18, Hab 3:8) | INFO |
| E4 | **Anchor sense-fitness** | an anchor's meaning must read in the **sense the cluster characterises**; flag anchors whose meaning is explicitly a *different* sense (e.g. **physical-rescue σῴζω anchoring inner-being Salvation VCGs** — Mat 14:30, Act 27:20, Heb 11:7) → review for anchor-fitness / set-aside / distinct VCG | INFO |
| E5 | **Category-slip / scope check** | verses pulled into an inner-being cluster on a category import — demonic "unclean spirit" (*akathartos*) grouped with ritual/moral **defilement** (Mar 3:11, Luk 6:18); involuntary ritual/bodily impurity treated as inner-being moral content (Lev 15) → is the verse genuinely inner-being? | INFO |
| E6 | **Uniform-lens over-tagging** | the inner-faculty lens applied so uniformly it adds a faculty the verse doesn't state (e.g. `will compromised` on a perception/judgement verse, Exo 23:8); flag mechanical `will`/`heart` tagging | INFO |
| E7 | **Anchor meaning-coverage** | report % of **anchors** carrying meaning+keywords per cluster (programme-wide only ~5.4% today, concentrated in the M10 family); a clean cluster needs its anchors meaning-enriched (complements B1a/B1b, which gate *is_relevant* coverage, not anchors specifically) | INFO |
| E8 | **Credit self-limiting meanings** | do **not** penalise meanings that correctly decline inner-being content (Mat 24:40: "no direct inner-being content"); the audit must not pressure every verse into an inner-being reading (silence-valid) | INFO* |

\*E8 is a guard, not a flag: it tells the auditor what *good* looks like so the other E checks don't push toward over-reading.

---

## Verdict & output

- **Gate verdict** = PASS unless any **GATE** aspect fails → **FAIL** (not validly Analysis Complete).
- **Incremental worklist** = the D items + any GATE/STRUCT failures, expressed as "re-submit (re-run a phase / add terms / adopt pointers)" vs "clear (resolve boundary / flag / observation; dissolve old VCG)".
- Per-cluster detail + a cross-cluster summary table + the consolidated worklist.
- Read-only; the auditor never writes. (Status demotion stays in the separate closure routine `_validate_analysis_complete`.)
