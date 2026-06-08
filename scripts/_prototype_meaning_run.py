"""_prototype_meaning_run.py — READ-ONLY prototype of the L1 verse-level MEANING RUN. For a term, parses its
BDB sense_text into stem-branches ((Qal)/(Niphal)/(Piel)…) and numbered senses, pulls the per-verse STEP
morph, and SELECTS the sense the morph activates — then shows it per verse for inspection. NO DB writes.

Two BDB disambiguation axes:
  - STEM axis  (Qal/Niphal/Piel → 1a/1b/1c): the morph stem resolves it mechanically.
  - NUMBERED   (1) … 2) …): a homonym/sense split morph does NOT resolve → residue → verse read (L2).

Usage:  python scripts/_prototype_meaning_run.py --strongs H3372G [--sample 25] --out <file>.md
"""
import argparse, os, re, sqlite3, sys
sys.path.insert(0, os.path.join("scripts", "analytics"))
sys.stdout.reconfigure(encoding="utf-8")
from step_client import StepClient
DB = os.path.join("database", "bible_research.db")

SPAN = re.compile(r"<span\s+morph='([^']*)'\s+strong='([^']*)'>([^<]*)</span>", re.I)
HEB_STEM = {"q": "Qal", "N": "Niphal", "p": "Piel", "P": "Pual", "h": "Hiphil", "H": "Hophal",
            "t": "Hithpael", "o": "Polel", "O": "Polal", "r": "Hithpolel", "v": "Hithpael"}
STEM_MARK = re.compile(r"\((Qal|Niphal|Piel|Pual|Hiphil|Hophal|Hithpael|Polel|Pilpel|Poel)\)", re.I)
NUM_MARK = re.compile(r"(?:^|\n)\s*(\d+)\)\s")


def base(code):
    m = re.match(r"^([HG]\d+)", code or ""); return m.group(1) if m else (code or "")


def morph_for(html, strong):
    want = strong; wbase = base(strong)
    for ma, sa, _t in SPAN.findall(html):
        sc = sa.split(); mc = ma.split()
        for i, s in enumerate(sc):
            if s == want or base(s) == wbase:
                return mc[i] if i < len(mc) else (mc[0] if mc else "")
    return ""


def stem_of(morph):
    if not morph or morph[0] != "H":
        return ""
    body = morph[1:].lstrip("-")
    if body[:1] == "V" and len(body) > 1:
        return HEB_STEM.get(body[1], f"?{body[1]}")
    return ""


SUBSHADE = re.compile(r"\d+[a-z]\d+\)")  # e.g. 1a1) 1a2) — within-stem shades


