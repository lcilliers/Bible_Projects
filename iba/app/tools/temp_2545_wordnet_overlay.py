"""Researcher request after #2545: overlay the current collections on the surface-level WordNet network (first round: the overlay and how well the two agree).

Input : wordnet-surface-pairs-v3-20261123.xlsx (sheets surface_pairs and pairs), wordnet-surface-distance-weighted-v3-20261123.csv (the weighted distance matrix),
        collections-v3-20261123.csv (a surface's collection = the collection whose member tier holds the word; member tiers core, synonym, opposite, gathered, phrase;
        no word is a member of two). Single-word surfaces only, as the pairing.
Output: _analytics/surfaces/exports/wordnet-collection-overlay-v1-20261123.xlsx and wordnet-collection-overlay-network-v1-20261123.png / .svg
        (the same network and layout as the pairing diagram; node colour = collection for the 18 largest collections in the network, grey = another collection,
        white = no collection; a pair inside one collection is drawn dark, a pair across collections light).
Read-only on the project. Temporary script (temp_ prefix). WordNet is an outside source: agreement or disagreement with a collection is a check, not a finding.
"""
import csv, collections, itertools, pathlib
import numpy as np
import networkx as nx
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from openpyxl import load_workbook, Workbook
from openpyxl.styles import Font

ROOT = pathlib.Path(__file__).resolve().parents[3]
EXP = ROOT / "_analytics" / "surfaces" / "exports"
S = "20261123"
MEMBER = {"core", "synonym", "opposite", "gathered", "phrase"}

wb = load_workbook(EXP / f"wordnet-surface-pairs-v3-{S}.xlsx", read_only=True)
surf = [(r[0], r[1], r[3]) for r in wb["surface_pairs"].iter_rows(min_row=2, values_only=True)]
names = [x[0] for x in surf]
edges = [(r[0], r[1], r[2], r[3]) for r in wb["pairs"].iter_rows(min_row=2, values_only=True)]

coll = {}
tier = {}
for r in csv.DictReader(open(EXP / f"collections-v3-{S}.csv", encoding="utf-8-sig")):
    if r["tier"] in MEMBER and " " not in r["word"].strip():
        w = r["word"].lower()
        if w not in coll:
            coll[w] = r["collection"]
            tier[w] = r["tier"]
cof = {n: coll.get(n.lower()) for n in names}
has = [n for n in names if cof[n]]

G = nx.Graph()
G.add_nodes_from(names)
for a, b, t, w in edges:
    G.add_edge(a, b, weight=w, etype=t)

same = diff = nocol = 0
internal = collections.Counter(); external = collections.Counter(); to_none = collections.Counter(); cross = collections.Counter()
for a, b, t, w in edges:
    ca, cb = cof[a], cof[b]
    if ca and cb:
        if ca == cb:
            same += 1; internal[ca] += 1
        else:
            diff += 1; external[ca] += 1; external[cb] += 1; cross[tuple(sorted((ca, cb)))] += 1
    else:
        nocol += 1
        for c in (ca, cb):
            if c:
                to_none[c] += 1
size = collections.Counter(cof[n] for n in has)
N = len(has)
expected_same = sum(v * (v - 1) for v in size.values()) / (N * (N - 1))
observed_same = same / (same + diff) if same + diff else 0

# weighted distance, inside collections against all surfaces
idx = {n: i for i, n in enumerate(names)}
M = np.full((len(names), len(names)), np.nan)
with open(EXP / f"wordnet-surface-distance-weighted-v3-{S}.csv", encoding="utf-8-sig") as f:
    rd = csv.reader(f)
    next(rd)
    for i, row in enumerate(rd):
        M[i, :] = [float(x) if x else np.nan for x in row[1:]]
