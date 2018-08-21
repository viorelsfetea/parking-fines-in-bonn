SELECT AVG(test) FROM (select date_trunc('day', time), COUNT(*) AS test
from bonn.parking_fines
WHERE extract(dow from time) = 0
GROUP BY 1) T