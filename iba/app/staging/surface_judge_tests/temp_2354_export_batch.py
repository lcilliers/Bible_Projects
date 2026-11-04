"""Throwaway export of a surface-judge batch file to CSV and Excel (#2354). Reads the batch file and iba.db read-only;
writes nothing to the database. Usage: python temp_2354_export_batch.py <batch name>"""
import csv
import datetime
import pathlib
import sqlite3
import sys

from openpyxl import Workbook
from openpyxl.styles import Font
from openpyxl.utils import get_column_letter

from iba.app.lib import surfacejudge as sj

name = sys.argv[1]
folder = pathlib.Path(r"C:\Bible_study_projects\outputs\concept-mapping\surface-group")
src = folder / f"{name}.jsonl"
conn = sqlite3.connect("file:C:/Bible_study_projects/iba/app/db/iba.db?mode=ro", uri=True)
rows_in = dict(sj.surface_list(conn))
recs = sj.read_batch(src)  # the last record of a surface is the one read

order = [s for s in rows_in if s in recs]
head = ["surface", "rows_for_word", "group", "reason", "model", "secs", "researcher_group", "researcher_note"]
judged, failed = [], []
for s in order:
    r = recs[s]
    if r.get("group"):
        judged.append([s, rows_in[s], r["group"], r.get("reason") or "", r.get("judged_by"), r.get("secs"), "", ""])
    else:
        failed.append([s, rows_in[s], "; ".join(r.get("errors") or [])[:300]])

stamp = datetime.datetime.now(datetime.timezone.utc).strftime("%Y%m%dT%H%MZ")
base = folder / f"{name}-export-{stamp}"
with open(f"{base}.csv", "w", newline="", encoding="utf-8-sig") as fh:
    w = csv.writer(fh)
    w.writerow(head)
    w.writerows(judged)

wb = Workbook()
ws = wb.active
ws.title = "Judged"
ws.append(head)
for r in judged:
    ws.append(r)
sm = wb.create_sheet("Summary")
sm.append(["batch", name])
sm.append(["exported (UTC)", stamp])
sm.append(["on the list", len(rows_in)])
sm.append(["judged", len(judged)])
sm.append(["failed (no usable answer)", len(failed)])
sm.append(["left", len(rows_in) - len(judged)])
sm.append([])
sm.append(["group", "surfaces", "rows for the word"])
for g in sorted({r[2] for r in judged}):
    sm.append([g, sum(1 for r in judged if r[2] == g), sum(r[1] for r in judged if r[2] == g)])
sm.append([])
sm.append(["Every group is the model's inferential answer (qwen3:30b), unconfirmed. Snapshot: the cycle may still be running."])
fl = wb.create_sheet("Failed")
fl.append(["surface", "rows_for_word", "errors"])
for r in failed:
    fl.append(r)
for sheet in (ws, sm, fl):
    for c in sheet[1]:
        c.font = Font(bold=True)
    for i in range(1, sheet.max_column + 1):
        sheet.column_dimensions[get_column_letter(i)].width = 14
ws.column_dimensions["A"].width = 22
ws.column_dimensions["C"].width = 20
ws.column_dimensions["D"].width = 70
ws.freeze_panes = "A2"
ws.auto_filter.ref = ws.dimensions
sm.column_dimensions["A"].width = 30
wb.save(f"{base}.xlsx")
print(f"{base}.csv / .xlsx : judged {len(judged)}, failed {len(failed)}, list {len(rows_in)}")
