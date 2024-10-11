CREATE TABLE customers
	(
		id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
		customer_name VARCHAR(30)

	)
;

CREATE TABLE contacts
	(
		id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
		contact_name VARCHAR(30),
		phone CHAR(14), 
		email VARCHAR(50),
		customer_id INT,
		
		CONSTRAINT fk_contacts_customers
			FOREIGN KEY (customer_id)
				REFERENCES customers(id)
					ON DELETE SET NULL
					ON UPDATE CASCADE
	)
;



INSERT INTO 
	public.customers (customer_name)
VALUES
	('BlueBird Inc'),
	('Dolphin LLC')
;
	
INSERT INTO 
	public.contacts(contact_name,	phone,	email, customer_id)
VALUES
	('John Doe',	'(408)-111-1234',	'john.doe@bluebird.dev',	1),
	('Jane Doe',	'(408)-111-1235',	'jane.doe@bluebird.dev',	1),
	('David Wright',	'(408)-222-1234',	'david.wright@dolphin.dev',	2)
;

DELETE FROM
	customers
WHERE
	id = 1
;