#!/usr/bin/env python3
"""DB module
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.exc import NoResultFound, 
from sqlalchemy.orm.session import Session

from user import Base, User


class DB:
    """DB class
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db", echo=True)
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
        """Add User to DB

        Args:
            email (str): email
            hashed_password (str): hashed password

        Returns:
            User: user
        """
        user = User(email=email, hashed_password=hashed_password)
        self._session.add(user)
        return user
    
    def find_user_by(self, **kwargs) -> User:
        """Find a user by a field name

        Returns:
            User: User object
        """

        try:
            user = self._session.query(User).filter_by(**kwargs)
        except NotFo
