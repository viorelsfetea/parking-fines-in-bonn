import psycopg2
import json

conn = psycopg2.connect("dbname=bonn user=viorel")
cur = conn.cursor()
file = "../data/count_by_day_of_the_week.json"

cur.execute("select to_char(time, 'day') as day, extract(dow from time) as date_part, count(*) as total from bonn.parking_fines group by 1, 2 ORDER BY date_part ASC")

results = []

for result in cur.fetchall():
	results.append([result[0].strip(), result[2]])

sunday = results.pop(0)
results.append(sunday) #sunday at the end

with open(file, 'w') as outfile:
    json.dump(results, outfile)

cur.close()
conn.close()