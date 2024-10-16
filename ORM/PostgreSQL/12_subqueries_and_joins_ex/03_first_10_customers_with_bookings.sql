SELECT
	b.booking_id,
	CAST(b.starts_at AS DATE),
	b.apartment_id,
	CONCAT(first_name, ' ', last_name) AS customer_name
FROM
	public.bookings AS b 
	RIGHT JOIN public.customers AS c ON c.customer_id = b.customer_id
ORDER BY
	CONCAT(first_name, ' ', last_name)
LIMIT 10
;