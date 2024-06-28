#!/usr/bin/python3
"""Defines a base class <BaseModel>."""
from uuid import uuid4
from datetime import datetime
import models
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class BaseModel:
    """Defines all common attributes/methods for other classes to inherit."""

    id = Column(String(60), unique=True, nullable=False, primary_key=True)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """Instantiates an object of <BaseModel>.

        Args:
            args (list): **WILL NEVER BE USE**.
            kwarg (dict): key/word arguement from  json file for instantiation.
        """
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if len(kwargs) != 0:
            for k in kwargs.keys():
                if k != '__class__':
                    if k in ['created_at', 'updated_at']:
                        setattr(self, k, datetime.fromisoformat(kwargs[k]))
                    else:
                        setattr(self, k, kwargs[k])

    def __str__(self):
        """Prints information of a <BaseModel> instance."""
        return f"[{self.__class__.__name__}] ({self.id}) {self.to_dict()}"

    def save(self):
        """Updates the public instance attribute <updated_at> with
        the current datetime. And updates the JSON file 'file.json'.
        """
        self.updated_at = datetime.today()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """Returns a dictionary containing all keys/values of
        <BaseModel> instance.
        """
        del_ = '_sa_instance_state'

        obj_dict = dict(self.__dict__)
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        if del_ in obj_dict.keys():
            del obj_dict[del_]
        return obj_dict

    def delete(self):
        """Deletes the current instance from the storage."""
        models.storage.delete(self)
