#!/usr/bin/python3
""" this model define class user """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    """
    Class that defines a user with different attributes and the table from
    the database to connect
    """
    __tablename__ = "users"
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)
    # Establish relationship between User and Places
    places = relationship('Place', backref="user", cascade="all ,\
                                delete-orphan")
