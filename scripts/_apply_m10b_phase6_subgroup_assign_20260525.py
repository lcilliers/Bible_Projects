"""M10b Phase 6 — sub-group structural apply + verse routing.

Per v2_8 §9. Per directive wa-cluster-M10b-dir-001-phase6-subgroup-assign-v1-20260525.md.

Operations:
- Op A: INSERT 6 cluster_subgroup rows (M10b-A..F).
- Op B: INSERT mti_term_subgroup rows (primary + secondary) for every (term, sub-group)
        pair. Multi-faceted: to.e.vah → C+D, bdelugma → C+D, ro.a → A+E.
- Op C: UPDATE verse_context.cluster_subgroup_id for every is_relevant vc row per
        resolved mapping (515 rows).
- Op D: cluster.status 'Data - In Progress' → 'Analysis - In Progress' (Phase 4 skipped).

Source: Sessions/Session_Clusters/M10b/wa-cluster-M10b-subgroup-mapping-v1-20260525.json

to.e.vah split (per-verse content review): D = passage groups from the AI mapping
(explicit references for Leviticus, Deuteronomy, historical reform narratives, Ezra,
Jeremiah, Ezekiel idolatry corpus). Every to.e.vah reference not in the D-list →
C (moral-character abomination, the broader default).

Resolved mapping written for audit:
  Sessions/Session_Clusters/M10b/wa-cluster-M10b-subgroup-mapping-resolved-v1-20260525.json
"""
from __future__ import annotations
import argparse, io, json, re, shutil, sqlite3, sys
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path

if sys.platform == "win32":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

REPO = Path(__file__).resolve().parent.parent
DB = REPO / "database" / "bible_research.db"
NOW = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
DIRECTIVE_ID = "wa-cluster-M10b-dir-001-phase6-subgroup-assign-v1-20260525"
MAPPING_PATH = REPO / "Sessions" / "Session_Clusters" / "M10b" / "wa-cluster-M10b-subgroup-mapping-v1-20260525.json"
RESOLVED_PATH = REPO / "Sessions" / "Session_Clusters" / "M10b" / "wa-cluster-M10b-subgroup-mapping-resolved-v1-20260525.json"

CLUSTER = "M10b"

