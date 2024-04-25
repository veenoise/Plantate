from flask import Flask, render_template, jsonify, request
from gemini import gemini_chat_api_request

app = Flask(__name__)

@app.route("/")
def index():
    return "<p>Hello, William</p>"


@app.route("/home")
def home():
    return render_template('home.html')


@app.route("/your-plants")
def plant_collection():
    return render_template('plants.html')


@app.route("/specific-plant")
def specific():
    return render_template('plant-specific.html')


@app.route("/gemini-doctor")
def gemini_doctor():
    return render_template('gemini-doctor.html')


@app.route("/login")
def login():
    return render_template('login.html')


@app.route('/api/plant-doctor')
def api_test():
    message = request.args.get('msg')
    return f'{gemini_chat_api_request(message)}'
