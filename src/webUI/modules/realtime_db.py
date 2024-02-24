import firebase_admin
from firebase_admin import credentials, db
from dotenv import load_dotenv
import os


load_dotenv()


def return_data():


    cred = credentials.Certificate("data-key.json")
    app2 = firebase_admin.initialize_app(cred, {'databaseURL': os.getenv("REALTIME_DB")}, name="app2")

    ref = db.reference("/", app=app2)

    data = ref.get()

    return data

