"""Assemble a Session C cluster publication from per-chapter drafts and emit a PDF.

For each chapter / appendix:
  - Reads the highest-version draft file from the source folder
  - Strips the per-file header (title + metadata + first separator)
  - Strips the trailing EVIDENCE-preservation marker
  - Concatenates with consistent spacing

Adds a title page and table of contents at the front. Writes both a master
Markdown file and a PDF.

Usage:
    python scripts/_assemble_cluster_publication_v1_20260512.py \\
        --cluster M15 \\
        --source "Sessions/Session_Clusters/M15/files published" \\
        --title "Wisdom, Understanding and Knowledge" \\
        --subtitle "A study of how Scripture treats the inner life of cognition, perception and word"
"""
import os, sys, re, argparse, glob
from datetime import datetime
from markdown_pdf import MarkdownPdf, Section
try: sys.stdout.reconfigure(encoding="utf-8")
except: pass


CHAPTER_DEFS = [
    ("ch1",  "1. What this study is"),
    ("ch2",  "2. The characteristics in this study"),
    ("ch3",  "3. The divine pattern"),
    ("ch4",  "4. Where each characteristic lives in the person"),
    ("ch5",  "5. How each characteristic works"),
    ("ch6",  "6. How each characteristic relates to the others"),
    ("ch7",  "7. The view from outside Scripture"),
    ("appa", "Appendix A — Terms in this study"),
    ("appb", "Appendix B — Key verses"),
    ("appc", "Appendix C — Method note"),
]


def find_highest_version(source_dir, cluster, key):
    """Find the highest -vN- file matching the pattern for this chapter key."""
    pattern = os.path.join(source_dir, f"WA-{cluster}-{key}-draft-v*-*.md")
    candidates = glob.glob(pattern)
    if not candidates:
        # case-insensitive search fallback
        all_files = glob.glob(os.path.join(source_dir, "*.md"))
        candidates = [f for f in all_files
                      if re.search(rf"-{key}-draft-v\d+-", os.path.basename(f), re.I)]
    if not candidates:
        raise SystemExit(f"No draft file found for {key}")

    def version_of(path):
        m = re.search(r"-v(\d+)-", os.path.basename(path))
        return int(m.group(1)) if m else 0

    return max(candidates, key=version_of)


def strip_header_and_footer(text, key):
    """Strip the per-file header block (up to first body section header) and the
    trailing EVIDENCE-preservation marker block."""
    lines = text.splitlines()

    # Find first body section header.
    # For chapters: the first `## N.` (where N is the chapter number)
    # For appendices: the first `## Appendix X`
    body_start = None
    for i, line in enumerate(lines):
        if key.startswith("ch"):
            chnum = key[2:]
            if re.match(rf"^##\s+{chnum}\.\s", line):
                body_start = i
                break
        elif key.startswith("app"):
            if re.match(r"^##\s+Appendix\s+[A-Z]", line):
                body_start = i
                break

    if body_start is None:
        # Fallback: skip past the first `---` separator after metadata
        sep_idx = next((i for i, l in enumerate(lines) if l.strip() == "---" and i > 5), None)
        body_start = (sep_idx + 1) if sep_idx is not None else 0

    # Find footer (EVIDENCE-preservation marker)
    footer_start = None
    for i in range(len(lines) - 1, -1, -1):
        if "EVIDENCE" in lines[i] and "preserved" in lines[i]:
            footer_start = i
            break
    if footer_start is not None:
        # Walk backwards through any blank lines and the separator `---` line
        while footer_start > 0 and (
            lines[footer_start - 1].strip() == "" or lines[footer_start - 1].strip() == "---"
        ):
            footer_start -= 1
    else:
        footer_start = len(lines)

    body = "\n".join(lines[body_start:footer_start]).rstrip() + "\n"
    return body


def build_toc(chapter_titles):
    out = ["## Contents\n"]
    for title in chapter_titles:
        out.append(f"- {title}\n")
    return "\n".join(out) + "\n"


