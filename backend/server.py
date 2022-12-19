"""
Name: Kyle Dell
CMSC447
"""
from flask import Flask, request, make_response
from flask_cors import CORS
from flask_json import FlaskJSON
import sqlite3
import threading
import json

app = Flask(__name__)
CORS(app)
FlaskJSON(app)
con = sqlite3.connect('../data/dashboard.db', check_same_thread=False)
cur = con.cursor()
endpoints = ["", "landmarks", "zipcodes", "covid", "crime", 'food_vendor']
lock = threading.Lock()

def landmarks():
    landmarks = []
    lock.acquire()
    resp = cur.execute("SELECT * FROM loc")
    for i in resp.fetchall():
        landmarks.append({'ID': int(i[0]), 'name': i[1], 'x': float(i[2]) / 111317.293, 'y': float(i[3]) / 121234.446})
    lock.release()
    return landmarks

def covid():
    covid = {}
    covid_dates = {}
    lock.acquire()
    resp = cur.execute("SELECT * FROM covid")
    old_date = ''
    new_date = ''
    for i in resp.fetchall():
        split_date = i[2].split('/')

        new_date = split_date[2] + '/' + split_date[0] + '/' + split_date[1]
        if old_date == '' or old_date == new_date:
            covid[i[1]] = {'ID': int(i[0]), 'total': int(i[3]), 'change': int(i[4])}
            old_date = new_date[:]
        else:
            covid_dates[old_date] = covid
            covid = {}
            covid[i[1]] = {'ID': int(i[0]), 'total': int(i[3]), 'change': int(i[4])}
            old_date = new_date[:]
    lock.release()
    return covid_dates

def zipcode():
    with open('../data/zipcode_geoJSON.json') as geojson_file:
        gjson = json.load(geojson_file)
    return gjson

def crime():
    crime = []
    crime_dates = {}
    lock.acquire()
    resp = cur.execute("SELECT * FROM crime")
    old_date = ''
    new_date = ''
    for i in resp.fetchall():
        new_date = i[3].split(' ')[0]
        if old_date == '' or old_date == new_date:
            if i[1] != '' and i[2] != '':
                crime.append({'ID': int(i[0]), 'x': float(i[1]), 'y': float(i[2]), 'location': i[4], 'type': i[5]})
                old_date = new_date[:]
        else:
            if i[1] != '' and i[2] != '':
                crime_dates[old_date] = crime
                crime = []
                crime.append({'ID': int(i[0]), 'x': float(i[1]), 'y': float(i[2]), 'location': i[4], 'type': i[5]})
                old_date = new_date[:]
    lock.release()
    return crime_dates
    
def food():
    response = []
    lock.acquire()
    resp = cur.execute("SELECT * FROM restaurant")
    for i in resp.fetchall():
        response.append({'ID': int(i[0]), 'address': i[1], 'location': i[2], 'zip_code': i[3], 'items_sold': i[4]})
    lock.release()
    return response

def index(endpoint):
    if request.method == "GET":
        if endpoint == "":
            return "Hello from server"
        elif endpoint == "landmarks":
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