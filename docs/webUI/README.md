# 0. Getting your firebase credentials: 

1. Login into firebase console. Create a new project if you haven't already. On the top left, you can find the settings button right next to `Project Overview`. Click on that and goto `Project Settings`.

2. Under `Project Settings`, select `Service Accounts`
3. Under `Service Accounts`, click on Generate new private key.

4. Download the resulting JSON file, rename it to `data-key.json` and place it under the root of the webUI folder inside src. 

### Database Setup: 

In firebase, you need two kinds of Databases: Firestore and Realtime database. Firestore database has 3 documents: `camera_info`, `history` and `users`. Add users who need to access the website under the `users` document. Each item in the `users` document contains three fields: `username`, `password` and `usertype`. The `usertype` value can be set either to `forest_officer` or `operator` depending on the user's role. 

The `history` document contains previous instances of the poacher being detected. The `camera_info` document contains the location where the cameras are installed. 

# 1. Setting Up the environment 

Install the required dependencies by running the following: 

```
pip install -r requirements.txt
```
The file is located inside `src/webUI`
 
Then, open the `.env.sample` file, and set the `REALTIME_DB` variable. This variable refers to the realtime DB the ESP32 uses for communication. 

# 2. Running the webUI:

Run `python app.py`. Then open a browser and goto `localhost:5000` and access the UI. 