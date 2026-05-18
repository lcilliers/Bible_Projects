"""M49 schema migration + M04 characteristic-and-observation data load.

Adds three new tables per researcher-approved proposal 2026-05-18:
- characteristic
- characteristic_subgroup
- cluster_observation

Loads M04's v4 characteristic map data:
- 7 characteristic rows
- 17 characteristic_subgroup links (16 sub-groups + M04-E partial second link)
- 4 cluster_observation rows (Phase 9 carry-forward notes)

Bumps schema_version from 3.22.0 to 3.23.0.

All operations run in a single transaction. Write apply report at:
  Sessions/Session_Clusters/M04/WA-M04-characteristic-load-applied-v1-{date}.md
"""
from __future__ import annotations
import json
import sqlite3
from datetime import datetime, timezone
from pathlib import Path

DB = Path("database/bible_research.db")
TODAY = datetime.now().strftime("%Y%m%d")
NOW_UTC = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
SOURCE = "M04-characteristic-map-v4-20260518"
OUT = Path(f"Sessions/Session_Clusters/M04/WA-M04-characteristic-load-applied-v1-{TODAY}.md")

# ---------------------------------------------------------------------------
# M04 characteristic data (lifted verbatim from v4 map)
# ---------------------------------------------------------------------------

M04_CHARACTERISTICS = [
    {
        "seq": 1,
        "short_name": "Exultation",
        "definition": (
            "The soul's active, surging, triumphant inner state directed at what is glorious or transcendent — "
            "above all at God. The inner being rises in exultant response. Distinguished from Joy by intensity "
            "and directedness; the person who exults is overwhelmed upward toward their object. In Scripture this "
            "is almost always Godward: the soul exults in YHWH's salvation, in his holy name, in his mighty acts."
        ),
    },
    {
        "seq": 2,
        "short_name": "Joy",
        "definition": (
            "The active inner experience of rejoicing — the soul's engaged, participatory delight in what is "
            "worth celebrating. Joy is less surging than Exultation and more active than Gladness. It is the "
            "inner being rejoicing in something: in the Lord, in community, in shared celebration, in what is "
            "promised and coming. The commanded 'rejoice in the Lord always' is Joy — an active inner disposition "
            "of engagement, not merely a warm background feeling."
        ),
    },
    {
        "seq": 3,
        "short_name": "Gladness",
        "definition": (
            "The inner state of settled, warm, positive brightness — the heart that is glad, the soul whose inner "
            "condition is light and well. Gladness is less active than Joy (which rejoices in something) and more "
            "diffuse: a quality of inner being rather than a directed act. It includes the cognitive face of the "
            "same state — the soul's recognition that things are good, which produces and expresses the gladness. "
            "The person who is glad has a positively-coloured inner condition."
        ),
    },
    {
        "seq": 4,
        "short_name": "Delight",
        "definition": (
            "The inner state of treasuring and taking pleasure in a specific object — the soul's resting "
            "satisfaction in what it loves. Delight is more object-focused than Gladness and more receptive than "
            "Exultation. The person who delights has found something that satisfies their inner being: they rest "
            "in it, return to it, orient themselves toward it. Includes the affective pleasure of the soul in "
            "God's word, the volitional orientation of the will toward what pleases, and — in its disordered form "
            "— the soul's misplaced treasuring of wrong objects."
        ),
    },
    {
        "seq": 5,
        "short_name": "Pleasure",
        "definition": (
            "The inner-being experience of pleasantness — the felt quality of agreeableness received from persons, "
            "relationships, creation, and material or sensory experience. Pleasure is the soul's positive receptive "
            "response to what is pleasant. Less directed than Delight (which focuses on a specific treasured object) "
            "and less active than Joy — Pleasure is the inner being's sense of agreeableness and satisfying ease "
            "in what surrounds it."
        ),
    },
    {
        "seq": 6,
        "short_name": "Wonder",
        "definition": (
            "The inner state of astonishment and awe before what exceeds ordinary comprehension — the soul "
            "arrested and overwhelmed by what it cannot fully grasp. Wonder is the inner being stilled rather than "
            "surging: it confronts what is too great to simply rejoice at. Includes wonder as proclamation "
            "(declaring the marvellous), wonder as incomprehensibility (too great to comprehend), and wonder as "
            "dark astonishment (appalling awe at what is terrible or wrong). Distinguished from Exultation by its "
            "arrested, contemplative character; from Joy by its perceptual-receptive rather than participatory "
            "character."
        ),
    },
    {
        "seq": 7,
        "short_name": "Suffering-Joy",
        "definition": (
            "The paradoxical inner capacity to find genuine joy in and through suffering — not merely alongside "
            "it, not despite it, but as an inner state that suffering itself produces or occasions. This is a "
            "distinct inner-being capacity from Joy (which rejoices in what is good) and from Gladness (which is "
            "the warm inner state of one whose condition is well): it is the soul's ability to genuinely rejoice "
            "when circumstances are against it, grounded in what suffering reveals or produces. The verse evidence "
            "is present: commanded rejoicing in trials (Jas 1:2), joy in tribulation producing proven character "
            "(Rom 5:3-5), rejoicing in present sufferings oriented to coming glory (1 Pet 1:6-8), and the fragile "
            "attempted cheerfulness of those under extreme adversity."
        ),
    },
]

