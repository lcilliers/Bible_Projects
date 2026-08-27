# Prose functionality test — escalation #908

> Two parts, as instructed: (a) the full live extract of every module/utility config tied to
> prose; (b) a step-by-step test plan quoting the actual `Prose.ps1` script layout, so you can run
> every test yourself from the literal commands below — nothing paraphrased.

## a) Extract — every script prose functionality actually touches

### Module config — `cfg_work_package` / `cfg_step`

**`cfg_work_package`**: `name='prose'` · `ps_script='iba/app/ps/Prose.ps1'` · `runs_over='none'` ·
`chained=0` · `inactive=0`

**`cfg_step`** (7 rows, all `kind='utility'`, all `inactive=0`):

| ordinal | step | handler | does |
|---:|---|---|---|
| 0 | `prose.extract` | `iba.app.handlers.prose:extract` | Programme-prose extract (JSON/MD/DOCX) |
| 1 | `prose.search` | `iba.app.handlers.prose:search` | FTS/plain search over `prose_section` |
| 2 | `prose.export_chapter` | `iba.app.handlers.prose:export_chapter` | Export a chapter to editable `.md` |
| 3 | `prose.import_chapter` | `iba.app.handlers.prose:import_chapter` | Turn an edited `.md` into a patch file (no DB write) |
| 4 | `prose.flag` | `iba.app.handlers.prose:flag` | Raise one `wa_data_quality_flags` instance (angle a) |
| 5 | `prose.flag_fix_propose` | `iba.app.handlers.prose:flag_fix_propose` | Search + write a review report (angle b, propose) |
| 6 | `prose.flag_fix_apply` | `iba.app.handlers.prose:flag_fix_apply` | Generate a supersede patch from an approved report (angle b, apply) |

### Utility config — `cfg_utility`, everything matching `%prose%`

**Live, active, this is what "prose functionality" means today:**

| module | file | status |
|---|---|---|
| `prosestore` | `iba/app/lib/prosestore.py` | active — the real implementation every step above dispatches into |
| `scripts_build_programme_prose_extract` | `scripts/build_programme_prose_extract.py` | active, `config_exempt=1` — thin CLI wrapper, superseded by `prosestore.py`, kept as documented direct-Python entry point |
| `scripts_export_prose_chapter_edit` | `scripts/export_prose_chapter_edit.py` | active, `config_exempt=1` — same, wraps `export_chapter` |
| `scripts_import_prose_chapter_edit` | `scripts/import_prose_chapter_edit.py` | active, `config_exempt=1` — same, wraps `import_chapter` |
| `scripts_search_prose` | `scripts/search_prose.py` | active, `config_exempt=1` — same, wraps `search` |

`Prose.ps1` itself is **not** a separate `cfg_utility` row — PS work-package scripts are registered
via `cfg_work_package.ps_script` only (same convention as `Passage.ps1`), not double-registered.

**Inactive — already-applied one-off migrations, not live functionality (excluded from this test
plan, listed for completeness):** `prose_first_layer_build_v1_20260824`,
`prose_change_log_build_v1_20260824`, `prose_add_edit_rules_build_v1_20260826`,
`prose_orphan_enum_fix_v1_20260826`, `flag_management_build_v1_20260823`.

**Inactive — dormant historical scripts from the old per-word Session A/B/C/D pipeline, not part
of the live prose module (excluded, listed for completeness):**
`scripts/_apply_file_chapter_lexical_prose_v1_20260702.py`,
`scripts/_apply_file_passage_lexical_prose_v1_20260704.py`,
`scripts/_apply_file_ruthlessness_lexical_prose_20260702.py`,
`scripts/_apply_file_synthesis_prose_v1_20260703.py`,
`scripts/_apply_prose_programme_chapter01.py`,
`scripts/_export_prose_to_md_v1_20260703.py`,
`scripts/_probe_primary_span_prose_reference_v1_20260705.py`,
`scripts/build_corpus_prose.py`, `scripts/build_session_a_prose.py`,
`scripts/_apply_d6_capture_contributor_source.py`, `query_db.py`.

