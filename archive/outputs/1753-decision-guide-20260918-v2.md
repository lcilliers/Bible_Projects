> **v2 note:** identical content to the original — refiled through `filingkit.versioned_path()`
> (the actual governed one-off-report mechanism) instead of a hand-typed path. v1 is archived at
> `outputs/archive/1753-decision-guide-20260918.md`.

# Escalation #1753 — decision guide

> **Update, same day, after your v4 answers:** B1/B2/B3 below are now investigated and mostly
> built, not just recommended — see BUILD.md #297-298 for the real detail. Five things need your
> approval right now: escalations **#1773, #1774, #1775, #1776, #1777** (each a `configmaint.propose`
> waiting on `Escalation.ps1 -Action Update -Id <id> -NextAction approved`). One thing is blocked on
> you specifically: the `passage.lexical_complete_at` deactivation was refused outright by Claude
> Code's own auto-mode permission classifier (not by any project rule) — same call shape as the
> other 4, just this one table got blocked; needs you to either run it yourself or grant the
> permission. B4/B5/B6 and Group A's mechanical fixes are still queued, not done yet.

**Escalation:** #1753 — "cfg\_\* is structurally coherent, but has findings needing your judgement"
**Source report:** [`outputs/configs/CONFIG-REPORT-v498-20260918.md`](configs/CONFIG-REPORT-v498-20260918.md) §0 (138 numbered items)
**Full history:** [`outputs/escalation/1753-escalation-history-v1-20260918.md`](escalation/1753-escalation-history-v1-20260918.md)

You said "proceed with followup" (v2) but the escalation bundles 15 finding categories with very
different weight — some are one-line mechanical fixes, some are genuinely yours to call. This
splits them so you only have to look at the second group.

---

## A. No decision needed — I'll fix these directly

These are deviations from an already-established standard (`feedback_fix_standard_violations_dont_ask`),
not judgement calls.

| # | Finding | What I'll do |
|---|---|---|
| 38 | GOVERNANCE.md older than the newest applied cfg change | Add the missing §8 entry |
| 54 | `prosestore.py` builds `-v{n}` filenames by hand | Switch to `filingkit.versioned_path()` |
| 55–61 | 7 PS scripts drifted from `ps tools worksheet.xlsx` (missing tabs / stale columns) | Add the 7 missing tabs, fix the `Config-Maintenance` column — **will warn before opening the xlsx** per your standing rule |
| 137–138 | 2 `.sqlite3-query` files have spaces in their names | Rename to hyphens |
| 105–131 | 27 files whose header names an escalation the filename doesn't carry | Rename to prefix the escalation id (mechanical, matches the convention everywhere else) |
| — (report gap) | The escalation's own JSON lists **9 unregistered project scripts** (4 `.claude/hooks/*.py`, 2 `_analytics/Clusters/*.py`, 2 `iba/docs/*.py`, 1 `scripts/discovery/*.py`) missing a `cfg_utility` row — but §0 of the *report* never numbers this category, it's silently dropped. That's a bug in the report generator itself, not a config decision. I'll register the 9 scripts (`governance.new_utility_registration_timing`) and fix the report so this category actually renders. | |

No response needed on these — flagging so you know they're moving, not asking permission.

---

## B. Actual decisions — this is what you're being asked

### B1. Two retired writers, 29 stale `filled_by` columns (items 9–37)

All 29 trace to exactly two steps, both already inactive:

- **`lexicon.parse`** (15 columns: `strong_meaning_parsed`, `strong_lsj_parsed`, `strong_mounce_parsed`) —
  its write grants were deactivated *this session* (escalations #1747–1749, completed ~08:23 today).
  These columns are stale simply because the metadata hasn't caught up to a decision you already made.
  **My recommendation: mark them dormant (no live writer) — no action needed from you, I'll update
  `filled_by` to reflect that.**
- **`lexical.enrich`** (14 columns: `passage.genre/lexical_complete_at`, `verse_lexical_note.*`) —
  this is the old verse-lexical pipeline, and it sits inside the **gated** #737 migration
  ("do not start until [analysis phase]"). It isn't dormant by a decision, it's dormant because
  the whole area is paused.

**Your call:** for the `lexical.enrich` group, do you want me to (a) leave `filled_by` as-is and
just add a note pointing at #737 as the reason, or (b) actually mark those columns/tables inactive
now, ahead of #737 resolving? I'd default to (a) — cheaper, reversible, and doesn't pre-empt #737.

### B2. "Orphan" cfg_enum groups (items 1–8)

8 enum groups (`cluster.status`, `cluster_subgroup.status`, 4×`ib_observation.*`, `lexical_code_class`,
`party_kind`) exist in config but nothing in the code looks them up by name. Two different things could
be true for each: the enum is genuinely dead (safe to deactivate), or the code *should* be validating
against it but isn't (a real gap — e.g. `ib_observation.status`/`.stage` look like they ought to be
enforced somewhere given how much observation-validation work happened today, #1769/#1770/#1771).

**Your call — I don't have enough signal to guess which of the 8 are "dead" vs "should be wired
in but isn't."** I can go look (grep every write site for each of the 8 domains and report back
which ones are actually validated some other way, e.g. inline rather than via `cfg.enum()`) if you
want that before you decide — say so and I'll do it as a follow-up rather than guessing here.

