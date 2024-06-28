#!/usr/bin/python3
"""Defines a class <state>."""
from models.base_model import BaseModel, Base
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models.city import City
import models


class State(BaseModel, Base):
    """A class <State> that inherits from <BaseModel>

    Public class attributes:
        name (str): Name of the state
    """
    __tablename__ = 'states'

    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade="all, delete, delete-orphan",
                          backref="state")

    @property
    def cities(self):
        """
            Serves as a relationship link for 'FileStorage' which returns
            a list of all 'City' instance with their 'state_id' attribute the
            same as 'self.id'.
        """
        my_cities = []
        dict_of_cities = models.storage.all(City)
        for val in dict_of_cities.values():
            if val.state_id == self.id:
                my_cities.append(val)
        return my_cities
