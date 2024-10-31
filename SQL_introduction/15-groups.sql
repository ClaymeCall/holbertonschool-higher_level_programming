-- Groups entries by score
SELECT score, COUNT(*) FROM second_table
GROUP BY score
ORDER BY number DESC;
