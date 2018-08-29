from datetime import date, datetime, timedelta

import psycopg2
import json

conn = psycopg2.connect("dbname=bonn user=viorel")
cur = conn.cursor()
file = "../data/count_by_time_period.json"


def datetime_range(start, end, delta):
    current = start
    if not isinstance(delta, timedelta):
        delta = timedelta(**delta)
    while current <= end:
        yield current
        current += delta

start = datetime(2015,1,1)
end = datetime(2015,1,2)

times = []
results = []

for dt in datetime_range(start, end, {'days': 0, 'hours': 0, 'minutes': 30}):
    times.append(dt.strftime("%H:%M"))

for index in range(len(times) - 1):
	interval = (times[index], times[index + 1])
	key = "{}-{}".format(interval[0], interval[1])

	cur.execute("""
		SELECT COUNT(*)
		FROM bonn.parking_fines
		WHERE time::time between time %s and %s
	""", interval)

	results.append([key, cur.fetchone()[0]])


with open(file, 'w') as outfile:
    json.dump(results, outfile)

cur.close()
conn.close()