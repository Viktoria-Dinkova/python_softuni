SELECT
	c.id AS driver_id,
	v.vehicle_type,
	CONCAT(c.first_name, ' ', c.last_name) AS driver_name 
	
FROM
	public.campers AS c
	JOIN public.vehicles v ON v.driver_id = c.id
;