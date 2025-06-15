from flask import Flask, request, render_template
from datetime import datetime

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
import os
load_dotenv()

uri = os.getenv('uri')

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

db = client.test
collection = db['flask-Signup']
app = Flask(__name__)

@app.route("/")
def home():
    current_date = datetime.now()
   
    format = current_date.strftime('%B %d')
    # print(format)
    day_of_week = current_date.strftime('%A')
    # print(day_of_week)
    time = current_date.strftime('%I:%M %p')
    # print(time)
    return render_template('index.html',date=format,dow = day_of_week,time=time)

@app.route("/submit",methods=["POST"])
def submit():
    form_data = dict(request.form)
    collection.insert_one(form_data)
    return render_template('submit.html')

if __name__== '__main__':
    app.run(debug=True)





