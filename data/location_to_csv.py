import csv

txt_file = open('./locations.txt', 'r')
csv_file = open('./locations.csv', 'w')

header = ["name", "x", "y"]
writer = csv.writer(csv_file)
writer.writerow(header)
lines = txt_file.readlines()
data = []
line_data = []
for line in lines:
	if 'name:' in line:
		line_data.append(line[6:].strip())
	if 'X:' in line:
		line_data.append(line[3:].strip())
	if 'Y:' in line:
		line_data.append(line[3:].strip())
	if len(line_data) == 3:
		data.append(line_data)
		line_data = []

for line in data:
	writer.writerow(line)
