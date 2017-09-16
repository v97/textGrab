#import requests
#from firebase import firebase

databaseURL = 'https://test-764cc.firebaseio.com/'

def getURL(relPath):
    return baseURL + relPath + '.json/'

def getFromDB(relPath):
    return requests.get(getURL('')).json()

#def putOnDB(relPath, item):
#print(getFromDB(''))

#strx = getURL('test')
#print(strx)
#data = {"test":3}
#r = requests.put(strx, data = data)

import pyrebase

config = {
  "apiKey": "AIzaSyCF_fwONZiVRr1s1jrVi7CzoXz-R1yKTj8",
  "authDomain": "projectId.firebaseapp.com",
  "databaseURL": databaseURL,
  "storageBucket": "test-764cc.appspot.com",
}

firebase = pyrebase.initialize_app(config)

storage = firebase.storage()

storage.child("images/example.jpg").put("canada.jpg")

#db = firebase.FirebaseApplication(baseURL)
#db.put('', 'testval', 1)

#r.status_code
#r.headers['content-type']
#r.encoding
#r.text