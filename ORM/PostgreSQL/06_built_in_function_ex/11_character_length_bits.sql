SELECT
	CONCAT(mountain_range, ' ',peak_name) AS "mountain_information",
	LENGTH(CONCAT(mountain_range, ' ',peak_name))  AS "characters_length",
	BIT_LENGTH(CONCAT(mountain_range, ' ',peak_name))  AS "bits_of_a_tring"
FROM
	peaks AS p
	INNER join mountains AS m on p.mountain_id = m.id
;