
CREATE DATABASE IF NOT EXISTS company_db;
USE company_db;

DROP TABLE IF EXISTS staff;
DROP TABLE IF EXISTS departments;

CREATE TABLE departments (
    dept_id INT PRIMARY KEY AUTO_INCREMENT,
    dept_name VARCHAR(50) NOT NULL UNIQUE,
    location VARCHAR(50) NOT NULL
);    

CREATE TABLE staff (
    staff_id INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    age INT,
    salary DECIMAL(10,2),
    dept_id INT NULL,
    CONSTRAINT fk_staff_dept
        FOREIGN KEY (dept_id) REFERENCES departments(dept_id)
);

INSERT INTO departments (dept_id, dept_name, location) VALUES
(1, 'IT', 'Bangalore'),
(2, 'HR', 'Hyderabad'),
(3, 'Finance', 'Mumbai'),   
(4, 'Marketing', 'Delhi'),
(5, 'Operations', 'Chennai'),
(6, 'R&D', 'Pune');

INSERT INTO staff (staff_id, first_name, last_name, age, salary, dept_id) VALUES
(101, 'Amit', 'Verma', 28, 55000.00, 1),  
(102, 'Sneha', 'Reddy', 32, 60000.00, 2),
(103, 'Ravi', 'Sharma', 26, 48000.00, NULL), 
(104, 'Pooja', 'Iyer', 29, 52000.00, 4),  
(105, 'Arjun', 'Mehta', 35, 75000.00, 1), 
(106, 'Divya', 'Nair', 30, 50000.00, 5),  
(107, 'Rahul', 'Kapoor', 41, 91000.00, 1),
(108, 'Priya', 'Singh', 24, 42000.00, NULL), 
(109, 'Vikram', 'Rao', 37, 68000.00, 4),  
(110, 'Neha', 'Kulkarni', 33, 58500.00, 2);

#1
SELECT * FROM staff;

#2
SELECT first_name, last_name, salary
FROM staff
WHERE salary > 60000;

#3
SELECT * 
FROM staff
WHERE dept_id IS NULL;

#4
SELECT * 
FROM staff
ORDER BY age ASC;

#5
SELECT COUNT(*) AS total_staff
FROM staff;

#Part B 

#6
SELECT * FROM departments;

#7
SELECT * 
FROM departments
WHERE location IN ('Bangalore', 'Chennai');

#8
SELECT dept_name
FROM departments
WHERE dept_name LIKE 'M%';

#9
SELECT COUNT(DISTINCT location) AS unique_locations
FROM departments;

#9
SELECT * 
FROM departments
ORDER BY dept_name ASC;

#Part C 

#11
SELECT s.first_name, s.last_name, d.dept_name
FROM staff s
INNER JOIN departments d ON s.dept_id = d.dept_id;

#12
SELECT s.first_name, s.last_name, s.salary
FROM staff s
INNER JOIN departments d ON s.dept_id = d.dept_id
WHERE d.dept_name = 'IT';


#Part D 

#14
SELECT s.first_name, s.last_name, d.dept_name
FROM staff s
LEFT JOIN departments d ON s.dept_id = d.dept_id;

#15 
SELECT s.first_name, s.last_name
FROM staff s
LEFT JOIN departments d ON s.dept_id = d.dept_id
WHERE d.dept_id IS NULL;


# RIGHT JOIN

#17
SELECT d.dept_name, s.first_name, s.last_name
FROM departments d
RIGHT JOIN staff s ON d.dept_id = s.dept_id;

#18
SELECT d.dept_name
FROM departments d
LEFT JOIN staff s ON d.dept_id = s.dept_id
WHERE s.staff_id IS NULL;

#19
SELECT d.dept_name, s.first_name, s.last_name
FROM departments d
LEFT JOIN staff s ON d.dept_id = s.dept_id;
