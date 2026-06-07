# Cluster status lifecycle + completion gates · design plan

**Living document** — single stable filename; version in this header, history + rollback in git. No `-vN` filename copies. [living-doc policy, 2026-05-31]
**Doc version:** 6 · **Created:** 2026-05-31 · **Last updated:** 2026-05-31
**Status:** Design plan for researcher review. No script built yet.
**Recent:** v3 review + C10–C12. v4 consolidated to single file. v5 grounded §3 against the DB. **v6 — §3 rewritten to the researcher's two-condition gate definition** (replacing the C1–C12 contract): (1) verse/tier findings captured; (2) every leftover — boundary, flag, SB/SD pointer — resolved to a validated observation or deleted after review. Link/structural repairs moved out to a data-cleansing prerequisite (§3.3).
**Owner items:** §F F13/F14 + §M4 in [wa-programme-open-items.md](../Programme/Program_reports/wa-programme-open-items.md).
**Enforces decisions:** §A A1 (pointers), A2 (old VCG codes), A3 (gaps), A4 (BOUNDARY + flags); relates to §M4 (status validation + spelling).
**Related:** gate-management refinement [wa-v3_0-refinement-1-gate-management-v1-20260529.md](wa-v3_0-refinement-1-gate-management-v1-20260529.md) — *attention* gates, a different concept (see §7).

---

## 1. The reframe (researcher direction 2026-05-31)

The earlier draft put a heavy multi-check "readiness gate" (F13) in front of input generation. That was the wrong place. The correct architecture:

- **The heavy validation belongs to the transition that PRODUCES `Analysis Complete`.** A cluster must not *earn* `Analysis Complete` unless its findings are captured and every leftover (boundary / flag / pointer) is resolved. This is the **Analysis-Complete gate** (§3).
- **F13 is then a trivial check** — "is `cluster.status = 'Analysis Complete'`?" It trusts the status because the gate already guaranteed it (§4).
- **Publishing produces a new status, `Publishing Ready`** (§5), set when inputs + prose + prose-in-DB are all done — the precondition for combined-document and other derivatives.

### The status lifecycle

```text
… analytical phases …
   → Analysis - In Progress
        │  ← Analysis-Complete completion contract (§3) MUST pass here
        ▼
   → Analysis Complete            ← pre-publishing; analysis validated
        │  ← publishing routine: generate inputs → coverage gate (F6)
        │                          → prose generation → prose ingested to DB
        ▼
   → Publishing Ready             ← NEW; ready for combined doc + derivatives
        │
        ▼
   → (Published / derivatives)
```

---

## 2. What produces `Analysis Complete` today — the finding

Investigated 2026-05-31. There is **no completion contract**. The status is flipped by per-cluster, per-phase closure scripts (e.g. `_apply_m10_phase12_closure`, `_apply_m38_phase_c`). A representative closure (`_apply_m10_phase12_closure_20260526.py`, L34–44):

```python
assert current[0] == 'Analysis - In Progress'           # only guard: prior status
cur.execute("UPDATE cluster SET status='Analysis Completed', …")  # bare flip
```

The **only** check is the prior status. No BOUNDARY check, no flag check, no pointer check, no coverage check, no linkage check. Consequences:

- This is exactly why the F7 audit keeps finding `Analysis Complete` clusters that fail readiness — nothing validated them at the transition.
- The **§M4 spelling drift originates here**: this script writes `Analysis Completed`; M38's wrote `Analysis Complete`. Ad-hoc scripts → inconsistent spelling.
- There is no single place that defines "what complete means" — it is reimplemented (or omitted) in every closure script.

**This is the script review you asked to dig into.** The fix is a single canonical closure routine that enforces the contract and writes one canonical status string.

---

## 3. The Analysis-Complete gate (the completion definition)

**The gate — researcher definition (2026-05-31).** A cluster is `Analysis Complete` when:

1. **Its verse/tier findings are captured** — the analytical findings grounded in the tier questions exist and are complete.
2. **Every leftover item — boundary, flag, Session B/D pointer — has been resolved to one of two end-states:** a **validated observation** (impact described), or **excluded/deleted after researcher review**.

**Nothing survives in limbo or as nonsense.** The cluster cannot be `Analysis Complete` while any leftover sits unreviewed, unconverted, or as a nonsense/irrelevant row still alive.

*(This replaces the earlier C1–C12 "contract" — that was one idea fragmented into twelve. These two conditions are the whole gate. Link/structural repairs are a separate data-cleansing prerequisite — §3.3.)*

### 3.1 The two conditions, operationally

**Condition 1 — verse/tier findings captured** (reads `cluster_finding`):

