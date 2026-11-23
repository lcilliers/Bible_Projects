"""Researcher request after #2545: pair every single-word surface with every other surface of the list that WordNet pairs it with.

Input : _analytics/surfaces/exports/behaviour-and-inner-state-surfaces-v3-20261109.csv (distinct `surface`, single words only: no space).
        WordNet 3.0, held in the project at data/imports/wordnet (cfg_setting surfaces.wordnet_data_dir when set; the folder that holds corpora/wordnet), read
        through NLTK. No word outside the surface list is added.
Pairing: surfaces A and B are paired when WordNet links them, and only then:
         synonym  = they share at least one synset (weight = number of synsets they share);
         antonym  = a lemma of one is an antonym of a lemma of the other (weight 1 per antonym link);
         both     = both hold (weight = the two added).
         A surface is looked up by its WordNet base form (morphy). Two surfaces with the same base form (walk / walked) are one lemma to WordNet: they
         are paired as `same_base` (weight = synsets shared, the same rule), so words of one base are drawn together and not set apart.
         Also linked, each with weight 1 per link: derivational (WordNet derivationally related forms and pertainyms: bold / boldness / boldly) and
         similar (WordNet similar-to between adjective sense groups: generous / bountiful, where a pair's weight counts the sense-group links).
Distance: shortest path over the pairs, two matrices: hops (every pair counts 1) and weighted (a pair is 1 / weight long, so more shared senses = nearer).
         A surface with no path to another has a blank cell.
Output : workbook, the two distance matrices (csv) and the weighted network diagram in _analytics/surfaces/exports/ (or the folder given as the first argument).
Read-only on the project. Temporary script (temp_ prefix); WordNet findings are an outside source, not study data.
"""
import csv, sys, pathlib, itertools, collections
import nltk
import networkx as nx
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from openpyxl import Workbook
from openpyxl.styles import Font

ROOT = pathlib.Path(__file__).resolve().parents[3]
SRC = ROOT / "_analytics" / "surfaces" / "exports" / "behaviour-and-inner-state-surfaces-v3-20261109.csv"
OUT = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / "_analytics" / "surfaces" / "exports"
WN_DIR = str(ROOT / "data" / "imports" / "wordnet")
try:
    import sqlite3, json
    _r = sqlite3.connect(str(ROOT / "iba" / "app" / "db" / "iba.db")).execute("select value from cfg_setting where key='surfaces.wordnet_data_dir' and inactive is not 1").fetchone()
    if _r:
        WN_DIR = str(ROOT / json.loads(_r[0]))
except Exception:
    pass
STAMP = "20261123"
nltk.data.path.insert(0, WN_DIR)
from nltk.corpus import wordnet as wn

rows = list(csv.DictReader(open(SRC, encoding="utf-8-sig")))
groups = collections.defaultdict(set)
for r in rows:
    groups[r["surface"]].add(r["surface_group"] or "(none)")
surfaces = sorted(s for s in groups if " " not in s.strip() and s.strip())

syn = {}          # surface -> set of synset names
lemmas = {}       # surface -> set of base forms WordNet resolves it to
anto = collections.defaultdict(set)   # surface -> set of antonym lemma names
for s in surfaces:
    ss = wn.synsets(s.lower())
    if not ss:
        continue
    syn[s] = {x.name() for x in ss}
    lemmas[s] = {wn.morphy(s.lower(), p) for p in "nvar"} - {None}
    for x in ss:
        for l in x.lemmas():
            if l.name().lower() == s.lower() or l.name().lower() in lemmas[s]:
                for a in l.antonyms():
                    anto[s].add(a.name().lower())

# derivational / pertainym lemma names reached from each surface's own lemmas
der = collections.defaultdict(set)
for s_ in syn:
    own = {s_.lower()} | lemmas[s_]
    for x in wn.synsets(s_.lower()):
        for l in x.lemmas():
            if l.name().lower() in own:
                for d in l.derivationally_related_forms() + l.pertainyms():
                    der[s_].add(d.name().lower())
