"""Reusable Markdown -> PDF exporter (reportlab; no external binaries).

Renders a nicely-typeset, shareable PDF from a markdown file. Handles H1/H2/H3,
blockquotes, horizontal rules, bullet lists, and inline **bold** / *italic* /
`code` / [text](link) (link text kept, target dropped). Read-only w.r.t. the DB.

Reusable (feedback_reusable_engine_scripts_and_continuous_learning): pass any
--in markdown and --out pdf.

Usage: python scripts/_export_md_to_pdf_v1_20260703.py --in PATH.md --out PATH.pdf [--title "..."]
"""
import sys, os, re, html

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.lib.enums import TA_LEFT, TA_JUSTIFY
from reportlab.lib.colors import HexColor
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, HRFlowable,
                                ListFlowable, ListItem)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle


def arg(n, d=None):
    k = f'--{n}'
    if k in sys.argv:
        i = sys.argv.index(k)
        if i + 1 < len(sys.argv):
            return sys.argv[i + 1]
    return d


INK = HexColor('#1a1a2e')
ACCENT = HexColor('#3b3b6d')
MUTE = HexColor('#555555')


def styles():
    ss = getSampleStyleSheet()
    base = 'Georgia' if False else 'Times-Roman'  # serif for an essay
    S = {}
    S['title'] = ParagraphStyle('t', parent=ss['Title'], fontName='Times-Bold',
                                fontSize=22, leading=27, textColor=INK, spaceAfter=14)
    S['h2'] = ParagraphStyle('h2', parent=ss['Heading2'], fontName='Times-Bold',
                             fontSize=15, leading=19, textColor=ACCENT, spaceBefore=16, spaceAfter=7)
    S['h3'] = ParagraphStyle('h3', parent=ss['Heading3'], fontName='Times-Bold',
                             fontSize=12.5, leading=16, textColor=ACCENT, spaceBefore=11, spaceAfter=5)
    S['body'] = ParagraphStyle('b', parent=ss['BodyText'], fontName=base,
                               fontSize=11, leading=16.5, textColor=INK, alignment=TA_JUSTIFY, spaceAfter=9)
    S['quote'] = ParagraphStyle('q', parent=S['body'], leftIndent=16, rightIndent=10,
                                fontSize=9.7, leading=14.5, textColor=MUTE, spaceBefore=2, spaceAfter=10)
    S['bullet'] = ParagraphStyle('bu', parent=S['body'], spaceAfter=4)
    return S


def inline(text):
    """Convert a line of markdown inline syntax to reportlab mini-markup."""
    # protect code spans, then escape, then re-apply markup
    text = html.escape(text, quote=False)
    text = re.sub(r'`([^`]+)`', r'<font face="Courier">\1</font>', text)
    text = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', text)          # [text](url) -> text
    text = re.sub(r'\*\*([^*]+)\*\*', r'<b>\1</b>', text)          # bold
    text = re.sub(r'(?<!\*)\*([^*]+)\*(?!\*)', r'<i>\1</i>', text)  # italic
    text = re.sub(r'★', '&#9733;', text)
    return text


def build(md_path, title=None):
    S = styles()
    flow = []
    lines = open(md_path, encoding='utf-8').read().replace('\r\n', '\n').split('\n')
    i = 0
    bullets = []

    def flush_bullets():
        nonlocal bullets
        if bullets:
            items = [ListItem(Paragraph(inline(b), S['bullet']), leftIndent=12) for b in bullets]
            flow.append(ListFlowable(items, bulletType='bullet', start='•',
                                     leftIndent=14, bulletFontSize=8))
            flow.append(Spacer(1, 5))
            bullets = []

    while i < len(lines):
        ln = lines[i].rstrip()
        if not ln.strip():
            flush_bullets(); i += 1; continue
        if ln.startswith('# '):
            flush_bullets(); flow.append(Paragraph(inline(ln[2:].strip()), S['title']))
        elif ln.startswith('## '):
            flush_bullets(); flow.append(Paragraph(inline(ln[3:].strip()), S['h2']))
        elif ln.startswith('### '):
            flush_bullets(); flow.append(Paragraph(inline(ln[4:].strip()), S['h3']))
        elif ln.strip() in ('---', '***', '___'):
            flush_bullets(); flow.append(Spacer(1, 4))
            flow.append(HRFlowable(width='100%', thickness=0.6, color=HexColor('#bbbbbb')))
            flow.append(Spacer(1, 6))
        elif ln.startswith('> '):
            flush_bullets()
            # gather consecutive quote lines
            q = [ln[2:].strip()]
            while i + 1 < len(lines) and lines[i + 1].startswith('> '):
                i += 1; q.append(lines[i][2:].strip())
            flow.append(Paragraph(inline(' '.join(q)), S['quote']))
        elif re.match(r'^[-*] ', ln):
            bullets.append(ln[2:].strip())
        else:
            flush_bullets(); flow.append(Paragraph(inline(ln.strip()), S['body']))
        i += 1
    flush_bullets()
    return flow


def main():
    src = arg('in'); out = arg('out'); title = arg('title')
    if not (src and out):
        print("need --in and --out"); return
    os.makedirs(os.path.dirname(out) or '.', exist_ok=True)
    doc = SimpleDocTemplate(out, pagesize=A4,
                            leftMargin=2.4*cm, rightMargin=2.4*cm,
                            topMargin=2.2*cm, bottomMargin=2.2*cm,
                            title=(title or os.path.basename(src)),
                            author='Soul Word Analysis Programme')
    doc.build(build(src, title))
    print(f"wrote {out} ({os.path.getsize(out)} bytes)")


if __name__ == '__main__':
    main()
