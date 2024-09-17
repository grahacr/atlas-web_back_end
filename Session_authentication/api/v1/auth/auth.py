#!/usr/bin/env python3
'''
module for Authentication
'''

from flask import request
from typing import List, TypeVar
import os


class Auth():
    '''
    Authentication class contains functions for
    Authentication
    '''
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        '''
        require_auth function takes 3 args:
        - self
        - path (string)
        - excluded_paths (list of strings)
        Return: boolean depending on if authentication is necessary
        '''
        if path is None:
            return True
        if excluded_paths is None or not excluded_paths:
            return True
        equalized_path = path.rstrip('/') + '/'
        equalized_excluded_path = ([route.rstrip('/') + '/'
                                    for route in excluded_paths])
        for route in equalized_excluded_path:
            if equalized_path.startswith(route):
                return False

        return True

    def authorization_header(self, request=None) -> str:
        '''
        authorization_header takes 2 args:
        - self
        - request (default value = None)
        Return: string
        '''
        if request is None:
            return None
        return request.headers.get('Authorization', None)

    def current_user(self, request=None) -> TypeVar('User'):
        '''
        current user function takes 2 args:
        - self
        - request (default value = None)
        Return: Type ('user')
        '''
        return None
    
    def session_cookie(self, request=None) -> str:
        '''
        session_cookie instance method takes 2 args:
        - self
        - request (default value = none)
        Return: string representing cookie value
        '''
        if request is None:
            return None
        session_name = os.getenv('SESSION_NAME', '_my_session_id')
        cookie_value = request.cookies.get(session_name)
        return cookie_value
