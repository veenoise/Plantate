from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, William</p>"


@app.route("/plants")
def plant_collection():
    return render_template('plants.html')