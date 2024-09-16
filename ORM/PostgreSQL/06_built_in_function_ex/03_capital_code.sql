ALTER TABLE 
	countries
ADD COLUMN 
	captial_code CHAR(2)
;

UPDATE 
	countries
SET
	captial_code = SUBSTRING(capital, 1, 2)
;

SELECT
	*
FROM
	countries
ORDER BY
	id
;
	