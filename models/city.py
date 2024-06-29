#!/usr/bin/python3
"""Defines a class <City>."""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models.place import Place


class City(BaseModel, Base):
    """A class <City> that inherits from <BaseModel>.

    Public class attributes:
        state_id (str): The <id> of a state.
        name (str): Name of the city.
    """
    __tablename__ = "cities"

    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
    places = relationship("Place", cascade="all, delete, delete-orphan",
                          backref="cities")
