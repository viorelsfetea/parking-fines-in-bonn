select count(*)
from bonn.parking_fines
where time::time between time '00:00:00' and '00:30:00'