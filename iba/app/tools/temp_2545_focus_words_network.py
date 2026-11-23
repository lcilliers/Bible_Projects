"""Escalation #2545: the focus words (love, joy, peace, patience, kindness, goodness, faithfulness, gentleness, self-control, hope, wisdom,
righteousness, temperance) against all 169 collections, as a network. Final diagram: focus-words-collections-network-v2-20261123.png/.svg.

Input: _analytics/surfaces/exports/collections-v3-20261123.csv only. A focus word is linked to the collection (its `core`) in whose `word` column it or a
listed form appears (green: member tier core/synonym/gathered; dashed blue: associated; dotted red: opposite or possible opposite). The links between
core words, and temperance to self-control, are Claude's own association model from temp_2545_core_word_network.py (read from that file): INFERENTIAL (B:4).
Read-only on the project; writes the two image files to the exports folder (or the folder given as the first argument). Temporary script (temp_ prefix).
"""
import csv, itertools, sys, pathlib
import networkx as nx
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

SCR = pathlib.Path(__file__).resolve().parent
ROOT = SCR.parents[2]
SRC = str(ROOT / "_analytics" / "surfaces" / "exports" / "collections-v3-20261123.csv")
OUT = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / "_analytics" / "surfaces" / "exports"

# reuse the association model of the first diagram (fields + pairs), without running its drawing
src = (SCR / "temp_2545_core_word_network.py").read_text(encoding="utf-8")

rows = list(csv.DictReader(open(SRC, encoding="utf-8-sig")))
cores = sorted({r["core"] for r in rows})
ns = {"itertools": itertools, "cores": cores}
code = src[src.index("# Model:"):src.index("# keep an edge if")]
exec(code, ns)
score = ns["score"]

FORMS = {
 "love": "love loves loved loving lovers love's", "joy": "joy joyful joyous", "peace": "peace peaceful",
 "patience": "patience patient patiently", "kindness": "kindness kind kindly", "goodness": "goodness good",
 "faithfulness": "faithfulness faithful faithfully", "gentleness": "gentleness gentle", "self-control": "self-control self-controlled",
 "hope": "hope hoped hopes", "wisdom": "wisdom wise wisely", "righteousness": "righteousness righteous righteously",
 "temperance": "temperance temperate",
}
form2focus = {f.replace("\ufffd", "'"): k for k, v in FORMS.items() for f in v.split()}

def norm(w):
    return w.lower().replace("\ufffd", "'")

links = {}   # (focus, core) -> set of tiers
for r in rows:
    f = form2focus.get(norm(r["word"]))
    if f:
        links.setdefault((f, r["core"]), set()).add(r["tier"])

MEMBER = {"core", "synonym", "gathered"}
def kind(tiers):
    if tiers & MEMBER: return "member"
    if tiers & {"associated"}: return "associated"
    return "opposite"

G = nx.Graph()
focus_nodes = ["F:" + k for k in FORMS]
G.add_nodes_from(focus_nodes, kind="focus")
linked = {c for (_, c) in links}
shown_cores = list(cores)
G.add_nodes_from(shown_cores, kind="core")
for (f, c), t in links.items():
    G.add_edge("F:" + f, c, etype=kind(t), weight=3 if kind(t) == "member" else 1.5 if kind(t) == "associated" else 1)
# associations among the cores shown (the model of the first diagram)
core_edges = [(a, b, s) for (a, b), s in score.items() if s >= 3]
has = {x for a, b, s in core_edges for x in (a, b)}
for n in shown_cores:
    if n not in has:
        for s_, (a, b) in sorted(((s_, k) for k, s_ in score.items() if n in k), reverse=True)[:2]:
            core_edges.append((a, b, s_))
for a, b, s in core_edges:
    G.add_edge(a, b, etype="model", weight=0.6)
# temperance is in no collection: place it by the model next to self-control and wise (inferential)
G.add_edge("F:temperance", "self-control", etype="model", weight=2)

