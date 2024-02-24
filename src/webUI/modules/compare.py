import firebase_admin
from firebase_admin import credentials, firestore
from dotenv import load_dotenv
from modules.realtime_db import return_data
import datetime

load_dotenv()


cred = credentials.Certificate("data-key.json")
app1 = firebase_admin.initialize_app(cred, name="app1")
db = firestore.client(app=app1)

def check_and_update():


    cam_info = db.collection("history")

    cam_info2 = sorted(cam_info.stream(), key=lambda x: x.to_dict()["Time"], reverse=True)

    top_time = cam_info2[0].to_dict()["Time"]




    data = return_data()

    time = int(data['Time']/1000)

    if(int(time) - int(top_time) > 0):
        cam_info.document(str(time)).set({
            "Camera": data['Camera'], 
            "Time": str(data['Time']), 
            "Persons": data['Persons']
        })