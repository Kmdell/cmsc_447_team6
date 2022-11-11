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
        totals[0][i] = totals[0][i].strip('total').strip('\n')

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

    for i in range(1, len(totals[0])):
        temp = {}
        temp['date'] = totals[0][i]
        for j in range(1, len(totals)):
            temp[totals[j][0]] = {
                'total' : totals[j][i],
                'change' : increments[j][i]
            }
        covid_dates.append(temp)
    
    print(covid_dates, len(covid_dates))
    
