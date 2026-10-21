"""_check_ve_signal_lists.py — completeness audit of EVERY seed/signal list in the VE engine.

The 2026-06-18 location fix showed the SEAT list was a stub. This applies the same discipline to the
OTHER hand-seeded lists (divine names, spirit-beings, perception, cognition, intensifier, causal): for
each, a curated set of the category's CANONICAL lemmas is diffed against what the engine actually holds,
and corpus presence is reported. Read-only. Flags present-in-corpus lemmas the engine is missing.

  python scripts/_check_ve_signal_lists.py
"""
import os, re, sqlite3, sys
sys.path.insert(0, os.path.dirname(__file__)); sys.path.insert(0, os.path.join(os.path.dirname(__file__), "analytics"))
import _ve_engine_v2 as eng

DB = os.path.join("database", "bible_research.db")
# curated CANONICAL members per category (the lexical job): {strong: gloss-hint}
EXPECTED = {
    "DIVINE": {  # divine names/titles used to detect God as object/agent/possessor
        "H3068": "YHWH", "H3069": "YHWH (Elohim-pointing)", "H0430": "Elohim", "H0433": "Eloah",
        "H0410": "El", "H0136": "Adonai", "H0113": "Adon (Lord)", "H7706": "Shaddai", "H3050": "Yah",
        "H5945": "Elyon (Most High)", "G2316": "Theos", "G2962": "Kyrios", "G5547": "Christos",
        "G5310": "Hypsistos (Most High)",
    },
    "SPIRIT_BEINGS": {  # for object-type = spiritual-being
        "G4151": "pneuma", "G1140": "daimonion", "G1142": "daimon", "H7307": "ruach", "H7700": "shed (demon)",
        "H4397": "malak (angel)", "G0032": "angelos (angel)", "H3742": "cherub", "H8314": "seraph",
    },
    "PERCEPTION": {  # perception verbs (cause-of-affect detection)
        "H7200": "ra'ah (see)", "H2372": "chazah (see/behold)", "H5027": "nabat (look)", "H8085": "shama (hear)",
        "H0238": "azan (give ear)", "G3708": "horao (see)", "G1492": "eido (see)", "G0991": "blepo (see)",
        "G2334": "theoreo (behold)", "G0191": "akouo (hear)",
    },
    "COGNITION": {  # cognition verbs
        "H3045": "yada (know)", "H0995": "bin (understand)", "H2449": "chakam (be wise)",
        "G1097": "ginosko (know)", "G1492": "oida (know)", "G1380": "dokeo (think)", "G3539": "noeo (perceive)",
    },
    "INTENSIFIER": {  # quantifier/intensifier
        "H7227": "rab (many)", "H7231": "rabab (many)", "H3966": "me'od (very)", "H3605": "kol (all)",
        "H1419": "gadol (great)", "G4183": "polys (many)", "G4970": "sphodra (exceedingly)", "G3029": "lian (very)",
    },
    "CAUSAL": {  # causal markers
        "H3588": "ki (because)", "H3282": "ya'an (because)", "G3754": "hoti", "G1063": "gar", "G1360": "dioti",
        "G1893": "epei (since)",
    },
}
ACTUAL = {"DIVINE": eng.DIVINE, "SPIRIT_BEINGS": eng.SPIRIT_BEINGS, "PERCEPTION": eng.PERCEPTION,
          "COGNITION": eng.COGNITION, "INTENSIFIER": set(eng.INTENSIFIER), "CAUSAL": eng.CAUSAL}


def main():
    c = sqlite3.connect(DB); c.row_factory = sqlite3.Row
    def units(strong):
        return c.execute("""SELECT COUNT(DISTINCT vc.id) FROM verse_context vc JOIN mti_terms m ON m.id=vc.mti_term_id
            WHERE COALESCE(vc.delete_flagged,0)=0 AND m.strongs_number LIKE ?""", (strong + "%",)).fetchone()[0]
    any_gap = False
    for cat, expected in EXPECTED.items():
        have = ACTUAL[cat]
        missing = [(s, g) for s, g in expected.items() if eng._canon(s) not in have]
        present_missing = [(units(eng._canon(s)), s, g) for s, g in missing if units(eng._canon(s)) > 0]
        present_missing.sort(reverse=True)
        print(f"\n=== {cat} — engine holds {len(have)} lemmas; {len(present_missing)} canonical member(s) MISSING & present in corpus ===")
        if present_missing:
            any_gap = True
            for u, s, g in present_missing:
                print(f"  {u:5} units  {s:7} {g}")
        else:
            print("  (complete — no missing canonical members present in the corpus)")
    print("\nNOTE: 'units' = term-in-verse occurrences of that lemma as a tagged term (a co-word can matter even at 0).")
    return 1 if any_gap else 0


if __name__ == "__main__":
    sys.exit(main())
