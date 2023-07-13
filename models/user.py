#!/usr/bin/python3
""" base_model """
import models
import uuid
from datetime import datetime


class User(BaseModel):
    """ User class that inherits from BaseModel: """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
