import csv
import psycopg2
from dateutil.parser import parse


file = "../data/ParkverstoesseBonn2017OpenData_raw.csv"
conn = psycopg2.connect("dbname=bonn user=viorel")
cur = conn.cursor()

def normalize_time(time):
	chars = len(time)

	if(chars == 1):
		time = "0" + time + "00" #9 to 0900
	if(chars == 2):
		time = "0" + time[0] + "0" + time[1] #48 to 0408
	elif(chars == 3):
		time = "0" + time; #948 to 0948

	minutes = time[2:]
	time = time[:-2] + ":" + minutes

	return time

with open(file, encoding='utf-8') as csvfile:
	reader = csv.reader(csvfile, delimiter=';', quotechar='"')
	
	for row in reader:
		time = normalize_time(row[1])
		date = parse(row[0] + " " + time, dayfirst=True)
		
		cur.execute("INSERT INTO bonn.parking_fines (time, address, amount, vehicle_type) VALUES (%s, %s, %s, %s)",(date, row[2], int(row[4]), row[5]))

conn.commit()
cur.close()
conn.close()
