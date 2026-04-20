# WA — Global Readiness Sweep Instruction

**Framework B — Soul Word Analysis Programme  
Per-word mechanical data readiness audit + remediation  
Version 1_0 | 20260419 | Status: Active — approved 2026-04-19 by le Roux Cilliers**

| **Document** | **Value** |
|---|---|
| Filename | wa-global-readiness-sweep-instruction-v1_0-20260419.md |
| Supersedes | (new document) |
| Companion documents | wa-global-general-rules [current] · wa-reference [current] · wa-claudecode-rules [current] · wa-patch-instruction [current] · wa-directive-instruction [current] · wa-sessionb-analysis-readiness [current] |
| Design reference | outputs/investigations/wa-global-readiness-sweep-design-v1-20260419.md (APPROVED 2026-04-19) |
| Produced | 2026-04-19 |
| Primary actor | Claude Code (CC) — executes sweep, produces patches + directives, applies patches under approval |
| Researcher role | Per-registry patch approvals; per-directive approvals; RD resolutions |
| Claude AI role | Null — no analytical work. Issues requiring analysis surfaced as Path 3 (deferred to per-word v1.6 Stage 1) or Path 5 (outstanding tasks) |
| Preconditions | (1) DB-wide review complete (Schema Completion Record G5 approved) · (2) Schema at `3.10.0` · (3) For 6 reprocess-triggered words: `engine/audit_word.py` rewrite (OT-DBR-001) if Path 2 re-extraction directives are to be executed |

---

## Governing Rules

This instruction is governed by **wa-global-general-rules [current]** plus **wa-claudecode-rules [current]**.

CC confirms at session start (per CC-LOAD-001):

- Global rules file loaded — state resolved version
- This instruction loaded — state resolved version
- CC rules file loaded — state resolved version
- Patch instruction loaded — state resolved version
- Directive instruction loaded — state resolved version
- Sweep design doc (`outputs/investigations/wa-global-readiness-sweep-design-v1-20260419.md`) — confirmed APPROVED

Do not proceed without all confirmations recorded in the session observations log.

---

## Change Log

**v1_0 (2026-04-19):** New document. Based on approved design workings `wa-global-readiness-sweep-design-v1-20260419.md` (all 14 open questions resolved). Incorporates post-DBR schema awareness — all references are to schema 3.10.0 (post M19–M28).

---

## 1. Pipeline Position

```text
STEP Bible → Phase 1 (registration + extraction) → audit_word
       │
       ▼
Verse Context (per word, Claude AI)
       │
       ▼
Dimension Review (per word / cluster, Claude AI)
       │
       ▼
wa-global-database-review (DB-wide schema/column/FK cleanup — COMPLETE 2026-04-19)
       │
       ▼
═══════════════════════════════════════════════════════════
wa-global-readiness-sweep (THIS INSTRUCTION)
  Per-word mechanical data audit + Path 1 remediation patches.
  CC executes. Claude AI role: null. Researcher approves per-
  registry patches + directives. Sweep is rerun-safe (idempotent).
═══════════════════════════════════════════════════════════
       │
       ▼
Session B Stage 1 (Analysis Readiness — v1.6) — per word, Claude AI
       │
       ▼
Session B Stage 2 (Analysis Output) — per word, Claude AI
```

---

## 2. Scope and Worklist

### 2.1 Worklist filter

```sql
SELECT no, word, cluster_assignment,
       session_b_status, verse_context_status, dim_review_status
FROM word_registry
WHERE carry_forward = 1
ORDER BY no;
```

Expected count: ~213 registries (carry_forward=1). Excluded: ~30 with `carry_forward = 0` or NULL.

### 2.2 Invocation scopes

| Flag | Scope |
|---|---|
| (none) | Full worklist — default |
| `--scope=registry:N` | Single registry (e.g. `registry:68` for grace) |
| `--scope=cluster:C17` | All carry_forward=1 registries in the named cluster |

### 2.3 Special treatment of the 6 reset-to-`Verse Context Reset` registries