# Sub-group → characteristic links. Tuples: (char_seq, sg_code, qualifier_note, is_partial, partial_register_note)
M04_CHAR_SUBGROUP_LINKS = [
    (1, "M04-A", "The Godward qualifier — exultation directed toward YHWH as object and ground; the primary and sole register of this characteristic in M04.", 0, None),
    (2, "M04-B", "The communal-festive qualifier — Joy enacted in community, structured by appointed feast and corporate worship; primary OT rejoicing vocabulary (sa.mach, sim.chah).", 0, None),
    (2, "M04-C", "The NT Spirit-and-Christ qualifier — Joy arising from faith in Christ, mediated by the indwelling Spirit, shaped by the gospel community; primary NT rejoicing vocabulary (chairo, chara).", 0, None),
    (2, "M04-D", "The solidarity qualifier — Joy constitutively shared: sought and completed through another's rejoicing (sunchairo).", 0, None),
    (2, "M04-E", "The eschatological qualifier — Joy oriented toward the not-yet; the soul's forward-engaged rejoicing grounded in divine promise of restoration.", 1, "Eschatological register (sa.s.von) — distinct from M04-E's suffering-paradox register which serves Characteristic 7."),
    (3, "M04-L", "The evaluative-cognitive qualifier — the soul's inner appraisal of what is genuinely good; the cognitive face of gladness: the assessment that produces and expresses the glad inner state.", 0, None),
    (3, "M04-O", "The circumstantial qualifier — gladness as the soul's warm inner response to good news, beneficial states, and refreshing circumstance.", 0, None),
    (4, "M04-G", "The divine-word qualifier — affective delight in God's word, law, testimonies, and YHWH himself as the treasured object.", 0, None),
    (4, "M04-H", "The volitional qualifier — delight as the will's orientation: sovereign willing-pleasure, directed inner resolve toward its object.", 0, None),
    (4, "M04-M", "The obedience qualifier — delight as the soul's orientation toward what is acceptable and pleasing to God; the compliance register of volitional delight.", 0, None),
    (4, "M04-N", "The relational-horizontal qualifier — delight in persons: parental attachment, the treasured nearness of a neighbour.", 0, None),
    (4, "M04-P", "The corrupt qualifier — delight misdirected toward evil objects, persons, and practices; the disordered face of the same capacity.", 0, None),
    (5, "M04-J", "The relational qualifier — pleasantness as the quality of what is agreeable in persons, bonds, speech, and creation.", 0, None),
    (5, "M04-K", "The sensory-material qualifier — pleasure registered through bodily and material experience: luxury, the soothing aroma of righteous worship, sensory satisfaction.", 0, None),
    (6, "M04-I", "The primary register — wonder at God's extraordinary works, their incomprehensibility, and dark astonishment at what is appalling.", 0, None),
    (7, "M04-E", "The suffering-paradox register — joy coexisting with and arising from suffering; forward-oriented rejoicing grounded in the promise of what suffering produces.", 1, "Suffering-paradox register (agalliao) — distinct from M04-E's eschatological register which serves Characteristic 2."),
    (7, "M04-F", "The fragile-composure qualifier — cheerfulness as a desired or attempted inner state under extreme adversity; the tenuous, barely-attained face of the same capacity.", 0, None),
]