tri = M[np.triu_indices(len(names), 1)]
all_mean = float(np.nanmean(tri))
rows_c = []
for c in sorted(size, key=lambda x: -size[x]):
    mem = [n for n in has if cof[n] == c]
    ii = [idx[n] for n in mem]
    sub = M[np.ix_(ii, ii)][np.triu_indices(len(ii), 1)] if len(ii) > 1 else np.array([])
    reach = int(np.sum(~np.isnan(sub))) if sub.size else 0
    mean_in = float(np.nanmean(sub)) if reach else None
    withpair = sum(1 for n in mem if G.degree(n) > 0)
    with_internal = sum(1 for n in mem if any(cof[m] == c for m in G[n]))
    rows_c.append((c, len(mem), withpair, with_internal, internal[c], external[c], to_none[c],
                   round(internal[c] / (internal[c] + external[c] + to_none[c]), 3) if (internal[c] + external[c] + to_none[c]) else None,
                   reach, round(mean_in, 3) if mean_in is not None else None))

out = Workbook()
ws = out.active; ws.title = "README"
for line in [
    "Overlay of the collections on the surface-level WordNet network (researcher's request after #2545). First round.",
    "A surface's collection is the collection whose member tier (core, synonym, opposite, gathered, phrase) holds the word in collections-v3-20261123.csv; single-word surfaces only; no surface is a member of two collections.",
    f"{len(names)} single-word surfaces; {N} have a collection; {len(names) - N} have none. {len(edges)} WordNet pairs.",
    f"Pairs with a collection at both ends: {same + diff}; inside one collection: {same} ({observed_same:.1%}); across two collections: {diff}. Pairs with a surface that has no collection: {nocol}.",
    f"If pairs fell at random among the surfaces that have a collection, {expected_same:.1%} would fall inside one collection: WordNet pairs fall inside a collection {observed_same / expected_same:.1f} times as often as chance.",
    f"Mean weighted distance (reachable pairs; shorter = nearer): all surfaces {all_mean:.2f}; see collection_cohesion for each collection's own mean.",
    "collection_a_b: for each two collections that WordNet pairs across (collection_pairs, most pairs first): every surface of both, its original collection, and the surfaces it is WordNet-paired with inside collection a (pairing a) and inside collection b (pairing b), each with its weight.",
    "collection_cohesion: members_in_network = members with a collection (single words); with_any_pair = members with at least one WordNet pair; with_pair_inside = members with a pair to another member of the same collection; internal_share = pairs inside / (inside + to other collections + to surfaces with no collection).",
    "WordNet is an outside source and modern English: agreement is support for a placement, disagreement is a case to read, not a verdict."]:
    ws.append([line])
ws.column_dimensions["A"].width = 190
def sheet(name, head, data):
    w = out.create_sheet(name); w.append(head)
    for c in w[1]: c.font = Font(bold=True)
    for r in data: w.append(list(r))
    w.freeze_panes = "A2"
    for i in range(1, len(head) + 1): w.column_dimensions[w.cell(1, i).column_letter].width = 22
sheet("collection_cohesion", ["collection", "members_in_network", "with_any_pair", "with_pair_inside", "pairs_inside", "pairs_to_other_collections", "pairs_to_no_collection",
                              "internal_share", "reachable_member_pairs", "mean_weighted_distance_inside"], rows_c)
sheet("surface_collection", ["surface", "surface_group", "collection", "tier", "pairs", "pairs_inside_collection", "pairs_other_collection", "pairs_no_collection"],
      [(n, g, cof[n] or "", tier.get(n.lower(), ""), G.degree(n),
        sum(1 for m in G[n] if cof[n] and cof[m] == cof[n]), sum(1 for m in G[n] if cof[n] and cof[m] and cof[m] != cof[n]),
        sum(1 for m in G[n] if not cof[m])) for n, g, d in surf])
sheet("collection_pairs", ["collection_a", "collection_b", "wordnet_pairs"], [(a, b, v) for (a, b), v in cross.most_common()])
# one sheet for every two collections that WordNet pairs across: the surfaces of both and the pairings each surface has inside each of the two (researcher's request)
members = collections.defaultdict(list)
for n in has:
    members[cof[n]].append(n)
