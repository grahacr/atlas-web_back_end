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
    def extract_base64_authorization_header(self, authorization_header: str) -> str:
        '''
        function extracts basic authorization header
        takes 2 args:
        - self
        - authorization_header (string)
        return: string representing basic auth header
        '''
        if authorization_header is None:
            return None
        if not isinstance(authorization_header, str):
            return None
        if authorization_header.startswith('Basic '):
            return authorization_header[6:]
        return None
