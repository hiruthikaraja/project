create database company_db;
use company_db;
create table employees(
Employee_ID int primary key auto_increment,
First_Name varchar(100),
Last_Name varchar(50),
Age int,
Department varchar(20),
Salary int );

insert into employees(First_Name,Last_Name,Age,Department,Salary)
values 
('Kokki','kumar','21','IT',25000),
('kavin','kamal','22','Manual',27000),
('madi','manoj','23','testing',28000),
('pottu','sree','21','QA',29000),
('adhi','mala','22','SDE',22000);

select * from employees;
select First_Name,Department,Salary from employees;
select * from employees where Department='IT';

update employees set Department = 'Accounts' where Department = 'Manual';
delete from employees where Department = 'QA';
