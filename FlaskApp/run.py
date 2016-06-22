from flask import Flask, render_template, send_from_directory, request
import http.client, urllib.request, urllib.parse, urllib.error, base64, requests
import json

app = Flask(__name__, static_url_path='')

@app.route("/")
def index():
    print("in index")
    return render_template('index.html', test_context="this is a string from the OTHER side!")

@app.route("/product.html")
def product():
    print("in index")
return render_template('product.html', test_context="this is a string from the OTHER side!")