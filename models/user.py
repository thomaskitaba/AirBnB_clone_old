#!/usr/bin/python3
""" base_model """
from models import BaseModel



class User(BaseModel):
    """ User class that inherits from BaseModel: """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
