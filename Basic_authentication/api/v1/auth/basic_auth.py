#!/usr/bin/env python3
'''
module for Basic Authentication
'''
from api.v1.auth.auth import Auth
from flask import request
from typing import TypeVar


class BasicAuth(Auth):
    '''
    BasicAuth class inherits from Auth
    '''