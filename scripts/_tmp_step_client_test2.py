"""End-to-end test for the enhanced step_client.py (v2)."""
import sys
sys.path.insert(0, r"G:\My Drive\Bible_study_projects")
from analytics.step_client import StepClient

c = StepClient()

for strong in ["H8057", "G5479", "H2428", "G9559"]:
    data = c.extract_word_data(strong)
    v = data["vocab"]
    print(
        f"{strong}: lang={v.get('language')}, gloss={v.get('gloss')!r}, "
        f"occur={v.get('occurrence_count')}, verse_count={data['verse_count']}, "
        f"testament={data['testament']}"
    )
    print(
        f"  meaning_numbered={v.get('meaning_numbered')}, "
        f"causative_form_present={v.get('causative_form_present')}"
    )
    lsj = v.get("lsj_entry", "")
    if lsj:
        print(f"  lsj_entry (first 120): {lsj[:120]}")
    smd = v.get("short_def_mounce", "")
    if smd:
        print(f"  short_def_mounce: {smd[:100]}")
    if data["notes"]:
        print(f"  notes: {data['notes']}")
    if data["verse_records"]:
        r0 = data["verse_records"][0]
        print(
            f"  first verse: {r0['ref']} | testament={r0['testament']} | "
            f"book={r0['book_code']} | ch={r0['chapter']} | v={r0['verse_num']} | "
            f"target_word={r0['target_word']!r}"
        )
    print()
