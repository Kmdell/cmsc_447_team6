from flask import Flask, request, make_response
from flask_cors import CORS
from flask_json import FlaskJSON
import csv
import geojson

app = Flask(__name__)
CORS(app)
FlaskJSON(app)

endpoints = ["", "landmarks", "zipcodes", "covid", "crime", 'food_vendor']

def landmarks():
    landmarks = []
    with open('../data/locations.csv', 'r') as csv_file:
        lines = csv_file.readlines()
        for i in range(len(lines)):
            if i > 0:
                line = lines[i].split("|")
                print("0: " + line[0] + " 1: " + line[1] + " 2: " + line[2] + " 3: " + line[3])
                landmarks.append({
                    "ID" : int(line[0]),
                    "Name" : line[1],
                    "X" : float(line[2]),
                    "Y" : float(line[3])
                })
    csv_file.close()
    return landmarks

def covid():
    covid_dates = []
    with open('../data/baltimore_city_zip_code_totals.csv') as csv_file:
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
        return covid_dates

def zipcode():
    with open('../data/md_maryland_zip_codes_geo.min.json') as geojson_file:
        gjson = geojson.load(geojson_file)
    return gjson

def crime():
    response = []
    with open('../data/Part_1_Crime_Data_.csv') as crime_csv:
        lines = []
        for line in crime_csv.readlines()[1:]:
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
    return response
    
def food():
    response = []
    with open('../data/Food_Vendor_Locations.csv') as crime_csv:
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
    return response

def index(endpoint):
    if request.method == "GET":
        if endpoint == "":
            return "Hello from server"
        elif endpoint == "landmarks":
            # temp function until database is created
            return landmarks()
        elif endpoint == "covid":
            return covid()
        elif endpoint == "zipcodes":
            return zipcode()   
        elif endpoint == "crime":
            return crime()
        elif endpoint == "food_vendor":
            return food()
        else:
            return endpoint

for endpoint in endpoints:
    app.add_url_rule("/" + endpoint, view_func=index, methods=["GET"], defaults={'endpoint': endpoint})