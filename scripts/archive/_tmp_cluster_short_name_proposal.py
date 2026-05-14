"""Propose short_name (<=15 chars) for each cluster, from description."""
import sqlite3, sys, re
try: sys.stdout.reconfigure(encoding="utf-8")
except: pass
conn = sqlite3.connect("database/bible_research.db")
conn.row_factory = sqlite3.Row

# Hand-curated overrides where the obvious first-word is awkward
OVERRIDES = {
    "M26": "Righteousness",  # 13 — fits
    "M34": "Perseverance",   # 12 — fits (Steadfastness=13 also fits)
    "FLAG": "Flag",
    "T2": "Supplementary",   # 13 — for the T2 bucket
}

def derive(code: str, description: str) -> str:
    if code in OVERRIDES:
        return OVERRIDES[code]
    # Take first comma-separated chunk, then first " and " split
    first = description.split(",")[0].strip()
    first = first.split(" and ")[0].strip()
    # Cap at 15 chars
    if len(first) <= 15:
        return first
    return first[:15]

print(f"{'code':<6s} {'short_name (≤15)':<17s} {'description':<55s} {'len':>4s}")
print("-" * 90)
for r in conn.execute("SELECT cluster_code, description FROM cluster ORDER BY cluster_code"):
    sn = derive(r["cluster_code"], r["description"] or "")
    over = " ←override" if r["cluster_code"] in OVERRIDES else ""
    print(f"{r['cluster_code']:<6s} {sn:<17s} {(r['description'] or '')[:55]:<55s} {len(sn):>4d}{over}")
conn.close()
