# Flag Management — introducing the flag table into prose management: proposal (escalation #829, continuing #833) — v1

> **SUPERSEDED 2026-08-24.** This should have been filed as the next revision of the one living
> proposal document for #829 (`prose-management-iba-first-layer-proposal-vN`), not a separate,
> differently-named file — the researcher caught this process mistake directly. All content below is
> carried forward, unchanged in substance, as §12–§13 of
> [`prose-management-iba-first-layer-proposal-v5-20260823.md`](prose-management-iba-first-layer-proposal-v5-20260823.md).
> Kept on disk as a record of the mistake, not as a document to keep reading — read v5 instead.

**Stage: propose/design**, per `cfg_behaviour_rule` class=`development`, rule_key=`test-plan-per-module-utility`
(escalation #828): plan/propose/design (in detail) → approve → build → test → approve. Nothing below
has been submitted to `configmaint.propose` or built. Filed against **#829** (the researcher's own
routing, this chat turn) — cross-referenced to **#833** (Flag Management), which already settled
*"the repurposed table pair IS the prose-flag mechanism"** (#829 v7). This document is the next,
concrete layer on top of that: how the mechanism actually reaches `prose_section`.

---

## 1. Instruction captured, verbatim (researcher, 2026-08-23)

*"The new flag table can be introduced into the prose management system. I imagine you need configs
to set its use. important is the connection that if methodology, terminology, and finding change for
stuff that is in use in prose, that an entry must be generated in the flag table. So I would say
there must be a utility that can be called, or at least raise the attention to rapidly add the
entries in the flag table. You can start this process by flag entries for the change of terminology
for sessions. The whole principle is that one does not need to drop and go and fix prose, but just
raise the flag."*

Read as four parts: (a) wire the already-repurposed flag table into prose, config-driven; (b) the
governing principle — a methodology/terminology/finding change that touches content already written
into prose obligates a flag entry, not an immediate fix; (c) a fast-entry utility, so raising a flag
is cheap enough to actually happen in the moment a change is made, not deferred; (d) start now, with
real entries, for the Session A/B/C/D → Base_data/Analysis/Publishing terminology change.

---

## 2. Gap found live, checked directly (not assumed)

**`wa_data_quality_flags` has no path to `prose_section` today.** Its schema, as actually rebuilt by
#833 (confirmed against `sqlite_master`, not the design doc):

```sql
CREATE TABLE wa_data_quality_flags (
    id               INTEGER PRIMARY KEY AUTOINCREMENT,
    strong_id        TEXT,
    verse_id         INTEGER,
    flag_id          INTEGER NOT NULL REFERENCES wa_quality_flag_types(id),
    description      TEXT,
    corrective_action TEXT,
    correction_date  TEXT,
    delete_flagged   INTEGER NOT NULL DEFAULT 0,
    last_changed     TEXT
)
```

`strong_id`/`verse_id` are both loose, documented-only references (per #833's own decision — SQLite
can't FK across `iba.db`/`bible_research.db`). Neither identifies a `prose_section` row, and most of
the content the researcher is pointing at (the Programme book's own narrative chapters) isn't
verse- or term-scoped at all — it's programme-level prose with `registry_id IS NULL` and
`metadata_json IS NULL`. Without a real connector, a flag raised today has nothing to point the
prose author back at. This is the concrete gap §3 closes.

**Second, unrelated gap found while grounding this** (worth fixing regardless, not folded silently
into #833's "complete" status): `cfg_column` for the two repurposed tables is **stale** —
`wa_data_quality_flags` still lists the pre-repurpose columns (`file_id`, `term_id`; no `strong_id`,
`verse_id`, `corrective_action`, `correction_date`, `delete_flagged` rows at all), and
`wa_quality_flag_types.deprecated` is still catalogued under its old name and old row-count
(`"0 for 25 codes, 1 for 4"` — describes the deleted 29-row vocabulary, not the live 3-row one; the
live column is actually named `delete_flagged`). `cfg_table` for both was correctly rewritten;
`cfg_column` was not — a real deviation from `governance.table_columns`
(`feedback_fix_standard_violations_dont_ask`). Proposed to fix as part of this build (§4), logged
against #833 since that's whose build left it stale, not re-litigated here.

---

## 3. Proposed design

### 3a. Schema — one nullable connector column

```sql
ALTER TABLE wa_data_quality_flags ADD COLUMN prose_section_id INTEGER REFERENCES prose_section(id);
```

Same database (`bible_research.db`), so this is a **real, enforceable FK** — unlike `strong_id`/
`verse_id`, which cross a database boundary. Nullable, matching `strong_id`/`verse_id`'s own
"optional" pattern (#833 §3a) — a flag can be term-scoped, verse-scoped, prose-scoped, or (rarely)
more than one, without forcing a shape. `SPAN[..]` — SQLite `ALTER TABLE ADD COLUMN` is safe here
(no data loss, no rebuild needed, unlike #833's own hard-delete-and-recreate).

### 3b. Config — the trigger obligation, stated as a real rule

One `cfg_behaviour_rule` row, `class='sqlite'` (matching #829/#833 precedent — this is a
database-state discipline, same reasoning as `governance.behaviour_boundary.backup_recovery`):

| Field | Value |
|---|---|
| `rule_key` | `prose-quality-flag-on-upstream-change` |
| `rule_text` | "When a methodology, terminology, or finding change makes existing prose content stale, the obligation is to raise a `wa_data_quality_flags` entry (`flag_group='PROSE_QUALITY'`) against the affected `prose_section` row(s) — not to stop and rewrite the prose in place. Prose gets fixed later, in its own pass; the flag is what prevents the drift from being silently lost in the meantime." |
| `source` | Researcher, 2026-08-23 (this instruction), escalation #829/#833 |
| `enforced_by` | Not mechanically enforced (no code path currently detects "this change affects that prose") — a discipline rule, made real and queryable via `cfg_behaviour_rule`, not yet automated. Matches the honest-limitation pattern already used for `governance.rules_must_be_config_driven` itself. |

### 3c. Utility — a fast-entry step, so raising a flag is genuinely cheap

New dispatcher step under the `prose` work package (the one #829 v4 §4-II proposes but hasn't built
yet — see dependency note below):

| ordinal | step | handler | kind | does |
|---|---|---|---|---|
| 4 | `prose.flag` | `iba.app.handlers.prose:flag` | utility | Raise a `wa_data_quality_flags` row: `--flag-code` (one of the 3 seeded `PROSE_QUALITY` codes, or a new one), `--prose-section-id` (repeatable, for batch raises against several rows at once), `--description` (required — the specific issue), `--corrective-action` (optional, filled in only if already known) |

Mirrors the shape `Escalation.ps1 -Action Raise` already uses (fast, single-purpose, mandatory
minimum fields) rather than inventing a new interaction pattern.

**Dependency, stated plainly:** `prose.flag` needs `cfg_work_package name='prose'` to exist to attach
to. That work package is proposed but **not yet built** — #829 v4 §4-9 is still awaiting your
approval (confirmed live: 0 rows in `cfg_work_package` for `name='prose'` today). Two ways to
proceed, your call:

1. **Bundle `prose.flag` into #829's still-pending build** as a fifth dispatcher step alongside the
   4 already proposed (extract/search/export/import) — one build, one approval, done together.
2. **Approve #829's v4 build first** (§4-9, already fully specified, nothing new), then this
   document's schema/config/utility land as a small follow-on increment once the work package exists.

Recommendation: (1) — it's one more row in an already-open build, and delaying it means the
"utility to rapidly add entries" the researcher just asked for stays unavailable until a second,
separate approval round.

### 3d. Write grant

```
writer='prose_flag', table_name='wa_data_quality_flags', database='bible_research'
```

---

## 4. Recatalogue fix (§2's second gap) — proposed alongside, not deferred

Rewrite `cfg_column` for both tables to match the live schema exactly: drop the 2 stale rows
(`file_id`, `term_id`) and the mis-named `deprecated` row on `wa_data_quality_flags`/
`wa_quality_flag_types`; add rows for `strong_id`, `verse_id`, `corrective_action`,
`correction_date`, `delete_flagged` (both tables' `delete_flagged`), and — once §3a is approved —
`prose_section_id`. Logged as a correction against **#833**, since that build's own sequencing (step
6) called for this and it didn't complete.

---

## 5. Starting batch — the Session A/B/C/D terminology change

**Grounding fact, already config-recorded:** `governance.programme_stages` — *"The research
programme has three main stages: Base_data (STEP through lexical); Analysis (deriving understanding
of the inner being); Publishing (essays and output for the results). Previously referred to as
Session A (base data), Session B/D (analytics), Session C (publishing)..."* The supersession is
already a stated fact; what's missing is prose carrying the old names forward as if still current.

**Live measurement** (checked directly, `prose_section.delete_flagged=0`, body text containing
`"Session A"`/`"Session B"`/`"Session C"`/`"Session D"`): **134 rows**, by `prose_section_type.
source_stage`:

| `source_stage` | rows | Note |
|---|---:|---|
| `programme` | 42 | **41 of these are in the `Programme` book itself** — the canonical-authority book (`governance.prose_canonical_authority`), chapters 0-3 of which are marked `reviewed`/`final` in `cfg_prose_chapter` yet still narrate the pipeline as "Session A/B/C/D" (verified live — e.g. prose_section id 10 "Programme flow", id 13 "Key methodological principles"). This is exactly the authoritative-content drift the researcher's principle targets. |
| `session_a` | 54 | Per-word Session A analytical output — the old per-word pipeline. Disposition of this whole body of content is itself an open question (#784 §9, not decided) — flagging it now doesn't block that decision, but it's a different kind of content from the Programme book. |
| `findings` | 15 | |
| `session_b` | 11 | |
| `session_c` | 8 | |
| `verse-analysis` | 4 | |

**Recommended starting scope: the 42 `programme`-stage rows** (via `prose.flag`, one entry per row,
`flag_code='Terminology change'`, `description` naming the specific old term(s) found in that row and
pointing at `governance.programme_stages` as the supersession record). This is the authoritative book,
the smallest coherent batch, and the clearest match to "stuff that is in use in prose" going stale.
The other 92 rows (mostly legacy `session_a` per-word output) are a real second batch, held back only
because they're entangled with #784 §9's still-open disposition question — recommend deferring them
to a second pass once that's settled, not skipping them silently.

If you'd rather flag all 134 in one pass regardless of the #784 §9 question, say so and I'll do that
instead — this is a scope call, not a mechanical one.

---

## 6. What I need from you

1. **§3a's schema addition** — `prose_section_id` nullable FK on `wa_data_quality_flags`. Approve as
   written, or a different shape?
2. **§3c's sequencing** — bundle `prose.flag` into #829's still-pending v4 build (recommended), or
   hold it for a follow-on round after v4 is approved separately?
3. **§5's starting scope** — the 42 `programme`-book rows only (recommended), or all 134 in one pass?

Once these are answered I'll run the build (schema, config, utility, recatalogue fix), test it, raise
the actual flag entries for the approved scope, and bring results back in one resolution against
#829 (cross-referencing #833 for the recatalogue correction).
