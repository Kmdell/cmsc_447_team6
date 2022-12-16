import sqlite3
con = sqlite3.connect('dashboard.db')
cur = con.cursor()

covid_dates = []
with open('./baltimore_city_zip_code_totals.csv') as csv_file:
    totals = []
    increments = []
    for line in csv_file.readlines():
        totals.append(line.split(',')[1:])
    
    for i in range(1, len(totals)):
        for j in range(1, len(totals[i])):
            if totals[i][j] == '':
                totals[i][j] = 0
            totals[i][j] = int(totals[i][j])
    
    for i in range(1, len(totals[0])):
        totals[0][i] = totals[0][i].strip('total').strip('\n').replace('_', '/')

    increments.append(totals[:1])
    for i in range(len(totals) - 1):
        increments.append([])
    for i in range(1, len(totals)):
        for j in range(len(totals[i])):
            if j == 0:
                increments[i].append(totals[i][0])
            elif j == 1:
                increments[i].append(totals[i][j] - 0)
            else:
                increments[i].append(totals[i][j] - totals[i][j - 1])
    
    input = []
    k = 0
    for i in range(1, len(totals[0])):
        for j in range(1, len(totals)):
            input.append((str(k), str(totals[j][0]), str(totals[0][i]), str(totals[j][i]), str(increments[j][i])))
            k += 1
        
    cur.executemany("INSERT INTO covid VALUES(?, ?, ?, ?, ?)", input)
    con.commit()
    
