"""temp_2173_ps_worksheet_sync.py -- brings `iba/docs/ps tools worksheet.xlsx` into line with the
live PS scripts (governance.ps_worksheet_sync_on_change), for #2173: the scripts this build added
or changed (Compliance.ps1 new; Narrative-Register.ps1 -Against; Spine-Check / Session-Close
descriptions) and the drift configmaint already reported on other tabs (Narrative-Register's
After/BuiltFrom/FileStem/Purpose/PurposeRef, Purge-SoftDeletes, VerseReading, and the three scripts
with no tab: Copy-NarrativeToLearning4Comfort, RelationalReading, Run-Stage1Batch).

For each script with drift (lib/cfgquality.find_ps_worksheet_drift): row 4 becomes the live param()
list (existing row-5 hints kept by flag name), row 6 column B the compiled command (a [switch] adds
its flag when the cell is set; a ValidateSet parameter is unquoted; any other value is quoted). A
missing tab is created in the same shape and listed on the Index tab. Descriptions (row 2 and the
Index) are refreshed from the script's .SYNOPSIS for the scripts named in REFRESH.

Usage: python -m iba.app.tools.temp_2173_ps_worksheet_sync [--dry-run]
Temporary (governance.scripts_and_routines)."""
from __future__ import annotations

import pathlib
import re
import sqlite3
import sys

import openpyxl
from openpyxl.styles import Font, PatternFill
from openpyxl.utils import get_column_letter

ROOT = pathlib.Path(__file__).resolve().parents[3]
PS = ROOT / "iba" / "app" / "ps"
WB = ROOT / "iba" / "docs" / "ps tools worksheet.xlsx"
REFRESH = {"Spine-Check", "Session-Close", "Compliance", "Narrative-Register"}
HEAD_FILL = PatternFill("solid", fgColor="FFD9E1F2")


def params(ps: pathlib.Path) -> list[tuple[str, bool, bool]]:
    """[(name, is_switch, is_validateset)] in declaration order, from the param() block."""
    text = ps.read_text(encoding="utf-8-sig")
    m = re.search(r"\bparam\s*\(", text, re.I)
    if not m:
        return []
    depth, i = 1, m.end()
    while depth and i < len(text):
        depth += {"(": 1, ")": -1}.get(text[i], 0)
        i += 1
    block = text[m.end():i - 1]
    out, pending_vs = [], False
    for tok in re.finditer(r"\[ValidateSet\(|\[switch\]\s*\$(\w+)|\$(\w+)", block, re.I):
        if tok.group(0).lower().startswith("[validateset"):
            pending_vs = True
            continue
        if tok.group(1):
            out.append((tok.group(1), True, False))
        else:
            out.append((tok.group(2), False, pending_vs))
        pending_vs = False
    seen, uniq = set(), []
    out = [p for p in out if p[0].lower() not in ("true", "false", "null")]   # $true in [Parameter()]
    for p in out:
        if p[0].lower() not in seen:
            seen.add(p[0].lower())
            uniq.append(p)
    return uniq


def synopsis(ps: pathlib.Path) -> str:
    text = ps.read_text(encoding="utf-8-sig")
    m = re.search(r"\.SYNOPSIS\s*(.*?)(?:\n\s*\.[A-Z]+|\n#>)", text, re.S)
    return re.sub(r"\s+", " ", m.group(1)).strip() if m else ps.stem


def formula(ps_params) -> str:
    parts = ["=A6"]
    for j, (name, sw, vs) in enumerate(ps_params):
        col = get_column_letter(3 + j)
        if sw:
            parts.append(f'IF({col}6<>"",${col}$4&" ","")')
        elif vs:
            parts.append(f'IF({col}6="","",${col}$4&" "&{col}6&" ")')
        else:
            parts.append(f'IF({col}6="","",${col}$4&" \'"&{col}6&"\' ")')
    return parts[0] + ('&" "&' + "&".join(parts[1:]) if len(parts) > 1 else "")


def write_tab(ws, ps: pathlib.Path, ps_params, hints: dict) -> None:
    ws.delete_rows(1, ws.max_row)
    ws["A1"] = ps.name
    ws["A1"].font = Font(bold=True, size=12)
    ws["A2"] = synopsis(ps)
    heads = ["script", "compiled command (copy/paste)"] + [f"-{p[0]}" for p in ps_params]
    for j, h in enumerate(heads, 1):
        c = ws.cell(row=4, column=j, value=h)
        c.fill = HEAD_FILL
        c.font = Font(bold=True)
        if j > 2:
            hint = hints.get(h.lower())
            if hint is None:
                hint = "switch (x to set)" if ps_params[j - 3][1] else None
            ws.cell(row=5, column=j, value=hint)
    ws["A6"] = f"iba\\app\\ps\\{ps.name}"
    ws["B6"] = formula(ps_params)
    ws.column_dimensions["A"].width = 34
    ws.column_dimensions["B"].width = 60


def main() -> int:
    dry = "--dry-run" in sys.argv
    sys.path.insert(0, str(ROOT))
    from iba.app.lib import cfgquality
    conn = sqlite3.connect(f"file:{ROOT / 'iba/app/db/iba.db'}?mode=ro", uri=True)
    drift = cfgquality.find_ps_worksheet_drift(conn, ROOT / "iba" / "app", ROOT)
    stems = {d.split(".ps1")[0] for d in drift} | REFRESH
    wb = openpyxl.load_workbook(WB)
    tabs = {}
    for ws in wb.worksheets:
        for row in ws.iter_rows(min_row=1, max_row=8, max_col=1, values_only=True):
            if isinstance(row[0], str) and row[0].lower().startswith("iba"):
                tabs[pathlib.Path(row[0].replace("\\", "/")).stem.lower()] = ws
    index = wb["Index"]
    done = []
    for stem in sorted(stems):
        ps = PS / f"{stem}.ps1"
        if not ps.exists():
            continue
        p = params(ps)
        ws = tabs.get(stem.lower())
        hints = {}
        if ws is not None:
            for c4, c5 in zip(ws[4], ws[5]):
                if isinstance(c4.value, str) and c4.value.startswith("-"):
                    hints[c4.value.lower()] = c5.value
        else:
            ws = wb.create_sheet(stem[:31])
            index.append([ps.name, synopsis(ps)[:250], "Active"])
        write_tab(ws, ps, p, hints)
        for row in index.iter_rows(min_row=5):
            if row[0].value == ps.name:
                row[1].value = synopsis(ps)[:250]
        done.append(f"{stem}: {len(p)} flag(s)")
    print("\n".join(done))
    if not dry:
        wb.save(WB)
        print(f"saved {WB}")
        left = cfgquality.find_ps_worksheet_drift(conn, ROOT / "iba" / "app", ROOT)
        print(f"drift after: {len(left)}")
        for x in left:
            print("  ", x)
    return 0


if __name__ == "__main__":
    sys.exit(main())
