import csv
import sqlite3

DATABASE_FILE = "dashboard.db"

con = sqlite3.connect(DATABASE_FILE)
cur = con.cursor()

filename = "locations.csv"
fields = []
rows = []

with open(filename, 'r') as csvfile:
	csvreader = csv.reader(csvfile)
	
	fields = next(csvreader)

	for row in csvreader:
		rows.append(row)
for row1 in rows:
    #print(row1)
    row2 = row1[0].split('|')
    #print(row2)
    if len(row2)==4:
        exe = ("INSERT INTO loc VALUES ('%s','%s','%s','%s')" % (row2[0].replace("'",""),row2[1].replace("'",""),row2[2].replace("'",""),row2[3].replace("'","")))
        cur.execute(exe)
print("done")
con.commit()
con.close()