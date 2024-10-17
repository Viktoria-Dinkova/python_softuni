SELECT
	b.booking_id,
	b.apartment_id,
	c.companion_full_name
FROM
	public.bookings AS b 
	JOIN public.customers AS c USING(customer_id)
WHERE
	b.apartment_id IS NULL
;