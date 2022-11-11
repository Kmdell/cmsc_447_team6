response = []
with open('./Part_1_Crime_Data_.csv') as crime_csv:
    lines = []
    i = 0
    for line in crime_csv.readlines()[1:]:
        print(i, end='')
        i += 1
        lines.append(line.split(',')[:4] + [line.split(',')[6]])
        

    for i in range(len(lines)):
        lines[i][3] = lines[i][3].split()[0].replace('/', '_')

    for line in lines:
        response.append({
            'date' : line[3],
            'X' : line[0],
            'Y' : line[1],
            'Description' : line[4]
        })
    
print(response)