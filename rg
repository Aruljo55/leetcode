SELECT 
    visited_on,
    amount,
    ROUND(
        SUM(amount) OVER (
            ORDER BY visited_on
            ROWS BETWEEN 6 PRECEDING AND CURRENT ROW
        ) / 7, 2) AS average_amount
FROM Customer
WHERE visited_on >= '2019-01-07'
ORDER BY visited_on;
