response = []
with open('./Food_Vendor_Locations.csv') as crime_csv:
    lines = []
    for line in crime_csv.readlines()[1:]:
        lines.append(line.split(','))
    
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            lines[i][j] = lines[i][j].replace(')"', '').replace('(', '')
        response.append({
            'X' : lines[i][-4],
            'Y' : lines[i][-5]
        })
    print(response)
