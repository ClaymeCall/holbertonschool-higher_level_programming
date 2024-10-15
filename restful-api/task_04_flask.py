#!/usr/bin/python3

from flask import Flask, request, jsonify
'''
Simple Flask API with the following endpoints:
- GET /: returns a welcome message.
- GET /data: returns the list of usernames.
- GET /status: returns the status of the API.
- GET /users/<username>: returns the profile of a user.
- POST /add_user: adds a new user to the API.
'''
app = Flask(__name__)

users = {}


@app.route("/")
def home():
    '''
    Root of the api, returns a welcome message
    '''
    return "Welcome to the Flask API!"

@app.route("/data")
def get_usernames():
    '''
    Returns the list of all usernames in user database.
    '''
    return jsonify(list(users.keys()))

@app.route("/status")
def get_status():
    '''
    Returns the status of the API.
    '''
    return "OK"

@app.route("/users/<username>")
def get_user_info(username):
    '''
    Returns the data of a certain user.
    '''
    if not users.get(username):
        return jsonify({"error": "User not found"}), 404
    else:
        return users.get(username)

@app.route("/add_user", methods=["POST"])
def return_user_info(username):
    '''
    Adds a new user to the database.
    '''
    new_user = request.get_json()
    username = new_user.get('username')

    if not username:
        return jsonify({"error": "Username is required"}), 400
    else:
        users[username] = new_user
        return jsonify({"message": "User added", "user": new_user}), 201


if __name__ == "__main__":
    app.run(debug=True)
