CREATE VIEW
	v_employees
AS
SELECT
	*
FROM
	employees
ORDER BY
	salary DESC
LIMIT 1
;

SELECT
	*
FROM
	v_employees
;