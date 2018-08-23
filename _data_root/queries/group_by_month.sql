SELECT to_char(time, 'month') AS month, to_char(time, 'MM') AS mm, count(*)
	FROM bonn.parking_fines
	GROUP BY 1,2
	ORDER BY mm ASC