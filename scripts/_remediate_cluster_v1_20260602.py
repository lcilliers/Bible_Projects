"""Master cluster-remediation orchestrator (one cluster, packaged).

Runs the playbook loop (wa-cluster-remediation-playbook-v1-20260601.md) as a single
package: AUDIT -> dispatch each failing aspect to its handler -> RE-AUDIT -> REPORT
-> (CLOSE). It calls the individual handler scripts as separate processes, so each
remains independently runnable while the orchestrator operates them as one unit.
Design: wa-cluster-remediation-orchestrator-design-v1-20260602.md.

TWO KINDS OF HANDLER
  - MECH  (deterministic, re-derives from existing data): runs inline on --apply.
  - SPEC  (a JUDGEMENT call — which flag to set aside, which finding to extend, which
           finding a pointer is adopted into): NEVER guessed. The orchestrator applies
           a spec ONLY if it is (a) present in the cluster folder AND (b) carries
           top-level "approved": true (the researcher's review signature). Otherwise it
           STOPS on that aspect — REQUIRES-INPUT (no spec) or REQUIRES-REVIEW (present,
           not yet approved). Use --emit-templates to scaffold the spec with the real
           items enumerated for review.

STOP POINTS (researcher confirmation is structural, not optional)
  Default (no --apply) = DRY: audit + full staged plan + spec/approval status. No writes.
  --apply advances ONE stage, then STOPS and reports:
     --stage mechanical : run MECH handlers (citation extractor; …) live
     --stage specs      : apply present+APPROVED judgement specs only
     --stage close      : if gate-clean, _close_cluster_analysis_v1 --apply
  Re-running picks the next stage from the live audit. Nothing crosses a judgement
  boundary without an approved spec.

Usage
  python scripts/_remediate_cluster_v1_20260602.py --cluster M38                  # dry plan
  python scripts/_remediate_cluster_v1_20260602.py --cluster M38 --emit-templates # scaffold specs
  python scripts/_remediate_cluster_v1_20260602.py --cluster M38 --apply --stage mechanical
  python scripts/_remediate_cluster_v1_20260602.py --cluster M38 --apply --stage specs
  python scripts/_remediate_cluster_v1_20260602.py --cluster M38 --apply --stage close
"""
import argparse, glob, importlib.util, json, os, subprocess, sys

if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
AUD_PATH = os.path.join(REPO, "scripts", "audit_cluster_v1_20260601.py")
_spec = importlib.util.spec_from_file_location("auditor", AUD_PATH)
aud = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(aud)

PY = sys.executable
SCRIPTS = os.path.join(REPO, "scripts")


def cdir(code):
    return os.path.join(REPO, "Sessions", "Session_Clusters", code)


def find_spec(code, kind_glob):
    files = sorted(glob.glob(os.path.join(cdir(code), f"wa-cluster-{code}-{kind_glob}.json")))
    return files[-1] if files else None


def spec_state(path):
    """-> ('absent'|'unapproved'|'approved', data|None)."""
    if not path or not os.path.exists(path):
        return "absent", None
    try:
        d = json.load(open(path, encoding="utf-8"))
    except Exception as e:
        return f"unreadable:{e}", None
    return ("approved" if d.get("approved") is True else "unapproved"), d


# --- Handler registry -------------------------------------------------------
# Each step: which audit aspects it clears, its kind, the spec-file glob (SPEC only),
# the applier command builder, and whether the applier is built yet.
def _cmd(*parts):
    return [PY, os.path.join(SCRIPTS, parts[0]), *parts[1:]]

MECH = "MECH"
SPEC = "SPEC"
NOOP = "NOOP"

# spec_glob, applier(file)->cmd, built?
DISPOSITIONS = ("pointer-dispositions-v*", lambda f: _cmd("_apply_pointer_dispositions_v1_20260601.py", "--file", f, "--apply"), True)
EXTENSION    = ("b7-citation-extension-v*", lambda f: _cmd("_apply_finding_citation_extension_v1_20260602.py", "--file", f, "--apply"), True)
ADOPTION     = ("pointer-adoption-v*",      lambda f: _cmd("_apply_pointer_adoption_v1_20260602.py", "--file", f, "--apply"), False)


