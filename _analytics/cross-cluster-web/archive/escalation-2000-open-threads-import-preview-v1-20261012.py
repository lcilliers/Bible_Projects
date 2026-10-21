"""Escalation #2000: preview of the open threads register as escalation rows of type 'thread'.

Read-only. Reads `open-threads-register.md` and iba.db (read-only), writes a JSON preview of the
escalation rows and their thread item rows (proposal v3 section 3), for the researcher's review
BEFORE anything is imported. Nothing is written to any database.

Usage:  python escalation-2000-open-threads-import-preview-v1-20261012.py [--out PATH]
"""
import json
import pathlib
import re
import sqlite3
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[1]
REGISTER = HERE / "open-threads-register.md"
DB = ROOT / "iba" / "app" / "db" / "iba.db"
OUT = HERE / "escalation-2000-open-threads-register-import-preview-v1-20261012.json"
REGISTER_REL = "_analytics/cross-cluster-web/open-threads-register.md"
TITLE_MAX = 60
TERMINAL = {"completed", "withdraw", "closed", "supersede"}

# Titles written by hand (60 characters or fewer). The 75 M02 pairing rows take their own
# "Anger (M02) and X (Mnn)" phrase, which is already short.
TITLES = {
    "OT-01": "Life by the statutes, and statutes without life",
    "OT-02": "Q1 What is death?",
    "OT-03": "Q2 Spirit and soul at death",
    "OT-04": "Q3 The heart after death",
    "OT-05": "Q4 The body raised; the glorified body",
    "OT-06": "God's hand: fuller pass and special-cluster scan",
    "OT-07": "Held items in the earlier ledgers",
    "OT-08": "Life and death as the meta layer",
    "OT-09": "A pass for gold nuggets left on the table",
    "OT-10": "Fear unit 3: weave held",
    "OT-11": "G5015 tarasso (to trouble, stir), outside the fear words",
    "OT-12": "The frame of 10.1 Feeling",
    "OT-13": "Ch 13 Under God's anger folded into 10.13",
    "OT-14": "Chapter 10 retune, not yet",
    "OT-15": "The heat family outside the M02 tag",
    "OT-91": "H6942H dedicate (M64) and the holiness words (M61)",
    "OT-92": "Routing the M64 choosing verses",
    "OT-93": "Parked: 41 choosing verses with no other M-code",
    "OT-94": "Mind in Romans 8: reasoning, or a seat that reasons",
    "OT-95": "M18 x M47 jealousy and zeal verses, held",
    "OT-96": "Generic good/better (tob) verses, held for the filter",
    "OT-97": "M18 forward marks to other clusters",
    "OT-98": "M72 and M18: 182 shared verses",
    "OT-99": "Fragmented verse readings: input for segment re-read",
    "OT-100": "The inner-being meaning of authority and ruling",
}

# Items set by hand where "comes back when" names no cluster or Strong's number.
MANUAL_ITEMS = {
    "OT-03": [("strand", "focused pull: soul and spirit with the death words")],
    "OT-06": [("strand", "the inner being acting through the hands")],
    "OT-07": [("strand", "fear"), ("cluster", "M01"), ("cluster", "M02")],
    "OT-08": [("strand", "life and death, and every later strand")],
    "OT-09": [("researcher", "the researcher chooses the point for a gold-nuggets pass")],
    "OT-10": [("researcher", "the researcher releases the fear unit 3 weave")],
    "OT-12": [("chapter", "10.1"), ("event", "the next key characteristic gets its own sub-chapter")],
    "OT-13": [("chapter", "10.13")],
    "OT-14": [("chapter", "10"), ("researcher", "the researcher calls the Ch 10 retune")],
    "OT-92": [("cluster", "M64"), ("researcher", "the researcher directs the routing of the choosing verses")],
    "OT-93": [("cluster", "M64"), ("researcher", "the researcher reopens the parked choosing verses")],
    "OT-96": [("researcher", "the researcher decides the delight-filter buckets")],
    "OT-99": [("researcher", "the researcher's downstream re-read of each narrative segment starts")],
}

# What stays open after a partial closure, read from the status cell (the forward marks it names).
REMAINING_ITEMS = {
    "OT-16": [("cluster", "M03", "Eze 19:14 forward to M03 (its M02 tag is 'dirge'; the verse holds no anger)"),
              ("verse", "Eze 19:14", "forward to M03")],
    "OT-98": [("cluster", "M58", "Gen 31:29 forward to M58 (the harm held back)"),
              ("verse", "Gen 31:29", "forward to M58")],
}

