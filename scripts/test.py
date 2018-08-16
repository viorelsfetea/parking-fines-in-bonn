
import csv
from dateutil.parser import parse

file = "../_data/ParkverstoesseBonn2017OpenData_raw.csv"

with open(file, newline='', encoding="utf-8") as csvfile:
    reader = csv.reader(csvfile, delimiter=';', quotechar='"')
    for row in reader:
        date = row[0]
        time = row[1]
        minutes = time[-2:]
        if(len(time) < 2):
        	time = "00:0" + minutes
        elif(len(time) == 2):
        	time = "00:" + minutes
        else:	
        	time = time[:-2] + ":" + minutes

        complete_date = date + " " + time
        print(parse(complete_date))