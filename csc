SELECT 
    category,
    COUNT(*) AS accounts_count
FROM (
    SELECT 
        CASE 
            WHEN income < 20000 THEN 'Low Salary'
            WHEN income BETWEEN 20000 AND 50000 THEN 'Average Salary'
            WHEN income > 50000 THEN 'High Salary'
        END AS category
    FROM Accounts
) AS categorized_accounts
GROUP BY category
ORDER BY FIELD(category, 'Low Salary', 'Average Salary', 'High Salary');
