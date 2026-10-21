"""Compact builder for Proverbs char-driven readings (Stage-4).

Emits the reading JSON in the corrected convention: 116 locus = the internal/external
token; 112 coupling = the pairing phrase; relational dims are flags (res=inferred,
self-pointing) UNLESS a span-id endpoint is given (res=span -> a real pair). Characteristic
carries the full poetic mandatory set (101,102,104,105,106,107,108,112,114,115,116);
qualifier/standalone carry NO ve_lexical (they are pair endpoints / role-only, D2) and are
handled by role-derivation in the apply — so they are NOT emitted here.

Usage (per-passage _tmp):
    from _pro_read_lib import Reading, IB, GOD, PER
    r = Reading(chapter=1, note="...")
    r.ch(sid, gloss, sense, typ, bearer, op, target, coupling, locus, disc,
         target_to=None, coupling_to=None)   # *_to = span-id -> real pair (res=span)
    path = r.write("p3715-1_24")   # -> verse-analysis/proverbs/_read/pro-<name>-reread-v1.json
"""
import json, os

IB = "internal:ib-state"; GOD = "external:god"; PER = "external:person"
OUT = os.path.join("verse-analysis", "proverbs", "_read")


def _rel(n, l, v, sid, to):
    """relational dim: a real span-pair if `to` given, else an inferred self-flag."""
    if to is not None:
        return {"n": n, "l": l, "k": "pair", "v": v, "to": int(to), "res": "span"}
    return {"n": n, "l": l, "k": "flag", "v": v, "to": int(sid), "res": "inferred"}


class Reading:
    def __init__(self, chapter, note="", book="Pro", book_id=20, provenance="reread-proverbs-2026"):
        self.chapter = chapter; self.note = note; self.book = book
        self.book_id = book_id; self.provenance = provenance; self.spans = {}

    def ch(self, sid, gloss, sense, typ, bearer, op, target, coupling, locus, disc,
           target_to=None, coupling_to=None, manner="none"):
        dims = [
            {"n": 101, "l": "sense", "k": "value", "v": sense},
            {"n": 102, "l": "type", "k": "value", "v": typ},
            {"n": 104, "l": "seat", "k": "flag", "v": "none", "res": "none"},
            _rel(105, "bearer", bearer, sid, None),
            {"n": 106, "l": "operation", "k": "event", "v": op},
            _rel(107, "target", target, sid, target_to),
            {"n": 108, "l": "manner", "k": ("flag" if manner == "none" else "flag"),
             "v": manner, "res": ("none" if manner == "none" else "inferred"), "to": int(sid)},
            _rel(112, "coupling", coupling, sid, coupling_to),
            {"n": 116, "l": "locus", "k": "value", "v": locus},
            {"n": 114, "l": "discovery", "k": "note", "v": disc},
            {"n": 115, "l": "role", "k": "value", "v": "characteristic"},
        ]
        # tidy manner none -> canonical
        if manner == "none":
            dims[6] = {"n": 108, "l": "manner", "k": "flag", "v": "none", "res": "none"}
        self.spans[str(sid)] = {"gloss": gloss, "dims": dims}

    def write(self, name):
        os.makedirs(OUT, exist_ok=True)
        path = os.path.join(OUT, f"pro-{name}-reread-v1.json")
        doc = {"book": self.book, "book_id": self.book_id, "chapter": self.chapter,
               "provenance": self.provenance, "note": self.note, "spans": self.spans}
        json.dump(doc, open(path, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
        chars = sum(1 for s in self.spans.values() if s["dims"][-1]["v"] == "characteristic")
        print(f"wrote {path} | characteristics: {chars}")
        return path
