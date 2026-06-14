# Table & Data Relevancy Map — usage / data-consumption view

> Built 2026-06-14 by working **backwards from the latest work** (per researcher direction). Two evidence sources, no inference-as-fact:
> 1. **Forensics** — per-table row count + last-write date (max timestamp column) from the live DB. This is the *data-consumption recency* signal: recently written = live; long-stale = candidate legacy.
> 2. **Documentary supersession** — what the dated written record explicitly says was retired/replaced (cited; see `02-failures-oversights-rework-log-20260614.md`).
>
> **Each table gets an EVIDENCE row and a PROPOSED status.** Where the documents do **not** explicitly settle a table's fate, the status is marked `⚠ PROPOSED — confirm` and is for the researcher to ratify. I supply the evidence; the researcher adjudicates. This is deliberately *not* asserted as final truth — that is the failure mode we are correcting.
>
> Caveat on dates: last-write = newest value in a timestamp column. Tables with **no** timestamp column show `—` (can't be dated this way) and are judged by row count + documentary evidence. A few writes (e.g. June morph-backfill into `wa_verse_records`) may not bump the table's `last_changed`, so treat a stale date on a foundational table as "structure stable," not "unused."

---

## Legend (the five buckets you asked for)

| Bucket | Meaning |
|---|---|
| 🟢 **CURRENT-CORE** | Central to the live L1/L2 + cluster/finding model; written by current work |
| 🟢 **CURRENT-INFRA** | Live engine/logging/control |
| 🔵 **FOUNDATION** | Stable Session-A term/verse data; last written mid-May; **read** constantly, rarely rewritten |
| 🟡 **STALE-RELEVANT** | Superseded model, but data retained/referenced or pending migration — *do not delete* |
| 🟠 **STALE-DEAD** | Legacy of a retired phase; no current reads/writes; candidate for retirement |
| ⚪ **EMPTY/UNUSED** | 0 rows or never used; not relevant |
| 🔮 **FUTURE** | Schema in place, not yet populated (planned) |

---

## A. LIVE — the current model (written June 2026)

| Table | Rows | Last write | Bucket | Evidence / role |
|---|---|---|---|---|
| `finding` | 343,434 | 2026-06-10 | 🟢 CURRENT-CORE | **The live unit.** L2 verse-read store (`l2_api` tier findings + `l2_meaning` paragraphs), universal finding table (M55). |
| `finding_question_link` | 332,184 | 2026-06-10 | 🟢 CURRENT-CORE | Finding → catalogue-question coverage map. |
| `cluster_finding` | 19,996 | 2026-06-11 | 🟢 CURRENT-CORE | Catalogue-prompted cluster-/characteristic-scope findings (most recently written table in the DB). |
| `finding_citation` | 51,148 | 2026-06-03 | 🟢 CURRENT-CORE | Polymorphic citations (verse / Strong's / cross-char) for cluster findings. |
| `finding_verse_link` | 3,586 | 2026-06-09 | 🟢 CURRENT-CORE | Finding → verse_record links (M:N). |
| `cluster` | 49 | 2026-06-10 | 🟢 CURRENT-CORE | Cluster registry (M01–M47 + FLAG + T2); status gates. |
| `mti_terms` | 7,581 | 2026-06-08 | 🟢 CURRENT-CORE | Term master; carries `cluster_code`, `vc_status`. **Has the unresolved OT-DBR-009 duplication (~41 dupes).** |
| `verse_context` | 43,722 | — | 🟢 CURRENT-CORE | Central verse-level record; L1/L2 read+write (relevance, keywords, analysis_note, pole, group_id, triage). No ts column. |
| `verse_context_group` | 4,155 | — | 🟢 CURRENT-CORE | VCG layer (kept in v3_0; ~86% citation-active). No ts column. |
| `characteristic` | 128 | 2026-05-28 | 🟢 CURRENT-CORE | Named inner-being characteristics per cluster (the analytical unit for Phase D). |
| `characteristic_subgroup` | 146 | 2026-05-28 | 🟢 CURRENT-CORE | Characteristic ↔ sub-group M:N. |
| `cluster_subgroup` | 175 | 2026-05-28 | 🟢 CURRENT-CORE | Thematic sub-groups within clusters. |
| `cluster_observation` | 276 | 2026-05-28 | 🟢 CURRENT-CORE | Write-on-discovery cross-phase observations. |
| `vcg_term` | 5,091 | 2026-05-28 | 🟢 CURRENT-CORE | VCG ↔ term M:N (replaced `verse_context_group.mti_term_id`, M45). |
| `mti_term_subgroup` | 1,196 | 2026-05-26 | 🟢 CURRENT-CORE | Term ↔ sub-group M:N (replaced `mti_terms.cluster_subgroup_id`, M44). |
| `wa_session_research_flags` | 704 | 2026-05-18 | 🟢 CURRENT-RELEVANT | Researcher pointers; June reader confirms still **read** (L5 adoption/resolution). ⚠ confirm whether still written. |
| `prose_section` | 249 | 2026-05-27 | 🟢 CURRENT-PARKED | v3_0 publication prose store; **built but publication is parked**. |
| `prose_section_type` | 96 | 2026-05-27 | 🟢 CURRENT-PARKED | Section-type registry for the above. |
| `schema_version` | 13 | 2026-06-10 | 🟢 CURRENT-INFRA | Migration log (→ 3.31.0). |
| `engine_run_log` | 769 | 2026-06-10 | 🟢 CURRENT-INFRA | L2 run audit. |
| `engine_stream_checkpoint` | 1,443 | 2026-06-10 | 🟢 CURRENT-INFRA | L2 resumability checkpoints. |
| `word_run_state` | 438 | — | 🟢 CURRENT-INFRA | Engine per-word state. |
| `word_registry` | 215 | — | 🟢 CURRENT-CORE | Lexical entry point + **C-code dimension anchor** (`cluster_assignment` C01–C22). Coexists with M-code clusters — *scaffolding, not dead*. |

## B. FOUNDATION — Session-A term/verse data (last written 2026-05-14; read constantly)

These are the stable substrate the whole pipeline reads. Last bulk write 2026-05-14 (the term/verse refresh); the June morph-backfill wrote `morph_code`/`stem` into `wa_verse_records` without necessarily bumping `last_changed`.

| Table | Rows | Last write | Bucket | Role |
|---|---|---|---|---|
| `wa_verse_records` | 229,957 | 2026-05-14* | 🔵 FOUNDATION | Span→verse; `span_strong_match` = authoritative usage signal; morph backfilled June. |
| `wa_term_inventory` | 7,560 | 2026-05-14 | 🔵 FOUNDATION | Per-term metadata, glosses, evidential status. |
| `wa_term_related_words` | 101,999 | — | 🔵 FOUNDATION | Related-term glosses (keyword vocab source). |
| `wa_term_root_family` | 2,861 | — | 🔵 FOUNDATION | Root families. |
| `wa_meaning_parsed` | 7,459 | 2026-05-14 | 🔵 FOUNDATION | Structured meaning parse. |
| `wa_meaning_sense` | 16,005 | — | 🔵 FOUNDATION | Sense branches; `stem_label` written at L1. |
| `wa_meaning_stem` | 13 | — | 🔵 FOUNDATION | Stem labels (small). |
| `wa_lsj_parsed` | 9 | 2026-05-14 | 🔵 FOUNDATION | LSJ parse (Greek; sparse). |
| `wa_file_index` | 207 | 2026-05-14 | 🔵 FOUNDATION | Per-file index (registry ↔ file). |
| `wa_verse_term_links` | 226,791 | 2026-04-13 | 🔵 FOUNDATION | Verse ↔ term + STEP sub-gloss. |
| `term_fetch_log` | 2,377 | 2026-05-14 | 🔵 FOUNDATION | STEP fetch audit. |
| `mti_term_cross_refs` | 462 | — | 🔵 FOUNDATION | MTI cross-refs. |
| `mti_term_flags` | 1,005 | — | 🔵 FOUNDATION | MTI flags. |
| `books` / `book_code_variants` | 66 / 112 | 2026-03-16 / — | 🔵 FOUNDATION | Static Bible reference. |

## C. STALE-RELEVANT — superseded model, data retained (⚠ do not delete; confirm disposition)

| Table | Rows | Last write | Bucket | Evidence / why retained |
|---|---|---|---|---|
| `wa_session_b_findings` | 2,883 | 2026-05-02 | 🟡 STALE-RELEVANT | Old Session B findings; superseded by `finding`/`l2_api`. Memory rule: **migrate into the universal `finding`** (post-M56), resolve via L2. Don't drop until migrated. |
| `wa_finding_catalogue_links` | 6,199 | 2026-05-02 | 🟡 STALE-RELEVANT | Old finding↔catalogue links (paired with the above). |
| `wa_finding_entity_links` | 287 | 2026-04-28 | 🟡 STALE-RELEVANT | Finding↔entity links; ⚠ no June reads/writes seen — confirm. |
| `wa_dimension_index` | 3,509 | 2026-05-02 | 🟡 STALE-RELEVANT | Dimension review **eliminated 2026-05-04** — but `word_registry.cluster_assignment` still uses C-codes and this is the C-code analytics. Retained reference, not live. ⚠ confirm whether C-code layer is being kept. |
| `wa_dim_review_cluster_log` | 6 | 2026-05-02 | 🟡 STALE-RELEVANT | Dimension-review completion log (same retired phase). |
| `wa_obs_question_catalogue` | 412 | 2026-04-16 | 🟡 STALE-RELEVANT | 189 T-questions; **being refactored** into the two-layer VE/SYNTH catalogue (v2, 2026-06-11; 16 DROP soft-deleted). Live-but-mutating. |
| `wa_finding_catalogue_links` / `wa_flag_type_question_link` | 6,199 / 12 | 2026-05-02 / 2026-04-20 | 🟡 STALE-RELEVANT | Catalogue routing; tied to the refactoring catalogue. |
| `wa_term_phase2_flags` | 1,570 | 2026-04-11 | 🟡 STALE-RELEVANT | Term phase-2 flags; partly legacy. ⚠ confirm. |
| `wa_data_quality_flags` | 19,304 | 2026-03-28 | 🟡 STALE-RELEVANT | Engine quality flags; last written March. ⚠ confirm whether still consulted. |
| `wa_cross_registry_links` | 158 | 2026-03-26 | 🟡 STALE-RELEVANT | Pre-cluster cross-registry links; superseded by cluster co-occurrence. |
| `wa_crosslink_type` | 11 | — | 🟡 STALE-RELEVANT | Reference for the above. |
| `wa_prose_section_citations` | 562 | 2026-04-28 | 🟡 STALE-RELEVANT | Older prose-citation index; superseded by `finding_citation`. ⚠ confirm. |
| `wa_rule_registry` | 59 | 2026-04-17 | 🟡 REFERENCE | Reference-as-DB rules (M32). Governance reference; static. |
| `wa_addendum_registry` | 22 | 2026-04-20 | 🟡 REFERENCE | **All 22 marked obsolete (M35).** Effectively dead-but-retained. |
| `wa_vocab_set` / `wa_vocab_member` | 8 / 39 | — | 🟡 REFERENCE | Controlled vocabularies (M22/M32). Live reference. |
| `wa_patch_type_registry` / `wa_file_name_pattern` / `wa_label_pattern` | 20 / 23 / 11 | 2026-04-24 / — / — | 🟡 REFERENCE | Reference-as-DB pattern registries (M34). |
| `wa_quality_flag_types` / `phase2_flag_types` | 29 / 25 | — | 🟡 REFERENCE | Flag-type reference. |

## D. STALE-DEAD — retired phase, no current use (candidate retirement; confirm)

| Table | Rows | Last write | Bucket | Evidence |
|---|---|---|---|---|
| `wa_session_b_dimensions` | **2** | 2026-03-28 | 🟠 STALE-DEAD | Only 2 rows ever; old Session B dimensional profile, abandoned. |
| `word_registry.vertical_pass_flag` (field) | 0/43,722 set | — | 🟠 STALE-DEAD | Confirmed unused; flagged for retirement (memory). |

## E. EMPTY / UNUSED (not relevant)

| Table | Rows | Bucket | Evidence |
|---|---|---|---|
| `session_d_runs` / `session_d_verse_links` / `session_d_term_links` / `session_d_observations` | 0 / 0 / 0 / 0 | ⚪ EMPTY | **Session D eliminated** in the cluster model; tables empty. Candidate drop after confirmation. |
| `sources` | 0 | ⚪ EMPTY | Zotero sources never populated. |
| `themes` | 0 | ⚪ EMPTY | Unused reference. |
| `prose_section_dimension_link` | 0 | ⚪ EMPTY | Never populated. |
| `prose_section_finding_link` | 0 | ⚪ EMPTY | Never populated. |
| `finding_revision` | 0 | 🔮 FUTURE | Audit-trail schema in place (M55), not yet written. |

---

## How to act on this (proposed, for your ratification)

1. **Nothing in 🟡/🟠/⚪ should be dropped on this map alone.** Each `⚠ confirm` is a question for you, not a verdict. The map's job is to put the evidence in one place.
2. **Highest-value confirmations** (these change how CLAUDE.md and queries should describe the DB):
   - Is the **C-code dimension layer** (`wa_dimension_index`, `word_registry.cluster_assignment`) being *kept* as a parallel index, or retired now that M-code clusters are the model? (Patience's `C08` hangs on this.)
   - Are **`wa_session_b_findings` + `wa_finding_catalogue_links`** to be migrated into `finding` (per the post-M56 rule) or frozen as historical?
   - Can the **`session_d_*`, `sources`, `themes`, `prose_section_*_link`** empties be dropped?
3. **The `finding` table (343k rows) is the live centre of gravity** — any "what's in the DB" description or CLAUDE.md refresh must lead with it, not with `word_registry`.
4. **OT-DBR-009 (`mti_terms` dedup)** sits under the CURRENT-CORE term master — unresolved and affecting ~2,209 verses' findings. It is the one integrity issue inside the live layer.

> Cross-checks: row counts + last-write from live DB forensics (2026-06-14); supersession claims cited in `02-failures-oversights-rework-log-20260614.md`; current read/write usage from the June reader against `wa-cluster-rollup-instruction-v3_2-DRAFT-20260607.md` and `wa-cluster-rollup-design.md`.