def resolve_plan(R):
    """Map the live audit's failing aspects to ordered remedial steps."""
    by = {r["id"]: r for r in R}
    def fail(aid):  # gate/struct FAIL, info REVIEW, or incr>0
        r = by.get(aid)
        return r and (r["status"] == "FAIL" or (r["status"] == "REVIEW") or (r["sev"] == "INCR" and isinstance(r["count"], int) and r["count"] > 0))

    steps = []
    # --- Mechanical: citation extractor clears B6 + the bulk of B7 ---
    if fail("B6") or fail("B7"):
        steps.append({"key": "CITATIONS", "kind": MECH, "aspects": ["B6", "B7"],
                      "desc": "citation extractor — re-derive finding_citation from finding text",
                      "cmd": _cmd("_extract_finding_citations_v1_20260525.py", "--cluster", CODE, "--live"),
                      "built": True})
    # --- Judgement: A6/A7/A2 dispositions ---
    if fail("A6") or fail("A7") or fail("A2"):
        steps.append({"key": "DISPOSITIONS", "kind": SPEC, "aspects": ["A6", "A7", "A2"],
                      "desc": "pointer/finding dispositions — set_aside / resolve / fold (+ A2 review no-op)",
                      "spec_glob": DISPOSITIONS[0], "applier": DISPOSITIONS[1], "built": DISPOSITIONS[2]})
    # --- Judgement: B7 residual (genuinely-uncited anchors AFTER the extractor) ---
    if fail("B7"):
        steps.append({"key": "B7_EXTENSION", "kind": SPEC, "aspects": ["B7"], "residual_after": "CITATIONS",
                      "desc": "B7 residual — extend host finding text to cite genuinely-uncited anchors",
                      "spec_glob": EXTENSION[0], "applier": EXTENSION[1], "built": EXTENSION[2]})
    # --- Judgement: D2 pointer adoption ---
    if fail("D2"):
        steps.append({"key": "ADOPTION", "kind": SPEC, "aspects": ["D2"],
                      "desc": "adopt unallocated pointers into a finding (+ xref + close), else set aside",
                      "spec_glob": ADOPTION[0], "applier": ADOPTION[1], "built": ADOPTION[2]})
    # --- Aspects with no handler built yet: surface, do not guess ---
    TODO = {"A4": "boundary disposition", "A5": "boundary disposition", "A8": "actionable-obs confirm",
            "B1a": "Phase-A meaning backfill", "B1b": "Phase-A keyword backfill", "B2": "grouping",
            "B3": "char-subgroup link", "B5": "VCG anchor designation", "C1": "old-VCG dissolution (mech)",
            "C2": "term-subgroup link", "D1": "new-term placement", "A9": "orphan-finding review"}
    for aid, label in TODO.items():
        if fail(aid):
            steps.append({"key": f"TODO_{aid}", "kind": "TODO", "aspects": [aid],
                          "desc": f"{label} — handler not built yet", "built": False})
    return steps


def audit(code):
    c = aud.conn()
    verdict, R = aud.audit_cluster(c, code)
    c.close()
    return verdict, R


def gate_fails(R):
    return [r for r in R if r["sev"] == "GATE" and r["status"] == "FAIL"]


def print_audit(tag, verdict, R):
    gf = gate_fails(R)
    print(f"\n[{tag}] verdict={verdict} | GATE fails={len(gf)}")
    for r in R:
        if r["status"] in ("FAIL", "REVIEW") or (r["sev"] == "INCR" and isinstance(r["count"], int) and r["count"] > 0):
            print(f"   {r['id']:<4} {r['sev']:<6} {r['status']:<7} {str(r['count']):>5}  {r['name']}")