# Cluster observations from v4 map's "Notes for Phase 9"
M04_OBSERVATIONS = [
    {
        "source_phase": "characteristic_mapping",
        "observation_type": "INTER_RELATIONSHIP",
        "target_phase": "phase_9_findings",
        "title": "Joy/Gladness inter-relationship within M04-B and M04-C",
        "description": (
            "M04-B (Communal/Festive Rejoicing) and M04-C (NT Joy in Christ) carry BOTH the active-rejoicing "
            "register (Joy, Characteristic 2) and the settled-warm register (Gladness, Characteristic 3) within "
            "their verse corpora. The characteristic map assigns these sub-groups to Joy as their dominant "
            "phenomenon; the Gladness dimension within them is expected to emerge from VCG-level analysis. This "
            "inter-relationship between Joy and Gladness is anticipated as one of the significant findings of "
            "Phase 9 for M04."
        ),
        "characteristic_seq": 2,
    },
    {
        "source_phase": "characteristic_mapping",
        "observation_type": "SPLIT_SUBGROUP",
        "target_phase": "phase_9_findings",
        "title": "M04-E serves both Characteristic 2 (Joy) and Characteristic 7 (Suffering-Joy)",
        "description": (
            "M04-E (Promised and Eschatological Joy) carries two distinct registers within its 35-verse corpus. "
            "Its eschatological forward-rejoicing register (sa.s.von — gladness promised as reversal of sorrow) "
            "belongs under Characteristic 2 — Joy. Its NT suffering-paradox register (agalliao — rejoicing in "
            "trials; joy that suffering itself occasions) belongs under Characteristic 7 — Suffering-Joy. The VCG "
            "structure within M04-E will show which VCGs serve which characteristic. Phase 9 should apply the 189 "
            "prompts to M04-E under both Characteristic 2 and Characteristic 7 separately, where the evidence permits."
        ),
        "characteristic_seq": None,
        "subgroup_code": "M04-E",
    },
    {
        "source_phase": "characteristic_mapping",
        "observation_type": "INTER_RELATIONSHIP",
        "target_phase": "phase_9_findings",
        "title": "Delight's breadth — affective/volitional/obedience/relational/corrupt inter-relationships",
        "description": (
            "Characteristic 4 (Delight) spans five sub-groups (M04-G affective, M04-H volitional, M04-M obedience, "
            "M04-N relational, M04-P corrupt) covering 247 verses. The inter-relationships between these registers "
            "— particularly between M04-G (affective delight in God) and M04-H (volitional delight as directed "
            "will) — are expected to be analytically significant in Phase 9. The single characteristic carries "
            "both the soul's affective orientation toward what is treasured and the will's directed pleasure; "
            "Phase 9 should examine how these dimensions of the same characteristic relate."
        ),
        "characteristic_seq": 4,
    },
    {
        "source_phase": "characteristic_mapping",
        "observation_type": "INTEGRATION_NOTE",
        "target_phase": "phase_9_findings",
        "title": "M04-L evaluative-cognitive face integrates with M04-O circumstantial under Gladness",
        "description": (
            "M04-L (Evaluative Goodness) and M04-O (Circumstantial Gladness) together form Characteristic 3 — "
            "Gladness. M04-L is the cognitive face (the soul's inner appraisal that something is good — the "
            "assessment that produces and expresses gladness); M04-O is the experiential face (the warm inner "
            "response to beneficial circumstance). Phase 9 findings for M04-L should be integrated with M04-O's "
            "findings under Characteristic 3, recognising these together name the cognitive + experiential aspects "
            "of one inner-being characteristic."
        ),
        "characteristic_seq": 3,
    },
]


