#!/usr/bin/python3
"""Defines a class <User."""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.place import Place


class User(BaseModel, Base):
    """A <User> class that inherits from <BaseModel>.

    Class Public Attributes:
        email (str): Email of the user
        password (str): Password of the user
        first_name (str): Optional first_name of the user
        last_name (str): Optional last_name of the user
    """
    __tablename__ = "users"

    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128))
    last_name = Column(String(128))
    places = relationship("Place", cascade="all, delete, delete-orphan",
                          backref="user")
