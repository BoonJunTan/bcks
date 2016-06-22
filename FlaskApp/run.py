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

@app.route('/js/<path:path>')
def send_js(path):
    return send_from_directory('js', path)


@app.route('/css/<path:path>')
def send_css(path):
    return send_from_directory('css', path)


@app.route('/img/<path:path>')
def send_img(path):
    return send_from_directory('img', path)


@app.route('/fonts/<path:path>')
def send_font(path):
    return send_from_directory('fonts', path)