- every expected tier-question for the cluster's characteristics has a finding **or** an explicit `gap` row (no silent omission);
- no mis-classified / nonsense rows survive (e.g. M38's T5.7.3 — a `cluster_synthesis` row whose body is only a gap acknowledgment — is fixed or removed).

**Condition 2 — every leftover resolved to observation-or-deleted:**

- **Boundaries** — no active `BOUNDARY` sub-group with live members; each member promoted to a real sub-group, routed, or set aside.
- **Flags & Session B/D pointers** (`wa_session_research_flags`) — every gating-code flag is `resolved=1`, having become a `cluster_observation` (impact described) **or** been deleted with a reason. The **A1 data-cleansing session** performs this conversion programme-wide (and fixes the registry→cluster links); the gate then just confirms none remain `resolved=0` for the cluster.
- **Observations** (`cluster_observation`) — every *actionable* observation is `confirmed` or `delete_flagged=1`; none dangling/orphaned. *Informational* design-rationale types (VCG/SUBGROUP/TIER rationales, `design-note`, CLUSTER_SYNTHESIS) stay "open" by design and are not leftovers.

### 3.2 The four homes — what the conditions actually read (grounded against the DB)

| Object | Scope | "Done/resolved" mechanism | Holds |
|---|---|---|---|
| `cluster_finding` | cluster | `finding_status` ∈ {finding, cluster_synthesis, silent, gap} | the **tier** findings (`obs_id` → catalogue question) — **Condition 1** |
| `cluster_observation` | **cluster** (direct `cluster_code`) | `status` ∈ {open, confirmed} + `resolution_note` | observations; informational design-rationale types stay "open" by design — **Condition 2** |
| `wa_session_research_flags` | **registry/word** (→ cluster via `mti_terms.owning_registry_fk → cluster_code`) | **`resolved` 0/1** on every row (+ `resolved_note`) — uniform across all codes | flags, SB findings, SD pointers, boundary-pending — **Condition 2** (converted by the A1 session) |
| `session_d_*` (4 tables) | — | `gate` / `researcher_flag` | **all empty today** — "Session D follow-up" = `SD_POINTER` flags in the row above |

### 3.3 Data cleansing is a separate prerequisite — not the gate

Per researcher direction, *"the data cleansing will fix the links."* Structural/link repairs — **old-format VCG codes** (A2), **`mti_term_subgroup` term linkage** (M38 had zero), and the **registry→cluster mapping** the A1 pointer-conversion needs — are a **data-cleansing pass that runs before/around the gate**, repairing the substrate the two conditions read. They are *not* gate logic; the gate simply can't be satisfied cleanly until the substrate is sound. (These were the old C5/C6.)

---

## 3.4 Where each cleanup category lands

The register's §G–P enumerate every known DB-intervention category. Each maps to exactly one home:

| Register § | Problem | Where it belongs |
|---|---|---|
| §G BOUNDARY · §L3 boundary-pending | active boundary members / flags | **Gate — Condition 2** (leftover → observation or delete) |
| §K · §L1–2 (SB/SD pointers) | stray flags / pointers | **Gate — Condition 2**, converted by the A1 session |
| §N finding-class (M38 T5.7.3) | mis-classified finding row | **Gate — Condition 1** (no nonsense rows) |
| tier omissions (if any) | missing tier answers | **Gate — Condition 1** |
| §N old-VCG (M06) · §N term-linkage (M38) | broken links | **Data-cleansing prerequisite** (§3.3) |
| §H small coverage gaps · §J no-inputs | inputs missing evidence | **Publishing stage** (post-AC, F6) — *except* BOUNDARY-derived gaps, which resolve with §G |
| §I large gaps (M04/M07/M08/M09) | ~4,000 findings not in inputs | **UNKNOWN — pending F3 diagnostic**: mis-keyed → publishing; truly absent → Condition 1 |
| §L4–L8 | breadth notes, stale review, etc. | **Programme housekeeping** (not cluster-completeness) |

Two things this settles: **coverage ≠ analytical completeness** (§H/§I/§J are post-AC, *not* the gate — A3's "no AC while a gap exists" loosely conflated them), and **§I is the one genuine unknown** until the F3 diagnostic classifies it.

## 3.5 Why the current "Analysis Complete" is unreliable — and retro-validation

Today the status is a bare `UPDATE` in per-cluster closure scripts with no checks (§2); the F7 audit only *observes* afterwards, reports counts rather than gating, and mixes coverage with analytical state. So **every cluster currently marked `Analysis Complete` is unverified.**

When the two-condition gate is built — as `_close_cluster_analysis.py`, the canonical closure that writes the status only on a full pass, its predicate shared by the F7 audit — it must be **run against every current `Analysis Complete` cluster**, and any that fail are **demoted** to `Analysis - In Progress`. That produces one authoritative "what actually needs fixing" verdict per cluster, replacing the scattered §G–P symptom lists.

---

> **Why a tier-keyed audit can't do this.** The current audit keys off tier `question_code`, so it cannot see a flag (no tier), an unconfirmed observation, or an orphan. The three live in three objects with three "done" mechanisms — `resolved` 0/1 for flags, `status` for observations, reachability for findings. The gate reads each on its own terms; it is not a single tier query. Non-tier items are **legitimately expected and must not be lost** ([[feedback_setaside_verses_inform_word_meaning]]) — accounted for (observation or set-aside-with-reason), not silently dropped.

---

## 4. F13 — simplified

F13 is now a one-line precondition at the top of the input generator (and the F9 wrapper):

```python
if cluster["status"] != "Analysis Complete":
    abort(f"{code}: status is {cluster['status']!r}, not 'Analysis Complete' — not eligible for input generation")
```

Hard stop, nonzero exit, zero files. It does **not** re-run the gate checks — it trusts that the §3 gate already enforced them at the transition. If the status is right, the cluster is publishable; if not, the researcher is pointed back to the contract / §G / the A1 session. (The full readiness report becomes a property of the §3 contract failure, not F13.)

---

## 5. New status — `Publishing Ready`

**Proposed** new `cluster.status` value (controlled-vocabulary change — CLAUDE.md §14; needs researcher sign-off).

- **Set when:** the publishing routine has completed for the cluster — (a) 7 chapter inputs generated and passed the F6 coverage gate, (b) prose generated for all chapters, (c) prose ingested into `prose_section` (F4).
- **Means:** the cluster is ready for combined-document assembly and other derivatives (docx/pdf), per [feedback_cluster_publish_outputs].
- **Gates:** the combined-doc / derivative generators should require `status='Publishing Ready'` (analogous to F13 requiring `Analysis Complete` before input generation).
- **Transition owner:** the prose-ingest step (F4) fires the transition on the 7th chapter, once coverage passed.

This makes the publishing phase a first-class, state-tracked stage rather than an implicit "we have some files on disk" condition.

---

## 6. Open questions for researcher review

1. **Canonical status spellings.** Confirm the set + fix §M4: `Analysis - In Progress` → `Analysis Complete` → `Publishing Ready`. (Today both `Analysis Complete` and `Analysis Completed` exist across 17 clusters.)
2. **Condition 2 — gating flag codes.** Linkage path confirmed (`registry_id` → `mti_terms.owning_registry_fk` → `cluster_code`). Which flag codes gate? Proposed gating: `SD_POINTER`, `SB_FINDING`, `BOUNDARY_DECISION_PENDING`, action-requiring `PH2_*`. Proposed non-gating: `VERSE_EVIDENCE_BREADTH_NOTE` and other note-only codes. Confirm the split.
3. **Condition 2 — actionable vs informational observations.** Which `cluster_observation` `observation_type`s are **actionable** (must be `confirmed`: candidates CROSS_CLUSTER_HANDOFF, SELF_CHECK_OBSERVATION) vs **informational/exempt** (VCG/SUBGROUP/TIER/SPLIT rationales, `design-note`, CLUSTER_SYNTHESIS, INTEGRATION_NOTE, INTER_RELATIONSHIP, TIER_READING_GUIDE, VERDICT_RATIONALE)?
4. **Condition 1 — the catalogue.** The authoritative list of expected tier-questions per characteristic, to test omissions against.
5. **Retro-validation.** When the gate is built, **re-validate** all current `Analysis Complete` clusters and demote failures (per §A "provisionally incomplete")? Recommended.
6. **`Publishing Ready` adoption.** Approve the new status + its transition point (F4, on 7th-chapter ingest after F6 pass)?
7. **Data-cleansing prerequisites (§3.3).** Old-format VCG codes → cluster path (via `verse_context`/sub-group); `mti_term_subgroup` term-linkage backfill — sequence these *before* the gate runs. (Not gate logic.)

---

## 7. Relationship to the other "gates"

Two unrelated uses of "gate":

- **Data/status gates (this doc):** the §3 Analysis-Complete gate, F13 (§4), F6 coverage gate — automated pass/fail on data/status.
- **Attention gates (mechanical / confirmation / judgment):** the [gate-management refinement](wa-v3_0-refinement-1-gate-management-v1-20260529.md) — about *researcher involvement* across phase boundaries.

They meet when a contract check **fails**: that surfaces as a **judgment gate** in the attention taxonomy — pipeline pauses, writes the failure report, waits for disposition.

---

## 8. Build estimate

- Closure routine skeleton + **Condition 2** (boundary + flag checks, reusing the v2-audit boundary logic) + canonical status write: ~1.5 h. Needs §6 q1 (statuses) + q2 (gating codes).
- **Condition 2** observation-disposition check (q3 type list): ~0.5 h.
- **Condition 1** (tier completeness + classification): ~1 h. Needs the catalogue (q4).
- Shared predicate module + F7 import + **retro-validation** pass (q5): ~1.5 h.
- F13 simplified status check: ~15 min.
- *Data-cleansing prerequisites (old-VCG, term-linkage) are separate work, sized in the cleanup plan, not here.*
- `Publishing Ready` status + transition wiring (in F4): folded into F4 build.

---

*Design plan only. Review §3 (the contract) and §6 (open questions) — those determine what gets coded. F13 itself is now trivial; the substance is the completion contract that produces the status.*
