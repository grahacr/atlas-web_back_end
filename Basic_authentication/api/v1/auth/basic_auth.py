#!/usr/bin/env python3
'''
module for Basic Authentication
'''
from api.v1.auth.auth import Auth
from flask import request
from typing import TypeVar, Tuple
import base64
from models.user import User
from models.base import Base


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

    def extract_user_credentials(self,
                                 decoded_base64_authorization_header:
                                 str) -> Tuple[str, str]:
        '''
        extract_user_credentials takes 2 args:
        - self
        - decoded_base64_authorization_header (String)
        Return: Tuple [string, string] representing user credentials
        '''
        if (decoded_base64_authorization_header is None or
            type(decoded_base64_authorization_header) is not str or
            ':' not in decoded_base64_authorization_header):
            return (None, None)
        separated = decoded_base64_authorization_header.split(':')
        return (separated[0], separated[1])

    def user_object_from_credentials(self, user_email: str,
                                     user_pwd: str) -> TypeVar('User'):
        '''
        user_object_from_credentials method takes 3 args:
        - self
        - user_email (String)
        - user_pwd (string)
        Return: User instance that matches email and pw
        '''
        if user_email is None and not isinstance(user_email, str):
            return None
        if user_pwd is None and not isinstance(user_pwd, str):
            return None

        try:
            users = User.search({'email': user_email})
            if not users:
                return None
            for user in users:
                if user.is_valid_password(user_pwd):
                    return user

        except Exception:
            return None

    def current_user(self, request=None) -> TypeVar('User'):
        '''
        current user method takes 2 args:
        - self
        - request (Default = none)
        Return:
        User instance object
        '''
        if request is None:
            return None
        authorized_header = self.authorization_header(request)
        if authorized_header is None:
            return None

        base64_header = self.extract_base64_authorization_header(authorized_header)
        if base64_header is None:
            return None

        decoded_header = self.decode_base64_authorization_header(base64_header)
        if decoded_header is None:
            return None

        user_cred = self.extract_user_credentials(decoded_header)
        if user_cred[0] is None or user_cred[1] is None:
            return None

        return self.user_object_from_credentials(user_cred)
