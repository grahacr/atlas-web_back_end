#!/usr/bin/env python3
"""DB module
"""
import bcrypt
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import InvalidRequestError
from typing import TypeVar
from user import User, Base


class DB:
    """DB class
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db", echo=False)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        '''
        add_user method takes 3 args:
        - self
        - email (string)
        - hashed_password (string)
        Returns: Instance of User
        adds user to the session/database
        '''
        new_user = User(email=email, hashed_password=hashed_password)
        self._session.add(new_user)
        self._session.commit()
        return new_user

    def find_user_by(self, **kwargs) -> User:
        '''
        find_user_by method takes arbritrary arguments
        - kwargs
        Returns: User from table by filtering
        using kwargs keywords
        '''
        try:
            user = self._session.query(User).filter_by(**kwargs).one()
        except NoResultFound:
            raise NoResultFound
        except Exception as e:
            raise InvalidRequestError
        return user

    def update_user(self, user_id: int, **kwargs) -> None:
        '''
        update_user method takes at least 3 args:
        - self
        - user_id (integer representing user)
        - **kwargs (any number of args representing attributes)
        Return: None. Only updating user attributes
        '''
        update_user = self.find_user_by(id=user_id)
        for key, value in kwargs.items():
            if not hasattr(update_user, key):
                raise ValueError()
            setattr(update_user, key, value)
            self.__session.commit()
