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
    daysSince4_11 = 0
    for count in row2[2:]:
    #rowArr = row2.split(',')
        exe = ("INSERT INTO covid_case_count VALUES ('%s','%s','%s','%s')" % (row2[1].replace("'","")+str(daysSince4_11),row2[1].replace("'",""),daysSince4_11,count))
        #print(exe)
        cur.execute(exe)
        daysSince4_11 += 1
print("done")
con.commit()
con.close()