def step_status_line(code, st):
    if st["kind"] == MECH:
        return f"MECH  · runs inline on --apply --stage mechanical · {'ready' if st['built'] else 'NOT BUILT'}"
    if st["kind"] == "TODO":
        return "TODO  · STOP — handler not built (surface, do not guess)"
    # SPEC
    path = find_spec(code, st["spec_glob"])
    state, _ = spec_state(path)
    if not st["built"]:
        return f"SPEC  · applier NOT BUILT · spec={os.path.basename(path) if path else '(none)'} [{state}]"
    if state == "absent":
        return "SPEC  · STOP — REQUIRES-INPUT (no spec; run --emit-templates, then review)"
    if state == "approved":
        return f"SPEC  · READY — approved spec present ({os.path.basename(path)})"
    return f"SPEC  · STOP — REQUIRES-REVIEW (spec present, not approved): {os.path.basename(path)}"


def _short(p):
    try:
        return os.path.relpath(p, REPO) if os.path.isabs(p) else p
    except ValueError:
        return os.path.basename(p)  # cross-drive (e.g. python on C:, repo on G:)


def run(cmd):
    print(f"   $ {' '.join(_short(p) for p in cmd)}")
    r = subprocess.run(cmd, cwd=REPO)
    if r.returncode != 0:
        raise SystemExit(f"ABORT: handler exited {r.returncode}")


# --- template emission ------------------------------------------------------
# Each emitted item carries its FULL evaluable text (flags: description; findings:
# finding) plus context columns, so the item is self-contained for review. The short
# label (e.g. DIM-180-SD001) is only an ID — the content lives in description/finding.
def enumerate_dispositions(code):
    c = aud.conn(); cur = c.cursor()
    regs = [r["owning_registry_fk"] for r in cur.execute("SELECT DISTINCT owning_registry_fk FROM mti_terms WHERE cluster_code=? AND COALESCE(delete_flagged,0)=0 AND owning_registry_fk IS NOT NULL", (code,))]
    items = []
    if regs:
        fph = ",".join("?" * len(aud.GATING_FLAGS)); rph = ",".join("?" * len(regs))
        for r in cur.execute(f"SELECT id, flag_code, COALESCE(flag_label,'') label, registry_id, cluster_link, cluster_link_basis, session_target, priority, COALESCE(description,'') descr FROM wa_session_research_flags WHERE COALESCE(resolved,0)=0 AND flag_code IN ({fph}) AND registry_id IN ({rph}) ORDER BY flag_code, id", (*aud.GATING_FLAGS, *regs)):
            items.append({"table": "wa_session_research_flags", "id": r["id"],
                          "action": "", "evaluation": "", "reason": "",
                          "_aspect": "A6", "_classifier": f"{r['flag_code']} {r['label']}",
                          "_registry_id": r["registry_id"], "_cluster_link": r["cluster_link"],
                          "_session_target": r["session_target"], "_priority": r["priority"],
                          "_text": r["descr"]})
    for r in cur.execute("SELECT DISTINCT sbf.id, COALESCE(sbf.finding_type,'') ft, COALESCE(sbf.finding,'') finding, sbf.registry_id, sbf.cluster_link, COALESCE(sbf.anchor_verses,'') av, COALESCE(sbf.session_b_instruction,'') instr, COALESCE(sbf.structural_relationship,'') sr FROM wa_session_b_findings sbf JOIN mti_terms mt ON mt.owning_registry_fk=sbf.registry_id AND COALESCE(mt.delete_flagged,0)=0 JOIN mti_term_subgroup mts ON mts.mti_term_id=mt.id AND COALESCE(mts.delete_flagged,0)=0 JOIN cluster_subgroup cs ON cs.id=mts.cluster_subgroup_id WHERE cs.cluster_code=? AND sbf.status IN ('pending','open') ORDER BY sbf.id", (code,)):
        items.append({"table": "wa_session_b_findings", "id": r["id"],
                      "action": "", "evaluation": "", "reason": "",
                      "_aspect": "A7", "_classifier": r["ft"], "_registry_id": r["registry_id"],
                      "_cluster_link": r["cluster_link"], "_anchor_verses": r["av"],
                      "_instruction": r["instr"], "_structural_relationship": r["sr"],
                      "_text": r["finding"]})
    c.close()
    return items