BOOKS = ("Gen Exo Lev Num Deu Jos Josh Jdg Rut Ruth 1Sa 2Sa 1Ki 2Ki 1Ch 2Ch 1Chr 2Chr Ezr Neh Est "
         "Job Psa Pro Ecc Song Isa Jer Lam Eze Ezek Dan Hos Joe Joel Amo Amos Oba Jon Mic Nah Hab "
         "Zep Hag Zec Mal Mat Mar Mrk Luk Joh Act Rom 1Co 2Co 1Cor 2Cor Gal Eph Phili Php Col 1Th "
         "2Th 1Ti 2Ti Tit Phm Heb Jam Jas 1Pe 2Pe 1Jo 2Jo 3Jo Jud Rev").split()
VERSE_RE = re.compile(r"\b(" + "|".join(sorted(BOOKS, key=len, reverse=True)) +
                      r")\.? (\d{1,3}):(\d{1,3}(?:[–-]\d{1,3})?)")
MCODE_RE = re.compile(r"\b([MT]\d{1,2}[a-z]?)\b(?:\s*\((\d+)\))?")
STRONG_RE = re.compile(r"\b([HG])(\d{1,4})([A-Z]?)\b")
ESC_RE = re.compile(r"#(\d{3,4})\b")
DATE_RE = re.compile(r"\b(20\d\d-\d\d-\d\d)\b")
FILE_RE = re.compile(r"`([^`]+?\.(?:md|csv|py|json))`")


def norm_strong(m):
    return f"{m.group(1)}{int(m.group(2)):04d}{m.group(3)}"


def response(kind, text, via, at, files=None):
    return {"kind": kind, "text": text, "via_escalation": via, "responded_by": "Claude",
            "responded_at": (at + "T00:00:00Z") if at and len(at) == 10 else at, "files": files or [],
            "recorded_from": "register status cell"}


def split_rows(text):
    for line in text.splitlines():
        if re.match(r"\|\s*~*OT-\d", line):
            cells = [c.strip() for c in line.strip().strip("|").split(" | ")]
            if len(cells) != 5:
                raise SystemExit(f"row does not split into 5 cells: {line[:80]}")
            yield cells


def status_word(cell, struck):
    s = re.sub(r"[*~]", "", cell).strip().lower()
    if struck or s.startswith(("resolved", "closed")):
        return "resolved"
    return "touched" if s.startswith("touched") else "open"


def resolve_files(text, tracked):
    found, unresolved = [], []
    for name in FILE_RE.findall(text):
        rel = (HERE / name).resolve() if ("/" in name or name.startswith("..")) else None
        if rel is not None and rel.exists():
            found.append(rel.relative_to(ROOT).as_posix())
            continue
        base = pathlib.PurePosixPath(name).name
        hits = [t for t in tracked if t.endswith("/" + base) or t == base]
        if len(hits) == 1:
            found.append(hits[0])
        elif "*" in name or not hits:
            unresolved.append(name)
        else:
            unresolved.append(f"{name} (matches {len(hits)} files)")
    return sorted(set(found)), unresolved


def items_for(alias, thread_cell, cbw, status_cell, live_states):
    items, seen = [], set()

    def add(kind, value, note, source):
        key = (kind, value)
        if key not in seen:
            seen.add(key)
            items.append({"kind": kind, "value": value, "status": "open", "note": note,
                          "source": source})

    for m in MCODE_RE.finditer(cbw):
        add("cluster", m.group(1), f"{m.group(2)} verses" if m.group(2) else None, "comes back when")
    # "M39/M42 (3)": the count belongs to both codes
    for a, b, n in re.findall(r"\b(M\d{2})/(M\d{2}) \((\d+)\)", cbw):
        for it in items:
            if it["value"] in (a, b) and (it["note"] is None or it["note"] == f"{n} verses"):
                it["note"] = f"{n} verses (shared {a}/{b})"
    for m in STRONG_RE.finditer(cbw):
        add("strong", norm_strong(m), None, "comes back when")
    for m in VERSE_RE.finditer(cbw):
        add("verse", f"{m.group(1)} {m.group(2)}:{m.group(3)}", None, "comes back when")
    for kind, value in MANUAL_ITEMS.get(alias, []):
        add(kind, value, None, "set by hand (no code in comes back when)")
    for kind, value, note in REMAINING_ITEMS.get(alias, []):
        add(kind, value, note, "status cell: left open after a partial closure")
    for m in VERSE_RE.finditer(thread_cell):
        add("verse", f"{m.group(1)} {m.group(2)}:{m.group(3)}", "named in the thread", "thread text")
    for m in ESC_RE.finditer(thread_cell + " " + cbw + " " + status_cell):
        eid = int(m.group(1))
        if live_states.get(eid) and live_states[eid] not in TERMINAL:
            add("escalation", f"#{eid}", f"open escalation named in the thread ({live_states[eid]})",
                "thread text")
    return items