def partners(n, c):
    ps = sorted((m for m in G[n] if cof[m] == c), key=lambda m: (-G[n][m]["weight"], m))
    return ", ".join(f"{m} ({G[n][m]['weight']})" for m in ps)
ab_rows = []
for (a, b), v in cross.most_common():
    for c in (a, b):
        for n in sorted(members[c]):
            ab_rows.append((n, cof[n], a, b, partners(n, a), partners(n, b)))
sheet("collection_a_b", ["surface", "original collection", "collection a", "collection b", "pairing a", "pairing b"], ab_rows)
out["collection_a_b"].column_dimensions["E"].width = 60
out["collection_a_b"].column_dimensions["F"].width = 60
out.save(EXP / f"wordnet-collection-overlay-v1-{S}.xlsx")

# diagram: the same network and layout as the pairing diagram
H = G.subgraph([n for n in G if G.degree(n) > 0]).copy()
pos = nx.spring_layout(H, weight="weight", k=0.35, iterations=300, seed=5)
top = [c for c, _ in collections.Counter(cof[n] for n in H if cof[n]).most_common(18)]
pal = [c for i, c in enumerate(plt.get_cmap("tab20").colors) if i not in (14, 15)]   # tab20 without its two greys: grey means another collection
colour = {c: pal[i] for i, c in enumerate(top)}
def col(n):
    c = cof[n]
    return colour[c] if c in colour else "#c8c8c8" if c else "#ffffff"
fig, ax = plt.subplots(figsize=(40, 40))
cross_e = [(a, b) for a, b in H.edges if not (cof[a] and cof[a] == cof[b])]
in_e = [(a, b) for a, b in H.edges if cof[a] and cof[a] == cof[b]]
nx.draw_networkx_edges(H, pos, edgelist=cross_e, ax=ax, edge_color="#bbbbbb", alpha=0.25, width=0.4)
nx.draw_networkx_edges(H, pos, edgelist=in_e, ax=ax, edge_color="#222222", alpha=0.7, width=1.6)
nx.draw_networkx_nodes(H, pos, ax=ax, node_size=[50 + 14 * H.degree(n) for n in H], node_color=[col(n) for n in H], edgecolors=["#888888" if not cof[n] else "white" for n in H], linewidths=0.6)
for c in top:
    pts = np.array([pos[n] for n in H if cof[n] == c])
    ax.text(*pts.mean(axis=0), c, fontsize=20, fontweight="bold", ha="center", va="center", bbox=dict(facecolor="white", alpha=0.65, edgecolor="none", pad=1.5))
ax.legend(handles=[Line2D([0], [0], marker="o", color="w", markerfacecolor=colour[c], markersize=14, label=f"{c} ({size[c]})") for c in top] + [
    Line2D([0], [0], marker="o", color="w", markerfacecolor="#c8c8c8", markersize=14, label="another collection"),
    Line2D([0], [0], marker="o", color="w", markerfacecolor="#ffffff", markeredgecolor="#888888", markersize=14, label="no collection"),
    Line2D([0], [0], color="#222222", lw=3, label="WordNet pair inside one collection"),
    Line2D([0], [0], color="#bbbbbb", lw=2, label="WordNet pair across collections or to a surface with no collection")], loc="lower left", fontsize=14, ncol=2)
ax.set_title(f"Collections overlaid on the WordNet network of single-word surfaces: {same} of {same + diff} pairs between placed surfaces fall inside one collection "
             f"({observed_same:.0%}; chance {expected_same:.1%})\n18 largest collections coloured; WordNet is an outside check", fontsize=22)
ax.axis("off"); fig.tight_layout()
fig.savefig(EXP / f"wordnet-collection-overlay-network-v1-{S}.png", dpi=90)
fig.savefig(EXP / f"wordnet-collection-overlay-network-v1-{S}.svg")
print(N, len(names) - N, "pairs inside/across/none:", same, diff, nocol, f"observed {observed_same:.3f} expected {expected_same:.4f} ratio {observed_same / expected_same:.1f}", "mean all", round(all_mean, 2))
for r in rows_c[:12]:
    print(r)
