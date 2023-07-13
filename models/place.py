#!/usr/bin/python3
from models.base_model import BaseModel
""" Place sub classes of BaseModel """


class Place(BaseModel):
    """ Place """
    city_id = ""  # string - empty string: it will be the City.id
    user_id = ""  # string - empty string: it will be the User.id
    name = ""    # string - empty string
    description = ""    # string - empty string
    number_rooms = 0    # integer - 0
    number_bathrooms = 0    # integer - 0
    max_guest = 0    # integer - 0
    price_by_night = 0    # integer - 0
    latitude = 0    # integer - 0
    longitude = 0    # integer - 0
    amenity_ids = []  # list of string - e
