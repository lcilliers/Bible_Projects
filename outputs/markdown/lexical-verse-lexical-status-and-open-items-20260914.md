# Verse-Lexical: Current Status and Open Items

**Generated:** 2026-09-14 · **Scope:** every open (not-yet-signed-off) escalation touching the verse-lexical base layer (Layer 1/Layer 2) and the cluster-reading pipeline that consumes it (subgroup → reading → answer → synthesis). 25 open escalations, grouped below. Recently-resolved items are listed for context only (§4).

This doc exists to bring verse-lexical to a close, per researcher instruction this session. It is a status register, not a design doc — each open item links to its own fuller record (an `iba/docs/*` spec, an `outputs/markdown/*` report, or the escalation itself via `iba/app/ps/Escalation.ps1 -Action History -Id <n>`).

---

## 1. The confirmed pipeline shape (this session)

Researcher direction, verbatim, recorded live on escalation **#1607** (and cross-referenced at **#1691**, **#1682**):

> "layer 1 need to be completed before stage cluster-subgroup, and is part of the input into this stage. layer 2 of the lexical will be part of stage cluster-subgroup where llm need to process the layer 2 lexical as part of the forming of the subgroups. subgroup have the following output capture sub groups, capture sub group membership, and process the catalogue questions into ib_observations for verse-lexical. the stage reading has as inputs by subgroup of the ib_observations for the subgroup, the lexical for all the related verses."

This is not a new idea out of nowhere — it operationalizes #1607 v14's own closing note from the last session ("fold in the lexical process... include the resulting lexical data when data preparation takes place for subgroup reading"), and it directly closes the gap #1607 v14 found live in the M10 prototype: **process a/b/c never passed role/party_kind/is_negator/T-code data to the LLM at all** — only plain verse text + span surface/morph + dictionary meanings. That gap is the same root cause the researcher named for the original study's 2026-08-03 closure ("llm's natural instinct of using the verse text, and effectively ignoring the enriched data that is available happened again").

The confirmed shape, stage by stage:

| Stage | Input | Process | Output |
|---|---|---|---|
| **cluster-subgroup** (process b) | Layer 1 lexical (must be COMPLETE first — hard precondition, not a parallel track) | LLM processes Layer 2 lexical *as part of* forming the subgroups | (1) subgroups captured, (2) subgroup membership captured, (3) catalogue questions processed into `ib_observations` tagged verse-lexical |
| **reading** (process c) | Per subgroup: that subgroup's own `ib_observations` (from process b) **+** the raw Layer 1/2 lexical for every verse the subgroup covers | — | (per #1682/#1691's existing spec, unchanged by this) |

Two things this settles that were open before this session:
- **#1691 v16 item (a)** asked whether `stage` needed a new value for process (b)'s own observations, proposed `subgroup` — now answered: yes, and its scope is specifically the catalogue-question pass, not just incidental findings.
- **Layer 2 is no longer a standalone pre-pass.** #1592/#1594/#1595/#1597/#1606's whole framing (`lexical.enrich` as an independent step producing `verse_lexical_note` rows *before* cluster-reading starts) needs to be read against this — those escalations' open decisions still stand, but the *mechanism* that consumes them is now "inside process b," not "a prior pipeline stage." None of this is built yet — recorded as the target shape for #1690/#1691/#1693 to build against.

---

## 2. Group A — Layer 1 / Layer 2 lexical core (`verse_lexical` / `verse_lexical_note`)

Column design, data quality, and readiness of the base lexical data itself.

