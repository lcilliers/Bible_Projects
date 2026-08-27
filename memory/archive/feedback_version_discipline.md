---
name: Version discipline — never delete or overwrite a prior version
description: Same base name = version bump (CLAUDE.md §9.4). Applies to ALL versioned files — instructions, reports, extracts. Never `rm` a prior version before regen.
type: feedback
originSessionId: 0b9d95eb-ab3c-4fd3-9dd9-6341794c07de
---
**Rule (CLAUDE.md §9.4):** "Same-name = version bump: if a file with the same base name already exists (regardless of date), the new file must carry an incremented `-v{n}` suffix. Never overwrite a prior version in place."

**Why:** Lapsed twice in this programme:
1. **2026-04-25** — edited `wa-versecontext-instruction-v3_5` and `wa-patch-instruction-v2_7` in place across multiple sessions (researcher caught it; reconstructed the chain from git history at commit `dc2b654`).
2. **2026-05-07** — `rm`d `wa-cluster-M05-comprehensive-v1-20260507.md` before regen so my script's `next_version` would emit "v1" again. Researcher caught it; the file was renamed to v2. The original v1 content (without the verse-stats section) was lost — git would have preserved it but I had not committed.
3. **2026-05-31** — overwrote `wa-programme-open-items-v1-20260531.md` (a hand-edited living register) ~6 times in place across one session via the Edit tool without ever bumping the version. Researcher could not verify which version they were reading. No script `next_version` helper applies to a hand-edited doc — that's the gap this clause now closes.

**How to apply — applies to ALL versioned files, not just instructions:**

1. **Before regenerating a report**, check what already exists at the destination path. If `{base}-v{N}-{date}.md` exists, the next run should produce v{N+1} — never v{N}.
2. **Never `rm` a prior version** to "make room" for a regen. The auto-version helpers in the scripts (`next_version()` / `next_version_in_dirs()`) do the right thing only when the prior file is left in place.
3. **Before editing an instruction document**, decide whether it is a minor-version bump (any update to a published doc) or a pre-publication fix (still in the same session as creation). Default to bump.
4. **For instructions:** copy the file to the new version filename, edit the new file, update internal Version/Filename/Supersedes/change-note fields, archive the predecessor in `Workflow/archive/`. Run `python scripts/_check_doc_versions.py` after.
5. **For reports:** let the script's `next_version` helper do the work. If the script doesn't have it, add it before generating.
6. **Archive superseded versions promptly.** For instructions, move to `Workflow/archive/`. For reports, leave in place — they form the version history in the same folder.
7. **For hand-edited LIVING documents (registers, design/methodology plans, working notes) — REVISED 2026-05-31:** do **NOT** filename-version them. Use a **single stable filename** (no `-vN`, no date in the name), put the version in the **metadata header** (`Doc version:` integer + `Last updated:` date), and let **git** be the history/rollback (`git log --follow`, `git show <rev>:<file>`). **No `archive/` copies.** Increment Doc version + Last updated per review-handback (not per keystroke). Codified in docs/file-organisation-rules.md **§2.3a**. This supersedes the earlier "copy to `-v{N+1}` + archive" approach for living docs (which churned archive copies and broke every cross-reference on each bump — the 2026-05-31 lapse #3 was the trigger to redesign). Reconciles with [[feedback_single_living_register]]: one stable file = the single source of truth; versioning is metadata, not new files.

**Snapshot vs living — which rule applies:**
- **Snapshot deliverables** (reports, extracts, instruction docs, anything referenced/pinned at a point in time): filename `-vN` versioning + archive prior (rules 1–6 above, file-org §2.3).
- **Living documents** (continuously edited in place): stable filename + metadata version + git (rule 7, file-org §2.3a).
A doc is "living" if it is expected to keep changing in place; "snapshot" if its value is being a fixed record of a moment.

**Don't:**

- ❌ `rm` the prior version before regen.
- ❌ Edit a published instruction document in place.
- ❌ Add multiple "addendum 2 / addendum 3" entries under the same version number — each addendum is its own minor version.
- ❌ Skip `_check_doc_versions.py` for instruction-doc edits because the change feels small.

**Recovery if I do violate this:** rename the new file to the next sequence number (e.g. v1 → v2 if v1 originally existed), note the loss in the response, and update the memory with another lapse incident.
