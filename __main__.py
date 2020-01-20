from flask import Flask, session, request
import requests
import os
import pyrebase

app = Flask(__name__)
app.config["DEBUG"] = True

#TODO: Remember to hide the api_key into a secret file (.env)
config = {
    "apiKey": "AIzaSyBJz6F8xTaz6V09A4cJYZtYXhEEwQKfyfY",
    "authDomain": "solarplane-491a7.firebaseapp.com",
    "databaseURL": "https://solarplane-491a7.firebaseio.com",
    "projectId": "solarplane-491a7",
    "storageBucket": "solarplane-491a7.appspot.com",
    "messagingSenderId": "996854836265",
    "appId": "1:996854836265:web:8d9f8d16e0b37ca77f4038",
    "measurementId": "G-48GG4FD671"
}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
db = firebase.database()

@app.route('/', methods=['GET'])
def welcome():
    return "The server is live. This is a project by Alessandro Gregolin and Lorenzo Lucatello"

@app.route('/signup', methods=["POST", "GET"])
def createUser():
    message = ""
    try:
        print(session['usr'])
        return "The user is already logged in"
    except KeyError:
        if request.method == "POST":
            data = request.get_json(force=True)
            email = data.userEmail
            password = data.userPassword
            try:
                user = auth.create_user_with_email_and_password(email, password)
                user = auth.refresh(user['refreshToken'])
                user_id = user['idToken']
                session['usr'] = user_id
                return "The user has been successfully created" #Now redirect the user to the page
            except:
                message = "Something went wrong"
                return "Something went wrong"
        return "No data was passed in the method for the user log in"

@app.route('/login', methods=["POST", "GET"])
def login():
    message = ""
    try:
        print(session['usr'])
        return "The user is already logged in"
    except KeyError:
        if request.method == "POST":
            data = request.get_json()
            email = data.userEmail
            password = data.userPassword
            try:
                user = auth.sign_in_with_email_and_password(email, password)
                user = auth.refresh(user['refreshToken'])
                user_id = user['idToken']
                session['usr'] = user_id
                return "The user has been successfully logged in"
            except:
                message = "Incorrect Password!"
        return "No data was passed in the method for the user log in"


@app.route('/admin')
def admin():
    try:
        print(session['usr'])
        return "The user is logged in, let him access the page"
    except:
        return "The user is not logged in, no access to the page"

if __name__ == '__main__':
    app.run()