| # | State / next | Open item |
|---|---|---|
| **#1560** | raised / review | 3 `cluster_strong` rows (G1135, G2424, H0802) carry bare, unmatchable Strong's codes — judgement call: does each map to *all* its suffixed variants, or was one specific sense intended? |
| **#1589** | raised / review | 6 of 15 `note_type` values (`idiom`, `pronoun_resolution`, `noun_relational`, `noun_severity`, `polarity`, `compound_unit`) have zero operational definition anywhere in `cfg_method_rule` — the LLM is currently judging 40% of the vocabulary on the bare name alone. |
| **#1590** | re-assigned / ready_for_approval | Greek/Hebrew role-tag bug — scale re-confirmed much larger than first found (G0846 'it/s/he' 5,482 occ., H0834A 'which' 5,448 occ., alone outweigh the original 82-row estimate 60x+). Gated on #1592's role-column rewrite decision. |
| **#1591** | re-assigned / ready_for_approval | 192-row `surface` word-alignment defects (0.035% of 544,572 live rows). No heuristic tried so far reproduces the original 192-row set — needs the original query/list, or a fresh call on detection method, before a repair can be proposed. Gated on #1592. |
| **#1592** | re-assigned / review | `verselexical.build` revisit/validate — Layer 1 role redesign. Most rounds closed (morph_code as-is, resolved_sense algorithm confirmed, 96 multi-cluster-code conflicts resolved down to 37 real ones, spun off to #1605, now closed). Role redesign itself still open. |
| **#1594** | re-assigned / ready_for_approval | Verse-lexical enrich validated against the catalogue questions — Window 1→Window 2 handoff gaps traced (`passage.genre`/`passage.lexical_complete_at` both orphaned by the #1451 verse-scoping redesign). Every named catalogue gap now has a sourced answer (Layer 1 vs Layer 2, where the data would come from). |
| **#1595** | re-assigned / ready_for_approval | `verse-lexical.note` structure/completeness — gated on the `noun_relational`/`noun_severity` pairing decision (shared with #1589) and #1593's lexicon-build scope. |
| **#1597** | in-progress / review | `verse_lexical_note.evidence_text` is 100% unpopulated (0/173 live notes) — same finding as #1607's D8. Two options on record, one decision closes both: enforce as required going forward, or formally merge into `value_text` (where practice has already converged). |
| **#1606** | re-assigned / ready_for_approval | 3-leg lexical readiness check (verse→span→strong→cluster). Leg 1/2 now **PASS clean** (Leg 2 closed as a side effect of the #1613 spine remediation). Leg 3 still fails: **111** live strongs with zero cluster allocation, sample dominated by H9xxx grammatical markers — same T2-pool classification work already done by hand for T4/T5/T6/T7/T9/T15; researcher's call on timing. |
| **#1607** | in-progress / review (v15) | Layer 1/2 six-point column-by-column validation. Most D-items (D1 role, D4 pairing, D11 gloss_consistent grain, D12 language, D13 verse_meta) are closed/decided. D2/D3 (resolved_sense source) are on hold pending the revised meaning-distillation method (the 3 parse tables were retired, #1668). **Now also carries this session's confirmed pipeline shape (§1)** as its live open item — the next build target once the sign-off pack (§3) is ready. |
| **#1665** | raised / review | cfg_* coherence advisory: `lexical_code_class` and `party_kind` cfg_enum groups are orphaned — defined but never looked up by name anywhere in code. Advisory only; needs approve (accept as known)/reject (fix)/revise. |

**Dependency note:** #1590 and #1591 are both explicitly gated on #1592's role-column rewrite; #1592 itself is largely closed except the role redesign, which per §1 is now expected to be settled as part of building the subgroup stage (role/T-code data has to reach the LLM correctly there). #1594/#1595/#1597/#1606 are all validation/readiness passes over the *current* Layer 1/2 design — they should be re-checked once the subgroup-stage build lands, not signed off independently of it.

---

## 3. Group B — Cluster-reading pipeline design (subgroup → reading → answer → synthesis)

The downstream pipeline that consumes verse-lexical. Six items form a **sign-off pack** — per researcher instruction, *none* of #1690/#1691/#1692/#1693/#1696/#1697 build until *all six* are signed off together. Of the six, **#1690, #1692, #1693 are already completed** (shown for context in §4); **#1691, #1696, #1697 remain open** below.

