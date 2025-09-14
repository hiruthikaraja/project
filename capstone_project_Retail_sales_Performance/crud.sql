INSERT INTO products (product_name, category, price)
VALUES
('Shampoo', 'Personal Care', 120.00),
('Biscuits', 'Food', 20.00),
('Notebook', 'Stationery', 40.00);

INSERT INTO stores (store_name, region)
VALUES
('Store A', 'North'),
('Store B', 'South');

INSERT INTO employees (first_name, last_name, role, store_id)
VALUES
('Amit', 'Verma', 'Manager', 1),
('Sneha', 'Reddy', 'Cashier', 2);

INSERT INTO sales (product_id, store_id, quantity, sale_date)
VALUES
(1, 1, 10, '2025-09-10'),
(2, 2, 20, '2025-09-11'),
(3, 1, 15, '2025-09-12');

SELECT * FROM sales;

UPDATE products SET price = 25.00 WHERE product_id = 2;

DELETE FROM sales WHERE sale_id = 1;
