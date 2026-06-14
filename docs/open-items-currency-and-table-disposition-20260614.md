# Open-items currency review + table disposition (2026-06-14)

> Closes open item #7. Two parts: (A) is `wa-programme-open-items.md` still a reliable worklist? (B) recommended disposition for the stale/ambiguous tables. **No irreversible DB change is executed here** — schema changes go via migration + researcher sign-off (operational governance §1). Reversible/documentation parts are done; the rest awaits an explicit go.

---

## Part A — Currency of `wa-programme-open-items.md` (v8, 2026-06-01)

The register is a **living doc, last updated 2026-06-01**. It **predates** the three events that reshaped the programme: the **DB loss (2026-06-03)**, the **foundations reset (2026-06-04)**, and the **L1/L2 verse-read pivot (2026-06-07/09)**. Three currency risks:

1. **"DONE" items from 2026-05-29 → 2026-06-02 are suspect.** The DB was recovered to a **2026-05-28** copy after the 06-03 loss, so DB-writing items the register marks DONE in that window — e.g. **A2** orphan-VCG dissolution (06-01), **M4b** retro-validation (05-31) — may have been **rolled back and not redone**. → re-verify each against the live DB before trusting "DONE".
2. **The publication / generator half is overtaken by the pivot.** §B (publishing edits), §C (cluster-instruction reconciliation), §D (files to archive), §E (section-type retirement), §F1–F14 (generator/ingest scripts), §H/§I (chapter-input coverage gaps) all serve the Session-C chapter-publication flow. The pivot **parked synthesis/distillation and publication** ("be patient — accumulate verse-meaning before distilling"). This whole agenda is **on hold, not current work**.
3. **The cluster-status / BOUNDARY / Analysis-Complete agenda (§A, §G, §M4) is pre-L2.** Clusters are now re-analysed via L2 verse-read; "Analysis Complete" status and BOUNDARY-pending cleanup are re-framed by that pivot. In particular **§A1/§K/§L (SB/SD pointer conversion) is superseded** by the rule that Session B findings resolve through L2 into the universal `finding` (memory: `feedback_session_b_findings_resolved_through_l2`).

**Items still live regardless of the pivot:** OT-DBR-009 (mti_terms dedup); v3_2 instruction finalisation (open item B3); the catalogue refit; science extracts not in DB.

**Recommendation:** the register is **not a reliable current worklist as-is.** Re-validate it against the live DB + the post-06-04 model, mark the overtaken sections superseded, split "still live" from "parked/overtaken", and **re-issue as Doc version 9** with a 2026-06-14 date. Until then, drive current work from the reconstruction (`01`/`04`), not this register.

---

## Part B — Table disposition recommendation

From reconstruction `03` + live forensics. Each row carries a recommendation **and** its reversibility. **Nothing irreversible is executed here.**

| Table(s) | Evidence | Recommendation | Type |
|---|---|---|---|
| **C-code layer** — `wa_dimension_index` (3,509), `wa_dim_review_cluster_log` (6), `word_registry.cluster_assignment` (C01–C22) | dimension review eliminated 2026-05-04; C-codes are still the registry's only cluster pointer | **KEEP as a legacy index — do not drop.** Marked legacy in docs (done). Retire only when an M-code pointer replaces `cluster_assignment` on `word_registry`. | reversible (doc) — ✅ done |
| `wa_session_b_findings` (2,883), `wa_finding_catalogue_links` (6,199), `wa_finding_entity_links` (287) | old finding model; rule = migrate into the universal `finding` (post-M56) via L2 | **MIGRATE into `finding`** — do not drop, do not freeze. Needs the post-M56 migration design. | needs migration + go |
| `session_d_*` (0 rows ×4) | Session D eliminated in the cluster model | **DROP candidate** (empty). Confirm Session D won't be revived, then a migration drops them. | needs migration + go |
| `sources`, `themes` (0 rows) | empty reference, never populated | **DROP** (or populate if intended). | needs migration + go |
| `prose_section_dimension_link`, `prose_section_finding_link` (0 rows) | never populated; citation model evolved to `finding_citation` | **DROP** after confirming `finding_citation` is the live model. | needs migration + go |
| `wa_prose_section_citations` (562, last write 04-28) | superseded by `finding_citation` (51k, live) | **Retire** once publication resumes on `finding_citation`. | needs migration + go |
| `finding_revision` (0) | M55 audit-trail schema, not yet used | **KEEP** (intended future use). | n/a |
| **Reference-as-DB registries** — `wa_rule_registry`, `wa_addendum_registry` (all 22 obsolete), vocab/pattern registries | created M32–34 as single-source-of-truth; stale since April | **Refresh to current rules/vocab, OR demote from "canonical"** and point back to the instruction docs (a stale SSOT is worse than none). | reversible (refresh) — researcher choice |
| **Catalogue tables** — `wa_obs_question_catalogue`, `finding_question_link`, `wa_finding_catalogue_links` | mid-refactor to the two-layer VE/SYNTH catalogue (not yet in DB) | **HOLD** — they move when the catalogue refit lands. | tied to catalogue refit |

### What this means for action
- **Done now (reversible/doc):** C-code legacy marking; relevancy map (03) updated.
- **Awaiting an explicit go (irreversible / migration):** the DROPs (`session_d_*`, `sources`, `themes`, `prose_section_*_link`), the SB-findings→`finding` migration, `wa_prose_section_citations` retirement.
- **Researcher choice:** refresh vs demote the reference-as-DB tables; resolve the C-code layer's long-term fate.

> These map to the four decisions surfaced for ratification — see the chat summary. I have **not** dropped any table or migrated any data, because those are irreversible scope decisions and the governance routes them through a migration with your sign-off.
