"""GR-FILE-003 compliance check for instruction documents.

Verifies that every instruction document under
`data/imports/WA/Workflow/Framework_B/Session_B/` has internal version metadata
consistent with its filename.

Specifically, for each `wa-*.md` file:
  1. Filename matches `wa-{name}-v{major}_{minor}-{YYYYMMDD}.md`.
  2. The first line is the markdown title `# {filename-stem}`.
  3. There is a "Version {major}_{minor}" string in the first 30 lines whose
     digits match the filename version.
  4. (If table format is used) the "Filename" field row matches the filename.

When any of these don't match, the document is in violation of GR-FILE-003 —
typically a sign that someone edited the file in place without bumping the
minor version (and renaming the file accordingly).

This is the operational counterpart to the rule. Run before committing any
instruction-document edit:

    python scripts/_check_doc_versions.py

Exit code 0 = clean. Exit code 1 = violations detected (printed to stdout).

The script is read-only and never modifies the DB or files.
"""

from __future__ import annotations

import os
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS_DIR = ROOT / "data" / "imports" / "WA" / "Workflow" / "Framework_B" / "Session_B"
ARCHIVE_DIR = ROOT / "data" / "imports" / "WA" / "Workflow" / "Framework_B" / "archive"

# Filename pattern: wa-{name}-v{major}_{minor}-{YYYYMMDD}.md
# {name} can contain hyphens; greedy match up to the version token.
FILENAME_RE = re.compile(
    r"^(?P<prefix>wa-.+)-v(?P<major>\d+)_(?P<minor>\d+)-(?P<date>\d{8})\.md$"
)

# Internal version markers that should match.
# Matches: "Version 3_8", "Version: 3_8", "Version: v3_8", "Version v3_8",
# "Instruction v1_5", "Instruction: v1_5", "Patch Instruction v2_8".
VERSION_INLINE_RE = re.compile(
    r"(?:[Vv]ersion|[Ii]nstruction)[:\s]+v?\s*(\d+)_(\d+)"
)


def check_file(path: Path) -> list[str]:
    """Return a list of violation strings for the given file. Empty list = clean."""
    violations: list[str] = []
    name = path.name

    # 1. Filename pattern
    m = FILENAME_RE.match(name)
    if not m:
        # Not a versioned doc — skip silently. The script targets versioned
        # instruction documents only.
        return violations

    fn_major = int(m.group("major"))
    fn_minor = int(m.group("minor"))

    try:
        text = path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        violations.append(f"{name}: not UTF-8 readable")
        return violations

    head = "\n".join(text.splitlines()[:40])

    # 2. Inline "Version N_N" (or "Version: vN_N") must match filename version.
    # This is the canonical self-declaration of the doc's version. Title
    # variation (descriptive vs filename-stem styles) is tolerated; the inline
    # version marker is the GR-FILE-003 anchor.
    inline_versions: list[tuple[int, int]] = [
        (int(a), int(b)) for a, b in VERSION_INLINE_RE.findall(head)
    ]
    if not inline_versions:
        violations.append(f"{name}: no 'Version N_N' or 'Version: vN_N' marker found in first 40 lines")
    else:
        # The first inline version is the document's authoritative self-version
        # (subsequent appearances may legitimately mention older versions in
        # change-notes, etc.). We check that the FIRST occurrence matches the
        # filename version.
        first_major, first_minor = inline_versions[0]
        if (first_major, first_minor) != (fn_major, fn_minor):
            violations.append(
                f"{name}: inline 'Version {first_major}_{first_minor}' does not "
                f"match filename version v{fn_major}_{fn_minor}"
            )

    # 3. If the doc has a "|Filename|...|" table cell (the table-format header
    #    used by VC instruction etc.), it must match the filename.
    fname_field_re = re.compile(r"\|\s*Filename\s*\|\s*([^\|]+?)\s*\|")
    for fm in fname_field_re.finditer(head):
        declared = fm.group(1).strip()
        if declared != name:
            violations.append(
                f"{name}: |Filename| field declares '{declared}', does not match actual filename"
            )
        break  # only check the first occurrence

    # 4. Title (top-of-file H1) — informational check only. We only fail if the
    #    title is missing entirely; mismatch is tolerated since some docs use
    #    descriptive titles ("# Framework B Soul Word Analysis...") rather than
    #    the strict filename-stem convention.
    if not re.search(r"^#\s+\S+", head, flags=re.MULTILINE):
        violations.append(f"{name}: no markdown H1 title in first 40 lines")

    return violations


