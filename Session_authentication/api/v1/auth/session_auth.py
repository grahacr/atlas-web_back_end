#!/usr/bin/env python3
'''
module for Session Authentication
'''
from api.v1.auth.auth import Auth
from flask import request
from typing import TypeVar, Tuple
import base64
from models.user import User
from models.base import Base


class SessionAuth(Auth):
    pass