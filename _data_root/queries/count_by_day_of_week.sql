select to_char(time, 'day') as day, extract(dow from time) as date_part,
       count(*) as "total"
from bonn.parking_fines
group by 1, 2
ORDER BY date_part ASC