in_wn = sorted(syn)
not_in_wn = [s for s in surfaces if s not in syn]

# index: synset -> surfaces, antonym lemma -> surfaces whose own lemma it is
by_syn = collections.defaultdict(list)
for s in in_wn:
    for x in syn[s]:
        by_syn[x].append(s)
by_lemma = collections.defaultdict(list)
for s in in_wn:
    for b in lemmas[s] | {s.lower()}:
        by_lemma[b].append(s)

shared = collections.Counter()
for x, ls in by_syn.items():
    for a, b in itertools.combinations(sorted(ls), 2):
        shared[(a, b)] += 1
same_base = {k for k in shared if lemmas[k[0]] & lemmas[k[1]]}
antn = collections.Counter()
for s in in_wn:
    for a in anto[s]:
        for t in by_lemma.get(a, []):
            if t != s:
                antn[tuple(sorted((s, t)))] += 1

derc = collections.Counter()
for s_ in in_wn:
    for nm in der[s_]:
        for t in by_lemma.get(nm, []):
            if t != s_:
                derc[tuple(sorted((s_, t)))] += 0
                derc[tuple(sorted((s_, t)))] = 1
simc = collections.Counter()
seen_sim = set()
for x in {wn.synset(n) for v in syn.values() for n in v}:
    for y in x.similar_tos():
        k = tuple(sorted((x.name(), y.name())))
        if k in seen_sim:
            continue
        seen_sim.add(k)
        for a in by_syn.get(x.name(), []):
            for b in by_syn.get(y.name(), []):
                if a != b:
                    simc[tuple(sorted((a, b)))] += 1
edges = {}
def edge(k):
    return edges.setdefault(k, {"syn": 0, "ant": 0, "der": 0, "sim": 0})
for k, v in shared.items():
    edge(k)["syn"] = v
for k, v in antn.items():
    edge(k)["ant"] = v
for k, v in derc.items():
    edge(k)["der"] = v
for k, v in simc.items():
    edge(k)["sim"] = v

G = nx.Graph()
G.add_nodes_from(surfaces)
for (a, b), d in edges.items():
    kind = ("same_base" if (a, b) in same_base else "both" if d["syn"] and d["ant"] else "synonym" if d["syn"] else
            "derivational" if d["der"] else "similar" if d["sim"] else "antonym")
    G.add_edge(a, b, weight=d["syn"] + d["ant"] + d["der"] + d["sim"], syn=d["syn"], ant=d["ant"], der=d["der"], sim=d["sim"], etype=kind)

comps = sorted(nx.connected_components(G), key=len, reverse=True)
comp_of = {n: i + 1 for i, c in enumerate(comps) for n in c}

# workbook
wb = Workbook()
def sheet(name, head, data, first=False):
    ws = wb.active if first else wb.create_sheet()
    ws.title = name
    ws.append(head)
    for c in ws[1]:
        c.font = Font(bold=True)
    for r in data:
        ws.append(list(r))
    ws.freeze_panes = "A2"
    for i, h in enumerate(head, 1):
        w = max([len(str(h))] + [len(str(r[i - 1])) for r in data[:300]])
        ws.column_dimensions[ws.cell(1, i).column_letter].width = min(w + 2, 90)

