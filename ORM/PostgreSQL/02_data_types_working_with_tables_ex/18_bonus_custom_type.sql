CREATE TYPE address AS (
	street VARCHAR(50),
	city VARCHAR(50),
	postalCode CHAR(4)
);

CREATE TABLE customers (
	id SERIAL PRIMARY KEY,
	customer_name VARCHAR(150),
	customer_address address
);

INSERT INTO 
	customers(customer_name, customer_address)
VALUES
	('PESHO', ('some street2', 'sofia', '7823'));
	
SELECT 
	(customer_address).street
FROM customers;