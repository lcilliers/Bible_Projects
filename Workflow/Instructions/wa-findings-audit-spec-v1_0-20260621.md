# Findings Audit — Specification

- **Doc:** wa-findings-audit-spec-v1_0-20260621.md · **Version:** v1_0 · **Date:** 2026-06-21 · **Status:** Policy RESOLVED (§8) — ready for implementation.
- **Rev (2026-06-21):** STOP is researcher-releasable after reporting; added FA-23 (unsubstantiated superlatives/exaggeration); added the corrective-action taxonomy (CA-1…CA-4, §3.1); §8 policy decisions resolved (all checks; STOP set FA-01/05/06/18; REVIEW blocking is corrective-action-dependent; self-explanatory report required; retro-baseline M03–M06).
- **Purpose:** a gate Claude Code runs **before** it (a) captures a cluster's findings into the DB and (b) produces the cluster essay — to catch structural, coverage, scope, data-quality and grounding problems while they are still cheap to fix.
- **Owner of the gate:** Claude Code (runs it). **Owner of the policy:** the researcher (sets severities; signs off REVIEW items).
- **Rationale:** every check below is grounded in a failure mode actually hit during the M01–M08 rework (cited in *[trigger]*). The audit converts those one-off catches into a standing check.

---

## 1. When it runs (two gates)

| Gate | Runs before | Blocks | Checks |
|---|---|---|---|
| **Gate 1 — Pre-capture** | `_apply_{cluster}_findings_capture` (findings → DB) | DB writes | FA-01 … FA-17 |
| **Gate 2 — Pre-essay** | essay drafting + `_apply_capture_cluster_essay` | essay capture | FA-18 … FA-22 |

A cluster does not advance past a gate while a **STOP** is open **unless the researcher releases it** — CC reports the STOP and the researcher approves the release (logged); a STOP is never silently bypassed. **REVIEW** items must be explicitly acknowledged by the researcher (logged), but do not hard-block. **WARN/PASS** proceed.

## 2. Inputs

Per cluster `MNN`:
- the findings files on disk: per-characteristic **tier-answers** + **evidence-profile**, the **cluster synthesis**, the **ib-characteristics** map (and any obslog);
- the cluster's **ve_lexical extract** JSON (and its meta);
- the **live DB** (mti_terms, verse_context, wa_verse_records, characteristic, prose_section);
- the **tier catalogue** (active question set) and the **controlled vocabulary** (for the jargon filter).

## 3. Outcome model

- **STOP** — a correctness defect; capture/essay does not proceed automatically. CC **reports** it; the researcher may **release** it with explicit approval (logged) or direct a corrective action (§3.1). Never silently bypassed.
- **REVIEW** — a judgement the researcher must see and sign off. **Whether it blocks depends on the corrective action chosen (§3.1):** CA-1 (accept) → proceed; CA-2 (CC fix) → corrected, then proceed; CA-3/CA-4 → blocks until resolved. Logged in the audit report.
- **WARN** — a hygiene issue; noted, non-blocking.
- **PASS** — clear.

Each check is also tagged **[AUTO]** (mechanical, CC-scriptable) or **[JUDGE]** (needs researcher/AI assessment; the audit surfaces the evidence).

### 3.1 Corrective actions

Every open **STOP** and **REVIEW** item is resolved by recording one of four corrective actions in the audit report. Only **CA-2** may be taken by CC on its own initiative; the rest are researcher-driven or researcher-approved.

