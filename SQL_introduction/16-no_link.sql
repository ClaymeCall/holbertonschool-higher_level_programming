-- Lists all recoreds without an empty name value
SELECT score, name FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