def enumerate_adoptions(code):
    c = aud.conn(); cur = c.cursor()
    like = f"%,{code},%"
    items = []
    for r in cur.execute("SELECT id, flag_code, COALESCE(flag_label,'') label, registry_id, cluster_link, COALESCE(description,'') descr FROM wa_session_research_flags WHERE flag_code IN ('SD_POINTER','SB_FINDING','SB_INNER_BEING','SD_CLUSTER') AND COALESCE(resolved,0)=0 AND cluster_link IS NOT NULL AND (','||cluster_link||',') LIKE ? ORDER BY id", (like,)):
        items.append({"table": "wa_session_research_flags", "id": r["id"],
                      "action": "", "target_finding_id": None, "new_finding_text": "", "reason": "",
                      "_classifier": f"{r['flag_code']} {r['label']}", "_registry_id": r["registry_id"],
                      "_cluster_link": r["cluster_link"], "_text": r["descr"]})
    c.close()
    return items


def _has_filled(path, key):
    """True if an existing spec already has any item with a non-empty action (don't clobber review work)."""
    if not os.path.exists(path):
        return False
    try:
        d = json.load(open(path, encoding="utf-8"))
    except Exception:
        return True  # unreadable -> be safe, don't overwrite
    return any(str(it.get("action", "")).strip() for it in d.get(key, []))


def _render_review_md(code, disp, adopt):
    L = [f"# M{code[1:] if code.startswith('M') else code} remediation — review sheet (judgement items)",
         "" if False else "",
         f"**Cluster:** {code} · **2026-06-02** · read-only rendering of the emitted spec(s) for review.",
         "Full evaluable text is shown per item. Record decisions in the matching JSON "
         "(`action`/`evaluation`/`reason`), then set top-level `\"approved\": true`.", ""]
    def block(title, items, kind):
        L.append(f"## {title} ({len(items)})"); L.append("")
        for it in items:
            L.append(f"### id {it['id']} · {it.get('_classifier','')} · reg {it.get('_registry_id','')} · link {it.get('_cluster_link','')}")
            for ctx in ("_session_target", "_priority", "_anchor_verses", "_instruction", "_structural_relationship"):
                v = it.get(ctx)
                if v:
                    L.append(f"- _{ctx.strip('_')}_: {v}")
            L.append("")
            L.append(f"> {it.get('_text','').strip()}")
            L.append("")
            if kind == "disp":
                L.append("**action:** _____  ·  **reason:** _____")
            else:
                L.append("**action:** adopt|set_aside  ·  **target_finding_id:** _____  ·  **reason:** _____")
            L.append("")
    if disp:
        a6 = [x for x in disp if x.get("_aspect") == "A6"]; a7 = [x for x in disp if x.get("_aspect") == "A7"]
        if a6: block("A6 — gating flags (SD_POINTER): resolve / set_aside / convert-to-observation", a6, "disp")
        if a7: block("A7 — stray Session-B findings: set_aside / fold / resolve", a7, "disp")
    if adopt:
        block("D2 — unallocated pointers: adopt into finding (+xref+close) or set_aside", adopt, "adopt")
    return "\n".join(L) + "\n"


def emit_templates(code):
    out = []
    disp = enumerate_dispositions(code)
    if disp:
        p = os.path.join(cdir(code), f"wa-cluster-{code}-pointer-dispositions-v1-20260602.json")
        if _has_filled(p, "dispositions"):
            print(f"   skip (has filled actions — not clobbering): {os.path.basename(p)}")
        else:
            json.dump({"cluster": code, "date": "2026-06-02", "approved": False,
                       "method": "REVIEW REQUIRED: evaluate each item on its full _text (v3_0 §10.1 / v2_9 §18); set action (set_aside|resolve|fold|review) + evaluation + reason. Underscore-prefixed fields are read-only evidence. Set top-level \"approved\": true after researcher review to let the orchestrator apply.",
                       "dispositions": disp}, open(p, "w", encoding="utf-8"), indent=2, ensure_ascii=False)
            print(f"   wrote {os.path.basename(p)} ({len(disp)} items, full text) — REQUIRES REVIEW")
        out.append(p)
    adopt = enumerate_adoptions(code)
    if adopt:
        p = os.path.join(cdir(code), f"wa-cluster-{code}-pointer-adoption-v1-20260602.json")
        if _has_filled(p, "adoptions"):
            print(f"   skip (has filled actions — not clobbering): {os.path.basename(p)}")
        else:
            json.dump({"cluster": code, "date": "2026-06-02", "approved": False,
                       "method": "REVIEW REQUIRED: for each pointer evaluate _text; set action (adopt|set_aside). adopt -> target_finding_id (existing) or new_finding_text; record reason. Underscore fields are read-only evidence. Applier _apply_pointer_adoption_v1 is TO BUILD.",
                       "adoptions": adopt}, open(p, "w", encoding="utf-8"), indent=2, ensure_ascii=False)
            print(f"   wrote {os.path.basename(p)} ({len(adopt)} items, full text) — REQUIRES REVIEW + applier build")
        out.append(p)
    if disp or adopt:
        mp = os.path.join(cdir(code), f"wa-cluster-{code}-remediation-review-v1-20260602.md")
        open(mp, "w", encoding="utf-8").write(_render_review_md(code, disp, adopt))
        print(f"   wrote {os.path.basename(mp)} — readable review sheet (full text per item)")
        out.append(mp)
    if not out:
        print("   no judgement aspects require templates.")
    return out


