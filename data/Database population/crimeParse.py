import csv
import sqlite3

DATABASE_FILE = "dashboard.db"

con = sqlite3.connect(DATABASE_FILE)
cur = con.cursor()

filename = "Part_1_Crime_Data_.csv"
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
    exe = ("INSERT INTO crime VALUES ('%s','%s','%s','%s','%s','%s')" % (row2[2].replace("'",""),row2[17].replace("'",""),row2[16].replace("'",""),row2[3].replace("'",""),row2[5].replace("'",""),row2[6].replace("'","")))
    #print(exe)
    cur.execute(exe)
print("done")
con.commit()
con.close()