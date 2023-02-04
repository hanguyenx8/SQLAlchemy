from flask import render_template, request
from saleapp import app
import os



@app.route("/")
def home():
    users = [{
        "name": "Nguyen Van A",
        "email": "nva@gmail.com"
    }]
    return users


#app.run()