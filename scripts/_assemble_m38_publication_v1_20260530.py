"""Assemble M38 published book from chapter drafts + appendices.

Reads each draft file, strips per-chapter scaffolding (frontmatter, cross-chapter
profile line, EVIDENCE blocks, sub-group descriptions), concatenates into a
single MD book, and renders to DOCX.
"""
from __future__ import annotations
import re, sys
from pathlib import Path

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

CLUSTER = "M38"
DATE = "20260530"
PUB_DIR = Path(f"Sessions/Session_Clusters/{CLUSTER}/publishing")
INPUTS_DIR = Path(f"Sessions/Session_Clusters/{CLUSTER}/inputs")

CHAPTERS = [
    ("ch1", "20260530"),
    ("ch2", "20260529"),
    ("ch3", "20260529"),  # v2
    ("ch4", "20260529"),
    ("ch5", "20260530"),
    ("ch6", "20260530"),
    ("ch7", "20260530"),
    ("appa", "20260530"),
    ("appb", "20260530"),
    ("appc", "20260530"),
]


def get_draft_path(ch_key: str, date: str) -> Path:
    """Get the draft path, preferring v2 over v1 if present."""
    v2 = PUB_DIR / f"wa-cluster-{CLUSTER}-{ch_key}-draft-v2-{date}.md"
    v1 = PUB_DIR / f"wa-cluster-{CLUSTER}-{ch_key}-draft-v1-{date}.md"
    return v2 if v2.exists() else v1


def strip_scaffolding(text: str) -> str:
    """Strip the per-chapter file header + per-section evidence scaffolding."""
    lines = text.splitlines()
    # Drop the H1 + H2 + frontmatter block (Cluster: ... through the first ---)
    # Then drop the optional "Cross-chapter consistency" section.

    i = 0
    while i < len(lines) and not lines[i].strip().startswith("# "):
        i += 1
    if i < len(lines):
        i += 1
    while i < len(lines) and not lines[i].strip().startswith("## "):
        i += 1
    if i < len(lines):
        i += 1
    while i < len(lines) and lines[i].strip() != "---":
        i += 1
    if i < len(lines):
        i += 1
    while i < len(lines) and lines[i].strip() == "":
        i += 1
    if i < len(lines) and "Cross-chapter consistency" in lines[i]:
        while i < len(lines) and lines[i].strip() != "---":
            i += 1
        if i < len(lines):
            i += 1
    body = "\n".join(lines[i:]).strip()

    # Strip the per-section evidence scaffolding inherited from chapter 2 input:
    # - HTML EVIDENCE comment blocks
    # - "**Sub-group description (from analytical record):**" + the blockquote that follows
    # - "**Key verses for this characteristic:**" + the verse-block entries that follow,
    #   until the next section header (### N.M ...) or end of file.
    body = re.sub(
        r"<!-- EVIDENCE:.*?<!-- /EVIDENCE -->",
        "",
        body,
        flags=re.DOTALL,
    )

    # Strip "Sub-group description" blocks: header + blockquote paragraph
    body = re.sub(
        r"\*\*Sub-group description \(from analytical record\):\*\*\s*\n+>.*?(?=\n\n[^>]|\Z)",
        "",
        body,
        flags=re.DOTALL,
    )

    # Strip "Key verses for this characteristic:" sections up to next ### header
    body = re.sub(
        r"\*\*Key verses for this characteristic:\*\*.*?(?=\n###|\Z)",
        "",
        body,
        flags=re.DOTALL,
    )

    # Collapse multi-blank-line runs
    body = re.sub(r"\n{3,}", "\n\n", body)
    return body.strip()


def extract_appb_table_from_input() -> str:
    """Read the appB input file and extract the verse table."""
    appb_input = INPUTS_DIR / f"wa-cluster-{CLUSTER}-appb-input-v1-20260529.md"
    text = appb_input.read_text(encoding="utf-8")
    # Find the table: starts at first line beginning with '|', ends at first blank line after
    lines = text.splitlines()
    table_lines: list[str] = []
    in_table = False
    for line in lines:
        if line.startswith("|"):
            table_lines.append(line)
            in_table = True
        elif in_table and not line.strip():
            break
    return "\n".join(table_lines)


def main():
    parts: list[str] = []
    parts.append("# Salvation, Redemption and Deliverance")
    parts.append("### A study of seven inner-life characteristics in Scripture")
    parts.append("")
    parts.append(f"**Programme reference:** {CLUSTER} — Salvation")
    parts.append(f"**Authored:** 2026-05-30")
    parts.append("")
    parts.append("---")
    parts.append("")

    for ch_key, date in CHAPTERS:
        path = get_draft_path(ch_key, date)
        if not path.exists():
            print(f"MISSING: {path}")
            continue
        text = path.read_text(encoding="utf-8")
        body = strip_scaffolding(text)

        # Insert appB verse table after the appB closing note
        if ch_key == "appb":
            table = extract_appb_table_from_input()
            # appB draft body has prose; insert the table after it
            body = body + "\n\n" + table

        parts.append(body)
        parts.append("")
        parts.append("---")
        parts.append("")
        print(f"Included: {path.name} ({len(body):,} chars)")

    parts.append("")
    parts.append(f"*Salvation, Redemption and Deliverance — A study of seven inner-life characteristics in Scripture. v1 — 2026-05-30.*")

    out_md = PUB_DIR / f"wa-cluster-{CLUSTER}-book-v1-{DATE}.md"
    out_md.write_text("\n".join(parts), encoding="utf-8")
    print()
    print(f"Wrote: {out_md} ({out_md.stat().st_size:,} bytes)")


if __name__ == "__main__":
    main()
