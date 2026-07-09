"""
Anchor the M10 deferred-exploration register (SDX-01..08) as Session D pointers
in wa_session_research_flags (researcher go-ahead 2026-06-23). Option (a):
registry_id anchored to the M10 'sin' registry (no 147); cluster_link carries the
cross-cluster reach. Read-only by default; --live applies after a snapshot.
"""
import sqlite3, os, shutil, sys

DB = os.path.join('database', 'bible_research.db')
REG_SIN = 147  # word_registry.no for 'sin' (M10 anchor)

ITEMS = [
 ('M10-SDX-01','HIGH','M10,M28,M29,M47',
  "Does sin intrinsically express itself; can sin exist unexpressed? Expression rooted in the heart (Mat 15:19; #27 generative conceived->born) but interior sin is real before any deed (Psa 58:2; Pro 24:9); sin always known to God (Jer 17:1, #13); suppression itself a posture (#4). TEST: is expression/manifestness a structural property of ALL sin (outward/God-ward/posture)? Needs M28/M29 desire, M47 heart, Jam 1:14-15."),
 ('M10-SDX-02','HIGH','M10,M11,M38,M12',
  "Where does ATONEMENT live? Central biblical concept not encapsulated in any unit - scattered across chat.tat 'sin-offering' + kip.pu.rim (#14) and M10c purification (#29-31). Own unit, cross-cutting layer, or primarily another cluster's? Needs M11 (Repentance/Forgiveness), M38 (Salvation), M12 (Purity)."),
 ('M10-SDX-03','HIGH','ALL',
  "Does the OBJECT-KIND typology generalise programme-wide? M10 holds several kinds beyond 'characteristic' - status/condition, record/liability, identity, expression, mechanism, remedy, external-agency. Do these recur across all clusters (the programme's real ontology) or is M10 special? Needs the section-10 definitional gate + a test against every cluster."),
 ('M10-SDX-04','HIGH','ALL',
  "DUAL-VIEW / multi-dimensional model: a concept appears in M10 as an operation-view AND may have a characteristic-view cluster of its own (M10b<->M27; defilement<->M12). Is the dual-view applied CONSISTENTLY across the whole cluster set? Needs a programme-wide consistency audit."),
 ('M10-SDX-05','MEDIUM','M10,M26,M12,M13,M31',
  "POLE-PAIR / antithesis structure: sin<->righteousness (M26), defilement<->purity (M12), faithlessness<->faith (M13/M31), wicked<->righteous. Is the inner being described by paired opposites as a general structure? Needs the partner clusters analysed."),
 ('M10-SDX-06','MEDIUM','M10,M13,M31,M26,M06,M42,M14,M08,M03,M07,M23,M35',
  "HOME-CALL relocations: concepts whose home may be another cluster - #20 Faithlessness->M13/M31, #22 Injustice->M26, #9/#28 Sinful speech->M06/M42, #10 mechanisms->M14/M08/M31, #21 Perversion->M03/M07/M23/M35, and the recognised inner-being characteristics #20/#21/#27 (kept in M10 for now, possibly relocated). Confirm once target clusters analysed."),
 ('M10-SDX-07','MEDIUM','M10,M01',
  "EXTERNAL SPIRITUAL AGENCY as an object-kind: the 'evil one' (Satan, #24) and the unclean spirit (#32) are external agents, not the person's own interior - a distinct kind imposed from without. How does it relate across the inner-being clusters (fear M01; the spiritual-being interface)? Cross-cluster."),
 ('M10-SDX-08','MEDIUM','M10',
  "EXTERNAL-POLE elements: a.von 'punishment' sense (H5771I = retribution/judgement) and #8 political-fact revolt are external-pole, not inner-being states. In scope for an inner-being study, or cross-referenced out? Needs the programme-wide external-pole scope rule."),
]

def main():
    live = '--live' in sys.argv
    conn = sqlite3.connect(DB); conn.row_factory = sqlite3.Row

    # guard: skip any label already present
    existing = {r['flag_label'] for r in conn.execute(
        "SELECT flag_label FROM wa_session_research_flags WHERE flag_label LIKE 'M10-SDX-%'")}
    todo = [it for it in ITEMS if it[0] not in existing]

    print(f"anchor registry_id={REG_SIN} (sin) · flag_code=SD_POINTER · session_target=D")
    print(f"{len(todo)} to insert ({len(ITEMS)-len(todo)} already present):")
    for label, pri, links, desc in todo:
        print(f"  {label} [{pri}] clusters={links}\n      {desc[:110]}...")

    if not live:
        print("\n(dry-run — pass --live to apply)"); return

    snap = os.path.join('backups', 'bible_research_pre-sdx-flags_20260623.db')
    os.makedirs('backups', exist_ok=True); shutil.copy2(DB, snap)
    print(f"\nSnapshot: {snap}")

    cur = conn.cursor()
    for label, pri, links, desc in todo:
        cur.execute(
            "INSERT INTO wa_session_research_flags "
            "(registry_id, file_id, flag_code, flag_label, strongs_reference, cross_registry_id, "
            " priority, session_target, description, session_raised, raised_date, resolved, "
            " cluster_link, cluster_link_basis) "
            "VALUES (?, NULL, 'SD_POINTER', ?, NULL, NULL, ?, 'D', ?, "
            " 'M10-observations-2026-06-23', '2026-06-23', 0, ?, 'm10-observations-theme')",
            (REG_SIN, label, pri, desc, links))
    conn.commit()
    print(f"Inserted {len(todo)} SD_POINTER rows.")

    print("\nVerification:")
    for r in conn.execute("SELECT flag_label, priority, cluster_link FROM wa_session_research_flags "
                          "WHERE flag_label LIKE 'M10-SDX-%' ORDER BY flag_label"):
        print(f"  {r['flag_label']} [{r['priority']}] {r['cluster_link']}")

if __name__ == '__main__':
    main()
