# Catalogue outstanding-work harvest (v1)

**Filename:** 1444-catalogue-outstanding-work-harvest-v1-20260904.md
**Escalation:** #1444, spawned from #1007 (its closing resolution is the direct ancestor of #1383's
whole thread; #1383 does not cover all outstanding catalogue work)
**Task, verbatim:** harvest the actual refinement work on the catalogue that is still outstanding
from all the previous escalations, for review, to determine if there is more, or get a handle on
the updates related to catalogue.

**Method:** full-text search across `escalation` + `escalation_history` (every version's
comment/context/resolution/tried/short_description) for genuine mentions of
`wa_obs_question_catalogue`/`obs_catalogue`/"question catalogue" — not a bare substring match on
"catalogue" alone, which also hits unrelated tables (`wa_finding_catalogue_links`,
`wa_flag_type_question_link` migration work has its own "catalogue" in the name but is a distinct
table). Every genuine hit's **current live DB state** was then checked directly, not taken on the
escalation record's own word — per `verify-before-acting`/`feedback_verify_before_reporting_fixed`.

---

## 1. Every escalation genuinely about the catalogue, and its real current state

| Escalation | What it did | Recorded state | **Live-state check, this pass** |
|---|---|---|---|
| **#1007** | Origin. Identified "the catalogue" = `wa_obs_question_catalogue` + 4 linked tables (`cluster_finding`, `finding_question_link`, `wa_finding_catalogue_links`, `wa_flag_type_question_link`); built the `obs_catalogue.update`/`report.obs_catalogue` tools. **Its own closing resolution explicitly did NOT resolve** the deeper structural problem (Phase-1/Phase-2 question-window mismatch; no mechanism marking which words are IB-related) — named as the starting point for the next design pass. | closed | Confirmed still the right characterisation — #1378/#1379/#1383 are that "next design pass," in progress |
| #1368–#1372 | Bugs found *testing* the `obs_catalogue.update` tool (bad column, unknown `obs_id`, `database is locked` ×2) | completed | All genuine test-of-validation results, not defects (per their own resolutions) — confirmed nothing left open |
| **#1374** | Propose repurposing `scope` column's `use` text to the "Scope-focus" classification | withdraw | superseded by #1375's cleaner version — correct, no orphaned proposal |
| **#1375** | Apply the Scope-focus classification to `cfg_column.use` for `wa_obs_question_catalogue.scope` | completed | **Confirmed live, byte-for-byte**: the 8 real buckets (Word/term (lexical) / Characteristic (HIB behaviour) / Characteristic relational / The HIB / Verse-context / Other non-human beings / The verse / Science) are exactly what's in `cfg_column.use` today, for the 126 T-coded rows. `universal`/`leviticus` values are still present on the untiered rows — explicitly judged "no real value" by the researcher at the time, not a live defect. |
| **#1018** | Propose `wa_flag_type_question_link` → `cfg_table.inactive=1` (12 rows, all pointing at redundant/deleted catalogue questions) | **completed / approved** | **DRIFT FOUND, this pass**: live `cfg_table` row for `wa_flag_type_question_link` still shows `inactive=0` and the *original* use text ("Maps quality-flag types to the catalogue questions... Tiny and static: twelve rows...") — **not** the redundancy-finding text v2's own resolution said would be written. The escalation's own v2 comment even named the exact apply command (`Config-Maintenance.ps1 Propose -RunId RUN-20260829_053227_151-CONFIGMAINT`) — nothing in the live config shows that run's effect ever landed. Marked `completed`/`approved` without the underlying config change actually being present. |
| #1052 | Coherence error: `cfg_report_csv_table` (`report.obs_catalogue`) named `wa_obs_question_catalogue` as "not a known data or cfg_* table" | completed | `report.obs_catalogue` (`cfg_step`) is live and correctly scoped today — the coherence error itself is gone |
| #1055/#1056 | `report.obs_catalogue_path` found stale/hardcoded; researcher ruling: no hardcoded literals | completed | Confirmed live: `cfg_setting report.obs_catalogue_path = "Workflow/Catalogue/obs-catalogue.md"`, correctly config-driven, not hardcoded |
| #1020/#1021/#1024–#1037 | Migrate `wa_finding_catalogue_links`/`cluster_finding` content into `finding`/`finding_question_link` | completed | Confirmed live: both source tables `inactive=1` with full migration provenance notes (`source_legacy_ref` tags); `finding_question_link` is the live successor |
| #1377 | Glossary terms seeded from #1007's own catalogue exploration | completed | Folded into #1383's own "glossary updates needed" list already |