import math
import numpy as np
pos = nx.spring_layout(G, weight="weight", k=2.2, iterations=1500, seed=11)
xs = [p[0] for p in pos.values()]; ys = [p[1] for p in pos.values()]
span = max(max(xs) - min(xs), max(ys) - min(ys))
dmin = 0.075 * span
alln = list(G.nodes)
for _ in range(600):
    moved = False
    for i, a_ in enumerate(alln):
        for b_ in alln[i + 1:]:
            fa, fb = a_ in focus_nodes, b_ in focus_nodes
            lim = dmin if (fa and fb) else dmin * 0.62 if (fa or fb) else dmin * 0.28
            v = np.array(pos[a_]) - np.array(pos[b_]); dist = float(np.hypot(*v))
            if dist < lim:
                if dist < 1e-9: v = np.array([1e-3, 0.5e-3]); dist = float(np.hypot(*v))
                push = (lim - dist) / 2 * v / dist
                pos[a_] = tuple(np.array(pos[a_]) + push); pos[b_] = tuple(np.array(pos[b_]) - push); moved = True
    if not moved: break
fig, ax = plt.subplots(figsize=(36, 36))
style = {"member": ("#1b7a3a", "solid", 2.6), "associated": ("#4472c4", "dashed", 1.4), "opposite": ("#c0392b", "dotted", 1.8), "model": ("#999999", "solid", 0.8)}
for t, (col, ls, w) in style.items():
    es = [(a, b) for a, b, d in G.edges(data=True) if d["etype"] == t]
    nx.draw_networkx_edges(G, pos, edgelist=es, ax=ax, edge_color=col, style=ls, width=w, alpha=0.75 if t != "model" else 0.5)
cdeg = {n: sum(1 for _, _, d in G.edges(n, data=True) if d["etype"] != "model") for n in G}
bg = [n for n in shown_cores if n not in linked]; fg = [n for n in shown_cores if n in linked]
nx.draw_networkx_nodes(G, pos, nodelist=bg, ax=ax, node_size=200, node_color="#e4e4e4", edgecolors="white")
nx.draw_networkx_nodes(G, pos, nodelist=fg, ax=ax, node_size=[300 + 120 * cdeg[n] for n in fg], node_color="#f5d98a", edgecolors="white")
nx.draw_networkx_nodes(G, pos, nodelist=focus_nodes, ax=ax, node_size=3000, node_color="#2b5797", edgecolors="white", linewidths=2)
nx.draw_networkx_labels(G, pos, labels={n: n for n in fg}, ax=ax, font_size=11, verticalalignment="bottom")
nx.draw_networkx_labels(G, pos, labels={n: n for n in bg}, ax=ax, font_size=10, font_color="#555555")
nx.draw_networkx_labels(G, pos, labels={n: n[2:] for n in focus_nodes}, ax=ax, font_size=12, font_color="white", font_weight="bold")
ax.legend(handles=[
    Line2D([0], [0], color="#1b7a3a", lw=3, label="word (or its form) is a member of the collection (core, synonym, gathered)"),
    Line2D([0], [0], color="#4472c4", lw=2, ls="dashed", label="word is only associated with the collection"),
    Line2D([0], [0], color="#c0392b", lw=2, ls="dotted", label="word is the opposite or possible opposite there"),
    Line2D([0], [0], color="#999999", lw=1, label="association between two core words (Claude's own model, inferential)"),
    Line2D([0], [0], marker="o", color="w", markerfacecolor="#2b5797", markersize=16, label="focus word"),
    Line2D([0], [0], marker="o", color="w", markerfacecolor="#f5d98a", markersize=14, label="collection where a focus word appears"), Line2D([0], [0], marker="o", color="w", markerfacecolor="#e4e4e4", markersize=12, label="other collection (no focus word in it)")], loc="lower left", fontsize=13)
ax.set_title("Fruit-of-the-Spirit and godly-character words against all 169 collections\n"
             "Focus words and their forms found in the `word` column of collections-v3-20261123.csv; temperance has no row (placed by the model)", fontsize=18)
ax.axis("off"); fig.tight_layout()
fig.savefig(OUT / "focus-words-collections-network-v2-20261123.png", dpi=100)
fig.savefig(OUT / "focus-words-collections-network-v2-20261123.svg")
print(G.number_of_nodes(), G.number_of_edges(), len(shown_cores))
for f in FORMS:
    ms = sorted(c for (ff, c), t in links.items() if ff == f)
    print(f, len(ms), "collections:", ", ".join(f"{c}({kind(links[(f,c)])[0]})" for c in ms))