Compassion (23), fellowship (62), forgiveness (64), grace (68), love (103), mercy (111) were reset post-DBR. Sweep runs on them normally (per Q7):

- Path 1 remediation applied (mechanical patches additive only)
- Any structural invalidation → Path 4 RD
- Session B narratives from prior cycle remain in `outputs/markdown/` etc. as historical — sweep does not delete or import them

### 2.4 Locks

Per CC-LOCK-001: registries with `phase1_status = 'In Progress'` are skipped with an obslog note. Re-eligible in the next sweep session.

---

## 3. Governing Disciplines

- **Step-by-step** (GR-PROC-001). Each phase completed + signed off before the next.
- **Write on discovery** (GR-OBS-001, CC-OBS-001). Obslog is the primary record.
- **Data authoritative** (GR-PROC-002, CC-DATA-001). SQL against live DB + design workings only.
- **All changes through patches/directives** (GR-PROC-003). Patches to disk + researcher approval in obslog before apply.
- **No DB state assumptions** (GR-DB-001, CC-VERSION-001). Schema version check at session start.
- **Rerun-safe** (CC-RERUN-001). Sweep is idempotent; re-running on clean state is a no-op.
- **No analytical work** (CC-SCOPE-001). Surface to Path 3 or Path 5; never resolve inline.
- **RD via file** (CC-RD-001). Never ask in chat.
- **Skill-limit → outstanding tasks** (CC-SKILL-001).

---

## 4. Artefact Set

### 4.1 Per-sweep-session artefacts

| Artefact | Filename pattern |
|---|---|
| Sweep observations log | `outputs/session-logs/wa-global-readinesssweep-obslog-v{n}-{YYYYMMDD}.md` |
| Sweep session log | `outputs/session-logs/wa-global-readinesssweep-sessionlog-v{n}-{YYYYMMDD}.md` |
| RD accumulator | `outputs/wa-global-readinesssweep-rd-v{n}-{YYYYMMDD}.md` (created on first RD) |
| Sweep completion record | Within the obslog at sweep end |
| Programme readiness scorecard | `outputs/reports/wa-global-readiness-scorecard-{YYYYMMDD}.md` |

### 4.2 Per-registry artefacts

| Artefact | Filename pattern |
|---|---|
| Per-registry observations section | Within the sweep obslog |
| Per-registry remediation patch | `data/imports/WA/Patches/wa-{nnn}-{word}-readinesssweep-v{n}-{YYYYMMDD}.json` |
| Per-registry sub-process directive(s) | `data/imports/WA/Patches/wa-{nnn}-{word}-readinesssweep-dir-{seq}-{desc}-v{n}-{YYYYMMDD}.md` |

### 4.3 Persistent artefacts (cross-sweep)

| Artefact | Filename |
|---|---|
| Outstanding tasks (shared with DB review) | `outputs/wa-global-outstanding-tasks-v{n}-{YYYYMMDD}.md` |

### 4.4 Sweep identifier (per Q13)

Each sweep session has an identifier: `SWEEP-YYYYMMDD-NNN` (sequential per day). Stored in obslog header; carried on all artefact filenames where `{sweep_id}` would be useful.

---

## 5. Session Start Protocol

**Step S0 — Open or increment observations log** (GR-OBS-004, GR-FILE-004). First action of every session.

| Condition | Action |
|---|---|
| First sweep session | Create `wa-global-readinesssweep-obslog-v1-{YYYYMMDD}.md`. Write sweep identifier `SWEEP-{YYYYMMDD}-001`. |
| Resumption | Increment minor version `v[n.n+1]`. Sweep identifier retained if same day; increment sequence if new sweep. |

**Step S1 — Confirm governing documents loaded** (CC-LOAD-001). State resolved versions for 6 documents (see §Governing Rules).

**Step S2 — Pre-sweep tooling verification** (per Q5):

Run checks; halt on any failure:

| Check | Query / command | Expected |
|---|---|---|
| Schema version | `SELECT version_code FROM schema_version WHERE id = (SELECT MAX(id) FROM schema_version)` | `3.10.0` |
| `EXPECTED_SCHEMA_VERSION` | `engine/constants.py` | `3.10.0` (match) |
| Applicator presence | `ls scripts/apply_session_patch.py` | exists |
| Applicator PROSE ops | grep for `session_a_replace`, `insert on prose_section` | **If missing → Path 2 directives affecting prose writes are blocked.** Record in obslog. |
| audit_word.py post-DBR | grep for `somatic_link` or `god_as_subject` direct column reads | **If found → OT-DBR-001 still open; Path 2 audit_word re-run directives blocked.** Record in obslog. |

**Step S3 — Determine resume position** from Phase Progress Record in obslog:

| Last completed | Resume from |
|---|---|
| (blank) | S4 (begin worklist) |
| `worklist_built` | first registry in worklist |
| `registry_{nnn}_complete` | next registry in worklist |
| `all_registries_complete` | sweep close |

**Step S4 — Build worklist** per §2.1/§2.2 scope. Record count.

**Step S5 — Record resumption:**

```text
SESSION RESUMED: [date and time]
  Sweep identifier: SWEEP-YYYYMMDD-NNN
  Obslog version: v[n]
  Schema version: 3.10.0
  Worklist count: N
  Resume position: [registry nnn or 'worklist start']
  Pre-sweep tooling warnings: [none / list]
  Open RD items: [count]
  Outstanding tasks count: [count]
```

---

## 6. Per-Registry Pass — Phases R.A through R.L

For each registry `nnn` in the worklist, in order:

### Phase R.A — Registry state

Queries on `word_registry`:

| Check | SQL | Path if fail |
|---|---|---|
| Word identity | `word`, `no`, `cluster_assignment` | 4 (RD if mismatch) |
| Statuses | `session_b_status`, `verse_context_status`, `dim_review_status` | 1 if correctable; 4 otherwise |
| carry_forward | `carry_forward = 1` | (filter catches otherwise) |
| unique_term_count | Cross-check vs `COUNT(*) FROM wa_term_inventory WHERE ...` | 1 if drift > 5% |
| shared_term_count | Present | 1 if NULL → set 0 |
| dimensions | Not NULL or empty | 4 (RD if empty — Dimension Review may not have written) |
| `word_synopsis` (new M21) | Presence optional — record whether populated | 3 (researcher authors) |

### Phase R.B — Term inventory

Split into OWNER / XREF / deleted per v1.6 §B pattern. Post-DBR adjustments:

- **No more direct `somatic_link`/`god_as_subject` reads.** Use `mti_term_flags` joins:
    - GOD_AS_SUBJECT: `JOIN mti_term_flags mtf ON mtf.mti_term_id = mt.id AND mtf.flag_id = 1`
    - SOMATIC_INNER_LINK: `JOIN mti_term_flags mtf ON mtf.mti_term_id = mt.id AND mtf.flag_id IN (3,4)`
- **No more `status_note` reads** (M22 dropped).

**Three-number verse diagnostic** per OWNER term (from audit_word post-run summary or computed on-the-fly):

| Condition | Path |
|---|---|
| `span=0, active=0, deleted=0` | Path 2 — genuine zero-extraction; re-extraction directive |
| `span>0, active=0, deleted=span` | Path 2 — span filter failure; re-extraction + VC re-run |
| `active > occ × 1.1` | Path 4 — possible over-extraction |
| `active < occ × 0.2 AND occ > 20` | Path 1 — add `SMALL_VERSE_SAMPLE` quality flag if missing |

**XREF terms:** `mti_terms.status` must be `xref_[owning_word]` — Path 1 fix if NULL.

**Deleted terms:** `wa_term_inventory.delete_flagged = 1` where `mti_terms.status = 'delete'` — Path 1 fix if mismatch.

### Phase R.C — Verse records

Per OWNER term:

- `verse_text` non-NULL, non-empty — Path 3 if violated
- `reference` format `[Book] [Ch]:[Vs]` — Path 1 if malformed and recoverable
- `span_strong_match` — NULL count noted (Path 3 per WR-20 inherit)
- `translation = 'ESV'` — Path 4 if other
- `delete_flagged = 0` on active rows — Path 1

### Phase R.D — Verse context groups

`verse_context_group` + `verse_context`:

| Check | Path |
|---|---|
| `group_code` format `[mti_id]-[seq]` | Path 1 if correctable |
| `context_description` present (> 20 chars) | Path 4 if empty |
| Anchor verse count per group ≥ 1 | Path 2 (targeted VC anchor pass) |
| `is_anchor` and `is_related` mutually exclusive | Path 1 fix |
| `dominant_subject` valid value | Path 1 if `NONE` and derivable from context_description; Path 4 if NULL |
| Set-aside verse `set_aside_reason` populated | Path 3 (not blocking) |

### Phase R.E — Dimension assignments (post-DBR)

**Critical post-DBR adjustment:** `wa_dimension_index` is now 15 columns (M25 dropped 8 denormalised fields). Joins required for:

- `mti_term_id` → `verse_context_group.mti_term_id`
- `group_code` → `verse_context_group.group_code`
- `strongs_number`, `transliteration`, `gloss`, `language`, `owning_registry_word` → `mti_terms.*`
- `context_description` → `verse_context_group.context_description`

Checks (against retained columns):

| Check | Path |
|---|---|
| `dimension` not NULL | Path 2 (Dimension Review sub-process) |
| `dimension_confidence` in (`CLAUDE_AI`, `RESEARCHER`) | Path 2 for `KEYWORD_STRONG/WEAK`, `ROOT_INFERRED`, `UNCLASSIFIED` |
| `manual_override` populated (0 or 1) | Path 1 if NULL |
| Exactly one dimension row per active group | Path 4 if duplicates |

**Dimension vocabulary consistency check** (from dimension extract finding):

- Flag dimension labels using legacy slash style (e.g. `Theological/Divine-Human`) where the new canonical style is slash-less (e.g. `Divine-Human Correspondence`)
- Path 5 (outstanding task) — vocabulary normalisation is programme-wide, not per-registry

### Phase R.F — Flags, findings, catalogue counts (situational)

| Table | Filter | Record |
|---|---|---|
| `wa_session_b_findings` | `registry_id = nnn AND delete_flag = 0` | Total + by status |
| `wa_session_research_flags` | `registry_id = nnn` | By `session_target` and `resolved` |
| `wa_term_phase2_flags` | Active for this registry's terms | Count |
| `wa_obs_question_catalogue` | `source_registry_no = nnn OR source_word = [word]` | Extension count |
| FLAG-010 state | From `wa-global-flags [current]` | Informational |
| `wa_data_quality_flags` | Per term | Counts |

### Phase R.G — Supporting term data

| Check | Path |
|---|---|
| `wa_meaning_parsed`/`_sense`/`_stem` presence for OWNER terms | Path 3 if absent |
| `wa_lsj_parsed` for Greek terms | Note only |
| `wa_term_root_family` | `root_code` non-NULL if row exists → Path 1 |
| `wa_term_related_words` | Count (informational) |
| `wa_cross_registry_links` | Count (informational) |

### Phase R.H — Prose coverage (NEW — post-DBR)

Check whether prose store rows exist for this registry:

| Query | Expected | Path if fail |
|---|---|---|
| `SELECT COUNT(*) FROM prose_section WHERE registry_id = nnn AND delete_flagged = 0` | > 0 for Session B Analysis-Complete words (eventually); may be 0 pre-Session-A | Informational — flag whether Session A extract has been generated |
| Session A section presence (codes `sa_s1_d1`..`sa_s1_d6`) | Present if Session A has run | Path 5 — OT-DBR-SessionA (generator script not yet built) |
| `word_synopsis` populated on registry | Researcher-authored; may be NULL | Path 3 — note for researcher |