nbr = lambda n: sorted(G[n], key=lambda m: (-G[n][m]["weight"], m))
sheet("README", ["Notes"], [
    ["WordNet pairing of the single-word surfaces (researcher's request after #2545). Source list: behaviour-and-inner-state-surfaces-v3-20261109.csv, distinct surfaces with no space; no word outside the list is added."],
    ["WordNet 3.0 through NLTK. A pair = two surfaces of the list that WordNet links: synonym (share a synset; weight = synsets shared), antonym (antonym link between their lemmas; weight 1 per link), derivational (derivationally related form or pertainym: bold / boldness / boldly; weight 1), similar (similar-to between adjective sense groups: generous / bountiful; weight = sense-group links). A pair that holds several relations has the weights added; its type is the first that holds, in the order same_base, synonym (both with antonym), derivational, similar, antonym."],
    ["Surfaces with the same WordNet base form (walk / walked) are paired as same_base, weight = synsets shared, so words of one base sit together in the network."],
    ["WordNet is modern general English and an outside source: its links are not study findings and carry no inner-being reading. A surface can be linked through a sense that its verses never use."],
    [f"{len(surfaces)} single-word surfaces; {len(in_wn)} found in WordNet; {len(not_in_wn)} not in WordNet (listed, no pairs); {G.number_of_edges()} pairs; {sum(1 for c in comps if len(c) > 1)} connected groups of 2 or more; largest {len(comps[0])}; {sum(1 for c in comps if len(c) == 1)} surfaces with no pair."],
], first=True)
ws = wb["README"]; ws.column_dimensions["A"].width = 170

sheet("surface_pairs", ["surface", "surface_group", "in_wordnet", "pairs", "group_no", "paired_surfaces_with_weight"],
      [(n, "/".join(sorted(groups[n])), "yes" if n in syn else "no", G.degree(n), comp_of[n],
        ", ".join(f"{m} ({G[n][m]['weight']}{'a' if G[n][m]['etype'] != 'synonym' else ''})" for m in nbr(n))) for n in surfaces])
sheet("pairs", ["surface_a", "surface_b", "pair_type", "weight", "synsets_shared", "antonym_links", "derivational_links", "similar_links"],
      sorted(((a, b, d["etype"], d["weight"], d["syn"], d["ant"], d["der"], d["sim"]) for a, b, d in G.edges(data=True)), key=lambda x: (-x[3], x[0], x[1])))
sheet("groups", ["group_no", "surfaces", "pairs", "members"],
      [(i + 1, len(c), G.subgraph(c).number_of_edges(), ", ".join(sorted(c)) if len(c) > 1 else next(iter(c))) for i, c in enumerate(comps) if len(c) > 1])
sheet("not_in_wordnet", ["surface", "surface_group"], [(s, "/".join(sorted(groups[s]))) for s in not_in_wn])
wb.save(OUT / f"wordnet-surface-pairs-v3-{STAMP}.xlsx")

# diagram: surfaces with at least one pair, weighted spring layout
H = G.subgraph([n for n in G if G.degree(n) > 0]).copy()
pos = nx.spring_layout(H, weight="weight", k=0.35, iterations=300, seed=5)
cmap = {"inner_being_state": "#4472c4", "behaviour": "#e67e22", "(none)": "#999999"}
def col(n):
    g = groups[n]
    return cmap["inner_being_state"] if g == {"inner_being_state"} else cmap["behaviour"] if g == {"behaviour"} else "#8e5ea2" if len(g) > 1 else cmap["(none)"]
fig, ax = plt.subplots(figsize=(40, 40))
for t, c, ls in (("synonym", "#888888", "solid"), ("same_base", "#4472c4", "solid"), ("derivational", "#2e86ab", "dashed"), ("similar", "#8e5ea2", "dashed"), ("antonym", "#c0392b", "dotted"), ("both", "#1b7a3a", "solid")):
    es = [(a, b) for a, b, d in H.edges(data=True) if d["etype"] == t]
    nx.draw_networkx_edges(H, pos, edgelist=es, ax=ax, edge_color=c, style=ls, alpha=0.5, width=[0.3 + 0.5 * H[a][b]["weight"] for a, b in es])
