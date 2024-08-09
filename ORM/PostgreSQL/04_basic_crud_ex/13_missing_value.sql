SELECT 
	id,
	"first_name",
	"last_name"
FROM
	employees
WHERE
	middle_name IS NULL
FETCH FIRST 3 ROW ONLY
;