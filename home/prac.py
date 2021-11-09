
from firebase import firebase
from requests import post,get
from firebase.firebase import FirebaseApplication, FirebaseAuthentication

import pyrebase 
from pyrebase.pyrebase import Database
import firebase_admin
from firebase_admin import auth ,credentials, db
from datetime import date
from datetime import datetime 
import uuid

config = {    
    "apiKey": "AIzaSyDxtgOS-lNR5iHH-35xjs9r1gIwiLDW6E8",
    "authDomain": "neemeesh-trial.firebaseapp.com",
    "databaseURL": "https://neemeesh-trial-default-rtdb.firebaseio.com",
    "projectId": "neemeesh-trial",
    "storageBucket": "neemeesh-trial.appspot.com",
    "messagingSenderId": "608861234921",
    "appId": "1:608861234921:web:2792a40a8e9cf8611c7278",
    'measurementId': "G-67HDRQV9KN"
}
firebase = pyrebase.initialize_app(config) 
authe = firebase.auth() 
database = firebase.database()
cred = credentials.Certificate('neemeesh-trial-firebase-adminsdk-kl0a5-1cf2f25008.json')
firebase_admin.initialize_app(cred)

firebase=FirebaseApplication("https://neemeesh-trial-default-rtdb.firebaseio.com/", None)
courierusers=list(firebase.get("/Data/Signup/Courier",None).values())
courieruser=[]
couriernames=[]
for courierdetails in courierusers:
    for eachcompkey,eachcompval in courierdetails.items():
        if eachcompkey=='City' and eachcompval == 'Mumbai' :
              
            courieruser.append(courierdetails)
print(courieruser)            
for couriername in courieruser:
    couriernames.append(couriername['Name1'])

print(couriernames)    