nx.draw_networkx_nodes(H, pos, ax=ax, node_size=[40 + 14 * H.degree(n) for n in H], node_color=[col(n) for n in H], edgecolors="white", linewidths=0.3)
big = [n for n in H if H.degree(n) >= 6]
nx.draw_networkx_labels(H, pos, labels={n: n for n in big}, ax=ax, font_size=8)
from matplotlib.lines import Line2D
ax.legend(handles=[
    Line2D([0], [0], marker="o", color="w", markerfacecolor="#4472c4", markersize=14, label="inner-being-state surface"),
    Line2D([0], [0], marker="o", color="w", markerfacecolor="#e67e22", markersize=14, label="behaviour surface"),
    Line2D([0], [0], marker="o", color="w", markerfacecolor="#8e5ea2", markersize=14, label="surface in both groups"),
    Line2D([0], [0], color="#888888", lw=2, label="WordNet synonym pair (thicker = more shared senses)"),
    Line2D([0], [0], color="#4472c4", lw=2, label="same WordNet base form (walk, walked)"),
    Line2D([0], [0], color="#2e86ab", lw=2, ls="dashed", label="derivational form (bold, boldness, boldly)"),
    Line2D([0], [0], color="#8e5ea2", lw=2, ls="dashed", label="similar adjective sense groups (generous, bountiful)"),
    Line2D([0], [0], color="#c0392b", lw=2, ls="dotted", label="WordNet antonym pair"),
    Line2D([0], [0], color="#1b7a3a", lw=2, label="both synonym and antonym")], loc="lower left", fontsize=16)
ax.set_title(f"Single-word surfaces paired by WordNet: {H.number_of_nodes()} surfaces with a pair, {H.number_of_edges()} pairs\n"
             f"{len(surfaces) - H.number_of_nodes()} of {len(surfaces)} single-word surfaces have no pair and are not drawn (labels shown for surfaces with 6 or more pairs)", fontsize=24)
ax.axis("off"); fig.tight_layout()
fig.savefig(OUT / f"wordnet-surface-pairs-network-v3-{STAMP}.png", dpi=90)
fig.savefig(OUT / f"wordnet-surface-pairs-network-v3-{STAMP}.svg")

# distance matrices: shortest path over the pairs (hops; weighted with length 1 / weight)
import numpy as np
idx = {n: i for i, n in enumerate(surfaces)}
N = len(surfaces)
hop = np.full((N, N), -1, dtype=np.int32)
wtd = np.full((N, N), np.nan, dtype=np.float64)
for n in surfaces:
    i = idx[n]
    for m, d in nx.single_source_shortest_path_length(G, n).items():
        hop[i, idx[m]] = d
for u, v, d in G.edges(data=True):
    d["length"] = 1.0 / d["weight"]
for n in surfaces:
    i = idx[n]
    for m, d in nx.single_source_dijkstra_path_length(G, n, weight="length").items():
        wtd[i, idx[m]] = d
def write_matrix(path, m, fmt):
    with open(path, "w", encoding="utf-8-sig", newline="") as f:
        w = csv.writer(f)
        w.writerow(["surface"] + surfaces)
        for i, n in enumerate(surfaces):
            w.writerow([n] + [fmt(x) for x in m[i]])
write_matrix(OUT / f"wordnet-surface-distance-hops-v3-{STAMP}.csv", hop, lambda x: "" if x < 0 else int(x))
write_matrix(OUT / f"wordnet-surface-distance-weighted-v3-{STAMP}.csv", wtd, lambda x: "" if np.isnan(x) else round(float(x), 4))
reach = (hop >= 0).sum()
print("matrix", N, "x", N, "cells with a path", int(reach), "of", N * N, "; max hops", int(hop.max()), "; max weighted", round(float(np.nanmax(wtd)), 3))
print(len(surfaces), len(in_wn), len(not_in_wn), G.number_of_edges(), "same_base", sum(1 for _, _, d in G.edges(data=True) if d["etype"] == "same_base"), "drawn", H.number_of_nodes(),
      "groups", [len(c) for c in comps[:8]], "isolated", sum(1 for c in comps if len(c) == 1))
print(collections.Counter(d["etype"] for _, _, d in G.edges(data=True)))
