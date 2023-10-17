#!/usr/bin/python3
"""Define File Storage"""

import json
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State


class FileStorage():
    """Creating a class"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return object"""
        return self.__objects

    def new(self, obj):
        """ add new obj"""
        key = F"{obj.__class__.__name__} {obj.id}"
        self.__objects[key] = obj

    def save(self):
        """serializes objects to the JSON file"""
        dicobj = {}
        for key, obj in FileStorage.__object.items():
            dicobj[key] = obj.to_dict()
            with open(FileStorage.__filePath, "w") as f:
                dump(dicobj, f)

    def reload(self):
        """"deserializes the JSON file to object"""
        try:
            with open(FileStorage.__filePath, "r") as f:
                deserialized_obj = load(f)
                for key, value in deserialized_obj.items():
                    FileStorage.__objects[key] = eval(
                            value["__class__"])(**value)
        except FileNotFoundError:
            return



