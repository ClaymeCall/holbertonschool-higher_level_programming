-- Groups entries by score
SELECT SUM(*) FROM second_table
GROUP BY score
ORDER BY number DESC;