### Phase R.I — Consolidate and classify

Walk through all findings from R.A–R.H. Assign each to exactly one Path (1–5):

1. **Path 1** — mechanical correction → add to remediation patch
2. **Path 2** — sub-process re-run → produce directive
3. **Path 3** — deferred to per-word Stage 1 → record in outstanding tasks with tag `DEFER_STAGE1`
4. **Path 4** — RESEARCHER_DECISION → add to RD accumulator
5. **Path 5** — beyond CC skill → outstanding tasks with capability statement

Write the classification table to the obslog.

### Phase R.J — Patch + directive construction and approval gate

Build the remediation patch for this registry containing all Path 1 items. Name: `wa-{nnn}-{word}-readinesssweep-v1-{YYYYMMDD}.json`. Internal `patch_id`: `PATCH-{YYYYMMDD}-{nnn}-READINESSSWEEP-V1`. Patch type: `READINESSSWEEP` (new — **requires applicator extension; if not present, revert to `REPAIR-READINESSSWEEP` scenario**).

Build directive(s) for Path 2 items. Name: `wa-{nnn}-{word}-readinesssweep-dir-{seq}-{desc}-v1-{YYYYMMDD}.md`.

**Approval gate:** per Q6 — write to obslog:

```text
AWAITING APPROVAL: registry {nnn} {word}
  Patch file: [path]
  Directives: [paths]
  Path 1 items: N
  Path 2 items: M
  Path 3/5 items: K (in outstanding tasks)
  Path 4 items: L (in RD accumulator)

  Approval syntax: write below
    APPROVED: [date]        — proceed to apply
    REJECT: [reason]        — skip registry per Q14
```

CC polls obslog at session resume; does not proceed until marker present.

### Phase R.K — Apply + verify (post-approval)

After `APPROVED: [date]` marker found:

1. Apply patch via `python scripts/apply_session_patch.py --patch-file [path]`
2. Verify outcomes against expected states (targeted SELECTs per DBR-CHG pattern)
3. **Idempotence self-check** (per Q8): re-run phases R.A–R.H on the same registry; confirm **zero new Path 1 items**
4. If new items appear → patch construction had a gap → add to RD accumulator; do not proceed
5. If clean → record `REGISTRY {nnn} {word} — complete`

If rejected (`REJECT: [reason]` marker): record reason in RD accumulator; skip registry; continue to next (per Q14).

### Phase R.L — Registry completion record

Append to obslog:

```text
REGISTRY {nnn} {word} COMPLETE: [date]
  Path 1 applied: N
  Path 2 directives: M (status: awaiting / complete / blocked)
  Path 3 notes → outstanding tasks: K
  Path 4 RD items: L (status: resolved / open)
  Path 5 outstanding: J
  Idempotence check: PASS / FAIL
```

Move to next registry.

---

## 7. Session Close Protocol

**Step C1** — Do not end mid-registry if avoidable. Record exact position if interrupted.

**Step C2** — Verify obslog sections current (progress record, RD items, outstanding tasks references).

**Step C3** — Produce session log: `outputs/session-logs/wa-global-readinesssweep-sessionlog-v{n}-{YYYYMMDD}.md` — records position, open items, resume instructions.

**Step C4** — Save obslog with version increment. Record `SESSION CLOSED` block.

---

## 8. Sweep Completion (when worklist fully processed)

**Step F1** — Sweep completion record in obslog.

**Step F2** — **Programme Readiness Scorecard** (per Q11 — clustered with summary rows).

File: `outputs/reports/wa-global-readiness-scorecard-{YYYYMMDD}.md`

Structure:

```markdown
# Programme Readiness Scorecard — {date}

## Programme summary
Total registries: N
- Green (no Path 1/2/4 items): X
- Amber (Path 1 applied, no pending): Y
- Red (Path 2 directives outstanding or Path 4 RD open): Z

## Per cluster
### C01 — [label]
Summary row (counts by colour)
Per-registry rows

### C02 — [label]
...

## Per-registry detail
(Optional expansion — full grid)
```

