"""build_span_heatmap_v1.py  (READ-ONLY report)

Produce a per-verse span heat map for one book chapter from the IBA database.

For each verse of the chapter (in verse sequence) it counts word-spans and
splits them into:
  * candidate-char spans  = spans that carry a row in `span_candidate`
                            (an inner-being characteristic candidate)
  * non-char spans        = every other (non-deleted) span

Output: a self-contained, theme-aware HTML heat map (blue ramp = candidate-char,
green ramp = non-char; each cell annotated with its raw count).

Usage:
  python iba/app/tools/build_span_heatmap_v1.py --book John --chapter 1
  python iba/app/tools/build_span_heatmap_v1.py --book John --chapter 1 --out path.html

`--book` is the OSIS book name as stored in verse.osisId (e.g. John, Gen, Ps, Matt).
"""
import argparse
import html
import json
import os
import sqlite3

DB = os.path.join("iba", "app", "db", "iba.db")


def fetch(book: str, chapter: int):
    c = sqlite3.connect(DB)
    c.row_factory = sqlite3.Row
    rows = []
    q = """
    SELECT v.id, v.osisId, v.reference,
       (SELECT COUNT(*) FROM span s
          WHERE s.verse_id = v.id AND s.deleted = 0) AS total_spans,
       (SELECT COUNT(DISTINCT sc.span_id) FROM span_candidate sc
          JOIN span s2 ON s2.id = sc.span_id
          WHERE s2.verse_id = v.id AND s2.deleted = 0 AND sc.deleted = 0) AS char_spans
    FROM verse v
    WHERE v.deleted = 0
    """
    for r in c.execute(q):
        parts = (r["osisId"] or "").split(".")
        if len(parts) != 3:
            continue
        b, ch, vn = parts
        if b != book or not ch.isdigit() or int(ch) != chapter or not vn.isdigit():
            continue
        rows.append(
            dict(
                vnum=int(vn),
                reference=r["reference"],
                total=r["total_spans"],
                char=r["char_spans"],
                nonchar=r["total_spans"] - r["char_spans"],
            )
        )
    c.close()
    rows.sort(key=lambda x: x["vnum"])
    return rows


SCREEN = {
    "confirmed": ("check", "✓", "human present", "var(--good)"),
    "inferred": ("tilde", "~", "human inferred", "var(--muted)"),
    "none": ("flag", "⚑", "no human — flagged", "var(--flag)"),
}


