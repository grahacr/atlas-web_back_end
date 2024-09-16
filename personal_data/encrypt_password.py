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
