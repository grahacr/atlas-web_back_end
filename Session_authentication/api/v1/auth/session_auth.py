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
import uuid


class SessionAuth(Auth):
    '''
    class SessionAuth inherits from Auth class
    session authentication mechanism
    '''
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        '''
        create_session instance method takes 2 args:
        - self
        - user_id (string, default = none)
        Return: string representing session id
        '''
        if user_id is None or type(user_id) is not str:
            return None
        session_id = str(uuid.uuid4())
        self.user_id_by_session_id.update({session_id: user_id})
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        '''
        instance method takes 2 args:
        - self
        - session_id (string, default = None)
        Return: string representing user id
        that is associated with session id
        '''
        if session_id is None or type(session_id) is not str:
            return None
        user = self.user_id_by_session_id.get(session_id)
        return user