### B3. "Low config-density" utilities (items 39–53) — checked, not just listed

I read all 6 *non-migration* modules in this list rather than taking the report at face value:

- **`recordingpass.py` is a real gap, not a legitimate zero.** It hardcodes
  `SIMILARITY_THRESHOLD = 0.85` with its own comment admitting "not a tuned constant... a starting
  point" — exactly the pattern already fixed today for #1761 (M49's hardcoded 60 → `cfg_setting`).
  **Recommendation: promote it to `cfg_setting` (e.g. `recording.similarity_threshold`), same
  treatment as #1761, rather than marking it exempt.**
- **`lexicalenrich.py`, `lexicalscope.py`, `clusterfamilyscan.py`, `clusterstatus.py`** — I checked
  for hardcoded thresholds/magic values in all four and found none; they're pure DB-resolution /
  state-transition helpers with nothing tunable. **Recommendation: mark all four `config_exempt=1`.**
  (Caveat on `lexicalenrich.py` specifically: it's part of the same gated #737 pipeline as B1's
  `lexical.enrich` columns — exempting it now doesn't commit you to anything about #737.)
- **`handlers/catalogue.py`** — read it: 38 lines, a thin param-validating dispatcher that delegates
  everything to `cataloguewrite.py`. **Recommendation: `config_exempt=1`.**
- The remaining 9 items in this category (`apply_1598_*`, `create_verse_meta_table_*`,
  `drop_verse_meta_genre_column_*`, `add_verse_meta_status_column_*`,
  `add_lexicon_header_pos_tags_setting_*`, `create_vw_strong_meaning_raw_*`, `VerseMeta.ps1`) are
  one-off migration scripts / a PS dispatch wrapper — same shape as the 11 migrations already
  marked exempt in §2 of the report. **Recommendation: `config_exempt=1`, consistent with the
  existing 11.**

**Your call:** approve the recommendations above (I apply all 15 via `configmaint.propose` in one
batch), or flag any specific one you want handled differently.

### B4. 2 PS scripts bypassing `run.py` (items 103–104)

`Behaviour.ps1` and `VerseMeta.ps1` call `iba.app.(handlers|lib|tools)` directly instead of
dispatching through `iba.app.run`. This is architectural, not mechanical — every other PS script
goes through `run.py`, so this is either a real inconsistency to fix, or those two scripts have a
legitimate reason to be different (e.g. they were built before the `run.py` dispatch convention, or
they need something `run.py` doesn't support).

**Your call:** should these two be brought in line with the rest (route through `run.py`), or is
there a reason they're special that should be recorded instead of "fixed"?

### B5. 2 behaviour rules claiming delivery that doesn't verify (items 101–102)

`#65 audit-deliverable-cross-check-before-presenting` and `#27 heredoc-powershell-only` are marked
`context_delivered` in `cfg_behaviour_rule`, but the checker found no actual verifiable mechanism
(no memory file, no `governance.*` setting, no referenced doc) behind that claim. This is the same
`not_mechanically_checkable`-drift pattern #1388 already fixed for other rows — these two slipped
through.

**Your call:** do you want these two actually built (a real delivery mechanism), or is the honest
answer "downgrade the status" (e.g. to `judgment_call_pending` or `buildable_not_built`) until they
are? I'd lean toward downgrading rather than leaving a false `context_delivered` standing, but the
choice of what status is genuinely yours.

### B6. 5 config rows still carrying an unresolved hedge phrase (items 132–136)

`cfg_method_rule #67` (spine-on-demand-pull-mechanism), `#106` (battery-scope-excludes-verse-reading-
and-science-extract), and 3 `governance.*` settings (`prose_canonical_authority`,
`procedural_document_taxonomy`, `engineering_documentation_folder`) still have "not yet decided" /
"TBD"-shaped language sitting in a row marked active. Each one is a small, separate wording decision
— not something I should paraphrase away.

**Your call:** want these read out one at a time (I can pull the exact rule_text for each) so you
can either finalize the wording or explicitly mark it deferred, rather than left as a live hedge?

---

## Suggested next step

Everything in **A** I'll start on now unless you say otherwise. For **B**, the smallest thing you
could decide right now is **B3** (I've already done the legwork — it's just "approve the 15
exempt/build recommendations, yes/no"). B1/B4/B5/B6 need a short answer each; B2 needs you to tell
me whether to go investigate first.