# Sub-group definitions: (code, label, core_description, sort_order)
SUBGROUPS = [
    ("M10b-A", "The wicked person — settled inner orientation of wickedness",
     "CHAR-1 (Wickedness as settled person-identity). The wicked person as an inner-being type — "
     "the individual whose core moral character is defined by wickedness. Will corrupted, God actively "
     "excluded from the mind (practical atheism), inner orientation persistently bent toward harm and "
     "injustice. The conscience is suppressed or displaced by an inner voice of transgression. The will "
     "refuses God, chooses evil companions, and schemes against the righteous. Wickedness is not merely "
     "a series of acts but a stable identity and inner condition; divine judgment falls specifically on "
     "this person-type. Primary terms: ra.sha (179V), re.sha (9V), mir.sha.at (1V). Secondary: ro.a (1V "
     "for 1Sa 17:28). Phase 7 polysemy note: forensic-verdict sub-corpus within ra.sha (~5V) carries M10 "
     "cross-register flag and will receive a distinct VCG within this sub-group.",
     1),
    ("M10b-B", "Evil as the constitutional nature of the inner person",
     "CHAR-2 (Evil as constitutional inner nature). Evil as the structural condition of the inner person "
     "— not primarily the choice of the will moment by moment, but the constitutive nature from which "
     "corrupt choices flow. The heart is a treasury of evil that the person draws on; the inner nature "
     "is bent toward corruption as its default output. NT-distinctive analysis: humans constitutionally "
     "incline toward evil, evil thoughts originate in the heart, the heart's evil nature is the root of "
     "all outward moral failure. Primary terms: ponēros (63V), kakia (11V), adikia (8V), ponēria (7V), "
     "faulos (1V). Phase 7 polysemy note: cosmic-evil-agent / evil-one / evil-age sub-corpus within "
     "ponēros (~10–15V) carries M27 cross-register flag and will receive a distinct VCG. Mat 6:34 kakia "
     "(M03 trouble-register, 1V) and Eph 6:12 ponēria (M27 cosmic-evil, 1V) remain in this sub-group as "
     "flag-only minorities.",
     2),
    ("M10b-C", "Abomination — divine revulsion at corrupt moral character and conduct",
     "CHAR-3 (Abomination: divine-revulsion judgment on moral character). The category of evil that "
     "violates divine holiness and provokes God's active revulsion — directed at corrupt moral character "
     "and ethical failure rather than idolatry. Inner-being dimensions: the abominable person's inner "
     "state (crooked heart, proud heart, lying lips, perverted judgment, conscience violated and "
     "silenced), and the divine inner response (revulsion, disgust, hatred, rejection). The three-part "
     "co-occurrence pattern — act defiling + boundary transgressed + divine revulsion — names the "
     "mechanism of abomination. Primary terms: to.e.vah moral sub-corpus (~70V), bdelugma moral verses "
     "(4V — Luk 16:15, Rev 17:4, 17:5, 21:27), bdeluktos (1V Tit 1:16).",
     3),
    ("M10b-D", "Idolatrous abomination — will conformed to detestable false devotion",
     "CHAR-4 (Idolatrous abomination: the heart devoted to false gods). The specific form of abomination "
     "rooted in idolatrous devotion — the will's conformity to detestable practices, the heart going "
     "after idol-objects, worship corrupted through false devotion. Inner-being dimensions: the heart's "
     "defiant attachment to idols, the soul that actively delights in abominations rather than recoiling, "
     "the pride that converts beautiful gifts into idol-objects, the conscience deadened to the horror "
     "of idolatrous acts. Primary terms: to.e.vah idolatry sub-corpus (~37V), shiq.quts (25V — "
     "predominantly idol-objects named as detestable). Secondary: bdelugma desecration-event verses "
     "(2V — Mat 24:15, Mar 13:14). Cross-register flags: M27 (idol-object / concrete-abomination) strong; "
     "M10c (cultic/ritual defilement) for the Levitical/Deuteronomic/Ezekiel boundary-law and "
     "defilement-of-land sub-corpora.",
     4),
    ("M10b-E", "Iniquity — evil as an active inner process of scheming and harm-generation",
     "CHAR-5 (Iniquity as active inner scheming and evil generation). Evil as an ongoing active inner "
     "process — devised, cultivated, generated, and enacted from within. Iniquity is plotted on the bed "
     "at night, conceived in the heart, schemed by the mind, and born into harmful deeds. The evildoer "
     "is a person who works iniquity as a habitual pursuit, exploiting others, lurking with predatory "
     "intent. Also encompasses the evil-deeds register — deeds whose inner origin is wickedness, and "
     "whose quality marks the one who commits them. Primary terms: a.ven (66V), ro.a evil-deeds "
     "sub-corpus (13V). Phase 7 polysemy note: a.ven's trouble/distress sub-corpus (~18V) carries "
     "M03/M27 cross-register flags and will receive a distinct VCG within this sub-group. Neh 2:2 + "
     "Ecc 7:3 ro.a (M03 sadness register, 2V) remain in this sub-group as flag-only minorities.",
     5),
    ("M10b-F", "Blasphemy and defaming evil — wickedness flowing through the instrument of speech",
     "CHAR-6 (Evil expressed in speech: blasphemy, defamation, and perverse testimony). The inner "
     "character of wickedness expressed through speech — the defiant will that generates contemptuous "
     "blasphemy against God even under judgment, the hostile slander that falsely charges the innocent "
     "as evildoers, the deceptive misrepresentation that inverts moral reality through verbal manipulation. "
     "The hardened will interprets divine judgment as occasion for further defiance (Rev 16:9–21). Primary "
     "terms: blasfēmeō (11V), kakopoios (5V), atopos (1V). Cross-register flag: M06 "
     "(contempt / hostile speech / defiant rejection of authority) — blasfēmeō primary signal.",
     6),
]


