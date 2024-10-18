SELECT
	COUNT(b.booking_id)
FROM
	public.bookings AS b 
	JOIN public.customers AS c USING(customer_id)
WHERE
	TRIM(c.last_name) = 'Hahn'
;