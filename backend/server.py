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

def index(endpoint):
    if request.method == "GET":
        if endpoint == "":
            return "Hello from server"
        elif endpoint == "landmarks":
            # temp function until database is created
            return landmarks()
        else:
            return endpoint

for endpoint in endpoints:
    app.add_url_rule("/" + endpoint, view_func=index, methods=["GET"], defaults={'endpoint': endpoint})