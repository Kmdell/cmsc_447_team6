from flask import Flask, request, make_response
from flask_cors import CORS
from flask_json import FlaskJSON
import csv

app = Flask(__name__)
CORS(app)
FlaskJSON(app)

endpoints = ["", "landmarks", "covid", "night_out", "crime"]

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
                    'increment' : increments[j][i]
                }
            covid_dates.append(temp)
        return covid_dates

def index(endpoint):
    if request.method == "GET":
        if endpoint == "":
            return "Hello from server"
        elif endpoint == "landmarks":
            # temp function until database is created
            return landmarks()
        elif endpoint == "covid":
            return covid()
        else:
            return endpoint

for endpoint in endpoints:
    app.add_url_rule("/" + endpoint, view_func=index, methods=["GET"], defaults={'endpoint': endpoint})