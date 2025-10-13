-- Register Delta table for SQL queries
CREATE OR REPLACE TEMPORARY VIEW product_sales AS
SELECT * FROM delta.`/mnt/retail360/etl/products_sales_metrics`;

-- Query top 3 best-selling products
SELECT product_name, category, SUM(total_sale) AS total_sales
FROM product_sales
GROUP BY product_name, category
ORDER BY total_sales DESC
LIMIT 3;
