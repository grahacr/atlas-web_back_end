#!/usr/bin/env python3
'''
module for Session Authentication HTTPS routes
'''
from flask import Flask, request, jsonify
from api.v1.views import app_views
from os import getenv


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def session_login() -> str:
    '''
    POST route for session login
    session_login function takes no arguments
    handles routes for the session authentication
    '''

    from api.v1.app import auth
    from api.v1.views.users import User

    email = request.form.get('email')
    password = request.form.get('password')

    if email is None:
        return jsonify({"error": "email missing"}), 400
    if password is None:
        return jsonify({"error": "password missing"}), 400

    users = User.search({'email': email})
    if not users:
        return jsonify({"error": "no user found for this email"}), 404

    first_user = users[0]
    if not first_user.is_valid_password(password):
        return jsonify({"error": "wrong password"}), 401

    session_id = auth.create_session(first_user.id)
    json_user = first_user.to_json()
    
    response = jsonify(json_user)
    cookie = getenv('SESSION_NAME')
    response.set_cookie(cookie, session_id)

    return response
