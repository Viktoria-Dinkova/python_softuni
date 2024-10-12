SELECT
	t.town_id, 
	name, 
	address_text
FROM
	public.addresses AS a
	JOIN public.towns AS t ON t.town_id = a.town_id
WHERE
	name in ('San Francisco', 'Sofia', 'Carnation')
ORDER BY
	town_id,  
	address_text
;	