| Code | Corrective action | Driven by | Use when |
|---|---|---|---|
| **CA-1** | **Accept the deficiency** — acknowledge it and proceed as-is | Researcher | The deficiency is known and tolerable (e.g. a real but acceptable silence, a thin sub-corpus). |
| **CA-2** | **Minor in-file fix by CC** before updating DB/essay | **CC** (then logged) | A small, unambiguous mechanical correction in the findings/essay file — e.g. strip an unsubstantiated superlative (FA-23), fix naming/version (FA-02/04), drop a verse not in the corpus (FA-18). No interpretive change. |
| **CA-3** | **Targeted file / DB fix** | Researcher-led (CC executes) | A specific, scoped correction needing a judgement — e.g. re-gloss a term (FA-14), set aside a band (FA-13), repair a characteristic (FA-05). |
| **CA-4** | **Set aside the findings/essay and reproduce in AI Chat** | Researcher-approved | A systemic defect the file-level fixes can't repair; the findings/essay are parked (not captured / superseded) and regenerated via AI Chat. |

CC proposes a corrective action for each item; the researcher confirms (except CA-2, which CC may apply and report). A **released STOP** must carry one of CA-1/CA-3/CA-4 (CA-2 would have cleared it rather than released it).

---

## 4. Gate 1 — Pre-capture checks

### A. Presence & structure
- **FA-01 · Files present** [AUTO] **STOP.** Every expected findings file exists for the cluster: one tier-answers + one evidence-profile per characteristic, plus the cluster synthesis and the ib-characteristics map. *[trigger: M07 — capture was requested but no findings files existed.]*
- **FA-02 · Canonical naming** [AUTO] **WARN.** Filenames follow `wa-{cluster}-…-v{n}-{date}.md`; characteristic slugs are consistent within the cluster. *[trigger: M03/M04/M05/M06 each used a different tier-file naming convention.]*
- **FA-03 · Front-matter** [AUTO] **WARN.** Each file carries File · Date · Version · Cluster · change-note.
- **FA-04 · Version discipline** [AUTO] **WARN.** Same-base-name files carry incremented `-v{n}`; no in-place overwrite of a prior version (GR-FILE-003).

### B. Characteristic-model integrity
- **FA-05 · Characteristic set consistent** [AUTO] **STOP.** The characteristic letters/count agree across ib-characteristics, the tier-answers set, and the profile set (e.g. A–F present in all three). *[trigger: capture scripts key on a fixed CHARS list; a missing per-char file silently drops a characteristic.]*
- **FA-06 · No DB UNIQUE collision** [AUTO] **STOP.** Pre-flight the capture insert: the planned `char_seq` (100+n) and letter-prefixed `short_name` do not collide with existing `characteristic` rows; `source_file` not already captured. *[trigger: UNIQUE(cluster_code,char_seq) and UNIQUE(cluster_code,short_name) collisions during M03/M05 capture.]*
- **FA-07 · Definitions present** [AUTO] **WARN.** Each characteristic has a non-empty definition (parsed from ib-characteristics §3 or profile §1).

### C. Coverage & silence
- **FA-08 · Question coverage** [AUTO/JUDGE] **WARN.** Per characteristic, report answered-vs-silent against the active tier catalogue (target: all live questions addressed). Flag characteristics with anomalously low coverage.
- **FA-09 · Silence convention** [AUTO] **WARN.** The file uses the **standard** silence marker + a coverage summary (recommended: M06-style "X of Y per tier"). Flag prose-only or ad-hoc markers that defeat a queryable count. *[trigger: M03 prose / M04 "not evidenced" / M05 "Silent" / M06 "SILENT" — four conventions, not countable uniformly.]*
- **FA-10 · Silences explained** [AUTO+JUDGE] **REVIEW.** Every silent answer carries a stated reason, and each maps to an *expected cause* (faculty-not-engaged · data-shape · register · defining · lexical-fit · thin-evidence; see wa-silent-answers-why-expected-v1). Surface any silence not attributable to an expected cause as a candidate gap. *[trigger: the silent-answer audit, 2026-06-21.]*

