#!/usr/bin/python3
""" this model define class user """
from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy import Column, String
from models.city import City
from sqlalchemy.orm import relationship
from os import getenv
import models


class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    __tablename__ = "users"
    email = Column(string(128), nullable=False)
    password = Column(string(128), nullable=False)
    first_name = Column(string(128), nullable=False)
    last_name = Column(string(128), nullable=False)
