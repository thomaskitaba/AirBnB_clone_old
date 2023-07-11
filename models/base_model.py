#!/usr/bin/python3
""" base_model """
import uuid
from datetime import datetime


class BaseModel:
    """ BaseModel class """
    def __init__(self, *args, **kwargs):

        self.id = str(uuid.uuid4())
        self.created_at = datetime.now().isoformat()
        self.updated_at = datetime.now().isoformat()

    def __str__(self):
        """ __str__ """
        c_name = self.__class__.__name__
        id = self.id
        dict = self.__dict__
        return ("[{}] ({}) <{}>".format(c_name, id, dict))

    def save(self):
        """ save """
        self.updated_at = datetime.now().isoformat()

    def to_dict(self):
        """Return the dictionary representation of a Rectangle."""
        t_format = "%Y-%m-%dT%H:%M:%S.%f"
        return {
            "id": self.id,
            "created_at": datetime.strptime(self.created_at, t_format).isoformat(),
            "updated_at": datetime.strptime(self.updated_at, "%Y-%m-%dT%H:%M:%S.%f").isoformat(),
            "__class__": self.__class__.__name__
        }
