CREATE PROCEDURE CalculateDailySales(IN store INT, IN date_selected DATE)
BEGIN
    SELECT s.store_id, st.store_name, SUM(s.quantity * p.price) AS total_sales
    FROM sales s
    JOIN products p ON s.product_id = p.product_id
    JOIN stores st ON s.store_id = st.store_id
    WHERE s.store_id = store AND s.sale_date = date_selected
    GROUP BY s.store_id, st.store_name;
END;