| # | State / next | Open item |
|---|---|---|
| **#1526** | on-hold / ready_for_approval | Reading strategy vs. cluster size — anchor-verse-by-`resolved_sense` approach. Evidence filed: all 7 extreme-volume strongs checked collapse to 1–8 distinct senses, dominant sense covering 86.6–100% of occurrences. **On hold at researcher's own instruction** ("I am just going to begin the analytics and see what wash out") — not abandoned, evidence stays on record for resumption. |
| **#1547** | raised / review | "Prototype Window 2 analysis" placeholder (2026-09-07) — superseded in practice by #1682's actual M10 test work; never formally closed or re-pointed. |
| **#1682** | in-progress / review (v19) | Parent thread: verse-meaning-family synthesis read/output process design. Processes (a) assemble, (b) family/subgroup, (c) read, (d) answer, (e) synthesis are all spec'd (`iba/docs/1682-cluster-reading-process-spec-v1-20260911.md`) and M10-tested end to end. Split into the 4+2 component designs below. **Now also carries this session's confirmed pipeline shape (§1).** |
| **#1683** | re-assigned / review | M10's 32 legacy `characteristic` rows vs. Window 2 — decision made: rename 8 tables to `zz_legacy_*` (not hard-delete), including whole-table renames of `finding`/`verse_context` project-wide (458,096 / 55,775 rows). Premise partly changed by the DB fork (the original naming-collision motivation no longer applies to `cluster_subgroup`/`mti_term_subgroup`) — rename is now a disposition/clarity choice, not a technical blocker; not yet executed. |
| **#1691** | in-progress / review (v17) | Design: `ib_observation` table. Naming, columns, write-discipline (edit-in-place for reading/answer, append-only for synthesis) all finalized. Two items still open: (i) whether append-only needs a real enforcement mechanism (currently just convention — single-writer principle via #1693), (ii) the `subgroup`-stage observation shape — **partially answered by §1 this session**, not yet built. |
| **#1694** | raised / review | 37 M-codes (M32, M48–M84) live in `cluster_strong` with real row counts (M55: 72 rows, M72: 54, M73: 51) but no corresponding row in the `cluster` catalogue table. Decision needed: register per `governance.tables`, or is there a reason this range was never catalogued. |
| **#1695** | raised / review | Design: cluster-reading synergy/synthesis stage. **Explicitly deferred** by the researcher until the full build+test through (not including) the synergising stage is complete. |
| **#1696** | in-progress / review | Migrate `wa_obs_question_catalogue` to iba.db. Design fully resolved — inclusion filter (deleted=0 only, 98 live candidate rows), copy-vs-move (move; bible_research.db side marked inactive), scope boundaries all settled; candidate-row CSV filed for review. Part of the sign-off pack — not yet built. |
| **#1697** | in-progress / review | Add `status` + lifecycle enum to `iba.cluster`. 8-value enum and the rollup rule (cluster status = rollup over `cluster_subgroup.status`, except synthesis which gates on cluster status directly) both defined. Part of the sign-off pack — not yet built. |
| **#1698** | in-progress / revise | Synthesis stage is cross-cluster, not cross-family/subgroup as first modeled. `cluster_code` made nullable for stage='synthesis' (agreed) — actual cluster(s) recorded via `ib_node` rows instead. Naming stays 'synthesis' for now. **Still open:** item (ii), #1697's single-cluster `cluster.status='ready_for_synthesis'` precondition doesn't fit a genuinely cross-cluster synthesis run. |
| **#1699** | raised / review | IB Node Web phantom visualization jump-start — fully delivered (100-row phantom dataset, generator script, published interactive artifact, reusable builder script). Deliberately parked pending real `ib_node`/`ib_observation` data; nothing further needed until #1692/#1693 are populated for real. Effectively a completed record awaiting resumption, not an open design question. |

