#!/usr/bin/env python3
"""User Table in Flask and SQLAlchemy"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    """User table declaration in SQLAlchemy
    >>> id: int
    >>> email: str
    >>> hashed_password: str
    >>> session_id: str
    >>> reset_token: str
    """

    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    email = Column(String, nullable=False)
    hashed_password = Column(String, nullable=False)
    session_id = Column(String, nullable=True)
    reset_token = Column(String, nullable=True)

    # def __repr__(self):
    #     return f"User<@{self.id} | {self.email}>"