### D. Scope & set-aside
- **FA-11 · Verse-count reconciliation** [AUTO] **REVIEW.** The findings' in-scope verse count = the extract's = the DB in-scope corpus (`set_aside_reason IS NULL`, active). Report any divergence with its cause (set-aside vs term-reassignment vs stale extract). *[trigger: M08 cluster-summary 680 vs extract 253; M01–M03 stale-extract drift.]*
- **FA-12 · Set-asides documented** [AUTO] **WARN.** Out-of-scope occurrences carry a `set_aside_reason`; the findings name the scope basis. *[trigger: M02/M03/M08 set-aside passes.]*
- **FA-13 · Non-inner-being bands surfaced** [AUTO+JUDGE] **REVIEW.** Characteristics or term-bands with **zero inner-being faculty** across all occurrences are flagged for a cluster-vs-set-aside decision. *[trigger: M05 flag 6 — ekklēsia/koinōnia corporate band.]*

### E. Data-quality
- **FA-14 · Gloss ↔ sense consistency** [AUTO] **REVIEW.** For each high-frequency term, compare the term gloss to the distribution of per-occurrence senses; flag likely disambiguation artifacts (gloss says one thing, occurrences say another). *[trigger: M05 flag 5 — chesed glossed "shame" but 289 occurrences read "steadfast love".]*
- **FA-15 · Duplication** [AUTO] **REVIEW.** Detect intra-verse repeats and cross-Strong's splits that double-count evidence. *[trigger: M05 flag 7.]*

### F. Governance
- **FA-16 · Open forks listed** [AUTO+JUDGE] **REVIEW.** Extract every interpretive fork / open question / flag from the findings (e.g. ib-characteristics "interpretive choices", synthesis "open questions") into an acknowledgement list — so they are decided, not silently captured. *[trigger: M06 IC1–IC4; M05 flags 5/6/7.]*
- **FA-17 · Extract provenance current** [AUTO] **WARN.** The extract the findings were built on carries a real `extract_version` + generation date and reflects the current engine state (T2-filter, set-aside honouring); not a stale string. *[trigger: M05 "VERSION NOT CONFIRMED" + hardcoded 2026-06-18 source.]*

### G. Claims & substantiation
- **FA-23 · Unsubstantiated superlatives / exaggeration** [AUTO+JUDGE] **REVIEW.** Flag claims of **primacy, magnitude or absoluteness** and check each against the foundation — a superlative is allowed only where the data substantiates it. Patterns: "the most important … in the study", "the largest coverage for …", "the broadest/strongest/deepest", "by far", "unprecedented", "always / never", "every / none", "unique(ly)". A **programme-wide** superlative ("the most X in this research") is allowed only where **programme-wide data** is on hand — a within-cluster claim must be scoped to the cluster ("the most X *in this family*"). Unsubstantiated or over-scoped claims are flagged for correction (typically **CA-2** — CC tones the claim to what the evidence carries). **Runs at both gates:** over the findings prose at Gate 1 and the essay draft at Gate 2. *[trigger: essay style template §5 (no project-wide superlatives unless the foundation states programme-wide data).]*

---

## 5. Gate 2 — Pre-essay checks

- **FA-18 · Cited verses exist** [AUTO] **STOP.** Every verse the essay will quote exists in the corpus/DB. *[trigger: M06 essay — "love covers a multitude of sins" (1Pe 4:8) is not in the DB; dropped before drafting.]*
- **FA-19 · Quotes verbatim** [AUTO] **WARN.** Quoted verse text matches the DB text exactly (translation/wording).
- **FA-20 · Jargon filter** [AUTO] **WARN→STOP.** The essay draft is free of project-internal vocabulary (cluster · characteristic codes · tier codes · valence · faculty · finding · VCG · sub-group). STOP if codes leak; WARN on borderline terms. *[trigger: M05/M06 essay jargon catches.]*
- **FA-21 · Completeness / reverse-audit** [AUTO+JUDGE] **REVIEW.** Every captured characteristic and its substantive findings are either present in the essay or a justified silence (per the essay style template §3). *[trigger: the "essay leaves findings out" concern, 2026-06-20.]*
- **FA-22 · Derive-from-foundation** [JUDGE] **REVIEW.** No claim in the essay that the captured findings do not carry; new insights surfaced for capture rather than asserted.
- **FA-23 · Unsubstantiated superlatives** [AUTO+JUDGE] **REVIEW.** *Re-run here over the essay draft* — full definition in §4.G.