def parse_passage_groups(passage_strings: list[str]) -> set[str]:
    """Parse the AI's D-list passage strings into a set of canonical references.

    Handles patterns:
      - 'Book chap:verse' (full reference)
      - 'Book chap:verse, chap:verse, ...' (book carry-over)
      - 'chap:verse' alone (uses last book in context)
    Skips any text we don't recognise as a reference (descriptive prefixes etc).
    """
    out: set[str] = set()
    for chunk in passage_strings:
        last_book = None
        # Split on commas and semicolons at the outer level
        for piece in re.split(r"[,;]", chunk):
            piece = piece.strip()
            if not piece:
                continue
            # Strip leading non-reference prefix (e.g. 'Ezekiel idolatry: Eze 5:9')
            # Try to find a 'Book chap:verse' anywhere in the piece
            m = re.search(r"(\d?\s?[A-Z][a-z]+)\s+(\d+):(\d+(?:[-–]\d+)?)", piece)
            if m:
                last_book = m.group(1).replace(" ", "")
                chap, vspec = m.group(2), m.group(3)
                _expand(out, last_book, chap, vspec)
                continue
            # Just chap:verse — carry-over book
            m = re.match(r"^(\d+):(\d+(?:[-–]\d+)?)\s*$", piece)
            if m and last_book:
                chap, vspec = m.group(1), m.group(2)
                _expand(out, last_book, chap, vspec)
    return out


def _expand(out: set[str], book: str, chap: str, vspec: str) -> None:
    m = re.match(r"(\d+)[-–](\d+)$", vspec)
    if m:
        a, b = int(m.group(1)), int(m.group(2))
        for v in range(a, b + 1):
            out.add(f"{book} {chap}:{v}")
    else:
        out.add(f"{book} {chap}:{vspec}")


def resolve_mapping(conn) -> tuple[dict[int, str], dict[int, dict[str, int]]]:
    """Return (vc_id_to_subgroup_code, per_term_per_subgroup_count).

    Reads the AI mapping JSON, resolves all per-verse splits + to.e.vah passage
    groups against live DB rows.
    """
    mapping = json.loads(MAPPING_PATH.read_text(encoding="utf-8"))

    # Pull every active is_relevant vc row for M10b
    rows = list(conn.execute("""
        SELECT vc.id AS vc_id, vc.mti_term_id, vr.reference
        FROM verse_context vc
        JOIN mti_terms mt ON mt.id = vc.mti_term_id
        JOIN wa_verse_records vr ON vr.id = vc.verse_record_id
        WHERE mt.cluster_code = ?
          AND COALESCE(mt.delete_flagged, 0) = 0
          AND vc.is_relevant = 1
          AND COALESCE(vc.delete_flagged, 0) = 0
          AND COALESCE(vr.delete_flagged, 0) = 0
    """, (CLUSTER,)).fetchall())

    # Index AI's per-verse rules
    term_defaults: dict[int, str] = {}
    per_verse_rules: dict[int, dict[str, str]] = {}  # mti_id -> {reference: subgroup}
    for t in mapping["term_assignments"]:
        mti = t["mti_id"]
        term_defaults[mti] = t["primary_subgroup"]
        if t.get("split") and t["split"].get("type") == "per_verse_reference":
            d: dict[str, str] = {}
            for rule in t["split"]["rules"]:
                for ref in rule["references"]:
                    d[ref] = rule["assign_to"]
            per_verse_rules[mti] = d

    # to.e.vah special: parse passage groups
    toevah_d_refs: set[str] = set()
    for t in mapping["term_assignments"]:
        if t["mti_id"] == 250 and t.get("split", {}).get("type") == "per_verse_content_review":
            toevah_d_refs = parse_passage_groups(
                t["split"]["D_assign_guidance"]["passage_groups"]
            )
            break

    # Resolve every vc row
    vc_to_sg: dict[int, str] = {}
    per_term_per_sg: dict[int, dict[str, int]] = defaultdict(lambda: defaultdict(int))
    for r in rows:
        mti = r["mti_term_id"]
        ref = r["reference"]
        if mti in per_verse_rules and ref in per_verse_rules[mti]:
            sg = per_verse_rules[mti][ref]
        elif mti == 250:
            sg = "M10b-D" if ref in toevah_d_refs else "M10b-C"
        else:
            sg = term_defaults[mti]
        vc_to_sg[r["vc_id"]] = sg
        per_term_per_sg[mti][sg] += 1

    return vc_to_sg, per_term_per_sg