def build():
    text = REGISTER.read_text(encoding="utf-8")
    con = sqlite3.connect(f"file:{DB}?mode=ro", uri=True)
    live_states = dict(con.execute("select id, state from escalation"))
    answered = dict(con.execute("select id, coalesce(answered_at, raised_at) from escalation"))
    tracked = subprocess.run(["git", "ls-files"], cwd=ROOT, capture_output=True, text=True,
                             encoding="utf-8").stdout.splitlines()
    threads, review = [], []
    for alias_cell, thread_cell, raised_cell, cbw, status_cell in split_rows(text):
        struck = alias_cell.startswith("~~") or thread_cell.startswith("~~")
        alias = re.search(r"OT-\d+", alias_cell).group()
        status = status_word(status_cell, struck)
        notes = []

        pair = re.search(r"Anger \(M02\) and (.+?) \((M\d+[a-z]?)\)", thread_cell)
        title = TITLES.get(alias) or (f"Anger (M02) and {pair.group(1)} ({pair.group(2)})" if pair else None)
        if not title:
            title = alias
            notes.append("no title written")
        if len(title) > TITLE_MAX or "--" in title:
            notes.append(f"title fails the title check ({len(title)} chars)")

        dates = DATE_RE.findall(raised_cell)
        raised_at = (dates[0] if dates else "2026-10-02") + "T00:00:00Z"
        if not dates:
            notes.append("no date in 'raised'; register set-up date used")

        researcher_raised = "(researcher)" in thread_cell or raised_cell.lower().startswith("researcher")
        files, unresolved = resolve_files(thread_cell + " " + cbw + " " + status_cell, tracked)
        if unresolved:
            notes.append("file names not resolved to one path: " + "; ".join(unresolved))

        items = items_for(alias, thread_cell, cbw, status_cell, live_states)
        if not any(i["kind"] in ("cluster", "strong", "verse") for i in items):
            notes.append("no cluster, Strong's or verse item: matched only by strand/chapter/researcher/escalation")

        # Item reference (round 4): {alias}.{n}, numbered in order, never renumbered.
        for n, it in enumerate(items, 1):
            it["item_no"] = n
            it["ref"] = f"{alias}.{n}"
            it["opened_at"] = raised_at
            it["opened_by"] = None
            it["responses"] = []
        # Responses (round 5, Q5 approved): one row per response on escalation_thread_item_response.
        # The register's status cells stay whole in the thread's `tried` (decision 4a); only the
        # closures already made are written as responses.
        closed_by = ESC_RE.search(status_cell)
        closed_date = DATE_RE.search(status_cell)
        if status == "resolved":
            via = f"#{closed_by.group(1)}" if closed_by else None
            at = closed_date.group(1) if closed_date else (
                answered.get(int(closed_by.group(1))) if closed_by else None)
            if not closed_date and at:
                notes.append(f"closure date taken from {via}'s answered date, not the status cell")
            for it in items:
                it["status"] = "closed"
                it["responses"].append(response(
                    "closed", f"Closed with the thread, resolved in the register before migration"
                    f"{' (' + via + ')' if via else ''}. The ruling is the thread's resolution.",
                    via, at))
        else:
            for code in set(re.findall(r"closed for (M\d{2}[a-z]?)", status_cell)) | (
                    {"M72"} if alias in ("OT-16", "OT-98") else set()):
                i = status_cell.find(f"closed for {code}")
                segment = (status_cell[i:] if i >= 0 else f"closed for {code}").replace("**", "").strip()
                seg_files, _ = resolve_files(segment, tracked)
                added = [it for it in items if it["source"].startswith("status cell")]
                for it in added:
                    it["opened_at"], it["opened_by"] = "2026-10-12T00:00:00Z", "#1998"
                for it in items:
                    if it["kind"] == "cluster" and it["value"] == code:
                        it["status"] = "closed"
                        it["responses"].append(response("closed", segment, "#1998", "2026-10-12", seg_files))
                        for fw in REMAINING_ITEMS.get(alias, []):
                            if fw[0] == "cluster":
                                refs = ", ".join(f"{a['ref']} ({a['value']})" for a in added)
                                it["responses"].append(response(
                                    "forward", f"{fw[2]}. Adds {refs}.", "#1998", "2026-10-12"))
                notes.append(f"partial closure: {code} item closed, thread stays on-hold")
        if struck and not status_cell.lower().lstrip("*~ ").startswith(("resolved", "closed")):
            notes.append("row is struck through but its status cell does not say resolved")

        esc = {
            "id": "assigned at import",
            "alias": alias,
            "type": "thread",
            "short_description": title,
            "comment": thread_cell,
            "comes_back_when": cbw,
            "context": {"raised_in": raised_cell, "register": REGISTER_REL, "files": files},
            "tried": None,
            "state": "on-hold",
            "next_action": None,
            "next_action_assigned_to": "Claude",
            "resolution_kind": "self_correctable",
            "resolution": None,
            "source": "researcher" if researcher_raised else "Claude",
            "originator": "Researcher" if researcher_raised else "Claude",
            "raised_at": raised_at,
        }
        if status == "resolved":
            esc.update(state="completed", next_action="approved", resolution=status_cell,
                       answered_at=(closed_date.group(1) + "T00:00:00Z") if closed_date else None)
        elif status_cell.strip().strip("*").lower() not in ("open", "open."):
            esc["tried"] = "History before migration (from the register's status cell):\n" + status_cell

        # T5 (round 2, researcher: "in-progress only"): only a referencing escalation that is itself
        # in-progress moves the thread; other references wait until that escalation is started.
        open_refs = [i["value"] for i in items if i["kind"] == "escalation" and i["status"] == "open"
                     and live_states.get(int(i["value"][1:])) == "in-progress"]
        effect = (f"session start moves it to in-progress: in-progress escalation(s) {', '.join(open_refs)} "
                  "reference it") if open_refs and status != "resolved" else None
        threads.append({"register_status": status, "escalation": esc, "items": items,
                        "session_start_effect": effect, "review_notes": notes})
        if notes:
            review.append({"alias": alias, "notes": notes})
    return threads, review