**Step F3** — Outstanding tasks file carried forward (persistent).

---

## 9. Integrity Rules

| Rule | Text |
|---|---|
| RS-01 | Sweep is mechanical only. Any task requiring analytical judgement → Path 3 or Path 5 — never resolved inline (CC-SCOPE-001). |
| RS-02 | Schema version check at session start is non-negotiable (CC-VERSION-001). Mismatch → halt. |
| RS-03 | Per-registry patch requires researcher approval via obslog marker before application (CC-PATCH-001). |
| RS-04 | Sweep is rerun-safe. Re-running on a clean registry produces zero Path 1 items (CC-RERUN-001, CC-IDEM-001). |
| RS-05 | Locked registries (`phase1_status = 'In Progress'`) are skipped with obslog note; retried next session (CC-LOCK-001). |
| RS-06 | Every anomaly is classified into exactly one Path (1–5). No anomaly left unclassified. |
| RS-07 | `wa_dimension_index` reads must use joins to `verse_context_group` and `mti_terms` for data M25 dropped — no direct column reads on removed fields. |
| RS-08 | `somatic_link` and `god_as_subject` reads must use `mti_term_flags` joins (flag_id=1 for god; flag_id IN (3,4) for somatic). Direct column access on dropped fields is a bug. |
| RS-09 | Path 2 directives targeting `audit_word` re-runs are produced but execution is blocked until OT-DBR-001 (audit_word rewrite) is resolved — directives are recorded with `EXECUTION BLOCKED: OT-DBR-001` note. |
| RS-10 | Idempotence self-check (phase R.K) is mandatory after every applied patch. Gap detection → Path 4 RD. |
| RS-11 | RESEARCHER_DECISION items via RD accumulator `.md` file. Never asked in chat (CC-RD-001). |
| RS-12 | Tasks beyond CC's skill → outstanding tasks `.md` with capability statement (CC-SKILL-001). |

---

## 10. Appendix A — SQL Library

### A.1 Live OWNER terms for a registry

```sql
SELECT ti.id, ti.strongs_number, ti.transliteration, ti.language,
       ti.evidential_status, ti.occurrence_count, ti.causative_form_present,
       mt.status, mt.owning_word,
       (SELECT COUNT(*) FROM mti_term_flags mtf WHERE mtf.mti_term_id = mt.id AND mtf.flag_id = 1) AS has_god_as_subject,
       (SELECT COUNT(*) FROM mti_term_flags mtf WHERE mtf.mti_term_id = mt.id AND mtf.flag_id IN (3,4)) AS has_somatic
FROM wa_term_inventory ti
JOIN mti_terms mt ON mt.strongs_number = ti.strongs_number
WHERE ti.delete_flagged = 0
  AND ti.term_owner_type = 'OWNER'
  AND mt.status IN ('extracted', 'extracted_thin')
  AND mt.owning_registry_fk = :registry_id;
```

### A.2 Three-number verse diagnostic per term

```sql
SELECT ti.id, ti.strongs_number,
       SUM(CASE WHEN vr.span_strong_match = 1 THEN 1 ELSE 0 END) AS span_matches,
       SUM(CASE WHEN vr.delete_flagged = 0 THEN 1 ELSE 0 END)   AS active_verses,
       SUM(CASE WHEN vr.delete_flagged = 1 THEN 1 ELSE 0 END)   AS deleted_verses,
       ti.occurrence_count
FROM wa_term_inventory ti
LEFT JOIN wa_verse_records vr ON vr.term_inv_id = ti.id
WHERE ti.delete_flagged = 0 AND ti.term_owner_type = 'OWNER'
  AND ti.file_id IN (SELECT id FROM wa_file_index WHERE word_registry_fk = :registry_id)
GROUP BY ti.id;
```

### A.3 Dimension assignment with joins (post-DBR — all derivable joined)

