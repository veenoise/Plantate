from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, William</p>"


@app.route("/your-plants")
def plant_collection():
    return render_template('plants.html')

@app.route("/specific-plant")
def specific():
    return render_template('plant-specific.html')