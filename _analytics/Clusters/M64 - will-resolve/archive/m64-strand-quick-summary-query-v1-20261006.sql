-- M64 quick summary pull. Researcher-supplied query, 2026-10-06, run unchanged (read-only, iba.db).
-- Note: other_m_hits is filtered to cs.cluster_code = 'M64', so each M64 hit is paired with every
-- M64 hit in the same verse, itself included (distance 0).
WITH CL_hits AS (
  SELECT vl.id AS vl_id, vl.verse_id, vl.position AS cl_position,
         vl.strong AS cl_strong, vl.surface AS cl_surface
  FROM verse_lexical vl
  JOIN cluster_strong cs ON cs.strong = vl.strong AND cs.cluster_code = 'M64'
  JOIN cluster mc ON mc.cluster_code = cs.cluster_code AND mc.deleted = 0
  WHERE vl.deleted = 0
),
other_m_hits AS (
  SELECT vl.verse_id, vl.position AS other_position, vl.strong AS other_strong,
         vl.surface AS other_surface, cs.cluster_code AS other_cluster_code,
         c.short_name AS other_cluster_name
  FROM verse_lexical vl
  JOIN cluster_strong cs ON cs.strong = vl.strong
  JOIN cluster c ON c.cluster_code = cs.cluster_code AND c.deleted = 0
  WHERE vl.deleted = 0
    AND cs.cluster_code = 'M64'
    AND vl.verse_id IN (SELECT verse_id FROM CL_hits)
)
SELECT
  v.reference,
  m.cl_strong, ms.stepGloss AS cl_gloss, m.cl_surface, m.cl_position,
  o.other_strong, os.stepGloss AS other_gloss, o.other_surface,
  o.other_cluster_code, o.other_cluster_name, o.other_position,
  ABS(m.cl_position - o.other_position) AS distance
FROM CL_hits m
JOIN verse v ON v.id = m.verse_id
JOIN other_m_hits o ON o.verse_id = m.verse_id
LEFT JOIN strong ms ON ms.strongNumber = m.cl_strong
LEFT JOIN strong os ON os.strongNumber = o.other_strong
ORDER BY v.reference, m.cl_position, o.other_position;
