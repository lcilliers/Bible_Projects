# Escalation core model — decision-vs-defect axis (v5, FINAL — supersedes v1-v4)

**Escalation #798** (`from_id=753`). All open inputs from v4 answered below. If nothing new is
open after this, this proposal moves to `ready_for_approval`. §1/§2/§5/§6 unchanged from v4 (not
repeated in full — see v4 for their literal text; nothing in them changed).

---

## Open input 1 (§3.5, passage thresholds) — answered, with a structural correction

**Thresholds, exact:**
- Single-verse passages, **per book**: `(count of single-verse passages in that book) /
  (total verses in that book) > 20%` → breach.
- Average verses per passage, **per book**: `avg_verses_per_passage > 30` → breach.

Both computed per book using data `passage.py`'s `validate()` **already computes** (`by_book`:
`n`, `avg`, `single`, plus book's own total verse count via `books`/`verse` — one small addition
needed, see below) — no new query shape, just a new comparison.

**Structural correction, per your instruction — these do NOT belong in `cfg_setting`:**

No `cfg_passage`-shaped table exists yet. Per `governance.module.config`, it should. Building it:

**New table `cfg_passage`** (mirrors `cfg_setting`'s proven shape, minus the redundant `module`
column — the table itself is the scope):
```sql
CREATE TABLE cfg_passage (
    key      TEXT PRIMARY KEY,
    value    TEXT,
    use      TEXT,
    inactive INTEGER NOT NULL DEFAULT 0
)
```

**Governance registration that comes with any new table** (checked live — every existing `cfg_*`
table has these; `cfg_passage` needs them too):
- `cfg_table`: `database='iba', name='cfg_passage', grain='one row per key', use='Module-specific
  settings for the passage module (governance.module.config) — replaces module=passage rows
  formerly in the shared cfg_setting table.'`
- `cfg_column` ×4: `key` (PK), `value`, `use`, `inactive` — same `use` text style as `cfg_setting`'s
  own column docs.
- `cfg_write_grant`: `writer='configmaint.propose', table_name='cfg_passage', database='iba'` —
  matches `cfg_prose_chapter`'s exact grant pattern.

**All 6 rows `cfg_passage` will hold** (4 moved unchanged, 2 new — checked every live consumer by
grep first, see below):
```
key: passage.quality_report_path
value: "iba/app/reports/passage-quality.md"
use: where passage.validate persists its findings

key: passage.debate_session_chapter_guideline
value: 3
use: (unchanged from current cfg_setting row)

key: passage.debate_run_sequence
value: (unchanged JSON array, from current cfg_setting row)
use: (unchanged from current cfg_setting row)

key: passage.debate_staging_path_pattern
value: "iba/app/staging/operations/{book_lower}-{scope}-{step}.json"
use: (unchanged from current cfg_setting row)

key: passage.max_single_verse_pct
value: 20
use: "Per-book threshold: passage.validate escalates only if a book's (single-verse passage
      count / total verses in that book) exceeds this percentage. Below it, the book's
      distribution is accepted automatically — no researcher decision needed for an
      already-in-bounds result."

key: passage.max_avg_verses_per_passage
value: 30
use: "Per-book threshold: passage.validate escalates only if a book's average verses-per-passage
      exceeds this. Below it, accepted automatically."
```
Keys keep their **exact original text** (including the literal `passage.` prefix) — this means
every existing caller's string argument to `cfg.setting("passage.xxx", ...)` needs zero text
changes, only the *method* it's called through changes (below). Minimises the change surface,
per your own "no hidden decisions" instruction — I didn't rename anything without a reason to.

**Every live consumer of the 4 existing keys, found by grep, all updated to the new read path:**
- `iba/app/handlers/passage.py:249` — report path read
- `iba/app/lib/debaterun.py:40` — staging path pattern read
- `iba/app/ps/Chapter-Generate.ps1:105` — inline `python -c` calling `c.setting(...)` for the
  session guideline
- `iba/app/ps/Debate-Run.ps1:147` — inline `python -c` calling `c.setting(...)` for the run
  sequence
- `iba/app/lib/cfgquality.py:32` — the `REPORT_STEPS`-style mapping
  (`"passage.validate": "passage.quality_report_path"`) used to verify report paths are
  registered; needs to know this key now lives in `cfg_passage`, not `cfg_setting`, or it will
  falsely flag an orphan once moved.