def main():
    out = OUT
    if "--out" in sys.argv:
        out = pathlib.Path(sys.argv[sys.argv.index("--out") + 1])
    threads, review = build()
    from collections import Counter
    summary = {
        "threads": len(threads),
        "by_register_status": Counter(t["register_status"] for t in threads),
        "by_state": Counter(t["escalation"]["state"] for t in threads),
        "items": len([i for t in threads for i in t["items"]]),
        "items_by_kind": Counter(i["kind"] for t in threads for i in t["items"]),
        "items_closed": len([i for t in threads for i in t["items"] if i["status"] == "closed"]),
        "responses": len([r for t in threads for i in t["items"] for r in i["responses"]]),
        "responses_by_kind": Counter(r["kind"] for t in threads for i in t["items"] for r in i["responses"]),
        "threads_moved_to_in_progress_at_first_session_start":
            [t["escalation"]["alias"] for t in threads if t["session_start_effect"]],
        "rows_for_review": len(review),
    }
    rebuilt = json.loads((HERE / "escalation-2000-rebuilt-threads-v1-20261012.json").read_text(encoding="utf-8"))
    next_ot = max(int(t["escalation"]["alias"][3:]) for t in threads) + 1
    for t in rebuilt["proposed"]:
        alias = f"OT-{next_ot}"
        next_ot += 1
        t["escalation"]["alias"] = alias
        for n, it in enumerate(t["items"], 1):
            it["item_no"] = n
            it["ref"] = f"{alias}.{n}"
            it["opened_at"] = t["escalation"]["raised_at"]
            it["opened_by"] = None
            it["responses"] = []
    doc = {
        "about": ("Escalation #2000: preview of the open threads register as escalation rows of type "
                  "'thread', with their item rows. Nothing is imported. Proposal: "
                  "_analytics/cross-cluster-web/open-threads-table-proposal-v3-20261012.md"),
        "built_by": "_analytics/cross-cluster-web/escalation-2000-open-threads-import-preview-v1-20261012.py",
        "summary": summary,
        "review_list": review,
        "threads": threads,
        "rebuilt_from_closed_escalations": rebuilt,
    }
    out.write_text(json.dumps(doc, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(summary, ensure_ascii=False, indent=1))
    print("written:", out)


if __name__ == "__main__":
    main()
