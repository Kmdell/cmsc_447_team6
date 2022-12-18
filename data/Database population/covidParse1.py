import csv
import sqlite3

DATABASE_FILE = "dashboard.db"

con = sqlite3.connect(DATABASE_FILE)
cur = con.cursor()

filename = "MDCOVID19_MASTER_ZIP_CODE_CASES.csv"
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
    exe = ("INSERT INTO covid VALUES ('%s')" % (row2[1].replace("'","")))
    #print(exe)
    cur.execute(exe)
print("done")
con.commit()
con.close()