**Conclusion: there is exactly one PS script for prose — `Prose.ps1`, 7 steps.** Testing all 7
steps exercises every line of `prosestore.py` that's actually live; the 4 legacy CLI scripts run
the identical code underneath, so are not separately tested below unless you want the raw-Python
entry point exercised too (noted per-step where relevant).

## b) Test plan — the literal `Prose.ps1` script layout, step by step

**Full current parameter set, quoted directly from the script** (`iba/app/ps/Prose.ps1`):

```
-Step         Extract | Search | ExportChapter | ImportChapter | Flag | FlagFixPropose | FlagFixApply   [required]
-Book         book_label (Extract/ExportChapter)
-Chapter      chapter number (Extract/ExportChapter, combine with -Book)
-TypeId       single prose_section_type.id (ExportChapter, instead of -Book/-Chapter)
-IncludeBody  include full prose body text in the JSON extract (Extract)          [switch]
-AlsoMarkdown also emit a readable Markdown view (Extract)                        [switch]
-AlsoDocx     also emit a readable .docx view (Extract)                           [switch]
-Query        search text (Search)
-Limit        result cap (Search); default: prose.search_default_limit
-Fts          treat -Query as a raw SQLite FTS5 MATCH expression (Search)         [switch]
-InputFile    path to an edited chapter Markdown file (ImportChapter)
-Author       patch author, default 'researcher' (ImportChapter)
-FlagCode     one of the live PROSE_QUALITY flag_code values (Flag/FlagFixPropose/FlagFixApply)
-Description  the issue, in prose — required (Flag)
-Find         literal substring to search prose body for (FlagFixPropose)
-Replace      literal replacement text (FlagFixPropose)
-ProposalFile path to a FlagFixPropose report .json (FlagFixApply)
-SectionIds   comma-separated prose_section.id list, approved from the report (FlagFixApply)
-Out          output path override (all steps)
-Trace        print every config read (IBA_TRACE)                                [switch]
```