---

## 4. Group C — Answer-stage / catalogue-question quality

Feeds directly into how the "process d" (answer/catalogue-question) work inside the new subgroup-stage design (§1) should behave.

| # | State / next | Open item |
|---|---|---|
| **#1700** | in-progress / review | Answer-stage catalogue questions risk interpretive drift — systematic per-question review against the *old* finding table, question by question. T0/T1/T2/T4/T5/T6 sections done (all substantiated; recurring gap patterns named: source-data-gap placeholder, boundary exemption, off-target-but-substantive, process-note-as-answer). T3 (already independently diagnosed as a categorical failure, corroborating the #1598 faculties-retirement verdict) and T7 remain. |
| **#1701** | in-progress / review | Revisit inner-faculties framing — where do faculties belong now the study models the inner being as a system of operations rather than a set of entities. **Deliberately parked**, researcher's own words: "we will come back to this." Sharper framing recorded (entity-as-subject vs. process-as-subject) but not designed. |
| **#1702** | raised / review | Cluster T-codes vs. answer-stage question coverage — full evaluation of all 14 live T-codes delivered. Key finding: T4/T9's mechanical detection mechanism already exists and is wired to catalogue design intent, but the actual questions it should feed (T4.6.2a/3a) have **zero findings ever** — connected mechanism, unconnected question, cheapest available fix. `role`'s redesign (Group A, #1592) is the real blocker for every T-code beyond the 5 already wired. |

---

## 5. Recently resolved (context only — already signed off)

Not open items; listed so the closed ground isn't re-litigated.

- **#1690** (family/subgroup table design), **#1692** (`ib_node` trace table design), **#1693** (load/reconcile pass design) — all `completed`, approved as part of the same sign-off pack as #1691/#1696/#1697.
- **#1613** — base-data spine ruling + full remediation (verse/span/strong sync). Unblocked #1606 Leg 2 and #1607's D2/D3 gating.
- **#1668 / #1678 / #1679 / #1680** — the 3 `strong_meaning_parsed`/`lsj`/`mounce` parse tables retired; meaning-distillation method under revision (directly affects #1607 D2/D3, still open above).
- **#1681 / #1684 / #1686 / #1687 / #1688 / #1689** — spine-check housekeeping (H1506 FATAL fixed; discoverability section retired from the report).
- **#1598** — reallocation of M/T-code clusters; also the researcher's own verdict that closed the old T3 (Inner Faculties) framing, feeding #1700/#1701 directly.

---

## 6. Suggested closing sequence

Not a decision — a proposed order based on what's actually gating what, for the researcher's call:

1. **Quick, independent decisions** (no design dependency on anything else): #1560 (bare codes), #1589 (6 note_type rules), #1665 (approve/reject the orphaned enums), #1694 (M-code registration), #1699 (acknowledge as complete-for-now).
2. **Close the sign-off pack**: #1691 (2 remaining items), #1696, #1697 — plus #1698 item (ii), which #1697's rule directly depends on. #1690/#1692/#1693 are already through.
3. **Build the subgroup stage** per §1's confirmed shape — this is the one build that closes or re-grounds #1592 (role redesign), #1594/#1595/#1597/#1606 (Layer 1/2 validation — re-check once real data flows through), and answers #1702's "role is the blocker" finding.
4. **#1590/#1591** (role-tag bug, surface defects) — fix once #1592's role redesign lands from step 3.
5. **#1526** (anchor-verse reading strategy) — independent of the above; resume whenever the researcher wants to revisit reading pacing.
6. **#1700/#1701/#1702** — finish T3/T7 review under #1700, then feed all three into the answer-stage (process d) design once it's built inside the new subgroup-stage shape.

---

*Full history for any item: `iba/app/ps/Escalation.ps1 -Action History -Id <n>`. This doc's own record: cross-referenced at escalations #1607, #1691, #1682.*
