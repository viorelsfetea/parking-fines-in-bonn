import psycopg2
import json

conn = psycopg2.connect("dbname=bonn user=viorel")
cur = conn.cursor()
file = "../_data/daily_statistics.json"

cur.execute("SELECT *, to_char(items.day, 'day') day_name FROM (SELECT date_trunc('day', bonn.parking_fines.time) \"day\", count(*) FROM bonn.parking_fines group by 1 ORDER BY 1) AS items")

results = {}

for result in cur.fetchall():
	key = "{} ({})".format(result[0].strftime("%d %B"), result[2].strip())
	results[key] = result[1]

with open(file, 'w') as outfile:
    json.dump(results, outfile)

cur.close()
conn.close()