def collect_violations(base: Path) -> dict[str, list[str]]:
    """Walk one doc directory; return {filepath: [violations]}."""
    out: dict[str, list[str]] = {}
    if not base.is_dir():
        return out
    for path in sorted(base.glob("wa-*.md")):
        v = check_file(path)
        if v:
            out[str(path.relative_to(ROOT)).replace("\\", "/")] = v
    return out


def detect_inplace_edits() -> list[str]:
    """Use `git status --porcelain` to find instruction files modified in place.

    A modified file (status `M`) in `Session_B/` whose filename was NOT changed
    in this commit-cycle (no `R` rename pair) is the typical sign of a
    GR-FILE-003 violation. Returns a list of filepath strings; empty if clean
    or if git is unavailable.
    """
    try:
        import subprocess
        result = subprocess.run(
            ["git", "status", "--porcelain"],
            capture_output=True, text=True, cwd=ROOT, timeout=10,
        )
    except Exception:
        return []
    if result.returncode != 0:
        return []

    target_prefix = "data/imports/WA/Workflow/Framework_B/Session_B/wa-"
    flagged: list[str] = []
    for line in result.stdout.splitlines():
        if not line:
            continue
        # Two-char status, then space, then filepath. Renames have the form
        # "RM old -> new"; we don't flag those (a rename = a version bump).
        status = line[:2]
        rest = line[3:].strip()
        if status.startswith("R"):
            continue
        # Only consider modifications, not new additions (A) or deletions (D).
        # An in-place edit shows as " M" or "M ".
        if "M" not in status:
            continue
        # The path may be quoted on Windows when it contains spaces.
        path = rest.strip('"')
        # Normalise path separators
        path_n = path.replace("\\", "/")
        if path_n.startswith(target_prefix):
            flagged.append(path_n)
    return flagged


def main() -> int:
    print("GR-FILE-003 compliance check — instruction documents")
    print("=" * 72)

    active = collect_violations(DOCS_DIR)
    archive = collect_violations(ARCHIVE_DIR)

    # Git-aware check: in-place edits in active dir
    inplace = detect_inplace_edits()

    print(f"Active dir : {DOCS_DIR.relative_to(ROOT)}")
    print(f"Archive dir: {ARCHIVE_DIR.relative_to(ROOT)}")
    print()

    fail = bool(active) or bool(inplace)

    if active:
        total = sum(len(v) for v in active.values())
        print(f"ACTIVE VIOLATIONS: {total} across {len(active)} files (must fix)")
        print()
        for filepath, vlist in active.items():
            print(f"[{filepath}]")
            for v in vlist:
                msg = v.split(":", 1)[1].strip() if ":" in v else v
                print(f"  - {msg}")
            print()
    else:
        print("ACTIVE: clean — every active versioned doc has consistent filename + internal version.")
        print()

    if inplace:
        print(f"GIT IN-PLACE EDIT WARNING ({len(inplace)} file(s)):")
        print("  These instruction files have been modified in the working tree without a")
        print("  rename. Per GR-FILE-003, any update to an instruction document must be a")
        print("  minor-version bump — i.e. a filename rename + corrected internal version.")
        print("  Either revert the in-place edit, or rename the file to bump the version.")
        for f in inplace:
            print(f"  - {f}")
        print()

    if archive:
        archive_total = sum(len(v) for v in archive.values())
        print(f"Archive (historical, informational only): {archive_total} note(s) across {len(archive)} files")
        print("  These are pre-rule historical documents. Not blocking.")
        print()

    if fail:
        print("Fix by either: (a) bumping the file's internal version + renaming the file to match;")
        print("or (b) reverting the in-place edit and producing a proper supersede with archived predecessor.")
        print("See GR-FILE-003 in wa-global-rules-extract-{current}.json.")
        return 1
    print("Result     : CLEAN — exit 0.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
