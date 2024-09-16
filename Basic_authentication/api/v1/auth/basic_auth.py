#!/usr/bin/env python3
'''
module for Basic Authentication
'''
from api.v1.auth.auth import Auth
from flask import request
from typing import TypeVar
import base64


class BasicAuth(Auth):
    '''
    BasicAuth class inherits from Auth
    '''
    def extract_base64_authorization_header(
            self, authorization_header: str) -> str:
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

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        '''
        decode function takes 2 args:
        - self
        - base64_authorization_header (string)
        Return: string representing decoded header
        '''
        if base64_authorization_header is None:
            return None
        if not isinstance(base64_authorization_header, str):
            return None
        try:
            decoded_str = (base64.b64decode(base64_authorization_header)
                           .decode('utf-8'))
            return decoded_str
        except (base64.binascii.Error, UnicodeDecodeError) as e:
            return None
