#!/usr/bin/env python3
"""auth module
"""
import bcrypt
from db import DB
import uuid
from user import User
from sqlalchemy.orm.exc import NoResultFound


def _generate_uuid() -> str:
    new_uuid = uuid.uuid4()
    return str(new_uuid)

def _hash_password(password: str) -> bytes:
    '''

    '''
    password_bytes = password.encode()
    hashed = bcrypt.hashpw(password_bytes, bcrypt.gensalt())
    return hashed


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        '''
        register_user method takes 3 args:
        - self
        - email (string)
        - password (string)
        Return: User (newly registered in db)
        '''
        try:
            self._db.find_user_by(email=email)
            raise ValueError(f'User {email} already exists')
        except NoResultFound:
            hashed_password = _hash_password(password)
            registered_user = self._db.add_user(email, hashed_password)
            return registered_user

    def valid_login(self, email: str, password: str) -> bool:
        try:
            user = self._db.find_user_by(email=email)
            if bcrypt.checkpw(password.encode(), user.hashed_password):
                return True
            return False
        except Exception as e:
            return False
