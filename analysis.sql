-- Query 1: Category-wise revenue potential
SELECT category,
       COUNT(*) as product_count,
       AVG(price) as avg_price,
       SUM(stock) as total_stock
FROM api_products
GROUP BY category
ORDER BY avg_price DESC;

-- Query 2: Top rated expensive products
SELECT title, brand, price, rating, stock
FROM api_products
WHERE rating > 4.5
ORDER BY price DESC
LIMIT 10;