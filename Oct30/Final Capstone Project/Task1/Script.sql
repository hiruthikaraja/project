CREATE DATABASE retail_db;
USE retail_db;

CREATE TABLE products (
  product_id INT PRIMARY KEY AUTO_INCREMENT,
  name VARCHAR(50),
  category VARCHAR(30),
  price DECIMAL(10,2)
);

CREATE TABLE sales (
  sale_id INT PRIMARY KEY AUTO_INCREMENT,
  product_id INT,
  sale_date DATETIME,
  quantity INT,
  unit_price DECIMAL(10,2),
  store_id VARCHAR(20),
  total_amount DECIMAL(10,2),
  FOREIGN KEY (product_id) REFERENCES products(product_id)
);

CREATE TABLE inventory (
  inventory_id INT PRIMARY KEY AUTO_INCREMENT,
  product_id INT,
  stock_quantity INT,
  last_updated DATETIME,
  FOREIGN KEY (product_id) REFERENCES products(product_id)
);

-- CRUD Examples
INSERT INTO products (name, category, price)
VALUES ('Acrylic Necklace', 'Accessories', 199.00),
       ('Hoop Earrings', 'Accessories', 149.00),
       ('Cotton T-Shirt', 'Apparel', 499.00);

INSERT INTO sales (product_id, sale_date, quantity, unit_price, store_id, total_amount)
VALUES (1, '2025-10-01 10:00:00', 2, 199.00, 'Store-01', 398.00),
       (2, '2025-10-02 12:15:00', 1, 149.00, 'Store-01', 149.00),
       (3, '2025-10-05 15:00:00', 3, 499.00, 'Store-02', 1497.00);

-- Stored Procedure
DELIMITER //
CREATE PROCEDURE GetLowStockItems()
BEGIN
  SELECT p.name, i.stock_quantity
  FROM inventory i
  JOIN products p ON i.product_id = p.product_id
  WHERE i.stock_quantity < 10;
END //
DELIMITER ;

CALL GetLowStockItems();
