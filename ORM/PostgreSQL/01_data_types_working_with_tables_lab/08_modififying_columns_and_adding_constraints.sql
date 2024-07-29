ALTER TABLE employees
--RENAME COLUMN "name" TO first_name,
ALTER COLUMN first_name TYPE VARCHAR(30),
ALTER COLUMN first_name SET not null,
ADD COLUMN last_name VARCHAR(50) NOT NULL,
ADD COLUMN hiring_date date DEFAULT '2023-01-01';