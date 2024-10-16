SELECT
	b.booking_id,
	a."name" AS apartment_owner,
	a.apartment_id,
	CONCAT(first_name, ' ', last_name) AS customer_name
FROM
	public.bookings AS b 
	FULL JOIN public.customers AS c ON c.customer_id = b.customer_id
	FULL JOIN public.apartments AS a ON a.booking_id = b.booking_id
ORDER BY
	"booking_id", 
	"apartment_owner" ,
	"customer_name"
;