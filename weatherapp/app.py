from flask import Flask, make_response, jsonify, request, render_template, redirect, url_for, session
from flask_mysqldb import MySQL
from functools import wraps
from weather import getWeather
import requests
import config as cfg
import os
import json
from logs import logger
config = cfg.get_config()

logger.info(f'Configuration loaded from S3: {config}')


app = Flask(__name__)

app.secret_key = os.urandom(24)

# MySQL configurations
app.config['MYSQL_HOST'] = config['db']['host']
app.config['MYSQL_USER'] = config['db']['user']
app.config['MYSQL_PASSWORD'] = config['db']['password']
app.config['MYSQL_DB'] = config['db']['database']
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

mysql = MySQL(app)


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user' not in session:
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function


def get_suggestion(context):
    url = config['suggestion_app']  
    headers = {
        'Content-Type': 'application/json'
    }
    data = {
        "context": context
    }
    response = requests.post(url, headers=headers, json=data)
    return response.json()['answer']  

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        birth_date = request.form['birthday']
        email = request.form['email']
        state = request.form['state']

        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO Users(username, password, email, birth_date, state) VALUES (%s, %s, %s, %s, %s)", 
                    (username, password, email, birth_date, state))
        mysql.connection.commit()
        cur.close()
        return redirect(url_for('login'))
    
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM Users WHERE username = %s", [username])
        user = cur.fetchone()
        cur.close()
        
        if user and user['password'] == password:
            session['user'] = username
            return redirect(url_for('main'))
        else:
            return 'Login Failed'
        
    return render_template('login.html')  
    
    
@app.route('/health', methods=['GET'])
def healthcheck():
    return make_response(jsonify({'status': 'healthy'}), 200)

@app.route('/', methods=['GET'])
@login_required
def main():
    return app.send_static_file('main.html')

@app.route('/<filename>', methods=['GET'])
def static_files(filename):
    return app.send_static_file(filename)

@login_required
@app.route('/get_weather', methods=['GET'])
def get_weather():
    zip = request.args.get('zip')
    weather = getWeather(zip)
    context = weather.verbal_weather()
    # answer = get_suggestion(context)
    answer = 'no model yet available'
    report = weather.weather_report()
    report['suggestion'] = answer
    
    # Store the weather response in the Requests table
    weather_response = json.dumps(report)    
    user_name = session.get('user')
    cur = mysql.connection.cursor()
    cur.execute("SELECT user_id FROM Users WHERE username = %s", [user_name])
    user_id = cur.fetchone()['user_id']

    cur.execute("INSERT INTO Requests (user_id, zip_code, weather_response) VALUES (%s, %s, %s)", 
                (user_id, zip, weather_response))
    mysql.connection.commit()
    
    return jsonify(report)

@app.route('/history', methods=['GET'])
@login_required
def history():
    user_name = session.get('user')
    
    cur = mysql.connection.cursor()
    cur.execute("SELECT user_id FROM Users WHERE username = %s", [user_name])
    user_id = cur.fetchone()['user_id']
    
    cur.execute("SELECT * FROM Requests WHERE user_id = %s", [user_id])
    requests = cur.fetchall()
    cur.close()
    
    return render_template('history.html', requests=requests)


app.run(debug=True, host="0.0.0.0", port="8080")

    
    