create table orders(
order_id int primary key auto_increment,
customer_name varchar(50) not null,
product varchar(50),
quantity int,
price decimal(10,2),
order_date date);

INSERT INTO orders (customer_name, product, quantity, price, order_date) VALUES
('Rahul Sharma', 'Laptop', 1, 55000.00, '2025-01-05'),
('Priya Singh', 'Headphones', 2, 3000.00, '2025-01-06'),
('Aman Kumar', 'Mobile Phone', 1, 25000.00, '2025-01-06'),
('Sneha Reddy', 'Keyboard', 3, 1500.00, '2025-01-07'),
('Arjun Mehta', 'Monitor', 2, 12000.00, '2025-01-07'),
('Pooja Iyer', 'Laptop', 1, 60000.00, '2025-01-08'),
('Ravi Sharma', 'Mouse', 5, 800.00, '2025-01-08'),
('Neha Kapoor', 'Tablet', 1, 20000.00, '2025-01-09'),
('Vikram Rao', 'Printer', 1, 8500.00, '2025-01-09'),
('Divya Nair', 'Laptop', 2, 58000.00, '2025-01-10');

select * from orders where order_date = '2025-01-07';
select * from orders where price>20000;
select * from orders where product = 'Laptop';
select * from orders where quantity >2;
select * from orders order by price DESC;
select * from orders order by order_date,customer_name;

select count(*) as total_orders from orders;
select avg(price) as average from orders;
select max(price) as maxi from orders;
select sum(quantity) from orders;
select product,sum(quantity*price) from orders group by product;
select count(product) from orders group by product;
select avg(price) from orders group by customer_name;
select product, sum(quantity) from orders group by product having sum(quantity) >3;
select customer_name from orders group by customer_name having count(customer_name) >1;
