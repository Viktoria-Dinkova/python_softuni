SELECT
	b.booking_id,
	c.first_name,
FROM
	public.bookings AS b 
	CROSS JOIN public.customers AS c ON c.customer_id = b.customer_id
ORDER BY
		c.first_name
;