## 2. The one real gap this harvest found that no prior document named

**`finding_question_link` — the actual live mechanism that scores the catalogue against evidence —
has never been cross-referenced anywhere in #1378/#1379/#1383's nine documents, or in the just-filed
full build specification.**

Checked live: `finding_question_link` (bible_research.db, 332k rows) is the table that "joins
findings to the observation questions in `wa_obs_question_catalogue` that they answer — the
mechanism by which the question catalogue is scored against the evidence" (its own `cfg_table.use`
text). Its own use text also records: **"only 31 distinct questions are ever linked"** out of the
181-424 row catalogue. `report.obs_catalogue`'s own `cfg_step.does` text says outright: "structural
review of `wa_obs_question_catalogue` on its own — **no join to finding/finding_question_link**."

So the live tooling already knows, and says plainly, that nobody has ever checked which of the 181
active catalogue questions the 332k-row `finding` table has actually answered. #1383's entire
Stage-1 design (`verse_lexical`/`verse_lexical_note`, both `iba.db`) has no stated path to ever
populate `finding_question_link` (`bible_research.db`) — the design/propose document and the full
build specification both stop at "a catalogue question is answerable from Stage 1 data," never
"and here is how that becomes a scored `finding_question_link` row." **This is exactly what #1378
("Lexical-to-finding pipeline (per verse, per IB word)") exists to cover** — and #1378 is still
`state=raised`, untouched since 2026-09-01, while #1383 has run 22 versions designing Stage 1 ahead
of it.

This isn't a defect in #1383's own reasoning — Stage 1 was scoped deliberately as
Window-1/lexical-only, with the finding-production question explicitly assigned to "later" per the
blueprint. But it means **the catalogue's real outstanding work is not fully captured by #1383's
open items list** (which named the `phenomenon`/`operation` FK link as deferred, but never named
the `finding_question_link` gap at all) — this harvest is what surfaces it.

## 3. Everything else — genuinely closed, nothing further needed

`#1368`–`#1372` (tool bugs), `#1052`/`#1055`/`#1056` (config coherence/hardcoding), `#1020`/`#1021`/
`#1024`–`#1037` (finding-migration), `#1374`/`#1375` (scope classification), `#1377` (glossary
seeding) — every one of these checked live against its own claimed resolution, and every one
matches. No further action recommended on any of them.

## 4. Answer to the actual question — is there more?

**Yes, two items**, one small and mechanical, one real and substantial:

1. **#1018's drift** — the config change it claims was approved was never actually applied.
   Small, self-contained: re-propose `wa_flag_type_question_link.inactive=1` + the redundancy-
   finding use text through `Config-Maintenance.ps1 -Step Propose` and confirm it lands this time.
2. **The `finding_question_link` scoring gap (#1378)** — real, not small. #1383's Stage-1 build
   should not be treated as "the catalogue work" in full; #1378 is a distinct, still-unstarted piece
   of the same overall thread, and this harvest is the first document to name the specific mechanism
   (`finding_question_link`, 31-of-181 questions ever linked) it needs to eventually connect to.

Nothing else surfaced by this harvest is outstanding beyond what #1383's own open-items list (§i of
the full build specification) already names.

---

**Recommendation, not decided here:** keep #1444 open (in-progress) rather than closing it against
this one harvest pass — items 1-2 above are the concrete next actions, and #1444 is the natural
place to track whether #1018 gets re-applied and whether #1378 gets scoped/started, rather than
opening two more brand-new escalations for things already named here.
