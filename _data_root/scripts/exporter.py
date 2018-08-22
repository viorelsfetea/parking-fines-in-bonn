import psycopg2
import json
from decimal import Decimal

class CustomJsonEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Decimal):
            return float(obj)
        return super(CustomJsonEncoder, self).default(obj)

conn = psycopg2.connect("dbname=bonn user=viorel")
cur = conn.cursor()
file = "../data/export.json"

cur.execute("""SELECT address, COUNT(*) as total, SUM(amount) as money_total, round(AVG(amount), 2) as money_average
	FROM bonn.parking_fines
GROUP BY 1
ORDER BY total DESC""")

results = {"data": cur.fetchall()}
with open(file, 'w') as outfile:
    json.dump(results, outfile, cls=CustomJsonEncoder, ensure_ascii=False)

cur.close()
conn.close()