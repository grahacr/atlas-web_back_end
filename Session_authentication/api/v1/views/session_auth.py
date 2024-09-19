#!/usr/bin/env python3
'''
module for Session Authentication
'''
from flask import Flask, request, jsonify
from api.v1.views import app_views


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def session_login() -> str:
    
    from api.v1.app import auth

    email = request.form.get('email')
    password = request.form.get('password')

    if email is None:
        return jsonify({"error": "email missing"}), 400
    if password is None:
        return jsonify({"error: password missing"}), 400
    from api.v1.views.users import User
    users = User.search({'email': email})
    if not users:
        return jsonify({"error: no user found for this email"}), 404
    
    user = users[0]
    