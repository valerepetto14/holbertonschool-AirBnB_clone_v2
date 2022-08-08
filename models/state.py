#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime


class State(BaseModel, Base):
    """ State class """
    # creamos la tabla "states" la clase City va a estar asociada a esta tabla
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
