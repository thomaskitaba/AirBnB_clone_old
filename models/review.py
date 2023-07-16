#!/usr/bin/python3
""" Review sub classes of BaseModel """

from models.base_model import BaseModel


class Review(BaseModel):
    """ Review """

    place_id = ""   # string - empty string: it will be the Place.id
    user_id = ""    # string - empty string: it will be the User.id
    text = ""   # string - empty string
