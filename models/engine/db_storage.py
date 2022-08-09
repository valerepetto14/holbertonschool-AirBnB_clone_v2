#!/usr/bin/python3
"""define DBStorage"""
from os import getenv
from models.base_model import Base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)


class DBStorage:
    """def class DBStorage engine for database like mysql"""
    __engine = None
    __session = None
    def __init__(self)
        """def method init that initialized an objetc of DBStorage"""
        env = getenv("HBNB_ENV")
        userDB = getenv("HBNB_MYSQL_USER")
        passwordDB = getenv("HBNB_MYSQL_PWD")
        hostDB = getenv("HBNB_MYSQL_HOST")
        database = getenv("HBNB_MYSQL_DB")
        self.__engine = engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                           .format(userDB, passwordDB, hostDB,
                                   database), pool_pre_ping=True)
        if env == "test":
            Base.metadata.drop_all(self.__engine)
            
    def all(self, cls=None):
        """def method all that return all objetc depending of the class name"""
        dic_return = {}
        id = ""
        value = ""
        Session = sessionmaker(bind=engine)
        session = Session()
        clases = ["User", "State", "City", "Amenity", "Place" ,"Review"]
        if cls is None:
            for class in clases:
                data = session.query(class).all()
                for obj in data:
                    id = f"{obj.__class__}.{obj.id}"
                    value = obj
                    dic_return(id) = value
    
    def new(self, obj):
        """add the object to the current database session"""

    def save(self):
        """commit all changes of the current database session"""

    delete(self, obj=None):
        """delete from the current database session obj if not None"""
    
    reload(self):
        """method create"""

