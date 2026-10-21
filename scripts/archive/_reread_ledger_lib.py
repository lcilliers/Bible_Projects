#!/usr/bin/env python
"""Reusable ledger-scaffolding helpers for the corrected-method Psalms reread.
Guarantees each characteristic carries the full genre-aware poetic mandatory set
(101,102,104,105,106,107,108,112) + 116 locus + 114 discovery + 115 role, so a
hand-authored reading cannot silently miss a mandatory dim (G10). Qualifiers get
101 + 103 source(->char, res=span, G9b-safe) + 114 + 115; standalone 101+114+115.

Usage (per-psalm _tmp script):
    from _reread_ledger_lib import Reading, IB, GOD, PER
    r = Reading("Psa", 19, 79, note="...")
    r.ch(sid, sense, typ, bearer, op, target, coupling, locus, disc)
    r.qu(sid, sense, src_char_sid, disc)
    r.st(sid, sense, disc)
    r.write()   # -> verse-analysis/psalms/_read/psalm-0NN-reread-v1.json ; prints counts
"""
import json, os
from collections import Counter

IB="internal:ib-state"; GOD="external:god"; PER="external:person"

def _ch(sid, sense, typ, bearer, op, target, coupling, locus, disc):
    return [
        {"n":101,"l":"sense","k":"value","v":sense},
        {"n":102,"l":"type","k":"value","v":typ},
        {"n":104,"l":"seat","k":"pair","v":"none","res":"none"},
        {"n":105,"l":"bearer","k":"pair","v":bearer,"to":sid,"res":"inferred"},
        {"n":106,"l":"operation","k":"event","v":op},
        {"n":107,"l":"target","k":"pair","v":target,"to":sid,"res":"inferred"},
        {"n":108,"l":"manner","k":"pair","v":"none","res":"none"},
        {"n":112,"l":"coupling","k":"pair","v":coupling,"to":sid,"res":"inferred"},
        {"n":116,"l":"locus","k":"value","v":locus},
        {"n":114,"l":"discovery","k":"note","v":disc},
        {"n":115,"l":"role","k":"value","v":"characteristic"},
    ]

def _qu(sid, sense, src_to, disc):
    return [
        {"n":101,"l":"sense","k":"value","v":sense},
        {"n":103,"l":"source","k":"pair","v":"God-content qualifier","to":src_to,"res":"span"},
        {"n":114,"l":"discovery","k":"note","v":disc},
        {"n":115,"l":"role","k":"value","v":"qualifier"},
    ]

def _st(sid, sense, disc):
    return [
        {"n":101,"l":"sense","k":"value","v":sense},
        {"n":114,"l":"discovery","k":"note","v":disc},
        {"n":115,"l":"role","k":"value","v":"standalone"},
    ]

class Reading:
    def __init__(self, book, book_id, chapter, note="", provenance="reread-psalms-2026"):
        self.book=book; self.book_id=book_id; self.chapter=chapter
        self.note=note; self.provenance=provenance; self.spans={}
    def ch(self,sid,*a): self.spans[str(sid)]={"gloss":a[0],"dims":_ch(sid,*a)}
    def qu(self,sid,sense,src,disc): self.spans[str(sid)]={"gloss":sense,"dims":_qu(sid,sense,src,disc)}
    def st(self,sid,sense,disc): self.spans[str(sid)]={"gloss":sense,"dims":_st(sid,sense,disc)}
    def counts(self):
        return Counter(d["dims"][-1]["v"] for d in self.spans.values())
    def write(self):
        out=os.path.join("verse-analysis","psalms","_read",f"psalm-{self.chapter:03d}-reread-v1.json")
        doc={"book":self.book,"book_id":self.book_id,"chapter":self.chapter,
             "provenance":self.provenance,"note":self.note,"spans":self.spans}
        with open(out,"w",encoding="utf-8") as f: json.dump(doc,f,ensure_ascii=False,indent=1)
        c=self.counts()
        print(f"wrote {out} | spans:{len(self.spans)} | chars:{c['characteristic']} qual:{c['qualifier']} standalone:{c['standalone']}")
        return c['characteristic']
