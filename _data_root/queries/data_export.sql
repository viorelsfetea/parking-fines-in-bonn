SELECT address, COUNT(*) as total, SUM(amount) as money_total, round(AVG(amount), 2) as money_average
	FROM bonn.parking_fines
GROUP BY 1
ORDER BY total DESC