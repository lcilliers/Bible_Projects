import sqlite3

def run_query():
    conn = sqlite3.connect('file:database/bible_research.db?mode=ro', uri=True)
    cursor = conn.cursor()
    
    # prose_section_type joined to active current prose_section rows 
    # (source_stage='programme', delete_flagged=0, prose_section.delete_flagged=0, superseded_by_id IS NULL)
    # return chapter_no, sort_order, code, label, prose_section.id ordered by sort_order
    
    query = """
    SELECT 
        pst.chapter_no, 
        pst.sort_order, 
        pst.code, 
        pst.label, 
        ps.id
    FROM prose_section_type pst
    JOIN prose_section ps ON pst.id = ps.section_type_id
    WHERE pst.source_stage = 'programme'
      AND pst.delete_flagged = 0
      AND ps.delete_flagged = 0
      AND ps.superseded_by_id IS NULL
    ORDER BY pst.sort_order;
    """
    
    cursor.execute(query)
    rows = cursor.fetchall()
    
    print(f"Total active joined rows: {len(rows)}")
    print("\nJoined rows (ordered by pst.sort_order):")
    print(f"{'chapter_no':<12} | {'sort_order':<10} | {'code':<10} | {'label':<40} | {'prose_section.id':<16}")
    print("-" * 100)
    for r in rows:
        print(f"{str(r[0]):<12} | {str(r[1]):<10} | {str(r[2]):<10} | {str(r[3])[:40]:<40} | {str(r[4]):<16}")
        
    # Check duplicate or NULL sort_order values
    sort_orders = [r[1] for r in rows]
    null_count = sum(1 for so in sort_orders if so is None)
    
    seen = set()
    duplicates = set()
    for so in sort_orders:
        if so is not None:
            if so in seen:
                duplicates.add(so)
            seen.add(so)
            
    print("\n--- Sort Order Duplicates / NULLs Check ---")
    print(f"NULL sort_order count: {null_count}")
    print(f"Duplicate sort_order values: {sorted(list(duplicates))}")
    
    # Check rows where chapter_no changes while sort_order sequence is not monotonic
    # Specifically: 'any rows where chapter_no changes while sort_order sequence is not monotonic.'
    # Let's assess the exact progression of chapter_no and sort_order.
    # Monotonicity of sort_order: does it always increase or stay same?
    # Let's inspect chapter transitions and sort_order transitions.
    print("\n--- Monotonicity and Chapter Changes Check ---")
    prev_chapter = None
    prev_sort_order = None
    issues = []
    
    for idx, (chapter_no, sort_order, code, label, ps_id) in enumerate(rows):
        if idx > 0:
            # check if sort_order is monotonic (it is ordered by sort_order, so by definition pst.sort_order is non-decreasing).
            # But let's check if there are cases where chapter_no transitions but the sequence has oddities,
            # or if they meant ordering by something else or if we check if sort_order increases monotonically within/across chapters.
            # Let's check both ways.
            if sort_order < prev_sort_order:
                issues.append(f"Row {idx}: sort_order decreased from {prev_sort_order} to {sort_order} (this shouldn't happen because we ORDER BY sort_order)")
            
            # If chapter changes, does the sort_order sequence not progress monotonically? Or maybe we can check if within a chapter, sort_order is monotonic?
            # Or if sorted by chapter_no, is sort_order not monotonic? Let's check.
        prev_chapter = chapter_no
        prev_sort_order = sort_order

    # Let's query without ORDER BY sort_order (e.g. ORDER BY some other default, or let's inspect the entire active set sorted by chapter_no, then sort_order)
    query_by_chap = """
    SELECT 
        pst.chapter_no, 
        pst.sort_order, 
        pst.code, 
        pst.label, 
        ps.id
    FROM prose_section_type pst
    JOIN prose_section ps ON pst.id = ps.section_type_id
    WHERE pst.source_stage = 'programme'
      AND pst.delete_flagged = 0
      AND ps.delete_flagged = 0
      AND ps.superseded_by_id IS NULL
    ORDER BY pst.chapter_no, pst.sort_order;
    """
    cursor.execute(query_by_chap)
    rows_by_chap = cursor.fetchall()
    
    # Let's check if the sort_order is monotonic across this layout (sorted by chapter)
    prev_so = -1
    chap_monotonic_issues = []
    for r in rows_by_chap:
        if r[1] is not None:
            if r[1] < prev_so:
                chap_monotonic_issues.append(f"Sort order decreased (from {prev_so} to {r[1]}) when ordered by chapter_no at chapter {r[0]} code {r[2]}")
            prev_so = r[1]
            
    if chap_monotonic_issues:
        print("Issues when ordered by chapter_no first, then sort_order:")
        for issue in chap_monotonic_issues:
            print("  ", issue)
    else:
        print("Sort order is strictly monotonic when ordered by chapter_no.")
        
    print("\n--- Checking files for generated markdown/exporter output ---")
    # Let's find any markdown files or Python scripts related to exporters or generated markdown.
    
run_query()
