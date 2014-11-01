
import csv
import json

csvfilename = 'GpsFilePoints.csv'
jsonfilename = csvfilename.split('.')[0] + '.json'

csvfile = open('GpsFilePoints.csv', 'r')
jsonfile = open('GpsFilePoints.json','w')

fieldnames = ("UserID","FieldID","PointID","Lat","Lng","Ele","Time","Course","Hdop","Sat","Filtered")

reader = csv.DictReader( csvfile, fieldnames)
for row in reader:
    json.dump(row, jsonfile)
    jsonfile.write('\n')