def build_title_page(title, subtitle, date_str):
    return (
        f"# {title}\n\n"
        f"## {subtitle}\n\n"
        f"_{date_str}_\n\n"
        "---\n\n"
    )


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--cluster", required=True)
    ap.add_argument("--source", required=True, help="Folder containing draft files")
    ap.add_argument("--title", required=True)
    ap.add_argument("--subtitle", default="")
    ap.add_argument("--out-md", default=None)
    ap.add_argument("--out-pdf", default=None)
    args = ap.parse_args()

    code = args.cluster
    date_str = datetime.now().strftime("%Y-%m-%d")
    out_dir = f"Sessions/Session_Clusters/{code}"
    if args.out_md is None:
        args.out_md = os.path.join(out_dir, f"wa-cluster-{code}-publication-v1-{datetime.now().strftime('%Y%m%d')}.md")
    if args.out_pdf is None:
        args.out_pdf = args.out_md.replace(".md", ".pdf")

    print(f"Source folder: {args.source}")
    print(f"Output MD:     {args.out_md}")
    print(f"Output PDF:    {args.out_pdf}")
    print()

    # Discover highest-version drafts
    files = []
    chapter_titles = []
    for key, label in CHAPTER_DEFS:
        path = find_highest_version(args.source, code, key)
        ver = re.search(r"-v(\d+)-", os.path.basename(path)).group(1)
        print(f"  {key:5s} v{ver}  →  {os.path.basename(path)}")
        files.append((key, label, path))
        chapter_titles.append(label)

    # Assemble
    parts = [build_title_page(args.title, args.subtitle, date_str)]
    parts.append(build_toc(chapter_titles))
    parts.append("\n---\n\n")

    for key, label, path in files:
        with open(path, encoding="utf-8") as f:
            text = f.read()
        body = strip_header_and_footer(text, key)
        parts.append(body)
        parts.append("\n---\n\n")

    md = "".join(parts)
    md = re.sub(r"\n{3,}", "\n\n", md)  # collapse excess blank lines

    os.makedirs(os.path.dirname(args.out_md), exist_ok=True)
    with open(args.out_md, "w", encoding="utf-8") as f:
        f.write(md)
    print(f"\nWrote MD: {args.out_md}  ({len(md):,} chars, ~{len(md.split()):,} words)")

    # Build PDF — split into sections so the renderer applies page breaks
    pdf = MarkdownPdf(toc_level=2)
    css = """
    body { font-family: Georgia, 'Times New Roman', serif; line-height: 1.5; }
    h1 { font-size: 28pt; margin-top: 1.5em; }
    h2 { font-size: 18pt; margin-top: 1.2em; border-bottom: 1px solid #ccc; padding-bottom: 4px; }
    h3 { font-size: 14pt; margin-top: 1em; }
    h4 { font-size: 12pt; margin-top: 0.8em; }
    p  { text-align: justify; }
    blockquote { border-left: 3px solid #888; margin-left: 0; padding-left: 1em; color: #444; font-style: italic; }
    table { border-collapse: collapse; font-size: 9pt; }
    th, td { border: 1px solid #aaa; padding: 4px 6px; vertical-align: top; }
    th { background: #eee; }
    """

    # Split MD into sections at each `---` line so each major part gets a page break.
    # toc=True on every section so the PDF outline begins at the level-1 title.
    sections = re.split(r"\n---\n", md)
    for sec in sections:
        sec = sec.strip()
        if not sec:
            continue
        pdf.add_section(Section(sec + "\n", toc=True), user_css=css)

    pdf.meta["title"] = args.title
    pdf.meta["author"] = "Bible study project"
    pdf.save(args.out_pdf)
    print(f"Wrote PDF: {args.out_pdf}  ({os.path.getsize(args.out_pdf):,} bytes)")


if __name__ == "__main__":
    main()
