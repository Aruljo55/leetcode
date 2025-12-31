SELECT 
    CASE 
        WHEN MOD(s1.id, 2) = 1 THEN s2.id
        ELSE s1.id 
    END AS id,
    CASE 
        WHEN MOD(s1.id, 2) = 1 THEN s2.student
        ELSE s1.student 
    END AS student
FROM Seat s1
LEFT JOIN Seat s2 ON s1.id = s2.id - 1
ORDER BY id;
