# `wa_rule_registry` full review — what is still outstanding

> Escalation #689 (governance-alignment register #4): "review the entire related document and
> confirm what is still outstanding" — the related document is `source_document` on GR-LOAD-001/
> GR-OBS-001: `wa-global-general-rules-v2_11-20260418.json`, whose current compiled form is
> [`Workflow/Global_rules/wa-global-rules-all-v2-20260427.md`](../../Workflow/Global_rules/wa-global-rules-all-v2-20260427.md)
> (34 active rules, 12 categories). Confirmed live 2026-08-17: the DB's active count/category
> breakdown is byte-for-byte identical to the 2026-04-27 snapshot — **no row in `wa_rule_registry`
> has been touched since**, despite four major pivots since then (2026-06-25 reset, 2026-07-02
> verse-first, 2026-08-03 closure, 2026-08-15 IBA architecture correction). Every rule read in full
> before this table was built — not sampled.
>
> **Extended for escalation #690** (governance-alignment register #5 — "cross-referenced against
> `iba/app/GOVERNANCE.md`'s live `cfg_*` rules"): §"Cross-reference against live `governance.*`
> settings" below pulls all 30 active `governance.*` rows from `cfg_setting` and matches each one
> against the 34-rule table above — the specific ask #689's review didn't itself cover.

## Method

Each rule assessed against: (a) does its underlying MECHANISM still exist in Claude Code's actual
operating environment (vs. the old chat-based "Claude AI" role's sandbox — Project Files,
`present_files`, download-at-pass-close, in-chat obslog)? (b) does its PRINCIPLE still hold,
independent of mechanism? (c) is it already independently re-stated somewhere live (CLAUDE.md,
`iba/app/GOVERNANCE.md`, memory)? Verdict is a recommendation, not a decision — none of these are
applied; this is the evidence base for your call.

## `session_startup` (2) — the rules that triggered this review

| Rule | Verdict | Why |
|---|---|---|
| GR-LOAD-001 | **Obsolete** | Three-step chat confirmation ("Global rules loaded…", "Cadence discipline active…") has no Claude Code equivalent — CLAUDE.md §9 + this skill's own start-project procedure already govern session start differently. |
| GR-OBS-001 | **Obsolete** | Per-turn obslog file (`wa-obslog-*.md`, written before every chat response) has no Claude Code equivalent — memory + `outputs/session-logs/`/`Logs/` session logs + git commits serve this role now, on a different cadence (session-close, not per-turn). |

## `cadence_discipline` (1)

| Rule | Verdict | Why |
|---|---|---|
| GR-CAD-001 | **Obsolete (mechanism); principle already live elsewhere** | `present_files` is a Claude.ai-sandbox tool that doesn't exist in Claude Code. The underlying idea (show what was written, every turn) is already how this session actually operates — write, then state the file path/what changed — just not via this rule. |

## `data_discipline` (5) — technical DB rules, mostly tied to the retired Session B pipeline

| Rule | Verdict | Why |
|---|---|---|
| GR-DATA-001 (`mti_terms` active filter) | **Keep, relocate** | Still a real, technical, timeless filter if `mti_terms.status` still means what it says — worth confirming against current schema, but not obviously stale. Belongs in a live technical-reference doc, not a "Claude AI" rule. |
| GR-DATA-002 (extract authoritative for Session B) | **Obsolete** | Names "Session B" by name — CLAUDE.md's own banners mark the Session B/C/D pipeline as legacy substrate under the current method. |
| GR-DATA-003 (`mti_term_flags` for somatic classification) | **Needs a live-schema check, not a guess** | Technical field-authority rule — still correct only if `mti_term_flags`/`wa_term_inventory.somatic_link` are both still populated fields; not verified here. |
| GR-DATA-004 (confirm export version at session start) | **Obsolete** | "Complete word data export" is Session B-specific; no such per-session confirmation step exists in current practice. |
| GR-DATA-005 (`god_as_subject`/`somatic_link` verify-before-set) | **Obsolete (as a session-startup rule); principle sound** | Session B-specific fields/workflow; the underlying "verify against verse evidence before setting a field with a known high error rate" principle is generic and still good practice. |

## `database_discipline` (1)

