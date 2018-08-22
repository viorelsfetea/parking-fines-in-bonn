import csv
from postal.parser import parse_address

file = "../data/ParkverstoesseBonn2017OpenData_raw.csv"

i = 0

with open(file, encoding='utf-8') as csvfile:
	reader = csv.reader(csvfile, delimiter=';', quotechar='"')
	
	for row in reader:
		i += 1
		
		address = row[2].replace("Bonn, ", "").replace("Bonn , ", "").replace("Straße", "str.")
		print(address)
		print(parse_address(address))
		if i == 1000:
			break
