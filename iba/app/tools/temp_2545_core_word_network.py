"""Escalation #2545 (the researcher's finding on grace-type words): the core words of the collections as a modelled association network.

Input: the `core` column of _analytics/surfaces/exports/collections-v3-20261123.csv only. The links are Claude's own linguistic association model
(semantic fields + specific collocation pairs): INFERENTIAL (B:4), not measured co-occurrence and not study data. Read-only on the project; writes
core-word-network-v1-20261123.png/.svg to the exports folder (or the folder given as the first argument). Temporary script (temp_ prefix).
"""
import csv, itertools, sys, pathlib
import networkx as nx
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ROOT = pathlib.Path(__file__).resolve().parents[3]
SRC = str(ROOT / "_analytics" / "surfaces" / "exports" / "collections-v3-20261123.csv")
OUT = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / "_analytics" / "surfaces" / "exports"

rows = list(csv.DictReader(open(SRC, encoding="utf-8-sig")))
cores = sorted({r["core"] for r in rows})

# Model: general English word-association knowledge (no study data). Two parts:
# 1. semantic fields (words that share a field tend to occur in the same context): +1 per shared field
# 2. specific collocation / strong association pairs: +3
FIELDS = {
 "speech": "preach utter profess confess witness exhort warn teach command commend call promise whisper mutter roar blaspheme boast scoff chide ask supplication thank sing lament utter",
 "praise": "bless thank sing honor magnify majesty reverence serve dedicate offer commend renown godly solemn fear",
 "trust": "strengthen believe trust hope wait faithless loyalty firm endure confess convince earnest ready continual",
 "knowing": "know wise skill thought teach hear search count distinction intend convince real watch taste guard impartial self-control",
 "righteous": "righteous upright innocent godly justify impartial cleanse tenderhearted hospitality self-control loyalty forgive honor",
 "evil": "sin evildoer lawless crime deceive betray plot entice greed folly uncircumcised unclean abominable adultery willful rebel backsliding astray forsake kill cruel oppress shatter quarrel jealous anger",
 "pride": "pride boast abase submission scoff rich mighty chief bold willful magnify majesty",
 "joy": "delight gladden laugh sing comfort refresh love desire hope beauty care taste",
 "distress": "dry pain lament tribulation trial fear faint amazement confusion tumult disease anger jealous die bondage destruction cruel oppress roar",
 "conflict": "compel combat kill strive quarrel shatter destruction oppress cruel prevail snatch anger rebel tumult condemn",
 "judgment": "compel reject condemn justify reward govern command warn chide destruction convince impartial righteous crime trial",
 "turning": "reject repent return turn depart backsliding astray forsake change forgive confess cleanse remove escape save stumble",
 "life": "live die kill save disease destruction endure escape heritage",
 "giving": "strengthen supply share benefit offer fill hospitality reward heritage rich bless promise dedicate forgive",
 "mind": "heart thought intend desire know forget hard harden earnest willful consent choose count",
 "hardness": "dry reject hard harden firm cruel blind uncircumcised mute willful rebel stumble",
 "perception": "hear watch blind search taste open mute know witness guard",
 "fulfilment": "fulfill performing promise build labor prevail serve ready continual endure sloth",
 "ritual": "dedicate offer cleanse unclean uncircumcised solemn fast covered abominable confess heritage",
 "bonds": "bondage loosen united share loyalty love care hospitality combat",
}
PAIRS = """compel:command reject:forsake strengthen:comfort dry:faint dry:die fear:reverence fear:trust fear:godly fear:amazement hear:teach hear:open love:delight love:loyalty love:care sin:repent repent:return
return:turn forgive:repent forgive:sin forgive:covered harden:heart heart:thought heart:desire know:wise wise:skill righteous:upright righteous:justify
condemn:justify kill:die die:live save:escape blind:open bless:thank thank:sing sing:gladden gladden:delight pain:tribulation trial:tribulation
trial:endure endure:wait wait:hope hope:trust trust:believe believe:confess preach:teach warn:exhort exhort:comfort comfort:refresh boast:pride
pride:abase abase:submission deceive:betray entice:deceive plot:deceive quarrel:strive strive:combat anger:chide anger:quarrel jealous:anger
oppress:cruel shatter:destruction lawless:sin crime:sin evildoer:sin unclean:cleanse cleanse:forgive uncircumcised:unclean adultery:unclean
adultery:faithless faithless:backsliding backsliding:turn astray:turn stumble:astray honor:majesty majesty:renown magnify:honor mighty:prevail
rich:greed greed:desire sloth:labor labor:serve serve:submission supplication:ask ask:call call:command promise:fulfill fulfill:performing
command:fulfill hospitality:share share:supply supply:benefit reward:benefit heritage:promise tenderhearted:forgive tenderhearted:comfort
self-control:wise fast:supplication fast:lament lament:roar mutter:whisper whisper:utter utter:profess scoff:blaspheme chief:govern
govern:command combat:prevail snatch:save remove:depart loosen:bondage die:disease disease:pain confusion:tumult tumult:roar faint:fear
taste:delight desire:delight beauty:delight innocent:righteous impartial:justify guard:watch watch:wait watch:warn search:know search:ask
count:know convince:believe intend:plot intend:thought consent:choose choose:desire solemn:reverence dedicate:offer offer:serve build:labor
distinction:impartial earnest:hope earnest:continual firm:endure united:share forsake:depart forget:forsake follow:serve willful:rebel
rebel:lawless harden:hard hard:firm""".split()

