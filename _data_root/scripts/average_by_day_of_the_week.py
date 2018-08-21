import psycopg2
import json
from collections import OrderedDict

conn = psycopg2.connect("dbname=bonn user=viorel")
cur = conn.cursor()
file = "../data/average_by_day_of_the_week.json"

results = []

days = OrderedDict()
days[1] = "Monday";
days[2] = "Tuesday";
days[3] = "Wednesday";
days[4] = "Thursday";
days[5] = "Friday";
days[6] = "Saturday";
days[0] = "Sunday";

for day in days:
    print(day)
    cur.execute("""SELECT AVG(total) 
        FROM (SELECT date_trunc('day', time) as ss, COUNT(*) AS total 
                FROM bonn.parking_fines WHERE extract(dow from time) = %s GROUP BY 1) T
    """, (day,))
    results.append([days[day], round(cur.fetchone()[0])])


with open(file, 'w') as outfile:
    json.dump(results, outfile)

cur.close()
conn.close()