# Core, active modules: does the config do what it says, and does it say enough?

> The prior review (`configmaint-validate-gap-analysis-20260729.md`,
> `PLAN-config-system-remediation-v1-20260729.md`) audited cross-cutting infrastructure and the two
> **retired** modules (candidate, passage-build). It never asked the researcher's actual question
> of every **active, currently-used** module: *what does this config intend, does it actually do
> it, is it effective, and is it complete — does it control everything we'd expect it to.* This
> does that, module by module, against live code. Read-only.

## Method

For every module with real processing logic (`raw`, `registry`, `lexicon`, `narrative`, the
verse-span-meaning/passage-debate/whole-book-read report chain, `retention`), every `cfg_setting`
row was traced to its actual read site and the surrounding function was read in full — not just
grepped for co-occurrence (the existing orphan check's weaker test). Then the same function was
checked for hardcoded logic that has no `cfg_setting`/`cfg_enum` counterpart at all.

---

## `raw` (handlers/raw.py) — STEP ingestion, the foundation every word is built on

| setting | intends (per `use`) | actually does | effective? |
|---|---|---|---|
| `discovery.follow_related` | gate whether `relatedNos` are followed during seed discovery | `raw.py:79-80`: `if ctx.cfg.setting(...): pass  # would expand here` | **NO — dead.** Set it `true` via `configmaint.propose` and *nothing changes*; the expansion branch was never built. This passes the existing orphan check (the key literal sits next to a `.setting(` call) but fails the researcher's actual test: changing it changes nothing. |
| `language.greek_prefix` | Greek vs. Hebrew classification | `raw.py:132`: `"Greek" if resolved.startswith(greek) else "Hebrew"` | yes, confirmed |
| `meaning.head_marker` | split a `mediumDef` into head/tree | `_split_def`, confirmed applied | yes |

**Completeness gaps found (hardcoded, no config):**
- `validate()`'s no-null check scans a hardcoded tuple `("strong", "verse", "span")` — which tables
  get checked is a rule, not a fact, and isn't config.
- `backfill_meaning()`'s whole-book chapter bound is a hardcoded `999`.
- The `<br>`/`<BR>` normalisation regex in `_split_def` is hardcoded, duplicating the *concept*
  `raw.meaning_tree_clean_pattern` already expresses as config for the sibling check on
  `strong_meaning_tree.sense_text` — same fact, unrelated representations.
- `BASE_RE` (`^([HG]\d+)([A-Z]?)$`) hardcoded here — **already flagged once**
  (`GOVERNANCE.md` §5) as duplicating `candidate.lemma_base_pattern` (now inactive). **A third,
  previously unnoticed copy exists** in `lib/versespanmeaningreport.py:27` — see below. One fact,
  three homes now, not two.

## `registry` (handlers/registry.py) — the approval gate every new word passes through

| setting | intends | actually does | effective? |
|---|---|---|---|
| `registry.strip_ends_pattern` | normalise a word's entry form | applied in `lib/words.py` (not this file) | yes |

**Completeness gaps** — the two rules that actually decide the approval flow's outcome are both
hardcoded, with no config equivalent even though `cfg_status_flow` exists for exactly this purpose:
- `BUILT = ("raw-complete", "signed-off")` — which statuses count as "already built" (governs
  whether `exists()`/`create()` treat a word as done) is a Python tuple, not a `cfg_status_flow`
  read.
- The duplicate-word warning threshold — "warn only if the new word shares **100%** of its strongs
  with an existing word" (`registry.py:120`) — is a hardcoded business rule. There is no setting to
  tune it (e.g. warn at 80% overlap too), and no record of *why* 100% was chosen.

## `lexicon` (handlers/lexicon.py + lib/lexiconparse.py) — the single richest processing module in the app, with the thinnest config footprint

`lexicon.quality_report_path` (report location) is the module's **entire** config surface — one
setting. Every actual **parsing rule** — how a raw `strong_meaning_tree`/`strong_lexicon` row
becomes a `strong_meaning_parsed`/`strong_lsj_parsed`/`strong_mounce_parsed` row — lives in
`lib/lexiconparse.py`, which contains **zero** `cfg.setting()` calls anywhere (confirmed by direct
grep of the file). Hardcoded there instead: `NON_LATIN_SCRIPT_RE`, `OUTLINE_CODE_RE`,
`REF_TAG_RE`, `LINEBREAK_RE`, `_TOP_LEVEL_LABEL_RE`, `_BARE_SUBLABEL_RE` (six regexes) and
`_LEVEL_TAGS = {"level1","level2","level3","level4"}` — the entire rule-set that decides how a
sense-tree gets classified and split. This is the sharpest instance in the app of "the code decides
everything, the config decides nothing" for a module that is neither retired nor peripheral —
`lexicon.parse`/`lexicon.related` run regularly and feed the raw/backfill chain directly
(`handlers/raw.py:316-318` calls `rebuild_parsed_tables`/`fetch_related_for` on every backfill).

## `narrative` (handlers/narrative.py) — the inner-being narrative scope-check

| setting | intends | actually does | effective? |
|---|---|---|---|
| `narrative.scope_check_report_path` | report location | applied | yes |
| `method.inner_being_narrative_guidance_path` | point at the current guidance doc | read, existence-checked | yes, as a pointer |

**Completeness gap:** `REQUIRED_LABELS = ("Non-human ↔ human", "Human ↔ human", "Physical world ↔
human")` — the exact three channel labels that determine pass/fail — is a hardcoded Python tuple.
The single fact this whole check exists to enforce is not itself config; adding, renaming, or
retiring a channel requires a code change, not a `configmaint.propose`.

## The live verse-span-meaning / passage-debate / whole-book-read chain — the method in daily use right now

This is the sharpest finding in the whole review, because unlike the candidate/passage-build
material, **this is the method actively being used every session.**

`report.passage_debate` writes section headings **from config** (`cfg_report_section.heading`,
e.g. `"## Emergent questions log..."`, `"## Passage-level linkages (Q7)"`). `report.whole_book_read`
then **reads those same generated files back** to extract exactly those two sections — but does so
with its own **independently hardcoded** regexes:

```
lib/wholebookread.py:44  EQ_HEADING_RE = re.compile(r"^##\s+Emergent[- ]questions?\s+log", ...)
lib/wholebookread.py:45  LINKAGE_HEADING_RE = re.compile(r"...", ...)
```

**These are two independent representations of the same fact — the config value that controls
what gets *written*, and a hardcoded pattern that controls what gets *read back* — with nothing
keeping them in sync.** If `cfg_report_section.heading` for `report.passage_debate` were ever
changed via `configmaint.propose` (a fully sanctioned, ordinary action), `report.whole_book_read`
would silently stop finding the section in every future debate file, with no error pointing at the
cause — it would just report `NOT FOUND` the way it already does for a heading-variant mismatch
(`BUILD.md` §33's "third heading variant" incident is exactly this class of failure, already hit
once).

Also found here: `versespanmeaningreport.py:27` has its **own** copy of `BASE_RE`
(`^([HG]\d+)([A-Z]?)$`) — a third occurrence of the pattern named in `raw` above — and a hardcoded
`_STOP_TOKENS` set used in the AMBIGUOUS-span disambiguation logic, with no config equivalent.

## `retention` (lib/retention.py)

`retention.report_path` is applied correctly. **Completeness gap:** the report's row limits
(`LIMIT 50` ×2, `LIMIT 200`) are hardcoded, unlike the equivalent tunable elsewhere in the app
(`report.sample_verses`).

---

## What this changes about the migration plan

The existing plan's Phase 1/3 treated "hardcoded logic" and "config completeness" as things to
generalise into a *check* (a good instinct), but its Part A evidence for those categories came only
from the passage module and `run.py`. The findings above show the same two failure modes —
**a setting that's read but does nothing (`discovery.follow_related`)**, and **a whole rule-set
living only in code with no config counterpart (`lexicon` module; `narrative`'s required labels;
`registry`'s built-status set and duplicate threshold; the write/read heading duplication in the
live passage-debate chain)** — are present in core, active, currently-used modules, not just
retired ones. Folded into the plan as new Phase 1 remediation items and a standing Phase 3 check
(see `PLAN-config-system-remediation-v1-20260729.md`, updated).
