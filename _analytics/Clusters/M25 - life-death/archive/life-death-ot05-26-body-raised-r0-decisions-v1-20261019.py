"""OT-05.26 (#2160): one decision per uncited set-word verse of the R0 pull (read-only check).

Decisions come from reading each verse in its passage (report: life-death-ot05-26-body-raised-r0-v1-
20261019.md). This script only checks that every one of the pull's uncited set-word verses has
exactly one decision, and writes the decisions CSV.
"""
import csv
import pathlib
import sys

sys.stdout.reconfigure(encoding="utf-8")
HERE = pathlib.Path(__file__).parent
PULL = HERE / "life-death-ot05-26-body-raised-r0-pull-v1-20261019.csv"
OUT = HERE / "life-death-ot05-26-body-raised-r0-decisions-v1-20261019.csv"

G = {
    "A1 the inner acts toward the resurrection (deny, question, not understand, remember, believe, mock, fear)": [
        "Mat 22:23", "Mat 22:28", "Mat 22:31", "Mar 12:18", "Mar 12:23", "Mar 12:25", "Mar 12:26",
        "Luk 20:27", "Luk 20:33", "Luk 20:35", "Luk 20:37", "Mat 17:9", "Mar 9:9", "Mar 9:10",
        "Joh 20:9", "Joh 2:22", "Luk 24:46", "Joh 11:24", "Act 17:18", "Act 17:32", "Act 23:6",
        "Act 23:8", "Act 24:21", "Act 26:8", "1Cor 15:12", "1Cor 15:13", "1Cor 15:15", "1Cor 15:16",
        "2Ti 2:18", "2Ti 2:8", "Mat 27:64", "Mat 14:2", "Mar 6:14", "Luk 9:7"],
    "A2 raised with Christ now, and living from it": [
        "Rom 6:5", "Col 2:12", "Col 3:1", "Eph 2:6", "Eph 1:20", "Phili 3:11", "Rom 4:24",
        "1Pe 1:21", "1Pe 1:23"],
    "A3 living toward the resurrection (giving, enduring, self-control, seeking, sowing)": [
        "Luk 14:14", "Heb 11:35", "1Cor 9:25", "Rom 2:7", "Gal 6:8"],
    "A4 imperishable said of what is within, or held for the person": [
        "Eph 6:24", "1Pe 1:4", "Tit 2:7"],
    "A5 corruption as a bondage (Rom 8:21 here; the moral face forward to M57, OT-05.24)": [
        "Rom 8:21", "2Pe 2:12", "2Pe 2:19"],
    "A6 the dead raised as a sign, and the belief or plotting it moved": [
        "Mat 11:5", "Luk 7:22", "Joh 12:9", "Joh 12:17"],
    "B 13.1 God's character (immortal; assurance by raising him)": [
        "1Ti 1:17", "1Ti 6:16", "Act 17:31"],
    "D the section's own account, not yet carried (Life, and judgment; Christ first)": [
        "1Cor 15:21", "Rev 20:5", "Rev 20:6"],
    "E cited elsewhere: carried there, pointer only if the weave needs it": [
        "Luk 2:34", "Luk 16:31", "Joh 5:21", "Joh 11:25", "Act 2:31", "Rom 1:23", "Rom 6:4",
        "Rom 6:9", "Rom 6:12", "Rom 7:4", "Rom 10:9", "1Cor 15:32", "2Cor 1:9", "2Cor 4:11",
        "Eph 5:14", "Phili 3:10", "1Th 1:10", "Heb 11:19", "1Pe 1:18", "1Pe 3:4", "1Pe 3:21",
        "2Pe 1:4"],
    "C data: Christ raised proclaimed or witnessed, or the word in another sense": [
        "Mat 10:8", "Mat 27:53", "Mat 28:7", "Joh 12:1", "Joh 21:14", "Act 1:22", "Act 3:15",
        "Act 4:2", "Act 4:10", "Act 4:33", "Act 13:30", "Act 13:34", "Act 17:3", "Act 26:23",
        "Rom 1:4", "Rom 9:17", "1Cor 15:29", "Gal 1:1", "Col 2:22", "Heb 6:2"],
}

pull = {r["ref"]: r for r in csv.DictReader(PULL.open(encoding="utf-8"))
        if r["words"] and not r["cited_in_section"]}
seen: dict[str, str] = {}
for g, refs in G.items():
    for ref in refs:
        if ref in seen:
            sys.exit(f"{ref} decided twice: {seen[ref]} / {g}")
        if ref not in pull:
            sys.exit(f"{ref} is not an uncited set-word verse of the pull")
        seen[ref] = g
missing = sorted(set(pull) - set(seen))
if missing:
    sys.exit(f"{len(missing)} verses with no decision: {missing}")

with OUT.open("w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(["ref", "decision", "words", "cited_elsewhere", "text"])
    for ref, r in pull.items():
        w.writerow([ref, seen[ref], r["words"], r["cited_elsewhere"], r["text"]])
for g, refs in G.items():
    print(f"{len(refs):3}  {g}")
print(f"{len(seen):3}  total, every uncited set-word verse decided once -> {OUT.name}")