def parse_branches(sense_text):
    """Return {stem -> (branch_text, n_subshades)} from the BDB block, plus the count of numbered senses.
    A stem segment ends at the next (Stem) marker OR the next top-level numbered sense (e.g. '2)')."""
    t = sense_text or ""
    branches = {}
    marks = list(STEM_MARK.finditer(t))
    for i, m in enumerate(marks):
        stem = m.group(1).capitalize()
        end = marks[i + 1].start() if i + 1 < len(marks) else len(t)
        seg_raw = t[m.end():end]
        # trim a trailing top-level numbered sense that bleeds in (e.g. Piel … '2) to shoot')
        cut = re.search(r"(?:^|\s)\d+\)\s", seg_raw[3:])
        if i + 1 >= len(marks) and cut:
            seg_raw = seg_raw[:cut.start() + 3]
        nsub = len(SUBSHADE.findall(seg_raw))
        seg = re.sub(r"\s+", " ", seg_raw).strip().strip(":").strip()[:130]
        branches[stem] = (seg, nsub)
    nnum = len(set(NUM_MARK.findall(t)))
    return branches, nnum


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--strongs", required=True)
    ap.add_argument("--sample", type=int, default=24)
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    conn = sqlite3.connect(DB); conn.row_factory = sqlite3.Row; c = conn.cursor()

    inv = c.execute("SELECT transliteration, parsed_meaning_id FROM wa_term_inventory "
                    "WHERE strongs_number=? AND parsed_meaning_id IS NOT NULL LIMIT 1", (a.strongs,)).fetchone()
    tl = inv["transliteration"] if inv else a.strongs
    sense_text = ""
    if inv:
        row = c.execute("SELECT group_concat(sense_text, '\n') st FROM wa_meaning_sense "
                        "WHERE parsed_meaning_id=?", (inv["parsed_meaning_id"],)).fetchone()
        sense_text = row["st"] or ""
    branches, nnum = parse_branches(sense_text)

    sc = StepClient()
    recs, html = sc.get_verse_records_with_html(a.strongs)

    rows = []
    stem_count = {}
    for r in recs:
        m = morph_for(html.get(r["osisId"], ""), a.strongs)
        st = stem_of(m)
        stem_count[st or "(noun/none)"] = stem_count.get(st or "(noun/none)", 0) + 1
        seg, nsub = branches.get(st, ("", 0)) if st else ("", 0)
        applied = seg
        # stem resolved by morph? then check WITHIN-stem shade: >1 sub-shade ⇒ still needs the verse read (L2)
        stem_unresolved = (bool(branches) and st and st not in branches) or (bool(branches) and not st) \
            or (not branches and nnum > 1)
        shade_residue = bool(st and st in branches and nsub > 1)
        residue = "stem" if stem_unresolved else ("shade" if shade_residue else "")
        rows.append((r["ref"], r["esv_text"], r["target_word"], m, st, applied, residue))

    L = [f"# L1 meaning run — verse-level inspection: {a.strongs} {tl} (prototype)", ""]
    L.append("> READ-ONLY (`scripts/_prototype_meaning_run.py`). Per verse: STEP morph → stem → the BDB "
             "sense-branch the morph activates. NO DB writes. Residue = morph can't settle it (homonym / "
             "numbered-sense split) → verse read (L2).")
    L.append("")
    L.append(f"**Term {a.strongs} {tl} · {len(recs)} verses · {nnum} numbered BDB sense(s).**")
    if nnum > 1:
        L.append("")
        L.append(f"> ⚠ **Homonym/numbered-sense watch:** this term has {nnum} numbered BDB senses (e.g. a "
                 "separate sense beyond the stem branches). Morph resolves the STEM axis but not which "
                 "numbered sense — verses carrying the rare sense must be caught in the L2 read.")
    L.append("")
    L.append("### Parsed sense-branches (morph stem → meaning)")
    for stem, (txt, nsub) in branches.items():
        shade = f"  _({nsub} within-stem shades → L2 resolves which)_" if nsub > 1 else ""
        L.append(f"- **{stem}** → {txt}{shade}")
    if not branches:
        L.append("- _(no stem markers — single/noun sense; morph does not disambiguate)_")
    L.append("")
    L.append("### Stem distribution across the term's verses")
    L.append(", ".join(f"{k}: {v}" for k, v in sorted(stem_count.items(), key=lambda x: -x[1])))
    L.append("")
    L.append(f"### Sample verses (first {a.sample}) — applied meaning by morph")
    L.append("")
    L.append("| Ref | Verse (ESV) | target | morph | stem | applied (stem branch) | L2-residue |")
    L.append("|---|---|---|---|---|---|---|")
    for ref, txt, tgt, m, st, applied, residue in rows[:a.sample]:
        vt = (txt or "")[:62].replace("|", "/")
        ap = (applied or "—")[:80]
        L.append(f"| {ref} | {vt} | {tgt} | {m} | {st or '—'} | {ap} | {residue or '—'} |")
    L.append("")
    nstem = sum(1 for x in rows if x[6] == "stem")
    nshade = sum(1 for x in rows if x[6] == "shade")
    L.append(f"**Morph resolves the STEM axis for {len(rows)-nstem}/{len(rows)} verses.** "
             f"Remaining for the L2 verse read: **{nshade} within-stem shade** (e.g. Qal fear vs awe vs "
             f"reverence — the inner-being-critical split morph can't make) + the numbered-sense homonym "
             f"watch. _This is the L1-narrows / L2-decides boundary, made concrete._")
    os.makedirs(os.path.dirname(a.out), exist_ok=True)
    open(a.out, "w", encoding="utf-8").write("\n".join(L))
    print(f"{a.strongs} {tl}: {len(recs)} verses; branches={list(branches)}; "
          f"stem-unresolved {nstem}; shade-residue {nshade}; wrote {a.out}")


if __name__ == "__main__":
    main()