def main():
    global CODE
    ap = argparse.ArgumentParser()
    ap.add_argument("--cluster", required=True)
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--stage", choices=["mechanical", "specs", "close"], default=None)
    ap.add_argument("--emit-templates", action="store_true")
    a = ap.parse_args()
    CODE = a.cluster

    verdict, R = audit(CODE)
    print(f"===== remediate {CODE} =====")
    print_audit("BASELINE", verdict, R)
    steps = resolve_plan(R)

    print("\n----- remedial plan (staged) -----")
    if not steps:
        print("  no failing aspects — cluster is clean.")
    for st in steps:
        print(f"  [{st['key']}] aspects={','.join(st['aspects'])}: {st['desc']}")
        print(f"       {step_status_line(CODE, st)}")

    if a.emit_templates:
        print("\n----- emitting review templates -----")
        emit_templates(CODE)
        print("\nSTOP: review + fill the emitted spec(s); set \"approved\": true; then re-run with --apply --stage specs.")
        return

    if not a.apply:
        print("\nDRY-RUN: no writes. Next: --emit-templates (scaffold judgement specs) or "
              "--apply --stage mechanical (run the extractor).")
        return

    # ---- staged apply (one stage, then STOP) ----
    if a.stage == "mechanical":
        print("\n----- STAGE mechanical -----")
        ran = False
        for st in steps:
            if st["kind"] == MECH and st["built"]:
                run(st["cmd"]); ran = True
        if not ran:
            print("  (no mechanical handlers to run)")
        v2, R2 = audit(CODE); print_audit("RE-AUDIT", v2, R2)
        print("\nSTOP: review mechanical result; then --emit-templates for remaining judgement aspects.")
    elif a.stage == "specs":
        print("\n----- STAGE specs (approved only) -----")
        applied = False
        for st in steps:
            if st["kind"] != SPEC:
                continue
            path = find_spec(CODE, st["spec_glob"]); state, _ = spec_state(path)
            if not st["built"]:
                print(f"  [{st['key']}] SKIP — applier not built ({st['spec_glob']})"); continue
            if state == "approved":
                print(f"  [{st['key']}] applying approved spec {os.path.basename(path)}")
                run(st["applier"](path)); applied = True
            else:
                print(f"  [{st['key']}] STOP — spec {state} (need present + approved)")
        if not applied:
            print("  (no approved specs applied)")
        else:
            run(_cmd("_extract_finding_citations_v1_20260525.py", "--cluster", CODE, "--live"))  # re-derive citations post-extension
        v2, R2 = audit(CODE); print_audit("RE-AUDIT", v2, R2)
        print("\nSTOP: review re-audit; if gate-clean, --apply --stage close.")
    elif a.stage == "close":
        gf = gate_fails(R)
        if gf:
            print("\nREFUSE close: GATE fails remain:", ", ".join(r["id"] for r in gf)); return
        run(_cmd("_close_cluster_analysis_v1_20260601.py", "--cluster", CODE, "--apply"))
    else:
        print("\n--apply requires --stage {mechanical|specs|close}.")


if __name__ == "__main__":
    main()
