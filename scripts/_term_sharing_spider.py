"""Generate term-sharing spider/network diagram showing pools of connected words."""
import sqlite3
import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
from collections import defaultdict
import math

DB = os.path.join(os.path.dirname(__file__), "..", "data", "bible_research.db")
OUT = os.path.join(os.path.dirname(__file__), "..", "outputs")


def main():
    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row

    # Word names
    names = {}
    clusters = {}
    for r in conn.execute("SELECT no, word, cluster_assignment FROM word_registry"):
        names[r["no"]] = r["word"]
        clusters[r["no"]] = r["cluster_assignment"]

    # Build pairwise sharing matrix (only active, non-excluded)
    pairs = conn.execute("""
        SELECT fi1.registry_id as reg1, fi2.registry_id as reg2,
               COUNT(DISTINCT ti1.strongs_number) as shared_terms
        FROM wa_term_inventory ti1
        JOIN wa_file_index fi1 ON fi1.id = ti1.file_id
        JOIN wa_term_inventory ti2 ON ti2.strongs_number = ti1.strongs_number
             AND ti2.id != ti1.id AND ti2.delete_flagged = 0
        JOIN wa_file_index fi2 ON fi2.id = ti2.file_id
        JOIN word_registry wr1 ON wr1.id = fi1.word_registry_fk AND wr1.phase1_status != 'Excluded'
        JOIN word_registry wr2 ON wr2.id = fi2.word_registry_fk AND wr2.phase1_status != 'Excluded'
        WHERE ti1.delete_flagged = 0
        AND fi1.registry_id < fi2.registry_id
        GROUP BY fi1.registry_id, fi2.registry_id
        ORDER BY shared_terms DESC
    """).fetchall()

    conn.close()

    # Print top connections
    print(f"Total pairs with shared terms: {len(pairs)}")
    print(f"\nTop 30 strongest connections:")
    print(f"{'Word 1':<22} {'Word 2':<22} {'Shared':>6}")
    print("-" * 55)
    for p in pairs[:30]:
        w1 = names.get(p["reg1"], f"?{p['reg1']}")
        w2 = names.get(p["reg2"], f"?{p['reg2']}")
        print(f"{w1:<22} {w2:<22} {p['shared_terms']:>6}")

    # Build pools at different thresholds
    for threshold in [15, 10, 5]:
        filtered = [(p["reg1"], p["reg2"], p["shared_terms"]) for p in pairs if p["shared_terms"] >= threshold]

        # Union-find for connected components
        parent = {}
        def find(x):
            if x not in parent:
                parent[x] = x
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        def union(x, y):
            parent[find(x)] = find(y)

        for r1, r2, _ in filtered:
            union(r1, r2)

        components = defaultdict(set)
        for node in parent:
            components[find(node)].add(node)

        pools = sorted(components.values(), key=lambda s: -len(s))
        print(f"\n=== POOLS at threshold >= {threshold} shared terms ===")
        for i, pool in enumerate(pools):
            if len(pool) < 2:
                continue
            members = sorted(pool)
            word_list = ", ".join(f"{names.get(m, '?')}({m})" for m in members[:15])
            if len(members) > 15:
                word_list += f" ... +{len(members)-15} more"
            # Count internal edges
            edges = [(r1, r2, c) for r1, r2, c in filtered if r1 in pool and r2 in pool]
            print(f"  Pool {i+1}: {len(members)} words, {len(edges)} connections")
            print(f"    {word_list}")

    # Generate network diagram for threshold=10
    fig, axes = plt.subplots(1, 2, figsize=(24, 14))
    fig.suptitle("Term Sharing Network — Pools of Connected Registries", fontsize=16, fontweight="bold")

    for ax_idx, (threshold, ax) in enumerate([(15, axes[0]), (8, axes[1])]):
        filtered = [(p["reg1"], p["reg2"], p["shared_terms"]) for p in pairs if p["shared_terms"] >= threshold]

        # Get all nodes
        nodes = set()
        for r1, r2, _ in filtered:
            nodes.add(r1)
            nodes.add(r2)
        nodes = sorted(nodes)

        if not nodes:
            ax.text(0.5, 0.5, f"No connections at threshold={threshold}", transform=ax.transAxes, ha="center")
            continue

        # Layout: circular by cluster
        cluster_groups = defaultdict(list)
        for n in nodes:
            cl = clusters.get(n, "?")
            cluster_groups[cl].append(n)

        # Assign positions
        pos = {}
        total = len(nodes)
        angle_step = 2 * math.pi / total
        i = 0
        for cl in sorted(cluster_groups.keys()):
            for n in cluster_groups[cl]:
                angle = i * angle_step
                pos[n] = (math.cos(angle), math.sin(angle))
                i += 1

        # Cluster colors
        cluster_colors = {}
        cmap = plt.cm.get_cmap("tab20", 22)
        for ci, cl in enumerate(sorted(set(clusters.values()))):
            cluster_colors[cl] = cmap(ci)

        # Draw edges
        max_weight = max(c for _, _, c in filtered) if filtered else 1
        for r1, r2, count in filtered:
            if r1 in pos and r2 in pos:
                width = 0.5 + (count / max_weight) * 3
                alpha = 0.15 + (count / max_weight) * 0.4
                ax.plot([pos[r1][0], pos[r2][0]], [pos[r1][1], pos[r2][1]],
                        color="#888", linewidth=width, alpha=alpha, zorder=1)

        # Draw nodes
        for n in nodes:
            cl = clusters.get(n, "?")
            color = cluster_colors.get(cl, "#999")
            ax.scatter(*pos[n], s=120, color=color, edgecolors="#333", linewidth=0.5, zorder=2)
            name = names.get(n, str(n))
            if len(name) > 12:
                name = name[:11] + "."
            ax.annotate(name, pos[n], fontsize=5, ha="center", va="bottom",
                        xytext=(0, 5), textcoords="offset points")

        ax.set_title(f"Threshold: {threshold}+ shared terms ({len(nodes)} words, {len(filtered)} connections)", fontsize=12)
        ax.set_xlim(-1.3, 1.3)
        ax.set_ylim(-1.3, 1.3)
        ax.set_aspect("equal")
        ax.axis("off")

    # Legend
    legend_patches = []
    for cl in sorted(cluster_colors.keys())[:12]:
        legend_patches.append(mpatches.Patch(color=cluster_colors[cl], label=cl))
    axes[1].legend(handles=legend_patches, loc="lower right", fontsize=7, ncol=2, title="Cluster")

    plt.tight_layout(rect=[0, 0, 1, 0.96])
    out_path = os.path.join(OUT, "term_sharing_network_20260328.png")
    plt.savefig(out_path, dpi=150, bbox_inches="tight")
    print(f"\nChart saved: {out_path}")
    plt.close()


if __name__ == "__main__":
    main()