```sql
SELECT wdi.id AS dim_id,
       vcg.group_code,
       vcg.context_description,
       vcg.mti_term_id,
       mt.strongs_number, mt.transliteration, mt.gloss, mt.language,
       wr.word AS owning_word,
       wdi.dimension, wdi.dimension_confidence, wdi.dominant_subject,
       wdi.manual_override, wdi.anchor_count, wdi.related_count, wdi.set_aside_count
FROM wa_dimension_index wdi
JOIN verse_context_group vcg ON vcg.id = wdi.verse_context_group_id
JOIN mti_terms mt ON mt.id = vcg.mti_term_id
JOIN word_registry wr ON wr.id = wdi.owning_registry_no
WHERE wdi.owning_registry_no = :registry_id
  AND wdi.delete_flagged = 0
  AND vcg.delete_flagged = 0;
```

### A.4 Prose store coverage per registry

```sql
SELECT pst.code, pst.label, COUNT(ps.id) AS sections
FROM prose_section_type pst
LEFT JOIN prose_section ps
  ON ps.section_type_id = pst.id
  AND ps.registry_id = :registry_id
  AND ps.delete_flagged = 0
  AND ps.superseded_by_id IS NULL
WHERE pst.delete_flagged = 0
GROUP BY pst.id
ORDER BY pst.sort_order;
```

---

## 11. Appendix B — Patch Template (READINESSSWEEP type)

```json
{
  "_patch_meta": {
    "patch_id": "PATCH-YYYYMMDD-NNN-READINESSSWEEP-V1",
    "patch_type": "READINESSSWEEP",
    "registry_id": NNN,
    "word": "word_name",
    "produced_by": "claude_code",
    "produced_at": "YYYY-MM-DDTHH:MM:SSZ",
    "session_b_status": null,
    "sweep_id": "SWEEP-YYYYMMDD-NNN",
    "source_instruction": "wa-global-readiness-sweep-instruction-v1_0-20260419.md"
  },
  "operations": [
    {
      "op": "update",
      "table": "wa_term_inventory",
      "match": {"id": 1234},
      "set": {"language": "Hebrew"}
    },
    {
      "op": "insert",
      "table": "wa_data_quality_flags",
      "values": {"term_inv_id": 1234, "flag_id": 9, "description": "sweep: small verse sample"}
    }
  ]
}
```

---

## 12. Appendix C — Directive Template (Path 2)

```markdown
# Sweep Directive: re-extraction for [word] r{nnn}

**Directive ID:** WA-{nnn}-{word}-readinesssweep-dir-001-re-extraction-v1-{YYYYMMDD}
**Sweep:** SWEEP-{YYYYMMDD}-NNN
**Registry:** {nnn} {word}
**Reason:** Phase R.B identified span filter failure on N terms.

## Actions required
1. Re-extract verse data for Strong's: [list]
2. audit_word targeted re-run for registry {nnn}
3. Verse Context classification for affected terms
4. Return fresh extract

## Execution path
`python -m engine.engine --mode=audit_word --registry={nnn} --scope=extract_rerun`

## Blocker
**EXECUTION BLOCKED: OT-DBR-001** — `engine/audit_word.py` rewrite required before this directive can be executed. Directive recorded; execution deferred.

## Approval
[ ] APPROVED  [ ] REJECT
Date: ___
Reviewer: le Roux Cilliers
```

---

## Approval

**Researcher approval — write below:**

Status: [ ] APPROVED — PROCEED (sweep ready to run)  [ ] REVISIONS REQUESTED

Date:  
Reviewer: le Roux Cilliers
Notes:  

---

*wa-global-readiness-sweep-instruction-v1_0-20260419.md*
*Framework B — Soul Word Analysis Programme*
*Based on: wa-global-readiness-sweep-design-v1-20260419.md (APPROVED 2026-04-19)*
*Preconditions: Schema Completion Record G5 APPROVED (2026-04-19); schema 3.10.0.*
