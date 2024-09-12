CREATE DATABASE my_school;


USE my_school;



CREATE TABLE students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    age INT,
    grade CHAR(1)
);


INSERT INTO students (name, age, grade) VALUES
('Alice', 22, 'A'),
('Bob', 20, 'B'),
('Charlie', 19, 'C'),
('David', 25, 'A'),
('Eve', 18, 'B'),
('Frank', 22, 'A'),
('George', 21, 'C'),
('Hannah', 23, 'A'),
('Ian', 20, 'B'),
('Jessica', 22, 'C'),
('Kevin', 19, 'A'),
('Liam', 18, 'B'),
('Mia', 24, 'C'),
('Nina', 21, 'A'),
('Olivia', 25, 'B'),																																			
('Paul', 23, 'A'),
('Quinn', 22, 'C'),
('Rachel', 24, 'B');


CREATE TABLE employees (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    department VARCHAR(100),
    salary DECIMAL(10, 2)
);


INSERT INTO employees (name, department, salary) VALUES
('John', 'HR', 55000.00),
('Sarah', 'IT', 60000.00),
('Mike', 'HR', 52000.00),
('Linda', 'Finance', 65000.00),
('James', 'IT', 70000.00),
('Emma', 'Finance', 68000.00),
('Robert', 'IT', 72000.00),
('Sophia', 'HR', 48000.00),
('Alice', 'Finance', 62000.00),
('Bob', 'HR', 50000.00),
('Charlie', 'IT', 71000.00),
('David', 'Finance', 67000.00),
('Emily', 'IT', 75000.00),
('Frank', 'Finance', 64000.00),
('Grace', 'HR', 51000.00),
('Henry', 'IT', 79000.00),
('Isabella', 'Finance', 70000.00),
('Jack', 'HR', 56000.00),
('Karen', 'IT', 85000.00),
('Leo', 'Finance', 72000.00);


