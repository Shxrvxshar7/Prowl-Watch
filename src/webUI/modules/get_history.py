import firebase_admin
from firebase_admin import credentials, firestore
import datetime

cred = credentials.Certificate("data-key.json")
appx = firebase_admin.initialize_app(cred, name="appx")
db = firestore.client(app=appx)

def get_data(val):
    

    hist_coll = db.collection('history')

    cam_coll = db.collection("camera_info")

    cam_info2 = sorted(hist_coll.stream(), key=lambda x: x.to_dict()["Time"], reverse=True)

    my_items = []

    for item in cam_info2:
        x = item.to_dict()
        cam_no = x['Camera']
        query = cam_coll.where('cameraNumber', '==', str(cam_no)).get()
        dd = query[0].to_dict()

        ss = dd['latitude'] + ", " + dd['longitude']
        x['location'] = ss

        unixtime = x['Time']


        x['Date'] = str(datetime.datetime.fromtimestamp(int(unixtime)).date())
        x['Time'] = str(datetime.datetime.fromtimestamp(int(unixtime)).time())


        my_items.append(x)

    if val==1:
        return my_items[:10] if len(my_items) >= 10 else my_items, len(cam_coll.get()), my_items[0]['Date'] + ', ' + my_items[0]['Time'], len(cam_info2)
    
    return my_items
    
