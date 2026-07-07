import os

from flask import Flask, render_template, jsonify
from dotenv import load_dotenv
import os

app = Flask(__name__)

@app.route ("/")
def main ():
    return render_template("index.html")
