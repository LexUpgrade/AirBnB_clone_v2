#!/usr/bin/python3
"""Defines a Detabase Engine."""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from os import getenv
from models.base_model import Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class DBStorage:
    """SQLAlchemy Database Engine."""
    __engine = None
    __session = None

    def __init__(self):
        """Instantiates the engine."""
        uri = "mysql+mysqldb://{}:{}@{}/{}".format(getenv('HBNB_MYSQL_USER'),
                                                   getenv('HBNB_MYSQL_PWD'),
                                                   getenv('HBNB_MYSQL_HOST'),
                                                   getenv('HBNB_MYSQL_DB'))
        self.__engine = create_engine(uri, pool_pre_ping=True)

        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
            Queries the current database session of all objects depending of
            <cls> name.
        """
        objs = list()
        if cls:
            if type(cls) is str:
                cls = eval(cls)
            objs = self.__session.query(cls).all()
        else:
            cls_list = [State, City, Place, User]
            for cls_ in cls_list:
                objs.extend(self.__session.query(cls_).all())

        result_dict = dict()
        for obj in objs:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            result_dict[key] = obj
        return result_dict

    def new(self, obj):
        """Adds the new object <obj> to the current database session."""
        self.__session.add(obj)

    def save(self):
        """Commits all changes of the current database."""
        self.__session.commit()

    def delete(self, obj=None):
        """Deletes from the current database session <obj> if specified."""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """
            Create all tables in the database and activates the current
            database session.
        """
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()
