CREATE FUNCTION fn_count_employees_by_town(town_name VARCHAR(20))
RETURNS INT
AS
$$
DECLARE employees_count INT;

BEGIN
	SELECT
			COUNT(e.employee_id) INTO employees_count
	FROM
		employees AS e
		JOIN addresses AS a ON a.address_id = e.address_id
		JOIN towns AS t ON t.town_id = a.town_id
	WHERE
		t.name = TRIM(town_name);
	
	RETURN employees_count;
		
END
$$
LANGUAGE plpgsql;

