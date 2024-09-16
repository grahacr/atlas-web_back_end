#!/usr/bin/env python3
'''
module for handling passwords and their encryption
'''
import bcrypt


def hash_password(password: str) -> bytes:
    '''
    hash_password takes 1 argument:
    - password (a string)
    Returns:
    byte string (salted, hashed password)
    '''
    password_bytes = password.encode()
    hashed = bcrypt.hashpw(password_bytes, bcrypt.gensalt())
    return hashed


def is_valid(hashed_password: bytes, password: str) -> bool:
    '''
    is_valid function takes 2 args:
    - hashed_password (bytes)
    - password (string)
    Returns: boolean on password validity
    function encodes password to bytes and uses checkpw to
    validate it against hashed_password
    '''
    password_bytes = password.encode()
    return bcrypt.checkpw(password_bytes, hashed_password)
