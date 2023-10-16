#!/usr/bin/python3
"""Define File Storage"""

import json


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

    def reload(self):
        """"deserializes the JSON file to object"""


