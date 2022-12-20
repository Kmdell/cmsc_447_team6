import csv
import sqlite3

DATABASE_FILE = "dashboard.db"

con = sqlite3.connect(DATABASE_FILE)
cur = con.cursor()

filename = "Food_Vendor_Locations.csv"
fields = []
rows = []

with open(filename, 'r') as csvfile:
	csvreader = csv.reader(csvfile)
	
	fields = next(csvreader)

	for row in csvreader:
		rows.append(row)
for row2 in rows:
    #print(row2)
    #rowArr = row2.split(',')
    exe = ("INSERT INTO restaurant VALUES ('%s','%s','%s','%s','%s')" % (row2[0].replace("'",""),row2[4].replace("'",""),row2[8].replace("'","").replace("(","").replace(")",""),row2[11].replace("'",""),row2[5].replace("'","")))
    print(exe)
    cur.execute(exe)
print("done")
con.commit()
con.close()