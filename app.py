from flask import Flask, render_template, jsonify, request, session, redirect, url_for
from gemini import gemini_chat_api_request
from dotenv import load_dotenv
import os
from hashlib import pbkdf2_hmac
from cs50 import SQL
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = './static/uploads'
ALLOWED_EXTENSIONS = {'png', 'jpeg', 'jpg', 'webp', 'gif'}

db = SQL("sqlite:///dbPlantate.sqlite")

ITERATION = 600_000
SALT = os.getenv('SALT_HASH').encode('utf-8')

load_dotenv()

app = Flask(__name__)

app.secret_key = os.getenv('SESSION_KEY').encode('utf-8')

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/")
def index():
    return render_template('home.html')

@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/your-plants", methods=['GET', 'POST'])
def plant_collection():
    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('plant_collection', name=filename))

    return render_template('plants.html')

@app.route("/specific-plant")
def specific():
    return render_template('plant-specific.html')


@app.route("/gemini-doctor")
def gemini_doctor():
    return render_template('gemini-doctor.html')

@app.route("/login", methods=['GET', 'POST'])
def login():
    session.clear()

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
    session.clear()
    
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
