#!/usr/bin/python3
"""Defines a class <Place>."""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship


class Place(BaseModel, Base):
    """A class <Place> that inherits from <BaseModel>.

    Public class attributes:
        city_id (str): ID of the city
        user_id (str): ID of the user
        name (str): Name of the place
        description (str): Short description of the place
        number_of_rooms (int): Number of rooms
        number_bathrooms (int): Number of bathrooms
        max_guest (int): Max occupants
        price_by_night (int): Rate
        latitude (float): Latitude
        longitude (float): Longitude
        amenity_ids (list): ...
    """
    __tablename__ = "places"

    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float)
    longitude = Column(Float)
    amenity_ids = list()