def render(book: str, chapter: int, rows, screen=None):
    if not rows:
        raise SystemExit(f"No verses found for {book} {chapter} in {DB}")
    screen = screen or {}
    n_flag = sum(1 for k, v in screen.items() if v.get("status") == "none")
    present = {r["vnum"] for r in rows}
    seq = list(range(min(present), max(present) + 1))
    max_char = max((r["char"] for r in rows), default=0) or 1
    max_non = max((r["nonchar"] for r in rows), default=0) or 1
    tot_total = sum(r["total"] for r in rows)
    tot_char = sum(r["char"] for r in rows)
    tot_non = sum(r["nonchar"] for r in rows)
    by_v = {r["vnum"]: r for r in rows}
    chap_label = f"{book} {chapter}"

    def cell(count, mx, hue_var):
        # intensity 0..1 -> color-mix percentage; light text once dark enough
        frac = count / mx if mx else 0
        pct = round(frac * 100)
        dark_text = frac >= 0.55
        tcol = "var(--cell-ink-light)" if dark_text else "var(--cell-ink-dark)"
        bg = (
            f"color-mix(in oklab, {hue_var} {pct}%, var(--surface-1))"
            if count > 0
            else "var(--zero-cell)"
        )
        cls = "hz" if count == 0 else "hc"
        return (
            f'<td class="{cls}" style="background:{bg};color:{tcol}" '
            f'data-count="{count}">{count}</td>'
        )

    show_screen = bool(screen)

    def screen_cell(vn):
        sc = screen.get(str(vn))
        if not sc:
            return '<td class="scr"></td>'
        cls, glyph, lbl, col = SCREEN.get(sc.get("status"), SCREEN["inferred"])
        ground = html.escape(sc.get("ground", ""))
        note = html.escape(sc.get("note", ""))
        title = lbl + (f" — {sc.get('ground','')}" if sc.get("ground") else "")
        return (
            f'<td class="scr scr-{cls}" data-lbl="{html.escape(lbl)}" '
            f'data-ground="{ground}" data-note="{note}">'
            f'<span class="glyph" style="color:{col}" title="{html.escape(title)}">{glyph}</span></td>'
        )

    body_rows = []
    for vn in seq:
        flagged = show_screen and screen.get(str(vn), {}).get("status") == "none"
        rcls = " flagged" if flagged else ""
        if vn in by_v:
            r = by_v[vn]
            pctc = round(r["char"] / r["total"] * 100) if r["total"] else 0
            body_rows.append(
                f'<tr class="{rcls.strip()}" data-v="{vn}" data-ref="{html.escape(r["reference"])}" '
                f'data-total="{r["total"]}" data-char="{r["char"]}" '
                f'data-nonchar="{r["nonchar"]}" data-pctc="{pctc}">'
                f'<th scope="row" class="vlab">{vn}</th>'
                + cell(r["char"], max_char, "var(--char-hue)")
                + cell(r["nonchar"], max_non, "var(--non-hue)")
                + f'<td class="tot">{r["total"]}</td>'
                + (screen_cell(vn) if show_screen else "")
                + "</tr>"
            )
        else:
            span = 4 if show_screen else 3
            body_rows.append(
                f'<tr class="absent"><th scope="row" class="vlab">{vn}</th>'
                f'<td colspan="{span}" class="absent-cell">not in IBA verse set</td></tr>'
            )

    pct_char = f"{tot_char / tot_total * 100:.1f}" if tot_total else "0"
    rows_html = "\n".join(body_rows)

    screen_intro = (
        " Each verse also carries a <b>human-presence screen</b> — "
        '<span class="glyph" style="color:var(--good)">✓</span> a human being is named, '
        '<span class="glyph" style="color:var(--muted)">~</span> one is inferred, '
        '<span class="glyph" style="color:var(--flag)">⚑</span> none present or inferable '
        "(flagged, out of scope by the <i>God-is-arena</i> rule)."
        if show_screen else ""
    )
    flag_tile = (
        f'<div class="tile flagtile"><div class="n"><span class="sw" '
        f'style="background:var(--flag)"></span>{n_flag}</div>'
        f'<div class="k">Flagged · no human</div></div>'
        if show_screen else ""
    )
    screen_head = '<th style="text-align:center">Human?</th>' if show_screen else ""
    screen_legend = (
        '<div class="lg"><span class="glyph" style="color:var(--good)">✓</span>present'
        '<span class="glyph" style="color:var(--muted);margin-left:12px">~</span>inferred'
        '<span class="glyph" style="color:var(--flag);margin-left:12px">⚑</span>none (flagged)</div>'
        if show_screen else ""
    )
    screen_foot = (
        " The human-presence screen is an analytical judgement over the verse text "
        "(offered for validation, not a DB flag); hover a ⚑/✓/~ mark for its grounding word."
        if show_screen else ""
    )

    return f"""<title>Span heat map — {html.escape(chap_label)}</title>
<style>
  .viz-root {{
    color-scheme: light;
    --page: #f9f9f7; --surface-1: #fcfcfb;
    --text-primary: #0b0b0b; --text-secondary: #52514e; --muted: #898781;
    --grid: #e1e0d9; --border: rgba(11,11,11,0.10);
    --char-hue: #2a78d6;      /* blue  — candidate-char */
    --non-hue: #008300;       /* green — non-char */
    --zero-cell: #f4f3ef;
    --cell-ink-light: #0b0b0b; --cell-ink-dark: #ffffff;
    --good: #0ca30c; --flag: #d03b3b;
    --flag-wash: rgba(208,59,59,0.09); --flag-edge: #d03b3b;
    font-family: system-ui, -apple-system, "Segoe UI", sans-serif;
    color: var(--text-primary); background: var(--page);
    max-width: 760px; margin: 0 auto; padding: 28px 20px 60px;
  }}
  @media (prefers-color-scheme: dark) {{
    :root:where(:not([data-theme="light"])) .viz-root {{
      color-scheme: dark;
      --page: #0d0d0d; --surface-1: #1a1a19;
      --text-primary: #fff; --text-secondary: #c3c2b7; --muted: #898781;
      --grid: #2c2c2a; --border: rgba(255,255,255,0.10);
      --char-hue: #3987e5; --non-hue: #1baf7a;
      --zero-cell: #201f1d;
      --good: #0ca30c; --flag: #e66767;
      --flag-wash: rgba(230,103,103,0.12); --flag-edge: #e66767;
    }}
  }}
  :root[data-theme="dark"] .viz-root {{
    color-scheme: dark;
    --page: #0d0d0d; --surface-1: #1a1a19;
    --text-primary: #fff; --text-secondary: #c3c2b7; --muted: #898781;
    --grid: #2c2c2a; --border: rgba(255,255,255,0.10);
    --char-hue: #3987e5; --non-hue: #1baf7a; --zero-cell: #201f1d;
    --good: #0ca30c; --flag: #e66767;
    --flag-wash: rgba(230,103,103,0.12); --flag-edge: #e66767;
  }}
  .viz-root h1 {{ font-size: 1.4rem; margin: 0 0 4px; letter-spacing: -0.01em; }}
  .sub {{ color: var(--text-secondary); font-size: 0.9rem; margin: 0 0 18px; line-height: 1.5; }}
  .sub code {{ background: var(--surface-1); border: 1px solid var(--border);
    padding: 1px 5px; border-radius: 4px; font-size: 0.82em; }}
  .tiles {{ display: flex; gap: 10px; flex-wrap: wrap; margin: 0 0 22px; }}
  .tile {{ flex: 1 1 130px; background: var(--surface-1); border: 1px solid var(--border);
    border-radius: 10px; padding: 12px 14px; }}
  .tile .n {{ font-size: 1.5rem; font-weight: 650; }}
  .tile .k {{ font-size: 0.75rem; color: var(--muted); text-transform: uppercase;
    letter-spacing: 0.04em; margin-top: 2px; }}
  .tile .n .sw {{ display: inline-block; width: 10px; height: 10px; border-radius: 2px;
    margin-right: 6px; vertical-align: middle; }}
  .scroll {{ overflow-x: auto; }}
  table.heat {{ border-collapse: separate; border-spacing: 2px; width: 100%; }}
  table.heat thead th {{ font-size: 0.72rem; color: var(--muted); font-weight: 600;
    text-transform: uppercase; letter-spacing: 0.03em; padding: 4px 6px; text-align: center;
    position: sticky; top: 0; background: var(--page); }}
  table.heat thead th.k {{ display: inline-flex; }}
  .kdot {{ display:inline-block; width:9px; height:9px; border-radius:2px; margin-right:5px; vertical-align:middle; }}
  th.vlab {{ font-size: 0.8rem; color: var(--text-secondary); font-weight: 600;
    text-align: right; padding-right: 10px; width: 3.2rem; font-variant-numeric: tabular-nums; }}
  td.hc, td.hz {{ text-align: center; font-variant-numeric: tabular-nums; font-size: 0.85rem;
    font-weight: 600; border-radius: 5px; padding: 7px 0; min-width: 84px; }}
  td.hz {{ color: var(--muted) !important; font-weight: 400; }}
  td.tot {{ text-align: center; font-variant-numeric: tabular-nums; font-size: 0.85rem;
    color: var(--text-secondary); padding: 7px 8px; }}
  tr.absent td.absent-cell {{ text-align: center; color: var(--muted); font-size: 0.78rem;
    font-style: italic; padding: 6px; }}
  td.scr {{ text-align: center; padding: 7px 8px; width: 2.4rem; }}
  td.scr .glyph {{ font-size: 0.95rem; font-weight: 700; cursor: default; }}
  tr.flagged th.vlab {{ position: relative; }}
  tr.flagged td, tr.flagged th.vlab {{ background: var(--flag-wash); }}
  tr.flagged th.vlab {{ box-shadow: inset 3px 0 0 var(--flag-edge); }}
  tbody tr:hover th.vlab {{ color: var(--text-primary); }}
  .legend {{ display: flex; gap: 26px; flex-wrap: wrap; margin: 18px 2px 0;
    font-size: 0.76rem; color: var(--text-secondary); }}
  .legend .lg {{ display: flex; align-items: center; gap: 8px; }}
  .ramp {{ width: 120px; height: 10px; border-radius: 3px; border: 1px solid var(--border); }}
  .ramp.c {{ background: linear-gradient(90deg, var(--zero-cell), var(--char-hue)); }}
  .ramp.n {{ background: linear-gradient(90deg, var(--zero-cell), var(--non-hue)); }}
  #tt {{ position: fixed; pointer-events: none; z-index: 20; background: var(--text-primary);
    color: var(--page); font-size: 0.75rem; line-height: 1.35; padding: 7px 9px; border-radius: 6px;
    opacity: 0; transition: opacity .08s; max-width: 220px; }}
  #tt b {{ font-weight: 650; }}
  .foot {{ margin-top: 24px; font-size: 0.72rem; color: var(--muted); line-height: 1.5; }}
</style>
<div class="viz-root">
  <h1>Span heat map — {html.escape(chap_label)}</h1>
  <p class="sub">Word-spans per verse, in verse sequence, split into
    <b>candidate-char</b> spans (a span carrying a <code>span_candidate</code> row —
    an inner-being characteristic candidate) versus <b>non-char</b> spans (all other
    spans). Each cell is shaded by count within its own category (blue / green ramp)
    and labelled with the raw number.{screen_intro} Source: <code>iba/app/db/iba.db</code> ·
    tables <code>verse</code> · <code>span</code> · <code>span_candidate</code>.</p>

  <div class="tiles">
    <div class="tile"><div class="n">{tot_total}</div><div class="k">Total spans</div></div>
    <div class="tile"><div class="n"><span class="sw" style="background:var(--char-hue)"></span>{tot_char}</div><div class="k">Candidate-char · {pct_char}%</div></div>
    <div class="tile"><div class="n"><span class="sw" style="background:var(--non-hue)"></span>{tot_non}</div><div class="k">Non-char spans</div></div>
    <div class="tile"><div class="n">{len(rows)}</div><div class="k">Verses in set</div></div>
    {flag_tile}
  </div>

  <div class="scroll">
  <table class="heat">
    <thead><tr>
      <th class="vlab" style="text-align:right">Verse</th>
      <th><span class="kdot" style="background:var(--char-hue)"></span>Candidate-char</th>
      <th><span class="kdot" style="background:var(--non-hue)"></span>Non-char</th>
      <th>Total</th>
      {screen_head}
    </tr></thead>
    <tbody>
{rows_html}
    </tbody>
  </table>
  </div>

  <div class="legend">
    <div class="lg"><span>Candidate-char</span><span class="ramp c"></span><span>0 → {max_char}</span></div>
    <div class="lg"><span>Non-char</span><span class="ramp n"></span><span>0 → {max_non}</span></div>
    {screen_legend}
  </div>

  <p class="foot">Each ramp is scaled to its own maximum ({max_char} candidate-char,
    {max_non} non-char), so shade shows the pattern <i>within</i> a category — compare
    absolute magnitudes by the numbers, not by cross-category shade. A grey cell means
    zero. Verses absent from the IBA verse subset are marked and skipped.{screen_foot}</p>
</div>
<div id="tt"></div>
<script>
  const tt = document.getElementById('tt');
  document.querySelectorAll('table.heat tbody tr[data-v]').forEach(tr => {{
    const d = tr.dataset;
    tr.querySelectorAll('td.hc, td.hz').forEach((td, i) => {{
      const cat = i === 0 ? 'Candidate-char' : 'Non-char';
      const cnt = td.dataset.count;
      const pct = d.total > 0 ? Math.round(cnt / d.total * 100) : 0;
      const show = e => {{
        tt.innerHTML = `<b>${{d.ref}}</b><br>${{cat}}: <b>${{cnt}}</b> span${{cnt==1?'':'s'}}` +
          `<br>${{pct}}% of ${{d.total}} in verse`;
        tt.style.opacity = 1;
        const x = e.clientX + 14, y = e.clientY + 14;
        tt.style.left = Math.min(x, innerWidth - 230) + 'px';
        tt.style.top = y + 'px';
      }};
      td.addEventListener('mousemove', show);
      td.addEventListener('mouseleave', () => tt.style.opacity = 0);
    }});
    const sc = tr.querySelector('td.scr');
    if (sc && sc.dataset.lbl) {{
      const show = e => {{
        tt.innerHTML = `<b>${{d.ref}}</b><br>${{sc.dataset.lbl}}` +
          (sc.dataset.ground ? `<br><i>${{sc.dataset.ground}}</i>` : '') +
          (sc.dataset.note ? `<br>${{sc.dataset.note}}` : '');
        tt.style.opacity = 1;
        tt.style.left = Math.min(e.clientX + 14, innerWidth - 230) + 'px';
        tt.style.top = (e.clientY + 14) + 'px';
      }};
      sc.addEventListener('mousemove', show);
      sc.addEventListener('mouseleave', () => tt.style.opacity = 0);
    }}
  }});
</script>"""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--book", required=True, help="OSIS book name, e.g. John")
    ap.add_argument("--chapter", type=int, required=True)
    ap.add_argument("--out", default=None)
    ap.add_argument(
        "--screen",
        default=None,
        help="Optional human-presence overlay JSON ({verse: {status, ground, note}}). "
        "If omitted, a sibling ...-humanscreen.json next to --out is used when present.",
    )
    a = ap.parse_args()
    rows = fetch(a.book, a.chapter)
    out = a.out or os.path.join(
        "outputs", "markdown", f"span-heatmap-{a.book.lower()}-{a.chapter}-v1.html"
    )
    screen_path = a.screen or os.path.join(
        os.path.dirname(out), f"span-heatmap-{a.book.lower()}-{a.chapter}-humanscreen.json"
    )
    screen = None
    if os.path.exists(screen_path):
        with open(screen_path, encoding="utf-8") as f:
            screen = json.load(f)
    doc = render(a.book, a.chapter, rows, screen)
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        f.write(doc)
    scr_msg = f" · screen={os.path.basename(screen_path)}" if screen else " · no screen"
    print(f"wrote {out}  ({len(rows)} verses){scr_msg}")


if __name__ == "__main__":
    main()
