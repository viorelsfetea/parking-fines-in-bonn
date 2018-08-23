import psycopg2
import json

conn = psycopg2.connect("dbname=bonn user=viorel")
cur = conn.cursor()
file = "../data/monthly_statistics.json"

cur.execute("""SELECT to_char(time, 'month') AS month, to_char(time, 'MM') AS mm, count(*)
    FROM bonn.parking_fines
    GROUP BY 1,2
    ORDER BY mm ASC
""")

results = []

for result in cur.fetchall():
    results.append([result[0].strip(), result[2]])

with open(file, 'w') as outfile:
    json.dump(results, outfile)

cur.close()
conn.close()