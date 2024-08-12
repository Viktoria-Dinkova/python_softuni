CREATE VIEW view_addresses
AS 
SELECT
	first_name || ' ' || last_name AS full_name,
	department_id,
	number || ' ' || street AS address
FROM	
	public.employees AS e
	INNER JOIN public.addresses AS a ON e.address_id = a.id

;