def fetch_term_info(conn, mti_ids: list[int]) -> dict[int, dict]:
    rows = conn.execute(
        f"SELECT id, strongs_number, transliteration FROM mti_terms WHERE id IN "
        f"({','.join('?'*len(mti_ids))})", mti_ids
    ).fetchall()
    return {r["id"]: {"strongs": r["strongs_number"], "translit": r["transliteration"]} for r in rows}


def main(live: bool) -> int:
    print(f"=== M10b Phase 6 apply — mode={'LIVE' if live else 'DRY-RUN'} ===")

    if live:
        ts = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")
        backup = REPO / "backups" / f"bible_research_backup_{ts}_M10b-phase6-subgroup-assign.db"
        backup.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(DB, backup)
        print(f"Backup: {backup.relative_to(REPO)}")

    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row

    # Pre-checks
    pre_cluster = conn.execute(
        "SELECT status FROM cluster WHERE cluster_code=?", (CLUSTER,)
    ).fetchone()
    print(f"Pre cluster status: {pre_cluster['status']}")

    n_existing_sg = conn.execute(
        "SELECT COUNT(*) FROM cluster_subgroup WHERE cluster_code=? AND COALESCE(delete_flagged,0)=0",
        (CLUSTER,)
    ).fetchone()[0]
    if n_existing_sg:
        print(f"ERROR: {n_existing_sg} existing cluster_subgroup rows for {CLUSTER} — aborting.")
        return 1

    # Resolve mapping
    vc_to_sg, per_term_per_sg = resolve_mapping(conn)
    print(f"Resolved: {len(vc_to_sg)} vc rows mapped to {len(set(vc_to_sg.values()))} sub-groups")
    print()
    print("Per sub-group totals:")
    sg_counter = Counter(vc_to_sg.values())
    for sg_code, _, _, _ in SUBGROUPS:
        print(f"  {sg_code}: {sg_counter[sg_code]} verses")
    print()

    # Term-level summary
    term_info = fetch_term_info(conn, list(per_term_per_sg.keys()))
    print("Per-term sub-group assignment:")
    for mti in sorted(per_term_per_sg.keys(), key=lambda k: -sum(per_term_per_sg[k].values())):
        info = term_info[mti]
        sgs = ", ".join(f"{sg}={n}" for sg, n in sorted(per_term_per_sg[mti].items()))
        n_total = sum(per_term_per_sg[mti].values())
        print(f"  {info['strongs']:8s} {info['translit']:18s} (mti={mti}, V={n_total}): {sgs}")
    print()

    # Write resolved mapping for audit
    resolved = {
        "_meta": {
            "cluster_code": CLUSTER,
            "directive_id": DIRECTIVE_ID,
            "generated_at": NOW,
            "source_mapping": MAPPING_PATH.name,
            "total_verses": len(vc_to_sg),
        },
        "vc_to_subgroup": {str(k): v for k, v in sorted(vc_to_sg.items())},
        "per_subgroup_counts": {sg: sg_counter[sg] for sg, *_ in SUBGROUPS},
        "per_term_per_subgroup": {
            str(mti): dict(per_term_per_sg[mti]) for mti in sorted(per_term_per_sg.keys())
        },
    }
    if live:
        RESOLVED_PATH.write_text(json.dumps(resolved, indent=2, ensure_ascii=False), encoding="utf-8")
        print(f"Wrote resolved mapping: {RESOLVED_PATH.relative_to(REPO)}")
    else:
        print(f"(Resolved mapping would be written to: {RESOLVED_PATH.relative_to(REPO)})")

    if not live:
        print("\n[DRY-RUN — no DB writes]")
        conn.close()
        return 0

    # === LIVE apply ===
    conn.execute("BEGIN")
    try:
        # Op A: INSERT cluster_subgroup rows
        sg_id_by_code: dict[str, int] = {}
        for code, label, desc, sort_order in SUBGROUPS:
            cur = conn.execute(
                "INSERT INTO cluster_subgroup "
                "(cluster_code, subgroup_code, label, core_description, sort_order, "
                " status, version, source, delete_flagged, created_at, last_updated_date) "
                "VALUES (?, ?, ?, ?, ?, 'active', 'v1', ?, 0, ?, ?)",
                (CLUSTER, code, label, desc, sort_order, DIRECTIVE_ID, NOW, NOW),
            )
            sg_id_by_code[code] = cur.lastrowid
        print(f"Op A: created {len(sg_id_by_code)} cluster_subgroup rows")

        # Op B: INSERT mti_term_subgroup rows
        n_ms = 0
        for mti, sg_counts in per_term_per_sg.items():
            sg_sorted = sorted(sg_counts.items(), key=lambda x: -x[1])  # primary = biggest
            for i, (sg_code, n) in enumerate(sg_sorted):
                placement = f"[{'primary' if i == 0 else 'secondary'}] {n} verses"
                conn.execute(
                    "INSERT INTO mti_term_subgroup "
                    "(mti_term_id, cluster_subgroup_id, placement_note, "
                    " delete_flagged, created_at, last_updated_date) "
                    "VALUES (?, ?, ?, 0, ?, ?)",
                    (mti, sg_id_by_code[sg_code], placement, NOW, NOW),
                )
                n_ms += 1
        print(f"Op B: created {n_ms} mti_term_subgroup rows")

        # Op C: UPDATE verse_context.cluster_subgroup_id
        n_vc = 0
        for vc_id, sg_code in vc_to_sg.items():
            cur = conn.execute(
                "UPDATE verse_context SET cluster_subgroup_id=? "
                "WHERE id=? AND COALESCE(delete_flagged,0)=0",
                (sg_id_by_code[sg_code], vc_id),
            )
            n_vc += cur.rowcount
        print(f"Op C: updated {n_vc} verse_context.cluster_subgroup_id")

        # Op D: cluster status transition
        cur = conn.execute(
            "UPDATE cluster SET status='Analysis - In Progress', last_updated_date=? "
            "WHERE cluster_code=? AND status='Data - In Progress'",
            (NOW, CLUSTER),
        )
        print(f"Op D: cluster status flipped ({cur.rowcount} row updated)")

        # Post-state checks
        unrouted = conn.execute("""
            SELECT COUNT(*) FROM verse_context vc
            JOIN mti_terms mt ON mt.id = vc.mti_term_id
            WHERE mt.cluster_code = ? AND vc.is_relevant = 1
              AND COALESCE(vc.delete_flagged, 0) = 0
              AND vc.cluster_subgroup_id IS NULL
        """, (CLUSTER,)).fetchone()[0]
        if unrouted:
            raise RuntimeError(f"Post-check failed: {unrouted} unrouted is_relevant rows")
        print(f"Post-check: 0 unrouted is_relevant rows ✓")

        new_status = conn.execute(
            "SELECT status FROM cluster WHERE cluster_code=?", (CLUSTER,)
        ).fetchone()["status"]
        if new_status != "Analysis - In Progress":
            raise RuntimeError(f"Post-check failed: status is {new_status!r}")
        print(f"Post-check: cluster status = {new_status} ✓")

        conn.commit()
        print("\nCOMMITTED")
    except Exception:
        conn.rollback()
        print("ROLLED BACK")
        raise
    finally:
        conn.close()

    return 0


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--live", action="store_true", help="Apply (default: dry-run)")
    args = ap.parse_args()
    sys.exit(main(args.live))
