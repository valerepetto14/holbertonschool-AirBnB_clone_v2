#!/usr/bin/python3
"""define FileStorage"""
import json
from models.base_model import BaseModel
from os.path import exists
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import models


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        if cls is not None:
            dic = {}
            for key, value in FileStorage.__objects.items():
                cls_name = key.split(".")
                if cls_name[0] == cls.__name__:
                    dic[key] = value
            return dic
        else:
            return FileStorage.__objects

    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

    def save(self):
        """Saves storage dictionary to file"""
        with open(FileStorage.__file_path, 'w') as f:
            temp = {}
            temp.update(FileStorage.__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, f, indent=4)

    def reload(self):
        """Loads storage dictionary from file"""

        classes = {
                    'BaseModel': BaseModel, 'User': User, 'Place': Place,
                    'State': State, 'City': City, 'Amenity': Amenity,
                    'Review': Review
                  }
        try:
            temp = {}
            with open(FileStorage.__file_path, 'r') as f:
                temp = json.load(f)
                for key, val in temp.items():
                    self.all()[key] = classes[val['__class__']](**val)
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """
        Delete obj from __objects if it’s inside - if obj is equal to None,
        the method should not do anything.
        """
        if obj is None:
            pass
        else:
            # Creamos la key - es el: nombre de la clase + punto + id
            key = f"{obj.__class__.__name__}.{obj.id}"
            if self.__objects[key] is not None:
                del self.__objects[key]
                self.save()
            else:
                pass

    def close(self):
        """def method close"""
        self.reload()
