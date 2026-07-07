from flask import Flask, render_template, jsonify, request
from dotenv import load_dotenv
from markupsafe import escape
import os

app = Flask(__name__)

@app.route ("/")
def main ():
    return render_template("index.html")

@app.route ("/send")
def send ():
    return render_template("send.html")

@app.route ("/process-data", methods = ["POST"])
def process_data():
    firstname = request.form.get("firstname")
    age = int(request.form.get("age"))

    return f"<p> Hello {escape(firstname)}, You are {age} years old. </p>"