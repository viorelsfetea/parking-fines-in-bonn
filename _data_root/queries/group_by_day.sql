SELECT *, to_char(items.day, 'day') day_name 
FROM (
	SELECT date_trunc('day', bonn.parking_fines.time) "day", count(*) 
		FROM bonn.parking_fines 
		group by 1 ORDER BY 1
	) AS items