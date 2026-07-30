# Passage rules audit — where every passage-related rule actually comes from

> One-off investigation, requested 2026-07-29 after escalation #327 (Dan passage distribution)
> was flagged as possibly applying a defunct rule. Read-only — no code/config changed.

## Method

Per project convention: started at `cfg_work_package` / `cfg_step` (the routines), then
`cfg_setting` (their inputs), then the actual handler code that reads those settings — not from
instruction docs or prior report files.

## 1. The three passage-related work packages (`cfg_work_package`)

| work_package | ps_script | inactive |
|---|---|---|
| `build-passages` | `Build-Passages.ps1` | **1 (inactive)** |
| `passage-quality` | `Passage-Quality.ps1` | 0 (active) |
| `passage-debate-report` | `PassageDebate-Report.ps1` | 0 (active) |

## 2. Their steps (`cfg_step`)

| work_package | step | handler | inactive |
|---|---|---|---|
| `build-passages` | `passage.build` | `handlers/passage.py:build` | **1 (inactive)** |
| `passage-quality` | `passage.validate` | `handlers/passage.py:validate` | 0 (active) |
| `passage-debate-report` | `report.passage_debate` | `handlers/reports.py:passage_debate_report` | 0 (active) |

**`passage.build` — the only step that ever encoded an algorithmic boundary rule — is inactive.**

## 3. The `passage.*` settings (`cfg_setting`)

| key | value | inactive |
|---|---|---|
| `passage.default_rule` | `"char-continuity"` | **1** |
| `passage.cross_chapter` | `false` | **1** |
| `passage.min_shared_strongs` | `1` | **1** |
| `passage.review_over` | `10` | **1** |
| `passage.quality_report_path` | `"iba/app/reports/passage-quality.md"` | 0 |
| `report.passage_debate_naming_pattern` | `"WA-{book}-{range}-debate.md"` | 0 |
| `method.passage_read_guidance_path` | `"iba/docs/WA-passage-read-guidance-v1.4-2026-07-28.md"` | 0 |

**Every setting that actually forms a passage boundary or size threshold is retired.** Only path/
naming settings and the read-*method* pointer (how to read a passage, not how big one is) are live.

## 4. What retired them, and when

- **BUILD.md §23 (2026-07-26)** — researcher's own words: *"the past use, and rules have moved on.
  The assembly of the passages is no longer relevant... reconciling with potential new data is not
  worth it."* `migration/retract_passage_system.py` deactivated `build-passages` + `passage-quality`
  (2 work packages, 2 steps, 5 `passage.*` settings, 1 `cfg_report` row) **and soft-deleted the
  data itself** — 18,504 `passage` rows / 24,763 `verse_passage` rows, `deleted=1`, kept only for
  provenance (full CSV export at the time).
- **BUILD.md §28 (2026-07-27)** — the `passage`/`verse_passage` tables were **repurposed** as a
  plain completion-tracking record for the new verse-fanout method (`report.verse_span_meaning` +
  `report.passage_debate`), via `lib/passagetrack.py`. This is *not* a rule engine: it just upserts
  one `passage` row per book/range that a report step was run over, and links every covered verse
  to it. The range itself (`-Chapters` / `-Range`) is chosen by the researcher/AI when invoking the
  report step, per the reading method, not derived from any stored rule.
- **`reactivate_passage_quality.py` (2026-07-28)** — `passage-quality` / `passage.validate` was
  turned back on, but repurposed for a *second, distinct* purpose: a spot-check on the new
  debate-range sizes (e.g. "was Dan 11's 45-verse range the right call?"), not on raw
  candidate-driven fragmentation. See `handlers/passage.py:validate`'s own docstring (lines
  150-157).

## 5. Empirical confirmation — the live Dan passage rows carry no rule at all

```
SELECT source, rule, COUNT(*) FROM passage WHERE book='Dan' AND deleted=0 GROUP BY source, rule;
→ source=NULL, rule=NULL, n=16
```

All 16 live Dan passage rows have `rule=NULL` and `source=NULL` — the columns `passage.build()`
used to stamp (`"char-continuity"`/`"maximal"`, `"passage-build"`) are empty because these rows
were never produced by that handler. They were inserted by `passagetrack.py:_upsert_passage()`,
called from `report.verse_span_meaning`/`report.passage_debate` at whatever range the researcher/
AI ran those steps over.

## 6. What actually governs a passage's boundaries today

**Nothing algorithmic.** `WA-passage-read-guidance-v1.4-2026-07-28.md` (the live
`method.passage_read_guidance_path`) is a *reading* method — subject/operation/source/target,
step 1-5 — not a *sizing* rule. It says how to read a passage once you're in it; it does not say
how many verses make one. Range choice (7 verses for Dan 1:1-7, 45 for Dan 11) is a judgement call
made when scaffolding each debate — presumably following the natural unit the researcher/AI reads
as one coherent movement — with no DB-encoded threshold behind it.

## 7. Why escalation #327 is a defunct-rule remnant

`passage.validate`'s question — *"7-45 verses/passage (average 21.38)... is this acceptable, does
any range look like an outlier that should be reconsidered?"* — is the **same shape of question**
(and, per its own docstring, deliberately reuses the same shape) as the *original* 2026-07-21 check
that WAS validating the char-continuity/`review_over=10` rule against real thresholds. Now that
rule is retired and range choice is a manual judgement call per-debate, "is any range an outlier"
has no rule to be an outlier *against* — the question presupposes a governing distribution that no
longer exists. The check still has legitimate value as a **prompt for researcher sanity-review of
judgement calls**, but its wording inherits framing from a rule that's gone, which is exactly what
was flagged.

## Not done here

No code or config changed. No decision made about whether/how to reword `passage.validate`'s
escalation question, retire it, or replace it with something scoped to the actual current method.
That's a judgement call for the researcher.
