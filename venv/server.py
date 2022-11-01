from crypt import methods
from email.policy import default
from urllib import request
from flask import Flask
from flask_cors import CORS
from flask_json import FlaskJSON

app = Flask(__name__)
CORS(app)
FlaskJSON(app)

endpoints = ["landmarks", "covid", "night_out"]

def index(endpoint):
    if request.method == "GET":
        return endpoint

for endpoint in endpoints:
    app.add_url_rule("/" + endpoint, view_func=index, methods=["GET"], defaults={'endpoint': endpoint})