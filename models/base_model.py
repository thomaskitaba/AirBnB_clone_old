#!/usr/bin/python3
""" base_model """
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """ BaseModel class """

    def __init__(self, created_at, updated_at)
        self.id = str(uuid4())
        self.created_at = datetime.today.isoformat(sep='T', timespec='microseconds')()
        self.updated_at = datetime.today.isoformat(sep='T')
    def save(self):
        """ save """
        pass
    def __str__(self):
        """ __str__ """
        pass

    def to_dict(self):
        """ to_dict """
        pass
