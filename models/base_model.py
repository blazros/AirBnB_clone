#!/usr/bin/python3
"""Defines the BaseModel class."""
import models
from uuid import uuid4
from datetime import datetime

class BaseModel:
    def __init__(self, *args, **kwargs):
        """Initialize a new BaseModel.

        Args:
            *args (any): Unused.
            **kwargs (dict): Key/value pairs of attributes.
        """
        time_form = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.strptime(value, time_form)
                else:
                     self.__dict__[key] = value

    def save(self):
        """Update updated_at with the current datetime."""
        self.updated_at = datetime.today()

    def to_dict(self):
        """ Return the dictionary of the BaseModel instance."""
        dict_cpy = self.__dict__.copy()
        dict_cpy["created_at"] = self.created_at.isoformat()
        dict_cpy["updated_at"] = slef.updated_at.isoformat()
        dict_cpy["__class__"] = self.__class__.__name__
        return dict_cpy

    def __str__(self):
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)
