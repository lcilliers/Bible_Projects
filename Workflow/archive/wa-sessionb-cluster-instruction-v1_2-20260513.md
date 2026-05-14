# wa-sessionb-cluster-instruction-v1_2-20260513

> Framework B Soul Word Analysis Programme — Session B Cluster Analysis
> Version: v1_2 | Date: 20260513
> Status: **Active — authoritative instruction for Session B analytics**
> **Change note v1_1 → v1_2 (2026-05-13):** Refinements derived from M05/M06/M15/M26 completed runs. (1) §4 — removed `wa-cluster-overview-v{N}-{date}.md` from Phase 1 inputs (cluster context is contained in the comprehensive report; the overview is a programme-wide artefact, not a cluster-input). (2) §6 — T1 framework definition pulled out as a visible callout block so it cannot be missed; inputs reframed to reference sections of the comprehensive report rather than introducing additional report files (gloss list and root-family info are already in the comprehensive report's §1 and §3). (3) Status changed from DRAFT to Active.
> Replaces (on finalisation):
> - wa-sessionb-analysis-readiness [current]
> - wa-sessionb-analysis-output [current]
> - wa-dimensionreview-instruction [current]
> - wa-versecontext-instruction [current]
> - wa-registry-management-guide [current]
> Governed by: wa-global-general-rules [current]

---

## 1. Document scope

This instruction is the authoritative source for the Session B cluster analysis flow — the analytical phase that takes a cluster dataset (terms + verses + prior groupings) and produces a fully-classified cluster with sub-groups, verse-context groups, anchor verses, and a full catalogue-prompt findings record in the database.

**Remains in force, referenced by this instruction:**

- wa-directive-instruction [current] — every cluster-process change to the database goes via a directive (this instruction never authorises CC writes directly)
- wa-patch-instruction [current] — verse-status patches and any non-cluster-process DB writes
- wa-claudecode-instruction [current] — CC's operational responsibilities, including cluster-process directive execution
- wa-database-schema [current] — table reference (`cluster`, `cluster_subgroup`, `cluster_finding`, `verse_context_group`, `verse_context`)
- wa-sessiona-prose-instruction [current] — Session A prose source
- wa-sessionc-cluster-overview [current] — downstream consumer of completed cluster findings (the cluster publication process)
- wa-sessiond-orientation [current] — cross-cluster synthesis consumer
- wa-obs-catalogue-tiered (extract) — the 189-prompt catalogue (T0–T7), input to Phase 8
- wa-cluster-overview / wa-cluster-catalogue (extracts) — cluster-level metadata
- wa-programme-prose-extract — programme prose, not modified by this instruction

---

## 2. Operating principle

The non-negotiable rule, established at session open and applied throughout:

> **Read every verse. Do not sample. Read what they say. Let the structure and analysis emerge from what is found. No assumptions from memory. No jumping to conclusions. Write on discovery.**

Prior attempts at cluster analysis were discarded because they classified verses against pre-formed assumptions rather than reading each verse and deriving the analysis from what the verse actually said. Output that is structured and fluent but not grounded fails this rule.

The cluster at session open is a body of textual evidence waiting to be interrogated — not a set of claims waiting to be confirmed.

**Write-on-discovery — what this means in practice:** Every observation is written at the moment it is made, from the text that produced it. If an observation has not been written before moving to the next verse, it is not written — do not reconstruct observations from memory after the reading is complete. Memory compresses and distorts; the text does not. If you find yourself summarising at the end of a reading block rather than recording as you go, stop and go back.

**Cross-cluster contamination guard:** When working cluster N, prior knowledge from clusters 1 through N-1 must not colour the reading of cluster N's verses. Each cluster's verses are the sole authority for that cluster's findings. A finding that appears in a prior cluster is not evidence that the same finding applies here — it must be re-evidenced from this cluster's verse text. This is especially important for prompts where a cluster-level finding emerged prominently in prior work (e.g. the spirit-level silence finding in M06). Do not assume the same answer — re-read and re-determine each time.

**Fluency is not a quality signal.** Output that reads smoothly and is well-structured can still be entirely ungrounded. The test for every response in Phase 8 is not "does this sound right?" but "can I name the specific verse or group that evidences this?" If no verse can be named, the response is not evidenced — mark it S (silent) or G (gap) rather than producing plausible-sounding text.

---

## 3. Starting point — session open

Before any analytical work begins, the session opens in full compliance with the Session Startup Rule (`wa-global-rules-startup [current]`):

1. Obslog created with prefix `wa-obslog-{cluster_code}-{description}-v1-{YYYYMMDD}.md` and saved to `Sessions/Session_Clusters/{cluster_code}/`. Filename per `wa-global-rules-all [current]` GR-FILE-001 / GR-FILE-007.
2. Obslog version is incremented at every transition point — phases, sub-groups, terms. Writing to the obslog is non-negotiable from this point.
3. If obslog writing is interrupted or discontinued, the session **must stop**. Recover the missing recordings first; only then proceed.

The cluster dataset (extracts produced by the report scripts in §10) is the starting input. The dataset includes the terms assigned to the cluster, their associated verses, any prior verse-context groups, dimension assignments, findings, and SD pointers. Prior analytical results are treated as candidate evidence, not as confirmed truth — they will be read and re-validated by the work below.

**Cluster status transition at session open:** `cluster.status` must be `Not started` or `Data - In Progress`. If it is `Analysis Completed` or `Published`, this is a re-open scenario and requires explicit researcher direction.

---

## 4. Phase 1 — Comprehension of the dataset

**Purpose:** establish a reading-level understanding of the cluster — what terms, how many verses, what prior groupings exist, what evidence has already been recorded.

**Inputs (reports — see §14):**

- `wa-cluster-{code}-comprehensive-v{N}-{date}.md` — full per-term identity, every verse with status, all prior groups, findings, SD pointers
- `wa-cluster-{code}-detail-v{N}-{date}.md` — compact per-term overview

**Output:**

- High-level overview note in the obslog (Phase 1 section): term count, verse count, prior-group count, prior-finding count, prior-SD-pointer count, observations on data shape.

**No DB writes in Phase 1. No patches or directives produced.**

**Cluster status at end of Phase 1:** `Data - In Progress` (CC sets via §11 directive — small status-update directive at session open if needed).

---

## 5. Phase 2 — UT verse review

**Purpose:** ensure no verses carry status UT (untouched) — every verse with status UT must be read individually from its text, the term-spans noted, and the verse classified.

**Inputs:**

- `wa-cluster-{code}-comprehensive-v{N}-{date}.md` — UT verses are identified by status column (UT = no `verse_context` row exists for that `(verse_record_id, mti_term_id)` pair)

**Process per UT verse:**

1. Read the verse text in full. Note the term-spans recorded at this verse location.
2. Determine the term's actual relevance:
   - **Confirmed relevant** — the verse evidences the term's characteristic
   - **Borderline** — needs researcher decision; flagged for attention
   - **Set aside** — the verse uses the term in a sense unrelated to the cluster's characteristic; populate `set_aside_reason`
3. Record the determination in the obslog with the verse reference, term, and one-line reason.

**Output:**

- Obslog entries per verse (Phase 2 section)
- A UT review document: `Sessions/Session_Clusters/{code}/WA-{code}-UT-verse-review-v1-{date}.md` — table form, one row per (verse, term), with proposed status + reason
- The review document is the input to a CC apply step

**DB writes — VCREVISE patch (the existing VC-family patch type):**

Phase 2 uses the standard VC patch path per `wa-patch-instruction [current]` §3, §15. No new mechanism is introduced.

**ID resolution before patch authoring.** AI does not know `verse_record_id` at review-document authoring time. Before drafting the patch, AI runs a small resolver query (or asks CC for a one-shot lookup) to map every (book, chapter, verse_num, mti_term_id) tuple in the review document to its `verse_record_id`. The resolver output is a JSON dict that AI consumes when building the patch.

**Patch construction:**

- `_patch_meta.patch_type = "VCREVISE"`
- `_patch_meta.terms_covered` = every Strong's mti_term_id touched
- `_patch_meta.input_versions` = `{mti_term_id: md_version}` per `wa-patch-instruction [current]` §15.6.4-bis
- Filename: `wa-cluster-{code}-patch-vcrevise-utreview-v1-{date}.json` (cluster-prefixed VCREVISE per the cluster scope)
- Operations (per the existing VCREVISE catalogue):
  - Set-asides → `verse_context` upsert with `set_aside_reason` populated, `is_relevant=0`
  - Confirmed-relevants → `verse_context` upsert with `is_relevant=1`, `group_id` left null (Phase 7 will assign)
  - Borderlines → not written (held for researcher decision; recorded in obslog only)
- Patch validates and applies through `scripts/apply_session_patch.py`.

**Why patch, not directive, for Phase 2:** the user has chosen to stay with established DB methods. VCREVISE already supports the operation set; the resolver step makes verse_record_id available to AI; the patch path is auditable and idempotent. A directive route is technically equivalent but introduces an additional pattern that the new cluster instruction does not need.

**Companion review document:**

`Sessions/Session_Clusters/{code}/WA-{code}-UT-verse-review-v1-{date}.md` — the structured review (one row per verse-term, with proposed status + reason). The patch references this document in `_patch_meta.description`.

---

## 6. Phase 3 — Characteristic debate from the gloss list

**Purpose:** subdivide the cluster's terms into provisional sub-groups based on distinct characteristics.

### The T1 framework definition (apply throughout this phase)

> **A distinct inner-being characteristic has:**
>
> 1. **Identifiable constitutional location** — heart, mind, will, conscience, soul, spirit, or body — where in the inner person it sits.
> 2. **A distinguishable set of inner faculties engaged** — perception, thought, memory, feeling, conscience, will, agency.
> 3. **A recognisable impact** — the characteristic produces a definable effect on the person, on relationships, or on action.
> 4. **A structural opposite** — the characteristic has a named or implicit opposite that defines its contour from the other side.
> 5. **A distinguishing causal direction or directional object** — the characteristic is directed toward, produced by, or operating against something nameable.

A grouping that does not satisfy these criteria is not a characteristic-bearing sub-group; it is either a BOUNDARY (supportive / descriptive / qualifying term) or a flag for cluster reassignment.

### Recognised tension

The inner being is not made of separable bricks neatly assignable to sub-groups. It is made of compounds that morph and change character through the person's inner life. **The onion principle:** each analytical layer peels without discarding the whole. Sub-groupings are peels — not divisions.

### Inputs

The cluster's comprehensive report is the sole input — gloss list, root family, and per-term lexical detail are already in it:

- `wa-cluster-{code}-comprehensive-v{N}-{date}.md`:
  - **§1 Cluster summary** — cluster description, full gloss list, per-term stats
  - **§3 Per-term comprehensive detail** — for each Strong's: gloss, transliteration, root family, related words, verse counts, current placements

If a fresher snapshot is needed, re-run `_generate_cluster_comprehensive_v1_*.py` per the report-regen rule (§14). Do not introduce additional report files for this phase.

### Process

1. Read all glosses against the T1 characteristic definition above.
2. Propose provisional sub-groups, each named by the dominant characteristic it carries.
3. Identify three categories of terms:
   - **Characteristic-bearing** — assigned to a sub-group (e.g., M06-A Hatred)
   - **Supportive / descriptive / qualifying** — terms that enhance or describe but are not themselves characteristics → BOUNDARY sub-group (or equivalent)
   - **Flagged** — terms requiring further investigation, possibly belonging to a different cluster, or not fitting the cluster at all → flagged sub-group, or proposed cluster reassignment

### Output

- Provisional sub-group list with rationale per sub-group → obslog (Phase 3 section)
- A characteristic-debate document: `Sessions/Session_Clusters/{code}/WA-{code}-characteristic-debate-v1-{date}.md` — captures the full debate, candidate groupings, and rationale

**No DB writes in Phase 3.** The sub-groups remain provisional until Phase 4 control-read confirms them.

**Provisional-by-definition guard:** Phase 3 output is a hypothesis, not a finding. Grouping from glosses alone is inherently incomplete — glosses are compressed labels, not readings of the verses themselves. Do not treat Phase 3 groupings as settled. Do not begin Phase 5 reading with the assumption that the Phase 3 groupings are correct. The control read in Phase 4 exists precisely because Phase 3 groupings will need revision. In M06, the control read produced nine term reassignments, two new sub-groups (malice, BOUNDARY), and two cluster reassignments — none of which were visible from the glosses alone.

---

## 7. Phase 4 — Control read and the compound-morphing correction

**Purpose:** validate the provisional sub-groups via a bidirectional control read.

**Inputs:**

- The provisional sub-group list from Phase 3
- `wa-cluster-{code}-comprehensive-v{N}-{date}.md` — for each term's full meaning text, evidential status, and verse pattern

**Process — bidirectional control:**

- **Direction 1 — grouping → term:** does each term's actual description fit the proposed group?
- **Direction 2 — term → grouping:** does the term's full description resist the proposed group? Does it suggest a different sub-group, a different cluster, or no cluster at all?

The control read may surface:
- Re-assignment to another sub-group within the cluster
- Transfer into or out of the BOUNDARY / supporting sub-group
- Cluster reassignment (term moves to a different M-cluster, T2, or FLAG)
- Additional flags requiring researcher resolution

**Output:**

- Confirmed sub-group list with any cluster reassignments → obslog (Phase 4 section)
- Issues raised for researcher input, with proposed dispositions

**Open-question discipline:** Every question flagged during the control read that cannot be resolved by reading alone must be recorded in the obslog in the format OQ-NNN, with a proposed disposition. The directive is authored only after all OQ items are resolved — not submitted (the researcher review on submission is the normal workflow gate), but *authored*. An unresolved OQ means the directive's scope is not yet known. Researcher confirmation of all OQ dispositions is what makes the scope definite.

**DB writes — TWO directives may be produced:**

1. **Sub-group assignment directive** — creates `cluster_subgroup` rows (one per sub-group + BOUNDARY where applicable), assigns each term's `mti_terms.cluster_subgroup_id`. Pattern per `wa-directive-instruction [current]` §11.4.
   - Filename: `wa-cluster-{code}-dir-002-subgroup-assign-v1-{date}.md`
   - Required content per the five-element form (§11.3 of directive instruction):
     - **MOTIVATION** — cite the characteristic-debate document and obslog
     - **SCOPE** — every Strong's listed with its sub-group destination; every cluster_subgroup row to be created with code, label, description
     - **OUTCOME REQUIRED** — count per sub-group, total terms post-update
     - **COMPLETION CONFIRMATION** — `SELECT subgroup_code, COUNT(*) FROM mti_terms mt JOIN cluster_subgroup cs ON cs.id=mt.cluster_subgroup_id WHERE mt.cluster_code='{code}' GROUP BY subgroup_code` matches expected counts

2. **Cluster reassignment directive** (if applicable) — moves terms out of the cluster.
   - Filename: `wa-cluster-{code}-dir-003-term-rebind-v1-{date}.md` (or merged into the sub-group directive's Operation B)
   - Required content per directive §11.6
   - Companion: any orphan `cluster_subgroup` rows are cleaned up here

**Cluster status transition:** `Data - In Progress` → `Analysis - In Progress` (set as part of directive's outcome).

---

## 8. Phase 5 — First reading pass and 250-word sub-group summaries

**Purpose:** produce a high-level analytical summary per sub-group as context for the deeper passes that follow.

**Inputs:**

- A new extract reflecting the just-applied sub-groups: `wa-cluster-{code}-grouped-v{N}-{date}.md` (cluster → sub-group → group → anchor + verses, with stats and per-term lexical context per the v2 layout)
- The obslog with Phases 1–4 entries

**Report required at phase open:** a fresh grouped report reflecting Phase 4's applied directives must be uploaded before Phase 5 begins. The phase-start report requirement is stated at the head of each phase in the inputs section — follow that instruction. Do not proceed with a grouped report produced before Phase 4's sub-group assignments were applied; it will not reflect the confirmed sub-group structure (§14 report regen rule).

**Process per sub-group:**

1. Read every verse currently assigned to the sub-group (across all the sub-group's terms and groups).
2. Produce a 250-word summary describing what the sub-group's verses, taken together, evidence about the characteristic.
3. Record any observations that emerge during summary preparation — these may seed later finding entries.

**Output:**

- One 250-word summary per sub-group → obslog (Phase 5 section)
- A summary document: `Sessions/Session_Clusters/{code}/WA-{code}-subgroup-summaries-v1-{date}.md`

**No DB writes in Phase 5.**

---

## 9. Phase 6 — Group-verse mapping per sub-group

**Purpose:** every verse in the cluster (excluding set-asides) belongs to at least one `verse_context_group`, and each group has a precise context description grounded in the actual verse text.

A verse may carry more than one distinct inner-being phenomenon; in that case it receives multiple group assignments. A verse_context_group may contain multiple verses where the same context applies.

**Inputs:**

- `wa-cluster-{code}-grouped-v{N}-{date}.md` — verses by sub-group, current group assignments, anchor designations
- The obslog with the Phase 5 summaries

**Process per sub-group:**

1. Read every non-set-aside verse in the sub-group.
2. For each existing group, validate the description against the actual verse evidence; revise if necessary.
3. Where verses carry phenomena not captured by existing groups, propose new groups.
4. For each verse, record which group(s) it belongs to and the per-verse observation (the analytical note that captures what the verse contributes).
5. Designate one anchor verse per group — the verse that most directly and definitionally evidences the group's named phenomenon.
6. Identify cross-group dual assignments — verses that legitimately belong to two groups.

**Output per sub-group:**

- A group-verse mapping document: `Sessions/Session_Clusters/{code}/WA-{code}-{subgroup}-group-verse-mapping-v1-{date}.md`
- Structured per the M06-A precedent (`wa-directive-instruction [current]` §11.4):
  - One section per group: existing code OR provisional new code, status (RETAINED / RETAINED AND REFINED / NEW / REVIEW AND DECISION), description, verse table (Verse | Term | What the verse shows), anchor verse declaration with rationale
  - A cross-group / dual-assignment table at the end
  - Optional flags-for-CC section if any verses cannot be classified within the proposed structure

**Self-check before submission:**

- Every verse in the sub-group is either assigned to a group or has a `set_aside_reason`. No verse is left in P (pending) or UT (untouched) state.
- Every group has at least one anchor verse.
- The mapping document's verse counts add up to the sub-group's total non-set-aside count.

**Obslog discipline:** every group, verse-to-group assignment, anchor designation, and per-verse observation is recorded in the obslog as the work progresses — flushed to file at the end of each term within the sub-group.

**Conglomerate-group split instruction:** When reading the verses assigned to an existing group, if they contain genuinely distinct inner-being phenomena — different subjects, different directions, different faculty engagements, different consequences — the group must be split before the catalogue pass begins. Do not apply catalogue prompts to a conglomerate containing multiple distinct phenomena; the answers will be the average of things that are not the same, and the finding will be analytically false.

The test for splitting: can the group's verses be answered uniformly by a single anchor verse, or do different subsets of the verses require different anchors to answer the same prompt? If different anchors are needed for different subsets, the group should be split. Produce new groups with their own anchors, record the split in the obslog, and flag for CC via the Phase 7 directive.

In M06, the split of group 1601 (139 sa.ne verses) into five distinct groups was the most consequential single analytical act of the session. The instruction to split came from reading the verses — not from the group label.

**Phase 6 produces no DB writes.** The mapping documents are the analytical artefact; database application happens in Phase 7.

---

## 10. Phase 7 — Group-verse mapping application

**Purpose:** apply each sub-group's group-verse mapping document to the database.

**Inputs:**

- One group-verse mapping document per sub-group (produced in Phase 6)

**Routing — one directive per sub-group (default).** Each sub-group gets its own cluster-process directive. This default is the standard pattern for this instruction. Reasons:

1. Phase 6 produces one mapping document per sub-group; the directive boundary follows the document boundary naturally.
2. Failure radius is contained — a problem in M05-C's mapping does not roll back M05-A and M05-B writes.
3. AI can apply incrementally: complete one sub-group end-to-end (mapping → directive → apply → confirmation) before starting the next, which preserves the "discovery as you go" discipline (§2).
4. The administrative cost of N directives is small — each is ~1KB of metadata around a per-sub-group mapping document, and the apply script is the same shape across all sub-groups.

**Combined directive (single per cluster) — not the default.** Permitted only with explicit researcher direction; the trade-off is one transaction frame saved for one cluster-wide rollback exposure.

**Filename:** `wa-cluster-{code}-dir-{seq}-{subgroup}-mapping-v1-{date}.md` (e.g. `wa-cluster-M05-dir-004-A-mapping-v1-{date}.md`)
- Pattern: cluster-process directive per `wa-directive-instruction [current]` §11.4 (worked pattern A)
- Required content per the five-element form:
  - **MOTIVATION** — cite the mapping document and obslog session reference
  - **SCOPE** — sub-group code, term set (Strong's list), tables touched (`verse_context_group` UPDATE/INSERT, `verse_context` UPSERT including dual-assignment second rows, `is_anchor` flag toggles), explicit decision on set-asides ("set-asides not re-evaluated unless the mapping explicitly re-includes them")
  - **OUTCOME REQUIRED** — verse-count expectations per group post-apply, anchor count per group = 1, cross-group dual count, set-aside row count unchanged
  - **COMPLETION CONFIRMATION** — verse-count query per group, anchor-count query, dual-assignment query, set-aside count check, application report saved to `Sessions/Session_Clusters/{code}/WA-{code}-{subgroup}-group-mapping-applied-v1-{date}.md`

**Pre-flight (CC executes before any write):**

- Every verse reference in the mapping doc resolves to a `wa_verse_records` row for the named term
- Every term's mti_term_id is in the cluster and assigned to the named sub-group
- Every existing group_id matches its declared term
- Mapping verse counts match the doc's stated totals

**Halt-on-error before any write** — if pre-flight fails, CC reports and waits.

**Self-check before submitting each directive:** AI confirms in the obslog that all verses have been read, all are assigned to a group or have a set-aside reason, every group has an anchor.

**Cluster status remains** `Analysis - In Progress` through Phase 7.

---

## 11. Phase 8 — Catalogue pass (per-prompt analytical work)

**Purpose:** apply every prompt in the 189-prompt T0–T7 catalogue to each sub-group, producing one finding per (prompt × sub-group) plus cluster-level synthesis findings where the prompt's evidence cuts across sub-groups.

**Inputs (the working set):**

- `wa-cluster-{code}-grouped-v{N}-{date}.md` (latest version reflecting Phase 7 writes) — verses by sub-group, with anchors and per-verse observations
- `wa-obs-catalogue-tiered-v{N}-{date}.md` — the full 189-prompt catalogue (T0–T7). Refresh via `python scripts/build_obs_catalogue_tiered_extract.py` if a newer catalogue version has been seeded.
- The obslog through Phase 7

**Governing instruction (applied throughout all passes):**

> The focus is on describing the intricacies of the characteristic(s), rather than answering a theoretical question. Keep it grounded.

**Outcome codes — definitions:**

Every response to every prompt must carry one outcome code. These codes are not optional labels — they are the primary analytical record.

- **E (Evidenced):** The verse evidence in this sub-group's groups directly and explicitly addresses this prompt. The response must name at least one specific verse or group that evidences the claim. If no verse can be named, the code is not E.
- **S (Silent):** The verse evidence does not address this prompt for this sub-group. This is a finding in itself. A consistent pattern of silence across sub-groups is a cluster-level finding and must be recorded as such — do not write a series of identical negatives; write one cluster-level finding instead.
- **G (Gap):** The question should be answerable but the data needed is not yet available — either a CC database query is required (dimensional sharing counts, root architecture, LXX mapping) or an external resource is needed. G is not the same as S: S means the verses are silent; G means the data to answer may exist but has not been retrieved.

**Fluency guard — the most critical discipline in Phase 8:** Output that reads smoothly and is well-structured can still be entirely ungrounded. The test for every E-coded response is not "does this sound right?" but "which specific verse or group evidences this?" Do not produce E-coded responses from term glosses, group labels, general theological knowledge, or prior cluster findings. If no verse can be named, the outcome code is S or G. Structured, voluminous output can simulate genuine analytical work without performing it — this is the failure mode Phase 8 is most vulnerable to.

**BOUNDARY treatment:** BOUNDARY terms do not receive the full 189-prompt catalogue pass. Produce one structural characterisation note per BOUNDARY term: what role does this term play in the cluster economy? (Delivery mechanism? Quality marker? Behavioural expression?) Record under T1.2.1 (kind of inner-being phenomenon). If the characterisation reveals a term should be re-evaluated as a full sub-group, flag for researcher decision before proceeding.

**Discipline:**

- Every response anchored to a named verse or group.
- No theoretical elaboration beyond what the text shows.
- Silence recorded as silence, not glossed over.
- Each sub-group must have a complete answer for each catalogue prompt before the next sub-group begins.
- All observations rooted in the cluster's data — not from memory, not from AI training, not from extraneous knowledge, not from prior cluster findings.
- The style of the answer must allow Session C to articulate the analysis with only the findings as input.

**Sub-group completion gate:** Before moving from one sub-group to the next, confirm: all 189 prompts have an E, S, or G marker for the completed sub-group. No prompt is left blank. No response is left without a verse citation if coded E. Run the Phase 8 self-check (§16) and confirm it passes. Do not begin the next sub-group until this gate passes. Do not continue elaborating within a completed sub-group — move on.

**Output style — verbatim into the obslog:**

The findings are written by sub-group as they are found — no distraction by fringe observations. For each prompt × sub-group cell:

```
**T{tier}.{component}.{seq}** — {prompt text}

**[A — Hatred]** {finding text — verbatim, with verse anchors}

**[B — Contempt]** {finding text}

…

**[CLUSTER]** {cluster-level synthesis where applicable}
```

Markers used in the source document (and recognised by the loader script):

- `**[X]**` or `**[X — Label]**` → finding for that sub-group
- `**[A, B, C]**` → finding shared across listed sub-groups
- `**[CLUSTER]**` or `**[CLUSTER — all sub-groups]**` → cluster-level synthesis
- `**S — [scope]**` → silent for that scope
- `**G — [scope]**` or `**G**` → gap requiring CC database query

**Output document:** consolidated findings, structured into parts by tier:

- `Sessions/Session_Clusters/{code}/WA-{code}-consolidated-findings-v1-{date}-part1.md` (T0–T1)
- `…-part2-T2.md`, `…-part3-T3-T4.md`, `…-part4-T5-T7.md`

This split mirrors the M06 precedent and keeps each part to a manageable size.

**Phase 8 produces no DB writes.** The consolidated findings document is the analytical artefact; database application happens in Phase 9.

---

## 12. Phase 9 — Findings recording (validation + DB write)

**Purpose:** validate that every prompt has been applied to every sub-group with grounded evidence, then record the findings in `cluster_finding`.

**Inputs:**

- The four parts of the consolidated findings document (Phase 8 output)
- The obslog through Phase 8
- Any prior session findings (`wa_session_research_flags` rows) attached to terms in this cluster — see §12.1 for handling.

### 12.1 Legacy registry-era findings — `wa_session_research_flags`

The registry-era Q&A findings system (`wa_session_research_flags` rows with `flag_code` in `PH2_*`, `SB_FINDING`, `SB_DIMENSION`, `SD_POINTER`, etc.) **remains in place**. It is not deprecated, not retired, and not migrated. The cluster-level findings system (`cluster_finding`) is a new layer alongside it, not a replacement.

**Why both exist:**

- `wa_session_research_flags` is **registry-scope**: each row is anchored to a specific word's analytical session (Session B/D for that word). Many rows pre-date the cluster system.
- `cluster_finding` is **cluster + sub-group + catalogue-prompt scope**: each row answers a specific catalogue prompt for a specific sub-group of a specific cluster.
- Neither subsumes the other. A registry finding for "love (R103)" answers "what does the verse evidence say about *this word*?" A cluster finding for M05/M06/etc. answers "what does the verse evidence say about *this characteristic* in response to *this catalogue prompt*?"

**Per-cluster handling during Session B work:**

1. **Phase 1 (comprehension)** — when reading the cluster dataset, registry-era findings attached to any term in the cluster are visible in the comprehensive report. Read them as background context.
2. **Phase 4 (control read)** — registry findings may surface relevant cross-references (e.g. love's R103 finding noting hate as a structural opposite). Cite them in the obslog where they materially inform the cluster's classification.
3. **Phase 5–8 (catalogue passes)** — registry findings are appendix-tier reference. They may be cited as supporting evidence in a cluster-level finding but they do not replace verse-level evidence. Per `feedback_findings_marginal_value` (researcher feedback): registry findings are "registry-scope shotgun; cannot be applied to term-and-verse analysis directly. Use only as directional appendix for cross-cluster claims + shared anchor verses."
4. **Phase 9 (findings recording)** — `wa_session_research_flags` rows are **not modified** by this phase. The findings-record directive (§11.5 of `wa-directive-instruction [current]`) writes only to `cluster_finding`. The directive's Element 5 completion confirmation includes a check that `wa_session_b_findings` row count is unchanged.
5. **Phase 10 (verification)** — confirms the no-write rule. If any registry findings were inadvertently touched (e.g. by a directive's collateral query), it is flagged for repair.

**When a registry finding becomes relevant to a cluster finding:**

- Cite the registry finding in the cluster finding's `finding_text` by `flag_id` or by registry + question_code (e.g. "OBS-103-T2-017").
- Do **not** copy the registry finding's text verbatim — paraphrase with attribution. The cluster finding's text remains grounded in the cluster's verse evidence; the registry finding is supporting context, not the source.
- Optional future linkage: a `cluster_finding_related_flags` junction table could be introduced if cross-pointing becomes frequent. Not required for v1_0; researcher will direct if needed.

**Hard rules during Session B cluster work:**

- ❌ Do not modify any `wa_session_research_flags` row.
- ❌ Do not insert new `wa_session_research_flags` rows. New analytical claims at cluster scope go to `cluster_finding`. New analytical claims at registry scope are out of scope for this instruction.
- ❌ Do not retire / soft-delete registry findings. They remain accessible.
- ✓ Do read them as context.
- ✓ Do cite them by id in cluster findings where they materially support a cluster claim.

**Consolidated findings document — format requirement:** The consolidated findings document (parts 1–4) must be self-contained and readable without reference to any other file. This means:

- Every prompt answered with the full finding text per sub-group — not a structural label, not a cross-reference to another section, not a summary of what the finding addresses.
- Every E-coded response includes the specific verse reference(s) that ground it, in the body of the response text.
- The reader of the consolidated findings document should be able to write a Session C report using only that document.

This was a specific mid-session correction in M06: the initial consolidation document treated the 189 prompts at the structural level (cluster vs sub-group-specific) rather than answering each one with full text. The correction required producing the full text for all 189 prompts per sub-group. Build to the correct standard from the outset.

**Cross-sub-group review pass (before the directive is produced):**

After all sub-group catalogue passes are complete, read across the full set of findings before producing the directive. This is not a consolidation step and does not produce a new document — it is a review pass whose purpose is to identify findings that are only visible when all sub-group findings are in view simultaneously.

What to look for in this pass:

- **Cluster-level patterns** — a finding that appears in the same form across all or most sub-groups is a cluster-level finding, not seven sub-group findings. Record it as a single `[CLUSTER]` finding in the consolidated findings document at the relevant prompt.
- **Structural relationships between sub-groups** — causal sequences, constitutive relationships, or structural asymmetries (e.g. one sub-group is the receiving-side condition produced by the others) that are not visible within any single sub-group's pass.
- **Absences that become significant in totality** — a prompt that is silent across all sub-groups is a cluster-level finding. A faculty that is never named as primary across any sub-group is a finding about the cluster's character.
- **Internal contradictions** — if two sub-group findings appear to conflict, resolve the conflict by returning to the verse evidence before the directive is produced.

Any findings surfaced in this pass are added to the consolidated findings document at their relevant prompt location before the directive is authored. The directive is then built from the updated consolidated findings document.

**Validation step (before the directive is produced):**

- Every prompt in the catalogue was applied to each sub-group (or BOUNDARY where the cluster has one).
- Every response is grounded in named verse evidence.
- All `S` (silent) and `G` (gap) markers are intentional — silence is itself a finding when pattern is significant.
- The cross-sub-group review pass has been completed and any new cluster-level findings have been added to the consolidated findings document.
- Open questions from prior sessions that are still relevant to this cluster have been validated and either updated or noted in the obslog. Findings not validatable in this cluster's data are noted as such.

**Do not rerun the entire analysis** to prepare the directive — the directive is built from the obslog + updated consolidated findings, not from a new pass.

**DB writes — one directive per cluster:**

- Filename: `wa-cluster-{code}-dir-{seq}-findings-record-v1-{date}.md`
- Pattern: cluster-process directive per `wa-directive-instruction [current]` §11.5 (worked pattern B)
- Required content:
  - **MOTIVATION** — cite the consolidated findings document, the obslog session, the catalogue version (`catalogue_version` from `wa_obs_question_catalogue`)
  - **SCOPE** — table `cluster_finding`; cluster_code; source files (the four parts); operation: UPSERT one row per (prompt × scope), parsing `**T#.#.#**` headers and scope markers
  - **OUTCOME REQUIRED** — one row per source-document marker; `finding_status` per marker type (E→`finding`, S→`silent`, G→`gap`, CLUSTER→`cluster_synthesis`); `finding_text` set to verbatim prose; `source_file` set to the part-N filename; cells the source did not separately address may remain at the structural-loader stub or be omitted
  - **COMPLETION CONFIRMATION** — row counts by status (for cluster_code); 3-row sample; gap list (every `gap` row with prompt code, scope, excerpt); confirmation that `wa_session_b_findings` row count is unchanged for this cluster's terms

**Two-step load is acceptable:**

1. Structural loader — creates one row per (189 prompts × 7 sub-groups + 189 cluster-level rows) with status defaults
2. Full-text loader — parses the consolidated findings document and updates `finding_text` + `finding_status` for every authored marker

The structural loader fills in the cells the source author did not separately address with an explanatory stub (e.g. "Sub-group not separately addressed in source — see cluster-level finding for this prompt"). These stubs stay at status `finding` and are the legitimate "no per-sub-group finding required" marker.

**Cluster status remains** `Analysis - In Progress` through Phase 9.

---

## 13. Phase 10 — Database verification, gap resolution, completion

**Purpose:** verify the database state matches what the analysis declared, resolve any gaps that can be resolved by DB query, and close the cluster.

**Inputs:**

- The post-Phase-9 cluster_finding rows
- A verification report (CC produces; AI reviews)

**Step 1 — CC verification:**

CC runs a verification pass and produces `outputs/markdown/{code}_findings_verification_{date}.txt` (or equivalent) covering:

- Anchor verse claims — every group's named anchor exists as a `verse_context` row with `is_anchor=1`
- NT verse availability — every NT verse cited in the findings exists in `wa_verse_records` for the cited Strong's
- Group code references — every `group_code` cited in the findings exists with the expected `mti_term_id`
- Coverage summary — counts per status per scope; expected vs actual

CC raises flags for any mismatches.

**Step 2 — AI response (validation response document):**

For each flag, AI authors a verification-response document: `Sessions/Session_Clusters/{code}/WA-{code}-verification-response-v1-{date}.md` — covering:

- What the verification confirmed
- What the verification did not check (e.g., groups for sub-groups not in the original parser list)
- Each flag's analysis and the required action (DB repair, analytical correction, or "no change — verification artefact")

**Step 3 — Gap resolution:**

Gap rows (`finding_status='gap'`) are reviewed:

- Gaps resolvable by DB query (e.g. root-family architecture, dimensional sharing, LXX mapping, NT coinage check) — CC runs the queries and AI updates the gap rows to `finding` status with the resolved text
- Gaps requiring external data (e.g. external concordance work) — remain as `gap` with explanatory text marking the dependency

**Step 4 — Final corrections directive:**

- Filename: `wa-cluster-{code}-dir-{seq}-verification-corrections-v1-{date}.md`
- Pattern: cluster-process directive per `wa-directive-instruction [current]` §11.6 / §11.5 (lite)
- Required content:
  - **MOTIVATION** — cite the verification report and AI's verification-response
  - **SCOPE** — list of (prompt × scope) cells to update, BOUNDARY characterisations to insert, anchor flags to repair, etc.
  - **OUTCOME REQUIRED** — exact post-state per cell
  - **COMPLETION CONFIRMATION** — final remaining-gap count, BOUNDARY findings count, cluster-level findings count, sample rows

**Step 5 — Cluster closure:**

After CC confirms the corrections directive and verification reports clean:

- AI authors a one-line directive (or includes the status update in the corrections directive's Outcome) — `UPDATE cluster SET status='Analysis Completed', last_updated_date=? WHERE cluster_code=?`
- Researcher confirms before the status flip is recorded.

**Cluster status transition:** `Analysis - In Progress` → `Analysis Completed`.

The cluster is now ready for Session C consumption.

---

## 14. Reports — input/output map

The cluster reports produced by the analytics scripts in `scripts/`. All read-only, all re-runnable. Use the file naming convention `wa-cluster-{code}-{kind}-v{N}-{date}.md`; version auto-bumps per the script's `next_version` helper when re-run.

| Report | Script | Used in phases | Purpose |
|---|---|---|---|
| Cluster overview | `_generate_cluster_term_report_v1_*.py` | 1, 3 | Index across all 47 clusters; per-cluster term counts and dimension/finding/pointer aggregates |
| Per-cluster detail | `_generate_cluster_term_report_v1_*.py` | 1, 3, 5 | Compact per-term sheet for one cluster: identity, gloss, occurrences, dimensions |
| Comprehensive cluster | `_generate_cluster_comprehensive_v1_*.py` | 1, 2, 3, 4 | Full per-term + verses + groups + findings + pointers; verses by sub-group (post-apply). Phase 3 reads §1 (cluster summary, gloss list) and §3 (per-term detail with root family + related words). |
| Grouped cluster (v1 / v2) | `_generate_cluster_grouped_v1_*.py` | 5, 6, 8 | Cluster → sub-group → group → anchor + others. v2 adds sub-group statistics columns and per-term lexical context (root family + related words). Use v2 layout from Phase 5 onward. |
| Findings | `_generate_cluster_findings_report_v1_*.py` | 9, 10 | One section per sub-group, organised tier → component → prompt; status counts; gap list |
| Tiered prompts catalogue | `build_obs_catalogue_tiered_extract.py` | 8 | The 189-prompt T0–T7 working source for the catalogue pass |

**Report regen rule:** at the start of each phase that consumes a report, regenerate the report from the current DB state. Reports are snapshots — stale reports invite reasoning on outdated assumptions, which the operating principle (§2) prohibits.

---

## 15. Patches and directives — content checklist

This instruction never authorises CC to write to the database directly. Every DB change is mediated by a patch (`wa-patch-instruction [current]`) or a directive (`wa-directive-instruction [current]`).

**Patch vs directive routing for cluster work:**

| Operation | Method | Reason |
|---|---|---|
| Verse status update (UT → confirmed/borderline/set-aside) | **Patch (VCREVISE)** | Standard VC-family path; AI runs an ID-resolver query before authoring (see §5) |
| `cluster_subgroup` create + `mti_terms.cluster_subgroup_id` assign | Directive (§11.4) | Cluster-process — schema relationships span tables |
| Cluster reassignment (term moves between clusters) | Directive (§11.6) | Requires cleanup of orphan sub-group references |
| Group-verse mapping apply (`verse_context_group` + `verse_context` writes) | Directive (§11.4) | Source is structured markdown the parser must interpret |
| Cluster findings recording (`cluster_finding`) | Directive (§11.5) | Two-step structural+full-text load via parser |
| Schema enablement for cluster tables | Directive (§10) | DDL — applicator does not do DDL |
| Verse-context status corrections at scale (registry-style) | Patch (VERSECONTEXT family) | Field names and IDs known in advance |
| Word-registry / mti_terms metadata corrections | Patch | Standard data-write |

**Directive content — common requirements (per `wa-directive-instruction [current]` §3 + §11.3):**

Every cluster-process directive **must** specify:

1. **DIRECTIVE ID** in format `DIR-YYYYMMDD-NNN`
2. **MOTIVATION** — cite the source document(s), obslog session reference, the analytical pass that produced the artefact
3. **SCOPE** — cluster_code; sub-group code (if applicable); tables touched; selection criteria; explicit handling of set-asides ("not re-evaluated unless explicitly re-included")
4. **OUTCOME REQUIRED** — exact row counts per group/sub-group, anchor counts, status distribution, untouched-table check (e.g. `wa_session_b_findings` row count unchanged)
5. **COMPLETION CONFIRMATION** — queries CC must run + expected results

The directive's **filename** uses the cluster pattern (`wa-directive-instruction [current]` §2.3): `wa-cluster-{code}-dir-{seq}-{description}-v{n}-{YYYYMMDD}.md`. Sequence numbers reset per cluster.

**Directive companion files — per phase:**

| Phase | Directive description suffix | Companion source document |
|---|---|---|
| 2 | _(patch — VCREVISE; not a directive)_ | `WA-{code}-UT-verse-review-v1-{date}.md` (patch description references this) |
| 4 | `subgroup-assign` (and optional `term-rebind`) | `WA-{code}-characteristic-debate-v1-{date}.md` |
| 7 | `{subgroup}-mapping` | `WA-{code}-{subgroup}-group-verse-mapping-v1-{date}.md` |
| 9 | `findings-record` | `WA-{code}-consolidated-findings-v1-{date}-part{N}.md` (×4 parts) |
| 10 | `verification-corrections` | `WA-{code}-verification-response-v1-{date}.md` |

Each directive references its companion document(s) explicitly in the Motivation. CC parses the companion document(s) at execution time.

**Patches — when used:**

Verse-status patches in Phase 2 (if patch route is preferred over directive) follow `wa-patch-instruction [current]` §3 with `patch_type = "VCREVISE"` or the appropriate VC-family type. The `_patch_meta` block must include `terms_covered` and `input_versions` for every term touched (per patch instruction §15.6.4-bis). Pre-cluster patches (term metadata, registry status) are unchanged from the registry-era patch instruction.

---

## 16. Self-checks per phase

| Phase | AI self-check before submission |
|---|---|
| 2 | Every UT verse has a recorded determination; counts add up to total UT count |
| 3 | Every term is in a sub-group, BOUNDARY, or flagged for cluster reassignment; sub-groupings are explicitly provisional; every proposed sub-group has been tested against the five T1 criteria in §6 |
| 4 | Every open question (OQ-NNN) has a researcher-confirmed resolution; no OQ items remain open before the directive is authored |
| 5 | One summary per sub-group; each summary names verse anchors; grouped report was regenerated from current DB state before Phase 5 began |
| 6 | Every non-set-aside verse is assigned to a group; every group has an anchor; any existing conglomerate groups have been reviewed for splitting |
| 8 | Every prompt × sub-group cell has a finding, silent, or gap marker; every E-coded response names at least one specific verse; every consistent cross-sub-group silence pattern has been recorded as a cluster-level finding; BOUNDARY has structural characterisation notes (not a full pass); sub-group completion gate passed for each sub-group before moving to the next |
| 9 | Cross-sub-group review pass completed; any cluster-level findings added to consolidated findings document; validation step complete; every gap has CC-query path or external-dependency note; consolidated findings document is self-contained (full text per prompt per sub-group, verse citations in body) |
| 10 | All verification flags addressed; groups used in analytical passes are confirmed in database; cluster-status flip authorised |

**Silence-as-finding rule:** A consistent pattern of S (silent) across all or most sub-groups for a given prompt is not a non-result — it is a positive finding about the cluster's character. Record it as a cluster-level finding in the consolidated findings document. Example: if the spirit-level location is silent for every sub-group in this cluster, the finding is "the spirit level is silent across the entire cluster" — not seven separate S markers with no cluster-level note.

A failed self-check **stops the phase**. The work is not handed to CC until the self-check passes.

---

## 17. Status discipline

Per the Session Startup Rule and `wa-claudecode-instruction [current]`, AI never tells CC the cluster is "complete" — completion is set by the researcher, on review of CC's confirmation outputs. AI's role is to deliver a directive whose Completion Confirmation queries demonstrate the outcome required.

CC's role is to execute the directive faithfully and return the confirmation. CC does not extend scope, interpret ambiguity, or apply analytical judgement (per `wa-directive-instruction [current]` §8.4).

---

## 18. Change history

**v1_2 (2026-05-13) — Active, authoritative.** Refinements derived from M05/M06/M15/M26 completed runs. §4 — removed `wa-cluster-overview-v{N}-{date}.md` from Phase 1 inputs (cluster context is contained in the comprehensive report; the overview is a programme-wide artefact, not a cluster-input). §6 — T1 framework definition pulled out as a visible callout block so it cannot be missed; inputs reframed to reference sections of the comprehensive report rather than introducing additional report files (gloss list and root-family info are already in the comprehensive report's §1 and §3). Status changed from DRAFT to Active.

**v1_1 (2026-05-07) — DRAFT.** Additions and clarifications derived from the M06 first-run. No existing content removed. Changes: (1) §2 — write-on-discovery consequence, cross-cluster contamination guard, and fluency-is-not-quality-signal added; (2) §6 Phase 3 — provisional-by-definition guard added; (3) §7 Phase 4 — open-question discipline (OQ-NNN must be resolved before directive is authored) added; (4) §8 Phase 5 — phase-start report requirement cross-reference added; (5) §9 Phase 6 — conglomerate-group split instruction added; (6) §11 Phase 8 — outcome codes defined, BOUNDARY treatment clarified, fluency guard added, sub-group completion gate added, silence-as-finding instruction added, finding-text standard stated; (7) §12 Phase 9 — cross-sub-group review pass added (replaces consolidation step; surfaces cluster-level findings visible only across all sub-group passes); consolidated-findings format requirement stated; (8) §16 Self-checks — updated for all phase additions.

**v1_0 (2026-05-07) — DRAFT.** First issue. Three of the original five open items resolved on issue: Phase 7 default = per-sub-group directive (§10); Phase 2 default = VCREVISE patch with AI-resolved IDs (§5); legacy `wa_session_research_flags` retained as appendix-tier with explicit handling rules (§12.1).

---

*wa-sessionb-cluster-instruction-v1_2-20260513 | Active — authoritative instruction for Session B analytics*
*Replaces (on finalisation): wa-sessionb-analysis-readiness, wa-sessionb-analysis-output, wa-dimensionreview-instruction, wa-versecontext-instruction, wa-registry-management-guide*
*Cross-references: wa-directive-instruction [current] §11 (cluster-process directives), §10 (schema enablement); wa-patch-instruction [current] §3 (patch types), §15 (input version gate); wa-sessionc-cluster-overview [current] (downstream Session C cluster publication process)*
