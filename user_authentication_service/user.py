#!/usr/bin/env python3
'''
model for User model using sqlalchemy and
declarative base mapping
'''
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class User(Base):
    '''
    model for User ineriting from Base(Declarative base)
    with column attributes mapped to table
    '''
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    email = Column(String(250), nullable=False)
    hashed_password = Column(String(250), nullable=False)
    session_id = Column(String(250))
    reset_token = Column(String(250))