Live values you can use in the tests below (pulled fresh, not placeholders):
**Books** — `Programme` / `Detail design` / `Findings` / `Essays`. **A real `-TypeId`** — `1`
(`sa_s1_d1`, "Session A — Word Summary"). **Live `-FlagCode` values** — `Terminology change` /
`Methodology change` / `Style change`. **A real `prose_section.id`** — `27` ("An anchor verse is
the canonical citatio...").

Run each test from the project root (`C:\Bible_study_projects`). Each entry: the exact command,
what to look for, and what already-known behaviour it should reproduce (from this session's own
live testing, so you have something to compare your result against).

---

### Test 1 — `Extract`

```powershell
iba\app\ps\Prose.ps1 -Step Extract -Book Programme -AlsoMarkdown
```
**Expect:** writes a `.json` (+ `.md` from `-AlsoMarkdown`) under
`Workflow\Programme\programme_prose\`. Message reports a type/section count — last observed 51
types, 51 sections for `Programme`.

```powershell
iba\app\ps\Prose.ps1 -Step Extract -Book "Detail design"
```
**Expect:** a different, larger count (last observed 45 types, 169 sections) — and this book
should include type id 78 (`prog_purp_observations_framework`); `Programme`'s extract should not.

```powershell
iba\app\ps\Prose.ps1 -Step Extract -Book "NotARealBook"
```
**Expect:** clean rejection listing the 4 real book choices — not a crash.

---

### Test 2 — `Search`

```powershell
iba\app\ps\Prose.ps1 -Step Search -Query grace -Book Programme
```
**Expect:** a results file under `outputs\markdown\`, at least 1 hit (last observed: 1).

```powershell
iba\app\ps\Prose.ps1 -Step Search -Query grace -Fts
```
**Expect:** treats `grace` as a raw FTS5 MATCH expression (no `-Book` filter this time) — try an
FTS operator too, e.g. `-Query "grace NOT works"`.

---

### Test 3 — `ExportChapter`

```powershell
iba\app\ps\Prose.ps1 -Step ExportChapter -Book Programme -Chapter 0
```
**Expect:** an editable `.md` written to `outputs\markdown\prose-edits\`, named
`prose-edit-programme-chapter-0-v{n}-{date}.md` — `{n}` increments on every re-export of the same
book/chapter, never reuses a number. Open the file: near the top you should see a
`<!-- PROSE_EXPORT_SECTION_IDS: ... -->` marker line (added 2026-08-26, escalation #890 D3) — this
is what makes test 4's delete-detection possible.

```powershell
iba\app\ps\Prose.ps1 -Step ExportChapter -TypeId 1
```
**Expect:** exports by a single `prose_section_type.id` instead of book/chapter — a narrower
export.

---

### Test 4 — `ImportChapter` (round-trip with test 3's export)

**4a — re-import unchanged:**
```powershell
iba\app\ps\Prose.ps1 -Step ImportChapter -InputFile outputs\markdown\prose-edits\<the file from test 3>.md
```
**Expect:** refused — `"no changed sections... nothing to import"` — file left in place, not
archived.

**4b — edit one section, then import:** open the export from test 3, change the text under one
`##` heading (leave every `<!-- PROSE_... -->` marker line untouched), save, then run the same
command as 4a. **Expect:** succeeds — writes a patch to `Sessions\Patches\`, archives your edited
file to `outputs\markdown\prose-edits\archive\`. **Do not apply the generated patch** unless you
actually want that content change live (apply via
`python scripts\apply_session_patch.py <the patch file>`, `--dry-run` first).

**4c — delete-detection (escalation #890 D3):** export a fresh chapter (test 3 again), open it,
delete one entire section block (from its `<!-- PROSE_SECTION_ID: N -->` line down to the `---`
that ends it), save, then import. **Expect:** refused —
`"N section(s) [id] present in this file's original export are missing from it now"` — file left
in place, nothing written. (Confirmed live this session, id 4 on a Programme chapter-1 export.)

---

### Test 5 — `Flag` (angle a — writes directly, the one step that does)

```powershell
iba\app\ps\Prose.ps1 -Step Flag -FlagCode "Terminology change" -Description "TEST -- delete this row after"
```
**Expect:** a new `wa_data_quality_flags` row, message reports its `id`. **Clean up after**: this
writes directly, so either delete the test row yourself
(`DELETE FROM wa_data_quality_flags WHERE id=<the id>`) or leave it and tell me to.

```powershell
iba\app\ps\Prose.ps1 -Step Flag -FlagCode "Not a real code" -Description "test"
```
**Expect:** clean rejection listing the 3 real live codes — not a crash.

---

### Test 6 — `FlagFixPropose` (angle b, propose — no DB write)

```powershell
iba\app\ps\Prose.ps1 -Step FlagFixPropose -FlagCode "Terminology change" -Find "Session A" -Replace "the Base_data stage"
```
**Expect:** writes a `.json` report under `outputs\markdown\` listing every section containing
"Session A" (last observed live: 17 matches), each with its proposed replacement text. No DB
write, no patch file yet.

---

### Test 7 — `FlagFixApply` (angle b, apply — generates a patch, no DB write)

```powershell
iba\app\ps\Prose.ps1 -Step FlagFixApply -ProposalFile <the report from test 6>.json -SectionIds 10 -FlagCode "Terminology change"
```
**Expect:** generates a `PROSE` supersede patch under `Sessions\Patches\` for section 10 only.
**Do not apply it** unless you actually want "Session A" → "the Base_data stage" live in that
section — this is real content, not throwaway (only the *mechanism* was tested live this session,
not applied to real prose).

```powershell
iba\app\ps\Prose.ps1 -Step FlagFixApply -ProposalFile <same report>.json -SectionIds 999999 -FlagCode "Terminology change"
```
**Expect:** clean refusal — `"section id(s) [999999] are not in the proposal file"`.

---

## Sequencing note

Tests 1/2/5b/6/7b are fully independent and safe to run in any order, any number of times — none
of them write anything that needs cleanup (test 5a is the one exception: it's a real write, clean
up the test row after). Tests 3/4a/4c are also safe (export + refused import, nothing written).
**Test 4b and a real `FlagFixApply` (test 7a) are the only two that can end in a patch you might
actually apply** — treat generating the patch as safe/repeatable, but stop before running
`apply_session_patch.py` on it unless the content change is one you actually want.

---

*No escalation action taken beyond raising #908 — this is the deliverable it asked for.*