score = {}
def add(a, b, w):
    if a == b: return
    k = tuple(sorted((a, b)))
    score[k] = score.get(k, 0) + w

membership = {c: [] for c in cores}
for f, ws in FIELDS.items():
    ws = sorted(set(ws.split()))
    for w in ws:
        assert w in membership, f"{w} in field {f} is not a core"
        membership[w].append(f)
    for a, b in itertools.combinations(ws, 2):
        add(a, b, 1)
for p in PAIRS:
    a, b = p.split(":")
    assert a in membership and b in membership, p
    add(a, b, 3)

# keep an edge if it is a specific pair (>=3) or two fields shared; cap weaker links to each node's 3 best
G = nx.Graph()
G.add_nodes_from(cores)
for (a, b), s in score.items():
    if s >= 3:
        G.add_edge(a, b, weight=s)
isolated = [n for n in G if G.degree(n) == 0]
# connect words without a strong link by their best field link
for n in isolated:
    best = sorted(((s, k) for k, s in score.items() if n in k), reverse=True)[:2]
    for s, (a, b) in best:
        G.add_edge(a, b, weight=s)

comms = nx.community.greedy_modularity_communities(G, weight="weight")
cmap = {}
palette = plt.get_cmap("tab20").colors
for i, c in enumerate(sorted(comms, key=len, reverse=True)):
    for n in c: cmap[n] = palette[i % 20]

pos = nx.spring_layout(G, weight="weight", k=0.9, iterations=400, seed=7)
fig, ax = plt.subplots(figsize=(26, 26))
ws = [G[a][b]["weight"] for a, b in G.edges]
nx.draw_networkx_edges(G, pos, ax=ax, width=[0.4 + 0.35 * w for w in ws], alpha=0.35, edge_color="#666666")
nx.draw_networkx_nodes(G, pos, ax=ax, node_size=[160 + 60 * G.degree(n) for n in G], node_color=[cmap[n] for n in G], edgecolors="white", linewidths=1)
nx.draw_networkx_labels(G, pos, ax=ax, font_size=10)
ax.set_title(f"Core words of the collections: modelled association network ({G.number_of_nodes()} words, {G.number_of_edges()} links, {len(comms)} groups)\n"
             "Source: core column of collections-v3-20261123.csv; links are Claude's own linguistic association model (inferential), thicker = stronger", fontsize=18)
ax.axis("off")
fig.tight_layout()
fig.savefig(OUT / "core-word-network-v1-20261123.png", dpi=110)
fig.savefig(OUT / "core-word-network-v1-20261123.svg")
print(G.number_of_nodes(), G.number_of_edges(), len(comms), [len(c) for c in comms])
for c in sorted(comms, key=len, reverse=True): print(len(c), ", ".join(sorted(c)))
