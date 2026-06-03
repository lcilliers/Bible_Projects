"""Applier for COMMENT_EVALUATION outcomes (per cluster).

Reads a researcher-approved spec JSON and performs three write kinds:
  - new_findings : INSERT cluster_finding rows (comment adopted into new finding(s))
  - new_flags    : INSERT wa_session_research_flags rows (reciprocal pointer queued for
                   another cluster's later analysis)
  - fold_findings: UPDATE wa_session_b_findings (source comment folded/closed)

Never edits existing findings (new concepts are separate findings). Guarded, dry-run
default; requires top-level "approved": true to write. After --apply, re-run the citation
extractor (--cluster CODE --live) and the auditor.

  python scripts/_apply_comment_findings_v1_20260602.py --file PATH [--apply]
"""
import argparse, json, sqlite3
from datetime import datetime, timezone

DB = "database/bible_research.db"
NOW = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--file", required=True)
    ap.add_argument("--apply", action="store_true")
    a = ap.parse_args()
    d = json.load(open(a.file, encoding="utf-8"))
    nf = d.get("new_findings", [])
    flg = d.get("new_flags", [])
    fold = list(d.get("fold_findings", []))
    # fold_bulk: one status/cluster_link/note applied to a list of ids (e.g. a consolidated route)
    fb = d.get("fold_bulk")
    if fb:
        for i in fb["ids"]:
            fold.append({"id": i, "status": fb["status"], "cluster_link": fb.get("cluster_link"),
                         "resolution_note": fb.get("resolution_note")})
    print(f"{'APPLY' if a.apply else 'DRY-RUN'}: cluster={d.get('cluster')} "
          f"new_findings={len(nf)} new_flags={len(flg)} fold={len(fold)}"
          + (f" (incl. fold_bulk {len(fb['ids'])})" if fb else ""))
    for f in nf:
        print(f"  + cluster_finding obs {f['obs_id']} ({f.get('tier','')}) char {f['characteristic_id']}: {f['finding_text'][:70]}…")
    for fl in flg:
        print(f"  + flag {fl['flag_code']} link={fl['cluster_link']} reg {fl['registry_id']}: {fl['description'][:70]}…")
    for fo in fold:
        print(f"  ~ fold wa_session_b_findings id {fo['id']} -> {fo['status']} (link {fo.get('cluster_link')})")
    for rh in d.get("rehome_flags", []):
        print(f"  > rehome flag {rh['id']} -> SD_CLUSTER link {rh['cluster_link']}")
    for rf in d.get("resolve_flags", []):
        print(f"  x resolve+close flag {rf['id']}: {rf['resolved_note'][:60]}…")
    for co in d.get("confirm_observations", []):
        print(f"  = confirm observation {co['id']}")
    for et in d.get("exclude_terms", []):
        print(f"  - exclude+soft-delete term {et['id']}: {et['exclusion_reason'][:60]}…")

    if not a.apply:
        return
    if d.get("approved") is not True:
        raise SystemExit("ABORT: spec not approved (set top-level \"approved\": true)")

    c = sqlite3.connect(DB, timeout=30); cur = c.cursor()
    cur.execute("BEGIN")
    try:
        new_finding_ids = []
        for f in nf:
            cur.execute(
                "INSERT INTO cluster_finding (obs_id, cluster_code, characteristic_id, cluster_subgroup_id, vcg_scope, finding_status, finding_text, source_file, version, notes, delete_flagged, created_at, last_updated_date) "
                "VALUES (?,?,?,?,?,?,?,?,?,?,0,?,?)",
                (f["obs_id"], f["cluster_code"], f["characteristic_id"], f.get("cluster_subgroup_id"),
                 f.get("vcg_scope"), f.get("finding_status", "finding"), f["finding_text"],
                 f.get("source_file"), f.get("version", "v1"), f.get("notes"), NOW, NOW))
            new_finding_ids.append(cur.lastrowid)
        new_obs_ids = []
        for ob in d.get("new_observations", []):
            cur.execute(
                "INSERT INTO cluster_observation (cluster_code, characteristic_id, cluster_subgroup_id, source_phase, observation_type, target_phase, title, description, status, source_file, raised_date, created_at, last_updated_date) "
                "VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)",
                (ob["cluster_code"], ob.get("characteristic_id"), ob.get("cluster_subgroup_id"),
                 ob.get("source_phase", "comment-evaluation"), ob.get("observation_type", "cross-cluster-synthesis"),
                 ob.get("target_phase"), ob.get("title"), ob["description"], ob.get("status", "confirmed"),
                 ob.get("source_file"), NOW, NOW, NOW))
            new_obs_ids.append(cur.lastrowid)
        new_flag_ids = []
        for fl in flg:
            cur.execute(
                "INSERT INTO wa_session_research_flags (registry_id, flag_code, flag_label, priority, session_target, description, session_raised, raised_date, resolved, cluster_link, cluster_link_basis) "
                "VALUES (?,?,?,?,?,?,?,?,0,?,?)",
                (fl["registry_id"], fl["flag_code"], fl.get("flag_label"), fl.get("priority"),
                 fl.get("session_target"), fl.get("description"),
                 fl.get("session_raised", "comment-evaluation 2026-06-02"), NOW, fl.get("cluster_link"),
                 fl.get("cluster_link_basis")))
            new_flag_ids.append(cur.lastrowid)
        folded = 0
        for fo in fold:
            cur.execute("UPDATE wa_session_b_findings SET status=?, cluster_link=?, resolution_note=? WHERE id=?",
                        (fo["status"], fo.get("cluster_link"), fo.get("resolution_note"), fo["id"]))
            folded += cur.rowcount
        if folded != len(fold):
            c.rollback(); raise SystemExit(f"ABORT: folded {folded}!=expected {len(fold)}")
        # rehome_flags: re-home a gating SD_POINTER to another cluster (SD_POINTER -> SD_CLUSTER,
        # set cluster_link). Clears the source cluster's A6 (non-gating) + surfaces as target D2.
        rehomed = 0
        for rh in d.get("rehome_flags", []):
            cur.execute("UPDATE wa_session_research_flags SET flag_code='SD_CLUSTER', cluster_link=?, cluster_link_basis=? WHERE id=?",
                        (rh["cluster_link"], rh.get("basis", "re-homed from A6 (comment-evaluation)"), rh["id"]))
            rehomed += cur.rowcount
        if rehomed != len(d.get("rehome_flags", [])):
            c.rollback(); raise SystemExit("ABORT: rehome rowcount mismatch")
        # resolve_flags: pure process/database/registry-design pointers — mark resolved + close.
        resolved = 0
        for rf in d.get("resolve_flags", []):
            cur.execute("UPDATE wa_session_research_flags SET resolved=1, resolved_date=?, resolved_note=? WHERE id=?",
                        (NOW, rf["resolved_note"], rf["id"]))
            resolved += cur.rowcount
        if resolved != len(d.get("resolve_flags", [])):
            c.rollback(); raise SystemExit("ABORT: resolve rowcount mismatch")
        # exclude_terms: set-aside + soft-delete terms with no verses / not characteristic-relevant
        # (precedent: G9704/G9706 'STEP returned no verses; excluded from MTI').
        excluded_t = 0
        for et in d.get("exclude_terms", []):
            cur.execute("UPDATE mti_terms SET status='excluded', delete_flagged=1, exclusion_reason=? WHERE id=?",
                        (et["exclusion_reason"], et["id"]))
            excluded_t += cur.rowcount
        if excluded_t != len(d.get("exclude_terms", [])):
            c.rollback(); raise SystemExit("ABORT: exclude_terms rowcount mismatch")
        # confirm_observations: close open cluster_observation rows (status->confirmed + note).
        confirmed = 0
        for co in d.get("confirm_observations", []):
            cur.execute("UPDATE cluster_observation SET status='confirmed', resolution_note=?, resolved_date=?, last_updated_date=? WHERE id=?",
                        (co.get("resolution_note"), NOW, NOW, co["id"]))
            confirmed += cur.rowcount
        if confirmed != len(d.get("confirm_observations", [])):
            c.rollback(); raise SystemExit("ABORT: confirm_observations rowcount mismatch")
        # Reset-if-complete: any cluster a new pointer is assigned to that is already
        # 'Analysis Complete' must be re-opened so the pointer is re-analysed (researcher
        # directive 2026-06-02). Applies to flag cluster_link targets.
        reset = []
        targets = set()
        for fl in flg:
            for t in str(fl.get("cluster_link", "")).split(","):
                t = t.strip()
                if t and t != "T2":
                    targets.add(t)
        for t in sorted(targets):
            row = cur.execute("SELECT status FROM cluster WHERE cluster_code=?", (t,)).fetchone()
            if row and row[0] == "Analysis Complete":
                cur.execute("UPDATE cluster SET status='Ready for re-analysis', last_updated_date=? WHERE cluster_code=?", (NOW, t))
                reset.append(t)
        c.commit()
    except Exception:
        c.rollback(); raise
    print(f"APPLIED: cluster_finding ids {new_finding_ids}; observation ids {new_obs_ids}; "
          f"flag ids {new_flag_ids}; folded {folded}; rehomed {rehomed}; resolved {resolved}; confirmed_obs {confirmed}; excluded_terms {excluded_t}.")
    if reset:
        print(f"RESET (was Analysis Complete -> Ready for re-analysis, re-opened for new pointer): {reset}")
    print("Next: re-run citation extractor (--cluster {} --live) then re-audit.".format(d.get("cluster")))
    c.close()


if __name__ == "__main__":
    main()