def main():
    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()

    # Pre-check: verify current schema version
    current = cur.execute("SELECT version_code, migration_history FROM schema_version ORDER BY id DESC LIMIT 1").fetchone()
    print(f"Current schema_version: {current['version_code']}")
    if current["version_code"] != "3.22.0":
        print(f"WARNING: expected current schema 3.22.0, got {current['version_code']!r}")

    # Verify M04 sub-group ids
    sg_map = {
        r["subgroup_code"]: r["id"]
        for r in cur.execute(
            "SELECT id, subgroup_code FROM cluster_subgroup WHERE cluster_code='M04' AND COALESCE(delete_flagged,0)=0"
        ).fetchall()
    }
    expected_sgs = {f"M04-{c}" for c in "ABCDEFGHIJKLMNOP"}
    missing = expected_sgs - set(sg_map.keys())
    if missing:
        raise RuntimeError(f"Missing M04 sub-groups: {missing}")
    print(f"M04 sub-groups verified: {len(sg_map)} active")

    cur.execute("BEGIN")
    try:
        # ===== 1. Schema migration — create three new tables =====
        cur.execute("""
            CREATE TABLE characteristic (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                cluster_code TEXT NOT NULL,
                char_seq INTEGER NOT NULL,
                short_name TEXT NOT NULL,
                definition TEXT NOT NULL,
                source TEXT,
                version TEXT DEFAULT 'v1',
                notes TEXT,
                delete_flagged INTEGER DEFAULT 0,
                created_at TEXT NOT NULL,
                last_updated_date TEXT NOT NULL,
                UNIQUE(cluster_code, char_seq),
                UNIQUE(cluster_code, short_name)
            )
        """)
        cur.execute("CREATE INDEX idx_characteristic_cluster ON characteristic(cluster_code)")
        print("  CREATE TABLE characteristic + index")

        cur.execute("""
            CREATE TABLE characteristic_subgroup (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                characteristic_id INTEGER NOT NULL,
                cluster_subgroup_id INTEGER NOT NULL,
                qualifier_note TEXT,
                is_partial INTEGER DEFAULT 0,
                partial_register_note TEXT,
                delete_flagged INTEGER DEFAULT 0,
                created_at TEXT NOT NULL,
                last_updated_date TEXT NOT NULL,
                UNIQUE(characteristic_id, cluster_subgroup_id),
                FOREIGN KEY (characteristic_id) REFERENCES characteristic(id),
                FOREIGN KEY (cluster_subgroup_id) REFERENCES cluster_subgroup(id)
            )
        """)
        cur.execute("CREATE INDEX idx_charsg_char ON characteristic_subgroup(characteristic_id)")
        cur.execute("CREATE INDEX idx_charsg_sg ON characteristic_subgroup(cluster_subgroup_id)")
        print("  CREATE TABLE characteristic_subgroup + 2 indexes")

        cur.execute("""
            CREATE TABLE cluster_observation (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                cluster_code TEXT NOT NULL,
                characteristic_id INTEGER,
                cluster_subgroup_id INTEGER,
                source_phase TEXT NOT NULL,
                observation_type TEXT NOT NULL,
                target_phase TEXT,
                title TEXT NOT NULL,
                description TEXT NOT NULL,
                status TEXT DEFAULT 'open',
                resolution_note TEXT,
                raised_date TEXT NOT NULL,
                resolved_date TEXT,
                source_file TEXT,
                delete_flagged INTEGER DEFAULT 0,
                created_at TEXT NOT NULL,
                last_updated_date TEXT NOT NULL,
                FOREIGN KEY (characteristic_id) REFERENCES characteristic(id),
                FOREIGN KEY (cluster_subgroup_id) REFERENCES cluster_subgroup(id)
            )
        """)
        cur.execute("CREATE INDEX idx_obs_cluster ON cluster_observation(cluster_code)")
        cur.execute("CREATE INDEX idx_obs_target_open ON cluster_observation(target_phase) WHERE status = 'open'")
        cur.execute("CREATE INDEX idx_obs_char ON cluster_observation(characteristic_id)")
        print("  CREATE TABLE cluster_observation + 3 indexes")

        # ===== 2. M04 characteristic rows (7) =====
        char_id_by_seq = {}
        for c in M04_CHARACTERISTICS:
            cur.execute("""
                INSERT INTO characteristic (cluster_code, char_seq, short_name, definition, source, version, created_at, last_updated_date)
                VALUES ('M04', ?, ?, ?, ?, 'v1', ?, ?)
            """, (c["seq"], c["short_name"], c["definition"], SOURCE, NOW_UTC, NOW_UTC))
            char_id_by_seq[c["seq"]] = cur.lastrowid
        print(f"  INSERT 7 characteristic rows for M04 (ids {min(char_id_by_seq.values())}-{max(char_id_by_seq.values())})")

        # ===== 3. M04 characteristic_subgroup links (17) =====
        link_count = 0
        for char_seq, sg_code, qualifier, is_partial, partial_note in M04_CHAR_SUBGROUP_LINKS:
            cur.execute("""
                INSERT INTO characteristic_subgroup
                  (characteristic_id, cluster_subgroup_id, qualifier_note, is_partial, partial_register_note, created_at, last_updated_date)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (char_id_by_seq[char_seq], sg_map[sg_code], qualifier, is_partial, partial_note, NOW_UTC, NOW_UTC))
            link_count += 1
        print(f"  INSERT {link_count} characteristic_subgroup links")

        # ===== 4. M04 cluster_observation rows (4) =====
        obs_count = 0
        for o in M04_OBSERVATIONS:
            char_id = char_id_by_seq.get(o.get("characteristic_seq")) if o.get("characteristic_seq") else None
            sg_id = sg_map.get(o.get("subgroup_code")) if o.get("subgroup_code") else None
            cur.execute("""
                INSERT INTO cluster_observation
                  (cluster_code, characteristic_id, cluster_subgroup_id, source_phase, observation_type,
                   target_phase, title, description, status, raised_date, source_file, created_at, last_updated_date)
                VALUES ('M04', ?, ?, ?, ?, ?, ?, ?, 'open', ?, ?, ?, ?)
            """, (char_id, sg_id, o["source_phase"], o["observation_type"], o["target_phase"],
                  o["title"], o["description"], NOW_UTC,
                  "WA-M04-characteristic-map-v4-20260518.md", NOW_UTC, NOW_UTC))
            obs_count += 1
        print(f"  INSERT {obs_count} cluster_observation rows")

        # ===== 5. Bump schema_version (3.22.0 → 3.23.0; record M49) =====
        history = json.loads(current["migration_history"]) if current["migration_history"] else []
        history.append({
            "version": "M49",
            "description": "characteristic + characteristic_subgroup + cluster_observation tables; supports many-sub-groups-per-characteristic and observation-carry-forward across phases (researcher direction 2026-05-18)",
            "applied_at": NOW_UTC,
        })
        cur.execute("""
            INSERT INTO schema_version (version_code, applied_at, migration_history)
            VALUES ('3.23.0', ?, ?)
        """, (NOW_UTC, json.dumps(history)))
        print("  schema_version: 3.22.0 → 3.23.0 (M49)")

        conn.commit()
        print("\n=== All operations committed ===")

    except Exception:
        conn.rollback()
        print("ROLLED BACK due to error")
        raise

    # Verification queries
    print("\n--- Verification ---")
    n_char = cur.execute("SELECT COUNT(*) FROM characteristic WHERE cluster_code='M04'").fetchone()[0]
    n_link = cur.execute("SELECT COUNT(*) FROM characteristic_subgroup cs JOIN characteristic c ON c.id=cs.characteristic_id WHERE c.cluster_code='M04'").fetchone()[0]
    n_obs = cur.execute("SELECT COUNT(*) FROM cluster_observation WHERE cluster_code='M04'").fetchone()[0]
    print(f"M04 characteristics: {n_char} (expected 7)")
    print(f"M04 characteristic_subgroup links: {n_link} (expected 17)")
    print(f"M04 cluster_observations: {n_obs} (expected 4)")

    # Every sub-group accounted for?
    sg_coverage = cur.execute("""
        SELECT cs.subgroup_code,
               (SELECT COUNT(*) FROM characteristic_subgroup chs
                JOIN characteristic c ON c.id = chs.characteristic_id
                WHERE chs.cluster_subgroup_id = cs.id AND c.cluster_code='M04'
                AND COALESCE(chs.delete_flagged,0)=0) AS char_count
        FROM cluster_subgroup cs
        WHERE cs.cluster_code='M04' AND COALESCE(cs.delete_flagged,0)=0
          AND cs.subgroup_code != 'M04-BOUNDARY'
        ORDER BY cs.sort_order
    """).fetchall()
    print("\nSub-group → characteristic coverage:")
    for r in sg_coverage:
        marker = " (partial — 2 characteristics)" if r["char_count"] == 2 else ""
        print(f"  {r['subgroup_code']:10s} characteristic_count={r['char_count']}{marker}")

    # Write apply report
    L = []
    L.append("# M04 characteristic + observation schema load applied")
    L.append("")
    L.append(f"**Date:** {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    L.append(f"**Migration:** M49 (schema 3.22.0 → 3.23.0)")
    L.append(f"**Source:** {SOURCE}")
    L.append("")
    L.append("## Operations applied")
    L.append("")
    L.append("**Schema (M49):**")
    L.append("- CREATE TABLE `characteristic` + 1 index")
    L.append("- CREATE TABLE `characteristic_subgroup` + 2 indexes")
    L.append("- CREATE TABLE `cluster_observation` + 3 indexes (partial unique on target_phase WHERE status='open')")
    L.append("")
    L.append("**M04 data load:**")
    L.append(f"- INSERT {n_char} `characteristic` rows for M04")
    L.append(f"- INSERT {n_link} `characteristic_subgroup` links (16 sub-groups + M04-E partial second link)")
    L.append(f"- INSERT {n_obs} `cluster_observation` rows (Phase 9 carry-forward notes)")
    L.append("")
    L.append("## Characteristic inventory (M04)")
    L.append("")
    rows = cur.execute("SELECT char_seq, short_name FROM characteristic WHERE cluster_code='M04' ORDER BY char_seq").fetchall()
    L.append("| Seq | Short name |")
    L.append("|---:|---|")
    for r in rows:
        L.append(f"| {r['char_seq']} | {r['short_name']} |")
    L.append("")
    L.append("## Sub-group → characteristic mapping")
    L.append("")
    L.append("| Sub-group | Characteristic(s) |")
    L.append("|---|---|")
    for r in sg_coverage:
        char_rows = cur.execute("""
            SELECT c.short_name FROM characteristic_subgroup cs
            JOIN characteristic c ON c.id = cs.characteristic_id
            JOIN cluster_subgroup csg ON csg.id = cs.cluster_subgroup_id
            WHERE csg.subgroup_code = ? AND c.cluster_code='M04'
              AND COALESCE(cs.delete_flagged,0)=0
            ORDER BY c.char_seq
        """, (r["subgroup_code"],)).fetchall()
        names = " + ".join(c["short_name"] for c in char_rows) or "—"
        L.append(f"| {r['subgroup_code']} | {names} |")
    L.append("")
    L.append("## Carry-forward observations (4)")
    L.append("")
    obs_rows = cur.execute("""
        SELECT id, observation_type, title, target_phase, status FROM cluster_observation
        WHERE cluster_code='M04' ORDER BY id
    """).fetchall()
    L.append("| id | type | title | target_phase | status |")
    L.append("|---:|---|---|---|---|")
    for o in obs_rows:
        L.append(f"| {o['id']} | `{o['observation_type']}` | {o['title']} | {o['target_phase']} | {o['status']} |")
    L.append("")
    L.append("## Next steps")
    L.append("")
    L.append("1. Backfill: closed clusters (M01, M02, M03, M05, M06, M15, M20, M26, M39, M46) need their characteristic mapping done analogously to M04. Tracked in memory item `project-characteristic-backfill-backlog`.")
    L.append("2. M04 Phase 9: proceed under the new model — 189 prompts apply per characteristic (across constituent sub-groups). Layered v2 architecture (VCG-level Layer 1 → cluster aggregation Layer 2) sits on top.")
    L.append("3. v2_6 instruction draft: deferred until M04 Phase 9 validates the new model.")
    L.append("")
    L.append("---")
    L.append("")
    L.append("*End of apply report.*")

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text("\n".join(L), encoding="utf-8")
    print(f"\nReport: {OUT}")

    conn.close()


if __name__ == "__main__":
    main()
