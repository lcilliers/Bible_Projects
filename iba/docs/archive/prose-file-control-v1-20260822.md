# Prose file control — the write process (v1)

**Escalation #784.** Requested directly: file/filing control for the prose write process needs to
be thought through deep — naming, location, archiving, files being worked on, support material —
because the whole rewrite effort is going to run through `.md` files. This is a design analysis, not
a build — same status as everything else parked on #784 for detail design.

---

## 1. The one finding that should drive this design

Before naming/location/archiving rules, one thing found by tracing the actual code (not assumed
from the architecture doc's prose) changes what "control" has to mean here:

**The existing documentation says the edit `.md` file is disposable. The code makes it permanent.**

> "Temporary edit files may be discarded after the patch has been reviewed and applied."
> (`docs/prose-store-architecture.md` §8.1)

But `run_import_chapter` (`iba/app/lib/prosestore.py:639`) writes the edit file's own path into
the **database row it produces**, as `prose_section.source_file` — permanently, as part of the
content's own provenance record, not as a transient log line:

```python
"record": {
    "body": block["BODY"], "heading": row["heading"], "author": author,
    "status": "draft", "source_file": str(input_path).replace("\\", "/"),
    ...
```

Once a patch built from an edit file is applied, that file's path is baked into the live
`prose_section` row forever (until the row is next superseded). Discard the file per the
architecture doc's own instruction, and `source_file` becomes a dead pointer — the DB says where
the content came from, and there's nothing there. This is a real conflict between what's documented
and what the code actually does, not a hypothetical — worth fixing the instruction, not the code
(the permanence is correct: it's real provenance, the same discipline the rest of the programme
applies everywhere else — "every finding is substantiated by data," per the very Chapter 3 read
earlier this session).

**Consequence:** an edit file's disposability depends entirely on whether it was ever successfully
imported. That single fact is the spine of everything below.

---

## 2. The lifecycle of one edit file — five states, one branch

```
 EXPORTED ──edited──> IN EDIT ──imported──> PATCH PENDING ──applied──> PERMANENT (never discard)
    │                                            │
    └──never imported, abandoned──> STALE DRAFT ─┴──rejected──> back to IN EDIT (or abandoned)
```

| State | What's true | Safe to discard? |
|---|---|---|
| **Exported** | Fresh `.md` from `run_export_chapter`, matches DB exactly, no edits yet | Yes — regenerable on demand, nothing depends on it |
| **In edit** | Body text below the markers has been changed; markers untouched | Yes, if abandoned — nothing outside the file knows it exists yet |
| **Patch pending** | `run_import_chapter` has validated it and written a patch to `Sessions/Patches/`; patch not yet applied | **No** — the patch's `_patch_summary.source_edit_file` already names this exact path; discarding it now orphans a pending patch |
| **Permanent** | The patch has been applied; `prose_section.source_file` on the new row now names this file | **Never delete. Archive only.** This is provenance, not scratch work, from this point on. |
| **Stale draft** | Exported, edited or not, but never imported — superseded by a fresher export of the same chapter | Yes — same content is derivable again from the DB; nothing references this specific file |

This is the actual test for every rule below: **has this file's path been written into a patch or a
database row yet?** Before that point, it's scratch work. After, it's a record.

---

## 3. Naming — mostly right, one real gap found live this session

Current pattern (`prosestore.py:582`): `prose-edit-{book}-chapter-{n}-{YYYYMMDD}.md`. Matches the
general project convention (`docs/file-organisation-rules.md` §2.1: lowercase, hyphens, compact
date) in every respect but one.

**Gap, observed directly today, not theoretical:** there's no `-v{n}-` component. When today's path
fix was tested, re-running the chapter 2 export **silently overwrote** the file already produced
earlier the same day — no version bump, no archive of the prior copy. `docs/file-organisation-rules.md`
§2.3 states the project's own general rule directly: *"Same-day revisions: Increment the version
number... Only the latest version of a file remains in its active folder."* The chapter-edit export
doesn't follow its own project's rule.

Whether this matters depends on §1's finding: an **exported** (not-yet-imported) file being silently
overwritten same-day is harmless — it's regenerable, nothing points at the old copy. But once a file
reaches **patch pending** or **permanent**, an overwrite is a real problem — it would change the
content behind a `source_file` pointer that a patch or a database row already names. The fix isn't
necessarily "add `-v{n}-` to every export" (that's `feedback_simple_steps_not_engineered_designs`
territory if applied blindly) — it's specifically: **don't silently overwrite a file that a pending
patch or a live `prose_section.source_file` already references.** A same-day re-export of a chapter
that already has a patch pending against its prior export should refuse or version, not clobber.

---

## 4. Location — fixed this session, still needs writing down somewhere authoritative

`outputs/markdown/prose-edits/` is now correct in code (this session's earlier fix). It is **not
documented anywhere** — not in `docs/prose-store-architecture.md`, not in
`docs/file-organisation-rules.md` (which doesn't mention prose at all, anywhere, despite covering
dozens of other file types in detail). The convention existed only as lived practice until you named
it from memory.

**Genuine question, not decided here:** where should this rule actually live? Two real options, both
consistent with things already established this session:

- **Add it to `docs/file-organisation-rules.md`** — the existing, general-purpose home for exactly
  this kind of rule. Consistent with how every other file type in the project is governed.
- **Make it a `cfg_prose` setting** (or similar) — consistent with `governance.oneoff_report_dir`
  already doing exactly this (config-driven output location) for one-off reports, and consistent
  with this session's own earlier correction that prose's per-module config belongs in a real
  per-module table, not scattered documentation. This would also make the location genuinely
  enforced (code reads the config) rather than documented-and-hopefully-followed.

Given `docs/file-organisation-rules.md` itself is written for the pre-IBA/pre-reset file structure
in most of its sections (Session A–D folders, `Sessions-v2/`, `verse-analysis/` — much of it likely
carries the same staleness problem the prose books themselves have), and given the project's clear
direction this session (config governs, documents describe), **the config-driven option looks like
the better fit** — but this is a real design choice with a real cost (a markdown doc is free to
write, a config table needs the `configmaint.propose` build cycle), so it's named here, not decided.

---

## 5. Archiving — the gap that matters most, tied directly to §1

Nothing currently archives an edit file once it reaches **permanent** (§2). `apply_session_patch.py`
already archives the **patch** itself on success (`archive/patches/`, per
`docs/file-organisation-rules.md` §4 and confirmed in `docs/prose-store-architecture.md` §7) — but
nothing extends that same trigger to the **edit file the patch was built from**. The patch's own
`_patch_summary.source_edit_file` already names the exact path — the information needed to do this
is already sitting in every prose patch, unused.

**The natural fix, once this is built:** the same moment a `PROSE`-type patch is successfully
applied, also move its `source_edit_file` into an archive folder alongside it —
`outputs/markdown/prose-edits/archive/`, mirroring the exact pattern
`docs/file-organisation-rules.md` §4 already uses everywhere else ("New version of a file produced →
move prior version to `archive/` subfolder within the file's directory"). Not a new policy — the
existing one, just not yet wired to this specific file type. `prose_section.source_file` keeps
pointing at the same relative path either way, since archiving *moves* the file rather than deleting
it — worth confirming that assumption holds (an archived file's relative path changes, so
`source_file` would need to record the archive-relative path, or archiving would need to preserve
the original relative path some other way — a real detail to settle at build time, not glossed over
here).

**Stale drafts** (exported or edited, never imported) are the cheap case — nothing references them,
so `governance.redundancy_archiving`'s existing rule ("one-off artifacts no longer in use... archived
on a daily basis") already covers them in principle. In practice it isn't happening: this session
found 2026-08-14 and 2026-08-21 exports still sitting unarchived when this thread started, over a
week old. Worth noting as a live instance of an already-stated rule not being followed, not a new
rule needed.

---

## 6. "Files being worked on" — visibility, not a fourth mechanism

Right now there is no way to see which chapters currently have work in flight — exported-but-not-
imported, or imported-and-patch-pending — except by reading filenames and dates in the folder by eye.
At the scale being planned for (thousands of sections), that stops being workable.

**This doesn't need a new mechanism.** It's the same shape as the prose-change-flag idea already
being designed this session (v22/v23, reusing `wa_quality_flag_types`/`wa_data_quality_flags`): a
flag raised when a chapter enters edit, cleared when its patch applies. Building a separate
"in-flight" tracker alongside that would be exactly the kind of parallel plumbing already ruled out
for the change-flag design — this is a second use of the same table shape, not a third concept.
Flagging the connection now so detail design doesn't reinvent it separately.

---

## 7. Support material — no new rule needed, existing convention already holds

This thread's own design output (`prose-management-iba-v1`/`v2`, `prose-store-iba-incorporation-
plan-v4`, this document) already lives in `iba/docs/`, correctly, per
`governance.engineering_documentation_folder`. That convention is doing its job for prose *design*
material. Prose *content* material (edit files, patches) has its own separate, now-corrected
locations (§4/§5 above). No gap found here — stated for completeness, not because anything needs
fixing.

---

## 8. Summary — what's settled vs. what's a real decision

**Settled (applying existing rules, not new judgement calls):**
- The permanence finding (§1) — a fact about the code, not a choice.
- Archiving imported edit files alongside their patch, on the same trigger (§5) — the project's own
  existing archiving pattern, just extended to a file type it was never wired to.
- Reusing the change-flag mechanism for in-flight visibility rather than a new one (§6) — avoids
  duplicate plumbing already ruled out once this session.

**Real decisions, not made here:**
- Where the location rule itself gets written down — `file-organisation-rules.md` vs. a `cfg_prose`
  setting (§4).
- Whether same-day overwrite protection applies only from "patch pending" onward, or to every export
  (§3) — and what "refuse vs. version" should actually do when triggered.
- The archived-path / `source_file` interaction once archiving is built (§5) — needs settling before
  building, not glossed over.

---

## 9. Update 2026-08-22 — §3 and §5 built and tested, per researcher direction

Researcher resolved both open items directly: *"all files must be version controlled"* and
*"the import must get the file from the editing location, and on succesful update move the file to
archive"* — plus named the concrete symptom (*"the name of the file makes it impossible to link the
file with the book-chapter-session"*), read as the missing version number, since book+chapter were
already in the name but nothing distinguished repeat edits of the same one.

**Built** (`iba/app/lib/prosestore.py`): `run_export_chapter` now names every export
`{stem}-v{n}-{date}.md` where `{n}` is scanned across both the active folder and its archive, so a
version is never reused even after archiving; the stem itself now covers all three shapes
(book+chapter, book+section when there's no chapter, and the unbooked-section fallback). Testing
this live also surfaced §5's "archived-path vs. `source_file`" open question and settled it:
`run_import_chapter` computes the archive destination *before* building the patch, uses that
archived path (not the pre-move path) as `prose_section.source_file`, writes the patch, then moves
the file — so the DB's own provenance pointer is correct from the moment the patch is generated,
never a dangling reference even briefly.

**Tested live** (throwaway artifacts only, cleaned up after — no real content touched, DB
`prose_section` max id unchanged at 1040 throughout):

| Case | Result |
|---|---|
| Export chapter 2 twice in a row | `...chapter-2-v1-...md`, then `...chapter-2-v2-...md` — no overwrite |
| Export a single type-id that has a book+chapter (id 52, in Programme ch. 3) | Correctly used the chapter stem, not the section stem |
| Export a single type-id with no book at all (`src_logos`, id 101) | `prose-edit-unassigned-book-section-src_logos-v1-...md` — the fallback path works |
| Import an unedited export, unapplied | Patch generated; file physically moved from `prose-edits/` to `prose-edits/archive/`; patch's `source_file` and `source_edit_file` both correctly point at the *archived* path, confirmed by reading the written JSON, not assumed |

Also corrected `docs/prose-store-architecture.md` §8.1, which still said edit files "may be
discarded" — now states the permanence + auto-archive behaviour and points here.

**Not built / still open:** §4's location-rule placement (doc vs. `cfg_prose`) and §6's in-flight
visibility (folding into the prose-change-flag mechanism) — unchanged, still parked for detail
design.

---

## 10. Update 2026-08-22 (same day, cont.) — the section is the editing unit, not the chapter

Researcher correction, verbatim: *"chapter number are not unique across prose. each chapter can
have multiples sections. the sections is the editing unit. if a chapter export is exported then all
the sessions [sections] n the chapter will have to changfe version wich is not necessary. so book
exports and edit exports is not the same thing and is used differently."*

**Real bug this surfaced, confirmed by re-reading the code, not by inference:** `run_import_chapter`
built a `supersede` operation for **every** section block found in the edit file, unconditionally —
`ps.body` wasn't even in the row query, so nothing was ever compared. Re-exporting a 7-section
chapter to fix one typo and importing it back **would have superseded all 7 sections**, bumping
every one's `version` even though 6 had no change at all. Confirmed directly: today's own
first import test (§9) was run completely unedited and still generated 7 supersede operations —
harmless only because that patch was never applied.

**Fixed:** `run_import_chapter` now fetches `ps.body` and skips any block whose text matches the
current row exactly (normalised by `.strip()`, matching how export writes and import parses body
text). Only sections that actually changed get superseded. If a whole import has zero changed
sections, the function now refuses outright (*"nothing to import"*) and — correctly — leaves the
file in place rather than archiving it: an unedited export is still a disposable draft (§2's own
lifecycle table), not provenance for anything yet.

**"Book exports and edit exports... used differently"** — confirmed already true in the code
structure, not conflated: `run_extract` (whole-book/chapter JSON/MD/DOCX, no markers, read-only,
`Workflow/Programme/programme_prose/` + `outputs/docx/`) and `run_export_chapter` (marker-bearing,
round-trip-editable, `outputs/markdown/prose-edits/`) were already two separate functions with
separate output locations before today — the correction is stated here so the distinction stays
explicit going forward, not because anything needed un-conflating.

**"Chapter number are not unique across prose"** — checked: the export stem already includes
`book_label`, so two same-numbered chapters in different books (e.g. `Programme` ch. 3 vs. some
other book's ch. 3) already produce different filenames. Not a gap found in this pass; noted as
confirmed, not assumed.

**Tested live** (same throwaway-and-clean-up discipline as §9): exported chapter 2 fresh; imported
it completely unedited — correctly refused, file left in place, confirmed still present afterward;
edited exactly one of its 7 sections' body text and re-imported — patch generated with **1**
operation, not 7, `supersedes_id` matching the edited section, `source_file` pointing at the
archived path; file correctly archived (only on the real-change path, confirmed by checking both
locations before and after).
