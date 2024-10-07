SELECT 
	r.start_point, 
	r.end_point, 
	r.leader_id,
	CONCAT(c.first_name, ' ', c.last_name) AS leader_name
FROM 
	public.routes AS r
	JOIN public.campers c ON c.id = r.leader_id
;