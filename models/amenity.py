#!/usr/bin/python3
"""Defines a class <Amenity>."""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.place import place_amenity


class Amenity(BaseModel, Base):
    """A class <Amenity> that inherits from <BaseModel>.

    Public class attribute:
        name (str): ...
    """
    __tablename__ = "amenities"

    name = Column(String(128), nullable=False)
    place_amenities = relationship("Place", secondary=place_amenity)
