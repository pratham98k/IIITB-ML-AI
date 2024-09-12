show tables;

describe students;

describe employees;

-- 1.1 The SELECT statement is used to choose the columns you want to display from a table.
-- This query retrieves the name and age columns from the students table.
select name, age
from students;

-- 1.2  WHERE (Filtering Rows) You use WHERE to filter rows based on a condition.
-- This query returns only the students whose age is greater than 18.
select name, age
from students;
where age >= 18;

-- 1.3 GROUP BY (Grouping Data) GROUP BY groups rows with the same values in specified columns. It's often used with aggregate functions.
-- This query counts the number of employees in each department.
select department, count(*)
from employees
group by department;

-- 1.4 HAVING (Filtering Groups) HAVING filters groups, similar to how WHERE filters rows.
-- This query returns only the departments with more than 5 employees.
select department, count(*)
from employees
group by department
having count(*) > 5;

-- 1.5 ORDER BY (Sorting Results) ORDER BY sorts the results, either ascending (default) or descending.
-- This query sorts students by age in descending order.
select name, age 
from students
order by age desc;

-- 1.6 LIMIT (Restricting the Number of Rows) LIMIT restricts the number of rows returned.
-- This query retrieves the 3 oldest students.

select name, age
from students
order by age desc
limit 3;

-- 2. Operators, Aggregate Functions, and Expressions

-- 2.1 Relational and Logical Operators
-- =: Equal to
-- >: Greater than
-- <: Less than
-- AND, OR: Combine conditions.

-- This query retrieves students older than 18 with an 'A' grade.

select name, age
from students
where age > 18 and grade = "A";

-- 2.2 Arithmetic Operators You can use basic math operations in SQL queries.
-- This query increases each employee’s salary by 10% and returns the new value.

select name, salary * 1.1 as new_salary
from employees;


-- 2.3 Aggregate Functions
-- COUNT(): Counts the rows.
-- SUM(): Adds values.
-- AVG(): Finds the average.
-- MIN(): Finds the minimum.
-- MAX(): Finds the maximum.
-- This query calculates the average salary in the HR department.

select avg(salary)
from (employees)
where department = 'HR';


-- 2.4 Regular Expressions
-- In SQL, you can use the LIKE keyword with wildcards (%, _) for pattern matching.
-- This query returns students whose name starts with 'A'.
-- if we use '%A% this will return all values with a in name
select name
from students
where name like 'A%';

--  3. Nested Queries and CTEs
-- 3.1 Nested Queries (Subqueries)
-- A nested query is a query inside another query.
-- This query finds the student(s) with the maximum age.

select name
from students
where age = (select max(age) from students);


-- 3.2 Common Table Expressions (CTEs)
-- CTEs are used to define a temporary result set that can be referenced within a SELECT, INSERT, or UPDATE.
-- Here, the WITH statement defines a CTE called AverageSalaries which calculates the average salary per department. Then, the main query selects departments where the average salary is above $50,000.

WITH AverageSalaries AS (
  SELECT department, AVG(salary) AS avg_salary
  FROM employees
  GROUP BY department
)
SELECT department 
FROM AverageSalaries 
WHERE avg_salary > 50000;

-- 4. Views and Their Advantages Over CTEs

-- 4.1 Views
-- A view is a saved SQL query that can be reused like a table.
create view high_salary_employees as
select name salary
from employees
where salary > 60000;

-- You can now query high_salary_employees like this:

SELECT * FROM high_salary_employees;

-- 4.2 Advantages of Views Over CTEs
-- Persistence: Views are saved in the database and can be reused anytime, while CTEs are temporary and exist only for the duration of the query.
-- Security: Views can hide complex joins or specific columns, restricting user access.
-- Optimization: Views are precompiled, which can improve performance.


