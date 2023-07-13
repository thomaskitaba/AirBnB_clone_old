#!/usr/bin/python3
""" base_model """
from models.base_model import BaseModel


class User(BaseModel):
    """ User class that inherits from BaseModel: """
    email = ""  # string - empty string
    password = ""  # string - empty string
    first_name = ""  # string - empty string
    last_name = ""  # string - empty string