| Rule | Verdict | Why |
|---|---|---|
| GR-DB-001 (never assume DB state, always verify) | **Keep — still fully live** | Matches exactly how this session operates and matches memory `feedback_verify_db_claims_via_visible_tooling`. Should be re-anchored to a live document (CLAUDE.md or GOVERNANCE.md), not left stranded in an unrevised DB table addressing "Claude AI." |

## `document_discipline` (2)

| Rule | Verdict | Why |
|---|---|---|
| GR-REF-001 (single-authority content referencing) | **Keep — still live** | General documentation-governance principle, matches this whole governance-alignment register's own methodology. |
| GR-REF-002 (`[current]` token convention) | **Keep — actively cited today** | CLAUDE.md §10 names GR-REF-002 by number as the live convention governing all `Workflow/Instructions/` cross-references. This one rule is demonstrably still in force, unlike the other 33. |

## `file_format` (1)

| Rule | Verdict | Why |
|---|---|---|
| GR-FILE-005 (JSON/markdown/docx-on-request) | **Keep — still broadly true** | Matches current practice (this session writes `.md` for structured output). |

## `file_naming` (6) — **contains a real, live conflict, not just staleness**

| Rule | Verdict | Why |
|---|---|---|
| GR-FILE-001 (`[prefix]-[reference]-[short desc]-[version]-[date]`) | **Partially stale** | Still broadly the shape `docs/file-organisation-rules.md` follows for the main project; needs reconciling with that doc (itself flagged, register item #2), not just left in the DB. |
| GR-FILE-002 (30-char short description) | Unverified | Narrow mechanical constraint, not checked against current practice. |
| GR-FILE-003 (version format `v[major]_[minor]`, e.g. `v2_7`) | **CONFLICTS with current live rule** | CLAUDE.md §9.4 (2026-07-23, reinforced by git history) uses a **different, simpler convention**: same-name-file version bump = integer suffix `-v{n}` (`v2`, `v3`, no leading zero, no minor component) — not `v[major]_[minor]`. These are two different, incompatible schemes both currently "active" in their respective documents. This is a genuine, current conflict, not stale-but-harmless. |
| GR-FILE-006 (prefix/reference conventions incl. `wa-c17`, `wa-sd`) | **Obsolete (examples)** | References cluster/Session-D reference codes from the retired model; the general "wa- prefix, reference segment" shape may still hold, examples don't. |
| GR-FILE-007 (lowercase filenames) | **Keep — still true** | Matches observed practice. |
| GR-FILE-009 (compact `YYYYMMDD` in filenames) | **Keep — still true, and matches IBA's own convention** | `iba/app/reports/` naming (`{topic}-{YYYYMMDD}.md`) uses the same compact form. |

## `file_output` (1)

| Rule | Verdict | Why |
|---|---|---|
| GR-FILE-008 (dual-write to working dir + `/mnt/user-data/outputs/`) | **Obsolete — environment-specific** | `/mnt/user-data/outputs/` is the old Claude.ai sandbox path. Claude Code writes directly to the real project filesystem; there is no second "outputs" mount to dual-write to. |

## `pass_close` (1)

| Rule | Verdict | Why |
|---|---|---|
| GR-PASS-001 (download outputs before next pass) | **Obsolete — environment-specific** | "Download" was the old chat UI's file-delivery mechanism. Files are already on disk in the real project; nothing to download. |

## `process_discipline` (5)

| Rule | Verdict | Why |
|---|---|---|
| GR-HF-001 (help-forward restraint) | **Keep — principle still live** | Matches memory `feedback_deliberately_sparse_instructions_to_probe_defaults` and CLAUDE.md's cost-awareness framing, though written for "Claude AI" specifically. |
| GR-PROC-001 (step completion requires validated output) | **Keep — still live** | Matches memory `feedback_verify_before_reporting_fixed`/`feedback_close_the_loop_not_just_investigate_and_report`. |
| GR-PROC-002 (findings rooted in data, hypothesis vs. finding) | **Partially stale** | The `finding` table/hypothesis-vs-finding distinction belongs to the pre-reset lexical model; the underlying epistemic principle (don't present unsupported claims as confirmed) is generic and still right. |
| GR-PROC-004 (no patch/directive applied without researcher review) | **Keep — principle live, mechanism split** | For `bible_research.db`'s patch pipeline (CLAUDE.md §8, still current) this still applies directly. For IBA, the same principle is independently and more strongly enforced via `governance.config_changes_require_researcher_approval`/the escalation system — this rule and IBA's own governance now say the same thing through two different, disconnected mechanisms. |
| GR-TEMPO-001 (obslog write precedes chat response) | **Obsolete — mechanism-dependent on GR-OBS-001** | Falls with GR-OBS-001; no per-turn obslog to write before responding. |

## `programme_orientation` (8) — **the biggest block, and the most methodologically dated**

| Rule | Verdict | Why |
|---|---|---|
| GR-PROG-001 (verse always leads) | **Keep — still a live first principle** | Consistent with every method reset since; the verse-first framing is if anything MORE central under the 2026-07-02 verse-first pivot, not less. |
| GR-PROG-002 (governing question: spirit/soul/body) | **Keep — still the programme's actual question** | Unchanged across every pivot. |
| GR-PROG-003 (dimensions are data-derived) | **Partially stale** | "Dimension" now maps to the VE-lexical D1–D14 items under the current method, not the old dimension-review C-code model this rule was written against; principle (grounded in verse evidence, not imposed) still holds. |
| GR-PROG-004 (Session C primary, Session B deepens) | **Obsolete** | Names the retired Session B/C structure directly. |
| GR-PROG-005 (two-AI division: Claude AI decides, Claude Code executes via patch/directive only) | **CONFLICTS with actual current operation** | This session alone: I made analytical/design judgement calls (the escalation state-machine fix), wrote governance escalations, and edited documentation directly — not "Claude AI decides, Claude Code executes a patch." The two-role split this rule encodes has been effectively dissolved by Claude Code's actual scope of work; CLAUDE.md §1 still describes the two-AI role split in its own text, so this conflict exists at the CLAUDE.md level too, not just in the DB. |
| GR-PROG-006 (characteristic-perspective grouping) | **Obsolete** | Named-closed by the 2026-06-25 "Characteristics → Movements" reset banner in CLAUDE.md itself. |
| GR-PROG-007 (term-level inner-being filter) | **Partially stale** | Written for the old characteristic/VCG model; the term-driven verse-first method (2026-07-02) has its own filter logic in the catalogue/method docs. |
| GR-PROG-009 (inferential vs. confirmed labelling) | **Keep — principle still live** | Generic epistemic discipline, independent of which method version is current. |

## `researcher_decision` (1)

| Rule | Verdict | Why |
|---|---|---|
| GR-RD-007 (obslog = detail, chat = alert) | **Obsolete (mechanism); principle already re-stated live** | `docs/interaction-preferences.md` protocol #2 ("Output & Workings → .md Always... Chat is for alerts and brief summaries only") says the same thing through a different, already-live mechanism (`.md` files, not a per-turn obslog). |

## Cross-reference against live `governance.*` settings (escalation #690)

All 30 active `governance.*` rows pulled from `cfg_setting` (module `governance`, `inactive=0`) and
matched against the 34-rule table above. Most `wa_rule_registry` rows have **no** `governance.*`
counterpart at all — GOVERNANCE.md governs IBA's own process/config discipline, not research
content or the old chat-role's session mechanics, so this is expected, not a gap. Six real matches
found:

| `wa_rule_registry` rule | `governance.*` setting | Relationship |
|---|---|---|
| GR-PROC-004 (no patch/directive without researcher review) | `governance.config_control`, `governance.rules_must_be_config_driven`, `governance.escalation.scope` | **Duplicated, and now enforced more strongly.** Same principle, but IBA's version is a live, mechanically-gated escalation workflow (propose→validate→escalate→apply) rather than a text rule trusted to be followed. |
| GR-DB-001 (never assume DB state, always verify) | `governance.past_precedent_investigation_signals_missing_config` | **Related, not identical.** Same "verify, don't assume" spirit; IBA's version is narrower — specifically about config/precedent investigation signalling a missing `cfg_step`, not DB state generally. GR-DB-001's broader scope isn't fully subsumed. |
| GR-PROC-001 (step completion requires validated output) | `governance.reports_must_persist` | **Direct functional supersession, for the report-producing case.** IBA's version is mechanically checked (`lib/cfgquality.find_missing_report_paths`, run inside `configmaint.validate`) — not just documented. |
| GR-FILE-001/003/009 (universal filename/version structure) | `governance.oneoff_report_naming_pattern`, `governance.session_log_dir` | **Structural difference, not a clean duplicate.** IBA doesn't have one universal naming rule — it has a narrow `cfg_setting` per artifact type (reports, session logs each named separately). The old rules' universal ambition isn't matched by an equally universal IBA equivalent. |
| **GR-PROG-005** (two-AI split: Claude AI decides, Claude Code only executes patches) | **`governance.primary_responsibility`** | **DIRECT CONFLICT, confirmed.** IBA's setting: "Claude is responsible for the coding of, and maintenance of the integrity to ensure that all project operations are coded, controlled and maintained in the IBA application. This includes back-filling operations currently outside the application." That is a materially broader mandate (decide AND build AND maintain) than GR-PROG-005 grants Claude Code (execute a patch someone else decided on). This is the same conflict flagged in the main table, now confirmed against the actual `cfg_setting` text, not inferred. |
| GR-DATA-002/004 + GR-PROG-004 (Session A/B/C/D framing) | `governance.programme_stages` | **Renamed successor.** IBA's three-stage model (`Base_data → Analysis → Publishing`) is the direct, current replacement for the old four-stage Session A/B/C/D framing these rules assume. |

No `governance.*` row addresses GR-LOAD-001, GR-OBS-001, GR-CAD-001, GR-FILE-008, GR-PASS-001,
GR-TEMPO-001, GR-RD-007, GR-HF-001, GR-PROC-002, or the remaining `programme_orientation` content
rules (001/002/003/006/007/009) — consistent with the main table's verdicts for those (either
purely obsolete sandbox mechanics, or research-content rules outside GOVERNANCE.md's process scope
by design).

## Summary count (34 rules, each counted exactly once)

- **Keep as-is (still live, no conflict) — 12:** GR-DB-001, GR-REF-001, GR-REF-002, GR-FILE-005,
  GR-FILE-007, GR-FILE-009, GR-HF-001, GR-PROC-001, GR-PROC-004, GR-PROG-001, GR-PROG-002,
  GR-PROG-009.
- **Obsolete — mechanism from the retired chat-based role, no Claude Code equivalent — 7:**
  GR-LOAD-001, GR-OBS-001, GR-CAD-001, GR-FILE-008, GR-PASS-001, GR-TEMPO-001, GR-RD-007.
- **Obsolete — names the retired Session B/C/dimension-review pipeline directly — 4:** GR-DATA-002,
  GR-DATA-004, GR-PROG-004, GR-PROG-006.
- **Partially stale — principle sound, mechanics/terminology dated — 6:** GR-DATA-005, GR-PROC-002,
  GR-PROG-003, GR-PROG-007, GR-FILE-001, GR-FILE-006.
- **Real, current CONFLICTS (not just staleness) — need an explicit decision, not a bulk sweep — 2:**
  **GR-FILE-003** (version format `v_major_minor` vs. CLAUDE.md §9.4's actual `-v{n}` convention) and
  **GR-PROG-005** (two-AI role split vs. Claude Code's actual current scope of work, which CLAUDE.md
  §1 itself hasn't caught up to either).
- **Unverified against live schema/practice, not yet given a verdict — 3:** GR-DATA-001,
  GR-DATA-003, GR-FILE-002.

12 + 7 + 4 + 6 + 2 + 3 = 34. Every rule accounted for once.

## What's actually outstanding — three separate decisions, not one

1. **The 11 flatly obsolete rules** (7 mechanism-dead + 4 pipeline-named) are safe to mark
   `obsolete=1` in bulk, `superseded_by` pointing at CLAUDE.md §9 / `docs/interaction-preferences.md`
   / the relevant reset banner, once you confirm the bulk approach is right.
2. **The 6 partially-stale rows** need a judgement call each on whether the surviving principle is
   worth re-homing into a live document, or is already adequately covered elsewhere and can retire
   with the rest.
3. **The 2 real conflicts (GR-FILE-003, GR-PROG-005) need a decision, not a sweep** — each pits a
   still-`obsolete=0` DB rule against something CLAUDE.md itself currently asserts. Marking them
   obsolete resolves the conflict in CLAUDE.md's favour; the alternative is deciding CLAUDE.md is
   the one that's actually wrong on one or both points.
4. **The 3 unverified rows** (GR-DATA-001/003, GR-FILE-002) need a quick live-schema/practice check
   before either bucket above claims them — not decided here.

Not fixed here — this is the review the escalation asked for, not the disposition.