- 3 one-time migration scripts (`reactivate_passage_quality.py`, `cleanout_retired_passage_config.py`,
  `bootstrap_report_persistence_governance.py`) reference these keys in comments/history only —
  historical record, **not** touched (they already ran; editing them would rewrite history for no
  reason).

**New `Cfg` method** (generalised rather than passage-only, since `governance.module.config` is a
project-wide principle other modules will likely need too — flagging this generalisation choice
plainly rather than silently deciding it doesn't matter):
```python
def module_setting(self, table: str, key: str, default=None):
    """Generic reader for a per-module settings table shaped like cfg_setting (key/value/use/
    inactive) but scoped to one module -- e.g. cfg_passage. `table` is always a literal name
    supplied by the calling code, never external input."""
    r = self.conn.execute(
        f'SELECT value FROM "{table}" WHERE key=? AND inactive=0', (key,)).fetchone()
    val = json.loads(r["value"]) if r else default
    _trace(f"module_setting({table}, {key})", val)
    return val
```
Every call site above changes from `ctx.cfg.setting("passage.xxx", default)` to
`ctx.cfg.module_setting("cfg_passage", "passage.xxx", default)` — same key text, new table.

**One new small query** needed in `passage.py`'s `validate()`: total verses per book (for the
single-verse-percentage denominator) — a straightforward `SELECT book, COUNT(*) FROM verse ...
GROUP BY book`, joined against the existing `by_book` distribution data.

**This is a real migration, executed by a new one-time script** (matches how `cfg_prose_chapter`
was built — `migration/bootstrap_prose_authority_v1_20260818.py` — table creation is DDL, not a
`configmaint.propose` row-edit): `iba/app/migration/bootstrap_cfg_passage_v1_20260822.py` —
creates the table, registers it (`cfg_table`/`cfg_column`/`cfg_write_grant`), inserts all 6 rows,
then deletes the 4 old rows from `cfg_setting` in the same script (one atomic unit, not two
separate steps that could be left half-done).

## Open input 2 (§3.6, raw.zero_strongs_action) — set to `reject`

*"When this happen it will give me a chance to rethink the system because it should not happen."*
Updating §3.6's proposed default from `proceed` to **`reject`** — a zero-strongs result is
treated as anomalous, always, until you decide otherwise for a specific case. `discover()`'s fix
(§9 of v4) changes accordingly: `action = ctx.cfg.module_setting(...)` default `"reject"`, and the
`if action == "reject"` branch is now the expected, common path, not a fallback.

## Open input 3 (§7, debugging/logging) — specified for this build's own files, real issues found

Your rule: only raise a new escalation if this touches scripts *outside* this build's scope;
everything inside it gets proper debugging/logging specified here. Checked the actual files this
build already touches — found two concrete, real weaknesses, not generic principle:

1. **`iba/app/lib/escalation.py`, the CLI crash-wrapper (line 982):**
   ```python
   except Exception:
       pass   # never let a failure recording the crash mask the original crash itself
   ```
   The *intent* is right (a secondary failure while recording a crash must never hide the
   original crash) but the *implementation* silently discards the secondary failure with zero
   trace. Since this build adds a new required field (`resolution_kind`) to `raise_new()`, this
   exact code path is now the one most likely to break from this build's own changes — and if it
   does, nobody would ever see it. **Fix:** log the secondary failure to stderr before continuing:
   ```python
   except Exception as record_exc:
       print(f"[WARN] failed to record crash escalation: {record_exc!r}", file=sys.stderr)
   ```
   Original behaviour (never mask the real crash — the `raise` below still fires) unchanged.

2. **`iba/app/run.py`, the crash and report-stop blocks:** `esc_raise()` is called with no
   surrounding `try`/`except` at all. If `esc_raise()` itself throws (the same new-required-field
   risk as above), the ORIGINAL crash's clean traceback is replaced by the secondary one — Python's
   exception chaining keeps the original as `__context__`, but it's no longer the primary, clean
   signal. **Fix:** wrap both `esc_raise()` calls the same way as #1 above — log any secondary
   failure to stderr, never let it replace the original `raise`.

