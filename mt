SELECT 
    DATE_FORMAT(trans_date, '%Y-%m') AS month,  -- Extract year and month
    country,                                    -- Group by country
    COUNT(*) AS trans_count,                     -- Total number of transactions
    SUM(CASE WHEN state = 'approved' THEN 1 ELSE 0 END) AS approved_count,  -- Count approved transactions
    SUM(amount) AS trans_total_amount,           -- Total amount of all transactions
    SUM(CASE WHEN state = 'approved' THEN amount ELSE 0 END) AS approved_total_amount  -- Total amount of approved transactions
FROM 
    Transactions
GROUP BY 
    month, country
ORDER BY 
    month, country;
