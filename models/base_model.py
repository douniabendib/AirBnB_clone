#!/usr/bin/python3
"""define a basse mode"""

from uuid import uuid4
from datetime import datetime
import models



class BaseModel():
    """ Base Class """
    def __init__(self, *args, **kwargs):
        """Intialization of class
        
        Args:
            args: won’t be used
            kwargs:key of this dictionary is an attribute name 
            and value of this dictionary is value of this attribute name
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                elif key in ["created_at", "updated_at"]:
                    value = self.created_at = self.created_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
                setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def save(self):
        """Save function"""
        self.updated_at = datetime.now()
        models.storage.save()

    def __str__(self):
        """String"""
        return F"{[self.__class__.name]} {[self.id]} {[self.__dict__]}"

    def to_dict(self):
        """Dictionary representation"""
        dicformat = self.__dict__.copy()

        dicFormat["id"] = self.id
        dicFormat["__class__"] = self.__class__.__name__
        dicFormat["created_at"] = self.created_at.isoformat()
        dicFormat["updated_at"] = self.updated_at.isoformat()
        return dicFormat
