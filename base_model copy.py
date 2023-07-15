#!/usr/bin/python3
""" base_model """
import uuid
from models import storage
from datetime import datetime


class BaseModel:
    """ BaseModel class """
    def __init__(self, *args, **kwargs):
        t_format = "%Y-%d-%mT%H:%M:%S.%f"
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if len(kwargs) != 0:
            for key, val in kwargs.items():
                if kwargs[key] == "created_at":
                    self.created_at = datetime.strptime(val, t_format)
                elif kwargs[key] == "updated_at":
                    self.updated_at = datetime.strptime(val, t_format)
                elif kwargs[key] == "id":
                    self.id = val
        else:
            storage.new(self)

    def __str__(self):
        """ __str__ """
        c_name = self.__class__.__name__
        id = self.id
        dict = self.__dict__
        return ("[{}] ({}) <{}>".format(c_name, id, dict))

    def save(self):
        """ save """
        self.updated_at = datetime.now()
    def to_dict(self):
        """Return the dictionary representation of a Rectangle."""
        t_format = "%Y-%m-%dT%H:%M:%S.%f"
        return {
            "id": self.id,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
            "__class__": self.__class__.__name__
        }
