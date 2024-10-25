CREATE PROCEDURE sp_increase_salaries(department_name VARCHAR)
AS
$$
BEGIN
	UPDATE
		employees
	SET 
		salary = e.salary * 1.05	
	FROM
			employees AS e
			JOIN departments AS d USING(department_id)
	WHERE
			employees.employee_id = e.employee_id
			AND TRIM(d.name) = TRIM(department_name);

END;
$$
LANGUAGE plpgsql;