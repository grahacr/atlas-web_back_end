#!/usr/bin/env python3
'''
simple flask app for welcome message
'''

from flask import Flask, jsonify, request
from auth import Auth

app = Flask(__name__)
AUTH = Auth()


@app.route('/', methods=['GET'])
def hello():
    '''
    simple app route with GET method, no args
    return jsonified welcome message
    '''
    return jsonify({'message': 'Bienvenue'})


@app.route('/users', methods=['POST'])
def users():
    email = request.form['email']
    password = request.form['password']
    try:
        user = AUTH.register_user(email, password)
        return jsonify({"email": "<registered email>",
                        "message": "user created"})
    except Exception as e:
        return jsonify({"message": "email already registered"}), 400


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")
