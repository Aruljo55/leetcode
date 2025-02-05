CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
DETERMINISTIC
BEGIN
    RETURN (
        SELECT salary FROM (
            SELECT DISTINCT salary FROM Employee ORDER BY salary DESC LIMIT N
        ) AS temp_table ORDER BY salary ASC LIMIT 1
    );
END;
