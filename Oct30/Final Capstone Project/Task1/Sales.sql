-- mysql_schema_and_scripts.sql
-- Run in MySQL client (mysql -u root -p) or workbench

CREATE DATABASE IF NOT EXISTS retail_capstone;
USE retail_capstone;

-- PRODUCTS table
CREATE TABLE IF NOT EXISTS products (
  product_id INT AUTO_INCREMENT PRIMARY KEY,
  sku VARCHAR(64) NOT NULL UNIQUE,
  name VARCHAR(255) NOT NULL,
  category VARCHAR(100),
  price DECIMAL(10,2),
  created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- INVENTORY table
CREATE TABLE IF NOT EXISTS inventory (
  inventory_id INT AUTO_INCREMENT PRIMARY KEY,
  product_id INT NOT NULL,
  store_id VARCHAR(50),
  quantity INT DEFAULT 0,
  last_updated DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE
);

-- SALES table
CREATE TABLE IF NOT EXISTS sales (
  sale_id INT AUTO_INCREMENT PRIMARY KEY,
  product_id INT NOT NULL,
  sale_date DATETIME NOT NULL,
  quantity INT NOT NULL,
  unit_price DECIMAL(10,2) NOT NULL,
  store_id VARCHAR(50),
  total_amount DECIMAL(12,2) AS (quantity * unit_price) STORED,
  FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE
);

-- Sample CRUD operations

-- Insert sample products
INSERT INTO products (sku, name, category, price) VALUES
('SKU-1001','Acrylic Necklace','Accessories',199.00),
('SKU-1002','Hoop Earrings','Accessories',149.00),
('SKU-2001','Cotton T-Shirt','Apparel',499.00);

-- Insert inventory
INSERT INTO inventory (product_id, store_id, quantity) VALUES
(1,'Store-01',50),
(2,'Store-01',20),
(3,'Store-02',10);

-- Insert sales
INSERT INTO sales (product_id, sale_date, quantity, unit_price, store_id) VALUES
(1,'2025-10-01 10:00:00',2,199.00,'Store-01'),
(2,'2025-10-02 12:15:00',1,149.00,'Store-01'),
(3,'2025-10-05 15:00:00',3,499.00,'Store-02');

-- Read queries
SELECT p.*, i.store_id, i.quantity
FROM products p
LEFT JOIN inventory i ON p.product_id = i.product_id;

SELECT s.*, p.name, p.category
FROM sales s JOIN products p USING (product_id)
ORDER BY s.sale_date DESC LIMIT 50;

-- Update product price
UPDATE products SET price = 179.00 WHERE sku = 'SKU-1001';

-- Delete a product (cascades to inventory & sales)
-- DELETE FROM products WHERE product_id = 99;

-- Stored procedure: identify low-stock items under threshold
DELIMITER $$
CREATE PROCEDURE sp_get_low_stock(IN threshold INT)
BEGIN
  SELECT p.product_id, p.sku, p.name, i.store_id, i.quantity
  FROM products p
  JOIN inventory i ON p.product_id = i.product_id
  WHERE i.quantity <= threshold
  ORDER BY i.quantity ASC;
END$$
DELIMITER ;

-- Usage:
-- CALL sp_get_low_stock(10);