---

## 6. Output

A report `Sessions-v2/{CLUSTER}/findings/wa-findings-audit-{CLUSTER}-{date}.md`. **The report must read on its own (policy 8.3): every finding is written in plain language — *what was checked · what was found · why it matters · the recommended action* — so the researcher never has to open another file to decode an `FA`/`CA` reference. Codes appear only as a bracketed secondary tag, and the report carries its own short inline legend.** It contains:
1. **Verdict line:** `GATE 1: PASS | REVIEW(n) | STOP(n)` and the same for Gate 2 — each followed by a one-sentence plain summary.
2. **Findings** — one plain-language entry per non-PASS check, not a bare code table. *Example:* "**Coverage** — Gentleness reads silent on 26 questions, but every one is expected: gentleness is mind-governed, so the feeling-based questions don't apply. No action needed. *[FA-10 · REVIEW]*". *Example:* "**Verse check** — the essay quotes 1Pe 4:8 ('love covers a multitude of sins'), which isn't in the corpus; I'll drop it and use Pro 10:12 instead. *[FA-18 · STOP → CA-2]*".
3. **STOP list** — each with the evidence, CC's proposed corrective action (§3.1), and a **release** field (researcher approval to proceed).
4. **REVIEW list** — researcher sign-off items, each with the evidence to decide and CC's proposed corrective action (CA-1…CA-4).
5. **Acknowledgement block** — the researcher records, per open item, the **corrective action taken** and (for STOPs) the **release approval**; CC proceeds once recorded.

## 7. Workflow integration

```
findings ready
   └─► Gate 1 audit  ──STOP──► CC reports → researcher RELEASES (CA-1/3/4) or CC fixes (CA-2) → re-run
        │ REVIEW ─► researcher acknowledges + records corrective action (logged)
        ▼ PASS / released / ack
   capture findings → DB  (_apply_{cluster}_findings_capture)
        ▼
   Gate 2 audit (on the essay draft)  ──STOP──► CC reports → release or CC fixes → re-run
        │ REVIEW ─► researcher acknowledges + corrective action
        ▼ PASS / released / ack
   capture essay → DB + render docx/pdf
```

## 8. Policy decisions — RESOLVED (2026-06-21)

1. **STOP set** — **accepted:** FA-01, FA-05, FA-06, FA-18.
2. **REVIEW blocking** — **depends on the corrective action identified** (§3.1): CA-1 (accept) → log and proceed; CA-2 (CC fix) → CC corrects, then proceeds; CA-3/CA-4 → blocks until resolved.
3. **Audit-report readability** — **required:** the report must be understandable on its own. Every finding is written in plain language (what was checked · what was found · why it matters · recommended action); nothing requires consulting a separate file to decode FA/CA references. (See §6.)
4. **Scope of v1** — **all checks** implemented.
5. **Retro-audit baseline** — **M03–M06 only.** *(M07 in progress; M08 not yet started; M01–M02 are prototyping items that predate the standard and are out of scope.)*

*Deferred:* mandating the M06-style "X of Y per tier" coverage line as a findings-authoring convention. For now it is a **recommendation surfaced by FA-09 (WARN)**, not a hard requirement — elevate to a mandate when ready (it is what makes FA-08/09/10 fully automatic).

## 9. Implementation note (not part of the spec to approve)

Realisable as one read-only script `_audit_findings_v1_{date}.py --cluster MNN [--gate 1|2] [--essay PATH]` that emits the §6 report and returns a non-zero code on any open STOP — so it can sit as a precondition in the capture/essay step. Most checks are mechanical against the files + DB; the [JUDGE] checks emit the evidence for the researcher rather than a verdict.
