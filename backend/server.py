from flask import Flask, request, make_response
from flask_cors import CORS
from flask_json import FlaskJSON

app = Flask(__name__)
CORS(app)
FlaskJSON(app)

endpoints = ["landmarks", "covid", "night_out", "crime"]

def index(endpoint):
    if request.method == "GET":
        return endpoint

for endpoint in endpoints:
    app.add_url_rule("/" + endpoint, view_func=index, methods=["GET"], defaults={'endpoint': endpoint})