3. **New code added by this build** (the `self_correctable` close transaction,
   `escalate_to_decision()`, `Cfg.module_setting()`) **must participate in the existing `_trace()`/
   `IBA_TRACE` convention** already established in `cfg.py` — this is the project's own existing
   debugging mechanism; new code that doesn't use it would itself be a new instance of the same
   "sloppy" pattern. `module_setting()` already specified with a `_trace()` call above; the two new
   escalation transactions get the same treatment (trace the resolution_kind decision and the
   before/after state on every call).

Nothing here touches a file outside this build's own scope — no new escalation raised, per your
instruction.

## Open input 4 (§4, `escalate_to_decision`) — confirmed, no change

---

## Updated §8 — consolidated config list (supersedes v4's)

| Table | Row | Value |
|---|---|---|
| `cfg_behaviour_rule` | `development` / `decision-points-are-terminal-not-inline` | full text in v4 §1 |
| `cfg_enum` | `resolution_kind` = `decision_required` / `self_correctable` | v4 §2 |
| `cfg_escalation_requirement` | `raise` / `resolution_kind` / `always` / `field_required` | v4 §2 |
| `cfg_table` | `cfg_passage` | this document, above |
| `cfg_column` ×4 | `cfg_passage`'s own columns | this document, above |
| `cfg_write_grant` | `configmaint.propose` → `cfg_passage` | this document, above |
| `cfg_passage` ×6 | `quality_report_path`, `debate_session_chapter_guideline`, `debate_run_sequence`, `debate_staging_path_pattern` (moved, unchanged), `max_single_verse_pct`=20, `max_avg_verses_per_passage`=30 (new) | this document, above |
| `cfg_setting` | **4 rows deleted** (moved into `cfg_passage`) | — |
| `cfg_setting` | `raw.zero_strongs_action` | `"reject"` (was proposed `proceed` in v4, corrected) |

## Updated §9 — consolidated code-change list (supersedes v4's; additions in **bold**)

Everything in v4 §9, plus:

| File | Change |
|---|---|
| `iba/app/lib/cfg.py` | **New `module_setting(table, key, default)` method** |
| `iba/app/handlers/passage.py` | §3.5's threshold fix now reads via `module_setting("cfg_passage", ...)`; **new per-book total-verse query for the percentage denominator** |
| `iba/app/lib/debaterun.py` | Read-path swap to `module_setting("cfg_passage", ...)` |
| `iba/app/ps/Chapter-Generate.ps1`, `Debate-Run.ps1` | Inline `python -c` snippets updated to call `c.module_setting('cfg_passage', ...)` |
| `iba/app/lib/cfgquality.py` | `REPORT_STEPS`-style mapping updated to know `passage.quality_report_path` now lives in `cfg_passage` |
| `iba/app/handlers/raw.py` | §3.6 default corrected to `"reject"` |
| `iba/app/lib/escalation.py` | **Line 982's `except Exception: pass` → log to stderr, don't silently discard (§7 fix #1)** |
| `iba/app/run.py` | **Both `esc_raise()` calls in the crash/report-stop blocks wrapped with the same log-don't-mask pattern (§7 fix #2)** |
| **New:** `iba/app/migration/bootstrap_cfg_passage_v1_20260822.py` | The `cfg_passage` migration script (table + registration + row moves), one atomic unit |

## Updated §11 — build stages (Stage 1 revised to include the `cfg_passage` migration; others unchanged from v4)

**Stage 1 — config, now including the `cfg_passage` migration.**
*Test:* run `bootstrap_cfg_passage_v1_20260822.py`; confirm `cfg_passage` has exactly 6 rows and
`cfg_setting` no longer has any `passage.*` row; `Config-Maintenance.ps1 -Step Validate` exits
clean (no orphan-setting false positive from `cfgquality.py`'s updated mapping). Then the
`resolution_kind` requirement row, tested as in v4.

Stages 2–5: unchanged from v4 §11, with stage 4's `passage.validate` test now exercising the real
per-book percentage/average logic against live data instead of a placeholder.

---

## Status: no further open items from my side

If you confirm nothing else is open, next step per your instruction: I set this to
`ready_for_approval` with a full resolution, and on your approval, raise the separate build-tracking
escalation so the build itself can start immediately.
