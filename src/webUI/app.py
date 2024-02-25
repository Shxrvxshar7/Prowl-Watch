from flask import Flask, render_template, request, redirect, url_for, session, flash, get_flashed_messages
import firebase_admin
from firebase_admin import credentials, firestore
from dotenv import load_dotenv
from modules.get_history import get_data
from modules.compare import check_and_update
import threading
import time
import os

load_dotenv()
# Initialize Flask app
app = Flask(__name__)
api_key = os.getenv('API_KEY')
app.secret_key = api_key

# Initialize Firestore DB
cred = credentials.Certificate("data-key.json")
main = firebase_admin.initialize_app(cred, name="main")
db = firestore.client(app=main)


def run_update_check(interval):
    while True:
        check_and_update()
        time.sleep(interval)
    

# Route for login page
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user_type = check_user(username, password)
        print(user_type)
        if user_type == 'forest_officer':
            session['username'] = username
            session['user_type'] = user_type
            return redirect(url_for('index'))
        elif user_type == 'operator':
            session['username'] = username
            session['user_type'] = user_type
            return redirect(url_for('operator_page'))
        else:
            error = 'Invalid credentials. Please try again.'
            print("BAD")
            return render_template('login.html', error=error)
    return render_template('login.html')



# Function to check user credentials and determine user type in Firestore
def check_user(username, password):
    users_ref = db.collection('users').where('username', '==', username).where('password', '==', password)
    print(users_ref)
    user_docs = users_ref.stream()
    for user_doc in user_docs:
        user_data = user_doc.to_dict()
        return user_data.get('usertype', None)
    return None

# Route for forest_officer page
@app.route('/index')
def index():
    if 'username' in session and session['user_type'] == 'forest_officer':
        items, cam_info, last_incident, total_incident = get_data(1)
        return render_template('index.html', data=items, cam_info=cam_info, last_incident=last_incident, total_incident=total_incident)
    else:
        return redirect(url_for('login'))

# Route for operator page
@app.route('/operator_page')
def operator_page():
    if 'username' in session and session['user_type'] == 'operator':
        message = get_flashed_messages()
        return render_template('operator_page.html', message=message)
    else:
        return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session.pop('username', None)
    session.pop('user_type', None)
    return redirect(url_for('login'))


@app.route('/add_camera_info', methods=['POST'])
def add_camera_info():
    cameraNumber = request.form['cameraNumber']
    latitude = request.form['latitude']
    longitude = request.form['longitude']
    piModule = request.form['piModule']
    esp32Module = request.form['esp32Module']

    cam_info = db.collection('camera_info')

    new_camera_doc , doc_id = cam_info.add({
            'cameraNumber': cameraNumber,
            'latitude': latitude,
            'longitude': longitude,
            'piModule': piModule,
            'esp32Module': esp32Module
        })
    if doc_id:
        flash("Successfully added Data")
    else:
        flash("Error Adding Data")
    return redirect(url_for("operator_page"))


@app.route("/reports")
def reports():
    if 'username' in session and session['user_type'] == 'forest_officer':
        return render_template('reports.html', data=get_data(0))
    else:
        return "NOT OK!"

if __name__ == '__main__':

    interval = 30
    thread = threading.Thread(target=run_update_check, args=(interval,))

    thread.daemon = True
    thread.start()



    app.run(debug=True)
