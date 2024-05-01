from flask import Flask, render_template, jsonify, request, session, redirect, url_for
from gemini import gemini_chat_api_request
from dotenv import load_dotenv
from os import getenv
from hashlib import pbkdf2_hmac
from cs50 import SQL
db = SQL("sqlite:///dbPlantate.sqlite")

ITERATION = 600_000
SALT = getenv('SALT_HASH').encode('utf-8')

load_dotenv()

app = Flask(__name__)

app.secret_key = getenv('SESSION_KEY').encode('utf-8')

def check_session():
    if session:
        return True
    return False

@app.route("/")
def index():
    is_authenticated = check_session()

    return render_template('home.html', is_authenticated = is_authenticated)

@app.route("/home")
def home():
    return redirect(url_for('index'))

@app.route("/your-plants", methods=['GET', 'POST'])
def plant_collection():
    if request.method == 'POST':
        json_data = request.json
        print(json_data)
    return render_template('plants.html')

@app.route("/specific-plant")
def specific():
    return render_template('plant-specific.html')


@app.route("/gemini-doctor")
def gemini_doctor():
    return render_template('gemini-doctor.html')

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for('home'))

@app.route("/login", methods=['GET', 'POST'])
def login():
    if session:
        return redirect(url_for('home'))

    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        
        row = db.execute("SELECT * FROM tblUser WHERE strEmail = ?", email)

        if len(row) != 0:
            password = pbkdf2_hmac('sha256', password.encode('utf-8'), SALT * 2, ITERATION).hex()
            row = db.execute("SELECT strPassword FROM tblUser WHERE strEmail = ?", email)

            if len(row) != 0 and password == row[0]['strPassword']:
                session['user'] = email
                return redirect(url_for('home'))
            
            return render_template('login.html', invalid_message = 'Uh oh! Email or password incorrect.')

        return render_template('login.html', invalid_message = 'Uh oh! Email or password incorrect.')
    
    return render_template('login.html')

@app.route("/signup", methods=['GET', 'POST'])
def signup():
    if session:
        return redirect(url_for('home'))
    
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        row = db.execute("SELECT * FROM tblUser WHERE strEmail = ?", email)

        if len(row) == 0:
            password = pbkdf2_hmac('sha256', password.encode('utf-8'), SALT * 2, ITERATION).hex()
            db.execute("INSERT INTO tblUser (strEmail, strPassword) VALUES (?, ?)", email, password)
            session['user'] = email

        else:
            return render_template('signup.html', invalid_message='Uh oh! Email address already taken.')
        return redirect(url_for('home'))
    return render_template('signup.html')

@app.route('/api/plant-doctor')
def api_test():
    message = request.args.get('msg')
    return f'{gemini_chat_api_request(message)}'
