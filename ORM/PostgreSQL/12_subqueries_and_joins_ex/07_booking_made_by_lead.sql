SELECT
	b.apartment_id,
	b.booked_for,
	c.first_name,
	c.country
FROM
	public.bookings AS b 
	JOIN public.customers AS c USING(customer_id)
WHERE
	c.job_type LIKE '%Lead%'
;