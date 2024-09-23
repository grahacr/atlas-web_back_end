#!/usr/bin/env python3
"""auth module
"""
import bcrypt


def _hash_password(password: str) -> bytes:
    '''

    '''
    password_bytes = password.encode()
    hashed = bcrypt.hashpw(password_bytes, bcrypt.gensalt())
    return hashed
